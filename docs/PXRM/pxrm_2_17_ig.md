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
source_file: pxrm_2_17_ig.docx
status: draft
title: pxrm 2 17 ig.docx
---

**PXRM*2*17**

**USR*1*33**

## Clinical Reminders

## Polytrauma Marker Dialogs and Reminders

## INSTALLATION and SETUP GUIDE

**May 2010**

Office of  Development


###### Revision History

| Revision Date   |   Page(s) | Description                                              | Project Manager   | Author   |
|-----------------|-----------|----------------------------------------------------------|-------------------|----------|
| June 3, 2010    |        24 | Added description of HS/TIU Object installation changes. | REDACTED          | REDACTED |

Contents

Introduction	1

Clinical Reminders PXRM*2*17 Documentation	1

Web Sites	1

Pre-Installation	2

Required Software for PXRM*2*17	2

Required Software for USR*1*33	2

Estimated Installation Time	2

Installation	3

1.	Retrieve host file containing the multi-package build	3

2.	Install the build first in a training or test account.	3

3.	Load the distribution.	3

a.	Backup a Transport Global	3

b.	Compare Transport Global to Current System	3

c.	Verify Checksums in Transport Global	4

d.	Print Transport Global (optional)	4

4.	Install the build.	4

5.	Install File Print	4

6.	Build File Print	4

7.	Post-installation routine	5

8.	Deletion of init routines	6

Set-up	7

Set-up Instructions	10

Appendix A: Installation Example	13

Release Notes	18

Acronyms	26

## Introduction

The purpose of this project is to release a new national reminder and reminder dialog that will be used by Polytrauma Specialty providers to identify potential OEF/OIF Polytrauma patients and mark the patient with a Polytrauma Marker (health factor) when appropriate.

The Polytrauma Marker project includes two patches:

PXRM*2*17 -	Clinical Reminder patch with Polytrauma Marker reminder/dialog

USR*1*33 -	ASU patch with API that checks to see if a user is a member of a specific User Class


### Clinical Reminders PXRM*2*17 and USR*1*33 Documentation

| **Documentation**    | **Documentation File name**   |
|----------------------|-------------------------------|
| Installation Guide   | PXRM_2_17_IG.PDF              |
| ASU Technical Manual | ASUTM.PDF                     |

#### Web Sites

| **Site**                              | **URL**                                                                                                            | **Description**                                                                            |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| National Clinical Reminders site      | http://vista.med.va.gov/reminders                                                                                  | Contains manuals, PowerPoint presentations, and other information about Clinical Reminders |
| National Clinical Reminders Committee | [http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx](http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx) | This committee directs the development of new and revised national reminders               |
| Document Library                      | [http://www.va.gov/vdl/](http://www.va.gov/vdl/)                                                                   | Contains manuals for Clinical Reminders and                                                |

**NOTE** : In this document you will see references to both PXRM*2*17 and PXRM*2.0*17.  The difference is that PXRM*2*17 is the name of the patch and PXRM*2.0*17 is the name of the build.


## Pre-Installation

This manual describes how to install the bundled patches, PXRM*2*17 and USR*1*33.

### Required Software for PXRM*2*17

| **Package/Patch**                     | **Namespace**   |   **Version** | **Comments**   |
|---------------------------------------|-----------------|---------------|----------------|
| Clinical Reminders                    | PXRM            |           2   | Fully patched  |
| GEN. MED. REC. – VITALS  GMRV*5*25    | GMRV            |           5   |                |
| Health Summary                        | GMTS            |           2.7 | Fully patched  |
| HL7                                   | HL              |           1.6 | Fully patched  |
| Kernel                                | XU              |           8   | Fully patched  |
| MailMan                               | XM              |           7.1 | Fully patched  |
| NATIONAL DRUG FILE  PSN*4.0*176       | PSN             |           4   |                |
| Pharmacy Data Management  PSS*1.0*133 | PSS             |           1   |                |
| Outpatient Pharmacy  PSO*7.0*299      | PSO             |           7   |                |
| RADIOLOGY/NUCLEAR MEDICINE  RA*5*56   | RA              |           5   |                |
| TOOLKIT  XT*7.3*111                   | XT              |           7.3 |                |
| VA FileMan                            | DI              |          22   | Fully patched  |


### Required Software for USR*1*33

| **Package/Patch**                                                                         | **Namespace**   |   **Version** | **Comments**   |
|-------------------------------------------------------------------------------------------|-----------------|---------------|----------------|
| Authorization/Subscription Utility (ASU)  USR*115  USR*1*22  USR*1*18  USR*1*28  USR*1*29 | USR             |             1 |                |

### Estimated Installation Time: 10-15 minutes


## Installation

This build can be installed with users on the system, but it should be done during non-peak hours.

***The installation needs to be done by a person with DUZ(0) set to "@."***

### 1 Retrieve host file containing the multi-package build

Use ftp to access the build (the name of the host file is POYLTRAUMA\_MARKER.KID) from one of the following locations:

Albany                         REDACTED                  REDACTED

Hines                           REDACTED                     REDACTED

Salt Lake City             REDACTED                          REDACTED

### 2 Install the build first in a training or test account.

Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

### 3 Load the distribution.

In programmer mode type, D ^XUP, select the Kernel Installation &amp; Distribution System menu (XPD MAIN), then the Installation option, and then the option LOAD a Distribution.  Enter your directory name and POLYTRAUMA\_MARKER.KID at the Host File prompt.

**Example**

Select Installation Option: **LOAD** a Distribution

Enter a Host File: **POLYTRAUMA\_MARKER.KID**

KIDS Distribution saved on DEC 17, 2009@11:53:53 NEED TO UPDATE THIS WITH THE ACTUAL

Comment: USR*1.0*33 and PXRM*2.0*17

From the Installation menu, you may elect to use the following options:


### 4 Backup a Transport Global

This option will create a backup message of any routines exported with the patch.  It will NOT back up any other changes such as DDs or templates.

### 5 Compare Transport Global to Current System

This option will allow you to view all changes that will be made when the patch is installed.  It compares all components of the patch (routines, DDs, templates, etc.).

### 6 Verify Checksums in Transport Global

This option will allow you to ensure the integrity of the routines that are in the transport global.  If there are any discrepancies, do not run the Install Package(s) option. Instead, run the Unload a Distribution option to remove the Transport Global from your system.  Retrieve the file again from the anonymous directory (in case there was corruption in FTPing) and Load the Distribution again.  If the problem still exists, log a Remedy ticket and/or call the national Help Desk (1-888-596-HELP) to report the problem.

### 7 Print Transport Global (optional)

This option will allow you to view the components of the KIDS build.

### 8 Install the build.

From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s).  Select the build POLYTRAUMA MARKER 1.0 and proceed with the install.  If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

