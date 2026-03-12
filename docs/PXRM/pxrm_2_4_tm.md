---
app_name: 'Registry: Airborne Hazard Open Burn Pit (AHOBPR) (PXRM)'
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: null
doc_type: technical-manual
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-11'
is_base: false
is_change_pages: false
library_max_patch: null
package_id: PXRM
patch: null
patch_gap: null
section: ''
source_file: pxrm_2_4_tm.docx
status: draft
title: pxrm 2 4 tm.docx
---

<!-- image -->

**Clinical Reminders**

## TECHNICAL MANUAL

### July 2014

Product Development


## Table of Contents

Table of Contents	ii

Revision History	iv

Introduction	5

Clinical Reminders ICD-10 Update Project	5

Purpose of This Guide	7

Our Target Audience	7

Related Documentation and websites	7

Implementation and Maintenance	9

Implementation and Maintenance	10

Clinical Reminders Index Global	10

Implementation &amp; Maintenance	10

Clinical Reminders Managers Menu	10

Routine Information	11

Files and Globals List	12

File Descriptions	13

File Descriptions	14

File Descriptions	16

File Descriptions	17

File Descriptions	18

File Descriptions	19

Exported Menus and Options	22

Options not on a menu	24

Archiving and Purging	25

External Relations	26

External Relations	27

External Relations	28

Internal Relations	30

Package-Wide Variables	31

7/23/2014	Clinical Reminders V. 2.26 Technical Manual	ii

Generating Online Documentation	32

Generating Online Documentation	33

Generating Online Documentation	34

Generating Online Documentation	35

How to Generate Online Documentation	36

Glossary	37

Glossary	38

Glossary	39

Glossary	40

APPENDIX A: Security Guide	41

APPENDIX A: Security Guide, cont’d	42

Option not on a menu	42

Security Key	42

APPENDIX A: Security Guide, cont’d	44

File Security	44

Appendix B: Computed Expressions	45

**Revision History**

| **Revision Date**   | **Page(s)**   | **Description**                            | **Project Manager**   | **Author**   |
|---------------------|---------------|--------------------------------------------|-----------------------|--------------|
| July 2014           | various       | Updates based on reviews                   | REDACTED              | REDACTED     |
| May 2014            | Page 24, 42   | Added description of options not on a menu | REDACTED              | REDACTED     |
| April 2014          | Page 19       | Changes to file 811.2 made by PXRM*2*26    | REDACTED              | REDACTED     |
| April 2014          | Page 42       | Info about security key added              | REDACTED              | REDACTED     |
| March 2014          | throughout    | Changes made by patch 26                   | REDACTED              | REDACTED     |
| June 2011           | Page 13       | Changes made in patch 18                   | REDACTED              | REDACTED     |
| June 2006           | Page 13       | Changes to files made in patch 4           | REDACTED              | REDACTED     |
| May 2006            | Throughout    | Patch 4 changes                            | REDACTED              | REDACTED     |

## Introduction

#### Overview

The International Classification of Diseases (ICD) is a clinical coding system developed, monitored, and copyrighted by the World Health Organization (WHO). In the United States (US), the National Center for Health Statistics (NCHS), part of the Centers for Medicare and Medicaid Services (CMS), is the agency responsible for overseeing of the clinical modification to the ICD code set.

On January 16, 2009, the Centers for Medicare &amp; Medicaid Services (CMS) released a final rule for replacing the 30-year-old ICD-9-CM code set with International Classification of Diseases, Tenth Revision, Clinical Modification (ICD-10-CM) and International Classification of Diseases, Tenth Revision, Procedure Coding System (ICD- 10-PCS) with dates of service, or date of discharge for inpatients, that occur on or after the industry activation date. The classification system consists of more than 68,000 codes, compared to approximately 13,000 ICD-9-CM codes. There are nearly 87,000 ICD-10-PCS codes, while ICD-9-CM has nearly 3,800 procedure codes. Both systems also expand the number of characters allotted from five and four respectively to seven alpha-numeric characters. This value does not include the decimal point, which follows the third character for the ICD-10-CM code set. There is no decimal point in the ICD-10- PCS code set. These code sets have the potential to reveal more about quality of care, so that data can be used in a more meaningful way to better understand complications, better design clinically robust algorithms, and better track the outcomes of care. ICD-10-CM also incorporates greater specificity and clinical detail to provide information for clinical decision-making and outcomes research.

**VA’s Transition to ICD-10:** Implementation of ICD-10-CM and PCS is an immense undertaking, requiring system and business changes throughout all HIPAA-covered entities of the health care industry, including the U.S. Department of Veterans Affairs (VA). All inpatient discharges and outpatient encounter dates on or after the compliance date will require ICD-10 codes as the standard code set for recording and reporting diagnosis and inpatient procedures. This transition will impact Information Technology (IT) systems, secondary data stores, forms and business processes and stakeholders at all levels of the organization.

#### Clinical Reminders ICD-10 Update Project

In order to meet the compliance date, the Clinical Reminders ICD-10 Update project is updating the Clinical Reminders application to allow the use of ICD-10 codes. A very general approach has been taken, wherein Clinical Reminders taxonomies are being restructured to be Lexicon-based instead of pointer-based. This allows the use of any coding system supported by the Lexicon package. In addition to adding ICD-10 codes, SNOMED CT codes are being added. With the release of CPRS 29, SNOMED CT codes can be collected by Problem List and Clinical Reminders will be able to search for them.

**Patches in this project build PXRM*2.0*26**

