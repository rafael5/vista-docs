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
source_file: pxrm_2_0_53_rn.docx
status: draft
title: pxrm 2 0 53 rn.docx
---

**PXRM*2*53**

## Clinical Reminders


## REMINDER DIALOG SEARCH REPORT

## Release Notes

**September 2015**

Product Development


###### Table of Contents

Introduction	1

Install Details	1

Appendix A: Install Example	3

Appendix B: Search Report Examples	5

## Introduction

This patch adds a Reminder Dialog Search Report option to the Reminder Dialog Report menu. The Reminder Dialog Search Report allows sites to find Reminder Dialogs based on search criteria such as Coding Systems, Findings, and Dialog Items.

## Install Details


This patch is being distributed as a Packman Message.  The name of the host file is PXRM\_2\_0\_53.KID.  This file should be downloaded in ASCII format.

1.  Choose the PackMan message containing this patch.

2.  Choose the INSTALL/CHECK MESSAGE PackMan option.

3.  From the Kernel Installation and Distribution System Menu, select

the Installation Menu.  From this menu, you may elect to use the

following options. When prompted for the INSTALL NAME enter the patch

#(ex. PXRM*2.0*53):

a.  Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will not

backup any other changes such as DDs or templates.

b.  Compare Transport Global to Current System - This option will

allow you to view all changes that will be made when this patch

is installed.  It compares all components of this patch

(routines, DDs, templates, etc.).

c.  Verify Checksums in Transport Global - This option will allow

you to ensure the integrity of the routines that are in the

transport global.

4.  From the Installation Menu, select the Install Package(s) option and

choose the patch to install.

5.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of

Install? NO//' NO

6.  When prompted 'Want KIDS to INHIBIT LOGONs during the install?

NO//' NO

7.  When prompted 'Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO//' NO

8. If prompted 'Delay Install (Minutes):  (0 - 60): 0//' respond 0.


## Appendix A: Install Example

Select INSTALL NAME:    PXRM*2.0*53    1/8/15@10:32:06

=&gt; PXRM*2*53

This Distribution was loaded on Jan 08, 2015@10:32:06 with header of

PXRM*2*53

It consisted of the following Install(s):

PXRM*2.0*53

Checking Install for Package PXRM*2.0*53

Install Questions for PXRM*2.0*53

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME//   HOME (CRT)

Install Started for PXRM*2.0*53 :

Jan 08, 2015@10:33:03

Build Distribution Date: Nov 05, 2014

PXRM*2.0*53

--------------------------------------------------------------------------------

Installing Routines:

Jan 08, 2015@10:33:03

Installing PACKAGE COMPONENTS:

Installing OPTION

Jan 08, 2015@10:33:03

Updating Routine file...

Updating KIDS files...

PXRM*2.0*53 Installed.

Jan 08, 2015@10:33:03

Not a production UCI

NO Install Message sent

-------------------------------------------------------------------------------

+------------------------------------------------------------+

100%    ¦             25             50             75               ¦

Complete  +------------------------------------------------------------+

Install Completed

## Appendix B: Search Report Examples

Patch 53 (PXRM*2*53) Changes

PXRM*2*53 adds a Reminder Dialog Search Report option to the Reminder Dialog Report menu. The Reminder Dialog Search Report allows sites to find Reminder Dialogs that contain user entered search criteria such as Coding Systems, Findings, and Dialog components.

There are three main search options that can be used individually or combined together to get a larger report:

Search for coding system

Search for Finding Item(s) used in dialog component(s)

Search for specific Reminder Dialog component(s)

If you select Yes at the Search for coding system prompt and you also select Yes to one of the other prompts, this would work IN ADDITION TO the code search. Your output would have the dialogs that contained the coding system selected and also any dialogs that have the finding item or dialog item selected. If you only wanted to know every dialog that contained a coding system, select yes to the first coding prompt and select no to the next two prompts.

After choosing your main search option, you also have these options:

Search for Reminder Dialog by CPRS parameter(s)?

Display match criteria on the report?

Select Dialog Reports Option: SEA  Reminder Dialog Search Report

Search for coding system? N//

Enter 'Y' to build a list of coding systems. This list will be used to

find taxonomies with at least one code from the selected coding system

marked to be used in a dialog. Enter 'N' to skip search for coding

systems.

Select from the following coding systems:

1 10D

2 CPC

3 CPT

4 ICD

Enter your list for search criteria:  (1-4):

Search for Finding Item(s) used in dialog component(s)? N//

Enter 'Y' to build a list of Finding Items for which to search. This

list of items will be used to find dialogs in which they are contained

in either the Finding Item, Additional Finding Items or a Result Group

MH Test field. Enter 'N' to skip search for finding items.

If Yes is chosen, then additional options come up:

Search for Finding Item(s) used in dialog component(s)? N// YES

Select from the following reminder findings (* signifies standardized):

1 - EDUCATION TOPICS

2 - EXAM

3 - HEALTH FACTOR

4 - IMMUNIZATION

5 - MENTAL HEALTH

6 - ORDER DIALOG

7 - REMINDER TAXONOMY

8 - SKIN TEST

9 - VITAL TYPE

10 - WH NOTIFICATION PURPOSE

Enter your list for the report:  (1-10): 7

Search for all or selected REMINDER TAXONOMYS?

Select one of the following:

1         ALL

2         SELECTED

Enter response: SELECTED// 1  ALL

Search for specific Reminder Dialog component(s)? N//

Enter 'Y' to build a list of dialog items (Element, Group, Prompt,

Forced Value, Result Group, Result Element) for which to search. This

list will be used to find parent dialog(s) in which they are contained.

Enter 'N' to not look for dialog items.

Search for specific Reminder Dialog component(s)? N// YES

Select Dialog Definition:

Search for Reminder Dialog by CPRS parameter(s)? N//

Enter 'Y' to search for dialogs used on a CPRS CoverSheet set by a CPRS parameter such as by Division, Location, Service, System, User or User Class

and dialogs assigned as a TIU Template. Enter 'N' to search all dialog.

**This option should be used with one of the other above search criteria*

*The output will display all dialogs that fit into the selected CPRS parameter (Division, Location, Service, System, User, User Class) that have the chosen search criteria. This will narrow your search results to those that fit the parameter chosen.*

IF Yes is chosen then an additional option displays:

Search for Reminder Dialog by CPRS parameter(s)? N// YES

1 - Division

2 - Location

3 - Service

4 - System

5 - User

6 - User Class

Enter your list for the report:  (1-6):

Display match criteria on the report? N//

Enter 'Y' to display which search criteria was found in the dialog.

This information will be displayed with the dialog name in report

output under the Match Criteria heading. Enter 'N' to display the

dialog name only.

**Marking Yes will show a detailed report, No will show a summary report.*

Browse or Print? B// Print

At the end of the report you will have the option to deliver the report as a MailMan message.

Report Examples:

To Display a List of Dialogs that Contain a Specific Coding System (Summary Report)

In this example the search criteria is ICD10 codes:

Select Dialog Reports Option: SEA  Reminder Dialog Search Report

Search for coding system? N// YES

Select from the following coding systems:

1 10D

2 CPC

3 CPT

4 ICD

Enter your list for search criteria:  (1-4): 1

Search for Finding Item(s) used in dialog component(s)? N// O

Search for specific Reminder Dialog component(s)? N// O

Search for Reminder Dialog by CPRS parameter(s)? N// O

Display match criteria on the report? N// O

Browse or Print? B// Print

DEVICE: HOME//   TELNET PORT

Clinical Reminders Dialogs search report.

Reminder Dialogs:

Dialog: JMS HYPERTENSION NUTRITION/WT EDUC

Dialog: JMS VA-BLOOD PRESSURE CHECK

Dialog: NCG HYPERTENSION SCREEN

Press ENTER to continue:

Deliver the report as a MailMan message? N// O

To Display a List of Dialogs that Contain a Specific Coding System (Detail Report)

In this example the search criteria is icd10 codes:

Select Dialog Reports Option: SEA  Reminder Dialog Search Report

Search for coding system? N// YES

Select from the following coding systems:

1 10D

2 CPC

3 CPT

4 ICD

Enter your list for search criteria:  (1-4): 1

Search for Finding Item(s) used in dialog component(s)? N// O

Search for specific Reminder Dialog component(s)? N/// O

Search for Reminder Dialog by CPRS parameter(s)? N// O

Display match criteria on the report? N// YES *SELECTING YES HERE WILL GIVE A DETAILED REPORT*

Browse or Print? B// Print