Select Installation &amp; Distribution System Option: **Installation**

Select Installation Option: **INSTALL PACKAGE(S)**

Select INSTALL NAME: POLYTRAUMA MARKER 1.0

Answer "NO" to the following prompt:

Want KIDS to INHIBIT LOGONs during install? NO// **NO**

**NOTE: DO NOT QUEUE THE INSTALLATION** , because this installation may ask questions requiring responses and queuing will stop the installation. The most common are replacements for finding items or quick orders during the installation of Reminder Exchange file entries.

**Installation Example**

See Appendix A.

### 9 Install File Print

Use the KIDS Install File Print option to print out the results of the installation process. You can select the multi-package build or any of the individual builds included in the multi-package build.

Select Utilities Option: **Install** File Print

Select INSTALL NAME: PXRM*2.0*17

### 10 Build File Print

Use the KIDS Build File Print option to print out the build components.

Select Utilities Option:  Build File Print

Select BUILD NAME: **POLYTRAUMA MARKER 1.0**

DEVICE: HOME//

### 11 Post-installation routine

The installation will place the following exchange file entries in the Reminder Exchange file #811.8:

VA-AAA SCREENING

VA-PTSD REASSESSMENT (PCL)

VA-POLYTRAUMA MARKER

VA-BL DEPRESSION SCREEN

VA-HF ETOH SELF SCORE AUD 10

VA-EMBEDDED FRAGMENTS RISK EVALUATION

VA-GP EF CONTACT INFORMATION

VA-MH STOP CODES FOR PTSD EVALUATION

VA-HF ACUTE ILLNESS EVAL

DEPRESSION/PTSD REMINDER TERM UPDATES - PATCH 17

PXRM*2*17 COMPUTED FINDINGS

The post-install routine will install all the components of these Exchange file entries on your system. After the installation has finished, if you discover that any of these components weren’t installed correctly, you can use the Reminder Exchange option on the Reminders Manager Menu to install them.

NOTE: For the VA-AAA SCREENING (REMINDER/DIALOG), the term VA-OUTSIDE SCREENING FOR AAA was updated to include two health factors instead of just one. When the health summary type OB IMAGING FOR AAA is installed, you can choose to delete or replace each of the radiology procedures that are included on the health summary.  The radiology procedures that are included in the Exchange entry are:

MRA ABDOMEN, W OR W/O CONTRAST

MRA ABDOMEN W/O OR W

MRI ABDOMEN WITH CONTRAST

MRI ABDOMEN W/O&amp;W CONTRAST

MRI ABDOMEN W/O CONTRAST

ECHOGRAM PELVIC LIMITED

ECHOGRAM PELVIC

ECHOGRAM PELVIC COMPLETE

ECHOGRAM ABDOMEN LTD

ECHOGRAM ABDOMEN COMPLETE

ECHO AORTA IVC OR ILIAC VASC-LTD DUPLEX

ECHO AORTA IVC OR ILIAC VASC-COMPLETE DUPLE

CT ABDOMEN W/O CONT

CT ABDOMEN W/CONT

CT ABDOMEN W&amp;W/O CONT

Before you proceed with the Exchange install, determine which you are going to keep, delete, or replace.

### 12 Deletion of init routines

After everything has been successfully installed you may delete the following init routines:  PXRMP17E, PXRMP17I

## Set-up

**Overview**

This project was requested by the Office of Patient Care Services (PCS) to provide a means of improving care provided to veterans and active duty patients suffering from blast-related polytrauma (multiple complex injuries). VHA has identified this as one of several initiatives that will support health care of Operation Iraqi Freedom and Operation Enduring Freedom (OIF/OEF) veterans.

In order to provide the necessary specialized support and care for veterans with blast-related polytrauma injuries, it is essential to provide a means of easily identifying these veterans in the electronic health care record.  Clinicians need a way to quickly identify veterans with polytrauma injuries and Congress and Department of Veterans Affairs (VA) requires a means of tracking and reporting the care provided to these veterans.

This project includes new functionality that limits access of the reminder on the cover sheet to providers that are members of a locally defined Polytrauma rehabilitation user class.  The provider who is a member of this user class will be able to respond to the Polytrauma Marker reminder from the CPRS notes tab using a reminder dialog.

Sites currently use the Authorization/Subscription Utility software to control the level of authorization needed for signing specific document types and orderables. This will expand the use of the user class for reminder functionality.

A new national reminder computed finding, VA-ASU USER CLASS, has been created that can be used in reminder definitions, reminder terms, and reminder dialogs. This computed finding includes the ability to specify a user class showing that the user is active.

This computed finding can return multiple occurrences of a specified ASU user class for the user who is running the reminder evaluation or processing a reminder dialog.

When a user is assigned to an ASU User Class, there can be an Activation Date and an Expiration Date. For the purpose of this computed finding, the date of the finding will be the Activation Date. In those cases when there is no Activation Date, 00/00/0000 will be used.

