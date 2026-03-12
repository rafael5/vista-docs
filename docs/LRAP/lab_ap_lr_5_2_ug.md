---
app_name: 'Laboratory: Anatomic Pathology'
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: 2022-09
doc_type: user-manual
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-12'
is_base: false
is_change_pages: false
library_max_patch: null
package_id: LRAP
patch: 553
patch_gap: null
section: ''
source_file: lab_ap_lr_5_2_ug.docx
status: draft
title: Laboratory Anatomic Pathology (AP)
---

# Laboratory Anatomic Pathology (AP)

# Version 5.2

# User Guide

<!-- image -->

September 2022

Department of Veterans Affairs (VA)


Revision History

| Date           | Description (Patch # if applicable)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Author                        |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| September 2022 | LR*5.2*553:  Document formatting updates only                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | CPRS Development Team         |
| June 2021      | LR*5.2*544:  - Added Note for CPRS v32a - Added CPRS AP DIALOG parameter Hints - Added Log-in of Surgical Pathology Specimen Examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                               |
| 02/2019        | LR*5.2*504  Added Missing AP Alert Search to the Menu Options and added LRAPALERT section                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | HPS Clinical Sustainment Team |
| 09/2015        | LR*5.2*442, Updates for ICD-10 Patient Treatment File (PTF) Modifications:  - Updated title page, headers, footers, and Revision History. - Corrected styles and spacing issues throughout document. - Reformatted table in Appendix B. - Added text to Tissue Committee Review Cases Option (p.286, 377).                                                                                                                                                                                                                                                                                                                                                                   |                               |
| 08/2014        | LR*5.2*422 – Updates for ICD-10  Overall: Ensured all screen captures followed the SSN guidelines specified in  *Displaying Sensitive Date Guide*  .  Updated Title page  Added Revision History (pp i-ii)  Changed ICD9 to ICD (pp.3, 18, 192, 196)  "FS/Gross/Micro/Dx/ICD Coding [LRAPDGI]" (pp. 84, 360)  "Autopsy protocol &amp; ICD coding [LRAPAUDAA]" and "FS/Gross/Micro/Dx/ICD Coding [LRAPDGI]" (p.20)  "Autopsy protocol &amp; ICD coding [LRAPAUDAA]" (pp. 40 49, 343,362)  ICD Coding, Anat Path [LRAPICD] "Select ICD DIAGNOSIS:" and "FS/Gross/Micro/Dx/ICD Coding [LRAPDGI]" (p. 41)  ICD Coding, Anat Path [LRAPICD] "Select ICD DIAGNOSIS:" (pp. 67, 363) |                               |
| 01/2001        | Revised.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | VA OIT                        |
| 10/1994        | Initial document published.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | VA OIT                        |

**Preface**

**NOTE:** The Veterans Health Information Systems and Architecture ( **V** *IST* **A** ) Laboratory Anatomic Pathology User’s Manual released in October 1994 has been edited to include an Appendix B section. The appendix contains file, fields, options changes, and examples created by the release of patch LR*5.2*248.

The Anatomic Pathology User’s Manual was designed as a training guide and reference manual for Veterans Affairs Medical Center (VAMC) Site Managers, Lab Applications Coordinators, and all users of the Anatomic Pathology module of the Laboratory software application. It should be used in conjunction with other documentation of the Laboratory software application. The manual shows users how to enter, edit, and display information for Cytopathology, Autopsy Pathology, Surgical Pathology, Electron Microscopy, preselected lab test lists, and lists of unverified pathology reports. It also shows how to print reports, path micro/dx modification, cum path data summaries, and preselected lab test lists.

Table Of Contents

Introduction	2

Overview of Anatomic Pathology Module	2

Functionality	3

Orientation	5

Before You Begin	5

Special Keys, Commands, and Conventions	5

Manual Conventions	8

Package Management	10

Package Operations	12

Anatomic Pathology Menu	12

Menu Descriptions	13

Anatomic Pathology Menus	15

Workflow	21

A. Log-in	21

B. Data Entry	21

C. Final Reports	22

Summary of Selected AP Options	24

SNOMED Coding/Searches	25

Reports	28

Frozen Sections	28

Bone Marrows	28

Autopsy	29

Anatomic Pathology Menu Options	33

Data Entry, Anat Path [LRAPD]	34

Descriptions	34

Data entry for Autopsies [LRAPAUDA]	34

Coding	35

Data Entry for Autopsies [LRAPAUDA]	37

Provisional Anatomic Diagnoses [LRAPAUPAD]	37

Autopsy Protocol [LRAPAUDAP]	39

Autopsy Protocol and SNOMED Coding [LRAPAUDAB]	40

Autopsy Protocol and ICD Coding [LRAPAUDAA]	48

Final Autopsy Diagnoses Date [LRAPAUFAD]	50

Autopsy Supplementary Report [LRAPAUSR]	51

Autopsy [LRAPAUDAS]	53

Blocks, Stains, Procedures, Anat Path [LRAPSPDAT]	56

Surgical Pathology	56

Cytology	56

Electron Microscopy	56

Autopsy	56

General	57

Example 1:	Routine Data Entry for Surg Path (workload off)	57

Example 2:	Routine Data Entry for Surgical Pathology Frozen Section	59

Example 3:	Editing Data for Cytology	62

(data already entered based on workload profiles)	62

Example 4:	Data Entry for EM	65

Example 5:	Date/Times are not in Sequence	67

Example 6:	More than one Specimen	69

Coding, Anat Path [LRAPCODE]	71

SNOMED Coding, Anat Path [LRAPX]	71

ICD Coding, Anat Path [LRAPICD]	72

Clinical HX/Gross Description [LRAPDGD]	74

Example 1:	Entry of Information for a Surgical Pathology/	75

ASK FROZEN SECTION set to NO	75

Example 2:	Entry of Information for a Surgical Pathology Specimen with a	76

Frozen Section ASK FROZEN SECTION set to YES	76

FS/Gross/Micro/Dx [LRAPDGM]	78

FS/Gross/Micro/DX/SNOMED Coding [LRAPDGS]	81

Example 2:	Entry of Information for a Surgical Pathology Specimen	85

with a Frozen Section	85

Example 3:	Using a Template to enter a Bone Marrow Report	87

Example 4:	Using a Template to Enter a Bethesda system Report for a Cytology	95

FS/Gross/Micro/Dx ICD [LRAPDGI]	97

Enter Old Anat Path Records [LRAPOLD]	99

Supplementary Report, Anat Path [LRAPDSR]	101

Special Studies-EM;Immuno;Consult;pic, Anat Path [LRAPDSS]	104

Edit/Modify Data, Anat Path [LRAPE]	106

Description	106

Edit Log-In &amp; Clinical Hx Anat Path [LRAPED]	107

Modify Anat Path Gross/Micro/Dx/Frozen Sections [LRAPM]	110

Example 1:	Modify Anat Path Gross/Micro/Dx/Frozen Section	110

Example 2:	Surgical Pathology Final Patient Reports Printout	111

Example: 3	Surgical Pathology Final Patient Reports Printout	113

Inquiries, Anat Path [LRAPI]	122

Descriptions	122

Display Surg Path Reports for a Patient [LRAPSPCUM]	123

Display Cytopath Reports for a Patient [LRAPCYCUM]	123

Display EM Reports for a Patient [LRAPEMCUM]	123

Display Stains/Blocks for a Patient [LRAPST]	126

Show List of Accessions for a Patient [LRUPT]	127

Search Options, Anat Path [LRAPSEARCH]	128

Morphology Code Search, SNOMED [LRAPSM]	128

Procedure Code Search, SNOMED [LRAPSP]	131

ICD Code Search [LRAPSI]	132

MULTIAXIAL Code Search, SNOMED [LRAPSEM]	132

Cum Path Data Summaries [LRAPT]	139

Display Final Path Reports by Accession Number [LRAPPA]	145

Log-in Menu, Anat Path [LRAPL]	146

Delete Accession #, Anat Path [LRAPKILL]	154

Print Log Book [LRAPBK]	155

Surgical Pathology Log Book	156

Histopathology Worksheet [LRAPH]	157

Print, Anat Path [LRAPP]	158

Descriptions	158

Print Queue Information	162

Print All Reports on Queue [LRAP PRINT ALL ON QUEUE]	163

Example 1: Surgical Pathology Preliminary Report	163

Example 2: Surgical Pathology Final Patient Reports	166

Example 3: Surgical Pathology Report with Frozen Section	168

Example 4: Change in Prompts if you select the Autopsy Section	171

Delete Report Print Queue [LRAP DELETE]	176

List Pathology Reports in Print Queue [LRAPQ]	176

Print Single Report Only [LRAP PRINT SINGLE] option	178

Add Patient(s) to Report Print Queue [LRAP ADD]	183

Autopsy Data Review [LRAPAURV]	184

Alphabetical Autopsy List [LRAPAUA]	186

Autopsy Status List [LRAPAUSTATUS]	187

Anat Path Accession Reports [LRAPPAR]	188

Anat Path Accession List by Date [LRAPPAD]	188

Anat Path Accession List by Number [LRAPPAN]	190

Sum of Accessions by Date, Anat Path [LRAPA]	193

Entries by Dates, Patient and Accession Number [LRAPPF]	195

List of Path Cases by Resident, Tech, Senior or Clinicians [LRAPAUL]	196

.% Pos, Atyp, Dysp, Neg, Susp, &amp; Unsat : Cytopath [LRAPCYPCT]	197

Accession List with Stains [LRAPSA]	204

Accession Counts by Senior Pathologist [LRAPAULC]	206

Cum Path Data Summaries [LRAPT]	208

Anatomic Pathology Labels [LRAPLBL]	209

Anat Path Slide Labels [LRAPLM]	209

Anat Path Specimen Labels [LRAPLS]	215

Autopsy Slide Labels (Generic) [LRAUMLK]	216

Edit/Print/Display Preselected Lab Tests [LRUMDA]	218

Enter/Edit User Defined Lab Tests Lists [LRUMDE]	218

Edit Print/Display Preselected Lab Tests [LRUMDA]	222

Print Log Book [LRAPBK]	229

Print Final Path Reports by Accession Number [LRAPFICH]	230

SNOMED Field References [LRAPREF]	236

Descriptions	236

Enter/Edit SNOMED File References [LRAPSRE]	237

Medical Journal File Edit [LRAPLIB]	239

Print References for a SNOMED Entry [LRAPSRP]	240

Supervisor, Anat Path [LRAPSUPER]	241

Descriptions	241

Delete Anat Path Descriptions by Date [LRAPDAR]	247

Enter/Edit Lab Description File [LRAPDES]	249

Edit Pathology Parameters [LRAPHDR]	253

[Edit pathology parameters (Example 1 cont’d)]	255

[Edit pathology parameters (Example 2 cont’d)]	258

Enter/Edit Items in a SNOMED Field [LRSNOMEDIT]	263

Incomplete Reports, Anat Path [LRAPINC]	265

Print Path Modifications [LRAPMOD]	266

Example: Print Pathology Report Modifications	266

Anatomic Pathology Topography Counts [LRAPC]	272

Delete Free Text Specimen Entries [LRAPDFS]	274

Missing AP Alert Search (LRAPALERT)	274

AP Quality Assurance [LRAPQA]	277

Summary of TC and QA Codes	278

QA Codes Entry/Edit [LRAPQACD]	279

AP Consultation Searches and Reports [LRAPQACN]	283

[Listing of cases sent to SERS Printout]	287

Listing of cases sent to SERS Printout (contd)	289

Cum Path Summaries for Quality Assurance [LRAPQAC]	291

.% Pos, Atyp, Dysp, Neg, Susp, &amp; Unsat Cytopath [LRAPCYPCT]	293

Delete TC and QA Code [LRAPQADEL]	299

Frozen Section, Surgical Path Correlation [LRAPQAFS]	300

Print path gross/micr/dx/fr.sect modifications [LRAPQAM]	306

Example: ‘Surgical Pathology Report’	306

Example: ‘Surgical Pathology’ report continued	307

Malignancy Review [LRAPQAMR]	309

QA Outcome Review Cases [LRAPQOR]	315

10% Random Case Review, Surg Path [LRAPQAR]	323

Edit QA Site Parameters [LRAPQASP]	327

Tissue Committee Review Cases [LRAPQAT]	328

Anatomic Pathology Turnaround Time [LRAPTT]	336

Move Anatomic Path [LRAPMV]	339

AFIP Registries [LRAPAFIP]	341

Prisoner of War Veterans [LRAPDPT]	341

Persian Gulf Veterans [LRAPPG]	343

Edit Referral Patient File [LRUV]	344

Verify/Release Menu, Anat Path [LRAPVR]	346

Descriptions	346

Verify/Release Reports, Anat Path [LRAPR]	347

Example 1: Release of Surgical Report	347

Example 2: Release of an ‘Autopsy’ report	351

Supplementary Report Release, Anat Path [LRAPRS]	352

List of Unverified Pathology Reports [LRAPV]	354

Clinician Options, Anat Path [LRAPMD]	356

Descriptions	356

Display Surg Path Reports for a Patient [LRAPSPCUM]	358

Display Cytopath Reports for a Patient [LRAPCYCUM]	358

Display EM Reports for a Patient [LRAPEMCUM]	358

Edit/Print/Display Preselected Lab Tests [LRUMDA]	362

Print Surgical Pathology Report for a Patient [LRAPSPSGL]	363

Print Cytopathology Report for a Patient [LRAPCYSGL]	363

Print Electron Microscopy Report for a Patient [LRAPEMSGL]	363

Cum Path Data Summaries [LRAPT]	367

Autopsy Protocol/Supplementary Report [LRAPAUPT]	376

Example: Autopsy Protocol Report	378

Workload, Anat Path [LRAPW]	382

Descriptions	382

Cytopathology Screening Workload [LRAPWR]	383

Display Workload for an Accession [LRUWL]	385

EM Scanning and Photo Workload [LRAPWE]	387

Surg Path Gross Assistance Workload [LRAPWRSP]	390

Microfiche of Path Reports	393

To Use at a VAX site	393

To Use at a Non-VAX site	394

Creating a Microfiche Tape	395

Enhancements to Reports on Microfiche	399

Glossary	402

Index	432

Appendix A	438

Anatomic Pathology User Manual Notes for Patch LR*5.2*72	438

Overview of Multidivisional Functionality	439

Anatomic Pathology Data Dictionary and Functionality Changes	440

Anatomic Pathology Option, Functionality, and Other Changes	442

Instructions for Anatomic Pathology for Multidivisional Sites and Multiple AP Accession Areas	442

DATA MERGER Information for the Consolidation Sites	447

LAB DATA file (#63)	447

Post DATA MERGER Instruction for the Consolidation Sites	450

APPENDIX B	452

Anatomic Pathology Patch LR*5.2*248 Changes	452

LAB DATA file (#63) Changes	452

New Fields	452

Anatomic Pathology Option Changes	455

Enhancements	455

Supplementary Report, Anat Path [LRAPDSR] option	455

Autopsy supplementary report [LRAPAUSR] option	457

Modifications	458

Show List of Accessions for a Patient [LRUPT] option	458

Modify anat path gross/micro/dx/frozen section [LRAPM] option	459

Verify/Release Reports, Anat Path [LRAPR] option	460

Example 1: Release of Surgical Report	460

Example 2: Release of ‘Autopsy’ report	462

Enter old anat path records [LRAPOLD] option	464

Log-in, anat path [LRAPLG] option	464

Autopsy protocol/supplementary report [LRAPAUPT] option	464

Clinical Hx/Gross Description/FS [LRAPDGD] option	466

FS/Gross/Micro/Dx [LRAPDGM] option	466

FS/Gross/Micro/Dx/SNOMED Coding [LRAPDGS] option	466

FS/Gross/Micro/Dx/ICD Coding [LRAPDGI] option	466

Supplementary Report, Anat Path [LRAPDSR] option	467

Spec Studies-EM;Immuno;Consult;Pic, Anat Path [LRAPDSS] option	467

Provisional anatomic diagnoses [LRAPAUPAD] option	467

Autopsy protocol [LRAPAUDAP] option	467

Autopsy protocol &amp; SNOMED coding [LRAPAUDAB] option	468

Autopsy protocol &amp; ICD coding [LRAPAUDAA] option	468

Final autopsy diagnoses date [LRAPAUFAD] option	468

Autopsy supplementary report [LRAPAUSR] option	468

Special studies, autopsy [LRAPAUDAS] option	469

SNOMED coding, anat path [LRAPX] option	469

ICD coding, anat path [LRAPICD] option	469

Modify anat path gross/micro/dx/frozen section [LRAPM] option	469

Verify/release reports, anat path [LRAPR] option	470

Supplementary report release, anat path [LRAPRS] option	470

Print path gross/micr/dx/fr.sect modifications [LRAPQAM] option	470

Print path modifications [LRAPMOD] option	470

Example: Print Pathology Report Modifications	470

Print final path reports by accession # [LRAPFICH] option	476

Print all reports on queue [LRAP PRINT ALL ON QUEUE] option	476

Print single report only [LRAP PRINT SINGLE] option	482

Laboratory Option Modifications	482

Accession List by Date [LRUPAD]	482

Lab orders by collection type [LRRP5] option	482

INTRODUCTION

## Introduction

### Overview of Anatomic Pathology Module

Anatomic Pathology (AP) is divided into four sections: Surgical Pathology, Cytology (Cytopathology), Electron Microscopy, and Autopsy Pathology. For the current version, bone marrows are considered to be part of the Surgical Pathology and do not get a separate accession area or number.

The processes of accessioning, data entry, coding, and editing are similar for each of these sections. The computer program lets you select one of these processes (menus or options) and then the section. That is, if you wish to log in a specimen for Cytology, you first select the “Log-in Menu,” and then you’ll be prompted to choose the Anatomic Pathology section. This manual is organized according to these menus.

The search options are based on SNOMED and ICD CM coding.

If you have individuals whom you wish to restrict access to only one, or more than one, specific areas, this can be done through the use of specific security keys for each area.

Certain sections of the anatomic pathology data can be extracted by the Health Summary if the accession has been verified/released. Accessions which have not been verified/released indicate this status (i.e., the accession information, but not the diagnosis).

**NOTE:** With the exception of the Workload Menu, the option descriptions reflect the prompts if workload is turned off unless otherwise specifically noted. The specifics of implementation, data capture, and reports are included in the Technical Manual.

### Functionality

Valuable Quality Assurance features including:

•	list of incomplete pathology reports for all areas

•	turnaround time reports for all areas of pathology

•	generation of defined “groups” of cases requiring additional review

•	correlation of all information (i.e., special stains, immunopathology, and electron microscopy studies, etc.,), in a single report

•	printing of laboratory test results for specified tests for a patient

Increased **productivity**

•	on-line access to historical pathology data (diagnosis &amp; SNOMED codes only)

•	immediate availability of information regarding surgical pathology, cytology, and electron microscopy specimens

•	access to verified/released reports by non-laboratory personnel

•	elimination of paperwork through automatic transfer of data to all appropriate files

Comprehensive **search/reporting** capabilities

•	final pathology reports

•	log book of all specimens accessioned, including final diagnosis variety of reports based on morphology and topography field entries

•	list of patients with a particular diagnosis

•	list of specimens from a particular site

•	list of specimens from a particular surgical procedure

**Workload** statistics

•	number of patients reviewed

•	number of specimens accessioned

•	number of specimens from a particular organ/tissue

•	data for LMIP

**NOTE:** The documentation for the overall implementation of the AP module, implementation of workload, the overview of data capture and the reports generated is in the Planning and Implementation Guide.

ORIENTATION

## Orientation

This manual is organized as shown in the table of contents. The option section is arranged according to the Anatomic Pathology Menu structure as described in the Menu section. If you don’t know which menu an option appears on, look at the menu diagram or check the index for the page number in this manual where the option is described.

### Before You Begin

•	Get an access code from your supervisor and find out which terminal and test data you should use.

•	Check with your supervisor for instructions about your menu choices.

•	Read the section “Special Commands, Keys, and Conventions.”

•	See the glossary for computer and lab terminology.

•	Read the “User’s Guide to Computing” for information on VA FileMan conventions and other useful help on using your computer.

•	Review these other manuals available from your Applications Coordinator:

- Laboratory User Manual
- Laboratory Package Security Guide

### Special Keys, Commands, and Conventions

The keyboard you will work on is similar to that of a typewriter. However, there are some additional keys and functions you will be using.

**On-line help for documentation**

**?** Entering a question mark after a prompt will cause the computer to display instructions or a list of choices for responding to that prompt.

**??** Two question marks after a prompt will cause a more detailed explanation to be displayed. If you enter two question marks after a menu display, the options on that menu, with their bracketed option names (e.g., [LRAPED]) will appear.

**???** Three question marks will usually cause more detailed instructions to appear, or a list of choices.

**Enter, Return, or Carriage Return:**

There are three uses for the RETURN or ENTER key (denoted in this manual as &lt;Enter&gt; on some keyboards this is the key with the symbol  **:**

Entering information	After you respond to a prompt, you must press &lt;Enter&gt;.

Accepting a default	If you want to accept the default value (the most likely response or a previously defined response, followed by //), just press &lt;Enter&gt;.

Skipping a prompt	If you do not want to enter any information in response to a prompt, you may press &lt;Enter&gt;, and the next prompt will appear if the previous prompt wasn’t mandatory.

**NOTE:** You **must** respond to some prompts in order to use the rest of an option. In these cases, the system supplies a message indicating that you must enter a response before continuing. You can use the up arrow **(^)** to escape from the prompt but you will lose all information previously entered.

**Delete** Deletes previous characters one at a time.

**Control Key:** The CONTROL key, like the shift key, is held down

**(CTRL)** while pressing another key.

**CTRL/S** stops the printing or scrolling. Useful when viewing a listing longer than your screen length. Some terminals have “HOLD Screen” or “SCROLL/NO SCROLL” for stopping scrolling.

**CTRL/Q** causes printing or scrolling to resume after CTRL/S has been used.

**CTRL/U** deletes current input line if &lt;Enter&gt; has not been pressed.

**^** ( **up-arrow**

**uppercase 6)** terminates the line of questioning you are in and returns you to the previous level in the routine. If you continue to enter “^,” you can exit the menus and the laboratory system.

**Enter** the enter key on a computer keyboard is the key you press at the end of each line in order to enter the contents of that line into the computer. In some terminals this key is also called the return key.

**Halt** entered at any point in an option will terminate your session immediately.

**Continue** entered at any point in an option will terminate your session immediately, but the computer remembers what you were doing when you terminated. When you log on again, you will be asked if you want to continue at that same point.

**Press** indicates one keystroke.

**Example:** Press RETURN or &lt;Enter&gt; means press the RETURN key.

**Press “^” to halt** displayed at the bottom of the screen means that processing will terminate within the selected option, and the computer returns to the menu you selected the option from.

**DEVICE:** These two prompts are included in every option

**RIGHT MARGIN: 80//** description in which you select a device for printing output. Because each site can specify whether to display each of the above for each terminal that it has, you may not always be asked both prompts. You may always enter “Q” for QUEUE when you are asked for a device. You will then be asked to specify the device to print on and the time to print.

**INTERACTIVE** Your computer terminal prompts you with questions and

**DIALOGUE** you respond with information, such as patient name, name of the test you are requesting, etc.

### Manual Conventions

- The Veterans Health Information Systems and Architecture ( **V** *IST* **A** ) Laboratory Anatomic Pathology User’s Manual released in October, 1994 has been revised to included modifications created by Patch LR*5.2*248. Modifications and examples are listed in the Table of Contents section of this manual as “Modified Options”. Side Bars used throughout the manual to indicate when modifications were made to the options.
- Examples of the dialogues for Anatomic Pathology options are shown 10 point Courier font. Printed reports are also in 10 point Courier font. User responses are **bolded** .

Select Data entry for autopsies Option: **SR** Autopsy supplementary report
Data entry for 1990 ? YES// **&lt;Enter&gt;** Autopsy supplementary report
Select Accession Number/Pt name: **2** for 1990
LABPPATIENT, ONE ID: 000-00-0001
Select SUPPLEMENTARY REPORT DATE: **T** SEP 12, 1990

DESCRIPTION:
	1&gt; **Examination of brain shows no evidence of metastatic carcinoma.** 2&gt; **&lt;Enter&gt;** EDIT Option: **&lt;Enter&gt;**

- Reports or replicas of printouts are also in 10 point Courier font except where noted.

------------------------------------------------------------------
CLINICAL RECORD :			AUTOPSY SUPPLEMENTARY REPORT	Pg 1
------------------------------------------------------------------
Date died: APR 26, 1990			:Autopsy date: APR 26, 1990 12:55
Resident: LABPROVIDER, ONE			: FULL AUTOPSY Autopsy No. A90 1
------------------------------------------------------------------

SUPPLEMENTARY REPORT DATE: AUG 10, 1990 10:43
This is an autopsy supplementary report. It is separate from the

*[etc..................]*

- The italicized words contained in brackets: *[Enter Print Device Here]* , refer to editor’s comments.
- Pressing the return key at the “Select Print Device: *[Enter Print Device Here]”* prompt sends the output to your terminal. You can also send the output to a specified printer.

**NOTE:** The note box indicates that a special action may be recommended or required.

PACKAGE MANAGEMENT

## Package Management

The Anatomic Pathology module of the Laboratory System has certain aspects that should be noted by the user:

1. Although quality assurance systems have been integral components of clinical pathology and blood usage review for many years, they did not exist as structured systems in anatomic pathology. Recent changes made by the Joint Commission for the Accreditation of Healthcare Organizations (JCAHO) in monitoring medical staff functions have necessitated the development of a comparable system for anatomic pathology. Please see the section on AP Quality Assurance for information about Joint Commission on Accreditation of Healthcare Organizations (JCAHO) requirements for Anatomic Pathology.
2. During the verification of reports, the computer records the user of the option LRVERIFY. This is the equivalent of an electronic signature. For more about this part of the program, please see the Verify Release Menu.
3. During log-in, the accessioner can indicate the patient’s physician and the pathologist whose name will appear on the report. Care must be taken to ensure that this information is correct.
4. The Workload (WKLD) codes are based on the College of American Pathologists (CAP) codes. The CAP codes are used with the permission of the College of American Pathologists. Specific instruments and products are referenced by the Workload codes. These references should not be perceived as endorsement or approvals by the **V** *IST* **A** system or the Laboratory software applications.

PACKAGE OPERATIONS

## Package Operations

**NOTE** : For a more complete discussion of implementing and maintaining the Anatomic Pathology module, please see the Planning and Implementation Guide.

### Anatomic Pathology Menu

The Anatomic Pathology main menu is shown below. Whether you see this entire menu or selected portions depends on how your site sets up its menus and what security keys you have.

Select Laboratory Option: **8** Anatomic pathology

ANATOMIC PATHOLOGY MENU

Select Anatomic pathology Option: **?**

D  Data entry, anat path...

E  Edit/modify data, anat path...

I  Inquiries, anat path...

L  Log-in menu, anat path...

P  Print, anat path...

R  SNOMED field references...

S  Supervisor, anat path...

V  Verify/release menu, anat path...

C  Clinician options, anat path...

W  Workload, anat path...

Menu items having an ellipsis (...) following the text will contain additional menu items. For example, if you choose D, for Data entry, another menu of options is displayed:

Select Anatomic pathology Option: **D** Data entry, anat path

Select Data entry, anat path Option: **?**

AU  Data entry for autopsies...

BS  Blocks, Stains, Procedures, anat path

CO  Coding, anat path...

GD  Clinical Hx/Gross Description/FS

GM  FS/Gross/Micro/Dx

GS  FS/Gross/Micro/Dx/SNOMED Coding

GI  FS/Gross/Micro/Dx/ICD Coding

OR  Enter old anat path records

SR  Supplementary Report, Anat Path

SS  Spec Studies-EM;Immuno;Consult;Pic, Anat Path

#### Menu Descriptions

The primary Anatomic Pathology Menu consists of ten secondary menus which are composed of submenus and options.

**Menu Item	Description**

**Data Entry** Used to enter descriptive or diagnostic data for Autopsy Pathology, Cytopathology, Electron Microscopy, or Surgical Pathology.

**Edit/Modify Data** Used to edit entries in log-in data, descriptions or diagnoses in Autopsy, Cytopathology, EM, or Surgical Pathology.

**Inquiries** Allows you to search and display on your screen summaries, reports, and pathology entries by date for SNOMED or ICD CM codes specified or a list of accessions.

**Log-in** Allows you to log in specimens for autopsy, cytopathology, EM, or Surgical Path, to delete an accession number, to print a list of specimens for a date by accession area, or to print the log book.

**Print** Includes options to print user-defined lab tests and patient lists, the log book, reports listing the clinical history and gross description for review, final reports, lists of prisoner of war veterans that have AP specimens, accession lists (by various criteria), lists of path cases by resident, tech or senior pathologist, etc.

**Menu Item	Description**

**SNOMED Field** Allows entering and editing of SNOMED references, file references, entering and editing of medical journal entries, and printing of medical journal references for a SNOMED file entry.

**Supervisor** Includes options for printing topography counts, turnaround times, and Quality Assurance Reports, for deleting and editing reports, entering, editing, or deleting lab descriptions or items in a SNOMED field, and for printing incomplete reports or reports with copies of all microscopic/diagnosis changes made to the report since the report was released.

**Verify/Release Reports** Contains options for printing a list of unverified pathology reports, selectable by date, and for displaying and printing reports that have been verified by the pathologist.

**Clinician** Displays or prints many types of summaries and reports from this menu, including user-defined lab tests and patient lists and cumulative summaries of surgical path, cytopath, EM, and autopsy.

**Workload** List of options for anatomic pathology workload

#### Anatomic Pathology Menus

D  Data entry, anat path [LRAPD]

AU  Data entry for autopsies [LRAPAUDA]

PD  Provisional anatomic diagnoses [LRAPAUPAD]

AP  Autopsy protocol [LRAPAUDAP]

AS  Autopsy protocol &amp; SNOMED coding [LRAPAUDAB]

AI  Autopsy protocol &amp; ICD coding [LRAPAUDAA]

AF  Final autopsy diagnoses date [LRAPAUFAD]

SR  Autopsy supplementary report [LRAPAUSR]

SS  Special studies, autopsy [LRAPAUDAS]

BS  Blocks, Stains, Procedures, anat path [LRAPSPDAT]

CO  Coding, anat path [LRAPCODE]

SN  SNOMED coding, anat path [LRAPX]

IC  ICD coding, anat path [LRAPICD]

GD  Clinical Hx/Gross Description/FS [LRAPDGD]

GM  FS/Gross/Micro/Dx [LRAPDGM]

GS  FS/Gross/Micro/Dx/SNOMED Coding [LRAPDGS]

GI  FS/Gross/Micro/Dx/ICD Coding [LRAPDGI]

OR  Enter old anat path records [LRAPOLD]

SR  Supplementary Report, Anat Path [LRAPDSR]

SS  Spec Studies-EM;Immuno;Consult;Pic, Anat Path [LRAPDSS]

E  Edit/modify data, anat path [LRAPE]

LI  Edit log-in &amp; clinical hx, anat path [LRAPED]

MM  Modify anat path gross/micro/dx/frozen section [LRAPM]

SC  Edit anat path comments [LRAPEDC]

I  Inquiries, anat path [LRAPI]

DS  Display surg path reports for a patient [LRAPSPCUM]

DC  Display cytopath reports for a patient [LRAPCYCUM]

DE  Display EM reports for a patient [LRAPEMCUM]

BD  Display stains/blocks for a patient [LRAPST]

PA  Show list of accessions for a patient [LRUPT]

SE  Search options, anat path [LRAPSEARCH]

MC  MORPHOLOGY code search, SNOMED [LRAPSM]

DC  DISEASE code search, SNOMED [LRAPSD]

EC  ETIOLOGY code search, SNOMED [LRAPSE]

PC  PROCEDURE code search, SNOMED [LRAPSP]

FC  FUNCTION code search, SNOMED [LRAPSF]

IC  ICD code search [LRAPSI]

AX  MULTIAXIAL code search, SNOMED [LRAPSEM]

CS  Cum path data summaries [LRAPT]

FR  Display final path reports by accession # [LRAPPA]

L  Log-in menu, anat path [LRAPL]

LI  Log-in, anat path [LRAPLG]

DA  Delete accession #, anat path [LRAPKILL]

PB  Print log book [LRAPBK]

HW  Histopathology Worksheet [LRAPH]

P  Print, anat path [LRAPP]

PQ  Print all reports on queue [LRAP PRINT ALL ON QUEUE]

DQ  Delete report print queue [LRAP DELETE]

LQ  List pathology reports in print queue [LRAPQ]

PS  Print single report only [LRAP PRINT SINGLE]

AD  Add patient(s) to report print queue [LRAP ADD]

AU  Autopsy administrative reports [LRAPAUP]

AD  Autopsy data review [LRAPAURV]

AA  Alphabetical autopsy list [LRAPAUA]

AS  Autopsy status list [LRAPAUSTATUS]

AR  Anat path accession reports [LRAPPAR]

LD  Anat path accession list by date [LRAPPAD]

LN  Anat path accession list by number [LRAPPAN]

SD  Sum of accessions by date, anat path [LRAPA]

PD  Entries by dates, patient &amp; accession # [LRAPPF]

WK  Path cases by resident, tech, senior or clinician [LRAPAUL]

CP  % Pos, Atyp, Dysp, Neg, Susp, Unsat cytopath [LRAPCYPCT]

ST  Accession list with stains [LRAPSA]

WS  Accession counts by senior pathologist [LRAPAULC]

CS  Cum path data summaries [LRAPT]

LA  Anatomic pathology labels [LRAPLBL]

LM  Anat path slide labels [LRAPLM]

LS  Anat path specimen labels [LRAPLS]

AU  Autopsy slide labels (generic) [LRAUMLK]

LT  Edit/print/display preselected lab tests [LRUMDA]

PR  Print/display preselected lab tests [LRUMD]

EN  Enter/edit user defined lab test lists [LRUMDE]

PB  Print log book [LRAPBK]

PA  Print final path reports by accession # [LRAPFICH]

R  SNOMED field references [LRAPREF]

ER  Enter/edit SNOMED file references [LRAPSRE]

TO  Topography (SNOMED) reference [LRAPTR]

MO  Morphology (SNOMED) reference [LRAPMR]

ET  Etiology (SNOMED) reference [LRAPER]

DI  Disease (SNOMED) reference [LRAPDR]

FU  Function (SNOMED) reference [LRAPFR]

PR  Procedure (SNOMED) reference [LRAPPR]

OC  Occupation (SNOMED) reference [LRAPOR]

MJ  Medical journal file edit [LRAPLIB]

PR  Print references for a SNOMED entry [LRAPSRP]

TP  Topography (SNOMED) reference print [LRAPTP]

MP  Morphology (SNOMED) reference print [LRAPMP]

EP  Etiology (SNOMED) reference print [LRAPEP]

DP  Disease (SNOMED) reference print [LRAPDP]

FP  Function (SNOMED) reference print [LRAPFP]

PP  Procedure (SNOMED) reference print [LRAPPP]

OP  Occupation (SNOMED) reference print [LRAPOP]

S  Supervisor, anat path [LRAPSUPER]

DD  Delete anat path descriptions by date [LRAPDAR] Locked: LRAPSUPER

ED  Enter/edit lab description file [LRAPDES]

ER  Edit pathology parameters [LRAPHDR]

ES  Enter/edit items in a SNOMED field [LRAPSNOMEDIT]

TO  Topography (SNOMED) enter/edit [LRAPTOP] Locked: LRAPSUPER

MO  Morphology (SNOMED) enter/edit [LRAPMOR] Locked: LRAPSUPER

ET  Etiology (SNOMED) enter/edit [LRAPETI] Locked: LRAPSUPER

DI  Disease (SNOMED) enter/edit [LRAPDIS] Locked: LRAPSUPER

FU  Function (SNOMED) enter/edit [LRAPFUN] Locked: LRAPSUPER

PR  Procedure (SNOMED) enter/edit [LRAPPRO] Locked: LRAPSUPER

OC  Occupation (SNOMED) enter/edit [] Locked: LRAPSUPER

IR  Incomplete reports, anat path [LRAPINC]

MR  Print path modifications [LRAPMOD]

TC  Anatomic pathology topography counts [LRAPC]

DS  Delete free text specimen entries [LRAPDFS]

QA  AP quality assurance [LRAPQA]

CE  QA codes entry/edit [LRAPQACD] Locked: LRAPSUPER

CN  AP consultation searches and reports [LRAPQACN]

CS  Cum path summaries for quality assurance [LRAPQAC]

CY  % Pos, Atyp, Dysp, Neg, Susp, Unsat cytopath [LRAPCYPCT]

DC  Delete TC and QA codes [LRAPQADEL]

FS  Frozen section, surgical path correlation [LRAPQAFS]

MM  Print path micro modifications [LRAPQAM]

MR  Malignancy review [LRAPQAMR]

OR  QA outcome review cases [LRAPQOR] Locked: LRAPSUPER

RR  10% random case review, surg path [LRAPQAR]

SP  Edit QA site parameters [LRAPQASP]

TC  Tissue committee review cases [LRAPQAT]

TT  Anatomic pathology turnaround time [LRAPTT]

AF  AFIP registries... [LRAPAFIP]

PO  Prisoner of war veterans [LRAPDPT]

PG  Persian gulf veterans [LRAPPG]

MV  Move anatomic path accession [LRAPMV]

Edit referral patient file [LRUV]

V  Verify/release menu, anat path [LRAPVR]

RR  Verify/release reports, anat path [LRAPR] Locked: LRVERIFY

RS  Supplementary report release, anat path [LRAPRS]

LU  List of unverified pathology reports [LRAPV]

C  Clinician options, anat path [LRAPMD]

DS  Display surg path reports for a patient [LRAPSPCUM]

DC  Display cytopath reports for a patient [LRAPCYCUM]

DE  Display EM reports for a patient [LRAPEMCUM]

LT  Edit/print/display preselected lab tests [LRUMDA]

PR  Print/display preselected lab tests [LRUMD]

EN  Enter/edit user defined lab test lists [LRUMDE]

PS  Print surgical pathology report for a patient [LRAPSPSGL]

PC  Print cytopathology report for a patient [LRAPCYSGL]

PE  Print electron microscopy report for a patient [LRAPEMSGL]

CS  Cum path data summaries [LRAPT]

AR  Autopsy protocol/supplementary report [LRAPAUPT]

W  Workload, anat path [LRAPW]

CW  Cytopathology screening workload [LRAPWR]

DW  Display workload for an accession [LRUWL]

EW  EM scanning and photo workload [LRAPWE]

SW  Surg path gross assistance workload [LRAPWRSP]

### Workflow

Description of an Implemented Module

Anatomic specimen processing and report preparation consist of three phases (for purposes of our discussion):

1. Log-in: This is the equivalent to accessioning in the clinical lab.
2. Data entry: This is the equivalent to “Processing” in the clinical lab package.
    1. Gross description with printout to go to pathologist with the slides
    2. Micro description and Dx to secretary for final typing

3.	Final Reports: is a hybrid of verification and cumulative report output in the clinical lab package.

##### A. Log-in

The surgical pathology case is accessioned using “Log-in” which has four sub options, one for log-in, another to delete an accession, a third to print the log book, and a fourth to print a histopathology worksheet. You may want to have access to some of these options limited. At the conclusion of an accessioning session, or after the last one of the day, you may want to print the Log and Histopathology Worksheet. These can serve as a guide for embedding the next morning, since the specimen submitted is listed, as well as any comment made during accessioning.

After a month of entering data for cytologies and/or surgical is complete (i.e., there are no incompletes), the log for the month can be printed. By printing it at this time, it will contain the diagnoses of each case with the surgeon and pathologist listed, as well as person releasing the report. Until the permanent monthly log is printed, it might be useful to save the daily logs. Cytologies and autopsies are accessioned/logged-in with similar menus under their respective divisions.

##### B. Data Entry

The SF 515s are delivered to the pathology secretaries with a tape for dictation in the case of the surgicals, or alone in the case of cytologies. The secretary uses the option Gross description/clinical hx in the Data Entry option and is able to call up each case by accession number and enter the data from each of the headings at the top of the SF 515. At Gross Description, word-processing fields come up so that transcribing can be done. The screen editor feature may be used with any word processing field. This feature is selectable through the MailMan Menu options. At the completion of gross transcription, there is a prompt for another case. When all the transcriptions are completed, they can be printed. In the Print option, Print All Reports on Queue, select Preliminary Reports. This can be printed double-spaced or single-spaced, depending on your local preferences. Even if you choose double-space, the final report is single-spaced. It also prints out, on a following page, any cytology, surgical, electron microscopy, or autopsy accession(s) on this particular patient, which were previously entered into the system. This function will serve to gradually replace the card index file in the future. This printout is given to the pathologist with corresponding case slides. He will then dictate the microscopic findings and diagnosis. The diagnosis is stored in a separate field from the microscopic findings. If he wants to clarify or add to the gross description, it can be done at this time. When the dictation is complete, the recording media and the reports go to the pathology secretary for final transcription.

The secretary calls up the option Gross Review/Microscopic and SNOMED Coding. At the prompts, the accession number is entered to call up the case. The screen responds with the case and patient identification. The gross is displayed first; therefore, the opportunity exists to edit any changes at this time. The microscopic appears next, permitting transcription from the tape. The pathologist’s free-text diagnosis is entered. There are prompts for the pathologist name and for date completed. The SNOMED coding prompts appear last.

##### C. Final Reports

When all the microscopics with diagnoses are completed, Print All Reports on Queue is called up. Then select Final Reports. Take the default of “NO//” unless you specifically need to print extra copies. For extra file copies and for the Tumor Registrar, the Tissue Committee, etc., the signed copy can be duplicated or a new copy can be generated using the print single report options once it has been verified.

After the reports are signed, they are “released” through the Verify/Release Reports option. The person doing this must have the LRVERIFY key, which functions as the legal electronic signature of the person. The reports may now either be displayed or printed, via the option Pathology Report on a Patient. This option is also installed on the Medical Staff Menu and the Ward and Clinic Clerk Menus.

Health Summary can also access the verified report. Until such time as the report has been released, the message displayed indicates that the report is not verified. There is no other information available unless the patient has had previous completed accessions.

**HINTS:**

1. No detailed formatting is necessary for the final cytology or pathology reports, as far as the LIM is concerned. Each station has its own style of writing a cytology, surgical, autopsy, or electron microscopy report. The “word-processing” mode and the report parameters allow the site to specify the wording for the headers, whether the text should appear in upper or lower case, etc. Instruction regarding the word-processor will be necessary, especially for those who have never used MailMan. Your LIM can be of assistance with this.
2. When it comes to SNOMED coding, do it at the time of entering the microscopic and diagnosis. It will require a bit more attention from the pathologist. However, it will be most helpful to the transcriptionist. By including some of the more common codes on the preliminary report and a spot to record the codes for the case, this can be expedited. See the examples in the Edit Pathology Parameters [LRAPHDR] option. The coded diagnoses are not as descriptive nor elaborate as those dictated for the report, but they are extremely valuable. It is necessary to have both volumes of the CAP SNOMED Coding Manuals and Micro glossary for Surgical Pathology handy to look up some of the diagnoses — the Alphabetical listing is the more frequently consulted. The WKLD SNOMED manuals have the “synonyms” listed, which are not always in the synonym fields of the SNOMED codes supplied. The easiest method is to edit these to include local synonyms as well. It would be a monumental task to review the WKLD manuals and edit in every synonym. A responsible, talented pathology secretary can be most helpful with this editing process. It can also be an educational experience for anyone coding the anatomic reports. Coding is important, since this will look to search your files for a specific group of patients. Unless your station has infinite disk space, you will have to purge word-processing periodically. Initially, you might consider keeping one to two months, plus the current month. When you purge the word-processing, you are left with the name and demographics, accession number and SNOMED codes, and free text diagnosis.
3. There is an option to list the incomplete reports, (Cytology, Surgical Path, Electron Microscopy, and Autopsy), as well as an option to list the Unverified/Unreleased reports. In the Log-in for these sections, there is also a routine Show List of Accessions for a Patient which is rather handy at the time of doing frozen section or OR consults.
4. The Search options are easy to use — consult with your LIM for assistance in queuing times and some of the set-ups. The WKLD SNOMED manuals are necessary for doing this, since you need the code numbers to set your search parameters. Because of the potential impact on system resources, you may want some of the menu options restricted — again your LIM can assist you in this matter. The section entitled “SNOMED Coding/Searches” includes a detailed explanation of the SNOMED search capabilities.

#### Summary of Selected AP Options

To help prevent confusion between the Special Studies and Supplementary Report options, here is a comparison chart:

**Special Studies	Supplementary Report**

Select type of special study	Enter date/time and single (Consult, frozen section, etc.,) free-text field.

Enter ID#, and SNOMED codes	Release supplementary report, “Y” to verify free-text field. (Prompt for verifying only the Supplementary report.)

ID# and SNOMED codes will be displayed	Text deleted when descriptions

on Cum path summary and Log Book	are deleted.

Data is not archived

Reports may be retrieved using AP

Consultation searches and reports or

Search options, Anat path

**TC and QA Codes**

The following summarizes the differences between TC and QA Codes:

**TC Codes		QA Codes**

Numeric TC codes may be assigned	QA codes defined in LAB

description in LAB DESCRIPTIONS file	DESCRIPTIONS file

(Screen = AP SURG)		(Screen = I AP General)

Used to review Surgical cases	Entered for Surgical or Cytopath reports

Supervisor option - Edit QA Site 	Supervisor option- Edit

Parameters to allow TC	QA Site Parameters to allow

code entry	QA code entry

TC code should be entered for each 	QA Codes Entry/edit used to

surgical report	enter QA code for an accession

Use Tissue Committee Review Cases	QA Outcome Review cases

used to retrieve reports	to retrieve reports

### SNOMED Coding/Searches

For these SNOMED coding and searching functions, you must have access to one set of the following WKLD manuals:

1. SNOMED - Systematized Nomenclature of Medicine Vol. I and II
2. SNOMED - Microglossary for Surgical Pathology

Depending on local site factors, you may want more than one copy of one or both of the manuals. These can be obtained from the , .

Description of SNOMED

As part of an effort to standardize the coding of information regarding specific diseases, the Systematized Nomenclature of Medicine was developed. Using the various hierarchically structured systems-oriented axes, it is possible to code all anatomic and physiologic elements of a disease process, both normal and abnormal. Then, sum up these elements as a class of disease or recognized syndrome that has a unique code. For example:

T	+	M	+	E	+	F	=	D

Topography	Morphology		Etiology		Function	Disease

Lung	+	Granuloma	+	M. tuberculosis	+	Fever 	=	Tuberculosis

T-2800		M-44060		E-2001		F-03003		D-0188

With the nomenclature and classification categories, any diagnostic level from a presenting problem, sign or symptom to a complex final, clinical or pathological diagnosis can be appropriately and accurately coded for a patient. The procedure-to-diagnosis relationship will permit medical audit and more specific disease costing.

The two codes most commonly used by pathologists are **topography** and **morphology** . The topography field undertakes to provide a sufficiently detailed and structured nomenclature for those parts of the body whose identification might be needed for coding and retrieval of diagnostic data. The morphology field contains the normal and pathological changes or processes occurring in cells, tissues, or organs.

The AP package comes with the TOPOGRAPHY, MORPHOLOGY, and ETIOLOGY files defined. However, the person doing pathology coding will soon discover that the files are not complete, as there is many code numbers in the codebooks that are not in the file. If a particular topography or morphology doesn’t exist, don’t panic. Just jot down the name you are trying to enter and complete your case entry. You can go back to make the necessary code entries later. Look up the “Microglossary” first, and if not satisfactory, then try Vol. II, the alphabetical list, of the coding Manual, which is comprehensive and has most common synonyms listed. Most of the time you will find it. It will also give the coding number. Now select the option Edit SNOMED files and select the appropriate file (TOPOGRAPHY, MORPHOLOGY, ETIOLOGY, etc.) and enter the code number from your search of the Manual. The chances are that it will show up. Step through the fields until you get to SYNONYM and make your entry. When you go back to the case to code, and re-enter the “problem term,” it will be accepted.

**NOTE:** The apparent speed of the lookups may be slightly confusing. The abbreviation is in the same B cross-reference as the name. The synonyms are in the D cross-reference, which is searched after the B and C cross-references.

If after the search of the Manual, you find the term and code you need, but it isn’t in the computer files, you will be prompted “Are you adding a new name?” and, of course, you are. Perhaps an example will be helpful at this point: Say you have looked in the Manual and find “ carcinoma, metastatic” has the code 81406. When you enter 81406 in the Edit SNOMED Fields option (or using “enter/edit” in FileMan) for the Morphology field you will be prompted, “Are you adding ‘81406’ as a new morphology field (the 3616)?” Answer “YES.” The next prompt is for “Name” which has the code number you entered. Edit this to “adenocarcinoma, metastatic.” The next prompt is for the SNOMED code — enter 81406. The next prompt is “Abbreviation.” The next prompt is “Synonym” and is a multiple field. You may want to enter “metastatic adenocarcinoma.” You can also add “meta adeno” for quick lookup.

When adding to the SNOMED files, it is crucial to use the Manual as the primary reference. If you absolutely cannot find the code you need, you can enter a code that is close but with an identifying letter to indicate it is locally created. Another method is to start with your site station number, followed by three or four digits (including zeros), and write down the number and name in a logbook. Also write the CAP about obtaining an official recommendation about introducing the code. CAP may very well be working on the problem. When an official code is obtained, the locally created code can be changed to the official one. Previously coded cases will reflect the change. Most of your editing will be confined to adding synonyms for easier lookup at the time of coding.

Using SNOMED for Searches

The technique of setting up searches is rather easy. The search routines in each Anatomic section (Cytopathology, Surgical Pathology, Electron Microscopy, and Autopsy) are identical. The searches may be as broad or as specific as desired.

Each SNOMED code has five characters. Generally, each successive digit narrows the specificity of the search. For example, in topography, the **2** 0000 series is for the Respiratory system, **28** 000 is for lung, **282** 00 is for right upper lobe of lung and **2822** 0 is for right upper lobe of lung, posterior segment. Thus, entry of the correct codes is crucial to obtaining the desired output.

Wild cards may be used for any of the SNOMED codes, to broaden the scope of a single search. Entry of wild cards (*) will allow selection of a specific portion of the code, while not requiring all five digits. For example, entry of 8***3 for the morphology code would compile a list of all primary tumors, regardless of type.

**NOTE:** The wild card should only be used if necessary as a “placeholder.” Trailing wild cards should **not** be used, as they will slow down the search. If an asterisk (*) is entered, it will search for that digit to find a match. If nothing is entered for the digit, it will not search that digit at all.

**Example 1:** Listing of all GU tumors in the last two weeks for GU conference.

Topography:	7

Morphology:	8 for all tumors

8***3 for all primary tumors

8***6 for all metastatic tumors

Start with Date: TODAY/ **T-14**

Go  to  Date: TODAY// **&lt;Enter&gt;**

**Example 2:** Listing of all tumors/cancers for the Tumor Registry for both Cytopathology and Surgical Pathology.

Topography:	ALL

Morphology:	8

9

**NOTE:** It might be easier to give the necessary search options to the people handling the Tumor Registry to generate their own listing, since they are responsible for tracking all cancer cases/statistics.

#### Reports

The title “Pathologist”: at the end of Anatomic Pathologist reports has been removed. If you wish to have a title (MD., Ph.D., Hematologist, etc.) appear on the report, it is necessary to make entries in the NEW PERSON file (#200), Provider Class field (#53.5) which points to PROVIDER CLASS file (#7).

##### Frozen Sections

1. There is a separate field for entry of the Frozen Section information. If it is turned on (use the Edit Pathology Parameters [LRAPHDR] option), this field will appear in the log-in and data entry options. If there is any entry in the field, it will be included on the reports. The current capabilities for the reporting system of the module for entering and releasing reports are not conducive to allowing immediate release of the frozen section report. If the gross description and frozen section diagnosis are entered and released immediately in order to meet the CAP standard of providing a written frozen section diagnosis at the time of surgery, then the remainder of the data entry for an “amended report” is available for printing and viewing by physicians. The report has already been released and, therefore, the editorial control has been lost.

Manual systems, such as ones that either overprint the SF 515 with headers for gross impression and frozen section diagnosis or use a miscellaneous clinical lab form, are probably far more easily maintained. These can be used for the written report of the frozen section. The remainder of the specimen can then be processed, the gross and microscopic dictated and the report released.

1. Some consideration should be given as to whether the identity of the person to whom the frozen section report was given and the date/time given should be included on the report. This should be included in the text of the report.

##### Bone Marrows

1. By accessioning the bone marrows, including both the aspirate and the biopsy, all of the functions of the surgical pathology portion of the package can be used. To get a list of the bone marrows for a specified time, select the morphology search option and enter the SNOMED code for the bone marrow (06), enter “ALL” for the morphology prompt and specify the date range.
2. The list provided will include all of the bone marrows within that time, both by patient and by accession number. You can use the topography count option to get a count for a specified time. In addition, the accessions will be included on the Log Book for quick reference. By entering the aspirate and the biopsy as multiple specimens on the same accession number, all of the information can be integrated into a single report.
3. Example 3, in the data entry option Gross Review Microscopic/SNOMED Coding [LRAPDGS] option, shows how a template can be used to standardize the content of the bone marrow report. As noted in that option, the template is controlled by the LAB DESCRIPTION file #62.5.
4. At the time that the gross reports are submitted to the pathologist for microscopic dictation, it might also be helpful to routinely generate a printout of the patient’s most recent peripheral blood counts and other relevant tests that might be helpful in reaching a definitive diagnosis. This can be done using the Enter/Print/Display Preselected Lab Tests [LRUMDA] or by attaching an interim report.

##### Autopsy

1. Provisional Autopsy Diagnosis (PAD) are issued within 24-72 hours of performance of the autopsy. This data can be entered through the appropriate option and released for viewing by the physician if so desired. The Final Autopsy Diagnosis (FAD) is then entered once the microscopic and/or neuropathology description have been completed. Once the report is finalized, it should be released for viewing by the physicians.
2. The autopsy protocol simulates SF 503 (Rev. 2-79) and is designed to be sent to the chart and clinicians with the clinical and pathological diagnoses (final anatomic diagnoses). For a complete report of the autopsy, including gross and microscopic descriptions, the record is kept on file in Laboratory Service. This latter record may be a picture protocol (SF 507) or a text description of the autopsy. If a picture protocol is used, the microscopic description is written alongside the appropriate picture and gross description.

Here is the beginning of the report sent out:

**Example:**

-----------------------------------------------------------------------

CLINICAL RECORD /AUTOPSY PROTOCOL 			          Pg 1
-----------------------------------------------------------------------

Date died: NOV 4, 1986 12:30	/ Autopsy date: NOV 4, 1986
Resident: LABPROVIDER6, EIGHT 	/ TRUNK ONLY (N-146-86)
=======================================================================
Clinical diagnoses:
	Please see attached clinical summary. (The summaries are usually

sent to us by the clinical service)
-----------------------------------------------------------------------
Pathological diagnoses:

I.CARDIOVASCULAR SYSTEM:

A. Congestive Heart Failure
	1. Cardiomegaly (575 gm.)
	2. Hypertrophy, biventricular,
		Left ventricle 1.6 cm
		Right ventricle 0.6 cm.
B. Pericarditis, fibrinous
C. Atherosclerosis
	1. Coronary arteries
...
and so on.

After listing the pathological diagnoses, there is a summary of the case, including the clinical-pathological correlations. The final line of the report is:

COMPLETE AUTOPSY PROTOCOL AVAILABLE IN PATHOLOGY OFFICE

and the patient name, SSN, DOB, and age at death.

Weights that are entered during log-in of autopsy are displayed when a cumulative path report for a patient is requested.

According to the 1989 revisions of M-2 Part VI, Chapter 4, the completed autopsy report should be in the patient’s record within 60 days after the post mortem examination. The format and extent of the gross and microscopic descriptions will depend on local practice, but sufficient information will be included to support the diagnoses rendered on SF 503. Supplemental reports can be issued as necessary.

Some local practices are to provide the “Final Anatomic Diagnoses and Clinical Summary,” followed by a statement that the complete autopsy protocol is available in the Pathology Office. However, any site can enter in the system the entire gross and microscopic descriptions, if desired, since the simulated form is not restricted to a single page. In fact, some of the more interesting cases have been many pages long with much discussion and many references cited.

1. The options Final Autopsy Diagnosis Date [LRAPAUFAD] and Autopsy Data Review [LRAPAURV] expand the module’s ability to provide data for various Quality Assurance monitors. When the autopsy has been completed, the [LRAPAUFAD] option should be used to enter information into two fields, Major Diagnostic Disagreement and Clinical Diagnosis Clarified. In order to obtain information on the percent of deaths on which autopsies are performed, and the number of cases in which the autopsy provided information that either clarified or contradicted the clinical diagnosis, the [LRAPAURV] option can be used. This option searches the patient file for deaths occurring within the specified time. It tallies the number of deaths and the number of autopsies. A report is then generated which also includes the entries for the information entered through [LRAPAUFAD].

Additional QA codes can be assigned using the QA code entry/edit option in the Supervisor’s Menu. An example is provided in the option description of some possible codes for premortem/postmortem correlations.

1. The following reference provides a good explanation of the usefulness of the autopsy for quality assurance:

Schned, Alan R., Mogielnicki, R. Peter, and Stauffer, Marth E;

A comprehensive Quality Assessment Program on the Autopsy Service;

Am J Clin Pathol 86:133-138, 1986.

ANATOMIC PATHOLOGY

MENU OPTIONS

## Anatomic Pathology Menu Options

This section describes and gives examples of most of the options in the Anatomic Pathology module. Options that appear on more than one menu, or generic-type options (e.g., Print SNOMED References or the Search options) may only be described once. At the second occurrence of the option, a reference will be given as to which section to look at for a complete description.

**NOTE:** The **V** *IST* **A** Laboratory Anatomic Pathology User’s Manual released in October, 1994 has been edited to include Appendix B section. The appendix contains file, fields, options changes, and examples created by the release of patch LR*5.2*248.

### Data Entry, Anat Path [LRAPD]

#### Descriptions

**Option	Description**

##### Data entry for Autopsies [LRAPAUDA]

Provisional Anatomic

Diagnoses [LRAPAUPAD]	Allows entering the preliminary autopsy diagnoses.

Autopsy Protocol [LRAPAUDAP]	Allows entry of clinical diagnoses (including operations) and pathological diagnoses for later printing of AUTOPSY PROTOCOL (SF 503).

Autopsy Protocol &amp;

SNOMED Coding [LRAPAUDAB]	Allows entry and editing of autopsy summary and SNOMED codes.

Autopsy Protocol &amp;

ICD Coding [LRAPAUDAA]	Allows entry and edit of autopsy summary and ICD codes.

Final Autopsy Diagnoses

Date [LRAPAUFAD]	Stores date when senior pathologist signs out autopsy. This is when the final diagnoses are made. Includes prompts for MAJOR DIAGNOSTIC DISAGREEMENT (between autopsy &amp; clinical findings) and CLINICAL DIAGNOSIS CLARIFIED.

Autopsy Supplementary

Report [LRAPAUSR]	Allows entry of a supplementary report for an autopsy.

Special Studies, Autopsy	Allows entry of special studies (photography, electron microscopy, immunofluorescence, consultation) for organs or tissues specified.

**Option	Description**

Blocks, Stains, Procedures,

anat Path [LRAPSPDAT]	Allows entry of blocks, stains Surg Path and procedures used in surgical pathology.

##### Coding

SNOMED Coding, Anat Path	Allows entry or edit of the SNOMED codes for any existing Surgical Pathology accession.

ICD Coding, Anat Path	Allows entry or edit of the ICD-CM codes for any existing Anatomic Pathology accession.

Clinical Hx/Gross Description/FS	Enter anatomic pathology specimen gross description and clinical history.

FS/Gross/Micro/Dx

(New name for option)	Enter the microscopic descriptions and diagnosis. Edit the gross tissue description and frozen description.

FS/Gross/Micro/Dx/SNOMED Coding	Allows review of gross specimen

(New name for option)	description, and frozen description entry of microscopic description and diagnoses, and SNOMED coding.

FS/Gross/Micro/Dx/ICD Coding	Allows review of gross specimen

(New name for option)	description, and frozen description entry of microscopic description and ICD-CM coding for each accession number.

Enter Old Anat Path Records	Enter old (non-current) Anat Path reports for reference and historical purposes.

Supplementary Report, Anat Path	Used to add a supplementary report to any existing anatomic pathology accession.

Special Studies-EM;Immuno;Consult

Pic; Anat Path	Used to add a special study report

to an existing anatomic pathology accession.

#### Data Entry for Autopsies [LRAPAUDA]

##### Provisional Anatomic Diagnoses [LRAPAUPAD]

The provisional report is issued within 24-72 hours of the performance of the autopsy. With the exception of the Provisional Anatomic Dx Date, the fields are the same as those, which appear in the Autopsy Protocol [LRAPAUDAP] option. Data that is entered through this option is then edited when the final report is done. It is not stored separately. Once data is entered via this option, the accession is automatically placed in the print queue for autopsy report. By having a separate date field, it allows the issuance of this report to be tracked separately from that of the final report. This field is also used for the calculation of the turnaround time for PADs.

**Example:** Select Data entry, anat path Option: **AU** Data entry for autopsies

Select Data entry for autopsies Option: **PD** Provisional anatomic diagnoses

Data entry for 1992 ? YES// **&lt;Enter&gt;** (YES)

Select Accession Number/Pt name: **4** for 1992

LABPATIENT, TWO ID: 000-00-0002

CLINICAL DIAGNOSES:

1&gt;1. Left CVA

2&gt;2. Recurrent UTI.

3&gt;3. Aspiration pneumonia.

4&gt;

EDIT Option: **&lt;Enter&gt;**

PATHOLOGICAL DIAGNOSES:

1&gt;PROVISIONAL GROSS ANATOMIC PATHOLOGIC DIAGNOSIS (subject to revision):

2&gt;

3&gt;1. Bilateral pulmonary edema with bilateral pleural effusion (500cc)

4&gt;   a. Organizing pneumonia right lung

5&gt;   b. Pericardial effusion

6&gt;   c. Calcified granuloma, left upper lobe

7&gt;

8&gt;2.  a. Moderate arteriosclerosis of abdominal aorta

9&gt;   b. Cardiomegaly with LVH

10&gt;

11&gt;3. Bilateral granular kidneys (areteriolonephrosclerosis)

12&gt;   a. 3 x 2 cm cyst left kidney

13&gt;   b. 0.3 x 0.3 cm hemorrhagic cysts, left kidney

14&gt;   c. Hemorrhagic bladder mucosa

15&gt;

16&gt;4. Cholelithiasis with 25 stones (yellow 0.5 to 1 cm)

17&gt;   a. Congested liver parenchyma

18&gt;   b. Diverticulosis, colon

19&gt;

EDIT Option: **&lt;Enter&gt;**

PROVISIONAL ANAT DX DATE: **T** (NOV 25, 1992)

##### Autopsy Protocol [LRAPAUDAP]

Allows entry of clinical diagnoses (including operations) and pathological diagnoses for later printing of AUTOPSY PROTOCOL (SF 503).

Example:

Select Data entry for autopsies Option: **AP** Autopsy protocol
Data entry for 1990 ? YES// **&lt;Enter&gt;** (YES)

Select Accession Number/Pt name: **2** for 1990
LABPATIENT, ONE ID: 000-00-0001

DATE AUTOPSY REPORT COMPLETED: **7 29** (JUL 29, 1990)

Select AUTOPSY COMMENTS: Carcinoma of right lung// **&lt;Enter&gt;** CLINICAL DIAGNOSES:
	1&gt; **Carcinoma of right lung** 2&gt; **&lt;Enter&gt;** EDIT Option: **&lt;Enter&gt;** PATHOLOGICAL DIAGNOSES:
	1&gt; **I. Respiratory System** 2&gt; **A. Adenocarcinoma, Right Upper Lobe** 3&gt; **B. Atelectasis, Both lower lobes etc.** 4&gt; **&lt;Enter&gt;** EDIT Option: **&lt;Enter&gt;** Select Accession Number/Pt name: &lt;Enter&gt;

**NOTES:**

•	The date completed, not the AUTOPSY RELEASE DATE, is used for calculation of the turn-around-time since the autopsy may be released for viewing after the preliminary diagnosis was completed. Thus, it is not possible to tell from the release date/time whether that reflects the preliminary or the final report.

•	Once the final report is completed, it can be verified/released for viewing via the clinician option.

##### Autopsy Protocol and SNOMED Coding [LRAPAUDAB]

This option allows entry of clinical diagnoses (including operations) and pathological diagnoses and the corresponding SNOMED codes for the tissues and diagnoses.

**Example 1:** No Data Previously Entered for Provisional Report

If you answer “YES” to the “Enter Etiology, Function, Procedure &amp; Disease? NO//” prompt, you will be asked to select Etiology, Function, Procedure, and Disease for each Organ/Tissue.

Select Anatomic pathology Option: **D** Data entry, anat path

Select Data entry, anat path Option: **AU** Data entry for autopsies

Select Data entry for autopsies Option: **AS** Autopsy protocol &amp; SNOMED coding

Enter Etiology, Function, Procedure &amp; Disease? NO// **&lt;Enter&gt;**

Data entry for 1989 ? YES// **&lt;Enter&gt;** (YES)
Select Accession Number/Pt name: **75** for 1989
LABPATIENT, THREE ID: 000-OO-OOO3

Autopsy performed: November 15, 1989 Acc# 75
DATE AUTOPSY REPORT COMPLETED: **11/16** (NOV 16, 1989)
CLINICAL DIAGNOSES:

1&gt; CEREBRAL VASCULAR ACCIDENT

2&gt; **PNEUMONIA**

3&gt; **&lt;Enter&gt;**

EDIT Option: **&lt;Enter&gt;**

PATHOLOGICAL DIAGNOSES:

1&gt; **CARDIOVASCULAR SYSTEM: 1. MODERATE-SEVERE ATHEROSCLEROSIS OF AORTA**

2&gt; **AND LARGE ARTERIES WITH LEFT CAROTID**

3&gt; **ARTERY CALCIFIED BUT PROBE PATENT AT**

4&gt; **BIFURCATION.**

5&gt; **RESPIRATORY SYSTEM: 1. ACUTE BRONCHOPNEUMONIA WITH ABSCESSES** 6&gt; **AND EVIDENCE OF ASPIRATION, ALL RIGHT-SIDED**

7&gt; **LOBES AND LOWER LEFT LOBE.**

8&gt; **2. PULMONARY EMPHYSEMA**

9&gt; **3. CHRONIC BRONCHITIS**

10&gt; **&lt;Enter&gt;** EDIT Option: **&lt;Enter&gt;**

Select AUTOPSY ORGAN/TISSUE: **HEART** 32000

. . . AUTOPSY ORGAN/TISSUE NUMBER: 1// **&lt;Enter&gt;**

Select MORPHOLOGY: **54750** INFARCT,HEALED

Select MORPHOLOGY: **52110** ARTHEROSCLEROSIS

Select MORPHOLOGY: **&lt;Enter&gt;**

Select AUTOPSY ORGAN/TISSUE: **42000** AORTA 42000

AUTOPSY ORGAN/TISSUE NUMBER: 2// **&lt;Enter&gt;**

Select MORPHOLOGY: **52110** ARTHEROSCLEROSIS

Select MORPHOLOGY: **&lt;Enter&gt;**

Select AUTOPSY ORGAN/TISSUE: **&lt;Enter&gt;**

Select Accession Number/Pt name: **&lt;Enter&gt;**

**Example 2:** Finalizing a report for which the provisional report was previously entered.

**NOTES:**

- If the ‘Provisional Anatomical Diagnosis’ report was verified/released for viewing by the clinicians and if the pathologist does not want the final report accessible to the clinicians until that portion has been once again verified/released, it **must** be unreleased prior to entry of the ‘Final Anatomical Diagnosis’ information. This is acceptable for the Autopsy accession area since there is NO chance for adverse patient outcome.
- Prior to the release of patch LR*5.2*248, this was accomplished using the “@” key at the AUTOPSY RELEASE DATE/TIME// prompt in the Verify/release reports, anat path [LRAPR] option.
- With the release of patch LR*5.2*248, the Verify/release reports, anat path [LRAPR] option has been **modified** . Unreleasing the report is now accomplished by answering ‘YES’ to the Unrelease report?// **YES** prompt.

Select Anatomic pathology Option: **D** Data entry, anat path

Select Data entry, anat path Option: **AU** Data entry for autopsies

Select Data entry for autopsies Option: **AS** Autopsy protocol &amp; SNOMED coding

Enter Etiology, Function, Procedure &amp; Disease ? NO// **&lt;Enter&gt;** (NO)

Data entry for 1992 ? YES// **&lt;Enter&gt;** (YES)

Select Accession Number/Pt name: **5** for 1992

LABPATIENT, FOUR ID: 000-00-0004

DATE AUTOPSY REPORT COMPLETED: **T** (DEC 02, 1992)

CLINICAL DIAGNOSES:

1&gt;1. Left CVA

2&gt;2. Recurrent UTI

3&gt;3. Aspiration pneumonia

EDIT Option: **I** nsert after line: 3

4&gt; **4. Chronic renal failure**

5&gt; **&lt;Enter&gt;**

1 line inserted...

EDIT Option: **&lt;Enter&gt;**

PATHOLOGICAL DIAGNOSES:. . .

11&gt;3. Bilateral granular kidneys (arterionephrosclerosis)

12&gt;  a. 3 x 2 cm cyst left kidney

13&gt;  b. 0.3 x 0.3 cm hemorrhagic cysts, left kidney

14&gt;  c. Hemorrhagic bladder mucosa

15&gt;

16&gt;4. Choletlithiasis with 25 stones (yellow, 0.5 to 1 cm)

17&gt;  a. Congested liver parenchyma

18&gt;  b. Diverticulosis, colon

EDIT Option: **l** ist line: 1// **&lt;Enter&gt;** to: 19// **&lt;Enter&gt;**

1&gt;PROVISIONAL GROSS ANATOMIC PATHOLOGICAL DIAGNOSIS: (Subject to revision)

2&gt;

3&gt;1. Bilateral pulmonary edema with bilateral pleural effusion (500cc)

4&gt;   a. Organizing pneumonia right lung

5&gt;   b. Pericardial effusion

6&gt;   c. Calcified granuloma, left upper lobe

7&gt;

8&gt;2. a. Moderate arteriosclerosis of abdominal aorta

9&gt;   b. Cardiomegaly with LVH

10&gt;

11&gt;3. Bilateral granular kidneys (arterionephrosclerosis)

12&gt;   a. 3 x 2 cm cyst left kidney

13&gt;   b. 0.3 x 0.3 cm hemorrhagic cysts, left kidney

14&gt;   c. Hemorrhagic bladder mucosa

15&gt;

16&gt;4. Choletlithiasis with 25 stones (yellow, 0.5 to 1 cm)

17&gt;   a. Congested liver parenchyma

18&gt;   b. Diverticulosis, colon

19&gt;

EDIT Option: **1**

1&gt;PROVISIONAL GROSS ANATOMIC PATHOLOGICAL DIAGNOSIS: (Subject to revision)

Replace **P...P** With **P** Replace **(...** With **&lt;Enter&gt;** Replace **&lt;Enter&gt;**

PATHOLOGICAL DIAGNOSIS:

Edit line: **5**

5&gt;  b. Pericardial effusion

Replace **b....** With **b. Organizing pneumonia, right lung, with acute bronchitis** Replace **&lt;Enter&gt;**

1. Organizing pneumonia, right lung, with acute bronchitis Pericardial effusion

Edit line: **+1** 6

6&gt;  c. Calcified granuloma, left upper lobe

Replace **lobe** With **lobe (gross)** Replace **&lt;Enter&gt;**

c. Calcified granuloma, left upper lobe (gross)

Edit line: **in** sert after line: 6

7&gt; **d. Emphysema (bilateral) and focal atelectasis (left)**

8&gt; **&lt;Enter&gt;**

1 line inserted................

EDIT Option: **list** line: 1// **&lt;Enter&gt;** to: 20// **&lt;Enter&gt;**

1&gt;PATHOLOGICAL DIAGNOSIS:

2&gt;

3&gt;1. Bilateral pulmonary edema with bilateral pleural effusion (500cc)

4&gt;  a. Organizing pneumonia right lung

5&gt;  b. Organizing pneumonia, right lung, with acute bronchitis Pericardial effusion

6&gt;  c. Calcified granuloma, left upper lobe (gross)

7&gt;  d. Emphysema (bilateral) and focal atelectasis (left)

8&gt;

9&gt;2. a. Moderate arteriosclerosis of abdominal aorta

10&gt;  b. Cardiomegaly with LVH

11&gt;

12&gt;3. Bilateral granular kidneys (arterionephrosclerosis)

13&gt;  a. 3 x 2 cm cyst left kidney

14&gt;  b. 0.3 x 0.3 cm hemorrhagic cysts, left kidney

15&gt;  c. Hemorrhagic bladder mucosa

16&gt;

17&gt;4. Choletlithiasis with 25 stones (yellow, 0.5 to 1 cm)

18&gt;  a. Congested liver parenchyma

19&gt;  b. Diverticulosis, colon

20&gt;

EDIT Option: **5**

5&gt;  b. Organizing pneumonia, right lung, with acute bronchitis Pericardial effusion

Replace **P...** With **&lt;Enter&gt;** Replace **&lt;Enter&gt;**

b. Organizing pneumonia, right lung, with acute bronchitis

Edit line: **10**

10&gt;  b. Cardiomegaly with LVH

Replace **galy** With **galy(480 gm)** Replace **LVH** With **left ventricular hypertrophy**

Replace **&lt;Enter&gt;**

b. Cardiomegaly(480 gm) with left ventricular hypertrophy

Edit line: **insert** after line: **10**

11&gt;  c. Pericardial effusion with chronic peritonitis

12&gt;  d. Focal interstitial fibrosis

13&gt;

2 lines inserted.............. *[etc.....]*

EDIT Option: **insert** after line: **23**

24&gt; **&lt;Enter&gt;**

25&gt; **CLINICO-PATHOLOGICAL CORRELATION**

26&gt; **&lt;Enter&gt;**

27&gt; **Patient was an 81 year old Hispanic man ......**

28&gt; **&lt;Enter&gt;**

4 lines inserted......

EDIT Option: **&lt;Enter&gt;**

Select AUTOPSY ORGAN/TISSUE: **28000** LUNG    28000

AUTOPSY ORGAN/TISSUE NUMBER: 1// **&lt;Enter&gt;**

Select MORPHOLOGY: **36660** EDEMA, LYMPHATIC    36660

Select MORPHOLOGY: **32800** EMPHYSEMA    32800

Select MORPHOLOGY: **49000** FIBROSIS    49000

Select MORPHOLOGY: **&lt;Enter&gt;**

Select AUTOPSY ORGAN/TISSUE: **29000** PLEURA    29000

AUTOPSY ORGAN/TISSUE NUMBER: 2// &lt;Enter&gt;

Select MORPHOLOGY: **36300** EFFUSION    36300

Select MORPHOLOGY: **EFFUSION**

MORPHOLOGY: EFFUSION// **36330** EFFUSION, SEROSANGUINEOUS    36330

Select MORPHOLOGY: **&lt;Enter&gt;**

Select AUTOPSY ORGAN/TISSUE: **28100** RIGHT LUNG    28100

AUTOPSY ORGAN/TISSUE NUMBER: 3// **&lt;Enter&gt;**

Select MORPHOLOGY: **40000** INFLAMMATION    40000

Select MORPHOLOGY: **&lt;Enter&gt;**

Select AUTOPSY ORGAN/TISSUE: **28600** LEFT UPPER LOBE OF LUNG     28600

AUTOPSY ORGAN/TISSUE NUMBER: 4// **&lt;Enter&gt;**

Select MORPHOLOGY: **44000** INFLAMMATION, GRANULOMATOUS    44000

Select MORPHOLOGY: **&lt;Enter&gt;**

Select AUTOPSY ORGAN/TISSUE: **71000** KIDNEY    71000

AUTOPSY ORGAN/TISSUE NUMBER: 5// **&lt;Enter&gt;**

Select MORPHOLOGY: **52200** ARTERIOLOSCLEROSIS    52200

Select MORPHOLOGY: **&lt;Enter&gt;**

Select AUTOPSY ORGAN/TISSUE: **57000** GALLBLADDER    57000

AUTOPSY ORGAN/TISSUE NUMBER: 6// **&lt;Enter&gt;**

Select MORPHOLOGY: **30010** LITHIASIS    30010

Select MORPHOLOGY: **&lt;Enter&gt;**

Select AUTOPSY ORGAN/TISSUE: **56000** LIVER    56000

AUTOPSY ORGAN/TISSUE NUMBER: 7// **&lt;Enter&gt;**

Select MORPHOLOGY: **CONGESTION** 36100

Select MORPHOLOGY: **&lt;Enter&gt;**

Select AUTOPSY ORGAN/TISSUE: **670000** COLON    67000

AUTOPSY ORGAN/TISSUE NUMBER: 8// **&lt;Enter&gt;**

Select MORPHOLOGY: **32710** DIVERTICULOSIS    32710

Select MORPHOLOGY: **&lt;Enter&gt;**

Select AUTOPSY ORGAN/TISSUE: **42000** AORTA    42000

AUTOPSY ORGAN/TISSUE NUMBER: 9// **&lt;Enter&gt;**

Select MORPHOLOGY: **52000** ARTERIOSCLEROSIS    52000

Select MORPHOLOGY: **&lt;Enter&gt;**

Select AUTOPSY ORGAN/TISSUE: **33010** MYOCARDIUM    33010

AUTOPSY ORGAN/TISSUE NUMBER: 10// **&lt;Enter&gt;**

Select MORPHOLOGY: **71000** HYPERTROPHY    71000

Select MORPHOLOGY: **&lt;Enter&gt;**

Select AUTOPSY ORGAN/TISSUE: **&lt;Enter&gt;**

##### Autopsy Protocol and ICD Coding [LRAPAUDAA]

This option allows entry of clinical diagnoses (including operations), pathological diagnoses, and the corresponding ICD-CM codes for the pathology diagnoses. If the option doesn’t seem to work correctly, check with your site manager. The ICD-CM globals may not have been loaded (possibly because of space shortages).

Example:

Data entry for 2012 ? YES//  (YES)

Select one of the following:

1     Accession number

2     Unique Identifier (UID)

3     Patient Name

Select one: 1//  Accession number

Enter Accession Number: 2 for 2012

LABPATIENT,ONE          000-00-0001     DOB: Feb 1, 1800

Collection Date: Jun 25, 2012

Acc #: AU 12 2 []

Test(s): AUTOPSY LOG-IN

DATE AUTOPSY REPORT COMPLETED: **7 29** (JUL 29, 2012)
Select AUTOPSY COMMENTS:

CLINICAL DIAGNOSES:
	1&gt; **Carcinoma of right lung** 2&gt; **&lt;Enter&gt;** EDIT Option: **&lt;Enter&gt;** PATHOLOGICAL DIAGNOSES:
	1&gt; **CARDIOVASCULAR SYSTEM: 1. MODERATE-SEVERE ATHEROSCLEROSIS OF AORTA**

2&gt; **AND LARGE ARTERIES WITH LEFT CAROTID**

3&gt; **ARTERY CALCIFIED BUT PROBE PATENT AT**

4&gt; **BIFURCATION** .

5&gt; **RESPIRATORY SYSTEM: 1. ACUTE BRONCHOPNEUMONIA WITH ABSCESSES AND** 6&gt; **EVIDENCE OF ASPIRATION, ALL RIGHT-SIDED**

7&gt; **LOBES AND LOWER LEFT LOBE.**

8&gt; **2. PULMONARY EMPHYSEMA**

9&gt; **3. CHRONIC BRONCHITIS** 10&gt; **&lt;Enter&gt;** EDIT Option: &lt;Enter&gt;

Select AUTOPSY QA CODE:

Select AUTOPSY ICD CODE: **414.0** CORONARY ATHEROSCLEROSIS

. . . OK? YES// **&lt;Enter&gt;**

Select AUTOPSY ICD CODE: **433.1** CAROTID ARTERY OCCLUSION

. . . OK? YES// **&lt;Enter&gt;**

Select AUTOPSY ICD CODE: **513.0** ABSCESS OF LUNG

. . . OK? YES// **&lt;Enter&gt;**

Select AUTOPSY ICD CODE: **&lt;Enter&gt;**

Select Accession Number/Pt name: **&lt;Enter&gt;**

##### Final Autopsy Diagnoses Date [LRAPAUFAD]

When the autopsy has been completed, this option can be used to enter quality assurance information. If additional, more specific QA information is desired, QA codes can be defined in the LAB DESCRIPTIONS file (#62.5) and entered using the QA Codes Entry/Edit [LRAPQACD] option in the Supervisor’s Menu.

**NOTE:** The Final Autopsy Diagnosis Date is not used in the calculation of the turn-around-time.

Example:

Select Data entry, anat path Option: **AU** Data entry for autopsies

Select Data entry for autopsies Option: **AF** Final autopsy diagnoses date

Data entry for 1990 ? YES// **&lt;Enter&gt;** (YES)

Select Accession Number/Pt name: **2** for 1990
LABPATIENT, ONE: 000-00-0001

DATE FINAL AUTOPSY DIAGNOSES: **7 29** (JUL 29, 1990)
MAJOR DIAGNOSTIC DISAGREEMENT: **?** CHOOSE FROM:
			0	NO
			1	YES
MAJOR DIAGNOSTIC DISAGREEMENT: **NO** CLINICAL DIAGNOSIS CLARIFIED: **?** CHOOSE FROM:
			1	YES
			0	NO
			2	CONFIRMED
CLINICAL DIAGNOSIS CLARIFIED: **CONFIRMED** Select Accession Number/ Pt name: **&lt;Enter&gt;**

#### Autopsy Supplementary Report [LRAPAUSR]

**NOTE:** The Autopsy Supplementary Report [LRAPAUSR] option has been **modified** by the release of patch LR*5.2*248. This option now stores the ‘Autopsy Supplementary’ report audit information for any supplementary report that was modified (i.e., date/time the report text was modified, person name modifying the report text, and the original report text before it was modified) after the report had been released.

Based on the need to release the autopsy findings within a 60-day turn-around-time, information obtained from additional studies, such as those of neuropathology, can be added as Supplemental Reports.

Example:

Select Data entry for autopsies Option: **SR** Autopsy supplementary report

Data entry for 1990 ? YES// **&lt;Enter&gt;** Autopsy supplementary report

Select Accession Number/Pt name: **2** for 1990
LABPATIENT, ONE: 000-00-0001

Select SUPPLEMENTARY REPORT DATE: **T** SEP 12, 1990
	DESCRIPTION:
	1&gt; **Examination of brain shows no evidence of metastatic carcinoma.** 2&gt; **&lt;Enter&gt;** EDIT Option: **&lt;Enter&gt;** Select Accession Number/Pt name: **&lt;Enter&gt;**

**NOTES:**

The following ‘Autopsy Supplementary’ report may be generated using the Print Single Report Only [LRAP PRINT SINGLE] option or the Print All Reports on the Print Queue [LRAP PRINT ALL ON QUEUE] option specifying the desired report type.

**The shaded areas shown on the following example indicate modifications made to the report.**

**Example:** ‘Autopsy Supplementary’ report

----------------------------------------------------------------------------

CLINICAL RECORD|				AUTOPSY SUPPLEMENTARY REPORT		Pg 1

----------------------------------------------------------------------------

Date died: APR 26, 1990			|Autopsy date:APR 26, 1990 12:55
Resident: LABPROVIDER, ONE			|FULL AUTOPSY Autopsy No. A90 1
-----------------------------------------------------------------------------

SUPPLEMENTARY REPORT DATE: AUG 10, 1990 10:43

*** MODIFIED REPORT***

(Last modified: APR 26, 1990 12:00		typed by LABUSER, SEVEN

This is an autopsy supplementary report. It is separate from the protocol because there are many instances where the autopsy can be
signed out within the sixty day time limit but the brain exam may not be ready until after the deadline is past. The protocol can be sent to the patient's chart and the supplementary report can later follow without having to reprint the entire autopsy protocol.

SUPPLEMENTARY REPORT DATE: AUG 10, 1990 12:35

There can be as many supplementary reports as desired.

----------------------------------------------------------------------------

Pathologist: LABPROVIDER, TWO					jg| Date SEP 12, 1990

R5ISC								AUTOPSY SUPPLEMENTARY REPORT

LABPATIENT, FIVE		000-00-0005		SEX:M		DOB: FEB 1, 1901

MEDICINE		LABPROVIDER, ONE				AGE AT DEATH: 51

##### Autopsy [LRAPAUDAS]

This option allows entry of special studies (photography, electron microscopy, immunofluorescence, consultation) for organs or tissues specified.

Any additional studies or supplemental information can be entered using either the Special Studies option or the Supplementary Report option. The Supplementary Report offers only the date/time of the report and a single free-text field. Data entered in this field will be deleted when the descriptions are deleted. The Special Studies option is more restrictive in its application; however, data entered is not deleted when descriptions are deleted. It can then be used for searches, etc., at some time in the future. For both options, entry of data will place the report in the final report print queue.

**NOTE:** Armed Forces Institute of Pathology (AFIP) case information can be entered as a Special Study by designating “Consultation” as the type of study.

Example:

Select Data entry, anat path Option: **AU** Data entry for autopsies

Select Data entry for autopsies Option: **SS** Special studies, autopsy

Data entry for 1990 ? YES// **&lt;Enter&gt;** (YES)

Select Accession Number/Pt name: **LABPATIENT, SIX** . 04-27-25  000000006  SC VETERAN

LABPATIENT, SIX. ID: OOO-OO-OOO6 Physician: LABPROVIDER, THREE

DIED JUN 1, 1990

Autopsy performed: JUN 2, 1990 Acc # 5

Select AUTOPSY ORGAN/TISSUE: LUNG// **&lt;Enter&gt;**

AUTOPSY ORGAN/TISSUE: LUNG// **&lt;Enter&gt;**

Select SPECIAL STUDIES: EM// **&lt;Enter&gt;**

DATE: AUG 2,1990// **&lt;Enter&gt;**

ID #: // **15**

DESCRIPTION: **&lt;Enter&gt;**

Select SPECIAL STUDIES: **?**

ANSWER WITH SPECIAL STUDIES

CHOOSE FROM:

1   PHOTOGRAPHY

2   FROZEN SECTION

3   EM

YOU MAY ENTER A NEW SPECIAL STUDIES, IF YOU WISH

CHOOSE FROM:

E  EM

I  IMMUNOFLUORESCENCE

P  PHOTOGRAPHY

C  CONSULTATION

F  FROZEN SECTION

Select SPECIAL STUDIES: **1** P

SPECIAL STUDIES: PHOTOGRAPHY// **&lt;Enter&gt;**

DATE: AUG 11,1986// **&lt;Enter&gt;**

ID #: P789-86// **&lt;Enter&gt;**

DESCRIPTION: **&lt;Enter&gt;**

1&gt;Photographs of lung gram stains

EDIT Option: **&lt;Enter&gt;**

Select SPECIAL STUDIES: **&lt;Enter&gt;**

Select AUTOPSY ORGAN/TISSUE: **&lt;Enter&gt;**

Select Accession Number/Pt name: **&lt;Enter&gt;**

#### Blocks, Stains, Procedures, Anat Path [LRAPSPDAT]

This option allows entry of data related to the blocks and special stains done on any type of pathology specimen.

**NOTE:** If workload is turned on for any of the areas, default data will be entered upon log-in. For details regarding a specific area, please see the Implementation Guide.

##### Surgical Pathology

Under the Surgical Pathology field 8, subfield .012 (specimen), there are 3 subfields:

PARAFFIN BLOCK

PLASTIC BLOCK

FROZEN TISSUE BLOCK

Under each of the above fields, there is a multiple containing STAIN/PROCEDURE, in the name field. This field points to the LABORATORY TEST file (#60).

##### Cytology

For cytology, data can be entered for SMEAR PREP, CELL BLOCK, MEMBRANE FILTER, PREPARED SLIDES, or CYTOSPIN preparation. Under each of these fields, there is a multiple which allows entry of a specific stain(s).

##### Electron Microscopy

For EM, data can be entered for the EPON BLOCKS. Under that subfield, there is a multiple, which allows entry of a specific stain.

##### Autopsy

For autopsy, data can be entered for the PARAFFIN BLOCK. Under that subfield, there is a multiple which allows entry of specific stains.

##### General

In File #60, the only fields which currently are necessary for the Blocks, Stains, Procedures option to function are the name field (.01) and the subscript field (4). The subscript field must be =SP. There are other required fields; however, the information entered plays no role at the current time. See example on the next page.

The information entered through this option is useful for 1) tracking the work performed on each accession via the Display Stains/Blocks for a Patient [LRAPST] option, 2) generating labels via the Anat Path Slide Labels [LRAPLM] option, to be placed on the glass slides used for microscopic examination, or 3) printing using the Accession List with Stains [LRAPSA] option to serve as a workload recording document.

Once specimens have been logged in, the Histopathology Worksheet [LRAPH] option will provide a mechanism for recording what data needs to be entered into the system. The worksheet includes all accessions and all specimens for each accession.

**NOTE:** Some detailed training on how to review/edit the data will be necessary unless the user already has experience in dealing with this option, or other data entry option that involves multiple fields. Dealing with these multiples is not intuitive even to the more experienced user.

##### Example 1:	Routine Data Entry for Surg Path (workload off)

Select Anatomic pathology Option: **DATA ENTRY, ANAT PATH** Select Data entry, anat path Option: **BLOC** ks, Stains, Procedures, anat path

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

			1.	PARAFFIN BLOCK
			2.	PLASTIC BLOCK
			3.	FROZEN TISSUE
Selection (1) : **1** PARAFFIN BLOCK
Selection (2) : &lt;Enter&gt;

Enter year: 1990//

Select Accession Number/Pt name: **22** for 1994

LABPATIENT, SEVEN: 000-00-0007

Date/time blocks prepared/modified: NOW// **&lt;Enter&gt;** (AUG 26, 1994@13:24) OK ? YES// **&lt;Enter&gt;** (YES)

Date/time slides stained: NOW// **&lt;Enter&gt;** (AUG 26, 1994@13:24) OK ? YES// **&lt;Enter&gt;** (YES)

LABPATIENT, SEVEN 0007 Acc #: 24 Date: APR 26, 1994

Slide/Ctrl Last stain/block date

SKIN

Paraffin Block

SKIN       Stain/Procedure            APR 26, 1994 08:00

H &amp; E STAIN            1    APR 26, 1994 08:00

ACID FAST STAIN, HISTOLOGY     1/1   MAY 30, 1994 08:30

PAS WITHOUT DIASTASE        1/1   MAY 30, 1994 08:00

A         Stain/Procedure            APR 26, 1994 08:00

H &amp; E STAIN            1    APR 26, 1994 08:00

PROSTATE CHIPS

Paraffin Block

B         Stain/Procedure            AUG 26, 1994 13:18

H &amp; E STAIN            1    AUG 26, 1994 13:19

A         Stain/Procedure            AUG 26, 1994 13:21

H &amp; E STAIN            1    AUG 26, 1994 13:21

Data displayed ok ? NO// **&lt;Enter&gt;** (NO)

Select SPECIMEN: PROSTATE CHIPS// **&lt;Enter&gt;**

Select SPECIMEN: PROSTATE CHIPS// **&lt;Enter&gt;**

Select PARAFFIN BLOCK ID: A// &lt;Enter&gt;

PARAFFIN BLOCK ID: A// **&lt;Enter&gt;**

DATE/TIME BLOCK PREPARED: AUG 26,1994@13:21// **&lt;Enter&gt;**

Select STAIN/PROCEDURE: H &amp; E STAIN// **&lt;Enter&gt;**

STAIN/PROCEDURE: H &amp; E STAIN// **B**

SLIDES PREPARED (#): 1// **&lt;Enter&gt;**

CONTROL SLIDES (#): **&lt;Enter&gt;**

DATE/TIME SLIDES STAINED: AUG 26,1994@13:21

// **&lt;Enter&gt;**

Select STAIN/PROCEDURE: **&lt;Enter&gt;**

Select PARAFFIN BLOCK ID: **&lt;Enter&gt;**

Select SPECIMEN: **&lt;Enter&gt;**

**NOTES:**

•	At the “Select SPECIMEN: PROSTATE CHIPS//” prompt, a return allows you to enter one to nine characters in a free text field to describe specifics of that block in the Example 1: Levels of myocardium were labeled A and H, etc.

•	Entry of stains/procedures must be done using VA FileMan. Entry of the stains into File #60 should be done using the FileMan option one. The entry for “H &amp; E STAIN” prompt must be exact in the name field in order for the data entry option to work for the default displayed. Since this stain is performed routinely on all surgical pathology specimens, the default has been included to expedite data entry.

##### Example 2:	Routine Data Entry for Surgical Pathology Frozen Section

Select Anatomic pathology Option: **D** Data entry, anat path

Select Data entry, anat path Option: **BS** Blocks, Stains, Procedures, anat

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

1. PARAFFIN BLOCK

2. PLASTIC BLOCK

3. FROZEN TISSUE BLOCK

Selection (1): **3** FROZEN TISSUE BLOCK

Selection (2): **&lt;Enter&gt;**

Enter year: 1994// **&lt;Enter&gt;** ( 1994) 1994

Select Accession Number: **24** for 1994

LABPATIENT, EIGHT ID: 000-00-0008

Date/time blocks prepared: NOW// **&lt;Enter&gt;** (AUG 26, 1994@08:01) OK ? YES// **&lt;Enter&gt;** (YES)

Date/time slides stained: NOW// **&lt;Enter&gt;** (AUG 26, 1994@08:01) OK ? YES// **&lt;Enter&gt;** (YES)

LABPATIENT, EIGHT 0008 Acc #: 24 Date: AUG 26, 1994

Slide/Ctrl Last stain/block date

LYMPH NODE

Paraffin Block

LYMPH NOD     Stain/Procedure

H &amp; E STAIN          1

Data displayed ok ? NO// **&lt;Enter&gt;** (NO)

Select SPECIMEN: LYMPH NODE// **&lt;Enter&gt;**

Select FROZEN TISSUE ID: **FS1**

DATE/TIME FROZEN PREPARED: AUG 26,1994@08:01// **&lt;Enter&gt;** (AUG 26, 1994@08:01)

FROZEN TISSUE BLOCK TYPE: **??**

Entry indicates if the frozen tissue block is used for rush

(rapid) diagnosis or routinely processed (not rush).

CHOOSE FROM: **&lt;Enter&gt;**

1    RUSH

0    NOT RUSH

FROZEN TISSUE BLOCK TYPE: **RUSH**

Select STAIN/PROCEDURE: FROZEN SECTION H &amp; E// &lt;Enter&gt;

SLIDES PREPARED (#): 1// **&lt;Enter&gt;**

CONTROL SLIDES (#): **&lt;Enter&gt;**

DATE/TIME SLIDES STAINED: AUG 26,1994@08:01// **&lt;Enter&gt;** (AUG 26, 1994@08:01)

Select STAIN/PROCEDURE: **&lt;Enter&gt;**

Select FROZEN TISSUE ID: **FS2**

DATE/TIME FROZEN PREPARED: AUG 26,1994@08:01// **&lt;Enter&gt;** (AUG 26, 1994@08:01)

FROZEN TISSUE BLOCK TYPE: **RUSH**

Select STAIN/PROCEDURE: FROZEN SECTION H &amp; E// &lt;Enter&gt;

SLIDES PREPARED (#): 1// **&lt;Enter&gt;**

CONTROL SLIDES (#): **&lt;Enter&gt;**

DATE/TIME SLIDES STAINED: AUG 26,1994@08:01// **&lt;Enter&gt;** (AUG 26 1994@08:01)

Select FROZEN TISSUE ID: **FS3**

DATE/TIME FROZEN PREPARED: AUG 26,1994@08:01// **&lt;Enter&gt;** (AUG 26, 1994@08:01)

FROZEN TISSUE BLOCK TYPE: **RUSH**

Select STAIN/PROCEDURE: FROZEN SECTION H &amp; E// &lt;Enter&gt;

SLIDES PREPARED (#): 1// **&lt;Enter&gt;**

CONTROL SLIDES (#): **&lt;Enter&gt;**

DATE/TIME SLIDES STAINED: AUG 26,1994@08:01// **&lt;Enter&gt;** (AUG 26, 1994@08:01)

Select STAIN/PROCEDURE: **&lt;Enter&gt;**

Select FROZEN TISSUE ID: **&lt;Enter&gt;**

Select SPECIMEN: **&lt;Enter&gt;**

LABPATIENT, EIGHT 0008 Acc #: 24 Date: AUG 26, 1994

Slide/Ctrl Last stain/block date

LYMPH NODE

Paraffin Block

LYMPH NOD     Stain/Procedure

H &amp; E STAIN        1

Frozen Tissue

FS1        Stain/Procedure       AUG 26, 1994 08:01

FROZEN SECTION H &amp; E   1    AUG 26, 1994 08:01

FS2        Stain/Procedure       AUG 26, 1994 08:01

FROZEN SECTION H &amp; E   1    AUG 26, 1994 08:01

FS3        Stain/Procedure       AUG 26, 1994 08:01

FROZEN SECTION H &amp; E   1    AUG 26, 1994 08:01

Data displayed ok ? NO// **Y** (YES)

**NOTE** :	If you then print labels through the Anat Path Slide Labels [LRAPLM] option, you will get three labels, as follows:

SURG	SURG	SURG

94-22	94-22	94-22

FS1	FS2	FS3

H&amp;E	H&amp;E	H&amp;E

VAMC513	VAMC513	VAMC513

##### Example 3:	Editing Data for Cytology

##### (data already entered based on workload profiles)

Select Anatomic pathology Option: **D** Data entry, anat path

Select Data entry, anat path Option: **BS** Blocks, Stains, Procedures

Select ANATOMIC PATHOLOGY section: **CY** CYTOPATHOLOGY

1. SMEAR PREP

2. CELL BLOCK

3. MEMBRANE FILTER

4. PREPARED SLIDES

5. CYTOSPIN

Selection (1): 1 SMEAR PREP

Selection (2): 2 CELL BLOCK

Selection (3): **&lt;Enter&gt;**

Enter year: 1994// **&lt;Enter&gt;** (1994) 1994

Select Accession Number: **5** for 1994

LABPATIENT, NINE ID: 000-00-0009

Date/time slides stained: NOW// **&lt;Enter&gt;** (AUG 26, 1994@14:13) OK ? YES// **&lt;Enter&gt;** (YES)

LABPATIENT, NINE 0009 Acc #: 5 Date: AUG 26, 1994

Slide/Ctrl Last stain date

BRONCHIAL WASHING CYTOLOGY

Smear Prep

SMEAR PRE     Stain/Procedure

PAP STAIN, SMEAR PREP   	2    AUG 26, 1994 14:13

Cell Block

CELL BLOC     Stain/Procedure

H &amp; E STAIN        	1    AUG 26, 1994 14:13

Data displayed ok ? NO// **&lt;Enter&gt;** (NO)

Select SPECIMEN: BRONCHIAL WASHING CYTOLOGY// **&lt;Enter&gt;**

Select SMEAR PREP: SMEAR PRE// **&lt;Enter&gt;**

SMEAR PREP: SMEAR PRE// **&lt;Enter&gt;**

Select STAIN/PROCEDURE: PAP STAIN, SMEAR PREP

// **&lt;Enter&gt;**

STAIN/PROCEDURE: PAP STAIN, SMEAR PREP// **&lt;Enter&gt;**

SLIDES PREPARED (#): 2// **4**

CONTROL SLIDES (#): **&lt;Enter&gt;**

DATE/TIME SLIDES STAINED: AUG 26,1994@14:13

// **&lt;Enter&gt;**

Select STAIN/PROCEDURE: **&lt;Enter&gt;**

Select SMEAR PREP: **&lt;Enter&gt;**

Select CELL BLOCK: CELL BLOC// **&lt;Enter&gt;**

CELL BLOCK: CELL BLOC// **&lt;Enter&gt;**

Select CELL BLOCK STAIN: H &amp; E STAIN// **&lt;Enter&gt;**

CELL BLOCK STAIN: H &amp; E STAIN// **&lt;Enter&gt;**

SLIDES PREPARED (#): 1// **2**

CONTROL SLIDES (#): **1**

DATE/TIME SLIDES STAINED: AUG 26,1994@14:13

// **N** (AUG 26, 1994@14:14)

Select CELL BLOCK STAIN: **&lt;Enter&gt;**

Select CELL BLOCK: **&lt;Enter&gt;**

Select SPECIMEN: **&lt;Enter&gt;**

LABPATIENT, NINE 0009 Acc #: 5 Date: AUG 26, 1994

Slide/Ctrl Last stain date

BRONCHIAL WASHING C

Smear Prep

SMEAR PRE     Stain/Procedure

PAP STAIN, SMEAR PREP     4    AUG 26, 1994 14:13

Cell Block

CELL BLOC     Stain/Procedure

H &amp; E STAIN          2/1   AUG 26, 1994 14:14

Data displayed ok ? NO// **Y** (YES)

**NOTE:** Based on this data, you will get seven labels using the Anat Path Slide Labels [LRAPLM] option, as follows:

CY    	CY    	CY    	CY    	CY    	CY

94-5   	94-5   	94-5   	94-5   	94-5   	94-5

SMEAR PRE  SMEAR PRE	SMEAR PRE	SMEAR PRE	CELL BLOC	CELL BLOC

H &amp; E   	H &amp; E   	H &amp; E   	H &amp; E   	H &amp; E   	H &amp; E

VAMC578  	VAMC578  	VAMC578  	VAMC578  	VAMC578  	VAMC578

CY    	CY    	CY    	CY    	CY    	CY

94-5

CELL BLOC

H &amp; E

VAMC578  	VAMC578  	VAMC578  	VAMC578  	VAMC578  	VAMC578

The 3rd line of the label defaults to the preparation technique. If you wish to have the specimen appear on the label, the default should be edited, rather than accepting the default as has been done in this example.

##### Example 4:	Data Entry for EM

Select Anatomic pathology Option: **D** Data entry, anat path

Select Data entry, anat path Option: **BS** Blocks, Stains, Procedures, anat path

Select ANATOMIC PATHOLOGY section: EM

Enter year: 1992// **&lt;Enter&gt;** ( 1992) 1992

Select Accession Number: **7** for 1992

LABPATIENT, TEN ID: 000-00-0010

Date/time blocks prepared: NOW// **&lt;Enter&gt;** (JAN 13, 1992@10:34)

OK ? YES// **&lt;Enter&gt;** (YES)

Date/time sections prepared: NOW// **&lt;Enter&gt;** (JAN 13, 1992@10:34)

OK ? YES// **&lt;Enter&gt;** (YES)

LABPATIENT, TEN 0010 Acc #: 7 Date: JAN 13, 1992

Count   Last section/block date

KIDNEY

Epon Block

EPON 1      Stain/Procedure        JAN 13, 1992  10:34

GRID EM          5    JAN 13, 1992  10:34

THICK SECTION EM      2    JAN 13, 1992  10:34

Data displayed ok ? NO// **Y** (YES)

##### Example 5:	Date/Times are not in Sequence

Select Anatomic pathology Option: **D** Data entry, anat path

Select Data entry, anat path Option: **Blocks** , Stains, Procedures, anat path

Select ANATOMIC PATHOLOGY section: EM

Enter year: 1992// **&lt;Enter&gt;** ( 1992) 1992

Select Accession Number: **3** for 1992

LABPATIENT1, ONE ID: 000-00-0011

Date/time blocks prepared: NOW// **T@3A** (JAN 08, 1992@03:00) OK ? YES// **&lt;Enter&gt;**

Date/time must not be before date/time specimen received

(JAN 08, 1992@14:50)

Select Accession Number: **3** for 1992

LABPATIENT1, ONE ID: 000-00-0011

Date/time blocks prepared: NOW// **T@1451** (JAN 08, 1992@14:51) OK ? YES// **&lt;Enter&gt;**

Date/time slides/grids prepared: NOW// **&lt;Enter&gt;** (JAN 08, 1992@14:51)

OK ? YES// **N** (NO)

Date/time slides/grids prepared: NOW// **T@1450** (JAN 08, 1992@14:50)

OK ? YES// **&lt;Enter&gt;** (YES)

Date/time must not be before date/time blocks prepared

(JAN 08, 1992@14:51).

Select Accession Number: **3** for 1992

LABPATIENT1, ONE ID: 000-00-0011

Date/time blocks prepared: NOW// **T@1450** (JAN 08, 1992@14:50) OK ? YES// **&lt;Enter&gt;**

Date/time slides/grids prepared: NOW// **&lt;Enter&gt;** (JAN 08, 1992@14:52)

OK ? YES// **&lt;Enter&gt;**

LABPATIENT1, ONE ID:0011 Acc #: 3 Date: JAN 8, 1992

Count  Last stain/block date

KIDNEY

Epon Block

EPON 1      Stain/Procedure       JAN 8, 1992 14:50

GRID EM           5  JAN 8, 1992 14:52

THICK SECTION EM      2  JAN 8, 1992 14:52

Data displayed ok ? NO// **Y** (YES)

Select Accession Number: **&lt;Enter&gt;**

Select Data entry, anat path Option: **&lt;Enter&gt;**

##### Example 6:	More than one Specimen

Select Anatomic pathology Option: **DATA ENTRY** , anat path

Select Data entry, anat path Option: **BLOCKS** , Stains, Procedures, anat path

Select ANATOMIC PATHOLOGY section: EM

Enter year: 1992// **&lt;Enter&gt;** ( 1992) 1992

Select Accession Number: **8** for 1992

LABPATIENT1, TWO ID: 000-00-0012

Date/time blocks prepared: NOW// **&lt;Enter&gt;** (JAN 13, 1992@10:39) OK ? YES// **&lt;Enter&gt;** (YES)

Date/time sections prepared: NOW// **&lt;Enter&gt;** (JAN 13, 1992@10:39) OK ? YES// **&lt;Enter&gt;** (YES)

LABPATIENT1, TWO 0012 Acc #: **8** Date: JAN 13, 1992

Count   Last section/block date

SKIN

Epon Block

EPON 1      Stain/Procedure

JAN 13, 1992 10:39

GRID EM             5    JAN 13, 1992 10:39

THICK SECTION EM        2    JAN 13, 1992 10:39

KIDNEY

Epon Block

EPON 1      Stain/Procedure          JAN 13, 1992 10:39

GRID EM             5    JAN 13, 1992 10:39

THICK SECTION EM        2    JAN 13, 1992 10:39

Data displayed ok ? NO// **Y** (YES)

#### Coding, Anat Path [LRAPCODE]

##### SNOMED Coding, Anat Path [LRAPX]

Although SNOMED coding is usually entered at the time the diagnosis is entered, it may be necessary to enter codes at a later time.

**Example:** Select Anatomic pathology Option: **D** Data entry, anat path

Select Data entry, anat path Option: **CO** Coding, anat path

Select Coding, anat path Option: **SN** SNOMED coding, anat path

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

Enter Etiology, Function, Procedure &amp; Disease ? NO// **&lt;Enter&gt;** (NO)
Data entry for 1990 ? YES// **&lt;Enter&gt;** (YES)

Select Accession Number/Pt name: **LABPATIENT, ONE** 05-08-16 000000001
LABPATIENT, SEVEN ID: 000-00-0007
AGE: 72 DATE OF BIRTH: MAY 8, 1916
PATIENT LOCATION: 1A// &lt;Enter&gt;

Specimen(s)	Count #	Accession #	Date

SKIN	(1)	23	NOV 21, 1988 not verified
	(2)	22	NOV 20, 1988
PROSTATE CHIPS
	(3)	22	JUN 4, 1986
	(4)	567	APR 5, 1982

More accessions ? NO// **&lt;Enter&gt;** (NO)
		Choose Count #(1-4): **3** Accession #: 22 Date: JUN 4, 1990

DATE REPORT COMPLETED: JUN 4,1986// **&lt;Enter&gt;** Select ORGAN/TISSUE: **SKIN** ORGAN/TISSUE: SKIN// **&lt;Enter&gt;** Select MORPHOLOGY: **PSORIASIS** MORPHOLOGY: PSORIASIS// **&lt;Enter&gt;** Select MORPHOLOGY: **&lt;Enter&gt;** Select ORGAN/TISSUE: **&lt;Enter&gt;** Select Accession Number/Pt name: **&lt;Enter&gt;** Select Coding, anat path Option: &lt;Enter&gt;

**NOTE:** At the “Enter Etiology, Function, Procedure &amp; Disease ? NO//” prompt, a Y for “YES” allows you to enter etiology, procedure, or Disease codes.

##### ICD Coding, Anat Path [LRAPICD]

Use this option to enter or edit only the ICD-CM codes for the tissues of any existing accession. If this option doesn’t seem to work correctly, check with your site manager. The ICD-CM globals may not have been loaded (possibly because of space shortages).

Example:

Select Anatomic pathology Option: **D** Data entry, anat path

Select Data entry, anat path Option: **CO** Coding, anat path

Select Coding, anat path Option: **SN** ICD coding, anat path

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

          SURGICAL PATHOLOGY (SP)

Data entry for 2012 ? YES//  (YES)

Select one of the following:

1     Accession number

2     Unique Identifier (UID)

3     Patient Name

Select one: 1//  Accession number

Enter Accession Number/Pt name: **22** LABPATIENT, SEVEN 05-08-16 000000007

Specimen(s):

BRONCH BRUSHINGS

DATE REPORT COMPLETED: JUN 4,2012// &lt;Enter&gt;

Select ICD DIAGNOSIS: **491.2** OBSTRUCT CHR BRONCHITIS
	. . .OK? YES// **NO**

Select ICD DIAGNOSIS: **491.9** CHRONIC BRONCHITIS
. . .OK? YES// **&lt;Enter&gt;**

Select ICD DIAGNOSIS: **&lt;Enter&gt;**

Enter Accession Number/Pt name: **&lt;Enter&gt;** Select Coding, anat path Option: &lt;Enter&gt;

#### Clinical HX/Gross Description [LRAPDGD]

Data entry in this option has been designed to mimic the information on the SF 515. During the log-in process, the specimen entry was an exact match for an entry in the LAB DESCRIPTIONS file (#62.5). The text entered in File #62.5 was thus stuffed into the Gross Description field for editing as shown below.

If the initials of the specific pathologist were included as part of the name, the specimen can then be edited to delete those initials. The gross description which was stuffed from File #62.5 during the log-in will be displayed for editing. By using the edit option, entering an asterisk (*) at the “Replace” prompt, and the correct information at the “With” prompt, the entry process is greatly expedited. If the screen editor is on, then replacing the asterisk becomes very simple.

**NOTES:**

•	For both the Gross Description and the Microscopic Description word-processing fields, the text entered will automatically wordwrap unless a &lt;Enter&gt; and a space are entered. The maximum length of a line is 255 characters. When data is first entered, it calculates the line length, based on the 255 character limit. If you wish to use the &lt;Enter&gt; to control the appearance of the text on the screen, you may do so. However, when the report is printed, it will wordwrap and recalculate the lines. In order to prevent this, such as for a listing, you will need to enter at least one space at the beginning of the line. A space at the beginning of a line prevents that line from being joined to the one before it.

•	In order to make editing of the gross description or microscopic description easier, enter “P” for print at the “Edit option” prompt. If you then request line numbers and a rough draft, word-processing text will print accordingly. If you enter “L” for List instead, it will list the text by line number on the screen, but will not provide the choice of a device.

•	Sometimes you will try to enter a gross description for a specimen which was already logged in and the system will not accept the accession at the “Select Accession” prompt, yet it is obvious that the specimen was logged in with that number assigned. Probably the specimen was logged in using the option designed to enter old data and was not put in the accession file. You will need to go through the regular log-in process, select the same accession, and when the system indicates that it is in the patient file, but not in the accession file, indicate that you wish to add it to the accession file.

•	The screen editor (from the new version of MailMan) can be used for any word processing field. Please consult your LIM on how to turn this feature on.

##### Example 1:	Entry of Information for a Surgical Pathology/

##### ASK FROZEN SECTION set to NO


```vista
Select Anatomic pathology Option: **D** Data entry, anat path
Select Data entry, anat path Option: **GD** Clinical Hx/Gross Description/FS
Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY
```
Data entry for 1988 ? YES// **&lt;Enter&gt;** (YES)
Select Accession Number/Pt name: **22** for 1988
LABPATIENT, SEVEN ID: 000-00-0007
Specimen(s):PROSTATE CHIPS
Select SPECIMEN: PROSTATE CHIPS// **&lt;Enter&gt;** SPECIMEN: PROSTATE CHIPS// **&lt;Enter&gt;** Select SPECIMEN: **&lt;Enter&gt;** BRIEF CLINICAL HISTORY:
	1&gt; **Nocturia and difficulty voiding urine.** 2&gt; **&lt;Enter&gt;** EDIT Option: **&lt;Enter&gt;** PREOPERATIVE FINDINGS:
	1&gt; **Same** . 
	2&gt; **&lt;Enter&gt;** EDIT Option: **&lt;Enter&gt;**

OPERATIVE FINDINGS:
	1&gt; **SAme** .

2&gt; **&lt;Enter&gt;**

Edit line: 1
	Replace **A &lt;Enter&gt;** With **a &lt;Enter&gt;** Replace **&lt;Enter&gt;** Same.
Edit line: **&lt;Enter&gt;** EDIT Option: **&lt;Enter&gt;** POSTOPERATIVE DIAGNOSIS:
	1&gt; **Same** . 
	2&gt; **&lt;Enter&gt;** EDIT Option: **&lt;Enter&gt;**

RESIDENT PATHOLOGIST: **LABPROVIDER, FOUR.** GROSS DESCRIPTION:
	1&gt;Specimen consists of * grams of prostate gland tissue.
EDIT Option: **1** 1&gt;Specimen consists of * grams of prostate gland tissue.
	Replace *** &lt;Enter&gt;** With **25 &lt;Enter&gt;** Replace **&lt;Enter&gt;** Specimen consists of 25 grams of prostate gland tissue.
Edit line: **&lt;Enter&gt;** EDIT Option: **&lt;Enter&gt;**

Select Accession Number/Pt name: **&lt;Enter&gt;**

##### Example 2:	Entry of Information for a Surgical Pathology Specimen with a

##### Frozen Section ASK FROZEN SECTION set to YES


```vista
Select Anatomic pathology Option: **D** Data entry, anat path
Select Data entry, anat path Option: **GD** Clinical Hx/Gross Description/FS
Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY
```

Data entry for 1992 ? YES// **&lt;Enter&gt;** (YES)

Select Accession Number/Pt name: **26** for 1992

LABPATIENT1, THREE ID: 000-00-0013

Specimen(s):

LEFT NOSE BIOPSY

Select SPECIMEN: LEFT NOSE BIOPSY// **&lt;Enter&gt;**

SPECIMEN: LEFT NOSE BIOPSY// **&lt;Enter&gt;**

Select SPECIMEN: **&lt;Enter&gt;**

BRIEF CLINICAL HISTORY:

1&gt; **Exc  BCC**

2&gt; **&lt;Enter&gt;**

EDIT Option: **&lt;Enter&gt;**

PREOPERATIVE DIAGNOSIS:

1&gt; **BCC**

2&gt; **&lt;Enter&gt;**

EDIT Option: **&lt;Enter&gt;**

OPERATIVE FINDINGS:

1&gt; **same**

2&gt; **&lt;Enter&gt;**

EDIT Option: **&lt;Enter&gt;**

POSTOPERATIVE DIAGNOSIS:

1&gt; BCC

RESIDENT PATHOLOGIST: **LABPROVIDER, FIVE**

GROSS DESCRIPTION:

1&gt; **SCO a round skin biopsy measuring 1 x 1 x 0.5 cm. There is an ill**

2&gt; **defined depressed central lesion. A suture marks the superior margin**

3&gt; **which is inked in red. Inferior margin is inked in green, anterior blue**

4&gt; **and posterior uninked. Representative sections embedded.**

EDIT Option: **&lt;Enter&gt;**

FROZEN SECTION:

1&gt; **, adequately excised.**

2&gt; **Reported to LABPROVIDER, ONE at x2420 at 10:55AM.**

EDIT Option: **&lt;Enter&gt;**

Select Accession Number/Pt name: **&lt;Enter&gt;**

#### FS/Gross/Micro/Dx [LRAPDGM]

Use this option to enter just the microscopic descriptions and edit the gross tissue descriptions if necessary. If you enter a specimen name in the Log-in option, the Gross Description field in this option will be automatically filled with an expanded specimen description from the specimen description file.

The LAB DESCRIPTIONS file (#62.5) can also be useful for rapid entry of microscopic descriptions if the pathologists can agree on a standardized text for some of the “*” (name as it appears in File #62.5), &lt;Enter&gt; at line one, &lt;Enter&gt; at line two and at the edit option. This will stuff the SPECIMEN DESCRIPTION into the Microscopic Description field for that specimen.

If some editing is required, you will need to re-enter the accession # at the next “Select Accession Number/Pt. name” prompt. When the microscopic description is redisplayed the text that was copied from File #62.5, can be edited.

**NOTE:** Inclusion of the Frozen Section and Surgical Pathology Diagnosis fields in the edit template is controlled through the Edit Pathology Reports Parameters [LRAPHDR] option in the Supervisors Menu.

**HINTS:**

1. Use of the space bar and &lt;Enter&gt; will not expedite this process because it will only bring back the same patient and ask you to choose from a list of accessions for that patient.
2. This is **only** useful for entry of a SINGLE microscopic finding. If multiple specimens are submitted for which more than one micro must be entered, it may either be done manually OR use “* (name)” for the first, complete the remaining prompts and re-enter the accession number to add the remainder of the microscopic description
3. You can identify cases requiring review by the Tissue Committee by adding the “TC Code” prompt. Use the Edit QA Site Parameters option if you wish to include this prompt in this edit template.

**Example 1:** Entry of Information for a Cytopathology Specimen

Select Data entry, anat path Option: **GM** FS/Gross/Micro/Dx

Select ANATOMIC PATHOLOGY section: **CY** CYTOPATHOLOGY

Data entry for 1990 ? YES// **&lt;Enter&gt;** (YES)

Select Accession Number/Pt name: **23**

LABPATIENT1, FOUR ID: 000-00-0014

Specimen(s)

SPUTUM

GROSS DESCRIPTION:

1&gt; **10cc of tan viscous material submitted**

MICROSCOPIC EXAM/DIAGNOSIS:

1&gt; **Glomerular basement membranes are thickened and there is increased**

2&gt; **mesangial matrix.**

3&gt; **&lt;Enter&gt;**

CYTOTECH: **LABPROVIDER, SIX**

PATHOLOGIST: **LABPROVIDER, SEVEN**

DATE REPORT COMPLETED: TODAY// **&lt;Enter&gt;** (DEC 01, 1989)

REVIEWED BY PATHOLOGIST: **YES**

Select Accession Number/Pt name: **&lt;Enter&gt;**

**Example 2:** Entry of Information for a Surgical Pathology Specimen with a Frozen Section

Select Data entry, anat path Option: **GM** FS/Gross/Micro/Dx

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

Data entry for 1992 ? YES// **&lt;Enter&gt;** (YES)

Select Accession Number/Pt name: **26** for 1992

LABPATIENT1, FIVE: 000-00-0015

Specimen(s):

LEFT NOSE BIOPSY

FROZEN SECTION:

1&gt;, adequately excised.

2&gt;Reported to LABPROVIDER, SEVEN at x2420 at 10:55AM.

EDIT Option: **&lt;Enter&gt;**

GROSS DESCRIPTION:

1&gt;SCO a round skin biopsy measuring 2 1 x 1 x 0.5 cm. There is an ill

2&gt;defined depressed central lesion. A surface suture marks the superior

3&gt;margin which is inked in red. Inferior margin is inked in green,

4&gt;anterior blue and posterior uninked. Representative sections embedded.

5&gt; **&lt;Enter&gt;**

EDIT Option: **&lt;Enter&gt;**

MICROSCOPIC EXAM/DIAGNOSIS:

1&gt; **Residual basal cell carcinoma in biopsy site. Adequately excised. See**

2&gt; **also S92-16.**

3&gt; **&lt;Enter&gt;**

EDIT Option: **&lt;Enter&gt;**

PATHOLOGIST: LABPROVIDER, EIGHT// **&lt;Enter&gt;**

DATE REPORT COMPLETED: **T** (DEC 03, 1992)

TC CODE: **1** 1

#### FS/Gross/Micro/DX/SNOMED Coding [LRAPDGS]

Once the pathologist dictates the microscopic description or frozen section description and returns the preliminary report, the data can be entered. The gross description appears first, providing an opportunity to make any necessary changes noted in the preliminary report. The diagnosis appears last.

For all the word-processing fields, the text entered will automatically word-wrap unless a &lt;Enter&gt; and a space are entered. The maximum length of a word-processing field is 255 characters. When data is first entered, the line length is calculated, based on this limit. If you wish to use the &lt;Enter&gt; to control the appearance of the text on the screen, you may do so. However, when the report is printed, it will word-wrap and recalculate the lines. In order to print this (e.g., for a listing), enter at least one space at the beginning of the line. A space before a character at the beginning prevents that line from being joined to the one before it.

To make editing of the report easier, enter “P” for Print at the “Edit option” prompt. If you then request line numbers and a rough draft, word-processing text will print accordingly. If you enter “L” for List instead, it will list the text by line number on the screen, but will not provide the choice of a device.

The LAB DESCRIPTIONS file (#62.5) can also be useful for rapid entry of microscopic descriptions if the pathologists can agree on a standardized text for some of the more common diagnoses. Entry of (*) followed by the name as it appears in File #62.5 will stuff the SPECIMEN DESCRIPTION into the Microscopic Description field for that specimen. If some editing is required, you will need to reenter the accession # at the next “Select Accession Number/Pt. name” prompt. When the description is redisplayed, the text that was copied from File #62.5 can be edited.

Inclusion of the Frozen Section and/or Surgical Pathology Diagnosis (or Cytopathology, etc.,) fields in the edit template is controlled by the Edit pathology parameters [LRAPHDR] in the Supervisors Menu.

**HINTS:**

1. Use of the space bar and &lt;Enter&gt; will not expedite this process because it will only bring back the same patient and ask you to choose from a list of accessions for that patient.
2. This is only useful for entry of a single microscopic finding. If multiple specimens are submitted for which more than one micro must be entered, you may either be do it manually **or** use “* (name)” for the first, complete the remaining prompts, and re-enter the accession number to add the rest of the microscopic description.
3. You can identify cases requiring review by the Tissue Committee by adding the “TC Code” prompt. Use the Edit QA Site Parameters option if you wish to include this prompt in this edit template. In the example below, the prompt is included.

**NOTES:**

• At the “TC CODE: 1//” prompt, enter numeric between 0 and 9. If a preset description is to be attached to the numeric code and is to be printed on the report generated by the Tissue Committee Review Cases option, this description can be entered into the LAB DESCRIPTIONS file (#62.5). This data is not included on any display or print option other than Tissue Committee Review Cases. It can be edited with the QA Code Entry/Edit option even if the report has been released, to prevent designation of the report as “modified.”

• At the “Select ORGAN/TISSUE:” prompt, enter free text description or SNOMED code. Synonyms can be added for a particular code by using the appropriate edit option. Some topography codes are sex-specific and may not be selected if the patient sex is not appropriate.

• Two or more specimens with exactly the same name can be entered, by enclosing the entry in quotation marks for the second and subsequent specimens.

**Example:**

Select ORGAN/TISSUE: **LIVER** 56000 (SNOMED code appears since it is an identifier)

ORGAN/TISSUE NUMBER: 1// **&lt;Enter&gt;**

The second time around:

Select ORGAN/TISSUE: **“LIVER”**

ORGAN/TISSUE NUMBER: 2// **&lt;Enter&gt;**

To subsequently select one of many of the same entries, choose by ORGAN/TISSUE NUMBER for that particular case (accession).

• For those Surgical Pathology specimens on which EM is being done, entering a comment at the end of the microscopic description to indicate the “EM#-Report to follow” will at least indicate that there will be an electron microscopy and a cross-reference for the SP report will be provided.

• If you wish to enter a disease SNOMED code only, simply enter ^DISEASE at the Morphology prompt to expedite the process.

• If the system doesn’t recognize a MORPHOLOGY (but has accepted a TOPOGRAPHY) when you are entering SNOMED coding, you may have a spelling error, or the entry in the MORPHOLOGY file (#61.1) may be entered differently. You can look it up in the SNOMED coding manual and try to enter the actual code, or have the supervisor check the SNOMED reference file and add a new code if necessary.

**Example 1:** Entry of Information for a routine Surgical Pathology Specimen

Select Data entry, anat path Option: **GS** FS/Gross/Micro/Dx/SNOMED Coding 

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY 
Enter Etiology, Function, Procedure &amp; Disease ? NO// **&lt;Enter&gt;** (NO)
Data entry for 1990 ? YES// **&lt;Enter&gt;** (YES)
Select Accession Number/Pt name: **22** for 1990
LABPATIENT, SEVEN ID: 000-00-0007
Specimen(s) :
PROSTATE CHIPS

GROSS DESCRIPTION:
	1&gt;Specimen consists of 25 grams of prostate gland tissue.
EDIT Option: **&lt;Enter&gt;** MICROSCOPIC EXAM/DIAGNOSIS:
	1&gt; **Prostate gland tissue showing glandular and stromal hyperplasia. In one chip of 134 there is a small focus of well differentiated adenocarcinoma.** 2&gt;&lt;Enter&gt;

EDIT Option: **&lt;Enter&gt;** PATHOLOGIST: LABPROVIDER, THREE// **&lt;Enter&gt;** DATE REPORT COMPLETED: **NOV 20, 1990**

TC CODE: 1// ?

(ENTER: Numeric between 0 and 9.

TC CODE: 1// **&lt;Enter&gt;**

Select ORGAN/TISSUE: **prostate** 77100

ORGAN/TISSUE NUMBER: 1// **&lt;Enter&gt;** WEIGHT (gm): **25** Select MORPHOLOGY : **WDA** ??
	Select MORPHOLOGY: **adenocarcinoma, well** DIFFERENTIATED 814031
	Select MORPHOLOGY : **hyperplasia** 72000
	Select MORPHOLOGY: **&lt;Enter&gt;** Select ORGAN/TISSUE: **&lt;Enter&gt;** Select Accession Number/Pt name: **&lt;Enter&gt;**

##### Example 2:	Entry of Information for a Surgical Pathology Specimen

##### with a Frozen Section

Select Data entry, anat path Option: **GS** FS/Gross/Micro/Dx/SNOMED Coding

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

Enter Etiology, Function, Procedure &amp; Disease ? NO// **Y** (YES)

Data entry for 1992 ? YES// **&lt;Enter&gt;** (YES)

Select Accession Number/Pt name: **26** for 1992

LABPATIENT1, THREE ID: 000-00-0013

Specimen(s):

LEFT NOSE BIOPSY

This accession has a FROZEN SECTION report.

Be sure 'FROZEN SECTION' is entered as a SNOMED code in the PROCEDURE field

for the appropriate organ or tissue.

FROZEN SECTION:

1&gt;, adequately excised.

2&gt;Reported to LABPROVIDER, THREEat x2420 at 10:55AM.

EDIT Option: **&lt;Enter&gt;**

GROSS DESCRIPTION:

1&gt;SCO a round skin biopsy measuring 1 x 1 x 0.5 cm. There is an ill

2&gt;defined depressed central lesion. A suture marks the superior margin

3&gt;whichis inked in red. Inferior margin is inked in green, anterior blue

4&gt;and posterior uninked. Representative sections embedded.

EDIT Option: **&lt;Enter&gt;**

MICROSCOPIC EXAM:

1&gt;Residual basal cell carcinoma in biopsy site. Adequately excised. See

2&gt;also S92-16.

EDIT Option: **&lt;Enter&gt;**

SURGICAL PATH DIAGNOSIS: **BASAL CELL CARCINOMA**

PATHOLOGIST: LABPROVIDER, EIGHT// **&lt;Enter&gt;**

DATE REPORT COMPLETED: DEC 3,1992// **&lt;Enter&gt;**

TC CODE: 1// **&lt;Enter&gt;**

Select ORGAN/TISSUE: **02140** SKIN OF NOSE    02140

ORGAN/TISSUE NUMBER: 1// **&lt;Enter&gt;**

Select MORPHOLOGY: **80903** BASAL CELL CARCINOMA    80903

Select ETIOLOGY: **&lt;Enter&gt;**

Select MORPHOLOGY: **09400** SURGICAL MARGINS FREE OF TUMOR    09400

Select ETIOLOGY: **&lt;Enter&gt;**

Select MORPHOLOGY: **&lt;Enter&gt;**

Select FUNCTION: **&lt;Enter&gt;**

Select PROCEDURE: **1141** BIOPSY, EXCISION    1141

Select PROCEDURE: **3082** FROZEN SECTION     3082

Select PROCEDURE: **&lt;Enter&gt;**

Select DISEASE: **&lt;Enter&gt;**

Select ORGAN/TISSUE: **&lt;Enter&gt;**

##### Example 3:	Using a Template to enter a Bone Marrow Report

Select Data entry, anat path Option: **GS** FS/Gross/Micro/Dx/SNOMED Coding

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

Enter Etiology, Function, Procedure &amp; Disease ? NO// **Y** (YES)

Data entry for 1992 ? YES// **&lt;Enter&gt;** (YES)

Select Accession Number/Pt name: **26** for 1992

LABPATIENT, SEVEN ID: 000-00-0007

Specimen(s):

BONE MARROW

GROSS DESCRIPTION:

1 **&lt;Enter&gt;**

MICROSCOPIC EXAM/DIAGNOSIS:

1&gt; **BONE MARROW**

**NOTE:** enter a “*” followed by the entry name in the LAB DESCRIPTION file (#62.5). Please see the example under Enter/Edit Lab Description file option under the Supervisor Menu.

2&gt; **&lt;Enter&gt;**

EDIT Option: **&lt;Enter&gt;**

After completing the prompts, recall the same accession and you will see the specimen description from the entry in the lab description file in the Microscopic Exam/Diagnosis field:

Select Accession Number/Pt name: **26** for 1992

LABPATIENT, SEVEN ID: 000-00-0007

Specimen(s):

BONE MARROW

GROSS DESCRIPTION:

1 **&lt;Enter&gt;**

MICROSCOPIC EXAM/DIAGNOSIS:

1&gt; **BONE MARROW**

18&gt; DIAGNOSIS: *****

19&gt; **&lt;Enter&gt;**

20&gt; COMMENT: *****

EDIT Option: **E**

EDIT Option: **2**

2&gt; Polys:*

Replace ***** with **8** Replace **&lt;Enter&gt;**

Polys: 8

Edit line: **3**

3&gt; Bands:*

Replace ***** With **0** Replace **&lt;Enter&gt;**

Bands: 0

Edit line: **4**

4&gt; Lymphs:*

Replace ***** With **90** Replace **&lt;Enter&gt;**

Lymphs: 90

Edit line: **5**

5&gt; Monos:*

Replace ***** With **2** Replace **&lt;Enter&gt;**

Monos: 2

Edit line: **6**

6&gt; Eosins:*

Replace ***** With **0** Replace **&lt;Enter&gt;**

Eosins: 0

Edit line: **7**

7&gt; Basos:*

Replace ***** With **0** Replace **&lt;Enter&gt;**

Basos: 0

Edit line: **14**

14&gt;PERIPHERAL BLOOD:*

Replace ***** With **Lymphocytes markedly increased with frequent smudge cells. Lymphocytes maturing with smudged chromatin and only rare nuclei. Platelets adequate.**

Replace **&lt;Enter&gt;**

PERIPHERAL BLOOD: Lymphocytes markedly increased with frequent smudge cells. Lymphocytes maturing with smudged chromatin and only rare nuclei. Platelets adequate.

Edit line: **16**

16&gt;BONE MARROW:*

Replace ***** With **1. Advance lymphoid infiltrate.** Replace **&lt;Enter&gt;**

BONE MARROW: 1. Advanced lymphoid infiltrate.

Edit line: **i** nsert after line: **16**

16&gt; **BONE MARROW: 1. Advanced lymphoid infiltrate.**

17&gt; **2. Decreased cellular elements.**

18&gt; **3. Decreased stainable iron.**

19&gt; **&lt;Enter&gt;**

2 lines inserted.........

EDIT Option: **20**

20&gt;DIAGNOSIS:*

Replace ***** With **Chronic lymphocytic leukemia (see comment) with extensive diffuse bone marrow infiltrate.** Replace **&lt;Enter&gt;**

DIAGNOSIS: Chronic lymphocytic leukemia (see comment) with extensive diffuse bone marrow infiltrate.

EDIT Option: **22**

22&gt;COMMENT:*

Replace ***** With **The bone marrow shows advanced lymphocytic infiltration.**

Replace **&lt;Enter&gt;**

COMMENT: The bone marrow shows advanced lymphocytic infiltration.

Edit line: insert after line: **22**

22&gt; **COMMENT: The bone marrow shows advanced lymphocytic infiltration.**

23&gt; **Recommend iron replacement trial to rule out component of iron**

24&gt; **deficiency in etiology of the observed anemia. Correlate with serum**

25&gt; **ferritin levels. There is no evidence of transformation to a more**

26&gt; **aggressive histological type.**

27&gt; **&lt;Enter&gt;**

4 lines inserted.....

EDIT Option: **&lt;Enter&gt;**

PATHOLOGIST: LABPROVIDER, NINE.// **&lt;Enter&gt;**

DATE REPORT COMPLETED: JUN 28, 1988// **&lt;Enter&gt;**

*[The final report is shown below]*

-------------------------------------------------------------------

MEDICAL RECORD :	SURGICAL PATHOLOGY   Pg 1
-------------------------------------------------------------------

Submitted by: LABPROVIDER, THREE	Date obtained: JUN 28, 1988
-------------------------------------------------------------------

Specimen:
LT. POSTERIOR ILIAC CREST BX.
BONE MARROW ASPIRATE
--------------------------------------------------------------------

Brief Clinical History:
Patient with newly diagnosed (7/87) CLL with gastric involvement at time of Biliroth in 7/87 with progressive anemia/decreased Ct. borderline FL studies.
---------------------------------------------------------------------Preoperative Diagnosis:
------------------------------------------------------

Operative Findings:


Postoperative Diagnosis:
			Surgeon/physician: LABPROVIDER, THREE
====================================================================
							PATHOLOGY REPORT
Laboratory: VAMC			Accession No. 12
Gross description		Pathology Resident	LABPROVIDER, NINE LABPATIENT1, TWO LABPATIENT, TEN

	1. Specimen consists of a single cylindrical fragment of bone tissue measuring 0.8 x 0.2 cm. Entire specimen submitted after decalcification.
	2. Specimen consists of multiple dark tan soft elongated to irregular fragments of tissue measuring 1.3 x 0.4 x 0.2 cm. Entire specimen submitted
in 1 cassette.


Microscopic exam/diagnosis:
	DIFFERENTIAL:
		Polys:8
		Bands:0
		Lymphs:90
		Monos:2
		Eosins:0
		Basos:0
		Blasts:0
		Promyel:0
		Myelos:0
		Metas:0

PERIPHERAL BLOOD: Lymphocytes markedly increased with frequent
	smudge cells. Lymphocytes maturing with smudged chromatin and only rare 	nuclei. Platelets adequate.

BONE MARROW:			1.	Advanced lymphoid infiltrate.
						2.	Decreased cellular elements.
						3.	Decreased stainable iron.

DIAGNOSIS: Chronic lymphocytic leukemia (see comment) with extensive

diffuse bone marrow infiltrate.
	COMMENT: The bone marrow shows advanced lymphocytic infiltration.
	Recommend iron replacement trial to rule out component of iron 
	deficiency in etiology of the observed anemia. Correlate with serum 	ferritin levels. There is no evidence of transformation to a more 	aggressive histological type.

SNOMED code(s):
T-06000: bone marrow
	M-98233: chronic lymphoid leukemia
	D-4010 : anemia
	F-10364 : iron stores, bone marrow, decreased (t-06000)

---------------------------------------------------------------------
										(End of report)
LABPROVIDER, THREE				rg: Date NOV 20,.1990
---------------------------------------------------------------------
LABPATIENT, SEVEN				  SURGICAL PATHOLOGY Report
ID:000-00-0007 SEX:M DOB:5/8/16 AGE: 74 LOC: 1A LABPROVIDER, SEVEN

##### Example 4:	Using a Template to Enter a  system Report for a Cytology

Select Data entry, anat path Option: **GS** FS/Gross/Micro/Dx/SNOMED Coding

Select ANATOMIC PATHOLOGY section: **CY** CYTOPATHOLOGY

Enter Etiology, Function, Procedure &amp; Disease ? NO// **&lt;Enter&gt;** (NO)

Data entry for 1992 ? YES// **&lt;Enter&gt;** (YES)

Select Accession Number/Pt name: **6** for 1992

LABPATIENT1, SIX ID: 000-00-0016

Specimen(s):

CERVICOVAGINAL SMEAR

GROSS DESCRIPTION:

1&gt;Two smears received.

EDIT Option: **&lt;Enter&gt;**

MICROSCOPIC EXAM/DIAGNOSIS:

1&gt; *

**NOTE:** enter a “*” followed by the entry name in the LAB DESCRIPTION file (#62.5). Please see the example under Enter/Edit Lab Description file option under the Supervisor Menu.

2&gt; **&lt;Enter&gt;**

EDIT Option: **&lt;Enter&gt;**

***[After completing the prompts recall the same accession and you will see the specimen description from the entry in the lab description file in the Microscopic Exam/Diagnosis field:]***

Select Accession Number/Pt name: **6** for 1992

LABPATIENT1, SIX ID: 000-00-0016

Specimen(s):

CERVICOVAGINAL SMEAR

GROSS DESCRIPTION:

1&gt;Two smears received.

EDIT Option: **&lt;Enter&gt;**

MICROSCOPIC EXAM/DIAGNOSIS:

1&gt;Statement on Specimen Adequacy

2&gt;  ( ) Satisfactory for interpretation

3&gt;  ( ) Less than optimal

4&gt;  ( ) Unsatisfactory

5&gt; **&lt;Enter&gt;**

6&gt; Explanation for less than optimal/unsatisfactory specimen:

7&gt;  ( ) Scant cellularity

- ( ) Poor fixation or preservation

9&gt;  ( ) etc.

EDIT Option: **&lt;Enter&gt;**

#### FS/Gross/Micro/Dx ICD [LRAPDGI]

This option allows review of gross specimen and frozen section description, entry of microscopic description and diagnosis and ICD-CM coding for each accession number. If this option doesn’t seem to work correctly, check with your site manager; the ICD-CM globals may not have been loaded (possibly because of space shortages).

You can identify cases requiring review by the Tissue Committee by adding the “TC Code” prompt. Use the Edit QA Site Parameters option if you wish to include this prompt in this edit template. In the example below, the prompt is not included.

Example:

Select Data entry, anat path Option: **GI** FS/Gross/Micro/Dx/ICD Coding

Select ANATOMIC PATHOLOGY section: **CY** CYTOPATHOLOGY

CYTOPATHOLOGY (CY)

Data entry for 2012 ? YES//  (YES)

Select one of the following:

1     Accession number

2     Unique Identifier (UID)

3     Patient Name

Select one: 1//  Accession number

Enter Accession Number/Pt name: 1 for 2012

LABPATIENT,NINE          000-00-0009     DOB: Feb 1, 1800

Collection Date: Jun 25, 2012

Acc #: CY 12 1 []

Test(Specimen(s):

SPUTUM

GROSS DESCRIPTION:

1&gt;Specimen consists of 15 ml of serous milky fluid.

EDIT Option: **&lt;Enter&gt;**

MICROSCOPIC EXAM/DIAGNOSIS:

1&gt;No lower respiratory elements are found.

2&gt;

3&gt;DIAGNOSIS: SPUTUM: UNSATISFACTORY

4&gt; **&lt;Enter&gt;**

EDIT Option: **&lt;Enter&gt;**

CYTOTECH: **LABPROVIDER, TEN**

PATHOLOGIST: LABPROVIDER1, ONE// **&lt;Enter&gt;**

DATE REPORT COMPLETED: MAY 12,1989// **&lt;Enter&gt;**

REVIEWED BY PATHOLOGIST: YES// **&lt;Enter&gt;**

Select ICD DIAGNOSIS: **786.4** 786.4  ABNORMAL SPUTUM

...OK? YES// **&lt;Enter&gt;** (YES)

ICD DIAGNOSIS: 786.4// **&lt;Enter&gt;**

Select ICD DIAGNOSIS: **&lt;Enter&gt;**

Number of slides: 4 // **&lt;Enter&gt;**

Number paraffin blocks: 1 // **&lt;Enter&gt;**

Select Accession Number/Pt name: **&lt;Enter&gt;**

#### Enter Old Anat Path Records [LRAPOLD]

Entry of old cases from the “Card file” can be accomplished in several different ways, as follows:

a)	If you do not have sufficient secretarial resources to tackle the whole file, you may decide to enter the historical data on a case-by-case basis as new specimens are received. If so, you will probably need to resolve who will be assigning SNOMED codes to the diagnosis found on the cards. If the old cards are pulled and given to the pathologist with the gross descriptions of the current specimen, the pathologist would have access to the previous information and could do that coding at the same time. The old data could then be entered on that patient, making the cumulative summary comprehensive.

b)	If you have the secretarial resources, then the file can be tackled straight-forwardly.

There are two ways to enter the old cases:

Method A:	There is the direct option of entering “Old cases” and doing the coding in one pass. This is the quickest. However, if you feel that the physician may want to be aware of prior specimen diagnoses, the data will not be found in the option Pathology report for a patient if it is entered through this option. It will show up on the Cumulative Path Report option in the Anatomic Menu and with the gross description print options.

Method B:	If you want recent old cases available for physician review, then they will have to be individually accessioned and coded. This requires an additional step, plus the extra step of clearing the print queues (unless you want to document the results of the accessioning/coding process).

Example:	Enter Old Anat Path Records

Select Data entry, anat path Option: **OR** Enter old anat path records

This option skips entering accession number in the Accession Area file.
	Is this what you want ? NO// **Y** (YES)

Select ANATOMIC PATHOLOGY section: SURGICAL PATHOLOGY 

Enter Etiology, Function, Procedure &amp; Disease ? NO// **&lt;Enter&gt;** (NO)

Enter Special Studies ? NO// **&lt;Enter&gt;** (NO)

Select Patient Name: LABPATIENT, SEVEN 05-08-16 000000007
LABPATIENT, SEVEN ID: 000-00-0007
AGE: 72 DATE OF BIRTH: MAY 8, 1916
PATIENT LOCATION: 1A// **&lt;Enter&gt;** Date (must be exact) specimen taken: **5 6 90** (MAY 06, 1990)

Enter Accession number: **123** Ac #123 in SURGICAL PATHOLOGY FILE for 90
	Patient: LABPATIENT1, SEVEN ID: 000-00-0017

Enter Accession number: **566** DATE REPORT COMPLETED: MAY 7, 1990// **&lt;Enter&gt;** (MAY 07, 1986)
PATHOLOGIST: **LABPROVIDER1, TWO** Select ORGAN/TISSUE: **SKIN** 01000
	ORGAN/TISSUE NUMBER: 1// **&lt;Enter&gt;** Select MORPHOLOGY: **43000** CHRONIC INFLAMMATION 43000
	Select MORPHOLOGY: **&lt;Enter&gt;** Select ORGAN/TISSUE: **&lt;Enter&gt;** Select COMMENT: **&lt;Enter&gt;** Date (must be exact) specimen taken: **&lt;Enter&gt;** Select Patient Name: **&lt;Enter&gt;** Select Data entry, anat path Option: &lt;Enter&gt;

**NOTE:** If you attempt to enter a surgical pathology number, but the system rejects it as already existing, there was probably a clerical error. Go into the option Print Log Book and enter the appropriate information to display what the system has recorded for the SP number in question. The system will display the usual information and you can resolve with which patient the number actually belongs. The fact that the data was entered through [LRAPOLD] and the accession is not in the accession file does not prohibit it from being accessible through this option.

#### Supplementary Report, Anat Path [LRAPDSR]

**NOTE:** The Supplementary Report, Anat Path [LRAPDSR] option was **modified** by the release of patch LR*5.2*248. This option stores audit information for any ‘Supplementary’ report that was modified after the report had been released. The audit information now being stored is the date and time the text was modified, the person’s name modifying the text, and the original text before it was modified.

Any additional studies or supplemental information can be entered using the Spec Studies-EM;Immuno;Consult;Pic, Anat Path [LRAPDSS] option or the Supplementary Report, Anat Path [LRAPDSR] option. The ‘Supplementary’ report offers only the date/time of the report and a single free-text field. Data entered in this field will be deleted when the descriptions are deleted. The Special Studies option is more restrictive in its application. However, data entered is not deleted when descriptions are deleted. It can then be used for searches, etc. at some time in the future. Entry of data will place either report in the final report print queue, but supplemental reports must be “released” before the information is available.

**HINT:** AFIP case information can be entered as a Special Study by designating “Consultation” as the type of study.

**Example:	‘** Supplementary’ report


```vista
Select Anatomic pathology Option: **D** Data entry, anat path
Select Data entry, anat path Option: **SR** Supplementary Report, Anat Path
Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY
```

Enter Etiology, Function, Procedure &amp; Disease ? NO// **&lt;Enter&gt;** Data entry for 1988 ? YES// **&lt;Enter&gt;** (YES)
Select Accession Number/Pt name: 23 for 1990
LABPATIENT, SEVEN ID: 000-00-0007
Specimen(s):
SKIN

DATE REPORT COMPLETED: NOV 21, 1990// **&lt;Enter&gt;** Select SUPPLEMENTARY REPORT DATE/TIME: N NOV 21, 1988 11:00
	DESCRIPTION:
	1&gt; **This is an example of a supplementary report. It can be used to report** 2&gt; **the results of recuts**

3&gt; **RET** &gt;
EDIT Option: **&lt;Enter&gt;**

Select ORGAN/TISSUE: **&lt;Enter&gt;** Select Accession Number/Pt name: **23** for 1990
LABPATIENT, SEVEN ID: 000-00-0007
Specimen(s):
SKIN
DATE REPORT COMPLETED: NOV 21,1990// **&lt;Enter&gt;** Select SUPPLEMENTARY REPORT DATE/TIME: NOV 21, 1990@11:00
		// **N** NOV 21, 1990 11:01
	DESCRIPTION:
	1&gt; **There can be more than one supplementary report.**

2&gt;&lt;Enter&gt;
EDIT Option: **&lt;Enter&gt;**

NOTES:

As mentioned on the prior page, with the release of patch LR*5.2*248, if a modification is made to a released ‘Supplementary’ report, audit information is now being stored. When printing the ‘Supplementary’ report using Print Single Report Only [LRAP PRINT SINGLE] option or Print All Reports on Queue [LRAP PRINT ALL ON QUEUE] option, the report will display the **new** ‘MODIFIED REPORT’ information (i.e., date and time the report text was modified, person’s name that modified the report, and the original text before it was modified).

**The shaded areas shown in the following example indicate modifications made to the report.**

**Example:** ‘Supplementary Final’ report

----------------------------------------------------------------------------
	MEDICAL RECORD :		SURGICAL PATHOLOGY		Pg 1
----------------------------------------------------------------------------
Submitted by: LABPROVIDER, SEVEN		Date obtained: NOV 21, 1990
----------------------------------------------------------------------------
Specimen:
SKIN
----------------------------------------------------------------------------
Brief Clinical History:
	Scaly eruption on extensor surfaces of forearms.
----------------------------------------------------------------------------
Preoperative Diagnosis:
	Psoriasis
----------------------------------------------------------------------------
Operative Findings:
	Psoriasis
-----------------------------------------------------------------------------
Postoperative Diagnosis:
	Same					Surgeon/physician: LABPROVIDER, SEVEN
============================================================================
					  PATHOLOGYY REPORT
Laboratory: R5ISC						Accession No. SP90 23
----------------------------------------------------------------------------
Gross description:		 Pathology Resident: LABPROVIDER1, THREE
	3mm punch biopsy of skin

Microscopic exam/diagnosis:

Skin and subjacent tissue showing parakeratosis, elongation and blunting of rate ridges, and neutrophilic abscesses in the parakeratotic layer consistent with psoriasis.

Supplementary Report:
	Date: NOV 21, 1990 11:00

*** MODIFIED **REPORT** ***

(Last modified: NOV 21, 1990 11:00 typed by LABUSER, ONE

This is an example of a supplementary report. It can be used to report

the results of re-cuts, special stains, etc.

Date: NOV 21, 1990 11:01
	There can be more than one supplementary report.
CONSULTATION AFIP#123456789 Date: NOV 21, 1990
SKIN
This is a description of the findings of EM study.
----------------------------------------------------------------------------
										(End of report)
									rg| Date NOV 21, 1990
----------------------------------------------------------------------------

LABPATIENT, SEVEN							STANDARD FORM 515
ID:000-00-0007 SEX:M DOB:5/8/16 AGE 72			LOC:1A
									LABPROVIDER, SEVEN

#### Special Studies-EM;Immuno;Consult;pic, Anat Path [LRAPDSS]

The special studies option under the data entry menu is useful for entering consultations. For example, if a specimen is sent to AFIP, you can enter it as a consultation; enter AFIP 1234 as the ID and the AFIP report date. It is probably a major waste of time to actually enter the report under the word-processing field since the actual report (hard copy) is charted and filed with the surgical path (cytology, etc.) report.

This data is included on the cum path data summary and the second page of the preliminary report. It is not archived/purged. Additional programming allows searching on these fields. In other words, you can request a search of a specified topography and morphology with a particular special study.

Any additional studies or supplemental information can be entered using either the Special Studies option or the ‘Supplementary Report’ option. The Supplementary Report offers only the date/time of the report and a single free-text field. Data entered in this field will be deleted when the descriptions are deleted. The Special Studies option is more restrictive in its application; however, data entered is not deleted when descriptions are deleted. For both options, entry of data will place the report in the final report print queue.

Cases cannot be retrieved in the future based solely on the special studies information. In order to use the search options to retrieve cases, you will need to enter a procedure code also. For example, for Immunoperoxidase studies, additional programming accommodates entry of test results for specific procedure codes if so defined in the PROCEDURE FIELD file (#61.5). For consultations such as AFIP, SERS, and SERA, cases can be retrieved using the AP Consultation Searches and Reports [LRAPQACN] option in the Supervisor’s Menu **if** the procedure codes are entered.

**Example:**

Select Data entry, anat path Option: **SS** Spec Studies-EM;Immuno;Consult;Pic, Anat Path

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY 

Data entry for 1990 ? YES// **&lt;Enter&gt;** (YES)

Select Accession Number/Pt name: **23** for 1990
LABPROVIDER, SEVEN ID: 000-00-0007
Specimen(s):
SKIN

DATE REPORT COMPLETED: NOV 21,1990// **&lt;Enter&gt;** Select ORGAN/TISSUE: SKIN// **&lt;Enter&gt;** Select SPECIAL STUDIES: **?** ANSWER WITH SPECIAL STUDIES
	YOU MAY ENTER A NEW SPECIAL STUDIES, IF YOU WISH
CHOOSE FROM:
		E	ELECTRON MICROSCOPY
		I	IMMUNOFLUORESCENCE
		P	PHOTOGRAPHY
		C	CONSULTATION
		F	FROZEN SECTION
		IP	IMMUNOPEROXIDASE
	Select SPECIAL STUDIES: **C** (CONSULTATION)
	SPECIAL STUDIES ID #: **AFIP#123456789** DATE: **T** (NOV 21, 1990)

ID #: **AFIP#123456789** DESCRIPTION:
	1&gt; **This is an example of a consultation sent to the AFIP.** 2&gt; **&lt;Enter&gt;** EDIT Option: **&lt;Enter&gt;** Select SPECIAL STUDIES: **&lt;Enter&gt;** Select PROCEDURE: Y333 (ADMINISTRATION OF MEDICATION, EMERGENCY)

Select ORGAN/TISSUE: **&lt;Enter&gt;** Select Accession Number/Pt name: &lt;Enter&gt;

**NOTE:** A procedure from the Procedure field list or a SNOMED code must be entered at the “Select PROCEDURE” prompt for the report to show up in the search option.

#### Edit/Modify Data, Anat Path [LRAPE]

##### Description

**Menu Item	Description**

Edit Log-In &amp; Clinical Hx Anat Path	Edit entries in accessions that have been logged in for autopsy, cytopath, EM, or surgical path, but that have no descriptive or diagnostic data entered yet.

Modify Anat Path Gross/Micro/Dx	Allows changing microscopic description and

Frozen Section	diagnosis after the report has been released. A record is kept of the pre-modified text, date of change and who made the change. *** MODIFIED REPORT *** will appear on the report.

Edit Anat Path Comment	Allows editing of the accession comments for surg path, cytopath, and electron microscopy sections. The comments will appear on the log book for the appropriate section.

#### Edit Log-In &amp; Clinical Hx Anat Path [LRAPED]

You may change entries in accessions that have been logged in for autopsy, cytopath, EM, or surgical path, but have no descriptive or diagnostic data entered yet. For each accession number you may select multiple specimens to edit. In order to edit accessions that have been completed but not released, it is necessary to delete the completion date first.

For quality assurance review purposes, a new field Treating Specialty At Death has been added (63,14.6) for autopsies. If all of the data is entered, it is possible to have data on deaths sort by Service, Treating Specialty and Physician using the QA Outcome Review Cases [LRAPQOR] option in the Supervisor’s Menu.

**Example 1:**

Select Anatomic pathology Option: **E** Edit/modify data, anat path

Select Edit/modify data, anat path Option: **LI** Edit log-in data &amp; clinical hx, anat path

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY 

EDIT SURGICAL PATHOLOGY Log-In/Clinical Hx for 1990 ? YES// **&lt;Enter&gt;** (YES)

Enter SURGICAL Accession #: **23** LABPROVIDER, SEVEN ID: 000-00-0007  OK ? YES// **&lt;Enter&gt;** (YES)
Specimen date: NOV 21, 1990
Report released or completed. Cannot edit Log-in data.

Enter SURGICAL Accession #: **24** LABPATIENT1, EIGHT  ID: 000-00-0018 OK? YES// **&lt;Enter&gt;** (YES)
Specimen date: NOV 21, 1990

PATIENT LOCATION: 1A// **&lt;Enter&gt;** SURGEON/PHYSICIAN: LABRPOVIDER1, FOUR// **&lt;Enter&gt;** SPECIMEN SUBMITTED BY: LABRPOVIDER1, FOUR // **&lt;Enter&gt;** Select SPECIMEN: HERNIA SAC// **&lt;Enter&gt;** SPECIMEN: HERNIA SAC// **&lt;Enter&gt;** Select SPECIMEN: **&lt;Enter&gt;**

BRIEF CLINICAL HISTORY:

1&gt; **&lt;Enter&gt;**

PREOPERATIVE DIAGNOSIS:

1&gt;

OPERATIVE FINDINGS:

1&gt; **&lt;Enter&gt;**

POSTOPERATIVE DIAGNOSIS:dx

1&gt; **&lt;Enter&gt;**

DATA/TIME RECEIVED: NOV 21, 1988@08:58// **&lt;Enter&gt;** PATHOLOGIST: LABPROVIDER1,, TWO// **&lt;Enter&gt;** RESIDENT PATHOLOGIST: PROVIDER1, FIVE// **&lt;Enter&gt;**

Select COMMENT: **&lt;Enter&gt;** Enter SURGICAL Accession #: **&lt;Enter&gt;**

**Example 2:**

Select Anatomic pathology Option: **E** Edit/modify data, anat path

Select Edit/modify data, anat path Option: **LI** Edit log-in data &amp; clinical hx, anat path

Select ANATOMIC PATHOLOGY section: **AU** AUTOPSY

EDIT AUTOPSY Log-In/Clinical Hx for 1992 ? YES// **&lt;Enter&gt;** (YES)

Enter AUTOPSY Accession #: 4

LABPATIENT1, NINE ID: 000-00-0019 OK ? YES// **&lt;Enter&gt;** (YES)

Edit Weights &amp; Measurements ? NO// **&lt;Enter&gt;** (NO)

Date Died: NOV 25, 1992

AUTOPSY DATE/TIME: NOV 26,1992// **&lt;Enter&gt;**

LOCATION: 1A// **&lt;Enter&gt;**

SERVICE: SURGERY// **&lt;Enter&gt;**

TREATING SPECIALITY AT DEATH: CRITICAL CARE UNIT// **&lt;Enter&gt;**

PHYSICIAN: LABPROVIDER, THREE// **&lt;Enter&gt;**

RESIDENT PATHOLOGIST: LABPROVIDER, EIGHT// LABPROVIDER1, SIX

SENIOR PATHOLOGIST: LABPROVIDER1, SIX // LABPROVIDER, EIGHT

AUTOPSY TYPE: FULL AUTOPSY// **&lt;Enter&gt;**

AUTOPSY ASSISTANT: LABPROVIDER1, FIVE LEE// **&lt;Enter&gt;**

Enter AUTOPSY Accession #: **&lt;Enter&gt;**

#### Modify Anat Path Gross/Micro/Dx/Frozen Sections [LRAPM]

Once a report has been completed and released, the data entry options previously used to enter the data can no longer be accessed. Once modified, the report is placed back into the print queue again for reprinting and must be re-released. This report will indicate that it is a modified report. For those cases in which a question arises as to the exact change, both the old and the new report information can be obtained using the Print Path Micro/Dx Modifications [LRAPMOD] option. However, this data only remains in the system until the descriptions are deleted.

##### Example 1:	Modify Anat Path Gross/Micro/Dx/Frozen Section

Select Edit/modify data, anat path Option: **MM** Modify anat path gross/micro/dx/frozen section

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

Modify data for 1994 ? YES// **&lt;Enter&gt;** (YES)

Select Accession Number/Pt name: **2** for 1994

LABPATIENT1, TEN ID: 000-00-0110

Specimen(s):

PROSTATE CHIPS

1. MODIFY GROSS DESCRIPTION

2. MODIFY MICROSCOPIC DESCRIPTION

3. MODIFY DIAGNOSIS

4. MODIFY FROZEN SECTION

CHOOSE (1-4): **2**

Are you sure you want to modify MICROSCOPIC DESCRIPTION text ? NO// **Y** (YES)

MICROSCOPIC DESCRIPTION:

1&gt;Glomerular basement membranes are thickenedd and there is increased mesangial matrix.

EDIT Option: **Add** lines
 2&gt; **Also present are small prostatic infarcts and foci of squamous metaplasia** .

3&gt; **&lt;Enter&gt;**

EDIT Option: **&lt;Enter&gt;**

**NOTES:**

•	The report immediately becomes a “modified report” upon selection of the accession, regardless of the type of change entered.

•	Once any portion of the report is modified, the status of the accession changes to being unreleased. Once the modification is reviewed and approved by the pathologist, it must be rereleased using the Verify/Release reports [LRAPR] option.

•	The text of both the original and the modifications can be reviewed and/or maintained in hard copy using the Print Path Micro/Dx Modifications [LRAPMOD] option in the Supervisor’s Menu. However, these modifications are retrievable bypatient, not by date modified. These modifications remain in the system until the descriptions are purged using the Delete Anat Path Descriptions by Date [LRAPDAR] option.

##### Example 2:	Surgical Pathology Final Patient Reports Printout

Select Print, anat path Option: **PS** Print single report only

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

1. Preliminary reports

2. Final    reports

Select 1 or 2 : **2**

SURGICAL PATHOLOGY FINAL PATIENT REPORTS

Select Patient Name: LABPATIENT1, TEN 02-01-22  000000110  NO   NSC VETERAN

LABPATIENT2, ONE ID: 000-00-0021 Physician: LABPROVIDER1, SEVEN

AGE: 72 DATE OF BIRTH: FEB 1, 1922

Ward on Adm: 1 EAST Service: MEDICINE

Adm Date: APR 8, 1993 10:53 Adm DX: DIAGNOSIS

Present Ward: 1 EAST          MD: LABPROVIDER, SEVEN

Specimen(s)          Count #  Accession #  Date Obtained

( 1)      7    AUG 25, 1994 not verified

LEFT LEG

( 2)      6    AUG 25, 1994 not verified

left hip chip

( 3)      2    AUG 24, 1994

PROSTATE CHIPS

Choose Count #(1-3): **3**

Accession #: 2  Date Obtained: AUG 24, 1994

Print SNOMED &amp;/or ICD codes on report ? NO// **&lt;Enter&gt;** (NO)

Select Print Device: *[Enter Print Device Here]*

##### Example: 3	Surgical Pathology Final Patient Reports Printout

----------------------------------------------------------------------------

MEDICAL RECORD |          SURGICAL PATHOLOGY       Pg 1

----------------------------------------------------------------------------

Submitted by: LABPROVIDER1, EIGHT        Date obtained: AUG 24, 1994

----------------------------------------------------------------------------

Specimen (Received AUG 24, 1994 10:37):

PROSTATE CHIPS

----------------------------------------------------------------------------

Brief Clinical History:

Nocturia and difficulty voiding urine.

----------------------------------------------------------------------------

Preoperative Diagnosis:

same.

----------------------------------------------------------------------------

Operative Findings:

same.

----------------------------------------------------------------------------

Postoperative Diagnosis:

same.

Surgeon/physician: AMY NORTH MD

============================================================================

PATHOLOGY REPORT

Laboratory: VAMC                   Accession No. SP 94 2

----------------------------------------------------------------------------

Pathology Resident: LABPROVIDER1, FIVE MD

Frozen Section:

Basal cell .

Gross Description:

Specimen consists of 5 grams of prostate gland tissue.

Microscopic exam/diagnosis:

*** MODIFIED REPORT ***

(Last modified: AUG 27, 1994 17:30 typed by LABUSER, TWO)

Glomerular basement membranes are thickenedd and there is increased

mesangial matrix. Also present are small prostatic infarts and foci

of squamous metaplasia. Another small infarts and foci of squamous

metaplasia.

Supplementary Report:

Date: AUG 26, 1994 18:09

This is an example of a supplementary report. It can be used to report

the results of recuts.

Date: AUG 26, 1994 18:10

---------------------------------------------------------------------------

(See next page)

LABPROVIDER1, EIGHT MD                ec | Date AUG 25, 1994

---------------------------------------------------------------------------

LABPATIENT1, TEN                     STANDARD FORM 515

ID:000-OO-O110 SEX:F DOB:2/1/22 AGE:72 LOC:1 EAST

ADM:APR 8, 1993 DX:DIAGNOSIS           LABPROVIDER1, EIGHT MD

------------------------------------------------------------------------------

MEDICAL RECORD |          SURGICAL PATHOLOGY        Pg 2

------------------------------------------------------------------------------

PATHOLOGY REPORT

Laboratory: VAMC                   Accession No. SP 94 2

------------------------------------------------------------------------------

This is another supplementary report.

CONSULTATION AFIP#123456789 Date: AUG 26, 1994 18:17

PROSTATIC FASCIA

This is an example of a consultation sent to the AFIP.

-------------------------------------------------------------------------------

(End of report)

LABPROVIDER1, NINE                   ec | Date AUG 25, 1994

------------------------------------------------------------------------------

LABPATIENT1, TEN                  STANDARD FORM 515

ID:000-00-0000 SEX:F DOB:2/1/22 AGE:72 LOC:1 EAST

ADM:APR 8, 1993 DX:DIAGNOSIS           LABPROVIDER1, EIGHT MD

Edit Anat Path Comments [LRAPEDC]

Restrictions in the code prohibit access to this field once the report had been verified/released. Since this field does not appear on the final report, but is included on the log book used internally, the comment field can be used for a variety of purposes. This option allows editing of the accession comments for surg path, cytopath and electron microscopy sections even if the reports have been released. The comments will appear on the log book for the appropriate section until such time as the descriptions are purged.

**Example 1:** Enter/edit Specimen Comment(s)

Select Anatomic pathology Option: **SC** Edit anat path comments

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

1. Enter/edit specimen comment(s) *[New]*

2. Enter/edit delayed report comment(s) *[New]*

CHOOSE (1-2): **1** *[New]*

EDIT SURGICAL PATHOLOGY specimen comments for 1990 ? YES// **&lt;Enter&gt;** (YES)

Enter SURGICAL Accession #: **22** LABPATIENT, SEVEN ID: 000-00-0007 OK ? YES// **&lt;Enter&gt;** (YES)
Specimen date: NOV 20, 1990
Select COMMENT: This comment will appear on the log book.
		// **And so will this one** Select COMMENT: **?** ANSWER WITH COMMENT
CHOOSE FROM:
	1	This comment will appear on the log book.
	2	And so will this one
	YOU MAY ENTER A NEW COMMENT, IF YOU WISH
	 ANSWER MUST BE 1-75 CHARACTERS IN LENGTH
Select COMMENT: &lt;Enter&gt;

On Surgical Pathology reports, a list of all other staff pathologists who have been shown the case, as well as consultants, can be entered into the log-in comment field, for the accession to indicate additional review. It might also be advantageous to include a line to record the name of the clinician and the time contacted on initial malignant specimens.

**Report:** Print Log Book

Select Log-in menu, anat path Option: **PB** Print log book

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

SURGICAL PATHOLOGY LOG BOOK

Print SNOMED codes if entered ? NO// **&lt;Enter&gt;** (NO)

Log book year: 1990 OK ? YES// **&lt;Enter&gt;** (YES)

Start with Acc #: **22**

Go  to  Acc #: LAST // **&lt;Enter&gt;**

Select Print Device: *[Enter Print Device Here]*

NOV 30, 1990 10:40  VAMC                       Pg: 1

SURGICAL PATHOLOGY LOG BOOK for 1990

# =Demographic data in file other than PATIENT file

Date  Num  Patient       ID  LOC   PHYSICIAN    PATHOLOGIST

-----------------------------------------------------------------------------

11/20 22 LABPATIENT, SEVEN 8472 1 EAST LABPROVIDER1, NINE LABPROVIDER, SEVEN

Date specimen taken:10/24/90     Entered by:LABUSER, TWO

Released by: LABUSER, TWO

PROSTATE CHIPS

This comment will appear on the log book.
      And so will this one

This would provide documentation for quality assurance purposes as well as for general information. In order to get this information incorporated into the final copy, the information described should be entered in the Microscopic Description field.

**Example 2:** Enter/Edit Delayed Report Comment(s)

Select Edit/modify data, anat path Option: **SC** Edit anat path comments

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

1. Enter/edit specimen comment(s)

2. Enter/edit delayed report comment(s)

CHOOSE (1-2): **2**

EDIT SURGICAL PATHOLOGY delayed report comments for 1993 ? YES// **&lt;Enter&gt;** (YES)

Enter SURGICAL Accession #: **31**

LABPATIENT2, TWO ID: 000-00-0022 OK ? YES// **&lt;Enter&gt;** (YES)

Specimen date: SEP 22, 1993

Select DELAYED REPORT COMMENT: Also there are many special stains

// **?**

ANSWER WITH DELAYED REPORT COMMENT

CHOOSE FROM:

1        Report delayed because of decalcification.

2        Also there are many special stains

YOU MAY ENTER A NEW DELAYED REPORT COMMENT, IF YOU WISH

Answer must be 1-75 characters in length.

Select DELAYED REPORT COMMENT: **2** Also there are many special stains

Enter SURGICAL Accession #: **&lt;Enter&gt;**

**Report 1:** Print Log Book

Select Print, anat path Option: **PB** Print log book

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

SURGICAL PATHOLOGY LOG BOOK

Print SNOMED codes if entered ? NO// **&lt;Enter&gt;** (NO)

Log book year: 1993 OK ? YES// **&lt;Enter&gt;** (YES)

Start with Acc #: **31**

Go  to  Acc #: LAST // **&lt;Enter&gt;**

Select Print Device: *[Enter Print Device Here]*

SEP 27, 1993 07:46  REGION 7                    Pg: 1

SURGICAL PATHOLOGY LOG BOOK for 1993

# =Demographic data in file other than PATIENT file

Date  Num  Patient       ID LOC    PHYSICIAN     PATHOLOGIST

--------------------------------------------------------------------------

9/22   31 LABPATIENT2, TWO    0456 CARDIOLOG LABPROVIDER, ONE    LABPROVIDER, THREE

Date specimen taken:09/22/93     Entered by:LABPROVIDER, EIGHT

SKIN

Specimen submitted in alcohol.

Report delayed because of decalcification.

Also there are many special stains

--------------------------------------------------------------------------

**Report 2:**

Select Anatomic Pathology Option: **C** Clinician options, anat path

Select Clinician options, anat path Option: **DS** Display surg path reports for a patient

SURGICAL PATHOLOGY PATIENT REPORT(S) DISPLAY

Select Patient Name: LABPATIENT2, TWO 03-04-56   000000022   NSC VETERAN

LABPATIENT2, TWO ID: 000-00-0022 Physician: LABPROVIDER1, TEN

AGE: 37 DATE OF BIRTH: MAR 4, 1956

PATIENT LOCATION: CARDIOLOGY// &lt;Enter&gt;

Is this the patient ? YES// **&lt;Enter&gt;** (YES)

Date Spec taken: SEP 22, 1993     Pathologist:LABPROVIDER, THREE MD

Date Spec rec'd: SEP 22, 1993 16:23 Resident:

REPORT INCOMPLETE           Accession #: 31

Submitted by: LABPROVIDER, ONE    Practitioner:LABPROVIDER, ONE

--------------------------------------------------------------------------

Report delayed because of decalcification.

Also there are many special stains

Report not verified

### Inquiries, Anat Path [LRAPI]

#### Descriptions

**Menu Item	Description**

Display Surg Path Reports for a Patient	Display on the screen surgical pathology reports for a patient.

Display Cytopath Reports for a Patient	Display on the screen Cytopathology reports for a patient.

Display EM Reports For a Patient	Display on the screen Electron Microscopy reports for a patient.

Display Stains/Blocks for a Patient	Display tissue blocks and stains for an accession.

Show List of Accessions for a Patient	If you need to find all the accession numbers (in one accession area) for one patient, you may do so with this option. The information is displayed on the screen only; you can’t print the list with this option.

Search Options, Anat Path: 	All of these options search pathology entries by date for the portion of the SNOMED code specified.

Morphology Code Search

Disease Code Search

Etiology Code Search

Procedure Code Search

Function Code Search

ICD Search	Searches pathology entries by date for ICD-CM diagnosis code.

MULTIAXIAL Code Search, SNOMED	Searches pathology entries by date for the SNOMED codes specified.

Cum Path Data Summaries	Cumulative summary of surgical path, EM, and autopsy for screen display or hard copy.

Display Final Path Reports by Accession	Display final pathology reports which have been verified.

#### Display Surg Path Reports for a Patient [LRAPSPCUM]

#### Display Cytopath Reports for a Patient [LRAPCYCUM]

#### Display EM Reports for a Patient [LRAPEMCUM]

The options to display pathology reports for a patient automatically start with a display of the most recent specimen, which has been completed/released. No “DEVICE” prompt is included in this option. Reports can be printed through other options.

Example:

Select Anatomic pathology Option: **C** Clinician options, anat path

Select Clinician options, anat path Option: **DS** Display surg path reports for a patient

        SURGICAL PATHOLOGY PATIENT REPORT(S) DISPLAY

Select PATIENT NAME: LABPATIENT1, TEN 02-01-22 000-00-0110 NO NSC VETERAN

LABPATIENT1, TEN 02-01-22 000-00-0110 Physician: LABPROVIDER1, SEVEN

AGE: 72 DATE OF BIRTH: FEB 1, 1922

Ward on Adm: 1 EAST Service: MEDICINE

Adm Date: APR 8, 1993 10:53 Adm DX: ACCIDENT

Present Ward: 1 EAST          MD: LABPROVIDER1, SEVEN

PATIENT LOCATION: 1 EAST// &lt;Enter&gt;

Is this the patient ? YES// **&lt;Enter&gt;** (YES)

Date Spec taken: AUG 25, 1994     Pathologist:LABPROVIDER1, FIVE MD

Date Spec rec'd: AUG 25, 1994 19:41 Resident:

Date completed: AUG 26, 1994     Accession #: 7

Submitted by: LABPROVIDER2, ONE MD  Practitioner: LABPROVIDER2, ONE MD

-----------------------------------------------------------------------------

Specimen:

LEFT LEG

CONSULTATION AFIP#12345 Date: AUG 26, 1994

This is just a consultation.

-----------------------------------------------------------------------------

SNOMED/ICD codes:

T-Y9400: LEG

Date Spec taken: AUG 25, 1994     Pathologist: LABPROVIDER2, ONE MD

Date Spec rec'd: AUG 25, 1994 19:36 Resident:

REPORT INCOMPLETE           Accession #: 6

Submitted by: LABPROVIDER1, FIVE MD  Practitioner: LABPROVIDER1, FIVE MD

-----------------------------------------------------------------------------

Report not verified

Date Spec taken: AUG 24, 1994     Pathologist: LABPROVIDER1, FIVE MD

Date Spec rec'd: AUG 24, 1994 10:37 Resident: LABPROVIDER2, TWO

Date completed: AUG 25, 1994     Accession #: 2

Submitted by: LABPROVIDER1, SEVEN MD Practitioner: LABPROVIDER1, SEVEN MD

-----------------------------------------------------------------------------

Specimen:

PROSTATE CHIPS

Brief Clinical History:

Nocturia and difficulty voiding urine.

Preoperative Diagnosis:

same.

Operative Findings:

same.

Postoperative Diagnosis:

same.

Frozen Section:

Basal cell .

Gross Description:

Specimen consists of 5 grams of prostate gland tissue.

Microscopic exam/diagnosis: (Date Spec taken: AUG 24, 1994)

*** MODIFIED REPORT ***

(Last modified: AUG 27, 1994 17:30 typed by LABUSER, TWO)

Glomerular basement membranes are thickenedd and there is increased

mesangial matrix. Also present are small prostatic infarts and foci of

squamous metaplasia. Another small infarts and foci of squamous

metaplasia.

Supplementary Report:

Date: AUG 26, 1994 18:09 not verified

Date: AUG 26, 1994 18:10 not verified

CONSULTATION AFIP#123456789 Date: AUG 26, 1994 18:17

This is an example of a consultation sent to the AFIP.

-----------------------------------------------------------------------------

SNOMED/ICD codes:

T-18969: PROSTATIC FASCIA

P-Y333 : ADMINISTRATION OF MEDICATION, EMERGENCY

**NOTE:** The Cytopath and EM reports work essentially the same way as the above example.

#### Display Stains/Blocks for a Patient [LRAPST]

Information on the specific accessions is entered through the Blocks, Stains, Procedures, Surg Path [LRAPSPDAT] option.

Example:

Select Clinician options, anat path Option: **BD** Display stains/blocks for a patient
Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

Select Patient Name: LABPATIENT, SEVEN  05-08-16 000000007  NO  NSC VETERAN

LABPATIENT, ONE ID: 000-00-0001   Physician: LABPROVIDER2, TWO

AGE: 74 DATE OF BIRTH: MAY 8, 1916

Ward on Adm: 1 EAST Service: MEDICINE

Adm Date: APR 8, 1994 10:53 Adm DX: FALL ON - LEFT HIP

Present Ward: 1 A          MD: LABPROVIDER2, TWO

PATIENT LOCATION: 1 A// &lt;Enter&gt;

Specimen(s)          Count #  Accession #  Date

( 1)      7    AUG 25, 1994

LEFT LEG

( 2)      6    AUG 25, 1994

left hip chip

( 3)      2    AUG 24, 1994

PROSTATE CHIPS

Choose Count #(1-3): **3**

LABPATIENT, SEVEN 0007 Acc #: 2 Date: AUG 24, 1994

Slide/Ctrl Last stain/block date

PROSTATE CHIPS

Paraffin Block

A         Stain/Procedure            AUG 27, 1994 19:26

TRICHROME STAIN          1    AUG 27, 1994 19:26

B         Stain/Procedure            AUG 27, 1994 19:26

TRICHROME STAIN          1    AUG 27, 1994 19:26

Select Patient Name: **&lt;Enter&gt;**

#### Show List of Accessions for a Patient [LRUPT]

This option allows you to find all the accession numbers, in one accession area, for one patient. This is a screen display only option.

Example:

Select Anatomic pathology Option: **I** Inquiries, anat path

Select Inquiries, anat path Option: **PA** Show list of accessions for a patient

Select ACCESSION AREA: **SP** SURGICAL PATHOLOGY

Select Patient Name: LABPATIENT2, THREE		08-18-27		000000023
LABPATIENT2, THREE ID: 000-00-0023  Physician: LABPROVIDER, SEVEN

AGE: 63 DATE OF BIRTH: AUG 18, 1927
PATIENT LOCATION: 1A// **&lt;Enter&gt;** Is this the patient ? YES// **&lt;Enter&gt;** (YES)

SURGICAL PATHOLOGY LABPATIENT2, THREE ID: 000-00-0023
Spec Date/time		Acc #		PHYSICIAN		SPECIMEN(S)

Spec Date/time Acc #      PHYSICIAN    SPECIMEN(S)

08/25/94    SP94 7     LABPROVIDER2, TWO   LEFT LEG

08/25/94    SP94 6     LABPROVIDER1, NINE   left hip chip

08/24/94    SP94 2     LABPROVIDER2, THREE   PROSTATE CHIPS

#### Search Options, Anat Path [LRAPSEARCH]

The search options include SNOMED search options (MORPHOLOGY, DISEASE, ETIOLOGY, PROCEDURE, FUNCTION, and MULTIAXIAL) and search options.

**SNOMED:** You may search the anatomic reports by site (Topography) and then by the Morphology, Disease, Etiology, Procedure, or Function field. The results should be queued and printed only. You may enter up to six characters of the code. The entries can only contain digits, the letters “X” and “Y” or “*” for wild cards. One character entered = most general and all characters = most specific.

**HINTS:**

1. Each search option will display the information in two different formats: first, in alphabetical order by patient, then in numeric order by accession number. This makes retrieval of slides, reports, etc., easier.
2. At the end of each report, there is a summary of the number of accessions searched, as well as the % of codes searched which met the designated criteria.

##### Morphology Code Search, SNOMED [LRAPSM]

Example:

Select Inquiries, anat path Option: **SE** Search options, anat path

Select Search options, anat path Option: **MC** MORPHOLOGY code search, SNOMED

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

SURGICAL PATHOLOGY search by MORPHOLOGY code

TOPOGRAPHY (Organ/Tissue)

Select 1 or more characters of the code

For all sites type 'ALL' : **ALL**

MORPHOLOGY

For all choices type 'ALL'

Choice # 1: Select 1 or more characters of the code: **ALL**

Start with Date TODAY// **&lt;Enter&gt;** AUG 30, 1994

Go  to  Date TODAY// **-365** (AUG 30, 1993)

Select Print Device: *[Enter Print Device Here]*

AUG 30, 1994 10:25  VAMC                       Pg: 1

SURGICAL PATHOLOGY SEARCH(AUG 30, 1993=&gt;AUG 30, 1994)

# =  patient

SNOMED TOPOGRAPHY CODE: ALL--         SNOMED MORPHOLOGY CODE: ALL--

-----------------------------------------------------------------------------

NAME    ID SEX AGE ACC #  ORGAN/TISSUE    MORPHOLOGY

LABPATIENT2, FOUR 0024 F 62   5-94 SKIN OF NOSE    BASAL CELL ADENOMA

LABPATIENT2, FIVE 0025 M 83   3-94 LIVER       HYPERPLASIA

ADENOCARCINOMA

LABPATIENT2, SIX  0026 M 68   8-94 BONE MARROW    LEUKEMIA

AUG 30, 1994 10:25  VAMC                       Pg: 2

SURGICAL PATHOLOGY SEARCH(AUG 30, 1993=&gt;AUG 30, 1994)

# =  patient

SNOMED TOPOGRAPHY CODE: ALL--         SNOMED MORPHOLOGY CODE: ALL--

-----------------------------------------------------------------------------

ACC #  NAME        ID SEX AGE MO/DA ORGAN/TISSUE   MORPHOLOGY

3-94 LABPATIENT2, FIVE 0025 M  83 8/24 LIVER       HYPERPLASIA

ADENOCARCINOMA

5-94 LABPATIENT2, FOUR 0024 F  62 8/24 SKIN OF NOSE   BASAL CELL ADENOMA

8-94 LABPATIENT2, SIX  0026 M  68 8/25 BONE MARROW    LEUKEMIA

AUG 30, 1994 10:25  VAMC                       Pg: 3

SURGICAL PATHOLOGY SEARCH(AUG 30, 1993=&gt;AUG 30, 1994)

# =  patient

SNOMED TOPOGRAPHY CODE: ALL--         SNOMED MORPHOLOGY CODE: ALL--

-----------------------------------------------------------------------------

RESULT OF SURGICAL PATHOLOGY SEARCH:

PATIENTS WITHIN PERIOD SEARCHED: 11

SURGICAL PATHOLOGY ACCESSIONS WITHIN PERIOD SEARCHED: 11

3 OF  11 PATIENTS(27.27%)

3 OF   6 SNOMED CODE ALL SPECIMENS(50.00%)

6 ORGAN/TISSUE SPECIMENS WITHIN PERIOD SEARCHED

(SNOMED TOPOGRAPHY CODE ALL IS 100.00%)

DISEASE code search, SNOMED [LRAPSD] option and ETIOLOGY code search, SNOMED [LRAPSE] option.

##### Procedure Code Search, SNOMED [LRAPSP]

Example:	Procedure Code Search for Soft Tissue which was positive for the Immunopath Stain Vimentin

Select Search options, anat path Option: **PC** PROCEDURE code search, SNOMED

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

SURGICAL PATHOLOGY search by PROCEDURE code

TOPOGRAPHY (Organ/Tissue)

Select 1 or more characters of the code

For all sites type “ALL”: **1X**

PROCEDURE

Select only procedures with results ? NO// **Y** (YES)

Enter 1 for positive results or 0 for negative results: **1**

For all choices type “ALL”

Choice #1: Select 1 or more characters of the code: **3630004**

Choice #2: Select 1 or more characters of the code: **&lt;Enter&gt;**

Start with Date TODAY// **7-1-90** (JUL 01, 1990)

Go to  Date TODAY// **AUG 24, 1990**

Select Print Device: *[Enter Print Device Here]*

*[The printout follows the same pattern as other SNOMED searches and will not be printed.]*

**NOTE:** By designating “ASK RESULT” as “YES” in File #61.5 (PROCEDURE FIELD) for the specific procedure code, data indicating the test result can be entered during data entry when that specific procedure code is entered for a case. This can then be used for retrieval of cases via the SNOMED search options.

##### ICD Code Search [LRAPSI]

You can search the anatomic reports by the ICD-CM code. Because the search may be lengthy, the results should be queued to a printer. If this option does not seem to work correctly, check with your site manager. The ICD-CM globals may not have been loaded (possibly because of space shortages).

Example:

Select Search options, anat path Option: **IC** ICD code search

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY          SURGICAL PATHOLOGY SEARCH BY ICD CODE

Start with Date TODAY// **DEC 4, 1990**

Go to Date TODAY// **T-100** (SEP 13, 1990)

Select ICD DIAGNOSIS CODE NUMBER: **414 414.0** CORONARY ATHEROSCLEROSIS

...OK? YES// **&lt;Enter&gt;** (YES)

Select Print Device: *[Enter Print Device Here]*

DEC 4, 1990 14:02 SIUG  VAMC                Pg: 1

SURGICAL PATHOLOGY SEARCH (SEP 13, 1990=&gt;DEC 4, 1990)

ICD CODE: 414.0    CORONARY ATHEROSCLEROSIS

------------------------------------------------------------------

NAME     ID     SEX   AGE   ACC #

LABPATIENT, THREE 000-00-0003  M   53    13

##### MULTIAXIAL Code Search, SNOMED [LRAPSEM]

For some types of searches, it is desirable to specify more than one type of SNOMED code for the search criteria. This option provides that additional flexibility.

For those types of codes in which you don’t want to specify criteria, merely enter &lt;Enter&gt; for that prompt. If you enter “ALL,” the search will only include cases for which a code is entered.

For some purposes, such as selection of cases for discussion at conferences, additional information on the cases (including physician, the microscopic description, etc.,) is useful. By answering the prompts accordingly, the output from the search can be changed. **See Example 2** .

**Example 1:** Search for Soft Tissue which was Positive for the Immunopath Stain VIMENTIN which had a Morphology of a Primary Tumor.

Select Search options, anat path Options: **AX** MULTIAXIAL code search, SNOMED

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

SURGICAL PATHOLOGY multiaxial SNOMED search

TOPOGRAPHY (Organ/Tissue)

Select 1 or more characters of the code

For all sites type “ALL” : **1X**

MORPHOLOGY

For all choices type “ALL”

MORPHOLOGY choice # 1:Select 1 or more characters of the code: 88**3

ETIOLOGY (for all choices type “ALL”)

Choice # 1: Select 1 or more characters of the code: **88**

MORPHOLOGY choice #2:Select 1 or more characters of the code:&lt;Enter&gt;

PROCEDURE

Select only procedures with results ? NO// **Y** (YES)

Enter 1 for positive results or 0 for negative results: **1**

For all choices type “ALL”

PROCEDURE choice #1:Select 1 or more characters of the code: **3630004**

PROCEDURE choice #2: Select 1 or more characters of the code: **&lt;Enter&gt;**

DISEASE

For all choices type “ALL”

DISEASE choice #1: Select 1 or more characters of the code: **&lt;Enter&gt;**

FUNCTION

For all choices type “ALL”

FUNCTION choice # 1: Select 1 or more characters of the code: **&lt;Enter&gt;**

Start with Date TODAY// **10-1-90** (OCT 01, 1990)

Go to  Date TODAY// **&lt;Enter&gt;** JAN 1, 1990

List by accession number with specimens and microscopic dx ? NO// **Y** (YES)

LIST SPECIAL STUDIES ? NO// **Y** (YES)

Include SNOMED CODES on report ? NO// **Y** (YES)

Enter SEARCH COMMENT: **SOFT TISSUE SARCOMAS VIMENTIN POSITIVE**

**Example 2:** Search for Cases for GI Conference

Select Search options, anat path Option: **AX** MULTIAXIAL code search, SNOMED

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

SURGICAL PATHOLOGY multiaxial SNOMED search

TOPOGRAPHY (Organ/Tissue)

Select 1 or more characters of the code

For all sites type 'ALL' : **5**

MORPHOLOGY

For all choices type 'ALL'

MORPHOLOGY choice # 1: Select 1 or more characters of the code: **ALL**

ETIOLOGY (for all choices type 'ALL')

Choice # 1: Select 1 or more characters of the code: **&lt;Enter&gt;**

PROCEDURE

Select only procedures with results ? NO// **&lt;Enter&gt;** (NO)

For all choices type 'ALL'

PROCEDURE  choice # 1: Select 1 or more characters of the code: **&lt;Enter&gt;**

DISEASE

For all choices type 'ALL'

DISEASE   choice # 1: Select 1 or more characters of the code: **&lt;Enter&gt;**

FUNCTION

For all choices type 'ALL'

FUNCTION  choice # 1: Select 1 or more characters of the code: **&lt;Enter&gt;**

Start with Date TODAY// **1-1-88** (JAN 01, 1988)

Go  to  Date TODAY// **9-8-94** (SEP 08, 1994)

List by accession number with specimens and microscopic dx ? NO// **Y** (YES)

List special studies ? NO// **Y** (YES)

Include SNOMED CODES on report ? NO// **Y** (YES)

Enter SEARCH COMMENT: **&lt;Enter&gt;**

Select Print Device: *[Enter Print Device Here]*

SEP 8, 1994 13:20   ISC, VERIFICATION ACCT          Pg: 1

SURGICAL PATHOLOGY SEARCH (JAN 1, 1988-SEP 8, 1994)

Date  # =  patient     For: LABPROVIDER2, Four

Taken  Patient       ID  Physician     LOC   Acc# PATHOLOGIST

-----------------------------------------------------------------------------

06/29/89 LABPATIENT2, SIX 3454 LABPROVIDER, SEVEN  5N 2 LABPROVIDER2, FIVE

Specimen(s):  TOOTH

AS ABOVE

T-54010 TOOTH

M-23350 IMPACTED TOOTH

PHOTOGRAPHY 1 Date: JUN 29, 1989

-----------------------------------------------------------------------------

07/24/89 LABPATIENT2, SEVEN 0027 LABPROVIDER2, SIX 1E 3 LABPROVIDER2, NINE

Specimen(s):  GALLBLADDER

T-57000 GALLBLADDER

M-30010 LITHIASIS

-----------------------------------------------------------------------------

08/24/94 LABPATIENT2, FIVE 0027 LABPROVIDER, 2, SIX 1 EAST 3 LABPROVIDER1, NINE

SEP 8, 1994 13:20   ISC, VERIFICATION ACCT          Pg: 2

SURGICAL PATHOLOGY SEARCH (JAN 1, 1988-SEP 8, 1994)

Date  # =  patient     For: LABPROVIDER2, FOUR

Taken  Patient       ID  Physician     LOC   Acc# PATHOLOGIST

-----------------------------------------------------------------------------

08/24/94 LABPATIENT2, FIVE 0027 LABPROVIDER, 2, SIX 1 EAST LABPROVIDER1, NINE 3

Specimen(s):  LIVER BIOPSY

IMPACTED TUSK Glandular and stromal hyperplasia.

T-56000 LIVER

M-81403 ADENOCARCINOMA

M-72000 HYPERPLASIA

CONSULTATION 134 Date: SEP 3, 1994 13:16

-----------------------------------------------------------------------------

SEP 8, 1994 13:21   ISC, VERIFICATION ACCT          Pg: 3

SURGICAL PATHOLOGY SEARCH (JAN 1, 1988-SEP 8, 1994)

# =  patient    SNOMED FIELDS    For:LABPROVIDER2, FOUR

-----------------------------------------------------------------------------

RESULT OF SURGICAL PATHOLOGY SEARCH:

PATIENTS WITHIN PERIOD SEARCHED: 28

SURGICAL PATHOLOGY ACCESSIONS WITHIN PERIOD SEARCHED: 28

ORGAN/TISSUE SPECIMENS WITHIN PERIOD SEARCHED: 12

The following fields were used for the search :

TOPOGRAPHY FIELD: 5

MORPHOLOGY FIELD: ALL

#### Cum Path Data Summaries [LRAPT]

This option provides a cumulative summary of surgical path, cytopath, EM, and autopsy for screen display or hard copy. Data for special studies are also included in this report.

Example:

Select Inquiries, anat path Option: **CS** Cum path data summaries

Cum path data summaries

1. DISPLAY cum path data summary for a patient

2. PRINT cum path data summary for patient(s)

Select (1-2): 1

DISPLAY cum path data summary for a patient

Select Patient Name: **LABPATIENT1, FOUR** 02-01-12 000-00-0014

NSC VETERAN

LABPATIENT1, FOUR 000-00-0014  Physician: LABPROVIDER2, EIGHT

AGE: 77 DATE OF BIRTH: FEB 1, 1912

Ward on Adm: 1 EAST Service: PSYCHOLOGY

Adm Date: APR 8, 1993 10:53 Adm DX: STRESS

Present Ward: 1 EAST          MD: LABPROVIDER2, EIGHT

PATIENT LOCATION: 1 EAST// **&lt;Enter&gt;**

Is this the patient ? YES// **&lt;Enter&gt;** (YES)

LABPATIENT1, FOUR 000-00-0014  DOB: FEB 1, 1912 LOC:1 EAST

-------------------------------------------------------------------

SURGICAL PATHOLOGY

Organ/tissue:  Date rec'd: 03/28/89  Acc #: 9

Report not verified.

Organ/tissue:  Date rec'd: 11/08/88  Acc #: 21

SKIN

BIOPSY, PUNCH

PSORIASIS

IMMUNOFLUORESCENCE 21-I Date: NOV 13, 1988

LIVER

PAIN, NOS

LOSS OF VOICE

BIOPSY, NEEDLE

DIABETES MELLITUS

TUBERCULOSIS

CIRRHOSIS

ALCOHOL

HEMANGIOMA

-------------------------------------------------------------------

SURGICAL PATHOLOGY

Organ/tissue:  Date rec'd: 11/08/88  Acc #: 21

LIVER

ELECTRON MICROSCOPY E-21-88 Date: NOV 13, 1988 06:27

Organ/tissue:  Date rec'd: 11/07/88  Acc #: 20

Report not verified.

Organ/tissue:  Date rec'd: 08/01/88  Acc #: 12

Press return to continue or “^” to escape **&lt;Enter&gt;**

LABPATIENT1, FOUR 000-00-0014  DOB: FEB 1, 1912 LOC:1 EAST

--------------------------------------------------------------------

SURGICAL PATHOLOGY

NAIL OF TOE

HEMATOMA

Organ/tissue:  Date rec'd: //   Acc #: 345

Report not verified.

Organ/tissue:  Date rec'd: 06/02/88  Acc #: 7

SKIN

BIOPSY, NOS

DIABETES MELLITUS, ADULT ONSET TYPE

PSORIASIS

ABSCESS

STAPHYLOCOCCUS AUREUS

Organ/tissue:  Date rec'd: 05/10/88  Acc #: 5

Report not verified.

SURGICAL PATHOLOGY

Organ/tissue:  Date rec'd: 03/04/78  Acc #: 1

SKIN

KERATOSIS, SEBORRHEIC

Organ/tissue:  Date rec'd: 01/02/78  Acc #: 56

BLOOD

NORMAL CELLULAR MORPHOLOGY

Organ/tissue:  Date rec'd: 06/07/45  Acc #: 6789

LIVER

CIRRHOSIS

--------------------------------------------------------------------

CYTOPATHOLOGY

Organ/tissue:  Date rec'd: 09/25/88  Acc #: 7

SPUTUM

CARBUNCLE

Organ/tissue:  Date rec'd: 08/22/88  Acc #: 6

Report not verified.

Organ/tissue:  Date rec'd: 05/04/88  Acc #: 1

SPUTUM

NEGATIVE FOR MALIGNANT CELLS

no comment

good specimen

CYTOPATHOLOGY

Organ/tissue:  Date rec'd: 08/04/87  Acc #: 35

Report not verified.

Press return to continue or “^” to escape **&lt;Enter&gt;**

LABPATIENT1, FOUR 000-00-0014  DOB: FEB 1, 1912 LOC: 1 EAST

-------------------------------------------------------------------

Organ/tissue:  Date rec'd: 08/03/87   Acc #: 34

Report not verified.

Date rec'd: 08/03/87  Acc #: 33

Report not verified.

Organ/tissue:  Date rec'd: 07/31/87  Acc #: 14

Organ/tissue:  Date rec'd: 07/31/87  Acc #: 15

ABDOMEN

ACQUIRED DIGITAL FIBROKERATOMA

Organ/tissue:  Date rec'd: 07/31/87  Acc #: 30

Report not verified.

Organ/tissue:  Date rec'd: 07/31/87  Acc #: 29

Report not verified.

Organ/tissue:  Date rec'd: 06/10/87  Acc #: 26

Organ/tissue:  Date rec'd: 06/10/87  Acc #: 24

Organ/tissue:  Date rec'd: 06/10/87  Acc #: 23

Organ/tissue:  Date rec'd: 06/10/87  Acc #: 22

Organ/tissue:  Date rec'd: 05/06/87  Acc #: 12

Report not verified.

CYTOPATHOLOGY

Organ/tissue:  Date rec'd: 03/05/87  Acc #: 11

Report not verified.

SPUTUM

POSITIVE FOR MALIGNANT CELLS

Organ/tissue:  Date rec'd: 08/20/86  Acc #: 10

Organ/tissue:  Date rec'd: 07/21/86  Acc #:  9

SKIN

CARBUNCLE

MALIGNANT MELANOMA

Organ/tissue:  Date rec'd: 07/02/86  Acc #:  7

BRONCHIAL BRUSHING CYTOLOGIC MATERIAL

SUSPICIOUS FOR MALIGNANT CELLS

SPUTUM

EM Date: JUL 18, 1986

IMMUNOFLUORESCENCE Date: JUL 18, 1986

Organ/tissue:  Date rec'd: 05/13/86  Acc #:  4

LUNG

CHEST PAIN, NOS

ANOREXIA

BIOPSY, ASPIRATION OF TISSUE OR FLUID

POSITIVE FOR MALIGNANT CELLS

Press return to continue or “^” to escape **&lt;Enter&gt;**

LABPATIENT1, FOUR 000-00-0014  DOB: FEB 1, 1912 LOC: 1 EAST

---------------------------------------------------------------------

CARCINOMA, SQ CELL

Organ/tissue:  Date rec'd: 03/09/86  Acc #:   2

Organ/tissue:  Date rec'd: 02/24/86  Acc #:   1

ELECTRON MICROSCOPY

Organ/tissue:  Date rec'd: 07/28/87  Acc #:  10

Report not verified.

Organ/tissue:  Date rec'd: //   Acc #: ?

Report not verified.

Organ/tissue:  Date rec'd: 07/03/86  Acc #:   1

KIDNEY

MITOCHONDRIAL ALTERATION

GLOMERULONEPHRITIS, MEMBRANOPROLIFERATIVE

IMMUNOFLUORESCENCE 890O8-K Date: JUL 6, 1986 08:55

Organ/tissue:  Date rec'd: 04/12/84  Acc #: 2319

LIVER

NORMAL TISSUE MORPHOLOGY

KIDNEY

ELECTRON MICROSCOPY

Organ/tissue:  Date rec'd: 04/12/84  Acc #: 2319

KIDNEY

IMMUNOFLUORESCENCE 3 Date: JUL 17, 1986

Organ/tissue:  Date rec'd: 03/04/84  Acc #:  23

KIDNEY

MITOCHONDRIAL ALTERATION

LYSOSOMAL DEBRIS

#### Display Final Path Reports by Accession Number [LRAPPA]

You can use this option to display final pathology reports which have been verified for surgical pathology, electron microscopy, or cytopathology from one accession to another.

Example:

Select Inquiry, anat path Option: **FR** DISPLAY FINAL PATH REPORTS BY ACCESSION #

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

SURGICAL PATHOLOGY FINAL PATIENT REPORTS DISPLAY

Enter year: 1991// **&lt;Enter&gt;** (1991)

Start with accession #: **1362**

Go to accession #: **1735**

Date Spec taken: JAN 11, 1991		Pathologist: LABPROVIDER2, TEN

Date Spec rec’d: JAN 12, 1991	Resident:

Date Completed: JAN 13, 1991	Accession #: 23

Submitted by: LABPROVIDER, ONE	Practitioner: LABPROVIDER, ONE

------------------------------------------------------------------

Specimen:
	PROSTATE CHIPS
Brief Clinical History:
	Nocturia and difficulty voiding urine.
Preoperative Diagnosis:
	Enlarged prostate.
Operative Findings:
	Same.
Gross description:
	Specimen consists of 25 grams of prostate gland tissue.
Microscopic exam/diagnosis:
	Prostate gland tissue showing glandular and stromal hyperplasia. In one chip of 134 there is a small focus of well differentiated adenocarcinoma.

### Log-in Menu, Anat Path [LRAPL]

**Menu Item	Description**

Log-In Anat Path	Used to log in accessions in Anatomic Pathology. You must hold the appropriate key to the accession area. The accession is never removed from the system automatically; it can be deleted through “Delete accession #,” if the report has not been completed and released. The comments entered are deleted through one of the two purge options in the Supervisor’s Menu, approximately every six months depending on the amount of disk space available.

Delete Accession #, Anat Path	Used to delete an accession number for autopsy, cytopath, EM, or surgical path if the report has not been completed and released.

Print Log Book	Prints accessions from one number to another within a year.

Histopathology Worksheet	Prints lists of specimens for a date by accession number.

Although the option used for log-in is the same for all areas, the prompts displayed will vary according to the area selected.

During specimen log-in, the system displays other accessions on that patient within five days. This should eliminate duplicate accessions when additional specimens are received for a case with multiple specimens.

If you enter a specimen name in the Log-in option, the Gross Description field in the Microscopic/Gross Review option will be automatically filled with an expanded specimen description from the specimen description file.

If a comment such as “incomplete clinical information” is entered into the system at the time of log-in, it will be printed out on the Log Book. It could then be used to flag surgical and cytologies submitted without adequate clinical information and clinical history. These could then be tallied and investigated as a quality assurance monitor for Anatomic Pathology. It also might be helpful in identifying specific individuals or locations from which incomplete or erroneous SF 515s are being received.

**NOTE:** The entry created in Field .07, Subfile 63.08, SURGEON/PHYSICIAN, is a pointer to the NEW PERSON file (#200). This is also stored in the ACCESSION file (#68) for that accession.

**NOTE:** CPRS v32a (OR*3.0*539) introduced the AP Order Dialog in CPRS which allows clinicians to place anatomic pathology orders via the LR OTHER LAB AP TESTS dialog. A new parameter in the LABORATORY SITE file (#69.9) named CPRS AP DIALG ON was also introduced. This parameter must be set to YES in order to allow log-in of orders created by the new AP Order Dialog. See Example 3 below.

HINTS:

If a “^” is entered at any point in the data entry, **except** during a multiple entry, the system will display a message and will delete the accession information.

If the CPRS AP DIALOG parameter has been set to YES in the LABORATORY SITE file (#69.9), a prompt of “Select Order number:” will be presented. Enter the Lab Order # created by the CPRS order at this prompt, or press Enter to continue with the previous log-in process.

If the system will not accept the patient you are trying to enter, there may be a spelling error or a SSN error on the SF 515 or in the computer, in which case you would correct the error before continuing. Another possibility is that the patient is an outside referral case of a non-VA patient. You must then enter the patient as a referral, as follows:

Example:

Select Patient Name: **?:?**

CHOOSE FROM: 1 PATIENT

2 PERSON

4 LAB CONTROL NAME

5 BLOOD DONOR

6 REFERRAL PATIENT

7 RESEARCH

8 STERILIZER

9 ENVIRONMENTAL

1. NON PATIENT WORKLOAD

11	NEW PERSON

Select: **6**

ANSWER WITH REFERRAL PATIENT NAME, OR IDENTIFIER, OR REFERRAL SOURCE

DO YOU WANT THE ENTIRE 18-ENTRY REFERRAL PATIENT LIST? **N** (NO)

Select REFERRAL PATIENT NAME: **LABPATIENT2, EIGHT**

ARE YOU ADDING ' LABPATIENT2, EIGHT’ AS A NEW REFERRAL PATIENT (THE 19TH)? **Y** (YES)

REFERRAL PATIENT DOB: **5-5-18** (MAY 05, 1918)

REFERRAL PATIENT IDENTIFIER: **0028**

LABPATIENT2, EIGHT ID: 0028

AGE: 76

PATIENT LOCATION: ???// 2E 2 EAST

Assign SURGICAL PATHOLOGY accession #: 19 ? YES// **^**

Then later in the option, you will probably want to enter the referring hospital/physician in the Comment field(s).

If you have attempted to enter a patient name and you are still at the “Select PATIENT NAME” level, the prompt will show PATIENT NAME in upper case. If this happens, you are in the PATIENT file (#2) already, and entry of “??” will not provide the choice of files, only a choice of patient names. Return to the option name level to begin again. The prompt will then display “Select Patient Name” in upper and lower case, and you will be able to get to the REFERRAL file. If you enter **REF:?** , you will automatically get a listing of patients already in the file.

When a log book is printed, a number will be shown in front of the patient’s name to indicate that it is a non-VA patient. The entries in the Comment field are also included.

**Example 1:** Log-in of Routine Surgical Path Specimen with ASK FROZEN SECTION set to “NO”

ANATOMIC PATHOLOGY MENU

Select Log-in menu, anat path Option: **L** Log-in, anat path

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

Log-In for 1990 ? YES// **&lt;Enter&gt;** (YES)

Select Patient Name: **LABPATIENT, SEVEN** 05-08-16 00-00-0007

LABPATIENT, SEVEN ID: 00-00-0007
AGE: 72 DATE OF BIRTH: MAY 8, 1916
PATIENT LOCATION: 1A// &lt;Enter&gt;

Checking surgical record for this patient...

No operations on record in the past 7 days for this patient.

Assign SURGICAL accession #: 22 ? YES// **&lt;Enter&gt;** (YES)
Date/time Specimen taken: TODAY// **&lt;Enter&gt;** (NOV 20, 1988)
SURGEON/PHYSICIAN: **LABPROVIDER, SEVEN &lt;Enter&gt;** SPECIMEN SUBMITTED BY: LABPROVIDER, SEVEN MD// **&lt;Enter&gt;** Select SPECIMEN: **PROSTATE CHIPS** Select SPECIMEN: **&lt;Enter&gt;** DATE/TIME RECEIVED: NOW// **&lt;Enter&gt;** (NOV 20, 1988@9:20)
PATHOLOGIST: **LABPROVIDER, THREE** Select COMMENT: **This comment will appear on the log book.** Select COMMENT: **&lt;Enter&gt;** Select Patient Name: **&lt;Enter&gt;**

Example 2:	Log-in of Frozen Section Specimen for Surgical Path

Select Log-in menu, anat path Option: **LI** Log-in, anat path

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

Log-In for 1992 ? YES// **&lt;Enter&gt;** (YES)

Select Patient Name: **LABPATIENT1, FIVE** 04-27-25   000000015   SC VETERAN

LABPATIENT1, FIVE ID: 000-00-0015 Physician: LABPROVIDER, THREE

AGE: 67 DATE OF BIRTH: APR 27, 1925

PATIENT LOCATION: EMERGENCY ROOM// SURGERY

Accession number assigned for 12/02/92 is: 24

Assign SURGICAL PATHOLOGY accession #: 26 ? YES// **&lt;Enter&gt;** (YES)

Date/time Specimen taken: TODAY// **&lt;Enter&gt;** (DEC 03, 1992)

SURGEON/PHYSICIAN: **LABPROVIDER, THREE** LABPROVIDER, THREE

SPECIMEN SUBMITTED BY: LABPROVIDER, THREE MD// **&lt;Enter&gt;**

Select SPECIMEN: **LEFT NOSE BIOPSY**

Select SPECIMEN: **&lt;Enter&gt;**

DATE/TIME SPECIMEN RECEIVED: NOW// **&lt;Enter&gt;** (DEC 03, 1992@10:45)

PATHOLOGIST: **LABPROVIDER, EIGHT** LABPROVIDER, EIGHT

Select COMMENT: **Call x3028 or x2420 with frozen results** (Call x3028 or x2420

with frozen results)

Select COMMENT: **&lt;Enter&gt;**

FROZEN SECTION:

1&gt; **, adequately excised** .

2&gt; **Reported to LABPROVIDER2, TWO at x2420 at 10:55AM** . .

3&gt; **&lt;Enter&gt;**

EDIT Option: **&lt;Enter&gt;**

**Example 3** : Log-in of Surgical Pathology Specimen when using the AP Order Dialog in CPRS

(NOTE: if the CPRS AP Dialog ON field in the LABORATORY SITE file (#69.9) is set to YES, log-in of orders created via the AP Order Dialog in CPRS is enabled. Entering the Lab Order # from the CPRS order will retrieve all information entered in the order dialog in CPRS. If nothing is entered at the prompt to “Select Order number”, the traditional log-in process will be used.)

Select Log-in menu, anat path &lt;TEST ACCOUNT&gt; Option: **LI  Log-in, anat path**

Select Performing Laboratory: ZZ ALBANY//     NY  VAMC  500

Select Order number: **167**

ALBANY,PATIENT                000-00-1234    Requesting location: LAB

Date/Time Ordered: 05/20/2021 13:06          By: USER,CPRS

-Lab Order # 167                           Provider: PROVIDER,DEMO

AP SPECIMEN  SKIN

DERMATOLOGY       ROUTINE Requested (WARD COL) for:  05/20/2021@13:06

+++++++++++++++   SPECIMEN DATA  +++++++++++++++

SPECIMEN: SKIN

SPECIMEN DESCRIPTION: SKIN Left Punch Biopsy 3mm

AP SPECIMEN: SKIN                     COLLECTION SAMPLE: AP SPECIMEN

=================   END OF SPECIMEN DATA ==================

PRESS '^' TO STOP

+++++++++++++++ DIALOG RESPONSE  +++++++++++++++

SUBSCRIPT: [SP]                       CPRS AP SCREEN: 124-DERMATOLOGY

SURGEON/PHYSICIAN: PROVIDER,DEMO

BRIEF CLINICAL HISTORY:

Mole with irregular margins on back of left hand

PREOPERATIVE DIAGNOSIS:

Possible Melanoma

================== END OF DIALOG RESPONSE ==================

PRESS '^' TO STOP

Do you wish to continue with this accession [Yes/No]? **YES**

PATHOLOGIST: **LABPROVIDER, EIGHT** LABPROVIDER, EIGHT

COLLECTION DATE/TIME: **T@1300** (MAY 20, 2021@13:00)

Checking surgical record for this patient...

ALBANY,PATIENT  MALE DOB:2/4/1964 SSN:000-00-1234

No operations on record in the past 7 days.

-------------------------------------

Display of CPRS data in LAB DATA file

-----------------------------------------------------------------------------

DATE/TIME SPECIMEN TAKEN: May 20, 2021 13:00

PATHOLOGIST: BELSCHWINDER,MICHAEL     SURGICAL PATH ACC #: SP 21 2

SURGEON/PHYSICIAN: PHYSICIAN,DEMO

PATIENT LOCATION: LAB

DATE/TIME SPECIMEN RECEIVED: MAY 20, 2021@13:09:13

-----------------------------------------------------------------------------

BRIEF CLINICAL HISTORY:

Mole with irregular margins on back of left hand

PREOPERATIVE DIAGNOSIS:

Possible Melanoma

--- End of CPRS data in LAB DATA file ---

****  Enter Next Order ****

Select Performing Laboratory: ZZ ALBANY//     NY  VAMC  500

Select Order number:

Example 4:	Log-in of Cytopathology Specimen

Select Log-in menu, anat path Option: **L** Log-in, anat path

Select ANATOMIC PATHOLOGY section: **CY** CYTOPATHOLOGY

Log-In for 1990 ? YES// **&lt;Enter&gt;** (YES)

Select Patient Name: **LABPATIENT, SEVEN** 05-08-16  000000007  NON-VETERAN (OTHER)

LABPATIENT, SEVEN ID: 000-00-0007  AGE: 74 DATE OF BIRTH: MAY 8, 1916

PATIENT LOCATION: 1A// **11b**

Assign CYTOPATHOLOGY accession #: 1 ? YES// **&lt;Enter&gt;** (YES)

Date/time Specimen taken: TODAY// **&lt;Enter&gt;** (AUG 28, 1990)

PHYSICIAN: **LABPROVIDER. THREE**

SPECIMEN SUBMITTED BY: LABPROVIDER, THREE// **&lt;Enter&gt;**

Select SPECIMEN: **Prostate chips**

Select SPECIMEN: **&lt;Enter&gt;**

DATE/TIME SPECIMEN RECEIVED: NOW// **&lt;Enter&gt;** (AUG 28, 1990@12:04)

PATHOLOGIST: **LABPROVIDER3, ONE**

Select COMMENT: **&lt;Enter&gt;**

GROSS DESCRIPTION:

1&gt;10 cc of tan viscous material submitted.

2&gt; **&lt;Enter&gt;**

EDIT Option:

Select Patient Name: **&lt;Enter&gt;**

**Example 5:** More than one EM Specimen

Select Anatomic pathology Option: **L** Log-in menu, anat path

Select Log-in menu, anat path Option: **L** Log-in, anat path

Select ANATOMIC PATHOLOGY section: EM

Log-In for 1992 ? YES// **&lt;Enter&gt;** (YES)

Select Patient Name: **LABPATIENT1, TWO** 06-18-62   000-00-0012

**LABPATIENT1, TWO** ID: 000-00-3333 Physician: LABPROVIDER3, TWO

AGE: 29 DATE OF BIRTH: JUN 18, 1962

PATIENT LOCATION: 1B// &lt;Enter&gt;

Assign EM accession #: 8 ? YES// **&lt;Enter&gt;** (YES)

Date/time Specimen taken: TODAY// **&lt;Enter&gt;** (JAN 13, 1992)

PHYSICIAN:  LABPROVIDER3, THREE

SPECIMEN SUBMITTED BY: LABPROVIDER3, FOUR // **&lt;Enter&gt;**

Select SPECIMEN: **SKIN**

Select SPECIMEN: **KIDNEY**

Select SPECIMEN: **&lt;Enter&gt;**

DATE/TIME SPECIMEN RECEIVED: NOW// **&lt;Enter&gt;** (JAN 13, 1992@10:39)

PATHOLOGIST: **LABPROVIDER, EIGHT** LABPROVIDER, EIGHT

RESIDENT OR EMTECH: LABPROVIDER3, FIVE

Select COMMENT: **&lt;Enter&gt;**

Example 6:	Log-in of Autopsy

ANATOMIC PATHOLOGY MENU

Select Anatomic pathology Option: **L** Log-in menu, anat path

Select Log-in menu, anat path Option: **LI** Log-in, anat path

Select ANATOMIC PATHOLOGY section: **AU** AUTOPSY

Log-In for 1992 ? YES// **&lt;Enter&gt;** (YES)

Select Patient Name: B9898 LABPATIENT, FOUR  12-18-25  000000004  NSC VETERAN

LABPATIENT, FOUR  ID: 000-00-0004 Physician: LABPROVIDER, THREE

DIED DEC 1, 1992

Assign AUTOPSY accession #: 5 ? YES// **&lt;Enter&gt;** (YES)

Enter Weights &amp; Measurements ? NO// **&lt;Enter&gt;** (NO)

AUTOPSY DATE/TIME: **T** (DEC 01, 1992)

LOCATION: **1A**

SERVICE: **MEDICINE**

TREATING SPECIALTY AT DEATH: **INTERNAL MEDICINE**

PHYSICIAN: LABPROVIDER1, SIX

RESIDENT PATHOLOGIST: **&lt;Enter&gt;**

SENIOR PATHOLOGIST: **&lt;Enter&gt;**

AUTOPSY TYPE: **F** FULL AUTOPSY

AUTOPSY ASSISTANT: **&lt;Enter&gt;**

NOTES:

•	Date of death must be entered in the PATIENT file (#2) before an autopsy can be entered.

•	The system will now allow nonstandard numeric defaults for weights; i.e., 11.0 rather than 11.

•	For quality assurance review purposes, a new field Treating Specialty at Death (63,14.6) has been added to the Log-in Anatomic Pathology [LRAPLG] option. If all of the data is entered, it is possible to have data on deaths sort by Service, Treating Specialty, and Physician using the QA Outcome Review Cases [LRAPQOR] option in the Supervisor’s Menu.

#### Delete Accession #, Anat Path [LRAPKILL]

This option will only work if the report has not been completed and/or verified.

Example:

Select Anatomic pathology Option: **L &lt;Enter&gt;** Log-in menu, anat path

Select Log-in menu, anat path Option: **DA** Delete accession #, anat path

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY
			Delete an Accession Number

Accession number date: **90** (1990)

Select Accession # : **22** LABPATIENT, SEVEN ID: 000000007 DOB: MAY 8, 1916

ACC # 22
Report completed &amp;/or released, deletion not allowed.

Select Accession # : **24** LABPATIENT1, EIGHT ID: 000-00-0018 DOB: JAN 23, 1934

ACC # 24 DATE RECEIVED: NOV 21, 1990 08:58 OK to DELETE ? NO// **&lt;Enter&gt;** (NO)
	NOT DELETED

Select Accession # : **24** LABPATIENT1, EIGHT ID: 000000018 DOB: JAN 23, 1934

ACC # 24 DATE RECEIVED: NOV 21, 1990 08:58 OK to DELETE ? NO// **Y** Select Accession # : **&lt;Enter&gt;** Select Log-in menu, anat path Option: &lt;Enter&gt;

#### Print Log Book [LRAPBK]

Once the specimens have been logged in, printing the log book provides a quick reference. If this report is then reprinted when the reports are completed and released, the final diagnoses (based on the SNOMED codes) and the release information will also be included.

Although specimens entered as “old records” are not entered in the ACCESSION file (#68), those accessions can be accessed using this option. This may be very helpful in resolving problems with duplicate numbers/data entry errors.

The “Log Book” serves as a quick reference and a viable alternative to having the system search for an accession number, but it is necessary for the person making the inquiry to know the approximate date. Printing a list of surgical pathology accessions by patient name, using this option on a monthly or quarterly basis, facilitates the inquiry process during computer downtimes.

Example:

Select Print, anat path Option: **Print log book** Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY 

		       SURGICAL PATHOLOGY LOG BOOK

Print SNOMED codes if entered ? NO// **Y** (YES)

Print only Topography and Morphology codes ? NO// **&lt;Enter&gt;**

Log book year: 1991 OK ? YES// **&lt;Enter&gt;** (YES)
Start with Acc #: **20** Go to Acc #: LAST // **22** Select Print Device: [Enter Print Device Here]

**NOTES:**

•	Use of the log-in Comment field for documentation of consultations or notification of malignancies as shown above provides one mechanism for documentation for quality assurance purposes.

•	Once the word-processing/description fields are purged, the log-in comments will no longer be included; therefore, if this log book is to be used for permanent hard copy of comments, it must be printed for the desired period before the word processing fields are purged.

#### Surgical Pathology Log Book

NOV 20, 1990 09:31 SURGICAL PATHOLOGY LOG BOOK for 1990	Pg: 1
# = Demographic data in file other than PATIENT file
Date 	Num	Patient		ID	  LOC	PHYSICIAN	PATHOLOGIST
-----------------------------------------------------------------------------
11/07	20	LABPATIENT1, FOUR	0014 	1A	LABPROVIDER, THREE	LABPROVIDER, THREE
Date specimen taken:11/07/90	Entered by:	LABPROVIDER3, SIX
		SKIN
------------------------------------------------------------------------------
11/08	21	LABPATIENT1, FOUR	0014	1A	LABPROVIDER1, TWO	LABPROVIDER, ONE
Date specimen taken:11/08/90	Entered by:	LABPROVIDER3, SIX
						Released by: LABPROVIDER3, SIX
		SNOMED codes:
		 SKIN
			Dx: PSORIASIS
			Procedure: BIOPSY, PUNCH
		 LIVER
			Dx: CIRRHOSIS: HEMANGIOMA
			Procedure: BIOPSY, NEEDLE
-----------------------------------------------------------------------------
11/20	22	LABPATIENT, SEVEN	0007 	1A	LABPROVIDER, SEVEN 	LABPROVIDER, THREE
Date specimen taken:11/20/90	Entered by:	LABPROVIDER3, SIX
				Released by:LABUSER, THREE
		PROSTATE 
			Dx: ADENOCARCINOMA
				Reviewed by LABPROVIDER3, SEVEN on 11/22/90
				Notified LABPROVIDER, THREE on 11/22/90

#### Histopathology Worksheet [LRAPH]

Once specimens have been logged in, this worksheet will provide a mechanism for recording data which will subsequently be entered, using the Blocks, Stains, Procedures, Surg Path [LRAPSPDAT] option. The worksheet includes all accessions and all specimens for each accession.

Example:

Select Print, anat path Option: **HW** Histopathology Worksheet
		HISTOPATHOLOGY DATA SHEET

```vista
Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY
Select ACCESSION DATE: **T** (NOV 20, 1990)
Select Print Device: [Enter Print Device Here]
```

R5ISC
		SURGICAL SHEET	ACCESSION DATE: NOV 20, 1990	  Pg: 1
------------------------------------------------------------------------------
	SURG	:	SPECIMEN		: CASSETTE	: BLOCKS	: SLIDES	: STAINS
-----------------------------------------------------------------------------
90-22	:	PROSTATE CHIPS	:				:			:			:
-----------------------------------------------------------------------------

**NOTE:** Some detailed training on how to review/edit the data will be necessary unless the user already has experience in dealing with this option, or other data entry options which involve multiple fields. Dealing with these multiples is not intuitive even to the more experienced user.

### Print, Anat Path [LRAPP]

#### Descriptions

**Option	Description**

Print All Reports on Queue	Prints a report listing the clinical history and gross description for review for patients on the cumulative report print queue, as well as final reports for patients and completed autopsy reports.

Delete Report Print Queue	Deletes the entries on the print queue list for the area specified.

List Pathology Reports in Print Queue	Displays a list of preliminary or final reports in a print queue.

Print Single Reports Only	Prints the report of pathology accessions in cytopath, EM, autopsy, or surgical path for cumulative reports for micro exams.

Add Patient(s) to Report Print	Adds patients to the report print queue. Queue for the area specified.

**Autopsy Administrative Reports:**

Autopsy Data Review	Review of autopsy data includes # of deaths, number of autopsies, autopsy %, cases with and without major diagnostic disagreements, and cases in which clinical diagnoses are clarified.

Alphabetical Autopsy List	List of autopsies from one date to another. Report includes patient name, the SSN, Autopsy number, and autopsy date.

**Option	Description**

Autopsy Status List	List of autopsies from one accession # to another within a year. Report includes Autopsy #, patient name, last four digits of the SSN, location, autopsy date, date of final autopsy diagnoses (FAD), and date autopsy completed.

**Anat Path Accession Reports:**

Anat Path Accession List by Date	Prints or displays an accession list for a specific date or a range of dates, alphabetically by patient or in ascending accession number order. If the cytopathology accessions were reviewed by a pathologist, “*” will appear after the slide count.

Anat Path Accession List by Number	Prints or displays an accession list for a specific accession number or range of numbers, by patients alphabetically or by ascending accession number.

Sum of Accessions by Date, Anat Path	Lists accession counts by day from one date to another with totals and number of patients.

Entries by Dates, Patient, 	Prints a list of accessions by

and Accession #	patient, with organ/tissue data, an accession # index, or (for cytopath) a calculation of the percent of positive

diagnoses, for specified dates.

List of Path Cases by Resident,	Prints or displays a list of the senior

Tech or Senior or Clinician	resident’s, technician’s, pathologist’s or clinician’s cases for a specified time.

% Pos, Atyp, Dysp, Neg, Susp, &amp; Unsat	Prints the number and % of positive,

Cytopath	negative, and suspicious specimens for malignancy and unsatisfactory specimens from one date to another.

**Option	Description**

Accession List With Stains	Lists histologic stains for a selected series of accessions.

Accession Counts by Senior Pathologist	Tallies cases by accession area, sorted by the senior pathologist assigned to the case. Contributes to analysis of quality assurance information, since this information relies on the total number of cases, as well as the data for the “outlyers.”

Cum Path Data Summaries	Cumulative summary of surgical path, EM, and autopsy for screen display or hard copy.

**Anatomic Pathology Labels:**

Anat Path Slide Labels	Allows labels to be printed for surgical

Anat Path Specimen Labels	path, cytopath, electron microscopy

Autopsy Slide Labels (generic)	and autopsy from one number to another within a year. If there is more than one specimen for an accession, a separate label will print for each specimen.

**Edit/Print/Display Preselected Lab Tests:**

Print/Display Preselected Lab Tests	Users can define lab tests and patient

Enter/Edit User Defined Lab Test	lists for display or to print, from one date to another. If tests are not defined by the user, the lab-defined list will be displayed.

Print Log Book	Prints accessions from one number to another within a year.

Print Final Path Reports by Accession	Prints accessions from one number to

Number	another within a year. Can be used to make tapes for microfiche.

#### Print Queue Information

A print queue is a list of reports to be printed. When a gross description for any accession is entered, that accession is added to the preliminary report print queue or list of accessions to be printed on demand. Likewise, when the microscopic description is entered, the accession is placed on the final report print queue. All reports on either of these queues may be printed at any time, usually daily. Please remember at some point to “kill” the queue before the next day’s reports are typed. If this is not done, the previous day’s reports will print again, as well as the current day’s, resulting in a lot of wasted paper and time. Either preliminary reports or final reports may be printed singly without affecting what is on either queue. Reports may also be added to either queue manually, using the Add Patient(s) to Report Print Queue [LRAP ADD] option, in an instance where the old or duplicate report needs to be reprinted.

#### Print All Reports on Queue [LRAP PRINT ALL ON QUEUE]

This option prints either preliminary reports listing the clinical history and gross description for review for patients on the cumulative report print queue or final reports for patients and completed autopsy reports.

**NOTE:** The Print All Reports on Queue [LRAP PRINT ALL ON QUEUE] option has been **modified** with the release of patch LR*5.2*248.

**NOTE:** When printing from the print queue, save the print queue until you verify that the reports have been printed successfully. If the printer has problems, runs out of paper, etc., it can be very frustrating to figure out what was in the print queue. If it prints successfully, the print queue can then be deleted. If it is not deleted at that point, that batch of reports will reprint the next time.

##### Example 1: Surgical Pathology Preliminary Report

Select Print, anat path Option: PQ Print all reports on queue

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

		1.	Preliminary reports
		2.	Final reports
Select 1 or 2 : 1 Preliminary reports

Preliminary reports for SURGICAL PATHOLOGY
Add/Delete reports to/from print queue for 1990? NO// N
Select Print Device: [Enter Print Device Here]

**Example 1:** Surgical Pathology Preliminary Report *continued*

------------------------------------------------------------------
MEDICAL RECORD :			SURGICAL PATHOLOGY		Pg 1
------------------------------------------------------------------
Submitted by: LABPROVIDER, SEVEN		Date obtained: NOV 20, 1990
------------------------------------------------------------------
Specimen:
PROSTATE CHIPS
------------------------------------------------------------------
Brief Clinical History:
	Nocturia and difficulty voiding urine.
------------------------------------------------------------------
Preoperative Diagnosis:
	Enlarged prostate.
------------------------------------------------------------------
Operative Findings:
	Same.
------------------------------------------------------------------
Postoperative Diagnosis:
	Same.

	Surgeon/physician: LABPROVIDER, SEVEN
==================================================================
					 PATHOLOGY REPORT
Laboratory: R5ISC					Accession No. SP90 22
------------------------------------------------------------------
			   **** REPORT INCOMPLETE ****

Gross description:		Pathology Resident: LABPROVIDER3, TWO

	Specimen consists of 25 grams of prostate gland tissue.

Microscopic exam/diagnosis:

------------------------------------------------------------------
									(End of report)
 LABPROVIDER, THREE				rg : Date
------------------------------------------------------------------
LABPATIENT, SEVEN				SURGICAL PATHOLOGY Report
ID:000-00-0007 SEX:M DOB:5/8/16 AGE:74 LOC:1A LABPROVIDER, SEVEN

**Example 1:** Surgical Pathology Preliminary Report *continued*

NOV 20, 1990 09:27 ANATOMIC PATHOLOGY R5ISC			Pg 2
------------------------------------------------------------------
LABPATIENT, SEVEN		SSN: 000-00-0007 DOB:5/8/16

				SURGICAL PATHOLOGY
	Organ/tissue:	Date rec'd: 11/20/90	Acc #:  22
	Report not verified.
	Organ/tissue:	Date rec'd: 06/04/89	Acc #:  22
	SKIN
		PSORIASIS
	Organ/tissue:	Date rec'd: 04/05/87	Acc #: 567
	SKIN OF FACE
		BASAL CELL CARCINOMA
	Organ/tissue:	Date rec'd: 02/01/85	Acc #:  12
	INGUINAL REGION
		HERNIA SAC
	Organ/tissue:	Date rec'd: 01/02/85	Acc #: 3456
	SKIN
		PSORIASIS
				CYTOPATHOLOGY
	Organ/tissue:	Date rec'd: 06/03/90	Acc #:  6
	SPUTUM
		NEGATIVE FOR MALIGNANT CELLS
	Organ/tissue:	Date rec'd: 07/09/88	Acc #: 4588
	URINE
		NEGATIVE FOR MALIGNANT CELLS
	Organ/tissue:	Date rec'd: 05/06/81	Acc #: 1233
	SPUTUM
		NEGATIVE FOR MALIGNANT CELLS
				ELECTRON MICROSCOPY
	Organ/tissue:	Date rec'd: 02/01/89	Acc #:  23
	KIDNEY
		GLOMERULONEPHRITIS, MESANGIAL PROLIFERATIVE
================================================================

##### Example 2: Surgical Pathology Final Patient Reports

You will need to decide whether the copy of the report to be charted should contain the SNOMED codes. If the report for the local pathology office file is to have the codes, but the one to be charted is not, you will have to print the reports on the print queue twice, answering the prompts differently each time.

Select Print, anat path Option: **PQ** Print all reports on queue

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY 

			1.	Preliminary reports
			2.	Final reports
Select 1 or 2 : **2** Final reports

				SURGICAL PATHOLOGY FINAL PATIENT REPORTS

Print SNOMED &amp;/or ICD codes on final report(s)? NO// **Y** (YES)

Save final report list for reprinting ? NO// **Y** (YES)
Select Print Device: *[Enter Print Device Here]*

**Example 2:** Surgical Pathology Final Patient Reports *continued*

MEDICAL RECORD :		SURGICAL PATHOLOGY			Pg 1
----------------------------------------------------------------------------
Submitted by: LABPROVIDER, SEVEN		Date obtained: NOV 20, 1990
----------------------------------------------------------------------------
Specimen:
PROSTATE CHIPS
----------------------------------------------------------------------------
Brief Clinical History:
	Nocturia and difficulty voiding urine.
----------------------------------------------------------------------------
Preoperative Diagnosis:
	Enlarged prostate.
----------------------------------------------------------------------------
Operative Findings:
	Same.
----------------------------------------------------------------------------
Postoperative Diagnosis:
	Same
					Surgeon/physician: LABPROVIDER, SEVEN
============================================================================
	   					 PATHOLOGY REPORT
Laboratory: R5ISC					Accession No. SP88 22
----------------------------------------------------------------------------
Gross description:	   Pathology Resident: LABPROVIDER3, TWO

	Specimen consists of 25 grams of prostate gland tissue.

Microscopic exam:
	Prostate gland tissue showing glandular and stromal hyperplasia. In one chip of 134 there is a small focus of well differentiated adenocarcinoma.

SURGICAL PATH DIAGNOSIS: Well differentiated adenocarcinoma.
SNOMED code(s):
T-77100: prostate
	M-814031: adenocarcinoma, well differentiated
	M-72000: hyperplasia
---------------------------------------------------------------------------
										(End of report)
LABPROVIDER, THREE				rg: Date NOV 20,.1990
---------------------------------------------------------------------------
LABPROVIDER, SEVEN				   SURGICAL PATHOLOGY Report
ID:000-00-0007 SEX:M DOB:5/8/16 AGE: 74 LOC: 1A  LABPROVIDER, SEVEN

##### Example 3: Surgical Pathology Report with Frozen Section

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

1. Preliminary reports

2. Final reports

Select 1 or 2 : **2**

SURGICAL PATHOLOGY FINAL PATIENT REPORTS

Add/Delete reports to/from print queue for 1992 ? NO// **&lt;Enter&gt;** (NO)

Print SNOMED &amp;/or ICD codes on final report(s) ? NO// **Y** (YES)

Save final report list for reprinting ? NO// **Y** (YES)

Select Print Device: *[Enter Print Device Here]*

**Example 3:** Surgical Pathology Report with Frozen Section *continued*

---------------------------------------------------------------------------

MEDICAL RECORD |          SURGICAL PATHOLOGY      Pg 1

---------------------------------------------------------------------------

Submitted by: LABPROVIDER, THREE        Date obtained: DEC 3, 1992

---------------------------------------------------------------------------

Specimen (Received DEC 3, 1992 10:45):

LEFT NOSE BIOPSY

---------------------------------------------------------------------------

Brief Clinical History:

---------------------------------------------------------------------------

Preoperative Diagnosis:

---------------------------------------------------------------------------

Operative Findings:

---------------------------------------------------------------------------

Postoperative Diagnosis:

Surgeon/physician: LABPROVIDER, THREE

===========================================================================
PATHOLOGY REPORT

Laboratory:  ISC-DEVELOPMENT ACCOUNT     Accession No. SP92 26

---------------------------------------------------------------------------

Gross Description

SCO a round skin biopsy measuring 1 x 1 x 0.5 cm. There is an ill

defined depressed central lesion. A suture marks the superior margin

which is inked in red. Inferior margin is inked in green, anterior

blue and posterior uninked. Representative sections embedded.

Frozen Section:

Basal cell , adequately excised. Reported to LABPROVIDER, THREE at x2420 at  10:55AM.

Microscopic Description

Residual basal cell carcinoma in biopsy site. Adequately excised.

See also S92-16.

SURGICAL PATH DIAGNOSIS: Basal cell carcinoma.

SNOMED code(s):

T-02140: skin of nose

M-80903: basal cell carcinoma

M-09400: surgical margins free of tumor

P-1141 : biopsy, excision

---------------------------------------------------------------------------

(End of report)

LABPROVIDER, EIGHT               lh | Date DEC 3, 1992

--------------------------------------------------------------------------

LABPATIENT1, FIVE                  STANDARD FORM 515

ID:000-00-0015 SEX:M DOB:4/27/25 AGE:67 LOC:SURGERY   LABPROVIDER, THREE

##### Example 4: Change in Prompts if you select the Autopsy Section

**NOTE:** The Autopsy section for the Print All Reports on Queue [LRAP PRINT ALL ON QUEUE] option has been **modified** with the release of patch LR*5.2*248 as follows:

If any ‘Autopsy supplementary report data has been modified after the report has been released the AUTOPSY SUPPLEMENTARY Modified Report audit information (e.g., Last modified: Aug 16, 2000 09:54 and typed by SMITH, JOHN) is now displayed. This information also appears for supplementary report data that appears on the Autopsy Protocol report.

The ‘Autopsy Protocols Report’ FOOTER has been modified by adding labels to the patient and physician names (i.e., Patient: and Physician:) of the report FOOTER to clearly distinguish between the two. The remaining data in the FOOTER has been realigned to allow for better readability.

The ‘Autopsy Protocol Report’ final page HEADER has been reformatted to allow for better readability. The report body displays the weights, measures, and SNOMED coding information.

**The shaded areas display changes made in the ‘Anatomic Pathology Report’ HEADER and FOOTERS.**

Select Anatomic pathology Option: **P** Print, anat path

Select Print, anat path Option: **PQ** Print all reports on queue

Select ANATOMIC PATHOLOGY section: **AU** AUTOPSY

1. Autopsy protocols

2. Autopsy supplementary reports

Select 1 or 2: **1&lt;Enter&gt;**

Autopsy Protocols

(D)ouble or (S)ingle spacing of report(s): **S&lt;Enter&gt;**

Print weights, measures and coding (if present): ? YES// **&lt;Enter&gt;** (YES)

Save protocol list for reprinting ? NO// **Y** (YES)

Select Print Device: *[Enter Print Device Here]*

**Example 4:** Change in Prompts if you Select the Autopsy Section *continued*

---------------------------------------------------------------------------

CLINICAL RECORD |         AUTOPSY PROTOCOL      Pg 1

---------------------------------------------------------------------------

Date died: DEC 1, 1992         | Autopsy date: DEC 1, 1992

Resident:                | FULL AUTOPSY Autopsy No. A92 5

---------------------------------------------------------------------------

Clinical History

1. Left CVA 2. Recurrent UTI 3. Aspiration pneumonia 4. Chronic renal failure

---------------------------------------------------------------------------

Anatomic Diagnoses

PATHOLOGICAL DIAGNOSIS:

1. Bilateral pulmonary edema with bilateral pleural effusion (500cc)

a. Organizing pneumonia right lung

b. Organizing pneumonia, right lung, with acute bronchitis

c. Calcified granuloma, left upper lobe (gross)

d. Emphysema (bilateral) and focal atelectasis (left)

2. a. Moderate arteriosclerosis of abdominal aorta

b. Cardiomegaly(480 gm) with left ventricular hypertrophy

c. Pericardial effusion with chronic peritonitis

d. Focal interstitial fibrosis

3. Bilateral granular kidneys with severe arterial and

arterionephrosclerosis and mesangeal thickening

a. 3 x 2 cm cyst left kidney

b. 0.3 x 0.3 cm hemorrhagic cysts, left kidney

c. Hemorrhagic bladder mucosa

d. Hemorrhagic bladder mucosa with chronic cystitis and prostatic

urethritis

4. Choletlithiasis with 25 stones (yellow, 0.5 to 1 cm)

a. Congested liver parenchyma

b. Diverticulosis, colon

GROSS BRAIN DIAGNOSIS: No pathologic diagnosis MICROSCOPIC BRAIN

DIAGNOSIS: pending - supplemental report to be issued.

CLINICO-PATHOLOGICAL CORRELATION

Patient was an

-----------------------------------------------------------------------------

Pathologist: LABPROVIDER, THREE            lh| Date DEC 2, 1992

----------------------------------------------------------------------------

ISC									AUTOPSY PROTOCOL

Patient: LABPATIENT, FOUR	000-00-0004		SEX: M	DOB: DEC 18, 1925

BON-AHMED/OPC		Physician: LABPROVIDER, THREE		AGE AT DEATH:66

DEC 2, 1992  08:10	 ISC						Pg: 2

ANATOMIC PATHOLOGY

----------------------------------------------------------------------------

LABPATIENT, FOUR	000-00-0004			DOB:DEC 18, 1925

Acc #: 5		AUTOPSY DATA		Age: 66

Date/time Died					Date/time of Autopsy DEC 1, 199 **2** FULL AUTOPSY		DEC 1, 1992

Resident: LABPROVIDER6, SEVEN			Senior:LABPROVIDER, THREE

SNOMED code(s):

T-28000: lung

M-36660: edema, lymphatic

M-32800: emphysema

M-49000: fibrosis

T-29000: pleura

M-36330: effusion, serosanguineous

T-28100: right lung

M-40000: inflammation

T-28600: left upper lobe of lung

M-44000: inflammation, granulomatous

T-71000: kidney

M-52200: arteriolosclerosis

T-57000: gallbladder

M-30010: lithiasis

T-56000: liver

M-36100: congestion

T-67000: colon

M-32710: diverticulosis

T-42000: aorta

M-52000: arteriosclerosis

T-33010: myocardium

M-71000: hypertrophy

-------------------------------------------------------------------------------

Pathologist: LABPROVIDER, THREE           lh | Date DEC 2, 1992

-------------------------------------------------------------------------------

ISC									AUTOPSY PROTOCOL

Patient: LABPATIENT, FOUR	000-00-0004		SEX: M	DOB: DEC 18, 1925

MEDICINE			Physician: LABPROVIDER, THREE		AGE AT DEATH:66

#### Delete Report Print Queue [LRAP DELETE]

Deletes all entries on the report queue for the accession area that is selected.

Select Print, anat path Option: **DQ** Delete report print queue

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

		1.	Preliminary reports
		2.	Final reports
Select 1 or 2 : **2** SURGICAL PATHOLOGY FINAL PATIENT REPORTS

OK TO DELETE THE SURGICAL PATHOLOGY FINAL REPORT LIST? NO// **Y** (YES)
LIST DELETED !

#### List Pathology Reports in Print Queue [LRAPQ]

Whenever data is entered through the Gross Description/Clinical Hx [LRAPDGD] option for any accession area, the system will automatically place the patient in the print queue for preliminary reports. When data is entered through the other data entry options (i.e., those for final surgical path reports, modified reports or supplementary reports), the patient is automatically placed in the print queue for final reports.

**Example 1:** Surgical Pathology Preliminary Report

Select Anatomic pathology Option: **P** Print, anat path

Select Print, anat path Option: **LQ** List pathology reports in print queue
Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY 

			List of pathology reports in print queue

		1.	Preliminary reports
		2.	Final reports
Select 1 or 2 : **1** Select Print Device: [Enter Print Device Here]

-----------------------------------------------------------------------------
			SURGICAL PATHOLOGY PRELIMINARY REPORTS IN PRINT QUEUE	Pg: 1
Acc #	Date			Patient							SSN
	22	11/20/90	 	LABPATIENT, SEVEN		     000-00-0007
=============================================================================

**Example 2:** Surgical Pathology Final Report

ANATOMIC PATHOLOGY MENU

Select Anatomic pathology Option: **P** Print, anat path

Select Print, anat path Option: **LQ** List pathology reports in print queue
Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

			List of pathology reports in print queue

		1.	Preliminary reports
		2.	Final      reports
Select 1 or 2 : **2** Select Print Device: [Enter Print Device Here]

Acc #	Date	Patient					SSN
5	05/09/90	LABPATIENT1, FOUR			000-00-0014
15	08/11/90	LABPATIENT2, NINE			000-00-0029
21	11/08/90	LABPATIENT1, FOUR			000-00-0014
22	11/20/90	LABPATIENT, SEVEN			000-00-0007

#### Print Single Report Only [LRAP PRINT SINGLE] option

This option prints pathology accessions in Cytopath report for EM, autopsy, or surgical path for cumulative reports for micro exams.

Example:	Preliminary Reports

Select Anatomic pathology Option: **P** Print, anat path

Select Print, anat path Option: **PS** Print single report only

Select ANATOMIC PATHOLOGY section: **EM**

1. Preliminary reports

2. Final    reports

Select 1 or 2 : **1**

Preliminary reports for EM

Select PATIENT NAME: LABPATIENT1, FOUR. 02-01-12 0000000014 NO NSC VETERAN

LABPATIENT1, FOUR ID: 000-00-0014 Physician: LABPROVIDER2, EIGHT

AGE: 77 DATE OF BIRTH: FEB 1, 1912

Ward on Adm: 1 EAST Service: PSYCHOLOGY

Adm Date: JUL 8, 1990 10:53 Adm DX: STRESS

Present Ward: 1 EAST          MD: LABPROVIDER, SEVEN

Specimen(s)   Count #  Accession #  Date

( 1)      10    JUL 28, 1990 not verified

( 2)      6    JUN 10, 1990 not verified

( 3)      1    JUL 3, 1989 KIDNEY BIOPSY

( 4)     2319    APR 12, 1989 SPUTUM

More accessions ? NO// **&lt;Enter&gt;** (NO)

Choose Count #(1-4): **1**

Accession #: 10  Date: JUL 28, 1990

Select Print Device: *[Enter Print Device Here]*

MEDICAL RECORD |      EM                Pg 1

-----------------------------------------------------------------

Submitted by: LABPROVIDER1, TWO Date obtained: JUL 28, 1990

------------------------------------------------------------------

Specimen (Received JUL 28, 1990 12:35):

------------------------------------------------------------------

Brief Clinical History:

------------------------------------------------------------------

Preoperative Diagnosis:

------------------------------------------------------------------

Operative Findings:

------------------------------------------------------------------Postoperative Diagnosis:

Surgeon/physician: LABPROVIDER3, EIGHT

==================================================================

PATHOLOGY REPORT

Laboratory: SIUG, VAMC            Accession No. EM90 10

------------------------------------------------------------------

Prepared by: IFCAP ADPAC

Gross description:

This is where the gross description should be entered.

Microscopic description:

This is where the microscopic examination description should be

entered.

------------------------------------------------------------------

(See next page)

LABPROVIDER2, ONE              ec | Date SEP 2, 1994

------------------------------------------------------------------

LABPATIENT1, FOUR               STANDARD FORM 515

ID:000-00-0002 SEX:M DOB:2/1/12 AGE:77 LOC:AMBULATORY SURGERY

LABPROVIDER3, EIGHT

DEC 1, 1989 11:41  SIUG                  Pg: 2

ANATOMIC PATHOLOGY

------------------------------------------------------------------

SURGICAL PATHOLOGY

Organ/tissue:    Date rec'd: 03/28/90   Acc #:  9

Report not verified.

Organ/tissue:    Date rec'd: 11/08/89   Acc #: 21

SKIN

PSORIASIS

IMMUNOFLUORESCENCE 21-I Date: NOV 13, 1989

LIVER

PAIN, NOS

LOSS OF VOICE

DIABETES MELLITUS

TUBERCULOSIS

CIRRHOSIS

ALCOHOL

HEMANGIOMA

ELECTRON MICROSCOPY E-21-88 Date: NOV 13, 1989 06:27

Organ/tissue:    Date rec'd: 11/07/89   Acc #: 20

Report not verified.

Organ/tissue:    Date rec'd: 08/01/89   Acc #: 12

NAIL OF TOE

HEMATOMA

Organ/tissue:    Date rec'd: //      Acc #: 345

Report not verified.

Organ/tissue:    Date rec'd: 06/02/89   Acc #:  7

SKIN

PAIN, NOS

DIABETES MELLITUS, ADULT ONSET TYPE

PSORIASIS

ABSCESS

STAPHYLOCOCCUS AUREUS

Organ/tissue:    Date rec'd: 05/10/89   Acc #:  5

Report not verified.

Organ/tissue:    Date rec'd: 07/31/88   Acc #: 12

ACHILLES TENDON

ACQUIRED DIGITAL FIBROKERATOMA

Organ/tissue:    Date rec'd: 07/31/88   Acc #: 475

Report not verified.

Organ/tissue:    Date rec'd: 03/05/88   Acc #: 457

Report not verified.

Organ/tissue:    Date rec'd: 02/09/88   Acc #: 456

SKIN

BASAL CELL CARCINOMA

Organ/tissue:    Date rec'd: 01/03/88   Acc #:  1

SKIN

CHRONIC INFLAMMATION

DEC 1, 1989 11:41  SIUG                  Pg: 3

ANATOMIC PATHOLOGY

------------------------------------------------------------------

LABPATIENT1, FOUR        SSN:000-00-0014 DOB:2/1/12

CYTOPATHOLOGY

Organ/tissue:    Date rec'd: 09/25/90   Acc #:  7

SPUTUM

CARBUNCLE

Organ/tissue:    Date rec'd: 08/22/90   Acc #:  6

Report not verified.

Organ/tissue:    Date rec'd: 05/04/90   Acc #:  1

SPUTUM

NEGATIVE FOR MALIGNANT CELLS

Organ/tissue:    Date rec'd: 08/04/89   Acc #:  35

Report not verified.

Organ/tissue:    Date rec'd: 08/03/89   Acc #:  34

Report not verified.

Organ/tissue:    Date rec'd: 08/03/89   Acc #:  33

Report not verified.

Organ/tissue:    Date rec'd: 07/31/89   Acc #:  14

Organ/tissue:    Date rec'd: 07/31/89   Acc #:  15

ABDOMEN

ACQUIRED DIGITAL FIBROKERATOMA

Organ/tissue:    Date rec'd: 07/31/89   Acc #:  30

Report not verified.

Organ/tissue:    Date rec'd: 07/31/89   Acc #:  29

Report not verified.

Organ/tissue:    Date rec'd: 06/10/89   Acc #:  24

Organ/tissue:    Date rec'd: 06/10/89   Acc #:  23

Organ/tissue:    Date rec'd: 06/10/89   Acc #:  22

Organ/tissue:    Date rec'd: 05/06/89   Acc #:  12

Report not verified.

Organ/tissue:    Date rec'd: 03/05/89   Acc #:  11

Report not verified.

SPUTUM

POSITIVE FOR MALIGNANT CELLS

Organ/tissue:    Date rec'd: 08/20/88   Acc #:  10

Organ/tissue:    Date rec'd: 07/21/88   Acc #:  9

SKIN

CARBUNCLE

MALIGNANT MELANOMA

Organ/tissue:    Date rec'd: 07/18/88   Acc #: 2319

BRONCHIAL CYTOLOGIC MATERIAL

ATYPIA, MILD

Organ/tissue:    Date rec'd: 07/08/88   Acc #:  8

SPUTUM

Organ/tissue:    Date rec'd: 07/02/88   Acc #:  7

BRONCHIAL BRUSHING CYTOLOGIC MATERIAL

#### Add Patient(s) to Report Print Queue [LRAP ADD]

This option allows you to add a patient or patients to a print queue without having to go back into the report and reverify.

Example:

Select Print, anat path Option: **AD** Add patient(s) to report print queue

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

			1.	Preliminary reports
			2.	Final reports
Select 1 or 2 : **2** SURGICAL PATHOLOGY FINAL PATIENT REPORTS
Select Patient Name: **LABPATIENT2, TEN** 07-06-84  000-00-0210
LABPATIENT2, TEN ID: 000-00-0210 Physician: LABROVIDER1, TWO

AGE: 10 DATE OF BIRTH: JUL 6, 1984
Ward on Adm: 2 EAST Service: PEDIATRICS

Adm Date: APR 8, 1994 10:53 Adm DX: FEVER

Present Ward: 1 EAST          MD: LABPROVIDER3, NINE
Specimen(s)			Count #	Accession #	Date
						( 1)		   123	AUG 31, 1994
  Accession #: 123  Date: AUG 31, 1994

Select Patient Name: **&lt;Enter&gt;** Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

			1.	Preliminary reports
			2.	Final      reports
Select 1 or 2 : **2** SURGICAL PATHOLOGY FINAL PATIENT REPORTS
Select Patient Name: **LABPATIENT, SEVEN** 05-08-16    000000007
LABPATIENT, SEVEN ID: 000-00-0007
AGE: 74 DATE OF BIRTH: MAY 8, 1916

Ward on Adm: 3 EAST Service: UROLOGY

Adm Date: SEP 4, 1993 10:53 Adm DX: PAIN

Present Ward: 1 EAST          MD: LABPROVIDER1, SEVEN

Specimen(s)			Count #		Accession #	Date
						( 1)		    22		SEP 6, 1994
PROSTATE CHIPS
						( 2)		    22		JUN 4, 1989
						( 3)		   567		APR 5, 1986
						( 4)		    12		FEB 1, 1984
More accessions ? NO// **&lt;Enter&gt;** (NO)
		Choose Count #(1-4) : **1** Accession #: 22  Date: SEPV 6, 1994

Select Patient Name: **&lt;Enter&gt;** Autopsy Administrative Reports [LRAPAUP]

##### Autopsy Data Review [LRAPAURV]

Use this option to obtain information on the percent of deaths on which autopsies are performed and the number of cases in which the autopsy provided information which either clarified or contradicted the clinical diagnosis. The option searches the patient file for deaths occurring within the specified time. It tallies the number of deaths and the number of autopsies as well as the data entered through the Final Autopsy Diagnosis Date [LRAPAUFAD] option.

Example:

Select Print, anat path Option: **AU** Autopsy administrative reports

AD	Autopsy data review

AA	Alphabetical autopsy list

AS	Autopsy status list

Select Autopsy administrative reports Option: **AD** Autopsy data review
Start with Date TODAY// **&lt;Enter&gt;** SEP 08, 1993
Go  to  Date TODAY// **1/1/90** (JAN 01, 1990)

Count only in-patient deaths ? YES// **&lt;Enter&gt;** (YES)
Select Print Device: [Enter Print Device Here]

SEP 8, 1993 14:44  VAMC                       Pg: 1

AUTOPSY DATA REVIEW (JAN 1, 1990-SEP 8, 1993)

|DIAGNOSTIC     | CLINICAL DIAGNOSIS

|----------In-patient-------------|DISAGREEMENT    | CLARIFIED

Autopsy  Autopsy date      | Yes    No   | Yes  No  Verified

-----------------------------------------------------------------------------

A90  1  MAY 31, 1990 12:00         X     X

A93  1  MAY 11, 1993 15:56    X          X

A93  2  MAY 11, 1993 15:58    X          X

A93  3  MAY 11, 1993 16:03    X          X

A93  4  MAY 11, 1993 16:07    X          X

A93  5  JUN 20, 1993       X          X

A93  6  AUG 6, 1993 12:57    X          X

A93  8  AUG 6, 1993 13:09    X          X

Please hold, calculating Autopsy% ...

SEP 8, 1993 14:44  VAMC                       Pg: 2

AUTOPSY DATA REVIEW (JAN 1, 1990-SEP 8, 1993)

|DIAGNOSTIC     | CLINICAL DIAGNOSIS

|----------In-patient-------------|DISAGREEMENT    | CLARIFIED

# Deaths # Autopsies  Autopsy% |#Yes   #No   | #Yes  #No  Verified

-----------------------------------------------------------------------------

10     8    80.0    7     1    8

##### Alphabetical Autopsy List [LRAPAUA]

This option provides a list of autopsies from one date to another and is meant to replace a site’s card file of autopsies.

Example:

Select Anatomic pathology Option: **P** Print, anat path

Select Print, anat path Option: **AU** Autopsy administrative reports

Select Autopsy administrative reports Option: **AA** Alphabetical autopsy list

Start with Date TODAY// **&lt;Enter&gt;** DEC 24, 1991

Go  to  Date TODAY// **1/1** (JAN 01, 1991)

Select Print Device: *[Enter Print Device Here]*

DEC 24, 1991 05:42  VAMC                     Pg: 1

Autopsy List from JAN 1, 1991 to DEC 24, 1991

Patient              SSN     Autopsy#  Autopsy Date

-------------------------------------------------------------------------

LABPATIENT3, ONE      000-00-0031   AU91-23  3/23/91

##### Autopsy Status List [LRAPAUSTATUS]

This option produces a list of autopsies from one accession # to another within a year. The report includes Autopsy #, patient name, last four digits of the SSN, location, autopsy date, date of Final Autopsy Diagnoses (FAD), and date autopsy completed.

Example:

Select Autopsy administrative reports Option: **AS** Autopsy status list

				AUTOPSY STATUS LIST
Select year: **90** (1990)
Start with Acc #: **1** Go   to  Acc #: LAST // **&lt;Enter&gt;** Select Print Device: [Enter Print Device Here]

SEP 12, 1988 10:22		LABORATORY SERVICE R5ISC			Pg: 1
Autopsy Status List		   |---------------Date -----------|
Acc#	Patient		ID		Loc	Autopsy	PAD		FAD	Completed Pathologist(s)

1 LABPATIENT, FIVE	0005 CCC	4/26/88	4/26/88	4/26/88	4/26/88	LABPROVIDER2, TWO
																						LABPROVIDER, ONE
	2 LABPATIENT, ONE	0001 1A		7/28/88	7/29/88	7/29/88	7/29/88	LABPROVIDER, ONE
																						LABPROVIDER3, TWO

#### Anat Path Accession Reports [LRAPPAR]

##### Anat Path Accession List by Date [LRAPPAD]

This patient report, printed monthly or quarterly, provides a valuable resource during computer downtime or for those times in which the exact date of the specimen is unknown.

**Example 1:**

Select Anatomic pathology Option: **P** Print, anat path

Select Print, anat path Option: **AR** Anat path accession reports

Select Anat path accession reports Option: **LD** Anat path accession list by date

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY 

						SURGICAL PATHOLOGY ACCESSION LIST
Start with Date TODAY// **&lt;Enter&gt;** (NOV 21, 1990)
Go  to   Date TODAY// **T-7** (NOV 07, 1990)

List by (A)ccession number (P)atient : **A** ccession number
Select Print Device: [Enter Print Device Here]

NOV 21, 1990 14:29 VAMC                         Pg: 1
LABORATORY SERVICE SURGICAL PATHOLOGY (NOV 07, 1990 - NOV 21, 1990) 
# - Not VA patient													% = Incomplete
Acc #	Date Patient				ID		Loc 	Physician
------------------------------------------------------------------------------
22		11/20	LABPATIENT, SEVEN	0007	1A	LABPROVIDER, SEVEN	PROSTATE
	 This comment will appear on the log book.
23		11/21	LABPATIENT, ONE	8472	1A	LABPROVIDER, SEVEN	SKIN		%No SNOMED code

Example 2:	Anat path accession reports

Select Print, anat path Option: **AR** Anat path accession reports

Select Anat path accession reports Option: **LD** Anat path accession list by date

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

SURGICAL PATHOLOGY ACCESSION LIST
Start with Date TODAY// **&lt;Enter&gt;** SEP 02, 1994
Go  to   Date TODAY// **T-29** (AUG 09, 1990)

List by (A)ccession number (P)atient : **P** atient 
Select Print Device: [Enter Print Device Here]

SEP 07, 1994 14:29	VAMC															Pg: 1
LABORATORY SERVICE SURGICAL PAT ACCESSIONS (AUG 9, 1994 - SEP 7, 1994) 
# -  patient										% = Incomplete
Count	ID		Patient					Acc#

1) 0032 #LABPATIENT3, TWO    12 08/30 1 WEST No SNOMED code

14 08/30 2 EAST No SNOMED code

2) 0033 #LABPATIENT3, THREE   13 08/30 1 WEST No SNOMED code

3) 0021 LABPATIENT2, ONE     6 08/25 1 EAST No SNOMED code

7 08/25 1 EAST LEG

4) 0034 LABPATIENT3, FOUR    16 09/02 AMBULAT No SNOMED code

17 09/03 AMBULAT No SNOMED code

5) 0035 LABPATIENT3, FIVE    11 08/27 RED CLI TOE

6) 0036 LABPATIENT3, SIX     10 08/26 1 EAST No SNOMED code

7) 0037 LABPATIENT3, SEVEN    2 08/24 1 EAST PROSTATIC FASCIA

8) 0038 LABPATIENT3, EIGHT    1 08/10 1 EAST No SNOMED code

9) 0039 LABPATIENT3, NINE     4 08/24 1 WEST PROSTATE

##### Anat Path Accession List by Number [LRAPPAN]

Prints or displays an accession list for a specific accession number or range of numbers, by patients, alphabetically, or by ascending accession number.

**Example 1:** List by Accession number

Select Anat path accession reports Option: **LN** Anat path accession list by number

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY 

          SURGICAL PATHOLOGY ACCESSION LIST

Accession list date: 1994 OK ? YES// **&lt;Enter&gt;** (YES)
Start with Acc #: **1** Go  to  Acc #: LAST// **17** LIST BY PATIENT ? NO// **&lt;Enter&gt;** (NO)
Select Print Device: [Enter Print Device Here]

-----------------------------------------------------------------------------
SEP 08, 1994 14:30 				 														Pg: 1

LABORATORY SERVICE SURGICAL PATHOLOGY ACCESSIONS for 1994		
# -  patient												 % = Incomplete

Acc num   Patient     ID  Loc      Organ/tissue

-----------------------------------------------------------------------------

1 LABPATIENT3, EIGHT   0038 P 1 EAS %   No SNOMED code

2 LABPATIENT3, SEVEN   0037 1 EAS     PROSTATIC FASCIA

3 LABPATIENT2, FIVE   0025 1 EAS     LIVER

4 LABPATIENT3, NINE   0039 1 WES     PROSTATE

5 LABPATIENT3, EIGHT   0038 1 NOR     SKIN OF NOSE

6 LABPATIENT2, ONE    0021 1 EAS %    No SNOMED code

7 LABPATIENT2, ONE    0021 1 EAS     LEG

8 LABPATIENT2, SIX    0026 5 NOR     BONE MARROW

10 LABPATIENT3, SIX    0036 1 EAS     No SNOMED code

11 LABPATIENT3, FIVE   0035 RED C     TOE

12 #LABPATIENT3, TWO   0032 1 WES     No SNOMED code

13 #LABPATIENT3, THREE  0033 1 WES %    No SNOMED code

14 #LABPATIENT3, TWO   0032 2 EAS %    No SNOMED code

15 LABPATIENT2, SIX    0026 5 NOR %    No SNOMED code

16 LABPATIENT3, FOUR   0034 AMBUL     No SNOMED code

17 LABPATIENT3, FOUR   0034 AMBUL %    No SNOMED code

**Example 2:** List by Patient

Select Anat path accession reports Option: **LN** Anat path accession list by number 
Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY 

				SURGICAL PATHOLOGY ACCESSION LIST

Accession list date: 1994 OK ? YES// **&lt;Enter&gt;** (YES)
Start with Acc #: **5** Go  to  Acc #: LAST// **12** LIST BY PATIENT ? NO// **Y** Select Print Device: *[Enter Print Device Here]*

-----------------------------------------------------------------------------SEP 08, 1994 14:30	VAMC							Pg: 1

LABORATORY SERVICE SURGICAL PATHOLOGY ACCESSIONS for 1988

# -  patient				% = Incomplete

Count ID  Patient        ACC#   Organ/tissue

--------------------------------------------------------------------------

1) 0032 #LABPATIENT3, TWO     12   No SNOMED code

2) 0021 LABPATIENT2, ONE      6 %  No SNOMED code

7   LEG

3) 0035 LABPATIENT3, FIVE     11   TOE

4) 0036 LABPATIENT3, SIX      10   No SNOMED code

5) 0024 LABPATIENT2, FOUR      5   SKIN OF NOSE

6) 0026 LABPATIENT2, FSIX      8   BONE MARROW

##### Sum of Accessions by Date, Anat Path [LRAPA]

This option lists accession counts by day from one date to another, with totals and number of patients.

Select Anat path accession reports Option: **SD** Sum of accessions by date, anat path

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

SURGICAL PATHOLOGY ACCESSION/SPECIMEN LIST COUNT BY DAY

Start with Date TODAY// **&lt;Enter&gt;** SEP 08, 1995
Go  to   Date TODAY// **1/1/90** (JAN 01, 1990)
Select Print Device: [Enter Print Device Here]

SEP 8, 1994 18:32   ISC, VERIFICATION ACCT          Pg: 1

SURGICAL PATHOLOGY ACCESSION/SPECIMEN COUNT BY DATE

FROM JAN 1, 1990 TO SEP 8, 1994

DATE           Accession Count   Specimen count

---------------------------------------------------------------------------

APR 30, 1990           1          1

MAY 1, 1990           1          1

AUG 24, 1990           1          1

AUG 10, 1994           1          2

AUG 24, 1994           4          4

AUG 25, 1994           3          3

AUG 26, 1994           2          2

AUG 27, 1994           1          1

AUG 30, 1994           3          3

SEP 2, 1994           2          2

SEP 3, 1994           1          1

---------      ---------

Total number          20         21

Total Patients: 16

##### Entries by Dates, Patient and Accession Number [LRAPPF]

Although this report provides much of the same information as that from Accession List by Date [LRAPPAD] option or Print Log Book [LRAPBK] option, the summary here is by patient and also includes the SNOMED-coded diagnoses. It can be used to provide a full hard copy of the patient’s cumulative summary during computer downtimes. This report should either be printed for short periods of time or during non-peak hours, since it includes **all** patients within the time specified, and will be quite lengthy.

Example:

Select Anat path accession reports Option: **PD** Entries by dates,patient &amp; accession #

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

		SURGICAL PATHOLOGY Entries by Patient &amp; Accession # Index

Start with Date TODAY// **&lt;Enter&gt;** NOV 21, 1990
Go   to  Date TODAY// **T-14** (NOV 07, 1990)
Select Print Device: *[Enter Print Device Here]*

LABPATIENT, SEVEN			000-00-0007		BORN: MAY 8, 1916
	Organ/tissue:	Date rec'd: 11/21/90	  Acc #:	23
	Report not verified.
	Organ/tissue:	Date rec'd: 11/20/90	  Acc #:	22
	PROSTATE 25 GM
		ADENOCARCINOMA, WELL DIFFERENTIATED
		HYPERPLASIA

LABPATIENT1, FOUR			000-00-014		BORN: FEB 1, 1912
	Organ/tissue:	Date rec'd: 11/08/90	  Acc #:	21
	SKIN
		PSORIASIS
	LIVER
		PAIN
		DIABETES MELLITUS
		CIRRHOSIS
		  ALCOHOL
	Organ/tissue:	   Date recorded: 11/07/90			Acc #:	20
	Report not verified.

NOV 21, 1990 14:32															Pg 1
SURGICAL ACCESSION INDEX (from: NOV 7, 1990 to: NOV 21,90 )
YEAR Acc# Entry						Identifier			File	
------------------------------------------------------------------

1990 :

20	LABPATIENT1, FOUR	0OOOOOO14			REFERRAL PT

21	LABPATIENT1, FOUR	0OOOOOO14

22	LABPATIENT, SEVEN	000000007			RESEARCH

23	LABPATIENT, SEVEN	000000007

##### List of Path Cases by Resident, Tech, Senior or Clinicians [LRAPAUL]

This option provides a comprehensive listing, for pathology residents, senior pathologists, or clinicians of all cases within the specified time. It is particularly useful for residents needing to document a particular number/type of cases in the specified accession area.

Example:

Select Print, anat path Option: **AR** Anat path accession reports

Select Anat path accession reports Option: **WK** List of path cases by resident, tech or senior

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY 

		1.	SURGICAL PATHOLOGY list by Resident Pathologist
		2.	SURGICAL PATHOLOGY list by Senior  Pathologist

3.	SURGICAL PATHOLOGY list by Surgeon/Physician
Select 1 - 3: **1** Select Resident Pathologist: **ANEY, RUSS** Start with Date TODAY// **&lt;Enter&gt;** NOV 21, 1990
Go  to   Date TODAY// **1 1** (JAN 01, 1990)

Print Topography and Morphology entries ? NO// **Y** (YES)
Select Print Device: [Enter Print Device Here]

-----------------------------------------------------------------------------
NOV 21, 1990  14:34 R5ISC                   Pg:1
R. ANEY's SURGICAL PATHOLOGY list from:JAN 1, 1990 to:NOV 21,1990
Count	Case#        Case date	Patient/SSN
-----------------------------------------------------------------------------

1)	17	       09/09/90	LABPATIENT2, THREE	000-00-0023
		PROSTATE
		     HYPERPLASIA, GLANDULAR AND STROMAL
2)	22          11/20/90		LABPATIENT,SEVEN	000-00-0007
		PROSTATE
		     ADENOCARCINOMA, WELL DIFFERENTIATED
		     HYPERPLASIA
3)	 23	         11/21/90	LABPATIENT,SEVEN	000-00-0007
		SKIN
		     PSORIASIS

##### .% Pos, Atyp, Dysp, Neg, Susp, &amp; Unsat : Cytopath [LRAPCYPCT]

Use this option to print the number and % of positive, negative, and suspicious specimens for malignancy and unsatisfactory specimens from one date to another. The listing provides information that will assist in meeting a requirement of the College of American Pathologists (CAP).

If you wish to use the same topography list on a regular basis, these topography categories can be entered in the Edit Pathology Reports Parameters [LRAPDHR] option.

If you wish to specify morphology codes, these codes can be entered in the [LRAPDHR] option under MORPHOLOGY ENTRY. If there are no entries, the SNOMED codes that will be used for the search are as follows:

M09010	Unsatisfactory specimen

M09460	Negative for malignant cells

M69760	Suspicious for malignant cells

M80013	Positive for malignant cells

**Example 1:**

Select Anat path accession reports Option: **CP** % Pos, Atyp, Dysp, Neg, Susp, &amp; Unsat cytopath 

					Cytology Specimens:

Use morphology list? YES// **&lt;Enter&gt;** (YES)

UNSATISFACTORY SPECIMEN
				 NEGATIVE FOR MALIGNANT CELLS

SUSPICIOUS FOR MALIGNANT CELLS
				 POSITIVE FOR MALIGNANT CELLS

Use topography category list? YES// **NO** Select 1 or more characters of SNOMED TOPOGRAPHY code (Choice # 1): **2** ENTER IDENTIFYING COMMENT: **RESPIRATORY** Select 1 or more characters of SNOMED TOPOGRAPHY code (Choice # 2): **7** ENTER IDENTIFYING COMMENT: **GU** Select 1 or more characters of SNOMED TOPOGRAPHY code (Choice # 3): **&lt;Enter&gt;** Start with Date TODAY// **&lt;Enter&gt;** SEP 09, 1994
Go  to   Date TODAY// **1 1 90** (JAN 01, 1990)
Select Print Device: *[Enter Print Device Here]*

SEP 9, 1994 07:23   ISC, VERIFICATION ACCT          Pg: 1

CYTOPATHOLOGY COUNTS From JAN 1, 1990 To SEP 9, 1994

Location           Location Count        Count

-----------------------------------------------------------------------------

RESPIRATORY (2):									3						3
	NEGATIVE FOR MALIGNANT CELLS											
GU (7):												1						1

SUSPICIOUS FOR MALIGNANT CELLS										

Total specimens found:													4
				 UNSATISFACTORY SPECIMEN
				 NEGATIVE FOR MALIGNANT CELLS

SUSPICIOUS FOR MALIGNANT CELLS
				 POSITIVE FOR MALIGNANT CELLS

**NOTE:** As shown in the example above, failure to enter SNOMED codes for each category results in the sum of the % not being equal to 100%; i.e., there are four specimens and only three were coded.

**Example 2:**

Select Anat path accession reports Option: **CP** % Pos, Atyp, Dysp, Neg, Susp, &amp; Unsat cytopat

Cytology Specimens:

Use morphology list? YES// **&lt;Enter&gt;** (YES)
				 UNSATISFACTORY SPECIMEN
				 NEGATIVE FOR MALIGNANT CELLS

SUSPICIOUS FOR MALIGNANT CELLS
				 POSITIVE FOR MALIGNANT CELLS

Use topography category list? YES// **&lt;Enter&gt;** *(YES)*

51030	ORAL MUCOUS MEMBRANE

1Y010	SYNOVIAL FLUID

2Y030	SPUTUM

2Y410	BRONCHIAL MATERIAL

2Y610	PLEURAL FLUID

3X110	PERICARDIAL FLUID

6X210	ESOPHAGEAL

6X310	GASTRIC

6X940	PERITONEAL FLUID

7X100	URINE

8X210	VAGINAL

8X330	VAGINAL/CERVICAL

X1010	CSF

Start with Date TODAY// **5-1-90** (MAY 01, 1990

Go    to    Date TODAY// **5/31/90** (MAY 31, 1990)

Select Print Device: *[Enter Print Device Here]*

**NOTE:** The topography category list is generated using the Edit Pathology Report Parameters option in the Supervisor’s Menu.

JUL 31, 1990 12:51  VAMC					Pg: 1

CYTOPATHOLOGY COUNTS

From MAY 1, 1990 To MAY 31, 1990			Count

--------------------------------------------------------------------------

ORAL MUCOUS MEMBRANE (51030):				 1

NEGATIVE FOR MALIGNANT CELLS		 1	(100.0%

SYNOVIAL FLUID (1Y010):				 1

NEGATIVE FOR MALIGNANT CELLS		 1	(100.0%)

SPUTUM (2Y030):				12

UNSATISFACTORY SPECIMEN		 1	(8.3%)

NEGATIVE FOR MALIGNANT CELLS		11	(91.7%)

BRONCHIAL MATERIAL (2Y410):				10

NEGATIVE FOR MALIGNANT CELLS		 5	(50.0%)

SUSPICIOUS FOR MALIGNANT CELLS	 1	(10.0%)

POSITIVE FOR MALIGNANT CELLS		 2	(20.0%)

PLEURAL FLUID (2Y610):				 5

NEGATIVE FOR MALIGNANT CELLS		 5	(100.0%)

ESOPHAGEAL  (6X210):				 2

NEGATIVE FOR MALIGNANT CELLS		 1	(50.0%)

PERITONEAL FLUID  (6X940):				 4

NEGATIVE FOR MALIGNANT CELLS		 4	(100.0%)

URINE  (7X100):				42

NEGATIVE FOR MALIGNANT CELLS		31	(73.8%)

SUSPICIOUS FOR MALIGNANT CELLS	 5	(11.9%)

VAGINAL  (8X210):				 1

NEGATIVE FOR MALIGNANT CELLS		 1	(50.0%)

VAGINAL/CERVICAL  (8X330):				 2

NEGATIVE FOR MALIGNANT CELLS		 1	(50.0%)

CSF  (X1010):				 5

UNSATISFACTORY SPECIMEN		 1	(20.0%)

NEGATIVE FOR MALIGNANT CELLS		 4	(80.0%)

Total specimens found:				85

UNSATISFACTORY SPECIMENS		 2	( 2.4%)

NEGATIVE FOR MALIGNANT CELLS		65	(76.5%)

SUSPICIOUS FOR MALIGNANT CELLS	 6	( 7.1%)

POSITIVE FOR MALIGNANT CELLS		 2	( 2.4%)

##### Accession List with Stains [LRAPSA]

If the data is being entered through the Blocks, Stains, Procedures, Anat Path [LRAPSPDAT] option, it can be printed using this option. This summary provides a helpful tool for workload recording.

Example:

Select Anatomic path accession reports Option: **ST** Accession list with stains
Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY 

					SURGICAL PATHOLOGY STAIN LIST

Stain list date: 1994 OK ? YES// **&lt;Enter&gt;** (YES)
Start with Acc #: **20** Go  to   Acc #: LAST// **&lt;Enter&gt;** Select Print Device: [Enter Print Device Here]

SEP 9, 1994 07:31  VAMC                       Pg: 1

LABORATORY SERVICE SURGICAL PATHOLOGY BLOCKS/STAINS

-----------------------------------------------------------------------------

Acc #:   1 AUG 10, 1994 LABPATIENT3, TEN 000-00-0310

TIS

TISSUE

Paraffin Block

A      Stain/Procedure

TRICHROME STAIN          1/1   08/25/94 12:41

Paraffin Block

B      Stain/Procedure

TRICHROME STAIN          1    08/25/94 12:41

Plastic Block

C      Stain/Procedure

TRICHROME STAIN          1/1   08/25/94 12:41

Frozen Tissue

D      Stain/Procedure

TRICHROME STAIN          1/1   08/25/94 12:41

Acc #:   2 AUG 24, 1994 PILLOW,TED 459-85-9832

PROSTATE CHIPS

Paraffin Block

A      Stain/Procedure

TRICHROME STAIN          1    08/27/94 19:26

Paraffin Block

B      Stain/Procedure

TRICHROME STAIN          1    08/27/94 19:26

##### Accession Counts by Senior Pathologist [LRAPAULC]

Analysis of quality assurance information relies not only on the data for the “outlyers,” but also on the total number of cases. Cases are tallied by accession area, and are sorted by the senior pathologist assigned to the case.

Example:

Select Anatomic pathology Option: **P** Print, anat path

Select Print, anat path Options: **AR** Anat path accession reports

Select Anat path accession reports Option: **WS** Accession counts by senior pathologist

Start with Date TODAY// **1-1-90** (JAN 01, 1990)

To   Date TODAY// **9-9-93** (SEP 09, 1993)

Select Print Device: *[Enter Print Device Here]*

SEP 09, 1993 10:07    VAMC		Pg: 1

Accession counts by Senior Pathologist

From JAN 1, 1990 to:SEP 09, 1993

-----------------------------------------------------------------------------

SURGICAL PATHOLOGY

LABPATIENT4, ONE :		165

LABPATIENT4, TWO:		47

LABPATIENT4, THREE:		89

LABPATIENT4, FOUR:		72

LABPATIENT4, FIVE:		81

LABPATIENT4, SIX:		57

Unassigned accessions :     1

------

Total	512

CYTOPATHOLOGY

LABPATIENT4, SEVEN:		38

LABPATIENT4, EIGHT:		71

LABPATIENT4, NINE:		41

LABPATIENT4, TEN:		53

------

Total	203

ELECTRON MICROSCOPY

LABPATIENT5, ONE:		21

LABPATIENT5, TWO:		19

------

Total	40

AUTOPSY PATHOLOGY

LABPATIENT5, THREE :		4

LABPATIENT5, FOUR:		3

LABPATIENT5, FIVE:		3

LABPATIENT5, SIX:		7

Unassigned accessions :     5

------

Total	22

Unassigned accessions for AUTOPSY PATHOLOGY

MAY 11, 1993 15:56    Accession #: 1

JUN 20, 1993        Accession #: 5

AUG 6, 1993 12:57    Accession #: 6

AUG 6, 1993 13:03    Accession #: 7

AUG 6, 1993 13:09    Accession #: 8

#### Cum Path Data Summaries [LRAPT]

Cumulative summary of surgical path, EM, and autopsy for screen display or hard copy.

For example, please see option in the Inquiry Option section.

#### Anatomic Pathology Labels [LRAPLBL]

##### Anat Path Slide Labels [LRAPLM]

Once data has been entered through the Blocks, Stains, Procedures, Anat Path [LRAPSPDAT] option, labels can be generated for an accession, regardless of the area, which can be attached to the glass slides used for microscopic examination. If workload has been turned on for the area and the files have been appropriately setup, default data will have been entered during log-in and labels can be generated based on that with no additional data entry. See the Technical Manual for details.

The labels include five lines of data:

1)	Accession area (SURG for Surgical Pathology, CY for Cytopathology, etc.,)

2)	Accession number

3)	Block ID for Surgical Pathology and Autopsy, Preparation Technique for 	Cytopathology

4)	Stain/procedure print name

5)	Facility number from the DD global

The number of labels generated is based on the data entered. One slide label is generated for each slide of a specified stain. The format of the label is designed to allow printing of regular size print on a 1 x 1 inch label.

If workload is turned on for the accession area, these labels can be generated based on default setups without going through the Blocks, Stains, Procedures, Anat Path [LRAPSPDAT] option. The block ID, the stain and the default number of slides will be entered automatically based on the file setups for the Workload Profile. (See the Technical Manual for details.) However, if you do not go through the Blocks, Stains, Procedures, Anat Path [LRAPSPDAT] option to enter the date/time stained, you will not have any workload captured.

For autopsies, it is possible to create a set of generic labels that will be able to be printed immediately after log-in if workload is turned on. Use the Edit Pathology Report Parameters [LRAPHDR] option to enter this listing. See Example 4.

**NOTES:**

•	When data is entered through the [LRAPSPDAT] option, or automatically if the workload profiles are built, the individual slide/stain are placed in a queue to be printed. If the two prompts to reprint and to add/delete are both answered “NO,” these labels in the queue will print. At that time, the software sets a flag for those labels indicating that they have been printed.

•	If the two prompts to reprint and to add/delete are both answered “NO” and there are no labels in the queue to print, a message to that effect will be printed. This is based on the Counter field #63.8122,.07.

•	By indicating that you wish to “reprint” slide labels for the specified accession, you will reprint the labels which have previously been printed (flaggedto indicate such). Any new stains which have been entered, but which have not been printed for the first time will **not** be included in the reprint.

**Example 1:** Surgical Pathology

Select Anatomic pathology labels Option: **LM** Anat path slide labels

      SLIDE LABEL PRINT OPTION
Select AP section: **SP** SURGICAL PATHOLOGY 
Enter year: 1990// **&lt;Enter&gt;** (1990)

Reprint slide labels? NO// **&lt;Enter&gt;** (NO)

Add/Delete slide labels to print? NO// **&lt;Enter&gt;** (NO)

Start with accession number: **22** Go  to   accession number: LAST// **22** Select Print Device: [Enter Print Device Here]

SURG	SURG	SURG	SURG	SURG	SURG
90-22	90-22	90-22
A	B	B
H &amp; E	H &amp; 
R5ISC	R5ISC	R5ISC	R5ISC	R5ISC	R5ISC

**Example 2:** No Data Entered Through Blocks, Stains, Procedures [LRAPSPDAT] for the Accession (and workload not turned on)

Select Log-in menu, anat path Option: **LM** Anat path slide labels

Select ANATOMIC PATHOLOGY section: **CY** CYTOPATHOLOGY

Enter year: 1993// **&lt;Enter&gt;** (1993) 1993

Reprint slide labels ? NO// **&lt;Enter&gt;** (NO)

Add/Delete slide labels to print ? NO// **&lt;Enter&gt;** (NO)

Print CYTOPATHOLOGY slide labels for 1993

Start with accession number: **6**

Go  to  accession number: LAST// **&lt;Enter&gt;**

Select Print Device: *[Enter Print Device Here]*

There are no labels to print.

Select Anatomic pathology labels Option: **&lt;Enter&gt;**

**Example 3:** Cytology (no data entered through [LRAPSPDAT], workload profiles built). (Had label printer problems when it came to this number.)

Select ANATOMIC PATHOLOGY section: **CY** TOPATHOLOGY

Enter year: 1993// **&lt;Enter&gt;** (1993) 1993

Reprint slide labels ? NO// **Y** (YES)

Start with accession number: **5**

Go  to  accession number: LAST// **5**

Select Print Device: *[Enter Print Device Here]*

CY    	CY    	CY    	CY    	CY    	CY

93-5   	93-5   	93-5

SMEAR PRE	SMEAR PRE	CELL BLOC

PAP SMP  	PAP SMP  	H &amp; E

VAMC 578 	VAMC 578 	VAMC 578 	VAMC 578 	VAMC 578 	VAMC 578

Select Anatomic pathology labels Option: **&lt;Enter&gt;**

**Example 4:** Autopsy (no data entered through [LRAPSPDAT], workload turned on, generic list entered in the LAB SECTION file (#69.2))

Select Anatomic pathology labels Option: **LM** Anat path slide labels

Select ANATOMIC PATHOLOGY section: **AU** AUTOPSY

Enter year: 1993// **&lt;Enter&gt;** (1993) 1993

Reprint slide labels ? NO// **&lt;Enter&gt;** (NO)

Add/Delete slide labels to print ? NO// **&lt;Enter&gt;** (NO)

Print AUTOPSY slide labels for 1993

Start with accession number: **1**

Go  to  accession number: LAST// **1**

Select Print Device: *[Enter Print Device Here]*

AU    	AU    	AU    	AU    	AU    	AU

93-1   	93-1   	93-1   	93-1   	93-1   	93-1

HEART   	R LUNG  	L LUNG  	LIVER   	SPLEEN  	L KIDNEY

H &amp; E   	H &amp; E   	H &amp; E   	H &amp; E   	H &amp; E   	H &amp; E

VAMC 578 	VAMC 578 	VAMC 578 	VAMC 578 	VAMC 578 	VAMC 578

AU    	AU    	AU    	AU    	AU    	AU

93-1   	93-1   	93-1   	93-1

R KIDNEY 	L ADRENAL R ADRENAL 	PROSTATE

H &amp; E   	H &amp; E   	H &amp; E   	H &amp; E

VAMC 578 	VAMC 578 	VAMC 578 	VAMC 578 	VAMC 578 	VAMC 578

**NOTE:** Based on the following setup in [LRAPHDR]

Select GENERIC LABEL: PROSTATE// **?**

ANSWER WITH GENERIC LIST

CHOOSE FROM:

1        HEART

2        R LUNG

3        L LUNG

4        LIVER

5        SPLEEN

6        L KIDNEY

7        R KIDNEY

8        L ADRENAL

9        R ADRENAL

10        PROSTATE

YOU MAY ENTER A NEW GENERIC LIST, IF YOU WISH

ANSWER MUST BE 1-30 CHARACTERS IN LENGTH

##### Anat Path Specimen Labels [LRAPLS]

Labels can be generated for a variety of purposes. Once a series of specimens are logged into the system, a batch of labels can be printed. One label is generated for each specimen. If several specimens are submitted on a single accession, each specimen will get a separate label.

The labels print on the same label stock as the rest of the lab and contain three lines of information, including the full accession number, the patient ID information, and the specimen. The specimen text is the text entered during log-in of the accession.

Example:


```vista
Select Anatomic pathology labels Option: **LS** Anat path specimen labels
Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY 
Enter year: 1990// **PRINTER**
```

Start with accession number: **22** Go   to   accession number: LAST// 22

REMEMBER TO
			ALIGN THE PRINT HEAD ON THE FIRST LINE OF THE LABEL

				 ENTER NUMBER OF LINES FROM
			 TOP OF ONE LABEL TO ANOTHER: 7// **&lt;Enter&gt;**

Select Print Device: [Enter Print Device Here]

SURG 1120 22 Date taken:11/20/90
LABPATIENT, SEVEN		000-00-0007
PROSTATE CHIPS

##### Autopsy Slide Labels (Generic) [LRAUMLK]

This option allows the user to print slide labels for an autopsy EVEN IF no generic labels have been entered and no data has been entered through the Blocks, Stains, Procedures, Anat Path [LRAPSPDAT] option for specific blocks.

Example:

Select Laboratory DHCP Menu Option: **ANA** tomic pathology

ANATOMIC PATHOLOGY MENU

Select Anatomic pathology Option: **P** Print, anat path

Select Print, anat path Option: **LA** Anatomic pathology labels

Select Anatomic pathology labels Option: **AU** Autopsy Slide Labels (generic)

Autopsy Slide Labels

Enter year: 1993// **&lt;Enter&gt;** (1993) 1993

Enter Autopsy Case number: **1**

Want labels for whole case? YES// **&lt;Enter&gt;** (YES)

Enter total number of blocks : **20**

Want to enter additional stains :? NO// **&lt;Enter&gt;**

Select Print Device: *[Enter Print Device Here]*

AU    	AU    	AU    	AU    	AU    	AU

93-1   	93-1   	93-1   	93-1   	93-1   	93-1

1     	2     	3     	4     	5     	6

H &amp; E   	H &amp; E   	H &amp; E   	H &amp; E   	H &amp; E   	H &amp; E

VAMC578  	VAMC578  	VAMC578  	VAMC578  	VAMC578  	VAMC578

AU    	AU    	AU    	AU    	AU    	AU

93-1   	93-1   	93-1   	93-1   	93-1   	93-1

7     	8     	9     	10    	11    	12

H &amp; E  	H &amp; E   	H &amp; E   	H &amp; E   	H &amp; E   	H &amp; E

VAMC578  	VAMC578  	VAMC578  	VAMC578  	VAMC578  	VAMC578

AU    	AU    	AU    	AU    	AU    	AU

93-1   	93-1   	93-1   	93-1   	93-1   	93-1

13    	14    	15    	16    	17    	18

H &amp; E   	H &amp; E   	H &amp; E   	H &amp; E   	H &amp; E   	H &amp; E

VAMC578  	VAMC578  	VAMC578  	VAMC578  	VAMC578  	VAMC578

AU    	AU    	AU    	AU    	AU    	AU

93-1   	93-1   	93-1   	93-1   	93-1   	93-1

19    	20

H &amp; E   	H &amp; E

VAMC578  	VAMC578  	VAMC578  	VAMC578  	VAMC578  	VAMC578

#### Edit/Print/Display Preselected Lab Tests [LRUMDA]

##### Enter/Edit User Defined Lab Tests Lists [LRUMDE]

You can create patient lists, which allow you to easily monitor results of specific CH-subscript tests, using this option. These lists may be:

1. Created by the user
2. Transferred from another user **if** the user has no list(s) already defined or
3. Edited/modified by the user

Although it is possible to transfer the test list from another user, the lists are user-specific. Once the lists are created, the results may be printed using the Print/Display Preselected Lab Tests [LRUMD] option.

If no test list is created or transferred, the Print/Display Preselected Lab Tests option will print the generic list defined by the laboratory.

**Example 1:**

Select Print, Anat path Option: **LT** Edit/print/display preselected lab tests

Select Edit/print/display preselected lab tests Option: **EN** Enter/edit user defined lab test lists

You have no test lists. Instead of creating your own

would you prefer to another user's lists ? NO// **&lt;Enter&gt;** (NO)

Select LABORATORY TEST NAME: **PT PRO** THROMBIN TIME

Enter list#, order# : **1,1**

Select LABORATORY TEST NAME: **PT-CC**

Enter list#, order# : **1,2**

Select LABORATORY TEST NAME: **APTT**

Enter list#,order# : **1,3**

Select LABORATORY TEST NAME: **&lt;Enter&gt;**

Test order#:	1	2	3	4	5	6	7

-------------|--------|-------|-------|------|------|------|------|

Test list#:1 |PT	  |PT   |APTT  |

-------------|--------|-------|-------|------|------|------|------|

(E)nter/edit a test (D)elete a test list (R)emove all test lists

Enter E, D, R, or &lt;CR&gt; to accept lists: **&lt;Enter&gt;**

**Example 2:** To Print Test Lists

Select Edit/print/display preselected lab tests Option:

**EN** Enter/edit user defined lab test lists

SEP 1, 1992 19:31  VAMC                     Pg: 1

Test list for LABPROVIDER, EIGHT

Test order#:  1    2    3    4    5    6    7

-----------------|-------|-------|-------|-------|-------|-------|-------|

Test list#: 1  |HGB  |HCT  |WBC  |PLT  |WESTERG|PT   |PTT  |

-----------------|-------|-------|-------|-------|-------|-------|-------|

Test list#: 2  |PMN  |LYMPH |

-----------------|-------|-------|-------|-------|-------|-------|-------|

Test list#: 3  |GLUCOSE|BUN  |CREAT |NA   |K   |CL   |CO2  |

-----------------|-------|-------|-------|-------|-------|-------|-------|

Test list#: 4  |T. BIL |

-----------------|-------|-------|-------|-------|-------|-------|-------|

Test list#: 5  |SGOT  |

-----------------|-------|-------|-------|-------|-------|-------|-------|

Test list#: 6  |SGPT  |

-----------------|-------|-------|-------|-------|-------|-------|-------|

Test list#: 7  |ALK PHO|

-----------------|-------|-------|-------|-------|-------|-------|-------|

Test list#: 8  |ALBUMIN|

-----------------|-------|-------|-------|-------|-------|-------|-------|

Test list#: 9  |PROTEIN|

'^' TO STOP: ^

(E)nter/edit a test (D)elete a test list (R)emove all test lists

(P)rint test lists

Enter E, D, R, P or &lt;CR&gt; to accept lists: P

Select Print Device: *[Enter Print Device Here]*

SEP 1, 1992 19:31  VAMC                      Pg: 1

Test list for LABPROVIDER, EIGHT

-----------------------------------------------------------------------------

Test order#:  1    2    3    4    5    6    7

-----------------|-------|-------|-------|-------|-------|-------|-------|

Test list#: 1  |HGB  |HCT  |WBC  |PLT  |WESTERG|PT   |PTT  |

-----------------|-------|-------|-------|-------|-------|-------|-------|

Test list#: 2  |PMN  |LYMPH |

-----------------|-------|-------|-------|-------|-------|-------|-------|

Test list#: 3  |GLUCOSE|BUN  |CREAT |NA   |K   |CL   |CO2  |

-----------------|-------|-------|-------|-------|-------|-------|-------|

Test list#: 4  |T. BIL |

-----------------|-------|-------|-------|-------|-------|-------|-------|

Test list#: 5  |SGOT  |

-----------------|-------|-------|-------|-------|-------|-------|-------|

Test list#: 6  |SGPT  |

-----------------|-------|-------|-------|-------|-------|-------|-------|

Test list#: 7  |ALK PHO|

-----------------|-------|-------|-------|-------|-------|-------|-------|

Test list#: 8  |ALBUMIN|

-----------------|-------|-------|-------|-------|-------|-------|-------|

Test list#: 9  |PROTEIN|

-----------------|-------|-------|-------|-------|-------|-------|-------|

Test list#: 10  |CHOL  |

-----------------|-------|-------|-------|-------|-------|-------|-------|

Test list#: 11  |CPK  |LDH  |LDH1  |LDH 2 |LDH 3 |LDH 4 |LDH 5 |

-----------------|-------|-------|-------|-------|-------|-------|-------|

**NOTES:**

•	New prompt, “^ TO STOP” If test lists more than one screen, only one screen at a time is displayed

•	You can now print test lists.

##### Edit Print/Display Preselected Lab Tests [LRUMDA]

After you have created/defined a list, verified results may be printed for patient, controls or referrals, provided data is entered in the LABORATORY DATA file (#63). Lists of patients may be transferred to or merged with another user; however, the list of patients is user-specific. In adding or editing the patient list, you may group the patients. If patients are grouped, you can retrieve results for a specified group of patients or a single patient, instead of automatically getting results on all patients in the list. Group names can be alphabetical, numeric, or a combination.

It is possible to retrieve microbiology results using this option, by responding to the prompt appropriately. The information provided, shown in Example 3, reflects all data **except** the antibiotic sensitivities. The status of the data, i.e., Preliminary Report or Final Report, is also included.

For the CH subscript tests, no units or reference ranges are included with the data.

If you haven’t defined a test list, the system will use the default list entered by the Laboratory Information Manager (LIM).

Example 1:

Select Edit/print/display preselected lab tests Option: **P** Print/display preselected lab tests

Print/display tests for a single patient or group ? NO// **&lt;Enter&gt;** (NO)

1) LABPATIENT5, SEVEN

(R)emove a patient (A)dd/edit patients (T)ransfer list to another user

(D)elete list			(M)erge list with another user

Enter R, A, T, D, M or &lt;CR&gt; to accept list: **&lt;Enter&gt;**

Print/display microbiology results instead of defined lab tests ? NO// **&lt;Enter&gt;** (NO)

Print by (T)est list (P)atient list

Enter T or P: **P**

Print ALL test lists ? YES// **N** (N)

Enter test list number(s): **6**

Start with Date TODAY// **5.30.93** (MAY 30, 1993)

Go  to   Date TODAY// **1.13.92** (JAN 13, 1993)

Select Print Device: *[Enter Print Device Here]*

APR 18, 1994 08:32 VAMC		Pg:1

List for: LABPROVIDER3, TEN

----------------------------------------------------------------------------

000-00-0008    LOC:1 TEST        Patient: LABPATIENT1, THREE

NA    K   CL

05/25/93 09:19       140    8H*   2L*

05/24/93 16:18       canc

05/24/93 16:17       123L

10/16/92 23:57       140   4.5   104L*

09/30/92 13:40       140   4.3   102L*

09/23/92 11:55               100L*

08/07/92 13:47               75L*

04/16/92 17:28       140   4.3   100

04/16/92 16:53       140   4.5   97L

04/16/92 16:53       140   4.2   103

04/16/92 16:52       140    4   97L

04/16/92 16:25       140   3.2L   98L

04/07/92 11:19       145   canc

02/13/92 14:30       135   4.3   103

----------------------------------------------------------------------------

**Example 2:** Retrieval of Chemistry Results for a Group of Patients (by patient)

Select Edit/print/display preselected lab tests Option: **P** Print/display lab tests for selected patients

Print/display tests for a single patient or group ? NO// **Y** (YES)

1. Single patient

2. Group of patients

3. Patients for a ward

4. Patients for a clinic

Select 1,2,3 or 4: **1** . 1

Print/display microbiology results instead of defined lab tests ? NO// **&lt;Enter&gt;** (NO)

Print by (T)est list (P)atient list

Enter T or P: **P**

Print ALL test lists ? YES// **N** (NO)

Enter test list number(s): **1,2,4**

Start with Date TODAY// **11/18/88** (NOV 18, 1988)

Go  to   Date TODAY// **11/30/88** (NOV 30, 1988)

Select Print Device: *[Enter Print Device Here]*

SEP 28, 1989 08:38 VAMC				Pg:1

List for: LABPROVIDER3, TEN				PT GRP:1

-----------------------------------------------------------------------------

SSN:000-00-0800 	LOC:RENAL CONSULT     Patient: LABPATIENT5, EIGHT

=============================================================================

SSN: 000-00-0802	LOC:11W		 Patient: LABPATIENT5, NINE

CREAT	CREA-C	BUN	BUN-CC	BLD

11/30	04:00		1.8

11/28	12:49		1.8

11/28	11:56		1.8

11/23	15:30	URINE							3+

11/23	04:04		1.8				32

-----------------------------------------------------------------------------

HAPTO FREEHGB	C3	C4	CPK	LD

11/30	04:00						1084

11/30	04:00		2.9

11/30	04:00		339			117	 984

**Example 3:** Retrieval of Microbiology Results

Select Edit/print/display preselected lab tests Option: **PR** Print/display preselected lab tests

Print/display tests for a single patient or group ? NO// **&lt;Enter&gt;** (NO)

1) LABPATIENT5, TEN          (2) LABPATIENT1, FOUR

(R)emove a patient (A)dd/edit patients    (T)ransfer list to another user

(D)elete list   (P)atient group deletion (M)erge  list with another user

(S)end list to printer

Enter R, A, T, D, P, M, S or &lt;CR&gt; to accept list: **&lt;Enter&gt;**

Print/display microbiology results (excluding antibiotics)

instead of defined lab tests? NO// **Y** (YES)

Start with Date TODAY// **&lt;Enter&gt;** SEP 8, 1994

Go  to  Date TODAY// 5 20 94 (MAY 20, 1994)

New page for each patient ? NO// **&lt;Enter&gt;** (YES)

Select Print Device: [Enter Print Device Here]

SEP 8, 1994 10:49  VAMC                        Pg: 1

List for: LABPROVIDER2, FOUR

-----------------------------------------------------------------------------

SSN: 000-00-0800  LOC:2 EAST        Patient: LABPATIENT5, TEN

Date     Site/specimen         Collection sample Accession number

05/20/94 14:38 NASAL BONE          SWAB       MICRO 93 6

Tests: PARASITE EXAM

PARASITE RPT DATE:MAY 20, 1994       FINAL REPORT

-----------------------------------------------------------------------------

=============================================================================

**Example 4:** To Print a User’s Patient List (new functionality)

Print/display tests for a single patient or group ? NO// **&lt;Enter&gt;** (NO)

1) PATIENT,FIRST        (HEM)  2) PATIENT,SECOND (ONC)

(R)emove a patient (A)dd/edit patients (T)ransfer list to another user

(D)elete list   (P)atient group deletion (M)erge  list with another user

(S)end list to printer

Enter R, A, T, D, P, M, S or &lt;Enter&gt; to accept list: **S**

Select Print Device: *[Enter Print Device Here]*

SEP 8, 1994 11:02  VAMC                       Pg: 1

Patient list for: LABPROVIDER2, FOUR

----------------------------------------------------------------------------

1) LABPATIENT5, TEN.       (2) LABPATIENT1, FOUR

#### Print Log Book [LRAPBK]

For a description and example of this option, see Log-In Option section.

#### Print Final Path Reports by Accession Number [LRAPFICH]

Use this option to print final path reports from one accession to another within the same calendar year.

This option can be used to make tapes for microfiche (See Microfiche of Path Reports).

Select Print, anat path Option: **PA** Print final path reports by accession #

Select ANATOMIC PATHOLOGY SECTION: **SP** SURGICAL PATHOLOGY

Select Accession YEAR: **1990** ( 1990)

Start with accession #: **3**

Go   to accession #: **3**

Select Print Device: *[Enter Print Device Here]*

-----------------------------------------------------------------------------

MEDICAL RECORD |          SURGICAL PATHOLOGY        Pg 1

-----------------------------------------------------------------------------

Submitted by: LABPROVIDER, ONE         Date obtained: MAR 16, 1990

-----------------------------------------------------------------------------

Specimen (Received MAR 16, 1990 15:55):

BONE MARROW

-----------------------------------------------------------------------------

Brief Clinical History:

-----------------------------------------------------------------------------

Preoperative Diagnosis:

-----------------------------------------------------------------------------

Operative Findings:

-----------------------------------------------------------------------------

Postoperative Diagnosis:

Surgeon/physician: LABPROVIDER, ONE

=============================================================================

PATHOLOGY REPORT

Laboratory: SLC                   Accession No. SP90 3

-----------------------------------------------------------------------------

Gross description:

-----------------------------------------------------------------------------

(See next page)

LABPROVIDER4, ONE                  vtn| Date MAR 19, 1990

-----------------------------------------------------------------------------

LABPATIENT6, ONE                SURGICAL PATHOLOGY Report

ID:000-00-0061  SEX:M DOB:5/22/86 AGE:4 LOC:PHRENOLOGY

LABPROVIDER, ONE

-----------------------------------------------------------------------------

MEDICAL RECORD |          SURGICAL PATHOLOGY        Pg 2

-----------------------------------------------------------------------------

PATHOLOGY REPORT

Laboratory: SLC                   Accession No. SP90 3

-----------------------------------------------------------------------------

Several spicules of bone are received as well as 10 unstained slides

with material on them.

Microscopic exam/diagnosis:

-----------------------------------------------------------------------------

(See next page)

LABPROVIDER4, ONE                  vtn| Date MAR 19, 1990

-----------------------------------------------------------------------------

LABPATIENT6, ONE                  SURGICAL PATHOLOGY Report

ID: 000-00-0800 SEX: M DOB:5/22/86 AGE:4 LOC:PHRENOLOGY

LABPROVIDER, ONE

-----------------------------------------------------------------------------

MEDICAL RECORD |          SURGICAL PATHOLOGY        Pg 3

-----------------------------------------------------------------------------

PATHOLOGY REPORT

Laboratory: SLC                   Accession No. SP90 3

-----------------------------------------------------------------------------

CELLULARITY: HYPER CELLULAR

M:E RATIO: 1.5:1

DESCRIPTION: There is megaloblastoid rubroid and myeloid

proliferation.

-----------------------------------------------------------------------------

(See next page)

LABPROVIDER4, ONE                  vtn| Date MAR 19, 1990

-----------------------------------------------------------------------------

LABPATIENT6, ONE                   SURGICAL PATHOLOGY Report

ID: 000-00-0800 SEX:M DOB:5/22/86 AGE:4 LOC:PHRENOLOGY

LABPROVIDER, ONE

-----------------------------------------------------------------------------

MEDICAL RECORD |          SURGICAL PATHOLOGY        Pg 4

-----------------------------------------------------------------------------

PATHOLOGY REPORT

Laboratory: SLC                   Accession No. SP90 3

-----------------------------------------------------------------------------

DIAGNOSIS: BONE MARROW EXAMINATION:

MEGALOBLASTIC BONE MARROW

COMMENT: Suggest B12 and folate studies.

-----------------------------------------------------------------------------

(See next page)

LABPROVIDER4, ONE                  vtn| Date MAR 19, 1990

-----------------------------------------------------------------------------

LABPATIENT6, ONE                    SURGICAL PATHOLOGY Report

ID: 000-00-0800 SEX:M DOB:5/22/86 AGE:4 LOC:PHRENOLOGY

LABPROVIDER, ONE

-----------------------------------------------------------------------------

MEDICAL RECORD |          SURGICAL PATHOLOGY        Pg 5

-----------------------------------------------------------------------------

PATHOLOGY REPORT

Laboratory: SLC                   Accession No. SP90 3

-----------------------------------------------------------------------------

RESIDENT:

SNOMED code(s):

T-06000: bone marrow

M-75950: megaloblastic erythropoiesis

-----------------------------------------------------------------------------

(End of report)

LABPROVIDER4, ONE                  vtn| Date MAR 19, 1990

-----------------------------------------------------------------------------

LABPATIENT6, ONE                    SURGICAL PATHOLOGY Report

ID: 000-00-0800 SEX:M DOB:5/22/86 AGE:4 LOC:PHRENOLOGY

LABPROVIDER, ONE

### SNOMED Field References [LRAPREF]

#### Descriptions

**Option	Description**

Enter/Edit SNOMED file References	Allows entry or edit of file references that may be printed on patients’ records or used for reference reading.

Topography (SNOMED) Reference

Morphology (SNOMED) Reference

Etiology (SNOMED) Reference

Disease (SNOMED) Reference

Function (SNOMED) Reference

Procedure (SNOMED) Reference

Occupation (SNOMED) Reference

Medical Journal file Edit	Allows entry or editing of medical journals that can be listed in file references on patients’ records.

Print References for a SNOMED Entry	Allows printing of medical journal references for a SNOMED file entry.

Topography (SNOMED) Reference Print

Morphology (SNOMED) Reference Print

Etiology (SNOMED) Reference Print

Disease (SNOMED) Reference Print

Function (SNOMED) Reference Print

Procedure (SNOMED) Reference Print

Occupation (SNOMED) Reference Print

#### Enter/Edit SNOMED File References [LRAPSRE]

This option allows entry or edit of file references that may be printed on patients’ records or used for reference reading. As shown below, the references may be restricted by topography and may be turned ON/OFF depending on the entry in the field List on Patient Record. This example is for the Morphology field. The other fields work the same way.

Example:

Select Anatomic pathology Option: **R** SNOMED field references
Select SNOMED field references Option: **?** ER	Enter/edit SNOMED file references
	MJ	Medical journal file edit
	PR	Print references for a SNOMED entry

Select SNOMED field references Option: **PR** Print references for a SNOMED entry

Select Enter/edit SNOMED file references Option: **?** TO	Topography (SNOMED) reference
	MO	Morphology (SNOMED) reference
	ET	Etiology (SNOMED) reference
	DI	Disease (SNOMED) reference
	FU	Function (SNOMED) reference
	PR	Procedure (SNOMED) reference
	OC	Occupation (SNOMED) reference

Select Enter/edit SNOMED file references Option: **M** Morphology (SNOMED) reference

Select MORPHOLOGY FIELD NAME: **WDA** (SNOMED) reference ADENOCARCINOMA, WELL DIFFERENTIATED 		814031
Select TITLE OF ARTICLE: **Well-differentiated adenocarcinoma of the prostate** AUTHOR(S): **Kern WH** (SNOMED) reference
	MEDICAL JOURNAL: **CANCER** VOLUME: **41** STARTING PAGE: **2046** DATE: **1978** (1978)
	LIST ON PATIENT RECORD: **YES** Select TOPOGRAPHY RESTRICTION: **77** Select TOPOGRAPHY RESTRICTION: **&lt;Enter&gt;** Select TITLE OF ARTICLE: **&lt;Enter&gt;** Select MORPHOLOGY FIELD NAME: &lt;Enter&gt;

**NOTE:** The pathology report below, shows how the journal reference is included since the field List on Patient Record was set to “YES” and the condition for the topography restriction (i.e., prostate (77)) was met.

-----------------------------------------------------------------------------
	MEDICAL RECORD :				SURGICAL PATHOLOGY		Pg 1
-----------------------------------------------------------------------------
Submitted by: LABPROVIDER, SEVEN			Date obtained: NOV 20, 1990
-----------------------------------------------------------------------------
Specimen:
PROSTATE CHIPS
-----------------------------------------------------------------------------
Brief Clinical History:
	Nocturia and difficulty voiding urine.
-----------------------------------------------------------------------------
Preoperative Diagnosis:
	Enlarged prostate.
-----------------------------------------------------------------------------
Operative Findings:
	Same.
-----------------------------------------------------------------------------
Postoperative Diagnosis:
	Same.
				Surgeon/physician: LABPROVIDER, SEVEN
=============================================================================
			   PATHOLOGY REPORT
Laboratory: R5ISC						Accession No. SP88 22
-----------------------------------------------------------------------------
Gross description:		Pathology Resident: LABPROVIDER4, TWO
	Specimen consists of 25 grams of prostate gland tissue.

Microscopic exam/diagnosis:

						*** MODIFIED REPORT ***
(Last modified: NOV 21, 1990 09:01 typed by GINS, DONALD)
Prostate gland tissue showing glandular and stromal hyperplasia. In one chip of 134 there is a small focus of well differentiated adenocarcinoma.
Also present are small prostatic infarcts and foci of squamous metaplasia.

Reference:
Well-differentiated adenocarcinoma of the prostate
Kern WH
CANCER vol.41 pg. 2046 Date: 1978
-----------------------------------------------------------------------------
									(End of report)
Pathologist: LABPROVIDER, THREE				dg : Date NOV 21, 1990
-----------------------------------------------------------------------------
LABPATIENT, SEVEN				   SURGICAL PATHOLOGY Report
ID:000-00-0007  SEX:M DOB:5/8/16 AGE:74 LOC: 1A
						LABPROVIDER, SEVEN

#### Medical Journal File Edit [LRAPLIB]

This option allows entry or editing of medical journals that can be listed in file references on patients’ records.

Example:

Select JOURNAL: **JAMA**

JOURNAL ABBREVIATION: JAMA// **&lt;Enter&gt;**

FULL NAME: **JOURNAL OF THE AMERICAN MEDICAL ASSOCIATION**

CITY OF : // **&lt;Enter&gt;**

NLM CALL NUMBER: **J11248**

NLM TITLE CONTROL NUMBER: **12398767**

COMMENT:

1&gt; **&lt;Enter&gt;**

#### Print References for a SNOMED Entry [LRAPSRP]

This option allows SNOMED file references to be printed on patients’ records or used for reference reading. The example below describes how to request a printout for the Morphology field. The option works essentially the same for the other SNOMED fields.

Example:

Select Anatomic pathology Option: **R** SNOMED field references

Select SNOMED field references Option: **?** ER	Enter/edit SNOMED file references
	MJ	Medical journal file edit
	PR	Print references for a SNOMED entry
 
Select SNOMED field references Option: **PR** Print references for a SNOMED entry 
Select Print references for a SNOMED entry Option: **?** TO	Topography (SNOMED) reference print
	MO	Morphology (SNOMED) reference print
	ET	Etiology (SNOMED) reference print
	DI	Disease (SNOMED) reference print
	FU	Function (SNOMED) reference print
	PR	Procedure (SNOMED) reference print
	OC	Occupation (SNOMED) reference print

Select Print references for a SNOMED entry Option: **M** Morphology (SNOMED) reference

Select MORPHOLOGY FIELD NAME: **WDA** (SNOMED) reference ADENOCARCINOMA, WELL DIFFERENTIATED 		814031
Select Print Device: *[Enter Print Device Here]*

NAME: ADENOCARCINOMA, WELL DIFFERENTIATED

SNOMED CODE: 814031		ABBREVIATION: WDA

TITLE OF ARTICLE:Well-differentiated adenocarcinoma of the prostate 
	AUTHOR(S): Kern WH 		MEDICAL JOURNAL: CANCER
	VOLUME: 41			STARTING PAGE: 2046 
	DATE: 1978 			LIST ON PATIENT RECORD: YES
	TOPOGRAPHY RESTRICTION: 77

### Supervisor, Anat Path [LRAPSUPER]

#### Descriptions

**Option	Description**

Delete Anat Path Descriptions by Date	Deletes gross description, microscopic/ diagnosis text, specimen, comments, and record of modifications since release of report.

Enter/Edit Lab Description File	The specimen description for an entry in this file will be entered as the gross description for an accession if the SPECIMEN name entered at log-in time exactly matches the LAB DESCRIPTION NAME. The specimen description for an entry in this file will be entered as the microscopic description for an accession if an “ ***** ” precedes the exact match in the LAB DESCRIPTION file when an entry is made at the microscopic description prompt.

Edit Pathology Parameters	Allows editing of path report headers

(New name for this option)	for anatomic pathology; can specify upper or lower-case printing of SNOMED &amp; ICD-CM codes.

**OLD NAME was Edit Pathology Report Parameters.**

Enter/Edit Items in a SNOMED field	Enter or edit entries in one or more SNOMED fields. You must have the LRAPSUPER key to use this option.

Topography (SNOMED) enter/edit

Morphology (SNOMED) enter/edit

Etiology (SNOMED) enter/edit

Disease (SNOMED) enter/edit

Function (SNOMED) enter/edit

Procedure (SNOMED) enter/edit

Occupation (SNOMED) enter/edit

**Option	Description**

Incomplete Reports, Anat Path	Use this option to print a list of the

(New name for this option)	Incomplete Anatomic Pathology section reports.

Print Pathology Modifications	Prints a report with all copies of microscopic/diagnosis changes made to the report since the report was released (verified). Contains both the original and modified data.

Anatomic Pathology Topography Counts	Prints counts of organ/tissues (SNOMED topography) specified by code, from one date to another; shows # of patients, accessions, and organ/tissues for the time specified. If more than one topography is requested, there will be a count and percentage of the total organ/tissues within the time period for each topography.

Delete Free Text Specimen Entries	Allows deletion of free text specimen entries for surgical path, cytopath and electron microscopy for a time selected. Workload data associated with the specimens will also be deleted.

Missing AP Alert Search	Searches for missing alerts on verified cases as well as incorrectly set fields on the order. Sends an alert and MailMan message to the user running the option as well as the “LMI” mail group after completion.

**AP Quality Assurance Reports**

QA Codes Entry/Edit	Edit the QA code with this option. This will allow access to that specific field once the report has been released, without placing the report into a print queue or classifying the report as “modified.”

**NOTE:** This data is not included in any display or print option other than Tissue Committee review cases.

**Option	Description**

AP Consultation Searches and Reports	Internal and external consultations may be entered for individual anatomic pathology accessions using procedure codes from the SNOMED manuals.

Cum Path Summaries for 	The process of reviewing the

Quality Assurance	diagnoses for correlation is greatly simplified by compiling a consolidated report of the cum path data summaries for all patients having specimens accessioned for a specified accession area.

% Pos, Atyp, Dysp, Neg, Susp, Unsat	Prints the number and % of positive,

Cytopath	negative, and suspicious specimens for malignancy and unsatisfactory specimens from one date to another.

Delete TC and QA Codes	Allows deletion of all tissue committee and quality assurance codes for an anatomic pathology section for a specified time.

**Option	Description**

Frozen Section, Surgical Path	Allows searches on a regular basis to

Correlation	identify cases for review, to determine

correlation between frozen section and permanent section diagnoses, if documentation of physician diagnoses are appropriate, and if a second pathologist agrees with the original diagnosis.

Print Path Micro Modifications	Prints path reports that have modified microscopic descriptions from one date to another.

Malignancy Review	Simplifies and expedites the review process for all malignancy cases that required review by a second pathologist. Generates a report that includes an alphabetical listing by patient, listing by accession number, and calculations. Also useful for quality assurance studies by other clinical services.

QA Outcome Review Cases	Provides a list of cases that have been reviewed for JCAHO.

10% Random Case Review, Surg Path	Searches the topographies entered for the time specified, then randomly selects 10% of the cases for each topography, to be included on the report required for Quality Assurance. The report generated includes a summary of the topography counts, a listing of the cases identified, and copy of the final report for each accession identified.

**Option	Description**

Edit QA Site Parameters	Allows the TC code prompt to appear when the pathologist enters the final diagnosis, thus enabling cases to be selected later using the Tissue Committee Review Cases option.

Tissue Committee Review Cases	Produces a listing of cases by TC code (if set in the Edit QA Site Parameters option), followed by statistical information on the number of accessions, and number and percentage for each code. Additional information is then provided for each case on the list, including an expanded version of the “Cum path data summary” with admitting/discharge information and ICD-CM codes, and the final report for the accession number listed.

**NOTE: With the implementation of LR*5.2*442, a report may contain up to twenty-five each ICD-10 diagnosis or procedure codes for a given patient record.**

Anatomic Pathology Turnaround Time	Provides the number of days cases submitted to pathology were in the lab before being signed out.

Move Anatomic Path Accession	If it is necessary to transfer data associated with a specific surgical pathology accession from one file to another, this option is used.

**AFIP Registries** List of AFIP registries

Persian Gulf Veterans	List of veterans who served in the  with pathology specimens.

Prisoner of War Veterans	List of prisoners of war veterans that have anatomic pathology specimens for the time specified.

Edit Referral Patient File	Edit referral patient file fields.

#### Delete Anat Path Descriptions by Date [LRAPDAR]

Use this option to delete the word-processing fields for the gross description, the frozen section, the microscopic description, any modifications in the microscopic diagnosis and the specimen log-in comments. The capability to exclude purging of the microscopic description field and/or the frozen section description field exists.

This option does **not** delete the data associated with the specimen that is related to the blocks, stains, and procedures. This is accomplished using the Delete Free Text Specimen Entries [LRAPDFS] option.

All personnel involved with each of the areas should be notified in advance of purging, to ensure that all necessary hard copies have been printed for future reference. It is also desirable to print both the list of incomplete reports and unverified reports, using the Incomplete Reports, Anat Path [LRAPINC] and the List of Unverified Path Reports [LRAPV] options. This will allow necessary follow up and resolution before purging.

**NOTE:** The length of time which the full text should be left on the system before these fields are deleted is to be determined by the site based on storage capabilities and frequency of access to the data.

Example:

Select Supervisor, anat path Option **: DD** Delete anat path descriptions by date

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

Remove descriptions from SURGICAL PATHOLOGY File

Start with Date TODAY// **1-1-91** (JAN 01, 1991)

Go  to  Date TODAY// **12-31-91** (DEC 31, 1991)

OK to DELETE DESCRIPTIONS (clinical,pathological)

from one date through the other ? NO// **Y** (YES)

OK to delete Microscopic Description/Diagnosis entries ? NO// **&lt;Enter&gt;** (NO)

OK to delete Frozen Section Description entries ? NO// **&lt;Enter&gt;** (NO)

...........

OK DONE !

#### Enter/Edit Lab Description File [LRAPDES]

Using the LAB DESCRIPTIONS file; (#62.5), it is possible to copy generic gross and microscopic descriptions into both the Gross Description field (#63.08,1 for Surgical Pathology, #63.09,1 for Cytopathology, and #63.08,1 for Electron Microscopy) and the Microscopic Description field (#63.08,1.1 for Surgical Pathology, #63.09,1.1 for Cytopathology and #63.02,1.1 for Electron Microscopy) for subsequent editing. The description which is pulled will be the only data which appears in the field. These will not appear until the user leaves the accession. Thus, if editing is to be done, the user must return to the accession. QA codes in the LAB DESCRIPTIONS file must have the AP General (I) screen.

**Example 1:** Entry of a Specimen Description

Select Supervisor, anat path option: **ED** Enter/edit lab description file

Select LAB DESCRIPTIONS NAME: **PROSTATE CHIPS** PROSTATE GLAND TISSUE
NAME: PROSTATE CHIPS// **&lt;Enter&gt;** EXPANSION: PROSTATE GLAND TISSUE Replace **&lt;Enter&gt;** SCREEN: AP SURG// **&lt;Enter&gt;** SPECIMEN DESCRIPTION: 
	1&gt; **Specimen consists of * grams of prostate gland tissue.** EDIT Option: **&lt;Enter&gt;** Select LAB DESCRIPTIONS NAME: &lt;Enter&gt;

**NOTES:**

•	At the “SPECIMEN DESCRIPTION” prompt, enter the text that you wish to be copied. Use some symbol such as “*” or “/” at those places in the test where edits will routinely be made, such as those to enter measurements.

•	Specimen description for an entry in this file will be entered as the gross description for an accession if the Specimen name entered at log-in time exactly matches the Lab Description Name. The specimen description for an entry in this file will be entered as the microscopic description for an accession if a “*” precedes the exact match in the LAB DESCRIPTION file #(62.5) when entering data at the microscopic description prompt.

•	If you can’t get all of the pathologists to agree on a single description, you can enter a description name, a character and the initials of the pathologist. When logging in the specimens, the person doing the entry can then enter the specimen name, exact character and the initials of the pathologist doing gross descriptions that day, and the correct description will be selected. For example, PROSTATE-DG and PROSTATE-CR could reflect two slightly different versions preferred by two pathologists. The same process can also work for the microscopic descriptions.

Example 2:	Entry of an Autopsy QA Code

Select Supervisor, anat path Option: **ED** Enter/edit lab description file

Select LAB DESCRIPTIONS NAME: A1

Are you adding A1 as a new LAB DESCRIPTION? **YES**

NAME: A1// **&lt;Enter&gt;**

EXPANSION: **AU PRE/POSTMORTEM CORRELATION - Diagnosis confirmed/verified**

SCREEN: **AP** GENERAL

SPECIMEN DESCRIPTION:

1&gt; **&lt;Enter&gt;**

Select LAB DESCRIPTIONS NAME: **&lt;Enter&gt;**

**Example 3:** Enter a Template to use the Bethesda System Description.

Select Anatomic pathology Option: **S** Supervisor, anat path

Select Supervisor, anat path Option: **ED** Enter/edit lab description file

Select LAB DESCRIPTIONS NAME:

ARE YOU ADDING '' AS A NEW LAB DESCRIPTIONS? **Y** (YES)

LAB DESCRIPTIONS EXPANSION:  SYSTEM FOR REPORTING CERVICAL/VAGINAL

LAB DESCRIPTIONS SCREEN: **C** AP CYTO

SPECIMEN DESCRIPTION:

1&gt; **Statement on Specimen Adequacy**

2&gt; **( ) Satisfactory for interpretation**

3&gt; **( ) Less than optimal**

4&gt; **( ) Unsatisfactory**

5&gt; **&lt;Enter&gt;**

6&gt; **Explanation for less than optimal/unsatisfactory specimen:**

7&gt; **( ) Scant cellularity**

8&gt; **( ) Poor fixation or preservation**

9&gt; **( ) etc.**

10&gt; **&lt;Enter&gt;**

EDIT Option: **&lt;Enter&gt;**

Select LAB DESCRIPTIONS NAME: **&lt;Enter&gt;**

#### Edit Pathology Parameters [LRAPHDR]

This option provides significant site flexibility in configuring the various pathology report.

1. Specific headers are entered for each of the areas within Anatomic Pathology. For Surgical Pathology, REPORT HEADER 1 appears above the gross description, REPORT HEADER 2 appears above the microscopic description and REPORT HEADER 3 appears above the frozen section diagnosis if there is an entry in the frozen section field for that accession and REPORT HEADER 4 appears above the diagnosis if there is an entry in the diagnosis field for that accession. See Example 1.

1. By using the SNOMED &amp; QA Coding field, it is possible to include information at the end of the preliminary reports. In Example #1 below, the field is used to provide a standardized mechanism for the pathologist to enter relevant comments and codes when dictating the microscopic description.

1. By using the Topography Category field, it is possible to standardize a list of topographies used in other options. See Example 2.

1. By using the Select Slide Label field (under Cytology) it is possible to select what will appear on the label. See Example 2.

1. By using the Morphology Entry field, it is possible to control the specific codes to be included in the report, % Pos, Atyp, Dysp, Neg, Susp, &amp; Unsat Cytopath specimens [LRAPCYPCT]. See Example 3.

1. By answering yes to the New Pg for Supplementary Rpt. field, it is possible to cause the Supplementary Report to print on a new page. This field is also available for Autopsy cases. See Example 5.

Printing the gross description in double-spacing for the pathologist to review/edit when he is dictating the microscopic descriptions is helpful. This can be done by entering “double” for the “Gross Description Spacing” prompt. The final report is not affected by this entry it will remain single-spaced.

**Example 1:** Surgical Pathology

**NOTE:** At the “SNOMED &amp; QA CODING:” prompt, enter free text word processing. Anything entered in this field will appear at the end of the preliminary report. This is specific for each type of report.

Select Supervisor, anat path Option: **ER** Edit pathology parameters

Select LAB SECTION PRINT NAME: **SP** SURGICAL PATHOLOGY
REPORT HEADER 1: Gross description:// ?

ANSWER MUST BE 1-50 CHARACTERS IN LENGTH

Enter the heading you want displayed when path report is printed.
REPORT HEADER 1: Gross description:// **&lt;Enter&gt;** REPORT HEADER 2: Microscopic exam: Replace **&lt;Enter&gt;**

REPORT HEADER 3: Frozen section diagnosis:// **&lt;Enter&gt;**

REPORT HEADER 4: Diagnosis:// **&lt;Enter&gt;** PRINT SNOMED/ICD CODES: LOWER CASE// **&lt;Enter&gt;** GROSS DESCRIPTION SPACING: DOUBLE// **&lt;Enter&gt;** LINES IN A LABEL: 7// **&lt;Enter&gt;** ACCESSION PREFIX: SP// **&lt;Enter&gt;** PRINT SF-515 LINES: YES// **&lt;Enter&gt;**

NEW PG FOR SUPPLEMENTARY RPT: YES// **NO** *[New]*

ASK TC CODES: YES// **&lt;Enter&gt;**

SNOMED &amp; QA CODING:

1)***************************************************************************

2)***************************************************************************

3) **&lt;SPACE&gt;&lt;Enter&gt;**

4) **PLEASE CIRCLE ALL APPROPRIATE CODES &amp; INDICATE A TOPOGRAPHY &amp; MORPHOLOGY:**

5) **&lt;Enter&gt;**

6) **QA CODE:	0	Inadequate clinical information**

7) **1	Pathology as expected**

9) **2	Disease tissue, expected pathology NOT found**

10) **3	 tissue, disease expected**

11) **4	Unexpected tissue for procedure**

12) **6	Tissue is absent, but expected**

13) **7	Insufficient tissue**

14) **8	Foreign bodies**

15) **&lt;SPACE&gt;&lt;Enter&gt;&lt;Enter&gt;**

16) **SNOMED CODES: 	Topography:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

17) **Morphology:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

18) **Etiology:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

19) **Procedure:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

20) **Common procedures:**

21) **3082	Frozen section(FS)	1149	Fine needle aspiration (FNA)**

22) **1140	Biopsy, NOS	1142	Biopsy, open (OP)**

23) **1141	Biopsy, excisional	1143	Biopsy, needle (NB)**

24) **1100	Excision (resection)	3219	Frozen tissue storage**

25) **3205	Tissue Processing,RUSH**

26) **&lt;SPACE&gt;&lt;Enter&gt;**

27) **0654001	AFIP consultation	0654004 Internal (intradepartmental)**

28) **&lt;SPACE&gt;&lt;Enter&gt;**

29) **0656	Outside case, slides returned**

EDIT Option: **&lt;Enter&gt;**

#### [Edit pathology parameters (Example 1 cont’d)]

Select TOPOGRAPHY CATEGORY: **&lt;Enter&gt;**

Select MORPHOLOGY ENTRY: **&lt;Enter&gt;**

ASK FROZEN SECTION: YES// **&lt;Enter&gt;**

ASK SURG PATH DIAGNOSIS: YES// **&lt;Enter&gt;**

**Example 2:** Cytopathology

Select Supervisor, anat path Option: **ER** Edit pathology parameters

Select LAB SECTION PRINT NAME: **CY** CYTOPATHOLOGY

REPORT HEADER 1: Gross Description// **&lt;Enter&gt;**

REPORT HEADER 2: Microscopic description Replace **&lt;Enter&gt;**

REPORT HEADER 3: **&lt;Enter&gt;**

REPORT HEADER 4: Diagnosis:// **&lt;Enter&gt;**

Select SLIDE LABEL: SMEAR PREP// **?**

ANSWER WITH SLIDE LABEL

CHOOSE FROM:

CELL BLOCK

CYTOSPIN

MEMBRANE FILTER

PREPARED SLIDES

SMEAR PREP

YOU MAY ENTER A NEW SLIDE LABEL, IF YOU WISH

Answer must be 1-30 characters in length.

Select SLIDE LABEL: SMEAR PREP// **&lt;Enter&gt;**

SLIDE LABEL: SMEAR PREP// **&lt;Enter&gt;**

PRINT NAME: SMEAR// **?**

Answer must be 1-9 characters in length.

PRINT NAME: SMEAR// **&lt;Enter&gt;**

Select SLIDE LABEL: **&lt;Enter&gt;**

PRINT SNOMED/ICD CODES: LOWER CASE// **&lt;Enter&gt;**

GROSS DESCRIPTION SPACING: SINGLE// **&lt;Enter&gt;**

LINES IN A LABEL: 7// **&lt;Enter&gt;**

ACCESSION PREFIX: CY// **&lt;Enter&gt;**

PRINT SF-515 LINES: YES// **&lt;Enter&gt;**

NEW PG FOR SUPPLEMENTARY RPT: YES// **&lt;Enter&gt;**

ASK TC CODES: YES// **&lt;Enter&gt;**

SNOMED &amp; TC CODING: **&lt;Enter&gt;**

13) **09010	Unsatisfactory Specimen**

14) **&lt;Enter&gt;**

15) **Also:	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

16) **\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

17) **&lt;Enter&gt;**

18) **Common procedures:	1149	Fine needle aspiration (FNA)**

19) **1143	Biopsy, needle (NB)**

20) **0654004 Internal consultation (intradepartmental)**

21) **0654001 AFIP consultation**

EDIT Option: **&lt;Enter&gt;**

Select TOPOGRAPHY CATEGORY: **?**

ANSWER WITH TOPOGRAPHY CATEGORY

CHOOSE FROM:

YOU MAY ENTER A NEW TOPOGRAPHY CATEGORY, IF YOU WISH

Answer must be 1-7 characters in length and contain only digits, and

the letters 'X' and/or 'Y'.

One character enter -&gt; most general

*[Edit pathology parameters (Example 2 cont’d)]*

All characters entered -&gt; most specific

Select TOPOGRAPHY CATEGORY: **51030**

COMMENT: ORAL MUCOUS MEMBRANE// **&lt;Enter&gt;**

Select TOPOGRAPHY CATEGORY: **1Y010**

TOPOGRAPHY CATEGORY COMMENT: **SYNOVIAL FLUID**

COMMENT: SYNOVIAL FLUID// **&lt;Enter&gt;**

Select TOPOGRAPHY CATEGORY: **2Y030**

TOPOGRAPHY CATEGORY COMMENT: **SPUTUM**

COMMENT: SPUTUM// **&lt;Enter&gt;**

Select TOPOGRAPHY CATEGORY: **2Y410**

TOPOGRAPHY CATEGORY COMMENT: **BRONCHIAL MATERIAL**

COMMENT: BRONCHIAL MATERIAL// **&lt;Enter&gt;**

Select TOPOGRAPHY CATEGORY: **2Y610**

TOPOGRAPHY CATEGORY COMMENT: **PLEURAL FLUID**

COMMENT: PLEURAL FLUID// **&lt;Enter&gt;**

Select TOPOGRAPHY CATEGORY: **3X110**

TOPOGRAPHY CATEGORY COMMENT: **PERICARDIAL FLUID**

COMMENT: PERICARDIAL FLUID// **&lt;Enter&gt;**

Select TOPOGRAPHY CATEGORY: **6X210**

TOPOGRAPHY CATEGORY COMMENT: **ESOPHAGEAL**

COMMENT: ESOPHAGEAL// **&lt;Enter&gt;**

Select TOPOGRAPHY CATEGORY: **6X310**

TOPOGRAPHY CATEGORY COMMENT: **GASTRIC**

COMMENT: GASTRIC// **&lt;Enter&gt;**

Select TOPOGRAPHY CATEGORY: **6X940**

TOPOGRAPHY CATEGORY COMMENT: **PERITONEAL FLUID**

COMMENT: PERITONEAL FLUID// **&lt;Enter&gt;**

Select TOPOGRAPHY CATEGORY: **7X100**

TOPOGRAPHY CATEGORY COMMENT: **URINE**

COMMENT: URINE// **&lt;Enter&gt;**

Select TOPOGRAPHY CATEGORY: **8X330**

TOPOGRAPHY CATEGORY COMMENT: **VAGINAL/CERIVICAL**

COMMENT: VAGINAL/CERVICAL// **&lt;Enter&gt;**

Select TOPOGRAPHY CATEGORY: **8X210**

TOPOGRAPHY CATEGORY COMMENT: **VAGINAL**

COMMENT: VAGINAL// **&lt;Enter&gt;**

Select TOPOGRAPHY CATEGORY: **X1010**

TOPOGRAPHY CATEGORY COMMENT: **CSF**

COMMENT: CSF// **&lt;Enter&gt;**

Select TOPOGRAPHY CATEGORY: **?**

ANSWER WITH TOPOGRAPHY CATEGORY

CHOOSE FROM:

51030	ORAL MUCOUS MEMBRANE

1Y010	SYNOVIAL FLUID

2Y030	SPUTUM

26410	BRONCHIAL MATERIAL

2Y610	PLEURAL FLUID

3X110	PERICARDIAL FLUID

6X210	ESOPHAGEAL

6X310	GASTRIC

6X940	PERITONEAL FLUID

7X100	URINE

8X210	VAGINAL

8X330	VAGINAL/CERVICAL

X1010	CSF

Select TOPOGRAPHY CATEGORY: **&lt;Enter&gt;**

#### [Edit pathology parameters (Example 2 cont’d)]

Select MORPHOLOGY ENTRY: **&lt;Enter&gt;**

ASK CYTOPAH DIAGNOSIS: **&lt;Enter&gt;**

NOTES:

•	These topography categories are then used as the list referred to in the % Pos, Atyp, Dysp, Neg, Susp, &amp; Unsat Cytopath [LRAPCYPCT] option.

•	The accession prefix appears on the hard copy reports and in the microscopic slide labels.

**Example 3:** Use of Prompt “Select MORPHOLOGY ENTRY” for Cytopathology

Select Anatomic pathology Option: **S** Supervisor, anat path

Select Supervisor, anat path Option: **ER** Edit pathology parameters

Select LAB SECTION PRINT NAME: **CY** CYTOPATHOLOGY

REPORT HEADER 1: GROSS DESCRIPTION // **&lt;Enter&gt;**

REPORT HEADER 2: MICROSCOPIC DESCRIPTION // **&lt;Enter&gt;**

PRINT SNOMED/ICD CODES: // **&lt;Enter&gt;**

GROSS DESCRIPTION SPACING: // **&lt;Enter&gt;**

LINES IN A LABEL: // **&lt;Enter&gt;**

ACCESSION PREFIX: CY// **&lt;Enter&gt;**

PRINT SF-515 LINES: // **&lt;Enter&gt;**

NEW PG FOR SUPPLEMENTARY RPT: YES// **NO** *[New]*

ASK TC CODES: // **YES**

SNOMED &amp; TC CODING:

1&gt; **&lt;Enter&gt;**

Select TOPOGRAPHY CATEGORY: 7// **&lt;Enter&gt;**

TOPOGRAPHY CATEGORY: 7// **&lt;Enter&gt;**

COMMENT: GU// **&lt;Enter&gt;**

Select TOPOGRAPHY CATEGORY: **&lt;Enter&gt;**

Select MORPHOLOGY ENTRY: CELLULAR MORPHOLOGY

(morphology list is edited here)

**NOTE:** The change allows a site to create an alternate list of morphology selections for cytology percentages instead of the exported list of %positive, negative, suspicious, and unsatisfactory.

ASK CYTOPAH DIAGNOSIS: **&lt;Enter&gt;**

Example 4:	Electron Microscopy

Select Anatomic pathology Option: **S** Supervisor, anat path

Select Supervisor, anat path Option: **Edit pat** hology parameters

Select LAB SECTION PRINT NAME: **EM** EM

REPORT HEADER 1: Gross Description// **&lt;Enter&gt;**

REPORT HEADER 2: Microscopic Description Replace **&lt;Enter&gt;**

REPORT HEADER 3: **&lt;Enter&gt;**

REPORT HEADER 4: Diagnosis:// **&lt;Enter&gt;**

PRINT SNOMED/ICD CODES: LOWER CASE// **&lt;Enter&gt;**

GROSS DESCRIPTION SPACING: **&lt;Enter&gt;**

LINES IN A LABEL: **&lt;Enter&gt;**

ACCESSION PREFIX: EM// **&lt;Enter&gt;**

PRINT SF-515 LINES: **&lt;Enter&gt;**

NEW PG FOR SUPPLEMENTARY RPT: **YES**

ASK TC CODES: **YES**

SNOMED &amp; TC CODING:

1&gt; **&lt;Enter&gt;**

Select TOPOGRAPHY CATEGORY: **&lt;Enter&gt;**

Select MORPHOLOGY ENTRY: **&lt;Enter&gt;**

ROUTINE PROCEDURE 1: 2// **&lt;Enter&gt;**

ROUTINE PROCEDURE 2: 5// **&lt;Enter&gt;**

ASK EM DIAGNOSIS: YES// **&lt;Enter&gt;**

**NOTES:**

The prompts “ROUTINE PROCEDURE 1” and “ROUTINE PROCEDURE 2” are new and are asked when EM is entered when prompted for the LAB SECTION PRINT NAME.

ROUTINE PROCEDURE 1 is the number of times procedure is routinely performed. (For EM the number of thick sections made per block.)

ROUTINE PROCEDURE 2 is the number of times routine procedure is performed. (For EM the number of grids routinely made per block.)

Example 5:	Autopsy

Select Supervisor, anat path Option: **ER** Edit pathology parameters

Select LAB SECTION PRINT NAME: **AU** AUTOPSY

REPORT HEADER 1: Clinical History// **&lt;Enter&gt;**

REPORT HEADER 2: Anatomic Diagnoses// **&lt;Enter&gt;**

REPORT HEADER 3: **&lt;Enter&gt;**

REPORT HEADER 4: **&lt;Enter&gt;**

PRINT SNOMED/ICD CODES: LOWER CASE// **&lt;Enter&gt;**

GROSS DESCRIPTION SPACING: **&lt;Enter&gt;**

LINES IN A LABEL: **&lt;Enter&gt;**

ACCESSION PREFIX: A// **&lt;Enter&gt;**

PRINT SF-515 LINES: **&lt;Enter&gt;**

NEW PG FOR SUPPLEMENTARY RPT: YES// **??** &lt;-new

If a page feed is wanted before printing the supplementary

report a 'YES' is entered.

CHOOSE FROM:

1    YES

0    NO

1    yes

0    no

NEW PG FOR SUPPLEMENTARY RPT: YES// **&lt;Enter&gt;**

ASK TC CODES: **&lt;Enter&gt;**

Select GENERIC LABEL: PROSTATE// **&lt;Enter&gt;**

GENERIC LABEL: PROSTATE// **&lt;Enter&gt;**

Select GENERIC LABEL: **&lt;Enter&gt;**

SNOMED &amp; TC CODING:

1&gt; **&lt;Enter&gt;**

Select TOPOGRAPHY CATEGORY: **&lt;Enter&gt;**

Select MORPHOLOGY ENTRY: **&lt;Enter&gt;**

Select Supervisor, anat path Option: **&lt;Enter&gt;**

#### Enter/Edit Items in a SNOMED Field [LRSNOMEDIT]

The SNOMED-coded diagnoses are not as descriptive or elaborate as the information dictated for the final report, but they are very valuable since they will be the only remaining diagnoses after the word-processing fields are purged.

Entries in the file include the field name (which is printed on the reports, etc.,) the code number, and multiple synonyms. To make data entry of the SNOMED codes easy, other synonyms can be added to reflect popular terminology.

Example:

Select Enter/edit items in a SNOMED field Option: **?** TO	Topography	(SNOMED)	enter/edit
	MO	Morphology	(SNOMED)	enter/edit
	ET	Etiology	(SNOMED)	enter/edit
	DI	Disease	(SNOMED)	enter/edit
	FU	Function	(SNOMED)	enter/edit
	PR	Procedure	(SNOMED)	enter/edit
	OC	Occupation	(SNOMED)	enter/edit

Select Enter/edit items in a SNOMED field Option: **MO** Morphology (SNOMED) enter/edit

Select MORPHOLOGY FIELD NAME: **ADENOCARCINOMA** 1	ADENOCARCINOMA, INTESTINAL TYPE   81443
	2	ADENOCARCINOMA, METASTATIC     81406
	3	ADENOCARCINOMA, MICROINVASIVE    81405
	4	ADENOCARCINOMA, MODERATELY DIFFERENTIATED 814032
	5	ADENOCARCINOMA, POORLY DIFFERENTIATED 814033
TYPE '^' TO STOP, OR
CHOOSE 1-5: **&lt;Enter&gt;** 6	ADENOCARCINOMA, UNDIFFERENTIATED 814034
	7	ADENOCARCINOMA, WELL DIFFERENTIATED 814031
	8	ADENOCARCINOMA, CYLINDROID TYP ADENOID CYSTIC CARCINOMA 82003
CHOOSE 1-8 **4** ADENOCARCINOMA, MODERATELY DIFFERENTIATED 814032
NAME: ADENOCARCINOMA, MODERATELY DIFFERENTIATED Replace **&lt;Enter&gt;** SNOMED CODE: 814032// **&lt;Enter&gt;** ABBREVIATION: **MDA** Select SYNONYM: MODERATELY DIFFERENTIATED ADENOCARCINOMA// **&lt;Enter&gt;** Select TITLE OF ARTICLE: **&lt;Enter&gt;** Select MORPHOLOGY FIELD NAME: **MDA** ADENOCARCINOMA, MODERATELY DIFFERENTIATED 814032
NAME: ADENOCARCINOMA, MODERATELY DIFFERENTIATED Replace &lt;Enter&gt;

#### Incomplete Reports, Anat Path [LRAPINC]

Incomplete reports are lacking a “DATE/TIME COMPLETED.” Since the data is entered in the FS/Gross/Micro/Dx [LRAPDGM] or FS/Gross/Micro/Dx/SNOMED Coding [LRAPDGS] options, they generally are reports for which the microscopic description was not entered.

The listing of “Incomplete Reports” is **not** the same as the listing of “Unverified Reports.” Reports can be completed, signed, and distributed even though the verification/release step was overlooked.

Example:

Select Anatomic pathology Option: **S** Supervisor, anat path

Select Supervisor, anat path Option: **IR** Incomplete reports, anat path

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY 

		SURGICAL PATHOLOGY Incomplete Reports
Start with Date TODAY// **&lt;Enter&gt;** NOV 22, 1990
Go   to  Date TODAY// **11 1** (NOV 01, 1990)
Select Print Device: *[Enter Print Device Here]*

Incomplete SURGICAL PATHOLOGY Reports

FROM NOV 22, 1990 TO NOV 1, 1990

Acc # Date   Patient       ID  Location      Pathologist

-----------------------------------------------------------------------------

20	11/07/90	LABPATIENT1, FOUR	8762  1A	LABPROVIDER, THREE

#### Print Path Modifications [LRAPMOD]

A copy of the modifications provides useful documentation for quality assurance purposes. This option provides a consolidated report with both the original and the modified data. These changes must be printed **before** purging the word processing fields!

**NOTE:** The Print Path Modifications [LRAPMOD] option was **modified** by the release of patch LR*5.2*248. This option will print audit information for any ‘Supplementary Report’ that was modified after its release.

##### Example: Print Pathology Report Modifications

Select Supervisor, anat path Option: **MR** Print path modifications

Print pathology report modifications

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

Select Patient Name: LABPATIENT1, TEN  02-01-22  000-00-0110   NO   NSC VETERAN

LABPATIENT1, TEN ID: 000-00-011 Physician: LABPROVIDER4, THREE

AGE: 72 DATE OF BIRTH: FEB 1, 1922

Ward on Adm: 1 EAST Service: MEDICINE

Adm Date: APR 8, 1993 10:53 Adm DX: ACCIDENT

Present Ward: 1 EAST          MD:

Specimen(s)       Count #  Accession #  Date Obtained

( 1)      7    AUG 25, 1994 not verified

LEFT LEG

( 2)      6    AUG 25, 1994 not verified

left hip chip

( 3)      2    AUG 24, 1994

PROSTATE CHIPS

Choose Count #(1-3): **3**

Accession #: 2  Date Obtained: AUG 24, 1994

Select Print Device: *[Enter Print Device Here]*

**Example:** Print Pathology Report Modifications *continued*

-----------------------------------------------------------------------------

MEDICAL RECORD |          SURGICAL PATHOLOGY        Pg 1

-----------------------------------------------------------------------------

Submitted by: LABPROVIDER4, THREE       Date obtained: AUG 24, 1994

-----------------------------------------------------------------------------Specimen (Received AUG 24, 1994 10:37):

PROSTATE CHIPS

-----------------------------------------------------------------------------

Brief Clinical History:

Nocturia and difficulty voiding urine.

-----------------------------------------------------------------------------Preoperative Diagnosis:

same.

-----------------------------------------------------------------------------

Operative Findings:

same.

-----------------------------------------------------------------------------

Postoperative Diagnosis:

same.

Surgeon/physician: LABPROVIDER4, FOUR

=============================================================================

PATHOLOGY REPORT

Laboratory: VAMC                   Accession No. SP 94 2

-----------------------------------------------------------------------------

Pathology Resident: LABPROVIDER1, FIVE

Frozen Section:

Basal cell .

Gross Description:

Specimen consists of 5 grams of prostate gland tissue.

Microscopic exam/diagnosis:

*** MODIFIED REPORT ***

(Last modified: AUG 27, 1994 17:30 typed by LABUSER, TWO)

Date modified:AUG 27, 1994 17:19 typed by LABUSER, TWO  Glomerular basement membranes are thickenedd and there is increased

mesangial matrix.

Date modified:AUG 27, 1994 17:30 typed by LABUSER, TWO

Glomerular basement membranes are thickenedd and there is increased

mesangial matrix. Also present are small prostatic infarts and foci

of squamous metaplasia.

==========Text below appears on final report==========

Glomerular basement membranes are thickenedd and there is increased

(See next page)

LABPROVIDER4, FOUR                ec | Date AUG 25, 1994

LABPATIENT1, TEN                  STANDARD FORM 515

ID:00-00-0110 SEX:F  DOB:2/1/22  AGE:72   LOC:1 EAST

ADM:APR 8, 1993 DX:ACCIDENT           LABPROVIDER4, THREE

**Example:** Print pathology report modifications *continued*

----------------------------------------------------------------------------

MEDICAL RECORD |          SURGICAL PATHOLOGY       Pg 2

----------------------------------------------------------------------------

PATHOLOGY REPORT

Laboratory: VAMC                   Accession No. SP 94 2

-----------------------------------------------------------------------------

mesangial matrix. Also present are small prostatic infarts and foci

of squamous metaplasia. Another small infarts and foci of squamous

metaplasia.

Supplementary Report:

Date: AUG 26, 1994 18:09

This is an example of a supplementary report. It can be used to report

the results of recuts.

Date: AUG 26, 1994 18:10

***MODIFIED REPORT***

(Last modified: AUG 26, 1994 18:19 typed by LABUSER, FOUR)

Date modified: AUG 26, 1994 18:19 typed by LABUSER, FOUR

This is another supplementary report.

==========Text below appears on final report==========

This is another supplementary report. When the supplementary report was

released, this line was added to the report.

CONSULTATION AFIP#123456789 Date: AUG 26, 1994 18:17

PROSTATIC FASCIA

This is an example of a consultation sent to the AFIP.

SNOMED code(s):

T-18969: PROSTATIC FASCIA

P-Y333 : ADMINISTRATION OF MEDICATION, EMERGENCY

----------------------------------------------------------------------------

(End of report)

LABPROVIDER4, FOUR                  ec | Date AUG 25, 1994

----------------------------------------------------------------------------

LABPATIENT1, TEN                  STANDARD FORM 515

ID: 00-00-0110 SEX:M DOB:2/1/22   AGE:72    LOC:1 EAST

ADM:APR 8, 1993 DX:ACCIDENT           LABPROVIDER4, THREE

#### Anatomic Pathology Topography Counts [LRAPC]

A breakdown of the specimens accessioned within a specified time may be useful for quality assurance purposes, survey responses, etc. This option searches all topographies coded for the accessions within the time specified; therefore, only those with SNOMED codes entered can be evaluated.

Example:

Select Supervisor, anat path Option: **TC** Anatomic pathology topography counts

TOPOGRAPHY COUNTS

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY 

TOPOGRAPHY (Organ/tissue)
Choice # 1: Select 1 or more characters of the code: **01** Choice # 2: Select 1 or more characters of the code: **2** Choice # 3: Select 1 or more characters of the code: **5** Choice # 4: Select 1 or more characters of the code: **6** Choice # 5: Select 1 or more characters of the code: **7** Choice # 6: Select 1 or more characters of the code: **&lt;Enter&gt;** Start with Date TODAY// **&lt;Enter&gt;** Go  to   Date TODAY// **1 1** (JAN 01, 1988)
Select Print Device: [Enter Print Device Here]

-----------------------------------------------------------------------------

LABORATORY SERVICE R5ISC
NOV 22, 1990 08:26	SURGICAL PATHOLOGY TOPOGRAPHY COUNTS		PG:1
Topography	Count	From:JAN 1, 1990	To:NOV 22, 1990
------------------------------------------------------------------------------
	T-2....	2	12.50%
	T-5....	3	18.75%
	T-7....	2	12.50%
	T-01...	7	43.75%

# Patients: 11
# accessions: 22
# organ/tissues: 16
% = % of organ/tissues

#### Delete Free Text Specimen Entries [LRAPDFS]

This option lets you purge data associated with the specimen regarding the special stains. Separating this from the purging of other word-processing fields provides additional flexibility for the site in determining the length of time to keep data on-line. This may be particularly important for evaluation of workload over an extended period of time.

Example:

Select Supervisor, anat path Option: **DS** Delete free text specimen entries

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY 

Remove free text specimen entries from SURGICAL PATHOLOGY File

Start with Date TODAY// **1 1 89** (JAN 01, 1989)
Go  to   Date TODAY// **12 31 89** (DEC 31, 1989)

		OK to DELETE FREE TEXT ENTRIES from
		JAN 1, 1989 to DEC 31, 1989? NO// **Y** (YES)
. . . . . . . . . . . . . . . . . . . . . . . . 
OK, DONE.

#### Missing AP Alert Search (LRAPALERT)

This option will search verified Anatomic Pathology cases to determine if alert(s) were generated and if the ORDERS (#100) file is set correctly. Sites will be able to manually run the option and/or set it in TaskMan to run automatically at various times during the day.

Several sites have find that alerts are not generated after some cases are verified. The issue is not reproducible except by forcing a session disconnect after electronically signing a case but before specifying whether additional alerts are sent. It is unknown whether this is the scenario causing missing alerts at sites.

The option is located under the LRAPSUPER (Supervisor, anat path) menu:

AL   Missing AP Alert Search

Select Supervisor, anat path &lt;TEST ACCOUNT&gt; Option: AL Missing AP Alert Search

This option will search for missing Anatomic Pathology alerts

on verified accessions as well as other issues such as

incorrect settings in the Orders (#100) file.

This routine will run in the background and send an alert as well as

a MailMan message to you as well as the MailMan group "LMI".

The search may take upwards of 20 minutes to run the first time

or if it is run infrequently.

The dates for the following prompts pertain to the dates that an

Anatomic Pathology case is verified.

(The date range cannot be more than a year due to the possibility that

the search may take a long time to complete.)

Date to begin search: T-1       MAY 02, 2018

Date to end search: T         MAY 03, 2018

Requested Start Time: NOW// (MAY 03, 2018@11:44:26)

Task #: 8041918 has been queued to run on May 03, 2018@11:44:26

Alerts and MailMan messages are sent to the user running the option as well as members of the “LMI” MailMan group. Recipients can then decide whether an alert needs to be manually queued using the already existing option “Send an AP Alert” which is under the menu "Verify/release menu, anat path".

**If no issues are found:**

**NOTE** : If TaskMan executes the search option, alert(s) and a MailMan message are sent only if issues are found.

- Alert:

1.I No Missing AP Alerts Found on May 03, 2018@11:44

- MailMan message:

Subj: No Anatomic Pathology Alert Search Issues Found [#269405] 05/03/18@11:44

2 lines

From: Anatomic Pathology Missing Alert Search In 'IN' basket.  Page 1 *New*

-------------------------------------------------------------------------------

No missing Anatomic Pathology alert issues found on May 03, 2018@11:44.

Date Range Searched: May 02, 2018 to May 03, 2018.

**If issues are found** *(the following case was configured to mimic the issue in a test account)* :

**NOTE:** If the option was executed by TaskMan, alert(s) and a MailMan message are only sent

to members of the LMI mail group.

- Alert (an alert is sent for each case which has a missing alert):

1.I *** ALERT NOT SENT FOR ACCESSION: SP 18 61 ***

- MailMan message (all issues found are combined into one MailMan message):

Subj: Anatomic Pathology Alert Search Issues Found [#269407] 05/03/18@11:52

6 lines

From: Anatomic Pathology Missing Alert Search In 'IN' basket.  Page 1 *New*

-------------------------------------------------------------------------------

Date Range searched: May 02, 2018 to May 03, 2018.

Anatomic Pathology Alert Search Issues Found

SP 18 61:

- is missing package reference for order 5598183.

- has no results date/time for order 5598183.

- *** did not generate an alert. ***

#### AP Quality Assurance [LRAPQA]

Although quality assurance systems have been integral components of clinical pathology and blood usage review for many years, they did not exist as structured systems in anatomic pathology. Recent changes made by the Joint Commission for the Accreditation of Healthcare Organizations (JCAHO) in monitoring medical staff functions have necessitated the development of a comparable system for anatomic pathology.

Quality assurance in anatomic pathology can be defined as the mechanisms and programs which assure quality care through accuracy in tissue/cell diagnosis. In anatomic pathology, the diagnosis is based on a number of steps, beginning with the submission of tissue/specimens for examination, examination of the specimens, evaluation and correlation of clinical data and history, assessment of the morphological observations, and concluding with the issuance of a final diagnosis. Since quality assurance deals with outcomes, the clinical course of the patient subsequent to the diagnosis must also be evaluated. This encompasses issues related to the timeliness of the report and correlation of the pathology report with other clinical findings/reports (e.g., diagnostic radiology).

To simplify the process of identifying cases for both internal and external review, a group of options has been created to extract cases to meet preset criteria for surgical pathology. These include:

100% review of cases involving frozen sections

100% review of cases involving a bone, muscle or soft tissue malignancy

100% review of cases involving a gynecological malignancy

100% review of cases involving a malignancy from a specified topography

10% random review of cases

Listing of cases sent for consultation (AFIP, SERS, etc.,)

In addition, options have been created to extract cases for cytopathology, including:

100% review of cases involving a malignancy or suspicious morphology

100% review of cases accessioned for correlation of diagnoses

Options are also included to assist in the performance of surgical case review by the Tissue Committee (TC). By entering a numeric QA code at the time the case is finalized, the pathologist assists in the extraction of cases according to certain criteria designated by the Tissue Committee.

##### Summary of TC and QA Codes

The following table summarizes the differences between TC Codes and QA Codes:

**TC Codes	QA Codes**

Numeric TC codes may be 		QA codes defined in LAB

assigned description in LAB		DESCRIPTIONS file

DESCRIPTIONS file		(Screen=I AP General)

(Screen=AP SURG)

-	Used to review Surgical cases	-	Entered for Surgical or

Cytopath reports

-	Supervisor option - Edit QA	-	Supervisor option- Edit

Site Parameters to allow TC		QA Site Parameters to allow

code entry		QA code entry

-	TC code should be entered for 	-	QA Codes Entry/edit used to

each surgical report		enter QA code for an accession

-	Use Tissue Committee Review	- 	QA Outcome Review cases

Cases to retrieve reports		used to retrieve reports

##### QA Codes Entry/Edit [LRAPQACD]

You can enter or edit both QA and TC codes with this option. This will allow access to that specific field once the report has been released, without placing the report into a print queue or classifying the report as “modified.”

This data is not included in any display or print option other than Tissue Committee review cases and QA outcome review cases. Only entries in the LAB DESCRIPTION file using the AP GENERAL (I) screen can be selected.

**Example 1:** Surgical Pathology - Editing of TC Code and Entry of QA Code

Select AP quality assurance reports Option: **CE** Quality assurance code entry

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

Data entry for 1990 ? YES// **&lt;Enter&gt;** (YES)

Select Accession Number/Pt name: **5630** for 1990

LABPATIENT6, TWO. ID: 000-00-0062

Specimen(s):

POLYPS X2

Select SPECIMEN COMMENT:

TC CODE: 1// **?**

CHOOSE FROM:

1	1

2	2

3	3

4	4

5	5

6	6

7	7

8	8

9	9

0	0

TC CODE: 1// **2**

Select QA CODE: **?**

ANSWER WITH QA CODE

YOU MAY ENTER A NEW QA CODE, IF YOU WISH

QA codes must be less than 3 characters.

Selects entries with less than 3 characters

ANSWER WITH LAB DESCRIPTIONS NAME

DO YOU WANT THE ENTIRE LAB DESCRIPTIONS LIST? **Y** (YES)

CHOOSE FROM:

C1	CYTOLOGY CORRELATION QA REVIEW-no disagreement

C2	CYTOLOGY CORRELATION QA REVIEW-minor disagreement (no Dx/Rx change)

C3	CYTOLOGY CORRELATION QA REVIEW-major disagreement (Dx or Rx change)

F1	FROZEN SECTION QA REVIEW-no disagreement

F2	FROZEN SECTION QA REVIEW-minor disagreement (no Dx/Rx change)

F3	FROZEN SECTION QA REVIEW-major disagreement (Dx or Rx change)

M1	MALIGNANCY QA REVIEW-no disagreement

M2	MALIGNANCY QA REVIEW-minor disagreement (no Dx/Rx change)

M3	MALIGNANCY QA REVIEW-major disagreement (Dx or Rx change)

R1	RANDOM QA REVIEW-no disagreement

R2	RANDOM QA REVIEW-minor disagreement (no Dx/Rx change)

R3	RANDOM QA REVIEW-major disagreement (Dx or Rx change)

S1	SERS/SERA QA REVIEW-no disagreement

S2	SERS/SERA QA REVIEW-minor disagreement (no Dx/Rx change)

S3	SERS/SERA QA REVIEW-major disagreement (Dx or Rx change)

S4	SERS/SERA QA REVIEW-legitimate disagreement

Select QA CODE: **M1** MALIGNANCY QA REVIEW-no disagreement

Select QA CODE: **&lt;Enter&gt;**

Select Accession Number/Pt name: **&lt;Enter&gt;**

**NOTE:** Although the “TC CODE: 1//” prompt is a numeric set, no description is included. If a description is entered into the LAB DESCRIPTIONS file (#62.5), specifying AP SURG as the screen, that description will appear on the report generated by Tissue Committee Review Cases.

**Example 2:** Entry of QA Code for Autopsy

Select AP quality assurance reports Option: **CE** Quality assurance code entry

Select ANATOMIC PATHOLOGY section: **AU** AUTOPSY

Data entry for 1992 ? YES// **&lt;Enter&gt;** (YES)

Select Accession Number/Pt name: **63** for 1992

LABPATIENT6, THREE  ID: 000-00-0063

Select AUTOPSY QA CODE: **??**

CHOOSE FROM:

A1   AU PRE/POSTMORTEM CORRELATION - Diagnosis confirmed/verified

A2   AU PRE/POSTMORTEM CORRELATION - indeterminate

A3   AU PRE/POSTMORTEM CORRELATION - significant clarification of diff.Dx

A4   AU PRE/POSTMORTEM CORRELATION - major unsuspected/additional Dx

A5   AU PRE/POSTMORTEM CORRELATION - major disagreement in Dx

A6   AU PRE/POSTMORTEM CORRELATION - clinical info insufficient

A7   AUTOPSY QA REVIEW - no disagreement on peer review

A8   AUTOPSY QA REVIEW - minor disagreement on peer review (no Dx change)

A9   AUTOPSY QA REVIEW - major disagreement on peer review

D1   DEATH CLINICAL FACTORS - unremitting course of disease

D2   DEATH CLINICAL FACTORS - error in judgment/treatment

D3   DEATH CLINICAL FACTORS - complication or therapeutic proc.

D4   DEATH CLINICAL FACTORS - unrecognized diagnosis w/ premortem evidence

D8   DEATH - NO PRONOUNCEMENT DOCUMENTED

Select AUTOPSY QA CODE: **A1** AU PRE/POSTMORTEM CORRELATION - Diagnosis confirmed/verified

Select AUTOPSY QA CODE: **D1** DEATH CLINICAL FACTORS- unremitting course of disease

Select AUTOPSY QA CODE: **&lt;Enter&gt;**

Select Accession Number/Pt name: **&lt;Enter&gt;**


##### AP Consultation Searches and Reports [LRAPQACN]

Internal and external consultations may be entered for individual anatomic pathology accessions using procedure codes from the SNOMED manuals which include:

0650	Consultation NOS

0651	Consultation, Limited

0652	Consultation, Intermediate

0653	Consultation, Extensive

0654	Consultation, Comprehensive

However, the procedure code may be up to seven digits. This allows further flexibility in specifying the type of consultation, etc., For example, external consultations might include:

0654001		AFIP		consultation

0654002		SERS	external review

0654003		SERA	external review

Internal consultations might include:

0654004		Consultation, internal

0654005		GI conference

0654006		Pulmonary conference

0654007		Renal conference

0654008		Morbidity &amp; Mortality

0654009		Tumor Board

By entering the procedure codes for the individual cases, the information is documented as part of the Cum path data summary for the patient for future reference. By entering specific ID numbers and dates for the case using the Spec Studies-EM;Immuno;Consult;Pic, Anat Path option, the cross-referencing is complete.

Searches are specific for the accession area, including all topographies. However, the search can be broad (to include all procedure codes starting with 065) or narrow (all 4-7 digits specified). Cases are listed by patient, and then by accession number, followed by the calculations and the data for that specific accession. The data for each accession is identical to that included on the “log book”; i.e., the accession information, the SNOMED codes, and all special studies information.

The following abbreviations are used:

AFIP = Armed Forces Institute of Pathology

SERS = Systematic External Review of Surgical Pathology

SERA = Systematic External Review of Autopsies

Example:	Listing of Cases Sent to SERS

Select Supervisor, anat path Option: **QA** AP quality assurance reports

Select AP quality assurance reports Option: **CN** AP consultation searches and reports

Consultation search with report.

This report may take a while and should be queued to print at non-peak hours.

OK to continue ? NO// **Y** (YES)

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

Choice # 1 Select consultation code (must begin with 065): **0654002**

Choice # 2: Select consultation code (must begin with 065): **&lt;Enter&gt;**

Start with Date TODAY// **1-1-90** (JAN 01, 1990)

Go  to   Date TODAY// **1-31-90** (JAN 31, 1990)

Select Print Device: *[Enter Print Device Here]*

**NOTE:** In this example, the search will contain all topographies for which the procedure code 0654002 (SERS external review) has been entered. This search and case listing can be used for several purposes, including:

tally of number and type of cases sent to SERS

documentation of AFIP # for each specific case sent to SERS

reviewing specific outcomes for quality assurance purposes; i.e., # cases sent, # agreements, # disagreements, etc.

#### [Listing of cases sent to SERS Printout]

OCT 16, 1990 14:55 SURGICAL PATHOLOGY SEARCH(JAN 1, 1990=&gt;JAN 31, 1990) Pg 1

# =  patient

SNOMED TOPOGRAPHY CODE: ALL--	SNOMED PROCEDURE CODE: 0654002

-----------------------------------------------------------------------------

NAME		ID	SEX AGE	ACC #  ORGAN/TISSUE  PROCEDURE

LABPATIENT6, FOUR	0064	M	92	284-89	PROSTATE	SERS EXTERNAL REVIEW

LABPATIENT6, FIVE	0065	M	62	 95-89	PROSTATE	SERS EXTERNAL REVIEW

LABPATIENT6, SIX	0066	M	61	205-89		SERS EXTERNAL REVIEW

LABPATIENT6, SEVEN0067	M	42	 23-89	ESOPHAGUS	SERS EXTERNAL REVIEW

LABPATIENT6, EIGHT0068	M	62	518-89	SKIN OF TRUNK	SERS EXTERNAL REVIEW

-----------------------------------------------------------------------------

OCT 16, 1990 14:55 SURGICAL PATHOLOGY SEARCH(JAN 1, 1990=&gt;JAN 31, 1990  Pg 2

# =  patient

SNOMED TOPOGRAPHY CODE: ALL--	SNOMED PROCEDURE CODE: 0654002

-----------------------------------------------------------------------------

ACC #	NAME	ID	SEX	AGE	ORGAN/TISSUE  PROCEDURE

284-89	LABPATIENT6, FOUR	0064M	92	PROSTATE	SERS EXTERNAL REVIEW

95-89	LABPATIENT6, FIVE	0065	M	62	PROSTATE	SERS EXTERNAL REVIEW

205-89	LABPATIENT6, SIX	0066	M	61		SERS EXTERNAL REVIEW

23-89	LABPATIENT6, SEVEN0067	M	42	ESOPHAGUS	SERS EXTERNAL REVIEW

518-89	LABPATIENT6, EIGHT0068	M	62	SKIN OF TRUNK	SERS EXTERNAL REVIEW

-----------------------------------------------------------------------------

OCT 16, 1990 14:55 SURGICAL PATHOLOGY SEARCH(JAN 1, 1990=&gt;JAN 31, 1990) Pg 3

# =  patient

SNOMED TOPOGRAPHY CODE: ALL--	SNOMED PROCEDURE CODE: 0654002

-----------------------------------------------------------------------------

RESULT OF SURGICAL PATHOLOGY SEARCH

PATIENTS WITHIN PERIOD SEARCHED: 563

SURGICAL PATHOLOGY ACCESSIONS WITHIN PERIOD SEARCHED: 565

5 OF	563 PATIENTS (0.89%)

5 OF	669 SNOMED CODE ALL   SPECIMENS( 0.75%)

669 ORGAN/TISSUE SPECIMENS WITHIN PERIOD SEARCHED

(SNOMED TOPOGRAPHY CODE ALL IS 100.00%)

#### Listing of cases sent to SERS Printout (contd)

DEC 27, 1989 08:19 vamc				Pg: 4

SURGICAL PATHOLOGY CONSULTATIONS

-----------------------------------------------------------------------------

LABPATIENT6, SEVEN		000-00-0067

Organ/tissue:		Date rec'd: 01/04/89	Acc #:	23

ESOPHAGUS

SERS EXTERNAL REVIEW

ACUTE INFLAMMATION

CONSULTATION AFIP#2249480-1 Date: OCT 20, 1989

-----------------------------------------------------------------------------

LABPATIENT6, FIVE				000-00-0065

Organ/tissue:		Date rec'd: 01/09/89	Acc #:	95

PROSTATE

SERS EXTERNAL REVIEW

HYPERPLASIA, GLANDULAR

-----------------------------------------------------------------------------

LABPATIENT6, SIX					000-00-0066

Organ/tissue:		Date rec'd: 01/13/89	Acc #:	205

SERS EXTERNAL REVIEW

ADENOMATOUS POLYP

CONSULTATION AFIP#2249395-1 Date: OCT 18, 1989

-----------------------------------------------------------------------------

LABPATIENT6, FOUR					000-00-0064

Organ/tissue:	Date rec'd: 01/19/89		Acc #:	284

PROSTATE

BIOPSY, NOS

SERS EXTERNAL REVIEW

INFLAMMATION

ADENOCARCINOMA

CONSULTATION AFIP#2249417-3 Date: NOV 21, 1989

-----------------------------------------------------------------------------

LABPATIENT6, NINE					000-00-0069

Organ/tissue:		Date rec'd: 01/30/89	Acc #:	518

SKIN OF TRUNK

SERS EXTERNAL REVIEW

BOWEN'S DISEASE

KERATOSIS, ACTINIC

CONSULTATION AFIP#2249406-6 Date: OCT 18, 1989

**NOTE:** This last page is particularly useful as a work list for tracking cases submitted, but for which no report has been received, such as accession #95 above.

##### Cum Path Summaries for Quality Assurance [LRAPQAC]

By compiling a consolidated report of the cum path data summaries for all patients having specimens accessioned for a specified accession area, the process of reviewing the diagnoses for correlation is greatly simplified.

For example, by routinely printing the report for cytology on a monthly basis, the reviewer can determine the number of cases in which a subsequent specimen was submitted to surgical pathology and whether the diagnoses correlate. In the following case, the patient underwent a fine needle biopsy on 1/4/89 (submitted to Cytopathology) and subsequently underwent surgery on 1/26/89, at which time specimens were submitted to Surgical Pathology and Electron Microscopy.

Example:

Select AP quality assurance reports Option: **CS** Cum path summaries for quality assurance

Quality assurance cum path data summaries

for accessions from one date to another

Select ANATOMIC PATHOLOGY section: **CY** CYTOPATHOLOGY

Do you want to specify a site/specimen (Topography) ? NO// **YES** (YES)

TOPOGRAPHY (Organ/Tissue)

Select 1 or more characters of the code

For all sites type 'ALL' : ALL

Start with Date TODAY// **1/1/89** (JAN 01, 1989)

Go  to   Date TODAY// **1/31/89** (JAN 31, 1989)

Select Print Device: *[Enter Print Device Here]*

OCT 16, 1989  11:45            VAMC      Pg 1

ANATOMIC PATHOLOGY

CYTOPATHOLOGY QA from JAN 1, 1989 to JAN 31, 1989

-----------------------------------------------------------------------------

LABPATIENT6, TEN       SSN:000-00-0610 DOB:APR 4, 1944

SURGICAL PATHOLOGY

Organ/tissue:     Date rec'd: 01/08/89	Acc #:	726

BONE MARROW

LYMPHOCYTIC INFILTRATE

Organ/tissue:     Date rec'd: 01/26/89	Acc #:	435

LYMPH NODE OF NECK

FROZEN SECTION

MALIGNANT LYMPHOMA, UNDIFFERENTIATED CELL TYPE

IMMUNOPEROXIDASE IP89-43 Date: JAN 30, 1989

#1.	FROZEN SECTION

CYTOPATHOLOGY

Organ/tissue:     Date rec'd: 01/04/89	Acc #:	16

LYMPH NODE OF NECK

BIOPSY, FINE NEEDLE

HYPERPLASIA, ATYPICAL LYMPHOID

IMMUNOPEROXIDASE IP89-6 Date: JAN 6, 1989

ELECTRON MICROSCOPY

Organ/tissue:     Date rec'd: 01/26/89	Acc #:	45

LYMPH NODE OF NECK

ELECTRON MICROSCOPY

MALIGNANT LYMPHOMA, UNDIFFERENTIATED CELL TYPE

S89-435-1

Organ/tissue:     Date rec'd: 01/04/89	Acc #:	 3

LYMPH NODE OF NECK

LYMPHOCYTIC INFILTRATE

C89-16

##### .% Pos, Atyp, Dysp, Neg, Susp, &amp; Unsat Cytopath [LRAPCYPCT]

Use this option to print the number and the % of positive, negative, and suspicious specimens for malignancy and unsatisfactory specimens from one date to another. The listing provides information which will assist in meeting a requirement of the College of American Pathologists (CAP). The prompt “Use topography category list?” will appear only if a topography list has been created using the [LRAPDAR] option in the Supervisor’s Menu.

The morphology list and the topography category list are defined using the Edit Pathology Report Parameters [LRAPDHR] option.

**Example 1:** Using morphology entry list

Select Anat path accession reports Option: **CY** % Pos, Atyp, Dysp, Neg, Susp, &amp; Unsat cytopath

Cytology Specimens:

Use morphology list? YES// **&lt;Enter&gt;** (YES)

Use topography category list? YES// **NO** Select 1 or more characters of SNOMED TOPOGRAPHY code (Choice # 1): **2** ENTER IDENTIFYING COMMENT: **RESPIRATORY** Select 1 or more characters of SNOMED TOPOGRAPHY code (Choice # 2): **7** ENTER IDENTIFYING COMMENT: **GU** Select 1 or more characters of SNOMED TOPOGRAPHY code (Choice # 3): **&lt;Enter&gt;** Start with Date TODAY// **&lt;Enter&gt;** NOV 21, 1988
Go  to   Date TODAY// **1 1** (JAN 01, 1988)
Select Print Device: *[Enter Print Device Here]*

-----------------------------------------------------------------------------
NOV 21, 1988 14:35    					Pg: 1
CYTOPATHOLOGY	From JAN 1, 1988 To NOV 21, 1988

Location           Location Count  Count

-----------------------------------------------------------------------------
RESPIRATORY (2):					3
	NEGATIVE FOR MALIGNANT CELLS				2 	 (66.7%)
	GU (7):						1
	SUSPICIOUS FOR MALIGNANT CELLS			1		 (100.0%)
Total specimens found:					4
	UNSATISFACTORY SPECIMEN							 ( 0.0%)
	NEGATIVE FOR MALIGNANT CELLS				2		 (50.0%)
	SUSPICIOUS FOR MALIGNANT CELLS			1		 (25.0%)
	POSITIVE FOR MALIGNANT CELLS						 ( 0.0%)

**NOTE:** As shown in the example above, failure to enter SNOMED codes for each category results in the sum of the % not being equal to 100%; i.e., there are four specimens and only three were coded.

**Example 2:** Using default morphology codes and defined topography category listing

Select AP Quality Assurance Option: **CY** % Pos, Atyp, Dysp, Neg, Susp, &amp; Unsat cytopath

		Cytology Specimens:

Use morphology list? YES// **NO**

% POSITIVE FOR MALIGNANT CELLS

% SUSPICIOUS FOR MALIGNANT CELLS

% NEGATIVE FOR MALIGNANT CELLS

% UNSATISFACTORY SPECIMEN

Use topography category list? YES// ?

ANSWER “YES”, “NO”, “^”, “@” 
	or press RETURN key to accept default response (if one)? YES// &lt;Enter&gt;

51030	ORAL MUCOUS MEMBRANE

1Y010	SYNOVIAL FLUID

2Y030	SPUTUM

2Y410	BRONCHIA MATERIAL

2Y610	PLEURAL FLUID

3X110	PERICARDIAL FLUID

6X210	ESOPHAGEAL

6X310	GASTRIC

6X940	PERITONEAL FLUID

7X100	URINE

8X210	VAGINAL

8X330	VAGINAL/CERVICAL

X1010	CSF

Start with Date TODAY// **5-1-90** (MAY 01, 1990)

Go    to    Date TODAY// **5/31/90** (MAY 31, 1990)

Select Print Device: *[Enter Print Device Here]*

**NOTE:** The list at the “Use topography category list? YES//” prompt is generated at the using the Edit Pathology Report Parameters option in the Supervisor’s Menu.

JUL 27, 1990 12:51  VAMC					Pg: 1

CYTOPATHOLOGY COUNTS	From MAY 1, 1990 To MAY 31, 1990

Location               Location Count    Count

-----------------------------------------------------------------------------

ORAL MUCOUS MEMBRANE (51030):		1

NEGATIVE FOR MALIGNANT CELLS	1  (100.0%)

SYNOVIAL FLUID (1Y010):		1

NEGATIVE FOR MALIGNANT CELLS	1  (100.0%)

SPUTUM (2Y030):		12

UNSATISFACTORY SPECIMEN	1   (8.3%)

NEGATIVE FOR MALIGNANT CELLS	11   (91.7%)

BRONCHIAL MATERIAL (2Y410):		10

NEGATIVE FOR MALIGNANT CELLS	 5   (50.0%)

SUSPICIOUS FOR MALIGNANT CELLS	 1   (10.0%)

POSITIVE FOR MALIGNANT CELLS	 2   (20.0%)

PLEURAL FLUID (2Y610):		5

NEGATIVE FOR MALIGNANT CELLS	 5  (100.0%)

ESOPHAGEAL  (6X210):		2

NEGATIVE FOR MALIGNANT CELLS	 1   (50.0%)

PERITONEAL FLUID  (6X940):		4

NEGATIVE FOR MALIGNANT CELLS	 4  (100.0%)

URINE  (7X100):		42

NEGATIVE FOR MALIGNANT CELLS	31   (73.8%)

SUSPICIOUS FOR MALIGNANT CELLS	 5   (11.9%)

VAGINAL  (8X210):		1

NEGATIVE FOR MALIGNANT CELLS	 1   (50.0%)

VAGINAL/CERVICAL  (8X330):		2

NEGATIVE FOR MALIGNANT CELLS	 1   (50.0%)

CSF  (X1010):		5

UNSATISFACTORY SPECIMEN	1   (20.0%)

NEGATIVE FOR MALIGNANT CELLS	 4   (80.0%)

Total specimens found:		85

UNSATISFACTORY SPECIMENS	 2   (2.4%)

NEGATIVE FOR MALIGNANT CELLS	65   (76.5%)

SUSPICIOUS FOR MALIGNANT CELLS	 6   (7.1%)

POSITIVE FOR MALIGNANT CELLS	 2   (2.4%)

##### Delete TC and QA Code [LRAPQADEL]

This option allows purging of the Tissue Committee (TC) codes and the Quality Assurance (QA) codes. Separating this from the other purges allows additional flexibility for the site in determining the length of time to keep data on-line.

Example:

Select AP quality assurance reports Option: **DC** Delete TC and QA codes

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

Delete Tissue committee/QA codes from SURGICAL PATHOLOGY File

Start with Date TODAY// **1-1-90**

Go  to  Date TODAY// **3-3-90**

OK to DELETE TC/QA codes

from one date thru another ? NO// **&lt;Enter&gt;** (NO)

Select AP quality assurance Option: **&lt;Enter&gt;**

##### Frozen Section, Surgical Path Correlation [LRAPQAFS]

By entering a procedure code (3082) for each case involving a frozen section, a search can be done on a regular basis to identify cases for review. These cases can then be reviewed to determine:

1. whether the frozen section diagnosis correlates with that of the permanent section diagnosis
2. whether the documentation of the required physician diagnosis was appropriate, and/or
3. whether a second pathologist agrees with the original diagnosis.

In order to expedite the review process, the report generated includes the data obtained from the search; i.e., alphabetical listing by patient followed by the listing by accession number and the calculations, and a copy of the final report for each accession identified.

**Example:** Frozen Section Search

ANATOMIC PATHOLOGY MENU

Select Anatomic pathology Option: **S** Supervisor, anat path

Select Supervisor, anat path Option: **QA** AP quality assurance

Select AP quality assurance Option: **FS** Frozen section, surgical

path correlation

Frozen section search with optional permanent path reports.

This report may take a while and should be queued to print at

non-peak hours.

OK to continue ? NO// **Y** (YES)

Do you want corresponding permanent pathology reports

to print following search ? NO// **&lt;Enter&gt;** (NO)

-----------------------------------------------------------------------------

Start with Date TODAY// **&lt;Enter&gt;** MAR 19, 1992

Go  to  Date TODAY// **1 1** (JAN 01, 1992)

Select Print Device: *[Enter Print Device Here]*

**NOTE:** This search includes all topographies.

MAR 19, 1992 07:05 SURGICAL PATHOLOGY SEARCH(JAN 01, 1992=&gt;Mar 19, 1992) Pg 1

# =  patient

SNOMED TOPOGRAPHY CODE: ALL --SNOMED PROCEDURE CODE: 3081 or 3082-

-----------------------------------------------------------------------------

NAME	ID	SEX	AGE	ACC #	ORGAN/TISSUE	PROCEDURE

LABPATIENT7, ONE	0071	M	31	435-92	LYMPH NODE OF NECK	FROZEN SECTION

PIRIFORM RECESS	FROZEN SECTION

LABPATIENT7, TWO	0072	M	58	443-92	LARYNX	FROZEN SECTION

-----------------------------------------------------------------------------

MAR 19, 1992 07:05 SURGICAL PATHOLOGY SEARCH(JAN 01, 1992=&gt;Mar 19, 1992) Pg 2

# =  patient

SNOMED TOPOGRAPHY CODE: ALL --	SNOMED PROCEDURE CODE: 3081 or 3082-

-----------------------------------------------------------------------------

ACC #	NAME	ID	SEX	AGE	ORGAN/TISSUE	PROCEDURE

435-92	LABPATIENT7, ONE	0071	M	31	LYMPH NODE OF NECK	FROZEN SECTION

443-92	LABPATIENT7, TWO	0072	M	58	LARYNX	FROZEN SECTION

PIRIFORM RECESS	FROZEN SECTION

-----------------------------------------------------------------------------

MAR 19, 1992 07:05 SURGICAL PATHOLOGY SEARCH(JAN 01, 1992=&gt;Mar 19, 1992) Pg 3

# =  patient

SNOMED TOPOGRAPHY CODE: ALL --	SNOMED PROCEDURE CODE: 3081 or 3082-

-----------------------------------------------------------------------------

RESULT OF SURGICAL PATHOLOGY SEARCH:

PATIENTS WITHIN PERIOD SEARCHED: 33

SURGICAL PATHOLOGY ACCESSIONS WITHIN PERIOD SEARCHED: 33

2 OF 33 PATIENTS (6.06%)

2 OF 38 SNOMED CODE ALL SPECIMENS (5.26%)

38 ORGAN/TISSUE SPECIMENS WITHIN PERIOD SEARCHED

(SNOMED TOPOGRAPHY CODE ALL IS 100.00%)

-----------------------------------------------------------------------------
	MEDICAL RECORD :			SURGICAL PATHOLOGY		Pg 1
-----------------------------------------------------------------------------
Submitted by: LABPROVIDER, SEVEN		Date obtained: JAN 26, 1992
-----------------------------------------------------------------------------
Specimen: (Received JAN 26, 1992)
1. RT. NECK NODE

2. RT NECK NODE.

-----------------------------------------------------------------------------
Brief Clinical History:
-----------------------------------------------------------------------------
Preoperative Diagnosis:
-----------------------------------------------------------------------------
Operative Findings:
-----------------------------------------------------------------------------
Postoperative Diagnosis:
				Surgeon/physician: LABPROVIDER, SEVEN
=============================================================================
				   PATHOLOGY REPORT
Laboratory: R5ISC					Accession No. S92 435
-----------------------------------------------------------------------------

Gross description:	   Pathology Resident: LABRPOVIDER4, FIVE

	1. Specimen previously submitted for frozen section FS DIAGNOSIS:

Malignant undifferentiated tumor consists of two irregular necrotic

soft to firm lymphoid tissue pieces altogether measuring 2.5 x 2 x 1.5 cm.

All embedded. Specimen were sent for flow cytometry, electronmicroscopy

and immuno staining.

2. Specimen is similar measuring 4 x 3 x 2.5 cm. This is an enlarged 	lymph node, firm which on cut section shows a fish-flesh surfaces.

Representative sections are embedded.

1. FS DIAGNOSIS: Malignant undifferentiated tumor

Microscopic description/diagnosis:
	DIAGNOSIS BASED ON LIGHT AND ELECTRON MICROSCOPY (EM9-45) AND

IMMUNOSTUDIES: Undifferentiated, non Burkitt's type (high grade diffuse

lymphoma) IgM lambda positive, involving right and left neck lymph nodes.

LABPROVIDER4, SIX, hematopathologist, , concurs with the

diagnosis.

-----------------------------------------------------------------------------

(End of report)
LABPROVIDER, SEVEN					rg: Date MAR 17,.1992
-----------------------------------------------------------------------------
LABPATIENT7, ONE0071			   SURGICAL PATHOLOGY Report
ID:000-00-0071 SEX:M DOB:5/8/59 AGE: 31 LOC: 1A
						LABPROVIDER, SEVEN

##### Print path gross/micr/dx/fr.sect modifications [LRAPQAM]

Use this option to print path reports that have modified microscopic descriptions from one date to another. The information indicates the order of the entries — the original report followed by the first modification, the second modification, etc.

**NOTE:** The Print Path Micro Modifications [LRAPQAM] option has been **modified** to include ‘Supplementary Report’ changes with the release of patch LR*5.2*248. Use the [LRAPQAM] option to print ‘Surgical Pathology Reports’ that have microscopic descriptions and/or ‘Supplementary’ reports modified from one date to another.

##### Example: ‘Surgical Pathology Report’

Select Anatomic pathology Option: **S** Supervisor, anat path

Select Supervisor, anat path Option: **QA** AP quality assurance reports

Select AP quality assurance reports Option: **MM** Print path micro modifications

Select ANATOMIC PATHOLOGY Section: **SP** SURGICAL PATHOLOGY

Start with Date TODAY// **6/1/90** (JUN 01, 1990)

Go   to    Date TODAY/ **6/30/90** (JUN 30, 1990)

Select Print Device: *[Enter Print Device Here]*

##### Example: ‘Surgical Pathology’ report continued

-----------------------------------------------------------------------------
	MEDICAL RECORD :			SURGICAL PATHOLOGY		Pg 1
-----------------------------------------------------------------------------Submitted by: LABUSER, FIVE			Date obtained: JUN 5, 1990
-----------------------------------------------------------------------------
Specimen: (Received JUN 6, 1990)
RECTAL Bx.

-----------------------------------------------------------------------------
Brief Clinical History:
	Hx of ACUTE DIARRHEA.
-----------------------------------------------------------------------------
Preoperative Diagnosis:
	DIARRHEA
-----------------------------------------------------------------------------
Operative Findings:

SESSILE POLYP 4MM SIZE AT 15 CM - BX DONE.
-----------------------------------------------------------------------------
Postoperative Diagnosis:

S/A
					Surgeon/physician: 
=============================================================================
							   PATHOLOGY REPORT
Laboratory: Hines VAMC					Accession No. S90 3017
-----------------------------------------------------------------------------
Gross description:

A particle of soft grayish white tissue that measures 0.3 cm in diameter.

All embedded.

Microscopic description/diagnosis:

*** MODIFIED REPORT ***

(Last modified: JUN 21, 1990 09:17 typed by RENC,NORMA)

Date modified: JUN 21, 1990 09:17 typed by RENC,NORMA

Small hyperplastic polyp.

-----------------------------------------------------------------------------

Small adenomatous polyp.

-----------------------------------------------------------------------------

(See next page)

LABPROVIDER4, SEVEN		     nr : Date JUN 7, 1990

-----------------------------------------------------------------------------
LABPATIENT7, THREE		  SURGICAL PATHOLOGY Report
ID:000-00-0067 SEX:M DOB:7/14/19 AGE: 73 LOC: MHC
							LABPROVIDER, SEVEN

##### Malignancy Review [LRAPQAMR]

As detailed in M-2, Part VI, Chapter 2, entitled “Surgical Pathology and Cytology Services” dated July 10, 1989, all cases involving soft tissue, bone, muscle, or gynecological tissue should be reviewed by a second pathologist. While it is possible to do individual searches of several morphology codes, this option both simplifies and expedites the process. Cases are identified by topography; (i.e., soft tissue and bone/muscle (T1) or gynecological (T8), and include all SNOMED morphology codes beginning with 8 and 9 and ending in 1, 2, 3, 6, or 9).

The report generated includes the data obtained from the search — alphabetical listing by patient followed by the listing by accession number and the calculations, a copy of the final report for each accession identified, and a cum path data summary, if requested.

This option can also be used to generate listings of cases and final reports for quality assurance studies being performed by other clinical services.

**HINT:** By including the cum path data summary as well as the final report for the accessions, it is possible to identify which cases involved new malignancies, thus requiring documentation of physician notification.

**Example 1:** Listing of all Bone and Soft Tissue Malignancies for Surgical Pathology Case Reviews

Select Supervisor, anat path Option: **QA** AP quality assurance reports

Select AP quality assurance reports Option: **MR** Malignancy review

Select ANATOMIC PATHOLOGY Section: **SP** SURGICAL PATHOLOGY

Malignancy review

This report may take a while and should be queued to print at non-peak hours.

OK to continue ? NO// **Y** (YES)

Do you want corresponding permanent pathology reports **&lt;-** *[New]*

to print following search ? NO// **Y** (YES)

Include suspicious for malignancy cases? YES// **&lt;Enter&gt;**

1. Bone and soft tissue

2. Female genital tract

3. Other topography

Select 1, 2, or 3: **1**

Do you want corresponding permanent pathology reports

to print following search ? NO// **&lt;Enter&gt;** (NO)

Start with Date TODAY// **11-1-89** (NOV 01, 1989)

Go  to   Date TODAY// **11-30-89** (NOV 30, 1989)

Select Print Device: *[Enter Print Device Here]*

DEC 27, 1989 07:05 		VAMC

SURGICAL PATHOLOGY SEARCH(NOV 1, 1989=&gt;NOV 30, 1989)          Pg: 1

# =  patient

SNOMED TOPOGRAPHY CODE: 1-----	SNOMED MORPHOLOGY CODE: MALIGNANT-

-----------------------------------------------------------------------------

NAME	ID	SEX	AGE	ACC #	ORGAN/TISSUE	MORPHOLOGY

LABPATIENT7, ONE	0071	M	31	435-89	VERTEBRA	CARCINOMA, METASTATIC

LABPATIENT7, TWO	0072	M	58	443-89	KNEE JOINT	CARCINOMA, METASTATIC

-----------------------------------------------------------------------------

DEC 27, 1989 07:05 		 VAMC

SURGICAL PATHOLOGY SEARCH(NOV 1, 1989=&gt;NOV 30, 1989)          Pg: 1

# =  patient

SNOMED TOPOGRAPHY CODE: 1-----	SNOMED MORPHOLOGY CODE: MALIGNANT-

-----------------------------------------------------------------------------

ACC #	NAME	ID	SEX	AGE	MO/DA	ORGAN/TISSUE	MORPHOLOGY

443-89	LABPATIENT7, TWO	0072	M	58	11/01	KNEE JOINT	CARCINOMA,MET

435-89	LABPATIENT7, ONE	0071	M	31	11/28	VERTEBRA	CARCINOMA,MET

-----------------------------------------------------------------------------

DEC 27, 1989 07:05 		VAMC

SURGICAL PATHOLOGY SEARCH(NOV 1, 1989=&gt;NOV 30, 1989)           Pg: 1

# =  patient

SNOMED TOPOGRAPHY CODE: 1-----	SNOMED MORPHOLOGY CODE: MALIGNANT-

-----------------------------------------------------------------------------

RESULT OF SURGICAL PATHOLOGY SEARCH:

PATIENTS WITHIN PERIOD SEARCHED: 482

SURGICAL PATHOLOGY ACCESSIONS WITHIN PERIOD SEARCHED: 482

2 OF	 482 PATIENTS( 0.41%)

2 OF	 34 SNOMED CODE 1  SPECIMENS (5.88%)

539 ORGAN/TISSUE SPECIMENS WITHIN PERIOD SEARCHED

(SNOMED TOPOGRAPHY CODE 1 IS 6.31%)

**NOTE:** The final reports and cum path data summaries for these two patients would be included following this page.

**Example 2:** Listing of lung malignancies for correlation of surgical pathology diagnoses with that of diagnostic radiology

Select Anatomic pathology Option: **S** Supervisor, anat path

Select Supervisor, anat path Option: **QA** AP quality assurance reports

Select AP quality assurance reports Option: **MR** Malignancy review

Select ANATOMIC PATHOLOGY Section: **SU** RGICAL PATHOLOGY

Malignancy review

This report may take a while and should be queued to print at non-peak hours.

OK to continue ? NO// **Y** (YES)

Do you want corresponding permanent pathology reports **&lt;-** *[New]*

to print following search ? NO// **Y** (YES)

**NOTE:** If the ANATOMIC PATHOLOGY section is CYTOPATHOLOGY, the following prompt appears: “Include suspicious for malignancy cases ? YES//”

Include suspicious for malignancy cases? YES// **&lt;Enter&gt;**

1. Bone and soft tissue

2. Female genital tract

3. Other topography

Select 1, 2, or 3: **3**

TOPOGRAPHY (Organ/Tissue)

Select 1 or more characters of the code

For all sites type 'ALL' : **28**

Do you want corresponding permanent pathology reports

to print following search ? NO// **&lt;Enter&gt;** (NO)

Start with Date TODAY// **11-1-89** (NOV 01, 1989)

Go  to   Date TODAY// **11-30-89** (NOV 30, 1989)

Select Print Device: *[Enter Print Device Here]*

**NOTE:** The report is not included, as the format is identical to that in Example 1.

##### QA Outcome Review Cases [LRAPQOR]

If the outcome of the quality assurance review is entered using the QA Codes Enter/Edit [LRAPQACD] option, the results can be retrieved in a variety of formats, depending on how the prompts are answered.

The report can sort by accession number, by QA code and pathologist or by QA code only. It is also possible to print only specific QA codes.

For the Autopsy area, the data for the inpatient death and the % autopsies by clinical service and treating specialty is also included.

**Example 1:** Listing of surgical path cases reviewed by QA code and pathologist

Select AP quality assurance Option: **QA** outcome review cases

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

Start with Date TODAY// **5-1-90** (MAY 01, 1990)

Go  to  Date TODAY// **5-31-90** (MAY 31, 1990)

Sort by QA CODE and PATHOLOGIST ? NO// **Y** (YES)

Sort by QA CODE only ? NO// **&lt;Enter&gt;**

Select Print Device: *[Enter Print Device Here]*

SEP 17, 1990 07:33     VAMC                   Pg:1

QA CODES FOR SURGICAL PATHOLOGY From: MAY 1, 1990 To: MAY 31, 1990

Acc #	Rec’d

-----------------------------------------------------------------------------

Pathologist: LABPROVIDER4, EIGHT

F1  FROZEN SECTION- QA review-no disagreement

2355	05/01/90

2430	05/07/90

Number of cases:	2

R2  RANDOM QA REVIEW-minor disagreement (no Dx or Rx change)

Number of cases: 1

2433	05/07/90

Number of cases:	1

R3  RANDOM QA REVIEW-major disagreement (Dx or Rx change)

2456	05/01/90

Number of cases:	1

Total cases:		4

Pathologist: LABPROVIDER4, NINE.

F1  FROZEN SECTION- QA review-no disagreement

2423	05/04/90

2488	05/09/90

Number of cases:	2

Total cases:		2

Pathologist: LABPROVIDER4, TEN

M1  MALIGNANCY QA REVIEW- minor disagreement (no Dx or Rx change)

2559	05/11/90

Number of cases:	2

Total cases:		2

Pathologist: LABPROVIDER5, ONE

F1  FROZEN SECTION- QA review-no disagreement

2338	05/01/90

Number of cases:	2

Total cases:		2

Pathologist: LABPROVIDER5, ONE

M1  MALIGNANCY QA REVIEW- minor disagreement (no Dx or Rx change)

2637	05/16/90		Number of cases: 		2

**Example 2:** Listing of Autopsy Cases by QA Code Only

Select AP quality assurance Option: **QA** outcome review cases

Select ANATOMIC PATHOLOGY section: **AU** AUTOPSY

Start with Date TODAY// **10-1-91** (OCT 01, 1991)

Go  to  Date TODAY// **10-31-91** (OCT 31, 1991)

Sort by QA CODE / PATHOLOGIST ? NO// **Y** (YES)

Sort by QA CODE only ? NO// **Y** (YES)

Select Print Device: *[Enter Print Device Here]*

DEC 3, 1992 11:57  VAMC                 Pg: 1

QA CODES for AUTOPSY From: OCT 1, 1991 To: OCT 31, 1991

Acc #   Date   Pathologist

-------------------------------------------------------------------------------

A1  AU PRE/POSTMORTEM CORRELATION - Diagnosis confirmed/verified

122    10/21/91 LABPROVIDER, THREE

128    10/31/91 LABPROVIDER5, TWO

Total QA Codes: 2

A4  AU PRE/POSTMORTEM CORRELATION - major unsuspected/additional Dx

115    10/11/91 LABPROVIDER, THREE

126    10/25/91 LABPROVIDER, THREE

Total QA Codes: 2

D1  DEATH CLINICAL FACTORS- unremitting course of disease

122    10/21/91 LABPROVIDER, THREE

128    10/31/91 LABPROVIDER5, TWO

Total QA Codes: 2

D3  DEATH CLINICAL FACTORS- complication or therapeutic proc.

126    10/25/91 LABPROVIDER, THREE

Total QA Codes: 1

D4  DEATH CLINICAL FACTORS- unrecognized diagnosis w/ premortem evidence

115    10/11/91 LABPROVIDER, THREE

126    10/25/91 LABPROVIDER, THREE

Total QA Codes: 2

D8  DEATH - NO PRONOUNCEMENT DOCUMENTED

124    10/23/91 LABPROVIDER5, THREE

128    10/31/91 LABPROVIDER5, TWO

Total QA Codes: 2

Total cases reviewed: 5

DEC 3, 1992 11:57  VAMC                      Pg: 2

QA CODES by SERVICE, TREATING SPECIALTY and CLINICIAN

From OCT 1, 1991 To OCT 31, 1991

-------------------------------------------------------------------------------

A1  AU PRE/POSTMORTEM CORRELATION - Diagnosis confirmed/verified

SERVICE: MEDICINE

TREATING SPECIALTY: HEMATOLOGY/ONCOLOGY

CLINICIAN: LABPROVIDER5, FOUR

Autopsy: 128 Date: 10/31/91

TREATING SPECIALTY: INFECTIOUS DISEASE

CLINICIAN: LABPROVIDER5, FIVE

Autopsy: 122 Date: 10/21/91

Total QA Codes for A1: 2

A4  AU PRE/POSTMORTEM CORRELATION - major unsuspected/additional Dx

SERVICE: MEDICINE

TREATING SPECIALTY: GASTROINTESTINAL

CLINICIAN: LABPROVIDER5, SIX

Autopsy: 126 Date: 10/25/91

TREATING SPECIALTY: PULMONARY

CLINICIAN: ?

Autopsy: 115 Date: 10/11/91

Total QA Codes for A4: 2

D1  DEATH CLINICAL FACTORS- unremitting course of disease

SERVICE: MEDICINE

TREATING SPECIALTY: HEMATOLOGY/ONCOLOGY

CLINICIAN: LABPROVIDER5, FOUR

Autopsy: 128 Date: 10/31/91

TREATING SPECIALTY: INFECTIOUS DISEASE

CLINICIAN: LABPROVIDER5, FIVE

Autopsy: 122 Date: 10/21/91

Total QA Codes for D1: 2

D3  DEATH CLINICAL FACTORS- complication or therapeutic proc.

SERVICE: MEDICINE

TREATING SPECIALTY: GASTROINTESTINAL

CLINICIAN: LABPROVIDER5, SIX

Autopsy: 126 Date: 10/25/91

Total QA Codes for D3: 1

D4  DEATH CLINICAL FACTORS- unrecognized diagnosis w/ premortem evidence

SERVICE: MEDICINE

TREATING SPECIALTY: GASTROINTESTINAL

CLINICIAN: LABPROVIDER5, SIX

Autopsy: 126 Date: 10/25/91

TREATING SPECIALTY: PULMONARY

CLINICIAN: ?

Autopsy: 115 Date: 10/11/91

Total QA Codes for D4: 2

D8  DEATH - NO PRONOUNCEMENT DOCUMENTED

SERVICE: MEDICINE

TREATING SPECIALTY: HEMATOLOGY/ONCOLOGY

CLINICIAN: LABPROVIDER5, FOUR

Autopsy: 128 Date: 10/31/91

TREATING SPECIALTY: INFECTIOUS DISEASE

CLINICIAN: LABPROVIDER5, FIVE

Autopsy: 124 Date: 10/23/91

Total QA Codes for D8: 2

DEC 3, 1992 11:58  VAMC                     Pg: 3

AUTOPSY DATA REVIEW (OCT 1, 1991-OCT 31, 1991)

|----------In-patient-------------|

Treating Specialty         | #Deaths #Autopsies  Autopsy% |

-------------------------------------------------------------------------------

45  	14   	31.1

CARDIOLOGY           	4

CCU                 	2

ENDOCRINE           	3   	1    	33.3

EXTENDED CARE       	3  	1    	33.3

GASTROINTESTINAL     	3  	2    	66.7

GENERAL SURGERY     	1

HEMATOLOGY/ONCOLOGY	9  	1    	11.1

INFECTIOUS DISEASE     	4 	2    	50.0

INTERMEDIATE CARE      	3

MICU                 	1

ORTHOPEDIC            	1  	1    	100.0

PERIPHERAL VASCULAR  	1

PULMONARY          	4 	4    	100.0

RENAL               	3

RICU                 	2  	2    	100.0

SICU               	1

Select AP quality assurance Option: **&lt;Enter&gt;**

##### 10% Random Case Review, Surg Path [LRAPQAR]

As detailed in M-2, Part VI, Chapter 2, entitled “Surgical Pathology and Cytology Services,” dated July 10, 1989 random case review of cases is required. However, the specific formula detailed makes selection of cases based on topography codes difficult. This option searches the topographies entered for the time specified, then randomly selects 10% of the cases for each topography to be included on the report. All SNOMED morphology codes are included in the case selection.

The report generated includes:

1. a summary of the topography counts,
2. a copy of the final report for each accession identified, and
3. a listing of the cases identified (in the same format as that for the log in book).

For those facilities in which a 10% sample would exceed the 300 case per annum (25 case per month) maximum, the listing will expedite selection of cases, since all of the topography, morphology, and procedure codes are included.

**NOTE:** Since the case selection is random, reprinting the report will not provide the same listing of cases.

Example:

Select AP quality assurance Option: **RR** 10% random case review, surg path

10% Surgical Pathology Review

This report may take a while and should be queued to print at

non-peak hours.

OK to continue ? NO// **Y** (YES)

Do you want corresponding permanent pathology reports *[New]*

to print following search ? NO// **&lt;Enter&gt;** (NO)

Start with Date TODAY// **&lt;Enter&gt;** MAR 19, 1992

Go  to  Date TODAY// **1 1 91** (JAN 01, 1991)

Select Print Device: *[Enter Print Device Here]*

MAR 19, 1992 12:56  VAMC                 Pg: 1

10% Surgical Pathology Review from JAN 1, 1991 to MAR 19, 1992

-----------------------------------------------------------------

Total accessions:     22

Topography 0:  12

Topography 2:  1

Topography 5:  2

Topography 6:  5

Topography X:  1

Topography Y:  1

Accessions for review:   6 (25.00%)

MAR 19, 1992 12:56  VAMC                Pg: 1

10% Surgical Pathology Review from JAN 1, 1991 to MAR 19, 1992

ACC #   NAME                SSN

-----------------------------------------------------------------

5-91 LABPATIENT7, FOUR          000-00-0074

LIVER

CIRRHOSIS, MICRONODULAR

-----------------------------------------------------------------

7-91 LABPATIENT7, FIVE          000-00-0075

APPENDIX

INFLAMMATION, ACUTE FIBRINOUS

SKIN

POLYP, FIBROEPITHELIAL

-----------------------------------------------------------------

1-92 LABPATIENT7, SIX           000-00-0076

RIGHT LUNG

CARCINOMA, SQ CELL

INFLAMMATION, GRANULOMATOUS

-----------------------------------------------------------------

5-92 LABPATIENT, EIGHT          000-00-0008

LYMPH NODE OF NECK

HODGKIN’S DISEASE, NODULAR SCLEROSIS

-----------------------------------------------------------------

6-92 LABPATIENT7, SEVEN          000-00-0077

SKIN OF FACE

WOUND, ABRADED

TOE

WOUND, CONTUSED

AUDITORY CANAL, OSSEOUS PORTION

INSPISSATED CERUMEN

-----------------------------------------------------------------

10-92 LABPATIENT7, EIGHT          000-00-0078

APPENDIX

ACUTE INFLAMMATION

-----------------------------------------------------------------

##### Edit QA Site Parameters [LRAPQASP]

Surgical case review is a JCAHO-mandated medical staff monitoring function. In most, if not all, facilities, this function is performed by the Tissue Committee. Cases for review are selected based on correlation of preoperative and postoperative diagnoses. If the pathologist is actively involved in this evaluation, a TC code can be assigned at the time the final diagnosis is made. This code can be entered into the system and later used for selecting cases, using the Tissue Committee Review Cases option.

If the field is set to include the “TC Code” prompt in the edit template for the Microscopic/Gross Review and Gross Review/ Microscopic/SNOMED Coding options, the user will be required to enter data, since the field is mandatory.

Example:

Select AP quality assurance reports Option: **SP** Edit QA site parameters

Select LAB SECTION PRINT NAME: **SP** SURGICAL PATHOLOGY

ASK TC CODES: YES// **&lt;Enter&gt;**

**NOTE:** At the “ASK TC CODES: YES” prompt, enter “Y” for yes to have the “TC code” prompt appear in the data entry edit template. “N” for no.

##### Tissue Committee Review Cases [LRAPQAT]

Surgical case review is a JCAHO mandated medical staff monitoring function. In most, if not all, facilities, this function is performed by the Tissue Committee.

Cases for review are selected based on correlation of preoperative and postoperative diagnoses. At the time the pathologist issues the report, a QA Code can be assigned. This code is then entered during data entry of the microscopic description and SNOMED coding if the prompt “ASK TC Code” is set to “YES” using the Edit QA Site Parameters or the Edit Pathology Reports Parameters options. Assignment of a free text description to the numeric code is then done by entering the description in the LAB DESCRIPTIONS file (#62.5) and specifying “APSURG” as the screen. If a facility chooses not to have a preset description displayed as a default, no entry is necessary in the LAB DESCRIPTIONS file (#62.5).

By allowing the TC codes to be included on the report to be specified, additional flexibility has been provided. In the report shown in the example, TC Codes were not included since these are cases in which the expected pathology was found.

The listing of cases by TC Code is followed by statistical information on the number of accessions, and number and percentage for each code. Additional information is then provided for each case on the list, including:

1. An expanded version of the “Cum path data summary” which also incorporates admitting/discharge information and ICD-CM codes from the PATIENT TREATMENT file.

**NOTE: With the implementation of LR*5.2*442, a report may contain up to twenty-five each ICD-10 diagnosis or procedure codes for a given patient record.**

2.	The final report for the accession number listed.

These have been included to expedite review of the cases by the committee members and minimize the impact on the pathology office.

Although it is less common, TC codes can also be assigned to accessions from other areas if desired. This can either be done for only specific cases using the QA Codes Entry/Edit [LRAPQACD] option or for all cases if the ASK TC codes are turned on for that area.

Example 1:

Select Anatomic pathology Option: **S** Supervisor, anat path

Select Supervisor, anat path Option: **QA** AP quality assurance reports

Select AP quality assurance reports Option: **TC** Tissue committee review cases

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

TC CODE SEARCH

This report may take a while and should be queued to print at non-peak hours.

OK to continue ? NO// **Y** (YES)

Select a number from 0 to 9 (Choice# 1): **1** (1)

ENTER IDENTIFYING COMMENT: 1// **TISSUE AS EXPECTED**

Select a number from 0 to 9 (Choice# 2): **&lt;Enter&gt;**

Start with Date TODAY// **&lt;Enter&gt;** MAR 19, 1992

Go  to  Date TODAY// **1 1** (JAN 01, 1992)

Also print cumulative path data summaries ? NO// **&lt;Enter&gt;** (NO)

Select Print Device: *[Enter Print Device Here]*

MAR 19, 1992 13:02  VAMC                 Pg: 1

TC Code Search from JAN 1, 1992 to MAR 19, 1992

Patient                 SSN    Acc#   Date

----------------------------------------------------------------------

TC Code: 1 TISSUE AS EXPECTED

LABPATIENT7, NINE         000-00-0079    9 MAR 7, 1992

LABPATIENT2, TEN          000-00-0210    2 JAN 7, 1992

LABPATIENT7, SIX          000-00-0076    1 JAN 7, 1992

LABPATIENT, EIGHT         000-00-0008    4 JAN 7, 1992

LABPATIENT, EIGHT         000-00-0008    5 JAN 8, 1992

LABPATIENT7, TEN          000-00-0710    3 JAN 7, 1992

LABPATIENT7, EIGHT         000-00-0078    10 MAR 7, 1992

LABPATIENT8, ONE          000-00-0081    7 JAN 13, 1992

LABPATIENT7, SEVEN         000-00-0077    6 JAN 13, 1992

TC Code: NONE

LABPATIENT, SIX          00-00-0006    8 JAN 14, 1992

LABPATIENT6, ONE          00-00-0061    11 MAR 8, 1992

MAR 19, 1992 13:02  VAMC                 Pg: 2

TC Code Search from JAN 1, 1992 to MAR 19, 1992

Patient                 SSN    Acc#   Date

----------------------------------------------------------------------

TC Code: NONE

LABPATIENT8, TWO.        000-00-0082   12 MAR 8, 1992

LABPATIENT8, THREE        000-00-0083   13 MAR 8, 1992

LABPATIENT8, FOUR        000-42-0084   14 MAR 8, 1992

MAR 19, 1992 13:02  VAMC                 Pg: 3

TC Code Search from JAN 1, 1992 to MAR 19, 1992

----------------------------------------------------------------------

TC Code  Count   % of Accessions

1      9     64.29

NONE    5     35.71

-----

Total         14

TC Code: 1 TISSUE AS EXPECTED

**Example 2:** Cytopathology

ANATOMIC PATHOLOGY MENU

Select Anatomic pathology Option: **S** Supervisor, anat path

Select Supervisor, anat path Option: **AP** quality assurance

Select AP quality assurance Option: **Tissue** committee review cases

Select ANATOMIC PATHOLOGY section: CYTOPATHOLOGY

TC CODE SEARCH

This report may take a while and should be queued to print at non-peak

hours.

OK to continue ? NO// **Y** (YES)

Select a number from 0 to 9 (Choice# 1): **1** (1)

ENTER IDENTIFYING COMMENT: 1// **&lt;Enter&gt;** NO PROBLEM

Select a number from 0 to 9 (Choice# 2): **&lt;Enter&gt;**

Start with Date TODAY// **&lt;Enter&gt;** MAR 26, 1992

Go  to  Date TODAY// **1 1** (JAN 01, 1992)

Also print cumulative path data summaries ? NO// **&lt;Enter&gt;** (NO)

Select Print Device: *[Enter Print Device Here]*

MAR 26, 1992 19:20  VAMC                     Pg: 1

TC Code Search from JAN 1, 1992 to MAR 26, 1992

Patient                 SSN    Acc#   Date obtained

--------------------------------------------------------------------------

TC Code: 1 NO PROBLEM

LABPATIENT8, TEN        000000810     1   JAN 9, 1992

TC Code: NONE

MAR 26, 1992 19:20  DALLAS-ISC                 Pg: 2

TC Code Search from JAN 1, 1992 to MAR 26, 1992

--------------------------------------------------------------------------

TC Code  Count   % of Accessions

1      1     100.00

NONE    0      0.00

-----

Total          1

TC Code: 1 NO PROBLEM

TC Code: NONE

**Example 3:** Electron Microscopy

Select Anatomic pathology Option: **S** Supervisor, anat path

Select Supervisor, anat path Option: **QA** AP quality assurance

Select AP quality assurance Option: **Tissue** committee review cases

Select ANATOMIC PATHOLOGY section: EM

TC CODE SEARCH

This report may take a while and should be queued to print at non-peak

hours.

OK to continue ? NO// **Y** (YES)

Select a number from 0 to 9 (Choice# 1): **1** (1)

ENTER IDENTIFYING COMMENT: 1// **&lt;Enter&gt;** NO PROBLEM

Select a number from 0 to 9 (Choice# 2): **&lt;Enter&gt;**

Start with Date TODAY// **&lt;Enter&gt;** MAR 26, 1992

Go  to  Date TODAY// **1 1** (JAN 01, 1992)

Also print cumulative path data summaries ? NO// **&lt;Enter&gt;** (NO)

Select Print Device: *[Enter Print Device Here]*

MAR 26, 1992 19:26  VAMC                     Pg: 1

TC Code Search from JAN 1, 1992 to MAR 26, 1992

Patient                 SSN    Acc#   Date obtained

--------------------------------------------------------------------------

TC Code: 1 NO PROBLEM

LABPATIENT, EIGHT          000000008     1   JAN 8, 1992

##### Anatomic Pathology Turnaround Time [LRAPTT]

To effectively monitor the laboratory portion of the turnaround time (TAT), a comparison is made of the REPORT RELEASE DATE with the DATE RECEIVED to calculate the number of “days in lab.” A check is done of the dates involved, to ensure exclusion of holidays and weekends. If REPORT RELEASE DATE has a date entered, that date will be used in the calculation of turnaround time for all areas except Autopsy. For autopsies, the TAT can be calculated for either the PAD (based on the PROVISIONAL AP DIAGNOSIS DATE) or the FAD (based on the DATE AUTOPSY REPORT COMPLETED).

Turnaround time reports generated for each accession area may include either all cases for the period requested, or only cases exceeding a specified time for the period requested.

If the TAT reports are to include only the exceptions, flexibility is provided for each site to designate the acceptable time each time the report is generated. In addition to the list of the cases exceeding the time specified, the report provides:

1. count of accessions
2. average TAT for the completed cases
3. number and % of cases exceeding the limit
4. the number of incomplete cases not included in the calculations

If the cases analyzed are from sources other than the Patient file, totals and calculations are included for the Patient file and the referral file separately.

In those cases in which the % of cases exceeding the limit is unacceptable, reprinting the same report using different limits may be valuable in investigating and reviewing the data.

**Example 1:** Surgical Pathology

Select QA quality assurance reports Option: **TT** Anatomic pathology turnaround time

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY 
Start with Date TODAY// **9-1-94** (SEP 01, 1994)
Go  to   Date TODAY// **1-1-94** (JAN 01, 1994)

Identify cases exceeding turnaround time limit ? NO// **Y** (YES)

Enter limit in days: 10

Select Print Device: *[Enter Print Device Here]*

**NOTE:** At the “Identify cases exceeding turn around time limit ? NO//” prompt enter “YES” to include only those cases exceeding a specified time limit. Enter **&lt;Enter&gt;** to include all cases.

SEP 9, 1994 10:02   ISC, VERIFICATION ACCT          Pg: 1

Turnaround time for SURGICAL PATHOLOGY (Exceeding 20 days)

From: JAN 1, 1994 To: SEP 9, 1994           Lab work

Acc # Rec'd   Entry        ID Typist Released Days Pathologist

-----------------------------------------------------------------------------

1  08/10/94 LABPATIENT3, EIGHT     0114P ec  LABPROVIDER5, SEVEN

If '#', '*' or '?' is after Acc # then demographic data is in file indicated:

# = Referral file * = Research file ? = Other file listed below

Total cases: 17

Incomplete cases: 10

Complete  cases:  7

Average turnaround time (days): 2.86  Cases exceeding limit: 4 (57.14%)

Total PATIENT file cases: 14

Incomplete cases:  7

Complete  cases:  7

Average turnaround time (days): 2.86  Cases exceeding limit: 4 (57.14%)

Total REFERRAL PATIENT file cases: 2

Incomplete cases:  2

Complete  cases:  0

Total RESEARCH file cases: 1

Incomplete cases:  1

Complete  cases:  0

**Example 2:** Autopsy Provisional Anatomical Diagnosis

Select AP quality assurance Option: **TT** Anatomic pathology turnaround time

Select ANATOMIC PATHOLOGY section: **AU** AUTOPSY

1. Turnaround time for PAD

2. Turnaround time for FAD

Select 1 or 2: **1**

Start with Date TODAY// **11-1-92** (NOV 01, 1992)

Go  to  Date TODAY// **&lt;Enter&gt;** DEC 3, 1992

Identify cases exceeding turnaround time limit ? NO// **&lt;Enter&gt;** (NO)

Select Print Device: *[Enter Print Device Here]*

DEC 3, 1992 10:30  VAMC                       Pg: 1

PAD Turnaround time for AUTOPSY

From: NOV 1, 1992 To: DEC 3, 1992           		Lab work

Acc #  Performed Entry      	ID	 Typist 	Completed 	Days 	Pathologist

-------------------------------------------------------------------------------

1 F 05/31/92 LABPATIENT8, SIX    0086  lab        COUGAR

1 F 05/11/92 LABPATIENT8, SEVEN   0087

1 F 08/24/92 LABPATIENT2, FIVE   0025  ec  08/24/92  &lt;1 PATHOLOGIST

F= FULL AUTOPSY H= HEAD ONLY T= TRUNK ONLY O=OTHER LIMITATION

Total cases: 11

Incomplete cases: 10

Complete  cases:  1

**NOTES:**

•	For the PAD, the calculation is based on the entry in the Provisional Autopsy Dx Date field (File 63, Field 14.9).

•	For the FAD, the calculation is based on the entry in the Date Autopsy Report Completed field (File 63, Field 13).

#### Move Anatomic Path [LRAPMV]

If it is necessary to transfer data associated with a specific surgical pathology accession from one file to another (e.g., REFERRAL file to PATIENT file, **or** from one patient to another within the PATIENT file) this option can be used.

This option eliminates the need to edit the global for those occurrences in which a surgical pathology accession is assigned to a patient and the error is not detected until after the report has been verified/released.

This option is locked with the LRLIAISON key because of the implications of such a data transfer.

**Example:** Accession Originally Entered on a Referral Patient who was Subsequently Admitted

ANATOMIC PATHOLOGY MENU

Select Anatomic pathology Option: **S** upervisor, anat path

Select Supervisor, anat path Option: **MV** Move anatomic path accession

Move an accession from one patient to another

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

Accession Year: 1992 ? YES// **N** (NO)

Enter YEAR: **91** ( 1991)

Move Accession Number: **8** for 1991

LABPATIENT, SIX ID: 00-00-0006

File: REFERRAL PATIENT

Move accession to

Select Patient Name: **LABPATIENT, SIX** 04-27-25   0000000006

File: PATIENT

OK TO MOVE? NO// **Y** (YES)

Move Accession Number: **8** for 1991

LABPATIENT, SIX ID: 00-00-0006

File: PATIENT

Move accession to

Select Patient Name: **LABPATIENT, SIX** 04-27-25   0000000006

File: PATIENT

No need to move accession to the same patient

#### AFIP Registries [LRAPAFIP]

This option lists the AFIP registries.

##### Prisoner of War Veterans [LRAPDPT]

Use this option to list prisoner of war veterans who have anatomic pathology specimens for the time specified.

Example:

Select AFIP registries Option: **PO** Prisoner of war veterans

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

SURGICAL PATHOLOGY SEARCH FOR PRISONER OF WAR VETERANS

Start with Date TODAY// **1/2/94** (JAN 02, 1994)

Go  to  Date TODAY// **&lt;Enter&gt;** (APR 6, 1994)

Select Print Device: *[Enter Print Device Here]*

APR 6, 1994 08:28  VAMC                        Pg: 1

LABORATORY SERVICE  SURGICAL PATHOLOGY POW VETERANS

From: JAN 2, 1994 to APR 6, 1994

Patient                 DOB         ID

-----------------------------------------------------------------------------

LABPATIENT1, TWO             JUN 18, 1962    000-00-0012

POW PERIOD WORLD WAR II -

Specimen date: 02/01/94         Accession number: 4

-----------------------------------------------------------------------------

LABPATIENT1, THREE           APR 27, 1925     000-00-0013

POW PERIOD KOREAN

Specimen date: 03/31/94         Accession number: 17

Specimen date: 03/18/94         Accession number: 14

Specimen date: 02/24/94         Accession number: 6

-----------------------------------------------------------------------------

##### Veterans [LRAPPG]

Use this option to list veterans who served in the  with pathology specimens.

Example:

Select AFIP registries Option: **PG** Persian gulf veterans

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

Start with Date TODAY// **2/1/94** (FEB 01, 1994)

Go  to  Date TODAY// **&lt;Enter&gt;** APR 6, 1994

Select Print Device: *[Enter Print Device Here]*

APR 6, 1994 08:25  VAMC                       Pg: 1

LABORATORY SERVICE  SURGICAL PATHOLOGY PERSIAN GULF WAR

From: FEB 1, 1994 to APR 6, 1994

Patient                DOB         ID

-----------------------------------------------------------------------------

LABPATIENT1, THREE           APR 27, 1925     000-00-0013

WAR

Specimen date: 03/31/94         Accession number: 17

Specimen date: 03/18/94         Accession number: 14

Specimen date: 02/24/94         Accession number: 6

-----------------------------------------------------------------------------

#### Edit Referral Patient File [LRUV]

This option allows you to edit referral patient file fields.

Example:

Select Supervisor, anat path Option: **EDIT REFERRAL** patient file

Select REFERRAL PATIENT NAME: **LABPATIENT1, THREE** 04-27-58   089485948

NAME: LABPATIENT1, THREE // **&lt;Enter&gt;**

SEX: MALE// **&lt;Enter&gt;XXXXXXXX**

DOB: 04/27/58// **&lt;Enter&gt;**

MARITAL STATUS: **&lt;Enter&gt;**

RELIGION: **&lt;Enter&gt;**

IDENTIFIER: 000000008// **&lt;Enter&gt;**

REFERRAL SOURCE: **&lt;Enter&gt;**

PROVIDER: **&lt;Enter&gt;**

STREET ADDRESS: **&lt;Enter&gt;**

STREET ADDRESS 2: **&lt;Enter&gt;**

STREET ADDRESS 3: **&lt;Enter&gt;**

CITY: **&lt;Enter&gt;**

STATE: **&lt;Enter&gt;**

ZIP CODE: **&lt;Enter&gt;**

PHONE: **&lt;Enter&gt;**

OFFICE PHONE: **&lt;Enter&gt;**

PHONE #3: **&lt;Enter&gt;**

PHONE #4: **&lt;Enter&gt;**

DATE OF DEATH: **&lt;Enter&gt;**

### Verify/Release Menu, Anat Path [LRAPVR]

#### Descriptions

**Option	Description**

Verify/Release Reports, Anat Path	Allows displaying and printing of reports after they are verified by the pathologist. **Note:** The report release prompt has been changed to a yes/no question.

Supplementary Report Release	Allows displaying and anat path printing of supplementary reports after they are verified by the pathologist.

List of Unverified Pathology Reports	Provides a list of unverified pathology reports and supplementary reports for surgical pathology, cytopathology or electron microscopy, selected by date.

#### Verify/Release Reports, Anat Path [LRAPR]

This option allows the reports to be approved for release to medical personnel on the wards with access to a CRT. Reports should **not** be released until the final report has been reviewed and signed by the pathologist. Once the report is released, persons outside the laboratory can view the information with the necessary access. The information can be extracted either by the Health Summary software or the [LRAPSPCUM], [LRAPCYCUM], [LRAPEMCUM] options in the Clinician options, anat path [LRAPMD] menu. Changes, which need to be made after the report is released, **must** be accomplished using the modified or the supplemental report options as appropriate to the change.

**NOTE:** The Verify/Release Reports, Anat Path [LRAPR] option was **modified** with the release of patch LR*5.2*248. The REPORT RELEASE DATE/TIME prompt has been changed to a YES/NO question.

**Changes to the Verify/Release Reports, Anat [LRAPR] option are indicated in the shaded areas of the following example.**

##### Example 1: Release of Surgical Report

Select Verify/release menu, anat path Option: **RR** Verify/release reports, anat path

RELEASE PATHOLOGY REPORTS

Select ANATOMIC PATHOLOGY SECTION: SUR SURGICAL PATHOLOGY

SURGICAL PATHOLOGY (SUR)

Data entry for 1994 ? YES// **&lt;Enter&gt;** (YES)

Select Accession Number/Pt name: **7** for 1994

LABPATIENT1, TEN ID: 000-00-0110

Release report? NO// YES **&lt;Enter&gt;**

Report released...

Select Accession Number/Pt name: **&lt;Enter&gt;**

**NOTE:** If an attempt is made to release a report that has already been released, the following is displayed.

Report released JUN 26, 1994@16:52:57 by LABPROVIDER5, EIGHT

Select Accession Number/Pt name:

**NOTE:** Once the report is released, the release information is included on the log book as shown below.

Select Print, anat path Option: **PB** Print log book

Select Log-in menu, anat path Option: **PB** Print log book

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

SURGICAL PATHOLOGY LOG BOOK

Print SNOMED codes if entered ? NO// **&lt;Enter&gt;** (NO)

Log book year: 1994 OK ? YES// **&lt;Enter&gt;** (YES)

Start with Acc #: **7**

Go  to  Acc #: LAST // **7**

Select Print Device: *[Enter Print Device Here]*

AUG 30, 1994 11:38  VAMC                       Pg: 1

SURGICAL PATHOLOGY LOG BOOK for 1994

# =Demographic data in file other than PATIENT file

Date  Num  Patient       ID  LOC   PHYSICIAN     PATHOLOGIST

-----------------------------------------------------------------------------

8/25   7 LABPATIENT1, TEN   0110 1 EAST  LABPROVIDER2, ONE;

LABPROVIDER1, FIVE

Date specimen taken:08/25/94     Entered by: LABUSER, TWO

Released by: LABUSER, SIX

**NOTES:**

At the “RELEASE REPORT” prompt, enter the Date/time the report is to be released. Once released, the name of the person releasing the report can be obtained from the logbook.

If a report is modified, it will need to be re-released. In this case, the original date/time will be stored in the appropriate Original Release Date field and this new date can be entered. This new date will not affect calculation of the turnaround time except in the case of ‘Autopsy’ reports. In that particular case, the Release Date/Time can be deleted for the Provisional Diagnosis.

In order to meet the requirements of CAP and JCAHO, no option exists to “unrelease a report” Changes in reports should be done using either the modified or supplemental reports options. In the rare event that an accession is assigned to the wrong patient and the data needs to be corrected, the Move Anatomic Path [LRAPMV] option can be used if appropriate. If not, the global will need to be edited to “unrelease” the report before anything else can be done. Editing will need to be done by someone from the IRM staff with programmer access. Once the LRDFN for the patient is ascertained, Date Report Completed field (#.03) and Release Report field (#.11) need to be deleted for Files #63.08 (SURGICAL PATHOLOGY), #63.09 (CYTOPATHOLOGY), or #63.02 (ELECTRON MICROSCOPY).

A check exists to ensure that the report has a “date completed” before allowing its release. If there is no date report completed, the user will get “BEEPED” and see the message: “No date report completed, cannot release” after selecting the Accession Number/Pt name

**NOTE:** The Verify/Release Reports, Anat Path [LRAPR] option has been **modified** with the release of patch LR*5.2*248. The “AUTOPSY RELEASE DATE/TIME” prompt has been changed to YES/NO question.

**Changes made in the Verify/Release Reports, Anat Path [LRAPR] option are indicated in the shaded areas of the following example.**

##### Example 2: Release of an ‘Autopsy’ report

Select Anatomic pathology Option: **V** Verify/release menu, anat path

Select Verify/release menu, anat path Option: **RR** Verify/release reports, anat path

RELEASE PATHOLOGY REPORTS

Select ANATOMIC PATHOLOGY SECTION: **au** AUTOPSY

Data entry for 1992 ? YES// **&lt;Enter&gt;** (YES)

Select Accession Number/Pt name: **5** for 1992

LABPATIENT, FOUR ID: 000-00-0004

Release report? NO// **YES&lt;Enter&gt;**

Report released...

Select Accession Number/Pt name: **&lt;Enter&gt;**

**NOTE:** For Autopsy, it may be necessary to unrelease a report. This occurs when a Provisional Anatomical Diagnosis was verified/released for viewing by the clinicicians but the pathologist does not want the final report accessible to the clinicians until that portion has once again been verified/released. Therefore, it must be unreleased prior to entry of the Final Anatomical Diagnosis information. Since there is no chance for adverse patient outcome, this was done prior to the release of LR*5.2*248 by using the “@” key at the “AUTOPSY RELEASE DATE/TIME” prompt. With the release of patch LR*5.2*248, this was replaced by a YES/NO question as follows:

Select Anatomic pathology Option: V Verify/release menu, anat path

RR   Verify/release reports, anat path

RS   Supplementary report release, anat path

LU   List of unverified pathology reports

Select Verify/release menu, anat path Option: RR Verify/release reports, anat path

RELEASE PATHOLOGY REPORTS

Select ANATOMIC PATHOLOGY SECTION: AU AUTOPSY

AUTOPSY (AU)

Data entry for 1992 ? YES// **&lt;Enter&gt;** (YES)

Select Accession Number/Pt name: 1 for 1992

LABPATIENT8, EIGHT ID: 000-00-0088

Report released SEP 18, 1992@13:11:20 by LABPROVIDER5, NINE

Unrelease report? NO// YES **&lt;Enter&gt;**

Report unreleased...

#### Supplementary Report Release, Anat Path [LRAPRS]

Use this option to release supplementary reports for Surgical Pathology, Cytopathology or Electron Microscopy.

Select Verify/release menu, anat path Option: **RS** Supplementary report release, anat path

RELEASE SUPPLEMENTARY PATHOLOGY REPORTS

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

Data entry for 1990 ? YES// **&lt;Enter&gt;** (YES)

Select Accession Number/Pt name: **1** for 1990

LABPATIENT8, NINE ID: 000-00-0089

Specimen(s):

SKIN

Select SUPPLEMENTARY REPORT DATE:1-7-1990@10:00:00// **&lt;Enter&gt;** JAN 7,1990 @10:00

RELEASE SUPPLEMENTARY REPORT ? NO// **Y** (YES)

Select Accession Number/Pt name: **&lt;Enter&gt;**

#### List of Unverified Pathology Reports [LRAPV]

Use this option to print or display a list of unverified pathology reports for surgical pathology, cytopathology, or electron microscopy for a specified section and time period.

**Example 1:** Surgical Path

Select Verify/release menu, anat path Option: **LU** List of unverified pathology reports

Select ANATOMIC PATHOLOGY section: **CY** CYTOPATHOLOGY

1) List of unverified SURGICAL PATHOLOGY reports

2) List of unverified SURGICAL PATHOLOGY supplementary reports

Select 1 or 2: **1**

Start with Date TODAY// **&lt;Enter&gt;**

Go  to  Date TODAY// **T-30** (AUG 09, 1990)

Select Print Device: *[Enter Print Device Here]*

SEP 9, 1990    09:29  SIUG                     Pg: 1

CYTOPATHOLOGY UNVERIFIED REPORTS

BY DATE SPECIMEN TAKEN FROM AUG 9, 1990 TO SEP 9, 1990

DATE   Accession number    Patient             SSN

-----------------------------------------------------------------------------

08/22/90   11         LABPATIENT8, TEN        000-00-0810

08/16/90   5         LABPATIENT, NINE        000-00-0008

**Example 2:** Cytopathology

Select Verify/release menu, anat path Option: **LU** List of unverified pathology reports

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

1) List of unverified SURGICAL PATHOLOGY reports

2) List of unverified SURGICAL PATHOLOGY supplementary reports

Select 1 or 2: **2**

Start with Date TODAY// **&lt;Enter&gt;** SEP 24, 1990

Go  to  Date TODAY// **&lt;Enter&gt;** SEP 24, 1990

Select Print Device: *[Enter Print Device Here]*

SEP 24, 1990 11:43  SALT  ISC            Pg: 1

SURGICAL PATHOLOGY UNVERIFIED SUPPLEMENTARY REPORTS

BY DATE SPECIMEN TAKEN FROM SEP 24, 1990 TO SEP 24, 1990

DATE    Accession number  Patient        SSN

------------------------------------------------------------------

09/24/90     7    LABPATIENT8, NINE       000-00-0089

### Clinician Options, Anat Path [LRAPMD]

#### Descriptions

**Option	Description**

Display Surg Path Reports for a Patient	Display on the screen surgical pathology reports for a selected patient if the report has been verified.

Display Cytopath Reports for a Patient	Display on the screen cytopathology reports for a selected patient if the report has been verified.

Display EM Reports for a Patient	Display on the screen EM reports for a selected patient if the report has been verified.

Enter/Edit User Defined Lab Test Lists	Create new test lists or change the name or individual tests on an existing list. These are lists created by a clinician to follow tests for specific patients. If there are no lists already created under a user’s name, he may use another user’s list.

Print/Display Preselected Lab Tests	Displays or prints user-defined lab tests and patient lists from one date to another. If tests are not defined by the user, the lab-defined list will be displayed.

Print Surgical Pathology Report for	If report results have been released,

a Patient	you may print the surgical pathology report for a patient.

Print Cytopathology Report for a Patient	If report results have been released, you may print the cytopath report for a patient.

**Option	Description**

Print Electron Microscopy Report for 	Prints an electron microscopy

a Patient	report for a patient, if results have been released.

Cum Path Data Summaries	Displays or prints the cumulative summary of surgical path, cytopath, EM, or autopsy.

Autopsy Protocol/Supplementary Report	If autopsy report is verified, prints report.

#### Display Surg Path Reports for a Patient [LRAPSPCUM]

#### Display Cytopath Reports for a Patient [LRAPCYCUM]

#### Display EM Reports for a Patient [LRAPEMCUM]

These options automatically start with a display of the most recent specimen which has been completed/released.

No “DEVICE” prompt is included in this option. Reports can be printed through Print Surgical Pathology Report for a Patient [LRAPSPSGL] or other print options.

**HINTS:**

1. Display Cytopath Reports for a Patient [LRAPCYCUM] option and Display EM Reports for a Patient [LRAPEMCUM] option work essentially the same as this option.
2. The “Date Spec Taken” listed at the top of this report has also been inserted after the “Microscopic exam/diagnosis” heading to prevent confusion if the report is more than one page in length.

Example:

Select Clinician options, anat path Option: **DS** Display surg path reports for a patient

SURGICAL PATHOLOGY PATIENT REPORT(S) DISPLAY

Select Patient Name: LABPATIENT1, TEN   02-01-22  000000110  NO  NSC VETERAN

LABPATIENT, SIX ID: 00-00-0006 Physician: LABPROVIDER5, TEN

AGE: 72 DATE OF BIRTH: FEB 1, 1922

Ward on Adm: 1 EAST Service: MEDICINE

Adm Date: APR 8, 1993 10:53 Adm DX: ACCIDENT

Present Ward: 1 EAST          MD: LABPROVIDER3, NINE

PATIENT LOCATION: 1 EAST// &lt;Enter&gt;

Is this the patient ? YES// **&lt;Enter&gt;** (YES)

Date Spec taken: AUG 25, 1994     Pathologist: LABPROVIDER1, FIVE

Date Spec rec'd: AUG 25, 1994 19:41 Resident:

Date completed: AUG 26, 1994     Accession #: 7

Submitted by: LABPROVIDER2, ONE  Practitioner: LABPROVIDER2, ONE

-----------------------------------------------------------------------------

Specimen:

LEFT LEG

CONSULTATION AFIP#12345 Date: AUG 26, 1994

This is just a consultation.

-----------------------------------------------------------------------------

SNOMED/ICD codes:

T-Y9400: LEG

Date Spec taken: AUG 25, 1994    Pathologist: LABPROVIDER2, ONE

Date Spec rec'd: AUG 25, 1994 19:36 Resident:

REPORT INCOMPLETE           Accession #: 6

Submitted by: LABPROVIDER1, FIVE    Practitioner: LABPROVIDER1, FIVE

-----------------------------------------------------------------------------

Report not verified

Date Spec taken: AUG 24, 1994     Pathologist: LABPROVIDER1, SEVEN

Date Spec rec'd: AUG 24, 1994 10:37 Resident: LABPROVIDER1, FIVE

Date completed: AUG 25, 1994     Accession #: 2

Submitted by: LABPROVIDER1, SEVEN   Practitioner: LABPROVIDER1, SEVEN

-----------------------------------------------------------------------------

Specimen:

PROSTATE CHIPS

Brief Clinical History:

Nocturia and difficulty voiding urine.

Preoperative Diagnosis:

same.

Operative Findings:

same.

Postoperative Diagnosis:

same.

Frozen Section:

Basal cell .

Gross Description:

Specimen consists of 5 grams of prostate gland tissue.

Microscopic exam/diagnosis: (Date Spec taken: AUG 24, 1994)

*** MODIFIED REPORT ***

(Last modified: AUG 27, 1994 17:30 typed by CASUGAY,ELSIE)

Glomerular basement membranes are thickenedd and there is increased

mesangial matrix. Also present are small prostatic infarts and foci of

squamous metaplasia. Another small infarts and foci of squamous metaplasia.

Supplementary Report:

Date: AUG 26, 1994 18:09 not verified

Date: AUG 26, 1994 18:10 not verified

CONSULTATION AFIP#123456789 Date: AUG 26, 1994 18:17

This is an example of a consultation sent to the AFIP.

-----------------------------------------------------------------------------

SNOMED/ICD codes:

T-18969: PROSTATIC FASCIA

P-Y333 : ADMINISTRATION OF MEDICATION, EMERGENCY

#### Edit/Print/Display Preselected Lab Tests [LRUMDA]

This option allows for user defined lab tests and patient lists for display/print from one date to another. If tests not defined by the user the lab defined list will be displayed.

Please refer to the Print Menu for examples of this menu.

#### Print Surgical Pathology Report for a Patient [LRAPSPSGL]

#### Print Cytopathology Report for a Patient [LRAPCYSGL]

#### Print Electron Microscopy Report for a Patient [LRAPEMSGL]

If report results have been released (using the option, Verify/Release Pathology Reports [LRAPR]), you may print the surgical pathology report for a patient. For reports that have several pages (End of report) will appear at the bottom of the last page, and (See next page) will appear on all preceding pages. In addition, the words “see signed copy in chart” appear above the pathologist’s name in lieu of the signature. The Print Cytopathology Report for a Patient [LRAPCYSGL] and Print Electron Microscopy Report for a Patient [LRAPEMSGL] options work essentially the same as this option.

**Example:**

Select Clinician options, anat path Option: **P**

Select Patient Name: **LABPATIENT1, FOUR** 02-01-12  0000000014

NSC VETERAN

LABPATIENT1, FOUR ID: 000-00-0014  Physician: LABPROVIDER2, EIGHT

AGE: 77 DATE OF BIRTH: FEB 1, 1912

PATIENT LOCATION: CARDIOLOGY// **&lt;Enter&gt;**

Specimen(s    Count #  Accession #  Date

( 1)    9    MAR 28, 1990 not verified

SKIN

( 2)    21    NOV 8, 1989

( 3)    20    NOV 7, 1989 not verified

SKIN

( 4)    12    AUG 1, 1989

TOENAIL

More accessions ? NO// **&lt;Enter&gt;** (NO)

Choose Count #(1-4): **2**

Accession #: 21  Date: NOV 8, 1989

Print SNOMED &amp;/or ICD codes on final report(s) ? NO// **y** (YES)

Select Print Device: *[Enter Print Device Here]*

-----------------------------------------------------------------------------

MEDICAL RECORD |       SURGICAL PATHOLOGY           Pg 1

-----------------------------------------------------------------------------

Submitted by: LABPROVIDER1, TWO      Date obtained: NOV 8, 1989

-----------------------------------------------------------------------------

Specimen (Received NOV 8, 1989 13:31):

-----------------------------------------------------------------------------

Brief Clinical History:

-----------------------------------------------------------------------------

Preoperative Diagnosis:

-----------------------------------------------------------------------------

Operative Findings:

-----------------------------------------------------------------------------

Postoperative Diagnosis:

Surgeon/physician: LABPROVIDER2, EIGHT

=============================================================================

PATHOLOGY REPORT

Laboratory: SIUG                   Accession No. SP88 21

-----------------------------------------------------------------------------

Gross description:

Skin ellipse 2x1x.3 cm

Microscopic exam/diagnosis:

Psoriasis

IMMUNOFLUORESCENCE 21-I Date: NOV 13, 1988

SKIN

This is an immunofluorescent study of the skin specimen

submitted. There is no evidence of immune deposits in the

basement membrane.

ELECTRON MICROSCOPY E-21-88 Date: NOV 13, 1989 06:27

LIVER

This is an electron microscopic study of the liver biopsy.

There are may giant mitochondria in all grids examined.

SNOMED code(s):

T-01000: skin

M-48840: psoriasis

P-1148 : biopsy, punch

T-56000: liver

M-49500: cirrhosis

-----------------------------------------------------------------------------

See signed copy in chart                   (End of report)

LABPROVIDER, ONE                      rg | Date NOV 8, 1989

-----------------------------------------------------------------------------

LABPATIENT1, FOUR             WORK COPY ONLY !!

ID:000-00-0014 SEX:M DOB:2/1/12 AGE:77 LOC:CARDIOLOGY

LABPROVIDER2, EIGHT

#### Cum Path Data Summaries [LRAPT]

Cumulative summary of surgical path, cytopath, EM, and autopsy for screen display or hard copy.

**Example 1:** Screen Display

Select Clinician options, anat path Option: **CS** Cum path data summaries

Cum path data summaries

1. DISPLAY cum path data summary for A patient

2. PRINT  cum path data summary for  patient(s)

Select (1-2): **1**

DISPLAY cum path data summary for a patient

Select Patient Name: **LABPATIENT1, THREE** 04-27-25   000000013   SC VETERAN

LABPATIENT1, THREE ID: 000-00-0013 Physician: LABPROVIDER, EIGHT

AGE: 68 DATE OF BIRTH: APR 27, 1925

PATIENT LOCATION: 1 TEST// &lt;Enter&gt;

Is this the patient ? YES// **&lt;Enter&gt;** (YES)

DUSTY,ANDY      089-48-5948    DOB: APR 27, 1925 LOC: 1 TES

-----------------------------------------------------------------------------

SURGICAL PATHOLOGY

Organ/tissue:    Date rec'd: 03/31/94   Acc #:  17

Report not verified.

Organ/tissue:    Date rec'd: 03/18/94   Acc #:  14

Report not verified.

Organ/tissue:    Date rec'd: 02/24/94   Acc #:  6

Report not verified.

Organ/tissue:    Date rec'd: 06/25/93   Acc #:  14

Report not verified.

Organ/tissue:    Date rec'd: 06/21/93   Acc #:  6

Report not verified.

Organ/tissue:    Date rec'd: 12/03/92   Acc #:  26

Report not verified.

Organ/tissue:    Date rec'd: 12/02/92   Acc #:  24

LIVER

CIRRHOSIS

Organ/tissue:    Date rec'd: 09/24/92   Acc #:  8

Report not verified.

Organ/tissue:    Date rec'd: 08/31/92   Acc #:  23

LIVER

Organ/tissue:    Date rec'd: 12/26/91   Acc #:  8

Organ/tissue:    Date rec'd: 12/26/91   Acc #:  8

LIVER

INFLAMMATION

LYMPH NODE

INFLAMMATION

ESOPHAGUS

FROZEN SECTION

INFLAMMATION

STOMACH

NORMAL TISSUE MORPHOLOGY

Organ/tissue:    Date rec'd: 04/28/91   Acc #:  2

APPENDIX

ACUTE INFLAMMATION

Organ/tissue:    Date rec'd: 04/26/91   Acc #:  1

SKIN

EXCISION, COMPLETE

BASAL CELL CARCINOMA

BONE MARROW

BIOPSY, NEEDLE

NORMAL TISSUE MORPHOLOGY

-----------------------------------------------------------------------------

CYTOPATHOLOGY

-----------------------------------------------------------------------------

CYTOPATHOLOGY

Organ/tissue:    Date rec'd: 04/11/94   Acc #:  16

Report not verified.

Organ/tissue:    Date rec'd: 03/29/94   Acc #:  10

Report not verified.

Organ/tissue:    Date rec'd: 12/01/92   Acc #:  25

Report not verified.

Organ/tissue:    Date rec'd: 04/28/92   Acc #:  19

Report not verified.

Organ/tissue:    Date rec'd: 12/17/91   Acc #:  6

SPUTUM

UNSATISFACTORY SPECIMEN

Organ/tissue:    Date rec'd: 04/26/91   Acc #:  1

SPUTUM

ACUTE INFLAMMATION

NO EVIDENCE OF MALIGNANCY

-----------------------------------------------------------------------------

ELECTRON MICROSCOPY

Organ/tissue:    Date rec'd: 12/17/91   Acc #:  1

Report not verified.

Select Patient Name: **&lt;Enter&gt;**

**Example 2:** Hard Copy

Select Clinician options, anat path Option: **CS** Cum path data summaries

Cum path data summaries

1. DISPLAY cum path data summary for A patient

2. PRINT  cum path data summary for  patient(s)

Select (1-2): **2**

Select Patient Name: **LABPATIENT9, ONE** 04-27-25   000000091   SC VETERAN

LABPATIENT9, ONE ID: 000-00-0091    Physician: LABPROVIDER, EIGHT

AGE: 68 DATE OF BIRTH: APR 27, 1925

PATIENT LOCATION: 1 TEST// **&lt;Enter&gt;**

Is this the patient ? YES// **&lt;Enter&gt;** (YES)

Another patient: ? NO// **Y** (YES)

Select Patient Name: **LABPATIENT9, TWO** 05-23-52   000000092P   NSC VETERAN

Pat Info: VERY SICK

LABPATIENT9, TWO ID: 000-00-0092P Physician: LABPROVIDER6, ONE

Infection control warning:

VERY SICK

AGE: 41 DATE OF BIRTH: MAY 23, 1952

Ward on Adm: PSYCH Service: PSYCHIATRY

Adm Date: AUG 23, 1991 07:53 Adm DX: TIRED HOUSEWIFE SYNDROM

Present Ward: PSYCH           MD: LABPROVIDER6, ONE

PATIENT LOCATION: PSYCH// &lt;Enter&gt;

Is this the patient ? YES// **&lt;Enter&gt;** (YES)

Another patient: ? NO// **N** (NO)

Select Print Device: *[Enter Print Device Here]*

APR 18, 1994 10:28 VAMC               Pg: 1

ANATOMIC PATHOLOGY

-----------------------------------------------------------------------------

LABPATIENT9, TWO        SSN:00-00-0092  PDOB:MAY 23, 1952

SURGICAL PATHOLOGY

Organ/tissue:    Date rec'd: 03/07/94   Acc #:  11

Report not verified.

Organ/tissue:    Date rec'd: 11/22/93   Acc #:  39

Report not verified.

CYTOPATHOLOGY

Organ/tissue:    Date rec'd: 02/24/94   Acc #:  2

Report not verified.

Organ/tissue:    Date rec'd: 07/17/91   Acc #:  5

SPUTUM

CARCINOMA, SQ CELL

Organ/tissue:    Date rec'd: 04/28/91   Acc #:  4

SPUTUM

UNSATISFACTORY SPECIMEN

BRONCHIAL WASHING CYTOLOGIC MATERIAL

CONSULTATION, INTERNAL

CARCINOMA, SQ CELL

BRONCHIAL BRUSHING CYTOLOGIC MATERIAL

CARCINOMA, SQ CELL

ANATOMIC PATHOLOGY

-----------------------------------------------------------------------------

LABPATIENT1, THREE          SSN:000-00-0013 DOB:APR 27, 1925

SURGICAL PATHOLOGY

Organ/tissue:    Date rec'd: 03/31/94   Acc #:  17

Report not verified.

Organ/tissue:    Date rec'd: 03/18/94   Acc #:  14

Report not verified.

Organ/tissue:    Date rec'd: 02/24/94   Acc #:  6

Report not verified.

Organ/tissue:    Date rec'd: 06/25/93   Acc #:  14

Report not verified.

Organ/tissue:    Date rec'd: 06/21/93   Acc #:  6

Report not verified.

Organ/tissue:    Date rec'd: 12/03/92   Acc #:  26

Report not verified.

Organ/tissue:    Date rec'd: 12/02/92   Acc #:  24

LIVER

CIRRHOSIS

Organ/tissue:    Date rec'd: 09/24/92   Acc #:  8

Report not verified.

Organ/tissue:    Date rec'd: 08/31/92   Acc #:  23

LIVER

Organ/tissue:    Date rec'd: 12/26/91   Acc #:  8

LIVER

INFLAMMATION

LYMPH NODE

INFLAMMATION

ESOPHAGUS

FROZEN SECTION

INFLAMMATION

STOMACH

NORMAL TISSUE MORPHOLOGY

Organ/tissue:    Date rec'd: 04/28/91   Acc #:  2

APPENDIX

ACUTE INFLAMMATION

Organ/tissue:    Date rec'd: 04/26/91   Acc #:  1

SKIN

EXCISION, COMPLETE

BASAL CELL CARCINOMA

BONE MARROW

BIOPSY, NEEDLE

NORMAL TISSUE MORPHOLOGY

APR 18, 1994 10:28  VAMC               Pg: 2

ANATOMIC PATHOLOGY

-----------------------------------------------------------------------------

LABPATIENT1, THREE          SSN:000-00-0013 DOB:APR 27, 1925

CYTOPATHOLOGY

Organ/tissue:    Date rec'd: 04/11/94   Acc #:  16

Report not verified.

Organ/tissue:    Date rec'd: 03/29/94   Acc #:  10

Report not verified.

Organ/tissue:    Date rec'd: 12/01/92   Acc #:  25

Report not verified.

Organ/tissue:    Date rec'd: 04/28/92   Acc #:  19

Report not verified.

Organ/tissue:    Date rec'd: 12/17/91   Acc #:  6

SPUTUM

UNSATISFACTORY SPECIMEN

Organ/tissue:    Date rec'd: 04/26/91   Acc #:  1

SPUTUM

ACUTE INFLAMMATION

NO EVIDENCE OF MALIGNANCY

APR 18, 1994 10:28  VAMC               Pg:  3

ANATOMIC PATHOLOGY

-----------------------------------------------------------------------------

LABPATIENT1, THREE          SSN:000-00-0013 DOB:APR 27, 1925

ELECTRON MICROSCOPY

Organ/tissue:    Date rec'd: 12/17/91   Acc #:  1

Report not verified.

#### Autopsy Protocol/Supplementary Report [LRAPAUPT]

**NOTE:** The Autopsy Protocol report [LRAPAUPT] option has been **modified** with the release of patch LR*5.2*248. The “Autopsy Protocol Reports” FOOTER has been reformatted to include new information. The final page HEADER has been reformatted for better readability.

If the autopsy report has been verified/released, it will be accessible through this option. The report content will reflect the current content of the report.

**For example:**

1. If the site enters a provisional gross anatomical diagnosis and releases the report, this will be accessible until the accession is “unreleased.”
2. If the site enters a provisional gross anatomical diagnosis and does not release the report, this will not be accessible until the accession is “released.”

Example:

Select Anatomic pathology Option: **C** Clinician options, anat path

Select Clinician options, anat path Option: **AR** Autopsy protocol or supplementary report

Select Patient Name: **LABPATIENT, FOUR** 12-18-25   000000004   NSC VETERAN

LABPATIENT, FOUR ID: 000-00-0004 Physician: LABPROVIDER, THREE

DIED DEC 1, 1992

Autopsy performed: DEC 1, 1992 Acc # 5

Select Print Device: *[Enter Print Device Here]*

##### Example: Autopsy Protocol Report

**NOTE:** The “Autopsy Protocol Report” FOOTER has been modified to include the **new** Physician and Patient labels to clearly distinguish between the patient and physician names.

**The shaded areas in the following example display changes made to the footer:**

----------------------------------------------------------------------------

CLINICAL RECORD |         AUTOPSY PROTOCOL        Pg 1

----------------------------------------------------------------------------

Date died: DEC 1, 1992         	| Autopsy date: DEC 1, 1992

Resident:             		| FULL AUTOPSY Autopsy No. A92 5

----------------------------------------------------------------------------

Clinical History

1. Left CVA 2. Recurrent UTI 3. Aspiration pneumonia

----------------------------------------------------------------------------

Anatomic Diagnoses

PROVISIONAL GROSS ANATOMIC PATHOLOGICAL DIAGNOSIS: (Subject to revision)

1. Bilateral pulmonary edema with bilateral pleural effusion (500cc)

a. Organizing pneumonia right lung

b. Pericardial effusion

c. Calcified granuloma, left upper lobe

2. a. Moderate arteriosclerosis of abdominal aorta

b. Cardiomegaly with LVH

3. Bilateral granular kidneys (arterionephrosclerosis)

a. 3 x 2 cm cyst left kidney

b. 0.3 x 0.3 cm hemorrhagic cysts, left kidney

c. Hemorrhagic bladder mucosa

4. Choletlithiasis with 25 stones (yellow, 0.5 to 1 cm)

a. Congested liver parenchyma

b. Diverticulosis, colon

----------------------------------------------------------------------------

Pathologist: LABPROVIDER, THREE         wty| Date DEC 1, 1992

----------------------------------------------------------------------------

CIOFO								AUTOPSY PROTOCOL

Patient: LABPATIENT, FOUR		000-00-0004	SEX:M		DOB:DEC 18, 1992

Bon-AHMED/OPC		Physician: LABPROVIDER6, TWO		AGE AT DEATH: 75

**NOTE:** The Autopsy Protocol/Supplementary report [LRAPAUPT] option has been **modified** with the release of patch LR*5.2*248. The “AUTOPSY PROTOCOL REPORT” final page header and footer were reformatted to allow for better readability. The report can be generated by using the [LRAPAUPT] option.

**The shaded areas in the following example display the changes made in the final page header and footer:**

DEC 2, 1992 07:49		 CIOFO						Pg:2

ANATOMIC PATHOLOGY

----------------------------------------------------------------------------

LABPATIENT, FOUR		000-00-0004		DOB:DEC 18, 1925

Acc #:5			AUTOPSY DATA	Age: 66

Date/time Died					Date/time of Autopsy

DEC 1, 1992 1700		FULL AUTOPSY	DEC 1, 1992 1801

Resident: LABPROVIDER6, NINE			Senior: LABPROVIDER, THREE

-----------------------------------------------------------------------------

Pathologist: LABPROVIDER, THREE					wty| Date DEC 2, 1992

----------------------------------------------------------------------------

CIOFO								AUTOPSY PROTOCOL

Patient: LABPATIENT, FOUR	000-00-0004		SEX:M		DOB: DEC 18, 1925

MEDICINE			Physician:	LABPROVIDER6, TWO		AGE AT DEATH: 66

### Workload, Anat Path [LRAPW]

#### Descriptions

**Option	Description**

Cytopathology Screening Workload	Records date/time cytopathology slides are screened and captures screening workload.

Display Workload for an Accession	Displays tests and WKLD codes for an accession for a date for an accession area.

EM Scanning and Photo Workload	Option allows recording workload for scanning and photography of EM grids and making of prints.

Surg Path Gross Assistance Workload	Use this option to record workload for gross description and cutting of surgical tissue by a non-physician.

#### Cytopathology Screening Workload [LRAPWR]

This option is used to enter the workload for screening by the cytotechnologist. (If this is not done by a cytotech, but is done by the pathologist, no workload should be tallied.)

The date/time entered for screening must be later than the staining date/time. If the staining date/time has not been entered yet, the information for screening cannot be entered.

**Example:**

Select Workload, anat path Option: **CW** Cytology screening workload

Enter year: 1993// **&lt;Enter&gt;**

Select Accession Number: **11** for 1993

Date/time slides examined: NOW// **&lt;Enter&gt;** (APR 1,1993 15:09)  OK? YES// **&lt;Enter&gt;** (YES)

LABPAIENT1, FOUR 0014 Acc #: 11 Date: APR 1, 1993

Slide/Ctrl  	Date Slides Examined

BRONCHIAL WASHING

Smear Prep

SMEAR PRE  Stain/Procedure

* 1) PAP STAIN, SMEAR PREP	 2    	APR 1, 1993 15:09

Cell Block

CELL BLOC  Stain/Procedure

* 2) H &amp; E STAIN     	 1    	APR 1, 1993 15:09

Data displayed ok ? NO// **Y** (YES)

Select Accession Number: **&lt;Enter&gt;**

**NOTES:**

•	Screening WKLD codes are captured based on the date/time entered for screening. However, if the data for the staining date/time has not been entered yet, the information for screening cannot be entered. The date/time examined MUST be later than the date/time stained.

•	In the case of the codes for PAP smears, determination of the appropriate code may not be totally transparent since the selection of the code is based on whether the PAP smear result is negative or positive. Based on the PAP STAIN execute code, which is controlled by the REQUIRED COMMENT, the software will check the SNOMED morphology code. If the right codes have been entered for suspicious or positive (M69760 or M80013) or negative (M09460), the appropriate code will be selected. If the morphology code has not been entered or does not match, a prompt will be displayed to select the correct code.

•	If an accession is reentered once the date/time screened has been entered, a prompt will appear to allow entry of a code for rescreening of negative GYN PAP smears for QA purposes. Previously accumulated workload cannot be edited using this option.

#### Display Workload for an Accession [LRUWL]

During those times when verification of data capture is necessary, i.e., testing, software implementation or software changes, this can be accomplished by using this option. Keep in mind that this display reflects the last date/time entered for each test as it is based on data in File 68. In order to look at the actual date/time for workload for a given test where part of the work was done at one time and part of the work was done at a later time, it is necessary to look at File #64.1.

**Example:**

Select Workload, anat path Option: **DW** Display workload for an accession

Select ACCESSION AREA: **SP** SURGICAL PATHOLOGY

Select SURGICAL PATHOLOGY Date: 1993// **91** 1991

Select SURGICAL PATHOLOGY Accession Number for 1991: **11**

TEST: XXSURGICAL PATHOLOGY LOG-IN   TECHNOLOGIST: GINS,RON

COMPLETE DATE: DEC 31, 1991@07:21

WKLD CODE: Surgical Path., Init. Handling

TEST MULTIPLY FACTOR: 1        WKLD CODE COUNTED: YES

WKLD CODE TALLY: 1          COMPLETION TIME: DEC 31, 1991@07:21

USER: LABPROVIDER, EIGHT            INSTITUTION: REGION 5

MAJOR SECTION: SURGICAL PATHOLOGY   LAB SUBSECTION: SURGICAL PATHOLOGY

WORK AREA: SURGICAL PATHOLOGY

WKLD CODE: Transcription: File Search/Retrieve

TEST MULTIPLY FACTOR: 1        WKLD CODE COUNTED: YES

WKLD CODE TALLY: 1          COMPLETION TIME: DEC 31, 1991@07:21

USER: LABPROVIDER, EIGHT     INSTITUTION: REGION 5

MAJOR SECTION: SURGICAL PATHOLOGY   LAB SUBSECTION: SURGICAL PATHOLOGY

WORK AREA: SURGICAL PATHOLOGY

TEST: EXTENSIVE GROSS SURGICAL     TECHNOLOGIST: LABPROVIDER, EIGHT

COMPLETE DATE: DEC 31, 1991@07:22

WKLD CODE: Tissue Preparation      TEST MULTIPLY FACTOR: 1

WKLD CODE COUNTED: YES        WKLD CODE TALLY: 1

COMPLETION TIME: DEC 31, 1991@07:22  USER: GINS,RON

INSTITUTION: REGION 5         MAJOR SECTION: SURGICAL PATHOLOGY

LAB SUBSECTION: SURGICAL PATHOLOGY  WORK AREA: SURGICAL PATHOLOGY

#### EM Scanning and Photo Workload [LRAPWE]

This option allows recording workload for scanning and photography of EM grids and making of prints.

**NOTE:** In order to input workload associated with the scanning of the EM grids, the prompt “Ask ‘Date/time grids scanned:’ prompt for each accession ? NO//” must be answered “YES.”

Example:	Entry of only photography workload

Select Anatomic pathology Option: **W** Workload, anat path

Select Workload, anat path Option: **EW** EM scanning and photo workload

Ask 'Date/time grids scanned:' prompt for each accession ? NO// **&lt;Enter&gt;** (NO)

Enter year: 1992// **&lt;Enter&gt;** ( 1992) 1992

Select Accession Number: **8** for 1992

Date/time prints made: NOW// **&lt;Enter&gt;** (JAN 13, 1992@10:40) OK ? YES// **&lt;Enter&gt;** (YES)

LABPATIENT1, TWO 0012 Acc #: **8** Date: JAN 13, 1992

GRIDS  GRIDS  PRINTS LAST DATE/TIME   LAST DATE/TIME

BLOCK ID PREPARED SCANNED  MADE    SCANNED      PRINTS MADE

SKIN

*1) EPON 1   5    0    0            01/13/92 10:40

KIDNEY

*2) EPON 1   5    0    0            01/13/92 10:40

Data displayed ok ? NO// **&lt;Enter&gt;** (NO)

(If more than one block a selection must be made)

Select *BLOCK ID#: **1**

EPON 1

DATE/TIME prints made: JAN 13, 1992@10:40// **&lt;Enter&gt;** (JAN 13, 1992@10:40)

TOTAL NUMBER of prints made: **10**

Select *BLOCK ID#: **2**

EPON 1

DATE/TIME prints made: JAN 13, 1992@10:40// **&lt;Enter&gt;** (JAN 13, 1992@10:40)

TOTAL NUMBER of prints made: **14**

Select *BLOCK ID#: **&lt;Enter&gt;**

LABPATIENT1, TWO 0012  Acc #: **8** Date: JAN 13, 1992

GRIDS  GRIDS  PRINTS LAST DATE/TIME   LAST DATE/TIME

BLOCK ID PREPARED SCANNED  MADE    SCANNED      PRINTS MADE

SKIN

*1) EPON 1   5    0    10            01/13/92 10:40

KIDNEY

*2) EPON 1   5    0    14            01/13/92 10:40

Data displayed ok ? NO// **Y** (YES)

Select Accession Number: **&lt;Enter&gt;**

**NOTE:** The workload accumulated for only this portion of the data entry would be as shown in the following extract of information displayed by Display Workload for an Accession [LRUWL] option prior to the time the Nightly Cleanup [LRTASK NIGHTY] option is run.

Select EM Accession Number for 1992: **8**

TEST: EM PRINT/ENLARGEMENT       URGENCY OF TEST: WKLD

TECHNOLOGIST: LABPROVIDER6, THREE   COMPLETE DATE: JAN 13, 1992@10:40

WKLD CODE: Photography Print Enlarge  TEST MULTIPLY FACTOR: 14

WKLD CODE COUNTED: NO         WKLD CODE TALLY: 0

COMPLETION TIME: JAN 13, 1992@10:40  USER: LABPROVIDER6, THREE

INSTITUTION: HINES, IL        MAJOR SECTION: EM

LAB SUBSECTION: EM          WORK AREA: EM

Select EM Accession Number for 1992: **&lt;Enter&gt;**

Select EM Date: **&lt;Enter&gt;**

#### Surg Path Gross Assistance Workload [LRAPWRSP]

If the histology personnel, i.e., non-physicians, assist in the performance of the surgical pathology gross description, this workload can be recorded using this option. This option will allow entry of the date/time of the gross description/cutting and will allow designation of the type of assistance, i.e., routine gross, extensive gross or technical assistance. This will then automatically order the appropriate test and appropriate verify workload codes. Workload data entered through this option is tallied in the usual manner and is accession specific, i.e., it is **not** treated as MANUAL INPUT workload.

**Example:** Select Anatomic pathology Option: **W** Workload, anat path

Select Workload, anat path Option: **SW** Surg path gross assistance workload

Enter year: 1991// **&lt;Enter&gt;** ( 1991) 1991

Select Accession Number: **11** for 1991

LABPATIENT1, EIGHT ID: 000-00-0018

Date/time Gross Description/Cutting: NOW// **&lt;Enter&gt;** (DEC 31, 1991@07:22)

OK ? YES// **&lt;Enter&gt;**

LABPATIENT1, EIGHT 0018 Acc #: 11 Date: DEC 31, 1991

Date Gross Description/Cutting Type

STOMACH            DEC 31, 1991@07:22

Data displayed ok ? NO// **&lt;Enter&gt;** (NO)

Select SPECIMEN: STOMACH// **&lt;Enter&gt;**

GROSS DESCRIPTION/CUTTING TYPE: **??**

Select 1 or “R” when the gross description and cutting of surgical

tissue is performed by a nonphysician (e.g., a pathology assistant)

Select 2 or “E” when extensive gross processing is required by

technical assistants in addition to the usual dissection and

description (e.g., orientation of a renal biopsy and splitting it

for light and electron microscopy, and immunofluorescence)

Select 3 or “T” when technical or clerical staff assist with

gross processing.

CHOOSE FROM:

1    ROUTINE GROSS SURGICAL

2    EXTENSIVE GROSS SURGICAL

3    TECHNICAL ASSISTANCE SURGICAL

GROSS DESCRIPTION/CUTTING TYPE: **2** EXTENSIVE GROSS SURGICAL

GROSS DESCRIPTION/CUTTING DATE: DEC 31,1991@07:22 // **&lt;Enter&gt;**

Select SPECIMEN: **LABPATIENT1, EIGHT** 0018 Acc #: 11 Date: DEC 31, 1991

Date Gross Description/Cutting Type

STOMACH            DEC 31, 1991@07:22 EXTENSIVE GROSS SURGICAL

Data displayed ok ? NO// **Y** (YES)


MICROFICHE OF PATH REPORTS


## Microfiche of Path Reports

The storage of Anatomic Pathology reports over a number of years requires a considerable amount of space for the bound volumes, whether they are all retained in the Pathology Service or stored off-site. Other methods of compact storage can greatly economize on use of this space. Such methods as microfilming and microfiche. Newer techniques such as compact laser discs are emerging, and may already be available, but at considerable expense. This section provides instructions for using microfiche within the Anatomic Pathology module of the Laboratory package.

Microfiche and microfilming are technologies well-developed at this time and are relatively inexpensive. Many hospitals are using these techniques in various departments on a daily basis—even for reports which are computerized. The equipment and service costs to microfiche anatomic pathology reports are reasonable and can be accommodated by almost any budget.

A microfiche reader-printer in the Anatomic Pathology department is an absolute necessity for using microfiche. Reader/printers range in cost from about $550 - $600 for the low usage installations, and about $2500 for the higher volume pathology laboratories. A copy machine, which is accessible in most hospitals, is a helpful adjunct.

### To Use at a VAX site

Using the Microfiche Path Reports option from the Anatomic Pathology Menu - VAX SITES

**Example:**

Select OPTION: **PA** (PRINT FINAL PATH REPORTS BY ACCESSION #)

Select ANATOMIC PATHOLOGY SECTION: **SP** SURGICAL PATHOLOGY

DATE: **1-90** (JAN 1990)

Start with accession #: **1**

Go to accession #: **900**

DEVICE: **MICROFICHE** INPUT/OUTPUT OPERATION: **N**

Do you want to queue this report ? No// **N** (NO)

### To Use at a Non-VAX site

1. Coordinate the procedure with your IRM office.

The IRM office will have to load the tape drive with tape and place it on line. Do not purge the text in the files until you have the fiche and are satisfied with the result.

Be sure to lock the Print Final Path Reports by Accession # [LRAPFICH] option with a security key to prevent accidental use by inappropriate users.

1. Enter the menu option, Print final path reports by accession #.

Follow the prompts as you would to print any list in the selected Laboratory AP section.

1. At the “Device” prompt, enter: “MICROFICHE/81.”

This will now print to the magtape and also tie up your terminal until the job is complete. Thus, it is recommended that it be done during a known low-user time period.

1. When the job is completed, give the tape to a service bureau.

The service bureau will convert it into fiche. The service bureau will need to know the drive settings and how many frames per fiche, etc. The turnaround time is as short as overnight once they have the characteristics for your AP jobs. You may have to do several runs to fine-tune the fiche. We recommend practicing with about ten cases before doing the serious run.

#### Creating a Microfiche Tape

**Example 1:** Cytopathology, Electron Microscopy, and Surgical Pathology

Select Print, anat path Option: **?**

PQ	Print all reports on queue

DQ	Delete report print queue

LQ	List pathology reports in print queue

PS	Print single report only

AD	Add patient(s) to report print queue

AU	Autopsy administrative reports

AR	Anat path accession reports

CS	Cum path data summaries

LA	Anatomic pathology labels

LT	Edit/print/display preselected lab tests

PB	Print log book

Prisoner of war veterans

PA	Print final path reports by accession #

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Print, anat path Option: **PA** PRINT FINAL PATH REPORTS BY ACCESSION #

Select ANATOMIC PATHOLOGY SECTION: **SP** SURGICAL PATHOLOGY

(or Cytopathology or Electron Microscopy)

DATE: **90** (1990)

Start with accession #: **1362**

Got to accession: **1735**

DEVICE: **MICROFICHE/81**

MICROFICHE MAGTAPE 81

This device is not a printer!

ARE YOU SURE you want to use it? NO// **Y** (YES)

Since you have not queued the report it will print

immediately on the device selected.

But you will not be able to use your terminal

during the printing.

Is this what you want? NO// **Y** (YES)

Select Print, anat path Option: **&lt;Enter&gt;**

**Example 2:** Autopsy

Select ANATOMIC PATHOLOGY option: **P** PRINT, ANAT PATH OPTION

Select Print, anat path Option: **AD** ADD PATIENT(S) TO REPORT PRINT QUEUE

Select PATIENT NAME: LABPATIENT, ONE	08-08-48	000000001		NON-VETERAN

LABPATIENT, ONE ID:000-00-0001 Physician:	LABPROVIDER2, EIGHT

DIED JUL 27, 1990

Autopsy performed: JUL 28, 1990 08:00 Acc # 2

Select PATIENT NAME: **&lt;Enter&gt;**

Select Print, anat path Option: **PQ** PRINT ALL REPORTS ON QUEUE

Select ANATOMIC PATHOLOGY section: **AU** AUTOPSY

1.	Autopsy protocols

2.	Autopsy supplementary reports

Select 1 or 2: **1**

Autopsy Protocols

(D)ouble or (S)ingle spacing of report(s): **D**

Print weights, measures and coding (if present): ? YES// **&lt;Enter&gt;** (YES)

Save protocol list for reprinting ? NO// **&lt;Enter&gt;** (NO)

DEVICE: **MICROFICHE/81**

MICROFICHE MAGTAPE 81

This device is not a printer!

ARE YOU SURE you want to use it? NO// **Y** (YES)

Since you have not queued the report it will print

immediately on the device selected.

But you will not be able to use your terminal

during the printing.

Is this what you want? NO// **Y** (YES)

Select Print, anat path Option,: **&lt;Enter&gt;**

### Enhancements to Reports on Microfiche

A number of improvements are recommended to enhance reports on microfiche such as the following:

Data Pages:

Double or triple size of data header with key index data on top of each page.

Bold or italic data field anywhere in data--double size data available under some conditions.

Titling:

Normal and reverse polarity. By title segments or portion of segments.

Multiple number and variable size of characters by title segments.

Eyeball Pages:

Eye readable data to highlight major changes within data.

For example: new report, or change in departments. Data breaks can be used with the eyeball pages to advance to the top of the next column for quicker user access to their data.

Bypass Options:

Ability to bypass selected data pages not meaningful to the end user.

This could include system-generated data, banner pages, alignment pages or selected reports in multiple report file.

Data Break Options:

Ability to break to the next microfiche or the next column whenever a significant change in data occurs. This allows selective grouping of specific reports to various user groups, or a selective breakdown of a large report to specific user areas.

Indexing Options:

Standard page index in lower right corner of the microfiche.

Column index at the bottom of each column.

The index page is enhanced by suppressing the printing of identical index values, which makes it easier and quicker to read and use. **Benefits:**

Information retrieval from microfiche becomes much easier and, as a result, user productivity will dramatically improve. User departments have reported retrieval time improvements of 25% to 50% with these techniques. User acceptance of microfiche will also dramatically improve as information retrieval becomes easier and quicker. Increased user productivity will result in direct dollar savings to VAMCs.

GLOSSARY

## Glossary

Abbreviated Response	This feature allows you to enter data by typing only the first few characters for the desired response. This feature will not work unless the information is already stored in the computer.

Access Code	A code that allows the computer to identify you as a user authorized to gain access to the computer. Your code is greater than six and less than twenty characters long; can be numeric, alphabetic, or a combination of both; and is usually assigned by a site manager or application coordinator. (See the term verify code in the Glossary.)

Accession	A unique alpha-numeric (combination of letters and numbers) assigned to an individual patient specimen when it is received in the laboratory. The accession is assigned by the computer and contains the laboratory departmental designation, the date and an accession number. This accession serves as identification of the specimen as it is processed through the laboratory. (Example: HE 0912 1)

Accession Area	A functional area or department in the laboratory where specific tests are performed. The accession area defines the departmental designation contained in each accession.

Accession Date	The date of the accession, part of the total alpha-numeric accession of each specimen.

Accession Number	A unique number assigned to each accession.

ADP	Automated Data Processing

ADT	Admission, Discharge, Transfer. A component of the MAS software package .

AEMS	Automated Engineering Management Systems. This is the Engineering Service software package.

AFIP	Armed Forces Institute of Pathology; an external review board.

AMIE	Automated Management Information Exchange. A system that allows the Veterans Benefits Administration to use their WANG System to query medical centers via the VADATS network. See WKLD.

AMIS	Automated Management Information System; a method for tabulating Workload.

AMIS/CAP CODES	Numbers assigned to lab procedures by the  for compiling workload statistics.

ANSI	American National Standards Institute. An organization that compiles and publishes computer industry standards.

ANSI MUMPS	The MUMPS programming language, now officially called “M” Technology, is a standard; that is, an American National Standard. MUMPS stands for Massachusetts General Hospital Utility Multi-Programming System.

APP	Applications Portability Profile

Algorithm	A predetermined set of instructions for solving a specific problem in a limited number of steps.

Application	A computer program (e.g., a package) that accomplishes tasks for a user.

Application Coordinator	The designated individual responsible for user-level management and maintenance of an application package (e.g., IFCAP, Laboratory, Pharmacy, Mental Health).

ARG	Application Requirements Group. A designated group of applications experts who work with the developers of a software package to define and approve the contents of the package.

Array	An arrangement of elements in one or more dimensions. A MUMPS array is a set of nodes referenced by subscripts which share the same variable name.

ASCII	American Standard Code for Information Interchange. A series of 128 characters, including uppercase and lowercase alpha characters, numbers, punctuation, special symbols, and control characters.

Attribute Dictionary	See data dictionary.

Audit	An audit is a physical record of access to a file. The VA FileMan and Kernel provide audit tools that may be used to maintain a continuous audit trail of changes that are made to an existing database. Elements that can be tracked include, but are not limited to, fields within files and files themselves. Records are kept of the date/time and user making changes. In addition, the Kernel provides tools for auditing system access, option access, and device usage. Logs store the date/time of access, user identification and name of the option or device used.

Audit Access 	A user’s authorization to mark or indicate that certain information stored in a computer file should be audited.

Audit Trail	A chronological record of computer activity automatically maintained to trace the use of the computer.

Auto Instruments	Automated instruments used in the Lab that identify and measure tissue or other specimens.

Backup	The process of creating duplicate data files and/or program copies that serve in case the original is lost or damaged.

Baud (Baud rate)	A measure of times per second that switching can occur in a communications channel. Data transmission speed roughly equivalent to 1 bit per second (bps). Commonly used baud rates include 300, 1200, 2400, 3600, 4800, and 9600.

Bidirectional	Automated instruments that send and receive information from DHCP.

Boolean	A term used in computer science for data that is binary (i.e., either true or false).

Boot	To load instructions into main memory to get a computer operational.

Buffer	A temporary holding area for information.

Bug	An error in a program. Bugs may be caused by syntax errors, logic errors, or a combination of both.

Bypass Options	Ability to bypass selected data pages not meaningful to the end user. This could include system-generated data, banner pages, alignment pages or selected reports in multiple report files.

CAP	Numbers assigned to lab procedures by the  for compiling work statistics.

Caret	A symbol expressed as ^ (up caret), &lt; (left caret), or &gt; (right caret). In many MUMPS systems, a right caret is used as a system prompt and an up caret as an exiting tool from an option. The up caret is also known as the up-arrow symbol or “shift-6” key.

Checksum	The result of a mathematical computation involving the individual characters of a routine or file.

Cipher 	A system that arbitrarily represents each character by one or more other characters.

Collection List	A listing of routine laboratory tests ordered for inpatients. The list is used by the Phlebotomy team during routine collection of specimens from the wards. The list is sorted by ward location, and includes both patient information (Name, SSN, and bed/room number) and test information, type of specimen to collect, amount needed, date and time tests were ordered, urgency status, order number, and accession number.

Command	A combination of characters that instruct the computer to perform a specific operation.

Computed Field	This field takes data from other fields and performs a predetermined mathematical function (e.g., adding two columns together). You will not, however, see the results of the mathematical calculation in the file. Only when you are printing or displaying information on the screen will you see the results for this type of field.

Computer	A device that processes information. A machine that has input, output, storage, and arithmetic devices plus logic and control units.

Control Key	The Control Key (Ctrl on the keyboard) performs a specific function in conjunction with another key. In some word-processing applications, for example, holding down the Ctrl key and typing an A will cause a new set of margins and tab settings to occur; Ctrl-S causes printing on the terminal screen to stop; Ctrl-Q restarts printing on the terminal screen; Ctrl-U deletes an entire line of data entry when the return key is pressed.

Core	The fundamental clinical application packages of DHCP. The original core of applications built on the Kernel and VA FileMan were Admission, Discharge and Transfer (ADT), Scheduling, Outpatient Pharmacy, and Clinical Laboratory. Additional software packages were added to implement Core+6 and Core+8 configurations.

CPU	Central Processing Unit. Those parts of computer hardware that carry out arithmetic and logic operations, control the sequence of operations performed, and contain the stored program of instructions.

Cross Reference	A cross-reference on a file provides direct access to the entries in several ways. For example, the Patient file is cross-referenced by name, social security number, and bed number. When asked for a patient, the user may then respond with the patient’s name, social security number, or bed number. Cross reference speeds up access to the file for printing reports. A cross reference is also referred to as an index or cross-index.

CRT	Cathode Ray Tube. A piece of computer hardware that looks something like a television screen. The CRT and keyboard collectively are called your terminal. A vacuum tube that guides electrons onto a screen to display characters or graphics. Also called VDT for video display terminal.

Cumulative	A chartable patient report of all data accumulated on a patient over a given time period.

Cursor	A flashing image on your screen (generally a horizontal line or rectangle) that alerts you that the computer is waiting for you to make a response to an instruction (prompt).

Data	In the generic sense, data is information that can be processed and/or produced by computers.

Data Attribute	A characteristic of a unit of data such as length, value, or method of representation. VA FileMan field definitions specify data attributes.

Database	A set of data, consisting of at least one file, that is sufficient for a given purpose. The Kernel database is composed of a number of VA FileMan files. A collection of data can be about a specific subject (e.g., the Patient file). A data collection has different data fields (e.g., patient name, SSN, date of birth).

Database Management System	A collection of software that handles the storage, retrieval and updating of records in a database. A Database Management System (DBMS) controls redundancy of records and provides the security, integrity, and data independence of a database. VA FileMan is the Database Management System for the DHCP software.

Databreak options	Ability to break to the next microfiche or the next column whenever a significant change in data occurs. This allows selective grouping of specific reports to various user groups, or a selective breakdown of a large report to specific user areas.

Data Dictionary	A Data Dictionary (DD) contains the definitions of a file’s elements (fields or data attributes); relationships to other files; and structure or design. Users generally review the definitions of a file’s elements or data attributes; programmers review the definitions of a file’s internal structure.

Data Dictionary Access	A user’s authorization to write/update/edit the data definition for access computer file. Also known as DD Access.

Data Dictionary Listing	This is the printable report that shows the data dictionary. DDs are used by users, programmers, and documenters.

Data Processing	Logical and arithmetic operations performed on data. These operations may be performed manually, mechanically, or electronically. Sorting through a card file by hand would be an example of the first method; using a machine to obtain cards from a file would be an example of the second method; and using a computer to access a record in a file would be an example of the third method.

DBA	Within the VA, the Database Administrator oversees package development with respect to DHCP Standards and Conventions (SAC) such as name-spacing, file number ranges, and integration issues.

Debug	To correct logic errors and/or syntax errors in a computer program. To remove errors from a program.

Default	A response the computer considers the most probable answer to the prompt being given. It is identified by double slash marks (//) immediately following it. This allows you the option of accepting the default answer or entering your own answer. To accept the default, you simply press the enter (or return) key. To change the default answer, type in your response.

Delete	The key on your keyboard (may also be called D or backspace on some terminals) that allows you to delete individual characters working backwards by placing the cursor immediately after the last character of the string of characters you wish to delete. The @ sign (the “shift-2” key) may also be used to delete a file entry or data attribute value. The computer will ask “Are you sure you want to delete this entry?” to insure you do not delete an entry by mistake.

Delimiter	A special character used to separate a field, record, or string. VA FileMan uses the "   character as the delimiter within strings.

Device	A terminal, printer, modem, or other type of hardware or equipment associated with a computer. A host file of an underlying operating system may be treated like a device in that it may be written to (e.g., for spooling).

Device file	A DHCP file (in VA FileMan) where devices (printers or terminals) are defined.

DHCP	The Decentralized Hospital Computer Program of the Veterans Health Administration (VHA), Department of Veterans Affairs (VA). DHCP software, developed by the VA, is used to support clinical and administrative functions at VA medical centers nationwide. It is written in MUMPS and, via the Kernel, will run on all major MUMPS implementations regardless of vendor. DHCP is composed of packages which conform with name spacing and other DHCP standards and conventions.

Disk	The medium used in a disk drive for storing data.

Disk Drive	A peripheral device that can be used to “read” and “write” on a hard or floppy disk.

Documentation	User documentation is an instruction manual that provides users with sufficient information to operate a system. System documentation describes hardware and operating systems provided by a system vendor. Program documentation describes a program’s organization and the way in which the program operates and is intended as an aid to programmers who will be responsible for revising the original program.

DRG	Diagnostic Related Group

DSCC	The Documentation Standards and Conventions Committee

DSS	Decision Support System

E3R	Electronic Error Enhancement Reporting System

Electronic Signature 	A code that is entered by a user which represents his or her legally binding signature.

Encryption	Scrambling data or messages with a cipher or code so that they are unreadable without a secret key. In some cases encryption algorithms are one directional; they only encode and the resulting data cannot be unscrambled (e.g., access/verify codes).

Enter	Pressing the return or enter key tells the computer to execute your instruction or command or to store the information you just entered.

Entry	A VA FileMan record. It is uniquely identified by an internal entry number (the .001 field) in a file.

EP	Expert Panel

Extended Core	Those applications developed after the basic core DHCP packages were installed (e.g., Dietetics, Inpatient Pharmacy). Also referred to as Core+6 or Core+8.

Eyeball pages	Eye readable data to highlight major changes within data; for example: new report, or change in departments. Data breaks can be used with the eyeball pages to advance to the top of the next column for quicker user access to their data.

Field	In a record, a specified area used for the value of a data attribute. The data specifications of each VA FileMan field are documented in the file’s data dictionary. A field is similar to blanks on forms. It is preceded by words that tell you what information goes in that particular field. The blank, marked by the cursor on your terminal screen, is where you enter the information.

File	A set of related records treated as a unit. VA FileMan files maintain a count of the number of entries or records.

FileManager	See VA FileMan.

FOIA	The Freedom Of Information Act. Under the provisions of this public law, software developed within the VA is made available to other institutions, or the general public, at a nominal charge that covers the cost of reproduction, materials, and shipping.

Free Text	The use of any combination of numbers, letters, and symbols when entering data.

FTAM	File Transfer, Access, and Management

GKS	Graphic Kernel Standard

Global	In the MUMPS language, a global is a tree-structured data file stored in the common database on the disk.

Global Variable	A variable that is stored on disk (MUMPS usage).

GOSIP	Government Open Systems Interconnection Profile

GUI	Graphic User Interface

Hacker	A computer enthusiast; also, one who seeks to gain unauthorized access to computer systems.

Handshake 	A method for controlling the flow of serial communication between two devices, so that one device transmits only when the other device is ready.

Hardware	The physical equipment pieces that make up the computer system (e.g., terminals, disk drives, and central processing units). The physical components of a computer system.

Header	Information at the top of a report.

Help Prompt	The brief help that is available at the field level when entering one or more question marks.

HINQ	Hospital Inquiry. A system that permits medical centers to query the Veterans Benefits Administration systems via the VADATS network.

HIS	Hospital Information Systems

HOST	Hybrid Open Systems Technology

IFCAP	Integrated Funds Distribution, Control Point Activity, Accounting and Procurement

IHS	Indian Health Service

IHS	Integrated Hospital System

Interactive Language	The dialogue that takes place between the computer and the user in the form of words on the screen of the user’s CRT.

Initialization	The process of setting variables in a program to their starting value.

Input Transform	An executable string of MUMPS code which is used to check the validity of input and converts it into an internal form for storage.

IRAC	Information Resources Advisory Council

IRM	Information Resource Management

ISC

JCAHO	Joint Commission for the Accreditation of Health Care Organizations.

Jump (also called 	The Up-Arrow Jump allows you to go from a

Up-Arrow Jump)	particular field within an input template to another field within that same input template. You may also Jump from one menu option to another menu option without having to respond to all the prompts in between. To jump, type an up-arrow (^) - the “shift-6” key on most keyboards - and then type the name of the field in the template or option on your menu you wish to jump to.

Kernel	A set of DHCP software routines that function as an intermediary between the host operating system and the DHCP application packages such as Laboratory, Pharmacy, IFCAP, etc. The Kernel provides a standard and consistent user and programmer interface between application packages and the underlying MUMPS implementation. Two Kernel components, VA FileMan and MailMan, are self-contained to the extent that they may stand alone as verified packages. Some of the Kernel components are listed below along with their associated namespace assignments.

VA FileMan	Dl

MailMan	XM

Sign-on Security	XU

Menu Management	XQ

Tools	XT

Device Handling	ZIS

Task Management	ZTM

Key	A security code that is assigned to individual users that allows access to options.

Lab Sub-section	Refers to the subdivision of lab major sections. If your lab uses this system, your reports will be printed and totaled by lab sub-section as well as lab section.

LAYGO access	A user’s authorization to create a new entry when editing a computer file. (Learn As You GO, the ability to create new entries).

Line Editor	This is VA FileMan’s special line-oriented text editor. This editor is used for the word-processing data type.

LMIP	Laboratory Management Index Program

Local Variable	A variable that is stored in a local partition.

Load List	Used for organizing the workload in various accession areas of the laboratory. A load list is generated for each automated instrument, and is used to arrange the order in which standards; controls and patient specimens are to be run on the specific instrument.

Log In/On	The process of gaining access to a computer system.

Log Out/Off	The process of exiting from a computer system.

Looping	A set of instructions in a program that are repeatedly executed. When set up correctly, VA FileMan allows you to loop through groups of entries in a file without having to select each entry individually.

LSI	Large Scale Integrating Interface also known as Laboratory System Interface, an instrument for translating data between DHCP and auto instruments.

Magnetic Tape	Plastic or mylar tape on reels or cassettes used for data storage (also called mag tape).

MailMan	An electronic mail system that allows you to send and receive messages from other users via the computer.

Major Section	Refers to the grouping of lab sub-sections into major groups within the lab. A lab may consist of the following major sections: General Clinical (may include hematology, toxicology, serology, chemistry, etc.), Blood Bank, Microbiology, and Anatomic Pathology. If your lab uses this system, your workload report will be reported by major section (“Section Workload Report”).

Mandatory Field	This is a field that requires a value. A null response is not valid.

MAS	Medical Administration Service

Menu	A list of options you are authorized access to and may select from.

Menu Tree	A series of menus you sequence through in order to get to the specific option you desire.

Microfiche	A device for microfilming for data storage.

Microscan	An automated instrument used for organism identification and for measuring antibiotics within the Microbiology module.

MIRMO	Medical Information Resources Management Office in the Department of Veterans Affairs Central Office in Washington, DC.

MIS	Management Information Systems

Modem	A device for connecting a terminal to a telephone line, allowing it to communicate with another modem. Modems include the following types.

Direct Connect *—* The modem is directly hooked into the phone line.

Acoustic *—* The modem is connected to the telephone through the handset.

Auto Answer—When it detects a ring signal, the modem will “answer the phone.”

Auto Dial *—* The modem, upon command from the terminal or the computer, will dial another modem.

Multiple-valued	More than one data value is allowed as the value of a data attribute for an entry.

Utility Multi-Programming System

Name spacing	A convention for naming DHCP package elements. The DBA assigns unique character strings for package developers to use in naming routines, options, and other package elements so that packages may coexist. The DBA also assigns a separate range of file numbers to each package.

NAVAP	National Association of VA Physicians

NCD	National Center for Documentation, located at the Birmingham ISC.

NIST	National Institute of Standards and Technology

NOAVA	Nationwide Office Automation for Veterans Affairs

Node	In a tree structure, a point at which subordinate items of data originate. A MUMPS array element is characterized by a name and a unique subscript. Thus the terms node, array element, and subscripted variable are synonymous. In a global array, each node might have specific fields or “pieces” reserved for data attributes such as name. In data communications, the point at which one or more functional units connect transmission lines.

Numeric field	A response that is limited to a restricted number of digits. It can be dollar valued or a decimal figure of specified precision.

OE/RR	Order Entry and Results Reporting

On-line	A device is on-line when it is connected to the computer.

On-the-fly	A term given to the process of not permanently storing data in the data dictionary but having a computation performed at run time.

Operating System	A basic program that runs on the computer, controls the peripherals, allocates computing time to each user, and communicates with terminals.

Order number	A number generated by the computer each time a test is ordered - unique for each patient’s order - starting at midnight JAN 1 with order number 1. The order number provides identification of patient specimens both during transport to the laboratory and until accession numbers have been assigned to the specimens. Generally used by non-laboratory personnel; e.g., ward, section, number.

OS/M	Occurrence Screen/Monitor

Output Transform 	An executable string of MUMPS code which converts internally stored data into a readable display.

PACS	Picture Archiving and Communications Systems

Package	The set of programs, files, documentation, help prompts, and installation procedures required for a given software application. For example, Laboratory, Pharmacy, and MAS are packages. A DHCP software environment composed of elements specified via the Kernel’s Package file. Elements include files and associated templates, name spaced routines, and name spaced file entries from the Option, Key, Help Frame, Bulletin, and Function files. Packages are transported using VA FileMan’s DIFROM routine that creates initialization routines to bundle the files and records for export. Installing a package involves running the installation routines that will recreate the original software environment. Verified packages include documentation. As public domain software, verified packages may be requested through the Freedom of Information Act (FOIA).

Password	A user’s secret sequence of keyboard characters, which must be entered at the beginning of each computer session to provide the user’s identity.

Pattern Match	A preset formula that includes any one of the following types: 1) letters, numbers, or symbols; 2) letters, numbers, and symbols; 3) letters and numbers; 4) symbols and letters; 5) numbers and symbols. If the information entered (does not match the formula exactly, the computer rejects the user’s response).

Peripheral Device	Any hardware device other than the computer itself (central processing unit plus internal memory). Typical examples include card readers, printers, CRT units, and disk drives.

Pointer	Points to another file where the computer stores information needed for the field of the file in which you are currently working. If you change any of the information in the field in which you are working, the new information is automatically entered into the “pointed to” file.

POSIX	Portable Operating System Interface for Computing Environments

Printer	A printing or hard copy terminal.

Program	A list of instructions written in a programming language and used for computer operations.

Programmer Access Code 	An optional three-to-eight character code that allows the computer to identify you as a user authorized to enter into programmer mode (see also access code). Once in programmer mode, you will use Standard MUMPS, DHCPs official programming language, to interact with the computer. Programmer access is very tightly restricted to authorized, qualified individuals.

Programmer Access	Privilege to become a programmer on the system and work outside many of the security controls of Kernel.

Prompt	The computer interacts with the user by issuing questions called prompts, to which the user issues a response.

QA	Quality Assurance

RAM	Random Access Memory

Read Access	A user’s authorization to read information stored in a computer file.

Reader-printer	A device for displaying and printing microfiche.

Record	A set of related data treated as a unit. An entry in a VA FileMan file constitutes a record. A collection of data items that refers to a specific entity. For example, in a name-address-phone number file, each record would contain a collection of data relating to one person.

Required Field	A mandatory field, one that must not be left blank. The prompt for such a field will be asked until the user enters a valid response.

RMEC

ROM	Read Only Memory. A type of memory that can be read but not written.

Routine	A program or a sequence of instructions called by a program, that may have some general or frequent use. MUMPS routines are groups of program lines which are saved, loaded, and called as a single unit via a specific name.

SAC	Standards and Conventions. Through a process of verification, DHCP packages are reviewed with respect to SAC guidelines as set forth by the Standards and Conventions Committee (SACC). Package documentation is similarly reviewed in terms of standards set by the Documentation Standards and Conventions Committee (DSCC).

SACC	Standards and Conventions Committee of the Decentralized Hospital Computer Program.

Screen (Noun) 	The display surface of a video terminal.

Screen (Verb) 	The process of checking a user’s input for a pre-defined format or condition (e.g., date within a permitted range).

Screen Editor	This is VA FileMan’s special screen-oriented text editor. This editor is used for the word-processing data type.

Scroll/no scroll	The scroll/no scroll button (also called hold screen) allows the user to “stop” (no scroll) the terminal screen when large amounts of data are displayed too fast to read and to “restart” (scroll).

SERA	Systematic External Review of Autopsies.

SERS	Systematic External Review of Surgical Pathology.

Set of codes	Usually a preset code with one or two characters. The computer may require capital letters as a response (e.g., M for male and F for female). If anything other than the acceptable code is entered, the computer will reject the response.

Site Manager/IRM Chief	At each site, the individual who is responsible for managing computer systems, installing and maintaining new modules, and serving as liaison to the ISCs.

SIUG/ARG	Special Interest User Group/Application Requirements Group. A designated group of applications experts who work with the developers of a software package to define and approve the contents of the package.

SNOMED	Systematized Nomenclature of Medicine, developed to standardize the coding of information regarding specific diseases.

Software	The set of instructions and data required to operate the computer. One type is called operating system software - fundamental computer software that supports other software. The second type is called applications software - customized programs that tell the computer how to run applications (e.g., Pharmacy, Laboratory).

Spacebar Return Feature	You can answer a VA FileMan prompt by pressing the spacebar and then the return key. This indicates to VA FileMan that you would like the last response you were working on at that prompt recalled.

Spooling	Procedure by which programs and output can be temporarily stored until their turn to print.

SQL	Structured Query Language

Stop Code	A number assigned to the various clinical, diagnostic, and therapeutic sections of a facility.

Sub-routine	A sequence of MUMPS code that performs a specific task, usually used more than once.

Subscript	A symbol that is associated with the name of a set to identify a particular subset or element. In MUMPS, a numeric or string value that is enclosed in parentheses; is appended to the name of a local or global variable; identifies a specific node within an array.

Syntax	A term for the rules that govern the construction of a machine language.

Template	A means of storing report formats, data entry formats, and sorted entry sequences is the opposite of “On-the-Fly.” A template is a permanent place to store selected fields for use at a later time.

Terminal	See CRT. May be either a printer or CRT/monitor/visual display terminal.

Titling	Methods of displaying titles on microfiche.

- Normal and reverse polarity.

- By title segments or portion of segments.

- Multiple number and variable size of

characters by title segments.

Treating Area	The section or service of the hospital that requests a test. Some hospital systems have an embedded code that determines if the ordered test is for an inpatient or outpatient.

Tree Structure	A term sometimes used to describe the structure of a MUMPS array. This has the same structure as a family tree, with the root at the top, and ancestor nodes arranged below, according to their depth of subscripting. All nodes with one subscript are at the first level, all nodes with two subscripts at the second level, and so on.

Trigger	A trigger is an instruction that initiates a procedure. In VA FileMan, a trigger can be set up when entry of data in one field automatically updates a second field value.

Truncate	Truncating is a process that drops characters of text or numbers (without rounding) when the text or numbers are limited to a specific location to store or print them. For example, the number 5.768 is truncated to 5.76 when stored or printed in a location that holds only four characters.

Uneditable Field	This is a status given to fields to prevent any editing of data in the field.

Up Arrow	A character on your keyboard that looks like this: “^” character is used mainly for exiting or opting out of answering VA FileMan prompts and jumping to other fields in VA FileMan. The “^” character is the “shift-6” key on most keyboards.

User Access	Access to a computer system. The user’s access level determines the degree of computer use and the types of computer programs available. The systems manager assigns the user an access level. (See also access code and programmer access code.)

Utility Routine	A routine that performs a task that many programmers utilize.

VA	The Department of Veterans Affairs, formerly called the Veterans Administration.

VACO	Department of Veterans Affairs Central Office

VADATS	Veterans Administration Data Transmission System (replaced by IDCU about two to three years ago).

VA FileMan	A set of programs used to enter, maintain,

(also called VA FileManager)	access, and manipulate a database management system consisting of files. A package of on-line computer routines written in the MUMPS language that can be used as a stand-alone database system or as a set of application utilities. In either form such routines can be used to define, enter, edit, and retrieve information from a set of computer-stored files.

VA MailMan	A computer-based message system

VAMC	Department of

Variable	A character or group of characters that refer to a value. MUMPS recognizes three types of variables: local variables, global variables, and special variables. Local variables exist in a partition of main memory and disappear at sign off. A global variable is stored on disk, potentially available to any user. Global variables usually exist as parts of global arrays. The term “global” may refer either to a global variable or a global array. A special variable is defined by system operation (e.g., $TEST).

VAX	Virtual Address Extension

VDT	Video Display Terminal (See CRT)

Verification (data verification)	The process by which technologists review data in the computer for a specific patient and verify (validate) that it is accurate before releasing the data to the physician.

Verification 	A process of internal and external

(package verification) 	package review carried out by a DHCP verification team (people who were not involved in the development of the package. Software and associated documentation are reviewed in terms of DHCP Standards and Conventions.

Verify Code	An additional security precaution used in conjunction with the access code. Like the access code, it is also 6 to 20 characters in length and if entered incorrectly will not allow the user to access the computer. To protect the user, both codes are invisible on the terminal screen. The code must be a combination of alphabetic and numeric characters.

VHA	Veterans Health Administration

VITEK	An automated instrument is used for organism identification and for measuring antibiotics within the Microbiology module.

WKLD	Abbreviation for workload. The Department of Veterans Affairs off shoot of CAP workload reporting. Also used for LMIP applications. See LMIP.

WKLD Code	Numbers assigned to lab procedures by the Laboratory program for compiling work statistics.

Work List	Used for collecting and organizing work in various accession areas of the laboratory. A work list is generated for manual or automated tests (singly or in batches) and can be defined by number of tests and/or which tests to include. It can also be used as a manual worksheet by writing test results directly on the worklist.

Wrap-around mode	Text that is fit into available column positions and automatically wraps to the next line, sometimes by splitting at word boundaries (spaces).

Write Access	A user’s authorization to write/update/edit information stored in a computer file.

INDEX

## Index


1989 revisions of M-2 Part VI, Chapter 4, 42

## A

Accession List by Date [LRUPAD] option, 383

AFIP, 224

Anatomic Pathology, i, iii, v, vi, vii, viii, 11, 15, 18, 21, 25, 26, 28, 47, 49, 110, 130, 131, 137, 144, 154, 180, 203, 206, 210, 222, 260, 301, 323, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 355, 358, 362, 379, 383

Anatomic Pathology main menu, 25

Anatomic Pathology Menu, **26**

Anatomic specimen processing, 32

autopsy protocol, 41

Autopsy protocol &amp; ICD-CM coding [LRAPAUDAA], 373

Autopsy protocol &amp; SNOMED coding [LRAPAUDAB], 373

Autopsy protocol [LRAPAUDAP] option, 372

Autopsy Protocol/Supplementary Report [LRAPAUPT] option, 369

Autopsy Status List [LRAPAUSTATUS], 165

Autopsy supplementary report [LRAPAUSR] option, 364, 373

## B

Before You Begin, iii, 15

bone marrows, 40

Bypass Options, 305

## C

CAP) codes, 21

clinical diagnoses, 58

Clinical Hx/Gross Description/FS [LRAPDGD] option, 371

Clinical Summary, 43

**Clinician** , vii, 25, 27, 30, 110, 112, 115, 143, 268, 275, 277, 280, 282, 284, 288, 348

Comment, 132

## D

Data Break Options, 305

**Data Entry** , iii, iv, 26, 33, 48, 51, 65, 67, 71, 348

Data Pages, 305

Delete Accession. , Anat Path

Description of SNOMED, 37

## E

Edit SNOMED files, 38

**Edit/Modify Data** , iv, 26, 100

Enter old anat path records [LRAPOLD] option, 369

Entering a question mark, 15

Eyeball Pages, 305

## F

Final Anatomic Diagnoses, 43

Final Anatomical Diagnosis information, 54

Final autopsy diagnoses date [LRAPAUFAD], 373

Final Autopsy Diagnosis, 41

Final Reports, 32

Frozen Section information, 40

FS/Gross/Micro/Dx [LRAPDGM] option, 371

FS/Gross/Micro/Dx/ICD-CM Coding [LRAPDGI], 371

FS/Gross/Micro/Dx/SNOMED Coding [LRAPDGS], 371

## G

generic-type options, 47

Gross description, **32**

Gross Description field, 131

## H

Histopathology Worksheet, 130

## I

ICD-CM coding, anat path [LRAPICD] option, 374

incomplete clinical information, 131

Indexing Options, 305

**Inquiries** , iv, 25, 26, 28, 111, 116, 117, 124, 365, 366

## J

JCAHO, 21

## L

LAB DATA file (#63), vii, viii, 345, 346, 347, 348, 353, 355, 358, 359, 360, 361

Lab orders by collection type [LRRP5] option was **modified** , 383

**Listing of Cases Sent to SERS** , 230

Log Book, 41

**Log-in** , iii, v, 11, 25, 26, 28, 32, 35, 79, 101, 108, 130, 131, 133, 134, 135, 136, 137, 138, 182, 269, 348

Log-In Anat Path, 130

**Log-in of Cytopathology Specimen** , 135

**Log-in of Frozen Section Specimen** , 134

Log-in of Routine Surgical Path Specimen, 133

LOG-IN, ANAT PATH [LRAPLG] option, 369

LRVERIFY, 34

## M

Manual Conventions, iii, 18

Micro description and Dx, **32**

microscopics, 34

Modify anat path gross/micro/dx/frozen section [LRAPM] option, 366, 374

More than one EM Specimen, 136

**morphology** , 37

## P

patch LR*5.2*248, **i** , **47** , 54, 60, 95, 96, 147, 154, 242, 268, 270, 288, 290

pathology diagnoses, 58

picture protocol, 41

Preliminary Reports, 33

**Print** , 26

Print all reports on queue [LRAP PRINT ALL ON QUEUE] option, 379

Print final path reports by accession # [LRAPFICH] option, 379

Print Log Book, 130

Print path gross/micr/dx/fr.sect modifications [LRAPQAM] option, 375

Print path modifications [LRAPMOD] option, 375

print queue for autopsy report, 51

Print single report only [LRAP PRINT SINGLE] option, 383

**Provisional Anatomic** , 51

Provisional anatomic diagnoses [LRAPAUPAD], 372

Provisional Autopsy Diagnosis (, 41

## Q

quality assurance features, 12

quality assurance information, 59

Quality Assurance monitors, 43

## S

Search options, 35

**search/reporting** capabilities, 12

SERS, 224

SERS external review, 230

SF 503, 42

SF 515, 131

SF 515s, 33

Show list of accessions for a patient [LRUPT] option, 365

SNOMED coding, **33**

SNOMED coding, anat path [LRAPX] option, 374

**SNOMED Field** , 27

SNOMED files, 38

Spec Studies-EM;Immuno;Consult;Pic, Anat Path [LRAPDSS] option, 372

Special Keys, Commands, and Conventions, iii, 15

Special Studies, 62

Special Studies and Supplementary Report, 36

Special studies, autopsy [LRAPAUDAS] option, 374

supplemental reports, 60

Supplementary Report option, 62

Supplementary report release, anat path [LRAPRS] option, 375

Supplementary Report, Anat Path [LRAPDSR], 372

Supplementary Report, Anat Path [LRAPDSR] option, 362

surgical pathology, 32

system will not accept the patient you are trying to enter, 131

## T

title (MD., Ph.D., Hematologist, etc.), 40

Titling, 305

**topography** , 37

## V

**Verify/Release Reports** , vi, viii, 27, 34, 267, 268, 270, 366, 367

Verify/release reports, anat path [LRAPR] option, 54, 348, 375

Verify/Release Reports, Anat Path [LRAPR] option has been **modified** , 270

## W

wild card, 39

WKLD SNOMED manuals, 34

**Workload** , vii, 11, 12, 21, 25, 27, 30, 180, 203, 291, 292, 294, 295, 296, 297, 310, 323

**Workload** statistics, 12

APPENDIX A

ANATOMIC PATHOLOGY

USER MANUAL NOTES FOR

PATCH LR*5.2*72

## Appendix A

### Anatomic Pathology User Manual Notes for Patch LR*5.2*72

This section of the AP manual contains a list of files, fields, new options, and options changes created by the release of patch LR*5.2*72.

Patch LR*5.2*72 enhancements allow a facility to operate Anatomic Pathology and Blood Bank modules in a multidivisional mode. All data is resident in a single primary Laboratory database, but is now identifiable by division. For those sites that are not multidivisional, but wish to have multiple accession areas in Anatomic Pathology, the changes to accommodate multidivisional functionality will also provide this functionality. A few additional changes unrelated to multidivisional functionality have also been included.

This appendix includes **only portions** of the Release Notes and Installation Guide. For additional details, including post-installation instructions for the Laboratory Information Manager regarding necessary file changes which apply to all types of facilities using the Anatomic Pathology software, consult the Laboratory LR*5.2*72 Patch Release Notes and Installation Guide.

#### Overview of Multidivisional Functionality

In order to accommodate multidivisional functionality, it is necessary to clearly identify the primary site as defined by VA FileMan, the associated divisions for which data is being entered and accessed as defined in the INSTITUTION file (#4) and the associated divisions to which individual users may be assigned as defined by the NEW PERSON file (#200), DIVISION field (#16). Based on the data dictionaries, the primary site is assigned a numeric code (3 digits) and the associated divisions are defined based on suffixes attached to that numeric code.

To minimize confusion, the term institution is used in conjunction with the word primary to indicate the parent facility at which the software and the database reside, i.e. the one with the straight numeric in INSTITUTION file (#4). The other facilities are referred to as divisions and will have a suffix appended to the numeric portion for their entry in the INSTITUTION file (#4).

For purposes of reports and other items with medicolegal implications, the name of the primary institution will be utilized; however, reference to the specific division will be included whenever possible and appropriate. For the pathology reports and the microscopic slide labels, the name of the primary institution will be used and will not reflect the division.

Whenever possible, the accession area or division to which the user is currently assigned is displayed to minimize confusion for those users who may be assigned to more than one division. For Anatomic Pathology, this functionality is utilized in conjunction with a new variable LRDICS which is called by many routines.

Because searches of data in LAB DATA file (#63) are done by accession area, and access to the accession area is limited by the DUZ(2), it will be necessary for the pathologists to be assigned to all of the divisions in order for them to have access to search all of the AP data; however this will **not** be necessary for the clinicians since the clinicians menu options allow the clinicians to access Anatomic Pathology reports for a patient, regardless of the division of the accession area for the specimen.

#### Anatomic Pathology Data Dictionary and Functionality Changes

1. The name and the input transform for LAB DATA file (#63), AUTOPSY ACC # field (#14) were **changed** from a numeric field to a free text field (5-15 characters) with a specific format determined by the input transform. The AUTOPSY ACC # field (#14) now includes the abbreviation for the accession area, concatenated with the year of the accession, concatenated with the accession number. This accommodates multidivisional functionality.
2. The name and the input transform in LAB DATA file (#63), EM subfile (#63.02), EM ACC # field (#.06) were **changed** from a numeric field to a free text field (5-15 characters) with a specific format determined by the input transform. The EM subfile (#63.02), EM ACC # field (#.06) now includes the abbreviation for the accession area, concatenated with the year of the accession, concatenated with the accession number. This accommodates both multiple accession areas within the “EM” subscript in a single division and multidivisional functionality.
3. The name and the input transform in LAB DATA file (#63), SURGICAL PATHOLOGY subfile (#63.08), SURGICAL PATH ACC # field (#.06) were **changed** from a numeric field to a free text field (5-15 characters) with a specific format determined by the input transform. The field now includes the abbreviation for the accession area concatenated with the year of the accession concatenated with the accession number. This accommodates both multiple accession areas within the “SP” subscript in a single division and multidivisional functionality.
4. The name and the input transform in LAB DATA file (#63), CYTOPATHOLOGY subfile (#63.09), CYTOPATH ACC # field (#.06) were **changed** from a numeric field to a free text field (5-15 characters) with a specific format determined by the input transform. The CYTOPATHOLOGY subfile (#63.09), CYTOPATH ACC # field (#.06) now includes the abbreviation for the accession area, concatenated with the year of the accession, concatenated with the accession number. This accommodates both multiple accession areas within the "CY" subscript in a single division and multidivisional functionality.
5. A **new** field was added to ACCESSION file (#68). The **new** DIV field (#26) is a subfield of the ACCESSION NUMBER field (#1), which is a subfield of the DATE field (#2). The **new** DIV field (#26) is a pointer to the INSTITUTION file (#4) which captures the division of the log-on person based on the DUZ(2). The data is then subsequently stored in the ACCESSION file (#68), in TEST field (#11), WKLD CODE subfield (#6), INSTITUTION subfield (#3) which has an associated “AC” cross reference.
6. The input transform was changed for LAB DATA file (#63), AUTOPSY RELEASE DATE/TIME field (#14.7) to prevent entries of a previous date/time and a future date/time.
7. The input transform was changed for EM subfile (#63.02), REPORT RELEASE DATE/TIME field (#.11) to prevent entries of a previous date/time, and a future date/time.
8. The input transform was changed for SURGICAL PATHOLOGY subfile (#63.08), REPORT RELEASE DATE/TIME field (#.11) to prevent entries of a previous date/time, and a future date/time.
9. The input transform was changed for CYTOPATHOLOGY subfile (#63.09), REPORT RELEASE DATE/TIME field (#.11) to prevent entries of a previous date/time, and a future date/time.
10. A **new** field was added to the ACCESSION file (#68). The **new** ASSOCIATED DIVISION subfile field (#1) of the ASSOCIATED DIVISION field multiple (#.091) **must** be completed even if there is only a single division. In the majority of the Anatomic Pathology menu options, the division of the user is assessed. Only those accession areas assigned to the same division as the user can be accessed.

##### Anatomic Pathology Option, Functionality, and Other Changes

1. In the Log-in, anat path [LRAPLG] option of the[LRAPL] menu, the routine was **changed** to eliminate the error caused if the user attempted to log in an autopsy on a referral patient who did not have a date of death entered. (NOIS call MEM-0595-70138)
2. By **changing** the data dictionaries for the anatomic pathology accession numbers in LAB DATA file (#63), SURGICAL PATHOLOGY subfile (#63.08), SURGICAL PATH ACC # field (#.06), EM subfile (#63.02), EM ACC # field (#.06), CYTOPATHOLOGY subfile (#63.09), CYTOPATH ACC # field (#.06), and AUTOPSY ACC # field (#14), it is now possible to have multiple accession areas for a single “AP” subscript (regardless of whether the facility is multidivisional).

**Example:** You may wish to have a separate accession area for Bone Marrows, which is associated with the LR subscript “SP”, in addition to the Surgical Pathology accession area.

**NOTE:** The abbreviation for the accession area now controls the format of the accession number on the report, instead of it being based on the entry in the Edit pathology report parameters [LRAPHDR] option.

1. In the Verify/release reports, anat path [LRAPR] option of the Verify/Release Anat Path Menu [LRAPVR] submenu has been **changed** . The date/time of the release has been limited to current time only.

**NOTE:** The ability to enter a previous date/time has been removed for all of the anatomic pathology subscripts, in an effort to increase the validity of the data.

1. The FS/Gross/Micro DX/SNOMED coding [LRAPDGS] option of the Data Entry, Anat Path [LRAPD] submenu has been **changed** . The ability to use the LAB DESCRIPTIONS file (#62.5) for rapid entry of standardized text has been expanded to include the LAB DATA file (#63), SURGICAL PATHOLOGY DIAGNOSIS field (#8), SURGICAL PATH DIAGNOSIS subfield (#1.4).
2. For the Autopsy protocol [LRAPAUPT] option in the Clinician option, Anat path [LRAPMD] menu, a variable was **reset** to eliminate the error which occurred if the option was moved to another menu. (NOIS HOU-0196-715 and LIT-0895-72013)
3. For the Prisoner of War Veterans [LRAPDPT] option in the AFIP Registries....[LRAPAFIP] submenu of the Supervisor, anat path [LRAPSUPER] menu, the problem created by Patch LR*5.2*114 in which additional patients who should not have been included in the report were included is fixed. (NOIS MAD-0596-41915)

##### Instructions for Anatomic Pathology for Multidivisional Sites and Multiple AP Accession Areas

**NOTE:** The asterisk ( ***** ) indicates changes that **must** be done before the software will run as multidivisional OR before the software will accommodate multiple AP accession areas (not necessarily immediately).

1.	Now that the LRAPFIX conversion routine has been run, make the necessary changes in the ACCESSION file (#68) in the primary site to reflect the desired setups. Do **NOT** make these changes before the conversion routine is run or the accession numbers for the previous data will not be converted properly.

**NOTE:** At this point, the AREA field (#.01) can be edited ; however, for those entries which already exist, the ABBREVIATION field (#.09) **cannot** be edited!

- If you have multiple AP accession areas in non-multidivisional site, you might have a setup such as:

**NOTE:** These are examples only; therefore, the facility IDs may **not** be correct.

AREA field (#.01): SURGICAL PATHOLOGY

LR SUBSCRIPT field (# .02): SURGICAL PATHOLOGY

ABBREVIATION field (#.09): SP

ASSOCIATED DIVISION field(#.091), subfield (#.01): Long Beach (600)

LAB DIVISION field (#.19): Anatomic Pathology

AREA field (#.01): BONE MARROW

LR SUBSCRIPT field (#.02): SURGICAL PATHOLOGY

ABBREVIATION field (#.09): BM

ASSOCIATED DIVISION field(#.091), subfield (#.01): Long Beach (600)

LAB DIVISION field (#.19): Anatomic Pathology

AREA field (#.01): CYTOLOGY

LR SUBSCRIPT field (#.02): CYTOLOGY

ABBREVIATION field (#.09): CY

ASSOCIATED DIVISION field (#.091), subfield (#.01): Long Beach (600)

LAB DIVISION field (#.19): Anatomic Pathology

AREA field (#.01): AUTOPSY

LR SUBSCRIPT field (#.02): AUTOPSY

ABBREVIATION field (#.09): AU

ASSOCIATED DIVISION field (#.091, subfield (#.01): Long Beach (600)

LAB DIVISION field (#.19): Anatomic Pathology

b.	If you are a multidivisional site, there are a variety of ways in which the file can be setup to produce the desired effect.

**NOTE:** Remember, at this point, the AREA field (#.01) can be edited; however, for entries that already exist in the ABBREVIATION field (#.09) **cannot** be edited!

**NOTE:** If you wish to use an alpha suffix to annotate the abbreviation, rather than an alpha prefix, this will not confuse the users during accessioning as the users will only be able to access those areas assigned to the appropriate division.

***WARNING:** If data is being merged from more than one site, such as is planned for those sites who are consolidating, it is absolutely **critical** that each of the anatomic pathology accession areas which existed in the site of origin be added to the site into which the data is being merged. **If this is not done, users will not be able to access that data** through the search or print options. See (#4) below for details.

(1) IF both sites process and report their own surgical path work, but only the  site does bone marrow procedures

**Comments:**

Primary site = 663 (); American  = 663A

The cum path summary and health summary show all of the accession areas, still split by subscript.

Access to enter/edit data is controlled by the assignment of divisions in the NEW PERSON file (#200).

AREA field (#.01): SEATTLE SURG PATH

LR SUBSCRIPT field (#.02): SURGICAL PATHOLOGY

ABBREVIATION field (#.09): SSP

ASSOCIATED DIVISION field (#.091), subfield(#.01): Seattle (663)

LAB DIVISION field (#.19): Anatomic Pathology

AREA field (#.01): AMER.  SURG PATH

LR SUBSCRIPT field (#.02): SURGICAL PATHOLOGY

ABBREVIATION field (#.09): ASP

ASSOCIATED DIVISION field (#.091), subfield (#.01):  (663A)

LAB DIVISION field .(#19): Anatomic Pathology

AREA field (#.01): SEATTLE BONE MARROW

LR SUBSCRIPT field (#.02): SURGICAL PATHOLOGY

ABBREVIATION field (#.09): SBM

ASSOCIATED DIVISION field (#.091), subfield (#.01): Seattle (663)

LAB DIVISION field (#.19): Anatomic Pathology

(2) IF cytology specimens are obtained at both sites, but are processed/reported at one site

**Comments:**

Accessioning can be done by each facility, but only a single number sequence will be utilized.

The division logging in the specimen will be captured and displayed on the log book. The header for the log book will be based on the division printing it, but the accession area is also included.

AREA field (#.01): CYTOLOGY

LR SUBSCRIPT field (#.02): CYTOLOGY

ABBREVIATION field (#.09): SCY

ASSOCIATED DIVISION field (#.091, subfield (#.01): Seattle (663)

ASSOCIATED DIVISION field (#.091, subfield (#.01): American  (663A)

LAB DIVISION field (#.19): Anatomic Pathology

(3) IF surgical pathology specimens are obtained at both sites, but only accessioned, processed and reported at one site,

AREA field (#.01): CYTOLOGY

LR SUBSCRIPT field (#.02): CYTOLOGY

ABBREVIATION field (#.09): TCY

ASSOCIATED DIVISION field (#.091), subfield (#.01 ): Temple

LAB DIVISION field (#.19): Anatomic Pathology

**NOTE:** It will **not** be possible to tell which division submitted the specimen because the accession area is the same and the division logging in the specimen will be captured and displayed on the log book.

(4) IF data is being merged from more than one site, such as is planned for those sites who are consolidating, it is absolutely **critical** that each of the anatomic pathology accession areas which existed in the site of origin be added to the site into which the data is being merged.

**Comments:**

Access to the accession area is controlled by the entry in the ASSOCIATED DIVISION field (#.091). If the site which is usually doing the accessioning for the new specimens received after the consolidation is **NOT** included, this accession area will not be available as a choice. Users will only be able to access the ‘OLD’ data through the search or print options if they can designate that division upon sign-on.

AREA field (#.01): WACO CYTOLOGY

LR SUBSCRIPT field .(#02): CYTOLOGY

ABBREVIATION field (#.09): WCY

ASSOCIATED DIVISION field (#.091, subfield (#.01 ): Waco

LAB DIVISION field (#.19): Anatomic Pathology

2.	For those sites, which are multidivisional, a new option has been created, (i.e. Change to new division [LRUCHGDIV]). This option allows the user to change from one associated division to another, as appropriate based on the entry(ies) for DIVISION field (#16) for that user in the NEW PERSON file (#200), without having to log out and sign back in. It appears in the Blood bank patient [LRBLP] menu; however, if the process flow and task assignments are such for anatomic pathology that users need to input or view data from more than one division, it may be appropriate to assign this option to that user's secondary menu or to one of the AP submenus.

### DATA MERGER Information for the Consolidation Sites

**NOTE:** Data merger routines will be available for both Blood Bank and Anatomic Pathology data in File 63; however, these will be issued as a s separate patch.

#### LAB DATA file (#63)

Laboratory data on the legacy systems will be available for a long period of time and all Lab data that is normally available through a health summary component IS going to be viewable on the primary system; however, for Anatomic Pathology, this is not adequate. It is imperative that historic records be available for to the pathologist, particularly when trying to make a rapid diagnosis on a specimen submitted for frozen section.

For Anatomic Pathology, this includes the following fields:

field 2 EM (subfile 63.02)

field 8 SURGICAL PATHOLOGY (subfile 63.08)

field 9 CYTOPATHOLOGY (subfile 63.09)

field 11 AUTOPSY DATE/TIME

field 12 DATE/TIME OF DEATH

field 12.1 PHYSICIAN

field 12.5 AGE AT DEATH

field 13 DATE AUTOPSY REPORT COMPLETED

field 13.01 AUTOPSY TYPIST

field 13.1 DATE FINAL AUTOPSY DIAGNOSES

field 13.5 RESIDENT PATHOLOGIST

field 13.6 SENIOR PATHOLOGIST

field 13.7 AUTOPSY TYPE

field 13.8 AUTOPSY ASSISTANT

field 14 AUTOPSY ACC #

field 14.1 LOCATION

field 14.5 SERVICE

field 14.6 TREATING SPECIALTY AT DEATH

field 14.7 AUTOPSY RELEASE DATE/TIME

field 14.8 AUTOPSY RELEASED BY

field 14.9 PROVISIONAL ANAT DX DATE

field 16, BODY HEIGHT (in)

field 17 BODY WT (lb)

field 18 LUNG,RT (gm)

field 19 LUNG,LT (gm)

field 20 LIVER (gm)

field 21 SPLEEN (gm)

field 22 KIDNEY,RT (gm)

field 23,KIDNEY,LT (gm)

field 24 HEART (gm)

field 25 BRAIN (gm)

field 25.1 PITUITARY GLAND (gm)

field 25.2 THYROID GLAND (gm)

field 25.3 PARATHYROID, LEFT UPPER (gm)

field 25.4 PARATHYROID, LEFT LOWER (gm)

field 25.5 PARATHYROID, RIGHT UPPER (gm)

field 25.6 PARATHYROID, RIGHT LOWER (gm)

field 25.7 ADRENAL, LEFT (gm)

field 25.8, ADRENAL, RIGHT (gm)

field 25.9 PANCREAS (gm)

field 25.91 TESTIS, LEFT (gm)

field 25.92 TESTIS, RIGHT (gm)

field 25.93 OVARY, LEFT (gm)

field 25.94 OVARY, RIGHT (gm)

field 26 TRICUSPID VALVE (cm)

field 27 PULMONIC VALVE (cm)

field 28 MITRAL VALVE (cm)

field 29 AORTIC VALVE (cm)

field 30 RIGHT VENTRICLE (cm

field 31 LEFT VENTRICLE (cm)

field 31.1, PLEURAL CAVITY, LEFT (ml)

field 31.2 PLEURAL CAVITY, RIGHT (ml)

field 31.3 PERICARDIAL CAVITY (ml)

field 31.4 PERITONEAL CAVITY (ml)

field 32 AUTOPSY ORGAN/TISSUE

field 32.1 AUTOPSY COMMENTS

field 32.2 CLINICAL DIAGNOSES

field 32.3 PATHOLOGICAL DIAGNOSES

field 32.4, AUTOPSY SUPPLEMENTARY REPORT

field 33 AUTOPSY SPECIMEN

field 80 AUTOPSY ICD CODE

field 83.1 MAJOR DIAGNOSTIC DISAGREEMENT

field 83.2 CLINICAL DIAGNOSIS CLARIFIED

field 99 AUTOPSY QA CODE

### Post DATA MERGER Instruction for the Consolidation Sites

The ability to merge Anatomic Pathology data from sites, which are consolidating so that critical data stored before the consolidation will still be accessible through the usual options, will be released in a separate patch. The LRAPFIX2 conversion routine will be included in this separate patch and will redo the appropriate cross-references ("ASPA", "ACYA', "AEMA", and "AAUA") for LAB DATA file (#63) for the SP, CY, EM, and AU subscript accessions.

APPENDIX B

ANATOMIC PATHOLOGY

PATCH LR*5.2*248 CHANGES

## APPENDIX B

## Anatomic Pathology Patch LR*5.2*248 Changes

The Anatomic Pathology User Manual Appendix B section contains a list of files, fields, and option changes that occurs with the installation of patch LR*5.2*248.

### LAB DATA file (#63) Changes

LAB DATA file (#63) has been **edited** to add **new** audit trail functionality. The audit trail will display changes made to the Electron Microscopy, Surgical Pathology, Cytopathology, and Autopsy Supplementary reports that are edited after previously being released for review. The modified Supplementary reports will display the name of the person modifying the report, date and time the report was modified, and the report original text at release, and currently modified text.

#### New Fields

Table : LAB DATA File (#63) Field Changes

| ## LAB DATA file (#63)  ## Modified Fields                                                                                                                                                                                                                                               | ## LAB DATA file (#63)  ## New Fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EM (Electron Microscopy) field (#2), subfile (#63.02)  SUPPLEMENTARY REPORT field (#1.2), subfile (#63.207), was  **edited**  to create four  **new**  fields. These fields are used to add the  **new**  audit trail functionality to the EM Electron Microscopy supplementary reports. | SUPPLEMENTARY REPORT MODIFIED field (#2) multiple, subfile (#63.2072). This is the date/time in which this supplementary report was modified. This information is stored for audit trail purpose. It is updated by the software and can only be modified from programmer mode.  SUPPLEMENTARY REPORT MODIFIED field (#.01). This is the date/time in which this supplementary report was modified.  PERSON MODIFYING TEXT field (#.02). This is the DUZ of the person who modified the supplementary report. It is updated by the software and can only be modified from programmer mode.  PREMODIFICATION TEXT field (#1), subfile (#6320721). This is the text of the supplementary report, as it existed before it was modified. It is updated by the software and can only be modified from programmer mode.                                                                                                                         |
| SURGICAL PATHOLOGY field (#8), subfile (#63.08)  SUPPLEMENTARY REPORT field (# 1.2), subfile (#63.817) were  **edited**  to create four  **new**  fields. These fields are used to add the  **new**  audit trail functionality to the Surgical Pathology supplementary report.           | SUPPLEMENTARY REPORT MODIFIED field (#2), subfile (#63.8172). This is the date/time in which this supplementary report was modified. This information is stored for audit trail purpose. It is updated by the software and can only be modified from programmer mode.  SUPPLEMENTARY REPORT MODIFIED field (#.01). This is the date/time in which this supplementary report was modified. This information is stored for audit trail purpose. It is updated by the software and can only be modified from programmer mode.  PERSON MODIFYING TEXT field (#.02). This is the DUZ of the person who modified the supplementary report. It is updated by the software and can only be modified from programmer mode.  PREMODIFICATION TEXT field (#1), subfile (#6381721). This is the text of the supplementary report, as it existed before it was modified. It is updated by the software and can only be modified from programmer mode. |
| CYTOPATHOLOGY field (#9), subfile (#63.09)  SUPPLEMENTARY REPORT field (#1.2), subfile (#63.907) were  **edited**  to create four  **new**  fields. These fields are used to add the  **new**  audit trail functionality to the Cytopathology supplementary reports.                     | SUPPLEMENTARY REPORT MODIFIED field (#2), sub-file (#63.9072). This is the date/time in which this supplementary report was modified. This information is stored for audit trail purpose. It is updated by the software and can only be modified from programmer mode.  SUPPLEMENTARY REPORT MODIFIED (#.01). This is the date/time in which this supplementary report was modified. This information is stored for audit trail purpose. It is updated by the software and can only be modified from programmer mode...  PERSON MODIFYING TEXT field (#.02). This is the DUZ of the person who modified the supplementary report. It is updated by the software and can only be modified from programmer mode.  PREMODIFICATION TEXT field (#1), subfile (#63.90721). This is the text of the supplementary report, as it existed before it was modified. It is updated by the software and can only be modified from programmer mode.   |
| AUTOPSY SUPPLEMENTARY REPORT field (#32.4), subfile (#63.324) was  **edited**  to create four  **new fields**  used to add the audit trail  **new**  functionality to the Autopsy supplementary report audit trail.                                                                      | SUPPLEMENTARY REPORT MODIFIED field (#2), subfile (#63.3242). This is the date/time in which this supplementary report was modified. This information is stored for audit trail purpose. It is updated by the software and can only be modified from programmer mode.  SUPPLEMENTARY REPORT MODIFIED field (#.01). This is the date/time in which this supplementary report was modified. This information is stored for audit trail purpose. It is updated by the software and can only be modified from programmer mode.  PERSON MODIFYING TEXT field (#.02) stores the user DUZ that modified an Autopsy supplementary report.  PREMODIFICATION TEXT field (#1), subfile (63.32421). This is the text of the supplementary report, as it existed before it was modified. It is updated by the software and can only be modified from programmer mode.                                                                                 |

### Anatomic Pathology Option Changes

The following Anatomic Pathology options were changed with the release of patch LR*5.2*248:

#### Enhancements

##### Supplementary Report, Anat Path [LRAPDSR] option

The Supplementary Report, Anat Path [LRAPDSR] option has been enhanced to include the audit trail **new** functionality. The audit trail information contains the name of the person editing the report, date and time the report was edited, and the original text before the report was changed. **E3R:** 3687. **NOIS:** SAM-0599-21489, DAY-0499-40904, SLC-1199-52531, SLC-1199-51746.

**NOTE:** The shaded areas shown in the following example indicate modifications made to the “Supplementary” report.

**Example:** Supplementary report

----------------------------------------------------------------------------
	MEDICAL RECORD :		SURGICAL PATHOLOGY		Pg 1
----------------------------------------------------------------------------
Submitted by: LABPROVIDER, SEVEN	Date obtained: NOV 21, 1990
----------------------------------------------------------------------------
Specimen:
SKIN
----------------------------------------------------------------------------
Brief Clinical History:
	Scaly eruption on extensor surfaces of forearms.
----------------------------------------------------------------------------
Preoperative Diagnosis:
	Psoriasis
----------------------------------------------------------------------------
Operative Findings:
	Psoriasis
-----------------------------------------------------------------------------
Postoperative Diagnosis:
	Same					Surgeon/physician: LABPROVIDER, SEVEN

============================================================================
					  PATHOLOGYY REPORT
Laboratory: R5ISC						Accession No. SP90 23
----------------------------------------------------------------------------
Gross description:		 Pathology Resident: LABPROVIDER6, FOUR
	3mm punch biopsy of skin

Microscopic exam/diagnosis:

Skin and subjacent tissue showing parakeratosis, elongation and blunting of rate ridges, and neutrophilic abscesses in the parakeratotic layer consistent with psoriasis.

Supplementary Report:
	Date: NOV 21, 1990 11:00

*** MODIFIED **REPORT** ***

(Last modified: NOV 21, 1990 11:00 typed by LABUSER, ONE

This is an example of a supplementary report. It can be used to report

the results of re-cuts, special stains, etc.

Date: NOV 21, 1990 11:01
	There can be more than one supplementary report.
CONSULTATION AFIP#123456789 Date: NOV 21, 1990
SKIN
This is a description of the findings of EM study.
----------------------------------------------------------------------------
										(End of report)
									rg| Date NOV 21, 1990
----------------------------------------------------------------------------

LABPATIENT, SEVEN							STANDARD FORM 515
ID:000-00-0000 SEX:M DOB:5/8/16 AGE 72			LOC:1A
									LABPROVIDER, SEVEN

##### Autopsy supplementary report [LRAPAUSR] option

The Autopsy supplementary report [LRAPAUSR] option has been **enhanced** to include an audit trail. The audit trail information contains the name of the person editing the report, date and time the report was edited, the report original text and currently modified text. **E3R:** 3687. **NOIS:** SAM-0599-21489, DAY-0499-40904, SLC-1199-52531, SLC-1199-51746.

**NOTE:** The shaded areas shown in the following example indicate modifications made to the “Autopsy Supplementary” report.

**Example:** Autopsy Supplementary report

----------------------------------------------------------------------------

CLINICAL RECORD|				AUTOPSY SUPPLEMENTARY REPORT		Pg 1

----------------------------------------------------------------------------

Date died: APR 26, 1990			|Autopsy date:APR 26, 1990 12:55
Resident: LABPROVIDER, ONE		|FULL AUTOPSY Autopsy No. A90 1
-----------------------------------------------------------------------------

SUPPLEMENTARY REPORT DATE: AUG 10, 1990 10:43

*** MODIFIED **REPORT** ***

(Last modified: APR 26, 1990 12:00		typed by DUCK,JOE

This is an autopsy supplementary report. It is separate from the protocol because there are many instances where the autopsy can be
signed out within the sixty day time limit but the brain exam may not be ready until after the deadline is past. The protocol can be sent to the patient's chart and the supplementary report can later follow without having to reprint the entire autopsy protocol.

SUPPLEMENTARY REPORT DATE: AUG 10, 1990 12:35

There can be as many supplementary reports as desired.

----------------------------------------------------------------------------

Pathologist: LABPROVIDER, THREE				jg| Date SEP 12, 1990

----------------------------------------------------------------------------

R5ISC								AUTOPSY SUPPLEMENTARY REPORT

LABPATIENT, FIVE	000-00-0005		SEX:M		DOB: FEB 1, 1901

MEDICINE		LABPROVIDER, ONE			AGE AT DEATH: 51

#### Modifications

##### Show List of Accessions for a Patient [LRUPT] option

The Show list of accessions for a patient [LRUPT] option has been **modified** with the following changes:

This option now displays the accession number when the Autopsy section is selected to generate a report.

- Some tests were missing on the report for accessions in which the user enters a collection date for the previous year but the order date is in the current year. This option was modified to use the correct year so that the missing tests will now appear. **NOIS:** AUG-0398-32638, SYR-0193-10004.

**NOTE:** The shaded areas shown in the following example indicate the modifications made in the ‘Show list of accessions for a patient [LRUPT] option”.

Example of report for Chemistry:

Select Anatomic pathology Option: **I** Inquiries, anat path

Select Inquiries, anat path Option: **PA** Show list of accessions for a patient

Select ACCESSION AREA: **CH** CHEMISTRY

Select Patient Name: LABPATIENT9, THREE	08-18-27	000000093
LABPATIENT2, THREE ID: 000-00-0023 Physician: LABPROVIDER, SEVEN

AGE: 63 DATE OF BIRTH: AUG 18, 1927
PATIENT LOCATION: 1A// **&lt;Enter&gt;** Is this the patient ? YES// **&lt;Enter&gt;** (YES)

CHEMISTRY      LABPATIENT9, THREE ID:000-00-0093  TESTS ORDERED

Spec Date/time Acc #      Site/specimen       Tests

01/15/93 10:11 CH 0115 9    SERUM           1)CALCIUM

12/26/92 11:00 CH 0115 8    SERUM           1)GLUCOSE

11/13/92 16:14 CH 1113 6    SERUM           1)GLUCOSE

Example of report for Autopsy:

Select Anatomic pathology Option: I Inquiries, anat path

Select Inquiries, anat path Option: PA Show list of accessions for a patient

Select ACCESSION AREA: AU AUTOPSY

Select Patient Name: LABPATIENT9, FOUR

LABPATIENT9, FOUR ID: 000-00-0094 Physician: LABPROVIDER6, FIVE.

DIED FEB 5, 1996

Is this the patient ? YES//  (YES)

AUTOPSY       LABPATIENT9, FOUR ID: 000-00-0094

Autopsy date/time Autopsy #

JUL 31, 1997      10

##### Modify anat path gross/micro/dx/frozen section [LRAPM] option

The Modify anat path gross/micro/dx/frozen section [LRAPM] option was **modified** with the following changes:

- This option was **modified** to allow queuing and printing of a “COMPLETED” report when the patient is a male.
- This option was **modified** to prevent a report from becoming “UNRELEASED” even though no changes were made to the report. **NOIS:** BHS-0600-12155.

##### Verify/Release Reports, Anat Path [LRAPR] option

The Verify/Release Reports, Anat Path [LRAPR] option has been **modified** with the following changes:

- The REPORT RELEASE DATE/TIME// prompt has been changed from allowing entry of a future date and time response to a Release report? // YES or NO question response. If the user response is YES, the current date and time stored.
    - The Autopsy verified/released report previously required using the @ sign to unrelease a report. This option was changed to require a YES/NO prompt response to unrelease a report. **NOIS:** REN-0197-61357

**NOTE:** Changes made to the Verify/Release Reports, Anat [LRAPR] option is indicated in the shaded areas of the following example.

##### Example 1: Release of Surgical Report

Select Verify/release menu, anat path Option: **RR** Verify/release reports, anat path

RELEASE PATHOLOGY REPORTS

Select ANATOMIC PATHOLOGY SECTION: SUR SURGICAL PATHOLOGY

SURGICAL PATHOLOGY (SUR)

Data entry for 1994 ? YES// **&lt;Enter&gt;** (YES)

Select Accession Number/Pt name: **7** for 1994

LABPATIENT1, TEN ID: 000-00-0110

Release report? NO// YES **&lt;Enter&gt;**

Report released...

Select Accession Number/Pt name: **&lt;Enter&gt;**

**NOTE:** If an attempt is made to release a report that has already been released, the following is displayed.

Report released JUN 26, 1994@16:52:57 by LABPROVIDER6, SIX

Select Accession Number/Pt name:

##### Example 2: Release of ‘Autopsy’ report

Select Anatomic pathology Option: **V** Verify/release menu, anat path

Select Verify/release menu, anat path Option: **RR** Verify/release reports, anat path

RELEASE PATHOLOGY REPORTS

Select ANATOMIC PATHOLOGY SECTION: **au** AUTOPSY

Data entry for 1992 ? YES// **&lt;Enter&gt;** (YES)

Select Accession Number/Pt name: **5** for 1992

LABPATIENT, FOUR  ID: 000-00-0004

Release report? NO// **YES&lt;Enter&gt;**

Report released...

Select Accession Number/Pt name: **&lt;Enter&gt;**

Select Anatomic pathology Option: V Verify/release menu, anat path

RR   Verify/release reports, anat path

RS   Supplementary report release, anat path

LU   List of unverified pathology reports

Select Verify/release menu, anat path Option: RR Verify/release reports, anat path

RELEASE PATHOLOGY REPORTS

Select ANATOMIC PATHOLOGY SECTION: AU AUTOPSY

AUTOPSY (AU)

Data entry for 1992 ? YES// **&lt;Enter&gt;** (YES)

Select Accession Number/Pt name: 1 for 1992

LABPATIENT8, EIGHT. ID: 000-00-0088

Report released SEP 18, 1992@13:11:20 by SMITH,DOE

Unrelease report? NO// YES **&lt;Enter&gt;**

Report unreleased...

##### Enter old anat path records [LRAPOLD] option

The Enter old anat path records [LRAPOLD] option used for entering certain pathology historical data was **modified** to correct an undefined variable error. **NOIS:** OKL-0799-72578, FAV-0999-71182, AUG-1299-32707, ANN-0200-42620, WRJ-0500-10974.

##### Log-in, anat path [LRAPLG] option

The Log-in, anat path [LRAPLG] option has been **modified** with the following changes:

A five second time-out has been put on record locking to prevent system hang time when logging-in with this option. **NOIS:** MUS-0395-70386, SHR-0595-70238.

FileMan look-up call (DIE) will not store three question marks (???) as data for patient location. The three question marks (???) have been replaced with UNKNOWN, which is FileMan compatible. **NOIS:** DUB-0895-32241, LEB-0899-22335, SAM-0499-22281, WRJ-0298-11480, SAM-0598-20421.

##### Autopsy protocol/supplementary report [LRAPAUPT] option

The autopsy protocol/supplementary Report [LRAPAUPT] option has been **modified** to correct the following:

- Printing of unnecessary form feeds for Autopsy Protocol and Supplementary reports. **NOIS:** WPB-0696-30073, IND-1097-41646.

The Autopsy Protocol report header and footer have been reformatted for better readability. Labels have been added before the physician and patient names (i.e., “Physician:” and “Patient:”)

**NOTE:** The shaded areas in the following example display changes made to the footer.

----------------------------------------------------------------------------

CLINICAL RECORD |         AUTOPSY PROTOCOL        Pg 1

----------------------------------------------------------------------------

Date died: DEC 1, 1992         	| Autopsy date: DEC 1, 1992

Resident:             		| FULL AUTOPSY Autopsy No. A92 5

----------------------------------------------------------------------------

Clinical History

1. Left CVA 2. Recurrent UTI 3. Aspiration pneumonia

----------------------------------------------------------------------------

Anatomic Diagnoses

PROVISIONAL GROSS ANATOMIC PATHOLOGICAL DIAGNOSIS: (Subject to revision)

1. Bilateral pulmonary edema with bilateral pleural effusion (500cc)

a. Organizing pneumonia right lung

b. Pericardial effusion

c. Calcified granuloma, left upper lobe

2. a. Moderate arteriosclerosis of abdominal aorta

b. Cardiomegaly with LVH

3. Bilateral granular kidneys (arterionephrosclerosis)

a. 3 x 2 cm cyst left kidney

b. 0.3 x 0.3 cm hemorrhagic cysts, left kidney

c. Hemorrhagic bladder mucosa

4. Choletlithiasis with 25 stones (yellow, 0.5 to 1 cm)

a. Congested liver parenchyma

b. Diverticulosis, colon

----------------------------------------------------------------------------

Pathologist: LABPROVIDER, THREE            wty| Date DEC 1, 1992

----------------------------------------------------------------------------

CIOFO								AUTOPSY PROTOCOL

Patient: LABPATIENT, FOUR	000-00-0004	SEX:M		DOB:DEC 18, 1992

Bon-AHMED/OPC		Physician: LABPROVIDER6, TWO		AGE AT DEATH: 75

##### Clinical Hx/Gross Description/FS [LRAPDGD] option

The Clinical Hx/Gross Description/FS [LRAPDGD] option has been **modified** to correct re-entering a patient’s name at the Accession Number/Patient Name prompt and a second prompt within this option. The option now performs the patient name lookup at the first prompt, thereby eliminating the need for the second prompt.

##### FS/Gross/Micro/Dx [LRAPDGM] option

The FS/Gross/Micro/Dx [LRAPDGM] option has been **modified** to correct re-entering a patient’s name at the Accession Number/Patient Name prompt and a second prompt within this option. The option now performs the patient name lookup at the first prompt, thereby eliminating the need for the second prompt.

##### FS/Gross/Micro/Dx/SNOMED Coding [LRAPDGS] option

The FS/Gross/Micro/Dx/SNOMED Coding [LRAPDGS] option has been **modified** to correct re-entering a patient’s name at the Accession Number/Patient Name prompt and a second prompt within this option. The option now performs the patient name lookup at the first prompt, thereby eliminating the need for the second prompt.

##### FS/Gross/Micro/Dx/ICD Coding [LRAPDGI] option

The FS/Gross/Micro/Dx/ICD Coding [LRAPDGI] option has been **modified** to correct re-entering a patient’s name at the Accession Number/Patient Name prompt and a second prompt within this option. The option now performs the patient name lookup at the first prompt, thereby eliminating the need for the second prompt.

##### Supplementary Report, Anat Path [LRAPDSR] option

The Supplementary Report, Anat Path [LRAPDSR] option has been **modified** to correct re-entering a patient’s name at the Accession Number/Patient Name prompt and a second prompt within this option. The option now performs the patient name lookup at the first prompt, thereby eliminating the need for the second prompt.

##### Spec Studies-EM;Immuno;Consult;Pic, Anat Path [LRAPDSS] option

The Spec Studies-EM;Immuno;Consult;Pic, Anat Path [LRAPDSS] option has been **modified** to correct re-entering a patient’s name at the Accession Number/Patient Name prompt and a second prompt within this option. The option now performs the patient name lookup at the first prompt, thereby eliminating the need for the second prompt.

##### Provisional anatomic diagnoses [LRAPAUPAD] option

The Provisional anatomic diagnoses [LRAPAUPAD] option has been **modified** to correct re-entering a patient’s name at the Accession Number/Patient Name prompt and a second prompt within this option. The option now performs the patient name lookup at the first prompt, thereby eliminating the need for the second prompt.

##### Autopsy protocol [LRAPAUDAP] option

The Autopsy protocol [LRAPAUDAP] option has been **modified** to correct re-entering a patient’s name at the Accession Number/Patient Name prompt and a second prompt within this option. The option now performs the patient name lookup at the first prompt, thereby eliminating the need for the second prompt.

##### Autopsy protocol &amp; SNOMED coding [LRAPAUDAB] option

The Autopsy protocol &amp; SNOMED coding [LRAPAUDAB] option has been **modified** to correct re-entering a patient’s name at the Accession Number/Patient Name prompt and a second prompt within this option. The option now performs the patient name lookup at the first prompt, thereby eliminating the need for the second prompt.

##### Autopsy protocol &amp; ICD coding [LRAPAUDAA] option

The Autopsy protocol &amp; ICD coding [LRAPAUDAA] option has been **modified** to correct re-entering a patient’s name at the Accession Number/Patient Name prompt and a second prompt within this option. The option now performs the patient name lookup at the first prompt, thereby eliminating the need for the second prompt.

##### Final autopsy diagnoses date [LRAPAUFAD] option

The Final autopsy diagnoses date [LRAPAUFAD] option has been **modified** to correct re-entering a patient’s name at the Accession Number/Patient Name prompt and a second prompt within this option. The option now performs the patient name lookup at the first prompt, thereby eliminating the need for the second prompt.

##### Autopsy supplementary report [LRAPAUSR] option

The Autopsy supplementary report [LRAPAUSR] option has been **modified** to correct re-entering a patient’s name at the Accession Number/Patient Name prompt and a second prompt within this option. The option now performs the patient name lookup at the first prompt, thereby eliminating the need for the second prompt.

##### Special studies, autopsy [LRAPAUDAS] option

The Special studies, autopsy [LRAPAUDAS] option has been **modified** to correct re-entering a patient’s name at the Accession Number/Patient Name prompt and a second prompt within this option. The option now performs the patient name lookup at the first prompt, thereby eliminating the need for the second prompt.

##### SNOMED coding, anat path [LRAPX] option

The SNOMED coding, anat path [LRAPX] option has been **modified** to correct re-entering a patient’s name at the Accession Number/Patient Name prompt and a second prompt within this option. The option now performs the patient name lookup at the first prompt, thereby eliminating the need for the second prompt.

##### ICD coding, anat path [LRAPICD] option

The ICD coding, anat path [LRAPICD] option has been **modified** to correct re-entering a patient’s name at the Accession Number/Patient Name prompt and a second prompt within this option. The option now performs the patient name lookup at the first prompt, thereby eliminating the need for the second prompt.

##### Modify anat path gross/micro/dx/frozen section [LRAPM] option

The Modify anat path gross/micro/dx/frozen section [LRAPM] option has been **modified** to correct re-entering a patient’s name at the Accession Number/Patient Name prompt and a second prompt within this option. The option now performs the patient name lookup at the first prompt, thereby eliminating the need for the second prompt.

##### Verify/release reports, anat path [LRAPR] option

The Verify/release reports, anat path [LRAPR] option has been **modified** to correct re-entering a patient’s name at the Accession Number/Patient Name prompt and a second prompt within this option. The option now performs the patient name lookup at the first prompt, thereby eliminating the need for the second prompt.

##### Supplementary report release, anat path [LRAPRS] option

The Supplementary report release, anat path [LRAPRS] option has been **modified** to correct re-entering a patient’s name at the Accession Number/Patient Name prompt and a second prompt within this option. The option now performs the patient name lookup at the first prompt, thereby eliminating the need for the second prompt.

##### Print path gross/micr/dx/fr.sect modifications [LRAPQAM] option

The Print path gross/micr/dx/fr.sect modifications [LRAPQAM] option was **modified** to include report changes in the ‘Supplementary’ reports modified after their release. **E3R** : 3687. **NOIS:** SAM-0599-21489, DAY-0499-40904, SLC-1199-52531, SLC-1199-51746.

##### Print path modifications [LRAPMOD] option

The Print path modifications [LRAPMOD] option has been **modified** to print the audit trail new information for supplementary reports. The audit trail information contains the name of the person editing the report, date and time the report was edited, and the original text before the report was changed. **E3R:** 3687. **NOIS:** SAM-0599-21489, DAY-0499-40904, SLC-1199-52531, SLC-1199-51746.

**NOTE:** The shaded area in the following examples display changes made in the report.

##### Example: Print Pathology Report Modifications

Select Supervisor, anat path Option: **MR** Print path modifications

Print pathology report modifications

Select ANATOMIC PATHOLOGY section: **SP** SURGICAL PATHOLOGY

Select Patient Name: LABPATIENT1, TEN: 000000110 NO   NSC VETERAN

LABPATIENT1, TEN: 000-00-0110 Physician: LABPROVIDER4, THREE

AGE: 72 DATE OF BIRTH: FEB 1, 1922

Ward on Adm: 1 EAST Service: MEDICINE

Adm Date: APR 8, 1993 10:53 Adm DX: ACCIDENT

Present Ward: 1 EAST          MD:

Specimen(s)       Count #  Accession #  Date Obtained

( 1)      7    AUG 25, 1994 not verified

LEFT LEG

( 2)      6    AUG 25, 1994 not verified

left hip chip

( 3)      2    AUG 24, 1994

PROSTATE CHIPS

Choose Count #(1-3): **3**

Accession #: 2  Date Obtained: AUG 24, 1994

Select Print Device: *[Enter Print Device Here]*

-----------------------------------------------------------------------------

MEDICAL RECORD |          SURGICAL PATHOLOGY        Pg 1

-----------------------------------------------------------------------------

Submitted by: LABPROVIDER4, THREE        Date obtained: AUG 24, 1994

-----------------------------------------------------------------------------Specimen (Received AUG 24, 1994 10:37):

PROSTATE CHIPS

-----------------------------------------------------------------------------

Brief Clinical History:

Nocturia and difficulty voiding urine.

-----------------------------------------------------------------------------Preoperative Diagnosis:

same.

-----------------------------------------------------------------------------

Operative Findings:

same.

-----------------------------------------------------------------------------

Postoperative Diagnosis:

same.

Surgeon/physician: LABPROVIDER4, FOUR

=============================================================================

PATHOLOGY REPORT

Laboratory: VAMC                   Accession No. SP 94 2

-----------------------------------------------------------------------------

Pathology Resident: LABPROVIDER1, FIVE

Frozen Section:

Basal cell .

Gross Description:

Specimen consists of 5 grams of prostate gland tissue.

Microscopic exam/diagnosis:

*** MODIFIED REPORT ***

(Last modified: AUG 27, 1994 17:30 typed by PEREZ,ELSIE)

Date modified:AUG 27, 1994 17:19 typed by PEREZ,ELSIE

Glomerular basement membranes are thickenedd and there is increased

mesangial matrix.

Date modified:AUG 27, 1994 17:30 typed by PEREZ,ELSIE

Glomerular basement membranes are thickenedd and there is increased

mesangial matrix. Also present are small prostatic infarts and foci

of squamous metaplasia.

==========Text below appears on final report==========

Glomerular basement membranes are thickenedd and there is increased

LABPROVIDER4, FOUR                 ec | Date AUG 25, 1994

LABPATIENT1, TEN                 STANDARD FORM 515

ID:000-00-0110 SEX:F  DOB:2/1/22  AGE:72   LOC:1 EAST

ADM:APR 8, 1993 DX:ACCIDENT           LABPROVIDER4, THREE

----------------------------------------------------------------------------

MEDICAL RECORD |          SURGICAL PATHOLOGY       Pg 2

----------------------------------------------------------------------------

PATHOLOGY REPORT

Laboratory: VAMC                   Accession No. SP 94 2

-----------------------------------------------------------------------------

mesangial matrix. Also present are small prostatic infarts and foci

of squamous metaplasia. Another small infarts and foci of squamous

metaplasia.

Supplementary Report:

Date: AUG 26, 1994 18:09

This is an example of a supplementary report. It can be used to report

the results of recuts.

Date: AUG 26, 1994 18:10

***MODIFIED REPORT***

(Last modified: AUG 26, 1994 18:19 typed by DOE,SUE)

Date modified: AUG 26, 1994 18:19 typed by DOE,SUE

This is another supplementary report.

==========Text below appears on final report==========

This is another supplementary report. When the supplementary report was

released, this line was added to the report.

CONSULTATION AFIP#123456789 Date: AUG 26, 1994 18:17

PROSTATIC FASCIA

This is an example of a consultation sent to the AFIP.

SNOMED code(s):

T-18969: PROSTATIC FASCIA

P-Y333 : ADMINISTRATION OF MEDICATION, EMERGENCY

----------------------------------------------------------------------------

(End of report)

LABPROVIDER4, FOUR                ec | Date AUG 25, 1994

LABPATIENT1, TEN                      STANDARD FORM 515

ID:000-00-0110 SEX:M DOB:2/1/22   AGE:72    LOC:1 EAST

ADM:APR 8, 1993 DX:ACCIDENT           LABPROVIDER4, THREE

##### Print final path reports by accession # [LRAPFICH] option

The Print final path reports by accession # [LRAPFICH] option has been **modified** to correct the following:

- The Print final path reports by accession # [LRAPFICH] option has been **modified** to correct printing of unnecessary form feeds for the Final Pathology Report by Accession Number. **NOIS:** WPB-0696-30073, IND-1097-41646
- The Print final path reports by accession # [LRAPFICH] option has been **modified** to display audit trail new information on the supplementary report. **E3R:** 3687. **NOIS:** SAM-0599-21489, DAY-0499-40904, SLC-1199-52531, SLC-1199-51746

##### Print all reports on queue [LRAP PRINT ALL ON QUEUE] option

The Print all reports on queue [LRAP PRINT ALL ON QUEUE] option has been **modified** as follows:

Corrected the printing of unnecessary form feeds and accession number that are entered to long for Anatomic Pathology reports (i.e., Surgical Pathology, Cytopathology and Electron Microscopy Preliminary, Final and Supplementary, and Autopsy Protocol and Supplementary reports). **E3R:** 3687. **NOIS:** WPB-0696-30073, IND-1097-41646 NOIS: SAM-0599-21489, DAY-0499-40904, SLC-1199-52531, SLC-1199-51746, MAR-0398-22377.

The Autopsy Protocol report header and footer have been reformatted for better readability. Labels have been added before the physician and patient names (i.e., “Physician:” and “Patient:”).

- The option has been modified to display audit information on supplementary reports. **E3R:** 3687. **NOIS:** SAM-0599-21489, DAY-0499-40904, SLC-1199-52531, SLC-1199-51746

**NOTE:** The shaded areas display changes made in the ‘Autopsy Protocol Report’ HEADER and FOOTERS.

Select Anatomic pathology Option: **P** Print, anat path

Select Print, anat path Option: **PQ** Print all reports on queue

Select ANATOMIC PATHOLOGY section: **AU** AUTOPSY

1. Autopsy protocols

2. Autopsy supplementary reports

Select 1 or 2: **1&lt;Enter&gt;**

Autopsy Protocols

(D)ouble or (S)ingle spacing of report(s): **S&lt;Enter&gt;**

Print weights, measures and coding (if present): ? YES// **&lt;Enter&gt;** (YES)

Save protocol list for reprinting ? NO// **Y** (YES)

Select Print Device: *[Enter Print Device Here]*

**Example 4:** Change in Prompts if you Select the Autopsy Section *continued*

---------------------------------------------------------------------------

CLINICAL RECORD |         AUTOPSY PROTOCOL      Pg 1

---------------------------------------------------------------------------

Date died: DEC 1, 1992         | Autopsy date: DEC 1, 1992

Resident:                | FULL AUTOPSY Autopsy No. A92 5

---------------------------------------------------------------------------

Clinical History

1. Left CVA 2. Recurrent UTI 3. Aspiration pneumonia 4. Chronic renal failure

---------------------------------------------------------------------------

Anatomic Diagnoses

PATHOLOGICAL DIAGNOSIS:

1. Bilateral pulmonary edema with bilateral pleural effusion (500cc)

a. Organizing pneumonia right lung

b. Organizing pneumonia, right lung, with acute bronchitis

c. Calcified granuloma, left upper lobe (gross)

d. Emphysema (bilateral) and focal atelectasis (left)

2. a. Moderate arteriosclerosis of abdominal aorta

b. Cardiomegaly(480 gm) with left ventricular hypertrophy

c. Pericardial effusion with chronic peritonitis

d. Focal interstitial fibrosis

3. Bilateral granular kidneys with severe arterial and

arterionephrosclerosis and mesangeal thickening

a. 3 x 2 cm cyst left kidney

b. 0.3 x 0.3 cm hemorrhagic cysts, left kidney

c. Hemorrhagic bladder mucosa

d. Hemorrhagic bladder mucosa with chronic cystitis and prostatic

urethritis

4. Choletlithiasis with 25 stones (yellow, 0.5 to 1 cm)

a. Congested liver parenchyma

b. Diverticulosis, colon

GROSS BRAIN DIAGNOSIS: No pathologic diagnosis MICROSCOPIC BRAIN

DIAGNOSIS: pending - supplemental report to be issued.

CLINICO-PATHOLOGICAL CORRELATION

Patient was an

-----------------------------------------------------------------------------

Pathologist: LABPROVIDER, THREE          lh| Date DEC 2, 1992

----------------------------------------------------------------------------

ISC								AUTOPSY PROTOCOL

Patient: LABPATIENT, FOUR		000-00-0004		SEX: M	DOB: DEC 18, 1925

BON-AHMED/OPC		Physician: LABPROVIDER2, TWO	AGE AT DEATH:66

DEC 2, 1992  08:10	 ISC						Pg: 2

ANATOMIC PATHOLOGY

----------------------------------------------------------------------------

LABPATIENT, FOUR		000-00-0004		DOB:DEC 18, 1925

Acc #: 5				AUTOPSY DATA	Age: 66

Date/time Died						Date/time of Autopsy DEC 1, 199 **2** FULL AUTOPSY	DEC 1, 1992

Resident: LABPROVIDER6, SEVEN				Senior: LABPROVIDER, THREE

SNOMED code(s):

T-28000: lung

M-36660: edema, lymphatic

M-32800: emphysema

M-49000: fibrosis

T-29000: pleura

M-36330: effusion, serosanguineous

T-28100: right lung

M-40000: inflammation

T-28600: left upper lobe of lung

M-44000: inflammation, granulomatous

T-71000: kidney

M-52200: arteriolosclerosis

T-57000: gallbladder

M-30010: lithiasis

T-56000: liver

M-36100: congestion

T-67000: colon

M-32710: diverticulosis

T-42000: aorta

M-52000: arteriosclerosis

T-33010: myocardium

M-71000: hypertrophy

------------------------------------------------------------------------------

Pathologist: LABPROVIDER, THREE            lh | Date DEC 2, 1992

------------------------------------------------------------------------------

ISC									AUTOPSY PROTOCOL

Patient: LABPATIENT, FOUR		000-00-0004		SEX: M	DOB: DEC 18, 1925

MEDICINE			Physician: LABPROVIDER2, TWO		AGE AT DEATH:66

##### Print single report only [LRAP PRINT SINGLE] option

The Print single report only [LRAP PRINT SINGLE] option has been **modified** as follows:

Corrected the printing of unnecessary form feeds and accession number that are entered to long for Anatomic Pathology reports (i.e., Surgical Pathology, Cytopathology and Electron Microscopy Preliminary, Final and Supplementary, and Autopsy Protocol and Supplementary reports). **E3R:** 3687, SAM-0599-21489, DAY-0499-40904, SLC-1199-52531, SLC-1199-51746. **NOIS:** WPB-0696-30073, IND-1097-41646, MAR-0398-22377.

The Autopsy Protocol report header and footer have been reformatted for better readability. Labels have been added before the physician and patient names (i.e., “Physician:” and “Patient:”).

- The option has been **modified** to display audit trail new information on supplementary reports. **E3R:** 3687. **NOIS:** SAM-0599-21489, DAY-0499-40904, SLC-1199-52531, SLC-1199-51746

#### Laboratory Option Modifications

##### Accession List by Date [LRUPAD]

The Accession List by Date [LRUPAD] option report is incorrectly displaying a numeric value that has no meaning to the user in the ‘Tech’ column. The option has been **modified** to print the initials of the technologist who verified the report. **NOIS:** ALN-0395-10067

##### Lab orders by collection type [LRRP5] option

The Lab orders by collection type [LRRP5] option was **modified** to resolve the reporting of incorrect tests as being ordered if a particular test has a SYNONYM field (#2) multiple, Synonym sub-file (#60.1), of the LABORATORY TEST file (#60) that is identical to the internal entry number (IEN) of the look-up test. The correct tests (instead of the synonyms) are now displayed on the report. **NOIS:** IND-0797-40657.