DEVICE: HOME//   TELNET PORT

Clinical Reminders Dialogs search report.

Reminder Dialogs:

Dialog: JMS HYPERTENSION NUTRITION/WT EDUC

Match Criteria:

Dialog Element: TX HYPERTENSION CODES

Finding: TX.VA-HYPERTENSION

Coding System: 10D

Dialog: JMS VA-BLOOD PRESSURE CHECK

Match Criteria:

Dialog Element: TX HYPERTENSION CODES

Finding: TX.VA-HYPERTENSION

Coding System: 10D

Dialog: NCG HYPERTENSION SCREEN

Match Criteria:

Dialog Element: TX HYPERTENSION CODES

Finding: TX.VA-HYPERTENSION

Coding System: 10D

Press ENTER to continue:

Deliver the report as a MailMan message? N// O

To Display a List of Dialogs that Contain a Specific Coding System (Detail Report) that Are Assigned at the System Level

In this example the search criteria is ICD-9 codes:

Select Dialog Reports &lt;TEST ACCOUNT&gt; Option: SEA  Reminder Dialog Search Report

Search for coding system? N// YES

Select from the following coding systems:

1 10D

2 CPC

3 CPT

4 ICD

Enter your list for search criteria:  (1-4): 4

Search for Finding Item(s) used in dialog component(s)? N// O

Search for specific Reminder Dialog component(s)? N// O

Search for Reminder Dialog by CPRS parameter(s)? N// YES

1 - Division

2 - Location

3 - Service

4 - System

5 - User

6 - User Class

Enter your list for the report:  (1-6): 4

Display match criteria on the report? N// YES

Browse or Print? B// Print

DEVICE: HOME// 0;240;99999  TELNET PORT

Clinical Reminders Dialogs search report.

CPRS Cover Sheet Reminder Dialogs for System:

Dialog: AIMS Test

Match Criteria:

Dialog Element: POV SCREENING FOR OTHER SPECIFIED CONDITIONS DONE

Finding: TX.POV SCREENING FOR OTHER SPECIFIED CONDITIONS DONE

Coding System: ICD

Dialog Element: POV SCREENING FOR OTHER SPECIFIED CONDITIONS DONE

ELSEWHERE

Finding: TX.POV SCREENING FOR OTHER SPECIFIED CONDITIONS DONE

Coding System: ICD

Dialog: AM DM A1C

Match Criteria:

Dialog Element: TX DIABETIC DIAGNOSIS CODES

Finding: TX.DIABETES

Coding System: ICD

Press ENTER to continue:

Deliver the report as a MailMan message? N// O

Report of All Dialogs that Have a Finding Item (Summary)

In this example the search criteria is dialogs that contain education topics:

Select Dialog Reports Option: SEA  Reminder Dialog Search ReportSearch for coding system? N// O

Search for Finding Item(s) used in dialog component(s)? N// YES

Select from the following reminder findings (* signifies standardized):

1 - EDUCATION TOPICS

2 - EXAM

3 - HEALTH FACTOR

4 - IMMUNIZATION

5 - MENTAL HEALTH

6 - ORDER DIALOG

7 - REMINDER TAXONOMY

8 - SKIN TEST

9 - VITAL TYPE

10 - WH NOTIFICATION PURPOSE

Enter your list for the report:  (1-10): 1

Search for all or selected EDUCATION TOPICS?

Select one of the following:

1         ALL

2         SELECTED

Enter response: SELECTED// 1  ALL

Search for specific Reminder Dialog component(s)? N// O

Search for Reminder Dialog by CPRS parameter(s)? N// O

Display match criteria on the report? N// O

Browse or Print? B// Print

DEVICE: HOME//   TELNET PORT

Clinical Reminders Dialogs search report.

Reminder Dialogs:

Dialog: VA-ALCOHOL F/U POS AUDIT-C

Dialog: VA-ECOE EDUCATION TPL

Dialog: VA-ECOE FOLLOW-UP NOTE

Press ENTER to continue:

Deliver the report as a MailMan message? N//

Report of All Dialogs that Have a Finding Item (Detail)

In this example the search criteria is all dialogs that contain education topics:

SEA  Reminder Dialog Search Report

Search for coding system? N// O

Search for Finding Item(s) used in dialog component(s)? N// YES

Select from the following reminder findings (* signifies standardized):

