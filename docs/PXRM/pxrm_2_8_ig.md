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
patch: null
patch_gap: null
section: ''
source_file: pxrm_2_8_ig.docx
status: draft
title: pxrm 2 8 ig.docx
---

<!-- image -->

## Traumatic Brain Injury (TBI) Screening Reminder

**PXRM*2*8**

### INSTALLATION &amp; SETUP GUIDE

**March 2007**

Health Provider Systems Department of Veterans Affairs

#### Contents

INTRODUCTION	1

Web Sites	1

PRE-INSTALLATION	2

Required Software	2

File installed	2

Routines Installed	2

Estimated Installation Time	2

INSTALLATION	3

1. Retrieve the PXRM*2.0*8 build	3
2. Install the build first in a training or test account.	3
3. Load the distribution.	3
    1. Verify Checksums in Transport Global	3
    2. Print Transport Global	4
4. Install the package.	4
    1. Install File Print (optional)	6
    2. Build File Print (optional)	6
    3. Post-installation routine	6
SETUP OF TBI DIALOG	7
    1. Mapping a site-specific quick order	8
    2. Add the nationally distributed reminders to the CPRS Cover Sheet	10
    3. Verify that the dialog functions properly	11
APPENDICES	13
Appendix A: Reminder Definition Inquiry	14
Appendix B: Reminder Dialog Screen Shots	18
ii	Clinical Reminders TBI Screening Patch PXRM*2*8	3/20/2007
Installation and Setup Guide

#### Introduction

PXRM*2*8 distributes the new National VA-TBI SCREENING reminder definition and dialog. This reminder has been developed and sponsored by the Office of Patient Care Services.

##### Web Sites:

