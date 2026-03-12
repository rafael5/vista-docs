---
app_name: 'Registry: Airborne Hazard Open Burn Pit (AHOBPR) (PXRM)'
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: null
doc_type: setup-config
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-11'
is_base: false
is_change_pages: false
library_max_patch: null
package_id: PXRM
patch: 176
patch_gap: null
section: ''
source_file: pxrm_2_18_ig.docx
status: draft
title: PATIENT             PT ID     APPT D/T             CLINIC          STATUS
---

## High Risk Mental Health Patient – Reminder &amp; Flag


**Patches**

**DG*5.3*836**

**GMTS*2.7*99**

**PXRM*2*18**

**SD*5.3*578**

**TIU*1.0*260**

## INSTALLATION and SETUP GUIDE

**February 2012**

Product Development


Contents

Introduction	1

Related Manuals	2

Web Sites	2

Pre-Installation	3

Required Software for PXRM*2*18	4

Estimated Installation Time: 10-15 minutes	5

Installation	6

1.	Retrieve the host file containing the multi-package build, HIGH RISK MH 1.0.	6

2.	Install the build first in a training or test account.	6

3.	Load the distribution.	6

a.	Backup a Transport Global	7

b.	Compare Transport Global to Current System	7

c.	Verify Checksums in Transport Global	7

d.	Print Transport Global (optional)	9

4.	Install the build.  (see an example of the install  Appendix A)	9

5.	Install File Print	10

6.	Build File Print	10

7.	Post-installation routines	11

8.	Deletion of init routines	12

Post-Install Set-up Instructions	13

Appendix A: Installation Example	17

Appendix B – Nightly Background Job and Ad Hoc Report Examples	25

Ad Hoc No Show Report by Mental Health Only Stop Code Example	33

Ad Hoc No Show Report by Mental Health Clinic	36

Ad Hoc No Show Report for All Clinics	37

Acronyms	44

## Introduction

The purpose of this project is to release 1) two new Scheduling reports that identify no-show “high risk for suicide” patients that missed their MH appointments, 2) a new national reminder and reminder dialog that will be used by providers to document results of following up with a high risk for suicide patient that missed a MH appointment, and 3) provide a health summary type with MH-specific supporting information. This functionality is in Increment 1 and 2 of the High Risk MH Patient – Reminder and Flag project.

The first release of the High Risk Mental Health Patient- Reminder and Flag (HRMHP) project includes five patches, which will be installed as a combined build, HIGH RISK MH 1.0. This Installation Guide describes installing and setting up Increments 1 and 2. Increments 3 and 4 will be released in a future build.

SD*5.3*578

This Scheduling patch provides two new MH NO SHOW Scheduling Reports for use by Suicide Prevention Coordinators and other Mental Health professionals. The reports will support following up with High Risk for Suicide patients who missed a scheduled MH appointment.

DG*5.3*836

This Registration Patient Record Flag patch provides new interfaces used by the Scheduling and Reminder patches to determine the High Risk for Suicide flag status on a specified date.

PXRM*2*18

This patch will create a national reminder to notify clinicians of a patient's risk of suicide and will create a dialog the clinicians can use to document follow-up with the high risk patients when they miss MH appointments. This Clinical Reminder patch supports the Scheduling patch by providing a national Reminder Location List of Mental Health stop codes used for scheduled appointments.  Additionally, this patch includes miscellaneous clinical reminder maintenance changes. Details of all the Clinical Reminder changes can be found in the Release Notes.

GMTS*2.7*99

This patch installs four Health Summary Components (MAS CONTACTS, MAS MH CLINIC VISITS, MH HIGH RISK PRF HX, and MH TREATMENT COORDINATOR),  two Health Summary Types (VA-MH HIGH RISK PATIENT  and REMOTE HIGH RISK MH PATIENT),, and a single Health Summary Object(VA-MH HIGH RISK PATIENT (TIU)).

TIU*1*260

This patch will install one new Object into the TIU DOCUMENT DEFINITION file (8925.1): MH MISSED APPOINTMENTS 10D.

MH MISSED APPOINTMENTS 10D is used by the VA-MH HIGH RISK NO SHOW

FOLLOW-UP reminder dialog to display any No-Show or No-Show and Rescheduled mental health clinic appointments for the past 10 days.

This High Risk MH build can be installed with users on the system. Installation will take between 5 and 15 minutes. A number of Clinical Reminders Exchange entries will be installed and the installer may be prompted for replacement items. Because of this, the build should not be queued and the site's Clinical Reminders manager should be on hand during the install. Details about these Exchange entries can be found below.


**IMPORTANT** – The reminder term VA-MHV INFLUENZA IMMUNIZATION will be installed with the overwrite action, which means that all locally mapped findings will be removed. Therefore, prior to the installation, sites should use the “Inquire about Reminder Term” option to check this term and verify that it has been mapped with your local findings.  If there are no mapped local findings, then after this install, add proper local mappings to complete this reminder term’s definition.  If there are local mapped findings in the reminder definition, save the output of the term inquiry for this term into something permanent (such as a document). After the installation, the term will have a single mapped finding, which will look similar to this:

Finding Item: INFLUENZA, HIGH DOSE SEASONAL, PRESERV-FREE

(FI(1)=IM(612013))

Finding Type: IMMUNIZATION

Beginning Date/Time: 8/20/10

Use the saved term inquiry as a reference and add back the locally mapped findings that were removed.  Do not remove the mapped finding that was installed by the patch.


#### Related Manuals

| **Documentation**                                   | **Documentation File name**   |
|-----------------------------------------------------|-------------------------------|
| High Risk Mental Health Patient Release Notes       | PXRM_2_RN.PDF                 |
| Clinical Reminders User Manual                      | PXRM_2_18_UM.PDF              |
| Clinical Reminders Manager’s Manual                 | PXRM_2_MM.PDF                 |
| Clinical Reminders Technical Manual                 | PXRM_2_18_TM.PDF              |
| Scheduling Patch 578 Installation and Setup Guide   | SD_5_3_578_IG.PDF             |
| Registration Patch 836 Installation and Setup Guide | DG_5_3_836_IG.PDF             |
| Health Summary User Manual                          | HSUM_2_7_99_UM.PDF            |
| Health Summary Technical  Manual                    | HSUM_2_7_99_TM.PDF            |

#### Web Sites