1 - EDUCATION TOPICS

2 - EXAM

3 - HEALTH FACTOR

4 - IMMUNIZATION

5 - MENTAL HEALTH

6 - ORDER DIALOG

7 - REMINDER TAXONOMY

8 - SKIN TEST

9 - VITAL TYPE

10 - WH NOTIFICATION PURPOSE

Enter your list for the report:  (1-10): 1

Search for all or selected EDUCATION TOPICS?

Select one of the following:

1         ALL

2         SELECTED

Enter response: SELECTED// 1  ALL

Search for specific Reminder Dialog component(s)? N// O

Search for Reminder Dialog by CPRS parameter(s)? N// O

**Display match criteria on the report? N// YES**

Browse or Print? B// Print

DEVICE: HOME//   TELNET PORT

Clinical Reminders Dialogs search report.

Reminder Dialogs:

Dialog: VA-ALCOHOL F/U POS AUDIT-C

Match Criteria:

Dialog Element: VA-HF ALC WITHIN SAFE LIMITS CONTINUE

Finding: ED.ALCOHOL USE AND MEDICAL PROBLEMS

Dialog Group: VA-GP ALC SCREEN POS MEDICAL PROBLEMS

Finding: ED.ALCOHOL USE AND MEDICAL PROBLEMS

Dialog: VA-ECOE EDUCATION TPL

Match Criteria:

Dialog Element: VA-ECOE EDU OTHER

Finding: ED.VA-ECOE OTHER TOPIC

Dialog: VA-ECOE FOLLOW-UP NOTE

Match Criteria:

Dialog Element: VA-ECOE EDU OTHER

Finding: ED.VA-ECOE OTHER TOPIC

Dialog Element: VA-ECOE EDU PRECAUTIONS EL

Finding: ED.VA-ECOE SEIZURE PRECAUTIONS

Dialog Element: VA-ECOE EDU AED SIDE EFFECTS EL

Finding: ED.VA-ECOE AED SIDE EFFECTS

Dialog Element: VA-ECOE EDU CONTRACEPTION EL

Finding: ED.VA-ECOE CONTRACEPTION

Dialog Element: VA-ECOE EDU DRIVING EL

Finding: ED.VA-ECOE DRIVING

Press ENTER to continue:

Deliver the report as a MailMan message? N//

Report of All Dialogs that Have a Finding Item (Summary)

In This Example The Search Criteria Is Dialogs That Contain A Specific Mental Health Finding:

Select Dialog Reports Option: SEA  Reminder Dialog Search Report

Search for coding system? N// O

Search for Finding Item(s) used in dialog component(s)? N// YES

Select from the following reminder findings (* signifies standardized):

1 - EDUCATION TOPICS

2 - EXAM

3 - HEALTH FACTOR

4 - IMMUNIZATION

5 - MENTAL HEALTH

6 - ORDER DIALOG

7 - REMINDER TAXONOMY

8 - SKIN TEST

9 - VITAL TYPE

10 - WH NOTIFICATION PURPOSE

Enter your list for the report:  (1-10): 5

Search for all or selected MENTAL HEALTHS?

Select one of the following:

1         ALL

2         SELECTED

Enter response: SELECTED//

Select MENTAL HEALTH: AUDIT

Select MENTAL HEALTH:

Search for specific Reminder Dialog component(s)? N// O

Search for Reminder Dialog by CPRS parameter(s)? N// O

Display match criteria on the report? N// O

Browse or Print? B// Print

DEVICE: HOME//   TELNET PORT

Clinical Reminders Dialogs search report.

Reminder Dialogs:

Dialog: ALCOHOL USE SCREEN POS DIALOG

Dialog: CO-ALCOHOL F/U POS AUDIT-C

Dialog: VA-ALCOHOL F/U POS AUDIT-C

Press ENTER to continue:

Deliver the report as a MailMan message? N//

Report of All Dialogs that Have a Finding Item (Detail):

In this example the search criteria is dialogs that contain a specific mental health finding:

Select Dialog Reports Option: SEA  Reminder Dialog Search Report

Search for coding system? N// O

Search for Finding Item(s) used in dialog component(s)? N// YES

Select from the following reminder findings (* signifies standardized):

1 - EDUCATION TOPICS

2 - EXAM

3 - HEALTH FACTOR

4 - IMMUNIZATION

