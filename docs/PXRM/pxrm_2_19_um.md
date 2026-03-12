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
source_file: pxrm_2_19_um.docx
status: draft
title: pxrm 2 19 um.docx
---

Home Telehealth

## Clinical Reminders and Dialogs User Guide

<!-- image -->

July 2017

#### Department of Veterans Affairs

**Office of Information and Technology (OI&amp;T)**

**Revision History**

NOTE: The revision history cycle begins once changes or enhancements are requested after the document has been baselined.

| **Date**   |   **Revision** | **Description**                                       | **Author**                 |
|------------|----------------|-------------------------------------------------------|----------------------------|
| 06/29/2017 |            1.1 | Revised to reflect content as of Tv13 of patch bundle | Development Team           |
| 01/05/2016 |            1   | Initial                                               | C2/Booz Allen, PMO Support |

#### Table of Contents

1.	Introduction	1

1.1.1.	Web Sites	1

1. Purpose	1
2. Document Orientation	2
    1. Clinic Location	2
    2. Note Title	2
    3. Template	2
        1. Assumptions	3
        2. Coordination	3
        3. Disclaimers	3
        2. Documentation Disclaimer	4
        5. References and Resources	4
            1. System Summary	6
                1. System Configuration	6
                2. Data Flows	7
            2. Fundamentals	7
        2.1, System Configuration	7
            1. Completing a Note	7
            2. Using Templates for Documentation	10
            2. Reminder Dialog Templates	11
            3. Encounter/CPT Codes	15
        Encounter Form Completion:	16
            1. Completing an Encounter	16
            2. Data Objects	17
            3. Health Factors	18
            4. HT Education Topics	19
                1. Clinical Reminder Process	22
            How to satisfy Clinical Reminders	22
                1. How to Run a “Reminders Due” Report	23
                    1. Getting Started	25
                        1. Complete the New Mini-template for Previously Enrolled HT patients	25
                    2. Templates and Program Enrollment	28
                        2. Home Telehealth Consult Request	28
                            1. Completing the HT SCREENING CONSULT note from the CPRS consult tab	31
                            2. Completing the HT SCREENING CONSULT note from the CPRS Notes tab	34
                TECH EDUCATION AND INSTALLATION	40
                ASSESSMENT TREATMENT PLAN	42
                CONTINUUM OF CARE FORM (CCF)	49
                CAREGIVER RISK ASSESSMENT	56
                INTERVENTION NOTE	58
                MONTHLY MONITOR NOTE	59
                PERIODIC EVALUATION	60
                EMERGENCY MANAGEMENT CLASSIFICATION	63
                DISCHARGE TEMPLATE	64
                Other	66
                VIDEO VISIT	66
                    1. Acronyms and Abbreviations	68
                **Appendix**
                **Crosswalk Titles and Stop Codes Option 1 and 2**

##### Crosswalk for Clinic Location and CPT Codes

## 1 Introduction

1. Software Disclaimer	3

1. Dialog Templates	10

The purpose of this project is to release new national reminders, reminder dialogs, and TIU progress note titles that will be used by Care Coordinators managing patients enrolled in HT programs.

The Office of Connected Care (OCC) has been working to develop a comprehensive, user- friendly, and accurate delivery model for documentation in the Computerized Patient Record System (CPRS) for use by all Home Telehealth (HT) staff. It is vitally important to have documentation standardized for appropriate delivery of care to the Veterans, ability to pull accurate data, and ease of quality management and chart reviewing. For that reason, the national templates should not be edited or revised at the local or VISN level to maintain the integrity of the data collected as well as ensure any further national revisions or updates are appropriately captured and standardized.

Two Master Preceptor-led committees spearheaded the work in creating this standardized documentation system. One was tasked with standardizing the Clinic Location titles and use of Stop Codes- both Primary and Secondary as well as developing a group of note titles that would intuitively reflect the work done by HT staff. The second committee was tasked with creating templates to be attached to the appropriate note titles. This again was to ensure that a standardized, high quality of care was delivered to the Veteran population, that the same information was being obtained, and that documentation was made as streamlined as possible.

#### 1.1.1.Web Sites

| **Site**                              | **URL**                                                  | **Description**                                                                                                                                                    |
|---------------------------------------|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| National Clinical Reminders site      | http://vista.med.va.gov/reminders                        | Contains manuals, PowerPoint presentations, and other information about  Clinical Reminders                                                                        |
| National Clinical Reminders Committee | http://vaww.portal.va.gov/sites/ncrc public/default.aspx | This committee directs the development of new and revised national reminders                                                                                       |
| VistA Document Library                | http://www.va.gov/vdl/                                   | Contains manuals for nationally released software in use across VHA, such as: Clinical Reminders, CPRS,  Consults/Request Tracking, and Text Integration Utilities |

### Purpose

