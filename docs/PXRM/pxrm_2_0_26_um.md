---
app_name: 'Registry: Airborne Hazard Open Burn Pit (AHOBPR) (PXRM)'
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: null
doc_type: user-manual
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
source_file: pxrm_2_0_26_um.docx
status: draft
title: '#'
---

# Clinical Reminders ICD-10 Updates

# PXRM*2*26

User Manual

May 2014


Product Development

Revision History

| Date         | Description                     | Author   |
|--------------|---------------------------------|----------|
| March 2014   | Updates per test version 7      | REDACTED |
| January 2014 | Updates per test version 6      | REDACTED |
| Nov-Dec 2013 | Updates per Analyst review      | REDACTED |
| October 2013 | Updates per test version 5      | REDACTED |
| July 2013    | Added Dialog changes            | REDACTED |
| June 2013    | Added Dialog changes for ICD-10 | REDACTED |
| Feb 2013     | Created draft user manual       | REDACTED |
|              |                                 |          |

Table of Contents

1.	Background	1

1.1.	Clinical Reminders	1

2.	Introduction	2

2.1.	Purpose of this Manual	2

2.2.	Related Documentation	3

2.3.	Related Web Sites	3

2.4.	Target Audience	3

3.	Taxonomy Management Changes	4

3.1.	Changes made to Taxonomy Management by Patch 26 (PXRM*2*26)	4

3.2.	Taxonomy Management Dialog Changes	5

4.	Reminder Taxonomy Management Overview	7

5.	Using Reminder Taxonomy	10

5.1.	Reminder Taxonomy Management Main Screen	10

5.2.	Reminder Taxonomy Management Actions	10

5.2.1.	Reminder Taxonomy Action Examples	12

5.2.2.	Use in Dialog Report	53

6.	Using Reminder Dialogs Taxonomy Features	55

6.1.	Background – Before and After	55

6.2.	New Fields	55

6.3.	Examples	59

7.	Glossary/Acronyms	72

Appendix A – ScreenMan and Browser Overviews	74

7.1.1.	Browser Overview	78

Table of Figures

Figure 1: Terminal Setup	8

Figure 2: Display Setup	9

Figure 3: Save from scrolling regions	9

Figure 4: Taxonomy Management main screen	10

Figure 5: Edit Action Screen	22

Figure 6: Edit Action Form 2	24

Figure 7: Coding System Selection Form	25

Figure 8: Copying a taxonomy definition screen	27

Figure 9: Standard Editing form	28

Figure 10: Standard Editing form 2	29

Figure 11: Browsing Taxonomy Inquiry	31

Figure 12: Browsing Taxonomy Change Log	33

Figure 13: Selecting Code Search screen	34

Figure 14: Code Search Results	35

Figure 15: Example Spreadsheet for Importing codes from a CSV file	36

Figure 16: Selecting Import Method example	37

Figure 17: Taxonomy Inquire example	40

Figure 18: Excel Spreadshee with codes	41

Figure 19: Opening spreadsheet as a text file	42

Figure 20: Entering the number of the Taxonomy that the import file will be imported to	43

Figure 21: Select PA as the import method	43

Figure 22: Pasting the CSV file	44

Figure 23: Browsing the list of codes that were pasted	45

Figure 24: Taxonomy Inquiry of codes that were pasted	46

Figure 25: Using the TAX option to import a taxonomy from another taxonomy	47

Figure 26: Selecting another taxonomy to import from	48

Figure 27: Browsing list of codes screen	49

Figure 28: Importing a taxonomy from a web site	50

Figure 29: Starting the import process	51

Figure 30: Browsing the list of codes imported from a website	52

Figure 31: Browsing Use in Dialog Report	54

Figure 32: ScreenMan Screen	74

## 1 Background

The International Classification of Diseases (ICD) is a clinical coding system developed, monitored, and copyrighted by the World Health Organization (WHO). In the United States (US), the National Center for Health Statistics (NCHS), part of the Centers for Medicare and Medicaid Services (CMS), is the agency responsible for overseeing of the clinical modification to the ICD code set.

On January 16, 2009, the Department of Health and Human Services (HHS) published the 45 CFR Part 162 Final Rule for the Health Insurance Portability and Accountability Act (HIPAA) Administrative Simplification: Modifications to Medical Data Code Set Standards to Adopt the International Classification of Diseases, 10 th Revision Clinical Modification and Procedure Coding System (ICD-10-CM and ICD-10-PCS) for all healthcare organizations currently using the 9 th Edition of the Clinical Modification code set, or ICD-9-CM (also just referred to as “ICD-9”). Presently, ICD-9-CM encompasses both Clinical Modification and Procedure Coding System code set. On August 24, 2012, the Secretary for HHS published final ruling officially changing the ICD-10 compliance date to October 1, 2014 – Congress has since changed the compliance date to October 2015.

**Implementation** of ICD-10-CM and PCS is an immense undertaking, requiring system and business changes throughout all HIPAA-covered entities of the health care industry, including the U.S. Department of Veterans Affairs (VA). All inpatient discharges and outpatient encounter dates on or after the compliance date will require ICD-10 codes as the standard code set for recording and reporting diagnosis and inpatient procedures.  This transition will impact Information Technology (IT) systems, secondary data stores, forms and business processes and stakeholders at all levels of the organization.

### Clinical Reminders

Sites will need to identify clinical reminder taxonomies that may be used in one or more clinical reminders. The next step will be to determine the ICD-10 codes to be added when the software is made available for use.

For services occurring on October 1, 2015, ICD-9 codes will become inactive. It will important to assure that the comparable ICD-10 codes are added to the reminder taxonomies in order for those codes to become active on the compliance date. Because ICD-9 taxonomies, however, may have historical data needed for Clinical Reminders even after the compliance date, previous ICD-9 codes will not be removed. ICD-10 codes will read as “selectable” and able to be added to the taxonomies as a range or as individual codes, depending on what needs to be included in the Clinical Reminder definitions.


## 3 Introduction

The purpose of the Clinical Reminders ICD-10 Update project is to update Clinical Reminders to allow the use of ICD-10 codes. A very general approach has been taken, wherein Clinical Reminders taxonomies are being restructured to be Lexicon-based instead of pointer-based. This allows the use of any coding system supported by the Lexicon package. In addition to adding ICD-10 codes, SNOMED CT codes are being added. When CPRS 29 is released, SNOMED CT codes will be collected by Problem List, and Clinical Reminders will be able to search for them.

The project includes three patches:

**DG*5.3*862 - PTF ICD-10 CHANGES FOR CLINICAL REMINDERS**

