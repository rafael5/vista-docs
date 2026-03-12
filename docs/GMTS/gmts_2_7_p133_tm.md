---
app_name: 'CPRS: Health Summary (GMTS)'
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: 2019-05
doc_type: technical-manual
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-11'
is_base: false
is_change_pages: false
library_max_patch: null
package_id: GMTS
patch: 125
patch_gap: null
section: ''
source_file: gmts_2_7_p133_tm.docx
status: draft
title: Health Summary
---

# Health Summary

# Technical Manual

<!-- image -->

**Version 2.7**

**March 2020**

**Department of Veterans Affairs (VA)**

**Office of Information and Technology (OIT)**

## Preface

The Health Summary package integrates clinical data from Veterans Health Administration Information Systems Architecture (VistA) ancillary packages into patient health summaries which can be viewed online or printed as reports.

This manual is intended to be used as a technical reference guide for IRM Service, ADPACs, and Clinical Coordinators.

NOTE: This manual has been revised to describe changes that have been made, through patches, to Health Summary V. 2.7 since its release in 1994.

**Revision History**

| **Revision Date**   | **Page or Chapter**           | **Description**                                                                                                                                                                                                                                                                                                              | **Author**   |
|---------------------|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| 03/16/2020          | Title, i, ii, Appendix D, all | GMTS*2.7*133:  - Moved the section, **New Features in Health Summary** , into **Appendix D** for historical purposes - Updated the Title page, Revision History, and Footers                                                                                                                                                 | REDACTED     |
| 12/31/2019          | Title, 1, 72                  | GMTS*2.7*129:  - Updated Title page, TOC, and footers - Removed instances of Social Work                                                                                                                                                                                                                                     | REDACTED     |
| 06/14/2019          | 3, 30, 81, global             | GMTS*2.7*125:  Pg. 3, Under New Features in Health Summary, added description of GMTS*2.7*125  Pg. 30, under Released Patches for Health Summary 2.7, added GMTS*2.7*125  Pg. 81 Added RACI  Reworded paragraph under ‘Patch GMTS*2.7*125 Updates for Health Summary Components.’  Revised date on Title page and in footers |              |
| 09/14/2018          | 3, 29, 43, 78                 | Updated for GMTS*2.7*94. Added a summary of the patch. Added to a steps that discusses the availability of HS components and the menu option GMTS PS PS MED RECON CONFIG CHECK.                                                                                                                                              |              |
| 11/03/2017          | i, ii, iii, v, 12, and 14     | Updated  for GMTS*2.7*120                                                                                                                                                                                                                                                                                                    |              |
| 09/08/2015          | 27                            | Updated for GMTS*2.7*111                                                                                                                                                                                                                                                                                                     |              |
| June 2014           | 27                            | Edit per Release Coordinator (added ICD-10 screen example)                                                                                                                                                                                                                                                                   |              |
| March 2014          | 25                            | Added description of GMTS*2.7*101                                                                                                                                                                                                                                                                                            |              |
| December, 2013      | 11, 14                        | Added description of GMTS*2.7*107                                                                                                                                                                                                                                                                                            |              |
| Sept 2012           | Throughout manual             | Edits per Release Coordinators                                                                                                                                                                                                                                                                                               |              |
| Apr-June 2012       | 22                            | Added description of GMTS*2.7*104                                                                                                                                                                                                                                                                                            |              |
| Nov 2011            | 22                            | Added description of GMTS*2.7*102                                                                                                                                                                                                                                                                                            |              |
| Aug. 2011           | 12, 34, misc                  | Added description of GMTS*2.7*88 and documented new SHORT HS BY LOCATION FIELD                                                                                                                                                                                                                                               |              |
| April 2011          | 7, 10                         | Added description of GMTS*2.7*92                                                                                                                                                                                                                                                                                             |              |
| November 2010       | n/a                           | Added description of GMTS*2.7*90                                                                                                                                                                                                                                                                                             |              |
| December 2002       | Edits throughout manual.      | Edits per SQA and NVS review.                                                                                                                                                                                                                                                                                                |              |
| October 2002        | Updates throughout manual.    | Added documentation covering functionality exported in patches GMTS*2.7*56 and GMTS*2.7*58.                                                                                                                                                                                                                                  |              |
| March 2002          | Pages 7-8                     | Resolved E3R list updated                                                                                                                                                                                                                                                                                                    |              |
| February 2002       | Pgs 22-24                     | New menu of options enabling managers to control HS types on the reports tab in CPRS                                                                                                                                                                                                                                         |              |
| January 2002        | Throughout                    | Changes made by patches to version 2.7 since its release in 1994, and specifically for patches 29, 45, 47, and 49                                                                                                                                                                                                            |              |

## Table of Contents

Introduction to Health Summary	1

Definition of a Health Summary	1

Packages Providing Data	1

Components and Types	1

Printing Health Summaries	2

PDX Transmission of Health Summaries	2

Health Summary Implementation &amp; Maintenance	2

Set Up Site Parameters	5

Ad Hoc Health Summaries	7

CPRS Interface	7

Relationship to Integrated Billing’s Encounter Form Utilities	7

Nightly Batch Processing	8

Health Summary Components Headers and Abbreviations	8

Customized Health Summary Types	8

Customizing the Ad Hoc Health Summary Type	9

Routine Descriptions	11

Files and Globals List	12

Exported Menus, Options, and Function	14

Cross-References	18

Purging and Archiving	19

Callable Routines	20

External Relations	25

Database Integration Agreements	25

Internal Relations	26

Generating Online Documentation	27

Print Results of the Installation Process	29

Routines	30

Globals	31

XINDEX	31

Data Dictionaries/ Files	32

?, ??, and ??? Online Help	33

Glossary	34

Appendix A—Defining New Components	36

Appendix BHealth Summary Security	45

Menu Access	45

Security	45

Health Summary Type File	46

Owner	46

Lock	46

Health Summary Object File	46

Creator	46

Health Summary Component File	47

Lock	47

VA FileMan File Protection	47

Appendix C: CPRS Program Operations and Maintenance Responsible, Accountable, Consulted and Informed (RACI)	48

Appendix D: Historical Documentation Shift from GMTS*2.7*133 (Do Not Update)	49

New Features in Health Summary	49

Released Patches for Health Summary 2.7	74

Index	77


## Introduction to Health Summary

### Definition of a Health Summary

A health summary is a user-customized, clinical summary report consisting of patient information *components* . Each component presents the most currently available summary data from one of the ancillary packages listed below, for a given patient, with optional limits by time, number of occurrences, and selection items. These summaries can be viewed online or printed.

### Packages Providing Data

Automated Med Info	OE/RR (Order Entry/Results Reporting

Exchange (AMIE)	Outpatient Pharmacy

Allergy Tracking System	Patient Care Encounter (PCE)

Clinical Reminders	Problem List

Consults		Progress Notes

Dietetics	Radiology

Discharge Summary	Registration

Inpatient Medications	Scheduling

Lab		Surgery

Medicine		VISTA Imaging

Mental Health

Nursing (Vital Signs)

### Components and Types

Components and their behavior are specified by records in the Health Summary Component file (142.1). When a “permanent” Health Summary is created, its *type* , as defined by the owner/creator, is saved in the Health Summary Type file (142).

***Definitions***

*Component* Summarized patient data extracted from various DHCP software packages.

*Type* A structure or template containing defined components and unique characteristics.

### Printing Health Summaries

Permanent or pre-defined health summaries may be run or printed for a single patient or all patients at a given hospital location (Patient Health Summary and Hospital Location Health Summary options). If a *clinic or operating room location* is selected (instead of a ward) in the Hospital Location Health Summary option, the user will be prompted to enter a beginning and ending visit or surgery date. Only those patients with visits or surgeries scheduled for the specified date will have health summaries generated.

### PDX Transmission of Health Summaries

Health Summaries (except components with selection items or unique local components) can be transmitted by PDX–Patient Data Exchange–which transfers patient data between VA facilities using the MailMan electronic mail utility. See PDX V. 1.5 documentation for more information.

### Health Summary Implementation &amp; Maintenance

The Health Summary Maintenance Menu contains the following options for implementing and maintaining Health Summary.

| **Option**                                       | **Description**                                                                                                                                                                                                                                                                                                                                                     |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Disable/Enable Health Summary Component**      | Selectively enable or disable Health Summary Components. A disable action may be identified as either temporary or permanent. When a component is temporarily disabled, an “OUT OF ORDER MESSAGE” may be entered and displayed with the component. When permanently disabled, the component is not displayed.                                                       |
| **Create/Modify Health**  **Summary Components** | Create/modify new Health Summary components, either by duplication and renaming of existing components or by entering all appropriate fields for a component created on-site.                                                                                                                                                                                       |
| **Edit Ad Hoc Health Summary Type**              | Enter/edit a component's default parameters (Time and Occurrence limits, Selection Items, Hospital Location Displayed, ICD Text Displayed, Provider Narrative Displayed, Header names, and whether to print component headers if no data is available) or delete components of the Ad Hoc Health Summary Type.                                                      |
| **Rebuild Ad Hoc Health Summary Type**           | Reloads the Ad Hoc Health Summary Type with ALL (previously defined) components, including any defined by the site, and, optionally, all DISABLED components sequenced alphabetically by name. Disabled components will not be displayed, but when they are re-enabled will automatically show up in the Ad Hoc Health Summary if they are included in the rebuild. |
| **Resequence a Health Summary Type**             | Resequence the components of a given Health Summary Type from 5, in increments of 5 (e.g., 5, 10, 15, 20,...,5  *n*  where  *n*  is the total number of components).                                                                                                                                                                                                |

| **Option**                              | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Create/Modify Health Summary Type**   | Create a new or modify an existing health summary type. New types created by this option automatically define the type’s owner as the creator, unless the creator holds the GMTSMGR security key. If the creator has this key, the GMTSMGR holder may designate anyone as the owner.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Health Summary Objects Menu**         | Use this option to access utilities to add/edit a Health Summary Object, display the characteristics of a Health Summary Object, test a Health Summary Object, or export/import a Health Summary Object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Edit Health Summary Site Parameters** | Edit six Health Summary parameters to local specifications.  1) PROMPT FOR ACTION PROFILE; editing this parameter to YES allows users to be prompted for printing a patient’s Outpatient Pharmacy Action Profile in tandem with a health summary.  2) INCLUDE BAR CODE ON ACTION PROFILES; editing this parameter to YES allows bar codes to be printed with Action Profiles.  3) INCLUDE COMMENTS ON LABS; editing this parameter to YES causes comments to be printed in the Chemistry and Hematology, the Lab Test Selected, and the Lab Cumulative components.  4) SPOOL DEVICE; specify spool device name to which Health Summary output can be directed during a PDX request.  5) SHORT HS BY LOCATION COVER; allow the number of times each location prints on the cover sheet to change from 6 to 1.  6) ERROR MESSAGE RECIPIENT: This is the user or mail group that will receive error messages from the Health Summary Package when they are sent. Instances of when  error messages are sent would be when a tasked batch print job needs to exit without producing a report. |


### Set Up Site Parameters

Use the Edit Health Summary Site Parameters option in the Health Summary Maintenance Menu [GMTS IRM/ADPAC MAINT MENU] to review and set up the site parameters. These parameters allow users to:

- Print an Outpatient Pharmacy Action Profile in tandem with a Health Summary.

- Print bar codes when Action Profiles are printed.

- Present Lab comments at display indicating comments are available for the Lab Chemistry and Hematology, the Lab Cumulative Selected, and the Lab Tests Selected components, or present the !! symbol to indicate comments are available for the Chemistry and Hematology and Lab Tests Selected components.

- Specify a spool device where PDX requests will be stored.

- Change the number of times each location prints on the cover sheet from 6 times to 1 time.

See example on next page.

***Example***

Select Health Summary Maintenance Menu Option: **7** Edit Health Summary Site Parameters

Select HEALTH SUMMARY PARAMETERS: **?**

ANSWER WITH HEALTH SUMMARY PARAMETERS NAME:

HOSPITAL

YOU MAY ENTER A NEW HEALTH SUMMARY PARAMETERS, IF YOU WISH

NAME MUST BE HOSPITAL

Select HEALTH SUMMARY PARAMETERS: **HOSPITAL**

PROMPT FOR ACTION PROFILE: YES// **??**

If this parameter is set to Y or YES, the user will be prompted to

include the Outpatient Pharmacy Action Profile when printing Health

Summaries by location (both interactive and batch mode) and by patient.

CHOOSE FROM:

Y        yes

N        no

PROMPT FOR ACTION PROFILE: YES// **Y** YES

INCLUDE BAR CODES ON ACTION PROFILES: **?**

Enter YES to include bar codes when Action Profiles are printed by

Health Summary

Choose from:

Y        yes

N        no

INCLUDE BAR CODES ON ACTION PROFILES: YES// **&lt;RET&gt;   YES**

INCLUDE COMMENTS FOR LABS: YES// **??**

If this parameter is set to Y or YES, the Chemistry &amp; Hematology, the

Lab Tests Selected, and the Lab Cumulative Selected components will

present comments for results. For the Chemistry &amp; Hematology and the 	Lab Tests Selected components, the comments will be displayed 	immediately following the results. For the Lab Cumulative Selected 	components, a lower-case letter will be displayed to the left of the 	date for entries with comments. Comments will be displayed after all 	the results are displayed , with the comments linked by the lower-case 	letter. Up to 26 comments can be included.

If blank, N or NO, the Chemistry &amp; Hematology and the Lab Tests components 	will present the symbol "!!" next to tests which include

comments, and a footnote referring the user to the Lab Interim Report.

CHOOSE FROM:

Y        yes

N        no

INCLUDE COMMENTS FOR LABS: YES// **&lt;RET&gt;** YES

SPOOL DEVICE: SPOOL// **??**

This is the SPOOL DEVICE to which Health Summary output can be directed

during a PDX request for one or more Health Summary components.

Choose from:

SPOOL		SPOOL TO VMS		DSAB:[MUMPS,DEVMGR]

SPOOL DEVICE : **SPOOL**

SHORT HS BY LOC COVERS: Yes// ??

This parameter is to be used in conjunction with the Hospital Location

Health Summary [GMTS HS BY LOC] report to shorten the cover page for

each location.  When printing in standard Letter (8.5 x 11) format, the

name of the hospital location is printed six times which results in an

overflow onto the next page.  If this parameter is set to 'Y' the name

will only print one time, thus saving paper.

Choose from:

N        No

Y        Yes

SHORT HS BY LOC COVERS: Yes//

Select HEALTH SUMMARY PARAMETERS: **&lt;RET&gt;**

### Ad Hoc Health Summaries

Temporary (ad hoc) health summaries can be created “on-the-fly” and run for individual patients, as follows.

1. First, select a combination of components from a menu of all available components.
2. Next, (if applicable) specify time limits, occurrence limits, hospital location, ICD text display, provider narrative display, and selection items for any of the components, or accept site-defined defaults.
3. Then, select a patient and run the resulting health summary.

Both pre-defined and ad hoc health summaries may be run interactively on your terminal or directed to any printer. Pre-defined health summary types can also be queued to run nightly for all patients at any specified location(s). Either interactive or batch-mode print-by-location health summaries may also be printed “in tandem” with the Outpatient Pharmacy Action Profile (including bar codes) for each of the patients at the selected location.

### CPRS Interface

Health Summary V. 2.7 interfaces with the Computerized Patient Record System (CPRS)  to provide Order Entry users with an integrated view of both *orders* (from CPRS) and *results* (from Health Summary). This interface, in turn, enhances Health Summary by allowing Health Summary users:

*Multiple Patient Selection* .

You can select multiple patients from ward, clinic, treating specialty, attending physicians, personal or team lists. Health Summary uses enhanced patient look-up routines in CPRS for reporting results.

### Relationship to Integrated Billing’s Encounter Form Utilities

The Integrated Billing package (Encounter Form Utilities) includes a Print Manager that allows sites to define reports that should print along with encounter forms for a specific clinic or division and for specified appointments. One of the options, “Define Available Health Summary”, allows a health summary to be made available for use by the print manager. See the *IB Encounter Form Utilities User Manual* for further information.

### Nightly Batch Processing

The Health Summary package allows coordinators to schedule batch processing of health summaries for patients in a particular ward, or to schedule batch processing of health summaries a specified number of days before patients are scheduled for clinic visits or operating rooms. The benefits of batch processing are.

1)	It enables the clinic to have the most currently available clinical information when the patient arrives for the appointment, and

2)	Processing of the prints takes place during non-peak computer hours.

To use this, feature the IRM Service must first use the option Schedule/Unschedule Options on the TaskMan menu, and schedule the GMTS TASK STARTUP option to initiate nightly batch printing. (See page 31 in the *Health Summary Installation Guide.* ) Each time this option runs, it uses the parameters set up by the Health Summary Coordinator in the Set-up Batch Print Locations option. For Version 2.7 of Health Summary, this option has been updated to recognize non-workdays. For clinics and operating rooms, if it is set up to print two days in advance, Tuesday’s clinics will print on Friday rather than on Sunday. If Tuesday happens to be a holiday, the Wednesday clinics will print on Friday.