If a Beginning Date/Time and Ending Date/Time are used with the finding, then the period defined by the Activation Date and Expiration Date must overlap with the period defined by the Beginning Date/Time and the Ending Date/Time in order for the finding to be true. When the Activation Date is missing, a 0 will be used in its place for determining the overlap. When the Expiration Date is missing, the evaluation date will be used in its place for determining the overlap.

The Computed Finding Parameter can be used to optionally specify either the internal entry number or the exact name of an ASU User Class. If this option is used, then each User Class the user is a member of is checked to see if it is either the specified User Class or a child of the specified User Class. Only the User Classes that pass this test will remain on the list of a user's User Classes. For example, if the user is a member of the user class ATTENDING PHYSICIAN which is a child of the user class PHYSICIAN and the Computed Finding Parameter is set to "PHYSICIAN" then ATTENDING PHYSICIAN would be true. If the Computed Finding Parameter was set to CARDIOLOGIST, then ATTENDING PHYSICIAN would be false since it is not a child of CARDIOLOGIST.

The Polytrauma Assessment reminder definition contains a new national reminder term which will be pre-defined with the new computed finding for the ASU User Class.  Sites will be required to add the Computed Finding Parameter to the national reminder term.  The parameter should specify the local ASU User Class that identifies specialty provider members that focus on Polytrauma and Rehabilitation services at the local facility.

The Polytrauma Assessment reminder uses a series of national Reminder Taxonomies to determine whether the patient has multiple diagnoses that identify the patient as a potential Polytrauma patient.  The combination of the diagnoses found and the user’s ASU user class will determine whether the reminder is applicable to the patient.

If the reminder is applicable to the patient and the patient has not been previously assessed for Polytrauma, the reminder will be DUE and will appear on the cover sheet and in the reminder drawer on the CPRS notes tab.

The reminder will be resolved by the provider responding to reminder dialog responses that result in the assessment that the patient “is” or “is not” an OEF/OIF Polytrauma patient.  The responses will cause Health Factors to be created that make the reminder no longer due.

If the CPRS user views Clinical Maintenance output for the Polytrauma Assessment reminder and the user is not a member of the ASU User Class, then a message will be included in the Patient Cohort section indicating that the ASU User Class was not found.

The new Polytrauma Assessment reminder dialog was created outside the OI Field Office and tested at three sites based on input from Rehabilitation Service stakeholders.

This reminder/dialog includes branching logic that will use the new national reminder term that is defined with the ASU user class used by the reminder definition. The branching logic will check to see if the CPRS user is a member of the ASU user class before continuing with the reminder dialog.  If the CPRS user is not a member of the ASU user class, then the reminder dialog will display text indicating the reminder is not applicable and the user is not the appropriate user to complete the reminder dialog.

Completing the reminder dialog will cause a progress note to be created and Health Factors will be populated in PCE. These health factors will be used by future reminder definition evaluation to indicate the reminder is resolved.

NOTE: This project raised a question about which sites use the PXRM NEW PARAMETER mechanism to determine which reminders should be presented to a user. In order for developers to answer this question, a new mechanism is needed at the sites to send information to the developers in a MailMan message.

Upon installation of the PXRM*2*17 patch, the post-installation process will check the local system’s setting of the PXRM NEW PARAMETER setting and will send a MailMan message to a FORUM Mail Group that will be defined with reminder developers as members.  The MailMan message will contain the site and its current PXRM NEW PARAMETER setting. **If your site doesn’t have NEW REMINDERS PARAMETER set to yes, then the Reminder Manager will not be able to assign the polytrauma reminder by user class.**

## Set-up Instructions

**1.   Map the orderable item that your Radiology department wants you to use to the AAA screening dialog.**

**2.  Check the site’s local definitions for ASU User Classes for a user class representing Polytrauma Specialists only.**

- If there isn’t one defined, create this user class and assign it to Polytrauma Specialists users at your facility.

- Use the User Class Management Menu, User Class Definition option to create/edit the Polytrauma Specialist class.

--- User Class Management Menu ---

1      User Class Definition

2      List Membership by User

3      List Membership by Class

5      Manage Business Rules

Select User Class Management Option: 1  User Class Definition

Select User Class Status: ACTIVE// **&lt;Enter&gt;** Active

Start With Class: FIRST// &lt;Enter&gt;

Go To Class: LAST// &lt;Enter&gt;

Searching for the User Classes..................................................

................

Edit User Class

1    ACCOUNTANT                                          ACC

2    ACCOUNTS PAYABLE EMPLOYEE                           PAY

3    ACCOUNTS RECEIVABLE EMPLOYEE                        RCV

4    ACCREDITATION REPRESENTATIVE                        JCAHO

5    ACTING ASSISTANT CHIEF                              AAC

6    ACTING ASSISTANT DIRECTOR                           AAD

7    ACTING CHIEF                                        AC

8    ACTING DIRECTOR                                     AD

9    ADDICTION MEDICINE                                  REHAB

10   ADJUDICATION OFFICER                                ADJ

11   ADMINISTRATIVE ASSISTANT                            AA

12   ADMINISTRATIVE INTERN                               AI

13   ADMINISTRATIVE OFFICER                              AO

14   ADMINISTRATIVE OFFICER OF THE DAY                   AOD

15   ADOLESCENT MEDICINE INTERNIST                       ADOLMD

Edit User Class

Select Action: Next Screen// **&lt;Enter&gt;** NEXT SCREEN

+         + Next Screen  - Prev Screen  ?? More Actions

Edit User Class

Select Action: Next Screen// Create a Class

Select CLASS: **POLYTRAUMA SPECIALIST**

Are you adding 'POLYTRAUMA SPECIALIST' as a new USR CLASS (the 121ST)? No// **Y** (Yes)

NAME: POLYTRAUMA SPECIALIST  Replace &lt;Enter&gt;

