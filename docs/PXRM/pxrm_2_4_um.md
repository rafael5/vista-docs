---
app_name: 'Registry: Airborne Hazard Open Burn Pit (AHOBPR) (PXRM)'
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: null
doc_type: user-manual
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
source_file: pxrm_2_4_um.docx
status: draft
title: "Patients with Reminder Applicable\tDue"
---

<!-- image -->

**Clinical Reminders**

**Version 2.0 Patch PXRM*2*4**

**CLINICIAN GUIDE**

**October 2006**

V *ist* A HSD&amp;D Department of Veterans Affairs

**Revision History**

NOTE: Changes throughout the manual made for patch 4 are highlighted in blue.

| **Date**     | **Page #**                           | **Description**                                              | **Project Manager**   | **Technical Writer**   |
|--------------|--------------------------------------|--------------------------------------------------------------|-----------------------|------------------------|
| May- July 06 | Throughout                           | Edits per development updates                                | REDACTED              | REDACTED               |
| Apr 06       | Appendix D                           | Added descriptions and examples of GEC Referral  Reports     | REDACTED              | REDACTED               |
| Apr 06       | throughout                           | Edits per SQA review                                         | REDACTED              | REDACTED               |
| Feb 2006     | 39                                   | Changes to Reminder Reports made in PXRM*2.0*4               | REDACTED              | REDACTED               |
| Feb 2006     | 115                                  | Added appendix about OEF/OIF reminder released in PXRM*2.0*5 | REDACTED              | REDACTED               |
| Feb  2006    | 74                                   | Added FAQs                                                   | REDACTED              | REDACTED               |
| Sept 2005    | 5                                    | Changes to GEC Referral, made in PXRM*2.0*4                  | REDACTED              | REDACTED               |
| Sept 2005    | Appendix D: VA GEC  Referral Reports | Changes to GEC Reports (new option), made in PXRM*2.0*4      | REDACTED              | REDACTED               |

**Table of Contents**

Clinical Reminders V. 2.0 and This Guide	1

**Table of Contents**

Purpose of This Guide	1

Our Target Audience	1

Related Documentation	1

Introduction	2

Benefits of Clinical Reminders	2

Clinical Practice Guidelines	2

Functionality in Version 2	5

Set-up of Clinical Reminders.	6

1. Using Clinical Reminders	7

Chapter 1: Clinical Reminders and CPRS Overview	7

Chapter 2: Resolving Clinical Reminders	15

Chapter 3: Resolving IHD Reminders	19

Chapter 4: Processing Mental Health Reminders	30

Chapter 5: Using Reminder Reports	37

Chapter 6: Health Summaries and Clinical Reminders	42

Health Summary on Reports Tab in CPRS	43

My HealtheVet Health Summary	44

Chapter 7: VA-Geriatric Extended Care (GEC) Referral	47

Chapter 8: Code Set Versioning (CSV) Changes in Reminders	68

Chapter 9: My HealtheVet Changes in Reminders.	69

Chapter 10: CPRS: Integration with Women’s Health	70

Appendix A: FAQS, Hints, and Tips	74

Appendix B: Glossary	77

Appendix C: Edit Cover Sheet Reminder List.	80

Appendix D: VA GEC Referral Reports	83

Appendix E: Iraq &amp; Afghan Post-Deployment Screen	115

Index	126

