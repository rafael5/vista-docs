---
app_name: Laboratory (LA and LR)
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
package_id: LR
patch: null
patch_gap: null
section: ''
source_file: lab5_2um.docx
status: draft
title: lab5 2um.docx
---

LABORATORY

USER MANUAL

<!-- image -->

Version 5.2

September 2024

**Department of Veterans Affairs (VA)**

**Office of Information and Technology (OIT)**

Revision History

| **Date**       | **Page**                   | **Description**                                                                                                                                                                                                                                                                                                                                                                                     | **Author**                                         |
|----------------|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| September 2024 | 103                        | LR*5.2*574:  A note was added that results which are auto released do not trigger automatic printing of the Interim Report.                                                                                                                                                                                                                                                                         | REDACTED                                           |
| September 2020 | 99, 102, 107, 140          | LR*5.2*527:  - Accessioning Menu: **Reprint** - deleted "Removing an accession [LRDELOG]" - Accessioning Menu Options: **NOTE:** , **NOTE:** , and **2** – Added two electronic signature notes and removed a “removing an accession” section - Ward Lab Menu Options: **NOTE:** - Added an electronic signature note - Updated Title page, Revision History, Table of Contents, Index, and Footers | Liberty ITS  REDACTED                              |
| May 2018       | 32-33,  89  36-39          | Patch LR*5.2*476 – Added new FileMan report for Historical Lab Results and included note under the Cumulative Report topic.  Added information to Microbiology Results Entry regarding batch entry of preliminary comments for accessions.                                                                                                                                                          | REDACTED                                           |
| February 2018  | Title Page, 12, 61-62, 143 | Patch LR*5.2*495 – Updates include two new options within the Microbiology menu, the Edit Inactive DT Multiple - ETIOLOGY File (MIME) and Edit Inactive DT Single - ETIOLOGY File (MISE). These options allow the populating/editing of a new inactive date field that has been added to the ETIOLOGY FIELD File (#61.2).                                                                           | Mantech Mission, Solutions and Services  REDACTED. |
| Sept 2017      | 87 & 88                    | Patch LR*5.2*497 – Updated option description for "Interim reports by location (manual queue)"                                                                                                                                                                                                                                                                                                      | REDACTED                                           |
| Nov 2016       | 105                        | Patch LR*5.2*465 – This patch enables multidivisional facilities to customize the number of labels required for each site in LABORATORY TEST File (#60) by adding two new fields that can be configured for a specific lab test at a specific facility: The INSTITUTION EXTRA LABELS field (#60.15,.01) and the NUMBER OF LABELS subfield (#60.15,1).                                               | REDACTED                                           |
| June 2005      | 62-64                      | Patch LR*5.2*257- The Microbiology Trend Report [LRMITS] option is enhanced to sort the ‘Antimicrobial Trend Report’ by DIVISION.                                                                                                                                                                                                                                                                   | REDACTED                                           |
| June 2005      | 147                        | Patch LR*5.2*257- The Microbiology Trend Report [LRMITS] option is enhanced to sort the ‘Antimicrobial Trend Report’ by DIVISION.                                                                                                                                                                                                                                                                   | REDACTED                                           |

Preface

The Laboratory User Manual Version 5.2 is designed to help Laboratory staff and ward personnel to use the Laboratory package. The Laboratory Information Manager (LIM) may want to train Laboratory staff and other users with this manual as the basic text.

For technical information and guidance, the user should consult the Laboratory Technical Manual V. 5.2. For LIM implementation information, see the Laboratory Planning and Implementation Guide.

**Table of Contents**

Introduction	1

About This Manual	1

Intranet	1

Special Notations	1

Audience	2

How to use this Manual	4

Before you Begin	4

New User	4

Experienced User	5

Laboratory Information Manager (LIM)	5

Benefits of Installation	6

Using the Software	6

Laboratory Menu	8

Microbiology Menu	8

Package Management	11

Package Operation	12

Menu Description	12

Laboratory Security Keys	13

Workflow - General Laboratory	16

Diagram of Laboratory Package Workflow	17

Collection of Specimens	18

Data Modification	29

Special Reports	30

Using the Microbiology Module	33

Accessioning	33

Microbiology Results Entry	36

Entry of Antimicrobial Susceptibility Results	40

Preliminary vs. Final Reports	42

Verification and Report Generation; Supervisory Review	45

Microbiology Automated Verification	46

Work Documents	65

Results Lookup	66

Special Output	68

MIME Edit Inactive DT Multiple - ETIOLOGY File	70

MISE Edit Inactive DT Single - ETIOLOGY File	71

Instrumentation/Interfacing	73

Load/Work List	73

Unidirectional Communications	75

Supervisors/Selector of Instrumentation	78

Bidirectional Communications	79

Lab Software	80

Handshake Routines (Bidirectional)	81

The Processing Routine	81

Bidirectional Routines	81

Checklist For Instrument Interface	82

Instrument Interface Trouble Shooting	83

Reports and Outputs	89

Cumulative Report	89

Cumulative Report Generation	89

How the Cumulative is Formatted	90

Rerun Options of the Cumulative	93

Interim Reports	96

Interim Report Menu Options (Manual)	97

Supervisor’s Report	102

Lab Menu Options	103

Laboratory VistA Menu [LRMENU	103

Phlebotomy Menu [LR GET]	104

Phlebotomy Menu Option Descriptions	106

Accessioning Menu [LR IN]	110

Accessioning Menu Option Descriptions	112

Process Data in Lab Menu Option Descriptions	125

Quality Control Menu [LRQCM]	144

Quality Control Menu Option Descriptions	144

Results Menu [LR OUT]	148

Results Menu Option Descriptions	149

Information-Help Menu [LRHELP]	156

Information-Help Menu Option Descriptions	156

Ward Lab Menu [LRWARDM]	159

Ward Lab Menu Option Descriptions	160

Anatomic Pathology [LRAP]	170

Blood Bank LRBL]	170

Microbiology Menu [LRMI]	172

Microbiology Menu Option Descriptions	172

Supervisor Menu [LRSUPERVISOR]	182

Supervisor Menu Option Descriptions	190

Glossary	227

Index	233

### Introduction

#### About This Manual

The Laboratory module is part of the integrated Veterans Health Information Systems and Architecture () software, which automates the manual procedures used in the following laboratory areas:

1. Ordering of tests and procedures on both patient and non-patient specimens

2.	Collection and Accessioning of specimens into the Laboratory database

3.	Processing and analysis in appropriate department or work areas

4.	Review and verification of results

5.	Reporting of results and/or diagnoses for clinical health care treatment

6.	Analysis and reporting of quality control data used in generating results

7.	Providing management statistical data as well as requirements for accreditation by regulating bodies and agencies

#### Intranet

Documentation for this product can now be found on the VA Intranet. You will find it at the following address:

http://vista.med.va.gov/vdl/

This address will take you to SD&amp;D’s Virtual Documentation Library (VDL) page where you will find a list of available end-user documentation for current applications.

#### Special Notations

In this manual, the user’s response is in bold type, but will not appear on the screen as bold. The bold part of the entry is the letter or letters that must be typed so that the computer can identify the response. In most cases, you need only enter the first few letters. This increases speed and accuracy.

Every response you type must be followed by pressing the return key (or enter key for some keyboards). Whenever the return or enter key should be pressed, you will see the symbol **&lt;RET&gt;** . This symbol is not shown but is implied if there is underlined and bold input.

Throughout the package, help frames may be accessed from most prompts by entering one, two, or three question marks (?, ??, ???).

Within the examples representing actual terminal dialogues, the author may offer information about the dialogue. This information is enclosed in brackets (e.g., *[Select Print Device])* and will not appear on the screen.

#### Audience

The Laboratory/Pathology module is a clinically oriented application, designed to provide data to health care providers as well as to other health care personnel. For this reason, it is a multifaceted module with many spins off advantages for other hospital services. Its primary function is to assist the Laboratory/Pathology Service in managing and automating workload generated by health care providers.

The Health Care Provider

The module provides a method for the provider to place requests into the system for collection and analysis of patient specimens. It also provides a means of tracking work activities to completion and reporting. When results become available, users may view the results in a variety of formats.

The Pathology and Laboratory Service

- The module provides methods for identifying and processing the workload.
- All processing labels, accessioning numbers, and work sheets are automated.
- Test result values are accepted from manual input and/or automated instruments.
- Test data is displayed and reviewed by laboratory personnel for accuracy.
- Data is not available for clinical use until of data has been verified by appropriate Laboratory personnel.
- After verification, the results can be automatically distributed to the appropriate locations by the module.
    - Data are provided for management reports and administrative support.
    - Data are collected to satisfy regulatory bodies who accredit the institution. These data are capture automated and are available on demand

#### How to use this Manual

This manual is designed to show users (lab and ward personnel) how to:

Enter, edit, or display information for

| Ordering     | Reports          |
|--------------|------------------|
| Accessioning | Lab tests        |
| Worklists    | Auto Instruments |
| Results      | Print reports    |

Option descriptions are arranged according to lab menus, with a description of the prompts and possible responses. Many of the options described here have examples following the description.

Sections can be rearranged to fit the menu design that your station chooses, or compiled into smaller user manuals for individual sections.

Anatomic Pathology and Blood Bank options are contained in separate manuals.

#### Before you Begin

##### New User

If you are unfamiliar with the Laboratory package or other  software applications, we recommend that you study the DHCP (Decentralized Hospital Computer Program) *User’s Guide to Computing.* This orientation guide is a comprehensive handbook benefiting first time users of any  application. The purpose of the introductory material is to help you become familiar with basic computer terms and the components of a computer. It is reproduced and distributed periodically by the Kernel Development Group. To request a copy, contact your local Information Resources Management (IRM) staff.

- Get an access code from your supervisor, find out which terminal, and test data you should use.
- Read and familiarize yourself thoroughly with the Orientation section.
- Read the Package Operation section to get an idea of how the overall package works.
- Check with your supervisor for instructions about your menu choices.
- See the glossary for computer and lab terminology.

Other manuals that Information Resource Management (IRM) or your Laboratory Information Manager (LIM) have that you may want to use as you become familiar with the package are:

- Anatomic Pathology User Manual
- Blood Bank User Manual

##### Experienced User

Read the Orientation section that will explain how this manual is written. Some of the conventions have been changed since the last issue of this manual.

Use the Table of Contents or Index to go directly to the options that you want more information about.

Other manuals that IRM or your LIM have that you may want to use, as you become more experienced with the intricacies of the package are:

- Laboratory Technical Manual
- Laboratory Security Guide
- Anatomic Pathology User Manual
- Blood Bank User Manual
- Users Guide to Computing
- VA FileMan User’s Manual

##### Laboratory Information Manager (LIM)

Be sure to read the Laboratory Release Notes to familiarize yourself with the new version of the Laboratory package.

Skim the Orientation section to familiarize yourself with the new conventions used in this manual.

Be sure that you have available a complete set of the following manuals.

(It is recommended that a complete set be kept in your work area.)

- Users Guide to Computing
- VA FileMan User Manual
- Laboratory Release Notes
- Laboratory Installation Guide
- Laboratory Technical Manual
- Laboratory Security Guide
- Blood Bank User Manual
- Anatomic Pathology User Manual

As of Version 5.2, the FileMan options will not be exported with the Laboratory package. The LIM should arrange with their IRM to have the necessary options added to their secondary menus.

#### Benefits of Installation

- Lab test information is more accurate, timely, and accessible.
- Status of orders is more accessible to lab and ward personnel.
- Transcription of test results is more convenient.
- Analyses of data can be compared.
- Automated (instrument) data entry reduces transcription errors.
    - Abnormal and critical values can be flagged, to assist in review of data.
    - Quality control data can be collected, automatically performed, and reported.
    - Test descriptions and requirements are available to lab and ward personnel on all tests performed.
    - Delta checks can be made on a series of data to establish trends or significant clinical variations in value.
    - Special reports can be generated such as: total lab workload during a period of time, progress reports on all tests in progress, turnaround time, Supervisor Summaries, anatomic pathology QA, and blood bank inventory and tracking epidemiological studies.

#### Using the Software

You will usually see a menu when you first sign on to any  software. This menu lists the different options you may select from. Frequently when you select an item on a menu, you will see another menu asking you to select again. You may need to go through several levels of menus before you reach the specific option you require. This series of menus is called a *menu tree* .

Once you are familiar with the option names, you can request that the lists not appear on the screen (however entering a “?” will show you the entire option list). This can help speed up the response time on your system. Contact your LIM to have this done.

NOTE	Each user can use the User’s Toolbox menu (TBOX) menu on their secondary menu to “Edit User Characteristics” to make this change.

##### Laboratory Menu

The main laboratory menu, available to the LIMs and supervisors, appears as follows:

1	Phlebotomy menu...

2	Accessioning menu...

3	Process data in lab menu...

4	Quality control menu...

5	Results menu...

6	Information-help menu...

7	Ward lab menu...

8	Anatomic pathology...

9	Blood bank...

10	Microbiology menu...

11	Supervisor menu...

Some customized menus may appear different from this example. The ellipses (...) following a menu indicate this is a menu containing options or sub menus.

Each of these menu items, when selected will display another menu. For example, if you choose 10, Microbiology Menu, another menu will be displayed. (If menu items are numbered, you can enter either the number or the first letter(s) of the option or menu you wish to select.)

##### Microbiology Menu

MIME	Edit Inactive DT Multiple - ETIOLOGY File

MISE	Edit Inactive DT Single - ETIOLOGY File

RB	Results entry (batch)

RE	Results entry

VS	Verification of data by supervisor

VT	Verification of data by tech

WKLD	Review accession workload

Accessioning, standard (Microbiology)

Batch accessioning

Lab statistics menu...

Long form accession list for microbiology

Microbiology print menu...

References...

Results menu...

Short accession list

Show list of accessions for a patient

STD/QC/REPS/MANUAL WKLD COUNT

Supervisor menu...

Some of these are options, and some are menus (as you can see by the three dots). The letters before an option name, for example, RB, are called a synonym and are short cut ways of selecting the option. If you select Microbiology Print menu... for example, you will see:

All results for selected accessions

Cumulative patient report

Health Department report

Infection control survey report

Long form accession list

Microbiology trend report

Patient report

Short accession list

### Package Management

The Laboratory software package makes use of Current Procedural Terminology (CPT) codes which is an American Medical Association (AMA) copyrighted product. Its use is governed by the terms of the agreement between the Department of Veterans Affairs and the AMA.

The Workload (WKLD) codes are based on the College of American Pathologists (CAP) codes. The CAP codes are used with the permission of the . Specific instruments and products are referenced by the Workload codes. These references should not be perceived as endorsement or approvals by the  system or the Laboratory software package.


### Package Operation

#### Menu Description

The lab options are exported as menus, which group the options with similar functions together into general categories, as follows:

**Menu	Function**

Phlebotomy Menu [LR GET]	Options the lab uses to get (collect) the

test orders and specimens

Accessioning Menu [LR IN]	Options the lab uses to put the orders 	in (enter into) the system
Process Data in Lab Menu [LR DO!]	Option the lab uses to do (process) the 	work on the specimens
Quality Control Menu [LRQCM]	Options for maintaining quality 
	assurance
Results Menu [LR OUT]	Options the lab uses to report or send

outpatient test results
Information-Help Menu [LRHELP]	Options the lab uses to obtain 
	additional “help” or information about 	tests, orders, make inquiries, etc.

Ward Lab Menu [LRWARDM]	Options used by the ward personnel to 	place orders, make inquiries, etc.
Anatomic Pathology [LRAP]	Options used by the Anatomic Pathology module
Blood Bank [LRBL]	Options used by the Blood Bank 	module
Microbiology Menu [LRMI]	Options related to the microbiology 	section
Supervisor Menu [LRSUPERVISOR]	Options used by supervisors to perform

specialized functions in the lab

#### Laboratory Security Keys

The laboratory package supplies various security keys that act as follows:

Some routines check for user security keys. If you do not have the appropriate security key assigned to you, the routine will not work for you.

Certain options and menus are “locked” with security keys. These keys are used as locks for particular options, and are checked elsewhere during the execution of the option. In some cases, the lack of the appropriate security key will prevent you from seeing an option although you have been assigned a menu that normally contains that option.

If one of your fellow workers can use/see an option that you cannot, compare the security keys that you have to the keys that he/she has. You can see which keys that you have by signing onto the computer and use the option Display User Characteristics that is found on your (TBOX). You should see something similar to the following example.

LABUSER, ONE   (#153)DEVICE: 7mLAT-TERM27m  ($I: \_LTA7913:)JOB: 7m5414969

ENVIRONMENT                             ATTRIBUTES

-----------                             -----------

Site ........  ISC                Type-ahead ....... Y

UCI ......... INV,VER                   Time-out ......... 300

Signed on ... 11:33                     Fileman code(s) .. @

Terminal type C-VT320

KEYS HELD

---------

LRLAB          LRVERIFY       LRSUPER        LRLIASON

LRMICRO        LRBLOODBANK    LRANAT         LRPHSUPER      LRPHMAN

LRBLSUPER      LRAPSUPER      LRSP           LRCY           LREM

LRAU           LRMIVERIFY     LRSS           LRBLAH         LRLAISON

MENU PATH

---------

Systems Manager Menu (EVE)

User's Toolbox (XUSERTOOLS)

Display User Characteristics (XUUSERDISP)

Last Device Used: \_LTA7913:

This display tells you a lot. It tells you what account you are in (this one is in the INV,VER UCI at the Dallas ISC). The security keys are listed. The Menu Path shows how the user got to this option.

By comparing your user characteristics to your colleague’s user characteristics, you can tell your LIM exactly which keys you do not have. However, each user of the Lab package will have the appropriate “keys” assigned for their level of access by their supervisor or LIM. A user that is in Chemistry will not be assigned the LRMICRO (Microbiology) key unless the tech will need to work in the Microbiology department. Therefore, you may not have a key that a coworker has because you work in different areas or have different levels of responsibilities.

Following is a list of the Lab keys:

**Key	Users**

LRANAT	Anatomic Pathology users*

LRAPSUPER	Anyone allowed to use the Anatomic Pathology

Supervisor Menu and edit SNOMED codes

LRAU	Autopsy Module users*

LRBLOODBANK	Blood Bank users

LRBLSUPER	For Blood Bank supervisory level decisions

LRCY	Cytology Module users*

LREM	Electron Microscopy Module users*

LRLAB	Laboratory Personnel only

LRLIASON	Laboratory Application Coordinator

LRMICRO	Microbiology users

LRMIVERIFY	Microbiology personnel*

LRSP	Surgical Pathology Module users*

LRSUPER	Laboratory Supervisors

LRVERIFY	Anyone who is authorized to verify lab results

LRPHMAN	Phlebotomists*

LRPHSUPER	Supervisor of the phlebotomy collection team

* These keys may be used to lock menu options, as the site deems appropriate.

#### Workflow - General Laboratory

The following sections attempt to explain how different combinations of the lab options may be used to:

- Collect and receive specimens ordered for scheduled collection into the lab, with or without the collection lists and labels (Microbiology is covered in a different section).
    - Receive specimens into the lab at any other time
        - Organize the workload onto various types of lists or work documents
            - Enter, review, verify, and modify test results
                - Identify and/or generate various lists to be retained in the lab for record-keeping purposes.
            Each topic lists the procedure(s), some general comments (if applicable), and the specific options used. The diagrammed flow chart on the next page shows some of the basic pathways specimens may take as they are processed into and out of the lab.

#### Diagram of Laboratory Package Workflow

##### Collection of Specimens

Without Collection List/Labels

###### Manual slips only

Blood collection can be performed in the same manner as before the implementation of the computer system. Manual slips are used to request tests and are brought back to the lab with the manually labeled specimens obtained by the phlebotomist. When the work arrives in the lab, the test requests are entered into the computer using the Multipurpose accessioning [LRQUICK] option that assign an order number and an accession number which should be written on the lab request slips. A label will be generated and place on the corresponding tubes of blood. A phlebotomist, lab clerk, aide, or technologist (in their respective departments or areas) can perform the accessioning process. The slips are used to keep a tally of the work to be done as the specimens are processed before testing.

**Comments:** This system of collection very closely mirrors most the previous manual system, and will not require any major adjustments to existing procedures. It will also greatly decrease the amount of initial computer training the lab personnel will need. Bottlenecks in the flow of work into the lab may be created if all of the specimens are arriving to be accessioned into the system at the same time. This system does not allow the use of computer generated labels for the blood draw, or does it provide information to the wards regarding the collection status of the specimens.

This option is only recommended for low volume samples drawn by ward or clinic staff or other special remote collection sites.

With Collection List/Labels

###### Manual slips, Order numbers

Manual slips with test requests to be drawn during the routine lab collection can be sent to the lab either the night before or early the morning of the scheduled collection. The test requests are entered into the system and given order numbers using the Fast lab test order (ROUTINE) [LROW ROUTINE] option. After all requests have been entered, the software will combine all of the order and generate a collection list (that is to be given to the phlebotomist to use on the wards). The software also assigns all of the orders an accession number using the Create new collection list [LRTASK PHSET] or Print collection list/labels [LRPHLIST] options. The labels are placed on the specimens as it is collected. The labeled specimens and collection lists are brought back to the Laboratory by the phlebotomist after the collections are done. The specimens received are entered into the computer as “collected” or “not collected” (“or canceled”) using the Itemized routine lab collection [LRPHITEM] option or Receipt of routine lab collection from wards [LRPHEXCPT] option.

The reason(s) for any cancellations are also entered at the same time. After the confirmation of the receipt of collected specimens into the computer has been completed, the labeled specimens are distributed to each location. The accessions are now available for inclusion on any Laboratory work/load lists. Also a list of specimens which were not collected, as well as the reasons for cancellation can be printed and kept in the Lab for reference using the List of orders not collected [LRNODRAW] option. This list is also available to the wards using the Ward collection summary [LRDRAW] option.

Options To Use:  	Fast lab test order (ROUTINE) [LROW ROUTINE]

Create new collection list [LRTASK PHSET] or

Add to collection list [LRPHMAN]

i.Print collection list/labels ;[LRPHLIST]

Itemized routine lab collection [LRPHITEM] or

Receipt of routine lab collection from wards [LRPHEXCPT]

List of orders not collected [LRNODRAW]

Ward collection summary [LRDRAW]

###### 1 Ward order entry, Lab collect

Test requests for blood orders to be drawn as part of a scheduled lab collection may also be entered directly from the wards or other remote location using ward order entry. The test orders are entered into the computer by the ward clerk or physician using the Lab test order [LROW] or Fast lab test order [LROW ROUTINE] options. Those orders are retained by the Laboratory software and combined when the collection list is created using the Create new collection list [LRTASK PHSET] or Add to collection list [LRPHMAN] options. The lab can then print the collection list and labels by using the Print collection list/labels [LRPHLIST] option for use during the draw. Receipt of the specimens collected and cancellation of those not collected (with the appropriate comments) is acknowledged using the °Itemized routine lab collection [LRPHITEM] or Receipt of routine lab collection from wards [LRPHEXCPT] options to release the accessions for generation of work documents in the lab. The labeled specimens are then distributed to each lab area for processing. Also, a list of specimens which were not collected, as well as the reasons for cancellation, may be printed and kept in the lab for reference by using the List of orders not collected [LRNODRAW] option.

This list is also available to the wards by using the Ward collection summary [LRDRAW] option. This method is just like the previous one, except the ward personnel directly enter the test and manual slips do not have to be generated.

Options To Use:	Lab test order [LROW] or Fast lab test order [LROW ROUTINE]

Create new collection list [LRTASK PHSET] or

Add to collection list [LRPHMAN]

Print collection list/labels [LRPHLIST]

Itemized routine lab collection [LRPHITEM] or

Receipt of routine lab collection from wards [LRPHEXCPT]

List of orders not collected [LRNODRAW]

Ward collection summary [LRDRAW]

Organizing Your Workload

After the specimens have been collected, received or logged in, and been assigned accession numbers, the following types of lists or work documents may be generated for the purposes of organizing the work to be done in each lab department and for tracking down problems:

1. **Load/work lists** - In many larger labs, it may be less cumbersome to use load or work lists as lists of pending accessions or to indicate what work needs to be done in a certain area. The format of these lists is determined by the field entries for each load/work list name in the LOAD/WORK LIST file (#68.2).

When using load or work lists, it is generally a good idea to start fresh at the beginning of each shift, by clearing any unverified data using the Clear instrument/worklist data [LRINSTCLR] option and unloading the list sequence using the Unload load/work list [LRLLCT] option before you attempt to create or build using the i.Build a load/work list; [LRLL] and Print a load/work list [LRLLP] options, the first load/work list of the day. You can limit or specify which accessions appear on the list by requesting the list to build a specified range of accession numbers or specified profile onto the list. Profiles and the tests they contain are defined in the LOAD/WORK LIST file (#68.2). Remember, if you are running an interfaced auto instrument on-line, you must have a load/work list defined for it and associated with that instrument in the AUTO INSTRUMENT file (#62.4). A specified urgency or range of urgencies can build a load or work lists and accessions can be entered on a list only when the tests ordered exactly match the tests defined in the list profile.

Example: 	If a load list profile consists of two tests, T3 and T4, the list can be specified to build only the accessions that have both T3 and T4 ordered on the list. Accessions having only a T3 ordered would NOT be built onto that list. The load or work list that has been created can now be used to find the appropriate specimens, aliquot samples, label sample cups, etc.

The lists can also be manipulated in order to allow you to insert using the Insert a sample on a load/work list [LRLLINST] option, move using the Move a load/work list entry [LRLLMOVE] option, and remove using the Remove a load/work list entry [LRLLREMV] option samples onto and off the lists as originally built, if desired.

Options To Use: 	Clear instrument/worklist data [LRINSTCLR]

Unload load/work list [LRLLCT]

Build a load/work list [LRLL] and

Print a load/work list [LRLLP]

Insert a sample on a load/work list [LRLLINST]

Move a load/work list entry [LRLLMOVE]

Remove a load/work list entry [LRLLREMV]

1. **Incomplete test report** - This list or report will display patient name, social security number, location, test name, order urgency, and accession number, as well a status of the incomplete test(s). The report may be requested for a given accession area or for a selected group of tests within an accession area.

Option To Use: Incomplete test status report [LRWRKINC]

1. **Long form accession list** - This list gives a detailed printout of all the pending accessions for a given accession area. It may be requested by specific date or range of dates, specific tests, and/or by incomplete tests only. This list may also be used as a worklist or as a replacement for manual logbooks or worksheets. It can also be useful to use as a checklist at the end of each shift for finding any specimens that have not been run, or determining the work which is leftover and will be run during the next shift.

Option To Use: Long form accession list [LRACC1]

1. **Short accession list** - This option produces an abbreviated form of the above “long form” list. It displays the accession number, patient name, test name, and status of any incomplete tests. The list may also be generated after test results have been entered, as it will display the verified test results for single tests, and then can be used for a hard copy of the results to be left in the lab for reference.

Option To Use: Short accession list [LRACC2]

NOTE:	The following types of lists or work documents may be generated for the purposes of tracking down problems.

1. **Show list of accessions for a patient** - This option lists all accessions which have been received in the lab for a given patient, and can be used to help locate a missing specimen if only the patient name is known. (Display only, you cannot print this report.)

Option To Use: Show list of Accession for a patient [LRUPT]

1. **Review by order number** - This option can be of help when trying to find a specimen when all the information available is the order number.

Option To Use: Review by Order number [LRCENLKUP] (display only, you cannot print this report).

1. **Lookup accession** - This option lists all the information available in the system about a single accession, by accession number, and can be used to track down a misplaced specimen.

Option To Use: Look up accession [LR LOOKUP ACCESSION] (Display only, you cannot print this report.)

1. **List of orders not collected** - This list, which is generated after receipt of specimens from a routine scheduled collection, can also be consulted when trying to find a missing specimen. If, during the receiving process, a specimen or group of specimens from a single ward location is overlooked, the system will not release those accessions, but leave them with a status of on collection list (when using the option Receipt of routine lab collections from wards [LRPHEXCPT], or with a status of canceled (when using the option Itemized routines lab collection [LRPHITEM].

Option To Use: List of orders not collected [LRNODRAW]

1. **Alternate types of lists** - You may also choose to gather specimens and perform the requested analyses based on the information printed on the accession labels which are placed on the specimens themselves (and not create a list of any kind). Or, to use extra labels printed at the time of specimen collection or accessioning to manually build a work list, by placing the labels onto an appropriately titled page of a log book or worksheet as the specimens arrive in the particular area of the lab. Additional labels can also be printed using the Reprint labels option to attach to log books or worksheets.
###### Data Entry, Review, and Verification

###### Manual Tests Not On A Load or Work List

If you are using a long form or short accession list, manual list created from labels, log entries, or the information on the accession label placed on each specimen as your method of workload organization, and the tests are performed manually (in other words, NOT on an interfaced instrument), you may:

**Function	Option**

| a)	Enter, review, and verify the test results individually, prompted by accession number in numerical sequence   | Enter/verify/modify data (manual) [LRENTER]                                                   |
|---|-----------------------------------------------------------------------------------------------|
| b)	Enter and verify a test result for a range or batch of accessions, in which you can specify whether or not to automatically “stuff” a result or specify the result for each accession within the group   | Batch data entry (chem, hem, tox, etc.) [LRSTUF]                                              |
| c)	Enter the results individually and review those results as a group, with the option of obtaining a hard copy of the review   | Enter/verify/modify data (manual) [LRENTER]  Group data review (verified &amp; EM) [LRGVP]    |
| d)	Enter and review the results individually or in groups  and verify those results for a specified range of accessions.   | Enter/verify/modify data (manual) [LRENTER]  or Group data review (verified &amp; EM) [LRGVP] |
| e)	Order, accession, enter results, review results, and verify the results of a test after performing the test.   | Bypass normal data entry [LRFAST]                                                             |
| f)	Accession, enter results, review results, and verify the results of a test after performing the test. This would be used for specimens brought to the lab with an order number already assigned through ward order entry.   | Accession order then immediately enter data [LR ACC THEN DATA]                                |

###### Manual Tests on A Load or Work List

If you are performing the tests by manual methods or running them on an instrument which is NOT interfaced, and you have created load or work lists to better organize these accessions, you may:

**Function	Option**

| a)	enter, review, and verify each result or set of results individually, prompted by either load list tray/cup number or  by worklist sequence number   | Enter/verify data (load list) [LRVRW2]  Enter/verify data (Work list) [LRVRW]                                                                                            |
|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| b)	enter the results individually,      review them as a group, with the option of obtaining a hard copy of the review   | Enter/verify data (load list)[LRVRW2] or Enter/verify data (Work list) [LRVRW] or Enter/verify/modify data (manual) [LRENTER]  Group unverified review (EA,EL,EW) [LRGP] |
| c)	enter and review the results individually  or in groups and  verify those results in a “batch” or group.   | .Enter/verify data (Work list) [LRVRW2] or Enter/verify data (Work list) [LRVRW]  Group unverified review (EA,EL,EW) [LRGP]  Group verify (EA,EL,EW) [LRVRW2]            |

###### Tests Run on-line with an Interfaced Instrument

1. If you are running the tests on the instrument by load list, you may:

**Function	Option**

| a)	review data transmitted from the instrument through the LSI to the computer individually prompted by load list tray/cup number    | Enter/verify data (load list) [LRVRW2]     |
|---|--------------------------------------------|
| b)	review data transmitted from the instrument through the LSI to the computer individually (auto instrument) prompted by accession number order   | Enter/verify data [LRVR]                   |
| c)	review data transmitted from the instrument through the LSI to the computer in a group   | Group unverified review (EA,EL,EW) [LRGP]  |
| d)	verify data reviewed by any method individually prompted by load list tray/cup number   | Enter/verify data (load list) [LRVRW2]     |
| e)	verify data reviewed by any method individually prompted by accession number order   | Enter/verify data (auto instrument) [LRVR] |
| f)	verify data reviewed by any method in a group   | Group verify(EA,EL,EW) [LRVRW2] or [LRGV]  |

2. If you are running the tests on the instrument by accession, you may:

**Function	Option**

| a)	review data transmitted from the instrument through the LSI to the computer individually prompted by accession number order   | Enter/verify data (auto instrument) (“EA”) [LRVR]   |
|---|-----------------------------------------------------|
| b)	review data transmitted from the instrument through the LSI to the computer in a group   | Group unverified review (EA,EL,EW) [LRGP]           |
| c)	verify data reviewed by any method individually, prompted by accession number order   | Enter/verify data (auto instrument)  (EA) [LRVR]    |
| e)	verify data reviewed by any method in a group   | Group verify (EA,EL,EW) (GA) [LRGV]                 |

