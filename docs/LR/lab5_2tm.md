---
app_name: Laboratory (LA and LR)
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: 2022-09
doc_type: technical-manual
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-12'
is_base: false
is_change_pages: false
library_max_patch: null
package_id: LR
patch: 553
patch_gap: null
section: ''
source_file: lab5_2tm.docx
status: draft
title: Laboratory
---

# Laboratory

# Technical Manual

<!-- image -->

March 2024

Department of Veterans Affairs (VA)


## Revision History

| Date           | Revised Pages                                                            | Patch Number                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------|--------------------------------------------------------------------------|------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| March 2024     | 257                                                                      | LR*5*2*570                                                 | Corrected wording to be more specific                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| September 2022 |                                                                          | LR*5.2*553                                                 | File #69.73 is removed from Lab and moved to the CPRS OR namespace                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| June 2021      | Title, i,186                                                             | LR*5.2*544                                                 | - Enables the GUI component to the VistA Laboratory Enhancement (VLE) ) Anatomic Pathology (AP) Order Dialog enhancement - Added CPRS LAB TEST (#60) EDIT, Print Laboratory Test CPRS Screen, CPRS AP Dialog Menu, CPRS Dialog Print (#69.71) to Exported Options list - Updated the contents to LR AP DIALOG CONFIG File (#69.73                                                                                                                                                                                                                                                                                              |
| December 2016  | 18, 176, 182, 212, 213, 276                                              | LR*5.2*462  LR*5.2*469  LR*5.2*482  LR*5.2*479  LR*5.2*483 | - Added new file LR AP DIALOG CONFIG (#69.73) and new file LR CPRS PARAMETERS (#69.71) - Added 69.71 LR CPRS PARAMETERS and 69.73 LR AP DIALOG CONFIG to the field list - Added LR CPRS PARAMETERS and LR AP DIALOG CONFIG to the Cross Reference List - Added new section entitled Anatomic Pathology Order Dialog that describes the VistA Laboratory Enhancement (VLE) ) Anatomic Pathology (AP) Order Dialog enhancement - Deleted the Lab Option, **Remove an accession LRDELOG** , which was listed below, Audit of deleted/edited comments - Updated Title page, Revision History, Table of Contents, Index and Footers |
| September 2020 | Title, i, 192, all                                                       | LR*5.2*527                                                 | Liberty ITS;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| October 2019   | Title, 19, 159, 160                                                      | LR*5.2*519                                                 | - Added a **Warning** message and deleted the following Serum write up - Added 4 routines starting at **LRWU8** .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| November 2018  | 31-32                                                                    | LR*5.2*508                                                 | Removed a reference to an obsolete field and changed a reference to a specimen for Mycology and Bacteriology entries in the EXECUTE CODE file (#62.07). Also added an example of DESCRIPTION field (#6) text.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| May 2018       | 31  32, 43-44, 152                                                       | LR*5.2*476                                                 | Added topic to describe batch entry of preliminary comments for accessions.  Added note on FileMan Lab Results reporting, provided description and examples, and added new routine LRFRSLT to Routine Descriptions.                                                                                                                                                                                                                                                                                                                                                                                                            |
| February 2018  | Title page,  Page 186  File List &amp; Descriptions,  Page 170 &amp; 174 | LR*5.2*495                                                 | Allow the entry and editing of the newly created field INACTIVE DATE (#64.9102) in the ETIOLOGY FIELD File (#61.2).  Included two new options for the Labs Microbiology Menu (MIME, and MISE).  Included the MLTF file number and description to the File List section.  Mantech Mission, Solutions and Services  NDS Developer:  NDS Analyst                                                                                                                                                                                                                                                                                  |
| November 2016  | Pages 24, 30                                                             | LR*5.2*465                                                 | This patch enables multidivisional facilities to customize the number of labels required for each site in LABORATORY TEST File (#60) by adding two new fields that can be configured for a specific lab test at a specific facility: The INSTITUTION EXTRA LABELS field (#60.15,.01) and the NUMBER OF LABELS subfield (#60.15,1).                                                                                                                                                                                                                                                                                             |
| October 1994   |                                                                          |                                                            | Initial Version.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |


### 3 Preface

The Laboratory Technical Manual has been designed to provide the Department of Veterans Affairs Medical Center (VAMC), Information Resources Management Service (IRM), and the Laboratory Information Manager (LIM) with the necessary technical information required to efficiently and effectively implement, maintain, and manage Laboratory Version 5.2 software package.

The technical documentation provides sufficient information about the software package for programmers and IRM technical personnel to operate and maintain the software package without additional assistance from package Developers. This Technical Manual was created to fulfill that requirement.

Introduction	1

Purpose	2

Area of Application	2

Organization of Manual	2

Functional Description	2

Functionality	3

Laboratory Module Work Flow	5

Package Specific Notations	6

Implementation and Maintenance	7

System Integrity Checks	8

Check Files for Inconsistencies [LRCHKFILES]	8

Laboratory Package Routine Integrity Menu	11

Lab Routine Integrity Menu	11

[LR Integrity Loop]	12

[LR Integrity Load]	12

[LR Integrity Single]	12

File Editing	13

Other Laboratory Configurable Files	14

Laboratory Files Not to be Edited	16

New Data Names	17

Add a New Data Name Using a Option	17

File Structure/Interaction	18

Editing the Files	20

General Laboratory	21

Laboratory Security Keys	22

Workload Recording	23

Lab Labels	25

Batch Entry of Preliminary Comments for Accessions	27

Microfiche of Path Reports	28

Cumulative Report	29

Further Cumulative Functionality (Version 5.2)	29

TaskManager	34

Device Parameters	35

Initialize LAC Globals &amp; X References [LRAC INITIALIZE]	35

Interim Reports	36

Tasking the Interim	37

Batched Interim	37

FileMan Lab Results Reporting	41

Instrumentation and Interfacing	44

Supervisors/Choosers of Instrumentation	45

Load/Work Lists	46

Instrument Data Flow	47

Automated Instrument Interfacing	49

Automated Instrument Data Flow	50

AUTO INSTRUMENT file (#62.4) Fields List	51

AUTO INSTRUMENT file (#62.4) Fields Description	53

Bidirectional Communications	57

Handshake Routines (Bi-directional)	58

Processing Routine	59

Download Routine	59

Bidirectional Related Fields	60

Version 2 LSI Eprom Installation	62

LSI Wire Wrapping	67

Other LSI Chip Information	69

Wiring Diagrams and Pin Definitions for Automated Instruments	71

Automated Instrument Interface Specifications	71

Automated Instruments Interface	73

Interfacing .i.Pin Definitions	74

LSI .i.Interface Testing	74

Checklist for Instrument Interface	74

Instrument Interface Troubleshooting	75

LAPORTX X Routine	79

LAPX  Routine	79

Instrument Routines	79

^LA &amp; ^LAH Global Descriptions	85

Justification and Descriptions	85

Description of ^LA Global	85

Description of ^LAH Global	85

VAX Example of Device Setup	86

Example of How to Define the .i.Echo Device	89

Bar Code Readers (Blood Bank Module)	90

Bar Code Labels	91

Implementation for the .i.OTC 800 Printer	92

Implementation for .i.Intermec 8646 Printer	94

MicroScan Interface	96

Implementation	96

MicroScan Mainframe Interface Version 19.02 Software	98

The Upload	106

The Download	108

VITEK Interface	110

VITEK Interface Instructions	110

Troubleshooting for VITEK	127

Printout A	130

Printout B	131

Printout C	134

Printout D	135

Printout E	137

Interface Guide for OE/RR Package	139

Routine Descriptions	141

OE/RR Routines	162

Callable Routines	163

Supported References	164

Entry Point References	164

File List and Descriptions	168

File List	169

Brief File Descriptions	171

Exported Options	177

Laboratory Options List	178

Distribution of Menus	189

Menus with .i.Entry or Exit Action	189

Security Keys	190

Individual Module Requirements/Concerns	191

Anatomic Pathology	191

Blood Bank	191

Chemistry/Immunology	191

Microbiology	192

Phlebotomy	192

LRTASK Options	192

Cross References	194

Purging and Archiving	207

Force Cumulative Data to Permanent Page [LRAC FORCE]	208

Purge Old Orders and Accessions [LROC]	210

Archive of LAB DATA file (#63)	211

Archive Options	211

Search for Lab Data to Archive	212

Write Data to Off-Line Media	212

Clear data from the LAR global	212

Read Data from Off-Line Media	212

Purge Data Found in the Search Option	212

Find Patient’s Archived Data	212

Convert Archived LR Data	212

Restore Archived Data to LR Global	212

External Relations	214

External Referenced Files and Fields	215

External Routines	216

External Variables	216

Required Software	216

DBA Integration Agreements	217

Laboratory as a Subscriber	219

Internal Relations	240

Stand Alone Menus	241

Package-wide Variables	243

On-line Documentation	249

File Number Ranges	250

Namespacing	250

Special Templates	250

On-Line Help Using Kernel	250

On-line Help From Your Terminal Screen	251

How To Print Data Dictionaries	252

Global Journaling	253

Mapping Routines	255

Mapping Routines	257

Glossary	268

Appendix A	292

Index	301

INTRODUCTION

## Table of Contents

## Introduction

### 4 Purpose

The purpose of the Laboratory Technical Manual is to provide the Department of Veterans Affairs Medical Center (VAMC), Information Resource Management Service (IRM), and Laboratory Information Manager (LIM) with a technical description of the Lab package setup, special capabilities, files, security, routines, globals, and data dictionaries. Familiarity with the fundamentals of MUMPS, VA FileManager, Laboratory User Manual, Blood Bank User Manual, Anatomic Pathology User Manual, and the Planning and Implementation Guide is assumed.

#### Area of Application

The Laboratory V. 5.2 package covers every functional area of the Clinical Laboratory:

•	Anatomic Pathology	•	Results Reporting

•	Blood Bank	•	Serology

•	Chemistry	•	Surgical Pathology

•	Coagulation	•	Test Accessioning/Ordering

•	Hematology	•	Toxicology

•	Microbiology	•	Urinalysis

•	Phlebotomy	•	Auto Instrument

•	Quality Control	•	Workload Recording

#### Organization of Manual

This manual is organized into major chapters plus an Introduction and a Glossary for the complete guide. The chapters represent functional content areas or issues to be addressed in package implementation and maintenance.

Other manuals relevant to the Laboratory package are:

•	Anatomic Pathology User Manual	VA FileManager Programmer Manual

•	Blood Bank User Manual	Users Guide To Computing

•	Laboratory User Manual	MailMan User Manual

•	Laboratory Technical Manual	Kernel Systems Manual

•	Laboratory Planning and Implementation Guide

•	VA FileManager User Manual

•	Kernel Technical Manual

#### Functional Description

•	What is the Laboratory Package?

The Laboratory package is part of the integrated Decentralized Hospital Computer Program (DHCP) Core Package and a clinically oriented system designed to provide data to health care providers as well as to other health care personnel. Its primary function is to assist the Pathology &amp; Laboratory Medicine Service in managing and automating the workload and reporting process. The Laboratory package includes software for all major functional areas; selected examples of software modules are illustrated in this section.

Who does the Laboratory package serve?

Health Care Providers/Other Health Care Providers:

The Laboratory package is a clinically oriented application, designed to provide data to health care providers as well as to other health care personnel. For this reason, it is a multifaceted package with many spins off advantages for other hospital services. Its primary function is to assist the Pathology &amp; Laboratory Medicine Service in managing and automating workload generated by the Medical Center primary mission.

Who can use the Laboratory Package and for what purpose?

The Health Care Provider:

The Laboratory package provides a method for Health Care Providers to place requests into the system for collection and analysis of patient’s specimens. It also provides a means of tracking work activities to completion and reporting. When results become available, users may view the results in a variety of formats.

The Clinical Pathology &amp; Laboratory Medicine Service:

The package provides methods of identifying and processing workload.

Test result values are accepted from manual input and/or automated instruments and test data is displayed for review before verification.

After verification, the results may be automatically distributed to appropriate locations throughout the institution.

Data is provided for management reports and administrative support.

What are the benefits of the Laboratory Package?

Lab test information is more accurate, timely, and accessible.

Status of orders is more accessible to lab and hospital personnel.

Abnormal and critical values can be flagged to assist in verification and review of data.

Quality control data can be collected, automatically performed, and reported.

Delta checks can be made on a series of data to establish trends or significant clinical variations in value.

#### Functionality

Phlebotomy/Ordering

Supports ward order entry.

Reports status and transactions of tests.

Prints collection lists/labels.

Tracks the laboratory accession numbers and order numbers.

Provides maximum ordering frequency (number per day, daily, user defined 	limits).

Flag duplicate orders.

Processes special ward instructions at time of ordering.

Specimen Processing

Provides worklists by urgency and accession number (instrument-specific).

Produces incomplete lists.

Produces workload/data capture reports.

Produces review lists for verification of data.

Verification/Release of Data

Provides Delta Checks, flagging high/low/critical results.

Provides customized input checking.

Provides automatic calculations (e.g., LDL).

Supports review/verification by group or individuals accessions.

Unidirectional and Bi-directional Auto Instrument Support.

Reports

Produces supervisory management reports, audit trail reports, system integrity reports, quality assurance, and utilization review reports.

Produces discharge summaries and cumulative and discrete episode reports.

Produces automatic transmission of data at time of verification to the ordering location.

Provides quality control.

Provides search capabilities (SNOMED criticals, HI-LO).

Provides Antimicrobial Trend Reports.

Provides Infection Control Reports.

Provides Health Department Reports.

Provides multiple reports of microbial interpretation.

Provides searches for cytological agents with defined antimicrobial patterns.

#### Laboratory Module Work Flow

#### Package Specific Notations

This section describes notes and warnings used to indicate user responses.

##### 1 Warning Symbol

***WARNING:** The warning symbol indicates that the action to be performed is critical.

##### 2 Note Box

**NOTE:** The note box indicates that a special action may be recommended or required.

IMPLEMENTATION AND MAINTENANCE

## Implementation and Maintenance

### 5 System Integrity Checks

#### Check Files for Inconsistencies [LRCHKFILES]

This option includes the check from Check Patient and Lab data Cross Pointers [LRCKPTR] option plus additional checks on potential inconsistencies in various files. The following is a list of some of the messages, which might be generated if there are discrepancies or problems. There are several routines that run when this option is called up. This option is most useful when you are initially setting up your files.

**NOTE:** Only the first 20 errors are totaled for the section, but a total error count is provided with the group.

**Messages:** Messages are labeled either: **F** (fatal) or **W** (warning).

**NOTES:**

•	Messages are labeled either **F** (fatal) or **W** (warning).

•	Fatal indicates potential problems with various software functions. Consult your Regional ISC if necessary.

•	Warning is not critical, and under most situations can be ignored. However, if you are experiencing problems with a particular item, please investigate. Consult your respective ISC if uncertain of the impact.

**From File #60:** The user can choose not to check tests that are defined as NEITHER in the TYPE field when the option is selected.

F	-	A test can NOT be Atomic and Cosmic at the same time.

W	-	Atomic test has no site/specimen; therefore no units or range

F	-	Test MUST have a HIGHEST URGENCY value

F	-	The data name field must be re-entered to set up location and field

F	-	BAD Data name

F	-	Needs a print name entered

W	-	Does not have a print order

F	-	BAD pointer to the ACCESSION file (#68)

F	-	BAD lab collection sample pointer to the COLLECTION SAMPLE file (#62)

F	-	BAD pointer to the PROCEDURE file (#61.5)

F	-	BAD Edit code pointer to the EXECUTE CODE file (#62.07)

F	-	BAD Batch data code pointer to the EXECUTE CODE file (#62.07)

F	-	BAD pointer in panel

F	-	Test is on its own panel (infinite loop)

F	-	BAD entry in Specimen/Site subfile

F	-	BAD Specimen/Site subfile pointer to TOPOGRAPHY FIELD file (#61)

F	-	BAD type of DELTA CHECKS file (#62.1) pointer

F	-	BAD collection sample pointer to COLLECTION SAMPLE file (#62)

F	-	BAD required comment pointer to EXECUTE CODE file (#62.07)

From File #68:

F	-	Missing the LR subscript

W	-	Missing the print order

F	-	Has no abbreviation

F	-	BAD common accession # pointer to the ACCESSION file (#68)

F	-	BAD accession transform pointer to the EXECUTE CODE file (#62.07)

F	-	Accession transform field and EXECUTE CODE file (#62.07) not match

F	-	BAD verification code pointer to the EXECUTE CODE file (#62.07)

F	-	Verification code and EXECUTE CODE file (#62.07) don’t match

F	-	Does not have an accession

W	-	Does not have an order number

F	-	Does not have an Order on file

F	-	BAD pointer to test LABORATORY TEST file (#60)

F	-	BAD pointer to URGENCY file (#62.05)

F	-	BAD pointer to the specimen COLLECTION SAMPLE file (#62)

F	-	BAD pointer to COLLECTION SAMPLE file (#62)

F	-	BAD instrument pointer to the AUTO INSTRUMENT file (#62.4)

F	-	BAD control name pointer to the LAB CONTROL NAME file (#62.3)

From File #69:

F	-	Entry LRDFN in ^LR(is missing

F	-	Does not have an ORDER number

F	-	BAD pointer to COLLECTION SAMPLE file (#62)

F	-	BAD pointer to the USER file (#)

F	-	BAD pointer to the LABORATORY TEST file (#60)

F	-	BAD pointer to the URGENCY file (#62.05)

F	-	BAD pointer to the ACCESSION file (#68)

F	-	BAD pointer to the specimen TOPOGRAPHY file (#61)

From File #s 68.2 and 62.4

F	-	MISSING ZERO NODE

F	-	Has duplicate routine entry

F	-	SYSTEM must have a device to get the data from

F	-	Has no program name. This will prevent data processing

F	-	Must have a Load/Work List entry

F	-	Enter a number that has a BAD test pointer

W	-	A sequence/batch should have 0 cups/tray

F	-	BAD pointer in the LOAD transform field

F	-	BAD pointer in the INITIAL setup field

F	-	Does not have a profile defined

F	-	Has a BAD test pointer

F	-	At least one test of the panel must NOT be build name only

F	-	BAD accession area pointer

All of the **F** or **W** messages give you a place to start looking within each file mentioned; most of them you can fix by making required field changes. Some will have to be fixed by using some of the utility functions of VA FileMan or re-cross-referencing certain fields within files. If the “fix” is not evident to you, ask your ISC for help.

You should run this check every three months and after any unscheduled downtimes.

#### Check Patient and Lab Data Cross Pointers [LRCKPTR]

This option should probably be run on some kind of routine basis (monthly would probably be more than adequate). This could be part of a laboratory quality assurance program to verify the internal consistency of the laboratory data files. The program goes through each file to see if there is an LR pointer. If there is, it then looks to see if that pointer is correct. The program then goes through the lab data file to see what file is being pointed to and makes sure there is a corresponding entry in that file.

### 6 Laboratory Package Routine Integrity Menu

#### Lab Routine Integrity Menu

This menu option is designed for IRM Site Managers to provide the means to load LR ROUTINE INTEGRITY CHECKER file (#69.91) with data after package installation and provide a method to view data on a single routine. It loops through the File #69.91 to determine if any routines have been changed/edited. Lab Routine Integrity [LR INTEGRITY] menu is composed of three options:

LR Integrity Load

LR Integrity Loop

LR Integrity Single

This menu is also designed for support persons to determine the integrity of the laboratory routines, by determining the routine size and the ASCII value of the characters which are in the routine. By using these values you can determine:

If the routine has been altered or edited.

The size of the routine (used in determining routine map space.)

A double-check on patch application. (This is not foolproof.)

The total number of routines (excluding all INITs).

Options which have been deleted or renamed. These are used in the post INITs.

LR ROUTINE INTEGRITY CHECKER file (#69.91) is based upon versions. If a version is no longer in use, that version can be deleted from the file.

The Lab Routine Integrity [LR INTEGRITY] menu is distributed on the Lab liaison [LRLIAISON] menu.

You must delete all INITs before loading these routines.

This file is not exported with routines. The site must load the routines into the global/file. Option LR Integrity Load is provided for that purpose.

#### Loop thru LR Integrity [LR Integrity Loop]

This option will loop through the entire LR ROUTINE INTEGRITY CHECKER file (#69.91) to determine if any of the loaded routines in the file have been changed or edited.

#### Load Integrity File [LR Integrity Load]

This option will load the LR ROUTINE INTEGRITY CHECKER file (#69.91) with lab routines that have the correct version number in the second line. Those routines that do not match (e.g., LRINITs) will not be loaded.

The option should be done as soon as possible. Users can be logged on during this process.

If there are local routines in the LRZ namespace and you wish these to be included in the LR ROUTINE INTEGRITY CHECKER file (#69.91), they must have the correct second line format and version number.

Second line format

;;xx.xx;LAB SERVICE;**pn**;date/time

where xx.xx=Version Number

pn=Patch Number

#### Check a Single Routine Size [LR Integrity Single]

This option allows you to review stored data about a single routine. After entering the routine name, the option will show you the current data and compare this data with values stored in LR ROUTINE INTEGRITY CHECKER file (#69.91). It then indicates if the routine has been changed/edited.

This option will also allow you to determine if a patch has been applied correctly. To get a complete listing, use the VA FileMan Print option.

### 7 File Editing

The Laboratory Information Manager can perform editing file entries if they have VA FileMan access. File attributes generally cannot be edited.

There are certain files and or fields, which require great caution when editing or entering data. Some of these fields may contain mumps codes. A FileMan access code of programmer is required to edit these files/fields. The assignment of programmer access codes is a local issue. Therefore, certain files and fields may not be accessible by the LIM.

**NOTE:	Deletion** from most files is strongly discouraged. It can be done in certain instances, but use caution. If there is any uncertainty, do not delete entries until advised by your Regional ISC.

If file entries are edited (either initially or after system implementation), they **must** be done in this order:

1. TOPOGRAPHY FIELD file (#61)

COLLECTION SAMPLE file (#62)

ACCESSION file (#68)

LAB DATA file (#63)

LABORATORY TEST file (#60)

ACCESSION TEST GROUP file (#62.6)

LABORATORY SITE file (#69.9)

It is recommended that before adding entries to the above files, you run Check Files for Inconsistencies [LRCHKFILES] option to find any inconsistencies. Correct any **fatal** responses listed. When this is completed, you will be ready to add new entries.

After the above files are finished, other files may be changed in any order. The above seven files must be changed in that order because of the interdependence of the files.

#### Other Laboratory Configurable Files

MORPHOLOGY FIELD file (#61.1)

ETIOLOGY FIELD file (#61.2)

FUNCTION FIELD file (#61.3)

DISEASE FIELD file (#61.4)

PROCEDURE FIELD file (#61.5)

OCCUPATION FIELD file (#61.6)

URGENCY file (#62.05)

ANTIMICROBIAL SUSCEPTIBILITY file (#62.06)

EXECUTE CODE file (#62.07)

DELTA CHECKS file (#62.1)

LAB SECTION file (#62.2)

LAB CONTROL NAME file (#62.3)

AUTO INSTRUMENT file (#62.4)

LAB DESCRIPTIONS file (#62.5)

AGGLUTINATION STRENGTH file (#62.55)

WKLD CODE file (#64)

WKLD LOG file (#64.03)

WKLD NON WORKLOAD PROCEDURES file (#64.05)

WKLD CODE LAB SECT file (#64.21)

LAB REPORTS file (#64.5)

INTERIM REPORTS file (#64.6)

BLOOD INVENTORY file (#65)

BLOOD BANK UTILITY file (#65.4)

BLOOD DONOR file (#65.5)

LAB LETTER file (#65.9)

BLOOD PRODUCTS file (#66)

OPERATION (MSBOS) file (#66.5)

BLOOD COMPONENT file (#66.9)

REFERRAL PATIENT file (#67)

RESEARCH file (#67.1)

STERILIZER file (#67.2)

ENVIRONMENTAL file (#67.3)

LOAD/WORK LIST file (#68.2)

WORKLIST HEADINGS file (#68.4)

LAB JOURNAL file (#95)

#### Laboratory Files Not to be Edited

ARCHIVED LR DATA file (#63.9999)

WKLD SUFFIX CODE file (#64.2)

ARCHIVED WORKLOAD DATA file (#64.19999)

WKLD ITEM FOR COUNT file (#64.22)

WKLD INSTRUMENT MANUFACTURER file (#64.3)

CUMULATIVE file (#64.7)

ARCHIVED BLOOD INVENTORY file (#65.9999)

NON PATIENT WORKLOAD file (#67.4)

LAB MONTHLY WORKLOADS file (#67.9)

ARCHIVED LAB MONTHLY WORKLOADS file (#67.99999)

LAB ORDER ENTRY file (#69)

LR CPRS PARAMETERS file  (#69.71)

- Patch LR*5.2*462 contains a modification to the LABORATORY TEST (#60), LAB ORDER ENTRY (#69), LABORATORY SITE (#69.9) and adds the new file LR CPRS PARAMETERS (#69.71).

## NOTES:

#### New Data Names

In the LABORATORY TEST file (#60), each test entry with a CH subscript and a type of BOTH or OUTPUT has a location or data name. See the location Data Name field of File #60. This data name points to a unique field in the LAB DATA file (#63) where the data for that test is to be stored. This unique field also defines what type of value can be entered as a result for the test (free text, numeric, or a set of codes).

**NOTE:** Panels, profiles, and tests with subscripts other than CH do not have data name entries.

The exported version of the LAB DATA file (#63), subfield #4 contains subfield entries called data names, most of which are associated with corresponding pre-supplied entries in the LABORATORY TEST file (#60). These data names determine the type of response allowable when entering a result for a laboratory test. You should print a list of possible subfields to determine if additional entries must be added. The addition of data names must be done by using Add a new data name [LRWU5] option.

##### 3 Add a New Data Name Using a Option

Select Lab liaison menu Option: **DATA** Add a new data name

This option will add a new data name to the lab package.

DATA NAME: **GLUCOSE-TIMED**

ARE YOU ADDING GLUCOSE-TIMED (SUBFIELD # 7022001) AS A NEW DATA NAME? NO// **Y** (YES)

Enter data type for test: (N)umeric, (S)et of Codes, or (F)ree text? **F**

Minimum length: **2**

Maximum length: **30**

'GLUCOSE-TIMED' added as a new data name

Data Name: GLUCOSE-TIMED    Subfield #: 7022001    Type: FREE TEXT

Input Transform: K:$L(X)&gt;30!($L(X)&lt;2) X

Minimum length: 2

Maximum length: 30

You must now add a new test in the LABORATORY TEST file and use

GLUCOSE-TIMED as the entry for the DATA NAME field.

**Warning:** It is not advisable to use FileMan for adding or editing the Data Name field.  FileMan will not perform some of the checks for duplicate names, etc. that are performed by the options “Add a new data name” and “Modify an existing data name.”

#### File Structure/Interaction

Before you begin the process of reviewing and editing the Laboratory package files (also known as site-configuring), it is important to note which of the files should be edited prior to implementation and the sequence in which they should be modified.

The database for the Laboratory package is composed of a series of files. These files contain all the information that is needed by the system to process or interpret test data and are the basis for storage, organization, and retrieval of that data.

The files and the data they contain form the backbone of a comprehensive network that is used on three levels:

1. Within files

Between files in the lab package

Among files in the lab package and other package files

Information within a file may in some ways be dependent upon other elements stored in the **same file.** When this occurs, it is said that the file points to, or references itself. Similarly, data contained in one file may point to another separate file or a group of files. Finally, files within the lab package can be pointers to files found in other packages in the system (i.e., ADT or PHARMACY). This occurs when the lab file information is drawn **from** data contained in an outside file or when the lab file information **points to** an outside file.

Based on the relationships that exist between the files, the sequence of events during file modification becomes very important. Files that must be edited or modified in sequence are:

1. TOPOGRAPHY file (#61)

COLLECTION SAMPLE file (#62)

ACCESSION file (#68)

LAB DATA file (#63)

LABORATORY TEST file (#60)

ACCESSION TEST GROUP file (#62.6)

LABORATORY SITE file (#69.9)

These seven files are also known as Day One files, although editing of other files in addition to those listed above must be done in order to bring up a fully functional Laboratory package. We are classifying them as primary or preimplementation files **,** which include the following:

1. TOPOGRAPHY file (#61)

COLLECTION SAMPLE file (#62)

ACCESSION file (#68)

LAB DATA file (#63)

LABORATORY TEST file (#60)

ACCESSION TEST GROUP file (#62.6)

LABORATORY SITE file (#69.9)

LAB CONTROL NAME file (#62.3)

AUTO INSTRUMENT file (#62.4)

LAB REPORTS file (#64.5)

INTERIM REPORTS file (#64.6)

LOAD/WORK LIST file (#68.2)

**NOTE:** Remember that the first seven files must be reviewed/edited in that order. These are the Day One files.

We have included review here, since in most cases you will only have to review the entries in the TOPOGRAPHY file (#61) to make sure the site/specimens you need are there. If you have to add an entry, do it first. The remaining primary files can be modified in any order you wish, with a few exceptions. If you want to put controls on a load or worklist, the entry must be made in the LAB CONTROL NAME file (#62.3) first. In order to specify what load or worklist is run on a particular instrument, you have to build the LOAD/WORK LIST file (#68.2) entry first and then associate it with the correct instrument in the AUTO INSTRUMENT file (#62.4).

To better understand the interrelationships of the files and their corresponding field characteristics, one of the first things you should do is use VA FileMan to obtain a list of file attributes (otherwise known as a data dictionary) for each and every Laboratory package file. These listings will provide the information on type of field, length of field, number of decimals allowed, whether a field requires an entry, input transforms, output transforms, cross references and identifiers, as well as pointers which exist between the files. A good understanding of the files, what information they contain and how they interrelate is important in the implementation process.

#### Editing the Files

If you have lots of extra time, feeling ambitious, or a stickler for details, you can also modify the other Laboratory package files prior to implementation, although the package initially will be fully functional without extensive editing. Three exceptions here are Microbiology, Anatomic Pathology, and Blood Bank related files. These files should be reviewed and modified before bringing up those portions of the lab package. Specific information about those pre-implementation files can be found in the Microbiology, Anatomic Pathology, and Blood Bank sections in the Planning and Implementation Guide.

Listed below are some suggested steps you should take when adding to, editing, modifying, or otherwise changing any entries in the laboratory package files before and after implementation:

1. FAMILIARIZE YOURSELF WITH THE FILES - list the entries (if any); obtain a printout of the data dictionary for the file; figure out what type of information goes into the file.

GATHER APPROPRIATE INFORMATION - compile and organize the necessary information for editing the file; consult existing lab documentation and procedures; consult with department personnel from each area of the lab.

EDIT THE FILE - add new entries or modify existing entries; **DO NOT DELETE** existing entries unless absolutely necessary; consult with your site manager or regional ISC for any questions or problems. **BE CAREFUL!**

DOCUMENT YOUR WORK - obtain new copies of any and all file listings and printouts for reference after making any changes.

CHANGES AFTER GOING LIVE - determine what other file(s) (if any) will be affected by the change, **always** make any changes to the day one files in the specified order, and document your changes (what fields and files, as well as the date).

ADDING EXTRA LABELS FOR AN INSTITUTION IN A MULTI-DIVISIONAL FACILITY – Customize the number of labels, beyond the default, required for a specific lab test at a specific facility. This number is set in LABORATORY TEST File (#60) utilizing two new fields, the INSTITUTION EXTRA LABELS field (#60.15,01) and the NUMBER OF LABELS subfield (#60.15,1). A LIM, with production package access for a multidivisional facility, must configure this functionality.

**NOTE:** For a complete description of each field in the LABORATORY files (#60-#69.91 and #95), see the Planning and Implementation Guide.

### 8 General Laboratory

#### Menu Description

Familiarize yourself with as many of the options available as possible in the exported package. The more you review and practice, the more benefits you will gain from all the time you spent modifying the lab files. Even the most carefully defined database would not be much help if the lab personnel do not know how to **use** the package.

The laboratory options are exported as menus, which group the options with similar functions together into general categories, as follows:

**Menu	Function**

Laboratory DHCP Menu	This is the primary menu options

Phlebotomy Menu [LR GET]		Options the lab uses to get (collect) the test 	orders and specimens

Accessioning Menu [LR IN]		Options the lab uses to put the orders in

(enter into) the system

Process Data In Lab Menu		Option the lab uses to do (process) the work [LR DO!] on the specimens

Quality Control Menu		Options for maintaining quality assurance

Results Menu [LR OUT]		Options the lab uses to report or send out patient test results

Information-Help Menu		Options the lab uses to obtain additional

[LR HELP]	“help” or information about tests, orders,

make inquiries, etc.
Anatomic Pathology [LRAP]				Options used by the Anatomic Pathology  module

Blood Bank [LRBL]						Options used by the Blood Bank module

Microbiology Menu {LRMI]					Options related to the microbiology section

Supervisor Menu							Options used by supervisors to perform

[LRSUPERVISOR]	specialized functions in the lab

Ward Lab Menu [LRWARDM]		Options used by the ward personnel to place orders, make inquiries, etc.

#### Laboratory Security Keys

The laboratory package supplies various security keys that act as follows:

Some routines check for user security keys. If you do not have the appropriate security key assigned to you, the routine will not work for you.

Certain options and menus are locked with security keys. These keys are used as locks for particular options, and are also checked elsewhere during the execution of the option. In some cases, the lack of the appropriate security key will prevent you from seeing an option even though you have been assigned a menu that normally contains that option.

Each user of the Laboratory package must have the appropriate security keys assigned before accessing the package. The SECURITY KEY file (#19.1) contains the key names with a short description. The following is a list of the Lab keys:

KEY	USERS

LRANAT	Anatomic Pathology users

LRAPSUPER	Anyone allowed to use the Anatomic Pathology Supervisor Menu and edit SNOMED codes

LRAU	Autopsy Module users

LRBLOODBANK	Blood Bank users

LRBLSUPER	For Blood Bank supervisory level decisions

LRCY	Cytology Module users

LREM	Electron Microscopy Module users

LRLAB	Laboratory Personnel only

LRLIASON	Laboratory Information Manager*

LRMICRO		Microbiology users

LRMIVERIFY	Microbiology personnel

LRSP	Surgical Pathology Module users

LRSUPER	Laboratory Supervisors

LRVERIFY	Anyone who is authorized to verify lab results

LRPHMAN	Phlebotomists

LRPHSUPER	Supervisor of the phlebotomy collection team

Any combination of the above security levels may be used, as deemed appropriate by the Laboratory.

***** Highest security level of all keys. The Laboratory Information Manager* key should be reserved for LIM and IRM Support staff.

#### Workload Recording;

The DHCP Laboratory Workload recording and reporting system is a flexible and comprehensive technique for capturing work performed. The system covers all areas of the laboratory, both clinical and anatomical. Although differing methods for capturing the workload data are used, all data is uniform in structure and content. The level of reporting may be general or specific depending on how the files are setup. The data is designed to allow either gross bottom line figures or highly detailed line item reports.

There are four levels of data concentration or reporting levels.

1. National level

Administrative level (Site specific)

Lab section level

Accession level (data for each patient sample)

The highest report would be the “National level” and it is similar to the AMIS report. This report supplies total work load for the reporting institutions. Various miscellaneous reports could be obtained from the national roll-up data base as needs are identified. The report would be used by offices dealing with national and regional issues (i.e., Regional Director, Central Office).

The next lower reporting level would be the “Administrative level” which contains site specific data in more detail. Administrative reports contain data dealing with ordering location, or time of day work was completed. This type of report can be used by the hospital director, chief of staff, or Laboratory service.

The next reporting level is of the most benefit (internally) to the laboratory service would be the “Lab section level”. The site can then control the level of granularity they wish the data to be collected. This level contains all information known about the work performed except the patients’ identity and accession number. There could be several reports dealing with specific areas or sections of the laboratory. Reports may be generated for a  particular bench or workstation.

The lowest reporting level is of the most benefit to lab supervisors would be the “Accession level”. This data level is the most detailed, and includes more than 30 data elements at this level. There are a wide variety of potential views of the data collected, and unique displays can be devised by the user. Remember this level contains the patient identity and the accession numbers.

All levels of reporting below the national level (the highest collecting point) can be manipulated via VA FileMan sorts and prints, thus allowing ad hoc reports to be designed by the reporting sites. The data structure is flexible and standard, providing data that is standardized at the national level yet customized at the site levels. The degree of granularity at the site level will not affect the data at the national level. The data collected at the national level will be consistent and standardized.

To achieve standardized and consistent data content at all levels, the schemes outlined in the “Manual For Laboratory Workload Reporting” published by the College of American Pathologists (CAP) was used. This manual outlines methods for identifying and collecting workload. The terminology, categories, methods, etc., were adopted into the DHCP reporting methods. The elements of the most current CAP manual are loaded into DHCP files. The CAP manual represents the seed for the DHCP National Laboratory Test File. From this basic guideline, additional data elements are collected to satisfy specific concerns of Department of Veterans Affairs. It is recommended that the LIM get a copy of the manual and review it before implementation. Using a functional specific outline by the Laboratory program office, a system of data collection and tabulation was devised.

The actual process of data collection is designed to relieve the verifying technologist of as much of the burden of additional work tasks or keystrokes. The technologist needs only to answer one or two additional questions while in the course of normal activity to trigger data collection. Additional keystrokes will be necessary to capture many non-routine procedures. The collecting process is virtually transparent to the technologist. The collecting system has a great deal of flexibility inherently designed into it, thus allowing each site the ability to tailor their system to their particular work flow.

Although methods of collecting may vary from site to site, the data is comparable to any other site's data at any level. This supports management and functional needs without regard to data source. If a particular procedure and method is performed at one site, it will be identified the same way at any other site.

Approximately 80-85% of workload data is collected automatically by the system. The remaining 15-20% can be entered into the system manually. This feature allows for input during periods when the system was unavailable to capture the data automatically.

As new instruments, techniques and procedures become available, new workload code will be distributed via national releases. This ensures that data remains standardized and consistent for site to site. A procedure for coordinating DHCP activity and the College of American Pathologist will be worked out to remove any conflicts of methods and terms.

For Blood Bank, Cytology, Surgical Pathology, EM, and Autopsy sections, you will have to add necessary tests as specified to capture workload. See details in the individual sections.

**NOTE:** For further detail on the implementation of Workload, please see the Planning and Implementation Guide.

#### Lab Labels

There are seven lab label types available for use in the Laboratory package. Only one of these label types can be used at any given time. The label type is defined in the LABORATORY SITE file (#69.9).

Barcode label are now supported, not all labels are distributed with barcode functionality.

1. **3.5 X 15/16 Accession # 1st (LRLABEL):** This is the default label if no label is entered in the LABORATORY SITE file.

**Example:**

HE 0904 ET

AAA,A	09/04/88

000-11-1222  W:OLD B:4401-C

LAVENDER	Order: 1101

CBC

2. **2 X 5 UNEVEN (LRLABEL1)** :  This is the 10-part SLC label at 16.5 CPI, with 1 label printed for every four tests on the accession.

**Example:**

AAA,A	CH 0910 2	CH 0910 2	CH 0910 2	CH 0910 2	CH 0910 2

000-11-1222 W:1B	09/10/88	09/10/88	09/10/88	09/10/88	09/10/88

SMALL RED TOP Order: 1118		AAA,A	AAA,A	AAA,A		AAA,A

CHEM 7		RED TOP	RED TOP	RED TOP	RED TOP

AAA,A	CH 0910 2	CH 0910 2	CH 0910 2	CH 0910 2	CH 0910 2

000-11-1222 W:1B	09/10/88	09/10/88	09/10/88	09/10/88	09/10/88

3. **ORDER # FIRST (LRLABEL2):** The order number appears on the top line.

**Example:**

Order: 1101

AAA,A

000-11-1222 W:OLD

HE 0904 35	LAVENDER

CBC

4. **MEDLAB (LRLABEL3):** 7-part MEDLAB type label.

Example:

AAA,A	AAA,A	AAA,A

HE 0904 35	W:OLD	HE 0904 ET	W:OLD	HE 0904 35	W:OLD

000-11-1222	09/04/88	000-11-1222	09/04/88	000-11-1222	09/04/88

LAVENDER Order:1101	LAVENDER Order:1101	LAVENDER Order:1101

CBC

HE 0904 35	HE 0904 35	HE 0904 35	HE 0904 35

09/04/88	09/04/88	09/04/88	09/04/88

5. **SITE File (LRLABEL4):** This label type can be used for a label program that is developed at the local site. The name of the site developed routine must be LRLABEL4. This name can be used when a modification is made to one of the previous four label routines to meet site-specific requirements.

6. **SITE DEVELOPED (LRLABEL5):** This label type is used for VA Form 10-1392.

**Example:**

URINE 0714 4	URINE 0714 4	URINE

7. **INTERMEC LABEL (LRLABEL6):** Requires Intermec Printers.

**Example:**

**NOTE:** Multidivisional facilities can customize the number of labels, beyond the default number, required for a selected lab test at a selected local division.

The requirements and procedures associated with printing labels for institutions that share the same Veterans Integrated System Technology Architecture (VistA) database are addressed utilizing two new fields: The INSTITUTION EXTRA LABELS field (#60.15,01) and the NUMBER OF LABELS subfield (#60.15,1).

For further detail on the implementation of this feature in a multi-divisional facility, refer to the Laboratory Planning and Implementation Guide.

#### Batch Entry of Preliminary Comments for Accessions

Patch LR*5.2*476  modified data in the EXECUTE CODE (#62.07) file to enable batch entry of preliminary comments for designated accession numbers. When a microbiology technologist needs to enter preliminary comments for accessions with negative cultures in VistA, this enhancement enables the technologist to enter the same comment for multiple accession numbers. For example, a site might process hundreds of urine cultures daily. Currently, the technologist must enter "No growth after 24 hours" as a preliminary result individually for each applicable accession. With this modification, technologists can enter the same preliminary result for all applicable accessions at once, thereby reducing the time and effort required to make preliminary results available for clinical use.

To accomplish this, the modification adds data to the BACTERIOLOGY, MYCOLOGY, and TB BACTERIOLOGY records in the EXECUTE CODE file, EXECUTE CODE (#1) field. The data is taken from sub-fields located in the LAB DATA (#63) file, MICROBIOLOGY (#63.05) sub-file, MICROBIOLOGY (#5) field. The sub-fields are:

- PRELIMINARY BACT COMMENT (#1) sub-field for Bacteriology accessions
- PRELIMINARY MYCOLOGY COMMENT (#20.5) sub-field for Mycology accessions
- PRELIMINARY TB COMMENT (#26.5) sub-field for Mycobacteriology accessions

Using the RB Results Entry (Batch) [LRMISTUF] option, the technologist can select a sub-field and enter a preliminary comment for multiple accession numbers. Once the comment is entered, routine LRMISTF updates the corresponding BACTERIOLOGY, MYCOLOGY, or TB BACTERIOLOGY data record in the EXECUTE CODE file.

To verify that sub-fields #1, #20.5, and #26.5 are assigned to the corresponding data records, invoke 'INQUIRE TO FILE ENTRIES' in FileMan to display the EXECUTE CODE field in the EXECUTE CODE file for the names BACTERIOLOGY, MYCOLOGY, and TB BACTERIOLOGY as shown below:

Select OPTION: INQUIRY TO FILE ENTRIES

NAME: BACTERIOLOGY                      TYPE: EDIT

EXECUTE CODE: S DR="11.55////"\_DUZ\_";.055;.05;.99;11.6;11.5;1;S

LRSPEC=$P(

LRBG0,U,5),Y=$S(LRSPEC=71:11.57,LRSPEC=360:11.58,1:0);11.57;S

Y=0;11.58",LREND=0 D ^DIE S:$D(Y) LREND=1 Q:$D(Y)  D ^LRMIBUG Q:LREND  S

DR="13;11" D ^DIE Q

NAME: MYCOLOGY                          TYPE: EDIT

EXECUTE CODE: S

DR="19.5////"\_DUZ\_";.05;.99;19;20;20.5;21;18",DR(2,63

.37)=".01:99" D ^DIE Q

NAME: TB BACTERIOLOGY                   TYPE: EDIT

EXECUTE CODE: S

DR="25.5////"\_DUZ\_";.05;.99;23;24;25;26;26.5;27;22",DR(2,6

3.39)=".01;1:99" D ^DIE Q

To review a description of each EXECUTE CODE field entry shown above, invoke 'INQUIRE TO FILE ENTRIES' in FileMan to display DESCRIPTION field (#6) text in the EXECUTE CODE file for the names BACTERIOLOGY, MYCOLOGY, and TB BACTERIOLOGY, as shown below:

Select OPTION: INQUIRY TO FILE ENTRIES

BACTERIOLOGY

Stuff BACT PERSON with current user; COLLECTION SAMPLE; SITE/SPECIMEN; COMMENT

ON SPECIMEN; BACT RPT STATUS; PRELIMINARY BACT COMMENT; if specimen is urine

use URINE SCREEN; if specimen is sputum use SPUTUM SCREEN. Enter the ORGANISM

and antibiotics (edit templates may be utilized); BACT RPT REMARK; BACT RPT

DATE APPROVED.

MYCOLOGY

Stuff MYC PERSON with current user; SITE/SPECIMEN; COMMENT ON SPECIMEN;

MYCOLOGY RPT STATUS; multiple FUNGUS/YEAST including QUANTITY and COMMENTS;

PRELIMINARY MYCOLOGY COMMENT; MYCOLOGY RPT REMARK; MYCOLOGY RPT DATE APPROVED.

TB BACTERIOLOGY

Stuff TB ENTERING PERSON with current user; SITE/SPECIMEN; COMMENT ON SPECIMEN;

TB RPT STATUS; ACID FAST STAIN; QUANTITY; multiple MYCOBACTERIUM including

QUANTITY, COMMENTS and DRUGS; PRELIMINARY TB COMMENT; TB RPT REMARK; TB RPT

DATE APPROVED.

Microfiche of Path Reports;

The storage of Anatomic Pathology reports over a number of years requires a considerable amount of space for the bound volumes, whether they are all retained in the Pathology Service or stored off-site. Other methods of compact storage can greatly economize on use of this space. Some such methods include microfilming and microfiche. Newer techniques such as compact laser discs are emerging, and may already be available, but at considerable expense. This section provides instructions for setting up and using microfiche within the Anatomic Pathology module of the Laboratory package.

Microfiche and microfilming are technologies well developed at this time and are relatively inexpensive. Many hospitals are using these techniques in various departments on a daily basis, even those which are computerized. The equipment and service costs to microfiche anatomic pathology reports are reasonable and can be accommodated by almost any budget.

A microfiche reader-printer in the Anatomic Pathology department is an absolute necessity for using microfiche. Reader/printers range in cost from about $550 - $600 for the low usage installations, and from $2500 for the higher volume pathology laboratories. A Xerox or copy machine, which is accessible in most hospitals, is a helpful adjunct.

For further information, please see the Planning and Implementation Guide.

### 9 Cumulative Report

The cumulative reports are a printed accumulation of laboratory test results that have been reported (verified) during a given time interval (usually one day). With these reports, it is possible to see trends in laboratory results over a period of time. New data is displayed together with previous data so that the ultimate result is better patient care. Another feature is the ease with which results can be retrieved in a patient’s chart. Some sites may choose to print these reports daily. While others may choose to print them Monday-Friday only.

The cumulative is generally printed alphabetically by location. Within each location, it is printed alphabetically by patient name. When the location is FILEROOM, the cumulative prints by the last four digits of the patient’s SSN# (sorted by last 2, then the next 2 digits). The report is designed to replace the usual lab reporting slips that are filed in the patient’s chart. With these reports, it is possible to see trends in lab data over a long period of time. The LAB REPORTS file (#64.5) is used to define a site’s cumulative report.

**NOTE:** Similar reporting capabilities are available through FileMan. See the FileMan Lab Results Reporting topic on page 33 for information on generating lab results for a specific patient, specimen type, and lab test, looking back over a specified number of days.

The fields that must have entries in LAB REPORTS file (#64.5) are:

**Lab Report Name:** For each printer that you set up, you will need a lab report name. An entry here allows you to designate a device for printing and a range of locations to print for each device.

**Device:** Name of printer to be used.

**Starting Location:** First location to print to the device.

**Ending Location:** Last location to print to the device.

If you have decided to start your cumulatives by the using the Manual queuing of cumulative [LRAC MANUAL] option, this is all you need to set up.

#### Further Cumulative Functionality (Version 5.2)

With Version 5.2, the capability to print the FILE ROOM cumulatives at a different time from the INPATIENT cumulatives exists.

Two new functionalities exist.

1.	Inpatients and separate locations print on one time schedule and all other outpatients print on another schedule. For the outpatients to print on the different schedule, the following file entries **must** exist.

64.5,4 (File Room) =“YES”

64.5,17 (Separate File Room) = “YES”

Reports multiple has File Room 1 and File Room 2 with 64.56,3 (FileRoom Report) =“YES” in each Starting and Ending location containing “FileRoom”

2.	Inpatients and separate locations print on one time schedule, one set of outpatient reports print on a different time schedule, one location and another set of outpatient reports print at the same time of the other outpatients but at a different location. This is done by filling out 64.57,1 (Alternate File Room).

##### 4 Fields for Fileroom Cumulative (LAB REPORTS file (#64.5))

A.	File Room Report Date field (#16): This field is used if the site prints the FILEROOM location on a different schedule than the regular Cumulative print. If this feature is utilized, the last date the FILE ROOM location(s) were printed is stored in this field.

B.	Separate File Room field (#17):	This new field is used to designate the FILE ROOM cumulative being printed on a schedule different from the regular cumulative. To utilize this feature the following needs to be setup.

C.	File Room Report field (#3) in Report Name multiple field (#2): This new field is used to designate a report to print a file room location. It is used in conjunction with File Room field (#4) and Separate File Room field (#17). It allows the cumulative to identify those reports which should be run when a site wishes to print the file room reports and they are doing so on a schedule separate from the regular cumulative.

D. Alternate File Room field (#1) in the Separate Report Location multiple field (#6): This new field is used to designate those locations which a site wishes to print to a “FILE ROOM” location but which they do not wish to be a standard file room. This could be sites which have satellite clinics which have their own file rooms. The name entered here will cause this location to be sorted to a location called “FILE ROOM\_ alternate file room name” followed by a “1” or “2”. The patients will be sorted in terminal digit order similar to the regular file room. This requires that the site has File Room field (#4) set to “YES” to sort non inpatients to location “FILE ROOM”.

Setting up the files

1.	Set Separate File Room field (#17) to “YES” - this tells the cumulative that you are printing the FILE ROOM on a schedule different from the regular cumulative schedule.

2.	For regular FILE ROOM patients, set up one or two reports as follows (FileMan requires the different names):

If one report:	starting location:	FILE ROOM1

ending location:	FILE ROOM2

If two reports:

first report:	starting location:	FILE ROOM1

ending location:	FILE ROOM1

second report:	starting location:	FILE ROOM2

ending location:	FILE ROOM2

Define the other fields as with a regular report.

3.	Set File Room field (#4) to “YES” - this old field allows the program to sort all non-inpatients to two locations, FILE ROOM1 and FILE ROOM2, based on terminal digit of SSN.

4.	If you also want to print certain locations to an alternate file room, such as a file room at a satellite clinic then in addition to #2 above, perform the following:

A.	Enter the location(s) that you want to print as a separate report location by entering them in the Separate Report Location field (#6).

B.	Enter in Alternate File Room field (#1), the name to use for this File Room. This name will be concatenated with “FILE ROOM”.

**Example:** DALLAS OPC would result in file rooms FILE ROOM\_DALLAS OPC1 and “FILE ROOM\_DALLAS OPC2.”

**NOTES:**

•	The “\_”, underscore is used to insure that these locations sort after the regular file room locations.

•	Two locations for each file room would be created based on terminal digit of SSN or identifier (non PATIENT file (#2)) similar to the regular file rooms. These locations will print on the same schedule as regular file rooms. Either set up separate reports to print these locations or utilize reports defined in Step #3 above and alter the ending location to include these locations.

5.	On each report, set the File Room Report field (#3) in the Report Name multiple field (#2) to “YES”.

The cumulative software will check when attempting to print a cumulative for a location that contains the name “FILE ROOM” in the following. If Separate File Room field (#17) is set to “YES” and the report being run is not set to “YES” for File Room Report field (#3) then it will skip running the cumulative for that location. This is to prevent another report which may print locations “A” thru “Z” from printing the file rooms unintentionally.

**Example:** Sample of a filled in file

Select OPTION: **ENT** ER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: LAB REPORTS// **&lt;RET&gt;**

EDIT WHICH FIELD: ALL// **17** SEPARATE FILE ROOM

THEN EDIT FIELD: **2** REPORT NAME    (multiple)

EDIT WHICH REPORT NAME SUB-FIELD: ALL// . **01** REPORT NAME

THEN EDIT REPORT NAME SUB-FIELD: **5** STARTING LOCATION

THEN EDIT REPORT NAME SUB-FIELD: **10** ENDING LOCATION

THEN EDIT REPORT NAME SUB-FIELD: **3** FILE ROOM REPORT

THEN EDIT REPORT NAME SUB-FIELD: **&lt;RET&gt;**

THEN EDIT FIELD: **4** FILE ROOM

THEN EDIT FIELD: **6** SEPARATE REPORT LOCATION    (multiple)

EDIT WHICH SEPARATE REPORT LOCATION SUB-FIELD: ALL// . **01** SEPARATE REPORT LOCATION

THEN EDIT SEPARATE REPORT LOCATION SUB-FIELD: **1** ALTERNATE FILE ROOM

THEN EDIT SEPARATE REPORT LOCATION SUB-FIELD: **&lt;RET&gt;**

THEN EDIT FIELD: **&lt;RET&gt;**

STORE THESE FIELDS IN TEMPLATE:

Select LAB REPORTS NAME: **CUM** ULATIVE REPORTS

SEPARATE FILE ROOM: YES// **&lt;RET&gt;**

Select REPORT NAME: FILE ROOM1// **&lt;RET&gt;**

REPORT NAME: FILE ROOM1// **&lt;RET&gt;**

STARTING LOCATION: FILE ROOM1// **&lt;RET&gt;**

ENDING LOCATION: FILE ROOM1// **&lt;RET&gt;**

FILE ROOM REPORT: YES// **&lt;RET&gt;**

Select REPORT NAME: **&lt;RET&gt;**

FILE ROOM: YES// **&lt;RET&gt;**

Select SEPARATE REPORT LOCATION: CARDIOLOGY// **&lt;RET&gt;**

SEPARATE REPORT LOCATION: CARDIOLOGY// **&lt;RET&gt;**

ALTERNATE FILE ROOM: EEE TEST// **&lt;RET&gt;**

Select SEPARATE REPORT LOCATION: **&lt;RET&gt;**

SEPARATE FILE ROOM: YES// **&lt;RET&gt;**

##### 5 Changed Routines

1.	Routine LRAC changes:

A.	Code to prevent selection of file room reports if printing on separate schedule.

B.	Task separate file room reports both using tasked option and manually.

C.	Includes the last file room patient list in building the current list. Same criteria apply, if the report date is greater than the report date stored for the patient then it is added to the list. This was to catch any patients who are on the previous file room cumulative but were not actually printed. If for some reason a patient is not printed, they will roll forward to the next cumulative list.

2.	Routine LRAC1: Code to check if report and location are file room and is this a file room report. Will skip location if it is not supposed to print.

3.	Routine LRAC8: Routine to only go thru LAC global once when checking for header changes. Previously it would go thru global for each change. If more than one change would increase delay in starting the printing by factor of the number of changes. This routine allows the LIM to make multiple changes without adversely delaying start on cumulative.

4.	Routine LRACK:

A.	Routine to check if separate file rooms are implemented and only clear those reports which are not file room.

B.	Changed cumulative device status report to print manual print and file room report fields, separate file room turned on and last file room report date.

5.	Routine LRACKL1: Routine to check if site wants alternate file rooms in addition to regular file rooms. Checks separate locations for alternate file room name.

6.	Routine LRACM2F

A.	Display the date of last cumulative (REPORT DATE) when asking for report date.

B.	Allow user to select multiple locations or all locations. When printing file rooms on a separate schedule, the list can get quite long.

C.	Patients are numbered within location, corresponds to display when user uses reprint option. Also tells you how many patients in each location. Total of all patients and number processed at end of report.

D.	If user prints only some locations then report indicates those locations printed.

E.	On FILE ROOM patients, the report prints the patients SSN not the sorted terminal digit number. The reports still come out in the sorted terminal digit number order.

F.	If printed to a terminal, does page breaks at end of page.

G.	If location continued on successive pages, locations marked as continued.

H.	Prints date/time report is generated and report date.

These are the tasked and interactive options to control printing of the File Room Cumulative:

1.	NAME: LRTASK CUM FILEROOM

MENU TEXT: Task Cumulative Fileroom Report

DESCRIPTION: This option is used to print fileroom cumulative patients. This option determines the last time the fileroom patients were printed. It then identifies all fileroom patients that require printing since the last run and moves them into the patient list for the most recent cumulative run. Finally, it queues a task to print these patients to specified printers.

WHEN THE LAB REPORTS FILE HAS BEEN PROPERLY SET, THIS OPTION WILL ALLOW THE PRINTING OF THE FILEROOM CUME ON A DIFFERENT SCHEDULE THAN THE INPATIENT CUMES.

The manual version of this option is LRAC MANUAL FILE ROOM CUM. This option is designed to be tasked. The manual version SHOULD NOT be tasked.

ROUTINE: CLOCK^LRACFR

2.	NAME: LRAC MANUAL FILE ROOM

MENU TEXT: Manual queuing of File Room cumulative

TYPE: run routine

DESCRIPTION: This option is the manual version of the LRTASK CUM FILEROOM option. If you do not wish to schedule automatic printing of the fileroom cum via the LRTASK CUM FILEROOM option, you may use this option instead. This option should never be tasked. There are some questions asked when this option is used. When the proper file setup has been done, this option will allow the printing of the file room cum on a different schedule than inpatient cums.

ROUTINE: LRACFR

#### TaskManager

The TaskManager can control the printing of the cumulative by means of LRTASK CUM option in OPTION file (#19). Although the time interval between prints is usually one day, it may be set to any time period convenient to your station. The output device can be any printing terminal.

The cumulative has the ability to print portions of the report to different devices, thereby sending reports to locations near where they will be needed.

**Example:** Locations ranging from A to LZ can be sent to device A and locations ranging from LAX to ZZZ can be sent to device B. Or a remote site can specify a printer at the remote site. Dividing the task between printers and CPUs will optimize the run-time required for the cumulative.

Automatic queuing of the report is done using the LRTASK CUM options. The fields QUEUED TO RUN AT WHAT TIME and RESCHEDULING FREQUENCY in the OPTION file (#19) need to be set up appropriately. This option will then spawn reports for all devices defined in the Lab Report Name field of the LAB REPORTS file (#64.5), with the exception of those reports that have an entry in the Manual Print Field of the LAB REPORTS file (#64.5).

If you want to queue a device on another CPU, the DEVICE file (#3.5) on each CPU must have the queued device as one of its entries with the field OTHER CPU containing the Volume set of the other CPU.

#### Device Parameters

The device parameters for all devices that print (or reprint) the cumulative should be the same. Because paging and permanent determinations are made at the time of printing, the device parameters (IOM, IOSL, CPI, LPI, etc., see the VA FileManager Programmer Manual for a discussion of these parameters) need to remain constant.

When initially setting up the device parameters, there are no restrictions on selection of lines per inch, characters per inch, form length, or form width. If you are using profiles that are large and require multiple lines of headings (horizontal format), then it is suggested that you use eight lines per inch and possibly greater than 80 columns in your definitions to accommodate more data per page.

The cumulative should not be sent to a CRT except for testing purposes. If you do specify a CRT, you will need to redefine the lines per screen and number of columns to emulate a printer.

The horizontal display uses the variable IOM (right margin) to decide when to break a line of tests into a second line. If a line of tests is too long to fit on one line, changing the value of IOM (through the device file (#3.5) or when prompted with “DEVICE:”) may get all the tests on one line. Be sure to choose the correct pitch on the printer that you are using.

The vertical display calculates the number of data columns, based on the total number of columns defined in IOM. Likewise, by manipulating the page length (IOSL), you can reduce or increase the number of sets of data to be printed on a given page.

Once these parameters have been determined and you are in production, they should not be changed. It is critical if another printer is used, that the parameters are identical to the previous printer.

***WARNING:** This rule applies to new, additional, or different printer devices. Otherwise the cumulative report may be seriously affected.

#### Initialize LAC Globals &amp; X References [LRAC INITIALIZE]

This option is used when the medical center is ready to begin actual charting of the daily cumulative. It may be run multiple times to restart the page numbering during the testing phase of implementation. Once actual charting has begun, IT SHOULD NEVER BE RUN AGAIN **!** While all pages are numbered and dated, the potential for confusion is obvious.

* **WARNING:** Once in production, this option **should be removed** from menus or disabled!

### 10 Interim Reports

Interim reports are designed to display or produce a printed report of verified lab results that occur in the interim of the running of the cumulative. These reports are in a different format from the cumulative and should not be charted.

It is most important to remember that the interim was not intended to keep up with patient movement. The location entered during the accessioning process will be the location used for printing purposes.

Interim reports will include comments from LABORATORY TEST file (#60), Site/Specimen field (#100), and Interpretation subfield (#5.5). At this time, these comments do not appear on the cumulative report.

Both MI and CH subscripted are available for review with the interim report options. An accession area must have a print order set up in ACCESSION file (#68), for results to print on the interim report. For non-lab users (no LRLAB key), only those tests set up as Both or Output in File #60 will print on interim reports. Users having the LRLAB key may see data entered as “Input Only.”

Since only verified reports will be displayed, the interim reports will not display the status of tests (i.e., incomplete, testing in progress) and hospital staff should be instructed to check the option “Order/Test Status” before generating an interim.

Interim reports can be printed at various times during the day to a centralized printer. Printing is controlled by the LRTASK options, run by TaskMan, and the INTERIM REPORTS file (#64.6). The appropriate LRTASK option should have Fields #200, #201, and #202 filled in with the tasking information. File #64.6 needs to have locations defined for which interim reports are printed, and the HOSPITAL LOCATION file (#44) must also have the Abbreviation field filled in. Whether or not to transmit results immediately upon verification and whether or not to include location on interim reports is also defined. In order to transmit results upon verification, the Que Verified Test(s) fields in the LABORATORY SITE file (#69.9) needs to contain a value of “YES”. If an accession area does not have a print order, the results for that area will not be printed on the interims.

There are several ways to generate interim reports:

Called up automatically for various times of the day using TaskManager

Printed as reports become available (Immediate Interims)

The automatic interim report feature allows a site to select a range of urgencies to print. A field is available in File 64.6 called Urgency Cutoff. This field can be used to establish a range of urgencies to print automatically to a certain location (i.e., If Stat = 1, Pre Op= 2, Routine = 3, and Pre Op is entered into this field, then any urgency less than or equal to 2 will print automatically. The numeric designation is assigned during the enter/edit process on creation of the urgency in the URGENCY file (#62.05).

When deciding to use the automatic interim feature, please keep in mind that every time a test is verified, reverified, etc., a report will print. If you have several tests per accession number and each test is verified separately, you will generate a sheet for each time a test on the accession number is verified.

Called up manually through a menu option for either one patient, a hospital location, or by physician.

Those using the interim for lookup purposes (other than Interim Report for Selected Tests as Ordered [LRRSP]), you need to remember that the dates used in the selection for review are the collection date and time. All interim reports print in inverse date order. This can be very frustrating if your Lab routinely holds tests over for batching purposes. If you verify a test today but it’s collection time is last week, it will not print with today’s interims since the interim option works from the collection date and not the verify date.

Both MI and CH subscripted tests can be available for review with the interim report options.

#### Tasking the Interim

There are two different interim reports that can be tasked. There is the tasked batched interim which is generated at a particular time of day and another interim that is called an immediate interim.

##### 6 c4.Immediate Interim

You must edit several files or have the files edited.

**File (#69.9):** Field:Que Ch, He Etc. Verified Test(S)

Field:Que Micro Verified Test(S)

These fields must be set to “NO” if you do not want the interim to print automatically.

**File (#64.6):** Field:Location

Must contain the location name that acts as a pointer to File #44.

Field:Immediately Transmit Results

Must be set to “YES”

Field:Device

Field:Urgency Cutoff

All reports will print if field is blank. When it has an entry, only higher urgencies will print

##### 7 Batched Interim

Batched Interim can be set up for various times of the day to a centralized printer.

**NOTE:** This device is set up in File #19 under the option name and is NOT that designated in File #64.6.

The information that will print on this report will be the verified data for that day, from midnight until the time of printing. If you elect to have more than one printing each day, you will not get just the reports since the time of the last printing but all verified results for the day. The printing will occur alphabetically by location and within each location, alphabetically by patient name.

**File (#64.6)** Field:Location

Must contain an entry for each ward location

Field:Interim Reporting must contain “YES”.

**File (#19)** Option Name: LRTASK Daily Interim 1, Fields #200, #201, and #202 must contain entries. These fields are for device, frequency (once a day, once a week), and time. For each interim time of day, you will need a different tasked option. (e.g., LRTASK daily Interim I, LRTASK Daily Interim 2, etc.)

### 11 FileMan Lab Results Reporting

Patch LR*5.2*476  added a new FileMan function, LRRESULT, to the FUNCTION (#.5) file. This function enables reporting on lab results for a specific patient, specimen type, and lab test, looking back over a specified number of days. This enhancement applies only to lab tests with verified results for patients currently admitted.

Users must be familiar with FileMan file structure and commands to create and run a report. The four input parameters required to execute the function must be entered in the following sequence:

a) Patient number from the PATIENT (#2) file, entered as NUMBER

b) Specimen type internal entry number (IEN) from the TOPOGRAPHY FIELD (#61) file

c) IEN of the lab test in the LABORATORY TEST (#60) file

d) Look-back number of days

The new entry in the FUNCTION file is defined as follows:

NAME: LRRESULT

MUMPS CODE: S X=$$GETLAB^LRFRSLT(X,X1,X2,X3)

NUMBER OF ARGUMENTS: 4

EXPLANATION: Lab result retriever -- used with the format of

LRFRSLT(a,b,c,d) where a is referenced as INTERNAL(PATIENT), b is the

specimen file 61 IEN, c is the lab file 60 test IEN, and d is the number

of days to search back

Following is an abbreviated example of how to run the report for a verified lab test.

Example #1 from the PATIENT file:

VISTAS1:VISTA&gt;D P^DI

VA FileMan 22.2

Select OPTION: PRINT FILE ENTRIES

Output from what File: EXECUTE CODE// 2  PATIENT  (85282 entries)

Sort by: NAME// @CURRENT ADMISSION

Start with CURRENT ADMISSION: FIRST// T-2500  (DEC 26, 2010)

Go to CURRENT ADMISSION: LAST// T  (OCT 30, 2017)

Within CURRENT ADMISSION, Sort by:

First Print FIELD: CURRENT ADMISSION;L20

Then Print FIELD: .01;L20  NAME

Then Print FIELD: LRRESULT(NUMBER,70,71,2500);"TEST RESULT"

Then Print FIELD:

Heading (S/C): PATIENT List//

STORE PRINT LOGIC IN TEMPLATE:

START at PAGE: 1//

DEVICE: ;80;999  HOME  (CRT)

PATIENT List                               OCT 30, 2017@07:48   PAGE 1

TEST

CURRENT ADMISSION     NAME                  RESULT

-----------------------------------------------------------------------

JAN 13,2011@10:16:57  SQDYSE,HAD AHH        0.0 %;1/6/11@07:00

FEB 4,2011@14:05:40   OIDA,KXNI L CU        1.7 %;2/15/11@07:00

FEB 11,2011@20:22:57  PXAHB,HIZRYI P        11.1 fL;3/7/11@07:00

FEB 15,2011@10:46     HRSZLJEHU,BHUZDS F    12.1 %;2/14/11@07:00

FEB 23,2011@10:13:29  PUXL,TLRA G           1.8 %;1/14/11@10:15

FEB 23,2011@15:07:16  MLJELDY,FDAKHUSX S    8.9 fL;3/7/11@07:00:01

==================================================================

The function can also be invoked from the PRESCRIPTION (#52) file for a given drug, as shown below. Note that the patient number is referenced as INTERNAL(PATIENT).

Example #2 from the PRESCRIPTION file:

Print File Entries

Output from what File: PRESCRIPTION//     (10490531 entries)

Sort by: RX #// 'ISSUE DATE

Start with ISSUE DATE: FIRST// 4/2/2007  (APR 02, 2007)

Go to ISSUE DATE: LAST// 4/2/2007  (APR 02, 2007)

Within ISSUE DATE, Sort by: DRUG["IBUPROFEN"

First Print FIELD: .01  RX #

Then Print FIELD: 1  ISSUE DATE

Then Print FIELD: 6  DRUG

Then Print FIELD: LRRESULT(INTERNAL(PATIENT),72,1603,720);"Creatinine

-720 days"

Then Print FIELD:

Heading (S/C): PRESCRIPTION List//

STORE PRINT LOGIC IN TEMPLATE:

START at PAGE: 1//

DEVICE:   HOME (CRT)    Right Margin: 80//

PRESCRIPTION List                      NOV 20, 2017@16:17    PAGE 1

Creatinine

RX #         ISSUE DATE   DRUG                            -720 days

--------------------------------------------------------------------------

######      APR 2,2007   IBUPROFEN 800MG TAB               1.25

mg/dL;4/11/16@09:07:56

######      APR 2,2007   IBUPROFEN 800MG TAB               1.25

mg/dL;4/11/16@09:07:56

######      APR 2,2007   IBUPROFEN 800MG TAB               1.13

mg/dL;3/28/16@12:30

######      APR 2,2007   IBUPROFEN 800MG TAB               NONE FOUND IN

LAST 720DAYS

INSTRUMENTATION AND INTERFACING


## NOTES:

## Instrumentation and Interfacing

### 13 Introduction

Since interfacing instruments is such an important part of the modern laboratory, all users should be familiar with the process of “interfacing” and why it is not just a “plug the machine in” process as many instrument sales representatives claim.

### 14 Supervisors/Choosers of Instrumentation

* **WARNING:** If you are involved with selecting an instrument to use in your Laboratory, be aware that there are three possible scenarios facing you when you decide to interface.

1. There is a completed approved interface routine written for that particular instrument. It may be unidirectional or it may be bidirectional, but either way, it has been tested and works at other DHCP sites.

There is an interface routine written for that particular instrument but it has not been completely tested. It may still be in Alpha test (first try) or Beta test (later tries). In this case, you have the option of waiting until other sites finish the testing or becoming an Alpha/Beta site. If you choose to become a test site, you will have to commit your time and IRM time to checking the data for problems and working with the developer to correct those problems.

There is not an interface routine written for that particular instrument. In this case, you can become an Alpha site yourself or you can wait until another site purchases the instrument, goes through the process of having the routine created and approved. If you choose to become a test site, remember that you will have to commit your time and IRM time to checking the data for problems and working with the developer to correct those problems.

**NOTE:** Remember, a DHCP routine must exist in order for you to effectively interface your new instrument.

It does not matter that the Manufacturer Sales Representative says that it can be interfaced. (To most Sales Representatives, that means the instrument has a RS-232 plug in the back and it can be connected to an outside computer with a standard communication line.) Without the interface program to “translate,” your DHCP system will not understand what the instrument “is saying” and where to store the data.

### 15 Load/Work Lists

The LOAD/WORK LIST file (#68.2) controls the building and printing of load/work lists. Each automated instrument has to be linked to a load/work list entry. For each load/work list entry, there is at least one profile that lists the tests and controls that are used with that profile on that load/work list. In normal operation there is at least one load/work list and profile per type of instrument and one for each bench.

For example, a multiple profiles for a load/work list might be a particular kind of test that is run on a weekly basis; e.g., a Thursday profile. At other times during the week, it is run with another profile. The definition of the profile determines what tests are going to be pulled out of the accessions to be included on that load/work list. You predefine all the various ways that you will reference that test. You may use synonyms, define it as parts of profiles or subparts of other panels or profiles in the LABORATORY TEST file (#60).

You need to specify individually in the load list Profile field (#50) those tests that need to be verified. The Build Name Only field (#2) in LOAD/WORK LIST file (#68.2) is a “YES/NO” question. If you answer “YES” the test (either single or a panel) will be used only to build the profile for the load/work list. If set to “NO”, (and the test is a single test), then the sequence of tests on the profile will be defined by the order in which they are added to this field. If set to “NO”, and the test is a panel, the test sequence will be defined by the order in which they have been added to the panel test name in LABORATORY TEST file (#60) in the Lab tests included in Panel field (#200).

For example, if you enter a load/work list for Electrolytes and define one profile for the list, also called Electrolytes. Into this profile you will be putting the **single tests** Na, K, Cl, and CO2 from LABORATORY TEST file (#60). Set these tests BUILD NAME ONLY=NO. Also, add the panel LYTES which includes all these tests and set its BUILD NAME ONLY=YES.

### 16 Instrument Data Flow

The general flow of data from the instrument to the computer to verification is described here. The first staging of the data is in the LSI INTERFACE. The data is stored with a flag as to what hardware port the data came from. The data is sent from the LSI INTERFACE to the host system one at a time (with handshaking) by the LAB routine and then goes into the ^LA global with the first subscript representing the individual instrument line using the internal entry # for the instrument from the AUTO INSTRUMENT file (#62.4). This data is then processed by a special routine for that instrument and the processed data is stored in the ^LAH global until it is verified by a lab tech or deleted. When no data has accumulated for approximately 3 minute, the ^LA global for the instrument is deleted and completely removed.

The LAB routine runs continuously and looks for data from the LSI INTERFACE. As soon as the LAB routine receives data from the instrument, it starts putting the data into the ^LA global, subscripted by instrument number, and simultaneously executes the NEW DATA node for this instrument in the AUTO INSTRUMENT file  (#62.4) to start up the routine responsible for processing the data out of the ^LA global. The data that is contained in the ^LA global is the raw instrument data. If additional data is coming in from the same instrument and the ^LA global already exists, the LAB routine does not restart a new routine. The new data continues to be accumulated in the ^LA global. This means that if data already exists in the ^LA global and the routine is not running for that instrument, data will continue to accumulate in the ^LA global, but will not be processed out. This situation will exist until the LRJOB function is run to start the proper routine.

The running of the appropriate routine processes the data out of the ^LA global and stores the data in the ^LAH global. This is a temporary storage area. The AUTO INSTRUMENT file (#62.4) contains information on the tests that are run, where in the input string the test value is located, and where to store the data in the ^LAH global. This is the same as the location used in the ^LR global. Also there is a pointer to the LOAD/WORK LIST file (#68.2) that gives the subscript for the ^LAH global, what method to use in linking the data to a sample in the ACCESSION file (#68), whether to OVERLAY data and whether to process by accession number, sequence number or tray cup. The first subscript of the ^LAH global is tied uniquely to a given load/work list. If data is NOT overlaid, then each new sample’s data will get a new entry in ^LAH. If the data is to be overlaid, then a new entry will be made only if the linking variable cannot be found in the file.

***WARNING:** Neither ^LA nor ^LAH is VA FileMan compatible.

The processing of the data out of the ^LAH global is usually done during verification of instrument data. If not, it accumulates data for a day or until the CLEAR INSTRUMENT function is done. When the instrument data is cleared, data in ^LA, ^LAH is purged. Upon verification, the data from ^LAH is moved into the ^LR global. This global, ^LR(, LAB DATA file (#63) is VA FileManager compatible. All data that remains unverified stays in the ^LAH global.

To avoid confusion with data from the previous shift, the Clear Instrument/Worklist data [LRINSTCLR] option should be run at the beginning of every day (or perhaps, every shift). For example, if there is an accession number 120 verified, then that data still exists under that accession number. If you then run a new accession number 120, you would get the data from the previous accession number 120. If you ran another sample through the system for accession 120 for the current time period, you would then have two sets of data for the accession number 120. If you have ROLLOVER specified in ACCESSION file (#68) and the data is unverified, you would not be able to create a new 120. This is complicated by the fact that the AUTO INSTRUMENT file (#62.4) allows two ways of running the programs, one of which is that every sample gets a unique entry in the ^LAH global, even if it belongs to the same tray and cup and to the same person. This means you can consecutively accumulate multiple copies of data. The technologist then must make a decision about which set of data or combination of sets is correct. This cannot be batch verified. To avoid this situation you clear the instrument using the Clear Instrument/Worklist data option.

Verification (and movement of data from ^LAH to ^LR) can be accomplished two ways:

1. Use the Enter/Verify Data (auto instrument) option. This takes one accession number, one sequence number, or one tray/cup at a time, displays the data and asks for verification. When it is verified, it moves to ^LR and is then available to the wards, on cumulative reports, etc.

Use the Group Unverified Review (auto instrument) option. This prints the data from the ^LAH global. You may check it for critical values, delta checks,  etc. When you are ready to verify all or parts of the data, use the Group Verify (auto instrument) option to verify it and move it to the ^LR global. You cannot group verify data that has multiple entries of data not overlaid. If there are cases of multiple sets of data, the group verify skips the data and notifies you. The technologist must make the decision as to which data to use. To do this, use the Enter/Verify (auto instrument) option to make a manual selection.

If the Overlay Data field in the AUTO INSTRUMENT file (#62.4) is set to “YES”, then a test is overlaid by a new run of the same test. If, for example, you get an out of range check, you can rerun the sample and the values will replace the previous values. This is done for all values that are transmitted from the instrument. To correctly use this method, you must remember that new data substitutes for old data (that is, new data writes over existing data).

### 17 Automated Instrument Interfacing

The LAB routine ties a port to the LSI device (data concentrator). If multiple LSI devices are used, corresponding multiple LAB routines would have to run, and each would be designated separately (i.e., LAB1, LAB2, LAB3, etc.). They are all identical except that each one increments by 10 the internal count on the first subscript of the ^LA global. Data goes across the line that is specified as the beginning lab data line (specified in the device file). Because it goes by name (LABDATA) rather than by line number, it is always LABDATA, LABDATA1, LABDATA2, etc., depending on which line you are using.

When the LAB routine is running, any data that comes from a given line hooked to the LSI goes to the same designated number line in the ^LA global; (i.e., if it comes out of line number 5 it would go into ^LA(5,. At the same time, if this is new data and nothing exists in the ^LA(5, global), the LAB program starts up whatever appropriate automated instrument routine belongs to number 5 as defined in the AUTO INSTRUMENT file (#62.4). The AUTO INSTRUMENT file (#62.4) is number meaningful in that the Field #.001 is defined. The individual entries tie to individual devices. For example, if you have multiple Coulters, you would have multiple entries with a different name for each Coulter, in the AUTO INSTRUMENT file (#62.4) (e.g., coulter1, coulter2). It is essentially a one to one mapping of line to the specific instrument.

If the data is already defined in the ^LA global and the processing routine is not running, data will continue to accumulate in that ^LA global and nothing will happen to it. The LAB program assumes that the target global already exists and the processing routine is running. If the target global does not exist, it assumes that the program is not running and tasks the routine to process that global.

AUTO INSTRUMENT file (#62.4) determines what load listing mechanism it is supposed to use for moving the data in the ^LAH global. The ^LAH global is defined in the LOAD/WORK LIST file (#68.2). The ^LAH global is a temporary global where data is brought in and retained sequentially. Each succeeding piece of data is stored in the ^LAH global and its first subscript based on the same subscript as the entries in the File #68.2. When the data is verified and placed in the ^LR global, it is removed from the ^LAH global.

**NOTE:** If you need help with an Auto Instrument, your respective ISC will be very happy if you can supply them a hard copy of the routines being run, a copy of the ^LAH and ^LA globals, parameters from the instrument, version of the software on the instrument, and a hard copy of the AUTO INSTRUMENT file (#62.4).

#### Automated Instrument Data Flow

#### AUTO INSTRUMENT file (#62.4) Fields List

The AUTO INSTRUMENT file (#62.4) contains all specific information related to each automated instrument in the laboratory. It is used to define the site specific parameters by which each instrument will be run, including what automated interface routine program will be used, the type of load or work list that will be run on the instrument, and the individual tests which will generate data from that instrument. The file specifically defines for each instrument the name, echo device, program, load/work list, entry for LAGEN routine, lab test associated with the instrument, WKLD suffix code, and alarm terminal (the alerting terminal when the interface line is not working).

It is necessary to review and edit this file prior to interfacing any automated instruments to be run on-line. For more complete information on how this is accomplished and the implications of editing this file, please refer to the section of this manual entitled Instrumentation/Interfacing.

(.001) NUMBER

(.01) NAME

(.14) WKLD METHOD

(.15) WKLD CODE METHOD NAME

(.16) WKLD CODE SUFFIX

(1) ECHO DEVICE

(2) PROGRAM

(3) LOAD/WORK LIST

(5) ENTRY for LAGEN ROUTINE

(6) CROSS LINKED BY

(9) *ECHO ALL INPUT

(10) METHOD

(11) DEFAULT ACCESSION AREA

(12) OVERLAY DATA

(20) NEW DATA

(25) RESTART

(26) HANDSHAKE RESPONSE

(27) ACK TRIGGER VALUE

(28) ACK RESPONSE VALUE

(29) DIRECT DEVICE

(30) CHEM TESTS (Subfile 62.41)

(.001) Number

(.01) Test

(2) Param 1

(3) Param 2

(4) Param 3

(6) Download Code

(11) Routine Storage

(31) LOAD CHEM TESTS

(40) ALARM TERMINAL (Subfile 62.42)

(.01) Alarm Terminal

(60) MICRO CARD TYPE (Subfile 62.43)

(.01) Micro Card Type

(.5) Card Name

(.7) Process Card Call

(1) Organism (Subfile 62.44)

(.01) Organism

(1) Card Code For Organism

(2) Drug (Subfile 62.46)

(.001) Number

(.01) Drug

(1) Drug Node

(2) Param 1

(3) Card Code

(4) Display Order

(9) Section

(10) Bit Position

(3) Message (Subfile 62.461)

(.001) Number

(.01) Code

(2) Flag Value

(3) Message

(70) INTERFACE NOTES

(91) DOWNLOAD ENTRY

(92) DOWNLOAD PROTOCOL ROUTINE

(93) FILE BUILD ENTRY

(94) FILE BUILD ROUTINE

(95) SEND TRAY/CUP LOCATION

(96) QUEUE BUILD

(97) MICRO INTERPRETATION CHECK

(100) METH NAME

(101) MEAN DATA VALUE 1

(102) MEAN DATA VALUE 2

(103) MEAN DATA VALUE 3

(105) MICRO AUTO APPROVAL METHOD

(106) DEFAULT AUTO MICRO TEST

(107) SITE NOTES DATE (Subfile 62.4107)

(.01) Site Notes Date

(1) TEXT (Subfile 62.41071)

(.01) Text

#### AUTO INSTRUMENT file (#62.4) Fields Description

**(.001) NUMBER:** The internal number assigned by the system whenever an entry is added. Do not edit.

**(.01) NAME:** This is the name (3-30 characters) of the instrument. If you have more than one of the same instrument, be sure to designate them; e.g., Ektachem 400-I and Ektachem 400-II.

**(.14) WKLD METHOD:** This field indicates what method the system should use as a default method for workload identification purposes.

**(.15) WKLD CODE METHOD NAME:** This field is automatically filled in when a selection of WKLD code method name is made. I represents an eye readable name of the code selected.

**(.16) WKLD CODE SUFFIX:** This field indicates what suffix should be used as a default suffix code for this instrument.

**(1) ECHO DEVICE:** Echo of raw instrument data to a CRT or a printer is no longer supported. This field is used when setting up a LSI or a direct connect auto instrument. Refer to the section on automated instrument file set up for more information. This field identifies the device name that the auto instrument data line is connected.

**(2) PROGRAM:** The free text name of the interface routine (copies of the presupplied entries in this file. If the program (routine) is not listed here in the exported version for your instrument, contact your regional ISC or Site Manager to see whether the appropriate routine is available.

**(3) LOAD/WORK LIST:** Points to the LOAD/WORK LIST file (#68.2). This is a required field. Choose the load/work list name that will be used for this instrument if you plan to run by list. If you plan to run by accession number, this field must also be filled in with the name of the load/work list, even though you may not use it when running the instrument.

**(5) ENTRY FOR LAGEN ROUTINE:** Choose from a set of codes based on how you plan to run this instrument. (This entry sets up the correct cross-reference between the raw data and the patient or specimen identification.)

You may have to test different combinations, depending on the particular interface routine and/or the way your instrument transmits the raw data, especially if you are lucky enough to have an older or more obsolete instrument. Check with the instrumentation/interface portion of this guide for more information.

**(6) CROSS LINKED BY:** This field specifies a variable from the interface program which helps set up the cross-reference between data and sample, and is dependent on the interface routine itself. (See the instrumentation/interface section.)

**(9) *ECHO ALL INPUT:** If the echo device field has been filled in, answering “YES” will tell the system to echo all data to that device. If you choose “NO”, no data will be echoed. This field will be deleted in later version.

**(10) METHOD:** A free text field (1-20 Characters) specifying the method of the testing performed by the instrument. (It is easiest to fill this in with the instrument name.)

**(11) DEFAULT ACCESSION AREA:** Points to the ACCESSION file (#68) and defines a default accession area from which the tests run on the instrument are pulled. (If no accession area is specified, as in the case of running by accession, when only the numeric portion of the entire accession is specified, the system will assign that accession number to the default accession area listed here as an entry.) If the load/worklist field has been filled in, this field should match the accession area for that list.

**(12) OVERLAY DATA:** Setting this field to “YES” will allow data to overlay (or replace) previous unverified data (i.e., when specimens are rerun). If you set this field to “NO”, the second set of data will be transmitted **in addition to** the existing data. You would have to clear instrument data to remove the previous data first, and then re-run the specimens, especially if you will be group reviewing and verifying.

**(20) NEW DATA:** For most instruments, this field will have an entry of D NEW^LASET. This is a string of executable code which is used whenever a new string of data starts to come from the automated instrument.

**(25) RESTART:** This is a string of executable code which restarts everything for this particular instrument if there has been a power failure, or if the routines have become totally lost.

**(26) HANDSHAKE RESPONSE:** If the instrument requires a handshake response, this field contains the executable MUMPS code to set the response into the variable OUT. S OUT=$C (6) (OUT contains the ASCII character 6 “ACK”)

**(27) ACK TRIGGER VALUE:** This field contains the ASCII sequence use to acknowledge an auto instrument. Not all instruments utilize this field. This is the decimal value that will trigger the ACK response (0-99).

**(28) ACK RESPONSE VALUE:** If this instrument setup instructions indicate a standard ACK value is required by the instrument, enter the $C(X) for the acknowledgment. Not all instruments make use of this field. Where X= the ASCII number of the ACK character.

**(29) DIRECT DEVICE:** This field is used when bypassing the LSI. It is the name of the device that is used to communicate with a direct connect instrument.

**(30) CHEM TESTS (Subfile):** This is actually a misnomer - it should read TESTS or LAB TESTS, since the entries in this multiple field specify the laboratory test names which will be run (generate data) on the instrument. (You do not run chem tests on a Coulter!)

**(.001) Number:** Internal entry number of the test entry in this field, assigned by the system. Can only be changed if you delete the test first, and re-enter it. This number may be meaningful to the auto instrument and how it identifies the test.

**(.01) Test:** Points to the appropriate test(s) in the LABORATORY TEST file (#60). Again these entries can be changed only by deleting them first and then re-entering.

**(2) PARAM 1:** This is used to extract a test from a data stream. It may contain a line number or character number. Set by LASET into TC(I,2) this field. Check the interface notes or review the routine.

**(3) PARAM 2:** This is used to extract a test from a data stream. It may contain a line number or character number set by LASET into TC(I,3) in this field. Type a whole number between 0 and 10000. Refer to the instrumentation/interface section for information about these five fields.

**(4) PARAM 3:** This is used to extract a test from a data stream. It may contain a line number or character number set by LASET into TC(I,4) in this field.

**(6) Download Code:** This is the code to send the instrument for downloading of load lists that this test is requested.

**(11) Routine Storage:** Pointer to the LAB DATA file (#63) and is triggered by the test name, above. Do not edit.

**(31) LOAD CHEM TESTS:** This field is used by the LASET routine to determine what to do with the chem test subfile. T or blank moves the data into the TC array. U moves the data into the ^TMP(“LA”,$J, global. N will not move at all. Set according to needs of instrument routine.

**(40) ALARM TERMINAL (Subfile):** A multiple field to be filled in with the device name(s) where a warning message will print should the LSI/interface stop.

**(.01) Alarm Terminal:** This field contains the name/numbers of devices which will report the status of the interface. This points to the DEVICE (#3.5). Enter the device names that should be told of a LSI interface stop.

**(60) MICRO CARD TYPE (Subfile):** This entire subfile is at present devoted to supporting bidirectional interfacing of the Microbiology auto instrument. If you are not attempting to interface one of these types of instruments, you may ignore this entire subfile. If you are attempting to interface such an instrument, consult Microbiology Instruments Guide. There are examples available for various instruments.

**(.01) Micro Card Type:** Enter the Micro Card Type. Answer must be 1-4 characters in length (Instrument card type). This is a HEX code which represent the card type. OE=GRAM.

**(.5) Card Name:** Enter the Card Type Name e.g., Gram Neg Id Card Name. Refer to the instrumentation/interface section of the guide for information.

**(7) Process Card Call:** If a routine is required to process incoming data from the instrument, enter a routine name. See interface notes for routine(s) names. These fields have been added to facilitate the interfacing of microbiology instruments.

**(1) Organism (Subfile):** This subfield contains a list of possible identifiable organism which can be identified on or by this card. It is a multiple field and contains particulars for each organism.

**(.01) Organism:** Enter the name of organism which is in ETIOLOGY file (#61.2). This file will only allow organism which are either Bacterium, Fungus, or Mycobacterium identifiers.

**(1) Card Code For Organism:** Enter the card code for this organism. It is usually a two digit Hex code.

**(2) Drug (Subfile):** This subfield contains a list of drugs which Card is capable of testing and reporting.

**(.001) Number:** Enter the number used by the instrument to identify the drug in uploaded data stream. Enter 1-99 matching the index from the instrument.

**(.01) Drug:** Field 4 under the existing multiple field Drug, called display order, has been added. This is to assist Micro in displaying the drugs in the order in which they come off the instrument.

**(1) Drug node:** Enter the drug name which the number corresponds to in File #62.06.

**(2) PARAM1:** Enter a MUMPS code string needed to convert/extract data into the variable V. This field is similar to Param 1 fields in other auto instruments. The name has been changed to prevent confusion in referring to the two fields.

**(3) Card code:** This is the code from the card to do the lookup on. On each card it is possible to have codes represent different messages or canned comments. This subfield identifies the relationship. Enter the code, the card upload data will be contained.

**(4) Display Order:** Enter a number between 1-100 for display order, or 0 for file entry order.

**(9) Section:** Answer must be 2-30 characters in length.

**(10) Bit Position:** What bit (number of characters from the left) position the drug is located.

**(3) Message (Subfile):** For each card code, there can be an associated message to represent that code. This subfield setup that relationship.

**(.001) Number:** Type a whole number between 1 and 99. This field represents the internal file number for this message. This number must be unique to the file.

**(01) Code:** Message code, entry must be 1-10 characters in length.

**(2) Flag value:** This field contains the flag value sent by the instrument with the upload data. Value if matches then include msg.

**(3) Message:** When the flag value is detected this message will be used. This field is similar to the LAB DESCRIPTION file and Expanded comments.

**(70) INTERFACE NOTES:** This word processing field contains notes on how to set up the instrument and other pertinent information on interfacing the instrument, entered by lab package developers.

**(91) DOWNLOAD ENTRY:** This field is used to indicate an entry point into the routine used to do the actual downloading of data to the instrument.

**(92) DOWNLOAD PROTOCOL ROUTINE:** This field is used to indicate the routine used to do the actual downloading of records to instrument.

**(93) FILE BUILD ENTRY:** This field is used to indicate the entry point into a routine that is used to reformat the worklist record for transmission and place it in the 0 nodes of the LA global.

**(94) FILE BUILD ROUTINE:** This field is the name of the routine which is used to reformat the worklist records for transmission.

**(95) SEND TRAY/CUP LOCATION:** This field will contain the default to the question, Send Tray/Cup location, used by the same bidirectional routines.

**(96) QUEUE BUILD:** This field contains the Default answer to Queue to build Question.

**(97) MICRO INTERPRETATION CHECK:** This field specifies how the data being processed should be handled.

**(100) METH NAME:** Pointer to the method field of this file, and will be stuffed automatically. Refers to the statistical method used by the instrument.

**(101) MEAN DATA VALUE 1:** These fields should contain the expected mean values of the first, second, and third results.

**(102)MEAN DATA VALUE 2:** A group of three results to be used in the Bull Algorithm quality control calculations.

**(103) MEAN DATA VALUE 3:** Example, the MCV, MCH, and MCHC values from a CBC.

**(105) MICRO AUTO APPROVAL METHOD:** This field selects the method to be used with this instrument during verification. This entry will allow “RPT DATE APPROVAL” prompt during verification. The default is VS (Verify Supervisor). If one wants the report to release and verified, enter VS, otherwise a supervisor must release the report before being verified and printed to the cumulative.

**NOTE:** The Micro Auto Approval Method field (#105) is associated with the Micro Approval Method field in the LAB REPORTS file (#64.5). Make sure the fields agree and are appropriate for your site. **This field is only used for MICROBIOLOGY AUTOMATED INSTRUMENTS.**

**(106) DEFAULT AUTO MICRO TEST:** This is the default Laboratory test name to be used to record workload for each organism when using the Automated Micro Instrument to verify test.

**(107) SITE NOTES DATE (Subfile):** Date of the note.

**(.01) Site Notes Date:** Date

**(1) TEXT (Subfile):** The actual text of the note. This is a word processing 	field.

**(.01) Text:** The actual text of the note.

### 18 Bidirectional Communications

Bidirectional communications of Laboratory instruments can be done at your site if the following items have been accomplished:

1.	Version 2 EPROM chips have been installed in the LSI. These chips may be obtained from your regional ISC.

2.	Version 5.1 or greater of the DHCP Automatic Lab instruments package has been installed.

3.	DHCP bidirectional routines have been written for the instrument to be interfaced. These routines will include the bi-directional communication routine(s) for downloading and uploading, routine(s) to move the data from ^LA to the ^LAH globals, and may also include verification routine(s) in the case of microbiology instruments.

4.	The AUTOMATED INSTRUMENT file (#62.4) has been properly defined for the instrument to be interfaced.

5.	A LOAD/WORK LIST file (#68.2) has been properly defined.

6.	Ability of the instrument to function in the bidirectional mode. This ability should have documentation provided by the instrument manufacturer which should include complete information on the bidirectional communications protocol and procedure, instrument setup (there may be many ways to configure an instrument), and an example of the expected download and upload data stream.

It is important to mention that there are no industry standards which define bidirectional communications. This means each manufacturer may have completely different approaches to the problem of downloading and uploading information from an instrument to and from a host CPU. Each instrument is a completely separate experience. For this chapter we have defined the term “download” as patient demographic data, specimen and test information and other necessary data required to perform and report test results sent from the host CPU to the instrument. Upload is defined as data sent from the automated instrument to the host CPU as completed test result and other information necessary for the verification and reporting of test results in the DHCP laboratory software. For example, the communication protocol KERMIT, used by Kodak in their Ektachem, is the choice of the manufacturer and may not be the choice of other instrument manufacturers.


#### Handshake Routines (Bi-directional)

The handshake program called by the Lab program is used to check the incoming records. The program has several responsibilities:

1. Check for the start of the data block.

2. Calculate the checksum for the data block.

3. Check for the end of the data block.

4. Compare the calculated checksum to the checksum received in the data block.

5. If the checksum is correct, the program may send an acknowledgment that it has received the data correctly if it is required, and send the next block of data to the instrument, or do nothing but return to the Lab program.

6. If the checksum is invalid, the program resets the “I” subscript entry so that the next record received will overwrite the bad record and send a negative acknowledgment to the instrument if it is required.

7. If a record is to be sent to the instrument, the appropriate number of requests for service are generated in the “Q” subscript of the ^LA global and the program returns to the Lab program for actual sending of the record(s).

#### Processing Routine

Each instrument has a unique single routine. The Lab program will find which routine to use from the Program field of the AUTOMATED INSTRUMENT file (#62.4) for each automated instrument that is interfaced. The processing routine also has several responsibilities:

1. Gets data from the ^LA global.

2. Determines the accession number.

3. Breaks out the raw data into individual elements.

4. Manipulates the raw data from the instrument.

5. Stores manipulated data in ^LAH( Load/Work list #, for that accession number.

Storage of data in ^LA is done in three main areas. Results data being received is stored sequentially under the ^LA(T, “I” subscript for each instrument (where T is the internal number of the AUTO INSTRUMENT file (#62.4). Download data is stored sequentially under the ^LA(T, O subscript for each instrument. An additional area under the Q subscript is used to indicate service requests made for each instrument. These service requests are stored sequentially so that the requests are processed in a first-in-first-out (FIFO) manner. An instrument requesting service for incoming records or by the download programs for outgoing records lists its request under this Q node.

The following is an example of ^LA for instrument T: (Where T = Instrument #)

^LA(T,”I”)	=34	The total number of records received

^LA(T,”I”,0)	=1	Number of records processed

^LA(T,”I”,1)	=data	Data received from instrument T

^LA(T,”I”,34)	=data	Last record of data received

^LA(T,”O”)	=10	Total number of records to be sent

^LA(T,”O”,0)	=1	Number of last record sent to instrument T

^LA(T,”O”,1)	=data	Record to be sent to instrument T

^LA(T,”O”,10)	=data	Last record to be sent

^LA(“Q”)	=25	Last request number for service

^LA(“Q”,25)	=7	Service request to LAB program from instrument on port 7 of LSI

#### Download Routine [LA DOWN]

This option invokes an instrument specific routine to process a load worklist for downloading to the instrument. The option will prompt you with a series of questions relating to the building of the download record. Care must be taken to ensure that only the desired accessions are built on the worklist.

The building of the download records are performed in two steps:

**Step 1:** All of the accessions which have tests indicated on the load worklist are collected and stored in the load worklist file, indexed by cup.

**Step 2:** The protocol converting process transforms the data stored at the above node into the correct format for downloading, which includes headers, checksum, and end of file marker.

It usually requires several programs to execute a bidirectional protocol, and they are namespaced accordingly.

#### Related Fields

With the advent of bidirectional software, several fields were added to the file. It is recommended that a new set of file attributes be generated for Version 5.1 or later versions.

**LABORATORY TEST file (#60)**

Field #412, called Culture ID prefix, is used to indicate to the VITEK that this is a test to be downloaded and used to indicate a multiplier factor. This is so multiple tests can be downloaded for one accession.

**AUTO INSTRUMENT file (#62.4)**

Field #91, called Download entry, is used to indicate an entry point (line tag) into the download protocol routine.

Field #92, called Download protocol routine, is used to indicate the routine used to do the actual downloading of data records to the auto instrument.

Field #93, called File build entry, is used to indicate the entry point into (line tag) a File Build routine.

Field #94, called File build routine, is used to enter the name of the routine which is used to reformat the load/worklist records for transmission and places the reformatted record in the O nodes of the ^LA global.

Field #95, called Send tray/cup, is used to indicate the default answer to the question Send tray/cup.

Field #96, called Queue build, is used to indicate the default answer to the question, Queue build.

Field #4, under the existing field Micro Card multiple field Drug called display order has been added. This is to assist Micro in displaying the drugs in the order in which they come off the instrument.

Field #6, under the existing multiple field Chem tests, is where a new field called Download code has been added. This new field is used to store the character code that is used in the download to indicate the actual laboratory test to be run.

**LABORATORY SITE file (#69.9)**

Field #210, called Download Full Data, is used to indicate to the download routine how much data to download to the instrument. If a site answers “NO” to this field, the download routine will only download the instrument required fields. If “YES” is answered to this field, the download routine will download all possible data fields that the instrument will accept. The time taken to download each record and storage capacity of the instrument are the issues here. The smaller the download record, the less time it will take to complete the process. Check your automated instrument setup and try to send the minimum amount of data necessary to meet the auto instrument and your site requirements.

### 19 Version 2 LSI Eprom Installation

There are two methods for upgrading the LSI with the Version 2 Eprom chips.

A.	If you do not have the expertise available to change the EPROM chips, you can call your regional ISC for advice on installing the new chips.

**NOTE:** Some ISCs may also provide installation of the chips at the ISC. This, of course, should be arranged in advance of sending the LSI to an ISC. Each ISC will have its own policy about EPROM chip installation.

B.	If you do have the expertise available to change the chips, you can use the following procedure to do the upgrade/installation.

1. If your LSI is on-line to the system, shut down the Lab program gracefully. This is done by entering the following command in programmer mode in the UCI and on the CPU where the Lab routine is running. Be sure to do a system status to verify where the Lab routine is running and do not shut down the Lab routine if any automated instruments are still sending automated testing data.

S ^LA(“STOP”,x)=““ where x = Instrument number (i.e., 1 for the first LSI and 11 for the second LSI, etc.,)

For example: S ^LA(“STOP”,1)=““
will stop the LAB routine for a systems first LSI.

**NOTE:** If your LSI is not on line, or you are planning to change the EPROMs in the backup LSI, it is very important to check out the backup/inactive LSI in the unidirectional mode first. Do this by switching LSIs and running the backup LSI and checking it out with ALL AUTOMATED INSTRUMENTS THAT HAVE BEEN INTERFACED with exactly the same four wire phone cables. This will check the functionality and wire wrapping of the backup LSI. If a particular automated instrument works with the first LSI and does not work with the second LSI, first check that the RJ11 plug is properly plugged in, then check the wire wrapping of the second LSI on the port that does not work. **** If the LSI has been sent out for repair, many times boards may be exchanged at the repair shop and your wire wrapping is altered. The best way to ensure that both LSIs are always working properly is to rotate the LSIs on a regular basis.

2. Do a system status to verify that the LAB routine has stopped. If the LAB routine has stopped, turn off the LSI.

3. Disconnect power from the LSI.

4. Disconnect the CPU line to port 1 on the LSI.

5. Remove 2 screws from the rear of the LSI where ports are connected.

6. Carefully lower the panel, remove and label the cables from the top two boards before disconnecting.

* **WARNING:** For the following steps, it is advisable to have some means of grounding yourself and the board work area to eliminate the possibility of differential ground potentials which could damage the board components or EPROM chips. Most biomedical engineering sections will have grounding equipment and anti-static foam to place the LSI boards and new EPROM chips on. Adherence to the above caution will ensure a trouble-free EPROM chip installation.

7. Carefully remove the top board from the card cage and lay it on the work area with the gold edge connector on your left and the 2-ribbon connector plugs on your right.

8. Referring to figure 2-1 on page 2-2 of the General Digital GDC 2100 Data Concentrator Maintenance and Operations Manual, locate sockets XE39 and XE32 in the upper center of the board. These pages are also included in the appendix at the end of this chapter.

**LSI Graphic - Processor Board**

9.	Orient the new chips with the chips in XE39 and XE32.

**NOTE:** The new EPROM chips you receive may look different from the chips that are in the LSI. The chip may have a notch in the end, a cut corner, a small dot in one corner or some other type of corner marking. This marking is used to determine which corner pin is Pin number 1 of the chip. It is critical that the new EPROM chip be installed in exactly the same orientation as the old one. This is done by locating where the pin number 1 is on the old and the new chip. To properly align PIN 1 of the chip, place the notch or the small dot pointing to the right or toward the handle.

10.	The chip in XE39 is the LOW byte (bits 0-7) chip and the chip in XD32 is the HIGH byte (bits 8-15) chip and the new chips should be oriented in the same manner, ensuring that PIN 1 is inserted into the PIN 1 slot.

**NOTE:** It is very important to be careful when installing the new chips to know where pin 1 is, avoid damaging any of the pins and to be sure all pins are seated in the chip holder on the board. This can be accomplished by following the notes and instructions about PIN 1 and holding the chip at an angle and starting to seat all pins on one side of the chip into the socket. Using gentle pressure toward the seated side and downward, rotate the chip until the pins from the other side are seated into the socket. Then apply pressure to the center of the chip and/or to both ends and seat the new chip firmly into the socket.

11.	Using a chip remover, remove chips from XE39 (LOW byte) site, observing where pin 1 is. Install the new EPROM LOW bye chip with pin 1 in the proper orientation. Remove the XD32 (HIGH byte) chip and install the new EPROM HIGH byte chip, being careful to observe where pin 1 is located.

12.	Replace the board in the empty top position card cage of the LSI, making sure it is fully seated.

**NOTE:** The new EPROM chips check the baud rate, parity, number of data bits and number of stop bits more stringently than the Version 1 chips. Even though your automated instruments worked with the old chips, there may be configuration inconsistencies between the LSI and your automated instruments with the new EPROM chips. For this reason, while you have the LSI opened up, double check the port boards (DLV11J’s) in the LSI to be sure the baud rate, number of stop bits, number of data bits and parity are EXACTLY that which the instrument(s) are transmitting. If the setting(s) are not correct, you may get no data, a mix of lower case and upper case characters, or get garbled data in the ^LA global. Parity was not checked adequately in the Version 1 chip. This has been corrected in the Version 2 chip, so if your site has problems, we suggest looking at this wire wrap first. If you have questions on wire wrapping, refer to the section in this manual. You should also have handy the interface information supplied by the AUTOMATED instrument manufacturer and double check what parameters the automated instrument is set to transmit. If there are transmission inconsistencies, change the one that is easiest for your site.

13.	Double check the port boards (DLV11Js) to be sure that the baud rate, number of stop bits, number of data bits and the parity are EXACTLY that which the automated instrument is transmitting. Refer to the above note if there are inconsistencies. If you are not sure about the port numbering sequence, refer to the diagram in this chapter on LSI Interface ports.

14.	Reconnect the removed cables to their proper locations.

15.	Raise and replace the panel and screws removed in steps 5 and 6.

**NOTE:** It is now time to do some verification that the installation of the new EPROM chip has been successful. This verification should be done in a step by step mode for the best results.

16.	Using a RJ11 four wire system, connect a CRT terminal to port 1 of the LSI. Additional information on wiring configuration is elsewhere in this section.

17.	Set the CRT for 2400 baud, no parity, 8 data bit characters and 1 stop bit.

18.	Reconnect the power to the LSI.

19.	Turn on the LSI Interface.

20.	After a few seconds you should see a startup message that looks something like:

**STARTED V 2.24 XXXXXXXXX**

If you do not see this message, go back and double check all your work to be sure everything is right, including your terminal cable pins 2 and 3.

21.	When you see the STARTUP message, on the CRT, all upper case, type T00L000&lt;RET&gt;&lt;RET&gt; (these are number zero, and not the letter O).

22.	If you see the character A on the screen, everything is fine and you can continue to the next step. If you see nothing, double check the lines from the LSI to the terminal and return to step 20. If this does not help and you are still not able to obtain the A character on the CRT, call your ISC for help.

23.	Shut off the interface.

24.	Disconnect the CRT from port 1 of the LSI and reconnect the CPU line to the LSI port 1.

25.	Modify the system device table for the Device Number (IO) the LSI is connected to, from 1200 to 2400 baud.

26.	Use Test the Interface option [LA LAB Test] to verify that the LSI can communicate to the host CPU and the host CPU can transmit to the LSI. If the option is successful, you will get the message:

STARTED V2.24 XXXXXXXXXX

followed by additional line by line information as the LSI and host CPU communicate with each other. A Control C will exit the option when you are satisfied all is working OK. If you do not get the STARTED message, do a Control C and run the option again.

When you are prompted to turn off and then on the LSI, be sure the LSI is off for a full five seconds. If you still do not get the STARTED message, go back to step 24 to check your RJ11 connection and then check each additional step. If you are still unable to get the STARTED message, call your ISC for assistance.

27.	Restart the LAB program using the Restart processing of instrument data option [LA JOB]. The option sometimes takes 10 to 30 seconds to start the LAB job, so be sure to not start the LAB job more than once. If the LAB job does not start, contact your System Manager/IRM Chief for help in starting the LAB job.

28.	After the LAB job has been successfully started, run the Check the Interface [LA 1103] option to verify that the lab interface system is OK and ready to transmit automated instrument data.

29.	If the Check the Interface report is OK, then run each automated instrument in the UNIDIRECTIONAL mode that they were  running in before installing the new EPROM chips. See if you are able to verify results from each automated instrument, using the EA (Enter/Verify Data-Auto Instrument) [LRVR] option, or whatever option your site uses to verify test results from interfaced automated instruments.

30.	You have now successfully completed the installation of the new EPROM chips. Please mail the old chips back to your ISC in the chip carrier the chips were sent to you in, for recycling. (Please do this quickly, since there is a limited supply of the EPROM chips.)

#### LSI Wire Wrapping

The following steps should be taken to reconfigure the LSI. Be sure the unit is unplugged and the area is free of static. The boards requiring reconfiguration are DLV11J DEC boards.

1. Place LSI on table with RJ11 phone jacks facing you.

Remove two screw which hold the RJ11 panel to the LSI.

Carefully lower the RJ11 panel.

The ribbon cable is connected to three boards. The top board is the processor and needs no adjustments. Make sure to number or mark the tags on the wire cables before you remove them from the plugs. Carefully remove the appropriate board. The middle board corresponds to 1J3 through 1J0, while the lower board corresponds to 2J3 through 2J0. The board slides out through the space created by the RJ11 panel removal. Pull gently on the two thumb tabs located on either side of the board. A gentle rocking to either side may dislodge the board easier. Place the board alongside of the LSI so the four plugs remain at the front of the RJ11 panel of the LSI and so the little black chips on the board face up. Rotate the board 180 degrees so you can read the lettering on the board.

Inspect the board for loose wires and/or chips. On the lower left is a 3 x 9 row set of pins with tiny wires wrapped around some of the pins. It is labeled A5 at the left and 01X at the bottom. At the lower right is another set of pins labeled A6 and BXH. These pins determine the address and vector jumpers for the processor and do not require any change. At the top left and top right are 4 x 3 rows of pins. These pins configure the DLV11J board to be RS232 or RS423 EIA-compatible. These sets of pins do not need to be changed. At the top center of the board is a set of 2 x 5 row pins and one set of three pins. The factory has pins 0, 1, 2, 3 connected to pin W. The W corresponds to 1200 baud and by connecting the W to 0, 1, 2, 3, all 4 RJ11 phone ports are set for 1200 baud. The numbers correspond to the RJ11 ports, while each letter corresponds to a different baud rate (letter: U=150, T=300, V=600, W=1200, 6=4800, N=9600, K-19200, Z=38400). The wires are frequently daisy chain wire wrapped. Along the left side of the board are four sets of 3 x 4 rows of pins. The top set is labeled CH0 for the corresponding J0 RJ11 jack and its left label is EDSP. There are wire wraps or blue chips on the pins. The pins determine the other line parameters (D=data bits, S=stop bits, P=parity inhibit, E=even parity enabled).

Wire wrap the appropriate pins using a wire wrap tool. The tool is usually available in your BMET shop.

**Example:** I want to change P2 and 2J3, 2J2, and 2J1 to 2400 baud, no parity, 1 stop, and 7 data bits. I want to change 2J0 to 4800 baud, even parity, 1 stop, and 8 data bits.

**Solution 1:**

P2 is factory set to 1200 baud, no parity, 8 data bits, and 1 stop bit. This should not be changed. The wire wrap is on the processor board and is different from the previous discussion. It is unlikely that you will have 9 devices interfaced, and you should save this channel (P2) for last. If problems develop, you can fall back to this channel.

**Solution 2:**

To set 2J3, 2J2, 2J1, to 2400 baud, find the top center set of pins and unjumper the leads from 1, 2, 3, to W and re-jumper 1, 2, 3, to Y. Unjumper pin 0 to W and rejumper 0 to pin L. Avoid touching other pins with un-insulated wires. To set 2J3, 2J2, 2J1, to no parity, locate the left hand 4 sets of 3 x 4 pins and verify for CH3, CH2, CH1, the P letter has the right two pins jumpered (1 and X pins). Remember, this is factory preset to no parity. The E jumper must be connected from X to 0 or 1 even if the parity bit is disabled. Verify that channel 1, 2, 3 letter E is wire-wrapped. The factory preset stop bit is one so channels 1, 2, 3, for letter S should have the left and right pins wrapped, bypassing the center 1 pin. To set channels 1, 2, 3 for, 7 data bits, remove the blue plastic clips or wire wrap from the D set of pins and wire wrap the left and right (X to 0) pins. To set J0 to even parity, wire wrap CH0 letter E center and right pins together (X to 1) and CH0 letter P left and right pins together (X to 0).

The factory has preset the CH0 to 1 stop but 8 data bits, so the S letter should have the left and right pins wrapped (X to 0) and the D letter should have the center and right pins wire wrapped.

Label the RJ11 outlets with the appropriate configuration.

A complete explanation can be found on pages 2-12 through 2-14 of Section III in the General Digital, GDC2100 Data Concentration Maintenance, and Operations Manual, November 30, 1984.

#### Other LSI Chip Information

Using Version 1 chips, you will notice many blank lines in the LA global. These lines usually are not blank, but have control characters which were not printable. With the advent of the Version 2 chips, all control characters have been made printable. This is done by taking each control character and generating a two character printable code, which makes it easy to see what has been received by the system. The printable code is in the following format:

~C

where ~ is a prefix notation telling you that the next character is a control character. The C is the printable form of the control character. This is generated by taking the ASCII value of the control character and adding 64 to it, giving a new value. This value is then used to get the printable character.

**Example:** ACK has an ASCII value of 66

add 64 to this 64

giving a value of 70

The ASCII value for the letter F is 70

Therefore an ACK would be represented as ~F

Some of the most common control codes you will see in the LA data stream are:

**Example:** STX(	start of text)						ASCII value 2	=	~B

ETX	(end of text)							ASCII value 3	=	~C

EDT	(end of transmission)				ASCII value 4	=	~D

ENQ	(enqueue request)					ASCII value 5	=	~E

ACK	(acknowledge)						ASCII value 6	=	~F

NAK	(negative acknowledgment)		ASCII value 21	=	~U

Whenever a control code is seen, the LSI changes the code into the above format and sends it with a carriage return, line feed after it. Therefore, a control code will always be either on a line by itself or the last character on the line.

The components of the LSI are well defined in the General Digital Maintenance and Operation manual that was supplied with each LSI. It would be very wise to locate one of these manuals at your Medical Center and keep it handy for reference. General Digital has gone out of business, so repair service for the LSI must be obtained by your site from a local vendor. If you can’t find a local vendor, we suggest calling your ISC for information on vendors who will repair the LSI. Except for the special EPROM chips provided by the Dallas ISC, all components of the LSI are standard equipment and may be purchased from vendors on the open market. Using the General Digital Maintenance and Operation manual as a guide, the Medical Center’s biomedical engineering shop could purchase all the LSI components and assemble another LSI. If this approach is taken, a Medical Center would be able to service their own LSIs and always have a spare. Any site wishing to take this route could request additional EPROMs from their ISC and buy the other components on the open market.

### 20 Wiring Diagrams and Pin Definitions for Automated Instruments

#### Automated Instrument Interface Specifications

**TYPE OF INTERFACE:** RS 232

**CABLES:** Two 2: twisted pairs

Pair 1: 1 transmit signal, 1 signal ground

Pair 2: (Optional) 1 receive signal, 1 signal ground

Shield: (Optional)

**CONNECTORS:**

A.	Connector for the instrument end of cable is instrument specific. Usually a DB 25P or DB 25S connector.

B.	The Interface end of cable needs a modular phone plug to connect to a modular phone jack located on the LSI.

**NOTE:** Use the fact that the ground wires on the LSI are shorted together to eliminate wiring problems when wiring up instruments.

If you plug into the LSI, then check the four wires at the other end to find out which two are shorted. These are ground wires and will be connected to pins 1 and 7 (it does not matter which) on the computer port or the instrument. Now there are only two wires to worry about and they will go on 2, and 3 so if one combination does not work, try the other.

If the instrument requires jumpers, start out by shorting pins 4 to 5, and pins 6, 8, and 20 together.

For runs of any distance, you should always use four wires, two twisted pairs, properly terminated on pins 2, 3, 7, and 1.

**NOTE:** On the instrument side of the LSI connect pin 1 only at one end.

#### Automated Instruments Interface

#### Interfacing Pin Definitions

The default configuration of the interface ports (i.e., the way they are shipped) is 1 stop bit, 8 data bits, no parity, and 1200 baud rate. The configuration of the interface and the instruments must match each other. Wire wrap connections must be changed to modify the configuration.

#### LSI Interface Testing

When the LSI is first turned on, the LED on the processor board will go on for 1/2 second, then off for 1 to 2 seconds, then on for 1/2 second, then off. In the time that the LED is off, the software is doing a memory test. At this time, the LED will flash at a 1 second rate, and the message STARTED V. 2.24 123456789: X is sent to the host from port 1 of the LSI. At this time a terminal can simulate the host for checking the LSI, as shown below.

**D ^LABTEST**

=&gt;T01L001 1 1 A

&lt;==T01L011M001       .M001,H0000

==&gt;T00L000 A

==&gt;T00L00  A

#### Checklist for Instrument Interface

1.	Instrument must be transmitting data.

2.	Correct baud Rate:

instrument baud rate = interface instrument port baud rate

host system baud rate = interface system port baud rate

3.	Echo device defined in the DEVICE file.

4.	LAB program routine must be running.

5.	The device baud rate is correct.

6.	ZTM program routine must be running (Task Manager).

7.	AUTO INSTRUMENT file (#62.4) is defined correctly.

8.	Input lines are wired correctly.

#### Instrument Interface Troubleshooting

**•	LSI management:** To shut down the LAB program set the STOP node by entering the following:

**S ^LA(“STOP”,N)=“ ”** **(WHERE N represents the AUTO INSTRUMENT file (#62.4) entry number for the LSI)**

The LAB job will continue starting processing routines until no more data remains in ^LA global. At this time, LAB will check the STOP node and if it exists, it will kill off ^LA and shut itself down. This is the proper way to bring down the LAB job and not have partial data left in ^LA.

**NOTE:** This will not work if the LAB job is not actually running as happens sometimes when it shows up on system status but no processing routines get started.

• **Multiple LSI:** The procedure is the same except the LSI need to be stopped and started in a certain order.

1.	Stopping LAB: shut down in reverse order LSI #3, then LSI #2, then LSI # 1.

2.	Starting LAB: start in numerical order...first LSI #1, then LSI #2, etc.

Crashes and just having IRM kill the LAB job can account for incomplete date streams in ^LA which in turn may cause the processing routine to error out when the LAB job is started again. If this happens, the best thing to do is  have IRM kill the ^LA(n) node and either retransmit your data or rerun it.

**•	Troubleshooting** (with and without programmer access) **:** Techs reports the Enter/verified data (auto instrument) option, EA indicated there is no data to verify. Use Lab interface [LA INTERFACE] menu and observe the system status display. Is there data in ^LA? ^LAH? If “YES” to both, use the Watch the data in ^LA global [LA WATCH] option to look at upload data. If ^LA(n, “I” ,0)= less than ^LA(n, “I”), this is the last line that was processed and you should look at ^LA(n, “I”, value of ^LA(n, “I”,0)) for any unusual characters. To view ^LAH global data you can do the following:

1. Version 5.2: Use the Watch the data in ^LA global [LA WATCH] option.

Check to see if the results reported missing are in fact in ^LAH.

**•	The normal identifier node in ^LAH looks like this:**

For the most part, the above data stream will be what you look for as a healthy identifier node. The most common problem  is a missing date entry. The probable cause of this is that the ID or Account number transmitted did not find a match in the accession file. If you were in "EA" and entered the tray and cup as 1 &amp; 2, the results would be displayed to you. There is an occasion where all you might see is this:

^LAH(n,1,1,0)=1^2^^^7^^STKS

This is a healthy identifier node for an instrument set to verify by tray/cup. This is not all that common since verify by accession is the most common choice.

Data in ^LA? YES, ^LAH? NO:

Again, check the “I”) and “I”,0) nodes in ^LA. If “I”) has value and “I”,0)=0 check the error log to find out what may have happened to the processing routine.(Lab Interface menu =&gt; Lab error trap listing option , or the ^LA(“ERR”) node). Verify that the routine entered in the AUTO INSTRUMENT file (#62.4) is correct and if there was an entry in the error log, make sure the variable LANM equals this entry. Check to see that other instruments on the same LSI are still running. If not, the Lab program has shut down. If they are, suspect a problem in the ^LA data stream causing the processing routine to quit or crash.

If the latter is the case, it is time to call in IRM. Have them clear the variables from the partition leaving only the basic system variables. If ^LA(“LOCK”,n) is set, kill it. Set ^LA(n, “I”,0)=0, zload the processing routine and start executing the code command by command writing variables as you go until you get to the point where the data stream fails the code and causes it to either ignore the data or quit.

Data in ^LA? NO, ^LAH? NO:

What you are seeing here could be one of two things: **1)** the instrument has stopped transmitting (suspect either a wiring problem or instrument parameter has been reset to a default of no transmission), or **2)** the processing routine completed it is task and killed off ^LA(n) and ^LA(“LOCK”,n). You can check number “1” by watching the ^LA global while a transmission is in progress. If you suspect number two, have IRM set ^LA(n, “I”)=0, and ^LA(n, “I”,0)=0. This will stop the processing routine from acting on the new data that you will now transmit and give IRM a chance to step through the code as in the procedure previously stated.

Illegal Number or Maximum Errors:

The most likely cause is having the letter E as part of the value of V when it is used for setting the value of a variable in the plus form.

**Example:** S ID=+V. Find out who or what is adding this E to the data. Accession numbers should not contain alpha characters although some instruments allow this type of entry.

Variables used in auto instrument interface routines:

**TSK,T =** both are used to represent the port or instrument number.

**LANM =** processing routine name.

**ID =** accession number.

**IDE =** instrument sequence number.

**TRAY and CUP** are self-explanatory.

**TC( ) =** the array built when ^LASET is run.

These variables contain the information from the AUTO INSTRUMENT file (#62.4) for test name, data name location, and params 1-3:

**Example:** TC(I,0)=1....................First test in AI chem test field.

TC(I,1)=TV (384,1)....Data name location (storage)

TC(I,2)=................... .Param 1 value

TC(I,3)=.....................Param 2 value

TC(I,4)=WBC............Param 3 value

TV( ) = the array built by indirection in the processing routine, used to set test values into ^LAH.

**Code example:** S @TEST(TEST)=+V will set the following:

where TEST = WBC and TEST(“WBC”)= TV(384,1)  TV(384,1)=5.7

where TEST = RBC and TEST(“RBC”) = TV(385,1) TV(385,1)=4.32 etc.

TEST( ) = array that holds test name identifiers built from param 3 or TC(I,4)

**Example:** TEST(“WBC”) = TV(384,1)

IN = the value of the data node being processed (^LA(n,“I”,X)

Y (1) = the value of IN. This may be a single entry or an array. It is used for parsing out data.

V = used for passing a value to the subroutine NUM and then setting a variable upon returning.

LAGEN =- contains the executable code determined by the ENTRY for LAGEN ROUTINE entry in the AUTO INSTRUMENT file (#62.4).

LWL = the internal entry number for the load/worklist used by this instrument. It is set by taking the 4th piece of the auto instruments zero node from AUTO INSTRUMENT file (#62.4).

**Example:** ^LAB(62.4,2,0)=Coulter STKS^^LACOLTSE^ **7** ^^LOG^ID^^^STKS without programmer access you can use FileMan Inquiry option and use number instead of standard output when inquiring on the load/worklist entry.

**• Local AUTO INSTRUMENT files:**

The most important trouble shooting tool you can have is to keep a file on each instrument interfaced. This file should contain the following information captured when the interface is up and working well:

1. samples of the LA and LAH data streams,

copy of the routine used,

captured print of the AUTO INSTRUMENT file (#62.4) and LOAD/WORKLIST file (#68.2) entries,

any pertinent data related to the wiring of the interface,

instrument parameter settings.

Direct connect instruments:

Direct connecting of instruments should be reserved for those instances where going through the LSI just will not work. This happens sometimes when two or more major instruments are on the same LSI. The traffic during transmission slows the verification process down to unacceptable levels. If the instrument in question does not have a direct connect routine as part of the released package there are three alternatives available to you:

1. Place one instrument on its own LSI,

Get a local programmer to modify a copy of the LAPORTXX routine to work with this instrument,

Submit an official request to the Auto Instrument ARG for approval of development. Some sites have expressed the desire to bypass the LSI completely and direct connect ALL instruments. This causes much overhead on the system because every instrument would have to have a background job associated with it which increases the chances for problem by how ever many background jobs you have running. The LSI is old, it is simple, but it works.

### 21 LAPORTX X Routine

The LAPORTXX routine is provided to be copied and modified when developing a new direct connect routine. It is meant to be a starting point only, and cannot be ran as is. Once modified, this routine will act like the LAB job in that it will watch a single port (not from the LSI) and store the data transmitted into a specified ^LA(XX port. The important criteria here is that you choose a port outside the range of existing LSI(s). Remember each LSI has a range of ten starting with 1-10, 11-20, 21-30, and so on. If you have two LSIs in use on your system select a direct port of 33 for example.

### 22 LAPX  Routine

The LAPX routine is provided to be copied and modified when developing a new unidirectional routine. Just like the LAPORTXX routine, this routine is meant to be a starting point only and cannot be used without modification.

### 23 Instrument Routines

The following is a list of instruments that have been written and tested. Most of these are unidirectional routines. Where there is a bidirectional routine for the instrument, this is so indicated.

**NOTE:** All the routines that began with a “LAI” have been renamed to prevent any accidental confusion with INIT routines.

**Status code**

5.1	Released with Version 5.1

#nn	Patch number (Version 5.1)

UD	Under active development - either at the Dallas ISC or in cooperation with a local site initiative at an official test site

I	Inactive (a site may have it interfaced but it is not officially supported)

5.2	To be released with Version 5.2

**Bi/Uni code**

B	Bidirectional

U	Unidirectional

Name                           Routine(s)       Bi/Un    Status

ABL3 RADIOMETER                 LAABL3          U          5.1

ABL4 RADIOMETER                 LAABL3          U          5.1

ABL300 RADIOMETER               LAABL3          U          5.1

ABL330 RADIOMETER                               U          I

ABL500 BLOODGAS                 LAABL500        U          #117

ACA3                            LAACA           B          5.1

ACA4                            LAACA4          B          5.1

ACA5                            LAACA4          B          5.1

ACCUDATA GTS                                    U          UD

ALTAIRE                         LAALTA          U          5.1

APPRAISE, BECKMAN                               U          I

ARRAY, BECKMAN                                  U          I

ASTRA (4,6,8/8E,IDEAL, LINKED)  LAASTRA         U          5.1

ATLAS                           LACLT20P        U          #113

AXSYM, ABBOTT                                   U/B        UD

AUTOSCAN 4                      LAMSA           U          5.1

BIOVATION KEYPAD (URINALYSIS)   LABIOU          U          5.1

BIOVATION KEYPAD (HEMATOLOGY)   LABIOH          U          5.1

BMD 8700 (printer port)         LABMD87P        U          5.1

CELLDYNE 1600                                   U          I

CELLDYNE 3000                                   U          I

CENTRIFICHEM 600                LACCHEM6        U          5.1

CHEM 1, TECHNICON               LACHEM1         U          5.1

CHEM 1, TECHNICON                               B          UD

CLINITEK 200                    LACLT200        U          5.1

CLINITEK 200 W/ DMS             LACTDMS         U          5.1

CLINITEK 200+                   LACLT20P        U          #113

CLINITEK 2000                   LACLNTEK        U          5.1

CLINITEK 5500                   LACL5500        U          5.1

CLINTEK FORM PRINTER            LACLNTE         U          5.1

COAGAMATE                                       U          I

COAGAMATE X2                    LACOAGX2        U          5.1

COAG XC+                                        U          I

COAG RA4                                        U          I

COBAS BIO                       LACBIO          U          5.1

COBAS FARA                      LACFARA         U          5.1

COBAS FARA BI                                   B          I

COBAS FARA II                   LAFARA2         U          5.2

COBAS MIRA                      LACMIRA         U          5.1

COBAS MIRA S                    LACMIRAS        U          5.1

COBRA/PACKARD                                   U          I

COMP-U-DIFF, MODULUS            LAMODH          U          5.1

CORNING ACS 180                                 U          I

CORNING 178                     LAC178          U          5.1

CORNING 178 THRU HP             LAC178H         U          5.1

CORNING 278 LS1                                 U          I

CORNING 278 LS2                                 U          I

CORNING 288                                     U          I

COULTER 770                     LAS550          U          5.1

COULTER JR+5                    LACOLT5         U          5.1

COULTER JT                      LACOLT5         U          5.1

COULTER JT3                     LACOLT5         U          5.1

COULTER JT3 (running EO#,BA#)   LACOLT6         U          5.1

COULTER MAXIM                   LACOLTES        U          #11

COULTER S EDMAC 2400 INTERFACE  LACOLT24        U          5.1

COULTER S PLUS                  LACOLT1         U          5.1

COULTER S PLUS 2                LACOLT2         U          5.1

COULTER S w/COURT II            LASCT           U          5.1

COULTER S SR                    LACOLT5         U          5.1

COULTER S+ JR                   LACOLT5         U          5.1

COULTER S+4                     LACOLT5         U          5.1

COULTER S+5                     LACOLT5         U          5.1

COULTER S+6                     LACOLT5         U          5.1

COULTER S+6, DT W/DH INT        LACOLT6         U          5.1

COULTER SR+2 W/QC MODULE        LACOLT3         U          5.1

COULTER STKR-S                  LACOLT5         U          5.1

COULTER STKS 1E                 LACOLTSE        U          #11

COULTER Sr.                     LACOLT          U          5.1

COULTER S550                    LAS550          U          5.1

COULTER S560                    LAS550          U          5.1

COULTER S770                    LAS550          U          5.1

COULTER S790                    LAS790          U          5.1

COULTER S880                    LAS790          U          5.1

COULTER T660                    LACOLT5         U          5.1

CX3, BECKMAN                    LASTRA          U          5.1

CX4, BECKMAN                    LABCX4B         U          5.1

CX4, BECKMAN                    LABCX4B         B          5.1

LABCX4D

LABCX4H

LABCX4XX

CX5, BECKMAN                    LABCX4B         U          5.1

CX5, BECKMAN                    LABCX4B         B          5.1

LABCX4D

LABCX4H

LABCX4XX

CX7, BECKMAN                                    U          UD

CX7, BECKMAN                                    B          I

DACOS, COULTER                  LADACOS         U          5.1

DEMAND                          LADMND          U          5.1

DIMENSION, DUPONT               LAACA4          U          5.1

DIMENSION DIRECT CON, DUPONT    LAAIMPXX        B          5.1

LADIMD

LADIMPI

DIMENSION H-6000, DUPONT        LAH6K           U          5.1

E4A, BECKMAN                    LAE4A           U          5.1

EDC, HELENA                     LAHEDC          B          I

LAHEDCD

EKTACHEM 400                    LAEKT4          U          5.1

EKTACHEM 700                    LAEKT7          U          5.1

EKTACHEM 700 (printer port)     LAEKT7P         U          5.1

EKTACHEM 700 BI                 LAEKT7B         B          5.1

LAEKT7B1

LAEKT7B2

LAEKT7B3

LAEKT7D

LAKERM2

LAKERM3

EKTACHEM 700 DIR.CON.                           B          I

EKTACHEM 700 (updated software)                 B          I

ELECTRA 900, MLA                LAMLA1KC        U          5.2

ELECTRA 1000, MLA               LAMLA1KC        U          5.2

ELT 1500                        LAELT8D         U          5.1

ELT8, DS                        LAELT           U          5.1

ELT8 with 3 cell diff           LAELT8D         U          5.1

EPX BI DIRECT CON           LAEPXD, LAEPXPX     B          5.2

ERA, PHOTON                     LAERA           U          5.1

EXECUTIVE, ABBOTT               LAEXEC          U          5.1

H1, TECHNICON                   LAH1            U          5.1

H3, TECHNICON                                   U          I

H6000, TECHNICON                LAH6K           U          5.1

HEMALOG D, TECHNICON            LAHLOG          U          5.1

HEMATRAK 360                    LAH480          U          5.1

HEMATRAK 480                    LAH480          U          5.1

HEMATRAK 590 GEOMETRIC          LAH480          U          5.1

HEMATRAK 590 W/ DIFFS           LAHTRK          U          5.1

HITACHI 704                     LAH705          U          5.1

HITACHI 705                     LAH705          U          5.1

HITACHI 717                     LAH717U         U          5.1

HITACHI 717 THRU CCA            LAHTCCA         U          5.1

HITACHI 717 BI                                  B          I

HITACHI 717 W/JT                                B          UD

HITACHI 736 W/ JT1000           LAHT1K          B/U        5.1

LAHT1KD

HITACHI 737                     LAH737          U          5.1

HITACHI 747                     LAH747          U          5.1

HITACHI 747                     LAH747          B          #99

HITACHI 911                                     B          UD

IL 1303                         LAL13           U          5.1

IL 1306                         LAL1306         U          5.1

IL 1312                         LAL1312         U          5.1

IL 508                          LAL508          U          5.1

IL 943                          LAL943          U          5.1

IL CELLECT 8E                   LACEL8E         U          5.1

IL BGE                                          U          I

IL BG3                          LALBG3          U          5.2

IMX, ABBOTT                     LAAIMX          U          #118

INTERLINK, BECKMAN              LABITKU         U          5.1

IRIS                            LAYRIS          U          5.1

KDA, AMERICAN MONITOR           LAKDA           U          5.1

KEYBOARD DIFF                   LAKDIFF         U          5.1

LAKDIFF1

LAKDIFF2

LAKDIFF3

KEYBOARD URINE                  LAKUR           U          5.1

LAKUR1

KOAGULAB 40-A                   LAKOAG40        U          5.1

MICROSCAN                       LAMSA           U          5.1

MICROSCAN                       LAMSA1          B          5.1

LAMILL

LAMSBLD

LAMSD

LAMSP

LAMSPAN

MLA 700                         LAMLA7          U          5.1

MLA 900                         LAMLA1K         U          #98

MLA 900C                        LAMLA1K         U          #98

MLA 1000C                       LAMLA1K         U          #98

MONARCH 2000, IL                LAMONARK        U          5.1

MULTISTAT 3                     LAMSTAT         U          5.1

NE 8000 (same as SYSMEX 8000)   LASYS8K         U          5.1

LASYSMEX

NOVA 4+4                        LANOVA          U          5.1

NOVA 11+11                      LANOVA          U          5.1

NOVA STAT PROFILE               LANOVST         U          5.1

PARALLEL, AMERICAN MONITOR      LAPARA          U          5.1

PARALLEL (printer port)         LAPARAP         U          5.1

PARAMAX, BAXTER                 LAPMAX          U          5.1

PARAMAX, BAXTER                 LAPMAX          B          5.1

LAPMAXD

PARAMAX 700ZX                                   B          I

PERSPECTIVE                     LAPER           U          5.1

PERSPECTIVE                     LAPER           B          5.1

LAPERD

RA4, ORGANON                    LACOARA4        U          5.2

RA-1000, TECHNICON              LARA1K          U          5.1

RA-2000, TECHNICON              LARA2K          U          5.1

RA2X, TECHNICON                 LARA2K          U          5.1

RA2XT, TECHNICON                LARA2K          U          5.1

RAPIMAT II, BEHRING             LARAPMT         U          5.1

RAPIMAT II BI,  BEHRING                         B          I

REP, HELENA                                     U          I

SMA II/C                        LASMA2C         U          5.1

SMA II/Gen 2                    LASMA2          U          5.1

SMA 60                          LASMA12         U          5.1

SMA 18/60-VICKERS SP120 INTERFACE  LASP120      U          5.1

SMAC I                          LASMACA         U          5.1

SMAC I                          LASMACA4        B          5.1

LASMACA

LATECH1

LATECHHS

LATECHD

SPECTRUM, ABBOTT                LASPEC          U          5.1

SPECTRUM                                        B          I

STRATUS, BAXTER                                 U          I

SYSMEX 8000                     LASYS8K         U          5.1

SYSMEX E-5000                   LASYSMEX        U          5.1

SYSMEX E2000                    LASYSMEX        U          5.1

SYSMEX K1000                    LASYSMEX        U          5.1

TDX, ABBOTT                     LATDX           U          5.1

TDX (with specimen ID) V10.1    LATDX1          U          5.1

TDX, PACKARD                    LATDX           U          5.1

TOA                             LATOA           U          5.1

UR-O-COMP, MODULUS              LAMODU          U          5.1

UR-O-COMP, MODULUS VERT FORM    LAMODUT         U          5.1

VITEK (Version 5.0 or less)     LAMIVTK         B          5.1

LAMIVTKC

LAMIVTKD

LAMIVTKU

LAMIV11

LAMIV12

LAMIV10

LAMIV00

LAMIVT5

LAMIVT6

LAMIVTE6

LAMIVTK6

LAMIAUT7

LAMIAUT8

LAMICRA

VITEK (Version 5.0 or more)     LAMIVTK         B          5.2

LAMIVTKC

LAMIVTKD

LAMIV11

LAMIV12

LAMIV10

LAMIV00

LAMIAUT7

LAMIAUT8

LAMICRA

LAMIVT5

LAMIVT6

LAMIVTE6

LAMIVTK6

### 24 ^LA &amp; ^LAH Global Descriptions

#### Justification and Descriptions of Non VA FileMan Compatible Globals

The ^LA and ^LAH globals are used by the automated instrument routines in the lab package to capture the raw data produced by lab instruments and then to process the data into a usable format.

The data in the ^LA and ^LAH globals is transient, but is different from ^TMP($J globals in that its existence transcends a single job and needs to be translated.

#### Description of ^LA Global

^la(0)=raw auto instrument datA		^62.45P

^LA(INSTRUMENT #, “I”)	=	Pointer to last data node added

^LA(INSTRUMENT #,“I”,0)	=	Pointer to last data node processed

^LA(INSTRUMENT #,“I”,IFN)	=	Raw data

^LA(INSTRUMENT #,“0”)	=	Count of nodes queued for sending

^LA(INSTRUMENT #,“0”,0)	=	Count of nodes sent

^LA(INSTRUMENT #,“O”,IFN)	=	Raw data

^LA(INSTRUMENT #,“Q”)	=	Count (used in queuing)

^LA(“LOCK”,IFN)	=	““ (Running flag to only allow one routine to run)

^LA(“STOP”,IFN)	=	““  (If set, tells routine to stop running)

^LA(“Q”)		=	Count (Used in queuing)

^LA(“Q”,IFN)		=(Tells LAB routine which instruments have data)

^LA(“TP”,0)		=	Pointer to last data node added (If set, the LAB routine stores a copy of all instrument data under this node; can be used in trouble-shooting an instrument)

^LA(“TP”,IFN)	=	Instrument #^Raw data...

#### Description of ^LAH Global

^LAH(0)		=	PROCESSED LOAD/WORK LIST DATA^68.3P^.

^LAH(LOADLIST #)	=	Count of entries

^LAH(LOADLIST #,1,IFN,0)	= Tray^Cup^Accession area #^Date^Accession #^^Method

^LAH(LOADLIST #,1,IFN,TEST FLD #)	=	Result^^Flags

^LAH(LOADLIST #,1,“B”,TRAY;CUP,IFN)	=	““ (Cross-reference for tray/cup

^LAH(LOADLIST #,1,“C”,ACCESSION #,IFN)	=	““ (Cross-reference for Accession #)

^LAH(LOADLIST #,1,“E”,IDE #,IFN)	=	““ (Cross-reference for IDE #)

The LAB DATA file (#63) is strictly a storage file for all the test results (data), comments, etc. The field names are descriptive of the contents in that they are the names of the tests, procedures, antibiotics, etc. The content of the field is the data value.

#### VAX Example of Device Setup for the Laboratory System Interface

(LSI) Excerpted from the VAX Cookbook - May 1989, pp 4-52-53

*** WIRING DIAGRAM:**

**LSI	DECSERVER**

2 ------------------------------	2

3 ------------------------------	3

7 ------------------------------	7

*** DECSERVER PORT SETUP:**

From the DECserver local&gt; prompt:

(where xx would be a DECserver port #, and DHCP is the name of the dedicated service.)

**Local&gt; set port xx access remote modem disabled name LSI speed 2400****

**Local&gt; save port xx**

Using Terminal Server Configurator (TSC) (see Chapter 5.E Terminal Server Software for more info on TSC)

TSC&gt; define port xx access remote modem disabled name LSI speed 2400**

If Port 8 on a DECserver were SET and DEFINED in this manner, the DECserver SHOW PORT command would result in the following:

**Local&gt; show port 8**

Port 8:

Character size :	8	Input Speed:		2400**

Flow Control:	xon	Output Speed:		2400**

Parity:	none	Modem Control:	disabled

Access:	Remote	Local Switch:		none

Backward Switch:	none	Name:				LSI

Break:	Disabled	Sessions Limit:	   4

Forward Switch:	none	Type:				ANSI

Preferred/Dedicated Service:	none

Authorized/Current Groups:	0

Enabled Characteristics:

Message Codes, Verification

**NOTE:** For Version 1 EPROM chips, the speed is 1200 baud. For Version 2 EPROM (bidirectional) chips, the speed is 2400 baud. Check with the Lab Application Coordinator to determine if the Version 2 chips  have been installed.

*** VMS SETUP :**

Under $MGR LATCP a port must CREATEd and SET. See example of LTLOAD.COM in Chapter 5.E Terminal Server Software. In the following example with LTAxxx, xxx would be replaced by the actual name assigned to the port at the site. DSVnn would be replaced by the actual DECserver name. ‘port\_name’ would be replaced by the physical name of the port (e.g. LC-1-6) or other site-specific format. It is IMPORTANT that ‘port\_name’ be the same as defined on the DECserver and as created by LATCP.

LTLOAD.COM

Ex. $	MCR LATCP

CREATE PORT LTAxxx: /NOLOG

SET PORT LTAxxx: /APPLICATION/NOLOG/NOQUEUE/NODE-DSVnn/NAME-port\_name

The system manager must run the following VMS command procedure to create the Automatic Log-in File database, SYSALF.DAT:

$ @SYS$MANAGER:ALFMAINT.COM

Once created, the DSM utility ^ALF is used to tie terminals to a VMS username.

* DSM SETUP:

The LSI port on the DECserver should be set up to bypass the VMS username prompt. A DSM utility ^ALF is used, as follows. In this example, DECserver DSV22, port LC-1-8 is the port the LSI is connected to that is tied to username DHCP:

&gt; **D ^ALF**

Edit or List the VMS Automatic Log-in file: SYS$SYSTEM:SYSALF.DAT

Do you want to add or modify (A),delete (D), or list (L) records? **A**

Add record, or modify an existing record.

Terminal (ddcu)? DSV22/LC-1-8

User Name? DHCP

Terminal DSV22/LC-1-8 user DHCP record added

SYS$SYSTEM:SYSALF.DAT has been updated.

###### Example of How to Define the Echo Device

###### for the “System” Auto Instrument

(The device entered is the IO port on the host CPU that will be connected to P1 of the LSI.)

Select Systems Manager Menu Option: **F** VA FileMan

VA FileMan Version 17.32

Select VA FileMan Option: **E** nter or Edit File Entries

INPUT TO WHAT FILE: **AUTO INSTRUMENT**

EDIT WHICH FIELD: ALL// **&lt;RET&gt;**

Select AUTO INSTRUMENT NAME: **SYSTEM**

NAME: SYSTEM// **&lt;RET&gt;**

ECHO DEVICE: 70// **&lt;RET&gt;**

PROGRAM: LAB// **&lt;RET&gt;**

LOAD/WORK LIST: **^**

Select AUTO INSTRUMENT NAME: **&lt;RET&gt;**

Select VA FileMan Option: **&lt;RET&gt;**

### 25 Bar Code Readers (Blood Bank Module)

The Blood Bank Module uses bar code technology for the input of data relating to the units of blood/blood components - i.e., the blood component (a five digit code), the donor unit ID number (an 8-11 characters number) and the donor ABO/Rh. While the data can be entered manually, it requires at least 50% more time and obviously introduces the possibility of clerical errors. In facilities where the number of units in inventory is relatively large, repetitive entry of groups of numbers or letters of 8-11 characters can result in a significant error rate. In facilities where donors are drawn, the savings in time are even more dramatic, in that labeling of the units after processing is decreased from two technologists to one technologist with a bar code reader.

There are two types of bar code readers available, the pen/wand type and the laser. The ONLY requirements for the bar code reader to be used in the Blood Bank Module are as follows:

1. ability to read Codabar, since this is used for all donor labels in accordance with the Uniform Blood Labeling Act.

ability to be connected in line between the CRT and the CPU via cables.

ability to set the unit to read stop codes.

To determine which type of reader is appropriate for your facility, and to evaluate the various readers on the market, you should consider the following:

Overall numbers of blood/blood components being handled in a given period of time, equating to the likelihood of typographical errors.

Number of rejections, i.e., the ease with which the reading is attempted before the data is accepted, since this will have a major effect on time savings.

The condition of the units being scanned; i.e., are most of the units red blood cells whose labels are in good shape, even though not a flat surface? OR are many of the units of Fresh Frozen Plasma and/or Cryoprecipitate, since this requires reading through cellophane covering on the box, around curves, through moisture, etc.?

The ease of handling the reader. Wand/pens are much easier to handle because you can still use your hands for something else, whereas with the laser gun model, you must keep setting the laser down to enter the expiration dates, etc. unless it is also bar coded.

Example of Bar Code Reader set up

Symbol Technologies Laser scan 7000II Hand Held Laser Scanner with the Symbol link LL340 Controller box. (REDACTED is using this technology)

All settings are set up by scanning the proper bar code in the instruction booklet.  Use the following settings:

CODABAR ONLY

NOTIS EDITING                   ENABLED

DECODE UPC/EAN SUPPLEMENTAL     ENABLED

UPC-E PREAMBLE                  NONE

UPC-A PREAMBLE                  NONE

BAUD                            9600

CHECK PARITY OF RECEIVED CHARACTERS      DISABLED

TRANSMISSION DIRECTION          TALK &amp; H'SHAKE SEC ONLY

STOP BIT SELECT                 1 STOP BIT

**NOTE:** This example is to show you what sort of setting you will see. The Laboratory package does not advocate using this particular brand.

### 26 Bar Code Labels (Accession Labels)

Version 5.2 includes the ability to print bar codes labels for specified accession areas. One bar code label, with the number part of the accession barcoded, along with the regular accession label can be printed. This ability is broken down by accession areas. It will allow a laboratory to turn on or off the printing of bar codes for a specific accession area.

At present, the routine is written only for the default label type which is a 15/16" x 3.5" label using the LRLABEL routine and the VAF 10-1392 label using the LRLABEL5 routine. Two printers have been defined to allow the printing of bar codes. They are the OTC 800 dot-matrix printer and the Intermec heat sensitive printer.

#### Implementation for the OTC 800 Printer

The following files must be edited for bar code printing:

##### 8 1. ACCESSION file (#68)

There is a new field (#5) called BAR CODE PRINT. For printing of bar codes for a specified area, this field needs to be set to “YES”. To turn off the bar codes for an area, delete the “YES”.

##### 9 2. TERMINAL TYPE file (#3.2)

A terminal type needs to be created for an OTC printer that has the Bar Code ON field (#60) and BAR CODE OFF field (#61) defined as follows:

BAR CODE ON:  *27,“[4;3;0;;;]”,*27,"[3t"

BAR CODE OFF:  *27,“[0t”

Within the BAR CODE ON, the numbers between the [ ] define the format of the bar code. In some circumstances these could to be changed, but realize the LRLABEL routine will need to be modified to accommodate the changes (i.e., changing the height of the bar code or printing the eye readable bar code).

The following format is used:

[Pl;P2;P3;P4;P5;P6;P7;P8]

Pl	specifies the type of bar code to print

O	Interleaved 2 of 5

4	Code 39 (default value)

5	EAN-8

6	EAN-13

9	Codabar a/a	start and stop character a

10	Codabar b/b	start and stop character b

11	Codabar c/c	start and stop character c

12	Codabar d/d	start and stop character d

13	UPC - A

14	UPC - E

P2 is the height adjustment. The height is adjustable from 1/12 inch to 10 inches in 1/12-inch increments. P2=n, where height = (n * 1/12"). The valid range of n is 1 to 120. P2=3 gives a barcode 1/4" high (equivalent to 2 lines). Any barcode larger than this will require a label greater than 15/16" or routine modification.

P3 specifies a readable line which is printed below the bar code.

O - Do not print human readable line

1 - Print human readable line

Parameters P4 through P8 should not be specified. These have to do with the width of the bars and spaces in the bar code symbol.

A suggested name for your newly created Terminal type is P-OTC (LAB BAR CODES).

##### 10 3. DEVICE file (#3.5)

In the field Subtype (#3), enter in the newly created OTC (bar code) terminal type for your OTC label printer.

##### 11 4. LABORATORY SITE file (#69.9)

In the field LABEL TYPE (#302), either leave it empty to use the default routine (LRLABEL) or if you had to modify LRLABEL enter in your modified routine LRLABEL4.

**Label Example:**

HE 0123 100

NAME,PATIENT	1234

||||||||||||||||

||||||||||||||||

||||||||||||||||

CBC,DIFF

#### Implementation for Intermec 8646 Printer;

##### 12 Printer setup

There are three banks of program (DIP) switches in the back panel of the Intermec 8646 printer. Check and set them up as follows:

Top DIP switch bank: 1 to 5 OFF

Middle DIP switch bank: 1 ON, 2 and 3 OFF, 4 and 5 ON, 6 and 7 OFF

Bottom DIP switch bank: 1 and 2 OFF, 3 and $ ON, 5 OFF, 6 ON, 7 and 8 OFF

The settings specify these parameters for the printer:

1. Character set = USA

Batch = disable

Self-trip mode = disable

Baud = 9600

Parity = space

Stop bit = one

Label stock = regular

Control mode = Computer

Protocol command = user designed/interfaced

Print direction/Format rotation = breach

Right margin override = disable

Bar width = 10 millimeter

Label size used: 1 by 3 inch (Intermec Part No. 049114)

##### 13 Files setup

The following files must be edited for bar code printing:

###### 1. ACCESSION file (#68)

Set field (#5) Bar Code Print to “YES” for printing bar codes for a specified area. To turn off the bar codes, delete the “YES”.

###### 2. TERMINAL TYPE file (#3.2)

P-Other

###### 3. DEVICE file (#3.5)

In the Subtype field (#3), enter the newly created Intermec (bar code) terminal type for your Intermec label printer.

**Example:**

NAME: BARCODE PRT                          $I: \_LTA 109:

VOLUME SET (CPU): DEV                      SIGN-ON: NO

KEY OPERATOR: FRANK &amp; TUAN                 NEAREST PHONE: 270

FORM FEED: #                               MARGIN WIDTH: 132

BACK SPACE: $C(8)                          PAGE LENGTH:

MNEMONIC: INTERMEC

SUBTYPE:P-OTHER                            TYPE: TERMINAL

# OF ATTEMPT: 5                            LOCK-OUT TIME:5

TIME READ (#OF SEC.): 300

###### 4.	LABORATORY SITE file (#69.9)

In the Label Type field (#302), either leave it empty to use the default routine LRLABEL6 or if you have to modify LRLABEL6, enter your modified routine LRLABEL4.

One of the functions of the LRLABEL6 routine is to specify and to down load the format of the bar codes. For more information on the setting of the format, consult the Intermec 8640 Series Thermal Transfer Printer Manual.

### 27 MicroScan Interface

#### Implementation

##### 14 c4.AutoSCAN 4 and AutoSCAN W/A;

Read volumes 1 and 2 of the MicroScan Mainframe Interface documentation thoroughly before proceeding.

1. System Wiring

The MicroScan AutoSCAN 4 and the AutoSCANW/A are wired identically to the LSI for either unidirectional or bidirectional  transmission. A 9-pin female connector links a communication port on the MicroScan to the LSI. Use comm port #2 for the AutoSCAN 4 and comm port #3 for the W/A.

MicroScan          RJ11 Block         LSI

3 -----------------------------2-------------------------2

2 -----------------------------3-------------------------3

5 -----------------------------7-------------------------7

4 -----------------------------20------------------------1

a. The MicroScan is wired to an RJ11 block.

b. A straight thru telephone wire connects the RJ11 block to the LSI.

**NOTE:** No jumping is necessary.

2. Software Requirements

a. MicroScan: Two Way DMS Interface Version 18.0 or higher

b. Host: DHCP Laboratory Version 5.0 or higher

3. Interface Setup

The Interface customization files are found by selecting option #8, optional programs, from the MicroScan DMS main menu. You must select the appropriate interface program from the optional program menu to have the interface main menu displayed.

INTERFACE MAIN MENU

1. Interface Customization

2. Request Specimens from the Mainframe (Two-Way)

3. Select/Transmit Specimens to Mainframe

4. Log on New Dataset

5. Transmit/Request DMS Customizable information

6. Interface log file and Maintenance

7. Backup/Restore Interface Customization &amp; Log File

8. Process WalkAway Specimens (V. 19.02)

#### MicroScan Mainframe Interface Version 19.02 Software

The Interface Customization Menu option will display the  communication parameters and formats menu. The DMS computer is configured and the date format established through this menu.

**NOTE:** All references to DMS files refers to the MicroScan computer files not DHCP files.

INTERFACE CUSTOMIZATION MENU

1.	Communication Parameters

2.	Custom Data Fields Formats

3.	Suppress/Customize Data Field Transmission

4.	Cross-Reference Table

5.	Protocol Character Definitions

6.	Device Maintenance

7.	Print Interface Customization (not discussed)

8.	Customize WalkAway Specimen Processing

#1 COMMUNICATION PARAMETERS MENU

Device Name/Type: **LABSYSTEM** - VA SYSTEM

1.	Baud Rate: **1200** (bps)

2.	Word Length: **8** (bits)

3.	# Of Stop Bits: 1

4.	Parity: **None**

5.	Protocol: **XON**

6.	Serial Port #: **Comm-#**

7.	Timeout Delay: **20** (secs)

8.	Checksum Type: SUM-ASCII

9.	Null Field OK: **Yes**

10.	Field Delimiter: **124 ACSII (|)**

11.	String Delimiter: **0 ASCII (^ @)**

12.	Delimit Character Fields: **No**

13.	Hospital/Lab ID: **None**

14.	Use Modem Commands: **No**

15.	Phone Number: **&lt;RET&gt;**

16.	Modify Modem Commands

#2 CUSTOM DATA FIELD FORMATS MENU

Device Name: **LABSYSTEM**

1.	Specimen Number Type: **Normal**

2.	Date/Time Format: **YYMMDD|HHMMSS**

3.	Organism Name Format: **Abbreviated**

4.	Single Therapy Reporting: **NO**

5.	Sort Transmission Selections: **Specimen Number**

6.	Combine Panel Transmit Method: **1**

7.	Suppress MICs for Breakpoint Panels: **No**

8.	Transmit Data In Long Patient Report Format: **Yes**

9.	Transmit QC Data: **No**

Remember field #5 always sort by Specimen Number, not by Patient ID.

#3 SUPPRESS/CUSTOMIZE DATA FIELDS TRANSMISSION

1.	Patient Name						13.	Comment Records

2.	Physician Name						14.	Panel Names

3.	Ward Names							15.	Organism Names

4.	Source Names						16.	Long Drug Names

5.	Comment Text						17.	Patient Records

6.	Service Names						18.	Specimen Records

7.	Institution Name					19.	Isolate Records

8.	Free Text Records					20.	End Records

9.	Additional Drugs					21.	Biotype Number

10.	MicroScan Interpretation		22.	Header Records

11.	MicroScan Dosages					23.	Drug/Therapy Records

12.	NCCLS Interpretation				24.	Technician Names

Select those options (1-24) that you wish to change. Options that are highlighted will be suppressed from transmission.

**NOTE:** Do not suppress #17, Patient Records.

#4 CROSS-REFERENCE TABLES MENU

**NOTE:** It is the site decision to set up cross-reference tables. You can set up a cross-reference tables for (a) ward mnemonics and (b) source mnemonics. The ward mnemonics associates every hospital location abbreviation in the DHCP HOSPITAL LOCATION file (#44) with the DMS CUSTOMIZATION file for ward locations. This is only needed if the site wants data stored differently from the downloaded ward abbreviation or site/specimens.

1. Cross-reference Status: Enable, Key length = 5

2. Select/Suppress Data Fields

3. Edit Tables

4. Print Tables

5. Rebuild Tables

6. Set Maximum Field Length

**NOTE:** EXCEPTION, if a site/specimen has an alternate screen define in the ANTIMICROBIAL SUSCEPTIBILITY file (#62.06), the cross-reference table for SOURCE mnemonics must be defined to upload the internal entry number for that source:

MicroScan Code	Mainframe Equivalent Code

1. Enter MicroScan code for	Enter the internal entry number

specified site/specimen	from the topography file for that

(example: URI)	site/specimen (ex. 71 for urine)

#5 PROTOCOL CHARACTER DEFINITONS MENU

1.	&lt;STX&gt;			- -		2

2.	&lt;EXT&gt;			- -		3

3.	&lt;EOT&gt;			- -		4

4.	&lt;CR&gt;			- -		13

5.	&lt;LF&gt;			- -		13

6.	&lt;XON&gt;			- -		17

7.	&lt;XOFF&gt;		- -		19

8.	&lt;ACK&gt;			- -		6

9.	&lt;NAK&gt;			- -		21

10.	&lt;ENQ&gt;			- -		5

11.	&lt;Prefix		- -		0

12.	&lt;Suffix&gt; 1	- -		0

13.	&lt;Suffix&gt; 2	- -		0

14.	&lt;Suffix&gt; 3	- -		0

#6	DEVICE MAINTENANCE MENU

1.	Create a New Device

2.	Log on to New Device

3.	Edit Current Device Attributes

4.	Delete a Device

Option 3 DEVICE ATTRIBUTES MENU

1.	Device Name: **LABSYSTEM** (free text entry)

2.	Device Type: **VA System**

3.	Auto-Monitor: **No**

4.	Auto-Transmit Time: **Disabled**

5.	Auto-Transmit Format: **Test Date**

**All Results**

6.	Auto-Request Time: **Disabled**

7.	Auto-Request Format: **Test Date**

**All Results**

8.	Number of search Days for Auto-select Data: **1**

(Types for #2: 1=LIS, 2=MicroScan system, 3=PharmLink and 4=VA/SAIC)

#8 CUSTOMIZE WALKAWAY SPECIMEN PROCESSING MENU

WALKAWAY SPECIMEN PROCESS LIST OPTIONS SUB-MENU

1. WalkAway Selection Enabled for: **All Isolates**

2. Sort Process List by: **Transmission order**

3. Suppress Oxidase Prompting: **Yes**

4. Suppress Indole Prompting: **No**

5. Default to Non-Hemolytic Reaction: **No**

6. Auto-Process Complete Isolates: **No**

**NOTE:** Above is site/configurable.

4. MicroScan File Setup

a. The DMS ward table listing file includes the most common ward/clinic locations used by the microbiology department of the VAMC.

**Example:**

1. 1  AG

2. 2  A1

3. 3  A2

34 B1  MEDICAL CLINICS

35 B2  ALCOHOLIC CLINIC

etc

**NOTE:** A cross-reference table can be set up under the interface customization menu to correlate the MicroScan DMS file with the DHCP HOSPITAL LOCATION file (#44).

b. The  source table listing file includes the names of all site/specimens or sources encountered by the microbiology dept.

**NOTE:** The source called URINE must be DESIGNATED as urine to DMS.

**Example:**

1.  1  NOSE/SINUS

2.  2  THROAT/MOUTH

3.  3  SPUTUM

34  99  NOT SPECIFIED

Press RETURN to continue or ‘^’ to exit:

**NOTE:** A cross-reference table can be set up under the interface customization menu to correlate this DMS file with the DHCP topography field file (#61).

c. The organism file on the MicroScan contains all the organisms identified by the MicroScan.

**NOTE:** All these organisms must be accounted for by DHCP in the ETIOLOGY file (#61.2) and AUTO INSTRUMENT file (#62.4).

d. The selected panel list displays those MIC panels selected by the microbiology department to be analyzed by either the autoSCAN 4 or the autoSCANW/A.

5. DHCP Laboratory Files

a. ANTIMICROBIAL SUSCEPTIBILITY file (#62.06)

1) Use the autoSCAN 4 and autoSCANW/A documentation to get a list of all drugs reported by MicroScan.

2) Refer to the Microbiology Implementation section for the procedure of adding new drugs to the DHCP and add any drug not already in File #62.06.

3) Reindex the following indices in File #62.06 AD,AJ,AO,AI, and AS.

4) D ^LAMSBLD to build the MicroScan mic x-reference in File #62.06

5) Manually enter the MIC values (dilution ratios) for trimeth/sulfa, amox/k clavulanate, and ticar/k clavulanate in File #62.06.

b. LABORATORY DATA file (#63)

1) New drug entries must be added to the LABORATORY DATA file (#63).

2) Follow the procedure in the Laboratory Technical Manual for adding these new drugs to File #63.

c. ETIOLOGY FIELD file (#61.2)

1) Get a list of all organisms which the AutoSCAN 4 and the W/A will report.

2) Follow the procedure described in the Lab Implementation Guide for adding these organisms.

d. LABORATORY SITE file (#69.9)

1) A new field called Download Full Data must be filled in. Answer “NO” to this field.

2) The Micro report format is site-specific. The choices are:

I INTERPRETATION ONLY

R RESULTS ONLY

B BOTH INTERPRETATION AND RESULT

No entry defaults to interpretation only.

e. LOAD/WORK LIST file (#68.2)

1) Create separate load/worklists for the AutoSCAN 4 and/or the W/A. Tests listed on the worklist are site-specific.

2) AutoSCAN 4 worklist:

Name: BR-MICROSCAN(AUTOSCAN 4)  Type: **SEQUENCE/BATCH**

CUPS PER TRAY: 0        FULL TRAY ONLY: **NO**

EXPAND PANELS ON PRINT:NO    VERIFY BY: **ACCESSION**

SUPPRESS SEQUENCE #: NO     INCLUDE UNCOLLECTED ACCESS.: **NO**

RUN OR TRAY NUMBER: 1       DATE: **DATE**

TECH: NAME           ACCESSION AREA: **BMICROBIOLOGY**

LAST TRAY: 1          LAST CUP: **0**

BUILDING IN PROGRESS: **NO**

PROFILE: AUTOSCAN 4        ACCESSION AREA: B **MICROBIOLOGY**

TEST: CULTURE &amp; SENSITIVITY    BUILD NAME ONLY: **NO**

TEST: BLOOD CULTURE        BUILD NAME ONLY: **NO**

TEST: FUNGUS CULTURE       BUILD NAME ONLY: **NO**

TEST: RO/MRSA           BUILD NAME ONLY: **NO**

TEST: LEGIONELLA CULTURE     BUILD NAME ONLY: **NO**

TRAY #: 1

3) Walk/Away worklist: (Same as autoSCAN 4 worklist)

f. AUTO INSTRUMENT file (#62.4)

1) Certain fields are site specific, such as Name, Loadlist, and Micro Auto Approval.

2) Be sure only one entry exists for each instrument in the AUTO INSTRUMENT file (#62.4).

3) The entry name, load/work list, accession area and program parameters will be instrument specific. The routine, LAMSA, was ZSAVED as ZLAMSA to be used as the program for one of the autoSCAN.

4) A representation of the AutoSCAN 4 entry in the AUTO INSTRUMENT file (#62.4) follows: (Same for MicroScan)

NUMBER: **16** NAME:BR-3-AUTOSCAN

PROGRAM: **LAMSA**

LOAD/WORK LIST: **BR-MICROSCAN**

ENTRY FOR LAGEN ROUTINE: **Acce** ssion cross-reference

CROSS LNKED BY: +IDE METHOD: **AUTOSCAN 4**

DEFAULT ACCESSION AREA: **BMIC** ROBIOLOGY

OVERLAY DATA: **YES**

HANDSHAKE RESPONSE: **D ^LAMSP**

NEW DATA: **D NEW^LASET**

RESTART: **D RESTART^LASET**

**NOTES:**

1.	There is only (1) micro card type and card name for the AutoSCAN.

2.	Each organism in the ETIOLOGY file (#61.2), which is identified by the DMS AutoSCAN, must be correlated to the DMS internal number for that organism (card code).

MICRO CARD TYPE: GEN         CARD NAME: GENERAL CARD

ORGANISM:ESCHERICHIA COLI CARD CODE FOR ORGANISM: 1

ORGANISM:ESCHERICHIA COLI LYS- ORN-   CARD CODE FOR ORGANISM: 51

ORGANISM:ESCHERICHIA COLI  CARD CODE FOR ORGANISM: 851

ORGANISM:ESCHERICHIA FERGUSONII     CARD CODE FOR ORGANISM: 803

...                      ...

...                      ...

ORGANISM:SPOROBOLMYCES SALMONICOLOR   CARD CODE FOR ORGANISM: 512

Each antibiotic in File #62.06 must be correlated with the autoSCAN abbreviation for that antibiotic (card code).

**Example:**

NUMBER: 1                DRUG: AMIKACIN

DRUG NODE: 2.0016           CARD CODE:Ak

NUMBER: 2                DRUG: AMOX/K CLAV’ATE

DRUG NODE: 2.00525021         CARD CODE:Aug

NUMBER: 3                DRUG: AMPICILLIN

DRUG NODE: 2.0012           CARD CODE:Am

NUMBER: 62               DRUG: VANCOMYCIN

DRUG NODE: 2.0006           CARD CODE: Va

FILE BUILD ROUTINE: LAMSD
MICRO INTERPRETATION STYLE: INSTRUMENT INTERPRETATION ONLY

(Choices are:)

F CHECK ANTIMICROBIAL FILE INTERPRETATION ONLY

I CHECK INSTRUMENT INTERPRETATION ONLY

B CHECK BOTH FILE AND INSTRUMENT INTERPRETATION OVERWRITE WITH FILE

g. TOPOGRAPHY FIELD file (#61)

1) The topography abbreviation is downloaded to DMS and null entries  should be no problem.

2) Using DMS mnemonics as abbreviations for the TOPOGRAPHY FIELD file (#61) is site specific.

3) Get a listing from the microbiology department of the most commonly seen site/specimens.

h. COLLECTION SAMPLE file (#62)

1) Using DMS mnemonics as synonyms for COLLECTION SAMPLE file (#62) entries is site-specific.

2) Compare the DMS SOURCE file printout with a printout from the COLLECTION SAMPLE file (#62).

3) Ensure that there are equivalent entries in both files.

#### The Upload

1. The AutoSCAN 4 and the AutoSCAN W/A are not set to automatically upload their data to the mainframe.

2. Enter the Interface Main Menu and choose option #3, Select/Transmit specimens to mainframe.

INTERFACE MAIN MENU

1. Interface Customization

2. Request Specimens form the Mainframe (Two-Way)

3. Select/Transmit Specimens to Mainframe

4. Log on New Dataset

5. Transmit/Request DMS Customizable Information

6. Interface log file and Maintenance

7. Backup/Restore Interface Customization &amp; Log File

8.	Process Walk Away Specimens

3. The interface range of data selection menu is displayed:

1. Select specimens by range

2. Select by range of dates collected

3. Select by range of dates tested

4. Select by range of patient ID numbers

5. Select all information in dataset

6. Quick-Select for today’s tests

7. Retransmit Quick-Select

8. Select individual specimen numbers

Enter Selection or ESCape to exit: **&lt;RET&gt;**

Press RETURN to continue or ‘^’ to exit:

4. Choose option #8, Select individual specimen numbers. The microbiology department uses this option because they can retransmit the data and also select individual isolate data for a given specimen number to be uploaded to DHCP. Refer to the MicroScan mainframe interface operation manual for specific instructions. The following is an example of possible selections:

Select Individual Specimen/Isolate Combinations:

Enter specimen number, ESCape to continue: &lt;specimen number&gt;

Enter isolate number, return for ALL, ESCape to continue: &lt;isolate #&gt;

Enter isolate number, return for ALL, ESCape to continue: &lt;enter the next isolate number or ESCape&gt;

Enter the specimen number, ESCape to continue: &lt;enter next specimen number or ESCape&gt;

5. The Interface Data Option Menu is now displayed:

INTERFACE DATA OPTION MENU

1. Review Selected Data

2. Send data currently selected to mainframe

3. Suppress individual specimen/isolates

4. Print Selected Data

Enter number or ESCape to exit: **&lt;RET&gt;**

6. First review the selected data (option #1) and then send the selected data to the mainframe (option #2).

7. You will be prompted to press return when ready to transmit or ESCape to exit.

SENDING DATA TO MAINFRAME

Patient ID #:

Specimen #:

Isolate #:

Records left to transmit:

Press RETURN to continue or ‘^’ to exit: **&lt;RET&gt;**

Press ESCape to Abort transmission

**NOTE:** Once the RETURN key is pressed, transmission begins. As the warning shows, you stop the transmission by pressing the ESCAPE key.

8. Any error encountered during upload will be recorded in the MicroScan transmission log.

9. The upload data is initially stored in ^LA(AI#,”I”,#). The data is processed from ^LA to ^LAH. Once the data is in ^LAH it is available to be verified.

10. You can verify the MicroScan data using the Verify micro auto data option.

#### The Download

Downloading is moving data from DHCP to the automated instrument. This includes accession number, patient name, ID, ward location, provider, site /specimen, panel number, and isolate number.

The download can be subdivided into four activities:

1. Unloading the existing load/worklist

2. Clearing the instrument/worklist data

3. Building the MicroScan worklist

4. Downloading the MicroScan worklist to the instrument

1.	Unload the existing load/worklist is done with the Unload Load/worklist option. This takes ALL accessions off the list, leaving it blank.

2.	Clearing the load/worklist is done using the Clear Instrument/worklist data option. This option removes ALL data (verified and unverified) from the ^LAH global. Make sure all data has been unloaded and verified before using this option.

3.	The MicroScanworklist is built using the MicroScan Load Worklist (Build) option. The Microbiology department personnel must correlate the microbiology accession number with the DMS panel number for all accessions to be properly downloaded. The following tray/panel names are examples:

Panel number			Panel name

11							HNID

17							Neg Combo 7

32							Rapid Anaerobe ID

33							Rapid Yeast ID

Example of building a load/worklist for downloading:

Select Automated Microbiology Menu Option: **MicroScan Load Worklist build**

Select LOAD/WORK LIST NAME: **MICROSCAN** (name of worklist)

Select only from the MICROBIOLOGY accession area

Select Accession: **MI**

Accession Date: TODAY// **94**

Number part of Accession: **3000**

LAST,FIRST  ###-##-####

What test(s) to add?

1 CULTURE &amp; SENSITIVITY

Enter Choice(s): **1**

Enter Choice(s): **&lt;RET&gt;**

Select TEST or PANEL NUMBER: 1// **17**

ISOLATE: 1// **&lt;RET&gt;**

Select TEST or PANEL NUMBER: **“17”** ;  (if same panel, put in **“ ”** )

ISOLATE: 1// **2**

Select TEST or PANEL NUMBER: **32**

ISOLATE: 1// **3**

4. The Download Procedure

a. The MicroScan interface files must be open to receive the download from DHCP. Ensure that the interface main menu is displayed on the MicroScan CRT screen before initiating the download.

b. The download is accomplished using the Download Auto Micro Worklist option.

Select Automated Microbiology Menu Option: **Download Auto Micro Worklist**

Select AUTO INSTRUMENT NAME: **MICROSCAN** (or AI number) Working on the download file for instrument MICROSCAN from the LOAD list MICROSCAN from the LOAD list BR-MICROSCAN(AUTOSCAN4) or (WR-MICROSCAN(W/A))

Starting Tray number: 1// **&lt;RET&gt;**

Starting SEQUENCE number: **&lt;RET&gt;**

Send TRAY/CUP locations? NO// **&lt;RET&gt;** (this default is controlled by Field #95 in the AUTO INSTRUMENT file (#62.4))

QUEUE WORK? NO// **&lt;RET&gt;** (this default is controlled by Field #96 in the AUTO INSTRUMENT file (#62.4))

DONE.    Data should start moving now

You can monitor the transfer of information from DHCP to the MicroScan via the LSI by using the LA WATCH option. The download data is stored in ^LA(AI#,”0”,#). The LA WATCH option indicates the total number of records to be processed and the rate at which the records are being processed.

c. The MicroScan indicates when it is receiving data from the mainframe. The patient’s ID number, the specimen number and the isolate number will be displayed on the CRT as the data is being received.

Receiving data from mainframe. Please Wait.

Processing:	PAT ID#:

SPECIMEN #:

ISOLATE #:

After all the data has been transmitted from DHCP to MicroScan, the MicroScaninterface screen will return to the main menu.

d. An error message will be displayed on the MicroScan side if there were any download transmission error(s). Review the transmission log. You will get error messages if the mnemonics for Wards, Physicians, or Services are missing from the DMS customized files. These errors do not seem to cause any problems.

e. The MicroScan will automatically tag the downloaded isolates and will assign MicroScan panel ID numbers to all downloaded isolates. You will observe a warning message on the MicroScan CRT reporting the isolates  were downloaded. You cannot proceed until you have entered in asked for information about the isolate. Once the information has been entered, bar code labels and worksheets can be generated.

### 28 VITEK Interface

Auto Instruments are an integral part of the Laboratory package. The VITEK is an automated instrument used in microbiology for microorganism identification and antibiotic measurements. This guide provides all of the instructions for setting up and using this instrument within the microbiology module of the Laboratory package. Step by step installation instructions, diagrams, option descriptions, troubleshooting suggestions, file setup, lists of card types, and examples of VITEK printouts are shown.

Each element of how to set up and use the interface with the VITEK is described in this manual in step-by-step procedures. On-line displays are shown. Examples of possible user responses are listed, following the on-line displays.

#### VITEK Interface Instructions

**I. System wiring**

A. VITEK system.

The VITEK system wiring is the same for both unidirectional and bidirectional. The following is a cable diagram for connecting the VITEK to an LSI.

VITEK	LSI

2 -----------------\/------------- 2

3 ----------------- /\------------ 3

4--

5--

6--

8--|------------------------------20|

20--

7----------------------------------- 7

B. LSI

The VITEK will run unidirectional with the old Version 1 EPROMS in the LSI.

If you are going to run the VITEK in a bidirectional mode, you will have to install the Version 2 EPROMS before bidirectional capabilities will work. Refer to the section in this chapter about bidirectional interfacing and Version 2 EPROMS.

**II. Software Requirements**

A. VITEK Unidirectional:	AMS R06.1 or later bidirectional:
BCI Version 02.3 or later.

B. Host:	DHCP Laboratory Version 5.0 or later.

**III. Interface Setup**

A. Unidirectional: At the VITEK system prompt run the program cisend and set the parameters as follows:

**&gt;cisend**

The following menu will display:

REQUEST COMPUTER INTERFACE

TRANSMISSION

l) TRANSMIT BY SLOT OR TRAY

2) TRANSMIT BY AMS ID

5) RETRANSMIT ALL NAKS

6) TRANSMIT TEST PATTERN

7) UTILITIES

Q) QUIT

Choose option 7) UTILITIES

Select each of these options and respond to the prompts as shown in the example:

COMPUTER INTERFACE UTILITIES

1) Turn Computer Interface ON/OFF:

2) Set retry wait

3) Set number of seconds for ACK wait

4) Set number of NACKS before auto disable

5) Set STX/ETX protocol

6) Set Serial port characteristics

7) Set Display data option

8) Enable/Disable AMS Computer Interface

Q) Quit

Responses will be:

COMPUTER INTERFACE UTILITIES

1. Turn Computer Interface ON/OFF: **ON**

2. SET RETRY WAIT: **10**

3. Set number of seconds for ACK wait: **10**

4. NACKS BEFORE AUTO DISABLE: **O** (defeated)

5. STX/ETX PROTOCOL: **“SSS”/**

6. HOST PROTOCOL CHARACTERISTICS: **?**

1200 BAUD

NO PARITY

8 BIT/CHAR

2 STOP BITS

XON wait 10

CHAR DELAY 0

7. DISPLAY DATA OPTIONS: **ON**

8. AMS COMPUTER INTERFACE: **ENABLE**

B. Bidirectional: At the VITEK system prompt run the program bciutil and set the parameters as follows:

**&gt;bciutil**

The following menu is displayed:

BIDIRECTIONAL COMPUTER INTERFACE

RESULTS TRANSMISSION

1) Transmit Results by Slot or Tray

2) Transmit Results by AMS ID

3) Retransmit all NAKs

4) Utilities

q) Quit

**NOTE:** The following menu displays are before Pre 3.1 BCI Software installation.

Select option 4) Utilities

The following menu will appear:

BIDIRECTIONAL COMPUTER INTERFACE

UTILITIES (VERSION XX.X)

1) Delete Negative Exams

2) Status and Exception Logs Menu

3) Transmit Test Pattern

4) Set Serial Port Characteristics

5) Set interface Characteristics

6) Display data on screen

7) Set Field Characteristics

8) Transmit Back in Service

9) Results (Upload) Options

*) Special options

q) Quit

Select option 4) Set Serial Port Characteristics

This menu will appear with defaults. Following the directions displayed on the screen, make changes where necessary to match values shown here:

SERIAL PORT CHARACTERISTICS

Number of Ports: 1

Baud Rate: 1200

Parity: None

Character Size: 8

Stop Bits: 2

Startup Message: Disable

Once you have finished here, return to the previous menu.

Select option 5) Set interface Characteristics

The following menu will appear with defaults. Following the directions displayed on the screen, make changes where necessary to match the values shown here. This menu is used to set up the interface.

BI-DIRECTIONAL COMPUTER INTERFACE CHARACTERISTICS

1.	BI-DIRECTIONAL INTERFACE (UPLOAD) IS: **ENABLED**

2.	BI-DIRECTIONAL INTERFACE (DOWNLOAD) IS: **ENABLED**

3.	DOWNLOAD PORT: **/dev/tty1**

4.	UPLOAD PORT: **/dev/tty1**

5.	TIMEOUTS (seconds):

CHECKSUM &lt;ACK&gt;: **60** HOST RESPONSE: **60**

XON/XOff: **10**

6.	RETRY LIMITS: 
	CHECKSUM ERROR: **3** &lt;ENQ&gt; **: 3**

7.	RETRY INTERVALS (seconds):

CHECKSUM ERROR: **10** &lt;ENQ&gt; **: 10**

8.	DELAYS (Seconds):

LAST MASTER: **10** INTERRECORD: **2** INTERMESSAGE: **10**

9.	END OF RECORD FORMATS:

STX: **DISABLED** ETX: **DISABLED** ENQ: **DISABLED**

RS: **ENABLED** GS: **ENABLED** EOT: **DISABLED**

10.TOTAL NUMBER OF FAILED MESSAGES ALLOWED: **3**

11.FIELD TERMINATION CHARACTER(S): **:**

12. SEPARATOR CHARACTERS: DATE: TIME: **&lt;RET&gt;**

13.DUPLICATE DEMOGRAPHICS UPDATE: **ENABLED**

STARTUP MESSAGE: DISABLED  DUPLICATE UPDATE: **ENABLED**

Use the following VITEK command to make a printout of the configuration:

imp&gt;p bciep

It is also recommended that each site perform a backup of the new BCI configuration to a floppy/tape.

C. **Cautions**

1.	If, during an upload session, the VITEK does not receive an acknowledgment from DHCP within the 10 second time wait limit, the VITEK will retransmit the record. This will be evident by looking at the LA global and observing that the record is in duplicate. If this occurs, go to the VITEK system console and type the command:

&gt;/etc/hostcts off

This should eliminate the duplicate sending of records.

2.	If, during transmission, the VITEK does not receive acknowledgment from DHCP that the records had been received within 3 tries, the VITEK turns its interface off. When this occurs several things must be remembered:

a. The VITEK will not transmit data again until the operator turns the interface back on.

b. Once the interface has been turned back on the operator can retransmit records ONLY if the cards have NOT been removed from the VITEK. If the cards have been removed, the entire test must be rerun or the result must be entered manually into DHCP.

3.	This system was written to support revision AI or later of the VITEK software. Sometime around Revision L, there was a change in the reporting of values out of the VITEK. Then with Revision W to Revision AI, values were periodically changed along with a change in NCCLS interpretations. Therefore, we will ONLY support Revision AI or later.

4.	With the release of VITEK AMS software version DSAMS-R06.1, there was a change in the byte positions used for transmitting the drug code for each antimicrobial on both the Gram positive and Gram negative susceptibility cards. This change in the VITEK data stream required an accompanying change in the DHCP program. The program used for the encoded upload on a bidirectional interface is LAMIVTE6. The program used for a unidirectional interface is LAMIVT6

**IV. VITEK File Setup**

A. Unidirectional

The VITEK does not require any special file setup to run in the uni-directional mode. If you are going to run the VITEK unidirectional, proceed to section V.

B. Bidirectional

The VITEK requires several tables to be defined by the operator before the instrument can be run in the bidirectional mode. These tables use abbreviations that are normally limited to a maximum of 6 characters and must be set up to match the corresponding DHCP files to accommodate downloaded information.

You will need access to information in the following DHCP files:

HOSPITAL LOCATION file (#44)

TREATING SPECIALTY file (#45.7)

COLLECTION SAMPLE file (#62)

TOPOGRAPHY FIELD file (#61)

LABORATORY TEST file (#60)

Updating the first four VITEK files are optional (HOSPITAL LOCATION, HOSPITAL SERVICE file, SPECIMEN SOURCE file, and BODY TYPE file). However, it is recommended for Full Download. For each of the files listed below, refer to the proper section of this manual for VITEK instructions to obtain the procedure for adding data.

1. HOSPITAL LOCATION file

**NOTE:** This is the VITEK file, **not** the DHCP HOSPITAL LOCATION file (#44).

A file printout of this file will look like the following:

hospital name

hospital address

hospital section

name of chief

(date printed) Hospital Location Page 1

------------------------------------------------------------------------

lockey	loctext

------------------------------------------------------------------------

lbw		1 BW

2BW		2 B

2BS		2 BS Psychiatry

a. Lockey - must match the abbreviation field (#l) of the DHCP HOSPITAL LOCATION file (#44) with a maximum of six (6) characters.

b. Loctext - matches the name field (#.01) of the DHCP HOSPITAL LOCATION file (#44).

2. HOSPITAL SERVICE file

A file printout of this file will look like the following:

hospital name

hospital address

hospital section

name of chief

(date printed)	Hospital service	Page 1

---------------------------------------------------------------------

serkey	sertext

---------------------------------------------------------------------

NONE

MEDICI	MEDIC

NEUROL	NEUROLOGY

a. Serkey - matches the first six characters of the name field (#.01) of the TREATING SPECIALTY file (#45.7).

b. Sertext - matches the full name of the name field (#.01) of the TREATING SPECIALTY file (#45.7).

3. SPECIMEN SOURCE file

A file printout of this file will look like the following:

hospital name

hospital address

hospital section

name of chief

(date printed)	specimen source	Page 1

---------------------------------------------------------------------

source	srcdes	source group	ser-urin

---------------------------------------------------------------------

BLOOD	BLOOD CULTURE	BLOOD	S

CSF	CSF/CEREBROSPINAL FLUID		S

BRONCH	BRONCHIAL WASHING FLUID		S

URINE	URINE	URINE 	U

a. Source - six (6) character abbreviation from the Synonym field (#8) of the DHCP COLLECTION SAMPLE file (#62).

b. Srcdes: Name field (#.01) from the DHCP COLLECTION SAMPLE file (#62).

4. BODY SITE file

A file printout of this file will look like the following:

hospital name

hospital address

hospital section

name of chief

date printed	body site	Page 1	siteid	sitetext

---------------------------------------------------------------------

Y4100 	ABDOMEN

42500 	ABDOMINAL AORTA

2Y414 	BRONCHIAL WASHING

a. Siteid - matches the SNOMED code field (#2) of the TOPOGRAPHY FIELD file (#61).

b. Sitetext - matches the name field (#.01) of the TOPOGRAPHY FIELD file (#61).

**Hints**

**•** There are many different methods for obtaining the data needed to complete the VITEK BODY SITE file. Here are two possible ways: (1) Do a FileMan print of the name field (#.01) and SNOMED Code field (#2) from the DHCP TOPOGRAPHY FIELD file (#61).

**NOTE:** The TOPOGRAPHY FIELD file (#61) contains several thousand entries.

• Use this printout to select the desired sites and SNOMED codes for entry into the VITEK BODY SITE file.

• Use the DHCP Lab accession and test counts [LRUPAC] option to generate a list of previously used culture sites for a specified time frames (i.e., two years). Use this list as a worksheet to look up the SNOMED codes and then again as a worksheet for entry into the VITEK BODY SITE file.

5. EXAM TYPE file

A file printout of this file will look like the following:

hospital name

hospital address

hospital section

name of chief

(date printed)	exam type	Page 1 	culcode	 culname	alink	  	capunit

------------------------------------------------------------------------

BLOOD		BLOOD CULTURE  		 300.0

CULTUR 	CULTURE &amp; SENSITIVITY 300.0

FUNGAL 	FUNGAL CULTURE			 300.0

GRAM S 	GRAM STAIN				 300.0

a. Culcode - Matches the first six (6) characters for the test name from the name field (#.01) of the LABORATORY TEST file (#60).

b. Culname - matches the name field (#.01) of the LABORATORY TEST file (#60).

• Print File #60, by selecting **only** the accession area Microbiology. This will eliminate CHEM and HEMO tests.

**V. DHCP File Setup**

A. General Information

There are a number of DHCP files which **must** be updated before you can run the instrument on-line. These files must be updated in the proper order for the system to work properly. Each of these will be discussed in the following sections in the order that they must be updated.

Because of the need for field sensitivity to system security, some of these files will require higher levels of FileMan access than most Lab personnel have. If, while editing these files, you do not see a field shown here, you will have to see your IRM service to have this data entered for you.

The VITEK will overlay DHCP data only if the organism name is an exact match.

**Example:** If GNR is entered as a preliminary result at the “Select ORGANISM:” prompt, the VITEK will not overlay the final ID of **E. Coli** instead **E. Coli** would be considered as a second isolate.

Each site will need to evaluate their workflow in relation to this occurrence. One possible solution is to use the Preliminary Bact Comment as a field for entry of 1+ GNR, etc. The execute code “Bacteriology” (File #62.07) may need to be edited to include this subfield (#1). (See Planning and Implementation Guide).

B. ETIOLOGY FIELD file (#61.2)

1.	Obtain lists of all organisms which the VITEK will report. These are found in Tables 3.2, 3.5, 3.8, 3.9, 3.12, and 3.14 of the VITEK Computer Interface Specification. All organisms listed in the VITEK must have an entry in the ETIOLOGY FIELD file (#61.2). “Slash call” organisms should be entered.

2.	Refer to your Microbiology implementation section in this manual for the procedure for adding these organisms.

C.	LAB DATA file (#63)

1.	Refer to the VITEK documentation (Tables 4.4 and 5.4) for a list of all drugs reported by the VITEK. All drug entries must be included in the LAB DATA file (#63).

2.	Refer to the Microbiology implementation section in this manual for the procedure in adding these New Antibiotics to LAB DATA file (#63).

D.	ANTIMICROBIAL SUSCEPTIBILITY file (#62.06).

1.	All new drug entries entered above must be added to the ANTIMICROBIAL SUSCEPTIBILITY file (#62.06).

2.	Entries in the ANTIMICROBIAL SUSCEPTIBILITY file (#62.06) should include entries in the fields:

2		Susceptibility Results

.01	Susceptibility Result ....(MIC Value)

1		Default Interpretation

3		Alternate Interpretation

Refer to VITEK documentation (Table 4.4 and 5.4) for MIC values and category interpretations for each antibiotic.

3.	Refer to your Microbiology implementation section in this manual for the procedure to add new drugs to the system and add any drug not already in the file.

E.	LABORATORY TEST file (#60)

1.	A new field was defined in this file called Culture ID Prefix.

2.	The VITEK will only accept unique accession numbers. Since a given accession containing more than one test is not considered unique by the VITEK, use of a prefix for all accessions resolves this problem.

3.	Enter a number between zero (0) and nine (9) in this field to be used as a prefix to the accession number for this test. The user must enter this prefix along with the accession number directly on the VITEK card. Then when the download program is run, the prefix will be automatically added to the accession number to make it unique. The upload program will strip the prefix off so that it does not interfere with the verification process.

If this field is not filled in, the download program will not build a record for downloading which has this test on it.

When the VITEK cards are read to determine the accession number, a blank location is considered a zero (0). Assigning the most commonly downloaded test (C&amp;S) a prefix of 0 in the LABORATORY TEST file (#60) will eliminate the need to enter a prefix on the VITEK card for any C&amp;S.

F. LABORATORY SITE file (#69.9)

1. A new field has been added—DOWNLOAD FULL DATA—that must be filled in.

2. Answering this field with “YES” will cause the download program to download the maximum amount of demographic data it can to the VITEK.

3. An answer of “NO” will cause the program to download only those fields required by the VITEK to run the sample. These required fields are the Patient ID (SSN), the Specimen ID (accession number), the Culture ID (accession number plus prefix), and the Culture Type (test name from File #60).

G. LOAD/WORK LIST file (#68.2).

1.	While the VITEK is not inherently a tray/cup type instrument, it is run this way by our system. A Load/worklist must be set up for the download routines to be able to build and send the DOWNLOAD file to the instrument.

2.	The following is an example of a load/work list for the VITEK:

Select LOAD/WORK LIST NAME: VITEK

LOAD TRANSFORM: UNIVERSAL

TYPE: TRAY/CUP

CUPS PER TRAY: 30

FULL TRAY’S ONLY: NO

EXPAND PANELS ON PRINT:

INITIAL SETUP:

VERIFY BY: ACCESSION

PROFILE: MISC

ACCESSION AREA: MICROBIOLOGY

TEST: GC CULTURE

BUILD NAME ONLY: NO

TEST: C&amp;S

BUILD NAME ONLY: NO

TEST: QUANTITATIVE CULTURE

BUILD NAME ONLY: NO

H. AUTO INSTRUMENT file (#62.4)

1. The AUTO INSTRUMENT file (#62.4) comes with an entry for the VITEK, which is used for both unidirectional and bidirectional operation.

2. Use the VA FileMan Transfer Entries option to copy this entry to the instrument number of the LSI where the VITEK will run.

**CAUTION:** Do not Delete the entry at the end when VA FileMan asks you.

3. Using the VA FileMan Enter/Edit option, fill in the beginning fields of the new entry you have just created as follows:

Select AUTO INSTRUMENT NAME: VITEK

NAME: VITEK//

ECHO DEVICE:

PROGRAM: LAMIVTK//

if running a version before VITEK 6.1 Revision AO

a. unidirectional enter LAMIVTK

b. bidirectional enter LAMIVTKU

if running VITEK R 6.1 Revision AO or later

a. unidirectional enter LAMIVT6

b. bidirectional enter LAMIVTE6

LOAD/WORK LIST: VITEK// **&lt;RET&gt;**

ENTRY for LAGEN ROUTINE: **Accession cross-reference**

CROSS LINKED BY: +ID// **&lt;RET&gt;**

ECHO ALL INPUT: NO// **&lt;RET&gt;**

METHOD:	VITEK// **&lt;RET&gt;**

DEFAULT ACCESSION AREA:	MICROBIOLOGY// **&lt;RET&gt;**

OVERLAY DATA: YES// **&lt;RET&gt;**

NEW DATA: D NEW^LASET// **&lt;RET&gt;**

RESTART: D RESTART^LASET// **&lt;RET&gt;**

HANDSHAKE RESPONSE: D^LAMIVTKC// **&lt;RET&gt;**

a. unidirectional enter S OUT=$C(6)

b. bidirectional enter D ^LAMIVTKC

ACK TRIGGER VALUE: **&lt;RET&gt;**

ACK RESPONSE VALUE: **&lt;RET&gt;**

Select TEST: ^LOAD CHEM

LOAD CHEM TESTS: **&lt;RET&gt;**

Select ALARM TERMINAL: **&lt;RET&gt;**

AMIS SUFFIX CODE: **&lt;RET&gt;**

4.	Now we will be working with several multiples fields starting with the Micro Card Type. There are many card types defined. Each of these will require updating.

The following discussion on card types will be more meaningful if you reference Appendix D of the VITEK Computer Interface Specification documentation for a numerical listing of all the valid cards for the VITEK.

**NOTE:** The Appendix D is part of your Vitek instrument documentation. We do not include a copy a as it is continually updated by the manufacturer.

* **WARNING:** These predefined card types must NEVER be deleted as all flex cards will be referring to these cards for data conversion.

**Card 0F** is the main Gram Positive Identification (GPI) card and contains the gram positive organisms listed in table 3.8 of the VITEK manual.

**Card 0FB** is the secondary Gram Positive Identification card and holds table 3.9 of gram positive organisms. This card is a pseudo card and does not have a card call.

**NOTE:** The 0F and 0FB cards are used by the processing routines as required by the data being passed by the VITEK for lookup of any Gram positive organism.

**Card 0E** is the Gram Negative Identification card (GNI) and contains table 3.5 of gram negative organisms. This card is used for look up of organisms for all gram negative cards.

**Card 0C** is used for organism look up when doing Bacillus Identification (BACIL) and contains table 3.2 of Bacillus organisms.

**Card 05** is used for organism look up when doing Yeast identification (YBC) and contains table 3.14 of Yeast organisms.

**Card 0B** is used for urine identification for the UID-1 card and contains table 3.12 list of organisms.

**Card 12** is used for urine identification from the UID-3 card and contains table 3.12 list of organisms.

**NOTE:** The above examples are of the cards most likely to be used by a site.

Select MICRO CARD TYPE: **0F** (HEX Code from VITEK APPENDIX D)

MICRO CARD TYPE: 0F// **&lt;RET&gt;**

CARD NAME: GPI// **&lt;RET&gt;**

PROCESS CARD CALL: D 511^LAMIV11// **&lt;RET&gt;**

Process card calls for the remaining card types are:

a.	For GPI card enter D 511^LAMIV11

b.	For GPI-2 card enter nothing.

c.	For GNI card enter D 512^LAMIV12

d.	For Bacillus card enter D 52^LAMIV10

e.	For Yeast card enter D 54^LAMIV11

f.	For UID-l card enter D ^LAMIV10

g.	For UID-3 card enter D 510^LAMIV10

h.	For Gram Neg Flex cards enter D ^LAMIV12

i.	For Gram Pos Flex cards enter D ^LAMIV11

These card calls change the encoded VITEK data into an organism name, a drug name, a raw MIC value, and an interpretation, which will be displayed during verification.

5.	Now within the MICRO Card Type field enter in the organisms **only** for those cards which are Identification type cards (i.e., Gram Negative Id, Gram Positive Id, Bacillus ID, etc.). If this is not an ID card but a Flex Susceptibility card leave this field blank and continue at Step #7 below.

For each organism enter the organism name as listed in the ETIOLOGY FIELD file (#61.20) and its card code from tables 3.2, 3.5, 3.8, 3.9, 3.12, or 3.14 in the VITEK Computer Interface Specification. Many organisms will have multiple entries. Use the conventional FileMan method of quotes around the name (organism) to enter an organism after the first entry has been made.

Select ORGANISM: STREPTOCOCCUS PYOGENES

ORGANISM: STREPTOCOCCUS PYOGENES// **&lt;RET&gt;**

CARD CODE FOR ORGANISM: 00// **&lt;RET&gt;** (HEX code from table 3.8)

Select ORGANISM: **&lt;RET&gt;**

6.	Continue adding organisms for this card type until you have them all  entered. When you have them entered for this card type use the ^ to leave this card type and return to the “MICRO CARD TYPE” prompt and continue to Step #7 below.

7.	For card types which are Flex panel cards, it will be necessary to add drugs to the card type along with several other pieces of data. Each drug listed for a given card type must be entered in the file. Some antimicrobials will have multiple entries, each with a different card code.

The routine LAMIV00 contains all the strings of code for processing the card data into raw MIC values. A printout of all line tags with comments (Printout A) is at the end of this section. Also included are printouts of the X replacement values in PARAM1 for GNS and GPS cards (Printouts B and C), respectively.

These printouts along with your VITEK Computer Interface Specification documentation of drug Tables 4.4 and 5.4 and the Section references 4.3 (GNS Flex panel card configuration) and 5.3 (GPS Fles panel card configuration) will be used for filling in the PARAM1 field.

The line references within this routine have documentation for which interpretation table and which drug codes are valid for that string.

Select MICRO CARD TYPE: **13** (HEX CODE FROM VITEK APPENDIX D)

MICRO CARD TYPE: 13// **&lt;RET&gt;**

CARD NAME: GNS// **&lt;RET&gt;**

PROCESS CARD CALL: D ^LAMIV12// **&lt;RET&gt;** (See above)

Select ORGANISM: **&lt;RET&gt;**

Select DRUG: **CHLORAM** (See VITEK Section 4.3, GNS CARD CONFIGURATION)

DRUG: CHLORAM// **&lt;RET&gt;**

DRUG NODE:2.0008// (No Editing)

PARAM1: **S LARTN=“x”\_U\_”LAMIV00” D @LARTN**

a.	The string of code above is the same for all PARAM1 fields except for the character x.

b.	To determine the value for the character x refer to the card configuration reference in section 4.3 (GRAM NEGATIVE) or 5.3 (GRAM POSITIVE) of the VITEK Computer Interface Specification. In this example we are dealing with the GNS card which is the first card listed in section 4.3.

c.	Referring to VITEK Table 4.4, we see that the drug, Chloramphenicol, has several interpretations listed — one set of interpretations for a card code of 6 and another set of interpretations for a card code of d.

d.	The drug Chloramphenicol has two possible card codes to be entered. Let’s focus on the second code d.

e.	Referencing Printout B (GNS CARD TYPES) of DHCP VITEK Interface Guide, look down the list of GNS drugs until you find Chloramphenicol with a CODE of “d”. The x replacement value is “8”.

f.	Enter the PARAM1 string as shown above and replace the x character with the code given for this card and drug code listed Printout B.

g.	Therefore the string of code for PARAM1 will be entered as:

S LARTN=“8”\_U\_”LAMIV00” D @LARTN

If the drug has more than one code for the Flex card the drug must be added one time for each code that is used. As in this case, we would have to add Chloramphenicol a second time with a card code of “6” and the x PARAM1 field having a value of “7”.

Card Code: d//

This is the drug code for this drug as listed in the VITEK computer interface specifications section 4.3 (gram negative) or 5.3 (gram positive) card types.

There are some drugs with card codes of “@^?” which cannot be added through FileMan. When these codes are encountered, leave the card code field blank. After the card type is completed, we will run a routine which will add these codes.

Display Order: 7//

This field controls the order of display of the drugs during verification. In most cases, this would be the order in which the results are printed on the VITEK printer. If a given drug has multiple entries for this card type, each entry should have the **same** display order.

Section:

Bit Position:

Select Drug:

8.	Continue adding drugs for this card type until you have them all entered. When you have completed entering drugs, enter “^” at the “Select Drug” prompt to take you back to the “MICRO CARD TYPE” prompt.

Select MICRO CARD TYPE: **&lt;RET&gt;**

INTERFACE NOTES:. . .

221&gt;

EDIT Option: **&lt;RET&gt;**

DOWNLOAD ENTRY: **&lt;RET&gt;**

DOWNLOAD PROTOCOL ROUTINE: **&lt;RET&gt;**

FILE BUILD ENTRY: **&lt;RET&gt;**

FILE BUILD ROUTINE:	LAMIVTKD// **&lt;RET&gt;**

SEND TRAY/CUP LOCATION:	no// **&lt;RET&gt;**

QUEUE BUILD:  no// **&lt;RET&gt;**

MICRO INTERPRETATION CHECK: F

METH NAME: **&lt;RET&gt;**

MEAN DATA VALUE 1: **&lt;RET&gt;**

MEAN DATA VALUE 2: **&lt;RET&gt;**

9. Once you have filled in the data for the MICRO card types and finished the rest of the auto instrument entry you may have to run a routine to add the additional drug codes listed in Step #7 above. If you do not need to add any codes, go to step #11.

10. Adding drug codes “@^?” is done by running the option Load VITEK special characters. This routine (LRMICRA) will prompt the auto instrument entry, the card type, and then step through the drug nodes displaying the entered code. You can enter the code or press return to accept the default. The routine will either continue, when the return is pressed, or enter the code into the file and build the “C” cross-reference entry for you.

***WARNING:** If the AUTO INSTRUMENT file (#62.4) is ever reindexed you will have to run this option again to re-enter these codes, as they will be lost.

11. You have now completed the AUTO INSTRUMENT file (#62.4).

**VI. Operational Procedures**

A. **Unidirectional:** The VITEK in unidirectional mode requires no special procedure. The cards are placed in the incubators after being inoculated and marked with the accession number. When the results are available they will be automatically uploaded to DHCP and processed.

B. **Bidirectional:** The operation in bidirectional mode is somewhat different than the unidirectional mode since the demographics and tests will be downloaded to the instrument. Information (for building the download files) is collected from the Load/Work List.

The following is a typical procedure to utilize the bidirectional capabilities after the accessioning process is completed.

1. The accession number with prefix is placed on the VITEK card to be run.

2. The card is inoculated.

3. The card is placed in the incubator.

4. The tech then uses the option Add accession to micro worklist to add the accessions and build the appropriate list.

5. After all accession have been added, the tech uses the Download to Micro Auto Instrument option. This option builds the download files and downloads them into the VITEK.

6. When the download is completed, the VITEK will begin processing the cards.

7. When the results are complete on the VITEK, the card is read and the results are uploaded to DHCP and processed.

8. The tech then uses the Verify Micro Auto Instrument Data option to edit/verify the data.

#### Troubleshooting for VITEK

**Problem:** No organism for this accession

**Possible Causes &amp; Solutions:**

1. Organism has two or more columns of susceptibility results for one VITEK card.

**Solution:** Organism must be given Key I.D. on VITEK and retransmitted to DHCP.

2. The probability is &lt; 80%, therefore the LAMIV1* programs will screen out these isolates and will not be transfer them to ^LAH.

3. Isolate needs to be Key ID on the VITEK

4. Organism has not been entered in AUTO INSTRUMENT file (#62.4).

**Solution:** Enter organism in AUTO INSTRUMENT file (#62.4), subfield micro card type, subfield organism.

5. Organism code in AUTO INSTRUMENT file (#62.4) is incorrect.

**Solution:** Refer to VITEK interface specifications. Correct organism code in AUTO INSTRUMENT file (#62.4).

6. Each organism in the AUTO INSTRUMENT file (#62.4) must have a cross reference, ^LAB(62.4,X,7,Card,2, “C”

**Solution:** Delete organism entry, reenter it in the AUTO INSTRUMENT file (#62.4), and then re-transmit data.

7. Organism is not properly identified in the ETIOLOGY FIELD file (#61.2).

**Solution:** All organisms added to the AUTO INSTRUMENT file (#62.4) must be identified as Bacterium, Fungus, or Mycobacterium.

8. Result was not sent from the VITEK or interface program was not running.

**Solution:** Retransmit, using the CISEND menu, Check status of lab program. Remember that the data can only be re-transmitted if the cards are still in the VITEK incubator.

**Problem:** Only one isolate is displayed, and ALL the VITEK cards for that accession number are displayed for that organism (e.g., Kleb pneumo GNI, GNSFl, GNSF2 cards run, Enterococcus GPSTA card run, yet all cards are displayed for Kleb pneumo).

**Possible Cause and Solution:**

Each isolate run on the VITEK must be given a unique ID number. The last digit is processed as the isolate number for that accession.

**Solution:** Be sure each isolate is assigned a unique ID number. For example, 3000-0 (gram neg isolate #1), 3000-1(gram positive isolate #1), 3000-2 (gram positive isolate #2). If you do not use the zero to indicate the first isolate, then 3000-1 is isolate #1.

**Problem:** Susceptibility Interpretation is incorrect

**Possible Solutions:**

1. Edit the drug in the ANTIMICROBIAL SUSCEPTIBILITY file (#62.06). Many drugs such as Ticarcillin and Mezlocillin have different interpretations, depending on the type of organism identified. Use the Alternate Interpretation field to set up correct interpretation for the isolate. Use the most common result for the field susceptibility result, and then enter the “exceptions” using the Alternate Interpretation field.

2. Check Param1 value for that drug in the AUTO INSTRUMENT file (#62.4). The MIC value is set when Param1 is executed.

**Problem:** Unable to use E to edit a drug sent from the VITEK

**Possible Solution:**

1. Add the drug to the Edit Template defined in File #63. The edit templates are associated with each organism in the ETIOLOGY FIELD file (#61.2). The template drugs may be changed by editing the template in File (#63).

**Problem:** No data uploaded for an accession

**Possible Solutions:**

1. Use VITEK CISEND menu to send a test pattern to ^LA WATCH the data in the ^LA global to check and see if the data gets there. If the test pattern is not sent to ^LA, check the interface cable or the LSI. Verify that the interface is enabled on the VITEK.

2. Verify that the lab job and auto instrument routine are running.

**Problem:** **No data for VITEK worklist**

**Possible Solution:** Check Param 1 values in AUTO INSTRUMENT file (#62.4). Clerical errors in this field could cause the program to error out. For example, an incorrect line tag entry would cause a &lt;liner&gt; error. If the program does not process the data successfully, no data will be transferred to ^LAH.

**Problem:** Unable to edit comments which were sent from the VITEK

**Possible Solution:** Check the Edit code in File #60 and in the EXECUTE CODE file (#62.07). This code determines which fields are displayed to the user. Special messages which are uploaded from the VITEK to DHCP are stored as comments in File #60 (LAB DATA), Field #5 (Microbiology), Subfield #12 (organism), and Subfield #2 (Comment).

#### Printout A

**laMIV00;SLC/DLG/FHS/DAL - PROCESS VITEK V VALUE FROM FILE ;7/20/90  09:37 ;;;5.14P2;LAB;;07/15/92 12:13**

IN PARAM1 OF THE DRUG NODE OF THE MICRO CARD TYPE OF THE AUTO INSTRUMENT FILE YOU ENTER S RUN="x"\_LARTN D @RUN WHERE x IS THE LINE TAG WHICH WILL DETERMINE THE MIC VALUE.

0;	POS CODE 7=?C

1;	POS CODE 0&lt;&gt;B

2;NEG CODE 1

3;NEG CODE [   	POS CODE G

4;	POS CODE 34

5;NEG CODE 79 	POS CODE 5

6;NEG CODE AD, 	POS CODE 9 ab

7;NEG CODE 68,   	POS CODE 8 QR

8;NEG CODE d  	POS CODE 2@

9;	POS CODE :

A;NEG CODE \    	POS CODE DI

B;NEG CODE 345, 	POS CODE 1

C;NEG CODE 0,

D;NEG CODE ;

E;NEG CODE &lt;

F;NEG CODE Tjt     	POS CODE H

G;NEG CODE NPR grs  	POS CODE E NOS

H;NEG CODE HI	POS CODE M

I;NEG CODE C

J;NEG CODE MWXY] yxz   	POS CODE F

K;NEG CODE GV

L;NEG CODE FJO\_akl

M;NEG CODE &gt;?@

N;NEG CODE :

O;NEG CODE bc

P;POS CODE ;A

Q;NEG CODE SU

R;NEG CODE Zfuy	POS CODE P

S;NEG CODE K^

T;NEG CODE Qghmnop

U;NEG CODE 2`

V;NEG CODE i  	POS CODE 6

W;NEG CODE L

X;NEG CODE E

Y;NEG CODE e

Z;NEG CODE =

A1;	POS CODE J

A2;	POS CODE K

A3;	POS CODE L

A4;NEG CODE B

A6;NEG CODE w	POS CODE T

#### Printout B


**NOTE:** This printout is an example only. Due to the constant updating by MicroScan, you should consult the manufacturers literature for the most recent information.

### 30 GNS Card Types

DRUG 	DRUG	‘x’ REPLACEMENT

CODE 	NAME	VALUE FOR PARAM1

O	AMIKACIN	C

;	AMIKACIN	D

X	AMOXICILLIN/CA	J

1	AMPICILLIN	2

&lt;	AMPICILLIN	E

F	AZLOCILLIN	L

\_	AZLOCILLIN	L

Y	AZTREONAM	J

2	CARBENICILLIN	U

=	CARBENICILLIN	Z

`	CARBENICILLIN	U

3	CEFAMANDOLE	B

&gt;	CEFAMANDOLE	M

M	CEFAZOLIN	J

N	CEFONICID	G

G	CEFOPERAZONE	K

H	CEFOTAXIME	H

Z	CEFOTETAN	R

4	CEFOXITIN	B

?	CEFOXITIN	M

W	CEFTAZIDIME	J

O	CEFTIZOXIME	L

a	CEFTIZOXIME	L

V	CEFTRIAXONE	K

P	CEFUROXIME	G

q	CEFUROXIME

5	CEPHALOTHIN	B

@	CEPHALOTHIN	M

6	CHLORAMPHENICOL	7

d	CHLORAMPHENICOL	8

S	CINOXACIN	Q

f	CINOXACIN	R

[	CIPROFLOXACIN	3

\	ENOXACIN	A

7	GENTAMICIN	5

A	GENTAMICIN	6

T	IMIPENEM	F

Q	MEZLOCILLIN	T

g	MEZLOCILLIN	T

h	MEZLOCILLIN	T

I	MOXALACTAM	H

U	NALIDIXIC ACID	Q

R	NETILMICIN	G

B	NITROFURANTOIN	A4

e	NITROFURANTOIN	Y

i	NITROFURANTOIN	V

]	NORFLOXACIN	J

j	NORFLOXACIN	F

J	PIPERACILLIN	L

k	PIPERACILLIN	L

l	PIPERACILLIN	L

8	TETRACYCLINE	7

C	TETRACYCLINE	I

K	TICARCILLIN	S

L	TICARCILLIN	W

m	TICARCILLIN	T

n	TICARCILLIN	T

^	TICARCILLIN/CA	S

o	TICARCILLIN/CA	T

p	TICARCILLIN/CA	T

9	TOBRAMYCIN	5

D	TOBRAMYCIN	6

:	TRIMETH-SULFA	N

E	TRIMETH-SULFA	X

b	TRIMETH-SULFA	O

c	TRIMETH-SULFA	O

r	AMPICILLIN/SULBACTAM	G

w	OFLOXACIN	A6

s	CEFSULODIN	G

t	DOXYCLINE	F

u	FOSFOMYCIN	R

v	MINOCYCLINE

x	CEFACLOR	J

y	CEFOTIAM	R

z	CEPHRADINE	J

10	NITROXOLIN	J

#### Printout C


**NOTE:** This printout is an example only. Due to the constant updating by MicroScan, you should consult the manufacturers literature for the most recent information.

### 32 GPS Card Types

DRUG	DRUG	‘x’ REPLACEMENT

CODE	NAME	VALUE IN PARAM1

D	AMOXICILLIN/CA	A

O	AMPICILLIN	1

&lt;	AMPICILLIN	1

&gt;	AMPICILLIN	1

B	AMPICILLIN	1

E 	AMPICILLIN/SULBACTAM 	G

F	CEFAZOLIN	J

1	CEPHALOTHIN	B

2	CHLORAMPHENICOL	8

@	CHLORAMPHENICOL	8

G	CIPROFLOXACIN	3

3	CLINDAMYCIN	4

4	ERYTHROMYCIN	4

5	GENTAMICIN	5

K	GENTAMICIN	A2

6	NITROFURANTOIN	V

H	NORFLOXACIN	F

:	OXACILLIN	9

I	OXACILLIN	A

7	PENICILLIN G	O

=	PENICILLIN G	O

?	PENICILLIN G	O

C	PENICILLIN G	O

J	RIFAMPIN	Al

L	STREPTOMYCIN	A3

8	TETRACYCLINE	7

;	TRIMETH-SULFA	P

A	TRIMETH-SULFA	P

9	VANCOMYCIN	6

a	VANCOMYCIN	6

b	VANCOMYCIN	6

M	CEFOTAXIME	H

O	CEFUROXIME	G

P	FOSFOMYCIN	R

Q	FUSIDIC ACID	7

R	IMIPENEM	7

S	NETILMICIN	G

T	OFLOXACIN	A6

#### Printout D


**NOTE:** This printout is an example only. Due to the constant updating by MicroScan, you should consult the manufacturers literature for the most recent information.

### 34 Micro Card Type: 13

NUMBER: 7	NAME: VITEK BI-DIRECTIONAL

PROGRAM: LAMIVTE6	LOAD/WORK LIST: VITEK

ENTRY FOR LAGEN ROUTINE: Accession cross-reference

CROSS LINKED BY: +ID	ECHO ALL INPUT: YES

METHOD: VITEK	DEFAULT ACCESSION AREA: MICROBIOLOGY

OVERLAY DATA: YES	HANDSHAKE RESPONSE: D ^LAMIVTKC

NEW DATA: D NEW^LASET	RESTART: D RESTART^LASET

MICRO CARD TYPE: 13	CARD NAME: GNS

ORGANISM: ESCHERICHIA COLI	CARD CODE FOR ORGANISM: 00

ORGANISM: PROTEUS MIRABILIS	CARD CODE FOR ORGANISM: 01

ORGANISM: PROTEUS SP	CARD CODE FOR ORGANISM: 02

ORGANISM: KLEBSIELLA SP	CARD CODE FOR ORGANISM: 03

ORGANISM: PSEUDOMONAS AERUGINOSA	CARD CODE FOR ORGANISM: 04

ORGANISM: PSEUDOMONAS SP	CARD CODE FOR ORGANISM: 05

ORGANISM: CITROBACTER SP	CARD CODE FOR ORGANISM: 06

ORGANISM: ENTEROBACTER SP	CARD CODE FOR ORGANISM: 07

ORGANISM: SERRATIA SP	CARD CODE FOR ORGANISM: 08

ORGANISM: PROVIDENCIA SP	CARD CODE FOR ORGANISM: OA

ORGANISM: PSEUDOMONAS MALTOPHILIA 	CARD CODE FOR ORGANISM: OB

ORGANISM: ACINETOBACTER SP	CARD CODE FOR ORGANISM: 0C

NUMBER: 1	DRUG: AMIKACN

DRUG NODE: 2.0016	PARAMl: S LARTN=“C”\_U\_”LAMIV00”D @LARTN

CARD CODE: O	DISPLAY ORDER: 1

NUMBER: 2	DRUG: AMPICLN

DRUG NODE: 2.0012	PARMl: S LARTN=“2”\_U\_”LAMIV00” D @LARTN

CARD CODE: 1	DISPLAY ORDER: 2

NUMBER: 3	DRUG: CARBENICILLIN

DRUG NODE: 2.0013	PARMl: S LARTN=“U”\_U\_”LAMIV00” D @LARTN

CARD CODE: 2	DISPLAY ORDER: 3

NUMBER: 4	DRUG: CEFMAND

DRUG NODE: 2.0017	PARMl: S LARTN=“B”\_U\_”LAMIV00” D @LARTN

CARD CODE: 3	DISPLAY ORDER: 4

NUMBER: 5	DRUG: CEFOXITIN

DRUG NODE: 2.0018	PARMl: S LARTN=“B”\_U\_”LAMIV00” D

@LARTN

CARD CODE: 4	DISPLAY ORDER: 5

NUMBER: 6	DRUG: CEPHALOTHIN

DRUG NODE: 2.0034	PARMl: S LARTN=“B”\_U\_”LAMIV00” D @LARTN

CARD CODE: 5	DISPLAY ORDER: 6

NUMBER: 7	DRUG: CHLORAM

DRUG NODE: 2.0008	PARMl: S LARTN=“7”\_U\_”LAMIV00” D @LARTN

CARD CODE: 6	DISPLAY ORDER: 7

NUMBER: 8	DRUG: GENTMCN

DRUG NODE: 2.0007	PARMl: S LARTN=“5”\_U\_”LAMIV00” D @LARTN

CARD CODE: 7	DISPLAY ORDER: 8

NUMBER: 9	DRUG: TETRCLN

DRUG NODE: 2.0011	PARMl: S LARTN=“7”\_U\_”LAMIV00” D @LARTN

CARD CODE: 8	DISPLAY ORDER: 9

NUMBER: 10	DRUG: TOBRMCN

DRUGNODE: 2.0014	PARMl: S LARTN=“5”\_U\_”LAMIV00” D @LARTN

CARD CODE: 9	DISPLAY ORDER: 10

NUMBER: 11	DRUG: TRMSULF

DRUG NODE: 2.0015	PARMl: S LARTN=“N”\_U\_”LAMIV00” D @LARTN

CARD CODE::	DISPLAY ORDER: 11

NUMBER: 14	DRUG: CARBENICILLIN

DRUG NODE: 2.0013	PARMl: S LARTN=“U”\_U\_”LAMIV00” D @LARTN

CARD CODE: ‘	DISPLAY ORDER: 3

NUMBER: 22	DRUG: TRMSULF

DRUG NODE: 2.0015	PARMl: S LARTN=“O”\_U\_”LAMIV00” D @LARTN

CARD CODE: b	DISPLAY ORDER: 11

NUMBER: 23	DRUG: CHLORAM

DRUG NODE: 2.0008	PARMl: S LARTN=“8”\_U\_”LAMIV00” D @LARTN

CARD CODE: d	DISPLAY ORDER: 7

PROCESS CARD CALL: D ^LAMIV12

NUMBER: 1	CODE: 46

FLAG VALUE: O	MESSAGE: Oxidase negative

NUMBER: 2	CODE: 46

FLAG VALUE: 1	MESSAGE: Oxidase positive

#### Printout E


### 36 VITEK Printout Results

Accession # 3130

AMS ID	503130-0 (A1-5)	DSAMS0-R6.4

Report date:	Tue Jul 24 11:55:47 1992

Type:	Gram Negative Identification Card

FINAL	Elapsed time:	4 hours

DP3 -	OFG +	GC  +	ACE -	ESC +	PLI +

URE +	CIT +	MAL +	TDA -	PXB -	LAC +

MLT +	MAN +	XYL +	RAF +	SOR +	SUC +

IND +	ADO +	COU -	H2S -	ONP +	RHA +

ARA +	GLU +	ARG -	LYS +	ORN -	OXI -

3371776364

99 % Klebsiella pneumoniae (indole -)/oxytaca (indole +)

1 % Enterobacter aerogenes

AMS ID	503130-0 (A1-6) 	DSAMS0-R6.4

Report date:	Tue Jul 24 11:55:48 1992

Type:	Gram Negative General Susceptibility - F1

FINAL	Elapsed time:	5 hours

Cefazolin	&lt;=8 S

Ceftazidime	&lt;=8 S

Ceftriaxone	&lt;=8 S

Gentamicin	&gt;=16 R

Amikacin	&lt;=2 S

Cefotetan	&gt;=16 S

Cefoxitin	&lt;=2 S

Cefuroxime-sodium 	&lt;=4 S

Cefuroxime-axetil 	&lt;=4 S

Cephalothin	&gt;=32 R

Tobramycin	&gt;=16 R

MIC values in mcg/ml ( M2)	Oxidase negative

GNI ID:	Klebsiella pneumoniae (indole -)/c (indole +)

3371776364

AMS ID	503130-0 (A1-7)	DSAMS0-R6.4

Reportdate: 	TueJul 24 11:55:49 1992

Type:	Gram Negative General Susceptibility - F2

FINAL	Elapsed time: 	5 hours

Ampicillin	&gt;=32 R

Ciprofloxacin	&lt;=0.5 S

Piperacillin	&gt;=256 R

Tetracycline	&gt;=16 R

Trimeth-sulfa	&lt;=10 S

Aztreonam	&lt;=8 S

Carbenicillin	&gt;=512 R

Imipenem	&lt;=4 S

Mezlocillin	&gt;=256 R

Ticarcillin	&gt;=256 R

Ticarcillin/CA	&gt;=256 R

MIC values in mcg/ml( M2 )	Oxidase negative

GNI ID: Klebsiellapneumoniae (indole -)/oxytoca (indole +)

3371776364

AMS ID	503130-0 (A1-6)	DSAMS0-R4.01

Report date: 	Tue Jul 24 11:55:48 1990

Type: Gram Negative General Susceptibility - Fl

FINAL Elapsedtime: 	5 hours

Albacillin/Sulbact	&gt;=32 R

Cephalothin	&gt;=32 R

Ciprofloxacin	&lt;=0.5 S

Clindamycin	&gt;=8 R

Erythromycin	&gt;=8 R

Oxacillin	&gt;=8 R

Penicillin	&gt;=16 R

Tetracycline	&gt;=16 R

Trimeth-sulfa	&lt;=10 S

Vancomycin	&lt;=0.5 S

Beta lactamase	Positive

MIC values in mcg/ml ( M2)Catalase positive

Keyboard ID:Coag negative staph.

Mate not resident

CF, CA, AMOX/CA, AMP/SULB reported as “R” for oxacillin-resistant staph-NCCLS

INTERFACE GUIDE

FOR OE/RR PACKAGE

**NOTE:** Please refer to the OE/RR documentation for the most recent information.

1. Use this routine to load the lab protocols in the PROTOCOL file (#101). This should only be used the first time you install OE/RR.

**D EN^LRX6**

2. Use the OE/RR Interface Parameters options, on the Lab Liaison Menu to edit the parameters as indicated by the OE/RR documentation.

**Comments:**

1. Integration between the Laboratory package and OE/RR can be switched “ON” or “OFF” by editing a single field. To do so, edit the ON field in the Package Site Parameters multiple field of the ORDER PARAMETERS file (#100.99).

2. A cross reference exists in LABORATORY TEST file (#60), Field #200.01 to enhance the capability to check for duplicate orders.

3. Review the accuracy and applicability of the Laboratory administration schedules.

ROUTINE DESCRIPTIONS

#### Routine Descriptions

#### LA routines

LA1103 ;SLC/RWF- TO CHECK THE STATUS OF THE LSI-11 INTERFACE ; 8/5/87  21:0 ;

LAABL3 ;SLC/RWF- ABL3/ABL4 BLOOD GAS INSTRUMENT ;7/20/90  07:08 ;

LAABL500;SLC/RAF - RADIOMETER ABL500,505,520  ;5/27/93  07:00;

LAACA  ;SLC/RWF,CJS- 'ACA3' ROUTINE FOR AUTOMATED DATA  ;8/16/90  14:52 ;

LAACA4 ;SLC/RWF- ACA4, ACA5, DIMENSION ;7/20/90  07:11 ;

LAALTA ;SLC/RWF- ALTAIRE ;7/20/90  07:12 ;

LAAIMX  ;INDY/PLS;SLC/RAF- IMX ROUTINE FOR MEIA QUAN. DATA; 06/18/93  11:01 ;;;PLS 55693,31670

LAASTRA;SLC/RWF- ASTRA 4,6,8,8E,IDEAL (CALCULATING IE ANION GAP;7/20/90 07:13;

LAB    ;SLC/RWF- AUTOMATED INSTRUMENT LAB INTERFACE ;9/10/90  13:59 ;

LABALARM;SLC/RWF- ALARM FOR LAB ;7/20/90  07:18 ;

LABCX4B;SLC/DLG- BECKMAN CX4 AND CX5 UNI AND BIDIRECTIONAL ;7/20/90  07:25 ;

LABCX4D;SLC/DLG - BECKMAN CX4 AND CX5 BUILD DOWNLOAD FILE. ;8/16/90  10:33 ;

LABCX4H;SLC/DLG - BECKMAN CX4 AND CX5 PROTOCOL CONTROLLER ; 3/28/89  9:37 AM ;

LABCX4I;SLC/DLG/FHS - BECKMAN BIDIRECTIONAL DIRECT CONNECT SETUP ;9/21/90

LABCX4XX;SLC/DLG- BECKMAN BIDIRECTIONAL DIRECT CONNECT INTERFACE ;8/16/90 14:53;

LABERR ; SLC/FHS - ERROR TRAP FOR LABORATORY AUTO INSTRUMENTS  ;11/20/90  09:45

LABERRP; SLC/FHS - PRINT OUT LA("ERR" ERROR TRAP

LABINIT;SLC/RWF- LAB INIT RUNTIME ;8/16/90  10:18 ;

LABIOH ;SLC/RWF- ROUTINE FOR BIOVATION HEME KEYPADS ;7/20/90  07:32 ;

LABIOU ;SLC/RWF- ROUTINE FOR BIOVATION URINALYSIS KEYPAD ;7/20/90  07:33 ;

LABITKU;SLC/DLG- BECKMAN INTERLINK UPLOAD UNIDIRECTIONAL ; 5/9/89  2:36 PM ;

LABL330;SLC/ECB&amp;RWF,DLG- ABL330 BLOOD GAS ANALYZER; ;9/17/90  12:47

LABMD87P;SLC/RWF- BMD 8700 ROUTINE USING REPORT FORMAT ;7/20/90  07:35 ;

LABTEST;SLC/RWF- AUTOMATED INSTRUMENT INTERFACE TESTING ;7/20/90  07:37 ;

LAC178 ;SLC/RWF - CORNING 178 BLOOD GAS ;7/20/90  07:41 ;

LAC178HP;SLC/FHS  DUAL CORNING 178 VIA HP COMPUTER ;8/16/90  14:12

LACBIO ;SLC/DCM/RWF- COBAS BIO DATA  ;7/20/90  07:43 ;

LACCHEM6;SLC/RWF- CENTRIFICHEM 600 ;7/20/90  07:43 ;

LACEL8E;SLC/DLG - CELLECT 8E ;8/16/90  14:07 ;

LACFARA;SLC/RWF- COBAS FARA ;7/20/90  07:45 ;

LACHEM1;SLC/DLG- TECHNICON CHEM1 UNIDIRECTIONAL AUTOMATED DATA;7/20/90 07:46 ;

LACL5500;SLC/RWF- AMES CLINI-TEK 5500 ;7/20/90  07:47 ;

LACLNTE;SLC/RWF- AMES CLINI-TEK FORM PRINTER AUTOMATED DATA  ;8/16/90  14:53 ;

LACLNTEK;SLC/RWF- AMES CLINI-TEK AUTOMATED DATA ;8/16/90  14:54 ;

LACLT200;SLC/RWF- AMES CLINI-TEK 200 ;7/20/90  07:49 ;

LACLT20P;SLC/RWF/RAF- AMES CLINITEK 200 PLUS ; 7/14/93  8:20 AM ;

LACMIRA;SLC/DLG- COBAS MIRA ;10/22/91  08:59 ;

LACMIRAS;SLC/DLG- COBAS MIRA S ;7/20/90  07:50 ;

LACOAGX2;SLC/RWF- ROUTINE FOR COAGAMATE X2 ;7/20/90  07:51 ;

LACOARA4;SLC/RAF - ORGANON RA4 INTERFACE ;09/12/94   07:00

LACOLT ;SLC/RWF- COULTER SR DATA PROCESSING ;7/20/90  07:51 ;

LACOLT1;SLC/RWF- COULTER S+ DATA PROCESSING ;7/20/90  07:52 ;

LACOLT2;SLC/RWF- COULTER S PLUS II DATA PROCESSING ;7/20/90  07:53 ;

LACOLT24;SLC/RWF- COULTER S WITH A EDMAC MODEL 2400 INTERFACE ;7/20/90 07:53 ;

LACOLT3;SLC/RWF- FOR COULTER SR. PLUS II WITH QC MODULE ;7/20/90  07:54 ;

LACOLT5;SLC/RWF- COULTER S PLUS T660 IV V VI JT JT3 SR ST STKR;7/20/90 07:54 ;

LACOLT6;SLC/RWF- COULTER S PLUS VI, DT WITH DH INTERFACE ;7/20/90  07:55 ;

LACOLTSE;SLC/DLG/FHS - COULTER STACK S VER. 1E SOFTWARE DATA PROCESSING ;8/16/90  14:0 ;

LACOLTSS;SLC/DLG- COULTER STACK S DATA PROCESSING ;8/16/90  14:0 ;

LACRIT ;SLC/RWF- PRINT OUT CRITICAL VALUES AT DATA GATHER TIME;7/20/90 07:56 ;

LACTDMS;SLC/DLG- AMES CLINI-TEK 200 W/DMS ;7/20/90  07:57 ;

LADACOS;SLC/RWF- COULTER DACOS ;7/20/90  08:0 ;

LADEKT7B;SLC/RWF/DLG - EKTACHEM 700 BI-DIRECTIONAL  ;7/23/90  11:04 ;

LADIMD ;SLC/DLG- DIMINESION BUILD DOWNLOAD FILE. ;10/17/90  12:51 ;

LADIMPI;SLC/DLG/FHS - DIMENSION DIRECT CONNECT SETUP ;8/16/90  14:15 ;

LADIMPXX;SLC/DLG- DIMENSION DIRECT CONNECT INTERFACE ;8/16/90  14:15 ;

LADJOB ;SLC/DLG- JOB DIRECT CONNECTED AUTOMATED LAB ROUTINES ;6/25/90  13:46

LADKERM2;SLC/RWF/DLG - BUILD A KERMIT FILE TO SEND  ;2/8/90  14:50 ;

LADKERM3;SLC/RWF/DLG - UNPACK KERMIT RECORDS  ;12/6/89  09:24 ;

LADKERMI;SLC/RWF/DLG - KERMIT PROTOCOL CONTROLLER  -  DIRECT CONNECT ;7/19/90 15:06 ;

LADMND ;SLC/RWF- DEMAND ANALYZER IN MODE 3 ;7/20/90  08:06 ;

LADOWN ;SLC/RWF - TOP LEVEL OF DOWNLOAD OPTIONS ;7/20/90  08:06 ;

LADOWN1;SLC/DG - UTILITY PARTS OF DOWNLOAD ;7/20/90  08:07 ;

LAE4A  ;SLC/RWF- BECKMAN E4A ELECROTLYTE ANALYZER ;8/16/90  14:15 ;

LAEKT4 ;SLC/RWF- KODAK EKTACHEM 400 ROUTINE ;7/20/90  08:11 ;

LAEKT7 ;SLC/RWF- KODAK EKTACHEM 700 ROUTINE ;7/20/90  08:11 ;

LAEKT7B;SLC/RWF/DLG- EKTACHEM 700 BI-DIRECTIONAL  ;8/17/90  09:10 ;

LAEKT7D;SLC/RWF/DLG - KODAK EKTACHEM 700 BUILD DOWNLOAD FILE. ;8/15/90 15:10 ;

LAEKT7P;SLC/RWF- KODAK EKTACHEM 700 ROUTINE ** MODIFIED TO USE 2ND PRINTER PORT ** ;7/20/90  08:14 ;

LAELT  ;SLC/RWF- ELT 8/8DS AUTOMATED DATA ;8/16/90  13:59 ;

LAELT8D;SLC/RWF- ORTHO ELT8 WITH 3 CELL DIFF / ELT 1500 ;7/20/90  08:16 ;

LAEPXD ;SLC/DLG -ABBOTT EPX BUILD DOWNLOAD FILE. ;7/20/90  08:20 ;

LAEPXPXX;SLC/DLG- AUTOMATED SINGLE INSTRUMENT EPX DIRECT CONNECT LAB INTERFACE ;9/5/90  14:34 ;

LAERA  ;SLC/DLG- PHOTON ERA ;7/20/90  08:21 ;

LAEXEC ;SLC/RWF- ABBOTT EXECUTIVE ;7/20/90  08:22 ;

LAFARA2 ;SLC/RAF- COBAS FARA II;8/1/94  06:45 ;

LAFUNC ;SLC/DLG - GENERIC FUNCTIONS USED BY LA ROUTINES ;7/20/90  08:28 ;

LAGEN  ;SLC/CJS- LAB AUTOMATED DATA ;7/20/90  08:28 ;

LAH1   ;SLC/RWF- TECHNICON H1 ;7/20/90  08:35 ;

LAH480 ;SLC/RWF- HEMATRAK 360, 480, 590 ;7/20/90  08:35 ;

LAH6K  ;SLC/RWF- DUPONT H6000 AUTOMATED DATA ;7/20/90  08:36 ;

LAH705 ;SLC/RWF- HITACHI 704/705 ;7/20/90  08:37 ;

LAH717D;SLC/DLG - HITATCHI 717 BUILD DOWNLOAD FILE. ;7/20/90  08:38 ;

LAH717H;SLC/DLG - HITACHI 717 WITH JT-717 PROTOCOL CONTROLLER ;7/20/90 09:10 ;

LAH717U;SLC/DLG- HITACHI 717 ROUTINE FOR AUTOMATED DATA ;7/20/90  09:10 ;

LAH737 ;SLC/RWF- HITACHI 737 ;7/20/90  09:11 ;

LAH747 ;SLC/FHS/RAF - HITACHI 747 ;8/15/92  15:41

LAHLOG ;SLC/RWF- TECHNICON HEMALOG D ;7/20/90  09:12 ;

LAHT1K ;SLC/DLG- HITACHI 736 WITH JT 1000  ;7/20/90  09:14 ;

LAHT1KD;SLC/DLG - HITATCHI 736 WITH JT1000 BUILD DOWNLOAD FILE.;8/16/90 10:31;

LAHTCCA;SLC/DLG- HITACHI 717 THRU CCA SYSTEM ;7/20/90  09:16 ;

LAHTCCAD;SLC/DLG - HITATCHI 717 THRU CCA SYSTEM BUILD DOWNLOAD FILE. ;7/20/90  09:17 ;

LAHTCCAH;SLC/DLG - HITACHI 717 THRU CCA SYSTEM PROTOCALL CONTROLLER  ;7/20/90  09:18 ;

LAHTRK ;SLC/RWF,CJS- HEMATRAK 590 DIFF COUNTER ;8/16/90  14:18 ;

LAHWATCH;SLC/RAF/DALISC/TNN - WATCH DATA IN ^LAH GLOBAL ;1/13/92  12:41

LAJOB  ;SLC/DCM- JOB AUTOMATED LAB ROUTINES ;4/27/89  09:41 ;

LAJOB1 ;SLC/DCM,RWF - STATUS OF AUTOMATED LAB ROUTINES ;7/11/89  10:29 ;

LAKDA  ;SLC/RWF- AM. MONITOR KDA ;7/20/90  09:23 ;

LAKDIFF;SLC/RWF- KEYBOARD DIFFERENTIAL COUNTER ;8/16/90  10:38 ;

LAKDIFF1;SLC/RWF,LL/RES- KEYBOARD DIFF PART 2 ; 7/14/87  08:02 ;

LAKDIFF2;SLC/RWF,LL/RES- RBC MORPHOLOGY ; 7/14/87  08:01 ;

LAKDIFF3;SLC/DLG- LAB ROUTINE DATA VERIFICATION BY WORKLIST OF KEYBOARD DIFFS ; 7/28/88  10:01 AM ;

LAKERM2;SLC/RWF/DLG - BUILD A KERMIT FILE TO SEND THRU LSI ;7/20/90  09:25 ;

LAKERM3;SLC/RWF/DLG - UNPACK KERMIT RECORDS VIA LSI ;7/20/90  09:26 ;

LAKERMIT;SLC/RWF/DLG - KERMIT PROTOCALL CONTROLLER THRU LSI ;7/20/90  09:24 ;

LAKOAG40;SLC/RWF- ORTHO KOAGULAB 40-A ;7/20/90  09:23 ;

LAKUR  ;SLC/RWF- KEYBOARD URINE COUNTER ;8/16/90  10:39 ;

LAKUR1 ;SLC/RWF - URINALYSIS Part 2 ; 9/19/87  18:36 ;

LAL13  ;SLC/RWF- PROCESS IL- 1303 DATA ;8/16/90  10:35 ;

LAL1306;SLC/IL- PROCESS IL- 1306 DATA ;8/16/90  10:36 ;

LAL1312;SLC/RWF- IL 1312 BLOOD GAS INSTRUMENT ;7/20/90  09:20 ;

LAL508 ;SLC/RWF,BUF/DCN - IL 508 ROUTINE ;7/20/90  09:21 ;

LAL943 ;SLC/RWF- IL 943 ;7/20/90  09:21 ;

LALBG3;SLC/RAF - IL BG3 Blood Gas Analyzer interface ;9/2/94 14:33 ;

LAMIAUT0;SLC/FHS -  MICRO AUTO INSTRUMENT PROGRAM VITEK ;7/20/90  09:31 ;

LAMIAUT1;SLC/FHS -  CONTINUE MICRO AUTO INSTRUMENT PROGRAN VITEK  ;7/23/90 11:06;

LAMIAUT2;SLC/FHS -  CONTINUE MICRO AUTO INSTRUMENT PROGRAM VITEK ;7/20/90 09:33 ;

LAMIAUT3;DLG/SLC -  MICRO DISPLAY ANTIBIOTICS FOR VERIFY ;7/20/90  09:32 ;

LAMIAUT4;SLC/FHS - EDIT OR VERIFY MICRO AUTO INSTRUMENTS; ;7/20/90  09:33

LAMIAUT5;DAL/FHS - DELETE MICRO AUTOMATED DATA UTILITY

LAMIAUT6;SLC/FHS - DISPLAY MICRO DRUGS IN ORDER ;7/20/90  09:34

LAMIAUT7;FHS/SLC - CREATE LOAD LIST FOR VITEK ;7/20/90  09:34

LAMIAUT8;FHS/SLC - ADD OR DELETE FROM VITEK LOAD LIST ;7/20/90  09:35

LAMICRA;SLC/DLG - VITEK AUTOINSTRUMENT LOAD OF SPECIAL CHARACTERS ;7/20/90 09:36;

LAMILL ;SLC/DLG - BUILD LOAD LIST FOR MICROSCAN ;7/20/90  09:36 ;

LAMIV00;SLC/DLG- PROCESS VITEK V VALUE FROM FILE  ;7/20/90  09:37 ;

LAMIV10;SLC/DLG - PROCESS VITEK BACILLUS AND UID CARDS ;7/20/90  09:37 ;

LAMIV11;SLC/DLG - PROCESS VITEK GPS &amp; YBC CARDS ;7/20/90  09:38 ;

LAMIV12;SLC/DLG - PROCESS VITEK GNS CARDS  ;7/20/90  09:38 ;

LAMIVT5;SLC/DLG/DAL/FHS - VITEK MICRO DATA  NEW FORMAT AMS 06.1;8/16/90  13:37 ;

LAMIVT6;SLC/DLG/DAL/FHS - VITEK MICRO DATA  ENCODED NEW FORMAT UNI AMS 06.1;8/16/90  13:37 ;

LAMIVTE6;SLC/DLG/FHS/DAL - VITEK MICRO DATA  ENCODED AMS 06.1 NEW FORMAT ;5/26/92

LAMIVTK;SLC/DLG - VITEK MICRO DATA  ;8/16/90  13:37 ;

LAMIVTK6;SLC/DLG - VITEK MICRO DATA  BCI R02.1 R02.2 ;12/23/91 ;

LAMIVTKC;SLC/DLG - VITEK PROTOCOL CONTROLLER ;7/20/90  09:40 ;

LAMIVTKD;SLC/RWF - VITEK BUILD DOWNLOAD FILE. ;7/18/89  11:51 ;

LAMIVTKU;SLC/DLG - VITEK MICRO DATA  ;8/16/90  13:36 ;

LAMLA1KC;SLC/DLG/FHS -  ELECTRA 900/900C/1000C ;03/25/93  15:41 ;

LAMLA7 ;SLC/RWF- MLA ELECTRA 700 ;7/20/90  09:42 ;

LAMODH ;SLC/RWF- MODULUS COMP-U-DIFF ;7/20/90  09:42 ;

LAMODU ;SLC/RWF- MODULUS UR-O-COMP ;7/20/90  09:43 ;

LAMODUT;SLC/DLG- MODULUS KEYPAD VETICAL FORMAT ;7/20/90  09:43 ;

LAMONARK;SLC/RWF- IL MONARK ;7/20/90  09:45 ;

LAMSA  ;SLC/DLG - MICROSCAN AND AUTOSCAN4 DATA ANALYZER  ;8/16/90  13:35 ;

LAMSA1 ;SLC/DLG - MICROSCAN PROCESS MIC/THERAPY RECORD ;3/7/91  09:47 ;

LAMSBLD;SLC/DLG - BUILD MICROSCAN MIC X-REF IN FILE 62.06 ;7/20/90  09:48 ;

LAMSD  ;SLC/DLG - MICROSCAN BUILD DOWNLOAD FILE ;7/20/90  09:48 ;

LAMSP  ;SLC/DLG - MICROSCAN PROTOCALL ROUTINE W/O ACK-NAK ;7/20/90  09:49 ;

LAMSPAN;SLC/DLG - MICROSCAN PROTOCALL ROUTINE W/ ACK-NAK  ;7/20/90  09:50 ;

LAMSTAT;SLC/RWF- MULTISTAT III ROUTINE ;7/20/90  09:50 ;

LANOVA ;SLC/RWF- NOVA 4+4 / 11+11 ;7/20/90  09:56 ;

LANOVST;SLC/DLG- NOVA STAT PROFILE ANALYSER ;7/20/90  09:56 ;

LANTEG ;ISC/XTSUMBLD KERNEL - Package checksum checker ;JAN 04, 1994@17:47:36

LANTEG0;ISC/XTSUMBLD KERNEL - Package checksum checker ;JAN 04, 1994@17:47:36

LAPARA ;SLC/RWF- PARALLEL ANALYZER ;7/20/90  09:57 ;

LAPARAP;SLC/RWF- PARALLEL - PRINTER PORT FORMAT ;7/20/90  09:57 ;

LAPER  ;SLC/DLG- PERSPECTIVE ;7/20/90  09:58 ;

LAPERD ;SLC/DLG AMERICAN MONITOR PERSPECTIVE BUILD DOWNLOAD FILE. ;7/20/90 09:58;

LAPFICH;AVAMC/REG- MICROFICH PATH REPORTS  ;7/20/90  09:59

LAPMAX ;SLC/RWF- PARAMAX  ;7/20/90  10:01 ;

LAPMAXD;SLC/DLG PARAMAX BUILD DOWNLOAD FILE. ;7/20/90  10:01 ;

LAPORTXX;SLC/DLG- AUTOMATED SINGLE INSTRUMENT LAB INTERFACE ;8/16/90  14:22 ;

LAPX    ;SLC/RWF - TEMPLATE ROUTINE FOR AUTOMATED DATA, this routine will not work until INTENTIONAL bugs are removed ;7/20/90  10:02 ;

LARA1K ;SLC/RWF- TECHNICON RA-1000 ;7/20/90  10:02 ;

LARA2K ;SLC/RWF-DCM FOR RA 2000 THRU PORT EXPANDER ;7/20/90  10:03 ;

LARAPMT;SLC/DLG- RAPIMAT URINE PAD ROUTINE ;7/20/90  10:04 ;

LARMK  ;SLC/FHS - SET UP REMARKS FOR AUTO-INSTRUMENTS  ;10/10/90 18:16

LAS550 ;SLC/RWF- COULTER S550,770 ;7/20/90  10:04 ;

LAS790 ;SLC/RWF- COULTER S790  ;7/20/90  10:05 ;

LASCT  ;SLC/RWF- COULTER S with COURT II ;7/20/90  10:05 ;

LASET  ;SLC/RWF- AUTO INSTRUMENTS SETUP VAR FOR DATA COLECTION ;2/19/91 12:03;

LASMA12;SLC/DLG,PORTLAND/JT,SLC/RWF- SMA 12/60 INTERFACE ;7/20/90  10:08 ;

LASMA2 ;SLC/RWF- SMA II/(GENERATION 2) SYSTEM ROUTINE ;7/20/90  10:08 ;

LASMA2C;SLC/RWF- SMA II/C SYSTEM ROUTINE ;7/20/90  10:09 ;

LASMAC4;SLC/RWF- SMAC RUN CONTROL FOR SMAC (LASMACA) ;7/20/90  10:10 ;

LASMACA;SLC/RWF- GETS DATA FROM SMAC ;8/16/90  11:03 ;

LASP120;SLC/RWF- VICKERS SP-120 INTERFACE FOR SMA 18/60 AUTOMATED DATA ;7/20/90  10:12 ;

LASPEC ;SLC/RWF- ABBOTT SPECTRUM VERSION M2.0 ;7/20/90  10:12 ;

LASTATUS;SLC/FHS - TO CHECK SYSTEM STATUS OF AUTO INSTRUMENT JOBS ;11/6/89 12:03

LASTRA ;SLC/RWF- ASTRA 4,6,8,8E,IDEAL,CX3 (NON-CALCULATING) ;8/16/90  13:53 ;

LASYS8K;SLC/DLG- SYSMEX 8000 ;7/20/90  10:13 ;

LASYSMEX;SLC/RWF- TOA  SYSMEX K-1000/E-2000/E-5000 ;7/20/90  10:14 ;

LATDX  ;SLC/RWF- ABBOTT TDX,PACKARD TDX ;7/20/90  10:16 ;

LATDX1 ;SLC/RWF- ABBOTT TDX WITH SPEC ID VERSION 10.1 ;10/25/90  14:31 ;

LATOA  ;SLC/RWF- TOA AUTO INSTRUMENT ;7/20/90  10:17 ;

LAWATCH;SLC/RWF/FHS - WATCH DATA IN ^LA GLOBAL ;8/8/89  11:36 ;

LAYRIS ;SLC/RWF- IRIS ;7/20/90  09:22 ;

**LA pre- and post- init routines**

LAIPOST ;SLC/FHS -  AUTO INSTRUMENTS POST INIT ;5/10/90  11:33

LAIPRE  ;DALISC/JRR - AUTO INSTRUMENTS PRE INIT ENVIRONMENT CHECK ; 3/14/94

### 37 OE/RR Routines

The following routines are namespaced LR but are actually part of the OE/RR package.

**OERR routines that are LAB namespaced**

LRX6   ;SLC/DCM - ENTRY POINTS TO MOVE LAB FILES TO 101 ;10/3/90  13:19 ;

LRX60  ;SLC/DCM - MOVE FILE 60 TO 101 ; 7/3/89  10:30 ;

LRX62P6;SLC/DCM - MOVE FILE 62.6 ENTRIES INTO 101 ;10/2/90  17:20 ;

LRX62P61;SLC/DCM - MOVE FILE 62.6 INTO 101 CONT. ;9/7/89  17:33 ;

LRX6PRO;SLC/DCM - MOVE LAB PROFILES INTO 101 CONT. ;11/26/90  16:10 ;

LRXO0  ; SLC/DCM - Process Lab actions

LRXO00 ; SLC/DCM - Lab Orders ;4/18/91  10:31

LRXO1  ; SLC/DCM - Lab Orders ;4/18/91  10:31

LRXO10 ; SLC/DCM - Process lab order from OE/RR ;5/20/91  07:10 ;

LRXO11 ; SLC/DCM - Setup order &amp; accession for OE/RR ;3/29/90  16:40 ;

LRXO1A ; SLC/DCM - Lab Orders cont.;4/18/91  10:31

LRXO2  ; SLC/DCM - Lab Order Cont.

LRXO3  ; SLC/DCM - Lab Order Cont.

LRXO4  ; SLC/DCM - Lab Order Cont. ;3/11/91  14:02

LRXO4A ; SLC/DCM - Lab Order Cont. ;3/11/91  14:02

LRXO5  ; SLC/DCM - Lab collection times ;1/17/92  11:52 ;

LRXO6  ; SLC/DCM - Comment Utility ; 3/31/88  3:54 PM ;

LRXO7  ; SLC/DCM - Lab collection samples ; 7/3/89  15:07 ;

LRXO8  ; SLC/DCM - Check max freq of lab orders ;8/30/89  10:09

LRXO9  ; SLC/DCM - Order Comments

LRXOS0 ; SLC/DCM - Order timing utility ;1/29/91  14:44

LRXOS1 ; SLC/DCM - Order cancel by patient movement ;7/17/90  12:17

LRXREF ;SLC/RWA - BUILD CROSS-REFERENCES FOR RE-INDEX ;7/9/92  01:26

LRXREF1;SLC/RWA - CONTINUE BUILD X-REF FOR RE-INDEX ;5/15/90  12:41

**OE/RR routines that are LAB namespaced, replaced with each new version of OE/RR.**

LRO       LRO    ;SLC/DCM - Being replaced ;1/10/91  16:0 ;

LRO1      LRO1   ;SLC/DCM - Being replaced ; 3/9/89  19:39 ;

LRO2      LRO2   ;SLC/DCM - Being replaced ;1/10/91  16:01 ;

LRO3      LRO3   ;SLC/DCM - Being replaced ; 7/3/89  15:07 ;

LRO4      LRO4   ;SLC/DCM - Being replaced ;1/31/91  08:46 ;

LRO5      LRO5   ;SLC/DCM - Being replaced ;1/10/91  16:01 ;

LRO6      LRO6   ;SLC/DCM - Being replaced ; 2/14/89  18:07 ;

LRO7      LRO7   ;SLC/DCM - Being replaced ;1/9/91  17:32 ;

LRO8      LRO8   ;SLC/DCM - Being replaced ;1/10/91  16:0 ;

LRORDST1;SLC/CJS,RWF - Being replaced ;3/29/90  16:40 ;

LROSX0 ;SLC/DCM - Being replaced ;1/29/91  14:44

LROSX1 ;SLC/DCM - Being replaced ;7/17/90  12:17

CALLABLE ROUTINES

#### Callable Routines

The following listings are drawn from the Forum DBA menu.

### 38 Supported References

This list is of the references approved by the DBA.

LISTING OF SUPPORTED REFERENCES BY PACKAGE     JUL 28,1994  15:17    PAGE 1

NAME

DBIA #     TYPE

--------------------------------------------------------------------------------

CUSTODIAL PACKAGE: LAB SERVICE

LAB(61.4,          10133      File

LAB(61.4,D0,0)

LAB(61.2,          10131      File

LAB(61.2,D0,0)

LAB(61.3,          10132      File

LAB(61.3,D0,0)

LAB(60,            10054      File

LAB(60,D0,0)

LAB(61.1,          10130      File

LAB(61.1,D0,0)

LAB(61.6,          10135      File

LAB(61.6,D0,0)

LAB(61.5,          10134      File

LAB(61.5,D0,0)

LAB(61,            10055      File

LAB(61,D0,0)

### 39 Entry Point References

This list is of the agreements between packages. Any restrictions on the use of the entry points are detailed in this report.

**LAB SERVICE Custodial DBI Agreements **

-------------------------------------------------------------------------------

NAME: DBIA240-B             ENTRY: 710

CUSTODIAL PACKAGE: LAB SERVICE                  Dallas

SUBSCRIBING PACKAGE: AUTOMATED MED INFO           Albany

USAGE: Private            APPROVED: APPROVED

STATUS: Active              EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE:                        ROOT:

DESCRIPTION:                        TYPE: Routine

Laboratory Package has given permission to AMIE to make the following

calls: Routine Calls:

CH^LRRP2

MI^LRRP2

PT^LRX    Current Agreement number 95 Per our phone conversation on

6/7/93.  No more setting of the ZTSK AND ZTQUEUED variables.  Call the

following entry points: D DT^LRX,EN^LRPARAM.  This will work for any

version of Lab.

ROUTINE: LRRP2

COMPONENT:  CH

VARIABLES:

COMPONENT:  MI

VARIABLES:

********************

NAME: DBIA240-C             ENTRY: 715

CUSTODIAL PACKAGE: LAB SERVICE                  Dallas

SUBSCRIBING PACKAGE: AUTOMATED MED INFO           Albany

USAGE: Private            APPROVED: APPROVED

STATUS: Active              EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE:                        ROOT:

DESCRIPTION:                        TYPE: Routine

Laboratory Package has given permission to AMIE to make the following

calls: Routine Calls:

PT^LRX    Current Agreement number 95 Per our phone conversation on 6/7/93.  No more setting of the ZTSK AND ZTQUEUED variables. `

}”\\\\ Call the following entry points: D DT^LRX,EN^LRPARAM.  This will work for any version of Lab.

ROUTINE: LRX

COMPONENT:  PT

VARIABLES:

COMPONENT:  DT

VARIABLES:

********************

NAME: DBIA240-D             ENTRY: 716

CUSTODIAL PACKAGE: LAB SERVICE                  Dallas

SUBSCRIBING PACKAGE: AUTOMATED MED INFO           Albany

USAGE: Private            APPROVED: APPROVED

STATUS: Active              EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE:                        ROOT:

DESCRIPTION:                        TYPE: Routine

Laboratory Package has given permission to AMIE to make the following calls: Per our phone conversation on 6/7/93. No more setting of the ZTSK AND ZTQUEUED variables.  Call the following entry points: D

DT^LRX,EN^LRPARAM.  This will work for any version of Lab.

ROUTINE: LRPARAM

COMPONENT:  EN

VARIABLES:

********************

NAME: DBIA95-B              ENTRY: 558

CUSTODIAL PACKAGE: LAB SERVICE                  Salt Lake City

SUBSCRIBING PACKAGE: COMPENSATON AND PE           Albany

USAGE: Private            APPROVED: APPROVED

STATUS: Active              EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE:                        ROOT:

DESCRIPTION:                        TYPE: Routine

Request an agreement with the lab developers for usage of the following:

variables:

Only those associated with the routines below

Routines from indicated entry points:

PT^LRX

ROUTINE: LRX

COMPONENT:  PT

VARIABLES:

********************

NAME: DBIA95-C              ENTRY: 559

CUSTODIAL PACKAGE:

LAB SERVICE                  Salt Lake City

SUBSCRIBING PACKAGE: COMPENSATON AND PE           Albany

USAGE: Private            APPROVED: APPROVED

STATUS: Active              EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE:                        ROOT:

DESCRIPTION:                        TYPE: Routine

Request an agreement with the lab developers for usage of the following:

variables:

Only those associated with the routines below

Routines from indicated entry points:

SWITCH^LRRP2

ROUTINE: LRRP2

COMPONENT:  SWITCH

VARIABLES:

********************

NAME: DBIA59-B              ENTRY: 520

CUSTODIAL PACKAGE: LAB SERVICE                  Salt Lake City

SUBSCRIBING PACKAGE: INTERIM MANAGEMENT           Birmingham

USAGE: Private            APPROVED: APPROVED

STATUS: Active              EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE:                        ROOT:

DESCRIPTION:                        TYPE: Routine

- ECT namspaced option runs routine ^LRUPACA

Enter ACTION: S DIC=68,DIC(0)="QEAM" D ^DIC K DIC I Y&gt;0 S LRAA=+Y,

LRAA(1)=$P(Y,U,2)

SEE DBIA59-A

ROUTINE: LRUPACA

********************

NAME: DBIA59-C              ENTRY: 521

CUSTODIAL PACKAGE: LAB SERVICE                  Salt Lake City

SUBSCRIBING PACKAGE: INTERIM MANAGEMENT           Birmingham

USAGE: Private            APPROVED: APPROVED

STATUS: Active              EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE:                        ROOT:

DESCRIPTION:                        TYPE: Routine

- ECT namespaced option runs routine ^LRCAPS.

- Refences file 68 Accession (read only)

2  DATE

.01 DATE

1 ACCESSION NUMBER

.01 LRDFN

11 TESTS

.01 TESTS

SEE DBIA59-A

ROUTINE: LRCAPS

********************

NAME: DBIA207               ENTRY: 207

CUSTODIAL PACKAGE: LAB SERVICE                  Dallas

SUBSCRIBING PACKAGE: SURGERY                      Birmingham

USAGE: Private            APPROVED: APPROVED

STATUS: Active              EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE:                        ROOT:

DESCRIPTION:                        TYPE: Routine

Surgery is granted a database integration agreement with Laboratory allowing Surgery to make a call to LRRP2 by executing %ZOSF("TEST"), then calling LRRP2.

ROUTINE: LRRP2

FILE LIST AND DESCRIPTIONS

File List and Descriptions

### 40 File List

The files listed below are Laboratory files that will be exported with Laboratory Version 5.2 software package:

UPDATE	DATA	MERGE OR

THE	COMES	OVERWRITE

DATA	WITH	SITE'S

FILE	DICTIONARY	FILE	DATA

-----------------------------------------------------------------------------

60	LABORATORY TEST	YES	YES	MERGE

61	TOPOGRAPHY FIELD	YES	NO

61.1	MORPHOLOGY FIELD	YES	NO

61.2	ETIOLOGY FIELD	YES	NO

61.3	FUNCTION FIELD	YES	NO

61.4	DISEASE FIELD	YES	NO

61.5	PROCEDURE FIELD	YES	NO

61.6	OCCUPATION FIELD	YES	NO

62	COLLECTION SAMPLE	YES	NO

62.05	URGENCY	YES	NO

62.06	ANTIMICROBIAL SUSCEPTIBILITY	YES	NO

62.07	EXECUTE CODE	YES	NO

62.1	DELTA CHECKS	YES	NO

62.2	LAB SECTION	YES	NO

62.3	LAB CONTROL NAME	YES	NO

62.4	AUTO INSTRUMENT	YES	NO

62.5	LAB DESCRIPTIONS	YES	NO

62.55	AGGLUTINATION STRENGTH	YES	NO

62.6	ACCESSION TEST GROUP	YES	NO

63	LAB DATA	YES	NO

63.9999	ARCHIVED LR DATA	YES	NO

64	WKLD CODE	YES	YES	OVERWRITE

64.03	WKLD LOG FILE	YES	NO

64.05	NON WORKLOAD PROCEDURES	YES	YES	OVERWRITE

64.1	WKLD DATA	YES	NO

64.19999	ARCHIVED WKLD DATA	YES	NO

64.2	WKLD SUFFIX CODES	YES	YES	OVERWRITE

64.21	WKLD CODE LAB SECT	YES	YES	OVERWRITE

64.22	WKLD ITEM FOR COUNT	YES	YES	OVERWRITE

64.3	WKLD INSTRUMENT MANUFACTURER	YES	YES	OVERWRITE

64.5	LAB REPORTS	YES	NO

64.6	INTERIM REPORTS	YES	NO

64.7	CUMULATIVE	YES	NO

65	BLOOD INVENTORY	YES	NO

65.4	BLOOD BANK UTILITY	YES	NO

65.5	BLOOD DONOR	YES	NO

65.9	LAB LETTER	YES	NO

65.9999	ARCHIVED BLOOD INVENTORY	NO	NO

66	BLOOD PRODUCT	YES	NO

66.2	BLOOD BANK VALIDATION	YES	NO	OVERWRITE

66.3	MASTER LABORATORY TEST FILE	YES	NO

66.5	OPERATION (MSBOS)	YES	NO

66.9	BLOOD COMPONENT	YES	NO

67	REFERRAL PATIENT	YES	NO

67.1	RESEARCH	YES	NO

67.2	STERILIZER	YES	NO

67.3	ENVIRONMENTAL	YES	NO

67.4	NON PATIENT WORKLOAD	YES	NO

67.9	LAB MONTHLY WORKLOADS	YES	NO

67.99999	ARCHIVED LAB MONTHLY WORKLOADS	YES	NO

68	ACCESSION	YES	NO

68.2	LOAD/WORK LIST	YES	NO

68.4	WORKLIST HEADINGS	YES	NO

68.45	GROUP USER MANUAL	YES	NO

69	LAB ORDER ENTRY	YES	NO

69.1	COLLECTION LIST	YES	NO

69.2	LAB SECTION PRINT	YES	NO

69.71	LR CPRS PARAMETERS	YES	YES	OVERWRITE

69.9	LABORATORY SITE	YES	NO

69.91	LR ROUTINE INTEGRITY CHECKER	YES	YES	OVERWRITE

95	LAB JOURNAL	YES	NO

### 41 Brief File Descriptions

The following is a brief description of the Laboratory files. For a complete description of the files and fields refer to the file section of the Laboratory Planning and Implementation Guide V. 5.2. For a printout of the files and fields use the List File Attributes [DILIST] option of VA FileManager.

**60 LABORATORY TEST**

This is the file that holds the information about individual Laboratory test.

**61 TOPOGRAPHY FIELD**

This is the TOPOGRAPHY FIELD file of SNOMED.

**61.1 MORPHOLOGY FIELD**

This is the MORPHOLOGY FIELD file of SNOMED.

**61.2 ETIOLOGY FIELD**

This is the ETIOLOGY FIELD file of SNOMED.

**61.3 FUNCTION FIELD**

This is the FUNCTION FIELD file of SNOMED.

**61.4 DISEASE FIELD**

This is the DISEASE FIELD file of SNOMED.

**61.5 PROCEDURE FIELD**

This is the PROCEDURE FIELD file of SNOMED.

**61.6 OCCUPATION FIELD**

This is the OCCUPATION FIELD file of SNOMED.

**62 COLLECTION SAMPLE**

Collection samples for laboratory specimens.

**62.05 URGENCY**

This file contains the defined urgencies.

**62.06 ANTIMICROBIAL SUSCEPTIBILITY**

This file is used by each laboratory to define specific information about the types of antibacterial antibiotics your laboratory uses.

**62.07 EXECUTE CODE**

The execute code file is used to store a variety of program instructions that are used in various programs in the Laboratory package.

**62.1 DELTA CHECKS**

The DELTA CHECKS file contains entries whose use is optional. They are entered in the LABORATORY TEST file (#60) under the site/specimen for the Type of delta check field.

**62.2 LAB SECTION**

This file defines the functional laboratory areas. Each area may have multiple accession areas. Entries may be added, but supplied entries should not be modified or deleted.

**62.3 LAB CONTROL NAME**

This file contains the definition of each of the laboratory controls used as part of the laboratory’s quality control program.

**62.4 AUTO INSTRUMENT**

This is the master file controlling how the Laboratory package interprets the running of the instruments interfaced to the CORE system.

**62.5 LAB DESCRIPTIONS**

This file is basically a dictionary of abbreviated codes or notations which are used in the laboratory repeatedly. Each one of the canned codes will expand to a full length message whenever the code is typed in at a “Select COMMENT:” prompt.

**62.55 AGGLUTINATION STRENGTH**

List of all strengths of reactions.

**62.6 ACCESSION TEST GROUP**

This file is used to setup Accession Test Groups (menus for accessioning tests).

**63 LAB DATA**

Patient’s  verified laboratory data.

**63.9999 ARCHIVED LR DATA**

This file is where patient lab data are stored during the archive process. It has the same data definitions as the Subfile #63.04 in LAB DATA file (#63). This file requires no editing by the user.

**64 WKLD CODE**

This file contains the list of WKLD Codes, which are used to compile Laboratory workload statistics. This file is exported with data from the most current instrument listings.

**64.03 WKLD LOG**

This file contains an entry for each WKLD related activity.

**64.05 WKLD NON WORKLOAD PROCEDURES**

Non workload activities Procedure List not to be added to weighted workload.

**64.1 WORKLOAD WKLD DATA**

This file contains the Laboratory workload data.

**64.19999 ARCHIVED WORKLOAD WKLD DATA**

This file contains Laboratory archived workload data.

**64.2 WKLD SUFFIX CODES**

This file contains a listing of National approved Workload Suffix codes.

**64.21 WKLD CODE LAB SECT**

This file contains the lab section to be used. This field is not the lab section which is used at the local site.

**64.22 WKLD ITEM FOR COUNT**

This file contains all of the approved item description used for counting Workload data.

**64.3 WKLD INSTRUMENT MANUFACTURER**

This file contains an approved list of Venders/Manufacturers of Laboratory equipment of test reagents.

**64.5 LAB REPORTS**

This file contains the design for the output format for the cumulative report and the supervisor’s reports.

**64.6 INTERIM REPORTS**

This file is used to define whether or not your site will be generating interim reports of patient lab values and to what locations these reports will be sent or routed.

**64.7 CUMULATIVE**

This file stores temporary pages of the cumulative report. The data in this file is maintained by the cumulative routines.

**65 BLOOD INVENTORY**

Units of various blood components.

**65.4 BLOOD BANK UTILITY**

This file contains donor affiliation groups, collection sites, items related to donor history, and transfusion reaction types.

**65.5 BLOOD DONOR**

List of blood donors with demographic, collection, and test data and components prepared from each collection.

**65.9 LAB LETTER**

This file stores lab consultations and blood donor letters.

**65.9999 ARCHIVED BLOOD INVENTORY**

This is the Archived file for the various blood components.

**66 BLOOD PRODUCT**

Blood products and reagents for blood banks and transfusion services.

**66.2 BLOOD BANK VALIDATION**

This file provides a mechanism for documenting the mandated validation of the Blood Bank software documentation.

**66.3 MASTER LABORATORY TEST FILE**

This file contains the codes and information that is to be associated to the respective laboratory test/specimen combinations.

**66.5 OPERATION (MSBOS)**

Contains operations/procedures with identified maximum Surgical Blood Order Schedules (MSBOS).

**66.9 BLOOD COMPONENT**

This file is used as a pick list of blood components available to be ordered by users needing to make a selection from another DHCP package. This file is locally edited by the LIM.

**67 REFERRAL PATIENT**

This file defines the patients demographic information for referral patients for whom test values  will be entered into the system.

**67.1 RESEARCH**

This file contains the names of research entities (i.e., animals and tissues, etc.)

**67.2 STERILIZER**

This file is used for names of sterilizers in the hospital.

**67.3 ENVIRONMENTAL**

This file is used by laboratory to enter names for environmental cultures or cultures of other inanimate entities.

**67.4 NON PATIENT WORKLOAD**

This file will be developed in later version to support non workload functions (i.e., TQI, QC).

**67.9 LAB MONTHLY WORKLOADS**

This file is used to collect workload data in preparation for transmission to the National Data Base Center.

**67.99999 ARCHIVED LAB MONTHLY WORKLOADS**

This field contains archived LAB MONTHLY WORKLOADS file data.

**68 ACCESSION**

This file contains entries which represent the functional subdivisions or departments of the laboratory, referred to by the Laboratory package software as accession areas.

**68.2 LOAD/WORK LIST**

This file contains the information needed to define each load or work list used to organize the workload in the laboratory.

**68.4 WORKLIST HEADINGS**

This file allows the lab to customize the short accession list.

**68.45 GROUP USER MANUAL**

This file is for future use.

**69 LAB ORDER ENTRY**

This file controls the orderly sequence of lab test ordering.

**69.1 COLLECTION LIST**

This contains the lab collection list entries.

**69.2 LAB SECTION PRINT**

This file used to hold print headers for anatomic path reports and as a temporary holding file for pathology cumulative, incomplete and complete reports. It is also used for Blood Bank Module special report format.

**69.71 LR CPRS PARAMETERS**

This file was added to support of the VistA Lab Enhancement (VLE) Anatomic Pathology order dialog enhancements in LR*5.2*462.

**69.9 LABORATORY SITE**

This file holds specific information which defines certain site parameters relating to the actual functioning of your laboratory.

**69.91 LR ROUTINE INTEGRITY CHECKER**

This file contains routine size (^%ZOSF(“size”)) and routine bit size (^LRINTEG) for exported lab packages by version number.

**95 LAB JOURNAL**

This file contains medical journals which provides references for various Bacteriology articles

EXPORTED OPTIONS

Exported Options

This section provides a list of exported options in the Laboratory package. It also include the distribution of menus to users and note any restrictions on menu distribution.

### 42 Laboratory Options List

OPTION LIST                                    AUG 21,1994  14:48    PAGE 1

MENU TEXT                                      NAME

------------------------------------------------------------------------------

Check the lab interface                        LA 1103

AP Microfiche Archive                          LA AP FICHE

Set instrument to run by Accession             LA AUTO ACC

Set instrument to run by load list             LA AUTO LLIST

Direct Connect Auto-Instrument  Start          LA DIR JOB

Download a load list to an Instrument.         LA DOWN

Lab Error Trap Listing                         LA ERR PRINT

Lab interface menu                             LA INTERFACE

Restart processing of instrument data          LA JOB

Keypad differential for CRT's                  LA KB DIFF

Test the interface                             LA LAB TEST

Change instrument run mode.                    LA LRLL/AC SWITCH

Automated Microbiology Menu                    LA MI MENU

MicroScan Load Worklist (Build)                LA MI MICROSCAN L/W BUILD

Load Vitek Special Characters                  LA MI SPECIAL CHARACTER LOAD Verify Micro Auto Data                         LA MI VERIFY AUTO

Vitek Load Worklist (Build)                    LA MI VITEK L/W BUILD

Watch the data in the LA global.               LA WATCH LAB                                            Edit controls added to the accessions each day LR ACC CONTROLS

Accession order then immediately enter data    LR ACC THEN DATA

Clear data from the LAR global                 LR ARCHIVE CLEAR

Find patient's archived data                   LR ARCHIVE DATA

Archive lab data                               LR ARCHIVE MENU

Convert archived data to use New Person file   LR ARCHIVE NP CONVERSION

Purge data found in the Search option          LR ARCHIVE PURGE

Read data from off-line media                  LR ARCHIVE READ MEDIA

Restore archived data to LR global             LR ARCHIVE RESTORE

Search for lab data to archive                 LR ARCHIVE SEARCH

Write data to off-line media                   LR ARCHIVE WRITE MEDIA

Download Format for Intermec Printer           LR BARCODE FORMAT LOAD

Lab test turnaround time                       LR CAPTT

Count accessioned tests                        LR COUNT ACC TESTS

Process data in lab menu                       LR DO!

Phlebotomy menu                                LR GET

Health Department report                       LR HEALTH DEPT

Accessioning menu                              LR IN

Infection warning edit                         LR INF WARN

LAB ROUTINE INTEGRITY MENU                     LR INTEGRITY

Load Integrity File                            LR INTEGRITY LOAD

Loop thru LR INTEGRITY                         LR INTEGRITY LOOP

Check a single routine size                    LR INTEGRITY SINGLE

LIM workload menu                              LR LIM/WKLD MENU

Lookup accession                               LR LOOKUP ACCESSION

Results menu                                   LR OUT

Misc. Processing Menu                          LR PROCESS, MISC

Rollover Accession (Manual)                    LR ROLLOVER

Summary list (supervisors')                    LR SUP SUMMARY

Supervisor workload menu                       LR SUPER/WKLD MENU

Lab statistics menu                            LR WKLD

Review accession workload                      LR WKLD AUDIT

WKLD code list by code                         LR WKLD CODE BY CODE

WKLD code list by name                         LR WKLD CODE BY NAME

Edit workload comments                         LR WKLD COMMENTS

PHASE 1: Move data from 64.1 to 67.9.          LR WKLD LMIP 1

Recompile Phase 1 LMIP Data.                   LR WKLD LMIP 1 REPEAT

PHASE 2: Collect data for transmit to NDB.     LR WKLD LMIP 2

PHASE 3: Print of data to be sent to NDB.      LR WKLD LMIP 3

PHASE 4: Create E-mail message for NDB.        LR WKLD LMIP 4

PHASE 5: Purge monthly WKLD data from 67.9.    LR WKLD LMIP 5

Manually compile WKLD and workload counts      LR WKLD MANUAL

Workload manual input                          LR WKLD MANUAL INPUT

Requesting center dictionary                   LR WKLD REQUEST

Lab section list by code                       LR WKLD SECTION BY CODE

Lab section list by name                       LR WKLD SECTION BY NAME

Service dictionary                             LR WKLD SERVICE

Turn on site workload statistics               LR WKLD STATS ON

Turn on workload stats for accession area      LR WKLD STATS ON ACC AREA

Std/QC/Reps Manual Workload count              LR WKLD STD/QC/REPS

Lab subsection by Lab section                  LR WKLD SUB BY SECTION

Lab subsection list                            LR WKLD SUBSECTION

Test dictionary                                LR WKLD TEST DICT

WKLD statistics reports                        LR WKLD2

File listings                                  LR WKLD3

LMIP Reports/Data Collection                   LR WKLD4

CPRS LAB TEST (#60) EDIT                       LR7OAP CPRS 60 EDIT

Print Laboratory Test CPRS Screen              LR7OAP CPRS 60 PRINT

CPRS AP Dialog Menu                            LR7OAP CPRS DIALOG MENU

CPRS Dialog Print (#69.71)                     LR7OAP CPRS DIALOG PRINT

Cumulative menu                                LRAC

Reprint a permanent page from cumulative       LRAC 1 PAGE

Mumps A index of the LAB REPORTS file          LRAC A

Mumps A, AC, &amp; AR indexes of the LAB REPORTS   LRAC A AC AR

Mumps AC index of the LAB REPORTS file         LRAC AC

Mumps AR index of the LAB REPORTS file         LRAC AR

Diagnostic routine for Lab Reports file (64.5) LRAC DIAG

Patient Lab Discharge Summary (Manual)         LRAC DISCHARGE

Force cumulative data to Permanent Page        LRAC FORCE

Print a full patient summary                   LRAC FULL PATIENT SUMMARY Initialize LAC global &amp; X references           LRAC INITIALIZE

List of patients by location for cumulative

report                                        LRAC LIST

Reprint cumulative on a given location         LRAC LOC

Reprint cumulative from location to location   LRAC LOC-LOC

Manual queuing of cumulative                   LRAC MANUAL

Manual Queuing of Fileroom Cum                 LRAC MANUAL FILEROON CUM Reprint cumulative on a given patient          LRAC PT

Purge the Cumulative file                      LRAC PURGE

Cumulative device status                       LRAC STATUS

Re-cross-reference indexes in LAB REPORTS file LRAC XREF

Long form accession list                       LRACC1

Short accession list                           LRACC2

Work sheet Accession list                      LRACC3

Work sheet of all unverified accessions for

a date                                        LRACC4

Supervisor's report                            LRACS MANUAL

Add tests to a given accession.                LRADD TO ACC

Add tests to an already existing order number  LRADD TO ORDER

Lab add test(s) to an existing order           LRADDTST

Anatomic pathology                             LRAP

Add patient(s) to report print queue           LRAP ADD

Delete report print queue                      LRAP DELETE

Print all reports on queue                     LRAP PRINT ALL ON QUEUE

Print single report only                       LRAP PRINT SINGLE

Sum of accessions by date, anat path           LRAPA

AFIP registries                                LRAPAFIP

Alphabetical autopsy list                      LRAPAUA

Data entry for autopsies                       LRAPAUDA

Autopsy protocol &amp; ICD9CM coding               LRAPAUDAA

Autopsy protocol &amp; SNOMED coding               LRAPAUDAB

Autopsy protocol                               LRAPAUDAP

Special studies, autopsy                       LRAPAUDAS

Final autopsy diagnoses date                   LRAPAUFAD

Path cases by resident, tech, senior or

clinician                                     LRAPAUL

Accession counts by senior pathologist         LRAPAULC

Autopsy administrative reports                 LRAPAUP

Provisional anatomic diagnoses                 LRAPAUPAD

Autopsy protocol/supplementary report          LRAPAUPT

Autopsy data review                            LRAPAURV

Autopsy supplementary report                   LRAPAUSR

Autopsy status list                            LRAPAUSTATUS

Print log book                                 LRAPBK

Anatomic pathology topography counts           LRAPC

Coding, anat path                              LRAPCODE

Display cytopath reports for a patient         LRAPCYCUM

% Pos, Atyp, Dysp, Neg, Susp, Unsat cytopath   LRAPCYPCT

Print cytopathology report for a patient       LRAPCYSGL

Data entry, anat path                          LRAPD

Delete anat path descriptions by date          LRAPDAR

Enter/edit lab description file                LRAPDES

Delete free text specimen entries              LRAPDFS

Clinical Hx/Gross Description/FS               LRAPDGD

FS/Gross/Micro/Dx/ICD9CM Coding                LRAPDGI

FS/Gross/Micro/Dx                              LRAPDGM

FS/Gross/Micro/Dx/SNOMED Coding                LRAPDGS

Disease    (SNOMED) enter/edit                 LRAPDIS

Disease    (SNOMED) reference print            LRAPDP

Prisoner of war veterans                       LRAPDPT

Disease    (SNOMED) reference                  LRAPDR

Supplementary Report, Anat Path                LRAPDSR

Spec Studies-EM;Immuno;Consult;Pic, Anat Path  LRAPDSS

Edit/modify data, anat path                    LRAPE

Edit log-in &amp; clinical hx, anat path           LRAPED

Edit anat path comments                        LRAPEDC

Display EM reports for a patient               LRAPEMCUM

Print electron microscopy report for a patient LRAPEMSGL

Etiology   (SNOMED) reference print            LRAPEP

Etiology   (SNOMED) reference                  LRAPER

Etiology   (SNOMED) enter/edit                 LRAPETI

Print final path reports by accession #        LRAPFICH

Function   (SNOMED) reference print            LRAPFP

Function   (SNOMED) reference                  LRAPFR

Function   (SNOMED) enter/edit                 LRAPFUN

Histopathology Worksheet                       LRAPH

Edit pathology parameters                      LRAPHDR

Inquiries, anat path                           LRAPI

ICD9CM coding, anat path                       LRAPICD

Incomplete reports, anat path                  LRAPINC

Delete accession #, anat path                  LRAPKILL

Log-in menu, anat path                         LRAPL

Anatomic pathology labels                      LRAPLBL

Log-in, anat path                              LRAPLG

Medical journal file edit                      LRAPLIB

Anat path slide labels                         LRAPLM

Anat path specimen labels                      LRAPLS

Modify anat path gross/micro/dx/frozen section LRAPM

Clinician options, anat path                   LRAPMD

Print path modifications                       LRAPMOD

Morphology (SNOMED) enter/edit                 LRAPMOR

Morphology (SNOMED) reference print            LRAPMP

Morphology (SNOMED) reference                  LRAPMR

Move anatomic path accession                   LRAPMV

Occupation (SNOMED) enter/edit                 LRAPOCC

Enter old anat path records                    LRAPOLD

Occupation (SNOMED) reference print            LRAPOP

Occupation (SNOMED) reference                  LRAPOR

Print, anat path                               LRAPP

Display final path reports by accession #      LRAPPA

Anat path accession list by date               LRAPPAD

Anat path accession list by number             LRAPPAN

Anat path accession reports                    LRAPPAR

Entries by dates,patient &amp; accession #         LRAPPF

Persian gulf veterans                          LRAPPG

Procedure  (SNOMED) reference print            LRAPPP

Procedure  (SNOMED) reference                  LRAPPR

Procedure  (SNOMED) enter/edit                 LRAPPRO

List pathology reports in print queue          LRAPQ

AP quality assurance                           LRAPQA

Cum path summaries for quality assurance       LRAPQAC

QA codes entry/edit                            LRAPQACD

AP consultation searches and reports           LRAPQACN

Delete TC and QA codes                         LRAPQADEL

Frozen section, surgical path correlation      LRAPQAFS

Print path micro modifications                 LRAPQAM

Malignancy review                              LRAPQAMR

10% random case review, surg path              LRAPQAR

Edit QA site parameters                        LRAPQASP

Tissue committee review cases                  LRAPQAT

QA outcome review cases                        LRAPQOR

Verify/release reports, anat path              LRAPR

SNOMED field references                        LRAPREF

Pathology reports for a patient                LRAPRPT

Supplementary report release, anat path        LRAPRS

Accession list with stains                     LRAPSA

DISEASE code search, SNOMED                    LRAPSD

ETIOLOGY code search, SNOMED                   LRAPSE

Search options, anat path                      LRAPSEARCH

MULTIAXIAL code search, SNOMED                 LRAPSEM

FUNCTION code search, SNOMED                   LRAPSF

Print a pathology report for a patient         LRAPSGL

ICD9CM code search                             LRAPSI

MORPHOLOGY code search, SNOMED                 LRAPSM

Enter/edit items in a SNOMED field             LRAPSNOMEDIT

PROCEDURE code search, SNOMED                  LRAPSP

Display surg path reports for a patient        LRAPSPCUM

Blocks, Stains, Procedures, anat path          LRAPSPDAT

Print surgical pathology report for a patient  LRAPSPSGL

Enter/edit SNOMED file references              LRAPSRE

Print references for a SNOMED entry            LRAPSRP

Display stains/blocks for a patient            LRAPST

Supervisor, anat path                          LRAPSUPER

Cum path data summaries                        LRAPT

Topography (SNOMED) enter/edit                 LRAPTOP

Topography (SNOMED) reference print            LRAPTP

Topography (SNOMED) reference                  LRAPTR

Anatomic pathology turnaround time             LRAPTT

List of unverified pathology reports           LRAPV

Verify/release menu, anat path                 LRAPVR

Workload, anat path                            LRAPW

EM scanning and photo workload                 LRAPWE

Cytopathology screening workload               LRAPWR

Surg path gross assistance workload            LRAPWRSP

SNOMED coding, anat path                       LRAPX

Autopsy pathology                              LRAU

Data entry, Autopsy Path                       LRAUDA

Autopsy protocol &amp; ICD9CM coding               LRAUDAA

Autopsy protocol &amp; SNOMED coding               LRAUDAB

SNOMED coding, Autopsy Path                    LRAUDAC

ICD9CM coding, Autopsy Path                    LRAUDAI

Autopsy protocol                               LRAUDAP

Delete autopsy protocols by date               LRAUDAR

Special studies, Autopsy                       LRAUDAS

Final Autopsy Diagnoses Date                   LRAUFAD

Log-in, Autopsy path                           LRAULG

Autopsy Slide Labels (generic)                 LRAUMLK

Print option, Autopsy path                     LRAUP

Blood bank                                     LRBL

Blood Bank Administrative Data                 LRBLA

Crossmatch/Transfusions by Specialty/Physician LRBLAA

Print data change audits                       LRBLAD

Remove data change audits                      LRBLAR

Inventory ABO/Rh re-check counts               LRBLC

Blood bank consultation reports                LRBLCN

Donor                                          LRBLD

Donor collection/deferral edit                 LRBLDA

Apheresis donor list                           LRBLDAP

Acknowledge donor award by deletion            LRBLDAWARD

Donor collection/processing                    LRBLDC

Collection disposition report                  LRBLDCD

Collection disposition/component preparation   LRBLDCP

Component preparation report                   LRBLDCR

Cumulative donations and awards                LRBLDCU

Edit donor consent                             LRBLDCX

Donor demographics                             LRBLDD

Gallon donor report                            LRBLDDA

ABO/Rh testing of donor units                  LRBLDDAT

Donor unit testing worklist                    LRBLDDAW

Donor deferral report                          LRBLDDR

Blood donor group/type edit                    LRBLDEDIT

Emergency donor report                         LRBLDEDR

Permanent deferral/special comments            LRBLDEF

Print ex-donors                                LRBLDEX

First time blood donors                        LRBLDFD

Group affiliation report                       LRBLDGA

Group donation report                          LRBLDGDR

Remove ex-donors                               LRBLDK

Donor lists/labels/letters                     LRBLDL

Donor registration                             LRBLDLG

Enter/edit donor letters                       LRBLDLT

Mobile (Collection Site) report                LRBLDMC

Donor month/holiday recall list                LRBLDMR

Old blood donor records                        LRBLDO

Patient credits from blood donations           LRBLDPCR

Permanent donor deferral report                LRBLDPD

Donor phenotyping                              LRBLDPH

List of donors by last attempt date            LRBLDPL

Blood product rejection report                 LRBLDPRR

Donor history, physical and consent form       LRBLDR

Blood donor recruitment reports                LRBLDRPTS

Test review/Component labeling/release         LRBLDRR

Donor scheduling report                        LRBLDSC

Donor short draw report                        LRBLDSD

Donor summary reports                          LRBLDSR

Lab tests(not ABO/Rh) on donor units           LRBLDT

Abnormal donor tests                           LRBLDTA

Donor unit testing prooflist                   LRBLDTR

Donor unit supplemental testing prooflist      LRBLDTRS

Donor blood testing/review/release             LRBLDU

Donor unit ABO/Rh recheck                      LRBLDUC

Edit blood bank files                          LRBLEF

Inventory                                      LRBLI

CMV Antibody Status Report                     LRBLICV

Disposition -not transfused                    LRBLIDN

Disposition -relocation                        LRBLIDR

Disposition-not transfused                     LRBLIDU

Blood bank inventory integrity report          LRBLII

Unit CAUTION tag labels                        LRBLILA

Log-in regular (invoices)                      LRBLILR

Enter blood inventory typing charges           LRBLILS

Phenotyped units available                     LRBLIPH

Single unit information- display               LRBLIPSD

Single unit information- print                 LRBLIPSP

Transfusion reactions report                   LRBLIPTR

Unit issue book entries                        LRBLIRB

Blood inventory status reports                 LRBLIS

Shipping invoices for blood components         LRBLISH

Transfusion data report                        LRBLITR

Transfusions by treating specialty/physician   LRBLITS

Blood inventory transaction reports            LRBLITX

Unit ABO/Rh confirmation                       LRBLIUC

Unit phenotyping                               LRBLIUP

Units release to stock (cancel) by patient     LRBLIUR

Blood utilization &amp; summary reports            LRBLIUS

Inventory ABO/Rh testing worksheet             LRBLIW

Units on Xmatch by date/time xmatched          LRBLIX

Autologous disposition report                  LRBLJB

Edit pooled blood product                      LRBLJM

Transfused RBC for treating specialty          LRBLJUT

Blood bank patient                             LRBLP

Add BB patient(s) to report queue              LRBLP ADD

Delete BB report print queue                   LRBLP DELETE

Print all BB patient reports on print queue    LRBLP PRINT ALL ON QUEUE

Print single BB patient report                 LRBLP PRINT SINGLE

Antibodies by patient                          LRBLPAB

Patient accession list                         LRBLPAL

Blood bank tests report                        LRBLPBR

Request/select/xmatch blood components         LRBLPC

Patient transfusions &amp; hematology results      LRBLPCH

Blood component requests                       LRBLPCS

Pediatric unit preparation                     LRBLPED

Patient ABO/Rh edit                            LRBLPEDIT

Previous records                               LRBLPER

Enter test data                                LRBLPET

Patient Medication List                        LRBLPH

Select units for patients                      LRBLPIC

Prolonged transfusion times                    LRBLPIT

Specimen log-in                                LRBLPLOGIN

File 81 conversion                             LRBLPOST

Patient antibody report (short list)           LRBLPR

Patient antibody report (long-list)            LRBLPRA

Inappropriate transfusion requests report      LRBLPRIT

Special instructions                           LRBLPSI

Blood transfusion results                      LRBLPT

Unknown unit transfusion reaction              LRBLPTXR

Enter crossmatch results                       LRBLPX

Inquiries                                      LRBLQ

Patient blood bank record                      LRBLQDR

Units assigned/components requested            LRBLQPR

Single donor information                       LRBLQSD

Single donor demographic information           LRBLQSDD

Single unit status                             LRBLQST

Single unit (display/print) information        LRBLQSU

Reports                                        LRBLR

Crossmatch:Transfusion report                  LRBLRCT

Supplier invoices (inventory)                  LRBLRIN

Special typing charges (inventory)             LRBLRIS

Supplier transactions (inventory)              LRBLRIT

Test counts by location                        LRBLRTC

Units available (indate/no disposition)        LRBLRUA

Print units with final disposition             LRBLRUF

Units with no disposition                      LRBLRUN

Blood bank workload reports                    LRBLRWK

Supervisor                                     LRBLS

Blood donor edit options                       LRBLSD

Delete a user's patient list                   LRBLSDPL

Edit blood product file                        LRBLSEB

Edit unit - patient fields                     LRBLSEC

Edit unit disposition fields                   LRBLSED

Free autologous/directed donor units           LRBLSEE

Edit blood bank descriptions file              LRBLSEF

Edit donor history questions                   LRBLSEH

Edit unit log-in                               LRBLSEL

Remove units with final disposition            LRBLSER

Tests for inclusion in transfusion report      LRBLSET

Edit blood bank utility file                   LRBLSEU

Edit number of lines in a label                LRBLSF

Blood bank inventory edit options              LRBLSI

Edit lab letter file                           LRBLSLL

Maximum surgical blood order edit              LRBLSMS

Edit Corresponding Antigen/Antibody            LRBLSNO

Blood bank patient edit options                LRBLSP

Edit previous transfusion record               LRBLSPP

Remove inappropriate transfusion requests      LRBLSRI

Blood component request edit                   LRBLSRQ

Edit blood bank site parameters                LRBLSSP

Summary and deletion reports                   LRBLSSR

Tests for display on patient look-up           LRBLST

Blood bank workload                            LRBLSW

Transfusion reaction count                     LRBLTA

Test worklist                                  LRBLTTW

Tests for transfusion follow-up                LRBLTX

Transfusion follow-up tests                    LRBLTXA

Blood bank validation documentation            LRBLVAL

Validation documentation                       LRBLVALI

Print blood bank validation                    LRBLVALP

Ward                                           LRBLW

Add a new WKLD code to file                    LRCAP CODE ADD

RCS-CDR/LMIP REPORT                            LRCAPAM5

Workload code list                             LRCAPD

WKLD log file download                         LRCAPDL

Etiology WKLD Codes (Force)                    LRCAPF

Workload Statistics by Major Section           LRCAPMA

Workload cost report by major section          LRCAPML

Workload Report                                LRCAPR1

Treating Specialty Workload Report             LRCAPTS

Delete entire order or individual tests        LRCENDEL

Review by order number                         LRCENLKUP

Check files for inconsistencies                LRCHKFILES

Check patient and lab data cross pointers      LRCKPTR

Audit of deleted/edited comments               LRDCOM

Edit atomic tests                              LRDIEATOMIC

Edit cosmic tests                              LRDIECOSMIC

Graph results                                  LRDIST

Ward collection summary for lab orders         LRDRAW

Enter/verify/modify data (manual)              LRENTER

Test description information                   LREV

Bypass normal data entry                       LRFAST

Fast Bypass Data Entry/Verify                  LRFASTS

General report for selected tests              LRGEN

Group unverified review (EA, EL, EW)           LRGP

Group verify (EA, EL, EW)                      LRGV

Group data review (verified &amp; EM)              LRGVP

Information-help menu                          LRHELP

Clear instrument/worklist data                 LRINSTCLR

Reprint order accession label(s)               LRLABXOL

Reprint accession label(s)                     LRLABXT

Lab liaison menu                               LRLIAISON

Summary list (extended supervisors')           LRLISTE

Build a load/work list                         LRLL

Edit control placement on load/work list       LRLL CONTROLS

Set new "starting sequence number"             LRLL NEW 1ST SEQUENCE #

Change Load/Work list type.                    LRLL TYPE

Unload Load/Work List                          LRLLCT

Edit the default parameters Load/Work list.    LRLLE DFT

Edit the Load/Work list profile                LRLLE PRO

Insert a Sample on a Load/Work list            LRLLINST

Move a Load/Work list entry                    LRLLMOVE

Print a load/work list                         LRLLP

Active Load Work Listing                       LRLLPA

Remove a Load/Work list entry                  LRLLREMV

Laboratory DHCP Menu                           LRMENU

Microbiology menu                              LRMI

Long form accession list for microbiology      LRMIACC1

Batch accessioning                             LRMIBL

Accessioning, standard (Microbiology)          LRMICROLOGIN

Results entry                                  LRMIEDZ

Edit Inactive DT Multiple – ETIOLOGY File      LRMIME

Edit Inactive DT Single – ETIOLOGY File        LRMISE

Verification of data by tech                   LRMINEWD

Microbiology print menu                        LRMIP

Cumulative patient report                      LRMIPC

All results for selected accessions            LRMIPLOG

Patient report                                 LRMIPSZ

References                                     LRMIREF

Enter/Edit medical journal references          LRMIREF JOURNAL

Enter/Edit micro journal references            LRMIREF MICRO

Inquire to micro journal references            LRMIREF MICRO I

Infection control survey report                LRMISEZ

Results entry (batch)                          LRMISTUF

Microbiology Trend Report                      LRMITS

Verification of data by supervisor             LRMIVER

Re-index Antimicrobial Suscept File (62.06)    LRMIXALL

List of orders not collected (Long form)       LRNDLST

Set a new starting accession number            LRNEWSTART

List of lab orders not collected               LRNODRAW

Special test accessioning                      LRNONCOM

Purge old orders &amp; accessions                  LROC

Accessioning tests ordered by ward order entry LROE

Documentation for lab options                  LROPT

Listing of Laboratory Menus/Options            LROPTLST

Order/test status                              LROS

Lab test order                                 LROW

Fast lab test order (IMMEDIATE COLLECT)        LROW IMMED COLLECT

Fast lab test order (ROUTINE)                  LROW ROUTINE

Fast lab test order (SEND PATIENT)             LROW SEND PAT

Fast lab test order (WARD COLLECT)             LROW WARD COL

Reprint a Ward Collect Order                   LROWRP

Receipt of routine lab collection from wards   LRPHEXCPT

Itemized routine lab collection                LRPHITEM

Print collection list/labels                   LRPHLIST

Add to collection list                         LRPHMAN

Quality control display (Levey-Jennings)       LRQC

Add/edit QC name &amp;/or edit test means          LRQCADDNAME

Bull algorithm quality control                 LRQCC

Manually accession QC, Environmental, etc.     LRQCLOG

Quality control menu                           LRQCM

Multipurpose accessioning                      LRQUICK

Interim report by provider                     LRRD

Interim reports for 1 provider (manual queue)  LRRD BY MD

Interim report                                 LRRP2

Interim report for selected tests              LRRP3

Lab orders by collection type                  LRRP5

Detail workload report                         LRRP6

Workload statistics by accession area and

shift                                         LRRP8

Interim reports by location (manual queue)     LRRS

Interim reports for 1 location (manual queue)  LRRS BY LOC

Interim report for selected tests as ordered   LRRSP

Flagged Specimens                              LRSMAC3

Run Smac                                       LRSMAC5

Halt Smac Run                                  LRSMAC6

Smac Support menu                              LRSMACMENU

Search for high/low values of a test           LRSORA

Search for critical value flagged tests        LRSORC

Search for abnormal and critical flagged tests LRSORD

Manual Enter Clinic Stop Codes                 LRSTOPC

Batch data entry (chem, hem, tox, etc.)        LRSTUF

Supervisor reports                             LRSUPER REPORTS

Supervisor menu                                LRSUPERVISOR

SUPERVISOR'S SUMMARY REPORT FOR TASKMAN        LRTASK ACS

LOAD CONTROLS ON THE ACCESSION LISTS.          LRTASK CONJAM

TASK THE CUMULATIVE TO RUN EACH NITE           LRTASK CUM

TASK CUMULATIVE FILEROOM REPORT                LRTASK CUM FILEROOM

QUEUED INTERIM DAILY REPORT (FIRST)            LRTASK DAILY INTERIM 1

QUEUED INTERIM DAILY REPORT (SECOND)           LRTASK DAILY INTERIM 2

Patient Lab Discharge Summary                  LRTASK DISCHARGE

START-UP THE BACK GROUND 'LAB' ROUTINE         LRTASK LAB

NIGHTLY CLEANUP                                LRTASK NIGHTY

CREATE NEW COLLECTION LIST                     LRTASK PHSET

CREATE NEW COLLECTION LIST                     LRTASK PHSET1

CREATE A COLLECTION LIST                       LRTASK PHSET2

ROLLOVER ACCESSION                             LRTASK ROLLOVER

Inquiry to LAB TEST file                       LRTESTDIQ

Delete test from an accession                  LRTSTOUT

Print accession list(s)                        LRUAC

File list for lab                              LRUCONTENTS

Changes in verified lab data                   LRUER

Print future collection labels                 LRUFCL

Print single future collection label           LRUFCLS

Outline for one or more files                  LRUFILE

Print/display preselected lab tests            LRUMD

Edit/print/display preselected lab tests       LRUMDA

Delete user selected lab test/patient lists    LRUMDD

Enter/edit user defined lab test lists         LRUMDE

Enter/edit predefined lab test lists           LRUMDL

User selected lab test/patient list edits      LRUMDLM

Accession list by number                       LRUPA

Lab accession and test counts                  LRUPAC

Accession and test counts by shift             LRUPACS

Test counts by treating specialty              LRUPACT

Accession list by date                         LRUPAD

Show list of accessions for a patient          LRUPT

Print group user manual                        LRUPUM

Edit group user manual                         LRUPUME

Edit referral patient file                     LRUV

Accession area worklist                        LRUW

Display workload for an accession              LRUWL

Enter/verify data (auto instrument)            LRVR

Enter/verify data (Work list)                  LRVRW

Enter/verify data (Load list)                  LRVRW2

Ward lab menu                                  LRWARDM

Incomplete test status report                  LRWRKINC

Add a new data name                            LRWU5

Modify an existing data name                   LRWU6

Add a new internal name for an antibiotic      LRWU7

Update Lab protocols for OE/RR                 LRX0

Update ALL lab protocols                       LRX1

Update protocol for a single lab test          LRX2

Update protocols for all lab tests             LRX3

Update protocols for all accession groups      LRX4

Update protocols for single accession group    LRX5

OE/RR interface parameters                     LRXOSX

Inquire to a Lab administration schedule       LRXOSX0

Edit a lab administration schedule             LRXOSX1

Edit HOSPITAL SITE parameters                  LRXOSX2

LABORATORY TEST MENU                           LRXQ1

### 43 Distribution of Menus

The Laboratory package menus consists of 11 main areas. Each Laboratory may reorganize the order and grouping of menus according to its specific needs and work flow.

Laboratory Options [LRMENU]

1. Phlebotomy menu [LR GET]

2. Accessioning menu [LR IN]

3. Process data in lab menu [LR DO!]

4. Quality control menu [LRQCM]

5. Results menu [LR OUT]

6. Information-help menu [LRHELP]

7. Ward lab menu [LRWARDM]

8. Anatomic pathology [LRAP]

9. Blood bank [LRBL]

10. Microbiology menu [LRMI]

11. Supervisor menu [LRSUPERVISOR]

### 44 Menus with Entry or Exit Action

Listed below are Laboratory V. 5.2 menus that contain entry or exit action:

NAME: LR IN                             MENU TEXT: Accessioning menu

ENTRY ACTION: D ^LRPARAM

NAME: LRWARDM                       MENU TEXT: Ward lab menu

ENTRY ACTION: D ^LRWD,^LRPARAM

NAME: LRAP                              MENU TEXT: Anatomic pathology

ENTRY ACTION: S IOP="HOME" D ^%ZIS W @IOF,?28,"ANATOMIC PATHOLOGY MENU"

NAME: LRBL                              MENU TEXT: Blood bank

ENTRY ACTION: S IOP="HOME" D ^%ZIS W @IOF,?35,"BLOOD BANK"

NAME: LRMI                              MENU TEXT: Microbiology menu

EXIT ACTION: K A,Z

NAME: LRMENU                         MENU TEXT: Laboratory DHCP Menu

ENTRY ACTION: D ^LRPARAM        EXIT ACTION: D ^LRKILL

### 45 Security Keys

Each user of the Laboratory package must have the appropriate keys assigned before accessing the Lab package. The SECURITY KEY file (#19.1) contains the key names and a short description. You will need to enter the users names under each of the appropriate key names. Following is a list of the Lab keys:

KEY	USERS

LRANAT	Anatomic Pathology users

LRAPSUPER	Anyone allowed to use the Anatomic Pathology Supervisor Menu and edit SNOMED codes

LRAU	Autopsy Module users

LRBLOODBANK	Blood Bank users

LRBLSUPER	For Blood Bank supervisory level decisions

LRCY	Cytology Module users

LREM	Electron Microscopy Module users

LRLAB	Laboratory Personnel only

LRLIASON	Laboratory Information Manager

LRMICRO	Microbiology users

LRMIVERIFY	Microbiology personnel

LRSP	Surgical Pathology Module users

LRSUPER	Laboratory Supervisors

LRVERIFY	Anyone who is authorized to verify lab results

LRPHMAN	Phlebotomists

LRPHSUPER	Supervisor of the phlebotomy collection team

Any combination of the above security levels may be used, as deemed appropriate by the Laboratory.

#### Individual Module Requirements/Concerns

##### 15 Anatomic Pathology

In addition to the LRLAB and LRVERIFY security keys, the Anatomic Pathology module requires several specific keys to access the appropriate accession areas and options which should be limited to supervisory level or experience personnel.

LRANAT	Anatomic Pathology users*

LRAU	Autopsy Module users*

LRCY	Cytology Module users*

LREM	Electron Microscopy Module users*

LRSP	Surgical Pathology Module users*

LRAPSUPER	Allows anyone to use the Anatomic Pathology Supervisor Menu and edit SNOMED codes

LRSUPER	Laboratory Supervisors

Since the various options, excluding those in the Supervisor menu, do not require specific security keys once you have the appropriate accession area keys, regulating access to the options must be accomplished via strict menu management.

##### 16 Blood Bank

In addition to the LRLAB and LRVERIFY security keys, the Blood Bank Module requires only the LRBLOODBANK key to access the majority of the options. The LRBLSUPER key is, however necessary to access all of the options in the Supervisor’s Menu, as well as to release incompatible blood using the Disposition-relocation [LRBLIDR] option in the Inventory Menu.

Since the various options, excluding those in the Supervisor’s menu, do not require specific security keys, regulating access to the options must be accomplished via strict menu management. Menus must be constructed at each site, tailored to the actual needs of the individuals using the module.

##### 17 Chemistry/Immunology

The Chemistry subscript Module requires the LRLAB and LRVERIFY security keys to access the majority of the options. The LRSUPER key is necessary to access the options in the Supervisor’s Menu.

##### 18 Microbiology

In addition to the LRLAB and LRVERIFY security keys, the Microbiology Module requires only the LRMICRO key to access the majority of the options and to release results. The LRSUPER key is necessary to access the options in the Microbiology Supervisor Menu,

##### 19 Phlebotomy

The phlebotomy section requires the LRLAB key to access the necessary options. The LRPHSUPER key is, however, necessary to access the options needed by the Phlebotomy supervisor.

### 46 LRTASK Options

These options are designed to be scheduled through TaskMan.

**OPTION	ROUTINE	DESCRIPTION**

LRTASK ACS	LRACS	Supervisor’s daily summary report based on File #64.5. The format is by location, by patient. If a summary is desired by accession number, use the LR SUP SUMMARY option. The LR SUP SUMMARY option is more comprehensive and bulkier. This option should be chosen only if the job failed to run.

LRTASK CONJAM	LRCONJAM	Run by TaskMan each night to set up the controls for the accession list.

LRTASK CUM	CL2^LRAC	Function automatically run by TaskMan. This function should only be selected if the job failed to start. Any other reprints or reruns of any part of the cumulative should be initiated via one of the reprint options in the cumulative menu. Various versions of this option can be created if multiple devices are used to print the cumulative.

LRTASK CUM	CLOCK^LRACFR	This option is used to print file

FILEROOM		room cumulative patients. This option determines the last time the file room patients were printed. It then identifies all file room patients that require printing since the last run and move those entries to the current list of cumulative file room patients. Finally it queues a task to print these patients to specified printers. When the LAB REPORTS file has been properly set, this option will allow the printing of the file room cum on a different schedule than in patient cums.

LRTASK DAILY	AIDQ^LRRP2	MenuMan queue option for the

INTERIM 1		first daily interim cumulative report.

LRTASK DAILY	AIDQ^LRRP2	Same as LRTASK DAILY

INTERIM 2		INTERIM 1.

LRTASK DISCHARGE	DQ^LRACSUM	For automatic queuing of a Laboratory discharge summary for patients discharge T-1 from the date this option is invoked. The report is in a similar format as the full patient summary and the cumulative report. The only results that are printed are those that are ordered from the date of admission to the date of discharge.

LRTASK LAB	DQ^LAB	Option to be used by the TaskMan to start up the background LAB routine each time the system is started from a boot.

LRTASK NIGHTY	LRNIGHT	Routine run nightly by TaskMan to do some lab cleanup.

LRTASK PHSET	LRPHSET	Routine run each day by TaskMan to create the collection list.

LRTASK PHSET1	LRPHSET	Routine run each day by TaskMan to create the collection list.

LRTASK ROLLOVER	LROLOVER	Routine run each night by TaskMan to roll forward the unverified accessions.

CROSS REFERENCES

Cross References

The cross references are grouped by files. The field affected is identified along with the cross reference name or number, if there is no name.

**Select FILE: 60  LABORATORY TEST**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

*  "AB"                 60.02          .01   LAB TEST

*  "B"                     60          .01   NAME

*  "C"                     60            5   LOCATION (DATA NAME)

*  "D"                     60           51   PRINT NAME

**Select FILE: 61  TOPOGRAPHY FIELD**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

*  "B"                     61          .01   NAME

*  "C"                     61            2   SNOMED CODE

*  "D"                  61.01          .01   SYNONYM

*  "E"                     61            6   ABBREVIATION

**Select FILE: 61.1  MORPHOLOGY FIELD**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

*  "B"                   61.1          .01   NAME

*  "C"                   61.1            2   SNOMED CODE

*  "D"                  61.11          .01   SYNONYM

**Select FILE: 61.2  ETIOLOGY FIELD**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

*  "B"                   61.2           .01   NAME

*  "C"                   61.22          .01   SYNONYM

*  "D"                   61.2            2   SNOMED CODE

*  "E"                   61.23          .01   *BIOCHEMICAL WORKUP

**Select FILE: 61.3  FUNCTION FIELD**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

*  "B"                   61.3          .01   NAME

*  "C"                   61.3            2   SNOMED CODE

*  "D"                   61.31         .01   SYNONYM

*  "E"                   61.3            4   IDENTIFIER

**Select FILE: 61.4  DISEASE FIELD**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

*  "B"                   61.4           .01   NAME

*  "C"                   61.4             2   SNOMED CODE

*  "D"                   61.41          .01   SYNONYM

**Select FILE: 61.5  PROCEDURE FIELD**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

*  "B"                   61.5           .01   NAME

*  "C"                   61.5             2   SNOMED CODE

*  "D"                   61.51          .01   SYNONYM

**Select FILE: 61.6  OCCUPATION FIELD**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

*  "B"                   61.6         .01       NAME

*  "C"                   61.6           2       SNOMED CODE

"D"                   61.61        .01       SYNONYM

**Select FILE: 62  COLLECTION SAMPLE**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

*  "B"                     62          .01   NAME

*  "C"                     62            3   TUBE TOP COLOR

*  "D"                  62.01          .01   SYNONYM

**Select FILE: 62.05  URGENCY**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

*  "B"                  62.05          .01   URGENCY

**Select FILE: 62.06  ANTIMICROBIAL SUSCEPTIBILITY**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

"AC"                 62.06            1   DRUG NODE

*  "AD"                 62.06            1   DRUG NODE

"AF"                 62.06            6   ABBREVIATION

*  "AI"                 62.06            1   DRUG NODE

*  "AJ"                 62.06            1   DRUG NODE

*  "AO"                 62.06           .5   PRINT ORDER

*  "AS"                 62.06            1   DRUG NODE

*  "B"                  62.06          .01   NAME

*  "C"                  62.06            5   INTERNAL NAME

*  "D"                  62.06            6   ABBREVIATION

**Select FILE: 62.07  EXECUTE CODE**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

"AC"                 62.07            5   SUBSCRIPT NAME

*  "B"                  62.07          .01   NAME

**Select FILE: 62.1  DELTA CHECKS**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

*  "B"                   62.1          .01   NAME

**Select FILE: 62.3  LAB CONTROL NAME**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

"AC"                  62.3          .01   NAME

*  "B"                   62.3          .01   NAME

**Select FILE: 62.4  AUTO INSTRUMENT**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

*  "AC"                  62.4          100   METH NAME

"AD"                  62.4            3   LOAD/WORK LIST

"AS"                  62.4            5   ENTRY for LAGEN ROUTINE

*  "B"                   62.4          .01   NAME

*  "C"                   62.4            2   PROGRAM

*  "D"                   62.4           10   METHOD

**Select FILE: 62.5  LAB DESCRIPTIONS**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

*  "AC"                  62.5          .01   NAME

*  "AD"                  62.5            5   SCREEN

*  "B"                   62.5          .01   NAME

**Select FILE: 62.55  AGGLUTINATION STRENGTH**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

*  "B"                  62.55          .01   NAME

*  "C"                  62.55            1   WILL STAND FOR

**Select FILE: 62.6  ACCESSION TEST GROUP**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

*  "B"                   62.6          .01   ACCESSION TEST GROUP

**Select FILE: 63  LAB DATA**

XREF            DD       FLD NUM     FIELD NAME

---------------   --------   ----------   ------------------------------

*  "AAU"                   63           11   AUTOPSY DATE/TIME

*  "AAUA"                  63           14   AUTOPSY #

*  "AB"                63.017          .11   TRANSFUSION REACTION TYPE

"AC"                 63.34          .01   PARASITE

*  "ACY"                63.09           .1   DATE/TIME SPECIMEN RECEIVED

*  "ACYA"               63.09          .06   ACCESSION #

"AD"                  63.3          .01   ORGANISM

"AE"                 63.37          .01   FUNGUS/YEAST

*  "AEM"                63.02           .1   DATE/TIME SPECIMEN RECEIVED

*  "AEMA"               63.02          .06   ACCESSION #

"AF"                 63.39          .01   MYCOBACTERIUM

"AG"                 63.43          .01   VIRUS

*  "AR"               63.0171          .02   TRANSFUSION REACTION TYPE

*  "ASP"                63.08           .1   DATE/TIME SPECIMEN RECEIVED

*  "ASPA"               63.08          .06   SURGICAL PATH ACC #

"AZZ"                   63          .02   PARENT FILE

*  "B"                     63          .01   LRDFN

"CZZ"                   63          .03   NAME

**Select FILE: 63.9999  ARCHIVED LR DATA**

XREF            DD       FLD NUM     FIELD NAME

---------------   --------   ----------   ------------------------------

"AZZ"              63.9999          .02   PARENT FILE

*  "B"                63.9999          .01   LRDFN

"CZX"              63.9999          .03   NAME

"CZZ"              63.9999          .03   NAME

**Select FILE: 64  WKLD CODE**

XREF            DD       FLD NUM     FIELD NAME

---------------   --------   ----------   ------------------------------

"AC"                    64           15   ACTIVATE WKLD CODE

*  "B"                     64          .01   PROCEDURE

*  "C"                     64            1   WKLD CODE

*  "D"                     64          .01   PROCEDURE

*  "E"                     64            1   WKLD CODE

"F"                     64          .04   PRINT NAME

*   "G"                 64.019          .01   SYNONYM

**Select FILE: 64.05  NON WKLD PROCEDURES**

XREF            DD       FLD NUM     FIELD NAME

---------------   --------   ----------   ------------------------------

*  "B"                  64.05          .01   PROCEDURE

*  "C"                  64.05            1   WKLD CODE

**Select FILE: 64.1  WKLD DATA**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

"B"                   64.1          .01   INSTITUTION

**Select FILE: 64.2  WKLD SUFFIX CODES**

XREF            DD       FLD NUM     FIELD NAME

---------------   --------   ----------   ------------------------------

*  "AC"                  64.2           15   ACTIVATE WKLD CODE

*  "B"                   64.2          .01   NAME

*  "C"                   64.2            1   WKLD SUFFIX CODE

*  "D"                   64.2           11   MANUFACTURER

*  "E"                   64.2           11   MANUFACTURER

*  "F"                   64.2            1   WKLD SUFFIX CODE

**Select FILE: 64.19999    ARCHIVED WORKLOAD WKLD DATA**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

"B"               64.19999          .01   INSTITUTION

**Select FILE: 64.21  WKLD CODE LAB SECT**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

*  "B"                  64.21          .01   NAME

*  "C"                  64.21            1   ABBREV.

"D"                  64.21            2   SYNONYM

*  "E"                  64.21          .01   NAME

**Select FILE: 64.22  WKLD ITEM FOR COUNT**

XREF            DD       FLD NUM     FIELD NAME

---------------   --------   ----------   ------------------------------

*  "B"                  64.22          .01   ABBREV

*  "C"                  64.22            1   Full Name

*  "D"                  64.22            1   Full Name

**Select FILE: 64.3  WKLD INSTRUMENT MANUFACTURER**

XREF            DD       FLD NUM     FIELD NAME

---------------   --------   ----------   ------------------------------

*  "B"                   64.3          .01   NAME

**Select FILE: 64.5  LAB REPORTS**

XREF            DD       FLD NUM     FIELD NAME

---------------   --------   ----------   ------------------------------

*  "AC"                 64.53            4   TEST LOCATION

*  "B"                   64.5          .01   NAME

"MUMPS5"              64.5            7   REPORT DATE

**Select FILE: 64.6  INTERIM REPORTS**

XREF            DD       FLD NUM     FIELD NAME

---------------   --------   ----------   ------------------------------

"AC"                  64.6       600000   EPIC REPORTING

*  "AD"                  64.6            3   DEVICE

*  "AI"                  64.6          .01   LOCATION

*  "AS"                  64.6            1   IMMEDIATELY TRANSMIT RESULTS

"AS1"                 64.6          .01   LOCATION

*  "B"                   64.6          .01   LOCATION

**Select FILE: 64.7  CUMULATIVE**

XREF            DD       FLD NUM     FIELD NAME

---------------   --------   ----------   ------------------------------

*  "B"                   64.7          .01   LRDFN

**Select FILE: 65  BLOOD INVENTORY**

XREF            DD       FLD NUM     FIELD NAME

---------------   --------   ----------   ------------------------------

*  "A"                     65          .05   DATE/TIME RECEIVED

"AA"                 65.31          .01   COMPLETE DATE/TIME

*  "AB"                    65          4.2   DISPOSITION DATE

"AC"                    65          4.1   DISPOSITION

"AD"                    65           10   ABO INTERPRETATION

*  "AE"                    65          .06   EXPIRATION DATE/TIME

"AF"                    65           11   RH  INTERPRETATION

"AG"                    65          4.1   DISPOSITION

"AH"                    65          .04   COMPONENT

*  "AI"                    65          .06   EXPIRATION DATE/TIME

"AJ"                    65          .01   UNIT ID

"AK"                    65          .04   COMPONENT

*  "AL"                 65.03          .01   DATE/TIME UNIT RELOCATION

"AM"                 65.01          .01   PATIENT XMATCHED/ASSIGNED

*  "AN"                 65.02          .09   DATE/TIME CROSSMATCHED

"AO"                    65          .02   SOURCE

*  "AP"                 65.01          .02   DATE/TIME UNIT ASSIGNED

"APS"                   65          4.1   DISPOSITION

"AQ"                    65          .04   COMPONENT

"AR"                 65.15          .08   PREVIOUS DATE LOGGED-IN

*  "AT"                    65          .01   UNIT ID

*  "AU"                    65            8   RESTRICTED FOR

*  "B"                     65          .01   UNIT ID

*  "C"                     65          .01   UNIT ID

**Select FILE: 65.4  BLOOD BANK UTILITY**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

*  "B"                   65.4          .01   NAME

*  "C"                   65.4          .03   FULL NAME

**Select FILE: 65.5  BLOOD DONOR**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

"AA"               65.5991          .01   COMPLETE DATE/TIME

"AC"                 65.54           10   ABO INTERPRETATION

*  "AD"                 65.54          .01   DONATION OR DEFERRAL DATE

"AE"                 65.54           11   RH INTERPRETATION

"AF"                 65.54           12   SYPHILIS SEROLOGY

"AG"                 65.54           13   HBsAg

"AH"                 65.54           14   HIV ANTIBODY

"AI"                 65.54           15   ANTIBODY SCREEN RESULT

"AJ"                 65.54           16   HBcAb

"AK"                 65.54           17   ALT

"AL"                 65.54           18   HTLV-I ANTIBODY

"AM"                 65.54           19   HCV ANTIBODY

*  "AT"                 65.54            4   UNIT ID

*  "B"                   65.5          .01   NAME

*  "C"                  65.54            4   UNIT ID

*  "D"                  65.54            4   UNIT ID

"E"                   65.5          .03   DOB

"F"                   65.5          .01   NAME

*  "G"                   65.5          .13   SSN

*  "G4"                  65.5          .13   SSN

"G40"                 65.5          .01   NAME

**Select FILE: 65.9  LAB LETTER**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

*  "B"                   65.9          .01   NAME

**Select FILE: 65.9999  ARCHIVED BLOOD INVENTORY**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

"A"                65.9999          .05   DATE/TIME RECEIVED

"AA"               65.999931        .01   COMPLETE DATE/TIME

"AB"               65.9999          4.2   DISPOSITION DATE

"AC"               65.9999          4.1   DISPOSITION

"AD"               65.9999           10   ABO INTERPRETATION

"AE"               65.9999          .06   EXPIRATION DATE/TIME

"AF"               65.9999           11   RH  INTERPRETATION

"AG"               65.9999          4.1   DISPOSITION

"AH"               65.9999          .04   COMPONENT

"AI"               65.9999          .06   EXPIRATION DATE/TIME

"AJ"               65.9999          .01   UNIT ID

"AK"               65.9999          .04   COMPONENT

"AL"               65.999903        .01   DATE/TIME UNIT RELOCATION

"AM"               65.999901        .01   PATIENT XMATCHED/ASSIGNED

"AN"               65.999902        .09   DATE/TIME CROSSMATCHED

"AO"               65.9999          .02   SOURCE

"AP"               65.999901        .02   DATE/TIME UNIT ASSIGNED

"APS"              65.9999          4.1   DISPOSITION

"AQ"               65.9999          .04   COMPONENT

"AR"               65.999915        .08   PREVIOUS DATE LOGGED-IN

"AT"               65.9999          .01   UNIT ID

"AU"               65.9999            8   RESTRICTED FOR

"B"                65.9999          .01   UNIT ID

"C"                65.9999          .01   UNIT ID

**Select FILE: 66  BLOOD PRODUCT**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

*  "B"                     66          .01   NAME

*  "C"                     66            2   SYNONYM

*  "D"                     66          .05   PRODUCT CODE

**Select FILE: 66.5  OPERATION (MSBOS)**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

*  "B"                   66.5          .01   NAME

**Select FILE: 66.9  BLOOD COMPONENT**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

"B"                   66.9          .01   NAME

**Select FILE: 67  REFERRAL PATIENT**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

*  "B"                     67          .01   NAME

*  "C"                     67          .09   IDENTIFIER

*  "CN"                    67           .1   REFERRAL SOURCE

*  "D"                     67          .01   NAME

**Select FILE: 67.1    RESEARCH**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

*  "B"                   67.1          .01   NAME

*  "C"                   67.1            9   IDENTIFIER

*  "D"                   67.1          .01   NAME

**Select FILE: 67.2  STERILIZER**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

"AC"                  67.2           .1   LOCATION

*  "B"                   67.2          .01   NAME

*  "C"                   67.2            9   IDENTIFIER

**Select FILE: 67.3  ENVIRONMENTAL**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

*  "B"                   67.3          .01   NAME

*  "C"                   67.3            9   IDENTIFIER

**Select FILE: 67.4  NON PATIENT WORKLOAD**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

"B"                   67.4          .01   NAME

**Select FILE: 67.9  LAB MONTHLY WORKLOADS**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

"B"                   67.9          .01   PRIMARY INSTITUTION

**Select FILE: 67.99999  ARCHIVED LAB MONTHLY WORKLOADS**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

"B"               67.99999          .01   PRIMARY INSTITUTION

**Select FILE: 68  ACCESSION**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

"AA"                 68.04            4   COMPLETE DATE

*  "AC"                 68.02           13   DATE/TIME RESULTS AVAILABLE

*  "AD"                    68         .095   *LAB SECTION

*  "AE"                    68          .04   COMMON ACCESSION #'S WITH AREA

"AMI"                68.04            4   COMPLETE DATE

*  "B"                     68          .01   AREA

**Select FILE: 68.2  LOAD/WORK LIST**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

*  "B"                   68.2          .01   NAME

**Select FILE: 68.4  WORKLIST HEADINGS**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

"B"                   68.4          .01   NAME

**Select FILE: 69  LAB ORDER ENTRY**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

*  "AA"                 69.01           13   COLLECTION STATUS

"AN"                 69.01           21   DATE/TIME RESULTS AVAILABLE

*  "B"                     69          .01   DATE ORDERED

*  "C"                  69.01          9.5   ORDER #

*  "D"                  69.01          .01   LRDFN

**Select FILE: 69.1  COLLECTION LIST**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

*  "B"                   69.1          .01   COLLECTION ROUTE

*  "LRPH"               69.11          .01   TEST

"LRPH1"              69.11            4   SPECIMEN #

**Select FILE: 69.9  LABORATORY SITE**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

"AC"                  69.9          .01   SITE NAME

*  "B"                   69.9          .01   SITE NAME

**Select FILE: 69.91  LR ROUTINE INTEGRITY CHECKER**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

*  "B"                  69.91          .01   Version #

"C"                69.9113          .01   Patch #

**Select FILE: 69.2  LAB SECTION PRINT**

XREF            DD       FLD NUM               FIELD NAME

---------------   --------   ----------   ------------------------------

*  "B"                 69.2       .01               NAME

*  "C"                 69.2       .02               ABBREVIATION

**Select FILE: 69.71  LR CPRS PARAMETERS**

INDEX             FILE                       FIELD(S)

------------------  ---------------  ----------------------------------------

*B                  69.71            NAME (#.01)

*C                  69.71            SYNONYM (#1)

-B                 69.712           QUESTIONS (#.01)

-B                 69.713           URL LINK (#.01)

-B                 69.714           CPRS ID NAME (#.01)

**Select FILE: 95  LAB JOURNAL**

XREF            DD       FLD NUM              FIELD NAME

---------------   --------   ----------   ------------------------------

*  "B"                   95      .01                  JOURNAL ABBREVIATION

*  "C"                   95      .02                  FULL NAME

PURGING AND ARCHIVING

## Purging And Archiving

### 47 Force Cumulative Data to Permanent Page [LRAC FORCE]

The concept of temporary and permanent pages is part of the cumulative design. For pages to be in this format, the cumulative must have been initialized.

One of the eligibility requirements for archiving of laboratory data from the ^LR global assumes that the cumulative is in use and that the 9th piece of ^LR is set to a permanent page designation when a page becomes “full.”

Unfortunately, many patients do not have the activity level which will result in a “full” page within a reasonable time frame. In the case of deceased patients, the temporary pages have no mechanism to become permanent since there is no longer any activity for these pages.

This, in conjunction with some site selectable parameters such as not printing cumulatives for either inpatients or outpatients, not initializing the cumulative report, etc., has resulted in increasing disk space requirements by laboratory.

The option Force Cumulative Data to Permanent Page [LRAC FORCE] can be used to set the 9th piece in the ^LR global to a permanent page designation. This option can be used whether or not a cumulative report has printed. By setting the page designation in ^LR, the data is considered to be permanent and eligible for subsequent archiving. Data is not removed from the system until the archiving utilities have been run.

To use the option, the field Grace Period For Inactivity in the LABORATORY SITE file (#69.9) must contain an entry. Each site should establish a reasonable time frame for inactivity (e.g., if a patient has not had any activity - no tests ordered - for 6 months, 2 years, etc., we might want to make it eligible for archiving). The field entry represents the number of days of inactivity.

For those patients who had Force Cumulative Data To Permanent Page [LRAC FORCE] option run for a cumulative report, the page numbers will reflect the last temporary page. There is no reprinting of the cumulative report at this time.

**Example:** If the last temporary pages to print on SMITH,JOHN were 1:1,2:2,25:1 and there has been no activity on this patient for the grace period for inactivity, the current page designation will be forced into the 9th piece of ^LR global. When the pages are forced to permanent, the ^LR(LRDFN,”PG” node is updated. The next time the patient has data for each of these pages, the pages to print will be 1:2,2:3,25:2.

**NOTE:** If there has been any data reported within the grace period for any page, the patient data is not forced. Either all pages are forced or no pages are forced.

If the patient results have not been initialized and printed in the cumulative report format, the data is still eligible for forcing to permanent pages. The routine looks at the data in ^LR and determines the major header page for the results. The increment within the major header will be set to “1” for all results, regardless of the amount of data for each of the headers. If this patient subsequently does have a cumulative report printed, the temporary pages will start with the second page increment within the Major Header; i.e., MAJOR HEADER:2 (increment within the major header).

A list of patients is generated during the running of this routine, which will print the LRDFN, patient’s name, and pages that were forced to permanent.

The ^LRO(68,”AC” and ^LAC(“LRAC” cross references to the data in ^LR(LRDFN,”CH” are also killed off.

**NOTE:** You may want to stop journaling during the running of this routine, because of the increased amount of journal space used when global nodes are killed.

### 48 Purge Old Orders and Accessions [LROC]

Ordering and accession information for those accession areas in ACCESSION file (#68) set up to have a transform of DAILY is purged with this utility option. Data stored in ^LRO(68,”LRAA”,^LRO(69, “C”, and ^LRO(69, “B” are killed off during the running of this routine. The amount of data retained will be determined by the field GRACE PERIOD FOR ORDERS in File #69.9. Once this data is purged, any option referencing the accession number (e.g., CH 0814 44) or the order number will no longer be accessible. Some examples of options are: EM (Enter/verify/modify data), Review by Order Number, Interim Report for Selected Tests as Ordered.

This option should be run on a regular basis to control the amount of disk space required by laboratory. Your site should determine an appropriate length of time to retain at this type of information. It is recommend that the site retain at least 120 days of accession/orders.

For accession areas (i.e., for referral tests) where the turnaround time may exceed the Grace Period for Orders, consider setting these up for monthly or yearly accession area transform.

Never run this option Purge Old Orders and Accessions [LROC] during peak activity hours since it is system-intensive. A Site Manager may want to disable journaling ^LRO, depending on the amount of data in these files to be purged and the frequency with which the option is run. To purge the data for ^LRO(68,”LRAA” for those Accession areas other than daily, VA FileManager must be used.

**Example:** Purging of a yearly, quarterly, or monthly Accession area transform deletion.

Select OPTION: **E** (ENTER OR EDIT FILE ENTRIES)
INPUT TO WHAT FILE:    OPTION// **68** ACCESSION    (22 entries)
EDIT WHICH FIELD:    ALL// **DATE** (multiple)
             EDIT WHICH DATE SUB-FIELD:    ALL// **&lt;RET&gt;** THEN EDIT FIELD: **&lt;RET&gt;** Select ACCESSION AREA: **MICRO** BIOLOGY

Select DATE:    1987// **&lt;RET&gt;** DATE:    1987// **@** SURE YOU WANT TO DELETE THE ENTIRE DATE? **Y** (YES)

**NOTES:**

1.	An answer of “YES” will delete an entire year.

2.	Monthly Accession Areas delete entire month.

3.	Quarterly Accession Areas delete entire quarter.

#### Archive of LAB DATA file (#63)

The archive process looks through the LAB DATA file (#63) for data from microbiology (MI), chemistry, urinalysis, hematology, serology, etc., (CH). Any found eligible are copied to the global ^LAR for subsequent processing by the archive utilities.

Eligibility is determined by the following criteria:

a.	Lab determines the minimum retention period. The default is currently T-180. Note that the retention period should be longer than the time the data is saved in the Accession and Order files. Micro data is retained an additional 370 days by the archive search, to accommodate the yearly accession area.

b.	For CH tests, the results must have been printed to a cumulative permanent page. For MI tests, any data older than the retention period is eligible to be archived. Clinic patients with low activity, deceased patients, or any other group with few lab tests ordered will never turn over permanent pages and the current utility will never archive this data. The option, Force cumulative data to permanent page [LRAC FORCE], can be used to set the 9th piece in the ^LR global to a permanent page designation. By setting the page designation in ^LR, the data is considered to be permanent and eligible for subsequent archiving.

c.	Tests for Lab Controls, Research, Environmental, and Reference patients are selected for archive solely on the basis of the retention period.

##### 20 Archive Options

You reach the archiving options using the following pathway:

Supervisor menu [LRSUPERVISOR]

Lab liaison menu [LRLIASON]

Archive lab data [LR ARCHIVE MENU]

1  Search for lab data to archive [LR ARCHIVE SEARCH]

**&gt; Locked with LRLIASON

2  Write data to off-line media [LR ARCHIVE WRITE MEDIA]

3  Clear data from the LAR global [LR ARCHIVE CLEAR]

**&gt; Locked with LRLIASON

4  Read data from off-line media [LR ARCHIVE READ MEDIA]

5  Purge data found in the Search option [LR ARCHIVE PURGE]

**&gt; Locked with LRLIASON

6  Find patient's archived data [LR ARCHIVE DATA]

7  Convert archived data to use New Person file [LR ARCHIVE NP CONVERSION]

8  Restore archived data to LR global [LR ARCHIVE RESTORE]

The six archiving options are listed below in the required sequence for archiving and/or restoring of data (they MUST be run in this order):

**NOTE:** It is recommended to run Force Cumulative Data to Permanent Page [LRAC FORCE] option before proceeding.

1.	Search for Lab Data to Archive

Data to be archived should be older than the beginning of the month three months ago. Anatomic Pathology and Blood Bank data are not archived.

2.	Write Data to Off-Line Media

After having created entries in the ^LAR global, the data should be written to off-line media for purposes of long-term storage. The site manager should determine the method of data storage of the ^LAR global.

3.	Clear data from the LAR global

Data found in the Search Archive option is removed by this option.

4.	Read Data from Off-Line Media

After having cleared the ^LAR global, the data should be read back in, to verify and purge what has been archived. The site manager should determine the method of data retrieval of the ^LAR global.

5.	Purge Data Found in the Search Option

Data found in the Search archive option are stored in the ^LAR global. Note that the data is removed from both the ^LR and the ^LAR globals. This step cannot be run unless step 3 has been done. This step loops through LAR and removes the corresponding entry from the LAB DATA file (#63). Accession nodes are checked before deletion to make sure that nothing has been modified since the search phase. A record is kept in the LAB DATA file (#63) to indicate that this patient has had archived data and to tell which tape has been used.

6.	Find Patient’s Archived Data

Once the archived tape has been restored to the system, a single patient or all patients may be retrieved from that archived tape. Data for a patient which has been archived, the storage location of the data is saved with the patient’s remaining entry in the ^LR(global. This information can be found using this option.

7.	Convert Archived LR Data

This option is used to convert the data to the NEW PERSON file (#200).

***WARNING:** It is required that this step be performed before any patient data is utilized. Failure to do so will result in various names being incorrect. Patients name in clinical data does not require this conversion process.

8.	Restore Archived Data to LR Global

This option is used to restore data into the LR global that has been archived.

**NOTES:**

1.	To reproduce a cumulative for patient data that has been restored from the archives, use the Reprint cumulative on a given patient [LRAC PT] option, and re-initialize the patient’s entire cumulative.

2.	The physical and logical names you are asked for during the archiving process are meant to be identifiers for you to keep record of archiving processes. They are NOT physical or logical devices (e.g., printer, terminal, etc.,).

3.	When you restore a patient to the ^LR global, you now have two records. One active on the ^LR global and one archived. When you archive that section of the ^LR global, you will have two archive records on that one patient.

EXTERNAL RELATIONS

## 5 External Relations

This section explains special relations and agreements between routines in this package and routines in other packages. It also specifies versions of FileMan, Kernel, and other packages required.

### 49 External Referenced Files and Fields

FILES	Fields Used

2	PATIENT	Name, SSN, Sex, DOD, Current Admission, 		Date Of Death, Ward

19.1	SECURITY KEY	Name

40.5	HOLIDAY	Date

40.8	MEDICAL CENTER DIV.	Version Node

42	WARD LOCATION	Name

42.4	SPECIALTY	PTF Code, Service

4.3	KERNEL SITE	Default Institution Parameters

44	HOSPITAL LOCATION	Name, Abbreviation, Treating Specialty,			Type

45	PTF	Procedures, Movement Record

45.7	FACILITY TREATING 	Name

SPECIALTY

50	DRUG	Generic Name

50.5	DRUG CLASSIFICATION	Name

52	PRESCRIPTION	Drug

55	PHARMACY PATIENT	Prescription Profile

80	ICD DIAGNOSIS	Code Number, Diagnosis

80.1	ICD OPERATION/	Code Number Operation Procedure

PROCEDURE

81	CPT	Description, Blood Component Request,			Short Name

81.1	CPT CATEGORY	CPT Category Name

100	ORDER	OERR Internal File#

101	PROTOCOL	(Entire File)

130	SURGERY	Name

200	NEW PERSON	Name

405	PATIENT MOVEMENT	Admission, Discharge, &amp; Transfer

**NOTE:** Permission has been received from the respective package developers to reference these fields.

### 50 External Routines

The Laboratory package makes calls to VA FileMan, MenuMan, MailMan, Pharmacy, OE/RR routines, tools, and utilities supplied through the Kernel software:

%DT	%DTC	%ZIS

%ZTLOAD	%ZOSV	DIC

SDACS	PSJEEU	DIC1

DICD	ORX	DICN

DICQ	XMD	DIE

DIK	XQH	DIM

DIP	XUS	DIQ

DIWP	ZU	DIWW

Two Department of Defense (DoD) routines (IAAPRIV and IAARNUM) are called by the Laboratory software if the variable DUZ (“AG”) contains “ARMYAFN.”

The DoD MILITARY RANK file is pointed to by the Military Rank field in the BLOOD DONOR file. This file will only exist at DoD sites.

### 51 External Variables

The variable DIU(0) is used to determine the manner in which to create or recreate certain cross-references.

### 52 Required Software

You must have Kernel V. 7.1 or greater and FileMan V. 20.0 or greater installed and running before Laboratory V. 5.2 can be used. The current MAS V. 5.2 or greater should also be installed. The LAB JOURNAL file (#95) is also required by the Microbiology module. If Lab is installed in an agency other than the Veterans Administration (as defined by the Agency code field in the KERNEL SITE PARAMETER file), the routines IAAPRIV and IAARNUM may be required for DoD Sites.

**Package	Versions (or Greater)**

Kernel	7.1

FileMan	20.0

MAS	5.3

Laboratory 	5.1

(if already resident)

OE/RR	2.5

AMIE	2.5

Inpatient Medication	3.2

### 53 DBA Integration Agreements

LIMs and IRM personnel need to be aware of the fields controlled by Lab that affect other programs BEFORE they make any programming changes. To obtain the most current listing, the DBA menu is located on Forum under secondary options.

**Example:**

Select Mailman Menu Option: **DBA**

Select DBA Option: **?**

1      List Package file by Name

2      List Package file by Prefix

3      Find lo-high range of filenumbers

4      Package file inquire

5      Package file inquire by #

6      Institution file inquire

7      SACC Exemptions ...

8      Supported references (DBIC library) ...

**&gt; Out of order:  Replaced by 'Integration Agreements Menu'

9      Projected releases

10     Domain file inquire

11     Integration Agreements Menu ...

12     Standards and Conventions

13     MOP-UP ...

14     Quarterly Briefing Report by season

15     QBR for one activity

16     Peer Review Participation

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select DBA Option: **11** Integration Agreements Menu

Select Integration Agreements Menu Option: **?**

O      Instructions for Entering IA's

1      Get New Integration #'s

2      Add/Edit

3      Inquire

4      Roll-up into Mail Message

5      File Agreements Menu ...

6      Routine Agreements Menu ...

7      Subscriber Package Menu ...

8      Custodial Package Menu ...

9      Print Other

10     Print Pending

11     Print Active

12     Print All

13     List Supported References

14     List Open Subscription

15     List Controlled Subscription

16     Subscribe to an Open Subscription Reference

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Integration Agreements Menu Option: **8** Custodial Package Menu

Select Custodial Package Menu Option: **?**

1      Print ACTIVE by Custodial Package

2      Print ALL by Custodial Package

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Custodial Package Menu Option: **1** Print ACTIVE by Custodial Package

Select PACKAGE NAME: LAB

1   LAB SERVICE          LR

2   LAB SITE CODE          LBAR

CHOOSE 1-2: 1

DEVICE: **(Enter Printer Name)**

**LAB SERVICE Custodial DBI Agreements **

-----------------------------------------------------------------------------

NAME: DBIA240-A             ENTRY: 240

CUSTODIAL PACKAGE: LAB SERVICE                  Dallas

SUBSCRIBING PACKAGE: AUTOMATED MED INFO           Albany

USAGE: Private            APPROVED: APPROVED

STATUS: Active              EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE: 63                     ROOT: LR(

DESCRIPTION:                        TYPE: File

Laboratory Package has given permission to AMIE to make the following

calls:

GLOBAL REF.    NODE;PIECE          USAGE

^LR(           "CH";11        Current Agreement number 95

"MI";11        Current Agreement number 95

^LR(D0,'CH',

^LR(D0,'MI',

ROUTINE:

This listing continues for many pages and will not be reproduced here.

#### Laboratory as a Subscriber

The Laboratory is also a subscriber to other packages for permission to use their entry points or information.

LAB SERVICE Integration Agreements subscribed to

------------------------------------------------------------

NAME: File 101              ENTRY: 872

CUSTODIAL PACKAGE: ORDER ENTRY/RESULT           Salt Lake City

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Controlled Subscri APPROVED: APPROVED

STATUS: Active              EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE: 101                    ROOT: ORD(101,

DESCRIPTION:                        TYPE: File

This file may be referenced by packages to maintain protocols within their

namespace. This file may also be pointed to.

ROUTINE:

********************

NAME: File 100.99           ENTRY: 874

CUSTODIAL PACKAGE: ORDER ENTRY/RESULT           Salt Lake City

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Controlled Subscri APPROVED: APPROVED

STATUS: Active              EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE: 100.99                 ROOT: ORD(100.99,

DESCRIPTION:                        TYPE: File

This file may be referenced by packages interfacing with OE/RR to see if

OE/RR has been installed in the manner:

I $D(^ORD(100.99)) ...

Packages may also setup entries in the Package Parameters portion of this file.

ROUTINE:

********************

NAME: DBIA916               ENTRY: 916

CUSTODIAL PACKAGE: VA FILEMAN                   San Francisco

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

For duration of Lab Version 5.2: Blood Bank and

Anatomic Pathology namespaced routines refer to

^DIC(file #,0,"GL") to locate global nodes for data.

USAGE: Controlled Subscri APPROVED: APPROVED

STATUS: Active              EXPIRES:

DURATION: Next Version        VERSION: Fileman 20

FILE:                        ROOT: DIC(

DESCRIPTION:                        TYPE: File

^DIC(D0,0,'GL')

1        GLOBAL NAME                 Direct Global Read

A direct global read is

performed on this node to

determine the global root for a file.

ROUTINE:

********************

NAME: File 100.98           ENTRY: 873

CUSTODIAL PACKAGE: ORDER ENTRY/RESULT           Salt Lake City

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Controlled Subscri APPROVED: APPROVED

STATUS: Pending             EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE: 100.98                 ROOT: ORD(100.98,

DESCRIPTION:                        TYPE: File

This file may be referenced to determine an appropriate Display Group for an order in the manner:

S ORTO=$O(^ORD(100.98,'B','OTHER HOSPITAL SERVICES',0))

ROUTINE:

********************

NAME: File 100.01           ENTRY: 875

CUSTODIAL PACKAGE: ORDER ENTRY/RESULT           Salt Lake City

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Controlled Subscri APPROVED: APPROVED

STATUS: Pending             EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE: 100.01                 ROOT: ORD(100.01,

DESCRIPTION:                        TYPE: File

This file may be pointed to.

ROUTINE:

********************

NAME: PSJEEU                ENTRY: 901

CUSTODIAL PACKAGE: INPATIENT MEDICATI           Birmingham

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Controlled Subscri APPROVED: APPROVED

STATUS: Active              EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE:                        ROOT:

DESCRIPTION:                        TYPE: Routine

This is a set of utilities that can be used to create, validate and

process order timing schedules.

ROUTINE: PSJEEU

COMPONENT:  ENSE

VARIABLES:  PSJPP       Input

This is the package prefix as found in

the PACKAGE file (9.4).

PSJSHLS     Input

This is executable code that sets $T to

be used to screen Hospital Locations when

editing schedules and shifts. If PSJSHLS

exists, DIC("S") is set to PSJSHLS. The

scheduler will not try to validate

PSJSHLS.

Allows the editing of the ADMINISTRATION SCHEDULE file (51.1)

COMPONENT:  ENSHE

VARIABLES:  PSJPP       Input

This is the package prefix as found in

the PACKAGE file (9.4).

PSJSHLS     Input

This is executable code that sets $T to

be used to screen Hospital Locations when

editing schedules and shifts. If PSJSHLS

exists, DIC("S") is set to PSJSHLS. The

scheduler will not try to validate

PSJSHLS.

Allows the editing of the ADMINISTRATION SHIFT file (51.15).

COMPONENT:  ENSVI

VARIABLES:  PSJPP       Input

This is the package prefix as found in

the PACKAGE file (9.4).

PSJX        Input

This is the schdule to be viewed. If only

the first few characters of the schedule

name is entered, the user will be asked

to select from all schedules in the

ADMINISTRATION SCHEDULE file (51.1)

beginning with these characters. If a

valid schedule is selected, information

pertaining to the schedule will be

displayed.

View standard schedule information.

COMPONENT:  ENSV

VARIABLES:  PSJX        Both

This is the schdule to be validated. If

only the first few characters of the

schedule name is entered, the user will

be asked to select from all schedules in

the ADMINISTRATION SCHEDULE file (51.1)

beginning with these characters. If a

valid schedule is selected, it's name

will will be returned in PSJX. If a valid

schedule is not selected, PSJX will be

killed.

PSJPP       Input

This is the package prefix as found in

the PACKAGE file (9.4).

PSJM        Output

This is the frequency in minutes that the

action is to be taken. This will be null

if PSGX is invalid.

PSJAT       Output

These are the administration times or

shifts that are associated with the

selected schedule. This will be null if

PSGX is invalid.

PSJY        Output

This is a pointer to the ADMINISTRATION

SCHEDULE file (51.1) if PSJX is found in

the file. This will be null if PSJX is

invalid or not found.

PSJTS       Output

This is a code representing the type of

schedule. This will be null if the

schedule is invalid.

PSJAX       Output

This is the maximum days continuous

orders last for the selected schedule, or

null if not found.

PSJW        Input

This is a pointer to the HOSPITAL

LOCATION file (44). This is an optional

variable that may be used to determine

the administration times or shifts by

location.

PSJNE       Input

If this optional variable is defined,

there is no dialogue with the user.

Validates a schedule and gives the administration times or

shifts and frequency (in minutes) of the schedule.

COMPONENT:  ENATV

VARIABLES:  X           Both

This contains the administration times to

be validated. X will be killed if the

administration times are invalid.

Validates administration times. This may be used in an input transform.

COMPONENT:  ENSHV

VARIABLES:  X           Both

This should be set to the administration

shift to be validated. If the

administration shift passed in X is

invalid, X will be killed.

Validates shifts. If the shift passed in X is invalid X will be killed.

COMPONENT:  ENSPU

VARIABLES:  PSJSCH      Input

This is the schedule to be processed.

PSJM        Input

This is the frequency (in minutes) that

an action is to take place. Used for

continuous and range schedules.

PSJAT       Input

This is either a set of administration

times or shifts, depending on the type of

schedule. If it is administration times,

it will be similar to:

PSJAT="04-08-12-16-20". If it is shifts,

it will be similar to:

PSJAT="M-E",PSJAT("M")="05-11",PSJAT("E")="1 8-22".

PSJTS       Input

This is a code representing the type of

schedule defined in PSJSCH. The codes

are: C - CONTINUE; D - DAY OF THE WEEK;

DR - DAY OF THE WEEK-RANGE; O - ONE-TIME;

R - RANGE; and S - SHIFT.

PSJSD       Input

This is the start date/time of the order.

PSJFD       Input

This is the stop date/time of the period

where the action is to take place.

PSJOSD      Input

This is the start date/time of the order.

If PSJOSD is not found, PSJSD is used.

PSJOFD      Input

This is the stop date/time of the order

(action to take place). If PSJOFD is not

found, PSJFD is used.

PSJC        Output

This is the number of times (and when) an

action is to take place. Calculates the number of times (and when) an action is to take place.

COMPONENT:  ENDSD

VARIABLES:  PSJSCH      Input

This is the name of the schedule to be

used in determining the start date/time.

PSJAT       Input

This is either a set of administration

times or shifts, depending on the type of

schedule. If it is administration times,

it will be similar to:

PSJAT="04-08-12-16-20". If it is shifts,

it will be similar to:

PSJAT="M-E",PSJAT("M")="05-11",PSJAT("E")="1 8-22".

PSJTS       Input

This is a code representing the type of

schedule defined in PSJSCH. The codes

are: C - CONTINUE; D - DAY OF THE WEEK;

DR - DAY OF THE WEEK-RANGE; O - ONE-TIME;

R - RANGE; and S - SHIFT.

PSJX        Output

This will be returned as either a

date/time in VA FileMan interal format,

or null if the start date/time cannot be

calculated. Provides a date/time that might be used as a default value for the start date of an order.

********************

NAME: OR                    ENTRY: 861

CUSTODIAL PACKAGE: ORDER ENTRY/RESULT           Salt Lake City

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Controlled Subscri APPROVED:

STATUS: Pending             EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE:                        ROOT:

DESCRIPTION:                        TYPE: Routine

ROUTINE: OR

COMPONENT:  EN

VARIABLES:  X           Input

Variable pointer of the protocol.

OE/RR Processor. This is the main entry point to run the

OE/RR program.  It is called with X set as a variable

pointer to the initial protocol.

********************

NAME: ORUHDR                ENTRY: 862

CUSTODIAL PACKAGE: ORDER ENTRY/RESULT           Salt Lake City

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Controlled Subscri APPROVED:

STATUS: Pending             EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE:                        ROOT:

DESCRIPTION:                        TYPE: Routine

ROUTINE: ORUHDR

COMPONENT:  EXT

VARIABLES:  ORIFN       Both

Internal number in file 100 of the order

to display.

ORAGE       Output

Patient age.

ORIO        Output

ORANSI      Output

ORDOB       Output

Patient Date of Birth

ORFT        Output

ORHI        Output

ORNP        Output

Pointer to file 200 for Current

Agent/Provider

ORL         Output

Variable pointer to the variable pointer.

ORPD        Output

ORPNM       Output

Patient name

ORPV        Output

Pointer to Provider file for the person

requesting the order.

ORSEQ       Output

ORSEX       Output

Patient sex.

ORSSN       Output

Patient SSN

ORTIT       Output

Title

ORTS        Output

Pointer to Treating Specialty associated

with the order.

ORVP        Output

Variable pointer toe object of an order.

ORWARD      Output

Inpatient Ward location. Displays a standard header for detailed order displays. If calling this from within OE/RR, it is not necessary to killthe returned variables.  OE/RR will kill them.

COMPONENT:  PGBRK

VARIABLES:  DIROUT      Output

User entered a '^^'

OREND       Output

User entered a '^'

Displays 'Press return to continue or "^" to escape' at

page breaks.

********************

NAME: ORUPREF2              ENTRY: 863

CUSTODIAL PACKAGE: ORDER ENTRY/RESULT           Salt Lake City

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Controlled Subscri APPROVED:

STATUS: Pending             EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE:                        ROOT:

DESCRIPTION:                        TYPE: Routine

ROUTINE: ORUPREF2

COMPONENT:  EN3

VARIABLES:  ORPKG       Input

Package pointer.

ORDEF       Input

Default protocol for setting up protocols.

ORFL        Input

File link - variable pointer for procedure

file.

ORDANM      Input

Optional name of the protocol.

ORDA        Input

Internal number of an existing protocol

to be updated.

OREA        Input

Action used in lieu of default defined in

OROEF

ORTXT       Input

Name of protocol; if not defined, the .01

filed of the procedure referenced is used.

Utility for 'on-the-fly' protocol creation.  See OE/RR Developers guide.

********************

NAME: ORUTL                 ENTRY: 864

CUSTODIAL PACKAGE: ORDER ENTRY/RESULT           Salt Lake City

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Controlled Subscri APPROVED:

STATUS: Pending             EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE:                        ROOT:

DESCRIPTION:                        TYPE: Routine

ROUTINE: ORUTL

COMPONENT:  READ

VARIABLES:

********************

NAME: ORVOM                 ENTRY: 865

CUSTODIAL PACKAGE: ORDER ENTRY/RESULT           Salt Lake City

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Controlled Subscri APPROVED:

STATUS: Pending             EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE:                        ROOT:

DESCRIPTION:                        TYPE: Routine

ROUTINE: ORVOM

********************

NAME: ORX                   ENTRY: 866

CUSTODIAL PACKAGE: ORDER ENTRY/RESULT           Salt Lake City

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Controlled Subscri APPROVED: APPROVED

STATUS: Pending             EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE:                        ROOT:

DESCRIPTION:                        TYPE: Routine

ROUTINE: ORX

COMPONENT:  FILE

VARIABLES:  OREPDUZ     Input

DUZ of the person entering the order.

ORL         Input

Variable pointer to the variable pointer.

ORPCL       Input

Variable pointer to the protocol that

created the order.

ORNP        Input

Pointer to file 200 for Current

Agent/Provider

ORVP        Input

Variable pointer to the object of an

order.

ORCOST      Input

Cost of the order

OREVENT     Input

Two piece variable delimited by a

semicolon.  The first piece is the time

at which an event should occur.  The

second piece is a character that has

meaning to a package.

ORIT        Input

Variable pointer to the item ordered.

ORLOG       Input

Time the order is entered.

ORPK        Input

Package reference defined by the package

when an order is created.

ORPURG      Input

Grace days before an order is purged.

ORSTOP      Input

Order Stop Date

ORSTRT      Input

Order start date

ORSTS       Input

Order status

ORTO        Input

Pointer to Display Group file. Identifies

the service receiving the order.

ORTS        Input

Pointer to Treating Specialty associated

with the order.

ORTX(i)     Input

Order Text.

ORIFN       Output

Internal entry number of order in file

100

COMPONENT:  RETURN

VARIABLES:  ORIFN       Input

Internal entry number of order.

ORETURN(OR  Input

Cost of the order.

ORETURN(OR  Input

Two piece variable delimited by a

semicolon.  The first piece is the time

at which an event should occur.  The

second piece is a character that has

meaning to a package.

ORETURN(OR  Input

Variable pointer to the item ordered.

ORETURN(OR  Input

Free text, package defined reference.

ORETURN(OR  Input

Grace period before purging order.

ORETURN(OR  Input

Pointer to file 200 for Current

Agent/Provider

ORETURN(OR  Input

Stop Date

ORETURN(OR  Input

Start Date

ORETURN(OR  Input

Pointer to Order Status

ORETURN(OR  Input

Order Text

COMPONENT:  ST

VARIABLES:  ORIFN       Input

Internal entry number of the order.

ORSTS       Input

Order Status

********************

NAME: ORX2                  ENTRY: 867

CUSTODIAL PACKAGE: ORDER ENTRY/RESULT           Salt Lake City

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Controlled Subscri APPROVED:

STATUS: Pending             EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE:                        ROOT:

DESCRIPTION:                        TYPE: Routine

ROUTINE: ORX2

COMPONENT:  LK

VARIABLES:  X           Input

Variable pointer of patient.

Y           Output

Y=1 if lock is successful, 0 if failed.

Used when updating orders for a patient to check that

someone else is not also updating orders at the same time

for the same patient.  This will attempt to set a software

lock on the patient.  Applications using this entry point

must also call the entry point ULK^ORX2 to unlock the

patient when the updating process is finished.

COMPONENT:  ULK

VARIABLES:  X           Input

Variable pointer to the patient.

Used in conjunction with the entry point LK^ORX2 to unlock

a patient during the process of adding orders.  Do not call

this entry point unless you have already successfully

locked the patient.

********************

NAME: ORX3                  ENTRY: 868

CUSTODIAL PACKAGE: ORDER ENTRY/RESULT           Salt Lake City

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Controlled Subscri APPROVED:

STATUS: Pending             EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE:                        ROOT:

DESCRIPTION:                        TYPE: Routine

ROUTINE: ORX3

COMPONENT:  NOTE

VARIABLES:  ORNOTE(i)   Input

i=internal # of the notification

ORVP        Input

Variable pointer to the patient.

ORIFN       Input

Order number that you want this

notification to linked to.

This is an entry point that creates a notification for a

package.

********************

NAME: ORX5                  ENTRY: 869

CUSTODIAL PACKAGE: ORDER ENTRY/RESULT           Salt Lake City

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Controlled Subscri APPROVED:

STATUS: Pending             EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE:                        ROOT:

DESCRIPTION:                        TYPE: Routine

ROUTINE: ORX5

COMPONENT:  DC

VARIABLES:  ORIFN       Input

Pointer to the order.

This entry is called when a package needs to create a DC

order.

COMPONENT:  HOLD

VARIABLES:  ORIFN       Input

Pointer to the order.

This entry is called when a package needs to place a HOLD

on an ordered item.

********************

NAME: ORX7                  ENTRY: 870

CUSTODIAL PACKAGE: ORDER ENTRY/RESULT           Salt Lake City

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Controlled Subscri APPROVED:

STATUS: Pending             EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE:                        ROOT:

DESCRIPTION:                        TYPE: Routine

ROUTINE: ORX7

COMPONENT:  DC

VARIABLES:  ORIFN       Input

Pointer to the order.

ORNATR      Input

Identifies the Nature of Order.

This entry point is provided for orders that are discontinued

by the service. This creates a DC order for the order

identified by ORIFN.

********************

NAME: ORX8                  ENTRY: 871

CUSTODIAL PACKAGE: ORDER ENTRY/RESULT           Salt Lake City

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Controlled Subscri APPROVED: APPROVED

STATUS: Pending             EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE:                        ROOT:

DESCRIPTION:                        TYPE: Routine

ROUTINE: ORX8

COMPONENT:  EN(ORIFN)

VARIABLES:  ORIFN       Input

Pointer to the order.

ORUPCHUK('  Output

=WHO ENTERED^External Format

ORUPCHUK('  Output

=PATIENT LOCATION

ORUPCHUK('  Output

=CURRENT AGENT/PROVIDER^External format

ORUPCHUK('  Output

=WHEN ENTERED

ORUPCHUK('  Output

=PROTOCOL

ORUPCHUK('  Output

=CURRENT AGENT/PROVIDER^External Format

ORUPCHUK('  Output

=STOP DATE

ORUPCHUK('  Output

=CURRENT START DATE

ORUPCHUK('  Output

=STATUS^External format

ORUPCHUK('  Output

=TO (display group)^External Format

ORUPCHUK('  Output

=ORDER TEXT (Multiple)

ORUPCHUK('  Output

=OBJECT OF ORDER

This entry point returns data from the Order file (100) for

a particular order.

COMPONENT:  NOTIF(ORIFN,ORNOTE)

VARIABLES:  ORIFN       Input

Pointer to the order

ORNOTE      Input

Pointer to the notification

********************

NAME: DBIA13                ENTRY: 13

CUSTODIAL PACKAGE: REGISTRATION                 Albany

SUBSCRIBING PACKAGE: LAB SERVICE                  Salt Lake City

USAGE: Private            APPROVED: APPROVED

STATUS: Active              EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE: 2                      ROOT: DPT(

DESCRIPTION:                        TYPE: File

PATIENT NODE .35 - DEATH INFO USED TO STUFF ^LR( GLOBAL.

^DPT(dfn,.35)

.351     DATE OF DEATH        .35;1    Direct Global Write

.352     DEATH ENTERED BY     .35;2    Direct Global Write

ROUTINE:

********************

NAME: DBIA29                ENTRY: 29

CUSTODIAL PACKAGE: VA FILEMAN                   San Francisco

SUBSCRIBING PACKAGE: LAB SERVICE                  Salt Lake City

USAGE: Private            APPROVED: APPROVED

STATUS: Active              EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE:                        ROOT: DD(

DESCRIPTION:                        TYPE: File

Routines LRWU5 &amp; LRWU7 Do direct sets to the Data Dictionary.  The

routines allow the user to add a new Data Name or Antibiotic without

giving programmer access.

ROUTINE:

********************

NAME: DBIA327               ENTRY: 327

CUSTODIAL PACKAGE: VA FILEMAN                   San Francisco

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Private            APPROVED: APPROVED

STATUS: Active              EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE: .401                   ROOT: DIBT(

DESCRIPTION:                        TYPE: File

Laboratory V5.2 (only V5.2) is granted the following exemption:

The laboratory is supplying a pre release 5.2 patch. The patch will allow

the site to mimic the conversion process required for V5.2 install. As a

part of the process a FileMan sort template is created of all providers

the software was unable to repoint to VA(200.

The creation of the sort template is done with a DIC call and a DR string.

We are not aware of a method to load the actual data. Therefore, this

function is hard coded.

The exemption is only required for the one time conversion process. Listed

below is the actual code involved. Please advise of any suggestion you

feel will be of benefit.

EXCEPT(LRFILE,LRD0)     ;- LOGS EXCEPTIONS FROM THE CONVERSIONS OF DATA

FROM 6 A ND 16

; exceptions are put into a SORT template so the the site can

; then use fileman enter edit to correct problems found.

;

N DIC,LRSORT,X,Y

I '$D(^DIBT("B",LRFILE\_"-EXCEPTIONS")) D ADD

I '$D(LRSORT) S LRSORT=$O(^DIBT("B",LRFILE\_"-EXCEPTIONS",0))

S ^DIBT(LRSORT,1,LRD0)=""

Q

;

ADD     ; add a new sort template to be used for exception logging and

editing

N X,Y

S DIC="^DIBT(",DIC(0)="L",DIC("DR")="2///^S X=""T"";4///^S X=$P(LR

FILE," "-"",2);5///^S X=0;"

S X=LRFILE\_"-EXCEPTIONS" D FILE^DICN S LRSORT=+Y

Q

ROUTINE:

********************

NAME: DBIA98-B              ENTRY: 561

CUSTODIAL PACKAGE: TASK-MANAGER QUEUE           San Francisco

SUBSCRIBING PACKAGE: LAB SERVICE                  Salt Lake City

USAGE: Private            APPROVED: APPROVED

STATUS: Active              EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE:                        ROOT: %ZTSK(

DESCRIPTION:                        TYPE: File

Version 5.1 of the laboratory package has a temporary agreement for the

following:

2) To reference the global %ZTSK directly to display the error trap data.

(Rick has been notified of our usage of the %ZTSK global)

When Kernel release their error trapping system, Lab will convert to the

Kernel supported methodology.

ROUTINE:

********************

NAME: DBIA912               ENTRY: 912

CUSTODIAL PACKAGE: VA FILEMAN                   San Francisco

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Private            APPROVED: APPROVED

STATUS: Active              EXPIRES:

DURATION: Next Version        VERSION: Fileman 20

FILE:                        ROOT: DIC(

DESCRIPTION:                        TYPE: File

^DIC("AC" - Screen lookup on files for the Lab application group.

^DIC("AC","LR"

ROUTINE:

********************

NAME: DBIA913               ENTRY: 913

CUSTODIAL PACKAGE: REGISTRATION                 Albany

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Private            APPROVED: APPROVED

STATUS: Active              EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE: 21                     ROOT: DIC(21

DESCRIPTION:                        TYPE: File

In Lab V 5.2 patient Persian Gulf information is being obtained from

inquiries to global locations.  Routines LRAPPOW and LRAPDPT reference the

globals ^DIC(21, .

^DIC(21,

.01      NAME                 0;1      Direct Global Read

ROUTINE:

********************

NAME: DBIA917               ENTRY: 917

CUSTODIAL PACKAGE: VA FILEMAN                   San Francisco

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Private            APPROVED: APPROVED

STATUS: Active              EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE:                        ROOT: DISV(

DESCRIPTION:                        TYPE: File

Laboratory V 5.2 uses ^DISV(DUZ,"LRACC") and ^DISV(DUZ,"LRAN") to store

items.

An example is in routine LRACC at line LRACC+4:

S:$L(X)&gt;2 ^DISV(DUZ,"LRACC")=X S:X=" " X=$S($D(^DISV(DUZ,"LRACC")):

^("LRACC"),1:"?")

Lab needs an agreement for read/write access to ^DISV(DUZ,"LRACC") and

^DISV(DUZ,"LRAN")

ROUTINE:

********************

NAME: DBIA918               ENTRY: 918

CUSTODIAL PACKAGE: REGISTRATION                 Albany

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Private            APPROVED: APPROVED

STATUS: Active              EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE: 2                      ROOT: DPT(

DESCRIPTION:                        TYPE: File

Read only access for the ^DPT( global to obtain Period of Service and POW

information.

Read ^DPT(dfn,.52) to obtain POW information.

Read ^DPT(dfn,.32) to obtain Period of Service information.

^DPT(dfn,.52)

.525     POW STATUS INDICATED .52;5    Direct Global Read

.526     POW CONFINEMENT LOCA .52;6    Direct Global Read

^DPT(dfn,.32)

.323     PERIOD OF SERVICE    .32;3    Direct Global Read

ROUTINE:

********************

NAME: DBIA921               ENTRY: 921

CUSTODIAL PACKAGE: PHARMACY                     Birmingham

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Private            APPROVED: APPROVED

STATUS: Active              EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE: 52.6                   ROOT: PS(52.6,

DESCRIPTION:                        TYPE: File

Read only access for the ^PS(52.6,X,0) node.

In routines LRBLPE1 and LRBLPH:

...I $D(^PS(52.6,X,0)...W !,"IV DRUG: ",$P(^(0),"^")

^PS(52.6,x,0)

.01      PRINT NAME           0;1      Direct Global Read

ROUTINE:

********************

NAME: DBIA923               ENTRY: 923

CUSTODIAL PACKAGE: SCHEDULING                   Albany

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Private            APPROVED: APPROVED

STATUS: Active              EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE: 40.7                   ROOT: DIC(40.7

DESCRIPTION:                        TYPE: File

The following fields are accessed in a read-only manner:

^DIC(      40.7      STOP CODE file

1    AMIS REPORTING STOP CODE

In routines LRCAPPH line LRCAPPH+8

SDC     S SDC=$S($P(^("NITE"),U,3):$G(^DIC(40.7,+$P(^LAB(69.9,1,"NITE"),

U,3),0)),1:"") S LRSDC=$S($P(SDC,U,2):+$P(SDC,U,2),1:108)

LRSTOPC line LRSTOPC+3

S

LRSDC=$S(+$P($G(^DIC(40.7,+$P($G(^LAB(69.9,1,"NITE")),U,3),0)),U,2):

$P(^(0),U,2),1:108),CNT=0,LREND=0

Routine LRSTOPC manually records clinic stop codes for Lab.  Routine

LRCAPPH automatically records clinic stop codes for Lab.

ROUTINE:

********************

NAME: DBIA924               ENTRY: 924

CUSTODIAL PACKAGE: REGISTRATION                 Albany

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Private            APPROVED: APPROVED

STATUS: Active              EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE: 11                     ROOT: DIC(11,

DESCRIPTION:                        TYPE: File

Read only access for the ^DIC(11, global.

In routine LRMIHDR line LRMIHDR+22:

I LRMARST S LRMARST=$S($D(^DIC(11,LRMARST,0)):$P(^(0),U),1:"")

^DIC(11,D0,0)

.01      NAME                 0;1      Direct Global Read

ROUTINE:

********************

NAME: DBIA925               ENTRY: 925

CUSTODIAL PACKAGE: REGISTRATION                 Albany

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Private            APPROVED: APPROVED

STATUS: Active              EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE: 10                     ROOT: DIC(10,

DESCRIPTION:                        TYPE: File

Read only access to the ^DIC(10, global.

In routine LRMIHDR line LRMIHDR+21:

I LRRACE S LRRACE=$S($D(^DIC(10,LRRACE,0)):$P(^(0),U),1:"")

^DIC(10,D0,0)

.01      NAME                 0;1      Direct Global Read

ROUTINE:

********************

NAME: DBIA931               ENTRY: 931

CUSTODIAL PACKAGE: REGISTRATION                 Albany

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Private            APPROVED: APPROVED

STATUS: Active              EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE: 81                     ROOT: ICPT(

DESCRIPTION:                        TYPE: File

Direct read access to the ^ICPT( global, CPT file #81.

In routine LRBLPCSS, Blood Bank Pre-op Component selection,

read node ^ICPT(x,"D",z,0) to print description field.

In routine LRBLPOST, Blood Bank Post-init, read node ^ICPT(x,"LR").  This

will move all 66 fields to our own field in ^LAB(66.5, .  This is one time

for V. 5.2 installation only.

^ICPT(x,'D',z,0)

.01      DESCRIPTION          0;1      Direct Global Read

^ICPT(x,'LR',y,0)

66       BLOOD COMPONENT REQU 0;1      Direct Global Read

ROUTINE:

********************

NAME: DBIA935               ENTRY: 935

CUSTODIAL PACKAGE: REGISTRATION                 Albany

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Private            APPROVED: APPROVED

STATUS: Active              EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE: 22                     ROOT: DIC(22,

DESCRIPTION:                        TYPE: File

In Lab V 5.2 patient POW information is being obtained from inquiries to

global locations.  Routines LRAPPOW and LRAPDPT reference the global

^DIC(22, .

^DIC(22

.01      NAME                 0;1      Direct Global Read

ROUTINE:

********************

NAME: DBIA908               ENTRY: 908

CUSTODIAL PACKAGE: SCHEDULING                   Albany

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Private            APPROVED:

STATUS: Pending             EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE: 44                     ROOT: SC(

DESCRIPTION:                        TYPE: File

Read only access for the ^SC global.

Read ^SC(n,0) to obtain Hospital Location name and abbreviation.

TREATING SPECIALTY used as pointer to 45.7 FACILITY TREATING

SPECIALTY, ^DIC(45.7,TREATING SPECIALTY,0), which is

used as pointer to file 42.4, SPECIALTY,

^DIC(42.4,FACILITY TREATING SPECIALTY,0)

Read ^SC("B", and ^SC("C", cross references to get patient location

internal entry #: $O(^SC("B",X,0)) and $O(^SC("C",X,0)).

Read access to the ^SC(D0,"I") node to obtain inactivate date

(field # 2505) and re-activate date (field # 2506).

Read only access to ^SC(D0,"S",D1,1,D2,0) to access patients by

clinic location and clinic date to print lab report.

Read only access to ^SC(D0,"S",DATE) used to check if a clinic

meets on a specified date.

^SC(D0,0)

.01      NAME                 0;1      Direct Global Read

1        ABBREVIATION         0;2      Direct Global Read

3        INSTITUTION          0;4      Direct Global Read

9.5      TREATING SPECIALTY   0;20     Direct Global Read

2        TYPE                 0;3      Direct Global Read

^SC(D0,'I')

2505     INACTIVATE DATE      I;1      Direct Global Read

2506     REACTIVATE DATE      I;2      Direct Global Read

^SC('B',

.01      NAME                          Direct Global Read

B Cross Reference

^SC('C',

1        ABBREVIATION                  Direct Global Read

C Cross Reference

^SC(D0,'S',D1,1,D2,0)

ROUTINE:

********************

NAME: DBIA920               ENTRY: 920

CUSTODIAL PACKAGE: PHARMACY                     Birmingham

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Private            APPROVED:

STATUS: Pending             EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE: 52                     ROOT: PSRX(

DESCRIPTION:                        TYPE: File

Read only access for the ^PSRX(x,0) node.

In routines LRBLPE1 and LRBLPH:

...I $D(^PSRX(Y,0)) S ^TMP($J,+$P(^(0),"^",6))=O

^PSRX(x,0)

6        DRUG                 0;6      Direct Global Read

ROUTINE:

********************

NAME: DBIA922               ENTRY: 922

CUSTODIAL PACKAGE: PHARMACY                     Birmingham

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Private            APPROVED:

STATUS: Pending             EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE: 55                     ROOT: PS(55

DESCRIPTION:                        TYPE: File

Read only access to the following nodes in the Pharmacy Patient file #55.

All these references are found in routines LRBLPE1 and LRBLPH.

^PS(55,DFN,"IV",X,"AD",Y,0)

K ^TMP($J) F X=0:0 S X=$O(^PS(55,DFN,"IV",X)) Q:'X!(R[U)  F Y=0:0

S Y=$O(^PS(55,DFN,"IV",X,"AD",Y)) Q:'Y!(R[U)  S ^TMP($J,+^(Y,0))=""

^PS(55,DFN,5,X,1,Y,0)

K ^TMP($J) F X=0:0 S X=$O(^PS(55,DFN,5,X)) Q:'X!(R[U)  F Y=0:0

S Y=$O(^PS(55,DFN,X,1,Y)) Q:'Y!(R[U)  S ^TMP($J,+^(Y,0)=""

^PS(55,dfn,'IV',x,'AD',y,0)

.01      ADDITIVE             0;1      Direct Global Read

^PS(55,dfn,5,x,1,y,0)

.01      DRUG                 0;1      Direct Global Read

ROUTINE:

********************

NAME: DBIA927               ENTRY: 927

CUSTODIAL PACKAGE: SURGERY                      Birmingham

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Private            APPROVED:

STATUS: Pending             EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE: 130                    ROOT: SRF(

DESCRIPTION:                        TYPE: File

Read only access for the ^SRF global.

Routine LRBLPCSS, blood bank routine, pre-op component selection,

checks for pending operations by looping through the "ADT" Date of

Operation cross reference then lists operations scheduled.  The date,

operation procedure, and principal procedure code is listed.

^SRF('ADT',dfn,x,a)

.09      DATE OF OPERATION    0;9      Direct Global Read

Loop through this

cross-reference to list

operations scheduled.

^SRF(DO,'OP')

Direct Read Access to print operation procedure and code.

ROUTINE:

********************

NAME: DBIA995               ENTRY: 995

CUSTODIAL PACKAGE: OUTPATIENT PHARMAC           Birmingham

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Private            APPROVED:

STATUS: Pending             EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE: 55                     ROOT: PS(55,

DESCRIPTION:                        TYPE: File

Read only access to the following nodes in the Pharmacy Patient file #55.

This reference is found in routines LRBLPE1 and LRBLPH.

^PS(55,DFN,"P",X,0)

F X=0:0 S X=$O(^PS(55,DFN,"P",X)) Q:'X  I $D(^(X,0)) S Y=+^(0)

I $D(^PSRX(Y,0))...

^PS(55,DFN,'P',X,0)

.01      PRESCRIPTION PROFILE 0;1      Direct Global Read

ROUTINE:

********************

NAME: DBIA999               ENTRY: 999

CUSTODIAL PACKAGE: VA FILEMAN                   San Francisco

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Private            APPROVED:

STATUS: Pending             EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE:                        ROOT: DD(

DESCRIPTION:                        TYPE: File

Read only access for the ^DD( Global.

ROUTINE:

********************

NAME: DBIA98-A              ENTRY: 98

CUSTODIAL PACKAGE: TASK-MANAGER QUEUE           San Francisco

SUBSCRIBING PACKAGE: LAB SERVICE                  Salt Lake City

USAGE: Private            APPROVED: APPROVED

STATUS: Active              EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE:                        ROOT:

DESCRIPTION:                        TYPE: Other

Version 5.1 of the laboratory package has a temporary agreement for the

following:

1) To save system $Z variables in local variables for storage  in our

error trap.

When Kernel release their error trapping system, Lab will convert to the

Kernel supported methodology.

ROUTINE:

********************

NAME: DBIA893               ENTRY: 893

CUSTODIAL PACKAGE: SURGERY                      Birmingham

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Private            APPROVED: APPROVED

STATUS: Active              EXPIRES:

DURATION: Next Version        VERSION:

FILE:                        ROOT:

DESCRIPTION:                        TYPE: Other

The LRSPOLR* routines were written by Alan Monosky (surgery developer) to

provide an interface with the Surgery software. These routines have been

changed to SROSPLG* and will reside in the Surgery namespace. An

integration agreement is requested so as to export these routines with

Version 5.2 of the Lab Package. Changes were made to Lab Routine LRAPLG

which references LRSPOLR.

ROUTINE: SR0SPLG*

********************

NAME: DBIA910               ENTRY: 910

CUSTODIAL PACKAGE: MAILMAN                      Washington

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Private            APPROVED:

STATUS: Pending             EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE:                        ROOT:

DESCRIPTION:                        TYPE: Other

Lab is requesting a new domain for the purpose of uploading a monthly

laboratory workload reports to Austin.  The increase in traffic should be

less than 30K per institution once per month.  Typically a message is

about 200 lines.

NAME: Q-LMI.VA.GOV                  FLAGS: S

RELAY DOMAIN: FOC-AUSTIN.VA.GOV  DHCP ROUTING INDICATOR:LAB

PHYSICAL LINK DEVICE:  MINIOUT TRANSMISSION SCRIPT: SCRIPT TEXT:

ROUTINE:

********************

NAME: DBIA911               ENTRY: 911

CUSTODIAL PACKAGE: KERNEL                       San Francisco

SUBSCRIBING PACKAGE: LAB SERVICE                  Dallas

USAGE: Private            APPROVED:

STATUS: Pending             EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE:                        ROOT:

DESCRIPTION:                        TYPE: Other

Lab requests a sharing agreement to export the Diagram Menus (XUUSERACC)

option within the LAB LIAISON (LRLIAISON) menu.

ROUTINE:

********************

NAME: DBIA83                ENTRY: 83

CUSTODIAL PACKAGE: SCHEDULING                   Albany

SUBSCRIBING PACKAGE: LAB SERVICE                  Salt Lake City

USAGE: Private            APPROVED: APPROVED

STATUS: Active              EXPIRES:

DURATION: Till Otherwise Agr  VERSION:

FILE:                        ROOT:

DESCRIPTION:                        TYPE: Routine

Lab uses suported call EN3^SDACS for adding stop codes.

ROUTINE: SDACS

COMPONENT:  EN3

VARIABLES:

********************

INTERNAL RELATIONS

## 6 Internal Relations

The Menu Entry Action, D ^LRPARAM, must be on any menu entry to Laboratory options (it only needs to be at the highest menu). Likewise, the Menu Exit Action D ^LRKILL must be on the same highest menus.

### 54 Stand Alone Menus

The following menus have menu actions necessary for their proper functioning. Items on these menus must not be moved without incorporating the appropriate actions.

LA INTERFACE	Lab interface menu	Menu Entry Action: D ^LAJOB1

LRMENU	Laboratory	Menu Entry Action: D ^LRPARAM

Menu Exit Action: D ^LRKILL

LRMI	Microbiology menu	Menu Exit Action: K A,Z

LRUAC	Print accession list(s)	None

LRBL	Blood Bank Menu	Menu Entry Action: S IOP

=“HOME” D ^%ZIS W

@IOF,?35,“BLOOD BANK”

LR INTEGRITY	Lab Routine Integrity	None

Menu

The global reference, ^LAC($J, is used for temporary storage of data while reprinting a permanent page from the cumulative.

The global references ^LA(and ^LAH(is used for Auto Instrument and workload functions (non FileMan compatible).

All of the routines, files, and options within the Laboratory V. 5.2 software package are within SACC programming requirements.

PACKAGE-WIDE VARIABLES

## 7 Package-Wide Variables

Laboratory V. 5.2 package wide variables are created by the routine LRPARAM. A call to this routine should be placed on the highest Laboratory User Menu in the entry field. Laboratory local variables are deleted by the routine LRKILL. A call to this routine should be placed as an exit action on the highest Laboratory User Menu.

LRBLOOD	Default specimen type for blood

LRLABKY	Variable to indicate if the user has certain security keys

Variable is defined if the user holds LRLAB key

1st piece by ^ is 1 if user holds LRVERIFY

2nd piece by ^ is 1 if user holds LRSUPERVISOR

3rd piece by ^ is 1 if user holds LRLAISON

LRORN	Set to 1 if OE/RR is activated

LRPARM	Set to 1 concatenated with 2-255 pieces of the ^LRO(69.9,1,0) 	globals contains information from the LABORATORY SITE file

LRPARM(VR)	The version number of Laboratory Package installed

LRPLASMA	Default plasma specimen type

LRSERUM	Default serum specimen type

LRUNKNOW	Default unknown specimen type

LRURINE	Default urine specimen type

LRVIDO	Escape sequence required to turn on reverse video and video blink

LRVIDOF	Escape sequence required to turn off LRVIDO action

SACC EXEMPTIONS LIST

4    STANDARD SECTION:   4B          Package-wide variables

DATE GRANTED:

LRBLOOD, LRDT0, LRORN, LRPARAM, LRPLASMA, LRUNKNOW, LRSERUM, and LRURINE are package-wide variables for use within LAB.


STANDARDS AND CONVENTIONS COMMITTEE (SACC) EXEMPTIONS

## 8 Standards and Conventions Committee (SACC) Exemptions

SACC EXEMPTIONS LIST                           JUL 28,1994  15:33    PAGE 1

-----------------------------------------------------------------------------

LAB SERVICE

1    STANDARD SECTION:   6D          FM compatibility

DATE GRANTED:

The LA global is exempted from VA FileMan compatibility.  It holds

raw data from automated instruments.

2    STANDARD SECTION:   6D          FM compatibility

DATE GRANTED:

The LAH global is exempted from VA FileMan compatibility.  It holds

the raw data while it is being processed.

3    STANDARD SECTION:   2A          OPEN, CLOSE device

DATE GRANTED:

Laboratory, when dealing with automated instruments, may issue

direct OPENs and CLOSEs of devices.

4    STANDARD SECTION:   4B          Package-wide variables

DATE GRANTED:

LRBLOOD, LRDT0, LRORN, LRPARAM, LRPLASMA, LRUNKNOW, LRSERUM, and

LRURINE are package-wide variables for use within LAB.

5    STANDARD SECTION:   5C          Vendor specific routines

DATE GRANTED:

The Laboratory package has a temporary exemption to use a vendor

specific routine, %ET, to capture errors during background data

processing.  It is only used during interfaced instrument data

processing.  When Kernel provides the needed functionality

Laboratory will discontinue use of %ET.

6    STANDARD SECTION:   2D2         * &amp; # READs

DATE GRANTED:   JUL 17,1989

The Laboratory package may use * and #-reads in the software for the

auto-instrument interface and keyboard emulators.

7    STANDARD SECTION:   6F          KILL DD global

DATE GRANTED:   MAR 20,1990

A one time exemption has been granted for direct Sets and Kills of

specific DD's in the version 5 post init routine.

8    STANDARD SECTION:   1           ANSI

DATE GRANTED:   MAR  4,1991

Laboratory may use the argumentless FOR in version 5.1.

9    STANDARD SECTION:   2A          B,J,V,Z,$V,$Z

DATE GRANTED:   MAR 18,1991

Lab may save system $Z variables in local variables for storage in

their error trap for automated instruments.

10    STANDARD SECTION:   5F          %ZTLOAD

DATE GRANTED:   MAR 18,1991

Lab may reference the global %ZTSK directly to display the error

trap data stored there.

11    STANDARD SECTION:   6F          KILL DD global

DATE GRANTED:   MAR 18,1991

Lab may kill bad "NM" and bad 9.2 DD nodes directly in their 5.1

post init.

ON-LINE DOCUMENTATION9 On-Line Documentation

This section describes how to generate on-line documentation. It also provides file numbers and/or file number ranges, namespaces, and special templates. The user is informed where to find Kernel documentation, how to print the data dictionaries, and diagram menus.

### 56 File Number Ranges

The Laboratory files number ranges includes Files #60 through #69.91 and #95.

### 57 Namespacing

Laboratory uses the name spaces of LR and LA for all exported routines, menus, options, and templates.

### 58 Special Templates

Two compiled print templates included in the Laboratory V. 5.2 package are located in BLOOD DONOR file (#65.5).

**Templates 	Routines Invoked**

LRBL DONOR TESTING REPORT	^LRBLDPT

LRBL DONOR TESTING SUPPLEMENT	^LRBLDPK

### 59 On-Line Help Using Kernel

On-line documentation about the Laboratory may be obtained in a number of ways. The print OPTION file (#19) and Menu Management Menu will display a list of namespaced options associated with the Laboratory package. Other namespaced entries may also be retrieved from the Print, Input, and Sort Templates files, and the Security Key, Function, Bulletin, and Help Frame files. The structure of the file may be displayed with the VA FileMan List File Attributes options in several formats. Routines may be printed with options on the Programmer’s Option Menu which call the %ZPT1 routine to print the first and optionally second line, or %ZTPP to print the entire routine to an output device. Globals may be displayed with the List Globals option.

The use of question marks at the file and field level is described in the VA FileMan Technical Manual. The use of question marks within the menu system will invoke help about options and menus. See On-line Help From Your Terminal Screen section for further information.

### 60 On-line Help From Your Terminal Screen

All DHCP applications provide some degree of on-line help for users. This means that assistance is available to you from the computer, on your terminal screen. In the menu system, the help function will assist you with your menus, describing your options so that you make the proper choice.

**?** Displays menu	If you enter a single question mark, you will be given a list of the menu options available to you. Only the options which pertain to the specific application you are working in will be listed.

**??** More Options	Two question marks will give you your menu options plus a list of automatic menu options. These are options you do not normally see on your menus, but which are available to you in any program you are working in. This menu is referred to as your secondary menu. Locked options are displayed if the user holds the key.

**???** Describes Options	Three question marks provide you with a brief description of the options you can choose from. Use this feature when you are uncertain which menu option to select in order to accomplish your work.

**?** (option name)	If you type one question mark and the option name (or the first letter or number), you will enter the on-line help frame system (if your site has installed the help frames, check with your site manager). Information is available about the series of prompts and technical data for that option or menu, etc.

### 61 How To Print Data Dictionaries

The structure of the file may be displayed with the VA FileMan List File Attributes options in several formats.

**Example:** How to print a Data Dictionary using VA FileMan.

Select VA FileMan Option: **8  List File Attributes** OUTPUT FROM WHAT FILE: // **60 LABORATORY TEST** Select SUB-FILE: **&lt;RET&gt;** Select LISTING FORMAT: **STANDARD** // **&lt;RET&gt;** DEVICE: **(Enter Printer Name)** RIGHT MARGIN:  132// &lt;RET&gt;

GLOBAL JOURNALING

## 10 Global Journaling

NAME        GLOBAL      JOURNALLING                DESCRIPTION

-----------------------------------------------------------------------------

LAB SERVICE

LAB         optional--not required        This global contains the

basic laboratory files

used in setting up the

package.

LR          mandatory!                     This global contains

the patients results which

have been verified by the

laboratory package. It

also contains status of

test. e.g.., "Pending"

Other data such as

cummulative or archive

data is also stored in

this global.

**** Protection of this

global is very important.

Order and accessions

point to entries in this

file.

LAR                                        This file contains the

archive patient data. It

indicates where the data

has been stored and

certain other information.

LRD         mandatory!                    This file contains

information relative to

the Blood Bank Donor

Inventory. This file is

very important to Blood

Bank.

LRE         optional--not required        This file contains

certain donor information

which the Blood Bank

module has collected over

time. If data is lost it

could impact the Blood

Bank if it runs a donor

program.

LRT         optional--not required        This file contains

results on specimens which

are not patients e.g..,

Research, Enviromental,

Referral, and Sterilizer

In some cases Patient

Data could be stored in

this global, if so, then

this global should be

treated as ^LR( global.

LRO         mandatory!                    This file generally

contains the Order made to

the Laboratory Package.

Without this file all

previous orders can not be

referenced. Care should be

made to preserve this

file.

DIC(68.4                                 This globals contains

work list heading and is

the only Laboratory global

not name spaced.

LAM         mandatory!                  This file contains the

nationally distributed

WKLD Code file. It also

may contain those site

specific entries.

**Lab Automated Instruments**

LAB(62.4,   not recommended            FILE OF AUTOMATED

INSTRUMENTS PARAMETERS

LA(         not recommended              This global contains

strings of data going to

and coming from auto mated

instruments. It also

contains the index into

auto instrument generated

errors trap. For certain

instruments there will be

“C” nodes These are used

for storage when using bi-

directional instrument.

LAH(        not recommended              This global contains

automated instrument data

awaiting verification the

Technologist.

**Mapping Routines**

The following routines should be mapped.

LAGEN     LAMIAUT0  LAMIAUT1  LAMIAUT2  LAMIAUT3  LAMIAUT4  LAMIAUT5

LAMIAUT6  LAMIAUT7  LAMIAUT8

LRAFUNC   LRAFUNC1  LRAFUNC5  LRAFUNC6  LRAFUNC7  LRCAPA12

LRCAPU    LRCAPV    LRCAPV1   LRCAPV11  LRCAPV1A  LRCAPV2   LRCAPV3

LRDIQ     LRDPA     LRDPA1    LRDPA2    LRGEN     LRGEN1    LRGEN2

LRLABAR    LRLABLD   LRLABLD0  LRLABLIO  LRLTR    LRLTR2

LRMIBUG   LRMIEDZ   LRMIEDZ2  LRMIEDZ3  LRMIEDZ4  LRMIPSU   LRMIPSZ

LRMIPSZ1  LRMIPSZ2  LRMIPSZ3  LRMIPSZ4  LRMIPSZ5  LRMIV1    LRMIV2

LRMIV3    LRMIV4    LRMIVER   LRMIVER1  LRORD     LRORD1    LRORD2

LRORD2A   LRORD3    LRORDD    LRORDST   LRORDST1  LROW      LROW1

LROW1A    LROW2     LROW2A    LROW2P    LROW2RP   LROW3     LROW4

LROW5     LRPARAM   LRRP      LRRP1     LRRP2     LRRP3     LRRP4

LRRP5     LRRP5A    LRRP6     LRRP6A1   LRRP6A2   LRRP6A3   LRRP6B1

LRRP6B2   LRRP6B3   LRRP8     LRRP8A    LRRP8B    LRVER     LRVER1

LRVER2    LRVER3    LRVER3A   LRVER4    LRVER5    LRVR      LRVR1

LRVR2     LRVR3     LRVR4     LRVR5     LRWU      LRWU1     LRWU2

LRWU3     LRWU4     LRWU5     LRWU6     LRX       LRXREF    LRXREF1

ANATOMIC PATHOLOGY ORDER DIALOGS

## 11 Anatomic Pathology Order Dialog

### 62 System Overview

The new VistA Laboratory Enhancement (VLE) Anatomic Pathology (AP) Order Dialog is an enhancement to the existing ordering functionality inherent in CPRS with respect to AP that was introduced after the installation of releases LR*5.2*462, LR*5.2*469, LR*5.2*482, LR*5.2*479, and LR*5.2*483   Thus, the new AP Order Dialog will be fully integrated with the legacy Anatomic Pathology system.

Overall, the VLE AP Order Dialog will provide standardization to the current process of AP Order, thereby effectively increasing accuracy, efficiency, and tracking capabilities of specimen processing.  The VLE AP Order Dialog will eliminate the manual transcription of handwritten information from the Standard Form (SF) 515 into the existing AP Order Dialog thereby preventing the misidentification of patients, and providing a mechanism to confirm a patient-specimen match.

Patch LR*5.2*469 will provide thirteen new templates defined by the specialty areas of:

- BONE MARROW
- BRONCHIAL BIOPSY
- BRONCHIAL CYTOLOGY
- DERMATOLOGY
- FINE NEEDLE ASPIRATE
- GASTROINTESTINAL ENDOSCOPY
- GENERAL FLUID
- GYNECOLOGY (PAP SMEAR)
- RENAL BIOPSY
- TISSUE EXAM
- URINE
- UROLOGY, PROSTATE
- UROLOGY, BLADDER/URETER

After a user enters a new AP Order, and the information has been captured and stored by the system, users will be able to view and modify the AP Order or cancel the AP Order.

Patch LR*5.2*462 will modify the Anatomic Pathology specimen log-in option and will provide Surgery Case information, where applicable.

The Anatomic Pathology specimen log-in has been updated to prompt the user for a CPRS order number; the order number prompt will be available in VistA.  When a user enters an order number, the process shall deviate from the current Log-in Anatomic Pathology option in that it shall display any data entered via the CPRS AP Order Dialog.

The Surgery Case functionality will capture a patient’s surgery history, if applicable, over a period of the past seven days. If surgery cases are found for a patient, the cases will be displayed to the user for selection to incorporate into the Anatomic Pathology accession.  When Surgical Case information is added to the Anatomic Pathology fields it will be displayed first, followed by the information obtained from the CPRS order.

Patch LR*5.2*482 addresses an error related to released patch LR*5.2*462.  In brief, the emergency release resolves the error generated when using the option "Verify/release reports, anat path" [LRAPR] to verify/release an Autopsy (AU) accession.  The patch contains two routines; no options or menus are related to the patch release.

Patch LR*5.2*479 is a warranty release patch that provides resolutions to several issues.  The issues and resolutions are the following:

- Sub files 60.0216611,.01 (AOE CPRS SCREEN) and 60.12166,.01 (AOE SCREEN) in the LABORAOTRY TEST file (#60) were erroneously released with the distribution of patch LR*5.2*462. To resolve the issue, the two fields will be removed from the data dictionary with the LR479 post-install routine.

- Sub file 69.321661,.01 (VFD AOE) in the LAB ORDER ENTRY file (#69) was erroneously released with the distribution of patch LR*5.2*462.  To address this issue, the field is removed from the data dictionary with the LR479 post-install routine.

- Specimen Login in VistA does not assign the correct accession number when using the new accession process added to the “AP Specimen Log In” option with patch LR*5.2*462. The order number entered at this point was created using the new AP Order Dialog in CPRS. The accession area assigned to the Laboratory test in file #60 was not being honored and only SURGICAL PATHOLOGY (SP) and CYTOLOGY (CY) accession areas were being utilized.  To resolve the issue, routine modifications were made to honor the correct accession area as defined in the Laboratory test file in association with the division of the user accessioning the order.

- The Practitioner field in CPRS displays '0' if Surgeon/Physician is blank in VistA; note that this is for Backdoor orders only.  To address this issue, routine modifications were made to correct the storage of a zero if a Surgeon/Physician was not entered during the accessioning process.

- Locked login process of AP Orders via Accessioning menu (not that this is post release LR479). To resolve this issue, option Accessioning tests ordered by ward order entry [LROE] has been modified which will now not allow Anatomic Pathology orders to be processed. The  user will see the following message before exiting the option:

<!-- image -->

This is an Anatomic Path order

Must use 'Log-in, anat path' Option to accession this Order

- AP Backdoor order from VistA displays Send Patient to Lab as default Collection Status.  To address this issue, routine modifications were made to change the default from SP Send Patient to WC Ward Collect.

- Backdoor AP Order from VistA does not display patient location in CPRS.  To correct this issue, routine modifications were made to pass the correct pointer to CPRS so that the ordering location will be reflected correctly.

- Error &lt;SUBSCRIPT&gt;AP+2^LRXREF was being triggered during AP Specimen Log-in accessioning of orders created in CPRS. In this situation, there was code in the routine that was attempting to continue the accessioning process even if the test being accessioned did not have an accession area defined that matched the division of the accessioning person. The default lookup was expecting to find an SP for Surgical Pathology or a CY for Cytopathology accession area abbreviations. If a site changed these abbreviations to something other than SP and CY, the &lt;SUBSCRIPT&gt; error would be triggered. To address this issue, routine modifications were made to remove the default accession area logic and replace it with code that will exit the user with the following message:
<!-- image -->

[ TISSUE EXAM]  DOES NOT HAVE AN APPROPRIATE ACCESSION AREA DEFINED

Log-in Aborted

Patch LR*5.2*483 is a warranty release patch that provides a resolution related to an issue in the LR*5.2*479 patch.  The patch contains only a correction to the second line of the routine LRAPKOE.  The second line erroneously listed patch LR*5.2*469 when it was released with LR*5.2*479. This reference to LR*5.2*469 will be removed as LRAPKOE was NOT released as part of LR*5.2*469.  Not that there are no other changes related to the functionality in LRAPKOE.

### 63 Document Orientation

The intended user base of the VLE AP Order Dialog enhancement will include ordering clinicians, laboratory technicians/technologists, and anatomic pathologists.  The ordering clinician will be responsible for initiating the original AP order, specimen collection, and submission to the laboratory.  The laboratory technicians/technologists will serve as the intermediate processors to receive, accession, and process the various AP specimens for review by the anatomic pathologist.  The anatomic pathologists will complete the process by examining the specimens and entering results into the VistA database.  Once the process is complete, the ordering clinician will be able to view the results.

Secondary users of the system will include staff authorized to view orders in the Electronic Health Record (EHR) and general Administrators.  The responsibilities of this user group will revolve around the viewing of lab orders and the overall upkeep, configuration, and operation of the system.

The user community of clinicians, medical technologists (MTs), pathologists, and ancillary staff are highly proficient in clinical laboratory medicine procedures, particularly AP orders, and are also highly proficient in the use of the CPRS and legacy VistA Laboratory software.

<!-- image -->

High-Level Flow Diagram

### 64 List of Routines

| **Routine**   | **Release**            | **Brief Description**                                              |
|---------------|------------------------|--------------------------------------------------------------------|
| LR462A        | LR*5.2*462             | Environment check and post install.                                |
| LR7OAPKM      | LR*5.2*462             | Inbound CPRS Message Handler.                                      |
| LR7OB3        | LR*5.2*462             | Build message, backdoor from Lab order number.                     |
| LR7OF0        | LR*5.2*462             | Receive/Route MSG array from OE/RR; This routine invokes IA #2187. |
| LR7OFAO       | LR*5.2*462             | Setup file 69 for AP orders.                                       |
| LRAP          | LR*5.2*462             | Anatomic Path Utility; Called by many routines in AP package.      |
| LRAPDA        | LR*5.2*462             | Anatomic Path Data Entry.                                          |
| LRAPKLG       | LR*5.2*462             | Moves SP data from SURGICAL RECORD.                                |
| LRAPKLG1      | LR*5.2*462             | Status of SURGICAL CASE.                                           |
| LRAPKOE       | LR*5.2*462, LR*5.2*483 | CRPS AP LAB ORDER ENTRY and ACCESSION.                             |
| LRAPKOE1      | LR*5.2*462             | AP LAB ORDER ENTRY continued.                                      |
| LRAPKOEU      | LR*5.2*462             | AP CPRS DIALOG UTILITIES routine.                                  |
| LRAPLG        | LR*5.2*462             | AP Log-in.                                                         |
| LRAPLG1       | LR*5.2*462             | AP Log-in continued.                                               |
| LRAPRES1      | LR*5.2*462; LR*5.2*482 | AP ESIG Release Report/Alert.                                      |
| LROS          | LR*5.2*462             | Lab Order Status.                                                  |
| LRUWLF        | LR*5.2*462             | File #68 Utility.                                                  |
| LR469A        | LR*5.2*469             | LAB Anatomic Pathology installation support.                       |
| LRUDEL        | LR*5.2*462             | To delete an AP accession number.                                  |
| LROE          | LR*5.2*479             | AP LAB ORDER ENTRY and ACCESSION.                                  |
| LRXREF        | LR*5.2*479             | Builds cross references for the re-index.                          |
| LR482         | LR*5.2*482             | Post install environment check.                                    |

### 65 Templates

The following new templates are associated with Patch LR*5.2*462.

| **Template Name**    | **File Name and Number**        |
|----------------------|---------------------------------|
| LR7OAP DIALOG SCREEN | LR CPRS PARAMETERS  FILE #69.71 |
| LR7OAP CPRS 60       | LABORATORY TEST  FILE #60       |

### 66 Parameters

New parameters are not associated with the releases.

### 67 Data Dictionary

The following list summarizes the Data Dictionaries (DDs) associated with releases LR*5.2*462, LR*5.2*469, and LR*5.2*479:

- DD for File 69.71, LR CPRS PARAMETERS FILE.
- DD for File 60, field 21661; points to LR CPRS PARAMETERS (#69.71), field CPRS SCREEN (#.01).
- DD for File 69.9, field 21661.

### 68 Exported Options

The following is a list of options exported with the software.

1. LR7OAP CPRS 60 EDIT
2. LR7OAP CPRS 60 PRINT
3. LR7OAP CPRS DIALOG MENU
4. LR7OAP CPRS DIALOG PRINT
5. LRXOSX USE AS LINK FOR MENU/ITEM/SUBSCRIBERS

#### Technical descriptions and details for each option are listed below.

##### 21 LR7OAP CPRS 60 EDIT

MENU TEXT: CPRS LAB TEST (#60) EDIT

TYPE: edit

PACKAGE: LAB SERVICE

DESCRIPTION:   This option will allow the user to map AP CPRS SCREEN to a specific laboratory test.

Short Menu Text: AP CPRS TEST EDIT    DIC {DIC}: LAB(60,

DIC(0): AEMNO                         D.: B

DIE: LAB(60,                          DR {DIE}: [LR7OAP CPRS 60 EDIT]

FLDS: [LR70AP CPRS 60 EDIT]

UPPERCASE MENU TEXT: CPRS LAB TEST (#60) EDIT

##### 22 LR7OAP CPRS 60 PRINT

MENU TEXT: Print Laboratory Test CPRS Screen

TYPE: run routine

PACKAGE: LAB SERVICE

DESCRIPTION:   This option will printed a sorted listing of Laboratory Tests (#60) that are linked to LR CPRS PARAMETERS Screens (#69.71).  The report can be sorted two ways.  The user can select the method.

Short Menu Text: Print CPRS Screen List

ROUTINE: PRT^LRAPKOEU                 DIC {DIC}: LAB(69.71,

DIE: LAB(69.71,

UPPERCASE MENU TEXT: PRINT LABORATORY TEST CPRS SCR

##### 23 LR7OAP CPRS DIALOG MENU

MENU TEXT: CPRS AP Dialog Menu

TYPE: menu

PACKAGE: LAB SERVICE

DESCRIPTION:   This menu contains options to manage implementation of CPRS AP Dialog enhancement.

ITEM: LR7OAP CPRS 60 EDIT               SYNONYM: ED

DISPLAY ORDER: 1

ITEM: LR7OAP CPRS DIALOG PRINT          SYNONYM: PRT

DISPLAY ORDER: 2

ITEM: LR7OAP CPRS 60 PRINT              SYNONYM: LST

Short Menu Text: CPRS Dialog Menu     TIMESTAMP: 64065,36782

UPPERCASE MENU TEXT: CPRS AP DIALOG MENU

##### 24 LR7OAP CPRS DIALOG PRINT

MENU TEXT: CPRS Dialog Print (#69.71)

TYPE: print

PACKAGE: LAB SERVICE

DESCRIPTION:   This option will provide a listing of the entries in LR CPRS PARAMETERS (#69.71)

INDEPENDENTLY INVOCABLE: YES          Short Menu Text: CPRS DIALOG PRT

DIC {DIC}: LAB(69.71,                 DIC {DIP}: LAB(69.71,

FLDS: .01,.05,.06,1,2                 BY: [LR7OAP DIALOG SCREENS]

FR: 100

UPPERCASE MENU TEXT: CPRS DIALOG PRINT (#69.71)

ITEM: LR7OAP CPRS DIALOG MENU           SYNONYM: AP

##### 25 LRXOSX

MENU TEXT: OE/RR interface parameters

TYPE: menu

PACKAGE: LAB SERVICE

DESCRIPTION:   This is a menu containing options that deal with various parameters used in the OE/RR interface.

ITEM: LRXOSX2                           SYNONYM: EH

DISPLAY ORDER: 1

ITEM: LRXOSX1                           SYNONYM: AS

DISPLAY ORDER: 2

ITEM: LRXOSX0                           SYNONYM: IL

DISPLAY ORDER: 3

ITEM: LR7O PARAM MENU       SYNONYM: CC

DISPLAY ORDER: 5

UPPERCASE MENU TEXT: OE/RR INTERFACE PARAMETERS

GLOSSARY

Glossary

This Glossary contains terms and their definitions that may not be familiar to the user who is accessing the facility’s computers for the first time. Basic terms, acronyms, and phrases that are used throughout the DHCP environment are included.

Abbreviated Response	This feature allows you to enter data by typing only the first few characters for the desired response. This feature will not work unless the information is already stored in the computer.

Access Code	A code that allows the computer to identify you as a user authorized to gain access to the computer. Your code is greater than six and less than twenty characters long; can be numeric, alphabetic, or a combination of both; and is usually assigned by a site manager or application coordinator. (See the term verify code  in the Glossary.)

Accession	A unique alpha numeric (combination of letters and numbers) assigned to an individual patient specimen when it is received in the laboratory. The accession is assigned by the computer and contains the laboratory departmental designation, the date and an accession number. This accession serves as identification of the specimen as it is processed through the laboratory. (Example: HE 0912)

Accession Area	A functional area or department in the laboratory where specific tests are performed. The accession area defines the departmental designation contained in each accession.

Accession Date	The date of the accession, part of the total alpha-numeric accession of each specimen.

Accession Number	A unique number assigned to each accession.

ADP	Automated Data Processing

ADT	Admission, Discharge, Transfer. A component of the MAS software package .

AFIP	Armed Forces Institute of Pathology; an external review board.

AEMS	Automated Engineering Management Systems. This is the Engineering Service software package.

AMIE	Automated Management Information Exchange. A system that allows the Veterans Benefits Administration to use their WANG System to query medical centers via the VADATS network.

AMIS	Automated Management Information System: a method for tabulating Workload.

AMIS/CAP Codes	Numbers assigned to lab procedures by the College of American Pathology for compiling work statistics.

ANSI	American National Standards Institute. An organization that compiles and publishes computer industry standards.

ANSI MUMPS	The MUMPS programming language is a standard; that is, an American National Standard. MUMPS stands for Massachusetts General Hospital Utility Multi Programming System.

APP	Applications Portability Profile

Algorithm	A predetermined set of instructions for solving a specific problem in a limited number of steps.

Application	A computer program (e.g., a package) that accomplishes tasks for a user.

Application Coordinator	The designated individual responsible for user level management and maintenance of an application package (e.g., IFCAP, Laboratory, Pharmacy, Mental Health).

ARG	Applications Requirements Group

Array	An arrangement of elements in one or more dimensions. A MUMPS array is a set of nodes referenced by subscripts which share the same variable name.

ASCII	American Standard Code for Information Interchange. A series of 128 characters, including uppercase and lowercase alpha characters, numbers, punctuation, special symbols, and control characters.

Attribute Dictionary	See data dictionary.

Audit	An audit is a physical record of access to a file. The VA FileMan and Kernel provide audit tools that may be used to maintain a continuous audit trail of changes that are made to an existing database. Elements that can be tracked include, but are not limited to, fields within files and files themselves. Records are kept of the date/time and user making changes. In addition, the Kernel provides tools for auditing system access, option access, and device usage. Logs store the date/time of access, user identification and name of the option or device used.

Audit Access 	A user’s authorization to mark or indicate that certain information stored in a computer file should be audited.

Audit Trail	A chronological record of computer activity automatically maintained to trace the use of the computer.

Auto Instruments	Automated instruments used in the Lab that identify and measure tissue or other specimens.

Backup	The process of creating duplicate data files and/or program copies as are serve in case the original is lost or damaged.

Baud (Baud rate)	A measure of times per second that switching can occur in a communications channel. Data transmission speed roughly equivalent to 1 bit per second (bps). Commonly used baud rates include 300, 1200, 2400, 3600, 4800, 9600.

Bidirectional	Automated instruments that send and receive information from DHCP.

Boolean	A term used in computer science for data that is binary (i.e., either true or false).

Boot	To load instructions into main memory to get a computer operational.

Buffer	A temporary holding area for information.

Bug	An error in a program. Bugs may be caused by syntax errors, logic errors, or a combination of both.

CAP	College of American Pathology

Caret	A symbol expressed as “^” (up caret), “&lt;” (left caret), or “&gt;” (right caret). The “^” (up caret) is also known as the (up-arrow symbol) or (shift-6) key. In many MUMPS systems, a “&gt;” (right caret) is used as a system prompt and a “^” (up caret) as an exiting tool from an option.

Checksum	The result of a mathematical computation involving the individual characters of a routine or file.

Cipher 	A system that arbitrarily represents each character by one or more other characters.

Collection List	A listing of routine laboratory tests ordered for inpatients. The list is used by the Phlebotomy team during routine collection of specimens from the wards. The list is sorted by ward location, and includes both patient information (Name, SSN, bed/room number) and test information, type of specimen to collect, amount needed, date and time tests were ordered, urgency status, order number and accession number.

Command	A combination of characters that instruct the computer to perform a specific operation.

Computed Field	This field takes data from other fields and performs a predetermined mathematical function (e.g., adding two columns together). You will not, however, see the results of the mathematical calculation in the file. Only when you are printing or displaying information on the screen will you see the results for this type of field.

Computer	A device that processes information. A machine that has input, output, storage, and arithmetic devices plus logic and control units.

Control Key	The Control Key (Ctrl on the keyboard) performs a specific function in conjunction with another key. In some word processing applications, for example, holding down the Ctrl key and typing an A will cause a new set of margins and tab settings to occur; Ctrl-S causes printing on the terminal screen to stop; Ctrl-Q restarts printing on the terminal screen; Ctrl-U deletes an entire line of data entry when the return key is pressed.

Core	The fundamental clinical application packages of DHCP. The original core of applications built on the Kernel and VA FileMan were Admission, Discharge and Transfer (ADT), Scheduling, Outpatient Pharmacy, and Clinical Laboratory. Additional software packages were added to implement Core+6 and Core+8 configurations.

CPU	Central Processing Unit. Those parts of computer hardware that carry out arithmetic and logic operations, control the sequence of operations performed, and contain the stored program of instructions.

Cross Reference	A cross reference on a file provides direct access to the entries in several ways. For example, the Patient file is cross referenced by name, social security number, and bed number. When asked for a patient, the user may then respond with either the patient's name, social security number, or bed number. Cross reference speeds up access to the file for printing reports. A cross reference is also referred to as an index or cross index.

CRT	Cathode Ray Tube. A piece of computer hardware that looks something like a television screen. The CRT and keyboard collectively are called your terminal. A vacuum tube that guides electrons onto a screen to display characters or graphics. Also called VDT for video display terminal.

Cumulative	A chartable patient report of all data accumulated on a patient over a given time period.

Cursor	A flashing image on your screen (generally a horizontal line or rectangle) that alerts you that the computer is waiting for you to make a response to an instruction (prompt).

Data	In the generic sense, data is information that can be processed and/or produced by computers.

Data Attribute	A characteristic of a unit of data such as length, value, or method of representation. VA FileMan field definitions specify data attributes.

Database	A set of data, consisting of at least one file. that is sufficient for a given purpose. The Kernel database is composed of a number of VA FileMan files. A collection of data about a specific subject (e.g., the Patient file). A data collection has different data fields (e.g., patient name, SSN, date of birth). An organize collection of data about a particular topic.

Database Management System	A collection of software that handles the storage, retrieval and updating of records in a database. A Database Management System (DBMS) controls redundancy of records and provides the security, integrity, and data independence of a database.

Data Dictionary	A Data Dictionary (DD) contains the definitions of a file’s elements (fields or data attributes); relationships to other files; and structure or design. Users generally review the definitions of a file’s elements or data attributes; programmers review the definitions of a file’s internal structure.

Data Dictionary Access	A user’s authorization to write/update/edit the data definition for access computer file. Also known as DD Access.

Data Dictionary Listing	This is the printable report that shows the data dictionary. DDs are used by users, programmers, and Documenters.

Data Processing	Logical and arithmetic operations performed on data. These operations maybe performed manually, mechanically, or electronically. Sorting through a card file by hand would be an example of the first method; using a machine to obtain cards from a file would be an example of the second method; and using a computer to access a record in a file would be an example of the third method.

DBA	Within the VA, the Database Administrator oversees package development with respect to DHCP Standards and Conventions (SAC) such as namespacing, file number ranges, and integration issues.

Debug	To correct logic errors and/or syntax errors in a computer program. To remove errors from a program.

Default	A response the computer considers the most probable answer to the prompt being given. It is identified by double slash marks (//) immediately following it. This allows you the option of accepting the default answer or entering your own answer. To accept the default, you simply press the enter (or return) key. To change the default answer, type in your response.

Delete	The key on your keyboard (may also be called D or backspace on some terminals) which allows you to delete individual characters working backwards by placing the cursor immediately after the last character of the string of characters you wish to delete. The “@” sign (shift 2) may also be used to delete a file entry or data attribute value. The computer will ask “Are you sure you want to delete this entry?” to insure you do not delete an entry by mistake.

Delimiter	A special character used to separate a field, record, or string. VA FileMan uses the " character as the delimiter within strings.

Device	A terminal, printer, modem, or other type of hardware or equipment associated with a computer. A host file of an underlying operating system may be treated like a device in that it may be written to (e.g., for spooling).

DHCP	The Decentralized Hospital Computer Program of the Veterans Health Administration (VHA), Department of Veterans Affairs (VA). DHCP software, developed by the VA, is used to support clinical and administrative functions at VA medical centers nationwide. It is written in MUMPS and, via the Kernel, will run on all major MUMPS implementations regardless of vendor. DHCP is composed of packages which conform with name spacing and other DHCP standards and conventions.

Disk	The medium used in a disk drive for storing data.

Disk Drive	A peripheral device that can be used to read and write on a hard or floppy disk.

Documentation	User documentation is an instruction manual that provides users with sufficient information to operate a system. System documentation describes hardware and operating systems provided by a system vendor. Program documentation describes a program’s organization and the way in which the program operates and is intended as an aid to programmers who will be responsible for revising the original program.

DRG	Diagnostic Related Group

DSCC	The Documentation Standards and Conventions Committee

DSS	Decision Support System

E3R	Electronic Error Enhancement Reporting System

Electronic Signature 	A code that is entered by a user which represents his or her legally binding signature.

Encryption	Scrambling data or messages with a cipher or code so that they are unreadable without a secret key. In some cases encryption algorithms are one directional; they only encode and the resulting data cannot be unscrambled (e.g., access/verify codes).

Enter	Pressing the return or enter key tells the computer to execute your instruction or command or to store the information you just entered.

Entry	A VA FileMan record. It is uniquely identified by an internal entry number (the .001 field) in a file.

Extended Core	Those applications developed after the basic core DHCP packages were installed (e.g., Dietetics, Inpatient Pharmacy). Also referred to as Core+6 or Core+8.

EP	Expert Panel

Field	In a record, a specified area used for the value of a data attribute. The data specifications of each VA FileMan field are documented in the file's data dictionary. A field is similar to blanks on forms. It is preceded by words that tell you what information goes in that particular field. The blank, marked by the cursor on your terminal screen, is where you enter the information.

File	A set of related records treated as a unit. VA FileMan files maintain a count of the number of entries or records.

FileManager	See VA FileMan.

FOIA	The Freedom Of Information Act. Under the provisions of this public law, software developed within the VA is made available to other institutions, or the general public, at a nominal charge that covers the cost of reproduction, materials, and shipping.

Free Text	The use of any combination of numbers, letters, and symbols when entering data.

FTAM	File Transfer, Access, and Management

GKS	Graphic Kernel Standard

Global	In the MUMPS language, a global is a tree structured data file stored in the common database on the disk.

Global Variable	A variable that is stored on disk (MUMPS usage).

GOSIP	Government Open Systems Interconnection Profile

Hacker	A computer enthusiast; also, one who seeks to gain unauthorized access to computer systems.

Hardware	The physical equipment pieces that make up the computer system (e.g., terminals, disk drives, central processing units). The physical components of a computer system.

Header	Information at the top of a report.

Help Prompt	The brief help that is available at the field level when entering one or more question marks.

HINQ	Hospital Inquiry. A system that permits medical centers to query the Veterans Benefits Administration systems via the VADATS network.

HIS	Hospital Information Systems

IFCAP	Integrated Funds Distribution, Control Point Activity, Accounting, and Procurement

IHS	Indian Health Service

IHS	Integrated Hospital System

Interactive Language	The dialogue that takes place between the computer and the user in the form of words on the screen of the user’s CRT.

Initialization	The process of setting variables in a program to their starting value.

Input Transform	An executable string of MUMPS code which is used to check the validity of input and converts it into an internal form for storage.

IRAC	Information Resources Advisory Council

IRM	Information Resource Management

ISC	Information Systems Center

JCAHO	Joint Commission for the Accreditation of Health Care Organizations.

Jump (also called	The “^” (shift 6 on most keyboards) allows

Up Arrow Jump)	you to jump or up arrow jump to and from a particular field within an input template to another field within that same input template. You may also Jump from one menu option to another menu option without having to respond to all the prompts in between. To jump, type an “^” (shift 6), and then type the name of the field in the template or option on your menu you wish to jump to.

Kernel	A set of DHCP software routines that function as an intermediary between the host operating system and the DHCP application packages such as Laboratory, Pharmacy, IFCAP, etc. The Kernel provides a standard and consistent user and programmer interface between application packages and the underlying MUMPS implementation. Two Kernel components, VA FileMan and MailMan, are self-contained to the extent that they may stand alone as verified packages. Some of the Kernel components are listed below along with their associated namespace assignments.

VA FileMan	Dl

MailMan	XM

Sign-on Security	XU

Menu Management	XQ

Tools	XT

Device Handling	ZIS

Task Management	ZTM

Key	A security code that is assigned to individual users that allows access to options.

Lab Data	Patient’s verified laboratory data.

Lab Sub-section	Refers to the subdivision of lab major sections. If your lab uses this system, your reports will be printed and totaled by lab sub-section as well as lab section.

LAYGO access	A user’s authorization to create a new entry when editing a computer file. (Learn As You GO, the ability to create new entries).

Line Editor	This is VA FileMan s special line-oriented text editor. This editor is used for the word-processing data type.

Local Variable	A variable that is stored in a local partition.

Load List	Used for organizing the workload in various accession areas of the laboratory. A load list is generated for each automated instrument, and is used to arrange the order in which standards, controls and patient specimens are to be run on the specific instrument.

Log In/On	The process of gaining access to a computer system.

Log Out/Off	The process of exiting from a computer system.

Looping	A set of instructions in a program that are repeatedly executed. When set up correctly, VA FileMan allows you to loop through groups of entries in a file without having to select each entry individually.

LSI	Laboratory System Interface, an instrument for translating data between DHCP and auto instruments.

Magnetic Tape	Plastic or mylar tape on reels or cassettes used for data storage (also called mag tape).

MailMan	An electronic mail system that allows you to send and receive messages from other users via the computer.

Major section	Refers to the grouping of lab subsections into major groups within the lab. A lab may consist of the following major sections: General Clinical (may include hematology, toxicology, serology, chemistry, etc.), Blood Bank and Anatomic Pathology. If your lab uses this system, your workload report will be reported by major section (“Section Workload Report”).

Mandatory Field	This is a field that requires a value. A null response is not valid.

MAS	Medical Administration Service

Menu	A list of options you are authorized access to and may select from.

Menu Tree	A series of menus you sequence through in order to get to the specific option you desire.

Microscan	An automated instrument used for organism identification and for measuring antibiotics within the Microbiology module.

MIRMO	Medical Information Resources Management Office in the Department of Veterans Affairs Central Office in Washington, DC.

MIS	Management Information Systems

Modem	A device for connecting a terminal to a telephone line, allowing it to communicate with another modem. Modems include the following types.

Direct Connect: The modem is directly hooked into the phone line.

Acoustic: The modem is connected to the telephone through the handset.

Auto Answer: When it detects a ring signal, the modem will “answer the phone.”

Auto Dial—The modem, upon command from the terminal or the computer, will dial another modem.

Multiple-valued	More than one data value is allowed as the value of a data attribute for an entry.

MUMPS	Massachusetts General Hospital Utility Multi-Programming System

Name spacing	A convention for naming DHCP package elements. The DBA assigns unique character strings for package developers to use in naming routines, options, and other package elements so that packages may coexist. The DBA also assigns a separate range of file numbers to each package.

NAVAP	National Association of VA Physicians

NCD	National Center for Documentation, located at the Birmingham ISC.

NIST	National Institute of Standards and Technology

NOAVA	Nationwide Office Automation for Veterans Affairs

Node	In a tree structure, a point at which subordinate items of data originate. A MUMPS array element is characterized by a name and a unique subscript. Thus the terms node, array element, and subscripted variable are synonymous. In a global array, each node might have specific fields or "pieces" reserved for data attributes such as name. In data communications, the point at which one or more functional units connect transmission lines.

Numeric field	A response that is limited to a restricted number of digits. It can be dollar valued or a decimal figure of specified precision.

OE/RR	Order Entry and Results Reporting

On-line	A device is on-line when it is connected to the computer.

On the fly	A term given to the process of not permanently storing data in the data dictionary but having a computation performed at run time.

Operating System	A basic program that runs on the computer, controls the peripherals, allocates computing time to each user, and communicates with terminals.

Order number	A number generated daily by the computer each time a test is ordered - unique for each patient order - starting at midnight with order number 1. The order number provides identification of patient specimens both during transport to the laboratory and until accession numbers have been assigned to the specimens. Generally used by non-laboratory personnel; e.g., ward, section, number.

OS/M	Occurrence Screen/Monitor

Output Transform 	An executable string of MUMPS code which converts internally stored data into a readable display.

PACS	Picture Archiving and Communications Systems

Package	The set of programs files, documentation, help prompts, and installation procedures required for a given software application. For example, Laboratory, Pharmacy, and MAS are packages. A DHCP software environment composed of elements specified via the Kernel’s Package file. Elements include files and associated templates, name spaced routines, and name spaced file entries from the Option, Key, Help Frame, Bulletin, and Function files. Packages are transported using VA FileMan’s DIFROM routine that creates initialization routines to bundle the files and records for export. Installing a package involves running the installation routines that will recreate the original software environment. Verified packages include documentation. As public domain software, verified packages may be requested through the Freedom of Information Act (FOIA).

Password	A user’s secret sequence of keyboard characters, which must be entered at the beginning of each computer session to provide the user's identity.

Pattern Match	A preset formula that includes any one of the following types: letters, numbers, or symbols; 2) letters, numbers, and symbols; 3) letters and numbers; 4) symbols and letters; 5) numbers and symbols. If the information entered does not match the formula exactly, the computer rejects the user's response.

Peripheral Device	Any hardware device other than the computer itself (central processing unit plus internal memory). Typical examples include card readers, printers, CRT units, and disk drives.

Pointer	Points to another file where the computer stores information needed for the field of the file in which you are currently working. If you change any of the information in the field in which you are working, the new information is automatically entered into the "pointed to" file.

POSIX	Portable Operating System Interface for Computing Environments

Printer	A printing or hard copy terminal.

Program	A list of instructions written in a programming language and used for computer operations.

Programmer Access Code 	An optional three-to-eight character code that allows the computer to identify you as a user authorized to enter into programmer mode (see also access code). Once in programmer mode you will use Standard MUMPS DHCP official programming language to interact with the computer. Programmer access is very tightly restricted to authorized and qualified individuals.

Programmer Access	Privilege to become a programmer on the system and work outside many of the security controls of Kernel.

Prompt	The computer interacts with the user by issuing questions called prompts, to which the user issues a response.

QA	Quality Assurance

RAM	Random Access Memory

Read Access	A user’s authorization to read information stored in a computer file.

Record	A set of related data treated as a unit. An entry in a VA FileMan file constitutes a record. A collection of data items that refer to a specific entity. For example, in a name-address-phone number file, each record would contain a collection of data relating to one person.

Required Field	A mandatory field, one that must not be left blank. The prompt for such a field will be asked until the user enters a valid response.

RMEC	Regional Medical Education Center

ROM	Read Only Memory. A type of memory that can be read but not written.

Routine	A program or a sequence of instructions called by a program, that may have some general or frequent use. MUMPS routines are groups of program lines which are saved, loaded, and called as a single unit via a specific name .

SAC	Standards and Conventions. Through a process of verification, DHCP packages are reviewed with respect to SAC guidelines as set forth by the Standards and Conventions Committee (SACC). Package documentation is similarly reviewed in terms of standards set by the Documentation Standards and Conventions Committee (DSCC).

SACC	Standards and Conventions Committee of the Decentralized Hospital Computer Program.

Screen	(Noun) The display surface of a video terminal.

Screen	(Verb) The process of checking a user’s input for a predefined format or condition (e.g., date within a permitted range).

Screen Editor	This is VA FileMan’s special screen oriented text editor. This editor is used for the word-processing data type.

Scroll/no scroll	The scroll/no scroll button (also called hold screen) allows the user to stop (no scroll) the terminal screen when large amounts of data are displayed too fast to read and restart (scroll).

SERA	Systematic External Review of Autopsies.

SERS	Systematic External Review of Surgical Pathology.

Set of codes	Usually a preset code with one or two characters. The computer may require capital letters as a response (e.g., M for male and F for female). If anything other than the acceptable code is entered, the computer will reject the response.

Site Manager/IRM Chief	At each site, the individual who is responsible for managing computer systems, installing and maintaining new modules, and serving as liaison to the ISCs.

SIUG/ARG	Special Interest User Group/Application Requirements Group. A designated group of applications experts who work with the developers of a software package to define and approve the contents of the package.

SNOMED	Systematized Nomenclature of Medicine, developed to standardize the coding of information regarding specific diseases.

Software	The set of instructions and data required to operate the computer. One type is called operating system software - fundamental computer software that supports other software. The second type is called applications software - customized programs that tell the computer how to run applications (e.g., Pharmacy, Laboratory )

Spacebar Return Feature	You can answer a VA FileMan prompt by pressing the spacebar and then the return key. This indicates to VA FileMan that you would like the last response you were working on at that prompt recalled.

Spooling	Procedure by which programs and output can be temporarily stored until their turn to print.

SQL	Structured Query Language

Stop Code	A number assigned to the various clinical, diagnostic, and therapeutic sections of a facility

Sub-routine	A sequence of MUMPS code that performs a specific task, usually used more than once.

Subscript	A symbol that is associated with the name of a set to identify a particular subset or element. In MUMPS, a numeric or string value that is enclosed in parentheses; is appended to the name of a local or global variable; identifies a specific node within an array.

Syntax	A term for the rules that govern the construction of a machine language.

Template	A means of storing report formats, data entry formats, and sorted entry sequences is the opposite of “On the Fly”. A template is a permanent place to store selected fields for use at a later time.

Terminal	See CRT. May be either a printer or CRT/monitor/visual display terminal.

Treating Area	The section or service of the hospital that requests a test. Some hospital systems have an embedded code that determines if the ordered test is for an inpatient or outpatient.

Tree Structure	A term sometimes used to describe the structure of a MUMPS array. This has the same structure as a family tree, with the root at the top, and ancestor nodes arranged below, according to their depth of subscripting. All nodes with one subscript are at the first level, all nodes with two subscripts at the second level, and so on.

Trigger	A trigger is an instruction that initiates a procedure. In VA FileMan, a trigger can be set up when entry of data in one field automatically updates a second field value.

Truncate	Truncating is a process that drops characters of text or numbers (without rounding) when the text or numbers are limited to a specific location to store or print them. For example, the number 5.768 is truncated to 5.76 when stored or printed in a location that holds only four characters.

Uneditable Field	This is a status given to fields to prevent any editing of data in the field.

Up Arrow	A character on your keyboard that looks like this “^”. The “^” character is used mainly for exiting or opting out of answering VA FileMan prompts and jumping to other fields in VA FileMan. The “^” character is the “shift 6” key on most keyboards.

User Access	Access to a computer system. The user’s access level determines the degree of computer use and the types of computer programs available. The systems manager assigns the user an access level. (See also access code and programmer access code.)

Utility Routine	A routine that performs a task that many programmers utilize.

VA	The Department of Veterans Affairs, formerly called the Veterans Administration.

VACO	Department of Veterans Affairs Central Office

VADATS	Veterans Administration Data Transmission System

VA FileMan	A set of programs used to enter, maintain, access, and manipulate a database management system consisting of files. A package of online VA FileManager computer routines written in the MUMPS language which can be used as a stand-alone database system or as a set of application utilities. In either form, such routines can be used to define, enter, edit, and retrieve information from a set of computer-stored files.

VA MailMan	A computer-based message system.

VAMC	Department of Veterans Affairs Medical Center

Variable	A character or group of characters that refer to a value. MUMPS recognizes three types of variables: local variables, global variables, and special variables. Local variables exist in a partition of main memory and disappear at sign off. A global variable is stored on disk, potentially available to any user. Global variables usually exist as parts of global arrays. The term “global” may refer either to a global variable or a global array. A special variable is defined by system operation (e.g., $TEST).

VAX	Virtual Address Extension

VDT	Video Display Terminal (See CRT)

Verification (data verification)	The process by which technologists review the data the computer for a specific patient and verify (validate) that it is accurate before releasing the data to the physician.

Verification 	A process of internal and external

(package verification) 	package review carried out by a DHCP verification team (people who were not involved in the development of the package). Software and associated documentation are reviewed in terms of DHCP Standards and Conventions.

Verify Code	An additional security precaution used in conjunction with the access code. Like the access code, it is also 6 to 20 characters in length and if entered incorrectly will not allow the user to access the computer. To protect the user, both codes are invisible on the terminal screen.

VHA	Veterans Health Administration.

VITEK	An automated instrument is used for organism identification and for measuring antibiotics within the Microbiology module.

WKLD	This is the abbreviation for workload used by the Laboratory package.

Work List	Used for collecting and organizing work in various accession areas of the laboratory. A work list is generated for manual or automated tests (singly or in batches) and can be defined by number of tests and/or which tests to include. It can also be used as a manual worksheet by writing test results directly on the worklist.

Wrap-around mode	Text that is fit into available column positions and automatically wraps to the next line, sometimes by splitting at word boundaries (spaces).

Write Access	A user’s authorization to write/update/edit information stored in a computer file.

APPENDIX A

#### Appendix

EXCERPTS FROM GENERAL DIGITAL’S MAINTENANCE AND OPERATIONS MANUAL FOR THE GDC 2100 (LSI)

Section 1 Data Concentrator

1.1 General Description

The GDC-2100 is a general purpose computer programmed to perform a data concentration function. The computer is composed of a DEC SBC 11/21 PLUS single-board computer and two DEC DLV11-J’s. The modules are housed and powered by a Sigma SA-H136 chassis. Data input and output is accomplished via 10 RJ11 connectors on the back panel.

Some features of the GDC 2100 are:

-DEC PDP 11 instruction set
-32 K bytes of RAM
-16 K bytes of ROM
-60 HZ clock
-10 RS232 serial ports interfaced through RJ11 connectors
-65 watt power supply
-cooling fan
-external power and restart connectors

1.2 Application Description

The GDC 2100 has 10 serial connectors. The connectors are numbered P1, P2, 1J0-1J3, and 2J0-2J3. The software accepts data from all connectors except P1 in blocks up to 256 ASCII bytes. The blocks are terminated by a CR or any control character. Data is output from P1 in the format: /TXXLYYYMZZZ/CR/Data/CR/ where X is a two-digit ASCII line number, YYY is a three-digit ASCII-length number and ZZZ is a three-digit ASCII message number. The data concentrator holds the message buffer until an “A” is received. An “N” requests retransmission.

1.3 Installation

Unpack the GDC 2100 and visually inspect it for damage that might have occurred during shipping. If damage is noted, please notify General Digital Corporation. Each shipping container should contain:

-GDC 2100 Computer

-GDC 2100 Manual

-AC power cord

-two brackets

The unit is shipped set for 115VAC. If voltage change is required, consult section IV of this manual. The unit is installed by connecting P1 to the data output line and connectors P2, 1J0-1J3 and 2J0-2J3 to data lines from the sources. The unit is designed for table-top operation or optionally may be secured by removing the four rubber feet and attaching the two tie-down bars. Power is applied by the rear panel switch.

1.4 Specifications

The unit has slots for four dual wide boards. Three of these are factory installed. They are numbered 1-4 from top to bottom. Slot one has the KXT11 processor. Slots two and three have DLV11-J’s installed. All serial lines are set for 1200 baud, 8 bits, one stop bit, no parity.

Slot 1 KXT11-AA	32 K bytes RAM (Socket B and local)

16 K BYTES ROM (Socket A)

60 HZ CLOCK

SLU 1 CSR=177560

VECTOR   60

SLU 2 CSR=    120

Slot 2 DLV11-J	CSR=176500

VEC=300

Slot 3 DLV11J	CSR=176600

VEC=340

1.5 Troubleshooting

Due to the simple nature of the GDC-2100, there are only three things that can go wrong. The power supply, the processor, or one of the DLV11-J’s can fail. On power-up, the processor executes a comprehensive “bit-walk” memory diagnostic; when power is applied, the LED on the KXT11 will blink on for one second and then go out for five seconds while the memory is tested. After this time, the LED will blink on a one-second interval.

Since General Digital has gone out of business the repair of the LSI has become a local issue. Since the LSI is comprised of standard DEC components, repairs should be able to be made whether by your local BME shop or a local repair vendor. If no local vendor is available your ISC can give you information on possible vendors to repair the LSI.

If one line fails (input from one source) replace the appropriate board. If the line is 1J0-1J3, replace the board in slot 2. If the line is 2J0-2J3, replace the board in slot 3. All other failures, will require more extensive repair and the whole unit will need to be sent out for repair. If a board is removed, the internal cabling may become confused. The cable has ten small connectors that are inserted into the boards with the wire going down. The left-most connector (brown, yellow, orange, red wires) goes to slot 1, J1 (the right-most of the two small sockets). The next connector to the right (green, gray, purple, blue wires) goes to slot 1, J2 (the left-most socket). The next four connectors to the right go to slot 2, in sequential order from right to left. The last four connectors go to slot 3 in sequential order from right to left.

Table 2-11 Summary of Console Selection Jumper Configurations

Label	Console selected	Console Not Selected

C1	Install jumper from	Install jumper from

wire wrap pins	wire wrap pins
		X to 1		X to 0.

	C2	Install jumper from	Install jumper from
		wire wrap pins		wire wrap pins
		X to 1.		X to 0.

2.2.3 Configuring Channel Word Formats

2.2.3.1	General - Each DLV11-J SLU channel can be individually configured for number of data bits (7 to 8); even, odd or no parity; 1 or 2 STOP bits, and baud rate (described in Paragraph 2.2.4). The serial character format is shown in Figure 2-6; jumper locations are shown in Figure 2-7; and a summary of possible character format jumper configurations is shown in Table 2-12.

2.2.3.2	Number of Data Bits - The serial character format for each channel can be configured for either seven or eight data bits. Three D (data) wire wrap posts are provided for the purpose of selecting the number of data bits per character for each channel. If seven data bits per character are desired, connect a jumper from wire wrap D pin X to pin 0. To configure eight data bits, connect the jumper from wire wrap D pin X to pin 1.

2.2.3.3	Number of STOP Bits - The serial character format for each channel can be configured for either one or two STOP bits. Configure one STOP bit operation by connecting a jumper between S (stop) wire wrap pin X and pin 0. To configure two STOP bits, connect a jumper from wire wrap S pin X to pin 1.

**NOTE:** The two STOP bits are generally only required for use with Teletype@ terminals.

2.2.3.4 Parity Inhibit - Even, odd, or no parity bit generation and detection can be configured for each channel. If no parity bit generation or detection is desired, delete the bit by connecting a jumper between P (parity) wire wrap pins X and 1. If a parity bit is desired, connect P pins X and 0. Select even parity by connecting a jumper between E (even parity) wire wrap pin X and pin 1. Select odd parity by connecting a jumper between E pin X and pin 0.

**NOTE:** To prevent hardware damage within the channel, the E jumper must ALWAYS be installed. This is true regardless of the configuration of the P (parity) jumper.

Table 2-12 Summary of Character Format Jumper Configurations

Wire wrap Connection

UART

Label	Parameter	X to 0	X to 1	Comments

D	Number of	7 bits	8 bits	LSB is

data bits			transmitted

first

S	Number of	1 bit	2 bits

stop bits

P	Parity inhibit	Parity generation	Parity generation

and detection	and detection

enabled	disabled

E	Even parity	Odd parity	Even parity	Requires P

enabled	enabled	enabled	jumper

connected

from X to 0

**NOTE:** The E jumper must be connected to either 0 or 1, even if the parity bit is disabled.

2.2.4 Baud Rate - Each channel can be configured for baud rates ranging from 150 to 38400 bits/s. Baud rate jumpers are shown in Figure 2-7. One baud rate clock input wire wrap pin is provided for each channel (pins 0-3 and channels 0-3 respectively). Both transmitter and receiver functions for a given channel operate at the same baud rate; split baud rate operation is not provided.

**NOTE:** A 110 baud rate clock generator circuit is contained on the optional DLV11-KA 20 mA option. When 110 baud operation is desired, do not connect the baud rate jumper on the DLV11-J module for that particular channel. The 110 baud clock will be supplied by the DLV11-KA option through the interface connector.

Configure baud rates (except 110 baud) by connecting a jumper from an appropriate baud rate generator output wire wrap pin to the baud rate clock input pin (labeled 0-3); one jumper is required for each channel. Baud rate generator outputs are identified in Table 2-13.

**NOTE:** If more than one channel requires the same baud rate, wire wrap jumpers may be daisy-chained.

Table 2-13 Baud Rate Generator Outputs

Wire wrap	Baud Rate

Pin Label	(bits/s)

U	150

T	300

V	600

W	1200

Y	2400

L	4800

N	9600

K	19200

Z	38400

2.2.5 Channel 3 BREAK Response - Channel 3 (normally used as the console device) can respond to a BREAK condition on the receive line such as when an operator presses the BREAK key on the associated terminal. The BREAK key transmits a continuous space signal which is detected by the DLV11-J circuits as a framing error. If no operation is desired, do not connect jumpers to the B, X, and H wire wrap pins. Boot and Halt response are described as follows:

**Boot** - This function causes the processor to restart operation by executing a bootstrap program. The bootstrap program starts at memory location 173000 whenever a BREAK condition occurs on the receive data line; this will occur only if processor power-up mode 2 is configured on the processor module. Otherwise, the processor will respond to its configured power-up mode.

Configure the bootstrap response by connecting a jumper from wire wrap pin X to B.

**Halt** - This function causes the processor to halt whenever a BREAK condition occurs on the receive data line. This operation will occur regardless of the processor power-up mode configured on the processor module. Whenever the processor halts, console octal debugging technique (ODT) micro code is invoked.

Configure the BREAK response by connecting a jumper from wire wrap pins X to H.

The location of the BREAK response jumpers is shown in Figure 2-7 and a summary of possible configurations is shown in Table 2-14.

Table 2-14 Channel 3 BREAK Operation Jumper Summary

BREAK

Response

Operation	Jumper Connection

Boot	Install jumper between wire wrap pins X and B

Halt	Install jumper between wire wrap pins X and H

No response	No jumper installed

**LSI GRAPHIC - PROCESSOR BOARD**

**DLV11J DEC Board**

INDEX

#### Index

* **WARNING:** , 47

**?** , 264

**?** (option name), 264

**??** , 264

**???** , 264

Anatomic Pathology, 198

ANTIMICROBIAL SUSCEPTIBILITY file, 103, 119

Archive Options, 218

archiving of laboratory data from the ^LR global, 215

AUTO INSTRUMENT file, 104, 121

Automated Instrument Interface Specifications, 72

Automated Instrument Interfacing, 51

Automated Instruments Interface, 74

Bar Code Labels, 91

Batch Entry of Preliminary Comments for Accessions, 29

Batched Interim, 39

Bidirectional Communications, 59

Bidirectional Related Fields, 61

Blood Bank, 198

Brief File Descriptions, 177

Check a Single Routine Size, 14

Check Files for Inconsistencies [LRCHKFILES], 10

Clear data from the LAR global, 219

COLLECTION SAMPLE file, 105

control code, 71

Cross References, 203

Cumulative Report, 31

Day One files, 20

DBA Integration Agreements, 225

Description of ^LA Global, 86

Description of ^LAH Global, 86

Device Parameters, 37

DHCP Laboratory Files, 103

Direct connect instruments, 79

Download Auto Micro Worklist, 109

Download Full Data, 103

Download Routine, 61

Echo Device, 89

Editing, 15

Entry or Exit Action, 196

Entry Point References, 169

ETIOLOGY FIELD file, 103, 119

Exported Options, 185

External Referenced Files and Fields, 223

External Relations, 223

External Routines, 224

External Variables, 224

File List, 175

File Number Ranges, 263

File Structure/Interaction, 20

FileMan Lab Results Reporting, 43

Force Cumulative Data to Permanent Page [LRAC FORCE], 215

Global Journaling, 269

handshake program, 60

How To Print Data Dictionaries, 265

Immediate Interim, 39

Instrument Data Flow, 49

Instrument Interface Troubleshooting, 76

Instrument Routines, 80

interface, 47

INTERFACE DATA OPTION MENU, 106

Interface Testing, 75

Interim Reports, 38

Intermec 8646 Printer, 94

Internal Relations, 251

IRM personnel, 225

LAB DATA file, 119

lab label, 27

Lab Labels, 27

Lab Routine Integrity Menu, 13

LABORATORY DATA file, 103

Laboratory Module Work Flow, 6

Laboratory Security Keys, 24

LABORATORY SITE file, 103, 120

LABORATORY TEST file, 120

LAPORTX X Routine, 80

LAPX  Routine, 80

LIMs, 225

Load Integrity File, 14

LOAD/WORK LIST file, 120

LOAD/WORK LIST file, 103

Load/Work Lists, 48

**Local AUTO INSTRUMENT files** , 79

Loop thru LR Integrity, 14

**LRLABEL4** , 28

LRTASK Options, 199

LSI, 96

**LSI Graphic** , 65

LSI Wire Wrapping, 68

Mapping Routines, 273

Microfiche of Path Reports, 30

MicroScan File Setup, 101

MicroScan Interface, 96

Namespacing, 263

New Data Names, 19

Non VA FileMan Compatible Globals, 86

Note Box, 7

OE/RR documentation, 141

OE/RR Routines, 165

On-line Help From Your Terminal Screen, 264

On-Line Help Using Kernel, 263

OTC 800 Printer, 92

Package-Wide Variables, 255

Pin Definitions, 75

Planning and Implementation Guide, 22, 26, 28, 30, 119, 177

preimplementation files, 20

Processing Routine, 60

Purge Old Orders and Accessions [LROC], 217

Read Data from Off-Line Media, 219

Required Software, 224

RJ11, 96

Routine Descriptions, 145

RS-232, 47

Search for Lab Data to Archive, 219

Security Keys, 197

Special Templates, 263

Stand Alone Menus, 251

Standards and Conventions Committee (SACC) Exemptions, 259

Supervisors/Choosers of Instrumentation, 47

Supported References, 169

System Integrity Checks, 10

Tasking the Interim, 39

TaskManager, 36

TOPOGRAPHY FIELD file (. 61)

Troubleshooting for VITEK, 127

Version 2 LSI Eprom Installation, 63

**VITEK File Setup** , 115

VITEK Interface, 110

VITEK Interface Instructions, 110

**WARNING** , 37, 49, 63, 122, 125

Warning Symbol, 7

wire wrap tool, 68

Wiring Diagrams and Pin Definitions for Automated Instruments, 72

Workload Recording, 25

## Interface Guide for OE/RR Package

The section of the Technical manual provide a list of Laboratory V. 5 .2 software package routines and first line descriptions.

**Conversion routines**

LR52CNV;SLC/MRH/FHS - DRIVER FOR THE LAB DATA CONVERSION TO FILE 200

LR52CNV0;SLC/MRH/FHS - UTILITIES FOR 5.2 DATA CONVERSION

LR52CNV1;SLC/MRH/FHS ; Callable DATE-TIME functions

LR52CNV3;SLC/MRH/FHS - NEW PERSON CONVERSION FOR LAB ^LR(

LR52CNV4;SLC/MRH/FHS - continuation of LR52CNV3

LR52CNV5;SLC/MRH/FHS - NEW PERSON CONVERSION FOR LAB ^LRD(65 ; 1/23/91

LR52CNV7;SLC/MRH/DALISC/FHS - NEW PERSON CONVERSION FOR LAB ^LRO(67.9; 1/23/91

LR52CNV8;SLC/MRH/FHS - NEW PERSON CONVERSION FOR LAB ^LRO(68;1/23/91

LR52CNV9;SLC/MRH/FHS - NEW PERSON CONVERSION FOR LAB ^LRO(69...;

LR52CNVA;SLC/MRH/FHS - NEW PERSON CONVERSION FOR LAB ^LAR("Z" ; 1/23/91

LR52CNVP;DALISC/J0-REPRINT CONVERSION EXCEPTION REPORT ;01/08/93

LR52CNVU;DALISC/FHS - NEW PERSON CONVERSION FOR LAB ^LR( CONTINUED

LR52CNVX;SLC/AM/DALISC/FHS - WKLD (CAP) CODE LIST REPORT PRE INSTALL 5.2 ;1/16/91 15:34 ;

LR52NTEG;ISC/XTSUMBLD KERNEL - Package checksum checker ;JAN 04, 1994@18:44:16

LR52TIM2;DALISC/J0-CONVERSION TIMES REPORT ;12/11/92

LR52TIME;DALISC/J0-CONVERSION TIMES REPORT ;12/11/92

**Regular routines**

LRABG     ;SLC/RWF - PULMONARY LAB DATA DISPLAY ; 8/25/87  08:27 ;

LRABG1    ;SLC/RWF - PULMONARY LAB DATA DISPLAY ; 2/22/87  2:08 PM ;

LRAC      ;SLC/DCM/MILW/JMC - CUMULATIVE REPORTS DRIVER ;2/20/91  08:33 ;

LRAC1     ;SLC/DCM/MILW/JMC - CUMULATIVE CONT. ;2/19/91  09:55 ;

LRAC2     ;SLC/DCM - CUMULATIVE CONT. ; 12/12/88  10:16 ;

LRAC2A    ;SLC/DCM - CUMULATIVE CONT. ; 25 Oct 88  2:56 PM ;

LRAC3     ;SLC/DCM - PRINT CUMULATIVE REPORT ; 3/3/88  13:23 ;

LRAC4     ;SLC/DCM - PRINT CUMULATIVE REPORT ; 5/16/88  10:49 ;

LRAC5     ;SLC/DCM - PRINT CUMULATIVE REPORT ; 12/23/87  11:13 ;

LRAC6     ;SLC/DCM/MIWL/JMC - PRINT CUMULATIVE REPORT CONT. (MISC.); 1/31/89 15:02 ;

LRAC7     ;SLC/DCM - SET-UP FOR THE KILL ; 8/11/87  09:41 ;

LRAC8     ;SLC/DCM/MILW/JMC - REFORMAT ^LAC WHEN FILE 64.5 IS CHANGED; 10/2/87  11:30 ;

LRAC9     ;SLC/DCM - PRINT CUMULATIVE REPORT ; 3/3/88  13:25 ;

LRACC     ;SLC/RWF - READ ACCESSION ; 7/10/87  17:38 ;

LRACDIAG  ;SLC/DCM - DIAGNOSTIC REPORT FOR LAB REPORTS FILE (64.5);2/19/91 10:09;

LRACF     ;SLC/RWA - FORCE PAGES TO FULL ;2/19/91  10:10

LRACFILE  ;SLC/DCM - SORT FILE ROOM PATIENTS BY SSN ; 6/2/87  11:30 ;

LRACFIX   ;SLC/DCM - REBUILD ^LRO(68,"AC") FROM A GIVEN DATE AFTER ALL LRAC X-REF ARE REINITIALIZED. ; 5/30/86  2:47 PM ;

LRACFR    ;MILW/JMC- Lab cumulative print fileroom patients ;2/20/91  08:33 ;

LRACK     ;SLC/DCM/MILW/JMC - CHECK CUMULATIVE DEVICE STATUS ; 9/30/87  15:11 ;

LRACKL    ;SLC/DCM/MILW/JMC - CHUTES &amp; LADDERS ; 2/16/88  16:15 ;

LRACKL1   ;DALISC/FHS/MIWL/JMC - CONTINUES CHUTES &amp; LADDERS ; 03/24/92 18:40

LRACM     ;SLC/DCM - MENU FOR CUMULATIVE REPORTS ;2/19/91  10:11 ;

LRACM1    ;SLC/DCM - MENU FOR CUMULATIVE REPORTS CONT. ;2/20/91  08:36 ;

LRACM2    ;SLC/DCM - MENU FOR CUMULATIVE REPORTS ;2/19/91  10:16 ;

LRACM2F   ;MILW/JMC - LIST CUM PATIENT BY LOCATION

LRACM3    ;SLC/DCM - REPRINT/INITIALIZE PATIENT CUM REPORT ;6/12/89  16:21 ;

LRACM4    ;SLC/DCM - INIT CUM REPORTS CONT. ; 9/10/87  09:55 ;

LRACP     ;SLC/DCM - CUMULATIVE PURGE ;2/19/91  10:17 ;

LRACPG    ;SLC/RWF - REMOVE LR(LRDFN,"PG") TO INITIALIZE PAT CUM;19 JUN 84 12:38PM ;

LRACS     ;SLC/DCM - DAILY LAB SUMMARY REPORTS ;2/19/91  10:18 ;

LRACS1    ;SLC/DCM - DAILY LAB SUMMARY REPORTS ; 2/22/87  3:06 PM ;

LRACS2    ;SLC/DCM - LAB SUMMARY REPORT CONT. (MISC.) ; 2/22/87  3:08 PM ;

LRACS3    ;SLC/DCM - MISCELLANEOUS TESTS FOR SUPERVISORS SUMMARY;6/11/87 13:38 ;

LRACSUM   ;SLC/DCM - INDIVIDUAL PATIENT SUMMARY. ;4/17/91  14:30 ;

LRACSUM1  ;SLC/DCM - INDIVIDUAL PATIENT SUMMARY CONT. ; 10/8/87  11:14 ;

LRACSUM3  ;SLC/DCM - PRINT INDIVIDUAL PATIENT SUMMARY ; 3/3/88  13:30 ;

LRACSUM4  ;SLC/DCM - PRINT INDIVIDUAL PATIENT SUMMARY ; 2/11/88  12:06 ;

LRACSUM5  ;SLC/DCM - PRINT INDIVIDUAL PATIENT SUMMARY ; 3/3/88  13:32 ;

LRACSUM6  ;SLC/DCM - PRINT INDIVIDUAL PATIENT SUMMARY (MISC.) ; 3/9/88  10:23 ;

LRAD2ORD  ;SLC/CJS - ADD TESTS TO AN EXISTING ORDER ;2/5/91  11:31 ;

LRAFUNC   ;SLC/MRH/FHS - FUNCTION CALLS A5AFUNC

LRAFUNC1  ;SLC/MRH/FHS -  FUNCTION CALL  DATE/TIME  A5AFUNC1

LRAFUNC5  ;SLC/MRH/FHS - FUNCTION CALLS  CONVERSION IN MEASURMENTS  A5AFUNC5

LRAFUNC6  ;SLC/MRH/FHS - FUNCTION CALLS  CONVERSION IN MEASUREMENT  A5AFUNC6

LRAFUNC7  ;SLC/MRH/FHS - FUNCTION CALL  CONVERSION IN MEASUREMENT  A5AFUNC7

LRAIPRIV  ; DALISC/LD - DOD SITE'S PRIVACY ACT STATEMENT GEM/LL

LRAIRNUM  ;DoD/GEM - DoD SPECFIC ROUTINE  FIND INPATIENT REGISTER NUMBER GEM/LL ; 12/9/86  2:24 PM ;

LRAP      ;AVAMC/REG - ANATOMIC PATH UTILITY ;10/7/93  10:10 ;

LRAPA     ;AVAMC/REG - ANAT PATH ACCESSIONS PER DAY ;2/18/93  10:25 ;

LRAPAP    ;AVAMC/REG - ANATOMIC SORT BY PARENT FILE ; 10/25/88  20:15 ;

LRAPAUA   ;AVAMC/REG - AUTOPSY LIST ;2/18/93  10:26 ;

LRAPAUL   ;AVAMC/REG - PATHOLOGY LIST BY PATHOLOGIST/TECH ;3/4/94  09:26 ;

LRAPAULC  ;AVAMC/REG - ACCESSION COUNTS BY PATHOLOGIST ;2/18/93  10:27

LRAPAUPT  ;AVAMC/REG - AUTOPSY PRINT ;5/9/91  18:17 ;

LRAPAUSR  ;AVAMC/REG - AUTOPSY SUPPLEMENTARY REPORT ;3/11/94  08:41 ;

LRAPBK    ;AVAMC/REG - AP LOG BOOK ;3/3/94  10:23 ;

LRAPBK1   ;AVAMC/REG - AP LOG BOOK ;1/12/94  12:55

LRAPBS    ;AVAMC/REG - BLOCK/SLIDE DATA ENTRY ;3/7/92  10:14 ;

LRAPBS1   ;AVAMC/REG - BLOCK/SLIDE DATA ENTRY ;4/4/94  13:37 ;

LRAPBS2   ;AVAMC/REG - BLOCK/SLIDE DATA ENTRY ;2/6/92  19:19 ;

LRAPC     ;AVAMC/REG - ANAT TOPOGRAPHY COUNTS ;2/18/93  10:30 ;

LRAPCUM   ;AVAMC/REG - AP PATIENT CUM ;9/27/93  06:59 ;

LRAPCUM1  ;AVAMC/REG - AP PATIENT CUM ;7/15/93  10:36 ;

LRAPCWK   ;AVAMC/REG - STUFF CYTOPATH WORKLOAD ;4/1/94  14:40

LRAPD     ;AVAMC/REG - AP DATA ENTRY ;7/15/93  19:18

LRAPD1    ;AVAMC/REG - AP DATA ENTRY ;10/26/93  15:14

LRAPDA    ;AVAMC/REG - ANATOMIC PATH DATA ENTRY ;3/7/94  07:51 ;

LRAPDAC   ;AVAMC/REG - DELETE AP YEARLY ACCESSIONS  ;5/9/91  18:12 ;

LRAPDEL   ;AVAMC/REG - ANAT PATH DELETE DESCRIPTIONS ;9/30/93  07:01 ;

LRAPDPT   ;AVAMC/REG - POW PTS ;3/18/94  08:58 ;

LRAPDS    ;AVAMC/REG - AP REPORT DISPLAYS/PRINTS ;9/24/90  08:15 ;

LRAPED    ;AVAMC/REG - ANATOMIC PATH EDIT LOG-IN ;8/20/93  14:28 ;

LRAPEDC   ;AVAMC/REG - EDIT ANATOMIC PATH COMMENTS ;9/27/93  07:19 ;

LRAPF     ;AVAMC/REG - CY/EM/SP RPT ;7/15/93  15:24 ;

LRAPFICH  ;AVAMC/REG - MICROFICH PATH REPORTS ;2/18/93  10:31

LRAPFTS   ;AVAMC/REG - AP FREE TEXT SEARCH ; 11/12/88  09:24 ;

LRAPH     ;AVAMC/REG - HISTOLOGY RECORD ;2/18/93  10:33 ;

LRAPHDR   ;AVAMC/REG - ANATOMIC PATH DEFAULTS ;7/16/93  06:25 ;

LRAPJNC   ;AVAMC/REG - INCOMPLETE PATH RPTS ;2/18/93  10:34 ;

LRAPKOPT  ;AVAMC/REG - DEL OBSOLETE OPTIONS/CREATE X-REF 62.5,5; 1/29/89 12:45 ;

LRAPL     ;SLC/BA/AVAMC/REG - ANATOMIC PATH LABELS ;10/21/93  12:27 ;

LRAPLG    ;AVAMC/REG - AP LOG-IN ;4/11/94  14:36 ;

LRAPLG1   ;AVAMC/REG - LOG-IN CONT. ;10/29/93  15:28 ;

LRAPLG2   ;AVAMC/REG - LOG-IN DATA FROM FILE #63 ;7/14/93  13:47 ;

LRAPM     ;AVAMC/REG - ANATOMIC PATH MODIFY MICRO/DX ;11/5/93  11:07 ;

LRAPMOD   ;AVAMC/REG - PRINT PATH MICRO MODIFICATIONS ;7/18/93  09:05 ;

LRAPMV    ;AVAMC/REG - MOVE AP ACCESSION ;9/11/92  14:27 ;

LRAPOLD   ;AVAMC/REG - ENTER OLD AP ACCESSIONS ;6/27/94  12:32 ;

LRAPONC   ;AVAMC/REG - FIND MALIGNANCIES FOR ONCOLOGY ;5/21/91  11:43

LRAPP     ;AVAMC/REG - AP PRINT ;11/22/92  11:03 ;

LRAPPA    ;AVAMC/REG - CY/EM/SP PATIENT RPT ;7/15/93  10:20 ;

LRAPPF    ;AVAMC/REG - ANATOMIC PATH FILE SORT ;2/18/93  10:35 ;

LRAPPF1   ;AVAMC/REG - ANAT PATH FILE PRINT BY PT ;2/21/91  12:47 ;

LRAPPF2   ;AVAMC/REG - ANAT PATH ACC# INDEX ;9/13/89  16:37 ;

LRAPPOW   ;AVAMC/REG - POW PATIENT LOOK-UP ;11/14/91  15:42 ;

LRAPPRE   ;AVAMC/REG - ANATOMIC PATH PRE-INIT ;10/6/90  12:29

LRAPQ     ;AVAMC/REG - ANAT PATH QUEUE LIST ;2/18/93  10:35 ;

LRAPQAC   ;AVAMC/REG - AP QA ;7/14/93  15:18 ;

LRAPQACD  ;AVAMC/REG - ENTER TC/QA CODES ;9/25/90  09:12

LRAPQACN  ;AVAMC/REG - CONSULTATION RPTS ;2/18/93  10:38

LRAPQAFS  ;AVAMC/REG - FROZEN SECTION/SURG PATH RPTS ;2/18/93  10:39

LRAPQAM   ;AVAMC/REG - PRINT PATH MICRO MODIFICATIONS ;2/18/93  10:39 ;

LRAPQAMR  ;AVAMC/REG - MALIGNANCY REVIEW ;7/14/93  14:59

LRAPQAR   ;AVAMC/REG - 10% SURG PATH REVIEW ;2/18/93  10:43

LRAPQAT   ;AVAMC/REG - TC CODE SEARCH ;2/18/93  10:44

LRAPQAT1  ;AVAMC/REG - QA CODE SEARCH ;4/17/91  14:31

LRAPQOR   ;AVAMC/REG - QA CODE REPORT ;2/18/93  10:45

LRAPQOR1  ;AVAMC/REG - QA CODE REPORT ;2/18/93  10:46

LRAPQOR2  ;AVAMC/REG - QA AUTOPSY DATA ;9/17/90  07:52

LRAPQOR3  ;AVAMC/REG - QA AUTOPSY DATA ;9/17/90  07:52

LRAPR     ;AVAMC/REG- ANAT RELEASE REPORTS ;5/9/94  14:37 ;

LRAPREF   ;AVAMC/REG - SNOMED REFERENCE OPTION SELECTOR ;3/9/94  13:20 ;

LRAPS     ;AVAMC/REG - AP PATIENT SCREEN DISPLAY ;3/11/94  14:06 ;

LRAPS1    ;AVAMC/REG - ANATOMIC PATH PRINT ;3/11/94  14:08 ;

LRAPS2    ;AVAMC/REG - AUTOPSY PRT ;1/28/93  13:02 ;

LRAPS3    ;SLC/DCM - AP PATIENT SCREEN DISPLAY FOR OE/RR ;12/10/90  12:21

LRAPSA    ;AVAMC/REG - TISSUE STAIN LIST ;2/18/93  10:46 ;

LRAPSE    ;AVAMC/REG - AP SEARCHES ; 7/29/88  17:53 ;

LRAPSEM   ;AVAMC/REG - MULTIAXIAL SNOMED SEARCH ;8/16/93  12:13 ;

LRAPSEM1  ;AVAMC/REG - SEARCH BY SNOMED CODE PRINT ;8/16/93  08:23 ;

LRAPSEM2  ;AVAMC/REG - SEARCH BY SNOMED CODE PRINT ;8/5/93  07:48 ;

LRAPSL    ;AVAMC/REG - ANATOMIC PATH SLIDE LABELS ;4/26/94  10:04 ;

LRAPSL1   ;AVAMC/REG - ANATOMIC PATH SLIDE LABELS ;5/9/91  12:08

LRAPSM    ;AVAMC/REG - SNOMED SEARCH ;2/18/93  10:52 ;

LRAPSM1   ;AVAMC/REG - SEARCH BY SNOMED CODE PRINT ;2/7/90  12:41 ;

LRAPST    ;AVAMC/REG - TISSUE STAIN LOOK-UP ;8/4/91  12:40 ;

LRAPST1   ;AVAMC/REG - AUTOPSY TISSUE STAIN LOOK-UP ;8/4/91  12:40 ;

LRAPSWK   ;AVAMC/REG - STUFF AP WORKLOAD ;9/3/93  08:35

LRAPT     ;AVAMC/REG - AP PATIENT RPT ;3/8/94  09:36 ;

LRAPT1    ;AVAMC/REG - ANATOMIC PATH PRINT ;9/13/89  16:19 ;

LRAPT2    ;AVAMC/REG - AUTOPSY PRT ;4/5/94  12:38 ;

LRAPT3    ;AVAMC/REG - AUTOPSY RPT PRINT COND(1)'T ;9/13/89  13:46 ;

LRAPTT    ;AVAMC/REG - TURNAROUND TIME PATH ;5/4/94  12:41 ;

LRAPTT1   ;AVAMC/REG - TURNAROUND TIME PATH ;1/4/93  10:56 ;

LRAPV     ;AVAMC/REG - ANAT PATH REPORTS NOT VERIFIED ;10/14/93  08:18 ;

LRAPWA    ;AVAMC/REG - GETP AP ACCESSION FOR WORKLOAD ;8/3/91  13:01

LRAPWE    ;AVAMC/REG - DATE/TIME GRIDS SCANNED/PRINTS MADE ;1/10/92  19:02

LRAPWE1   ;AVAMC/REG - STUFF EM SCANNED GRIDS ;4/22/93  10:03

LRAPWEA   ;AVAMC/REG - EM GRIDS SCANNED/PRINTS MADE ;1/12/92  18:04

LRAPWKA   ;AVAMC/REG - STUFF AP WORKLOAD ;4/23/93  07:25

LRAPWKA1  ;AVAMC/REG - STUFF SLIDE LABELS ;3/8/92  10:18

LRAPWR    ;AVAMC/REG - DATE/TIME SLIDES READ ;1/10/92  07:12

LRAPWR1   ;AVAMC/REG - STUFF CYTOPATH SCREENED SLIDES ;5/5/93  10:39

LRAPWSPG  ;AVAMC/REG - GROSS DESCRIPTION WORKLOAD ;8/4/91  09:25 ;

LRAPWU    ;AVAMC/REG - AP WORKLOAD UTILITY ;4/1/94  14:33

LRAPX     ;AVAMC/REG - AP CODING ;12/20/89  16:39 ;

LRAUAW    ;AVAMC/REG - AUTOPSY DATA ENTRY ;11/25/92  09:00 ;

LRAUDA    ;AVAMC/REG - AUTOPSY PATH DATA ENTRY ;6/10/94  14:20 ;

LRAUFIX   ;AVAMC/REG - RELEASE AUTOPSY REPORTS ;2/18/93  13:47 ;

LRAUL     ;AVAMC/REG - PATHOLOGY LIST BY PATHOLOGIST/TECH ;2/18/93  10:54 ;

LRAUMLK   ;VAMC 695/MLK - AUTOPSY SLIDE LABELS;1/21/91 ;3/9/94  13:22

LRAURPT   ;AVAMC/REG - AUTOPSY RPT ;4/5/94  12:44 ;

LRAURV    ;AVAMC/REG - AUTOPSY DATA REVIEW ;2/18/93  12:24 ;

LRAUS     ;AVAMC/REG - PRINT ICD SEARCH ;9/13/89  18:55 ;

LRAUSICD  ;AVAMC/REG - AUTOPSY ICD9CM SEARCH ;3/9/94  13:24 ;

LRAUSM    ;AVAMC/REG - AUTOPSY SNOMED SEARCH ;9/16/93  08:22 ;

LRAUSTA   ;AVAMC/REG - AUTOPSY STATUS LIST ;2/19/93  10:27 ;

LRBARA    ;SLC/RAF ;INTERMEC 4100 2 LABEL FORMAT 8/29/94  12:36

LRBARB    ;SLC/JL/RAF ; INTERMEC 4100 10 PART LABEL FORMAT 8/29/94 12:36

LRBLA     ;AVAMC/REG - BB ADM DATA ;4/16/93  10:20

LRBLA1    ;AVAMC/REG - BB ADM DATA ;2/18/93  08:20

LRBLA2    ;AVAMC/REG - BB ADM DATA ;2/26/92  09:20

LRBLAA    ;AVAMC/REG - XM:TX BY TREATING SPECIALTY REPORT ;2/23/93  14:00 ;

LRBLAA1   ;AVAMC/REG - XM:TX BY TREATING SPECIALTY REPORT ;4/12/92  08:41 ;

LRBLAB    ;AVAMC/REG - BB ADM DATA ;4/18/93  07:45

LRBLAGG   ;AVAMC/REG - BLOOD BANK AGGLUTINATION STRENGTH ;3/9/94  10:29 ;

LRBLB     ;AVAMC/REG - BLOOD BANK BAR CODE READER ; 11/12/88  15:15 ;

LRBLBU    ;AVAMC/REG - BB UNIT BAR CODE ;1/15/90  14:17 ;

LRBLC     ;AVAMC/REG - ABO/RH COUNT ;2/18/93  08:37 ;

LRBLCAP   ;AVAMC/REG - BB CAP WORKLOAD ;3/3/93  14:31

LRBLCMV   ;AVAMC/REG - UNIT PHENOTYPE BY ABO/RH ;9/13/89  19:30 ;

LRBLCON   ;AVAMC/REG - LAB CONSULTS  ;02/12/89  11:15 ;

LRBLD     ;AVAMC/REG - CK BLOOD DONOR ENTRY ; 10/19/88  18:28 ;

LRBLDA    ;AVAMC/REG - BLOOD DONOR LIST ;2/18/93  08:43 ;

LRBLDA1   ;AVAMC/REG - BLOOD DONOR LABELS ; 10/23/88  15:45 ;

LRBLDAA   ;AVAMC/REG - DONOR/DEFERRAL LETTERS ;3/1/89  19:11 ;

LRBLDAL   ;AVAMC/REG - BLOOD DONOR LETTERS ;7/18/91  08:52 ;

LRBLDC    ;AVAMC/REG - DONOR COMPONENT PREP ;4/19/94  11:58 ;

LRBLDC1   ;AVAMC/REG - COMPONENT PREP WORKLOAD ;4/20/93  11:49

LRBLDCR   ;AVAMC/REG - COMPONENT PREPARATION REPORT ;2/18/93  08:44 ;

LRBLDCU   ;AVAMC/REG - CUMULATIVE DONATION CALCULATIONS ;2/18/93  08:47 ;

LRBLDED   ;AVAMC/REG - BLOOD DONOR EDIT ;4/19/94  12:10 ;

LRBLDEL   ;AVAMC/REG - DELETE FILE 65 ENTRIES ;8/14/90  14:36 ;

LRBLDELT  ;AVAMC/REG - DELETE FILE 65 ENTRIES ;8/18/89  10:55 ;

LRBLDEX   ;AVAMC/REG - EX-BLOOD DONORS ;2/18/93  08:54 ;

LRBLDEX1  ;AVAMC/REG - EX-BLOOD DONORS ;9/13/89  20:44 ;

LRBLDEX2  ;AVAMC/REG - EX-BLOOD DONORS ;12/13/89  11:30 ;

LRBLDK    ;AVAMC/REG - DELETE EX-DONORS (65.5 ENTRIES) ; 11/12/88  13:19 ;

LRBLDL    ;AVAMC/REG - BLOOD DONOR LIST ;2/18/93  08:55 ;

LRBLDL1   ;AVAMC/REG - BLOOD DONOR LABELS ; 10/23/88  15:45 ;

LRBLDLG   ;AVAMC/REG - BB DONOR LOG-IN ;3/9/94  12:48 ;

LRBLDP    ;AVAMC/REG - BLOOD DONOR PRINT OPTS ;6/23/92  09:23 ;

LRBLDPA   ;AVAMC/REG - BLOOD DONOR PRINT ;2/18/93  08:57 ;

LRBLDPA1  ;AVAMC/REG - BLOOD DONOR PRINT  ;6/24/90  20:57 ;

LRBLDPA2  ;AVAMC/REG - BLOOD DONOR PRINT  ;6/24/90  20:57 ;

LRBLDPAW  ;AVAMC/REG - BLOOD DONOR PRINT  ;6/24/90  20:57 ;

LRBLDPH   ;AVAMC/REG - DONOR PHENOTYPING ;3/9/94  12:51

LRBLDPK   ; GENERATED FROM 'LRBL DONOR TESTING SUPPLEMENT' PRINT TEMPLATE (#1479) ; 07/27/94 ; (FILE 65.5, MARGIN=132)

LRBLDPL   ;AVAMC/REG - BLOOD DONOR LIST BY DATE ;2/18/93  09:00 ;

LRBLDPT   ; GENERATED FROM 'LRBL DONOR TESTING REPORT' PRINT TEMPLATE (#1475) ; 07/27/94 ; (FILE 65.5, MARGIN=132)

LRBLDPT1  ; GENERATED FROM 'LRBL DONOR TESTING REPORT' PRINT TEMPLATE (#2590) ; 01/20/93 ; (continued)

LRBLDR    ;AVAMC/REG - DONOR REGISTRATION FORM ;3/9/94  12:53 ;

LRBLDR1   ;AVAMC/REG - DONOR EXAM,COLLECTION ;2/11/94  07:50 ;

LRBLDRR   ;AVAMC/REG - REVIEW/RELEASE COMPONENTS ;3/25/92  22:12 ;

LRBLDRR1  ;AVAMC/REG - LABEL-RELEASE COMPONENTS COND'T ;10/27/92  09:49 ;

LRBLDRR2  ;AVAMC/REG - DO NOT RELEASE BLOOD COMPONENT ;2/4/93  12:06 ;

LRBLDSC   ;AVAMC/REG - DONOR SCHEDULING REPORT ;2/18/93  09:01

LRBLDT    ;AVAMC/REG - DONOR UNIT TESTING ;4/6/93  10:48 ;

LRBLDTA   ;AVAMC/REG - ABNORMAL DONOR TESTS ;2/18/93  09:04 ;

LRBLDUC   ;AVAMC/REG - DONOR ABO/RH RECHECK ;3/25/92  22:39 ;

LRBLDW    ;AVAMC/REG - BLOOD DONOR WORKLIST ;2/18/93  09:06 ;

LRBLDX    ;AVAMC/REG - DONOR ABO/RH TESTING ;3/25/92  22:42 ;

LRBLFIX   ;AVAMC/REG - FIX DISPOSITION X-REF ;8/14/92  12:54

LRBLJ     ;AVAMC/REG - BLOOD BANK INVENTORY OPTS ; 5/30/86  3:40 PM ;

LRBLJA    ;AVAMC/REG - BB INVENTORY DATA ENTRY ;7/16/93  15:02 ;

LRBLJA1   ;AVAMC/REG - BB INVENTORY WORKLOAD ;11/5/93  07:35

LRBLJB    ;AVAMC/REG - AUTOLOGOUS UNIT DISPOSITION LIST ;2/18/93  09:08

LRBLJC    ;AVAMC/REG - COMPONENT DISPOSITION LIST ;2/18/93  09:10

LRBLJCK   ;AVAMC/REG - INVENTORY ABO/RH CK ;11/5/93  10:31 ;

LRBLJD    ;AVAMC/REG - BB UNIT DISPOSITION ;6/10/94  10:20 ;

LRBLJD1   ;AVAMC/REG - POOL COMPONENTS ;6/10/94  11:27 ;

LRBLJDA   ;AVAMC/REG - BB UNIT DISP NEW UNIT ;6/10/94  10:22 ;

LRBLJDM   ;AVAMC/REG - MULTIPLE COMP PREP, INVENTORY ;2/11/93  14:56 ;

LRBLJDP   ;AVAMC/REG -  PRINT UNIT DISPOSITION ;2/18/93  09:11 ;

LRBLJED   ;AVAMC/REG - BB INVENTORY EDIT ;6/27/94  14:34 ;

LRBLJI    ;AVAMC/REG - CHECK FILE ENTRIES ;2/18/93  09:14 ;

LRBLJL    ;AVAMC/REG - UNIT RELOCATION ;11/5/93  10:37 ;

LRBLJL1   ;AVAMC/REG - UNIT RELOCATION ;3/12/93  15:28 ;

LRBLJLA   ;AVAMC/REG - CROSSMATCH LABELS ;6/21/93  09:26 ;

LRBLJLG   ;AVAMC/REG - BB INVENTORY LOG-IN ;11/4/93  12:20 ;

LRBLJLG1  ;AVAMC/REG - REVIEW UNIT LOG-IN ;6/27/94  14:31 ;

LRBLJM    ;AVAMC/REG - EDIT POOLED UNIT ;3/9/94  13:01 ;

LRBLJM1   ;AVAMC/REG - EDIT POOLED UNIT ;7/12/92  22:09 ;

LRBLJP    ;AVAMC/REG - BB INVENTORY PRINT OPTS ;3/9/94  13:03 ;

LRBLJPA   ;AVAMC/REG - BB INVENTORY FINAL DISPOSITION ;2/18/93  09:22 ;

LRBLJPA1  ;AVAMC/REG - UNIT FINAL DISPOSITION ;12/28/92  09:24 ;

LRBLJPA2  ;AVAMC/REG - UNIT FINAL DISPOSITION ;9/14/89  07:13 ;

LRBLJPH   ;AVAMC/REG - UNIT PHENOTYPE BY ABO/RH ;2/18/93  09:26 ;

LRBLJPP   ;AVAMC/REG - PLATLET TX ;2/18/93  09:28 ;

LRBLJPP1  ;AVAMC/REG - PT ADM,RX SPECIALTY,ICD9CM CODES ;4/17/91  14:31 ;

LRBLJR    ;AVAMC/REG - RELEASE FROM XMATCH ;3/15/92  12:11 ;

LRBLJRB   ;AVAMC/REG - UNIT ISSUE BOOK ;2/18/93  09:30 ;

LRBLJSH   ;AVAMC/REG - BB INVENTORY SHIPMENTS ;2/18/93  09:31 ;

LRBLJT    ;AVAMC/REG - BB ITEMIZED TRANSACTIONS ;2/18/93  09:32 ;

LRBLJTS   ;AVAMC/REG - TRANSFUSION STATISTICS ;4/12/93  15:19 ;

LRBLJTS1  ;AVAMC/REG - TRANSFUSION STATS ;3/3/93  22:49 ;

LRBLJTS2  ;AVAMC/REG - TRANSFUSION STATISTICS ;9/14/89  08:54 ;

LRBLJU    ;AVAMC/REG - FIND UNITS NO DISPOSITION ;2/18/93  09:33 ;

LRBLJU1   ;AVAMC/REG - FIND UNITS NO DISPOSITION ;5/3/91  05:48 ;

LRBLJUT   ;AVAMC/REG - BB INVENTORY FINAL DISPOSITION ;3/9/94  14:02 ;

LRBLJW    ;AVAMC/REG - INVENTORY ABO/RH WORKSHEET ;7/28/93  07:29 ;

LRBLJX    ;AVAMC/REG - UNITS ON XMATCH ;2/18/93  09:36 ;

LRBLP     ;AVAMC/REG - BLOOD BANK PATIENT OPTS ;4/11/94  07:55 ;

LRBLPA    ;AVAMC/REG - GET PATIENT INSTR./TESTS ; 8/30/88  19:58 ;

LRBLPAB   ;AVAMC/REG - ANTIBODIES IDENTIFIED ;2/18/93  09:37 ;

LRBLPB    ;AVAMC/REG - PATIENT ANTIBODIES ;2/18/93  09:40 ;

LRBLPBR   ;AVAMC/REG - BB TESTS REPORT ;3/28/94  11:59 ;

LRBLPBR1  ;AVAMC/REG - BB TESTS REPORT ;3/28/94  12:02 ;

LRBLPC    ;AVAMC/REG - TRANSFUSIONS/HEM RESULTS ;2/18/93  09:42 ;

LRBLPC1   ;AVAMC/REG - PT ADM,RX SPECIALTY,ICD9CM CODES ;11/18/91  20:36 ;

LRBLPCS   ;AVAMC/REG - COMPONENT SELECTION FOR PATIENTS ;3/1/91  12:51 ;

LRBLPCS1  ;AVAMC/REG - COMPONENT SELECTION CK PT SPEC ;10/26/90  12:0 ;

LRBLPCSS  ;AVAMC/REG - PRE-OP COMPONENT SELECTION ;7/23/93  15:36 ;

LRBLPD    ;AVAMC/REG - BB PT INFO ;2/18/93  09:42 ;

LRBLPD1   ;SLC/DCM - BB PT INFO for OE/RR pt lists ;12/10/90  12:21

LRBLPE    ;AVAMC/REG - BB DATA ENTRY BY ACC # ;12/14/92  22:22 ;

LRBLPE1   ;AVAMC/REG - PATIENT DRUG LIST ;2/6/91  09:54

LRBLPED   ;AVAMC/REG - PEDIATRIC UNIT PREPARATION ;3/15/92  11:33 ;

LRBLPED1  ;AVAMC/REG - PEDIATRIC UNIT PREPARATION ;2/6/91  09:18 ;

LRBLPED2  ;AVAMC/REG - PROCESS PEDIATRIC UNIT ;2/4/93  12:07 ;

LRBLPEW   ;AVAMC/REG - BB WORKLOAD ;3/9/94  13:09

LRBLPH    ;AVAMC/REG - PATIENT DRUG LIST ;2/18/93  09:44

LRBLPIT   ;AVAMC/REG - PROLONGED TRANSFUSION TIMES ;2/18/93  09:45 ;

LRBLPP    ;AVAMC/REG - BB PATIENT PRINT OPTS ; 7/18/88  07:0 ;

LRBLPQA   ;AVAMC/REG - TRANSFUSION REQUEST DATA ;2/18/93  09:45 ;

LRBLPR    ;AVAMC/REG - BLOOD BANK PT RECORD ;2/18/93  09:46 ;

LRBLPR1   ;AVAMC/REG - BLOOD BANK PT RECORD-COND'T ;12/28/92  10:30 ;

LRBLPRA   ;AVAMC/REG - BB PT RECORD ;2/18/93  09:46 ;

LRBLPT    ;AVAMC/REG - TRANSFUSION RESULTS ;4/13/94  12:58 ;

LRBLPT1   ;AVAMC/REG - TRANSFUSION RESULTS (COND'T) ;12/11/92  07:38 ;

LRBLPTR   ;AVAMC/REG - TRANSFUSION DATA REPORT ;2/18/93  09:47 ;

LRBLPTR1  ;AVAMC/REG - TRANSFUSIONS/HEM RESULTS ;3/5/91  09:20 ;

LRBLPUS   ;AVAMC/REG - PATIENT UNIT SELECTION ;10/6/92  15:19 ;

LRBLPUS1  ;AVAMC/REG - PATIENT UNIT SELECTION ;10/28/90  10:21 ;

LRBLPUS2  ;AVAMC/REG - PATIENT UNIT SELECTION ;2/1/94  09:51 ;

LRBLPX    ;AVAMC/REG - XMATCH RESULTS ;12/13/93  08:55 ;

LRBLPX1   ;AVAMC/REG - XMATCH RESULTS (COND'T) ;9/8/92  20:30 ;

LRBLQPR   ;AVAMC/REG - PRINT UNITS/COMPONENTS ;2/18/93  09:48 ;

LRBLQST   ;AVAMC/REG - SINGLE UNIT STATUS ; 2/14/89  17:04 ;

LRBLRCT   ;AVAMC/REG - CROSSMATCH:TRANSFUSION REPORT ;2/18/93  09:50 ;

LRBLS     ;AVAMC/REG - BLOOD BANK SUPERVISOR OPTS ;3/9/94  09:42 ;

LRBLSET   ;AVAMC/REG - SET DD(65.091,.03 ;7/23/92  12:39

LRBLSSN   ;DALISC/FHS/DVR/AVAMC/REG - SSN SYNTAX CHECKER/EDIT; 11/12/88 15:30 ;

LRBLST    ;AVAMC/REG - BB SUPERVISOR ;9/18/89  10:08 ;

LRBLSTR   ;AVAMC/REG - BB SUPERVISOR ;2/18/93  09:51 ;

LRBLSUM   ;AVAMC/REG - BLOOD BANK SUMMARY ;3/28/94  12:10 ;

LRBLTA    ;AVAMC/REG - TRANSFUSION REACTION COUNTS ;7/2/93  07:05 ;

LRBLTA1   ;AVAMC/REG - TRANSFUSION REACTION COUNTS ;10/7/90  10:54 ;

LRBLTX    ;AVAMC/REG - TESTS FOR TX RELATED DISORDERS ; 2/17/88  20:59 ;

LRBLTXA   ;AVAMC/REG - TRANSFUSION FOLLOW-UP ;2/18/93  09:55 ;

LRBLU     ;AVAMC/REG - BB UTIL ;6/27/94  14:29 ;

LRBLUL    ;AVAMC/REG - BB UTIL ;4/13/93  07:17 ;

LRBLVAL   ;AVAMC/REG - OPTION VALIDATOR ;3/9/94  13:18

LRBLW     ;AVAMC/REG - STUFF WORKLOAD IN 65 ;11/5/93  10:38

LRBLWD    ;AVAMC/REG - STUFF WORKLOAD IN 65.5 ;2/7/91  18:45

LRBLWDS   ;AVAMC/REG - STUFF WORKLOAD IN 65.5 ;3/3/93  14:37

LRBLXREF  ;AVAMC/REG - SET BLOOD INVENTORY XREF ; 9/17/88  17:32 ;

LRBLY     ;AVAMC/REG - STUFF DATA IN LAB LETTERS ;2/20/89  16:15 ;

LRCAP64   ;DALISC/FHS - PURGE 64.1 FILE   LMIP PHASE 6

LRCAP67   ;DALISC/FHS - PURGE 67.9 FILE   LMIP PHASE 5

LRCAPA12  ;SLC/RJS/FHS - LAB WORKLOAD  DIVISION REPORT;8/23/91 1039;

LRCAPACC  ;SLC/RJS/FHS - LAB WORKLOAD DIVISION REPORT BY CAP CODE;8/23/91 1039;

LRCAPAM0  ;SLC/FHS - INTRO FOR MOVE WKLD DATA FROM 64.1 TO 67.9;10/14/91 08:15

LRCAPAM1  ;SLC/FHS - MOVE WKLD DATA FROM 64.1 TO 67.9;10/14/91 08:15

LRCAPAM2  ;DALISC/FHS/JBM - PHASE 2 OF LMIP DATA COLLECTION 67.9 TO ^LAH(

LRCAPAM3  ;SLC/FHS - LAB PHASE 3 LMIP DATA COLLECTION PRINT REPORT;8/23/91 1039;

LRCAPAM4  ;SLC/RS/DALISC/FHS - LMIP PHASE 4 BUILD MAILMAN MESSAGES FOR LAB LMIP WORKLOAD TRANS ;8/23/91 1039;

LRCAPAM5  ;DALISC/FHS - RCS 14-4 REPORT PART 1

LRCAPAM6  ;DALISC/FHS - RCS 14-4 REPORT PART 2

LRCAPAM7  ;DALISC/J0 - RCS 14-4 REPORT, LMIP PAGE COUNTERS ;5/10/93

LRCAPAM8  ;DALISC/J0 - RCS 14-4 REPORT LMIP PAGE PRINT ;5/10/93

LRCAPAM9  ;DALISC/FHS - RCS 14-4 REPORT LMIP SUPPLEMENT PAGE PRINT ;5/10/93

LRCAPAMP  ;DALISC/FHS - PURGE AND RE RUN LMIP PHASE 1

LRCAPAUD  ;SLC/FHS - DISPLAY WORKLOAD FOR ACCESSION ;2/13/91  11:05

LRCAPBB   ;SLC/AM/DALISC/FHS - STORE WORKLOAD FROM 65,65.5 INTO ^LRO(64.1 ;4/17/91

LRCAPD    ;SLC/AM/DALISC/FHS/J0 - WORKLOAD CODE LIST REPORT;1/16/91 15:34 ;

LRCAPDL   ;DALISC/FHS - FORMATE DATA FROM 64.03 FOR DOWN LOAD TO SPREAD SHEET

LRCAPF    ;DALISC/FHS - STUFF WKLD CODE INTO FILE 60 61.2 62.07 ETC

LRCAPMA   ;SLC/AM/DALISC/FHS/J0  -  WKLD REPORT BY MAJOR SECTION; 2/6/91@16:04

LRCAPMA1  ;SLC/AM/DALISC/FHS/J0  -  WKLD REPORT BY MAJ SCTN; 2/6/91

LRCAPMA2  ;SLC/AM/DALISC/FHS/J0 - WKLD REPORT BY MAJOR SECTION; 2/6/91

LRCAPMA3  ;SLC/AM/DALISC/FHS/J0 - WKLD REPORT BY MAJOR SECTION; 2/6/91

LRCAPML   ;SLC/AM/DALISC/FHS/J0  -  WKLD COST REPORT BY MAJ SCTN; 2/6/91@16:04

LRCAPML1  ;SLC/AM/DALISC/FHS/J0 - WKLD COST REP BY MAJ SCTN; 2/6/91@16:04

LRCAPML2  ;SLC/AM/DALISC/FHS - WKLD COST REP BY MAJ SCTN; 2/6/91@16:04

LRCAPML3  ;SLC/AM/DALISC/FHS - WKLD COST REP BY MAJ SCTN; 2/6/91@16:04

LRCAPMR   ;SLC/AM/DALISC/FHS/J0  -  SETUP WORKLOAD REPORT PARAMETERS;7-MAR-1991 14:58:24.12

LRCAPMR1  ;DALISC/J0 - WKLD STATS REPORT - STD/QC/RPT/MAN PRINT ; 4/9/93

LRCAPMR2  ;DALISC/J0 - WKLD STATS REPORT - COMMENTS PRINT ; 4/9/93

LRCAPPH   ;DALISC/FHS - PROCESS PHLEBOTOMY WORKLOAD DATA ; 09/28/93 13:04

LRCAPR1   ;DALISC/PAC/FHS/JBM - WKLD REP GENERATOR-MAIN ;10/15/92 11:15

LRCAPR1A  ;DALISC/PAC/FHS/JBM - WKLD REP GENERATOR-SELECT ;10/15/92 11:15

LRCAPR2   ;DALISC/PAC/FHS/JBM - WKLD REP GENERATOR-BUILD ;10/11/92 01:55

LRCAPR3   ;DALISC/PAC/FHS/JBM - WKLD REP GENERATOR-PRINT 1 ;10/16/92 16:49

LRCAPR3A  ;DALISC/PAC/FHS/JBM - WKLD REP GENERATOR-PRINT 2 ;10/16/92 16:49

LRCAPR4   ;DALISC/PAC/FHS/JBM - WKLD REP GENERATOR-UTILITIES ;10/16/92 16:49

LRCAPS    ;DALISC/FHS - REPLACEMENT RTN OF WKLD REP GENERATOR-MAIN ;10/15/92 11:15

LRCAPTS   ;SLC/AM/DALISC/FHS  -  TREATING SPECIALITY WORKLOAD REPORT; 2/6/91@16:

LRCAPTS1  ;SLC/AM/DALISC/FHS - PRINT TREATING SPECIALTY WKLD REPORT; 2/6/91@16:04

LRCAPU    ;DALISC/J0 - LAB CAP UTILITIES ;3/17/93

LRCAPV    ;SLC/FHS - DETERMINE WKLD CODE AND STUFF INTO 68 ;2/19/91  11:45

LRCAPV1   ;SLC/FHS - DETERMINE CAP AND STUFF INTO LRO(68 PART 1

LRCAPV11  ;SLC/FHS - CREAT NEW WKLD CODES ADDED BY THE SITE

LRCAPV1A  ;SLC/FHS - SET NEW WKLD CODE INTO ^LAM

LRCAPV1S  ;SLC/FHS - SET WKLD CODE INTO LRO(68 PART 2

LRCAPV2   ;SLC/AM/DALISC/FHS - STORE WORKLOAD FROM 68 INTO ^LRO(64.1 ;5/2/91  09:03

LRCAPV3   ;SLC/AM/DALISC/FHS - CONTINUE STORE OF CAP WORKLOAD TO 64.1

LRCAPVM   ;SLC/FHS - ADD WKLD CODES FOR MICRO VERIFICATION ;

LRCE      ;SLC/RWF/MILW/JMC - LOOK-UP ON CENTRAL ENTRY # ;2/5/91  11:29 ;

LRCENDE1  ;SLC/CJS - ORDER DELETE ;2/5/91  12:23 ;

LRCENDEL  ;SLC/CJS - ORDER DELETE ;2/5/91  12:28 ;

LRCHIV    ;SLC/RWF - SET UP O("S") VARIABLES FOR ARCHIVE. ;2/5/91  12:30 ;

LRCHIVD   ;SLC/MRH/DALISC/FHS - DEARCHIVE FROM ^LAR TO ^LR ;2/5/91  12:31 ;

LRCHIVE   ;SLC/RWF - REMOVE OLD DATA FROM PT. FILE ;8/10/89  11:11 ;

LRCHIVK   ;SLC/RWF - REMOVE OLD LAB DATA ; 12/14/87  15:46 ;

LRCKF     ;SLC/RWF - CHECK FILE FOR COHESIVENESS ; 8/30/87  17:19 ;

LRCKF60   ;SLC/RWF - CHECK FILE 60 ;4/4/89  20:36 ;

LRCKF62   ;SLC/RWF - CHECK FILE'S ACC TEST FILE ; 2/22/87  1:46 PM ;

LRCKF68   ;SLC/RWF - CHECK FILE 68 ; 8/27/87  10:32 ;

LRCKF69   ;SLC/RWF - CHECK FILE 69 ; 2/22/87  1:47 PM ;

LRCKFLA   ;SLC/RWF - CHECK LOAD LIST &amp; AUTO INSTRUMENT FILES ;2/5/91  12:32 ;

LRCKPTR   ;SLC/RWF - CHECK ^LR &amp; ^DPT CROSS POINTERS ; 8/30/87  17:20 ;

LRCONJAM  ;SLC/CJS - JAM CONTROLS ONTO ACCESSION ;2/19/91  10:31 ;

LRCYPCT   ;AVAMC/REG - CYTOPATH %POS,NEG,SUSP, &amp; UNSAT ;9/16/93  08:09 ;

LRDATEDH  ;DALISC/DRH - DATE RANGE FOR LRRS 1-14-94

LRDCOM    ;SLC/BA - REPORT OF DELETED OR EDITED COMMENTS ;2/19/91  10:32 ;

LRDIED    ;SLC/RWF - EDIT ; 8/5/87  10:38 ;

LRDIQ     ;SF/GFT/DALISC/FHS - MODIFIED LAB VERSION OF CAPTIONED TEMPLATE FILEMAN 19 ;1/10/92  10:23 AM

LRDIST    ;SLC/CJS - DATA DISTRIBUTION ;2/20/91  10:09 ;

LRDIST1   ;SLC/CJS/MILW/JMC - DATA DISTRIBUTION ;2/5/91  13:00 ;

LRDIST2   ;SLC/DM - WRITE SUMMARY OF LEVY-JENNINGS LRQC CHART ;2/5/91  13:06 ;

LRDIST3   ;SLC/CJS - DATA DISTRIBUTION ; 2/22/87  1:53 PM ;

LRDIST4   ;SLC/DCM - GRAPH ENTRY FOR OE/RR ;12/6/90  18:32

LRDPA     ;SLC/RWF/CJS - FILE OF FILES LOOKUP ON ENTITIES ;3/8/94  07:59 ; [ 10/28/93  2:46 PM ]

LRDPA1    ;AVAMC/REG - PT LOOKUP IN FILES FOR LAB ;3/28/94  10:55 ;

LRDPA2    ;AVAMC/REG - PT BLOOD BANK LOOKUP ;12/14/92  10:47 ;

LRDRAW    ;SLC/CJS - WARD COLLECTION SUMMARY ;2/19/91  10:34 ;

LREV      ;SLC/CJS - REVIEW OF LRTEST DESCRIPTIONS ;2/19/91  13:06 ;

LREXEC    ;SLC/RWF - EXECUTE CODE EXPANSION ; 6/2/86  7:54 AM ;

LREXECU   ;SLC/RWF - EXECTUE CODE UTILITY ; 3/31/88  3:54 PM ;

LREXPD    ;SLC/RWF - EXPLODE A LRTEST LIST ;2/5/91  13:15 ;

LRFAC     ;MILW/JMC/DALISC/FHS - CUM PRINT FOR FILEROOM PATIENTS TO SEPARATE PRINTER

LRFAST    ;SLC/CJS - FAST ENTRY ;2/5/91  13:15 ;10/07/93 08:16

LRFASTS   ;DALISC/FHS - ENHANCED LRFAST ROUTINE  ACCESSION/VERIFY PROCESS

LRFLAG    ;SLC/RWF - SEARCH ^LRO(68.2,INST,8, FOR FLAGED SAMP ;2/5/91  13:16 ;

LRFNDLOC  ;SLC/CJS - RETURN A LOCATION FROM ^LRO(69,LRODT,1,"AR",LRLLOC,SN) ;2/8/91  08:42 ;

LRFRSLT   ;AITC/CR - LAB DATA FUNCTION API WRAPPER ;11/04/16 2:45 PM

LRGEN     ;SLC/RWF - GENERAL REPORT FOR SELECTED TESTS ;4/5/89  14:09 ;

LRGEN1    ;SLC/RWF - GENERAL DATA DISPLAY ;2/19/91  10:35 ;

LRGEN2    ;SLC/RWF - CUMULATIVE REPORT FOR SELECTED TESTS ; 8/25/87  08:35 ;

LRGP      ;SLC/CJS/RWF - INSTRUMENT GROUP DELTA CHECK DISPLAY ;2/5/91  13:19 ;

LRGP1     ;SLC/CJS/RWF - COMMON PARTS TO INSTRUMENT GROUP VERIFY/CHECK ;2/5/91  13:21 ;

LRGP2     ;SLC/CJS/RWF - COMMON PARTS TO INSTRUMENT GROUP VERIFY/CHECK ;2/5/91  13:23 ;

LRGV      ;SLC/RWF - INSTRUMENT GROUP VERIFY DATA ;2/5/91  13:26 ;

LRGV1     ;SLC/RWF - PART2 OF INSTRUMENT GROUP VERIFY DATA ;2/8/91  09:29 ;

LRGV2     ;SLC/RWF - PART2 OF INSTRUMENT GROUP VERIFY DATA ;2/8/91  09:36 ;

LRGVG2    ;SLC/RWF - VERIFY GENERAL DATA AS A GROUP,CONT. ; 2/22/87  2:00 PM ;

LRGVGK    ;SLC/RWF - ROUTINE TO KILL A LIST OF VARIABLES ; 10/8/87  19:24 ;

LRGVK     ;SLC/RWF - KILL OFF VARIABLES FROM LRVR*,LRVER*,LRGV*,LRGP* ; 10/8/87  19:25 ;

LRGVK1    ;SLC/RWF - KILL OFF VARIABLES FROM LRTSTJAN  ;10/10/90  11:11

LRGVP     ;SLC/CJS - GROUP DATA REVIEW DISPLAY ;2/5/91  13:29 ;

LRHDR     ;SLC/CJS - HEALTH DEPARTMENT REPORT ;2/19/91  10:37 ;

LRKILL    ;SLC/CJS - CLEAN-UP AFTER LR ROUTINES ;7/28/89  17:27 ;

LRLABAR   ;SLC/FHS - LABEL BAR CODE DOWN LOAD FORMAT

LRLABEL   ;SLC/TGA - PRINTS STANDARD LABELS 3.5X15/16 ;2/6/91  08:18 ;

LRLABEL1  ;SLC/TGA - PRINTS LABELS 2X5 UNEVEN ;2/6/91  08:18 ;

LRLABEL2  ;SLC/TGA - PRINTS LABELS ORDER # FIRST ;2/6/91  08:17 ;

LRLABEL3  ;SLC/RWF - PRINTS MEDLAB LABELS ;2/6/91  08:06 ;

LRLABEL5  ;DUR/KT/AT - PRINTS ON VAF 10-1392 LABELS ;2/6/91  08:05 ;

LRLABEL6  ;SLC/FHS - BAR CODE LABELS FOR THE INTERMEC PRINTER

LRLABELA  ;SLC/RAF - INTERMEC 4100 2 LABEL PRINT BARCODE/PLAIN ;10/20/93  10:16

LRLABELB  ;SLC/JL/RAF - 10 PART LABELS FOR THE INTERMEC 4100 PRINTER

LRLABELF  ;SLC/CJS/DALISC/DRH - PRINT COLLECTION LIST (CONT.) ; 3/28/89  19:39 ;

LRLABLD   ;SLC/TGA - LABELS ON DEMAND ; 5/22/87  20:42 ;

LRLABLD0  ;DALISC/FHS/DRH - LABELS ON DEMAND FOR FUTURE LAB COLLECT

LRLABLDS  ;DALISC/FHS/DRH - PRINT SINGLE LABELS ON DEMAND FOR FUTURE LAB COLLECT

LRLABLIO  ;SLC/TGA - TESTS LABEL PRINTER ;8/8/89  11:17 ;

LRLABXOL  ;RVAMC/PLS/DALISC/FHS - REPRINT ACCESSION LABELS FOR ENTIRE ORDER ; 5/19/93  07:40

LRLABXT   ;SLC/TGA - REPRINTS DEMAND LABELS ;2/19/91  10:38 ;

LRLAM     ;SLC/CJS - STUFF AMIS DATA INTO LAM GLOBAL ;2/5/91  14:18 ;

LRLIST    ;SLC/RWF/CJS - LAB RESULTS LIST ;2/19/91  10:39

LRLISTE   ;SLC/RWF/CJS/DALISC/FHS/JBM/DRH - LAB RESULTS LIST, EXTENDED ;2/19/91  10:39

LRLL      ;SLC/RWF - LOAD LIST CONTROL ;2/19/91  10:41 ;

LRLL1     ;SLC/RWF - LOAD LIST SCAN. ;2/19/91  10:42 ;

LRLL1A    ;SLC/RWF - LOAD LIST CONTROL ; 2/23/89  17:29 ;

LRLL2     ;SLC/RWF - LOAD LIST BUILD ;2/6/91  07:45 ;

LRLL3     ;SLC/RWF - LOAD LIST BUILD UTILITY ;2/5/91  14:34 ;

LRLL4     ;SLC/RWF - LOAD LIST BUILD, CONT. (Control's) ;2/6/91  07:44 ;

LRLLP     ;SLC/RWF - LOAD LIST PRINT ;2/19/91  10:43 ;

LRLLP2    ;SLC/RWF - TRAY LIST PRINT ;2/5/91  14:37 ;

LRLLP3    ;SLC/RWF/MILW/JMC - SEQUENCE LIST PRINT ;2/5/91  14:38 ;

LRLLP4    ;SLC/RWF - SET UP DISPLAY ORDER FOR PRINT ;2/5/91  14:38 ;

LRLLP5    ;SLC/RWA/MILW/JMC- EXPANDED TRAY LIST PRINT ;2/5/91  14:39 ;

LRLLS     ;SLC/RWF - LOAD LIST FIX UP ; 8/17/87  11:16 ;

LRLLS2    ;SLC/RWF/MILW/JMC- LOAD LIST FIX UP ;2/5/91  14:40 ;

LRLLS3    ;SLC/RWF - MORE LOAD/WORK LIST CODE ;2/5/91  14:41 ;

LRLLU     ;SLC/RWF - LOAD LIST UTILITY ; 6/2/86  8:10 AM ;

LRLS      ;SLC/BA- PREINIT FOR AMIS FILE ;2/5/91  14:48 ;

LRLSR     ;SLC/RWF - REPORT SORT UTILITY ;2/5/91  14:49 ;

LRLSTWRK  ;SLC/CJS/DALISC/DRH - BRIEF ACCESSION LIST ;2/19/91  10:44 ;

LRLSTWRL  ;SLC/CJS/DALISC/DRH - BRIEF ACCESSION LIST PART 2 ;2/6/91  07:41 ;

LRLTR     ;SLC/RWF - PRINT BIG LETTERS ; 10/6/87  11:56 ;

LRLTR2    ;SLC/DCM - SET-UP LETTERS ; 6/2/86  8:11 AM ;

LRMIBL    ;AVAMC/REG - BATCH ORDERING/ACCESSION LOGING ; 8/25/87  08:37 ;

LRMIBUG   ;AVAMC/REG,SLC/CJS,BA- DISPLAY ORGANISMS ;6/5/89  09:21 ;

LRMIEDZ   ;AVAMC/REG/SLC/CJS/BA - MICROBIOLOGY EDIT ROUTINE ;4/24/89  14:35 ;

LRMIEDZ2  ;SLC/CJS/BA,AVAMC/REG - MICROBIOLOGY EDIT ROUTINE ; 2/22/89  11:16 ;

LRMIEDZ3  ;SLC/CJS/BA - MICROBIOLOGY EDIT ROUTINE CONT. ; 7/21/87  11:01 ;

LRMIEDZ4  ;DALISC/FHS - CONTINU MICROBIOLOGY EDIT ;3/24/92

LRMIHDR   ;SLC/CJS/BA - HEALTH DEPARTMENT REPORT ;2/19/91  10:46 ;

LRMILL    ;SLC/DLG - BUILD LOAD LIST FOR MICROSCAN ;4/4/89  21:38 ;

LRMINEW   ;SLC/CJS/BA - NEW DATA TO BE REVIEWED/VERIFIED ;4/24/89  14:36 ;

LRMINEW1  ;SLC/CJS/BA - NEW DATA TO BE REVIEWED/VERIFIED ; 11/23/87  16:34 ;

LRMINEW2  ;SLC/CJS/BA - NEW DATA TO BE REVIEWED/VERIFIED ;2/19/91  10:49 ;

LRMIPC    ;SLC/CJS/BA - MICROBIOLOGY CUMULATIVE PATIENT REPORT ;2/19/91 10:51 ;

LRMIPLOG  ;SLC/CJS/BA - PRINT BY LOG NUMBER ;2/19/91  10:53 ;

LRMIPSU   ;AVAMC/REG/SLC/CJS/BA - MICRO PATIENT REPORT ; 10/7/87  08:42 ;

LRMIPSZ   ;AVAMC/REG/SLC/CJS/BA - MICRO PRINT/SINGLE SPECIMEN REPORT ;2/19/91  10:55 ;

LRMIPSZ1  ;AVAMC/REG/SLC/CJS/BA - MICRO PATIENT REPORT ;2/19/91  10:57 ;

LRMIPSZ2  ;AVAMC/REG/SLC/CJS/BA - MICRO PATIENT REPORT - BACTERIA, SIC/SBC, MIC ;3/28/90  15:23 ;

LRMIPSZ3  ;SLC/CJS/BA- MICRO PATIENT REPORT - STERILITY, PARASITES, VIRUS ; 6/22/87  16:15 ;

LRMIPSZ4  ;SLC/CJS/BA - MICRO PATIENT REPORT - AFB, FUNGUS ; 6/22/87  16:17 ;

LRMIPSZ5  ;AVAMC/REG/SLC/CJS/BA - MICRO PATIENT REPORT - BACTERIA, ANTIBIOTICS ; 10/24/88  16:18 ;

LRMIS     ;AVAMC/REG - DELETE MICROBIOLOGY AUDITS ;4/26/89  14:38

LRMISEZ   ;AVAMC/REG/SLC/BA - MICROBIOLOGY INFECTION CONTROL DATA ; 2/14/89  17:10 ;

LRMISEZ1  ;AVAMC/REG/SLC/BA - MICROBIOLOGY INFECTION CONTROL DATA;4/17/91 14:29;

LRMISEZ2  ;AVAMC/REG/SLC/BA - MICRO INFECTION CTRL SURVEY ; 10/1/87  17:12 ;

LRMISEZ3  ;AVAMC/REG/SLC/BA - MICRO INF CTRL SURVEY CONT'D ; 10/1/87  17:15 ;

LRMISEZ4  ;AVAMC/REG/SLC/BA - MICRO INF CTRL SURVEY COND'T; 3/28/87  6:41 PM ;

LRMISEZA  ;AVAMC/REG/SLC/BA - MICROBIOLOGY INF CONTROL DATA ; 10/9/87  16:18 ;

LRMISEZB  ;AVAMC/REG/SLC/BA - MICROBIOLOGY INFECTION CONTROL DATA ; 7/11/87  01:50 ;

LRMISR    ;SLC/CJS/BA - INPUT TRANSFORM FOR ANTIBIOTIC SENSITIVITIES ;6/14/89  08:36 ;

LRMISR1   ;SLC/BA - INPUT TRANSFORM FOR ANTIBIOTIC SENSITIVITIES; 7/14/87 09:34;

LRMISTF   ;SLC/CJS/BA - MASS DATA ENTRY INTO FILE 63.05 ;4/24/89  14:40 ;

LRMISTF1  ;SLC/CJS/BA - MASS DATA ENTRY INTO FILE 63.05 ; 11/23/87  17:24 ;

LRMITS    ;SLC/STAFF - MICRO TREND ;10/14/92  15:59

LRMITSE   ;SLC/STAFF - MICRO TREND ENTRY ;3/4/93  17:07

LRMITSEC  ;SLC/STAFF - MICRO TREND ENTRY COMPREHENSIVE ;10/19/92  10:08

LRMITSES  ;SLC/STAFF - MICRO TREND ENTRY SELECTIONS ;10/18/92  16:03

LRMITSP   ;SLC/STAFF - MICRO TREND PROCESS ;3/4/93  16:59

LRMITSPC  ;SLC/STAFF - MICRO TREND PROCESS COUNT ;10/17/92  23:16

LRMITSPE  ;SLC/STAFF - MICRO TREND PROCESS EXTRACT ;10/28/93  15:17

LRMITSPO  ;SLC/STAFF - MICRO TREND PROCESS ORGANISMS ;3/4/93  14:54

LRMITSPS  ;SLC/STAFF - MICRO TREND PROCESS SETUP ;10/12/92  20:07

LRMITSR   ;SLC/STAFF - MICRO TREND REPORT ;10/17/92  22:52

LRMITSRH  ;SLC/STAFF - MICRO TREND REPORT HEADER ;10/12/92  20:26

LRMITSRS  ;SLC/STAFF - MICRO TREND REPORT SETUP ;11/7/93  12:33

LRMIU4    ;SLC/RWF,BA - READ MICRO ACCESSION ; 2/27/89  08:33 ;

LRMIUT    ;SLC/CJS/BA/AVAMC/REG - MICROBIOLOGY UTILITIES ; 10/9/87  16:19 ;

LRMIUT1   ;SLC/BA/MILW/JMC - INPUT TRANSFORMS FOR MICRO ; 4/5/88  4:54 PM ;

LRMIV     ;SLC/DLG - MICROBIOLOGY VERIFY AUTO INST ROUTINE ;4/24/89  14:41 ;

LRMIV1    ;SLC/DLG - LAB ROUTINE DATA VERIFICATION ;2/6/91  08:21 ;

LRMIV2    ;SLC/DLG - MICROBIOLOGY VERIFY AUTO INST ROUTINE ; 12/6/88  17:28 ;

LRMIV3    ;SLC/DLG - MICROBIOLOGY VERIFY AUTO INST ROUTINE CONT.;9/9/88 1:03 PM;

LRMIV4    ;SLC/DLG - MICRO DISPLAY ANTIBIOTICS FOR VERIFY ; 12/8/88  23:02 ;

LRMIVER   ;SLC/CJS/BA - MICROBIOLOGY CHART COPY APPROVAL ;4/24/89  14:42 ;

LRMIVER1  ;SLC/CJS/BA- MICRO CHART COPY APPROVAL CONT. ;2/19/91  11:01 ;

LRMIXALL  ;DALISC/FHS - RE INDEX "AI" "AJ" "AS" FOR ^LAB(62.06

LRMIXPD   ;SLC/BA - LAB DESCRIPTIONS ;2/6/91  08:23 ;

LRMIXR1   ;SLC/BA - X-REF FOR ANTIBIOTIC INTERPRETATION ^LAB(62.06,"AJ") ; 8/5/87  10:40 ;

LRMIXR2   ;SLC/BA - X-REF FOR DISPLAY SCREEN ^LAB(62.06,"AS",; 8/5/87  10:40 ;

LRMIXR3   ;SLC/BA - ANTIBIOTIC INTERPRETATION ^LAB(62.06,"AI", X-REF ; 4/4/87  21:05 ;

LRMIZAP   ;SLC/BA - MICRO CONVERSION ; 8/5/87  18:18 ;

LRMIZAP1  ;SLC/BA - MICRO CONVERSION ; 4/4/87  21:05 ;

LRMRSHRT  ;SLC/CJS - MULTI-RULE SHEWHART QUALITY CONTROL ;2/6/91  08:35 ;

LRNDLST   ;SLC/CJS - PRINT LIST OF NON-DRAW ORDERS ;2/19/91  11:03 ;

LRNIGHT   ;SLC/CJS/AVAMC/REG - NIGHTLY LAB CLEANUP ;6/5/90  21:08 ;

LRNIGHT1  ;SLC/DCM - NIGHTLY LAB CLEANUP (^LAM,^LRO(67.9) ;2/6/91  08:47 ;

LRNIGHT2  ;AVAMC/REG - STUFF CAP DATA INTO LAM GLOBAL ;2/6/91  08:48 ;

LRNITEG   ;SLC/FHS - INTEGRITY CHECKER FOR LAB SERVICE PACKAGE;8/3/89  17:52 ;

LRNITEGL  ;SLC/FHS - LOAD INTERGRITY FILE 69.91 ; 4/7/89  00:05 ;

LRNODRAW  ;SLC/CJS - PRINT LIST OF NON-DRAW ORDERS ;2/19/91  11:04 ;

LRNORMAL  ;SLC/RWF - TO RETURN TEST NORMALS ;2/6/91  08:54 ;

LRNPXA    ;SLC/MRH/FHS - NEW PERSON CONVERSION FOR ^LAR("Z" ; 1/23/93

LRNPXA0   ;SLC/MRH/FHS/J0 - NEW PERSON CONVERSION FOR ^LAR("Z" ; 1/23/93

LRNPXA1   ;SLC/MRH/FHS/JB0 - NEW PERSON CONVERSION FOR ^LAR("Z" ; 1/23/93

LRNUM     ;SLC/BA - NUMERIC INPUT TRANSFORM ;2/6/91  08:55 ;

LRO       ;SLC/DCM - Being replaced ;1/10/91  16:0 ;

LRO1      ;SLC/DCM - Being replaced ; 3/9/89  19:39 ;

LRO2      ;SLC/DCM - Being replaced ;1/10/91  16:01 ;

LRO3      ;SLC/DCM - Being replaced ; 7/3/89  15:07 ;

LRO4      ;SLC/DCM - Being replaced ;1/31/91  08:46 ;

LRO5      ;SLC/DCM - Being replaced ;1/10/91  16:01 ;

LRO6      ;SLC/DCM - Being replaced ; 2/14/89  18:07 ;

LRO7      ;SLC/DCM - Being replaced ;1/9/91  17:32 ;

LRO8      ;SLC/DCM - Being replaced ;1/10/91  16:0 ;

LROC      ;SLC/CJS - ORDER LIST CLEAN-UP ;2/6/91  10:46 ;

LROC1     ;SLC/CJS - TO CLEAN UP LAB ANCILLARY FILE ;2/6/91  10:53 ;

LROCM     ;SLC/FHS - WARNING MESSAGE ORDER LIST CLEAN-UP ;8/8/89  07:48

LROE      ;SLC/CJS - LAB ORDER ENTRY AND ACCESSION ;2/6/91  09:25 ;

LROE1     ;SLC/CJS - MORE ORDER ENTRY ;6/24/91  10:52 ;

LROE2     ;DALISC/FHS - CONTINUED MORE ORDER ENTRY ; 3/24/92

LROI      ;SLC/CJS - LAB ORDER INFORMATION UPDATE ; 8/25/87  08:46 ;

LROLOVER  ;SLC/CJS - ROLL OVER DAILY LAB ACCESSION NUMBERS ;2/19/91  11:07 ;

LROPT     ;SLC/BA- HELP FRAME INFO ON LAB OPTIONS ;2/19/91  11:09 ;

LROPTLST  ;SLC/FHS - LIST OPTIONS FOR VERIFICATION ;2/19/91  11:10 ;

LROR      ;SLC/CJS - LAB MODULE FOR OR ;3/29/90  16:39 ;

LROR1     ;SLC/DCM - LAB MODULE FOR OR (CONT.) ; 3/29/89  10:09 ;

LROR2     ;SLC/BA,DCM - PRINT THE DATA FOR OR REPORTS ;3/29/90  16:43 ;

LROR3     ;SLC/DCM - CANCEL,PURGE,SETUP,CLEAN EXECUTES ;11/26/90  10:10 ;

LROR4     ;SLC/DCM - MICRO DETAILED DISPLAY ON ORDERS ;4/17/91  14:29 ;

LROR4A    ;AVAMC/REG/SLC/CJS/BA - MICRO PATIENT REPORT - BACTERIA, SIC/SBC, MIC ; 3/16/88  2:41 PM ;

LROR4B    ;AVAMC/REG/SLC/CJS/BA - MICRO PATIENT REPORT - BACTERIA, ANTIBIOTICS ; 3/16/88  3:47 PM ;

LROR5     ;SLC/CJS - LAB MODULE FOR OR ; 12/5/88  09:34 ;

LROR6     ;SLC/DCM - EDIT LAB ORDERS FOR OE/RR ;9/11/89  16:55 ;

LROR6A    ;SLC/DCM - EDIT UNRELEASED LAB ORDERS FOR OE/RR ;9/11/89  16:55 ;

LROR6B    ;SLC/DCM/RWA - EDIT UNRELEASED LAB ORDERS FOR OE/RR CONT;9/11/89 16:55;

LROR7     ;SLC/DCM - RENEW LAB ORDERS ;5/1/89  17:51 ;

LROR8     ;SLC/DCM - FLAG/HOLD ORDERS ;5/1/89  17:46 ;

LROR9     ;SLC/DCM - ADD TESTS TO AN EXISTING ORDER THRU OE/RR; 9/23/88  15:15 ;2/8/91  07:29 ;

LRORD     ;SLC/CJS - LAZY ACCESSION LOGGING ;2/6/91  12:54 ;

LRORD1    ;SLC/RWF - LAZY ACCESSION LOGGING ;2/6/91  13:11 ;

LRORD2    ;SLC/CJS - MORE OF LAZY ACCESSION LOGGING ;2/6/91  12:57 ;

LRORD2A   ;SLC/FHS - CHECK FOR MAX FREQ OF ORDERS ;2/6/91  13:00

LRORD3    ;SLC/CJS - MORE LAZY ACCESSION LOGGING ;2/6/91  13:01 ;

LRORDD    ;SLC/FHS - CHECK FOR DIFFERENT URGENCY WITH IN ORDER ;2/6/91 13:05 ;

LRORDERN  ;SLC/CJS - DETERMINE NEXT LRORDER NUMBER ; 6/2/86  8:33 AM ;

LRORDIM   ;DALISC/FHS - PROCESS IMMEDIATE LAB COLLECT ALLOWABLE COLLETCTION TIMES

LRORDK    ;SLC/FHS - CLEAN UP AFTER ACCESSIONING PROCESS ;8/7/89  13:58

LRORDST   ;SLC/CJS/RWF - SET THE ORDER AND ACCESSION ;2/6/91  13:17 ;

LRORDST1  ;SLC/CJS/RWF - Being replaced ;3/29/90  16:40 ;

LROS      ;SLC/CJS - LAB ORDER STATUS ;2/6/91  13:26 ;

LROSPLG   ;B'HAM ISC/ADM - MOVE SP DATA FROM SURGICAL RECORD ;4/12/94  08:54

LROSPLG1  ;B'HAM ISC/ADM - STATUS OF SURGICAL CASE ;4/12/94  08:55

LROSPLG2  ;B'HAM ISC/ADM - COPY INFO FROM OPERATION RECORD; 09 AUG 1993  9:57 AM ;4/12/94  08:56

LROSX0    ;SLC/DCM - Being replaced ;1/29/91  14:44

LROSX1    ;SLC/DCM - Being replaced ;7/17/90  12:17

LROW      ;SLC/CJS - LAB ORDER ENTRY, WARD ;2/6/91  13:30 ;

LROW1     ;SLC/CJS - TEST &amp; SAMP ;2/6/91  13:32 ;

LROW1A    ;SLC/CJS - TEST &amp; SAMP CONTINUED FROM LROW1; 12/12/88  18:48 ;8/30/89  10:48

LROW2     ;SLC/CJS - TEST &amp; SAMPLE VERIFICATION ;2/6/91  13:49 ;

LROW2A    ;SLC/FHS - CONTINUING TEST &amp; SAMPLE VERIFICATION; ;2/6/91  13:50

LROW2P    ;SLC/TGA - PRINTS WARD COLLECT ORDER IN LAB ;2/19/91  11:11 ;

LROW2RP   ;SLC/RWA - OPTION TO REPRINT A ORDER ;2/6/91  13:55 ;

LROW3     ;SLC/CJS/MILW/JMC - LIST THE TESTS ORDERED AND ALLOW EDITING ;2/6/91  13:57 ;

LROW4     ;SLC/CJS - LAB ORDER ENTRY, WARD (CONT.) ;7/28/89  20:08 ;

LROW5     ;SLC/CJS - LAB ORDER ENTRY, WARD ;2/6/91  13:59 ;

LRPARAM   ;SLC/CJS/DALISC/FHS - SET LAB PARAMETERS ;2/6/91  14:25 ;

LRPHEXPT  ;SLC/CJS/RWF - EXCEPTION LOGIN OF ACCESSIONS ; 8/3/87  16:01 ;

LRPHITE1  ;SLC/CJS - LRPHITEM, CONT. ; 7/19/88  12:15 ;

LRPHITE2  ;SLC/CJS - LRPHITEM CONT. ; 2/23/88  10:44 ;

LRPHITE3  ;SLC/CJS/RWF- ITEMIZED LOGIN ; 9/8/87  12:39 ;

LRPHITEM  ;SLC/CJS/RWF- ITEMIZED LOGIN ;6/24/91  10:49 ;

LRPHLIS1  ;SLC/CJS - PRINT COLLECTION LIST (CONT.) ; 3/28/89  19:39 ;

LRPHLIST  ;SLC/CJS - PRINT COLLECTION LIST ;2/19/91  11:13 ;

LRPHSET   ;SLC/CJS - COLLECTION LIST TO ACCESSIONS ;2/19/91  11:16 ;

LRPHSET1  ;SLC/CJS - COLLECTION LIST TO ACCESSIONS ;7/11/90  11:50 ;

LRPHSET2  ;SLC/RWA - COLLECTION LIST TO ACCESSIONS CONT ;

LRQC      ;SLC/CJS - QUALITY CONTROL DISPLAY ; 6/2/86  8:38 AM ;

LRQCC     ;SLC/CJS - QUALITY CONTROL FOR BULL ALGORITHM ;2/6/91  14:28 ;

LRQCLOG   ;SLC/CJS - QUALITY CONTROL LOGGING ;3/28/90  15:20 ;

LRRD      ;SLC/DCM/BA - INTERIM REPORT BY PHYSICIAN ;2/19/91  11:33 ;

LRRK      ;SLC/BA - INTERIM REPORT CLEANUP ; 3/16/88  8:00 PM ;

LRRP      ;SLC/RWF/BA - PROCESS DATA FOR INTERIM REPORTS ; 11/10/88  08:48 ;

LRRP1     ;SLC/RWF/BA - PRINT THE DATA FOR INTERIM REPORTS ; 11/9/88  17:31 ;

LRRP2     ;SLC/RWF - INTERIM REPORT ;10/24/91  09:58 ;

LRRP3     ;SLC/RWF/BA - INTERIM REPORT FOR SELECTED TESTS ;2/19/91  11:38 ;

LRRP4     ;SLC/DCM - INTERIM REPORT FOR OE/RR PATIENT LISTS ;12/10/90  13:39

LRRP5     ;DALISC/JBM - COLLECTION REPORT ;10/20/92

LRRP5A    ;DALISC/JBM - COLLECTION REPORT-PRINT ;10/20/92

LRRP6     ;DALISC/J0 - LAB TEST/WORKLOAD CODE REPORTS ;12/07/92

LRRP6A1   ;DALISC/J0 - LAB TEST SUMMARY REPORT-BUILD ;11/27/92

LRRP6A2   ;DALISC/J0 - LAB TEST SUMMARY REPORT-CONDENSED ;11/27/92

LRRP6A3   ;DALISC/J0 - LAB TEST SUMMARY REPORT-DETAILED ;12/08/92

LRRP6B1   ;DALISC/J0 - WORKLOAD CODE SUMMARY REPORT-BUILD ;11/27/92

LRRP6B2   ;DALISC/J0 - WORKLOAD CODE SUMMARY REPORT-CONDENSED ;11/27/92

LRRP6B3   ;DALISC/J0 - WORKLOAD CODE SUMMARY REPORT-DETAILED ;12/08/92

LRRP7     ;DALISC/J0 - MANUAL WKLD STATS REPORT ; 5/19/93

LRRP8     ;DALISC/TNN/J0 - WKLD STATS REPORT BY SHIFT ; 4/9/93

LRRP8A    ;DALISC/TNN/J0 - WKLD STATS REPORT BY SHIFT ; 4/9/93

LRRP8B    ;DALISC/TNN/J0 - WKLD STATS REPORT BY SHIFT ; 4/9/93

LRRP8C    ;DALISC/TNN/J0 - WKLD STATS REPORT BY SHIFT ; 4/9/93

LRRS      ;SLC/DCM/BA/DALISC/FHS - INTERIM REPORT BY LOCATION (MANUAL QUEUE) ;2/19/91  11:39 ;

LRRS12    ;SLC/DCM,BA/DALISC/FHS/DRH - INTERIM REPORT BY LOCATION (MANUAL QUEUE) ;2/19/91  11:39 ;

LRRS13    ;SLC/DCM,BA/DALISC/FHS/DRH - INTERIM REPORT BY LOCATION (MANUAL QUEUE) ;2/19/91  11:39 ;

LRRSP     ;SLC/RWF/BA - INTERIM REPORT FOR SELECTED TESTS AS ORDERED ;2/19/91  11:41 ;

LRSETUP   ;SLC/CJS/DALISC/FHS - REINITIALIZE DATA FILES ;2/6/91  14:34 ;

LRSLOW    ;SLC/CJS/DALISC/FHS - MODIFIED FAST ENTRY ;2/5/91  13:15 ;

LRSMAC    ;SLC/RWF - CHEM. LAB SMAC REPORT ;2/19/91  13:08 ;

LRSOR     ;SLC/RWF/CJS - SOME SPECIAL OUTPUT ROUTINES ;2/6/91  15:19 ;

LRSOR1    ;SLC/RWF/CJS - SOME SPECIAL OUTPUT ROUTINES ; 6/2/86  8:43 AM ;

LRSORA    ;DRH/DALISC - HIGH/LOW VALUE REPORT ;2/19/91  11:42 ;

LRSORA0   ;DRH/DALISC -  Continuation of LRSORA  07-28-93

LRSORA1   ;SLC/KCM - CREATE SEARCH LOGIC ; 8/5/87  11:40 ;

LRSORA2   ;SLC/KCM/DALISC/DRH - SEARCH LAB DATA AND PRINT REPORT ;8/28/89 12:07;

LRSORA3   ;SLC/KCM - SEARCH LAB DATA AND PRINT REPORT ;8/28/89  12:07 ;

LRSORB    ;SLC/RWF - SCAN PART OF LRSORA ; 7/3/86  12:47 PM ;

LRSORC    ;SLC/RWF/DALISC/JBM - CRITICAL VALUE REPORT ; 8/30/87  17:25 ;

LRSORC1   ;SLC/RWF/DALISC/JBM - CRITICAL VALUE REPORT ; 8/30/87  17:25 ;

LRSORC1A  ;DALISC/DRH - LRSORC Continued ;07-22-93

LRSORD    ;SLC/RWF/DALISC/JBM - CRITICAL VALUE REPORT ; 8/30/87  17:25 ;

LRSORD1   ;SLC/RWF/DALISC/JBM- CRITICAL VALUE REPORT ; 8/30/87  17:25 ;

LRSORD1A  ;DALISC/DRH - LRSORC Continued ;07-22-93

LRSPDA    ;AVAMC/REG - SURGICAL PATH DATA ENTRY ; 9/11/88  17:13 ;

LRSPGD    ;AVAMC/REG - ANATOMIC PATH DESCRIPTION ;2/24/94  09:45 ;

LRSPRPT   ;AVAMC/REG - CY/EM/SP PATIENT RPT ;1/4/94  08:55 ;

LRSPRPT1  ;AVAMC/REG - SURG PATH RPT PRINT CONT. ;7/15/93  15:19 ;

LRSPRPT2  ;AVAMC/REG - SURG PATH PRINT SNOMED ;7/15/93  15:20 ;

LRSPRPTM  ;AVAMC/REG - MODIFIED PATH REPORT ;7/18/93  08:38 ;

LRSPS     ;AVAMC/REG - CY/EM/SP PATH SEARCH LROPT SELECTOR; 6/24/86 12:21 PM ;

LRSPSICD  ;AVAMC/REG - CY/EM/SP ICD SEARCH ;3/9/94  13:26 ;

LRSPSICP  ;AVAMC/REG - SEARCH BY ICD CODE PRINT ;9/14/89  19:05 ;

LRSPT     ;AVAMC/REG - AP PRELIMINARY REPORTS ;9/1/93  12:27 ;

LRSTATUS  ;SLC/FHS - TO CHECK SYSTEM STATUS OF AUTO INSTRUMENT JOBS ;11/6/89  12:03

LRSTOPC   ;DALISC/FHS - MANUALLY RECORD CLINIC STOP CODES FOR LAB

LRSTUF    ;SLC/CJS - MASS DATA ENTRY INTO FILE 63.04 ; 10/8/87  19:28 ;

LRSTUF1   ;SLC/CJS - MASS DATA ENTRY INTO FILE 63.04 ;2/6/91  15:47 ;

LRSTUF2   ;SLC/CJS - MASS DATA ENTRY INTO FILE 63.04 ;2/6/91  15:49 ;

LRU       ;AVAMC/REG - LAB UTILITY ;4/22/94  13:05 ;

LRUA      ;AVAMC/REG - ANAT PATH UTILITY ;7/15/93  15:37 ;

LRUB      ;AVAMC/REG - GET 62.5 ENTRIES ; 11/12/88  07:45 ;

LRUBL     ;AVAMC/REG - FIND PATIENT MISMATCHES  ;2/18/93  13:24

LRUC      ;AVAMC/REG - GET PATIENT LOCATION ;7/25/89  21:21 ;

LRUCE     ;AVAMC/REG - LAB COMMENT EDIT ; 6/2/86  9:03 AM ;

LRUCLR    ;SLC/CJS/AVAMC/REG - CLEAN UP WORKLIST FILE ; 11/12/88  07:55 ;

LRUCN     ;AVAMC/REG - LAB CONSULTS ;2/18/93  12:34 ;

LRUCNBB   ;AVAMC/REG - COOMBS/ANTIBODY REPORT ;02/12/89  12:30 ;

LRUD      ;AVAMC/REG - STUFF DATA CHANGES ;1/14/91  10:58 ;

LRUD1     ;AVAMC/REG - STUFF DATA CHANGE IN COMMENT FIELD ;1/14/91  09:44

LRUDEL    ;AVAMC/REG - DELETE AN AP ACCESSION NUMBER ;6/12/93  09:13 ;

LRUDIT    ;AVAMC/REG - DATA CHANGE AUDIT ;4/19/89  14:25 ;

LRUDPT    ;AVAMC/REG - POW PTS ;2/18/93  12:36 ;

LRUE      ;AVAMC/REG - RESULTS FOR SELECTED LAB TESTS ;3/3/94  12:11 ;

LRUER     ;AVAMC/REG - ERROR TRACKING ;2/22/94  07:03 ;

LRUET     ;AVAMC/REG - RESULTS FOR A TEST RANGE ;2/18/93  12:43 ;

LRUFILE   ;AVAMC/REG - FILE OUTLINE ;2/18/93  12:46 ;

LRUG      ;AVAMC/REG - GET LRDFN ;8/23/93  09:18 ;

LRUL      ;AVAMC/REG - PATIENT UTILITY LIST ;6/14/92  11:03

LRULA     ;AVAMC/REG - EDIT LOCATION ;3/9/94  13:28 ;

LRULB     ;AVAMC/REG - LAB LOG-BOOK ;2/18/93  12:48 ;

LRULB1    ;AVAMC/REG - LAB LOG-BOOK CONT. ;3/3/94  14:28 ;

LRULEN    ;AVAMC/REG - BYTE COUNT FOR ACCESSIONS ;5/9/91  18:19 ;

LRUMD     ;AVAMC/REG - MD SELECTED LAB RESULTS ;3/10/94  09:13 ;

LRUMD1    ;AVAMC/REG - MD SELECTED TESTS/PATIENTS ;6/16/93  13:24 ;

LRUMD2    ;AVAMC/REG - MD SELECTED TESTS/PATIENTS ;2/18/93  12:57 ;

LRUMDF    ;AVAMC/REG - DEFAULT TEST LIST ;8/11/93  17:51 ;

LRUMDM    ;AVAMC/REG - MD SELECTED LAB RESULTS ;8/24/93  15:01 ;

LRUMDP    ;AVAMC/REG - MD SELECTED LAB RESULTS ;3/10/94  09:16 ;

LRUMDS    ;AVAMC/REG - MD SELECTED PATIENT GROUPS ;10/15/91  19:22 ;

LRUMDU    ;AVAMC/REG - MD SELECTED TEST UTILITY ;1/21/94  08:17 ;

LRUMDU1   ;AVAMC/REG - MD SELECTED TEST UTILITY ;2/18/93  13:01

LRUMI     ;AVAMC/REG - MICRO RREJCTED SPECIMEN REPORT ;10/6/93  11:52 ;

LRUMSG    ;AVAMC/REG - SEND SPECIAL MESSAGE ; 12/14/88  09:16 ;

LRUP      ;AVAMC/REG - GET PARENT FILE DATA ; 5/2/88  18:23 ;

LRUPA     ;AVAMC/REG - LAB ACCESSION LIST:DATE &amp; TEST ;3/3/94  09:42 ;

LRUPA1    ;AVAMC/REG - LAB ACCESSION LIST COND'T ;3/3/94  10:07 ;

LRUPA2    ;AVAMC/REG - LAB ACCESSION LIST BY PAT ;2/18/93  13:07 ;

LRUPAC    ;AVAMC/REG - LAB ACCESSION COUNTS BY DATE ;2/18/93  13:08 ;

LRUPACA   ;AVAMC/REG - LAB ACC COUNTS BY LOC ;2/18/93  13:09 ;

LRUPACS   ;AVAMC/REG - LAB ACCESSION COUNTS BY SHIFT ;2/18/93  13:09 ;

LRUPACT   ;AVAMC/REG - LAB ACC COUNTS BY TREATING SPECIALTY ;9/30/93  11:57 ;

LRUPAD    ;AVAMC/REG - LAB ACCESSION LIST BY DATE ;3/3/94  10:38 ;

LRUPAD1   ;AVAMC/REG - LAB ACCESSION LIST COND'T ;3/3/94  10:40 ;

LRUPAD2   ;AVAMC/REG - LAB ACCESSION LIST BY PATIENT ;2/18/93  13:11 ;

LRUPQ     ;AVAMC/REG - LAB RESULTS BY ACCESSION AREA ;2/18/93  13:12 ;

LRUPQ1    ;AVAMC/REG - LAB RESULTS BY ACCESSION AREA (COND'T) ;3/8/94  09:03 ;

LRUPS     ;AVAMC/REG - PATIENT SPEC LOOK-UP ;8/5/91  13:42 ;

LRUPT     ;AVAMC/REG - PATIENT TESTS ORDERED BY DATE ;3/4/93  11:23 ;

LRUPUM    ;AVAMC/REG - USER MANUAL ;3/9/94  13:31

LRUQ      ;AVAMC/REG - CHECK FOR BAD POINTERS TO LAB FILE ;2/18/93  13:13

LRUR      ;AVAMC/REG - LAB TEST COUNTS BY SPECIMEN ;2/18/93  13:14 ;

LRURG     ;AVAMC/REG - TRANSFER ROUTINES ;5/5/91  06:51 ;

LRUSE     ;AVAMC/REG - ENTER/EDIT SNOMED FIELDS ; 6/2/86  9:12 AM ;

LRUSET    ;AVAMC/REG - RELEASE REPORTS ; 8/5/87  10:43 ;

LRUSNOM   ;AVAMC/REG - ANATOMIC PATH REFERENCES ;4/12/94  10:15 ;

LRUSP     ;AVAMC/REG - ADD/DELETE SPECIAL STAIN ; 10/9/87  16:26 ;

LRUT      ;AVAMC/REG - TIME DIFFERENCES ; 8/22/88  21:0 ;

LRUTA     ;AVAMC/REG - DISPLAY LAB TEST INFO FOR LAB ; 2/14/89  17:18 ;

LRUTAD    ;AVAMC/REG - ADD/DELETE LAB TEST/PROCEDURE ; 11/12/88  09:34 ;

LRUTELL   ;AVAMC/REG - FIND EXISTING ACCESSION NUMBER ; 6/2/86  9:13 AM ;

LRUTL     ;AVAMC/REG - GENERAL LAB UTILITY ;6/21/93  09:25 ;

LRUTRAN   ;AVAMC/REG - TRANSFER ^LR(LRDF,LRSS, TO ^LR(LRDFN#2,LRSS, ;5/9/91  18:24 ;

LRUTT     ;AVAMC/REG - LAB TEST TURNAROUND TIME; 12/23/88 12:45 ;6/12/93 12:22 ;

LRUTW     ;AVAMC/REG - DISPLAY LAB TEST INFO FOR LAB ; 2/14/89  17:19 ;

LRUU      ;AVAMC/REG - FIND FIELD FOR A SUBSCRIPT &amp; PIECE ; 9/2/87  09:35 ;

LRUV      ;AVAMC/REG - EDIT REF FILE ;3/9/94  13:38 ;

LRUW      ;AVAMC/REG - ACCESSION AREA WORKLIST ;2/22/94  07:21 ;

LRUWG     ;AVAMC/REG - SINGLE TEST WORKLIST ;2/22/94  09:45 ;

LRUWK     ;REG/AVAMC - WORKLOAD UTILITY ;8/20/93  06:57

LRUWL     ;AVAMC/REG - DISPLAY WORKLOAD FOR ACCESSION ;3/9/94  13:40

LRUWLF    ;AVAMC/REG - FILE #68 UTILITY ;3/28/91  16:07 ;

LRVER     ;SLC/CJS - LAB ROUTINE DATA VERIFICATION ;6/24/91  15:45 ;

LRVER1    ;SLC/CJS - LAB ROUTINE DATA VERIFICATION ;2/7/91  15:19 ;

LRVER2    ;SLC/CJS - LAB ROUTINE DATA VERIFICATION ;2/7/91  11:36 ;

LRVER3    ;SLC/CJS - DATA VERIFICATION ;2/7/91  11:43 ;

LRVER3A   ;SLC/CJS - DATA VERIFICATION ;2/7/91  11:46 ;

LRVER4    ;SLC/CJS - LAB ROUTINE DATA VERIFICATION ;2/7/91  12:03 ;

LRVER5    ;SLC/CJS - LAB ROUTINE DATA VERIFICATION ;2/7/91  12:04 ;

LRVR      ;SLC/CJS - LAB ROUTINE DATA VERIFICATION ;3/28/90  17:06 ;

LRVR1     ;SLC/CJS - LAB ROUTINE DATA VERIFICATION ;3/28/90  17:14 ;

LRVR2     ;SLC/CJS - LAB ROUTINE DATA VERIFICATION ; 10/9/87  16:29 ;

LRVR3     ;SLC/CJS - LAB ROUTINE DATA VERIFICATION ; 11/17/88  16:17 ;

LRVR4     ;SLC/CJS - LAB ROUTINE DATA VERIFICATION ; 2/21/89  21:06 ;

LRVR5     ;SLC/CJS - LAB ROUTINE DATA VERIFICATION ;4/20/89  18:02 ;

LRVRKIL   ;DALISC/FHS - LAB ROUTINE DATA VERFICATION VARIABLE KILLER ;03/24/92 17:30

LRVRW     ;SLC/CJS - LAB ROUTINE DATA VERIFICATION BY WORKLIST; 6/2/86 9:18 AM ;

LRWD      ;SLC/RWF - DISPLAY NAMES OF PATIENTS WITH RECENTLY VERIFIED DATA ;2/7/91  12:06 ;

LRWLHEAD  ;SLC/DCM - WORKLIST HEADINGS ;2/8/91  07:34 ;

LRWLST    ;SLC/CJS,RWF- ACCESSION SETUP.  LROE1,LRSTIK &amp; LRFAST CALL HERE ;2/28/91  08:37 ;

LRWLST1   ;SLC/CJS/RWF - ACCESSION SETUP ;2/7/91  12:21 ;

LRWLST11  ;SLC/CJS,RWF - ACCESSION SETUP ;2/7/91  13:34 ;

LRWLST12  ;SLC/CJS/RWF/FHS - ACCESSION SETUP ; 9/9/87  15:41 ;

LRWLST13  ;SLC/CJS/RWF - ACCESSION SETUP ; 1/7/87  12:12 PM ;

LRWLST2   ;SLC/CJS/RWF - ACCESSION SETUP ;2/7/91  13:37 ;

LRWRKIN1  ;SLC/DCM/CJS - LRWRKINC, CONT. ; 2/22/87  11:39 AM ;

LRWRKINC  ;SLC/DCM/CJS - INCOMPLETE STATUS REPORT ;2/19/91  11:47 ;

LRWRKLS1  ;SLC/CJS/DALISC/DRH - LRWRKLST, CONT. ;2/7/91  14:29 ;

LRWRKLST  ;SLC/CJS/DALISC/DRH - LONG ACCESSION LIST ;2/19/91  11:46 ;

LRWRKS    ;SLC/RWF - WORK SHEET ACCESSION LIST ;2/19/91  11:48 ;

LRWRKS2   ;SLC/RWF/MILW/JMC - WORK SHEET ACCESSION LIST PART 2;2/7/91  14:48 ;

LRWU      ;SLC/RWF/MILW/J - UTILITY FUNTIONS ; 12/28/88  11:04 ;

LRWU1     ;SLC/RWF/DALISC/FHS - ORDERING/ACCESSION UTILITIES ;6/5/89  16:25 ;

LRWU2     ;SLC/RWF - UTILITY # 2 ; 8/5/87  11:12 ;

LRWU3     ;SLC/RWF - COLLECT STARTING AND ENDING DATES FOR REPORTS ; 7/23/87 14:17 ;

LRWU4     ;SLC/RWF - READ ACCESSION ;2/7/91  14:49 ;

LRWU5     ;SLC/RWF/BA - ADD A NEW DATA NAME TO FILE 63 ; 5/15/87  22:53 ;

LRWU6     ;SLC/RWF/BA - MODIFY AN EXISTING DATA NAME ; 5/19/87  23:54 ;

LRWU7     ;SLC/BA - ADD A NEW ANTIBIOTIC TO FILE 63 ; 5/15/87  23:31 ;

LRWU8     ;DALOI/WPW - TOOL TO FIX ORGANISM SUBFILE AND DATA ;06/06/12  16:06

LRWU8A    ;DALOI/TCK - TOOL TO FIX ORGANISM SUBFILE &amp; DATA-PART 2 ;06/18/12  1

3:32

LRWU9     ;DALOI/CKA - TOOL TO DETECT, FIX, AND REPORT BAD DATA NAMES ; 15 Apr

2019  2:27 PM

LRWU9A    ;HPS/DSK - TOOL TO DETECT, FIX, AND REPORT BAD DATA NAMES ;Apr 11, 2

019@16:00

LRX       ;SLC/BA - UTILITY ROUTINES -- PREVIOUSLY ^LAB("X","...");2/8/91 07:30 ;

**LR pre- and post- init routines**

LRIPOS    ;SLC/FHS - POST INIT V 5.2 [ 06/09/94  7:08 PM ]

LRIPOS2   ;AVAMC/REG - SET DD(65.091,.03 PART OF LRINIT POST INITS V 5.2;7/23/92  12:39 [ 06/09/94  6:46 PM ]

LRIPOS3   ;SLC/RWA/DALISC/JRR - LR POST INTI UPDATE MENU OPTIONS ;2/8/91  07:37 ;

LRIPOS4   ;DALISC/FSH - LR POST INIT CONTINUED

LRIPOSXM  ;DALISC/PAC - SEND MAIL MESSAGE TO LAB DEVELOPERS ;7/10/92  12:35

LRIPRE    ;SLC/FHS/REG - PRE-INIT FOR VERSION 5.2 AFTER USER COMMIT;10/18/90 13:36 ;

LRIPRE1   ;SLC/AM/DALISC/FHS - WKLD (CAP) CODE LIST REPORT PRE INSTALL/INIT 5.2 ;1/16/91 15:34 ; [ 06/09/94  6:20 PM ]

LRIPRE2   ;DALISC/J0 - PURGE OBSOLETE WORKLOAD DATA

LRIPRECK  ;SLC/FHS - PRE-INIT ENVIRONMENT CHECK FOR VERSION 5.2 ;10/18/90 13:36 ;