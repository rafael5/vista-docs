---
app_name: 'Registry: Airborne Hazard Open Burn Pit (AHOBPR) (PXRM)'
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: null
doc_type: release-notes
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
source_file: pxrm_2_24_rn.docx
status: draft
title: pxrm 2 24 rn.docx
---

## High Risk Mental Health Patient –

## National Reminder and Flag

Patches

DG*5.3*849

GMTS*2.7*104

PXRM*2*24

SD*5.3*588

TIU*1.0*265

OR*3.0*348

**Release Notes**

April 2013


Product Development

**CONTENTS**

Introduction	1

Related Documentation	2

Related Web Sites	3

Release Notes	4

Project Overview	4

Project Features	6

Registration – Patient Record Flag (DG)	6

Scheduling (SD)	8

Health Summary (GMTS)	11

Text Integration Utility (TIU)	16

Order Entry (OR)	16

Clinical Reminder s (PXRM)	17

Remedy Ticket and Other Fixes	24

Other Fixes	26

Acronyms	28

**FIGURES**

Figure 1.0 – PRF Category I Flag Example	13

Figure 2.0 – CPRS GUI Reports Tab, VA-MH HIGH RISK PATIENT Health Summary	14

Figure 3.0 – Reminder Resolution for High Risk MH No-Show Follow-up reminder	15

Figure 4.0 – No-show health factors entered at any time on the date of the missed appointment  resolve all no-show appointment follow-up on that day.	20

Figure 5.0 – Example Of VA-HIGH RISK MH NO-SHOW FOLLOW-UP Dialog, with changed information text	23

## Introduction

The purpose of the High Risk Mental Health Patient- National Reminder and Flag (HRMHP) project is to support Mental Health (MH) professionals in the tracking of Veterans with the High Risk for Suicide Patient Record Flag (PRF) who have missed Mental Health (MH) Clinic appointments due to a no-show.

This is the second release of the (HRMHP) project. It includes six patches, which will be installed as a combined build, HIGH RISK MH 2.0.

**PXRM*2.0*24 - MH HIGH RISK PHASE 2**

This Clinical Reminders patch includes an updated reminder, which includes a new computed finding (VA-PCMM MHTC), a new dialog that will display the MHTC, and a new Reminder (VA- MHTC NEEDS ASSIGNMENT).

**OR*3*348**

This patch adds a new provider recipient, Primary Care Management Module (PCMM) Mental Health Treatment Coordinator (MHTC), to the existing ORB PROVIDER RECIPIENTS parameter. A new notification is also being released with this patch: SUICIDE ATTEMPTED/ COMPLETED. This informational notification is triggered by Clinical Reminders when a MH SUICIDE ATTEMPTED or MH SUICIDE COMPLETED health factor has been documented in PCE. It will be added as a ‘C’ code to the existing ‘PATOMERS’ values.

**TIU*1.0*265**

