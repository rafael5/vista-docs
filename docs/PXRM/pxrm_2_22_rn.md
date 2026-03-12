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
source_file: pxrm_2_22_rn.docx
status: draft
title: pxrm 2 22 rn.docx
---

<!-- image -->

**PXRM*2*22**

**OR*3*357**

## Clinical Reminders


## TERATOGENIC MEDICATIONS ORDER CHECKS

## Release Notes

**July 2012**

Product Development


Contents

Introduction	1

Pre-Installation Step:	2

Clinical Reminders PXRM*2*22 Documentation	2

Web Sites	2

Acronyms	3

National Acronym Directory:	3

Appendix A: Frequently Asked Questions (FAQ) about the Teratogenic Medications Order Check	4

Appendix B: Creating an Order Check	8

## Introduction

A teratogenic medication is one that can increase the risk of birth defects if taken at a particular time during pregnancy. In response to several requests, a CPRS Order Check was developed to remind providers when they prescribe a known or potential teratogen for a female patient of child-bearing potential. This reminder system is based on the FDA pregnancy categories (A, B, C, D, and X) and a set of additional criteria from First Data Bank that uses published literature and other available information. For lactating patients, the system also uses criteria to notify providers when a medication can cause serious side effects in a breastfeeding infant

This Teratogenic Medication Order Check project contains two patches, PXRM*2.0*22 and OR*3.0*357.


PXRM*2.0*22 releases two new National Reminder Order Checks for placing Teratogenic Medications. A pre-installation routine will identify any previously identified components and rename them correctly, and the patch installation will create or overwrite VA-named, national reminder components


This patch also addresses two bug fixes in the Reminder Order Check setup. To address these fixes, the Reminder Order Check System was divided into two files:

- File 801 Reminder Order Check Items Group

File 801 contains the grouping of Orderable Items. This file has also been modified to allow groups to include entries from the Drugs file, file #50, VA Generic file, file #50.6 and VA Drug Class file, file # 50.605.

- File 801.1 Reminder Order Check Rules.

File 801.1 contains the Reminder Order Check Rules.

These changes will allow sites to modify the Active and Testing Fields for National Rules.

OR*3.0 *357 contains changes to support the modifications to the Reminder Order

Check System release. To support these changes. ORKCHK5 has been updated to support the new API format for PXRMORCH. While testing this patch, a bug was found in the Order Check System, it was possible for the medium severity reminder order check to not show in CPRS if the order check system could not connect to First DataBank. ORCHECK, has been updated to fix this problem.

**Remedy Tickets fixed**

- 502067      Timeout error in clinical reminder order checks
- 536991      National reminder order checks don’t allow for proper active/testing flag management
- 599706      Usage setting not displaying for clinical reminder checks on reminder definition inquiries
- 603685      Reminder dialog elements set as disable and do not send, were getting changed to disable and send upon reminder exchange
- 606277      Error in loading reminder dialogs via reminder exchange; some IMM entries were not getting installed.
- 616620       Errors when $P was being used in a Function Finding.

To support the two-file structures, the existing menu options have been renamed and two new options are released with this patch:

- Reminder Order Check Rule Inquiry
- Reminder Order Check Test.

The method for creating and editing Reminder Order Checks has been modified to use ScreenMan forms. See the Reminders Manager’s Manual for further instructions.


### Pre-Installation Step:

- All existing reminder order checks will need to be rebuilt after installation of PXRM*2*22. We recommend that you print a copy of any existing Reminder Orderable Item Groups (File #801) on your system, using FileMan or Reminder Order Checks Inquiry. This will be used to help you re-create order checks after the install. See Appendix B in the Installation Guide for an example of using the Reminder Order Checks Inquiry to do this.


### Clinical Reminders PXRM*2*22 Documentation

| **Documentation**                   | **Documentation File name**              |
|-------------------------------------|------------------------------------------|
| Installation Guide                  | PXRM\_2\_22\_IG.PDF  PXRM\_2\_22\_IG.DOC |
| Clinical Reminders Manager’s Manual | PXRM\_2\_22\_MM.PDF  PXRM\_2\_22\_MM.DOC |
| Release Notes                       | PXRM\_2\_22\_RN.PDF  PXRM\_2\_22\_RN.DOC |

#### Web Sites

| **Site**                              | **URL**                                                                                                            | **Description**                                                                            |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| National Clinical Reminders site      | http://vista.med.va.gov/reminders                                                                                  | Contains manuals, PowerPoint presentations, and other information about Clinical Reminders |
| National Clinical Reminders Committee | [http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx](http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx) | This committee directs the development of new and revised national reminders               |
| VistA Document Library                | [http://www.va.gov/vdl/](http://www.va.gov/vdl/)                                                                   | Contains manuals for Clinical Reminders and CPRS (OR).                                     |

## Acronyms

The OIT Master Glossary is available at: [http://vaww.oed.wss.va.gov/process/Library/master\_glossary/masterglossary.htm](http://vaww.oed.wss.va.gov/process/Library/master_glossary/masterglossary.htm)


#### National Acronym Directory:

[http://vaww1.va.gov/Acronyms/](http://vaww1.va.gov/Acronyms/)

| Term    | Definition                                                     |
|---------|----------------------------------------------------------------|
| ASU     | Authorization/Subscription Utility                             |
| CPRS    | Computerized Patient Record System                             |
| ESM     | Enterprise Systems Management (ESM)                            |
| FIM     | Functional Independence Measure                                |
| GUI     | Graphical User Interface                                       |
| IAB     | Initial Assessment & Briefing                                  |
| MH      | Mental Health                                                  |
| MHA3    | Mental Health Assistant Version 3                              |
| MHV     | My Healthy Vet                                                 |
| MST     | Military Sexual Trauma                                         |
| OIT     | Office of Information and Technology                           |
| OIF/OEF | Operation Iraqi Freedom/Operation Enduring Freedom             |
| OR      | Order Entry namespace                                          |
| PCS     | Patient Care Services                                          |
| PD      | Product Development                                            |
| PTSD    | Post Traumatic Stress Syndrome                                 |
| PXRM    | Clinical Reminder Package namespace                            |
| RSD     | Requirements Specification Document                            |
| TIU     | Text Integration Utility                                       |
| VA      | Department of Veteran Affairs                                  |
| VHA     | Veterans Health Administration                                 |
| VistA   | Veterans Health Information System and Technology Architecture |
| WV      | Women’s Health package namespace                               |
| YS      | Mental Health package namespace                                |


## Appendix A: Frequently Asked Questions (FAQ) about the Teratogenic Medications Order Check

**Q: What is a “teratogenic” medication?**

**A:** A teratogenic medication is one that can increase the risk of birth defects if taken at a particular time during pregnancy. A **known teratogen** is a medication that causes birth defects in humans. Examples include thalidomide (limb defects), isotretinoin (syndrome of defects including oral clefts), valproic acid (neural tube defects), and mycophenolate (facial clefts, anotia).  A **potential teratogen** is a medication that causes   malformations or other abnormal pregnancy outcomes in animal studies – these outcomes are more concerning if they occur at doses similar to human doses. Some medications increase the risk for pregnancy loss (miscarriage), growth abnormalities (e.g., growth restriction), or functional deficits (e.g., decreased fetal kidney function).  These are also important adverse reproductive effects.

**Q: What is the new Teratogenic Medication Order Check?**

**A:** In response to several requests, a CPRS Order Check was developed to remind providers when they prescribe a known or potential teratogen for a female patient of child-bearing potential. This reminder system is based on the FDA pregnancy categories (A, B, C, D, and X) and a set of additional criteria from First Data Bank that uses published literature and other available information.  For lactating patients, the system also uses criteria to notify providers when a medication can cause serious side effects in a breastfeeding infant

**Q: What are the FDA pregnancy categories?**

**A:** The FDA categories are a helpful system for distinguishing the relative teratogenic risk of a medicine based on studies in animals and experience in human pregnancy. As a health care provider, your awareness of these issues can help you better prescribe for and counsel your female patients of child-bearing potential. See the following table for category descriptions.

**Q: How will the Teratogenic Medication Order Check work?**

**A:** When a provider prescribes a medication with a pregnancy category D or X for a female patient between the ages of 18 and 50, the system will automatically provide an order check to ensure that you are aware of the reproductive risk associated with the medication. Certain additional medications with evidence of concern (e.g., some category C medications or FDA-unclassified medications) will also trigger an alert.

**Q: What do you do if you get an Order Check?**

**A:** (1) Consider whether this medication is most appropriate for the patient’s condition or whether there are other appropriate options with less reproductive risk.

(2) Counsel the patient about the risks and benefits of treatment should pregnancy occur.

(3) Ask the patient about pregnancy planning and use of contraception. This risk/benefit discussion is an important one.

(4) For breastfeeding patients, consider whether there is an alternative medication with lower concentrations in breast milk or fewer risks for the infant and encourage the patient to discuss her medications with the infant’s pediatrician.  LactMed ( [http://toxnet.nlm.nih.gov/cgi-bin/sis/htmlgen?LACT](http://toxnet.nlm.nih.gov/cgi-bin/sis/htmlgen?LACT) ) is an online resource from the NIH that provides available information about use of medications during lactation.

Q: **Where can I get information about the pros/cons of continuing use of a teratogenic medication during pregnancy?**

**A:** Deciding whether to continue a potential or known teratogen during pregnancy is complicated.  Not treating or under-treating a pregnant woman’s medical condition can be riskier to the fetus than the medication itself.  It is helpful to read the pregnancy subsection of drug labeling, which provides information about the reproductive risks of medications.  Current labeling can be found at Drugs@FDA or at [www.DailyMed.nlm.nih.gov](http://www.dailymed.nlm.nih.gov/) .  Reprotox is an online resource that summarizes available information about the reproductive risks of medications.  Reprotox may be available online through your facility’s library and will be available through the VACO library in the near future.  The Organization of Teratology Information Services has fact sheets available online about medications and their risks during pregnancy ( [http://www.otispregnancy.org/otis-fact-sheets-s13037#1](http://www.otispregnancy.org/otis-fact-sheets-s13037) ).  Your local pharmacist and women’s health providers can provide more information.

**Q: How can I help my patients avoid unintended pregnancy?**

**A:** About 50% of pregnancies in the United States are unplanned. During patient encounters, ask women of child-bearing potential (age 15 to 50) about their plans for pregnancy and need for contraception.

The most effective reversible contraceptives are the IUDs (Mirena or Paragard) and subdermal implants (Nexplanon, previously Implanon). These contraceptives are available through the VA prosthetics department and can be inserted by a local trained women’s health provider. Oral contraceptive pills and emergency contraception are on the VA formulary, and condoms are available through the VA. Female Veterans using contraceptives other than IUDs and implants should be advised to keep a supply of emergency contraception on hand in case of unprotected intercourse or contraceptive failure.

**Q: When will the Order Check be available?**

**A:** The Order Check will come as a VistA Clinical Reminders patch, PXRM*2*22.  At the time of this message, release is anticipated during the fourth quarter of calendar year 2012.

**Q: How often will this Order Check appear?**

A: Clinicians will be notified every time any category D or X medications or certain other medications with evidence for concern (e.g., some category C medications or FDA-unclassified medications) are ordered for a female patient of child-bearing potential who is without documentation of medical inability to become pregnant.

**Q: Will the Order Check display even if the patient has no chance of becoming pregnant, such as post-hysterectomy?**

**A:** No. The Order Check is designed to recognize several exclusion criteria that can be generally described as “medical inability to conceive.”  For example, patients for whom the appropriate ICD-9 a code for hysterectomy is recorded will not trigger an alert.  Other ICD-9 a exclusion criteria include menopausal state and IUD use.

**Q: Can clinicians add information to the electronic health record that should exclude a patient from this Order Check?**

**A:** Yes, each site can define additional situations or “Health Factors” when the Order Check does not apply. The local application support team can add these Health Factors to the Reminder Term called “VA-TERATOGENIC MEDICATIONS ORDER CHECK EXCLUSIONS (TERM).”  The support team can also suggest to the Women’s Health Program Office that a Health Factor be added as part of a subsequent national update.

**Points of Contact for further information about the Teratogenic Medications Order Check:**

- Your facility’s pharmacy informaticist (ADPAC)
- Your facility’s clinical reminders manager (often one of the Clinical Application Coordinators)
- REDACTEDat Pharmacy Benefits Management (REDACTED)
- REDACTED, Director Reproductive Health, Women Veterans Health Strategic Healthcare Group, (REDACTED )

a At the time of this message, the transition from ICD-9 to ICD-10 has not yet taken place

FDA Pregnancy categories

| **Table 1.   FDA Pregnancy categories**  **(language summarized from 21CFR201.57)**   |                                                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Category**                                                                          | **Definition**                                                                                                                                                                                                                                                                                                                                                                                                        |
| **A**                                                                                 | Adequate and well-controlled (AWC) studies in pregnant women have failed to demonstrate a risk to the fetus in the first trimester of pregnancy (and there is no evidence of a risk in later trimesters).                                                                                                                                                                                                             |
| **B**                                                                                 | Animal reproduction studies have failed to demonstrate a risk to the fetus and there are no AWC studies in pregnant women, OR animal studies demonstrate a risk and AWC studies in pregnant women have not during the first trimester (and there is no evidence of risk in later trimesters).                                                                                                                         |
| **C**                                                                                 | Animal reproduction studies have shown an adverse effect on the fetus, there are no AWC studies in humans, AND the benefits from the use of the drug in pregnant women may be acceptable despite its potential risks. OR animal studies have not been conducted and there are no AWC studies in humans.                                                                                                               |
| **D**                                                                                 | There is positive evidence of human fetal risk based on adverse reaction data from investigational or marketing experience or studies in humans, BUT the potential benefits from the use of the drug in pregnant women may be acceptable despite its potential risks (for example, if the drug is needed in a life-threatening situation or serious disease for which safer drugs cannot be used or are ineffective). |
| **X**                                                                                 | Studies in animals or humans have demonstrated fetal abnormalities OR there is positive evidence of fetal risk based on adverse reaction reports from investigational or marketing experience, or both, AND the risk of the use of the drug in a pregnant woman clearly outweighs any possible benefit (for example, safer drugs or other forms of therapy are available).                                            |

The FDA published a proposed rule in the May 29, 2008, Federal Register that proposes new labeling regulations for prescription drugs. These regulations, once implemented, will eliminate the pregnancy categories from drug labeling. When a final rule publishes, VHA will determine how to best update this order check process so that it will remain both current and useful to VA providers.

## Appendix B: Creating an Order Check

**ScreenMan Overview**

The redesigned Reminder Order Check functionality uses ScreenMan. ScreenMan is VA FileMan's *screen-oriented* data entry tool. It is an alternative to the scrolling mode approach. With ScreenMan, data is entered in *forms* . Each form field occupies a fixed position on the screen (instead of scrolling off!). You can see many data fields at once, and use simple key combinations to edit data and move from field to field on a screen. You can also move from one screen to another like turning through the pages of a book. For a detailed explanation of using ScreenMan, please refer to the VA FileMan Getting Started manual.

**The ScreenMan Screen**

<!-- image -->

**ScreenMan Descriptions**

Required fields are underlined

<!-- image -->

Current field – reverse video

<!-- image -->

<!-- image -->

<!-- image -->

RULE NAME : DABIGATRAN AND RENAL FUNCTION-2

DISPLAY NAME : **DABIGATRAN AND RENAL FUNCTION**

STATUS : **PROD**

SEVERITY : **MEDIUM**

Active Duty

<!-- image -->

TERM:

Reminder Term: Active Duty

Term Evaluation Status: **True**

<!-- image -->

<!-- image -->

ORDER CHECK TEXT: The dose of dabigatran should be reduced to 75mg PO BID wh ...

RULE DESCRIPTION:

CLASS : **LOCAL**

SPONSOR:

REVIEW DATE:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

<!-- image -->

Initial Multiple field

<!-- image -->

Command line: You can enter Exit, Save,  Close,

Next Page, and Refresh here.

Pop-up subpage where you can edit the selected entry in the multiple.

<!-- image -->

Fields are usually composed of a *data element* and a *caption* . ScreenMan displays data elements in high intensity (boldface) and other text in regular intensity. Text that identifies a data element is called a *caption* and is usually followed by a colon ( **:** ). A caption and its associated data element are together called a *field* . Captions of *required* fields are underlined; to save any changes you make on the form, required fields *must* contain data.

**How to Navigate Between Fields and Pages**

There are a number of ways you can move the cursor from field to field on a form (i.e., navigate). This is to provide you with as much flexibility as possible so that you can work quickly and efficiently with forms.

You can use the keystrokes listed in the following table to move the cursor to various fields located on a ScreenMan form:

| **To**                                                   | **Press**                                                  |
|----------------------------------------------------------|------------------------------------------------------------|
| Move to the next field (to right or below).              | **&lt;Tab&gt;**                                            |
| Move to the previous field (to left or above).           | **&lt;PF4&gt;**                                            |
| Move to the field above.                                 | **&lt;ArrowUp&gt;**                                        |
| Move to the field below.                                 | **&lt;ArrowDown&gt;**                                      |
| Move to the next field in the pre-defined edit sequence. | **&lt;Enter&gt;**                                          |
| Edit a WORD-PROCESSING field.                            | At field, press  **&lt;Enter&gt;**                         |
| Select a Subrecord in a Multiple.                        | At field, press  **&lt;Enter&gt;**                         |
| Move to the next block on current page.                  | **&lt;PF1&gt;&lt;PF4&gt;**                                 |
| Jump to a specific field.                                | **^**  followed by Caption of field and  **&lt;Enter&gt;** |
| Jump to the Command Line.                                | **^&lt;Enter&gt;**                                         |
| Move to next page                                        | **&lt;PF1&gt;&lt;ArrowDown&gt;**  or  **&lt;PageDown&gt;** |
| Move to previous page                                    | **&lt;PF1&gt;&lt;ArrowUp&gt;**  or  **&lt;PageUp&gt;**     |
| Move to a page you specify                               | **&lt;PF1&gt;P**                                           |

**Saving and Exiting**

To SAVE or EXIT the form, you need to reach ScreenMan's command line. It's reachable from any ScreenMan screen. To reach the command line, do any one of the following:

1. Enter a caret ("^") at any field prompt.
2. Press **&lt;Enter&gt;** , **&lt;Tab&gt;** , or **&lt;PF4&gt;** to move from field to field until you reach the command line.
3. Press **&lt;ArrowDown&gt;** or **&lt;ArrowUp&gt;** to move the cursor from field to field downwards or upwards, until you reach the command line.

Then you can enter SAVE or EXIT at the command line (see below).

**Word-Processing Fields**

To edit or display a WORD-PROCESSING field, press the Enter/Return key at the WORD-PROCESSING field. This clears the screen and passes control to your Preferred Editor to edit the field. If you do not have a Preferred Editor, the Screen Editor is used. When you exit the editor, you return to the ScreenMan screen.

**Multiples Linked to "Pop-Up" Subpages**

A Multiple field can appear on a page and be linked to a regular or "pop-up" subpage. When you navigate to the Multiple field, select a Subrecord, and press the Enter/Return key, you are taken to the subpage, which contains the fields within the Multiple.

In the following illustration, the Multiple is the field with the caption "Select EMPLOYMENT HISTORY:". When you enter "FEB 1,1950" at this field, you are taken into a "pop-up" subpage, where you can edit the fields for that particular Subrecord:

###### Exiting a Subpage

While in a subpage, your only Command Line options are CLOSE and REFRESH. You cannot EXIT, Quit, or SAVE until you return to the parent page. You can return to the parent page by pressing **&lt;PF1&gt;C** or issuing the CLOSE command at the Command Line. From there, you can select another Subrecord to edit or navigate to another field.

##### Order Check Example

**Purpose** : Design an Order Check for dabigatran (Pradaxa®) to remind providers about dose reduction when creatinine clearance is less than 30 mL/min

This example uses serum creatinine values greater than 2 mg/dL to focus more on the order check than on the lab result

1. **Create a reminder term that will identify patients with reduced renal clearance. (Patients with Cr &gt; 2 mg/dL)**

Select Reminder Term Management Option: **TE** Add/Edit Reminder Term

Select Reminder Term: **ZZ CREATININE &gt; 2 (TERM)**

Are you adding 'ZZ CREATININE &gt; 2 (TERM)' as

a new REMINDER TERM (the 1215TH)? No// **Y** (Yes)

REMINDER TERM CLASS: **L** LOCAL

NAME: ZZ CREATININE &gt; 2 (TERM)  Replace

CLASS: LOCAL//

Reminder Term has no findings!

Select Finding: **LT. CREATININE**

Are you adding ' CREATININE' as a new FINDINGS (the 1ST for this REMINDER TERM)? No// **Y** (Yes)

Editing Finding Number: 1

FINDING ITEM:  CREATININE//

CONDITION: **I V&gt;2**

1. **Create a reminder order check rule that calls the reminder term created in step 1 when its status is TRUE.  The rule also contains the text that will appear in the order check window.**

- Each RULE exists as a part of the OI Group
- That allows you to set up multiple rules that apply to the same list of drugs

Select Reminder Managers Menu Option: **ROC** Reminder Order Check Menu

Select Reminder Order Check Menu Option: **RE** Add/Edit Reminder Order Check Rule

Select Reminder Order Check Items Group by one of the following:

N:  ORDER CHECK ITEMS GROUP NAME

C:  VA DRUG CLASS

D:  DRUG

G:  VA GENERIC

O:  ORDERABLE ITEM

R:  ORDER CHECK RULE

Q:  QUIT

Select Reminder Order Check Items Group by:  (N/C/D/G/O/R/Q): N// **R** ORDER CHECK RULE

Select REMINDER ORDER CHECK RULES RULE NAME: **DABIGATRAN AND RENAL FUNCTION**

Are you adding 'DABIGATRAN AND RENAL FUNCTION' as

a new REMINDER ORDER CHECK RULES (the 4TH)? No// **Y** (Yes)

RULE NAME: DABIGATRAN AND RENAL FUNCTION

DISPLAY NAME : **DABIGATRAN AND RENAL FUNCTION**

ACTIVE FLAG : **YES**

TESTING FLAG : **YES**

SEVERITY : **MEDIUM**

TERM : **&lt;Enter&gt;**

**When you press Enter after Term:, a box pops up and prompts you for the Term name and Term Evaluation Status.**

REMINDER TERM: ZZ CREATININE &gt; 2 (TERM)

TERM EVALUATION STATUS: **TRUE** .

**Either a Term or a Definition must be defined; if you don’t enter a Term, the prompt appears for DEFINITION.**

DEFINITION **&lt;Enter&gt;**

REMINDER DEFINITION:                                                     DEFINITION EVALUATION STATUS:                                            OUTPUT TEXT:

**When you press Enter after Term:, a box pops up and prompts you for the Term name**

ORDER CHECK TEXT:

**Order Check Text and Rule Description are word-processing fields. When you press Enter, a word-processing screen opens up.**

==[ WRAP ]==[ INSERT ]======&lt; ORDER CHECK TEXT &gt;========[ &lt;PF1&gt;H=Help ]

**The dose of dabigatran should be reduced to 75mg PO BID when the**

**patient's creatinine clearance is estimated to be less than**

30 mL/min.

&lt;=====T=======T====T======T=======T=======T=======T=======T=======T&gt;===

RULE DESCRIPTION: &lt;Enter&gt;

RULE NAME : **DABIGATRAN AND RENAL FUNCTION**

DISPLAY NAME : **DABIGATRAN AND RENAL FUNCTION**

ACTIVE FLAG : **YES**

TESTING FLAG : **YES**

SEVERITY : **MEDIUM**

TERM: ZZ **CREATININE &gt; 2 (TERM)**

TERM EVALUATION STATUS: TRUE

ORDER CHECK TEXT: The dose of dabigatran should be reduced to 75mg PO BID wh ...

RULE DESCRIPTION:

CLASS : **LOCAL**

**SPONSOR:**

**REVIEW DATE:**

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit     Save     Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND:                              Press &lt;PF1&gt;H for help    Insert

1. **Create an Order Check Item Group**

Similar ScreenMan actions and word-processing fields shown in the example above apply in this option.

Select Reminder Managers Menu Option: ROC  Reminder Order Check Menu

Select Reminder Order Check Menu Option: GE  Add/Edit

Reminder Order Check Items Group

Select reminder order check items group by:  (N/C/D/G/O/R/Q): N// &lt;Enter&gt;

ORDER CHECK ITEM GROUP NAME

Reminder Order Check Item Group: DABIGATRAN AND RENAL FUNCTION

Are you adding 'DABIGATRAN RENAL FUNCTION' as

a new REMINDER ORDER CHECK ITEMS GROUP (the 4TH)? No// Y  (Yes)

--PHARMACY ITEM--------------------------------------------------------

. DR.DABIGATRAN ETEXILATE 150MG ORAL CAP               Word-

processing field                 .

-----------------------------------------------------------------------

Word-processing

field

--REMINDER ORDER CHECK RULE--------------------------------------------

. DABIGATRAN AND RENAL FUNCTION                                           .

-----------------------------------------------------------------------

GROUP NAME: DABIGATRAN

PHARMACY ITEM LIST (0 entry)

ORDERABLE ITEM LIST (0 entries)

REMINDER ORDER CHECKS RULES LIST (1 entry)

CLASS: LOCAL

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Select reminder order check items group by:  (N/C/D/G/O/R/Q): N// QUIT

1. **Connect the rule to the order check item group using the Add/Edit Reminder Order Check Items Group option.**

1. **In CPRS, turn off the Clinical Reminders Live Order Check.**

<!-- image -->

- Set the rule’s testing flag to True.
- Set the group’s Active Flag to True.
- Run the Reminder Order Check Test option to validate that the active rule shows for each patient.
- In CPRS, place a corresponding order for the order group for each test patient.
    - Validate that only the active rule shows in the order check form.
**Result**
<!-- image -->

<!-- image -->