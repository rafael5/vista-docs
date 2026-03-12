---
app_name: Computerized Patient Record System (CPRS)
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: null
doc_type: technical-manual
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-11'
is_base: false
is_change_pages: false
library_max_patch: null
package_id: CPRS
patch: null
patch_gap: null
section: ''
source_file: prt_tm_r.docx
status: draft
title: '#'
---

# Provider Role Tool (PRT)

# Technical Manual

<!-- image -->

July 2021


Revision History

**NOTE:** The revision history cycle begins once changes or enhancements are requested after the document has been baselined.

| **Date**   |   **Revision** | **Description**                                                                                                                    | **Author**            |
|------------|----------------|------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| 07/28/2021 |           0.07 | OR*3*453: Redacted the manual for the VA Document Library (VDL).  Removed names links to software builds.                          | CPRS Development Team |
| 07/16/2021 |           0.06 | OR*3*453: Updated the Remote Procedure Calls section.                                                                              | REDACTED              |
| 11/30/2020 |           0.05 | OR*3*453: Removed the embedded RACI because it is not required in the Technical Manual.                                            | REDACTED              |
| 07/30/2020 |           0.04 | OR*3*453: Fixed a typo in the 6/12/2020 Revision History.  J. Crumley’s name was misspelled.                                       | REDACTED              |
| 06/26/2020 |           0.03 | OR*3*453: Removed the patch number from the title page, updated the RACI, fixed an error in section 1.3 (changed tier 2 to tier 3) | REDACTED              |
| 06/12/2020 |           0.02 | OR*3*453: Revised dates on title page and footers                                                                                  | REDACTED              |
| 07/2019    |           0.01 | OR*3*453: Initial Draft                                                                                                            | REDACTED              |

Artifact Rational

A Technical Manual is a required end-user document for all OI&amp;T software releases. The intended audience for this document is local IT support, management, and development personnel for nationally released software. It provides sufficient technical information about the software for developers and technical personnel to operate and maintain the software with only minimal assistance from Product Support staff.

**Table of Contents**

1.	Introduction	1

1.1.	Purpose	1

1.2.	System Overview	1

1.3.	Document Orientation	2

2.	Implementation and Maintenance	3

2.1.	System Requirements	3

2.2.	System Setup and Configuration	4

3.	Files	4

4.	Routines	4

5.	Exported Options	5

6.	Mail Groups, Alerts, and Bulletins	5

7.	Public Interfaces	5

7.1.	Integration Control Registrations	5

7.2.	Application Programming Interfaces	5

7.3.	Remote Procedure Calls	5

7.4.	HL7 Messaging	6

7.5.	Web Services	6

8.	Standards and Conventions Exemptions	6

8.1.	Internal Relationships	6

8.2.	Software-wide Variables	6

9.	Security	6

9.1.	Security Menus and Options	6

9.2.	Security Keys and Roles	6

9.3.	File Security	6

9.4.	Electronic Signatures	6

9.5.	Secure Data Transmission	6

10.	Archiving	6

11.	Non-Standard Cross-References	6

12.	Troubleshooting	7

12.1.	Special Instructions for Error Correction	7

12.2.	National Service Desk and Organizational Contacts	7

13.	Acronyms and Abbreviations	7

Appendix A. Parameters	9

A.1.	Parameter Definitions	9

## 1 Introduction

### Purpose

The purpose of this Technical Manual is to familiarize users and support personnel with the features and internal workings of the Provider Role Tool (PRT).

### System Overview

The Provider Role Tool application enables authorized users to reassign future alerts for *qualifying patient orders* from a current provider to one or more new providers. The goal of this is to handle the cases where a provider changes roles while remaining at the same site (for example, a provider who moves from VA to DOD but does not relocate or a resident rotates from one specialty service to another, i.e.: Oncology to Surgery). The goal is for the current provider to no longer receive notifications for orders written in the previous role, while being able to receive notifications for orders written in the new role. The purpose is to improve patient care by having alerts available to the provider now responsible for continuing that treatment/therapy for the patient.

The Provider Role Tool is a Graphical User Interface (GUI) application that can run standalone or can be added to the Computerized Patient Record System (CPRS) Tools Menu.