The National Office of Connected Care (OCC) requested a comprehensive, integrated template set in use at all VA facilities caring for Home Telehealth patients. These templates are the replacements for the earlier set of templates posted on the web site (VA Intranet): [http://vaww.telehealth.intranet.dev.webops.va.gov/](http://vaww.telehealth.intranet.dev.webops.va.gov/) .Those templates were either not used at all by sites, or significantly modified. A group of representative HT clinicians from around the Country did a bi-monthly series of teleconferences, revising the content of the templates. Several Pilots were performed over a couple of years to produce the final product.

The templates were converted to reminder dialogs for the special features the reminder dialogs provide, such as:

- Linked health factors * (See Health Factor section below)
- for the ability to use as data objects for display back in the templates
- Ability to suppress checkboxes for items in order to require a response
- A specific “required items missing” message
- Ability to send alternate text into the progress note (text different from that in the template)
- Ability to have embedded orders
- Ability to send ICD-10 (Diagnosis) and CPT (Procedure) codes to the GUI Encounter Form
- Ability to trigger and satisfy a clinical reminder even if in the TEMPLATES drawer

- for data capture; these will be incorporated into the existing HT VSSC data cubes

If you have questions about the templates or documentation process, you may contact your HT Program Lead.

If you have technical problems with the CPRS application or technical (computer) problems with accessing/launching/signing the templates, **please contact your site CAC (Clinical Application Coordinator).**

### Document Orientation

There are **THREE** distinct items to grasp in this new Documentation process:

1. **Clinic Location-** gives the correct coding for workload. Choosing the correct Clinic Location to identify the activity is critical. This is how the data is created for reports in the VHA Support Service Center (VSSC) Cube such as 683, Monthly Notes, or 371, Screening Consult.

1. **Note Title-** The choice of the correct title identifies the activity, and in most cases the correct Template will automatically be attached.

1. **Template-** As noted above, these are generally attached to the appropriate Note Title. These templates are explained at length later in this document. Templates are mandatory and provide Health Factor data. The HT Templates are comprehensive, yet very user friendly and support the minimum documentation standards. They have many options and free text so take advantage of these and populate the template to reflect a complete and accurate description of the topic being covered. Any updates to these templates will be made and approved at the National level.

**Crosswalk: Titles and Stop Codes Option 1 and 2, See appendices.**

#### Assumptions

This guide was written with the following assumed experience/skills of the audience:

1. User has working knowledge of CPRS GUI, including, but not limited to, using Clinical Reminder dialogs to process and document patient encounters,
2. User has been provided the appropriate active roles, menus, and security keys required for the software.
3. User has validated access to the software.
4. User has completed any prerequisite training.

#### Coordination

##### Table 2: Deployment Roles and Responsibilities

| **Team**                                                                                 | **Phase / Role**   | **Tasks**                                |
|------------------------------------------------------------------------------------------|--------------------|------------------------------------------|
| Development team and test sites                                                          | Installation       | Test for operational readiness           |
| Development team and National product support                                            | Deployment         | Execute deployment                       |
| Regional PM/ Field Implementation Services (FIS)/ Office of Policy and Planning (OPP) PM | Installation       | Plan and schedule installation           |
| Site CACs & Clinical Staff, Nat’l Education & Training                                   | Deployment         | Post-installation readiness and training |

#### Disclaimers

##### Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

##### Documentation Disclaimer

The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

#### Documentation Conventions

Each project establishes a release baseline of critical information prior to the Project Management Accountability System (PMAS) MS1 review. This is the information that enters into change control at deployment. A subset of this information accompanies the product release to the field. This is referred to as the release package, which includes the product build (software and hardware specifications) along with the body of user and technical documentation that support the install, operations, training, and support of the product as well as authorizations required for deployment. The Release Package includes the following ProPath documents:

- System Design Document (SDD)
- Version Description Document (VDD)
- Operational Acceptance Plan (OAP)
- Project Management Plan (PMP)
- Production Operations Manual (POM)
- Authority to Operate (ATO)
- Installation Guide and Back-Out/Rollback Plan
- Deployment Plan
- Operational Readiness Review (ORR) Checklist Submission Documents (Business Requirements Document, Requirements Specification Document, Test Evaluation Summary, Requirements Traceability Matrix, User Guide, Technical Manual, etc.)

Additionally, end user training will be provided by the Office of Connected Care, Implementation Team. All user training materials developed by the team will be made available in My Telehealth and in the HT Web Site; HT Master Document Library SharePoint [http://vaww.telehealth.va.gov/pgm/ht/index.asp.](http://vaww.telehealth.va.gov/pgm/ht/index.asp)

#### References and Resources

Home Telehealth Clinical Reminders and Dialogs User Guide

Found in the clinical reminder section of [http://www.va.gov/vdl/](http://www.va.gov/vdl/) Home Telehealth Installation and Setup Guide

Found in the clinical reminder section of [http://www.va.gov/vdl/](http://www.va.gov/vdl/)

### National Service Desk and Organizational Contacts

Support will be performed by the National Service Desk – Tuscaloosa (NSD) (Tier 1 Support), Enterprise Program Management Office (EPMO) Health Product Support Team (Tier 2 Support), and the National VistA Maintenance Support Group (Tier 3 Support).

Tier 1 Support will be provided by the NSD utilizing the CA Service Desk Management (SDM) system. Home Telehealth users (or their designee), with problems that cannot be resolved locally, will call the NSD to open a CA SDM ticket. Issues not resolved by the Tier 1 Support Team will be assigned to Tier 2 Support in CA SDM. Tier 2 Support for Home Telehealth Clinical Reminders, Health Summary, and Text Integration Utilities will include assistance from the respective EPMO Health Product Support Team. Issues not resolved by the Tier 2 Support Team will be assigned to Tier 3 Support in CA SDM. Tier 3 Support is the highest level of support for VistA applications, which includes business analysts, software testers, system administrators, developers, and database administrators who have specialized technical knowledge of VistA. Tier 3 Support will provide services, such as, issue resolution and defect management on all issues/defects that have not been resolved by the Tier 1 and 2 Support Teams. Any defect found will be logged in CA SDM and also in Rational ClearQuest (as required).

Table 1 outlines the incident priority levels and the time frame for response:

**Table 1: Incident Priority Levels and Time Frame for Response**

| **Priority Level**   | **Call Received**          | **Time Frame for Response**                              | **Priority Level Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------------|----------------------------|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Urgent**           | During business hours      | Requester will be directly contacted by Service Provider | An urgent incident is a catastrophic incident of an operating environment where production systems are severely impacted, down or not functioning. Under this scenario, one of the following situations may exist:  - Loss of production data and no procedural work around exists. - Patient care and/or safety are at risk or damage is incurred. - Complete loss of a core organizational or  business process where work cannot reasonably continue.                           |
|                      | During non- business hours |                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **High**             | During business hours      | Requester will be directly contacted by Service Provider | A high incident is a problem where a system is functioning but in a severely reduced capacity. The situation is causing:  - Significant impact to portions of the business operations and productivity. - No loss of production data and / or a procedural work around exists. - The system is exposed to potential loss or interruption of service. Includes incidents that significantly impact development  and/or production, but where an alternative operation is available. |
|                      | During non- business hours |                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Medium**           | During business hours      | Average of two (2) business hours or less                | A medium incident is a medium-to-low impact problem which involves partial non-critical                                                                                                                                                                                                                                                                                                                                                                                            |

| **Priority Level**   | **Call Received**          | **Time Frame for Response**                 | **Priority Level Description**                                                                                                                                                                                                                                                                                                |
|----------------------|----------------------------|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                      | During non- business hours | No After Hours Coverage will be provided    | functionality loss. A medium incident impairs some operations but allows the user or an application to continue to function. This may be a minor incident with limited loss or no loss of functionality or impact to the user's operation and incidents in which there is an easy circumvention or avoidance by the end user. |
| **Low**              | During business hours      | Average of eight (8) business hours or less | A low incident has no impact on the quality, performance, or functionality of the system. Low incidents have minimal organizational or business impact.                                                                                                                                                                       |
|                      | During non- business hours | No After Hours Coverage will be provided    | A low incident has no impact on the quality, performance, or functionality of the system. Low incidents have minimal organizational or business impact.                                                                                                                                                                       |

***NOTE*** *: If you require further technical assistance, please notify your local IT support to log a national CA Service Desk Manager (SDM) ticket (previously a Remedy™ ticket) or contact the REDACTED and have them submit a national CA ticket to the Incident Area: NTL.APP.VISTA.CLINICAL REMINDERS 2\_0 and we will contact you*

## 2 System Summary

1. To provide a means to add the HT ENROLLMENT STARTING DATE to the patient’s electronic record, a health factor that is needed.
2. To provide a means to trigger the HT CONTINUUM OF CARE (FOLLOW-UP) clinical reminder every 6 months after the HT CONTINUUM OF CARE (INITIAL) has been done, if the patient remains on NIC (Non-Institutional Care) or Chronic Care Management (CCM) criteria.
3. To meet our VERA requirements both NIC and CCM require q6 month CCF updates.
4. While in the normal workday, to be able to update the note titles, and templates for clinician’s activity with the patients.
5. To complete the consult request using the HT SCREENING CONSULT note title.
6. To be properly integrated with VistA and *ACTIVATE* a patient via VistA Integration any time after a consult has been initiated.
7. To check Reminder Status correctly after processing a reminder in the SAME CPRS GUI session.

### System Configuration

The clinical reminders, reminder dialog templates, TIU note titles, and other supporting components are all elements in the established configuration of VistA and CPRS GUI. Users access CPRS from personal and shared workstations. CPRS operates against centralized instances of the VistA database.

If desired, more specific technical information for each application may be obtained from the following locations.

CPRS Technical Manual(s)

[http://www.va.gov/vdl/documents/Clinical/Comp\_Patient\_Recrd\_Sys\_(CPRS)/cprslmtm.pdf](http://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/cprslmtm.pdf) [http://www.va.gov/vdl/documents/Clinical/Comp\_Patient\_Recrd\_Sys\_(CPRS)/cprsguitm.pdf](http://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/cprsguitm.pdf) Clinical Reminders 2.0 Technical Manual

[http://www.va.gov/vdl/documents/Clinical/CPRS-Clinical\_Reminders/pxrm\_2\_4\_tm.pdf](http://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_4_tm.pdf) TIU Technical Manual

[http://www.va.gov/vdl/documents/Clinical/CPRS-Text\_Integration\_Utility\_(TIU)/tiutm.pdf](http://www.va.gov/vdl/documents/Clinical/CPRS-Text_Integration_Utility_(TIU)/tiutm.pdf) Health Summary Technical Manual

[http://www.va.gov/vdl/documents/Clinical/CPRS-Health\_Summary/hsum\_2\_7\_104\_tm.pdf](http://www.va.gov/vdl/documents/Clinical/CPRS-Health_Summary/hsum_2_7_104_tm.pdf)

### Data Flows

The templates described in this manual are used within the confines of CPRS GUI and VistA, both of which are well-documented elsewhere. These templates do not alter existing data flows and therefore are not discussed here.

## 3 Fundamentals

Knowledge of encounters, reminders, and Text Integrated Utilities (TIU) is critical to make use of the products in this patch. This section provides a basic understanding of the fundamentals of these packages within CPRS and VistA. For additional information see the documents listed in section 2.1, System Configuration.

### Completing a Note

The templates in this patch must be accessed through the Notes tab in CPRS.

1. To create a note in CPRS, select the notes tab and click the NEW NOTE button:
<!-- image -->
2. The 'location for current activities' window will appear, and it defaults to the CLINIC APPT tab:

<!-- image -->

1. Change to the NEW VISIT tab and select the appropriate HT clinic location. Click OK to close the window. If writing a note on a patient without any contact with that patient, either phone, office or home (HBPC), then mark this visit “historical”. This has to be done at the time the note is initiated.

1. Select a HT note title by typing “HT”. Select the appropriate HT note title. Click OK.

1. The correct template will launch after clicking “OK” on the correct note title.

1. Two types of templates are included with the HT documentation patch. For a description and tips for each type see the next section of this guide.

1. Once the template is completed always read and make edits before signing.

1. Sign the note with your electronic signature, then click OK:

CPRS Tips:

- Know the default for CPRS timing out. If CPRS times out while completing a template, the information entered into the template will be lost.
- You cannot go into another patient’s chart while working on a template, you will lose it. If you need to go into another chart before you have finished the template, open a second CPRS.

This patch updates the name of several TIU progress note titles released by the Office of Connected Care several years ago. Below is a list of note titles released in this patch. Each should have a National template linked, so that once the note title is opened in CPRS the template will automatically open. The templates must be linked by local CACs. If a template is not displaying appropriately contact the local CAC for help.

- HT Screening Consult
- HT Assessment Treatment Plan
- HT Tech Education
- HT Intervention

- HT Monthly Monitor
- HT Periodic Evaluation
- HT Continuum of Care
- HT Caregiver Assessment
- HT Video Visit
- HT Discharge
- HT Note
- HT Telephone Case Management (not used)

### Using Templates for Documentation

The Home Telehealth notes use two types of templates, dialog templates (sometimes called flat templates or txml templates) and reminder dialog templates (sometimes called dialogs or reminders). Each type has distinct features. Below are tips for each type.

#### Dialog Templates

1. In a dialog template if a required field is missed a NON-SPECIFIC required item missing message will pop up once the template is complete; shown below on the right. There are

(3) of these types of templates in the HT template set.

1. Dialog templates display “Template” in the top blue title bar.
2. These templates are only stored as text within the patient’s record and do not have health factors or orders embedded in the template.

#### Reminder Dialog Templates

Reminder Dialogs are another type of template in the CPRS GUI. A reminder dialog has an alarm clock icon in front of the name (example):

<!-- image -->

1. Reminder dialogs have three windows:

1. The top window is the template form (you can stretch it vertically to see and work on more items, but DO NOT COVER the 'FINISH button")
2. The middle window is a preview of the completed note.
3. The bottom window displays the specific data items to be stored in the encounter VistA (apart from the note text) once the FINISH button is selected.

Bottom Window

Middle Window

Top Window

1. Reminder dialogs display “reminder dialog template” in the top blue title bar.

1. With these types of templates, there is a window below the template which provides a preview of the completed note (left of the blue arrow below). When you have finished populating the template click the finish button to send the information to the unsigned progress note. You need to accurately populate information while in the template. Editing information after leaving the template will not place health factors into CPRS or will populate exactly what you entered. If for some reason your Veteran decides not be enrolled and you have begun your template, do not “cancel” you will want to “DELETE THE NOTE” otherwise health factors will be captured.

1. If all REQUIRED items (noted with an asterisk) have not been addressed, A specific “required items missing” message will display to help identify which sections to go back to answer (example below). These boxes have several formats, some tell the missing and some will not). The required fields must be addressed before the FINISH button can be clicked to finish the note successfully.

<!-- image -->

1. One advantage of reminder dialogs is that they can be resized and moved on the screen, so that you can read another note:

<!-- image -->

#### Encounter/CPT Codes

An encounter is a professional contact between a patient and a health care provider vested with responsibility for diagnosing, evaluating, and treating the patient’s condition. Encounters occur in both the outpatient and inpatient setting.

1. Contact can include face-to-face interactions or those accomplished via telecommunications technology.
2. Secure Messaging was implemented in 2012 in Primary Care, Specialty Medicine and Surgical Care. Secure Messaging can substitute for other types of communication and encounters and may improve the quality of in-person visits. See the following website for details: [http://vaww.va.gov/MYHEALTHEVET/Secure\_Messaging.asp](http://vaww.va.gov/MYHEALTHEVET/Secure_Messaging.asp)
3. Encounters are neither occasions of service nor activities incidental to an encounter for a provider visit. For example, the following activities are considered part of the encounter itself however do not constitute encounters on their own: taking vital signs, documenting chief complaint, giving injections, pulse oximetry, etc.
4. A telephone contact between a health care provider and a patient is only considered an encounter if the telephone contact is documented and that documentation include the appropriate elements of a face-to-face encounter, namely history and clinical decision- making. Telephone encounters must be associated with a clinic, that is assigned one of the DSS Identifier telephone codes and are to be designated as count clinics. NOTE: Count refers to workload meeting the definition of an encounter or an occasion of service.
5. Program Support staff cannot enter encounters in CPRS for workload credit. They can document using the HT Tech Education Note which is a non-count clinic; or use HT Note and mark it Historical.

Crosswalk for Clinic Location and CPT Codes, see Appendences

#### Encounter Form Completion:

1. The Encounter Form is very important for capturing clinical work.
2. Any clinical activity that involves professional contact (as described above) with the Veteran should be recorded in an encounter.
3. Elements to be completed in the encounter:
    1. Service Connection
    2. Diagnosis
    3. Procedure – CPT codes
4. Professional contact can be either face to face or via telecommunications.
    4. When a note is written related to interaction with the Veteran/Caregiver you are required to do an encounter unless the clinic is non-count.
    5. When you do not have professional contact with the Veteran you must use the correct note title but you must click Historical to indicate that the note does not meet the requirements of an encounter.
5. CPT Codes specific to HT activities need to be selected in the encounter form.

#### Completing an Encounter

1. Complete the type of visit. Choose the appropriate selection for that visit under section name. Be sure to answer the Veteran Service Connection question under the “Visit Related To” box when appropriate.
<!-- image -->

1. Complete encounter information be selecting the appropriate tab(s) and completing the section.

#### Data Objects

The Home Telehealth templates include data objects. Data objects allow for information to be pulled into the note from another part of the patient’s record.

The new HT data objects (in the HT templates) are listed below:

- ADMISSIONS PAST YEAR
- CONSULTS PAST(6M)
- GEC IADLS (LAST)
- GEC BASIC ADLS (LAST)
- HT BARRIERS TO LEARNING
- HT BASIC ADLS
- HT CAREGIVER
- HT CATEGORY OF CARE LAST
- HT CONTINUUM OF CARE LAST
- HT EMERGENCY PRIORITY RATING
- HT ENROLLMENT START
- HT IADLS
- HT MED RECON
- HT NIC/CCM RATING LAST
- HT REMINDERS DUE
- HT VETERAN’S GOAL
<!-- image -->
- NEXT OF KIN
- OUTPT APPTS PAST YR

17 *July 2017*

The data objects are shown in the appendix; in the screen shots of the templates to the right – they are circled in *RED* .

#### Health Factors

Reminder Dialog Templates include over 200 health factors. Health factors allow storage of pieces of health information in the patient’s record. They are organized into categories, which can be seen on Health Summaries and in data object displays in templates.

They can be extracted and used for reporting on reminder completion rates, performance, and workload. They are also extracted and located in the VSSC data cubes (also known as Pyramid) which allow reports to be created.

Health factors are linked to options in reminder dialogs. Once that item is selected, the health factor is placed in the encounter form. They are displayed in the bottom window of reminder dialogs/reminder templates (example below)

The national templates should not be edited or revised at the local or VISN level to maintain the integrity of the data collected as well as ensure any further national revisions or updates are appropriately captured and standardized. There can be changes made to the templates after their release but changes will be done at the National level for all templates. This too ensures the integrity of data pulled.

#### HT Education Topics

Education topics are similar to health factors, except they are used to capture information specifically regarding patient education. Five new Education Topics (a parent topic and four sub- topics) are deployed in this patch linked to specific items across the new HT template set.

VA-HOME TELEHEALTH (HT)

VA-HOME TELEHEALTH-IN HOME MONITORING

VA-HOME TELEHEALTH-DISEASE MGMT/PATIENT SELF-MGMT VA-HOME TELEHEALTH-MEDICATION MANAGEMENT

VA-HOME TELEHEALTH-CAREGIVER EDUCATION/SUPPORT

These were developed with guidance from the HT leadership. These items are stored in VISTA and would automatically display on your site's PATIENT EDUCATION Health Summary (if your site has one). Here's a sample at Puget Sound:

These education topics also have an OPTIONAL rating in the template, so that you can rate the patient/caregiver’s LEVEL OF UNDERSTANDING for a specific education topic. The small LOWEST window in a reminder template shows the patient education item (2 nd circle in *red* on the image below). Example:

<!-- image -->

The selections in the **“Level of Understanding”** drop-down picklist are:

### HT Clinical Reminders

Four new CLINICAL REMINDERS for Home Telehealth are included in this patch. Each will display in the “Clinical Reminders” section of the CPRS cover sheet when it comes due.

1. **HT Continuum of Care** ***(Initial Continuum of Care)*** (CCF, Continuum of Care Form)

The trigger for this reminder to become “DUE” is the HT ASSESSMENT TREATMENT PLAN template which includes the enrollment start date.

- This reminder is inactivated if the patient is discharged from HT or expires ( the HT Discharge template must be used for discharging the patient from HT ).

- This reminder is resolved by completing the HT CONTINUUM OF CARE template and selecting “INITIAL” at the top of the template.

- This reminder is due only ONCE in a course of HT care (enrollment through discharge).

##### HT Continuum of Care (Follow-Up) – (triggers with a 2-week lead time)

This reminder becomes DUE two weeks before the 6-month period for a patient that is still a HT-enrolled Veteran and who continues to meet NIC (Non-Institutional Care) criteria or CCM (Chronic Care Management) when the previous Continuum of Care was done.

- This reminder is inactivated if the patient is discharged from HT or expires ( the HT Discharge template must be used for discharging the patient from HT ).

- This reminder is inactivated if the patient is *reassessed* via use of the HT CONTINUUM OF CARE TEMPLATE and is rated DOES NOT MEET NIC CRITERIA or CCM CRITERIA, even though the patient is still enrolled in HT. If a Veteran has a change in their status and is now NIC or CCM, or if they were classified HPDP due to partial responding and their response rates improves, a new CCF will need to be done which will re-set the clinical reminder.

- This reminder is resolved by completing the HT CONTINUUM OF CARE template and selecting the "FOLLOW-UP" item at the top of the template.

##### HT Caregiver Assessment

This reminder is triggered after the HT CONTINUUM OF CARE (INITIAL) template has been done and if the patient has an UNPAID CAREGIVER (an item with a health factor that is in that template).

- This reminder is inactivated if the patient is discharged from HT or expires ( the HT Discharge template must be used for discharging the patient from HT ).

- This reminder is resolved by completing the HT Caregiver Assessment template (the Caregiver Risk Assessment section, which is the set of 4 questions with 5 answers each).

##### HT Periodic Evaluation (triggers with a 2-week lead time)

This reminder becomes DUE 166 days after the patient has a HT ENROLLMENT START DATE filed in VISTA ( *that template item is in the HT ASSESSMENT TREATMENT PLAN templat* e) and can be reset by your CAC as previously noted to coincide with program polices.

- This reminder is set to trigger every 166 (or per program policy) days if the Veteran remains enrolled in HT.

- This reminder is inactivated if the patient is discharged from HT or expires ( the HT Discharge template must be used for discharging the patient from HT ).

- This reminder is resolved by completing the HT PERIODIC EVALUATION template.

### Clinical Reminder Process

#### How to satisfy Clinical Reminders

1. A reminder will display in the “Clinical Reminders” section of the CPRS cover sheet when it becomes due. The status will display as:
    1. “DUE NOW” indicating the intervention is due for the patient.
    2. A date indicating the intervention is past due and was due on that date.
    3. “DUE SOON” indicating the intervention should be addressed soon.

1. Clicking on a reminder on the cover sheet displays the details of the reminder and the health factor that established the reminder timeline.

1. To complete the reminder, go to the notes section, select new note, then select the appropriate clinic and progress note and then complete the assessment due. (see below example)

### How to Run a “Reminders Due” Report

Reminder Due reports are reports which use the reminder logic to display a list of patients who have the reminder due for the specified timeframe in the report.

1. Request that the facility CAC assign the appropriate staff the 6 reminders due report templates.

1. Reminder Due reports are run from VistA, not CPRS.

1. At the “Select” menu option, type “^Reminders due report” or access the reminder due reports option by following instructions from local CACs.

1. At the Select Report Template: type in **HT**

1. Your **HT reminder templates** will be displayed. Indicate the number of the report you wish to run.

Select REPORT TEMPLATE:

1. HT (4) REMINDERS SUMMARY
2. HT C/G RISK ASSESSMENT
3. HT CCF FOLLOW-UP
4. HT CCF INITIAL 2
5. HT PERIODIC EVALUATION

Selecting number 1 will give you a summary report of all the reminders due. Numbers 2-5 will give you a report for that **specific** reminder.

<!-- image -->

HT Leads: Contact your designated CAC (whoever created your reminder due report templates) at your facility when a NEW HT clinic is created, as the reminder templates are configured to HT clinics that were created by individual name when the CAC built the reminder report template.

## 4 Getting Started

### Complete the New Mini-template for Previously Enrolled HT patients

There is a new, small template for HT use only. This template is **to be used ONLY on patients who are CURRENTLY ENROLLED in Home Telehealth before the new HT National Templates were installed and activated at your VA facility.** This template has three purposes:

1. To provide a means to add the HT ENROLLMENT STARTING DATE to the patient’s electronic record. This added health factor is needed:

1. to provide the data object for HT ENROLLMENT STARTING DATE in the HT DISCHARGE TEMPLATE ( *otherwise it’ll be ‘No data available’)*

1. To trigger the HT PERIODIC EVALUATION clinical reminder.

1. *CoP requires this evaluation/documentation to be done no later than 180 days from the previous evaluation however programs can set their own policies for when this is due as long as it does not exceed 180 days. The clinical reminder in the patch is currently set for 160 days to provide a lead time. CACs can adjust the default to correspond with local policies i.e. every 90 days.*

1. To provide a means to trigger the HT CONTINUUM OF CARE (FOLLOW-UP) clinical reminder every 6 months after the HT CONTINUUM OF CARE (INITIAL) has been done, if the patient continues to meet NIC (Non-Institutional Care) or Chronic Care Management (CCM) criteria.

The local CAC will notify the site Lead or Program Manager when the patch is loaded and ready for use. It should be used to enter the appropriate information and date for the three items requested.

Staff should notify the HT site Lead when this template has been completed for ALL Home Telehealth patients currently enrolled for which the HT ASSESSMENT TREATMENT PLAN TEMPLATE was not documented. This template will be phased out (removed) when all patients that need this documentation has been done. The local CAC will need to remove this template from the shared folder in CPRS.

Programs should devise a system to determine which patients the template has been completed. A TIU report for the 3 health factors can be created by the local CAC. Veterans being enrolled when the templates come out will not need the mini template **(as long as the NEW Template that captures the information is in use.)**

Staff should use the "HT Note" title to enter this template in CPRS. MARK IT HISTORICAL. Staff will not need to complete an encounter for this one time note.

1. Find and open the template named HT Template for Previously Enrolled Patients from the Notes tab in CPRS. Contact the local CAC to identify where the template is located within CPRS.

1. First item in the template is documentation of the date the veteran was enrolled in Home Telehealth
<!-- image -->
    - Make sure to fill out the DAY of the month as well as the correct month and year.

1. The second item opens to the NIC/CCM categorization. The “YES” answers have a required fill-in for the date. The “NO” answer doesn’t expand. If no, they are likely classified HPDP, and the CCF does not have to be repeated unless there is a change in their condition.
<!-- image -->

<!-- image -->

- If it is a newly enrolled patient, enter their **date of admission** when the initial Continuum of Care form was completed.

- Make sure to fill out the DAY of the month as well as the correct month and year.

- To meet our VERA requirements both NIC and CCM require CCF updates every 6 months.

1. The 3 rd item asks when the LAST periodic evaluation was done which will trigger the HT PERIODIC EVALUATION clinical reminder on the appropriate date.

1. If a newly enrolled patient is not yet due for a periodic evaluation because they have been in the program less than the number of days required for review per policy (90, 120, 180 days etc.), still answer YES and **enter the enrollment date** as the date of last periodic review.

1. If “No” is documented here, a clinical reminder will automatically populate that a Periodic Evaluation is due now – despite the fact the patient has only been in the program less than the required number of days for review. The ‘no’ item does not expand any further.

1. The local site CAC can adjust the time frame the HT PERIODIC EVALUATION clinical reminder is due depending on your local policy.

<!-- image -->

- Make sure to fill out the DAY of the month as well as the correct month and year.

<!-- image -->

10. When done, click the **FINISH** button at the bottom of the form. If you still have questions about this template, please contact your site’s **HT Lead.**

**X WRONG NOTE/WRONG PATIENT** : If a template is documented on the wrong patient make sure data cleanup occurs, so encounter data as well as the note is removed from the patient record. Notify your HIMS (Health Information Management Service) to do this cleanup.

## 5 Templates and Program Enrollment

HT program services begin when consults are completed and Veterans are screened. The “HT Screening Consult” note is completed and if the Veteran is enrolled, the Care Coordinator proceeds with the enrollment process and required documentation using the templates and note titles covered in this user guide. VISN and local program leadership should ensure staff have been properly trained on choosing the appropriate clinic location, note title, and

template. Training is also provided by the Implementation Team.

Below are the new templates with guidance on their use. They appear in order of the enrollment process.

### Home Telehealth Consult Request.

A new template will be embedded in the local consult order for Home Telehealth services. The provider will click on the consult order and launch the template: (Sites have found it helpful to inform their Providers that they will see a new version of the HT Consult.)

Below is the Enrollment Consult Template

<!-- image -->

<!-- image -->

<!-- image -->

The consult should be completed by HT staff using the HT SCREENING CONSULT note title; this title generates the progress note and is used to CLOSE the consult.

There are two ways to access the consult request for consult completion:

1. Completing the HT SCREENING CONSULT note from the Consult tab in CPRS
2. Completing the HT SCREENING CONSULT note from the Notes tab in CPRS

#### Completing the HT SCREENING CONSULT note from the CPRS consult tab

If you are **certain** that your patient **does not meet the enrollment criteria,** do not open the template that closes the consult because this will use your time unnecessarily. We recommend that you cancel the consult (or follow local guidance) and add comments to the provider why the Veteran is not a candidate for enrollment.

1. If processing a “new consult” alert, the CONSULTS tab will open on that specific consult request or the consult can be accessed by clicking on the CONSULTS tab, then select the HT consult request.

1. The local consult may have a different name than displayed in the screenshots

1. Click on ACTION, then drop down to CONSULT RESULTS, then mouse over to “COMPLETE/UPDATE Results”:

**HOME TELEHEAL**

1. Select the appropriate Visit, Clinic Location (was the encounter by phone, in clinic or Veterans’ home), and date/time (if veteran isn't an inpatient). Click “OK”.
2. Select the “ **HT SCREENING CONSULT Note** ” note title.
<!-- image -->

1. This is the only note title that should be used to complete/close the consult. **You can** set this single HT consults note title as a **DEFAULT** note title on the CONSULTS tab. **Here's how to do this:**

<!-- image -->

1. Go to TOOLS, then OPTIONS (Each VA site will have a different list of TOOLS menu items, but all have OPTIONS):

1. Go to the **NOTES tab** and click the **“Document Titles”** button:
<!-- image -->

1. Under **“Document class”** , select **CONSULTS** from the drop-down pick list:

<!-- image -->

1. Select the **HT SCREENING CONSULT** Note title.

1. Click the **ADD** (the ADD button is an option prior to adding the document title) button to move that note title to the **RIGHT** window ('your list of titles').

The Note Title will move to the right window.

1. To set it as the **DEFAULT** note title on the **CONSULTS tab** (so that it is automatically preselected as the title to close your consult requests), click on the title in the right-hand window, and then click the **'SET AS DEFAULT'** button.

1. Now click the **OK button to save** your changes.

(If you want to *REMOVE* a title, simply select it so it is highlighted in the right-hand window, and then click the *REMOVE* button.)

#### Completing the HT SCREENING CONSULT note from the CPRS Notes tab

1. Select the NOTES tab

1. Click on NEW NOTE
<!-- image -->

1. Select the correct clinic location. The correct clinic to select would be the **HT Screening Office** or **Telephone or Home** ; depending on where the vet was screened.

1. Select the **HT SCREENING CONSULT** note title, as it is the ONLY HT Note Title that links to a consult request. Once the note title is selected, a list of consult requests for that patient will display.

1. Any consult for that patient that the author has authorization to complete will display, so other consults may be in the list. Ensure to only select the Home Telehealth consult.

1. Highlight the consult request and then click OK to make the link to the consult and then close the window.

1. The template will open.
<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

### TECH EDUCATION AND INSTALLATION

Below are the Tech Education and Installation Template

<!-- image -->

This template incorporates what is usually discussed with Veterans/Caregivers at enrollment related to technology use. It can be used by support staff.

<!-- image -->

### ASSESSMENT TREATMENT PLAN

Below is the Assessment Treatment Plan Template

The screen shots taken below are in sequence to how the Template flows.

Boxes will open and may ask additional information for example, when you hit the box “Veteran consents to participate in the HT Program this is what you will see:

The template training provided by the Implementation Team discusses various items of interest in the templates such as what goes in the “Discussion details” box and why.

Note: The Joint Commission requires all providers to do an assessment of oxygen safety. This is included **above** noted by the arrow.

Next is the following

As stated previously, some fields are optional, and remember to add detail in text boxes.

<!-- image -->

Medication Interventions is located after Medication Management which ties the topics together in one place

<!-- image -->

<!-- image -->

Living Arrangements/Environmental Safety is mostly about environmental safety, not living arrangements. The CCF (Continuum of Care Form) identifies some of this information; you may decide to go over living arrangements and the Veterans support system in your summary.

Note: The CCF template can be launched here or can be a free-standing note. If you put it here the note can be very long. If you do not include it here, you will need to ensure clinical information located in the form is discussed in your assessment in order to be comprehensive and identify problems the Veteran is facing. Screen shots of the CCF are below.

The Caregiver Risk Assessment is linked to the Zarit Burden Scale if there is an unpaid caregiver. This template can also be done as a free-standing note.

Referrals for Caregiver/Veteran assistance opens to many choices related to assistance that might be needed for the Veteran and or Caregiver

<!-- image -->

Please refer to the Continuity of Operations Guidance (CooP) located on the HT Web page [http://vaww.telehealth.va.gov/pgm/ht/index.asp](http://vaww.telehealth.va.gov/pgm/ht/index.asp) . The template not only includes determining a level of priority for contacting a Veteran after a disaster but also includes discussing disaster planning with them which is also part of CooP.

<!-- image -->

This completes the Admission Assessment Template. If you hit “Phone” on “Type of encounter” it populates your encounter for you.

##### Edit your note in CPRS before signing it.

You can paste your own sub-templates at this time into the document but this should not replace completing required fields in the template as health factors are imbedded.

### CONTINUUM OF CARE FORM (CCF)

Below is the Continuum of Care Form Template

<!-- image -->

For help completing the CCF refer to the Continuum of Care Guidance and Patient Participation Guidance documents on the HT Home page [http://vaww.telehealth.va.gov/pgm/ht/index.asp](http://vaww.telehealth.va.gov/pgm/ht/index.asp)

Pay attention to “Assessment type”, you only choose “Initial assessment” **one time** , the rest are follow up. The date you complete the CCF updates the clinical reminder.

Note: if you have Veterans classified HPDP due to partial respondering you will not get a clinical reminder for the CCF however if their response rates improve to over 70% in a 3 month period do a CCF (NOT INITIAL..IT IS STILL A FOLLOW UP) to identify the classification to NIC or CCM (change it in Vendor software too so they get counted for VERA reimbursement).

The CCF template pulls in the Next of Kin from CPRS for your convenience. Although the template allows you to update the information, it does NOT update the change in CPRS. You should follow local procedures for updating demographics.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

### CAREGIVER RISK ASSESSMENT

Below is the **Caregiver Assessment Template** :

The Zarit Caregiver Burden Scale is embedded in the Caregiver Risk Assessment template.

<!-- image -->

<!-- image -->

The Caregiver Risk Assessment **MUST** be completed if the Veteran has an unpaid caregiver. Sometimes staff members have found that the caregiver feels uncomfortable answering these questions in front of the Veteran. You can be creative and have this already printed out for the caregiver to complete while you are talking with the veteran, or even perhaps mail this to the caregiver with a self-addressed stamped envelope.

Note: This clinical reminder is different. The reminder is active when you hit the radial button “Unable to screen” but does not show up in CPRS for 7 days allowing you time to try and reach the caregiver. If you do not complete the screening, the clinical reminder stays on until you do.

(Note: other staff doing the Zarit Burden, use the same template so there is a possibility the clinical reminder will be completed by someone other than HT staff, most likely Social Workers)

<!-- image -->

The intent here is to assess how our caregivers are doing, not just completing a form. Anytime you sense a caregiver is not doing well you can complete the Zarit Burden and make a referral to Social Work.

### INTERVENTION NOTE

The following is the HT Intervention Note (684).

The intervention note is used anytime an intervention is made based on out of range responses received from the Veteran’s technology.

<!-- image -->

Any subjective or objective information that is not a measurement would go into the additional information text box. Clinicians then document (in the assessment text box) their assessment based upon any of the above information. The “Intervention/Plan:” section is what the care coordinator did, suggest, or recommends. It should include Veterans input and responses.

Documentation should also include communication and collaboration with other staff or programs, updates, or revisions to the Veteran’s plan of care and/or services.

### MONTHLY MONITOR NOTE

Below is the **Monthly Monitor Note** .

This note does not require provider cosigning and should not have clinical information. This is the (683) note for counting enrollees nationwide, is required for VERA reimbursement, and allows staff to get work load credit for time spent reviewing Veteran alerts to their daily session received from technology.

<!-- image -->

This is not like other templates; it is a boiler plate which is populated. Most programs use a “Group Note” to enter this on all their Veterans. It is to be entered near the end of the month. There used to be guidance that a Diagnosis is required in this note however National HIMS (Health Information Management Service) guidance has exempted this for HT since there is no billing associated with this. Follow your local guidance if different.

Contact your local “Group Note” specialist if you do not know how to use “Group Notes”.

### PERIODIC EVALUATION

Two full templates are embedded in the Periodic Evaluation Template:

1. HT Caregiver High Risk Screen *(optional section)*
2. HT Caregiver/Veteran Referral template *(optional section)*

The Periodic Evaluation Template is used to re-assess/evaluate the Veterans status and update the Veteran’s provider and plan of care. It has to be completed no later than every 180 days. A

program that’s polices call for reevaluation at a different time frame i.e. every 90 days, can have the reminders set accordingly (but NOT to exceed 180 days).

<!-- image -->

Below is the Periodic Evaluation

Note: at the top, it will display if there are clinical reminders due and the date last HT CCF was completed. THERE IS NO LINK TO THE CCF FROM THIS TEMPLATE.

The first question you come to is “Veterans Current HT Category of Care”. If the CCF is due, in order to accurately answer this question, you will need to complete the form before you populate the template. Some options include: you can complete the CCF template using the CCF Form

<!-- image -->

note title and mark the encounter historical; you can make it an addendum to the Periodic Note as long as you have the accurate information to identify the current level of care.

This template has "Veteran Health Education". This box opens to extensive options for education related to Home Telehealth-specific, or General Topics, see below.

This was not put in the Admission Assessment Treatment Plan due to its length; it is expected the initial clinical summary and plan of care will identify education given upon admission.

<!-- image -->

Including this sub template in the Periodic template accounts for more time to have worked with the Veteran and cover education provided during the review period and beyond.

The above “Caregiver utilization of referrals” is only used if a referral has been **previously** submitted. Also, please note at this point **you need to revisit** the caregiver risk assessment and referral **if** the Veteran has an unpaid caregiver.

### EMERGENCY MANAGEMENT CLASSIFICATION

The **Emergency Management Classification** is re-addressed in **every periodic** evaluation or according to program polices.

The Disaster Plan is also completed reflecting information or assistance extended to the Veteran or Caregiver.

<!-- image -->

### DISCHARGE TEMPLATE

Below is the Discharge Template

This is to be completed when the Veteran is discharged from the program. Remember, doing this note turns off all clinical reminders. For this reason if you end up re enrolling a Veteran, even within 30 days, an Admission Assessment and Treatment Plan Template will need to be completed.

<!-- image -->

<!-- image -->

### Other:

### VIDEO VISIT

Below is the Video Visit Template

Video visits have not occurred in HT during the previous contract with Vendors (prior to June 2017). With the new 2017 contract, Video Visits is (or will be, depending on the Vendor) an

<!-- image -->

option. However National Telehealth guidance has not been provided at the time of this manuals publication.

<!-- image -->

Troubleshooting

*N/A*

## a. Acronyms and Abbreviations

| ***Abbreviation***   | ***Definition***                                    |
|----------------------|-----------------------------------------------------|
| CoP                  | Conditions of Participation                         |
| CPRS                 | Computerized Patient Record System                  |
| CPT                  | Current Procedural Terminology                      |
|                      |                                                     |
| GEC                  | Geriatric E Care                                    |
| GMTS                 | Health Summary (VistA software package)             |
| GUI                  | Graphical User Interface                            |
|                      |                                                     |
| HT                   | Home Telehealth                                     |
| ICD-9                | International Classification of Diseases            |
|                      |                                                     |
| OCC                  | Office of Connected Care                            |
|                      |                                                     |
| TIU                  | Text Integration Utilities (Vista software package) |

Appendix

Crosswalk Note Titles, Stop Codes, and Definitions **Option 1** programs

| **Current Clinic Location**                                                      |   **Prim. Stop Code** |   **Sec. Stop Code** | **Note Titles**               | **Templates**                  | **Definition**                                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------|-----------------------|----------------------|-------------------------------|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **HT SCREENING OFC**                                                             |                   685 |                  371 | HT Screening Consult          | HT  Screening Consult Template | This consult document is used to document initial evaluation for enrollment WHETHER OR NOT the patient is actually enrolled.  **NOTE:**  Use to close consult                                                                                                                                                                                                       |
| **HT SCREENING TC**  **or**  **HT SCREENING PHONE**  **or**  **HT SCREENING PH** |                   686 |                      |                               |                                |                                                                                                                                                                                                                                                                                                                                                                     |
| **HT TECH EDUCATION**                                                            |                   674 |                  685 | HT Tech Education Note        | HT Tech Education Template     | This document contains patient education, skill validation and installation for technology on all HT patients.  NOTE: ALWAYS attached to the coding pair 674/685 (Non- Count)  Use as often as needed when re-educating the patient on technology, changing or troubleshooting technology or adding new peripheral devices. Training/Education on  technology only. |
| **HT INTERVENTION**                                                              |                   686 |                  684 | **HT**  **Intervention Note** | HT  Intervention Template      | This progress note contains information about all interventions generated from symptoms, behavior and knowledge data gathered from daily monitoring by a non-video messaging device.  **NOTE:**  Use  **ONLY**  to  document patient encounters in response to alerts from vendor data- not to be used as generic note, and not to be used with  VIDEO visit.       |

| **HT MONTHLY MONITOR**                                                                          | 683        |   685 | **HT Monthly Monitor Note**                                                                                                                                                        | HT Monthly Monitor Template            | This progress note contains information about the monthly monitoring of patients assigned non-video messaging devices.  **NOTE:**  To be completed for patients to capture workload for daily review of HT data. Please see the HT Operations manual for more detailed instructions on how to properly use this encounter.                          |
|-------------------------------------------------------------------------------------------------|------------|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **HT VIDEO VISIT**                                                                              | 685        |   179 | HT Video Visit Note                                                                                                                                                                | HT Video Visit Template                | This document contains information about any visit over a video device (tele-Monitor/ Videophone) that meets required criteria for secondary Stop Code xxx179  **NOTE:**  Must meet certain documentation requirements of replicating a face-to-face visit or it can’t be coded as 179                                                              |
| **HT ASSESS TX PLAN HM**                                                                        | Home 118   |   685 | HT  Assessment Treatment Plan                                                                                                                                                      | HT  Assessment Treatment Plan Template | This document contains information about the visit with the patient/caregiver which includes the clinical assessment and the HT Plan of Care. Additional signature is requested by the Primary Care Provider (and others, including program staff, as appropriate).Additional time needs to be allocated in DSS upon setup for this Clinic Location |
| **HT ASSESS TX PLAN TC**  **or**  **HT ASSESS TX PLAN PHONE**  **or**  **HT ASSESS TX PLAN PH** | TC 686     |       |                                                                                                                                                                                    |                                        |                                                                                                                                                                                                                                                                                                                                                     |
| **HT ASSESS TX PLAN OF**  **or**  **HT ASSESS TX PLAN OFC**                                     | Clinic 685 |       |                                                                                                                                                                                    |                                        |                                                                                                                                                                                                                                                                                                                                                     |
| **HT VISIT TC**  **or**  **HT VISIT PHONE**  **or**  **HT VISIT PH**                            | 686        |   685 | **FIRST, select the HT Clinic Location (left) where the visit is taking place:**  1. **By telephone (TC, Phone, PH)** 2. **In the office (OFC)** 3. **At the patient's home (HM)** |                                        |                                                                                                                                                                                                                                                                                                                                                     |
| **HT VISIT OFC**                                                                                | 685        |       |                                                                                                                                                                                    |                                        |                                                                                                                                                                                                                                                                                                                                                     |
| **HT VISIT HM**                                                                                 | 118        |   685 |                                                                                                                                                                                    |                                        |                                                                                                                                                                                                                                                                                                                                                     |

| **SECOND**  **, select a Note Title/Template (right) to pair with the clinic location (above)**   |                                     |                                     | HT Discharge Note                   |                                     | HT  Discharge Template              |                                                                                                                                                           | This Document contains closure of the patients’ case and discharge from the HT program. Basically, this note is a discharge summary.  NOTE: Designed to facilitate closing the case of a HT patient. May have an encounter attached to it if the discharge is done by telephone or office visit. Will not have an encounter if patient is not present.   |
|---------------------------------------------------------------------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                   |                                     |                                     | HT Note                             |                                     | N/A                                 |                                                                                                                                                           | Generic Note title to encompass all other HT activities. This note title does not have a template.                                                                                                                                                                                                                                                       |
|                                                                                                   |                                     |                                     | HT Periodic Evaluation Note         |                                     | HT Periodic Evaluation Template     |                                                                                                                                                           | Periodic review and upgrade of the plan of care  NOTE: Summarization of care for a period of time. Interval dependent on VISN/Program.                                                                                                                                                                                                                   |
|                                                                                                   |                                     |                                     | HT Continuum of Care Note           |                                     | HT  Continuum of Care Template      |                                                                                                                                                           | Note title to be used with the Continuum of Care clinical reminder dialog  NOTE: Initial CCF will be included in the Assessment Treatment Plan template. This note title to be used thereafter.                                                                                                                                                          |
|                                                                                                   |                                     |                                     | HT Caregiver Assessment             |                                     | HT  Caregiver Assessment Template   |                                                                                                                                                           | NOTE: Will combine both the High-risk Screen & referral for assistance in one note title and template.                                                                                                                                                                                                                                                   |
| Additional Note Titles in the Patch                                                               | Additional Note Titles in the Patch | Additional Note Titles in the Patch | Additional Note Titles in the Patch | Additional Note Titles in the Patch | Additional Note Titles in the Patch | Additional Note Titles in the Patch                                                                                                                       | Additional Note Titles in the Patch                                                                                                                                                                                                                                                                                                                      |
| **HT CASE MGMT TC**  **or**  **HT CASE MGMT PHONE**  **or**  **HT CASE MGMT PH**                  |                                     |                                     | HT  Telephone Case Management       | N/A                                 |                                     | This note title is no longer approved by the Office of Connected Care. If they are available through the patch, do not use them. Use the HT Note title  . |                                                                                                                                                                                                                                                                                                                                                          |
| **HT CASE MGMT OFC**                                                                              |                                     |                                     | HT  Telephone Case Management       | N/A                                 |                                     | This note title is no longer approved by the Office of Connected Care. If they are available through the patch, do not use them. Use the HT Note title    | This note title is no longer approved by the Office of Connected Care. If they are available through the patch, do not use them. Use the HT Note title                                                                                                                                                                                                   |

**Current Clinic Location**

**Prim. Stop Code**

**Sec. Stop Code**

Program Dependent (Prog Dep.) Clinic

**HT SCREENING TC**

This document contains patient education, skill validation and installation for technology on all HT patients.

This progress note contains information about all interventions generated from symptoms, behavior and knowledge data gathered from daily monitoring by a non-video messaging device.

**Note Titles**

**Templates**

**Definition**

Code

**or**

Prog. Dep Phone Code

**HT SCREENING OFC**

This consult document is used to document initial evaluation for enrollment WHETHER OR NOT the patient is actually enrolled.

**HT SCREENING PHONE**

NOTE: ALWAYS attached to the coding pair 674/685 (Non-Count) Use as often as needed when re- educating the patient on technology, changing or troubleshooting technology or adding new peripheral devices. Training/Education on technology only.

**NOTE:** Use **ONLY** to document patient encounters in response to alerts from vendor data- not to be used as generic note, and not to be used with VIDEO visit.

HT

**or**

HT

Screening Consult Template

**NOTE:** Use to close consult

**HT SCREENING PH**

Prog. Dep Phone Code

371

Screening Consult

HT Tech Education Note

HT Tech Education Template

**HT INTERVENTION**

684

**Intervention Note**

Intervention Template

**HT TECH EDUCATION**

674

685

Crosswalk Note Titles, Stop Codes, and Definitions **Option 2** programs

| **HT MONTHLY MONITOR**                                                                          | 683                   |   Prog. Dep. | **HT Monthly Monitor Note**                                                                                                                                                        | HT Monthly Monitor Template            | This progress note contains information about the monthly monitoring of patients assigned non-video messaging devices.  **NOTE:**  To be completed for patients to capture workload for daily review of HT data. Please see the HT Operations manual for more detailed instructions on how to properly use this encounter.                          |
|-------------------------------------------------------------------------------------------------|-----------------------|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **HT VIDEO VISIT**                                                                              | Prog Dep              |          179 | HT Video Visit Note                                                                                                                                                                | HT Video Visit Template                | This document contains information about any visit over a video device (tele-Monitor/ Videophone) that meets required criteria for secondary Stop Code xxx179  **NOTE:**  Must meet certain documentation requirements of replicating a face-to-face visit or it can’t be coded as 179                                                              |
| **HT ASSESS TX PLAN HM**                                                                        | Prog and Location Dep |          685 | HT  Assessment Treatment Plan                                                                                                                                                      | HT  Assessment Treatment Plan Template | This document contains information about the visit with the patient/caregiver which includes the clinical assessment and the HT Plan of Care. Additional signature is requested by the Primary Care Provider (and others, including program staff, as appropriate).Additional time needs to be allocated in DSS upon setup for this Clinic Location |
| **HT ASSESS TX PLAN TC**  **or**  **HT ASSESS TX PLAN PHONE**  **or**  **HT ASSESS TX PLAN PH** |                       |              |                                                                                                                                                                                    |                                        |                                                                                                                                                                                                                                                                                                                                                     |
| **HT ASSESS TX PLAN OF**  **or**  **HT ASSESS TX PLAN OFC**                                     |                       |              |                                                                                                                                                                                    |                                        |                                                                                                                                                                                                                                                                                                                                                     |
| **HT VISIT TC**  **or**  **HT VISIT PHONE**  **or**  **HT VISIT PH**                            | Prog. Dep Phone Code  |          685 | **FIRST, select the HT Clinic Location (left) where the visit is taking place:**  1. **By telephone (TC, Phone, PH)** 2. **In the office (OFC)** 3. **At the patient's home (HM)** |                                        |                                                                                                                                                                                                                                                                                                                                                     |
| **HT VISIT OFC**                                                                                | Prog. Dep Clinic Code |          685 |                                                                                                                                                                                    |                                        |                                                                                                                                                                                                                                                                                                                                                     |
| **HT VISIT HM**                                                                                 | 118 or Prog Dep       |          685 |                                                                                                                                                                                    |                                        |                                                                                                                                                                                                                                                                                                                                                     |

| **SECOND**  **, select a Note Title/Template (right) to pair with the clinic location (above)**   |                        |                        | HT  Discharge Note            | HT  Discharge Template             | This Document contains closure of the patients’ case and discharge from the HT program. Basically, this note is a discharge summary.  NOTE: Designed to facilitate closing the case of a HT patient. May have an encounter attached to it if the discharge is done by telephone or office visit. Will not have an encounter if patient is not present.   |
|---------------------------------------------------------------------------------------------------|------------------------|------------------------|-------------------------------|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                   |                        |                        | HT Note                       | N/A                                | Generic Note title to encompass all other HT activities. This note title does not have a template.                                                                                                                                                                                                                                                       |
|                                                                                                   |                        |                        | HT Periodic Evaluation Note   | HT Periodic Evaluation Template    | Periodic review and upgrade of the plan of care  NOTE: Summarization of care for a period of time. Interval dependent on VISN/Program.                                                                                                                                                                                                                   |
|                                                                                                   |                        |                        | HT  Continuum of Care Note    | HT  Continuum of Care Template     | Note title to be used with the Continuum of Care clinical reminder dialog  NOTE: Initial CCF will be included in the Assessment Treatment Plan template. This note title to be used thereafter.                                                                                                                                                          |
|                                                                                                   |                        |                        | HT  Caregiver Assessment      | HT  Caregiver Assessment  Template | NOTE: Will combine both the High-risk Screen &amp; referral for  assistance in one note title and template.                                                                                                                                                                                                                                              |
| Additional Note Titles                                                                            | Additional Note Titles | Additional Note Titles | Additional Note Titles        | Additional Note Titles             | Additional Note Titles                                                                                                                                                                                                                                                                                                                                   |
| **HT CASE MGMT TC**  **or**  **HT CASE MGMT PHONE**  **or**  **HT CASE MGMT PH**                  |                        |                        | HT  Telephone Case Management | N/A                                | This note title is no longer approved by the Office of Connected Care. If they are available through the patch, do not use them. Use the HT Note title.                                                                                                                                                                                                  |
| **HT CASE MGMT OFC**                                                                              |                        |                        | HT  Telephone Case Management | N/A                                | This note title is no longer approved by the Office of Connected Care. If they are available through the patch, do not use them. Use the HT Note title                                                                                                                                                                                                   |

|                              |                                                 |                                                 |                                                 |                                                                                                                                                                                                                                                                                                                                                    |                              |
|------------------------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| **Clinic Location**          | **MD/NP/PA CPT**                                | **RN CPT**                                      | **SW CPT**                                      | **CPT Comments**                                                                                                                                                                                                                                                                                                                                   | **Note Title / Template**    |
| HT ASSESS TX PLAN OFC        | Face to Face                                    | Face to Face                                    | Face to Face                                    | Records clinical activities with patient by licensed practitioner                                                                                                                                                                                                                                                                                  | HT Assessment Treatment Plan |
|                              | 99201 – 99215                                   | 99211                                           | 99499                                           | Records clinical activities with patient by licensed practitioner                                                                                                                                                                                                                                                                                  |                              |
| HT ASSESS TX PLAN TC (PHONE) | Telephone                                       | Telephone                                       | Telephone                                       | HT is one of the programs under the Office of Patient Care Services that is exempt from the time elements as follows:  The codes can be used when a call is initiated by a provider and the time elements will not apply - such as a visit within past seven (7) days - many of our programs require multiple calls within a seven (7) day period. | HT Assessment Treatment Plan |
|                              | 99441 – 99443                                   | 98966, 98967,  98968                            | 98966, 98967,  98968                            |                                                                                                                                                                                                                                                                                                                                                    |                              |
|                              | 99441: 5-10  mins. of medical discussion        | 98966: 5-10  mins. of medical discussion        | 98966: 5-10  mins. of medical discussion        |                                                                                                                                                                                                                                                                                                                                                    |                              |
|                              | 99442: 11 -20  mins. of medical discussion      | 98967: 11 -20  mins. of medical discussion      | 98967: 11 -20  mins. of medical discussion      |                                                                                                                                                                                                                                                                                                                                                    |                              |
|                              | 99443: 21 -30  mins. of medical discussion      | 98968: 21 -30  mins. of medical discussion      | 98968: 21 -30  mins. of medical discussion      |                                                                                                                                                                                                                                                                                                                                                    |                              |
| HT TECH EDUCATION            | NO ENCOUNTER FORM ATTACHED TO NON-COUNT CLINIC. | NO ENCOUNTER FORM ATTACHED TO NON-COUNT CLINIC. | NO ENCOUNTER FORM ATTACHED TO NON-COUNT CLINIC. | NO ENCOUNTER FORM ATTACHED TO NON-COUNT CLINIC.                                                                                                                                                                                                                                                                                                    | HT Tech Education            |
| HT INTERVENTION              | Telephone                                       | Telephone                                       | Telephone                                       | Records clinical activities with patient by licensed practitioner (See  above)                                                                                                                                                                                                                                                                     | HT Intervention              |
|                              | 99441 – 99443                                   | 98966, 98967,  98968                            | 98966, 98967,  98968                            |                                                                                                                                                                                                                                                                                                                                                    |                              |
| HT MONTHLY MONITOR           | 99091                                           | 99091                                           | 99091                                           | Analysis and interpretation of physiologic data by the physician or other qualified health care professional. The data (e.g., blood pressure) is stored digitally and may be transmitted by the patient and/or the  caregiver to the                                                                                                               | HT Monthly Monitor           |

|                     |                         |                              |                              | physician.                                                                                                                                                        |                        |
|---------------------|-------------------------|------------------------------|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| HT VIDEO VISIT      | 99201 – 99215  GT       | 99211 GT                     | 99499 GT                     | The CPT code  used when this service is delivered face to face is used along with the modifier to denote the telecomm delivery of care  GT = interactive telecomm | HT Video Visit         |
| HT VISIT TC (PHONE) | Telephone99441  – 99443 | Telephone98966, 98967, 98968 | Telephone98966, 98967, 98969 | CPT Codes are dependent on what is done, face to face in the office, in the home, or on the telephone.                                                            | HT Note (no template)  |
| HT VISIT OFC        | 99201 – 99215           | 99211                        | 99499                        | These are real face to face visits in the office.                                                                                                                 | HT Note (no template)  |
| HT VISIT HOME       | 99341 – 99350           | G0154                        | G0155                        | These are real face to face visits in the home.                                                                                                                   | HT Note  (no template) |
|                     |                         |                              |                              |                                                                                                                                                                   |                        |
|                     |                         |                              |                              |                                                                                                                                                                   |                        |
|                     | HT CAREGIVER ASSESSMENT | TBD                          | TBD                          | In development. Recommended that these be captured as collateral and not  under the patient.                                                                      |                        |

2 nd CPT Crosswalk without added column with note titles, easier formatting

| **Clinic Location ***        | **MD/NP/PA CPT**                                | **RN CPT**                                      | **SW CPT**                                      | **CPT Comments**                                                                                                                                                                                                                                                                                                                                      |
|------------------------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HT ASSESS TX PLAN OFC        | Face to Face                                    | Face to Face                                    | Face to Face                                    | Records clinical activities with patient by licensed practitioner                                                                                                                                                                                                                                                                                     |
| HT ASSESS TX PLAN OFC        | 99201 – 99215                                   | 99211                                           | 99499                                           | Records clinical activities with patient by licensed practitioner                                                                                                                                                                                                                                                                                     |
| HT ASSESS TX PLAN TC (PHONE) | Telephone                                       | Telephone                                       | Telephone                                       | CCHT is one of the programs under the Office of Patient Care Services that is exempt from the time elements as follows:  The codes can be used when a call is initiated by a provider and the time elements will not apply - such as a visit within past seven (7) days - many of our programs require multiple calls within a seven  (7) day period. |
|                              | 99441 – 99443                                   | 98966, 98967,  98968                            | 98966, 98967,  98968                            |                                                                                                                                                                                                                                                                                                                                                       |
|                              | 99441: 5-10  mins. of medical discussion        | 98966: 5-10  mins. of medical discussion        | 98966: 5-10  mins. of medical discussion        |                                                                                                                                                                                                                                                                                                                                                       |
|                              | 99442: 11 -20  mins. of medical discussion      | 98967: 11 -20  mins. of medical discussion      | 98967: 11 -20  mins. of medical discussion      |                                                                                                                                                                                                                                                                                                                                                       |
|                              | 99443: 21 -30  mins. of medical discussion      | 98968: 21 -30  mins. of medical discussion      | 98968: 21 -30  mins. of medical discussion      |                                                                                                                                                                                                                                                                                                                                                       |
| HT TECH EDUCATION            | NO ENCOUNTER FORM ATTACHED TO NON-COUNT CLINIC. | NO ENCOUNTER FORM ATTACHED TO NON-COUNT CLINIC. | NO ENCOUNTER FORM ATTACHED TO NON-COUNT CLINIC. | NO ENCOUNTER FORM ATTACHED TO NON-COUNT CLINIC.                                                                                                                                                                                                                                                                                                       |
| HT INTERVENTION              | Telephone                                       | Telephone                                       | Telephone                                       | Records clinical activities with patient by licensed practitioner (See above)                                                                                                                                                                                                                                                                         |
| HT INTERVENTION              | 99441 – 99443                                   | 98966, 98967,  98968                            | 98966, 98967,  98968                            | Records clinical activities with patient by licensed practitioner (See above)                                                                                                                                                                                                                                                                         |
| HT MONTHLY MONITOR           | 99091                                           | 99091                                           | 99091                                           | Analysis and interpretation of physiologic data by the physician or other qualified health care professional. The data (e.g., blood pressure) is stored digitally and may be transmitted by the patient and/or the  caregiver to the physician.                                                                                                       |

| HT VIDEO VISIT      | 99201 – 99215  GT         | 99211 GT                     | 99499 GT                     | The CPT code used when this service is delivered face to face is used along with the modifier to denote the telecomm delivery of care  GT = interactive telecomm   |
|---------------------|---------------------------|------------------------------|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HT VISIT TC (PHONE) | Telephone99441  – 99443   | Telephone98966, 98967, 98968 | Telephone98966, 98967, 98969 | Phone definition noted above.                                                                                                                                      |
| HT VISIT OFC        | 99201 – 99215             | 99211                        | 99499                        | These are real face to face visits in the office.                                                                                                                  |
| HT VISIT HOME       | 99341 – 99350             | G0154                        | G0155                        | These are real face to face visits in the home.                                                                                                                    |
|                     |                           |                              |                              |                                                                                                                                                                    |
|                     |                           |                              |                              |                                                                                                                                                                    |
|                     |                           |                              |                              |                                                                                                                                                                    |
| TBD                 | CCHT CAREGIVER ASSESSMENT | TBD                          | TBD                          | In development. Recommended that these be captured as collateral and not under the patient.                                                                        |