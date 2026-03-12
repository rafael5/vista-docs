---
app_name: 'CPRS: Adverse Reaction Tracking (ART) (GMRA)'
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
package_id: GMRA
patch: null
patch_gap: null
section: ''
source_file: gmra_4_50_rn.docx
status: draft
title: Release Notes
---

**Send Mail Message When VA Drug Class Field is Empty**

**Patch GMRA*4.0*50**

# Release Notes

<!-- image -->

**November 2016**


.

Table of Contents

1.	Introduction	1

2.	Purpose	1

3.	Audience	1

4.	This Release	1

4.1.	New Features and Functions Added	1

4.2.	Enhancements and Modifications to Existing	1

4.3.	Known Issues	2

5.	Product Documentation	2

6.	Installation Instructions	2

6.1.	Pre-Installation Instructions	2

6.2.	Installation Instructions	3

6.3.	Post-Installation Instructions	3

## 1 Introduction

This patch generates an email message through the VistA MailMan application when a new causative agent is added to a Patient Allergies File (#120.8) and the VA Drug Class is not specified in the VA Drug Class field (#3).

This modification to VistA originated as a field-developed enhancement for local use at a VA facility. It was determined that the modification would be of benefit to the wider VistA user community, and so it is now being deployed nationally.

The following New Service Request (NSR) is resolved with this patch:

- NSR20140712  – Send Mail Message When VA Drug Class Field is Empty

## 2 Purpose

The purpose of this document is to communicate changes to the VistA system resulting from implementation of GMRA*4.0*50.

## 3 Audience

This document targets users of Adverse Reaction Tracking in VistA and the Computerized Patient Record System (CPRS).

## 4 This Release

The following sections provide a summary of the new features and enhancements introduced by this patch, as well as any known issues.

### New Features and Functions Added

This patch adds no new VistA or CPRS features or functions.

### Enhancements and Modifications to Existing

Patch GMRA*4*50 generates an email message through the VistA MailMan application when a new causative agent is added to a Patient Allergies File (#120.8) and the VA Drug Class is not specified in the VA Drug Class field (#3). Causative agents are medications and substances to which the patient exhibits an adverse reaction or allergy, and are tracked for each patient in the Patient Allergies File (#120.8) using the VistA Adverse Reaction Tracking package. The email message is sent the first time a new causative agent without a designated VA Drug Class is added for a patient. Subsequent observations associated with the same causative agent do not trigger an email. The email is sent only once for each causative agent without a designated VA Drug Class added to a Patient Allergies File (#120.8).

The email message is directed to members of a predefined email group. This email group, “ADVERSE\_ALLERGY\_WARNING,” is created by a post-installation routine if it is not present upon installation of the patch. The email group must be populated with the email addresses of individuals to be notified when a new causative agent is added to a Patient Allergies File (#120.8) without a designated VA Drug Class in the VA Drug Class field (#3).

The following new routine was added to implement the enhancement introduced by this patch:

- GMRA50P1 – This routine builds the ADVERSE\_ALLERGY\_WARNING email group, if it does not already exist. Individuals who should receive an email indicating a causative agent was added to a patient file without a defined VA Drug Class must be added to this group.

The following routines were modified to implement the enhancement introduced by this patch:

- GMRAPEM0 – This routine creates a subroutine that determines if the causative agent passed to it has a defined VA Drug Class. If not, an email is sent to the ADVERSE\_ALLERY\_WARNING email group notifying members of the undefined VA Drug Class.

This routine was also modified to pass the identity of the new causative agent to this new subroutine for processing for the patient whose Patient Allergies File (#120.8) is being edited in VistA.

- GMRAGUI1 – This routine was modified to pass the identity of the new causative agent to the new subroutine in GMRAPEM0 for processing for the patient whose Patient Allergies File (#120.8) is being edited in CPRS.

### Known Issues

None.

## 5 Product Documentation

Additional end-user documentation available for this patch includes:

- Adverse Reaction Tracking Technical Manual – gmra\_4\_tm.pdf
- Adverse Reaction Tracking User Manual – gmra\_4\_tm.pdf

These documents can be found in the VA Software Document Library (VDL).

## 6 Installation Instructions

### Pre-Installation Instructions

The following patches must be installed before GMRA*4.0*50:

- GMRA*4*36
- GMRA*4*42

This patch may be installed with users on the system although it is  recommended that it be installed during non-peak hours to minimize  potential disruption to users.  This patch should take less than 5  minutes to install.

### Installation Instructions

1.	Choose the PackMan message containing this patch.

2.	Choose the INSTALL/CHECK MESSAGE PackMan option.

3.	From the Kernel Installation and Distribution System Menu, select the Installation Menu.  From this menu, you may elect to use the following options. When prompted for the INSTALL NAME enter GMRA*4.0*50.

a. Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.

b.  Print Transport Global - This option will allow you to view the components of the KIDS build.

c. Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed.  It compares all components of this patch (routines, DD's, templates, etc.).

d.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.

4. 	From the Installation Menu, select the Install Package(s) option and choose the patch to install.

5.	If prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//' press &lt;Enter&gt;.

6.	When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO// Press &lt;Enter&gt;

7.	When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// Press &lt;Enter&gt;

8.	If prompted 'Delay Install (Minutes): (0-60): 0//', press &lt;Enter&gt;.

9.	If prompted 'Enter the Device you want to print the Install  messages. You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install. DEVICE: HOME//   HOME (CRT)', press &lt;Enter&gt;.

### Post-Installation Instructions

The mail group: ADVERSE\_ALLERGY\_WARNING was added with this patch.

Appropriate persons will need to be added to this mail group that should  receive the email when the VA Drug Class field is empty.