This build changes Clinical Reminders taxonomies from being pointer-based to being Lexicon- based. A number of things are done to accomplish this. The Reminder Taxonomy data dictionary (file #811.2) is restructured, a new taxonomy management system is introduced, and taxonomy evaluation is changed to accommodate the new structure. For Reminder Dialogs, users will no longer be able to add ICD-9-CM and/or CPT-4 codes to a Reminder Dialog, but will need to create a Taxonomy, assign codes, and then add the Taxonomy to the Reminder Dialog.

See the User Manual and the Taxonomy Management and Dialog Management sections of the Clinical Reminders Manager’s Manual for details of changes made by PXRM*2.0*26.

Under the Lexicon-based structure, codes are no longer entered as a range, eliminating the need for taxonomy expansion. The post-install routine in PXRM*2.0*26 will convert all existing taxonomies and reminder dialogs to the new structure.

### DG*5.3*862

This build updates the Clinical Reminders Index cross-references in the PTF file (#45) to accommodate ICD-10 diagnosis and procedure codes. It restructures the PTF portion of the Clinical Reminders Index to a generic format that can support all ICD coding systems. This format is:

^PXRMINDX (45, CODING SYSTEM,"INP", CODE, NODE, DFN, DATE, DAS)

^PXRMINDX (45, CODING SYSTEM,"PNI", DFN, NODE, CODE, DATE, DAS)

Where CODING SYSTEM is a three-character abbreviation as defined in the Coding Systems file (#757.03) and CODE is the code, not the pointer. For details, see the Clinical Reminders Index Technical Guide/Programmer’s Manual (PXRM\_INDEX\_TM).

The post-install routine will start a background job to rebuild the file #45 index in the new format.

### GMPL*2.0*44

This build updates the Clinical Reminders Index cross-references in the Problem file (#9000011) to accommodate ICD-10 CM diagnosis codes. It restructures the Problem List portion of the Clinical Reminders Index to a generic format that can support ICD and SNOMED CT coding systems. This format is:

^PXRMINDX (9000011, CODING **SYSTEM,”ISPP”, CODE, STATUS, PRIORITY, DFN, DLM, DAS)**

^PXRMINDX (9000011, CODING SYSTEM,”PSPI”, DFN, STATUS, PRIORITY, CODE, DLM, DAS)

Where CODING SYSTEM is a three-character abbreviation as defined in the Coding Systems file (#757.03) and CODE is the code, not the pointer. For details, see the Clinical Reminders Index Technical Manual (PXRM\_INDEX\_TM).

The post-install routine will start a background job to rebuild the file #9000011 index in the new format.

#### Purpose of This Guide

This Technical Manual is designed to help your site implement and maintain Clinical Reminders. It includes detailed information such as system requirements, file descriptions, and routine descriptions.

#### Our Target Audience

We have developed this guide for the following individuals, who are responsible for installing, supporting, maintaining, and testing this package:

- Information Resources Management (IRM)
- Clinical Application Coordinators (CAC) – called Application Package Coordinators (ADPAC) at some sites
- Product Support (PS)
- Software Quality Assurance (SQA)

Refer to the Web sites listed below when you want to receive more background and technical information about PXRM V. 2.0, and to download this manual and related documentation.

#### Related Documentation and websites

Clinical Reminders Main Web page: [http://vista.med.va.gov/reminders/](http://vista.med.va.gov/reminders/)

#### Documentation Retrieval Process

Your site can also retrieve the Clinical Reminders V. 2.0 documentation listed below from the V *ist* A Documentation Library (VDL) or from the following FTP addresses. The preferred method is to “FTP” the files from [**download.vista.med.va.gov.**](ftp://ftp.fo-slc.med.va.gov/) This location automatically transmits files from the first available FTP Server to the appropriate directory on your system. (See the order listed below under the FTP Address column). **Note:** If you prefer, you can retrieve the software *directly* from one of the FTP Servers, listed below, under the FTP Address column.

#### FTP Addresses Available for Downloading PXRM V. 2.0 Documentation

| **OI Field Office**   | **FTP Address**   | **Directory**   |
|-----------------------|-------------------|-----------------|
| Albany                | REDACTED          | REDACTED        |
| Hines                 | REDACTED          | REDACTED        |
| Salt Lake City        | REDACTED          | REDACTED        |

**Clinical Reminders V. 2*26 Documentation and Related File names**

| Documentation          | **Documentation File name**   |
|------------------------|-------------------------------|
| Installation Guide     | PXRM_2_0_26_IG.PDF            |
| Release Notes          | PXRM_2_0_26_RN.PDF            |
| Reminders Index Manual | PXRM_INDEX_TM.PDF             |

| User Manual      | PXRM_2_0_26_UM.PDF   |
|------------------|----------------------|
| Manager’s Manual | PXRM_2.0_MM.PDF      |

Clinical Reminders documentation can also be found in the VistA Documentation Library: [http://www.va.gov/vdl](http://www.va.gov/vdl)

Implementation and maintenance of Clinical Reminders occur several ways:

1. Integration with other applications:
2. Health Summary
3. Patient Care Encounter (PCE)

Management of Clinical Reminders includes coordinating with these other entities. This linkage should remain transparent to users, but will require setup and coordination by the IRM office and Clinical Coordinators. See the technical and user manuals of those packages for implementation instructions.

1. Setting site parameters with options on the Manager Menu and the CPRS Coversheet option.

1. Allocating menus and options (see the Menus and Options section).

1. User customization through CPRS GUI Coversheet options.

### Clinical Reminders Index Global

The Clinical Reminders Index Global was designed to provide an index of clinical data, which, in turn, supports rapid access to the data. You can find complete information about the Clinical Reminders Index in the Clinical Reminders Index Technical Manual.

## Implementation &amp; Maintenance

### Clinical Reminders Managers Menu

The Clinical Reminders Managers Menu contains the following menu options for implementing and maintaining Clinical Reminders. Each of these menu options contain more options, which are described in the following sections of this manual.

Reminders Managers Menu [PXRM MANAGERS MENU]

CF  Reminder Computed Finding Management ... [PXRM CF MANAGEMENT] RM  Reminder Definition Management ... [PXRM REMINDER MANAGEMENT] SM Reminder Sponsor Management [PXRM SPONSOR MANAGEMENT]

TXM Reminder Taxonomy Management ... [PXRM TAXONOMY MANAGEMENT] TRM Reminder Term Management ... [PXRM TERM MANAGEMENT]

LM Reminder Location List Management ... [PXRM LOCATION LIST MANAGEMENT]

RX	Reminder Exchange [PXRM REMINDER EXCHANGE] RT	Reminder Test [PXRM REMINDER TEST]

OS	Other Supporting Menus ... [PXRM OTHER SUPPORTING MENUS] INFO	Reminder Information Only Menu ... [PXRM INFO ONLY]

DM	Reminder Dialog Management ... [PXRM DIALOG MANAGEMENT]

CP	CPRS Reminder Configuration [PXRM CONFIGURATION MANAGEMENT] RP	Reminder Reports ... [PXRM REMINDER REPORTS]

MST	Reminders MST Synchronization Management ... [PXRM MST MANAGEMENT]

PL	Reminder Patient List Menu ... [PXRM PATIENT LIST MENU] PAR	Reminder Parameters ... [PXRM REMINDER PARAMETERS]

ROI	Reminder Orderable Item Menu

XM	Reminder Extract Menu [PXRM EXTRACT MENU] GEC	GEC Referral Report	[GEC REFERRAL REPORT]

#### Routine Information

**Namespace:** *PXRM*

XUPRROU (List Routines) prints a list of any or all of the PXRM routines. This option is found on the XUPR-ROUTINE-TOOLS menu on the XUPROG (Programmer Options) menu, which is a sub-menu of the EVE (Systems Manager Menu) option. See the list of checksums in Appendix B.

The first line of each routine contains a brief description of the general function of the routine. Use the Kernel option XU FIRST LINE PRINT (First Line Routine Print) to print a list of just the first line of each xxx subset routine.

Select Systems Manager Menu Option: **programmer** Options Select Programmer Options Option: **routine Tools**

Select Routine Tools Option: **First Line Routine Print**

PRINTS FIRST LINES

routine(s) ?	&gt; **PXRM***

Clinical Reminders V. 2.0*26 (PXRM*2.0*26) updates some of the following files. Journaling is recommended.

The namespace for the Clinical Reminders package is PXRM and the primary global is ^PXRM.

**Global	Name**

^PXRM(800	CLINICAL REMINDER PARAMETERS

^PXRM (801	REMINDER ORDERABLE ITEM GROUP

^PXRMD(801.41	REMINDER DIALOG

^PXRMD(801.42	REMINDER GUI PROCESS

^PXRMD(801.43	REMINDER FINDING ITEM PARAMETER

^PXRMD(801.45	REMINDER FINDING TYPE PARAMETER

^PXRMD(801.5	REMINDER DIALOG PATIENT ASSOCIATION

^PXRMD(801.55	REMINDER GEC DIALOG ASSOCIATION HISTORY

^PXRMD(801.9	REMINDER RESOLUTION STATUS

^PXRMD(801.95	HEALTH FACTOR RESOLUTION

^PXRMD(802.4	REMINDER FUNCTION FINDING

^PXRMPT(810.1	REMINDER REPORT TEMPLATE

^PXRM(810.2	REMINDER EXTRACT DEFINITION

^PXRMXT(810.3	REMINDER EXTRACT SUMMARY

^PXRM(810.4	REMINDER LIST RULE

^PXRMXP(810.5	REMINDER PATIENT LIST

^PXRM(810.6	REMINDER EXTRACT ERRORS

^PXRM(810.7	REMINDER EXTRACT COUNTING RULE

^PXRM(810.8	REMINDER COUNTING GROUP

^PXRMD(810.9	REMINDER LOCATION LIST

^PXD(811.2	REMINDER TAXONOMY

^PXRMD(811.4	REMINDER COMPUTED FINDINGS

^PXRMD(811.5	REMINDER TERM

^PXRMD(811.6	REMINDER SPONSOR

^PXRMD(811.7	REMINDER CATEGORY

^PXD(811.8	REMINDER EXCHANGE

^PXD(811.9	REMINDER DEFINITION

Note: You can learn more about these files by generating a list with file attributes using VA FileMan.

|   **File #** | **File Name**                   | **File Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|       800    | CLINICAL REMINDER PARAMETERS    | This file is used to define local parameters for maximum # of index errors, reminder management mail groups, health summary clinical maintenance disclaimers, SSN (full or truncated), MST synchronization, and websites.  The file is exported with one entry that contains parameters used by Clinical Reminders.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|       801    | REMINDER ORDERABLE ITEM GROUP   | This file contains a list of Orderable Items that should have a reminder definition or a reminder term evaluation run against them as an order check.  The Orderable Item will only be evaluated when the user places the order in CPRS. An Orderable Item Group can contain a list of Orderable Items and a list of Rules. A  reminder rule can only contain one reminder term or one reminder definition.                                                                                                                                                                                                                                                                                                                                                                                                   |
|       801.41 | REMINDER DIALOG                 | This file is used to define all of the components that work together to define a reminder dialog. Reminder dialog definitions are used by the CPRS GUI for  reminder resolution.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|       801.42 | REMINDER GUI PROCESS            | This file summarizes GUI functionality that has been created for particular dialog processing on the GUI side.  The GUI functionality can be associated with an entry in the Reminder Dialog file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|       801.43 | REMINDER FINDING ITEM PARAMETER | This file is used to predefine a preferred dialog element or dialog group to represent a reminder finding item.  Auto-generation of a reminder dialog from the reminder definition uses the dialog in this file in preference to using the Finding Type Parameter's prefix and suffix to create a sentence. The finding items are restricted to finding types that can be used to resolve the reminder from the CPRS GUI. This file is for local use only. It does not contain any nationally distributed entries.  Local entries in this file are not exchanged with other sites via the reminder exchange tool.                                                                                                                                                                                             |
|       801.45 | REMINDER FINDING TYPE PARAMETER | This file is used by the process that generates reminder dialogs for a reminder. During this process, for each reminder finding item in a reminder definition, one or more dialog elements are created depending on the Finding Type parameters in this file. The file content is distributed with the package but may be edited by sites to reflect how the site uses PCE data. The site can alter the pre-defined prefix and suffix text used to create sentences. The  site can also disable creation of sentences for specific types of resolution statuses (e.g., Disable creation of education refused for an education topic because the site prefers to use Health Factors to represent refusals).  The entries distributed in this file may not be deleted and new entries may not be added locally. |

|   **File #** | **File Name**                       | **File Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|       801.5  | REMINDER DIALOG PATIENT ASSOCIATION | This file contains a small amount of static data. Entries are entered and removed as Reminder Dialogs are processed by the CPRS GUI. Its main purpose is to keep track of and supply an Encounter Date/Time to the GUI interface so that the date/time  can be later added to fields in the V HEALTH FACTOR file.                                                                                                                                                                                                                                                             |
|       801.55 | REMINDER GEC DIALOG                 | This file contains a permanent history of activity that occurred during the use of the Reminder Geriatric Extended Care Dialogs. Information is added when a  GEC Dialog is used and information is added about the patient                                                                                                                                                                                                                                                                                                                                                   |
|       801.9  | REMINDER RESOLUTION STATUS          | This file defines the resolution statuses that may be related to a finding. National resolution statuses are distributed in this file, but sites may create local resolution statuses. If local resolutions are defined, they must be mapped to a national resolution status. The national resolution statuses are used by the process that creates dialog sentences for finding items.  The distributed national resolution statuses may not be deleted.                                                                                                                     |
|       801.95 | HEALTH FACTOR RESOLUTION            | This file defines the resolution statuses that should be related to a particular health factor. The resolution status can be derived for most patient  findings (visit file helps determine done and historical). In order to know the appropriate resolution statuses for a health factor, they must be defined in this file.  This file is for local use. No health factor resolution statuses are distributed in this file.                                                                                                                                                |
|       802.4  | REMINDER FUNCTION FINDING FUNCTIONS | Function findings operate on data from standard findings and return computed  data. They can be used in patient cohort logic and resolution logic. This file  defines the functions that can be used in function findings.                                                                                                                                                                                                                                                                                                                                                    |
|       810.1  | REMINDER REPORT TEMPLATE            | This file is used by the reminder reports options only. For each type of report (e.g. Reminders Due) selection parameters used in a report may be saved as a template when the report is being run. When running reports, the user may opt to retrieve parameters from an existing template as the basis of a new report. Templates may be modified, renamed, copied or deleted from the reminder report options. The parameters for the reminder reports consist of a  patient sample (e.g. PCMM team) from which a patient list is built and also a list of reminders to be |

|    |    | evaluated for each selected patient.  The field names in the template file correspond to the local variable and array names used in the print routines.   |
|----|----|-----------------------------------------------------------------------------------------------------------------------------------------------------------|

|   **File #** | **File Name**               | **File Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|--------------|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        810.2 | REMINDER EXTRACT DEFINITION | National extract definitions were sent out with Clinical Reminders V.2.0 to support site roll-up of reporting totals to the Austin Automation Center (AAC). The generic extract functionality supports corporate level management analysis by providing reports that:  - summarize patient reminder compliance totals (not applicable, applicable, due, not due) - summarize finding total counts that reflect the most recent findings resulting from reminder evaluation - summarize finding total counts that reflect site activities during the reporting month. - list unique applicable patients included in the finding count (Patient List is not sent to Austin)  An extract definition may be manually run or set up to automatically run monthly or quarterly. The  extract can be defined to only produce compliance totals, or to also include finding totals. |
|        810.3 | REMINDER EXTRACT SUMMARY    | This file stores compliance totals found for a specific extract. The extract entries are read-only and may be selected by number or extract name. The  extract summary entries are currently created from two types of processing: 1) Generic EXTRACT tool manual runs and automated runs 2) LREPI ENHANCE MANUAL RUN and LREPI NIGHTLY  TASK on day 15 of each month  Extracts and transmissions for a selected prior period may be initiated manually from Extract Summary  options. Existing extracts may also be re-transmitted, if required.                                                                                                                                                                                                                                                                                                                           |
|        810.4 | REMINDER LIST RULE          | This file is used to define what extract criteria should be used to build reminder patient lists. Extract criteria is defined as "list rules" in this file. The file is used by the Reminder Patient List option and Reminder Extract Management option to create patient lists.  There are four types of record in the file:  Patient List Rules - define an existing patient list Finding Rules - define reminder terms  Reminder Rule - defines a reminder definition that builds a patient list based on the patient cohort logic using the ending date as the evaluation date.  Rule Sets- defines a multiple of sequentially defined list rules  (a rule set cannot be included in the multiple).                                                                                                                                                                     |

|   **File #** | **File Name**                  | **File Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------------|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        810.5 | REMINDER PATIENT LIST          | Patient lists in this file are created from the Reminder Due reporting option, Reminder Patient List option or from Reminder Extract runs. Reminder patient lists are retained for 5 years in this file before being  purged. Individual patient lists can have the automatic purge turned off.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|        810.7 | REMINDER EXTRACT COUNTING RULE | This file is used during extract processing when an extract definition's TYPE OF TOTALS field is defined with COMPLIANCE AND FINDING TOTALS. When the extract type is for COMPLIANCE TOTALS only, there will not be an extract counting rule defined in the REMINDER EXTRACT DEFINITION file (#810.2). When the  extract type includes FINDING TOTALS, then the extract definition needs to reference a counting rule  for each reminder processed by the extract.                                                                                                                                                                                                                                                                                                                                                                                      |
|        810.8 | REMINDER COUNTING GROUP        | Counting groups are used for extract processing when the extract type is COMPLIANCE AND FINDING TOTALS. Each counting group defines reminder terms and type of counts to be totaled during an extract run.  Counting groups are referenced and combined into one Extract Counting Rule in the REMINDER EXTRACT COUNTING RULE file (#810.7).  Nationally distributed groups are prefixed 'VA-' and cannot be modified by a site.                                                                                                                                                                                                                                                                                                                                                                                                                         |
|        810.9 | REMINDER LOCATION LIST         | This file contains lists of stop codes and hospital locations for use as reminder findings. The stop codes and hospital locations are those associated with  a Visit file entry.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|        811.2 | REMINDER TAXONOMY              | This file stores the Clinical Reminders taxonomies. Taxonomies are used as Clinical Reminders findings and provide a way to define a set of codes as a single finding. Taxonomies are structured so that any of the coding systems defined in Lexicon's Coding System (file #757.03) can be used. However, in order for a coding system to be used in Clinical Reminders, there must be a  source in VistA where the coded patient data is stored. Examples are V POV (file #9000010.07) which stores ICD  diagnosis   codes and PTF (file #45) which  stores ICD diagnosis and procedure codes. The coding systems that meet this criteria are listed for selection in the taxonomy editor.  This file contains a combination of nationally distributed and local entries. Nationally distributed entries have their names prefixed with VA- and their |

|    |    | Class is National. Local entry names cannot start with VA- or have a National Class.   |
|----|----|----------------------------------------------------------------------------------------|

|   **File #** | **File Name**              | **File Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|--------------|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        811.4 | REMINDER COMPUTED FINDINGS | When none of the standard finding types will work, a computed finding can be created. There are two steps in creating a computed finding: First a MUMPS routine must be written. Information about how to do this can be found in the Clinical Reminders Manager Manual. The second step is to make an entry in this file, which contains a list of reminder computed findings.  This file contains a combination of nationally distributed and local entries. Nationally distributed entries have their name prefixed with VA-. Local entry names cannot start with VA-.                                                                                                                                                                                                                                                                                                                                                                                                                           |
|        811.5 | REMINDER TERM              | This file defines terms that may be used within reminder definitions. Reminder terms are useful for national reminders involving findings that are based on local file definitions (e.g., laboratory test, drug file, radiology). National reminder terms have limited editing capabilities which allow sites to map their local finding items to a term. Sites may create local reminder terms, providing an easy way to group a variety of findings and treat them the same way in a reminder. When a reminder with terms is evaluated, the finding items mapped to the term are used to find the patient data, but the patient data is reported based on the term the data is mapped to.  The most recent true finding will be used to represent the term.  This file contains a combination of national, local, and VISN level terms. Any local terms are assigned an internal entry number prefixed with your site number. Nationally distributed entries will have a Term Type of "National". |
|        811.6 | REMINDER SPONSOR           | This file contains the names of groups or organizations that are sponsors of reminder components such as definitions, terms, and dialogs.  Entries cannot be edited using FileMan; you must use the Reminder Sponsor Edit option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

|   **File #** | **File Name**       | **File Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|--------------|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        811.7 | REMINDER CATEGORY   | This file contains reminder categories. Reminder categories are created at each site and are not released with the reminder package.  A reminder category is a list of reminders (or other reminder categories) and is used to group reminders for display in the CPRS GUI. Reminder categories are allocated to individual users, locations, service, or  system using the option PXRM CPRS LOOKUP CATEGORIES.                                                                                                                                    |
|        811.8 | REMINDER EXCHANGE   | The Reminder Exchange File is used to store packed reminder definitions.  Entries in this file should never be edited.                                                                                                                                                                                                                                                                                                                                                                                                                             |
|        811.9 | REMINDER DEFINITION | This file contains Clinical Reminder definitions. For a detailed description of the contents of this file, see the Clinical Reminders Manager Manual. Additional information may be found at the Clinical Reminders web site: http//vista.med.va.gov/reminders/  This file contains a combination of nationally distributed and local entries. Any local entries are assigned an internal entry number prefixed with your site number. Nationally distributed entries have their  name prefixed with VA-. Local entry names cannot start with VA-. |

### FILE #811\_2 DD changes made by PXRM*2*26

In the past when building a taxonomy, the user input a low code and a high code to define a range. The range was expanded and stored in file #811.3. We have been told by the Lexicon team that this approach should be dropped for several reasons. In some coding systems the concept of a range does not exist and in those where it does there is no guarantee that it will continue to exist. For example, in a fairly recent CPT update a code was inserted in the middle of the range that is unrelated to anything else in that range.

The new approach is to allow the user who is building a taxonomy to choose from a set of codes returned by a Lexicon search. The search is based on a term/concept and a coding system. For example, the term/concept might be diabetes mellitus and the coding systems could be ICD-9 diagnosis, ICD-10 diagnosis, and SNOMED CT.

This is the new structure with the intent of being able to support any coding system that is in file #757.03. Part of this is new and will replace what is below it. See the three captures further below to see what is new and what will be removed.

^PXD(811.2,D0,0)= (#.01) NAME [1F] ^ (#.02) BRIEF DESCRIPTION [2F] ^ (#.03)

==&gt;DIALOG HEADER TEXT [3F] ^ (#4) PATIENT DATA SOURCE [4F] ^

==&gt;^ (#1.6) INACTIVE FLAG [6S] ^	^	^ (#10) USE INACTIVE

==&gt;PROBLEMS [9S] ^

^PXD(811.2,D0,1,0)=^811.22^^	(#2) DESCRIPTION

^PXD(811.2,D0,1,D1,0)= (#.01) DESCRIPTION [1W] ^

^PXD(811.2,D0,20,0)=^811.23A^^	(#20) SELECTED CODES

^PXD(811.2,D0,20,D1,0)= (#.01) LEXICON TERM/CONCEPT [1F] ^

^PXD(811.2,D0,20,D1,1,0)=^811.231A^^	(#1) CODING SYSTEM

^PXD(811.2,D0,20,D1,1,D2,0)= (#.01) CODING SYSTEM [1F] ^ (#1) NUMBER OF CODES

==&gt;SELECTED [2N] ^

^PXD(811.2,D0,20,D1,1,D2,1,0)=^811.2312A^^	(#2) CODE LIST

^PXD(811.2,D0,20,D1,1,D2,1,D3,0)= (#.01) CODE [1F] ^ (#1) USE IN DIALOG [2S]

==&gt;^

^PXD(811.2,D0,80,0)=^811.22102^^	(#2102) ICD9 RANGE OF CODES

^PXD(811.2,D0,80,D1,0)= (#.01) ICD9 LOW CODE [1F] ^ (#1) ICD9 HIGH CODE [2F]

==&gt;^ (#2) ICD9 ADJACENT LOWER CODE [3F] ^ (#3) ICD9

==&gt;ADJACENT HIGHER CODE [4F] ^

^PXD(811.2,D0,80.1,0)=^811.22103^^	(#2103) ICD0 RANGE OF CODES

^PXD(811.2,D0,80.1,D1,0)= (#.01) ICDO LOW CODE [1F] ^ (#1) ICD0 HIGH CODE

==&gt;[2F] ^ (#2) ICD0 ADJACENT LOWER CODE [3F] ^ (#3)

==&gt;ICD0 ADJACENT HIGHER CODE [4F] ^

^PXD(811.2,D0,81,0)=^811.22104^^	(#2104) CPT RANGE OF CODES

^PXD(811.2,D0,81,D1,0)= (#.01) CPT LOW CODE [1F] ^ (#1) CPT HIGH CODE [2F] ^

==&gt;(#2) CPT ADJACENT LOWER CODE [3F] ^ (#3) CPT ADJACENT

==&gt;HIGHER CODE [4F] ^

^PXD(811.2,D0,100)= (#100) CLASS [1S] ^ (#101) SPONSOR [2P:811.6] ^ (#102)

==&gt;REVIEW DATE [3D] ^

^PXD(811.2,D0,110,0)=^811.21D^^	(#110) EDIT HISTORY

^PXD(811.2,D0,110,D1,0)= (#.01) EDIT DATE [1D] ^ (#1) EDIT BY [2P:200] ^

^PXD(811.2,D0,110,D1,1,0)=^811.212^^	(#2) EDIT COMMENTS

^PXD(811.2,D0,110,D1,1,D2,0)= (#.01) EDIT COMMENTS [1W] ^

^PXD(811.2,D0,SDX,0)=^811.23102IP^^	(#3102) SELECTABLE DIAGNOSIS

^PXD(811.2,D0,SDX,D1,0)= (#.01) SELECTABLE DIAGNOSIS [1P:80] ^ (#1) DISPLAY

==&gt;TEXT [2F] ^ (#2) DISABLED [3S] ^

^PXD(811.2,D0,SDZ)= (#3106) GENERATE DIALOG DX PARAMETER [1S] ^ (#3107)

==&gt;CURRENT VISIT DX DIALOG HDR [2F] ^ (#3108) HISTORICAL

==&gt;VISIT DX DIALOG HDR [3F] ^

^PXD(811.2,D0,SPR,0)=^811.23104IP^^	(#3104) SELECTABLE PROCEDURE

^PXD(811.2,D0,SPR,D1,0)= (#.01) SELECTABLE PROCEDURE [1P:81] ^ (#1) DISPLAY

==&gt;TEXT [2F] ^ (#2) DISABLED [3S] ^

^PXD(811.2,D0,SPZ)= (#3110) GENERATE DIALOG PR PARAMETER [1S] ^ (#3111)

==&gt;CURRENT VISIT PR DIALOG HDR [2F] ^ (#3112) HISTORICAL

==&gt;VISIT PR DIALOG HDR [3F] ^

The above capture shows the entire structure. The following capture shows the new portion that will replace much of what follows it.

^PXD(811.2,D0,1,0)=^811.22^^	(#2) DESCRIPTION

^PXD(811.2,D0,1,D1,0)= (#.01) DESCRIPTION [1W] ^

^PXD(811.2,D0,20,0)=^811.23A^^	(#20) SELECTED CODES

^PXD(811.2,D0,20,D1,0)= (#.01) LEXICON TERM/CONCEPT [1F] ^

^PXD(811.2,D0,20,D1,1,0)=^811.231A^^	(#1) CODING SYSTEM

^PXD(811.2,D0,20,D1,1,D2,0)= (#.01) CODING SYSTEM [1F] ^ (#1) NUMBER OF CODES

==&gt;SELECTED [2N] ^

^PXD(811.2,D0,20,D1,1,D2,1,0)=^811.2312A^^	(#2) CODE LIST

^PXD(811.2,D0,20,D1,1,D2,1,D3,0)= (#.01) CODE [1F] ^ (#1) USE IN DIALOG [2S]

==&gt;^

These sections will be removed

There is a new taxonomy editor that uses a combination of List Manager, ScreenMan, and the Browser. The user is free to input a Lexicon Term/Concept but the editor constrains their choice of Coding System. Once they select a coding system the combination of Term/Concept and Coding System is passed to a Lexicon API that returns a list of codes. The list is displayed using List Manager and the user can select the codes they want to include in the taxonomy and mark them to use in a dialog also. When they are done editing the data in the Coding System multiple is stored via a call to UPDATE^DIE.

## Exported Menus and Options

This table shows top-level menus; sub-menus are described in the Description column.

| **Option**                           | **Option Name**               | **Syn**   | **Description**                                                                                                                                                                                            |
|--------------------------------------|-------------------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reminder Computed Finding Management | PXRM CF MANAGEMENT            | CF        | This option provides tools for viewing or editing reminder computed findings.                                                                                                                              |
| Reminder Definition Management       | PXRM REMINDER MANAGEMENT      | RM        | This menu contains options for creating, copying, and editing reminder definitions, as well as the options for maintaining the  parameters used by CPRS for reminder processing.                           |
| Reminder Taxonomy  Management        | PXRM TAXONOMY MANAGEMENT      | TXM       | This option provides all aspects of taxonomy management including creation, editing, and  inquiry.                                                                                                         |
| Reminder Location List Management    | PXRM LOCATION LIST MANAGEMENT |           | Location Lists store locations as stop codes or hospital locations. This option provides tools for viewing and editing location lists.                                                                     |
| Reminder Computed Finding Management | PXRM CF MANAGEMENT            | CF        | This option provides tools for viewing and editing reminder computed findings.                                                                                                                             |
| Reminder Definition Management       | PXRM REMINDER MANAGEMENT      | RM        | This menu contains options for creating, copying, and editing reminder definitions, as well as the options for maintaining the parameters used by CPRS for reminder processing.                            |
| Reminder Sponsor Management          | PXRM SPONSOR MANAGEMENT       | SM        | A Reminder Sponsor is the organization or group that sponsors a Reminder Definition, such as the Office of Quality and  Performance. Options on this menu let you view, define, or edit Reminder Sponsors. |
| Reminder Taxonomy Management         | PXRM TAXONOMY MANAGEMENT      | TXM       | This option provides all aspects of taxonomy management including creation, editing, and  inquiry.                                                                                                         |
| Reminder Term Management             | PXRM TERM MANAGEMENT          | TRM       | This menu allows you to edit, map, and view reminder terms.                                                                                                                                                |
| Reminder Location List Management    | PXRM LOCATION LIST MANAGEMENT | LM        | Location Lists store locations as stop codes or hospital locations. This option provides tools for viewing and editing location lists.                                                                     |
| Reminder Exchange                    | PXRM REMINDER EXCHANGE        | RX        | This option allows sites to exchange reminder definitions, dialogs, and other reminder components via MailMan messages and host files.                                                                     |
| Reminder Test                        | PXRM REMINDER TEST            | RT        | This utility helps you test and troubleshoot your reminders when you create them or  when you have problems.                                                                                               |
| Other Supporting Menus               | PXRM OTHER SUPPORTING MENUS   | OS        | This option contains menus from related packages such as PCE and Health Summary.                                                                                                                           |
| Reminder Information Only Menu       | PXRM INFO ONLY                | INFO      | This menu provides information-only options for users who need information about  reminders but do not need the ability to make changes.                                                                   |

| Reminder Dialog Management               | PXRM DIALOG MANAGEMENT   | DM   | This menu allows maintenance of the parameters used by CPRS for reminder dialog processing.                                                                                                                                                                          |
|------------------------------------------|--------------------------|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reminder Reports                         | PXRM REMINDER REPORTS    | RP   | This is a menu of Clinical Reminder reports that clinicians can use for summary and detailed level information about patients' due and satisfied reminders. This option also  contains reports that clinical coordinators can use to assign menus to specific users. |
| Reminders MST Synchronization Management | PXRM MST MANAGEMENT      | MST  | This option provides the Clinical Reminders MST management options. These options give you the ability to synchronize the MST History file #29.11 with MST data recorded  elsewhere and to determine when the synchronization was last done.                         |
| Reminder Patient List  Menu              | PXRM PATIENT  LIST MENU  | PL   | This menu contains options to manage list  rules and patient lists.                                                                                                                                                                                                  |
| Reminder Orderable Item Group Menu       | PXM ORDER                | OI   | This menu contains options to allow sites to create Reminder Order Checks                                                                                                                                                                                            |
| Reminder Parameters                      | PXRM REMINDER PARAMETERS | PAR  | This menu contains the options, Edit Site  Disclaimer and Edit Web Sites, which allow you to modify the parameters for these items.                                                                                                                                  |
| Reminder Extract Menu                    | PXRM EXTRACT MENU        | XM   | This option allows management of extract definitions, extract runs, and extract transmissions.                                                                                                                                                                       |
| GEC Referral Report                      | PXRM GEC REFERRAL REPORT | GEC  | This is the option that is used to generate GEC Reports. GEC (Geriatrics Extended  Care) is used for referral of geriatric patients to receive further care                                                                                                          |

#### Options not on a menu

The option PXRM DISABLE/ENABLE EVALUATION provides a manual disable/enable function. If for some reason, reminder evaluation needs to be disabled, it can be done through this option. This option should be given to a very limited number of people and can only be used by holders of the PXRM MANAGER key. When the issue that required disabling evaluation has been handled, reminder evaluation can be enabled again using this same option. Note that this option can be used to enable evaluation even if it was not disabled using this option. For example, if reminder evaluation was automatically disabled for an index rebuild, this option could be used to enable evaluation even though the index is still rebuilding. If that is done, the MailMan messages will start being sent again.

Purging and archiving capabilities are not currently available in Clinical Reminders.

**Required Packages**

Clinical Reminders V. 2.0*18 requires that the following software is installed and fully patched.

#### Remote Procedure Calls (RPCs)

An RPC is a procedure called from the client (the user’s workstation) communicating to the server (the M database). Clinical Reminders contains Reminder Dialogs that are used within CPRS, from the Notes tab, thus requiring RPCs to facilitate this communication.

A complete listing of RPCs is available under the DBA menu on Forum. The Database Administrator (DBA) maintains a list of RPCs.

1. PXRM EDUCATION SUBTOPICS
2. PXRM EDUCATION SUMMARY
3. PXRM EDUCATION TOPIC
4. PXRM MENTAL HEALTH
5. PXRM MENTAL HEALTH RESULTS
6. PXRM MENTAL HEALTH SAVE
7. PXRM PROGRESS NOTE HEADER
8. PXRM REMINDER CATEGORIES
9. PXRM REMINDER CATEGORY
10. PXRM REMINDER DETAIL
11. PXRM REMINDER DIALOG
12. PXRM REMINDER DIALOG (TIU)
13. PXRM REMINDER DIALOG PROMPTS
14. PXRM REMINDER EVALUATION
15. PXRM REMINDER INQUIRY
16. PXRM REMINDER RPC
17. PXRM REMINDER WEB
18. PXRM REMINDERS (UNEVALUATED)
19. PXRM REMINDERS AND CATEGORIES

#### Database Integration Agreements

Complete integration agreements are under the DBA menu on Forum.

Non-destructive, read-only component routines have been written to present VistA ancillary package data.

The package interacts with and extracts data from many other VistA software packages. Permission to use data from the other packages is obtained by completing a written integration agreement with each of the other packages.

The Database Administrator (DBA) maintains a list of Integration Control Registrations (ICRs) or mutual agreements between software developers, allowing the use of internal entry points or other software-specific features that are not available to the general programming public.

To obtain the current list of ICRs to which Clinical Reminders is a custodian, do the following:

Select DBA MENU Option: ??

NAME	NAMESPACE    AND   FILESPACE    REGISTRATIONS ... IAs	INTEGRATION CONTROL REGISTRATIONS ...

PKG	PACKAGE FILE INFORMATION ...

STN	INSTITUTION FILE INFORMATION ... STND	STANDARDS ...

Select    DBA    MENU   Option:   ia	INTEGRATION    CONTROL   REGISTRATIONS

Select   INTEGRATION   CONTROL   REGISTRATIONS    Option:  ?

HELP	Instructions for Entering ICRs

GET#	GET NEW Integration Control Registration #(s) ADD	ADD/EDIT     Pending      Integration Control Registration   ROLL	Roll up ICR into Mail Message

FILE	File-type   Integration   Control   Registrations Menu ...   ROU	Routine-type ICRs Menu ...

RPC	Remote Procedure Call-type ICRs Menu   ...   OTH	Print 'Other'-type ICRs

SUPP	Supported References Menu ...

CONT	Controlled    Subscription ICRs Menu   ...   PRIV	Private ICRs Menu ...

CUST	Custodial Package Menu ...

INQ	Inquire    to    an    Integration   Control Registration SUBS	Subscriber Package Menu ...

APIS	Supported API Report VBLE	Lookup ICRs by Variable

Select    Custodial    Package    Menu   Option:   1	ACTIVE ICRs by Custodial Package

Select PACKAGE NAME: **P** XRM

DEVICE: HOME// **&lt;Enter&gt;** UCX DEVICE Right Margin: 80// **&lt;Enter&gt;**

ACTIVE    ICRs    by    Custodial Package Print   ALL    ICRs    by Custodial Package Supported References Print All

1

2

3

PEND	Print ICRs in Pending Status ACTV	Print       Active ICRs

ALL	Print ALL ICRs

Enter  ??  for  more  options,   ???   for   brief   descriptions, ?OPTION for help text.

Select INTEGRATION CONTROL REGISTRATIONS Option: cust	 Custodial Package Menu

Select Custodial Package Menu Option: ?

.

All options are independently invokable.

There are no package-wide variables in Clinical Reminders.

#### KIDS Build and Install Print Options Print a list of package components

Use the KIDS Build File Print option if you would like a complete listing of package components (e.g., routines and options) exported with this software. See the example in Appendix C.

&gt;D ^XUP

Setting up programmer environment Terminal Type set to: C-VT100

Select OPTION NAME: XPD MAIN	Kernel Installation &amp; Distribution System menu Edits and Distribution ...

Utilities ... Installation ...

Select Kernel Installation &amp; Distribution System Option: Utilities Build File Print

Install File Print

Convert Loaded Package for Redistribution Display Patches for a Package

Purge Build or Install Files Rollup Patches into a Build Update Routine File

Verify a Build

Verify Package Integrity

Select Utilities Option: Build File Print Select BUILD NAME: **CLINICAL REMINDERS 2.0**

**Print Results of the Installation Process**

Use the KIDS Install File Print option if you’d like to print out the results of the installation process.

Select Utilities Option:	Install File Print Select INSTALL NAME: **CLINICAL REMINDERS 2.0**

DEVICE: HOME// ;;999	ANYWHERE

#### Other Kernel Print Options

Besides using the Kernel Installation &amp; Distribution (KIDS) options to get lists of routines, files, etc., you can also use other Kernel options to print online technical information.

#### Routines

The namespace for the Clinical Reminders package is PXRM. Use the Kernel option, List Routines [XUPRROU], to print a list of any or all of the Clinical Reminder routines. This option is found on the Routine Tools [XUPR-ROUTINE- TOOLS] menu on the Programmer Options [XUPROG] menu, which is a sub- menu of the Systems Manager Menu [EVE] option.

#### Example:

The first line of each routine contains a brief description of the general function of the routine. Use the Kernel option, First Line Routine Print [XU FIRST LINE PRINT], to print a list of just the first line of each Health Summary subset routine.

#### Example:

**Globals**

The globals used in the package are PXRM*, PXRMD*, and PXD*:

Use the Kernel option, List Global [XUPRGL], to print a list of any of these globals. This option is found on the Programmer Options menu [XUPROG], which is a sub-menu of the Systems Manager Menu [EVE] option.

**Example:**

#### Inquire To Option File

The Kernel Inquire option [XUINQUIRE] provides the following information about a specified option(s):

- Option name.
- Menu text.
- Option description.
- Type of option.
- Lock (if any).

In addition, all items on the menu are listed for each menu option.

#### XINDEX

XINDEX is a routine that produces a report called the VA Cross-Referencer. This report is a technical and cross-reference listing of one routine or a group of routines. XINDEX provides a summary of errors and warnings for routines that do not comply with VA programming standards and conventions, a list of local and global variables and what routines they are referenced in, and a list of internal and external routine calls.

XINDEX is invoked from programmer mode: D ^XINDEX. When selecting routines, select XXX* .

#### Data Dictionaries/ Files

The number-spaces for Clinical Reminders files are 800. 801, 811-. Use the VA FileMan DATA DICTIONARY UTILITIES, option #8 (DILIST, List File Attributes), to print a list of these files. Depending on the FileMan template used to print the list, this option will print out all or part of the data dictionary for the PXRM files.

#### List File Attributes

The FileMan List File Attributes option [DILIST] lets you generate documentation about files and file structure. If you choose the “Standard” format, you can see the following Data Dictionary information for a specified file(s):

- File name and description.
- Identifiers.
- Cross-references.
- Files pointed to by the file specified.
- Files that point to the file specified.
- Input templates.
- Print templates.
- Sort templates.

**Example:**

&gt; **D P^DI**

VA FileMan 21.0

Select OPTION: **DATA DICTIONARY UTILITIES**

Select DATA DICTIONARY UTILITY OPTION: **LIST FILE ATTRIBUTES**

START WITH WHAT FILE: 800

(1 entry)

GO TO WHAT FILE: 821

Select LISTING FORMAT: STANDARD// **[Enter]**

DEVICE: **PRINTER**

In addition, the following applicable data is supplied for each field in the file: field name, number, title, global location, description, help prompt, cross-reference(s), input transform, date last edited, and notes.

The “Global Map” format of this option generates an output that lists all cross-references for the file selected, global location of each field in the file, input templates, print templates, and sort templates.

#### ?, ??, and ??? Online Help

**?** Enter one question mark to see helpful information about the components of the health summary type used in the health summary and the options available.

**??** Enter two question marks to see a list of available health summary components.

**???** Enter three question marks for detailed help, if available.

#### CPRS Online Help

In CPRS, help relating to Clinical Reminders is available from the Help menu.

#### Internet

Clinical Reminders information is also available from the Clinical Reminders website [http://vista.med.va.gov/reminders/](http://vista.med.va.gov/reminders/) and from the V *ist* A Documentation Library (VDL): [http://vista.med.va.gov/vdl/](http://vista.med.va.gov/vdl/) or [http://www.va.gov/vdl](http://www.va.gov/vdl)

#### Acronyms

Full VA list: [http://vaww1.va.gov/acronyms/fulllist.cfm#A](http://vaww1.va.gov/acronyms/fulllist.cfm)

AIMS	Abnormal Involuntary Movement Scale AITC	Austin Information Technology Center API	Application Programmer Interface.

CAC	Clinical Application Coordinator CPRS	Computerized Patient Record System. DBIA	Database Integration Agreement.

EPRP	External Peer Review Program

GUI	Graphical User Interface.

HRMH	High Risk Mental Health

HSR&amp;D	Health Services Research and Development HL7	Health Level 7

IHD	Ischemic Heart Disease

LSSD	Last Service Separation Date

MDD	Major Depressive Disorder

MH	Mental Health

OIT	Office of Information &amp; Technology

OQP	Office of Quality and Performance

PD	Product Development (formerly OED) PXRM	Clinical Reminders Namespace

QUERI	Quality Enhancement Research Initiative SAS	Simple Authentication and Security

SRS	Software Requirements Specification

VHA	Veterans Health Administration. VISN	Veterans Integrated Service Networks.

**V** IS *T* **A** Veterans Health Information System and Technology Architecture.

YS	Mental Health Namespace

**OIT Master Glossary:** [**http://vaww.oed.wss.va.gov/process/Library/master\_glossary/masterglossary.htm**](http://vaww.oed.wss.va.gov/process/Library/master_glossary/masterglossary.htm)

**Definitions**

AITC SAS Files	AITC SAS files contain data that is equivalent to data stored in the Reminder Extract Summary entry in the Reminder Extract Summary file. AITC manages SAS files for use by specifically defined users.

Applicable	An evaluation status that indicates patients whose findings met the patient cohort reminder evaluation.

Due	An evaluation status that indicates patients whose reminder evaluation status is due.

Extract Parameter	Parameters that define how to identify the patient cohort. A

national extract entry is defined for each extract process. This entry defines an extract name, how often to automatically run the named extract process, the rules used to identify target patients, what reminders should be run against what patient list, what type of finding counts to accumulate, and where to transmit results.

Extract Run	A periodic extract job based on the Extract Parameter

definition. The extract job creates an entry in the Reminder Extract Summary file. The extract job automatically starts a transmission job to transmit the extract summary data to a queue at the AAC. The successful completion of the Extract Run schedules the next periodic Extract Run.

Extract Summary	An extract summary containing the results of an extract process is created by this process in the Extract Summary File. This Extract Summary entry will help coordinators track the extract process through successful transmission processing by AAC.

Finding Count Rules	A Finding Count Rule defines the group of findings to

accumulate, the type of finding total, and whether to use the TOTAL or APPLICABLE patient cohorts to calculate finding counts.

Finding Group	Group of Reminder Terms within the Extract Parameter File used for counting purposes.

Finding Totals	Totals derived using Finding Count Rules.

HL7 Transmissions	HL7 transmission packages contain HL7 messages that are processed between the transmitting system and AAC.

List Rules	A List Rule is a set of rules that define which findings shall be used to determine whether a patient should be added or removed from a patient list.

National Database	All sites running Mental Health QUERI software transmit their data to a new compliance totals database at the AAC.

Not Applicable	An evaluation status that indicates patients whose findings did not meet the patient cohort reminder evaluation.

Not Due	An evaluation status that indicates patients whose reminder evaluation status is not due.

Reminder Definitions Reminder Definitions comprise the predefined set of finding items used to identify patient cohorts and reminder resolutions.

Reminders are used for patient care and/or report extracts.

Reminder Dialog	Reminder Dialogs comprise a predefined set of text and findings that together provide information to the CPRS GUI, which collects and updates appropriate findings while building a progress note.

Reminder Patient List A list of patients that is created from a set of List Rules and/or as a result of report processing. Each Patient List is assigned a name and is defined in the Reminder Patient List File. Reminder Patient Lists may be used as an incremental step to completing national extract processing or for local reporting needs. Patient Lists created from the Reminders Due reporting process are based on patients that met the patient cohort, reminder resolution, or specific finding extract parameters. These patient lists are used only at local facilities.

Reminder Terms	Predefined finding items that are used to map local findings to national findings, providing a method to standardize these findings for national use.

Reminder Totals	Totals that are accumulated from the reminder evaluation process based on the APPLICABLE, NOT APPLICABLE, DUE, AND

NOT DUE statuses.

Report Reminders	Reminders may be defined specifically for national reporting. Report Reminders do not have a related Reminder Dialog in CPRS and are not used by clinicians for patient care. However, clinical reminders that are used in CPRS may also be used for national reminder reporting. All reminders targeted for national reporting are defined in Extract Parameters.

Reporting Period Extract	The extracts may be for monthly, quarterly, or yearly processing. The extracts are formatted and transmitted to the national database via HL7 messaging using a report format.

Resolved	An evaluation status that indicates a patient’s reminder was satisfied by actions taken by the patient and/or clinician.

Total	The total number of patients in a patient list (denominator) based on the criteria defined in the Reminder List Rule file.

Transmission Run	The Transmission Run is started automatically by the Extract Run, but may also be manually scheduled.  The extract process starts the Transmission Run just before completing the Extract Run. The Transmission Run transmits extract summary data to an AAC queue via HL7 transmissions. This data updates the Reminder Extract Summary entry for the reporting period.

Security for Clinical Reminders is managed by menu/option assignment, file access, and one security key.

Reports produced by this package are highly confidential and should be treated with the same security precautions as a patient’s medical record.

#### Menu Access

The Clinical Reminders package contains the following menus/options. Assign these menus as follows.

| **Menu/Option**                       | **Option Name**                | **Assignment**                                                                                                        |
|---------------------------------------|--------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| Reminder Computed Finding  Management | PXRM CF MANAGEMENT             | CACs, Reminders managers                                                                                              |
| Reminder Definition  Management       | PXRM REMINDER  MANAGEMENT      | CACs, Reminders managers                                                                                              |
| Reminder Sponsor  Management          | PXRM SPONSOR  MANAGEMENT       | CACs, Reminders managers                                                                                              |
| Reminder Taxonomy  Management         | PXRM TAXONOMY  MANAGEMENT      | CACs, Reminders managers                                                                                              |
| Reminder Location List  Management    | PXRM LOCATION LIST  MANAGEMENT | CACs, Reminders managers                                                                                              |
| Reminder Term  Management             | PXRM TERM MANAGEMENT           | CACs, Reminders managers                                                                                              |
| Reminder Exchange                     | PXRM REMINDER  EXCHANGE        | CACs, Reminders managers                                                                                              |
| Reminder Test                         | PXRM REMINDER TEST             | CACs, Reminders managers                                                                                              |
| Other Supporting Menus                | PXRM OTHER SUPPORTING  MENUS   | CACs, Reminders managers                                                                                              |
| Reminder Information Only Menu        | PXRM INFO ONLY                 | Assign to users (e.g., clinicians) who need information about reminders but do not need the  ability to make changes. |
| Reminder Dialog  Management           | PXRM DIALOG  MANAGEMENT        | CACs, Reminders managers                                                                                              |
| CPRS Reminder Configuration           | PXRM CPRS CONFIGURA-  TION     | CACs, Reminders managers                                                                                              |

| **Option**                               | **Option Name**           | **Assignment**                                                                                                                                                                                                                                                       |
|------------------------------------------|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reminder Reports                         | PXRM REMINDER REPORTS     | This is a menu of Clinical Reminder reports that clinicians can use for summary and detailed level information about patients' due and satisfied reminders. This option also contains reports that clinical coordinators can use to assign menus to  specific users. |
| Reminder Patient  List Menu              | PXRM PATIENT  LIST MENU   | CACs, Reminders managers                                                                                                                                                                                                                                             |
| Reminders MST Synchronization Management | PXRM MST MANAGEMENT       | CACs, Reminders managers                                                                                                                                                                                                                                             |
| Reminder Parameters                      | PXRM REMINDER  PARAMETERS | CACs, Reminders managers                                                                                                                                                                                                                                             |
| Reminder Extract  Management             | PXRM EXTRACT  MENU        | CACs, Reminders managers                                                                                                                                                                                                                                             |
| GEC Referral Report                      | PXRM GEC REFERRAL REPORT  | This is the option that is used to generate GEC Reports. GEC (Geriatrics Extended Care) is used for referral of geriatric patients to receive further  care                                                                                                          |

#### Option not on a menu

The option PXRM DISABLE/ENABLE EVALUATION provides a manual disable/enable function. If for some reason, reminder evaluation needs to be disabled, it can be done through this option. This option should be given to a very limited number of people and can only be used by holders of the PXRM MANAGER key. When the issue that required disabling evaluation has been handled, reminder evaluation can be enabled again using this same option. Note that this option can be used to enable evaluation even if it was not disabled using this option. For example, if reminder evaluation was automatically disabled for an index rebuild, this option could be used to enable evaluation even though the index is still rebuilding. If that is done, the MailMan messages will start being sent again.

#### Security Key

**PXRM MANAGER**

DESCRIPTION:

Assign this key to people who are responsible for managing Clinical Reminders.

#### Options/actions requiring key

**PXRM DISABLE/ENABLE EVALUATION**

(see above description)

**PXRM FINDING USAGE REPORT on** the PXRM REMINDER REPORTS menu

- The field called **Creator** is populated when someone creates a reminder report template. This field will be used when someone accesses the template. The user accessing the template must either be the same user who created the template or must hold the PXRM MGR key to be able to access the option to edit the template. If the user is not the creator and does not hold the PXRM MANAGER key, they will not see the prompt to edit the template.

#### Patient List Management Option

Actions

- Create Patient List

Secure List? prompt

If the answer to this prompt is “YES,” the list becomes a private list, which means that the only people who can view the list are the creator, anyone who the creator has given view access, and anyone who holds the PXRM MANAGER KEY.

- ED (Edit Patient List) – if you are the creator of the list you can use this action to edit the name and type of list; if you hold the PXRM MANAGER key you can also edit the creator of the list.
- USR (View Users) – this action is applicable only to private lists. If you are the creator of the list or hold the PXRM MANAGER key you can use this action to give other users either view only or full access to the patient list. You can also remove a user’s access to the list.

## APPENDIX A: Security Guide, cont’d

#### File Security

The table below indicates the security that the Clinical Reminders software package establishes for its files.

|   **Number** | **Name**                             | **DD**   | **RD**   | **WR**   | **DEL**   | **LAYGO**   | **AUDIT**   |
|--------------|--------------------------------------|----------|----------|----------|-----------|-------------|-------------|
|       800    | CLINICAL REMINDER  PARAMETERS        | @        |          | @        | @         | @           | @           |
|       801.41 | REMINDER DIALOG                      | @        |          | @        | @         | @           | @           |
|       801.42 | REMINDER GUI PROCESS                 | @        |          | @        | @         | @           | @           |
|       801.43 | REMINDER FINDING ITEM  PARAMETER     | @        |          | @        | @         | @           | @           |
|       801.45 | REMINDER FINDING TYPE  PARAMETER     | @        |          | @        | @         | @           | @           |
|       801.5  | REMINDER DIALOG  PATIENT ASSOCIATION | @        | @        | @        | @         | @           | @           |
|       801.9  | REMINDER RESOLUTION  STATUS          | @        |          | @        | @         | @           | @           |
|       801.95 | HEALTH FACTOR  RESOLUTION            | @        |          | @        | @         | @           | @           |
|       802.4  | REMINDER FUNCTION FINDING            | @        | @        | @        | @         | @           | @           |
|       810.1  | REMINDER REPORT  TEMPLATE            | @        |          | @        | @         | @           | @           |
|       810.2  | REMINDER EXTRACT  PARAMETERS         | @        |          | @        | @         | @           | @           |
|       810.3  | REMINDER EXTRACT  SUMMARY            | @        |          | @        | @         | @           | @           |
|       810.4  | REMINDER LIST RULE                   | @        |          | @        | @         | @           | @           |
|       810.5  | REMINDER PATIENT LIST                | @        |          | @        | @         | @           | @           |
|       810.7  | REMINDER EXTRACT  FINDING RULE       | @        |          | @        | @         | @           | @           |
|       810.8  | REMINDER FINDING GROUP               | @        |          | @        | @         | @           | @           |
|       810.9  | REMINDER LOCATION  LIST              | @        |          | @        | @         | @           | @           |
|       811.2  | REMINDER TAXONOMY                    | @        |          | @        | @         | @           | @           |
|       811.3  | EXPANDED TAXONOMIES                  | @        |          | @        | @         | @           | @           |
|       811.4  | REMINDER COMPUTED  FINDINGS          | @        |          | @        | @         | @           | @           |
|       811.5  | REMINDER TERM                        | @        |          | @        | @         | @           | @           |
|       811.6  | REMINDER SPONSOR                     | @        |          | @        | @         | @           | @           |
|       811.7  | REMINDER CATEGORY                    | @        |          | @        | @         | @           | @           |
|       811.8  | REMINDER EXCHANGE                    | @        |          | @        | @         | @           | @           |
|       811.9  | REMINDER DEFINITION                  | @        |          | @        | @         | @           | @           |

## Appendix B: Computed Expressions

*From the FileMan Technical Manual*

Clinical Reminders uses M Operators/Computed Expressions to Computed expressions can consist of a single [element.](http://www.hardhats.org/fileman/u2/ce_el.htm) However, often several elements are joined together using operators. Operators are characters that perform some action on elements.

- [Unary Operators](http://www.hardhats.org/fileman/u2/ce_op.htm)
- [Binary Operators](http://www.hardhats.org/fileman/u2/ce_op.htm)
- [Boolean Operators](http://www.hardhats.org/fileman/u2/ce_op.htm)
- [Parentheses in Expressions](http://www.hardhats.org/fileman/u2/ce_op.htm)
- [Example of a Compound Expression](http://www.hardhats.org/fileman/u2/ce_op.htm)

**Unary Operators**

The simplest operators are the unary operators. They force a numeric interpretation of the element that follows. They can also affect the sign of the resulting number. The unary operators are:

| **Unary Operator**   | **Description**                                  |
|----------------------|--------------------------------------------------|
| **+**                | Positive numeric interpretation (sign unchanged) |
| **-**                | Negative numeric interpretation (sign changed)   |

**Binary Operators**

Another set of operators takes two elements, manipulates them, and returns a result. These are called binary operators. You can use the following binary operators in computed expressions:

| **Binary Operator**   | **Description**                                                        |
|-----------------------|------------------------------------------------------------------------|
| +                     | Addition                                                               |
| -                     | Subtraction                                                            |
| *                     | Multiplication                                                         |
| /                     | Division                                                               |
| **                    | Exponentiation (2**2=8)                                                |
| \                     | Integer (truncated) division (e.g., 13\2 = 6)                          |
| _                     | Concatenation (e.g., "AB"_"CDE" = ABCDE)                               |
| #                     | Modulo; returns the remainder of one number divided by another (7#3=1) |

**Boolean Operators**

A third set of operators makes a comparison between two elements and returns a true or false value. These are known as Boolean operators. If the outcome of a Boolean operation is true, the value one (1) is returned; if false, zero (0) is returned. You can use these Boolean operators in computed expressions:

| **Boolean Operator**   | **Description**                                           |
|------------------------|-----------------------------------------------------------|
| >                      | Greater than                                              |
| <                      | Less than                                                 |
| =                      | Equal to                                                  |
| ]                      | Follows (in alphabetical order)                           |
| [                      | Contains (e.g., "AB"["A" is true; "A"["AB" is false)      |
| !                      | Or, either element is true [e.g., (2=3)!(5<10) is true]   |
| &                      | And, both elements are true [e.g., (2=3)&(5<10) is false] |

An apostrophe ( **'** ) means negation or NOT. It can precede any of the Boolean operators. Thus, **6'&gt;8** is read six is not greater than eight, which is true (a one is returned).

**Parentheses in Expressions**

In the absence of parentheses, the expression is evaluated strictly left to right. One operator is not given precedence over another. Use parentheses to control the order in which the operations of a computed expression are performed. Expressions within parentheses are evaluated first. Thus **3+4/2** is 3.5, whereas **3+(4/2)** is 5.

You can also use parentheses to ensure that the enclosed material is treated as an expression when there might be some ambiguity. For example, suppose you want to force a numeric interpretation of the SSN field. You need to use the **+** [unary operator](http://www.hardhats.org/fileman/u2/ce_op.htm) .

However, the following will not yield the desired result:

SORT BY: **+SSN**

Is the **+** the unary operator or the sort specifier (meaning that you want to subtotal results by SSN)? In this case, it will be interpreted as the sort specifier. However, if you put the expression in parentheses, the **+** will definitely be interpreted as an operator:

SORT BY: **(+SSN)**

**Example of Compound Expression**

An example of a computed expression containing several elements and operators is:

"Beds occupied: "\_(NUMBER OF BEDS*OCCUPANCY PERCENTAGE/100)

First, the part within the parentheses is evaluated. NUMBER OF BEDS and OCCUPANCY PERCENTAGE are field names. Their contents are multiplied and the result is divided by 100. That result is concatenated with the literal string "Beds occupied: " giving a result like:

Beds occupied: 484

#### Boolean Logic Primer for Clinical Reminders

*Thanks to Terri Murphy, Durham VAMC, 9/26/01*

1. Findings are either found/present/true for a given patient at a given time, or not (0=not found, 1=found).
2. Logic statements join a series of findings together to form an equation that is overall either true or not.
3. There are four ways to join findings in this logic statement:
    1. AND (&amp;): FI(1)&amp;FI(2) means that both findings 1 and 2 must be found for this overall logic statement to be true.
    2. OR (!): FI(1)!FI(2) means that if either finding 1 or finding 2 is found, then the overall logic statement is true.
    3. AND NOT (&amp;’): FI(1)&amp;’FI(2) means that finding 1 must be found and also finding 2 is not found. Both of these must occur for this overall statement to be true.
    4. OR NOT (!’): FI(1)!’FI(2) means that finding 1 must be found or finding 2 is not found. If either of these occur, the overall logic statement is true.
4. There is a default way that these logic statements are formed, done by the computer, with the findings loaded into the logic statement in the order in which they are entered into the reminder definition. The computer works from left to right to work out the logic statement. This can have unintended consequences. For example, it is not always enough to give a finding an AND to be sure that this finding has to be present for the overall logic statement to be true. For example, let’s say FI(1) is not found (=0), FI(2) is found (=1) and FI(3) is found (=1).

a. FI(1)&amp;FI(2)!FI(3) would be evaluated as overall true, even though FI(1) which was given an AND in the logic field is not found

1. The way around this is to do customized logic, by either changing the order of the findings in the logic statement OR by adding parentheses. The computer calculates the results of things within parentheses first, then goes back and moves from left to right; so, in the example above the outcome is changed with the addition of parentheses:
    1. FI(1)&amp;(FI(2)!FI(3)) would be evaluated as not true because finding 1 is not found. The steps the computer takes are first: FI(2)!FI(3)= true, then FI(1)&amp;(true)=not true, because finding 1 is not found. In this case, giving FI(1) in the logic field worked as intended.
2. This may be overly simplistic, but the way I think of it is to have a series of AND or AND NOTs in the cohort logic (ORs or OR NOTS can be inside parentheses) and a series of ORs in the resolution logic (ANDs, AND NOTs can be inside parentheses). This works for me, but each logic statement needs to be evaluated individually.

- CPRS