[http://vaww1.va.gov/pcs/](http://vaww1.va.gov/pcs/) VHA Patient Care Services (PCS) [http://vista.med.va.gov/reminders](http://vista.med.va.gov/reminders) National Clinical Reminders site

For more detailed information about use of this TBI Screening reminder, please review the PowerPoint at: [http://vista.med.va.gov/reminders/TBI%20SCREENING%20REMINDER%20PPT%203-14-](http://vista.med.va.gov/reminders/TBI%20SCREENING%20REMINDER%20PPT%203-14-07.ppt) [07.ppt](http://vista.med.va.gov/reminders/TBI%20SCREENING%20REMINDER%20PPT%203-14-07.ppt)

#### Pre-Installation

Clinical Reminders patch PXRM*2.0*8 adds one new reminder and dialog, along with taxonomies, reminder terms, and health factors to support the TBI project.

##### Required Software

| **Package/Patch**   | **Namespace**   |   **Version** | **Comments**   |
|---------------------|-----------------|---------------|----------------|
| Clinical Reminders  | PXRM            |           2   | Fully patched  |
| HL7                 | HL              |           1.6 | Fully patched  |
| Kernel              | XU              |           8   | Fully patched  |
| MailMan             | XM              |           7.1 | Fully patched  |
| VA FileMan          | DI              |          22   | Fully patched  |

##### File installed

1. REMINDER EXCHANGE

##### Data is added to the following files:

|   801.41 | REMINDER DIALOG     |
|----------|---------------------|
|    811.5 | REMINDER TERM       |
|    811.9 | REMINDER DEFINITION |

**Routine Installed**

PXRMP8I

##### Estimated Installation Time

This patch can be loaded with users on the system. Installation will take less than two minutes. Installation should be coordinated with the person who manages Clinical Reminders at your site and be scheduled during a time of lower system usage.

#### Installation

This build can be loaded with users on the system. Updating of cross-references for the new data added to the files will occur during the install.

***The install needs to be done by a person with DUZ(0) set to "@."***

##### 1 Retrieve the PXRM*2.0*8 build

Use FTP to access the build, PXRM\_2\_0\_8.KID, from one of the following locations:

| Albany         | REDACTED   | REDACTED   |
|----------------|------------|------------|
| Hines          | REDACTED   | REDACTED   |
| Salt Lake City | REDACTED   | REDACTED   |

##### 2 Install the build first in a training or test account.

Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

##### 3 Load the distribution.

In programmer mode, D ^XUP, select the Kernel Installation &amp; Distribution System menu (XPD MAIN), then the Installation option, then the option LOAD a Distribution. Enter your directory name and PXRM\_2\_0\_8.KID at the Host File prompt.

##### Example

Select Installation Option: **LOAD** a Distribution

Enter a Host File: **PXRM\_2\_0\_8.KID**

KIDS Distribution saved on Comment: TBI Reminder

From the Installation menu, you may elect to use the following options:

##### 4 Verify Checksums in Transport Global

This option will allow you to ensure the integrity of the routines that are in the transport global. If there are any discrepancies, do not run the Install Package(s) option. Instead, run the Unload a Distribution option to remove the Transport Global from your system.

Retrieve the file again from the anonymous directory (in case there was corruption in FTPing) and Load the Distribution again. If the problem still exists, log a Remedy ticket and/or call the national Help Desk (1-888-596-HELP) to report the problem.

##### 5 Print Transport Global

This option will allow you to view the components of the KIDS build.

##### 6 Install the package.

From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the package PXRM*2.0*8 and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

Answer "NO" to the following prompts:

Want KIDS to INHIBIT LOGONs during install? YES// **NO**

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// **NO**

NOTE: Do NOT queue the installation, because this installation may contain a question requiring a response and queuing will stop the installation. (If for some reason, your site doesn’t have GMRCOR CONSULT finding item, you’ll be prompted to enter an existing Order Dialog name.)

##### Installation Example

| 811.8	REMINDER EXCHANGE	(including data) Note:	You already have the 'REMINDER EXCHANGE' File. I will OVERWRITE your data with mine.  Want KIDS to INHIBIT LOGONs during the install? YES// NO  Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO  Enter the Device you want to print the Install messages.  You can queue the install by enter a 'Q' at the device prompt.                                                         |                                                                                                                                              |    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|----|
| Enter a '^' to abort the install.  DEVICE: HOME//	HOME  Complete	PXRM*2.0*8  Install Started for PXRM*2.0*8 :  Mar 07, 2007@15:51:40                                                                                                                                                                                                                                                                                                                      | Do NOT queue the installation, because this installation may contain a question requiring a response and queuing will stop the installation. |    |
| Build Distribution Date: Mar 07, 2007  Installing Routines:  Mar 07, 2007@15:51:40  Running Pre-Install Routine: PRE^PXRMP8I Installing Data Dictionaries:  Mar 07, 2007@15:51:40  Installing Data:  Mar 07, 2007@15:51:40  Running Post-Install Routine: POST^PXRMP8I Installing reminder VA-TBI SCREENING  Updating Routine file... Updating KIDS files...  PXRM*2.0*8 Installed.  Mar 07, 2007@15:51:47  Install Message sent #42971 Install Completed |                                                                                                                                              |    |

##### 7 Install File Print (optional)

Use the KIDS Install File Print option to print out the results of the installation process.

Select Utilities Option: **Install** File Print Select INSTALL NAME: **PXRM***

##### 8 Build File Print (optional)

Use the KIDS Build File Print option to print out the build components.

##### 9 Post-installation routine

The post-install routine, POST^PXRMP8I, installs the “packed” components of the VA- TBI SCREENING reminder and VA-TBI SCREENING reminder dialog onto your system, via reminder exchange tools. The reminder exchange entry being installed is called VA- TBI-SCREENING.

After the installation has finished, if you discover that the components weren’t installed correctly for some reason, you can use the Exchange options on the Reminders Manager Menu to install the components of the “packed” reminder.

The init routine PXRMP8I may be deleted once the installation has completed. Sites should use the Kernel “Delete Routines” option [XTRDEL] to delete this routine.

### Setup of TBI Dialog

The TBI reminder is applicable to all patients whose last service separation date is after 9/11/01 and to active duty patients.

NOTE: This reminder uses the same reminder term that was included in the VA-IRAQ &amp; AFGHAN POST-DEPLOY SCREEN reminder to determine whether active duty patients should be screened or not. The reminder term VA-ACTIVE DUTY is included in this reminder and is available to cause patients to be part of the cohort. This term contains the computed finding

VA-PATIENT TYPE, which can be used to include active duty patients. **Sites that do not screen active duty patients may remove the computed finding from this reminder term.**

This reminder is resolved if the patient did not serve in OEF/OIF, as recorded by using this reminder dialog or the VA-IRAQ &amp; AFGHAN POST-DEPLOY SCREEN dialog. Therefore, the denominator for this reminder is the same as that used for the VA-IRAQ &amp; AFGHAN POST- DEPLOY SCREEN – this number DOES NOT represent the number of patients who served in OEF/OIF. **Please note that this reminder and the VA-IRAQ &amp; AFGHAN POST-DEPLOY SCREEN reminder are not constructed to run reports on those patients who actually served in OEF/OIF.**

- NOTE: Some local sites use additional reminders that have more appropriate denominators and look at patients with known OEF/OIF service who need TBI screening, or who screened positive for TBI and need follow-up, or have positive PTSD screens or positive depression screens.

When a veteran’s screen is positive, the positive findings should be reviewed with the patient by an appropriately trained clinician and a consult for further evaluation recommended. In general, it is best if the clinician personally completes the screen, particularly as the questions asked are of clinical value. If clinic support staff collects answers to the initial questions on the screen, positive screens must be brought to the attention of the responsible clinician immediately and reviewed with the patient. Consults should not be automatically submitted without discussion between clinician and the patient.

##### Setup Steps

After installing Patch 8, follow the steps below to implement your TBI screening reminder and dialog.

The following dialog elements are meant to be used for ordering a consult to the team at your facility that does further evaluation of patients with possible TBI.

VA-TBI OI CONSULT FOR KNOWN TBI VA-PDIQ POLYTRAUMA CONSULT

At the time of install, the Reminder Dialog will use the GMRCOR CONSULT finding item as the consult order dialog for both of these dialog elements. Sites should substitute a quick order or an order menu for ordering consults to the TBI team at your facility. If no such service is available yet, then sites may wish to leave the GMRCOR CONSULT in the element until a consult becomes available.

The mapping of the Quick Order should be done by the site Clinical Reminder Manager.

##### 10 Mapping a site-specific quick order

To map a site-specific quick order to the above elements, do the following from the Reminder Managers menu.

##### Summary of steps:

1. Select DM Reminder Dialog Management.
2. Select DI Reminder Dialogs.
3. Type CV for Change View.
4. Type E for Dialog Elements.
5. Type SL for Search List.
6. Type the name of the element from above.
7. At the Find Next prompt, type No.
8. Type the item number next to the dialog element, VA-TBI OI CONSULT FOR KNOWN TBI.
9. At the finding Item Prompt, enter Q. plus the name of the site-specific Quick Order or order menu.
10. Press Enter at the Additional Finding prompt.
11. Repeat the above steps for the other dialog element, VA-PDIQ POLYTRAUMA CONSULT

##### Detailed Example

1. Select DM Reminder Dialog Management from the Reminder Managers Menu.

Select OPTION NAME:	PXRM MANAGERS MENU	Reminder Managers Menu	menu

CF	Reminder Computed Finding Management ... RM	Reminder Definition Management ...

SM	Reminder Sponsor Management ... TXM	Reminder Taxonomy Management ... TRM	Reminder Term Management ...

LM	Reminder Location List Management ... RX	Reminder Exchange

RT	Reminder Test

OS	Other Supporting Menus ...

INFO	Reminder Information Only Menu ... DM	Reminder Dialog Management ...

CP	CPRS Reminder Configuration ... RP	Reminder Reports ...

MST	Reminders MST Synchronization Management ... PL	Reminder Patient List Menu ...

PAR	Reminder Parameters ...

XM	Reminder Extract Menu ... GEC	GEC Referral Report

Select Reminder Managers Menu Option: DM	Reminder Dialog Management

1. Select DI Reminder Dialogs

DP	Dialog Parameters ... DI	Reminder Dialogs

DR	Dialog Reports ...

IA	Inactive Codes Mail Message

Select Reminder Dialog Management Option: DI	Reminder Dialogs

1. Type CV for Change View.

| Dialog List	Mar 07, 2007@16:03:23	Page:	1 of	27 REMINDER VIEW (ALL REMINDERS BY NAME)  Item Reminder Name	Linked Dialog Name &amp; Dialog Status  1. 01-DIAB PTS (5Y) W/O DIAB EXAM (1Y 2. 10-DIAB PTS (5Y) W/O DIAB EXAM (1Y 3. 21-DIAB PTS (5Y) W/O DIAB EXAM (1Y 4. 691 PNT EYE CLINIC	PNT EYE DIABETES-DLG 5. A NEW REMINDER	A NEW REMINDER	Disabled 6. AGETEST	VA-HEPC AUTOGENERATE TEST   |       |    |                    |                                               |    |      |     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|----|--------------------|-----------------------------------------------|----|------|-----|
| +                                                                                                                                                                                                                                                                                                                                                                                               | Enter | ?? | for more actions   | for more actions                              |    |      | >>> |
| AR	All reminders CV	Change View  Select Item: Next                                                                                                                                                                                                                                                                                                                                              |       |    | LR RN  Screen// CV | Linked Reminders Name/Print Name  Change View | QU | Quit |     |

1. Type E, for Dialog Elements

Select one of the following:

1. Reminder Dialogs
2. Dialog Elements
3. Forced Values
4. Dialog Groups

P	Additional Prompts

R	Reminders

RG	Result Group (Mental Health) RE	Result Element (Mental Health)

TYPE OF VIEW: R// E	Dialog Elements

1. Type SL for Search List.

1. Type the name of the dialog element, VA-TBI OI CONSULT FOR KNOWN TBI.

Select Item: Next Screen// SL	SL

Search for: VA-TBI OI CONSULT FOR KNOWN TBI

1. ADDITIONAL COMMENTS (PXRM COMMENT)	Dialog Element
2. ADDITIONAL COMMENTS(2 LINES WP)	Dialog Element

...searching for 'VA-TBI OI CONSULT FOR KNOWN TBI'................

Find Next 'VA-TBI OI CONSULT FOR KNOWN TBI'? Yes// NO

CO	Copy Dialog	PT	List/Print All	QU	Quit

1. Type the item number next to the element, then press Enter

| Dialog List	Mar 07, 2007@16:04:22	Page:	102 of	115 DIALOG VIEW (DIALOG ELEMENTS)  +Item Dialog Name	Dialog type	Status  162	VA-TBI OI CONSULT FOR KNOWN TBI	Dialog Element  162	VA-TBI SCREEN REFUSAL	Dialog Element  162	VA-TEXT AIMS INSTRUCTION	Dialog Element  162	VA-TEXT AIMS INSTRUCTION (1)	Dialog Element  162	VA-TEXT BLANK LINE	Dialog Element   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **+	+ Next Screen	- Prev Screen	?? More Actions	&gt;&gt;&gt;**                                                                                                                                                                                                                                                                                              |
| AD	Add	CV	Change View	INQ	Inquiry/Print CO	Copy Dialog	PT	List/Print All	QU	Quit  Select Item: Next Screen// 162  Dialog Name:  **VA-TBI OI CONSULT FOR KNOWN TBI**  Current dialog element/group name: VA-TBI OI CONSULT FOR KNOWN TBI Used by:	VA-TBI TEXT PREVIOUS DX NO SCREEN (Dialog Group)                                                           |

1. At the finding Item Prompt, enter Q. plus the name of the site-specific Quick Order or order menu.

FINDING ITEM: GMRCOR CONSULT// **Q.ZGMRC TBI**

1. Press Enter at the Additional Finding prompt.

Select ADDITIONAL FINDINGS: **&lt;Enter&gt;**

Input your edit comments. Edit? NO//

1. Repeat the above steps for the other dialog element, VA-PDIQ POLYTRAUMA CONSULT

##### 11 Add the nationally distributed reminders to the CPRS Cover Sheet

1. Open a patient chart, click on the reminders clock, and when the available Reminders window opens, click on Action, and then select “Edit Cover Sheet Reminder List.”

1. When the Cover Sheet Reminder List opens, find the TBI screening reminder.

<!-- image -->

1. Click on the TBI Screening (VA-TBI SCREENING) reminder and click the Add button (or double-click the reminder).

##### 12 Verify that the dialog functions properly

Test the TBI Reminder dialog in CPRS and verify the following:

- Correct Progress Note text is posted
- Finding Item gets sent to PCE
- Reminder is satisfied

Check the Clinical Maintenance component display in CPRS after testing the dialog to ensure that all the activities are reflected in the clinical maintenance display.

<!-- image -->

## Appendices

##### Appendix A: VA-TBI SCREENING Reminder Inquiry

**Appendix B: VA-TBI SCREENING reminder dialog screen shots**

##### Appendix A: Reminder Definition Inquiry

Select Reminder Definition: TBI Screening	VA-TBI SCREENING	NATIONAL DEVICE: ;;999	HOME

REMINDER DEFINITION INQUIRY	Mar 07, 2007 2:03:47 pm	Page 1

VA-TBI SCREENING	No.	793

Print Name:	TBI Screening

Class:	NATIONAL

Sponsor:	Office of Patient Care Services Review Date:

Rescission Date:

Usage: CPRS, DATA EXTRACT, REPORTS

Related VA-* Reminder:

Reminder Dialog:	VA-TBI SCREENING Priority:

Reminder Description:

Reminder is applicable once in a lifetime of all patients whose date of separation from the service is 9/11/01 or later and have had service in OEF/OIF.	If Service Date of Separation is more recent than last TBI Screening, then reminder will be due again for patient.

Reminder is resolved by completing the screen.

Reminder creation requested by the Office of Patient Care Services. Designed by the TBI Screening Workgroup chaired by Dr. Barbara Sigford and based on a reminder from Minneapolis built by Ronald Patire.

Technical Description:

Reminder is due for all patients with DOS of 9/11/01 or later.	Reminder is resolved by any of the health factors associated with the responses of section 1; OR health factor for Previous TBI Diagnosis; OR health factor TBI PT Refused..

Baseline Frequency:

Do In Advance Time Frame:	Wait until actually DUE Sex Specific:

Ignore on N/A:

Frequency for Age Range:	99Y - Once for all ages Match Text:

No Match Text:

Findings:

---- Begin: VA-IRAQ/AFGHAN PERIOD OF SERVICE	(FI(1)=RT(490)) ------------

Finding Type: REMINDER TERM Use in Patient Cohort Logic: AND

Beginning Date/Time: 09/11/2001

Not Found Text: The patient's last service separation date is prior to 9/11/01.

\\

Mapped Findings:

Mapped Finding Item: CF.VA-LAST SERVICE SEPARATION DATE

Beginning Date/Time: SEP 11, 2001

---- End: VA-IRAQ/AFGHAN PERIOD OF SERVICE -------------------------------

---- Begin: VA-ACTIVE DUTY	(FI(2)=RT(568019)) ---------------------------

Finding Type: REMINDER TERM Use in Patient Cohort Logic: OR

Mapped Findings:

Mapped Finding Item: CF.VA-PATIENT TYPE Condition: I V="ACTIVE DUTY"

End: VA-ACTIVE DUTY

---- Begin: VA-TBI SCREENING COMPLETED SCREENING RESOLUTIONS	(FI(3)=RT(824))

Finding Type: REMINDER TERM Use in Resolution Logic: AND

Mapped Findings:

Mapped Finding Item: HF.TBI-FRAGMENT/BULLET Health Factor Category: TBI SOURCE

Mapped Finding Item: HF.TBI-BULLET Health Factor Category: TBI SOURCE

Mapped Finding Item: HF.TBI-VEHICULAR Health Factor Category: TBI SOURCE

Mapped Finding Item: HF.TBI-FALL Health Factor Category: TBI SOURCE

Mapped Finding Item: HF.TBI-BLAST Health Factor Category: TBI SOURCE

Mapped Finding Item: HF.TBI-SECTION I - NO Health Factor Category: TBI-SECTIONS

---- End: VA-TBI SCREENING COMPLETED SCREENING RESOLUTIONS ---------------

---- Begin: VA-IRAQ/AFGHAN SERVICE NO	(FI(4)=RT(489)) -------------------

Finding Type: REMINDER TERM Use in Resolution Logic: OR

Found Text: The record indicates that the patient did not serve in OEF or OIF.

\\

Mapped Findings:

Mapped Finding Item: HF.NO IRAQ/AFGHAN SERVICE Health Factor Category: IRAQ/AFGHANISTAN

End: VA-IRAQ/AFGHAN SERVICE NO

---- Begin: VA-IRAQ/AFGHAN SERVICE	(FI(5)=RT(568012)) -------------------

Finding Type: REMINDER TERM

Mapped Findings:

Mapped Finding Item: HF.IRAQ/AFGHAN SERVICE Health Factor Category: IRAQ/AFGHANISTAN

End: VA-IRAQ/AFGHAN SERVICE

---- Begin: VA-TBI-PREVIOUS TBI DX	(FI(6)=RT(828)) ----------------------

Finding Type: REMINDER TERM Use in Resolution Logic: OR

Beginning Date/Time: 9/11/01

Found Text: Patient has documentation of previous TBI diagnosis on chart.

Mapped Findings:

Mapped Finding Item: HF.TBI-PREVIOUS TBI DX Health Factor Category: TBI-SECTIONS

End: VA-TBI-PREVIOUS TBI DX

---- Begin: VA-TBI-PT REFUSAL	(FI(7)=RT(829)) ---------------------------

Finding Type: REMINDER TERM Use in Resolution Logic: OR

Beginning Date/Time: T-30D

Mapped Findings:

Mapped Finding Item: HF.TBI-PT REFUSAL Health Factor Category: TBI-SECTIONS

End: VA-TBI-PT REFUSAL

---- Begin: VA-LAST SERVICE SEPARATION DATE	(FI(8)=CF(27)) --------------

Finding Type: REMINDER COMPUTED FINDING

---- End: VA-LAST SERVICE SEPARATION DATE --------------------------------

Function Findings:

---- Begin: FF(1)---------------------------------------------------------

Function String: MRD(4)&gt;MRD(1) Expanded Function String:

MRD(VA-IRAQ/AFGHAN SERVICE NO)&gt;MRD(VA-IRAQ/AFGHAN PERIOD OF SERVICE)

Not Found Text: The patient's most recent service separation date is more recent than their last screening

- if the patient was discharged after 9/11/01 then rescreening is needed after any new period of service.

End: FF(1)

---- Begin: FF(2)---------------------------------------------------------

Function String: MRD(3)&gt;MRD(1) Expanded Function String:

MRD(VA-TBI SCREENING COMPLETED SCREENING RESOLUTIONS)&gt;MRD( VA-IRAQ/AFGHAN PERIOD OF SERVICE)

End: FF(2)

---- Begin: FF(3)---------------------------------------------------------

Function String: MRD(1)&gt;MRD(4,5) Expanded Function String:

MRD(VA-IRAQ/AFGHAN PERIOD OF SERVICE)&gt;MRD(VA-IRAQ/AFGHAN SERVICE NO, VA-IRAQ/AFGHAN SERVICE)

Found Text: The patient's most recent service separation date is more recent than their last screening

- if the patient was discharged after 9/11/01 then rescreening is needed after any new period of service.

End: FF(3)

General Patient Cohort Found Text:

Patients who served in combat in either Iraq (Operation Iraqi Freedom) or in Afghanistan (Operation Enduring Freedom) should be screened for Traumatic Brain Injury.

General Patient Cohort Not Found Text:

Patients who were discharged from the service prior to 9/11/01 or who did NOT serve in OEF or OIF do NOT need to be screened for TBI.

Default PATIENT COHORT LOGIC to see if the Reminder applies to a patient: (SEX)&amp;(AGE)&amp;FI(1)!FI(2)

Expanded Patient Cohort Logic:

(SEX)&amp;(AGE)&amp;FI(VA-IRAQ/AFGHAN PERIOD OF SERVICE)!FI(VA-ACTIVE DUTY)

Customized RESOLUTION LOGIC defines findings that resolve the Reminder: (FI(4)&amp;FF(1))!(FI(5)&amp;FF(2))!FI(6)!FI(7)

Expanded Resolution Logic:

(FI(VA-IRAQ/AFGHAN SERVICE NO)&amp;FF(1))!(FI(VA-IRAQ/AFGHAN SERVICE)&amp; FF(2))!FI(VA-TBI-PREVIOUS TBI DX)!FI(VA-TBI-PT REFUSAL)

Web Sites:

##### Appendix B: Reminder Dialog Screen Shots

For more detailed information about use of this TBI Screening reminder, please review the PowerPoint at: [http://vista.med.va.gov/reminders/TBI%20SCREENING%20REMINDER%20PPT%203-14-](http://vista.med.va.gov/reminders/TBI%20SCREENING%20REMINDER%20PPT%203-14-07.ppt) [07.ppt](http://vista.med.va.gov/reminders/TBI%20SCREENING%20REMINDER%20PPT%203-14-07.ppt)

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->