---
app_name: 'CPRS: Consult/Request Tracking (GMRC)'
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: 2024-08
doc_type: user-manual
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-12'
is_base: false
is_change_pages: false
library_max_patch: null
package_id: GMRC
patch: 206
patch_gap: null
section: ''
source_file: consum.docx
status: draft
title: Consult/Request Tracking
---

# Consult/Request Tracking

# User Manual

<!-- image -->

Version 3.0

August 2024

Department of Veterans Affairs (VA)


Revision History

| Date    | Patch        | Description                                                                                                                                                                                                                                                                                                                                                                                                          | Authors               |
|---------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| 08/2024 | GMRC*3.0*206 | Updated for 508 compliance                                                                                                                                                                                                                                                                                                                                                                                           | CPRS Development Team |
| 09/2021 | GMRC*3.0*181 | Redaction of screen captures to remove IP addresses and then remove arrows and call outs. Various places throughout manual.                                                                                                                                                                                                                                                                                          | Liberty ITS           |
| 03/2021 | GMRC*3.0*84  | NSR 20110210 – Added the Prosthetics Consult Updated entry to the notifications table, added the Prosthetics Consult Updated section.                                                                                                                                                                                                                                                                                | Liberty ITS           |
| 03/2021 | GMRC*3.0*170 | - Replaced sentence in the Cancelled to Discontinued Consults section with, “ **Each consult fitting the parameter criteria is evaluated as to whether the consult was resubmitted and then cancelled again on a later date. If there is no later cancellation date, the consult is discontinued by calling the $$DC^GMRCGUIA API.** ” - Updated Title page, Revision History, Table of Contents, Index, and Footers | Liberty ITS           |
| 11/2020 | GMRC*3.0*145 | Under Enhancements since Version 2.5, added paragraph describing GMRC*3.0*145.  Under Consult/Request Resolution, updated text for notification trigger  Revised dates on Title page and footers                                                                                                                                                                                                                     | **REDACTED**          |
| 11/2019 | GMRC*3.0*139 | Added Auto-forwarding to DST Consult handling. See page 2, 4                                                                                                                                                                                                                                                                                                                                                         | **REDACTED**          |
| 4/2019  | GMRC*3.0*124 | Added reference to changes in Package Operation Workflow for users of Care Coordination (CC) Decision Support Tool (DST). See Page 12                                                                                                                                                                                                                                                                                | **REDACTED**          |
| 3/2019  | GMRC*3.0*119 | Added Help Text that displays when entering ??? at the "Select Consult Tracking Reports Option:" prompt. See Page 159  Added the Administratively Released Consults by Group Local Report example. The report was changed to include in the counts those services that were made in a consult name including -DS or -ADMIN but then forwarded to a different service. See Page 162.                                  | **REDACTED**          |
| 2/2019  | GMRC*3.0*113 | Added the Cancelled to Discontinued Consults section. Added the option GMRC CX TO DC PARAMETER EDIT, where user is able to update parameters that drive the overnight job GMRC CHANGE STATUS X TO DC. Page 161 – 162.                                                                                                                                                                                                | **REDACTED**          |
| 1/2019  | GMRC*3*110   | When a user clicks on the Consults tab, then highlights a Consult, the details of the consult appear in the right-hand panel. This display was changed to display the Unique Consult ID (UCID) at the top. See Page 161.                                                                                                                                                                                             | **REDACTED**          |
| 12/2018 | GMRC*3.0*107 | Added details for new GMRC Reports to support the ADMIN KEY consults for consults that are Administratively released by Policy. See pages 158 – 161.                                                                                                                                                                                                                                                                 | **REDACTED**          |
| 08/2018 | XU*8.0*679   | Added note regarding electronic Signature Block restrictions. See Page 19.                                                                                                                                                                                                                                                                                                                                           | **REDACTED**          |
| 03/3018 | GMRC*3*91    | Added information about additional recipients receiving an alert. See Page 139 and Page 150.                                                                                                                                                                                                                                                                                                                         | **REDACTED**          |
| 03/2018 | GMRC*3*92    | Update the VistA last name criteria.  Applied up-to-date 508 standards and VA compliance to title page, Revision History table, headings, and footers.                                                                                                                                                                                                                                                               | **REDACTED**          |
| 03/2018 | GMRC*3*89    | Modified SF 513 images (Image 1 and Image 2) to reflect addition of Age and Cell Phone fields. Added info re: set up of a secondary printer for SF 513. Added info on new Consult Closure Tool.                                                                                                                                                                                                                      | **REDACTED**          |
| 02/2016 | GRMC*3*81    | Changed the Earliest Appropriate Date to Clinically Indicated Date. Pages: 16, 22, 32,  Error! Bookmark not defined.                                                                                                                                                                                                                                                                                                 | **REDACTED**          |
| 08/2014 | GMRC*3*75    | Modified description to CONSULT/REQUEST UPDATED; added description of HCPS and RAS to Glossary                                                                                                                                                                                                                                                                                                                       | **REDACTED**          |
| 01/2015 | GMRC*3*82    | Modified SF 513 Images to reflect SSN format change.                                                                                                                                                                                                                                                                                                                                                                 | **REDACTED**          |
| 02/2014 | GMRC*3*73    | ICD-10 Remediation                                                                                                                                                                                                                                                                                                                                                                                                   | **REDACTED**          |
| 02/2014 | GMRC*3*73    | Added info to description for CONSULT/REQUEST UPDATED and Consult/Request Has an Added Comment.                                                                                                                                                                                                                                                                                                                      | **REDACTED**          |
| 08/2011 | GMRC*3*71    | Modified description for CONSULT/REQUEST UPDATED                                                                                                                                                                                                                                                                                                                                                                     | **REDACTED**          |
| 02/2011 |              | Earliest Appropriate Date Patch 66                                                                                                                                                                                                                                                                                                                                                                                   | **REDACTED**          |
| 08/2009 |              | Combat Veteran (CV) status added to SF 513                                                                                                                                                                                                                                                                                                                                                                           | **REDACTED**          |
| 04/2006 |              | Updates/corrections to patient and provider names to comply with SOP 192-352                                                                                                                                                                                                                                                                                                                                         | **REDACTED**          |
| 12/2004 |              | SOP 192-352 applied (scrubbed)                                                                                                                                                                                                                                                                                                                                                                                       | **REDACTED**          |
| 06/2002 |              | Include Patch 25                                                                                                                                                                                                                                                                                                                                                                                                     |                       |
| 04/2002 |              | Include Patch 22 & 25                                                                                                                                                                                                                                                                                                                                                                                                |                       |
| 11/2001 |              | Include Patch 17                                                                                                                                                                                                                                                                                                                                                                                                     |                       |
| 06/2001 |              | Include Patch 21                                                                                                                                                                                                                                                                                                                                                                                                     |                       |
| 02/2001 |              | Include Patch 15, 19, & 20                                                                                                                                                                                                                                                                                                                                                                                           |                       |
| 10/2000 |              | Include Patches 13, 14, 16, & 18                                                                                                                                                                                                                                                                                                                                                                                     |                       |
| 07/2000 |              | Add Patches 6 thru 8, 11, & 12                                                                                                                                                                                                                                                                                                                                                                                       |                       |
| 09/1998 |              | Include Patches 1 thru 5                                                                                                                                                                                                                                                                                                                                                                                             |                       |
| 12/1997 |              | Initial Release                                                                                                                                                                                                                                                                                                                                                                                                      |                       |

###### 

###### Table of Contents

Introduction	1

Overview	2

Purpose	2

Relationship to Other Packages	2

Enhancements since Version 2.5	3

GMRC*3.0*145	3

GMRC*3.0*139	3

Relations with other VistA Components	4

Related Manuals and Other References	6

Package Management	7

Service Update and Tracking Security	7

Consult Service Tracking	7

Package Operation	11

Workflow	11

1. The Clinician Orders a Consult	13

2. The Consult Service Gets a Written Copy	22

3. If Accepted, an Appointment is Held	23

4. Results are Entered and Signed	26

5. The Originating Clinician Receives an Alert that the Consult is Complete	29

6. The SF 513 Report Becomes Part of the Patient’s Medical Record	31

Quick Orders	34

Using the Consults Package with TIU	36

Direct TIU Input	36

Correcting Misdirected Results	40

Using the Consults Package with Medicine	52

Using the Consults Package with Clinical Procedures	55

Windows Quick Start	56

Introduction 57	56

Windows Flow of Information 58	56

Other Windows Topics 77	56

Introduction	57

Windows Flow of Information	58

Other Windows Topics	77

Changes made by Patch 73 for ICD-10 Remediation	81

Package Reference	100

General Service User Menu	100

Consult Service Tracking Option	101

Completion Time Statistics	106

Service Consults Pending Resolution	107

Consult Status	108

Actions	112

Brief Action Descriptions	112

Add Comment (CM) Action	115

Cancel (or Deny) Consult	116

Change View (CV) Action	118

Complete Request (CT) Action	119

Deny Request (DY) Action	119

Detailed Order Display (DD) Action	120

Discontinue Order (DC) Action	124

Edit/Resubmit (ER)   Action	126

Forward Request (FR) Action	126

Make Addendum (MA) Action	126

Print Form (PF) Action	126

Print Screen Contents (PS) Action	127

Quit (Q) Action	127

Receive Request (RC) Action	128

Remove Medicine Results (RM)	130

Results Display (RT) Action	131

Schedule (SC) Action	132

Select New Patient (SP) Action	134

Significant Findings (SF) Action	136

Notifications about Consults and Requests	138

Enabling Notifications	143

New Service Consult/Request	146

Consult/Request Resolution	149

Consult/Request Updated	150

Consult/Request Cancel/Hold	151

Consult/Request Has an Added Comment	154

Order(s) Require Electronic Signature	155

Significant Findings for a Consult	156

Prosthetics Consult Updated	156

ADMIN KEY Reports	156

UCID Display	163

Cancelled to Discontinued Consults	163

Glossary	165

Index	167


## Introduction

The *Consult/Request Tracking User Manual* provides descriptions of Consults’ options and other information required to effectively use the Consult/Request Tracking package (or Consults).

This manual is for people who use the Consults package in the course of their hospital duties, including:

Care providers: doctors, nurses, pharmacists, and therapists who make or service requests for consultations on patients.

Clerical staff, who assist the above-mentioned people.

Quality Assurance and management, who have an interest in seeing that VA patients receive the best possible care.

Consults functionality is available from a Windows interface (GUI—Graphical User Interface) on a PC workstation or from a roll-and-scroll List Manager (LM) interface on a traditional CRT (Cathode Ray Tube) terminal or terminal emulation software on a PC workstation.

You can pull out parts of this manual, such as the **User Introduction to GUI** section or the **Package Operation** section, to use for unit training or reference. General parts of this manual, such as the **Package Orientation** section, have been written with examples from Consults to make the general information more meaningful to this application.

### Overview

#### Purpose

Consult/Request Tracking package V. 3.0 improves the quality of patient care by:

Interfacing with CPRS to provide an efficient mechanism for clinicians to order consults and procedure requests.

Providing consulting services with the ability to update and track the progress of a consult/procedure request from the point of receipt through its final resolution.

Providing results reporting that includes doctor's notes and comments entered during the tracking process.

#### Relationship to Other Packages

The Consults package works with the following packages:

Computerized Patient Record System (CPRS)

Text Integration Utilities (TIU)

##### Relationship of Consults to CPRS

###### From CPRS Actions to Consults:

Ordering

Order checking

Order updates via HL7 messages

Inter-Facility Consults via HL7 messages

Tracking Consults activity

Resulting  TIU and Consults

Notifications

###### From Consults actions to CPRS:

Consult status changes update the CPRS order

Forwarded and edit/resubmitted consults get a new service/correction order from CPRS

Sends alerts based on consult activity

Auto-forwarding of Consult Orders to new Consult text

##### Relationship of Consults to TIU

###### From TIU Actions to Consults:

Select a consult to associate with a note

One consult link per consult note

Sends TIU updates to consult package for:

New consult note entered

Consult note completed

New addendum completed

Disassociate a note

Extract notes for SF 513 and displays

###### From Consult Actions to TIU:

A consult may have multiple notes associated with it.

Lists the notes associated with a consult.

Uses TIU to act on a note.

Updates consult status and activity log from TIU updates.

### Enhancements since Version 2.5

#### GMRC*3.0*145

This patch, part of the larger CPRS GUI v31 Mission Act release, assists with implementing the Decision Support Tool (DST) and Consult Toolbox (CTB) directly into CPRS GUI. Please consult the DST and CTB user manuals on the VistA Document Library for detailed information regarding use of these features.

#### GMRC*3.0*139

