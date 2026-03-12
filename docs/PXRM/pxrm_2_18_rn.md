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
source_file: pxrm_2_18_rn.docx
status: draft
title: PATIENT             PT ID     APPT D/T             CLINIC          STATUS
---

**PXRM*2*18**

## High Risk Mental Health Patient -

## Reminder and Flag

## Release Notes

**February 2012**

Product Development


Contents

Introduction	1

Related Documentation	2

Web Sites	2

Release Notes	3

Project Overview	3

Project Features	4

Scheduling	4

Registration – Patient Record Flag	6

Health Summary	6

Text Integration Utility (TIU)	7

Clinical Reminder Patch 18 (PXRM*2*18)	7

New Options and Reports	7

New report	8

New Computed Findings	8

Updates to National Reminders in Patch 18	8

Clinical Reminders Maintenance Enhancements and Fixes	10

Remedy Tickets 	10

General Fixes and Enhancements:	13

Reminder Computed Findings	13

Reminder Definitions	16

Reminder Dialogs	20

Reminder Exchange	21

Reminder Location Lists	21

Reminder Patient Lists	21

Reminder Reports	22

Reminder Terms	22

Reminder Test	22

Reminder Category	22

National Reminder Exchange Entries Distributed with this patch	23

Acronyms	24

## Introduction

The purpose of this project is to release 1) two new Scheduling reports that identify no-show “high risk for suicide” patients that missed their MH appointments, 2) a new national reminder and reminder dialog that will be used by providers to document results of following up with a high risk for suicide patient that missed a MH appointment, and 3) provide a health summary type with MH-specific supporting information. This functionality is in Increment 1 and 2 of the High Risk MH Patient – Reminder and Flag project.

The first release of the High Risk Mental Health Patient- Reminder and Flag (HRMHP) project includes five patches, which will be installed as a combined build. This Installation Guide describes installing and setting up Increments 1 and 2. Increments 3 and 4 will be released in a future build.

SD*5.3*578

This Scheduling patch provides two new MH NO SHOW Scheduling Reports for use by Suicide Prevention Coordinators and other Mental Health professionals.  The reports will support following up with High Risk for Suicide patients that missed a scheduled MH appointment.

DG*5.3*836

This Registration – Patient Record Flag patch provides new interfaces used by the Scheduling and Reminder patches to determine the High Risk for Suicide flag status on a specified date.

PXRM*2*18

This patch will create a national reminder to notify clinicians of a patient's risk of suicide and will create a dialog the clinicians can use to document follow-up with the high risk patients when they miss MH appointments. This Clinical Reminder patch supports the Scheduling patch by providing a national Reminder Location List of Mental Health stop codes used for scheduled appointments.  Additionally, this patch includes miscellaneous clinical reminder maintenance changes. Details of all the Clinical Reminder changes can be found in the Release Notes.

GMTS*2.7*99

This patch installs four Health Summary Components (MAS CONTACTS, MAS MH CLINIC VISITS, MH HIGH RISK PRF HX, and MH TREATMENT COORDINATOR),  two Health Summary Types (VA-MH HIGH RISK PATIENT  and REMOTE HIGH RISK MH PATIENT),, and a single Health Summary Object(VA-MH HIGH RISK PATIENT (TIU)).

TIU*1*260

The Text Integration Utility patch contains a single Health Summary Object and a single new TIU Health Summary object based on the new VA-MH HIGH RISK PATIENT Health Summary Type from GMTS*2.7*99. The TIU/HS object will be used in the VA-MH HIGH RISK NO  SHOW FOLLOW-UP Reminder Dialog distributed in PXRM*2*18.

### Related Documentation

| **Documentation**                                            | **Documentation File name**   |
|--------------------------------------------------------------|-------------------------------|
| High Risk Mental Health Patient Installation and Setup Guide | PXRM_2_18_IG.PDF              |
| Clinical Reminders User Manual                               | PXRM_2_18_UM.PDF              |
| Clinical Reminders Manager’s Manual                          | PXRM_2_MM.PDF                 |
| Clinical Reminders Technical Manual                          | PXRM_2_18_TM.PDF              |
| Scheduling Install Guide                                     | SD_5_3_578_IG.PDF             |
| Registration Install Guide                                   | DG_5_3_836_IG.PDF             |
| Health Summary User Manual                                   | HSUM_2_7_99_UM.PDF            |
| Health Summary Technical  Manual                             | HSUM_2_7_99_TM.PDF            |
|                                                              |                               |

#### Web Sites