| **Site**                              | **URL**                                                                                                            | **Description**                                                                            |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| National Clinical Reminders site      | http://vista.med.va.gov/reminders                                                                                  | Contains manuals, PowerPoint presentations, and other information about Clinical Reminders |
| National Clinical Reminders Committee | [http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx](http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx) | This committee directs the development of new and revised national reminders               |
| VistA Document Library                | [http://www.va.gov/vdl/](http://www.va.gov/vdl/)                                                                   | Contains manuals for Clinical Reminders and                                                |

**NOTE** : In this document you will see references to both PXRM*2*18 and PXRM*2.0*18.  The difference is that PXRM*2*18 is the name of the patch and PXRM*2.0*18 is the name of the build.

## Pre-Installation

**Pre-Install Setup Steps:**

**We recommend that the team who will be responsible for implementing this project coordinate before installing the patches, to determine the first two pre-install steps. This team could include MH coordinators, Suicide Prevention Coordinators, Clinical Application Coordinators (CACs), Reminders Managers, and IRM staff.**

1. (IRM staff or CAC): Check to see if there is a local Patient Record Flag entry for “HIGH RISK FOR SUICIDE.” Open the “Record Flag Management” menu option on the “Patient Record Flags Main Menu,” and then use the Change Category (CC) action to switch to Flag Category II (Local) and see what’s listed as local flags.  HIGH RISK FOR SUICIDE was the PRF name recommended by VHA Directive 2008-036, dated July 18, 2008.

During the DG*5.3*836 install, IRM staff will be asked:

Do you want to update the Parameter Definition for the local Patient Record Flag related to HIGH RISK FOR SUICIDE at this time? YES//

Enter the Local Patient Record Flag that you are using as your "High Risk

for Suicide" flag.  If not already defined use the Directive

recommendation: HIGH RISK FOR SUICIDE. If already defined use your current

flag name.

Recommended Flag: HIGH RISK FOR SUICIDE  Replace

1. (IRM staff, Mental Health Coordinator, or CAC) During the SD*5.3*578 install, IRM staff will be asked to enter the name for the mail group owner of the new mail group SD MH NO SHOW NOTIFICATION.  The owner assigned will be responsible for entering the names of Suicide Prevention Coordinators and/or other MH professionals into the Mail Group. Sites can decide who this owner should be – an IRM staff member, a CAC, or one of the MH-SPC team. Check to see if there’s a mail group expert at your site. NOTE: Self enrollment is not allowed for this mail group.

1. Prior to installing the patch, the HEALTH SUMMARY COMPONENT file (#142.1) needs to be examined for any ABBREVIATION entries that will conflict with the four new components exported with this patch.  Each new national component along with its ABBREVIATION is listed here:

NAME                                    ABBREVIATION

MAS CONTACTS                            CON

MAS MH CLINIC VISITS FUTURE             MHFV

MH HIGH RISK PRF HX                     MHRF

MH TREATMENT COORIDNATOR                MHTC

The "C" cross-reference for the HEALTH SUMMARY COMPONENT file (#142.1) contains the ABBREVIATION for each component.  Examine the global listing for this cross-reference to determine if any local components will need the ABBREVATION field updated. If an ABBREVIATION conflict is found, the "Create/Modify Health Summary Components" option of the GMTS IRM MAINTENANCE MENU should be used to edit the local component's ABBREVIATION.

The GMTS patch contains an installation routine (GMTSPI99) that will perform an environment check, do any necessary housekeeping, and then install the new Health Summary items. The environment check will examine the HEALTH SUMMARY COMPONENT file (#142.1) to ensure there will not be any NAME (.01) or NUMBER (.001) collisions with the four new nationally deployed Health Summary Components (MAS CONTACTS, MAS MH CLINIC VISITS FUTURE , MH HIGH RISK PRF HX , and MH TREATMENT COORDINATOR).  If any possible collisions are found, the install will be aborted until the issue is resolved.  After the issue has been addressed, local IT staff can re-install the patch.

After the environment check, the PRE section of the routine will delete any previous versions of: the Reminder Exchange file used to deploy portions of the Health Summary items, the Health Summary Components, and the Health Summary Types (VA-MH HIGH RISK PATIENT and REMOTE HIGH RISK MH PATIENT). PRE will also re-index the HEALTH SUMMARY TYPE and HEALTH SUMMARY COMPONENT files along with rebuilding the Ad Hoc Health Summary.

After PRE, the POST section of the routine will create stub entries in file #142 for the remote Health Summary Type, and then call the silent Reminder Exchange install utility to install the remaining Health Summary items.  Lastly, POST will re-index the HEALTH SUMMARY TYPE and HEALTH SUMMARY COMPONENT files along with rebuilding the Ad Hoc Health Summary.

1. Check for local mappings of VA-MHV INFLUENZA IMMUNIZATION (see pages 2 and 14 in this manual for more instructions).

### Required Software for PXRM*2*18

| **Package/Patch**                     | **Namespace**   |   **Version** | **Comments**   |
|---------------------------------------|-----------------|---------------|----------------|
| Clinical Reminders  PXRM*2*17         | PXRM            |           2   | Fully patched  |
| GEN. MED. REC. – VITALS  GMRV*5*25    | GMRV            |           5   |                |
| Health Summary                        | GMTS            |           2.7 | Fully patched  |
| HL7                                   | HL              |           1.6 | Fully patched  |
| Kernel                                | XU              |           8   | Fully patched  |
| MailMan                               | XM              |           7.1 | Fully patched  |
| NATIONAL DRUG FILE  PSN*4.0*176       | PSN             |           4   |                |
| Pharmacy Data Management  PSS*1.0*133 | PSS             |           1   |                |
| Outpatient Pharmacy  PSO*7.0*299      | PSO             |           7   |                |
| RADIOLOGY/NUCLEAR MEDICINE  RA*5*56   | RA              |           5   |                |
| Registration  DG*5.3*836              | DG              |           5.3 | Fully patched  |
| Scheduling  SD*5.3*578                | SD              |           5.3 | Fully patched  |
| TOOLKIT  XT*7.3*111                   | XT              |           7.3 |                |
| VA FileMan                            | DI              |          22   | Fully patched  |


**Required Software for DG*5.3*836**

| **Package/Patch**       | **Namespace**   |   **Version** | **Comments**   |
|-------------------------|-----------------|---------------|----------------|
| Registration/Enrollment | DG              |           5.3 | Fully patched  |

**Required Software for SD*5.3*578**

| **Package/Patch**   | **Namespace**   |   **Version** | **Comments**   |
|---------------------|-----------------|---------------|----------------|
| Scheduling          | SD              |             5 | Fully patched  |


**Required Software for GMTS*2.7*99**

| **Package/Patch**   | **Namespace**   |   **Version** | **Comments**   |
|---------------------|-----------------|---------------|----------------|
| Health Summary      | GMTS            |           2.7 | Fully patched  |

**Required Software for TIU*1*260**

| **Package/Patch**          | **Namespace**   |   **Version** | **Comments**   |
|----------------------------|-----------------|---------------|----------------|
| Text Integration Utilities | TIU             |             1 | Fully patched  |

### Estimated Installation Time: 10-15 minutes


## Installation

This manual describes how to install the combined build that includes builds DG*5.3*836,  SD*5.3*578, GMTS*2.7*99, TIU*1.0*260, and PXRM*2.0*18.

This build can be installed with users on the system, but it should be done during non-peak hours.

***The installation needs to be done by a person with DUZ(0) set to "@."***

***NOTE: DO NOT QUEUE THE INSTALLATION, because this installation asks questions requiring responses and queuing will stop the installation. A Reminders Manager or CAC should be present to respond to these.***

**NOTE: We recommend that a Clinical Reminders Manager or CAC be present during the install, so that if questions occur during the install of Reminder Exchange entries, a knowledgeable person can respond to them.**

### 1 Retrieve the host file containing the multi-package build, HIGH RISK MH 1.0.

Use ftp to access the build (the name of the host file is HIGH\_RISK\_MH\_1\_0 .KID) from one of the following locations (with the ASCII file type):

ftp.fo-albany.med.va.gov                  &lt;ftp://ftp.fo-albany.med.va.gov&gt;

Hines                           ftp.fo-hines.med.va.gov                     &lt;ftp://ftp.fo-hines.med.va.gov&gt;

ftp.fo-slc.med.va.gov                          &lt;ftp://ftp.fo-slc.med.va.gov&gt;

### 2 Install the build first in a training or test account.

Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

### 3 Load the distribution.

In programmer mode type, D ^XUP, select the Kernel Installation &amp; Distribution System menu (XPD MAIN), then the Installation option, and then the option LOAD a Distribution.  Enter your directory name and HIGH\_RISK\_MH\_1.0.KID at the Host File prompt.

**Example**

Select Installation Option: **LOAD** a Distribution

Enter a Host File: [DIR] HIGH\_RISK\_MH\_1.0.KID,where [DIR] is the local

directory where you have stored the host file.

Loading Distribution...

HIGH RISK MH 1.0

DG*5.3*836

SD*5.3*578

Build GMTS*2.7*99 has an Environmental Check Routine

Want to RUN the Environment Check Routine? YES//

GMTS*2.7*99

Will first run the Environment Check Routine, GMTSPI99

Verifying installation environment...

Checking Health Summary Component file (#142.1)

TIU*1.0*260

PXRM*2.0*18

Use INSTALL NAME: HIGH RISK MH 1.0 to install this Distribution.

From the Installation menu, you may elect to use the following options:


### 4 Backup a Transport Global

This option will create a backup message of any routines exported with the patch.  It will NOT back up any other changes such as DDs or templates.

INSTALL NAME: HIGH RISK MH 1.0

### 5 Compare Transport Global to Current System

This option will allow you to view all changes that will be made when the patch is installed.  It compares all components of the patch (routines, DDs, templates, etc.).

### 6 Verify Checksums in Transport Global

This option will allow you to ensure the integrity of the routines that are in the transport global.  If there are any discrepancies, do not run the Install Package(s) option. Instead, run the Unload a Distribution option to remove the Transport Global from your system.  Retrieve the file again from the anonymous directory (in case there was corruption in FTPing) and Load the Distribution again.  If the problem still exists, log a Remedy ticket and/or call the national Help Desk (1-888-596-HELP) to report the problem.

Select INSTALL NAME: HIGH RISK MH 1.0

=&gt;    High Risk Mental Health multi-package build, increment 1.

;Created on Dec 09, 2011@08:20:31

It consisted of the following Install(s):

HIGH RISK MH 1.0     DG*5.3*836     SD*5.3*578    GMTS*2.7*99    TIU*1.0*260

PXRM*2.0*18

Want each Routine Listed with Checksums: Yes//   YES

DEVICE: HOME//   VIRTUAL TELNET

PACKAGE: HIGH RISK MH 1.0

-------------------------------------------------------------------------------

0 Routine checked, 0 failed.

PACKAGE: DG*5.3*836     1

-------------------------------------------------------------------------------

DG53836P  Calculated    3205508

DGPFAPIH  Calculated   25281301

DGPFAPIU  Calculated   23057347

3 Routines checked, 0 failed.

PACKAGE: SD*5.3*578

-------------------------------------------------------------------------------

SDAMQ     Calculated    9692546

SDMHAD    Calculated  116553024

SDMHAD1   Calculated   85354679

SDMHNS    Calculated   24321441

SDMHNS1   Calculated   98089996

5 Routines checked, 0 failed.

PACKAGE: GMTS*2.7* 1

-------------------------------------------------------------------------------

GMTSMHAP  Calculated   10560404

GMTSMHCI  Calculated   11062334

GMTSMHRF  Calculated    3664137

GMTSMHTC  Calculated      56951

GMTSPI99  Calculated   27352766

5 Routines checked, 0 failed.

PACKAGE: TIU*1.0*260     1

-------------------------------------------------------------------------------

TIULO1    Calculated   20992898

TIUPI260  Calculated    4988159

2 Routines checked, 0 failed.

PACKAGE: PXRM*2.0*18

-------------------------------------------------------------------------------

PXRM      Calculated   34618632

PXRMBMI   Calculated   15288671

PXRMCDEF  Calculated    2105486

PXRMCDUE  Calculated   41810574

PXRMCF    Calculated   54030816

PXRMCLST  Calculated   23383800

PXRMCSD   Calculated   79166791

PXRMCSTX  Calculated   33730668

PXRMDATE  Calculated   67839072

PXRMDEV   Calculated   28252558

PXRMDLL   Calculated  110071468

PXRMDLLA  Calculated   80062265

PXRMDLRP  Calculated   90356438

PXRMDNVA  Calculated    6248881

PXRMDRUG  Calculated   62235689

PXRMENOD  Calculated   20293476

PXRMERRH  Calculated   20920805

PXRMEUT   Calculated   48589168

PXRMEVFI  Calculated   10519647

PXRMEXFI  Calculated   53336583

PXRMEXHF  Calculated   46895809

PXRMEXIC  Calculated   79443458

PXRMEXIU  Calculated   65964028

PXRMEXPD  Calculated  193477804

PXRMEXPS  Calculated  186693422

PXRMEXSI  Calculated   38179497

PXRMEXU0  Calculated    6669231

PXRMEXU5  Calculated   37340412

PXRMFF    Calculated   39772882

PXRMFF0   Calculated   16903444

PXRMFFAT  Calculated    1990669

PXRMFFDB  Calculated   67646936

PXRMFFH   Calculated    8850687

PXRMFRPT  Calculated  109052864

PXRMHF    Calculated   40695055

PXRMICHK  Calculated  126620696

PXRMINDX  Calculated   36208748

PXRMINTR  Calculated   38456694

PXRMLDR   Calculated   20371554

PXRMLEX   Calculated   13035630

PXRMLOCF  Calculated   95480822

PXRMLOCL  Calculated   26781951

PXRMLOG   Calculated   61916340

PXRMLOGX  Calculated   66338920

PXRMMATH  Calculated    1055537

PXRMMSG   Calculated    1586253

PXRMMST   Calculated   74769587

PXRMOUTU  Calculated   15123879

PXRMP18E  Calculated    7271326

PXRMP18I  Calculated   53411935

PXRMPCMM  Calculated    8447638

PXRMPDEM  Calculated   63031342

PXRMPDRP  Calculated   99170461

PXRMPDRS  Calculated   66950480

PXRMPLST  Calculated   53881985

PXRMPRF   Calculated   14561968

PXRMPSN   Calculated   29549599

PXRMPTD2  Calculated    5119289

PXRMPTL   Calculated   36712533

PXRMRDI   Calculated   38535158

PXRMREDT  Calculated   70692621

PXRMSEL1  Calculated   46693402

PXRMSTAC  Calculated   10361634

PXRMSTS   Calculated  177106484

PXRMTAX   Calculated   65705767

PXRMTERM  Calculated   55250159

PXRMUTIL  Calculated   90350759

PXRMVITL  Calculated   14733842

PXRMVLST  Calculated   47316348

PXRMVSIT  Calculated   10620425

PXRMXDT1  Calculated   70086449

71 Routines checked, 0 failed.

### 7 Print Transport Global (optional)

This option will allow you to view the components of the KIDS build.

### 8 Install the build.  (See an example of the install in Appendix A)

**NOTE: DO NOT QUEUE THE INSTALLATION** , because this installation asks questions requiring responses and queuing will stop the installation. A Reminders Manager or CAC should be present to respond to these.

From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s).  Select the build HIGH RISK MH 1.0 .KID and proceed with the install.  If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

Select Installation &amp; Distribution System Option: **Installation**

Select Installation Option: **INSTALL PACKAGE(S)**

Select INSTALL NAME: HIGH RISK MH 1.0

Answer "NO" to the following prompts:

Want KIDS to INHIBIT LOGONs during install? NO// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

**Example of questions asked during install:**

Checking Install for Package SD*5.3*578

Install Questions for SD*5.3*578

Incoming Mail Groups:

Enter the Coordinator for Mail Group 'SD MH NO SHOW NOTIFICATION': XXXXX,XXX

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Checking Install for Package DG*5.3*836

Install Questions for DG*5.3*836

Do you want to update the Parameter Definition for the local Patient Record Flag

related to HIGH RISK FOR SUICIDE at this time? YES//

Enter the Local Patient Record Flag that you are using as your "High Risk

for Suicide" flag.  If not already defined use the Directive

recommendation: HIGH RISK FOR SUICIDE. If already defined use your current

flag name.

Recommended Flag: HIGH RISK FOR SUICIDE  Replace

**Installation Example**

See Appendix A.

### 9 Install File Print

Use the KIDS Install File Print option to print out the results of the installation process. You can select the multi-package build or any of the individual builds included in the multi-package build.

Select Utilities Option: **Install** File Print

Select INSTALL NAME: HIGH RISK MH 1.0


### 10 Build File Print

Use the KIDS Build File Print option to print out the build components.

Select Utilities Option:  Build File Print

Select BUILD NAME: HIGH RISK MH **1.0**

DEVICE: HOME//

### 11 Post-installation routines

The installation will place the following exchange file entries in the Reminder Exchange file #811.8:

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

NATIONAL BLOOD PRESSURE CONDITION CHANGES

The contents of NATIONAL BLOOD PRESSURE CONDITION CHANGES are described in the Systolic/Mean/Diastolic discussion in the Release Notes.

VA-MH NO SHOW APPT CLINICS LL

The VA-MH NO SHOW APPT CLINICS LL location list includes clinic stop codes for MH clinics that are scheduled for face-to-face appointments.

The post-install routine will install all the components of these Exchange file entries on your system. After the installation has finished, if you discover that any of these components weren’t installed correctly, you can use the Reminder Exchange option on the Reminders Manager Menu to install them.

**Health Summary**

The GMTS*2.7*99 post-install routine will create stub entries in file #142 for the  remote Health Summary Type, and then call the silent Reminder Exchange  install utility to install the remaining Health Summary items.  Lastly, POST will re-index the HEALTH SUMMARY TYPE and HEALTH SUMMARY COMPONENT files along with rebuilding the Ad Hoc Health Summary.

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

### 12 Deletion of init routines

After everything has been successfully installed you may delete the following init routines:  PXRMP18E, PXRMP18I

## Post-Install Set-up Instructions

**1.   Enter names to mail group**

Enter the names of Suicide Prevention Coordinators and/or other MH professionals responsible for coordinating follow-up of High Risk for Suicide patients that miss a MH appointment.  The mail group owner of the SD MH NO SHOW NOTIFICATION mail group (as entered during the installation process) will need to add these names after the multi-package build is installed. The mail group members added to this mail group will receive the new Scheduling report results (from the nightly background job) in a MailMan Message. This can include all facility SPCs if you’re an integrated site.

**Example:**

&gt;D ^XUP

Setting up programmer environment

This is a TEST account.

Select OPTION NAME: **XMMGR**

Manage Mailman     menu

Check MailMan Files for Errors

Create a Mailbox for a user

Disk Space Management ...

Group/Distribution Management ...

Local Delivery Management ...

MailMan Site Parameters

Network Management ...

New Features for Managing MailMan

Select Manage Mailman Option: **Group/Distribution Management** ... [XMMGR-GROUP-MAINTENANCE]

Select Group/Distribution Management Option: Mail **Group Coordinator's Edit** [XMMGR-MAIL-GRP-COORDINATOR]

This option allows a mail group coordinator to edit the mail groups that

he or she is the coordinator of (and no others).  It does not allow edit

of remote recipients.

Select MAIL GROUP NAME: SD MH NO SHOW NOTIFICATION

Select MEMBER: MHUSER,TWO

Are you adding 'MHUSER,TWO' as a new MEMBER (the 1ST for this MAIL GROUP)? No// **YES**

Select MEMBER: MHUSER,THREE

1. **Assign report options**

Assign these report options to the primary or secondary menu options of your Suicide Prevention Coordinators, Mental Health Treatment Coordinator, and other Mental Health Professionals who will be tracking missed appointments for high risk for suicide patients:

- SD MH NO SHOW AD HOC REPORT
    - Scheduling Mental Health AD HOC NO SHOW Report
- SD MH NO SHOW NIGHTLY BGJ
    - No Show Nightly Background Job   (tasked job)

1. **Add the new health summary types to the CPRS Reports tab display**

Follow your facility’s rules and conventions for adding these health summary types.

1. VA-MH HIGH RISK PATIENT - This Type contains the four Health Summary Components mentioned above, and is the basis for creating the VA-MH HIGH RISK PATIENT (TIU) Health Summary Object.
2. REMOTE MH HIGH RISK PATIENT - This Type contains the same components as the VA-MH HIGH RISK PATIENT and allows viewing the aforementioned information from remote sites.

Sequencing new Health Summary types is done in the GUI Parameters option.

**Example**

Select CPRS Manager Menu Option: **PE** CPRS Configuration (Clin Coord)

Select CPRS Configuration (Clin Coord) Option: **GP** GUI Parameters

Select GUI Parameters Option: **HS** GUI Health Summary Types

Allowable Health Summary Types may be set for the following:

2   User          USR    [choose from NEW PERSON]

3   Division      DIV    [choose from INSTITUTION]

4   System        SYS    [TEST.FO-SLC.MED.VA.GOV]

5   Service       SVC    [choose from SERVICE/SECTION]

Enter selection: **4** System   xxx.MED.VA.GOV

- Setting Allowable Health Summary Types  for System: PUGET-SOUND.MED.VA.GOV -

Sequence: 20//

Health Summary: VA-HIGH RISK MH PATIENT

Sequence: 21//                (your sequence numbers will be different)

Health Summary: REMOTE MH HIGH RISK PATIENT

1. **Assign the High Risk MH No-Show Follow-up reminder to users’ coversheets, following local policies.**

**Edit Cover Sheet Reminder List Example**

1. **If necessary, edit the Parameter Definition for the PRF FOR SUCIDE PREVENTION.** If your site has a different name for this PRF, you’ll need to go into the Parameter Tools option (XPAR MENU TOOLS) to change this. NOTE: You may need programmer access to use this option.

Select General Parameter Tools Option: EP  Edit Parameter Values

--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: PRF FOR SUICIDE PREVENTION  DGPF SUICIDE FLAG

PRF for Suicide Prevention

------------ Setting DGPF SUICIDE FLAG  for Package: REGISTRATION ------------

Value: HIGH RISK FOR SUICIDE  Replace

1. Update the reminder term with the name of the local PRF flag, after setting up the DG SUICIDE PREVENTION parameter.

---- Begin: VA-MH HIGH RISK FOR SUICIDE PRF (FI(2)=RT(811)) --------------

Finding Type: REMINDER TERM

Use in Patient Cohort Logic: AND

Beginning Date/Time: FIEVAL(1,1,"DATE")

Ending Date/Time: FIEVAL(1,1,"DATE")+1D

Mapped Findings: CF.VA-PATIENT RECORD FLAG

INFORMATION

Computed Finding Parameter: HIGH RISK FOR SUICIDE^L

---- End: VA-MH HIGH RISK FOR SUICIDE PRF --------------------------------

- Use the Reminder Term edit option (Reminder Manager’s Menu)
- Select the VA-MH HIGH RISK FOR SUICIDE PRF reminder term
- Select the Finding CF.VA-PATIENT RECORD FLAG INFORMATION
- Add local PRF name to Computed Finding Parameter followed by “^L”.
- Example:

Computed Finding Parameter: HIGH RISK FOR SUICIDE^L

1. If you are using $P in a Condition, we recommend that you replace it with the appropriate CSUBs. Several national definitions and terms were originally distributed with Conditions using $P; as part of this patch they will be updated to use the SYSTOLIC and DIASTOLIC CSUBs.

SYSTOLIC/MEAN/DIASTOLIC and use of CSUB instead of $P: The Clin4 support team pointed out that the value for blood pressure can come back in either of the following forms: SYSTOLIC/DIASTOLIC or SYSTOLIC/MEAN/DIASTOLIC ( the second form is not very common). If the second form comes back, then the DIASTOLIC CSUB would have the value for mean, and if $P was used in a Condition, it would also be the mean. The code was changed so that the DIASTOLIC CSUB will always have the correct value.

1. Add back locally mapped findings if they were removed. As stated in Pre-Installation instructions, the reminder term VA-MHV INFLUENZA IMMUNIZATION was installed with the overwrite action, which means that all locally mapped findings were removed. Therefore, prior to the installation, you were advised to use the “Inquire about Reminder Term” option to check this term and verify that it was mapped with your local findings.  If there are no mapped local findings, then after this install, add proper local mappings to complete this reminder term’s definition After the installation, the term will have a single mapped finding which will look similar to this:

Finding Item: INFLUENZA, HIGH DOSE SEASONAL, PRESERV-FREE

(FI(1)=IM(612013))

Finding Type: IMMUNIZATION

Beginning Date/Time: 8/20/10

Use the saved term inquiry as a reference and add back the locally mapped findings that were removed.  Do not remove the mapped finding that was installed by the patch.

## Appendix A: Installation Example

NOTE: DO NOT QUEUE THE INSTALL!!

HIGH RISK MH 1.0    12/9/11@10:32:48

=&gt; High Risk Mental Health multi-package build, increment 1.  ;Created on

This Distribution was loaded on Dec 09, 2011@10:32:48 with header of

High Risk Mental Health multi-package build, increment 1.  ;Created on Dec 09

, 2011@08:20:31

It consisted of the following Install(s):

HIGH RISK MH 1.0     DG*5.3*836     SD*5.3*578    GMTS*2.7*99    TIU*1.0*260

PXRM*2.0*18

Checking Install for Package HIGH RISK MH 1.0

Install Questions for HIGH RISK MH 1.0

Checking Install for Package DG*5.3*836

**Install Questions for DG*5.3*836**

**Do you want to update the Parameter Definition for the local Patient Record Flag**

**related to HIGH RISK FOR SUICIDE at this time? YES// NO**

**Enter the Local Patient Record Flag that you are using as your "High Risk**

**for Suicide" flag.  If not already defined use the Directive**

**recommendation: HIGH RISK FOR SUICIDE. If already defined use your current**

**flag name.**

**Recommended Flag: HIGH RISK FOR SUICIDE  Replace**

**Example:** HIGH RISK FOR SUICIDE^L   ( *^L indicates that it’s a local PRF name.)*

**Checking Install for Package SD*5.3*578**

**Install Questions for SD*5.3*578**

**Incoming Mail Groups:**

**Enter the Coordinator for Mail Group 'SD MH NO SHOW NOTIFICATION': CRUSER,ONE//      OC        OI&amp;T STAFF**

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Checking Install for Package GMTS*2.7*99

Will first run the Environment Check Routine, GMTSPI99

GMTS*2.7*99 has been previously installed.  Environment check complete.

Install Questions for GMTS*2.7*99

Incoming Files:

811.8     REMINDER EXCHANGE  (including data)

Note:  You already have the 'REMINDER EXCHANGE' File.

I will OVERWRITE your data with mine.

Checking Install for Package TIU*1.0*260

Install Questions for TIU*1.0*260

Checking Install for Package PXRM*2.0*18

Install Questions for PXRM*2.0*18

Incoming Files:

801.41    REMINDER DIALOG

Note:  You already have the 'REMINDER DIALOG' File.

802.4     REMINDER FUNCTION FINDING FUNCTIONS  (including data)

Note:  You already have the 'REMINDER FUNCTION FINDING FUNCTIONS' File.

I will OVERWRITE your data with mine.

811.4     REMINDER COMPUTED FINDINGS  (including data)

Note:  You already have the 'REMINDER COMPUTED FINDINGS' File.

I will OVERWRITE your data with mine.

811.5     REMINDER TERM  (Partial Definition)

Note:  You already have the 'REMINDER TERM' File.

811.6     REMINDER SPONSOR

Note:  You already have the 'REMINDER SPONSOR' File.

811.7     REMINDER CATEGORY  (Partial Definition)

Note:  You already have the 'REMINDER CATEGORY' File.

811.8     REMINDER EXCHANGE  (including data)

Note:  You already have the 'REMINDER EXCHANGE' File.

I will OVERWRITE your data with mine.

811.9     REMINDER DEFINITION

Note:  You already have the 'REMINDER DEFINITION' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

**DO NOT QUEUE THIS INSTALL!!**

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME//   TCP

Install Started for HIGH RISK MH 1.0 :

Build Distribution Date: Dec 09, 2011

Installing Routines:

Feb 15, 2012@18:20:26

Install Started for DG*5.3*836 :

Feb 15, 2012@18:20:26

Build Distribution Date: Dec 09, 2011

Installing Routines:

Feb 15, 2012@18:20:26

Installing PACKAGE COMPONENTS:

Installing PARAMETER DEFINITION

Feb 15, 2012@18:20:26

Running Post-Install Routine: POST^DG53836P

Updating Parameters File...

Updating Routine file...

Updating KIDS files...

DG*5.3*836 Installed.

Feb 15, 2012@18:20:26

Not a production UCI

NO Install Message sent

Install Started for SD*5.3*578 :

Feb 15, 2012@18:20:26

Build Distribution Date: Dec 09, 2011

Installing Routines:

Feb 15, 2012@18:20:26

Installing PACKAGE COMPONENTS:

Installing MAIL GROUP

Installing OPTION

Feb 15, 2012@18:20:26

Updating Routine file...

Updating KIDS files...

SD*5.3*578 Installed.

Feb 15, 2012@18:20:26

Not a production UCI

NO Install Message sent

Install Started for GMTS*2.7*99 :

Feb 15, 2012@18:20:26

Build Distribution Date: Dec 09, 2011

Installing Routines:

Feb 15, 2012@18:20:26

Running Pre-Install Routine: PRE^GMTSPI99

Cleaning up any previous versions of Reminder Exchange file entry

Cleaning up any previous test versions of Health Summary Components

Cleaning up any previous versions of Health Summary Types

Re-index and rebuild after housekeeping

Re-Indexing Health Summary Component file ................ &lt; done &gt;

Re-Indexing Health Summary Type file ..................... &lt; done &gt;

Ad Hoc Summary

Gathering Ad Hoc Summary information.................... &lt; done &gt;

Purging old Ad Hoc Summary.............................. &lt; done &gt;

Rebuilding Ad Hoc Summary............................... &lt; done &gt;

Ad Hoc Health Summary successfully rebuilt

Installing Data Dictionaries:

Feb 15, 2012@18:20:29

Installing Data:

Feb 15, 2012@18:20:30

Running Post-Install Routine: POST^GMTSPI99

Creating stub entries for Health Summary Types.

Installing Health Summary items and TIU/HS object.

1. Installing Reminder Exchange entry GMTS FOR HRMH

Re-index and rebuild after install

Re-Indexing Health Summary Component file ................ &lt; done &gt;

Re-Indexing Health Summary Type file ..................... &lt; done &gt;

Ad Hoc Summary

Gathering Ad Hoc Summary information.................... &lt; done &gt;

Purging old Ad Hoc Summary.............................. &lt; done &gt;

Rebuilding Ad Hoc Summary............................... &lt; done &gt;

Ad Hoc Health Summary successfully rebuilt

Updating Routine file...

Updating KIDS files...

GMTS*2.7*99 Installed.

Feb 15, 2012@18:20:33

Not a production UCI

NO Install Message sent

Install Started for TIU*1.0*260 :

Feb 15, 2012@18:20:33

Build Distribution Date: Dec 09, 2011

Installing Routines:

Feb 15, 2012@18:20:33

Running Post-Install Routine: EN^TIUPI260

Creation of TIU Object MH MISSED APPOINTMENTS 10D successful...

Updating Routine file...

Updating KIDS files...

TIU*1.0*260 Installed.

Feb 15, 2012@18:20:34

Not a production UCI

NO Install Message sent

Install Started for PXRM*2.0*18 :

Feb 15, 2012@18:20:34

Build Distribution Date: Dec 09, 2011

Installing Routines:

Feb 15, 2012@18:20:35

Running Pre-Install Routine: PRE^PXRMP18I

DISABLE options.

DISABLE protocols.

Removing old data dictionaries.

Deleting data dictionary for file # 801.41

Deleting data dictionary for file # 802.4

Deleting data dictionary for file # 811.4

Deleting data dictionary for file # 811.6

Deleting data dictionary for file # 811.9

Installing Data Dictionaries:

Feb 15, 2012@18:20:37

Installing Data:

Feb 15, 2012@18:20:41

Installing PACKAGE COMPONENTS:

Installing INPUT TEMPLATE

Installing OPTION

Feb 15, 2012@18:20:41

Running Post-Install Routine: POST^PXRMP18I

Rebuilding Custom Date Due data structures.

ENABLE options.

ENABLE protocols.

Rebuilding Sponsor B and BN indexes.

There are 13 Reminder Exchange entries to be installed.

1. Installing Reminder Exchange entry NATIONAL BLOOD PRESSURE CHANGES

2. Installing Reminder Exchange entry VA-MH NO SHOW APPT CLINICS LL

3. Installing Reminder Exchange entry VA-INFLUENZA 2010 UPDATES

4. Installing Reminder Exchange entry VA-TEXT INFO SCREEN FOR AAA (RD)

5. Installing Reminder Exchange entry VA MH SCREENING REMINDERS UPDATE

6. Installing Reminder Exchange entry VA-EMBEDDED FRAGMENTS RISK EVALUATION

7. Installing Reminder Exchange entry VA BRANCHING LOGIC REMINDER UPDATES

OEF/OIF

8. Installing Reminder Exchange entry VA-INFLUENZA H1N1 UPDATE

9. Installing Reminder Exchange entry VA-MHV INFLUENZA VACCINE

10. Installing Reminder Exchange entry VA-ALCOHOL F/U POS AUDIT-C

11. Installing Reminder Exchange entry VA-MH HIGH RISK NO-SHOW FOLLOW-UP

12. Installing Reminder Exchange entry VA-TB/POSITIVE PPD

13. Installing Reminder Exchange entry VA-PATIENT RECORD FLAG INFORMATION

Checking national computed finding print names.

CF VA-ADMISSIONS FOR A DATE RANGE

Print Name: Admissions for a Date Range

New print Name: VA-Admissions for a Date Range

CF VA-AGE

Print Name: Patient Age

New print Name: VA-Patient Age

CF VA-ALLERGY

Print Name: Allergy

New print Name: VA-Allergy

CF VA-BMI

Print Name: Body Mass Index

New print Name: VA-Body Mass Index

CF VA-BSA

Print Name: Body Surface Area

New print Name: VA-Body Surface Area

CF VA-CURRENT INPATIENTS

Print Name: Current Inpatients

New print Name: VA-Current Inpatients

CF VA-DATE OF BIRTH

Print Name: Patient's Date of Birth

New print Name: VA-Patient's Date of Birth

CF VA-DATE OF DEATH

Print Name: Patient's Date of Death

New print Name: VA-Patient's Date of Death

CF VA-DISCHARGE DATE

Print Name: Veteran Last Separation Date

New print Name: VA-Veteran Last Separation Date

CF VA-DISCHARGES FOR A DATE RANGE

Print Name: Discharges for a Date Range

New print Name: VA-Discharges for a Date Range

CF VA-ETHNICITY

Print Name: Patient's Ethnicity

New print Name: VA-Patient's Ethnicity

CF VA-IS INPATIENT

Print Name: Is Inpatient

New print Name: VA-Is Inpatient

CF VA-LAST SERVICE SEPARATION DATE

Print Name: Veteran Last Separation Date

New print Name: VA-Veteran Last Separation Date

CF VA-MST STATUS

Print Name: MST Status

New print Name: VA-MST Status

CF VA-PATIENT TYPE

Print Name: PATIENT TYPE

New print Name: VA-Patient Type

CF VA-PATIENTS WITH APPOINTMENTS

Print Name: Patients with Appointments

New print Name: VA-Patients with Appointments

CF VA-PRIMARY CARE PROVIDER

Print Name: PCMM Primary Care Provider

New print Name: VA-PCMM Primary Care Provider

CF VA-PRIMARY CARE TEAM

Print Name: PCMM Primary Care Team

New print Name: VA-PCMM Primary Care Team

CF VA-PROGRESS NOTE

Print Name: Progress Note

New print Name: VA-Progress Note

CF VA-PTF HOSPITAL DISCHARGE DATE

Print Name: PTF Hospital Discharge Date

New print Name: VA-PTF Hospital Discharge Date

CF VA-RACE 2003

Print Name: Patient's Race, 2003 and On.

New print Name: VA-Patient's Race, 2003 and On.

CF VA-RACE PRE 2003

Print Name: Patient's pre-2003 Race

New print Name: VA-Patient's pre-2003 Race

CF VA-REMINDER DEFINITION

Print Name: Reminder Definition Computed Finding

New print Name: VA-Reminder Definition Computed Finding

CF VA-TREATING FACILITY LIST

Print Name: Treating FaciLity list

New print Name: VA-Treating Facility List

CF VA-VETERAN

Print Name: Patient is a Veteran

New print Name: VA-Patient is a Veteran

CF VA-WH MAMMOGRAM ABNORMAL IN WH PKG

Print Name:

New print Name: VA-WH Mammogram Abnormal in WH pkg

CF VA-WH MAMMOGRAM IN WH PKG

Print Name: Mammogram in WH pkg

New print Name: VA-Mammogram in WH pkg

CF VA-WH PAP SMEAR ABNORMAL IN WH PKG

Print Name:

New print Name: VA-WH Pap Smear Abnormal in WH pkg

CF VA-WH PAP SMEAR IN LAB PKG

Print Name: Lab Pap Smear SNOMED

New print Name: VA-Lab Pap Smear SNOMED

CF VA-WH PAP SMEAR IN WH PKG

Print Name: Pap Smear in WH pkg

New print Name: VA-Pap Smear in WH pkg

Setting CF PARAMETER REQUIRED field for national computed findings.

Updating Routine file...

Updating KIDS files...

PXRM*2.0*18 Installed.

Feb 15, 2012@18:27:53

Not a production UCI

NO Install Message sent

Updating Routine file...

Updating KIDS files...

HIGH RISK MH 1.0 Installed.

Feb 15, 2012@18:27:53

No link to PACKAGE file

PXRM*2.0*18                             
Install Completed

1      Load a Distribution

2      Verify Checksums in Transport Global

3      Print Transport Global

4      Compare Transport Global to Current System

5      Backup a Transport Global

6      Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option:

## Appendix B – Nightly Background Job and Ad Hoc Report Examples

This is a sample of the High Risk Mental Health NO Show Nightly Report.  This report is generated at the end of the Scheduling Nightly Background job, and will be sent in a Mailman message to those persons added to mail group SD MH NO SHOW NOTIFICATION. All persons in this mail group will receive the High Risk Mental Health NO SHOW report that is generated from the scheduling nightly background job. An option to manually run the no show background job if there was an error in running the report, has also been created called SD MH NO SHOW NIGHTLY BGJ  (High Risk MH No-Show Nightly Report).

The Background job will list the patients who had a status of “NO-SHOW,”  “NO SHOW WITH AUTO-REBOOK,” and “No Action Taken” for the day before that have the patient record flag  ‘”High Risk for Mental Health.” It will list patients for all mental health clinics/stop codes that are defined in the Remote location list ‘VA-MH NO SHOW APPT CLINICS LL’. The VA-MH NO SHOW APPT CLINICS LL location list includes clinic stop codes for MH clinics that are scheduled for face-to-face appointments.

This report will list future scheduled appointments for 30 days in the future.

**This is how the report will display to the screen when reading mailman.**

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

HIGH RISK MENTAL HEALTH NO SHOW NIGHTLY REPORT                     PAGE    2

Enter RETURN to continue or '^' to exit:

Subj: HRMH NO SHOW NIGHTLY REPORT MESSAGE #  [#111884]   Page 3

-------------------------------------------------------------------------------

By CLINIC for Appointments on 4/5/11                      Run: 4/6/2011@11:56

#    PATIENT             PT ID     APPT D/T             CLINIC          STATUS

******************************************************************************

DIVISION/CLINIC/STOP CODE: TROY1/LIZ'S MENTAL HEALTH CLINIC/202

1    HRMHpatient,One     0001     4/5/2011 9:00 am     LIZ'S MENTAL HE *NSA

Future Scheduled Appointments:

4/7/2011 9:00 am          LIZ'S MENTAL HEALTH CLINIC

4/14/2011 9:00 am         LIZ'S MENTAL HEALTH CLINIC

4/17/2011 9:00 am         LIZ'S MENTAL HEALTH CLINIC

2    HRMHpatient,Two     0002     4/5/2011 3:00 pm     LIZ'S MENTAL HE *NSA

Future Scheduled Appointments:

4/14/2011 9:00 am         LIZ'S MENTAL HEALTH CLINIC

4/17/2011 9:00 am         LIZ'S MENTAL HEALTH CLINIC

3    HRMHpatient,Two     0002     4/5/2011 4:00 pm     LIZ'S MENTAL HE *NS

Enter RETURN to continue or '^' to exit:

Subj: HRMH NO SHOW NIGHTLY REPORT MESSAGE #  [#111884]   Page 4

-------------------------------------------------------------------------------

Future Scheduled Appointments:

4/14/2011 9:00 am         LIZ'S MENTAL HEALTH CLINIC

4/17/2011 9:00 am         LIZ'S MENTAL HEALTH CLINIC

4    HRMHpatient,Three   0003     4/5/2011 2:00 pm     LIZ'S MENTAL HE *NAT

Future Scheduled Appointments:

4/14/2011 9:30 am         LIZ'S MENTAL HEALTH CLINIC

4/18/2011 8:00 am         D-PSYCH

DIVISION/CLINIC/STOP CODE: TROY1/MENTAL HEALTH/188

1    HRMHpatient,One     0001     4/5/2011 8:00 am     MENTAL HEALTH   *NAT

Future Scheduled Appointments:

4/7/2011 9:00 am          LIZ'S MENTAL HEALTH CLINIC

4/14/2011 9:00 am         LIZ'S MENTAL HEALTH CLINIC

4/17/2011 9:00 am         LIZ'S MENTAL HEALTH CLINIC

2    HRMHpatient,Two     0002     4/5/2011 1:00 pm     MENTAL HEALTH   *NAT

Enter RETURN to continue or '^' to exit:

Subj: HRMH NO SHOW NIGHTLY REPORT MESSAGE #  [#111884]   Page 5

-------------------------------------------------------------------------------

Future Scheduled Appointments:

4/14/2011 9:00 am         LIZ'S MENTAL HEALTH CLINIC

4/17/2011 9:00 am         LIZ'S MENTAL HEALTH CLINIC

3    HRMHpatient,Three   0003     4/5/2011 11:00 am    MENTAL HEALTH   *NS

Future Scheduled Appointments:

4/14/2011 9:30 am         LIZ'S MENTAL HEALTH CLINIC

4/18/2011 8:00 am         D-PSYCH

**High Risk MH No-Show Ad hoc Report**

This option (SD MH NO SHOW AD HOC REPORT) will list by one, many or All stop codes or only Mental Health stop codes defined in the Reminder Location List file under the ‘VA-MH NO SHOW APPT CLINICS LL’ entry.

A series of prompts will be asked of the user to refine the report.

- The user will be asked to select a beginning and ending date:  this will list the report within a certain date range.

- The division will be asked of the user: The report can list by one, many or all divisions.

- The user will then be asked to choose how the report should sort: by (M)ental Health Quick List, which will list only those clinics defined in the Reminder Location list, or by (C)linics or (S)top codes both of which will further prompt the user to refine the sort. If ?, ?? is entered by the user, a help prompt will be displayed.

- If the user selects to sort by (S)top codes, a prompt asking them to select stop codes by listing (A)ll stop codes, (mental health as well as non mental health) or (M)ental Health stop codes only (that are defined in the Reminder Location List) and are stop codes in the divison/s chosen to list in this report. Both selections will allow the user to choose one, many, or all stop codes.

- A prompt asking the number of days in the future to list the future scheduled appointment is asked and will list the future scheduled appointments that many days in the future.

When the report displays or prints:

- The division/Stop Code Name – Name/Number will display on the report once for all patients who have no showed for that Stop Code and division.  It will display again, when the stop code or division changes.

- A total page will be displayed at the end of the report.

Special Note:  At the Select Stop Code prompt, the stop code may be selected by the stop code file number (as example, selecting 188 below) or by the AMIS Reporting stop code (500 – 599 code numbers).  An example of each is shown below.

**No Show displays for (A)ll stop codes:**

Notice that when the user is prompted Select Stop codes: ALL//, if the user enters ??, the prompt displays all stop codes for mental health that are associated with the stop codes listed in the Reminder Location List VA-MH NO SHOW APPT CLINICS LL and non mental health stop codes to select  (green highlight). The user can also hit return at that prompt and stop Codes for all stop codes will display.

DEVISC1A3:MNTVLL 16d3&gt;D ^XQ1

Select OPTION NAME:    SD MH NO SHOW AD HOC REPORT     High Risk MH No-Show Adoc Report

High Risk MH No-Show Adhoc Report

***************  High Risk Mental Health NO SHOW Adhoc Report ***************

Select Beginning Date: 11/10/11// T-15  (OCT 21, 2011)

Select    Ending Date: 11/10/11// T  (NOV 10, 2011)

Select division: ALL// ??

ENTER:

- Return for all divisions, or

- A division and return when all divisions have been selected--limit 20

Imprecise selections will yield an additional prompt.

(e.g. When a user enters 'A', all items beginning with 'A' are displayed.)

Choose from:

1            ALBANY     500

2            TROY1     500TA

3            OLD ALBANY     501

4            NEW TROY     500Z

5            ON THE HUDSON IN HISTORIC TROY     610

6            AUGUSTA VAMC, DOWNTOWN DIVISION     524

7            TROY2     500B

500          SATELLITE CLINIC     500BY

501          SATELLITE CLINIC1     501BY

502          TEST2     502A0

503          FACNEW     500FT

504          ?BAD, ONE     500BW

505          ALBANY2     500

506          TEST DIVISION     500

507          NEW TEST     507ER

539          CINC     539

540          MARCIA'S TEST DIVISION 5009AA     9005AA

541          ALB-PRRTP     500PA

542          NORM'S NURSING HOME     5009AB

^

Select division: ALL//

Sort report by (M)ental Health Clinic Quick List,(C)linic or (S)top Code: M//?

Enter: 'M' to run the report using the face-to-face Mental Health clinics

defined in the 'VA-MH NO SHOW APPT CLINICS LL' Reminder Location List

- with no additional prompts to refine the list of Mental Health clinics.

Enter: 'C' to run the report by clinics which will then prompt

to refine the list of clinics to use.

Enter: 'S' to run the report by stop codes which will then prompt

to refine the list of stop codes to use.

Sort report by (M)ental Health Clinic Quick List,(C)linic or (S)top Code: M//S

Stop Code Selection:

A  All Stop Codes

M  Mental Health Stop Codes only

Select: (A)ll Stop Codes  A//?

Enter:  'A' for All Stop Codes

'M' for Mental Health Stop Codes only

Select: (A)ll Stop Codes  A//

Select Stop codes: ALL// ??

ENTER:

- Return for all Stop codes, or

- A Stop codes and return when all Stop codes have been selected--limit 20

Imprecise selections will yield an additional prompt.

(e.g. When a user enters 'A', all items beginning with 'A' are displayed.)

Choose from:

1            EMERGENCY UNIT     1     10-01-1987

3            MENTAL HYGIENE(INDIV.)     83     10-01-1987

4            MENTAL HYGIENE(GROUP)     77     10-01-1987

5            DAY TREATMENT CENTER     78     10-01-1987

6            DAY HOSPITAL     79     10-01-1987

7            DRUG DEPENDENCE     80     10-01-1987

8            ALCOHOL TREATMENT     81     10-01-1987

9            PSYCHIATRY     84     10-01-1987

10           PSYCHOLOGY     85     10-01-1987

11           NEUROBEHAVIORAL     86     10-01-1987

13           GENERAL MEDICAL     27     10-01-1987

14           ALLERGY IMMUNOLOGY     28     10-01-1987

15           CARDIOLOGY     29     10-01-1987

16           DERMATOLOGY     30     10-01-1987

17           ENDO/METAB(EXCEPT DIAB.)     31     10-01-1987

18           DIABETES     32     10-01-1987

19           GASTROENTEROLOGY     33     10-01-1987

20           HEMATOLOGY     34     10-01-1987

21           HYPERTENSION     35     10-01-1987

'^' TO STOP:

Select Stop codes: ALL//

Select Number of days to List Future Appointments: 30//?

Enter a number of days from 1 to 90. Future scheduled appointments

for the patients will list that number of days in the future

on the No Show report.

Select Number of days to List Future Appointments: 30//

This output requires 80 column output

Select Device: 0;80;9999  UCX/TELNET

...HMMM, THIS MAY TAKE A FEW MOMENTS...

HIGH RISK MENTAL HEALTH NO SHOW ADHOC REPORT BY                       PAGE 1

STOP CODES for Appointments 10/26/11-11/10/11           Run: 11/10/2011@10:16

PATIENT                PT ID     APPT D/T            CLINIC              STATUS

******************************************************************************

DIVISION/STOP/CLINIC: ALBANY/141/GEN MED

1  HRMHpatient,One	 0001      10/31/2011 11:00 am GEN MED             *NAT

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

2  HRMHpatient,Two	 0002      10/31/2011 10:00 am D-PSYCH             *NAT

Home: (518)518-5181

Cell: (555)888-9999

Emergency Contact:

E-Cont.: HRMHecontact,Two

MHTC:

Future Scheduled Appointments:

11/14/2011 8:00 am        DERMATOLOGY

11/14/2011 8:30 am        PSYCH CLINIC

11/21/2011 8:00 am        DERMATOLOGY

11/21/2011 9:00 am        D-PSYCH

Results:

DIVISION/STOP/CLINIC: ALBANY/195/PSYCH CLINIC

1  HRMHpatient,One 	 0001      10/26/2011 9:00 am  PSYCH CLINIC        *NAT

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

2  HRMHpatient,Two	 0002      11/1/2011 8:00 am   PSYCH CLINIC        *NSA

Home: (518)518-5181

Cell: (555)888-9999

Emergency Contact:

E-Cont.: HRMHecontact,Two

MHTC:

Future Scheduled Appointments:

11/14/2011 8:00 am        DERMATOLOGY

11/14/2011 8:30 am        PSYCH CLINIC

11/21/2011 8:00 am        DERMATOLOGY

11/21/2011 9:00 am        D-PSYCH

Results:

HIGH RISK MENTAL HEALTH NO SHOW ADHOC REPORT BY                       PAGE 2

STOP CODES for Appointments 10/26/11-11/10/11           Run: 11/10/2011@10:16

PATIENT                PT ID     APPT D/T            CLINIC              STATUS

******************************************************************************

DIVISION/STOP/CLINIC: ON THE HUDSON IN HISTORI/202/LIZ'S MENTAL HEALTH CLINIC

1  HRMHpatient,One	 0001      11/4/2011 8:00 am   LIZ'S MENTAL HE     *NAT

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

2  HRMHpatient,Two	 0002      11/7/2011 8:00 am   LIZ'S MENTAL HE     *NAT

Home: (518)518-5181

Cell: (555)888-9999

Emergency Contact:

E-Cont.: HRMHecontact,Two

MHTC:

Future Scheduled Appointments:

11/14/2011 8:00 am        DERMATOLOGY

11/14/2011 8:30 am        PSYCH CLINIC

11/21/2011 8:00 am        DERMATOLOGY

11/21/2011 9:00 am        D-PSYCH

Results:

HIGH RISK MENTAL HEALTH NO SHOW ADHOC REPORT BY                       PAGE 3

STOP CODES for Appointments 10/26/11-11/10/11           Run: 11/10/2011@10:16

PATIENT                PT ID     APPT D/T            CLINIC              STATUS

******************************************************************************

DIVISION/STOP/CLINIC: TROY1/144/DERMATOLOGY

1  HRMHpatient,One	 0001      10/26/2011 8:00 am  DERMATOLOGY         *NAT

Home: (518)518-5181

Cell: (555)888-9999

Emergency Contact:

E-Cont.: HRMHecontact,One

Provider:  HRMHprovider,One

MHTC:

Future Scheduled Appointments:

11/14/2011 8:00 am        DERMATOLOGY

11/14/2011 8:30 am        PSYCH CLINIC

11/21/2011 8:00 am        DERMATOLOGY

11/21/2011 9:00 am        D-PSYCH

Results:

2  HRMHpatient,Two	 0002      10/31/2011 8:00 am  DERMATOLOGY         *NAT

Home: (518)518-5181

Cell: (555)888-9999

Emergency Contact:

E-Cont.: HRMHecontact,Two

Provider:  HRMHprovider,Two     MHTC:

Future Scheduled Appointments:

11/14/2011 8:00 am        DERMATOLOGY

11/14/2011 8:30 am        PSYCH CLINIC

11/21/2011 8:00 am        DERMATOLOGY

11/21/2011 9:00 am        D-PSYCH

Results:

HIGH RISK MENTAL HEALTH NO SHOW ADHOC REPORT BY                       PAGE 4

STOP CODES for Appointments 10/26/11-11/10/11           Run: 11/10/2011@10:16

Totals Page

******************************************************************************

Division/Clinic Appointment Totals

Division/CLinic                                                          Unique

NS   NSA   NAT  Patients

ALBANY/D-PSYCH                                           0     0     2      2

ALBANY/GEN MED                                           0     0     1      2

ALBANY/PSYCH CLINIC                                      0     1     1      2

ON THE HUDSON IN HISTORI/LIZ'S MENTAL HEALTH CLINIC      0     0     2      2

TROY1/DERMATOLOGY                                        0     0     2      2

*STATUS: NS = No Show      NSA = No Show Auto Rebook     NAT = No Action Taken

DEVISC1A3:MNTVLL 16d3&gt;

#### Ad Hoc No Show Report by Mental Health Only Stop Code Example

This is an example of how the No Show displays for (M)ental Health only stop codes.  Notice when the user is prompted Select Stop codes: ALL//, if the user enters ??, the prompt displays all stop codes for only mental health stop codes that are associated with the stop codes listed in the Reminder Location List VA-MH NO SHOW APPT CLINICS LL will be listed for the user to select  (green highlight). The user can choose one or many stop codes or the user can also hit return at that prompt and stop codes for all mental health stop codes will display that had no showed patients with Patient Record flag, High Risk for Suicide.

DEVISC1A3:MNTVLL 16d3&gt;D ^XQ1

Select OPTION NAME:    SD MH NO SHOW AD HOC REPORT     High Risk MH No-Show Ado

c Report

High Risk MH No-Show Adhoc Report

***************  High Risk Mental Health NO SHOW Adhoc Report ***************

Select Beginning Date: 11/10/11// T-15  (OCT 26, 2011)

Select    Ending Date: 11/10/11// T  (NOV 10, 2011)

Select division: ALL//

Sort report by (M)ental Health Clinic Quick List,(C)linic or (S)top Code: M//S

Stop Code Selection:

A  All Stop Codes

M  Mental Health Stop Codes only

Select: (A)ll Stop Codes  A//M

Select Stop codes: ALL// ??

ENTER:

- Return for all Stop codes, or

- A Stop codes and return when all Stop codes have been selected--limit 20

Imprecise selections will yield an additional prompt.

(e.g. When a user enters 'A', all items beginning with 'A' are displayed.)

Choose from:

188          MENTAL HEALTH CLINIC - IND     502

189          MH RESIDENTIAL CARE IND     503

191          DAY TREATMENT-INDIVIDUAL     505

192          DAY HOSPITAL-INDIVIDUAL     506

195          PSYCHIATRY - INDIVIDUAL     509

196          PSYCHOLOGY-INDIVIDUAL     510

198          MENTAL HEALTH CLINIC-GROUP     550

200          MHICM - INDIVIDUAL     552

201          DAY TREATMENT-GROUP     553

202          DAY HOSPITAL-GROUP     554

205          PSYCHIATRY - GROUP     557

206          PSYCHOLOGY-GROUP     558

207          PSYCHOSOCIAL REHAB - GROUP     559

208          SERV-MH GROUP     572

209          SERV-MH INDIVIDUAL     571

237          SUBSTANCE USE DISORDER IND     513

238          SUBSTANCE USE DISORDR GRP     560

247          PTSD CLINICAL TEAM PTS IND     540

257          PTSD - GROUP     516

^

Select Stop codes: ALL// MENT

1   MENTAL HEALTH CLINIC - IND       502

2   MENTAL HEALTH CLINIC-GROUP       550

3   MENTAL HEALTH CONSULTATION       512

CHOOSE 1-3: 1  MENTAL HEALTH CLINIC - IND     502

Select another Stop codes: 195  PSYCHIATRY - INDIVIDUAL     509

...OK? Yes//   (Yes)

Select another Stop codes: 554  DAY HOSPITAL-GROUP     554

Select another Stop codes:

Select Number of days to List Future Appointments: 30//

This output requires 80 column output

Select Device: 0;80;99999  UCX/TELNET

...EXCUSE ME, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

HIGH RISK MENTAL HEALTH NO SHOW ADHOC REPORT BY                       PAGE 1

STOP CODES for Appointments 10/26/11-11/10/11           Run: 11/10/2011@12:05

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

2  HRMHpatient,Two	 0002      10/31/2011 10:00 am D-PSYCH             *NAT

Home: (518)518-5181

Cell: (555)888-9999

Emergency Contact:

E-Cont.: HRMHecontact,Two

MHTC:

Future Scheduled Appointments:

11/14/2011 8:00 am        DERMATOLOGY

11/14/2011 8:30 am        PSYCH CLINIC

11/21/2011 8:00 am        DERMATOLOGY

11/21/2011 9:00 am        D-PSYCH

Results:

DIVISION/STOP/CLINIC: ALBANY/195/PSYCH CLINIC

1  HRMHpatient,One	 0001      10/26/2011 9:00 am  PSYCH CLINIC        *NAT

Home: (518)518-5181

Cell: (555)888-9999

Emergency Contact:

E-Cont.: HRMHecontact,one

MHTC:

Future Scheduled Appointments:

11/14/2011 8:00 am        DERMATOLOGY

11/14/2011 8:30 am        PSYCH CLINIC

11/21/2011 8:00 am        DERMATOLOGY

11/21/2011 9:00 am        D-PSYCH

Results:

2  HRMHpatient,Two	 0002      11/1/2011 8:00 am   PSYCH CLINIC        *NSA

Home: (518)518-5181

Cell: (555)888-9999

Emergency Contact:

E-Cont.: HRMHecontact,Two

MHTC:

Future Scheduled Appointments:

11/14/2011 8:00 am        DERMATOLOGY

11/14/2011 8:30 am        PSYCH CLINIC

11/21/2011 8:00 am        DERMATOLOGY

11/21/2011 9:00 am        D-PSYCH

Results:

HIGH RISK MENTAL HEALTH NO SHOW ADHOC REPORT BY                       PAGE 2

STOP CODES for Appointments 10/26/11-11/10/11           Run: 11/10/2011@12:05

PATIENT                PT ID     APPT D/T            CLINIC              STATUS

******************************************************************************

DIVISION/STOP/CLINIC: ON THE HUDSON IN HISTORI/202/LIZ'S MENTAL HEALTH CLINIC

1  HRMHpatient,One	 0001      11/4/2011 8:00 am   LIZ'S MENTAL HE     *NAT

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

2  HRMHpatient,Two	0002      11/7/2011 8:00 am   LIZ'S MENTAL HE     *NAT

Home: (518)518-5181

Cell: (555)888-9999

Emergency Contact:

E-Cont.: HRMHecontact,Two

MHTC:

Future Scheduled Appointments:

11/14/2011 8:00 am        DERMATOLOGY

11/14/2011 8:30 am        PSYCH CLINIC

11/21/2011 8:00 am        DERMATOLOGY

11/21/2011 9:00 am        D-PSYCH

Results:

HIGH RISK MENTAL HEALTH NO SHOW ADHOC REPORT BY                       PAGE 3

STOP CODES for Appointments 10/26/11-11/10/11           Run: 11/10/2011@12:05

Totals Page

*****************************************************************************

Division/Clinic Appointment Totals

Division/CLinic                                                          Unique

NS   NSA   NAT  Patients

ALBANY/D-PSYCH                                           0     0     2      2

ALBANY/PSYCH CLINIC                                      0     1     1      2

ON THE HUDSON IN HISTORI/LIZ'S MENTAL HEALTH CLINIC      0     0     2      2

*STATUS: NS = No Show      NSA = No Show Auto Rebook     NAT = No Action Taken

#### Ad Hoc No Show Report by Mental Health Clinic

This is a sample of the High Risk Mental Health NO Show Ad Hoc report, (option SD MH NO SHOW AD HOC REPORT, that will list by one, many, All clinics or only Mental Health clinics defined in the Reminder Location List file under the ‘VA-MH NO SHOW APPT CLINICS LL’ entry.

A series of prompts will be asked of the user to refine the report.

- The user will be asked to select a beginning and ending date:  this will list the report within a certain date range.

- The division will be asked of the user: The report can list by one, many or all divisions.

- The user will then be asked to choose how the report should sort: by (M)ental Health Quick List, which will list only those clinics defined in the Reminder Location list, or by (C)linics or (S)top codes both of which will further prompt the user to refine the sort. If ?, ?? is entered by the user, a help prompt will be displayed.

- If the user selects to sort by clinic, a prompt asking them to select clinics by listing All clinics, (mental health as well as non mental health) or Mental Health clinics only (that are defined in the Reminder Location List) and are clinics in the divisions chosen to list in this report. Both selections will allow the user to choose one, many, or all clinics.

- A prompt asking the number of days in the future to list the future scheduled appointment is asked and will list the future scheduled appointments that many days in the future.

When the report displays or prints:

- The division/Clinic name will display on the report once for all patients who have no showed for that clinic and division.  It will display again, when the clinic or division changes.

- A totals page will be displayed at the end of the report.

#### Ad Hoc No Show Report for All Clinics

This is an example of how the No Show displays for All clinics.  Notice when the user selects (C)linics as the sort, the user is asked to select (A)ll or (M)ental Health clinics only.  If the user selects (A)ll and enters ?? at the list prompt, all mental health as well as non-mental health clinics can be selected, or if the user hits return, all clinics will be selected and will display on the report.

DEVISC1A3:MNTVLL&gt;D ^XQ1

Select OPTION NAME: SD MH NO SHOW AD HOC REPORT       High Risk MH No-Show Adhoc

Report

High Risk MH No-Show Adhoc Report

***************  High Risk Mental Health NO SHOW Adhoc Report ***************

Select Beginning Date: 11/09/11// T-10  (OCT 30, 2011)

Select    Ending Date: 11/09/11// T  (NOV 09, 2011)

Select division: ALL// ?

ENTER:

- Return for all divisions, or

- A division and return when all divisions have been selected--limit 20

Imprecise selections will yield an additional prompt.

(e.g. When a user enters 'A', all items beginning with 'A' are displayed.)

Answer with MEDICAL CENTER DIVISION NUM, or NAME, or FACILITY NUMBER, or

TREATING SPECIALTY

Do you want the entire 27-Entry MEDICAL CENTER DIVISION List? ?

Select division: ALL// ??

ENTER:

- Return for all divisions, or

- A division and return when all divisions have been selected--limit 20

Imprecise selections will yield an additional prompt.

(e.g. When a user enters 'A', all items beginning with 'A' are displayed.)

Choose from:

1            ALBANY     500

2            TROY1     500TA

3            OLD ALBANY     501

4            NEW TROY     500Z

5            ON THE HUDSON IN HISTORIC TROY     610

6            AUGUSTA VAMC, DOWNTOWN DIVISION     524

7            TROY2     500B

500          SATELLITE CLINIC     500BY

501          SATELLITE CLINIC1     501BY

502          TEST2     502A0

503          FACNEW     500FT

504          ?BAD, ONE     500BW

505          ALBANY2     500

506          TEST DIVISION     500

507          NEW TEST     507ER

539          CINC     539

540          MARCIA'S TEST DIVISION 5009AA     9005AA

541          ALB-PRRTP     500PA

542          NORM'S NURSING HOME     5009AB

^

Select division: ALL//

Sort report by (M)ental Health Clinic Quick List,(C)linic or (S)top Code: M//?

Enter: 'M' to run the report using the face-to-face Mental Health clinics

defined in the 'VA-MH NO SHOW APPT CLINICS LL' Reminder Location List

- with no additional prompts to refine the list of Mental Health clinics.

Enter: 'C' to run the report by clinics which will then prompt

to refine the list of clinics to use.

Enter: 'S' to run the report by stop codes which will then prompt

to refine the list of stop codes to use.

Sort report by (M)ental Health Clinic Quick List,(C)linic or (S)top Code: M//C

Clinic Selection:

A  All clinics

M Mental Health clinics only

Select: (A)ll clinics  A//?

Enter : 'A' for All clinics

'M' for Mental Health clinics only

Select: (A)ll clinics  A//

Select Clinic: ALL//??

ENTER:

- Return for all Clinics, or

- A Clinic and return when all Clinics have been selected--limit 20

Imprecise selections will yield an additional prompt.

(e.g. When a user enters 'A', all items beginning with 'A' are displayed.)

Choose from:

1            DERMATOLOGY

2            UROLOGY

3            PSYCHOLOGY

5            ONCOLOGY

6            AUTO DUMMY6

8            TEST22

9            PSYCHIATRY

10           DEMO

11           OLDSET

12           CHOW

13           ROYTEST

14           TST926

15           PULMONARY

16           RHEUMATOLOGY

17           ROY777

18           NEWDEMO

19           NUCLEAR MEDICINE

20           EYE           KAPLON,DENNIS

21           CHIROPRACTOR

'^' TO STOP:

Select: (A)ll clinics  A//

Select Number of days to List Future Appointments: 30//?

Enter a number of days from 1 to 90. Future scheduled appointments

for the patients will list that number of days in the future

on the No Show report.

Select Number of days to List Future Appointments: 30//20

This output requires 80 column output

Select Device: 0;80;9999  UCX/TELNET

...SORRY, I'M WORKING AS FAST AS I CAN...

HIGH RISK MENTAL HEALTH NO SHOW ADHOC REPORT BY                       PAGE 1

CLINICS for Appointments 10/20/11-11/9/11               Run: 11/9/2011@11:02

PATIENT                PT ID     APPT D/T            CLINIC              STATUS

******************************************************************************

DIVISION/CLINIC/STOP: ALBANY/D-PSYCH/188

1  HRMHpatient,One     0001      10/20/2011 10:00 am D-PSYCH             *NAT

Home: (518)XXX-XXXX

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

2  HRMHpatient,Two	 0002      10/25/2011 8:00 am  D-PSYCH             *NAT

Home: (518)518-5181

Cell: (555)888-9999

Emergency Contact:

E-Cont.: HRMHecontact,Two

MHTC:

Future Scheduled Appointments:

11/14/2011 8:00 am        DERMATOLOGY

11/14/2011 8:30 am        PSYCH CLINIC

11/21/2011 8:00 am        DERMATOLOGY

11/21/2011 9:00 am        D-PSYCH

Results:

3  HRMHpatient,Three 	 0003      10/31/2011 9:00 am  D-PSYCH             *NAT

Home: (518)518-5181

Cell: (555)888-9999

Emergency Contact:

E-Cont.: HRMHecontact,Three

MHTC:

Future Scheduled Appointments:

11/14/2011 8:00 am        DERMATOLOGY

11/14/2011 8:30 am        PSYCH CLINIC

11/21/2011 8:00 am        DERMATOLOGY

11/21/2011 9:00 am        D-PSYCH

Results:

4  HRMHpatient,Four      0004      10/31/2011 10:00 am D-PSYCH             *NAT

Home: (518)518-5181

Cell: (555)888-9999

Emergency Contact:

E-Cont.: HRMHecontact,Four

MHTC:

Future Scheduled Appointments:

11/14/2011 8:00 am        DERMATOLOGY

11/14/2011 8:30 am        PSYCH CLINIC

11/21/2011 8:00 am        DERMATOLOGY

11/21/2011 9:00 am        D-PSYCH

Results:

DIVISION/CLINIC/STOP: ALBANY/GEN MED/141

1  HRMHpatient,One      0001      10/31/2011 11:00 am GEN MED             *NAT

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

DIVISION/CLINIC/STOP: ALBANY/PSYCH CLINIC/195

1  HRMHpatient,One      0001      10/26/2011 9:00 am  PSYCH CLINIC        *NAT

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

2  HRMHPATIENT,Two      0002      11/1/2011 8:00 am   PSYCH CLINIC        *NSA

Home: (518)518-5181

Cell: (555)888-9999

Emergency Contact:

E-Cont.: HRMHecontact,Two

MHTC:

Future Scheduled Appointments:

11/14/2011 8:00 am        DERMATOLOGY

11/14/2011 8:30 am        PSYCH CLINIC

11/21/2011 8:00 am        DERMATOLOGY

11/21/2011 9:00 am        D-PSYCH

Results:

HIGH RISK MENTAL HEALTH NO SHOW ADHOC REPORT BY                       PAGE 2

CLINICS for Appointments 10/20/11-11/9/11               Run: 11/9/2011@11:02

PATIENT                PT ID     APPT D/T            CLINIC              STATUS

*****************************************************************************

DIVISION/CLINIC/STOP: ON THE HUDSON IN HISTORI/LIZ'S MENTAL HEALTH CLINIC/202

1  HRMHpatient,One     0001      11/4/2011 8:00 am   LIZ'S MENTAL HE     *NAT

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

2  HRMHpatient,Two     0002      11/7/2011 8:00 am   LIZ'S MENTAL HE     *NAT

Home: (518)518-5181

Cell: (555)888-9999

Emergency Contact:

E-Cont.: HRMHecontact,Two

MHTC:

Future Scheduled Appointments:

11/14/2011 8:00 am        DERMATOLOGY

11/14/2011 8:30 am        PSYCH CLINIC

11/21/2011 8:00 am        DERMATOLOGY

11/21/2011 9:00 am        D-PSYCH

Results:

HIGH RISK MENTAL HEALTH NO SHOW ADHOC REPORT BY                       PAGE 3

CLINICS for Appointments 10/20/11-11/9/11               Run: 11/9/2011@11:02

PATIENT                PT ID     APPT D/T            CLINIC              STATUS

******************************************************************************

DIVISION/CLINIC/STOP: TROY1/DERMATOLOGY/144

1  HRMHpatient,One     0001      10/20/2011 9:00 am  DERMATOLOGY         *NAT

Home: (518)518-5181

Cell: (555)888-9999

Emergency Contact:

E-Cont.: HRMHecontact,One

Provider:  HRMHprovider,One

MHTC:

Future Scheduled Appointments:

11/14/2011 8:00 am        DERMATOLOGY

11/14/2011 8:30 am        PSYCH CLINIC

11/21/2011 8:00 am        DERMATOLOGY

11/21/2011 9:00 am        D-PSYCH

Results:

2  HRMHpaitent,Two     0002      10/25/2011 10:00 am DERMATOLOGY         *NAT

Home: (518)518-5181

Cell: (555)888-9999

Emergency Contact:

E-Cont.: HRMHecontact,Two

Provider:  HRMHprovider,Two

MHTC:

Future Scheduled Appointments:

11/14/2011 8:00 am        DERMATOLOGY

11/14/2011 8:30 am        PSYCH CLINIC

11/21/2011 8:00 am        DERMATOLOGY

11/21/2011 9:00 am        D-PSYCH

Results:

3  HRMHpatient,Three   0003      10/26/2011 8:00 am  DERMATOLOGY         *NAT

Home: (518)518-5181

Cell: (555)888-9999

Emergency Contact:

E-Cont.: HRMHecontact,Three

Provider:  HRMHprovider,Three

MHTC:

Future Scheduled Appointments:

11/14/2011 8:00 am        DERMATOLOGY

11/14/2011 8:30 am        PSYCH CLINIC

11/21/2011 8:00 am        DERMATOLOGY

11/21/2011 9:00 am        D-PSYCH

Results:

4  HRMHpatient,Four    0004      10/31/2011 8:00 am  DERMATOLOGY         *NAT

Home: (518)518-5181

Cell: (555)888-9999

Emergency Contact:

E-Cont.: HRMHecontact,Four

Provider:  HRMHprovider,Four

MHTC:

Future Scheduled Appointments:

11/14/2011 8:00 am        DERMATOLOGY

11/14/2011 8:30 am        PSYCH CLINIC

11/21/2011 8:00 am        DERMATOLOGY

11/21/2011 9:00 am        D-PSYCH

Results:

HIGH RISK MENTAL HEALTH NO SHOW ADHOC REPORT BY                       PAGE 4

CLINICS for Appointments 10/20/11-11/9/11               Run: 11/9/2011@11:02

Totals Page

*****************************************************************************

Division/Clinic Appointment Totals

Division/CLinic                                                          Unique

NS   NSA   NAT  Patients

ALBANY/D-PSYCH                                           0     0     4      4

ALBANY/GEN MED                                           0     0     1      1

ALBANY/PSYCH CLINIC                                      0     1     1      1

ON THE HUDSON IN HISTORI/LIZ'S MENTAL HEALTH CLINIC      0     0     2      2

TROY1/DERMATOLOGY                                        0     0     4      4

*STATUS: NS = No Show      NSA = No Show Auto Rebook     NAT = No Action Taken

**(M)ental Health clinics only:**

Notice when the user selects Mental health only, the user can choose to list all mental health clinics or choose a number of clinics to list.

DEVISC1A3:MNTVLL 2d0&gt;D ^XQ1

Select OPTION NAME:    SD MH NO SHOW AD HOC REPORT     High Risk MH No-Show Adho

c Report

High Risk MH No-Show Adhoc Report

***************  High Risk Mental Health NO SHOW Adhoc Report ***************

Select Beginning Date: 11/09/11// T-10  (OCT 30, 2011)

Select    Ending Date: 11/09/11// T  (NOV 09, 2011)

Select division: ALL//

Sort report by (M)ental Health Clinic Quick List,(C)linic or (S)top Code: M//C

Clinic Selection:

A  All clinics

M Mental Health clinics only

Select: (A)ll clinics  A//M

Select Clinic: ALL// ??

ENTER:

- Return for all Clinics, or

- A Clinic and return when all Clinics have been selected--limit 20

Imprecise selections will yield an additional prompt.

(e.g. When a user enters 'A', all items beginning with 'A' are displayed.)

Choose from:

38           RESEARCH

41           PULLIT

47           MEDICINE SWO

48           LUNCH TIME LITTLE THEATRE

83           APPLE PIE

173          PROVIDENCE TEST X

425          PSYCH CLINIC

450          D-PSYCH

487          LIZ'S MENTAL HEALTH CLINIC

553          MARY'S CLINIC

566          JDS MIDNGHT

568          JDS 60 MIN

572          Eric Clinic II (Mental Health)

578          TEST-SMOKE

580          MENTAL HEALTH           MARKS,MARY

Select Clinic: ALL// D-PSYCH

Select another Clinic:

Select Number of days to List Future Appointments: 30//

This output requires 80 column output

Select Device: 0;80;9999  UCX/TELNET

...EXCUSE ME, JUST A MOMENT PLEASE...

HIGH RISK MENTAL HEALTH NO SHOW ADHOC REPORT BY                       PAGE 1

CLINICS for Appointments 10/30/11-11/9/11               Run: 11/9/2011@10:57

PATIENT                PT ID     APPT D/T            CLINIC              STATUS

*****************************************************************************

DIVISION/CLINIC/STOP: ALBANY/D-PSYCH/188

1  HRMHpatient,One     0001      10/31/2011 9:00 am  D-PSYCH             *NAT

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

2  HRMHpatient,Two     0002      10/31/2011 10:00 am D-PSYCH             *NAT

Home: (518)518-5181

Cell: (555)888-9999

Emergency Contact:

E-Cont.: HRMHecontact,Two

MHTC:

Future Scheduled Appointments:

11/14/2011 8:00 am        DERMATOLOGY

11/14/2011 8:30 am        PSYCH CLINIC

11/21/2011 8:00 am        DERMATOLOGY

11/21/2011 9:00 am        D-PSYCH

Results:

HIGH RISK MENTAL HEALTH NO SHOW ADHOC REPORT BY                       PAGE 2

CLINICS for Appointments 10/30/11-11/9/11               Run: 11/9/2011@10:57

Totals Page

*****************************************************************************

Division/Clinic Appointment Totals

Division/CLinic                                                          Unique

NS   NSA   NAT  Patients

ALBANY/D-PSYCH                                           0     0     2      2

*STATUS: NS = No Show      NSA = No Show Auto Rebook     NAT = No Action Taken

DEVISC1A3:MNTVLL&gt;

## Acronyms

| Term       | Definition                                                      |
|------------|-----------------------------------------------------------------|
| ASU        | Authorization/Subscription Utility                              |
| Clin4      | National Customer Support team that supports Clinical Reminders |
| CPRS       | Computerized Patient Record System                              |
| DBA        | Database Administration                                         |
| DG         | Registration and Enrollment Package namespace                   |
| ESM        | Enterprise Systems Management (ESM)                             |
| FIM        | Functional Independence Measure                                 |
| GMTS       | Health Summary namespace (also HSUM)                            |
| GUI        | Graphic User Interface                                          |
| HRMH/HRMHP | High Risk Mental Health Patient                                 |
| IAB        | Initial Assessment & Briefing                                   |
| ICD-10     | International Classification of Diseases, 10th Edition          |
| ICR        | Internal Control Number                                         |
| IOC        | Initial Operating Capabilities                                  |
| LSSD       | Last Service Separation Date                                    |
| MHTC       | Mental Health Treatment Coordinator                             |
| OHI        | Office of Health Information                                    |
| OI         | Office of Information                                           |
| OIF/OEF    | Operation Iraqi Freedom/Operation Enduring Freedom              |
| OIT/OI&T   | Office of Information Technology                                |
| OMHS       | Office of Mental Health Services                                |
| ORR        | Operational Readiness Review                                    |
| PCS        | Patient Care Services                                           |
| PD         | Product Development                                             |
| PIMS       | Patient Information Management System                           |
| PMAS       | Program Management Accountability System                        |
| PTM        | Patch Tracker Message                                           |
| PXRM       | Clinical Reminder Package namespace                             |
| RSD        | Requirements Specification Document                             |
| SD         | Scheduling Package Namespace                                    |
| SQA        | Software Quality Assurance                                      |
| USR        | ASU package namespace                                           |
| VA         | Department of Veteran Affairs                                   |
| VHA        | Veterans Health Administration                                  |
| VISN       | Veterans Integrated Service Network                             |
| VistA      | Veterans Health Information System and Technology Architecture  |