This patch adds Auto-forwarding functionality. When the Decision Support Tool (DST) transmits the Auto-forward information to CPRS, the existing CPRS RPC process will detect the Auto-forward request and forward the Order to a new Consult location, which is referenced in the REQUEST SERVICE file (#123.5).

##### General Overview of Consults/Request Tracking

Consults can be accessed through Windows NT, Windows 95, or a later Microsoft Windows version with the CPRS GUI Interface or through the List Manager (LM) interface.

Consult ordering is managed by CPRS Order Entry from within the CPRS Order tab. This includes Quick Orders.

Consult resulting is based on TIU Consult Notes, Medicine package results, and provider comments.

Services must be defined within the ALL SERVICES hierarchy in order to access their consults and requests.

Tracking services are not orderable unless the user is an update user for the service or its parent service.

The ordering provider may edit and resubmit a consult after it has been canceled.

##### Alert Actions

Users can process consult service update actions from the alert.

The recipient of an alert for a cancelled request can edit and resubmit the request from the alert .

##### Reporting

The Standard Form 513 is based on a hard-coded consults routine instead of the OE/RR Print Formats. This facilitates results printing when the consult reaches final resolution.

A report with completion time statistics has been added.

A report with pending consults has been added.

Lists of consults can be viewed by order status, service, and/or date range.

##### Communications

HL7 messages and protocols are the communications medium between CPRS and Consults.

##### Setup

Consult services have a related entry in the CPRS Orderable Items file (#101.43).

Management of procedures and services must be done through Consult options.

### Relations with other VistA Components

The Consults package communicates with CPRS through HL7 messages. Order Checking receives information from the Consults package through CPRS. Notifications is the only major package that Consults communicates with directly. When the requesting clinician signs the order, Consults sends a notification to the consulting physician and when the consulting physician signs the final report, Consults sends a notification to the requesting physician.

<!-- image -->

Inter-Facility Consults (IFC) are requested, acted upon, and viewed the same way as regular Consults. Typically consults that are handled at a different facility have the remote facility indicated in their title, such as “Eye Exam—Salt Lake.” The software uses HL7 messaging in the background to communicate inter-facility consults and actions between cooperating facilities. Results are filed at the resulting facility, but since CPRS uses Remote Data Views in the background to access the results, users do not need to treat Inter-Facility Consults any differently.

### Related Manuals and Other References

If you are an ADPAC or IRM personnel, the *Consult/Request Tracking Technical Manual* would probably aid in your understanding of Consults setup and operation.

Consults is installed with CPRS, so the *CPRS Installation Guide* is the appropriate manual to refer to on installation issues that aren’t covered in the *Consult/Request Tracking Technical Manual* .

TIU provides boilerplate text and other text-oriented services. The *TIU Clinical Coordinator &amp; User Manual* would assist you in using these features.

Consults package is highly integrated with CPRS. As such, any Consults package user should be familiar with the *CPRS Clinician’s Getting Started Guide* and the *CPRS Clinical Coordinator &amp; User Manual.*

See our web pages at: REDACTED


## Package Management

### Service Update and Tracking Security

Your ADPAC can use the Consult Service User Management option, in conjunction with availability to various menus and options, to control access to Consults functionality. The menus that can be provided to you are:

#### Consult Service Tracking

The Consult Service Tracking menu provides access to basic consult tracking functions and reports but can also provide complete update capabilities if you have been granted update privileges by your ADPAC.

Individual options in the Consults package that may be useful to you, and what access they provide, are detailed in the following table:

| Option                              | Services                                                                        |
|-------------------------------------|---------------------------------------------------------------------------------|
| Consult Service Tracking            | Tracking and/or update functionality depending upon your individual privileges. |
| Completion Time Statistics          | Reporting.                                                                      |
| Service Consults Pending Resolution | Reporting.                                                                      |

With the GMRC Service User Management option, your ADPAC can set you up to be an update user for one or more services at your hospital. In addition, the ADPAC can grant the ability to receive consult notifications according to criteria outlined in the following table:

| Category                                          | Notifications Received                                                                   |
|---------------------------------------------------|------------------------------------------------------------------------------------------|
| UPDATE USERS W/O NOTIFICATIONS                    | Unless otherwise set up, will not receive notifications.                                 |
| UPDATE TEAMS W/O NOTIFICATIONS                    | Unless otherwise set up, will not receive notifications.                                 |
| UPDATE USER CLASS W/O NOTIFS                      | Unless otherwise set up, will not receive notifications.                                 |
| SERVICE INDIVIDUAL TO NOTIFY                      | Receive consult notifications for your service.                                          |
| SERVICE TEAM TO NOTIFY                            | Receive consult notifications for patients assigned to your team.*                       |
| NOTIFICATION BY PT LOCATION  INDIVIDUAL TO NOTIFY | Receive all consult notifications for your service for patients in a specified ward.     |
| NOTIFICATION BY PT LOCATION  TEAM TO NOTIFY       | Receive consult notifications for patients assigned to your team and in a specified ward |
| SPECIAL UPDATES INDIVIDUAL                        | An individual who has privileges to perform group status updates.                        |

These categories are not mutually exclusive, meaning you may receive notifications based on being present on one or more of the lists detailed in the foregoing table.

* NOTE: The service team does not receive the CONSULT/REQUEST UPDATED notification if another member of that team or an update user is the user adding the comment

| Privilege               | Granted                       |
|-------------------------|-------------------------------|
| Originate a consult     | Anyone with access to CPRS    |
| Sign a consult          | Anyone who can sign an order  |
| Change a consult status | Anyone with update privileges |
| View or print a consult | Anyone with access to CPRS    |

In summary, update user capabilities vary depending on

The option(s) that you are assigned.

Privileges granted in the Consults Service User Management option.


## Package Operation

The operation of the Consults package involves multiple people, at various skill levels, in various parts of the hospital. A consult request may be entered by a clinician or a clerk under a clinician’s direction. This request acts as a depository of information about itself.

It collects notes and keeps records on everything that happens to it. When complete it becomes part of the patient’s medical record.

In the pages that follow, we present this flow of information, and show the actions that must be taken at each step in the process. Many of these actions must be taken by persons other than those originating the consult.

Also, Consults uses CPRS during the initiation process and TIU during the completion process. In this section, we give some information about each of these packages that may help you in using Consults.

### Workflow

**1. The clinician orders a consult.** While in a patient's CPRS medical record, a clinician enters an order for a consultation or procedure.

**2. The consult service gets a written copy.** An alert and a hard-copy of the SF 513 are sent to the consult service.

**3. If accepted, an appointment is held.** To accept the consult, the service uses the **receive** action. The service can also **discontinue** or **cancel** the consult. Cancelled consults can be edited and re-submitted by the ordering clinician.

**4. Results are entered and signed.** The consult service enters results and comments. Resulting is primarily done using TIU.

**5. The originating clinician receives an alert that the consult is complete.** The results can now be examined and further action taken on behalf of the patient.

**6. The SF 513 report becomes part of the patient’s medical record.** A hard copy can be filed, and the electronic copy is online for paperless access.

*NOTE: Under the Care Coordination (CC) Decision Support Tool (DST) project, the release of Patch GMRC*3.0*124 modifies the above workflow. The workflow changes effective with the installation of this patch will only impact users of DST. For further information regarding the workflow process for DST users, please refer to the DST User Guide, which can be found in the VA Software Document Library (VDL) under [CPRS: Consult/Request Tracking](https://www.va.gov/vdl/application.asp?appid=62) .

<!-- image -->

#### The Clinician Orders a Consult

Consult orders can be entered:

From the CPRS medical record screen, Consults tab

CPRS GUI interface program, Consults tab

##### Ordering Within the CPRS Package

Primarily, Consult orders should be placed through the CPRS Add New Orders action.

In this manual we provide a step-by-step display of the process for ordering consult or procedures requests through the CPRS package. We first go through a brief list of steps, then we discuss each step in detail.

##### To Order a Consult:

A.	Select CPRS Clinician Menu (OE) from the Clinician Menu.

B.	Select the patient.

C.	Select Chart Contents, and then Consults.

D.	Select Order New Consult.

E.	Answer questions on the particulars of the request.

To go over in detail how to order a consult:

##### A.	Select CPRS Clinician Menu (OE) from the Clinician Menu

Exactly how you do this option depends on how IRM or your ADPAC set up your menu. This example shows one way of performing step A.

Select Clinician Menu Option: ?

OE     CPRS Clinician Menu

RR     Results Reporting Menu

AD     Add New Orders

RO     Act On Existing Orders

PP     Personal Preferences ...

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Clinician Menu Option: **OE**

The screen now looks like this:

Patient Selection             Apr 07, 1999 14:51:30           Page:   1 of  1

Current patient: ** No patient selected **

Patient Name                   ID        DOB            Room-Bed

No patients found.

Enter the number of the patient chart to be opened                 &gt;&gt;&gt;

+   Next Screen           CV  Change View ...       FD  Find Patient

-   Previous Screen       SV  (Save as Default List)Q   Close

Select Patient: Change View //

##### B.	Select the Patient

Select the patient as you would in any other package. Type a patient ID such as the patient's name, social security number, or the patient's last initial followed by the last 4 digits of the social security number. If more than one patient matches the key you entered, select the patient from the list presented on the screen.

Select Patient: Change View // **C2342**

1   C2342  CPRSPATIENT,TWO       03-04-32     666902342      MILITARY RETIREE

2   C2342  CPRSPATIENT,TWELVE    02-03-23     666242342      MILITARY RETIREE

CHOOSE 1-2: **2** CPRSPATIENT,TWELVE        02-03-23   666242342     MILITARY RETIREE

Searching for the patient's chart ...

(Continued on the next page.)

The screen now looks something like this:

Cover Sheet                   Feb 13, 1999 12:53:14        Page:    1 of    2

CPRSPATIENT,TWELVE 666-24-2342              1A/B-1      FEB 3,1923 (74)   &lt;CA&gt;

PrimCare: CPRSProvider, Three                   PCTeam: GOLD

Item                                         Entered

Allergies/Adverse Reactions                |

1    BEESWAX (hives, itching, watering eyes,     | 03/28/97

anxiety)                                   |

|

Patient Postings                           |

2    CRISIS NOTE                                | 02/25/97 12:18

|

Recent Vitals                              |

No data available                          |

|

Immunizations                              |

No immunizations found.                    |

|

Eligibility                                |

Not Service Connected                      |

+         Enter the numbers of the items you wish to act on.                 &gt;&gt;&gt;

NW  Enter New Allergy/ADR CV  (Change View ...)     SP  Select New Patient

AD  Add New Orders        CC  Chart Contents ...    Q   Close Patient Chart

Select: Next Screen//

##### C.	Select Chart Contents, then Consults

To get to the menu containing Order New Consults, you must go through the Chart Contents menu, then select the Consults screen. This can be done in one step by typing:

CC;CON

All Consults                  Feb 13, 1998 12:56:32          Page:   1 of   1

CPRSPATIENT,TWELVE 666-24-2342              1A/B-1      FEB 3,1923 (74)   &lt;CA&gt;

PrimCare: CPRSProvider, Three                   PCTeam: GOLD

Consult/Procedure                            Requested       Status

1    CARDIOLOGY Consult                         | 02/25/97 11:02  complete

Enter the numbers of the items you wish to act on.                 &gt;&gt;&gt;

NW  Enter New Allergy/ADR CV  (Change View ...)     SP  Select New Patient

AD  Add New Orders        CC  Chart Contents ...    Q   Close Patient Chart

Select: Chart Contents//

##### D.	Select Order New Consult

Type NW and press the &lt;Enter&gt; key.

##### Answer Questions on the Particulars of the Request

Select: Chart Contents// **NW** Order New Consult

Consult                   Procedure

Order new: **C** Consult

Delay release of these orders? NO// **&lt;Enter&gt;**

Consult to Service/Specialty: **POD** FOOT CLINIC   FOOT CLINIC

Reason for Request:

1&gt;PERSISTENT SMALL FISSURES AND SCALING ON BOTH FEET.

2&gt;

EDIT Option:

Category: INPATIENT// **&lt;Enter&gt;**

Urgency: ROUTINE// **??**

Select from:

1 STAT

2 ROUTINE

3 WITHIN 48 HOURS

4 WITHIN 72 HOURS

5 EMERGENCY

Select the urgency indicating how quickly results from this consult are needed.

Urgency: ROUTINE// &lt;Enter&gt;

Clinically indicated date:TODAY// &lt;Enter&gt;

If the request is for a future service, such as an EKG in 6 months, then enter the future date here.

<!-- image -->

Select from:

1 Bedside

2 Consultant's Choice

Select the preferred place to see the patient for this consult.

Place of Consultation: Bedside// &lt;Enter&gt;

Attention: **CPRSPROVIDER,TH** REE           CT          PHYSICIAN

Provisional Diagnosis: **TINEA PEDIS**

-------------------------------------------------------------------------------

Consult to Service/Specialty: Podiatry

Reason for Request: PERSISTENT SMALL FISSURES AND SCALING ON ...

Category: INPATIENT

Urgency: ROUTINE

Place of Consultation: Bedside

Attention: CPRSPROVIDER,THREE

Provisional Diagnosis: TINEA PEDIS

-------------------------------------------------------------------------------

(P)lace, (E)dit, or (C)ancel this order? PLACE// &lt;Enter&gt;

... order placed.

Add another Consult order? NO//

(Continued on the next page.)

The screen now looks something like this:

All Consults                  Feb 13, 1998 12:58:32            Page:   1 of   1

CPRSPATIENT,TWELVE 666-24-2342              1A/B-1      FEB 3,1923 (74)   &lt;CA&gt;

PrimCare: CPRSProvider, Three                   PCTeam: GOLD

Consult/Procedure                            Requested       Status

1    CARDIOLOGY Consult                         | 02/25/97 11:02  complete

Enter the numbers of the items you wish to act on.                 &gt;&gt;&gt;

NW  Enter New Allergy/ADR CV  (Change View ...)     SP  Select New Patient

AD  Add New Orders        CC  Chart Contents ...    Q   Close Patient Chart

Select: Chart Contents//

Notice that the consult just entered is not yet displayed. It is not displayed until after you have signed the order.

##### Sign the Consult

Enter your electronic signature here.

<!-- image -->

+   Next Screen                        $   Sign All Orders

-   Previous Screen                    Q   Close

Select: Sign All Orders// **$** Sign All Orders

Enter your Current Signature Code:    SIGNATURE VERIFIED

Processing orders ...

When applied to an approved medical record, an electronic signature has the same legal weight as a signature made with a pen on paper. For this reason, electronic signatures are part of the overall security system maintained by IRMS.

When the computer prints a document that has been signed and/or cosigned, an electronic signature block is included. What appears in this block is user configurable through the User’s Toolbox option.

In this example we change a title and electronic signature:

Select Consult Service Tracking Option: **??**

CS     Consult Service Tracking [GMRC SERVICE TRACKING]

PC     Service Consults Pending Resolution [GMRC RPT PENDING CONSULTS]

ST     Completion Time Statistics [GMRC COMPLETION STATISTICS]

Or a Common Option:

CWA    Patient Warning (CWAD) Display [GMRPNCW]

MA     MailMan Menu ... [XMUSER]

TBOX   User's Toolbox ... [XUSERTOOLS]

VA     View Alerts [XQALERT]

Continue [XUCONTINUE]

**&gt; Reverse lock ZZLUKE

Halt [XUHALT]

Restart Session [XURELOG]

Time [XUTIME]

Where am I? [XUSERWHERE]

You have PENDING ALERTS

Enter  "VA   VIEW ALERTS     to review alerts

Select Consult Service Tracking Option: **TBOX** User's Toolbox

Select User's Toolbox Option: **?**

Display User Characteristics

Edit User Characteristics

Electronic Signature code Edit

Menu Templates ...

Spooler Menu ...

Switch UCI

TaskMan User

User Help

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select User's Toolbox Option: **EL** ectronic Signature code Edit

This option is designed to permit you to enter or change your Initials,

Signature Block Information, Office Phone number, and Voice and

Digital Pagers numbers.

In addition, you are permitted to enter a new Electronic Signature Code

or to change an existing code.

INITIAL: CRS// **&lt;Enter&gt;**

The electronic signature is typed here.

<!-- image -->

SIGNATURE BLOCK TITLE: DOCTOR// **MD**

OFFICE PHONE: 555- **588-5000**

ANALOG PAGER: **4038**

DIGITAL PAGER: **&lt;Enter&gt;**

Enter your Current Signature Code:    SIGNATURE VERIFIED

The new signature is typed here.

<!-- image -->

Your typing will not show.

ENTER NEW SIGNATURE CODE:

RE-ENTER SIGNATURE CODE FOR VERIFICATION:

DONE

And here.

<!-- image -->

Select User's Toolbox Option:

***NOTE:** CONCERNING SPACES IN LAST NAMES OF PROVIDERS SIGNING CONSULTS

Providers with last names in VistA containing spaces who sign Consults – especially Inter-Facility Consults – should have spaces removed from their VistA last name.  In certain situations, spaces in the provider’s  VistA last name may cause IFC Consults to fail to complete.  Removing spaces from the VistA last will prevent this problem.  Space removal can be accomplished two ways:  by combining the parts of the last name or including a hyphen.  For example, the name "DE LUCA" should be changed to "DELUCA".  Another example:  the unhyphenated last name "JONES SMITH" should be changed to "JONES-SMITH".  Please contact your facility system access coordinator with your request to edit your VistA last name.  Space removal is also recommended as part of VA name standardization; more details are described by Kernel patches XU*8*134 and XU*8*343.

* **NOTE** : If the SIGNATURE BLOCK PRINTED NAME and SIGNATURE BLOCK TITLE fields are disabled at your site, contact your supervisor to request entry of your name and title.

The signature block, as changed in the example above, looks like this:

/es/CPRSPROVIDER,SEVEN

MD

The /es/ annotation indicates that the medical document was electronically signed

If for some reason you do not sign an order at the time you write it, then the system enters the order into your list of alerts. Signing the order is then simply a matter of responding to the alert as in the following example:

You have PENDING ALERTS

Enter  "VA   VIEW ALERTS     to review alerts

Select OE/RR Manager Menu Option: **VA** View Alerts

1.  CPRSPATIE (C0999): Order requires electronic signature.

2.  TIUPATIEN (T3456): New  Consult/Request (Stat)

Select from 1 to 2

or enter ?, A I, F, P, M, R, or ^ to exit: 1

Searching for the patient's chart ...

Unsigned Orders            Feb 13, 1999 13:01:58       Page:    1 of    1

CPRSPATIENT,TWELVE 666-24-3456              1A/B-1      FEB 3,1923 (74)   &lt;CA&gt;

PrimCare: CPRSProvider, Three                   PCTeam: GOLD

Item Ordered                              Requestor Start Stop Sts

1    CT ABDOMEN W&amp;W/O CONT *UNSIGNED*        | CPRSPROVIDER,THREE   unr

2    Discontinue CBC BLOOD WC LB# 269        | CPRSPROVIDER,TEN     unr

*UNSIGNED*                              |

3    Change SODIUM SERUM SERUM WC to GLUCOSE |                      pend

SERUM SERUM SP LB# 242 *UNSIGNED*       |

4    Change GLUCOSE SERUM SERUM SP to        |                      pend

POTASSIUM SERUM SERUM SP LB# 242        |

*UNSIGNED*                              |

Enter the numbers of the items you wish to act on.            &gt;&gt;&gt;

+   Next Screen           -   Previous Screen       Q   Quit

Select:Quit// 1

Unsigned Orders            Feb 13, 1998 13:02:58       Page:    1 of   1

CPRSPATIENT,TWELVE 666-24-2342              1A/B-1      FEB 3,1923 (74)   &lt;CA&gt;

PrimCare: CPRSProvider, Three                   PCTeam: GOLD

Item Ordered                              Requestor Start Stop Sts

1    CT ABDOMEN W&amp;W/O CONT *UNSIGNED*        | CPRSPROVIDER,THREE   unr

2    Discontinue CBC BLOOD WC LB# 269        | CPRSPROVIDER,TEN     unr

*UNSIGNED*                              |

3    Change SODIUM SERUM SERUM WC to GLUCOSE |                      pend

SERUM SERUM SP LB# 242 *UNSIGNED*       |

4    Change GLUCOSE SERUM SERUM SP to        |                      pend

POTASSIUM SERUM SERUM SP LB# 242        |

*UNSIGNED*                              |

Enter the numbers of the items you wish to act on.            &gt;&gt;&gt;

Change                                  Sign

Discontinue                             Detailed Display

Select action: S   Sign

-- CT ABDOMEN W&amp;W/O CONT  --

Enter your Current Signature Code:    SIGNATURE VERIFIED

The electronic signature is typed here.

<!-- image -->

CT ABDOMEN W&amp;W/O CONT  signed.

Print CHART COPY for the orders: YES// **&lt;Enter&gt;** YES

DEVICE: LTA35// **&lt;Enter&gt;** C-ITOH 300 LINE PRINTER

DO YOU WANT YOUR OUTPUT QUEUED? NO// **&lt;Enter&gt;** (NO)

Unsigned Orders            Feb 13, 1998 13:03:58     Page:    1 of    1

CPRSPATIENT,TWELVE 666-24-2342              1A/B-1      FEB 3,1923 (74)   &lt;CA&gt;

PrimCare: CPRSProvider, Three                   PCTeam: GOLD

Item Ordered                              Requestor         Start Stop  Sts

1    CT ABDOMEN W&amp;W/O CONT *UNSIGNED*        | CPRSPROVIDER,ONE               unr

2    Discontinue CBC BLOOD WC LB# 269        | CPRSPROVIDER,TWO               unr

*UNSIGNED*                              |

3    Change SODIUM SERUM SERUM WC to GLUCOSE |                                pend

SERUM SERUM SP LB# 242 *UNSIGNED*       |

4    Change GLUCOSE SERUM SERUM SP to        |                                pend

POTASSIUM SERUM SERUM SP LB# 242        |

*UNSIGNED*                              |

Enter the numbers of the items you wish to act on.            &gt;&gt;&gt;

+   Next Screen           -   Previous Screen       Q   Quit

Select:Quit// &lt;Enter&gt;  Quit

#### The Consult Service Gets a Written Copy

The consult service receives an alert and a printed SF 513. The Consultation Form is automatically generated in the receiving clinic when the requesting physician signs the order. (In the case of Inter-Facility Consults, the request in routed to the resulting facility and printed there.) A Secondary Printer can be configured in VistA (see the *Consult/Request Tracking Technical Manual* for instructions). When configured, this automatically prints the SF 513 to both services whenever printing is requested.

**Caution:** The Consultation Form (SF 513) generated by this package for use by the receiving services is highly confidential and should be treated with the same security precautions as other patient medical record documents.

The computerized consultation form created and printed by this package may only be placed in a patient’s medical record, as a valid medical form, *if* it has been authorized for medical record use by the Medical Records Committee at your facility.

--------------------------------------------------------------------------------

MEDICAL RECORD                   |     CONSULTATION SHEET

--------------------------------------------------------------------------------

CPRSPATIENT,NINETY

XXX-XX-9200     02/03/1904  (Age 113)  		NSC VETERAN

CV ELIGIBLE

Cell: (000) 555-1919

--------------------------------------------------------------------------------

Consult Request: Consult                         |Consult No.: 10943

--------------------------------------------------------------------------------

To: CARDIOLOGY

From: 2B MED                                |Requested: 08/24/2009 11:00 am

--------------------------------------------------------------------------------

Requesting Facility: BOISE                   |ATTENTION: CPRSPROVIDER,SEVEN

================================================================================

REASON FOR REQUEST: (Complaints and findings)

Patient has a Hx of hypertrophic cardiomyopathy Dx'ed 3 years ago and

seems to be somewhat stable.  Lung fields appear slightly edematious on

Chest X-Ray and we need an assessment of cardiac function prior to

increasing Digitalis dosages.

--------------------------------------------------------------------------------

PROVISIONAL DIAG: Cardiomyopathy, Hypertrophic (425.1)

--------------------------------------------------------------------------------

REQUESTED BY:                      |PLACE:                 |URGENCY:

CPRSPROVIDER,TEN                   |Bedside                |Routine

PHYSICIAN                          |                       |

(Pager: )                          |SERVICE RENDERED AS:   | Clinically Indicated

date:

(Phone: )                          |Inpatient              | Jan 31, 2011

--------------------------------------------------------------------------------

W O R K I N G   C O P Y

No Consultation Results available.

================================================================================

AUTHOR &amp; TITLE:                                       |

|DATE:

--------------------------------------------------------------------------------

ID #:\_\_\_\_\_\_\_|ORGANIZATION:            BOISE  |REG #:\_\_\_\_  |LOC: 2B MED

--------------------------------------------------------------------------------

Standard Form 513 (Rev 9-77)

#### If Accepted, an Appointment is Held

It is fairly common for a consult to be sent to the wrong clinic. For this reason, it is very easy to forward a consult to another clinic. Simply use the FR (Forward Request) action to specify the new receiving clinic.

In this example, a Neurology consult is forwarded to Psychiatry at the discretion of the consulting physician:

Select OPTION NAME: **ORMGR** OE/RR Manager Menu      menu

You have PENDING ALERTS

Enter  "VA   VIEW ALERTS     to review alerts

Select OE/RR Manager Menu Option: **VA** View Alerts

1.I  CPRSPATIE (C3779): Critical High Lab: LITHIUM 5 02/06 10:51

2.   ARTPATIEN (A9600): New  Consult/Request (Today)

Select from 1 to 12

or enter ?, A I, F, P, M, R, or ^ to exit: **2**

Consult/Request Alerts      Feb 13, 1999 13:06           Page: 1 of  1

CPRSPATIENT,TWELVE 666-24-3779              1A/B-1      FEB 3,1923 (74)   &lt;CA&gt;

Ward: 2B MED

Requested  St     No.   Consult/Procedure Request

185  02/12/97   p      1636  NEUROLOGY Consult

Enter ?? for more actions

RC Receive                CM Add Comment            DD Detailed Display

FR Forward                CT Complete/Update        RT Results Display

CX Cancel (Deny)          MA Make Addendum          PF Print Form 513

DC Discontinue            SC Schedule

Select Action: Quit// **FR** Forward Consult

Forward Request To Another Service For Action.

Select the service to send the consult to.

Forward Consult to which Service/Specialty: **PSY** CHIATRY

Who is responsible for Forwarding the Consult: **CPRSPROVIDER,SE** VEN    CS     HYN

Actual Date/Time of Activity: NOW//   (Feb 13, 1999@14:24)

Urgency: Today// **&lt;Enter&gt;** Today

Enter COMMENT:

1&gt; List of symptoms indicates Psychiatry would give better work up.

2&gt; &lt;Enter&gt;

EDIT Option: **&lt;Enter&gt;**

(Continued on the next page.)

Consult/Request Alerts      Feb 13, 1998 13:07          Page:  1 of  1

CPRSPATIENT,TWELVE 666-24-3779              1A/B-1      FEB 3,1923 (74)   &lt;CA&gt;

Number    Date  Stat  Service           Procedure

185  02/12/97 p     PSYCHIATRY        Consult

Enter ?? for more actions

RC Receive                CM Add Comment            DD Detailed Display

FR Forward                CT Complete/Update        RT Results Display

CX Cancel (Deny)          MA Make Addendum          PF Print Form 513

DC Discontinue            SC Schedule

Select Action: Quit//

##### Receive the Consult

Performing the Receive action on a consult changes its status from Pending to Active. This puts your clinic on record as accepting responsibility for completing the consult.

There are two ways to receive a consult:

From a consult tracking screen.

From a notification alert of a new consult. See page 128 for an example of this method.

In the following example, we receive a consult from a consult tracking screen:

CONSULT TRACKING              Oct 05, 2000 09:18:22          Page:    1 of    1

CPRSPATIENT,TWELVE 666-24-3779              1A/B-1      FEB 3,1923 (74)   &lt;CA&gt;

Wt.(lb): No Entry

Requested  St     No.   Consult/Procedure Request

1   05/06/97   p       226  PSYCHIATRY Cons

Enter ?? for more actions

SP Select Patient   FR Forward          CT Complete/Update  RT Results Display

CV Change View ...  CX Cancel (Deny)    MA Make Addendum    PF Print Form 513

RC Receive          DC Discontinue      SF Sig Findings     RM Remove Med Rslt

SC Schedule         CM Add Comment      DD Detailed Display ER Edit/Resubmit

Select: Quit// **RC** Receive Request

Who received it?: **CPRSPROVIDER,SE** VEN         CS

Date/Time Actually Received: NOW// **&lt;Enter&gt;** (NOV 01, 1997@09:05)

Enter COMMENT...

1&gt;Pt will be seen ASAP

2&gt; &lt;Enter&gt;

EDIT Option: **&lt;Enter&gt;**

CONSULT TRACKING              Oct 05, 2000 09:18:22          Page:    1 of    1

CPRSPATIENT,TWELVE 666-24-3779              1A/B-1      FEB 3,1923 (74)   &lt;CA&gt;

Wt.(lb): No Entry

Requested  St     No.   Consult/Procedure Request

1   05/06/97   a       226  PSYCHIATRY Cons

Enter ?? for more actions

SP Select Patient   FR Forward          CT Complete/Update  RT Results Display

CV Change View ...  CX Cancel (Deny)    MA Make Addendum    PF Print Form 513

RC Receive          DC Discontinue      SF Sig Findings     RM Remove Med Rslt

SC Schedule         CM Add Comment      DD Detailed Display ER Edit/Resubmit

Select: Quit//

#### Results are Entered and Signed

The consult service enters results and comments. When you request the Complete (CT) action from the Consults service tracking or CPRS Consults screen, V *IST* A shifts you into TIU.

In the following example, we complete a consult and enter findings through Consult’s link to TIU:

Select Consult Service Tracking Option: **CS** Consult Service Tracking

Select Patient: **CPRSPATIENT,TW** ELVE         05-05-55     666553779     YES     SC

VETERAN

Select Service/Specialty: ALL SERVICES// **PUL** MONARY

List From Starting Date:  ALL DATES // **&lt;Enter&gt;** ALL DATES

CONSULT TRACKING              Oct 05, 2000 09:22:45          Page:    1 of    1

CPRSPATIENT,TWELVE 666-24-3779              1A/B-1      FEB 3,1923 (74)   &lt;CA&gt;

Wt.(lb): 180

Requested  St     No.   Consult/Procedure Request

1   09/04/97   p       319  PULMONARY Cons

Enter ?? for more actions

SP Select Patient   FR Forward          CT Complete/Update  RT Results Display

CV Change View ...  CX Cancel (Deny)    MA Make Addendum    PF Print Form 513

RC Receive          DC Discontinue      SF Sig Findings     RM Remove Med Rslt

SC Schedule         CM Add Comment      DD Detailed Display ER Edit/Resubmit

Select: Quit// **CT** Complete

CHOOSE No. 1-2: **1**

Creating new progress note...

Patient Location:  2B

Date/time of Admission:  10/05/00 09:22

Date/time of Note:  NOW

Author of Note:  CPRSPROVIDER,SEVEN

...OK? YES// **&lt;Enter&gt;**

Calling text editor, please wait...

==[ WRAP ]==[ INSERT ]===&lt; Patient: CPRSPATIENT,TWELVE &gt;===[ &lt;PF1&gt;H=Help ]===

Mr. CPRSPatient’s regimen is lacking in inhaled corticosteroids.  Recognizing

that asthma is an inflammatory process, inhaled steroids are important

in controlling the inflammatory response.  My practice for severely

out-of-control asthmatics is to use high-dose inhaled steroids,

typically vanceril, 16 puffs qid, with a spacing device such as the

Aerochamber. I would institute such a regimen while he is here.

Mr. CPRSPatient has an in-house pet dog and an outside pet cat.  I have

told him that the cat should go, even if it is outdoors.  Cat saliva

contains a glycoprotein that leaves residue on their coats and flakes

into the air; it is problematic for many asthmatics.

The purulent phlegm asthmatics have during exacerbations is usually

due to the eosinophils, not from infection.  Antibiotics are usually

not necessary.

If you like, you may refer Mr. CPRSPatient to my clinic after discharge.

&lt;======T=======T=======T=======T=======T=======T=======T=======T=======T=&gt;=====T

(Continued on next page.)

Your electronic signature is typed here.

<!-- image -->

Enter your Current Signature Code:    SIGNATURE VERIFIED..

Print this note? No// **Y** YES

Do you want WORK copies or CHART copies? CHART// **&lt;Enter&gt;**

DEVICE: HOME// **WORK** OTC

DO YOU WANT YOUR OUTPUT QUEUED? NO// **Y** (YES)

Requested Start Time: NOW// **&lt;Enter&gt;** (Oct 05, 2000 09:23:05)

Request Queued!

CONSULT TRACKING              Oct 05, 2000 09:23:45          Page:    1 of    1

CPRSPATIENT,TWELVE 666-24-3779              1A/B-1      FEB 3,1923 (74)   &lt;CA&gt;

Wt.(lb): 180

Requested  St     No.   Consult/Procedure Request

1   09/04/97   c       319  PULMONARY Cons

Enter ?? for more actions

SP Select Patient   FR Forward          CT Complete/Update  RT Results Display

CV Change View ...  CX Cancel (Deny)    MA Make Addendum    PF Print Form 513

RC Receive          DC Discontinue      SF Sig Findings     RM Remove Med Rslt

SC Schedule         CM Add Comment      DD Detailed Display ER Edit/Resubmit

Select: Quit//

Note:	The Consult Closure Tool in VistA can be used to generate a team list of consults with a pending status that potentially need to be closed. The tool can be configured to search for consults by Clinic, Procedure, Service, and Order Item. The resulting list can be reviewed in CPRS, and consults can be closed using the tool within VistA. The *Consult/Request Tracking Technical Manual* provides instructions on using the tool.

#### The Originating Clinician Receives an Alert that the Consult is Complete

After the consult is complete, Notifications sends an alert (via FileMan Alerts) of the completion. This is done while you are in the menu terminal mode, as such:

CPRSPATIE (C8829): Completed Consult CAR

TIUPATIEN (T2342): Cancelled consult PLM

ARTPATIEN (A9898): Completed Consult GASTROENTEROLOGY

CPRSPATIE (C8831): Completed Consult PLM with Sig Findings

Enter  "VA   VIEW ALERTS     to review alerts

Select Consult Service Tracking Option:

To receive an on-screen report of the results, respond as in the following example:

Select Consult Service Tracking Option: **VA** View Alerts

1.   CPRSPATIE (C8829): Completed Consult CAR

2.   TIUPATIEN (T2342): Cancelled consult PLM

3.   ARTPATIEN (A9898): Completed Consult GASTROENTEROLOGY

4.   CPRSPATIE (C8831): Completed Consult PLM with Sig Findings

Select from 1 to 4

or enter ?, A I, F, P, M, R, or ^ to exit

or RETURN to continue: **3**

Processing alert: TIUPATIEN (T8829): Completed Consult PLM

Consult/Request Alerts        Feb 26, 1999 14:56:57          Page:    1 of    1

TIUPATIENT,TWELVE 666-24-2342              1A/B-1      FEB 3,1923 (74)   &lt;CA&gt;

Wt.(lb): No Entry

Requested  St     No.   Consult/Procedure Request

1   01/08/99   c      1337  PULMONARY Cons

Enter ?? for more actions

SP Select Patient   FR Forward          CT Complete/Update  RT Results Display

CV Change View ...  CX Cancel (Deny)    MA Make Addendum    PF Print Form 513

RC Receive          DC Discontinue      SF Sig Findings     RM Remove Med Rslt

SC Schedule         CM Add Comment      DD Detailed Display ER Edit/Resubmit

Compiling Result Display...

(Continued on next page.)

Here we select the Results Display (RT) action:

Results Display               Feb 26, 1999 14:59:10          Page:    1 of    1\_

TIUPATIENT,TWELVE 666-24-2342              1A/B-1      FEB 3,1923 (74)   &lt;CA&gt;

Consult No.: 1337                                             Wt.(lb): No Entry

------------------------------MEDICINE CS CONSULT------------------------------

Pt should stay away from Oyster Crackers.

Signature: /es/CPRSPROVIDER,SEVEN         Date: FEB 12, 1999@11:35:14

Source Information

Document Status: COMPLETED

Entry Date: FEB 12, 1999@11:32                    Author: CPRSPROVIDER,S

Expected Signer: CPRSPROVIDER,SEVEN         Expected Cosigner: None

Entered By: CRS                           TIU Document #: 5365

Urgency: None

================================================================================

Enter ?? for more actions

Select Action: Quit//

#### The SF 513 Report Becomes Part of the Patient’s Medical Record

After the consult is complete, Consults sends an alert to the requesting physician. The requesting physician can use the Print Report action to obtain a copy of the final Consults report. In the following example, the consult we want to print has already been selected:

CONSULT TRACKING              Feb 13, 1998 13:20:44            Page:   1 of   1

CPRSPATIENT,TWELVE 666-24-3779              1A/B-1      FEB 3,1923 (74)   &lt;CA&gt;

Wt.(lb): 178

Requested  St     No.   Consult/Procedure Request

1   11/01/97   c       675  PULMONARY Consult

2   10/28/97   a       506  &lt;MEDICINE EAST&gt; Consult

3   07/21/97   c       285  PULMONARY Pulmonary Function Test

Enter ?? for more actions

SP Select Patient   FR Forward          CT Complete/Update  RT Results Display

CV Change View ...  CX Cancel (Deny)    MA Make Addendum    PF Print Form 513

RC Receive          DC Discontinue      SF Sig Findings     RM Remove Med Rslt

SC Schedule         CM Add Comment      DD Detailed Display ER Edit/Resubmit

Select: Quit// **PT** Print Form

Chart Copy (Y/N) Y// **&lt;Enter&gt;**

DEVICE: HOME// **;;9999** HOME

(Continued on next page)

MEDICAL RECORD         |      CONSULTATION SHEET

--------------------------------------------------------------------------------

CPRSPATIENT,FOUR                             SERVICE CONNECTED 50% to 100%

XXX-XX-4442     03/03/1960  Age: 57          SC VETERAN

123 SESAME ST.

APT. 4

SALT LAKE CITY   UTAH      84101 Phone: 000-555-1289 Cell: 000 -555-1010

--------------------------------------------------------------------------------

Consult Request: Consult                               |Consult No.: 675

--------------------------------------------------------------------------------

To: PULMONARY

From: NOT 2B                                |Requested: 11/01/1997 10:13 am

--------------------------------------------------------------------------------

Requesting Facility: ELY                     |ATTENTION: CPRSPROVIDER,TWO ================================================================================

Current Primary Care Provider: CPRSPROVIDER,SEVEN

Current Primary Care Team: GOLD TEAM

REASON FOR REQUEST: (Complaints and findings)

Pt experiences shortness of breath when out of bed.

--------------------------------------------------------------------------------

PROVISIONAL DIAG: CHEESE HANDLER’S LUNG

--------------------------------------------------------------------------------

REQUESTED BY:                      |PLACE:                 |URGENCY:

CPRSPROVIDER,SEVEN                 |Bedside                |Routine

Chief of Surgery                   |                       |

(Pager: 9999)                      |SERVICE RENDERED AS:   |

(Phone: 1234)                      |Inpatient              |

--------------------------------------------------------------------------------

W O R K I N G   C O P Y

CONSULTATION NOTE #2330

TITLE: PULMONARY CS CONSULT

DATE OF NOTE: NOV 01, 1997@10:15:35  ENTRY DATE: NOV 01, 1997@10:15:35

AUTHOR: CPRSPROVIDER,SEVEN   EXP COSIGNER:

URGENCY:                            STATUS: COMPLETED

At the time I went to examine the pt, he was acutely broncho-

spastic and in moderately severe respiratory distress.  I had him

deliver a puff of albuterol with an Aerochamber; his technique was

poor. I then instructed him and delivered an additional four puffs,

which he did with good technique.  He was improved and with a clear

lung exam within a few seconds (though wheezes were still present

on forced expiration).

The pt regimen is lacking in inhaled corticosteroids.  Recognizing

that asthma is an inflammatory process, inhaled steroids are important

in controlling the inflammatory response.  My practice for severely

out-of-control asthmatics is to use high-dose inhaled steroids,

typically vanceril, 16 puffs qid, with a spacing device such as the

Aerochamber. I would institute such a regimen while he is here.

/es/ CPRSPROVIDER,SEVEN

Signed: 11/01/1997 10:17

--------------------------------------------------------------------------------

PROVISIONAL DIAG: Arrhythmia (427.9)

--------------------------------------------------------------------------------

REQUESTED BY:                      |PLACE:                 |URGENCY:

CASEY,BEN                          |Bedside                |Routine

CHIEF OF SURGERY                   |                       |

(Pager: )                          |SERVICE RENDERED AS:   |CLINICALLY INDICATED DATE:

(Phone: )                          |Inpatient              |Jan 31, 2011

-------------------------------------------------------------------------------

See page 126 for details on the Print Report (PR) action.

### Quick Orders

Quick Orders are a feature of CPRS that allow certain prompts to be automatically filled in by the computer. Your ADPAC can set them up (a subject that is discussed in the *CPRS Setup Guide* .)

CPRS is shipped with a number of quick orders. Number 91, EKG, Portable on the screen pictured below is one of them. These quick orders do not have any of the fields filled in. They are only provided as place-holders and limited examples of what is possible.

Add New Orders                Feb 13, 1998 13:21:08          Page:   1 of   1

CPRSPATIENT,TWELVE 666-24-3779              1A/B-1      FEB 3,1923 (74)   &lt;CA&gt;

0  ORDER SETS...          30 PATIENT CARE...        70 LABORATORY...

1  Patient Movement       31 Condom Catheter        71 Chem 7

2  Diagnosis              32 Guaiac Stools          72 T&amp;S

3  Condition              33 Incentive Spirometer   73 Glucose

4  Allergies              34 Dressing Change        74 CBC w/Diff

75 PT

10 PARAMETERS...          40 DIETETICS...           76 PTT

11 TPR B/P                41 Regular Diet           77 CPK

12 Weight                 42 Tubefeeding            78 CPK

13 I &amp; O                  43 NPO at Midnight        79 LDH

14 Call HO on                                       80 Urinalysis

50 IV FLUIDS...           81 Culture &amp; Suscept

20 ACTIVITY...            51 OUTPATIENT MEDS...

21 Ad Lib                 55 INPATIENT MEDS...      90 OTHER ORDERS...

23 Bed Rest / BRP                                   91 EKG: Portable

24 Ambulate TID           60 IMAGING ...

25 Up in Chair TID        61 Chest 2 views PA&amp;LAT   99 Text Only Order

Enter the number of each item you wish to order.                   &gt;&gt;&gt;

+   Next Screen           TD  Set Delay ...         Q   Done

Select Item(s): Done//

Basically, quick orders supply stock answers to some of the prompts required to make an order. For example, if we filled in the values for the placeholder EKG, Portable, we might answer the following questions in the quick order template:

Consult to Service/Specialty: **Cardiology**

Category: **Inpatient**

Place of Consult: **Bedside**

These three prompts are then excluded when you select EKG from the orders screen—relieving you of the necessity of filling in answering several prompts.

The other four prompts, Reason for the Request, Urgency, Attention, and Provisional Diagnosis, are all left blank in the quick order template. The answer to these questions change every time we place an order for a portable EKG. These four questions are the only ones asked when you place an order for “EKG, Portable.”

### Using the Consults Package with TIU

#### Direct TIU Input

On page 26 are the directions for entering results from the Consult/ Result Tracking screen. You can also enter results directly from TIU. This may be preferable if you are doing large volumes of consults or it fits your office work flow.

The basic steps to entering findings through TIU given here are. The interested user should look at the *TIU Clinical Coordinator &amp; User Manual* for further information.

##### From TIU, choose Integrated Document Management.

As with almost everything in V *IST* A, exactly how you do this depends on how your system is set up. If you cannot find this option on your menu, consult your ADPAC.

Example:

Select Progress Notes/Discharge Summary [TIU] Option: **?**

1      Progress Notes User Menu ...

2      Discharge Summary User Menu ...

3      Integrated Document Management ...

4      Personal Preferences ...

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Progress Notes/Discharge Summary [TIU] Option: **3** Integrated Document

Management

--- Clinician's Menu ---

Select Integrated Document Management Option:

##### Select Enter/edit Document.

Example:

Select Integrated Document Management Option: **?**

1      Individual Patient Document

2      All MY UNSIGNED Documents

3      Multiple Patient Documents

4      Enter/edit Document

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Integrated Document Management Option: **E** nter/edit Document

##### Enter the patient’s name.

Follow the usual V *IST* A conventions for selecting a patient.

Example:

Select PATIENT NAME: **CPRSPATIENT,FI** V       03-05-33     666332432     YES     SC VETERAN

A: Known allergies

Select TITLE:

##### Select a document title.

Using the standard help functions (? or ??), you can see a list of titles that are available to you. Consult your supervisor or ADPAC about which one is appropriate to your situation.

Example:

Select TITLE: **?**

Answer with TIU DOCUMENT DEFINITION NAME, or ABBREVIATION, or

PRINT NAME

Do you want the entire TIU DOCUMENT DEFINITION List? **Y** (Yes)

Choose from:

ADVANCE DIRECTIVE      TITLE

ADVERSE REACTION/ALLERGY      TITLE

ASI-ADDICTION SEVERITY INDEX      TITLE

BP TEST NOTE      TITLE

CLINICAL WARNING      TITLE

CRISIS NOTE      TITLE

DISCHARGE SUMMARY      TITLE

MEDICINE CONSULT      TITLE

Select TITLE: **M** EDICINE CONSULT          TITLE

Creating new progress note...

Patient Location:  2B

Date/time of Admission:  05/10/96 10:17

Date/time of Note:  NOW

Author of Note:  CPRSPROVIDER,SEVEN

...OK? YES//

You must link your Result to a Consult Request...

The following CONSULT REQUEST is available:

1. JUL 16, 1997@06:08  278     PULMONARY

CHOOSE 1-1:

##### Choose the consult to enter findings.

TIU lists one or more active consults for the patient. Select the one you have findings for.

Example:

The following CONSULT REQUEST is available:

1. JUL 16, 1997@06:08  278     PULMONARY

CHOOSE 1-1: 1  278

Calling text editor, please wait...

1&gt;

##### Enter and edit findings.

TIU enters the editor specified in your V *IST* A personal preferences. There are a number of alternate ways to enter findings in TIU. Consult the *TIU Clinical Coordinator &amp; User Manual* for details.

Example:

Calling text editor, please wait...

1&gt; No significant findings. Suggest respiratory therapy.

2&gt;

EDIT Option:

Saving MEDICINE CONSULT with changes...

Enter your Current Signature Code:

##### Sign the findings.

At the prompt, enter your signature code. If you do not sign the document at this time, VISTA generates an alert to remind you to sign it at a later time.

There is a detailed discussion of electronic signatures under step 2, *Sign the Consult* .

##### Repeat for other patients.

After TIU accepts your signature, it prompts you for another patient name.

Enter your electronic signature here.

<!-- image -->

Enter your Current Signature Code: SIGNATURE VERIFIED..

You may enter another CLINICAL DOCUMENT. Press RETURN to exit.

Select PATIENT NAME:

Note:	If your site supports the dictation and transcription of Consult results, you may also use the batch upload facility of TIU to support single-point transfer of Consult results in mixed batches (with Discharge Summaries, Progress Notes, etc.) for either in-house or contract transcription services.

#### Correcting Misdirected Results

Occasionally a consult result is linked to the wrong consult. If this is detected prior to signature, it is possible for the author of a consult result to re-direct the record to a different consult request by any of several methods, as illustrated in the examples below:

- Through the Link to Request action, when processing the alert for the unsigned consult result:
- Through the Individual Patient Document option (which is identical to the Browse action, accessible by a number of familiar paths from TIU Clinician's options, or through the CPRS LM Chart).
- You may choose the Link action from the All My Unsigned Documents Option.
- From the CPRS Chart.

Following signature, such corrections can only be made by those persons who are granted permission to do so under the Authorization/ Subscription Utility (ASU). Information on how to make this kind of correction is contained in the Consult/Request Tracking Technical Manual.

Examples:

You may redirect a consult result through the Link to Request action, when processing the alert for the unsigned consult result:

--- Clinician's Menu ---

1      Progress Notes User Menu ...

2      Discharge Summary User Menu ...

3      Integrated Document Management ...

4      Personal Preferences ...

Select Progress Notes/Discharge Summary [TIU] Option: **VA** View Alerts

1.   CPRSPATIE (C0167P): PULMONARY CONSULT available for signature.

2.   ARTPATIEN (A1414): New order(s) placed.

3.   ARTPATIEN (A1414): New consult PLM (Routine)

4.   CPRSPATIE (C2432): New consult CAR (Routine)

Select from 1 to 4

or enter ?, A I, F, P, M, R, or ^ to exit: **1**

Opening PULMONARY CONSULT record for review...

(Continued on the next page.)

Browse Document               Jan 26, 1998 16:49:32        Page:    1 of    1

PULMONARY CONSULT

CPRSPATIENT,T 666-01-0167P  PULMONARY CLINIC     Visit Date: 01/26/98@16:37

DATE OF NOTE: JAN 26, 1998@16:37:34  ENTRY DATE: JAN 26, 1998@16:37:34

AUTHOR: TIUPROVIDER,THREE    EXP COSIGNER:

URGENCY:                            STATUS: UNSIGNED

DEMOGRAPHICS: CPRSPATIENT,TWO

666-01-0167P

31

JAN 1,1967

His disposition is good.

+ Next Screen  - Prev Screen  ?? More actions                    &gt;&gt;&gt;

Find                      Make Addendum             Identify Signers

Print                     Sign/Cosign               Delete

Edit                      Copy                      Link ...

Quit

Select Action: Quit// **L** Link ...

Problem(s)                Patient/Visit             Link with Request

Specify Linkage: **L** Link with Request

You must link your Result to a Consult Request...

The following CONSULT REQUEST(S) are available:

1&gt;  JAN 23, 1998@11:14  759     PULMONARY

2&gt;  JAN 23, 1998@11:14  760     PULMONARY

CHOOSE 1-2: **2** 760

Opening PULMONARY CONSULT record for review...

Browse Document               Jan 26, 1998 16:49:32        Page:    1 of    1

PULMONARY CONSULT

CPRSPATIENT,T 666-01-0167P  PULMONARY CLINIC     Visit Date: 01/26/98@16:37

DATE OF NOTE: JAN 26, 1998@16:37:34  ENTRY DATE: JAN 26, 1998@16:37:34

AUTHOR: TIUPROVIDER,THREE    EXP COSIGNER:

URGENCY:                            STATUS: UNSIGNED

DEMOGRAPHICS: CPRSPATIENT,TWO

666-01-0167P

31

JAN 1,1967

His disposition is good.

+ Next Screen  - Prev Screen  ?? More actions                    &gt;&gt;&gt;

Find                      Make Addendum             Identify Signers

Print                     Sign/Cosign               Delete

Edit                      Copy                      Link ...

Quit

Select Action: Quit// **&lt;Enter&gt;** Quit

(Continued on the next page.)

1.   CPRSPATIE (C2342): New order(s) placed.

2.   TIUPATIEN (T0167P): PULMONARY CONSULT available for signature.

3.   ARTPATIEN (A1414): New order(s) placed.

4.   ARTPATIEN (A1414): New consult PLM (Routine)

5.   CPRSPATIE (C2432): New consult CAR (Routine)

Select from 1 to 5

or enter ?, A I, F, P, M, R, or ^ to exit: **&lt;Enter&gt;**

2.  Through the Individual Patient Document option as shown here (which is identical to the Browse action, accessible by a number of familiar paths from TIU Clinician's options, or through the CPRS LM Chart):

--- Clinician's Menu ---

1      Progress Notes User Menu ...

2      Discharge Summary User Menu ...

3      Integrated Document Management ...

4      Personal Preferences ...

Select Progress Notes/Discharge Summary [TIU] Option: **IN** tegrated Document Management

--- Clinician's Menu ---

1      Individual Patient Document

2      All MY UNSIGNED Documents

3      Multiple Patient Documents

4      Enter/edit Document

Select Integrated Document Management Option: **IN** dividual Patient Document

Select PATIENT NAME: **CPRSPATIENT,TW** O           01-01-67     666010167P       ACTIVE DUTY

A: Known allergies

Available documents:  06/13/91 thru 01/26/98  (7)

Please specify a date range from which to select documents:

List documents Beginning: 06/13/91// **T-1** (JAN 25, 1998)

Thru: 01/26/98// **&lt;Enter&gt;** (JAN 26, 1998)

1   01/26/98 16:37    PULMONARY CONSULT                     CPRSPROVIDER,TWO

Visit: 01/26/98

One document found within date range...

Opening PULMONARY CONSULT record for review...

(Continued on the next page.)

Browse Document               Jan 26, 1998 16:49:32        Page:    1 of    1

PULMONARY CONSULT

CPRSPATIENT,T 666-01-0167P  PULMONARY CLINIC     Visit Date: 01/26/98@16:37

DATE OF NOTE: JAN 26, 1998@16:37:34  ENTRY DATE: JAN 26, 1998@16:37:34

AUTHOR: TIUPROVIDER,THREE    EXP COSIGNER:

URGENCY:                            STATUS: UNSIGNED

DEMOGRAPHICS: CPRSPATIENT,TWO

666-01-0167P

31

JAN 1,1967

His disposition is good.

+ Next Screen  - Prev Screen  ?? More actions                    &gt;&gt;&gt;

Find                      Make Addendum             Identify Signers

Print                     Sign/Cosign               Delete

Edit                      Copy                      Link ...

Quit

Select Action: Quit// **L** Link ...

Problem(s)                Patient/Visit             Link with Request

Specify Linkage: **L** Link with Request

You must link your Result to a Consult Request...

The following CONSULT REQUEST(S) are available:

1&gt;  JAN 23, 1998@11:14  759     PULMONARY

2&gt;  JAN 23, 1998@11:14  760     PULMONARY

CHOOSE 1-2: **2** 760

Opening PULMONARY CONSULT record for review...

(Continued on the next page.)

Browse Document               Jan 26, 1998 16:49:32        Page:    1 of    1

PULMONARY CONSULT

CPRSPATIENT,T 666-01-0167P  PULMONARY CLINIC     Visit Date: 01/26/98@16:37

DATE OF NOTE: JAN 26, 1998@16:37:34  ENTRY DATE: JAN 26, 1998@16:37:34

AUTHOR: TIUPROVIDER,THREE    EXP COSIGNER:

URGENCY:                            STATUS: UNSIGNED

DEMOGRAPHICS: CPRSPATIENT,THREE

666-01-0167P

31

JAN 1,1967

His disposition is good.

+ Next Screen  - Prev Screen  ?? More actions                    &gt;&gt;&gt;

Find                      Make Addendum             Identify Signers

Print                     Sign/Cosign               Delete

Edit                      Copy                      Link ...

Quit

Select Action: Quit// **&lt;Enter&gt;** Quit

Select PATIENT NAME: **&lt;Enter&gt;**

Nothing selected.

3. You may choose the Link action from the All My Unsigned Documents Option, as shown below:

--- Clinician's Menu ---

1      Individual Patient Document

2      All MY UNSIGNED Documents

3      Multiple Patient Documents

4      Enter/edit Document

Select Integrated Document Management Option: **A** ll MY UNSIGNED Documents

Searching for the documents.....

MY UNSIGNED Documents         Jan 26, 1998 16:51:18        Page:    1 of    3

by AUTHOR (TIUPROVIDER,THREE) or EXPECTED COSIGNER    40 documents

Patient               Document                      Ref Date  Status

1    CPRSPATIENT,T (C0167) PULMONARY CONSULT             01/26/98  unsigned

2    ARTPATIENT,TW (A4321) Adverse React/Allergy         01/22/98  unsigned

3    CPRSPATIENT,O (C8796) Reparatory Therapy Note       01/20/98  uncosigned

4    CPRSPATIENT,F (R1350) Reparatory Therapy Note       01/16/98  uncosigned

5    CPRSPATIENT,T (C9999) Reparatory Therapy Note       01/16/98  uncosigned

6    CPRSPATIENT,T (C1350) Reparatory Therapy Note       01/15/98  uncosigned

7    TIUPATIENT,EI (T1239) Reparatory Therapy Note       01/15/98  uncosigned

8    CPRSPATIENT,T (C1563) Reparatory Therapy Note       01/14/98  uncosigned

9    CPRSPATIENT,T (C1563) Reparatory Therapy Note       01/14/98  uncosigned

10   PNPATIENT,FIV (P1350) Reparatory Therapy Note       01/14/98  uncosigned

11   DSPATIENT,TEN (D6572) Reparatory Therapy Note       01/14/98  uncosigned

12   HSPATIENT,ONE (H2591) Reparatory Therapy Note       01/14/98  uncosigned

13   TIUPATIENT,EI (T1239) Reparatory Therapy Note       01/14/98  uncosigned

14   TIUPATIENT,EI (T1239) Reparatory Therapy Note       01/14/98  uncosigned

+         + Next Screen  - Prev Screen  ?? More Actions                    &gt;&gt;&gt;

Find                      Sign/Cosign               Change View

Add Document              Detailed Display          Copy

Edit                      Browse                    Delete Document

Make Addendum             Print                     Quit

Link ...                  Identify Signers

Select Action: Next Screen// **L** Link ...

Problems                  Patient/Visit             Link with Request

Specify Linkage: **L** Link with Request

Select Document(s):  (1-14): **1**

You must link your Result to a Consult Request...

The following CONSULT REQUEST(S) are available:

1&gt;  JAN 23, 1998@11:14  759     PULMONARY

2&gt;  JAN 23, 1998@11:14  760     PULMONARY

CHOOSE 1-2: **2** 760

(Continued on next page.)

MY UNSIGNED Documents         Jan 26, 1998 16:51:32        Page:    1 of    3

by AUTHOR (TIUPATIENT,THREE) or EXPECTED COSIGNER    40 documents

Patient               Document                      Ref Date  Status

1    CPRSPATIENT,T (C0167) PULMONARY CONSULT             01/26/98  unsigned

2    ARTPATIENT,TW (A4321) Adverse React/Allergy         01/22/98  unsigned

3    CPRSPATIENT,O (C8796) Reparatory Therapy Note       01/20/98  uncosigned

4    CPRSPATIENT,F (R1350) Reparatory Therapy Note       01/16/98  uncosigned

5    CPRSPATIENT,T (C9999) Reparatory Therapy Note       01/16/98  uncosigned

6    CPRSPATIENT,T (C1350) Reparatory Therapy Note       01/15/98  uncosigned

7    TIUPATIENT,EI (T1239) Reparatory Therapy Note       01/15/98  uncosigned

8    CPRSPATIENT,T (C1563) Reparatory Therapy Note       01/14/98  uncosigned

9    CPRSPATIENT,T (C1563) Reparatory Therapy Note       01/14/98  uncosigned

10   PNPATIENT,FIV (P1350) Reparatory Therapy Note       01/14/98  uncosigned

11   DSPATIENT,TEN (D6572) Reparatory Therapy Note       01/14/98  uncosigned

12   HSPATIENT,ONE (H2591) Reparatory Therapy Note       01/14/98  uncosigned

13   TIUPATIENT,EI (T1239) Reparatory Therapy Note       01/14/98  uncosigned

14   TIUPATIENT,EI (T1239) Reparatory Therapy Note       01/14/98  uncosigned

+         ** Item 1 Reassigned. **                                          &gt;&gt;&gt;

Find                      Sign/Cosign               Change View

Add Document              Detailed Display          Copy

Edit                      Browse                    Delete Document

Make Addendum             Print                     Quit

Link ...                  Identify Signers

Select Action: Next Screen// **Q** Quit

--- Clinician's Menu ---

1      Individual Patient Document

2      All MY UNSIGNED Documents

3      Multiple Patient Documents

4      Enter/edit Document

Select Integrated Document Management Option:

4. From the CPRS Chart, the dialog looks like this (NOTE: If CONSULTS is defined as a CLASS under CLINICAL DOCUMENTS, this approach is not yet available):

OE     CPRS Clinician Menu

RR     Results Reporting Menu

AD     Add New Orders

RO     Act On Existing Orders

PP     Personal Preferences ...

Select Clinician Menu Option: **OE** CPRS Clinician Menu

Clinic PULMONARY CLINIC       Jan 27, 1998 15:20:32        Page:    1 of    1

Current patient: ** No patient selected **

Patient Name                   ID        DOB          Appointment Date

No patients found.

Enter the number of the patient chart to be opened

+   Next Screen           CV  Change View ...       FD  Find Patient

-   Previous Screen       SV  Save as Default List  Q   Close

Select Patient: Change View// **CPRSPATIENT, FIFTYTHREE** 01-01-67

107010167P       ACTIVE DUTY

A: Known allergies

Searching the patient's chart ...

(Continued on the next page.)

Cover Sheet                   Jan 27, 1998 15:20:40        Page:    1 of    1

CPRSPATIENT,TWO                 666-01-0167P1A           JAN 1,1967 (31)   &lt;A&gt;

Item                                       Entered

Allergies/Adverse Reactions              |

1    DUST                                     | 10/07/97

|

Patient Postings                         |

&lt;None&gt;                                   |

|

Recent Vitals                            |

No data available                        |

|

Immunizations                            |

No immunizations found.                  |

|

Eligibility                              |

Not Service Connected                    |

|

Enter the numbers of the items you wish to act on.                &gt;&gt;&gt;

NW  Enter New Allergy/ADR CV  (Change View ...)     SP  Select New Patient

AD  Add New Orders        CC  Chart Contents ...    Q   Close Patient Chart

Select: Chart Contents// **CC;N** Chart Contents ...

Searching the patient's chart ...

Signed Notes                  Jan 27, 1998 15:20:46        Page:    1 of    1

CPRSPATIENT,TWO                 666-01-0167P1A         JAN 1,1967 (31)   &lt;A&gt;

Currently viewing 17 notes

Title                                      Written      Author     SigSt

1    PULMONARY CONSULT                        | 01/26 16:37  CPRSPROVI  compl

2    Respiratory Therapy Note                 | 12/11 16:59  CPRSPROVI  uncos

3    General Note                             | 10/16 /91    CPRSPROVI  compl

4    General Note                             | 06/17 /91    CPRSPROVI  compl

5    General Note                             | 06/13 /91    CPRSPROVI  compl

Enter the numbers of the items you wish to act on.                &gt;&gt;&gt;

NW  Write New Note        CV  Change View ...       SP  Select New Patient

AD  Add New Orders        CC  Chart Contents ...    Q   Close Patient Chart

Select: Chart Contents// **CV** Change View ...

(Continued on the next page.)

Signed Notes                  Jan 27, 1998 15:20:46        Page:    1 of    1

CPRSPATIENT,TWO                 666-01-0167P1A         JAN 1,1967 (31)   &lt;A&gt;

Currently viewing 17 notes

Title                                      Written      Author     SigSt

1    PULMONARY CONSULT                        | 01/26 16:37  CPRSPROVI  compl

2    Cardiology Note                          | 12/11 16:59  CPRSPROVI  uncos

3    General Note                             | 10/16 /91    CPRSPROVI  compl

4    General Note                             | 06/17 /91    CPRSPROVI  compl

5    General Note                             | 06/13 /91    CPRSPROVI  compl

Enter the numbers of the items you wish to act on.                &gt;&gt;&gt;

1    all signed           4    signed/author             Save as Preferred View

2    my unsigned          5    signed/dates              Remove Preferred View

3    my uncosigned

Select context: 2   my unsigned

Searching the patient's chart ...

Unsigned Notes                Jan 27, 1998 15:20:55        Page:    1 of    1

CPRSPATIENT,TWO                 666-01-0167P1A         JAN 1,1967 (31)   &lt;A&gt;

Currently viewing all unsigned notes

Title                                      Written      Author     SigSt

1    PULMONARY CONSULT                        | 01/27 15:19  CPRSPROVI  unsig

Enter the numbers of the items you wish to act on.                &gt;&gt;&gt;

NW  Write New Note        CV  Change View ...       SP  Select New Patient

AD  Add New Orders        CC  Chart Contents ...    Q   Close Patient Chart

Select: Chart Contents// **1**

(Continued on the next page.)

Unsigned Notes                Jan 27, 1998 15:20:55        Page:    1 of    1

CPRSPATIENT,TWO                 666-01-0167P1A         JAN 1,1967 (31)   &lt;A&gt;

Currently viewing all unsigned notes

Title                                      Written      Author     SigSt

1    PULMONARY CONSULT                        | 01/26 16:37  CPRSPROVI  unsig

Enter the numbers of the items you wish to act on.                &gt;&gt;&gt;

Edit                Detailed Display    Identify signers

Make Addendum       Browse              Copy

Sign                Print               Delete

Select Action: **BR** Browse

Browse Document               Jan 26, 1998 16:49:32        Page:    1 of    1

PULMONARY CONSULT

CPRSPATIENT,T  666-01-0167P  PULMONARY CLINIC     Visit Date: 01/26/98@16:37

DATE OF NOTE: JAN 26, 1998@16:37:34  ENTRY DATE: JAN 26, 1998@16:37:34

AUTHOR: TIUPROVIDER,THREE          EXP COSIGNER:

URGENCY:                            STATUS: UNSIGNED

DEMOGRAPHICS: CPRSPATIENT,TWO

666-01-0167P

31

JAN 1,1967

His disposition is good.

+ Next Screen  - Prev Screen  ?? More actions                    &gt;&gt;&gt;

Find                      Make Addendum             Identify Signers

Print                     Sign/Cosign               Delete

Edit                      Copy                      Link ...

Quit

Select Action: Quit// **L** Link ...

Problem(s)                Patient/Visit             Link with Request

Specify Linkage: **L** Link with Request

You must link your Result to a Consult Request...

The following CONSULT REQUEST(S) are available:

1&gt;  JAN 23, 1998@11:14  759     PULMONARY

2&gt;  JAN 23, 1998@11:14  760     PULMONARY

CHOOSE 1-2: **2** 760

Opening PULMONARY CONSULT record for review...

(Continued on next page.)

Browse Document               Jan 26, 1998 16:49:32        Page:    1 of    1

PULMONARY CONSULT

CPRSPATIENT,T 666-01-0167P   PULMONARY CLINIC     Visit Date: 01/26/98@16:37

DATE OF NOTE: JAN 26, 1998@16:37:34  ENTRY DATE: JAN 26, 1998@16:37:34

AUTHOR: TIUPROVIDER,THREE    EXP COSIGNER:

URGENCY:                            STATUS: UNSIGNED

DEMOGRAPHICS: CPRSPATIENT,TWO

666-01-0167P

31

JAN 1,1967

His disposition is good.

+ Next Screen  - Prev Screen  ?? More actions                    &gt;&gt;&gt;

Find                      Make Addendum             Identify Signers

Print                     Sign/Cosign               Delete

Edit                      Copy                      Link ...

Quit

Select Action: Quit// **&lt;Enter&gt;** Quit

Unsigned Notes                Jan 27, 1998 15:20:55        Page:    1 of    1

CPRSPATIENT,TWO                 666-01-0167P1A         JAN 1,1967 (31)   &lt;A&gt;

Currently viewing all unsigned notes

Title                                      Written      Author     SigSt

1    PULMONARY CONSULT                        | 01/27 15:19  CPRSPROVI  unsig

Enter the numbers of the items you wish to act on.                &gt;&gt;&gt;

NW  Write New Note        CV  Change View ...       SP  Select New Patient

AD  Add New Orders        CC  Chart Contents ...    Q   Close Patient Chart

Select: Chart Contents// **Q** Close Patient Chart

### Using the Consults Package with Medicine

If your site is set up for attaching Medicine results to consults, and there are results available, then Consults prompts you to attach relevant results during the Complete/Update action.

In this example, we attach medicine results to a consult we are completing:

CONSULT TRACKING              Jun 21, 2000 14:23:01          Page:    1 of    3

CPRSPATIENT,FOUR 666-43-8796          2B M              DEC 4,1949 (50)   &lt;CAD&gt;

Wt.(lb): No Entry

Requested  St     No.   Consult/Procedure Request

1   05/16/00  a      1719  ELECTROCARDIOGRAM CARDIOLOGY Proc

2   05/15/00  c      1718  ELECTROCARDIOGRAM CARDIOLOGY Proc

3   02/09/00  p      1679  Holter Monitoring CARDIOLOGY Cons

4   06/18/99  a      1538  PACEMAKER SURVEILLANCE CARDIOLOGY Proc

5   04/07/99  c      1433  Holter Monitoring CARDIOLOGY Cons

6   06/11/98  pr     1047  CARDIOLOGY Cons

7   09/24/97  c       341 *CARDIOLOGY Cons

8   02/03/97  dc      209  CARDIOLOGY Cons

9   07/28/95  c        94  ECHO CARDIOLOGY Proc

10  07/20/95  c        88  ELECTROCARDIOGRAM CARDIOLOGY Proc

11  07/20/95  c        87  ELECTROCARDIOGRAM CARDIOLOGY Proc

12  04/23/92  c        64 *ELECTROCARDIOGRAM CARDIOLOGY Proc

+         Enter ?? for more actions

SP Select Patient   FR Forward          CT Complete/Update  RT Results Display

CV Change View ...  CX Cancel (Deny)    MA Make Addendum    PF Print Form 513

RC Receive          DC Discontinue      SF Sig Findings     RM Remove Med Rslt

SC Schedule         CM Add Comment      DD Detailed Display ER Edit/Resubmit
Select: Next Screen// **CT** Complete/Update

CHOOSE No. 1-32: **1**

Attach Medicine Results? Y// **&lt;Enter&gt;** ES

Procedure/Medicine Resulting  Jun 21, 2000 14:29:50          Page:    1 of    1

CPRSPATIENT,FOUR 666-43-8796             2B M              DEC 4,1949 (50)   &lt;CAD&gt;

Available Medicine Results

Type of Proc.           Procedure Date      Summary

1   ELECTROCARDIOGRAM       AUG 13,1997         ABNORMAL

2   ELECTROCARDIOGRAM       JUL 31,1995@08:04   NORMAL

Select action or item number

AR Associate Result       DR Display selected medicine result

Select action: Quit//

Notice that when we tried to complete a consult with available Medicine results, Consults prompted us, “Attach Medicine Results?” By responding affirmatively, we are presented a screen with a list of the qualifying Medicine results and the ability to both explore these results and attach one or more of them to the consult.

For this to happen, two things must have taken place:

1.      Your CAC or IRM must have defined certain procedures as qualifying to provide results to your service.

2.      Those procedures must have been performed on your patient and the results entered into VistA.

In the following example, a medicine result is associated with the current consult and the complete action is finished:

Procedure/Medicine Resulting  Jun 21, 2000 14:29:50          Page:   1 of    1

CPRSPATIENT,FOUR 666-43-8796           2B M              DEC 4,1949 (50)   &lt;CAD&gt;

Available Medicine Results

Type of Proc.           Procedure Date      Summary

1   ELECTROCARDIOGRAM       AUG 13,1997         ABNORMAL

2   ELECTROCARDIOGRAM       JUL 31,1995@08:04   NORMAL

Select action or item number

AR Associate Result       DR Display selected medicine result

Select action: Quit// **AR** Associate Result

Select item:  (1-2): **1**

ELECTROCARDIOGRAM       AUG 13,1997         ABNORMAL

Are you sure you want to associate this result? NO// **Y** YES

Procedure/Medicine Resulting  Jun 21, 2000 14:41:16          Page:    1 of    1

CPRSPATIENT,FOUR 666-43-8796          2B M              DEC 4,1949 (50)   &lt;CAD&gt;

Available Medicine Results

Type of Proc.           Procedure Date      Summary

1   ELECTROCARDIOGRAM       JUL 31,1995@08:04   NORMAL

Select action or item number

AR Associate Result       DR Display selected medicine result

Select action: Quit// **&lt;Enter&gt;** QUIT

Continue with Note Entry? Y// **N** NO

CONSULT TRACKING              Jun 21, 2000 14:41:35         Page:    1 of    3

CPRSPATIENT,FOUR 666-43-8796          2B M              DEC 4,1949 (50)   &lt;CAD&gt;

Wt.(lb): No Entry

Requested  St     No.   Consult/Procedure Request

1   05/16/00  c      1719  ELECTROCARDIOGRAM CARDIOLOGY Proc

2   05/15/00  c      1718  ELECTROCARDIOGRAM CARDIOLOGY Proc

3   02/09/00  p      1679  Holter Monitoring CARDIOLOGY Cons

4   06/18/99  a      1538  PACEMAKER SURVEILLANCE CARDIOLOGY Proc

5   04/07/99  c      1433  Holter Monitoring CARDIOLOGY Cons

6   06/11/98  pr     1047  CARDIOLOGY Cons

7   09/24/97  c       341 *CARDIOLOGY Cons

8   02/03/97  dc      209  CARDIOLOGY Cons

9   07/28/95  c        94  ECHO CARDIOLOGY Proc

10  07/20/95  c        88  ELECTROCARDIOGRAM CARDIOLOGY Proc

11  07/20/95  c        87  ELECTROCARDIOGRAM CARDIOLOGY Proc

12  04/23/92  c        64 *ELECTROCARDIOGRAM CARDIOLOGY Proc

+         Enter ?? for more actions

SP Select Patient   FR Forward          CT Complete/Update  RT Results Display

CV Change View ...  CX Cancel (Deny)    MA Make Addendum    PF Print Form 513

RC Receive          DC Discontinue      SF Sig Findings     RM Remove Med Rslt

SC Schedule         CM Add Comment      DD Detailed Display ER Edit/Resubmit

Select: Next Screen//

Notice that after we exited the Procedure/Medicine Resulting screen, we were prompted about entering a note. If we had responded with a Yes, we would have been able to attach a TIU note to the consult we were closing in addition to the Medicine results.

### Using the Consults Package with Clinical Procedures

Individual consult types can be designated to be resulted with the Clinical Procedures package. If this is the case, then Consults expects clinical procedures results to be attached to the consult. This attachment is usually accomplished with the CPUser program.

If the instrument in question has not yet been connected to Clinical Procedures, then the consult may be completed in the usual way by an authorized provider. (Authorized providers being clinicians whom the CAC has set up as an interpreter for the appropriate service.) In this case Consults will filter the note titles available and only allow you to use Clinical Procedures titles.

When the clinical procedure results are present, Consults changes the status to PR (partial results). This means that, at least, at stub of a TIU document has been attached to the consult. It could also mean that one or more images and/or instrument reports created by a clinical device are also attached to the consult. Additionally, the interpretation of the clinical device image(s) or text may have been uploaded and is ready for signature.

The minimum required by the consults package to complete a clinical procedures consult is the interpretation of the clinical device output. If this is not supplied via upload, then it must be entered by the consulting clinician. When this interpretation is entered, the following fields are required and are prompted for (if not already present):

<!-- image -->

Selecting a button with an arrow pointing down displays a drop-down list of choices. A button with three dots brings up a calendar control to select a date and time.

### Windows Quick Start

### Introduction 57

#### Windows Flow of Information 58

##### Starting Consults in Windows 58

##### Order New Consult 60

##### Print Form 62

##### Forward Request 63

##### Receive Request 64

##### Comment 66

##### Complete a Consult (From the Consults Tab) 68

##### Complete a Consult (From the Notes Tab) 70

##### Complete a Consult (From Medicine Results) 74

#### Other Windows Topics 77

##### Cancel Request 77

##### Detailed Display 80

##### Discontinue Order 79

##### Make Addendum 86

##### New Date Range 89

##### Results Display 92

##### Select Consult 93

##### Select New Patient 94

##### Select Service 95

##### View by Status 96


#### Introduction

##### 1 Before each process, select the consult.

##### Most processes assume that you have already selected a Consult already. If you hover over a Consult, the full line displays.

<!-- image -->

#### Windows Flow of Information

##### Starting Consults in Windows

###### Start CPRS for Windows by locating the appropriate icon (usually in your Star folder if using VACS or a share folder, or on your desktop).

###### Log-on to your system using your PIV card or your user name and access code.

<!-- image -->

###### Select a patient. You can user the Patient List area to select a smaller list of patients, if one is defined for you. Type in part of the patient’s name or many sites user the first letter of the last name and the last 4 of the social security number. When you identify the correct patient name, double-click on it, or highlight it and select OK.

<!-- image -->

###### Select the Consults Tab:

<!-- image -->

##### Order New Consult

###### Select New Consult by selecting Action | New Consult or selecting the New Consult button.

<!-- image -->

###### Fill out the Order a Consult dialog:

<!-- image -->

Select the Specialty or Service to which the Consult request will be sent. You can also use the button at the end of the field to see a tree view.

If needed, change the Urgency, Place, Attention, and Provisional Diagnosis boxes.

Select if the patient will be an inpatient or outpatient.

Enter a Clinically Indicated Date.

If needed, type the reason for request or add to boilerplate text.

If the Provisional Diagnosis field is active, you must enter a diagnosis. If the field is yellow, you must use the Lexicon button to select the provisional diagnosis.

Review the information in the box at the bottom of the dialog.

When the information is complete and correct, select **Accept Order** .

##### Print Form 513

###### Select Print from the File Menu:

Select File | Print or follow the underlined letters from the keyboard by pressing Alt+F (together) then P.

<!-- image -->

###### Select the Printer Device:

1. Select Chart Copy or Work Copy.
2. If needed, start typing the device name, CPRS finds the closest match. Or use the scroll bar and then click on the printer you want.
3. Then select OK or press the Enter key.
<!-- image -->

##### Forward Request

###### Select Forward:

1. Select the appropriate Consult.
2. Click on Action | Consult Tracking | Forward or follow the underlined character on the keyboard by pressing Alt+A (together), then C, and then F.

<!-- image -->

###### Fill in the Forward Consult dialog:

1. Select the correct service.
2. Type in the reason for forwarding this Consult.
3. If necessary, change the Urgency, Attention, and date and time of the action.
4. Enter comments or reason for forwarding as needed.
5. When finished, select OK.
<!-- image -->

##### Receive Request

###### Select Receive:

1. Select Action | Consult Tracking | Receive or use the keyboard by pressing the underlined characters: First Alt and A (together), then C, and then R.
<!-- image -->

###### Select OK.

1. If you need some other time, change it using the Date/time of this action field.
2. If the action should be by some other person, change the name in the Action by field.

<!-- image -->

##### Comment

###### Select Add Comment:

1. Select Action | Consult Tracking | Add Comment or use the keyboard following the underlined letters: First Alt+A (together), then C, then A.

<!-- image -->

###### Fill in the Add Comment to Consult Dialog:

1. Type your comment in the text area.
2. Then select the Send Alert check box.

<!-- image -->

###### Select the People to Receive the Alert:

1. Selecting the names in the right list adds them to the Currently selected recipient list to receive the alert.
2. If you need to remove someone from the list, select their name in the right pane.
3. When the list has all the people that you want to receive the alert, select OK.

<!-- image -->

<!-- image -->

###### Select OK:

1. When finished, select OK.
<!-- image -->

##### Complete a Consult (From the Consults Tab)

###### Select Complete/Update Results:

1. Select Action | Consult Results | Complete/ Update Results or use the keyboard following the underlined letters:  First Alt+A (together) then R and then C.
<!-- image -->

###### Select the Title of the Note:

1. Start typing the Title, then press Enter when the correct Title is highlighted.
2. If the Expected Cosigner box appears, you also need to fill in the Expected Cosigner.
<!-- image -->

###### Type in the text of the results:

As with any TIU document, part of it can be boiler-plate. And part of it may be entered by you. This can be typed directly or cut and pasted from a word.

<!-- image -->

###### Save the note:

You can save the note to finish and sign later by selecting Save Without Signature. This changes the status to Partial Results (pr).

Or you can sign it now using Sign Note Now. This changes the status to Complete (c).

<!-- image -->

##### Complete a Consults (From the Notes Tab)

Before starting, from the CPRS Windows program, select the correct patient and click the Notes tab.

###### Select New Note.

<!-- image -->

###### Select the Title of the Note:

1. Type the beginning of the note title, locate the correct title and highlight it.
2. When finished, select  OK.

<!-- image -->

###### Select the consult to complete.

<!-- image -->

###### Type in the text of the results.

As with any TIU document, part of it can be boiler-plate, and part of it may be entered by you.

<!-- image -->

###### Save the note.

You can save it to finish and sign later by using the Save Without Signature menu item.  This changes the status to Partial Results (pr).

Or you can sign it now by using the Sign Note Now menu item. This changes the status to Complete (c).

<!-- image -->

##### Complete a Consult (From the Medicine Results)

###### Select Attach Medicine Results:

Procedures are indicated by the medical icon (caduceus).

If medicine results are available for this patient, the menu command Attach Medicine Results is turned on (not grayed out).

1. To attach Medicine results, select Action | Consults Results | Attach Medicine Results.
<!-- image -->

###### Select the medicine result:

1. Select the medicine result you want.
2. Select **OK** .
<!-- image -->

###### No signature is necessary at this time.

##### Undo Medicine Results

###### Select Remove Medicine Results

Windows activates this menu command when a result *you can* remove is present in the selected consult.

1. Select Action | Consult Results | Remove Medicine Results.
<!-- image -->

###### Select the medicine result to be removed.

1. If more medicine results are present, they will be listed in the Remove Medicine Result dialog.
<!-- image -->

Consults keeps and displays a complete audit trail as shown below.

<!-- image -->

#### Other Windows Topics

##### Cancel (Deny) Request

Note: 	This is a consult receiver’s action. If you are the consult originator, use the Discontinue Order action.

###### Select Cancel:

1. Select Action | Consult Tracking | Cancel, or follow the underlined letters by typing Alt and A together (Alt+A), then C, and then C again.
<!-- image -->

###### Consult dialog:

1. Type the reason for the denial.  Be specific enough so that the originating provider can correct and resubmit the consult.
2. When finished, select OK.

A notification is automatically sent to the consult originator so that the consult can be edited and resubmitted.

<!-- image -->

##### Discontinue Order

Note:	This is a consult originator’s action. If you are the consult receiver, use the Cancel (Deny) action.

###### Select Discontinue:

1. Click on Action, then Consult Tracking, then Discontinue, or follow the underlined characters on the keyboard by pressing Alt+A (together), then C, and then D.

<!-- image -->

###### Fill out the Discontinue Consult dialog:

1. Type in the reason in the Comments box.
2. When finished, select **OK** .

A notification is automatically sent to the originator of the consult with information about the discontinuation of the order.

<!-- image -->

##### Detailed Display

Postings codes have the following meanings:

C–There are Crisis Note(s) present.

W—There are Clinical Warning Note(s) present.

A—There are allergies present.

D—There are Directive Note(s) present.

Click here for specifics.

<!-- image -->

<!-- image -->

1. Select the consult you want to see.

The consult number can be used to quickly access a specific consult in a variety of situations.

The Detailed Display includes:

Current Primary Care information

Current Eligibility information

Order information

Last action information

A record of activity

All signed notes.

Information about unsigned notes.

Notes, Results, and Addenda

All other text fields associated with the consult.

#### Changes made by Patch 73 for ICD-10 Remediation

ICD Diagnosis Code Display

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

The Consults package will display ICD Diagnosis on the display details of Consults/Procedures orders.

- If the user selects an order to display details and the Provisional Diagnosis was entered as an ICD-9 diagnosis using the Lexicon, the ICD-9 diagnosis code and description/definition will be displayed.
- If the user selects an order to display details and the Provisional Diagnosis was entered as an ICD-10 diagnosis using the Lexicon, the ICD-10-CM diagnosis code and full description/definition will be displayed.
- If the user selects an order to display and the Provisional Diagnosis was entered using free text data entry, then Consults will not designate the diagnosis as ICD-9 or ICD-10.
- If the user selects an existing consult to display and the Provisional Diagnosis was entered using the Lexicon, then Consults will designate the particular diagnosis as ICD-9 or ICD-10.

<!-- image -->

<!-- image -->

- ICD Diagnosis on the Display SF 513 action will be displayed for a particular Consults or Procedure.
    - If the user performs the action Display SF 513 for a consult or procedure for which ICD-10 diagnosis was entered, Consults will display the ICD-10-CM diagnosis code and full description/definition.
    - If the user performs the action Display SF 513 for a consult or procedure and the Provisional Diagnosis was entered using free text data entry, then Consults will not designate the diagnosis as ICD-9 or ICD-10.
    - If the user performs the action Display SF 513 for a consult or procedure and the Provisional Diagnosis was entered using the Lexicon, then Consults will designate the particular diagnosis as ICD-9 or ICD-10.

ICD Diagnosis Search

Consults will provide the ability to search on ICD-10-CM diagnosis full (expanded) text descriptions and codes.

<!-- image -->

- Consults will display ICD Diagnosis on the Display SF 513 action for a particular Consults or Procedure.
    - If the user performs the action Display SF 513 for a consult or procedure for which ICD-10 diagnosis was entered, Consults will display the ICD-10-CM diagnosis code and full description/definition.
    - If the user performs the action Display SF 513 for a consult or procedure and the Provisional Diagnosis was entered using free text data entry, Consults will not designate the diagnosis as ICD-9 or ICD-10.
    - If the user performs the action Display SF 513 for a consult or procedure and the Provisional Diagnosis was entered using the Lexicon, then Consults will designate the particular diagnosis as ICD-9 or ICD-10.

##### Make Addendum

An Addendum is a *medical* statement by a patient care professional about a specific Note. It differs from a Comment in that it is about medical matters, where Comments, which can be written by anyone, should contain information needed to *administer* the consult.

###### Select the Consult and the Note:

1. First select the correct consult under All Consults.
2. Then, in the box below the New Procedure box to select the note.

<!-- image -->

###### Select Make Addendum

1. Select Action | Consult Results | Make Addendum, Or follow the underlined character on the keyboard by pressing Alt+A (together), then C, and then F.
<!-- image -->

###### Type the addendum.

An addendum supplies supplementary information on the patient’s condition.

As with other TIU objects, addendum may include boilerplate text.

<!-- image -->

###### Save the note:

You can save it to finish and sign later by using the Save Without Signature menu item.  This changes the status to Partial Results (pr).

Or you can sign it now by using the Sign Note Now menu item. This changes the status to Complete (c).

<!-- image -->

##### New Date Range

###### Select Consults by Date Range:

1. Select View | Consults by Date Range, or use the keyboard to follow the underlined letters: Alt+V (together) then R.
<!-- image -->

###### Fill in the List Consults by Date Range Dialog:

1. For the Beginning date, in the List Consults by Date Range dialog, enter the date or select the Calendar control by selecting the button with three dots.
2. If using the calendar control, Initially, the current date is highlighted. Select the month, day, and time you want. These arrow buttons next to the date enables the user to go up or down the months.
3. When you have the correct date and time, select OK.
4. Select an Ending Date using the same method described above.
5. In the List Consults by Date Range dialog, select the sort order oldest to newest or vice versa.
<!-- image -->
<!-- image -->

###### In the List Consults by Date Range dialog, select OK.

Below is an example of dates entered and the sort order in the List Consults by Date Range dialog.

<!-- image -->

After you click OK only consults within the date range are displayed. The date range is displayed  above the Consults box.

<!-- image -->

##### Quit

There are two ways to Exit CPRS.

The simplest way to quit is to click on the X in the upper right-hand corner of the window.

<!-- image -->

Or you can select Exit from the File menu, or you can press the Alt and F4 keys at the same time (Alt+F4).

<!-- image -->

##### Results Display

1. Highlight the correct Consult.
2. Get the results for the current consult by selecting Action | Consult Tracking | Display Results.

The results display gives only the signed results and addendum making it easier to focus in on the information you need.

It also gives author information on unsigned and/or unreleased notes.

<!-- image -->

Note:	If this were an Inter-Facility Consult, CPRS’s Remote Data Views would retrieve the results over the VA Intranet. This may take slightly longer.

##### Select Consult

1. Select the consult you want to view or perform an action on.
2. If the consult has more than one note associated with it, that is indicated.

<!-- image -->

##### Select New Patient

###### Choose Select New Patient from the File Menu, or follow the underlined letter from the keyboard by pressing Alt+F (together) then N.

<!-- image -->

###### Use the Patient Selection Dialog:

1. If a list has been created that narrows the patient list, select the radio button to change the appropriate list of patients, such as a Clinic perhaps.
2. Under Patients, type anything here that is allowed in V *IST* A patient prompts (many frequently use the first letter of the last name and last 4 of the social security number) and a list of matches appear directly below.
3. Select the patient by double-clicking a name or highlight the name and press OK.

<!-- image -->

##### Select Service

###### Select Consults by Service from the View Menu:

1. Select View | Consults by Service, or follow the underlined letters from the keyboard by pressing Alt+V (together) then S.
2. In the List Consults by Service dialog that displays, you can expand hierarchies by clicking the plus sign, contract them by clicking the minus sign. You can also change the sort order of this list if you want to.
3. Locate the service, highlight it, and select OK.
<!-- image -->

<!-- image -->

##### View by Status

###### Select Consults by Status from the View Menu, follow the underlined letters from the keyboard by pressing Alt+V (together) then U.

<!-- image -->

###### Select the status you want from the list:

1. Click on the status or statuses you want to see. Hold down the Ctrl key when selecting to select more than one status.
2. Change the sort order if needed.
3. When finished, click the OK button, or press the Enter key.
<!-- image -->

Now the list of consults only has ones with the status you selected.

<!-- image -->

##### Custom List

Custom List enables the user to select the service or services, statuses, and the beginning and ending date rages. Users can also group the items by Consults/ Procedures, Service, or Status and set the sort order.

###### Select Custom View from the View Menu by selecting View | Custom View

<!-- image -->

###### Select the view you want.

Do one or more of the following:

1. Select one or more services from the tree view. Use the shift and Ctrl keys to select multiple statuses (or services).
2. Enter a beginning date and ending date. You can either type it in or select the button to use the calendar control.
3. If you want to group them, select the Group method: You can group by Consults/ Procedures, Service, or Status.

<!-- image -->

###### 3.Click OK.

## Package Reference

There are three menus, six notifications, and 18 actions that make up the package that is Consults. In the preceding section, **Package Operation** , we discussed a number of these in order to explain how the Consult/Request Tracking package works. In this section, we give each of a description of each of these in turn to provide reference information for you.

### General Service User Menu

If you are a Consults user from a service other than Medicine or Pharmacy services, you probably have the GMRC General Service User menu. This menu gives you access to all the basic functionality you need to track Consults for your service.

As a General Service User, you have access to three basic options as shown in this example:

Select Consult Service Tracking Option: **?**

CS     Consult Service Tracking

PC     Service Consults Pending Resolution

ST     Completion Time Statistics

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Consult Service Tracking Option:

#### Consult Service Tracking Option

The Consult/Request Service Tracking option may be used to:

Review the latest activity related to a patient's consult/procedure request orders.

Update or track activities related to a patient's consults.

The menu of actions available to you depends on whether you are a Review Only user or an Update user. The names and the synonyms for each menu action is listed below:

##### Review Only and Update Actions

| ACTION NAME       | SYNONYM   | GUI Menu Action                                    |
|-------------------|-----------|----------------------------------------------------|
| Next Screen       | +         |                                                    |
| Previous Screen   | -         |                                                    |
| Add Comment       | CM        | Action&#124;Consult Tracking&#124;Add Comment      |
| Change Date Range | CV;DT     | View&#124;Consults by Date Range                   |
| Detailed Display  | DD        | Action&#124;Consult Tracking&#124;Detailed Display |
| Edit/Resubmit     | ER        | Action&#124;Consult Tracking&#124;Edit Resubmit*   |
| Redisplay Screen  | RD        |                                                    |
| Select Patient    | SP        | File&#124;Select New Patient                       |
| Select Service    | CV;SS     | View&#124;Consults by Service                      |
| Print Form 513    | PF        | File&#124;Print                                    |
| Quit              | Q         | File&#124;Exit                                     |
| Results Display   | RT        | Action&#124;Consult Tracking&#124;Display Results  |
| View By Status    | CV;ST     | View&#124;Consults by Status                       |

* ER (Edit/Resubmit) may be used only by the originating provider or an update user. It is available on this menu in case the originating provider is not an update user.

##### Update Only Actions

| ACTION NAME          | SYNONYM   | GUI Menu Command                                           |
|----------------------|-----------|------------------------------------------------------------|
| Complete (Update)    | CT        | Action&#124;Consult Results&#124;Complete/Update Results   |
| Cancel (Deny)        | DY        | Action&#124;Consult Tracking &#124;Deny                    |
| Discontinue          | DC        | Action&#124;Consult Tracking &#124;Discontinue             |
| Forward              | FR        | Action&#124;Consult Tracking &#124;Forward                 |
| Receive              | RC        | Action&#124;Consult Tracking &#124;Receive                 |
| Remove Med Rslt      | RM        | Action&#124; Consult Tracking&#124;Remove Medicine Results |
| Schedule             | SC        | Action&#124;Consult Tracking&#124;Schedule                 |
| Significant Findings | SF        | Action&#124;Consult Tracking&#124;Significant Findings     |
| Make Addendum        | MA        | Action&#124;Consult Results&#124;Make Addendum             |

Each review screen displayed has a prompt at the bottom of the display screen. This prompt varies according to what Consults thinks you are going to do next. Thus, it is either “Select Consult:” or “Select Action:” depending on various system variables. If the prompt is “Select Consult:” you may either select a consult or an action. If the prompt is “Select Action:” you may only select an action. In either case a ? at this prompt provides you with a menu of actions.

Before you use this option, you need to know:

- The patient's name or identification.

You may identify a patient by entering information other than the patient's name. Some possibilities are: Social Security Number (SSN), Ward Location, or Room-Bed, at the Select Patient prompt.

- The service or specialty.

The default answer at the Select Service/Specialty Tracking prompt is always ALL SERVICES//. The response you make at the prompt determines what action you are able to select. If you accept the ALL SERVICES default, the Review Only actions are the only ones available. Alternatively, a service/specialty could be specified to restrict the number of consults to review. If you are an Update user for the service/specialty you selected, then you have all actions available to you at the action prompt.

An example of the Consult/Request Service Tracking option and default Review Only actions available for use with the option are shown in the following sample dialogue. User responses are in bold.

Select Consult Service Tracking Option: **?**

CS     Consult Service Tracking

PC     Service Consults Pending Resolution

ST     Completion Time Statistics

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Consult Service Tracking Option: **CS** Consult/Request Service Tracking

Select Patient: **CPRSPATIENT,FO** UR           01-01-51     666123456     YES     SC VET

ERAN

Select Service/Specialty: ALL SERVICES// **&lt;Enter&gt;** ALL SERVICES

List From Starting Date: ALL DATES// **&lt;Enter&gt;** ALL

Select the Consult/Request Service Tracking option from your menu and enter the name of the patient whose consults/requests you want to review.

At the Select Service/Specialty prompt enter the name of the Service or hierarchy of services the consult was referred to. If consults are available in the service or hierarchy for the patient specified, they are listed as shown in the following display.

CONSULT TRACKING              Oct 06, 2000 08:24:24          Page:    1 of    1

CPRSPATIENT,FOUR   666-44-2222     8E/3E101-1            MAR 3,1960 (40)   &lt;AD&gt;

Wt.(lb): 184

Requested  St     No.   Consult/Procedure Request

1   10/06/00   p      1766  EYE CLINIC Cons

Enter ?? for more actions

SP Select Patient         RT Results Display        ER Edit/Resubmit

CV Change View ...        PF Print Form 513

DD Detailed Display       CM Add Comment

Select: Quit//

##### Review Only Actions

Enter ?? at the Select Item(s) prompt to see the complete list of options available to you.

Select Consult: Quit// ??

Enter the display number of the item you wish to act on, or select an action.

If you'd like another view of the consults, enter CV.

Status key:

'a' - active          'c' - complete         'dc' - discontinued

'p' - pending         'x' - cancelled        'pr' - partial results

's' - scheduled       'e' - expired

Enter ?? to see a list of actions available for navigating the list.

Press &lt;return&gt; to continue ...

The following actions are also available:

+    Next Screen          RD   Redisplay Screen

-    Previous Screen      UP   Up a Line            CWAD Display CWAD Info

FS   First Screen         DN   Down a Line

LS   Last Screen                                    SL   Search List

PS   Print Screen         EX   Exit

GO   Go to Page           PT   Print List

Enter RETURN to continue or '^' to exit:

If you are an update user, the menu of actions includes additional actions such as received, completed, and discontinued.

The help display also includes a key to abbreviations used in consult screens, including the Consult Tracking screen currently under discussion.

##### Update Select Actions

If you are an Update user, then the Consult Tracking display looks like this:

CONSULT TRACKING              Oct 06, 2000 08:26:04          Page:    1 of    2

CPRSPATIENT,FOUR   666-44-2222     8E/3E101-1            MAR 3,1960 (40)   &lt;AD&gt;

Wt.(lb): 184

Requested  St     No.   Consult/Procedure Request

1   11/17/98   x      1211  BRONCHOSCOPY PULMONARY Proc

2   07/13/98   c      1112 *PULMONARY Cons

3   06/18/98   c      1062 *PULMONARY Cons

4   06/12/98   c      1050  PULMONARY Cons

5   06/08/98   c      1028  PULMONARY Cons

6   06/04/98   dc     1022  PULMONARY Cons

7   05/27/98   dc      940  PULMONARY Cons

8   05/20/98   dc      919  PULMONARY Cons

9   05/13/98   c       898 *PULMONARY Cons

10  05/01/98   c       881  PULMONARY Cons

11  04/15/98   c       843  PULMONARY Cons

12  03/16/98   c       827  PULMONARY Cons

+         Enter ?? for more actions

SP Select Patient   FR Forward          CT Complete/Update  RT Results Display

CV Change View ...  CX Cancel (Deny)    MA Make Addendum    PF Print Form 513

RC Receive          DC Discontinue      SF Sig Findings     RM Remove Med Rslt

SC Schedule         CM Add Comment      DD Detailed Display ER Edit/Resubmit Select: Next Screen//

Each action is described in detail in the **Actions** section of **Package** Reference starting on page 112.

#### Completion Time Statistics

This report is intended to help hospitals track overall quality of service. High numbers on this report can indicate the presence of bottlenecks in the organization that might need management attention.

In the following example, a report on completion times is printed for Pulmonary Service:

Select Consult Service Tracking Option: **?**

CS     Consult Service Tracking

PC     Service Consults Pending Resolution

ST     Completion Time Statistics

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Consult Service Tracking Option: **ST** Completion Time Statistics

Select Service/Specialty: ALL SERVICES// **PUL** MONARY

List From Starting Date: ALL DATES//

...HMMM, LET ME THINK ABOUT THAT A MOMENT...........

DAYS TO COMPLETE CONSULT STATSOct 06, 2000 08:28:22          Page:    1 of    1

Number Of Days To Complete A Consult For Services Statistics.

FROM: ALL   TO: OCT 6,2000

Consult/Request Completion Time Statistics

FROM: ALL   TO: OCT 6,2000

SERVICE: PULMONARY

Total Number Of Consults Completed: 200

Mean Days To Complete: 46.8                       Standard Deviation: 104.7

Total INPATIENT Consults: 32

Mean Days To Complete: 60.7                       Standard Deviation: 125.1

Total OUTPATIENT Consults: 30

Mean Days To Complete: 93.4                       Standard Deviation: 155.5

Total Unclassified Consults: 138

Mean Days To Complete: 33.4                       Standard Deviation: 81.0

Enter ?? for more actions

SS  Select Service        PR  Print Completion Statistics To A Printer.

Select Item(s): Quit//

#### Service Consults Pending Resolution

The purpose of the Service Consults Pending Resolution option is to list the pending and active consults. Use it to stay informed about the overall status of consults for your service.

In the following example, the option is used to view pending and active Pulmonary consults:

Select Consult Service Tracking Option: **?**

CS     Consult Service Tracking

PC     Service Consults Pending Resolution

ST     Completion Time Statistics

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Consult Service Tracking Option: **PC** Service Consults Pending Resolution

Select Service/Specialty: **PUL** MONARY

List From Starting Date: ALL DATES// **&lt;Enter&gt;**

...EXCUSE ME, LET ME THINK ABOUT THAT A MOMENT...

Service Consults by Status    Oct 06, 2000 08:31:39          Page:    1 of    5

To Service:  PULMONARY

From: ALL   To: OCT 6,2000

Status      Last Action      Request Date  Patient Name      Pt Location

Consult/Request By Status

FROM: ALL   TO: OCT 6,2000

SERVICE: PULMONARY

Pending    CPRS RELEASED ORDER 09/20/00 CPRSATIENT,FOU (6572) 2B MED

Pending    CPRS RELEASED ORDER 09/19/00 CPRSATIENT,ONE (5678) 2B MED

Pending    CPRS RELEASED ORDER 09/19/00 CPRSATIENT,FIV (1111) 2B MED

Pending    CPRS RELEASED ORDER 07/20/00 CPRSATIENT,TWO (3241) 2B MED

Pending    PRINTED TO          06/29/99 CPRSATIENT,SIX (8829) GENERAL MEDICINE

Pending    PRINTED TO          06/28/99 CPRSATIENT,FOU (3779) 1A

Pending    PRINTED TO          06/15/99 CPRSATIENT,SEV (8828) 13A PSYCH

Pending    PRINTED TO          06/08/99 CPRSATIENT,FIF (4111) 1A

Pending    PRINTED TO          06/03/99 CPRSATIENT,EIG (2345) ONCOLOGY

Pending    PRINTED TO          06/03/99 CPRSATIENT,SIX (9235) 1A

Pending    PRINTED TO          06/03/99 CPRSATIENT,NIN (3242) ONCOLOGY

Pending    PRINTED TO          06/03/99 CPRSATIENT,TEN (5525) ONCOLOGY

+         Enter ?? for more actions                                          &gt;&gt;&gt;

Service             Status              Number on/off       Print List

Select Item(s): Next Screen//

Note:	Someone in your clinic or service should review this list daily to make sure that all consults are being attended to.

### Consult Status

The following table gives the statuses that Consults uses, along with their abbreviation, name, and description:

| Abbreviation   | Name            | Description                                                                              |
|----------------|-----------------|------------------------------------------------------------------------------------------|
| a              | ACTIVE          | Orders that are active or have been accepted by the service for processing.              |
| c              | COMPLETE        | Orders that require no further action by the ancillary service.                          |
| dc             | DISCONTINUE     | Orders that have been stopped prior to expiration or completion.                         |
| p              | PENDING         | Orders that have been placed but not yet accepted by the service filling the order.      |
| pr             | PARTIAL RESULTS | All or part of a consult completion report has been entered but has not yet been signed. |
| s              | SCHEDULED       | The receiving clinic has scheduled an appointment for the patient.                       |
| x              | CANCELLED       | Orders that have been rejected by the ancillary service without being acted on.          |

The following table gives the actions that Consults uses along with the status after the action is performed:

| Consult Actions     | Status after Action   |
|---------------------|-----------------------|
| CPRS Released Order | PENDING               |
| Discontinued        | DISCONTINUED          |
| Incomplete Report   | PARTIAL RESULTS       |
| Completed           | COMPLETE              |
| Edited/Resubmit     | PENDING               |
| Schedule            | SCHEDULED             |
| Forwarded           | PENDING               |
| Canceled            | CANCELLED             |
| Added Comment       | No change in status   |
| Received            | ACTIVE                |
| Printed             | No change in status   |

This table shows actions that are tracked in Consults V. 3.0. Actions that are new with 3.0 are indicated as well as which Consults menu (update or review) initiates the action. If an order status change can result from the action, the new status is shown.

| ##   ## TRACKED  ## ACTION TYPE   | ## New  ## V.3.0   | ## Update  ## Actions   | ## Review  ## Actions   | RELATED OE/RR STATUS        | ##   ##   ## Comment                                                                                                                                                                         |
|-----------------------------------|--------------------|-------------------------|-------------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Added Comment                     |                    | X                       | X                       |                             | Review users can add a comment.                                                                                                                                                              |
| Addendum Added To                 | X                  | X                       |                         |                             | Based on adding a signed and released addendum to a completed note via the Complete/Update or Make Addendum action or through TIU actions.                                                   |
| Cancelled                         | X                  | X                       |                         | CANCELLED                   | This is used in 3.0 replacing the 2.5 Deny action.                                                                                                                                           |
| Complete/  Update                 |                    | X                       |                         | COMPLETE or PARTIAL RESULTS | Changed title to imply Complete can be chosen multiple times by clinicians entering results. TIU actions can also cause this tracking action. Includes the one-time Administrative Complete. |
| Disassociate Result               | X                  |                         |                         |                             | Currently done through TIU actions. In the future will be used to remove an incorrectly associated note.                                                                                     |
| Discontinued                      |                    | X                       |                         | DISCONTINUED                | No longer includes Denied.                                                                                                                                                                   |
| Edit Before Release               | Obso-lete          |                         |                         | UNRELEASED                  | Moved unreleased consults to Order Entry in CPRS conversion.                                                                                                                                 |
| Edit/Resubmitted                  | X                  |                         |                         | PENDING                     | The originating provider can edit and resubmit a consult from either an alert or the Consult Tracking screen. An update user may also use this action.                                       |
| CPRS Released Order               |                    |                         |                         | PENDING                     | Used in 3.0 to represent a signed/released Consult order from CPRS.                                                                                                                          |
| Forwarded From                    |                    | X                       |                         | PENDING                     |                                                                                                                                                                                              |
| Incomplete RPT                    |                    |                         |                         | PARTIAL RESULTS             | Status name has changed from Incomplete RPT. Based on Complete/Update action, and/or TIU actions, if the first consult note is not completed.                                                |
| New Note Added                    | X                  |                         |                         | PARTIAL RESULTS/ COMPLETE   | Based on Complete/Update action and/or TIU actions.                                                                                                                                          |

Consult Action/Status Overview (Continued)

| ##   ## TRACKED  ## ACTION TYPE   | ## New  ## V.3.0   | ## Update  ## Actions   | ## Review  ## Actions   | RELATED OE/RR STATUS   | ##   ##   ## Comment                                                                                                                                                                                                                  |
|-----------------------------------|--------------------|-------------------------|-------------------------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Printed to                        |                    |                         |                         |                        | Based on the original order being signed and released, forwarded, and edit/resubmitted. The SF 513 printed at the Service is accomplished with the Consult package hard-coded format. (OE/RR print templates cannot include results.) |
| Received                          |                    |                         |                         | ACTIVE                 |                                                                                                                                                                                                                                       |
| Schedule                          | X                  | X                       |                         | ACTIVE                 | The Schedule action does not actually schedule an appointment or link to the scheduling package. It does allow a convenient way to annotate a consult after an appointment has been scheduled by some other means.                    |
| Service Entered                   |                    |                         |                         | ACTIVE                 | Currently unavailable.                                                                                                                                                                                                                |
| Sig Finding Update                | X                  | X                       |                         |                        | May be used independently from Administrative Complete action from 2.5.                                                                                                                                                               |
| Status Change                     | X                  |                         |                         | ACTIVE                 | Used by TIU when a note is disassociated from a consult and there are no other results associated with the it.                                                                                                                        |
| Unknown Action                    | X                  |                         |                         | NO STATUS              | Used in displays if action is unknown.                                                                                                                                                                                                |

### Actions

#### Brief Action Descriptions

##### Review Only Actions

**DD** The ***Detailed Order Display*** action displays specific order activities and details, audit/tracking trails and results.

**CT** The ***New Date Range*** allows you to change date range while in the Consult Tracking screen. This date range change does not change the patient or require you to select a new patient. It is a subordinate action to Change View (CV).

**CV** The ***Change View*** action gives you the capability to view consults by Service, Status, or Date Range. This is done by adding the modifying action to CV as such: CV;SS for Select Service. CV;ST for View by Status. CV;DT for New Date Range.

**PF** The **Print Form** action produces a copy of SF 513.

**RT** The ***Results Display*** action displays the results of the consult or procedure request order.

**SP** The ***Select New Patient*** action allows you to select a new patient’s name at any time, while using this option, rather than having to log out of the option and log back in.

**SS** The ***Select Service*** action allows you to select a different service/specialty in which to review orders. It is a subordinate action to Change View (CV).

**ST** The **View by Status** action allows you to select one or more statuses to display on the screen. It is a subordinate action to Change View (CV).

**CM** This action synonym may be entered at the Select prompt if the Service/Specialty wishes to add a ***Comment*** to an existing consult order. An example is a comment indicating that the requesting clinician wants a HOLD put on an order that has already been Received and is active in a Service/Specialty.

**ER** Although the ***Edit/Resubmit*** action shows up on the Review Only menu, it can only be executed by the originating provider or an update user. When a consult is cancelled or denied for clerical reasons (such as insufficient data), then the information on the consult  can be edited and resubmitted it with this action. Alternatively, the originating provider may perform this function from the alert.

**Q** The ***Quit*** action exits all Consults options.

##### Update Actions

**CT** The ***Complete Request*** action updates the CPRS status of a consult from Active to Completed. When the patient’s consult review screen is displayed again, both the consult’s current status and the Last Activity field will be updated to indicate that the consult’s new current status is Completed.

Complete Request also links you to TIU so that you can enter findings.

**CX** The ***Cancel*** *(or* ***Deny) Request*** action may be used by Service personnel to deny a request for completion of a consult/procedure received by their Service. A comment concerning the reason for denial must added when using this action.

**DC** The ***Discontinue Order*** action allows Service/Specialty personnel to change an order’s current status and Last Activity field to Discontinued. In addition, a comment may be added concerning the reason for discontinuance.

**FR** Entering the ***Forward Request*** allows you to forward a consult or request to any other Service/Specialty, provided that Service/ Specialty has been set up by IRM personnel to receive consults on line. As an example, this action could be used when Cardiology Service has mistakenly received a consult that should have been sent to Hematology Service.

**MA** The ***Make Addendum*** action allows one or more people to add their comments to the results of a consult. Contrast this to Add Comment, which adds a note to the consult.

**RC** The ***Received Request*** action is used by a Service/Specialty to acknowledge receipt of a new consult/request in the Service and to update the current CPRS status of the consult/request to Active rather than Pending. The Last Activity field on the patient’s review screen will also be updated to indicate that the consult was Received.

**RM	The** ***Remove Medicine Results*** action is used when a medicine result has been attached to a consult in error. Its use is restricted, but generally speaking, it can be done by anyone who can attach medicine results.

**SC** The ***Schedule*** action can be used by a Service/Specialty to annotate a consult that an appointment has been scheduled for the patient. (It does not schedule an appointment or link to the Scheduling Package.)

**SF** The ***Significant Findings*** action is used by a Service/ Specialty to mark a consult has having significant findings. When the Sig Findings flag is set to “Y” an asterisk is placed next to the consult in the review display.

Note:	Actions that require you to select an existing order can be done in one of two ways:

Select the action.

Select the order.

Or

Select the order.

Select the action.

The actions that are affected by this are:

DD	Detailed Order Display

CM	Comment Order

CT	Complete Request

DC	Discontinue Order

CY	Deny Request

FR	Forward Request

RC	Received Request

SC	Schedule

ER	Edit/Resubmit

#### Add Comment (CM) Action

The Add Comment action allows you to append a comment to a consult order when important information about the consult needs to be added to the original order or when a caregiver needs to furnish information before the consult is ready to be closed out.

The Add Comment action can be performed by any user.

To use the Comment Order action from Windows:

- From the Consults tab, highlight the consult you want to add a comment to.
- Select Action|Consult Request|Add Comment.

<!-- image -->

<!-- image -->

#### Cancel (or Deny) Consult

The Cancel action is one of several options the receiving clinic or service uses to process a request (see **Forward the Consult** under **Work Flow** page 23).

The originating clinician is automatically sent an alert that the request has been canceled.

This action is provided for all update options in the Consults package.

Example:

Select Consult Management Option: **CS** Consult Service Tracking

Select Patient: **CPRSPATIENT,FO** UR           01-01-51     666123456     YES     SC VET

ERAN

Select Service/Specialty: ALL SERVICES// **PUL** MONARY

List From Starting Date:  ALL DATES // **&lt;Enter&gt;** ALL DATES

CONSULT TRACKING              Jun 19, 1997 04:21:18          Page:   1 of   1

CPRSPATIENT,FOUR 666-43-8796          2B M              DEC 4,1949 (50)   &lt;CAD&gt;

Wt.(lb): 184

Requested  St     No.   Consult/Procedure Request

1  02/03/97   a      999   PULMONARY Consult

2  02/03/97   a      989   PULMONARY Consult

3  02/03/97   c      929  *PULMONARY Consult

4  02/03/97   c      873  *PULMONARY Consult

5  01/09/97   c      872   PULMONARY UGI

6  09/06/96   dc     500   PULMONARY ECHO

7  03/05/92   dc     444   PULMONARY Electrocardiogram

Enter ?? for more actions

SP Select Patient   FR Forward          CT Complete/Update  RT Results Display

CV Change View ...  CX Cancel (Deny)    MA Make Addendum    PF Print Form 513

RC Receive          DC Discontinue      SF Sig Findings     RM Remove Med Rslt

SC Schedule         CM Add Comment      DD Detailed Display ER Edit/Resubmit

Select: Quit// **CX** Cancel (Deny)

CHOOSE No. 1-2: **2**

Responsible Clinician: **CPRSPROVIDER** ,TWO         CRS          PHYSICIAN

Date/Time of Actual Activity: NOW// **&lt;Enter&gt;** (JUN 19, 1997@04:21)

Enter COMMENT:

1&gt;Duplicate Consult

2&gt; &lt;Enter&gt;

EDIT Option: **&lt;Enter&gt;**

(Continued on next page.)

CONSULT TRACKING              Jun 19, 1997 04:22:02          Page:   1 of   1

CPRSPATIENT,FOUR 666-43-8796          2B M              DEC 4,1949 (50)   &lt;CAD&gt;

Wt.(lb): 184

Requested  St     No.   Consult/Procedure Request

1  02/03/97   x      999   PULMONARY Consult

2  02/03/97   a      989   PULMONARY Consult

3  02/03/97   c      929  *PULMONARY Consult

4  02/03/97   c      873  *PULMONARY Consult

5  01/09/97   c      872   PULMONARY UGI

6  09/06/96   dc     500   PULMONARY ECHO

7  03/05/92   dc     444   PULMONARY Electrocardiogram

Enter ?? for more actions

SP Select Patient   FR Forward          CT Complete/Update  RT Results Display

CV Change View ...  CX Cancel (Deny)    MA Make Addendum    PF Print Form 513

RC Receive          DC Discontinue      SF Sig Findings     RM Remove Med Rslt

SC Schedule         CM Add Comment      DD Detailed Display ER Edit/Resubmit

Select: Quit//

The originating clinician then has the option of editing and resubmitting the request. This is done either from the view alerts function, or from the consult tracking screen with the Edit/Resubmit (ER) action. An update user for the subject service may also edit and resubmit a canceled consult.

#### Change View (CV) Action

The Change View action is really three different actions packaged into one. They are:

- View by Status (ST)
- Change Date Range (DT)
- Select Service (SS)

Enter the CV action followed by one of these three options. You can do this as two different entries, or you can put both commands on the same line separated by a semicolon, like this: CV;DT

In the following example we use the CV action to display selected statues:

With this action you can selectively display consults on the Consult Tracking screen base on the consult’s status. In the following example, the display is changed to view only consults with a status of Pending or Discontinued. For a list of consult statuses and their meanings, see page 108.

CONSULT TRACKING              Jul 30, 1997 09:21:02          Page: 1 of    2

CPRSPATIENT,FOUR 666-43-8796          2B M              DEC 4,1949 (50)   &lt;CAD&gt;

Wt.(lb): 184

Requested  St     No.   Consult/Procedure Request

1   10/06/00   p      1766  EYE CLINIC Cons

2   09/21/00   p      1764  Electrocardiogram CARDIOLOGY Proc

3   04/25/00   s      1713  CARDIOLOGY Cons

4   03/21/00   c      1701  CARDIOLOGY (SOUTH) Cons

5   02/22/00   pr     1687  PULMONARY (SOUTH) Cons

6   01/26/00   c      1665  CARDIOLOGY Cons

7   06/02/99   c      1483  VENTRICAL LEAD IMPLANT CARDIOLOGY Proc

8   04/29/99   a      1455  CARDIOLOGY (oex) CARDIOLOGY Cons

9   02/18/99   x      1395  CARDIOLOGY Cons

10  01/06/99   c      1322  M'S SPECIALTY SEA-M'S SPECIALTY Cons

11  01/05/99   c      1310 *GASTROENTEROLOGY CARDIOLOGY Cons

12  01/04/99   c      1287  CARDIOLOGY Cons

+         Enter ?? for more actions

SP Select Patient         RT Results Display        ER Edit/Resubmit

CV Change View ...        PF Print Form 513

DD Detailed Display       CM Add Comment

Select Consult: Next Screen// **CV** Change View ...

DT   Date Range

ST   Status

SS   Service

Only Display Consults With Status of: All Status's// **p** Pending

Another Status to display: **s** Scheduled

Another Status to display: **a** Active

Another Status to display: **&lt;Enter&gt;**

(Continued on the next page.)

CONSULT TRACKING              Jul 30, 1997 09:21:10          Page:   1 of   1

CPRSPATIENT,FOUR 666-43-8796          2B M              DEC 4,1949 (50)   &lt;CAD&gt;

Wt.(lb): 184

Requested  St     No.   Consult/Procedure Request

1   10/06/00   p      1766  EYE CLINIC Cons

2   09/21/00   p      1764  Electrocardiogram CARDIOLOGY Proc

3   04/25/00   s      1713  CARDIOLOGY Cons

8   04/29/99   a      1455  CARDIOLOGY (oex) CARDIOLOGY Cons

Enter ?? for more actions

SP Select Patient         RT Results Display        ER Edit/Resubmit

CV Change View ...        PF Print Form 513

DD Detailed Display       CM Add Comment

Select Consult: Quit//

#### Complete Request (CT) Action

The Complete Request action which updates a consult order’s CPRS status to completed (c).

Using the CT action informs the system that you are completely finished with a consult or procedure. An alert is sent to the originating provider and marks the record of the consult as complete.

Finally, the Complete action links you to TIU so that you can enter results. See page 26 for an example of this feature.

If a user is set up as either an Administrative User or on an Administrative User Team, the option exists to perform an Administrative Complete. In the GUI (Windows) interface, this is a separate command under Action | Consult Tracking. In List Manager, if the user has Administrative privileges, then the program asks if an Administrative Complete should be performed. (An Administrative complete does not have results attached to it.)

#### Deny Request (DY) Action

The Deny Request action has been subsumed by the Cancel action. See Cancel (CX) Action on page 116.

#### Detailed Order Display (DD) Action

The Detailed Order Display action provides a list of all consult information contained in the computer file.

Example:

Select Consult Management Option: **CS** Consult Service Tracking

Select Patient: **CPRSPATIENT,FOUR** CPRSPATIENT,FOUR         12-04-49     666438796       SC VETERAN

Select Service/Specialty: ALL SERVICES// **PUL** MONARY

List From Starting Date:  ALL DATES // **&lt;Enter&gt;** ALL DATES

CONSULT TRACKING              Nov 01, 1997 13:55:32          Page:   1 of   1

CPRSPATIENT,FOUR 666-43-8796          2B M              DEC 4,1949 (50)   &lt;CAD&gt;

Wt.(lb): 184

Requested  St     No.   Consult/Procedure Request

1   11/01/97   c       675  PULMONARY Consult

2   10/06/00   p       566  EYE CLINIC Cons

3   09/21/00   p       464  Electrocardiogram CARDIOLOGY Proc

Enter ?? for more actions

SP Select Patient   FR Forward          CT Complete/Update  RT Results Display

CV Change View ...  CX Cancel (Deny)    MA Make Addendum    PF Print Form 513

RC Receive          DC Discontinue      SF Sig Findings     RM Remove Med Rslt

SC Schedule         CM Add Comment      DD Detailed Display ER Edit/Resubmit

Select:Quit// **DD** Detail Display

Select Consult Number: 1

You can do just the opposite of the example above, i.e., you can select a consult first then type the action DD. The result is the same.

(Continued on next page.)

CONSULTS DETAILED DISPLAY     Nov 01, 1997 13:55:42          Page:   1 of   5

CONSULT DETAILED DISPLAY                             Consult No.: 675

CPRSPATIENT,TWO     666-67-1996     DOB: MAR 5,1949 (48)  Wt. (lb): No Entry

Current Inpatient/Outpatient: Inpatient

Ward:                  2B

Eligibility:           SC VETERAN

To Service:            PULMONARY

From Service:          MEDICINE

Reason For Request:    Pt experiences shortness of breath when out of

bed.

Status:                COMPLETE

ATTENTION:            CPRSPROVIDER,TWO

Place:                Bedside

Urgency:              Routine

Request Activity      Date/Time       Ordering Clinician  Entered By

11/01/97 10:13  CPRSPROVIDER,ONE    CPRSPROVIDER,ONE

RECEIVED              11/01/97 10:15  CPRSPROVIDER,ONE    CPRSPROVIDER,ONE

+         Enter ?? for more actions

Select Action:Next Screen// **&lt;Enter&gt;**

CONSULTS DETAILED DISPLAY     Nov 01, 1997 14:00:20          Page:    2 of  5

CONSULT DETAILED DISPLAY                             Consult No.: 675

CPRSPATIENT,TWO     666-67-1996     DOB: MAR 5,1949 (48)  Wt. (lb): No Entry

+

COMPLETED             11/01/97 10:17  CPRSPROVIDER,ONE   CPRSPROVIDER,ONE

----------------------------- TIU CONSULT REPORT -------------------------------

Source Information

Reference Date: NOV 01, 1997@10:15:35            Author: CPRSPROVIDER,ONE

Entry Date: NOV 01, 1997@10:15:35        Entered By: CA

Expected Signer: CPRSPROVIDER,ONE     Expected Cosigner: None

Urgency: None                    Document Status: COMPLETED

Line Count: 21                       TIU Document #: 2330

Subject: None

Associated Problems   No linked problems.

Edit Information

Edit Date: NOV 01, 1997@10:17:23         Edited By: CPRSPROVIDER,ONE

+         Enter ?? for more actions

Select Action:Next Screen// **&lt;Enter&gt;**

(Continued on next page.)

CONSULTS DETAILED DISPLAY     Nov 01, 1997 14:02:13          Page:   3 of   5

CONSULT DETAILED DISPLAY                             Consult No.: 675

CPRSPATIENT,TWO     666-67-1996     DOB: MAR 5,1949 (48)  Wt. (lb): No Entry

+

Reassignment History   Document Never Reassigned.

Signature Information

Signed Date: NOV 01, 1997@10:17:35         Signed By: CPRSPROVIDER,ONE

Signature Mode: ELECTRONIC

Cosigned Date: None                        Cosigned By: None

Cosignature Mode: None

Document Body

At the time I went to examine the pt, he was acutely broncho-

spastic and in moderately severe respiratory distress.  I had him

deliver a puff of albuterol with an Aerochamber; his technique was

poor. I then instructed him and delivered an additional four puffs,

which he did with good technique.  He was improved and with a clear

lung exam within a few seconds (though wheezes were still present

+         Enter ?? for more actions

Select Action:Next Screen// **&lt;Enter&gt;**

CONSULTS DETAILED DISPLAY     Nov 01, 1997 14:03:47          Page:   4 of   5

CONSULT DETAILED DISPLAY                             Consult No.: 675

CPRSPATIENT,TWO     666-67-1996     DOB: MAR 5,1949 (48)  Wt. (lb): No Entry

+

on forced expiration).

The pt regimen is lacking in inhaled corticosteroids.  Recognizing

that asthma is an inflammatory process, inhaled steroids are important

in controlling the inflammatory response.  My practice for severely

out-of-control asthmatics is to use high-dose inhaled steroids,

typically vanceril, 16 puffs qid, with a spacing device such as the

Aerochamber. I would institute such a regimen while he is here.

The pt has an in-house pet dog and an outside pet cat.  I have

told him that the cat should go, even if it is outdoors.  Cat saliva

contains a glycoprotein that leaves residue on their coats and flakes

into the air; it is problematic for many asthmatics.

The purulent phlegm asthmatics have during exacerbations is usually

+         Enter ?? for more actions

Select Action:Next Screen// **&lt;Enter&gt;**

(Continued on the next page.)

CONSULTS DETAILED DISPLAY     Nov 01, 1997 14:07:36          Page:   5 of   5

CONSULT DETAILED DISPLAY                             Consult No.: 675

CPRSPATIENT,TWO     666-67-1996     DOB: MAR 5,1949 (48)  Wt. (lb): No Entry

+

due to the eosinophils, not from infection.  Antibiotics are usually

not necessary.

If you like, you may refer Mr. Bud to my clinic after discharge.

==================================== END =====================================

Enter ?? for more actions

Select Action:Quit//

#### Discontinue Order (DC) Action

The Discontinue Order (DC) action is used by clinical personnel to stop a consult/procedure request after it has been signed. This differs from the cancel action in that there is not Edit/Resubmit action available on a discontinued order.

In the example below, the Discontinue Order action is used to cancel a duplicate order:

Select OPTION NAME: **GMRC MG** R          Consult Management      menu

Select Consult Management Option: cs  Consult Service Tracking

Select Patient: **CPRSPATIENT,FOUR** CPRSPATIENT,FOUR         12-04-49     666438796       SC VETERAN

Select Service/Specialty: ALL SERVICES// **PUL** MONARY

List From Starting Date:  ALL DATES // **&lt;Enter&gt;** ALL DATES

CONSULT TRACKING              Jun 19, 1997 09:31:19          Page:   1 of   1

CPRSPATIENT,FOUR 666-43-8796          2B M              DEC 4,1949 (50)   &lt;CAD&gt;

Wt.(lb): 184

Requested  St     No.   Consult/Procedure Request

1   10/06/00   p      1766  EYE CLINIC Cons

2   09/21/00   p      1764  Electrocardiogram CARDIOLOGY Proc

3   04/25/00   c      1713  CARDIOLOGY Cons

4   03/21/00   c      1701  CARDIOLOGY (SOUTH) Cons

5   02/22/00   pr     1687  PULMONARY (SOUTH) Cons

6   01/26/00   c      1665  CARDIOLOGY Cons

7   06/02/99   c      1483  VENTRICAL LEAD IMPLANT CARDIOLOGY Proc

8   04/29/99   c      1455  CARDIOLOGY (oex) CARDIOLOGY Cons

9   02/18/99   x      1395  CARDIOLOGY Cons

10  01/06/99   c      1322  MARCIA'S SPECIALTY SEA-MARCIA'S SPECIALTY Cons

11  01/05/99   c      1310 *GASTROENTEROLOGY CARDIOLOGY Cons

12  01/04/99   c      1287  CARDIOLOGY Cons

Enter ?? for more actions

SP Select Patient   FR Forward          CT Complete/Update  RT Results Display

CV Change View ...  CX Cancel (Deny)    MA Make Addendum    PF Print Form 513

RC Receive          DC Discontinue      SF Sig Findings     RM Remove Med Rslt

SC Schedule         CM Add Comment      DD Detailed Display ER Edit/Resubmit

Select Consult: Quit// **DC** Discontinue

CHOOSE No. 1-7: **3**

Responsible Clinician: **CPRSPROVIDER,TWO** CRS          PHYSICIAN

Date/Time of Actual Activity: NOW// **&lt;Enter&gt;** (JUN 19, 1997@09:31)

Enter COMMENT:

1&gt;Duplicate

2&gt; &lt;Enter&gt;

EDIT Option: **&lt;Enter&gt;**

(Continued on next page.)

CONSULT TRACKING              Jun 19, 1997 09:31:58          Page:   1 of   1

CPRSPATIENT,FOUR 666-43-8796          2B M              DEC 4,1949 (50)   &lt;CAD&gt;

Wt.(lb): 184

Requested  St     No.   Consult/Procedure Request

1   10/06/00   p      1766  EYE CLINIC Cons

2   09/21/00   p      1764  Electrocardiogram CARDIOLOGY Proc

3   04/25/00   dc     1713  CARDIOLOGY Cons

4   03/21/00   c      1701  CARDIOLOGY (SOUTH) Cons

5   02/22/00   pr     1687  PULMONARY (SOUTH) Cons

6   01/26/00   c      1665  CARDIOLOGY Cons

7   06/02/99   c      1483  VENTRICAL LEAD IMPLANT CARDIOLOGY Proc

8   04/29/99   c      1455  CARDIOLOGY (oex) CARDIOLOGY Cons

9   02/18/99   x      1395  CARDIOLOGY Cons

10  01/06/99   c      1322  MARCIA'S SPECIALTY SEA-MARCIA'S SPECIALTY Cons

11  01/05/99   c      1310 *GASTROENTEROLOGY CARDIOLOGY Cons

12  01/04/99   c      1287  CARDIOLOGY Cons

Enter ?? for more actions

SP Select Patient   FR Forward          CT Complete/Update  RT Results Display

CV Change View ...  CX Cancel (Deny)    MA Make Addendum    PF Print Form 513

RC Receive          DC Discontinue      SF Sig Findings     RM Remove Med Rslt

SC Schedule         CM Add Comment      DD Detailed Display ER Edit/Resubmit

Select Consult: Quit//

#### Edit/Resubmit (ER)   Action

In the case where a consult is cancelled (or denied) for clerical reasons (e.g., test results that indicate that the consult is needed), then the original submitter or an update user for the relevant service has a chance to edit the consult to include the missing information and resubmit it. This may be done from either the alert screen, or from the consult tracking screen. In either case, the procedure is the same. See **Consult/Request Cancel/Hold** on page 150 for an example.

#### Forward Request (FR) Action

Entering the Forward Request allows you to forward a consult or request to any other Service/Specialty, provided that Service/Specialty has been set up by IRM personnel to receive consults online. Thus, the decision by the referring clinician regarding who should receive the consult can be modified by the receiving Service/Specialty. This action is available from both the CPRS screen and the Consult/Request Alerts screen.

If a request needs to be forwarded to a clinic that is not a sub-service of your clinic, the FR (Forward Request) action should be used. This action is discussed in the **Forward the Consult** section under **Work Flow** on page **23** .

#### Make Addendum (MA) Action

The Make Addendum action allows one or more people to add their comments to the results of a consult. Contrast this to Add Comment, which adds a note to the consult before it is resulted.

There is an example of Make Addendum in the Windows section on page 86.

#### Print Form (PF) Action

With the Print Form Action, you can print either a chart or working copy of the consult form. To use this action from the Windows interface, follow these steps:

From the Consults tab, select the consult you want to print.

- Select File | Print Form.
- Select the printer you want the form to come out on.
- Choose Chart Copy or Work Copy.
- Choose OK.

For an example of the Print Form option as used from the List Manager interface, see page 29.

<!-- image -->

#### Print Screen Contents (PS) Action

This option prints the information that is on the screen. The output is not exactly a screen image, as it does not include the prompt area at the bottom of the screen. To print the entire contents of a consult request, use the Print Form (PF) action.

Example:

CONSULTS DETAILED DISPLAY     Jun 20, 1997 10:40:56        Page:    1 of    2

CONSULT DETAILED DISPLAY                             Consult No.: 208

CPRSPATIENT,FOUR 666-43-8796          2B M              DEC 4,1949 (50)   &lt;CAD&gt;

Current Inpatient/Outpatient: Inpatient

Ward:                  1A

Eligibility:           SC VETERAN

To Service:            PULMONARY

From Service:

Provisional Diagnosis: Broken interface with CPRS.

Reason For Request:    Checking action of DY (denying) a consult as to

DC (discontinuing) a consult.

Status:                DISCONTINUED

Urgency:              SWITCH BED

Request Activity      Date/Time       Ordering Clinician  Entered By

ENTERED IN OE/RR      03/05/97 16:09  CPRSPROVIDER,TWO    CPRSPROVIDER,TWO

//

Forwarded From MEDICINE

+         Enter ?? for more actions

Select Action:Next Screen// ps   PS

DEVICE: HOME// laser  PRINTER ROOM LN11 12 PITCH

DO YOU WANT YOUR OUTPUT QUEUED? NO//   (NO)

#### Quit (Q) Action

Enter the Quit (Q) action at the last Select prompt to quit using your Consults option.

Users may enter Q to Quit or ^ to Exit the option at any time.

#### Receive Request (RC) Action

Performing the Receive action on a consult changes its status from Pending to Active. This puts your clinic on record as accepting responsibility for completing the consult.

On page 25 we give an example of receiving a consult from a consult tracking screen. This is an example of receiving a consult from a notification alert:

You have PENDING ALERTS

Enter  "VA   VIEW ALERTS     to review alerts

Select OE/RR Manager Menu Option: **VA** View Alerts

1.  CPRSPATIENT,FOUR (C8796): New  Consult/Request ()

2.  CPRSPATIENT,TWO (C9600): New Consult/Request  (Today)

4.  CPRSPATIENT,ONE (C3456): Consult/Request DENIED Consult

Select from 1 to 6

or enter ?, A I, F, P, M, R, or ^ to exit: **1**

Consult/Request Alerts      Feb 13, 1998 13:34:56      Page:   1 of  1

CPRSPATIENT,FOUR 666-43-8796          2B M              DEC 4,1949 (50)   &lt;CAD&gt;

Wt.(lb): 184

Number    Date     Stat  Service           Procedure

187      02/14/97 p     NEUROLOGY         Consult

Enter ?? for more actions

SP Select Patient   FR Forward          CT Complete/Update  RT Results Display

CV Change View ...  CX Cancel (Deny)    MA Make Addendum    PF Print Form 513

RC Receive          DC Discontinue      SF Sig Findings     RM Remove Med Rslt

SC Schedule         CM Add Comment      DD Detailed Display ER Edit/Resubmit

Select: Quit// RC   Receive Request

Who received it?: **CPRSPROVIDER,ONE** OC

Date/Time Actually Received: NOW//    (FEB 13, 1998@13:36)

(Continued on the next page.)

Consult/Request Alerts      Feb 13, 1998 13:36:52       Page:   1 of   1

CPRSPATIENT,FOUR 666-43-8796          2B M              DEC 4,1949 (50)   &lt;CAD&gt;

Wt.(lb): 184

Number    Date     Stat  Service           Procedure

187       02/14/97 a     NEUROLOGY         Consult

Enter ?? for more actions

SP Select Patient   FR Forward          CT Complete/Update  RT Results Display

CV Change View ...  CX Cancel (Deny)    MA Make Addendum    PF Print Form 513

RC Receive          DC Discontinue      SF Sig Findings     RM Remove Med Rslt

SC Schedule         CM Add Comment      DD Detailed Display ER Edit/Resubmit

Select: Quit//

#### Remove Medicine Results (RM)

This action is used when a medicine result has been attached to a consult in error. Its use is restricted, but generally speaking, it can be done by anyone who can attach medicine results.

Attaching medicine results is done in conjunction with the Complete (CT) action in List Manager. See the section on medicine resulting on page 52 for details. In Windows, attaching and detaching medicine results are accomplished thru their own menu commands that are activated whenever medicine results are available. Fore an example of medicine results in Windows, refer to the Windows Quick Start section on page 74.

In this example, we use List Manager to remove an incorrect medicine results:

CONSULT TRACKING              Mar 02, 2001@13:53:35          Page:    1 of    1

CPRSPATIENT,FOUR 666-43-8796          2B M              DEC 4,1949 (50)   &lt;CAD&gt;

Wt.(lb): 184

Requested  St     No.   Consult/Procedure Request

1   03/02/01  p       599  ELECTROCARDIOGRAM CARDIOLOGY Proc

2   02/21/01  c       597  ELECTROCARDIOGRAM CARDIOLOGY Proc

3   10/10/96  a       242  ELECTROCARDIOGRAM CARDIOLOGY Proc

4   09/08/95  c       187  CARDIOLOGY CLINIC Cons

5   08/14/95  pr      183  12 LEAD STAT EKG CARDIOLOGY Proc

6   08/14/95  c       184  12 LEAD STAT EKG CARDIAC TRANSPLANT Proc

7   04/29/94  pr       53  ECHO CARDIOLOGY Proc

8   04/29/94  pr       54  ECHO CARDIOLOGY Proc

9   04/29/94  p        55  ECHO CARDIOLOGY Proc

Enter ?? for more actions

SP Select Patient   FR Forward          CT Complete/Update  RT Results Display

CV Change View ...  CX Cancel (Deny)    MA Make Addendum    PF Print Form 513

RC Receive          DC Discontinue      SF Sig Findings     RM Remove Med Rslt

SC Schedule         CM Add Comment      DD Detailed Display ER Edit/Resubmit

Select: Quit// **RM**

CHOOSE No. 1-9: **1**

Procedure/Medicine Resulting  Mar 02, 2001@11:34:48          Page:    1 of    1

CPRSPATIENT,FOUR 666-43-8796          2B M              DEC 4,1949 (50)   &lt;CAD&gt;

Consult No.: 242             Associated Medicine Results

1   ELECTROCARDIOGRAM       OCT 2,1995@10:00    ABNORMAL

Select action or item number

DM Disassociate result    DR Display Result

Select Action:Quit// **DM**

Select item:  (1-1): **1**

ELECTROCARDIOGRAM       OCT 2,1995@10:00    ABNORMAL

Are you sure you want to disassociate this result? NO// **Y** YES

#### Results Display (RT) Action

The Results Display (RT) action allows you to review results of any consult/request for a patient.

The following is an example of the report displayed when you select the RT action:

C S L T   R E S U L T S   D I S P L A Y

CPRSPATIENT,FOUR 666-43-8796          2B M              DEC 4,1949 (50)   &lt;CAD&gt;

---------------------- ELECTROCARDIOGRAM SUMMARY REPORT ---------------------

DIAGNOSIS

Interpretation Code (rhythm):  SINUS TACHYCARDIA

Interpretation Code (config):  ABNORMAL ECG

INDICATIONS

Type OF EKG:                   STAT RETRIEVAL

SUMMARY

Summary:                       ABNORMAL

Summary procedure:             Sinus rhythm has replaced atrial flutter

Press return to continue or “^” to escape **&lt;Enter&gt;**

#### Schedule (SC) Action

The Schedule action is similar to the Receive (RC) action in that it changes the status of a consult. There is no interface with the Scheduling Package at this time. This action is intended only for annotation purposes.

Unlike the Receive action, this action sends an alert. You can use this alert to inform the requestor of the date and time of the appointment.

In the following example we change the status of a consult from “p” pending to “s” scheduled:

CONSULT TRACKING              Jun 08, 2000 21:14:16          Page:    1 of    1

CPRSPATIENT,FOUR 666-43-8796          2B M              DEC 4,1949 (50)   &lt;CAD&gt;

Wt.(lb): 184

Requested  St     No.   Consult/Procedure Request

1   07/22/99   p      1561  EXERCISE TOLERANCE TEST CARDIOLOGY Proc

2   05/20/99   p      1470  CARDIOLOGY (oex) CARDIOLOGY Cons

3   04/13/99   c      1437  CARDIOLOGY (oex) CARDIOLOGY Cons

4   04/01/99   c      1429  CARDIOLOGY (oex) CARDIOLOGY Cons

5   02/26/99   c      1406  CARDIOLOGY Cons

6   01/05/99   c      1312  CARDIOLOGY Cons

7   01/04/99   c      1290 *CARDIOLOGY Cons

8   12/18/98   c      1252  CARDIOLOGY Cons

9   12/14/98   c      1234  CARDIOLOGY Cons

Enter ?? for more actions

SP Select Patient   FR Forward          CT Complete/Update  RT Results Display

CV Change View ...  CX Cancel (Deny)    MA Make Addendum    PF Print Form 513

RC Receive          DC Discontinue      SF Sig Findings     RM Remove Med Rslt

SC Schedule         CM Add Comment      DD Detailed Display ER Edit/Resubmit

Select: Quit// **SC** Schedule

CHOOSE No. 1-9: **2**

Who scheduled it?: CPRSPROVIDER,ONE  CPRSPROVIDER,ONE  OC          PHYSICIAN

Enter COMMENT...

1&gt;9:30 pm Jun 23 in Bldg 4

2&gt; &lt;Enter&gt;

EDIT Option: **&lt;Enter&gt;**

Do You Wish To Send An Alert With This Comment? N// **Y** YES

Send Alert To Requesting Provider CPRSPROVIDER,THREE? N// **Y** YES

Send Alert to: **&lt;Enter&gt;**

Processing Alerts...

(Continued on the next page.)

CONSULT TRACKING              Jun 08, 2000 21:16:45          Page:    1 of    1

CPRSPATIENT,FOUR 666-43-8796          2B M              DEC 4,1949 (50)   &lt;CAD&gt;

Wt.(lb): 200

Requested  St     No.   Consult/Procedure Request

1   07/22/99   p      1561  EXERCISE TOLERANCE TEST CARDIOLOGY Proc

2   05/20/99   s      1470  CARDIOLOGY (oex) CARDIOLOGY Cons

3   04/13/99   c      1437  CARDIOLOGY (oex) CARDIOLOGY Cons

4   04/01/99   c      1429  CARDIOLOGY (oex) CARDIOLOGY Cons

5   02/26/99   c      1406  CARDIOLOGY Cons

6   01/05/99   c      1312  CARDIOLOGY Cons

7   01/04/99   c      1290 *CARDIOLOGY Cons

8   12/18/98   c      1252  CARDIOLOGY Cons

9   12/14/98   c      1234  CARDIOLOGY Cons

Enter ?? for more actions

SP Select Patient   FR Forward          CT Complete/Update  RT Results Display

CV Change View ...  CX Cancel (Deny)    MA Make Addendum    PF Print Form 513

RC Receive          DC Discontinue      SF Sig Findings     RM Remove Med Rslt

SC Schedule         CM Add Comment      DD Detailed Display ER Edit/Resubmit

Select: Quit//

#### Select New Patient (SP) Action

This option allows you to change patients at any time.

Example:

CONSULT TRACKING              Jun 20, 1997 14:44:26          Page:   1 of   1

CPRSPATIENT,FOUR 666-43-8796          2B M              DEC 4,1949 (50)   &lt;CAD&gt;

Wt.(lb): 184

Requested  St     No.   Consult/Procedure Request

1   08/18/99   a      1586  PULMONARY Cons

2   08/18/99   a      1585  PULMONARY Cons

3   06/23/99   c      1545  PULMONARY Cons

Enter ?? for more actions

SP Select Patient   FR Forward          CT Complete/Update  RT Results Display

CV Change View ...  CX Cancel (Deny)    MA Make Addendum    PF Print Form 513

RC Receive          DC Discontinue      SF Sig Findings     RM Remove Med Rslt

SC Schedule         CM Add Comment      DD Detailed Display ER Edit/Resubmit

Select: Quit// **SP** New Patient

Select Patient: **CPRSPATIENT,THREE** 01-01-51     666123456     YES     SC VETERAN

Select Service/Specialty: ALL SERVICES// **PUL** MONARY

List From Starting Date:  ALL DATES // **&lt;Enter&gt;** ALL DATES

(Continued on the next page.)

CONSULT TRACKING              Jun 20, 1997 14:44:38          Page:   1 of   1

CPRSPATIENT,THREE             666-12-3456   2B              MAR 3,1960 (40)   &lt;AD&gt;

Wt.(lb): 184

Requested  St     No.   Consult/Procedure Request

1   09/14/98   c      1163  PULMONARY Cons

2   09/09/98   dc     1162  PULMONARY Cons

3   07/14/98   dc     1116  PULMONARY Cons

4   07/14/98   c      1114 *CARDIOLOGY PULMONARY Cons

Enter ?? for more actions

SP Select Patient   FR Forward          CT Complete/Update  RT Results Display

CV Change View ...  CX Cancel (Deny)    MA Make Addendum    PF Print Form 513

RC Receive          DC Discontinue      SF Sig Findings     RM Remove Med Rslt

SC Schedule         CM Add Comment      DD Detailed Display ER Edit/Resubmit

Select:  Quit//

#### Significant Findings (SF) Action

The Significant Findings action allows a clinic or service to append a significant findings flag onto a consult (whether completed or not). The action prompts you to enter a comment and sends an alert either at the time the SF action is taken or when the consult is complete. An asterisk is placed next to the consults that have a Significant Findings value of Y.

In this example we add a significant finding to an already completed consult:

CONSULT TRACKING              May 01, 1998 14:51:35        Page:    1 of    2

CPRSPATIENT,THREE             666-12-3456   2B              MAR 3,1960 (40)   &lt;AD&gt;

Wt.(lb): 184

Requested  St     No.   Consult/Procedure Request

1   09/21/00   p      1764  Electrocardiogram CARDIOLOGY Proc

2   04/25/00   c      1713  CARDIOLOGY Cons

3   01/26/00   c      1665  CARDIOLOGY Cons

4   06/02/99   c      1483  VENTRICAL LEAD IMPLANT CARDIOLOGY Proc

5   04/29/99   c      1455  CARDIOLOGY (oex) CARDIOLOGY Cons

6   02/18/99   x      1395  CARDIOLOGY Cons

7   01/05/99   c      1310 *GASTROENTEROLOGY CARDIOLOGY Cons

8   01/04/99   c      1287  CARDIOLOGY Cons

9   12/18/98   c      1249  CARDIOLOGY Cons

10  10/09/98   c      1184  CARDIOLOGY Cons

11  08/24/98   dc     1144  CARDIOLOGY Cons

12  07/13/98   c      1113 *CARDIOLOGY Cons

+         Enter ?? for more actions

SP Select Patient   FR Forward          CT Complete/Update  RT Results Display

CV Change View ...  CX Cancel (Deny)    MA Make Addendum    PF Print Form 513

RC Receive          DC Discontinue      SF Sig Findings     RM Remove Med Rslt

SC Schedule         CM Add Comment      DD Detailed Display ER Edit/Resubmit

Select: Next Screen// **SF** Sig Findings

CHOOSE No. 1-17: **1**

Current Significant Findings = not entered yet

Are there significant findings? (Y/N/U): unknown// yes

Enter COMMENT:

1&gt;Pt experiencing 60% loss of breathing efficiency.

2&gt;

EDIT Option:

Alert will be sent to Requesting Provider: CPRSPROVIDER,TWO

Send Alert to: CPRSPROVIDER,TWO added to the list.

And Send Alert to: CPRSPROVDER,THREE already in the list.

And Send Alert to:

Processing Alerts...

(Continued on the next page.)

CONSULT TRACKING              May 01, 1998 14:52:28        Page:    1 of    2

CPRSPATIENT,THREE             666-12-3456   2B              MAR 3,1960 (40)   &lt;AD&gt;

Wt.(lb): 184

Requested  St     No.   Consult/Procedure Request

1   09/21/00   p      1764 *Electrocardiogram CARDIOLOGY Proc

2   04/25/00   c      1713  CARDIOLOGY Cons

3   01/26/00   c      1665  CARDIOLOGY Cons

4   06/02/99   c      1483  VENTRICAL LEAD IMPLANT CARDIOLOGY Proc

5   04/29/99   c      1455  CARDIOLOGY (oex) CARDIOLOGY Cons

6   02/18/99   x      1395  CARDIOLOGY Cons

7   01/05/99   c      1310 *GASTROENTEROLOGY CARDIOLOGY Cons

8   01/04/99   c      1287  CARDIOLOGY Cons

9   12/18/98   c      1249  CARDIOLOGY Cons

10  10/09/98   c      1184  CARDIOLOGY Cons

11  08/24/98   dc     1144  CARDIOLOGY Cons

12  07/13/98   c      1113 *CARDIOLOGY Cons

+         Enter ?? for more actions

SP Select Patient   FR Forward          CT Complete/Update  RT Results Display

CV Change View ...  CX Cancel (Deny)    MA Make Addendum    PF Print Form 513

RC Receive          DC Discontinue      SF Sig Findings     RM Remove Med Rslt

SC Schedule         CM Add Comment      DD Detailed Display ER Edit/Resubmit

Select: Next Screen//

### Notifications about Consults and Requests

During your session, you may notice:

You have PENDING ALERTS

Enter "VA VIEW ALERTS to review alerts

Select Clinician Menu Option:

This appears on the screen before each prompt. You may enter VA at any menu prompt in which this message appears to view patient information related to pending notifications.

There are six notifications relating to consults:

| OE/RR Notifications                   |   Notification Number | Recipients                                                                                                                                      |
|---------------------------------------|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| New Service Consult/Request           |                    27 | Service Users plus Attention                                                                                                                    |
| Consult/Request Resolution            |                    23 | Ordering Provider on Complete                                                                                                                   |
| Consult/Request Cancel/Hold           |                    30 | Ordering Provider and others as determined by who is taking the action.  The NOTIFY ON DC field in file 123.5 affects who gets the alert on DC. |
| Consult/Request Update                |                    63 | Determined by the individual taking the associated action.*                                                                                     |
| Order(s) Require Electronic Signature |                     5 | Determined by CPRS                                                                                                                              |
| Prosthetics Consult Updated           |                    89 | Determined by the individual taking the associated action.  See the Add Prosthetics Consult Updated section for more details.                   |

The purpose of these notifications is to allow you to take appropriate follow-up action. This might involve merely reading new information, or it might involve several actions on your part such as scheduling an appointment, signing a consult, resubmission, etc.

*NOTE:

- When a comment is added by an UPDATE USER, the alert will only go to the ordering provider (unless additional alert recipients are added).
- When a comment is added by a SERVICE TEAM member, the alert will only go to the ordering provider (unless additional alert recipients are added).
- Any additional recipients added during the Add Comment Action will receive the alert, even if a selected recipient has the alert Disabled.

To initiate the follow-up action, enter VA at the prompt after the view alerts message. In the following example, a user follows up a notification by signing an order:

You have PENDING ALERTS

Enter "VA VIEW ALERTS to review alerts

Select CPRS Manager Menu Option: **VA** View Alerts

1. CPRSPATIENT,ONE (C4723): New order(s) placed.

2. CPRSPATIENT,THREE (C3456): Consult/Request DENIED To Service: PODIATRY

3. CPRSPATIENT,ONE (C4723): Order requires electronic signature.

Select from 1 to 3

or enter ?, A I, F, P, M, R, or ^ to exit

or RETURN to continue: **3**

Processing alert: CPRSPATIENT,ONE (C4723): Order requires electronic signature.

Searching the patient's chart ...

Unsigned Orders                Sep 24, 1997 09:22:04            Page: 1 of 1

CPRSPATIENT,THREE             666-12-3456   2B              MAR 3,1960 (40)   &lt;AD&gt;

Selected date range: None Selected

Item Ordered                                Requestor     Start   Stop     ts

1    &gt;&gt; Weight *UNSIGNED*                      | CPRSPROVIDER,O                 unr

2    Consult to CARDIOLOGY Consultant's Choice | CPRSPROVIDER,O                 unr

*UNSIGNED*                                |

3    Consult to CARDIOLOGY Consultant's Choice | CPRSPROVIDER,O                 unr

*UNSIGNED*                                |

Enter the numbers of the items you wish to act on.

Enter the numbers of the items you wish to act on.                 &gt;&gt;&gt;

+   Next Screen                - Previous Screen             Q Quit

Select: Quit// **2**

Unsigned Orders                Sep 24, 1997 09:22:04            Page: 1 of 1

CPRSPATIENT,THREE             666-12-3456   2B              MAR 3,1960 (40)   &lt;AD&gt;

Selected date range: None Selected

Item Ordered                                Requestor    Start   Stop     Sts

1    &gt;&gt; Weight *UNSIGNED*                      | CPRSPROVIDER,O                 unr

2    Consult to CARDIOLOGY Consultant's Choice | CPRSPROVIDER,O                 unr

*UNSIGNED*                                |

3    Consult to CARDIOLOGY Consultant's Choice | CPRSPROVIDER,O                 unr

*UNSIGNED*                                |

Enter the numbers of the items you wish to act on.

Enter the numbers of the items you wish to act on.                 &gt;&gt;&gt;

Change                                  Sign

Discontinue                             Detailed Display

Enter your electronic signature here.

<!-- image -->

Consult to CARDIOLOGY Consultant's Choice –

Enter your Current Signature Code:    SIGNATURE VERIFIED

Consult to CARDIOLOGY Consultant's Choice signed.

Searching the patient's chart ...

(Continued on the next page.)

Unsigned Orders                Sep 24, 1997 09:22:04            Page: 1 of 1

CPRSPATIENT,THREE             666-12-3456   2B              MAR 3,1960 (40)   &lt;AD&gt;

Selected date range: None Selected

Item Ordered                                Requestor     Start  Stop      ts

1    &gt;&gt; Weight *UNSIGNED*                      | CPRSPROVIDER,O                 unr

3    Consult to CARDIOLOGY Consultant's Choice | CPRSPROVIDER,O                 unr

*UNSIGNED*                                |

Enter the numbers of the items you wish to act on.

Enter the numbers of the items you wish to act on.                 &gt;&gt;&gt;

+   Next Screen                - Previous Screen             Q Quit

Select: Quit//

#### Enabling Notifications

In many cases Notifications will not come to you automatically. To find out what Notifications you should be getting, you can run the Show Me the Notifications I Can Receive option from the Notifications Management Menu. If this report shows any notifications you want to receive that are disabled, you may enable them with the Enable/Disable My Notifications option.

In this example we run the Show Me the Notifications I Can Receive report and then enable Consult/Request Cancel/Hold, Consult/Request Resolution, and New Service Consult/Request (Notice that Order(s) Require Electronic Signature is already on):

Select Notification Mgmt Menu Option: **?**

1      Enable/Disable My Notifications

2      Erase All of My Notifications

3      Set Notification Display Sort Method (GUI)

4      Send me a MailMan bulletin for Flagged Orders

5      Show Me the Notifications I Can Receive

6      Set Surrogate to Receive My Notifications

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Notification Mgmt Menu Option: **5** Show Me the Notifications I Can Receive

Would you like help understanding the list of notifications? No// **Y** (Yes)

DEVICE: HOME// **&lt;Enter&gt;** VAX

Notification List Help Message                    Page:   1

The delivery of notifications as alerts is determined from values set for:

Users, OE/RR Teams, Service/Sections, Inpatient Locations,

Hospital Divisions, Computer System and Order Entry/Results Reporting.

Possible values include 'Enabled', 'Disabled' and 'Mandatory'. These values

indicate a User's, OE/RR Team's, Service's, Location's, Division's, System's

and OERR's desire for the notification to be 'Enabled' (sent under most

conditions), 'Disabled' (not sent), or 'Mandatory' (almost always sent.)

All values, except the OERR (Order Entry) value, can be set by IRM

or Clinical Coordinators. Individual users can set 'Enabled/Disabled/Mandatory'

values for each specific notification via the 'Enable/Disable My Notifications'

option under the Personal Preferences and Notification Mgmt Menu option menus.

'ON' indicates the user will receive the notification under normal conditions.

'OFF' indicates the user normally will not receive the notification.

Notification recipient determination can also be influenced by patient

location (inpatients only.) This list does not consider patient location

when calculating the ON/OFF value for a notification.

- End of Report -

Press RETURN to continue: **&lt;Enter&gt;**

This will take a moment or two, please stand by.................................

...............

DEVICE: HOME// **&lt;Enter&gt;** VAX

Notification List for CPRSPROVIDER,ONE           Page:   1

Notification                      ON/OFF For This User and Why

--------------------------------  ---------------------------------------------

ABNORMAL IMAGING RESULTS          ON   OERR value is Mandatory

ABNORMAL LAB RESULT (INFO)        ON   User value is Mandatory

ABNORMAL LAB RESULTS (ACTION)     OFF  OERR value is Disabled

ADMISSION                         ON   OERR value is Enabled

CONSULT/REQUEST CANCEL/HOLD       ON   User value is Mandatory

CONSULT/REQUEST RESOLUTION        ON   User value is Mandatory

CONSULT/REQUEST UPDATED           OFF  OERR value is Disabled

CRITICAL LAB RESULT (INFO)        ON   OERR value is Mandatory

CRITICAL LAB RESULTS (ACTION)     ON   OERR value is Mandatory

DC ORDER                          OFF  OERR value is Disabled

DECEASED PATIENT                  ON   OERR value is Enabled

DISCHARGE                         OFF  OERR value is Disabled

DNR EXPIRING                      OFF  OERR value is Disabled

ERROR MESSAGE                     OFF  OERR value is Disabled

FLAG ORDER FOR CLARIFICATION      ON   OERR value is Enabled

FLAGGED OI EXPIRING - INPT        OFF  OERR value is Disabled

FLAGGED OI EXPIRING - OUTPT       OFF  OERR value is Disabled

FLAGGED OI ORDER - INPT           OFF  OERR value is Disabled

FLAGGED OI ORDER - OUTPT          ON   System value is Enabled

FLAGGED OI RESULTS - INPT         OFF  OERR value is Disabled

FLAGGED OI RESULTS - OUTPT        OFF  OERR value is Disabled

FOOD/DRUG INTERACTION             OFF  OERR value is Disabled

FREE TEXT                         OFF  OERR value is Disabled

IMAGING PATIENT EXAMINED          OFF  User value is Disabled

IMAGING REQUEST CANCEL/HELD       ON   OERR value is Enabled

IMAGING RESULTS                   OFF  User value is Disabled

IMAGING RESULTS AMENDED           OFF  OERR value is Disabled

LAB ORDER CANCELED                OFF  OERR value is Disabled

LAB RESULTS                       OFF  OERR value is Disabled

MEDICATIONS EXPIRING              OFF  OERR value is Disabled

NEW ORDER                         OFF  OERR value is Disabled

NEW SERVICE CONSULT/REQUEST       ON   User value is Mandatory

NPO DIET MORE THAN 72 HRS         OFF  OERR value is Disabled

ORDER CHECK                       OFF  OERR value is Disabled

ORDER REQUIRES CHART SIGNATURE    ON   OERR value is Mandatory

ORDER REQUIRES CO-SIGNATURE       OFF  OERR value is Disabled

ORDER REQUIRES ELEC SIGNATURE     ON   OERR value is Mandatory

ORDERER-FLAGGED RESULTS           OFF  OERR value is Disabled

SERVICE ORDER REQ CHART SIGN      ON   OERR value is Mandatory

STAT IMAGING REQUEST              OFF  OERR value is Disabled

STAT ORDER                        OFF  OERR value is Disabled

STAT RESULTS                      OFF  OERR value is Disabled

TRANSFER FROM PSYCHIATRY          OFF  OERR value is Disabled

UNSCHEDULED VISIT                 ON   OERR value is Enabled

UNVERIFIED MEDICATION ORDER       OFF  OERR value is Disabled

UNVERIFIED ORDER                  OFF  OERR value is Disabled

URGENT IMAGING REQUEST            OFF  OERR value is Disabled

- End of Report -

Select Notification Mgmt Menu Option: **1** Enable/Disable My Notifications

Enable/Disable My Notifications

-------------------------------------------------------------------------------

------------------- Setting   for User: CPRSPROVIDER,ONE -------------------

Select Notification: cons

1   CONSULT/REQUEST CANCEL/HOLD

2   CONSULT/REQUEST RESOLUTION

3   CONSULT/REQUEST UPDATED

CHOOSE 1-3: **3** CONSULT/REQUEST UPDATED

Are you adding CONSULT/REQUEST UPDATED as a new Notification? Yes// **&lt;Enter&gt;** YES

Notification: CONSULT/REQUEST UPDATED// **&lt;Enter&gt;** CONSULT/REQUEST UPDATED   CONSULT/REQUEST UPDATED

Value: **?**

Code indicating processing flag for the entity and notification.

Select one of the following:

M         Mandatory

E         Enabled

D         Disabled

Value: **E** nabled

Select Notification: &lt;Enter&gt;

Select Notification Mgmt Menu Option:

#### New Service Consult/Request

This notification is triggered by the Consults package when a new consult has been requested by a user.

In the following example, the system displays three notifications for new Consults:

CPRSPATIE (C5377): New consult Neuro (Stat)

CPRSPATIE (C3456): New consult CAR (Routine)

CPRSPATIE (C6572): New consult PLM (Routine)

Enter "VA VIEW ALERTS to review alerts

Select Systems Manager Menu Option:

As a follow-up action, the system displays the consult in a Consult/Tracking screen so that the recipient can take appropriate action. To initiate the follow-up action, enter VA at the prompt and select the notification you want to follow-up on. After selecting this notification from the View Alerts menu, the system deletes the notification.

In the following example, a new consult is first examined and then a receive action is performed:

1.   CPRSPATIE (C2342): NEW consult CAR (Routine)

2.   CPRSPATIE (C2432): Consult COMPLETED: CAR

Select from 1 to 3

or enter ?, A I, F, P, M, R, or ^ to exit

or RETURN to continue: **A**

Processing alert: CPRSPATIENT,NINE (C2342): NEW consult  (Routine)

Consult/Request Alerts        Feb 13, 1998 13:43:55        Page:    1 of    1

CPRSPATIENT,NINE         666-24-2342   1A              MAR 3,1960 (40)   &lt;AD&gt;

Wt.(lb): 184

Number       Date    St  Service                    Procedure

1          12/16/97  p   CARDIOLOGY                 EKG Portable

Enter ?? for more actions

SP Select Patient   FR Forward          CT Complete/Update  RT Results Display

CV Change View ...  CX Cancel (Deny)    MA Make Addendum    PF Print Form 513

RC Receive          DC Discontinue      SF Sig Findings     RM Remove Med Rslt

SC Schedule         CM Add Comment      DD Detailed Display ER Edit/Resubmit

Select Action: Quit// **DD** Detailed Display

Compiling Report...

CONSULTS DETAILED DISPLAY     Dec 19, 1997 08:12:04        Page:    1 of    5

CONSULT DETAILED DISPLAY                             Consult No.: 731

CPRSPATIENT,FORTY     000-00-0040     DOB:  (74)  Wt. (lb): No Entry

Current Inpatient/Outpatient: Inpatient

Ward:                  1A

To Service:            CARDIOLOGY

From Service:          1A

Consult Type:          EKG Portable

Provisional Diagnosis: Cardiomyopathy

Reason For Request:    Rule out alternate diagnosis

Status:                PENDING

Service is to be rendered on an INPATIENT basis

ATTENTION:            CPRSPROVIDER,SEVEN

Place:                Bedside

Urgency:              Stat

Request Activity      Date/Time       Ordering Clinician  Entered By

CPRS RELEASED ORDER   12/16/97 15:52  CPRSPROVIDER,SEVEN  CPRSPROVIDER,SEVEN

+         Enter ?? for more actions

Select Action: Next Screen// **Q** Q

Consult/Request Alerts        Feb 13, 1998 13:44:53        Page:    1 of    1

CPRSPATIENT,NINE         666-24-2342   1A              MAR 3,1960 (40)   &lt;AD&gt;

Wt.(lb): 184  Number Date    St  Service                    Procedure

1          12/16/97  p   CARDIOLOGY                 EKG Portable

Enter ?? for more actions

SP Select Patient   FR Forward          CT Complete/Update  RT Results Display

CV Change View ...  CX Cancel (Deny)    MA Make Addendum    PF Print Form 513

RC Receive          DC Discontinue      SF Sig Findings     RM Remove Med Rslt

SC Schedule         CM Add Comment      DD Detailed Display ER Edit/Resubmit

Select Action: Quit// **RC** Receive

Who received it?: **CPRSPROVIDER,SEVEN** SC

Date/Time Actually Received: NOW//   (DEC 19, 1997 @ 08:12)

(Continued on the next page.)

Consult/Request Alerts        Dec 19, 1997 08:13:01        Page:    1 of    1

CPRSPATIENT,NINE         666-24-2342   1A              MAR 3,1960 (40)   &lt;AD&gt;

Wt.(lb): 184  Number Date    St  Service                    Procedure

1          12/16/97  a   CARDIOLOGY                 EKG Portable

Enter ?? for more actions

SP Select Patient   FR Forward          CT Complete/Update  RT Results Display

CV Change View ...  CX Cancel (Deny)    MA Make Addendum    PF Print Form 513

RC Receive          DC Discontinue      SF Sig Findings     ER Edit/Resubmit

SC Schedule         CM Add Comment      DD Detailed Display

Select Action: Quit// **&lt;Enter&gt;** QUIT

Continue Processing ALERTS ? Y//

#### Consult/Request Resolution

**NOTE** : This notification is typically triggered by the Consults package when it determines that a consult is complete but may also be triggered when an associated result has been amended or removed.

In the following example, the originating provider receives notifications that consults are complete:

CPRSPATIE (C3456): Completed Consult CAR HOLTER

CPRSPATIE (C1996): *Completed Consult CAR

CPRSPATIE (C8910): Completed Consult PSURG

Enter "VA   VIEW ALERTS      to review alerts

Select Systems Manager Menu Option:

As a follow-up action, the system displays the Consult/Request and results/report. To initiate the follow-up action, enter VA at the prompt and select the notification you want to follow-up on. After viewing, the system deletes the notification.

Notice the asterisk on the second notification. This means that there are significant findings for that consult.

The less common usage for the Consult/Request Resolution notification applies to amending or reassigning results. In the following example, the signed result was amended, and the originating provider received notification that the consult has been reactivated, followed immediately by another notification that the consult has been completed. The two back-to-back notifications are a result of the software processing the amendment action on the document, which essentially translates into a disassociate result activity for the consult, followed immediately by the signature (completion) action for the document. In this scenario, the consult would not have any other linked documents already in a completed status.

If, during the result removal, the consult does not change status, but does have significant findings, the alert text will appear as: “*Removed consult note for"

CPRSPATIE (C3456): Reactivated consult, removed note for VASCULAR SURGERY

CPRSPATIE (C3456): Completed Consult VASCULAR SURGERY

CPRSPATIE (C7890): *Removed consult note for AUDIOLOGY OUTPT

CPRSPATIE (C1996): *Completed Consult CAR

CPRSPATIE (C8910): Completed Consult PSURG

Enter "VA   VIEW ALERTS      to review alerts

#### Consult/Request Updated

This alert is triggered when a comment is added to consult, or the consult is scheduled.  Comments may be added either with the Add Comment (CM) action or the Schedule (SC) action. The text of the alert is altered depending on which one of these actions initiated the alert as follows:

**Adding a Comment #63** "Comment Added to Consult: . . ."

**Scheduling #63** "Scheduled Consult:  . . ."

As a follow-up action, the system displays the consult with comments. If appropriate, the clinician may write an additional comment or take other actions as needed.

- When a comment is added by an UPDATE USER, the alert will only go to the ordering provider (unless additional alert recipients are added).
- When a comment is added by a SERVICE TEAM member, the alert will only go to the ordering provider (unless additional alert recipients are added).
- Any additional recipients added during the Add Comment action will receive the alert, even if a selected recipient has the alert Disabled.

This alert is also used by the Healthcare Claims Processing System (HCPS) to notify VA providers the status of a patient who has been referred to a Non-VA Care provider or facility. When an HCPS user enters a comment in RAS, CPRS is updated. The HCPS user might not be a user in VistA; a proxy user will display for ‘Responsible Person’ and ‘Entered By’ in the CPRS, as shown below:

Facility

Activity                Date/Time/Zone      Responsible Person  Entered By

-------------------------------------------------------------------------------

ADDED COMMENT           08/08/14 22:31      HCPS,APPLICATION    HCPS,APPLICATION

(entered) 08/08/14 22:40

Author: CPRSPROVIDER,TEN

#### Consult/Request Cancel/Hold

This notification is triggered from the Consults package when a Consult request is cancelled, discontinued, or put on hold.

In the following example, a user receives notification of a discontinued and a denied consult:

CPRSPATIE (C2342): Cancelled consult CAR

CPRSPATIE (C9876): Discontinued Consult MEDICINE

CPRSPATIE (C3456): Cancelled consult POD

Enter "VA   VIEW ALERTS      to review alerts

Select Systems Manager Menu Option:

As a follow-up action, the system displays consult with comments. If appropriate, the submitter may resubmit the consult based on this new information. To initiate the follow-up action, enter VA at the prompt and select the notification you want to follow-up on. After viewing, the notification is deleted by the system.

In the following example, a cancelled order is edited and resubmitted:

You have PENDING ALERTS

Enter  "VA   VIEW ALERTS     to review alerts

Select Consult Service Tracking Option: **VA** View Alerts

1.   CPRSPATIE (C2342): Cancelled consult to PLM

2.   CPRSPATIE (C3456): Discontinued consult to CAR

3.   CPRSPATIE (C2432): Completed Consult CAR

Select from 1 to 3

or enter ?, A I, F, P, M, R, or ^ to exit

or RETURN to continue: **1**

Processing alert: CPRSPROVIDER,EI (E8840): Cancelled consult PLM

(Continued on next page.)

Edit Consult Order            Feb 26, 1999 15:58:08          Page:    1 of    2

Edit Consult for Patient CPRSPATIENT,EIGHT  Consult Number: 1336

Sending Provider: CPRSPROVIDER,SEVEN

Field Name                   Current Field Contents

CURRENT STATUS: (Not Editable): CANCELLED

CANCELLED BY (Not Editable): CPRSPROVIDER,SEVEN

CANCELLED COMMENT (Not Editable):

Testing edit.

------------------------------------------------------------------------------

CANCELLED BY (Not Editable): CPRSPROVIDER,SEVEN

CANCELLED COMMENT (Not Editable):

Testing edit/resubmit.

------------------------------------------------------------------------------

SENDING PROVIDER (Not Editable): CPRSPROVIDER,SEVEN

REQUEST TYPE (Not Editable): Consult

-------------------------------------------------------------------------------

1 TO SERVICE: PULMONARY

2 PROCEDURE:

3 Performed as INPT OR OUTPT: Outpatient

+         Enter ?? for more actions

ED Edit A Field           RS ReSubmit Consult

Select Action: Next Screen// **&lt;Enter&gt;**

Edit Consult Order            Feb 26, 1999 16:01:18          Page:    2 of    2

Edit Consult for Patient CPRSPATIENT,EIGHT  Consult Number: 1336

Sending Provider: CPRSPROVIDER,SEVEN

+ Field Name                   Current Field Contents

4 URGENCY: Routine

5 PLACE OF CONSULTATION:

6 ATTENTION (CONSULTANT):

7 PROVISIONAL DIAGNOSIS:

8 REASON FOR REQUEST:

Pt has trouble breathing.

9 COMMENT(S): (Add Only)

ADDED COMMENT (Not Editable) Entered: Jan 11, 1999 BY: CPRSPROVIDER,SEVEN

Testing, more testing.

Enter ?? for more actions

ED Edit A Field           RS ReSubmit Consult

Select Item/Action:Quit// **7**

(Continued on the next page.)

Edit Consult Order            Feb 02, 1999 10:44:38          Page:    2 of    2

Edit Consult for Patient CPRSPATIENT,NINE  Consult Number: 1366

Sending Provider: CPRSPROVIDER,SEVEN

+ Field Name                   Current Field Contents

8 REASON FOR REQUEST:

Pt is having chest pains.

9 COMMENT(S): (Add Only)

Enter ?? for more actions

ED Edit A Field           RS ReSubmit Consult

Select Item/Action:Quit// **ED** Edit A Field

Select the fields to edit: **7**

Provisional Diagnosis: **Angina**

Edit Consult Order            Feb 26, 1999 16:06:16          Page:    2 of    2

Edit Consult for Patient CPRSPATIENT,EIGHT  Consult Number: 1336

Sending Provider: CPRSPROVIDER,SEVEN

+ Field Name                   Current Field Contents

4 URGENCY: Routine

5 PLACE OF CONSULTATION:

6 ATTENTION (CONSULTANT):

7 PROVISIONAL DIAGNOSIS: Angina

8 REASON FOR REQUEST:

Pt has trouble breathing.

9 COMMENT(S): (Add Only)

ADDED COMMENT (Not Editable) Entered: Jan 11, 1999 BY: CPRSPROVIDER,TWO

Testing, more testing.

Enter ?? for more actions

ED Edit A Field           RS ReSubmit Consult

Select Action: Quit// **&lt;Enter&gt;** QUIT

(Continued on the next page.)

This Consult Has Not Been Resubmitted!!

Resubmit Or All Edits Will Be Lost!!

Do you wish to resubmit now? ? YES// **Y** YES

Resubmitting Consult ... One moment please ...

Filing Tracking Data...

1.   CPRSPATIE (C3456): Discontinued consult to CAR

2.   CPRSPATIE (C2432): Completed Consult CAR

Select from 1 to 2

or enter ?, A I, F, P, M, R, or ^ to exit

or RETURN to continue:

##### Special Considerations for Discontinued Orders

When an order is Discontinued, who gets the notification depends on the source of the discontinuation. This is dependent on the NOTIFY ON DC field in file 123.5 for the service to which the consult was directed. This field is set by the Set up Consult Services (SS) command of the Consult Management Option.

#### Consult/Request Has an Added Comment

If a comment is added to a consult by someone in the receiving service, that person is prompted to send notification to the originator of the consult and to any other persons. Other recipients of this notification are controlled as a New Service Consult.

In the following example, a clinician in the Surgery service has added a comment:

SIMPSON,H (S9999): Comment Added to Consult CARDIOLOGY

Enter  "VA   VIEW ALERTS     to review alerts

Select Consult Management Option:

The follow-up action is to display the orders containing the comments so that you can read them.

- When a comment is added by an UPDATE USER, the alert will only go to the ordering provider (unless additional alert recipients are added).
- When a comment is added by a SERVICE TEAM member, the alert will only go to the ordering provider (unless additional alert recipients are added).

#### Order(s) Require Electronic Signature

If you do not sign a consult at the time you initiate it, the CPRS triggers a notification reminding you of the need for an electronic signature.

In the following example, three notifications are presented for Consults that need an electronic signature:

CPRSPATIE (C3456): Order requires electronic signature.

CPRSPATIE (C4723): Order requires electronic signature.

CPRSPATIE (C3234): Order requires electronic signature.

Enter  "VA   VIEW ALERTS     to review alerts

Select Systems Manager Menu Option:

The follow-up action is to display the orders requiring electronic signature in a CPRS screen so that you can use the Sign action. The system deletes the notification after you have signed the order.

#### Significant Findings for a Consult

If the status of the Significant Findings Flag is changed in any way, an alert is sent by the Consults package. As far as the recipients and delivery, this notification is treated like a Consult/ Request Resolution.

This alert may be delayed, at the user’s option, until the consult is complete.

In the example that follows, three significant findings notifications are present. One for a completed consult, one for a pending consult, and one for the Significant Findings Flag being turned off on a completed consult:

CPRSPATIE (C3456): Sig Findings for consult CAR

CPRSPATIE (C6572): Sig Findings for consult CAR

CPRSPATIE (C1432): No Sig Findings for consult PLM

Enter  "VA   VIEW ALERTS     to review alerts

Select Systems Manager Menu Option:

The follow-up action is to display the orders that have had a change in the Significant Findings Flag in the CPRS screen so that you can examine them.

#### Prosthetics Consult Updated

This alert is essentially a copy of the Consult/Request Updated alert and is intended to separate the update alert traffic between prosthetics consults and all other consults. Users not interested in updates to prosthetics requests may turn this alert off.

The Prosthetics Consult Updated alert is triggered by the Add Comment (CM) or Schedule action (SC) when those actions are taken on a consult request to a prosthetics service. 

The text of the alert is altered depending on which one of these actions initiated the alert as follows:

**Adding a Comment #89** "Comment Added to consult: . . ."

**Scheduling #89** "Scheduled Consult: . . ."

As a follow-up action, the system displays the consult with comments. If appropriate, the clinician may write an additional comment or take other actions as needed.

- When a comment is added by an UPDATE USER, the alert will only go to the ordering provider (unless additional alert recipients are added).
- When a comment is added by a SERVICE TEAM member, the alert will only go to the ordering provider (unless additional alert recipients are added).

### ADMIN KEY Reports

A new GRMC Patch for “Admin Key Reporting” has been created to generate 3 new GRMC Reports.

- GMRC RPT ADMIN RELEASE CONSULT
- GMRC RPT ADMIN REL CONS USER
- GMRC RPT ADMIN REL CONS GROUPR

These reports allow local GMRC users to generate reports that will show the overall usage of the “Administratively Released by Policy” consults.

The user steps required to access and to display these reports are:

VISTAS1:VISTA&gt;D ^XUP

Select OPTION NAME: GMRC MGR       Consult Management

RPT    Consult Tracking Reports ...

SS     Set up Consult Services

SU     Service User Management

CS     Consult Service Tracking

RX     Pharmacy TPN Consults

GU     Group update of consult/procedure requests

UA     Determine users' update authority

UN     Determine if user is notification recipient

NR     Determine notification recipients for a service

TD     Test Default Reason for Request

LH     List Consult Service Hierarchy

PR     Setup procedures

CP     Copy Prosthetics services

CCT    Menu for Closure Tools ...

DS     Duplicate Sub-Service

FS     Define Fee Services

IFC    IFC Management Menu ...

TP     Print Test Page

Select Consult Management &lt;TEST ACCOUNT&gt; Option: RPT  Consult Tracking Reports

TI     Administratively Released Consults by Title

GR     Administratively Released Consults by Group

US     Administratively Released Consults by User

ST     Completion Time Statistics

PC     Service Consults Pending Resolution

SH     Service Consults Schedule-Management Report

CC     Service Consults Completed

CP     Service Consults Completed or Pending Resolution

IFC    IFC Requests

IP     IFC Requests By Patient

IR     IFC Requests by Remote Ordering Provider

LCR    Consults Local Completion Rate

NU     Service Consults with Consults Numbers

PI     Print IFC Requests

PL     Print Consults by Provider, Location, or Procedure

PM     Consult Performance Monitor Report

PR     Print Service Consults by Status

SC     Service Consults By Status

TS     Print Completion Time Statistics Report

Select Consult Tracking Reports &lt;TEST ACCOUNT&gt; Option: ???

'Administratively Released Consults by Title'     Option name: GMRC RPT ADMIN RE

LEASE CONSULT     Synonym: TI

The ADMINISTRATIVELY RELEASED CONSULTS BY TITLE report displays counts of

the number of consults created by the OR ADMIN RBP TO CC security key

(ADMIN key) and ADMINISTRATIVELY RELEASED BY POLICY. The user will enter

a date range, and the report will be sorted by Consult Title (Request

Service name).

'Administratively Released Consults by Group'     Option name: GMRC RPT ADMIN RE

L CONS GROUPR     Synonym: GR

The ADMINISTRATIVELY RELEASED CONSULTS BY GROUP report displays counts of

the number of consults created by the OR ADMIN RBP TO CC security key

(ADMIN key) and ADMINISTRATIVELY RELEASED BY POLICY. The user will enter

a date range, and the report will be sorted by Consult Group (DS or

ADMIN).

'Administratively Released Consults by User'     Option name: GMRC RPT ADMIN REL

CONS USER     Synonym: US

The ADMINISTRATIVELY RELEASED CONSULTS BY USER report displays counts of

the number of consults created by the OR ADMIN RBP TO CC security key

(ADMIN key) and ADMINISTRATIVELY RELEASED BY POLICY. The user will enter

a date range, and the report will be sorted by User.

Select Consult Management &lt;TEST ACCOUNT&gt; Option: RPT  Consult Tracking Reports

TI     Administratively Released Consults by Title

GR     Administratively Released Consults by Group

US     Administratively Released Consults by User

ST     Completion Time Statistics

PC     Service Consults Pending Resolution

SH     Service Consults Schedule-Management Report

CC     Service Consults Completed

CP     Service Consults Completed or Pending Resolution

IFC    IFC Requests

IP     IFC Requests By Patient

IR     IFC Requests by Remote Ordering Provider

LCR    Consults Local Completion Rate

NU     Service Consults with Consults Numbers

PI     Print IFC Requests

PL     Print Consults by Provider, Location, or Procedure

PM     Consult Performance Monitor Report

PR     Print Service Consults by Status

SC     Service Consults By Status

TS     Print Completion Time Statistics Report

Select Consult Tracking Reports &lt;TEST ACCOUNT&gt; Option: TI  Administratively Rele

ased Consults by Title

Enter Consult Released Starting Date: T-90

Enter Consult Released Ending Date: T

**Admin Released Consults-Title** Oct 12, 2018@08:17:12        Page:    1 of    1

VAMC: FACILITY VAMC

From: Jul 14, 2018   To: Oct 12, 2018

Releasing Person                                      Number

COMMUNITY CARE-ADMIN-CARDIAC                          58

CPRSADMINUSER,ONE                                   48

CPRSPROVIDER,ONE                                    10

COMMUNITY CARE-DS-CARDIAC                             42

CPRSADMINUSER,ONE                                   34

CPRSPROVIDER,ONE                                    8

GRAND TOTAL 100

Enter ?? for more actions

Select Action:Quit//

TI     Administratively Released Consults by Title

GR     Administratively Released Consults by Group

US     Administratively Released Consults by User

ST     Completion Time Statistics

PC     Service Consults Pending Resolution

SH     Service Consults Schedule-Management Report

CC     Service Consults Completed

CP     Service Consults Completed or Pending Resolution

IFC    IFC Requests

IP     IFC Requests By Patient

IR     IFC Requests by Remote Ordering Provider

LCR    Consults Local Completion Rate

NU     Service Consults with Consults Numbers

PI     Print IFC Requests

PL     Print Consults by Provider, Location, or Procedure

PM     Consult Performance Monitor Report

PR     Print Service Consults by Status

SC     Service Consults By Status

TS     Print Completion Time Statistics Report

Select Consult Tracking Reports &lt;TEST ACCOUNT&gt; Option: GR  Administratively Rele

ased Consults by Group

Enter Consult Released Starting Date: T-90

Enter Consult Released Ending Date: T

**Admin Released Consults-User** Oct 12, 2018@08:15:21        Page:    1 of    1

VAMC: FACILITY VAMC

From: Jul 14, 2018   To: Oct 12, 2018

Admin &amp; DS                                            Number

ADMIN                                                 58

COMMUNITY CARE-ADMIN-CARDIAC                        58

CPRSADMINUSER,ONE                                48

CPRSPROVIDER,ONE                                 10

DS                                                    42

COMMUNITY CARE-DS-CARDIAC                           42

CPRSADMINUSER,ONE                                34

CPRSPROVIDER,ONE                                 8

GRAND TOTAL 100

Enter ?? for more actions

Select Action:Quit//

TI     Administratively Released Consults by Title

GR     Administratively Released Consults by Group

US     Administratively Released Consults by User

ST     Completion Time Statistics

PC     Service Consults Pending Resolution

SH     Service Consults Schedule-Management Report

CC     Service Consults Completed

CP     Service Consults Completed or Pending Resolution

IFC    IFC Requests

IP     IFC Requests By Patient

IR     IFC Requests by Remote Ordering Provider

LCR    Consults Local Completion Rate

NU     Service Consults with Consults Numbers

PI     Print IFC Requests

PL     Print Consults by Provider, Location, or Procedure

PM     Consult Performance Monitor Report

PR     Print Service Consults by Status

SC     Service Consults By Status

TS     Print Completion Time Statistics Report

Select Consult Tracking Reports &lt;TEST ACCOUNT&gt; Option: US  Administratively Rele

ased Consults by User

Enter Consult Released Starting Date: T-90

Enter Consult Released Ending Date: T

On the GR report above, it is possible that a consult was originally made with the Admin Key, but then forwarded to a consult service that is neither -DS or -ADMIN. In this event the consult should still show and be counted under the DS or ADMIN group heading wherever it was first created. The screen shot below is an example of that:

**Admin Released Consults-Group** Feb 01, 2019@09:56:59          Page:    1 of    1

VAMC: VAMC

From: Feb 01, 2019   To: Feb 01, 2019

Admin &amp; DS                                            Number

ADMIN                                                 2

CARDIOLOGY DENVER                                   1

CPRSADMINUSER,ONE                                1

COMMUNITY CARE-ADMIN-CARDIAC                        1

CPRSADMINUSER,ONE                                1

GRAND TOTAL 2

Enter ?? for more actions

Select Action:Quit//

**Admin Released Consults-User** Oct 12, 2018@08:15:21        Page:    1 of    1

VAMC: FACILITY VAMC

From: Jul 14, 2018   To: Oct 12, 2018

Orderable Item                                        Number

CPRSADMINUSER,ONE                                     82

COMMUNITY CARE-ADMIN-CARDIAC                        48

COMMUNITY CARE-DS-CARDIAC                           34

CPRSPROVIDER,ONE                                      18

COMMUNITY CARE-ADMIN-CARDIAC                        10

COMMUNITY CARE-DS-CARDIAC                           8

GRAND TOTAL 100

Enter ?? for more actions

Select Action:Quit//

#### UCID Display

In patch 96 a new field was created to track Community Care Consults. The field is #80 (UNIQUE CONSULT ID aka UCID) in file #123 (REQUEST/CONSULTATION). Patch 110 displays the UCID in the Consult Details at the top:

<!-- image -->

#### Cancelled to Discontinued Consults

After the installation of the GMRC*3.0*113 patch, the CSLT CANCELLED TO DISCONTINUED parameter will be set as follows:

Is the overnight cancel to discontinue job active? = NO

How many days back to start with? = 31

How many days back to end with? = 365

This parameter steers the overnight job, GMRC CHANGE STATUS X TO DC, by the date range specified in fields 2 and 3 of the multi-valued parameter. By default, upon installation, the **Is the overnight cancel to discontinue job active?** field is set to **NO** which means that it is disabled. The site is responsible for deciding if the overnight job should run and setting it to “YES” to enable it.

The overnight job then looks for consults that have been cancelled during this period. Each consult fitting the parameter criteria is evaluated as to whether the consult was resubmitted and then cancelled again on a later date. If there is no later cancellation date, the consult is discontinued by calling the $$DC^GMRCGUIA API. It is possible for specific users on a VistA site to change the date range prescribed by these parameters by adjusting the “ **How many days back to start with?** ” and the “ **How many days back to end with?** ” parameters with the following. However, if the **Is the overnight cancelled to discontinued job active?** parameter is set to **NO** the other two questions will not be asked.

Select OPTION NAME: GMRC CX TO DC PARAMETER EDIT       GMRC CX TO DC PARAMETER EDIT

GMRC CX TO DC PARAMETER EDIT

Is the overnight cancelled to discontinued job active? YES//

How many days back to start with:  (0-99999): 31// 15  09/12/2018

How many days back to end with:  (15-999999): 365// 420  08/03/2017

New contents of parameter:

Is the overnight cancelled to discontinued job active? = Y

How many days back to start with? = 15  09/12/2018

How many days back to end with? = 420  08/03/2017

## Glossary

**Action** An action in Consults can be selected throughout processing to 1) control screen movement, 2) add new consult orders, or 3) process existing orders.

**Consult** Referral of a patient by the primary care physician to another hospital service/ specialty, to obtain a medical opinion based on patient evaluation and completion of any procedures, modalities, or treatments the consulting specialist deems necessary to render a medical opinion.

**Consulting Site** In the case of Inter-Facility Consults (IFC, see below) the VA facility that originates the consult.

**Discontinued Orders** Orders that are discontinued or cancelled.

**HCPS** The Healthcare Claims Processing System is a centralized, automated system that will support the management of purchased care referrals/authorizations.

**IFC** Inter-Facility Consults permits the transmitting of consults and related information between Department of Veterans Affairs facilities. Consult requests are made to remote facilities because the needed service is not locally available or for patient convenience. Although the Consult Package is utilized in the hospital settings, Consult requests between facilities have been done manually in the past.

**Order** A request for a consult (service/sub-specialty evaluation) or procedure (Electrocardiogram) to be completed for a patient.

**Order Cancellation** A request to stop performance of a consult/procedure request; the order may be edited and reactivated

**Order Discontinuation** A request to stop (discontinue) performance of a consult/procedure request.

**Procedure Request** Any procedure (EKG, Stress Test, etc.) which may be ordered from another service/ specialty without first requiring formal consultation.

**RAS** Referral and Authorization System; see HCPS.

**Request** See Procedure Request.

**Requestor** This is the health care provider (e. g., the physician/clinician) who requests the order to be done.

**Result** A consequence of an order. Refers to evaluation or status results. When you use the Complete Request (CT) action on a consult or request, you are transferred to TIU to enter the results.

**Resulting Site** In the case of Inter-Facility Consults (IFC, see above) the remote site that performs the consult and enters the results.

**Screen Context** This term refers to the particular selection of orders displayed on the screen (e. g., Medicine consults for the patient Ralph Jones).

**Service** A clinical or administrative specialty (or department) within a Medical Center.

**Status Result** A result that indicates the processing state of an order; for example, a Pharmacy TPN Consult order may be discontinued (dc) or completed (c).

**Status Symbols** Codes used in order entry and Consults displays to designate the status of the order.


## Index

Action, 185

Action Descriptions, 124

Actions

Change View (CV), 130

Comment (CM), 127

Complete Request (CT), 132

Deny Request (DY), 133

Detailed Order Display (DD), 134

Discontinue Order (DC), 138

Edit/Resubmit (ER), 140

Forward Request (FR), 141

Order of, 126

Print Form (PF), 143

Print Screen Contents (PS), 144

Quit (Q), 145

Receive Request (RC), 146

Remove Medicine Results (RM), 148

Results Display (RT), 149

Review Only, 124

Schedule (SC), 150

Select New Patient (SP), 152

Significant Findings (SF), 154

Update/Tracking, 124

View by Status (ST), 130, 131

ACTIVE, 119, 146

Add New Orders, 15

Add Original Consult, 63

Alert Actions, 4

All My Unsigned Documents, 47

asterisk, 154

Auto-forwarding, **2** , **4**

Brief Action Descriptions, 124

Cancel (CX), 128

Cancel Request (CX), 83

CANCELLED, 119

Change Date Range (DT), 130

change signature, 20

Change View (CV), 130

Clinical Procedures, 58

Clinically Indicated Date, 18, 24, 34, 64, 84

Comment (CM), 69, 127

COMPLETE, 119

Complete a Consult (From the Consults Tab), 72

Complete a Consults (From the Notes Tab), 75

Complete Request (CT), 72, 132

Completion Time Statistics, 117

Consult, 185

Consult Service Tracking Option, 111

Consult Status, 119

Consult/Request Cancel/Hold, 169

Consult/Request Has An Added Comment, 174

Consult/Request Resolution, 167

*Consult/Request Tracking Technical Manual* , 7, 24, 30

Consult/Request Updated, 168

Consultation Form (SF 513), 24

**Consulting Site** , 185

Correcting Misdirected Results, 42

*CPRS Clinical Coordinator &amp; User Manual* , 7

*CPRS Installation Guide* , 7

*CPRS Technical Manual* , 36

Custom List, 108

Deny, 128

Deny Request (DY), 133

Detailed Display (DD), 86, 124

Detailed Order Display (DD), 134

DISCONTINUE, 119

Discontinue Order (DC), 85, 125, 138, 169

Discontinued Orders, 119, 130, 173, 185

Edit/Resubmit (ER), 140

electronic signature, 20, 21, 41, 159, 174

Enabling Notifications, 161

Enhancements Since Version 2.5, 4

FilaMan Alerts, 31

Forward Request (FR), 25, 66, 125, 141

General Service User Menu, 110

Glossary, 185

Healthcare Claims Processing System, 168, 185

HL7, 2, 5

IFC, 6, 185

IFC Requests by Remote Ordering Provider, 175

Integrated Document Management, 38

Inter-Facility Consults, 6

Introduction, 1

Make Addendum (MA), 92, 142

Management, 9

Manuals, 7

Medical Records Committee, 24

Medicine Package, 54, 59

Medicine Results), 79

