---
app_name: 'CPRS: Consult/Request Tracking (GMRC)'
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: null
doc_type: setup-config
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-12'
is_base: false
is_change_pages: false
library_max_patch: null
package_id: GMRC
patch: null
patch_gap: null
section: ''
source_file: consifc.docx
status: draft
title: consifc.docx
---

<!-- image -->

Inter-Facility Consults

Implementation Guide

Released: April 2002

Revised: Sep 2020


Product Development

##### Revision History

| Originally released                                                                                                                                                                                                 | April 2002     |          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|----------|
| Patch 28                                                                                                                                                                                                            | October 2002   |          |
| 192-352 applied                                                                                                                                                                                                     | December 2004  | REDACTED |
| GMRC*3*53 Updated pg. 20                                                                                                                                                                                            | February 2007  | REDACTED |
| GMRC*3.0*58  Added errors 702 &amp; 703                                                                                                                                                                             | October 2008   | REDACTED |
| GMRC*3.0*63  Updated report format  pg. 19                                                                                                                                                                          | June 2009      | REDACTED |
| GMRC*3*44  Pg. 11                                                                                                                                                                                                   | January 2013)  | REDACTED |
| GMRC*3.0*154  Added section for Mail Group Enhancement for Cerner Converted Sites  pg.12  Added section for Error Handling - Cerner to VistA pg. 54                                                                 | May 2020       | REDACTED |
| GMRC*3.0*154  Changed paragraph “Error 201 Unknown Patient” from “every 3 hours” to “Every hour” pg. 40  Changed paragraph “Cerner to VistA Error 201 Unknown Patient” from “every 3 hours” to “Every hour”  pg. 55 | September 2020 | REDACTED |

Key: TW (Technical Writer)

PM (Project Manager)

###### Table of Contents

Introduction	2

Purpose of Inter-Facility Consults	2

Scope of the Manual	2

Audience	2

Coordination with Consulting Partners	4

Inter-Facility Field Relations:	5

Restrictions	5

Service Configuration at Requesting Facility	6

Service Configuration at the Consulting Facility:	8

Procedure Configuration at the Requesting Facility	9

Procedure Configuration at the Consulting Facility	10

Prosthetics Modification	11

Mail Group Setup	12

IFC PATIENT ERROR MESSAGES	12

IFC CLIN ERRORS	12

IFC TECH ERRORS	13

Mail Group Enhancement for Cerner Converted Sites	13

GMRC CRNR IFC ERRORS	14

GMRC TIER II CRNR IFC ERRORS	14

GMRC CRNR IFC CLIN ERRORS	14

GMRC CRNR IFC TECH ERRORS	14

Inter-Facility Consults Reports	16

IFC Requests	17

Print IFC Requests	20

IFC Requests by Patient	21

IFC Requests by Remote Ordering Provider	22

Inter-Facility Consults Management Options	24

Test IFC Implementation	25

Configure Test Account Patients	27

List incomplete IFC transactions	28

Print All Incomplete IFC Transactions	30

IFC Transaction Report	31

Locate IFC by Remote Consult Number	33

Edit IFC Processing Parameters	35

Monitor IFC Background Job Parameters	36

Background Task	37

Error Handling	40

Inter-Facility Consult Errors	40

Error 101—Unknown Consult/Procedure request	41

Error 201—Unknown Patient	42

Error 202—Local or Unknown MPI Identifiers	45

Error 301—Service not Matched to Receiving Facility	47

Error 401—Procedure not Matched to Receiving Facility	48

Error 501—Error in Procedure Name	49

Error 601—Multiple Services Matched to Procedure	50

Error 701—Error in Service Name	51

Error 702— Service is Disabled Error! Bookmark not defined.	52

Error 703— Procedure is Inactive	53

Error 801—Inappropriate Action for Specified Request	54

Error 802 - Duplicate, activity not filed	54

Error 901—Unable to Update Record Successfully	55

Error 902—Earlier Pending Transactions	55

Error 903—HL Logical Link not Found	56

Error 904—VistA HL7 Unable to Send Transaction	56

Error None	57

Error Handling - Cerner to VistA	58

Error 101—Unknown Consult/Procedure request	58

Error 201—Unknown Patient	58

Error 202—Local or Unknown MPI Identifiers	60

Error 301—Service not Matched to Receiving Facility	61

Error 401—Procedure not Matched to Receiving Facility	61

Error 501—Error in Procedure Name	61

Error 601—Multiple Services Matched to Procedure	61

Error 701—Error in Service Name	62

Error 702— Service is Disabled	62

Error 703— Procedure is Inactive	62

Error 801—Inappropriate Action for Specified Request	63

Error 802—Duplicate, activity not filed	63

Error 901—Unable to Update Record Successfully	63

Error 902—Earlier Pending Transactions	63

Error 903—HL Logical Link not Found	64

Error 904—HL7 Unable to Send Transaction	64

Summary of Errors	64

Test Account Setup	66

HL7 Setup (Test Accounts Only)	66

Information to Gather	66

Implementation Steps Using the HL7 Information Table	67

Managing VistA HL7	69

Patient Configuration in Test Systems	70

Index	73


## Introduction

### Purpose of Inter-Facility Consults

The Inter-Facility Consults was originally released as patch GMRC*3*22 of the Consult/Request Tracking Package. Its intention is to allow consults and requests to be transmitted between Veterans Health Administration facilities while:

- Minimizing the impact on end users of the Consults system.

### Scope of the Manual

System setup, cooperation between facilities, and management of error conditions is required for the system to work effectively. This manual provides information deemed necessary to carry out these functions.

From time to time improvements are made to the Consults package, including improvements to Inter-Facility Consults. The latest information about Consults, as well as the latest version of this manual, is posted on the Consults Web Page at:

REDACTED

or

REDACTED

In addition, a FAQ (Frequently Asked Questions) is maintained by the development team and posted at:

REDACTED or

REDACTED

### Audience