5 - MENTAL HEALTH

6 - ORDER DIALOG

7 - REMINDER TAXONOMY

8 - SKIN TEST

9 - VITAL TYPE

10 - WH NOTIFICATION PURPOSE

Enter your list for the report:  (1-10): 5

Search for all or selected MENTAL HEALTHS?

Select one of the following:

1         ALL

2         SELECTED

Enter response: SELECTED//

Select MENTAL HEALTH: AUDIT

Select MENTAL HEALTH:

Search for specific Reminder Dialog component(s)? N// O

Search for Reminder Dialog by CPRS parameter(s)? N// O

Display match criteria on the report? N// YES

Browse or Print? B// Print

DEVICE: HOME//   TELNET PORT

Clinical Reminders Dialogs search report.

Reminder Dialogs:

Dialog: ALCOHOL USE SCREEN POS DIALOG

Match Criteria:

Dialog Element: TEST AUDIT 10

Finding: MH.AUDIT

Dialog: CO-ALCOHOL F/U POS AUDIT-C

Match Criteria:

Dialog Result Group: PXRM AUDIT RESULT GROUP

Finding: MH.AUDIT

Dialog Element: VA-HF ETOH SELF SCORE AUD 10

Finding: MH.AUDIT

Dialog: VA-ALCOHOL F/U POS AUDIT-C

Match Criteria:

Dialog Result Group: PXRM AUDIT RESULT GROUP

Finding: MH.AUDIT

Dialog Element: VA-HF ETOH SELF SCORE AUD 10

Finding: MH.AUDIT

Press ENTER to continue:

Deliver the report as a MailMan message? N// O

To Find Everywhere a Dialog Component Is Used (Summary):

In this example the search criteria is a specific reminder dialog element:

Select Dialog Reports Option: SEA  Reminder Dialog Search Report

Search for coding system? N// O

Search for Finding Item(s) used in dialog component(s)? N// O

Search for specific Reminder Dialog component(s)? N// YES

Select Dialog Definition: VA-HF ACUTE ILLNESS       dialog element     NATIONAL

Select Dialog Definition:

Search for Reminder Dialog by CPRS parameter(s)? N// O

Display match criteria on the report? N// O

Browse or Print? B// Print

DEVICE: HOME//   TELNET PORT

Clinical Reminders Dialogs search report.

Reminder Dialogs:

Dialog: VA-ALCOHOL USE SCREENING (AUDIT-C)

Dialog: VA-DEPRESSION SCREEN

Dialog: VA-EMBEDDED FRAGMENTS RISK EVALUATION

Dialog: VA-IRAQ &amp; AFGHANISTAN POST DEPLOYMENT SCREEN

Dialog: VA-PTSD SCREENING

Press ENTER to continue:

Deliver the report as a MailMan message? N//

To Find Everywhere a Dialog Component Used (Detail)

In this example the search criteria is a specific reminder dialog element:

Select Dialog Reports Option: SEA  Reminder Dialog Search Report

Search for coding system? N// O

Search for Finding Item(s) used in dialog component(s)? N// O

**Search for specific Reminder Dialog component(s)? N// YES**

Select Dialog Definition: VA-HF ACUTE ILLNESS     dialog element     NATIONAL

Select Dialog Definition:

Search for Reminder Dialog by CPRS parameter(s)? N// O

**Display match criteria on the report? N// YES**

Browse or Print? B// Print

DEVICE: HOME//   TELNET PORT

Clinical Reminders Dialogs search report.

Reminder Dialogs:

Dialog: VA-ALCOHOL USE SCREENING (AUDIT-C)

Match Criteria:

Dialog : VA-HF ACUTE ILLNESS

Dialog: VA-DEPRESSION SCREEN

Match Criteria:

Dialog : VA-HF ACUTE ILLNESS

Dialog: VA-EMBEDDED FRAGMENTS RISK EVALUATION

Match Criteria:

Dialog : VA-HF ACUTE ILLNESS

Dialog: VA-IRAQ &amp; AFGHANISTAN POST DEPLOYMENT SCREEN

Match Criteria:

Dialog : VA-HF ACUTE ILLNESS

Dialog: VA-PTSD SCREENING

Match Criteria:

Dialog : VA-HF ACUTE ILLNESS

Press ENTER to continue:

Deliver the report as a MailMan message? N//