The anticipated responsible group for this reassignment would be the one the provider was leaving. However, it is possible that a site may determine that the reassignment duties would be assigned to a different team – such as the Clinical Application Coordinators. Of course, input from the team the provider is leaving will be required. For example, if a provider is leaving Oncology, the Oncology chief will have to inform the person doing reassignment what provider will pick up the treatment of the patients that are affected.

The following picture shows the architecture from a high level:

<!-- image -->

Figure 1: High-level Architecture (hardware and communication)

### Document Orientation

Audience: Local support staff, such as CACs, Information Technology (IT) Operations and Services (ITOPS) support, Product Support, and development personnel for tier 3 sustainment support.

Assumptions: This manual assumes a working knowledge of VistA.

Document Conventions: This manual uses several methods to highlight different aspects of the material:

- Descriptive text is presented in a proportional font (as represented by this font).
- **Note:** Notes are used to call a user’s attention to an important matter or idea. It will be in bold.
- **Warning:** This paragraph is a caution for users that if they do something, the result could be serious including loss of data.
- “Snapshots” of computer online displays (i.e., character-based screen captures/dialogs) and computer source code are shown in a non-proportional font and enclosed within a box.

Select OPTION NAME: XPAR EDIT PARAMETER		Edit Parameter Values

Edit Parameter Values

#### Disclaimers

##### Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

##### Documentation Disclaimer

The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

#### References

##### Product Documentation

The following documents apply to this release:

- Provider Role Tool Deployment, Installation, Back-Out, and Rollback Guide
- Provider Role Tool Technical Manual
- Provider Role Tool User Guide
- Provider Role Tool Release Notes

