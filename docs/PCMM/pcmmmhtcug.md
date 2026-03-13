---
app_name: Primary Care Management Module (PCMM)
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: 2012-10
doc_type: user-manual
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-12'
is_base: false
is_change_pages: false
library_max_patch: null
package_id: PCMM
patch: 589
patch_gap: null
section: ''
source_file: pcmmmhtcug.docx
status: draft
title: pcmmmhtcug.docx
---

<!-- image -->

**Primary Care Management**

**Module (PCMM) – Mental Health Treatment Coordinator (MHTC)**

**User Manual**

January 2012

Revised December 2012


Product Development (PD)

Revision History

| Date     | Description (Patch # if applicable.)                                                                                      | Project Manager   | Technical Writer   |
|----------|---------------------------------------------------------------------------------------------------------------------------|-------------------|--------------------|
| Dec 2012 | Minor updates for clarification                                                                                           | REDACTED          | REDACTED           |
| Oct 2012 | SD*5.3*589 – Addition of MH Reporting capability                                                                          | REDACTED          | REDACTED           |
| Oct 2012 | OR*3*348 – Added Notifications section                                                                                    | REDACTED          | REDACTED           |
| Jul 2012 | SD*5.3*581 – Changes to the Assigning Staff to Positions section: added step 5, and updated screens at steps 1, 4, and 6. | REDACTED          | REDACTED           |
| Jan 2012 | SD*5.3*575 - Initial version.                                                                                             | REDACTED          | REDACTED           |

Table of Contents

Introduction	4

Overview of the Primary Care Management Module	4

Mental Health Treatment Coordinator Overview	4

Sensitive Information	5

Notifications	5

PCMM Mental Health Treatment Coordinator	6

PCMM Online Help	7

Creating a Mental Health Team	7

Adding Positions to a Mental Health Team	12

Assigning Staff to Positions	15

Mental Health Reports – Roll and Scroll	19

MH PCMM STOP CODES (404.61) File Overview	19

Accessing the Mental Health Reports	19

Roll and Scroll – Changing output display setting	20

MH Clinician’s Patient Report	21

MH Encounter Report	24

MH Historical Patient Assignment Detail Report	25

MH Historical Team Assignment Summary Report	28

PCMM Mental Health Business Rules	30

Mental Health Patient	30

Mental Health Team	31

Mental Health Staff	31

MHTC Roles	31

PCMM VistA - MH Reporting Business Rules	31

MH PCMM Report Menu Options	31

MH Clinician’s Patient Report	31

MH Encounter Report	32

MH Historical Patient Assignment Detail Report	32

MH Historical Team Assignment Summary Report	33

References	33

Glossary	34

Appendix A:  Standard Position File (#403.46)	i

Appendix B:  MH Routines, Files &amp; Options	iii

Routines	iii

Files	iii

Options	iv

Appendix C:  MH PCMM STOP CODES File (#404.61)	i

## Introduction

### Overview of the Primary Care Management Module

The Primary Care Management Module (PCMM) was developed to assist the Department of Veterans Affairs (VA) facilities in implementing primary care. PCMM supports both primary care and non-primary care teams. Teams are groups of staff members organized for a certain purpose. The software allows you to setup and define a team, assign positions to the team, assign staff to the positions, assign patients to the team, assign patients to practitioners, and reassign patients from one team to another team.

### Mental Health Treatment Coordinator Overview

This User Guide supports the Identification of Principal Mental Health Provider (IPMHP) project under the Improve Veteran Mental Health (IVMH) initiative. It explains the new functionality introduced within PCMM to address the critical need to rapidly identify a patient’s Mental Health Treatment Coordinator (MHTC) so that veterans with conditions such as depression, suicidal ideation and Post Traumatic Stress Disorder (PTSD) can be treated more quickly and effectively. This affects nurses, physicians, ward clerks, Primary Care Management Module (PCMM) coordinators and all other mental health professionals.

The list below provides a high level overview of the new functionality around Mental Health Treatment Coordinators (MHTCs):

- 24 new roles added: Refer to Appendix A:  Standard Position File (#403.46) for a complete listing of positions available in PCMM.
    - Addiction Therapist
    - Addiction Therapist (MHTC)
    - Chaplain
    - Chaplain (MHTC)
    - Clinical Nurse Specialist (MHTC)
    - Clinical Pharmacist (MHTC)
    - LPC
    - LPC (MHTC)
    - MFT
    - MFT (MHTC)
    - Nurse (RN) (MHTC)
    - Nurse Practitioner (MHTC)
    - Occupational Therapist
    - Occupational Therapist (MHTC)
    - Peer Support Staff
    - Physician Assistant (MHTC)
    - Physician-Psychiatrist (MHTC)
    - Psychologist (MHTC)
    - Recreation Therapist
    - Recreation Therapist (MHTC)
    - Social Worker (MHTC)
    - Rehab/Psych Technician (MHTC)
    - Voc Rehab Spec/Counselor
    - Voc Rehab Spec/Counselor (MHTC)
- Ability to create a Mental Health Team
- MHTC information is displayed in CPRS on the patient inquiry and primary care display
- Ability to pull reports on MHTC using the PCMM VistA environment
    - MH Clinician’s Patient Report
    - MH Encounter Report
    - MH Patient Assignment Detail Report
    - MH Historical Team Assignment Summary Report

Refer to Appendix B:  MH Routines, Files &amp; Options for a listing of PCMM Routines, Files and Options associated with MH.


### Sensitive Information

To avoid displaying sensitive information regarding our patients and staff, the examples in this manual contain test data. The steps were captured from a testing environment where the staff and patients’ personal data is not real data. Real social security numbers (SSNs) and other personal identifiers are not used.

## Notifications

New provider recipients, Primary Care Management Module (PCMM) Mental Health Treatment Coordinator (MHTC), have been added to the existing ORB PROVIDER RECIPIENTS parameter. It has been added as a 'C' code to the existing 'PATOMERS'values.  Below is the set of codes indicating default provider recipients of a notification by their title or relationship to the patient.  Notifications can be set up with any or all of the following codes:

P (Primary Provider): deliver notification to the patient's Primary Provider.

A (Attending Physician): deliver notification to the patient's Attending Physician.

T (Patient Care Team): deliver notification to the patient's Primary Care Team.

O (Ordering Provider): deliver notification to the provider who placed the order which triggered the notification.

M (PCMM Team): deliver notification to users/providers linked to the patient via PCMM Team Position assignments.

E (Entering User): deliver notification to the user/provider who entered the order's most recent activity.

R (PCMM Primary Care Practitioner): deliver notification to the patient's PCMM Primary Care Practitioner.

S (PCMM Associate Provider): deliver notification to the patient's PCMM Associate Provider.

C (PCMM Mental Health Treatment Coordinator): deliver notification to the patient's PCMM Mental Health Treatment Coordinator.

MHTCs can specify to be the default provider recipients of certain pertinent notifications, such as for Admissions, Discharge, and Deceased Patient, to name a few.

SUICIDE ATTEMPTED/ COMPLETED is a new notification related to MH. This informational notification is triggered by Clinical Reminders when a MH SUICIDE ATTEMPTED or MH SUICIDE COMPLETED health factor has been documented in Patient Care Encounter (PCE). It is exported with package parameter values set as follows:

. ORB ARCHIVE PERIOD - 30

. ORB DELETE MECHANISM - Individual Recipient

. ORB FORWARD BACKUP REVIEWER - No

. ORB FORWARD SUPERVISOR - No

. ORB FORWARD SURROGATES - No

. ORB PROCESSING FLAG - Disabled

. ORB PROVIDER RECIPIENTS - MHTC and PCMM Team (CM)

. ORB URGENCY - High

***NOTE:*** An ORB PROVIDER RECIPIENT parameter value of “CM” is exported with the Suicide behavior notification. Therefore, the suicide behavior notification will be sent to the MHTC and PCMM Mental Health team if any are set up and configured at the site.

## PCMM Mental Health Treatment Coordinator

Mental Health teams are created following similar steps as you would to create a Primary Care team. Additional items have been added to fields to allow you to identify the team as a mental health team. New positions have been created to provide designated MHTC roles. Refer to the business rules section of this manual to obtain further information on how these fields are handled in the system.

Reference the PCMM User Manual if further detail or instruction is needed for PCMM functionality as this manual only covers MHTC PCMM functionality. A link to the PCMM User Manual can be found in the Reference section of this document. The instructions provided in this manual for creating a MH team and adding positions to a MH team can additionally be accessed through the PCMM online help, if needed as a quick reference while navigating through the PCMM application.

### PCMM Online Help

The PCMM application has an online help feature that contains high level instructions of what is displayed in this guide. Below is a listing of the sections within the online help related to the PCMM instructions provided in this guide

- **Mental Health Team Setup:** contains an overview of the MH capability in PCMM.
    - **Create a New Mental Health Team** :  provides instruction on how to set up a MH Team.
    - **Assign Positions to a Mental Health Team** :  provides instruction on how to assign positions to a MH Team.

1. Log into PCMM.
<!-- image -->
2. Click on the  toolbar speedbutton to launch the online help file.
3. Click on Contents.
4. Select the appropriate online help section.

### Creating a Mental Health Team

<!-- image -->

1. From the main screen after login, select the **Team** speedbutton  from the toolbar located in the upper left of the screen.

<!-- image -->

1. In the resulting pop up window, select the **New** button, as highlighted below to create a new team.
<!-- image -->

1. After clicking the **New** button, the team name pop up window appears. Enter in the MHTC Team name in this window’s text field, then select **OK** in the bottom left of this window.

<!-- image -->

1. The Primary Care Team Profile box appears with the team name populated. Enter in the team information on the General and the Settings tab.

<!-- image -->

##### Field Descriptions

1. *Name (text box)

The name of the team, 3-30 characters in length. If the new team name matches an existing team name, you will be so notified and asked for a different name.

1. Phone Number (text box)

Enter a phone number for the team, 3-20 characters.

1. Description (text box)

Any descriptive information specific to the team.

1. Current Activation (Label)

This label field displays the most recent activation date for the team.

1. Current Inactivation (Label)

This label field displays the most recent inactivation date for the team.

1. Positions (button)

This button takes you to the Team Positions Setup Screen. This button remains disabled until all required fields are complete with creating the new team.

1. **Autolinks (button)** (FUNCTIONALITY DISABLED)

***TIP:*** *Required fields are signified in this documentation by an asterisk* ******* *next to the field name. The SAVE button will not be enabled until all required fields contain information.*

1. On the Setting tab, select Mental Health Treatment from the Purpose drop-down list. Then fill in Service, Institution and Team Printer fields as necessary.

Note:  Upon selection of Mental Health Treatment, the Primary Care Team check box field to the right will be disabled. A mental health team cannot be set up as a primary care team.

1. Click on the **Save** icon.

<!-- image -->

##### Field Descriptions – Primary Care Team Profile Settings Tab

1. Purpose (drop down list)

The Purpose defines the role of the team. Mental Health Treatment would be the purpose for a Mental Health team.

1. Service (lookup box)

This is the medical center service most closely associated with the team.

1. Institution (lookup box)

This is the entry from the INSTITUTION file (#4) associated with the team. It includes VA and non-VA institutions.

***TIP:*** *Each division at a multidivisional facility has its own entry in the INSTITUTION file.*

1. Default Team Printer (lookup box)

The PCMM reports do not use this field.

1. Primary Care Team (check box)

Click in this box if this team can be the primary care team for any patient.

1. Restrict Consults (check box)

Click in this box to prevent users from making consult appointments to clinics in which this team's patients are not enrolled.

1. Team Closed (check box)

Click in this box to close the team. Additional patients should not be added to a team if it is designated as closed.

1. Auto-Assign to Team from Clinic (check box)

Click in this box to automatically assign the patient to a team when he is enrolled in a clinic that is an "associated clinic" of one of the team's positions.

1. Auto-Discharge from Team from Clinic (check box)

Click in this box to automatically discharge the patient from a team when he is discharged from a clinic that is an "associated clinic" of one of the team's positions.

1. Team Assignments (text box)

Allowed (numeric display) Maximum number of patients that should be assigned to this team.

Actual (numeric display) Number of patients currently assigned to this team.

1. The calendar box opens where you would select the team activation date, then select **OK** .

<!-- image -->

### Adding Positions to a Mental Health Team

<!-- image -->

1. Click on the **Position** icon  in the toolbar at the top of the main screen to start adding positions to the mental health team.

<!-- image -->

1. In the resulting window, click once on the desired team name to select it, and then click the **OK** button at the upper right of the Select Team window.

<!-- image -->

1. If the team has no positions assigned to it, an information box appears. Click the **OK** button in this box to proceed.

<!-- image -->

1. The Primary Care Team Position Setup window appears. At the top of the screen validate that the team selected displays at the top of the window, then select the **Add New Position** icon.

<!-- image -->

1. Type in the name of the position you wish to add.  Select **OK** .

<!-- image -->

1. Fill in all required information on the General tab. The Position field will be auto-populated with what was entered in the previous step. Scroll through the drop-down list and select the necessary role associated with the created position. Then select **Save** .

Note:  MHTC positions listed in the drop-down list will display with (MHTC) following the position name. MH Teams can consist of MHTC designated positions as well as non-MHTC designated positions.

<!-- image -->

Note:  PCMM will not allow a Mental Health team to be set up as a Primary Care Team.  Therefore when creating positions, the settings options located on the position Settings tab will be disabled (grayed out) as it is related to Primary Care Providers.

1. The calendar box pops up where you select the creation date of the position, then select **OK** .

<!-- image -->

You will return to the Primary Care Team Position Setup screen, where the new position created is highlighted yellow.

Repeat Steps 1 – 7 until all necessary positions have been created for the MH Team.

Note:  Positions can be created and activated without any staff assigned to them.  It is important to assure that staff is assigned to the new position upon creation.

### Assigning Staff to Positions

1. Navigate to the Staff/FTEE tab on the Primary Care Team Position Setup form, select the **Add Staff** icon.

<!-- image -->

1. Type in the name of the staff member and click on the **Search** icon.

<!-- image -->

1. Select the appropriate staff member returned in the staff lookup results, then select **OK** .

<!-- image -->

1. The selected staff member’s name appears in **BLUE** , select **Save** .

<!-- image -->

1. Now you can enter the FTEE for this position. Click in FTEE edit box and enter the FTEE for this position. Click Save.

Note: Entry of FTEE is optional; please check your current Local or National policy guidance on the requirements to delineate staff FTEE.

1. The staff member has been successfully added to the team. The staff member appears in the Staff Assignment History box in the lower right of the screen.

Repeat steps 1 – 5 until all necessary staff members have been assigned to each position associated with the MH Team.

<!-- image -->

## Mental Health Reports – Roll and Scroll

Mental Health reports are generated through the PCMM VistA environment. They are available through the roll and scroll Menu options. There are currently 4 reports available for mental health. One of the reports identifies MH patients in need of an MHTC. The other three reports provide historical and clinician data. The reports are described in further detail in the following sections.

This portion of the user guide will:

- Provide instruction for how to access the reports
- Provide an overview of each report describing the data that will be displayed for each
- Provide a step-by-step process for running each report available

**Note:** These Mental Health reports pull data based upon current PCMM GUI team setup parameters.  SUBSCRIPT errors may occur if a team was not created with a Team Purpose.  Examples of SUBSCRIPT errors which may be encountered include:

&lt;SUBSCRIPT&gt;MHTEAM+5^SCMCMHU1 ^SD(403.47,"")

&lt;SUBSCRIPT&gt;GETALL+12^SCMCMHU1 ^SD(403.47,"")

To rectify these errors, review the team setup and enter an appropriate team purpose.

### MH PCMM STOP CODES (404.61) File Overview

The MH PCMM STOP CODES file is used by the MH Encounter Report for determining if a Veteran meets the requirements for need of an MHTC. This file will initially be populated with current active stop codes that are reflected in the current VHA Mental Health Services policies.

The VHA Mental Health Services is responsible for notifying the National Patch release of changes that need to be made to the file when there are additions or deletions to the list of active MH stop codes that should be included in the report.  This information will be communicated through existing channels of communication with the file regarding policy issues for MHTC/PCMM (e.g., VISN Mental Health Leaders, MH PCMM Coordinators).

Any changes made to this file could result in the MH Encounters Report not producing valid and reliable data on which Veterans need to be assigned to an MHTC.

### Accessing the Mental Health Reports

Reports are accessed through the PCMM VistA environment.  A menu has been established specific to mental health, containing all reports available for pulling necessary data to assist with monitoring the care for a mental health patient.

To access the reports, follow the below steps:

***Note:*** In order to access the MH PCMM Report Menu, SCMC MH PCMM RPT MENU should be assigned to the user’s secondary menu options.

Go to the secondary menu options and type **SCMC MH PCMM RPT MENU** to access the MH PCMM Report Menu.

SCMC MH PCMM RPT MENU– MH PCMM Report Menu

<!-- image -->

### Roll and Scroll – Changing output display setting

Some of the MH reports require a 132-column output setting for displaying the output across your screen without any wrapped columns.  It is recommended to set up these options prior to running the MH Reports.  The reports that require this setting to display the output better will have a note in the description of the report in the below sections.

***Note:*** After running the MH Reports, restore your display settings back to the default setting of 80-columns.

To modify this setting in VistA:

1. Click on **Setup** , located in the upper left-hand corner, fourth option over from the left.
2. Click on **display** , then select the **Screen** tab along the upper left of the window.
3. Click on the Columns **132** radio button to select that display setting.
4. Click **OK** .

Changing display settings in VistA

<!-- image -->

### MH Clinician’s Patient Report

The MH Clinician’s Patient report will display the number of patients assigned to each MH provider on a team. The report will display both a summary report on the number of patients assigned to each provider on a mental health team and a detail report for each provider. The user chooses from three different sort options affecting the output of both the detail and summary reports. The headings/column names are not affected by the sort. For the detail report, sort option [1] Division, Team, Clinician sorts first by division, then team and lists the patients for each provider specified (including “all”) on each team and the summary report will similarly order the list alphabetically by team then provider. Sort options [2] and [3] both list patients assigned to each provider spec **i** fied in alphabetical order by clinician while sort option [2] also breaks down the list by team. If you only want data for 1 team, it is likely that all 3 sort options will yield the same output order. This report requires 132-column output.

Report Options:

- Select Institution/Division:  may select one/many/all institutions/divisions
- Select Mental Health team:  may select one/many/all MH Team(s)
- Select Role:  may select one/many/all Role(s)
- Select Clinician/Provider:  may select one/many/all Clinician/Provider(s)
- Select output sort options (not mandatory):
    1. Division, Team, Clinician
    2. Division, Practitioner, Team
    3. Practitioner, Associated Clinic

Summary Report columns:

- Clinician
- Position
- Team
- Patient Assigned

Detail Report columns:

- Clinician
- Patient Name
- Patient ID (Patient’s SSN - 5 leading X’s followed by the last 4 of SSN)
- Primary Eligibility
- Last Appointment
- Next Appointment
- Clinic

***Note:*** The last/next appointment and clinic columns will only display when “associated clinics” have been entered for the provider in PCMM. If a provider has more than one clinic listed in PCMM under the “associated clinics” tab, then all of those clinics will be listed vertically for that provider in the “clinic” column.

Steps for running this report:

1. From the MH PCMM Report Menu, type in **MH Clinician’s Patient Report** where prompted and press **ENTER.**

**Shortcut:** at **Select MH PCMM Report Menu Option** prompt, type **MH C** and the remainder of the name will auto populate after pressing **ENTER** .

1. Enter in a division or press **ENTER** to move forward and select **ALL** divisions if you choose.
2. Enter in a team name; may enter one/many/ or **ALL,** once entered, press **ENTER.**
3. At the select role prompt, enter in a specific role or type **ALL** to run this report for all roles and press **ENTER.**
4. At the Select Practitioner prompt, enter in a specific Practitioner or enter **ALL** and press ENTER.
5. At the Print Summary Only prompt select **No** to enable the ability to print both Summary and Detail or **Yes** to only print out the Summary report and press **ENTER.**

***Note:*** If you choose to print summary only, follow on to step 7 **.** If you choose **No** , Skip over to step 8.

1. At the prompt for delimited format, enter Yes or No.  If **Yes** is chosen, move on to step 9, otherwise, move forward and select a sort option.
2. At the Sort By prompt type in the option number as listed below for selecting your sort options, then press **ENTER** :
    1. Division, Team, Clinician
    2. Division, Practitioner, Team
    3. Practitioner, Associated Clinic
3. This report requires a 132-column output, at the DEVICE: HOME// prompt, enter **0;132** and press **ENTER** to run the report.

***Note:*** If **No** was entered back in step 6, the detail reports will display first (one report for each Practitioner), Press Any Key to Continue or ‘^’ to Quit

Sample: MH Clinician’s Patients Detail Report

<!-- image -->

1. The summary report will follow the display of the detail report(s).

Sample MH Clinician’s Patients Summary Report

<!-- image -->


### MH Encounter Report

The MH Encounter Report will display all patients with the specified number of qualifying MH encounters within the specified date range who do not have a MHTC identified in PCMM. This report enables the user to select an Institution, a date range, and the number of outpatient encounters (default = 3). The report will display a list of patients in descending order from the earliest encounter to the most recent encounter within the date range selected. The Encounter report will display only one encounter per day and will only count one encounter per day towards the number of encounters selected by the user. This report should be exported to an excel spreadsheet for readability.

Report Options:

- Select an Institution:  may select one/many/all institutions
- Select a date range
- Select number of outpatient encounters:  default will be three if nothing is provided, maximum will be ten

***Note:*** This report will display only one encounter per day which will be counted towards the number of encounters selected by user.

Columns displayed:

- Patient Name
- SSN (last 4)
- Days since last encounter
- Encounter
    - Clinic Name
    - Location of encounter
    - Future Appointment date/location

Steps for running this report:

1. From the MH PCMM Report Menu, enter in **MH Encounter Report** , press **ENTER.**

**Shortcut:** at **Select MH PCMM Report Menu Option** prompt, type **MH E** and the remainder of the name will auto populate after pressing **ENTER** .

1. Enter in a Beginning Date: **MMDDYYYY** , press **ENTER.**
2. Enter in an Ending Date: **MMDDYYYY** , press **ENTER.**
3. Enter in the Institution, press **ENTER.**
4. A list may populate, enter the number of choice for selecting the institution, and press **ENTER.**
5. Enter in the number of outpatient encounters (default is 3, maximum is 10), press **ENTER.**

**Tip:** to accept the default of 3 outpatient encounters, no need to type anything, just press **ENTER.**

1. At the DEVICE: HOME// prompt press **ENTER** to run the report.

***Note:*** This report should be run during off-peak hours as it can take hours to run. It is recommended to use a spooler for running this report.

Sample: MH Encounter Report

<!-- image -->


### MH Historical Patient Assignment Detail Report

The MH Historical Patient Assignment Detail Report will display the history of a patient’s mental health team, provider, and position assignments in addition to primary care assignments.

Report Options:

- Select a specific patient:  enter in patient’s name

***Note:*** user can enter in patient’s last name or a portion of it (minimum amount of characters is 3) to populate a list of patients to select from.

- Select a date range

Data displayed along top of report:

- Patient Name
- SSN
- Date of Birth
- Age
- Sex

Columns displayed in report:

- Assignment (Non primary care provider)
- Active (Date)
- Inactive (Date)
- Assigned by/date

Steps for running this report:

1. From the MH PCMM Report Menu, enter in **MH Historical Patient Assignment Detail Report** and press **ENTER.**

**Shortcut:** at **Select MH PCMM Report Menu Option** prompt, type **MH Historical P** and the remainder of the name will auto populate after pressing **ENTER** .

1. Enter in patient’s last name then press **ENTER.**
2. A list will populate, continue to press **ENTER** to filter through the list to find your patient, then type in the number of the patient and press **ENTER.**
3. Enter a Beginning Date where prompted, format is **MMDDYYYY** and press **ENTER.**
4. Enter in an Ending Date, format is **MMDDYYYY** or **TODAY** is the alternate option for entry.
5. Press **ENTER** to run the report.

Sample: Historical Patient Assignment Detail Report (page 1)

<!-- image -->

Sample: Historical Patient Assignment Detail Report (page 2)

<!-- image -->

Sample: Historical Patient Assignment Detail Report (page 3)

<!-- image -->

Sample: Historical Patient Assignment Detail Report (page 4)

<!-- image -->

### MH Historical Team Assignment Summary Report

This report will display the MH Team Assignment history. It will display a count of team and team position assignments within a given date range. There are two main parts to this report.  The first part of the report shows the “Summary of Team and Team Position Assignments”. The second part of the report shows the “Team Assignments without Active Position Assignments” and displays a list of patients who have been assigned to a mental health team in PCMM but have not been assigned to any position (including non-MHTC) on that team within the date range specified. A third part of the report, “Position Assignments Without Active Team Assignments”, displays patients who are assigned to a position but not a team during the date range specified.  The third part of the report usually will not display because PCMM should not allow a patient to be assigned to a position without a team assignment. This report requires 132-column output.

Report Options:

- Select a date range
- Select Institution:  may select one/many/all institutions

Columns displayed in Summary of Team and Team Position Assignments report:

- MH Team
- MAX Pts.
- Team Assignment
- Open Slots
- Patients w/o a MHTC Assignment
- Patients w/o a MH Team Assignment

Columns displayed in Team Assignments without Active Position Assignments and Position Assignments without Active Team Assignments reports:

- Division
- Team
- Patient Name
- Social Security Number (SSN) (5 leading X’s followed by the last 4 of SSN)
- Active Date
- Inactive Date

Steps for running this report:

1. From the MH PCMM Report Menu, enter in **MH Historical Team Assignment Summary Report** and press **ENTER.**

**Shortcut:** at **Select MH PCMM Report Menu Option** prompt, type **MH HISTORICAL T** and the remainder of the name will auto populate after pressing **ENTER** .

1. At the Final Summary Only prompt enter **NO** to display both final summary and detail reports or **YES** to display Final Summary only, press **ENTER.**
2. Enter a beginning date, format is **MMDDYYYY** , press **ENTER.**
3. Enter in an ending date, press **ENTER** if you wish to select today’s date, otherwise enter **MMDDYYY** , and press **ENTER.**
4. Select Institution, enter **ALL** to select all institutions or enter in a specific institution, and press **ENTER.**
5. Enter in the team name where prompted, press **ENTER.**
6. Press **ENTER** at the Ok prompt.
7. This report requires a 132 column output, at the DEVICE: HOME// prompt, enter **0;132** and press **ENTER.**

Sample: MH Historical Team Assignment Summary:  Summary of Team and Team Position Assignments Report

<!-- image -->

Sample: MH Historical Team Assignment Summary:  Team Assignments Without Active Position Assignments Report

<!-- image -->

Sample:  MH Historical Team Assignment Summary:  Position Assignments Without Active Team Assignments Report

<!-- image -->

## PCMM Mental Health Business Rules

The PCMM Business Rules provide information on how some of the PCMM fields will be handled for mental health team, team positions, and patient assignments. These rules are not intended to be all encompassing, but for general information purposes to allow some basic validation within the system to ensure data integrity.


### Mental Health Patient

- A patient who has been assigned a Primary Care Provider can be assigned to a MHTC.
- A patient who has not been assigned to a Primary Care Provider can be assigned to a MHTC.
- A patient can be assigned to multiple providers within their assigned mental health team.
- A patient can be assigned to multiple mental health teams.
- A patient cannot have more than one MHTC.

### Mental Health Team

- In order for a team to be designated as a mental health team, the “Mental Health Treatment” purpose needs to be selected within the Primary Care Team Profile Settings.
- A mental health team can only be designated as a non-primary care team.
- If Mental Health Treatment is selected as the purpose, the Primary Care Team checkbox will be disabled (grayed out).
- If Mental Health Treatment is selected as the purpose, the checkboxes on the Settings tab will be disabled when setting up positions for that mental health team.
- A mental health team can have an unlimited number of positions.  Those positions can be occupied by any number of designated mental health roles.

### Mental Health Staff

- Any staff member assigned to a MHTC Role can additionally be assigned to any non-mental health team.

### MHTC Roles

- The naming convention for a designated MHTC role will display as, “&lt;role&gt; (MHTC)”.  For example, “Social Worker (MHTC)”.
- The MHTC designation will display in all areas where the Role is viewed.

## PCMM VistA - MH Reporting Business Rules

The PCMM VistA – MHTC Reporting business rules provides further information on the Mental Health Report Menu Options and the reports listed within this menu.

- The mental health reporting capability will enable a user to identify specific needs of our Veteran patients.
- The clinicians overseeing the patients care will have the ability to identify patients in need of continuing mental health treatment.

### MH PCMM Report Menu Options

- A standalone secondary Mental Health menu will be available for accessing the mental health reporting options.
- The secondary menu will need to be assigned to the appropriate designated Mental Health personnel.
- The secondary menu will contain the mental health reports displayed in this user guide.

### MH Clinician’s Patient Report

- The Mental Health Clinician’s Patient Report will allow for selections of Institution/Division, MH Team, Role and Clinician/Provider for the initial search criteria on data returned.
- All search criteria options will have the ability to select “All” or a user will have the option to choose specific information from each selection.
- If the user chooses to Print Summary only and display in delimited format, they will not be prompted to select a sort option.
- The Mental Health Clinician’s Patient Report will display the number of patients assigned to each Mental Health provider.
- This report will have the look and feel of the PCMM Practitioner’s Patients report and will accommodate the specific needs of Mental Health so that it provides both a summary report on number of patients assigned and a detail report when there is a need to see specific teams.
- The Mental Health Clinician’s Patient summary report will display columns of data listing the Clinician, Position, Team and Patients Assigned.
- The Mental Health Clinician’s Patient detail report will display columns of data listing the Clinician, Patient Name, Patient ID, Primary Eligibility, Last Appointment, Next Appointment and Clinic.

### MH Encounter Report

- The Mental Health Encounter Report will use the DSS Identifiers to determine if a patient has been seen in a mental health circumstance.
- The search criteria for this report will be date range and a number of outpatient encounters (default is 3, maximum is 10).
- The Mental Health Encounter Report will not select patients already assigned to a MHTC.
- The Mental Health Encounter Report will identify patients assigned to a Mental Health team and do not have an assigned MHTC.
- The Mental Health Encounter Report will display a list of patients in descending order from the earliest encounter to the most recent encounter.
- The future date for a patient appointment will be displayed.
- The patient information output for this report will be Patient Name and SSN.
- The Mental Health Encounter Report will display columns of data providing Clinic Name, Locations of last three encounters, and Date since last encounter and Future Appointment Date/Location.
- The Encounter Report will display only one encounter per day which will be counted towards the number of encounters selected by the user.

### MH Historical Patient Assignment Detail Report

- The Mental Health Historical Patient Assignment Detail Report will display the history of a patient’s MHTC, Mental Health teams and Mental Health Providers assignments.
- The Mental Health Historical Patient Assignment Detail Report will have the same look and feel of the Historical Patient Assignment Detail (PAD) report within the PCMM reporting options.
- The search criteria for this report will be patient’s name and date range.
- The patient information output for this report will be Patient Name, SSN, Date of Birth, Age and Sex.
- The Mental Health Historical Patient Assignment Detail Report will display columns of data providing Assignment, Active, Inactive and Assigned by/date.

### MH Historical Team Assignment Summary Report

- The Mental Health Historical Team Assignment Summary Report will represent a count of team and team position assignments within a date range selected.
- The report will contain two parts; first page will display the “Summary of Team and Team Position Assignments”, the second page will display the “Team Assignments without Active Position Assignments” information.
- The Mental Health Historical Team Assignment Summary Report will contain a prompt to select a date range and allow the user to choose specific Institution(s) and Team(s) or select “All” for the criteria.
- The Mental Health Historical Team Assignment Summary Report will display columns of data providing the Mental Health team, Maximum Patients, Team Assignments, Total Unique Patients, Open Slots, Patients w/o MHTC Assignments and Patients w/o MH Team Assignments on the first page, and Summary of Team and Team Positions Assignments.
- The Mental Health Historical Team Assignment Summary Report will display columns of data providing the Division, Team, Patient Name, SSN, Active Date and Inactive Date on the second page of the report, Team Assignments Without Active Position Assignments.

## References

- [PCMM User Manual](http://www4.va.gov/vdl/documents/Clinical/Pri_Care_Mgmnt_Module_(PCMM)/pcmmug.pdf) – sections to refer to for further instruction on processes covered in this manual listed below(quick link to sections from the table of contents):
    - Create a New Team
    - Assign Positions to a Team
    - Assign Staff Members to a Position
Additional sections for reference related to Mental Health (quick link to sections from the table of contents):
    - Assign Single Patient to Team/Position(s)
    - Assign Multiple Patients to Team/Position(s)
    - Reassign Multiple Patients to Team/Position(s)
    - Edit an Existing Team
    - Reports – Roll and Scroll
        - [CPRS User Guide, GUI Version](http://www4.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/cprsguium.pdf)

## Glossary

| **Term**                        | **Definition**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CALENDAR DISPLAY                | Within PCMM, when there is a date field, the user can “double click” the field and a miniature calendar will ‘pop up’ for selection of a date and year. This is used for activation and deactivation dates as well as discharge dates.                                                                                                                                                                                                                                                                                                                                                                 |
| CLOSING                         | Another term for ‘inactivating’ a position or team.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| DIETITIAN                       | Performs patient care duties related to nutrition and weight management                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| DROP DOWN LIST                  | When a user selects an item from the MENU BAR, a list is displayed in a vertical format. For example, if a user selects FILE, a list drops down showing all options that are available under the main heading FILE: File, Edit, Print, Save                                                                                                                                                                                                                                                                                                                                                            |
| ENHANCEMENT                     | An ‘enhancement’ to an already existing Class I software package is the introduction of new or improved functionality.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| GUI                             | Graphical User Interface                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| HIGHLIGHT                       | To ‘Highlight’ a name, team, position, or date, one would place the cursor (or arrow) on the name, team, or position they wish to choose and ‘click’ the mouse button to select it or highlight it.                                                                                                                                                                                                                                                                                                                                                                                                    |
| HISTORY FILE                    | Although not specific to any one document, a history file is a compilation of various pieces of information pertaining to individual teams, positions, etc. for future reference and clarification.                                                                                                                                                                                                                                                                                                                                                                                                    |
| ENCOUNTER                       | An encounter is a contact between patient and a provider who has primary responsibility for assessing and treating the patient.  A patient may have multiple encounters per visit. Outpatient encounters include scheduled appointments and walk-in unscheduled visits. A clinician’s telephone communication with a patient may be represented by a separate visit entry. If the patient is seen in an outpatient clinic while an inpatient, this is treated as a separate encounter.                                                                                                                 |
| ICON                            | An Icon is an image or snapshot of something that is visually understood and is represented in a ‘box’. For instance, an ICON that stands for ‘cutting’ a piece of text out of a document would be a box with a picture of a pair of scissors in it. They are also known as ‘buttons’.                                                                                                                                                                                                                                                                                                                 |
| INSTITUTION                     | A Department of Veterans Affairs (VA) facility assigned a number by headquarters, as defined by Directive 97-058. An entry in the INSTITUTION file (#4) that represents the Veterans Health Administration (VHA). There are a wide variety of facility types in the INSTITUTION file, including medical centers, clinics, domiciliary, administrative centers, Veterans Integrated Service Networks (VISNs), and so forth.                                                                                                                                                                             |
| LOG OFF                         | This is referred to logging off or signing out of a particular software package or system. To end the session, to ‘get out’ of a package, etc.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| LOG ON                          | This is referred to logging on or signing onto a particular software package or system. To open or start a new session.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| MENTAL HEALTH CLINICIAN         | A clinician who provides mental health care as defined by their privileges or scope of practice. Disciplines that represent Mental Health Clinician include Psychologist, Physician Assistant, Nurse, Psychiatrist, etc.  When referenced in PCMM, a “Mental Health Clinician” refers to those disciplines listed in the roles defined in section “3.2.1 PCMM Requirements” of the ID PMHP SSD.  Note: Whether a particular Mental Health Clinician can serve as a MHTC is determined by their license, education and/or certification as defined in the OMHS Uniform Mental Health Services Handbook. |
| MH Treatment Coordinator (MHTC) | The liaison between the patient and the mental health system at a VA site.  There is only one MH treatment coordinator per patient and they are the key coordinator for behavioral health services care.  For more information about the MH treatment coordinator’s responsibilities, see VHA Handbook 1160.1, "Uniform Mental Health Services in VA Medical Centers and Clinics," pp. 3-4.  **Note:**  In the handbook, the MHTC is called the Principal Mental Health Provider.                                                                                                                      |
| PCE                             | Patient Care Encounter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| PCMM                            | Primary Care Management Module                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| POSITION                        | A name assigned by site to describe/define a Role in PCMM.  Positions are displayed in several tables on the PCMM GUI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| PRIMARY CARE                    | Primary care is the provision of integrated, accessible health care services by clinicians that are accountable for addressing a large majority of personal health care needs.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ROLE                            | A function or task of a staff member involved with the implementation, maintenance and continued success of primary care.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| TEAM                            | Teams are groups of staff members organized for a certain purpose (e.g., Primary Care, Mental Health).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| TEAM PROFILE                    | This is a screen within PCMM that shows the various characteristics of a particular team, e.g., number of patients allowed for enrollment, name, positions assigned, etc.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| TEXT BOX                        | The text box is also known as the DIALOGUE box as described above. It provides the user with an area in which to identify certain characteristics of a particular component of PCMM. For example, the description of what a team is for (provides primary care to patients that have been discharged from the hospital within the last 6 months).                                                                                                                                                                                                                                                      |
| VistA                           | Veterans Health Information Systems and Technology Architecture, formerly known as Decentralized Hospital Computer Program, encompass the complete information environment at VA medical facilities.                                                                                                                                                                                                                                                                                                                                                                                                   |


## Appendix A:  Standard Position File (#403.46)

The below 54 entries are available to choose from in the Position pick-list:

| ADDICTION THERAPIST                |
|------------------------------------|
| ADDICTION THERAPIST (MHTC)         |
| ADMIN COORDINATOR                  |
| CARE MANAGER                       |
| CASE MANAGER                       |
| CHAPLAIN                           |
| CHAPLAIN (MHTC)                    |
| CLINICAL NURSE SPECIALIST          |
| CLINICAL NURSE SPECIALIST (MHTC)   |
| CLINICAL PHARMACIST                |
| CLINICAL PHARMACIST (MHTC)         |
| DESIGNATED WOMEN’S HEALTH PROVIDER |
| DIETITIAN                          |
| HEALTH TECHNICIAN                  |
| INTERN (PHYSICIAN)                 |
| LPC                                |
| LPC (MHTC)                         |
| MAS CLERK                          |
| MEDICAL STUDENT                    |
| MFT                                |
| MFT (MHTC)                         |
| NURSE (LPN)                        |
| NURSE (RN)                         |
| NURSE (RN) (MHTC)                  |
| NURSE PRACTITIONER                 |
| NURSE PRACTITIONER (MHTC)          |
| OCCUPATIONAL THERAPIST             |
| OCCUPATIONAL THERAPIST (MHTC)      |
| OIF OEF CLINICAL CASE MANAGER      |
| OIF OEF PROGRAM MANAGER            |
| OIF OEF TRANSITION PATIENT ADV     |
| OTHER                              |
| PATIENT SERVICES ASSISTANT         |
| PEER SUPPORT STAFF                 |
| PHYSICIAN ASSISTANT                |
| PHYSICIAN ASSISTANT (MHTC)         |
| PHYSICIAN-ATTENDING                |
| PHYSICIAN-PRIMARY CARE             |
| PHYSICIAN-PSYCHIATRIST             |
| PHYSICIAN-PSYCHIATRIST (MHTC)      |
| PHYSICIAN-SUBSPECIALTY             |
| PSYCHOLOGIST                       |
| PSYCHOLOGIST (MHTC)                |
| RECREATION THERAPIST               |
| RECREATION THERAPIST (MHTC)        |
| REHAB/PSYCH TECHNICIAN             |
| REHAB/PSYCH TECHNICIAN (MHTC)      |
| RESIDENT (PHYSICIAN)               |
| SOCIAL WORKER                      |
| SOCIAL WORKER (MHTC)               |
| TEAM PHARMACIST                    |
| TRAINEE                            |
| VOC REHAB SPEC/COUNSELOR           |
| VOC REHAB SPEC/COUNSELOR (MHTC)    |

Return to MHTC Overview section

Return to files listing in Appendix B:  MH Routines, Files &amp; Options

## Appendix B:  MH Routines, Files &amp; Options

### Routines

| **Routine Name**   | **Description**                                                                                                                                                                                                                                                |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SCMCMHTC           | ***Input Attribute***  Name:  DFN  ***Definition:***  Patient Identification Number  ***Output Attribute Name:***  MHTC  ***Definition:***  Pass the MHTC for a patient to CPRS for display, including IEN and PCMM Team, Position and Role.                   |
| SCMCMH             | ***Input Attribute Name***  :  DFN and TEAM IEN  ***Definition:***  Patient Identification Number and Team IEN from file (404.57)  ***Output Attribute Name and Definition:***  True or False (0 or 1) is returned.                                            |
| SCRPU4             | ***Input Attribute Name***  :  DFN  ***Definition:***  Patient Identification Number  ***Modified Logic***  *:*  Adds call to display MHTC, primary care team, primary care provider and team phone for patient DFN on date ADATE in CPRS.                     |
| SCMCMHE            | ***Related Options:***  SCMC MH PCMM ENCOUNTER RPT  ***Current Logic:***  This report will allow for the identification of patients who need a MH assignment.  This will be done using DSS Identifiers to determine if a patient has been seen in a MH clinic. |
| SCMCMHPP           | ***Related Option:***  SCMC MH PCMM CLINICIAN PAT RPT  ***Current Logic:***  This report identifies the size and constituents of a Mental Health Clinician within PCMM.                                                                                        |
| SCMCMHP2           | ***Related Option:***  SCMC MH PCMM CLINICIAN PAT RPT  ***Current Logic:***  This report identifies the size and constituents of a Mental Health Clinician within PCMM.                                                                                        |
| SCMCMHHP           | ***Related Option:***  SCMC MH PCMM HIST PAT RPT  ***Current Logic:***  This report is a history of Mental Health patient assignments within PCMM.                                                                                                             |
| SCMCMHHT           | ***Related Option:***  SCMC MH PCMM HIST TEAM SUMMARY  ***Current Logic:***  This report will display Mental Health PCMM Team Assignment history. The report is a summary of the assignment history.                                                           |
| SCMCMHU1           | ***Related Option:***  SCMC MH PCMM CLINICIAN PAT RPT  ***Current Logic:***  This report identifies the size and constituents of a Mental Health Clinician within PCMM.                                                                                        |


### Files

| **File Name &amp; Number**       | **File Documentation**                                                                                                                                                  |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| STANDARD POSITION FILE (#403.46) | 24 roles added to existing file.  Refer to Appendix A:  Standard Position File (#403.46) for listing.                                                                   |
| MH PCMM STOP CODES (#404.61)     | File contains a list of Mental Health Stop Codes used when running the SCMC MH PCMM ENCOUNTER RPT. Refer to Appendix C:  MH PCMM STOP CODES File (#404.61) for listing. |

### Options

| **Option Name**                                                         | **Option Definition**                                                                                                                                                                                                         |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MH PCMM Report Menu                                                     | MH PCMM Report Menu to display the below menu options:  MH Clinician’s Patient Report  MH Encounter Report  MH Historical Patient Assignment Detail Report  MH Historical Team Assignment Summary Report                      |
| MH Clinician’s Patient (SCMC MH PCMM CLINICAN PAT RPT)                  | This report identifies the size and constituents of a Mental Health Clinician within PCMM.  Go back to associated Routine:  SCMCHPP  Go back to associated Routine:  SCMCMHP2  Go back to associated Routine:  SCMCMHU1       |
| MH Encounter Report (SCMC MH PCMM ENCOUNTER RPT)                        | This report will allow for the identification of patients who need a MH assignment.  This will be done using DSS Identifiers to determine if a patient has been seen in a MH clinic.  Go back to associated Routine:  SCMCMHE |
| MH Historical Patient Assignment Detail (SCMC MH PCMM HIST PAT  RPT)    | This report identifies the size and constituents of a Mental Health Clinician within PCMM.  Go back to associated Routine:  SCMCHHP                                                                                           |
| MH Historical Team Assignment Summary (SCMC MH PCMM HIST TEAM  SUMMARY) | This report will display Mental Health PCMM Team Assignment history. The report is a summary of the assignment history.  Go back to associated Routine:  SCMCMHHT                                                             |

Return to MHTC Overview


## Appendix C:  MH PCMM STOP CODES File (#404.61)

**Note:** This Veterans Health Administration (VHA) Directive defines the purpose and use of Decision Support System (DSS) Identifiers. DSS Identifiers are also commonly known as stop codes.  The below list of stop codes were derived by the Nationally released list of stop codes. The stop codes number cannot be changed without approval from the VHA. The nomenclature can be changed at individual sites so might not reflect the national list nomenclature. It is recommended to use the nomenclature from the national released list. Future updates to the #404.61 file should utilize the National patch module.

**MH PCMM STOP CODES LIST                        OCT 25, 2012 12:14**

**CLINIC STOP NAME                                     CODE      EXCLUDE CODE**

--------------------------------------------------------------------------------

ACTIVE DUTY SEXUAL TRAUMA                  524

C&amp;P VIA CVT PROV SITE                               445               YES

C&amp;P VIA CVT PT SITE                                    444              YES

COMP &amp; PENS (C&amp;P) EXAMS                      450               YES

DAY HOSPITAL-GROUP                                554

DAY HOSPITAL-INDIVIDUAL                        506

DAY TREATMENT-GROUP                            553

DAY TREATMENT-INDIVIDUAL                    505

DES EXAM                                                      448                YES

GRANT &amp; PER DIEM GROUP                       504

GRANT &amp; PER DIEM INDIV                          511

HCHV/HCMI GROUP                                    508

HCHV/HCMI INDIV                                       529

HUD/VASH GROUP                                      507

HUD/VASH INDIV                                         522

IDES VIA CVT PROV SITE                             447                YES

IDES VIA CVT PT SITE                                   446                YES

INTNSE SUB USE DSRDER GRP                   547

INTNSE SUB USE DSRDER IND                    548

MENTAL HEALTH CLINIC - IND                   502

MENTAL HEALTH CLINIC-GROUP              550

MH CWT/SE FACE TO FACE                        568

MH CWT/TWE FACE TO FACE                    574

MH INCENTIVE THERAPY F TO F                573

MH RESIDENTIAL CARE IND                        503

MH VOCATIONAL ASSISTANCE - IND         535

MH VOCATIONAL ASSISTANCE-GRP          575

MHICM - GROUP                                           567

MHICM - INDIVIDUAL                                   552

MOVE! PGM GROUP                                     373            YES

MOVE! PGM INDIV                                        372            YES

OPIOID SUBSTITUTION                                  523

PCT-POST TRAUMATIC STRESS-GRP            561

PRRC GROUP                                                   583

PRRC INDIVIDUAL                                              582

PSYCHIATRY - GROUP                                       557

PSYCHIATRY - INDIVIDUAL                               509

PSYCHOGERIATRIC - GROUP                            577

PSYCHOGERIATRIC - INDIVIDUAL                    576

PSYCHOLOGY-GROUP                                       558

PSYCHOLOGY-INDIVIDUAL                               510

PSYCHOSOCIAL REHAB - GROUP                     559

PSYCHOSOCIAL REHAB - IND                            532

PTSD - GROUP                                                     516

PTSD - INDIVIDUAL                                             562

PTSD CLINICAL TEAM PTS IND                          540

PTSD DAY HOSPITAL                                          580

RRTP ADMISSION SCREENING SRVCS             596

RRTP AFTERCARE GRP     		                          595

RRTP AFTERCARE IND                                       588

RRTP PRE-ADMIT IND                                       598

SERV-MH GROUP                                              572

SERV-MH INDIVIDUAL                                      571

SMOKING CESSATION                                      707           YES

SUB USE DISORDER HOME VST                      514

SUBST USE DISORDER/PTSD TEAMS              519

SUBSTANCE USE DISORDER IND                     513

SUBSTANCE USE DISORDR GRP                      560

TELE SMOKE CESS PROV SITE                          708           YES

WOMEN'S STRESS DISORDER TEAMS          525

Return to Appendix B:  MH Routines, Files &amp; Options