Information in this manual is technical in nature and is intended to be used by Veterans Affairs Medical Center (VAMC) Information Resource Management Service (IRMS) staff members and Clinical Application Coordinators (CAC's).

## Coordination with Consulting Partners

Before any technical implementation of the Inter-Facility Consults (IFC) software, decisions and coordination must take place with those VA facilities that will receive consults from your facility, or send consults to your facility. The entire Inter-Facility Consults process is based on proper file set up at both the requesting and consulting sites.

### Inter-Facility Field Relations:

The fields involved in Inter-Facility Consults act as pointers in that they contain the name of an object at another facility or in another file. The following table shows what the fields at the requesting facility point to:

|    |    |
|----|----|
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |

<!-- image -->

The following table shows what the fields at the consulting facility point to:

|    |    |
|----|----|
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |
|    |    |

<!-- image -->

Both consult and procedure requests may be configured for inter-facility processing. Consult request are set up using the Set up Consult Services [GMRC SETUP REQUEST SERVICES] option. Procedure requests are set up using the Setup procedures [GMRC PROCEDURE SETUP] option.

### Restrictions

Because of technical incompatibilities, the following cannot be set up for inter-facility processing:

- Procedures that are configured to be part of the Clinical Procedures interface.

Planners can work around this restriction by setting up inter-facility clinical procedures to be resulted via traditional methods.

### Service Configuration at Requesting Facility

The requesting facility must specify two pieces of information:

1. The identification of the consulting facility.
2. The service name at the consulting facility.

In the following partial terminal capture, a site such as Boise sets up to send inter-facility plastic surgery consults to the XXX HCS. Notice that SERVICE NAME is unique and indicates that the service is not performed at Boise:

Select Consult Management Option: SS Set up Consult Services

Select Service/Specialty:   PLASTIC SURGERY - XXX HCS

SERVICE NAME: PLASTIC SURGERY - XXX HCS  Replace   With  &lt;Enter&gt;

ABBREVIATED PRINT NAME (Optional): PSURG SL//

INTERNAL NAME: ??

This field holds a name that can be used for internal name-spacing.

This name will not be viewable to users when selecting a service.

This name may be used to look up entries in the file via VA FileMan

and the Setup Consult Services option.

INTERNAL NAME: IFCR SL PLASTIC SURGERY

Select SYNONYM: PSURGSL// &lt;Enter&gt;

. . .

RESTRICT DEFAULT REASON EDIT: &lt;Enter&gt;

Inter-facility information:

IFC ROUTING SITE: ?

Enter the VA site that will perform consults directed to this service

Only national institution file entries may be selected

IFC ROUTING SITE: ??

This field contains the VA facility that will perform consults requested

for this service. When a consult for this service is ordered, it will

automatically be routed to the VA facility in this field.

IFC ROUTING SITE: XXX HCS

IFC REMOTE NAME: ??

This field contains the name of the service that will be requested at

the VAMC defined in the IFC ROUTING SITE field.

Enter the name of the service exactly as it is named at the remote

facility. If this name does not match the name of the service at the

routing site, the request will fail to be filed at the remote site. This

will delay or prohibit the performance and processing of this request.

IFC REMOTE NAME: PLASTIC SURGERY

SERVICE INDIVIDUAL TO NOTIFY: &lt;Enter&gt;

. . .

The IFC REMOTE NAME must match, letter-for-letter, the service name as set up at the consulting facility. Furthermore, the consulting facility must fill in the corresponding IFC SENDING FACILITY multiple with Boise. Boise is the site name from which they will accept inter-facility consults. Note that in this case a consulting facility may have more than one entry if they consult for more than one requesting facilities.

Services that have the IFC ROUTING FACILITY and IFC REMOTE NAME fields completed, will be performed and completed by a remote facility. Although no update activities on the consult are expected at the requesting facility, you may configure update users to receive notification of activities taking place at the consulting facility.

### Service Configuration at the Consulting Facility:

At the consulting facility the Set up Consult Services action is used to set up the fact that Plastic Surgery consults will be coming from Boise HCS and Las Vegas HCS:

Select Consult Management Option: SS  Set up Consult Services

Select Service/Specialty: PLASTIC SURGERY

SERVICE NAME: PLASTIC SURGERY// &lt;Enter&gt;

ABBREVIATED PRINT NAME (Optional): PSURG //

INTERNAL NAME: ??

This field holds a name that can be used for internal name-spacing.

This name will not be viewable to users when selecting a service.

This name may be used to look up entries in the file via VA FileMan

and the Setup Consult Services option.

INTERNAL NAME: IFCL PLASTIC SURGERY

Select SYNONYM: PSURG// &lt;Enter&gt;

. . .

RESTRICT DEFAULT REASON EDIT: &lt;Enter&gt;

Inter-facility information:

Select IFC SENDING FACILITY: LAS VEGAS HCS// ??

LAS VEGAS HCS

You may enter a new IFC SENDING FACILITY, if you wish

This field contains the VA facilities that may send inter-facility

consults to this service. Only active, primary VA facilities should

be entered in this field.

Select IFC SENDING FACILITY: BOISE HCS

SERVICE INDIVIDUAL TO NOTIFY: KENT,CLARK//&lt;Enter&gt;

. . .

Notice that the Set up Consult Services action did not even prompt for the IFC ROUTING SITE or IFC REMOTE NAME. For each individual service, the condition of being a requesting facility and being a consulting facility are mutually exclusive. Facilities may fulfill both rolls, but each individual service must be set up uniquely.

The INTERNAL NAME is provided so that CACs and IRM personnel can more readily organize consults services. This provides an alternate way of accessing consult services though the Setup Service (SS) action. In other words, you can type this name at the “Select Service/Specialty:” prompt when going in to change service setup fields.

### Procedure Configuration at the Requesting Facility

Setting up inter-facility procedures is identical to setting up inter-facility consults, except that you use the Setup Procedures action.

In this example, Boise sets up Colonoscopy as in inter-facility procedure to be done at XXX HCS:

Select Consult Management Option: PR Setup procedures

Select Procedure:COLONOSCOPY – XXX HCS

...OK? Yes// &lt;Enter&gt;  (Yes)

NAME: COLONOSCOPY// &lt;Enter&gt;

INACTIVE: &lt;Enter&gt;

Select SYNONYM: COL// &lt;Enter&gt;

INTERNAL NAME: ??

This field holds a name that can be used for internal name-spacing.

This name will not be viewable to users when selecting a procedure.

This name may be used to look up entries in the file via VA

FileMan and the Setup Procedures option.

INTERNAL NAME: IFCR SL COLONOSCOPY

Select RELATED SERVICES: GASTROENTEROLOGY// &lt;Enter&gt;

TYPE OF PROCEDURE: &lt;Enter&gt;

PREREQUISITE:

No existing text

Edit? NO// &lt;Enter&gt;

PROVISIONAL DX PROMPT: &lt;Enter&gt;

PROVISIONAL DX INPUT: &lt;Enter&gt;

DEFAULT REASON FOR REQUEST:

No existing text

Edit? NO// &lt;Enter&gt;

RESTRICT DEFAULT REASON EDIT: &lt;Enter&gt;

Inter-facility information:

IFC ROUTING SITE: XXX HCS    UT  VAMC  660

IFC REMOTE PROC NAME: COLONOSCOPY

Orderable Item Updated

The IFC REMOTE PROC NAME must match, letter-for-letter, the procedure name as set up at the consulting facility. Furthermore, the consulting facility must fill in the corresponding IFC SENDING FACILITY multiple with Boise.

The PROCEDURE, on the other hand, is a local designation. We advise that you adopt some naming convention for procedures that are performed as inter-facility procedures.

The INTERNAL NAME is provided so that CACs and IRM personnel can more readily organize consult procedures. This provides an alternate way of accessing consult procedures though the Setup Procedures (PR) action. In other words, you can type this name at the SELECT PROCEDURE prompt when going in to change service setup fields.

### Procedure Configuration at the Consulting Facility

At the consulting facility the Setup Procedures action is used to set up the fact that Colonoscopy consults will be coming from Boise:

Select Consult Management Option:  Setup procedures

Select Procedure: COLONOSCOPY

...OK? Yes// &lt;Enter&gt;  (Yes)

NAME: COLONOSCOPY // &lt;Enter&gt;

INACTIVE:

Select SYNONYM: COLN// &lt;Enter&gt;

INTERNAL NAME: ??

This field holds a name that can be used for internal name-spacing.

This name will not be viewable to users when selecting a procedure.

This name may be used to look up entries in the file via VA

FileMan and the Setup Procedures option.

INTERNAL NAME: IFCL COLONOSCOPY

Select RELATED SERVICES: GASTROENTEROLOGY

// &lt;Enter&gt;

TYPE OF PROCEDURE: &lt;Enter&gt;

PREREQUISITE:

No existing text

Edit? NO// &lt;Enter&gt;

PROVISIONAL DX PROMPT: &lt;Enter&gt;

PROVISIONAL DX INPUT: &lt;Enter&gt;

DEFAULT REASON FOR REQUEST:

No existing text

Edit? NO//&lt;Enter&gt;

RESTRICT DEFAULT REASON EDIT: &lt;Enter&gt;

Inter-facility information:

IFC ROUTING SITE: &lt;Enter&gt;

IFC REMOTE PROC NAME: &lt;Enter&gt;

Select IFC SENDING FACILITY: BOISE

1   BOISE                 ID  VAMC      531

2   BOISE                 ID  RO        347

3   BOISE                 ID  M&amp;ROC     447

4   BOISE                 ID  CHEP      932

5   BOISE                 ID  VANB      5319AA

Press &lt;RETURN&gt; to see more, '^' to exit this list,

CHOOSE 1-5: 1  BOISE                 ID  VAMC      531

Are you adding 'BOISE' as a new IFC SENDING FACILITY (the 1ST for this GMRC

PROCEDURE)? No// Y  (Yes)

Select IFC SENDING FACILITY: BOISE//&lt;Enter&gt;

Orderable Item Updated

Note: 	A procedure configured as a Clinical Procedure may not be configured as an inter-facility procedure. (This is because Remote Data View does not yet handle Imaging-type data and thus would not be able to return the full results to the requesting facility.) As a work-around, clinical procedures should be resulted with traditional methods.

Note: 	Even though the RELATED SERVICE is a multiple, the consulting facility can only have *one* RELATED SERVICE entry for an inter-facility procedure.

### Prosthetics Modification

Prosthetics requested that Consults add a call to EN^RMPRFC3 for use with patch RMPR*3.0*83. This will allow Prosthetics to process Consult HL7 messages.

This lists the only fields that have to be set up when you create them for the receiving and the sending facility.

For the VAMC receiving the consult:

1. It is recommended that the service name be set up before the sending facility creates their Service/Specialty entry, because the name of this service will be shared with the sending facility.
2. (Example of RECEIVING consult service name: "PROSTHETICS IFC nnn," where "nnn" is this VAMC's three to five character station number.)
3. The data field, IFC SENDING FACILITY, must include the name(s) of the VA Medical Center(s) sending the consult. Note: this is a multiple field and more than one VAMC can send an Inter-Facility Consult to this service.

For the VAMC sending the consult:

1. Since the consult will not be processed locally, most of the data fields can be left blank. It is recommended that the service name of this consult be human readable. (Example: "PROSTHETICS IFC aaa," where aaa is text that is easily understood to be the VAMC that is RECEIVING the consult, such as the facility name or abbreviation.) It is required that the characters "IFC" are part of the consult name. The following fields are required:
    - PROVISIONAL DX PROMPT must be set to REQUIRE.
    - PROVISIONAL DX INPUT must be set to LEXICON.
    - IFC ROUTING SITE must be set to the name of the VAMC that will receive the Inter-Facility Consult.
    - IFC REMOTE NAME must be the name of the service at the receiving facility and it must exactly match the text that is entered as the receiving consult at that VAMC. If this name does not match the name of the service at the routing site, the request will fail to be filed at the remote site. This will delay or prohibit the performance and processing of this request. Coordination with the receiving facility should occur before creating this entry to avoid problems. (Example of SENDING site's IFC REMOTE NAME: "PROSTHETICS IFC nnn," where "nnn" is the three to five character station number of the VAMC that will be receiving the consult. Coordination with the RECEIVING VAMC staff is required to assure that this data is entered correctly.)

## Mail Group Setup

The Inter-facility Consults enhancement brings in three new VistA mail groups. These mail groups are created upon installation of patch GMRC*3*22 on your system. The mail groups are used to deliver alerts or mail messages to the members as a result of various occurrences in Inter-facility Consults.

Note:	All three mail groups should be populated with members having the responsibilities listed below.

### IFC PATIENT ERROR MESSAGES

The members of this mail group receive mail messages related to patient registration issues affecting Inter-facility Consults. The members of this mail group should primarily consist of MAS personnel that have the authority to register patients and resolve MPI-PD inconsistencies.

If an inter-facility consult is requested for a patient and the MPI-PD information in the patient file is either a locally assigned identifier or the patient does not have any MPI-PD information on file, the members of this mail group will receive a mail message with the patient demographics listed and indicating that an outgoing inter-facility consult request could not be sent for the reasons listed. At this point the MPI-PD information should be resolved to match the national MPI information for the patient in question.

If an inter-facility consult has been requested at another facility and is waiting to be filed on the local system, the members of this mail group will receive a VistA e-mail message listing the patient demographics at the remote facility. At this point the patient should be registered so that the incoming request may be filed and processed. When IFC cannot uniquely identify a patient at the Receiving Facility, it sends a message to the IFC PATIENT ERROR MESSAGES group. This message is re-sent at approximately 3 hour intervals.

### IFC CLIN ERRORS

The members of this mail group will receive Kernel alerts regarding issues with incomplete inter-facility consult activities that encountered an error when updating the remote consult. The members of this mail group should primarily consist of the personnel responsible for set up and implementation of the Inter-facility Consults software.

The alerts received fall into the following categories:

- Incompletely or incorrectly defined procedures or services for use in Inter-facility Consults.
- Pending Inter-facility Consult requests if registration issues exist.

When a message is sent to IFC CLIN ERRORS, it is determined by the GMRC IFC ALERT IMMED ON PT ERR parameter. If set to YES, IFC CLIN ERRORS at the sending facility is notified immediately. Otherwise, IFC CLIN ERRORS at the sending facility is notified when the registration issue is still not resolved approximately every 24 hours (or every 8 attempts to re-transmit and notify the IFC PATIENT ERROR MESSAGES group).

If a registration issue is still unresolved at the receiving facility after eight transmissions of the request, the IFC CLIN ERRORS group at the receiving facility is sent a mail message approximately every 24 hours indicating the problem and the demographics of the patient at issue.

### IFC TECH ERRORS

The members of this mail group will receive Kernel alerts regarding issues with incomplete inter-facility consult activities that did not receive an appropriate response from the facility to which an activity was transmitted. The members of this mail group should consist of those IRM staff responsible for investigating errors in the Consult/Request Tracking package and may include those responsible for monitoring VistA HL7 operation.

The alerts received by this group could be caused by either a breakdown in network communications with the remote facility or an error occurring on the remote system. This group will be responsible for resolving error conditions with inter-facility consult transmissions.

## Mail Group Enhancement for Cerner Converted Sites

The installation of patch GMRC*3.0*154 creates four new Vista mail groups. These mail groups are used to support the commercial industry standard of the receiving system responsible for handling data errors.  Cerner uses this paradigm and does not support HL7 application negative acknowledgements from VistA.  The mail groups are used to deliver alerts or mail messages to the members as a result of various occurrences in Inter-facility Consults. The members of these mail groups will receive alerts and errors when the sending site is converted to Cerner and the receiving site is a non-converted VistA.

Note:	All four mail groups should be populated with members having the responsibilities listed below.

### GMRC CRNR IFC ERRORS

The members of this mail group receive all alerts from GMRC CNR IFC CLN ERRORS, and GMRC CNR IFC TECH ERRORS mail groups. The members of this mail group are Tier I support and consists of individuals that can assist the other mail group members in analyzing errors.

### GMRC TIER II CRNR IFC ERRORS

This mail group is a subscriber to GMRC CNR IFC CLN ERRORS, GMRC CNR IFC TECH ERRORS, and GMRC CRNR IFC ERRORS mail groups.  The members of this mail group receive all alerts in order to assist Tier I members in analyzing errors. Also, members in this mail group will work directly with the facilities to resolve the errors that cannot be addressed with code changes. Members of this mail group are Tier II support and consists of the following OEHRM experts:

- MUMPS support members
- Architecture support members
- VDIF support members
- Cerner support members

### GMRC CRNR IFC CLIN ERRORS

The members of this mail group will receive Kernel alerts for  issues with incomplete inter-facility consult activities that encountered an error when updating the remote consult from a Cerner converted facility. The members of this mail group should primarily consist of the individuals responsible for set up and implementation of the Inter-facility Consults software.

The alerts received fall into the following categories:

- Incompletely or incorrectly defined procedures or services for use in Inter-facility Consults.
- Pending inter-facility consult requests if registration issues exist.

### GMRC CRNR IFC TECH ERRORS

The members of this mail group will receive Kernel alerts for issues with incomplete inter-facility consult activities that did not receive an appropriate response from the non-converted facility to which an activity was transmitted. The members of this mail group should consist of individuals responsible for investigating errors in the Consult/Request Tracking package along with those whom are responsible for monitoring HL7 operation.

The alerts received by this group could be caused by either a breakdown in network communications with the non-converted facility, OpenLink, or VDIF (Veterans Data Integration and Federation).

## Inter-Facility Consults Reports

The Inter-Facility Consults reports are available on the Consult Tracking Reports menu [GMRC REPORTS] and the IFC Management Menu [GMRC IFC MGMT]. Currently four Inter-Facility Consults reports show up on this menu. They are:

| Report Synonym   | Report Name                              | Option Name                      |
|------------------|------------------------------------------|----------------------------------|
| IFC              | IFC Requests                             | [GMRC IFC RPT CONSULTS]          |
| IP               | IFC Requests by Patient                  | [GMRC IFC RPT CONSULTS BY PT]    |
| PI               | Print IFC Requests                       | [GMRC IFC PRINT RPT NUMBERED]    |
| IR               | IFC Requests by Remote Ordering Provider | [GMRC IFC RPT CONSULTS BY REMPR] |

IFC Requests (IFC) provides detailed information regarding inter-facility consults. Inter-Facility Consult Requests (PI) is the same report formatted for a printer.

IFC Request by Patient (IP) is similar to option Consult Service Tracking, except only displays inter-facility consults as a requesting or consulting facility.

IFC Requests by Remote Ordering Provider (IR) provides detailed information regarding inter-facility consults by remote ordering provider for consulting sites to utilize. The display is similar to the IFC/PI options.

### IFC Requests

This report provides such information as:

- Total Requests to Service
- Total Requests Scheduled to Service
- Total Requests Completed to Service
- Mean Days Completed to Service

This report provides information for both requesting and consulting facilities.

In the following example, we examine all Dental consults originating by us as a requesting facility:

Select IFC Management Menu Option: IFC Inter-Facility Consult Requests

Are you the Requesting site or the Consulting site:  (R/C): R  REQUESTING

Only Display Consults With Status of: All Status's// ?

Enter a code from the list.

Select one of the following:

al        All Status's

ap        All Pending

dc        Discont.

c         Completed

p         Pending

a         Active

s         Scheduled

pr        Incomplete

x         Cancelled

Only Display Consults With Status of: All Status's// &lt;Enter&gt;  All Status's

Select Service/Specialty: DENTAL

List From Starting Date: ALL DATES// &lt;Enter&gt;

...SORRY, LET ME THINK ABOUT THAT A MOMENT...

Inter-facility Consults       Feb 07, 2002@11:06:22          Page:    1 of    1.

IFC Requests: Requesting Site

Service: DENTAL

From: ALL   To: JAN 31,2002

Status      Last Action      Request Date  Patient Name      Pt Location      .

IF Consult/Request By Status - Requesting Site

FROM: ALL   TO: JAN 31,2002

SERVICE: DENTAL

Discont.   DISCONTINUED        10/18/01 CRPatient,F. (3333)     2B MED

Discont.   DISCONTINUED        10/18/01 CRPatient,F. (1990)     1A(1&amp;2)

Completed  ADDENDUM ADDED TO   10/23/01 CRPatient,F. (3333)     2B MED

Pending    CPRS RELEASED ORDER 12/20/01 CRPatient,S. (1990)     1A(1&amp;2)

Pending    CPRS RELEASED ORDER 12/03/01 CRPatient,S. (1990)     1A(1&amp;2)

Pending    CPRS RELEASED ORDER 11/30/01 CRPatient,T. (3323)     OUTHOUSE

Pending    CPRS RELEASED ORDER 11/13/01 CRPatient,T. (3241)     2B MED

Pending    CPRS RELEASED ORDER 10/18/01 CRPatient,F. (3333)     2B MED

Pending    CPRS RELEASED ORDER 10/03/01 CRPatient,S. (1990)     1A(1&amp;2)

Pending    CPRS RELEASED ORDER 10/02/01 CRPatient,S. (1990)     2B MED

Pending    ADDED COMMENT       10/01/01 CRPatient,S. (1990)     2B MED

+         Enter ?? for more actions                                          &gt;&gt;&gt;

Service                   Number on/off             Description of Data

Status                    Print List

Select Item(s): Next Screen//

There are additional fields that are not visible on an 80 column screen such as the screen in the example. They can be viewed by using the Shift to View Right action (&gt;). Using the Shift to View Left (&lt;) action restores the screen. If the report is for a consulting site, then the additional fields are: Routing Facility, Days Diff, and Red Date. If the report is for a requesting site, then the additional fields are: Routing Facility and Days Diff.

There are five actions you can do besides the default actions (like Next Screen, Previous Screen, Quit, &gt;, &lt;, …). These are change Service, Number on/off, Description of Data, Status, and Print List.

The change Service action allows you to re-display the report for a different service.

The Number on/off action changes the format of the report to include the consult number. To do this, it preserves the other columns but makes them narrower.

The Description of Data action gives a detailed description  for applicable data columns.

The Status action allows you to change which statuses are displayed in the report. In the following example the statuses displayed are changed from All Statuses to just the Pending, Active, and Scheduled consults:

Select Item(s): Next Screen// ST   Status

Only Display Consults With Status of: All Status's// P  Pending

Another Status to display: A  Active

Another Status to display: S  Scheduled

Another Status to display: &lt;Enter&gt;

...SORRY, THIS MAY TAKE A FEW MOMENTS...

Inter-facility Consults       Feb 07, 2002@11:06:22          Page:    1 of    2

IFC Requests: Requesting Site

Service: DENTAL

From: ALL   To: FEB 7,2002

Status      Last Action      Request Date  Patient Name      Pt Location     .

IF Consult/Request By Status - Requesting Site

FROM: ALL   TO: FEB 7,2002

SERVICE: DENTAL

Pending    CPRS RELEASED ORDER 12/20/01 CRPatient,F. (1990)          1A(1&amp;2)

Pending    CPRS RELEASED ORDER 12/03/01 CRPatient,F. (1990)          1A(1&amp;2)

Pending    CPRS RELEASED ORDER 11/30/01 CRPatient,T. (3323)          OUTHOUSE

Pending    CPRS RELEASED ORDER 11/13/01 CRPatient,T. (3241)          2B MED

Pending    CPRS RELEASED ORDER 10/18/01 CRPatient,F. (3333)          2B MED

Pending    CPRS RELEASED ORDER 10/03/01 CRPatient,F. (1990)          1A(1&amp;2)

Pending    CPRS RELEASED ORDER 10/02/01 CRPatient,F. (1990)          2B MED

Pending    ADDED COMMENT       10/01/01 CRPatient,F. (1990)          2B MED

Pending    CPRS RELEASED ORDER 09/27/01 CRPatient,F. (1990)          2B MED

Pending    EDIT/RESUBMITTED    09/13/01 CRPatient,F. (1990)          2B MED

Active     DISASSOCIATE RESULT 11/05/01 CRPatient,E. (0870)          2B MED

+         Enter ?? for more actions                                          &gt;&gt;&gt;

Service                   Number on/off             Description of Data

Status                    Print List

Select Item(s): Next Screen//

### Print IFC Requests

The Print IFC Requests (PI) is the same report as the IFC Requests (IFC) except that it formats the report so you can send it to a printer device.

In the following example, all active requests for the Dental service are listed:

Select Consult Tracking Reports Option: PI  Print IFC Requests

Are you the Requesting site or the Consulting site:  (R/C): R  REQUESTING

Only Display Consults With Status of: All Status's// A  Active

Another Status to display: &lt;Enter&gt;

Select Service/Specialty: DENTAL

List From Starting Date: ALL DATES//

Want to view a description of the data for this report now? NO// &lt;Enter&gt;

This print out is 132 columns wide.

DEVICE: HOME// &lt;Enter&gt;  ANYWHERE    Right Margin: 80// &lt;Enter&gt;

IF Consult/Request By Status - Requesting Site

FROM: ALL   TO: FEB 7,2002

Number St   Last Action         Req Dt   Patient Name            Patient Loca

tion               Routing Facility        Days Diff

SERVICE: DENTAL

2085 a    DISASSOCIATE RESULT 11/05/01 WAX,F. (0870)           2B MED

BOISE                      2

2045 a    RECEIVED            10/17/01 REDDIX,H. (3333)        2B MED

BOISE                      N/A

Total Requests Active:                                     2

Total Requests Pending Resolution:                         2

Total Requests To Service @ BOISE:                         2

Mean Days Completed To Service @ BOISE:                    2

Mean Days Completed To Service:                            2

Total Requests To Service:                                 2

Press &lt;ENTER&gt; To Continue:

Notice that only two consults were displayed.

### IFC Requests by Patient

The IFC Requests by Patient (IP) report is the same as the Consult Service Tracking (CS) option, except that it only displays inter-facility consults.  As such, once it has been invoked, all actions normally available to you in the Consult Service Tracking option are potentially usable.  Some actions are only available to the Consulting (Receiving) site, as they relate to the processing of the Consult.  The Edit/Resubmit action is only available at the Requesting (Sending) site, as that is the location responsible for submitting the Consult in the first place.

Select Consult Tracking Reports Option: IP  IFC Requests By Patient

Are you the Requesting site or the Consulting site:  (R/C): R  REQUESTING

Select Patient: CRPATIENT,EIGHT        2-2-35    666333333     YES

SC VETERAN

Select Service/Specialty: ALL SERVICES// &lt;Enter&gt;  GROUPER ONLY

List From Starting Date: ALL DATES// &lt;Enter&gt;

IFC Requests: Requesting Site Feb 07, 2002@11:23:36          Page:    1 of    1

CRPATIENT,EIGHT   666-33-3333                            FEB 2,1935 (67)   &lt;CA&gt;

Wt.(lb): 180

Requested  St     No.   Consult/Procedure Request                         .

1   01/10/02  p      9927  DERMATOLOGY - Boise Cons

2   01/09/02  p      9923  DERMATOLOGY Cons

3   10/25/01  a      2061  EKG - BOISE CARDIOLOGY (SOUTH) Proc

4   10/23/01  c      2058  DENTAL Cons

5   10/18/01  dc     2051  DENTAL Cons

6   10/18/01  p      2050  DENTAL Cons

7   10/17/01  a      2045  DENTAL Cons

Enter ?? for more actions

SP Select Patient   FR Forward          CT Complete/Update  RT Results Display

CV Change View ...  CX Cancel (Deny)    MA Make Addendum    PF Print Form 513

RC Receive          DC Discontinue      SF Sig Findings     RM Remove Med Rslt

SC Schedule         CM Add Comment      DD Detailed Display ER Edit/Resubmit

Select: Quit//

### IFC Requests by Remote Ordering Provider

If you need to determine the status of consults at your facility ordered from a certain provider at another facility, then you can use the IFC Requests by Remote Ordering Provider option.

When using this option, you must specify the name of the provider exactly at the prompt. If you enter a question mark, a screened list of ordering providers is displayed.

In this example we look at the Medicine consults from a provider at Boise:

Select IFC Management Menu Option: IR  IFC Requests by Remote Ordering Provider

Select Requesting site: BOISE

1   BOISE                 ID  VAMC      531

2   BOISE                 ID  RO        347

3   BOISE                 ID  M&amp;ROC     447

4   BOISE                 ID  CHEP      932

CHOOSE 1-4: 1  BOISE           ID  VAMC      531

Enter the ENTIRE name in proper CASE, exactly as it

appears in the list (including any credentials).

Use copy/paste to avoid typing errors.

NO partial matches are done.

Enter ? to display a list of possible entries.

Select Remote Ordering Provider: ?

CRPROVIDER,EIGHT

CRPROVIDER,FIVE

CRPROVIDER,FOUR

CRPROVIDER,NINE

CRPROVIDER,SEVEN

CRPROVIDER,SIX

CRPROVIDER,THREE

CRPROVIDER,TWO

CRPROVIDER,TEN

CRPROVIDER,ONE

Enter RETURN or '^' to exit: &lt;Enter&gt;

Enter the ENTIRE name in proper CASE, exactly as it

appears in the list (including any credentials).

Use copy/paste to avoid typing errors.

NO partial matches are done.

Enter ? to display a list of possible entries.

Select Remote Ordering Provider: CRPROVIDER,TWO

Only Display Consults With Status of: All Status's// &lt;Enter&gt;

Select Service/Specialty: MEDICINE

List From Starting Date: ALL DATES// &lt;Enter&gt;

...SORRY, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

Inter-facility Consults       Feb 21, 2002@09:16:26          Page:    1 of    2

IFC Requests: Consulting Site

Service: MEDICINE

From: ALL   To: FEB 21,2002

Status      Last Action      Request Date  Patient Name      Pt Location     .

IF Consult/Request By Status - Consulting Site

FROM: ALL   TO: FEB 21,2002

Routing Facility - BOISE

Remote Ordering Provider – CRPROVIDER,TWO

GROUPER: MEDICINE

GROUPER: CARDIOLOGY  in Group: MEDICINE

GROUPER: CARDIOLOGY Totals:

Total Requests To Grouper CARDIOLOGY:      0

SERVICE: EYE CLINIC in Group: MEDICINE

Pending    FWD TO REMOTE SERVI 01/07/02 CRPATIENT,S. (1990)          BOISE

Pending    REMOTE REQUEST RECE 12/21/01 CRPATIENT,F. (3333)        2B MED

+         Enter ?? for more actions                                          &gt;&gt;&gt;

Service                   Number on/off             Description of Data

Status                    Print List

Select Item(s): Next Screen// Select Item(s): Quit//

There are three other fields that are not visible on an 80 column screen such as the screen in the example. They are: Routing Facility, Days Diff, and Rec Date. They can be viewed by using the Shift to View Right action (&gt;). Using the Shift to View Left (&lt;) action restores the screen.

There are five actions you can do besides the default actions (like Next Screen, Previous Screen, Quit, &gt;, &lt;, …). These are change Service, Number on/off, Description of Data, Status, and Print List.

The change Service action allows you to re-display the report for a different service.

The Number on/off action changes the format of the report to include the consult number. To do this, it preserves the other columns but makes them narrower.

The Description of Data action gives a detailed description  for applicable data columns.

The Status action allows you to change which statuses are displayed in the report.

## Inter-Facility Consults Management Options

The Inter-Facility Consults Options [GMRC IFC MGMT] menu is part of the Consults Management [GMRC MGR] menu. This menu has the following options in it:

| Synonym   | Name                                       | Command                          |
|-----------|--------------------------------------------|----------------------------------|
| TI        | Test IFC implementation                    | [GMRC IFC TEST SETUP]            |
| LI        | List incomplete IFC transactions           | [GMRC IFC INC TRANS]             |
| IFC       | Inter-Facility Consult Requests            | [GMRC IFC RPT CONSULTS]          |
| TR        | IFC Transaction Report                     | [GMRC IFC TRANS]                 |
| LK        | Locate IFC by Remote Cslt #                | [GMRC IFC REMOTE NUMBER]         |
| BK        | Monitor IFC background job parameters      | [GMRC IFC BKG PARAM MON]         |
| AI        | Print All Incomplete IFC Transactions      | [GMRC IFC INC RPT]               |
| EP        | Edit IFC Processing Parameters             | [GMRC IFC PARAMETER EDIT]        |
| IP        | Inter-facility Consult Requests By Patient | [GMRC IFC RPT CONSULTS BY PT]    |
| IR        | IFC Requests by Remote Ordering Provider   | [GMRC IFC RPT CONSULTS BY REMPR] |
| MP        | Configure test account patients for IFC    | [GMRC IFC TEST PT MPI]           |
| PI        | Print Inter-facility Consult Requests      | [GMRC IFC PRINT RPT NUMBERED]    |

Inter-Facility Consult Requests (IFC), Inter-Facility Consult Requests by Patient (IP), Print Inter-Facility Consult Requests (PI), and  IFC Requests by Remote Ordering Provider (IR)  are covered under the Inter-Facility Consults Reports section above.

### Test IFC Implementation

The following example shows how to use the Test IFC Implementation option to check the setup of a procedure or consult service:

Select IFC Management Menu Option: TI  Test IFC implementation

Select one of the following:

P         procedure

C         consult service

Would you like to test a procedure or consult service: procedure

Select the GMRC Procedure that you'd like to test: EKG

1   EKG - BOISE

2   EKG  ELECTROCARDIOGRAM

CHOOSE 1-2: 1  EKG - BOISE

attempting to connect to remote system...

There is an implementation problem. The remote site indicated:

Multiple services matched to procedure

Would you like to test another implementation?

The following are the 7 most common errors that may be indicated with this option:

- 301 – Service not matched to receiving facility. You need to coordinate with the consulting facility. The consulting facility needs to use the Setup Service (SS) option to make sure your facility is correctly listed in the IFC SENDING FACILITY field.
- 401 – Procedure not matched to receiving facility. You need to coordinate with the consulting facility. The consulting facility needs to use the Setup Procedure (PR) option to make sure your facility is correctly listed in the IFC SENDING FACILITY field.
- 501 – Error in procedure name. Could not find a matching procedure at the consulting facility. You probably need to verify the spelling and use the Setup Procedure (PR) option to make sure the IFC REMOTE PROCEDURE NAME is correct in your Procedure file (#123.3).
- 601 – Multiple services matched to procedure. At the consulting facility, the RELATED SERVICES multiple must only contain a single value.
- 701 – Error in Service name. Could not find a matching service at the consulting facility. You probably need to verify the spelling and use the Setup Service (SS) option to make sure the IFC REMOTE NAME is correct in your Request Services (#123.5).
- 702 – Service is Disabled.  The Service has been disabled at the Consulting site.
- 703 – Procedure is Inactive.  The Procedure has been inactivated at the Consulting Site.

Note: 	Any error occurring within the VistA HL7 messaging system is also indicated in this option.

### Configure Test Account Patients

The Configure Test Account Patients for IFC option sets up a patient with a test account Integration Control Number (ICN) so that the patient may be used to test Inter-Facility Consults. An identical patient (with identical social security number) must be set up at both cooperating test sites. This option takes the social security number and appends a 9 to the beginning of it to produce a unique ICN. It then files this pseudo-ICN in the patient file for this patient. If the SSN for the patient is the same as another patient in the test account, the option will not proceed until this conflict is resolved.

This option must be exercised at both cooperating facilities before the patient may be used for Inter-facility Consults testing.

In this example, George F Babbitt is set up as a test patient:

Select IFC Management Menu Option: MP  Configure test account patients for IFC

Select shared patient: CRPATIENT,THIRTEEN        4-9-46    666668829     YES     SC VETERAN

Enrollment Priority: GROUP 3    Category: IN PROCESS    End Date:

Trying to set test patient ICN...

Done.

Select shared patient:

Note: 	This option will only function in test accounts.

### List incomplete IFC transactions

GMRC IFC INC TRANS is a tool for reviewing incomplete Inter-Facility Consult (IFC) Transactions. With this option you can retransmit an action that is not yet resolved.

This option can accept the following inputs when selecting a consult request:

- A Consult number.
- A Patient Name.
- A Service Name.
- A question mark to see a screened list of consults with incomplete activities.

The following screen capture error is inspected and a retransmit if performed:

Select IFC Management Menu Option: LI  List incomplete IFC transactions

Select a consult request: ?

Answer with REQUEST/CONSULTATION NUMBER, or FILE ENTRY DATE, or

PATIENT NAME, or TO SERVICE, or FROM, or DATE OF REQUEST, or

CPRS STATUS, or SENDING PROVIDER, or ASSOCIATED RESULTS

Do you want the entire REQUEST/CONSULTATION List? n  (No)

Type in the number, date of request or patient name.

Select a consult request: CRPATIENT,SEVEN          12-31-51    666781990       SC VETERAN

Incomplete IFC Transactions   Feb 07, 2002@12:10:05          Page:    1 of    1

Incomplete transaction(s) for consult#: 9907

.

An error occurred transmitting the following inter-facility consult

activity to BOISE:

Consult #: 9907

Remote Consult #:

Patient Name: CRPATIENT,SEVEN

To Service: DENTAL

Activity #: 1

Activity                 Date/Time/Zone      Responsible Person  Entered By

CPRS RELEASED ORDER     12/20/01 10:41      CRPROVIDER,THREE    CRPROVIDER,THREE

The error was: Error in Service name

Enter ?? for more actions

SC Select new Consult                   CM Mark transaction complete

RT Retransmit an IFC activity

Select action: Quit// RT   Retransmit an IFC activity

Select an activity number:  1

You have selected the following activity:

CPRS RELEASED ORDER entered Dec 20, 2001@10:41:08

Are you sure you want to retransmit this activity? Y  YES

Incomplete IFC Transactions   Feb 07, 2002@12:10:05          Page:    1 of    1

Incomplete transaction(s) for consult#: 9907

.

An error occurred transmitting the following inter-facility consult

activity to BOISE:

Consult #: 9907

Remote Consult #:

Patient Name: CRPATIENT,SEVEN

To Service: DENTAL

Activity #: 1

Activity                 Date/Time/Zone      Responsible Person  Entered By

CPRS RELEASED ORDER     12/20/01 10:41      CRPROVIDER,THREE    CRPROVIDER,THREE

The error was: Error in Service name

Enter ?? for more actions

SC Select new Consult                   CM Mark transaction complete

RT Retransmit an IFC activity

Select action: Quit//

The Re-transmit an IFC Activity action may be used when the listed error has been corrected and the activity should be transmitted to the remote facility again. This action is optional as the IFC Background job will resend any activities with corrected errors.

The Mark Transaction Complete action must be used with caution. This action is *only* used when each site can verify that the activity was transmitted and the consult record was appropriately updated.  This action will remove the activity from the listing in this option and suppress any future alerts about the error.

### Print All Incomplete IFC Transactions

Incomplete IFC transactions may be compiled as a printed report. This gives similar information as the List Incomplete IFC Transactions option discussed above, but does not require the selection of a specific consult number. This report also does not afford the opportunity to correct or re-transmit the consult(s). The main advantage of this option is that is gives you a hard-copy of the incomplete IFC transactions.

In this example this incomplete IFC Transactions Report is displayed on the computer screen:

Select IFC Management Menu Option: AI  Print All Incomplete IFC Transactions

DEVICE:   ANYWHERE &lt;Enter&gt;   Right Margin: 80// &lt;Enter&gt;

Incomplete IFC Transaction Report              OCT  1,2002  08:40    PAGE 1

--------------------------------------------------------------------------------

INCOMPLETE: YES

CONSULT/REQUEST #:    10059

DATE/TIME OF ENTRY: OCT 01, 2002@08:40:15

FACILITY: BOISE                       MESSAGE #: 660124336

CONSULT/REQUEST #: 10059              ACTIVITY #: 1

INCOMPLETE: YES                       TRANS. ATTEMPTS: 1

ERROR: Service not matched to receiving facility

Select IFC Management Menu Option:

### IFC Transaction Report

This option lists the current contents of the IFC Message Log (#123.6) file for one or all consults. This log is used by the Inter-Facility Consults software to insure transmission of Inter-Facility Consult requests. The IFC background job checks this log and takes appropriate action on requests that have not yet successfully completed.

Completed transactions are deleted by the software after a period of time. You can control this function by using the Edit IFC Processing Parameters [GMRC IFC PARAMETER EDIT] option, set the GMRC RETAIN IFC ACTIVITY DAYS (Days to retain IFC transactions) parameter to a number between 7 and 180. If this parameter is not set, completed transactions will be retained for 7 days. The higher the number set in this parameter the more disk space will be used by the IFC MESSAGE LOG file.

See the section on Error Handling below for more complete details.

At the “Select Consult/Request Number:” prompt, you may enter any one of the following:

- ALL to list all entries.
- The consult number to list that single consult.
- The patient name to select a consult from the consults on file for that patient.
- The to or from service to select a consult from the consults to or from that service.
- The date of request to select a consult originated on that date.
- The CPRS status, such as PENDING or PARTIAL RESULTS, to select a consult with that status.
- The sending provider to select a consult originated by that provider.

In the following example, we list all entries in the IFC Transaction Log:

Select IFC Management Menu Option: ?

<!-- image -->

TI     Test IFC implementation

LI     List incomplete IFC transactions

IFC    IFC Requests

TR     IFC Transaction Report

LK     Locate IFC by Remote Cslt #

BK     Monitor IFC background job parameters

AI     Print All Incomplete IFC Transactions

EP     Edit IFC Processing Parameters

IP     IFC Requests By Patient

IR     IFC Requests by Remote Ordering Provider

MP     Configure test account patients for IFC

PI     Print IFC Requests

Select IFC Management Menu Option: TR  IFC Transaction Report

NOTE: Successful transactions are deleted after one week.

Select Consult/Request Number: ALL// ?

Answer with REQUEST/CONSULTATION NUMBER, or FILE ENTRY DATE, or

PATIENT NAME, or TO SERVICE, or FROM, or DATE OF REQUEST, or

CPRS STATUS, or SENDING PROVIDER, or ASSOCIATED RESULTS

Do you want the entire 2033-Entry REQUEST/CONSULTATION List?

Select Consult/Request Number: ALL// &lt;Enter&gt;

List From Starting Date: ALL DATES// &lt;Enter&gt;

View by (C)onsult, (D)ate, (A)ctivity, or (M)essage Status: Consult// &lt;Enter&gt;

IFC Transactions              Jan 31, 2002@07:56:59          Page:    1 of    3

Transaction(s) for consult#: ALL

Consult     Entry Date/Time    Activity               Error                  .

2206         11/21/01 15:47     CPRS RELEASED ORDER    Local or unknown MPI ide

2219         11/26/01 16:06     CPRS RELEASED ORDER    Service not matched to r

2229         11/29/01 09:35     CPRS RELEASED ORDER    Service not matched to r

9907         12/20/01 10:41     CPRS RELEASED ORDER    Service not matched to r

9919         01/29/02 12:12     SIG FINDING UPDATE     Error in Service name

9919         01/29/02 12:15     SIG FINDING UPDATE     Unknown Patient

9921         01/09/02 09:53     FORWARDED FROM         Local or unknown MPI ide

9937         01/17/02 12:34     CANCELLED              Unknown Patient

9937         01/17/02 14:30     CANCELLED              Local or unknown MPI ide

9937         01/17/02 14:54     CANCELLED              Local or unknown MPI ide

9937         01/17/02 15:09     CANCELLED              Local or unknown MPI ide

9937         01/17/02 15:45     CANCELLED              Local or unknown MPI ide

9937         01/17/02 16:05     CANCELLED              Local or unknown MPI ide

9940         01/23/02 16:01     COMPLETE/UPDATE        No Error

9940         01/23/02 16:07     INCOMPLETE RPT         Service not matched to r

9940         01/23/02 16:24     DISASSOCIATE RESULT    Unknown Patient

9940         01/23/02 16:25     DISASSOCIATE RESULT    Local or unknown MPI ide

+         Enter ?? for more actions                                          &gt;&gt;&gt;

SC Select new Consult     DD Detailed Display

PL Print List             CV Change View

Select action:Next Screen// DD

Select a Consult number from the display:  (1-9999999): 2206

IFC Transactions              Mar 14, 2002@16:38:17          Page:    1 of    1.

Detailed Display

Consult#: 2206

.

ENTRY DATE/TIME: NOV 21, 2001@15:47:53

FACILITY: BOISE

MESSAGE #: 66036920

ACTIVITY #: 1

INCOMPLETE: YES

TRANS. ATTEMPTS: 1

ERROR: Service not matched to receiving facility

Enter ?? for more actions                                          &gt;&gt;&gt;

SC Select new Consult     DD Detailed Display

PL Print List             CV Change View

Select action:Quit//

### Locate IFC by Remote Consult Number

This option is designed to assist consulting facilities with consult inquiries from requesting facilities; e.g., “Do you have the consult with Boise number 845?” All other reports are based on the local consult number. When a call is made from a requesting facility for information on the status of a consult, they are not likely to have the consulting facility’s number—only their own number for that consult. This option gets around that problem by keying on the original consult number.

In this example, a CAC at XXX assists a Physician at Boise in looking up Boise consult number 845:

Select IFC Management Menu Option: ?

<!-- image -->

TI     Test IFC implementation

LI     List incomplete IFC transactions

IFC    IFC Requests

TR     IFC Transaction Report

LK     Locate IFC by Remote Cslt #

BK     Monitor IFC background job parameters

AI     Print All Incomplete IFC Transactions

EP     Edit IFC Processing Parameters

IP     IFC Requests By Patient

IR     IFC Requests by Remote Ordering Provider

MP     Configure test account patients for IFC

PI     Print IFC Requests

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select IFC Management Menu Option: LK  Locate IFC by Remote Cslt #

Choose the facility to which the remote entry belongs: ?

Answer with INSTITUTION NAME, or STATUS, or STATION NUMBER, or

OFFICIAL VA NAME, or CURRENT LOCATION, or NAME (CHANGED FROM)

Do you want the entire INSTITUTION List? N  (No)

Choose the facility to which the remote entry belongs: BOISE

1   BOISE                 ID  VAMC      531

2   BOISE                 ID  RO        347

3   BOISE                 ID  M&amp;ROC     447

4   BOISE                 ID  CHEP      932

CHOOSE 1-4: 1  BOISE           ID  VAMC      531

Select the Remote Consult Entry #:  (1-9999999): 845

Select one of the following:

B         brief

D         detailed

Display type: B// &lt;Enter&gt; detailed

Consult Detailed Display      Jan 31, 2002@08:20:11          Page:    1 of    5

TEST,BOB   333-44-7111                                          DEC 9,1950 (51)

Consult No.: 9943                                             Wt.(lb): No Entry

.

Current Pat. Status:   Outpatient

Order Information

To Service:            PLASTIC SURGERY

From Service:

Requesting Provider:

Service is to be rendered on an OUTPATIENT basis

Place:                 Consultant's choice

Urgency:               Routine

Orderable Item:

Consult:               Consult Request

Reason For Request:

Can surgery correct this patients aging process??

Inter-facility Information

+         Enter ?? for more actions

Select Action:Next Screen//

### Edit IFC Processing Parameters

<!-- image -->

- Days to retain complete IFC transactions (GMRC RETAIN IFC ACTIVITY DAYS)
- Alert CLIN group immediately on patient error (GMRC IFC ALERT IMMED ON PT ERR)
- Skip IFC re-transmissions on weekends (GMRC IFC SKIP WEEKEND RE-TRANS)

These are different from the IFC background job parameters which are discussed in the Monitor IFC Background Job Parameters section.

In the following example we use this option to check the settings of these parameters:

Select IFC Management Menu Option: EP  Edit IFC Processing Parameters

Configure IFC parameters for System: DEVCUR.FO-SLC.MED.VA.GOV

------------------------------------------------------------------------------

Days to retain complete IFC transactions          14

Alert CLIN group immed. on pt. err                YES

Skip IFC re-transmissions on weekends             YES

------------------------------------------------------------------------------

Retention days: 14// &lt;Enter&gt;

Alert CLIN group: YES// &lt;Enter&gt;

Skip weekends: YES// &lt;Enter&gt;

Select IFC Management Menu Option:

### Monitor IFC Background Job Parameters

This option lists the current state of parameters concerning the IFC background jobs. It also gives an alternate method of changing these parameters. For example, if the running of the IFC Background job should be delayed for any reason (e.g. to install a GMRC patch or system maintenance), it may be delayed by using the Edit background job start parameter action and setting the start time parameter to a date/time in the future.

In this example, we view the IFC background job parameters:

Select IFC Management Menu Option: BK  Monitor IFC background job parameters

RL Refresh background parameter list                                           .

IFC Background Parameters     Mar 14, 2002@16:27:11          Page:    1 of    1

Inter-facility Consults background job parameter display

.

The IFC background job last started:     Mar 14, 2002@15:48:57

The IFC background job last finished:    Mar 14, 2002@15:48:57

The IFC background job is on schedule or is

running.

It may be delayed by editing the start time

to a future date/time using the Edit start

time action.

Enter ?? for more actions

ES Edit background job start parameter

RL Refresh background parameter list

Select action:Quit//

Note:	The Edit Parameter Values [XPAR EDIT PARAMETER] option should not be used to edit the start or finish parameters for the IFC Background job.

### Background Task

The IFC background job is an important factor for successful implementation of Inter-facility Consults. It is automatically activated by any outgoing IFC activity, and performs the following:

- Monitors entries in the IFC MESSAGE LOG file (#123.6).
- Deletes completed entries from the IFC MESSAGE LOG file (#123.6).
- Re-transmits some entries from the IFC MESSAGE LOG file (#123.6) with errors.
- Sends notifications/mail messages to members of IFC mail groups.
- Schedules itself to run one hour after it finished last.

In addition, the IFC Background Startup option [GMRC IFC BACKGROUND STARTUP] should be scheduled as follows:

- Upon system startup
- Whenever TaskMan unexpectedly stops
- Every 8 hours

Note: 	Following installation, you should use the Schedule/Unschedule Options [XUTM SCHEDULE] option to schedule GMRC IFC BACKGROUND STARTUP to run every eight hours. Proper inter-facility consult messaging is dependent on this.

This task also starts the background job; the only difference is that this task schedules it at regular intervals.

Note the following system schedule:

Edit Option Schedule

Option Name: GMRC IFC BACKGROUND STARTUP

Menu Text: IFC Background Startup                    TASK ID:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: JAN 24,2002@12:50

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET: CUR

RESCHEDULING FREQUENCY: 8H

TASK PARAMETERS:

SPECIAL QUEUEING: Startup Persistent

Notes on the management of the Background Job:

- No Data integrity issues occur if the task or background job stops unexpectedly.
- In rare cases, it is possible to get duplicate IFC mail messages as a result of the background job. The duplicates should be ignored.
- Be sure that 8H is included in the rescheduling frequency when scheduling the task.
- There are checks built into the background job which prevent it from being run more than once an hour even though multiple events may attempt to trigger it.
- If TaskMan stops running, the task should automatically re-queue for a future date/time.
- The next outgoing IFC activity will also activate the background job.
- Placing TaskMan in a wait state should have no effect on the task.

The Background Job can be prevented from re-transmitting requests with Unknown Patient errors (201) or Local or Unknown MPI Identifiers errors (202) to the consulting facility on Saturday or Sunday. This is done using the Edit IFC Processing Parameters [GMRC IFC PARAMETER EDIT] option and setting the Skip IFC re-transmissions on weekends (GMRC IFC SKIP WEEKEND RE-TRANS) parameter to YES.

## Error Handling

In general, Inter-Facility Consults uses the Kernel alert system to notify key people of errors occurring in the system. Errors typically take the form of HL7 messages that cannot be properly delivered or processed.

In the case of inability to deliver a message, the system will retry automatically about one hour after the last attempt. In many of these cases, the error will resolve itself.

If the cause is missing file information, personnel assumed to have responsibility for that information are notified. The error may be in consult or procedure files, but it also may be in the patient file (i.e., the patient not identifiable at both sites). Once the file entries have been corrected, the system automatic retry will detect the new information and resolve the error.

### Inter-Facility Consult Errors

Key:

Requesting site: Facility at which the original consult request was made.

Consulting site: Facility tasked with fulfilling the consult request.

Originating site: Facility at which the current action occurred.

Note: 	Some of the Follow-up actions listed below require the use of FileMan. Others can be accomplished with the Consults actions such as Setup Services (SS) and Setup Procedures (PR). Once corrections are made, the activity can be retransmitted using the RETRANSMIT AN IFC ACTIVITY action of the List Incomplete IFC Transactions [GMRC IFC INC TRANS] option.

#### Error 101—Unknown Consult/Procedure request

| Cause                                        | Actions Taken                                                        | Follow-up                                                                                                                                                  |
|----------------------------------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unknown Consult or Procedure request number. | Originating Site: Notification sent to mail groups: IFC TECH ERRORS. | Originating Site: Correct the REMOTE CONSULT FILE ENTRY in the Request/ Consultation file (#123) & retransmit the activity in the IFC Message Log (#123.6) |

##### Example of Notification/Mail Message

Notification: Failed IFC transaction

Upon notification processing:

An error occurred transmitting the following inter-facility consult activity to &lt;site name&gt;:

Consult #: &lt;consult #&gt;

Patient Name: &lt;patient name&gt;

SSN: &lt;social security number&gt;

To Service: &lt;to service&gt;

(Procedure: &lt;procedure&gt;)

Activity  Date/Time/Zone Responsible Person  Entered By

&lt;data&gt;

The error was: Unknown Consult/Procedure request

#### Error 201—Unknown Patient

| Cause                                                                                                                                                                                                  | Actions Taken                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Follow-up                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unknown Patient.  Patient has either never been registered at the Consulting facility or the Master Patient Index (MPI) Integration Control Number (ICN) does not match that from the requesting site. | Consulting site: E-mail message sent to mail group: IFC PATIENT ERROR MESSAGES at the consulting facility. This message is renewed every hour and is continued until the error is corrected. IFC CLIN ERRORS receives mail message every 24 hours until the error is resolved.  Requesting site:  IFC CLIN ERRORS is notified. This occurs either immediately (if GMRC IFC ALERT IMMED ON PT ERR parameter is set to YES) or every 24 hours until the error is resolved. | In patch GMRC*3.0*154 code was added to check the correlation list (from the TREATING FACILITY LIST file #391.91) and, if the patient does not exist at the receiving site, a “proxy add” is executed to create (register) the patient at the receiving site. This should eliminate all manual registration of patients as described above. |

<!-- image -->

* If patient has a locally assigned ICN, use the Single Patient Initialization to MPI [MPIF IND MPI LOAD] to match record with the Requesting site's national ICN.  If patient has a national MPI ICN which does not match, use the Inactivate Patient from MPI [MPIF PAT INACT] and then the Single Patient Initialization to MPI [MPIF IND MPI LOAD] to match record with the Requesting site's national ICN.  If unable to inactivate patient from the MPI or if further information is required, refer to the Master Patient Index/Patient Demographics (MPI/PD) User and Master Patient Index/Patient Demographics Exception Handling Manuals for detailed instructions.

##### Example of Notification/Mail Message

Consulting site:

Subj: Incoming IFC patient error, &lt;patient name&gt;  [#47056] 31 Oct 01 13:08

From: CONSULT/REQUEST TRACKING PACKAGE  In 'IN' basket. Page 1  *New*

<!-- image -->

An Inter-facility Consult for the following patient has been requested.  
The patient has either never been registered at your facility or the national 
MPI ICN for this patient at your site does not match that from the requesting 
site.  Please refer to the Master Patient Index/Patient Demographics (MPI/PD) 
User Manual and Master Patient Index/Patient Demographics Exception 
Handling Manuals to resolve this error so request may be processed.

Patient demographics from &lt;site name&gt;

Patient name: &lt;patient name&gt;

SSN: &lt;patient ssn&gt;

Date of birth: &lt;patient dob&gt;

Sex: &lt;patient sex&gt;

Remote ICN: &lt;remote integration control number&gt;

Ordered Service:  FOOT CLINIC

The error is: Unknown Patient (201)

Requesting site:

Notification: Failed IFC transaction

Upon notification processing:

An error occurred transmitting the following inter-facility consult activity to &lt;site name&gt;:

Consult #: &lt;consult #&gt;

Patient Name: &lt;patient name&gt;

SSN: &lt;social security number&gt;

To Service: &lt;to service&gt;

(Procedure: &lt;procedure&gt;)

Activity  Date/Time/Zone Responsible Person  Entered By

&lt;data&gt;

The error was: Unknown patient (201)

#### Error 202—Local or Unknown MPI Identifiers

| Cause                                                                                                  | Actions Taken                                                                                                                                                                                                                                                                                                               | Follow-up   |
|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Patient is missing an Integration Control number (MPI number) or the ICN is a locally assigned number. | Requesting site: A mail message is sent to the IFC PATIENT ERROR MESSAGES mail group. Message is renewed every 3 hours. Also, an entry is inserted in the message log with this error attached. As long as the error is still unresolved, the IFC CLIN ERRORS group is alerted to the problem approximately every 24 hours. |             |

<!-- image -->

##### Example of Notification/Mail Message

Subj: Outgoing IFC patient error, &lt;patient name&gt;  [#47439] 26 Nov 01 11:22

From: CONSULT/REQUEST TRACKING PACKAGE.   Page 1    *New*

<!-- image -->

An Inter-facility Consult for the following patient has been requested. 
The PATIENT file is either missing an ICN or contains a local ICN.  
Please refer to the Master Patient Index/Patient Demographics(MPI/PD) User 
and Master Patient Index/Patient Demographics Exception Handling Manuals 
to resolve this error so request may be processed.

Patient name: &lt;patient name&gt;

SSN:  &lt;patient ssn&gt;

Date of birth:  &lt;patient dob&gt;

Sex:  &lt;patient sex&gt;

The error is: Local or unknown MPI identifiers (202)

#### Error 301—Service not Matched to Receiving Facility

| Cause                                                                             | Actions Taken                                                      | Follow-up                                                                                                                                                                                                 |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Sending facility not registered at consulting facility for the requested Service. | Requesting site: Notification sent to mail group: IFC CLIN ERRORS. | Consulting site: Correct the IFC SENDING FACILITY in the Request Services file (#123.5) using the Setup Consult Services [GMRC SETUP REQUEST SERVICES] option on the Consults Management Menu [GMRC MGR]. |

##### Example of Notification/Mail Message

Notification: Failed IFC transaction

Upon notification processing:

An error occurred transmitting the following inter-facility consult activity to &lt;site name&gt;:

Consult #: &lt;consult #&gt;

Patient Name: &lt;patient name&gt;

SSN: &lt;social security number&gt;

To Service: &lt;to service&gt;

(Procedure: &lt;procedure&gt;)

Activity  Date/Time/Zone Responsible Person  Entered By

&lt;data&gt;

The error was: Service not matched to receiving facility

#### Error 401—Procedure not Matched to Receiving Facility

| Cause                                                                               | Actions Taken                                                      | Follow-up                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------|--------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Sending facility not registered at consulting facility for the requested Procedure. | Requesting site: Notification sent to mail group: IFC CLIN ERRORS. | Consulting site: Correct the IFC SENDING FACILITY in the GMRC Procedure file (#123.3) using the Setup Procedure [GMRC PROCEDURE SETUP] option on the Consults Management Menu [GMRC MGR]. |

##### Example of Notification/Mail Message

Notification: Failed IFC transaction

Upon notification processing:

An error occurred transmitting the following inter-facility consult activity to &lt;site name&gt;:

Consult #: &lt;consult #&gt;

Patient Name: &lt;patient name&gt;

SSN: &lt;social security number&gt;

To Service: &lt;to service&gt;

(Procedure: &lt;procedure&gt;)

Activity  Date/Time/Zone Responsible

Person  Entered By &lt;data&gt;

The error was: Procedure not matched to receiving facility

#### Error 501—Error in Procedure Name

| Cause                                                                          | Actions Taken                                                      | Follow-up                                                                     |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------|-------------------------------------------------------------------------------|
| Error in the Procedure name (Procedure name not found at consulting facility). | Requesting site: Notification sent to mail group: IFC CLIN ERRORS. | Requesting site: Correct the IFC REMOTE PROC NAME in the GMRC PROCEDURE file. |

##### Example of Notification/Mail Message

Notification: Failed IFC transaction

Upon notification processing:

An error occurred transmitting the following inter-facility consult activity to &lt;site name&gt;:

Consult #: &lt;consult #&gt;

Patient Name: &lt;patient name&gt;

SSN: &lt;social security number&gt;

To Service: &lt;to service&gt;

(Procedure: &lt;procedure&gt;)

Activity  Date/Time/Zone Responsible Person  Entered By

&lt;data&gt;

The error was: Error in procedure name

#### Error 601—Multiple Services Matched to Procedure

| Cause                                      | Actions Taken                                                      | Follow-up                                                                                                                                                                                                                                                                                                       |
|--------------------------------------------|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Multiple services attached to a Procedure. | Requesting site: Notification sent to mail group: IFC CLIN ERRORS. | Consulting site: Correct the RELATED SERVICES multiple in the GMRC Procedure file (123.3) using the Setup Procedure [GMRC PROCEDURE SETUP] option of the Consults Management Menu [GMRC MGR]. For Inter-Facility Consults to work correctly, there must be only one related service at the Consulting Facility. |

##### Example of Notification/Mail Message

Notification: Failed IFC transaction

Upon notification processing:

An error occurred transmitting the following inter-facility consult activity to &lt;site name&gt;:

Consult #: &lt;consult #&gt;

Patient Name: &lt;patient name&gt;

SSN: &lt;social security number&gt;

To Service: &lt;to service&gt;

(Procedure: &lt;procedure&gt;)

Activity  Date/Time/Zone Responsible Person  Entered By

&lt;data&gt;

The error was: Multiple services matched to procedure

#### Error 701—Error in Service Name

| Cause                                                                  | Actions Taken                                                      | Follow-up                                                                  |
|------------------------------------------------------------------------|--------------------------------------------------------------------|----------------------------------------------------------------------------|
| Error in service name (Service name not found at consulting facility). | Requesting site: Notification sent to mail group: IFC CLIN ERRORS. | Requesting site: Correct the IFC REMOTE NAME in the REQUEST SERVICES file. |

##### Example of Notification/Mail Message

Notification: Failed IFC transaction

Upon notification processing:

An error occurred transmitting the following inter-facility consult activity to &lt;site name&gt;:

Consult #: &lt;consult #&gt;

Patient Name: &lt;patient name&gt;

SSN: &lt;social security number&gt;

To Service: &lt;to service&gt;

(Procedure: &lt;procedure&gt;)

Activity  Date/Time/Zone Responsible Person  Entered By &lt;data&gt;

The error was: Error in service name

#### Error 702— Service is Disabled Error! Bookmark not defined.

| Cause                                         | Actions Taken                                                        | Follow-up                                                                                                                                                                                                           |
|-----------------------------------------------|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Service has been disabled at Consulting Site. | Requesting site:  Notification sent to mail group:  IFC CLIN ERRORS. | Requesting site: Verify the correct consult was ordered, or work with the Consulting site to enable the consult service.  The consult will remain “pending” at the requesting site until the order is discontinued. |

##### Example of Notification/Mail Message

Notification: Failed IFC transaction

Upon notification processing:

An error occurred transmitting the following inter-facility consult activity to &lt;site name&gt;:

Consult #: &lt;consult #&gt;

Remote Consult #: &lt;remote consult #&gt;

Patient Name: &lt;patient name&gt;

SSN: &lt;social security number&gt;

To Service: &lt;to service&gt;

Activity  Date/Time/Zone Responsible Person  Entered By

&lt;data&gt;

The error was: Service is Disabled

#### Error 703— Procedure is Inactive

| Cause                                              | Actions Taken                                                        | Follow-up                                                                                                                                                                                                                   |
|----------------------------------------------------|----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Procedure has been inactivated at Consulting Site. | Requesting site:  Notification sent to mail group:  IFC CLIN ERRORS. | Requesting site: Verify the correct procedure was ordered, or work with the Consulting site to activate the procedure.  The consult procedure will remain “pending” at the requesting site until the order is discontinued. |

##### Example of Notification/Mail Message

Notification: Failed IFC transaction

Upon notification processing:

An error occurred transmitting the following inter-facility consult activity to &lt;site name&gt;:

Consult #: &lt;consult #&gt;

Remote Consult #: &lt;remote consult #&gt;

Patient Name: &lt;patient name&gt;

SSN: &lt;social security number&gt;

Procedure: &lt;procedure name&gt;

Activity  Date/Time/Zone Responsible Person  Entered By

&lt;data&gt;

The error was: Procedure is Inactive

#### Error 801—Inappropriate Action for Specified Request

| Cause                                                                             | Actions Taken                                    | Follow-up                                                                                                |
|-----------------------------------------------------------------------------------|--------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Consult records at the two facilities may be out of synch with regards to status. | Requesting site: Alerts sent to tech mail group. | Requesting Site: Contact IRM support at consulting site and compare records to insure they are in synch. |

##### Example of Notification/Mail Message

Notification: Failed IFC transaction

Upon notification processing:

An error occurred transmitting the following inter-facility consult activity to &lt;site name&gt;:

Consult #: &lt;consult #&gt;

Patient Name: &lt;patient name&gt;

SSN: &lt;social security number&gt;

To Service: &lt;to service&gt;

(Procedure: &lt;procedure&gt;)

Activity  Date/Time/Zone Responsible Person  Entered By &lt;data&gt;

The error was: Inappropriate action for specified request

#### Error 802 - Duplicate, activity not filed

| Cause                                                                                                                          | Actions Taken   | Follow-up   |
|--------------------------------------------------------------------------------------------------------------------------------|-----------------|-------------|
| The activity or the consult request in question has been transmitted to the remote site multiple times and is already on file. | None            | None.       |

##### Example of Notification/Mail Message

None.

#### Error 901—Unable to Update Record Successfully

| Cause                                                                                                               | Actions Taken                                                                 | Follow-up   |
|---------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------|
| Unable to update the record at the consulting facility. The record at the consulting facility is in use and locked. | Requesting site: HL7 message automatically resent every hour until satisfied. | None.       |

##### Example of Notification/Mail Message

None.

#### Error 902—Earlier Pending Transactions

| Cause                                                                                                                                                                                                                                                                                                    | Actions Taken                                                                                       | Follow-up                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| Occurs when an earlier IFC activity wasn't transmitted successfully to the remote facility.  This assures that a later activity doesn't get transmitted before the earlier one is complete and will keep the requesting and consulting facilities in synch. This will not send alerts nor mail messages. | Requesting Site: Verify pending earlier actions.  Actions will automatically retransmit every hour. | Requesting site: Correct previous error actions for consult. |

##### Example of Notification/Mail Message

None.

#### Error 903—HL Logical Link not Found

| Cause                                                                                                           | Actions Taken                                                                      | Follow-up                                                                                         |
|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| Unable to find HL Link to the remote facility. A notification will be sent to the mail group “IFC TECH ERRORS.” | Originating Site: Verify the consult service has the correct IFC ROUTING FACILITY. | Originating site: Contact IRM to see if there is an HL LOGICAL LINK for the IFC ROUTING FACILITY. |

##### Example of Notification/Mail Message

Notification: Failed IFC transaction

Upon notification processing:

An error occurred transmitting the following inter-facility consult activity to &lt;site name&gt;:

Consult #: &lt;consult #&gt;

Patient Name: &lt;patient name&gt;

SSN: &lt;social security number&gt;

To Service: &lt;to service&gt;

(Procedure: &lt;procedure&gt;)

Activity  Date/Time/Zone Responsible Person  Entered By &lt;data&gt;

The error was: HL Logical Link not found

#### Error 904—VistA HL7 Unable to Send Transaction

| Cause                          | Actions Taken                  | Follow-up                                                                                     |
|--------------------------------|--------------------------------|-----------------------------------------------------------------------------------------------|
| Unable to transmit HL7 message | Originating Site: Contact IRM. | Originating site: Assure that Vista HL7 is functioning properly and is not in an error state. |

#### Error None

| Cause                                  | Actions Taken                                                       | Follow-up                                                                                                                                                                               |
|----------------------------------------|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Incomplete transmission and no errors. | Originating site: Notification sent  to mail group IFC TECH ERRORS. | Originating site: Review the local error log and if necessary, contact the remote facility to determine if an error occurred and determine whether activity needs to be re-transmitted. |

##### Example of Notification/Mail Message

Notification: Failed IFC transaction

Upon notification processing:

An error occurred transmitting the following inter-facility consult activity to &lt;site name&gt;:

Consult #: &lt;consult #&gt;

Patient Name: &lt;patient name&gt;

To Service: &lt;to service&gt;

(Procedure: &lt;procedure&gt;)

Activity  Date/Time/Zone Responsible Person  Entered By

&lt;data&gt;

The error was: Technical error

## Error Handling - Cerner to VistA

The installation of GMRC*3.0*154 modifies the error handling process to accommodate the issue of Cerner not supporting application negative acknowledgements (NAKs) generated from VistA.  When the requesting facility has been “converted” to Cerner and the consulting facility is a traditional VistA instance, application negative acknowledgements (NAK) are processed at the consulting facility. The consulting facility will initiate MailMan to notify members of several mail groups of the error.  Errors generated at the consulting facility will need manual intervention to resolve.

Key:

Requesting site: Facility at which the original consult request was made.

Consulting site: Facility tasked with fulfilling the consult request.

Originating site: Facility at which the current action occurred.

Note:	Some of the Follow-up actions listed below require the use of FileMan. Others can be accomplished with the Consults actions such as Setup Services (SS) and Setup Procedures (PR). Once corrections are made, the activity can be retransmitted using the Cerner Millennium Platform.

### Error 101—Unknown Consult/Procedure request

| Cause                                        | Actions Taken                                                            | Follow-up                                                        |
|----------------------------------------------|--------------------------------------------------------------------------|------------------------------------------------------------------|
| Unknown Consult or Procedure request number. | Consulting Site: Notification sent to mail groups: GMRC CRNR IFC ERRORS. | Originating Site: Correct the Configuration of Consult/Procedure |

### Error 201—Unknown Patient

| Cause                                                                                                                                                                                                  | Actions Taken                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Follow-up                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Unknown Patient.  Patient has either never been registered at the Consulting facility or the Master Patient Index (MPI) Integration Control Number (ICN) does not match that from the requesting site. | Consulting site: E-mail message sent to mail group: IFC PATIENT ERROR MESSAGES at the consulting facility. This message is renewed every hour and is continued until the error is corrected. IFC CLIN ERRORS receives mail message every 24 hours until the error is resolved.  Requesting site:  IFC CLIN ERRORS is notified. This occurs either immediately (if GMRC IFC ALERT IMMED ON PT ERR parameter is set to YES) or every 24 hours until the error is resolved. | Consulting site: Register patient.  If the patient being registered is a new patient at your site, a query is sent to the Master Patient Index.  If the MPI finds an exact match, that MPI ICN will be assigned. If the MPI finds potential matches, a local ICN is assigned and an exception is logged for human resolution using the MPI/PD Exception Handling [RG Exception Handling] option.*  In patch GMRC*3.0*154 code was added to check the correlation list (from the TREATING FACILITY LIST file #391.91) and, if the patient does not exist at the receiving site, a “proxy add” is executed to create (register) the patient at the receiving site. This should eliminate all manual registration of patients as described above. |

Note:

- Error Code 201 generated by an consult placed in Cerner will not initiate the Proxy add API to register the patient.  The patient will have to be manually registered in VistA.  The negative acknowledgement produced by VistA is intercepted and held by VDIF.  VDIF will requeue the new consult order and resend that order to VistA every three hours until it receives a successful response from VistA.
- Error Code 201 from a consult placed in VistA will not be generated by Cerner because Cerner doesn’t support application acknowledgements.  The Proxy add API is initiated to automatically register the patient in Cerner. Once the patient is registered, the 201 error code is logged in the IFC Message Log(#123.6) for the IFC background job to read the error message and resend the consult.

### Error 202—Local or Unknown MPI Identifiers

| Cause                                                                                                  | Actions Taken                                                                                                                                                                                                                                                                                                               | Follow-up   |
|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Patient is missing an Integration Control number (MPI number) or the ICN is a locally assigned number. | Requesting site: A mail message is sent to the IFC PATIENT ERROR MESSAGES mail group. Message is renewed every 3 hours. Also, an entry is inserted in the message log with this error attached. As long as the error is still unresolved, the IFC CLIN ERRORS group is alerted to the problem approximately every 24 hours. |             |

<!-- image -->

### Error 301—Service not Matched to Receiving Facility

| Cause                                                                             | Actions Taken                                                                                                                    | Follow-up                                                                                                                                                                                                 |
|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Sending facility not registered at consulting facility for the requested Service. | Consulting site: Notification sent to mail group: GMRC CRNR IFC ERRORS, GMRC CRNR IFC CLIN ERRORS, GMRC TIER II CRNR IFC ERRORS. | Consulting site: Correct the IFC SENDING FACILITY in the Request Services file (#123.5) using the Setup Consult Services [GMRC SETUP REQUEST SERVICES] option on the Consults Management Menu [GMRC MGR]. |

### Error 401—Procedure not Matched to Receiving Facility

| Cause                                                                               | Actions Taken                                                                                                                    | Follow-up                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Sending facility not registered at consulting facility for the requested Procedure. | Consulting site: Notification sent to mail group: GMRC CRNR IFC ERRORS, GMRC CRNR IFC CLIN ERRORS, GMRC TIER II CRNR IFC ERRORS. | Consulting site: Correct the IFC SENDING FACILITY in the GMRC Procedure file (#123.3) using the Setup Procedure [GMRC PROCEDURE SETUP] option on the Consults Management Menu [GMRC MGR]. |

### Error 501—Error in Procedure Name

| Cause                                                                          | Actions Taken                                                                                                                    | Follow-up                                                |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| Error in the Procedure name (Procedure name not found at consulting facility). | Consulting site: Notification sent to mail group: GMRC CRNR IFC ERRORS, GMRC CRNR IFC CLIN ERRORS, GMRC TIER II CRNR IFC ERRORS. | Requesting site: Correct the Configuration of Procedure. |

### Error 601—Multiple Services Matched to Procedure

| Cause                                      | Actions Taken                                                                                                                    | Follow-up                                                                                                                                                                                                                                                                                                       |
|--------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Multiple services attached to a Procedure. | Consulting site: Notification sent to mail group: GMRC CRNR IFC ERRORS, GMRC CRNR IFC CLIN ERRORS, GMRC TIER II CRNR IFC ERRORS. | Consulting site: Correct the RELATED SERVICES multiple in the GMRC Procedure file (123.3) using the Setup Procedure [GMRC PROCEDURE SETUP] option of the Consults Management Menu [GMRC MGR]. For Inter-Facility Consults to work correctly, there must be only one related service at the Consulting Facility. |

### Error 701—Error in Service Name

| Cause                                                                  | Actions Taken                                                                                                                    | Follow-up                                             |
|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| Error in service name (Service name not found at consulting facility). | Consulting site: Notification sent to mail group: GMRC CRNR IFC ERRORS, GMRC CRNR IFC CLIN ERRORS, GMRC TIER II CRNR IFC ERRORS. | Requesting site: Correct the Configuration of Consult |

### Error 702— Service is Disabled

| Cause                                         | Actions Taken                                                                                                                      | Follow-up                                                                                                                |
|-----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| Service has been disabled at Consulting Site. | Consulting site:  Notification sent to mail group:  GMRC CRNR IFC ERRORS, GMRC CRNR IFC CLIN ERRORS, GMRC TIER II CRNR IFC ERRORS. | Requesting site: Verify the correct consult was ordered, or work with the Consulting site to enable the consult service. |

### Error 703— Procedure is Inactive

| Cause                                              | Actions Taken                                                                                                                      | Follow-up                                                                                                              |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Procedure has been inactivated at Consulting Site. | Consulting site:  Notification sent to mail group:  GMRC CRNR IFC ERRORS, GMRC CRNR IFC CLIN ERRORS, GMRC TIER II CRNR IFC ERRORS. | Requesting site: Verify the correct procedure was ordered, or work with the Consulting site to activate the procedure. |

### Error 801—Inappropriate Action for Specified Request

| Cause                                                                             | Actions Taken                                                                                                  | Follow-up                                                                                                |
|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Consult records at the two facilities may be out of synch with regards to status. | Consulting site: Alerts sent to GMRC CRNR IFC ERRORS, GMRC CRNR IFC CLIN ERRORS, GMRC TIER II CRNR IFC ERRORS. | Requesting Site: Contact IRM support at consulting site and compare records to insure they are in synch. |

### Error 802—Duplicate, activity not filed

| Cause                                                                                                                          | Actions Taken                                                                         | Follow-up   |
|--------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|-------------|
| The activity or the consult request in question has been transmitted to the remote site multiple times and is already on file. | Notification sent to mail group:  GMRC CRNR IFC ERRORS, GMRC TIER II CRNR IFC ERRORS. | None.       |

### Error 901—Unable to Update Record Successfully

| Cause                                                                                                               | Actions Taken                                                                 | Follow-up   |
|---------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------|
| Unable to update the record at the consulting facility. The record at the consulting facility is in use and locked. | Requesting site: HL7 message automatically resent every hour until satisfied. | None.       |

### Error 902—Earlier Pending Transactions

| Cause                                                                                                                                                                                                                                                                                                    | Cause                       | Actions Taken   | Actions Taken   | Follow-up   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|-----------------|-----------------|-------------|
| Occurs when an earlier IFC activity wasn't transmitted successfully to the remote facility.  This assures that a later activity doesn't get transmitted before the earlier one is complete and will keep the requesting and consulting facilities in synch. This will not send alerts nor mail messages. | N/A at the consulting site. |                 | None            | None        |

### Error 903—HL Logical Link not Found

| Cause                                          | Actions Taken               | Follow-up   |
|------------------------------------------------|-----------------------------|-------------|
| Unable to find HL Link to the remote facility. | N/A at the consulting site. | None        |

### Error 904—HL7 Unable to Send Transaction

| Cause                          | Actions Taken               | Follow-up   |
|--------------------------------|-----------------------------|-------------|
| Unable to transmit HL message. | N/A at the consulting site. | None        |

### Summary of Errors

| Error Number   | ##   ## Cause                                                                                                                                                                                                                                                                                            |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 101            | Unknown Consult or Procedure request number.                                                                                                                                                                                                                                                             |
| 201            | Unknown Patient. (Patient from MPI not registered at the consulting facility.)                                                                                                                                                                                                                           |
| 202            | Patient is missing an Integration Control number (MPI number) or the ICN is a locally assigned number.                                                                                                                                                                                                   |
| 301            | Sending facility not registered at consulting facility for the requested Service.                                                                                                                                                                                                                        |
| 401            | Sending facility not registered at consulting facility for the requested Procedure.                                                                                                                                                                                                                      |
| 501            | Error in the Procedure name (Procedure name not found at consulting facility).                                                                                                                                                                                                                           |
| 601            | Multiple services attached to a Procedure.                                                                                                                                                                                                                                                               |
| 701            | Error in service name (Service name not found at consulting facility).                                                                                                                                                                                                                                   |
| 702            | Service is disabled at Consulting Site.                                                                                                                                                                                                                                                                  |
| 703            | Procedure is Inactivated at Consulting Site.                                                                                                                                                                                                                                                             |
| 801            | Consult records at the two facilities may be out of synch with regards to status.                                                                                                                                                                                                                        |
| 802            | The activity or the consult request in question has been transmitted to the remote site multiple times and is already on file.                                                                                                                                                                           |
| 901            | Unable to update the record at the consulting facility. The record at the consulting facility is in use and locked.                                                                                                                                                                                      |
| 902            | Occurs when an earlier IFC activity wasn't transmitted successfully to the remote facility.  This assures that a later activity doesn't get transmitted before the earlier one is complete and will keep the requesting and consulting facilities in synch. This will not send alerts nor mail messages. |
| 903            | Unable to find HL Link to consulting facility.                                                                                                                                                                                                                                                           |
| 904            | Unable to transmit HL message.                                                                                                                                                                                                                                                                           |
| None           | Incomplete transmission and no errors.                                                                                                                                                                                                                                                                   |

## Test Account Setup

### HL7 Setup (Test Accounts Only)

#### Information to Gather

The information for the partnering facility can be most efficiently gathered by talking to the VistA systems support staff at the facility from which consults will be requested or received. Use the following table to record the required information from the test accounts at each facility:

##### HL7 Information Table

|   Item # | Item                                                  | ## Local facility  ## (column A)   | ## Partnering facility  ## (column B)   |
|----------|-------------------------------------------------------|------------------------------------|-----------------------------------------|
|        1 | Default Institution a                                 |                                    |                                         |
|        2 | Current domain b                                      |                                    |                                         |
|        3 | IP address and port# where HL7 is listening           |                                    |                                         |
|        4 | HL LOGICAL LINK associated with DEFAULT INSTITUTION d |                                    |                                         |

Notes:

1. DEFAULT INSTITUTION field from the one and only entry in file #8989.3.
2. DOMAIN NAME field from the one and only entry in file #4.3.
3. The IP address is the one used to telnet to the system, port number is typically 5025 for test systems.
4. Usually a nationally exported HL LOGICAL LINK can be found by using VA FileMan to inquire to file 870 and typing in the name or station number of the DEFAULT INSTITUTION. Enter the node name in this block.

### Implementation Steps Using the HL7 Information Table

This step is to configure the HL7 system to properly send and receive messages. The process must be done at the local as well as the partnering facility.

To correctly configure the HL7 message header to provide return address information for correct message administration:

1. Using the Site Parameter Edit [HL EDIT COMM SERVER PARAMETERS] option, edit the one entry and assure:
    1. The CURRENT DOMAIN field matches Item #2, column A.
    2. The CURRENT INSTITUTION field matches Item #1, column A.
    3. The IS THIS A PRODUCTION OR TEST ACCOUNT?  field is set to “training”.
    4. The MAIL GROUP FOR ALERTS field is set to a mail group containing those IRM staff monitoring the HL7 network communications. If there is not such mail group, one should be created and entered here.

2.	Using FileMan, add a new DOMAIN entry to file 4.2 named exactly the same as Item #2, column B.

1. In the *Flags* field, enter “S” for sending.
2. Edit the Synonym field following this example:

If the name of the DOMAIN is TEST.XXX.XX.XXX, you would add TEST.XXX.XX.XXX and TEST.XXX.XX.XXX to the synonym field.

If the name of the DOMAIN is TEST.XXX.XX.XXX, you would add TEST.XXX.XX.XXX and TEST.XXX.XX.XXX to the synonym field.

c. All other fields may be left blank.

1. Using the Institution Edit [XU-INSTITUTION-E] option,  edit the entry corresponding to Item #1, column A and assure that the DOMAIN field is set equal to Item #2, Column A.
2. Using the Institution Edit [XU-INSTITUTION-E] option, edit the entry corresponding to Item #1, column B and assure that the DOMAIN field is set equal to Item #2, Column B.
3. Using the Link Edit [HL EDIT LOGICAL LINKS] option, edit the entry from Item #4, column A and assure:
    1. The INSTITUTION field matches that in Item #1, column A.
    2. The DOMAIN field matches that in Item #2, column A.
    3. The LLP TYPE is set to TCP.
    4. On the second page of the form (accessed by pressing return in the LLP TYPE field), assure:
        1. The TCP/IP SERVICE TYPE field is set to Single Listener (likely a change).
        2. The TCP/IP ADDRESS field matches the ip address in Item #3, column A.
        3. The TCP/IP PORT field matches the port number in Item #3, column A.
    To correctly configure the HL7 message sending information for correct message administration:
        1. Using the Link Edit [HL EDIT LOGICAL LINKS] option, edit the entry from Item #4, column B and assure:
            1. The INSTITUTION field matches that in Item #1, column B.
            2. The DOMAIN field matches that in Item #2, column B.
            3. The LLP TYPE is set to TCP.
            4. On the second page of the form (accessed by pressing return in the LLP TYPE field), assure.
                1. The TCP/IP SERVICE TYPE field is set to CLIENT (SENDER).
                2. The TCP/IP ADDRESS field matches the IP address in Item #3, column B.
                3. The TCP/IP PORT field matches the port number in Item #3, column B.
    To test that the HL7 setup is correct, do the following:
        1. Using the Start/Stop Links [HL START] option, verify that the logical link in Item #4 Column A is running. (You must assure that the partnering facility has done this also.)
        2. Test your configuration using the Ping (TCP Only) [HL PING] option, and when prompted for HL LOGICAL LINK NODE, enter the entry in Item #4, column B. If the option states “PING worked,” communication between the local facility and the partnering facility is possible.  If the option returns any information other than “PING worked,” verify the information in the table and repeat steps 1-6.
    Note: 	For proper Inter-Facility Consults implementation, the preceding steps must be carried out at the partnering site as well.

#### Managing VistA HL7

Much of the management of VistA HL7 for the purposes of Inter-facility Consults will already be done in a production environment, but verifying that it is done will insure the reliability of HL7 messaging for Inter-facility Consults.

##### Steps involved in starting VistA HL7 filers and links for Inter-Facility Consults.

1. Using the Monitor, Start, Stop Filers [HL FILER MONITOR] option:
    1. Verify that at least one incoming filer and at least 1 outgoing filer are running and are not severely overdue
    2. If the filers are not running or are overdue, consult the VistA HL7 Site Manager &amp; Developer Manual for the proper mechanism to start the filers.
2. Using the Start/Stop Links [HL START] option, select the HL LOGICAL LINK from the table Item #4, column B. If the option indicates when the LLP was last started and asks, “Okay to shut down this job?” answer NO. Otherwise it will start the link up and allow outgoing HL7 messages to be routed through that link.
3. Using the Start/Stop Links [HL START] option, select the HL LOGICAL LINK from the table Item #4, column A. If the option indicates when the LLP was last started and asks, “Okay to shut down this job?” answer NO. Otherwise it will ask the method in which to run the receiver. BACKGROUND is the default and recommended setting. If you are not sure, select QUIT.
4. Using the TCP Link Manager Start/Stop [HL START/STOP LINK MANAGER] option, you can determine if the HL7 Link Manager is running.  If the option states: Link Manager already running!, it will ask if you want to stop the Link Manager.  Answer NO. Otherwise this option will start the Link Manager.
5. Each of the preceding steps will need to be completed at the partnering facility as well. Once these steps are complete at both facilities, Inter-facility Consults may be ordered and/or processed by your VAMC.

### Patient Configuration in Test Systems

Note: 	The following instructions apply to test systems only.

Patients that will be used for Inter-facility Consults testing must have matching MPI identifiers (Integration Control Number - ICN)  in the patient file at both partnering facilities.  Since real-time connections with the CIRN-MPI are not readily available from test systems, a utility option is provided to configure patient file entries for use in inter-facility consult testing.

The Configure Test Account Patients for IFC [GMRC IFC TEST PT MPI] option can be used to set the ICN for patients in a test account only. This option is to be used after the partnering facilities have agreed upon a patient that  will be used for testing. After identifying the patient, each site must assure that the name and social security number are identical on each system.  Once this option is executed on each system for the agreed upon patient, inter-facility consult testing may begin using that patient. This process must be repeated for each patient used in testing.

In the following example, we set up a fictional patient to be used in testing at one facility:

Select IFC Management Menu Option: MP  Configure test account patients for IFC

Select shared patient:  CRPATIENT,EIGHT        5-19-46    66666883 2     YES     SC VETERAN

Enrollment Priority:            Category: IN PROCESS    End Date:

Trying to set test patient ICN...

Done.

Select shared patient:

The same option must be executed on a fictional patient with an identical name and social security number at the partnering facility before Inter-Facility consults may be exchanged on that patient.

Note:

- This option will NOT execute in a production VistA system nor is it intended for use there.
- Test system patients with a  pseudo-SSN may not be configured using this option.
- Test system patients with 5 leading zeros in their SSN may not be configured using this option.
- The option will warn the user about any test system patient with a possible national MPI identifier (ICN) but will allow overwriting of that ICN.

## Index

Audience, 2

Background Job, 30

Background Job Parameters, 35

Background Task, 36

Configure Test Account Patients, 26

Coordination, 4

Duplicate activity, 52

Earlier Pending Transactions, 53

Edit IFC Processing Parameters, 34

Error Handling, 39

Error in Procedure Name, 47

Error in Service Name, 49

Errors, 39

Field Relations, 5

HL Logical Link, 54

HL7, 2, 14, 25, 39, 54

HL7 Implementation Steps, 58

HL7 Information Table, 57

HL7 Setup, 57

ICN, 61

IFC CLIN ERRORS, 12

IFC Patient Error Messages, 12

IFC Requests, 16

IFC Requests by Patient, 15, 20

IFC Requests by Remote Ordering Provider, 21

IFC TECH ERRORS, 14

IFC Transaction Report, 30

Inappropriate Action, 52

Integration Control Number, 61

Link not Found, 54

List incomplete IFC transactions, 27

Local or Unknown MPI Identifiers, 43

Locate IFC by Remote Consult Number, 32

Mail Group Setup, 12

Management Options, 23

Managing HL7, 60

Monitor IFC Background Job Parameters, 35

Multiple Services, 48

Patient Configuration, 61

Print All Incomplete IFC Transactions, 29

Print IFC Requests, 19

Procedure Configuration at the Consulting Facility, 10

Procedure Configuration at the Requesting Facility, 9

Procedure is Inactive, 51

Procedure Name, 5, 9, 24, 47

Procedure not Matched, 46

Purpose, 2

Remote Consult Number, 32

Remote Ordering Provider, 21

Reports, 15

Requests by Remote Ordering Provider, 21

Restrictions, 5

Scope of the Manual, 2

Service Configuration at Requesting Facility, 6

Service Configuration at the Consulting Facility, 8

Service is Disabled, 50

Service Name, 6, 24, 27, 49

Service not Matched to Receiving Facility, 45

Summary of Errors, 56

Test Account Patients, 26

Test Account Setup, 57

Test IFC Implementation, 24

Transaction Report, 30

Unable to Send Transaction, 54

Unable to Update Record, 53

Unknown Consult/Procedure request, 40

Unknown MPI Identifiers, 43

Unknown Patient, 41

Web Page, 2