New Date Range, 96

New Service Consult/Request, 164

Notifications, 156

Notifications Management Menu, 161

Operation, 13

Order, 2, 185

Order Cancellation, 138, 185

Order Checking, 5

Order Discontinuation, 185

Order New Consult, 15, 63

Order of Actions, 126

Order(s) Require Electronic Signature, 174

Package Management, 9

Package Operation, 13

Package Reference, 110

PARTIAL RESULTS, 119

PENDING, 119, 146, 150

Print Form (PF) Action, 65, 143

Print Screen Contents (PS), 144

Procedure Request, 2, 111, 124, 138, 186

prompt, 41, 112, 115, 124, 144, 145, 156, 158, 164, 167, 169

Purpose, 2

Quick Orders, 36

Quit (Q) Action, 99, 145

RAS, 168, 186

Receive Request (RC) Action, 67, 146

Relations with other VISTA Components, 5

Relationship to Other Packages, 2

Remote Ordering Provider, 175

Remove Medicine Results, 80

Remove Medicine Results (RM), 148

Request, 186

Requestor, 186

Requests, 1, 2

Requests by Remote Ordering Provider, 175

Result, 42, 186

**Resulting Site** , 186

Results, 38, 124, 132

Results Display (RT), 100, 124, 149

Review Only Actions, 111, 115, 124

Schedule (SC), 150

SCHEDULED, 119, 150

Screen Context, 186

Security, 9, 10

Select Consult, 101

Select New Patient (SP), 102, 152

Select Service (SS), 104, 130

service, 2, 10, 24, 186

Service Consults Pending Resolution, 118

Service Update and Tracking Security, 9

Set up Consult Services, 173

Setup, 5

signature, 20, 21, 41, 159, 174

Significant Findings (SF), 154

Significant Findings for a Consult, 175

Starting Consults in Windows, 61

status, 10, 27, 132, 146

Status after Action, 119

Status Result, 186

Status Symbols, 119, 186

Text Integration Utility (TIU), 7, 28, 38, 125, 132

*TIU Clinical Coordinator &amp; User Manual* , 7, 38, 41

TIU Correcting Misdirected Results, 42

TIU Direct Input, 38

Tracking Option, 111

Undo Medicine Results, 80

Update/Tracking, 124

Update/Tracking Actions, 112

Update/Tracking Select Actions, 116

User Menu, 110

Using the Consults Package with TIU, 38

View by Status (ST), 105, 108, 130, 131

web pages, 7

Windows, 61

Windows Quick Start, 59

Work Flow, 14