This build updates the Clinical Reminders Index cross-references in the PTF file (#45) to accommodate ICD-10 diagnosis and procedure codes. It restructures the PTF portion of the Clinical Reminders Index to a generic format that can support all ICD coding systems. See the Clinical Reminders Index Technical Guide/Developer’s Manual (PXRM\_INDEX\_TM) for more information.

**GMPL*2.0*44** - **PROBLEM LIST ICD-10 CHANGES FOR CLINICAL REMINDERS**

This build updates the Clinical Reminders Index cross-references in the Problem file (#9000011) to accommodate ICD-10 CM diagnosis codes. It restructures the Problem List portion of the Clinical Reminders Index to a generic format that can support ICD and SNOMED CT coding systems. See the Clinical Reminders Index Technical Guide/Developer’s Manual (PXRM\_INDEX\_TM) for more information.

**PXRM*2.0*26**

This build changes Clinical Reminders taxonomies from being pointer-based to being Lexicon- based. A number of things are done to accomplish this. The Reminder Taxonomy data dictionary (file #811.2) is restructured, a new taxonomy management system is introduced, and taxonomy evaluation is changed to accommodate the new structure. For Reminder Dialogs, users will no longer be able to add ICD-9-CM and/or CPT-4 codes to a Reminder Dialog, but will need to create a Taxonomy, assign codes, and then add the Taxonomy to the Reminder Dialog.

Under the Lexicon-based structure, codes are no longer entered as a range, eliminating the need for taxonomy expansion. The post-install routine will convert all existing taxonomies to the new structure.

See the Taxonomy Management and Dialog Management sections of the Clinical Reminders Manager’s Manual for details of the new taxonomy management system.

### Purpose of this Manual

This manual is intended for Clinical Application Coordinators and other Clinical Reminders managers who will create and modify taxonomies to use the new ICD-10 codes. It describes the various actions available for adding, editing, copying, and importing codes.

### Related Documentation

| Documentation                                               | Documentation File name   |                 |
|-------------------------------------------------------------|---------------------------|-----------------|
| Installation Guide                                          | PXRM_2_0_26_IG.PDF        |                 |
| Release Notes                                               | PXRM_2_0_26_RN.PDF        |                 |
| Clinical Reminders Manager’s Manual                         | PXRM_2_0_MM.PDF           |                 |
| Technical Manual                                            | PXRM_2_0_TM.PDF           | PXRM_2_0_TM.PDF |
| Clinical Reminders Index Technical Guide/Developer’s Manual | PXRM_INDEX_TM.PDF         |                 |

### ### ### Related Web Sites

| Site                                                      | URL                                                                                                                | Description                                                                                      |
|-----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| National Clinical Reminders site                          | http://vista.med.va.gov/reminders                                                                                  | Contains manuals, PowerPoint presentations, and other information about Clinical Reminders.      |
| National Clinical Reminders Committee SharePoint site     | [http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx](http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx) | This committee directs the development of new and revised national reminders.                    |
| VistA Document Library                                    | [http://www.va.gov/vdl/](http://www.va.gov/vdl/)                                                                   | Contains manuals for Clinical Reminders and related applications.                                |
| Health Information Management (HIM) ICD-10 Implementation | [http://vaww.vhahim.va.gov/](http://vaww.vhahim.va.gov/)                                                           | Contains general information, training resources, and other tools for VA’s transition to ICD-10. |

### Target Audience

Clinical Reminders Managers

Clinical Application Coordinators (CACs)

## 4 Taxonomy Management Changes

Reminder taxonomies, stored in file #811.2, provide a convenient way to create a set of coded values and give the set a name. For example, the VA-DIABETES taxonomy contains a list of ICD diagnosis codes that signify the patient has a diagnosis of diabetes.


### Changes made to Taxonomy Management by Patch 26 (PXRM*2*26)

***In the past*** , taxonomies were based on pointers to the ICD diagnosis file (#80), the ICD Operation/ Procedure file (#80.1), and the CPT file (#81). Multiple ranges of codes (low code to high code) could be defined for each of these coding systems. When editing was finished, each range of codes was expanded to include all the codes from the low code to the high code.

Some coding systems such as SNOMED CT do not assign any meaning to the codes, so they cannot be grouped by code and the concept of a range of codes is meaningless. In some cases, for coding systems that do support the concept of a range, code set updates have inserted an unrelated code into a range.

***New Approach:*** For the above reasons, patch PXRM*2*26  changes taxonomies so that they are Lexicon-based. This is a general approach that allows Clinical Reminders taxonomies to support any coding system defined in Lexicon’s Coding Systems file (#757.03), provided Lexicon maintains the coding system and patient data using the coding system is stored in VistA.

For each coding system it includes, the Coding Systems file defines a three-character abbreviation, nomenclature, source title, and source. Example: ICD, ICD-9-CM, International Classification of Diseases, Diagnosis, 9th Edition, and US Department of Health and Human Services. The three-character abbreviation provides a convenient way to refer to coding systems and is used by Clinical Reminders Taxonomies. The following coding systems are supported by Clinical Reminders:

| **Abbreviation**   | **Nomenclature**   |
|--------------------|--------------------|
| 10D                | ICD-10-CM          |
| 10P                | ICD-10-Proc        |
| CPT                | CPT-4              |
| CPC                | HCPCS              |
| ICD                | ICD-9-CM           |
| ICP                | ICD-9-Proc         |
| SCT                | SNOMED CT          |

### Taxonomy Management Dialog Changes

***In the past*** , users created Reminder Dialogs containing ICD-9-CM and/or CPT-4 codes. When using codes as Finding Items or Additional Finding Items in CPRS, the end user didn’t select codes; codes were automatically filed to VistA when the element/group was selected in the Reminder Dialog.

A Taxonomy could only be used as a Finding Item; it created a pick list of codes for the user to pick from in CPRS. The display in CPRS was controlled by the set-up in the Reminder Finding Parameter File (#801.45) and the Reminder Taxonomy File (#811.2). These controls determined if the Taxonomy should assign codes to the current encounter or an historical encounter. The controls also determined what prompts were assigned to the Reminder Dialog in CPRS.

***New approach*** : Users will no longer be able to add ICD-9-CM and/or CPT-4 codes to a Reminder Dialog. Users will need to create a Taxonomy, assign codes, and then add the Taxonomy to the Reminder Dialog. To maintain similar end user functionality in CPRS, a new prompt called Taxonomy Pick List Display has been  added to the dialog editor. This controls how Taxonomies should display in CPRS.

**New Fields**

***Taxonomy Pick List*** = This field controls if and what pick lists should appear in CPRS. The possible values are based on the setup of the Taxonomy in the Finding Item Field. If a pick list is set to not display, the active codes marked to be used in a dialog will automatically be filed to PCE for the encounter date for that element when the finish button is clicked.

- Four choices for display of pick list
- **CPT ONLY** – Displays ‘pick list’ for CPT only. All ICD codes in taxonomy are entered into PCE
- **NONE** – No ‘pick list’ for either ICD or CPT. All codes in taxonomy are entered into PCE
- Have to have a choice selected.
- These pick lists are only relevant for the Finding Type field (not Additional Findings field).

***Diagnosis Header*** : This field displays text that will be used for the Taxonomy Checkbox. The prompt is only available if the Taxonomy Selection Value is set to All. The default value is from the Reminder Finding Type Parameter.

***Procedure Header*** : This field displays text that will be used for the Taxonomy Checkbox. The prompt is only available if the Taxonomy Selection Value is set to All.. The default value is from the Reminder Finding Type Parameter.

Also, after PXRM*2.0*26, users will no longer be able to set one Taxonomy Element to prompt for both Current  and Historical Encounter Data. Users will need to create an element for each encounter type, Current and Historical.  If the element Resolution Type is set to Done Elsewhere, then the editor will prompt the user to accept the default prompts for the taxonomy which includes prompts for historical data.  prompt for historical data. Any other resolution type or no resolution type will prompt data for the current encounter date.

For the ICD-10 implementation, Reminder Dialogs will display ICD-9-CM or ICD-10-CM codes in a pick list based on the code set versioning rules. Reminder Dialogs determine what codes to display using the following rules:

- Current encounters= active codes for that encounter date; Addendums will use the parent note Encounter date.
- Historical encounters= active codes for system date

**Also note** that previously dialogs were set to both current and historical encounters.   Dialogs are now set to current encounters only. Please review dialogs before using in CPRS.

## 5 Reminder Taxonomy Management Overview

A new taxonomy management system replaces the previous taxonomy management menu. The new system uses a combination of List Manager, ScreenMan, and the Browser. List Manager should already be familiar to users of Clinical Reminders tools such as Dialog Management or Reminder Exchange. ScreenMan and the Browser may not be as familiar, but reviewing Appendix A of this manual or the FileMan documentation should give you enough knowledge to make using the taxonomy management system much easier.

**ScreenMan Overview**

ScreenMan is VA FileMan's *screen-oriented* data entry tool. It is an alternative to the Scrolling Mode approach. With ScreenMan, data is entered in *forms* . Each form field occupies a fixed position on the screen (instead of scrolling off!). You can see many data fields at once, and use simple key combinations to edit data and move from field to field on a screen. You can also move from one screen to another like turning through the pages of a book.

If you are not familiar with how to use ScreenMan, see Appendix A of this manual for a brief overview. ***For a detailed explanation of using ScreenMan and the Browser, please refer to the VA FileMan Getting Started manual.***

**Browser Overview**

The Browser lets you view any report *on the screen* instead of *on paper* . Do this by printing your report to the **BROWSER** device instead of the HOME device or a printer.

The Browser makes it very easy to view reports on screen. Its main features are:

1. Scroll forwards *and backwards* through a report. This means you don't lose reports "off the top" of the screen, like you do when you print to the HOME device.
2. Use the Search feature to find and immediately jump to any text in a report.
3. Copy text from the report to the VA FileMan Clipboard; later, if you're editing a mail message or other WORD-PROCESSING-type field with the Screen Editor, you can paste from the clipboard.

For more information on the Screen Editor, please refer to Chapter, "Screen Editor," in the FileMan Getting Started User Manual.

The Browser also lets you browse the contents of any word-processing-type field.

**Shortcuts and Screen setup Tips**

Both the Browser and ScreenMan have shortcuts that can save you a lot of time. Each shortcut begins by pressing the Num Lock (NL) key. (NOTE: some laptops don’t have a NumLock key, so you would need to use Map Keyboard on your Reflections Utility menu to map a terminal key to the PC NumLock key.)

Some Browser actions:

- (NL)B – go to bottom
- (NL)E – exit
- (NL)F – find
- (NL)H – help
- (NL)Q – quit
- (NL)T – go to top

Some ScreenMan shortcuts:

- (NL)C – close a screen
- (NL)E – exit and save changes
- (NL)H – help
- (NL)Q – exit and do not save changes
- (NL)Z – zoom editor

Your Reflections session setup makes a difference in the appearance of the ScreenMan display. The screen element Normal default is a white background and black foreground. Choosing a background color other than white and a foreground color that works well with the background color will provide a more readable ScreenMan display.

Figure 1: Terminal Setup

**Missing text when printing tip**

You may notice when printing large amounts of text to the screen, parts of it are missing. To fix this, the Reflections setup must have Save from Scrolling Regions checked. The sequence is:: Setup =&gt; Display =&gt; Screen =&gt; Display Memory Advanced.

Figure 2: Display Setup

Figure 3: Save from scrolling regions

## 6 Using Reminder Taxonomy

### Reminder Taxonomy Management Main Screen

When you select Taxonomy Management from the Clinical Reminders Manager Menu, you will go into a List Manager Taxonomy Management screen. It lists all of the taxonomies on your system. You can use the standard List Manager actions to search or scroll through the list.


Figure 4: Taxonomy Management main screen


### Reminder Taxonomy Management Actions

| Synonym   | Action       | Description                                                                                                                                                                                    |
|-----------|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ADD       | Add          | Use this action to create a new taxonomy.                                                                                                                                                      |
| EDIT      | Edit         | Use this action to edit an existing taxonomy.                                                                                                                                                  |
| COPY      | Copy         | This action allows the user to copy an existing taxonomy into a new one. The new taxonomy must have a unique name.                                                                             |
| INQ       | Inquire      | Use this action to obtain a detailed report about a taxonomy. It lists all the codes that have been selected, the code’s status, and shows if the code has been marked as Use In Dialog (UID). |
| CL        | Change Log   | Use this action to display a taxonomy’s change log (edit history).                                                                                                                             |
| EH        | Edit History | Use this action to display a taxonomy’s edit history.                                                                                                                                          |
| CS        | Code Search  | This action can be used to find all taxonomies that include a particular code.                                                                                                                 |
| IMP       | Import       | Use this action to import codes from a CSV file.                                                                                                                                               |
| UIDR      | UID Report   | This action runs the UID report which displays all inactive codes marked as UID.                                                                                                               |

For the Edit, Copy, Inquire, and Edit History actions, you can select the action and then the entry number, or if you select an entry, you will be prompted to choose one of these actions. When the Import action is selected, it prompts you for a taxonomy to import into. Code Search and UID Report do not prompt for a taxonomy because these reports are run on all taxonomies.

***NOTE –  KNOWN ANOMALY:**

For any action that works with a list, you can select the list and then the action or select the action and then the list. In the first case, the system uses List Manager’s list selection, which displays the list as a string of items. If the list has too many items, it generates an error.

The workaround is to select the action first.

For example, on the code selection screen, if you do an ICD-10 Lexicon search for diabetes, you will see a list of around 250 codes. If you enter 1-250 at the Select Action prompt, you’ll get a range error. However, if you select Add, then you can enter 1-250 and not get an error.

**Lexicon Selection** Nov 14, 2013@11:16:15        Page:   57 of   57

Term/Code: diabetes

253 ICD-10-CM codes were found.

+No. Code      Active     Inactive  Description

Gestational Diabetes

250 P70.2     10/1/2014            Neonatal diabetes mellitus

251 Z13.1     10/1/2014            Encounter for Screening for Diabetes

Mellitus

252 Z83.3     10/1/2014            Family History of Diabetes Mellitus

253 Z86.32    10/1/2014            Personal History of Gestational Diabetes

**+ Next Screen   - Prev Screen   ?? More Actions**

ADD  Add to taxonomy                    UID  Use in dialog

RFT  Remove from taxonomy               SAVE Save

RFD  Remove from dialog

Select Action: Quit// 1-250

&gt;&gt;&gt;  Range too large: 1-250.

#### Reminder Taxonomy Action Examples

##### Add

Use this action to add a new taxonomy, following these steps:

1. At the Select Action screen, type ADD.

1. Enter the Name and Class of the new taxonomy.

Are you adding 'JGTAXONOMY1' as a new REMINDER TAXONOMY (the 148TH)? No// Y

(Yes)

REMINDER TAXONOMY CLASS: LOCAL  LOCAL

1. Once these have been entered you will be taken to the ScreenMan edit form.


1. Press Enter at the Term/Code, and a screen for selecting or editing codes opens:

#### - The top line displays the Term/Code that will be used in the search.
- Use the directional arrows  to select a coding system for the search.
    1. Press Enter at any of the code search prompts and a Lexicon search screen opens and all the matches are listed.
        - The codes are displayed in a List Manager screen. At the top, it shows you the Term/Code and the number of codes found in the selected coding system.

#### #### #### #### At this point, the following actions are available:

| Synonym   | Action               | Description                                                                                                                                        |
|-----------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| ADD       | Add to taxonomy      | Adds the selected codes to the taxonomy.                                                                                                           |
| RFT       | Remove from taxonomy | Removes the selected codes from the taxonomy.                                                                                                      |
| RFD       | Remove from dialog   | Removes UID from the selected codes.                                                                                                               |
| UID       | Use in dialog        | Marks the selected codes as Use in Dialog.                                                                                                         |
| CV        | Change View          |                                                                                                                                                    |
| EXIT      | Exit with save       |                                                                                                                                                    |
| SAVE      | Save                 | Saves the results of the other actions. You may do multiple adds, removes, etc., but nothing is actually saved until the Save action is performed. |

1. Choose the correct code (by number) or go to next screen until you see the correct code at the “Select Action:” prompt.  Multiple numbers may be added at same time
| Comma separated list of entries   | 1,3,5   |
|-----------------------------------|---------|
| Range of entries                  | 4-8     |
| Combination                       | 3,9-12  |

#### *However, please be aware of the known anomaly noted on a previous page; if you enter a range of entries that is very long, you may get a range error. If so, you should select the action first and then the list of entries.

#### When you are finished, use the hidden action Quit to return to the coding system selection form. If desired, you can use the same Term/Code for searching another coding system; just move to the next coding system and press Enter. If you want to enter another Term/Code, use either the shortcut (NL)C (close) or (NL)Q (quit) to exit the coding system selection form and return to the main taxonomy edit form.

- **Once a SAVE is done, the screen for more codes is presented.  If no more codes are needed, use the NUM LOCK+E key configuration to exit**
- **Screen now shows there are two ICD codes added**

**Completed screen Example 1:**

#### Legend: The text on the right-hand side of the screen

(CSYS:QTY|:NUID|) = Coding System and Quantity|Not used in dialog|

The coding system for diabetes is 10D and there is only one code.

- **This taxonomy now has two codes that can only be used in reminder definition or reminder term**
- **If you want to use the codes in a reminder dialog, you must use the UID option**
- **In this example, entry 29 is now allowed for use in a reminder dialog (signified by gray highlighting)**

- **The taxonomy now has two codes for use in a reminder definition and one code for use in a dialog**

**Add Taxonomy To a Dialog**

- Add Taxonomy instead of ICD/CPT code
    - Finding Item
    - Additional Finding
- Abbreviation is TX

- Use RFT option to remove codes from taxonomy
    - This will also remove codes from UID
- Use RFD to remove codes from UID only

- In the example shown, only ICD-9 diagnosis codes were used/added
- The same process holds true for:
    - ICD-10  diagnosis
    - SNOMED CT
    - CPT-4
    - HCPCS
    - ICD-10 procedure
    - ICD-9 procedure

**Add a Group of  Codes to a Taxonomy**

- Different from pre-patch 26.
- Not pertinent to SNOMED CT, as adjacent codes are usually not related.
- After entering a term or partial code to get a list of returned matches, choose ADD option, select codes 1-80.
- SAVE or EXIT.

- All 80 codes pertaining to Diabetes were added to the taxonomy
- All 80 codes were enabled to be used in dialog by choosing UID for 1-80
- SAVE or EXIT.

##### Edit

Use this action to edit the fields in a taxonomy definition.

1. Scroll through the taxonomies by pressing the Enter key. Select the Edit action and then select the # of the taxonomy to edit.

1. When you select the Edit action, a ScreenMan form opens.

#### Figure 5: Edit Action Screen

1. Edit fields, as needed. To edit some fields, such as Description, you must press Enter, and then a word-processing screen opens:

#### #### To exit the word-processing screen, press &lt;PF1&gt;E (or the key you’ve mapped).

##### Taxonomy Field Descriptions

These are the fields that you can add information to on the Taxonomy Edit screen.

| NAME                  | DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NAME                  | This is the name of the taxonomy. It must be unique. Nationally distributed taxonomies start with “VA-“.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| DESCRIPTION           | Use this word-processing field to give a complete description of the taxonomy. Topics to consider including are what it represents and its intended usage.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| PATIENT DATA SOURCE   | Specifies where to search in VistA for patient data. It is a string of comma-separated key words. The list of key words is given below.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| USE INACTIVE PROBLEMS | Applies only to searches in Problem List. Normally inactive problems are not used. However when this field is set to YES, then both active and inactive problems are used. This field works just like the field with the same name that can be specified for a reminder definition finding or a reminder term finding. If this field is defined in the taxonomy, it will take precedence over the value of the corresponding field at the term or definition level.                                                                                                                             |
| PRIORITY LIST         | This field applies only to Problem List searches. It can be used to limit the problems that are included to those with the listed priorities. The possible values are:  A - acute  C - chronic  U - undefined  Any combination of these letters can be used. For example, 'A' would  limit the search to acute problems. 'CU' would include chronic problems and those whose priority is undefined. If this field is left blank then all priorities will be included.                                                                                                                           |
| INACTIVE FLAG         | Enter "1" to inactivate the taxonomy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| TERM/CODE (multiple)  | Term/Code and a Coding System are passed to the Lexicon search utility, which returns a list of codes based on the user’s search criteria. Terms are descriptions for a concept and the code is a unique identifier assigned to that description. A concept can have one or more descriptions to express the concept. An example of this in SNOMED CT is the concept code 271807003 that has a fully specified name of "Eruption of Skin", a preferred name of "Eruption" and several synonyms "Rash", "Skin Eruption", "Skin Rash". For more information, see the Lexicon Utility User Manual. |
| CLASS                 | This is the class of the entry. Entries whose class is National cannot be edited or created by sites.  N - NATIONAL  V - VISN  L -  LOCAL                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| SPONSOR               | This is the name of a group or organization that sponsors the taxonomy  ***.***                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| REVIEW DATE           | The review date is used to determine when the entry should be reviewed to verify that it is current with the latest standards and guidelines  ***.***                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| CHANGE LOG            | If changes were made, the date and the name of the user making the changes will be inserted automatically. You can optionally type in a description of the changes made during the editing session.                                                                                                                                                                                                                                                                                                                                                                                             |

##### Patient Data Source Keywords

| KEYWORD   | MEANING                                               |
|-----------|-------------------------------------------------------|
| ALL       | All sources (default)                                 |
| EN        | All PCE encounter data (CPT-4 & ICD diagnosis)        |
| ENPP      | PCE encounter data, principal procedure (CPT-4) only  |
| ENPD      | PCE encounter data, principal diagnosis (ICD) only    |
| IN        | All PTF inpatient data (ICD diagnosis and procedures) |
| INDXLS    | PTF inpatient DXLS diagnosis (ICD) only               |
| INM       | PTF inpatient diagnosis (ICD) movement only           |
| INPD      | PTF inpatient principal diagnosis (ICD) only          |
| INPR      | PTF inpatient procedure (ICD) only                    |
| PL        | Problem List (ICD diagnosis and SNOMED-CT)            |
| RA        | Radiology (CPT-4) only                                |

You may use any combination of these keywords. An example is EN,RA. This would cause the search to be made in V CPT and Radiology for CPT-4 codes. If PATIENT DATA SOURCE is left blank, the search is made in all the possible sources. You can also use a “-” to remove a source from the list; for example, IN,-INM.

It is important to remember that the link between CPT-4 codes and radiology procedures is maintained by sites. If this linkage is not kept current at your site, then the recommendation is **to not use RA** in Patient Data Source. It will be much more reliable to use radiology procedures directly as findings.

Figure 6: Edit Action Form 2

#### When you navigate to some of the fields on the form, you may see help in the command area. If more detailed help is needed, type ‘?’ or ‘??’.

Term/Code is a multiple of terms, codes, or code fragments that are used for a Lexicon search. In the above example, the code fragment 250 has been entered. When you press Enter, you will be taken to a form where you select the coding system to search.

Figure 7: Coding System Selection Form

The top line displays the Term/Code that will be used in the search. You can scroll through the list to select a coding system for the search. When the cursor is on a coding system and you press Enter, the Term/Code and the coding system are passed to the Lexicon search engine, which returns a list of matching codes. The codes are displayed in a List Manager screen. At the top it shows you Term/Code and the number of codes found in the selected coding system.

**Adding or Editing a taxonomy from Dialog View (Dialog Elements)**

You may also edit a taxonomy from Dialog Elements/Groups edit.

- TE action
- No Lexicon search function
- Must know specific code(s) to be added
- Only UID codes can be added or deleted

- A new taxonomy can also be added
- Taxonomy will NOT be added to Finding Item or Additional Finding automatically

- **Must know specific code(s) to be added**

##### Copy

Use this action to copy an existing taxonomy definition into a new entry. Once the taxonomy has been copied, you have the option of editing it.

1. Scroll through the list of Taxonomies on your main Taxonomy screen, until you see the taxonomy you wish to copy.
2. Enter COPY at the Select Action: prompt.
3. Enter the number of the taxonomy to be copied.
4. Enter a unique name for the copied taxonomy.

Figure 8: Copying a taxonomy definition screen

1. If you choose to edit the taxonomy you’ve copied, you will enter the standard editing form. Follow the previous instructions under the Edit action.

Figure 9: Standard Editing form

#### #### Figure 10: Standard Editing form 2

#### ##### Inquire

Use this action to get the details of a single taxonomy.

1. Select the taxonomy.
2. Select Condensed or Full. The condensed displays each code on a single line with a column for code, inactive, UID, and description.
3. Can choose any taxonomy available, not just items that are viewable

NOTE: For taxonomy inquiry print to display properly in Reflections, the setup must have Save from Scrolling Regions checked. The sequence is: Setup =&gt; Display =&gt; Screen =&gt; Display Memory Advanced.

1. Select Browse or Print. You have the option of browsing the output or choosing an output device:

Browse or Print? B//

**Example:**

- Use (NL) B to navigate to the bottom to see more details.

Figure 11: Browsing Taxonomy Inquiry – Condensed

**Example 2: Taxonomy Inquiry – Full**

- Use (NL) B to navigate to bottom to see more details

Figure 12: Browsing Taxonomy Inquiry – Full


##### Change Log

Use this action to see the historical details of a taxonomy; i.e., who created, edited, or copied it, and when. You will have the option of browsing the output or choosing an output device:

Browse or Print? B//

**Example: Browsing Taxonomy Change Log**

Figure 13: Browsing Taxonomy Change Log

##### Code Search

This lets you find all taxonomies that contain a particular code. When you select this action, you are prompted to input a code from any of the supported coding systems. You only need to enter the code; the coding system will be automatically determined.

Figure 14: Selecting Code Search screen

Figure 15: Code Search Results

##### Import

The Import action provides an easy way to import lists of codes into a taxonomy.

A CSV file (Comma Separated Values) is created from a spreadsheet. The first column is equivalent to the Term/Code, the second column is the three-character coding system abbreviation for one of the supported coding systems, and the rest of the columns are the codes to be imported for the Term/Code, coding system pair. The spreadsheet can have multiple rows, a row for each Term/Code, coding system, set of codes to be imported. The final step is to create a CSV file (comma-delimited text file), using the Save As action.

**NOTE:** The National Library of Medicine (NLM), in collaboration with the Office of the National Coordinator for Health Information Technology and the Centers for Medicare &amp; Medicaid Services has created a Value Set Authority Center ( [https://vsac.nlm.nih.gov/](https://vsac.nlm.nih.gov/) ). These value sets contain lists of terms and their codes and they can be useful for creating taxonomies.

The Import action facilitates their use by allowing import of the codes into a taxonomy. To prepare the data for import, the original spreadsheet should be copied into a new spreadsheet that can be edited. The CSV file should be moved to a directory that can be accessed from the VistA account that contains the taxonomy.

**Example Spreadsheet**

Figure 16: Example Spreadsheet for Importing codes from a CSV file

When the Import action is selected, you will be prompted to select a taxonomy to import into, and after it has been selected, you have the following choices:

Figure 17: Selecting Import Method example

##### Import: CSV Host File

If the CSV file has been saved as a host file, choose the HF option. You will then be prompted for a path. This is the directory/folder that contains the CSV file and it must be accessible from your VistA session. A list of all files with a ‘.CSV’ extension in that directory will be displayed; enter the file name at the prompt, (you do not need to include the .csv extension).

**NOTE:** Special privileges are required to access host file directories, so you may not be able to use this option.

**Example: Importing codes from a CSV host file**

Figure 17: Example for Importing codes from a CSV host file

At this point you will have the option of browsing the list of codes.

Figure 17a: Example for Importing codes from a CSV host file

Figure 17b: Example: Browsing list of codes screen

Figure 17c: Taxonomy Inquire example

If you are satisfied, then when the Browser is exited, respond yes to this prompt:

**Do you want to save the imported codes? Y//**

If there are problems with any of the codes, error messages will be displayed.

When the codes are imported into the taxonomy, each Term/Code will have “(imported)” appended to it so that you will know the codes were imported.

##### Import: CSV Paste

Another way to import a CSV file is the PA option. When you use this option, you open the CSV file on your workstation and copy it.

1. Create an Excel Spreadsheet. The first column of the new spreadsheet is equivalent to the Term/Code, the second column is the three-character coding system abbreviation for one of the supported coding systems, and the rest of the columns are the codes to be imported for the Term/Code, coding system pair. The spreadsheet can have multiple rows, a row for each Term/Code, coding system, set of codes to be imported. The final step is to create a CSV file (comma-delimited text file), using the Save As action.

Figure 18: Excel Spreadsheet with codes

1. Save the imported files as a CSV.
2. Open the CSV file, as a text file, using a text editor such as Notepad or Microsoft Word. (Select All Files in the Files of type box.)

Figure 19: Opening spreadsheet as a text file

1. Open the desired csv file, and copy the contents so they are ready for pasting.

1. In Taxonomy Management, select the action IMP and press enter.
2. At the prompt, enter the number of the Taxonomy that the import file will be imported to.

Figure 20: Entering the number of the Taxonomy that the import file will be imported to

1. Select PA for the import method.

Figure 21: Select PA as the import method

1. At the 'Paste the CSV file now prompt, click on Paste from the file menu (or select the Paste icon) and press &lt;enter&gt; to finish.

Figure 22: Pasting the CSV file

1. Next you will be given the opportunity to browse the list of codes that will be imported. If you are satisfied with the list, respond ‘Y’ to the following prompt to import the codes:

Figure 23: Browsing the list of codes that were pasted

1. After browsing, you’ll be asked if you want to save the codes.

**Do you want to save the imported codes? Y//**

1. You can also do an inquiry on the taxonomy you imported the codes into, to verify that these have been entered.

**+         + Next Screen   - Prev Screen   ?? More Actions**

**ADD  Add                                CS   Code Search**

**EDIT Edit                               IMP  Import**

**COPY Copy                               UIDR UID report**

**INQ  Inquire                            OINQ Old Inquire**

**CL   Change Log**

**Select Action: Next Screen// inq   Inquire**

**Display inquiry for which taxonomy?:  (1-254): 105**

.

Figure 24: Taxonomy Inquiry of codes that were pastedImport – TAX

If you choose the TAX option then you will be presented with a list of all the taxonomies on the system and you can create a list of taxonomies to import codes from.

1. Select Import and then select TAX.

Figure 25: Using the TAX option to import a taxonomy from another taxonomy

1. Select the Taxonomy you wish to copy.

Figure 26: Selecting another taxonomy to import from

The SEL action adds a taxonomy to the list and the REM action removes it from the list.

1. Once the list is built use the DONE action. You will then see the following prompt for each selected taxonomy:

**Ready to import codes from taxonomy (taxonomy name here)**

**Select one of the following:**

**ALL       All codes**

**SEL       Selected codes**

**Enter response: ALL//**

ALL will import all the codes and SEL will walk you through each Term/Coding System combination in the taxonomy and allow you to choose whether or not to import it.

1. At this point you will have the option of browsing the list of codes.

Figure 27: Browsing list of codes screen

1. If you are satisfied, then when the Browser is exited, respond yes to the prompt

“Do you want to save the imported codes?”

If there are problems with any of the codes, error messages will be displayed.

When the codes are imported into the taxonomy, each Term/Code will have “(imported)” appended to it so that you will know the codes were imported.

#### ##### WEB: Importing a CSV file from a web site

Some sites may find it useful to store their CSV files on a web location. If so, you can use the Import/Web action to import the file.

1. Select Import and then WEB.
2. Enter the url.

Figure 28: Importing a taxonomy from a web site

Hint - If you have the url copied to the clipboard you can paste it at the Input prompt.

1. The codes are imported. Messages about Invalid coding system pair indicate…..

Figure 29: Starting the import process

1. If you choose to browse the list of codes, you’ll see the codes that are imported for different coding systems:

Figure 30: Browsing the list of codes imported from a website

##### Use in Dialog Report

The Use in Dialog Report searches all taxonomies for inactive codes that are marked as Use in Dialog. If any of these are found, the Browser will display the taxonomies and information about the inactive code(s) they contain.

1. Select UID for Use in Dialog Report from the Lexicon Selection screen:


Figure 31: Browsing Use in Dialog Report

## 8 Using Reminder Dialogs Taxonomy Features

### Background – Before and After

***Before PXRM*2*26*** , users created Reminder Dialogs by adding individual ICD-9-CM and/or CPT-4 codes. When using codes as Finding Items or Additional Finding Items in CPRS, the end user didn’t select codes; codes were automatically filed to VistA when the element/group was selected in the Reminder Dialog. If the Reminder Dialog was set up to use a Taxonomy, it could only be used as a Finding Item; it created a pick list of codes for the user to pick from in CPRS.

The display in CPRS was controlled by the set-up in the Reminder Finding Parameter File (#801.45) and the Reminder Taxonomy File (#811.2). These controls determined if the Taxonomy should assign codes to the current encounter or an historical encounter and what prompts should be assigned to the Reminder Dialog in CPRS.

***After PXRM*2*26*** , users will no longer be able to add ICD-9-CM and/or CPT-4 codes to a Reminder Dialog. Users will need to create a Taxonomy, assign codes, and then add the Taxonomy to the Reminder Dialog. To maintain similar end user functionality in CPRS, a new prompt called Taxonomy Pick List Display has been added to the dialog editor. This controls how Taxonomies should display in CPRS.

### Dialog Taxonomy Editor

A simple taxonomy editor is available. It is accessed from dialog management (either the element or group view). Codes added in this editor are automatically marked as Use In Dialog. If a code is deleted in this editor, the Use In Dialog designation is removed from the code.


**Dialog List** Aug 08, 2013@12:07:04          Page:    1 of   15

REMINDER VIEW (ALL REMINDERS BY NAME)

Item Reminder Name                      Linked Dialog Name &amp; Dialog Status

1  14HTN (TESTING)

2  15 REMINDER DIALOG TESTS           15 TESTING DIALOG

3  15V-DIABETES TX TEST

4  AJM TAXONOMY                       AJM TAXONOMY

5  ARD 00 ANTICOAGULATION AFIB

**+         Enter ?? for more actions                                         &gt;&gt;&gt;**

AR   All reminders        LR   Linked Reminders     QU   Quit

CV   Change View          RN   Name/Print Name

Select Item: Next Screen// cv   Change View

Select one of the following:

D         Reminder Dialogs

E         Dialog Elements

F         Forced Values

G         Dialog Groups

P         Additional Prompts

R         Reminders

RG        Result Group (Mental Health)

RE        Result Element (Mental Health)

TYPE OF VIEW: R// e  Dialog Elements


**Select Item: Next Screen// te   Dialog Taxonomy Edit**

**Select REMINDER TAXONOMY NAME: 1**

**1   10 EG CPT ONLY       LOCAL**

**2   10 EG ICD10 AND CPT       LOCAL**

**3   10 EG ICD10 ONLY       LOCAL**

**4   10 EG ICD9 AND CPT       LOCAL**

**5   10 EG ICD9 ONLY       LOCAL**

**Press &lt;RETURN&gt; to see more, '^' to exit this list, OR**

**CHOOSE 1-5: 2  10 EG ICD10 AND CPT     LOCAL**

### ### New Fields

***Taxonomy Pick List Display*** - This field controls if and what pick lists should appear in CPRS. The possible values for the option are based on the setup of the Taxonomy in the Finding Item Field. If a pick list is set to not display, then the active codes marked to be used in a dialog will automatically be filed to PCE for the encounter date for that element when the finish button is clicked. Taxonomies that contain more than one ICD and/or CPT codes

These pick lists are only relevant for the Finding Type field (not Additional Findings field)

- Four choices for display of ‘pick list’
- **CPT ONLY** – Displays ‘pick list’ for CPT only.  All ICD codes in taxonomy are entered into PCE
- **NONE** – No ‘pick list’ for either ICD or CPT.  All codes in taxonomy are entered into PCE
- Have to have a choice selected

***Diagnosis Header*** = This field displays text that will be used for the Taxonomy Checkbox. The prompt is only available if the Taxonomy Selection Value is set to All. The default value is from the Reminder Finding Type Parameter.

***Procedure Header*** = This field displays text that will be used for the Taxonomy Checkbox. The prompt is only available if the Taxonomy Selection Value is set to All.. The default value is from the Reminder Finding Type Parameter.

**Also, after PXRM*2.0*26, users will no longer be able to set one Taxonomy Element to prompt for both Current  and Historical Encounter Data. Users will need to create an element for each encounter type, Current and Historical.  If the element Resolution Type is set to Done Elsewhere, then the editor will prompt the user to accept the default prompts for the taxonomy which includes prompts for historical data.  prompt for historical data. Any other resolution type or no resolution type will prompt data for the current encounter date.**

For the ICD-10 implementation, Reminder Dialogs will display ICD-9-CM or ICD-10-CM in a pick list based on the code set versioning rules. Reminder Dialogs determine what codes to display using the following rules:

- Current encounters= active codes for that encounter date; Addendums will use the parent note Encounter date.
- Historical encounters= active codes for system date

### Examples

A demo Taxonomy that is a copy of VA-ADB AORTIC; this demo has additional codes set to be used in a dialog.

-----------------------------------------------------------------------------

AAA TAX DEMO                                                         No. 115

-----------------------------------------------------------------------------

Class: LOCAL

Sponsor:

Review Date:

Description:

ICD codes and CPT codes indicating AAA

Inactive Flag:

Patient Data Source:

Use Inactive Problems:

Selected Codes:

**Lexicon Search Term/Code: Abdominal aortic aneurysm**

Coding System: ICD-10-CM

Code       Activation Inactivation  UID  Description

---------  ---------- ------------  ---  -----------

I71.3      01/01/2012                X   Abdominal Aortic Aneurysm, Ruptured

I71.4      01/01/2012                X   Abdominal Aortic Aneurysm, without

Rupture

**Lexicon Search Term/Code: Copy from CPT range 34800 to 34805**

Coding System: CPT-4

Code       Activation Inactivation  UID  Description

---------  ---------- ------------  ---  -----------

34800      01/01/2001                X   Endovascular Repair of Infrarenal

Abdominal Aortic Aneurysm or

Dissection; using Aorto-Aortic

Tube Prosthesis

34802      01/01/2001                X   Endovascular Repair of Infrarenal

Abdominal Aortic Aneurysm or

Dissection; using Modular

Bifurcated Prosthesis (one Docking

Limb)

34803      01/01/2005                X   Endovascular Repair of Infrarenal

Abdominal Aortic Aneurysm or

Dissection; using Modular

Bifurcated Prosthesis (two Docking

Limbs)

34804      01/01/2001                X   Endovascular Repair of Infrarenal

Abdominal Aortic Aneurysm or

Dissection; using Unibody

Bifurcated Prosthesis

34805      01/01/2004                X   Endovascular Repair of Infrarenal

Abdominal Aortic Aneurysm or

Dissection; using Aorto-Uniiliac

or Aorto-Unifemoral Prosthesis

**Lexicon Search Term/Code: Copy from CPT range 34825 to 34832**

Coding System: CPT-4

Code       Activation Inactivation  UID  Description

---------  ---------- ------------  ---  -----------

34825      01/01/1989  01/01/1990        Placement of Proximal or Distal

Extension Prosthesis for

Endovascular Repair of Infrarenal

Abdominal Aortic Aneurysm; Initial

Vessel

01/01/2001                    Placement of Proximal or Distal

Extension Prosthesis for

Endovascular Repair of Infrarenal

Abdominal Aortic or Iliac

Aneurysm, False Aneurysm, or

Dissection; Initial Vessel

34826      01/01/1989  01/01/1990        Placement of Proximal or Distal

Extension Prosthesis for

Endovascular Repair of Infrarenal

Abdominal Aortic Aneurysm; each

additional Vessel

01/01/2001                    Placement of Proximal or Distal

Extension Prosthesis for

Endovascular Repair of Infrarenal

Abdominal Aortic or Iliac

Aneurysm, False Aneurysm, or

Dissection; each additional Vessel

(List Separately in addition to

Code for Primary Procedure)

34830      01/01/2001                    Open Repair of Infrarenal Aortic

Aneurysm or Dissection, plus

Repair of Associated Arterial

Trauma, Following Unsuccessful

Endovascular Repair; Tube

Prosthesis

34831      01/01/2001                    Open Repair of Infrarenal Aortic

Aneurysm or Dissection, plus

Repair of Associated Arterial

Trauma, Following Unsuccessful

Endovascular Repair;

Aorto-Bi-Iliac Prosthesis

34832      01/01/2001                    Open Repair of Infrarenal Aortic

Aneurysm or Dissection, plus

Repair of Associated Arterial

Trauma, Following Unsuccessful

Endovascular Repair;

Aorto-Bifemoral Prosthesis

**Lexicon Search Term/Code: Copy from CPT range 35081 to 35103**

Coding System: CPT-4

Code       Activation Inactivation  UID  Description

---------  ---------- ------------  ---  -----------

35081      06/01/1994                    Direct Repair of Aneurysm,

Pseudoaneurysm, or Excision

(Partial or Total) and Graft

Insertion, with or without Patch

Graft; for Aneurysm and Associated

Occlusive Disease, Abdominal Aorta

35082      06/01/1994                    Direct Repair for Ruptured

Aneurysm involving the Abdominal

Aorta

35091      06/01/1994                    Direct Repair of Aneurysm,

Pseudoaneurysm, or Excision

(Partial or Total) and Graft

Insertion, with/without Patch

Graft; for Aneurysm and Associated

Occlusive Disease, Abdominal Aorta

involving Visceral Vessels

(Mesenteric, Celiac, Renal)

35092      06/01/1994                    Direct Repair for Ruptured

Aneurysm involving the Mesenteric,

Celiac or Renal Arterial Branch of

the Abdominal Aorta

35102      06/01/1994                    Direct Repair of Aneurysm,

Pseudoaneurysm, or Excision

(Partial or Total) and Graft

Insertion, with/without Patch

Graft; for Aneurysm and Associated

Occlusive Disease, Abdominal Aorta

involving Iliac Vessels (Common,

Hypogastric, External)

35103      06/01/1994                    Direct Repair for Ruptured

Aneurysm involving the Iliac

Vessels (Common, Hypogastric,

External) of the Abdominal Aorta

**Lexicon Search Term/Code: Copy from CPT range 75952 to 75953**

Coding System: CPT-4

Code       Activation Inactivation  UID  Description

---------  ---------- ------------  ---  -----------

75952      01/01/2001                    Endovascular Repair of Infrarenal

Abdominal Aortic Aneurysm or

Dissection, Radiological

Supervision and Interpretation

75953      01/01/1989  01/01/1990        Placement of Proximal or Distal

Extension Prosthesis for

Endovascular Repair of Infrarenal

Abdominal Aortic Aneurysm,

Radiological Supervision and

Interpretation

01/01/2001                    Placement of Proximal or Distal

Extension Prosthesis for

Endovascular Repair of Infrarenal

Aortic or Iliac Artery Aneurysm,

Pseudoaneurysm, or Dissection,

Radiological Supervision and

Interpretation

**Lexicon Search Term/Code: Copy from ICD range 441.3 to 441.4**

Coding System: ICD-9-CM

Code       Activation Inactivation  UID  Description

---------  ---------- ------------  ---  -----------

441.3      10/01/1978  01/01/2012    X   Abdominal aneurysm, ruptured

441.4      10/01/1978  01/01/2012    X   Abdominal aneurysm without mention

of rupture

This taxonomy includes the following numbers of codes:

ICD-10-CM: 2

CPT-4: 18

ICD-9-CM: 2

Total number of codes: 22

Below are screen shots of how CPRS will display the taxonomy using different values.

**Example 1**

**Setting a Taxonomy as a finding item to display pick lists for both I10 and CPT codes, for current encounters only.**

NAME: AAA DEMO ELEMENT//

DISABLE:

CLASS: L  LOCAL

SPONSOR:

REVIEW DATE:

RESOLUTION TYPE:

ORDERABLE ITEM:

FINDING ITEM: TX.AAA TAX DEMO     LOCAL

...OK? Yes//   (Yes)

Additional findings: none

Select ADDITIONAL FINDING:

Select one of the following:

A         All

D         ICD Diagnoses Only

P         CPT Procedures Only

N         None

Taxonomy Pick List: A// ll

Diagnosis Header: Diagnosis recorded at encounter.  Replace

Procedure Header: done.//

Default prompts for the taxonomy:

Prompt: PXRM COMMENT

Prompt: PXRM PRIMARY DIAGNOSIS

Prompt: PXRM QUANTITY

Prompt: PXRM ADD TO PROBLEM LIST

Select one of the following:

Y         Yes

N         No

Add Prompts to the dialog: Yes//

DIALOG/PROGRESS NOTE TEXT:

No existing text

Edit? NO// YES

==[ WRAP ]==[ INSERT ]======&lt; DIALOG/PROGRESS NOTE TEXT &gt;====[ &lt;PF1&gt;H=Help ]

This taxonomy contains both diagnosis and procedure codes. The dialog is

set to display a pick list for both sets of codes. This dialog is set to

file the codes to the current encounter.

&lt;=======T=======T=======T=======T=======T=======T=======T=======T=======T&gt;===

ALTERNATE PROGRESS NOTE TEXT:

No existing text

Edit? NO//

EXCLUDE FROM PROGRESS NOTE:

SUPPRESS CHECKBOX:

Select SEQUENCE: 4//

SEQUENCE: 4//

ADDITIONAL PROMPT/FORCED VALUE: PXRM ADD TO PROBLEM LIST

//

OVERRIDE PROMPT CAPTION:

START NEW LINE:

EXCLUDE FROM PN TEXT:

REQUIRED:

Select SEQUENCE:

REMINDER TERM:

Input your edit comments.

Edit? NO//

Select DIALOG to add:  Select the correct AAA codes.

With these settings, the user is able to pick from a pick list of diagnoses and procedure codes to add to the current encounter.

**Example 2**

**Setting a Taxonomy as a finding item to display pick lists for both I10 and CPT codes for historical encounters only.**

NAME: AAA DEMO ELEMENT//

DISABLE:

CLASS: ??

Enter the class.

Choose from:

N        NATIONAL

V        VISN

L        LOCAL

CLASS: L  LOCAL

SPONSOR:

REVIEW DATE:

RESOLUTION TYPE:    DONE ELSEWHERE (HISTORICAL)

...OK? Yes//   (Yes)

ORDERABLE ITEM:

FINDING ITEM: AAA DEMO

Additional findings: none

Select ADDITIONAL FINDING:

Select one of the following:

A         All

D         ICD Diagnoses Only

P         CPT Procedures Only

N         None

Taxonomy Pick List: A// ll

Diagnosis Header: History of Diagnosis.  Replace

Procedure Header: previously done.//

Default prompts for the taxonomy:

Prompt: PXRM COMMENT

Prompt: PXRM VISIT DATE

Required: Yes

Prompt: PXRM OUTSIDE LOCATION

Prompt: PXRM PRIMARY DIAGNOSIS

Prompt: PXRM QUANTITY

Prompt: PXRM ADD TO PROBLEM LIST

Select one of the following:

Y         Yes

N         No

Add Prompts to the dialog: Yes//

DIALOG/PROGRESS NOTE TEXT:

No existing text

ALTERNATE PROGRESS NOTE TEXT:

No existing text

Edit? NO//

EXCLUDE FROM PROGRESS NOTE:

SUPPRESS CHECKBOX:

Select SEQUENCE: 6//

SEQUENCE: 6//

ADDITIONAL PROMPT/FORCED VALUE: PXRM ADD TO PROBLEM LIST

//

OVERRIDE PROMPT CAPTION:

START NEW LINE:

EXCLUDE FROM PN TEXT:

REQUIRED:

Select SEQUENCE:

REMINDER TERM:

Input your edit comments.

Edit? NO//

With these settings, the user is able to assign diagnosis and/or procedure codes to a historical encounter. The historical date will be created based on the Date prompt for both the diagnosis and the procedure checkboxes.

**Example 4**

**Setting a Taxonomy as a finding item to display pick lists for only diagnosis codes for the current encounters.**

NAME: AAA DEMO ELEMENT//

DISABLE:

CLASS: L  LOCAL

SPONSOR:

REVIEW DATE:

RESOLUTION TYPE:

ORDERABLE ITEM:

FINDING ITEM: TX.AAA TAX DEMO     LOCAL

...OK? Yes//   (Yes)

Additional findings: none

Select ADDITIONAL FINDING:

Select one of the following:

A         All

D         ICD Diagnoses Only

P         CPT Procedures Only

N         None

Taxonomy Pick List: A// D  ICD Diagnoses Only

Diagnosis Header: Diagnosis recorded at encounter.  Replace

Default prompts for the taxonomy:

Prompt: PXRM COMMENT

Prompt: PXRM PRIMARY DIAGNOSIS

Prompt: PXRM QUANTITY

Prompt: PXRM ADD TO PROBLEM LIST

Select one of the following:

Y         Yes

N         No

Add Prompts to the dialog: Yes//

DIALOG/PROGRESS NOTE TEXT:

No existing text

Edit? NO// YES

==[ WRAP ]==[ INSERT ]======&lt; DIALOG/PROGRESS NOTE TEXT &gt;====[ &lt;PF1&gt;H=Help ]

This taxonomy contains both diagnosis and procedure codes. The dialog is

set to only display a pick list for diagnosis codes. The dialog is set to

file the codes to the current encounter.

&lt;=======T=======T=======T=======T=======T=======T=======T=======T=======T&gt;===

ALTERNATE PROGRESS NOTE TEXT:

No existing text

Edit? NO//

EXCLUDE FROM PROGRESS NOTE:

SUPPRESS CHECKBOX:

Select SEQUENCE: 4//

SEQUENCE: 4//

ADDITIONAL PROMPT/FORCED VALUE: PXRM ADD TO PROBLEM LIST

//

OVERRIDE PROMPT CAPTION:

START NEW LINE:

EXCLUDE FROM PN TEXT:

REQUIRED:

Select SEQUENCE:

REMINDER TERM:

Input your edit comments.

Edit? NO//

With these settings, the user will be able to pick diagnosis codes to add to the current encounter. The active procedure codes that were marked to be used in a dialog will automatically be filed to the current encounter. No historical data will be stored for this element. **Notice there was not a need to add a Diagnosis Header for this scenario.**

**Example 5**

**Setting a Taxonomy as a finding item to display pick lists for CPT codes only for the current encounters.**

NAME: AAA DEMO ELEMENT//

DISABLE:

CLASS: L  LOCAL

SPONSOR:

REVIEW DATE:

RESOLUTION TYPE:

ORDERABLE ITEM:

FINDING ITEM: TX.AAA TAX DEMO     LOCAL

...OK? Yes//   (Yes)

Additional findings: none

Select ADDITIONAL FINDING:

Select one of the following:

A         All

D         ICD Diagnoses Only

P         CPT Procedures Only

N         None

Taxonomy Pick List: A// P  CPT Procedures Only

Procedure Header: done.//

Default prompts for the taxonomy:

Prompt: PXRM COMMENT

Prompt: PXRM QUANTITY

Select one of the following:

Y         Yes

N         No

Add Prompts to the dialog: Yes//

DIALOG/PROGRESS NOTE TEXT:

No existing text

Edit? NO// YES

==[ WRAP ]==[ INSERT ]======&lt; DIALOG/PROGRESS NOTE TEXT &gt;====[ &lt;PF1&gt;H=Help ]

This taxonomy contains both diagnosis and procedure codes. The dialog is

set to only display a pick list for procedure codes. The dialog is set to

filed the codes to the current encounter.

&lt;=======T=======T=======T=======T=======T=======T=======T=======T=======T&gt;===

ALTERNATE PROGRESS NOTE TEXT:

No existing text

Edit? NO//

EXCLUDE FROM PROGRESS NOTE:

SUPPRESS CHECKBOX:

Select SEQUENCE: 2//

SEQUENCE: 2//

ADDITIONAL PROMPT/FORCED VALUE: PXRM QUANTITY//

OVERRIDE PROMPT CAPTION:

START NEW LINE:

EXCLUDE FROM PN TEXT:

REQUIRED:

Select SEQUENCE:

REMINDER TERM:

Input your edit comments.

Edit? NO//

With these settings, the user will be able to pick the Procedure codes to assign to the current encounter. The active diagnosis codes marked to be used in the dialog will automatically be assigned to the encounter. No historical data will be stored for this element. **Notice there was not a need to add a Diagnosis Header for this scenario.**

**Example 6**

**Setting a Taxonomy as a finding item to display no pick list set to display.**

NAME: AAA DEMO ELEMENT//

DISABLE:

CLASS: L  LOCAL

SPONSOR:

REVIEW DATE:

RESOLUTION TYPE:

ORDERABLE ITEM:

FINDING ITEM: TX.AAA TAX DEMO     LOCAL

...OK? Yes//   (Yes)

Additional findings: none

Select ADDITIONAL FINDING:

Select one of the following:

A         All

D         ICD Diagnoses Only

P         CPT Procedures Only

N         None

Taxonomy Pick List: A// None

DIALOG/PROGRESS NOTE TEXT:

No existing text

Edit? NO// YES

==[ WRAP ]==[ INSERT ]======&lt; DIALOG/PROGRESS NOTE TEXT &gt;====[ &lt;PF1&gt;H=Help ]=

This taxonomy contains both diagnosis and procedure codes. The dialog is

set to not display a pick list. This dialog is set to file codes to the

current encounter.

&lt;=======T=======T=======T=======T=======T=======T=======T=======T=======T&gt;===

ALTERNATE PROGRESS NOTE TEXT:

No existing text

Edit? NO//

EXCLUDE FROM PROGRESS NOTE:

SUPPRESS CHECKBOX:

Select SEQUENCE: 1

ADDITIONAL PROMPT/FORCED VALUE: PXRM PRIMARY DIAGNOSIS       prompt     NATIOL

...OK? Yes//   (Yes)

OVERRIDE PROMPT CAPTION:

START NEW LINE:

EXCLUDE FROM PN TEXT:

REQUIRED:

Select SEQUENCE: 5

ADDITIONAL PROMPT/FORCED VALUE: PXRM ADD TO PROBLEM LIST     prompt     NATIONAL

OVERRIDE PROMPT CAPTION:

START NEW LINE:

EXCLUDE FROM PN TEXT:

REQUIRED:

Select SEQUENCE: 10

ADDITIONAL PROMPT/FORCED VALUE: PXRM QUANTITY       prompt     NATIONAL

...OK? Yes//   (Yes)

OVERRIDE PROMPT CAPTION:

START NEW LINE:

EXCLUDE FROM PN TEXT:

REQUIRED:

Select SEQUENCE: 15

ADDITIONAL PROMPT/FORCED VALUE: PXRM COMMENT       prompt     NATIONAL

OVERRIDE PROMPT CAPTION:

START NEW LINE:

EXCLUDE FROM PN TEXT:

REQUIRED:

Select SEQUENCE: REMINDER TERM:

Input your edit comments.

Edit? NO//

With this setting, all active diagnosis/procedure codes marked to be used in a dialog will automatically be filed to the current encounter.

To set any of the above to filed data for an historical encounter date. The Resolution Type field must be set to Done Elsewhere (Historical)

NAME: TAX NEW STRUCTURE ALL HISTORICAL  Replace

DISABLE:

CLASS: L  LOCAL

SPONSOR:

REVIEW DATE:

RESOLUTION TYPE:    DONE ELSEWHERE (HISTORICAL)

...OK? Yes//   (Yes)

ORDERABLE ITEM:

FINDING ITEM:  AAA TAX DEMO     LOCAL

Additional findings: none

Select ADDITIONAL FINDING:

Select one of the following:

A         All

D         ICD Diagnoses Only

P         CPT Procedures Only

N         None

Taxonomy Pick List: A// ll

Diagnosis Header: History of Diagnosis.  Replace

Procedure Header: previously done.//

Default prompts for the taxonomy:

Prompt: PXRM COMMENT

Prompt: PXRM VISIT DATE

Required: Yes

Prompt: PXRM OUTSIDE LOCATION

Prompt: PXRM PRIMARY DIAGNOSIS

Prompt: PXRM QUANTITY

Prompt: PXRM ADD TO PROBLEM LIST

Select one of the following:

Y         Yes

N         No

Add Prompts to the dialog: Yes//

DIALOG/PROGRESS NOTE TEXT:

No existing text

ALTERNATE PROGRESS NOTE TEXT:

No existing text

Edit? NO//

EXCLUDE FROM PROGRESS NOTE:

SUPPRESS CHECKBOX:

Select SEQUENCE: 6//

SEQUENCE: 6//

ADDITIONAL PROMPT/FORCED VALUE: PXRM ADD TO PROBLEM LIST

//

OVERRIDE PROMPT CAPTION:

START NEW LINE:

EXCLUDE FROM PN TEXT:

REQUIRED:

Select SEQUENCE:

REMINDER TERM:

Input your edit comments.

Edit? NO//

## 11 Glossary/Acronyms

The OIT Master Glossary is available at [http://vaww.oed.wss.va.gov/process/Library/master\_glossary/masterglossary.htm](http://vaww.oed.wss.va.gov/process/Library/master_glossary/masterglossary.htm)

National Acronym Directory:

[http://vaww1.va.gov/Acronyms/](http://vaww1.va.gov/Acronyms/)


| **Term**   | **Definition**                                                                                                           |
|------------|--------------------------------------------------------------------------------------------------------------------------|
| AAPC       | American Academy of Professional Coders                                                                                  |
| ADPAC      | Automated Data Processing Application Coordinator                                                                        |
| AHA        | American Hospital Association                                                                                            |
| AHIMA      | American Health Information Management Association                                                                       |
| AIS        | Automated Information Systems                                                                                            |
| AMA        | American Medical Association                                                                                             |
| AMI        | Acute Myocardial Infarction                                                                                              |
| AR         | Accounts Receivable                                                                                                      |
| ARC        | Allocation Resource Center                                                                                               |
| CAC        | Clinical Application Coordinator                                                                                         |
| CBO        | VHA Chief Business Office                                                                                                |
| CDC        | Centers for Disease Control and Prevention                                                                               |
| CFR        | Code of Federal Regulations                                                                                              |
| CMO        | VHA Chief Medical Officer                                                                                                |
| CMS        | Centers for Medicare and Medicaid Services                                                                               |
| COTS       | Commercial Off-The-Shelf Products                                                                                        |
| CPAC       | Consolidated Patient Account Center                                                                                      |
| CPRS       | Computerized Patient Record System                                                                                       |
| CPT        | Current Procedural Terminology                                                                                           |
| DoD        | US Department of Defense                                                                                                 |
| DRG        | Diagnosis Related Groups                                                                                                 |
| DSS        | Decision Support Services                                                                                                |
| EES        | VA/VHA Employee Education System                                                                                         |
| HER        | Electronic Health Record                                                                                                 |
| EKG        | Electrocardiogram                                                                                                        |
| ESM        | VHA Enterprise Systems Management Office                                                                                 |
| FSC        | VHA Financial Services Center                                                                                            |
| HAC        | VHA Health Administration Center                                                                                         |
| HCPCS      | Healthcare Common Procedure Coding System                                                                                |
| HHS        | US Department of Health and Human Services                                                                               |
| HIM        | VHA Office of Health Information Management                                                                              |
| HIMSS      | Healthcare Information and Management Systems                                                                            |
| HIPAA      | Health Insurance Portability and Accountability Act of 1996                                                              |
| ICD:       | International Classification of Diseases                                                                                 |
| ICD-9-CM   | or ICD-9: International Classification of Diseases, 9  th  Revision (Edition) Clinical Modification (includes PCS codes) |
| ICD-10     | International Classification of Diseases, 10  th  Revision (Edition) – used when pertaining to both ICD-10 code sets     |
| ICD-10-CM  | International Classification of Diseases, 10  th  Revision (Edition) Clinical Modification                               |
| ICD-10-PCS | International Classification of Diseases, 10  th  Revision (Edition) Procedure Coding System                             |
| IDMC       | Informatics and Data Management Committee                                                                                |
| HIS        | Indian Health Services                                                                                                   |
| IRM        | Information Resources Management                                                                                         |
| IT         | Information Technology                                                                                                   |
| NCHICA     | North Carolina Healthcare Information and Communications Alliance                                                        |
| NCHS       | National Center for Health Statistics                                                                                    |
| NLM        | National Library of Medicine                                                                                             |
| NLC        | VHA National Leadership Council                                                                                          |
| NPCD       | National Patient Care Database                                                                                           |
| OHI        | VA Office of Health Information                                                                                          |
| OIT        | Office of Information and Technology                                                                                     |
| ONS:       | VHA Office of Nursing Services                                                                                           |
| PAS        | Program Application Specialist                                                                                           |
| PCE        | Patient Care Encounter                                                                                                   |
| PCS        | VHA Office of Patient Care Services                                                                                      |
| PD         | Product Development                                                                                                      |
| PMO        | Project Management Office                                                                                                |
| PXRM       | Clinical Reminders namespace                                                                                             |
| SARS       | Severe Acute Respiratory Syndrome                                                                                        |
| SDE        | VA Service Delivery and Engineering                                                                                      |
| SNOMED CT  | Systematized Nomenclature of Medicine - Clinical Terms                                                                   |
| UR         | Utilization Review                                                                                                       |
| VA         | U.S. Department of Veterans Affairs                                                                                      |
| VAMC       | Veterans Affairs Medical Center                                                                                          |
| VERA       | Veterans Equitable Resource Allocation                                                                                   |
| VHA        | Veterans Health Administration                                                                                           |
| VISN       | Veterans Integrated Service Network                                                                                      |
| VistA      | Veterans Health Information System and Technology Architecture                                                           |
| WEDI       | Workgroup for Electronic Data Interchange                                                                                |
| WHO        | World Health Organization                                                                                                |

## 13 Appendix A – ScreenMan and Browser Overviews

##### ScreenMan Overview

The redesigned Reminder Taxonomy Management functionality uses ScreenMan. ScreenMan is VA FileMan's *screen-oriented* data entry tool. It is an alternative to the Scrolling Mode approach. With ScreenMan, data is entered in *forms* . Each form field occupies a fixed position on the screen (instead of scrolling off). You can see many data fields at once, and use simple key combinations to edit data and move from field to field on a screen. You can also move from one screen to another like turning through the pages of a book. ***For a detailed explanation of using ScreenMan, please refer to the VW FileMan Getting Started manual.***

Figure 36: ScreenMan Screen

**ScreenMan Descriptions**

Required fields are underlined

Current field – reverse video

NAME : TAXONOMY1

DESCRIPTION:

PATIENT DATA SOURCE **:**

USE INACTIVE PROBLEMS         PRIORITY LIST:

Term/Code:                       Selected Codes:

250

CLASS : **LOCAL**

SPONSOR:

REVIEW DATE:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND:                                      Press &lt;PF1&gt;H for help    Insert

Initial Multiple field

Fields are usually composed of a *data element* and a *caption* . ScreenMan displays data elements in high intensity (boldface) and other text in regular intensity. Text that identifies a data element is called a *caption* and is usually followed by a colon ( **:** ). A caption and its associated data element are together called a *field* . Captions of *required* fields are underlined; to save any changes you make on the form, required fields *must* contain data.

**How to Navigate Between Fields and Pages**

There are a number of ways you can move the cursor from field to field on a form (i.e., navigate). This is to provide you with as much flexibility as possible so that you can work quickly and efficiently with forms.

You can use the keystrokes listed in the following table to move the cursor to various fields located on a ScreenMan form:

| **To**                                                   | **Press**                                                  |
|----------------------------------------------------------|------------------------------------------------------------|
| Move to the next field (to right or below).              | **&lt;Tab&gt;**                                            |
| Move to the previous field (to left or above).           | **&lt;PF4&gt;**                                            |
| Move to the field above.                                 | **&lt;ArrowUp&gt;**                                        |
| Move to the field below.                                 | **&lt;ArrowDown&gt;**                                      |
| Move to the next field in the pre-defined edit sequence. | **&lt;Enter&gt;**                                          |
| Edit a WORD-PROCESSING field.                            | At field, press  **&lt;Enter&gt;**                         |
| Select a Subrecord in a Multiple.                        | At field, press  **&lt;Enter&gt;**                         |
| Move to the next block on current page.                  | **&lt;PF1&gt;&lt;PF4&gt;**                                 |
| Jump to a specific field.                                | **^**  followed by Caption of field and  **&lt;Enter&gt;** |
| Jump to the Command Line.                                | **^&lt;Enter&gt;**                                         |
| Move to next page                                        | **&lt;PF1&gt;&lt;ArrowDown&gt;**  or  **&lt;PageDown&gt;** |
| Move to previous page                                    | **&lt;PF1&gt;&lt;ArrowUp&gt;**  or  **&lt;PageUp&gt;**     |
| Move to a page you specify                               | **&lt;PF1&gt;P**                                           |

**Saving and Exiting**

To SAVE or EXIT the form, you need to reach ScreenMan's command line. It's reachable from any ScreenMan screen. To reach the command line, do any one of the following:

Enter a caret ("^") at any field prompt.

Press **&lt;Enter&gt;** , **&lt;Tab&gt;** , or **&lt;PF4&gt;** to move from field to field until you reach the command line.

Press **&lt;ArrowDown&gt;** or **&lt;ArrowUp&gt;** to move the cursor from field to field downwards or upwards, until you reach the command line.

Then you can enter SAVE or EXIT at the command line (see below).

**Word-Processing Fields**

To edit or display a WORD-PROCESSING field, press the Enter/Return key at the WORD-PROCESSING field. This clears the screen and passes control to your Preferred Editor to edit the field. If you do not have a Preferred Editor, the Screen Editor is used. When you exit the editor, you return to the ScreenMan screen.

**Multiples Linked to "Pop-Up" Subpages**

A Multiple field can appear on a page and be linked to a regular or "pop-up" subpage. When you navigate to the Multiple field, select a Subrecord, and press the Enter/Return key, you are taken to the subpage, which contains the fields within the Multiple.

In the following illustration, the Multiple is the field with the caption "Select EMPLOYMENT HISTORY:". When you enter "FEB 1,1950" at this field, you are taken into a "pop-up" subpage, where you can edit the fields for that particular Subrecord:

###### Exiting a Subpage

While in a subpage, your only Command Line options are CLOSE and REFRESH. You cannot EXIT, Quit, or SAVE until you return to the parent page. You can return to the parent page by pressing **&lt;PF1&gt;C** or issuing the CLOSE command at the Command Line. From there, you can select another Subrecord to edit or navigate to another field.


#### Browser Overview

The Browser lets you view any text *on the screen* instead of *on paper* . Do this by printing your text to the **BROWSER** device instead of the HOME device or a printer.

The Browser makes it very easy to view text on screen. Its main features are:

1. Scroll forwards *and backwards* through the text. This means you don't lose lines of text "off the top" of the screen, like you do when you print to the HOME device.
2. Use the Search feature to find a text string and immediately jump to occurrences of the search string.
3. Copy selected text from  to the VA FileMan Clipboard; later, if you're editing a mail message or other WORD-PROCESSING-type field with the Screen Editor, you can paste from the clipboard.

**Shortcuts and Screen setup Tips**

Both the Browser and ScreenMan have shortcuts that can save you a lot of time. Each shortcut begins by pressing the Num Lock (NL) key. (NOTE: some laptops don’t have a NumLock key, so you would need to use Map Keyboard on your Reflections Utility menu to map a terminal key to the PC NumLock key.)

Some Browser actions:

- (NL)B – go to bottom
- (NL)E – exit
- (NL)F – find
- (NL)H – help
- (NL)Q – quit
- (NL)T – go to top

Some ScreenMan shortcuts:

- (NL)C – close a screen
- (NL)E – exit and save changes
- (NL)H – help
- (NL)Q – exit and do not save changes
- (NL)Z – zoom editor

Your Reflections session setup makes a difference in the appearance of the ScreenMan display. The default for the screen element Normal is a white background and black foreground. Choosing a background color other than white and a foreground color that works well with the background color will provide a more readable ScreenMan display.


NOTE: For taxonomy inquiry print to display properly in Reflections, the setup must have Save from Scrolling Regions checked. Sequence is: Setup =&gt; Display =&gt; Screen =&gt; Display Memory Advanced.

**Example**


- **ALL** – Displays two pick lists for choosing codes
    - One for ICD and one for CPT
- **DX ONLY** – Displays pick list for ICD only. All CPT codes in taxonomy are entered into PCE

- **ALL** – Displays 2 pick lists for choosing codes
    - One for ICD and one for CPT
- **DX ONLY** – Displays ‘pick list’ for ICD only.  All CPT codes in taxonomy are entered into PCE