### Health Summary Components Headers and Abbreviations

Use the Information Menu option (available in all three Health Summary user menus) to get an online listing of the information contained in each health summary component or health summary type.

### Customized Health Summary Types

A user with access to the Coordinator’s or Enhanced menu can create a customized health summary type. Use the Create/Modify Health Summary Type menu option located on the Health Summary Enhanced Menu or the Build Health Summary Type submenu of the Health Summary Coordinator’s menu. Select the desired components, and (depending on the data required by the selected components) apply time limits or maximum occurrence limits to components which are date-sensitive. You may also apply ICD text, provider narrative, selection items, and header names for components that allow these to be specified.

Users who do not have access to the enhanced or coordinator's menus can request a customized health summary type from their IRMS or Health Summary coordinator. The form entitled “Request for Health Summary Type”, located in Appendix A of the *Health Summary User Manual,* is a convenient way to submit such requests.

### Customizing the Ad Hoc Health Summary Type

You can also customize the Ad Hoc Health Summary Type with the Edit Ad Hoc Health Summary Type option on the Maintenance Menu. This option lets you modify time and/or occurrence limits, hospital location displayed, ICD text displayed, provider narrative displayed, header names, or assign selection items (tests like WBC, Glucose) to the *selected* health summary components (Lab Cumulative Selected, Lab Cumulative Selected 1-4, Lab Tests Selected, Measurement Selected, Vital Signs Selected, and Radiology Impression Selected, etc.). Consult with your clinical coordinator and/or users about which selection items they would like to have on their Health Summaries.

You may select individual components and edit their default parameters or use the ^LOOP feature at the Select COMPONENT: prompt to loop through all of the components, editing the default values as you go.

**NOTE:** When selecting components from the Ad Hoc Health Summary menu, entering “ALL” allows all components to be selected. If the first three characters of a Header Name for a component are designated as “All”, however, then only the defined component will be selected. Avoid conflicts and loss of functionality by not using “all” at the front of new header names.

**Edit Ad Hoc Health Summary Type Example**

**NOTE:** Bold-faced text indicates user entries.

Select Health Summary Overall Menu Option Name: **Health Summary Maintenance Menu**

1      Disable/Enable Health Summary Component

2      Create/Modify Health Summary Components

3      Edit Ad Hoc Health Summary Type

4      Rebuild Ad Hoc Health Summary Type

5      Resequence a Health Summary Type

6      Create/Modify Health Summary Type

7      Edit Health Summary Site Parameters

Select Health Summary Maintenance Menu Option: **Edit Ad Hoc** Health Summary Type

Edit Ad Hoc Health Summary Type

&gt;&gt;&gt; EDITING the GMTS HS ADHOC OPTION Health Summary Type

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA:

Do you wish to review the Summary Type structure before continuing? NO// **&lt;RET&gt;**

Select COMPONENT: PROB

1   PROBLEM LIST ACTIVE             PLA

2   PROBLEM LIST ALL                PLL

3   PROBLEM LIST INACTIVE           PLI

CHOOSE 1-3: **1**

SUMMARY ORDER: 5// **&lt;RET&gt;** 5

ICD TEXT DISPLAYED: **??**

This field controls how ICD text is displayed in components where ICD

Text applies (e.g., PCE Outpatient Encounters, PCE Outpatient Diagnosis

and Problem List All). The applicable component display/print can be

customized to include ICD Text in the following format: code and long

description, code and short description, code only, long description only

or nothing. This control is independent of whether provider narrative is

displayed -- either or both may be specified.

Choose from:

L        long text

S        short text

C        code only

T        text only

N        none

ICD TEXT DISPLAYED: **S** short text

PROVIDER NARRATIVE DISPLAYED: **??**

This field controls whether provider narrative is displayed or not. It

applies to components where provider narrative is applicable (e.g., PCE

Outpatient Encounters, PCE Outpatient Diagnosis, Problem List All). This

control is independent of whether or not ICD text is displayed -- either

or both may be specified. If not specified, provider narrative will be

displayed by default.

Choose from:

Y        yes

N        no

PROVIDER NARRATIVE DISPLAYED: **Y** yes

HEADER NAME: Active Problems// **&lt;RET&gt;**

Select COMPONENT: **&lt;RET&gt;**

Do you wish to review the Summary Type structure before continuing? NO// **&lt;RET&gt;YES**

HEALTH SUMMARY TYPE INQUIRY

Type Name:  GMTS HS ADHOC OPTION

Title:  Ad Hoc Health Summary Type

Owner:                          LOCK:  GMTSMGR

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA:

Max        Hosp  ICD    Prov

Abb.  Order   Component Name         Occ  Time  Loc   Text   Narr  Selection

------------------------------------------------------------------------------

PLA   5       Active Problems                         short  yes

* = Disabled Components

Select COMPONENT:&lt;RET&gt;


## Routine Descriptions

**Namespace:** *GMTS*

XUPRROU (List Routines) prints a list of any or all of the Health Summary routines. This option is found on the XUPR-ROUTINE-TOOLS menu on the XUPROG (Programmer Options) menu, which is a sub-menu of the EVE (Systems Manager Menu) option.

Select Systems Manager Menu Option: **programmer** Options

Select Programmer Options Option: **routine Tools**

Select Routine Tools Option: **list Routines**

Routine Print

Want to start each routine on a new page: No// **[ENTER]**

routine(s) ?   &gt; **GMTS***

The first line of each routine contains a brief description of the general function of the routine. Use the Kernel option XU FIRST LINE PRINT (First Line Routine Print) to print a list of just the first line of each GMTS subset routine.

Select Systems Manager Menu Option: **programmer** Options

Select Programmer Options Option: **routine Tools**

Select Routine Tools Option: **First Line Routine Print**

PRINTS FIRST LINES

routine(s) ?   &gt; **GMTS***

## Files and Globals List

The following is a list of the files contained in the Health Summary package, including file number, name, global location, and an indicator if data comes with the file.

**Number	Name                   			Global		Data**

**142** HEALTH SUMMARY TYPE	^GMT(142,	YES

**Description**

This file contains the structure of a health summary. Components from the Health

Summary Components file (142.1) may be selected and restricted by number of

occurrences or time limits. The original creator of a type of Health Summary is the

owner of that type. Health summaries that are “owned” may not be modified or

deleted by anyone except the Clinical Coordinator. “Owned” Health Summaries may

be used by other users to print patient information.

**142.1** HEALTH SUMMARY COMPONENT	^GMT(142.1,	YES

**Description**

This file contains all components which may be used to create a Health Summary.

These entries are typically defined by a programmer. Components which represent

packages that are not in use may be disabled, so they will not be selected by users to

build new types of health summary reports.

**142.5** HEALTH SUMMARY OBJECTS	^GMT(142.5,	NO

**Description**

This file contains Health Summary Types that are to be embedded into another document as an object. The bulk of this file is made up of display flags which control how the object is to be embedded into the other document.

**142.98** HEALTH SUMMARY USER PREFERENCES        ^GMT(142.98,          YES

**Description**

This file determines how the list of Health Summary Types for the CPRS GUI report tab is to be organized (APPEND or OVERWRITE) for user selection. There are three major classes of Health Summary types, National (remote data view), user defined and system defined. User and system Health Summary Types are defined in the Kernel Parameters file. Append creates a single list, removing duplicates, and keeps the National Health Summary types group together. Overwrite stops building the list once a single group of Health Summary Types (User or System) is added to the list.

**142.99** HEALTH SUMMARY PARAMETERS	^GMT(142.99,	NO

**Description**

This file contains any site parameters that apply to the Health Summary package.

Currently there are six site parameters: 1) PROMPT FOR ACTION PROFILE; 2) INCLUDE BAR CODE ON ACTION PROFILES;  3) INCLUDE COMMENTS ON LABS;  4) SPOOL DEVICE 5) ERROR MESSAGE RECIPIENT; 6) SHORT HS BY LOCATION COVER

## Exported Menus, Options, and Function

The Health Summary Overall Menu [GMTS MANAGER] contains four menus.

1.	Health Summary Menu [GMTS USER]

2. Health Summary Enhanced Menu [GMTS ENHANCED USER]

3. Health Summary Coordinator’s Menu [GMTS COORDINATOR]

4. Health Summary Maintenance Menu [GMTS IRM/ADPAC MAINT MENU]

Assign these menus as follows.

1.	Give the Health Summary Menu [GMTS USER] menu to users who only need to print or display health summaries.

2.	Give the Health Summary Enhanced Menu [GMTS ENHANCED USER] menu to users who need to create, modify, or delete their *own* health summary types, in addition to printing health summaries.

3.	Give the Health Summary Coordinator’s Menu [GMTS COORDINATOR] menu to users who need to print or display health summaries, and who will also need to create, modify, or delete health summary types, and set up nightly batch printing at specified locations.

4.	Give the Health Summary Maintenance Menu [GMTS IRM/ADPAC MAINT MENU] to IRM staff or the Clinical Coordinator for any implementation and maintenance issues in Health Summary. This menu contains options to disable/enable health summary components for selection/display, create/modify new health summary components, edit and rebuild the Ad Hoc Health Summary Type, resequence the components in a health summary type, create/modify a health summary type, delete a health summary type, and edit health summary site parameters. With the release of GMTS*2.7*94 patch, it also contains a new GMTS PS MED RECON CONFIG CHECK option which will check the HEALTH SUMMARY TYPE ‘Essential Med List for Review’ to make sure it holds certain HEALTH SUMMARY COMPONENTs for which it was created in the first place.

5.	If an IRM staff member or the Clinical Coordinator needs access to all menus, give the Health Summary Overall Menu [GMTS MANAGER] to those users rather than assigning each menu option separately.

**Health Summary Overall Menu** [GMTS MANAGER]

**NOTE:** New menus and options (since the original release of v2.7) are highlighted in blue.

**1. Health Summary Coordinator’s Menu** [GMTS COORDINATOR]

1 Print Health Summary Menu ... [GMTS HS MENU]

1 Patient Health Summary [GMTS HS BY PATIENT]

2 Ad Hoc Health Summary [GMTS HS ADHOC]

3 Range of Dates Patient Health Summary [GMTS HS BY PATIENT &amp; DATE RANG]

4 Visit Patient Health Summary [GMTS HS BY PATIENT &amp; VISIT]

5 Hospital Location Health Summary [GMTS HS BY LOC]

6 Batch Print of All Clinics by Visit Date [GMTS HS FOR ALL CLINICS]

2 Build Health Summary Type Menu ... [GMTS BUILD MENU]

1 Create/Modify Health Summary Type [GMTS TYPE ENTER/EDIT]

2 Delete Health Summary Type [GMTS TYPE DELETE]

3 Information Menu ... [GMTS INFO ONLY MENU]

1 Inquire about a Health Summary Type [GMTS TYPE INQ]

2 List Health Summary Types [GMTS TYPE LIST]

3 Inquire about a Health Summary Component [GMTS COMP INQ]

4 List Health Summary Components [GMTS COMP LIST]

5 List Health Summary Component Descriptions [GMTS COMP DESC LIST]

4 Print Health Summary Menu ... [GMTS HS MENU]

1 Patient Health Summary [GMTS HS BY PATIENT]

2 Ad Hoc Health Summary [GMTS HS ADHOC]

3 Range of Dates Patient Health Summary [GMTS HS BY PATIENT &amp; DATE RANG]

4 Visit Patient Health Summary [GMTS HS BY PATIENT &amp; VISIT]

5 Hospital Location Health Summary [GMTS HS BY LOC]

6 Batch Print of All Clinics by Visit Date [GMTS HS FOR ALL CLINICS]

3 Set-up Batch Print Locations [GMTS HS BY LOC PARAMETERS]

4 List Batch Health Summary Locations [GMTS TASK LOCATIONS LIST]

5 CPRS Reports Tab 'Health Summary Types List' Menu [GMTS GUI REPORTS LIST

MENU]

1 Display 'Health Summary Types List' Defaults [GMTS GUI HS LIST

DEFAULTS]

2 Precedence of 'Health Summary Types List' [GMTS GUI HS LIST

PRECEDENCE]

3 Method of compiling 'Health Summary Types List' [GMTS GUI HS LIST

METHOD]

4 Edit 'Health Summary Types List' Parameters [GMTS GUI HS LIST

PARAMETERS]

**2. Health Summary Enhanced Menu** [GMTS ENHANCED USER]

1 Patient Health Summary [GMTS HS BY PATIENT]

2 Ad Hoc Health Summary [GMTS HS ADHOC]

3 Range of Dates Patient Health Summary [GMTS HS BY PATIENT &amp; DATE RANG]

4 Visit Patient Health Summary [GMTS HS BY PATIENT &amp; VISIT]

5 Hospital Location Health Summary [GMTS HS BY LOC]

6 Information Menu ... [GMTS INFO ONLY MENU]

1 Inquire about a Health Summary Type [GMTS TYPE INQ]

2 List Health Summary Types [GMTS TYPE LIST]

3 Inquire about a Health Summary Component [GMTS COMP INQ]

4 List Health Summary Components [GMTS COMP LIST]

5 List Health Summary Component Descriptions [GMTS COMP DESC LIST]

7 Create/Modify Health Summary Type [GMTS TYPE ENTER/EDIT]

8 Delete Health Summary Type [GMTS TYPE DELETE]

9 CPRS Reports Tab 'Health Summary Types List' Menu [GMTS GUI REPORTS

LIST MENU]

1 Display 'Health Summary Types List' Defaults [GMTS GUI HS LIST

DEFAULTS]

2 Precedence of 'Health Summary Types List' [GMTS GUI HS LIST

PRECEDENCE]

3 Method of compiling 'Health Summary Types List' [GMTS GUI HS LIST

METHOD]

4 Edit 'Health Summary Types List' Parameters [GMTS GUI HS LIST

PARAMETERS]

**3. Health Summary Menu** [GMTS USER]

1 Patient Health Summary [GMTS HS BY PATIENT]

2 Ad Hoc Health Summary [GMTS HS ADHOC]

3 Range of Dates Patient Health Summary [GMTS HS BY PATIENT &amp; DATE RANG]

4 Visit Patient Health Summary [GMTS HS BY PATIENT &amp; VISIT]

5 Hospital Location Health Summary [GMTS HS BY LOC]

6 Information Menu ... [GMTS INFO ONLY MENU]

1 Inquire about a Health Summary Type [GMTS TYPE INQ]

2 List Health Summary Types [GMTS TYPE LIST]

3 Inquire about a Health Summary Component [GMTS COMP INQ]

4 List Health Summary Components [GMTS COMP LIST]

7 CPRS Reports Tab 'Health Summary Types List' Menu [GMTS GUI REPORTS

LIST MENU]

1 Display 'Health Summary Types List' Defaults [GMTS GUI HS LIST

DEFAULTS]

2 Precedence of 'Health Summary Types List' [GMTS GUI HS LIST

PRECEDENCE]

3 Method of compiling 'Health Summary Types List' [GMTS GUI HS

LIST METHOD]

4 Edit 'Health Summary Types List' Parameters [GMTS GUI HS LIST

PARAMETERS]

**4. Health Summary Maintenance Menu** [GMTS IRM/ADPAC MAINT  MENU]

1 Disable/Enable Health Summary Component [GMTS IRM/ADPAC ENABLE/DISABLE]

2 Create/Modify Health Summary Components [GMTS IRM/ADPAC COMP EDIT]

3 Edit Ad Hoc Health Summary Type [GMTS IRM/ADPAC ADHOC EDIT]

4 Rebuild Ad Hoc Health Summary Type [GMTS IRM/ADPAC ADHOC LOAD]

5 Resequence a Health Summary Type [GMTS IRM/ADPAC TYPE RESEQUENCE]

6 Create/Modify Health Summary Type [GMTS TYPE ENTER/EDIT]

7 Edit Health Summary Site Parameters [GMTS IRM/ADPAC PARAMETER EDIT]

8 Health Summary Objects Menu [GMTS OBJ MENU]

1 Create/Modify Health Summary Object [GMTS OBJ ENTER/EDIT]

2 Inquire about a Health Summary Object [GMTS OBJ INQ]

3 Test a Health Summary Object [GMTS OBJ TEST]

4 Delete Health Summary Object [GMTS OBJ DELETE]

5 Export/Import a Health Summary Object [GMTS OBJ EXPORT/IMPORT]

1 Export a Health Summary Object [GMTS OBJ EXPORT]

2 Import/Install a Health Summary Object [GMTS OBJ IMPORT/INSTALL]

9 CPRS Reports Tab 'Health Summary Types List' Menu [GMTS GUI REPORTS

LIST MENU]

1 Display 'Health Summary Types List' Defaults [GMTS GUI HS LIST

DEFAULTS]