All CPRS documents are available at the VA (Software) Documentation Library (VDL) web site at the following CAPRI link: [https://www.va.gov/vdl/section.asp?secid=1](https://www.va.gov/vdl/section.asp?secid=1)

This website is usually updated within 1-3 days of the patch release date.

## 2 Implementation and Maintenance

N/A

### System Requirements

This VistA software is a Kernel Installation and Distribution System (KIDS) software release. The initial distribution will be done via a host file distribution. In addition, there is a GUI executable and help files that will be released as a ZIP file.

#### Hardware Requirements

The Provider Role Tool has no specific additional hardware, server, or workstation requirements. It will run under the existing hardware architecture.

#### Software Requirements

The Provider Role Tool expects a fully patched VistA system for installation.

#### Database Requirements

The Provider Role Tool utilizes and updates the data in the ORDER file (#100).

### System Setup and Configuration

For detailed information on the installation and setup required for the Provider Role Tool, please refer to the associated Deployment, Installation, and Rollback Guide. Summary information about what is exported with the application follows.

## 3 Files

The Provider Role Tool does not export any new files. However, it does modify the existing ORDER file (#100) as follows:

- ORDER TRANSFERS multiple (#70) field and it’s sub-fields:
    - TRANSFER DATE/TIME (#.01) field
    - TRANSFERRED FROM (#.02) field
    - TRANSFERRED TO (#.03) field
    - TRANSFER USER (#.04) field
- New Indices:
    - EPRTRDT created on the ORDER TRANSFERS multiple (#70) field of the ORDER (#100) file. The index is by the:
        - TRANSFERRED TO (.02) field of the ORDER TRANSFERS (#100.011) sub-file of the ORDER (#100) file
        - TRANSFER DATE/TIME (.01) field of the ORDER TRANSFERS (#100.011) sub-file of the ORDER (#100) file
        - ORDER # (.01) field of the ORDER (#100) file
    - EPRACDT created on the ORDER ACTIONS multiple (#.8) field of the ORDER (#100) file. The index is by the:
        - PROVIDER (#3) field of the ORDER ACTION (#100.08) sub-file of the ORDER (#100) file.
        - DATE/TIME ORDERED (#.01) field of the ORDER ACTION (#100.08) sub-file of the ORDER (#100) file.
        - ORDER # (.01) field of the ORDER (#100) file

## 4 Routines

The Provider Role Tool utilizes routines that were already present in the Order Entry/Results Reporting (OR) package.

The initial distribution created/modified the following routines:

ORB3

ORCSAVE

ORELR5

ORQ2

ORQ3

## 5 Exported Options

The only menu option associated with the Provider Role Tool is the GUI context menu: OR PRT GUI.

## 6 Mail Groups, Alerts, and Bulletins

There were no new mail groups, alerts, or bulletins distributed with the Provider Role Tool.

## 7 Public Interfaces

TBD

### Integration Control Registrations

No Integration Control Registrations (ICRs) were created or modified with the Provider Role Tool.

### Application Programming Interfaces

Other than supported ICR types of Application Programming Interfaces (APIs), the following APIs are utilized by the Provider Role Tool:

ORDERER^ORQOR2

STATUS^ORQOR2

### Remote Procedure Calls

The Provider Role Tool created and exported the following Remote Procedure Calls (RPCs):

ORQ3 AUTHUSR

ORQ3 EN

ORQ3 XFER

QRQ3 AUDIT

QRQ3 LOADALL

QRQ3 SAVEALL

QRQ3 XER HISTORY

The Provider Role Tool makes use of the following pre-existing RPCs:

ORWU USERINFO

ORWU DT

ORQOR DETAIL

ORWU NEWPERS

ORWU VERSRV

ORWUX SYMTAB

### HL7 Messaging

N/A

### Web Services

N/A

## 8 Standards and Conventions Exemptions

N/A

### Internal Relationships

N/A

### Software-wide Variables

N/A

## 9 Security

For security information, refer to the Post Installation Considerations in the OR\_3\_453 Install Guide.

### Security Menus and Options

N/A

### Security Keys and Roles

The Provider Role Tool requires that the user hold the OR PRT ACCESS key.

### File Security

The Provider Role Tool creates no new files.

### Electronic Signatures

N/A

### Secure Data Transmission

The Provider Role Tool uses the VistA broker architecture for communicating from the VistA server to the GUI application.

## 10 Archiving

N/A

## 11 Non-Standard Cross-References

N/A

## 12 Troubleshooting

TBD

### Special Instructions for Error Correction

TBD

### National Service Desk and Organizational Contacts

National Service Desk, REDACTED

## 13 Acronyms and Abbreviations

| 2FA   | Two-Factor Authentication                                                                                 |
|-------|-----------------------------------------------------------------------------------------------------------|
| CAC   | Clinical Application Coordinator                                                                          |
| CD2   | Critical Decision Point #2                                                                                |
| CPRS  | Computerized Patient Record System.                                                                       |
| DOD   | Department of Defense                                                                                     |
| GUI   | Graphical User Interface                                                                                  |
| ICR   | Integration Control Registrations                                                                         |
| ITOPS | Information Technology Operations and Services (formerly known as Service Delivery and Engineering [SDE]) |
| KIDS  | Kernel Installation and Distribution System                                                               |
| MVI   | Master Veteran Index                                                                                      |
| NSR   | New Service Request                                                                                       |
| PIN   | Personal Identification Number                                                                            |
| PIV   | Personal Identification Verification                                                                      |
| PRT   | Provider Role Tool                                                                                        |
| RACI  | Responsible, Accountable, Consulted, Informed                                                             |
| SDE   | Service Delivery and Engineering                                                                          |
| VA    | Veterans Affairs                                                                                          |
| VDL   | VA Document Library                                                                                       |
| VIP   | Veteran-focused Integration Process                                                                       |
| VistA | Veterans Health Information Systems and Technology Architecture                                           |

## 14 Appendix A. Parameters

Parameter Definitions

| **Parameter Name**   | **Parameter Definition**                                                                                                                                                                                                                                                             |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PRT EXCEPTION LOGGER | When this parameter is set to "yes", the application will display a custom access violation screen to the user as well as logging the error stack and allowing this to be sent via an email (if PRT EXCEPTION EMAIL is not blank).                                                   |
| PRT EXCEPTION EMAIL  | When the Exception Logger is enabled (PRT EXCEPTION LOGGER), the user has the ability to pre populate an email through Microsoft Outlook. If this parameter is not empty, the user can email the error log and this email address will be used for the pre population of that email. |
| PRT EXCEPTION PURGE  | When an error occurs and the Exception Logger is enabled (PRT EXCEPTION LOGGER), any file(s) that are older than the number of days set in this parameter will be removed from the user's machine.                                                                                   |