DISPLAY NAME: Polytrauma Specialist  Replace &lt;Enter&gt;

ABBREVIATION: POLY

ACTIVE: Y??

Indicate the status of the user class

Choose from:

1        Active

0        Inactive

ACTIVE: **1** Active

Select SUBCLASS: &lt;Enter&gt;

Rebuilding main class list......................................................

Find                      Expand/Collapse Class     Change View

Create a Class            List Members              Quit

Edit User Class

Select Action: Next Screen// **L** List Members

Select Class(s):  (399-413): **401**

User Classes                  Jan 29, 2010@17:07:55      Page:   27 of   42

ACTIVE USER CLASSES               622 Classes

+     Class Name                                         Abbrev

399  POLICE CLERK                                        POLICE

400  POLICE OFFICER                                      POLICE

401  POLYTRAUMA SPECIALIST

402  POST GRADUATE YEAR 1 RESIDENT                       PGY1

403  POST GRADUATE YEAR 2 RESIDENT                       PGY2

404  POST GRADUATE YEAR 3 RESIDENT                       PGY3

405  POST GRADUATE YEAR 4 RESIDENT                       PGY4

406  PRE-CERTIFICATION CLERK                             PRECERT

407  PRIVACY ACT OFFICER                                 PAO

408  PROCESSING &amp; RECORDS                                PRCREC

409  PROCESSING CLERK                                    PRCREC

410  PROCTOLOGIST                                        PROC

411  PROCUREMENT CLERK                                   PROC

412  PROGRAM ANALYST                                     PROGAN

413  PROGRAM ASSISTANT                                   PA

+         + Next Screen  - Prev Screen  ?? More Actions

Listing Members of #401

Searching for the User Classes.

Edit                      Schedule Changes          Quit

User Class Members            Jan 29, 2010@17:08:29      Page:    1 of    1

POLYTRAUMA SPECIALISTs               0 Members

Member                                              Effective  Expires

No POLYTRAUMA SPECIALISTs found

+ Next Screen  - Prev Screen  ?? More Actions                      &gt;&gt;&gt;

Add                       Remove                    Change View

Edit                      Schedule Changes          Quit

Select Action: Quit// **A** Add

Select MEMBER: **CRMEMBER,ONE** OC

MEMBER: CRMEMBER,ONE       //

EFFECTIVE DATE: &lt;Enter&gt;

EXPIRATION DATE: &lt;Enter&gt;

Select Another MEMBER: &lt;Enter&gt;

--- User Class Management Menu ---

Rebuilding membership list.

Edit                      Schedule Changes          Quit

User Class Members            Jan 29, 2010@17:11:20         Page:  1 of    1

POLYTRAUMA SPECIALISTs                 1 Member

Member                                               Effective  Expires

1    CRMEMBER,ONE

** CRMEMBER,ONE Added **                                       &gt;&gt;&gt;

Add                       Remove                    Change View

Edit                      Schedule Changes          Quit

Select Action: Quit//    Quit

Refreshing the list.

- Use the User Class Management Menu, List Membership by Class to ensure the correct membership for Polytrauma specialist

**3. Add the Computed Finding Parameter to the national reminder term**

- Modify the VA-POLYTRAUMA SPECIALIST ASU USER CLASS reminder term’s VA-ASU USER CLASS finding item’s computed finding parameter field to be the name (or internal entry number) of  the local ASU User Class assigned to Polytrauma Specialists.  Follow the help text as needed for formatting the parameter.

- The Polytrauma Marker reminder definition contains a new national reminder term, VA-POLYTRAUMA SPECIALIST ASU USER CLASS, which is pre-defined with the new VA-ASU USER CLASS computed finding.

- Sites are required to add the Computed Finding parameter to the national reminder term.  The parameter should specify the local ASU User Class that identifies specialty provider members that focus on Polytrauma and Rehabilitation services at the local facility.

## Appendix A: Installation Example

XPD MAIN       Kernel Installation &amp; Distribution System

Edits and Distribution ...

Utilities ...

Document Enhancement type patches

Installation ...

Patch Monitor Main Menu ...

Select Kernel Installation &amp; Distribution System Option: INStallation

1      Load a Distribution

2      Verify Checksums in Transport Global

3      Print Transport Global

4      Compare Transport Global to Current System

5      Backup a Transport Global

6      Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: 1  Load a Distribution

Enter a Host File: USER$:[MONTGOMERYA]POLYTRAUMA\_MARKER.KID

KIDS Distribution saved on Apr 14, 2010@14:01:02

Comment: USR*1.0*33 and PXRM*2.0*17

This Distribution contains Transport Globals for the following Package(s):

POLYTRAUMA MARKER 1.0

USR*1.0*33

PXRM*2.0*17

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

POLYTRAUMA MARKER 1.0

USR*1.0*33

PXRM*2.0*17

Use INSTALL NAME: POLYTRAUMA MARKER 1.0 to install this Distribution.

1      Load a Distribution

2      Verify Checksums in Transport Global

3      Print Transport Global

4      Compare Transport Global to Current System

5      Backup a Transport Global

6      Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: INSTall Package(s)

Select INSTALL NAME: POLYTRAUMA MARKER 1.0       Loaded from Distribution  4/23/

10@10:50:08

=&gt; USR*1.0*33 and PXRM*2.0*17  ;Created on Apr 14, 2010@14:01:02

This Distribution was loaded on Apr 23, 2010@10:50:08 with header of

USR*1.0*33 and PXRM*2.0*17  ;Created on Apr 14, 2010@14:01:02

It consisted of the following Install(s):

POLYTRAUMA MARKER 1.0     USR*1.0*33    PXRM*2.0*17

Checking Install for Package POLYTRAUMA MARKER 1.0

Install Questions for POLYTRAUMA MARKER 1.0

Checking Install for Package USR*1.0*33