This Text Integration Utility patch installs a new title to the TIU DOCUMENT DEFINITION (file #8925.1): PATIENT RECORD FLAG CATEGORY I – HIGH RISK FOR SUICIDE to be used with the new Patient Record Flag. The patch installation links the title to the existing document class PATIENT RECORD FLAG CAT I.

**DG*5.3*849**

This build installs a new national Patient Record Flag (PRF) for suicide prevention (HIGH RISK FOR SUICIDE). It also installs a new option that will allow the generation of new national PRFs for suicide prevention from local, active, suicide prevention PRFs.

**IMPORTANT DEPLOYMENT NOTE: SPC staff should NOT run the Processing mode of the DGPF LOCAL TO NATIONAL CONVERT option (Process Local-to-National option) until 30 days after the national release date and sites have also received approval from the national Office of Mental Health. This will help to minimize transmission error messages among sites with shared patients. These error messages occur when one of these sites has installed and runs the conversion, but another site that also sees the same patient(s) has not installed this newly released software patch(s). You MAY run the Report Only mode after installing the package, to get a preliminary report of local PRFs that will be converted.**

**SD*5.3*588**

This build contains two new proactive reports that list appointments for High Risk for Suicide patients who have appointments for the day. MHTC has been added to these reports and also to the SD MH NO SHOW AD HOC REPORT.

**GMTS*2.7*104**

This build modifies the Health Summary Component MH HIGH RISK PRF HX to now display the assignment status and history for the Category I HIGH RISK FOR SUICIDE Patient Record Flag and any assignment history found for the local Category II High Risk for Suicide flag. The Health Summary Component MH TREATMENT COORDINATOR is now fully functional and will display (if assigned) the Mental Health Treatment Coordinator (MHTC) for a given patient.  The information displayed will include the: name of the mental health treatment team, name of the MHTC, and office phone, analog pager and digital pager of the MHTC.


### Related Documentation

**Clinical Reminders PXRM*2*24 Documentation**

| **Documentation**            | **Documentation File name**   |
|------------------------------|-------------------------------|
| Installation and Setup Guide | PXRM_2_24_IG.PDF              |
| Release Notes                | PXRM_2_24_RN.PDF              |
| User Manual                  | PXRM_2_UM.PDF                 |
| Manager’s Manual             | PXRM_2_MM.PDF                 |

**Health Summary GMTS*2.7*104 Documentation**

| **Documentation**   | **Documentation File name**   |
|---------------------|-------------------------------|
| User Manual         | HSUM_2_7_104_UM.PDF           |
| Technical Manual    | HSUM_2_7_104_TM.PDF           |

**TIU*1*265 Documentation**

| **Documentation**                  | **Documentation File name**   |
|------------------------------------|-------------------------------|
| Clinical Coordinator & User Manual | TIUUM.PDF                     |
| Technical Manual                   | TIUTM.PDF                     |

**Scheduling SD*5.3*588 and Registration DG*5.3*849 Documentation**

| **Documentation**                                   | **Documentation File name**   |
|-----------------------------------------------------|-------------------------------|
| PIMS Technical Manual                               | PIMSTM.PDF                    |
| Scheduling User Manual – Outputs Menu               | PIMsSchOutput.pdf             |
| Scheduling User Manual - Menus, Intro & Orientation | PIMsSchIntro.pdf              |
| Patient Record Flag User Guide                      | PatRecFlagUG.pdf              |
| SDDG Install Review Guide                           | SDDG_Install_Review.pdf       |

**CPRS OR*2.0*348 Documentation**

| CPRS User Guide: GUI Version                 | CPRSGUIUM.PDF                     |
|----------------------------------------------|-----------------------------------|
| CPRS Technical Manual: GUI Version           | CPRSGUITM.PDF                     |
| CPRS Technical Manual                        | CPRSLMTM.PDF                      |

### Related Web Sites

| **SITE**                              | **URL**                                                                                                            | **DESCRIPTION**                                                                            |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| National Clinical Reminders site      | http://vista.med.va.gov/reminders                                                                                  | Contains manuals, PowerPoint presentations, and other information about Clinical Reminders |
| National Clinical Reminders Committee | [http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx](http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx) | This committee directs the development of new and revised national reminders               |
| Document Library                      | [http://www.va.gov/vdl/](http://www.va.gov/vdl/)                                                                   | Contains manuals for Clinical Reminders and related applications.                          |

## Release Notes


### Project Overview

This project addresses the New Service Request (NSR) &lt;&lt; NSR20070589 High Risk Mental Health Patient – National Reminder and Flag &gt;&gt;. The NSR was submitted by Kathleen Lysell, PCS, Mental Health Services and Jan Kemp, Associate Director for Education MIRECC.  This project is included in the Improve Veteran Mental Health (IVMH) initiative.

This request was submitted in support of recommendations from the Comprehensive VHA Mental Health Strategic Plan and VHA Handbook 1160.01, Uniform Mental Health Services in VA Medical Centers and Clinics, to improve continuity of care for Veterans receiving mental health services.

Major objectives of this request include:

1. Identify those Veterans who are at risk for suicide (Sites define this locally in the Patient Record Flag.)
2. Proactively seek to provide appropriate care to high risk, mental health patients who miss appointments
3. Evaluate patients for mental health disorders so that appropriate referrals can be made; identify those Veterans with a history of suicide attempt or suicidal ideation who miss an appointment; notify the mental health professional of the missed appointment; and track efforts to reach this Veteran.  If after three attempts, the Veteran is not reached, a staff member may need to call other patient contacts or request a welfare check.

The High Risk Mental Health Patient – National Reminder &amp; Flag is being released in two phases; the first phase was released in March 2012. This manual describes functionality available in phase two.

Phase 1 of this project provided the following:

1. Two new Scheduling reports that identify no-show “high risk for suicide” patients that missed their MH appointments,
2. A new national reminder and reminder dialog that will be used by providers to document results of following up with a high risk for suicide patient that missed a MH appointment, and
3. A new health summary type with MH-specific supporting information.

Phase 2 of this project provides the following:

1. Registration - Patient Record Flag enhancements will support distribution of a national HIGH RISK FOR SUICIDE PRF and tools for SPCs to automatically update patients based on the local High Risk for Suicide PRF.  Scheduling, Clinical Reminders, TIU, and Health Summary enhancements will access and display national HIGH RISK FOR SUICIDE PRF patient data.
2. The PCMM Mental Health Treatment Coordinator (MHTC) added to Scheduling reports, Health Summary objects, and Reminder Dialogs.
3. The Mental Health Suicide Behavior Report (SBR) Instrument available for use in our High Risk MH No-Show Follow-Up Clinical Reminder Dialog.

##### Remedy Tickets Fixed
242214
391498
573543
588393
592128
593623
606273
606623
610957
707134
710964
737901


781752

779803

### See pages ***19-22*** for details.

## Project Features


### Registration – Patient Record Flag (DG)

**DG*5.3*849** installs a new national Patient Record Flag (PRF): HIGH RISK FOR SUICIDE.

Clinically, the Category I PRF for high risk for suicide will not be available to the site until the install is completed. Furthermore, we recommend that the Category I HIGH RISK FOR SUICIDE PRF should not be assigned to a patient until the post-installation step is completed by an SPC on each VistA System. Until then, all of the high risk patients will continue to have the local Category II PRFs on their record that clinicians are accustomed to working with.

This build also installs a new option, Convert Local HRMH PRF to National [DGPF LOCAL TO NATIONAL CONVERT], which will allow an SPC to auto-generate new national PRFs for suicide prevention from local, active, suicide prevention Category II PRFs. **This option can be run in either Report-only or in Processing mode – but the Processing mode must not be run until OMHS informs the SPCs that it is OK to run.**

Select OPTION NAME: DGPF LOCAL TO NATIONAL CONVERT      Convert Local HRMH PRF to National     action

This option can be run in a report only mode which will provide a report

of what actions the local-to-national processing will perform.  Enter 'R'

to run the Report Only mode, or 'P' to begin the local-to-national PRF

processing.

Select one of the following:

R         Report Only

P         Process Local-to-National

Select which mode to run: R//Select which mode to run: R// R   Report Only

&gt;&gt; Results have been sent to the 'DGPF CLINICAL HR FLAG' mail group

When run in the report mode, reports will be generated and sent via MailMan to the new DGPF CLINICAL HR FLAG REVIEW mail group, showing which local PRFs can be processed, which ones may have potential errors needing to be corrected first, and which ones may need to be processed manually.

Pre-Report Example

Subj: Pre-report National Flag Create 5/9/12@14:56 [#129309] 05/09/12@14:56

47 lines

From: HRMH PRF GENERATE JOB In 'IN' basket.   Page 1 Priority!

Pre-scan summary from Local to National flag processing job

Run date: May 09, 2012@14:56:52

Started by: DGDEVELOPER, ONE

Summary of PRF Processing:

Total active Cat II flag assignments:   12

Cat I flags created:                     5

Potential errors Found:                  5

Cat II flags requiring manual action:    0

Found active Cat I and Cat II flags:     2

When run in the processing mode, the actual processing of the national PRFs from the local PRFs will take place.

 **IMPORTANT DEPLOYMENT NOTE: SPC staff should NOT run the Processing mode of the DGPF LOCAL TO NATIONAL CONVERT option (Process Local-to-National option) until 30 days after the national release date and they have also received approval from the national Office of Mental Health. This will help to minimize transmission error messages among sites with shared patients. These errors messages occur when one of these sites has installed and runs the conversion, but another site that also sees the same patient(s) has not installed this newly released software patch(s). SPC staff may run the Report Only mode of the option after installing the package, to get a preliminary report of local PRFs that will be converted.**

The process to generate the new national (category I) PRFs from the local (category II) PRFs will take existing, active, local PRFs for high risk for suicide and determine whether a national PRF can be created from the local PRF. If there is any issue with generating a national PRF, either an error message will be logged, or the record will be flagged for manual action by the suicide prevention coordinator. In this case, no national PRF is created and the local PRF will remain intact.

Basic requirements of auto-creating national PRF entries

- Local flag MUST BE currently active
- Local flag information will be pulled into the new National flag at creation.
- Various comments are updated to reflect auto-created information.
- If there is an issue with generating a National flag:
    - No National flag is created
    - Local flag remains intact
    - Error report will be generated
If a new national PRF can be created, the information from the local PRF will be used in creating the new national PRF, and upon successful creation of the new national PRF, the local PRF will be inactivated with a comment indicating a new national PRF has been created.
Upon creation of the new national PRF, the existing HL7 messaging functionality will be used to transmit the national PRF information to other known treating facilities, as is currently done when a National PRF is entered through the Patient Record Flag assignment menu.
**Ownership of Category I flag**
Each Category I flag assignment to a specific patient’s record is owned by a single facility. The facility that placed the Category I flag on the patient’s record would normally own and maintain the flag. The site that owns the Category I flag is the only site that can:
    - Review whether to remove or continue the flag
    - Edit the flag
    - Inactivate the flag
    - Reactivate the flag
    - Mark the flag as entered in error
    - Change ownership of the flag
    - Enter a Patient Record Flag Category I progress note for the flag
However, ownership of a Category I flag assignment can be transferred. If a patient received the majority of care at a different VA facility than the one that assigned the flag, the site giving the majority of care could request that ownership of the flag be transferred to the that site. The owning site could then change the ownership to the second site through the PRF software in List Manager.
DG*5.3*849 post-installation steps on every VistA system:
    - For each VistA system, OMHS will task an SPC to complete the post-install step that will automatically convert the Category II flag to the Category I flag (Process mode of DGPF LOCAL TO NATIONAL CONVERT option).
    - After all sites have installed HRMHP Phase 2 patches, the Office of Mental Health Services (OMHS) will announce on their SPC conference calls and via Outlook that the Process Mode of the DGPF LOCAL TO NATIONAL CONVERT option can now be run by the assigned SPC for the VistA system.
    - The assigned SPC will be responsible for ensuring that the Report-Only mode has already been run and resolved any patient issues found before running the Process mode.
    - The SPC will be responsible for regularly monitoring the PRF TRANSMISSION MANAGEMENT option to ensure that there are no transmission errors between their system and other systems due to the Process mode.
    - Any issues should be dealt with between the SPCs at each site.  For example, if two sites treating the same patient had the Category II flag, than the PRF TRANSMISSION MANAGEMENT option will inform them of the situation, and the SPCs will figure out which site should be the owner and use the Patient Record Flag Management option to assign/change the ownership.
    - The SPC will be responsible for reporting back to the OMHS when the process mode is completed.

#### Scheduling (SD)

**SD*5.3*588** contains two new proactive reports that list appointments for High Risk for Suicide patients who have appointments for the day. The SD MH PROACTIVE BGJ REPORT is a background job that will run in the background and send a mail message to the members of the SD MH NO SHOW NOTIFICATION mail group.

**IMPORTANT NOTE** : This report will be kicked off by the Scheduling nightly background job (SDAM BACKGROUND JOB) that should already be scheduled to run nightly on your system. It is the same background job that calls the High Risk MH No-Show Nightly Report [SD MH NO SHOW NIGHTLY BGJ].

**IMPORTANT NOT** E: DO NOT schedule these options:

- SD MH NO SHOW NIGHTLY BGJ
- SD MH PROACTIVE BGJ REPORT

Scheduling’s Nightly Background Job generates these reports.

An ad hoc report option, High Risk MH Proactive Adhoc Report SD MH PROACTIVE AD HOC REPORT, generates a proactive report that can be run by the users. This report is more flexible and allows users to refine the report to their specifications.

This report will list, by divisions, all patients with PRF High Risk for Suicide who have appointments in mental health clinics today. Totals will list the number of unique patients by division. The patients will list alphabetically by division and by date/time of the appointment.

This build also allows the SD MH NO SHOW AD HOC REPORT and SD MH NO SHOW NIGHTLY BGJ reports as well as the SD MH PROACTIVE AD HOC REPORT and SD MH PROACTIVE BGJ REPORT to now look for PRF activity from the new national Category I PRF “HIGH RISK FOR SUICIDE,'” as well as from the local PRF.

This patch contains format changes to two no show reports, High Risk MH No-Show Adhoc Report [SD MH NO SHOW AD HOC REPORT] and High Risk MH No-Show Nightly Report [SD MH NO SHOW NIGHTLY BGJ]:

The following changes were made for both reports:

- The provider name is now displayed directly under the No Show Appointment information, to keep everything connected
- Key for appointment status abbreviations (NS, NA, NAT) added to the heading and will now print on every page break.
- Appointment line now displays information in two lines:
    - line one: count, patient name , Patient ID 1st initial last name+last 4 ssn, appointment D/T, 30 character clinic name
    - line two: appointment status abbreviation, appointment provider name.
        - Patient ID is now 5 characters: first initial of last name + last 4 of SSN
        - 30-character Clinic name in both future and appointment data information
        - AM and PM removed from the date/time of appt.
    The High Risk MH No-Show Adhoc Report also includes the following changes:
        - The report now displays the name of the Mental Health Treatment Coordinator (MHTC) and the name of the care team they are assigned to in parentheses.
        - The results of the no show patient contact are also included.
        - Results added for resolution: Reminder term and health factor information.
    HIGH RISK MENTAL HEALTH NO SHOW ADHOC REPORT BY                       PAGE 1
    MH CLINICS for Appointments 5/14/12-5/23/12             Run: 5/23/2012@08:26
    *STATUS: NS = No Show      NA = No Show Auto Rebook     NAT = No Action Taken
    #   PATIENT              PT ID APPT D/T         CLINIC/STATUS/PROVIDER
    ******************************************************************************
    DIVISION/CLINIC/STOP: ISC-SLC-A4/Mental Health/188
    1   CRPATIENT,TWO        C4444 5/14/2012@08:00  Mental Health
    *NS   WHPROVIDER,THIRTEEN
    Home: (801)556-6666
    Cell: (801)222-6666
    Next of Kin:
    NOK: PRIMARY NOK CRPATIENT,TWO
    Relation: FRIEND
    Phone: (801)556-6666                  Phone: (801)556-6666
    Work Phone: (801)565-6565
    Emergency Contact:
    E-Cont.: PRIMARY NOK CRPATIENT,TWO
    Relation: FRIEND
    203 Main st
    SALT LAKE CITY, UT  84107
    Phone: (801)556-6666
    Work Phone: (801)565-6565
    MHTC:  MHCLINICIAN, ONE (HRMH TEST TEAM)
    Future Scheduled Appointments:  NO APPOINTMENTS SCHEDULED WITHIN 30 DAYS
    Results:
    Resolution: Last done 05/14/2012@12:00
    Reminder Term: VA-MH NOSHOW PT EMERGENT CARE
    Health Factor: MH NOSHOW PT EMERGENT CARE
    05/14/2012@12:00
    Reminder Term: VA-MH SUICIDE ATTEMPTED
    Health Factor: MH SUICIDE ATTEMPTED
    05/14/2012@12:00
    2   CRPATIENT,TWO        C4444 5/14/2012@12:00  Mental Health
    *NS   WHPROVIDER,THIRTEEN
    Home: (801)556-6666
    Cell: (801)222-6666
    Next of Kin:
    NOK: PRIMARY NOK CRPATIENT,TWO
    Relation: FRIEND
    Phone: (801)556-6666                  Phone: (801)556-6666
    Work Phone: (801)565-6565
    Emergency Contact:
    E-Cont.: PRIMARY NOK CRPATIENT,TWO
    Relation: FRIEND
    203 Main st
    SALT LAKE CITY, UT  84107
    Phone: (801)556-6666
    Work Phone: (801)565-6565
    MHTC:  MHCLINICIAN,ONE (HRMH TEST TEAM)
    Future Scheduled Appointments:  NO APPOINTMENTS SCHEDULED WITHIN 30 DAYS
    Results:
    Resolution: Last done 05/14/2012@12:00
    Reminder Term: VA-MH NOSHOW PT EMERGENT CARE
    Health Factor: MH NOSHOW PT EMERGENT CARE
    05/14/2012@12:00
    Reminder Term: VA-MH SUICIDE ATTEMPTED
    Health Factor: MH SUICIDE ATTEMPTED
    05/14/2012@12:00
    HIGH RISK MENTAL HEALTH NO SHOW ADHOC REPORT BY                       PAGE 2
    MH CLINICS for Appointments 5/14/12-5/23/12             Run: 5/23/2012@08:26
    Totals Page
    ******************************************************************************
    Division/Clinic Appointment Totals
    Division/CLinic                                                          Unique
    NS   NSA   NAT  Patients
    ISC-SLC-A4/Mental Health
    SD*5.3*588 contains a post-installation routine that will add two new parameters to the PARAMETERS (#8989.5) file, with associated parameter definitions added to the PARAMETER DEFINITION (#8989.51) file. The new parameter SDMH PROACTIVE DAYS stores a value that will list future appointments for the number of days stored in the parameter, for each patient on the report.
    This parameter is checked when the High Risk MH Proactive Nightly Report [SD MH PROACTIVE BGJ REPORT] is run. The second new parameter is SDMH NO SHOW DAYS which also stores a value that will list future appointments for the number of days stored in the parameter, for each patient on the High Risk MH No-Show Nightly Report [SD MH NO SHOW NIGHTLY BGJ].  The default value of 30 days will be populated by the post-init for both parameters. Sites may change the number of days stored in the parameter, by using the General Parameter Tools option, selecting the Edit Parameter Values option, and entering SDMH PROACTIVE DAYS or SDMH NO SHOW DAYS.

#### Health Summary (GMTS)

**GMTS*2.7*104** modifies two entries in the Health Summary Component file (142.1): MH HIGH RISK PRF HX and MH TREATMENT COORDINATOR.

These components are used in the VA-MH HIGH RISK PATIENT and REMOTE MH HIGH RISK PATIENT Health Summaries and are also available for use in the Health Summary Adhoc Report. Additionally, the VA-MH HIGH RISK PATIENT Health Summary is also embedded in the VA-MH HIGH RISK NO SHOW FOLLOW-UP Reminder Dialog released in Phase I of this project.

The MH HIGH RISK PRF HX component will now include the assignment history for the newly created Category I Patient Record Flag (HIGH RISK FOR SUICIDE).  The assignment history in Health Summary will display both Category II (local) and Category I (national) assignments for High Risk for Suicide until all local entries have been converted to the national flag.

The MH TREATMENT COORDINATOR component will now be fully functional and display the mental health treatment team, mental health treatment coordinator (MHTC), and the MHTC contact information.

Owner site and Originating site, along with PRF status, have been added.

**Sample output from the updated components:**

-------------------- MHRF - MH Suicide PRF Hx ------------

CATEGORY I (NATIONAL) PRF: HIGH RISK FOR SUICIDE

Date Assigned: Jan 18, 2012@08:49:28

Next Review Date: MAY 01, 2012

Owner Site: SALT LAKE CITY HCS

Originating Site: CHEYENNE VAMC

Assignment History:

Date: JAN 18, 2012@08:49:28

Action: NEW ASSIGNMENT

Approved By: MHCLINICIAN, TWO

Date: JAN 26, 2012@15:07:57

Action: CONTINUE

Approved By: MHCLINICIAN, TWENTY

Date: FEB 01, 2012@13:05:18

Action: CONTINUE

Approved By: MHCLINICIAN, TWENTY

Date: FEB 01, 2012@13:21:38

Action: ENTERED IN ERROR

Approved By: MHCLINICIAN, TWO

Date: FEB 01, 2012@13:41:05

Action: REACTIVATE

Approved By: MHCLINICIAN, TWENTY

Date: FEB 01, 2012@13:59:32

Action: CONTINUE

Approved By: MHCLINICIAN, TWO

CATEGORY II (LOCAL) PRF: HIGH RISK FOR SUICIDE

Date Assigned: Dec 08, 2011@09:28:23

Next Review Date:

Owner Site: SALT LAKE CITY HCS

Originating Site: CHEYENNE VAMC

Assignment History:

Date: DEC 08, 2011@09:28:23

Action: NEW ASSIGNMENT

Approved By: MHCLINICIAN, TWO

Date: JAN 12, 2012@15:46:32

Action: INACTIVATE

Approved By: MHCLINICIAN, TWENTY

CPRS GUI is able to display multiple Category I Patient Record Flags

Figure 1.0 – PRF Category I Flag Example

CPRS GUI Reports Tab, VA-MH HIGH RISK PATIENT Health Summary Display updated to include Cat I HIGH RISK FOR SUICIDE PRF, and MHTC info

Figure 2.0 – CPRS GUI Reports Tab, VA-MH HIGH RISK PATIENT Health Summary

Reminder Resolution for High Risk MH No-Show Follow-up reminder; additional information display now includes CAT I PRF and MHTC

Figure 3.0 – Reminder Resolution for High Risk MH No-Show Follow-up reminder

#### Text Integration Utility (TIU)

**TIU*1.0*265** installs a new TIU DOCUMENT DEFINITION (file #8925.1) title: PATIENT RECORD FLAG CATEGORY I – HIGH RISK FOR SUICIDE to be used with the new Patient Record Flag. The patch installation links the title to the existing document class PATIENT RECORD FLAG CAT I.

This patch also provides one fix to TUI*1*260 in routine ^TIULO1. A formatting error was discovered in the MH MISSED APPOINTMENTS 10D TIU object. This is the object that will display on the High Risk MH No-Show Follow-up reminder dialog whenever a patient has missed a mental health appointment within the last 10 days.

Remedy ticket **#781752** reported that Imported TIU-HS OBJECT won’t preview – problem of “NO OWNER.” Since a national coding solution can’t easily be made, instructions have been added to the TIU Technical Manual to describe how to resolve this at local sites.

#### Order Entry (OR)

**OR*3*348** adds a new provider recipient, Primary Care Management Module (PCMM) Mental Health Treatment Coordinator (MHTC), to the existing ORB PROVIDER RECIPIENTS parameter. It will be added as a 'C' code to the existing 'PATOMERS' values:

| **Code**   | **DESCRIPTION**                                                                                                                                                                     |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| P          | (Primary Provider): deliver notification to the patient's Primary Provider.                                                                                                         |
| A          | (Attending Physician): deliver notification to the patient's Attending Physician.                                                                                                   |
| T          | (Patient Care Team): deliver notification to the patient's OE/RR Teams (personal patient and team lists are evaluated for potential recipients) and to devices on an OE/RR team). . |
| O          | (Ordering Provider): deliver notification to the provider who placed the order which trigger the notification.                                                                      |
| M          | (PCMM Team): deliver notification to users/providers linked to the patient via PCMM Team Position assignments.                                                                      |
| E          | (Entering User): deliver notification to the user/provider that entered the order's most recent activity.                                                                           |
| R          | (PCMM Primary Care Practitioner): deliver notification to the patient's PCMM Primary Care Practitioner.                                                                             |
| S          | (PCMM Associate Provider): deliver notification to the patient's PCMM Associate Provider.                                                                                           |
| C          | (PCMM Mental Health Treatment Coordinator): deliver notification to the patient's PCMM Mental Health Treatment Coordinator.                                                         |

With this enhancement, MHTCs can now specify to be default provider recipients of certain pertinent notifications, such as for Admissions, Discharge, and Deceased Patient, to name a few. The ORB PROVIDER RECIPIENTS parameter definition in the PARAMETER DEFINITION file #8989.51 will also be updated accordingly to reflect these changes.

An MHTC is defined as a liaison between the patient and the mental health system at a VA site.  There is only one MHTC per patient and they are the key coordinator for behavioral health services care.

For more information about the MHTC's responsibilities, see VHA Handbook 1160.1, "Uniform Mental Health Services in VA Medical Centers for Clinics," pp 3-4.  Note: In the handbook, the MHTC is called the Principal Mental Health Provider.

A new notification is also being released with this patch: SUICIDE ATTEMPTED/ COMPLETED. This informational notification is triggered by Clinical Reminders when a MH SUICIDE ATTEMPTED or MH SUICIDE COMPLETED health factor has been documented in PCE. It is exported with package parameter values set as follows:

. ORB ARCHIVE PERIOD - 30

. ORB DELETE MECHANISM - Individual Recipient

. ORB FORWARD BACKUP REVIEWER - No

. ORB FORWARD SUPERVISOR - No

. ORB FORWARD SURROGATES - No

. ORB PROCESSING FLAG - Disabled

. ORB PROVIDER RECIPIENTS - MHTC and PCMM Team (CM)

. ORB URGENCY - High

**IMPORTANT NOTE: Notifications are processed by IEN (internal entry number) from the OE/RR NOTIFICATIONS File #100.9. Any site-defined notifications run the risk of being over-written by new notifications that are nationally released, especially those within the number range 1-9999, which is reserved for national release. If you have locally defined notifications, you may need to renumber them before this patch will install.  IEN #77 is being added. See Appendix B of the Patch 24 Installation Guide for instructions on how to recreate or re-point site-defined notifications occupying a national number-space.**

A validation routine is also added to the input transform of the NUMBER field (#.001) of the OE/RR Notifications File #100.9. This validation routine will prohibit new national notification entries by the site and validate the correct local notification number scheme &lt;your site's station number&gt;&lt;incremental notification number 01-99&gt;.

#### Clinical Reminder s (PXRM)

**PXRM*2*24** includes a new computed finding (VA- PCMM MHTC), a new reminder term (VA-MH HIGH RISK FOR SUICIDE PRF), updated and new reminder definitions, a modified dialog, and a new dialog that will display the MHTC.

- **Computed Findings**
    1. A new Computed Finding was added that detects whether a Mental Health Treatment Coordinator (MHTC) is defined for a patient.
REMINDER COMPUTED FINDING INQUIRY      Apr 16, 2012 2:36:22 pm Page 1
VA-PCMM MHTC                                                     No. 82
------------------------------------------------------------------------------
Print Name:             VA-PCMM Mental Health Treatment Coordinator
Class:                  NATIONAL
Sponsor:
Review Date:
Description:
This computed finding returns the patient's current Mental Health Treatment
Coordinator (MHTC). The Scheduling API this computed finding uses does not
take a date as a parameter so it only returns the MHTC as of the actual
calendar date. Therefore, this computed finding cannot be used to determine
if the patient had an MHTC sometime in the past.
The default value of the computed finding is the MHTC. The following
additional CSUBs are returned:
MHTC - Mental Health Treatment Coordinator ROLE - role TEAM - team TEAM
POSITION - team position
Entry Point: MHTC       Routine:    PXRMPCMM
    1. The description of CF.VA-PATIENT RECORD FLAG LIST was updated to include how to use the computed finding parameter to specify the flag type.
    - **Reminder Term**
A new term, The VA-MH HIGH RISK FOR SUICIDE PRF was added, to be used in the Reminder Definitions in the High Risk for Suicide Patient – Reminder &amp; Flag project. The following description was added to the VA-HIGH RISK FOR SUICIDE PRF Reminder Term:
This reminder looks for the national category I HIGH RISK FOR SUICIDE patient record flag and the local category II patient record flag used at your site.
This term is distributed to look for the local name HIGH RISK FOR SUICIDE, which is the first mapped finding in the Mapped Findings. The Computed Finding Parameter of HIGH RISK FOR SUICIDE^L means use the local patient record flag called HIGH RISK FOR SUICIDE.  If your site uses a different category II patient record flag name, then the computed finding parameter for the first mapped finding should be changed. For example, if your site uses SUICIDE RISK as the name of the category II patient record flag, then the computed finding parameter should be changed to SUICIDE RISK^L.
Do not change the second mapped finding with the Computed Finding Parameter of HIGH RISK FOR SUICIDE^N.
    - **Reminder Definition**
    1. New Reminder Definition: VA-MH HIGH RISK NO-SHOW ADHOC RPT
No reminder dialog is associated with this reminder. This new Reminder Definition looks for the first appointment found, given a date and time and looking through the rest of the day. It is resolved if the finding is documented within 1 week. It is used by the SD MH NO SHOW AD HOC REPORT to get Results related to the follow-up reminder for each missed appointment date/time, if results are available.
Example of Results section that prints after the Future Scheduled Appointments:
Future Scheduled Appointments: NO APPOINTMENTS SCHEDULED WITHIN 30 DAYS
Results:
Resolution: Last done 05/14/2012@12:00
Reminder Term: VA-MH NOSHOW PT EMERGENT CARE
Health Factor: MH NOSHOW PT EMERGENT CARE
05/14/2012@12:00
Reminder Term: VA-MH SUICIDE ATTEMPTED
Health Factor: MH SUICIDE ATTEMPTED
05/14/2012@12:00
    1. Added the term, Category I PRF for HIGH RISK FOR SUICIDE to the Reminder Definition.  The reminder now looks for both the Category I and Category II active PRF for High Risk for Suicide.
--STATUS-- --DUE DATE--  --LAST DONE--
High Risk MH No-Show Follow-up       DUE NOW     DUE NOW       unknown
Frequency: Due every 99Y - Once for all ages.
Reminder triggered by missed MH appointment and when resolved won't be due
again until another missed MH appointment occurs.
The patient has an active High Risk for Suicide Patient Record Flag and missed a MH appointment.
Cohort:
Reminder Term: VA-MH NOSHOW MISSED MH CLINIC APPTS
Computed Finding: VA-Appointments for a Patient
04/09/2012@12:00 value - Mental Health
CLINIC: Mental Health
APPOINTMENT STATUS: NO-SHOW
Reminder Term: VA-MH HIGH RISK FOR SUICIDE PRF
Computed Finding: VA-Patient Record Flag Information
01/31/2012@11:08:45 value - NEW ASSIGNMENT;
Flag - HIGH RISK FOR SUICIDE(I (NATIONAL)).
Assigned Jan 31, 2012@11:08:45 by MHPROVIDER, TWO. New record flag
assignment.
12/21/2010@15:36:02 value - NEW ASSIGNMENT;
Flag - HIGH RISK FOR SUICIDE(II (LOCAL)).
Assigned Dec 21, 2010@15:36:02 by MHPROVIDER, TWO. New record flag assignment.
    1. Changes to VA-MH HIGH RISK NO-SHOW FOLLOW-UP reminder definition:
        - Removed Occurrence Count of 5 from RT.VA-MH NOSHOW MISSED MH CLINIC APPTS Hospital Location, and only defined occurrence at the Reminder Definition level.
    It still looks back 10D and resolves with specific health factors entered from the reminder dialog the same day or a completed MH Appointment within 8 hours before or 72 hours after.
        - If the there are several No-show appointments for a given day, any of the no-show appointments (even the earliest appointment) on that day and the actions taken will resolve all of the no-show follow-ups for that day.
    No-show health factors entered at any time on the date of the missed appointment resolve all no-show appointment follow-up on that day.
    Figure 4.0 – No-show health factors entered at any time on the date of the missed appointment  resolve all no-show appointment follow-up on that day.
    Example Of Clinical Maintenance Output after selecting 8 AM Appointment
    --STATUS-- --DUE DATE--  --LAST DONE--
    High Risk MH No-Show Follow-up         DONE                   09/17/2012
    Frequency: Due every 99Y - Once for all ages.
    Reminder triggered by missed MH appointment and when resolved won't be due
    again until another missed MH appointment occurs.
    The patient has an active High Risk for Suicide Patient Record Flag and missed a MH appointment.
    Cohort:
    Reminder Term: VA-MH NOSHOW MISSED MH CLINIC APPTS
    Most recent appointment that triggered the reminder
    Computed Finding: VA-Appointments for a Patient
    09/17/2012@10:00 value - Mental Health
    APPOINTMENT DATE/TIME: 09/17/2012@10:00
    CLINIC: Mental Health
    APPOINTMENT STATUS: NO-SHOW
    09/17/2012@08:00 value - Mental Health
    APPOINTMENT DATE/TIME: 09/17/2012@08:00
    CLINIC: Mental Health
    APPOINTMENT STATUS: NO-SHOW
    Reminder Term: VA-MH HIGH RISK FOR SUICIDE PRF
    Computed Finding: VA-Patient Record Flag Information
    12/21/2010@15:33:08 value - NEW ASSIGNMENT;
    Flag - HIGH RISK FOR SUICIDE(II (LOCAL)).
    Assigned Dec 21, 2010@15:33:08 by MHPROVIDER, ONE. New record flag assignment.
    Resolution: Last done 09/17/2012@08:00
    Reminder Term: VA-MH NOSHOW PT CONTACTED
    Health Factor: MH NOSHOW PT CONTACTED
    09/17/2012@08:00
    Comments: Patient had flu
    The following fields were changed in the VA-MH HIGH RISK NO-SHOW FOLLOW-UP reminder:
        - Changed VA-MH NOSHOW MISSED MH CLINIC APPTS finding:
    Replaced the long description of clinic stops from the VA-MH NOSHOW MISSED MH CLINIC APPTS reminder term with a summary as follows:
    The list of DSS IDs (stop codes) used in the Reminder Location List finding for this term was provided by the Office of Mental Health Services and includes stop codes related to Mental Health that involve face-to-face contact with the patient.
        - Changed the VA-MH NOSHOW PT CONTACTED finding:
    BEGINNING DATE/TIME field changed to start the search with the missed appointment date/time minus 8 hours (-8H) so if multiple appointments were no-show on the same day, entering the Patient was contacted earlier than the appointment time will still resolve the reminder.
    Changed the Occurrence Count to -1, instead of 3, so the oldest entered Pt Contacted finding on the same day or following days will resolve the reminder, rather than using the most recent finding to resolve the reminder.
        - Changed the VA-MH NOSHOW PT EMERGENT CARE  finding:
    BEGINNING DATE/TIME field changed to start the search with the missed appointment date/time minus 8 hours (-8H) so if multiple appointments were no-show on the same day, entering the Patient went to emergent care earlier than the appointment time will still resolve the reminder.
    Also changed the Occurrence Count to -1, instead of 3, so the oldest entered Emergent Care finding on the same day or following days will resolve the reminder, rather than using the most recent finding to resolve the reminder.
        - Changed the VA-MH NOSHOW PT CALLED 3X UNSUCCESSFUL  finding:
    BEGINNING DATE/TIME field changed to start the search with the missed appointment date/time minus 8 hours (-8H) so if multiple appointments were no-show on the same day, entering the Patient was called three times earlier than the appointment time will show up as information.
    Added Occurrence Count of -1 to make sure the oldest 3x unsuccessful finding beginning with the beginning of the day of the missed appointment will display (not the most recent finding).
        - Changed the VA-MH NOSHOW PLAN DEVELOPED  finding:
    BEGINNING DATE/TIME field changed to start the search with the missed appointment date/time minus 8 hours (-8H) so if multiple appointments were no-show on the same day, entering a plan was developed earlier than the appointment time will still resolve the reminder.
    Changed  Occurrence Count to -1, instead of 3, so the oldest entered Plan Developed finding on the same day or following days will resolve the reminder, rather than using the most recent finding to resolve the reminder.
        - Changed the VA-MH NOSHOW OUTREACH LETTER  finding:
    BEGINNING DATE/TIME field changed to start the search with the missed appointment date/time minus 8 hours (-8H) so if multiple appointments were no-show on the same day, entering the Patient was sent an outreach letter earlier than the appointment time will show up as information.
    Added Occurrence Count of -1, so that the oldest entered Outreach Letter finding on the same day or following days will display, rather than using the most recent finding for information.
        - Changed the VA-MH NOSHOW OTHER OUTCOME  finding:
    BEGINNING DATE/TIME field changed to start the search with the missed appointment date/time minus 8 hours (-8H) so if multiple appointments were no-show on the same day, entering the other outcome earlier than the appointment time will be displayed as information.
    Added  Occurrence Count of -1, so the oldest entered Other Outcome finding on the same day or following days will resolve the reminder, rather than using the most recent finding to resolve the reminder.
        - Changed the VA-MH SUICIDE ATTEMPTED  finding:
    BEGINNING DATE/TIME field changed to start the search with the missed appointment date/time minus 8 hours (-8H), so if multiple appointments were no-show on the same day, entering the other outcome earlier than the appointment time will still resolve the reminder.
    Added Occurrence Count of -1, so the oldest entered Suicide Attempted finding on the same day or following days will resolve the reminder, rather than using the most recent finding to resolve the reminder.
        - Changed the VA-MH SUICIDE COMPLETED  finding:
    BEGINNING DATE/TIME field changed to be null so any Suicide Completed will resolve the reminder.
        - Changed the VA-MH APPT KEPT  finding:
    Changed Occurrence Count from 4 to -4, so the oldest kept appointment finding on the same day or following days will resolve the reminder, rather than using the most recent finding to resolve the reminder.
    Removed YES from the Use Status/Cond in Search field.
    Changed the Condition to include parentheses, to better document the logic. Changed !+V("CHECK-OUT DATE/TIME")&gt;0 to !(+V("CHECK-OUT DATE/TIME")&gt;0)
        - Removed three terms (VA-MH NOSHOW SUPPORT CONTACT, VA-MH NOSHOW INITIATE WELLNESS CHECK, VA-MH NOSHOW UNABLE TO REACH PT) from the reminder definition, since they are no longer valid responses in the related reminder dialog.
            1. New reminder definition: VA-MHTC NEEDS ASSIGNMENT.
                - This reminder looks for three completed appointments to MH clinics over the past year and checks to see if an MHTC is currently assigned to the patient. If no MHTC is assigned, the reminder will be due.
                - The reminder definition uses the new VA-PCMM MHTC computed finding.
                - There is no reminder dialog related to this reminder.
                - This reminder can be used from CPRS to show as due on the CPRS GUI Cover Sheet.
                - This reminder can also be used from Reminder Reporting options/Reminders Due Report. Reminder CACs can create a Reminders Due Report (User) template for an SPC user to get the list of patients who are scheduled for a MH appointment next week and are candidates for MHTC.
                - Uses Reminder Term VA-MH APPTS FOR MHTC ASSIGNMENT, which uses a new Reminder Location List called VA-MHTC APPT STOP CODES LL in the Computed Finding VA-Appointments for a Patient. **The new Reminder Location List is consistent with the national list of MH Encounter Stop Codes defined for sites by the Office of Mental Health Services.**
                - **Reminder Dialog**
            VA-HIGH RISK MH NO-SHOW FOLLOW-UP:  The dialog info text presented to the user was changed to clarify that the reminder is resolved if a completed encounter is found for  a MH appointment on the same day, or within 72 hours of the missed MH appointment.
            Figure 5.0 – Example Of VA-HIGH RISK MH NO-SHOW FOLLOW-UP Dialog, with changed information text
            The Mental Health Suicide Behavior Report (SBR) Instrument is available for use in the High Risk MH No-Show Follow-Up Clinical Reminder Dialog.
            To minimize confusion, the no lock statement in LOCK^PXRMDEDT was changed from:
            E  W !!,?5,"Another user is editing this file, try later" H 2 Q 0
            to
            E  W !!,?5,"Another user is editing this entry, try later." H 2 Q 0
            **Reminder Notifications**
                - New functionality was added that gives Clinical Reminders the ability to send notifications.  The specific notification is SUICIDE ATTEMPTED /COMPLETED that is described above in the OR*3.0*348 section.
            **Reminder Test**
                - A new feature was added to reminder test that shows step-by-step how function strings are evaluated. Also the display of the reminder test was moved to the FileMan Browser to make it easier to view.


### Remedy Ticket and Other Fixes

**COMPUTED FINDINGS:**

Remedy ticket # **758312** reported that CF.VA-EMPLOYEE was being incorrectly set as false whenever Beginning Date/Time was non-null. This problem was corrected and the description was updated.

**REMINDER EVALUATION:**

Remedy tickets # **588393** and # **606623** reported that comments recorded for a health factor (V Health Factor) disappear when INCLUDE VISIT DATA is set to yes. This is because the Visit file also has “COMMENTS” as CSUB data so that visit comments overwrite health factor comments. The solution was to change the CSUB for visit comments from “COMMENTS” to “VISIT COMMENTS”.

**REMINDER EXCHANGE:**

Remedy ticket # **592128** .  In some cases the Reminder Exchange silent installer was incorrectly linking reminder definitions and dialogs; this is corrected.

Remedy tickets # **573543** and # **593623.** There was a problem in Reminder Exchange causing an undefined error when installing a dialog using Install Selected instead of Install All. This was fixed.

Remedy ticket # **707134** . For components that are not installable, Reminder Exchange would create a non-installable placeholder in the Exchange file by only packing the .01. Because Exams typically only have a .01, they were being made non-installable when they should be installable. Additional checks to determine if a component is installable were added so Exams are now installable.

Remedy ticket # **779803** reported the following error when editing a dialog:

MSG("DIERR")=1^1

MSG("DIERR",1)=701

MSG("DIERR",1,"PARAM",0)=3

MSG("DIERR",1,"PARAM",3)= CRPROVIDER,TWO

MSG("DIERR",1,"PARAM","FIELD")=1

MSG("DIERR",1,"PARAM","FILE")=801.44

MSG("DIERR",1,"TEXT",1)=The value 'XXX,YYYY Z' for field EDIT BY in EDIT HISTO

RY SUB-FIELD in file REMINDER DIALOG is not valid.

MSG("DIERR","E",701,1)=

Select DIALOG to add:

This occurred because there were two entries in file #200 with the same .01 field, so FileMan could not resolve them. The code was changed to use the DUZ instead of the external value.

**REMINDER PATIENT LISTS:**

Remedy ticket # **610957** . A store error when trying to copy a large patient list to an OE/RR Team list was reported. The store error was occurring in a FileMan API that was being used to create the OE/RR Team list entry. The solution was to directly copy the patients instead of using the FileMan API.

**REMINDER TEST:**

Remedy ticket # **710964** . When a reminder definition uses CF.VA-REMINDER DEFINTION, it is possible for the display of the term findings to be corrupted if the reminder evaluated by the computed finding also includes terms as findings. This was fixed.

Remedy ticket # **242214** reported a reminder test taking an error when neither a patient nor reminder was selected. It no longer takes an error.

**REMINDER DIALOGS:**

Remedy ticket # **737901** pointed out that the no lock statement in LOCK^PXRMDEDT is confusing: E  W !!,?5," Another user is editing this file, try later" H 2 Q 0

Because the lock is on the entry, and not on the whole file, the suggestion was to change it to E  W !!,?5,"Another user is editing this entry, try later." H 2 Q 0

This change has been made.

Remedy ticket # **742674** and **761094** showed the undefined error

&lt;UNDEFINED&gt;MRD+2^PXRMFF0 *FIEVAL("1") when trying to evaluate a function finding using the MRD function for a taxonomy finding. This was occurring because during the evaluation, a lock could not be obtained for the taxonomy expansion and the finding was not being set to false as it should have been. This was corrected.

Remedy ticket # **391498** reported the following undefined error when a Reminders Due Report that was queued and then cancelled at the start time prompt: &lt;UNDEFINED&gt;QUE+8^PXRMXQUE *ZTSK

The undefined error was corrected.

Remedy ticket # **606273** reported that in Reminder Exchange, if a definition selected for packing was linked to a dialog and that definition used CF.VA-REMINDER DEFINITION, either directly or through a term, the dialog was not being packed. This was because the variable RIEN was not newed in CHKCF^PXRMEXPS and that same variable name is used in SDEF^PXRMEXPS so the original RIEN was being replaced with the RIEN for the computed finding.

**TIU-HEALTH SUMMARY OBJECTS:**

**Remedy ticket # 781752** - Imported TIU-HS objects won't PREVIEW -'NO OWNER'

TIU Health Summary objects created in one account (i.e. mirror), when exported and imported using Reminder Exchange over to another account at same site (i.e. production) fail to preview in the GUI template editor with a “NO OWNER” error message. The system does not recognize that “Clinical Coordinator” is the CLASS OWNER.

Resolution:

Reminder Exchange does not assign an owner in the TIU DOCUMENT DEFINITION file (#8925.1). The CLASS OWNER field (#.06) points to the USR CLASS file (#8930) and the PERSONAL OWNER field (#.05) points to the NEW PERSON file (#200). These two files may not be named or numbered the same way at all sites receiving the exported document definition. Therefore, the owner assignment cannot be exported reliably and must be reassigned upon import. The TIU documentation has been updated to explain this issue.

### Other Fixes

**REMINDER COMPUTED FINDINGS:**

- The following national computed findings had the field CF PARAMETER REQUIRED incorrectly marked as YES. The parameter was corrected.

VA-ADMISSIONS FOR A DATE RANGE

VA-APPOINTMENTS FOR A PATIENT

VA-ASU USER CLASS

VA-PATIENTS WITH APPOINTMENTS

- VA-APPOINTMENTS FOR a PATIENT was not setting the CSUB "APPOINTMENT DAT/TIME"; this has been fixed.
- The description of CF.VA-PATIENT RECORD FLAG LIST was updated to include how to use the computed finding parameter to specify the flag type:
    - This list type computed finding returns a list of all patients who have a specified record flag active any time in the date range.
    - The Computed Finding Parameter is used to specify the flag in the following format: FLAG NAME^FLAG TYPE, where FLAG NAME is the exact name of the flag and FLAG TYPE is L for local or N for national. FLAG TYPE is optional and defaults to L.

**REMINDER DEFINITIONS:**

- For list-type reminders, the definition integrity checker was not correctly checking the Baseline Age Findings to make sure that an age range was defined. This was corrected.

**REMINDER EXCHANGE:**

- If a dialog is being installed and the disable field was set to No, then the dialog was installed with a Disable Status of Disable and Send Message. For National Dialog the disable status should be set to No. This problem has been fixed.
- ROUTINE PXRMEXIC
- In patch PXRM*2*27, a problem occurred with a dialog not being installed properly, which led to a discussion of what the install actions should be for dialogs. As a result the update action was removed.

**REMINDER NOTIFICATION:**

- A test site reported the following undefined error:

$ZE= &lt;UNDEFINED&gt;SUICIDE+9^PXRMNTFY ^XTMP("PXRM PXK EVENT95523120725.100727",25284717,"HF",11313037,0,"AFTER")

The code was changed so that it won’t cause an error if the “AFTER” node does not exist.

**FUNCTION FINDINGS:**

- Function findings were changed in PXRM*2*18 to allow the MUMPS division operators in the function string, which meant there is the possibility of division by 0. The function finding evaluation code was changed to trap a division by 0 so it would not generate an error and the function finding was set to false if there was a division by 0.
- During testing of PXRM*2*24 it was determined that this behavior was not optimal; instead only the portion of the function string involving the division by 0 should be set to false. The function finding evaluator was changed to do this and a new feature was added to reminder test that shows step-by-step how the function string is evaluated.
- Also the display of the reminder test was moved to the FileMan Browser to make it easier to view.

## Acronyms

The OIT Master Glossary is available at [http://vaww.oed.wss.va.gov/process/ Library/master\_glossary/masterglossary.htm](http://vaww.oed.wss.va.gov/process/%20Library/master_glossary/masterglossary.htm)

| ## TERM    | DEFINITION                                                           |
|------------|----------------------------------------------------------------------|
| ASU        | Authorization/Subscription Utility                                   |
| Clin4      | National Customer Support team that supports Clinical Reminders      |
| CPRS       | Computerized Patient Record System                                   |
| DBA        | Database Administration                                              |
| DG         | Registration and Enrollment Package namespace                        |
| ESM        | Enterprise Systems Management (ESM)                                  |
| FIM        | Functional Independence Measure                                      |
| GUI        | Graphic User Interface                                               |
| HRMH/HRMHP | High Risk Mental Health Patient                                      |
| IAB        | Initial Assessment & Briefing                                        |
| ICD10      | International Classification of Diseases, 10th Edition               |
| ICR        | Internal Control Number                                              |
| IOC        | Initial Operating Capabilities                                       |
| IVMH       | Improve Veteran Mental Health, one of the Secretary’s 21 initiatives |
| LSSD       | Last Service Separation Date                                         |
| MHTC       | Mental Health Treatment Coordinator                                  |
| OHI        | Office of Health Information                                         |
| OI         | Office of Information                                                |
| OIF/OEF    | Operation Iraqi Freedom/Operation Enduring Freedom                   |
| OIT/OI&T   | Office of Information Technology                                     |
| OMHS       | Office of Mental Health Services                                     |
| ORT        | Operational Readiness Testing                                        |
| PCS        | Patient Care Services                                                |
| PD         | Product Development                                                  |
| PIMS       | Patient Information Management System                                |
| PMAS       | Program Management Accountability System                             |
| PRF        | Patient Record Flag                                                  |
| PTM        | Patch Tracker Message                                                |
| PXRM       | Clinical Reminder Package namespace                                  |
| RSD        | Requirements Specification Document                                  |
| SD         | Scheduling Package Namespace                                         |
| SQA        | Software Quality Assurance                                           |
| USR        | ASU package namespace                                                |
| VA         | Department of Veteran Affairs                                        |
| VHA        | Veterans Health Administration                                       |
| VISN       | Veterans Integrated Service Network                                  |
| VistA      | Veterans Health Information System and Technology Architecture       |