| **Purpose of This Guide**        | This Clinician Guide is designed to help the clinical practitioner understand Clinical Reminders V. 2.0, and to use the functionality to improve patient care and clinical processes. This guide will also give you an overview of the following national VA reminders/dialogs and components:  VA-Ischemic Heart Disease VA-Mental Health  VA-GEC Referral  VA-Women’s Health/CPRS Integration MyHealtheVet Reminders  OEF/OIF Reminder  **Target Audience**  We have developed this guide for the following types of users:  - Clinicians - Nurses - Clinical Application Coordinators (CAC) - Clinical Reminders Managers   |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Other Sources of Information** | **Related Documentation**  The following manuals are available from the VistA Documentation Library (VDL)  [http://www.va.gov/vdl](http://www.va.gov/vdl)  .  - Clinical Reminders Patch 4 Release Notes (PXRM\_2\_4\_RN.PDF) - Clinical Reminders Technical Manual (PXRM\_2\_4\_TM.PDF) - Clinical Reminders Manager Manual (PXRM\_2\_4\_MM.PDF) - Clinical Reminders V2.0 Setup Guide (PXRM\_2\_SG.PDF)  Other relevant information is also available on the Clinical Reminders website:  [http://vista.med.va.gov/reminders](http://vista.med.va.gov/reminders)  [/](http://vista.med.va.gov/reminders)                     |

| **Benefits of Clinical Reminders**  From Harvard Innovations award:  *The involvement of front-line providers, use of performance measures and universal use of electronic health records have enabled VA to set the national benchmark in quality of care. VistA's computerized system enables key decisions by checking links to automated drug distribution, leading to a significant reduction in the error rate.*  *VistA is innovative because of its unique linkage with standardized, consistent performance measurement.*  *VA's electronic health records provide patient- specific, comprehensive clinical decision support that results in a performance measurement system that encourages driven evidence- based practice.*   | **Clinical Reminders Overview**  The Clinical Reminder system helps caregivers deliver higher quality care to patients for both preventive health care and management of chronic conditions, and helps ensure that timely clinical interventions are initiated.  Reminders assist clinical decision-making and also improve documentation and follow-up, by allowing providers to easily view when certain tests or evaluations were performed and to track and document when care has been delivered. They can direct providers to perform certain tests or other evaluations that will enhance the quality of care for specific conditions. The clinicians can then respond to the reminders by placing relevant orders or recording clinical activities on patients’ progress notes.  Clinical Reminders may be used for both clinical and administrative purposes. However, the primary goal is to provide relevant information to providers at the point of care, for improving care for veterans. The package benefits clinicians by providing pertinent data for clinical decision-making, reducing duplicate documenting activities, assisting in targeting patients with particular diagnoses and procedures or site- defined criteria, and assisting in compliance with VHA performance measures and with Health Promotion and Disease Prevention guidelines.  **Clinical Practice Guidelines**  The Veterans Health Administration (VHA), in collaboration with the Department of Defense (DoD) and other leading professional organizations, has been developing clinical practice guidelines since the early 1990s. Guidelines for the Rehabilitation of Stroke and Amputation and the Care Guide for Ischemic Heart Disease were among the first distributed throughout VHA in 1996 and 1997. Since that time, numerous other guidelines, including guidelines on Diabetes Mellitus, COPD, Major Depressive Disorder, Psychoses, Tobacco Use Cessation, Hypertension, have been developed and distributed for implementation throughout the system.  VHA defines clinical practice guidelines as recommendations for the performance or exclusion of specific procedures or services for specific disease entities. These recommendations are derived through a rigorous methodological approach that includes a systematic review of the evidence to outline recommended practice. Clinical guidelines are seen by many as a potential solution to inefficiency and inappropriate variation in care.   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Benefits of Clinical Reminders**   | **Clinical Practice Guidelines**  **Purpose of Guidelines**  - Assure that the appropriate amount of care is provided (addressing both under &amp; over-utilization) - Reduce errors and promote patient safety - Ensure predictable and consistent quality - Promote learning and research - Facilitate patient and family education  **National Clinical Practice Guidelines Council (CPGC)**  Veterans Health Administration (VHA) Directive 2002-007 established the National Clinical Practice Guideline Council (NCPGC) to coordinate the adoption, implementation, and evaluation of clinical practice guidelines throughout the system.  The Council functions to:  - Prioritize clinical areas for which guidelines need to be developed or adapted/adopted - Oversee and participate in guideline development and/or adaptation - Assure maintenance and timely revision of existing guidelines - Collaborate with DOD regarding the use of guideline development to improve the quality of care and health management across VHA and the Military Health System - Facilitate implementation of guidelines by coordinating dissemination, consulting on studies, promoting education, and identifying and eliminating barriers to guideline implementation   |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Benefits of Clinical Reminders**   | **Clinical Reminders, Performance Measures, and Clinical Practice Guidelines**  Each Veterans Integrated Service Networks (VISN) must comply with performance measures that address Prevention Index/Chronic Disease Index (PI/CDI), as well as with the Health Promotion And Disease Prevention Program Handbook 1120.2, which states that each VHA facility shall have a program to educate veterans with respect to health promotion and disease prevention and to provide veterans with preventive medical care that includes screening and other clinical services.  The Clinical Reminders package offers tools to help clinicians comply with these performance measures and guidelines on a patient-by-patient basis. The use of these tools leads to improved patient care.  Providers can work with their local Clinical Application Coordinators to set up customized reminders based on local and national guidelines for patient education, immunizations, skin tests, measurements, exams, laboratory tests, mental health tests, radiology procedures, and other procedures.  For further information, see the PowerPoint presentation, “Implementing a Clinical Guideline Using Clinical Reminders,” available on the national Clinical Reminders web page  [http://vista.med.va.gov/reminders](http://vista.med.va.gov/reminders)  /  The Office of Quality and Performance oversees the VA’s performance measure plan. Each year the  [Performance Measurement Workgroup](http://vaww.oqp.med.va.gov/committees/pmwg/pmwg.asp)  (PMWG), recommends the annual Network Performance Plan to the Under Secretary for Health. The Plan is formally signed as the Network Director's annual performance appraisal. The specific details of the plan are published annually on the OQP website.  [http://vaww.oqp.med.va.gov/default.htm](http://vaww.oqp.med.va.gov/default.htm)   |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Benefits of Clinical Reminders**   | **Functionality in Version 2**  Clinical Reminders V. 2.0 supports Phase II of the Ischemic Heart Disease (IHD) and Mental Health QUERI projects. It adds four  *new*  IHD reminder definitions, two  *modified*  reminder definitions, modified reminder dialogs, reminder taxonomies, reminder terms, and health factors.  It also redistributes three Mental Health (MH) reminder definitions, along with the reminder dialogs, reminder taxonomies, and reminder terms, and health factors to support Phase II of the MH project.  Also included in version 2:  - Functionality for VA-GEC Referral (Geriatric Extended Care) - New Health Summary Reminders components and types to support MyHealtheVet - New Reminders and dialogs to support the CPRS: Integration with Women’s Health project - Corrections for problems reported in National Online Information Sharing (NOIS) and Remedy - Improved reminder evaluation functionality  Most of the changes in Version 2.0 of Clinical Reminders are technical and behind-the-scenes, affecting reminder definition and set-up. For further information, see your Clinical Applications Coordinator (CAC) or the Clinical Reminders website:  [http://vista.med.va/gov/reminders/](http://vista.med.va/gov/reminders/)  **Changes in Clinical Reminders Patch 4**  Most of the changes in Patch 4 are also technical and behind-the- scenes. Following are a few changes that clinicians might notice:  - If a frequency can’t be determined for a patient, the Status and Due Date will both be CNBD and the frequency display that follows the status line will be “Frequency: Cannot be determined for this patient.” - A new option, Restore or Merge Referrals, on the GEC reports menu gives the sites the ability to open a closed referral, merge two referrals, or close an open referral. - Normally when a patient is deceased, the status of the reminder is automatically set to “N/A.” A new flag was added that can be used to override this behavior and cause the status to be determined as usual. This change was made so that if the “Include dead patients” prompt on a Reminder Due Report was answered as “yes,” normal evaluation could be done.   |
|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Setup of Clinical Reminders**   | **Clinician Role in Setting up Reminders**  Clinicians play a role in the setup of reminders in the following ways:  1. Defining clinical reminder definitions and using them within Health Summaries, the CPRS GUI, and on encounter forms. Clinicians will be asked to assist Clinical Application Coordinators in selecting which reminders to implement and in defining the clinical aspects of the Clinical Reminder definitions, including:  - Defining Baseline Age Range Set(s) - Defining findings that identify whether the reminder applies to the patient, resolve (satisfy) the reminder, or provide additional clinical information-only from the following finding types:  - Reminder Frequency - Minimum and Maximum Age  - Health Factors, Immunizations, Skin Tests, Education Topics, Exams - Taxonomies (ICD Diagnosis, ICD0 Operation/Procedure, CPT Procedure ranges) - Lab Tests and Radiology Procedures - Local Drugs, Generic Drugs and Drug Classes - Vital Signs - Orders to place - Computed Findings to handle miscellaneous findings (such as veteran status, BMI, race and ethnicity).  1. Defining and using dialogs to resolve reminders. Within CPRS GUI, the clinician uses a point-and-click interface (dialog) for each reminder chosen to process. As you select check-boxed text indicating actions you performed at a given encounter, text is accumulated to add to the note in progress. When you have finished processing the reminders, encounter information is entered in PCE, orders are placed, vital signs are updated, and mental health tests are scored and stored in the Mental Health package, according to your selections. You can help your clinical coordinators define a list of possible actions related to the reminder, to create the appropriate dialog check-boxes for each reminder.  1. The clinician plays a major role by advising when encounter forms are a clinically appropriate method of entry of health factors, education topics, immunizations and skin tests into Patient Care Encounter (PCE) to satisfy the clinical reminders. In many clinical settings reminder dialogs offer the advantage of not only passing the information to PCE but also of clinical documentation in progress note text where it is easily available for other users.   |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 1: Clinical Reminders and CPRS Overview**  **The cover sheet display of reminders can be customized for Site, System, Location, or User.**   | **Using Clinical Reminders in CPRS**  Clinician reminders display in CPRS in four places:  - Cover Sheet - Clock button (upper right-hand corner of each tab in CPRS) - Notes tab - Reports tab (Health Summaries)  **Cover Sheet**  Clinical reminders are displayed on the cover sheet of CPRS. When you left-click on a reminder, details are presented in a pop-up window. By right-clicking on a reminder on the cover sheet, you can access the reminder definition and reference information.  More details about what’s available from the Cover Sheet are provided in the following pages.   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Cover Sheet Reminders Box**

| **Chapter 1: CPRS and Reminders Overview**   | If you left-click on a particular reminder you will see the Clinical Maintenance output, which gives you the details of the reminder evaluation. It tells you things such as why the reminder is due for your patient and what the reminder requires.  The Clinical Maintenance display has been expanded to include more details, such as relevant Reminder Terms and Health Factors.   |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

| **Chapter 1: Clinical Reminders and CPRS Overview**   | If you right-click on a reminder, you will bring up a popup menu that looks like this:  <!-- image -->  Clicking on Clinical Maintenance will give you the same Clinical Maintenance output you get by left-clicking.  If the reminder contains education topics, Education Topic Definition will be selectable and clicking on it will display the education topic definitions.  <!-- image -->   |
|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 1: CPRS and Reminders Overview**   | Clicking on reminder inquiry will produce a display of the reminder definition. For detailed information on how reminders are defined, see the Clinical Reminders Manager’s Manual.  <!-- image -->  If you click on Reference Information, you will get a list of web sites that have information related to the clinical reminder. Clicking on one of them will open your web browser at that site.  Clicking on Reminder Icon Legend will bring up a display that shows what the various reminder icons mean.   |
|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### Reminders Icon Legend

<!-- image -->

| **Chapter 1: CPRS and Reminders Overview**  **You or your site can determine the folder view, and whether the folders are open or closed when you first open the reminders drawer.**  **The contents of the tree can be determined by the user. Details of how this is done are found in**  **Appendix C**  **.**  **Using a dialog to resolve a clinical reminder is discussed in Chapter 2.**   | The next place you are likely to encounter Clinical Reminders is on the Notes tab. When you go to the Notes tab and open a new note, a Reminders tab—called a drawer—appears.  Reminders Drawer  When you click on the Reminders drawer, a list of reminders is displayed.  <!-- image -->  Reminders that have an associated dialog have a special icon (see the above display of reminder icons). If you click on one of these reminders, a dialog box appears, which lists possible actions or activities that may satisfy this reminder.   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 1: CPRS and Reminders Overview**   | Users have the ability to edit their own list of cover sheet reminders. (Before you do this we recommend that you check with your Reminder Manager to find out which reminders are recommended for your work area.) Click on the Tools menu then click on Options.  Clicking on Clinical Reminders will open one of two cover sheet editing forms. CPRS will automatically determine which form is appropriate for you to use. See  Appendix C  , for instructions on how to edit cover sheet reminders.  **Clock Button**  Another place you can interact with Clinical Reminders is by clicking on the reminders button (it looks like an alarm clock) in the upper right hand corner of the CPRS GUI.  <!-- image -->  This brings up the Available Reminders form which provides the same tree view you saw in the reminders drawer.   |
|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 1: CPRS and Reminders Overview**   |    | **Available Reminders form**  This form has two menus: View and Action.  **View Menu**  The View menu lets you determine which categories of reminders will be displayed in the tree view. Those with a checkmark to the left of this will be displayed. You can toggle the checkmark on or off by left clicking on the icon. Note: as soon as you click on an icon the View menu will disappear and the tree will be updated to match your current selection. To make another change, left-click on View.  As was mentioned earlier, the tree you see here is identical to the one you see in the Reminders drawer, so whatever change you make here affects the tree you see in the Reminders drawer.  Of primary interest to the clinician are the options on the Action menu that let you evaluate reminders.  **Action Menu**  <!-- image -->   |
|----------------------------------------------|----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 1: CPRS and Reminders Overview**   | **Available Reminders form**  **Action Menu Evaluate Reminders**  You can evaluate an individual reminder, all the reminders in a category, or a processed reminder. A processed reminder is one whose dialog has been processed. Which of these three options is selectable will depend on what has been selected on the reminders tree. If it is an individual reminder then Evaluate Reminder will be selectable, if it is a category then Evaluate Category Reminders will be selectable, and if it is a processed reminder then Evaluate Processed Reminder will be selectable.  The other two options are for Reminder Managers.  **CPRS Reports Tab**  Health Summaries containing Clinical Reminders can be viewed from the Reports tab in CPRS. See the Health Summary section later in this guide for more information.  The Ad hoc health summary can also be used to display selected clinical reminders using either an abbreviated display or the full clinical maintenance display. (See  Chapter 6: Health Summaries and Clinical Reminders  )   |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 2: Resolving Clinical Reminders**  **NOTE:**  **Your site can determine the folder view – which reminders and categories/folders appear in the reminders drawer.**   | **Summary of Steps to Process Reminders**  These are the basic steps for processing reminders from the Notes tab in CPRS. These steps are described in more detail in Chapter 3.  1. **Start a new progress note.** To process a reminder, start a new progress note. When you begin a new progress note, the reminders drawer appears.  1. **Open the reminders drawer.** When you click on the reminders drawer, you see several folders containing reminders for this patient. Possible folders include Due, Applicable, Not Applicable, All Evaluated, and Other Categories. These folders may contain a hierarchy of folders and reminders within folders. The view of folders is customizable by you (see Appendix C ). The folders and subfolders in the Reminders Drawer are sometimes called the “tree view.”  1. **Choose a reminder.** Open a folder (if necessary) and click a reminder that you wish to process. At this point, you may be asked to provide the primary encounter provider, so that any PCE data entered from reminder dialog processing can be saved.   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 2: Resolving Clinical Reminders**   | **Summary of Steps to Process Reminders**  **4. (cont’d)**  If the reminder has an associated reminder dialog, a small dialog icon is shown in the bottom-right corner of the clock icon. If you click on one of these reminders, a dialog box appears, which lists possible actions or activities that may satisfy this reminder. If this is a National reminder, the dialog was created by national developers and/or members of the Office of Quality and Performance. Otherwise, the contents of this dialog were created at your site by your Clinical Application Coordinator (CAC) or a Clinical Reminders Manager. Clinicians should be involved with defining these dialogs.  If no dialog icon is displayed on a reminder, it means that your site hasn’t created and/or linked a dialog to the reminder. Your CAC can provide information about this. Definitions of the reminders icons are available on the Action menu of the Available Reminders window (see page 10).   |
|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**These reminders have reminder dialogs linked to them, as indicated by the text box on the question mark.**

**The question mark indicates the reminder hasn’t been evaluated to determine its status. When you click on the reminder, it will be evaluated, and the icon changes accordingly. See page** **10** **for icon definitions.**

| **Chapter 2: Resolving Clinical Reminders, cont’d**  **TIP:**  **Use the Next or Back buttons to take you to the dialog for the next or previous reminder due in the reminders drawer.**   | **Summary of Steps to Process Reminders, cont’d**  1. **Complete the dialog box.** The dialog box lists possible actions or interventions that may be taken to satisfy this reminder. As you make selections from the dialog box, you can see the text of the progress note in the bottom part of the screen (below the Clear, Back, and Next buttons). Below the progress note text area is the encounter information including orders and PCE, Mental Health, and Vital Sign data. The bold text in these areas applies to the specific reminder you are processing. You can process multiple reminders.  1. **Expanded dialog boxes.** Clicking a checkbox may bring up additional choices: an area for comments, a diagnosis to choose, or other information that may satisfy the reminder.  **Dialog with orders.**  Reminder dialogs can include orders. If quick orders are included in the dialog, these are placed as soon as the reminder processing is finished and the orders are signed. If the order requires more information before releasing the order, an order dialog will appear after you click Finish, allowing you to complete the order.  **Mental health tests.**  Reminder dialogs can include a pre- defined set of mental health tests. The reminder definition can include any mental health test, but the reminder dialog is limited in the GUI resolution process to allow clinicians to enter results for the following tests: AIMS, AUDC, AUDIT, BDI, CAGE, DOM80, DOMG, MISS, and ZUNG. Progress  note text can be generated based on the mental health score.  1. **Finish processing the reminder and complete your note.** Click on the Finish button when you have checked all the appropriate checkboxes for each reminder you wish to process. You then go back to the Note window, where you can review and edit the reminder dialog progress note text added, to have a completed progress note for the encounter.  1. **(Optional) Evaluate processed reminders.** You can use the Action menu to select the Evaluate Processed Reminders menu item from the Reminders Available window, to ensure that the reminders are satisfied. This action will evaluate the reminders that you processed while you wait, and update the Reminders Available window and reminders drawer lists to reflect the new statuses.   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 3: Resolving IHD Reminders**   | **Overview**  **IHD Reminder Definitions**  The following IHD reminder definitions are distributed with Clinical Reminders Version 2.0:  **VA-IHD LIPID PROFILE**  This national reminder identifies patients with known IHD (i.e., a documented ICD-9 code for IHD on or after 10/01/99) who have not had a serum lipid panel within the last year. If a more recent record of an UNCONFIRMED IHD DIAGNOSIS is found, the reminder will not be applicable to the patient.  **VA-IHD ELEVATED LDL**  This national reminder identifies patients with known IHD (i.e., a documented ICD-9 code on or after 10/01/99) who have had a serum lipid panel within the last year, where the most recent LDL lab test (or documented outside LDL) is greater than or equal to 120 mg/dl. If a more recent record of an UNCONFIRMED IHD DIAGNOSIS is found, the reminder will not be applicable to the patient.  **VA-*IHD LIPID PROFILE REPORTING**  This national IHD Lipid Profile Reporting reminder is used monthly to roll up LDL compliance totals for IHD patients. This reminder identifies patients with known IHD (i.e., a documented ICD-9 code for IHD) who have not had a serum lipid panel/LDL (calculated or direct lab package LDL) or documented outside LDL within the last two years. If a more recent record of an UNCONFIRMED IHD DIAGNOSIS is found, the reminder will not be applicable to the patient.  **VA-*IHD ELEVATED LDL REPORTING**  This national IHD Elevated LDL Reporting reminder is used monthly to roll up compliance totals for management of IHD patients whose most recent LDL is greater than or equal to 120mg/dl. This national reminder identifies patients with known IHD (i.e., a documented  ICD-9 code) who have had a serum lipid panel within the last two years, where the most recent LDL lab test (or documented outside LDL) is greater than or equal to 120 mg/dl. If a more recent record of an UNCONFIRMED IHD DIAGNOSIS is found, the reminder will not be applicable to the patient. These compliance reminders are not for use in CPRS, so there are no related reminder dialogs.   |
|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 3: Resolving IHD Reminders**  **NOTE:**  **Due, Applicable, Not Applicable, All Evaluated, or Other Categories folders may be displayed.**  **You or your site can modify the contents of the “Other Categories” folder, through the option Add/Edit Reminder Categories on the CPRS Configuration Menu.**   | **Steps to Process VA-IHD Lipid Profile**  1. **Start a new progress note.**  When you begin a new progress note, the reminders “drawer” appears below the default list of notes. You are prompted to enter Progress Note properties (Title, date, etc.) before you begin processing reminders.  CRPROVIDER,ONE  **Reminders Drawer**  1. **Open the reminders drawer**  Click on the reminders drawer (button) to see reminders.  <!-- image -->   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 3: Resolving IHD Clinical Reminders**  **NOTE:**  **To process a reminder, a “reminder dialog” must be defined and associated (linked) with the reminder.**  **This is done by your Clinical Reminders Manager or coordinator (usually with clinician assistance). If a reminder dialog is available for a reminder, an icon representing a dialog is on the corner of the reminder icon.**   | **Steps to Process VA-IHD Lipid Profile, cont’d**  **3. Locate the IHD Lipid Profile reminder.**  If necessary, open a folder (Due, Applicable, Other Categories, etc.) and click on the IHD Lipid Profile Reminder.  <!-- image -->   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 3: Resolving IHD Clinical Reminders**   | **Steps to Process VA-IHD Lipid Profile, cont’d**  **4. Complete the dialog box.**  When you select the IHD Lipid Profile reminder to process, a dialog box appears, such as the one below. It shows the possible things that may satisfy the reminder.   |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Example: IHD Lipid Profile Dialog**

<!-- image -->

| **Chapter 3: Resolving IHD Clinical Reminders**   | **Steps to Process VA-IHD Lipid Profile, cont’d**  **4. Complete the dialog box, cont’d.**  If quick orders are included in the reminder dialog, these are activated as soon as the progress note is completed and the note and order are signed. If the order requires more information before completion, an order dialog will appear after you click Finish, allowing you to complete the order.  When you click a checkbox or item, the associated text that will be placed in the progress note is shown in the area below the buttons. Data that will update PCE, orders, Vital Signs, and Mental Health packages will be shown in the area below that.  See the example on the next page.   |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Example: Expanded Dialog when “Order Lipid Profile” Checked**

<!-- image -->

| **Chapter 3: Resolving IHD Clinical Reminders**   | **Steps to Process VA-IHD Lipid Profile, cont’d**  **4. Complete the dialog box, cont’d.**  When you click a checkbox or item, the associated text that will be placed in the progress note is shown in the area below the buttons. Data that will update PCE, orders, Vital Signs, and Mental Health packages is shown in the area below that.   |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Example: Progress Note text**

| **Chapter 3: Resolving IHD Clinical Reminders**   | **Steps to Process VA-IHD Lipid Profile, cont’d**  **Next and Back processing**  Use the Next button to process the next reminder that is due in the reminders drawer. Use the Back button to take you to the reminder processed previously to the one you are currently processing.  **Clinical Maintenance review**  While processing the reminder, you can review current Clinical Maintenance patient data related to the reminder by clicking on the Clinical Maint button at the bottom of the dialog box.  NOTE: Information in the Clinical Maintenance box has been expanded and enhanced in Version 2 of Clinical Reminders.  **Clearing a single reminder**  You will probably process several reminders for a single visit. If you have entered information on a reminder, but you need to start over on that reminder only, you can simply click Clear on the reminder from the reminders drawer, and then click the Clear button in the reminders dialog box. This removes all previous dialog selections from the reminder’s dialog box and removes the related text and data from the Progress Note text box and the PCE data box for this reminder. You can now start processing again. NOTE: Clicking Clear will remove the information from only one reminder. Be careful that you are on the correct reminder before you click Clear.   |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Example: Clinical Maintenance window for IHD Lipid Profile**

<!-- image -->

| **Chapter 3: Resolving IHD Clinical Reminders**   | **Steps to Process VA-IHD Lipid Profile, cont’d**  **Canceling out of the Processing dialog**  If you reach the Reminders Processing dialog by mistake or you wish to delete information that you have entered and start over, click Cancel.  **NOTE: If you click Cancel, you will lose all of the information for reminders that you have entered.**   |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Example: Warning box when Cancel button clicked**

<!-- image -->

| **Chapter 3: Resolving IHD Clinical Reminders**   | **Steps to Process VA-IHD Lipid Profile, cont’d**  1. **Finish processing the reminder**  After you have entered all the information, you can finish processing the reminders. When you finish, the following things will happen:  - The predefined text is placed in the note you have begun writing. - The encounter information is sent to PCE. - If there are orders defined in the dialog, it will also create the orders. If the orders require input (if they are not predefined quick orders without prompts), the order dialogs will come up so that you can complete the orders. You will then have to sign any orders that are created.  To finish processing reminders, click Finish.  After you click Finish, you are returned to the Note screen, where you can see the text created by reminder processing. You can edit this, as necessary.   |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Example: Progress Note after reminder dialog completion**

<!-- image -->

| **Chapter 3: Resolving IHD Clinical Reminders**   | **Steps to Process VA-IHD Lipid Profile, cont’d**  **7. (Optional) Evaluate processed reminders**  After you have processed a reminder, you can use this menu item in the Available Reminders window to see if your actions during the encounter satisfied the reminder. This action will evaluate the reminders that you processed while you wait, and update the Reminders Available window and Reminders drawer lists to reflect the new statuses.  NOTE: PCE data may take a few minutes to be correctly recorded. Please wait a few minutes after processing a reminder before evaluating it again to ensure that it was satisfied.  To evaluate processed reminders, go to the Available Reminders dialog by clicking on the Reminders button, choose Action, and then click on Evaluate Processed Reminders.   |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Example: Evaluate Processed Reminder**

<!-- image -->

| **Chapter 3: Resolving IHD Clinical Reminders**   | **VA-IHD ELEVATED LDL**  This national reminder identifies patients with known IHD (i.e., a documented ICD-9 code on or after 10/01/99) who have had a serum lipid panel within the last year, where the most recent LDL lab test (or documented outside LDL) is greater than or equal to 120 mg/dl. If a more recent record of an UNCONFIRMED IHD DIAGNOSIS is found, the reminder will not be applicable to the patient.  Use the same steps to process this reminder as those described above.   |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Example: IHD Elevated LDL Dialog**

<!-- image -->

| **Chapter 4: Processing Mental Health Reminders**   | **Mental Health Reminders**  The following Mental Health reminder definitions are re-distributed with Clinical Reminders Version 2.0:  **VA-ANTIPSYCHOTIC MED SIDE EFF EVAL**  The Abnormal Involuntary Movement Scale (AIMS) reminder has been designed to be due on all patients who are on any one of the antipsychotics (excluding ones like Compazine). The taxonomy for Schizophrenia is included in the reminder, but will not be part of the cohort logic. By leaving the taxonomy in the reminder, data roll-up can use the Report Extracts functionality in version 2.0, either with or without information on patients with Schizophrenia.  **VA-DEPRESSION SCREENING**  Screening for Depression using a standard tool should be done on a yearly basis. The yearly screening is satisfied by entry of a health factor indicating positive or negative results for the 2 question MacArthur screening tool or by entry of negative or positive results in the MH package. The reminder is also resolved by entry of information indicating that the patient is already being treated/evaluated in a Mental Health clinic.  Patients are automatically excluded from the cohort if they have a recent diagnosis of depression (ICD code in the past 1 year) and have either a CPT code for psychotherapy in the past 3 months or are on antidepressant medication (current supply of medication in the past 3 months).  **VA-POS DEPRESSION SCREEN FOLLOWUP**  The reminder is applicable if the patient has positive depression screen in the past 1 year (DEPRESSION SCREEN POSITIVE). If a more recent negative depression screen is entered, then the reminder becomes not applicable (DEPRESSION SCREEN NEGATIVE).   |
|-----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 4: Processing Mental Health Reminders, cont’d**  **NOTE**  **Sites that use a different screening tool than the 2 question MacArthur screening tool will need to create local health factors to indicate a positive or negative result and will need to map those local health factors to the national terms: DEPRESSION SCREEN NEGATIVE, and DEPRESSION SCREEN**   | **Mental Health Reminder Processing**  **Depression Screening**  The yearly screening is satisfied by entry of a health factor indicating positive or negative results for the 2-question MacArthur screening tool or by entry of negative or positive results of any of the following in the MH package:  Negative	Positive  DOM80=0	DOM80=1  DOMG&lt;4	DOMG&gt;3  CRS&lt;10	CRS&gt;9  BDI&lt;10	BDI&gt;9  Zung&lt;33	Zung&gt;32  The reminder is also resolved by entry of information indicating that the patient is already being treated/evaluated in a Mental Health clinic.   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Example: Depression Screening dialog initial window**

2-question McArthur test

| **Chapter 4: Processing Mental Health Reminders, cont’d**   | **Depression Screening (cont’d)**  When you click on the DOM80 or DOMG button, a window pops up that lets you perform the test. The results of the test go in the patient’s record – in the progress note and in the Mental Health package.   |
|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### Example: DOM80 test

This box pops up when you click on the DOM80 button.

| **Chapter 4: Processing Mental Health Reminders,**  ***cont’d***   | **Depression Screening (cont’d)**  The reminder is also resolved by the following:  - Unable to screen due to acute or medical illness - Patient refuses to answer depression screening questions - Entry of information indicating that the patient is already being evaluated/treated in a Mental Health clinic   |
|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Example: Other questions that resolve reminder**

<!-- image -->

| **Chapter 4: Processing Mental Health Reminders, cont’d**   | **Depression Screen Positive – Needs F/U Assessment**  This reminder is applicable if the patient has positive depression screen in the past 1 year (DEPRESSION SCREEN POSITIVE). If a more recent negative depression screen is entered, then the reminder becomes not applicable (DEPRESSION SCREEN NEGATIVE).   |
|-------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Example: Depression Screen Positive**

<!-- image -->

| **Chapter 4: Processing Mental Health Reminders, cont’d**   | **Abnormal Involuntary Movement Scale, (AIMS) Dialog**  This reminder dialog uses the AIMS Mental Health Instrument. If you click on the Perform AIMS button, the instrument pops up, so that you can answer the questions, which are scored and go into the Mental Health package and the Progress Note.  The reminder is also resolved by refusal to take the test or refusal to take antipsychotic medications.   |
|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Example: Eval for Abnl Involuntary Movements**

<!-- image -->

| **Chapter 4: Processing Mental Health Reminders, cont’d**   | **AIMS Dialog**  When you click on the Perform AIMS button, the screen below pops up, so that you can answer the questions, which are scored and go into the Mental Health package and the Progress Note.   |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Example: AIMS Mental Health Instrument**

<!-- image -->

|    | **Chapter 5: Using Reminder Reports**  **TIP:**  **Clinicians should work with their site’s clinical reminder coordinator or Clinical Application Coordinator to design and validate reports used at their site. Reporting can be resource-intensive and many sites have elected to centralize the access to run reports.**  **However, limited report templates may be available to selected clinicians who work closely with clinical reminders or QM at their site.**   | **Chapter 5: Reminder Reports**  Reminder reports allow you to do large and small-scale comparisons of clinics, divisions, teams, and providers and can help in finding patients who have “slipped through the cracks.”  - Ever want to know how well your team is doing with immunizations or diabetes care or pain assessments? - Ever want to know who is coming this week who needs pneumococcal immunization, or who needs diabetic foot exam and education, or who has had a high pain score in the past and needs a pain assessment? - Would anyone at your site ever want to look at a group of patients for a research project – patients with a creatinine between 1.5 and 5 who do not have diabetes who are under the age of 80?  Reports allow you to verify diagnoses, verify that appropriate treatment was given, identify patients requiring intervention, and validate effectiveness of care.  Reminder reports are very flexible. Reports can be run on:  - Location(s)  -One or more inpatient hospital locations  -Current inpatients  -Patients admitted during a date range  - Alphabetical - Sorted by ward/bed  -one or more outpatient hospital locations  -all hospital locations  -stop code(s)  -clinic group(s)  - OERR Team(s) - PCMM team(s), - PCMM provider(s) - Reminder patient list(s).  Reports can be combined or kept separate for one or more facility Report results can display:  - Summary results (numbers only) - Detailed results (patients’ names).  -Identifier: Entire social security number or last 4 numbers of social security number only  -Sort alphabetically or by date of the next clinic visit.  Reports can be run on either on patients with Past visits or with Future visits.   |
|----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

| **Chapter 5: Using Reminder Reports**  **TIP:**  The EPI extract finding list and total options are specific to the Hepatitis C Extract project. The extracted data is based on the following reminders: VA-HEP C RISK ASSESSMENT, VA- NATIONAL EPI LAB EXTRACT, and VA-NATIONAL EPI RX EXTRACT.   | **Reminder Reports, cont’d**  **Changes in Version 2**  New reports on the Reminder Reports menu or changes to report functionality in Clinical Reminders V. 2.0 include:  - Extract Queri Totals [PXRM EXTRACT QUERI TOTALS] This option prints reminder and finding totals for extract summaries created by the automatic QUERI extracts.  - GEC Referral Report, [PXRM GEC REFERRAL REPORT] This option is used to generate GEC Reports. GEC (Geriatrics Extended Care) is used for referral of geriatric patients to receive further care.  - New type of report, Reminder Patient List, on Reminders Due option.  - Ability to show inpatient location on future appointments.   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 5: Using Reminder Reports**   | **Changes in Version 2**  Version 2.0 of Reminders contains changes to the date range that can be used in searches in the Reminders Due reports. The changes include:  - Effective period and effective date are eliminated  o	Replaced with beginning date and ending date  - Any of the FileMan date formats are acceptable  o	May 14, 2003, T-1Y, T-2M, T-3D  - Beginning date default is beginning of data - Ending date default is today  **Benefits of Date Range Finding Searches**  - The search for findings is done only in the specified date range. - Retrospective reminder reports are now possible.  **Changes in Patch 4**  - A prompt was added to allow you to exclude/include Test Patients. - A prompt was added to allow you to exclude/include deceased patients.   |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 5: Using Reminder Reports**  **TIP:**  **Reminders Due Report:**  **The summary report may be run for several reminders.**  **The detailed report may only be run for one reminder**   | **Reminder Reports**  **Reminders Due Report**  For a selected reminder, the report lists any reminders that are currently due. Reports can be defined by the following criteria:  - Individual Patient - Reminder Patient List (all patients on a patient list created through the Patient List options) - Hospital Location (all patients with encounters) - OE/RR Team (all patients in team) - PCMM Provider (all practitioner patients) - PCMM Team (all patients in team)  **Summary report**  : displays totals of how many patients of those selected have reminders due.  **Detailed report:**  displays patients (in alphabetical order) with reminders due. The report displays for each patient the date the reminder is due, the date the reminder was last done, and next appointment date. The detailed report can also list all future appointments, if specified. Detailed reports for Location or Provider may also be sorted by next appointment date.  Reports by Hospital Location, Provider, or Team print a separate report for each Hospital Location, Provider, or Team selected.  Reports for all Hospital Locations are not separated by individual locations. The report by Hospital Location can report either current inpatients or admissions within a selected date range.   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 5: Using Reminder Reports**  **NOTE: After scheduling a Reminder report to run, you may receive a message such as the following:**  6294955: ^PXRMXPR, Reminder Due Report - print. Device NT\_SPOOL. VAH,ROU.  From Yesterday at 13:14, By you. Created without being scheduled.  **This doesn’t mean that there’s an error with the report processing. Clinical Reminders processes its reports in two tasks, one for SORT and one for PRINT. The print task will always show “created without being scheduled” until the sort task is complete.**   | **Reminder Reports**  **Report templates**  The selection criteria used for the Reminders Due reports may be saved into a report template file, with a user-specified identifier, as the report is being run.  When running the Reminder Due report, you may select from an existing template and run a new report using the parameters from the selected template. The prompts for date range and sort order are displayed, but all other parameters are taken from the previous report. If you select a print template, you may also edit the template and/or copy to a new template before running the report.  ***Scenario***  *: How many patients are not receiving reminders who should be for Hepatitis C?*  A report can be prepared that compares “Applicable” reminders to those that have been defined as “Due.” The difference may be a missed opportunity. This can be done by individual provider or for all providers in a location or medical center, as a quality assurance measure. The example below shows a summary report where the reminders selected are all related to Hepatitis C. This illustrates how you could use the summary report as part of a larger strategy for implementing and managing a Hepatitis C guideline using reminders.   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Example Report**

Report run on 175 patients.

16

7

0

36

27

15

3

4

4

6

172

30

36

36

45

19

12

13

Hep C Risk Factor Screen Hep C Test for Risk

Hep C Diagnosis Missed Hep C Diagnosis

Hep C- Dz &amp; Trans Ed Hep C - Eval for Rx Chr Hep - Hep A Titer Hepatitis A Vaccine Chr Hepatitis - AFP Chr Hepatitis - U/S

# Patients with Reminder Applicable	Due

| **Chapter 6: Health Summaries and Clinical Reminders**                          | **Health Summaries**  Reminder items can be added to health summary displays. Health summaries and reminder definitions can be tailored to suit clinicians’ needs.  **Health Summary Reminder Components**  - *Reminders Due:* an abbreviated component indicating only what is due now. - *Reminders Summary* : this provides the status, the next due date, and the last done date. - *Reminder Maintenance:* this component provides:  - Details about what was found from searching the **V** *IST* **A**  clinical data:  - Text related to the findings found or not found (as defined in the reminder). This includes taxonomies (ICD or CPT codes), health factors, and test results related to the reminder and computed findings (e.g., Body Mass Index). - Final frequency and age range used for the reminder.  NOTE: Statuses include “DUE SOON,” to allow you to process a reminder in advance, if convenient.   |                             |                               |                                 |            |    |
|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|-------------------------------|---------------------------------|------------|----|
| **Example of**  ***Reminder Due***  **as displayed on a health summary**        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                             |                               |                                 |            |    |
| Advanced Directives Education Alcohol Abuse Education                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | --STATUS-- DUE NOW  DUE NOW | --DUE DATE-- DUE NOW  DUE NOW | --LAST DONE--  unknown  unknown |            |    |
| **Example of Reminder Summary as displayed on a health summary**                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                             |                               |                                 |            |    |
| --STATUS--	--DUE DATE--	--LAST DONE--  Mammogram	RESOLVED	05/01/2003	10/01/2002 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                             |                               |                                 |            |    |
| Pap Smear                                                                       | Pap Smear                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | DUE NOW                     | 06/01/2003                    | unknown                         | unknown    |    |
| Diabetic Eye Exam                                                               | Diabetic Eye Exam                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | DUE NOW                     | 06/01/2003                    | 06/01/2002                      | 06/01/2002 |    |

#### Example of Reminder Maintenance as displayed on a health summary

| **Chapter 6: Health Summaries, cont’d**   | **Health Summary on Reports Tab in CPRS**  When you open the Reports tab, select Health Summary, and then select a Reminders Health Summary Type.   |
|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|

**Example: Health Summary on CPRS Report tab**

<!-- image -->

| **Chapter 6: Health Summaries, cont’d**  **NOTE:**  **The veteran’s private health record will be securely stored and only accessible by the veteran and others they have identified.**   | **My Health**  ***e***  **Vet Health Summary**  Clinical Reminders V.2.0 contains new health summary components to support the My Health  *e*  Vet project. These components will allow display of clinical reminder information to patients.  My Health  *e*  Vet is a Web-based system that empowers veterans with information and tools so that they can improve their health to the maximum extent possible. Participating veterans are given copies of key portions of their electronic health records.  New health summary components were devised that eliminate much of the technical text and code information that is contained in the CM component. These components will be used to display summary and detailed information on individual patient reminders to the patients from within My Health  *e*  Vet. They can be also used in other health summaries at a facility if it is useful for display to users at the site.   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 6: Health Summaries, cont’d**   | **My Health**  ***e***  **Vet Health Summary**  Two new national Health Summary types were created to include the new health summary components:  - REMOTE MHV REMINDERS DETAIL - REMOTE MHV REMINDERS SUMMARY  These are available in health summaries on the reports tab in CPRS. Use of these health summaries will allow anyone to view the reminders and text that are being displayed to the patients, even if the patient is being seen at a different site.   |
|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Example: MHVS Health Summary**

10/06/2004 08:55

************	CONFIDENTIAL REMOTE MHV REMINDERS SUMMARY	SUMMARY	************* CRPATIENT,ONE		000-31-9898	1A(1&amp;2)		DOB: 00/00/1950

MHVS - Summary Display

--STATUS-- --DUE DATE--	--LAST DONE--

Flu vaccine	DUE NOW	DUE NOW	unknown Please check these web sites for more information:

Web Site: CDC Influenza Home Page

URL: [http://www.cdc.gov/ncidod/diseases/flu/fluvirus.htm](http://www.cdc.gov/ncidod/diseases/flu/fluvirus.htm)

Web Site: Weekly Update on Influenza Rates

URL: [http://www.cdc.gov/ncidod/diseases/flu/weekly.htm](http://www.cdc.gov/ncidod/diseases/flu/weekly.htm)

CDC Site for weekly updates on the current influenza activity in the community.

Web Site: Dept HHS Information on Influenza Vaccination

URL: [http://odphp.osophs.dhhs.gov/pubs/guidecps/text/CH66.txt](http://odphp.osophs.dhhs.gov/pubs/guidecps/text/CH66.txt)

Web Site: California Influenza Information

URL: [http://www.dhs.ca.gov/ps/dcdc/VRDL/html/Flutable02-03.htm](http://www.dhs.ca.gov/ps/dcdc/VRDL/html/Flutable02-03.htm)

Web Site: Patient Handout for Influenza Vaccine

URL: [http://www.cdc.gov/nip/publications/VIS/vis-flu.pdf](http://www.cdc.gov/nip/publications/VIS/vis-flu.pdf)

| **Chapter 6: Health Summaries, cont’d**   | **My Health**  ***e***  **Vet Health Summary, cont’d**  The components can also be used in other health summaries at a facility if it is useful for display to users at the site   |
|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Example: MHVS Health Summary, cont’d**

| **Chapter 7: VA- Geriatric Extended Care (GEC) Referral**  **Important:**  This GEC screening tool is for the purpose of evaluating a patient’s needs for extended care and is not to be used as the document to refer or place a patient. The document should be part of a packet of information obtained when placing a patient.  Four different disciplines should complete the screening, making it less burdensome on any one individual.   | **VA-Geriatric Extended Care Referral**  **Overview**  Clinical Reminders V.2.0 includes a nationally standardized computer instrument called VA Geriatric Extended Care (GEC), which replaces paper forms for evaluating veterans for extended care needs. Paper forms that facilities use include VA Form 10-7108, VA Form 10064a- Patient Assessment Instrument (PAI), and VA Form 1204-Referral for Community Nursing Home Care (others sites use various instruments including Consults).  The GEC Referral is comprised of four reminder dialogs: VA-GEC SOCIAL SERVICES, VA-GEC NURSING ASSESSMENT, VA-GEC CARE RECOMMENDATIONS and VA-GEC CARE  COORDINATION. These dialogs are designed for use as Text Integration Utility (TIU) templates to enter data regarding the need for extended care. Data entered via the dialogs are captured as health factors to be used for local and national reporting.  The software also includes a new report menu that may be used for local analysis.   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 7: GEC, cont’d**  **Updates to GEC options and GEC Reports**  **See**  **Appendix D**  **for a description and examples of the GEC Report changes.**   | **Changes made in Patch 4 (PXRM*2.0*4)**  - The GEC Care Recommendation Dialog has been modified to allow more than one selection when a person wants to refer a patient to more than one location.  - Items 15-19 (Prognosis, Weight Bearing, Equipment, Diet, and Supplies) were moved from the “GEC Nursing” dialog to the “Care Recommendations” Dialog.  - A problem with the user being able to take some editing actions on GEC dialogs has been corrected, so the user is not able to copy or delete dialog groups from the GEC dialogs.  - An undefined error (&lt;UNDEFINED&gt;CALCMON+12&lt;&gt; PXRMG2M1) that occurred when the scheduled event fired off at the beginning of each month has been repaired.  - Several of the GEC Reports were not showing a complete list of patients or providers. This has now been corrected with this patch. The division and age of the patient has been added to some reports to help in identifying the patient.  - There is a new choice in the GEC reports menu that will give the sites the option to open a closed referral, merge two referrals, and close an open referral.   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 7: GEC, cont’d**   | **GEC Status Check**  There is no limit to the entry of GEC Referral data. Since there may be multiple entries of the same health factors over time, and since the data is entered via separate dialogs, extraction and viewing requires the data to be discretely identified. The GEC software depends upon the user to indicate when the data from a given referral should be concluded. The referral is finalized using a new feature called the GEC Status Indicator. This indicator is presented to the user as a dialog at the conclusion of the VA-GEC CARE COORDINATION dialog. It will prompt the user to indicate the conclusion of the Referral with a Yes or No response and will list any missing dialogs. If Yes is selected, the data for the current episode of the Referral is closed. If No is selected, the Indicator is displayed and the data entered will be included with the current episode of the Referral. The Indicator will then be displayed with each succeeding GEC dialog until Yes is selected.  To assist the ongoing management of completing GEC Referrals, the GEC Status Indicator may be added to the CPRS GUI Tools drop-down menu. It may be set at the User or Team level. If added to the drop- down menu, the Indicator may be viewed at any time and used to close the referral if needed.  *See your CAC or the Clinical Reminders V. 2.0 Setup Guide for instructions on adding this to the Tools menu.*  GEC dialogs also contain a checkbox called “CHECK TO SEE REFERRAL STATUS.” This checkbox appears on all dialog boxes and lets you see a real-time view of the current Referral’s dialog-completion status.  It presents information similar to that found on the GEC Referral Status Display and can be used to determine if the Referral can be finalized.   |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 7: GEC, cont’d**   | **GEC Status Check**  **Status Indicator Instructions, cont’d**  The Yes button should only be selected if the user is certain no changes are needed and they are ready to commit to the note’s authentication.  The Status Indicator does not update after the referral has been completed. Put another way, once a referral has been closed, it cannot be reopened. This same risk exists if a note is deleted after the Yes button has been selected and the user then reenters the dialog.  Users should  *always*  check the Status Indicator when a new referral is initiated on a patient. Doing so will provide the opportunity to close any previous referrals inadvertently left open.  **Example of Status Indicator when all dialogs are complete.**  <!-- image -->  **Example of Status Indicator when some dialogs are missing.**  <!-- image -->   |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 7: GEC, cont’d**   | **GEC Referral Ad hoc Health Summaries**  Two new health summary components have been created and distributed with this software:  - GEC Completed Referral Count (GECC) - GEC Health Factor Category (GECH)  The first displays all GEC referral data according to the occurrence and time limits identified.  If a user should have access to these GEC reports, they must have access to the Ad Hoc Health Summary type. (This can be set using GMTS GUI HS LIST PARAMETERS.)  **GEC Referral Reports**  The software includes a new set of reports that provide a variety of GEC health factor perspectives. The reports capture data elements for reporting and tracking use of the GEC Referral Screening Tool. The reports may be generated in formatted or delimited output. The Summary (Score) report provides summary (calculated) totals from specific sections of the screening tool identified by the Office of Geriatrics Extended Care. See  Appendix D  for more details.   |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 7: GEC, cont’d**   | **GEC Referral Reminders and Dialogs**  The GEC reminders are comprised of dialogs and health factors only. They have neither cohort nor resolution logic, and will not become due. They are intended only as TIU templates and do not need to be assigned to the CPRS Cover Sheet. Due to potential complications with reporting and duplicate entries, it is recommended that the GEC dialogs not be added to the Reminders drawer/Cover sheet.  The Referral was designed for inter-disciplinary use with dialogs created for separate services. However, a single user may perform them all. With only a few exceptions, each section of the dialogs is mandatory and is marked with an asterisk (*). The completion of all four dialogs constitutes a discrete episode of the GEC Referral.  The VA-GEC REFERRAL SOCIAL SERVICES, VA-GEC REFERRAL NURSING ASSESSMENT, and VA-GEC REFERRAL  CARE RECOMMENDATIONS dialogs comprise the clinical screening. The VA-GEC REFERRAL CARE COORDINATION dialog is used administratively to record the arrangement of and funding for extended care services. These dialogs may be performed in any order that local practices dictate. However, it is expected the screening portion will be completed prior to the coordination of services. When the screen is complete, a consult order should be placed to the service responsible for arranging services.  **GEC Consult Order**  Most sites have either an individual or a service responsible for arranging and coordinating extended care services. To accommodate local business practices and flexibility, sites may associate any consult service (or menu) they already have in place. If none exist, the sites may create a consult or establish some alternative practice to ensure that both services are arranged and that the VA-GEC REFERRAL CARE COORDINATION dialog is completed.  Sites will need to review the privileging status of those performing the GEC Referral. The staff assigned to place the consult order associated with the GEC dialogs will require the ability to place a consult order.   |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| **Chapter 7: GEC Usage, cont’d**  **NOTE:**  **Refer to Appendix C in the TIU/ASU Implementation Guide for complete instructions about Interdisciplinary Notes**   | **GEC Interdisciplinary Notes**  The GEC Referral dialogs are intended for use as TIU templates. It is also expected that they will be used as part of a TIU Interdisciplinary (ID) note. The Office of Geriatrics Extended Care requests that the parent ID note title be:  “GEC EXTENDED CARE REFERRAL”  **Steps to use the GEC Dialog templates:**  1. In the CPRS GUI, open the NOTES tab. 2. Click on New Note. **Example: Selecting GEC REFERRAL CARE COORDINATION** <!-- image --> Chapter 7: GEC Usage, cont’d  This is first screen shot when you select GEC REFERRAL CARE COORDINATION. When you select one type of service, the screen for that service type expands. The next screen shots show each in expanded form. **Example: GEC REFERRAL CARE COORDINATION Opening screen** <!-- image --> Chapter 7: GEC Usage, cont’d  This is the expanded screen when you select HOME CARE SERVICES in the GEC REFERRAL CARE COORDINATION dialog. Note the checkbox “CHECK TO SEE REFERRAL STATUS.” This is available on all dialog boxes and lets you see a real-time view of the current Referral’s dialog-completion status. It presents information similar to that found on the GEC Referral Status Display and can be used to determine if the Referral can be finalized. **Example: Expanded screen for HOME CARE SERVICES** <!-- image --> <!-- image --> <!-- image --> <!-- image --> <!-- image --> <!-- image --> <!-- image --> <!-- image --> **Example: CARE RECOMMENDATION Dialogs** With patch 4, the Prognosis, Weight Bearing, Diet, Equipment, and Supplies sections were moved from the Nursing Assessment dialog to the Care Recommendation dialog. <!-- image --> <!-- image --> In patch 4, these items were moved from Nursing Assessment to the Care Recommendation dialog. <!-- image --> <!-- image --> Chapter 8: Code Set Versioning   NOTE: The Code Text Descriptors project, released in October 2004, is a follow-up project to Code Set Versioning. It ensures that the diagnostic and procedure descriptions used for billing purposes must be the descriptors that were applicable at the time the service was provided. It doesn’t affect Clinical Reminders. Chapter 8: Code Set Versioning (CSV) Changes in Reminders Several changes and enhancements are included in Clinical Reminders V.2.0 in support of Code Set Versioning, mandated under the Health Information Portability and Accountability Act (HIPAA). The changes will insure that only active, on the encounter date, ICD9, ICD0, and CPT codes are selectable in the CPRS GUI application while using Clinical Reminder Dialogs. It will also produce several email messages to Clinical Reminder Managers to help in deciding the correct usage of these codes in the Taxonomies and Dialogs.  PXRM*1.5*18, which contained the CSV changes, was previously released in conjunction with CSV_UTIL v1, Code Set Versioning, which contains routines, globals, and data dictionary changes to recognize code sets for the International Classification of Diseases, Clinical Modification (ICD-9-CM), Current Procedural Terminology (CPT) and Health Care Financing Administration (HCFA) Common Procedure Coding System (HCPCS). When implemented, the Lexicon will allow translation of these three code systems to select codes based upon a date that an event occurred with the Standards Development Organization (SDO) established specific code that existed on that event date.  Version 2.0 of Clinical Reminders includes all of the CSV changes contained in patch 18. Chapter 9: My HealtheVet Chapter 9: My HealtheVet Changes in Reminders  Clinical Reminders V. 2.0 contains new health summary components to support the My HealtheVet project. These components will allow display of clinical reminder information to patients. New health summary components were devised that eliminate much of the technical text and code information that is normally displayed for clinicians. These new components will be used to display summary and detailed information on individual patient reminders to the patients from within My HealtheVet. They can be also used in other health summaries at a facility if it is useful for display to users at the site.  See the section under Chapter 5: Health Summary, for examples and descriptions of My HealtheVet HS components.  My Health Reminders are being developed for veterans to view in their My HealtheVet record. Twelve patient reminders have been created:  Influenza Vaccine Pneumonia Vaccine Colorectal Screen Mammogram Screen Pap Smear Screen Three for Diabetes: Eye, Foot and HbAlc (blood glucose) Two for lipids: lipid measurement and LDL control Hypertension BMI  These were distributed in patch PXRM*2*3 in June 2005.  The veteran will be able to click on a “Details” button to see the details of a reminder – comparable to the Clinical Maintenance screens in CPRS and Health Summary. Chapter 10: Women’s Veterans Health Reminders Chapter 10: CPRS: Integration with Women’s Health “It is VHA policy to provide a nationwide tracking system to ensure that consistent mammography and cervical screening follow-up is achieved and that patients have been properly notified of the test results.” (VHA Directive 98-501 dated November 19, 1998) To meet the data requirements of this policy, the Women’s Health (WH) VistA package was developed. However, none of the information contained within the WH software interfaced with CPRS, so the CPRS Integration with Women’s Health project was initiated.  Clinical Reminders patch PXRM*2*1 provides reminders and dialogs that enable CPRS GUI to interface with the Women’s Health package. These reminder dialogs will update the WH package at the same time that clinical care is recorded in CPRS GUI, thus eliminating the need for dual data entry. The exchange of data will enable Clinical Reminders to capture a greater percentage of data than is currently entered into the Women’s Health VistA package, but still allow continuation of Women’s Health Software reporting, tracking, and notification functionality.  Project Goals  Update Pap Smear and Mammogram screening reminders Provide review reminders that store clinical review results in the WH package. Provide dialogs for the screening and review reminders that clinicians can use to document pap smear tests and mammogram procedures. Result in a signed progress note documenting the WH Mammogram- and Pap Smear-related care and patient notifications.  The Mammogram Screening reminder replaces the following national reminders relating to mammograms and breast cancer screening:  VA-*BREAST CANCER SCREEN - rescinded 02/04/2005 VA-MAMMOGRAM - rescinded 02/04/2005  The Pap Screening reminder replaces the following national reminders relating to PAP smears and cervical cancer screening:  VA-*CERVICAL CANCER SCREEN - rescinded 02/04/2005 VA-PAP SMEAR - rescinded 02/04/2005 Chapter 10: Women’s Veterans Health Reminders     NOTE: See the WH Reminders Install and Setup Guide (PXRM_2_1_IG_PDF.) for complete instructions for setting up the WH reminders application. Chapter 10: CPRS: Integration with Women’s Health, cont’d Setup and implementation by local team  Sites will need to determine if the review reminders should be used locally. If a site is not set up for automatic update of WH, these reminders will not come due, so releasing the review reminders and dialogs might be confusing.  The VA-WH PAP SMEAR REVIEW RESULTS reminder will only come due if all of the following are true: PAP smear results are recorded in the VistA Lab package. VistA Lab package uses SNOMED codes. WH package has SNOMED codes mapped to the codes used by the VistA Lab package. WH parameters are set up to automatically receive VistA Lab results when the PAP smear procedure is verified and released. The VA-WH MAMMOGRAM REVIEW RESULTS reminder will only come due if all of the following are true: Mammogram results are recorded and verified in the VistA Radiology package. WH parameters are set up to automatically receive VistA Radiology results when the mammogram procedure is verified and released, and status of received mammogram result is set to OPEN. Chapter 10: Women’s Veterans Health Reminders     NOTE: You can see more information about the guidelines that the reminder is based on by clicking the top checkbox in the dialog. Steps to use dialogs:  On the CPRS cover sheet, click on the Reminders icon. Click on reminders in the Reminders box to see details of a reminder. Open the Notes tab and select New Note. Enter a title. Open the Reminders drawer and review the contents. Locate the Mammogram or Pap reminder you wish to complete (e.g., VA-WH Mammogram Screening) and click to open it. In the dialog box, check relevant actions. Finish the reminder processing. Review the text added to the note to assure its correctness. Ensure that the reminder can be satisfied by the individual finding items that were mapped to the reminder terms.  1. When the Progress Note Properties box opens, type GEC in the Title box. 2. The list of GEC dialog templates is displayed. 3. Select the first one to process.   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### Example: Mammogram Screening Dialog

<!-- image -->

| **Chapter 10: Women’s Veterans Health Reminders**  **The notification letter can be modified at your local site.**   | **Review Results Dialogs**  If your site uses the Women’s Health package, you can review the results of pap smear lab tests or mammogram procedures. You can then send notifications to patients to inform them of the results. The example below shows the Mammogram Review Results dialog and demonstrates sending a notification letter indicating that there is no evidence of malignancy. A follow-up mammogram can be scheduled.   |
|----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Review Results Dialog**

<!-- image -->

**Q:** Are the reminders our site has already defined compatible with the new Clinical Reminders V. 2.0 package?

**A:** Yes, a conversion utility is run when the package is installed that converts your reminders to the new file structure. Some reminders may need slight adjustments to work with the new functionality so if you notice any reminders that don’t seem to be working correctly notify your reminder manager.

**Q:** If orders are included in dialogs and I check these through the Notes tab in CPRS, are the orders actually placed, or is this just recording the intention to order something?

**A:** The order is actually placed, just as if you had ordered through the Orders tab. If the order is set up as a quick order, it will go through immediately (when you click the Finish button); if not a quick order, further questions will be asked to complete the order. The order will still need to be signed.

**Q:** When I click on a reminder to process, I get a message saying “no dialog is defined for this reminder.” What does this mean and what do I need to do?

**A:** See your CAC or Clinical Reminders manager. They need to create and link a dialog for this reminder.

**Q:** What do clinicians need to learn to use Clinical Reminders functionality?

**A:** The most important things to learn will be related to changes in workflow. It will be important to coordinate orders that are placed through reminder dialogs with nurses and clerks. You can work with your CACs and teams to share the responsibility for reminders so that no individual is overwhelmed with reminders. Also, learning to use reports correctly to produce meaningful data will be essential.

**Q:** Is there any way to do a reminder report on an individual finding item?

We want to add a check box that indicates depression is a new diagnosis. Is there a way to do a reminder report just on that one finding that will tell us how many of the patients that were seen that this was applicable for?

**A** : Set up a local reminder with that one finding as a resolution finding.

Define the reminder USAGE field as Reports, and then it will not appear on the cover sheet.

Additional trick:

Make the frequency to be 1 day, and put an OR for the resolution logic and AND for the COHORT logic. That then gives you output in the CM or health summary that gives the date it was last done so not only do you get a list of folks who have the finding but you also can tell when it was entered.

**Q:** When Clinical Maintenance is run on a reminder that is applicable due to a problem list entry, why is today's date pulled rather than the date of problem list entry?

**A:** There are two dates associated with ICD9 diagnoses found in PROBLEM LIST. There is the date entered and the date last modified. The PRIORITY field is used to determine if a problem is chronic or acute. ***If the problem is chronic, Clinical Reminders will use today’s date in its date calculations; otherwise it will use the date last modified.*** Note that it only uses active problems unless the field USE INACTIVE PROBLEMS is yes.

Q: I opened the Reminders Drawer and all my reminders have disappeared, what do I do?

A: Check your View list (Appendix D); most likely nothing will be checked. Select the reminder categories you want displayed and click on them so the checkmark is displayed.

## Appendix A: FAQS, Hints, and Tips

**Q:** I tried to run a report last night, but got this message this morning when I went to look at the task number.

6294955: ^PXRMXPR, Reminder Due Report - print. Device NT\_SPOOL. VAH,ROU.

From Yesterday at 13:14, By you. Created without being scheduled.

Does this mean that there’s an error with the report processing?

A: No, that message doesn’t mean there’s an error. Clinical Reminders processes its reports in two tasks, one for SORT and one for PRINT. The print task will always show “created without being scheduled” until the sort task is complete.

### Tips:

#### Clearing a Single Reminder

You will probably process several reminders for a single visit. If you have entered information on a reminder, but you need to start over on that reminder only, you can click Clear on the reminder from the Reminders Drawer, and then click the Clear button in the Reminders dialog box. This removes all previous dialog selections from the reminder’s dialog box and removes the related text and data from the Progress Note Text box and the PCE data box for this reminder.

You can now start processing again.

NOTE: Clicking Clear will remove the information from only one reminder. Be careful that you are on the correct reminder before you click Clear.

<!-- image -->

#### Canceling Out of the Processing Dialog

If you reach the Reminders processing dialog by mistake or you wish to delete information that you have entered and start over, click Cancel.

<!-- image -->

### Acronyms

AAC	Austin Automation Center

AIMS	Abnormal Involuntary Movement Scale API	Application Programmer Interface.

CAC	Clinical Application Coordinator CNBD	Cannot Be Determined (frequency) CPRS	Computerized Patient Record System. DBIA	Database Integration Agreement.

EPRP	External Peer Review Program

EVS	Enterprise VistA Service

GEC	Geriatric Extended Care

GUI	Graphical User Interface.

HSR&amp;D	Health Services Research and Development HL7	Health Level 7

IHD	Ischemic Heart Disease

LDL	Low-density lipo-protein

MDD	Major Depressive Disorder

MH	Mental Health

MHV	My HealtheVet

OQP	Office of Quality and Performance

PCE	Patient Care Encounter

QUERI	Quality Enhancement Research Initiative SAS	Statistical Analysis System

SQA	Software Quality Assurance

SRS	Software Requirements Specification

TIU	Text Integration Utilities

VHA	Veterans Health Administration. VISN	Veterans Integrated Service Networks. **V** IS *T* **A** Veterans Health Information System and

Technology Architecture.

**National Acronym Directory**

**Definitions**

#### AAC SAS Files

AAC SAS files contain data that is equivalent to data stored in the Reminder Extract Summary entry in the Reminder Extract Summary file. AAC manages SAS files for use by specifically defined users.

#### Applicable

The number of patients whose findings met the patient cohort reminder evaluation.

**CNBD** Cannot Be Determined. If a frequency can’t be determined for a patient, the Status and Due Date will both be CNBD and the frequency display that follows the status line will be “Frequency: Cannot be determined for this patient.”

#### Due

The number of patients whose reminder evaluation status is due.

#### National Database

All sites running IHD and Mental Health QUERI software transmit their data to a compliance totals database at the AAC.

#### Not Applicable

The number of patients whose findings did not meet the patient cohort reminder evaluation.

#### Not Due

The number of patients whose reminder evaluation status is not due.

#### Reminder Definitions

Reminder Definitions comprise the predefined set of finding items used to identify patient cohorts and reminder resolutions. Reminders are used for patient care and/or report extracts.

#### Reminder Dialog

Reminder Dialogs comprise a predefined set of text and findings that together provide information to the CPRS GUI, which collects and updates appropriate findings while building a progress note.

#### Reminder Patient List

A list of patients that is created from a set of List Rules and/or as a result of report processing. Each Patient List is assigned a name and is defined in the Reminder Patient List File. Reminder Patient Lists may be used as an incremental step to completing national extract processing or for local reporting needs. Patient Lists created from the Reminders Due reporting process are based on patients that met the patient cohort, reminder resolution, or specific finding extract parameters. These patient lists are used only at local facilities.

#### Reminder Terms

Predefined finding items that are used to map local findings to national findings, providing a method to standardize these findings for national use.

#### Report Reminders

Reminders may be defined specifically for national reporting. Report Reminders do not have a related Reminder Dialog in CPRS and are not used by clinicians for patient care. However, clinical reminders that are used in CPRS may also be used for national reminder reporting. All reminders targeted for national reporting are defined in Extract Parameters.

You can specify which reminders will appear on the cover sheet of CPRS. This is done by using the Edit Cover Sheet Reminder List option.

1. While on the CPRS Cover Sheet, click on the Tools menu.
2. From the drop-down menu that appears, click on Options. This screen appears:
<!-- image -->

1. Click on the Clinical Reminders button to get to the editing form.

<!-- image -->

1. Highlight an item in the Reminders not being displayed field and then click the Add arrow “&gt;” to add it to the Reminders being displayed field. You may hold down the Control key and select more than one reminder at a time.

1. When you have all of the desired reminders in the field, you may highlight a reminder and use the up and down buttons on the right side of the dialog to change the order in which the reminders will be displayed on the Cover Sheet.

**New Reminders Parameters (** ORQQPX NEW REMINDER PARAMS **)**

If you have been assigned this parameter, you can also modify the reminders view on the coversheet.

1. Click on the reminder button next to the CWAD button in the upper right hand corner of the CPRS GUI.
<!-- image -->

1. Click on Action, then click on Edit Cover Sheet Reminder List.

<!-- image -->

<!-- image -->

This form provides very extensive cover sheet list management capabilities. It consists mainly of three large list areas.

- *Cover Sheet Reminders (Cumulative List)* displays selected information on the Reminders that will be displayed on the Cover Sheet.
- *Available Reminders &amp; Categories* lists all available Reminders and serves as a selection list.
- *User Level Reminders* displays the Reminders that have been added to or removed from the cumulative list.

You may sort the Reminders in *Cover Sheet Reminders (Cumulative List)* by clicking on any of the column headers. Click on the Seq (Sequence) column header to view the Reminders in the order in which they will be displayed on your coversheet.

## Appendix D: VA GEC Referral Reports

VA GEC Reports display the percentage of patients referred to select GEC programs who meet the eligibility criteria as outlined in the Under Secretary for Health’s Information Letter IL 10- 2003-005 and VHA Handbook 1140.2.

VA GEC Reports provide quarterly statistical reports on the following VA-funded programs.

- Homemaker/Home Health Aide, when Funding Source=VA
- Adult Day Health Care, when Funding Source=VA
- VA In-Home Respite, when Funding Source=VA
- Care Coordination, when Funding Source=VA

When sites submit their quarterly reports, the national office will be able to generate a report for the General Accounting Office/Office of Inspector General that demonstrates compliance with the standards for assessing patients prior to placement in VA funded programs.

These same reports can be used at the local level to evaluate how well a site is performing in meeting compliance standards for placement of patients in VA-funded GEC programs.

#### Data Elements for Reporting

- Source
- Living Situation
- Instrumental Activities of Daily Living
- Basic Activities of Daily Living
- Patient Behaviors and Symptoms
- Cognitive Status
- Prognosis
- Age of Patient is 75 years or greater
- Patient Identified as a High Utilizer of Medical Services

#### Implementation Requirements

Local sites must task the job by setting the queue to automatically generate the quarterly reports.

The Office of Geriatric and Extended Care is responsible for importing data received, via electronic email, into a GEC-created excel spreadsheet.

#### New Option

GEC Fiscal Quarterly Rollup [PXRM GEC2 QUARTERLY ROLLUP]

This is a queueable option that will gather and report to Washington DC the Fiscal Quarterly information.

This option should never be placed on an individual’s menu. It should be scheduled for the 8th

day of the first month of the next calendar quarter at any time of the facility’s choosing. The rescheduling frequency should be set to “3M” (every three months).

#### New Mail Group

GEC2 NATIONAL ROLLUP

When this mail group is installed, it will contain the email address of the two individuals in Washington DC who will receive the quarterly data. These names should not be removed. Names of local individuals (for example, CACs) may be added, if they desire to receive these reports.

#### Important Note:

We recommend thorough testing of GEC reminder dialogs by staff prior to implementation to avoid GEC report roll-up inaccuracies. Testing of GEC reminder dialogs and reports in a test account should mimic the actual processes and workload capture used in the site's production environment.

Informatics staff and GEC referral staff should work together to identify potential issues that arise during testing that may require modification of clinical processes and/or workload capture.

Accurate capture and reporting of GEC referral health factors may require careful analysis of workload capture processes at sites that use Event Capture software. Inaccurate reporting may lead to questions from the Inspector General’s office concerning funding for the patients referred to the “Home Help” type of programs.

#### Potential issues if you use Event Capture

(reported by a test site):

1. Event capture does not pass workload to PCE in real time. Data is not passed to PCE until after hours, so this needs to be taken into account when testing.
2. There are several steps where real front-line users could make minor mistakes that would result in data entry/workload not matching up with the Care coordination note.
    1. Event capture date/time must be an exact match to the date/time of PCE/TIU
    2. Clinic location must be the same.
    3. Data passes after hours from EC to PCE.
    4. There is no drop-down menu to select from. 1 and 2 above must be manually entered.
    5. Patient name must be re-selected (or use spacebar return).

**NOTE:** Clinical Reminders Patch 4 (PXRM*2.0*4) contains a few minor changes to GEC Reports, including a new option, Restore or Merge Referrals.

#### GEC Referral Reports Examples

GEC Referral Reports are available on the Reminder Reports menu or on the Reminder Managers menu, depending on how your site has assigned options.

**NOTE:** Option 10 on the GEC Referral Report menu is new with patch PXRM*2.0*4.

#### Types of reports

1. Category
2. Patient
3. Provider by Patient
4. Referral Date
5. Location
6. Referral Count Totals
7. Category-Referred Service
8. Summary (Score)
9. 'Home Help' Eligibility
10. Restore or Merge Referrals

Options 2,3,4,5, named Patient, Provider by Patient, Referral Date, and Location, allow the user to visualize the referral for a patient by different views of the data. They all allow you to narrow the scope to a particular aspect of referral. The Patient view allows you to select a particular patient or several patients. Referral Date allow you to select a particular date range for the Referrals you wish to inquire about. Location refers to the location in the facility that the patient was at during this referral.

You can print the reports in a delimited format, if you wish to export the data to a spreadsheet.

#### Example 1: Category

This option first allows you to select a health factor category or several categories which correlate to different sections of the GEC dialogs. You can then select individual patients or all patients and a date range in order to view the health factors that were added to that patient’s database and Note. It reports both complete and incomplete referrals.

In this example, we picked all categories.

Select Reminder Reports Option: **g** GEC Referral Report All Reports will print on 80 Columns

Select one of the following:

Reminders Due Report Reminders Due Report (User) User Report Templates Extract EPI Totals

Extract EPI List by Finding and SSN Extract QUERI Totals

Review Date Report GEC Referral Report

D R U T L Q V G

Select Reminder Reports Option: ??

1. Category
2. Patient
3. Provider by Patient
4. Referral Date
5. Location
6. Referral Count Totals
7. Category-Referred Service
8. Summary (Score)
9. 'Home Help' Eligibility
10. Restore or Merge Referrals Select Option or ^ to Exit: 7// **1** Category
|   GEC | Referral Categories         |    |                          |
|-------|-----------------------------|----|--------------------------|
|     1 | ADDITIONAL INFO             |  2 | BASIC ADL                |
|     3 | COGNITIVE STATUS            |  4 | COMMENTS                 |
|     5 | CONTINENCE                  |  6 | DIET                     |
|     7 | DOMICILIARY                 |  8 | EQUIPMENT/PROSTHETICS    |
|     9 | EST. DURATION OF SERVICES   | 10 | GERIATRIC SERVICES       |
|    11 | GOALS OF CARE               | 12 | HOME CARE                |
|    13 | HOME TELEHEALTH             | 14 | HOMEBOUND STATUS         |
|    15 | HOSPICE CARE                | 16 | IADL                     |
|    17 | LANGUAGE                    | 18 | LIVING SITUATION         |
|    19 | LIVING SITUATION-WITH WHO   | 20 | NOT REFERRED TO CARE     |
|    21 | NURSING HOME CARE           | 22 | OTHER REFERRAL PROGRAM   |
|    23 | PATIENT BEHAVIORS/SYMPTOM   | 24 | PRIMARY UNPAID CAREGIVER |
|    25 | PROGNOSIS                   | 26 | REFERRING TO             |
|    27 | SERVICES IN THE HOME        | 28 | SKILLED CARE             |
|    29 | SKIN                        | 30 | SOURCE OF REFERRAL       |
|    31 | STRUCTURED LIVING SITUATION | 32 | WEIGHT BEARING           |

Select Categories from the list above using Commas and/or Dashes for ranges of numbers.

Select Categories or ^ to exit:	(1-32): 1-32// **&lt;Enter&gt;**

Select a Beginning Historical Date.

BEGINNING date or ^ to exit:	(1/1/1988 - 4/18/2006): T-600//	(AUG 26, 2004)

Select Ending Date.

ENDING date or ^ to exit:	(8/26/2004 - 4/18/2006): T//	(APR 18, 2006) Select one of the following:

A	All Patients

M	Multiple Patients

Select Patients or ^ to exit: M// ultiple Patients

Select PATIENT NAME:	CRPATIENT,EIGHT	YES	SC VETERAN

Select PATIENT NAME: **&lt;Enter&gt;**

Select one of the following: F	Formatted

D	Delimited

Select Report Format or ^ to exit: F// ormatted DEVICE: HOME//	HOME

==============================================================================

GEC Health Factor Category Detailed Report From: 08/26/2004 To: 04/18/2006

Co mplete and Incomplete Referrals

Category Patient Name

Health Factors	Value	Date

============================================================================== ADDITIONAL INFO

CRPATIENT,EIGHT (000000008)

| GEC ADVANCE DIRECTIVE                                         | NO   | 04/11/2005             |
|---------------------------------------------------------------|------|------------------------|
| GEC BETTER OTHER LIVING ENVIRONMENT                           | NO   | 04/11/2005             |
| GEC DIFFICULT TO ENTER/LEAVE HOME                             | NO   | 04/11/2005             |
| GEC DPOA FINANCIAL  Comment: HKJHK  GEC FIDUCIARY/CONSERVATOR |      | 04/11/2005  04/11/2005 |

Comment: JKLJL

GEC GUARDIAN	04/11/2005

Comment: L;';L

| GEC LEFT ALONE LAST 7D             | NO   | 04/11/2005   |
|------------------------------------|------|--------------|
| GEC OTHERS MOVED IN W/PT LAST 90D  | NO   | 04/11/2005   |
| GEC PHYSICAL ACTIVITY 2HRS LAST 7D | NO   | 04/11/2005   |

DOMICILIARY

CRPATIENT,EIGHT (000000008)

GEC DOMICILIARY FUNDING-VA	04/11/2005

GEC VA DOMICILIARY (REFERRED TO)	04/11/2005 EST. DURATION OF SERVICES

CRPATIENT,EIGHT (000000008)

GEC ONE WEEK OR LESS	04/11/2005 GOALS OF CARE

CRPATIENT,EIGHT (000000008)

GEC IMPROVE COMPLIANCE MEDS/TREATMENTS	04/11/2005 GEC MONITORING TO AVOID COMPLICATIONS	04/11/2005

HOME CARE

CRPATIENT,EIGHT (000000008)

| GEC COMMUNITY SKILLED HOME HEALTH                                               | GEC COMMUNITY SKILLED HOME HEALTH   | CARE   | 04/11/2005   | 04/11/2005   |
|---------------------------------------------------------------------------------|-------------------------------------|--------|--------------|--------------|
| GEC HOME BASED PR. CARE (REFERRED                                               | GEC HOME BASED PR. CARE (REFERRED   | TO)    | 04/11/2005   | 04/11/2005   |
| GEC HOMECARE FUNDING-VA                                                         | GEC HOMECARE FUNDING-VA             |        | 04/11/2005   | 04/11/2005   |
| GEC HOMECARE FUNDING-VA                                                         | GEC HOMECARE FUNDING-VA             |        | 07/14/2005   | 07/14/2005   |
| GEC HOMEMAKER/HOME HEALTH AIDE                                                  | GEC HOMEMAKER/HOME HEALTH AIDE      |        | 04/11/2005   | 04/11/2005   |
| GEC HOMEMAKER/HOME HEALTH AIDE                                                  | GEC HOMEMAKER/HOME HEALTH AIDE      |        | 07/14/2005   | 07/14/2005   |
| HOMEBOUND STATUS CRPATIENT,EIGHT (000000008)  GEC HOMEBOUND	NO	04/11/2005  IADL |                                     |        |              |              |
| CRPATIENT,EIGHT                                                                 | (000000008)                         |        |              |              |
| GEC DIFFICULT                                                                   | TRANSPORTATION/LAST                 | 7D     | NO           | 04/11/2005   |

| GEC             | DIFFICULTY MANAGING MEDS/LAST 7D   | DIFFICULTY MANAGING MEDS/LAST 7D   | NO         | 04/11/2005   |
|-----------------|------------------------------------|------------------------------------|------------|--------------|
| GEC             | DIFFICULTY MNG FINANCES/LAST 7D    | DIFFICULTY MNG FINANCES/LAST 7D    | NO         | 04/11/2005   |
| GEC             | DIFFICULTY PREPARE MEALS/LAST 7D   | DIFFICULTY PREPARE MEALS/LAST 7D   | NO         | 04/11/2005   |
| GEC             | DIFFICULTY PREPARE MEALS/LAST 7D   | DIFFICULTY PREPARE MEALS/LAST 7D   | YES        | 04/11/2005   |
| GEC             | DIFFICULTY USING PHONE/LAST 7D     | DIFFICULTY USING PHONE/LAST 7D     | NO         | 04/11/2005   |
| GEC             | DIFFICULTY W/ HOUSEWORK/LAST 7D    | DIFFICULTY W/ HOUSEWORK/LAST 7D    | NO         | 04/11/2005   |
| GEC             | DIFFICULTY WITH SHOPPING/LAST 7D   | DIFFICULTY WITH SHOPPING/LAST 7D   | NO         | 04/11/2005   |
| GEC             | MEALS PREPARED BY OTHERS/LAST 7D   | MEALS PREPARED BY OTHERS/LAST 7D   | NO         | 04/11/2005   |
| GEC             | MEALS PREPARED BY OTHERS/LAST 7D   | MEALS PREPARED BY OTHERS/LAST 7D   | YES        | 04/11/2005   |
| GEC             | RECENT CHANGE IN IADL RX           | RECENT CHANGE IN IADL RX           | NO         | 04/11/2005   |
| LANGUAGE        | LANGUAGE                           | LANGUAGE                           | LANGUAGE   | LANGUAGE     |
| CRPATIENT,EIGHT | CRPATIENT,EIGHT                    | (000000008)                        |            |              |
| GEC ENGLISH     | GEC ENGLISH                        |                                    | 04/11/2005 | 04/11/2005   |
| GEC SPANISH     | GEC SPANISH                        |                                    | 04/11/2005 | 04/11/2005   |

LIVING SITUATION CRPATIENT,EIGHT (000000008)

GEC BOARD AND CARE/ASSISTED LIVING	04/11/2005

GEC DOMICILIARY	04/11/2005

LIVING SITUATION-WITH WHO CRPATIENT,EIGHT (000000008)

GEC ALONE	04/11/2005

PRIMARY UNPAID CAREGIVER CRPATIENT,EIGHT (000000008)

GEC NO CAREGIVER	04/11/2005

REFERRING TO

CRPATIENT,EIGHT (000000008)

GEC ADL ASSISTANCE IN HOME	04/11/2005

GEC SKILLED CARE IN HOME	04/11/2005 SERVICES IN THE HOME

CRPATIENT,EIGHT (000000008)

| GEC HOME HEALTH AIDE/LAST 14D   |     | NO   | 04/11/2005   |
|---------------------------------|-----|------|--------------|
| GEC RN HOME VISIT(T+/-30D)      |     | NO   | 04/11/2005   |
| GEC SOCIAL WORK ASSISTANCE/LAST | 14D | NO   | 04/11/2005   |

SOURCE OF REFERRAL CRPATIENT,EIGHT (000000008)

GEC OUTPATIENT CLINIC	04/11/2005

Enter RETURN to continue or '^' to exit:

#### Example 2: Patient

This option lets you pick one or more patients for a specified date range. It then prints a report of all the referral information for each patient. Select Multiple Patients, if you wish to enter individual patient names. Otherwise, select All Patients.

This option reports by complete referrals only.

==============================================================================

Select Report Format or ^ to exit: F// **&lt;Enter&gt;** ormatted DEVICE: HOME// **;;999** HOME

Formatted Delimited

F D

Select Patients or ^ to exit: M// **&lt;Enter&gt;** ultiple Patients

Select PATIENT NAME: **CRPATIENT,EIGHT** ,CRPATIENT,EIGHT	CRPATIENT,EIGHT

Select PATIENT NAME: **&lt;Enter&gt;**

Select a Beginning Historical Date.

BEGINNING date or ^ to exit: (1/1/1988 - 4/18/2006): t-365// **&lt;Enter&gt;** (APR 18, 2005)

Select Ending Date.

ENDING date or ^ to exit:	(4/18/2005 - 4/18/2006): T// **&lt;Enter&gt;** (APR 18, 2006)

Select one of the following:

All Patients Multiple Patients

A M

Select Option or ^ to Exit: **2** Patient

Select one of the following:

Category Patient

Provider by Patient Referral Date Location

Referral Count Totals Category-Referred Service Summary (Score)

'Home Help' Eligibility Restore or Merge Referrals

1

2

3

4

5

6

7

8

9

10

Select Reminder Reports Option:	GEC Referral Report All Reports will print on 80 Columns

Select one of the following:

GEC Patient

From: 04/18/2005 To: 04/18/2006

Patient Category

Health Factor	Value	Date of Evaluation

==============================================================================

1) OUTPATIENT

1. CRPATIENT,EIGHT (000000008)	Total # Complete referrals: 4

Referral #1 ADDITIONAL INFO

GEC GUARDIAN	04/11/2005

Comment: L;';L HOME CARE

GEC HOME BASED PR. CARE (REFERRED TO)	04/11/2005 IADL

| GEC DIFFICULTY PREPARE MEALS/LAST                       | 7D                     | YES   | 04/11/2005   |
|---------------------------------------------------------|------------------------|-------|--------------|
| GEC MEALS PREPARED BY OTHERS/LAST                       | 7D                     | YES   | 04/11/2005   |
| LANGUAGE  GEC ENGLISH LIVING SITUATION  GEC DOMICILIARY | 04/11/2005  04/11/2005 |       |              |

Referral #2 HOME CARE

GEC COMMUNITY SKILLED HOME HEALTH CARE	04/11/2005 REFERRING TO

GEC SKILLED CARE IN HOME	04/11/2005

Referral #3 ADDITIONAL INFO

| GEC BETTER OTHER LIVING ENVIRONMENT   | GEC BETTER OTHER LIVING ENVIRONMENT   | NO         | 04/11/2005   |
|---------------------------------------|---------------------------------------|------------|--------------|
| GEC DIFFICULT TO ENTER/LEAVE HOME     | GEC DIFFICULT TO ENTER/LEAVE HOME     | NO         | 04/11/2005   |
| GEC LEFT ALONE LAST 7D                | GEC LEFT ALONE LAST 7D                | NO         | 04/11/2005   |
| GEC OTHERS MOVED IN W/PT LAST 90D     | GEC OTHERS MOVED IN W/PT LAST 90D     | NO         | 04/11/2005   |
| GEC PHYSICAL ACTIVITY 2HRS LAST 7D    | GEC PHYSICAL ACTIVITY 2HRS LAST 7D    | NO         | 04/11/2005   |
| GEC ADVANCE DIRECTIVE                 | GEC ADVANCE DIRECTIVE                 | NO         | 04/11/2005   |
| GEC DPOA FINANCIAL                    | GEC DPOA FINANCIAL                    |            | 04/11/2005   |
| Comment: HKJHK                        | Comment: HKJHK                        |            |              |
| GEC FIDUCIARY/CONSERVATOR             | GEC FIDUCIARY/CONSERVATOR             |            | 04/11/2005   |
| Comment: JKLJL DOMICILIARY            | Comment: JKLJL DOMICILIARY            |            |              |
| GEC DOMICILIARY FUNDING-VA            |                                       | 04/11/2005 | 04/11/2005   |
| GEC VA DOMICILIARY (REFERRED          | TO)                                   | 04/11/2005 | 04/11/2005   |
| EST. DURATION OF SERVICES             |                                       |            |              |
| GEC ONE WEEK OR LESS                  |                                       | 04/11/2005 | 04/11/2005   |

GOALS OF CARE

GEC MONITORING TO AVOID COMPLICATIONS	04/11/2005

GEC IMPROVE COMPLIANCE MEDS/TREATMENTS	04/11/2005 HOME CARE

| GEC HOMECARE FUNDING-VA                                   |                                      |    | 04/11/2005             |
|-----------------------------------------------------------|--------------------------------------|----|------------------------|
| GEC HOMEMAKER/HOME HEALTH HOMEBOUND STATUS  GEC HOMEBOUND | AIDE                                 | NO | 04/11/2005  04/11/2005 |
| IADL  GEC DIFFICULT TRANSPORTATION/LAST 7D                |                                      | NO | 04/11/2005             |
| GEC DIFFICULTY MANAGING MEDS/LAST 7D                      | GEC DIFFICULTY MANAGING MEDS/LAST 7D | NO | 04/11/2005             |
| GEC DIFFICULTY MNG FINANCES/LAST 7D                       | GEC DIFFICULTY MNG FINANCES/LAST 7D  | NO | 04/11/2005             |
| GEC DIFFICULTY USING PHONE/LAST 7D                        | GEC DIFFICULTY USING PHONE/LAST 7D   | NO | 04/11/2005             |
| GEC DIFFICULTY W/ HOUSEWORK/LAST 7D                       | GEC DIFFICULTY W/ HOUSEWORK/LAST 7D  | NO | 04/11/2005             |
| GEC DIFFICULTY WITH SHOPPING/LAST 7D                      | GEC DIFFICULTY WITH SHOPPING/LAST 7D | NO | 04/11/2005             |
| GEC RECENT CHANGE IN IADL RX                              | GEC RECENT CHANGE IN IADL RX         | NO | 04/11/2005             |

| GEC DIFFICULTY PREPARE MEALS/LAST 7D                                                                                                                                                                                                                                               | GEC DIFFICULTY PREPARE MEALS/LAST 7D     | GEC DIFFICULTY PREPARE MEALS/LAST 7D     | NO         | 04/11/2005   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|------------------------------------------|------------|--------------|
| GEC MEALS PREPARED BY OTHERS/LAST 7D                                                                                                                                                                                                                                               | GEC MEALS PREPARED BY OTHERS/LAST 7D     | GEC MEALS PREPARED BY OTHERS/LAST 7D     | NO         | 04/11/2005   |
| LANGUAGE  GEC SPANISH	04/11/2005  LIVING SITUATION  GEC BOARD AND CARE/ASSISTED LIVING	04/11/2005 LIVING SITUATION-WITH WHO  GEC ALONE	04/11/2005  PRIMARY UNPAID CAREGIVER  GEC NO CAREGIVER	04/11/2005  REFERRING TO  GEC ADL ASSISTANCE IN HOME	04/11/2005 SERVICES IN THE HOME |                                          |                                          |            |              |
| GEC HOME HEALTH AIDE/LAST 14D                                                                                                                                                                                                                                                      | GEC HOME HEALTH AIDE/LAST 14D            |                                          | NO         | 04/11/2005   |
| GEC RN HOME VISIT(T+/-30D)                                                                                                                                                                                                                                                         | GEC RN HOME VISIT(T+/-30D)               |                                          | NO         | 04/11/2005   |
| GEC SOCIAL WORK ASSISTANCE/LAST                                                                                                                                                                                                                                                    | GEC SOCIAL WORK ASSISTANCE/LAST          | 14D                                      | NO         | 04/11/2005   |
| SOURCE OF REFERRAL  GEC OUTPATIENT CLINIC  Referral #4 HOME CARE                                                                                                                                                                                                                   |                                          |                                          |            | 04/11/2005   |
| GEC HOMECARE FUNDING-VA                                                                                                                                                                                                                                                            |                                          | 07/14/2005                               | 07/14/2005 | 07/14/2005   |
| GEC HOMEMAKER/HOME HEALTH                                                                                                                                                                                                                                                          | AIDE                                     | 07/14/2005                               | 07/14/2005 | 07/14/2005   |
| Enter RETURN to continue or '^' to exit:                                                                                                                                                                                                                                           | Enter RETURN to continue or '^' to exit: | Enter RETURN to continue or '^' to exit: |            |              |

#### Example 3: Referral by Provider – All Providers

This option lets you pick one or more providers for a specified date range. It then prints a report of all the referral information for all of the referred patients for designated providers. Select Multiple Providers, if you wish to enter individual provider names. Otherwise, select All Providers.

This report displays counts of complete referrals only

| Select one of the following:  1. Category 2. Patient 3. Provider by Patient 4. Referral Date 5. Location 6. Referral Count Totals 7. Category-Referred Service 8. Summary (Score) 9. 'Home Help' Eligibility 10. Restore or Merge Referrals  Select Option or ^ to Exit: 1// 3	Provider by Patient Select one of the following:  A	All Providers  M	Multiple Providers Enter response: M// All Providers  Select a Beginning Historical Date.  BEGINNING date or ^ to exit:	(1/1/1988 - 4/19/2006): T-600//	(AUG 27, 2004)  Select Ending Date.  ENDING date or ^ to exit:	(8/27/2004 - 4/19/2006): T//	(APR 19, 2006) Select one of the following:  F	Formatted  D	Delimited  Select Report Format or ^ to exit: F// ormatted DEVICE: HOME// ;;999	HOME  ==============================================================================  GEC Provider  From: 08/27/2004 To: 04/19/2006  Report Displays Counts of Complete Referrals Only Provider  Patient	Completion Date	Dialog  ==============================================================================  CRPROVIDER,EIGHT (253)  CRPATIENT,THREE (000000003) (1 Evaluation(s) )   |                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| 02/10/2005                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | CARE COORDINATION  |
| 02/10/2005                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | SOCIAL SERVICES    |
| 02/10/2005                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | NURSING ASSESSMENT |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                    |

02/10/2005	CARE RECOMMENDATION CRPATIENT,FIVE (000000005) (1 Evaluation(s) )

01/31/2005	CARE COORDINATION

01/31/2005	SOCIAL SERVICES

01/31/2005	NURSING ASSESSMENT

01/31/2005	CARE RECOMMENDATION CRPATIENT,FOURTEEN (000000014) (2 Evaluation(s) )

01/27/2005	CARE COORDINATION

01/28/2005	CARE COORDINATION

01/28/2005	SOCIAL SERVICES

01/28/2005	NURSING ASSESSMENT

01/28/2005	CARE RECOMMENDATION PATIENT,CHRONIC (333448888) (1 Evaluation(s) )

02/10/2005	CARE COORDINATION

02/10/2005	SOCIAL SERVICES

02/10/2005	NURSING ASSESSMENT

02/10/2005	CARE RECOMMENDATION CRPATIENT,FOUR (000000004) (1 Evaluation(s) )

01/28/2005	CARE COORDINATION

01/28/2005	SOCIAL SERVICES

01/28/2005	NURSING ASSESSMENT

01/28/2005	CARE RECOMMENDATION CRPATIENT,ONE (666112222) (1 Evaluation(s) )

01/31/2005	CARE COORDINATION

01/31/2005	SOCIAL SERVICES

01/31/2005	NURSING ASSESSMENT

01/31/2005	CARE RECOMMENDATION

CRPROVIDER,ONE (1114)

CRPATIENT,TWO (000000002) (1 Evaluation(s) )

01/27/2005	CARE COORDINATION

01/27/2005	SOCIAL SERVICES CRPATIENT,EIGHT (000000008) (4 Evaluation(s) )

06/16/2005	CARE COORDINATION

06/16/2005	SOCIAL SERVICES

06/17/2005	CARE COORDINATION

06/17/2005	CARE RECOMMENDATION

06/28/2005	CARE COORDINATION

06/28/2005	SOCIAL SERVICES

06/28/2005	CARE RECOMMENDATION

07/14/2005	CARE COORDINATION CRPATIENT,FOUR (000000004) (1 Evaluation(s) )

06/17/2005	CARE COORDINATION

06/17/2005	CARE RECOMMENDATION CRPROVIDER,THIRTEEN (123456789066)

CRPATIENT,SIX (666042591P) (1 Evaluation(s) )

03/28/2005	CARE COORDINATION

03/28/2005	SOCIAL SERVICES

03/28/2005	NURSING ASSESSMENT

03/28/2005	CARE RECOMMENDATION

CRPROVIDER,TEN (123456789068)

CRPATIENT,EIGHT (000000008) (1 Evaluation(s) )

06/16/2005	SOCIAL SERVICES

06/16/2005	NURSING ASSESSMENT

06/16/2005	CARE RECOMMENDATION CRUPATIENT,TEN (123121234) (1 Evaluation(s) )

03/28/2005	CARE COORDINATION

03/28/2005	SOCIAL SERVICES

03/28/2005	NURSING ASSESSMENT

03/28/2005	CARE RECOMMENDATION

Enter RETURN to continue or '^' to exit:

Select one of the following:

1. Category
2. Patient
3. Provider by Patient
4. Referral Date
5. Location
6. Referral Count Totals
7. Category-Referred Service
8. Summary (Score)
9. 'Home Help' Eligibility
10. Restore or Merge Referrals

Select Option or ^ to Exit: 3//	Provider by Patient

Select one of the following:

A	All Providers

M	Multiple Providers

Enter response: A// Multiple Providers

Select NEW PERSON NAME: CRPROVIDER,ONE		OC Select NEW PERSON NAME: CRPROVIDER,TEN	TC Select NEW PERSON NAME:

Select a Beginning Historical Date.

BEGINNING date or ^ to exit:	(1/1/1988 - 4/19/2006): T-600//	(AUG 27, 2004)

Select Ending Date.

ENDING date or ^ to exit:	(8/27/2004 - 4/19/2006): T//	(APR 19, 2006)

Select one of the following:

F	Formatted

D	Delimited

Select Report Format or ^ to exit: F// ormatted DEVICE: HOME//	HOME

==============================================================================

GEC Provider

From: 08/27/2004 To: 04/19/2006

Report Displays Counts of Complete Referrals Only Provider

Patient	Completion Date	Dialog

==============================================================================

CRPROVIDER,ONE (1114)

CRPATIENT,TWO (000000002) (1 Evaluation(s) )

01/27/2005	CARE COORDINATION

01/27/2005	SOCIAL SERVICES CRPATIENT,EIGHT (000000008) (4 Evaluation(s) )

06/16/2005	CARE COORDINATION

NURSING ASSESSMENT CARE RECOMMENDATION

CARE COORDINATION SOCIAL SERVICES

CRPATIENT,TEN (666121234) (1 Evaluation(s) )

03/28/2005

03/28/2005

03/28/2005

03/28/2005

Enter RETURN to continue or '^' to exit:

Enter RETURN to continue or '^' to exit:

06/16/2005	SOCIAL SERVICES

06/17/2005	CARE COORDINATION

06/17/2005	CARE RECOMMENDATION

06/28/2005	CARE COORDINATION

06/28/2005	SOCIAL SERVICES

06/28/2005	CARE RECOMMENDATION

07/14/2005	CARE COORDINATION CRPATIENT,FOUR (000000004) (1 Evaluation(s) )

06/17/2005	CARE COORDINATION

06/17/2005	CARE RECOMMENDATION CRPROVIDER,TEN (123456789068)

CRPATIENT,EIGHT (000000008) (1 Evaluation(s) )

06/16/2005	SOCIAL SERVICES

06/16/2005	NURSING ASSESSMENT

06/16/2005	CARE RECOMMENDATION

#### Example 4: Referral Date

The Referral Date option lets you specify a particular date range as well as incomplete referrals, completed referrals, or both.

| 06/28/2005                                                                                                       | 06/28/2005   | 1 Days   | 1 Days        |            |
|------------------------------------------------------------------------------------------------------------------|--------------|----------|---------------|------------|
| 06/30/2005                                                                                                       |              | 294 Days | 294 Days      | Incomplete |
| 07/14/2005                                                                                                       | 07/14/2005   | 1 Days   | 1 Days        |            |
| CRPATIENT,FIVE (000000005)		1 Referral(s) 01/31/2005	01/31/2005	1 Days  CRPATIENT,FOUR (000000004)	2 Referral(s) |              |          |               |            |
| 01/28/2005                                                                                                       | 01/28/2005   | 1        | Days          | Days       |
| 06/17/2005                                                                                                       | 06/17/2005   | 1        | Days          | Days       |
| CRPATIENT,FOURTEEN (000000014)                                                                                   |              |          | 4 Referral(s) |            |
| 01/27/2005                                                                                                       | 01/27/2005   | 1        | Days          |            |
| 01/27/2005                                                                                                       |              | 448 Days | 448 Days      | Incomplete |
| 01/27/2005                                                                                                       | 01/27/2005   | 1 Days   | 1 Days        |            |
| 01/28/2005                                                                                                       | 01/28/2005   | 1 Days   | 1 Days        |            |
| CRPATIENT,THREE (000000003)                                                                                      |              |          | 2 Referral(s) |            |
| 01/27/2005                                                                                                       |              | 448 Days |               | Incomplete |
| 02/10/2005                                                                                                       | 02/10/2005   | 1 Days   | 1 Days        |            |

#### Example 5: Location

This option lets you print a report on patients by locations in the facility that the patient was at during this referral.

Select one of the following:

1. Category
2. Patient
3. Provider by Patient
4. Referral Date
5. Location
6. Referral Count Totals
7. Category-Referred Service
8. Summary (Score)
9. 'Home Help' Eligibility
10. Restore or Merge Referrals Select Option or ^ to Exit: 4// **5** Location

Select one of the following:

A	All Locations

S	Single Location Enter response: **A** ll Locations

Select a Beginning Historical Date.

BEGINNING date or ^ to exit:	(1/1/1988 - 4/19/2006): T-600//	(AUG 27, 2004)

Select Ending Date.

ENDING date or ^ to exit:	(8/27/2004 - 4/19/2006): T//	(APR 19, 2006)

Select one of the following:

F	Formatted

D	Delimited

Select Report Format or ^ to exit: F// ormatted DEVICE: HOME//	HOME

==============================================================================

Complete GEC Referrals by Location From: 08/27/2004 To: 04/19/2006

Location

Patient	Finish Date

==============================================================================

1 CRPROVIDER,ONE'S CLINIC	Total # Patients Evaluated= 5

| CRPATIENT,TEN	(123121234)   | 03/28/2005   |
|-----------------------------|--------------|
| CRPATIENT,EIGHT	(000000008) | 06/16/2005   |
| CRPATIENT,EIGHT	(000000008) | 06/17/2005   |
| CRPATIENT,EIGHT	(000000008) | 06/28/2005   |
| CRPATIENT,FOUR	(000000004)  | 01/28/2005   |

1A(1&amp;2)

Total # Patients Evaluated= 3

| CRPATIENT,FIVE	(000000005)                                                                                                                                                                                                                                                                                                                                                                     | 01/31/2005   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| CRPATIENT,FOURTEEN	(000000014)                                                                                                                                                                                                                                                                                                                                                                 | 01/27/2005   |
| CRPATIENT,FOURTEEN	(000000014)                                                                                                                                                                                                                                                                                                                                                                 | 01/28/2005   |
| 2B MED		Total # Patients Evaluated= 2 CRPATIENT,THREE	(000000003)	02/10/2005  CRPATIENT,TWO	(000000002)	01/27/2005  CARDIOLOGY		Total # Patients Evaluated= 1 GECPATIENT,TEN	(666233242)	02/08/2005  DIABETIC EDUCATION-INDIV-MOD BTotal # Patients Evaluated= 1 GECPATIENT,ONE	(666207282)	02/08/2005  GENERAL MEDICINE	Total # Patients Evaluated= 4  CRPATIENT,EIGHT	(666211234)	02/09/2005 |              |
| CRPATIENT,FIVE (666189600)                                                                                                                                                                                                                                                                                                                                                                     | 02/10/2005   |
| CRPATIENT,NINE (666886636)                                                                                                                                                                                                                                                                                                                                                                     | 02/09/2005   |
| CRPATIENT,ONE (666993242)                                                                                                                                                                                                                                                                                                                                                                      | 02/10/2005   |
| CRPATIENT,SEVEN (666388333)                                                                                                                                                                                                                                                                                                                                                                    | 02/16/2005   |
| CRPATIENT,SIX (666223220)                                                                                                                                                                                                                                                                                                                                                                      | 02/08/2005   |
| CRPATIENT,SIXTEEN(666223220)                                                                                                                                                                                                                                                                                                                                                                   | 02/10/2005   |
| CRPATIENT,TEN(666233242)                                                                                                                                                                                                                                                                                                                                                                       | 02/10/2005   |
| CRPATIENT,TWENTY (666448888)                                                                                                                                                                                                                                                                                                                                                                   | 02/10/2005   |

SALT LAKE OEX SALT LAKE OEX SALT LAKE OEX

10	Restore or Merge Referrals

Select Option or ^ to Exit: 2// **6** Referral Count Totals

Select one of the following: PA	Patient

PR	Provider

L	Location

D	Date

Select Sort Type or ^ to exit: **PA** Patient Select a Beginning Historical Date.

BEGINNING date or ^ to exit:	(1/1/1988 - 4/18/2006): t-365// **T-60** 0 (AUG 26, 2004)

Select Ending Date.

ENDING date or ^ to exit:	(8/26/2004 - 4/18/2006): T// **&lt;Enter&gt;** (APR 18, 2006)

Select one of the following: F	Formatted

D	Delimited

Select Report Format or ^ to exit: F// ormatted DEVICE: HOME// **;;999** HOME

==============================================================================

Referral Count by Patient

From: 08/26/2004 To: 04/18/2006

Report Displays Counts of Complete Referrals Only

Patient	SSN	Total Count	Division

==============================================================================

1. CRPATIENT,EIGHT 000000008
2. CRPATIENT,FIVE	000000005
3. CRPATIENT,FOUR	000000004
4. CRPATIENT,FOURTEEN000000014
5. CRPATIENT,THREE 000000003

OUTPATIENT

1

666112222

OUTPATIENT INPATIENT OUTPATIENT INPATIENT INPATIENT INPATIENT

4

1

2

3

1

1

000000002

This report allows you to create a report that counts the number of Complete referrals done during a time period selected by the user. You can select the counting to be done by Patient Name, Provider, Hospital Location, or for a certain date range. This should be useful for giving reports to other users of the system.

Select one of the following:

1

2

3

4

5

6

7

8

9

Category Patient

Provider by Patient Referral Date Location

Referral Count Totals Category-Referred Service Summary (Score)

'Home Help' Eligibility

The Category-Referred Service is a subset of the first option. It allows you to look at the health factors based on where the patient had been referred to. So if a user would like to view all of the patients that were referred to HOME TELEHEALTH, this is one way to get that information.

GEC Referral Service Categories

Select Categories from the list above using Commas and/or Dashes for ranges of numbers. Select Categories or ^ to exit:	(1-9): 1-9//

Select a Beginning Historical Date.

BEGINNING date or ^ to exit:	(1/1/1988 - 4/19/2006): T-300//	(JUN 23, 2005)

Select Ending Date.

ENDING date or ^ to exit:	(6/23/2005 - 4/19/2006): T// ^

Select a Beginning Historical Date.

BEGINNING date or ^ to exit:	(1/1/1988 - 4/19/2006): T-300// T-600	(AUG 27, 2004)

Select Ending Date.

ENDING date or ^ to exit:	(8/27/2004 - 4/19/2006): T//	(APR 19, 2006)

Select one of the following:

A M

All Patients Multiple Patients

Select Patients or ^ to exit: A// ll Patients

Select one of the following:

F D

Formatted Delimited

Select Report Format or ^ to exit: F// ormatted DEVICE: HOME// ;;999	HOME

GEC Health Factor Category Detailed Report From: 08/27/2004 To: 04/19/2006

Complete and Incomplete Referrals Category

Patient Name

Health Factors	Date

============================================================================== DOMICILIARY

**CRPATIENT,EIGHT** (000000008)

GEC DOMICILIARY FUNDING-VA	01/27/2005

GEC STATE HOME DOMICILIARY	01/27/2005

**CRPATIENT,FIVE	(000000005)**

| GEC DOMICILIARY FUNDING-VA   | 01/27/2005   |
|------------------------------|--------------|
| GEC DOMICILIARY FUNDING-VA   | 01/27/2005   |
| GEC DOMICILIARY FUNDING-VA   | 01/27/2005   |
| GEC DOMICILIARY FUNDING-VA   | 01/27/2005   |
| GEC VA DOMICILIARY           | 01/27/2005   |
| GEC VA DOMICILIARY           | 01/27/2005   |
| GEC VA DOMICILIARY           | 01/27/2005   |
| GEC VA DOMICILIARY           | 01/27/2005   |

CRPATIENT,FOUR (000000004)

GEC DOMICILIARY FUNDING-VA	01/28/2005

GEC VA DOMICILIARY	01/28/2005

GERIATRIC SERVICES CRPATIENT,FIVE (000000005)

| GEC GERI SERVICES FUNDING-VA      |                                   | 01/31/2005   | 01/31/2005   |
|-----------------------------------|-----------------------------------|--------------|--------------|
| GEC GERIATRIC EVAL/MGMT INPT      | UNIT                              | 01/31/2005   | 01/31/2005   |
| CRPATIENT,ONE (666442222)         |                                   |              |              |
| GEC GERI SERVICES FUNDING-VA      |                                   |              | 02/08/2005   |
| GEC GERIATRIC EVAL/MGMT INPT UNIT | GEC GERIATRIC EVAL/MGMT INPT UNIT |              | 02/08/2005   |
| CRPATIENT,THREE (000000003)       | CRPATIENT,THREE (000000003)       |              |              |
| GEC ADULT DAY HEALTH CARE         | GEC ADULT DAY HEALTH CARE         |              | 10/22/2001   |
| GEC HOMECARE FUNDING-VA           | GEC HOMECARE FUNDING-VA           |              | 10/22/2001   |
| CRPATIENT,TWO (000000002)         | CRPATIENT,TWO (000000002)         |              |              |
| GEC HOMECARE FUNDING-VA           | GEC HOMECARE FUNDING-VA           |              | 01/27/2005   |
| GEC VA IN-HOME RESPITE            | GEC VA IN-HOME RESPITE            |              | 01/27/2005   |
| CRPATIENT,EIGHT (000000008)       | CRPATIENT,EIGHT (000000008)       |              |              |
| GEC COMMUNITY SKILLED HOME HEALTH | GEC COMMUNITY SKILLED HOME HEALTH | CARE         | 04/11/2005   |
| GEC HOME BASED PR. CARE           | GEC HOME BASED PR. CARE           |              | 04/11/2005   |
| GEC HOMECARE FUNDING-VA           | GEC HOMECARE FUNDING-VA           |              | 04/11/2005   |
| GEC HOMECARE FUNDING-VA           | GEC HOMECARE FUNDING-VA           |              | 07/14/2005   |
| GEC HOMEMAKER/HOME HEALTH AIDE    | GEC HOMEMAKER/HOME HEALTH AIDE    |              | 04/11/2005   |
| GEC HOMEMAKER/HOME HEALTH AIDE    | GEC HOMEMAKER/HOME HEALTH AIDE    |              | 07/14/2005   |

WHPATIENT,FEMALEFOURTEEN (000000014)

| GEC ADULT DAY HEALTH CARE      | 01/28/2005   |
|--------------------------------|--------------|
| GEC HOMECARE FUNDING-VA        | 01/27/2005   |
| GEC HOMECARE FUNDING-VA        | 01/28/2005   |
| GEC HOMEMAKER/HOME HEALTH AIDE | 01/27/2005   |

CRPATIENT,ELEVEN (333448888)

GEC ADULT DAY HEALTH CARE	02/10/2005

GEC HOMECARE FUNDING-VA	02/10/2005 CRPATIENT,ONE (666112222)

GEC HOMECARE FUNDING-VA	01/31/2005

GEC VA IN-HOME RESPITE	01/31/2005 HOME TELEHEALTH

CRPATIENT,FOURTEEN (000000014)

| GEC HOME TELEHEALTH       | 01/27/2005   |
|---------------------------|--------------|
| GEC HOME TELEHEALTH       | 01/27/2005   |
| GEC TELEHEALTH FUNDING-VA | 01/27/2005   |
| GEC TELEHEALTH FUNDING-VA | 01/27/2005   |

WHPATIENT,FEMALEFOUR (000000004)

GEC HOME TELEHEALTH	06/17/2005

GEC TELEHEALTH FUNDING-VA	06/17/2005 HOSPICE CARE

CRPATIENT,TEN (666121234)

GEC HOSPICE FUNDING-MEDICARE	03/28/2005

GEC VA OUTPATIENT HOSPICE	03/28/2005 NOT REFERRED TO CARE

CRPATIENT,FOURTEEN (000000014)

GEC DOES NOT MEET CRITERIA	01/27/2005 NURSING HOME CARE

CRPATIENT,TWENTY (666211234)

GEC NURSING HOME FUNDING-VA	02/03/2005

GEC STATE VETERANS NURSING HOME	02/03/2005 STRUCTURED LIVING SITUATION

CRPATIENT,FIVE (000000005)

GEC ASSISTED LIVING	01/31/2005

GEC STRUCTURED LIVING FUNDING-VA	01/31/2005 CRPATIENT,FOUR (000000004)

GEC ASSISTED LIVING	06/17/2005

GEC STRUCTURED LIVING FUNDING-OTHER INS.	06/17/2005

Enter RETURN to continue or '^' to exit:

#### Example: Summary (Score)

Select

one of

the following:

1

Category

2

Patient

3

Provider by Patient

4

Referral Date

5

Location

6

Referral Count Totals

7

Category-Referred Service

8

Summary (Score)

9

'Home Help' Eligibility

10	Restore or Merge Referrals Select Option or ^ to Exit: 7// 8	Summary (Score)

Finished Date

Basic Skilled Patient	TOTAL IADL ADL	Care	Behaviors ACROSS

CRPATIENT,EI	(000000008) 06/16/2005	1	5	4	1	11

CRPATIENT,EI

(000000008)

06/17/2005

0

06/28/2005

07/14/2005

CRPATIENT,FI

(000000005)

01/31/2005

10

CRPATIENT,FO

(000000004)

01/28/2005

(000000014)

01/27/2005

Select a Beginning Historical Date.

Name

SSN

BEGINNING date or ^ to exit:	(1/1/1988 - 4/19/2006): T-600//	(AUG 27, 2004)

Select Ending Date.

ENDING date or ^ to exit:	(8/27/2004 - 4/19/2006): T//	(APR 19, 2006)

Select one of the following: A	All Patients

M	Multiple Patients

Select Patients or ^ to exit: A// ll Patients Select one of the following:

F	Formatted

D	Delimited

Select Report Format or ^ to exit: F// ormatted DEVICE: HOME// ;;999	HOME

==============================================================================

GEC Patient-Summary (Score) Data on Complete Referrals Only From: 08/27/2004 To: 04/19/2006

The Summary (Score) GEC option is a little different. This option is used to give some kind of a score to the patients’ needs. A value of 1 or 0 has been given to certain Health Factors. These Health Factors have to be placed into different categories: IADL’s, Basic ADL, Skilled Care, and Patient Behaviors. It calculates the Means and Standard Deviations for the totals. A user could watch these scores on a particular patient and see how his needs have gotten larger or smaller or a period of time.

==============================================================================

| CRPATIENT,TH	(000000003) 02/10/2005   | CRPATIENT,TH	(000000003) 02/10/2005   | CRPATIENT,TH	(000000003) 02/10/2005   | 0                       |    4 |    0 |     0 |     0 |    0 |    0 |    4 |     4 |     4 |   4 |
|---------------------------------------|---------------------------------------|---------------------------------------|-------------------------|------|------|-------|-------|------|------|------|-------|-------|-----|
| CRPATIENT,TW	(000000002) 01/27/2005   | CRPATIENT,TW	(000000002) 01/27/2005   | CRPATIENT,TW	(000000002) 01/27/2005   | 1                       |  0   |  0   |   0   |   0   |  0   |  0   |  1   |   1   |   1   |   1 |
| CRPATIENT,EIGHT                       | (666112222)                           | 01/31/2005                            | 01/31/2005              |  1   |  1   |       |   2   |      |  2   |  0   |       |   5   |   5 |
| CRPATIENT,EIGHT                       | (666112222)                           | 03/28/2005                            | 03/28/2005              |  7   |  7   |       |   2   |      | 15   |  5   |       |  29   |  29 |
| CRPATIENT,EIGHT                       | (666112222)                           | 02/09/2005                            | 02/09/2005              |  0   |  0   |       |   0   |      |  0   |  3   |       |   3   |   3 |
| CRPATIENT,EIGHT                       | (666112222)                           | 01/27/2005                            | 01/27/2005              |  0   |  0   |       |   0   |      |  0   |  0   |       |   0   |   0 |
| CRPATIENT,EIGHT                       | (666112222)                           | 02/03/2005                            | 02/03/2005              |  1   |  1   |       |   1   |      |  1   |  4   |       |   7   |   7 |
| CRPATIENT,EIGHT                       | (666112222)                           | 02/09/2005                            | 02/09/2005              |  0   |  0   |       |   2   |      |  0   |  0   |       |   2   |   2 |
| CRPATIENT,FIVE                        | (666112223)                           | 01/27/2005                            | 01/27/2005              |  3   |  3   |       |   0   |      |  2   |  1   |       |   6   |   6 |
| CRPATIENT,FIVE                        | (666112223)                           | 01/31/2005                            | 01/31/2005              |  0   |  0   |       |   1   |      |  1   |  2   |       |   4   |   4 |
| CRPATIENT,FIVE                        | (666112223)                           | 02/10/2005                            | 02/10/2005              |  0   |  0   |       |   0   |      |  0   |  0   |       |   0   |   0 |
| CRPATIENT,FIVE                        | (666112223)                           | 02/03/2005                            | 02/03/2005              |  0   |  0   |       |   2   |      |  1   |  0   |       |   3   |   3 |
| CRPATIENT,FIVE                        | (666112223)                           | 02/10/2005                            | 02/10/2005              |  0   |  0   |       |   3   |      |  0   |  0   |       |   3   |   3 |
| CRPATIENT,FIVE                        | (666112223)                           | 03/28/2005                            | 03/28/2005              |  1   |  1   |       |   6   |      |  8   |  3   |       |  18   |  18 |
| CRPATIENT,FIVE                        | (666112223)                           | 02/09/2005                            | 02/09/2005              |  0   |  0   |       |   6   |      |  0   |  0   |       |   6   |   6 |
| CRPATIENT,FIVE                        | (666112223)                           | 02/03/2005                            | 02/03/2005              |  0   |  0   |       |   3   |      |  0   |  1   |       |   4   |   4 |
| CRPATIENT,FIVE                        | (666112223)                           | 02/10/2005                            | 02/10/2005              |  0   |  0   |       |   5   |      |  0   |  0   |       |   5   |   5 |
| CRPATIENT,FOUR                        | (666112224)                           | 02/03/2005                            | 02/03/2005              |  1   |  1   |       |   2   |      |  0   |  0   |       |   3   |   3 |
| CRPATIENT,FOUR                        | (666112224)                           | 02/08/2005                            | 02/08/2005              |  7   |  7   |       |   1   |      |  0   |  0   |       |   8   |   8 |
| CRPATIENT,FOUR                        | (666112224)                           | 02/10/2005                            | 02/10/2005              |  3   |  3   |       |   3   |      |  0   |  0   |       |   6   |   6 |
| CRPATIENT,FOUR                        | (666112224)                           | 02/10/2005                            | 02/10/2005              |  0   |  0   |       |   3   |      |  0   |  0   |       |   3   |   3 |
| CRPATIENT,FOUR                        | (666112224)                           | 02/16/2005                            | 02/16/2005              |  5   |  5   |       |   2   |      |  0   |  2   |       |   9   |   9 |
| CRPATIENT,NINE                        | (666112225)                           | 02/08/2005                            | 02/08/2005              |  0   |  0   |       |   0   |      |  0   |  0   |       |   0   |   0 |
| CRPATIENT,NINE                        | (666112225)                           | 02/08/2005                            | 02/08/2005              |  3   |  3   |       |   0   |      |  0   |  0   |       |   3   |   3 |
| CRPATIENT,NINE                        | (666112225)                           | 02/09/2005                            | 02/09/2005              |  0   |  0   |       |   0   |      |  0   |  0   |       |   0   |   0 |
| CRPATIENT,NINE                        | (666112225)                           | 02/10/2005                            | 02/10/2005              |  0   |  0   |       |   2   |      |  0   |  0   |       |   2   |   2 |
| CRPATIENT,NINE                        | (666112225)                           | 02/08/2005                            | 02/08/2005              |  6   |  6   |       |   3   |      |  3   |  0   |       |  12   |  12 |
| CRPATIENT,NINE                        | (666112225)                           | 02/10/2005                            | 02/10/2005              |  0   |  0   |       |   2   |      |  0   |  0   |       |   2   |   2 |
| CRPATIENT,ONE                         | (666112226)                           | 02/08/2005                            | 02/08/2005              |  0   |  0   |       |   0   |      |  1   |  0   |       |   1   |   1 |
| CRPATIENT,ONE                         | (666112226)                           | 02/10/2005                            | 02/10/2005              |  0   |  0   |       |   2   |      |  0   |  0   |       |   2   |   2 |
| CRPATIENT,ONE                         | (666112226)                           | 02/10/2005                            | 02/10/2005              |  0   |  0   |       |   8   |      |  0   |  0   |       |   8   |   8 |
| CRPATIENT,ONE                         | (666112226)                           | 02/09/2005                            | 02/09/2005              |  0   |  0   |       |   0   |      |  0   |  2   |       |   2   |   2 |
| CRPATIENT,ONE                         | (666112226)                           | 01/31/2005                            | 01/31/2005              |  0   |  0   |       |   0   |      |  0   |  0   |       |   0   |   0 |
| CRPATIENT,ONE                         | (666112226)                           | 02/08/2005                            | 02/08/2005              |  0   |  0   |       |   1   |      |  0   |  1   |       |   2   |   2 |
| CRPATIENT,ONE                         | (666112227)                           | 02/03/2005                            | 02/03/2005              |  1   |  1   |       |   0   |      |  0   |  2   |       |   3   |   3 |
| CRPATIENT,SIX                         | (666112227)                           | 02/03/2005                            | 02/03/2005              |  0   |  0   |       |   0   |      |  0   |  0   |       |   0   |   0 |
| CRPATIENT,SIX                         | (666112227)                           | 02/08/2005                            | 02/08/2005              |  0   |  0   |       |   0   |      |  0   |  0   |       |   0   |   0 |
| CRPATIENT,SEVEN                       | (666112228)                           | 02/08/2005                            | 02/08/2005              |  2   |  2   |       |   1   |      |  0   |  0   |       |   3   |   3 |
| CRPATIENT,SEVEN                       | (666112228)                           | 02/16/2005                            | 02/16/2005              |  6   |  6   |       |   4   |      |  2   |  1   |       |  13   |  13 |
| CRPATIENT,TEN                         | (666112229)                           | 02/09/2005                            | 02/09/2005              |  3   |  3   |       |   2   |      |  0   |  0   |       |   5   |   5 |
| CRPATIENT,TEN                         | (666112229)                           | 02/10/2005                            | 02/10/2005              |  3   |  3   |       |   3   |      |  0   |  0   |       |   6   |   6 |
| CRPATIENT,TEN                         | (666112229)                           | 02/08/2005                            | 02/08/2005              |  3   |  3   |       |   3   |      |  4   |  2   |       |  12   |  12 |
| CRPATIENT,TEN                         | (666112229)                           | 02/09/2005                            | 02/09/2005              |  4   |  4   |       |   3   |      |  0   |  0   |       |   7   |   7 |
| CRPATIENT,TEN                         | (666112229)                           | 02/03/2005                            | 02/03/2005              |  3   |  3   |       |   2   |      |  7   |  3   |       |  15   |  15 |
| CRPATIENT,TEN                         | (666112229)                           | 02/10/2005                            | 02/10/2005              |  0   |  0   |       |   2   |      |  0   |  0   |       |   2   |   2 |
| CRPATIENT,TEN                         | (666112229)                           | 02/08/2005                            | 02/08/2005              |  0   |  0   |       |   0   |      |  0   |  0   |       |   0   |   0 |
| CRPATIENT,TEN                         | (666112229)                           | 02/08/2005                            | 02/08/2005              |  0   |  0   |       |   0   |      |  1   |  0   |       |   1   |   1 |
| CRPATIENT,TWELVE                      | (666112229)                           | 02/08/2005                            | 02/08/2005              |  1   |  1   |       |   3   |      |  0   |  1   |       |   5   |   5 |
| CRPATIENT,TWELVE                      | (666112229)                           | 02/10/2005                            | 02/10/2005              |  0   |  0   |       |   2   |      |  0   |  0   |       |   2   |   2 |
| CRPATIENT,TWELVE                      | (666112229)                           | 02/08/2005                            | 02/08/2005              |      |      |   4   |       |  3   |  6   |      |   2   |  15   |  15 |
| CRPATIENT,TWELVE                      | (666112229)                           | 02/08/2005                            | 02/08/2005              |  0   |  0   |       |   2   |      |  7   |  1   |       |  10   |  10 |
| CRPATIENT,TWELVE                      | (666112229)                           | 01/28/2005                            | 01/28/2005              |  2   |  2   |       |   3   |      |  1   |  3   |       |   9   |   9 |
| CRPATIENT,TWELVE                      | (666112229)                           | 01/26/2005                            | 01/26/2005              |  8   |  8   |       |  13   |      |  9   | 10   |       |  40   |  40 |
| CRPATIENT,TWELVE                      | (666112229)                           | 02/09/2005                            | 02/09/2005              |      |      |   3   |       |  2   |  0   |      |   0   |   5   |   5 |
| CRPATIENT,TWELVE                      | (666112229)                           | 01/31/2005                            | 01/31/2005              |  0   |  0   |       |   0   |      |  0   |  0   |       |   0   |   0 |
| CRPATIENT,TWELVE                      | (666112229)                           | 01/27/2005                            | 01/27/2005              |      |      |   0   |       |  0   |  0   |      |   0   |   0   |   0 |
| CRPATIENT,TWELVE                      | (666112229)                           | 01/28/2005                            | 01/28/2005              |  4   |  4   |       |   0   |      |  1   |  1   |       |   6   |   6 |
| Totals > >                            | Totals > >                            | Totals > >                            | Totals > >              | 96   | 96   | 121   | 121   | 78   | 78   | 53   | 348   | 348   |     |
| Means > >                             | Means > >                             | Means > >                             | Means > >               |  1.4 |  1.4 |   1.8 |   1.8 |  1.2 |  1.2 |  0.8 |   5.2 |   5.2 |     |
| Standard Deviations > >               | Standard Deviations > >               | Standard Deviations > >               | Standard Deviations > > |  2.6 |  2.6 |   2.9 |   2.9 |  2.9 |  2.9 |  1.8 |   8.6 |   8.6 |     |

#### Example: Home Health Eligibility Report (All patients)

‘Home Help’ Eligibility option is a way for the local facility to view the information that is sent to VACO GEC office. A quarterly report is sent to provide statistics as to the number of patients who are eligible for care in the home that is paid for by the VA.

=============================================================================

Referred to Homemaker/Home Health Aide(HHHA) or Adult Day Health Care(ADHC) or VA In-Home Respite(VAIHR) or Care Coordination programs(CC)

From: 01/01/2005 To: 03/31/2005

Fiscal Quarter: 2 (Calendar Quarter 1)

Criteria	Measured

Name	SSN	Prog.	0	#1 #2 #3 #4 Date	Criteria

=============================================================================

| CRPATIENT,ONE      | C0000   | VAIHR   | X   |     |    |    | 01/27/2005   | NOT   | MET   |
|--------------------|---------|---------|-----|-----|----|----|--------------|-------|-------|
| CRPATIENT,TWO      | C6667   | CC      |     | X   |    |    | 01/28/2005   |       |       |
| CRPATIENT,THREE    | C6668   | ADHC    |     | X   |    | X  | 02/09/2005   |       |       |
| CRPATIENT,FOUR     | C6669   | ADHC    | X   |     |    |    | 01/31/2005   | NOT   | MET   |
| CRPATIENT,FIVE     | C6660   | CC      | X   |     |    |    | 01/27/2005   | NOT   | MET   |
| CRPATIENT,SIX      | C6661   | CC      | X   |     |    |    | 01/27/2005   | NOT   | MET   |
| CRPATIENT,SEVEN    | C6668   | ADHC    |     | X   |    |    | 01/28/2005   |       |       |
| CRPATIENT,EIGHT    | C6663   | VAIHR   | X   |     |    |    | 01/31/2005   | NOT   | MET   |
| CRPATIENT,NINE     | C6664   | ADHC    |     | X   |    |    | 02/09/2005   |       |       |
| CRPATIENT,TEN      | C6670   | ADHC    |     |     |    | X  | 02/09/2005   |       |       |
| CRPATIENT,ELEVEN   | C6671   | CC      |     | X   |    |    | 01/27/2005   |       |       |
| CRPATIENT,TWELVE   | C6663   | ADHC    | X   |     |    |    | 02/09/2005   | NOT   | MET   |
| CRPATIENT,THIRTEEN | C6662   | VAIHR   | X   |     |    |    | 02/03/2005   | NOT   | MET   |
| CRPATIENT,THIRTEEN | C6662   | ADHC    |     | X	X | X  |    | 02/10/2005   |       |       |
| CRPATIENT,THIRTEEN | C6662   | ADHC    |     | X	X |    |    | 02/09/2005   |       |       |
| CRPATIENT,FOURTEEN | C6622   | HHHA    |     | X   | X  |    | 02/03/2005   |       |       |

Criteria

0: Not eligible under any criteria. 1: Problems with 3 or more ADL's.

2: 1 or more patient behavior or cognitive problem. 3: Expected life limit of less than 6 months.

4: Combination of the following:

2 or more ADL dependencies

&lt;AND&gt; 2 or more of the following: Problems with 3 or more IADL's

&lt;OR&gt; age of patients is 75 or more.

&lt;OR&gt; living alone in the community.

&lt;OR&gt; utilizes the clinics 12 or more time in the preceding 12 months.

Enter RETURN to continue or '^' to exit:

#### Example 9b: Home Health Eligibility Report (Multiple patients)

This report lets you select specific patient names to be included in a report.

#### Example: Restore or Merge Referrals

The ‘Restore or Merge Referrals’ option is not a report. It is a tool that was asked for by the users. Periodically, the GEC Referrals are closed before all of the dialogs are completed. This would mean that all of the dialogs would have to be re-completed. This tool allows the users to select a Partial or Whole Referral that they would need re-opened or merged with another referral. The user has a choice of Closing an open referral, Merging 2 referrals that are either complete or not, together making one referral or viewing all the referrals for a particular patient.

| Select Reminder Reports Option: G	GEC Referral Report All Reports will print on 80 Columns  Select one of the following:  1. Category 2. Patient 3. Provider by Patient 4. Referral Date 5. Location 6. Referral Count Totals 7. Category-Referred Service 8. Summary (Score) 9. 'Home Help' Eligibility 10. Restore or Merge Referrals  Select Option or ^ to Exit: 2// 10	Restore or Merge Referrals PATIENT:	WHPATIENT,EIGHT  SC VETERAN  WHPROVIDER,ONE	PRIMARY  Enrollment Priority: GROUP 1	Category: IN PROCESS	End Date:  ================================================================================ WHPATIENT,EIGHT (000000008)	AGE:57	OUTPATIENT	Unknown Division  Current Open Referral::  1	Jul 14, 2005 11:28:28 am (start date)  Care Coordination	by: CRPROVIDER,ONE	On: Jul 14, 2005  Historical Referral(s)::   |     |     |     |      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|-----|------|
| 2	Jun 30, 2005 11:41:10 am (start date)  Care Recommendation	by: CRPROVIDER,ONE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | On: | Jun | 30, | 2005 |
| 3	Jun 28, 2005 2:55:03 pm (start date)  Social Services	by: CRPROVIDER,ONE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | On: | Jun | 28, | 2005 |
| Care Recommendation	by: CRPROVIDER,ONE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | On: | Jun | 28, | 2005 |
| Care Coordination	by: CRPROVIDER,ONE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | On: | Jun | 28, | 2005 |
| Select one of the following:  C	CLOSE Open Referral  M	Merge 2 Referrals  V	View ALL Historical Referrals                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |     |     |     |      |

| 1. New Patient 2. Quit  Enter response: View ALL Historical Referrals  ================================================================================ WHPATIENT,EIGHT (000000008)	AGE:57	OUTPATIENT	Unknown Division  Current Open Referral::  1	Jul 14, 2005 11:28:28 am (start date)  Care Coordination	by: CRPROVIDER,ONE	On: Jul 14, 2005  Historical Referral(s)::   |     |     |     |      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-----|-----|------|
| 2	Jun 30, 2005 11:41:10 am (start date)  Care Recommendation	by: CRPROVIDER,ONE                                                                                                                                                                                                                                                                                             | On: | Jun | 30, | 2005 |
| 3	Jun 28, 2005 2:55:03 pm (start date)  Social Services	by: CRPROVIDER,ONE                                                                                                                                                                                                                                                                                                  | On: | Jun | 28, | 2005 |
| Care Recommendation	by: CRPROVIDER,ONE                                                                                                                                                                                                                                                                                                                                      | On: | Jun | 28, | 2005 |
| Care Coordination	by: CRPROVIDER,ONE                                                                                                                                                                                                                                                                                                                                        | On: | Jun | 28, | 2005 |
| Select one of the following:                                                                                                                                                                                                                                                                                                                                                |     |     |     |      |
| C	CLOSE Open Referral  M	Merge 2 Referrals  D	Display Last 2 Referrals Only  1. New Patient 2. Quit  Enter response: Merge 2 Referrals First Referral Record:	(1-3): 2  Second Referral Record:	(1-3): 3 DO MERGE                                                                                                                                                           |     |     |     |      |

**Algorithm for GEC (Next Generation) Software**

The information for the “criteria” is taken from the letter # IL 10-2004-005 entitled UNDER SECRETARY FOR HEALTH’S INFORMATION LETTER dated May 3 2004. pages B-2 and B-3

The following is the Algorithm that will be used in the software to determine if a patient meets the criteria necessary to be placed in one of the monitored programs. HEALTH FACTORS that are part of the patient record for an evaluation, are designated with capital letters (below).

7D = 7 days

YES or NO = Yes or No response from the Dialog Additional explanations found to the right of health factor

**Initial Requirement is to be referred to one of the following VA funded programs** . ( Requires **1** or **6,** plus one of the other Health Factors)

1. GEC ADULT DAY HEALTH CARE (REFERRED TO)
2. GEC HOMECARE FUNDING-VA
3. GEC HOMEMAKER/HOME HEALTH AIDE
4. GEC VA IN-HOME RESPITE
5. GEC HOME TELEHEALTH (REFERRED TO)
6. GEC TELEHEALTH FUNDING-VA

#### Criteria #1 : “Three or more Activities of Daily Living (ADL) dependencies.”

(Any 3 of the ADL’s below)

- GEC BATHING HELP/SUPERVISION LAST 7D-YES
- GEC BED POSITIONING HELP LAST 7D-YES
- GEC DRESS HELP/SUPERVISION LAST 7D-YES
- GEC EATING HELP/SUPERVISION LAST 7D-YES
- GEC INDEPENDENT IN WC LAST 7D-YES
- GEC MOVING AROUND INDOORS LAST 7D-YES
- GEC TOILET HELP/SUPERVISION LAST 7D-YES
- GEC TRANSFERS HELP/SPRVISION LAST 7D-YES

#### OR

**Criteria #2 : “Significant cognitive impairment** ” (Any 1 of those indicated below)

- GEC CAN BE UNDERSTOOD LAST 7D-NO
- GEC ENDANGERED SAFETY LAST 90D-YES
- GEC MADE REASONABLE DECISIONS LAST 7D-NO
- GEC HALLUCINATIONS/DELUSIONS LAST 7D-YES
- GEC PHYSICALLY ABUSIVE LAST 7D-YES
- GEC RESISTS CARE LAST 7D-YES
- GEC VERBALLY ABUSIVE LAST 7D-YES
- GEC WANDERING LAST 7D-YES

#### OR

**Criteria #3 “ Prognosis of Life Expectancy of less than 6 months”**

(Any 1 of these health factors )

- GEC LIFE EXPECTANCY &lt; 6MO-YES

#### OR

**Criteria #4 : “Two ADL dependencies and two or more of the following conditions:”**

(Any 2 of the ADL’s below and the additional requirements)

- GEC BATHING HELP/SUPERVISION LAST 7D-YES
- GEC BED POSITIONING HELP LAST 7D-YES
- GEC DRESS HELP/SUPERVISION LAST 7D-YES
- GEC EATING HELP/SUPERVISION LAST 7D-YES
- GEC INDEPENDENT IN WC LAST 7D-YES
- GEC MOVING AROUND INDOORS LAST 7D-YES
- GEC TOILET HELP/SUPERVISION LAST 7D-YES
- GEC TRANSFERS HELP/SPRVISION LAST 7D-YES

#### AND

“(a) Dependency in three or more Instrumental ADL (IADL)” (Any 3 of the IADL)

- GEC DIFFICULT TRANSPORTATION/LAST 7D-YES
- GEC DIFFICULTY MANAGING MEDS/LAST 7D-YES
- GEC DIFFICULTY MNG FINANCES/LAST 7D-YES
- GEC DIFFICULTY PREPARE MEALS/LAST 7D-YES
- GEC DIFFICULTY USING PHONE/LAST 7D-YES
- GEC DIFFICULTY W/ HOUSEWORK/LAST 7D-YES
- GEC DIFFICULTY WITH SHOPPING/LAST 7D-YES

#### OR

“(b) Recent discharge from a nursing home, or upcoming nursing home discharge plan

contingent on receipt of home and community – based care services.”

- GEC COMMUNITY NRSNG HOME (REFERRED FROM)
- GEC VA DOMICILIARY (REFERRED FROM)
- GEC VA NURSING HOME

#### OR

“(c) Seventy Five Years old , or older.”

(Obtained from the Patient’s Records using an API call)

#### OR

“(d) High use of medical services defined as **three** or more hospitalizations in the past year and/or utilization of outpatient and/or emergency evaluation units **twelve** or more times in the past year.

( The API ….GETAPPT^SDAMA201(…) to retrieve appointments etc.)

#### OR

“(f) Living alone in the Community”

GEC ALONE

## Appendix E - Iraq &amp; Afghan Post-Deployment Screen

### Operation Enduring Freedom and Operation Iraqi Freedom (OEF/OIF)

The Clinical Reminder, *Iraq &amp; Afghan Post-Deployment Screen,* which identified veterans of Operation Enduring Freedom in Afghanistan and Operation Iraqi Freedom *,* was enhanced and distributed to sites in November 2005. The OEF/OIF data will be rolled up for regional and national reporting purposes. Due to the fast track that this project has been placed on, the project will be completed in two phases.

- **Phase I** included modifications and enhancements to the current Afghan/Iraq reminder to better meet the needs of the field and provide the information needed for reporting purposes. In Phase I, the clinical reminder for post-deployment screening will be due for patients whose latest Separation date greater than 09/11/01. It is also due for active duty patients being seen at the VA.

#### 1 Phase II Extract Reports &amp; National Rollup of Data

Phase II is dependent on changes being made by Management Services to improve the quality and accuracy of a patient’s OEF and OIF combat data. The OEF/OIF Enrollment patch will include functionality that will manage OEF/OIF Combat Veteran data. Management Systems will require OEF/OIF patients to first be a combat veteran with a combat from and to date, where the combat to date ends after 10/07/01, and secondarily have an OEF or OIF indication if the patient served in the OEF or OIF theatre during the combat service period. Patient combat data will be collected by clerks during enrollment, registration, or the first VA visit.

Phase II Reminder development will be coordinated with Enrollment development to use the Combat Veteran data.

- Phase II includes re-distribution of the national OEF/OIF clinical reminder/dialog.

- In Phase II, the clinical reminder for post-deployment screening will be due for patients whose latest separation date is greater than 09/11/01, or patients whose latest combat end date was greater than 10/07/01 for service in the OEF or OIF combat theatre. The reminder will continue to also be due for active duty patients being seen at the VA.

### Example screens

On the following pages, we show examples of the dialog screens that you’ll see when you process the Iraq and Afghan Screening reminder.

### Iraq &amp; Afghan Post-Deployment Screen Reminder Dialog Screens

Note that the PTSD screen is not open. This means that it was done in the past six months. The depression screen is “open” because it has not been done in the past six months.

1. If you answer “yes,” to the first question, the rest of the dialog opens up. If the first question is answered “no,” then you are done.
<!-- image -->

1. When the dialog opens for a “yes” answer, the first question prompts for the location of service. OIF options are on the first screen below and OEF options are on the next screen.
<!-- image -->

<!-- image -->

1. If the first question has already been answered “yes,” then it doesn’t need to be answered again if subsequent users open the dialog to complete other sections. Note the radio button in front of the PTSD screen. This is necessary to allow the user to choose between doing the screen and entering a refusal (next screen).
<!-- image -->

The refusal options for PTSD, depression and alcohol are now present and consistent. The alcohol section is closed because it has been completed in the past six months.

<!-- image -->

1. Note that questions 4B and 4D are “closed” – they have been completed in the past six months. The refusal option is available for this section.

Entering a refusal option for any one of the sections will satisfy that section for one month. However, it will not cause that section of the dialog to be “closed” – the section will remain open but the reminder would no longer be due if all four refusal options are chosen.

<!-- image -->

1. The hyperlinks have been moved to the bottom of the dialog display.

<!-- image -->

1. If you would like to re-enter data on a closed section, click on the checkbox for that section – PTSD in this example
<!-- image -->

After choosing the closed PTSD section, it opens to allow completion.

<!-- image -->

This is what the dialog would look like if you did PTSD screening, Alcohol screening, and depression screening and then clicked on FINISH – and THEN opened the OEF/OIF reminder dialog – those sections would be closed.

<!-- image -->

Clicking on clinical maintenance shows which sections are needed. The display here is based on the completion of each section AFTER the service separation date. If the dates of all seven pieces listed above 1-3 and 4A-D are later than the last service separation date, then the reminder is resolved.

<!-- image -->

## Index

AAC SAS Files, 77

Acronyms, 77

Appendix A: FAQS, Hints, and Tips, 74 Appendix B: Glossary, 77

Appendix C: Edit Cover Sheet Reminder List, 80

Appendix D: VA GEC Reports, 83 Appendix E - Iraq &amp; Afghan Post-

Deployment Screen, 115

Applicable, 77

Chapter 1: Clinical Reminders - CPRS, 7, 9

Chapter 2: Resolving IHD Reminders, 19 Chapter 3: Processing Mental Health

Reminders, 30

Chapter 4: Using Reminder Reports, 37 Chapter 5: Health Summaries and Clinical

Reminders, 42

Chapter 6: Set up VA-Geriatric Extended Care (GEC) Referral, 47, 50

Chapter 7: Code Set Versioning Changes in Reminders, 68

Chapter 8: My Health *e* Vet Changes in Reminders, 69

Chapter 9: Women’s Veterans Health Reminders, 70, 71

Code Set Versioning, 68 Cover Sheet Reminder List, 80 CPT, 68

Definitions, 77

Due, 78

Edit Cover Sheet Reminder List, 80 FAQS, Hints, and Tips, 74

GEC, 47

GEC Consult Order, 52

GEC Interdisciplinary Notes, 53 GEC Referral Ad hoc Reports, 51, 83

GEC Referral Reminders, 52 GEC Referral Reports, 51 GEC Reports, 83

GEC Status Check, 49, 50

Glossary, 77

Health Information Portability and Accountability Act (HIPAA), 68

HIPAA, 68

ICD0, 68

ICD9, 68

IHD Reminder Definitions, 19

Iraq &amp; Afghan Post-Deployment Screen, 115

Mental Health Reminders, 30

My Health *e* Vet Health Summary, 45 Not Applicable, 78

Operation Enduring Freedom and Operation Iraqi Freedom, 115

Patient List, 78

Reminder Definitions, 78

Reminder Dialog, 78 Reminder Patient List, 78 Reminder Terms, 78

Report Reminders, 79

Standards Development Organization (SDO), 68

TIU Interdisciplinary (ID) note, 53 VA GEC Reports, 51, 83

VA-*IHD ELEVATED LDL REPORTING, 19

VA-*IHD LIPID PROFILE REPORTING, 19

VA-Geriatric Extended Care, 47, 83

VA-IHD ELEVATED LDL, 19, 29 VA-IHD LIPID PROFILE, 19

Women’s Veterans Health Reminders, 70