Install Questions for USR*1.0*33

Checking Install for Package PXRM*2.0*17

Install Questions for PXRM*2.0*17

Incoming Files:

811.4     REMINDER COMPUTED FINDINGS  (including data)

Note:  You already have the 'REMINDER COMPUTED FINDINGS' File.

I will OVERWRITE your data with mine.

811.8     REMINDER EXCHANGE  (including data)

Note:  You already have the 'REMINDER EXCHANGE' File.

I will OVERWRITE your data with mine.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME//   VIRTUAL TELNET

Install Started for POLYTRAUMA MARKER 1.0 :

Apr 23, 2010@10:50:43

Build Distribution Date: Apr 14, 2010

Installing Routines:  Apr 23, 2010@10:50:43

Install Started for USR*1.0*33 :

Apr 23, 2010@10:50:43

Build Distribution Date: Apr 14, 2010

Installing Routines:  Apr 23, 2010@10:50:44

Updating Routine file...

Updating KIDS files...

USR*1.0*33 Installed. Apr 23, 2010@10:50:44

Install Started for PXRM*2.0*17 :

Apr 23, 2010@10:50:44

Build Distribution Date: Apr 14, 2010

Installing Routines: Apr 23, 2010@10:50:45

Running Pre-Install Routine: PRE^PXRMP17

DISABLE options.

DISABLE protocols.

Installing Data Dictionaries: Apr 23, 2010@10:50:45

Installing Data: Apr 23, 2010@10:50:48

Installing PACKAGE COMPONENTS:

Installing OPTION Apr 23, 2010@10:50:48

Running Post-Install Routine: POST^PXRMP17I

ENABLE options.

ENABLE protocols.

Renaming some Sponsor entries

There are 12 Reminder Exchange entries to be installed.

1. Installing Reminder Exchange entry VA-AAA SCREENING

Selection item R.MRI ABDOMEN WITH CONTRAST does not exist, what do you want to do?

Select one of the following:

D         Delete

P         Replace with an existing entry

Q         Quit the install

Enter response: P  Replace with an existing entry

Select RAD/NUC MED PROCEDURES NAME: MRI

1   MRI-LT KNEE                                  (MRI  Detailed) CPT:73718

2   MRI-RT KNEE                                  (MRI  Detailed) CPT:73718

3   MRI  MAGNETIC IMAGE,LOWER EXTREMITY          (MRI  Detailed) CPT:73720

4   MRI  MAGNETIC IMAGE,UPPER EXTREMITY          (MRI  Detailed) CPT:73220

5   MRI  MAGNETIC IMAGE,ABDOMEN                  (MRI  Detailed) CPT:74181

Press &lt;RETURN&gt; to see more, '^' to exit this list, OR

CHOOSE 1-5: 5  MAGNETIC IMAGE,ABDOMEN                 (MRI  Detailed) CPT:74181

Selection item R.MRA ABDOMEN W/O OR W does not exist, what do you want to do?

Select one of the following:

D         Delete

P         Replace with an existing entry

Q         Quit the install

Enter response: P  Replace with an existing entry

Select RAD/NUC MED PROCEDURES NAME: ECHO PELVIS COMPLETE    (US   Detailed) CPT:76856

Selection item R.MRA ABDOMEN, W OR W/O CONTRAST does not exist, what do you want to do?

Select one of the following:

D         Delete

P         Replace with an existing entry

Q         Quit the install

Enter response: P  Replace with an existing entry

Select RAD/NUC MED PROCEDURES NAME: ECHO PELVIS LIMITED    (US   Detailed) CPT:76857

Selection item R.ECHO AORTA IVC OR ILIAC VASC-COMPLETE DUPLEX does not exist, what do you want to do?

Select one of the following:

D         Delete

P         Replace with an existing entry

Q         Quit the install

Enter response: Delete

Selection item R.ECHO AORTA IVC OR ILIAC VASC-LTD DUPLEX does not exist, what do you want to do?

Select one of the following:

D         Delete

P         Replace with an existing entry

Q         Quit the install

Enter response: Delete

Selection item R.ECHOGRAM PELVIC does not exist, what do you want to do?

Select one of the following:

D         Delete

P         Replace with an existing entry

Q         Quit the install

Enter response: Delete

Selection item R.MRI ABDOMEN W/O CONTRAST does not exist, what do you want to do?

Select one of the following:

D         Delete

P         Replace with an existing entry

Q         Quit the install

Enter response: Delete

Selection item R.MRI ABDOMEN W/O&amp;W CONTRAST does not exist, what do you want to do?

Select one of the following:

D         Delete

P         Replace with an existing entry

Q         Quit the install

Enter response: Delete

2. Installing Reminder Exchange entry VA-PTSD REASSESSMENT (PCL)

3. Installing Reminder Exchange entry VA-POLYTRAUMA MARKER

4. Installing Reminder Exchange entry VA-BL DEPRESSION SCREEN

5. Installing Reminder Exchange entry VA-HF ETOH SELF SCORE AUD 10

6. Installing Reminder Exchange entry VA-EMBEDDED FRAGMENTS RISK EVALUATION

7. Installing Reminder Exchange entry VA-GP EF CONTACT INFORMATION

8. Installing Reminder Exchange entry VA-GP ALC ADVICE2

9. Installing Reminder Exchange entry VA-MH STOP CODES FOR PTSD EVALUATION

10. Installing Reminder Exchange entry VA-HF ACUTE ILLNESS EVAL

11. Installing Reminder Exchange entry DEPRESSION/PTSD REMINDER TERM UPDATES

- PATCH 17

12. Installing Reminder Exchange entry PXRM*2*17 COMPUTED FINDINGS

MST synchronization queued; task number 3104209.

Updating Routine file...

Updating KIDS files...

PXRM*2.0*17 Installed.

Apr 23, 2010@16:40:10

Updating Routine file...