##### Data Modification

###### Before Verifying The Data

Changing or modifying entered data **before** it is verified may be accomplished by using the same methods as were used to enter the data originally. Any of the following options may be used:

1. Enter/verify/modify data (manual) [LRENTER]

2. Enter/verify data (load list) [LRVRW2]

3. Enter/verify data (worklist)  [LRVRW]

4. Enter/verify data (auto instrument) [LRVR]

###### After Verifying The Data

Changing or modifying entered data **after** it is verified may be accomplished by using the option Enter/Verify/Modify Data (manual) [LRENTER]. This is the **only** option which can be used to modify **previously verified** data!

NOTE: 	You cannot use the Bypass Normal Data Entry [LRFAST] or Accession Order then Immediately Enter Data [LR ACC THEN DATA] options, to modify data. This is because the “starting” point of each of these two options references the patient name or the order number, respectively. These options will not allow you to reference an already existing Accession #.

##### Special Reports

Various specialized reports exist that may be used by the Lab for quality control, quality assurance, and daily review and summary purposes. They include:

1. **Search for abnormal/critical flagged results** - finds any test results which are outside of the established or defined critical (panic) value ranges, or are otherwise abnormal (i.e., have failed a delta check, etc.), within a specified time span.

**OPTION:** [LRSORD]

2. **Search for critical value flagged tests** - finds any test results which have exceeded the critical value limits defined in the LABORATORY TEST file (#60), within a specified time span.

**OPTION:** [LRSORC]

3. **Search for high/low values of a test** - finds any results equal to, less than, or greater than the value you specify for a given test or group of tests, within a specified time span.

**OPTION:** [LRSORA]

4. **Quality control display (Levey-Jennings)** - will display the quality control data for a test or group of tests by a given lab control name (as defined in the LAB CONTROL NAME file (#62.3)), for a set number of time points. This is a highly specialized format which indicates the actual value of the control sample, and plots it against the established mean and +/- 1, 2, and 3 standard deviations on the display.

**OPTION:** [LRQC]

5. **Summary lists** - various reports which summarize large groups of data include:

a) **Supervisor’s report** - generated with a format similar to the daily cumulative reports; by date.

**OPTION:** [LRACS MANUAL]

b) **Summary list (supervisor’s)** - generated with a format similar to the long form accession list, with or without verified test results; by date.

**OPTION:** [LR SUP SUMMARY]

c) **Print a full patient summary** - lists all data in the computer for a given patient; inverse or forward chronological order. (“Working copy” of the cumulative.)

**OPTION:** [LRAC FULL PATIENT SUMMARY]

