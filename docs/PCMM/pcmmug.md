---
app_name: Primary Care Management Module (PCMM)
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: 2015-06
doc_type: user-manual
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-12'
is_base: false
is_change_pages: false
library_max_patch: null
package_id: PCMM
patch: 624
patch_gap: null
section: ''
source_file: pcmmug.docx
status: draft
title: 'of Patients  : 6'
---

<!-- image -->

**Primary Care Management**

**Module (PCMM)**

**User Manual**

September 1999

Revised June 2015


Office of Enterprise Development (OED)

Revision History

Initiated on 12/23/2004

| Date       | Description (Patch # if applicable.)                                                                                                                                                                                                                                               | Project Manager   | Technical Writer   |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--------------------|
| 12/23/2004 | Manual updated to comply with SOP 192-352 Displaying Sensitive Data                                                                                                                                                                                                                | REDACTED          | REDACTED           |
| 12/11/2006 | Manual updated to reflect additional functionality introduced with Patch SD*5.3*297                                                                                                                                                                                                | REDACTED          | REDACTED           |
| 08/08/2007 | Manual updated to show changes with Patch SD*5.3*483 – 508 Compliant Graphical User  Interface (GUI)                                                                                                                                                                               | REDACTED          | REDACTED           |
| 08/13/2007 | Manual updated to show changes with Patch SD*5.3*498                                                                                                                                                                                                                               | REDACTED          | REDACTED           |
| 09/26/2007 | Manual updated to show changes with Patch SD*5.3*515 – Added Non Primary Care Team set up for OIF OEF Case Management                                                                                                                                                              | REDACTED          | REDACTED           |
| 05/20/2008 | Manual updated to show changes with Patch SD*5.3*499 – Modifications to PCMM NIGHTLY TASK processing.                                                                                                                                                                              | REDACTED          | REDACTED           |
| 10/10/2008 | Manual updated to show changes with Patch SD*5.3*505 – PCMM Phase III Enhancements                                                                                                                                                                                                 | REDACTED          | REDACTED           |
| 01/15/2009 | Manual updated to add elaboration 3.1 regarding transmission errors with Patch SD*5.3*534 – PCMM, PAIT and SCHEDULING FIXES.                                                                                                                                                       | REDACTED          | REDACTED           |
<!-- rpc-table -->
| 04/01/2009 | Manual updated to reflect the SCMC CHECK FTEE RPC has been changed to return a value of 99.1 if non-numeric information is entered in the combo box.                                                                                                                               | REDACTED          | REDACTED           |
| 06/30/2009 | Manual updated to mark /Detailed Patient Assignments – Assigned PC option obsolete with Patch SD*5.3*535 – ASSOCIATED CLINIC, ENROLLMENT PCMM FIXES.                                                                                                                               | REDACTED          | REDACTED           |
| 02/19/2010 | Screen captures edited to comply with SOP 192-352, Displaying Sensitive Data                                                                                                                                                                                                       | REDACTED          | REDACTED           |
| 09/22/2011 | Manual updated with changes from Patch SD*5.3*504                                                                                                                                                                                                                                  | REDACTED          | REDACTED           |
| 06/19/2012 | Manual updated  (p. 8-10) for change made by Patch SD*5.3*539 - ELEC WAIT LIST, PAT APPT INFO TXN, PRIM CARE MGT MOD FIXES                                                                                                                                                         | REDACTED          | REDACTED           |
| 07/24/2012 | Manual updated with changes from Patch SD*5.3*581. It includes PCMM GUI version 1.3.0.27 (508 compliant). Added screenshot for FTEE and Panel Size Report. Added new GUI screenshots and description to Staff/FTEE Tab section. Updated Glossary with FTEE acronym and definition. | REDACTED          | REDACTED           |
| 01/16/2014 | Updated description of the PCMM status bar for patch SD*5.3*607.                                                                                                                                                                                                                   | REDACTED          | REDACTED           |
| 06/2015    | Removed HL7 instructions due to patch SD*5.3*624.                                                                                                                                                                                                                                  | REDACTED          | REDACTED           |

Table of Contents

Introduction	1

Overview of the Primary Care Management Module	1

508 Compliant GUI	2

Sensitive Information	2

Windows Conventions	3

Autolinks - (This functionality has been disabled.)	3

Report Templates	3

Non Primary Care Team set up for OIF OEF Case Management	3

Starting PCMM	5

Toolbar Speed buttons	5

Logging On	6

PCMM Parameters (PCMM Reassignment Mail Group)	6

Background Tasks	6

PCMM Nightly Task	6

HL7 Transmission	7

Inactivation Messages	8

Team Setup	13

Create a New Team	13

Assign Positions to a Team	20

Assign Staff Member to a Position	35

Assign Preceptor to a Position	40

Assign Single Patient to Team/Position(s)	43

Patient Reactivation of an Automatically Inactivated Patient	49

Assign Multiple Patients to Team/Position(s)	50

Reassign Multiple Patients to Team/Position(s)	58

Setting up OIF/OEF Teams	68

Edit an Existing Team	71

Team Setup	71

Position Setup	71

Staff Assignment	72

Single Patient Assignment	74

Creating Autolinks (functionality disabled)	75

Reports	77

Query Template Utility	77

Create a New Template	78

Create a New Template - Report Specifications	79

Modify an Existing Template	80

Printing Reports	81

Template Menu Bar Commands	82

Automated Patient Inactivation from Primary Care Panels Report - GUI	83

Report Descriptions - GUI	85

Reports – Roll and Scroll	86

Patient Reports and Options	87

Provider/Position Reports and Options	100

Team Reports and Options	110

Historical Assignment Reports	116

PCMM HL7 and Maintenance Menu	121

Wait List (Sch/PCMM) Menu	122

Stand-alone Options	123

Mass Team/Position Unassignment	123

Patient Team Position Assignment Review	128

PCMM Nightly Task  [SCMC PCMM NIGHTLY TASK]	129

Retransmit one Patient or Provider	130

Clean-Up Ghost Entries	130

Clean-Up Incorrect Team Institution Pointers	131

Windows Conventions	132

Standard Windows Objects	132

Form Buttons	134

Troubleshooting Guide	136

Inconsistency Descriptions with Detailed Correction Instructions	136

Error Report Window	145

PCMM Business Rules	146

Primary Care Team Business Rules	146

Team Setup	147

Team History	147

Team Position Setup	148

Team Position History	148

Team Position Staff History	149

Patient Team Assignment	149

Patient Team Position Assignment	150

Processing Team Reassignments	150

Processing Position Reassignments	150

Security Key Changes	152

Glossary	154

Appendix - Examples of PCMM Reports	161

Team/Position Assignment/Re-Assignment	161

Patient Listing for Team Assignments	162

Patient Team Position Assignment Review	163

Historical Patient Position Assignment Listing - Detail	164

Historical Patient Position Assignment Listing - Summary	165

Patients Scheduled for Inactivation from PC Panels	166

Patients with Extended Primary Care Inactivation	167

Patients Automated Inactivations from PC Panels	168

Extend Patient Inactivation Date	169

PCMM Edit Practitioner in Position Assig. File	170

Practitioner Demographics	171

Practitioner's Patients	172

Historical Provider Position Assignment Listing	173

PCMM Inconsistency Report	174

FTEE and Panel Size Report	175

Staff Sched for Inactivation	177

Staff Inactivated Report	179

Individual Team Profile	180

Team Member Listing	181

Team Patient Listing	182

Summary Listing of Teams	183

Historical Patient Assignment Detail	184

Historical Provider Position Assignment Listing	185

Historical Patient Position Assignment Listing	186

Historical Team Assignment Summary	187

Index	188

## Introduction

### Overview of the Primary Care Management Module

The Primary Care Management Module (PCMM) was developed to assist VA facilities in implementing primary care. PCMM supports both primary care and non-primary care teams. Teams are groups of staff members organized for a certain purpose. The software allows you to setup and define a team, assign positions to the team, assign staff to the positions, assign patients to the team, assign patients to practitioners, and reassign patients from one team to another team.

Tools are provided with the software to facilitate the startup process. These tools use the site's data (where available) to automate the following tasks:  identify patients to be assigned to primary care; assign patients to teams; assign patients to practitioners via team positions.

As part of PCMM, you are able to control the transmission of MailMan messages to team positions. MailMan messages are categorized into patient death notifications, inpatient notifications, consult notifications, team notifications, and automatic inactivation notifications. For each category, you can elect to have a position get messages for all patients on a team, only patients associated with that team position, or not send messages. You can also elect to have the messages for each category go to the position’s preceptor. A preceptor is a position that acts as a supervisor/monitor for another position.

Numerous reports may be generated. Some of the reports are affected by site parameters. Although many of the reports may be printed through both the roll and scroll interface and the GUI (graphical user interface), most of the reports are only accessed through the roll and scroll interface. Patient-oriented outputs, practitioner-oriented outputs, and team-oriented outputs may be produced.

The *Mass Team/Position Discharge* option provides the ability to discharge large numbers of patients from a team or position at one time. This option is only available through the roll and scroll interface. A confirmation MailMan message is generated from the utilization of this option.

Primary care team/position assignment/unassignment may be accomplished through the GUI interface or through the *Primary Care Team/Posn Assign or Unassign* Scheduling option and through the *PC Assign or Unassign* action in the Appointment Management option.

Every patient must be assigned a primary care provider (PCP). A PCP can be an attending physician (MD or DO), a nurse practitioner (NP), or a physician assistant (PA).

In some instances, a patient may be seen regularly by someone who is not licensed as an independent practitioner per the Health Care Finance Agency (HCFA). For example, an Intern Physician cannot work independently as a PCP, but may be assigned as an “Associate Provider Providing Primary Care (AP/PCP)” in PCMM. When those positions are established, they must be assigned a preceptor. Once a patient assignment is made to a position with a preceptor link, you will not be able to inactivate the link without establishing another.

The PCMM business rules provide information on how some of the PCMM fields will be handled for team and team positions. These rules are not intended to be all encompassing, but to allow basic checking within the system to ensure data integrity.

### 508 Compliant GUI

Section 508 of the Rehabilitation Act Amendments of 1998 requires that when Federal agencies develop, procure, maintain, or use electronic and information technology, they shall ensure that the electronic and information technology allows persons with disabilities to have access to and use of information and data that is comparable to the access to and use of information and data by persons who are not individuals with disabilities, unless an undue burden would be imposed on the agency.

The Section 508 Accessibility Testing and Training Center (T&amp;TC) was consulted and modifications to the GUI have been made to meet the requirements for 508 Compliance. The Primary Care Management Module GUI has been modified to allow screen readers, used by the visually impaired, to accurately interpret information on the screens. As a result, some buttons and boxes have been moved, replaced, or renamed and some screen titles have been modified. Although the developers have made every effort to retain the previous functionality, some functionality may have changed.

For more information on the VA 508 Compliance efforts, please visit the following website REDACTED

### Sensitive Information

To avoid displaying sensitive information regarding our patients and staff, the examples in this manual contain pseudonyms or scrambled data instead of real names. Our patients and staff will be referred to as PCMMPATIENT, ONE, PCMMPROVIDER, ONE, or PCMMUSER, ONE. Scrambled data is a series of random letters that replace a real name like AAADY, JWHTRE. Likewise real social security numbers (SSNs), real addresses and other personal identifiers are not used.

### Windows Conventions

The startup, setup, and assignment functions for PCMM use a graphical user interface (GUI). You may refer to the Windows Conventions Section for an explanation of the windows elements and form buttons used by the module.

### AutoLinks - (This functionality has been disabled.)

Autolinks connect a team with a set of wards, inpatient beds, practitioners, specialties, and clinics. **NOTE:** You cannot assign a patient to a primary care team or practitioner via AutoLinks. Autolinks will be used for inpatient teams by OE/RR.

### Report Templates

The Query Template Utility is provided on the GUI side to create report templates with a specified sort sequence and with specified category selections (divisions, teams, etc.). The templates may then be used to print the reports in the future without having to make sort selections and category selections each time.

### Non Primary Care Team set up for OIF OEF Case Management

In order to track seriously ill Operation Iraqi Freedom/ Operation Enduring Freedom (OIF/OEF) patients, they are assigned to the Transition Patient Advocate (TPA) resource. This is tracked by setting up a non-primary care team with the TPA as a position on the team. Patients identified for this program are assigned to the team. Previously only primary care teams were transmitted to Austin. This feature includes altering how transmissions are screened and transmitted. This non-primary care team information is now transmitted to Austin along with the primary care teams.

For further information, see sections in this manual on Setting up OIF/OEF Team, Team Setup, and Position Setup.


## Starting PCMM

When the Primary Care Module is started, the Menu and Toolbar below is displayed. Select either the FILE|VISTA LOGON menu bar command or the LOGON speed button to start.

Notice the status bar on the bottom of the screen consisting of seven segments. The first segment is used to display status messages when a SAVE action has successfully completed. The second segment indicates whether you are connected (if so, where) or not connected to VistA. The third shows the on/off status of the NUM LOCK key. The fourth displays insert/overwrite status but is not functional at this time. The fifth displays the current PCMM GUI version number.  The sixth displays the current PCMM GUI patch number.  The seventh contains the current time.

<!-- image -->

Click the OPTIONS|PREFERENCES menu bar command – then *Fonts* and/or *Background Colors* if you wish to change the font and/or background color used in the PCMM GUI.

### Toolbar Speed buttons

<!-- image -->

**Close Application**

Disconnects from the network and closes the application. If the network connection is still active, you will get a confirmation request before closing the application.

<!-- image -->

**Connect to/Disconnect from VistA**

Logs on/off the network

<!-- image -->

**Team Setup**

Opens the Select Team dialog box/Primary Care Team Profile form

<!-- image -->

**Position Setup**

Opens the Select Team dialog box/Primary Care Team Position Setup form

<!-- image -->

**Assign Patients**

Opens the Patient Lookup dialog box

<!-- image -->

**Show Associated Help**

Opens the PCMM Help File

### Logging On

When either the File|VISTA Logon menu bar command or the Connect to VistA speed button is clicked, the VistA Sign-on dialog box opens. System information concerning where you are currently working is provided. Enter your access code followed by the tab button. Enter your verify code and click the OK button. (The PCMM option must be assigned to you. If you get a message stating you are not registered to use PCMM, contact your IRM Service.)

### PCMM Parameters (PCMM Reassignment Mail Group)

Clicking the OPTIONS|PCMM PARAMETERS menu bar command opens the PCMM Parameters list box which displays the name of the PCMM Reassignment Mail Group. Members of this group receive the mail messages generated by the reassignment functionality. A new mail group, PCMM REASSIGNMENT, appears as the initial entry in this field.

If you wish to change the mail group, click on the down arrow. The current entry is deleted and a list of possible choices is displayed (a new mail group cannot be created here). Click on the correct entry and then the OK button. A confirmation box appears stating the parameter has been updated. Click the OK button in the confirmation box.

Tasks running in the background create the bulletins that it sends to this mail group

### Background Tasks

PCMM Nightly Task		[SCMC PCMM NIGHTLY TASK]

This task should be scheduled once a day. It reviews Patient Primary Care team position assignments and flags and inactivates patients as follows.

**Step 1**

Determine if the patient is new or established based on the length of time the patient has been assigned to the PCP position; if assigned to the position 12 months or less, then NEW; if assigned to the position more than 12 months, then ESTABLISHED.

All providers assigned to a particular position are evaluated. In this way any encounter kept for any of those providers (within their activity on the position) would count. The following rules apply.

- The same provider can be assigned, unassigned, assigned again, etc. Several segments of a local array are created for the same provider, if assigned more than once.
    - If a patient is assigned to PC position, and a provider assigned to that position has a preceptor, then all appointments for that patient have to be matched with both the provider (preceptee) from the PC position the patient is assigned to and with the preceptor provider as well. The range of days to be evaluated for the preceptor, if any, will be the same as identified for the PC provider.
        - If a patient is assigned to the PC preceptor position then only the provider(s) assigned to that position is (are) evaluated. The preceptor can have multiple preceptees assigned to the related positions, but it is not realistic to evaluate all of them.
    **Step 2**
    If a patient is NEW and it is the 11th month since being assigned to the position, check to see if the patient has any prior encounters with the PCP/APs in the preceding 11 months + 7 days and, if no encounters, flag for inactivation. Note that the look back should be for an encounter with any person that occupied the PCP/AP positions in the past 11 months + 7 days.  On month 12, if still no encounters with PCP/AP in the preceding 12 months + 7 days, inactivate. The 7 days’ time period will take into account the fact that the provider often sees the patient and then a day or two later assigns them to their panel.
    **Step 3**
    If a patient is ESTABLISHED, check to see if the patient has had any prior encounters with the PCP/AP in the preceding 23 months + 7 days and, if no encounters, flag for inactivation. On month 24, if still no encounters with PCP/AP in the preceding 24 months + 7 days, inactivate. Again, check for encounters with any persons that occupied the PCP/AP positions in the last 24 months + 7 days.**Note:** Inactivation will take place either on the 15th or last day of the month, immediately after the calculated inactivation.
    Flagging and unflagging patients for inactivation will take place each time SCMC PCMM NIGHTLY TASK is running. If any patients are flagged, then in addition to the current email messaging functionality, a message with the Subject line "Patient Scheduled for Inactivation from Primary Care Panel" will be sent to the PCMM PATIENT/PROVIDER INACTIVE Mail Group.
    This task also identifies staff members who are improperly assigned as Primary Care Providers (PCP). See Inactivation Messages section for examples of the types of bulletins that are sent.
    HL7 Transmission	 		[SCMC HL7 TRANSMISSION]
    Menu placed out of order.

### Inactivation Messages

Inactivation messages are addressed to the PCMM PATIENT/PROVIDER INACTIVE mail group. PCMM Coordinators and others who will be monitoring inactivation should have membership in this group. Examples of the five Bulletins are provided on the following pages.

**Patients Scheduled for Inactivation from Primary Care Panel**

Subj: Patients Scheduled for Inactivation from PC Panel  [#5404]

12/20/05@09:43  33 lines

From: POSTMASTER  In 'IN' basket.   Page 1

-------------------------------------------------------------------------------

Patients scheduled for inactivation from their Primary Care team and

Primary Care Provider assignments appear below.

Flagging of primary care patients from a PCMM panel occurs each time this

Inactivation Task is run.

All providers assigned to a particular position are evaluated.

If a patient is assigned to a PC position and the provider assigned to that

position has a preceptor all encounters for the patient will be checked for

matches with either the provider (preceptee)assigned to that position or

the provider (preceptor) assigned as preceptor to that position.

If a patient is assigned to the PC preceptor position then only the encounters

with the provider assigned as preceptor will be evaluated.

(a) If a patient is NEW and it is the 11th month since being assigned to

the position, and the patient had no prior encounters with the PCP/APs in

the preceding 11 months + 7 days then the patient is flagged

for inactivation.

(b) If a patient is ESTABLISHED and if the patient had no prior encounters

with the PCP/AP in the preceding 23 months + 7 days the patient

is flagged for inactivation.

Inactivation will occur on the fifteenth and the last day of the month

unless the patient has a completed appointment encounter with their current

Primary Care Provider (PCP) or their Associate Primary Care Provider (AP)

before that date. The patient may be reactivated to their previous PCP and PC

team if they return for care.

This message is generated each time when at least one new occurrence of

flagging for inactivation takes place, and unconditionally on the 15th and

the last day of a month.

Patients scheduled for Inactivation from Primary Care panels

Date

Scheduled

Patient Name         SSN   Provider               Team        for Inactivation

------------------------------------------------------------------------------

INSTITUTION: ABCD VAMC

PCMMPATIENT, ONE     2222  PCMMPROVIDER, EIGHT    BLUE TEAM   04/29/06

PCMMPATIENT, TWO     5555  PCMMPROVIDER, ELEVEN   BLUE TEAM   04/29/06

Enter message action (in IN basket): Ignore//

**Patients with Extended PCMM Inactivation Dates**

Subj: Patients With Extended PCMM Inactivation Dates  [#5405] 12/20/05@09:43

39 lines

From: POSTMASTER  In 'IN' basket.   Page 1

-------------------------------------------------------------------------------

By using the Extend Patient Inactivation Date option, these patients'

PCMM inactivation dates are now 60 days from their original inactivation date.

Inactivation occurs on the fifteenth and the last day of the month, unless

the patient has a completed appointment encounter with their current

Primary Care Provider (PCP) or their Associate Primary Care Provider (AP)

before that date. The patient may be reactivated to their previous PCP and PC

team if they return for care.

Patients with Extended PCMM Inactivation Dates

Date

Scheduled for

Patient Name         SSN  Provider             Team        Inactivation

------------------------------------------------------------------------------

INSTITUTION: ABCD VAMC

PCMMPATIENT, FOUR    9999 PCMMPROVIDER, SEVEN  BLUE TEAM   04/12/06

Enter message action (in IN basket): Ignore//

**Patients Automated Inactivations from Primary Care Panels**

Subj: Patients Automated Inactivations from PC Panels  [#5406]

12/20/05@09:43  965 lines

From: POSTMASTER  In 'IN' basket.   Page 1

-------------------------------------------------------------------------------

Patients inactivated from their Primary Care team and Primary Care Provider

assignments appear below.

Inactivation occurs on the fifteenth and the last day of a month, unless

the patient has a completed appointment encounter with their current

Primary Care Provider (PCP) or their Associate Primary Care Provider (AP)

before that date.

Inactivation of primary care patients from a PCMM panel occurs under

the following circumstances:

(a) The patient expires

(b) Newly assigned patients (either newly-enrolled patients or patients who

have been re-assigned to a different provider) who have not been seen by

their PCP or Associate Provider (AP) and 12 months have passed since the

time of assignment to that provider.  This provides every PCP a 1-year grace

period for seeing patients added to their panel (either newly-enrolled

patients or patients transferred from a different panel) before they are

inactivated. Patients must be seen by their PCP or AP within 12 months +7 days

of being assigned, or they need to be inactivated from the PCP's panel.

(c) Established patients that have been assigned to the PCP's panel for more

than 12 months, but have not been seen by their PCP or AP in the past

24 months +7 days need to be inactivated.

The patient may be reactivated to their previous PCP and PC team if they

return for care.

Patients Automated Inactivation from Primary Care Panels

Date        Reason

Patient     Patient

Patient Name         SSN  Provider              Team       Inact       Inact

-------------------------------------------------------------------------------

INSTITUTION: TEST VAMC

PCMMPATIENT,ONE      9736 PCMMPROVIDER,ONE      TEST TEAM  08/08/05    NO APPT

PCMMPATIENT,NINETY   5894 PCMMPROVIDER,THIRTY   TEST TEAM  05/17/04    DECEASED

Enter message action (in IN basket): Ignore//

**Primary Care Providers Scheduled for Inactivation**

Subj: Primary Care Providers Scheduled for Inactivation  [#5408] 12/20/05@09:44

64 lines

From: POSTMASTER  In 'IN' basket.   Page 1

-------------------------------------------------------------------------------

WARNING- The following primary care staff will be automatically

inactivated in PCMM software if a correct 'Person Class' and

'Provider Type' are not entered in the New Person File (#200) or

their role and position in the 'Position Setup' window is not

corrected to correspond with their 'Provider Type', 'Person

Class' and the Primary Care business rules stated below:

1. Staff designated as Primary Care Providers (PCPs) in PCMM that

are not an Attending physician (Attending MD or Attending DO), NP

or PA, shall be inactivated from PCMM

2. Staff designated as Associate Providers (APs) in PCMM, that are not

a Resident/Intern (Physician), NP or PA shall be inactivated in

PCMM

3. All persons designated as an Associate Provider or Primary Care

Provider, who do not have the correct 'Provider Type' and 'Person

Class' entered in the New Person file (#200) in VistA, shall be

inactivated from their Primary Care positions in PCMM six months

after installation of patch SD*5.3*297 Date: JUL 12,2006.

4. Please contact your PCMM Coordinator or Information Systems

to correct these problems

PRIMARY CARE PROVIDERS SCHEDULED FOR INACTIVATION

Provider's     Assoc     Team                      Person    # of Pts  Sch Inac

Name           Clinics   Position   Role           Class     Assigned  Date

-------------------------------------------------------------------------------

INSTITUTION: TEST VAMC

PCMMPROVIDER,ONE        INT AP INT INTERN (PHYSIC Allopathic and 2    01/31/06

PCMMPROVIDER,SIX        INT AP ADM ADMIN COORDINA Allopathic and 0    01/31/06

PCMMPROVIDER,TEN        PHYS AS AD ADMIN COORDINA Physicians (M. 0    01/31/06

Enter message action (in IN basket): Ignore//

**Primary Care Providers Inactivated**

Subj: Primary Care Providers Inactivated  [#5526] 12/20/05@10:28  6 lines

From: POSTMASTER  In 'IN' basket.   Page 1

-------------------------------------------------------------------------------

PRIMARY CARE PROVIDERS INACTIVATED

Provider's     Assoc     Team                      Person    # of Pts  Inac

Name           Clinics   Position   Role           Class     Assigned  Date

-------------------------------------------------------------------------------

Enter message action (in IN basket): Ignore//


## Team Setup

### Create a New Team

<!-- image -->

**1** . Click on the Team Setup toolbar speed button  or select the TEAM|SETUP menu bar command.

<!-- image -->

**Select Team Dialog Box Information**

Click on the desired entry to highlight it, and then click on the **OK** button to select. Clicking on **Cancel** closes the dialog box without selecting an entry. The scrollbar can be used to move up and down the list to find the desired entry. The **Find** button can be used to find a specific entry. If more than one match is found, the list box will clear and only the matching entries will be displayed. The **New** button allows you to enter a new team name. After entering the name, click on the OK button within the New Team dialog box.

**NOTES**

Names are saved in all uppercase letters.

If the TEAM/ACTIVE ONLY menu bar command is selected, only active teams appear for selection.

**2** . Click the New button of the Select Team dialog box and enter the new team name (3-30 characters).

**Create a New Team**

<!-- image -->

**3** . The Primary Care Team Profile form appears. When initially setting up a team, information should be entered on the General and Settings tabs before clicking the SAVE button to store the data.

**Note:** Required fields are signified in this documentation by an asterisk ***** next to the field name. If all required fields are not completed, the SAVE button will not be enabled and you will not be able to save the information.

You may refer to the Windows Conventions Section for an explanation of the standard windows objects (i.e., list box, lookup box, etc.) and form buttons.

**4** . Enter the team information on the General and Settings tabs. (See following pages). When creating a new team, data entry is not required on the History tab. The History tab will not be available for a new team until the initial entry is saved.

After you have entered all required data for the new team, click the SAVE button.

**5** . The popup calendar appears. Click on the date you wish to enter as the team activation date and click OK. The team has now been established.

<!-- image -->

If you wish to create positions on the team at this time, go back to the General Tab and click on the POSITIONS button. See the “Assign Positions to a Team” section under Team Setup for instructions.

**Create a New Team**

**primary Care Team Profile Screen**

**General Tab**

<!-- image -->

***Field Descriptions***

*Name (text box)

The name of the team, 3-30 characters in length. If the new team name matches an existing team name, you will be so notified and asked for a different name.

Phone Number (text box)

Enter a phone number for the team, 3-20 characters.

Description (text box)

Any descriptive information specific to the team.

Current Activation (Label)

This label field displays the most recent activation date for the team.

Current Inactivation (Label)

This label field displays the most recent inactivation date for the team.

Positions (button)

This button takes you to the Team Positions Setup Screen.

Autolinks (button) (FUNCTIONALITY DISABLED)

**Create a New Team**

**primary Care Team Profile Screen**

**Settings Tab**

<!-- image -->

***Field Descriptions***

*Purpose (drop down list)

The Purpose defines the role of the team. Primary care would be the usual choice but other kinds of teams may include Inpatient Ward, Community Care, etc.

*Service (lookup box)

This is the medical center service most closely associated with the team. It is an entry from the SERVICE file (#49) and includes clinical and non-clinical services.

*Institution (lookup box)

This is the entry from the INSTITUTION file (#4) associated with the team. It includes VA and non-VA institutions.

**NOTE:** Each division at a multidivisional facility has its own entry in the INSTITUTION file.

Default Team Printer (lookup box)

The PCMM reports do not use this field.

**Create a New Team**

Primary Care Team Profile Screen - Settings Tab

Primary Care Team (check box)

Click in this box if this team can be the primary care team for any patient. Even if the team's purpose is not primary care, it still may be able to act as a primary care team. Only a team that can act as a primary care team may have a primary care practitioner position assigned to it.

Restrict Consults (check box)

Click in this box to prevent users from making consult appointments to clinics in which this team's patients are not enrolled. Patients who are listed as “restrict consults” may only be enrolled in a new clinic if the user has the SC CONSULT security key. Consult appointments (an appointment where the patient is not enrolled in the clinic) may only be done via the Make Consult Appointment option. A MailMan message will be generated whenever a patient whose consults are restricted receives a consult appointment or is enrolled in a new clinic.

Team Closed (check box)

Click in this box to close the team. Additional patients should not be added to a team if it is designated as closed.

Auto-Assign to Team from Clinic (check box)

Click in this box to automatically assign the patient to a team when he is enrolled in a clinic that is an "associated clinic" of one of the team's positions. This will occur only if the associated clinic is unique to one team. It is recommended that **both** the Auto-Assign and Auto-Discharge boxes be checked or **neither** be checked.

Auto-Discharge from Team from Clinic (check box)

Click in this box to automatically discharge the patient from a team when he is discharged from a clinic that is an "associated clinic" of one of the team's positions. This will occur only if the patient has not been assigned to a team position.

Team Assignments (text box)

Allowed (numeric display)

This is the maximum number of patients that should be assigned to this team. Users are not prevented from adding additional patients to the team after the team's patient panel (list of patients) has reached this number. You should compare the current number of team assignments with the number allowed to balance team panel sizes.

Actual (numeric display)

This is the number of patients currently assigned to this team.

**Create a New Team**

**primary Care Team Profile Screen**

**History Tab**

When creating a new team, no data entry is required on this tab.

<!-- image -->

***Field Descriptions***

History Entries (list box)

This display shows the history of status change dates for this team. Double clicking an entry **or** highlighting an entry and pressing the spacebar displays that entry’s data in the edit boxes. A check mark next to an entry in the box indicates an activation date while the circle indicates an inactivation date.

*Effective Date

This is the date the status change will be effective. You may type the date in the date field, use the arrows, or double click in the edit box to drop down a calendar for date selection. Each component of the date (month/day/year) must consist of two characters (i.e., 02/22/96).

*Status (drop down list)

This is the status of the team as of the effective date.

**Create a New Team**

**Primary Care Team Profile Screen - History Tab**

*Reason (drop down list)

This is the reason for the change in the team's status.

OK (button)

Click OK to save changes.

Cancel (button)

Click Cancel to abort changes.

ADD History Entry (button)

Click ADD History Event to make changes in the activation/inactivation history.

### Assign Positions to a Team

**Note:** The procedure for creating a resident position that is an associate provider has changed due to the fact the application now enforces the business rule regarding residents as PCPs. Note that before a resident position can be created as a PCP associate provider, the resident position must have a staff member assigned to the resident position and a preceptor assigned to the resident. To create a resident position, follow the steps in the Creating a Resident Position section which follows.

**Creating a Team Position - General Instructions**

*If you have clicked on the Positions button on the General Tab of the Primary Care Team Profile form, begin at Step 3.*

**1** . Select the TEAM|POSITIONS menu bar command.

**2** . Select the team from the Select Team dialog box and click the OK button. Note that you cannot add a new position to an inactive team.

**3** . When the Primary Care Team Position Setup form appears, click Add New Position and the New Position dialog box appears. Enter the name of the new position and click OK. Positions that can act as preceptors should be created first so that they will exist for the team.

**4** . Enter the position information on the General, Settings, and Messages tabs (see following pages.) When initially creating a position, you must save the General tab information first before entering information in the other tabs. Information should then be entered in the General, Settings, and Messages tabs and click the SAVE button to store the data. No data entry is required on the History tab when creating a new position. All data displayed in the edit boxes applies to the position displayed in the forms header.

**5** . Required fields are signified in this documentation by an asterisk ***** next to the field name. You will not be allowed to save until all required fields have been completed. After you have entered all required data for the new position and clicked the SAVE button, this popup calendar appears. Click on the date you wish to enter as the position activation date and click OK. The position has now been established.

Position history record is automatically deleted if you click the Cancel button on the Enter Position Activation Date window when creating a new position.

<!-- image -->

**Assign Positions to a Team**

If you wish to assign a staff member to the position at this time, click on the STAFF button. See the “Assign Staff Member to a Position” section under Team Setup for instructions.

**Creating a Resident Position**

1. Click Add New Position to create team position and enter the Position, Role, and Description. Click Save to save the position.

1. Assign staff to the position:  Click Staff tab then click Assign button.

1. At the Staff lookup window, enter the last name of a Resident and click Search. A list of names will appear that match the last name you searched for. Click on the desired name and click OK to select it.

1. Enter the Effective date if necessary (it defaults to today's date), enter the Status if necessary, and Status Reason if necessary. Do not enter FTEE at this time. Click Save to save position.  Because a Resident can't be a PCP unless precepted, you will need to set up a Preceptor before you will be able to enter FTEE.

1. Click Preceptor tab, then click Assign and select a Preceptor for this resident. Click Save to save preceptor. A NP or PA cannot be assigned as a preceptor for a resident (or intern).

1. Click Settings tab, and click "Provides Primary Care as an Associate Primary Care Provider".

1. Enter the number of patients allowed for this position and click Save to save Settings.

1. Now you can enter the FTEE for this position. Click Staff/FTEE button. Click in FTEE edit box and enter the FTEE for this resident. Click Save.

**Assign Positions to a Team**

**Primary Care Team Position Setup Screen**

<!-- image -->

Features of the Primary Care Team Position Setup Screen

- Shows active/inactive team positions
- Displays role, staff name, PCP status, preceptor status, position status, and FTEE
- Central Save/Cancel buttons used to save all changes regardless of which tab user is on
- Selected team position highlighted as user navigates through tabs
- *Team Selected* dropdown list allows users to change teams without closing this screen
- Allows sorting of positions by 7 column headings – to activate a sort, place cursor at the column heading and click

**Assign Positions to a Team**

**Primary Care Team Position Setup Screen**

***Field Descriptions***

**Team Selected**

Displays the name of the current team you are working on. To change teams, click the drop down box and select another team name.

**Team Positions (list box)**

Displays team positions. The list box shows all team positions or only those currently active based on the Positions to Show selection. In order to select a position listed in the Team Positions list box, click on the entry **or** click the entry and press the spacebar.

**Show Active Only, Show All Positions (radio button)**

You may choose to show all positions associated with this team or only the currently active positions.

**Assign Positions to a Team**

**Primary Care Team Position Setup Screen**

**General Tab**

<!-- image -->

Position (text box)

The name of the position, 3-30 characters in length. If the new position name matches an existing position name on the current team, you will be so notified and asked for a different name.

Role (drop down list)

This is a list of standard roles to which the position is mapped.

Description (text box)

Descriptive information you may wish to add specific to the position.

Beeper (text box)

Beeper number for this position. This is a separate free text field. It is not linked to any other beeper or phone numbers in VistA.

**Assign Positions to a Team**

**Primary Care Team Position Setup Screen** - **General Tab**

Position Current Information (label)

Activation/Inactivation Date

These label fields may display the most recent activation/inactivation date for the selected position.

**Preceptor Position Name**

A preceptor is a position that acts as a supervisor/monitor for this position.

**Note:** *Physician Attending* is displayed when the highlighted physician is also a preceptor.

**Assign Positions to a Team**

**Primary Care Team Position Setup Screen**

**Settings Tab**

<!-- image -->

**NOTE:** If a provider other than an Attending, Resident/ Intern, PA or NP is selected, both boxes A and B will **not** be selectable.

Box “Allowed” under Patient for Position” is selectable for any position but its entry is required for the PCP staffed position and optional for other position.

***Field Descriptions***

**Provides Primary Care (check box)**

Only a Resident/Intern, NP, or PA shall be designated as an “Associate Provider” providing primary care.

**Precepts Associate Primary Care Providers (check box)**

Only an attending physician (MD or DO), NP, or PA can be designated a Precept to Associate Primary Care Providers.

**Assign Positions to a Team**

**Primary Care Team Position Setup Screen - Settings Tab**

Patients for Position (text box)

Allowed

The number of patients that should be assigned to this position. Users are not prevented from exceeding this number. It is required that you enter a value here before you can save Resident/Intern, NP, or PA as Primary Care Provider. Entry for all other positions that are not PCP ones are optional.

Actual

This is the number of patients that are currently assigned to this position.

User Class (lookup box)

This is the user class that must be used when selecting an individual to fill this position.

This field may be disabled at some sites.

See documentation for Staff/FTEE Tab in the Assign Staff Member to a Position section.

See documentation for the Preceptor/Preceptee Tab in the Assign Preceptor to a Position section.

**Assign Positions to a Team**

**Primary Care Team Position Setup Screen**

**Associated Clinics Tab**

<!-- image -->

If there is an existing clinic you wish to associate with this position, it should be entered here. The application provides for entering and saving multiple associated clinics for primary care providers and for associate primary care providers. The associated clinics will print on all PCMM reports with an associated clinic column or field.

The entire name of the associated clinic is displayed and remains on display after saving changes.

**Assign Positions to a Team**

**Primary Care Team Position Setup Screen**

**Messages Tab**

<!-- image -->

As part of PCMM, you are able to control the transmission of MailMan messages to team positions. MailMan messages are categorized into patient death, inpatient activity, consult activity, and team activity. Check the appropriate button/box for each type of notification.

When creating a new position, be sure to click the SAVE button after data entry on this tab to store all the information you have entered here and on the previous two tabs.

**Assign Positions to a Team**

**Primary Care Team Position Setup Screen - Messages Tab**

***Field Descriptions***

Death Notifications

Will notify the recipient of entry/deletion of the DATE OF DEATH field for a patient

Inpatient Notifications

Will notify the recipient of an inpatient admission/transfer/discharge for a patient

Consult Notifications

Will notify the recipient of either an appointment being made or enrollment in a clinic in which the patient was not previously enrolled

Team Notifications

Will notify the recipient of a patient's team activity (assignment, discharge, etc.)

**Automatic Inactivation Notifications**

The software automatically checks the “Do Not Send” option of the “Automatic Inactivations Notifications” line for all active positions in PCMM.

***Button Descriptions***

Team

If checked, the position will receive messages that are generated for all the team's patients.

Position

If checked, the position will receive messages that are generated only for those patients in the team associated with the position.

Do Not Send

If checked, the position will not receive messages.

***Checkbox Description***

**Preceptor**

For each activity type - if checked, will add the position preceptor to the recipient list. The boxes will be disabled for preceptor positions.

**Assign Positions to a Team**

**Primary Care Team Position Setup Screen**

**History Tab**

When creating a new position, no data entry is required on this tab. The History Tab will not be available for a new position until the initial entry is saved.

<!-- image -->

***Field Descriptions***

History Entries (list box)

This display shows the history of status change dates for this position. A check mark next to an entry in the box indicates an activation date while the circle indicates an inactivation date.

**Assign Positions to a Team**

**Primary Care Team Position Setup Screen - History Tab**

*Effective Date

This is the date the status change will be effective. You may type the date in the date field, use the arrows, or double click in the edit box to drop down a calendar for date selection. Each component of the date (month/day/year) must consist of two characters (i.e., 02/02/96).

*Status (drop down list)

This is the status of the position as of the effective date.

*Reason (drop down list)

This is the reason for the change in the position's status.

Save (button)

Click Save to save changes.

Cancel (button)

Click Cancel to abort changes.

Add Entry (button)

Click Add Entry to make changes in the activation/inactivation history.

**NOTE:** If you attempt to inactive a position that has members assigned, you will get this warning screen.

<!-- image -->

**Assign Positions to a Team**

**Primary Care Team Position Setup Screen**

**Patients Tab**

<!-- image -->

The Patients Tab displays a list of all patients assigned to the team or selected position. The total number of patients assigned to the team/position is provided as well as search capability for a particular patient.

**Assign Positions to a Team**

**Primary Care Team Position Setup Screen**

**Patients Tab**

***Field Descriptions***

**Search For: (lookup box)**

Type the first three letters of the patient’s last name in the box and press the Search button.

**Show (radio button)**

Displays all patients assigned to the team or only those patients assigned to the selected position depending on which radio button is checked.

**Print (button)**

Allows for printing of the patient list.

### Assign Staff Member to a Position

***(For positions that are NOT part of a preceptor link)***

*If you have clicked on the Staff button on the Primary Care Team Position Setup form, begin at Step 4.  NOTE: You may also assign staff from the Team Position screen’s Staff/FTEE tab.*

**1** . Select the TEAM|ASSIGN STAFF menu bar command.

**2** . Select the team from the Select Team dialog box and click the OK button.

**3** . Select the position and click OK.

**4** . The Staff Assignment Add/Edit form appears. Click the ASSIGN button **or** choose the EDIT|ASSIGN MEMBER menu bar command.

**5** . The Staff Lookup dialog box appears. Type the staff member name (last, first) and click the SEARCH button. Possible matches appear in the list box. Make your selection and click OK. If the User Classification appears as part of the title bar, you may type a question mark in the lookup box for a listing of all available entries in that User Class. Only names of staff members assigned to that User Class will appear. If the User Class is turned off at your site, any staff member may be selected.

**6** . Enter FTEE for this position. It is required for a Primary Care Provider but optional for other staffed position.

**7** . The data fields on the Staff Assignment Add/Edit form will now be filled in. Click the SAVE button to accept these values, if correct. Close the form.

**8** . To inactivate the current assignment, click the INACTIVATE button **or** choose the EDIT|INACTIVATE CURRENT ASSIGNMENT menu bar command. Click the SAVE button.

**Assign Staff Member to a Position**

***(For positions that ARE part of a preceptor link)***

**1** . Select the TEAM|POSITIONS menu bar command.

**2** . Select the team from the Select Team dialog box and click the OK button.

**3** . Select the position from the Primary Care Team Position Setup form and click the STAFF tab.

**4** . The Staff Assignment Add/Edit section appears. Click the Add Staff button.

**5** . The Staff Lookup dialog box appears. Type the staff member name (last, first) and click the SEARCH button. Possible matches appear in the list box. Make your selection and click OK. If the User Classification appears as part of the title bar, you may type a question mark in the lookup box for a listing of all available entries in that User Class. Only names of staff members assigned to that User Class will appear. If the User Class is turned off at your site, any staff member may be selected. Staff members currently assigned to preceptor or precepted positions on the team may not be selectable depending on the type of position to which an assignment is being made.

**6.** Enter FTEE for this position if it is for a Primary Care Provider. Entry for other positions is optional. NOTE:  On Resident or other positions which need a preceptor, the position must be staffed and have a preceptor assigned before the FTEE field will be enabled.

**7** . The data fields on the Staff Assignment Add/Edit form will now be filled in. Click the SAVE button to accept these values, if correct.

**8** . To inactivate the current assignment, click the INACTIVATE button **or** choose the EDIT|INACTIVATE CURRENT ASSIGNMENT menu bar command. Click the SAVE button. If you inactivate a staff assignment for a position that is a current preceptor for another position and attempt to close the Staff Assignment Add/Edit form without creating a current staff assignment, your inactivation change will not be saved.

**Assign Staff Member to a Position**

**Primary Care Team Position Setup Screen**

**Staff/FTEE Tab**

<!-- image -->

When staff, positions, or teams are inactivated, they automatically default to T-1 (today minus one day).

A Non-primary care provider position or a position on a non-primary care team is not required to enter FTEE when originally staffed.

FTEE entered on any staffed position cannot be removed, but can be changed to another value when accepted. A staffed position with FTEE entered can have the value deleted if the person is INACTIVATED. This position can be populated with FTEE again after the position is staffed.

***Field Descriptions***

Effective Date

This is the date the status change will be effective. You may type the date in the date field, use the arrows, or double click in the edit box to drop down a calendar for date selection. Each component of the date must consist of two characters (i.e., 03/16/12).

**Assign Staff Member to a Position**

**Primary Care Team Position Setup Screen - Staff/FTEE Tab**

Status (drop down list)

This is the status of the staff member as of the effective date.

Status Reason (drop down list)

This is the reason for the change in the staff member's status.

**FTEE (Full-time Employee Equivalent)**

This is the decimal equivalent of the amount of time this position devotes to Patient Care. Entry of 0 for any staffed position is not allowed.

Staff Assignment History (list box)

This display shows the history of staff member assignment dates for the selected position. The displayed columns are Status (Active/Inactive), Date (date the position was Active/Inactive), and Staff Name. The last assignment date can be deleted using a right mouse click.

Add Staff (button)

Click on the Add Staff button to add a provider to this position. This will open the Staff Lookup Screen.

<!-- image -->

Type the first three letters of the provider’s last name in the Staff Lookup box and press the Search button. Select a provider from the list and click OK.

**Assign Staff Member to a Position**

**Primary Care Team Position Setup Screen - Staff/FTEE Tab**

<!-- image -->

***NOTE:** PCMM prevents entry and transmission of provider FTEE values greater than one to AITC. The total FTEE for any role cannot be greater than one within an institution or within institutions with the same first three digits of the institution number. Entry of non-numeric data in the FTEE box will return a value of 99.1 when evaluated for FTEE compliance.

### Assign Preceptor to a Position

**Note:** A staff member must be assigned to the preceptor position before a preceptor assignment can be made. Only positions eligible to be assigned a preceptor can have a preceptor assigned. The Add Preceptor button will be disabled if the position is not staffed or does not have the proper role to have a preceptor assigned. See the Business Rules section of this document for more information about preceptors.

**1.** Select the Team|Positions menu bar command.

**2.** Select the team from the Select Team dialog box and click the OK button.

**3.** Select the position from the Primary Care Team Position Setup screen. Click the Preceptor tab.

**4** . Click the Add Preceptor button.

**5** . The Select Preceptor Position dialog box appears. Click on the desired preceptor position then click OK. Only names of designated preceptor positions for the current team will be available for selection.

**6.** The data fields on the Preceptor Assignment Add/Edit form will now be filled in. Click the SAVE button to accept these values, if correct.

**7** . To inactivate the current assignment, click the INACTIVATE button. Click the SAVE button. If you inactivate a preceptor for a position with current or future patient assignments and attempt to close the Preceptor Assignment Add/Edit form without creating a current preceptor assignment, your inactivation change will not be saved.

**Assign Preceptor to a Position**

**Primary Care Team Position Setup Screen**

**Preceptor/Preceptee Tab**

<!-- image -->

A Preceptors/Preceptees Tab has been added to the Primary Care Team Position Setup screen to display the preceptor for a position, or if the position is a preceptor, it displays a list of preceptees.

Preceptees may be reassigned to another preceptor so that a particular preceptor may be deactivated.

A preceptor position may be changed to a non-preceptor position as long as the preceptor does not have preceptees assigned to him/her and no patients are assigned to that position.

**Assign Preceptor to a Position**

**Primary Care Team Position Setup Screen – Preceptor/Preceptee Tab**

***Field Descriptions***

*Effective Date

This is the date the status change will be effective. You may type the date in the date field, use the arrows, or double click in the edit box to drop down a calendar for date selection. Each component of the date must consist of two characters (i.e., 02/22/96).

*Status (drop down list)

This is the status of the preceptor position assignment as of the effective date.

*Status Reason (drop down list)

This is the reason for the change in the preceptor position assignment status.

Preceptor Assignment History (list box)

This display shows the history of preceptor position assignment dates for the selected position. Double clicking an entry **or** clicking an entry and pressing the spacebar displays that entry's data in the edit boxes. A check mark next to an entry in the box indicates an activation date while the circle indicates an inactivation date.

Add Preceptor (button)

Clicking the Add Preceptor button will open the Select Preceptor Position screen.

<!-- image -->

Select the desired preceptor from the list of Preceptors and click OK. This will activate the Preceptor Link.

### Assign Single Patient to Team/Position(s)

<!-- image -->

**1** . Click on the Assign Patients toolbar speed button or select the PATIENT|PATIENT ASSIGNMENT menu bar command.

<!-- image -->

**2** . The Patient Lookup dialog box appears. Type the patient name (last, first) and click the SEARCH button. If there is more than one match, possible matches will appear in the list box. Double click your selection **or** single click then click the SELECT button. Employee patients will display “sensitive” in the DOB and SSN columns. Accessing a sensitive patient record can trigger messages and bulletins being sent. If there is another patient with the same last name and same last four digits of the SSN as the selected patient, a warning message will appear to ensure you have selected the correct patient. If the selected patient requires a Means Test, a message will be displayed.

**Assign Single Patient to Team/Position(s)**

<!-- image -->

**3** . The Select Patient-Team Assignment screen appears. Based on whether or not the Show All Team Assignments menu bar command is selected, all team assignments or only current assignments will appear in the list box. All team assignments are displayed as the default. An asterisk in the PC column indicates the primary care team for this patient. Click the ASSIGN TEAM button and then select the team to which you wish to assign the patient.

A patient may be assigned to more than one panel on a given day as long as the patient un-assignment from all other primary care provider panels is completed on the same day.

**4** . The Team - Position Assignments screen appears. On the Team Assignment tab, check the Primary Care Team and Restrict Consults check boxes as appropriate. Change the Date Assigned if necessary. Click the SAVE button. Enter the information on the Position Assignments tab (see Position AssignmentS Tab).

**Assign Single Patient to Team/Position(s)**

**Team – Position Assignments Screen**

**Team Assignment Tab**

<!-- image -->

***Field Descriptions***

Dates

*Assigned

The date the patient is assigned to the team. Default will be today.

Discharged

The date the patient is discharged from the team.

Discharge Reason (Drop down list)

Click this to select a reason when discharging a patient. **NOTE:** Automatic reasons (Deceased and Automatic Inactivation) are set during automatic discharges and are not selectable by the user.

Primary Care Team for this Patient? (Check box)

Check this box if this team will be the primary care team for this patient. Patients may have only one team designated as their primary care team.

Patient Has Multiple PCPs (Check box)

Check this box if the patient is allowed to have multiple PCPs. Be sure to follow the Business Rules for allowing multiple PCPS.

Restrict Consults for this Patient? (Check box)

Check this box if you wish to restrict consults for this particular patient. This is only applicable to teams where consults are not restricted for the entire team.

**Assign Single Patient to Team/Position(s)**

**Team – Position Assignments Screen**

**Position Assignments Tab**

<!-- image -->

The Position Assignments tab displays existing assignments to positions on the selected team. The PC column will contain an asterisk to identify primary care provider positions and an x to identify associate provider positions. Other data provided includes position name, standard role, staff member, and whether or not the position can act as a preceptor.

**1** . Click the ASSIGN button. From the Select Position dialog box, choose the position you are assigning the patient to and click OK.

<!-- image -->

**Assign Single Patient to Team/Position(s)**

**Team – Position Assignments Screen - Position Assignments Tab**

**2** . The Position Information dialog box appears. Edit the assignment date and position type, if necessary. Click OK. Then click the SAVE button on the Position Assignments tab.

If the position has been associated with a clinic and the patient is not already enrolled there, you will now be asked if you want to enroll the patient in that clinic. If you answer YES, you will be asked if this is an outpatient enrollment. If you answer NO to outpatient enrollment, the enrollment will automatically be an ambulatory care enrollment.

**3** . If you wish to assign this patient to another position on this team, click the right mouse button and select “new position”. See Step 2.

<!-- image -->

*assignment Dates

Enter the date you are assigning the patient to the position.

Position Type

Primary Care Assignment? (check box)

Check the box if this is a primary care assignment.

**Assign Single Patient to Team/Position(s)**

**Team – Position Assignments Screen - Position Assignments Tab**

<!-- image -->

### Patient Reactivation of an Automatically Inactivated Patient

The Reactivate button will be enabled if the patient had an automatic inactivation by the system. It is provided for easy reactivation of a patient to their previous team and position.

<!-- image -->

1. Click Reactivate button.
2. A message box will appear showing the previously deactivated team and position and will confirm that you would like to reactivate the patient to the previous team and position (see image below).

<!-- image -->

**3.** Click Yes to confirm and reactivate the patient. This reactivates the original team and position assignment, keeping the original assigned date and removing the discharged date to reactivate the old assignment.

### Assign Multiple Patients to Team/Position(s)

**Team Assignment**

**1.** Select the PATIENT|MULTIPLE ASSIGNMENTS|TEAM ASSIGNMENT menu bar command.

**2.** Select a team through the Select Team To Assign To dialog box.

**3.** The Multiple Patient Assignments to Team form appears. Check the Primary Care Assignment and Restrict Consults check boxes if applicable.

**4.** From the *Select Patients by* drop down list, choose the method of patient selection. If your selection method is *PC Assignment with No Team* , click the GET LIST button and then enter the effective date. Go to Step 6.

**5.** Select the *clinic/stop code/clinic appointment/team* from the drop down list.

If you click the GET LIST button, patient names will appear in the *Available to Assign* box in maximum blocks of 200. If the NEXT BLOCK button is enabled, you may click it to see the next block of names. If your selection method was stop code or clinic appointment, you will be asked for a date range.

If you click the SELECT ALL button, you will get a confirmation box asking if you want to select all patients. If you click YES, all patients will **automatically** be assigned. No entries will appear in either list box and you do not need to proceed further.

**6.** Make your patient selections by clicking on the name.

**NOTE:** The lists of patients, which currently appear in the Available to Assign and New Assignments boxes, may be printed to a local (non-VistA) printer via a popup menu. Access the popup menu by clicking the right mouse (with the cursor inside the box) while the list is active.

**Assign Multiple Patients to Team/Position(s)**

**Team Assignment**

**7.** Move your selections from the *Available to Assign* list box to the *New Assignments* list box by one of the following methods.

1. Double clicking on an entry
2. Click and drag
3. Using the buttons

<!-- image -->

Moves the selected items from the Available to Assign

list box to the *New Assignments* list box.

<!-- image -->

Moves all the items currently in the *Available to*

*Assign* list box to the *New Assignments* list box.

<!-- image -->

Moves the selected items from the *New Assignments* list

box to the *Available to Assign* list box.

<!-- image -->

Moves all the items currently in the New Assignments

list box to the *Available to Assign* list box

**8.** Click the SAVE button. The selected patients are now assigned to the selected team.

**Assign Multiple Patients to Team/Position(s)**

**Team Assignment**

<!-- image -->

***Field Descriptions***

Select Patients by (drop down list)

You may choose to select the patients by clinic enrollment, stop code (active stop codes only), appointments, team enrollment, or pc assignment with no team.

Select Clinic {patient selection method} (drop down list)

Choose the clinic, stop code, clinic appointment, or team from which you wish to assign patients.

Available to Assign (list box)

Contains names of patients who are available to be assigned to the selected team.

Next Block (button)

The Available to Assign list box contains a maximum of 200 names in the displayed block. If the NEXT BLOCK button is enabled, you may click it to see the next block of names.

New Assignments (list box)

Contains names of patients who will be assigned to the selected team once the SAVE button is clicked.

**Assign Multiple Patients to Team/Position(s)**

**Team Assignment**

Entries Found  (numeric display)

Displays the total number of entries found matching the selection criteria.

Entries Processed  (numeric display)

Once the assignment is made and saved, the number of entries processed will be displayed.

Primary Care Assignment (check box)

Check this box if this team is to be the primary care team for these patients. The team must be able to provide primary care.

Restrict Consults (check box)

Click in this box to prevent users from making consult appointments to clinics in which this team's patients are not enrolled. Patients who are listed as “restrict consults” may only be enrolled in a new clinic if the user has the SC CONSULT security key. Consult appointments (an appointment where the patient is not enrolled in the clinic) may only be done via the new Make Consult Appointment option (option requires security key). A MailMan message will be generated whenever a patient whose consults are restricted receives a consult appointment or is enrolled in a new clinic.

**Assign Multiple Patients to Team/Position(s)**

**Position Assignment**

**1.** Select the PATIENT|MULTIPLE ASSIGNMENTS|POSITION ASSIGNMENT menu bar command.

**2.** Select a team through the Select Team To Assign To dialog box.

**3.** Select a position through the Select Position in Team dialog box.

**4.** The Multiple Patient Assignments to: {Position in Team} form appears. Check the Primary Care Assignment check box on the bottom of the form, if applicable.

**5.** From the *Select Patients by* drop down list, choose the method of patient selection. If your selection method is *PC Assignment with No Team* , click the GET LIST button and then enter the effective date. Go to Step 7.

**5a.** If you choose the “position enrollment” method of patient selection, the Select Team dialog box will appear.

1. To assign patients from one position to another position on the same team, select the team chosen at Step 2.
2. To assign patients from a position on one team to a position on another team, select the team **from** which you wish to assign patients.

**6.** Select the *clinic/stop code/clinic appointment/team/position* from the drop down list.

If you click the GET LIST button, patient names will appear in the *Available to Assign* box in maximum blocks of 200. If the NEXT BLOCK button is enabled, you may click it to see the next block of names. If your selection method is stop code or clinic appointment, you will be asked for a date range.

If you click the SELECT ALL button, you will get a confirmation box asking if you want to select all patients. If you click YES, all patients will **automatically** be assigned. No entries will appear in either list box and you do not need to proceed further.

**Assign Multiple Patients to Team/Position(s)**

**POSITION Assignment**

**7.** Make your patient selections by clicking on the name.

**NOTE:** The lists of patients which currently appear in the Available to Assign and New Assignments boxes may be printed to a local (non-VistA) printer via a popup menu. Access the popup menu by clicking the right mouse (with the cursor inside the box) while the list is active.

**8.** Move your selections from the *Available to Assign* list box to the *New Assignments* list box by one of the following methods.

1. Double clicking on an entry
2. Click and drag
3. Using the buttons

<!-- image -->

Moves the selected items from the Available to Assign

list box to the *New Assignments* list box.

<!-- image -->

Moves all the items currently in the *Available to*

*Assign* list box to the *New Assignments* list box.

<!-- image -->

Moves the selected items from the *New Assignments* list

box to the *Available to Assign* list box.

<!-- image -->

Moves all the items currently in the New Assignments

list box to the *Available to Assign* list box

**9.** Click the SAVE button. The selected patients are now assigned to the selected position.

**Assign Multiple Patients to Team/Position(s)**

**Position Assignment**

<!-- image -->

***Field Descriptions***

Select Patients by (drop down list)

You may choose to select the patients by clinic enrollment, stop code (active stop codes only), appointments, team enrollment, position enrollment, or pc assignment with no team.

Select {patient selection method} (drop down list)

Choose the clinic, stop code, clinic appointment, team, or position from which you wish to assign patients.

Available to Assign (list box)

Contains names of patients who are available to be assigned to the selected position.

Next Block (button)

The Available to Assign list box contains a maximum of 200 names in the displayed block. If the NEXT BLOCK button is enabled, you may click it to see the next block of names.

**Assign Multiple Patients to Team/Position(s)**

**POSITION Assignment**

New Assignments (list box)

Contains names of patients who will be assigned to the selected position once the SAVE button is clicked.

Entries Found (numeric display)

Displays the total number of entries found matching the selection criteria.

Entries Processed (numeric display)

Once the assignment is made and saved, the number of entries processed will be displayed.

Primary Care Assignment (check box)

Click in this box if the position you are assigning to is a primary care position for these patients. The position must be able to provide primary care.

Restrict Consults (check box)

Click in this box to prevent users from making consult appointments to clinics in which this team's patients are not enrolled. Patients who are listed as “restrict consults” may only be enrolled in a new clinic if the user has the SC CONSULT security key. Consult appointments (an appointment where the patient is not enrolled in the clinic) may only be done via the new Make Consult Appointment option (option requires security key). A MailMan message will be generated whenever a patient whose consults are restricted receives a consult appointment or is enrolled in a new clinic.

### Reassign Multiple Patients to Team/Position(s)

**Team REAssignment**

**1.** Select the PATIENT|MULTIPLE REASSIGNMENTS|TEAM REASSIGNMENT menu bar command.

**2.** The Multiple Patient Team Reassignment form appears. Click on the *Options [PC Assign]* tab. Check the Primary Care Assignment and Restrict Consults check boxes if applicable.

**3.** Click on the *Reassign* tab. From the *FROM Team* drop down list, select the team **from** which you are reassigning patients. From the *TO Team* drop down list, select the team **to** which you are reassigning patients. Patient names will appear in the *Available to Assign* list box in maximum blocks of 200. If the NEXT BLOCK button is enabled, you may click it to see the next block of names.

**4.** Make your patient selections by clicking on the name.

**5.** Move your selections from the *Available to Assign* list box to the *New Assignments* list box by one of the following methods.

1. Double clicking on an entry
2. Click and drag
3. Using the buttons

<!-- image -->

Moves the selected items from the Available to Assign

list box to the *New Assignments* list box.

<!-- image -->

Moves all the items currently in the *Available to*

*Assign* list box to the *New Assignments* list box.

<!-- image -->

Moves the selected items from the *New Assignments* list

box to the *Available to Assign* list box.

<!-- image -->

Moves all the items currently in the New Assignments

list box to the *Available to Assign* list box

**6.** Click the SAVE button. The selected patients are now reassigned to the selected team. Information concerning patients who were not reassigned will be provided to the user via a new MailMan message.

**Reassign Multiple Patients to Team/Position(s)**

**Team REAssignment**

**Multiple Patient Team Reassignment Screen**

<!-- image -->

***Field Descriptions***

Entries Information

Found (numeric display)

Displays the total number of entries found matching the selection criteria.

Processed (numeric display)

Once the assignment is made and saved, the number of entries processed will be displayed.

NOTE:  When utilizing multiple patient reassignment, the system refreshes the patient count incrementally in the team setting. You may not see all the patients reassigned immediately.

The system will continually refresh until all selected patients have been transferred and the appropriate numbers are displayed.

**Reassign Multiple Patients to Team/Position(s)**

**Team REAssignment**

**Multiple Patient Team Reassignment Screen**

**Options [PC Assign] Tab**

<!-- image -->

Options

Primary Care Assignment (check box)

Check this box if you want the *To* team to be the primary care team for these patients. The team must be able to provide primary care.

Restrict Consults (check box)

Click in this box to prevent users from making consult appointments to clinics in which the *To* team's patients are not enrolled. Patients who are listed as “restrict consults” may only be enrolled in a new clinic if the user has the SC CONSULT security key. Consult appointments (an appointment where the patient is not enrolled in the clinic) may only be done via the new Make Consult Appointment option (option requires security key). A MailMan message will be generated whenever a patient whose consults are restricted receives a consult appointment or is enrolled in a new clinic.

**Reassign Multiple Patients to Team/Position(s)**

**Team REAssignment**

**Multiple Patient Team Reassignment Screen**

**Reassign Tab**

<!-- image -->

From Team (drop down list)

Select the team from which you wish to reassign patients.

To Team (drop down list)

Select the team to which you wish to reassign patients.

Available to Assign (list box)

Contains names of patients who are available to be reassigned to the selected *To* team.

Next Block (button)

The Available to Assign list box contains a maximum of 200 names in the displayed block, if the NEXT BLOCK button is enabled, you may click it to see the next block of names.

New Assignments (list box)

Contains names of patients who will be reassigned to the selected *To* team once the SAVE button is clicked.

**Reassign Multiple Patients to Team/Position(s)**

**Position REAssignment**

**1.** Select the PATIENT|MULTIPLE REASSIGNMENTS|POSITION REASSIGNMENT menu bar command. The Multiple Patient Position Reassignment form appears.

**2** . Click on the *Options [PC Assign]* tab. Check the desired radio button under *Assignment Status* and select the date/date range under *Assignment Dates* if applicable. Check the *Primary Care Assignment* check box if applicable.

**3.** Click on the *Reassign* tab. Select a team from the *FROM Team* drop down list and a position from the *FROM Position* drop down list. Patient names will appear in the *Available to Assign* list box in maximum blocks of 200. If the NEXT BLOCK button is enabled, you may click it to see the next block of names.

**4.** Select a team from the *TO Team* drop down list and a position from the *TO Position* drop down list.

**5.** Make your patient selections by clicking on the name.

**6.** Move your selections from the *Available to Assign* list box to the *New Assignments* list box by one of the following methods.

- Double clicking on an entry
- Click and drag
- Using the buttons

<!-- image -->

Moves the selected items from the Available to Assign

list box to the *New Assignments* list box.

<!-- image -->

Moves all the items currently in the *Available to*

*Assign* list box to the *New Assignments* list box.

<!-- image -->

Moves the selected items from the *New Assignments* list

box to the *Available to Assign* list box.

<!-- image -->

Moves all the items currently in the New Assignments

list box to the *Available to Assign* list box

**7.** Click the SAVE button. The selected patients are now reassigned to the selected team and position. Information concerning patients who were not reassigned will be provided to the user (and to members of the PCMM Reassignment Mail Group) via a new MailMan message.

**Reassign Multiple Patients to Team/Position(s)**

**POSITION REAssignment**

**Multiple Patient Position Reassignment Screen**

<!-- image -->

***Field Descriptions***

Entries Information

Found (numeric display)

Displays the total number of entries found matching the selection criteria.

Processed (numeric display)

Once the assignment is made and saved, the number of entries processed will be displayed.

**Reassign Multiple Patients to Team/Position(s)**

**Position REAssignment**

**Multiple Patient Position Reassignment Screen**

**Options [PC Assign] Tab**

<!-- image -->

***Field Descriptions***

**Assignment Status (radio button)**

Select the assignment status for the list of patients which will appear in the FROM Position list box.

Assigned - Patients currently assigned to the selected FROM position.

Discharged - Patients who have been discharged from the selected FROM position.

Both - Patients in both the Assigned and Discharged categories.

**Reassign Multiple Patients to Team/Position(s)**

**Position REAssignment**

**Multiple Patient Position Reassignment Screen - Options [PC Assign] Tab**

**Assignment Dates**

Select the date or date range for the selected assignment status.

*If Assignment Status is*

Assigned	Date range will not be enabled.

Discharged	Both *from* and *to* date fields will be enabled.

Both	Only *from* date field will be enabled. Range will be to current

date.

**Options**

**Primary Care Assignment (check box)**

Click in this box if the position you are assigning to is a primary care position for these patients.

**Reassign Multiple Patients to Team/Position(s)**

**Position REAssignment**

**Multiple Patient Position Reassignment Screen**

**Reassign Tab**

<!-- image -->

***Field Descriptions***

From Team (drop down list)

Select the team from which you wish to reassign patients.

From Position (drop down list)

Select the position from which you wish to reassign patients.

To Team (drop down list)

Select the team to which you wish to reassign patients.

To Position (drop down list)

Select the position to which you wish to reassign patients.

Available to Assign (list box)

Contains names of patients who are available to be reassigned to the selected *To* team and position.

**Reassign Multiple Patients to Team/Position(s)**

**Position REAssignment**

**Multiple Patient Position Reassignment Screen - Reassign Tab**

Next Block (button)

The Available to Assign list box contains a maximum of 200 names in the displayed block, if the NEXT BLOCK button is enabled, you may click it to see the next block of names.

New Assignments (list box)

Contains names of patients who will be reassigned to the selected *To* team and position once the SAVE button is clicked.

### Setting up OIF/OEF Teams

To assist in the timely treatment of seriously ill Operation Iraqi Freedom (OIF) and Operation Enduring Freedom (OEF) veterans, the VA has established Transition Patient Advocates (TPA) in most VA facilities. Facilities are setting up PCMM non-primary care teams to help identify and track these OIF/OEF patients.

When setting up the new OIF/OEF, follow the same procedure for setting up the Primary Care teams. There may be only one OIF/OEF team per site.

Select OIF/OEF as the Team Purpose and uncheck the Primary care box.

<!-- image -->

Fill in the other required team fields with the information appropriate for your site.

**Setting up OIF/OEF Teams**

Enter the names of the positions according to your facility’s instructions and select the appropriate role from the list box.

Only the following roles are allowed on the OIF/OEF team.

OIF/OEF Transition Patient Advocate (TPA)

OIF/OEF Clinical Case Manager (CCM)

OIF/OEF Program Manager (PM)

<!-- image -->

Fill in the other required position fields with the information appropriate for your site.


## Edit an Existing Team

### Team Setup

<!-- image -->

**1** . Click on the Team Setup toolbar speed button  or select the TEAM|SETUP menu bar command.

**2** . Select the team you wish to edit from the Select Team dialog box and click the OK button.

**3** . Enter the correct information on the General or Settings tabs of the Primary Care Team Profile form. Click the SAVE button after editing for the data to be stored.

**4** . To inactivate the selected team, first click the ADD button on the History tab. After all data is entered, the OK button becomes enabled. Click the OK button to add the new entry to the History Log and store the information. A warning message appears when attempting to inactivate a team with active assignments on or after the inactivation date.

### Position Setup

*These steps cover editing of an existing position. If you are assigning a new position to a team, see “Assign Positions to a Team” under Team Setup.*

<!-- image -->

**1** . Click on the Position Setup toolbar speed button  or select the TEAM|POSITIONS menu bar command.

**2** . Select the team whose positions you wish to edit from the Select Team dialog box and click the OK button.

**3** . Double click the position you wish to edit from the Teams Position list box on the Primary Care Team Position Setup form. Enter the correct information on the General, Settings, or Messages tabs. Click the SAVE button after editing for the data to be stored.

**4** . To inactivate the selected position, first click the ADD button on the History tab. After all data is entered, the OK button becomes enabled. Click the OK button to add the new entry to the History Log and store the information. A warning message appears when attempting to inactivate a position with active assignments on or after the inactivation date.

### Staff Assignment

***(For positions that are NOT part of a preceptor link)***

*These steps cover editing where a staff member has already been assigned to a position. If you are initially assigning a staff member to a position, see “Assign Staff Member to a Position (For positions that are NOT part of a preceptor link)” under Team Setup.*

**1** . Select the TEAM|ASSIGN STAFF menu bar command.

**2** . Select the team whose staff you wish to edit from the Select Team dialog box and click the OK button.

**3** . Select the position you want to edit from the Select Position in Team dialog box and click OK. The Staff Assignment Add/Edit form appears.

**4** . To inactivate the current assignment, click the INACTIVATE button **or** click the right mouse button and select “Inactivate Current Member” **or** choose the EDIT|INACTIVATE CURRENT ASSIGNMENT menu bar command. Edit the effective date and status reason fields, if necessary. Click the SAVE button.

**5** . To assign a new staff member, click the ASSIGN button **or** click the right mouse button and select “Assign Member” **or** choose the EDIT|ASSIGN MEMBER menu bar command.

**6** . The Staff Lookup dialog box appears. Type the staff member name (last, first) and click the SEARCH button. Possible matches appear in the list box. Make your selection and click OK. If the User Classification appears as part of the title bar, you may type a question mark in the lookup box for a listing of all available entries in that User Class. Only names of staff members assigned to that User Class will appear. If the User Class is turned off at your site, any staff member may be selected.

**7** . Entry of FTEE for this position is required if it is the PCP position, otherwise it is optional.

**8** . Edit the effective date and status reason fields, if necessary. Click the SAVE button. Close the form.

**Staff Assignment**

***(For positions that ARE part of a preceptor link)***

*These steps cover editing where a staff member has already been assigned to a position that is part of a preceptor link. If you are initially assigning a staff member to a position, see “Assign Staff Member to a Position (For positions that ARE part of a preceptor link)” under Team Setup.*

**1** . Select the TEAM|POSITIONS menu bar command.

**2** . Select the team whose staff you wish to edit from the Select Team dialog box and click the OK button.

**3** . Select the position you want to edit from the Primary Care Team Position Setup form and then click on the Staff/FTEE button. The Staff Assignment Add/Edit form appears.

**4** . To inactivate the current assignment, click the INACTIVATE button **or** click the right mouse button and select “Inactivate Current Member” **or** choose the EDIT|INACTIVATE CURRENT ASSIGNMENT menu bar command. Edit the effective date and status reason fields, if necessary. Click the SAVE button. If you inactivate a staff assignment for a position that is a current preceptor for another position and attempt to close the Staff Assignment Add/Edit form without creating a current staff assignment, your inactivation change will not be saved.

**5** . To assign a new staff member, click the ASSIGN button **or** click the right mouse button and select “Assign Member” **or** choose the EDIT|ASSIGN MEMBER menu bar command.

**6** . The Staff Lookup dialog box appears. Type the staff member name (last, first) and click the SEARCH button. Possible matches appear in the list box. Make your selection and click OK. If the User Classification appears as part of the title bar, you may type a question mark in the lookup box for a listing of all available entries in that User Class. Only names of staff members assigned to that User Class will appear. If the User Class is turned off at your site, any staff member may be selected. Staff members currently assigned to a preceptor or precepted positions on the team may not be selectable depending on the type of position to which an assignment is being made.

**7** . Entry of FTEE for this position. is required if it is the PCP position, otherwise it is optional.

**8** . Edit the effective date and status reason fields, if necessary. Click the SAVE button. Close the form.

### Single Patient Assignment

*These steps cover editing where a patient has already been assigned to a team and/or position. If you are initially assigning a patient to a team/position, see “Assign Single Patient to Team/Position(s)” under Team Setup.*

<!-- image -->

**1** . Click on the Assign Patients toolbar speed button  or select the PATIENT|PATIENT ASSIGNMENT menu bar command.

**2** . The Patient Lookup dialog box appears. Type the patient name (last, first) and click the SEARCH button. If there is more than one match, possible matches will appear in the list box. Double click your selection **or** single click then click the SELECT button. Employee patients will display “sensitive” in the DOB and SSN columns. Accessing a sensitive patient record can trigger messages and bulletins being sent. If there is another patient with the same last name and same last four digits of the SSN as the selected patient, a warning message will appear to ensure you have selected the correct patient. If the selected patient requires a Means Test, a message will be displayed.

**3** . The Select Patient-Team Assignment form appears. Based on whether or not the Show All Team Assignments menu bar command is selected, all team assignments or only current assignments will appear in the list box. An asterisk in the PC column indicates the primary care team for this patient. If the patient is assigned to more than one team, click on the team for which you wish to edit patient assignment. Click the EDIT TEAM button.

**4** . **Team Assignment -** If necessary, edit the primary care team and restrict consults fields on the Team Assignment tab and click the SAVE button. To discharge a patient from a team, enter the date of discharge. Tab off the field and click the SAVE button. If the patient is assigned to positions on the team, the Review Active Positions dialog box will now appear. Clicking the DISCHARGE button will automatically enter the same discharge date for the associated active positions. Clicking the CANCEL button will cause the just entered date of discharge to be deleted. This action prevents patients being actively assigned to a position without having a team assignment

**5. Position Assignment -** To unassign an existing position assignment, double click on the position on the Position Assignment tab. The Position Information dialog box appears. Enter the unassigned date and click OK. Click the SAVE button. (History for this position assignment will remain.)

**NOTE:** If a patient has been assigned to a position in error (data entry error), the following steps should be taken. Click on the position. Select the EDIT|POSITION ASSIGNMENT|DELETE menu bar command. Confirm the deletion by clicking the OK button. You must hold the SC PCMM DELETE security key to perform this action. (History for this position assignment will be deleted.)


## Creating Autolinks (functionality disabled)

*If you have clicked on the Autolinks button on the General Tab of the Primary Care Team Profile form, begin at Step 3.*

**1** . Select the TEAM|TEAM AUTOLINKS menu bar command.

**2** . Select a team through the Select Team Dialog Box.

**3** . The AutoLink Specification form appears. Choose the type of autolink from along the top of the form.

<!-- image -->

**4** . The *Choices* list box displays the entries for the selected item. You may click the Show All button to display all possible entries **or** type a few characters in the Search box and click the Find button for a limited selection. When first opened, the boxes default to A.

***(This functionality has been disabled.)***

**5** . Move your selections from the *Choices* list box to the *AutoLinks* list box by one of the following methods.

1. Double clicking on an entry
2. Click and drag
3. Using the buttons

<!-- image -->

Moves the selected items from the Available to Assign

list box to the *New Assignments* list box.

<!-- image -->

Moves all the items currently in the *Available to*

*Assign* list box to the *New Assignments* list box.

<!-- image -->

Moves the selected items from the *New Assignments* list

box to the *Available to Assign* list box.

<!-- image -->

Moves all the items currently in the New Assignments

list box to the *Available to Assign* list box

**6** . Click the SAVE button to create the AutoLinks. (You may save after establishing the AutoLinks for each individual item or wait until links are established for all items.)

**7** . Repeat Steps 3 through 6 for each autolink type.

**NOTE** :  To obtain link detail information on an entry, click on the entry from one of the list boxes. Right mouse click and choose “Details”.


## Reports

### Query Template Utility

The Query Template Utility is used to create report templates with a specified sort sequence and with specified category selections (divisions, teams, etc.). Templates may then be used to print the report in the future without having to make sort selections and category selections each time.

1. Select REPORTS|SELECT REPORT menu bar command. The Query Template Utility form appears.

<!-- image -->

**Query Template Utility**

1. Click the desired category button at top of form **or** choose the TEMPLATE|OPEN menu bar command to display the desired template type(s) in the drop down list.

Per (Personal) - your templates only

Pub (Public) - public templates only

All - both your personal and all public templates

#### Create a New Template

<!-- image -->

**1.** Click the Create a New Template toolbar speed button  on the Query Template Utility form or choose the TEMPLATE|NEW menu bar command.

**2.** Edit the Name text box and enter a description.

**3.** Assign either Private or Public access level to the template by clicking the correct radio button.

**4.** Enter the report criteria.

1. Select the Report from the drop down list.

1. If the Sort field is disabled, the default sort values will be used. If the Sort field is enabled, select the desired sort from the drop down list.

1. Select the printer from the drop down list.

1. In addition to the Sort and Printer fields, some reports have other unique data fields. These fields will appear below the Selections button on the form. (See Report Descriptions for a description of each available PCMM report and any unique fields.)

**5.** Click the Selections Button and enter the report specifications (divisions, teams, etc.). ( *See Create a New Template - Report Specifications* ). To obtain selection detail information on an entry, click on the entry from either of the list boxes. Right mouse click and choose “Details”.

**6.** If you wish to save this template after you have made and validated your selections, click the Save Template Changes toolbar speed button, or choose the TEMPLATE|SAVE menu bar command.

**Query Template Utility**

#### Create a New Template - Report Specifications

<!-- image -->

**1.** Choose the category along the top of the form for which you wish to select report specifications.

**2.** The *Possible Choices* list box displays the entries for the selected item. When first opened, the Show All field is checked which displays all possible entries. For a limited selection of entries, click the Show All check box to display the Search box. Type a few characters in the Search box and click the Find button.

**NOTE:** If you have selected the Practitioner Demographics report, this form will appear differently. Since only one practitioner may be selected, the double arrow buttons are not visible. The SEARCH box appears instead of the SHOW ALL check box.

**Query Template Utility**

**3.** Move your selections from the *Possible Choices* list box to the *Selections* list box by one of the following methods.

1. Double clicking on an entry
2. Click and drag
3. Using the buttons

<!-- image -->

Moves the selected items from the Available to Assign

list box to the *New Assignments* list box.

<!-- image -->

Moves all the items currently in the *Available to*

*Assign* list box to the *New Assignments* list box.

<!-- image -->

Moves the selected items from the *New Assignments* list

box to the *Available to Assign* list box.

<!-- image -->

Moves all the items currently in the New Assignments

list box to the *Available to Assign* list box

**4.** Repeat Steps 1 to 3 for each category.

**5.** Click the Validate button. The validation action checks the relationships between the category selections (teams associated with correct division, clinics associated with correct division, etc.). If validation cannot be made, you will receive an Error Report explaining the inconsistency. Close the form.

#### Modify an Existing Template

**1** . Select REPORTS|SELECT REPORT menu bar command

**2.** Select the template name from the drop down list.

**3.** Edit the report criteria.

**4.** Click the Selections button and edit the report specifications (divisions, teams, etc.). Be sure to validate your selections when complete. Close the form.

**5.** If you wish to save this template, click the Save Template Changes toolbar speed button or choose the TEMPLATE|SAVE menu bar command.

**Query Template Utility**

#### Printing Reports

Reports cannot be printed to the screen using the graphical user interface. They must be sent to a printer. These same reports may be printed to both the screen and to a printer through the Scheduling software.

**To print a report from a template**

**1** . Select the reports|select reports menu bar command to open the Query Template Utility form.

**2** . Select the template name from the drop down list.

**3** . Click the Print Report toolbar speed button **or** choose the template|print menu bar command.

**4** . If the Report Print dialog box appears, select the printer from the drop down list and click OK.

**To print a report not set up in a template**

**1** . Select the reports|select reports menu bar command to open the Query Template Utility form.

**2** . Click the Create a New Template toolbar speed button.

**3.** Select the report name and report criteria (sort, printer, etc.).

**4.** Click the Selections button and choose the report specifications. Be sure to validate your selections when complete. Close the form.

**5.** Click the Print Report toolbar speed button **or** choose the template|print menu bar command.

**6** . If the Report Print dialog box appears, select the printer from the drop down list and click OK.

**Query Template Utility**

#### Template Menu Bar Commands

**Restore**

Will restore the selected template values to what they were at the time of the last save.

**Save As**

Use the Save As function to save an existing query under a different name.

1. Select the template name from the drop down list.
2. Select the *Save As* menu bar command and rename the template. Change the description if desired.
3. Follow Steps 3 through 5 under Modify an Existing Template.

**Set Default**

To set a template as your default value, select the template name from the drop down list and click the Set your Default Template to Current toolbar speed button **or** choose the *Set Default* menu bar command.

**Delete**

To delete an existing template, select the template name from the drop down list. Select the *Delete* menu bar command. Click OK.

### Automated Patient Inactivation from Primary Care Panels Report - GUI

This report is used to build a report listing patients that were unassigned during a specific date range.

1. Select REPORTS|PATIENTS AUTO INACTIVATION menu bar command. The Patients Auto Inactivation Criteria Selection form appears.

When selecting options keep in mind that the more categories you select, the longer the report will take. If no items in a category are selected, all are used. Please use care when making your selections to get the exact data you need.

<!-- image -->

**Creating an Automated Patient Inactivation from Primary Care Panels Report**

**1.** Click the Select Institutions button to select one or more institutions to include on the report.  The Choices dialog will appear. Click on desired Institution(s) then click Include Selected to include the selected institution(s) or Include All to include all institutions.

**2.** Click the Select Teams button to select one or more teams to include on the report. The Choices dialog will appear. Click on desired team(s) then click Include Selected to include the selected team(s) or Include All to include all teams.

**3.** Click the Select Positions button to select one or more positions to include on the report. The Choices dialog will appear. Click on desired position(s) then click Include Selected to include the selected position(s) or Include All to include all positions.

**4.** Click the Select Providers button to select one or more providers to include on the report. The Choices dialog will appear. Click on desired provider(s) then click Include Selected to include the selected provider(s) or Include All to include all providers.

**5.** Click the Sort Order button to select which fields the report will be sorted by. The Choices dialog will appear. Click on desired field(s) then click Include Selected to include the selected field (s) or Include All to include all fields.

**6.** Click Beginning Date drop down list arrow to right of date to drop down a calendar and select a beginning date for the report. You may also type in the date by double-clicking to highlight the day/month/year then type your changes.

**7.** Click Ending Date drop down list arrow to right of date to drop down a calendar and select an ending date for the report. You may also type in the date by double-clicking to highlight the day/month/year then type your changes.

**8.** Click Preview to view the report before printing or Print to print the report to any Windows printer.

### Report Descriptions - GUI

Below is a description of each available PCMM GUI report and any unique fields (shown in italics).

**Detailed Patient Assignments – obsolete**

Information can be found in the *Team Patient Listing* Report or *Practitioners Patients* Report

**Individual Team Profile**

Displays basic team definition information

**Patient Listing for Team Assignments**

Lists patients along with selected team information

**Practitioner Demographics**

Displays administrative information for a chosen practitioner - can only select one practitioner per report

**Practitioner's Patients**

Identifies the size and constituents of a practitioner's patient panel

*Summary Only* - Check to only print totals on the report

**Summary Listing of Teams**

Reports the number of patients assigned for each practitioner currently assigned to the team

**Team Member Listing**

Shows basic information on the team and member practitioners - may be used to review which practitioners were assigned to a team during a certain time period.

*Date Range* - Print the report for this date range. Double clicking on the date edit boxes generates a calendar to select from.

**Team Patient Listing**

Lists a team's patients and the clinics in which they are enrolled

### Reports – Roll and Scroll

Many PCMM Reports are available only as roll and scroll Menu options.

From the Outputs menu (under the Scheduling Manager’s menu), type **PCMM** to access the PCMM Main Menu. The PCMM Main Menu contains the following reports and options.

PT     PATIENT REPORTS AND OPTIONS ...

PR     PROVIDER/POSITION REPORTS AND OPTIONS ...

TM     TEAM REPORTS AND OPTIONS ...

HAR    HISTORICAL ASSIGNMENT REPORTS ...

HL     PCMM HL7 AND MAINTENANCE MENU ...

**&gt; Out of order:  This functionality is now accomplished by CDW/VSSC.

WL     Wait List (Sch/PCMM) Menu ...

**Note:** See Appendix for examples of many PCMM Reports.

**Reports – Roll and Scroll**

#### Patient Reports and Options

The Patient Reports and Options Menu accesses patient-related reports that are not available through the PCMM GUI.

Available Patient Reports are as follows.

AU	Team/Position Assignment/Re-Assignment

DPA	Detailed Patient Assignments

**&gt; Out of Order: Obsolete with SD*5.3*535

PAD	Historical Patient Assignment Detail

PATA	Patient Listing for Team Assignments

REV	Patient Team Position Assignment Review

PTAL	Historical Patient Position Assignment Listing

SCHD	Patients Scheduled for Inactivation from PC Panels

EXTD	Patients with Extended Primary Care Inactivation

INAC	Patients Automated Inactivations from PC Panels

EXTP	Extend Patient Inactivation Date

**Reports – Roll and Scroll**

**Patient Reports and Options**

##### Team/Position Assignment/Re-Assignment Option

This VistA option determines a patient's Primary Care status. This option is also available from the PCMM GUI (see note below). Based on status, it will prompt the user to select from the following choices.

- Assign patient to Primary Care (PC) or non-primary care team (if not currently assigned).
- Assign patient to PC or non-primary care Practitioner position (if assigned to a team, but not PC practitioner). User can perform a look-up by either position name or the current practitioner assigned to the position.
- Un-assign from team (if assigned to a PC or non-PC team). If patient is assigned to PC position, both the PC position and PC team will be unassigned.
- Un-assign from position.
- While assigning/un-assigning from a position:  If the position has an Associated Clinic, the user will be prompted to enroll/discharge the patient from that Associated Clinic.

**Note:** This option must be used in the PCMM GUI if you need to:

- Edit or delete
- Re-assign patients with future PC assignments
- If the team position does not have a practitioner currently assigned to it

**Reports – Roll and Scroll**

**Patient Reports and Options**

##### Detailed Patient Assignments OUT OF ORDER - OBSOLETE

This report provides information regarding patient team and clinic assignments. This report requires 132-column output.

Report Columns

- Patient Name
- Patient ID
- Means Test Status
- Primary Eligibility
- Last Appointment
- Next Appointment
- Enrolled Clinic
- Primary Care Provider
- Associate Provider

Report Options

- Select Division - May select one/many/all divisions
- Select Team - May select one/many/all teams
- (A)ssigned or (U)nassigned Patients to Primary Care Team - May select patients currently assigned or previously assigned to the chosen teams

**Reports – Roll and Scroll**

**Patient Reports and Options**

##### Historical Patient Assignment Detail

This 80-column report lists the providers and their positions and the teams to which the selected patient was assigned for the selected time frame.

Report Columns

- Patient
- SSN
- DOB
- Age
- Gender
    - Assignment
PC Provider
PC Associate Provider
PC Position
User Entering
Last Edited By
Status
PC Preceptor Position
PC Team
Non-PC Provider
Non-PC Position
Non-PC Preceptor Provider
Non-PC Preceptor Position
Non-PC Team
    - Active
    - Inactive
    - Assigned by/date
If user says YES to - Do you wish to view active patient record flag details?
Report Columns
    - Patient Record Flags
    - Date
    - Page  x of   n
    - Patient/SSN
    - DOB
    - ICN
    - CMOR
**Reports – Roll and Scroll**
**Patient Reports and Options**
**Historical Patient Assignment Detail, cont.**
Report Options
    - Select Patient Name
    - If Active Patient Record Flag(s) are present this option appears:
Do you wish to view active patient record flag details? Yes//
If yes, then Patient Record Flags are listed.
    - Select beginning date
    - Select ending date
    - Device
**Reports – Roll and Scroll**
**Patient Reports and Options**

##### Patient Listing for Team Assignments

This report provides information regarding patients’ team assignment, sorted by Team and Practitioner. This report requires 132-column output.

Report Columns

- Patient Name
- Patient ID
- Date Assigned
- Primary Care Type (PC?)

AP = Associate provider

PCP = Primary Care Provider

NPC = Non-Primary Care Provider

- Practitioner
- Position
- Standard Role
- Preceptor

Report Options

- Select Division - May select one/many/all divisions
- Select Team - May select one/many/all teams
- Select Role - May select one or all roles
- Select Practitioner – May select one or more practitioners

**Reports – Roll and Scroll**

**Patient Reports and Options**

##### Patient Team Position Assignment Review

This report reviews Patient Team Position Assignments and identifies active positions with discharged team assignments. The report then generates a MailMan message that delivers the information to the requestor.

Report Columns

- Patient Team Position Assignments Reviewed
- Number of Assignments with Problems
    - Team
    - Position
    - Patient
    - Error
Report Options
    - Select Team – May select one/many/all teams
**Reports – Roll and Scroll**
**Patient Reports and Options**

##### Historical Patient Position Assignment Listing

This report requires 132-column output.

Report Columns

Detailed Report contains

- Patient Name
- Patient ID
- Primary Eligibility
- Means Test Category
- Team
- Provider
- Team Position
- Primary Care Type (PC?)

AP = Associate provider

PCP = Primary Care Provider

NPC = Non-Primary Care Provider

- Enrolled Clinic
- Activation Date
- Inactivation Date

Report Columns

Summary Report contains

- Category
- Count
- Percent
- Total assignments that meet the parameters of this report
- Total unique patients that meet the parameters of this report

**Reports – Roll and Scroll**

**Patient Reports and Options**

**Historical Patient Position Assignment Listing, cont.**

Report Options

- Select beginning date
- Select ending date
- Select one of the following

P     Primary Care Assignments

N     Non- Primary Care Assignments

B     Both PC and Non-PC

Specify the type of assignments to include:

- Select one of the following:

D     Detail + Summary

S     Summary Only

Specify output format	(Choose output format from the list above)

- Select Institution - May select one/many/all institutions
- Select Team - May select one/many/all teams
- Select Team Position - May select one/many/all positions
- Select PC Provider  - May select one/many/all PC providers
- Select Assigned Provider - May select one/many/all assigned providers
- Select Associated Clinic - May select one/many/all positions
- Select one of the following   **** Output sort order (optional) ****

IN	Institution

TM	Team

TP	Team Position

PR	Provider

EC 	Enrolled Clinic

PT 	Patient

Sort output by	(Choose sort order from above list)

**Reports – Roll and Scroll**

**Patient Reports and Options**

##### Patients Scheduled for Inactivation from PC Panels

Header

Patients Scheduled for Inactivation from PC Panels (Title)	Date

Report Columns

- Patient Name
- SSN
- Institution
- PC Team
- Provider
- Team Position
- Date scheduled to Inactivate
- Next Appointment
- Date/Clinic

Report Options

- Select beginning date
- Select ending date
- Select Institution - May select one/many/all institutions
- Select Team - May select one/many/all teams
- Select Team Position - May select one/many/all positions
- Select PC Provider - May select one/many/all PC providers
- Select one of the following   **** Output sort order (optional) ****

IN	Institution

TM	Team

TP	Team Position

Patients Scheduled for Inactivation from PC Panels

PR	Provider

PT	Patient

Sort output by	(Displays the sort order selected)

**Reports – Roll and Scroll**

**Patient Reports and Options**

##### Patients with Extended Primary Care Inactivation

Report Columns

- Patient
- SSN
- Institution
- PC Team
- Provider/Position
- Preceptor/Position
- Date Scheduled for Inactivation/Reason

Report Options

- Select beginning date
- Select ending date
- Select Institution - May select one/many/all institutions
- Select Team - May select one/many/all teams
- Select Team Position - May select one/many/all positions
- Select Assigned Provider - May select one/many/all assigned providers
- Select one of the following   **** Output sort order (optional) ****

IN	Institution

TM	Team

TP	Team Position

PCMM Patients with Extended Inactivations

PR	Provider

P	Patient

Sort output by:	(Displays the sort order selected)

**Reports – Roll and Scroll**

**Patient Reports and Options**

##### Patients Automated Inactivations from PC Panels

Report Columns

- Patient
- SSN
- Institution
- PC Team
- Provider/Team Position
- Preceptor/Team Position
- Date Patient Inactivated
- Reason Patient Inactivated

Report Options

- Select beginning date
- Select ending date
- Select Institution - May select one/many/all institutions
- Select Team - May select one/many/all teams
- Select Team Position - May select one/many/all positions
- Select Assigned Provider - May select one/many/all assigned providers
- Select one of the following:   **** Output sort order (optional) ****

IN	Institution

TM	Team

TP	Team Position

PCMM Patients with Extended Inactivations

PR        Provider

PT        Patient

**Reports – Roll and Scroll**

**Patient Reports and Options**

##### Extend Patient Inactivation Date

This option lists the patients, by name only, that are scheduled for automatic inactivation for the selected team. It allows for extending the date of the automatic inactivation and selecting a reason for the extension.

Report Columns

- None

Report Options

- Select Team Name
- Select From - Select from the list of patients on the team that are schedule for inactivation
- Extend Automatic Inactivation  (Possible choices)

0  - Do Not Extend (Default)

1  - Patient has Future PC Appointment

2  - Provider Request – Will Contact Patient

3  - Patient Contacted Site for Appointment

4  - Other [Place comment here]

**Reports – Roll and Scroll**

#### Provider/Position Reports and Options

PCMM Roll and scroll – Provider/Position Reports and Options Menu

EP     PCMM Edit Practitioner in Position Assig. File

PD     Practitioner Demographics

PP     Practitioner's Patients

PRAL   Historical Provider Position Assignment Listing

INCR   PCMM Inconsistency Report

FTEE   FTEE and Panel Size Report

SSI    Staff Sched for Inactivation

SI     Staff Inactivated Report

**Reports – Roll and Scroll**

**Provider/Position Reports and Options**

##### PCMM Edit Practitioner in Position Assig. File

This report identifies invalid practitioner entries and allows for edits. It is locked with the SC PCMM SETUP security key.

**Reports – Roll and Scroll**

**Provider/Position Reports and Options**

##### Practitioner Demographics

This report provider information about the practitioners.

Report Columns

- Name
    - Date
        - Service/Section
        - Team
        - Position
        - Role
        - User Class
        - Room
        - Phone
        - Associated Clinic
        - Person Class
        - Patients Allowed
        - Patients Assigned
    Report Options
        - Select individual Practitioner - Answer with NEW PERSON NUMBER, or NAME, or INITIAL, or SSN, or VERIFY CODE, or NICK NAME, or MAIL CODE, or DEA#, or VA#, or ALIAS
        - Note:  Imprecise selections will yield an additional prompt.
    **Reports – Roll and Scroll**
    **Provider/Position Reports and Options**

##### Practitioner's Patients

Report Columns (Summary Report)

- Date
- Patients
- Practitioner Position
- Team
- Patients Assigned (Number of Patients Assigned)

Report Columns (Detailed Report)

- Date
- Team
- Division
- Practitioner
- Patient Name
- Patient ID
- Means Test Status
- Primary Eligibility
- Last Appointment
- Next Appointment
- Clinic

Report Options

- Select Division - May select one/many/all divisions
- Select Team - May select one/many/all teams
- Select Role - May select one/many/all roles
- Select Practitioner - May select one/many/all practitioners
- Print Summary Only? N// y  YES
- Sort By:

[1] Division, Team, Practitioner

[2] Division, Practitioner, Team

[3] Practitioner, Associated Clinic

**Reports – Roll and Scroll**

**Provider/Position Reports and Options**

##### Historical Provider Position Assignment Listing

This report reflects a count of all unique patients assigned to primary care and non-primary care within the date range selected. If a date range larger than one day has been selected, the total patients assigned to a provider may be greater than the maximum defined for the position. However, this does not imply that the provider had more than their maximum number of patients on any single date.

Report Columns

- Detail for Provider Position Assignments Effective 	(Date Range)
- Date printed		(Date and Time)
- Provider Name
- Position
- Primary Care Status (PC?)
- Team
- Associated Clinic
- Max. Patients Allowed
- Assigned Patients Primary Care (PC)
- Assigned Patients Non-Primary Care (Non-PC)
- Open Slots
- Precepted Patients Primary Care (PC)
- Precepted Patients Non-Primary Care (Non-PC)

**Reports – Roll and Scroll**

**Provider/Position Reports and Options**

**Historical Provider Position Assignment Listing, cont.**

Report Options

- Select beginning date: TODAY//  (APR 03, 2006)	Date Range Selection
- Select ending date: TODAY//  (APR 03, 2006)	Date Range Selection
- Select one of the following: 				Report Parameter Selection

P	PRIMARY CARE ASSIGNMENTS

N	NON-PRIMARY CARE ASSIGNMENTS

B	BOTH PC AND NON-PC

- Specify the type of assignments to include: BOTH// b  BOTH PC AND NON-PC
- Select one of the following:

D	DETAIL + SUMMARY

S	SUMMARY ONLY

Specify output format: DETAIL + SUMMARY// d  DETAIL + SUMMARY

Select Institution - May select one/many/all divisions

Select Team - May select one/many/all teams

Select Assigned Provider - May select one/many/all providers

Select Associated Clinic - May select one/many/all clinics

Select one of the following	Output sort order (optional)

IN	INSTITUTION

TM	TEAM

TP	TEAM POSITION

PR	PROVIDER

EC	ENROLLED CLINIC

Sort output by		(Lists selected output)

**Reports – Roll and Scroll**

**Provider/Position Reports and Options**

##### PCMM Inconsistency Report

Report Columns

- Position Inconsistencies
- Inconsistency		(i.e., Position has no staff assigned)
- Team
- Position
- Patient Inconsistencies
- Patient
- SSN
- Inconsistency		(i.e., Position assignment with inactive Team Assignment)
- Team
- Position

Report Options

- Select one of the following:

A	All Teams

S		Specific Teams

I		Inconsistency Descriptions

- Select one of the following: (Report Type)

B	Brief

DP	Detailed by PATIENT

DT	Detailed by TEAM

**Reports – Roll and Scroll**

**Provider/Position Reports and Options**

##### FTEE and Panel Size Report

Report Columns

- Date
- Provider’s Name
- Team
- Team Position
- AP or PCP
- Associated Clinic
- FTEE
- Patient’s for Position Actual/Active
- Patient’s for Position Allowed/Maximum
- Available Patient Openings
- Adjusted Panel Size
- Total

Report Options

- Select Institution - May select one/many/all divisions
- Select Team - May select one/many/all teams
- Select Team Position - May select one/many/all positions
- Select Assigned Provider - May select one/many/all providers
- Select one of the following:    Output sort order (optional)

IN	INSTITUTION

TM	TEAM

TP	TEAM POSITION

PR	PROVIDER

AC	ASSOCIATED CLINIC

- Sort output by		(Lists selected output )

**Reports – Roll and Scroll**

**Provider/Position Reports and Options**

##### Staff Sched for Inactivation

**Note:** Do not print this report between 7 am and 5 pm. Because this report is resource intensive, printing should be done during off peak hours.

Report Columns

- Date
- Name
- Team Position
- Associated Clinics
- Role
- Person Class
- Number of Patients (# of pts)
- Scheduled Inactivation Date
- Inconsistency Reason

Report Options

- Start with Institution
- Go to Institution
- Device

**Reports – Roll and Scroll**

**Provider/Position Reports and Options**

##### Staff Inactivated Report

Report Columns

- Date
- Name
- Team Position
- Associated Clinics
- Role
- Person Class
- Number of Patients (# of pts)
- Date Inactivation
- Inconsistency Reason

Report Options

- Start with Institution
- Go to Institution
- Device

**Reports – Roll and Scroll**

#### Team Reports and Options

Example of Team Reports and Options Menu

ITP    Individual Team Profile

TML    Team Member Listing

TPL    Team Patient Listing

SLT    Summary Listing of Teams

TAS    Historical Team Assignment Summary

**Reports – Roll and Scroll**

**Team Reports and Options**

##### Individual Team Profile

This report requires 132-column output. This report provides information team members and their assignments.

Report Columns

- Printed on (Date)
- Division
- Team Name
- Service/Section
- Team Phone
- Team Settings
- Status (Active /Inactive)
- Maximum Patients
- Unique Patients Assigned
- Purpose
- Note:  (This team is not accepting patients/This team is still accepting patients!)
- Team Description
- Team Position
- Provider Name
- Standard Role
- Primary Care Status (PC?)
- Patients Allowed
- Patients Assigned
- Associated Clinic

Report Options

- Select Division - May select one/many/all divisions
- Select Team - May select one/many/all teams

**Reports – Roll and Scroll**

**Team Reports and Options**

##### Team Member Listing

This 80 column report list team members during a specific date range. Using the default date of **Today** will list only current team members.

Report Columns

- Printed on
- Division
- Team Name
- Team Phone
- Primary Care Team (Yes/No)
- Members (Name)
- Position
- Standard Role
- User Class
- Associated Clinic
- Office Phone
- Room
- Begin Date
- End Date
- Person Class

Report Options

- Select Division - May select one/many/all divisions
- Select Team - May select one/many/all teams
- Begin Date
- End Date
- Select Role - May select one/many/all roles

**Reports – Roll and Scroll**

**Team Reports and Options**

##### Team Patient Listing

Report Columns

- Printed on
    - Division
    - Team
    - Team Phone
    - Primary Care Team (Yes/No)
    - Team Description
        - Patient Name
        - Patient ID
        - Practitioner
    [Not Assigned] = Patient assigned to Team but not to a position/provider
    [Inactive Position] = Patient assigned to Team &amp; Position but has no active provider
        - Role
            - Primary Care Type (PC?)
            - Last Appointment
            - Next Appointment
            - Associated Clinic
        Report Options
            - Select Division - May select one/many/all divisions
            - Select Team - May select one/many/all teams
            - Select Role - May select one/many/all roles
            - Sort by
        [1] Division, Team, Patient Name
        [2] Division, Team, Last 4 Pt ID
        [3] Division, Team, Practitioner, Patient Name
        [4] Division, Team, Practitioner, Last 4 Pt ID
        Select 1, 2, 3, or 4:
        **Reports – Roll and Scroll**
        **Team Reports and Options**

##### Summary Listing of Teams

Report Columns

- Printed on
    - Division
    - Team Name
    - Practitioner
    - Position
    - Primary Care Type (PC?)
    - Standard Role
    - Associated Clinic
    - Maximum Patients Allowed
    - Assigned Patients - Primary Care
    - Assigned Patients - Non Primary Care
    - Precepted Patients - Primary Care
    - Precepted Patients - Non Primary Care
Report Options
    - Select Division - May select one/many/all divisions
    - Select Team - May select one/many/all teams
    - Select Role - May select one/many/all roles
**Reports – Roll and Scroll**
**Team Reports and Options**

##### Historical Team Assignment Summary

This 132-column report represents a count of team and team position assignments within the date range selected. If a date range larger than one day has been selected, the total unique patients and assignments may be greater than the maximum defined for the team, reducing the open slots reflected by this report accordingly. However, this does not imply that the team had more than its maximum number of patients on any single date.

Report Columns

- Effective Date Range
- Printed on
- Division
- Team
- Primary Care Type (PC?)
- Maximum Patients
- Team Assignment
- Team Assignment Unique
- Team Position Assignments Primary Care
- Team Position Assignments Non Primary Care
- Team Position Unique Patients Primary Care
- Team Position Unique Patients Non Primary Care
- Total Unique Patients
- Open Slots
- Patients without Position Assignment
- Patients without Team Assignment

Report Options

- Begin Date
- End Date
- Select Institution - May select one/many/all institutions
- Select Team - May select one/many/all teams

**Reports – Roll and Scroll**

#### Historical Assignment Reports

Example of PCMM Roll and scroll – Historical Assignment Reports Menu

PAD    Historical Patient Assignment Detail

PRAL   Historical Provider Position Assignment Listing

PTAL   Historical Patient Position Assignment Listing

TAS    Historical Team Assignment Summary

**Reports – Roll and Scroll**

**Historical Assignment Reports**

##### Historical Patient Assignment Detail

Report Columns

- Date printed
- Patient
- SSN
- DOB
- Age
- Gender
- Assignment

PC Provider

PC Associate Provider

PC Position

User Entering

Last Edited By

Status

PC Preceptor Position

PC Team

Non-PC Provider

Non-PC Position

Non-PC Preceptor Provider

Non-PC Preceptor Position

Non-PC Team

- Active
- Inactive
- Assigned by/date

Report Options

- Select Patient Name
- Select beginning date
- Select ending date
- Device

**Reports – Roll and Scroll**

**Historical Assignment Reports**

##### Historical Provider Position Assignment Listing

Report Columns

- Effective Date Range
- Printed on
- Division
- Team
- Primary Care Type (PC?)
- Maximum Patients
- Team Assignment
- Team Assignment Unique
- Team Position Assignments Primary Care
- Team Position Assignments Non Primary Care
- Team Position Unique Patients Primary Care
- Team Position Unique Patients Non Primary Care
- Total Unique Patients
- Open Slots
- Patients without Position Assignment
- Patients without Team Assignment

Report Options

- Select beginning date
- Select ending date
- Select one of the following (Specify the type of assignments to include

P	PRIMARY CARE ASSIGNMENTS

N	NON-PRIMARY CARE ASSIGNMENTS

B	BOTH PC AND NON-PC

- Select one of the following (Specify output format)

D	 DETAIL + SUMMARY

SUMMARY ONLY

- Select Institution - May select one/many/all institutions
- Select Team - May select one/many/all teams
- Select Team Position - May select one/many/all positions
- Select one of the following (Sort output by)

IN	INSTITUTION

TM	TEAM

TP	TEAM POSITION

PR	PROVIDER

EC	ENROLLED CLINIC

:

**Reports – Roll and Scroll**

**Historical Assignment Reports**

##### Historical Patient Position Assignment Listing

In this 132-column report, more than one provider may be associated with a single patient position assignment. This output returns a separate output line for each related provider during the date range selected.

Report Columns

- Date printed
- Patient Name
- Patient  ID
- Primary Eligibility
- Means Test Category
- Team
- Provider
- Team Position
    - Primary Care Type (PC?)
AP   = Associate provider
PCP = Primary Care Provider
NPC = Non-Primary Care Provider
    - Enrolled Clinic
    - Activation Date
    - Inactivation Date
Report Options
    - Select beginning date
    - Select ending date
    - Select one of the following (Specify the type of assignments to include)
P		PRIMARY CARE ASSIGNMENTS
N	NON-PRIMARY CARE ASSIGNMENTS
B	BOTH PC AND NON-PC
    - Select one of the following (Specify output format)D	DETAIL + SUMMARY **or** S	 SUMMARY ONLY
    - Select Institution - May select one/many/all institutions
    - Select Team - May select one/many/all teams
    - Select Team Position - May select one/many/all positions
    - Select one of the following (Sort output by)
IN	INSTITUTION
TM	TEAM
TP	TEAM POSITION
PR	PROVIDER
EC	ENROLLED CLINIC
PT	PATIENT
**Reports – Roll and Scroll**
**Historical Assignment Reports**

##### Historical Team Assignment Summary

This 132-column report represents a count of team and team position assignments within the date range selected. If a date range larger than one day has been selected, the total unique patients and assignments may be greater than the maximum defined for the team, reducing the open slots reflected by this report accordingly. However, this does not imply that the team had more than its maximum number of patients on any single date.

Report Columns

- Effective Date Range
- Printed on
- Division
- Team
- Primary Care Type (PC?)
- Maximum Patients
- Team Assignment
- Team Assignment Unique
- Team Position Assignments Primary Care
- Team Position Assignments Non Primary Care
- Team Position Unique Patients Primary Care
- Team Position Unique Patients Non Primary Care
- Total Unique Patients
- Open Slots
- Patients without Position Assignment
- Patients without Team Assignment

Report Options

- Begin Date
- End Date
- Select Institution - May select one/many/all institutions
- Select Team - May select one/many/all teams

**Reports – Roll and Scroll**

### PCMM HL7 and Maintenance Menu

Menu placed out of order.

**Reports – Roll and Scroll**

### Wait List (Sch/PCMM) Menu

Example of Wait List (Sch/PCMM) Menu

1      Inquire Wait List (Sch/PCMM)

2      Enter/Edit Wait List (Sch/PCMM)

3      Disposition Wait List (Sch/PCMM) Entry

4      Wait List (Sch/PCMM) Reports ...

5      Wait List (Sch/PCMM) Parameter Enter/Edit

Stand-alone Options

This section includes the option documentation for the Mass Team/Position Unassignment option, the Patient Team Position Assignment Review option, the PCMM Nightly Task option, the Clean-Up Ghost Entries option, and the Clean-Up Incorrect Team Institution Pointers option. These options are not distributed as part of any existing menu. They are intended for IRM or select ADPAC personnel.

### Mass Team/Position Unassignment

**Introduction**

The Mass Team/Position Unassignment option can be used to unassign a large number of patients from an active team or an active position using the List Manager functionality. It is recommended that distribution of this option be limited.

The effective date you choose for the unassignment may be in the past, today, or in the future. The list of patients displayed contains all patients with assignments to the selected team/position, as of the selected effective date or after the effective date. Those with assignment dates in the future will show an asterisk (*) next to the assigned date.

When patients are unassigned from the team, they are also automatically unassigned from any associated position. If a position is associated with a clinic, you are given the opportunity to also discharge patients from the clinic.

The following is an explanation of the actions available.

**SA** Select all patients on the list

**DA** Deselect all patients on the list

**SP** Select individual patients

**DP** Deselect individual patients

**VA** List all patients. Those selected will show a YES in the Selected column.

**VS** Only list patient that have been selected

**VD** Only list patients that have not been selected

**UN** Will queue the unassignment process after you say you want to continue

**Mass Team/Position Unassignment**

After you have selected the patients, choose the Unassign Patients action. A summary of the unassignments that will occur is displayed. You are then asked if you are sure you want to continue. A YES response immediately queues the unassignment process and the Task # is displayed. A NO response returns the screen to where it was before the Unassign Patients action was entered.

A confirmation MailMan message is generated from the utilization of the unassign action. It contains the team name and the effective date of the unassignment. The “Entry#” (shown for errors and for future assignments that are deleted) is the internal entry number of the deleted entry. It comes from the PATIENT TEAM ASSIGNMENT file (#404.42) or the PATIENT TEAM POSITION ASSIGNMENT file (#404.43). The following applicable information is also contained in the mail message.

*Patients Processed*

Lists number of patients unassigned, number still assigned due to error, total patients, and any associated clinic discharges.

*Clinic Discharges*

Lists any associated clinic discharges. The position and associated clinic are displayed.

*Error List*

Lists those patients still assigned and the reason why.

*Unassigned List*

Lists those patients unassigned and, for team unassignment, unassignments which were automatically made from associated positions.

**Mass Team/Position Unassignment**

**Example**

Select Type of Mass Unassignment: Team// **&lt;RET&gt;**

Effective Date: T-1// **&lt;RET&gt;** (AUG 05, 1998)

Select TEAM NAME: **lidster**

&gt;&gt;&gt; Checking to see if any team positions are associated with clinics...

---------------------------------------------------------------------------

Team         : LIDSTER

Position     : PHYSICIAN-ATTENDING

Associated Clinic: 0RTHO

&gt;&gt;&gt; Do you want to discharge patients from this clinic? (Yes/No) **Y** YES

...SORRY, THIS MAY TAKE A FEW MOMENTS...

**Mass Team Unassignment** Aug 06, 1998 08:07:09   Page:  1 of  1

Team: LIDSTER              Total: 6 Selected: 0

Proposed Effective Date: 08/05/1998      View: ALL

Selected Patient Name           ID            Assigned  Unassigned

1             PCMMpatient, One       000-89-0909   08/12/97

2             PCMMpatient, Two       000-12-4321   04/30/97

3             PCMMpatient, Three     666-00-9899   01/16/98

4             PCMMpatient, Four      666-87-2290   09/22/97

5             PCMMpatient, Five      000-33-4122   05/04/98

6             PCMMpatient, Six       000-44-5634   *08/24/98

* Future Date

SA Select All      DP DeSelect Patients   VD View DeSelected

DA DeSelect All     VA View All       UN Unassign Patients

SP Select Patients    VS View Selected     QU Quit

Select Action: Quit// **SA** Select All

...EXCUSE ME, JUST A MOMENT PLEASE...

**Mass Team/Position Unassignment**

**Mass Team Unassignment** Aug 06, 1998 08:07:09   Page:  1 of  1

Team: LIDSTER              Total: 6 Selected: 0

Proposed Effective Date: 08/05/1998      View: ALL

Selected Patient Name         ID           Assigned  Unassigned

1    YES      PCMMpatient, One     000-89-0909  08/12/97

2    YES      PCMMpatient, Two     000-12-4321  04/30/97

3    YES      PCMMpatient, Three   666-00-9899  01/16/98

4    YES      PCMMpatient, Four    666-87-2290  09/22/97

5    YES      PCMMpatient, Five    000-33-4122  05/04/98

6    YES      PCMMpatient, Six     000-44-5634  *08/24/98

* Future Date

SA Select All      DP DeSelect Patients   VD View DeSelected

DA DeSelect All     VA View All       UN Unassign Patients

SP Select Patients    VS View Selected     QU Quit

Select Action: Quit// **UN** Unassign Patients

---------------------------------------------------------------------------

Team Unassignment Definition

---------------------------------------------------------------------------

Team       : LIDSTER

Effective Date  : 08/10/1998

# of Patients  : 6

Clinic Discharges:  Position         Associated Clinic

--------         -----------------

PHYSICIAN-ATTENDING   ORTHO

Are you sure you want to continue? No// **YES**

Task#: 5692

Enter RETURN to continue: **&lt;RET&gt;**

**Mass Team/Position Unassignment**

**Example of MailMan Message**

Subj: Mass Team Unassignment Information [#68602] 06 Aug 98 08:07 35 Lines

From: POSTMASTER (Sender: PCMMstaff, One) in 'IN' basket.  Page 1 **NEW**

-----------------------------------------------------------------------------

Mass Team Unassignment has been completed.

Team: LIDSTER

User: POSTMASTER

Effective Date: 08/06/1998

Patients Processed

Unassigned   : 6

Errors/Warnings: 0  (still assigned)

Total     : 6

Clinic Discharges:  Position           Associated Clinic

--------           -----------------

PHYSICIAN-ATTENDING      ORTHO

Error List:

===========

No errors to report

Unassigned List:

================

Patient              ID

-------              --

PCMMpatient, One			000-89-0909

PCMMpatient, Two			000-12-4321

&gt;&gt;&gt; Position assignment to PCMMprovider, One was unassigned.

&gt;&gt;&gt; Position assignment to PCMMRNprovider, One was unassigned

PCMMpatient, Three			666-00-9899

&gt;&gt;&gt; Position assignment to PHYSICIAN-ATTENDING was unassigned.

&gt;&gt;&gt; Discharged from ‘ORTHO’ clinic

PCMMpatient, Four			666-87-2290

&gt;&gt;&gt; Position assignment to PCMMprovider, One was unassigned.

&gt;&gt;&gt; Position assignment to PCMMRNprovider, One was unassigned

PCMMpatient, Five			000-33-4122

&gt;&gt;&gt; Position assignment to PCMMprovider, One was unassigned.

PCMMpatient, Six			000-44-5634

&gt;&gt;&gt; Future team assignment deleted.

Assignment Date: 08/24/98  Entry#: 3874

&gt;&gt;&gt; Position assignment to PCMMprovider, One:

&gt;&gt;&gt; Future position assignment deleted.

Assignment Date: 08/24/98  Entry#: 2447

Select MESSAGE Action: IGNORE (in IN basket)//

### Patient Team Position Assignment Review

**Introduction**

The Patient Team Position Assignment Review option makes a comparison of the entries in the PATIENT TEAM POSITION ASSIGNMENT file (#404.43) and the PATIENT TEAM ASSIGNMENT file (#404.42). It checks that the position assignment active timeframe is within the team assignment active timeframe. The current PCMM software is designed to prevent timeframe discrepancies. However, older versions of PCMM did allow these timeframe problems to occur. This report has been designed to help sites identify these problem assignments.

The report is in the form of a mail message and lists those position assignments that fall outside the team assignment active timeframe. Each entry in the mail message will display team name, position, patient name, error, position assigned/unassigned date, and team assigned/unassigned date.

You may correct timeframe discrepancies using the PCMM GUI as follows.

- From the Patient drop down menu, make sure *Show All Team Assignments* is checked.
- From the Patient drop down menu, select *Patient Assignments* .
- Enter the patient name.
- The Select Patient-Team Assignment dialog box appears. Double click on the problem Team Assignment.
- The Team-Position Assignments dialog box appears. Make note of the discharged date on the Team Assignment tab. Click on the Position Assignments tab. Double click on the problem Position Assignment.
- Enter the discharged date from above as the Unassigned Date.

**Example**

Select Team: ALL// **BLUE**

Select another Team: **RED**

Select another Team: **&lt;RET&gt;**

&gt;&gt;&gt; Task#: 388578

This task will send a MailMan message to you containing

the results of the position assignment review.

&gt;&gt;&gt; Press RETURN to continue: **&lt;RET&gt;**

**Patient Team Position Assignment Review**

Subj: Patient Team Position Assignment Review [#70086] 04 Sep 98 10:41 32 Lines

From: POSTMASTER (Sender: PCMMstaff, Two)  in 'IN' basket.  Page 1 **NEW**

-------------------------------------------------------------------------------

In order to correct the following active positions with discharged team

assignments, please refer to the documentation for the Patient Team Position

Assignment Review option found in the Stand-alone Options Section of the

PCMM User Guide.

Teams Reviewed:

BLUE

RED

Patient Team Position Assignments Reviewed:   12

Number of Assignments with Problems    :   3 ( 25.00%)

=============================================================================

Team: BLUE         Position: PRIMARY CARE PHYSICIAN

Patient: PCMMpatient, Seven (1010)

Error: Position Assigned Date is BEFORE Team Assigned Date

Position Assigned Date: 04/25/1996

Team Assigned Date: 04/28/1996

-----------------------------------------------------------------------------

Team: BLUE         Position: PRIMARY CARE PHYSICIAN

Patient: PCMMpatient, Eight (0144)

Error: Position Assigned Date is BEFORE Team Assigned Date

Position Assigned Date: 08/28/1998

Team Assigned Date: 08/30/1998

-----------------------------------------------------------------------------

Team: RED         Position: PHYSICIAN

Patient: PCMMpatient, Nine (7964)

Error: Position Unassigned Date is AFTER Team Unassigned Date

Team Unassigned Date: 04/01/1997

Position Unassigned Date: 07/09/1997

-----------------------------------------------------------------------------

Select MESSAGE Action: IGNORE (in IN basket)//


### PCMM Nightly Task  [SCMC PCMM NIGHTLY TASK]


This task should be scheduled once a day. It reviews patient team assignments and inactivates patients who have assignment dates greater than two years old and have not been seen in the last year. This task also identifies staff members who are improperly assigned as Primary Care Providers (PCP). The task also reviews data for other inactivation scenarios. See Inactivation Messages section for examples of the types of bulletins that are sent.


### Retransmit one Patient or Provider

To	 retransmit a single patient enter the patient name at the prompt:

Select PATIENT NAME

To retransmit all patients for a given provider, press return to select the provider.

Select Provider

Either the Patient name or the Provider name must be entered.


### Clean-Up Ghost Entries

**Introduction**

This utility has been created to clean up dangling pointers in the PATIENT TEAM POSITION ASSIGNMENT file (#404.43). This utility loops through the PATIENT TEAM POSITION ASSIGNMENT (#404.43) file and finds the pointers to the PATIENT TEAM ASSIGNMENT (#404.42) file. It will then prompt the user as to whether or not they want the utility to clean up the identified "Ghost Entries."

**Example**

SCMC CLEAN GHOST ENTRIES     Clean-Up Ghost Entries

Clean-Up Ghost Entries

Checking for "Ghost Entries" in the PATIENT TEAM POSITION ASSIGNMENT FILE.

This may take a moment.  You will be provided with a list showing corrupted

file entries.  To perform a clean-up accept the "Yes" prompt after the list

is displayed. Answer "No" to abort the clean-up.

DEVICE:   UCX/TELNET    Right Margin: 80//

PATIENT TEAM POSITION ASSIGNMENT LIST          AUG 10,2007  11:08    PAGE 1

--------------------------------------------------------------------------------

*** NO RECORDS TO PRINT ***

3159 entries searched.  Ghost entries found:  0

Nothing to clean up....


### Clean-Up Incorrect Team Institution Pointers

**Introduction**

This utility has been created to check each team's institution in order to make sure it contains at least the station's base numeric identifier. The utility will then provide a list of teams whose station number association does not match the numeric identifier listed.

**Example**

SCMC CLEAN INSTITUTION Clean-Up Incorrect Team Institution Pointers

Clean-Up Incorrect Team Institution Pointers

Your Station Name:  CHEYENNE VAMC

Number:  442

This option will output a list of TEAMS whose Station Number association

does not match the number listed above.

DEVICE:   TELNET TERMINAL

TEAM LIST                                      AUG 10,2007  11:01    PAGE 1

NAME                            INSTITUTION                     STATION #

--------------------------------------------------------------------------------

GREEN TEAM                      ALBANY, NY (NHCU)               5009AA

JOHN 498 TEST                   PROVIDENCE VAMC                 650

The listed entries from the TEAM file need to be reviewed for Institution.

PCMM GUI clients prior to SD*5.3*297 allowed Team association to any entry

in the Institution File.

If all teams have the correct institution, the following output will be generated:

TEAM LIST                                      AUG 10,2007  11:07    PAGE 1

NAME                            INSTITUTION                     STATION #

--------------------------------------------------------------------------------

*** NO RECORDS TO PRINT ***

No problems found.


## Windows Conventions

### Standard Windows Objects

These are the types of data entry fields located in standard windows forms:

**Check Box**

Toggles between a YES/NO, ON/OFF setting. Usually a square box containing a check mark or *x* . Clicking the box or pressing the spacebar toggles the check box setting.

**Command Button**

The Command button initiates an action. It is a rectangular box with a label that specifies what the button does. Command buttons that end with three dots indicate that a subsidiary screen may be evoked by selecting the command.

**Date Field**

Identified by “\_\_/\_\_/\_\_” or a date “mm/dd/yy”. Will usually have an associated popup calendar. Double clicking with the mouse inside the date edit box or tabbing to the edit box and then pressing the F2 key displays the calendar. Clicking on the desired date or using the arrow keys to move to a date and then pressing the spacebar selects the date. Each component of the date (month/day/year) must consist of two characters (i.e., 02/02/96). The selected entry will not be effective until you tab off or exit from the date field.

**Drop Down List**

A list box containing an arrow button on the right side which displays one entry at a time. Choose from a vertical list of choices. Select the entry you want by clicking the list entry. You cannot type in this box, only select an item from the list. Once an entry is selected, it cannot be deleted - only changed. If &lt;None&gt; is the last entry, selecting it will clear the list entry. If &lt;More&gt; is the last entry, selecting it will display additional entries. The selected entry will not be effective until you tab off or exit from the drop down list.

**F2 Key**

Where there is an additional action which may be taken on a field, pressing the F2 key will initiate that action.

**Faded Background**

Fields that appear with a faded background are currently disabled.

**List Box**

Box which shows a list of items. If more items exist than can be seen in the box, a scroll bar appears on the side of the box. Selecting an entry from a list box requires either double clicking the entry or single clicking the entry and pressing the spacebar.

**Standard Windows Objects**

**Lookup Box**

Choose from a vertical list of choices. By typing in a few characters and pressing the ENTER or TAB key, a list of matching entries drops down. Select the entry you want by clicking the list entry. Entering a question mark and then pressing ENTER or TAB or clicking the down arrow on an empty edit field gives a complete listing of available entries. If &lt;More&gt; is the last entry, selecting it will display additional entries.

Memo Field

This field is equivalent to a word-processing field.

Non-White Background

Items in fields that appear with a non-white background can be selected but cannot be modified directly in that field.

**Radio Button**

Radio buttons appear in sets. Each button represents a single choice and normally only one button may be selected at any one time. For example, MALE or FEMALE may be offered as choices through two radio buttons. Click in the button to select it.

**Right Mouse Button or Shift F10**

You may click the right mouse button or press Shift F10 for a popup box of menu items.

**Tab Key**

Use the TAB key or the mouse to move between fields. Do not use the RETURN key. The RETURN key is usually reserved for the default command button or action (except in menu fields).

**Text Box**

Type the desired characters into the edit box. The selected entry will not be effective until you tab off or exit from the text box.

### Form Buttons

Buttons which appear on tab pages apply only to that tab and not the entire form. If there are action buttons on both the tab page and the form, the tab button should normally be clicked first.

**Add**

Anytime you reach a screen and the ADD button is enabled, you must first click the ADD button before entering any information.

**Assign**

Used to assign a staff member, patient, or preceptor to a position.

**Autolinks -** ***(This functionality has been disabled.)***

Opens the Autolinks form used to establish linkages between a team and wards/beds/clinics/practitioners, etc. (for OE/RR).

**Cancel**

Cancels the latest entry (up until the OK or SAVE button is clicked).

**Close**

Closes the window. If there are any changes that have not been saved, you will get a confirmation message asking you if you want to continue without saving; save before exiting; or cancel the close action and return to the window.

**Edit**

Used to edit position information.

**Find**

Used to quickly find an entry. Enter the search string and click the OK button.

**Help**

Provides help for the area you are currently working in.

**New**

Used to open up a dialog box from which you can enter a new team or position.

**OK**

Adds the new entry after the data has been entered.

**Positions**

Opens the Primary Care Team Position Setup form. If the team has no active positions, the New Position dialog box will appear.

**Preceptor**

Opens the Preceptor Assignment Add/Edit form.

**Form Buttons**

**Save**

Saves all changes made since the last save action. If you attempt to save and all required fields have not yet been completed, you will receive notification that the required fields must be completed before saving.

**Search**

After at least three characters are typed in a lookup dialog box, clicking the Search button will bring up matching entries.

**Staff**

Opens the Staff Assignment Add/Edit form.

**Undo**

Undoes all changes made since the last save action and redisplays the original data.


## Troubleshooting Guide

### Inconsistency Descriptions with Detailed Correction Instructions

**1. Position with patient assignment has no staff assigned**

**Problem** :	Position exists with patients assigned to the Position, but no staff member is assigned to that Position.

**Fix:** Use PCMM GUI

**Steps:** Click Team pull down menu

- Select Positions
- Double Click on correct Team name
- Team Position Setup window opens
- Click on correct Active Team position
- Click on Staff button
- Click Assign button
- Enter name of staff member to assign to that position
- Change Effective Date if appropriate
- Click Save button

**2. Patient on a Team designated PC has no PCP assigned**

**Problem:** Patient is assigned to a Primary Care Team but has no Primary Care Practitioner assigned.

**Fix:** Use PCMM GUI

**Steps:** Click Patient pull down menu

- Click Patient pull down menu
- Select Patient Assignment
- Patient Lookup window opens
- Enter patient’s name
- Patient – Team Assignment window opens
- Double-click team name
- Team – Position Assignments window opens
- Click on Position Assignments tab
- Click Assign button
- Double-click correct Position
- Position Information window opens
- Change Assigned Date if appropriate
- Click OK button
- Click Save button
- Close windows

**Inconsistency Descriptions with Detailed Correction Instructions**

**Fix:** Use VistA options

**Steps:** Select Appointment Management option

- Enter Patient name
- Select PC – PC Assign or Unassign action
- The following is displayed:
    1. POSITION ASSIGNMENT - BY PRACTITIONER NAME
    2. POSITION ASSIGNMENT - BY POSITION NAME
    3. TEAM UNASSIGNMENT
Use either #1 or #2 to assign patient.
    - If you select #1: POSITION ASSIGNMENT - BY PRACTITIONER NAME
    - Position’s Current PRACTITIONER: (Enter Practitioner’s name)
Hint: Type ?? to see list of Practitioners for that Team.
    - Assignment Date: TODAY// (Press Return key)
    - Are you sure? (Yes/No)? (Enter YES)
    - Position Assignment made
    - If you select #2 POSITION ASSIGNMENT - BY POSITION NAME
    - POSITION’s Name: (Enter the name of the Position)
Hint:	Type?? to see list of Positions &amp; staff assigned to that Position for that Team.
    - Assignment Date: TODAY// (Press Return key)
    - Are you sure? (Yes/No)? (Enter YES)
    - Position Assignment made
**Inconsistency Descriptions with Detailed Correction Instructions**
**3. Patient has multiple active PCP assigned****Problem:** Patient has multiple active Primary Care Practitioner assigned.**Fix:** Use PCMM GUI**Steps:** Determine wish PCP assignment is correct
    - Click Patient pull down menu
    - Select Patient Assignment
    - Patient Lookup window opens
    - Enter patient’s name
    - Patient – Team Assignment window opens
    - Double-click team name
    - Team – Position Assignments window opens
    - Click on Position Assignments tab
    - Highlight the incorrect Position Assignment
    - Click on Edit pull-down menu
    - Select Position assignment
    - Click on Delete
    - Confirm window opens
    - Click on Yes button
    - Close windows
**4. Patient’s AP and PCP are the same****Problem:** Associate Provider and Primary Care Provider is the same staff member.**Fix:** Use PCMM GUI**Steps:** Patient Drop down menu
    - Make sure “Show All Team Assignments” is checked
    - Do Not check under Team drop down menu
    - “Active Only” as you will want all teams to show (active or inactive)
    - Under Team, Click on speed positions setup button
    - Select Team
    - Primary Care Position Setup screen is displayed
    - Click on one of the positions (AP or PCP)
    - Click on the Staff button
    - Click the Inactivate button
    - Assign an effective date, status and reason
Hint: If the date of today is selected, it will not show off the Inconsistency report until Midnight as assignment changes are valid until the end of the day.
    - Close
**Inconsistency Descriptions with Detailed Correction Instructions**
**5. AP is without a Preceptor****Problem:** Associate Provider is not assigned a Preceptor.**Fix:** Use PCMM GUI**Steps:** Click Team pull down menu
    - Select Positions
    - Double Click on correct Team name
    - Team Position Setup window opens
    - Click on correct Active Team position
    - Click on Preceptor button
    - Preceptor Assignment Add/Edit window opens
    - Click Assign button
    - Select Preceptor Position window opens
    - Double click correct Preceptor
    - Change Effective Date if appropriate
    - Click Save
    - Close windows
**6. AP position is not designated for PC****Problem:** Associate Provider is not listed as Can Provide Primary Care.**Fix:** Use PCMM GUI**Steps:** Click Team pull down menu
    - Select Positions
    - Double Click on correct Team name
    - Team Position Setup window opens
    - Click on correct Active Team position
    - Click Settings Tab
    - Click Can Provide Primary Care checkbox
    - Click Save button
    - Close windows
**Inconsistency Descriptions with Detailed Correction Instructions**
**7. PCP position is not designated for PC****Problem:** Primary Care Provider position is not listed as Can Provide Primary Care.**Fix:** Use PCMM GUI**Steps:** Click Team pull down menu
    - Click Team pull down menu
    - Select Positions
    - Double Click on correct Team name
    - Team Position Setup window opens
    - Click on correct Active Team position
    - Click Settings Tab
    - Click Can Provide Primary Care checkbox
    - Click Save button
    - Close windows
**8. Active position assignment with inactive Team Assignment/Team/Position****Problem:** An active Position assignment is associated with an inactive Team.**Fix:** Use PCMM GUI
**Steps:		Determine if Team should be inactive - If YES**
    - In order to correct this problem, the Team must be made active so that the patients assigned to this Team can be deleted and the Team made inactive again.
        - Click Team pull down menu
        - Click on Active only from pull down menu
        - Click Team pull down menu
        - Select Setup
        - Double Click on correct Team name
        - Click on History Tab
        - Click Add button
        - Change Effective Date if appropriate
        - Click on Reason down arrow
        - Select a reason from the drop down list
        - Click OK button
        - Click Close button
        - The Team is now active
        - (Steps necessary to delete patients assigned to this Team)
        - Click Patient pull down menu
        - Select Patient Assignments
        - Patient Lookup window opens
        - Enter Patient name
        - Double click patient name
    **Inconsistency Descriptions with Detailed Correction Instructions**
        - Select Patient – Team Assignment window opens
        - Double click Team
        - Click Position Assignments tab
        - Highlight correct Position Assignment
        - Click on Edit pull down menu
        - Select Position Assignment from pull down menu
        - Click on Delete from pull down menu
        - Confirm Window opens
        - Click Yes button
        - Close window
        - Make sure correct Team is highlighted
        - Click Assignments pull down menu
        - Select Delete from a Team from the pull down menu
        - Confirm Window opens
        - Click Yes button
        - Close window
        - (Repeat steps for each patient assigned to this Team)
        - (Steps necessary to make Team inactive)
        - Click Team pull down menu
        - Click on Active only from pull down menu
        - Click Team pull down menu
        - Select Setup
        - Double Click on correct Team name
        - Click on History Tab
        - Click Add button
        - Change Effective Date if appropriate
        - Click on Reason down arrow
        - Select a reason from the drop down list
        - Click OK button
        - Click Close button
        - The Team is now inactive
    **Inconsistency Descriptions with Detailed Correction Instructions**
    **Steps:		Determine if Team should be inactive - If NO**
        - The Team should not be inactive. You need to make this Team active. Follow these steps necessary to make a Team active.
        - Click Team pull down menu
        - Click Team pull down menu
        - Click on Active only from pull down menu
        - Click Team pull down menu
        - Select Setup
        - Double Click on correct Team name
        - Click on History Tab
        - Click Add button
        - Change Effective Date if appropriate
        - Click on Reason down arrow
        - Select a reason from the drop down list
        - Click OK button
        - Click Close button
        - The Team is now active
    **Inconsistency Descriptions with Detailed Correction Instructions**
    **9. Active position Assignment with Inactive Team Assignment/Team/Position****Problem:** An active Position assignment is associated with an inactive Position.**Fix** :	Use PCMM GUI
    **Steps:		Determine if Position should be inactive - If YES**
        - In order to correct this problem, the Position must be made active so that the patients assigned to this Position can be deleted and the Position made inactive again.
        - (The following steps are necessary to make position active.)
        - Click Team pull down menu
        - Select Positions
        - Double Click on correct Team name
        - Team Position Setup window opens
        - Click All Positions radio button to see All Positions (active and inactive)
        - Click on correct Team position
        - Click on History Tab
        - Click Add button
        - Change Effective Date if appropriate
        - Click on Reason down arrow
        - Select a reason from the drop down list
        - Click OK button
        - Click Close button
        - (The following steps necessary to delete patients assigned to this position)
        - Click Patient pull down menu
        - Select Patient Assignments
        - Patient Lookup window opens
        - Enter Patient name
        - Double click patient name
        - Select Patient – Team Assignment window opens
        - Double click Team
        - Click Position Assignments tab
        - Highlight correct Position Assignment
        - Click on Edit pull down menu
        - Select Position Assignment from pull down menu
        - Click on Delete from pull down menu
        - Confirm Window opens
        - Click Yes button
        - Close window
        - (Repeat steps for each patient assigned to this position)
    **Inconsistency Descriptions with Detailed Correction Instructions**
        - (The following steps necessary to make position inactive)
        - Click Team pull down menu
        - Select Positions
        - Double Click on correct Team name
        - Team Position Setup window opens
        - Click on correct Team position
        - Click on History Tab
        - Click Add button
        - Change Effective Date if appropriate
        - Click on Reason down arrow
        - Select a reason from the drop down list
        - Click OK button
        - Click Close button
        - Now the Position is inactive
    **Steps:		Determine if Position should be inactive - If NO**
        - You need to make this Position active.
        - (The following steps are necessary to make position active.)
        - Click Team pull down menu
        - Select Positions
        - Double Click on correct Team name
        - Team Position Setup window opens
        - Click on correct Team position
        - Click on History Tab
        - Click Add button
        - Change Effective Date if appropriate
        - Click on Reason down arrow
        - Select a reason from the drop down list
        - Click OK button
        - Click Close button
        - Now the Position is active

### Error Report Window

Below is an example of the Error Report Window which may appear if a specified action cannot be processed. A description of the error will appear in the window. You may print the error message. It will print to a windows device and not a VistA device.

<!-- image -->

**Process** - Shows what action was being taken at the time of the error.

**Lines** - Number of lines in the error message.

**Errors** - Number of errors being reported in the error message.


## PCMM Business Rules

The PCMM Business Rules provide information on how some of the PCMM fields will be handled for team, team positions, and patient assignments. These rules are not intended to be all encompassing, but for general information purposes to allow some basic checking within the system to ensure data integrity.

### Primary Care Team Business Rules

*A Primary Care Provider is a Staff Physician, Physician Assistant, or Nurse Practitioner.*

*An Associate Provider is a Resident and can be a Physician Assistant and a Nurse Practitioner.*

1. A patient cannot have more than one primary care provider.
2. A primary care provider is authorized to provide primary care and can act as a preceptor. A preceptor is a primary care provider who oversees the activities of an associate provider. The preceptor is the ultimate responsible person for the patient care provided.
3. An associate provider is authorized to provide primary care, but cannot act as a preceptor.
4. A staff physician is never an associate provider.
5. A physician assistant (PA) and nurse practitioner (NP) can be either the primary care provider (PCP) or an associate provider (AP). However, they cannot be both for the same patient.
6. An associate provider cannot be the primary care provider.
7. An associate provider must have a preceptor link to a primary care provider. An associate provider is not authorized to act on his/her own.
8. If a position has a preceptor assigned, that position cannot be a primary care provider or precept over another position. However, this position can and should be marked “can provide primary care”.
9. If a position is marked as “can provide primary care”, the preceptor assigned to this position must also have “can provide primary care” marked.
10. Primary care patient assignment cannot be made to an associate provider who does not have a preceptor assigned.
11. If “can act as preceptor on Primary Care Team” is marked, then “can provide primary care” must also be marked.
12. In order to be a preceptor on a primary care team, the provider must be able to provide primary care.
13. Establishing a preceptor link will report the associate provider and the primary care provider as active staff members in those positions.
14. The inactivation of a patient's PCMM assignment will continue even if a provider change is found.
15. When attempting to remove a primary care provider (preceptor) link from an associate provider, the software will check for patient assignments. If there are patient assignments, the user will not be allowed to leave the preceptor link empty (blank). If there are no patient assignments, the preceptor link may be removed. Once a preceptor link is removed, the associate provider doesn’t become the primary care provider, as the associate provider is not authorized to be the primary care provider
16. Assignments are valid until the end of a day. This allows for the enforcement of the rule that a patient cannot have more than one primary care provider on a given day. (TIP:  If you want to inactivate an assignment immediately, assign an inactive date of yesterday.)

### Team Setup

1. Required information for team setup includes team name, purpose, service, and institution. Additional data fields are optional and further define the team (phone no., description, default team printer, primary care team restrict consults, team closed, auto-assign to team from clinic, auto-discharge from team from clinic, team assignments allowed.)
2. The team name can be changed, but it must be a unique entry. Any name entered to replace an existing team name will be checked. If there is already a team with that name, whether active or inactive, replacement will not be allowed. You will be asked to confirm all name changes.
3. The deletion of any team is not permitted once a history entry has been established. Once a team is in use, you may inactivate it, but not delete it. If you attempt to delete, you will be given the warning message “The following conditions prevent deletion: History entries are entered”.

### Team History

1. When adding a new entry to the team history, the effective date, status, and reason for the entry must be completed before the entry can be saved.
2. When adding a new entry, the effective date for the new entry cannot be earlier than a previous entry in the history. For example, a new entry that would reactivate a team that was inactivated on September 1, could not have a date earlier than September 1.
3. You cannot have two consecutive entries of the same status.
4. You can only delete the latest date entry in the history list. Once another entry has been made which supersedes a previous entry, that entry can no longer be deleted.
5. The date for an existing entry can only be changed if it does not conflict with any of the other entries in the history. Since there may be other packages using this data in the future, changing a date could cause potential problems. Date changing should be reserved for only those occasions when an entry was made in error. If you change an existing date, you will be asked to confirm it.
6. The “reason” for any history entry can be changed.
7. The status cannot be changed for an existing entry. There are only two status values, active and inactive.
8. In order for a team to be inactivated, all positions and staff assignments must be inactivated.

Team Position Setup

- General required information for position setup includes position, role, and message notifications. Additional data fields are optional and further define team purpose (description, beeper, can provide primary care, can act as a preceptor, associated clinic, and number of patients allowed for position).
- See the Primary Care Team Business Rules concerning associate provider and positions that can act as a preceptor on a primary care team.
- The position name can be changed, but it must be a unique entry within the team. You can use the same name for any number of different teams, but not within the same team. Any name entered to replace an existing name will be checked. If there is already a position with that name within the team, whether active or inactive, replacement will not be allowed. You will be asked to confirm all name changes.
- The deletion of any position is not permitted.
- If a position is created in error, you will be able to remove it up until you assign a patient to it, or change its current status. Once a position is in use, you may inactivate it, but not delete it.

### Team Position History

1. When adding a new entry to the team position history, the effective date, status, and reason for the entry must be completed before the entry can be saved.
2. When adding a new entry, the effective date for the new entry cannot be earlier than a previous entry in the history. For example, a new entry that would reactivate a position that was inactivated on September 1, could not have a date earlier than September 1.
3. You cannot have two consecutive entries with the same status.
4. If you inactivate a position and there is a staff member currently active in the position, a warning message will display stating that the Team Member is Active in Position.
5. You can only delete the latest (last) history entry. Once another entry has been made which supersedes a previous entry, that entry can no longer be deleted.
6. The date for an existing entry can only be changed if it does not conflict with any of the other entries in the history. Since there may be other packages using this data in the future, changing a date could cause potential problems. Date changing should be reserved for only those occasions when an entry was made in error. If you change an existing date, you will be asked to confirm it.
7. The “reason” for any history entry can be changed.

Team Position Staff History

1. Only one staff member can be assigned to a position at any given time.
2. If there already is an active staff member, you will only be allowed to inactivate the current staff member.
3. The status cannot be changed for an existing entry. There are only two status values, active and inactive.
4. When assigning a new staff member to a team position, the member’s name, effective date, status, and reason for the assignment must be completed before the assignment can be entered.
5. When adding a new staff member to a position, the effective date for the new assignment cannot be earlier than the inactivation date of the previous assignment.
6. Only the last assignment entry can be deleted.
7. The date for an existing assignment can only be changed only if it does not conflict with any of the other assignment entries. Since there may be other packages using this data in the future, changing a date could cause potential problems. Date changing should be reserved for only those occasions when an entry was made in error. If you change an existing date, you will be asked to confirm it.
8. The “reason” for any history entry could be changed.
9. The “status reason” for an existing entry may be changed only if it is the latest assignment entry in the Assignment History log and has a status of inactive.

### Patient Team Assignment

1. The Inconsistency Report displays patients that are assigned to a primary care team without a position assignment. The assignments that are identified will require action.
2. Only teams that have the “Primary Care Team” box checked on the Settings Tab of the Team Setup Screen may be assigned as a primary care team. **Note:** This field determines if a team can ever be a primary care team. The team's purpose does not affect the ability of a team to function as a primary care team.
3. A patient can only be assigned to one primary care team on any given date.
4. A patient can be assigned to more than one non-primary care team.
5. In the Multiple Patient Assignments to a Team option, patients currently assigned to the destination team are not listed in the “Available to Assign” list as they are already assigned to that team.
6. In the Multiple Patient Assignments to a Team option, if “Make this a Primary Care Team Assignment” is checked, patients who do not have a primary care team will be assigned this team as their primary care team. Patients who have already been assigned to another team as their primary care team will not be assigned to the team.

Patient Team Position Assignment

1. In order for a position to be designated as the primary care practitioner position, the following conditions must exist:

the team must be able to provide primary care

the team must be designated as the patient’s primary care team

the position must be able to provide primary care

the patient can have no other position designated as primary care practitioner.

1. See the Primary Care Team Business Rules concerning associate provider and positions that can act a preceptor on a primary care team.
2. A patient cannot have more than one primary care provider on any given date.
3. Only positions from the patient's primary care team may serve as the primary care provider.
4. In multiple patient assignment, the assignment will fail if the patient is already assigned to a primary care team or a primary care position.
5. In multiple patient assignment, the assignment will fail if a death entry has been entered for the patient.
6. In the Multiple Patient Assignments to a Position option, selected patients who have not yet been assigned to the position's team and are permitted to be assigned to the position (e.g., no conflicts with primary care assignments) will be assigned to the team at the same time.
7. Assigning patients by using the Multiple Patient Assignment to a Position option automatically enrolls patients to the team with which the position is assigned.

Processing Team Reassignments

1. Team reassignment must be made from a source team to a destination team.
2. Team reassignment from a source team to a destination team can be made when the team exists now or in the future.

Processing Position Reassignments

1. Position reassignment must be made from a source position to a destination position.


## Security Key Changes

The PCMM security key assignments to the VistA PCMM Main Menu, along with its associated menus and options, have been changed as recommended by the PCMM User Workgroup.

**Security key changes as of August 2007**

The following options no longer require a security key.

SCMC EXTENDED REPORT

SCMC FLAGGED

SCMC INACTIVATED REPORT

SCMC PRACTITIONER FLAGGED

SCMC PC STAFF AUTO INACTIVATE

SCMC PCMM MAIN MENU

To access the following options, the user will need the SC PCMM SETUP security key.

SCMC PCMM NIGHTLY TASK

SCMC RETRANSMIT

SCMC PCMM ERR CODE REPORT

SCMC EXTEND A PATIENT

To access the following options, the user will need the SCMC PCMM RETRANSMIT security key.

SCMC PCMM TRANS ERROR PROC

SCMC PCMM TRANS ERROR REPORT

## Glossary

| ACOS                                        | Associate Chief of Staff                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ADMIN COORDINATOR                           | The administrative coordinator for Primary Care and Non-Primary Care Teams. This person is involved with administrative (MAS requirements and/or Clinic Administration) duties as well as oversight of the Scheduling process and Primary Care team definition.                                                                                                                                                                                                                                                                                                                                   |
| ARROW                                       | <!-- image -->  <!-- image -->  <!-- image -->  Arrow is a symbol (   ) that is used to scroll up and down lists, and left to right for moving objects.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ASSOCIATE PROVIDER                          | An Associate Provider is authorized to provide primary care, but cannot act as a Primary Care Provider. In PCMM, a Resident is designated as an Associate Provider. A Nurse Practitioner and/or Physician Assistant may be designated as an Associate Provider also. Per VHA Directive, every patient is to be assigned to a Primary Care Provider who is responsible for coordinating a patient’s overall care. The Associate Provider on a Primary Care Team must be assigned to a preceptor who can be a Primary Care Provider (must have a Primary Care Provider preceptor assigned to them). |
| AUSTIN INFORMATION TECHNOLOGY CENTER (AITC) | The central repository for National Care Patient Care Database (formerly the Austin Automation Center (AAC)).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| AUTO TEAM ENROLLMENT/DISCHARGE              | This is an option when setting up teams that will automatically enroll a patient to a team when the patient is enrolled in a clinic that is associated with that team. You can also discharge from a team (if not assigned to a position in a team) when the patient is discharged from a clinic associated with that team.                                                                                                                                                                                                                                                                       |
| BUTTON BAR                                  | Small boxes that contain graphic figures that represent various functions. Also referred to as Tool Bar.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| CALENDAR DISPLAY                            | Within PCMM, when there is a date field, the user can “double click” the field and a miniature calendar will ‘pop up’ for selection of a date and year. This is used for activation and deactivation dates as well as discharge dates.                                                                                                                                                                                                                                                                                                                                                            |
| CLERK                                       | This person is a clerk who performs data entry.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| CLINICAL PHARMACIST                         | Performs patient care duties related to patient medications as assigned or granted by the appropriate governing committee at the facility. These privileges may include and may or may not be limited to:  1. Initiation of renewal orders for chronic maintenance medications 2. Initiation of orders for laboratory tests necessary to monitor existing drug therapy.                                                                                                                                                                                                                           |
| CLINICAL SERVICE                            | A Service defined at the medical center, e.g. MEDICINE, SURGERY, INTERMEDIATE MEDICINE, etc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| CLOSING                                     | Another term for ‘inactivating’ a position or team.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| CONSULTS                                    | When a patient is referred to a clinic on a one-time basis, he/she is not normally enrolled in that clinic.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| CONTROL KEY                                 | A Control Key is the key on the lower left and right hand side of the keyboard that is entitled ‘CTRL’. When a user presses this key along with another character (e.g. CTRL + O), the user can select and OPTION, etc.                                                                                                                                                                                                                                                                                                                                                                           |
| DATABASE                                    | This refers to the information that is stored in your medical center’s computer program, e.g., patient information, service information, clinic information, etc.                                                                                                                                                                                                                                                                                                                                                                                                                                 |

| DIALOGUE BOX       | A dialogue box is a box or window that is placed within a screen that allows the user to enter a ‘free text’ message or description of the object being created (in some cases, the description of what a team is supposed to represent).                                                                                                                                                                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DIETITIAN          | Performs patient care duties related to nutrition and weight management                                                                                                                                                                                                                                                                                                                                                                                                           |
| DISPLAY BOX        | This is a ‘box’ or window that ‘DISPLAYS’ information or lists available clinics, positions or teams to choose from. The user may select an item from the list displayed.                                                                                                                                                                                                                                                                                                         |
| DOUBLE ARROW       | A ‘double arrow’ is just that (two arrows next to each other) indicating that more than one patient name may be moved over from an inactive status to an active status and back to an inactive status. (>>)                                                                                                                                                                                                                                                                       |
| DROP DOWN LIST     | When a user selects an item from the MENU BAR, a list is displayed in a vertical format. For example, if a user selects FILE, a list drops down showing all options that are available under the main heading FILE: File, Edit, Print, Save                                                                                                                                                                                                                                       |
| E-MAIL MESSAGES    | These are the messages that are generated by a software event that delivers information to designated users via MailMan. E-mail messages in the PCMM module would include information about death notifications, inpatient movements, consult notifications, and team notifications or changes.                                                                                                                                                                                   |
| ENHANCEMENT        | An ‘enhancement’ to an already existing Class I software package is the introduction of new or improved functionality.                                                                                                                                                                                                                                                                                                                                                            |
| GUI                | Graphical user Interface                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| FTEE               | Full Time Employee Equivalent. Applies to any staffed team position.                                                                                                                                                                                                                                                                                                                                                                                                              |
| HIGHLIGHT          | To ‘Highlight’ a name, team, position, or date, one would place the cursor (or arrow) on the name, team, or position they wish to choose and ‘click’ the mouse button to select it or highlight it.                                                                                                                                                                                                                                                                               |
| HISTORY FILE       | Although not specific to any one document, a history file is a compilation of various pieces of information pertaining to individual teams, positions, etc. for future reference and clarification.                                                                                                                                                                                                                                                                               |
| ICON               | An Icon is an image or snapshot of something that is visually understood and is represented in a ‘box’. For instance, an ICON that stands for ‘cutting’ a piece of text out of a document would be a box with a picture of a pair of scissors in it. They are also known as ‘buttons’.                                                                                                                                                                                            |
| INTERN (PHYSICIAN) | Performs patient care duties in accordance with Medical Center Policy and is supervised by a Preceptor who can act as a Primary Care Practitioner. Duties include, but may not be limited to, (1) completing history & physical examinations, (2) obtaining blood and other specimens, and (3) provision of patient medical care as permitted. Cannot act as Primary Care Provider. The Intern is an Associate Provider within a Primary Care Team (see Associate Provider Term). |
| IRM                | Information Resources Management                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| LOG OFF            | This is referred to logging off or signing out of a particular software package or system. To end the session, to ‘get out’ of a package, etc.                                                                                                                                                                                                                                                                                                                                    |
| LOG ON             | This is referred to logging on or signing onto a particular software package or system. To open or start a new session.                                                                                                                                                                                                                                                                                                                                                           |
| MACRO              | A shortcut for performing various tasks. For example, the CTRL key (as explained above), combined with certain letters performs functions or tasks without having to select a menu bar item.                                                                                                                                                                                                                                                                                      |
| MAS ADPAC          | Medical Administration Service Automated Data Processing Applications Coordinator                                                                                                                                                                                                                                                                                                                                                                                                 |
| MEDICAL STUDENT    | Performs patient care duties in accordance with Medical Center Policy and is supervised by a Preceptor who can act as a Primary Care Practitioner.                                                                                                                                                                                                                                                                                                                                |

| MENU BAR                   | A Menu Bar is usually listed at the TOP of a computer screen and it, unlike the tool bar, displays words as opposed to pictures. For example, the menu bar for FILE OPEN can be selected, but it can also be selected from a picture of a folder opening. The menu bar is just the ‘words’ for various functions. The menu bar as ‘drop down lists’ as explained above.                                                                                                                                                                                                                                                 |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MODULE                     | A portion of a major software package, e.g. Primary Care functionality is considered a MODULE of the Scheduling package.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| NPCD                       | National Patient Care Database - is maintained in Austin and receives selected demographic and encounter-based clinical, diagnostic data form VA medical centers. This data enables a detailed analysis of VHA inpatient and outpatient health care activity.                                                                                                                                                                                                                                                                                                                                                           |
| NURSE (LPN)                | Provides a variety of nursing services that do not require full professional nurse education, but are represented by the licensing of practical and vocational nurses by a State, Territory or the District of Columbia. Persons in these positions may also provide administrative assistance, such as making appointments, etc.                                                                                                                                                                                                                                                                                       |
| NURSE (RN)                 | Provides care to patients in clinics and other settings, administers anesthetic agents and supportive treatments to patients undergoing outpatient surgery and other medical treatments, promotes better health practices, and consults or advises nurses providing direct care to patients. Persons in this position require a professional knowledge and education in the field of nursing.                                                                                                                                                                                                                           |
| NURSE PRACTITIONER         | Performs patient care duties in accordance with Scope of Practice under the supervision of a designated physician or physicians and Medical Center Policy. Duties include, but are not limited to, appropriate assessments, orders diagnostic tests and consultations as necessary, prescribes treatment interventions in accordance with established protocols, provides or arranges follow-up care, and provides health teaching and supportive counseling. Is authorized to act as a Primary Care Provider or Associate Provider. The ability to act as a Primary Care Provider is decided by individual facilities. |
| OIF/OEF                    | Operation Iraqi Freedom/ Operation Enduring Freedom                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| OTHER                      | A general classification for those team members who do not belong in any of the listed Standard Position entries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| PANEL                      | A panel is a group of individual patients for which the Primary Care Provider has accepted primary care responsibility.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| PATIENT PANEL              | Group of individual patients assigned to Team/Position/  Practitioner. Can be either Primary Care or Non Primary Care patients; e.g., the Practitioner’s Patients Report includes both Primary Care and Non Primary Care patients assigned to the practitioner or other team position in the Patient Panel Count.                                                                                                                                                                                                                                                                                                       |
| PATIENT SERVICES ASSISTANT | Provides clerical and patient processing support to outpatient clinics, or other unit of a medical facility, in support of the care and treatment given to patients. This includes duties as receptionist, record-keeping duties, clerical duties related to patient care, and miscellaneous support to the medical staff of the unit.                                                                                                                                                                                                                                                                                  |
| PC COORDINATOR             | Primary Care Coordinator                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| PCMM                       | Primary Care Management Module                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| PCs                        | Personal computers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| PERSON CLASS FILE          | Consists of provider taxonomy developed by Health Care Finance Administration (HCFA). The taxonomy codifies provider type and provider area of specialization for all medical related providers.                                                                                                                                                                                                                                                                                                                                                                                                                        |

| PHYSICIAN ASSISTANT                   | Performs patient care duties in accordance with Scope of Practice under the supervision of a designated physician or physicians and Medical Center Policy. Duties include, but are not limited to, diagnostic and therapeutic medical care and services, taking case histories, conducting physical examinations, and ordering lab and other studies. Physician Assistants also may carry out special procedures, such as giving injections or other medication, apply or change dressings, or suturing minor lacerations. The ability to act as a Primary Care Practitioner is decided by individual facilities.                                                                                                                                                                                                                                                                                            |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PHYSICIAN-PRIMARY CARE                | As a physician, incumbent's duties are to advise on, administer, supervise or perform professional and scientific work in one or more fields of medicine. The degree of Doctor of Medicine or Doctor of Osteopathy is a fundamental requirement, along with a current license to practice medicine and surgery in a US State, territory or the District of Columbia. As a Primary Care practitioner, the incumbent provides the first point of assistance for a patient seeking care. Primary Care duties include: (1) Intake and initial needs assessment, (2) Health promotion and disease prevention, (3) Management of acute and chronic biopsychosocial conditions, (4) Access to other components of health care, (5) Continuity, and (6) Patient and non-professional care giver education & training. (from IL 10-93-031, Under Secretary for Health's Letter) Can act as Primary Care Practitioner. |
| PHYSICIAN-PSYCHIATRIST                | As a physician, incumbent's duties are to advise on, administer, supervise or perform professional and scientific work in one or more fields of medicine. The degree of Doctor of Medicine or Doctor of Osteopathy is a fundamental requirement, along with a current license to practice medicine and surgery in a US State, territory or the District of Columbia. The incumbent is also granted clinical privileges (by the appropriate governing Credentials committee) in regard to the practice of Psychiatry.                                                                                                                                                                                                                                                                                                                                                                                         |
| PHYSICIAN-SUBSPECIALTY                | As a physician, incumbent's duties are to advise on, administer, supervise or perform professional and scientific work in one or more fields of medicine. The degree of Doctor of Medicine or Doctor of Osteopathy is a fundamental requirement, along with a current license to practice medicine and surgery in a US State, territory or the District of Columbia. The incumbent is also granted clinical privileges (by the appropriate governing Credentials committee) concerning the practice of Specialty or Subspecialty care in the areas of Medicine or Surgery.                                                                                                                                                                                                                                                                                                                                   |
| POSITION                              | Teams are comprised of one or more staff positions. Individual practitioners are assigned to a team position. A position is designated to serve certain roles in the overall primary care setting.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| PRECEPTOR                             | Responsible for providing the overall care for patients assigned to an Associate Provider or Medical Student. On Primary Care Teams, the Preceptor must be able to provide Primary Care.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| PRIMARY CARE                          | Primary care is the provision of integrated, accessible health care services by clinicians that are accountable for addressing a large majority of personal health care needs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| PRIMARY CARE MANAGEMENT MODULE (PCMM) | Primary Care Management Module is the application for VA facilities to use for implementing primary care teams. Teams are created, positions associated with the teams are created, staff members are assigned to positions, and patients are assigned to the teams and positions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| PRIMARY CARE PROVIDER                 | In PCMM, the Primary Care Provider is the position determined to be responsible for the coordination of the patient’s primary care.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

| PSYCHOLOGIST           | Performs patient care duties in accordance with Clinical Privileges as assigned or granted by the appropriate governing committee in the area of Psychology and Mental Health. This may include individual, family and group counseling and psychotherapy, assertiveness and other behavior training, etc.                                                                                                                                                                                                                                       |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| REHAB/PSYCH TECHNICIAN | Provides patient care in accordance with Clinical Privileges as assigned or granted by the appropriate governing committee in the area of Psychology and Mental Health. This may include individual, family or group counseling. A degreed Psychologist or Mental health practitioner typically supervises the incumbent.                                                                                                                                                                                                                        |
| RESIDENT (PHYSICIAN)   | Performs patient care duties in accordance with Medical Center Policy and is supervised by a Preceptor who can act as a Primary Care Practitioner. Duties include, but may not be limited to, completing history and physical examinations, obtaining blood and other specimens, and provision of patient medical care as permitted. The resident is an Associate Provider within a Primary Care Team. As a Resident, the incumbent is responsible for providing patient care as directed by the Preceptor. Cannot act as Primary Care Provider. |
| RIGHT CLICK            | Normally on a computer ‘mouse’ there is two buttons at the top of the mouse. The button or area that can be ‘clicked’ on the right, is known as the RIGHT CLICK button.                                                                                                                                                                                                                                                                                                                                                                          |
| ROLE                   | A function or task of a staff member involved with the implementation, maintenance and continued success of primary care.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| SOCIAL WORKER          | Performs patient care duties in accordance with Clinical Privileges as assigned or granted by the appropriate governing committee in the area of Social Work. Provides direct services to individuals, groups and families with counseling, discharge planning, crisis intervention, etc.                                                                                                                                                                                                                                                        |
| SPECIALTY CLINICS      | A set of clinics that are defined as SUBSETS of generalized Service clinics such as Cardiology (specialty of Medicine); Orthopedics (specialty of Surgery), etc.                                                                                                                                                                                                                                                                                                                                                                                 |
| TEAM                   | Teams are groups of staff members organized for a certain purpose (e.g., Primary Care).                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| TEAM PHARMACIST        | A pharmacist who: (1) Is authorized to Fill/Dispense medications (2) Enter/Verify medication orders (3) Provide patient education relating to medications (4) Renew established medications under the protocols defined by the medical center.                                                                                                                                                                                                                                                                                                   |
| TEAM PROFILE           | This is a screen within PCMM that shows the various characteristics of a particular team, e.g., number of patients allowed for enrollment, name, positions assigned, etc.                                                                                                                                                                                                                                                                                                                                                                        |
| TEXT BOX               | The text box is also known as the DIALOGUE box as described above. It provides the user with an area in which to identify certain characteristics of a particular component of PCMM. For example, the description of what a team is for (provides primary care to patients that have been discharged from the hospital within the last 6 months).                                                                                                                                                                                                |
| TITLE BAR              | Title bar is the bar that shows the TITLE of the screen that the user is presently accessing. For instance, the TITLE BAR on the Team Set-Up screen could be ‘Team Profile’.                                                                                                                                                                                                                                                                                                                                                                     |
| TOOL BAR               | The Tool Bar is what is displayed either at the top of the screen or at the button, and contains a picture of all of the available ICONS that may be chose to perform certain tasks. Unlike the MENU BAR, the menu bar contains the ‘words’ for functions, whereas the TOOL BAR contains the ‘pictures’ that represent functions.                                                                                                                                                                                                                |
| TOOL BUTTONS           | A tool button is ONE of the icons that is shown across the top (or bottom) of a screen on the TOOL BAR.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| TPA                    | Transition Patient Advocates assist in tracking the treatment of seriously ill veterans of Operation Iraqi Freedom (OIF) and Operation Enduring Freedom (OEF)                                                                                                                                                                                                                                                                                                                                                                                    |
| UNIQUES                | Uniques for the purpose of PCMM Primary Care are defined as the individual veteran (patient) enrolled in VA health care that makes up the primary care provider’s panel.                                                                                                                                                                                                                                                                                                                                                                         |
| USER CLASS             | User Class is a file that will be transported with the Primary Care Management Module that stores the users (physicians, social workers, staff clerks, etc.) actual position titles as defined by the site.                                                                                                                                                                                                                                                                                                                                      |
| VistA                  | Veterans Health Information Systems and Technology Architecture, formerly known as Decentralized Hospital Computer Program, encompasses the complete information environment at VA medical facilities.                                                                                                                                                                                                                                                                                                                                           |

## Appendix - Examples of PCMM Reports

**This section provides brief examples of PCMM Reports. Selecting different options will change the content of the reports. All of the data included in the sample reports is for illustration purposes – No live data is used. Actual Reports will be much longer.**

Team/Position Assignment/Re-Assignment

<!-- image -->

### Patient Listing for Team Assignments

<!-- image -->

Patient Team Position Assignment Review

<!-- image -->

### Historical Patient Position Assignment Listing - Detail

<!-- image -->

### Historical Patient Position Assignment Listing - Summary

<!-- image -->

### Patients Scheduled for Inactivation from PC Panels

<!-- image -->

### Patients with Extended Primary Care Inactivation

<!-- image -->

Patients Automated Inactivations from PC Panels

<!-- image -->

### Extend Patient Inactivation Date

<!-- image -->

### PCMM Edit Practitioner in Position Assig. File

<!-- image -->

### Practitioner Demographics

<!-- image -->

### Practitioner's Patients

<!-- image -->

### Historical Provider Position Assignment Listing

<!-- image -->

### PCMM Inconsistency Report

<!-- image -->

### FTEE and Panel Size Report

<!-- image -->

| REPORT  KEY                    |                                                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Column Heading                 | Explanation of column heading.                                                                                                                                                                                                                                                                                                                                                                    |
| Provider's Name                | The name of the Provider.                                                                                                                                                                                                                                                                                                                                                                         |
| TEAM                           | The name of the team to which this position (and therefore provider) is assigned.                                                                                                                                                                                                                                                                                                                 |
| Team Position                  | The name of the team position to which this provider is assigned.                                                                                                                                                                                                                                                                                                                                 |
| AP or PCP                      | This column displays whether this provider is an Associate Primary Care Provider (AP) or a Primary Care Provider (PCP).                                                                                                                                                                                                                                                                           |
| Associated Clinic(s)           | The scheduling clinic(s) associated with this position/provider in the PCMM software.                                                                                                                                                                                                                                                                                                             |
| FTEE                           | The number of hours the provider spends providing care expressed as a Full-Time Employee Equivalent Examples: One FTEE=1.00=40 hours per week. 0.75 FTEE=30 hours per week. 0.50 FTEE=20 hours per week. Percent FTEE is equal to 100 x the FTEE number on this report. For example FTEE=0.75= 75%.                                                                                               |
| Patients for Position  Allowed | This represents the total maximum number of patients this provider is expected to care for on this panel.  This number is entered in the PCMM GUI 'Primary Care Team Position Setup' window on the 'Settings' tab. Additional patients above this number may be assigned to the provider depending on local management policy.                                                                    |
| Patients for Position  Actual  | The actual current number of active patients assigned to this provider in PCMM at the time of this report.  This number displays on the PCMM GUI 'Primary Care Team Position Setup' window on the 'Settings' tab different FTEE values. Example, Active patients 500/0.85 FTEE=588. This is the number of patients this provider would be expected to provide primary care for if their FTEE=1.0. |
| FTEE and Panel Size Total      | The total number of FTEE, patients for positions allowed, patients for positions actual, and available patient opening for this report. If this report is sorted on Associated Clinic, then subtotals for each clinic and a total for the entire report print. If this report is sorted on Team, then subtotals for each team and a total for the entire report print.                            |

### Staff Sched for Inactivation

<!-- image -->

<!-- image -->

### Staff Inactivated Report

<!-- image -->

### Individual Team Profile

<!-- image -->

### Team Member Listing

<!-- image -->

### Team Patient Listing

<!-- image -->

### Summary Listing of Teams

<!-- image -->

### Historical Patient Assignment Detail

--------------------------------------------------------------------------------

&lt;*&gt;  HISTORICAL PATIENT ASSIGNMENT DETAIL  &lt;*&gt;

For assignments effective OCT 7,2008 to OCT 7,2008

--------------------------------------------------------------------------------

Date printed: OCT 7,2008@14:22                                           Page: 1

--------------------------------------------------------------------------------

Patient: PCMMPATIENT, SIX  SSN: 666014621   DOB: JUL 21,1954  AGE: 54   FEMALE

--------------------------------------------------------------------------------

Assignment                  Active      Inactive    Assigned by/date

--------------------------  ----------  ----------  ----------------------------

PC Provider:

PCMMPROVIDER, ONE           10/05/2004              PCMMUSER, ONE (10/05/2004)

PC Associate Provider:  (none found)

PC Position:

PROV GREEN 6                10/05/2004              PCMMUSER, ONE (10/05/2004)

User Entering:

Last Edited By:

Status:

PC Preceptor Position:  (none found)

### Historical Provider Position Assignment Listing

<!-- image -->

### Historical Patient Position Assignment Listing

<!-- image -->

### Historical Team Assignment Summary

<!-- image -->

## Index


Accessibility 508 Complaint GUI	2

Appendix - Examples of PCMM Reports	161

Assign Multiple Patients to Team/Position	50

Assign Positions to a Team	20

Assign Preceptor to a Position	40

Assign Single Patient to Team/Position	43

Assign Staff Member to a Position	35

Autolinks	3


Background Tasks	6


Clean-Up Ghost Entries	130

Clean-Up Incorrect Team Institution Pointer	131

Create a New Team	13

Create a New Template	78, 84


Edit an Existing Team	71

Error Report Window	145

Examples of PCMM Reports	161


Form Buttons	134


Glossary	154


Historical Assignment Reports	116

HL7 Transmission	7


Logging On	6


Modify an Existing Template	80


Non Primary Care Team set up	3


OIF OEF Case Management	3

Overview of the Primary Care Management Module	1


Patient Reactivation of an Automatically Inactivated Patient	49

Patient Reports and Options	87

Patient Team Assignment Business Rules	149

Patient Team Position Assignment Business Rules	150

Patient Team Position Assignment Review	128

PCMM Business Rules	146

PCMM HL7 and Maintenance Menu	121

PCMM Nightly Task	6, 129

PCMM Parameters	6

PCMM Reassignment Mail Group	6

Primary Care Team Business Rules	146

Printing Reports	81

Processing Position Reassignments Business Rules	150

Processing Team Reassignments Business Rules	150

Provider/Position Reports	100


Query Template Utility	77, 83


Reassign Multiple Patients to Team/Position	58

Report Specifications	79

Report Templates	3

Reports	77

Reports – Roll and Scroll	86

Retransmit one Patient or Provider	130


SCMC HL7 Transmission	7

SCMC PCMM Nightly Task	6

Security Key Changes	152

Sensitive Information	2

Setting up OIF/OEF Teams	68

Single Patient Assignment	74

Stand-alone Options	123

Starting PCMM	5


Team History Business Rules	147

Team Position History Business Rules	148

Team Position Setup Business Rules	148

Team Position Staff History Business Rules	149

Team Reports	110

Team Setup	13

Team Setup Business Rules	147

Template Menu Bar Commands	82

Toolbar Speedbuttons	5

Troubleshooting Guide	136


Wait List (Sch/PCMM) Menu	122

Windows Conventions	3, 132