Updating KIDS files...

POLYTRAUMA MARKER 1.0 Installed.

Apr 23, 2010@16:40:10

Install Completed

## Release Notes

The Polytrauma Marker project releases a new national reminder and reminder dialog that Polytrauma Specialty providers can use to identify potential OEF/OIF Polytrauma patients and mark with a Polytrauma Marker (health factor), when appropriate.

The Polytrauma Marker project includes two patches:

PXRM*2*17 -	Clinical Reminder patch with Polytrauma Marker reminder/dialog

USR*1*33 -	ASU patch with API that checks to see if a user is a member of a specific User Class

**Patch USR*1*33 Description**

This patch changes displays of User Class Names in Authorization and   Subscription Utility (ASU) options. User Class Names are now shown by the name of the entry in the User Class File (File #8930).  Previously, they were shown by their display names. In particular, the User Class Definition Option [USR CLASS DEFINITION] has been changed to show the entry name of the User Class.

The User Class Definition Option [USR CLASS DEFINITION] is found under the User Class Management Menu [USR CLASS MANAGEMENT MENU], which is found under the TIU Maintenance Menu [TIU IRM MAINTENANCE MENU].

In addition, the module used to list the User Classes a particular user belongs to has been enhanced. It may now be set to list classes by entry name rather than by display name, if desired.

These changes are necessary because it is the entry name of the Class that users see in User Class edits and various ASU modules. Using the same name in displays avoids confusion.

The following example is from a medical center that has populated its User Class File (#8930) with User Class Names in upper case (as in ACCOUNTANT) and Display Names with title capitalization (as in Accountant). Thus in the User Class Definition Option [USR CLASS DEFINITION] all names that appear in the list of active user classes are the actual User Class Names and thus are all in upper case:

**User Classes** Apr 01, 2010@21:40:09         Page:    1 of   44

ACTIVE USER CLASSES                    653 Classes

Class Name                                         Abbrev

This is the User Class Name, not the Display Name.

1    ACCOUNTANT                                          ACC

2    ACCOUNTS PAYABLE EMPLOYEE                           PAY

3    ACCOUNTS RECEIVABLE EMPLOYEE                        RCV

4    ACCREDITATION REPRESENTATIVE                        JCAHO

5    ACTING ASSISTANT CHIEF                              AAC

6    ACTING ASSISTANT DIRECTOR                           AAD

7    ACTING CHIEF                                        AC

8    ACTING DIRECTOR                                     AD

9    ADDICTION MEDICINE                                  REHAB

10   ADJUDICATION OFFICER                                ADJ

11   ADMINISTRATIVE ASSISTANT                            AA

12   ADMINISTRATIVE INTERN                               AI

13   ADMINISTRATIVE OFFICER                              AO

14   ADMINISTRATIVE OFFICER OF THE DAY                   AOD

15   ADOLESCENT MEDICINE INTERNIST                       ADOLMD

+          + Next Screen   - Prev Screen   ?? More

Find                      Expand/Collapse Class     Change View

Create a Class            List Members              Quit

Edit User Class

Select OPTION NAME:

**Patch PXRM*2*17 Description**

**Reminder Exchange File Entries**

| **Reminder Definition/Dialog/Dialog Element**    | **Description**                                                                                                           |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| VA-AAA SCREENING (REMINDER/DIALOG)               | Updates term VA-OUTSIDE SCREENING FOR AAA to include two health factors instead of just one.                              |
| VA-POLYTRAUMA MARKER                             | Reminder print name: Combat Polytrauma Confirmation                                                                       |
| VA-PTSD REASSESSMENT (PCL) REMINDER/DIALOG       | Updates dialog to use the health factor UNABLE TO SCREEN-ACUTE MED CONDITION instead of UNABLE TO SCREEN - ACUTE ILLNESS. |
| VA-BL DEPRESSION SCREEN                          | Branching logic dialog element.                                                                                           |
| VA-HF ETOH SELF SCORE AUD 10                     | Update to dialog element VA-HF ETOH SELF SCORE AUD 10.                                                                    |
| VA-HF ETOH SELF SCORE AUD 10 dialog element      | Removes duplicate AUD10 entries from the result group which was duplicating text in the notes.                            |
| VA-EMBEDDED FRAGMENTS RISK EVALUATION            | Updated Reminder/dialog.                                                                                                  |
| VA-GP EF CONTACT INFORMATION DIALOG GROUP        | Updates the contact information fields to be local to allow local editing.                                                |
| VA-MH STOP CODES FOR PTSD EVALUATION             | Updates to the Reminder Location List for VA-MH STOP CODES FOR PTSD EVALUATION.                                           |
| VA-HF ACUTE ILLNESS EVAL                         | Updates to the dialog element VA-HF ACUTE ILLNESS EVAL.                                                                   |
| DEPRESSION/PTSD REMINDER TERM UPDATES - PATCH 17 | Updates to the reminder term VA-REFUSED PTSD SCREEN and VA-DEPRESSION SCREEN OEF/OIF.                                     |
| PXRM*2*17 COMPUTED FINDINGS                      | Described below.                                                                                                          |

**Reminder Computed Findings:**

Three national computed findings are included:

*VA-ASU USER CLASS (new)*

This multi-occurrence computed finding returns a list of the ASU User Classes that the user belongs to. The user is the person who is running the reminder evaluation or processing a reminder dialog.

When a user is assigned to an ASU User Class, there can be an Activation Date and an Expiration Date. For the purpose of this computed finding, the date of the finding will be the Activation Date. In those cases when there is no Activation Date, 00/00/0000 will be displayed as the date of the finding. If a Beginning Date/Time and Ending Date/Time are used with the finding, then the period defined by the Activation Date and Expiration Date must overlap the period defined by the Beginning Date/Time and the Ending Date/Time, in order for the finding to be true. When the Activation Date is missing, a 0 will be used in its place for determining the overlap. When the Expiration Date is missing, the evaluation date will be used in its place for determining the overlap.

The Computed Finding Parameter can be used to specify either the internal entry number or the exact name of an ASU User Class. If this option is used, then each User Class the user is a member of is checked to see if it is either the specified User Class or a child of the specified User Class. Only the User Classes that pass this test will remain on the list of the user's User Classes. For example, if the user is a member of the user class ATTENDING PHYSICIAN, which is a child of the user class PHYSICIAN, and the Computed Finding Parameter is set to "PHYSICIAN," then ATTENDING PHYSICIAN will remain on the list. If the Computed Finding Parameter was set to CARDIOLOGIST, then ATTENDING PHYSICIAN would be removed since it is not a child of CARDIOLOGIST.

If you want to specify the user class as PHYSICIAN, type the following in the computed finding parameter field: COMPUTED FINDING PARAMETER:PHYSICIAN

This computed finding uses date ranges like drug findings do, so if the user was an active member of the class anytime during the date range, the computed finding will be true. If you want to know if the user is active as of today, then use T for the beginning and ending date/time.

*VA-WAS INPATIENT (new)*

This multi-occurrence computed finding will search the Patient Movement File for a list of patient admissions and associated discharges. If the date range defined by the admission date and discharge date overlap the date range defined by the Beginning Date/Time and Ending Date/Time, the admission discharge pair will be kept on the list. If the patient's last admission does not have an associated discharge, then the evaluation date will be used in place of the discharge date in the overlap calculation.

The date of the finding will be the admission date, unless the Computed Finding Parameter is set to "DISCH," in which case the discharge date will be used. If you want to use discharge date as date of finding in the computed finding parameter field, type the following:  COMPUTED FINDING PARAMETER:DISCH

The "CSUB" values returned by this computed finding are:

"ADMISSION DATE"

"DISCHARGE DATE"

"LENGTH OF STAY"

*VA-ACTIVE PATIENT RECORD FLAGS (new)*

This multiple occurrence computed finding will return active patient record flags. The Computed Finding Parameter is used to precisely specify what flags to search for. Three parameters can be used: C for category, T for type, and F for a specific flag.

The possible values are:

Category - N (national), L (local)

Type - B (behavioral), C (clinical), O (other), and R (research)

Flag - exact name of the flag

Use the "^" character to include more than one parameter in the search specification.

Some examples:

C:L - searches for local flags

C:N^T:B - searches for national flags whose type is behavioral

F:DRINKING PROBLEM - searches for the flag DRINKING PROBLEM

T:C^F:INFECTIOUS DISEASE - searches for the flag INFECTIOUS DISEASE whose type is clinical

Only active flags that meet all the specified criteria will be returned. If no search parameters are specified, then no flags will be returned.

The date associated with a flag is the assigned date.

The following "CSUB" data is returned for each flag that is found:

APPRVBY  - approved by

ASSIGNDT - assigned date/time

CATEGORY - category

DATE     - assigned date/time

FLAG     - flag name

FLAGTYPE - flag type

ORIGSITE - originating site

OWNER    - owner site

REVIEWDT - review date/time

TIULINK  - pointer to the TIU note (only applies if the flag is linked to a

TIU note)

TIUTITLE - the note title (only applies if the flag is linked to a

TIU note)

**Reminder Evaluation:**

The resolution date calculation was not correct when the resolution logic contained a “NOT”. In those cases where the resolution logic evaluated to true, the resolution date was calculated to be 0. This was corrected so that the resolution date will no longer be calculated as 0.

The Clinical Maintenance output was not displaying the resolution finding header when the resolution logic evaluated to false, but one or more of the resolution findings was true. This was corrected.

There was a bug in the display of drug findings; for multiple drug findings in a term, only one occurrence of each finding type was displaying. This was corrected.

Other problems were reported with the display of drug findings. A complete fix of this pre-existing problem will require more time and testing than we have available for this patch, so a complete solution will have to come in a future patch. Nevertheless, one problem was rectified: The output was not consistent across inpatient, outpatient, and non-VA meds. The output was changed so that it is as consistent as possible (there are some fields that apply only to outpatient and some that apply only to non-VA.)

A bug was reported where a non-CH lab test would not work when used as a term finding, but would work when used as a definition finding. This is corrected.

A problem with an incorrect resolution date calculation for a resolution logic string containing a 'FF was corrected.

**Reminder Reports:**

Patch PXRM*2*12 added the new field OWNER to reminder report templates. E3R 20277 requested including this field when displaying the details of the template. This functionality has been added. If an owner is defined, the template will list the owner name. If an owner is not defined, the template will display "None" next to the owner field.

Remedy ticket 372679 reported a bug where the Reminders Due Report was not producing any output when the selected output device was a host file. This was found to be the case at some, but not all sites. The reason for this is that sites can name a host file device anything they want and the report was expecting a certain set of names. The solution was to use the type instead of the name, because types are standardized.

**Reminder Sponsor:**

The following Sponsors are renamed:

Mental Health and Behavioral Science Strategic Group

to

Office of Mental Health Services

Mental Health and Behavioral Science Strategic Group and Women Veterans

Health  Program

to

Office of Mental Health Services and Women Veterans Health Program

**Reminder Taxonomies:**

A new option, PXRM TAXONOMY CODE SEARCH, has been added to the TAXONOMY MANAGEMENT MENU. This option will let the user input a code and then it will search all taxonomies in the account and list those where it is used.

**Miscellaneous:**

The mechanism used by the Clinical Reminders package to deliver MailMan messages was changed to make it more flexible.

When PXRM*2.0*17 is installed in a test account, a MailMan message containing the value of ORQQPX NEW REMINDER PARAMS will be sent to the Clinical Reminders mail group. When the installation is done in a production account, the message will be sent to a Forum mail group. If a site doesn’t have NEW REMINDERS PARAMETER set to yes, then the Reminders Manager will not be able to assign the Polytrauma reminder by user class and that is the reason for the new computed finding. So if a site has a problem and Reminders developers or customer support staff know that a site has the parameter set to NO, developers or support staff can tell the site how to fix it.

A problem with the MST History file not updating after recording one of the MST health factors was reported; Remedy ticket #367613. A fix for this problem is included and the post-init will start an MST synchronization job to ensure that the MST History file is up-to-date.

A problem with an incorrect resolution date calculation for a resolution logic string containing a 'FF was corrected.

Prior to patch PXRM*2*17, there was a conflict between the VA-IRAQ &amp; AFGHAN POST-DEPLOY SCREEN reminder definition and its dialog. On the coversheet, the reminder was showing as DUE NOW, but when the dialog was opened, there were no items to complete. Briefly, this was because the two health factors DEP SCREEN 2 QUESTION NEG and DEP SCREEN 2 QUESTION POS were used in the definition with an ending date/time of 11/30/06 while in the dialog they had an ending date/time of 9/30/08. To resolve the problem, the Ending Date/Time was removed from the health factors in the definition. Complete details can be found below. If you are not interested, please skip the next section.

Background for the date conflict: One of the findings in the reminder definition was the reminder term VA-DEPRESSION SCREEN OEF/OIF, and two of its mapped findings were the health factors DEP SCREEN 2 QUESTION NEG and DEP SCREEN 2 QUESTION POS. Both of these mapped findings had an ending date/time of 11/30/06. However, the dialog used the branching term VA-BL DEPRESSION SCREENING that was mapped to the computed finding VA-REMINDER DEFINITION. VA-REMINDER DEFINITION evaluated the reminder definition VA-BL DEPRESSION SCREEN with the Condition checking for a status of “DUE NOW”.  Two of the findings in this reminder definition were the terms: VA-DEPRESSION SCREEN NEGATIVE, containing the health factor DEP SCREEN 2 QUESTION NEG as a mapped finding, and VA-DEPRESSION SCREEN POSITIVE, containing the health factor DEP SCREEN 2 QUESTION POS—both with an Ending Date/Time of 9/30/08. As noted above, the same two health factors were used in the term VA-DEPRESSION SCREEN OEF/OIF, but they had an Ending Date/Time of 11/30/06. Therefore, if a patient had either of these health factors given between the dates of 11/30/06 and 9/30/08, we would see this inconsistency. To resolve this problem, the Ending Date/Time on these health factors in the term VA-DEPRESSION SCREEN OEF/OIF was removed, but they were left in the terms VA-DEPRESSION SCREEN NEGATIVE and VA-DEPRESSION SCREEN POSITIVE. The reason was that this requires sites to do less remapping. After this change, if a patient has a health factor of DEP SCREEN 2 QUESTION NEG or DEP SCREEN 2 QUESTION POS given between the dates of 11/30/06 and 9/30/08, the reminder will no longer show as due on the coversheet. This change is made when the Reminder Exchange entry DEPRESSION/PTSD REMINDER TERM UPDATES - PATCH 17 is installed during the post-init.

DEPRESSION/PTSD REMINDER TERM UPDATES - PATCH 17

Per the Office of MH, the end dates were removed on any health factors used in the following terms:

VA-REFUSED PTSD SCREEN

VA-DEPRESSION SCREEN OEF/OIF

VA-DEPRESSION SCREEN NEGATIVE

VA-DEPRESSION SCREEN POSITIVE

Given that some sites have had problems with MHA, the MH instruments cannot be required at all sites and health factors may still be in use at some sites as late as FY10.  These old screening tools need to be included as valid.

**Problems installing TIU Health Summary Objects**

When installing a health summary type via Reminder Exchange, if any of the selection items are missing, users will now be able to delete the selection item, replace it with another one, or delete it from the health summary type.

In the past, if you tried to install a TIU Health Summary Object without installing the prerequisites first, the object method would not have the correct form, making it non-functional (even though it seemed as if it installed properly). Reminder Exchange now checks to make sure the Health Summary Object name can be resolved into an internal entry number so it will function properly. If it cannot be resolved, an error message is displayed telling the user to install the prerequisites and then it returns the user back to the main Exchange screen.

**USR*1.0*33**

A test site reported a hard error when trying to remove a user from a user class:

Current User Classes          Feb 09, 2010@12:55:37          Page:    1 of    1

XXX,YYY                                 3 Classes

User Class                                             Effective  Expires

1    AGP Test                                               10/21/09

2    ATTENDING PHYSICIAN                                    02/28/02

3    CARDIOLOGIST                                           07/01/00   12/31/08

4    TELEPHONE OPERATOR                                     01/01/98   01/29/10

Add                       Remove                    Quit

Edit                      Change View

Select Action: Quit// REM   Remove

Select Class(s):  (1-4): 4

S USER=$$GET1^DIQ(200,USER,.01) ; ICR 10060

This has been corrected.

## Acronyms

| Term    | Definition                                                     |
|---------|----------------------------------------------------------------|
| ASU     | Authorization/Subscription Utility                             |
| CPRS    | Computerized Patient Record System                             |
| ESM     | Enterprise Systems Management (ESM)                            |
| FIM     | Functional Independence Measure                                |
| GUI     | Graphic User Interface                                         |
| IAB     | Initial Assessment & Briefing                                  |
| OI      | Office of Information                                          |
| OIF/OEF | Operation Iraqi Freedom/Operation Enduring Freedom             |
| PCS     | Patient Care Services                                          |
| PXRM    | Clinical Reminder Package namespace                            |
| RSD     | Requirements Specification Document                            |
| VA      | Department of Veteran Affairs                                  |
| USR     | ASU package namespace                                          |
| VistA   | Veterans Health Information System and Technology Architecture |