6. **Historical Lab Results** - The LRRESULT function defined in the FUNCTION (#.5) file enables reporting on lab results through FileMan. This function enables reporting on lab results for a specific patient, specimen type, and lab test, looking back over a specified number of days. This functionality applies only to lab tests with verified results for patients currently admitted.

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

#### Using the Microbiology Module

##### Accessioning

Two options are provided for accessioning specimens in the Microbiology package.

These are:		Accessioning, Standard (Microbiology) [LRMICROLOGIN]

Batch Accessioning [LRMIBL]

“Multipurpose accessioning” can also be used; however, once you choose the MICROBIOLOGY accession test group, you will be working with an option identical to Accessioning, Standard.

Standard accessioning can be used for any accessioning situation. It allows any specimen to be accessioned for any number of tests (including those not in the accession test group). It allows the entry of one line (68 characters) of free text (or Lab Descriptions codes screened “A” (Order comments)) describing the specimen or order. For smaller hospitals or those with an evening or night shift with a reduced specimen volume, most accessioning will be done with this option.

“Batch accessioning” is very useful in the situation where a large number of the same type of specimens all have the same test requested. After specifying once the test requested, site/specimen, and urgency, you do not need to enter these again for subsequent patients. Like the standard accessioning option, one line of Order comments is available. This option is much faster for a high volume lab. However, it has the limitation of allowing only one test per specimen/accession.

Additional tests can be added to an accession via the Add Tests to a Given Accession [LRADD TO ACC] option found in the Accessioning Menu. Likewise, Delete a Test from an Accession [LRTSTOUT] is found in the Accessioning Menu. The package requires that a reason be given for deletion, or else no action will be taken. It should be noted that “Order comments that have a screen on them” Lab Descriptions codes will **not** expand out if used in this option.

NOTE: This option does not remove the test from an active load/worklist.

Four files have been provided to accession non-patient specimens:

The STERILIZER file (#67.2):	for accessioning spore strips or other means of Autoclave Performance Testing

The ENVIRONMENTAL file (#67.3):	for accessioning specimens from environmental sources, such as water, dialysate solutions, or other equipment

The RESEARCH file (#67.1):	for accessioning specimens from laboratory animals or non-patients, such as CAP proficiency testing

The REFERRAL PATIENT file (#67):	for accessioning specimens referred from other hospitals or laboratories (REFERRAL file (#67) **renamed** REFERRAL PATIENT file (#67))

These files are accessible via both the standard and batch accessioning options by entering the first letters ( e.g., RES or REF respectively for Research or Patient Referral files) of the name of the file, followed by a colon at the “Select Patient Name:” prompt. This is called “using extended file syntax”. The files will **not** be accessible if you enter the letters incorrectly and then get the “Select PATIENT NAME:” (ALL CAPITAL LETTERS) prompt. Should the latter prompt appear, you will need to leave the menu, return to the menu and re-enter the desired accessioning option to obtain the first prompt. The option Manually Accession QC, Environmental, etc. [LRQCLOG] can also be used.

**Example 1:** Correct entry

Select Patient Name: **STE:**

File: STERILIZER

Select STERILIZER NAME:

or

Select Patient Name: **S: Autoclave #1**

**Example 2:** Incorrect entry

Select Patient Name: **STE;**

Select PATIENT NAME:

In most cases, no demographic data exists for these files (unless, for example, you specifically set up your STERILIZER file (#67.2) with all the required information for each sterilizer at your site before you start), so the user will need to provide this information. Once entered, the data will be displayed the next time a specimen from that source is accessioned.

##### Microbiology Results Entry

There are two options available for the manual entry of Microbiology results:

•	RE Results Entry [LRMIEDZ]

•	RB Results Entry (Batch) [LRMISTUF]

Most results will be entered using the RE option. It allows entry of such information as organism(s) isolated, the amount of growth obtained, comments on that organism, and results of susceptibility testing where indicated, as well as general “report remarks” on the specimen as a whole. Depending on the edit code chosen in File #60 (points to EXECUTE CODE file (#62.07)), for each test you will see a different set of prompts. For example, those tests utilizing PARASITOLOGY will ask what stage(s) of the parasite was observed and will not ask for susceptibility results; ANTIBIOTIC LEVEL only allows entry of the name of a drug, draw time (peak, trough, random), and its level.

The various “comments” and “remarks” fields point to the LAB DESCRIPTIONS file (#62.5) and, as mentioned in the Laboratory PIG Manual, Screens are available to allow selective entry of only certain codes yielding expanded messages. Free text or combinations of codes and text are also allowable. Standard FileMan word-processing rules of error correction and deletion are followed.

RB Results Entry, (Batch) is used to enter results on many reports at once. However, only Gram Stain, Acid Fast Smear, Preliminary Comment, and the various Smear/Prep and Report Remarks (BACT, Parasite, Mycology, and TB) can be edited — you cannot batch Organism, Quantity, Comment, or Susceptibility Results. (These are known as “the Major Fields to Edit.”) There are three types of batching. These are,

1.	Automatically enter your entry,

2.	Prompt with your entry,

3.	Just prompt.

Type one is the fastest but least flexible method. It would be useful for a group of cultures all being reported with the same results, such as “no growth at 24 hours.” You tell the computer once what you want entered, indicate the accession numbers (either entered individually or as a range (“1-24” for example)) and it does the rest.

Type two would be used when most of the cultures would get the same results, but a few are different, such as urine where most are “&lt;1000 CFU/ML” but some are “&lt;10,000 CFU/ML.” After telling the system you want “&lt;1000 CFU/ML” entered and entering the appropriate accession numbers, it will scroll through each number, showing you &lt;1000 CFU/ML//. For those which are to get that result, just press RETURN, but for the “&lt;10,000s” you would enter that result instead, after the “//.”

Type three is the slowest but most flexible method. You need only specify the numbers to be edited and you can then enter any result (different for each accession, if necessary) as it appears upon the screen. More than one line of information can be entered.

RB allows for reporting either preliminary of final results, and for completing the individual test or leaving it incomplete. Results can be entered using RB **only** if the selected test on an accession number is not completed. If it is completed (accidentally or if for some reason additional or amended results must be entered), RE must be used.

The prompt, “Do you wish to make a new entry for the XXXX field? NO//” appears after all data has been batched into the selected accession numbers. It is most useful in type one batching, which only allows entry of one line of data. It allows you to batch another set of results without having to exit and re-enter the option.

You can use RB Results Entry (Batch) to enter the same preliminary comment for multiple accessions. For example, a site might process hundreds of urine cultures daily. Instead of entering "No growth after 24 hours" as a preliminary result individually for each applicable accession, you can enter the same preliminary result for all applicable accessions at once.

Preliminary comments are entered using the following fields:

- PRELIMINARY BACT COMMENT (#1) for Bacteriology accessions
- PRELIMINARY MYCOLOGY COMMENT (#20.5) for Mycology accessions
- PRELIMINARY TB COMMENT (#26.5) for Mycobacteriology accessions

Details on files, fields, and data used in this process are available in the *Laboratory Technical Manual* .

The following procedure illustrates data entry for Bacteriology accessions in the MICROBIOLOGY work load area.

1. 	Select options as shown below for the MICROBIOLOGY work load area. At the “Enter the field to edit:” prompt, choose 1 PRELIMINARY BACT COMMENT.

Figure 1: Preliminary Comment Batch Entry (Example 1)

<!-- image -->

2. 	Select options as shown below. At the “Enter #’s:” prompt, enter the accessions to which a preliminary comment will be assigned.

Figure 2: Preliminary Comment Batch Entry (Example 2)

<!-- image -->

3.	Enter the preliminary comment that applies to the accessions identified. In this example, the comment NO GROWTH IN 24 HOURS has been entered.

Figure 3: Preliminary Comment Batch Entry (Example 3)

<!-- image -->

**NOTE** : The RE Results Entry [LRMIEDZ] option can be used to display preliminary comments previously entered.

##### Entry of Antimicrobial Susceptibility Results

Each antimicrobial can store three values: a result, an interpretation, and a display screen. The result may be semi-quantitative (S, R, I, etc.) or a numeric value (MIC value). Entering a result will automatically stuff an associated interpretation and display screen (determined from the ANTIMICROBIAL SUSCEPTIBILITY file (#62.06). These may be set up to be organism and/or specimen specific. A display screen is used to suppress the display of results and interpretations to non-laboratory personnel. Three screens are available: “A” - always display, “N” - never display, or “R” - restrict display unless all interpretations that are always displayed are resistant.

The section Adding New Antimicrobials and Creating Templates, in the PIG Manual, describes the procedure for entering MIC results and the appropriate interpretations and screens into File #62.06. In most cases, all the technologist will need to do in Results Entry is enter the MIC value, and the system will “stuff” the correct interpretation, and will also “know” whether or not to display the results to the ward users. Occasionally, a situation will occur where one or the other will need to be changed. The entry of interpretations and/or screens may be accomplished in two ways:

1.	Entering the value in the specific antibiotic Interpretation and Screen fields. These fields are generally available when entering “YES” to the “Any other antibiotics?” prompts, and then entering “^ antibiotic name.” The availability of these fields is determined by the edit template that is entered in the Micro Other Template in the LABORATORY SITE file (#69.9).

2.	While entering an antimicrobial result, you can use a “*” to force a susceptibility interpretation or screen.

•	4 enters the result “4” without affecting the interpretation or screen

•	4*S enters the result “4” and the interpretation S (screen unaffected)

•	4**N enters the result “4” and the screen “Never Display” (interpretation 	unaffected)

•	&lt;2*S*R enters the result “&lt;2,” the interpretation “S” and the screen 	“Restrict Display”

•	*, *S, 4*, 2**, 4*N*S, and 4**X are examples of invalid entries

If you record results for a drug which is not included in your primary edit template defined for a particular etiology, it can be accessed by entering an up-arrow (^) at any antimicrobial prompt. The system will ask Any other Antibiotics? If you answer “YES,” you will be asked Select ANTIBIOTIC: You must then enter the name of the Antibiotic, preceded by an up-arrow (^). This will jump you to the appropriate subfield in your “OTHER” edit template in File #63. Failure to enter the up-arrow (^) will put you into the results entry mode used by the MIC/MBC test in File #60 (edit-type execute code MIC/MBC), except that you will not be able to enter the results for that antimicrobial. (You will have to add MIC/MBC to that accession number to enter the results.

##### Preliminary vs. Final Reports

Until you are very familiar with the package, you may find that the concept of preliminary or final reports is a tricky one to understand. The “P” or “F” really have no bearing on whether a test is completed or not, it is there merely for the physician’s reference.

The edit code, as previously mentioned, determines whether the test is considered Bacteriology, Mycology, Parasitology, etc. Much confusion can arise, particularly in the case of an Accession Area comprised of a group of tests with more than one edit code, such as the example of a “STOOLS” accession area. Such an area could include Bacteriology tests (Enteric culture, Campylobacter culture, C. difficile culture/toxin, etc.) and Parasitology tests (Parasite exam, Occult Blood, Fecal Fat, etc.). It must be thoroughly explained that the status for BACTERIOLOGY *must* remain “P” until *all* Bacteriology tests are completed, and likewise, the Parasitology status must remain “P” until all those tests are completed.

Consider an example of a tissue specimen accessioned for Gram Stain, Culture &amp; Susceptibility, KOH, and Fungal Culture.

NOTE:	We are assuming in this example that these four tests are all in the same accession area and therefore only one accession number was assigned to that specimen.

The first results you enter would probably be the Gram Stain. The BACTERIOLOGY REPORT STATUS remains “P,” even though the test is completed at the end of reporting, because the C&amp;S, which also gets edited as a BACT test, is still pending. It will remain “P” until the last time you enter results on the C&amp;S, at which time the status must be changed to “F” and the C&amp;S marked “completed.”

Likewise, the status of those two tests will have no bearing on that of the KOH or Fungal Culture, since these are controlled by the MYCOLOGY RPT STATUS. As described above, the status will remain “P” after the KOH is completed (even if the BACT status is already “F”!) and will not be changed to “F” until the Fungal culture is completed.

You may find it preferable **not** to pre select a test to be edited in the RE option. Without selecting a specific test, as each accession number is entered, you will see a list of tests accessioned for that number, along with the word “completed” where applicable. This can facilitate deciding whether or not the status should be changed to “F”.

A few more comments on Preliminary, Final, and Completed:

Smear/prep tests are internally completed as soon as the number is requested for results entry, even if no results are entered. Be aware of this!

The “XXXX RPT STATUS:” prompt applies to ALL tests in the XXXX report group, although it appears on INDIVIDUAL tests. You *must* answer this prompt with either **P** for PRELIMINARY or **F** for FINAL. It has *nothing* to do with whether results will be released outside the laboratory, **or** test completion status. Remember, a test can be marked “completed” and still retain the status of “preliminary”!

The “SELECT XXXX RPT REMARK:” prompt applies to ALL tests in the XXXX report group, although it appears on INDIVIDUAL tests. Be sure the results you enter adequately explain what test they belong to (See “Setting up your files” LAB DESCRIPTIONS file (#62.5) in the PIG Manual).

The “XXXX RPT DATE APPROVED:” prompt applies to ALL tests in the XXXX report group, although it appears on INDIVIDUAL tests. If a DATE is entered in this field, then ALL tests in the XXXX report group will be **automatically released** outside the laboratory. If there is a date in this field, the last tech to **see it, even if nothing is altered,** will have his user code displayed with the test results on EVERY report outside the laboratory. The “XXXX RPT DATE APPROVED:” prompt has **nothing** to do with test completion status, OR whether the report is PRELIMINARY or FINAL.

Although a test is designated “completed,” you can still change or add data to an accession number, but **only** via the RE option! Once designated “completed”, you cannot use RB to enter new or changed data.

The “completed” status can be removed by use of the “@”:

“BACTERIOLOGY DATE COMPLETED: JAN 9, 1994// “ **@** ”

Those tests automatically completed by the system (see comment #1 above) **cannot** have their “completed” status deleted without FileMan intervention.

The Preliminary Comments (LAB DATA file (#63), field 1 = BACT, 16.5 = PARASITE, 20.5 = MYCOLOGY, 16.5 = TB, 36.5 = VIRUS) are included in to some exported edit-type execute codes and may be added if desired to customized execute codes. They are unique in that any comments, results, etc., entered into the fields (they use the same screens in File #62.5 as do their corresponding Report Remark fields) can be viewed by non-Lab users only when the report status is Preliminary. Once finalized, however, only Lab users can see the comments.

Since no amended report message is automatically generated by the system at this time, it is suggested a Lab Descriptions code be used for this purpose, such as:

* * * AMENDED REPORT! * * *

which should be entered every time something is added or changed on a test previously designated as “complete” (or for other criteria as you deem necessary). It should be entered and screened for each of the Microbiology edit fields.

Likewise, some sort of system should be devised to handle the event where the wrong organism and susceptibilities were reported.

This information should *NOT* be deleted. A serious legal problem could occur if the physician begins treatment based on these results.

If the patient suffers an adverse effect from the prescribed drug and the physician then tries to go back to check the report, he/she may not be able to justify why he/she prescribed it, since it had been deleted as erroneous.

One possible system would be to have a lab description code saying “AMENDED REPORT” to use for laboratory errors and another saying “SUPPLEMENTAL REPORT” for additional work requested by the doctor, such as further identification or more antibiotics.

##### Verification and Report Generation; Supervisory Review

Verification of entered results is obtained by entering a “T” (Today) or “N” (NOW) at the prompt “BACT (MYCOLOGY, PARASITE, etc.) RPT DATE APPROVED” at the end of each accession edited in RE, or by answering “YES” to “Verify all results automatically?” in RB. This releases all entered data to be viewed by the ward. Use of the VT (Verification of Data by Tech) option is therefore unnecessary, except perhaps for lab clerks, aides, or secretaries who do not possess the LRVERIFY key and must have their work verified by a tech. (By using “N” the current time is entered with today’s date and turnaround times for Quality Assurance applications can be more accurately tracked.)

You may still prefer to use the VT or VS (“Verification of Data by Supervisor”) for supervisory review of data entered, since the “Summary List (Supervisors')” (Long form) is difficult to read for microbiology results. Both the VS and VT give a choice of displaying results as the ward will see them (suppressing those antimicrobials screened **R** estrict or **N** ever display) or as the Lab will see them (all antimicrobial results displayed, with an asterisk flagging those not screened **A** lways). VT will display all accessions edited, whereas VS is limited to those that include tests marked completed.

The LABORATORY REPORTS file (#64.5) contains a field called Micro Reports field (#3). Your procedure for enabling Micro results to print with the rest of the Laboratory cumulative will differ, depending on what your LIM selected as an entry for this field:

( **Null** ) = Micro reports will not print with the cumulatives.

An alternate means of printing must be used (e.g.,VT or VS)

**P** = Preliminary and final reports print

**F** = Final reports print

Micro Approval Method field (#11) determines what level of result verification (RE, VT, or VS) is necessary for Micro results to print with the cumulative. For further explanation, refer to the PIG manual.

#### Microbiology Automated Verification

The automated verification process attempts to blend automated procedures followed in auto instruments with the manual edit capability of the Result Entry option found under the Microbiology menu. The verification option will allow all of the features found in the standard manual verification options as well as addressing new situations posed by the automated process.

The first example represents a patient whom has no organism/isolate entered the patient’s laboratory file. Remember that if some data on an organism/ isolate has been already entered into the patient’s laboratory file, this data will also be displayed and can be edited. This example will use the MicroScan instrument.

The second example is a more involved technique that deals with data already in the patient’s laboratory file and multiple isolates of the same organism on the same specimen. If there is more than one isolate of the same organism/isolate, you must select the correct isolate to merge the data into. This will not happen very often, but the option has a method to handle just that. It allows you to add data to an existing organism/isolate in the patient’s laboratory file. It will also allow you to create an entirely new organism for the accession.

In the case of the multiple identical organism/isolate on the same specimen, the default prompt will prevent any accidental overlaying of data.

In some cases, the organism/isolate numbers may appear to skip. This is done purposefully to allow the organism/isolate to be deleted from the patient’s laboratory file, if required. Don’t be concerned if an isolate number is skipped; the data is accurate. However, if for some reason an organism/isolate is in the patient’s laboratory file, but has no quantity or no antibiotic values, it will not be displayed on the composite display. This anomaly may be, at best, confusing.

The default for Micro Approval Method is VT. This can be controlled by instrument. The field Micro Auto Approval Method (#105) in the auto instrument file (#62.4) controls this function. However, the “AVS” cross-reference used by the verification of data by supervisor is always built, no matter what is in this field, and even if the data doesn’t have to be verified by the supervisor before being released. Therefore, verification by supervisor can always be performed on automated verified data.

For details on the field entry prompts, consult your Laboratory Technical and PIG manuals. The Susceptibility edit templates used with Results Entry (RE) are used by this option.

###### Verification Flow Process

Example 1:

Verify Micro Auto Data

1.	Select ACCESSION AREA: MICRO MICROBIOLOGY

2.	Accession Date : 94// **&lt;RET&gt;** ( 1994)

3.	Select Auto Instrument MICROSCAN (F257)

4.	Enter number Part of Accession 1 // 10129 **&lt;RET&gt;**

The first prompt is the default accession area (as specified in the AUTO INSTRUMENT file (#62.4) from which you wish to verify results.

The second prompt is the default specimen accession date. The first two prompts default values will be used, if for some reason the automated instrument does not transmit data for these two fields.

The third prompt is the auto instrument, which transmits the results you wish to verify.

The fourth prompt has a default accession number. This is the first accession number in the ^LAH( global. You may select any valid accession number. If you enter a number which does not exist in the file or enter a “?” you may then choose to see a list of transmitted accession numbers. The screen shows a display of the patient and accession number demographics. This display allows you to positively identify the patient and the specimen. This display also lists comments or gram stain results if any already exist in the patient’s ^LR(file.

added to the data already transmitted. It is then possible to have partial data in the ^LAH( global.

NOTE:	Caution must be taken when verifying accessions before the entire instrument run has been completed and the transmitted data processed into ^LAH (the complete assay of a specimen may take a lot of time).

ACC # (10129)			JUL 18, 1994@09:52:46

TEST,LABPATIENT, ONE       SSN: 000-00-0001     LOC: REF

Specimen: URINE         Sample: URINE

Comment on Specimen				~MIDSTREAM URINE

Comment on Specimen :   ~MIDSTREAM URINE

**5.** Is this the correct patient/specimen ? YES// **&lt;RET&gt;** YES

TEST, LABPATIENT, ONE   000-00-0001

MICRO 94 10129

Pat Info: THIS IS A TEST

URINE  URINE

1  CULTURE &amp; SUSCEPTIBILITY

**6.** TEST #(S)  (or “ALL”): **&lt;RET&gt;**

**7.** ENTER QUANITY FOR (ESCHERICHIA COLI)  : **6U** (&gt;100,000 CFU/ML)

&gt;100,000 CFU/ML   ? YES// **&lt;RET&gt;** (YES)

The fifth prompt allows you to select a different accession number. If the specimen and patient are not correct, the accession number must be edited under other normally used options. You do not have the ability to edit patient data at this point. You can only edit specimen or test data with this option.

The next display is similar to the display found in other automated verification options. You can select which of the accessioned tests you wish to verify. Entering a return at the “Test” prompt, (the sixth prompt) is equal to an “ALL” input.

The seventh prompt allows you to enter a quantity for the first organism/isolate in the ^LAH( global. You can enter the quantity by using a lab description code or a number. If the same organism/isolate is also found in the patients ^LR( file, the quantity from the patient’s ^LR( file will be displayed as a default for you. You may accept, edit, or delete at the “Quantity” prompt. All of the organism/isolates transmitted from the auto instrument will be displayed in this manner. You are shown each isolate, which was identified and sent from the auto instrument and asked to enter the quantity. The susceptibility results will be displayed next.

**8.** Isolate (1)

ESCHERICHIA COLI

GENTAMICIN	2	S	A

CEFAZOLIN	4	S	A

AMPICILLIN	4	S	A

TRIMETH/SULFAMETH	2/38	S	A

AMIKACIN	32	I	A

PIPERACILLIN	16	S	A

CEFOPERAZONE	32	I	A

CEFTAZIDIME	4	S	A

IMIPENEM	8	I	A

AZTREONAM	16	I	A

CEFTRIAXONE	8	S	A

AMP/SULBACTAM	16/8	I	A

RETURN TO CONT. (‘^’ TO SKIP) **&lt;RET&gt;**

**9.** COMMENT ON SPECIMEN:  ~MIDSTREAM URINE // **&lt;RET&gt;**

BACT RPT STATUS: **F** FINAL REPORT

Select GRAM STAIN: **&lt;RET&gt;**

Select BACT RPT REMARK: **&lt;RET&gt;**

The next screen (#8) is a display of the antibiotics which have been transmitted for each organism/isolate. This display order of the antibiotics can be controlled in the instrument by entering a display order in the AUTO INSTRUMENT file (#62.4). This display is merely a display by organism/isolate and the antibiotic results. There will be an opportunity to edit this data later. Each organism/isolate will be displayed in turn. The “A” in the fourth column above represents the Antibiotic Screen, in which:

**A** = Always display **R** = Restrict display **N** = Never display.

If, however, you discover this data is erroneous, and should not be used or transferred from the ^LAH( global to the patient’s ^LR( file, enter a “^” at the “RETURN TO CONT. (“^” TO SKIP)” prompt and the data will be skipped completely, thereby eliminating the need to edit later.

The next four prompts (#9) allow you to enter appropriate entries to complete the verification process. You may edit, add, or delete entries at these prompts.

TEST,CU LABPATIENT, ONE SSN: 000-00-0001     LOC: REF

MICRO 94 10129  URINE  URINE

1.  ESCHERICHIA COLI  (&gt;100,000  CFU/ML )

:

SUSC	INTP

AMIKACIN	32	I

AMPICILLIN	4	S

AMP/SULBACTAM	16/8	I

AZTREONAM	16	I

CEFAZOLIN	4	S

CEFOPERAZONE	32	I

CEFTAZIDIME	4	S

CEFTRIAXONE	8	S

GENTAMICIN	2	S

PIPERACILLIN	16	S

TRIMETH/SULFAM	2/38	S

Then you will see a composite display of all organism/isolates currently in the patient’s ^LR( file. The data from the auto instrument (^LAH) has been added to the patient’s ^LR( file, but has not been removed from ^LAH( global yet. It is removed from the ^LAH( only after you enter your initials or clear the auto instrument data.

Caution must be taken that this review screen is correct and complete. The same files that normally affect the micro reports control its format.

**10.** (‘E’DIT data, ‘C’omments, ‘O’rganism, ‘W’orklist) // **O**

1  ESCHERICHIA COLI

Select ORGANISM: ESCHERICHIA COLI // **2441** STAPHYLOCOCUS AUREUS  2441

ORGANISM ISOLATE NUMBER: 2// **&lt;RET&gt;**

ORGANISM: STAPHYLOCOCUS AUREUS// **&lt;RET&gt;**

Select COMMENT: **4U** (&gt;50,000 - (75,000 CFU/ML)

Select COMMENT: **&lt;RET&gt;** (  )

Select COMMENT: **MIC** (MIC’s in mcg/ml)

Select COMMENT: **&lt;RET&gt;**

AMPICILLIN: **&gt;=16** (R)

AMP/SULBACTAM: **8** (S)

CEFAZOLIN: **8** (S)

CHLORAMPHENICOL: **8** (S)

CLINDAMYCIN: **8** (S)

ERYTHROMYCIN: **1** (S)

GENTAMICIN: **1** (S)

OFLOXACIN: **1**R** (S)   (restricted display)

OXACILLIN: **1** (S)

PENICILLIN: **&gt;=16** (R)

TETRACYCLINE: **1** (S)

TRIMETHAPRIM/SULFAMETHOXAZOLE: **2/38** (S)

VANCOMYCIN: **1** (S)

1   ESCHERICHIA COLI

2  STAPHYLOCOCUS AUREUS

The next prompt (#10) offers you four options to select from:

“E” to edit the entire accession (same as RE under the micro menu)

“C” to edit comments only

“O” to add, edit, or delete organism/isolates

“W” to edit the Load/work list

Entering an “E” will cause the verification process to behave as if you were in the manual Results Entry option. This is useful if you want to edit the entire accession data.

If you select “C”, you are able to edit the various comments on the specimen. In order to edit comments on the organism/isolate you must either select the “E” or “O” option.

The “O” entry allows you to edit, add, or delete a specific organism/ isolate. The edit templates and execute codes are honored as entered in LABORATORY TEST file (#60) and ETIOLOGY file (#61.2). You can edit organism/isolate comments with this function.

The only way to review comments sent from the autoinstrument is to select “O” or “E” to edit the organism.

There are two other possible responses to this prompt which are not displayed. These are the “@” (shift 2) and the “^” (shift 6). Both of these have the same effect. The routine will remove data which has been transferred for ^LAH( global to the patient file. It will only delete data that it has transferred. However, if the option transfers all of the data found in a patient’s file for a given organism/ isolate, the entire organism/isolate will be removed. Remember, the data are still stored in the ^LAH( global until cleared or initials are entered during verification.

The example represents the “O” edit prompts. The same edit templates used to edit organism/isolates under the RE manual are used here.

NOTE:	You can edit an existing organism/isolate, add an additional organism/ isolate, or an organism/isolate can be deleted entirely with this option. The example represents a manual addition of an organism/ isolate to the accession. You could just as easily edit an existing organism/isolate in the same manner. Notice how the “**” convention was used to change Ofloxocin’s display screen to “never display”.

**11.** Select ORGANISM: **&lt;RET&gt;**

**12.** TEST, LABPATIENT, ONE SSN: 000-00-0001     LOC: REF

MICRO 94 10129  URINE  URINE

1.  ESCHERICHIA COLI  (&gt;100,000  CFU/ML )

:             2.  STAPHYLOCOCUS AUREUS

:             :

SUSC	INTP	SUSC	INTP

AMIKACIN	32	I

AMPICILLIN	4	S	&gt;=16	R

AMP/SULBACTAM	16/8	I	8	S

AZTREONAM	16	I 	8	S

CEFAZOLIN	4	S

CEFOPERAZONE	32	I

CEFTAZIDIME	4	S

CEFTRIAXONE	8	S

CHLORAMPHENICOL			8	S

CLINDAMYCIN			8	S

ERYTHROMYCIN			1	S

GENTAMICIN	2	S	1	S

OFLOXACIN 			1*	S*

OXACILLIN			1	S

PENICILLIN			&gt;=16	R

PRESS RETURN FOR MORE **&lt;RET&gt;**

PIPERACILLIN	16	S

TETRACYCLINE			1	S

TRIMETH/SULFAM	2/38	S	2/38	S

VANCOMYCIN			1	S

**13.** (‘E’DIT data, ‘C’omments, ‘O’rganism, ‘W’orklist) // **C**

COMMENT ON SPECIMEN: ~MIDSTREAM URINE // **&lt;RET&gt;**

Select PRELIMINARY BACT COMMENT: **&lt;RET&gt;**

SELECT BACT RPT REMARK: **TC** (         *  TESTING COMPLETED  *)

SELECT BACT RPT REMARK: **&lt;RET&gt;**

After the editing session is completed (11), the next display (12) merely re-displays the data on accession, reflecting any changes which have been made to the data. You are allowed to edit further, if necessary, as shown in the remainder of the example.

The next part of the example (13) shows the prompts after selection of “C”. You may edit only the three fields shown. These are the same comment fields you would see under manual RE option.

You cannot edit comments for an organism. Use the “O” selection for that purpose.

TEST, LABPATIENT, ONE SSN: 000-00-0001     LOC: REF

MICRO 94 10129  URINE  URINE

1.  ESCHERICHIA COLI  (&gt;100,000  CFU/ML )

:             2.  STAPHYLOCOCUS AUREUS

:             :

SUSC	INTP	SUSC	INTP

AMIKACIN	32	I

AMPICILLIN	4	S	&gt;=16	R

AMP/SULBACTAM	16/8	I	8	S

AZTREONAM	16	I 	8	S

CEFAZOLIN	4	S

CEFOPERAZONE	32	I

CEFTAZIDIME	4	S

CEFTRIAXONE	8	S

CHLORAMPHENICOL			8	S

CLINDAMYCIN			8	S

ERYTHROMYCIN			1	S

GENTAMICIN	2	S	1	S

OFLOXACIN 			1*	S*

OXACILLIN			1	S

PENICILLIN			&gt;=16	R

PRESS RETURN FOR MORE **&lt;RET&gt;**

PIPERACILLIN	16	S

TETRACYCLINE			1	S

TRIMETH/SULFAM	2/38	S	2/38	S

VANCOMYCIN			1	S

**14.** (‘E’DIT data, ‘C’omments, ‘O’rganism, ‘W’orklist) // **E** Edit

(1)  CULTURE &amp; SUSCEPTIBILITY

TEST #(s) (or “ALL”): **&lt;RET&gt;**

Editing CULTURE &amp; SUSCEPTIBILITY

COLLECTION SAMPLE: URINE// **&lt;RET&gt;**

SITE/SPECIMEN: URINE// **&lt;RET&gt;**

COMMENT ON SPECIMEN: ~MIDSTRAM URINE // **&lt;RET&gt;**

BACT RPT STATUS: FINAL REPORT// **&lt;RET&gt;**

Select PRELIMINARY BACT COMMENT: **&lt;RET&gt;**

URINE SCREEN: **&lt;RET&gt;**

1  ESCHERICHIA COLI

2  STAPHYLOCOCUS AUREUS

Select ORGANISM: **1** ESCHERICHIA COLI

ORGANISM: ESCHERICHIA COLI// **&lt;RET&gt;**

QUANTITY: &gt;100,000 CFU/ML // **&lt;RET&gt;**

Select COMMENT: **MIC** (MIC’s in mcg/ml)

Select COMMENT: **&lt;RET&gt;**

AMIKACIN: 32// **^**

Any other antibiotics? NO// **&lt;RET&gt;** (NO)

1  ESCHERICHIA COLI

2  STAPHYLOCOCUS AUREUS

Select ORGANISM:

Select BACT RPT REMARK:         *  TESTING COMPLETE  *  //

BACT RPT DATE APPROVED: **&lt;RET&gt;**

This part of the example (#14) shows prompts you would see if you selected **“E”** . These prompts are the same prompts seen in the standard RE in manual verification.

**15.** (‘E’DIT data, ‘C’omments, ‘O’rganism, ‘W’orklist) // &lt;RET&gt;

Approve for release by entering your initials: kb

**16.** BACT RPT DATE APPROVED: **T** (JUL 18, 1994)

CULTURE &amp; SUSCEPTIBILITY completed: **N** (Jul 18. 1994@10:37)

**17.** (D)isplay (A)dd Work Load D

CULTURE &amp; SUSCEPTIBILITY

WKLD CODE: InHouse or Send Out Test~CULTURE/IN HOUSE

TEST MULTIPLY FACTOR: 1               WKLD CODE COUNTED: YES

WKLD CODE TALLY: 1                    COMPLETION TIME: JUL  18, 1994@9:52:40

USER: LABUSER, TWO                    INSTITUTION: REGION 7

MAJOR SECTION: MICROBIOLOGY           LAB SUBSECTION: MICROBIOLOGY

WKLD CODE: InHouse or Send Out Test~IDENTIFICATION/IN HOUSE

TEST MULTIPLY FACTOR: 1               WKLD CODE COUNTED: NO

WKLD CODE TALLY: 1                    COMPLETION TIME: JUL  18, 1994@10:31:26

USER: LABUSER, THREE                  INSTITUTION: REGION 7

MAJOR SECTION: MICROBIOLOGY

WKLD CODE: InHouse or Send Out Test~SUSCEPTIBILITY/IN HOUSE

TEST MULTIPLY FACTOR: 1               WKLD CODE COUNTED: NO

WKLD CODE TALLY: 1                    COMPLETION TIME: JUL  6, 1994@14:52:38

USER: LABUSER, THREE                  INSTITUTION: REGION 7

MAJOR SECTION: MICROBIOLOGY

WKLD CODE: SP Specimen~URINE

TEST MULTIPLY FACTOR: 1               WKLD CODE COUNTED: YES

WKLD CODE TALLY: 1                    COMPLETION TIME: JUL  18, 1994@09:52:40

USER: LABUSER, TWO                    INSTITUTION: REGION 7

MAJOR SECTION: MICROBIOLOGY           LAB SUBSECTION: MICROBIOLOGY

WKLD CODE: Etiology~BACTERIAL IDENTIFICATION, RAPID/PRESUMPTIVE

TEST MULTIPLY FACTOR: 1               WKLD CODE COUNTED: YES

WKLD CODE TALLY: 1                    COMPLETION TIME: JUL  18, 1994@10:31:26

USER: LABUSER, THREE                  INSTITUTION: REGION 7

MAJOR SECTION: MICROBIOLOGY

WKLD CODE: Etiology~BACTERIAL SUSCEPTIBILITY, AUTOMATED, MICROSCAN

TEST MULTIPLY FACTOR: 1               WKLD CODE COUNTED: YES

WKLD CODE TALLY: 1                    COMPLETION TIME: JUL  18, 1994@10:31:26

USER: LABUSER, THREE                  INSTITUTION: REGION 7

MAJOR SECTION: MICROBIOLOGY

WKLD CODE: ETIOLOGY~BACTERIAL ID/SUSC COMBO, AUTOMATED, MICROSCAN

TEST MULTIPLY FACTOR: 1               WKLD CODE COUNTED: YES

WKLD CODE TALLY: 1                    COMPLETION TIME: JUL  18, 1994@10:37:34

USER: LABUSER, THREE                  INSTITUTION: REGION 7

MAJOR SECTION: MICROBIOLOGY

WKLD CODE: +Micro Bacteriology Culture~MANUAL MICRO

TEST MULTIPLY FACTOR: 1               WKLD CODE COUNTED: YES

WKLD CODE TALLY: 1                    COMPLETION TIME: JUL  18, 1994@09:52:40

USER: LABUSER, TWO                    INSTITUTION: REGION 7

MAJOR SECTION: MICROBIOLOGY           LAB SUBSECTION: MICROBIOLOGY

(D)isplay (A)dd Work Load **&lt;RET&gt;**

Finally, at the “Approve for release by entering your initials:” prompt (#15), we have completed the editing of the accession test values, and enter the proper user initials. This will cause the removal of data from the ^LAH( global. Now the accession can only be edited via the routine manual method. The screen displays the final prompts for completion of the verification process (#16) and to display and/or editing of workload (#17). The report is placed in the print queue, if required, and the “AVS” cross reference is built.

**Data already in file:**

The next example is a case of dealing with data already in the patient’s ^LR( file and duplicate organism/isolate identification also coming from the auto instrument. This situation could occur in at least three ways:

1.	If data have been previously entered manually to the patient’s laboratory file and the organism/isolate was also placed on the auto instrument list (e.g., instrument downtime or a preliminary report based on off-line testing).

2.	You failed to enter your initials on the first pass verification, using the auto-verification option.

3.	If you verify data before the entire batch of accessions in the auto instrument has gone to completion.

Example 2:

Select ACCESSION AREA: **MICRO** BIOLOGY

ACCESSION DATE: 94// **&lt;RET&gt;** (1994)

Select Auto Instrument **MICROS** CAN(F257)

**1.** Enter number Part of Accession 10049 // **10130**

ACC # (10130)  JUL 18,1994@09:53:22

TEST, LABPATIENT, ONE    SSN: 000-00-0001     LOC: REF

Specimen: SPUTUM        Sample: SPUTUM

GRAM STAIN   &gt;25 PMN’S PERLOW POWER FIELD

&lt;10 EPITHELIAL CELLS PER LOW POWER FIELD

MANY GRAM NEGATIVE BACILLI

Comment on Specimen : **&lt;RET&gt;**

Is this the correct patient/specimen ? YES// **&lt;RET&gt;** (YES)

TEST, LABPATIENT, ONE   000-00-0001

MICRO 94 01030

SPUTUM SPUTUM

1 CULTURE &amp; SUSCEPTIBILITY

**2.** TEST #(s) (or "ALL"): **&lt;RET&gt;**

**3.** ENTER QUANTITY FOR (ESCHERICHIA COLI): **HG** (HEAVY GROWTH)

HEAVY GROWTH  ? YES// **&lt;RET&gt;** (YES)

ENTER QUANTITY FOR (PSEUDOMONAS AERUGINOSA): **MG** (MODERATE GROWTH)

MODERATE GROWTH  ? YES// **&lt;RET&gt;** (YES)

Beginning with the first prompt (1), the example shows the standard demographic display of the accession number. You indicate that this is the correct patient.

At the “TEST #(s) (or “ALL”):” prompt (2), the test to verify is selected.

The next four prompts (3) allow input of quantities for each organism/isolate in the ^LAH( global for this accession.

Please, notice that occasionally there may appear to be a missing isolate. Either this isolate has been completely deleted, or this isolate has no test data or quantity entered for this isolate. Do not become alarmed.

Isolate (1)

ESCHERICHIA COLI

GENTAMICIN	2	S	A

CEFAZOLIN	4	S	A

AMPICILLIN	4	S	A

TRIMETH/SULFAMETH	2/38	S	A

AMIKACIN	32	I	A

PIPERACILLIN	16	S	A

CEFOPERAZONE	32	I	A

CEFTAZIDIME	4	S	A

IMIPENEM	8	I	N

AZTREONAM	16	I	A

CEFTRIAXONE	8	S	A

AMP/SULBACTAM	16/8	I	A

RETURN TO CONT. (‘^’ TO SKIP) **&lt;RET&gt;**

TEST,LABPATIENT, ONE SSN: 000-00-0001

MICRO 94 01030  SPUTUM SPUTUM

**4.** There are NO antibiotics in the patients file

( No ) will add another organism

( Yes ) will overlay existing data

You already have 1 ESCHERICHIA COLI in the patient's file,

**5.** Do you want to add data one of THEM ? ? NO// **&lt;RET&gt;** (NO)

The next screen display (4) is shown because the option has determined that there is already an organism/isolate in the patient’s laboratory file which matches the organism/isolate it is about to store. The display (4) provides you with a view of all of the data stored in the patient’s laboratory file (there is none in this example).

If you answer “NO” or take the default at the “Do you want to add data to that one ? ? NO//” prompt (5), a completely new isolate is added to the patient’s laboratory file and the antibiotic will be transferred to that isolate. If you accept the default by accident, no values of the original isolate will be altered. If this was done in error, the extra isolate can be deleted later. (Use ^ to delete data.)

The option then displays the antibiotic for this particular isolate ( Escherichia coli ). The “RETURN TO CONT. (‘^’ TO SKIP)” prompt allows you not to transfer any of the antibiotic for this organism/isolate into the patient’s Laboratory file ^LR(. In this case, the extra isolate is created in the patient’s laboratory file. We entered a return and the next display shows that indeed the second organism/isolate has been added to the patient’s Laboratory file. It is isolate #3, (6).

Isolate (2)

PSEUDOMONAS AERUGINOSA

GENTAMICIN	2	S	A

TOBRAMYCIN	2	S	A

AMIKACIN	32	I	A

PIPERACILLIN	16	S	A

CEFOPERAZONE	32	I	A

CEFTAZIDIME	4	S	A

AZTREONAM	16	I	A

RETURN TO CONT. (‘^’ TO SKIP) **&lt;RET&gt;**

TEST, LABPATIENT, ONE SSN: 000-00-0001

MICRO 94 01030  SPUTUM SPUTUM

**6.** Isolate (3)

ESCHERICHIA COLI (HEAVY GROWTH)

AMIKACIN	32	I

AMPICILLIN	4	S

AMP/SULBACTAM	16/8	I

AZTREONAM	16	I

CEFAZOLIN	4	S

CEFOPERAZONE	32	I

CEFTAZIDIME	4	S

CEFTRIAXONE	8	S

GENTAMICIN	2	S

PIPERACILLIN	16	S

TRIMETH/SULFAM	2/38	S

( No ) will add another organism

( Yes ) will overlay existing data

You already have 1 PSEUDOMONAS AERUGINOSA in the patient's file,

**7.** Do you want to add data to one of Them ? ? NO// **Y** (YES)

COMMENT ON SPECIMEN: **&lt;RET&gt;**

BACT RPT STATUS: PRELIMINARY REPORT // **F** FINAL REPORT

Select GRAM STAIN: MANY GRAM NEGATIVE BACILLI // **&lt;RET&gt;**

SELECT BACT RPT REMARK: **NNRF** (NO  RESPIRATORY FLORA ISOLATED)

Select BACT RPT REMARK:

In the above display, a second duplicate that has been detected ( Pseudomonas aeruginosa ), and the data already in the patient’s laboratory file is shown. However, this time we wish to add to the data already in the patient’s laboratory file, as well as add any data not already there (7). This procedure will cause the patient’s laboratory file data to be overwritten with the data found in the ^LAH global. If there is more than one duplicate organism/isolate in the patient’s laboratory file, you will have to select which specific isolate number to be overwritten with the new data.

After the “Do you want to add data to one of them ? ? NO//” prompt, the display is as before, a display of what antibiotics are in ^LAH ( global for this organism/isolate.

TEST, LABPATIENT, ONE SSN: 000-00-0001

MICRO 94 01030  SPUTUM SPUTUM

2. PSEUDOMONAS AERUGINOSA (MODERATE GROWTH)

:		3.  ESCHERICHIA COLI (HEAVY GROWTH)

AMIKACIN	32	I	32	I

AMPICILLIN			4	S

AMP/SULBACTAM			16/8	I

AZTREONAM	16	I	16	I

CEFAZOLIN			4	S

CEFOPERAZONE	32	I	32	I

CEFTAZIDIME	4	S	4	S

CEFTRIAXONE			8	S

GENTAMICIN	2	S	2	S

PIPERACILLIN	16	S	16	S

TOBRAMYCIN	2	S

TRIMETH/SULFAM			2/38	S

('E'dit data, 'C'omments, 'O'rganism, ‘W’ORKLIST ) // **O**

**8.** 1.  ESCHERICHIA COLI

2.  PSEUDOMONAS AERUGINOSA

3.  ESCHERICHIA COLI

Select ORGANISM:

This display shows the #1 E. coli isolate (8) which was entered manually as a preliminary result but was not overwritten by the uploaded data, which became isolate #3. No susceptibility data exists for isolate #1, so it is not listed at the top.

TEST, LABPATIENT, ONE SSN: 000-00-0001

MICRO 94 01030  SPUTUM SPUTUM

2. PSEUDOMONAS AERUGINOSA (MODERATE GROWTH)

:		3.  ESCHERICHIA COLI (HEAVY GROWTH)

AMIKACIN	32	I	32	I

AMPICILLIN			4	S

AMP/SULBACTAM			16/8	I

AZTREONAM	16	I	16	I

CEFAZOLIN			4	S

CEFOPERAZONE	32	I	32	I

CEFTAZIDIME	4	S	4	S

CEFTRIAXONE			8	S

GENTAMICIN	2	S	2	S

PIPERACILLIN	16	S	16	S

TOBRAMYCIN	2	S

TRIMETH/SULFAM			2/38	S

('E'dit data, 'C'omments, 'O'rganism, ‘W’ORKLIST ) // **&lt;RET&gt;**

Approve for release by entering your initials: **kb**

BACT RPT DAE APPROVED: JUL 18, 1994// **T** (JUL 18, 1994)

CULTURE &amp; SUSCEPTIBILITY completed: **N** (JUL 18, 1994@10:46)

(D)isplay (A)dd Work Load: **&lt;RET&gt;**

The above example represents typical user input when completing the verification process.

As in every case, the final verification process includes a composite display. The example is the final full composite display of all of the patient’s test data for this accession. This is the final display before the actual verification takes place.

NOTE:	Remember, if the user initials are not entered, the accession data is not purged or cleared from the ^LAH( global. This means that this accession number can be verified again, and a similar scenario will result.

##### Work Documents

Load/work list generation is the same for Microbiology as for the rest of the laboratory. For non-automated (interfaced) applications, you may choose to modify the Suppress Sequence field (#.09) of the LOAD WORK LIST file (#68.2) to suppress printing of the sequence number, which substitutes the accession number on the printout and is easier to read. The exported version will provide you with several pre-made worklists, including Bacteriology, which includes such profiles as Blood Cultures, Routine Bacteriology, Mycology, and others. These profiles can be changed to reflect those tests performed at your site.

You may not care for the load/work list format and may want to try other worklist formats. There is no perfect document at this time, but there are workable substitutes. The Short and Long Form Accession Lists, [LRACC2] and [LRMIACC1] respectively, can be used to print a log sheet of specimens received daily and as a manual back-up system to record results. The Long Form has the advantage of allowing selection of one particular test to be listed (however, if the accession number has multiple tests, all the tests would list, not just the one you selected). You can also choose to print only incomplete entries, which thereby serve as “Incomplete Test Status Report.” The disadvantage is apparent to a large-volume lab, since this uses up quite a bit of paper.

The Short Accession List can be useful to the lab with several accession areas. A list for a hypothetical “Blood Cultures” accession area, if printed double-spaced, provides plenty of room to write Bactec Growth Index numbers, results, etc. Some tests, such as Antibiotic levels, which can be accessioned as a batch before their daily (etc.) run, thereby resulting in consecutive accession numbers, can be called up on the list by number rather than by date, resulting in a convenient list without undesired tests listed.

Accession List by date [LRUPAD], or by number [LRUPA] can be used to provide lists sorted by accession number, patient, or collection sample (you cannot, however, select a particular test name from an accession area). The format is very condensed, but it can be useful for QA applications.

##### Results Lookup

There are several options available for the techs to look up results in the case of a telephone inquiry.

1. The first is the Interim Report for Selected Tests as Ordered [LRRSP] option which you should be familiar with from the general Lab package. [LRRSP] option is only one of the Interim options that will display Micro results, but it is probably the best option used to find results quickly. With adequate training and familiarity with the acceptable names (and synonyms) of the tests, the physician can request precisely the test results he/she wants to see. The option requires no knowledge of accession areas and therefore is easy for the ward user to use.

The Patient Report [LRMIPSZ] option can also be used to find this information. You can call up reports either by accession number or by patient name (the more useful method for phone inquiries). This option requires knowledge of the accession area only if you are looking up results by accession number. If looking up by patient, you will receive a list (in reverse chronological order) of all available accessions for the patient. You will see the collection sample, number, and date only. You will not see the tests requested. To obtain this information, you may find it helpful to first check the Show List of Accessions for a Patient [LRUPT] before the Patient Report. The “Show List...” requires the Accession area, but then will tell you the date and time of collection, accession number, collection sample, and tests requested. You can then call up the Patient Report by accession number.

All Results for Selected Accessions  prints all available results for specified accession numbers. The format is the same as the Patient Report.

A very handy option to use when a request is received for results of multiple tests which may belong to several accession areas is General Report for Selected Tests [LRGEN] option. If you enter, Microbiology Test List (an entry in LABORATORY TEST file (#60)), at the “Select LABORATORY TEST:” prompt and specify the appropriate time frame, the package will search for and report results of MI-subscripted tests only in a format similar to the patient report. You can also specify a particular test and collection sample if needed.

Cumulative patient report is also very similar to the General Report. It is designed specifically to provide results of MI-subscripted test (without entry of Microbiology Test List). Both options list results in reverse chronological order and the “PRESS ‘^’ TO STOP” prompt allows you to stop when you find the results you need.

The Health Summary has become a very popular tool of the physician and other healthcare providers. It provides a customized condensed summary of reported results. It must be brought to the user’s attention that some important results are omitted from this report and an alternate option may be required. Mycobacterial susceptibilities are one type of result omitted from the Health Summary.

##### Special Output

Several reports have been designed to provide specialized information for the users of the Micro package. At this time, only bacteria (those entries in ETIOLOGY FIELD file #61.2 with an identifier of B (= bacteria)) appear on the Survey and Trend reports.

The Infection Control Survey Report [LRMISEZ] is used by the Laboratory and the Infection Control Unit to look for increases in the number of a particular organism isolated or the emergence and spread of a resistant organism. The report gives a listing of wards and all organisms isolated from that ward location. The report contains patient information, specimen, and antimicrobial susceptibilities of the isolates. The report also gives a survey by organism and where the organism was isolated. In addition to generating this report for all organisms, the user can choose to specify only one organism. This report can sort by ward/location, organism, provider, and patient. These reports can be generated over any time interval. You can select the number of days between a patient’s admission and collection of a sample (to help track iatrogenic infections) or specific susceptibility patterns. The field Micro Survey Report Defaults in the LABORATORY SITE file (#69.9) can be used to preselect a set of default parameters to be used to quickly request a printout. Because of the large amount of data manipulation required, it is usually queued to print at off-hours.

The Microbiology Trend Report  [LRMITS] option is enhanced to sort the ‘Antimicrobial Trend Report’ by DIVISION. This report is used to compare counts of organisms and patterns of antibiotic susceptibility. Different types of ‘Antimicrobial Trend Report’ by division can be generated. The Microbiology Trend Report [LRMITS] option is located on the Laboratory DHCP Menu [LRMENU] (locked with LRLAB security key), Microbiology menu [LRMI] (locked with LRMICRO security key), Microbiology print menu [LRMIP] option.

The ‘Antimicrobial Trend Report’ can be generated by DIVISION using the Microbiology Trend Report [LRMITS] option by the following categories:

- Organism
- Specimen
- Collection sample
- Patient
- Physician
- Location

The ‘Antimicrobial Trend Report’  can be generated by DIVISION using the Microbiology Trend Report [LRMITS] option by specified criteria:

- Types of organisms
- Isolates collected after a specified time from admission
- Merge criteria
- Antibiotic patterns
- Detailed reports

The ‘Antimicrobial Trend Report’ can be printed by the following DIVISIONS:

- (A)ll Divisions
- (S)elected Divisions
- (N)o Division Report? No

**NOTE:** Defaults for the ‘Antimicrobial Trend Report’ types can be defined in the LABORATORY SITE file (#69.9). Reports can be restricted to specific types of values (i.e., specific patients, specific specimens, etc.). The reports can be restricted to criteria that affect all types of reports.

The user selects the comprehensive criteria and types of ‘Antimicrobial Trend Reports.’ The time range is forced to months. The report is forced to be queued, preferably to be run during off-hours. The Antimicrobial Trend Reports extracts data from LAB DATA file (#63) and temporarily stores the data in a ^TMP global. The format of the ^TMP global is indexed similar to the outputs of the requested reports. Once the data has been collected, it is reprocessed; counted, and merged using the specified criteria selected. Data merges can be done so that isolates from the same patient and same organism and non-conflicting antibiotic patterns will only be counted once depending on being isolated from the same specimen, collection sample or any sample. A detailed ‘Antimicrobial Trend Report’ showing each isolate values can be used to confirm the counts reported. The data is reported by simply displaying the values of the ^TMP global.

A Health Department Report [LR HEALTH DEPT] option is available which lists all isolates that have been identified as reportable in Health Dept Report field (#10) of the ETIOLOGY FIELD file (#61.2). The report shows patient demographic information, including race, marital status, and occupation, in addition to the address and phone number. Actual culture results (other than the organism name) are not included, since this information can be retrieved by lookup of the accession number printed.

Although not a report option, the Infection Warning Edit [LR INF WARN] option (Supervisor’s Menu) may be useful to the Micro lab. This 1-10 character message appears on the accession labels, collection lists, and the “Show List,” but does not appear when accessioning or on any of the results report printouts. It could be used to indicate a specimen from a patient in isolation or for other purposes, as deemed necessary by your lab and/or Infection Control Unit.

##### MIME Edit Inactive DT Multiple - ETIOLOGY File

A new field INACTIVE DATE (#64.9102) has been added to the ETIOLOGY FIELD File (#61.2). This option allows those users with the LRSUPER key to ‘walk’ the ETIOLOGY FIELD File (#61.2) and enter an Inactive Date for those entries that should be Inactive. The user will have the ability to select an Identifier Name or ALL for Identifier Names. The option will start with the oldest entry (beginning) associated to the Identifier Name selected and allow the user to enter an Inactive Date for the entry displayed if that entry is inactive.

The user will be able to:

Input a date if the entry is inactive.

press &lt;Enter&gt; if the entry is active and go to the next entry.

Enter ‘^’ to exit the option. If the Identifier Name selected had previously been worked with the user will have the option to start with the next entry that follows where the last effort left off or to start over from the beginning for that Identifier Name.

This option only allows the entry of an Inactive Date. This option does not allow for the editing of previously entered Inactive Dates.

This option only displays entries that do not have an Inactive Date.

Example:

Select Microbiology menu  Option: **MIME** Edit Inactive DT Multiple - ETIOLOGY File

BACTERIUM           (B)

FUNGUS              (F)

PARASITE            (P)

MYCOBACTERIUM       (M)

VIRUS               (V)

CHEMICAL            (C)

DRUG                (D)

RICKETTSIAE         (R)

PHYSICAL AGENT      (A)

NULL                (N)

ALL                 (X)

Enter the Identifier Name or Code : **F** FUNGUS

Organism: FONSECAEA, NOS (7159228)

INACTIVE DATE: &lt;Enter&gt;

Organism: PHOMA SP (7159227)

INACTIVE DATE: **T** (OCT 10, 2017)

Organism: AEROBIC ACTINOMYCETE, NOS (7159226)

INACTIVE DATE: **^**

An '^' was detected. Quitting

#### MISE Edit Inactive DT Single - ETIOLOGY File

A new field INACTIVE DATE (#64.9102) has been added to the ETIOLOGY FIELD File (#61.2). This option allows those users with the LRSUPER key to Add, Edit, or delete the INACTIVE DATE for entries in the ETIOLOGY FIELD File (#61.2).

The user will enter a Etiology Field Name and be able to do the following:

Input a date if the entry is inactive.

Press &lt;Enter&gt; if the entry is active and go select a different entry.

Change the date for an entry

Enter ‘@’ to delete the Inactive Date for the entry if the entry is active.

Example:

Select Microbiology menu Option: MISE  Edit Inactive DT Single - ETIOLOGY File

This option allows the editing of the INACTIVE DATE field

in the ETIOLOGY FIELD File (#61.2).

Select ETIOLOGY FIELD NAME: SABADILLA

Organism: SABADILLA

Snomed Code: 6905        Gram Stain:

Identifier: CHEMICAL        Inactive Date:

INACTIVE DATE: T  (OCT 10, 2017)

Select ETIOLOGY FIELD NAME: ENCAINIDE

Organism: ENCAINIDE

Snomed Code: 7677        Gram Stain:

Identifier: DRUG            Inactive Date: OCT 10, 2017

NACTIVE DATE: OCT 10,2017// T  (OCT 10, 2017)

Select ETIOLOGY FIELD NAME: **ABSIDIA**

Organism: ABSIDIA

Snomed Code: 4011        Gram Stain:

Identifier: FUNGUS          Inactive Date: SEP 30, 2017

INACTIVE DATE: SEP 30,2017// **@**

SURE YOU WANT TO DELETE? **Y** (Yes)

Select ETIOLOGY FIELD NAME:


### Instrumentation/Interfacing

Since interfacing instruments is such an important part of the modern laboratory, all users should be familiar with the process of interfacing and why it is not just a plug the machine in process as many instrument sales representatives claim. By understanding the principles of interfacing and how instruments interact with the  system, you can help the LIM set up the files in the most efficient way possible for your use.

If you are involved with an interfaced instrument, you probably should become familiar with the files and “lingo” involved in interfacing an instrument. This section will use terms such as global (In the MUMPS language, a global is a tree-structured data file stored in the common database on the disk) and handshake (A method for controlling the flow of serial communication between two devices, so that one device transmits only when the other device is ready). For those of you who are LIMs, further details are to be found in the Technical Manual.

#### Load/Work List

The LOAD/WORK LIST file (#68.2) controls the building and printing of load/work lists. Each automated instrument has to be linked to a load/work list entry. For each load/work list entry, there is at least one profile that lists the tests and controls that are used with that profile on that load/work list. In normal operation, there is one load/work list and at least one profile per type of instrument and one for each bench. An example of multiple profiles for a load/work list might be a particular kind of test that is run on a weekly basis, (e.g., a Thursday profile). At other times during the week, it is run with another profile. The definition of the profile determines what tests are going to be pulled out of the accessions to be included on that load/work list. Your LIM will predefine all the various ways that you will reference that test. You may use synonyms - define it as parts of profiles, or subparts of other panels, or profiles in the LABORATORY TEST file (#60).

Your LIM needs to specify individually under the Profile field (#50) on the load list profile those tests that need to be verified. The Build Name Only field (#2) in the LOAD/WORK LIST file (#68.2) is a “YES/NO” question. If you answer “YES,” the test (either single or a panel) will be used only to build the profile for the load/work list. If set to “NO,” (and the test is a single test), then the sequence of tests on the profile will be defined by the order in which they are added to this field. If set to “NO,” and the test is a panel, the test sequence will be defined by the order in which they have been added to the panel test name in the LABORATORY TEST file (#60), Lab Tests Included in Panel field (#200). For example, enter a load/work list for “Electrolytes,” and define one profile for the list, also called “Electrolytes.” Onto this profile you will be pulling the **single** tests “Na, K, Cl, and CO2” **in that order** in File #60. This is an important point to remember so that the tests line up in the correct order during verification.

#### Unidirectional Communications

The general unidirectional flow of data from the instrument to the computer to verification is described here. The first staging of the data is in the Large Scale Integrated (LSI) Device INTERFACE. The data is stored with a flag as to what hardware port the data came from. The data is sent from the LSI INTERFACE to the host system one at a time with handshaking to the LAB routine and then goes into the ^LA global with the first subscript representing the individual instrument line from the AUTO INSTRUMENT file (#62.4). (If you are curious as to what this looks like, ask your LIM or IRM department to capture a data stream to look at.) This data is then processed by a special routine for that instrument and the processed data is stored in the ^LAH global until it is verified by a lab tech or deleted. When no data has accumulated for approximately 1 minute, the ^LA global for the routine is deleted and completely removed.

The LAB routine runs continuously and looks for data from the LSI INTERFACE. As soon as the LAB routine receives data from the instrument, it starts putting the data into the ^LA global, subscripted by instrument number, and simultaneously executes the NEW DATA node for this instrument in the AUTO INSTRUMENT file (#62.4) to start up the routine responsible for processing the data out of the ^LA global. The data that is contained in the ^LA global is the raw instrument data. If additional data is coming in from the same instrument and the ^LA global already exists, the LAB routine doesn’t restart a new routine. The new data continues to be accumulated in the ^LA global. This means that if data already exists in the ^LA global and the routine is not running for that instrument, data will continue to accumulate in the ^LA global, but will not be processed out. This situation will exist until the Restart Processing of Instrument Data [LA JOB] option is run to start the proper routine.

The running of the appropriate routine processes the data out of the ^LA global and stores the data in the ^LAH global. This is a temporary storage area. The AUTO INSTRUMENT file (#62.4) contains information on the tests that are run, where in the input string, the test value is located, and where to store the data in the ^LAH global. The first subscript of the ^LAH global is tied uniquely to a given load/work list. If data is **not** overlaid, each new sample’s data will get a new entry in ^LAH. If the data is to be overlaid, then a new entry will be made only if the linking variable cannot be found in the file.

The processing of the data out of the ^LAH global is usually done during verification of instrument data. If not, it accumulates data for a day or until the Clear Instrument/Worklist Data [LRINSTCLR] option function is done. When the instrument data is cleared, data in ^LA, ^LAH globals are purged. Upon verification, the data from the ^LAH global is moved into the ^LR global. This global is defined by the LABORATORY DATA  file (#63). All data that remains unverified stays in the ^LAH global.

To avoid confusion with data from the previous shift, the Clear Instrument/Worklist Data [LRINSTCLR] option should be run at the beginning of every day (or perhaps, every shift). For example, if there is an accession number 120 verified, then that data still exists under that accession number. If you then run a new accession number 120, you would get the data from the previous accession number 120. If you ran another sample through the system for accession 120 for the current time period, you would then have two sets of data for the accession number 120. (If you have ROLLOVER (specified in ACCESSION file (#68) and the data is unverified, you would not be able to create a new accession 120. This is complicated by the fact that the AUTO INSTRUMENT file (#62.4) allows two ways of running the programs, one of which is that every sample gets a unique entry in the ^LAH global, even if it belongs to the same tray and cup and to the same person. This means you can consecutively accumulate multiple copies of data. The technologist then must make a decision about which set of data or combination of sets is correct. This cannot be batch verified. To avoid this situation, you clear the instrument using the Clear Instrument/Worklist Data option.

Verification (and movement of data from ^LAH to ^LR) can be accomplished two ways:

1.	Use the Enter/Verify Data (auto instrument) [LRVR] option. This takes one accession number, one sequence number, or one tray/cup at a time, displays the data and asks for verification. When it is verified, it moves to ^LR and is then available to the wards, on cumulative reports, etc.

2.	Use the Group Unverified Review (EA,EL,EW) [LRGP] option. This prints the data from the ^LAH global. You may check it for critical values, delta checks, etc. When you are ready to verify all or parts of the data, use the Group Verify (EA,EL,EW) [LRGV] option to verify it and move it to the ^LR global. You cannot group-verify data that has multiple entries of data that are not overlaid. If there are cases of multiple sets of data, the group verify skips the data and notifies you. The technologist must make the decision as to which data to use. To do this, use the Enter/Verify (auto instrument) option to make a manual selection.

If the Overlay Data field, in the AUTO INSTRUMENT file (#62.4), is set to “YES,” then a test is overlaid by a new run of the same test. For example, if you get an out-of-range check, you can rerun the sample and the values will replace the previous values. This is done for all values that are transmitted from the instrument. To correctly use this method, you must remember that new data substitutes for old data (that is, new data writes over existing data).

#### Supervisors/Selector of Instrumentation

* **WARNING:** If you are involved with selecting an instrument to use in your Laboratory, be aware that there are three possible scenarios facing you when you decide to interface:

1.	There is a completed, approved interface routine written for that particular instrument. It may be unidirectional or it may be bi-directional, but either way, it has been tested and works at other  sites.

2.	There is an interface routine written for that particular instrument but it has not been completely tested. It may still be in Alpha test (first try) or Beta test (later tries). In this case, you have the option of waiting until other sites finish the testing or becoming an Alpha/Beta site. If you choose to become a test site, you will have to commit your time and IRM time to checking the data for problems and working with the developer to correct those problems.

3.	There is not an interface routine written for that particular instrument. In this case, you can become an Alpha site yourself or you can wait until another site purchases the instrument, goes through the process of having the routine created and approved. If you choose to become a test site, remember that you will have to commit your time and IRM time to checking the data for problems and working with the developer to correct those problems.

NOTE	A  routine must exist in order for you to effectively interface with your new instrument.

It does not matter that the Manufacturer’s Sales Representative says that it is interfacable. (To most Sales Representatives, interfacable means the instrument has a RS-232 plug in the back and it can be connected to an outside computer with a standard communication line.) Without the interface program to “translate,” your  system will not understand what the instrument “is saying” and where to store the data.

#### Bidirectional Communications

Bidirectional communications of Laboratory instruments can be done at your site if the following items have been accomplished:

1.	Version 2 LSI EPROM chips have been installed. These chips may be obtained from your regional ISC.

2.	Version 4.08 or greater of the VistA Laboratory software has been installed.

3.	VistA **bidirectional routines** have been written for the instrument to be interfaced. These routines will include the bidirectional communication routine(s) for downloading and uploading, routine(s) to move the data from ^LA to the ^LAH global, and may also include verification routine(s) in the case of microbiology instruments.

4.	The AUTOMATED INSTRUMENT file (#62.4), has been properly defined for the instrument to be interfaced.

5.	The load/work list has been properly defined in the LOAD/WORK LIST file (#68.2).

6. 	Ability of the instrument to function in the bidirectional mode. This ability should have documentation provided by the instrument manufacturer which should include complete information on the bidirectional communications protocol and procedure, instrument setup (there may be many ways to configure an instrument), and an example of the expected download and upload data stream.

NOTE	It is important to mention that there are no industry standards that define bidirectional communications. This means each manufacturer may have completely different approaches to the problem of downloading and uploading information from an instrument to and from a host CPU. Each instrument is a completely separate experience.

For this chapter we have defined the term “download” as patient demographic data, specimen and test information and other necessary data required to perform and report test results sent from the host CPU to the instrument. “Upload” is defined as data sent from the automated instrument to the host CPU a completed test result and other information necessary for the verification and reporting of test results in the  laboratory software. For example, the communication protocol KERMIT, used by Kodak in their Ektachem, is the choice of the manufacturer and may not be the choice of other instrument manufacturers.

##### Lab Software

When an automated instrument is interfaced, there are at least three computer systems interacting with each other, potentially using different hardware, operating systems and languages. The automated instrument may use one of many operating systems (DOS, UNIX, etc.,) and one of many languages (BASIC, C, FORTRAN, etc.,). The LSI is running a custom program written in Digital MACRO Assembler code (documentation and a hard copy of the original unidirectional code are found in Section V of the General Digital GDC 2100 Data Concentrator Maintenance and Operations Manual that came with each instrument). The bidirectional code was written at the Salt Lake ISC and San Francisco ISCs. The host CPU in the VA may be running VMS, MSM, DSM, or ISM for the operating system and a version of ANSI standard MUMPS as the language. The thread that holds all these variables together is the ability of each to understand and send information in ASCII over lines conforming to the RS-232-C standard.

The entire automated instrument communication system is driven by the LAB routine which must be started by TaskMan and run as a background task. This routine’s responsibility is to:

1.	Accept the concentrated data from the LSI.

2.	Check for the correctness of the transmission from the LSI.

3.	Break the data out for individual instruments.

4.	Store the data.

5.	See if the processing routine is running, by checking if ^LA(“instrument number” is defined. If not, start the specific routine for that automated instrument by executing the New Data field (#20), in the AUTOMATED INSTRUMENT file (#62.4).

6.	See if there is a need for handshaking, and if there is, call the routine.

7.	If no data is coming in, check to see if there is data to send out.

8.	If there is data to go out, get the data format for the LSI and send it.

9.	 to 1 until the interface is shut down.

When the specific automated instrument routine, which was started by the LAB program, has no more data to process, it deletes the data in ^LA for that instrument and gracefully stops running. The routine will be started again by the LAB program when new data is received for a specific automated instrument.

##### Handshake Routines (Bidirectional)

The handshake program(s) may be different for each bi-directional instrument a site attempts to interface. This variability is caused by the lack of clinical instrument bidirectional communication standards. When there are no standards, each manufacturer is able to “do their own thing” and therefore the communication protocols may be vastly different from manufacturer to manufacturer. An active ASTM subcommittee (E31.14) is working on developing bidirectional communication standards that will be acceptable to all parties involved. When the standards are finally adopted, our job will be a lot easier. However, the need for bidirectional communications in the VA laboratories is upon us now, and the Dallas ISC is developing new bidirectional and unidirectional interface routines for VA instruments. The handshake routine(s) called by the LAB routine is used to check the incoming records from an automated instrument.

##### The Processing Routine

This is usually a single routine for each automated instrument. The LAB program will find which routine to use from the Program field (#2) of the AUTOMATED INSTRUMENT file (#62.4) for each automated instrument that is interfaced.

##### Bidirectional Routines

There are several new routines needed to interface automated instruments in the bidirectional instruments. The routine ^LADOWN is used to determine which download processing routine to use in formatting the data from the previously built worklists and moving it to the “O” nodes of the LA global.

This option invokes an instrument-specific routine to process a load/work list for downloading to the instrument. The option will prompt you with a series of questions relating to the building of the down load records. Care must be taken to ensure that only the desired accessions are built on the work list.

##### Checklist For Instrument Interface

It is to the user’s advantage to have a familiarity with this checklist for troubleshooting purposes.

1.	Instrument must be transmitting data.

2.	Correct baud rate:

•	instrument baud rate = interface instrument port baud rate

•	host system baud rate = interface system port baud rate

3.	Echo device defined (for system).

4.	LAB program routine must be running.

5.	MUX program baud rate is correct.

6.	ZTM program routine must be running (Task Manager).

7.	AUTO INSTRUMENT file is defined correctly.

8.	Input lines are wired correctly.

NOTE	The size and resources of the site will determine whether this checklist can be performed by laboratory personnel or IRM/Biomed personnel.

#### Instrument Interface Trouble Shooting

Randy Frommater

– CIO Field Office

•	LSI management: To shut down the LAB program set the “STOP” node by entering the following:

S ^LA(“STOP”,n)= WHERE n represents the AUTO INSTRUMENT file (#62.4) entry # for the LSI). The LAB job will continue starting processing routines until no more data remains in ^LA global. At this time, LAB will check the “STOP” node and if it exists, it will kill off ^LA and shut itself down. This is the proper way to bring down the LAB job and not have partial data left in ^LA.

NOTE: 	This will not work if the LAB job is not actually running as happens sometimes when it shows up on system status but no processing routines get started.

•	Multiple LSI: The procedure is the same except the LSI need to be stopped and started in a certain order.

1. Stopping LAB: shut down in reverse order, LSI #3, then LSI #2, then LSI #1.

2. Starting LAB: start in numerical order, first LSI #1, then LSI #2, etc.

Crashes and just having IRM kill the LAB job can account for incomplete data streams in ^LA which in turn may cause the processing routine to error out when the LAB job is started again. If this happens, the best thing to do is have IRM kill the ^LA(n) node and either re-transmit your data or rerun it.

•	Troubleshooting (with and without programmer access): Techs report “EA” says no data to verify. Use lab interface menu and observe the system status display. Is there data in ^LA and ^LAH? If answer is “YES” to both, use Watch the Data in LA Global [LA WATCH] option to look at upload data. If ^LA(n,"I",0)= less than ^LA(n,"I"), this is the last line that was processed and you should look at ^LA(n,"I",value of ^LA(n,"I",0)) for any unusual characters. To view ^LAH global data you can do the following:

1.	Version 5.2: use the Watch Data in LA Global [LA WATCH] option. This option will give a choice of LA-raw data in LA GLOBAL or LAH-Verifiable data in LAH GLOBAL.

2.	Check to see if the results reported missing are in fact in LAH.

•	The normal identifier node in ^LAH looks like this:

For the most part, the above data stream will be what you look for as a healthy identifier node. The most common problem is a missing date entry. The probable cause of this is that the ID or Account number transmitted did not find a match in the ACCESSION file. If you were in “EA” and entered the tray and cup as 1 and 2, the results would be displayed to you. There is an occasion where all you might see is this:

**^LAH(n,1,1,0)=1^2^^^7^^STKS**

This is a healthy identifier node for an instrument set to verify by tray/cup. This is not all that common since verify by accession is the most common choice.

**•	Data in ^LA? YES, 	^LAH? NO:**

Again, check the "I") and "I",0) nodes in ^LA. If "I") has value and "I",0)=0 check the error log to find out what may have happened to the processing routine.(Lab Interface menu =&gt; Lab Error Trap Listing option , or the ^LA("ERR") node). Verify that the routine entered in the AI file is correct and if there was an entry in the error log, make sure the variable LANM equals this entry. Check to see that other instruments on the same LSI are still running. If not, the LAB program has shut down. If they are, suspect a problem in the ^LA data stream causing the processing routine to quit or crash.

If the latter is the case, it's time to call in IRM. Have them clear the variables from the partition leaving only the basic system variables. If ^LA("LOCK",n) is set, kill it. Set ^LA(n,"I",0)=0, ZLOAD the processing routine and start executing the code command by command writing variables as you go until you get to the point where the data stream fails the code and causes it to either ignore the data or quit.

**•	Data in ^LA? NO, ^LAH? NO:**

What you are seeing here could be one of two things, 1) the instrument has stopped transmitting (suspect either a wiring problem or instrument parameter has been reset to a default of no transmission), or 2) the processing routine completed it is task and killed off ^LA(n) and ^LA("LOCK",n). You can check number one by watching the ^LA global while a transmission is in progress. If you suspect number two, have IRM set ^LA(n,"I")=0, and ^LA(n,"I",0)=0. This will stop the processing routine from acting on the new data that you will now transmit and give IRM a chance to step through the code as in the procedure previously stated.

**•	Illegal Number or Maximum Errors:**

Most likely cause is having the letter “E” as part of the value of “V” when it is used for setting the value of a variable in plus form.

**Example:** =+V. Find out who or what is adding this “E” to the data. Accession numbers should not contain alpha characters although some instruments allow this type of entry.

**•	Variables used in auto instrument interface routines:**

TSK,T =	both are used to represent the port or instrument number.

LANM =	processing routine name.

ID =	accession number.

IDE =	instrument sequence number.

TRAY and CUP are self-explanatory.

TC( ) =	the array built when ^LASET is run.

These variables contain the information from the AI file for test name, data name location, and params 1-3.

Example:

TC(I,0)=1.....................First test in AI Chem Test field.

TC(I,1)=TV(384,1).....Data name location (storage)

TC(I,2)=......................Param 1 value

TC(I,3)=......................Param 2 value

TC(I,4)=WBC.............Param 3 value

TV( ) = the array built by indirection in the processing routine, used to set test 	values into ^LAH.

code example: S @TEST(TEST)=+V will set the following:

where TEST = WBC and TEST("WBC")= TV(384,1)          TV(384,1)=5.7

where TEST = RBC and TEST("RBC")= TV(385,1)           TV(385,1)=4.32 etc.

TEST( ) = array that holds test name identifiers built from param 3 or TC(I,4)

ex: TEST("WBC")=TV(384,1)

IN = the value of the data node being processed (^LA(n,"I",X))

Y (1) = the value of IN, this may be a single entry or an array. It is used for 	parsing out data.

V = used for passing a value to the subroutine NUM and then setting a variable 	upon returning.

LAGEN =- contains the executable code determined by the ENTRY for LAGEN 	routine entry in the AI file.

LWL = the internal entry number for the load/work list used by this instrument. It is set by taking the fourth piece of the auto instruments zero node from the AUTO INSTRUMENT file (#62.4).

ex: ^LAB(62.4,2,0)=Coulter STKS^^LACOLTSE^7^^LOG^ID^^^STKS			Without programmer access you can use FileMan Inquiry option and use			number instead of standard output when inquiring on the load/work list entry.

**Local Auto Instrument files:**

The most important trouble shooting tool you can have is to keep a file on each instrument interfaced. This file should contain the following information captured when the interface is up and working well:

1. Samples of the ^LA and ^LAH data streams.

2. Copy of the routine used.

3. Captured printout of the AUTO INSTRUMENT file (#62.4) and LOAD/WORK (#68.2).

4. Any pertinent data related to the wiring of the interface.

5. Instrument parameter settings.

###### Direct connect instruments:

Direct connecting of instruments should be reserved for those instances where going through the LSI just will not work. This happens sometimes when two or more major instruments are on the same LSI. The traffic during transmission slows the verification process down to unacceptable levels. If the instrument in question does not have a direct connect routine as part of the released package there are three alternatives available to you:

1. Place one instrument on its own LSI.

2. Get a local programmer to modify a copy of the LAPORTXX routine to work with this instrument.

3. Submit an official request to the Auto Instrument Application Requirements Group (ARG) for approval of development. Some sites have expressed the desire to bypass the LSI completely and direct connect all instruments. This causes much overhead on the system because every instrument would have to have a background job associated with it which increases the chances for problem by however many background jobs you have running. The LSI is old and simple, but it works.

### Reports and Outputs

#### Cumulative Report

Cumulative reports are an accumulation of patient results. With these reports, it is possible to see trends in laboratory results over a period of time. New data is displayed together with previous data so that the ultimate result is better patient care. Another feature is the ease with which results can be retrieved in a patient’s chart. Some sites may choose to print these reports daily; others may choose to print them Monday-Friday only.

The cumulative routines are very technical in nature and their discussion is beyond the scope of this manual. These routines are discussed in the Technical Manual. However, the laboratory reports themselves can be set up rather easily, with time and patience on the part of the laboratory application coordinator. The key word here is patience. The LIM may have to print some of the cumulative pages several times before you have your desired output.

NOTE	Similar reporting capabilities are available through FileMan. See the Historical Lab Results special report on page 31 for information on generating lab results for a specific patient, specimen type, and lab test, looking back over a specified number of days.

##### Cumulative Report Generation

Before printing ever occurs, there are several decisions that will need to be made at your site, including:

1.	What time of day should your report print?

2.	Who is responsible for monitoring the printing and distributing the reports?

3.	What printer or printers will you use? Where will they be located?

4.	What kind of paper will you use?

5.	Do you want to task your cumulative or start it by selecting an option from a menu?

If you are to be involved with the “printing of the CUME,” be sure that you know the answers to these questions because you will be asked by someone and usually it will be by an upset someone who did not receive the CUME report when they should have.

##### How the Cumulative is Formatted

###### What is a Major Header?

The major header name prints in full for the page title on your cumulative report. When you think of a cumulative, try to think of it as a book with chapters. Maybe chapters 1-10 are about Chemistry, chapters 11-15 for hematology, etc., or if your LIM took the system defaults, the numbers are kept in the order of their entry into the file.

Major headers are simply the chapters or sections of your book. When you look at the “page” on the top of the cumulative report sheet, what you will see is the “section number” and then the “page” within that section. The page that you see on the report is in the format, X:Y, and in this case X is the section number, or what is termed in our software as the major header, and Y is the page number within that section. This X is the internal entry number of that major header into the LAB REPORTS file (#64.5). The LIM can make this number whatever he/she wants to when he/she creates a new major header. Once set, it cannot be changed unless the major header is deleted and then re-entered. Also, you can never have two major headers within the same internal entry number. X will remain constant for that section, and the Y part of the page will increment.

For each major header, the name of the facility performing the tests is entered. Remember that this is a CAP requirement. This will appear either on the top or bottom of the report, depending on your entry for Top/Bot field (#5) in the LAB REPORTS file (#64.5).

In our example of X:Y (internal entry number of the major header: page increment within that major header), Y will increment when the page becomes full. When full, the page is designated at the bottom of the report as PERMANENT. The next time data is verified for this major header, a new page will print (X:Y+1). This page is a TEMPORARY page since the page is not full. Both TEMPORARY and PERMANENT are chart table copies of a patient’s laboratory data. The only difference is that once a page is designated PERMANENT, it will not reprint with the cumulative report. This page will never have a follow-up page to take its place since there will never be any updated or new data printed on it. A TEMPORARY page may or may not be updated in the future. For filing purposes, if there are two TEMPORARY pages with the same designation X:Y, only the page with the most recent date needs to be maintained.

###### What is a Minor Header?

Since our major headers are the “sections” of our report and are used for naming the pages, we need to consider just what the contents of each of these pages are. The contents of these pages are set up in the minor headers. Two formats can be used for these minor headers:

- the vertical display
- the horizontal display

These displays have several features in common. The full name of the minor header will be printed. You can have these names more fully define the contents of that page; e.g., Hepatic Profile, General Chemistry Tests, Autoimmune Disease Panel, CBC, etc.

1.	For each minor header, there can only be one site/specimen. This has to be a valid entry in the TOPOGRAPHY FIELD file (#61), such as plasma, urine, etc.

2.	Units of measurement— reference ranges — will print for each of the tests. This reference range can be in numeric (5-10) or free text (“NonObs”).

3.	Values outside the reference range are flagged as either L (low) or H (high), and if critical values have been entered in LABORATORY TEST file (#60) for the test — L* (low, critical) or H* (high, critical).

4.	Comments tied to the accession number can be footnoted to the report. Comments (at this time) are tied to an accession and not to an individual test.

5.	Print name for the tests will be the print name from File 60, but this can be modified.

6.	Print code set up in LABORATORY TEST file (#60) will be executed for each test. This can be modified, but requires an understanding of MUMPS code.

###### Vertical Display

If the LIM chose a vertical display, only one display can exist for a major header. The tests will be listed to the far left-hand side of the page. The column width is fixed at ten columns wide. The first print field for test values is in column nine. Units of measurement and reference ranges appear to the right of the test values.

###### Horizontal Display;

Test names, units of measurement, and reference ranges are listed horizontally across the top of the page. If your laboratory is using this format, you may have more tests than what will fit across the top of the page. If this is the case, the tests will wrap to a new line. You can use several horizontal formats to each page. The minor header will not print to this page unless one test in the minor header has verified data. This format can also be used to have several site/specimens appear on one page. An example of this is low-volume tests performed in Chemistry. The LIM might want to call the major header SPECIALS. Under this major header, she could have several minor headers such as STOOL SPECIAL TESTS - site/specimen: Stool, PLASMA SPECIAL TESTS - site/specimen: Plasma, URINE SPECIAL TEST-site/ specimen: Urine, etc. In this manner, the LIM could designate many infrequently ordered tests to one major header of your cumulative. The default column width for the horizontal format is set to seven. However, the wider widths seem to give an easier to read report. Odd numbers work best since the software tries to place the test name in the center of the column width.

##### Rerun Options of the Cumulative

If the cumulative fails to print, is interrupted, or a permanent page becomes lost, there are several reprint (rerun) options available. Again, if you are involved with the “printing of the CUME” be aware of these options.

NOTE	It is very important that any reprints must be done before the next cumulative is run.

###### By Patient

Reprint Cumulative on a Given Patient [LRAC PT]

If a single patient’s cumulative needs to be reprinted after the full run of a cumulative, use this option. The Reprint Cumulative on a Given Patient [LRAC PT] option can also be used to reprint the patient’s entire cumulative by choosing the following selection:

**Selection number 1** - Re-initialize/Print Patient’s Previous Cumulative of this option, can be used to print from a specified date.

Initially, this may not take a long time to run. However, if the patient's entire cumulative needs to be rerun to a much earlier date, it may take a long time and might affect the system’s performance. Selection number 1 should not be used except in extreme cases, and it should be stressed to staff etc., how important it is to know what to maintain in a patient's chart. If Selection number 1 is chosen, a warning message will appear:

****THIS PRINTOUT MUST BE CHARTED!!!****

The computer system will then tell you the starting date for which there is a cross-reference for data to appear on the cumulative. If only a single page in a patient’s chart needs to be reprinted, you should use the Reprint a Permanent Page from Cumulative [LRAC 1 PAGE] option. The user, however, must know the Permanent Page that needs to be printed.

**Selection number 2** - Reprint Patient’s Previous Cumulative of this option should be used for printing the patient’s last cumulative printing.

However, you can only reprint from the day’s previous run. If the cumulative has been run again, you will not be able to print a patient’s cumulative for runs other than the last printing. This has caused a lot of problems for many sites.

NOTE	The cumulative can be spooled, but it takes lots of IRM time.

###### Reprint a Permanent Page from Cumulative [LRAC 1 PAGE]

This option reprints a single permanent page from a patient’s cumulative. The page number must be specified in the same format as it is printed on the cumulative. Device settings and definitions must be the same as when the page originally printed.

###### By Location:

###### Reprint Cumulative on a Given Location [LRAC LOC]

This can be used to print a single ward location if something happened during the full run of the cumulative. This option cannot be used for non-standard locations such as FILE ROOM.

###### Reprint Cumulative from Location to Location [LRAC LOC-LOC]

By far the easiest to use. This option may also be used to initiate the unfinished portion of a cumulative. If pages have misprinted, you can designate a location, choose the patient within that location to start with, and then choose the ending location and the patient to end with. A very easy to use option.

#### Interim Reports

Interim reports are designed to display or produce a printed report of verified lab results that occur in the interim of the running of the cumulative. These reports are in a different format from the cumulative.

The intent was that these reports would serve at an intervening time from one cumulative printing to another. However, some medical centers have decided to use these as chartable copies for some hospital locations, such as outpatient clinics. This is a decision your MAS department may want to make. It is most important to remember that the interim was not intended to keep up with patient movement. The location entered during the accessioning process will be the location used for printing purposes. This can create problems in getting the printouts to the correct location.

Interim reports will include comments from LABORATORY TEST file (#60), Site/Specimen field (#100), Interpretation subfield (#55). At this time these comments do not appear on the cumulative report.

Both MI and CH subscripted are available for review with the interim report options. An accession area must have a print order set up in ACCESSION file (#68) for results to print on the interim report. For non-lab users (no LRLAB key), only those tests set up as Both or Output in LABORATORY TEST file (#60) will print on interim reports. Users having the LRLAB key may see data entered as Input Only.

Since only verified reports will be displayed, the interim reports will not display the status of tests (i.e., incomplete, testing in progress) and hospital staff should be instructed to check the Order/Test Status [LROS] option before generating an interim.

There are several ways to generate interim reports:

- Called up automatically for various times of the day using TaskManager
- Printed as reports become available (STAT interims)

The “STAT” or automatic interim report feature was enhanced in Version 4. If these reports are used only as a convenience report and not for charting, a site may now select to print only a range of urgencies. A field is available in INTERIM REPORTS file (#64.6) called Urgency Cutoff field (#4). This field can be used to establish a range of urgencies to print automatically to a certain location (i.e., If Stat=1, Pre-Op=2, Routine=3, and Pre-Op is entered into this field, then any urgency “less than” or “equal to 2” will print automatically). The numeric designation is assigned during the enter/edit process on creation of the urgency in the URGENCY file (#62.05).

When deciding to use the automatic interim feature, please keep in mind that every time a test is verified, re-verified etc., a report will print. If you have several tests per accession number and each test is verified separately, you will generate a sheet for each time, a test on the accession number is verified.

- Called up manually through a menu option for either one patient or a hospital location

Those using the interim for lookup purposes (other than Interim Report for Selected Tests as Ordered [LRRSP] option), you need to remember that the dates used in the selection for review are the collection date and time. All interim reports print in inverse date order.

**NOTE: Results which are auto released do not trigger automatic printing of the Interim Report.**

##### Interim Report Menu Options (Manual)

Menu options can be selected for locations or patients. The real plus for all the options by patient is the ease by which data can be retrieved. For lookup, all you need is the patient’s name and an approximate date range.

###### By Patient

###### Interim Report [LRRP2]

This report will output all tests within a specified time period for a given patient. At present, the default time range is T (today) through T-7. Only verified results are available. Microbiology data is now available through this option. At present, one page is printed per accession area if this option is printed.

Option: Interim Report [LRRP2]

Select Patient Name: **LABPATIENT, TWO** 12-2-43 000000002

Date to START with: TODAY// **&lt;RET&gt; (APR 9, 1989)**

Date to END with: T-7// **&lt;RET&gt; (APR 2, 1989)**

DEVICE: HOME// **[Enter print device]**

Many of the ward staff are using the defaults that have been set up in these options. For acute care patients, this might lead to an overwhelming amount of paper. Instruct anyone using the system to use the smallest date range possible. If they are unsure of a date or do not know the date, encourage them to use the option Order/Test Status.

**or:**

Select Patient Name: **LABPATIENT, TWO** 12-2-43 000000002

Date to START with: TODAY// **&lt;RET&gt; (APR 9, 1989)**

Date to END with: T-30// **&lt;RET&gt; (MAR 2, 1989)**

DEVICE: HOME// **[Enter print device]**

Please note that the user can specify any time period. It is important that your hospital staff know an approximate time range available to them. (How long will you keep data in the system — 90 days, 60 days?) If data is to be looked up for a previous calendar year, the date entered must include the month, the day, and the year.

Because of the complexities of the archiving algorithm, there is no good way of indicating an exact time period available in the system. Data is available if it is still in the ^LR global. Your site, if T-90 is used at the time of archiving, can at least guarantee 90 days for CH-subscripted tests and 365 days + 90 days for MI-subscripted tests.

###### Interim Report for Selected Tests as Ordered [LRRSP]

This report is a detailed format for an individual patient. The report is displayed for selected tests as they were ordered (lookup is done by orders in ^LRO(69)). This option allows the user to select a specific test or panel, or select the “ANY” test default which will output all verified tests for that patient during the specified time period.

Again, please remember, only verified tests will print with this option or any of the interim report options.

The time period available for lookup with this option is based on different criteria from the other interim report options. The period of time available for lookup is set up in the for Grace Period for Orders field (#15) in LABORATORY SITE file (#69.9). Whatever is in this field entry will be at least the minimum retention available for lookup.

###### Interim Report for Selected Tests [LRRP3]

The Interim Report for Selected Tests; [LRRP3] option is not to be confused with the Interim Report for Selected Tests as Ordered [LRRSP] option. This option allows you to select a test or multiple tests for lookup, even if the orders have been purged, the data is available.

###### By Provider

Interim Report by Provider [LRRD

This report can be used to select single provider, a range of providers, or all providers. Only one day’s worth of results can be printed. If more than one provider is selected, the printout is alphabetical by provider. There will be a title page with the first few characters of the provider’s name as section breaks. Then the patient’s name will follow in alphabetical order.

Interim Report by Provider

DAILY REPORT FOR DAY: TODAY// **&lt;RET&gt;**

Do you want (A)ll providers, a (R)ange of providers,

or (S)elected providers? S// **&lt;RET&gt;**

Interim Reports for 1 Provider (manual queue) [LRRD BY MD]

This report is for only one Provider for one day. Both of the Provider reports as well as the other interim report options use the collection date of the specimens.

###### By Location

Interim Reports for 1 Location (manual queue) [LRRS BY LOC]

This option reports all verified results from one ordering location for one collection date. The user will request the collection date and ordering location. Each patient's verified results for orders placed under the specified location as well as for orders placed under other locations on the specified collection date will print so as to provide complete laboratory information on the patient. (Patients who do not have orders placed under the selected ordering locations will not print.) If a test is collected on one day and verified on the next day, you must select the collection date.

This option is to be used for information only and should not be charted. The report prints site codes for tests.  You will be asked if you would like to print an address page.  The address page prints on a separate page(s) at the end of the report and lists the performing lab name, address and site code.

This option can be used by ward staff to call up data for patients on their respective floors. This option could be useful to call up before ward rounds. Many floor locations with the new system may be different from what the house staff is currently using. The staff should know these location names. CCU may now be 5ICU or other floors may be subdivided into several wards. (i.e., can be divided into three locations, in the system - 3B (NEURO), 3B (RHEUM), and 3B (ORTHO.)

These reports contain more than one accession per page and print by order number. Therefore, less paper is generated than by Interim Report by Patient.

Each time the option is called, all verified results for that collection date will print. An example of this would be if you use this option at 6 A.M. for rounds to get the verified results for that day, you would get all verified data since 12:00 A.M. to 6:00 A.M. If you call this report again at 1:00 P.M. that afternoon, you would get all the verified data for that day from 12:00 A.M. until 1:00 P.M. that day. You cannot get only the new data since the last printing of your interim report. The old data is repeated with the new verified data.

Interim Reports by Location (manual queue) [LRRS]

This option is the manual equivalent of the tasked options. The report prints according to the ordering location, not the patient's current location.  This option is an alternative to having the Interim report tasked.  For tasking, see option LRTASK DAILY INTERIM 1. If no results are available for a location, the option will print out the location heading followed by the next location heading.

Each patient's verified results for orders placed under the specified location(s) as well as for orders placed under other locations on the specified collection date(s) will print so as to provide complete laboratory information on the patient. (Patients who do not have orders placed under the specified location(s) will not be printed.)

The date chosen for this report is the collection date.  If a test is collected on one day and verified  on the next day, you must select the collection date.

The report prints site  codes for tests.  You will be asked if you would like to print an address page.  The address page prints on a separate page at the end of the report and lists the performing lab name, address and site code.

All locations will print unless otherwise specified. Again, all data for that day will print whether or not the option or floor had data printed at earlier times. The sorting sequence of this report will be alphabetically by location and then alphabetically within location.

This option is not part of the cumulative report and should not be charted.

###### Interim Contents

What can you expect to find on your interims?

The format of the interim is entirely different from that of the cumulative report. Some of the features of this report include:

- Form number 10-1338
- Patient demographic information:	Name, social security number, age, and ward location
- Title, which includes hospital name followed by Clinical Laboratory Report
- Date and time of printing of the report
- ordering information: Provider, date and time of collection, and specimen type
- Laboratory data

This section includes the name of the test as it appears in the LABORATORY TEST file (#60). However, for laboratory test names in File #60 that exceed more than 20 characters, the report defaults to the name in the Print Name field of File #60. For long panels, if one name exceeds 20 characters, this can make for some strange output.

The laboratory result is displayed with units of measurement and reference range for the specimen type. If the $SELECT function was used for sex or age for reference lows and highs, the correct reference range to match the patient’s age or sex will be displayed.

The tests will also appear according to the print order number assigned within an accession area.

If you have entered information in the Interpretation subfield of the field Site/Specimen in File #60, the information will be displayed as:

Eval:	And your interpretation...

There is also a KEY: to explain any high, low, or critical value flags.

#### Supervisor’s Report

The Supervisor’s Report outputs results by hospital location for a single (or group of) major header(s) as defined in the LAB REPORTS file (#64.5). This report uses the same file as the cumulative report to retrieve data. Since the cumulative report updates this file, the Supervisor’s Summary Report for TASKMAN [LRTASK ACS] option should be run after the cumulative report is finished.

- The Daily Summary Reports field (#15) in LAB REPORTS file (#64.5) is an arbitrary name given to a particular report. For each name, any number of headers can be selected to be included in the report. These headers point to the major headers already defined in the same file. All tests that are defined for the major headers will be included in the Report.
    - Unless the Sort By Patient field (#14) in the LAB REPORTS file (#64.5) is set to “YES” the report is sorted by location.
        - To task the report, use the Task Manager Schedule/Unschedule [ZTMSCHEDULE] option and answer the prompts for “Queued to Run at What Time” field (#200), “Device for Queued Job” field (#201), and “Rescheduling Frequency” field (#202). This report may also be scheduled by editing the OPTION file (#19).
            - To manually request a Supervisor’s Report, use the Supervisor’s Report [LRACS MANUAL] option in the Supervisor Reports Menu [LRSUPER REPORTS].

### Lab Menu Options

#### Laboratory  Menu [LRMENU

The Laboratory VistA Menu is the Laboratory package main menu. This menu includes all the options that is used by the Lab package. It is locked with the LRLAB key.

1      Phlebotomy menu ... [LR GET]

2      Accessioning menu ... [LR IN]

3      Process data in lab menu ... [LR DO!]

4      Quality control menu ... [LRQCM]

5      Results menu ... [LR OUT]

6      Information-help menu ... [LRHELP]

7      Ward lab menu ... [LRWARDM]

8      Anatomic pathology ... [LRAP]

**&gt; Locked with LRANAT

9      Blood bank ... [LRBL]

**&gt; Locked with LRBLOODBANK

10     Microbiology menu ... [LRMI]

**&gt; Locked with LRMICRO

11     Supervisor menu ... [LRSUPERVISOR]

**&gt; Locked with LRSUPER

Access to different parts of this menu are based on what keys you are assigned and which part of the menu is assigned to you.

#### Phlebotomy Menu [LR GET]

This menu contains options that the lab uses to **get** (collect) the test orders and specimens.

Add tests to a given accession. [LRADD TO ACC]

**&gt; Locked with LRLAB

Add tests to an already existing order number. [LRADD TO ORDER]

Add to collection list [LRPHMAN]

**&gt; Locked with LRPHSUPER

Delete entire order or individual tests [LRCENDEL]

Itemized routine lab collection [LRPHITEM]

Lab orders by collection type [LRRP5]

Lab test order [LROW]

List of lab orders not collected [LRNODRAW]

List of orders not collected (Long form) [LRNDLST]

Order/test status [LROS]

Print collection list/labels [LRPHLIST]

Print Future Collection Labels [LRUFCL]

**&gt; Locked with LRLAB

Print Single Future Collection Label [LRUFCLS]

**&gt; Locked with LRLAB

Receipt of routine lab collection from wards [LRPHEXCPT]

Test description information [LREV]

Ward lab menu ... [LRWARDM]

PA     Interim report  [LRRP2]

Interim report for selected tests as ordered [LRRSP]

Add tests to an already existing order number. [LRADD TO ORDER]

Delete entire order or individual tests [LRCENDEL]

Fast lab test order (IMMEDIATE COLLECT) [LROW IMMED COLLECT]

Fast lab test order (ROUTINE) [LROW ROUTINE]

Fast lab test order (SEND PATIENT) [LROW SEND PAT]

Fast lab test order (WARD COLLECT) [LROW WARD COL]

General report for selected tests [LRGEN]

Graph results [LRDIST]

Interim report by provider [LRRD]

Interim report for selected tests [LRRP3]

Interim reports for 1 location (manual queue) [LRRS BY LOC]

Lab test order [LROW]

List of lab orders not collected [LRNODRAW]

Order/test status [LROS]

Reprint a Ward Collect Order [LROWRP]

Review by order number [LRCENLKUP]

Show list of accessions for a patient [LRUPT]

Test description information [LREV]

Ward collection summary for lab orders [LRDRAW]

##### Phlebotomy Menu Option Descriptions

This section lists all of the blood drawing options and descriptions contained on the Phlebotomy Menu:

**Option	Description**

Add Tests to a Given Accession	This function allows the laboratory to add additional tests to an ALREADY EXISTING accession. A test cann **ot** be added to an accession which does not exist; instead use the option Add Tests to an Already Existing Order Number if the tests have been ordered but not accessioned.

Add Tests to an Already	This function allows tests to be

Existing Order Number	ordered on an already existing order number. If **any** of the tests are already accessioned, this function cannot be used to add any additional tests; the function Add Tests to an Existing Accession in the lab must be used.

Add to Collection List	Creates collection file (the same as LRPHSET), allows user to add more to an existing file or start a new one.

Delete entire order or	This option may be used to remove

individual tests	an entire order. The reason for deleting the order must be entered. If results have already been entered and verified for any part of the order, the order cannot be deleted.

Itemized Routine Lab Collection	This function allows an itemized receipt of routine lab collection from the wards. All collections received must be individually entered.

**Option	Description**

Lab orders by collection type	Prints a report of ordered tests for a collection type (LAB COLLECT, SEND PATIENT, OR WARD COLLECT) and a date.

Lab Test Order	This is to be used by the wards for order entry, not by the lab! The purpose of this function is to allow selection between sending the patient or specimen with the order number to the lab where it can be accessioned, or holding the test request in the computer until a collection list can be made and routine phlebotomy collection by the laboratory on the wards occurs.

List of Lab Orders not Collected	This option lists orders which have been indicated as not being collected by the phlebotomist after routine collection by lab on the ward.

List of orders not collected	This option is a complete display of

(Long form)	orders in File #69 which do not have a status of “C” (collected) and have a collect type of LC, SP, or WC. This option is the same as List of lab orders not collected option except that it is more complete.

Order/test status	After selecting a patient the status for all tests for that day is given. Each day will be prompted in inverse order. Future days can be requested. The report will output for a specified patient, Order #, Urgency, Status (test complete, on collection list, testing in progress, collected), Provider, and Accession #.

**Option	Description**

Print collection list/labels	Prints information which may be used for routine phlebotomy collection.

Print Future Collection Labels	This option is used to print collection labels for Lab collect. This option has several possible uses. The routine will print any order, which has the collection type of Lab Collect (LC), or Immediate Collection (IC). IC is what the ward uses to request specimen collection at a specific time outside of scheduled routine collection time (LC). Not all sites will provide the IC service. The option will prompt dates to search for uncollected LC and IC collection types.

The option will search those dates and print collection labels. A collection label differs from an Accession Label in two areas:

1) A collection label can be printed only for uncollected specimens.

2) The collection label has no accession number, instead the requested collection time is printed.

Except for these two areas, the two labels have identical information. A possible use for this option would be to print a list of patient collection labels in anticipation of computer down time. This option prints all orders having the type of LC or IC for the specified date(s). The option Print Single Future Collection Labels should be used to obtain a single collection label.

**Option	Description**

Print Single Future Collection	This option is a single label version of

Label	Print Future Collection option. There are two major differences from the other option.

1) This option requires the user to supply the Order Number.

2) It only prints a single label at a time.

Receipt of routine lab	After routine phlebotomy collection

collection from wards	has been made, accessions are designated as being in the lab by running this function. For a given location, orders not collected may be indicated, with the remainder for the location being logged in.

Test description information	This function display limited information from the LABORATORY TEST file (#60), such as special ordering information, normal ranges, etc.

Ward lab menu	For options name and descriptions assigned to this menu, please see the section on Ward lab menu of this manual.

### Accessioning Menu [LR IN]

This menu contains the options used to order laboratory tests for the Laboratory V. 5.2 software package.

Accessioning tests ordered by ward order entry [LROE]

Accessioning, standard (Microbiology) [LRMICROLOGIN]

Add tests to a given accession. [LRADD TO ACC]

**&gt; Locked with LRLAB

Bypass normal data entry [LRFAST]

Delete entire order or individual tests [LRCENDEL]

Delete test from an accession [LRTSTOUT]

Fast lab test order (IMMEDIATE COLLECT) [LROW IMMED COLLECT]

Fast lab test order (ROUTINE) [LROW ROUTINE]

Fast lab test order (SEND PATIENT) [LROW SEND PAT]

Inquiry to LAB TEST file [LRTESTDIQ]

**&gt; Locked with LRSUPER

Lab add test(s) to an existing order [LRADDTST]

**&gt; Locked with LRLAB

Lab orders by collection type [LRRP5]

Lookup accession [LR LOOKUP ACCESSION]

Manual Enter Clinic Stop Codes [LRSTOPC]

**&gt; Locked with LRLAB

Manually accession QC, Environmental, etc. [LRQCLOG]

Multipurpose accessioning [LRQUICK]

Order/test status [LROS]

Print accession list(s) ... [LRUAC]

Accession and test counts by shift [LRUPACS]

Accession list by date [LRUPAD]

Accession list by number [LRUPA]

Lab accession and test counts [LRUPAC]

Test counts by treating specialty [LRUPACT]

Print future collection labels [LRUFCL]

**&gt; Locked with LRLAB

Print single future collection label [LRUFCLS]

**&gt; Locked with LRLAB

Reprint accession label(s) [LRLABXT]

Reprint order accession label(s) [LRLHBXOL]

Review by order number [LRCENLKUP]

Show list of accessions for a patient [LRUPT]

Special test accessioning [LRNONCOM]

Test description information [LREV]

##### Accessioning Menu Option Descriptions

These options are used to order laboratory tests.

**Option	Description**

Accessioning tests ordered by	The first question asked is the Order

ward order entry	number. If the order has not been placed in the computer, this number does not exist and the question should be skipped. The patient and test information will be asked and an order number assigned. The option will then proceed to accession the order as if the Order number had been entered in the first place. The Order number is normally assigned at the time the ward places the order. This option is then used to accession tests ordered and brought to the lab by the ward, or to accession tests ordered by the ward and brought to the lab by the patient.

Accessioning, standard	This option allows you to accession

(Microbiology)	requested tests. It is especially useful for accessioning unusual specimens, or accessioning specimens that require a descriptive comment. You may also comment about the order. When you are asked to select the label printer, if you enter “^” labels will not be printed. You will then be asked to select a label printer with each new patient you select. When you select a printer, that printer will be used until you end that session.

**Option	Description**

Add tests to a given accession	This function allows the laboratory to add additional tests to an ALREADY EXISTING accession. If the accession does not exist, it cannot be done. A test cannot be added to an accession which does not exist; instead use the Add Tests to an Already Existing Order Number option if the tests have been ordered but not accessioned.

Bypass normal data entry	This option bypasses normal ordering, accessioning, and data entry. Where the results are in hand and no information regarding the order is in the computer, this option may be used to enter the patient name, the test, and the results. Note that information such as the person ordering the test, or alternative routing information is not asked (the report routing is taken from MAS information in the computer).

Delete entire order	This option may be used to remove an

or individual tests	entire order. The reason for deleting the order must be entered. If results have already been entered and verified for any part of the order, the order cannot be deleted.

NOTE:	If a panel component is being deleted and other components of that panel remain on the order, an electronic signature will not be required for cancel reasons which otherwise require an electronic signature.  Electronic signature is only required when the entire ordered test is deleted.

Delete test from an accession	This option may be used to remove individual tests from an accession.

NOTE:	If a panel component is being deleted and other components of that panel remain on the order, an electronic signature will not be required for cancel reasons which otherwise require an electronic signature.  Electronic signature is only required when the entire ordered test is deleted.

Fast lab test order 	This option is used by the wards to

(IMMEDIATE COLLECT)	request immediate collection of a test specimen by the laboratory. This option is similar to the Fast Lab Test Order (ROUTINE) except that these orders are not for scheduled laboratory collection times. These orders are placed for irregular collection times. Immediate Collect orders are restricted because the laboratory has set certain periods and days when this option can be used. If the requested times are not allowed, the user must make a PHONE CALL TO THE LAB TO ARRANGE FOR SPECIMEN COLLECTION

NOTE	It is recommended that the ordering person always call the laboratory to confirm the receipt of the placed order.

**Option	Description**

Fast lab test order (ROUTINE)	Tests for routine collection on the ward by the lab may be entered with this option before the creation of a collection list.

Fast lab test order	Same as multipurpose accessioning

(SEND PATIENT)	dialogue, only no labels are made, no accessions are created, and only appropriate for “SEND PATIENT” type of orders. The order number generated is used under the function “Accessioning Tests From Ward Order Entry” to generate the labels and indicate the specimen is in the lab.

Inquiry to LAB TEST file	This function displays information from the LABORATORY TEST file (#60). All defined fields that are associated with the requested test in File #60 are displayed. If information is missing on a particular test, the desired information must be first added to File #60. This option is just a lookup option to allow the user to inquire about how a test is defined in the LABORATORY TEST file (#60).

Lab add test(s) to an existing order	Tests on additional specimens may be kept with the original order number using this option. Note that additional accession(s) will be created.

Lab orders by collection type	Prints a report of ordered tests for a collection type (LAB COLLECT, SEND PATIENT, OR WARD COLLECT) and a date.

Lookup accession	This function allows the user to find information about a single accession.

**Option	Description**

Manual Enter Clinic Stop Codes 	This option is used to load clinic stop codes manually. This option should be used when the system has been down and none of the stop codes were captured.

NOTE	If you plan to retroactively accession your work that was missed during system down time, *there is no need to use this option. It will be captured automatically.*

.;

Manually Accession QC,	This option allows you access to various

Environmental, etc.	files other than the PATIENT file (i.e., REFERRAL PATIENT file (#67), RESEARCH file (#67.1), STERILIZER file (#67.2), ENVIRONMENTAL file (#67.3)) to accession Quality Control and other non-patient specimens and proficiency testing samples. These files may also be accessed via regular accessioning options (multipurpose, etc.) by use of “extended syntax” at the “Select Patient name:” prompt enter the file name (or enough letters to define the unique name) followed by a colon and then the name of the desired entry.

**Example**

Select Patient name: S: LAB AUTOCLAVE

**Option	Description**

Multipurpose accessioning	This function can be used by the laboratory to accession manually requested tests into the computer. Different areas of the laboratory may have different lists of their most often ordered tests (Accession Test lists) to speed entry. If one selects a single test on set-up, the function serves as a means of batch entry of the single test.

Order/test status	After selecting a patient, the status for all tests for that day is given. Each day will be prompted in inverse order. Future days can be requested. The report will output for a specified patient, Order #, Urgency, Status (test complete, on collection list, testing in progress, collected), Provider, and Accession #.

Print accession list(s)	Lists of accessions for an accession area. You have a choice of by date, by number, by patient, or for a collection sample.

Accession and Test Counts	Lists counts of each type of specimen and

by Shift 	tests in the ACCESSION file (#68) by shift from one date to another.

Accession List by Date	Provides a list of accessions for an accession area by date. You can print by accession number, patient, or collection sample.

Accession List by Number	Provides a list of accessions for an accession area by number. You can print by accession number, patient, or collection sample.

**Option	Description**

Lab Accession and Test	Lists counts of each type of specimen and

Counts	counts of each test from one date to another in the ACCESSION file (#68). If Autopsy, Surgical pathology, Cytopathology, or EM is selected only accession counts are given.

Test Counts by Treating	This option lists tests and counts by

Specialty	treating specialty for date range specified.

Print future collection labels	This option is used to print collection labels for Lab collect. This option has several possible uses. The routine will print any order that has the collection type of Lab Collect (LC) or Immediate Collection (IC). IC is what the ward uses to request specimen collection at a specific time outside of scheduled routine collection time (LC). Not all sites will provide the IC service. The option will prompt dates to search for uncollected LC and IC collection types. The option will search those dates and print COLLECTION LABELS.

A collection label differs from an Accession Label in two areas.

**1)** A collection label can be printed only for uncollected specimens.

**2)** The collection label has no accession number, instead the requested collection time is printed.

**Option	Description**

Print future collection labels	Except for these two areas, the two labels

(Continued)	have identical information. A possible use for this option would be to print a list of patient collection labels in anticipation of computer down time. This option prints all orders having the type of LC or IC for the specified date(s). The Print Single Future Collection Labels option should be used to obtain a single collection label.

Print single future	This option is a single label version of

collection label 	Print Future Collection option. There are two major differences from the other option.

**1)** This option requires the user to supply the Order Number.

**2)** It only prints a single label at a time.

Reprint accession label(s)	Reprint the labels for a selected accession or range of accessions.

Reprint order accessions label(s)	This option will reprint all of the accession labels for an entire order.

**Option	Description**

Review by order number	Essential information related to the order can be displayed with this function if the order number is known.

Show list of accessions	If you need to find all the accession

for a patient 	numbers (in one accession area) for one patient, you may do so with this option. All lab tests associated with each number are also displayed. The information is displayed on the screen only. You cannot print the list with this option.

Special test accessioning	Similar to Multipurpose accessioning, several additional questions are asked in this option. Key question indicates which accession area the test(s) will be put under and which file must be accessed (Patient, Referral, Environmental, etc.,). If the order number is known and entered, the accessioning is the same as the [LROE] option with the above noted exception. This option may be used for accessioning such specimens as employee health patients and other nonstandard patients; e.g., research animals. This is the only option that allows a tech to choose an accession number (not automatically assigned by the system).

Test description information	This function displays limited information from the LABORATORY TEST file (#60). Such as special ordering information, normal ranges, etc.

**Accessioning for an Institution in a Multi-Divisional Facility**

Multidivisional facilities can customize the number of labels required for a selected lab test at a selected institution. Using FileMan, the LIM defines the number of labels required, beyond the default number, in LABORATORY TEST File (#60).

The requirements and procedures associated with printing labels for institutions that share the same Veterans Integrated System Technology Architecture (VistA) database are addressed utilizing two new fields: The INSTITUTION EXTRA LABELS field (#60.15,01) and the NUMBER OF LABELS subfield (#60.15,1).

When a Laboratory package user logs in and accessions a lab test, the extra labels print automatically if the domain to which the user belongs, and the lab test ordered, have been previously configured for extra labels in the INSTITUTION EXTRA LABELS field ((#60.15,01).

For further detail on the implementation of this feature for institutions in a multi-divisional facility contact the LIM who manages the VistA database for your institution. Additional information is also available in the Laboratory Planning and Implementation Guide.Process Data in Lab Menu [LR DO!]

This menu contains options the Laboratory uses to process ( *do* ) data on the specimens.

EA     Enter/verify data (auto instrument) [LRVR]

EL     Enter/verify data (Load list) [LRVRW2]

EM     Enter/verify/modify data (manual) [LRENTER]

EW     Enter/verify data (Work list) [LRVRW]

GA     Group verify (EA, EL, EW) [LRGV]

**&gt; Locked with LRLIASON

MP     Misc. Processing Menu ... [LR PROCESS, MISC]

GD     Group data review (verified &amp; EM) [LRGVP]

GU     Group unverified review (EA, EL, EW) [LRGP]

Active Load Work Listing [LRLLPA]

Clear instrument/worklist data [LRINSTCLR]

**&gt; Locked with LRVERIFY

Incomplete test status report [LRWRKINC]

Insert a Sample on a Load/Work list [LRLLINST]

Keypad differential for CRT's [LA KB DIFF]

*Lab statistics menu ... [LR WKLD]

Long form accession list [LRACC1]

Move a Load/Work list entry [LRLLMOVE]

Remove a Load/Work list entry [LRLLREMV]

Rollover Accession (Manual) [LR ROLLOVER]

Set new "starting sequence number" [LRLL NEW 1ST SEQUENCE #]

Short accession list [LRACC2]

Smac Support menu ... [LRSMACMENU]

Clear instrument/worklist data [LRINSTCLR]

**&gt; Locked with LRVERIFY

Flagged Specimens [LRSMAC3]

Group verify (EA, EL, EW) [LRGV]

**&gt; Locked with LRLIASON

Halt Smac Run [LRSMAC6]

Quality control display (Levey-Jennings) [LRQC]

Run Smac [LRSMAC5]

Work sheet Accession list [LRACC3]

Work sheet of all unverified accessions for a date [LRACC4]

Accession order then immediately enter data [LR ACC THEN DATA]

Batch data entry (chem, hem, tox, etc.) [LRSTUF]

**&gt; Locked with LRVERIFY

Build a load/work list [LRLL]

Bypass normal data entry [LRFAST]

Download a load list to an Instrument. [LA DOWN]

Fast Bypass Data Entry/Verify [LRFASTS]

**&gt; Locked with LRLAB

Lookup accession [LR LOOKUP ACCESSION]

Order/test status [LROS]

Print a load/work list [LRLLP]

STD/QC/REPS manual workload count [LR WKLD STD/QC/REPS]^

Unload Load/Work List [LRLLCT]

*Lab statistics menu ... [LR WKLD]

Edit Workload Comments [LR WKLD COMMENTS]

File listings ... [LR WKLD3]

**&gt; Locked with LRSUPER

1      WKLD code list by code [LR WKLD CODE BY CODE]

2      WKLD code list by name [LR WKLD CODE BY NAME]

3      Lab section list by code [LR WKLD SECTION BY CODE]

4      Lab section list by name [LR WKLD SECTION BY NAME]

5      Lab subsection list [LR WKLD SUBSECTION]

6      Lab subsection by Lab section [LR WKLD SUB BY SECTION]

7      Service dictionary [LR WKLD SERVICE]

8      Requesting center dictionary [LR WKLD REQUEST]

9      Test dictionary [LR WKLD TEST DICT]

10     WKLD log file download [LRCAPDL]

Lab test turnaround time [LR CAPTT]

LMIP Reports/Data Collection ... [LR WKLD4]

**&gt; Locked with LRLIASON

1      PHASE 1: Move data from 64.1 to 67.9. [LR WKLD LMIP 1]

**&gt; Locked with LRSUPER

2      PHASE 2: Collect data for transmit to NDB. [LR WKLD LMIP 2]

**&gt; Locked with LRSUPER

3      PHASE 3: Print of data to be sent to NDB. [LR WKLD LMIP 3]

**&gt; Locked with LRSUPER

4      PHASE 4: Create E-mail message for NDB. [LR WKLD LMIP 4]

**&gt; Locked with LRSUPER

PHASE 5: Purge monthly WKLD data from 67.9. [LR WKLD LMIP 5]

**&gt; Locked with LRLIASON

Recompile Phase 1 LMIP Data. [LR WKLD LMIP 1 REPEAT]

**&gt; Locked with LRSUPER

Review accession workload [LR WKLD AUDIT]

STD/QC/REPS manual workload count [LR WKLD STD/QC/REPS]

Turn on site workload statistics [LR WKLD STATS ON]

**&gt; Locked with LRLIASON

Turn on workload stats for accession area

[LR WKLD STATS ON ACC AREA]

**&gt; Locked with LRLIASON

WKLD statistics reports ... [LR WKLD2]

**&gt; Locked with LRSUPER

1      PHASE 3: Print of data to be sent to NDB [LR WKLD LMIP 3]

**&gt; Locked with LRSUPER

2      Workload statistics by accession area and shift [LRRP8]

**&gt; Locked with LRSUPER

3      Workload cost report by major section [LRCAPML]

4      Detail Workload Report [LRRP6]

5      Treating Specialty Workload Report [LRCAPTS]

6      Workload Report [LRCAPR1]

Workload manual input [LR WKLD MANUAL INPUT]

##### Process Data in Lab Menu Option Descriptions

These options are used to process data on the specimens.

**Option	Description**

Enter/verify data	Data from an automated instrument

(auto instrument)	can be reviewed/edited individually by accession, by worklist sequence, by tray-cup. If the LRVERIFY key is owned, the data may also be verified. Once verified, the data are not available for viewing with this option. Likewise, if test results have been previously verified for a given accession, even new data from the automated instrument can neither be viewed nor verified. Entering the “*” character for any entry will substitute the word “canceled” as the result.

Enter/verify data (Load list)	Data from a loadlist can be reviewed /edited individually by the sequence defined on the loadlist. If the LRVERIFY key is owned, the data may also be verified. Once verified, the data are not available for viewing with this option. Likewise, if test results have been previously verified for a given accession, even new data can neither be viewed nor verified.

Enter/verify/modify data	Data may be entered and validated (if

(manual)	LRVERIFY key is owned). Data that has been previously validated may be corrected. Entering the “*” character for any entry will substitute the word “canceled” as the result.

**Option	Description**

Enter/verify data (Work list)	Data from a worklist can be reviewed/edited individually by the sequence defined on the worklist. If the LRVERIFY key is owned, the data may also be verified. Once verified, the data are not available for viewing with this option. Likewise, if test results have been previously verified for a given accession, even new data can neither be viewed nor verified.

Misc. Processing Menu....	This menu contains menu items that have been moved from the [LR DO!] Processing menu. This relocation will allow the entire Processing menu to fit on one screen display.

Group data review (verified &amp; EM)	Batch form of LRENTER function, for printout only; no editing.

Group unverified review (EA, EL, EW)	Batch review of automated instrument data, similar printout to LRGVP; no editing or verification is done.

Active Load Work Listing	This option will print a listing of all active Load/Work which have not been [UNLOADED]. The listing shows the Load List Name, the date built, user who requested the work list to be built, and the Accession Area.

NOTE	The asterisk (*) after the date indicates list has existed for more than 1 Day

**Option	Description**

Clear instrument/worklist data	This option clears the instrument data from the ^LAH(global. Use the Unload Load/Work List options to clear load/work list.

Incomplete test status report	Use this option to display or print a report of all incomplete tests in a specific accession area. You may list by accession number or by date. You may also limit the report to a specific test of combination of tests.

Insert a Sample on a	This option allows one to insert a sample

Load/Work list	on a load/work list, and allows you to move any sample previously occupying the same position.

**Option	Description**

Keypad differential for CRT’s	This is an option for entering differential counts in hematology using a CRT keyboard. It functions very much like an automated instrument that is connected to the LSI. The parameters that define what characters on the keyboard represent what portions of the differential are defined in the AUTO INSTRUMENT file (#62.4) under the entry Keyboard Diff. For each test there are three parameters PARAM. PARAM 3 is the character on the keyboard that represents that test. For example, if the test SEGS had a PARAM 3 equal to 1, then whenever the character “1” was pressed, a SEG would be added to the total count of SEGS. Tests that occupy internal numbers 1-27 in the AUTO INSTRUMENT file (#62.4) at the level CHEM TESTS are used in the entry of the WBC count. WBC count occupies three rows of characters: (1-9), (10-18), and (19-27). The keys “-”, “!”and “?” are reserved functions. If PARAM 2 is equal to “1” for these tests, then these tests will be used in the total count of WBC cells. PARAM 2 equal to “2” means that the test is not included in the total count. PARAM 1 is used to change the value of V, which is the value of the test you are counting or editing. For example, using the previous example, whenever you press “1”, you are adding 1 to the total count of SEGS, so the value of SEGS (V at this point) is changed to a percentage of total WBC cells counted. RBC Morphology tests are located at internal numbers 31-58 occupying three rows on the keyboard (31-39), (40-48), and (49-58). The backslash “\” is used to display the WBC values. To verify data entered with this option use the “EA” option.

**Option	Description**

The conditions of reviewing and verifying data entered with this option are the same as any other automated instrument.

The Load/Work List field entries used to test this option are as follows:

NAME: DIFF

LOAD TRANSFORM: UNIVERSAL TYPE: SEQUENCE/BATCH

CUPS PER TRAY: 0

FULL TRAY'S ONLY: NO

VERIFY BY: ACCESSION

PROFILE: DIFF

ACCESSION AREA: (whatever is appropriate)

TEST: (whatever is appropriate)

This option will only work with CRT’s that have cursor addressing capabilities and is VT-100 compatible.

Lab Statistics Menu.....	This is the menu for workload recording statistical and LMIP reports. Since the Lab Statistics Menu has a number of specialized support functions, it has its own menu.

Edit Workload Comments	This option permits the editing of WKLD Workload Comments. This should be used to record special situation or changes in methods of doing or recording workload. You may edit comments for the following:

**1)** The institution (Lab)

**2)** The WKLD Code itself

**3)** Make comments for a specific date(s)

**Option	Description**

File listings....	 file listings.

WKLD code list by code	This option lists in ascending WKLD code sequence the WKLD code, procedure name, unit weight, and unit for count. You may select a range of WKLD codes to print.

WKLD code list by name	This option lists in alphabetical order WKLD code procedures. The procedure name, WKLD code, unit weight, and unit for count are listed. You may select an alphabetical range of names to work with.

Lab section list by code	This option lists by section code every WKLD section on file for your site.

Lab section list by name	This option lists alphabetically every WKLD section on file for your site.

Lab subsection list	This report lists all WKLD (lab) subsections on file for your site.

Lab subsection by Lab section	This report lists the relationship between WKLD (lab) sections and subsections.

Service dictionary	This option lists all requesting location by treating specialties for your site. This option is useful in determining which locations do not have abbreviations entered in the file. The option [LR WKLD REQUEST] Requesting Center Dictionary ONLY list treating specialties with abbreviations.

**Option	Description**

Requesting center dictionary	This option lists by abbreviation every requesting center (or treating specialty) on file for your site.

NOTE	Only those treating specialties with abbreviations will be listed by this option. Use [LR WKLD SERVICE] Service Dictionary for a complete listing.

Test dictionary	This report lists all tests and procedures, synonyms, test cost, and accession area.

WKLD log file download	This option can be used to download data from the WKLD LOG FILE (#64.03) to spread sheets. The user is able to select the character used to separate data to match the spreadsheet used. The “^” character is not allowed as a field separator and the character may not be null. The output can be captured in an ASCII file to be later imported into a spreadsheet. The Collect Wkld Log File Data field (#616) that controls the collection of the data is located in the LABORATORY SITE file (#69.9). To stop data transfer, press return/enter key.

Lab test turnaround time	Provides counts of selected tests for a hospital location for a selected time. The test must have the date and times for receipt in lab and a completion of test to be included in the report.

LMIP Reports/Data Collection...	This menu contains options which perform various function related to collection and reporting LMIP data. Also there are several related printed reports found in this menu. This menu should be controlled by the Laboratory Information Manager or the Chief Technologist. Functions performed by this menu have national impact.

.1 to 67.9;

PHASE 1: Move data	This option performs the first step in

from 64.1 to 67.9.	producing your monthly report for LMIP and management. This option's function is to extract from your workload file (#64.1) ^LRO(64.1, which contains your daily workload, and roll up the data in a condensed form. The condensed data is stored in the LAB MONTHLY WORKLOADS file (#67.9) ^LRO(67.9). This option should be used two days after the last day of the month you wish to collect data for. Refer to your package documentation for more information.

PHASE 2: Collect data 	This option is the second phase of

for transmit to NDB.	LMIP data reporting. In this step, data is condensed further and formatted for transmission to the National Database. This formatted message is stored in a temporary global from which a review report will be created for your certification. Care should be taken with who has access to this menu. The Laboratory Information Manager or the Chief Technologist should control this option.

**Option	Description**

PHASE 3: Print of data	This option produces a printable

to be sent to NDB.	report of the data the system has collected for the requested reporting period. This data is in a format that allows transmission to the National Data center. In order for you to be able to review the compiled data it must be converted to human readable format. This report allows you to have a hard copy of the LMIP data for review. This data cannot be edited. The files which the data is extracted are editable to a limited degree. If this report does not conform to your manual workload tally procedures, a package implementation review may be required. Consult your Package documentation for further information.

PHASE 4: Create E-mail message	This is the last phase of data

for NDB.	collection leading to the creation of a mail message containing LMIP data. This option will take the formatted data from the temporary file and place the data into appropriately formatted mail message. The mail message will be sent only to the user creating the message. The User must forward the message via MailMan options to the National Data location. Consult LMIP directive for the proper forwarding procedures. If for some reason the message creation fails, this option can be ran multiple times.

The National Data center will only accept one data message for a single month. Send only one message to the National Database. The second one for any month will not be processed. Consult your package documentation for more information.

**Option	Description**

.9;

PHASE 5: Purge monthly	This option is used to purge

WKLD data from 67.9.	LMIP data from the LAB MONTHLY WORKLOADS file (#67.9) after data has been sent to the national database. It can also be used to purge data that is incorrect before building Workload Mail messages. Care should be taken that data is not deleted prematurely. If the site elects to archive this file, this should be done before this option is used to delete data.

Recompile Phase 1 LMIP Data	Allows the user to rerun Phase 1 of LMIP data collection. If for some reason, it becomes necessary to recompile the LMIP report this option will delete the data in ^LRO(67.9 for the selected reporting period (Month) and then reset the pointers in ^LRO(64.1 to allow the date to be recompiled again.

Phase I LMIP must be re-run after this option is used.

NOTE	This option should not be used after data has been submitted to the .

This option should be used after LMIP data has been reviewed and errors or discrepancies are noted.

This option may use large amounts of journal space. Coordinate with IRM before using.

**Option	Description**

Long form accession list	Detailed list of accessions by accession area. The list produces a complete listing of accessions over a specified time. The user can opt to print only specified tests and/or only uncompleted entries. The status of each test for an accession is also given. Microbiology has its own “Long Form Accession list” (LRMIACC1). The Long Form Accession list can effectively replace log books, provide a list of uncompleted test(s) for an accession area, and be used at the end of the shift and work day to monitor what is left on the list. Use the option “Remove an Accession” [LRDELOG] to remove an unwanted accession so that the “rollover” option, if activated, will work as desired.

Move a Load/Work list entry	Entries on a Load/Work list may be moved to alternative positions on the list.

Remove a Load/Work List Entry	This function allows the removal of a single load or work list entry from the list.

**Option	Description**

Rollover Accession (Manual)	This option should be used if the task option LRTASK ROLLOVER does not run for some reason. This option should not be the normal method for transferring incomplete accession from the previous day to the present day's accession file. If it becomes necessary to use this option, there has probably been a problem with TASK MANAGER. IRM Service should be notified if this option is required to move accession onto day's list.

NOTE	This option can be run multiple times without harm. It checks to see if the DATE ROLLOVER LAST RUN field is set correctly before actually performing the rollover function.

Set New Starting Sequence	This function allows the user to reset

Number 	the first sequence number in the data an automated instrument transmits. This option can only be used if the instrument is set up to transmit and identify data strictly by the order the data comes off the machine.

Short Accession List	A condensed list of accessions. You may combine more than one accession area on the list that may serve as a very abbreviated worklist.

SMAC Support Menu....	Since the SMAC has a number of specialized support functions, it has its own menu.

**Option	Description**

Clear Instrument/Worklist Data	This clears the instrument data. Use the Unload function to unload the load/work list.

Flagged Specimens	Reviews the specimens which have been flagged by the SMAC.

Group Verify (EA,EL,EW)	This option provides for batch verification of automated instrument data. If a delta check or critical range check is found, the data need not be approved. Must have the LRVERIFY key to use this option.

Halt SMAC Run	Terminates the interactive link between the interface and the tied terminal for the SMAC run.

Quality Control Display	Quality control data is displayed

(Levey-Jennings)	against the normal mean and standard deviation entered for the requested test (in the Test field of the LAB CONTROL NAME file (#62.3)). The option uses a modified Levey-Jennings format to allow a printout on the VA printers. This format is vertical and the time scale is sequential and not proportional.

The report will list all dates, control values, total # of controls (N), target range, actual range obtained, and will flag any values outside of 3SD. The control values outside of 3SD are not used in the calculation of the actual range obtained. The report also has a line where the responsible laboratory official may review the output of the report (CAP Requirement). The “mean” is denoted by the ***** line, 1SD &amp; 3SD are denoted by the ..... lines, and 2SD is denoted by the ::::: lines.

**Option	Description**

Run SMAC	This option starts a new SMAC run. You must first build the load list before this option will run.

Work Sheet Accession List	This option prints an Accession list in the format of a work-list.

Work sheet of all unverified	This option will print a list of all

accessions for a date	accessions that have any unverified tests on them. It will print in the work sheet format.

Accession order then	Specimens that possess order numbers

immediately enter data	are accessioned and results are enter data entered within the one option.

.);

Batch Data Entry	Once the set of accessions is specified, and

(chem, hem, tox, etc.)	the test to be edited is specified, the system loops through the accessions with minimum tech intervention. If the Automatically Stuff option is selected, and the text for entry is preceded by a “/” the text will not be checked with the input transform (data of a type other than that defined in the LABORATORY TEST file (#60) may be entered; (e.g., /canceled) for numeric fields.

Build a Load/Work List	This creates a load or work list for an instrument or manual test(s).

**Option	Description**

Bypass  Data Entry	This option bypasses normal ordering, accessioning, and data entry. When the results are in hand and no information regarding the specimen is in the computer, this option may be used to enter the patient's name, the test, and the results.

NOTE	Information such as the person ordering the test or alternative routing information is not asked (the report routing is taken from MAS information in the computer).

Download a Load List 	This option invokes an instrument

to an Instrument	specific routine to take a load list and prepare it for sending (downloading) to the instrument.

i.Fast Bypass Data Entry/Verify;	This option is similar to Bypass normal data entry, except it allows you to accession of several tests on the same patient. After the tests have been accessioned, the option will prompt the user with the accession numbers for the previously accessioned tests.

NOTE	This option is intended to phase out the use of bypass normal data entry option.

Lookup Accession	This function allows the user to find information about a single accession.

**Option	Description**

i.Order/test status;	After selecting a patient, for each day prompted, the status for all tests for that day are given. Each day will be prompted in inverse order. Future dates can be requested. The report will output for a specified patient, Order #, Urgency, Status (test complete, on collection list, testing in progress, collected), Provider, and Accession #.

i.Print a Load/Work List;	Prints a load or work list. You can start printing from any entry and it will reflect revised and new status of specimens.

Std/QC/Repeats manual	Allow the tech to manual update

workload count;	Standards, QC and repeats workload.

Unload Load/Work List	Remove the samples from the Load/Work list so they may be added to another Load/Work list or so a new one can be created.

#### Quality Control Menu [LRQCM]

This menu contains options for maintaining quality assurance.

Add/edit QC name &amp;/or edit test means [LRQCADDNAME]

**&gt; Locked with LRSUPER

Bull algorithm quality control [LRQCC]

Edit control placement on load/work list [LRLL CONTROLS]

**&gt; Locked with LRSUPER

Edit controls added to the accessions each day [LR ACC CONTROLS]

**&gt; Locked with LRSUPER

Manually accession QC, Environmental, etc. [LRQCLOG]

Quality control display (Levey-Jennings) [LRQC]

##### Quality Control Menu Option Descriptions

**Option	Description**

Add/edit QC name &amp;/or	Quality control names can be added or

edit test means	edited. Tests for listing on worklists may be edited. Tests can be individually listed for entering the expected mean and standard deviations. New control lots should have new name entries in this file.

Bull algorithm quality control	Displays cumulative data from the Bull algorithm. This Hematology Quality Control option allows the Hematology Supervisor to monitor the MCH, MCV, and MCHC hematology indices. These indices are grouped in “sets” of 20 values, from which the mean and delta values are calculated. It has been reported that these three indices do not vary except in extreme disease states. Hence, the indices are an indication of the stability and precision of the automated hematology instrument. Before using this option, the original article by Dr. Brian Bull should be studied. Refer to standard quality control manuals.

**Option	Description**

Edit control placement	This option allows the user to specify

on load/work list	where on the load/work list controls are to be placed and what tests are to be performed.

Edit controls added to the	This option allows the user to specify

accessions each day	what accessions are to have what tests. These are placed in the system at the beginning of each day. Be aware that the accession will not be added if the number to be assigned is already in use performed.

.;

Manually accession QC,	This option allows you access to various

environmental, etc.	files other than the Patient file (i.e., Referral, Research, Sterilizer, and Environmental) to accession Quality Control and other non-patient specimens and proficiency testing samples.

These files may also be accessed via regular accessioning options (multipurpose, etc.) by use of “extended syntax” at the “Select Patient name:” prompt enter the file name (or enough letters to define the unique name) followed by a colon and then the name of the desired entry. Example: “Select Patient name: S: LAB AUTOCLAVE.”

**Option	Description**

Quality control display	Quality control data are displayed

(Levey-Jennings)	against the normal mean and standard deviation entered for the requested test (in the Test field of the Lab Control Name file). The option uses a modified Levey-Jennings format to allow a printout on the VA printers. This format is vertical and the time scale is sequential and not proportional. The report will list all dates, control values, total # of controls (N), target range, actual range obtained, and will flag any values outside of 3SD. The control values outside of 3SD are not used in the calculation of the actual range obtained. The report also has a line where the responsible laboratory official may review the output of the report (CAP Requirement). The “mean” is denoted by the ***** line, 1SD &amp; 3SD are denoted by the ..... lines, and 2SD is denoted by the ::::: lines.

#### Results Menu [LR OUT]

This menu contains options that the lab uses to report or send out patient test results.

Edit/print/display preselected lab tests **...**

PR   Print/display preselected lab tests

EN   Enter/edit user defined lab test lists

General report for selected tests

Graph results

Interim report

Interim report by provider

Interim report for selected tests as ordered

Interim report for selected tests

Interim reports by location (manual queue)

Interim reports for 1 location (manual queue)

Interim reports for 1 provider (manual queue)

Order/test status

Print a full patient summary

Review by order number

##### Results Menu Option Descriptions

**Option	Description**

Edit/print/display preselected	User defined lab tests and patient

lab tests	lists for display/print from one date to another.

Enter/edit user defined lab test lists	Allows a user to define lab test panels to print/display. Each panel can have up to seven tests each. The tests must be chem, hem, ser, tox, coag, RIA, or ones for a urinalysis.

Print/display preselected lab tests	This option prints/displays preselected lab tests selected by the lab or the user. If no user selection, the default is lab selection. Users can keep their own lists of patients to print that can be edited upon entering the option. Physicians who want a quick list of preselected lab tests for his patients from one date to another and is not intended for chart copy can use this option.

General Report for Selected Tests	This function displays data in a highly generalized fashion. All tests requested are displayed up to 18 fields in a cumulative format. If more than 18 tests are to be displayed, an alternate format is used. If a test has a special format (predefined in the LABORATORY TEST file (#60)) then that test must be requested separately. If a specimen is specified, normal ranges are displayed if available.

NOTE	If a specimen is chosen for which there is no data, no data will be displayed.

**Option	Description**

Graph Results 	This option plots data in a highly generalized fashion. If a specimen is specified, normal ranges are displayed if available. One may also, choose to plot the data centered about the normal range or centered about the mean of the data being plotted. If the selected plot is according to ranges, then any values that differ from the mean of the normal ranges by more than three standard deviations are plotted in the extreme left or right column of the display, as the case may be. In addition to being plotted in the extreme left or right column, the value is distinguished by a “*” rather than a “X”.

Interim Report	This option will print or display interim reports for a selected patient, within a given time period. The printout will go in reverse date order. This report will printout all tests for the time period specified. If no results are available, the option will ask for another patient. This option will only print verified results.

Interim Report by Provider	This option is used to obtain all data on one day for selected physicians. All physicians can be selected or a range of physicians (this may be helpful if obtaining reports for all physicians but you wish to split the load between multiple printers). Multiple selections are allowed for selecting specific physicians. All reports are sorted by Provider name. If no results are available for a Provider, the option will print the physician’s name followed by the next physician’s name. This option is an alternative to having the Interim report tasked to the TaskManager. Only verified results will be printed.

**Option	Description**

Graph Results	This option is not part of the cumulative

(Continued)	report and the reports should not be charted. The date chosen for this report is the collection date.

If a test is ordered on one day and verified on the next, you have to select the order date to see the report.

Interim report for selected	Detailed report format for an

tests as ordered	individual patient. Report is done for selected tests as they are ordered. If the orders have been purged, the results will not be found because the result look-up is dependent on the orders. This option allows the user to select a specific test or panel, or select the “ANY” test default that will output all the verified tests for that patient during the period specified. If no results are available, the option will ask for another patient. This option will only print verified results and should be used for information only. The printout should not be charted.

Interim report for selected tests	This report will display results in inverse date order. The option allows the user to select a specific test or panel of tests for a specified period. Regardless of whether the orders have been purged, the results will be displayed. The report should not be charted.

**Option	Description**

Interim reports by location	Detailed report format for all data for

(manual queue)	one day sorted by location. If no results are available for a location, the option will print out the location heading followed by the next location heading. This option will only print verified results, and is not part of the cumulative report. The printout should not be charted. The date chosen for this report is the collection date. If a test is ordered on one day and verified on the next day, you must select the order date to see the report with this option.

Interim reports for 1 location	This option reports all verified results

(manual queue)	from one location for one day. The user will request the date and location. This option will only print verified results. This option is to be used for information only and the report should not be charted.

Interim reports for 1 provider	This option reports all verified results

(manual queue)	for one day for one Provider. (The user will request the date and Provider. This option will only print verified results.) The date requested should be the date the lab work was collected. This option is to be used for information only and the report should not be charted.

Order/test status	After selecting a patient, the status for all tests for that day is given. Each day will be prompted in inverse order. Future dates can be requested. The report will output for a specified patient, Order #, Urgency, Status (test complete, on collection list, testing in progress, collected), Provider, and Accession #.

**Option	Description**

Print a full patient summary	Prints a full patient summary using the format of the standard daily cumulative. This printout is not designed to replace any part of the patient cumulative. It simply captures **all** lab data on a patient and reports it in the same format as the cumulative. This report should be queued for after-hours since it can be lengthy.

Review by order number	Essential information related to the order can be displayed with this function if the order number is known.

#### Information-Help Menu [LRHELP]

This menu contains options that the lab uses to obtain additional “help” or information about tests, orders, make inquiries, etc.

General report for selected tests [LRGEN]

Inquiry to LAB TEST file [LRTESTDIQ]

**&gt; Locked with LRSUPER

Interim report for selected tests as ordered [LRRSP]

Order/test status [LROS]

Review by order number [LRCENLKUP]

Test description information [LREV]

##### Information-Help Menu Option Descriptions

**Option	Description**

General report for selected tests	This function displays data in a highly generalized fashion. All tests requested are displayed (up to 18 fields) in a cumulative format. If more than 18 tests are to be displayed, an alternate format is used. If a test has a special format (predefined in the LABORATORY TEST file (#60)) then the test must be requested separately. If a specimen is specified, normal ranges are displayed if available.

NOTE	If a specimen is chosen for which there is no data, no data will be displayed.

Inquiry to LAB TEST file	This function displays information from the LABORATORY TEST file (#60). All defined fields that are associated with the requested test in File #60 are displayed. If information is missing on a particular test, the desired information must be first added to File #60. This option is just a “lookup” option to allow the user to inquire about how a test is defined in the LABORATORY TEST file (#60).

**Option	Description**

Interim report for selected	Detailed report format for an

tests as ordered	individual patient. Report is done for selected tests as they are ordered. If the orders have been purged, the results will not be found because the result look-up is dependent on the orders. This option allows the user to select a specific test or panel, or select the “ANY” test default that will output all the verified tests for that patient during the period specified. If no results are available, the option will ask for another patient. This option will only print verified results and should be used for information only. The report should not be charted.

Order/test status	After selecting a patient, the status for all tests for that day is given. Each day will be prompted in inverse order. Future dates can be requested. The report will output for a specified patient, Order #, Urgency, Status (test complete, on collection list, testing in progress, collected), Provider, and Accession #.

Review by order number	Essential information related to the order can be displayed with this function if the order number is known.

Test description information	This function displays limited information from the LABORATORY TEST file (#60), such as special ordering information, normal ranges, etc.

#### Ward Lab Menu [LRWARDM]

This menu contains the standard options that can be assigned to ward personnel.

PA     Interim report  [LRRP2]

Interim report for selected tests as ordered [LRRSP]

Add tests to an already existing order number. [LRADD TO

ORDER]

Delete entire order or individual tests [LRCENDEL]

Fast lab test order (IMMEDIATE COLLECT) [LROW IMMED COLLECT]

Fast lab test order (ROUTINE) [LROW ROUTINE]

Fast lab test order (SEND PATIENT) [LROW SEND PAT]

Fast lab test order (WARD COLLECT) [LROW WARD COL]

General report for selected tests [LRGEN]

Graph results [LRDIST]

Interim report by provider [LRRD]

Interim report for selected tests [LRRP3]

Interim reports for 1 location (manual queue) [LRRS BY LOC]

Lab test order [LROW]

List of lab orders not collected [LRNODRAW]

Order/test status [LROS]

Reprint a Ward Collect Order [LROWRP]

Review by order number [LRCENLKUP]

Show list of accessions for a patient [LRUPT]

Test description information [LREV]

Ward collection summary for lab orders [LRDRAW]

##### Ward Lab Menu Option Descriptions

**Option	Description**

Interim report	This option will print or display interim reports for a selected patient, within a given time period. The printout will go inverse date order. This report will output all tests for the period specified. If no results are available, the option will ask for another patient. This option will only print verified results.

Interim report for selected tests	Detailed report format for an

as ordered	individual patient. Report is done for selected tests as they are ordered. If the orders have been purged, the results will not be found because the result look up is dependent on the orders. This option allows the user to select a specific test or panel, or select the “ANY” test default that will output all the verified tests for that patient during the period specified. If no results are available, the option will ask for another patient. This option will only print verified results and should be used for information only. The option should not be charted.

Add tests to an already	This function allows tests to be ordered

existing order number	on an already existing order number. If any of the tests are already accessioned, this function cannot be used to add any additional tests; the function Add Tests to an Existing Accession in the lab must be used.

Delete entire order or	This option may be used to remove an

individual tests	entire order. The reason for deleting the order must be entered. If results have already been entered and verified for any part of the order, the order cannot be deleted.

NOTE:	If a panel component is being deleted and other components of that panel remain on the order, an electronic signature will not be required for cancel reasons which otherwise require an electronic signature.  Electronic signature is only required when the entire ordered test is deleted.

**Option	Description**

Fast lab test order	This option is used by the wards to

(IMMEDIATE COLLECT)	request immediate collection of a test specimen by the laboratory. This option is similar to the Fast Lab Test Order (ROUTINE) except that these orders or not for scheduled laboratory collection times. These orders are placed for irregular collection times. The laboratory has set certain periods and days of the week when this will allow the user to select from.

NOTE	If the requested times are not allowed, the user must make a *phone call* to the lab to arrange for specimen collection.

It is recommended that the ordering person always call the laboratory to confirm the receipt of the placed order.

Fast lab test order (ROUTINE)	Tests for routine collection on the ward by the lab may be entered with this option before the creation of a collection list.

Fast lab test order	Same as multipurpose accessioning

(SEND PATIENT)	dialogue, only no labels are made, no accessions are created, and only appropriate for “SEND PATIENT” type of orders. The order number generated is used in conjunction with the function Accessioning Tests from Ward Order Entry to generate the labels and indicate the specimen is in the lab.

**Option	Description**

Fast lab test order	Same as multipurpose accessioning

(WARD COLLECT)	dialogue, only no labels are made, no accessions are created, and is only appropriate for “WARD COLLECT AND DELIVER” type of orders. The order number generated is used in conjunction with the function, Accessioning Tests from Ward Order Entry, to generate the labels indicating the specimen is in the lab.

General report for selected tests	This function displays data in a highly generalized fashion. All tests requested are displayed (up to 18 fields) in a cumulative format. If more than 18 tests are to be displayed, an alternate format is used. If a test has a special format (predefined in the LABORATORY TEST file (#60)) then that test must be requested separately. If a specimen is specified, normal ranges are displayed if available. Note that if a specimen is chosen for which there is no data, no data will be displayed.

Graph results	This function plots data in a highly generalized fashion. If a specimen is specified, normal ranges are displayed if available. Furthermore, one may choose to plot the data centered about the normal range or centered about the mean of the data being plotted. If the selected plot is according to normal ranges, then any values that differ from the mean of the normal ranges by more than three standard deviations are plotted in the extreme left or right column of the display, as the case may be. In addition to being plotted in the extreme left or right column, the value is distinguished by a “*” rather than a “X”.

**Option	Description**

Interim report by provider	This option is used to obtain all data on one day for selected provider. All providers can be selected or a range of providers (this may be helpful if obtaining reports for all providers but you wish to split the load between multiple printers). Multiple selections are allowed for selecting specific providers. All reports are sorted by provider name. If no results are available for a provider, the option will print the provider’s name followed by the next provider’s name. This option is an alternative to having the Interim report tasked to the TaskManager. Only verified results will be printed.

This option is not part of the cumulative report and the reports should not be charted. The date chosen for this report is the collection date. If a test is ordered on one day and verified on the next, you have to select the order date to see the report.

Interim report for selected tests	Detailed report format for an individual patient. Report is done for selected tests as they are ordered. If the orders have been purged, the results will not be found because the result look-up is dependent on the orders. This option allows the user to select a specific test or panel, or select the “ANY” test default which will output all the verified tests for that patient during the period specified. If no results are available, the option will ask for another patient. This option will only print verified results and should be used for information only. The option should not be charted.

**Option	Description**

Interim reports for 1 location	This option reports all verified

(manual queue)	results from one location for one day. The user will request the date and location. This option will only print verified results. This option is to be used for information only and the report should not be charted.

Lab test order	This is to be used by the wards for order entry, **not** by the lab! The two purposes of this function are:

- to allow selection between sending the patient or specimen with the order number to the lab where it can be accessioned
    - or holding the test request in the computer until a collection list can be made and routine phlebotomy collection by the laboratory on the wards occurs.
**Option	Description**
List of lab orders not collected	This option lists orders that have not been collected.
Order/test status	After selecting a patient, the status for all tests for that day is given. Each day will be prompted in inverse order. Future dates can be requested. The report will output for a specified patient, Order #, Urgency, Status (test complete, on collection list, testing in progress, collected), Provider, and Accession #.
Reprint a Ward Collect Order	This option allows the user to reprint a lab order for ward collect. You must know the patient’s name, date of order, and order number to use this option.
Review by order number	, essential information related to the order can be displayed with this function if the order number is known.
Show list of accessions for	This option allows you to find all the
a patient 	accession 	numbers (in one accession area) for one patient. All lab tests associated with each number are also displayed. The information is displayed on the screen only. You cannot print the list with this option.
Test description information	This function displays limited information from the LABORATORY TEST file (#60), such as special ordering information, normal ranges, etc.
Ward collection summary for	A summary of ward orders not yet
lab orders	accessioned. This function may be appropriate for the wards to use to determine their quality assurance of chart transcription to lab orders.

#### Anatomic Pathology [LRAP]

The anatomic pathology portion of the laboratory core package contains the following sections:

- Surgical pathology (SP),
- Cytopathology (CY),
- Electron microscopy (EM)
- Autopsy pathology (AU)

Within each section are options for log-in (LG), data entry (DA), print (P) and searches (S).

See the Anatomic Pathology User Manual for detailed descriptions of the options and functionality of this module.

D      Data entry, anat path ... [LRAPD]

E      Edit/modify data, anat path ... [LRAPE]

I      Inquiries, anat path ... [LRAPI]

L      Log-in menu, anat path ... [LRAPL]

**&gt; Locked with LRANAT

P      Print, anat path ... [LRAPP]

R      SNOMED field references ... [LRAPREF]

S      Supervisor, anat path ... [LRAPSUPER]

**&gt; Locked with LRAPSUPER

V      Verify/release menu, anat path ... [LRAPVR]

C      Clinician options, anat path ... [LRAPMD]

W      Workload, anat path ... [LRAPW]

#### Blood Bank LRBL]

See the Blood Bank User manual for complete descriptions of the module’s, functionality, and options.

D      Donor ... [LRBLD]

I      Inventory ... [LRBLI]

P      Blood bank patient ... [LRBLP]

Q      Inquiries ... [LRBLQ]

R      Reports ... [LRBLR]

S      Supervisor ... [LRBLS]

**&gt; Locked with LRBLSUPER

W      Ward ... [LRBLW]

#### Microbiology Menu [LRMI]

This menu contains the options routinely assigned to Microbiologists.

MIME         Edit Inactive DT Multiple - ETIOLOGY File

MISE          Edit Inactive DT Single - ETIOLOGY File

RB     Results entry (batch) [LRMISTUF]

RE     Results entry [LRMIEDZ]

VS     Verification of data by supervisor [LRMIVER]

**&gt; Locked with LRSUPER

VT     Verification of data by tech [LRMINEWD]

WKLD   Review Accession Workload [LR WKLD AUDIT]

Accessioning, standard (Microbiology) [LRMICROLOGIN]

Batch accessioning [LRMIBL]

Lab statistics menu ... [LR WKLD]

Long form accession list for microbiology [LRMIACC1]

Microbiology print menu ... [LRMIP]

References ... [LRMIREF]

Results menu ... [LR OUT]

Short accession list [LRACC2]

Show list of accessions for a patient [LRUPT]

STD/QC/REPS/MANUAL WKLD COUNT [LR WKLD STD/QC/REPS]

Supervisor menu ... [LRSUPERVISOR]

**&gt; Locked with LRSUPER

##### Microbiology Menu Option Descriptions

**Option	Description**

Edit Inactive DT Multiple - ETIOLOGY File	This option allows those users with the LRSUPER key to ‘walk’ the ETIOLOGY FIELD File (#61.2) and enter an Inactive Date for those entries that should be Inactive. The user will have the ability to select an Identifier Name or ALL for Identifier Names. The option will start with the oldest entry (beginning) associated to the Identifier Name selected and allow the user to enter an Inactive Date for the entry displayed if that entry is inactive.

Edit Inactive DT Single - ETIOLOGY File	This option allows those users with the LRSUPER key to Add, Edit, or delete the INACTIVE DATE for entries in the ETIOLOGY FIELD File (#61.2).

Results entry (batch)	Results entry (batch) allows you to enter either preliminary or final data for one field and test for multiple accession numbers in one session. The field choices are Bacteriology, Mycology, TB, Virology, Mycobacteriology, Parasite Report Remark, Gram Stain, Urine Screen, Sputum Screen, Parasitology Smear/Prep, Mycology Smear/Prep, and Acid Fast Stain. These choices are dependent on the microbiology test selected and specified on the test’s edit code. There are three levels of automation to choose from:

1. result is entered and you are not allowed to change it,
2. result is entered and you are allowed to change it,
3. no result is entered for you. You must have the LRVERIFY security key to use this option.

**Option	Description**

Results entry	Allows input of microbiology test results by accession number. A test or procedure may be selected in order to limit data entry to only that procedure. Input prompts are dependent on the procedure and organisms being reported. A date must be entered to complete the “FINAL” designation of the result.

Verification of data by supervisor	This option allows supervisors to create a list of accessions to be verified. The supervisor may choose a previously used list or choose a new list within a chosen date range. The list can be printed and reviewed before verification. The supervisor can exclude accessions from the list and then verify the remainder.

Verification of data by tech	Allows lab techs to check and approve their own result entries or supervisors to approve lab techs’ result entries (LRSUPER key is required to verify data entry by others). The lab tech or supervisor must choose a field to edit, and then those accessions that have been edited will be displayed. The lab tech or supervisor can exclude specific accessions from review, they can review the data as the wards or lab will see it, and they can exclude accessions from verification. The approved results can also be sent to a device near the requesting location.

Review accession workload	This option allows one to review what workload has been completed for a given accession.

Accessioning, standard	This option allows you to accession

(Microbiology)	requested tests. It is especially useful for accessioning unusual specimens, or accessioning specimens that require a descriptive comment. You may also comment about the order. When you are asked to select the label printer, if you enter “^”, labels will not be printed.

**Option	Description**

You will then be asked to select a label printer with each new patient you select. When you select a printer, that printer will be used until you end that session.

Batch Accessioning	You may use this option to accession any patient specimen for any test/procedure ordered. However, you are limited to ordering only one test per specimen. Use this option to accession a large number of identical types of specimens with the same test ordered. Once you enter the site /specimen and test name, you will not be asked for that information again. It is automatically assigned to each patient until you exit the option. It is a very quick, simple and efficient method for accessioning specimens into the laboratory.

Lab Statistics Menu....	This menu contains the WKLD statistics reports. For a complete description of the options, please refer the Process data in lab menu section in this manual for the Lab statistics menu.

Long form accession list	Same as Long form accession list, except

for microbiology	it only displays the accession areas associated with microbiology (MI-subscripted. The list produces a complete listing of accessions for a range of dates or a range of accession numbers. The user can opt to print only a specific test and/or only incomplete entries. The status of each test for an accession is also given. The long accession list can effectively replace logbooks in microbiology, and provide a list of incomplete cultures for review.

**Option	Description**

Microbiology Print Menu....	This menu contains all of the Microbiology print options.

All results for selected accessions	Prints all available results for selected accession numbers in microbiology.

i.Cumulative patient report;	Provides a comprehensive report of all microbiology tests, results, and status of tests for a specified patient for a specified date range. This option is only for a single patient.

Health Department report	Presents a report for a range of days of all isolates (with patient name, address, etc.) for all organisms (fungus, AFB, parasite, etc.) that are reportable to the State Health Department.

Infection control survey report	The Infection Control report is used by the Laboratory and Infection Control unit to look for increases in the number of a particular organism or the emergence and spread of a resistant organism. The report contains patient information, specimen or collection sample, and all isolates regardless of whether or not they have a sensitivity. For a particular accession area and within a specified time range, 4 separate reports can be obtained. Information can be grouped by:

1. location,
2. organism,
3. physician, and
4. patient.

A hospital can preselect the reports, or reports may be selected individually. Each report can include all information or be restricted to a single location, patient, etc. All reports can be restricted to a single organism. The collection sample or site/specimen sorts a survey by organism. All reports can be restricted to include only those patients with a length of stay in the hospital exceeding a specified # of days. This can be helpful in tracking hospital-acquired infections. The reports can also be restricted to include only those that have specific antibiotic patterns.

Long form accession list	Detailed list of accessions by accession area. The list produces a complete listing of accessions over a specified period. The user can opt to print only specified tests and/or only uncompleted entries. The status of each test for an accession is also given. Microbiology has its own “Long Form Accession” list (LRMIACC1). The Long Form Accession list can effectively replace log books, provide a list of uncompleted test(s) for an accession area, and be used at the end of the shift and work day to monitor what is left on the list. Use the Remove an Accession [LRDELOG] option to remove an unwanted accession so that the rollover option, if activated, will work as desired.

Microbiology Trend Report	**&gt; Extended help available. Type “?Microbiology” to see it. The Microbiology Trend Report [LRMITS] option is enhanced to sort the ‘Antimicrobial Trend Report’ by DIVISION. This report is used to compare counts of organisms and patterns of antibiotic susceptibility. Different types of ‘Antimicrobial Trend Report’ by division can be generated. The Microbiology Trend Report [LRMITS] option is located on the Laboratory DHCP Menu [LRMENU] (locked with LRLAB security key), Microbiology menu [LRMI] (locked with LRMICRO security key), Microbiology print menu [LRMIP] option.

Patient report	Provides a comprehensive report of microbiology data by selecting either patient or accession. If results are looked up by patient, the report will show all microbiology tests ordered on the specified patient, verified result of those tests, and the status of each test. The results may also be looked up by the accession number.

Short accession list	An abbreviated list of accessions. You may combine more than one accession area on the list that may serve as a very abbreviated worklist.

**Option	Description**

References....	This menu contains the Microbiology reference options.

Inquire to micro journal references	Use this option to search journals for articles on a specified etiologic agent.

Enter/Edit medical journal	This option allows entry and editing of

references;	the MEDICAL JOURNAL REFERENCE file.

Enter/Edit micro journal references	This option allows editing and entry of journal references to the MICRO file.

Results menu....	This menu contains the Lab results options. For a completed description of the options please refer to the Results menu section in this manual.

Short accession List	A condense list of accessions. You may combine more than one accession area on the list which may serve as a very abbreviated worklist.

Show list of accessions for a patient	If you need to find all the accession numbers (in one accession area) for one patient, you may do so with this option. The information is displayed on the screen only. You cannot print the list with this option.

Std/QC/Reps manual workload count	Allow the tech to manually update Standards, QC and repeated workload.

Supervisor Menu....	This menu contains the laboratory Supervisor options. For a complete description of the options, please refer to the Supervisor menu section in this manual.

#### Supervisor Menu [LRSUPERVISOR]

This menu contains options used by supervisors to perform specialized functions in the lab.

Add/edit QC name &amp;/or edit test means [LRQCADDNAME]

**&gt; Locked with LRSUPER

Change Load/Work list type. [LRLL TYPE]

**&gt; Locked with LRLIASON

Changes in verified lab data [LRUER]

Cumulative menu ... [LRAC]

**&gt; Locked with LRSUPER

Cumulative device status [LRAC STATUS]

Diagnostic routine for Lab Reports file (64.5) [LRAC DIAG]

**&gt; Locked with LRLIASON

Force cumulative data to Permanent Page [LRAC FORCE]

**&gt; Locked with LRSUPER

Initialize LAC global &amp; X references [LRAC INITIALIZE]

**&gt; Locked with LRLIASON

List of patients by location for cumulative report [LRAC LIST]

Manual queuing of cumulative [LRAC MANUAL]

Manual queuing of Fileroom Cum [LRAC MANUAL FILRROOM CUM]

Patient Lab Discharge Summary (Manual) [LRAC DISCHARGE]

Print a full patient summary [LRAC FULL PATIENT SUMMARY]

Purge the Cumulative file [LRAC PURGE]

**&gt; Locked with LRSUPER

Re-cross-reference indexes in LAB REPORTS file ... [LRAC XREF]

**&gt; Locked with LRLIASON

1      Mumps A index of the LAB REPORTS file [LRAC A]

2      Mumps AC index of the LAB REPORTS file [LRAC AC]

3      Mumps AR index of the LAB REPORTS file []

4      Mumps A, AC, &amp; AR indexes of the LAB REPORTS file

[LRAC A AC AR]

Reprint a permanent page from cumulative [LRAC 1 PAGE]

Reprint cumulative from location to location [LRAC LOC-LOC]

Reprint cumulative on a given patient [LRAC PT]

Reprint cumulative on a given location [LRAC LOC]

Documentation for lab options [LROPT]

**&gt; Locked with LRLIASON

Edit atomic tests [LRDIEATOMIC]

**&gt; Locked with LRSUPER

Edit control placement on load/work list [LRLL CONTROLS]

**&gt; Locked with LRSUPER

Edit controls added to the accessions each day [LR ACC CONTROLS]

**&gt; Locked with LRSUPER

Edit cosmic tests [LRDIECOSMIC]

**&gt; Locked with LRSUPER

Edit the default parameters Load/Work list. [LRLLE DFT]

**&gt; Locked with LRLIASON

Edit the Load/Work list profile [LRLLE PRO]

**&gt; Locked with LRLIASON

Infection warning edit [LR INF WARN]

**&gt; Locked with LRSUPER

Inquiry to LAB TEST file [LRTESTDIQ]

**&gt; Locked with LRSUPER

Lab interface menu ... [LA INTERFACE]

Change instrument run mode. [LA LRLL/AC SWITCH]

**&gt; Locked with LRVERIFY

Check the lab interface [LA 1103]

Clear instrument/worklist data [LRINSTCLR]

**&gt; Locked with LRVERIFY

Direct Connect Auto-Instrument  Start [LA DIR JOB]

Lab Error Trap Listing [LA ERR PRINT]

Restart processing of instrument data [LA JOB]

**&gt; Locked with LRVERIFY

Set instrument to run by Accession [LA AUTO ACC]

**&gt; Locked with LRSUPER

Set instrument to run by load list [LA AUTO LLIST]

**&gt; Locked with LRSUPER

Test the interface  [LA LAB TEST]

**&gt; Locked with LRLIASON

Watch the data in the LA global. [LA WATCH]

**&gt; Locked with LRVERIFY

Lab liaison menu ... [LRLIAISON]

**&gt; Locked with LRLIASON

ANT    Add a new internal name for an antibiotic [LRWU7]

**&gt; Locked with LRLIASON

DATA   Add a new data name [LRWU5]

**&gt; Locked with LRLIASON

MOD    Modify an existing data name [LRWU6]

**&gt; Locked with LRLIASON

Add a new WKLD code to file [LRCAP CODE ADD]

**&gt; Locked with LRLIASON

AP Microfiche Archive [LA AP FICHE]

Archive lab data ... [LR ARCHIVE MENU]

**&gt; Locked with LRLIASON

1     Search for lab data to archive [LR ARCHIVE SEARCH]

**&gt; Locked with LRLIASON

2     Write data to off-line media [LR ARCHIVE WRITE MEDIA]

3     Clear data from the LAR global [LR ARCHIVE CLEAR]

**&gt; Locked with LRLIASON

4     Read data from off-line media [LR ARCHIVE READ MEDIA]

5     Purge data found in the Search option [LR ARCHIVE PURGE]

**&gt; Locked with LRLIASON

6     Find patient's archived data [LR ARCHIVE DATA]

7     Convert archived data to use New Person file

[LR ARCHIVE NP CONVERSION]

8     Restore archived data to LR global

[LR ARCHIVE RESTORE]

Check files for inconsistencies [LRCHKFILES]

**&gt; Locked with LRLIASON

Check patient and lab data cross pointers [LRCKPTR]

**&gt; Locked with LRLIASON

Download Format for Intermec Printer [LR BARCODE FORMAT LOAD]

Edit atomic tests [LRDIEATOMIC]

**&gt; Locked with LRSUPER

Edit cosmic tests [LRDIECOSMIC]

**&gt; Locked with LRSUPER

File list for lab [LRUCONTENTS]

LAB ROUTINE INTEGRITY MENU ... [LR INTEGRITY]

LD     Load Integrity File [LR INTEGRITY LOAD]

LP     Loop thru LR INTEGRITY [LR INTEGRITY ]

Check a single routine size [LR INTEGRITY SINGLE]

LIM WORKLOAD MENU ... [LR LIM/WKLD MENU]

Detail Workload Report [LRRP6]

Etiology WKLD Codes (Force) [LRCAPF]

**&gt; Locked with LRSUPER

File 81 conversion [LRBLPOST]

**&gt; Locked with LRLIASON

PHASE 1: Move data from 64.1 to 67.9. [LR WKLD LMIP 1]

**&gt; Locked with LRSUPER

PHASE 2: Collect data for transmit to NDB.

[LR WKLD LMIP 2]

**&gt; Locked with LRSUPER

PHASE 3: Print of data to be sent to NDB.

[LR WKLD LMIP 3]

**&gt; Locked with LRSUPER

PHASE 4: Create E-mail message for NDB. [LR WKLD LMIP 4]

**&gt; Locked with LRSUPER

PHASE 5: Purge monthly WKLD data from 67.9.

[LR WKLD LMIP 5]

**&gt; Locked with LRLIASON

RCS-CDR/LMIP REPORT [LRCAPAM5]

Recompile Phase 1 LMIP Data. [LR WKLD LMIP 1 REPEAT]

**&gt; Locked with LRSUPER

SUPERVISOR WORKLOAD MENU ... [LR SUPER/WKLD MENU]

Detail Workload Report [LRRP6]

Lab orders by collection type [LRRP5]

Lab test turnaround time [LR CAPTT]

RCS-CDR/LMIP REPORT [LRCAPAM5]

Treating Specialty Workload Report [LRCAPTS]

Workload Cost Report by Major Section L]

Workload Report [LRCAPR1]

Workload Statistics by Accession Area and Shift

[LRRP8]   **&gt; Locked with LRSUPER

Workload Statistics by Major Section [LRCAPMA]

Treating Speciality Workload Report [LRCAPTS]

WORKLOAD Code list [LRCAPD]

Workload Cost Report by Major Section [LRCAPML]

Workload Report [LRCAPR1]

Workload Statistics by Accession Area and Shift

[LRRP8]     **&gt; Locked with LRSUPER

Workload Statistics by Major Section [LRCAPMA]

Manually compile WKLD and workload counts

[LR WKLD MANUAL]     **&gt; Locked with LRLIASON

OE/RR interface parameters ... [LRXOSX]

EH     Edit HOSPITAL SITE parameters [LRXOSX2]

AS     Edit a lab administration schedule [LRXOSX1]

IL     Inquire to a Lab administration schedule [LRXOSX0]

UP     Update Lab protocols for OE/RR ... [LRX0]

AP     Update ALL lab protocols [LRX1]

SL     Update protocol for a single lab test [LRX2]

LT     Update protocols for all lab tests [LRX3]

GP     Update protocols for all accession groups

[LRX4]

PS     Update protocols for single accession group

[LRX5]

Outline for one or more files [LRUFILE]

Turn on site workload statistics [LR WKLD STATS ON]

**&gt; Locked with LRLIASON

Turn on workload stats for accession area

[LR WKLD  STATS ON ACC AREA]

**&gt; Locked with LRLIASON

User selected lab test/patient list edits ... [LRUMDLM]

1      Enter/edit predefined lab test lists [LRUMDL]

2      Delete user selected lab test/patient lists [LRUMDD]

Lab statistics menu ... [LR WKLD]

Edit Workload Comments [LR WKLD COMMENTS]

File listings ... [LR WKLD3]

**&gt; Locked with LRSUPER

1      WKLD code list by code [LR WKLD CODE BY CODE]

2      WKLD code list by name [LR WKLD CODE BY NAME]

3      Lab section list by code [LR WKLD SECTION BY CODE]

4      Lab section list by name [LR WKLD SECTION BY NAME]

5      Lab subsection list [LR WKLD SUBSECTION]

6      Lab subsection by Lab section [LR WKLD SUB BY SECTION]

7      Service dictionary [LR WKLD SERVICE]

8      Requesting center dictionary [LR WKLD REQUEST]

9      Test dictionary [LR WKLD TEST DICT]

10     WKLD log file download [LRCAPDL]

Lab test turnaround time [LR CAPTT]

LMIP Reports/Data Collection ... [LR WKLD4]

**&gt; Locked with LRLIASON

1      PHASE 1: Move data from 64.1 to 67.9. [LR WKLD LMIP 1]

**&gt; Locked with LRSUPER

2      PHASE 2: Collect data for transmit to NDB. [LR WKLD LMIP 2]

**&gt; Locked with LRSUPER

3      PHASE 3: Print of data to be sent to NDB. [LR WKLD LMIP 3]

**&gt; Locked with LRSUPER

4      PHASE 4: Create E-mail message for NDB. [LR WKLD LMIP 4]

**&gt; Locked with LRSUPER

PHASE 5: Purge monthly WKLD data from 67.9. [LR WKLD LMIP 5]

**&gt; Locked with LRLIASON

Recompile Phase 1 LMIP Data. [LR WKLD LMIP 1 REPEAT]

**&gt; Locked with LRSUPER

Review Accession Workload [LR WKLD AUDIT]

STD/QC/REPS/MANUAL WKLD COUNT [LR WKLD STD/QC/REPS]

Turn on site workload statistics [LR WKLD STATS ON]

**&gt; Locked with LRLIASON

Turn on workload stats for accession area

[LR WKLD STATS ON ACC AREA]

**&gt; Locked with LRLIASON

WKLD statistics reports ... [LR WKLD2]

**&gt; Locked with LRSUPER

1      PHASE 3: Print of data to be sent to NDB. [LR WKLD LMIP 3]

**&gt; Locked with LRSUPER

2      Workload Statistics by Accession Area and Shift [LRRP8]

**&gt; Locked with LRSUPER

3      Workload Cost Report by Major Section [LRCAPML]

4      Detail Workload Report [LRRP6]

5      Treating Specialty Workload Report [LRCAPTS]

6      Workload Report [LRCAPR1]

Workload Manual Input [LR WKLD MANUAL INPUT]

Listing of Laboratory Menus/Options [LROPTLST]

Manually accession QC, Environmental, etc. [LRQCLOG]

Purge old orders &amp; accessions [LROC]

**&gt; Locked with LRSUPER

Set a new starting accession number [LRNEWSTART]

**&gt; Locked with LRSUPER

Supervisor reports ... [LRSUPER REPORTS]

Audit of deleted/edited comments [LRDCOM]

**&gt; Locked with LRLIASON

Changes in verified lab data [LRUER]

Count accessioned tests [LR COUNT ACC TESTS]

**&gt; Locked with LRSUPER

Search for abnormal and critical flagged tests [LRSORD]

Search for critical value flagged tests [LRSORC]

**&gt; Locked with LRSUPER

Search for high/low values of a test [LRSORA]

**&gt; Locked with LRSUPER

Summary list (extended supervisors') [LRLISTE]

**&gt; Locked with LRSUPER

Summary list (supervisors') [LR SUP SUMMARY]

**&gt; Locked with LRSUPER

Supervisor's report [LRACS MANUAL]

**&gt; Locked with LRSUPER

##### Supervisor Menu Option Descriptions

**Option	Description**

Add/edit QC name &amp;/or	Quality control names may be added or

edit test means	edited. Tests for listing on worklists may be edited. Tests may be individually listed for entering the expected mean and standard deviations. New control lots should have new name entries in this file.

Change Load/Work list type	Allows the user to change the load/work list from load list to work list or vice versa.

Changes in verified lab data	Tracking of “CH” subscripted tests with comments containing reported incorrectly as from one date to another.

Cumulative Menu....	Daily cumulative report menu. See Cumulative menu section for a complete description.

Cumulative device status	This option is used to get the status of the cumulative for a particular device. When cumulative is abnormally stopped, this display will give last printed location and patient for all devices used to print cumulative.

.5);

Diagnostic routine for	This option checks the LAB REPORTS

LAB REPORTS file (64.5)	file (#64.5) for erroneous entries and gives fatal and warning messages when problems are found. Problems reported by this option can be fixed by editing the appropriate fields in the LAB REPORTS file (#64.5) or if necessary by the LRAC XREF option (LRAC XREF re-cross references selected indexes).

**Option	Description**

Force cumulative data to	This option will identify patients who

Permanent Page	have been inactive in laboratory for the specified period of time in the Grace Period for Inactivity field of the LABORATORY SITE file (#69.9) and force their lab data onto a permanent cumulative page, making the data eligible

for archiving. Be sure to save the print out generated by this option, since the CUM pages do not print out. The print out is needed to identify the Permanent Page.

Initialize LAC global &amp;	This function is used on the occasion

X references	the hospital is ready to begin actual charting of the daily cumulative. It may be run multiple times to restart the page numbering during the testing phase of implementation. Once actual charting has begun, it should never be run again! While all pages are numbered and dated, the potential for confusion should be obvious. If you have access to this function, you are considered by those who have given you access to be a professional; act accordingly.

List of patients by location for	This function will list patients sorted by

cumulative report	location that are in the queue to get a cumulative for a given day. This option is useful when a reprint of the cumulative is required.

Manual queuing of cumulative	If the cumulative is not being automatically run through the LRTASK CUM option(s), this option may be used to run the cumulative.

**Option	Description**

Manual Queuing of Fileroom Cum	This option is the manual version of the LRTASK CUM FILEROOM option. If you do not wish to schedule automatic printing of the FILEROOM cum via the LRTASK CUM FILEROOM option, you may use this option instead. These options should never be task. There are some questions asked when this option is used. When the proper file setup has been done, this option will allow the printing of the file room cume on a different schedule than inpatient cumes.

Patient Lab Discharge Summary	This option will print a discharge

(Manual)	summary of laboratory results for a single patient for a specific episode of care or time period specified by the user, or multiple patients for episodes of care whose discharge dates fall within the range of dates selected by the user. The report is similar in format to the Full patient summary and the Cumulative report. The only lab results that are printed on the report are those that are ordered during the episode of care selected.

Print a full patient summary	Prints a full patient summary using the format of the standard daily cumulative. This printout is not designed to replace any part of the patient cumulative. It simply captures all lab data on a patient and reports it in the same format as the cumulative.

**Option	Description**

Purge the Cumulative file 	This option should be queued to run during an off peak time and not while the cumulative is running. It will determine which entries can be cleaned out of the cumulative file, using the number of days entered in the Grace Period for the Cumulative field in LABORATORY SITE file (#69.9).

Re-cross-reference indexes in	These options will allow the user to

LAB REPORTS file....	re-cross reference selected indexes from the LAB REPORTS file (#64.5).

Mumps A index of the	This option does a re-cross

LAB REPORTS file	reference on the mumps “A” index on the Lab Test subfield of the LAB REPORTS file (#64.5). The “A” cross reference contains reference ranges, critical ranges, and units from the LABORATORY TEST file (#60).

Mumps AC index of the 	This option does a re-cross

LAB REPORTS file	reference on the mumps “AC” index on the Test Location subfield of the LAB REPORTS file (#64.5). The “AC” cross reference is to identify the tests in the file that have data names (atomic tests) in the LAB DATA file (#63).

Mumps AR index of the	This option does a re-cross

LAB REPORTS file	reference on the mumps “AR” index on the Lab Test subfield of the LAB REPORTS file (#64.5). The “AR” cross reference holds the site/specimen for each test in the file.

Mumps A, AC, &amp; AR indexes of the 	This option does a re-cross

LAB REPORTS file	reference on the “A” and “AR” indexes of  the Lab Test subfield and the “AC” index of the Test Location subfield within the LAB REPORTS file (#64.5). All three indexes are re-cross referenced.

Reprint a permanent page	This option reprints a single permanent

from cumulative	page from a patient's cumulative. The page number must be specified in the same format as it is printed on the cumulative (i.e., X:Y). Device settings and definitions must be the same as when the original page was printed. Because of the difference in global structure of the cumulative file as opposed to the lab data file, residual pages might be printed in addition to the one requested. If this occurs, disregard the additional pages. Refer to technical documentation for information on how to avoid the problem of residual pages.

**Option	Description**

Reprint cumulative from	This is an option to reprint all or part of

location to location	the cumulative. This option should not be used as a substitute for the regular cumulative print [LRTASK CUM, LRAC MANUAL] options. FOR REPRINTS ONLY!

Reprint cumulative on a 	If a single patient’s cumulative needs

given patient	to be reprinted after the full run of the cumulative, use this function. This option can also be used to reprint the entire patient’s cumulative from a specified date. If this is done, the printout would most probably replace the cumulative in the patient’s chart. It may be more appropriate to reprint just a single permanent page from the patient’s cumulative. If this is desired, use [LRAC 1 PAGE] option.

Reprint cumulative on a	If certain pages of a given location’s

given location	cumulative need to be reprinted after the full run of the cumulative, use this function. This option only works for standard locations defined in the HOSPITAL LOCATION file (#44). If you need to print non standard locations or only print selected patients within the location, use the [LRAC LOC-LOC] option.

Documentation for lab options	This option allows you to print all or part of the help frames, if available, for an individual option in a usable reference format. It will also display the description for the selected option.

Edit atomic tests	Edit fields in the LABORATORY TEST file (#60) for tests which are single valued.

**Option	Description**

Edit control placement on	This option allows the user to specify

load/work List	where on the load/work list controls are to be placed and what tests they are to be.

Edit controls added to the	This option allows the user to specify

accessions each day	what accessions are to have what tests. These are placed in the system at the beginning of each day.

NOTE	Be aware that the accession will not be added if the number to be assigned is already in use.

Edit cosmic tests	This option allows you to edit the parameters of test panels without using VA FileMan.

Edit the default parameters 	This function allows the user to edit the

Load/Work List	default parameters of the Load/Work list file so that the preparation of load or work lists can reflect the way the tests are being done on the instrument or at the bench.

Edit the Load/Work list profile	This option allows the user to modify the list of what tests are to be pulled from the accessions and be put on the load or work list. If tests are accessioned to the area associated with the load/work list but are not on the given profile, the tests will not appear on the load/work list. If a specimen is further indicated for a given test on the profile, only tests for the indicated specimen will be put on the load/work list. If no specimen is indicated, any specimen with the indicated test will be placed on the load/work list.

**Option	Description**

Infection warning edit	This option enables the user to edit the infection warning for a patient. The warning appears on all labels printed for this patient.

.Inquiry to LAB TEST file	This function displays information from the LABORATORY TEST file (#60). All defined fields that are associated with the requested test in File #60 are displayed. If information is missing on a particular test, the desired information must be first added to File #60. This option is just a “lookup” option to allow the user to inquire about how a test is defined in the LABORATORY TEST file (#60).

Lab Interface Menu....	A menu of auto instrument options.

Change instrument run mode	Allows the user to change the way the instrument identifies a sample; i.e., by accession, by load list.

Check the lab interface	Determines the status of the lab interface.

Clear instrument/worklist data	This option clears the instrument data from the ^LAH( global. Use the UNLOAD/LOAD LIST options to clear load/work list.

**Option	Description**

Direct Connect Auto-Instrument	This option allows one to view Auto

Start	Instruments that are not connected to the LSI. These instruments are connected directly to the CPU. Use [LRJOB] option to view instruments on the LSI.

NOTE	This only functions properly if the instrument is connected to this CPU, not another. In other words, both the user and the instrument must be operating on the same CPU. Beckman CX5 is a direct connect instrument.

Lab Error Trap Listing	This option is used to list system errors involving the Auto Instruments routines. When an error occurs [LABERR] routines stores the variables in the ^%ZTSK global. The amount of time before these variables are automatically purged is controlled by Field #606 in File #69.9. This option will first present a list of error contained in the errors trap. This serves as an index giving some basic information about the error. A complete listing of the errors list can be obtained by entering “?.” One can then select a specific error for a detailed listing of variables.

**Option	Description**

Lab Error Trap Listing	This option does not allow for the

(Continued)	restoring of variables to the user’s local partition.

NOTE	The “Y” variable is consumed by the ^%ZTLOAD ROUTINES, therefore those variables are stored under LABZY(x). However if you enter “Y” you will be presented with correct “Y(x)” variables even though they are not shown in the complete display function. This option is primarily for programmers or advanced users. This option is generally of little use to the casual user, but this does allow the user to relay information to support persons not on the system.

Restart processing of	If, for some reason, an automated

instrument data	instrument routine is not started automatically by the master Lab program, this option may be used to start it.

Set instrument to run	This function allows the user to set the

by Accession 	selected instrument to be run on the basis of accession numbers. That is, the data transmitted from the automated instrument contains the accession number that allows the host computer to find who or what the data belongs to.

**Option	Description**

Set instrument to run	This function allows the user to set the

by load list	selected instrument to be run on the basis of load list numbers. That is, the data transmitted from the automated instrument contains the load list numbers that allow the host computer to find who or what the data belongs to.

Test the interface	A test mode for the lab interface to show the messages.

Watch the data in the LA global	This option allows you to watch the accumulation of data in the LA global and LAH global. You may also delete all data stored in a global.

Lab Liaison Menu....	This is the menu that only the LAB liaison person should have.

Add a new internal name for	Allows you to add a new internal name

an antibiotic	for an antibiotic.

Add a new data name	This option allows you to add a new data name to File #63.

Modify an existing data name	This option allows you to edit an existing data name.

**Option	Description**

Add a new WKLD code to file	This option allow one create a new WKLD code. The WKLD CODE file (#64) cannot be edited directly. New codes (those requiring suffixes) which are not in the distributed file, can be added with this option. Code are automatically generated for those procedures which are verified. However, if a code needs to be created before verification, use this option. You will be asked for the Procedure first. These choices come from WKLD CODE file (#64). Then you will be asked for the Suffix code, these come from WKLD CODE SUFFIX file (#64.2). If this code already exists, the information will be displayed. If it does not exist the option will create a new entry for you and display the new code data.

NOTE	Once a WKLD code has been created, do not delete it. *Repeat* -- *do not delete.*

AP Microfiche Archive	This option allow one to archive Anatomical Pathology Reports to a Microfiche. The tape drive must be previously defined and made ready before the use of this option. Refer to documentation for specifics.

Archive lab data....	This menu contains the options by which Data from laboratory can be archived or restored with these options.

**Option	Description**

Search for lab data to archive	Data to be archived must be older than the beginning of the month three months ago, on a patient not currently on a ward, and on a permanent page. If the data is before the time specified above it will be purged if unverified. Microbiology, Anatomic Pathology, and Blood Bank data are not archived.

Write data to off-line media	After having created entries in the ^LAR global, the data should be written to off-line media for purposes of long term storage.

Clear data from the LAR global	Data found in the Search archive option is temporarily removed by this option.

Read data from off-line media	After having Cleared the ^LAR global, the data should be read back in to verify and purge what has been archived.

Purge data found in the	Data found in the Search archive

Search option	option is stored in the ^LAR global. Data is removed from the LAB DATA file (#63) (^LR global) based on the data in the ^LAR global. The ^LAR data must be written to separate media, the Clear archive option run, the data read back from the media, then this option may be run to complete the archive.

NOTE	The data is removed from both the ^LR and the ^LAR globals.

**Option	Description**

Find patient’s archived data	Once data for a patient has been archived, the storage location of the data is saved with the patient’s remaining data. This information can be found using this option.

Convert archived data to use	After previously archived data

NEW PERSON file	is restored to the ^LAR global, this option should be run to convert any records that were not converted during the install of Laboratory V. 5.2. Do this before moving the data back into the ^LR global. Records previously converted will be unaffected.

Restore archived data to LR global	Used to restore data into the LR global that has been archived.

Check files for inconsistencies	This option will generate a report of potential inconsistencies in various files.

Check patient and lab data	This routine will look at all patients

cross pointers	 and check that the ab data entry pointed to points back to it. The routine then looks at all entries in the lab data file and checks that the pointed to file points back.

Download Format for	This option is used to down load the

Intermec Printer;	printer format for bar code accession labels. The routine for Intermec printers for the 1X3 format is LRLABAR. If not used for Intermec 1X3 labels, refer to routine LRLABEL6 for specifics.

Edit atomic tests	Edit fields in the LABORATORY TEST file (#60) for tests that are single valued.

**Option	Description**

Edit cosmic tests	This option allows you to edit the parameters of test panels without using FileMan.

File list for lab	Use this option to select from one number to another from a list of files for lab package or any other files.

LAB ROUTINE INTEGRITY	This menu should be assigned to the

MENU....	persons(s) who maintain the L* routines. The menu allows loading of LR ROUTINE INTEGRITY CHECKER file (#69.91) as well checking it contents for consistency.

Load Integrity File	This option is used to load L* routines into LR ROUTINE INTEGRITY CHECKER file (#69.91). This option is sensitive to the version number of the routine located on the second line of each routine. Once a version number has been selected, each routine will be checked for that version number. If the routine begins with a “L” and has the corrected version number, it is entered to the file. Routines size ($L) and total ASCII ($A) for each routine is entered in to the file. Once the file is loaded, any changes to the loaded routine can be detected. This has many uses (e.g., checking patch application or determining routine map size).

Loop thru LR INTEGRITY	This option will you to select a version number, starting routine and a ending routine to be check for integrity. This option uses the LR ROUTINE INTEGRITY CHECKER file (#69.91). After entering your selection the option will loop through the file printing a “.” for every record checked. When a routine fails the integrity checked it is printed out.

Check a single routine size	This option is used to check a routine against data stored in the LR ROUTINE INTEGRITY CHECKER file (#69.91). After the file has been loaded using LR INTEGRITY LOAD option, use of this option will check for integrity of that routine. The size and ASCII value of the selected routine will be compared to the date in the file. A message will then display the value(s) of the selected routine and indicate if the routine has changed. The routine are stored by version numbers.

LIM WORKLOAD MENU....	This menu contains all the workload related options available to the LIM.

Detail workload report	Provides a detailed print of Tests/WKLD codes for a date range.

Etiology WKLD Codes (Force)	This option is used to automatically add WKLD codes into the ETIOLOGY file (#61.2). A sort template must be created using the standard FileMan option. This option will utilize the selected template and then add WKLD codes. This feature can be used to speed up implementation of WLDK module. It also can be used to change existing/added WKLD codes.

File 81 conversion	Converts entries in File #81, Field #66 to File #66.5.

**Option	Description**

.1 to 67.9;

PHASE 1: Move data from 64.1	This option performs the first step in

to 67.9.	producing your monthly report for LMIP and management. This option’s function is to extract from your workload file (#64.1) ^LRO(64.1, which contains your daily workload, and roll up the data in a condensed form. The condensed data is stored in the LAB MONTHLY WORKLOADS file (#67.9) ^LRO(67.9 ). This option should be used two days after the last day of the month you wish to collect data for. Refer to your package documentation for more information.

PHASE 2: Collect data for transmit	This option is the second phase of

to NDB.	LMIP data reporting. In this step, data is condensed further and formatted for transmission to the National Data Base. This formatted message is stored in a temporary global from which a review report will be created for your certification. Care should be taken with who has access to this menu. The Laboratory Information Manager or the Chief Technologist should control this option.

**Option	Description**

PHASE 3: Print of data to be sent	This option produces a printable

to NDB.	report of the data the system has collected for the requested reporting period. This data is in a format, which allow transmission to the National Data center. In order for you to be able to review the compiled data it must be converted to a readable format. This report allows you to have a hard copy of the LMIP data for review. This data cannot be edited. The files which the data is extracted are editable to a limited degree. If this report does not conform to your manual workload tally procedures, a package implementation review may be required. Consult your Package documentation for further information.

PHASE 4: Create E-mail message	This is the last phase of data

for NDB.	collection leading to the creation of a mail message containing LMIP data. This option will take the formatted data from the temporary file and place the data into appropriately formatted mail message. The mail message will be sent only to the user creating the message. The User must forward the message via MailMan options to the National Data location. Consult LMIP directive for the proper forwarding procedures. If for some reason the message creation fails, this option can be ran multiple times.

The National Data center will only accept 1 data message for a single month. Send only one message to the National Data Base. The second one for any month will not be processed. Consult your package documentation for more information.

**Option	Description**

.9;

PHASE 5: Purge monthly WKLD	This option is used to purge

data from 67.9.	LMIP data from the LAB MONTHLY WORKLOADS file (#67.9) after data has been sent to the National database. It can also be used to purge data that is incorrect before building Workload Mail messages. Care should be taken that data is not deleted prematurely. If the site elects to archive this file, this should be done before this option is used to delete data.

RCS-CDR/LMIP REPORT	This option will provide a report based on treating specialty codes. This report is derived from the LAB MONTHLY WORKLOADS file (#67.9).

Recompile Phase 1 LMIP Data	Allows the user to rerun Phase 1 of LMIP data collection. If for some reason, it becomes necessary to recompile the LMIP report this option will delete the data in ^LRO(67.9 for the selected reporting period (Month) and then reset the pointers in ^LRO(64.1 to allow the date to be recompiled again. PHASE 1 LMIP MUST BE RE-RUN AFTER THIS OPTION IS USED.

NOTE	This option should not be used after data has been submitted to the national data center. This option should be used after LMIP data has been reviewed and errors or discrepancies are noted. This option may use large amounts of journal space. Coordinate with IRM before using.

SUPERVISOR WORKLOAD MENU....

Detail workload report	Provides a detailed print of Tests/WKLD codes for a date range.

Lab orders by collection type	Print a report of ordered tests for a collection type (LAB COLLECT, SEND PATIENT or WARD COLLECT) and a date.

Lab test turnaround time	Provides counts of selected tests for a hospital location for a selected time. Test must have date and times for receipt in lab and completion of test to be included in the report. Turnaround time=Lab Arrival Time field (#69.01,20) - Complete Date field (#68.04,4).

RCS-CDR/LMIP REPORT	This option will provide a report based on treating specialty codes. This report is derived from the LAB MONTHLY WORKLOADS file (#67.9).

Treating Specialty Workload	This option will provide a report divided by

Report;	Treating Specialty.

Workload cost report by 	Workload report summed by LAB division,

major section	major section, and lab subsection.

Workload Report	Allows generation of a workload report by numerous combinations of selection criteria, in either a detailed or condensed format.

**Option	Description**

Workload statistics by	This report is a summary of

accession area and shift	workload statistics broken down by work shifts, time ranges, accession areas, WKLD codes, and date ranges. The user is asked for the institution, accession areas, date range, WKLD codes, and a time range or a set of shifts, each with a specific time range. The statistics will show subtotal WKLD code counts for each shift/time range and counts for each WKLD code within a shift. A percentage for each CAP code within a shift subtotal will be calculated. This information will be summarized for each accession area, then an all-inclusive summary will be shown. After the detailed and summary sections, a section on workload data entered manually (Standard, QC, Repeat, and Manual) will print and finally a section on workload comments.

Workload Statistics by	Workload report summed by

Major Section	LAB division, major section, and subsection.

Treating Specialty Workload	This option will provide a report divided by

Report;	Treating Specialty.

WORKLOAD code list	Creates the Workload code list.

Workload Cost Report by 	Workload report summed by LAB division,

Major Section	major section, and lab subsection.

Workload Report	Allows generation of a workload report by numerous combinations of selection criteria, in either a detailed or condensed format.

**Option	Description**

Workload Statistics by	This report is a summary of

Accession Area and Shift	workload statistics broken down by work shifts, time ranges, accession areas, WKLD codes, and date ranges. The user is asked for the institution, accession areas, date range, WKLD codes, and a time range or a set of shifts, each with a specific time range. The statistics will show subtotal WKLD code counts for each shift/time range and counts for each WKLD code within a shift. A percentage for each CAP code within a shift subtotal will be calculated. This information will be summarized for each accession area, then an all-inclusive summary will be shown. After the detailed and summary sections, a section on workload data entered manually (Standard, QC, Repeat, and Manual) will print and finally a section on workload comments.

Workload Statistics by	Workload report summed by

Major Section

Manually compile WKLD	Run this option to manually

and workload counts	compile WKLD and workload counts prior to printing reports for a specific time period, if the LRTASK NIGHTY option did not run for any day during the report period.

OE/RR interface parameters....	This menu contains options that deal with various parameters used in the OE/RR interface.

**Option	Description**

Edit HOSPITAL SITE	This option allows editing the

parameters	HOSPITAL SITE multiple of the LABORATORY SITE file (#69.9). The parameters edited here are used in the OE/RR interface to allow or restrict the use multiple-continuous orders.

Edit a lab administration	This option allows the user to edit a

schedule;	lab schedule in the Administration Schedule used in the OE/RR interface.

Inquire to a Lab administration	This option allows the user to

schedule	inquire to the Administration Schedule file for schedules that apply to Laboratory orders used in the OE/RR interface.

Update Lab protocols	This is a menu of options that update

for OE/RR;	protocols used by OE/RR to be consistent with changes made in Lab files.

Outline for one or more files	Option allows printing of one or more file outlines.

.

Re-index ANTIMICROBIAL	This option is used to re-index a

SUSCEPTIBILITY file (#62.06)	single antibiotic in the ANTIMICROBIAL SUSCEPTIBILITY file (#62.06). This option differs from the FileMan re-index in two ways:

1. This option removes all X-ref entries.
2. It allows the user to select a single antibiotic. When a selection is made, X-Ref of “AI”, “AJ”, and “AS” cleared and redefined.

NOTE	This option may be used when trouble shooting Microbiology results print out of antibiotics.

**Option	Description**

Turn on site workload	This option is used to turn on workload

statistics	compiling features of Version 5.2 (Workload). In order for any workload statistics to be gathered, this field must be turned on (answer “YES”). When this field is turned on, phlebotomy workload data will be tallied (the field is WKLD Stats On, field (#17), in the LABORATORY SITE file (#69.9)).

NOTE There is a secondary switch to turn 
on workload data for each accession area (Workload On field). Both this field and the Workload On field in the ACCESSION file (#68) must be answered “YES”.

Turn on workload stats for	This option turns on workload data

accession area	collection for a specific accession area. If you wish to begin collection workload data for his accession area, answer “YES” to (Workload On field (#10) in the ACCESSION file (#68)).

NOTE	You must also have WKLD Stats field (#17) ON in the LABORATORY SITE file (#69.9) answered “YES”. Both fields must be answered “YES” for data collection to be activated.

User selected lab test/patient	User selected lab tests and patient lists

list edits....	option.

Enter/edit predefined lab test	This is a default list of lab tests in the

Lists	 “CH” subscript for users, especially physicians for their personal patient lists, and is not intended to be for chartable reports.

Delete user selected lab test/patient	Deletes users from lab temporary

lists	print (File #69.2, Field #7) if they have not used option LRUMD since a specified date.

Lab statistics menu....	This is the menu for WKLD statistics reports.

Edit Workload Comments	This option permits the editing of WKLD Workload Comments. This should be used to record special situation or changes in methods of doing or recording workload. You may edit comments for the following:

1. The institution (Lab)
2. The WKLD Code itself
3. Make comments for a specific date(s)

File listings....	 file listings.

WKLD code list by code	This option lists in ascending WKLD code sequence the WKLD code, procedure name, unit weight, and unit for count. You may select a range of WKLD codes to print.

**Option	Description**

WKLD code list by name	This option lists in alphabetical order WKLD code procedures. The procedure name, WKLD code, unit weight, and unit for count is listed. You may select an alphabetical range of names to work with.

Lab section list by code	This option lists by section code every WKLD section on file for your site.

Lab section list by name	This option lists alphabetically every WKLD section on file for your site.

Lab subsection list	This report lists all WKLD (lab) subsections on file for your site.

Lab subsection by Lab section	This report lists the relationship between WKLD (lab) sections and subsections.

Service dictionary	This option lists all services (requesting centers or treating specialties) on file for your site.

Requesting center dictionary	This option lists by abbreviation every requesting center (or treating specialty) on file for your site.

Test dictionary	This report lists all tests and procedures, synonyms, test cost and accession area.

WKLD log file download	This option can be used to download data from the WKLD LOG file (#64.03) to spread sheets. The user is able to select the character used to separate data to match the spreadsheet used. The ‘^’ character is not allowed as a field separator and the character may not be null. The output can be captured in an ASCII file to be later imported into a spreadsheet. Not all sites will make use of the option or this file. The field that controls the collection of the data into the file is located in the LABORATORY SITE file (#69.9) Collect Wkld Log file Data field (#616). To stop data transfer, press the return or enter key.

Lab test turnaround time	Provides counts of selected tests for a hospital location for a selected time. Test must have date and times for receipt in lab and completion of test to be included in the report. Turnaround time=LAB ARRIVAL TIME field (#69.01,20) - COMPLETE DATE field (#68.04,4).

LMIP Reports/Data Collection....	This menu contains option, which perform various functions related to collection and reporting LMIP data. Also there are several related printed reports found in this menu. The Laboratory Information Manager or the Chief Technologist should control this menu. Functions performed by this menu have national impact.

.1 to 67.9;

PHASE 1: Move data from 64.1	This option performs the first step in

to 67.9.	producing your monthly report for LMIP and management. This option’s function is to extract from your workload file (#64.1) ^LRO(64.1, which contains your daily workload, and roll up the data in a condensed form. The condensed data is stored in the LAB MONTHLY WORKLOADS file (#67.9) ^LRO(67.9). This option should be used two days after the last day of the month you wish to collect data for. Refer to your package documentation for more information.

**Option	Description**

PHASE 2: Collect data	This option is the second phase of

for transmit to NDB.	LMIP data reporting. In this step, data is condensed further and formatted for transmission to the National Data Base. This formatted message is stored in a temporary global from which a review report will be created for your certification. Care should be taken with who has access to this menu. The Laboratory Manager or the Chief Technologist should control this option.

PHASE 3: Print of data to be sent	This option produces a printable

to NDB.	report of the data the system has collected for the requested reporting period. This data is in a format, which allow transmission to the National Data center. In order for you to be able to review the compiled data it must be converted to a readable format. This report allows you to have a hard copy of the LMIP data for review. This data cannot be edited. The files which the data is extracted are editable to a limited degree. If this report does not conform to your manual workload tally procedures, a package implementation review may be required. Consult your Package documentation for further information.

Option	Description

PHASE 4: Create E-mail message	This is the last phase of data

for NDB.	collection leading to the creation of a mail message containing LMIP data. This option will take the formatted data from the temporary file and place the data into appropriately formatted mail message. The mail message will be sent only to the user creating the message. The User must forward the message via MailMan options to the National Data location. Consult LMIP directive for the proper forwarding procedures. If for some reason the message creation fails, this option can be run multiple times. The National Data center will only accept one data message for a single month. Send only one E-mail message to the NDB. The second one for any month will not be processed. Consult your package documentation for more information.

PHASE 5: Purge monthly WKLD	This option is used to purge

data from 67.9.	LMIP data from the LAB MONTHLY WORKLOADS file (#67.9) after data has been sent to the National database. It can also be used to purge data that is incorrect before building Workload Mail messages. Care should be taken that data is not deleted prematurely. If the site elects to archive this file, this should be done before this option is used to delete data.

Recompile Phase 1 LMIP Data	Allows the user to rerun Phase 1 of LMIP data collection. If for some reason, it becomes necessary to recompile the LMIP report this option will delete the data in ^LRO(67.9 for the selected reporting period (Month) and then reset the pointers in ^LRO(64.1 to allow the date to be recompiled again. PHASE 1 LMIP MUST BE RE-RUN AFTER THIS OPTION IS USED.

NOTE	This option should not be used after data has been submitted to the . This option should be used after LMIP data has been reviewed and errors or discrepancies are noted. This option may use large amounts of journal space. Coordinate with IRM before using.

**Option	Description**

Review accession workload	This option allows one to review what WKLD workload has been complete for a given accession.

STD/QC/REPS MANUAL 	Allow the tech to manual update

WKLD COUNT;	 Standards, QC, and repeats workload.

Turn on site workload statistics	This option is used to turn on workload compiling features of V. 5.2 (Workload). In order for any workload statistics to be gathered, this field must be turned on (answer “YES”). When this field is turn on phlebotomy workload data will be tallied.

NOTE	There is a secondary switch to turn on workload data for each accession area (). Both this field and the field  in the ACCESSION file (#68) must be answered “YES”.

Turn on workload stats for	This option turns on workload data

accession area	collection for a specific accession area. Answer “YES” if you wish to begin collection workload data for this accession area.

NOTE	You must also have WKLD Stats On field (#17) in the LABORATORY SITE file (#69.9) answered “YES”. Both fields must be answer “YES” for data collection to be activated.

WKLD statistics reports....	This menu contains option associated with workload reports and LMIP workload data.

**Option	Description**

PHASE 3: Print of data to be sent	This option produces a printable

to NDB.	report of the data the system has collected for the requested reporting period. This data is in a format, which allow transmission to the National Data center. In order for you to be able to review the compiled data it must be converted to a readable format. This report allows you to have a hard copy of the LMIP data for review. This data cannot be edited. The files which the data is extracted are editable to a limited degree. If this report does not conform to your manual workload tally procedures, a package implementation review may be required. Consult your Package documentation for further information.

Workload Statistics by	This report is a summary of workload

Accession Area and Shift	statistics broken down by work shifts, time ranges, accession areas, WKLD codes and date ranges. The user is asked for the institution, accession areas, date range, WKLD codes and a time range show subtotal WKLD code counts for each shift/time range and counts for each WKLD code within a shift. A percentage for each CAP code within a shift subtotal will be calculated. This information will be summarized for each accession area, then an all-inclusive summary will be shown. After the detailed and summary sections, a section on workload data entered manually (Standard, QC, Repeat and Manual) will print and finally a section on workload comments.

Workload Cost Report by	Workload report summed by major

Major Section	section and lab subsection.

Detail Workload Report	Provides a detailed print of Tests/WKLD codes for a date range.

.

Treating Specialty Workload 	This report sorts by treating specialty

Report

**Option	Description**

Workload Report	Allows generation of a workload report by numerous combinations of selection criteria, in either a detailed or condensed format.

Workload Manual Input	This option will allow the LIM to update the workload data. This may be necessary after a computer down time or special workload data not captured by the  system.

Listing of Laboratory Menus/Options	This option is used to provide a listing of options for a given menu. This option will print by menu and list all of the options for that menu, including any submenus. This listing can be used as a checklist of options tested. The listing will provide the menu text, option name (Program name if any) and the description of the option from OPTION file (#19). Generally LRMENU option is entered, however any menu can be used. This option is a simplified version of diagram menus. Very helpful when checking off options when testing a new release, or when comparing local menus to distributed versions.

.;

Manually accession QC,	This option allows you to accession

Environmental, etc.	quality control specimens, (lab control names) and specimens from blood donor, specimens for proficiency testing, referral, research, sterilizers, and environmental areas. Quality control specimens may be given accessions with this function. QC specimens may also be accessioned using “extended syntax”; i.e., LAB CONTROL NAME:QC NAME when using other test request functions. Usually, controls are automatically accessioned at the time of the creation of a load or work list.

Purge old orders &amp; accessions	This function allows a manually driven purging of old order and accession data. One must have records in some form accessible to the laboratory to satisfy JCAH and CAP requirements, though these do not have to be on the computer.

**Option	Description**

Set a new starting accession number	Allows resetting the default prompt for any accession area. **Caution** should be used in using this option! Usually used after manual backup procedures have been implemented after computer down time.

.

Supervisor reports....	This is the menu of reports for supervisors. See Supervisor Reports section for a complete description.

Audit of deleted comments	This option provides an audit of all comments that are deleted from “CH” subscripted results. The report may be for a single patient or for all patients. The user enters the time range of the report. The time range corresponds to the collection dates of specimens.

Changes in verified lab data	Tracking of “CH” subscripted tests with comments containing reported incorrectly as from one date to another.

Count accessioned tests	Provides a count of all tests by requesting area and cumulative totals for a given accession area. The report will list the number of accessions and test counts by location and also give a total number of accessions and total test count by accession area. The option has two displays “Counts by location” and “Counts by test.”

Search for abnormal and	Report of abnormal and critical results

critical flagged tests	between selected dates.

Search for critical value	This option will search the verified

flagged tests	data within a given time span looking for the critical value flag.

Search for high/low values of a test	This option will search for one or more tests looking for data values less than, equal to, or greater than a set value. The search will be for data verified within a given time span.

**Option	Description**

Summary list	All results for a given accession area(s)

(extended supervisor’s)	for a given date and range of accession numbers.

Summary list (supervisor’s)	All results for a given accession area (or areas) for a given date and range of accession numbers. This report can serve as an “audit trail” for a specimen. Includes information on person placing order, person performing test, verifying person, and dates and times of specimen collection and test completion. The report can be sorted by accession number or by patient, and can be printed in a long form, which includes the above mentioned information plus the test results.

Supervisor’s report	If the Tasked routine [LRTASK ACS] fails to generate its output, this function may be used to re-initiate the printout. This report is based on the same formats and definitions in File #64.5. The report is printed within location by patient. If a supervisor summary is desired by accession, then use the option [LR SUP SUMMARY]. [LRACS MANUAL] requires that entries be made in the Daily Summary Reports fields of the LAB REPORTS file (#64.5) in order to work.

### Glossary

This Glossary contains terms and their definitions that may not be familiar to the user who is accessing the facility’s computers for the first time. Basic terms, acronyms, and phrases that are used throughout the  environment are included.

Access Code	A code that allows the computer to identify you as a user authorized to gain access to the computer. Your code is greater than six and less than twenty characters long; can be numeric, alphabetic, or a combination of both; and is usually assigned by a site manager or application coordinator. (See the term verify code in the Glossary.)

Accession	A unique alpha-numeric (combination of letters and numbers) assigned to an individual patient specimen when it is received in the laboratory. The accession is assigned by the computer and contains the laboratory departmental designation, the date, and an accession number. This accession serves as identification of the specimen as it is processed through the laboratory. (Example: HE 09121)

Accession Area	A functional area or department in the laboratory where specific tests are performed. The accession area defines the departmental designation contained in each accession.

Accession Date	The date of the accession, part of the total alpha-numeric accession of each specimen.

Accession Number	A unique number assigned to each accession.

ADT	Admission, Discharge, Transfer. A component of the MAS software package.

AFIP	Armed Forces Institute of Pathology; an external review board.

AMIS	Automated Management Information System; a method for tabulating Workload.

ANSI MUMPS	The MUMPS programming language, now officially called “M” Technology, is a standard; that is, an American National Standard. MUMPS stands for Massachusetts General Hospital Utility Multi-Programming System.

Application	A computer program (e.g., a package) that accomplishes tasks for a user.

Application Coordinator	The designated individual responsible for user-level management and maintenance of an application package (e.g., IFCAP, Laboratory, Pharmacy, Mental Health).

Auto Instruments	Automated instruments used in the Lab that identify and measure tissue or other specimens.

Bidirectional	Automated instruments that send and receives information from .

CAP	 Pathology

CAP CODES	Numbers assigned to lab procedures by the  for compiling workload statistics.

Collection List	A listing of routine laboratory tests ordered for inpatients. The list is used by the Phlebotomy team during routine collection of specimens from the wards. The list is sorted by ward location, and includes both patient information (Name, SSN, bed/room number) and test information, type of specimen to collect, amount needed, date and time tests were ordered, urgency status, order number and accession number.

Core	The fundamental clinical application packages of . The original core of applications built on the Kernel and VA FileMan were Admission, Discharge and Transfer (ADT), Scheduling, Outpatient Pharmacy, and Clinical Laboratory. Additional software packages were added to implement Core+6 and Core+8 configurations.

Cumulative	A chartable patient report of all data accumulated on a patient over a given time period.

DRG	Diagnostic Related Group

E3R	Electronic Error Enhancement Reporting System.

Electronic Signature 	A code that is entered by a user which represents his or her legally binding signature.

EP	Expert Panel

Extended Core	Those applications developed after the basic core  packages were installed (e.g., Dietetics, Inpatient Pharmacy). Also referred to as Core+6 or Core+8.

Header	Information at the top of a report.

JCAHO	Joint Commission for the Accreditation of Health Care Organizations.

Lab Subsection	Refers to the subdivision of lab major sections. If your lab uses this system, your reports will be printed and totaled by lab subsection as well as lab section.

LIM	Laboratory Information Manager

LMIP	Laboratory Management Index Program

LSI	Large Scale Integrating Device also known as Laboratory System Interface, an instrument for translating data between  and auto instruments.

Major section	Refers to the grouping of lab subsections into major groups within the lab. A lab may consist of the following major sections: General Clinical (may include hematology, toxicology, serology, chemistry, etc.,) Blood Bank Microbiology, and Anatomic Pathology. If your lab uses this system, your workload report will be reported by major section (“Section Workload Report”).

Menu Tree	A series of menus you sequence through in order to get to the specific option you desire.

MicroScan	An automated instrument used for organism identification and for measuring antibiotics within the Microbiology module.

OE/RR	Order Entry and Results Reporting

Password	A user’s secret sequence of keyboard characters, which must be entered at the beginning of each computer session to provide the user’s identity.

Printer	A printing or hard copy terminal.

QA	Quality Assurance

SERA	Systematic External Review of Autopsies.

SERS	Systematic External Review of Surgical Pathology.

SNOMED	Systematized Nomenclature of Medicine developed to standardize the coding of information regarding specific diseases.

Treating Area	The section or service of the hospital that requests a test. Some hospital systems have an embedded code that determines if the ordered test is for an inpatient or outpatient.

VA	The Department of Veterans Affairs, formerly called the Veterans Administration.

VAMC	Department of

Verification (data verification)	The process by which technologists review data in the computer for a specific patient and verify (validate) that it is accurate before releasing the data to the physician.

Verification 	A process of internal and external

(package verification) 	package review carried out by a  verification team. Software and associated documentation are reviewed in terms of VistA Standards and Conventions.

VITEK	An automated instrument is used for organism identification and for measuring antibiotics within the Microbiology module.

WKLD	Abbreviation for workload. The Department of Veterans Affairs offshoot of CAP workload reporting. Also used for LMIP applications. See LMIP.

WKLD Code	Numbers assigned to lab procedures by the Laboratory program for compiling work statistics.

Work List	Used for collecting and organizing work in various accession areas of the laboratory. A work list is generated for manual or automated tests (singly or in batches) and can be defined by number of tests and/or which tests to include. It can also be used as a manual worksheet by writing test results directly on the worklist.

### Index

.C2.Supervisor’s Report, 85

@, 44

^, 44

Accession and Test Counts by Shift, 99

Accession List by Number, 99

Accession order then immediately enter data, 20, 119

Accessioning, 28

Accessioning Menu [LR IN], 9

Accessioning Tests Ordered by Ward Order Entry, 94

Accessioning, standard (Microbiology), 94, 144

Accessioning, Standard (Microbiology) [LRMICROLOGIN], 28

Active Load Work Listing, 107

Add a new data name, 163

Add a new internal name for an antibiotic, 163

Add a new WKLD code to file, 164

Add tests to a given accession, 95

Add Tests to a Given Accession [LRADD TO ACC], 28

Add Tests to an Already Existing Order Number, 134

Add to collection list, 15, 16

Add to Collection List, 89

Add/edit QC name and/or edit test means, 122

Add/Edit QC Name and/or Edit Test Means, 154

All results for selected accessions, 146

All Results for Selected Accessions, 55

Anatomic Pathology [LRAP], 9

antibiotic, 51

Antibiotic Screen, 42

antibiotics which have been transmitted, 42

Antimicrobial Trend Report, 56, 57

AP Microfiche Archive, 164

Archive lab data, 164

Audit of deleted comments, 185

AUTO INSTRUMENT file (. 62.4)

**automatically released** , 36

Batch Accessioning, 145

Batch Accessioning [LRMIBL], 28

Batch data entry (chem, hem, tox, etc.), 20

Batch Data Entry (chem, hem, tox, etc.), 119

baud rate, 67

Blood Bank [LRBL], 9

Both or Output, 79

Build a load/work list, 18

Build a Load/Work List, 119

Bull algorithm quality control, 122

Bypass normal data entry, 20, 95

Bypass Normal Data Entry, 24, 120

Change instrument run mode, 160

Change Load/Work list type, 154

Changes in verified lab data, 154, 185

Changing or modifying entered data, 24

Check a single routine size, 167

Check files for inconsistencies, 166

Check patient and lab data cross pointers, 166

Check the lab interface, 160

Clear data from the LAR global, 165

Clear instrument/worklist data, 108

Clear instrument/worklist data, 17, 18

Clear Instrument/Worklist Data, 118

Clear Instrument/Worklist Data [LRINSTCLR] option, 61

Convert archive data to use NEW PERSON file, 166

Count accessioned tests, 185

CPT, 8

Create new collection list, 15, 16

Cumulative device status, 154

Cumulative Menu...., 154

Cumulative patient report, 55

Delete a Test from an Accession, 28

Delete entire order, 95

Delete entire order or individual tests, 134

Delete test from an accession, 95

Delete user selected lab test/patient lists, 176

Detail workload report, 168, 171

Detail Workload Report, 183

Diagnostic routine for LAB REPORTS file (64.5), 154

Direct Connect Auto-Instrument Start, 161

Direct connect instruments:, 72

display order, 42

Display User Characteristics, 10

Documentation for lab options, 158

Download a Load List to an Instrument, 120

Download Format for This option is used to down load the, 166

Edit a lab administration schedule, 175

Edit atomic tests, 158, 166

Edit control placement on load/work list, 123

Edit controls added to the accessions each day, 159

Edit Controls Added to the Accessions Each Day, 123

Edit cosmic tests, 159, 167

Edit HOSPITAL SITE parameters, 175

edit templates, 43, 44

Edit the default parameters Load/Work List, 159

Edit the Load/Work list profile, 159

Edit Workload Comments, 110, 176

Edit/Print/Display Preselected Lab Test Menu, 126

Enter/Edit medical journal This option allows entry and editing of, 148

Enter/Edit micro journal references, 148

Enter/edit predefined lab test lists, 176

Enter/edit user defined lab test lists, 126

Enter/verify data, 22

Enter/verify data (auto instrument), 23, 24, 106

Enter/Verify Data (auto instrument), 62

Enter/verify data (load list), 21, 24

Enter/verify data (Load list), 106

Enter/verify data (load list) [LRVRW2], 21

Enter/verify data (Work list), 21, 107

Enter/verify data (Work list) [LRVRW], 21

Enter/verify data (worklist), 24

Enter/verify/modify data (manual), 20, 24, 106

Enter/verify/modify data (manual) [LRENTER], 20, 21

Enter/Verify/Modify Data (manual) [LRENTER], 24

ENVIRONMENTAL, 29

ETIOLOGY, 43

Etiology WKLD Codes (Force), 168

execute codes, 43

Extended File Syntax, 29

Fast lab test order, 15, 16

Fast lab test order (IMMEDIATE COLLECT), 96, 136

Fast lab test order (ROUTINE), 97, 136

Fast lab test order (SEND PATIENT), 97, 136

Fast lab test order (WARD COLLECT), 137

File 81 conversion, 168

File list for lab, 167

File listings, 111, 177

Find patient’s archived data, 166

Flagged Specimens, 118

Force cumulative data to Permanent Page, 155

General report for selected tests, 131, 137

General Report for Selected Tests, 55, 126

Graph results, 137

Graph Results, 127

Group data review, 107

Group data review (verified &amp; EM), 20

Group unverified review, 22, 23

Group unverified review, 21

Group unverified review, 107

Group Unverified Review (EA,EL,EW), 62

Group verify, 21, 22, 23

Group Verify (EA,EL,EW), 118

Halt SMAC Run, 118

Health Department report, 146

Health Department Report, 57

Historical Lab Results, 26

Incomplete test status report, 108

Incomplete test status report, 18

Infection control survey report, 146

Infection Control Survey Report, 56

Infection warning edit, 160

Infection Warning Edit, 57

Information-Help Menu [LRHELP], 9

Initialize LAC global &amp; X references, 155

Input Only., 79

Inquire to a Lab administration schedule, 175

Inquire to micro journal references, 148

Inquiry to LAB TEST file, 97, 131, 160

Insert a sample on a load/work list, 17, 18

Insert a Sample on a Load/Work list, 108

interface, 63

interfaced auto instrument on-line, 17

interfaced instrument,, 60

Interim report, 134

Interim Report, 127

Interim report by provider, 82, 138

Interim Report by Provider, 127

Interim report for selected tests, 128, 138

Interim report for selected tests as ordered, 134

Interim Report for Selected Tests as Ordered, 128, 132

Interim Report for Selected Tests as Ordered [LRRSP] option., 55

Interim reports by location (manual queue), 83, 129

Interim reports for 1 location (manual queue), 82, 129

Interim Reports for 1 Location (manual queue), 139

Interim reports for 1 provider (manual queue), 129

Itemized routine lab collection, 16

Itemized routine lab collection, 15

Itemized Routine Lab Collection, 89

Keypad differential for CRT’s, 109

Lab Accession and Test Counts, 100

Lab add test(s) to an existing order, 97

Lab Error Trap Listing, 161

Lab Interface Menu...., 160

Lab Liaison Menu...., 163

Lab orders by collection type, 90, 97, 172

LAB ROUTINE INTEGRITY MENU, 167

Lab section list by code, 111, 178

Lab section list by name, 111, 178

Lab statistics menu, 176

Lab Statistics Menu, 110, 145

Lab subsection by Lab section, 111, 178

Lab subsection list, 111, 178

Lab test order, 16, 139

Lab Test Order, 90

Lab test turnaround time, 112, 172, 179

LIM WORKLOAD MENU, 168

List of lab orders not collected, 140

List of Lab Orders not Collected, 90

List of orders not collected, 15, 16, 19

List of orders not collected (Long Form), 90

List of Patients by Location for Cumulative Report, 155

Listing of Laboratory Menus/Options, 184

LMIP Reports/Data Collection, 112, 179

Load Integrity File, 167

load list profile, 60

load or work lists, 17

load/work list, 60

**Local Auto Instrument files** , 71

Long form accession list, 18, 116, 147

Long form accession list for microbiology, 145

Look up accession, 19

Lookup accession, 97

Lookup Accession, 120

Loop thru LR INTEGRITY, 167

low volume samples drawn by ward or clinic staff, 14

LRANAT, 11

LRAPSUPER, 11

LRAU, 11

LRBLOODBANK, 11

LRBLSUPER, 11

LRCY, 11

LREM, 11

LRLAB, 11

LRLIASON, 11

LRMICRO, 11

LRMIVERIFY, 11

LRPHMAN, 11

LRPHSUPER, 11

LRSP, 11

LRSUPER, 11

LRVERIFY, 11

LSI management, 68

Major headers, 74

Manual Enter Clinic Stop Codes, 98

Manual queuing of cumulative, 155

Manual Queuing of Fileroom Cum, 156

Manually accession QC, Environmental, etc., 98, 123, 184

Manually compile WKLD and workload counts, 174

MENU PATH, 10

MIC results, 34

Micro Approval Method, 39

Microbiology Menu [LRMI], 9

Microbiology Print Menu...., 146

Microbiology Trend Report, 56

Microbiology Trend Report, 147

Modify an existing data name, 163

Move a load/work list entry, 17, 18

Move a Load/Work list entry, 116

Multiple LSI:, 68

Multipurpose accessioning, 99

Mumps A index of the LAB REPORTS file, 157

Mumps A, AC, &amp; AR indexes of the LAB REPORTS file, 157

Mumps AC index of the LAB REPORTS file, 157

Mumps AR index of the LAB REPORTS file, 157

new isolate, 51

OE/RR interface parameters, 174

Order/test status, 90, 99, 129, 132, 140

Order/Test Status, 79

organism/isolate, 39, 42

Outline for one or more files, 175

Overlay Data field, in the AUTO INSTRUMENT file (. 62.4), is set to

Patient Lab Discharge Summary (Manual), 156

Patient report, 147

Patient Report [LRMIPSZ] option, 55

pending accessions, 17

PHASE 1

Move data from 64.1 to 67.9, 112, 169, 179

PHASE 2

Collect data for transmit to NDB, 113, 169, 180

PHASE 3

Print of data to be sent to NDB, 114, 170, 180, 182

PHASE 4

Create E-mail message for NDB, 114, 170, 181

PHASE 5

Purge monthly WKLD data from 67.9, 115, 171, 181

Phlebotomy Menu [LR GET], 9

**Print a full patient summary** , 25, 130, 156

Print a load/work list, 17, 18

Print accession list(s), 99

Print collection list/labels, 16, 91

Print future collection labels, 100

Print Future Collection Labels, 91

Print single future collection label, 101

Print/display preselected lab tests, 126

Process Data in Lab Menu [LR DO!], 9

Purge data found in the Search option, 165

Purge old orders &amp; accessions, 184

Purge the Cumulative file, 157

Quality control display, 124

Quality Control Display, 118

**Quality control display (Levey-Jennings)** , 25

Quality Control Menu [LRQCM], 9

RB Results Entry (Batch) [LRMISTUF], 30

RCS-CDR/LMIP REPORT, 171, 172

RE Results Entry [LRMIEDZ], 30

Read data from off-line media, 165

Receipt of routine lab collection from wards, 15

Receipt of routine lab collection from wards, 16

Receipt of routine lab collection from wards, 16

Receipt of Routine Lab Collection from Wards, 92

Recompile Phase 1 LMIP Data, 115, 171, 181

Re-cross-reference Indexes in LAB Reports, 157

References, 148

REFERRAL PATIENT, 29

Re-index Antimicrobial Suscept File (62.06), 175

remote collection sites, 14

Remove a load/work list entry, 17, 18

Remove a Load/Work List Entry, 116

Reprint a permanent page from cumulative, 157

Reprint a Ward Collect Order, 140

Reprint accession label(s), 101

Reprint cumulative from location to location, 158

Reprint Cumulative on a Given Location, 158

Reprint cumulative on a given patient, 158

Reprint order accessions label(s), 101

Requesting center dictionary, 112, 178

RESEARCH, 29

Restart Processing of Instrument, 61

Restart processing of instrument data, 162

Restore archived data to LR global, 166

Results entry, 144

Results entry (batch), 142

Results menu, 148

Results Menu [LR OUT], 9

Review accession workload, 144, 182

Review by order number, 102, 130, 132, 140

Review by Order number, 19

Revision History, iii

Rollover Accession (Manual), 117

RS-232, 63

RS-232-C, 65

Run SMAC, 119

Search for abnormal and critical flagged tests, 185

**Search for abnormal/critical flagged results** , 25

**Search for critical value flagged tests** , 25, 185

**Search for high/low values of a test** , 25, 185

Search for lab data to archive, 165

security keys, 10

Service dictionary, 111, 178

Set a new starting accession number, 184

Set instrument to run by Accession, 162

Set instrument to run by load list, 163

Set New Starting Sequence Number, 117

Short accession list, 18, 147

Short accession List, 148

Short Accession List, 117

Short and Long Form Accession Lists, 54

Show list of Accession for a patient, 19

Show list of accessions for a patient, 102, 140, 148

SMAC Support Menu...., 117

Smear/prep tests, 36

Special test accessioning, 102

Std/QC/Repeats manual Allow the tech to manual update, 121

STD/QC/REPS MANUAL  Allow the tech to manual update, 182

Std/QC/Reps manual workload count, 148

STERILIZER, 29

**Summary list (supervisor’s)** , 25, 186

Summary list(extended supervisor’s), 185

**Summary lists** , 25

Supervisor Menu [LRSUPERVISOR], 9

Supervisor Menu...., 148

Supervisor reports, 185

SUPERVISOR WORKLOAD MENU, 171

**Supervisor’s report** , 25, 186

TBOX, 5, 10

Test Counts by Treating Specialty, 100

Test description information, 92, 102, 132, 140

Test dictionary, 112, 178

Test the interface, 163

Treating Specialty Workload, 183

Treating Specialty Workload This option will provide a report divided by, 172, 173

troubleshooting, 67

Turn on site workload statistics, 176, 182

Turn on workload stats for accession area, 176, 182

Unload load/work list, 17, 18

Unload Load/Work List, 121

Update Lab protocols for OE/RR, 175

User selected lab test/patient list edits, 176

User’s Toolbox menu, 5

Verification of data by supervisor, 144

Verification of Data by Supervisor, 38

Verification of data by tech, 144

Verification of Data by Tech, 38

VistA **bidirectional routines** , 64

Ward collection summary, 15, 16

Ward collection summary for lab orders, 140

Ward lab menu, 92

Ward Lab Menu [LRWARDM], 9

Watch the data in the LA global, 163

WKLD code list by code, 111, 177

WKLD code list by name, 111, 178

WKLD log file download, 112, 178

WKLD statistics reports, 182

Work Sheet Accession List, 119

Work sheet of all unverified accessions for a date, 119

WORKLOAD code list, 173

Workload cost report by major section, 172, 173, 183

Workload Manual Input, 184

Workload Report, 172, 173, 183

Workload statistics by accession area and shift, 173, 174, 183

Write data to off-line media, 165