2 Precedence of 'Health Summary Types List' [GMTS GUI HS LIST

PRECEDENCE]

3 Method of compiling 'Health Summary Types List' [GMTS GUI HS

LIST METHOD]

4 Edit 'Health Summary Types List' Parameters [GMTS GUI HS LIST

PARAMETERS]

10 CPRS Health Summary Display/Edit Site Defaults [GMTS GUI SITE DEFAULTS]

1 Display Site Health Summary List Defaults [GMTS GUI SITE DISPLAY

DEFAULTS]

2 Edit 'Health Summary Types List' Parameters [GMTS GUI SITE

ADD/EDIT LIST]

3 Edit Default HS Type List Compile Method [GMTS GUI SITE COMPILE

METHOD]

4 Add/Edit Allowable Entities for HS List [GMTS GUI SITE PRECEDENCE]

5 Resequence Allowable Entities for HS List [GMTS GUI SITE

RESEQUENCE]

**Function**

Health Summary exports a function called GMTS COMPONENT NAME. It is used for writing the HEADER NAME, DEFAULT HEADER NAME, or COMPONENT NAME in Health Summary reports.

## Cross-References

The number-space for Health Summary files is 142*. Use the VA FileMan DATA DICTIONARY UTILITIES, option #8 ( DILIST, List File Attributes), to print a list of these files. Depending on the FileMan template used to print the list, this option will print out all or part of the data dictionary for the GMTS files. If you choose the “Standard” format, you can see cross-reference information for a specified file(s).


## Purging and Archiving

**Archiving**