| **Site**                              | **URL**                                                                                                            | **Description**                                                                            |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| National Clinical Reminders site      | http://vista.med.va.gov/reminders                                                                                  | Contains manuals, PowerPoint presentations, and other information about Clinical Reminders |
| National Clinical Reminders Committee | [http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx](http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx) | This committee directs the development of new and revised national reminders               |
| Document Library                      | [http://www.va.gov/vdl/](http://www.va.gov/vdl/)                                                                   | Contains manuals for Clinical Reminders and related applications.                          |

## Release Notes


### Project Overview

This project addresses the New Service Request (NSR) &lt;&lt; NSR20070589 High Risk Mental Health Patient – National Reminder and Flag &gt;&gt;. The NSR was submitted by Kathleen Lysell, PCS, Mental Health Services and Jan Kemp, Associate Director for Education MIRECC.  This project is included in the Improve Veteran Mental Health (IVMH) initiative.

This request was submitted in support of recommendations from the Comprehensive VHA Mental Health Strategic Plan and VHA Handbook 1160.01, Uniform Mental Health Services in VA Medical Centers and Clinics, to improve continuity of care for Veterans receiving mental health services.

Major objectives of this request include:

1. Identify those veterans who are at risk for suicide (Sites define this locally in the Patient Record Flag.)
2. Proactively seek to provide appropriate care to high risk, mental health patients who miss appointments
3. Evaluate patients for mental health disorders so that appropriate referrals can be made; identify those veterans with a history of suicide attempt or suicidal ideation who miss an appointment; notify the mental health professional of the missed appointment; and track efforts to reach this veteran.  If after three attempts, the veteran is not reached, a staff member may need to call other patient contacts or request a welfare check.


### Project Features

#### Scheduling

SD*5.3*578 provides two new MH NO SHOW Scheduling Reports for use by Suicide Prevention Coordinators and other Mental Health professionals. The reports will support following up with High Risk for Suicide patients who missed a scheduled MH appointment.

- A new nightly “NO-SHOW” MH High Risk report triggered by the nightly SD Background job.
- An ad-hoc “NO-SHOW” MH High Risk report menu option.

**Example: No-Show Nightly Report background job, as displayed to the screen when reading Mailman.**

Subj: HRMH NO SHOW NIGHTLY REPORT MESSAGE#  [#111884] 04/06/11@11:56  73 lines

From: POSTMASTER  In 'IN' basket.   Page 1

-------------------------------------------------------------------------------

Division/Clinic Appointment Totals

Division/CLinic                                                         Unique

NS    NSA    NAT  Patients

ALBANY/D-PSYCH                                        1      1      1      3

TROY1/LIZ'S MENTAL HEALTH CLINIC                      1      2      1      3

TROY1/MENTAL HEALTH                                   1      0      2      3

*STATUS: NS = No Show      NSA = No Show Auto Rebook     NAT = No Action Taken

HIGH RISK MENTAL HEALTH NO SHOW NIGHTLY REPORT                     PAGE    1

By CLINIC for Appointments on 4/5/11                      Run: 4/6/2011@11:56

#    PATIENT             PT ID     APPT D/T             CLINIC          STATUS

******************************************************************************

DIVISION/CLINIC/STOP CODE: ALBANY/D-PSYCH/188

1    HRMHpatient,One      0001     4/5/2011 11:00 am    D-PSYCH         *NS

Future Scheduled Appointments:

4/7/2011 9:00 am          LIZ'S MENTAL HEALTH CLINIC

4/14/2011 9:00 am         LIZ'S MENTAL HEALTH CLINIC

4/17/2011 9:00 am         LIZ'S MENTAL HEALTH CLINIC

2    HRMHpatient,Two      0002     4/5/2011 2:00 pm     D-PSYCH         *NAT

Future Scheduled Appointments:

4/14/2011 9:00 am         LIZ'S MENTAL HEALTH CLINIC

4/17/2011 9:00 am         LIZ'S MENTAL HEALTH CLINIC

3    HRMHpatient,Three    0003     4/5/2011 9:00 am     D-PSYCH         *NSA

Future Scheduled Appointments:

4/14/2011 9:30 am         LIZ'S MENTAL HEALTH CLINIC

4/18/2011 8:00 am         D-PSYCH

**Example: Ad-hoc “NO-SHOW” MH High Risk report.**

Select OPTION NAME:    High Risk MH No-Show Adhoc Report

***************  High Risk Mental Health NO SHOW Adhoc Report ***************

Select Beginning Date: 11/10/11// T-15  (OCT 21, 2011)

Select    Ending Date: 11/10/11// T  (NOV 10, 2011)

Select division: ALL//

Sort report by (M)ental Health Clinic Quick List,(C)linic or (S)top Code: M//S

Stop Code Selection:

A  All Stop Codes

M  Mental Health Stop Codes only

Select: (A)ll Stop Codes  A//?

Enter:  'A' for All Stop Codes

'M' for Mental Health Stop Codes only

Select: (A)ll Stop Codes  A// M

Select Number of days to List Future Appointments: 30//

This output requires 80 column output

Select Device: 0;80;9999  UCX/TELNET

...HMMM, THIS MAY TAKE A FEW MOMENTS...

HIGH RISK MENTAL HEALTH NO SHOW ADHOC REPORT BY                       PAGE 1

STOP CODES for Appointments 10/26/11-11/10/11           Run: 11/10/2011@10:16

PATIENT                PT ID     APPT D/T            CLINIC              STATUS

******************************************************************************

DIVISION/STOP/CLINIC: ALBANY/188/D-PSYCH

1  HRMHpatient,One	 0001      10/31/2011 9:00 am  D-PSYCH             *NAT

Home: (518)518-5181

Cell: (555)888-9999

Emergency Contact:

E-Cont.: HRMHecontact,One

MHTC:

Future Scheduled Appointments:

11/14/2011 8:00 am        DERMATOLOGY

11/14/2011 8:30 am        PSYCH CLINIC

11/21/2011 8:00 am        DERMATOLOGY

11/21/2011 9:00 am        D-PSYCH

Results:

**Output format for the VA-APPOINTMENTS FOR A PATIENT computed finding:**

If no fields are requested via the Computed finding parameter, the only information returned is the appointment date/time and the location.  If this is the case, the display will look like this:

Computed Finding: VA-Appointments for a Patient

10/21/2005@08:00 value - DIABETIC EDUCATION-INDIV-MOD B

If additional fields are requested, then the display will look like this:

Computed Finding: VA-Appointments for a Patient

10/21/2005@08:00 value - DIABETIC EDUCATION-INDIV-MOD B

APPOINTMENT STATUS: SCHEDULED/KEPT

PATIENT: CRPATIENT, TWO

LENGTH OF APPOINTMENT: 30

COMMENTS: inject

OVERBOOK: N

ELIGIBILITY OF VISIT: SC LESS THAN 50%

APPOINTMENT TYPE: REGULAR

#### Registration – Patient Record Flag

DG*5.3*836  includes:

- An application interface (API) that will return the multiple assignment statuses, if applicable, for a specified Flag Name during a specified patient and date range. The Assignment History should be returned for assignment statuses that overlap the specified date range.
- An API that will return the list of patients with the specific Patient Record Flag active within a specified date range.

#### Health Summary

- GMTS*2.7*99 includes components that can be used as to display patient phone numbers and other contact information, the next scheduled appointment to any MH clinic, and the MH High Risk for Suicide local Patient Record Flag and assignment status information.
- The GMTS*2.7*99 post-install routine creates stub entries in file #142 for the remote Health Summary Type, and then calls the silent Reminder Exchange install utility to install the remaining Health Summary items.

**HEALTH SUMMARY Components**

MAS CONTACTS

MAS MH CLINIC VISITS FUTURE

MH HIGH RISK PRF HX

MH TREATMENT COORDINATOR

**HEALTH SUMMARY Types**

VA-MH HIGH RISK PATIENT

REMOTE HIGH RISK MH PATIENT

**HEALTH SUMMARY OBJECT**

VA-MH HIGH RISK PATIENT (TIU)


#### Text Integration Utility (TIU)

TIU*1*260 includes:

- TIU Health Summary object that displays patient phone numbers and other contact information, and
- Health Summary object or TIU object that displays the next scheduled appointment to any MH clinic (based on a predefined Reminder Location List).
- TIU Health Summary object that displays the MH High Risk for Suicide local Patient Record Flag and assignment status information.

### Clinical Reminder Patch 18 (PXRM*2*18)

This patch creates a national reminder to notify clinicians of a patient's risk of suicide and a dialog the clinicians can use to document follow-up with the high risk patients when they miss MH appointments. This Clinical Reminder patch supports the Scheduling patch by providing a national Reminder Location List of Mental Health stop codes used for scheduled appointments.  Additionally, this patch includes miscellaneous clinical reminder maintenance changes.

- A new VA-MH HIGH RISK NO-SHOW FOLLOW-UP Reminder Definition
- A new VA-MH HIGH RISK NO-SHOW Follow-up Reminder Dialog

The following new features or changes are included in the PXRM*2.0*18 build.

#### New Options and Reports

Two new options were added to the reminder definition management menu:

- Integrity Check Selected
- Integrity Check All.

These can be used to check the integrity of selected or all reminder definitions, including function findings. The integrity check will also be made automatically whenever a reminder definition has been edited. Fatal errors (F) that will prevent the reminder from working properly and warnings (W) will be given. The following checks are made:

W – The Usage field contains a “P” and it is not a national reminder

F – Each finding is checked to make sure it exists

F – If either the Beginning Date/Time or Ending Date/Time contains FIEVAL(M,”DATE”) or FIEVAL(M,N,”DATE”), the definition is checked to make sure it contains finding M and if an occurrence is used the Occurrence Count of finding M is checked to make sure it is greater than or equal to N.

F- Function findings functions of the form FUNCTION(M) and FUNCTION(M,N) are checked to make sure finding M is in the definition and the Occurrence Count of finding M is greater than or equal to N.

F – If a Custom Date Due is defined, it is checked to make sure that the findings used in the Custom Date Due all exist in the definition.

F – Patient Cohort Logic and Resolution Logic are checked to make sure that the findings used in the logic all exist in the definition.

F – Logic strings are checked to make sure their syntax is valid.

F – The definition contains Resolution Logic, but does not have a baseline frequency or any findings that will set a frequency.

W – The definition contains Resolution Logic, but does not have a baseline frequency. It does have findings that will set a frequency. This could be a problem if all findings that set frequency are false.

#### New report

PXRM DIALOG CHECKER ALL was added to the Dialog Reports Menu. It checks all active reminder dialogs for invalid items.

#### New Computed Findings

*(See below under Maintenance Enhancements and Fixes for further descriptions of these new CFs.)*

VA-PATIENT RECORD FLAG INFORMATION

VA-PATIENT RECORD FLAG LIST.

Note these computed findings require patch DG*5.3*836.

VA-FILEMAN DATE - uses the Computed Finding Parameter to take any date format used in Clinical Reminders and it sets the date of the finding to that date. The purpose is to use it in a function finding to make date comparisons. For example, did a finding occur within 60 days of today?

VA-RANDOM NUMBER - generates random numbers for partitioning patients in a research study.

New computed findings to support the needs of PACT (Patient Aligned Care Teams):

1   VA-PCMM PATIENTS ASSIGNED TO A PRACTICTIONER

2   VA-PCMM PATIENTS ASSIGNED TO A TEAM

3   VA-PCMM PC TEAM AND INSTITUTION

4   VA-PCMM PRACTICTIONERS ASSIGNED TO A PATIENT

The first two are list type and the second two are multiple type.

#### Updates to National Reminders in Patch 18

1. **Updated branching logic reminders**

VA-BL DEPRESSION SCREEN

Removed RT.VA-ACTIVE DUTY

Cohort: changed to due for all

Resolution: changed to resolve for any entry that is not before the LSSD

Changed the logic from

MRD(VA-DEPRESSION SCREEN NEGATIVE,VA-DEPRESSION SCREEN POSITIVE)&gt;MRD(VA-LAST SERVICE SEPARATION DATE)

To

MRD(VA-DEPRESSION SCREEN POSITIVE,VA-DEPRESSION SCREEN NEGATIVE)'&lt;MRD(VA-LAST SERVICE SEPARATION DATE)

VA-BL ALCOHOL SCREEN

Removed RT.VA-ACTIVE DUTY

Cohort: changed to due for all

Removed exclusions

Resolution: changed to resolve for any entry that is not before the Last Service Separation Date (LSSD)

VA-BL PTSD SCREEN

Removed RT.VA-ACTIVE DUTY

Cohort: changed to due for all

Removed exclusions

Resolution: changed to resolve for any entry that is not before the LSSD

Added a '0' to the Within Category Rank for the health factors.

VA-BL OEF/OIF EMBEDDED FRAGMENTS

VA-BL OEF/OIF FEVER

VA-BL OEF/OIF GI SX

VA-BL OEF/OIF SKIN SX

Removed RT.VA-IRAQ/AFGHAN PERIOD OF SERVICE and substitute CF.VA-LAST SERVICE SEPARATION DATE

Removed RT.VA-ACTIVE DUTY

Cohort: changed to due for all

Resolution: changed to resolve for any entry that is not before the LSSD

**2.	Updated URLs**

VA-ALCOHOL USE SCREEN (AUDIT-C)

VA-DEPRESSION SCREENING

VA-PTSD SCREENING

1. **VA-EMBEDDED FRAGMENTS RISK EVALUATION:** Added '0' to the Within Category Rank for EF-NO BLAST/EXPLOSION INJURY and EF-NO BULLET INJURY

1. **VA-ALCOHOL USE SCREENING (AUDIT-C)**
    1. Added occurrence count of 4 to AUD C in the alcohol screening reminder
    2. Updated the dialog by changing 'Optional open and optional complete (partial complete possible)' to 'Optional open and required complete or cancel before finish'.

1. **Fixed grammatical error in VA-TEXT INFO SCREEN FOR AAA**

1. **Distributing reminders VA-INFLUENZA H1N1 IMMUNIZATION, VA-INFLUENZA** H1N1 IMMUNIZATION HIGH RISK, and dialog VA-INFLUENZA H1N1 IMMUNIZATION (DIALOG).  Distribute as INACTIVE.

1. **Updated VA-ALCOHOL F/U POS AUDIT-C dialog** to display the education and advice interventions without a box around both and also to have the results of an AUDIT-10 go into the progress note.  Added an * to the word 'required' in 2 of the captions.

1. **Distributing the updates to the VA-MHV INFLUENZA VACCINE reminder** which update the age range and also the date of the reminder term for vaccination for the '10-'11 flu season.

1. **Added VA-TB/POSITIVE PPD** . This updates the taxonomy VA-TB/POSITIVE PPD by adding the ICD diagnosis code 795.51.

#### Clinical Reminders Maintenance Enhancements and Fixes

#### Remedy Tickets that have been fixed in PXRM*2*18

**173532 and 462943**

Problems printing demographic information from the patient list

Two issues:

1. Race and ethnicity will print normally when not delimited
2. When using demographics in patient lists, the number of clinic appointments to show is not honored if you DO NOT delimit the report.  For instance, if you choose the default of 1// for number of clinic appointments to show (when you are prompted for this), you will receive more than 1 appointment if the patient has more than 1 appointment.

**366957**

Divide by 0 errors in PXRMBMI routine

**376141**

Reminder Dialog incorrectly displays DISABLED.

In the reminder dialog ListManager option REMINDER VIEW (ALL REMINDERS BY NAME) a reminder dialog will be incorrectly listed as DISABLED if Field #3 (DISABLED) has a value of zero (NO).  If the same field is left NULL it will be displayed correctly.

**390685**

PXRM\_1\_5\_12\_TM.PDF is displaying incorrect information for the registration index within PXRMINDX.  Nodes are displaying in the incorrect order.

**391160 and 488811**

Health factors being installed via the Reminder Exchange Utility do not inherit the originating site’s IEN:

Upon install to other sites within our VISN of several clinical reminders developed in the Minneapolis Database, the IEN for the health factors being installed via the Reminder Exchange Utility did not inherit the originating site’s IEN.  Health Factors were installed at the other sites via the utility, and were not previously installed at the systems. None of the health factors installed with the IEN of originating site, and all installed with 3 digits IEN, which we know cannot be edited using existing menu options outside of Fileman per Remedy ticket (HD#370941   FRESNO, CA VAMC, submitted 12/22/09) since the IEN is less than 100000. Upon review of other reminders installed post Patch 12, I can see where this has occurred as well.  The reminder exchange utility should not be doing this.

**Resolution** : Health factors being installed via the Reminder Exchange Utility will inherit the originating site’s IEN. All PCE files are corrected with this fix.

**NOTE** : This fix is not retroactive.

**393320**

Installation of the VA-AAA Screening reminder in a live account showed the dialog as disabled when it is actually not disabled.  Dialog is able to be edited.  Dialog should not show disabled.

**399010**

A Location List only looks for the CLINIC Stop Code field for the visit and not a CREDIT Stop Code. Is that correct? When trying to use a LL w/ stop code 135 Post-Deploy Integrated Care (only), an INVALID INPUT ARRAY ENTRY error is generated. However, if any hospital location is added to the list, or a "primary" Clinic Stop Code, the error is not generated. The 135 stop code is supposed to be a "secondary" stop code according to national documentation.

**404828**

STORE+23^PXRMAPI0 errors

In file 811.7, a new sub-category was being added.  At the Sequence number prompt, a letter was accidentally typed instead of a numeric value that was expected.  An error occurred that closed the session.

**423379**

A VISN reminder was imported. The dialog was disabled so it was edited and changed the Disable prompt from "DISABLE AND SEND MESSAGE" to "0" OR "NO". In the Reminders View of the Dialog list it showed that the dialog was disabled. It was verified again that the disable prompt was set to NO but it continued to show that the dialog was disabled. Next was to the disable prompt and put an @ sign to remove "no" from the disable prompt. After this was done the "disable" text in the reminders view disappeared.

**475319**

All error messages follow the same format. What they are saying is that routine TIU^GMTSOBJ expects two variables DFN and a pointer to the HEALTH SUMMARY OBJECT file. However, in this error the name of the HEALTH SUMMARY OBJECT is being passed PROB LIST PALL CARE CONSULT (TIU and although it does exist in the HEALTH SUMMARY OBJECT file, Mumps cannot translate the name to the internal entry number.

In essence this line:

MSG("DIERR",1,"PARAM",3)=S X=$$TIU^GMTSOBJ(DFN,PROB LIST PALL CARE CONSULT (TIU))

Should read something like this:

S OBJ=$O(^GMT(142.5,"B","PROB LIST PALL CARE CONSULT (TIU)",0))

MSG("DIERR",1,"PARAM",3)=S X=$$TIU^GMTSOBJ(DFN,OBJ)

So the problem lies in how the utility packed up the TIU DOCUMENT DEFINITION.

TIU DOCUMENT DEFINITION entry PROB LIST PALL CARE CONSULT did not get installed! Examine the following error message for the reason.

The update failed, UPDATE^DIE returned the following error message:

MSG("DIERR")=1^1

MSG("DIERR",1)=701

MSG("DIERR",1,"PARAM",0)=3

MSG("DIERR",1,"PARAM",3)=S X=$$TIU^GMTSOBJ(DFN,PROB LIST PALL CARE CONSULT (TIU))

MSG("DIERR",1,"PARAM","FIELD")=9

MSG("DIERR",1,"PARAM","FILE")=8925.1

MSG("DIERR",1,"TEXT",1)=The value 'S X=$$TIU^GMTSOBJ(DFN,PROB LIST PALL CARE CONSULT (TIU))' for field OBJECT METHOD in file TIU DOCUMENT DEFINITION is not valid.

MSG("DIERR","E",701,1)=

**556433**

2 bugs -

1.  Reminder test displays N/A, whereas CPRS displays as DUE NOW

2.  Reminder test lists 4 function findings, but there are only 2 in the definition

**584156**

A problem is created when a person's name that is loading an exchanged reminder is not unique.

The update failed, UPDATE^DIE returned the following error message:

MSG("DIERR")=1^1

MSG("DIERR",1)=701

MSG("DIERR",1,"PARAM",0)=3

MSG("DIERR",1,"PARAM",3)=XXXX,XXXX

MSG("DIERR",1,"PARAM","FIELD")=1

MSG("DIERR",1,"PARAM","FILE")=801.44

MSG("DIERR",1,"TEXT",1)=The value “XXXX,XXXXX” for field EDIT BY in EDIT HISTORY SUB-FIELD in file REMINDER DIALOG is not valid.

MSG("DIERR","E",701,1)=

#### General Fixes and Enhancements

In patch PXRM*2*17, the reminders mail message delivery mechanism was generalized to make it more flexible. Several users pointed out that in the past, when an evaluation error occurred, the user doing the evaluation was identified in the mail message, but after patch 17, they no longer were and it was useful to have them identified whenever possible. Changes were made to identify the user receiving the error, whenever possible.

It was learned that the Pharmacy regularly sends updates that fire the Pharmacy update protocol event and these may not always contain drug class updates. Clinical Reminders is attached to this protocol for the purpose of creating an informational message about reminder content that may be affected by drug class updates. When no drug class changes were contained in the Pharmacy update the Clinical Reminders message about drug class updates only contained the header and this was confusing. To prevent this from happening, the code was changed so that if there is no drug class update the message will not be sent.

Some users found the message generated when there is a drug class update confusing and requested changes. Working in conjunction with the Pharmacy Team, a new format was developed. Statements like the following were removed:

VA GENERIC TOLTERODINE (IEN=3495) is represented by its

original drug class AU350, PARASYMPATHOLYTICS

The following was added at the end of the message:

“Check your reminder definitions and terms to be sure the change in drug class does not require adjustment to them.”

A site had a problem tracking down why a reminder did not seem to be working correctly. It turned out that patient data was being recorded incorrectly causing the time to be wrong. To make it easier to detect problems like this, times (when they exist) will be displayed as part of finding dates. Adding the ability to use hourly frequencies (see below) is another reason to display the time.

#### Reminder Computed Findings

Admission ward and discharge ward were added as CSUB data to the VA-WAS INPATIENT computed finding.

A new computed finding named VA-FILEMAN DATE was added. It uses the Computed Finding Parameter to take any date format used in Clinical Reminders and it sets the date of the finding to that date. The purpose is to use it in a function finding to make date comparisons. For example, did a finding occur within 60 days of today?

A new computed finding, VA-RANDOM NUMBER, was added. This is based on an idea from a site that used a locally developed computed finding to generate random numbers for partitioning patients in a research study. This computed finding uses the MUMPS $RANDOM function to return pseudo random numbers as the value. The Occurrence Count is the number of random numbers that will be returned and the Computed Finding Parameter is used to specify the range and optionally the number of decimal digits; the default is to generate integers, i.e., no decimal digits. The Occurrence Count entry on the finding will be an absolute value.  Entering an Occurrence Count of 5 or -5 will result in 5 returns.

The format of the Computed Finding Parameter is:  LB^UB^NDD, where LB is the inclusive lower bound, UB is the inclusive upper bound, and NDD is the optional number of decimal digits. LB and UB must be integers and UB must be greater than LB. If these conditions are not met then the computed finding will be false.

**NOTE** : This CF was developed for use with research program consideration/use.  No clinical uses have been identified at present.  Every evaluation of this finding on a given patient will yield different results, thus the name RANDOM.  Please use caution when using this Computed Finding in a clinical setting.***

Four new computed findings to support the needs of PACT (Patient Aligned Care Teams) were added. They are:

1   VA-PCMM PATIENTS ASSIGNED TO A PRACTICTIONER

2   VA-PCMM PATIENTS ASSIGNED TO A TEAM

3   VA-PCMM PC TEAM AND INSTITUTION

4   VA-PCMM PRACTICTIONERS ASSIGNED TO A PATIENT

The first two are list type and the second two are multiple type.

During testing of the new VA-PCMM computed findings continued, it was found that an additional parameter is required for them to work correctly. INCLUDE was added as an optional parameter to:

VA-PCMM PATIENTS ASSIGNED TO A PRACTITIONER

VA-PCMM PATIENTS ASSIGNED TO A TEAM

VA-PCMM PRACTITIONERS ASSIGNED TO A PATIENT

This is the part from the help for VA-PCMM PATIENTS ASSIGNED TO A TEAM that explains how to use INCLUDE:

NAME: VA-PCMM PATIENTS ASSIGNED TO A PRACTITIONER

ROUTINE: PXRMPCMM                     ENTRY POINT: PTPR

PRINT NAME: VA-PCMM Patients Assigned to a Practitioner

TYPE: LIST

DESCRIPTION:   This list type computed finding returns a list of patients

assigned to a practitioner in the date range defined by Beginning Date/Time

and Ending Date/Time. A patient will be on the list if they were assigned to

the practitioner at anytime during the date range. The Computed Finding

Parameter is used to specify the practitioner. It can be either the IEN or the

exact name (.01 field) from file #200, the New Person file.

The Computed Finding Parameter can be used to pass the optional parameter

INCLUDE. If you want to use this parameter, it is passed as the second piece

of the Computed Finding Parameter. The possible values of INCLUDE are:

0 - include patients who were assigned anytime in the date range.

1 - include patients who were assigned for the entire date range.

The default is 0.

The format for the computed finding parameter is: PRACTITIONER^INCLUDE

For example, if the practitioner is PROVIDER,ONE and you want the value of

INCLUDE to be 1 then the computed finding parameter would be:

PROVIDER,ONE^1

NAME: VA-PCMM PATIENTS ASSIGNED TO A TEAM

ROUTINE: PXRMPCMM                     ENTRY POINT: PTTM

PRINT NAME: VA-PCMM Patients Assigned to a Team

TYPE: LIST

DESCRIPTION:   This list type computed finding returns a list of patients

assigned to a team in the date range specified by Beginning Date/Time and

Ending Date/Time. If the patient was assigned to the team at anytime during

the date range they will be on the list. The Computed Finding Parameter is

used to specify the team. It can be either the IEN or the exact name (.01

field) from file #404.51, the Team file.

The Computed Finding Parameter can be used to pass the optional parameter

INCLUDE. If you want to use this parameter, it is passed as the second piece

of the Computed Finding Parameter. The possible values of INCLUDE are:

0 - include patients who were assigned anytime in the date range.

1 - include patients who were assigned for the entire date range.

The default is 0.

The format for the computed finding parameter is: TEAM^INCLUDE

For example, if the team is TEAM ONE and you want the value of INCLUDE to be 1

then the computed finding parameter would be:

TEAM ONE^1

NAME: VA-PCMM PRACTITIONERS ASSIGNED TO A PATIENT

ROUTINE: PXRMPCMM                     ENTRY POINT: PRPT

PRINT NAME: VA-PCMM Practitioners Assigned to a Patient

TYPE: MULTIPLE

DESCRIPTION:   This multiple valued computed finding returns a list of

practitioners assigned to a patient in the date range defined by the Beginning

Date/Time and Ending Date/Time.

The Computed Finding Parameter can be used to pass the optional parameter

INCLUDE. The possible values are:

0 - include practitioners who were assigned anytime in the date

range.

1 - include practitioners who were assigned for the entire date

range.

The default is 0.

For example, if you want the value of INCLUDE to be 1 then the computed

finding parameter would be: 1

Two new computed findings for working with patient record flags were created: VA-PATIENT RECORD FLAG INFORMATION and VA-PATIENT RECORD FLAG LIST. Note these computed findings require patch DG*5.3*836.

A site reported that they have some patients whose height has been entered as 0 and it causes the BMI computed finding to take an error. A check was added to the BMI and BSA computed findings to ignore any height entries with a value of 0. (It is difficult to determine how those got entered because the Vitals package normally will not allow heights of 0 to be entered.)

The patch init will make sure all national computed findings have print names starting with “VA-“. In conjunction with this the print name maximum length of 40 characters was increased to 64.

Several other national print name problems were corrected:

VA-PATIENT TYPE print name was PATIENT TYPE changed to VA-Patient Type.

VA-TREATING FACILITY LIST print name was Treating FaciLity list, it was changed to VA- Treating Facility List.

VA-WH MAMMOGRAM ABNORMAL IN WH PKG print name was blank; it was changed to VA-WH Mammogram Abnormal in WH PKG.

VA-WH PAP SMEAR ABNORMAL IN WH PKG print name was blank; it was changed to VA-WH Pap Smear Abnormal in WH PKG.

The computed finding VA-APPOINTMENTS FOR A PATIENT was not doing proper data reversal for a negative Occurrence Count; this was fixed. It was enhanced to display additional lines of text for each of the field numbers that can be passed in.

A problem was reported where computed findings whose date is the evaluation date/time were only displaying the time as a decimal number, 0.23252 in the CPRS display. This was not occurring when the same reminder was done in reminder test. This occurs because the RPC for CPRS calls MAIN^PXRM, which in turn calls EVAL^PXRM and is not passing the date into EVAL^PXRM. Reminder test calls EVAL^PXRM directly and is passing the date. Changes were made in NOW^PXRMDATE to accommodate the new frequencies, and a test was made for PXMRDATE=””.  It should have been +$G(PXRMDATE)=0. This change was made and MAIN^PXRM was changed to pass in the current date/time to EVAL^PXRM. Changing MAIN^PXRM to pass the current date/time to EVAL^PXRM means that PXRMCDEF would not work properly, so it was changed to call EVAL^PXRM.

The computed finding VA-DATE FOR AGE was modified to properly handle patients who were born on Feb 29. Previously, the new day was always Feb 29 even if the new year was not a leap year. Now if the new year is not a leap year, the day will be Feb 28.


#### Reminder Definitions

There were a couple of errors in the description of the Usage field.

Original Description:

The Usage field describes how the reminder definition will be used. This field must contain C if the reminder is to be selected in CPRS. The L or the O values will override all other values. For example, if L and C are defined in the usage field, the Reminder will not show on the cover sheet in CPRS, because L is in the Usage field.

This is free text field and can contain any combination of the following codes:

Code  Usage

C     CPRS

L     Reminder Patient List

O     Reminder Order Checks

P     Patient

R     Reminder Reports

X     Reminder Extracts

*     All of the above, except L, and O.

Corrected Description:

The Usage field describes how the reminder definition can be used. This field must contain C or * if the reminder is to be selected in CPRS. The L or the O values will override all other values. For example, if L and C are defined in the Usage field, the Reminder will not show on the cover sheet in CPRS, because L is in the Usage field.

This is free text field and can contain any combination of the following codes:

Code  Usage

C    CPRS

L    Reminder Patient List

O    Reminder Order Checks

P    Patient

R    Reminder Reports

X    Reminder Extracts

*    All of the above, except L, O, and P.

Remedy ticket #360708 reported a problem with the incorrect calculation of the resolution date when the resolution logic contains function findings. This occurred because the resolution date calculation was not properly differentiating between true and false function findings. This was corrected.

Remedy ticket #413731 pointed out a problem with non-VA meds that turned out to be two problems. The first is the old issue where the Index for non-VA meds has incorrect entries. Remedy ticket #347730 reporting this problem was submitted September 4, 2009 and it still has not fixed by Pharmacy. The second problem was a display issue. By default, the date of a drug finding is the stop date. If USE START DATE is true the date of a drug finding is the start date. However, even if USE START DATE was true, the stop date was being displayed as the date of the finding. That has been corrected so that now whichever date is selected for the drug finding will be displayed as its finding date.

Clin4 support staff pointed out that the value for blood pressure can come back in either of the following forms: SYSTOLIC/DIASTOLIC or SYSTOLIC/MEAN/DIASTOLIC; the second form is not very common. If the second form comes back then the DIASTOLIC CSUB would have the value for mean, and if $P was used in a Condition, it would also be the mean. The code was changed so that the DIASTOLIC CSUB will always have the correct value. If you are using $P in a Condition, we recommend that you replace it with the appropriate CSUBs. Several national definitions and terms were originally distributed with Conditions using $P; as part of this patch they will be updated to use the SYSTOLIC and DIASTOLIC CSUBs.

The following updates are made:

Definitions:

VA-HTN ASSESSMENT BP &gt;=140/90

FI(11)   CONDITION: I $P(V,"/",1)&gt;139!($P(V,"/",2)&gt;89)

changed to I (V("SYSTOLIC")&gt;139)!(V("DIASTOLIC")&gt;89)

FI(13)  CONDITION: I $P(V,"/",1)&gt;159!($P(V,"/",2)&gt;99)

changed to  I (V("SYSTOLIC")&gt;159)!(V("DIASTOLIC")&gt;99)

VA-HTN ASSESSMENT BP &gt;=160/100

FI(13) CONDITION: I $P(V,"/",1)&gt;159!($P(V,"/",2)&gt;99)

changed to I (V("SYSTOLIC")&gt;159)!(V("DIASTOLIC")&gt;99)

VA-HTN LIFESTYLE EDUCATION

FI(11) CONDITION: I $P(V,"/",1)&gt;139!($P(V,"/",2)&gt;89)  changed to I (V("SYSTOLIC")&gt;139)!(V("DIASTOLIC")&gt;89)

Terms:

VA-BP &gt;130/80

Mapped item 1:  CONDITION: I $P(V,"/",1)&gt;130!($P(V,"/",2)&gt;80)

changed to I (V("SYSTOLIC")&gt;130)!(V("DIASTOLIC")&gt;80)

VA-BP &gt;130/80 (ANY OF LAST 3)

Mapped item 1: CONDITION: I $P(V,"/",1)&gt;130!($P(V,"/",2)&gt;80)  changed to I (V("SYSTOLIC")&gt;130)!(V("DIASTOLIC")&gt;80)

VA-BP &gt;=140/90

Mapped item 1:  CONDITION: I $P(V,"/",1)&gt;139!($P(V,"/",2)&gt;89)

changed to I (V("SYSTOLIC")&gt;139)!(V("DIASTOLIC")&gt;89)

VA-BP &gt;=160/100

Mapped item 1:  CONDITION: I $P(V,"/",1)&gt;159!($P(V,"/",2)&gt;99)

changed to I (V("SYSTOLIC")&gt;159)!(V("DIASTOLIC")&gt;99)

On the Nov 19, 2010 national reminder call, there was a discussion about frequency being required. If there is no resolution logic, then frequency is not required as long as AGE is not in the cohort logic (because age is associated with a frequency). Even if there was no resolution logic, no age in the cohort logic, and no frequency, the status was being returned as CNBD. This was changed so that as long as there is no AGE in the cohort logic and no resolution logic, the status will be either DUE or N/A. If AGE is used in the cohort logic, then a baseline age range must be defined.

Special checks for list type reminders were added:

The cohort logic cannot start with a logical not

The cohort logic cannot contain a logical or not

If SEX is used in the cohort logic, the reminder must be sex-specific. SEX cannot be the first element in the cohort logic unless it is followed by AGE.

New functionality was added to allow using the date of one finding to set the date range of another finding. The syntax is FIEVAL(M,”DATE”) or FIEVAL(M,N,”DATE”) where M is the finding number and N is the occurrence. This means you can now use dates like FIEVAL(3,”DATE”)-3M as the Beginning or Ending Date/Time of another finding. The global reminder dates PXRMDOB and PXRMLAD can also be used. Note that if FIEVAL(M) is false or PXRMLAD does not exist then the finding whose date range depends on the date of finding M will be set to false.

In conjunction with allowing FIEVAL(M,N,”DATE”) to be used in Beginning Date/Time or Ending Date/Time additional frequency units were added. The allowed values are now: H (hours), D (days), W (weeks), M (months), and Y (years). This change applies everywhere that a frequency can be used including Beginning Date/Time, Ending Date/Time, Reminder Frequency in the Baseline Age Findings multiple, Findings multiple, Function Findings multiple, and Custom Date Due. Custom Date Due will now allow both “+” and “-“, in the past it only allowed “+”.

A number of changes and improvements were made to function findings:

The set of allowed operators in function finding strings was expanded. It now includes: +, -, *, **, /, \, #, !, &amp;, `, &gt;, &lt;, =, ], [. The additions were *, **, /, \, #.

An optional third argument of “N” was added to the DIFF\_DATE function. If this argument is present, the actual value instead of the absolute value is returned.

A new function DTIME\_DIFF, which is a generalized version of DIFF\_DATE, was added.

NOTE: There has been a lot of discussion about whether or not the default for the new function DTIME\_DIFF should be the absolute value like DIFF\_DATE. A poll of users came out slightly in favor of the default being the real value.

All function findings were improved to handle the case when the findings they use are false. Functions will now return the value “UNDEF” when they cannot be evaluated.

Two new functions, MAX\_VALUE and MIN\_VALUE, were added.

There were some CSUBs that could not be used in a function finding because they would not pass the input transform. ”ADMISSION DATE/TIME” is an example of one that could not be used. It was not passing because of the space and the “/”.The input transform was changed to allow all legitimate CSUBs.

Clin4 reported that list type reminder that used the VALUE function in a function finding failed the validation when creating a reminder rule. This was because the validater was written before functions could have CSUB values as arguments. The validation code was changed handle those cases.

Two new options were added to the reminder definition management menu:

- Integrity Check Selected
- Integrity Check All.

These can be used to check the integrity of selected or all reminder definitions, including function findings. The integrity check will also be made automatically whenever a reminder definition has been edited. Fatal errors (F) that will prevent the reminder from working properly and warnings (W) will be given. The following checks are made:

W – The Usage field contains a “P” and it is not a national reminder

F – Each finding is checked to make sure it exists

F – If either the Beginning Date/Time or Ending Date/Time contains FIEVAL(M,”DATE”) or FIEVAL(M,N,”DATE”) the definition is checked to make sure it contains finding M and if an occurrence is used the Occurrence Count of finding M is checked to make sure it is greater than or equal to N.

F- Function findings functions of the form FUNCTION(M) and FUNCTION(M,N) are checked to make sure finding M is in the definition and the Occurrence Count of finding M is greater than or equal to N.

F – If a Custom Date Due is defined, it is checked to make sure that the findings used in the Custom Date Due all exist in the definition.

F – Patient Cohort Logic and Resolution Logic are checked to make sure that the findings used in the logic all exist in the definition.

F – Logic strings are checked to make sure their syntax is valid.

F – The definition contains Resolution Logic but does not have a baseline frequency or any findings that will set a frequency.

W – The definition contains Resolution Logic but does not have a baseline frequency. It does have findings that will set a frequency. This could be a problem if all findings that set frequency are false.

#### Reminder Dialogs

A new report, PXRM DIALOG CHECKER ALL, was added to the Dialog Reports Menu. It checks all active reminder dialogs for invalid items.

As a result of Remedy ticket #418968, dialog loading was changed to look for prompts when loading a reminder taxonomy in a dialog. If prompts are defined, then they will display in CPRS instead of the default prompts defined in the reminder finding parameter file. Also, a SUPPRESS ALL PROMPTS prompt was added to the group and element editors. This prompt only shows when a taxonomy is used as a finding item. If the value is set to YES, then no prompts will show in CPRS when using a taxonomy in a dialog.

#### Reminder Exchange

A problem where a TIU Template was being packed up incorrectly was corrected.

All entries in PCE files were installing at a low IEN which makes them national so sites could not edit them. This was changed; now only national PCE entries will be installed at low IENs.

Reminder Exchange did not have all the functionality needed to for installing updates to national terms. The merge action preserved site mapped findings but did not allow updates of finding modifiers such as Beginning Date/Time and Ending Date/Time for nationally mapped findings. To improve this situation a new action called update was being added and a change to how merge works was made.

For terms, these actions work as follows:

- Update – any finding that is in the Exchange entry and not already mapped is added, findings that are in the Exchange entry and already mapped in the site entry are updated, i.e., all finding modifiers are set to the values in the Exchange entry. Findings that are mapped in the site entry but not in the Exchange entry are left as is.
- Merge – any finding that is already mapped in the site entry is left as is, any finding that is in the Exchange entry but not already mapped in the site entry is added.

For dialogs, these actions work as follows:

- Update – additional findings that are in the site entry are left and any additional findings that are in the Exchange entry but not already in the site entry are added. All other dialog fields are set to what is in the Exchange entry.
- Merge – additional findings that are in the site entry are left and any additional findings that are in the Exchange entry but not already in the site entry are added.

Note that during interactive installs action choices for dialogs are only available when using the install selection action. If install all is used, everything is installed in overwrite mode.

#### Reminder Location Lists

Using a non-existent location list was causing a hard error during reminder evaluation. A change was made so this will generate an evaluation status of ERROR instead causing a hard error. Also, a MailMan message will be sent to the Clinical Reminders group. The message has the following format:

The Computed finding evaluation requested by XXXX,YYY on

MMM DD, YYYY@HH:MM:SS requires appointment data which could not be obtained from the Scheduling database due to the following error(s):

INVALID INPUT ARRAY ENTRY

#### Reminder Patient Lists

A bug that prevented location lists from working properly when used to build a patient list was corrected.

Clin4 found a problem with a reminder rule incorrectly including patients who should not have been on a list. This was tracked to incorrect evaluation of a function finding for list building and the problem was corrected.

Clin4 reported that if Race was one of the selected items in a delimited output Patient Demographic Report, no values were listed unless the number of occurrences was two or more. This was fixed so that values are listed for any number of occurrences.

#### Reminder Reports

A site reported a problem with a reminder due report displaying the following error message:

**The Reminders Due Report  requested by XXXX,YYYYYY on Nov 23, 2010@14:24:21was cancelled for the following reason(s): INVALID INPUT ARRAY ENTRY**

A space was added between the date/time and the word “was”. The blank space between Report and requested was occurring because the report did not have a title. The code was changed to display the report title if it is defined, and not leave a blank space if it is not defined.

#### Reminder Terms

During the testing of PXRM*2.0*17, a test site noticed a problem with the output for drug classes in a term. The drug class the drug belonged to was not being displayed like it is when a drug class is used directly as a finding in a reminder definition. Code was added to display the drug class or VA Generic, so that the output is similar to when drug classes or VA Generics are used directly as findings in a definition.

#### Reminder Test

Display of Beginning Date/Time and Ending Date/Time for each finding was added.

The format is:

FIEVAL(“BDT”)=Input date/time

FIEVAL(“BDTE”)=evaluated date/time

FIEVAL(“EDT”)=Input date/time

FIEVAL(“EDTE”)=evaluated date/time.

#### Reminder Category

The input transform for the Display Order field in the Sub-Category multiple of the Reminder Category file had a bug. The first part of the input transform checks to make sure the user has typed in a number between 1 and 99, and the second part calls a routine to make sure the display order is unique. If the user inputs text instead of a number, the input fails the first part of the input transform and the routine is called with an undefined value for Display Order, which causes an error. The input transform was changed so that if the input fails the first part of the input transform, the routine is not called. Remedy ticket #404828.


#### National Reminder Exchange Entries Distributed with this patch

NATIONAL BLOOD PRESSURE CONDITION CHANGES

VA-MH NO SHOW APPT CLINICS LL

VA-INFLUENZA 2010 UPDATES

VA-TEXT INFO SCREEN FOR AAA (RD)

VA MH SCREENING REMINDERS UPDATE

VA-EMBEDDED FRAGMENTS RISK EVALUATION

VA BRANCHING LOGIC REMINDER UPDATES OEF/OIF

VA-INFLUENZA H1N1 UPDATE

VA-MHV INFLUENZA VACCINE

VA-ALCOHOL F/U POS AUDIT-C

VA-MH HIGH RISK NO-SHOW FOLLOW-UP

VA-TB/POSITIVE PPD

VA-PATIENT RECORD FLAG INFORMATION

The contents of NATIONAL BLOOD PRESSURE CONDITION CHANGES are described earlier.

The VA-MH NO SHOW APPT CLINICS LL location list includes clinic stop codes for MH clinics that are scheduled for face-to-face appointments.


## Acronyms

| Term       | Definition                                                           |
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