The Health Summary package does not provide archiving functionality because data is only stored for the Health Summary Type (#142), Health Summary Component (#142.1), and Health Summary Parameters (#142.99) files.

The Health Summary package does not duplicate storage of VISTA ancillary package data. Data is extracted as needed from the ancillary packages, is temporarily stored in ^TMP(&lt;namespace&gt;,$J, or ^UTILITY($J, and is deleted after the component has been printed or displayed.

**Purging**

The Delete Health Summary Type option [GMTS TYPE DELETE] is available on both the Coordinator’s and the Enhanced menus. The owner of a health summary type may delete it.

Privacy Act laws specifically state that patient information in VISTA which is retrievable by patient identifier is part of the patient medical record. Printed Health Summary information is patient information that is retrievable by patient identifier and is considered part of the patient record. However, since the information on the Health Summary can be found elsewhere in the patient record, administrators in a Medical Center can choose whether or not to file hard copies of health summaries in the medical record. If you choose to file copies in the medical record, be aware that *information in a health summary is only a summary and may not be complete in many cases* .

## Callable Routines

Health Summary does not provide any publicly supported entry points. Included below is a list of entry points that are used by the Health Summary package. Use of these entry points by other packages requires a private Data Base Integration Agreement (DBIA) with Health Summary.

**Routine: GMTS** : *Health Summary Main Routine*

| **Entry Point**   | **Comments**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ENCWA             | Entry point for printing without going through Health Summary print options and a pre-defined health summary type.  Receives:	DFN as valid patient internal entry number  GMTSPRM = “CD, CN,CW,ADR”. These are  valid component abbreviations from the “C”  cross reference of File 142.1. Does not support  components that require selection items.  GMTSTITL=“Text of Title”  GMTSPX1 - Optional internal FM date for range ending date  GMTSPX2 - Optional internal FM date for range beginning date  NOTE: 	Optional date range variables are both required  if a date range is desired.  Returns:	Health Summary report for a patient and the  specific components defined in GMTSPRM. |

**Routine: GMTSADOR** : *Ad Hoc Summary Driver*

| **Entry Point**   | **Comments**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MAIN              | Entry point to allowing the user to define components and defaults through the Ad Hoc menu interface and print health summaries for a programmer-specified patient and device.  Receives:	DFN as valid patient internal entry number. If DFN is not defined but the ORVP variable is, DFN will be set to the DFN in this variable. This is done to allow this entry point to be called through a protocol in support of OE/RR. If DFN and ORVP don’t exist, the user will be prompted to enter a  patient. |

**Routine: GMTSDVR** : *Health Summary Alternate Driver (OE/RR V2.5 compatible)*

| **Entry Point**                        | **Comments**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ENX(DFN,  GMTSTYP,  GMTSPX2,  GMTSPX1) | Entry point, with parameters, for printing a health summary  for a programmer-specified patient and device, without prompting  for additional information.  Receives:	DFN as valid patient internal entry number  GMTSTYP as a valid health summary type 		internal entry number.  GMTSPX1 and GMTSPX2 are optional Date and 	Range variables. They allow the time limits to be 	overridden for components that use time limits. 	Thus, beginning and ending dates can be  specified in order to get only data within that  time range.  GMTSPX2 - Internal FileMan date for beginning date range  GMTSPX1 - Internal FileMan date for ending date range |

**Routine: GMTSDVR** : *Health Summary Alternate Driver (OE/RR V2.5 compatible) cont’d*

| **Entry Point**   | **Comments**                                                                                                                                                                                                                                                                                                                             |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ENXQ              | External call for tasked Health Summary printing.  Receives:	DFN as valid patient internal entry number  GMTSTYP as a valid health summary type  IEN  GMTSPX1 - Optional internal FM date for ending date  GMTSPX2 - Optional FM date for beginning date  NOTE:  Optional date range variables are both required if a date range is used |

**Routine: GMTSOBJ** : *Health Summary Objects*

| **Entry Point**                                               | **Comments**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OBJ  INQ  DEL  TEST  GET(DFN,OBJ)  TIU(DFN,OBJ)  DIS(DFN,OBJ) | Create/Modify Health Summary Object - GMTS OBJ ENTER/EDIT  Inquire to Health Summary Object - GMTS OBJ INQ  Delete Health Summary Object - GMTS OBJ DELETE  Test Health Summary Object - GMTS OBJ TEST  Get Health Summary Object  Input:   DFN   IEN for Patient (file #2)  OBJ   IEN for Health Summary Object (file #142.5)  Output  Returns global array of Health Summary data  ^TMP("GMTSOBJ",$J,DFN,#)  Get Health Summary Object  (Entry Point for TIU)  Input    DFN   IEN for Patient (file #2)  OBJ   IEN for Health Summary Object (file #142.5)  Output Returns global array of Health Summary data  ^TMP("TIUHSOBJ",$J,"FGBL",0)  ^TMP("TIUHSOBJ",$J,"FGBL",#)  Display Object  Input    DFN   IEN for Patient (file #2)  OBJ   IEN for Health Summary Object (file #142.5) |

**Routine: GMTSU** : *Health Summary Utilities routine*

| **Entry Point**                         | **Comments**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **MTIM**  REGDT  REGDTM  SIDT  FMHL7DTM | Converts time from an internal format to a display format.  Receives: 	X=internal format Date/time as 2900310.1300  Returns: 	X=printable time as 13:00  Gets internal date and formats as MM/DD//YY  Receives: 	X=internal format Date/time as 2900310.1300  Returns:	X=03/10/90  Gets regular date and formats with time.  Receives: 	X=internal format Date/time as 2900310.1300  Returns:	X=03/10/90 13:00  Gets date in SI format as DD MMM YY  Receives:	X as internal FM date/time, e.g., 2890630.1650  Returns:	X=30 JUN 89  Gets HL7 format date/time as CCYYMMDDHHMM  Receives:	X=internal format 2900310.1300 as Date/time  Returns:	      X=29003101300 |

**Routine: GMTSU** : *Health Summary Utilities routine cont’d*

| **Entry Point**                          | **Comments**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DEM  NAME  GETRANGE  (Fromdate,  Todate) | Gets Demographic data from VADPT  Receives:	DFN  Returns: 	GMTSPNM,GMTSSN,GMTSDOB,SEX,  GMTSWARD,GMTSRB,GMTSAGE  Formats names.  Receives: 	FILE=(200)  IFN=(internal file number for above file),  NML=(desired length for name to be returned)  FNF=0 for FI, 1 for FN (flag to specify first name  format)  Returns:	NM=Lastname,First(name/initial) to specified  length.  Receives:	Fromdate and Todate which are variables (passed  by reference) that will return the From date and  the To date in inverted order.  Fromdate Inverted date to be used as stop date for displaying most recent data first.  Todate Inverted date to be used as start date for 	                 displaying most recent data first. |

**Routine: GMTSUP** : *Pagination Utilities*

| **Entry Point**          | **Comments**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CKP  CKP1  BREAK  HEADER | Called from all component print routines; before printing  each line checks $Y and flags form feeds.  Receives:	DFN as valid patient internal entry number  Returns:	GMTSNPG=0; No form feed has been forced  GMTSNPG=1; Form feed has been forced  GMTSQIT=defined when an up-arrow (^) has  been entered to quit summary  Help display of the optional components for navigation.  Called from CKP before printing the component data and when form feeds are forced. Writes the delimiter of each component.  Called from the driver at the beginning of the summary, and from CKP when form feeds are forced. Writes the running head of the summary report. |

## External Relations

Non-destructive, read-only component routines have been written to present VISTA ancillary package data.

### Database Integration Agreements

The Health Summary package interacts with, and extracts data from many other VISTA software packages. Permission for Health Summary to use data from the other packages is obtained by completing a written integration agreement with each of the other packages. Complete integration agreements are under the DBA menu on Forum.

## Internal Relations

All Health Summary options are independently invokable.

## Generating Online Documentation

**KIDS Build and Install Print Options**

**Print a list of package components**

Use the KIDS Build File Print option if you would like a complete listing of package components (e.g., routines and options) exported with this software.

&gt; **D ^XUP**

Setting up programmer environment

Terminal Type set to: C-VT100

Select OPTION NAME: **XPD MAIN** Kernel Installation &amp; Distribution System menu

Select Kernel Installation &amp; Distribution System Option: **U** tilities

Select Utilities Option: **B** uild File Print

Select BUILD NAME: **GMTS*2.7*58** HEALTH SUMMARY

DEVICE: HOME// **;;999** ANYWHERE

PACKAGE: GMTS*2.7*58     Dec 30, 2002 8:57 am                         PAGE 1

------------------------------------------------------------------------------

TYPE: SINGLE PACKAGE

TRACK NATIONALLY: YES

NATIONAL PACKAGE: HEALTH SUMMARY

DESCRIPTION:

The description of this build is found in the National Patch Module under

patch GMTS*2.7*58.

ENVIRONMENT CHECK :

PRE-INIT ROUTINE :

POST-INIT ROUTINE : POST^GMTSP58

PRE-TRANSPORT RTN :

UP    SEND  DATA                USER

DATE  SEC.  COMES  SITE   RSLV  OVER

FILE #      NAME                         DD    CODE  W/FILE DATA   PTS   RIDE

------------------------------------------------------------------------------

142.5       HEALTH SUMMARY OBJECTS       YES   YES   NO

INPUT TEMPLATE:

GMTS DELETE HLTH SUM TYPE    FILE #142         SEND TO SITE

GMTS EDIT EXIST HS TYPE    FILE #142           SEND TO SITE

GMTS EDIT HLTH SUM TYPE    FILE #142           SEND TO SITE

ROUTINE:

GMTS1                                          SEND TO SITE

GMTS2                                          SEND TO SITE

GMTSALG                                        SEND TO SITE

GMTSCNB                                        SEND TO SITE

GMTSDEM2                                       SEND TO SITE

GMTSLRC                                        SEND TO SITE

GMTSLROB                                       SEND TO SITE

GMTSLRS                                        SEND TO SITE

GMTSLRS7                                       SEND TO SITE

GMTSLRSC                                       SEND TO SITE

GMTSLRTE                                       SEND TO SITE

GMTSOBA                                        SEND TO SITE

GMTSOBA2                                       SEND TO SITE

GMTSOBD                                        SEND TO SITE

GMTSOBE                                        SEND TO SITE

GMTSOBH                                        SEND TO SITE

GMTSOBI                                        SEND TO SITE

GMTSOBJ                                        SEND TO SITE

GMTSOBL                                        SEND TO SITE

GMTSOBL2                                       SEND TO SITE

GMTSOBS                                        SEND TO SITE

GMTSOBS2                                       SEND TO SITE

GMTSOBT                                        SEND TO SITE

GMTSOBU                                        SEND TO SITE

GMTSOBV                                        SEND TO SITE

GMTSPXFP                                       SEND TO SITE

GMTSRASP                                       SEND TO SITE

GMTSRM                                         SEND TO SITE

GMTSULT                                        SEND TO SITE

GMTSULT5                                       SEND TO SITE

GMTSUP                                         SEND TO SITE

GMTSVSD                                        SEND TO SITE

GMTSXAB                                        SEND TO SITE

OPTION:

GMTS BUILD MENU                                USE AS LINK FOR MENU ITEMS

GMTS GUI HS LIST DEFAULTS                      SEND TO SITE

GMTS GUI HS LIST METHOD                        SEND TO SITE

GMTS GUI HS LIST PARAMETERS                    SEND TO SITE

GMTS GUI HS LIST PRECEDENCE                    SEND TO SITE

GMTS GUI REPORTS LIST MENU                     SEND TO SITE

GMTS GUI SITE ADD/EDIT LIST                    SEND TO SITE

GMTS GUI SITE COMPILE METHOD                   SEND TO SITE

GMTS GUI SITE DEFAULTS                         SEND TO SITE

GMTS GUI SITE DISPLAY DEFAULTS                 SEND TO SITE

GMTS GUI SITE PRECEDENCE                       SEND TO SITE

GMTS GUI SITE RESEQUENCE                       SEND TO SITE

GMTS IRM/ADPAC MAINT MENU                      USE AS LINK FOR MENU ITEMS

GMTS OBJ DELETE                                SEND TO SITE

GMTS OBJ ENTER/EDIT                            SEND TO SITE

GMTS OBJ EXPORT                                SEND TO SITE

GMTS OBJ EXPORT/IMPORT                         SEND TO SITE

GMTS OBJ IMPORT/INSTALL                        SEND TO SITE

GMTS OBJ INQ                                   SEND TO SITE

GMTS OBJ MENU                                  SEND TO SITE

GMTS OBJ TEST                                  SEND TO SITE

GMTS TYPE DELETE                               SEND TO SITE

REQUIRED BUILDS:                                  ACTION:

GMTS*2.7*49                                    Don't install, leave global

GMTS*2.7*56                                    Don't install, leave global

### Print Results of the Installation Process

Use the KIDS Install File Print option if you’d like to print out the results of the installation process.

Select Utilities Option: **Install** File Print

Select INSTALL NAME: **GMTS*2.7*58** Install Completed  2/26/02@09:06:39

=&gt; GMTS*2.7*49 TEST v5

DEVICE: HOME// ;;999  ANYWHERE

PACKAGE: GMTS*2.7*58     Dec 26, 2002 11:09 am                        PAGE 1

COMPLETED           ELAPSED

----------------------------------------------------------------------------

STATUS: Install Completed                 DATE LOADED: DEC 25, 2002@12:51:45

INSTALLED BY: MERRILL,DAVID

NATIONAL PACKAGE: HEALTH SUMMARY

INSTALL STARTED: DEC 26, 2002@09:06:33       09:06:39             0:00:06

ROUTINES:                                    09:06:34             0:00:01

PRE-INIT CHECK POINTS:

XPD PREINSTALL STARTED                       09:06:35             0:00:01

XPD PREINSTALL COMPLETED                     09:06:35

PRINT TEMPLATE                               09:06:35

OPTION                                       09:06:37             0:00:02

POST-INIT CHECK POINTS:

XPD POSTINSTALL STARTED                      09:06:38             0:00:01

XPD POSTINSTALL COMPLETED                    09:06:38

INSTALL QUESTION PROMPT                                               ANSWER

XPO1   Want KIDS to Rebuild Menu Trees Upon Completion of Install     YES

XPI1   Want KIDS to INHIBIT LOGONs during the install                 NO

XPZ1   Want to DISABLE Scheduled Options, Menu Options, and Protocols NO

MESSAGES:

Install Started for GMTS*2.7*58 :

Dec 26, 2002@09:06:33

Build Distribution Date: Mar 14, 2002

Installing Routines:

Dec 26, 2002@09:06:34

Installing PACKAGE COMPONENTS:

Installing PRINT TEMPLATE

Installing OPTION

Dec 26, 2002@09:06:37

Running Post-Install Routine: POST^GMTSP58

Updating Routine file...

Updating KIDS files...

GMTS*2.7*58 Installed.

Dec 26, 2002@09:06:39

Not a production UCI

NO Install Message sent

Call MENU rebuild

**Other Kernel Print Options**

Besides using the Kernel Installation &amp; Distribution (KIDS) options to get lists of routines, files, etc., you can also use other Kernel options to print online technical information.

### Routines

The namespace for the Health Summary package is GMTS. Use the Kernel option, List Routines [XUPRROU], to print a list of any or all of the Health summary routines. This option is found on the Routine Tools [XUPR-ROUTINE-TOOLS] menu on the Programmer Options [XUPROG] menu, which is a sub-menu of the Systems Manager Menu [EVE] option.

**Example:**

Select Systems Manager Menu Option: **programmer** Options

Select Programmer Options Option: **routine Tools**

Select Routine Tools Option: **list Routines**

Routine Print

Want to start each routine on a new page: No// **&lt;RET&gt;**

routine(s) ?   &gt; **GMTS***

The first line of each routine contains a brief description of the general function of the routine. Use the Kernel option, First Line Routine Print [XU FIRST LINE PRINT], to print a list of just the first line of each Health Summary subset routine.

**Example:**

Select Systems Manager Menu Option: **programmer** Options

Select Programmer Options Option: **routine Tools**

Select Routine Tools Option: **First Line Routine Print**

PRINTS FIRST LINES

routine(s) ?   &gt; **GMTS***

### Globals

The globals used in the Health Summary package are:

^GMT(142,

^GMT(142.1

^GMT(142.5,

^GMT(142.98,

^GMT(142.99,

Use the Kernel option, List Global [XUPRGL], to print a list of any of these globals. This option is found on the Programmer Options menu [XUPROG], which is a sub-menu of the Systems Manager Menu [EVE] option.

**Example:**

Select Systems Manager Menu Option: **programmer** Options

Select Programmer Options Option: **LIST Global**

Global ^GMT*

**Inquire To Option File**

The Kernel Inquire option [XUINQUIRE] provides the following information about a specified option(s).

- Option name.
- Menu text.
- Option description.
- Type of option.
- Lock (if any).

In addition, all items on the menu are listed for each menu option.

### 1 XINDEX

XINDEX is a routine that produces a report called the VA Cross-Referencer. This report is a technical and cross-reference listing of one routine or a group of routines. XINDEX provides a summary of errors and warnings for routines that do not comply with VA programming standards and conventions, a list of local and global variables and what routines they are referenced in, and a list of internal and external routine calls.

XINDEX is invoked from programmer mode: D ^XINDEX.

When selecting routines, select GMTS* and exclude the routines GMTSI* (the inits), GMTSON* and GMTSO0* (the onits).

## Data Dictionaries/ Files

The number-spaces for Health Summary files are 142-. Use the VA FileMan DATA DICTIONARY UTILITIES, option #8 ( DILIST, List File Attributes), to print a list of these files. Depending on the FileMan template used to print the list, this option will print out all or part of the data dictionary for the GMTS files.

**List File Attributes**

The FileMan List File Attributes option [DILIST] lets you generate documentation about files and file structure. If you choose the “Standard” format, you can see the following Data Dictionary information for a specified file(s).

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

START WITH WHAT FILE: **8925**

(1 entry)

GO TO WHAT FILE: 8925// 8926*

Select LISTING FORMAT: STANDARD// **[Enter]**

DEVICE: **PRINTER**

In addition, the following applicable data is supplied for each field in the file: field name, number, title, global location, description, help prompt, cross-reference(s), input transform, date last edited, and notes.

The “Global Map” format of this option generates an output that lists all cross-references for the file selected, global location of each field in the file, input templates, print templates, and sort templates.

### ?, ??, and ??? Online Help

**?** Enter one question mark to see helpful information about the components of the health summary type used in the health summary and the options available.

**??** Enter two question marks to see a list of available health summary components.

**???** Enter three question marks for detailed help, if available.


## Glossary

**Ad Hoc Summary** This is a temporary health summary that allows you to select health summary components, time and occurrence limits, and selection items for a particular patient.

**Components** Elements of data from DHCP packages that make up the health summary report (e.g., Demographics).

**DHCP** Decentralized Hospital Computer Program—previously the name for the VA program responsible for installing an integrated computer system in all DVA medical facilities. Now known as VISTA.

**Default** Prompts that have an answer followed by double slashes (//) are called defaults; this means a response has been pre-selected, based on the most likely response or the previous response to this prompt. For example, the prompt “Time Limit:” may have a default of 1 year for Lab Orders and would appear as: Time Limit: 1Y//. Defaults save you time by allowing you to just hit return rather than typing an answer.

**Device** A printer or a computer terminal screen. See the *DHCP Users Guide to Computing* for basic DHCP computer skills, including printing information.

**Hospital Location** For some PCE components, when this

**Displayed** flag is enabled, the Hospital Location abbreviation will be displayed.

**ICD Text Displayed** For some components, Diagnosis Text can be customized (e. g., long form, short form, code only, or no form of ICD Diagnosis).

**IB Encounter Form** The Integrated Billing Package (Encounter

**Utilities** Form Utilities) includes a Print Manager that allows sites to define reports that should print along with the encounter forms for a specific clinic or division and for specified appointments. One of the options, “Define Available Health Summary”, allows a Health Summary to be made available for use by the print manager. See the *IB Encounter Form Utilities User Manual* for further information.

**Lock** Restricts edit access for a given health summary type to the holders of any valid security key. For example, the GMTSMGR key is required to edit summary types that are locked by the GMTSMGR lock.

**Non-destructive** Health Summary components are non-destructive, meaning that the Health Summary package does not edit the data from the DHCP package where it extracts its information.

**Occurrence Limits** The number of past occurrences that will be reported on a health summary (e.g., the last five occurrences).

**Owner** The creator of a health summary type. Owners and holders of the GMTSMGR security key have sole access to modify their health summary type(s).

**Provider Narrative** For some components, when this flag

**Displayed** is enabled and a provider enters narrative text, the text will be displayed.

**Summary Order** The order in which components appear in a health summary, as defined by the creator of a Summary Type.

**Summary Type** The structure or template containing defined components and the unique characteristics with occurrence and time limits, and selection items. Used to print health summaries for patients.

**Time Limits** The time period of reference included on a health summary for a particular component (e.g., 2D, 1M, 1Y for two days, one month and one year).

**VISTA** The name for the VHA program responsible for installing an integrated computer system in all VHA medical facilities.


## Appendix A—Defining New Components

We encourage sites to submit E3Rs for new components (or enhancements to existing components) that they believe will be useful on a national basis. The Health Summary Expert Panel (EP) will evaluate these requests. If the EP approves the request, these new components will be provided as patches or in a future version of the Health Summary package, depending on the priority that is given to the request.

Sites have the option to create new components for Health Summary to provide for their site-specific needs. This may be an enhancement to one of the components that Health Summary provides, it can be a totally new one that accesses DHCP data that Health Summary currently doesn’t provide a component for, or it can be one to access non-DHCP supported (Class III software) packages.

**NOTE:** Please be aware that locally created components are not supported by National VISTA Service (NVS) or Systems Design and Development (SD&amp;D).

A Health Summary basket has been set up on SHOP, ALL where sites can put their locally developed component routines, in order to share this information with the rest of the DHCP community. We encourage you to take a look at what has already been done, as this may save you some time.

*To access SHOP,ALL from FORUM:*

1. Enter SHOP,ALL at your menu prompt and you’ll be “logged” on to SHOP,ALL
2. Enter SURROGATE NAME: **SHOP,ALL**
3. Select Mailman Option: **Read Mail**
4. Enter the Health Summary mail basket.

We would also like you to add any components you have created locally to SHOP,ALL .

**Format for Adding Components to SHOP,ALL**

If you have components you would like to share, please use the following instructions/format.

1. Start the subject of the message with:

HS Vx.x -- brief subject/component name, where x.x will be the version

2. Include a description, sample of the report, and the routines to produce the report. The routine should be under the name-space assigned to your station; e.g., Madison=ALW, Cincinnati=AFR. Send to:  REDACTED

3. The message will go to the IN Basket at SHOP,ALL. The SHOP,ALL administrators will read the IN basket daily and save the message to a basket called Health Summary.

**Hints for Developing local site components**

Before writing your own components, review some of the existing routines that have been written. Some good examples are the Patient Care Encounter, the Discharge Summary, or the Compensation and Pension components with the display routines in the Health Summary name space and the extract routines in the custodial package’s name-space. We suggest that when creating new components, you write two separate routines, one to extract the data and one to display the data. The display routine will call the extract routine and then display the data that was extracted.

Put any local routines you develop in your site’s routine name-space.

Local site components will be entered into the Health Summary Component (File #142.1) file with an internal file number beginning with your site number plus an additional 3 digits (e.g. At Salt Lake VAMC the first number would be 660001). This is to assure that nationally developed components are not overlaid by local site-developed components or vice versa. You will be prompted with a valid number when you enter a new component via the

Create/Modify Health Summary Components option on the Health Summary Maintenance Menu.

For the extract routine, we recommend that you set the data to the ^TMP("name",$J) global. The display routine will get the data from this global and display/print it. For the extract routine, you call it with the DFN (Patient Internal File Number) variable. Optionally, you could set it up for time and occurrence limits. GMTSEND (FileMan date to be used as the ending date for displaying data, GMTSBEG (FileMan date to be used as the beginning date for displaying data, and GMTSNDM (Maximum number of occurrences to display) are the variables to use to allow for time and occurrence limits. In your extract routine, make sure the date of the data is between the dates in the GMTSBEG and GMTSEND variables. Use the GMTSNDM variable to make sure you only get the maximum number of records that were entered for the occurrence limits.

Depending on how the cross-references are set up in the file you are extracting data from, you may want to use the reverse $ORDER M command or a cross-reference with an inverted FileMan date to get the most recent data first. When putting the data into the ^TMP global, you can invert the date (9999999-Date) as one of the subscripts. Or you can just include the date. When displaying the data, you will need to use the Reverse $ORDER M command to get the most recent data to display first, if you don’t use an inverted date subscript.

**NOTE:** Inverted FileMan dates mean that the date (e.g. 2950630) will  be subtracted from 9999999. This would give you 7049369. Inverted FileMan dates are used to order the data from most recent data to oldest data. With the Reverse $ORDER command, this convention won’t necessarily need to be followed in the future. Prior to the Reverse $ORDER M command, it was necessary to put the retrieved data in the ^TMP array with a subscript in Inverted FileMan Date/time in order that the user would see the most current data first in the Health Summary display.

Once you have extracted the data, you can print or display it. To allow for page breaks (and in the interactive display the capability to terminate or jump to another component), it is important that you issue the following commands before printing a line of data.

D CKP^GMTSUP Q:$D(GMTSQIT)

If this isn’t done before each line is written, the length of the document may exceed the length of the page or screen. You also will not get the component header to display before displaying the data. It is important that no lines are written, and the above commands are not issued if there is no data. For version 2.7 of Health Summary we implemented the capability to suppress component headers and “No Data Available” messages for Health Summary Types. In order to make this work, the CKP^GMTSUP routine was updated to set a flag that data was printed for a component. After the Health Summary driver processes each component for a Health Summary Type, the system checks to see if data was displayed for the component. If no data was displayed, the driver determines whether or not to display the component header and “No Data Available” messages.

**NOTE:** For any local site components that were written prior to version 2.7, if you want to be able to suppress component headers and “No Data Available” messages, you will need to evaluate them and remove calls to BREAK^GMTSUP. This command should not be executed within your routines and you should not display the message that there was no data available. You also want to be sure not to execute CKP^GMTSUP until you have data to display.

***Setting up a component to allow selection of specific items***

If you want to set up a component to allow selection of specific items, review one of the existing components that allows this capability, then follow these steps.

1. Add “GMTS” to the Application Group field for the file you want to select items from. You can do this through FileMan with the Edit File option under the Utility Functions option.
2. Add the pointed to file to the variable pointer Selection Item (field #4) sub-field in the multiple Structure (Field #1) field in the Health Summary Type (file #142) file. Do this through FileMan with the Modify File Attributes option.
3. When entering a new component to the Health Summary Component (file #142.1), be sure to enter the File to the Selection Item field. This can be done through the Create/Modify Health Summary Components option on the Health Summary Maintenance Menu.
4. In your application code, access the GMTSEG variable to determine the Selection Items for the file. The format of this array is GMTSEG(GMTSEGN,file number,Selection Item internal file number). GMTSEGN is the internal file number for the component. You can $ORDER on the third subscript of the array and get the Selection Item’s internal file number. In your extract routine you will then limit the extract to only retrieve records for the specified Selection Items.

**NOTE:** Typically, users at sites should not modify files. However, in order to include new components with selection items, it is necessary to modify a file’s structure. Therefore, we recommend extreme caution while following the procedures above.

**Create/Modify Health Summary Components**

The following sample dialogue can assist you in creating your own local health summary components.

**NOTE:** When selecting components from the Ad Hoc Health Summary menu, entering “ALL” allows all components to be selected. If the first three characters of a Header Name for a component are designated as “All”, however, then only the defined component will be selected. Avoid conflicts and loss of functionality by not using “all” at the front of new header names.

Select Health Summary Maintenance Menu Option: **2** Create/Modify Health

Summary Components

Select COMPONENT: CHEM 7

Are you adding 'CHEM 7' as a new HEALTH SUMMARY COMPONENT? Y  (Yes)

HEALTH SUMMARY COMPONENT NUMBER: 5000001//

Do you wish to duplicate an existing COMPONENT? YES//

CD    Advance Directive   CY    Cytopathology       RXNV  Non VA Meds

BADR  Brief Adv React/All EM    Electron Microscopy ONC   Oncology

ADR   Adv React/Allerg    MIC   Microbiology        ORC   Current Orders

BNC   BRAND NEW COMPONENT BMIC  Brief Microbiology  ED    Education

CPB   Clin Proc   Brief   LO    Lab Orders          EDL   Education Latest

CMB   Reminder Brief      BLO   Brief Lab Orders    EXAM  Exams Latest

CR    Reminders Due       SP    Surgical Pathology  HF    Health Factors

CF    Reminders Findings  SLT   Lab Tests Selected  SHF   Health Factor Select

CLD   Reminders Last Done MAGI  MAG Imaging         IM    Immunizations

CM    Reminder MaintenanceADC   Admission/Discharge OD    Outpatient Diagnosis

CRS   Reminders Summary   ADT   ADT History         OE    Outpatient Encounter

CW    Clinical Warnings   EADT  ADT History ExpandedST    Skin Tests

CP    Comp. &amp; Pen. Exams  CVF   Fut Clinic Visits   RXIV  IV Pharmacy

CNB   Brief Consults      CVP   Past Clinic Visits  RXOP  Outpatient Pharmacy

CN    Crisis Notes        CON   Patient Contacts    RXUD  Unit Dose Pharmacy

DI    Dietetics           DEM   Demographics        PLA   Active Problems

DCS   Discharge Summary   BDEM  Brief Demographics  PLL   All Problems

BDS   Brief Disch Summary DS    Disabilities        PLI   Inactive Problems

ENV   Full Environment    DD    Discharge Diagnosis       PROBLEM LSIT

FR    Fred                DC    Discharges          PN    Progress Notes

AVC   GEC                 MHFV  MH Clinic Fut VisitsBPN   Brief Progress Notes

Press RETURN to continue or '^' to exit:

GECC  Referral Count      PRC   ICD Procedures      SPN   Selected Prog Notes

GECH  Referral Categories OPC   ICD Surgeries

GAF   Global Assess Funct TR    Transfers           SCD   Spinal Cord Dysfunct

HS    HS Environment      TS    Treating Specialty  NSR   NON OR Procedures

II    Imaging Impression  MEDA  Med Abnormal        SRO   Surgery Only Reports

SII   Sel Image ImpressionMEDB  Med Brief Report    SR    Surgery Rpt (OR/NON)

IP    Imaging Profile     MEDC  Med Full Captioned  BSR   Brief Surgery Rpts

IS    Imaging Status      MEDF  Med Full Report     SNSR  Selected NON OR Proc

MEDS  Med (1 line) SummaryTC    TRAINING COMPONENT

MHPE  MH Physical Exam    URIN  URINALYSIS

BA    Blood Availability  MHRF  MH Suicide PRF Hx   VS    Vital Signs

BT    Blood Transfusions  MHTC  MH Treatment Coor   VSD   Detailed Vitals

CH    Chem &amp; Hematology   MHAL  MHA Admin List      VSO   Vital Signs Outpat.

SCLU  Lab Cum Selected    MHAS  MHA Score           SVS   Vital Signs Selected

SCL1  Lab Cum Selected 1  MHVD  Detail Display      SVSO  Vital Select Outpat.

SCL2  Lab Cum Selected 2  MHVS  Summary Display

SCL3  Lab Cum Selected 3  MRT2  Medication Worksheet

SCL4  Lab Cum Selected 4  NOK   Next of Kin

Enter COMPONENT to Duplicate: **SCLU** Lab Cum Selected

NAME: CHEM 7// **&lt;RET&gt;**

ABBREVIATION: **CH7**

DESCRIPTION:. . .

1&gt;This component contains information extracted from the Lab package. Not

2&gt;only do time and maximum occurrence limits apply to this component, but

3&gt;the user is allowed to select any number of atomic Lab tests. Data

4&gt;presented include:  collection date/time, specimen, test names with

5&gt;results and reference flags in columnar (horizontal) format. Comments will

6&gt;also be conditionally displayed, depending on the value of the DISPLAY

7&gt;COMMENTS ON LABS Health Summary Site Parameter. When comments are

8&gt;displayed, a lower case letter will be displayed to the left of the date

9&gt;for entries with comments. Comments will be displayed after all the

10&gt;results are displayed with comments being linked by the lower case letter.

11&gt;Up to 26 comments can be included.

EDIT Option: **&lt;RET&gt;**

PRINT ROUTINE: MAIN;GMTSLRSC// **??**

This is the entry point and routine to be called when the component is

run for a given health summary type.  Enter the line label, followed by

a semi-colon, followed by the routine name (e.g., MAIN;GMTSLRC).

PRINT ROUTINE: MAIN;GMTSLRSC// **&lt;RET&gt;**

TIME LIMITS APPLICABLE: yes// **??**

This field is set up by the programmer to indicate whether the routine to

print this component will allow a time range to be applied to the data

to be displayed in the Health Summary.

Choose from:

Y        yes

TIME LIMITS APPLICABLE: yes// **&lt;RET&gt;**

MAXIMUM OCCURRENCES APPLICABLE: yes// **??**

This field is used by the programmer to indicate whether the routine

which prints this component is set up to handle maximum occurrence limits

on the Health Summary.

Choose from:

Y        yes

MAXIMUM OCCURRENCES APPLICABLE: yes// **&lt;RET&gt;**

HOSPITAL LOCATION APPLICABLE: **??**

This field is used by the programmer to indicate whether the routine

which prints this component is set up to handle the display of the

hospital location abbreviation on the Health Summary.

Choose from:

Y        yes

HOSPITAL LOCATION APPLICABLE: **&lt;RET&gt;**

ICD TEXT APPLICABLE: **??**

This field is used by the programmer to indicate whether the routine

which prints this component is set up to handle the display of

standardized ICD text on the Health Summary.

Choose from:

Y        yes

ICD TEXT APPLICABLE: **&lt;RET&gt;**

PROVIDER NARRATIVE APPLICABLE: **??**

This field is used by the programmer to indicate whether the routine

which prints this component is set up to handle the display of the

provider narrative on the Health Summary.

Choose from:

Y        yes

PROVIDER NARRATIVE APPLICABLE: **&lt;RET&gt;**

LOCK: **??**

To be used for components such as psychology test results

Restricts viewing access under Print Health Summary Menu

LOCK: **&lt;RET&gt;**

DEFAULT HEADER NAME: **??**

The DEFAULT HEADER NAME will appear in menus and component headers in

preference to the COMPONENT NAME, but NOT in preference to the local

HEADER NAME, if it is defined for that component within a given Health

Summary Type.  If defined the local HEADER NAME will have precedence

within a given Health Summary Type.

DEFAULT HEADER NAME: **Chem 7**

Select SELECTION FILE: **??**

Choose from:

LABORATORY TEST

Enter the names or numbers of the files from which selection items

(e.g., lab tests (file 60), radiology procedures (file 71), or vital

signs (file 120.51)) may be chosen for this component.

Choose from:

60              LABORATORY TEST

71              RADIOLOGY PROCEDURES

120.51          VITAL TYPE

811.9           PCE REMINDER/MAINTENANCE ITEM

9001017         HEALTH SUMMARY MEAS PANEL

9999999.64      HEALTH FACTORS

Select SELECTION FILE: **60** LABORATORY TEST

...OK? Yes// **&lt;RET&gt;** (Yes)

SELECTION FILE: LABORATORY TEST// **&lt;RET&gt;**

SELECTION COUNT LIMIT: **??**

Enter the MAXIMUM number of selection items which may be selected for

any single appearance of this component in a given health summary type.

That is, a value of 7 will allow the user to select as many as seven

items, etc.

SELECTION COUNT LIMIT: **7**

Select SELECTION FILE: **&lt;RET&gt;**

ADD new Component to the AD HOC Health Summary? NO// **y** YES

&gt;&gt;&gt; EDITING the GMTS HS ADHOC OPTION Health Summary Type

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: **??**

This field allows health summary types to be set up to suppress printing

of components that contain no data when health summaries are printed from

a device. When health summary types are displayed on the screen,

components that contain no data will still be displayed with a "No data

available" message. This is done to eliminate any confusion that may

occur when jumping between components.

Choose from:

Y        yes

N        no

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: **y** yes

Do you wish to review the Summary Type structure before continuing? NO// **&lt;RET&gt;**

Select COMPONENT: CHEM 7// **&lt;RET&gt;** CH7

SUMMARY ORDER: 395// **395**

OCCURRENCE LIMIT: **5**

TIME LIMIT: **21d**

HOSPITAL LOCATION DISPLAYED: **y** yes

ICD TEXT DISPLAYED: **??**

Indicate whether the long form, short form, code only, text only, or no

form of ICD diagnosis text should appear in applicable components.

Choose from:

L        long text

S        short text

C        code only

T        text only

N        none

ICD TEXT DISPLAYED: **c** code only

PROVIDER NARRATIVE DISPLAYED: **y** yes

HEADER NAME: Chem 7// **&lt;RET&gt;**

No selection items chosen.

Select new items one at a time in the sequence you want them displayed.

You may select up to 7 items.

Select SELECTION ITEM: **CHEM 7**

Searching for a LABORATORY TEST  CHEM 7

...OK? Yes// **&lt;RET&gt;** (Yes)

Select the tests which you wish to include, in the

sequence in which you wish them to appear.

-- CHEM 7 --

1    CREATININE                         5    CHLORIDE

2    UREA NITROGEN                      6    CO2

3    SODIUM                             7    GLUCOSE

4    POTASSIUM                          8    ANION GAP

Select 1 - 7 LAB TEST(s): 1-7// **1-5,8** CREATININE   UREA NITROGEN   SODIUM

POTASSIUM   CHLORIDE   ANION GAP

Select SELECTION ITEM:

Please hold on while I resequence the summary order.............................

..................................................

&gt;&gt;&gt; Returning to Create/Modify Health Summary Component Option.

Select COMPONENT: **&lt;RET&gt;**

***Next, we’ll illustrate the case where a Nuclear Medicine component, created on site, is to be added to the component file and Ad Hoc Summary Type.***

Select Health Summary Maintenance Menu Option: **2** Create/Modify Health Summary Components

Create/Modify Health Summary Components

Select COMPONENT: **NUCLEAR MEDICINE**

Are you adding 'NUCLEAR MEDICINE' as

a new HEALTH SUMMARY COMPONENT? **Y** (Yes)

HEALTH SUMMARY COMPONENT NUMBER: 5000002// **&lt;RET&gt;**

Do you wish to duplicate an existing COMPONENT? YES// **NO**

NAME: NUCLEAR MEDICINE// **&lt;RET&gt;**

PRINT ROUTINE: **??**

This is the entry point and routine to be called when the component is

run for a given health summary type.  Enter the line label, followed by

a semi-colon, followed by the routine name (e.g., MAIN;GMTSLRC).

PRINT ROUTINE: **NUC;A5AMED**

ABBREVIATION: **NUC**

DESCRIPTION:

1&gt; **This component, created at &lt;site name&gt;, prints nuclear medicine**

2&gt; **report data, including: Study date time, Radiologist, Report Status,**

3&gt; **Impression, and Report text.**

4&gt; **&lt;RET&gt;**

EDIT Option: **&lt;RET&gt;**

TIME LIMITS APPLICABLE: **y** yes

MAXIMUM OCCURRENCES APPLICABLE: **y** yes

HOSPITAL LOCATION APPLICABLE: **&lt;RET&gt;**

ICD TEXT APPLICABLE: **&lt;RET&gt;**

PROVIDER NARRATIVE APPLICABLE: **&lt;RET&gt;**

LOCK: **&lt;RET&gt;**

DEFAULT HEADER NAME: **Nuclear Medicine**

Select SELECTION FILE: **&lt;RET&gt;**

ADD new Component to the AD HOC Health Summary? NO// **y** YES

&gt;&gt;&gt; EDITING the GMTS HS ADHOC OPTION Health Summary Type

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes// **&lt;RET&gt;**

Do you wish to review the Summary Type structure before continuing? NO// **&lt;RET&gt;**

Select COMPONENT: NUCLEAR MEDICINE// **&lt;RET&gt;** NUC

SUMMARY ORDER: 400// **400**

OCCURRENCE LIMIT: **5**

TIME LIMIT: **21d**

HOSPITAL LOCATION DISPLAYED: **y** yes

ICD TEXT DISPLAYED: **??**

Indicate whether the long form, short form, code only, text only, or no

form of ICD diagnosis text should appear in applicable components.

Choose from:

L        long text

S        short text

C        code only

T        text only

N        none

ICD TEXT DISPLAYED: **c** code only

PROVIDER NARRATIVE DISPLAYED: **y** yes

HEADER NAME: Nuclear Medicine// **&lt;RET&gt;**

Please hold on while I resequence the summary order..........................

...................................................

&gt;&gt;&gt; Returning to Create/Modify Health Summary Component Option.

Select COMPONENT: **&lt;RET&gt;**

## Appendix BHealth Summary Security

Health summaries produced by this package are highly confidential and should be treated with the same security precautions as a patient’s medical record.

### Menu Access

The Health Summary Overall Menu [GMTS MANAGER] contains four menus.

1. GMTS USER

2.	GMTS ENHANCED USER

3.	GMTS COORDINATOR

4.	GMTS IRM/ADPAC MAINT MENU

Assign these menus as follows. (See the *Health Summary User Manual* for complete user descriptions of menus and options).

1.	Give the Health Summary Menu [GMTS USER] menu to users who only need to print or display health summaries.

2.	Give the Health Summary Enhanced Menu [GMTS ENHANCED USER] menu to users who need to create, modify, or delete their *own* health summary types, in addition to printing health summaries.

3.	Give the Health Summary Coordinator’s Menu [GMTS COORDINATOR] menu to users who need to print or display health summaries, and who will also need to create, modify, or delete health summary types, and set up nightly batch printing at specified locations.

1. Give the Health Summary Maintenance Menu [GMTS IRM/ADPAC MAINT MENU] to IRM staff or the Clinical Coordinator for any implementation and maintenance issues in Health Summary. This menu contains options to disable/enable health summary components for selection/display, create/modify new health summary components, edit and rebuild the Ad Hoc Health Summary Type, re-sequence the components in a health summary type, create/modify a health summary type, delete a health summary type, and edit health summary site parameters.  With the release of GMTS*2.7*94 patch, it also contains a new GMTS PS MED RECON CONFIG CHECK option which will check the HEALTH SUMMARY TYPE ‘Essential Med List for Review’ to make sure it holds certain HEALTH SUMMARY COMPONENTs for which it was created in the first place.

### Security

Security is established via a combination of the GMTSMGR and GMTS VIEW ONLY security keys and the OWNER and LOCK fields in File 142 (Health Summary Type file).

GMTSMGR Security Key

The GMTSMGR security key allows holders to override the LOCK and OWNER access restrictions for editing health summary types. The IRM Chief and Health Summary Coordinators are likely holders of this key.

This security key allows the holder to edit general usage health summary types which are locked with the GMTSMGR key. It also provides master edit access to all other health summary types.

GMTS VIEW ONLY Security Key

The GMTS VIEW ONLY key allows holders to view a health summary on the CRT. Holders may use all of the familiar Health Summary options but will not be prompted for a device for printing paper copies of the health summary.

### Health Summary Type File

#### Owner

Owners of health summary types have edit access to health summary types they have created. The owner is designated when a health summary type is created. Usually the creator of a health summary type is automatically designated as its owner. However, if creators of heath summary types hold the GMTSMGR key, they may designate another person as the owner. If you are assigned the GMTSMGR key, you are *not* automatically designated as the owner. You may, however, enter your name as the “owner.”

#### Lock

This field can be used to specify a security key and is designated when the health summary type is created. This lock gives edit access for that health summary type to anyone who holds the matching security key. For example, someone creating a Pathology Health Summary Type may want to enter LRSUPER as the lock, thereby giving edit access to any holder of the LRSUPER security key. The four health summary types exported with the Health Summary package have the GMTSMGR lock.

A lock does not restrict an owner the lock gives permission. If a health summary type is locked, the owner of the health summary type is not required to have the key to access it; however, all other users must have the key.

### Health Summary Object File

#### Creator

Creators of health summary objects have edit access to health summary objects they have created. The creator is designated when a health summary object is created.

### Health Summary Component File

#### Lock

You may restrict any component from view by entering the name of a valid security key in the LOCK field for a given component. For example, if your site decides that only holders of the LRSPUSER key should be allowed to view the Surgical Pathology Health Summary component, then entering the name of that security key in the LOCK field of that component’s record will enforce that policy.

### VA FileMan File Protection

The Health Summary package files are exported with the following file protection provided by VA FileMan.

| **File Number**   | **Name**                        | **DD**   | **RD**   | **WR**   | **DEL**   | **LAYGO**   | **AUDIT**   |
|-------------------|---------------------------------|----------|----------|----------|-----------|-------------|-------------|
| File 142          | Health Summary Type             | @        |          |          |           | @           | @           |
| File 142.1        | Health Summary Components       | @        |          | @        | @         | @           | @           |
| File 142.5        | Health Summary Objects          | @        | @        | @        | @         | @           | @           |
| File 142.98       | Health Summary User Preferences | @        | @        | @        | @         | @           | @           |
| File 142.99       | Health Summary Parameters       | @        | @        | @        | @         | @           | @           |


## Appendix C: CPRS Program Operations and Maintenance Responsible, Accountable, Consulted and Informed (RACI)

| **Name**                                           | **Role**                       | **Gov or non-Gov?**   | **FTE (man-hours/yr.)**          | **Org**                                                      | **Contact Info**                                                            |
|----------------------------------------------------|--------------------------------|-----------------------|----------------------------------|--------------------------------------------------------------|-----------------------------------------------------------------------------|
| National Service Desk Tier 1                       | NSD Tier 1 Support             | Gov                   | No Change to Current Support     | NSD                                                          | Phone: 1-855-NSD-HELP                                                       |
| EPMO – clinical product support team – CLIN 2      | National OI&T – tier 2 support | Gov                   | No additional man hours required | National Service Desk (NSD) 888-596-4357 will route to team. | EPMO  – clinical product support team – CLIN 2                              |
| EPMO - HPS Clinical Task Order / VistA Maintenance | Tier 3                         | Gov                   | No additional man hours required | PD                                                           | Will be routed via Tickets from EMPO Clinic product Support CLIN 2          |
| CPRS Development team                              | Tier 3                         | Gov                   | No additional man hours required | PD                                                           | Kenny Condie – GUI only Tickets routed from Clin 2, Vista Maint post review |


## Appendix D: Historical Documentation Shift from GMTS*2.7*133 (Do Not Update)

### New Features in Health Summary

Some of the more recent patches are described below. For complete descriptions of all of the changes in Health Summary since the release of version 2.7 in 1994, please refer to the patches (described briefly on the following pages and in more detail in the Patch module on Forum).

Patch GMTS*2.7*125 Updates for Health Summary Components

GMTS*2.7*125 will be installed with patches PSN*4*567 and PSS*1*234, to release two new national Health Summary components that can be used to create objects or in Ad-Hoc reporting.

The components will allow selecting Outpatient prescriptions by drug class (VA classification) or by Pharmacy Orderable Item name. The component names are RXDC for drug classes and RXOI for Orderable Items.

Patch GMTS*2.7*94 Updates for the Essential Med List for Review

GMTS*2.7*94 will be installed with PSO*7*314  to correct issues reported with the Tool #1: Medication Reconciliation.  The Health Summary patch GMTS*2.7*94 will create a national entry in the HEALTH SUMMARY COMPONENT file (#142.1) for Tool #1: Med. Reconciliation (the abbreviation is MRT1).

Furthermore, a replica of the Tool #1 Medication Reconciliation called Medication Reconciliation No Glossary Tool #1 (the abbreviation is MRR1) will be created. The only difference between the two components is whether the Health Summary has a glossary. In the Essential Med List for Review Health Summary type, the site can use either the MRT1 component if they want the glossary at the end of the Health Summary, or if the site uses the MRR1 component, the same Health Summary will be displayed without the glossary at the end of the report.

Another feature recently added was to include all Dispense Drug data, including BCMA Last Action, into the report for Inpatient Medication data which incorporates Dosage information as well.

The GMTS*2.7*94 patch changes include the following:

1. Usage of data from other VA pharmacies via Remote Data Interoperability

(RDI) updated to include prescriptions where the status is “HOLD”.

1. The Essential Med List for Review was upated to retrieve all necessary BCMA actions, particularly for large volume IVs.

1. Corrected the service for Clinic Medications that used to show the service as “INPT”. The service for Clinic Medications now reads “CLIN”.

1. Ensured that the most recent order information was being correctly gathered. The change involved looking at the correct field in the prescription information and no longer infer that the latest expiration date implied the latest prescription.

1. The tool was modified to display multiple line provider comments in a more readable fashion.

1. The program was updated to assume that DoD prescriptions with an issue date more than 1 year in the past must be, by definition, now expired or discontinued and will no longer be considered “ACTIVE” even though that is precisely what is returned by the CHDR data.

1. The section of the report that showed “Other medications previously dispensed in the last year” was misleading. For example, prescriptions with no refills that were over 120 days old would not display at all. In some cases, this led to the belief that the Sig that was displaying was incorrect. The section in question has been removed from the report and the medications needed for the report were incorporated into the main body of the report.

1. The code was modified to recognize the On Call property flag for IV types of admixtures.

1. The following changes were also made:
    - Introductory text changed to describe what the report contains, what is does not contain, and that it specify what remote data is shown
    - Remote data warnings that give some information about why remote data may not display
    - Changes in the status names (Hold changed to On Hold, Suspended changed to Active/Suspended, etc)
    - Rx# added to active outpatient prescriptions
    - QTY added to days supply for outpatient
    - Status added to inpatient entries
    - Additive strength added to Intravenous Piggyback (IVPB) orders
    - Added pending orders to inpatient and outpatient
    - INP changed to INPT and OPT changed to OUTPT
    - Added additive strength and bags/day to inpatient IV Adm
    - Added status, admin rate, dose and freq to IVPBs, including number of bags per order
    - Added volume and rate of infusion to IV Adms
    - Supplies now separated from medications list
**Example of the Essential Med List for Review with the medication reconciliation information, allergy information, and the glossary of terms**
08/16/2018 11:01
*********  CONFIDENTIAL Essential Med List for Review SUMMARY   pg. 1 **********
PLJH,YDJEXALT    000-00-6671                                    DOB: 00/08/1957
---------------------------- MRT5 - Allergies/ADRs ----------------------------
FACILITY                                ALLERGY/ADR
--------                                -----------
*** WARNING: Remote Data from HDR not available ***
-------------------------- MRT1 - Med Reconciliation --------------------------
INCLUDED IN THIS LIST:  Alphabetical list of active outpatient
prescriptions dispensed from this VA (local) and dispensed from another
VA or DoD facility (remote) as well as inpatient orders (local pending and
active), local clinic medications, locally documented non-VA medications,
and local prescriptions that have expired or been discontinued in the past
90 days.
Non-VA Meds Last Documented On: ** Data not found **
************************************************************************
***NOTE*** The display of VA prescriptions dispensed from another VA or
DoD facility (remote) is limited to active outpatient prescription entries
matched to National Drug File at the originating site and may not include
some items such as investigational drugs, compounds, etc.
NOT INCLUDED IN THIS LIST: Medications self-entered by the patient into
personal health records (i.e. My HealtheVet) are NOT included in this
list. Non-VA medications documented outside this VA, remote inpatient
orders (regardless of status) and remote clinic medications are NOT
included in this list. The patient and provider must always discuss
medications the patient is taking, regardless of where the medication was
dispensed or obtained.
------------------------------------------------------------------------
OUTPT AMITRIPTYLINE HCL 10MG TAB (Status = Active)
TAKE TWO TABLETS BY MOUTH AT BEDTIME *MAY CAUSE DROWSINESS-AVOID
ALCOHOL*
Rx# 1002453 Last Released:              Qty/Days Supply: 60/30
Rx Expiration Date: 8/15/19             Refills Remaining: 11
OUTPT CEPHALEXIN 250MG CAP (Status = Active/Suspended)
TAKE SIX CAPSULES MOUTH BEFORE MEALS AND AT BEDTIME ** TAKE ON AN
EMPTY STOMACH **
Rx# 1002437 Last Released:              Qty/Days Supply: 720/30
Rx Expiration Date: 8/25/18             Refills Remaining: 0
OUTPT DIAZEPAM 5MG TAB (Status = Pending)
TAKE ONE-HALF TABLET BY MOUTH TWICE A DAY *MAY CAUSE
DROWSINESS-AVOID ALCOHOL*
Login Date: 8/15/18                     Qty/Days Supply: 30/30
Refills Ordered: 0
OUTPT DIGOXIN TAB (Status = Pending)
TAKE 0.25MG BY MOUTH DAILY
Login Date: 1/3/18                      Qty/Days Supply: 30/30
Refills Ordered: 3
OUTPT DIPHENHYDRAMINE HCL 50MG CAP (Status = Pending)
TAKE 1 CAPSULE subcutaneous EVERY EVENING *MAY CAUSE
DROWSINESS-AVOID ALCOHOL*
Login Date: 4/26/18                     Qty/Days Supply: 30/30
Refills Ordered: 0
OUTPT FENTANYL 25UG/H PATCH (Status = Active)
APPLY 1 PATCH AS DIRECTED EVERY THIRD DAY *MAY CAUSE
DROWSINESS-AVOID ALCOHOL*
Rx# 1002452 Last Released:              Qty/Days Supply: 10/30
Rx Expiration Date: 9/13/18             Refills Remaining: 0
OUTPT GABAPENTIN 300MG CAP (Status = Pending)
TAKE 2 CAPSULES subcutaneous TWICE A DAY
Login Date: 4/26/18                     Qty/Days Supply: 120/30
Refills Ordered: 0
OUTPT GLIPIZIDE 10MG TAB (Status = Pending)
TAKE ONE TABLET BY MOUTH TWICE A DAY
Login Date: 1/3/18                      Qty/Days Supply: 60/30
Refills Ordered: 0
OUTPT MONTELUKAST NA 10MG TAB (Status = Pending)
TAKE ONE TABLET BY MOUTH FOUR TIMES A DAY
Login Date: 1/3/18                      Qty/Days Supply: 120/30
Refills Ordered: 0
OUTPT SIMVASTATIN 20MG TAB (Status = Pending)
TAKE ONE TABLET subcutaneous DAILY AT BEDTIME
Login Date: 4/26/18                     Qty/Days Supply: 30/30
Refills Ordered: 0
------------------------------------------------------------------------
SUPPLIES
------------------------------------------------------------------------
==========PHARMACY TERMS AND POSSIBLE PATIENT ACTIONS===========
INPT = VA inpatient order
IV = VA intravenous medication
OUTPT = VA outpatient prescription
PHARMACY                                       POSSIBLE PATIENT
TERMS        EXPLANATION                       ACTIONS
--------     -------------------------------   -----------------
ACTIVE       A prescription that can be        If you have refills,
filled at the local VA pharmacy.  you may request a
refill of this
prescription from
your VA pharmacy.
CLINIC       A medication you received during  If you have questions
a visit to a VA clinic or         about this medication
emergency department.             contact your VA
healthcare team.
DISCONTINUED A prescription your provider has  Contact your VA
stopped. It is no longer          healthcare team if you
available to be sent to you or    need more of this
picked up at the VA pharmacy      medication.
window.
EXPIRED      A prescription which is too old   Contact your VA
to fill. This does not refer to   healthcare team if you
the expiration date of the        need more of this
medication in the container.      medication.
NON-VA       A medication that came from       If this medication is
someplace other than a VA         medication information
pharmacy. This may be a           is incorrect or out of
prescription from either the VA   date, please tell your
other providers that was filled   VA healthcare team.
outside the VA. Or, it may be an
over-the-counter (OTC), herbal,
dietary supplement or sample
medication.
ON HOLD      An active prescription that will  Contact your VA
not be filled until pharmacy      pharmacy when you need
resolves the issue.               more of this
medication.
PENDING      This prescription order has been  If you have been
sent to the pharmacy for review   instructed to start the
and is not ready yet.             this medication now,
contact your VA
pharmacy.
SUSPENDED    An active prescription that is    Contact your VA
not scheduled to be filled yet.   pharmacy if you need
You should receive it before you  this medication
run out.                          now.
==================================================================
*** END *  CONFIDENTIAL Essential Med List for Review SUMMARY   pg. 1 *********
<!-- image -->
Example of the Essential Med List for Review showing Rx# for existing and renewed medications
**Example of the Essential Med List for Review showing an active/suspended medication and more information for IVPB for both Clinic and Inpatient medications. The second item that is highlighted is a medication with a long SIG.**
<!-- image -->
**Example of the Essential Med List for Review showing several medications from different sources, such as Inpatient (INPT), Non-VA, Oupatient (OUTPT), and Clinic (CLIN). The report shows medication statuses of Pending and Active. The report now provides more information for Non-VA meds.**
<!-- image -->
**Example of the Essential Med List for Review showing a remote medication on hold**
<!-- image -->
**Example of the Essential Med List for Review showing a new inpatient and outpatient medication status abbreviations and how there is additional information for IV Infusions**
<!-- image -->
Patch GMTS*2.7*120 – HEALTH SUMMARY UPDATE FOR Medication Reconciliation Tool #2 (MRT2)
Currently, on the MRT2 non-VA medications do not display in the same manner as VA-prescribed medications. Patch GMTS*2.7*120 removes the inconsistencies in the display on the patient-facing report generated from the Health Summary data and given to the patient when admitted, discharged, or transferred. Per the Joint Commission's NPSG.03.06.01, a medication summary must be given to a patient upon each admission, discharge or transfer. The document used currently does not display non-VA medication information as thoroughly as it does VA medications. Even when all information is available, the MRT2 report does not present the Non-VA meds consistently. In fact, there is no 'worksheet space' available for the non-VA medications.
Note that non-VA medication orders are not required to have all the same fields as a VA prescribed medication.
An example of a complete patient-facing report using health summary information is as follows:
*********** CONFIDENTIAL Medication Worksheet SUMMARY pg. 1 ***********
BCMA,FIFTEEN-PATIENT   666-33-0015                      DOB: 04/07/1935
3 NORTH GU
---------------- MWS - Medication Worksheet (Tool #2) -----------------
Date: Jul 24, 2017        PATIENT MEDICATION INFORMATION        Page: 1
PRINTED BY THE VA MEDICAL CENTER AT: CAMP MASTER
FOR PRESCRIPTION REFILLS CALL (518) 472-4307
Name: BCMA,FIFTEEN-PATIENT     PHARMACY - ALBANY DIVISION
|---------------------------------------------------------------------|
|           |MORNING| NOON    |EVENING|BEDTIME|      COMMENTS         |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|                                                                     |
|**PENDING**  ACARBOSE  25MG  TAB                                     |
|     TAKE ONE TABLET BY MOUTH 3XW                                    |
|     Quantity: 5 Refills: 0                                          |
|---------------------------------------------------------------------|
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|                                                                     |
|**PENDING**  ACETAMINOPHEN 325MG                                     |
|     TAKE ONE TABLET BY MOUTH EVERY 4 HOURS AS NEEDED                |
|     Quantity: 180 Refills: 0                                        |
|---------------------------------------------------------------------|
| UNITS PER DOSE: |       |       |       |       |                   |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
|                                                                     |
|**NON-VA** ACARBOSE 25MG TAB                                         |
|     TAKE ONE TABLET BY MOUTH 3ID Do not take medication when        |
|     consuming alcohol. Take with a full glass of water only. Take on|
|     a full stomach. Do not mix with aspirin. Contact your provider  |
|     if you experience dizziness, excessive thirst, or hunger.       |
|---------------------------------------------------------------------|
| UNITS PER DOSE: |       |       |       |       |                   |
|---------------------------------------------------------------------|
Any medication items listed as "pending" are those that have just been written by your provider(s). These medication orders will be reviewed by your pharmacist, prior to the prescription(s) being dispensed. When you receive your new prescription(s), by mail or from the pharmacy window,be sure to follow the instructions on the prescription label. If you have any question about your medication, please call your provider or your pharmacist.
Any medication items listed as "NON-VA" are Medications you do not get from a VA pharmacy that your provider recorded in your medical record. This includes medication prescribed by VA or non-VA providers, over the counter medications, herbals, samples or other medications you take.
The screenshot below shows an example of a new and improved ‘NON-VA’ medication. It now has any entered comments listed with the medication.
<!-- image -->
Patch GMTS*2.7*111 – HEALTH SUMMARY UPDATE FOR ICD-10 PTF PROJECT
Patch GMTS*2.7*111 updates the following Health Summary Components (#142.1) to include an expanded number of diagnosis codes (1 primary and up to 24 secondary diagnoses), operation/surgery codes (up to 25), and procedure codes (up to 25) that may be present in the Patient Treatment File (PTF):
    - MAS ADMISSIONS/DISCHARGES
    - MAS ADT HISTORY EXPANDED
    - MAS DISCHARGE DIAGNOSIS
    - MAS PROCEDURES ICD CODES
    - MAS SURGERIES ICD CODESAny of the following **locally created** items will also be affected by the newly updated display capability included in this patch **if** those items leverage any of the affected components to generate output:
    - Health Summary Types
    - Health Summary Objects
    - TIU/Health Summary Objects
    - OE/RR Reports
Objects may be of particular interest as the newly expanded display would be more noticeable when an object is embedded in areas such as boilerplate text, note templates, and reminder dialog templates.
Patch GMTS*2.7*111 also updates the following reports that utilize one or more of the aforementioned Health Summary Components and will therefore now display the expanded data fields as appropriate:
    - HEALTH SUMMARY (#142)
        - REMOTE DEMO/VISITS/PCE (1Y)
        - REMOTE DEMO/VISITS/PCE (3M)
        - REMOTE DIS SUM/SURG/PROD (12Y)
    - OE/RR REPORT (#101.24)
        - ORRPW ADT ADM DC
        - ORRPW ADT DC DIAG
        - ORRPW ADT EXP
        - ORRPW ADT ICD PROC
        - ORRPW ADT ICD SURG
        - ORRPW DOD ADT EXP
GMTS*2.7*29 – REMOTE DATA VIEWS
GMTS*2.7*48 – REMOTE ONCOLOGY VIEW
Health Summary patches 29 and 48 export components for using Remote Data Views. With all the proper patches installed, you may view remote patient data through CPRS. Before you can do this, you must have Master Patient Index/Patient Demographics (MPI/PD) and several other patches installed. Once these are in place and the proper parameters have been set, you can access remote data from other VA facilities.
Currently, remote data views are limited to predefined, nationally exported Health Summary Types. Remote data may not be viewed by either the Ad Hoc Health Summary type or locally/user developed Health Summary types.
You can view remote clinical data using any Health Summary Type that has an identically named Health Summary Type installed at both the local and remote sites. However, for non-nationally exported health summary reports, the content of the report is subject to the report structure and configuration defined at the remote site.
Patch 29 (GMTS*2.7*29) adds the following Remote Data Views types.
REMOTE DEMO/VISITS/PCE (3M)
REMOTE MEDS/LABS/ORDERS (3M)
REMOTE TEXT REPORTS (3M)
REMOTE CLINICAL DATA (3M)
REMOTE CLINICAL DATA (1Y)
REMOTE DEMO/VISITS/PCE (1Y)
REMOTE MEDS/LABS/ORDERS (1Y)
REMOTE TEXT REPORTS (1Y)
REMOTE CLINICAL DATA (4Y)
REMOTE LABS LONG VIEW (12Y)
REMOTE LABS ALL (1Y)
REMOTE LABS ALL (3M)
REMOTE DIS SUM/SURG/PROD (12Y)
REMOTE OUTPATIENT MEDS (6M)
REMOTE ONCOLOGY VIEW
See Chapter 3, section 2 in the Health Summary User Manual for more information on using Remote Data Views.
GMTS*2.7*45 – INTERDISCIPLINARY PROGRESS NOTES
The purpose of this patch is to allow the Health Summary components 'Progress Notes' and 'Selected Progress Notes' to display the new interdisciplinary progress notes and all of the entries associated with the interdisciplinary note. The interdisciplinary note and all of the associated entries will be marked in the progress note components as follows.
**Note Type              	Marked as**
Primary Note          	Interdisciplinary Note
Addendum to Primary   	Interdisciplinary Note (addendum)
Child Note             	Interdisciplinary Note Entry
Addendum to Child     	Interdisciplinary Note Entry (addendum)
Patch GMTS*2.7*47 - CPRS Report Tab/NDBI/Misc Fixes
A menu of options has been added, CPRS Reports Tab “Health Summary Types List,” that allows users to control the Health Summary Types and the order that the Health Summary Types are listed in the Health Summary Types box on the Reports Tab of CPRS. This menu option has four menu items to edit and display the users’ preferences.
Patch GMTS*2.7*48 - REMOTE ONCOLOGY VIEW
This patch exports the REMOTE ONCOLOGY VIEW Health Summary Type and
installs it in the HEALTH SUMMARY TYPE file (#142), providing Remote
Data Views of Oncology Data. It also conducts a check to make sure
the Oncology Component is installed in the Patient Data Exchange's (PDX)
VAQ - DATA SEGMENT file (#394.71). This provides two methods for health
care providers and cancer registrars to request and view oncology data
on a patient seen at multiple sites: Remote Data Views for CPRS (GUI)
users and Patient Data Exchange for List Manager users.
Patch GMTS*2.7*49 - Demographics/HS Types List
A menu of options has been added, “CPRS Health Summary Display/Edit Site Defaults,” that allows IRM/Managers to control which Health Summary Types are on the reports tab and the order that the Health Summary Types appear in for the site. These site defaults will be used for users who do not have personal preferences set. This menu has four menu items to edit and display defaults for the site.
GMTS*2.7*50    Spinal Cord Dysfunction Update
GMTS*2.7*51    Radiology fixes
GMTS*2.7*52    Problem List HNC/MST Changes
GMTS*2.7*53    Demographics/Progress Notes Fixes
GMTS*2.7*54    Oncology ICD-O-3 Implementation
GMTS*2.7*55    Demographics/Progress Note Fixes
GMTS*2.7*56    DIVISION PARAMETER/DEMOGRAPHICS AND OTHER FIXES
GMTS*2.7*57    SURGERY DATA EXTRACTS
Patch GMTS*2.7*58     HS Objects and CNB/ADR/NOK/SII Components
A menu of options has been added, “Health Summary Objects Menu” that allows IRM/Managers to create Health Summary Objects to be used inside other documents. This menu also includes the ability to view, test, and export/import the Health Summary Objects. This patch also exports the new file HEALTH SUMMARY OBJECTS field #142.5, to store the Health Summary Object characteristics.
GMTS*2.7*59    BLOOD BANK COMPONENTS
GMTS*2.7*60    Race and Ethnicity (Demographics)
GMTS*2.7*61    Remote Medicine Report Fix
GMTS*2.7*62    MED/RXIV/HF/Miscellaneous
GMTS*2.7*63    Selection of Individual Health Factors
GMTS*2.7*64    TWEAK TO STANDARD REMOTE HEALTH SUMMARIES
GMTS*2.7*65    Non VA Medications
GMTS*2.7*66    CPRS HS REPORT ALLOCATION ERRORS
GMTS*2.7*67    NOT USED
GMTS*2.7*68    TRANSITIONAL PHARMACY HS OBJECT/TYPE
GMTS*2.7*69    Health Summary Resequencing/Medicine Correction
GMTS*2.7*7    HS Utilities, MXSTR Error
GMTS*2.7*70    GMTS SCHEDULING REPLACEMENT UPDATE
GMTS*2.7*71    CTD - HS Code Text Descriptors
GMTS*2.7*72    ONCOLOGY FORDS IMPLEMENTATION
GMTS*2.7*73    CORRECT BRANCH OF SERVICE IN DEMOGRAPHIC DISPLA
GMTS*2.7*74    HEALTH SUMMARY GAF COMPONENT
GMTS*2.7*75    RESTORE DISPLAY OF CLINICAL REMINDERS DISCLAIME
GMTS*2.7*76    ALPHA MODIFIERS NOT SHOWING AND COMMENTS PRINTI
GMTS*2.7*77    MENTAL HEALTH COMPONENTS
GMTS*2.7*78    NEW VITALS API AND OUTPATIENT PHARMACY API      GMTS*2.7*79    CORRECT REFERENCE RANGES ON REPORT TABS
GMTS*2.7*8     HS - PCE Components
GMTS*2.7*80    PHARMACY ENCAPSULATION
GMTS*2.7*81    VHA Enterprise Standard Title Display in Health C
GMTS*2.7*82    E-SIG BLOCK/HEALTH FACTORS/CLINICAL REMINDERS F
GMTS*2.7*83    DIETETICS COMPONENT UPDATE
GMTS*2.7*84    ADDING REASON FOR STUDY DISPLAY TO RADIOLOGY RE
GMTS*2.7*85    RESTRICT SENSITIVE DATA ON HEALTH SUMMARY PRINT
GMTS*2.7*87    NATIONAL HEALTH SUMMARY TYPES FOR SKIN RISK ASSMT
GMTS*2.7*88   LAB REFORMAT/142.1 UPDATE/SII COMP/HS BY LOC REPORT
Display column headers of TIU-Health Summary (HS) Object components when pulled up in succession.
Update Lab references range displays on HS report to coincide with format introduced by LR*5.2*356.
Update default value of fields TIME LIMITS and MAXIMUM OCCURRENCES for HS components MHA Admin List [MHAL] and MHA Score [MHAS] HS components.
Add new field, SHORT HS BY LOCATION COVER to the HEALTH SUMMARY
PARAMETERS FILE (#142.99) to change the number of times each location prints on the cover sheet from 6 to 1.
GMTS*2.7*89    SUPPORT OF CLINICAL REMINDERS ENHANCEMENTS
Patch GMTS*2.7*90 - ADD EARLIEST APPROPRIATE DATE TO HS ADHOC REPORT
Addition of the EARLIEST APPROPRIATE DATE (New Service Request 20051008) to the Health Summary Adhoc CNB - Brief Consults Report.
The EARLIEST APPROPRIATE DATE is the earliest appropriate date that the patient should be seen. This data field was added with CPRS v28.
GMTS*2.7*91  -  MHAL AND MHAS COMPONENTS NOT SHOWING ALL ADMININISTRATIONS
This patch will correct a defect in the MHAL and MHAS Health Summary components where all Mental Health instruments administered through the CPRS GUI do not display.
GMTS*2.7*92  -  CORRECTIONS TO MEDICATION WORKSHEET (TOOL #2)
This patch will correct a defect in the HEALTH SUMMARY COMPONENT file (#142.1) and creates a national entry for Tool #2: Medication Worksheet. Hard-coding of patient Social Security number has been removed and now all control of patient identifiers is controlled by the parameters set at the Health Summary Type level, consistent with other Class I software.
This patch also resolves the issue of the wrong pharmacy division printing on report headers by modifying internal programming. The internal programming that selects the name of the pharmacy division shown at the top of the worksheet and the pharmacy phone number associated with it has been revised. At facilities where there are multiple entries in OUTPATIENT SITE file (#59) that share the same SITE NUMBER, the Medication Worksheet is unable to distinguish between these entries in order to choose the correct pharmacy name and phone number for display in the report header. In these cases, the result may be that the displayed name and phone number are for a division other than the pharmacy’s preferred phone number for patient calls.
It also corrects a known issue from the initial release of Medication Reconciliation by adding status of HOLD to the Medication Worksheet.
GMTS*2.7*93 - COMBINE UNITS ON TRANSFUSION REPORT
This patch fixes a problem with the Blood Transfusion Report when using the report on a system running VBECS (Vista Blood Establishment Computer Software). The problem reported is that multiple units transfused on the same day were not being totaled but were rather displayed as separate lines for each transfused unit.
This patch corrects the problem by correctly totaling the units the way it did prior to VBECS.
This patch also adds Legacy Vista Data to the Blood Transfusion report. Prior to this change only transfusion data newly entered into VBECS were showing in the report. To see Legacy Vista Data, on the report, the parameter OR VBECS LEGACY REPORT has to be set to YES.
GMTS*2.7*95 – CORRECT B CROSS-REFERENCE
The NAME field (.01) of the HEALTH SUMMARY OBJECTS file (#142.5) had a 'B' cross-reference that only stored the first 30 characters of the name. When attempting to install a TIU/HS Object in Clinical Reminder Exchange, a FileMan error: "The update failed, UPDATE^DIE returned the following error message" would occur when the receiving site has multiple Health Summary Object entries that are not unique until after the 30-character length.
This patch corrects this problem by modifying the 'B' cross-reference to store the full 60 characters.
GMTS*2.7*99  – HIGH RISK MENTAL HEALTH PATIENT – NATIONAL REMINDER AND FLAG
This patch is in support of the Improve Veteran Mental Health (IVMH) initiative, High Risk Mental Health (HRMH) - National Reminder &amp; Flag. This patch will install four Health Summary Components, two Health Summary Types, a single Health Summary Object, and a single TIU/Health Summary object. The TIU/HS object will be used in the VA-MH HIGH RISK NO SHOW FOLLOW-UP Reminder Dialog distributed in PXRM*2*18.
**New Components, Types, and Objects in GMTS*2.7*99**
Four new entries are added to HEALTH SUMMARY COMPONENT (#142.1).
    1. MAS CONTACTS - This component will display contact phone numbers for the patient along with contact information for emergency and NOK contacts, if available.
    2. MAS MH CLINIC VISITS FUTURE - This component uses a Reminder Location List to help find the next appointment for the patient in any mental health clinic.
    3. MH HIGH RISK PRF HX - This component will display current assignment status and assignment history of the Category II (local) High Risk for Suicide Patient Record Flag.
    4. MH TREATMENT COORDINATOR - This component will display the Mental Health Treatment Coordinator assigned to this patient.
Two new entries are added to HEALTH SUMMARY TYPE (#142).
    1. VA-MH HIGH RISK PATIENT - This Type contains the four Health Summary Components mentioned above and is the basis for creating the VA-MH HIGH RISK PATIENT (TIU) Health Summary Object.
    1. REMOTE HIGH RISK MH PATIENT - This Type contains the same components as #1 and allows viewing the aforementioned information from remote sites.
One new entry is added to HEALTH SUMMARY OBJECT (#142.5).
    1. VA-MH HIGH RISK PATIENT (TIU) - This object is created from the VA-MH HIGH RISK PATIENT Health Summary Type and allows embedding the aforementioned information into a document. Its primary use here is to allow creation of the VA-MH HIGH RISK PATIENT TIU/HS object for use in the VA-MH HIGH RISK NO SHOW FOLLOW-UP Reminder Dialog.
One new entry is added to TIU DOCUMENT DEFINITION (#8925.1).
    1. VA-MH HIGH RISK PATIENT - This object makes the information found in the VA-MH HIGH RISK PATIENT Health Summary Type available for use in Reminder Dialogs and other documents.
GMTS*2.7*100 -PROBLEM WITH NEW MED WORKSHEET REPORT
The Medication Worksheet report in CPRS displayed a patient’s previous prescription Patient Instruction Signature comments in subsequent prescriptions, displaying incorrect Patient Instruction Signature comments for that prescription.
Routine GMTSPST2 has been modified to clear a prescription's signature lines before displaying a subsequent prescription.
Patch GMTS*2.7*102 – MENTAL HEALTH CLEANUP
The Mental Health package version 5.01 patch 60 (YS*5.01*60) removes
functionality from the Mental Health package that is no longer in use.
Specifically, patch YS*5.01*60 removes the MEDICAL RECORD file (file
#90), which the MENTAL HEALTH PHYSICAL EXAM health summary component
relies upon. Patch GMTS*2.7*102 will accomplish the following.
    1. Deactivate the MENTAL HEALTH PHYSICAL EXAM health summary component.
    2. Rebuild the Health Summary Adhoc Report (the GMTS HS ADHOC OPTION health summary type).
    3. Email a usage report containing the following listings.
        1. Health summary types that contain the MENTAL HEALTH PHYSICAL EXAM health summary component
        2. Health summary objects that contain the health summary types listed in (a)
    Patch GMTS*2.7*104 – MHTC &amp; CAT 1 PRF UPDATE TO HIGH RISK MH PATIENT HEALTH SUMMARY REPORT
    This patch is in support of Phase II of the Improve Veteran Mental Health (IVMH) initiative, High Risk Mental Health Patient (HRMHP) - National Reminder &amp; Flag project.
    This patch will modify two entries in the Health Summary Component file (142.1):
    MH HIGH RISK PRF HX and MH TREATMENT COORDINATOR.
    These components are used in the VA-MH HIGH RISK PATIENT and REMOTE MH
    HIGH RISK PATIENT Health Summaries; as well as being available for use in the Health Summary Adhoc Report.
    Additionally, the VA-MH HIGH RISK PATIENT Health Summary is embedded in the VA-MH HIGH RISK NO SHOW FOLLOW-UP Clinical Reminder Dialog which was released in Phase I of this project.
    The MH HIGH RISK PRF HX component includes the assignment history
    for the newly created Category I Patient Record Flag (HIGH RISK FOR SUICIDE). The assignment history in Health Summary displays both Category II (local) and Category I (National) assignments for High Risk for Suicide. Once all local entries have been converted to the national flag, you should only see the Category I Patient Record Flag.
    The MH TREATMENT COORDINATOR component has been activated with this patch and will display the Mental Health treatment Team, Mental Health Treatment4 Coordinator (MHTC), and the MHTC contact information.
    Sample output from the updated components.
    Health Summary Coordinator's Menu
    1      Print Health Summary Menu ...
    2      Build Health Summary Type Menu ...
    3      Set-up Batch Print Locations
    4      List Batch Health Summary Locations
    5      CPRS Reports Tab 'Health Summary Types List' Menu ...
    Select Health Summary Coordinator's Menu Option: 1 Print Health Summary Menu
    1      Patient Health Summary
    2      Ad Hoc Health Summary
    3      Range of Dates Patient Health Summary
    4      Visit Patient Health Summary
    5      Hospital Location Health Summary
    6      Batch Print of All Clinics by Visit Date
    Select Print Health Summary Menu Option: 1 Patient Health Summary
    Select Health Summary Type: VA-Mh High Risk Patient (VA-MH HIGH RISK PATIENT)
    Loading Ward Patient List...
    1A(1&amp;2) ward list
    1    AWHPATIENT, F   (0001)
    2    MHPATIENT, F    (0005)
    3    MHPATIENT, F    (0014)
    4    MHPATIENT, F    (0012) ~
    Select Patient(s): 1 AWHPATIENT,FEMALETWO
    09/13/2012 09:55
    *****************  CONFIDENTIAL MH HIGH RISK PATIENT SUMMARY  ******************
    AWHPATIENT,FEMALETWO    000-00-0001                          DOB: 05/11/1969
    1A(1&amp;2)
    -------------------------- MHRF - MH Suicide PRF Hx -------------------
    CATEGORY I (NATIONAL) PRF: HIGH RISK FOR SUICIDE
    Current Status: ACTIVE
    Date Assigned: Jan 18, 2012@08:49:28
    Next Review Date: APR 17, 2012
    Owner Site: SALT LAKE CITY HCS
    Originating Site: SALT LAKE CITY OIFO
    Assignment History:
    Date: JAN 18, 2012@08:49:28
    Action: NEW ASSIGNMENT
    Approved By: CPRSPROVIDER,TWENTY-SIX
    CATEGORY II (LOCAL) PRF: HIGH RISK FOR SUICIDE
    Current Status: INACTIVE
    Date Assigned: Dec 08, 2011@09:28:23
    Next Review Date: JAN 20, 2012
    Owner Site: SALT LAKE CITY HCS
    Originating Site: SALT LAKE CITY HCS
    Assignment History:
    Date: DEC 08, 2011@09:28:23
    Action: NEW ASSIGNMENT
    Approved By: CPRSPROVIDER,TWENTY-SIX
    Date: JAN 12, 2012@15:46:32
    Action: INACTIVATE
    Approved By: CPRSPROVIDER,TWENTY-SIX
    -------------------------- MHTC - MH Treatment Coor -------------------
    MH Treatment Team:  HRMH TEST TEAM
    MH Treatment Coordinator:  MHPROVIDER,TWENTY-SEVEN
    Office Phone:  555-123-4567
    Analog Pager:  12345
    Digital Pager:  98765
    Patch GMTS*2.7*107 – BUG FIXES - iMED NOTE, IMPORT HS OBJECT, VITALS TEXT
    This patch will resolve the following issues in the Health Summary package.
        1. INC000000418117 - Imed Consent note shows as unsigned
        1. Problem
    The problem occurs when the user selects either Heath summary component "SPN" (Selected Progress notes) or "PN" (Progress notes). If the user selects a "scanned document," VistA will append the text "&lt; THE ABOVE NOTE IS UNSIGNED &gt;" and "* DRAFT COPY *" to the bottom of the report even though scanned documents do not require a signature and are not drafts.
        1. Resolution
    Stopped the text from being appended on scanned documents that have an administrative closure date.
    Routine GMTSPN2 has been modified to check the TIU Document File. If the "ADMINISTRATIVE CLOSURE MODE" (1613) field is set to 'S' FOR scanned document, and "ADMINISTRATIVE CLOSURE DATE" (1606) has a value, the note will be excluded from having the unwanted text appended.
        1. INC000000752225 - ADHOC HS Vital Signs Detailed Display issue
        1. Problem
    When pain value of 99 is entered in vitals, the ADHOC Health Summary components ([VS] "Vital Signs", [VSD] "Vital Signs Detailed Display", and [SVS] "Vital Signs Selected") show the text "No Response”. When you view the same info via the Vitals Cumulative report, it correctly shows the text as "Unable to Respond”. No response to pain and unable to respond are two clinically different things.
        1. Resolution
    Changed the components to display "Unable to Respond"
    Routines GMTSVS, GMTSVSD, and GMTSVSS have been modified to write "Unable to Respond." GMTSVS was also modified to move Pain score to a new third line. GMTSVSS was also modified to allot more space (18 characters) for Pain score.
        1. INC000000784073 - Importing HS Object Questions
        1. Problem
    When using the [GMTS OBJ EXPORT] option in VistA, if one of the components used in the Health Summary type is a local component or has selected Items, the process completes with no error reported. However, when the receiving CAC tries to use the imported object, it fails to work. If VistA identifies the component as a local component or one that has selected Items, it simply omits the component without any type of error or warning.
        1. Resolution
    Modified VistA to return an error message and abort the export if the CAC tries to export a Health Summary Object that is associated with a Health Summary Type with a local component or selected items component. The following error messages were approved by the CPRS Clinical Workgroup.
        - "Can not export a Health Summary Object using a Health Summary Type that contains Local Health Summary Components"
        - "Health Summary Type &lt;TYPE&gt; contains Local Health Summary Component &lt;COMPONENT&gt;"
    Patch GMTS*2.7*101 - ICD-10 - Health Summary Updates
    This patch is part of the Computerized Patient Records System CPRSv30 project. This project will modify the Computerized Patient Record System, Text Integration Utilities, Consults, Health Summary, Problem List, Clinical Reminders, and Order Entry/Results Reporting to meet the requirements proposed by the Dept. of Health and Human Services
    to adopt ICD-10 code set standards Clinic Orders. This patch makes all changes to Health Summary that are required to move from the ICD-9 coding version to ICD-10.
        - Health Summary reports will differentiate between ICD-9 and ICD-10 diagnosis and procedure codes for diagnosis information that was coded using the ICD-9 or ICD-10 code set (not entered via free text) in CPRS. ADHOC reports allow the user to choose the Health Summary Components to include in the report. These reports can also display diagnosis information that users entered via other CPRS packages.
        - Health Summary Reports will print the ICD-9 or ICD-10 diagnosis or procedure diagnosis that was captured for the patient at the time the diagnosis was entered in CPRS and in the online report users entered via other CPRS packages.
    **Example: Display of Outpatient Diagnosis and Outpatient Encounter Components**
    **ICD-9 Example**
    <!-- image -->
    **ICD-10 Example**
    <!-- image -->
    Patch GMTS*2.7*111 - ICD-10 PTF Modifications - Health Summary Updates
    As part of the ICD-10 remediation effort for the VistA Admissions Discharge Transfer (ADT) module, DG*5.3*884 increased the maximum number of diagnosis, procedure, and operation codes that could be stored with a given entry in the PTF file (#45).  This Health Summary patch will update the following Health Summary Components (#142.1) to include the expanded fields as indicated.  Any Health Summary Type, Health Summary Object, TIU/HS Object, or OE/RR REPORT (#101.24) that uses these components as a basis for data will see the expanded fields (if populated) in the report output.
        - MAS ADMISSIONS/DISCHARGES – Updated to display up to 25 diagnosis codes with each occurrence.
        - MAS ADT HISTORY EXPANDED – Updated to display up to 25 diagnosis codes, up to 25 procedure codes, and up to 25 operation codes.
        - MAS DISCHARGE DIAGNOSIS – Updated to display up to 25 diagnosis codes with each occurrence.
        - MAS PROCEDURES ICD CODES – Updated to display up to 25 procedure codes with each occurrence.
        - **MAS SURGERIES ICD CODES – Updated to display up to 25 operation codes with each occurrence.**

### Released Patches for Health Summary 2.7

| **Patch #**   | **Description**                                                       | **Release Date**   |
|---------------|-----------------------------------------------------------------------|--------------------|
| GMTS*2.7*1    | Syntax Error in GMTS                                                  | 12/28/95           |
| GMTS*2.7*2    | Visit Dates, Task &                                                   | 02/29/96           |
| GMTS*2.7*3    | LAB Anatomic Path Ac                                                  | 09/06/96           |
| GMTS*2.7*4    | Medicine Data w/ Quo                                                  | 04/12/96           |
| GMTS*2.7*5    | CVP, EADT, Nightly T                                                  | 05/13/96           |
| GMTS*2.7*6    | Patient Selection                                                     | 06/06/96           |
| GMTS*2.7*7    | HS Utilities, MXSTR                                                   | 11/24/96           |
| GMTS*2.7*8    | HS - PCE Components                                                   | 08/22/96           |
| GMTS*2.7*9    | Lab Orders/Surgical                                                   | 11/08/96           |
| GMTS*2.7*10   | PCE Components                                                        | 03/04/97           |
| GMTS*2.7*11   | SURGERY COMPONENT FI                                                  | 10/23/98           |
| GMTS*2.7*12   | TIU-COMPATIBLE COMPO                                                  | 09/29/97           |
| GMTS*2.7*13   | Spinal Cord Dysfunct                                                  | 01/06/97           |
| GMTS*2.7*14   | Updated Rad/Nuc Med                                                   | 05/15/97           |
| GMTS*2.7*15   | Pharmacy & Current O                                                  | 06/05/98           |
| GMTS*2.7*16   | Health Summary Fixes                                                  | 10/07/97           |
| GMTS*2.7*17   | Blood Bank Component                                                  | 10/07/97           |
| GMTS*2.7*18   | Code change to accom                                                  | 03/27/98           |
| GMTS*2.7*19   | Duplicates on CVP co                                                  | 10/10/97           |
| GMTS*2.7*20   | UPDATED COMPONENTS f                                                  | 06/05/98           |
| GMTS*2.7*21   | Report headings and                                                   | 03/30/98           |
| GMTS*2.7*22   | Reminders-historical                                                  | 11/10/97           |
| GMTS*2.7*23   | NEW REMINDER COMPONE                                                  | 02/05/98           |
| GMTS*2.7*24   | Patient selection &                                                   | 03/30/98           |
| GMTS*2.7*25   | Component fixes                                                       | 09/10/98           |
| GMTS*2.7*26   | Imaging Component                                                     | 09/09/99           |
| GMTS*2.7*27   | Y2K COMPLIANCE CHANG                                                  | 04/17/98           |
| GMTS*2.7*28   | Y2K, NKA, LAB, VITAL                                                  | 03/05/99           |
| GMTS*2.7*29   | Remote Data View/Pri                                                  | 05/17/01           |
| GMTS*2.7*30   | HS Type Lookup/Concu                                                  | 08/06/99           |
| GMTS*2.7*31   | Inactive Clinics                                                      | 10/12/99           |
| GMTS*2.7*32   | Fix HS Type Lookup                                                    | 09/28/99           |
| GMTS*2.7*33   | Progress Notes by Vi                                                  | 10/13/99           |
| GMTS*2.7*34   | Clinical Reminder Di                                                  | 06/21/00           |
| GMTS*2.7*35   | Vitals/GAF/Oncology/                                                  | 05/19/00           |
| GMTS*2.7*36   | Oncology/Lab/Ad Hoc                                                   | 12/06/99           |
| GMTS*2.7*37   | CPT Modifiers and RX                                                  | 07/28/00           |
| GMTS*2.7*40   | Undefined Variable D                                                  | 09/01/00           |
| GMTS*2.7*42   | Oncology Component C                                                  | 12/21/00           |
| GMTS*2.7*43   | HFS/Window Print Fix                                                  | 05/07/01           |
| GMTS*2.7*44   | Error in GAF Score                                                    | 12/27/00           |
| GMTS*2.7*45   | Interdisciplinary Pr                                                  | 04/20/01           |
| GMTS*2.7*46   | Consults Brief Component                                              | 06/28/01           |
| GMTS*2.7*47   | CPRS Report Tab/NDBI                                                  | 10/04/01           |
| GMTS*2.7*48   | Remote Oncology View                                                  | 09/05/01           |
| GMTS*2.7*50   | Spinal Cord Dysfunct                                                  | 02/01/02           |
| GMTS*2.7*49   | Demographics/HS Type                                                  | 03/05/02           |
| GMTS*2.7*51   | Radiology fixes                                                       | 04/25/02           |
| GMTS*2.7*54   | Oncology ICD-O-3 Impleme                                              | 05/07/02           |
| GMTS*2.7*55   | Demographics/Progress No                                              | 05/23/02           |
| GMTS*2.7*52   | Problem List HNC/MST Cha                                              | 05/24/02           |
| GMTS*2.7*56   | Division Parameter/Demog                                              | 09/10/02           |
| GMTS*2.7*57   | Surgery Data Extracts                                                 | 9/7/04             |
| GMTS*2.7*58   | HS Objects and Components                                             | 1/03               |
| GMTS*2.7*59   | BLOOD BANK COMPONENTS                                                 | 12/6/02            |
| GMTS*2.7*60   | Race and Ethnicity (Demographics)                                     | 1/15/03            |
| GMTS*2.7*61   | Remote Medicine Report Fix                                            | 12/10/02           |
| GMTS*2.7*62   | MED/RXIV/HF/Miscellaneous                                             | 9/23/03            |
| GMTS*2.7*63   | Selection of Individual Health Factors                                | 2/15/05            |
| GMTS*2.7*64   | TWEAK TO STANDARD REMOTE HEALTH SUMMARIES                             | 10/7/03            |
| GMTS*2.7*65   | Non VA Medications                                                    | 5/20/04            |
| GMTS*2.7*66   | CPRS HS REPORT ALLOCATION ERRORS                                      | 7/29/04            |
| GMTS*2.7*67   | NOT USED                                                              |                    |
| GMTS*2.7*68   | TRANSITIONAL PHARMACY HS OBJECT/TYPE                                  | 9/12/03            |
| GMTS*2.7*69   | Health Summary Resequencing/Medicine Correction                       | 2/23/04            |
| GMTS*2.7*70   | GMTS SCHEDULING REPLACEMENT UPDATE                                    | 12/27/06           |
| GMTS*2.7*71   | CTD - HS Code Text Descriptors                                        | 12/08/04           |
| GMTS*2.7*72   | ONCOLOGY FORDS IMPLEMENTATION                                         | 4/01/05            |
| GMTS*2.7*73   | CORRECT BRANCH OF SERVICE IN DEMOGRAPHIC DISPLAY                      | 7/18/05            |
| GMTS*2.7*74   | HEALTH SUMMARY GAF COMPONENT                                          | 11/21/05           |
| GMTS*2.7*75   | RESTORE DISPLAY OF CLINICAL REMINDERS DISCLAIMER                      | 10/24/06           |
| GMTS*2.7*76   | ALPHA MODIFIERS NOT SHOWING AND COMMENTS PRINTI                       | 5/04/06            |
| GMTS*2.7*77   | MENTAL HEALTH COMPONENTS                                              | 1/07/08            |
| GMTS*2.7*78   | NEW VITALS API AND OUTPATIENT PHARMACY API                            | 4/24/06            |
| GMTS*2.7*79   | CORRECT REFERENCE RANGES ON REPORT TABS                               | 12/22/05           |
| GMTS*2.7*80   | PHARMACY ENCAPSULATION                                                | 8/20/08            |
| GMTS*2.7*81   | VHA Enterprise Standard Title Display in Health                       | 5/08/06            |
| GMTS*2.7*82   | E-SIG BLOCK/HEALTH FACTORS/CLINICAL REMINDERS F                       | 9/19/08            |
| GMTS*2.7*83   | DIETETICS COMPONENT UPDATE                                            | 9/28/07            |
| GMTS*2.7*84   | ADDING REASON FOR STUDY DISPLAY TO RADIOLOGY RE                       | 8/20/08            |
| GMTS*2.7*85   | RESTRICT SENSITIVE DATA ON HEALTH SUMMARY PRINT                       | 3/19/08            |
| GMTS*2.7*87   | NATIONAL HEALTH SUMMARY TYPES FOR SKIN RISK ASSESSMENT                | 10/30/07           |
| GMTS*2.7*88   | LAB REFORMAT/142.1 UPDATE/SII COMP/HS BY LOC REPORT                   | 10/28/11           |
| GMTS*2.7*89   | SUPPORT OF CLINICAL REMINDERS ENHANCEMENTS                            | 9/16/09            |
| GMTS*2.7*90   | ADD EARLIEST APPROPRIATE DATE TO HS ADHOC REPORT                      | 3/11               |
| GMTS*2.7*91   | MHAL AND MHAS COMPONENTS NOT SHOWING ALL ADMINISTRATIONS              | 6/26/09            |
| GMTS*2.7*92   | Corrections to Medication Worksheet (Tool #2)                         | 4/11               |
| GMTS*2.7*93   | COMBINE UNITS ON TRANSFUSION REPORT                                   | 6/22/10            |
| GMTS*2.7*94   | Updates for the Essential Med List for Review                         | 9/2018             |
| GMTS*2.7*99   | HIGH RISK MENTAL HEALTH PATIENT – NATIONAL REMINDER AND FLAG          | 4/12               |
| GMTS*2.7*101  | ICD-10 UPDATES                                                        | 5/14               |
| GMTS*2.7*102  | MENTAL HEALTH CLEANUP                                                 | 9/12               |
| GMTS*2.7*104  | MHTC & CAT 1 PRF UPDATE TO HIGH RISK MH PATIENT HEALTH SUMMARY REPORT | 10/12              |
| GMTS*2.7*107  | BUG FIXES - iMED NOTE, IMPORT HS OBJECT, VITALS TEXT                  | 11/2013            |
| GMTS*2.7*111  | ICD-10 PTF MODIFICATIONS                                              | 8/2015             |
| GMTS*2.7*125  | HEALTH SUMMARY COMPONENTS                                             | 5/2019             |


## Index

%INDEX, 48

^LOOP, 21

Ad Hoc Health Summaries, 19

**Ad Hoc Summary** , 52

*Ad Hoc Summary Driver* , 36

ancillary packages, 1

Appendix A—Defining New Components, 54

Appendix DHealth Summary Security, 65

batch processing, 20

Callable Routines, 35

**Components** , 52

Components and Types, 1

**Create/Modify Health** , 15

**Create/Modify Health Summary Components** , 58

**Create/Modify Health Summary Type** , 16

customized, 20

Customized Health Summary Types, 20

Customizing the AD HOC Health Summary Type, 21

**Data Dictionaries** , 49

Database Integration Agreements, 41

**Default** , 52

default parameters, 15

Defining New Components, 54

***Definitions*** , 1

**Disable/Enable Health Summary Component** , 15

DISABLED components, 15

E3Rs, 54

Edit Ad Hoc Health Summary Type, 21

**Edit Health Summary Site Parameters** , 16

Encounter Form Utilities, 19

enhanced patient look-up, 19

External Relations, 41

Files and Globals List, 25

**Function** , 31

Generating Online Documentation, 43

Globals, 25

Glossary, 52

**GMTS** , 35

GMTS COMPONENT NAME, 31

GMTS TASK STARTUP, 20

GMTS TYPE DELETE, 34

**GMTSADOR** , 36

**GMTSDVR** , 36, 37

GMTSMGR security key, 16

**GMTSU** , 37, 38, 39

**GMTSUP** , 39

Headers and Abbreviations, 20

*Health Summary Alternate Drive* , 36, 37

Health Summary files, 25

Health Summary Maintenance Menu, 15

Health Summary Security, 65

Health Summary Type file, 1

**Hospital Location** , 52

**ICD Text Displayed** , 52

INCLUDE BAR CODE ON ACT PROFILES, 16

INCLUDE COMMENTS ON LABS, 16

Information Menu option, 20

Integrated Billing Package, 19

**Lock** , 53, 66

Locks and Security, 66

Maintenance Menu, 15

modify an existing health summary type, 16

**Namespace** , 23

Nightly Batch Processing, 20

**Non-destructive** , 53

Non-destructive, read-only component routines, 41

occurrence limits, 20

**Occurrence Limits** , 53

OE/RR Interface, 19

OUT OF ORDER MESSAGE, 15

**Owner** , 53

Packages Providing Data, 1

*Pagination Utilities* , 39

PDX Transmission of Health Summaries, 2

permanent health summaries, 2

Print Manager, 19

**Printing Data Dictionaries** , 49

Printing Health Summaries, 2

PROMPT FOR ACTION PROFILE, 16

**Provider Narrative** , 53

Purging and Archiving, 34

queuing, 19

**Rebuild Ad Hoc Health Summary Type** , 15

Request for Health Summary Type, 20

**Resequence a Health Summary Type** , 15

Routine Descriptions, 23

Routines, 47

Schedule/Unschedule Options, 20

Security, 65

*SHOP,ALL* , 54

SPOOL DEVICE, 16

storage, 34

**Summary Order** , 53

**Summary Type** , 53

TASK STARTUP, 20

Time and Occurrence limits, 15

time limits, 20

Time Limits, 53

## —%—

## —^—

## —A—

## —B—

## —C—

## —D—

## —E—

## —F—

## —G—

## —H—

## —I—

## —L—

## —M—

## —N—

## —O—

## —P—

## —Q—

## —R—

## —S—

## —T—