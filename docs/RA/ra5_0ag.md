---
app_name: Radiology/Nuclear Medicine (RA)
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
package_id: RA
patch: null
patch_gap: null
section: ''
source_file: ra5_0ag.docx
status: draft
title: ra5 0ag.docx
---

<!-- image -->

**RADIOLOGY/NUCLEAR MEDICINE**

**ADPAC GUIDE**

**(Package Implementation and Maintenance)**

Version 5.0

January 2026


Health System Design and Development

Revision History

| **Date**       | **Page**                                                   | **Change**                                                                                                                                                                                                                                                                              |
|----------------|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| January 2026   | VII-58                                                     | RA*5.0*226 – New menu option ‘Activate/Inactivate Standard Procedures’ [RA PROCEDURE ACTIVATE] added to the ‘Procedure Edit Menu’ RA PROCEDURE EDIT MENU                                                                                                                                |
| April 2024     | V-7, V-12, V-15                                            | RA*5.0*210 – New division parameter FACILITY PHONE NUMBER added to the Division Parameter Set-up [RA SYSDIV] and Print Division Parameter List [RA SYSDIVLIST].                                                                                                                         |
| September 2022 | VII-45                                                     | RA*5.0*192 – Update the documentation on the ‘Major AMIS Code Entry/Edit’ [RA MAJORAMIS] option.                                                                                                                                                                                        |
| January 2022   | V-36-V39                                                   | RA*5*185 – Alternate Request Printer added to the ‘Device Specifications for Imaging Locations’ [RA DEVICE] menu. Also added the After Hours Order Parameters to the ‘Location Parameter List’ [RA SYSLOCLIST] option.                                                                  |
| September 2021 | VII-41                                                     | RA*5*183 added a warning to the ‘Label/Header/Footer Formatter’ option.                                                                                                                                                                                                                 |
| September 2021 | V-1, V-34                                                  | RA*5*184 – ‘Inactivate a Location’ [RA SYSINACT] option added to the ‘System Definition’ [RA SYSDEF] menu.                                                                                                                                                                              |
| June 2021      | IV-1                                                       | Patch RA*5*179 Update to security key.                                                                                                                                                                                                                                                  |
| March 2021     | X1-X5                                                      | Patch MAG*3*231 - Radiology Study Tracker Menu added to the Supervisor Menu.                                                                                                                                                                                                            |
| February 2021  | V-1, V-27, V-34                                            | Patch RA*5*178: Update to the System Definition Menu; add the new Outside Location Order Suppression [RA SYSUPLOC] option.                                                                                                                                                              |
| March 2020     |                                                            | Patch RA*5*161 – Update to Utility Files Maintenance menu; add new option ‘Radiology Community Care Consult Entry/Edit’ [RA COMCARE].                                                                                                                                                   |
| June 2019      | I-3, II-9, VII-1,81-83, XV-2                               | Patch RA*5.0*158: Update the 'Procedure Modifier Entry' [RA MODIFIER] description, remove the ‘Reason Edit’ option [RA REASON EDIT] and update of the FAQ (section XV) pertaining to procedure edits.                                                                                   |
| August 2018    | III-4, IV-1                                                | Patch RA*5*124. Documentation added for new RA UNVERIFY security key.                                                                                                                                                                                                                   |
| June 2017      | IX 7-8  V-35  VII-28                                       | Patch RA*5*137. Documentation added for new item on the RA HL7 Menu.  Add Registered Request Printer to ‘Location Parameter List’ [RA SYSLOCLIST] output.  Add pregnancy screen to Exam Status Tracking example.                                                                        |
| December 2016  | V-3,4,10  VII-82                                           | Patch RA*5*133. Document changes to Reason Enter/Edit and Division parameter Set-up.                                                                                                                                                                                                    |
| December 2004  | VIII-22-28, 32, 35, 37, 40, 43                             | Patch RA*5*45. Inserted documentation for new Procedure File Listings: HIST Display Rad/NM Procedure Contrast Media History and List of Procedures with Contrast.  Inserted a Note for several Procedure File Listings that contrast media associations will display, when appropriate. |
| March 2004     | VII-2, 3, 68, 69, VIII-21, 32, XI-1, XII-5, XVII-1, XVII-6 | Patch RA*5*45: Inserted text regarding no longer using AMIS codes to identify contrast medial use, and associating parent/descendant procedures that use contrast media.                                                                                                                |
| May 2003       | V-2                                                        | Patch RA*5*34: Inserted paragraphs regarding if parameter is set to NO or not answered at all.                                                                                                                                                                                          |
| May 2003       | VII-6                                                      | Patch RA*5*34: Moved ‘PRINT ON ABNORMAL REPORT’ entry up to align with top of row.                                                                                                                                                                                                      |
| May 2003       | VII-64                                                     | Patch RA*5*34: Inserted text regarding semicolon restriction on procedure name.                                                                                                                                                                                                         |
| May 2003       | XIV-5                                                      | Patch RA*5*34: Inserted text regarding several cases sharing one printset.                                                                                                                                                                                                              |
| September 2002 | VII-45                                                     | New entries and modifications to existing entries are prohibited without approval from Radiology Service VACO.                                                                                                                                                                          |
| September 2002 | VII-89                                                     | Added new option VistaRad Category Entry/Edit                                                                                                                                                                                                                                           |
| September 2002 | VIII-39                                                    | Added new option VistaRad Category Print                                                                                                                                                                                                                                                |
| July 2002      | V-8, V-13, V-16                                            | Added a Division Parameter for HL7 Applications                                                                                                                                                                                                                                         |
| July 2002      | IX-41                                                      | Added HL7 Radiology Menu                                                                                                                                                                                                                                                                |

Table of Contents

I.	Introduction	I-1

Implementation Checklist	I-1

Division, Location, Imaging Type Definitions	I-1

☞Parent/Descendent Exam and Printsets	I-4

☞Radiopharmaceuticals	I-4

II.	Implementation Check List	II-1

Update from V. 4.5 to V. 5.0	II-1

Virgin Installation (no previous version installed or implemented)	II-10

III.	Screening Methods	III-1

IV.	Security Keys	IV-1

RA ALLOC	IV-1

RA MGR	IV-1

RA RPTMGR	IV-1

RA VERIFY	IV-1

RA SWITCHLOC	IV-1

V.	System Definition Menu	V-1

Division Parameter Set-up	V-2

Division-wide Order Entry Parameters	V-2

Exam Entry/Edit Parameters	V-3

Films Reporting Parameters	V-5

Miscellaneous Division Parameters	V-7

HL7 Applications Associated with this Division	V-8

Imaging Locations Associated with this Division	V-9

Print Division Parameter List	V-14

Camera/Equip/Rm Entry/Edit	V-18

List of Cameras/Equip/Rms	V-20

Location Parameter Set-up	V-21

Flash Card, Jacket Labels, and Exam Label Param	V-21

Order Entry Parameters	V-22

Report Parameters	V-22

Cameras/Equip/Rooms Used by this Location	V-23

Default CPT Modifiers used by this Location	V-24

Recipients of the 'Stat' Alert for this Location	V-24

Imaging Type for this Location	V-25

Inactivate a Location	V-32

Outside Location Order Suppression	V-32

Location Parameter List	V-33

Device Specifications for Imaging Locations	V-35

VI.	Rad/Nuc Med Personnel Menu ...	VI-1

Classification Enter/Edit	VI-2

Clerical List	VI-6

Interpreting Resident List	VI-6

Interpreting Staff List	VI-6

Technologist List	VI-6

VII.	Utility Files Maintenance Menu...	VII-1

Complication Type Entry/Edit	VII-2

Diagnostic Code Enter/Edit	VII-4

Examination Status Entry/Edit	VII-7

Exported Setup	VII-18

Example Status Tracking Sessions	VII-27

Film Type Entry/Edit	VII-31

Label/Header/Footer Formatter	VII-34

Major AMIS Code Entry/Edit	VII-42

☞Nuclear Medicine Setup Menu	VII-43

☞Lot (Radiopharmaceutical) Number Enter/Edit	VII-44

☞Route of Administration Enter/Edit	VII-45

☞Site of Administration Enter/Edit	VII-46

☞Vendor/Source (Radiopharmaceutical) Enter/Edit	VII-47

Order Entry Procedure Display Menu ...	VII-49

Common Procedure Enter/Edit	VII-50

Display Common Procedure List	VII-56

Procedure Edit Menu ...	VII-57

Activate/Inactivate Standard Procedures	VII-58

Procedure Enter/Edit	VII-60

Procedure Message Entry/Edit	VII-74

Procedure Modifier Entry	VII-75

Radiology Community Care Consult Entry/Edit	VII-77

Reports Distribution Edit	VII-77

Sharing Agreement/Contract Entry/Edit	VII-80

Standard Reports Entry/Edit	VII-81

Valid Imaging Stop Codes Edit	VII-83

VIII.	Maintenance Files Print Menu ...	VIII-1

Complication Type List	VIII-2

Diagnostic Code List	VIII-3

Examination Status List	VIII-5

Film Sizes List	VIII-10

Label/Header/Footer Format List	VIII-11

Major AMIS Code List	VIII-12

Modifier List	VIII-13

☞Nuclear Medicine List Menu ...	VIII-14

☞Lot (Radiopharmaceutical) Number List	VIII-15

☞Route of Administration List	VIII-16

☞Site of Administration List	VIII-17

☞Vendor/Source (Radiopharmaceutical) List	VIII-18

Procedure File Listings ...	VIII-19

☞HIST Display Rad/NM Procedure Contrast Media History	VIII-20

Active Procedure List (Long)	VIII-24

Active Procedure List (Short)	VIII-25

Alpha Listing of Active Procedures	VIII-26

☞Barcoded Procedure List	VIII-27

Inactive Procedure List (Long)	VIII-30

Invalid CPT/Stop Code List	VIII-31

List of Inactive Procedures (Short)	VIII-33

☞List of Procedures with Contrast	VIII-34

☞Parent Procedure List	VIII-38

Procedure Message List	VIII-40

Series of Procedures List	VIII-41

Report Distribution Lists	VIII-43

Sharing Agreement/Contract List	VIII-43

Standard Reports Print	VIII-45

VistaRad Category Print	VIII-46

IX.	Radiology HL7 Menu	IX-1

Send ADT HL7 message to PACS	IX-1

Rad/Nuc Med HL7 Voice Reporting Errors	IX-2

Resend Radiology HL7 Message	IX-6

Resend Radiology HL7 Messages by Date Range	IX-7

X.	Radiology Study Tracker Menu	X-1

Check a Radiology or Consult Study for Images	X-1

Report Radiology Studies without Images	X-1

DICOM Query Client	X-2

DICOM Query/Retrieve Client	X-2

Compare Radiology Image Count on PACS with VistA	X-2

Retrieve Missing Radiology Images from PACS	X-4

Display stats for automatic radiology Q/R runs	X-4

Delete the stats for automatic radiology Q/R runs	X-4

Stop automatic Q/R processes	X-5

XI.	Worksheets	XI-1

Division Parameters	XI-1

Camera/Equip/Room	XI-3

Location Parameters	XI-4

Classification	XI-7

Blank Examination Status Worksheet	XI-9

Procedure Setup	XI-13

☞Radiopharmaceuticals	XI-14

Example Radiopharmaceutical Drug Classifications	XI-16

☞Nuclear Medicine Setup	XI-18

XII.	☞Parent/Descendent Exam and Printsets	XII-1

Definition	XII-1

Common Data for Printsets	XII-1

Non-Common Data for Printsets	XII-1

Single Report Setup for Printsets	XII-1

Special Character Designation for Printsets	XII-2

HL7 Interface	XII-3

Registration	XII-3

Editing Data	XII-4

Labels, Headers, Footers	XII-4

VA Fileman Prints/Inquiries	XII-5

Add Exams to Last visit	XII-5

CPRS Interface for Printsets	XII-5

Imaging/Multi-Media Interface Effects on Printsets	XII-5

XIII.	Case Edits and Status Tracking	XIII-1

Overview	XIII-1

Taking Control	XIII-1

Stuffing Data and Default Responses	XIII-1

☞Radiopharmaceutical Logic	XIII-2

☞Medication Logic	XIII-3

☞Radiopharm Prescription &amp; Prescribing Physician/Dose Logic	XIII-4

Population of Imaging Exam Data	XIII-5

XIV.	Outpatient Workload Crediting	XIV-1

Imaging Stop Codes File 71.5	XIV-1

Invalid CPT/Stop Code List	XIV-1

Valid Imaging Stop Codes Edit	XIV-1

Location Parameter Edit	XIV-1

Options that can Potentially Trigger Crediting	XIV-2

Crediting	XIV-2

Errors	XIV-3

XV.	Troubleshooting	XV-1

On-line Verifying of Reports	XV-1

Reports	XV-2

XVI.	Frequently Asked Questions	XVI-1

Imaging Types	XVI-1

Procedures	XVI-2

Case Numbers	XVI-4

Requesting/Scheduling Requests	XVI-6

Printing/Batching/Etc.	XVI-8

Purging Records	XVI-8

Verifying Reports	XVI-10

Hold/Cancelled/Pending/Scheduled	XVI-10

Doubling Workload Credit	XVI-11

Effect of Portable and Operating Room Modifiers	XVI-12

Complications	XVI-13

Contracting Out	XVI-13

Research	XVI-13

General Editing Helpful Hints	XVI-13

XVII.	☞Stop Task (TaskMan)	XVII-1

XVIII.	Glossary	XVIII-1

XIX.	Index	1

## 1 Introduction

As application coordinator, you are required to build, customize, and maintain the Radiology/Nuclear Medicine module files to meet the specific needs of your site. This document is provided to assist you in this function.

☞ This icon designates something as being new or changed in some way from the previous version.

### Implementation Checklist

We suggest using the checklist to make sure you do not miss any necessary steps in implementation. If your site implemented version 4.5, use the Update V. 4.5 to 5.0 Installation Checklist. If this is a first time installation or setup of this program, use the Virgin Installation Checklist.

### Division, Location, Imaging Type Definitions

There are three terms you must be familiar with in order to understand how this package functions. They are Division, Imaging Type, and Imaging Location.

A **Division** is defined as a major unit of an institution which requires separate management. In most instances, there is only one Division at a given medical center which is also referred to as the site. Integrated sites usually require at least one Division defined per site. The Division Parameter Set-up and Location Parameter Set-up options allow you to tailor the package to fit the particular needs of your department. All parameters are specific to the Division, which allows you, as the coordinator, to select the parameters you want to utilize with either a YES or NO answer.

An **Imaging Location** is defined as a physical location where a procedure can be performed. Each location has its own set of parameters defining location-specific criteria, e.g., label/header/footer formats, printer devices for flash cards,  jacket labels requests and reports and how many labels to print. An Imaging Location may be associated with **only one** Division and **only one** Imaging Type.

An **Imaging Type** must be assigned to each procedure and each Imaging Location. Therefore, many Imaging Types can be active within a single Division. Imaging Types other than General Radiology and Nuclear Medicine should only be "activated" if they indeed are Imaging Types used at your facility and report procedures and/or workload separately from the other Imaging Types. In other words, if you want CT scans to be on separate workload reports rather than on General Radiology workload reports, then you should activate the CT Scan Imaging Type (by associating locations that do CT Scans with the Imaging Type of CT scan and assigning CT scan procedures an Imaging Type of CT Scan). Imaging Types are limited in this package to the following:

**IMAGING TYPE			ABBREVIATION**

Angio/Neuro/Interventional			ANI

Cardiology Studies (Nuc Med)		CARD

General Radiology				RAD

Magnetic Resonance Imaging			MRI

Ultrasound					US

Vascular Lab					VAS

Mammography				MAM

You should **not** attempt to add any additional Imaging Types to the above list.

It is important to know how to activate an Imaging Type. When at least one Imaging Location and one or more procedures have been assigned a new Imaging Type, that Imaging Type becomes "active".

Below is a schematic showing relationships:

**Division, Imaging Location, Imaging Type, and Camera/Equipment/Room Relationships**

<!-- image -->

**Note:** The Imaging Type of any given procedure will determine in which Imaging Locations it may be registered and performed. Example: If the Imaging Type for procedure X is General Radiology, it can be registered in Imaging Locations A, B, and D.

### ☞Parent/Descendent Exam and Printsets

A major enhancement to this version is a single combined report for a set of related procedures. This is a "printset" mechanism for entering a single report for all descendent cases registered from a parent order (See Procedure Enter/Edit for more information on parent procedures). For more detailed information see Parent/Descendent Exams and Printsets. The ability to create a separate report for each procedure ordered under a single parent procedure still exists.

### ☞Radiopharmaceuticals

Another important addition with this version is the ability to enter and edit information specific to radiopharmaceuticals for Nuclear Medicine. A new menu, Nuclear Medicine Setup Menu under the Utility Files Maintenance Menu, allows the site to define parameters for radiopharmaceuticals concerning lot number, route and site of administration, and source/vendor. The addition of radiopharmaceutical fields has a major effect on case and status edits for Nuclear Medicine and Cardiology Studies Imaging Types. For more complete information, refer to the chapter Case Edits and Status Tracking.

## 2 Implementation Check List

### Update from V. 4.5 to V. 5.0

This implementation checklist assumes that you have fully implemented version 4.5 and now want to review for implementation the new functionality available in this version.

**Before** IRM loads this version into production:

1. Review the Release Notes to acquaint yourself with any changes that were made to this version of the software and update the users to those changes.
2. Review all new items in this manual (those designated by ☞) and read the chapters on Single Reports for Parent/Descendent Exams and Printsets and Case Edits and Status Tracking. Also, Procedure Enter/Edit in this manual and Report Entry/Edit and Diagnostic Code and Interpreter Edit by Case No. in the user manual are affected by printsets.
3. Radiology/Nuclear Medicine accesses the Pharmacy Drug file #50 for radiopharmaceuticals and their associated VA Classifications; therefore, the Drug file must contain all the radiopharmaceuticals used at your site. Provide the Pharmacy ADPAC with a list of the radiopharmaceuticals and work with the ADPAC to enter them into the Drug file. When entering Radiopharmaceuticals into the Drug file, it is recommended to enter the Nuclide then the Pharmaceutical as the Drug Name and also a synonym to make it easier for Radiopharmaceuticals to be retrieved. (See Example Radiopharmaceutical Drug Classifications under the chapter Worksheets.)

The Radiopharmaceuticals should be assigned one of the following VA Classifications under Diagnostic Agents:

DX200 Radiopharmaceuticals, Diagnostic

DX201 Imaging Agents (in vivo), Radiopharmaceuticals

DX202 Non-Imaging Agents Radiopharmaceuticals

1. If a status's Order is removed through the Examination Status Entry/Edit option but the Appear on Status Tracking field is set to YES, exams in that status will, after the installation of version 5.0, be available for edit in Status Tracking of Exams. The inactivated status will be processed after the active statuses. The purpose of this feature is to allow processing of exams to complete if they are in an inactive status and the case edit options do not prompt for the required fields to allow data entry to complete the cases. **If your site has a large volume of historic cases that fall into this category, you may want to make sure the Appear on Status Tracking field is set to NO prior to the installation of this version** .
2. Print the Active Procedure List (Short) to get a list of Nuclear Medicine procedures that can be used to fill out your worksheets for procedure set-up.
3. It will be necessary to train the technologists and transcriptionists in handling case and report entry/edits for printsets. This should be done in your training account prior to installing live.

The technologists must be made aware of the following:

1. If an exam is added through the Add Exam to Last Visit option, and the last visit was a printset/parent, the added exam becomes part of the printset. The report will be a single one even if the added exam is quite different from the substance of the parent.
2. If there are two parent requests of the same Imaging Type, do not use the Add Exam to Last Visit option to add the procedures of the second parent to the first. Doing this will create a single report for all procedures from both parents, and the second request will never be completed because all descendants will apply to completing the first request.

While you do the setup required after installation, Imaging Service users must be off the system. You should prepare as much as possible to minimize the downtime for Imaging Service users.

The following is a listing and discussion of all the new functionality that you may want to edit in setting up this version. It is strongly suggested that you review the following checklist and complete any worksheets **prior to the actual setup** . Then use the completed checklist and worksheets during the setup.

1. ❑	Division Parameter Set-up.
    1. AUTO E-MAIL TO REQ. PHYS? -If you want to automatically send Radiology/Nuclear Medicine findings when they are verified to the requesting physician via e-mail, you need to enter YES in this field.
| **Division**   | **E-Mail Findings**   |
|----------------|-----------------------|
|                |                       |
|                |                       |
|                |                       |
|                |                       |
    1. RPHARM DOSE WARNING MESSAGE - If you want to display a message other than the default message
This dose requires a written and signed directive by a physician.
to the user when the radiopharmaceutical dose falls outside the range of the "Low Adult Dose" and the "High Adult Dose", enter the message here. These fields reside in the Default Radiopharmaceuticals multiple in the Rad/Nuc Med Procedures file. Use the Procedure Enter/Edit option to adjust these values.
Message: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    1. ❑	Location Parameter Set-up.
    1. ALLOW 'RELEASED/NOT VERIFIED' - If you want to be able to display unverified reports to users outside the Imaging service, this Imaging Location parameter should be set to YES. This field was moved from the Division parameters. If as a Division parameter it contained a YES, then all the Imaging Locations for that Division will contain a YES in this field as a default after this version is installed. Otherwise, the default will be no.
| **Location**   | **Send Alert**   | **Allow Released/**  **Unverified**   |
|----------------|------------------|---------------------------------------|
|                |                  |                                       |
|                |                  |                                       |
|                |                  |                                       |
|                |                  |                                       |
|                |                  |                                       |
|                |                  |                                       |
|                |                  |                                       |
|                |                  |                                       |
|                |                  |                                       |
|                |                  |                                       |
|                |                  |                                       |
    1. STAT REQUEST ALERT RECIPIENTS - List any Radiology/Nuclear Medicine personnel that should receive an alert whenever a STAT request is submitted to the Imaging Location. Bypass this step if you don't want alerts sent.**Note:** To receive a STAT request alert, recipients must have a Radiology/Nuclear Medicine personnel classification. **To use this feature, the Division parameter, "Ask Imaging Location" must be set to YES, and CPRS (OE/RR V. 3.0 or higher) must be installed.**
| **Locations:**   | **Recipients:**   |
|------------------|-------------------|
|                  |                   |
|                  |                   |
|                  |                   |
|                  |                   |
|                  |                   |
|                  |                   |
|                  |                   |
|                  |                   |
|                  |                   |
    1. URGENT REQUEST ALERTS? - If you want to send alerts to selected personnel whenever there is a STAT request, enter YES in this field. Personnel designated to receive STAT request alerts will also receive URGENT alerts. **Note: To use this feature, the Division parameter "Ask Imaging Location" must be set to YES, and CPRS (OE/RR V. 3) or higher must be installed.**
    1. ❑	Diagnostic Code Enter/Edit.
INACTIVE - Print out a list of your diagnostic codes using the option Diagnostic Code List. If you want to inactivate any of the codes, so they do not appear as selections to the users, highlight them and refer to that list when doing this step of the setup.
    1. ❑	Examination Status Entry/Edit.
Editing this option takes a great deal of up front preparation. Make sure you read the information in the chapters Examination Status Entry/Edit and Case Edits and Status Tracking. Use the worksheet (See chapter Worksheets) when defining your changes.
A new Imaging Type, Mammography, was exported with this version. If you intend to activate Mammography as an Imaging Type, then be sure to include it when defining your changes to status tracking.**Note:** This installation will **turn on** the "Ask Radiopharmaceuticals and Dosages" parameter for all nuclear medicine and cardiology studies procedures. All other new parameters will be off. In order for nuclear medicine technologists to accurately enter radiopharmaceuticals, all radiopharmaceuticals used at your site must be entered into the Pharmacy Drug file.
The new fields to edit for all Imaging Types are as follows:
    1. GENERATE EXAMINED HL7 MESSAGE
    2. ASK MEDICATIONS &amp; DOSAGES
    3. ASK MEDICATION ADMIN DT/TIME &amp; PERSONThere are a number of new fields for Nuclear Medicine. If your facility wants to record data in most or all of the new radiopharmaceutical data fields, you will have to use Status Tracking to edit cases. Only through Status Tacking will you be able to control which prompts are asked at which statuses. In order to provide simplicity and avoid extra undesirable prompts at facilities who want to enter a minimum set of radiopharmaceutical data, the case editing options (Case No. Exam Edit and Edit Exam by Patient) do not prompt for all the new Nuclear Medicine fields. Instead, only the **radiopharmaceutical, dose administered, date/time of dose administration,** and **person who administered dose** will be consistently asked for nuclear medicine or cardiology studies cases. However, if data has already been entered via Status Tracking in other nuclear medicine related fields, the case edits will prompt for those fields to allow correction of erroneous radiopharmaceutical data already entered. In addition, if the procedure parameter so specifies, the case edits will prompt for radiopharmaceutical dose prescribed, prescribing physician, and witness to dose administration. The new fields to edit for Nuclear Medicine and Cardiology Studies Imaging Types are as follows:
    1. RADIOPHARMS &amp; DOSAGES REQUIRED
    2. ACTIVITY DRAWN REQUIRED (RADIOPHARM)
    3. DRAWN DT/TIME AND PERSON REQUIRED (RADIOPHARM)
    4. ADMIN DT/TIME/PERSON REQUIRED (RADIOPHARM)
    5. ROUTE/SITE REQUIRED (RADIOPHARM ADMINISTERED)
    6. LOT NO. REQUIRED (RADIOPHARM)
    7. VOLUME/FORM REQUIRED (RADIOPHARM)
    8. ASK RADIOPHARMACEUTICALS AND DOSAGES
    9. ASK ACTIVITY DRAWN (RADIOPHARMACEUTICAL)
    10. ASK DRAWN DT/TIME &amp; PERSON (RADIOPHARMACEUTICAL)
    11. ASK ADMIN DT/TIME &amp; PERSON (RADIOPHARMACEUTICAL)
    12. ASK ROUTE/SITE OF ADMIN (RADIOPHARM)
    13. ASK  NO. (RADIOPHARM)
    14. ASK VOLUME/FORM (RADIOPHARM)
    15. PRINT DOSAGE TICKET WHEN EXAM REACHES THIS STATUS**Note** : Printing of the dosage ticket requires that a valid print device assigned to the location (see IRM Menu, Device Specifications for Imaging Locations option, Dosage Ticket Printer prompt) and YES answered for the Radiopharms/Dosages Required field at the status you are editing (or lower).
    1. ❑	Examination Status Entry/Edit
Even if you do not make changes to the exam status parameters, select the option for each Imaging Type. This will trigger the Data Inconsistency Report and identify all problems. You can up-arrow at the Select an Examination Status prompt as shown here:Select an Imaging Type: NUCLEAR MEDICINESelect an Examination Status: **^**
\_\_\_\_\_\_\_\_\_ Checking order numbers used for status progression \_\_\_\_\_\_\_\_\_
within : NUCLEAR MEDICINE
Required order numbers are in place.
Data Inconsistency Report For Exam Statuses
DEVICE: HOME// (Enter a printer name)
    1. ❑	Label/Header/Footer Formatter. There are a number of new fields available that could be added to labels, headers or footers:
Long Case Number Barcode
Resident Signature Name
Staff Signature Name
Verifying Signature Name
Verifying Signature Title
Patient Address Line 1
Patient Address Line 2
Patient Address Line 3
    1. ❑	Nuclear Medicine Setup Menu contains four options. Routes and sites of administration of radiopharmaceuticals were exported with this version. Review the data in those files, using the print options Route of Administration List and Site of Administration List, before adding more entries. Worksheets for all four options are available in the chapter Worksheets. Add sites and vendors/sources before adding routes and lot numbers. Sites should be entered before routes so they will be selectable as valid sites for a route and lot numbers can be associated with vendors/sources. Also, routes and sites must be available for the next step, Procedure Enter/Edit. You may also want to request that IRM add the Lot Number Enter/Edit as a secondary menu option for the Nuclear Medicine technologists.
    2. ❑	Procedure Enter/Edit. This is another complex setup that requires considerable up front preparation. If you plan to use the nuclear medicine features, you will need to enter radiopharmaceutical parameters on the appropriate procedures. Use the worksheet, making as many copies as necessary. The new fields to edit for all Imaging Types are as follows:
    1. SINGLE REPORT
    2. PROMPT FOR MEDS
    3. DEFAULT MEDICATION
    4. EDUCATIONAL DESCRIPTION
    5. DISPLAY EDUCATIONAL DESCRIPTION**Note:** If you turn parents into printsets by answering YES to the "Single Report" prompt, the printset features will only take effect on cases registered **after** V. 5.0 is installed.
The new fields to edit for Nuclear Medicine and Cardiology Studies Procedures are as follows:
    1. SUPPRESS RADIOPHARM PROMPT
    2. PROMPT FOR RADIOPHARM RX
    3. DEFAULT RADIOPHARMACEUTICAL
LOW DOSE
HIGH DOSE
USUAL DOSE
ROUTE
FORM
If your site uses Parent procedures and you want a single report for all descendants, you can use the Print File Entries option to obtain a list of Parent procedures. You need not print the descendants as shown in this example. Or, you can use one of the existing procedure listing options to get complete data for all active procedures.Select Supervisor Menu Option: **Print File Entries**OUTPUT FROM WHAT FILE: (file name)// **RAD/NUC MED PROCEDURES**SORT BY: NAME// TYPE OF PROCEDURESTART WITH TYPE OF PROCEDURE: FIRST// **P** PARENTGO TO TYPE OF PROCEDURE: LAST// **P** PARENT
WITHIN TYPE OF PROCEDURE, SORT BY:FIRST PRINT FIELD: NAMETHEN PRINT FIELD: **DESCENDENTS** (multiple)THEN PRINT DESCENDENTS SUB-FIELD: . **01** DESCENDENTSTHEN : **&lt;RET&gt;**THEN PRINT FIELD: **&lt;RET&gt;**
*************************Heading (S/C): RAD/NUC MED PROCEDURES LIST Replace **&lt;RET&gt;**START AT PAGE: 1// **&lt;RET&gt;**
DEVICE: (device name)
    1. ❑	If you activate the new Imaging Type Mammography, be sure to enter any modifiers you want for that Imaging type using the option Procedure Modifier Entry.
    2. ❑	If you want Request Cancellations to print, give your IRM support staff a list showing which printer for each imaging location should be used to print them. They will enter these via their IRM menu using the Device Specifications for Imaging Location option.
    3. ❑	This release is year 2000 compliant. The Date of Birth and Current Patient Location (which is date/time stamped) fields for labels, headers and footers are affected because the year is now printed as four digits instead of two. Retest any labels or report headers/footers that contain these fields to make sure they don’t line wrap.

### Virgin Installation (no previous version installed or implemented)

1. ❑	Before IRM loads this system into production, you should read this manual, read over the installation instructions listed here, and complete any related worksheets. The software should be installed in a Training environment first so you can familiarize yourself with the setup procedure and train users as much as possible before going live.
2. ❑	Before you begin the process of building your files, you should consult with your IRM Service to be sure you have access to the security keys (RA MGR, RA ALLOC and RA VERIFY) and have been assigned the Rad/Nuc Med Total System Menu.
3. ❑	Provide the Pharmacy ADPAC with a list of the radiopharmaceuticals and work with the ADPAC to enter them into the Drug file. See an example of Radiopharmaceutical entries in the Drug file under the chapter Worksheets. They should be assigned one of the following VA Classifications under Diagnostic Agents:

1. DX200 Radiopharmaceuticals, Diagnostic
2. DX201 Imaging Agents (in vivo), Radiopharmaceuticals
3. DX202 Non-Imaging Agents Radiopharmaceuticals

1. ❑	Edit parameters for each Division at your facility using the option, Division Parameter Set-up. (See chapter Worksheets)
2. ❑	Edit parameters for each Imaging Location by using the option Location Parameter Set-up. (See chapter Worksheets)
3. ❑	Use the option Examination Status Entry/Edit for each Imaging Type that you activate at your facility. Read about examination status tracking first, including the information in chapter Case Edits and Status Tracking so that you understand the implications of activating an Imaging Type. You should have the exam status worksheets filled out ahead of time so that this part of the setup goes smoothly.
4. ❑	Review the rest of the options in the System Definition Menu and the Utility Files Maintenance Menu and make any changes that are appropriate for your site. Look for worksheets at the back of this manual.
5. ❑	Use the print options in the System Definition Menu, Rad/Nuc Med Personnel Menu, and the Maintenance Files Print Menu to obtain dated hard copies of the data for your records.
6. ❑	Determine the menus and/or options you need to assign to each of your users. There are a number of work related menus (such as clerk, file room, radiologist, ward, technologist, etc.) exported with this package. See the technical manual for more information. Give the list to IRM. You may want to review the Mailman bulletins provided by the Radiology/Nuclear Medicine software with IRM so mail groups with the appropriate members can be set up.
7. ☞❑ **This item is extremely important and should be done as soon as the above steps are complete. No user will be able to sign-on to the Radiology/Nuclear Medicine package unless s/he is assigned at least one Imaging Location.** Use the option Classification Enter/Edit in the Rad/Nuc Med Personnel Menu **now** and give each user access to whatever Imaging Locations they work with. It may be desirable to assign the RA ALLOC key to transcriptionists if they need to enter reports for all Imaging Locations.
8. ❑	Continue training your users.

## 3 Screening Methods

Most options are screened by a combination of Imaging Type, Division, and Imaging Location. Others are screened by "ownership". Division, Imaging Type, and Location screening methods are based on the following:

1. The set of locations the user is privileged to access (entered by the ADPAC or IRM through the Classification Enter/Edit option). Anyone who owns the RA ALLOC key can access all Imaging Locations so it isn't necessary to assign Imaging Locations to owners of this key. (Appropriate owners are ADPACs and transcriptionists.)
2. The sign-on location, which must be a location to which the user has access.
3. The user's Imaging Type access "set" and Division access "set" are calculated by the system, based on the Imaging Locations to which the user has access. They include all the Imaging Types and Divisions of all the locations in the user's access set. For example, if a user only has access to the General Radiology "X-RAY 1" Imaging Location which is in Division A, access will be calculated by the system as follows:
2. If the user selects an option that is screened by Imaging Type, s/he will be able to access data that is within General Radiology regardless of location or Division. This means the user could access more than one location if there are multiple locations of that Imaging Type.
3. If the user selects an option that is screened by Imaging Type and Division, s/he will be able to access data within Division A and General Radiology Imaging Type regardless of location.
4. If the user selects a non-screened option or an option screened by "ownership" of a report, batch, etc., the location/Imaging Type/Division screening will have no effect.

So far we have the following variations of screening:

Method No. and Description

1. Ownership (usually of reports or report batches).
1. Some variation of single location screening - Used for the option Register Patient for Exams because the Imaging Type of the procedure selected must match the Imaging Type of the sign-on location. Used for Add Exams to last Visit because the sign-on location must match the location of the exams previously entered for the visit.
2. Selected location(s) - Locations selected must be in the user's location access set, and must have an Imaging Type that matches the Imaging Type of the sign-on location. This method is used for Exam Status Display/Tracking options, and will be used for some of the reports that have to do with Orders/Requests. (Exam status options must work with one Imaging Type at a time since the exam statuses are now imaging-type specific.) Default response at location selection prompt is "ALL", which means all locations to which the user has access.
3. Sign-on Imaging Type - User is only allowed to select patients and/or cases with an Imaging Type that matches the Imaging Type of the sign-on location. This is used for the remainder of the case edit/view/cancel options.
4. Selected Imaging Types - If user can only access one Imaging Type, the system will default to that Imaging Type without prompting. If the user can access multiple Imaging Types, the user is prompted to select one or more Imaging Types. Default response is "ALL", which means all Imaging Types to which the user has access.
5. Division and Imaging Type selection - User first selects one or more Divisions from his/her Division access list (if only one Division is accessible, the system will default to it rather than prompt the user). Next, user selects one or more Imaging Types from his/her Imaging Type access list (which may now be further restricted, since they may have chosen a Division in which not all Imaging Types to which they have access are active). This method was used for Daily Report, Complication Report, Abnormal Report so far, and will be used for most workload and management reports on exams that have at least progressed to the "registration" stage. It is also used for transcriptionist options. Default responses to the Division and Imaging Type selection prompts are "ALL", which means all to which the user has been given access privileges.
6. Menu option allocation - This is always at the discretion of the site.
7. Division selection.

Here's a list of options and their screening methods:

Screening

Menu Option	Method		Key Needed

Access Erroneous Reports	None (On Supervisor Menu only)

Cancel a Request	None

Create a Batch	None

Delete a Report 	None		RA MGR

Delete Printed Batches by Date	None 		RA MGR

Display Rad/Nuc Med Procedure Information	None

Display a Rad/Nuc Med Report 	None

Display Patient Demographics	None

Distribution Queue Menu (all options)	None

Enter Last Past Visit Before 	None

Exam Deletion	None 		RA MGR

Exam Profile (selected sort)	None

Hold a Request	None

Inquire to File Entries (FileMan)	N/A (On Supervisor Menu only)

Jacket Labels	None

List Exams with Inactive/Invalid Statuses	None (On Supervisor Menu only)

List Reports in a Batch	None

Maintenance Files Print Menu (all options)	None (On Supervisor Menu only. 	If appropriate, printout will

show Imaging Type)

Nuclear Medicine List Menu (all options)	None

Nuclear Medicine Setup Menu (all options)	None

Outside Films Profile	None

Outside Films Registry Menu (all options)	None

Pending/Hold Rad/Nuc Med Request Log	None

Print a Batch of Reports	None

Print File Entries (FileMan)	N/A (On Supervisor Menu only)

Print Rad/Nuc Med Requests by Date	None

Print Selected Requests by Patient	None

Print Worksheets	None

Profile of Rad/Nuc Med Exams	None

Rad/Nuc Med Personnel Menu (all options)	None (On Supervisor Menu only)

Request an Exam	None

Schedule a Request	None

Search File Entries (FileMan)	N/A (On Supervisor Menu only)

Select Report to Print by Patient	None

Screening

Menu Option   	Method 		Key Needed

System Definition Menu (all options)	None (On Supervisor Menu only.			If appropriate, edits will be

by Imaging Type)

Test Label Printer	None

Transcription Report	None

Unverify a Report for Amendment	None 		RA UNVERIFY

Update Patient Record	None

Verify Batch	None 		RA VERIFY

View Exam by Case No..	None

Ward/Clinic Scheduled Request Log	None

Utility Files Maintenance Menu (all options) 	None (On Supervisor Menu only)

Add/Remove Report from Batch	1

Delete Printed Batches	1

On-line Verifying of Reports	1  		RA VERIFY

Resident On-line Pre-Verification	1  		RA VERIFY

Add Exams to Last Visit	2

Register Patient for Exams	2

Detailed Request Display	3

Exam Status Display	3

Log of Scheduled Requests by Procedure	3

Status Tracking of Exams	3

Switch Locations 	None

Cancel an Exam	4

Case No. Exam Edit	4

Diagnostic Code and Interpreter Edit

by Case No.	4

Duplicate Flash Card	4

Draft Report (Reprint)	4

Edit Exam by Patient	4

Indicate No Purging of an Exam/Report	4

Mass Override Exam Status	4  		RA MGR

Override a Single Exam Status to 'complete'	4  		RA MGR

Update Exam Status	4 (On Supervisor Menu only)

Screening

Menu Option   	Method 		Key Needed

Abnormal Exam Report    	6

Complication Report    	6

Daily Log Report     	6

Delinquent Status Report	6

Examination Statistics	6

Functional Area Workload Reports (all rots) 	6

Incomplete Exam Report	6

Personnel Workload Reports (all options	6

except the Transcription Report)

Report Entry/Edit    	6

Special Reports (all except AMIS reports) 	6

Unverified Reports	6

Verify Report Only    	6  		RA VERIFY

AMIS Code Dump by Patient	8

AMIS Report	8

**Note: The RA ALLOC key gives a user access to the broadest possible set of locations, Imaging Types, and Divisions possible with any given option. It is the equivalent of having access to all Imaging Locations.**

## 4 Security Keys

### RA ALLOC

Ownership of the RA ALLOC key overrides the location access security given to personnel through Classification Enter/Edit. Owners of the RA ALLOC key have expanded access to Imaging Locations, Imaging Types, and Divisions. In the case of most workload reports, this means they can select from a list of all Divisions and Imaging Types to include on the report. In the case of various edit and ordering functions, it means they can select from all locations within the Imaging Type to which they are currently signed on through the "Select sign-on location" prompt.

### RA MGR

The RA MGR key gives the user access to supervisor-type functions. Those functions are the following:

1. editing completed exams
2. adding an exam to a visit that is older than yesterday
3. showing the user all non-completed exams, not just those associated with the user's current Division, during execution of the "status tracking" function
4. updating the exam status of an exam to complete
5. deleting exams
6. deleting reports
7. entering a report on a cancelled exam if site parameters don't allow it
8. deleting printed batches by date

### RA RPTMGR

The RA RPTMGR key gives the user supervisor-type privilege to unverify a report, delete a report, and restore a deleted report. This key supersedes the RA MGR key which, prior to this patch, was required to delete and restore a report. This key replaces the RA UNVERIFY key previously required to back down a verified report.

### RA VERIFY

The RA VERIFY key allows users to verify reports.

### RA SWITCHLOC

The RA SWITCHLOC key gives the user access to switch locations across modalities at the time of registration. For example, the holder of this key can register an ANGIO procedure under a CT location if appropriate.

## 5 System Definition Menu

Supervisor Menu ...

System Definition Menu ...

**Camera/Equip/Rm Entry/Edit**

**Division Parameter Set-up**

**Inactivate a Location**

**List of Cameras/Equip/Rms**

**Location Parameter List**

**Location Parameter Set-up**

**Outside Location Order Suppression**

**Print Division Parameter List**

**Defining and Maintaining Your System Parameters**

In this chapter, we will show you how to define your system parameters using the above options, Division Parameter Set-up, Location Parameter Set-up, and Camera/Equip/Rm Entry/Edit. Once you have defined and entered or edited your system parameters, you should use the print options in the System Definition Menu to provide a dated hard copy of the parameters.

New Divisions, locations or cameras/equipment/rooms may be added or their parameters edited at any time throughout the use of the software. These options are used for file maintenance as well as implementation. If this is not a new implementation of the software, you should take this time to review your system parameters for any necessary updating of the files. In particular, check those items that appear with the ☞icon.

### Division Parameter Set-up

**[RA SYSDIV]**

The Division Parameter Set-up option is used to define Division unique information. The Radiology/Nuclear Medicine module was designed to handle the functions of multiple Divisions within a medical center even though most medical centers have only one Division. As a result, the program is structured around the Division concept. Therefore, **even if you are a single Division medical center you must enter at least one Division** using this option.

All Imaging Types and locations associated with this Division are affected by the parameters in this option. For instance, if a clinical history message is entered (number 3 below), the message will appear for any type of procedure ordered whether for general radiology, nuclear medicine, ultrasound, etc. If you require the impression on the report, it will be required on reports from all Imaging Types.

An existing Division may be edited or a new Division may be entered. All Divisions must be in the Institution file (# 4). The following is a listing of Division parameters and a brief explanation for each.

#### Division-wide Order Entry Parameters

1. ASK 'IMAGING LOCATION' - This field determines whether or not the "Submit Request To" prompt appears when a procedure is requested. If set to YES, the user will be **required** to enter the name of the Imaging Location where the request is to be sent and printed at the time they request an exam. During the requesting process, the division of the requesting location (i.e., patient location) is used to determine whether to prompt for a "Submit Request To" location. If the requesting location is not assigned a division in the Hospital Location file #44, the primary division will be used. The user will only be allowed to choose from Imaging Locations whose Imaging Type matches the Imaging Type of the procedure. **It is strongly recommended that you answer "YES" to this question.**

If you do not answer this prompt, the system default is NO and the prompt, "Submit Request To:" will not appear. Setting it to NO will make order tracking more difficult, and is not recommended. If it is set to YES, the Division will be able to implement alerts on STAT and URGENT requests once CPRS (OE/RR V. 3) is installed.

If it is set to NO or not answered at all, and there is only one imaging location with the same imaging type as the ordered procedure’s imaging type, then this lone imaging location will be assigned to the order.

If it is set to NO or not answered at all, and there are more than one imaging location with the same imaging type as the ordered procedure’s imaging type, then the order will not have an imaging location and will show up in the UNKNOWN section of the ‘Detailed Request Display’ [RA ORDER DISPLAY] option.

1. TRACK REQUEST STATUS CHANGES - If set to YES, this parameter establishes the collection of the date and time of request status changes. Request status changes pertain solely to the physician's order and whether it is in one of the following statuses: discontinued, complete, hold, pending, active, scheduled, unreleased. Request status changes can be used to find the status of an order at any given time in the past.

This prompt is now bypassed and automatically set to YES.

1. CLINICAL HISTORY MESSAGE - This is an **optional** , free text message, 5-70 characters in length that appears just prior to the prompt for the clinical history field. This is often used to remind the person entering the request that specific information is needed in the patient's clinical history.

If you bypass this field, no message will appear prior to the user seeing the prompt for the clinical history.

#### Exam Entry/Edit Parameters

1. DETAILED PROCEDURE REQUIRED - If set to YES, entry of a Parent, Series or Detailed procedure type, will be required. If set to NO, procedures with the procedure type Broad will be accepted during order entry as a valid entry. This parameter in the division of the requesting location is used to determine if a broad procedure can be ordered. At the time the procedure is registered, broad types won't be allowed if either the division of the imaging location or the division of the requesting location requires a detailed procedure. If no division is entered on the requesting (or imaging) location in the Hospital Location file #44, the primary division will be used. Depending on parameters in the Examination Status file, you can require that the procedure be changed to either a Series or Detailed procedure by the radiology or nuclear medicine staff in order for the examination to acquire a given status. Again think about those entering orders; will they be able to discriminate between the more specific Detailed and Series type procedure, or will they be more comfortable selecting a general procedure name from the Broad types?

If you choose to bypass this prompt, the system default is NO and users will be able to request Broad type procedures.

1. ASK 'CAMERA/EQUIP/RM' - Setting this parameter to YES indicates

that the question "Primary Camera/Equip/Rm" will be asked when the user is entering data about the examination in status tracking. If you want to track camera, equipment or room use for each procedure, answer YES to this prompt, keeping in mind that the user may still bypass the question if s/he chooses to do so. (The Examination status parameters; can be set to **require** this data before an exam can progress to a Complete (or other) status.)

If you accept the default of NO, the user will not see the Primary Camera/Equip/Rm prompt.

1. AUTO USER CODE FILING - The access code entered at sign-on is used automatically for the activity logs if this parameter is set to YES. If NO, the user(s) will be asked to enter access codes during various processes. This feature was used in older versions to minimize security risks of unattended logged-in terminals and multiple users sharing one terminal. It should not be necessary at most sites now, and should therefore be set to YES.

1. TRACK EXAM STATUS CHANGES - Setting this parameter to YES results in the recording of the dates/times of examination status changes. These statuses pertain to the exam, not the request. Statuses are defined by the site using the option Examination Status Entry/Edit. Examples of statuses that might be defined are as follows: Called for Exam, Cancelled, Complete, Examined, Transcribed, Waiting for Exam, etc.

This prompt is now bypassed and automatically set to YES.

1. ASK EXAM STATUS TIME - If the Track Exam Status Changes parameter is set to YES, then this parameter will appear. Setting this parameter to YES indicates that the user should be asked the time of the status change. The Date/Time is added to the Status Change Dt/Time subfile and to the Activity Log.

If set to NO or bypassed, the system automatically uses the current date and time and the prompt for time will not appear. This data is added only to the Activity Log.

1. TIME LIMIT FOR FUTURE EXAMS - This parameter sets a specific

number of hours in the future during which a patient can be registered for an exam. If this prompt is bypassed, the user will not be able to register a patient for a future date or time. The number of hours cannot exceed 168 (one week). Generally, registering a patient is done when the patient arrives at the Imaging Location. Registering a patient is not the same as scheduling a patient for a procedure, which takes any future date you want.

**Note: Registering patients in advance opens the possibility for exam updating before the exam really takes place. This can cause failure of workload crediting. Registration more than 24 hours in the future is not recommended.**

#### Films Reporting Parameters

1. ALLOW STANDARD REPORTS - Transcriptionists will be able to select a standard report when using the Report Entry/Edit option if this parameter is set to YES. There is an option, Standard Reports Entry/Edit, which can be used to build a standard report with a report text that is often used. An example of a standard/routine exam might be, Normal Chest with the text reading "Chest exam is within normal limits". If there are a number of such exams reported, allowing the transcriptionists this ability saves time. These standard reports are discussed in a later chapter.

1. ALLOW BATCHING OF REPORTS - If set to YES, the transcriptionist can group reports, generally by physician name, for easy, organized access or printing. If changes must be made, the transcriptionist can look for the report within a batch rather than by keeping track of record numbers and patient names. It provides a time-saving way to organize work.

1. ALLOW COPYING OF REPORTS - Contents of one report can be copied to another if this parameter is set to YES. If a patient has had more than one test and the report text and impression of one report are needed for another, this handy ability helps save time. It places the entire report text and impression text of the selected report into the one you are editing. The text can then be further edited. The Clinical History will be moved from the patient's current exam record to the report record, not from the copied report.

1. IMPRESSION REQUIRED ON REPORTS - Set this parameter to YES if the impression is required on a report in order for it to become verified and for the exam to progress to a status of Complete. (Also, see Examination Status parameter instructions for setting up at least the Complete status to require Impression if this parameter is set to YES.)

**Note: It is highly recommended that this parameter be set to YES. When reports are purged from the system, the clinical history and report text are deleted. Only the impression is retained on line.**

1. ALLOW VERIFYING BY RESIDENTS - This parameter can be set to YES to allow interpreting residents to verify their own reports while doing On-line Verifying of Reports. Further, if this parameter is set to YES and the resident's **individual** parameter, Allow Verifying of Others (in the New Person file), is **also** set to YES, the resident will be allowed to verify other interpreting physicians' reports in addition to their own.

It is recommended that residents NOT be allowed to verify reports because of the legal implications of report verification.

1. ALLOW RPTS ON CANCELLED CASES? - If this field is set to YES, 	any user can enter a report on a cancelled exam.

If this parameter is set to NO, only users who own the RA MGR key can edit or enter a report on a Cancelled case.

1. ☞WARNING ON RPTS NOT YET VERIF? - If this field is set to YES, results reports in all statuses except "Verified" will contain the status surrounded by asterisks under the body of the printed report. This can be useful in making sure that unverified report copies are not placed in patient charts or mistakenly interpreted as final results. (This is not a new feature. Only the name was changed.)
2. ☞AUTO E-MAIL TO REQ. PHYS? - If this field is set to YES, the system will automatically send the Radiology/Nuclear Medicine findings report to the Requesting Physician via e-mail at the time it is verified. If this field is left blank, verified reports will not be e-mailed to the requesting physician.

When a report is verified, the Auto E-Mail to Req. Phys. Field of the division for the requesting location is used to determine whether to send results to the requesting physician. If the requesting location is not assigned to a division in the Hospital Location file #44, the primary division will be used. **Note: If the requesting location is assigned to a division in the Hospital Location file #44, make sure that division is also defined in the Rad/Nuc Med Division file #79.**

1. ALLOW E-SIG ON COTS HL7 RPTS – If this field is set to YES, the system will automatically add the Electronic Signature Block printed name of the Verifying Physician that signed the report being transmitted to Radiology/Nuclear Medicine via an HL7 interface to a COTS voice reporting system. This parameter is only checked for COTS HL7 interfaces that use the Generate/Process Routine 'RAHLTCPB' in the subscriber protocol. **Note: The HL7 COTS interfaces supported by this option are the IBM MedSpeak interface released with patch RA*5*4 and the TalkStation and PowerScribe interfaces released with patch RA*5*12. See the appropriate appendix in the Rad/Nuc Med Technical Manual for additional information on these interfaces.**

#### Miscellaneous Division Parameters

1. FACILITY PHONE NUMBER - The field contains the main phone number for the facility. It is used to print on radiology reports along with the facility name and address. The facility contact information is a requirement for mammography reports. **The phone number must be entered in the format NNN-NNN-NNNN or (NNN) NNN-NNNN.**

1. PRINT FLASH CARD FOR EACH EXAM - To have **one** flash card automatically printed with each registration of a **case** for all Imaging Locations, set this parameter to YES. To allow the printing of more than one flash card, set this parameter to NO and use the Location Parameter Set-up option to enter the number you want printed for each location.

1. PRINT JACKET LBLS W/EACH VISIT - Indicate to the system that a jacket label be printed with each visit (may include many cases/exams) by setting this parameter to YES. The number of labels printed will be the same as the entry in the location parameter How Many Jacket Lbls Per Visit.
2. CONTRAST REACTION MESSAGE - This is an **optional** , free text field to be used for entering a warning message that will be displayed each time a patient who has had a reaction to contrast medium is registered for a procedure that uses a contrast medium.

If you bypass this field, no message will be displayed.

1. ☞RPHARM DOSE WARNING MESSAGE - This field contains the message displayed to the user when the dose falls outside the range of the "Low Adult Dose" and the "High Adult Dose" for the radiopharmaceutical. These fields reside in the Default Radiopharmaceuticals multiple in the Rad/Nuc Med Procedures file. Use the Procedure Enter/Edit option to adjust these values. If no values exist for a procedure, this message will have no effect.

#### HL7 Applications Associated with this Division

1. HL7 RECEIVING APPLICATION – this field should only be set if using ROUTING LOGIC with the Radiology HL7 subscriber PROTOCOLs (File #101). (See the Radiology/Nuclear Medicine V. 5.0 HL7 Manual for further details.)

If using ROUTING LOGIC then only the HL7 RECEIVING APPLICATIONs defined here will receive Radiology HL7 messages for this Division. If ROUTING logic IS BEING USED, BUT NO hl7 receiving applications ARE DEFINED, then Radiology HL7 messages for the Division will not be created.

If no applications are entered and ROUTING LOGIC is not set up (this is the normal setup), then the system assumes that all HL7 applications should receive HL7 messages created in this Division.

Note: If in doubt, do not set this field.

#### Imaging Locations Associated with this Division

1. IMAGING LOCATION - This field should contain all Imaging Locations associated with this Division. To determine the locations available for your selection before editing this field, you can use the option Print File Entries within the Supervisor Menu to obtain a list.

☞	Only those locations in the Hospital Location file #44 whose TYPE field is **CLINIC** and whose PATTERN DATE field is NULL will appear in this list. Also, print the Inactivate Date so you can avoid locations that have been inactivated.

OUTPUT FROM WHAT FILE: RAD/NUC MED PROCEDURES// HOSPITAL LOCATION

(148 entries)

SORT BY: NAME// **2** TYPE

START WITH TYPE: FIRST// **CLINIC** USES INTERNAL CODE: C

GO TO TYPE: LAST// **CLINIC** USES INTERNAL CODE: C

WITHIN TYPE, SORT BY: **PATTERN** (multiple)

PATTERN : **.01** PATTERN DATE

START WITH PATTERN DATE: FIRST// @

GO TO PATTERN DATE: LAST// @

WITHIN PATTERN DATE, SORT BY: **&lt;RET&gt;**

STORE IN 'SORT' TEMPLATE: **&lt;RET&gt;**

FIRST PRINT FIELD: NAME

THEN PRINT FIELD: INACTIVATE DATE

THEN PRINT FIELD: **&lt;RET&gt;**

*******************************

Heading (S/C): HOSPITAL LOCATION LIST Replace **&lt;RET&gt;**

START AT PAGE: 1// **&lt;RET&gt;**

DEVICE: **(Printer name)**

If you are in the process of editing this field in the Division Parameter Set-up option, entering one or two question marks will list your location choices.

New locations may also be entered in the Imaging Locations file #79.1 at this step. Entry of **new** Imaging Locations should be coordinated with Medical Administration Service and/or Information Resource Management. An Imaging Location must be defined in the Division parameters through entry at this step in order to process examinations from that location. Once an Imaging Location is associated with a Division, all the Division parameters become those of the location, unless stated otherwise.

☞	At the completion of your edits, the program checks each Imaging Location associated with the Division for invalid locations. A valid Imaging Location has a "Type" of CLINIC and has no appointment patterns. An error message will appear for any invalid Imaging Location. Any problem not fixed will result in failure to credit of procedures in that location. Correct the problem, and then run through the Division Parameter Set-up option again to make sure the location returns OK.

Two fields from the Division parameters directly impact the location parameters: Print Flash Card for Each Exam and Print Jacket Lbls W/Each Visit. If the flag for the first parameter is set to YES, then one flash card will be printed automatically for each examination and you will not be asked to enter an amount to print through the Location Parameters Set-Up option. If the Division parameter Print Jacket Lbls W/Each Visit is set to YES, jacket labels will be printed for each examination. The number of labels printed will be determined by the entry in the How Many Jacket Lbls Per Visit location parameter.

**Note:	Whenever changes are made to the Division parameters, any users currently signed on to the system who want to use the new changes must exit and reenter the package or use the Switch Locations option to make the new parameters take effect.**

Here is an example of how the Division parameters might be set up. Enter one or two question marks at the prompt if you need more information. There are a good number of default answers for your convenience. They are suggestions as to what is a usual answer but they can be changed by you. Striking the return key accepts the default as it is.

| Prompt/User Response                                                                                                                                                                                                                                                                                           | Discussion                                                                                                                                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Division Parameter Set-up  Select Division:  **NEW DIVISION**  ILLINOIS  VAMC 234  Are you adding 'NEW DIVISION' as a new RAD/NUC MED DIVISION (the 2ND)?  **Y**  (YES)                                                                                                                                        | Enter the name  or station number of the Division you want to set up.                                                                                                                                                                                                                                                                                                                                              |
| Division-wide Order Entry Parameters:  ------------------------------------  ASK 'IMAGING LOCATION': yes//  **&lt;RET&gt;**                                                                                                                                                                                    | Answering "  **yes**  " is recommended so that all requests will be associated with an Imaging Location for report sorting and request tracking purposes.                                                                                                                                                                                                                                                          |
| CLINICAL HISTORY MESSAGE:  **Enter clinical history relevant to the procedure.**                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Exam Entry/Edit Parameters:  ---------------------------  DETAILED PROCEDURE REQUIRED: no//  **&lt;RET&gt;**                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ASK 'CAMERA/EQUIP/RM': no//  **y**  es                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                    |
| AUTO USER CODE FILING: yes//  **&lt;RET&gt;**                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ASK EXAM STATUS TIME: no//  **Y**  yes                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                    |
| TIME LIMIT FOR FUTURE EXAMS:  **12**                                                                                                                                                                                                                                                                           | We will allow cases to be registered 12 hours in advance of the current date/time.                                                                                                                                                                                                                                                                                                                                 |
| Films Reporting Parameters:  ---------------------------  ALLOW STANDARD REPORTS: no//  **Y**  yes                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ALLOW BATCHING OF REPORTS: yes//  **&lt;RET&gt;**                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ALLOW COPYING OF REPORTS: yes//  **&lt;RET&gt;**                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                    |
| IMPRESSION REQUIRED ON REPORTS: yes//  **&lt;RET&gt;**                                                                                                                                                                                                                                                         | The impression is saved even though report texts and clinical histories may be purged. Respond YES to this prompt to prevent verifying and completing reports before an impression is entered.                                                                                                                                                                                                                     |
| ALLOW VERIFYING BY RESIDENTS: no//  **&lt;RET&gt;**                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ALLOW RPTS ON CANCELLED CASES?: no//  **&lt;RET&gt;**                                                                                                                                                                                                                                                          | If you answer NO to this prompt, only users with the RA MGR key may enter reports on cancelled cases.                                                                                                                                                                                                                                                                                                              |
| WARNING ON RPTS NOT YET VERIF?: yes//  **&lt;RET&gt;**                                                                                                                                                                                                                                                         | If this field is set to YES, the status of the results report will be printed on the output.                                                                                                                                                                                                                                                                                                                       |
| AUTO E-MAIL TO REQ PHYS? yes//  **&lt;RET&gt;**                                                                                                                                                                                                                                                                | If this field is set to YES, the report will be automatically sent to the Requesting Physician via e-mail at the time it is verified.                                                                                                                                                                                                                                                                              |
| ALLOW E-SIG ON COTS HL7 RPTS: yes//  **&lt;RET&gt;**                                                                                                                                                                                                                                                           | If this field is set to YES, the electronic signature of the verifying physician is printed on COTS HL7 reports.                                                                                                                                                                                                                                                                                                   |
| Miscellaneous Division Parameters:  -------------------------------------------------  FACILITY PHONE NUMBER:  PRINT FLASH CARD FOR EACH EXAM: no//  **&lt;RET&gt;**  PRINT JACKET LBLS W/EACH VISIT: no//  **&lt;RET&gt;**                                                                                    | Enter the phone number for this facility in the format NNN-NNN-NNNN or  (NNN) NNN-NNNN.                                                                                                                                                                                                                                                                                                                            |
| CONTRAST REACTION MESSAGE:  *****WARNING*** THIS PATIENT HAS HAD CONTRAST MEDIA REACTIONS**  RPHARM DOSE WARNING MESSAGE:  **THIS DOSE DEVIATES FROM THE PRESCRIBED RANGE AS OUTLINED IN THE DEPARTMENTAL PROCEDURES MANUAL, AND REQUIRES A SIGNED, DATED, AND WRITTEN DIRECTIVE BY AN AUTHORIZED PHYSICIAN.** | This message cannot exceed 70 characters.  This is a word processing field and may be as long as you like.                                                                                                                                                                                                                                                                                                         |
| HL7 Applications Associated with this Division:  ----------------------------------------------  Select HL7 RECEIVING APPLICATION:  **RA-TALKLINK-TCP**  ACTIVE  Select HL7 RECEIVING APPLICATION:  **&lt;RET&gt;**                                                                                            | Example shows how to restrict HL7 messages for this Division to TalkStation Voice Recognition tool only. If no HL7 applications are being used, or only one HL7 application, then leave this field blank.                                                                                                                                                                                                          |
| Imaging Locations Associated with this Division:  ------------------------------------------------  Select IMAGING LOCATION:  **?**  Answer with IMAGING LOCATIONS  You may enter a new IMAGING LOCATIONS, if you wish  Enter a location for this Division.  Answer with IMAGING LOCATIONS, or TYPE OF IMAGING | To obtain a list of locations available to you, enter a ? at this prompt. The entries in the Imaging Location file display with their Imaging Types in parentheses to the right. Entering ?? will display a list of all possible selections. If you do not see the location that you want, it is either not in the Hospital Location file or the Type field of the Hospital Location file does not contain CLINIC. |

Choose from:

*X-RAY 	(GENERAL RADIOLOGY-499)*

*NUC MED LOC 	(NUCLEAR MEDICINE-639)*

*ULTRASOUND 	(ULTRASOUND-499)*

*MAGNETIC RESONANCE IMAGING 	(MAGNETIC RESONANCE IMAGING-499)*

*NUC 	(NUCLEAR MEDICINE-499)*

*FLUORO 	(GENERAL RADIOLOGY-499)*

*RAD 	(GENERAL RADIOLOGY-639)*

*CAT SCAN 	(CT SCAN-499)*

US 	(ULTRASOUND-578)

You may enter a new IMAGING LOCATIONS, if you wish

Select the appropriate location.

The entry selected must be set up as an

'Imaging' type in the Hospital Location file.

| Prompt/User Response	                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Discussion                                                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Select IMAGING LOCATION:  **X-RAY**  (GENERAL RADIOLOGY-499)  ...OK? yes//  **&lt;RET&gt;**  (YES)  GENERAL RADIOLOGY  Location is already assigned to the HINES IRMFO Division! ??                                                                                                                                                                                                                                                                                                                                                                                                                                          | Remember a location can only belong to  **one**  Division. This is telling us X-RAY already belongs to Hines IRMFO. |
| Select IMAGING LOCATION:  **US**  (ULTRASOUND-578)  ...OK? yes//  **&lt;RET&gt;**  (YES)  ULTRASOUND  Are you adding 'US' as a new IMAGING LOCATIONS (the 1ST for this RAD/NUC MED DIVISION)?  **Y**  (YES)  Select IMAGING LOCATION:  **RAD**  (GENERAL RADIOLOGY-639)  ...OK? yes//  **&lt;RET&gt;**  (YES)  GENERAL RADIOLOGY  Are you adding 'RAD' as a new IMAGING LOCATIONS (the 2ND for this RAD/NUC MED DIVISION)?  **Y**  (YES)  Select IMAGING LOCATION:  **&lt;RET&gt;**  Division Parameters have been set!  Imaging Location X-RAY is OK.  Imaging Location ULTRASOUND is OK.  Imaging Location CAT SCAN is OK. |                                                                                                                     |

### Print Division Parameter List

**[RA SYSDIVLIST]**

Once all of the parameters are set for each of your Divisions, use this option to print a dated, hard copy of the settings for reference. Any time you make a change to the parameters, it is useful to keep a copy for historical reference. Here we show the settings for two Divisions, New Division and Hines CIO Field Office.

| Prompt/User Response                                             | Discussion   |
|------------------------------------------------------------------|--------------|
| Print Division Parameter List                                    |              |
| DEVICE:  **(Printer Name)**  RIGHT MARGIN: 80//  **&lt;RET&gt;** |              |

Rad/Nuc Med Division List     PAGE 1

------------------------------------------------------------------------------

Division/Facility Phone: NEW DIVISION/ 555-555-5555

------------------------

Track Request Status Changes? : NO

Track Exam Status Changes? : yes

Ask for Exam Status Time? : yes

Print Flash Card For Each Exam? : no

Ask for Imaging Location? : NO

Ask for Requested Date?

Auto User Code Filing?  : yes

Require Detail Procedure...

...upon Initial Exam Entry?: no

Print Jacket Labels...

...with each Visit?: no

Ask for Camera/Equipment/Room? : yes

Allow Rpts on Cancelled Exams? : no

Auto e-mail to Req. Physicians? : yes

Time Limit For Future Exams...

...in Hours?: 0

Allow Standard reports?  : yes

Allow Batching of reports? : yes

Rad/Nuc Med Division List     PAGE 2

------------------------------------------------------------------------------

Allow Copying of reports? : yes

Impression Required on reports? : yes

Allow Verifying by Residents? : no

Interpreting Staff Required? : NO

Warning on reports not yet...

...Verified? : yes

Allow e-sig on COTS HL7 reports? :yes

Contrast Message:

-----------------

***WARNING*** THIS PATIENT HAS HAD CONTRAST MEDIA REACTIONS

Clinical History Message:

-------------------------

***Enter clinical history relevant to procedure***

Resource Device:

----------------

Rad/Nuc Med Division List     PAGE 3

------------------------------------------------------------------------------

RAD RESOURCE DEVICE

Radiopharmaceutical Dose Warning Message:

-----------------------------------------

THIS DOSE DEVIATES FROM THE PRESCRIBED RANGE AS OUTLINED IN THE

DEPARTMENTAL PROCEDURES MANUAL, AND REQUIRES A SIGNED, DATED, AND WRITTEN

DIRECTIVE BY AN AUTHORIZED PHYSICIAN.

HL7 Receiving Applications for Division:

----------------------------------------

RA-PSCRIBE-TCP

Imaging Locations:

------------------

US

RAD

NUC

Rad/Nuc Med Division List     PAGE 4

------------------------------------------------------------------------------

Division: HINES CIO FIELD OFFICE

--------

Track Request Status Changes? : YES

Track Exam Status Changes? : yes

Ask for Exam Status Time? : yes

Print Flash Card For Each Exam? : no

Ask for Imaging Location? : YES

Ask for Requested Date?  : yes

Auto User Code Filing?  : yes

Require Detail Procedure...

...upon Initial Exam Entry?: no

Print Jacket Labels...

... with each Visit?: no

Ask for Camera/Equipment/Room? : yes

Allow Rpts on Cancelled Exams? : no

Auto e-mail to Req. Physicians? : yes

Time Limit For Future Exams...

...in Hours?: 96

Allow Standard reports?  : yes

Allow Batching of reports? : yes

Rad/Nuc Med Division List     PAGE 5

------------------------------------------------------------------------------

Allow Copying or reports? : yes

Impression Required on reports? : yes

Allow Verifying by Residents? : yes

Interpreting Staff Required? : NO

Warning on reports not yet...

...Verified?: yes

Allow e-sig on COTS HL7 reports? : yes

Contrast Message:

-----------------

***WARNING*** THIS PATIENT HAS HAD CONTRAST MEDIA REACTIONS

Clinical History Message:

-------------------------

**CLINICAL HISTORY IS MANDATORY**

Resource Device:

----------------

Rad/Nuc Med Division List     PAGE 6

------------------------------------------------------------------------------

Radiopharmaceutical Dose Warning Message:

-----------------------------------------

HL7 Receiving Applications for Division:

----------------------------------------

RA-TALKLINK-TCP

Imaging Locations:

------------------

X-RAY

ULTRASOUND

MAGNETIC RESONANCE IMAGING

FLUORO

CAT SCAN

### Camera/Equip/Rm Entry/Edit

**[RA SYSEXROOM]**

This option is used to enter cameras, equipment, and/or rooms that are used by the department. It will provide the list of choices for a user when entering a patient's procedure if, within the Division Parameters Set-up option, the field "Ask Camera/Equip/Room" contains a YES. If you have already decided that tracking this information is not important to your service, then skip this option.

When defining the parameters in each Imaging Location (Location Parameter Set-up), you will be asked to enter any cameras, equipment and/or rooms associated with the location. Each can be associated with one or more locations, since some sites use the same room across locations, Imaging Types, and Divisions. Cameras/Equipment/Rooms cannot be deleted through this option. However, you can "inactivate" them by removing them from the Imaging Location through the Location Parameter Set-up option.

1. CAMERA/EQUIP/ROOM - Enter new cameras, equipment, or rooms at this prompt. This field is directly associated with one or more Imaging Locations.
2. CAMERA/EQUIP/RM DESCRIPTION - Enter a description 3 - 40 characters in length to describe the type of camera, equipment, room or procedures performed.

| Prompt/User Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Discussion                                                                                                                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Camera/Equip/Rm Entry/Edit  Select Camera/Equip/Room:  **??**  Choose from:  CAMERA 1 Triple Head Spect Scanner  CAT SCAN PICKER PQ200 SCANNER  INP1 X-RAY GASTRO X-RAYS  INP2 X-RAY BROKEN LEG X-RAYS  MAMMOGRAPHIC Used in mammography exams.  MRI ROOM MAGNETIC RESONANCE IMAGING ROOM  NUC1 HEART IMAGING  NUC2 BRAIN IMAGING  OUTP1 X-RAY X-RAYS ONLY IN THIS ROOM  OUTP2 X-RAY ACCIDENT X-RAYS  PORTABLE PORTABLE  This field contains the name of this  camera/equipment/room. Names must be between  1 and 30 characters in length. | Enter one or two ? to obtain a list of selections already in the file.                                                                                                                |
| Select Camera/Equip/Room:  **PORTABLE II**  Are you adding 'PORTABLE II' as a new CAMERA/EQUIP/RM (the 12TH)?  **Y**  (YES)                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                       |
| CAMERA/EQUIP/RM DESCRIPTION:  **?**  Enter a brief description, between 3 and 40  characters in length, to define the types  of procedures performed.  CAMERA/EQUIP/RM DESCRIPTION:  **Portable used in Surgery**                                                                                                                                                                                                                                                                                                                           | This field can be used to describe this camera/equipment/room and define what types of procedures may be performed there. "Triple Head Spect Scanner" is an example of a description. |
| CAMERA/EQUIP/RM: PORTABLE II//  **&lt;RET&gt;**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                       |
| DESCRIPTION: Portable used in Surgery//  **&lt;RET&gt;**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                       |
| Select Camera/Equip/Rm:  **&lt;RET&gt;**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                       |

### List of Cameras/Equip/Rms

**[RA SYSEXLIST]**

Once you complete your entries for the Camera/Equip/Rm file #78.6, use this option to print a dated, hard copy of the contents of the file.

| Prompt/User Response                                             | Discussion   |
|------------------------------------------------------------------|--------------|
| List of Cameras/Equip/Rms                                        |              |
| DEVICE:  **(Printer Name)**  RIGHT MARGIN: 80//  **&lt;RET&gt;** |              |

Imaging Camera/Equipment/Room List    PAGE 1

CAMERA/EQUIP/RM RAD/NUC MED DIVISION LOCATION

------------------------------------------------------------------------------

CAMERA 1  HINES INFORMATION SY X-RAY

CAT SCAN  HINES INFORMATION SY CAT SCAN

INP1 X-RAY  HINES INFORMATION SY X-RAY

INP1 X-RAY  HINES INFORMATION SY FLUORO

INP2 X-RAY  HINES INFORMATION SY X-RAY

MRI ROOM  HINES INFORMATION SY MAGNETIC RESONANCE I

NUC1  NEW DIVISION  NUC MED LOC

NUC2  NEW DIVISION  NUC MED LOC

NUC2  HINES INFORMATION SY NUC

OUTP1 X-RAY HINES INFORMATION SY X-RAY

OUTP1 X-RAY HINES INFORMATION SY FLUORO

OUTP2 X-RAY HINES INFORMATION SY X-RAY

PORTABLE  NEW DIVISION  NUC MED LOC

PORTABLE  HINES INFORMATION SY X-RAY

PORTABLE  HINES INFORMATION SY ULTRASOUND

PORTABLE II **UNASSIGNED**  **UNASSIGNED**

**Note that "PORTABLE II" , created on the previous page, appears on this list as "**UNASSIGNED**". This is because "PORTABLE II" has not been assigned an Imaging Location. All camera/equipment/rooms that have been entered in the Camera/Equip/Rm file, but not assigned to any Imaging Location will appear at the end of this list.**

A camera/equipment/room can belong to more than one division/location.

### Location Parameter Set-up

**[RA SYSLOC]**

The Radiology/Nuclear Medicine program is designed to handle multiple locations within a Division. Each location must have its own set of parameters. The Location Parameter Set-up option is used by the coordinator to define Imaging Location parameters for new locations and edit location parameters for existing locations. **At least one location must be entered for each Division** . The following is a listing of location parameters and brief explanations.

1. LOCATION - An existing location may be edited or a new location may be entered at this prompt. Before entering a new location, use the option Print File Entries within the Supervisor Menu to see what locations are already in the file. Print the Imaging Type entries in the Hospital Location file #44 (sort by Type (from CLINIC to CLINIC) and print Name and Inactivate Date). Any location whose type is CLINIC is available for you to select at this prompt. Any locations you need but are not listed, you will need to create using this Location Parameter Set-up option. For the purpose of workload crediting, when a new location is selected, it will automatically be flagged as an "occasion of service" clinic in File 44. If there are appointment patterns, a duplicate clinic of the same name will automatically be added in File 44 and marked "occasion of service." **Note:** Always contact MAS and coordinate with them the addition of new locations.

When you and MAS add a new location that is not in the Hospital Location file, you must also enter a Hospital Location Type. The "HOSPITAL LOCATION TYPE:" prompt should always be answered with "CLINIC".

#### Flash Card, Jacket Labels, and Exam Label Param

**Note: Labels can be printed from the option Duplicate Flash Card even if the site parameters are not set up to print labels.**

**Note:** Printers for Flash Cards, Jacket Labels, Requests, and Reports for each Imaging Location are set up via the IRM Menu option Device Specifications for Imaging Locations. If printers have not been assigned, you will get a message "No default flash card printer has been assigned. Contact IRM."

If under the Division parameters, you answered YES to "PRINT FLASH CARD FOR EACH EXAM:" and/or "PRINT JACKET LBLS W/EACH VISIT:", you **will not** see the "HOW MANY..." prompt.

1. HOW MANY (FLASH CARDS, JACKET LABELS) PER VISIT - This is a whole number between 0 and 10 to establish a parameter for printing the number of cards and/or labels needed for each patient visit at this location.

This question will **not** appear if you entered YES at the Division parameter, "PRINT FLASH CARD FOR EACH EXAM:" and this location is associated with the Division. Bypassing each of these prompts or entering 0 will suppress the printing of the item.

HOW MANY EXAM LABELS PER EXAM - Exam labels are printed for each registered case. This is a whole number between 0 and 9.

1. DEFAULT (FLASH CARD, JACKET LABEL, EXAM LABEL) FORMAT - A default format can be entered for each card or label type. Each time cards or labels are printed for an exam registered to this location, they will be printed using the specified format. Formats for each may be designed using the option Label/Header/Footer Formatter.

#### Order Entry Parameters

This parameter identifies the printer used to print request forms (form 519) as procedures are ordered. It is set up via the IRM Menu option Device Specifications for Imaging Locations, at the prompt, "REQUEST PRINTER NAME:". If a printer has not been assigned to this prompt, a message will tell you to contact IRM.

#### Report Parameters

1. DEFAULT REPORT HEADER FORMAT - A report header format can be selected that will be printed at the top of all patient result reports printed from this location. Header formats can be designed using the option Label/Header/Footer Formatter.

1. DEFAULT REPORT FOOTER FORMAT - This is a report footer format that will be printed at the bottom of all patient result reports printed from this location. Footer formats can be designed using the option Label/Header/Footer Formatter.

1. REPORT LEFT MARGIN - This is a column number which indicates the left margin of patient result reports. This only affects the left margin for the impression, report text, and clinical history.

1. REPORT RIGHT MARGIN - The number entered here is used as the Report Right Margin. This affects the right margin for the impression, report text, and clinical history.

1. PRINT DX CODES IN REPORT? - If this field is set to YES, all primary and secondary diagnostic codes associated with the exam will be printed on the exam report. Since the primary diagnostic code may be printed in exam report headers and footers, you may also need to change report header and footer setups to get the diagnostic codes printed exactly as you wish. If this field is set to NO, you can include the primary diagnostic code in headers or footers by using the Label/Header/Footer Formatter.

**Note:** The device for this parameter is set up via the IRM Menu option Device Specifications for Imaging Locations. If a printer has not been assigned to this prompt, a message will tell you to contact IRM.

1. VOICE DICTATION AUTO-PRINT - If this field is set to YES, and voice dictation is used to enter a report, a copy of the report will be automatically printed on the device defined in the field Report Print Name.

#### Cameras/Equip/Rooms Used by this Location

1. CAMERA/EQUIP/RM - This multiple field will contain all cameras, equipment, or rooms associated with this Imaging Location. Cameras, equipment, and rooms already entered through the Camera/Equip/Rm Entry/Edit option may be used or new ones can be entered at this prompt.

#### Default CPT Modifiers used by this Location

Default CPT modifier(s) entered for this location will be automatically entered into each exam record during exam registration when the following 2 conditions are met:

- There is no default CPT Modifier for this exam's procedure.
- This location is the current sign-on (or switched-to) location.

Values entered for this field are not screened, because there is no CPT CODE for this location with which to compare it. The default values entered here may be rejected later during exam registration, when the default CPT Modifier(s) are screened, using the exam procedure's CPT CODE. If so, the following message will appear:

** Unable to enter default CPT Modifier \_\_ (Modifier name) **

#### Recipients of the 'Stat' Alert for this Location

1. ☞STAT REQUEST ALERT RECIPIENTS - To receive a stat request alert, a recipient must have a Radiology/Nuclear Medicine personnel classification. They will receive an alert whenever a STAT request is submitted to this Imaging Location. To use this feature, the Division parameter, "Ask Imaging Location" must be set to YES, and OE/RR Version 3.0 or higher must be installed.
2. ☞URGENT REQUEST ALERTS? - This field will determine if alerts will be sent to the Imaging Personnel defined in the "Stat Request Alert Recipients" field. If this field is set to YES, then all the users in the "Stat Request Alert Recipients" field will be sent an alert for urgent requests. To use this feature, the Division parameter "Ask Imaging Location" must be set to YES, and OE/RR Version 3.0 or higher (CPRS) must be installed.
3. ☞ALLOW 'RELEASED/NOT VERIFIED' - This Imaging Location parameter can be set to YES to allow reports to have the status "RELEASED/NOT VERIFIED" which permits the displaying and printing of the report to users outside of the Imaging service even if it is not yet verified. This field was moved from the Division parameters.

1. INACTIVE - This field should only be used if an Imaging Location is no longer used. If a date is entered in this field, the Imaging Location will not be available for selection at exam registration or request submission (i.e. the "SUBMIT REQUEST TO" prompt will not allow ordering clinicians to choose this location for request printing.) However, users can still select an inactive location to process exams previously registered to it.

#### Imaging Type for this Location

1. TYPE OF IMAGING - Type of imaging done at this location. Assign **one** of the following Imaging Types to your location:
    - Angio/Neuro/Interventional
    - CT Scan
    - General Radiology
    - Magnetic Resonance Imaging
    - Cardiology Studies (Nuc Med)
    - Nuclear Medicine
    - Ultrasound
    - Vascular Lab
    1. Mammography
This Location parameter should contain the name of the type of imaging from the Imaging Type file (#79.2). If this field is filled in, the system automatically adds the proper Imaging Type on the registration record. Only procedures assigned the same Imaging Type can be registered to the location.
Assigning a new Imaging Type (i.e. one not previously selected for any other location) implies that procedures of the new Imaging Type are performed under a separate service or section at your site, and separate workload report is desired. For instance, at some sites Ultrasound may be done separately from Radiology, and it would be appropriate to assign the Ultrasound Imaging Type to one or more locations. Once the Ultrasound Imaging Type is activated in this way, and procedures designated as Ultrasound Imaging Type have been registered, the system will report Ultrasound workload separately from Radiology workload.**Note:** The Cardiology Studies Imaging Type should NOT be assigned to a location unless nuclear cardiology studies are done under a service other than Nuclear Medicine.
The software was designed to handle nuclear cardiology alone, and therefore other types of cardiology examinations such as echocardiography should not be entered into the system. Further, local modifications to add Imaging Types are strongly discouraged due to the complexity of the underlying code and associated workload implications.
Be cautious about assigning an Imaging Type not previously used to a location. This "activates" the new Imaging Type. Imaging workload reports, enter/edit options, and screen displays are all separated by their Imaging Types. Be sure this is how your service wants to handle the package. Once this package is loaded, users sign on to a specific location, which is associated with an Imaging Type. Procedures are also associated with an Imaging Type. The best bet is to look at workload for each Imaging Type and each location. Are each now treated almost separately from all others?
    1. ☞CREDIT METHOD - This field indicates the type of credit this location receives for examinations. The default is REGULAR (code 0) , which means that for this Imaging Location both the exam and the interpretation are done at your facility. If this Imaging Location has been set up to register exams done in another facility, with the imaging interpretation only done at this facility, enter code 1 (Interpretation Only) . If exams are done in this location, but interpretation is done elsewhere, enter code 3 (Technical Component Only) . If both the exam and the interpretation are done elsewhere, and exams entered for this Imaging Location are entered only for record-keeping purposes, enter code 2 (No Credit) . (This field was added to the software with the installation of patch RA*4.5*4.) Until changes are made in the other Vist *A* software packages and in the  system, codes 1 and 3 will remain inactive and not selectable.
    2. ☞SUPPRESS ORDERING? – This field indicates if this location should be suppressed from submitting a radiology request to in CPRS. If it is set to ‘YES’, the location will not be displayed in the CPRS Radiology order dialog ‘Submit To’ box. Only locations whose CREDIT METHOD code is set to No Credit (2) are eligible for order suppression. This field will NOT suppress the location from being selected through the backdoor radiology package order menus. This field can be Y(ES) or NULL. (Field added to the software with the installation of patch RA*5.0*178.)
    3. ☞DSS ID - This field is used to identify the general outpatient area where an imaging exam was done. It is used only by DSS, and only when processing outpatients. It is roughly equivalent to the "Stop Codes" previously used for crediting outpatient exams. Only entries also in the Imaging Stop Codes file #71.5 are valid. (This field was added to the software with the installation of patch RA*4.5*4.)
**Note: There are three things you must remember to do now:**
1)	For every location you set up, be sure each is assigned to a Rad/Nuc Med Division in file #79, using the option Division Parameter Set-up.
**2)	Printers may not be set up for every location. If you see the following message when editing this option, you will need to provide IRM with the name of the location and determine with IRM which printer(s) should be used to print labels when exams are registered in this location and which printer should print requests submitted to this location. Also, a default results report printer may be assigned.**
No default flash card printer has been assigned. Contact IRM.
**3)	Whenever changes are made to the location parameters, any users currently signed on to the system who want to use the new location must use the Switch Locations option or exit and reenter the package to make the new parameters take effect.**
Here is an example of editing a new location:
| Prompt/User Response                                | Discussion                                                                                                                                                  |
|-----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Location Parameter Set-up  Select Location:  **??** | Enter two question marks to obtain a list of Imaging Locations already set up. The Imaging Type of each location appears to the right of the location name. |
| Choose from:  X-RAY                                 | (GENERAL RADIOLOGY-449)                                                                                                                                     |
| NUC MED LOC                                         | (NUCLEAR MEDICINE-639)                                                                                                                                      |
| ULTRASOUND                                          | (ULTRASOUND-449)                                                                                                                                            |
| MAGNETIC RESONANCE IMAGING                          | (MAGNETIC RESONANCE IMAGING-449)                                                                                                                            |
| NUC                                                 | (NUCLEAR MEDICINE-449)                                                                                                                                      |
| FLUORO                                              | (GENERAL RADIOLOGY-449)                                                                                                                                     |
This field points to the Hospital Location File,and contains the name of this location.
| Prompt/User Response                                                                                                                                                                                                                                            | Discussion                                                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Choose from:  CAT SCAN  FLUORO  MAGNET  MAGNETIC RESONANCE IMAGING  MAMMOGRAPHY  NUC MED LOC  NUCLEAR MEDICINE  ULTRASOUND  US  WESTSIDE XRAY  X-RAY  Name given by user to any ward, clinic, file room, operating room or other location within a VA facility. | You also get a list of all available locations that are in the Hospital Location file #44 whose "Type" field is set to "CLINIC". |
| Prompt/User Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Discussion   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| Select Location:  MAMMOGRAPHY  Are you adding 'MAMMOGRAPHY' as a new IMAGING LOCATIONS (the 10TH)?  **Y**  (Yes)  IMAGING LOCATIONS TYPE OF IMAGING:  **?**  Enter an Imaging Type for this location.  Answer with IMAGING TYPE, TYPE OF IMAGING, or ABBREVIATION  Choose from:  ANGIO/NEURO/INTERVENTIONAL  CARDIOLOGY STUDIES (NUC MED)  CT SCAN  GENERAL RADIOLOGY  MAGNETIC RESONANCE IMAGING  NUCLEAR MEDICINE  ULTRASOUND  VASCULAR LAB  MAMMOGRAPHY  IMAGING LOCATIONS TYPE OF IMAGING:  **MAMMOGRAPHY** |              |
* Since you have added a new Imaging Location, remember to assign *
* it to a Rad/Nuc Med Division through Division Parameter Set-up. *
| Prompt/User Response                                                                                                                                                                                                                                                                                                                                                                        | Discussion                                                                                                                                                                                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LOCATION: MAMMOGRAPHY//  **&lt;RET&gt;**                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                   |
| Flash Card Parameters:  ----------------------  HOW MANY FLASH CARDS PER VISIT:  **1**                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                   |
| DEFAULT FLASH CARD FORMAT:  **??**  This 'locations' parameter can contain the  default format (from the 'Flash  Cards Formats' file) to be used when queuing a  flash card to print. This format is the  default 'flash card' for the current location.  Choose from:  EXAM LABEL1  FLASH1 FORMAT  FOOTER1  HEADER1  JACKET1 FORMAT  TEST FORMAT  DEFAULT FLASH CARD FORMAT: FLASH1 FORMAT | Whenever you have a question about what to enter, use one or two question marks to give you information about the prompt. Here we get a list of available formats. If there are no selections, build some formats using the option Label/Header/Footer Formatter. |
| No default flash card printer has been assigned. Contact IRM.  Jacket Label Parameters:  ------------------------  HOW MANY JACKET LBLS PER VISIT:  **1**                                                                                                                                                                                                                                   | This is the notice telling you that no printer has been assigned by IRM to this location for use as a flash card printer.                                                                                                                                         |
| DEFAULT JACKET LABEL FORMAT:  **JAC**  KET1 FORMAT  No default jacket label printer has been assigned. Contact IRM.  Exam Label Parameters:  ----------------------  HOW MANY EXAM LABELS PER EXAM: 1//  **&lt;RET&gt;**                                                                                                                                                                    |                                                                                                                                                                                                                                                                   |
| DEFAULT EXAM LABEL FORMAT:  **EXAM**  LABEL1  Exam label printer is always the same as the flash card printer.                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                   |
| Prompt/User Response                                                                                                                                                                                                                                                                                                                                                                                                                                                | Discussion                                                                                                                                                                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Order Entry Parameters:  ----------------------  No default request printer has been assigned. Contact IRM.                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                |
| Report Parameters:  ------------------  DEFAULT REPORT HEADER FORMAT:  HEADER1  DEFAULT REPORT FOOTER FORMAT:  FOOTER1  REPORT LEFT MARGIN: 10//  **&lt;RET&gt;**  REPORT RIGHT MARGIN: 70//  **&lt;RET&gt;**                                                                                                                                                                                                                                                       | All the labels and formats were built using the option Label/Header/Footer Formatter and reside in the LBL/HDR/FTR Formats file #78.2.  (Device settings may over-ride these margins.)  For typical usage or  8 Ω x 11 paper, margins of 10 and 70 are common. |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                |
| PRINT DX CODES IN REPORT?:  **??**  If this field is set to Yes, all primary and secondary diagnostic codes associated with the exam will be printed on the exam report. (  **Note:**  Since the primary diagnostic code may be printed in exam report headers and footers, you may also need to change report header and footer set-ups to get the diagnostic codes printed exact as you wish.)  Choose from:  Y yes  N no  PRINT DX CODES IN REPORT?:  **Y**  yes |                                                                                                                                                                                                                                                                |
| No default report printer has been assigned. Contact IRM.                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                |
| Prompt/User Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Discussion                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cameras/Equip/Rooms Used by this Location:  ------------------------------------------  Select CAMERA/EQUIP/RM:  **??**  This field contains a list of cameras/equip/rms (from the 'Camera/Equip/Rm' file) that can be chosen when entering data for exams done in this 'location'.  Cameras/equip/rms can be used by more than one 'location'.  Choose from:  CAMERA 1 Triple Head Spect Scanner  CAT SCAN PICKER PQ200 SCANNER  INP1 X-RAY GASTRO X-RAYS  INP2 X-RAY BROKEN LEG X-RAYS  MAMMOGRAPHIC Used in mammography exams.  MRI ROOM MAGNETIC RESONANCE IMAGING ROOM  NUC1 HEART IMAGING  NUC2 BRAIN IMAGING  OUTP1 X-RAY X-RAYS ONLY IN THIS ROOM  OUTP2 X-RAY ACCIDENT X-RAYS  PORTABLE PORTABLE  PORTABLE II Portable used in Surgery  PORTABLE III PORTABLE IN ECC  This field contains the name of this camera/equipment/room. Names must be between 1 and 30 characters in length.  Select CAMERA/EQUIP/RM:  **MAMMO**  GRAPHIC  Used in mammography exams.  Are you adding 'MAMMOGRAPHIC' as a new CAMERAS/EQUIP/RMS (the 1ST for this IMAGING LOCATIONS)?  **Y**  (YES)  Select CAMERA/EQUIP/RM:  **&lt;RET&gt;** |                                                                                                                                                                                                                                        |
| Default CPT Modifiers used by this Location:  --------------------------------------------                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | More than one modifier may be entered.                                                                                                                                                                                                 |
| +----------------------------------------------------------------+  &#124; Your entry cannot be compared with a CPT CODE, so be very sure &#124;  &#124; that this is the Default CPT Modifier that you want to stuff &#124;  &#124; into every registered exam from this imaging location.  &#124;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                        |
| +----------------------------------------------------------------+  Select DEFAULT CPT MODIFIERS(LOC):  **26**  PROFESSIONAL COMPONENT  Are you adding '26' as a new DEFAULT CPT MODIFIERS (LOC) (the 1ST for this IMAGING LOCATIONS)? No//  **Y**  (Yes)  Select DEFAULT CPT MODIFIERS(LOC):  &lt;RET&gt;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                        |
| Recipients of the 'Stat' Alert for this Location:  -------------------------------------------------  Select STAT REQUEST ALERT RECIPIENTS:  **PROVIDER1,ONE**  Select STAT REQUEST ALERT RECIPIENTS:  **&lt;RET&gt;**  URGENT REQUEST ALERTS?:  **y**  yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Only persons with Radiology/Nuclear Medicine personnel classification can be entered at this prompt.  If this field is set to YES, then all the users in the STAT REQUEST ALERT RECIPIENTS field be sent an alert for urgent requests. |
| ALLOW 'RELEASED/UNVERIFIED': no//  **&lt;RET&gt;**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Entering YES in this field permits the displaying of any report from this location to users outside of the Imaging service even if it is not verified.                                                                                 |
| INACTIVE:  **&lt;RET&gt;**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | If this location is now inactive, enter the date when it became inactive                                                                                                                                                               |
| TYPE OF IMAGING: GENERAL RADIOLOGY//  **&lt;RET&gt;**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                        |
| CREDIT METHOD:  **0**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Enter:  0	Regular Credit  1	Interpretation Only  2	No Credit  3	Technical 			Component Only                                                                                                                                                                                                                                        |
| DSS ID:  **703**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Only entries also in the Imaging Stop Codes file #71.5 are valid as selections.                                                                                                                                                        |
| Select Location:  **&lt;RET&gt;**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                        |


### Inactivate a Location

**[RA SYSINACT]**

This option will set the INACTIVE field of the selected imaging location and the INACTIVE DATE field on the associated Occasion of Service (OOS) clinic in the HOSPITAL LOCATION file. It can also be used to inactivate the OOS clinic for an I-LOC that is already inactive.

**Note** that if you do NOT want to inactivate the OOS clinic, use the ‘Location Parameter Set-up’ option to set the inactive date on the imaging location only.

| Prompt/User Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Discussion                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| This option will allow you to inactivate an Imaging Location and the associated Occasion of Service (OOS) Hospital Location  Select Location:  **OUTSIDE VASCULAR**  (VASCULAR LAB-500) ALBANY  OUTSIDE VASCULAR STATUS: ACTIVE  OOS CLINIC (IEN 546) STATUS: ACTIVE  INACTIVATE 'OUTSIDE VASCULAR' Imaging Location? YES//  **&lt;Return&gt;**  Enter the INACTIVATION date for this location:  **T (SEP 16, 2021)**  ...Imaging Location inactivated!  ...OOS Clinic inactivated! | Select the imaging location that you wish to inactivate.  The imaging location and associated Occasion of Service (OOS) clinic active status is displayed. Depending on the status, you will be prompted to take action (inactivate the location and/or OOS clinic)  With an affirmative response above, the option prompts the user for the inactivation date to be applied to the imaging location and the OOS clinic. Future dates cannot be entered.  The option displays a message indicating success or failure. |

### Outside Location Order Suppression

**[RA SYSUPLOC]**

This option can be run at any time to update your NO CREDIT locations to suppress ordering. You may choose to update ALL or a selection of locations with this option. Only NO CREDIT locations can be selected for order suppression. If a location is set to suppress ordering, it will no longer be available in the CPRS Radiology Order Dialog to submit a radiology request to, however it can still be selected through the backdoor radiology order entry menus.

| Prompt/User Response                                                                                                                                                                                                                                                                                      | Discussion                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select Location(s):  **ALL**  Another one (Select/De-Select):  Location(s) updated...  Your outside location order suppression status:  OUTSIDE VASCULAR  Suppress Order?: YES  OUTSIDE MAMMOGRAPHY  Suppress Order?: YES  OUTSIDE CT SCAN  Suppress Order?: YES  OUTSIDE RADIOLOGY  Suppress Order?: YES | In this example, we select ALL locations. Note that it will only update locations whose CREDIT METHOD is No Credit (2).  The option will then display all available No Credit locations and their Suppress Order status. |

### Location Parameter List

**[RA SYSLOCLIST]**

After setting up all your locations, you should print out a hard copy of the data. **Make sure printers have been designated for each location where appropriate and each location has been given a Division. Any location not assigned to a Division will not appear on this report.** Note the sort order of this listing: Imaging Type, Division, Imaging Location.

Location Parameter List

Do you wish to include inactive Imaging Locations? No// **&lt;RET&gt;** NO

| Prompt/User Response                                                                                                                                                                                                                                                                                                                       | Discussion                                                                                                                                                                                                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select Imaging Location: All//  **&lt;RET&gt;**  Another one (Select/De-Select):  **-nuc**  1 NUC  2 NUC MED LOC  Choose 1-2:  **2**  (NUCLEAR MEDICINE-449)  Another one (Select/De-Select):  **-nuc**  (NUCLEAR MEDICINE)  Another one (Select/De-Select):  **&lt;RET&gt;**  DEVICE: (Enter printer) RIGHT MARGIN: 80//  **&lt;RET&gt;** | In this example, we are eliminating locations that belong to Nuclear Medicine. We accepted the default ALL because it was easier to eliminate the 2 Nuclear Medicine locations than it was to enter the 5 Radiology locations.  The following is just one page from a printout. |

Imaging Location List      PAGE 7

------------------------------------------------------------------------------

Location: X-RAY CLINIC

Division: ALBANY

Inactivation Date:

Imaging Type: GENERAL RADIOLOGY

Credit Method: Regular Credit

Suppress Ordering?: No

DSS ID: X-RAY &amp; FLUORO (XR &amp; RF)

Allow 'Released/Unverified': yes

Flash Card Parameters:   Jacket Label Parameters:

----------------------   ------------------------

Default Printer: P-DOT MATRIX BACK  Default Printer : P-DOT MATRI

Cards Per Visit: 4    Labels Per Visit: 0

Default Format : TESTALL   Default Format : JACKET1 FOR

Exam Label Parameters:   Order Parameters:

----------------------   -----------------

Default Printer: [Flash Card Printer] Default Printer: LINE

Labels Per Exam: 0    Cancellation Ptr: P-DOT MATRI

Default Format : EXAM LABEL1   Registered Ptr: RAD DIAG

After Hours Order Parameters:

----------------------------

Reporting Parameters:   Request Printer: RAD ALT XRA

---------------------   Printer Usage: AFTER HOURS

Default Printer:    Category of Exam: ALL

Default Header:    Start Time: 14:00

Default Footer:    End Time:  07:00

DX Codes in Rpt: yes    Weekends:  YES

Voice Dictation auto-print:   Holidays:  YES

Radiopharmaceutical

Dosage Ticket Parameters

------------------------

Default Printer:

Allowable Cam/Equip/Rms For This Location:

------------------------------------------

XRAY2

XRAY1

XRAY-3

Default CPT Modifiers for this location:

----------------------------------------

'Stat' Alert Recipients For This Location: Urgent Request Alerts?:

------------------------------------------

Community Care Consults for this location:

------------------------------------------

COMMUNITY CARE-IMAGING GENERAL RADIOLOGY-AUTO ALB

### Device Specifications for Imaging Locations

**[RA DEVICE]**

After setting up all your locations, **make sure printers have been designated for each location where appropriate.** This option to assign devices to imaging locations is located on the IRM Menu [RA SITEMANAGER]. The IRM parent menu is covered in more detail in the Radiology/Nuclear Medicine Technical Manual. The following is a listing of available default printers and brief explanations.

FLASH CARD PRINTER NAME: This 'locations' parameter can contain the device name (1-20 characters) that flash cards and exam labels are to be printed on. If this field is filled in, the system automatically queues the process and the user is not asked the device question.

JACKET LABEL PRINTER NAME: This 'locations' parameter can contain the device name (1-20 characters) that the jacket labels are to be printed on. If this field is filled in, the system automatically queues the process and the user is not asked the device question.

REQUEST PRINTER NAME: This 'locations' parameter can contain the device name (1-20 characters) that requests are to be printed on. If this field is filled in, the system automatically queues the process to the specified device. If this field is not filled in the request is not automatically queued to print to any device.

REPORT PRINTER NAME: This 'locations' parameter can contain the device name (1-20 characters) that reports are to be printed on. If this field is filled in, the system automatically queues the process and the user is not asked the device question.

CANCELLED REQUEST PRINTER: This field specifies the device where the cancelled request will be output.

REGISTERED REQUEST PRINTER: This field specifies the device where the registered request will be output.

ALTERNATE REQUEST PRINTER: This 'locations' parameter can contain the device name (1-20 characters) that requests are to be printed on based on the ALTERNATE PRINTER USAGE

parameter, either after hours or as an alternate printer. If this field is filled in and the other parameter criteria are met, the system automatically queues the request to the specified device. If this field is not filled in, the request is will queue to print to the REQUEST PRINTER, if defined.

The following is a listing of the Alternate Request Printer parameters:

ALTERNATE PRINTER USAGE: This location parameter is used in conjunction with the Alternate Request Printer to define its usage. The choices are:

1 AFTER HOURS PRINTER

2 ALTERNATE PRINTER

If After Hours Printer is selected, the printing logic will evaluate the After Hours parameters Begin/End times, along with Weekend, Holiday, and Category of Exam to determine if the request should be routed to the Alternate Request Printer.

If Alternate Printer is selected, the alternate printer parameters Requesting Location and Category Of Exam will be evaluated to determine if the request should be routed to the Alternate Request Printer.

AFTER HOURS BEGIN TIME: This location parameter is used in conjunction with the Alternate Request Printer to set the time of day that requests will automatically start printing on the Alternate Request Printer.

AFTER HOURS END TIME: This location parameter is used in conjunction with the Alternate Request Printer to set the time of day that requests will automatically be routed back to the Request Printer.

AFTER HOURS WEEKEND: This location parameter is used in conjunction with the Alternate Request Printer to determine if weekends (Saturday/Sunday) are considered after hours. If set to YES, radiology requests will be routed to the Alternate Request Printer all day on the weekend.

AFTER HOURS HOLIDAY: This location parameter is used in conjunction with the Alternate Request Printer to determine if holidays are considered after hours. If set to YES, radiology requests will be routed to the Alternate Request Printer all day on holidays. **Note that this parameter relies on the HOLIDAY file (#40.5) being populated with each year's holidays. If it is not populated, holidays will not be included in after hours printing.**

ARP CATEGORY OF EXAM: This location parameter is used in conjunction with the Alternate Request Printer to determine if the category of exam (patient classification) of the request will be routed to the Alternate Request Printer.

ALTERNATE PRINTER USAGE: This 'locations' parameter is used in conjunction with the Alternate Request Printer to identify requesting locations that will cause the request to be routed to the Alternate Request Printer.

Device Specifications for Imaging Locations

Do you want to see a 'help' message on printer assignment? **No//**

| Prompt/User Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Discussion                                                                                                                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select Imaging Location:  **ULTRASOUND CLINIC**  Default Printers:  -----------------  FLASH CARD PRINTER NAME:  **LABEL PTR**  JACKET LABEL PRINTER NAME:  LABEL PTR  REQUEST PRINTER NAME:  **REQUEST PTR**  REPORT PRINTER NAME:  **REPORT PTR**  CANCELLED REQUEST PRINTER:  **CAN REQ PTR**  REGISTERED REQUEST PRINTER:  **REQUEST PTR**  ALTERNATE REQUEST PRINTER:  **ALT REQ PTR**  ALTERNATE PRINTER USAGE:  **1**  AFTER HOURS PRINTER  AFTER HOURS BEGIN TIME:  **5p**  (17:00:00)  AFTER HOURS END TIME:  **7a**  (07:00:00)  AFTER HOURS WEEKEND:  **y**  YES  AFTER HOURS HOLIDAY:  **y**  YES  ARP CATEGORY OF EXAM:  **O**  OUTPATIENT | Select an existing imaging location  Enter the appropriate printers for various documents to print to, if desired.  These parameters are only displayed/populated if the alternate request printer is defined. |

## 6 Rad/Nuc Med Personnel Menu ...

Supervisor Menu ...

**Rad/Nuc Med Personnel Menu ...**

**Classi fication Enter/Edit**

**Clerical List**

**Interpreting Resident List**

**Interpreting Staff List**

**Technologist List**

**Overview:**

This menu is used to assign and track classifications of personnel who work in Diagnostic Radiology and Nuclear Medicine Services. There is only one edit option in this menu, Classification Enter/Edit. The other four options provide dated, hard copies of the data.

### Classification Enter/Edit

**[RA PNLCLASS]**

This function allows you to enter or edit personnel and their corresponding classifications. An employee will usually have only one user classification assigned to him or her at a given time; however, more than one classification per employee is allowed, as long as "Interpreting Resident" and "Interpreting Staff" are not assigned to the same employee.

☞	The Imaging Location Access prompt was changed to Rad/Nuc Med Location Access.

There are currently four classifications the personnel can be placed under. They are as follows:

1) Technologist

2) Interpreting Resident

3) Interpreting Staff

4) Clerk

All users requiring an electronic signature code (generally physician staff) should be assigned the XUSESIG option of KERNEL by the site manager.

1. All users of this package must be assigned Radiology/Nuclear Medicine location access. If they do not have at least one Radiology/Nuclear Medicine location, they will not be able to access the system.
2. **Whenever a user is on the system and their Radiology/Nuclear Medicine location access is edited via this option, that user must exit the package and reenter or use the Switch Locations option to have the new Radiology/Nuclear Medicine location access take effect.**

The prompts for technologist and clerk are identical, so only one example is shown here:

| Prompt/User Response                                                                                                   | Discussion   |
|------------------------------------------------------------------------------------------------------------------------|--------------|
| Classification Enter/Edit  Select Personnel:  **??**  Choose from:  PROVIDER,FOUR  PROVIDER,FIVE  ...  '^' TO STOP:  ^ |              |

| Prompt/User Response                                                                                                                                                                                                          | Discussion                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select Personnel:  **PROVIDER,**  SIX  Select RAD/NUC MED CLASSIFICATION:  **??**  Defines the role of this individual in the Radiology/Nuclear Medicine world.  Choose from:  T technologist  R resident  S  staff  C  clerk | Multiple classifications for one person are not usually necessary. Certain exam field edits are screened by classification. For example, only people who have a "technologist" classification are valid choices at the technologist prompt during case edits. Occasionally, residents are also classified as technologists because they act as technologists. ADPACs sometimes give themselves multiple classifications for testing purposes. |
| Select RAD/NUC MED CLASSIFICATION:  **T**  (technologist)  Are you adding 'technologist' as a new RAD/NUC MED  CLASSIFICATION (the 1ST for this NEW PERSON)?  Y  (YES)  Select RAD/NUC MED CLASSIFICATION:  **&lt;RET&gt;**   |                                                                                                                                                                                                                                                                                                                                                                                                                                               |

| Prompt/User Response                                                                                                                                         | Discussion   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| Select RAD/NUC MED LOCATION ACCESS:  **??**  This field will allow the user to access all data specific to a particular Radiology/Nuclear Medicine Location. |              |

Choose from:

X-RAY 	(GENERAL RADIOLOGY-449)

NUC MED LOC 	(NUCLEAR MEDICINE-639)

ULTRASOUND 	(ULTRASOUND-449)

MAGNETIC RESONANCE IMAGING 	(MAGNETIC RESONANCE IMAGING-449)

NUC 	(NUCLEAR MEDICINE-449)

FLUORO 	(GENERAL RADIOLOGY-449)

WESTSIDE XRAY 	(GENERAL RADIOLOGY-639)

CAT SCAN 	(CT SCAN-449)

US 	(ULTRASOUND-578)

RAD 	(GENERAL RADIOLOGY-578)

| Prompt/User Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Discussion                                                                                                                                                                                                                                                                                                                           |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select IMAGING LOCATION ACCESS:  **MAMMO**  GRAPHY  GENERAL RADIOLOGY  Are you adding 'MAMMOGRAPHY' as a new IMAGING  LOCATION ACCESS (the 1ST for this NEW PERSON)?  Y  (YES)  Select IMAGING LOCATION ACCESS:  **&lt;RET&gt;**  RAD/NUC MED INACTIVE DATE:  **&lt;RET&gt;**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Since this employee can access Mammography and Mammography is within General Radiology type of imaging, this employee will have access to the exam data belonging to the Mammography location and, in options where access is determined by Imaging Type, this employee will also be able to view data for all of General Radiology. |
| Select Personnel:  PROVIDER,SEVEN                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                      |
| Select RAD/NUC MED CLASSIFICATION:  **R**  (resident)  Are you adding 'resident' as a new RAD/NUC MED  CLASSIFICATION (the 1ST for this NEW PERSON)?  Y  (YES)  Select RAD/NUC MED CLASSIFICATION:  **&lt;RET&gt;**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | The same prompts appear for both resident and staff. Here is an example of data entry for resident.                                                                                                                                                                                                                                  |
| Select IMAGING LOCATION ACCESS:  **MAMMO**  GRAPHY  GENERAL RADIOLOGY  Are you adding 'MAMMOGRAPHY' as a new IMAGING  LOCATION ACCESS (the 1ST for this NEW PERSON)?  Y  (YES)  Select IMAGING LOCATION ACCESS:  **&lt;RET&gt;**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                      |
| RAD/NUC MED INACTIVE DATE:  **&lt;RET&gt;**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                      |
| STAFF REVIEW REQUIRED:  **??**  This field applies to 'Interpreting Resident'  personnel. If it contains a 'yes',  an interpreting staff is required to  review this resident's report results.  Choose from:  Y yes  N no  STAFF REVIEW REQUIRED:  **Y**  yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                      |
| ALLOW VERIFYING OF OTHERS:  **??**  If this field is set to 'YES' and the 'ALLOW VERIFYING BY RESIDENTS' Division parameter is also set to 'YES' then this resident is allowed to verify reports associated with another interpreting physician. (If both parameters are set to 'YES' the 'On-line Verifying of Reports' option will prompt the user to 'Select Interpreting Physician:' allowing the user to select an interpreting physician other than him/herself.) If this field is set to 'NO' then this resident is only allowed to verify his/her own reports. If the Division parameter 'ALLOW VERIFYING BY RESIDENT' is set to 'NO' then regardless of how this field is set, the resident will not be allowed to verify other interpreting physicians' reports.  If the user is classified as Interpreting Staff, s/he will always be allowed to select another interpreting physician's name and reports if this field is set to 'YES'.  Choose from:  y YES  n NO  ALLOW VERIFYING OF OTHERS:  **NO** |                                                                                                                                                                                                                                                                                                                                      |
| Select Personnel:  **&lt;RET&gt;**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                      |

### Clerical List

**[RA PNLCLERK]**

### Interpreting Resident List

**[RA PNLRES]**

### Interpreting Staff List

**[RA PNLSTAFF]**

### Technologist List

**[RA PNLTECH]**

Each personnel type is printed in the same manner. Here is an example of the Interpreting Resident List. Keep in mind that ownership of the RA ALLOC key means the user has access to every Imaging Location, even though none may be assigned to him/her.

| Prompt/User Response                                                                                                                                        | Discussion   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| Select Rad/Nuc Med Personnel Menu Option:  **INT**  1 Interpreting Resident List  2 Interpreting Staff List  Choose 1-2:  **1**  Interpreting Resident List |              |
| DEVICE: (Printer Name) RIGHT MARGIN: 80//  **&lt;RET&gt;**                                                                                                  |              |

INTERPRETING RESIDENT LIST     PAGE 1

STAFF

INACTIVE REV RAD/NUC MED

NAME  DATE  REQ'D CLASSIF. IMAGING LOC ACCESS

------------------------------------------------------------------------------

PROVIDERA,ONE    resident X-RAY

Rad/Nuc Med Keys:

------------------------------------------------------------------------------

PROVIDER,SEVEN   yes resident MAMMOGRAPHY

Rad/Nuc Med Keys:

------------------------------------------------------------------------------

PROVIDERC,ONE   no  technologist

resident ULTRASOUND

X-RAY

Rad/Nuc Med Keys: RA ALLOC

------------------------------------------------------------------------------

PROVIDERD,THREE   no  resident X-RAY

Rad/Nuc Med Keys:

## 7 Utility Files Maintenance Menu...

Supervisor Menu ...

**Utility Files Maintenance Menu ...**

**Complication Type Entry/Edit**

**Diagnostic Code Enter/Edit**

**Examination Status Entry/Edit**

**Film Type Entry/Edit**

**Label/Header/Footer Formatter**

**Major AMIS Code Entry/Edit**

**Nuclear Medicine Setup Menu ...**

**Order Entry Procedure Display Menu ...**

**Procedure Edit Menu ...**

**Radiology Community Care Consult Entry/Edit**

**Reports Distribution Edit**

**Sharing Agreement/Contract Entry/Edit**

**Standard Reports Entry/Edit**

**Valid Imaging Stop Codes Edit**

**Overview:**

New data may be added or edited via these options at any time throughout the use of the software. These options are therefore used for file maintenance as well as implementation. If this is not a new implementation of the software, you should take this time to review their contents for any necessary updating of the files. In particular, check those items that appear with the ☞icon.

This menu has corresponding options in the Maintenance Files Print Menu. As with the System Definition Menu edit options, you may want to use the Maintenance Files Print Menu to print a dated hard copy of the data entered in each file to keep your own record of changes.

### Complication Type Entry/Edit

**[RA COMPEDIT]**

This function allows the coordinator to enter or edit complication types that may occur during an exam. This option will produce the selection list you see when prompted for a complication type in the Case No. Exam Edit and Edit Exam by Patient options. These two options are used to associate complication types with specific examinations.

When there is a contrast medium reaction, the patient's record in the Adverse Reaction Tracking package will be automatically updated to indicate the patient has had a contrast media reaction. As a result, every time the patient is registered for a procedure which may involve contrast media, the user will be warned and s/he should then take the appropriate action. (The system uses CPT codes to determine whether contrast media may be used for a given procedure.)

Two complications are exported with the system, "Contrast Reaction" and "No Complication". Other site specific entries can be added using this function. You should not delete or change complication type names.

A list of complication types can be obtained through the Complication Type List option.

| Prompt/User Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Discussion                                                                                                                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Complication Type Entry/Edit  Select COMPLICATION TYPES:  **??**  Choose from:  CONTRAST REACTION  NAUSEA AND VOMITING  NO COMPLICATION  SEVERE MORBIDITY  This field contains the name of the type of  complication that may be associated with an  exam.  Initially, the system contains two complication  types: 'Contrast Reaction', and 'No  Complication'. Other complication types may be  entered by the rad/nuc med coordinator at each  site and can be 3 to 30 characters in length. | Before adding a new complication, check to see what your site already has in the file. In this example, we see four complications. Pregnancy is not there so let's add that to the file. |

| Prompt/User Response                                                                                                                                                                                                                                                                                                                                                                            | Discussion                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select COMPLICATION TYPES:  **PREGNANCY**  Are you adding 'PREGNANCY' as a new COMPLICATION  TYPES (the 5TH)?  **Y**  (Yes)  COMPLICATION: PREGNANCY//  **&lt;RET&gt;**  CONTRAST MEDIUM REACTION?:  **?**  Enter 'Y' for YES if the complication is a contrast medium reaction.  Choose from:  Y YES  N NO  CONTRAST MEDIUM REACTION?:  **N**  NO  Select COMPLICATION TYPES:  **&lt;RET&gt;** | If the Contrast Medium Reaction field is set to YES, when a patient's exam complication field is edited to include this complication, the Adverse Reaction Tracking package interface will be triggered so that contrast media can be recorded as an allergy/reaction for this patient.  The Complication Report also uses this field to determine how many patient reactions were due to contrast media. |

**Note:** All contrast media allergies and reactions are stored in the Adverse Reaction Tracking (ART) package rather than in the Radiology/Nuclear Medicine package. The automatic interface to the ART package will add contrast media to the patient's allergy records when a Rad/Nuc Med user enters this reaction through the Update Patient Record option or when entering complications marked as contrast media type reactions. When a procedure that uses a contrast medium is ordered or registered for a patient who has had a previous adverse reaction to the contrast medium, the contrast reaction message is displayed to the user.

There are other data items that most facilities require to complete the record or to submit an FDA report. It is suggested that one person from the Imaging department be responsible for following up on contrast media reactions. This person should be a member of the GMRA VERIFY DRUG ALLERGY and GMRA P&amp;T COMMITTEE FDA mail groups so that s/he receives bulletins on patient reactions to contrast media. This person should be given the necessary ART key(s) and menu option(s) to enter additional information in a consistent manner and verify the data. Talk to IRM and your Clinical Coordinator to set this up.

### Diagnostic Code Enter/Edit

**[RA DIAGEDIT]**

This function allows the coordinator to enter/edit diagnostic codes used in reports. This file builds the selection list the user sees when prompted for a Diagnostic Code.

The following is the list of diagnostic codes that are loaded as part of the initialization process:

2. Minor Abnormality
3. Major Abnormality, No Attn. Needed
4. Abnormality, Attn. Needed
5. Major Abnormality, Physician Aware
6. Undictated Films Not Returned, 3 Days
7. Unsatisfactory/Incomplete Exam
8. Possible Malignancy, Follow-up Needed

☞	An Inactive field  was added so that a code could be inactivated and no longer appear as a selection for the user. Entries should not be deleted. The names of entries should also not be changed, once in production, since this could affect their meaning in historical data.

Entering a diagnostic code for each case serves a number of purposes:

1. Diagnostic codes can be used to generate alerts to the requesting clinician whenever an examination has an abnormal result. In this option, you may designate which diagnostic codes trigger these alerts. More than one code may be designated to trigger an alert message.
2. If the site decides to enter a diagnostic code for exams, database searches using VA FileMan can be performed using the Diagnostic Code field of the exam record in the search criteria. For example, the database can be searched for all CHEST PA&amp;LAT procedures which have a diagnostic code of "Normal", or all that are "Unsatisfactory/Incomplete Exam".
3. Each case can be assigned **multiple** diagnostic codes. This allows you to not only indicate the **urgency** of the problem, but the **nature** of the problem as well, assuming you create the appropriate additional diagnostic codes. Diagnostic codes can also be used to flag teaching cases or other interesting cases if you create the appropriate diagnostic codes (example: "Teaching Case").
4. Diagnostic codes that have a YES in the "Print on Abnormal Report" field will result in exams with those codes appearing on an abnormal report that can be used for follow up and tracking.

| Prompt/User Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Discussion                                                                                                                                                                                                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Diagnostic Code Enter/Edit  Select DIAGNOSTIC CODES:  **??**  Choose from:  1  2  MINOR ABNORMALITY  3  MAJOR ABNORMALITY, NO ATTN. NEEDED  4  ABNORMALITY, ATTN. NEEDED  5  MAJOR ABNORMALITY, PHYSICIAN AWARE  6  UNDICTATED FILMS NOT RETURNED, 3 DAYS  7  UNSATISFACTORY/INCOMPLETE EXAM  8  POSSIBLE MALIGNANCY, FOLLOW-UP NEEDED  9  POSSIBLE MALIGNANCY, FOLLOW-UP CRITICAL  This field contains a short diagnostic code to  indicate the results of the interpreting  physician's analysis of the images. Diagnostic  codes can be between 3 and 40 characters in  length and can be used as a basis for database  searches. (i.e.. How many '' chest exams  were performed during a specific time period?)  Eight diagnostic codes are included with the  original package. Other site-specific  diagnostic codes may be entered by the rad/nuc  med coordinator at each site. | We want to add a diagnostic code for overexposure. Let's first see what the file contains by entering "??" at the Diagnostic Codes prompt. Codes 1 - 8 were exported with the software. Code #9 was added by the site.  We want to add a code so we enter the name of the code in 3 - 40 characters. |
| Select DIAGNOSTIC CODES:  **OVEREXPOSURE, MECH ERROR**  Are you adding 'OVEREXPOSURE, MECH ERROR' as  a new DIAGNOSTIC CODES (the 10TH)?  **Y**  (Yes)  DIAGNOSTIC CODES NUMBER: 10//  **&lt;RET&gt;**  DIAGNOSTIC CODE: OVEREXPOSURE, MECH ERROR  Replace  **&lt;RET&gt;**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | It will be the 10th code.  We have an opportunity to change the code number if we want and edit the name. Some facilities use special code # ranges for each Imaging Type (e.g., 50-59 for CT, 90-99 for MRI).                                                                                       |
| DESCRIPTION:  **OVEREXPOSURE DUE TO A MECHANICAL ERROR**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | We can give the code a longer description, 1 - 80 characters.                                                                                                                                                                                                                                        |
| PRINT ON ABNORMAL REPORT:  **Y**  YES                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Should exams given this code print on the Abnormal Exam Report? If yes, then enter a YES at this prompt.                                                                                                                                                                                             |
| GENERATE ABNORMAL ALERT?:  **N**  NO  INACTIVE:  **&lt;RET&gt;**  Select DIAGNOSTIC CODES:  **&lt;RET&gt;**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Do you want this code to generate an Alert to the requesting physician? For this example, an alert is not needed.  For more information about alerts, refer to OE/RR and Kernel documentation.                                                                                                       |

### Examination Status Entry/Edit

**[RA EXAMSTATUS]**

The Examination Status file #72 contains various statuses for each Imaging Type. An examination status is a designated point from the time a case is registered in an Imaging Location (Waiting for Exam) through its completion (Complete). These statuses **do not** include request statuses such as Pending and Hold or results reporting statuses such as Draft and Verified. If your site decides to activate any Imaging Type other than General Radiology, then you must use this option to define how the statuses will work for each Imaging Type activated. If this is a virgin installation of the software, General Radiology should be treated no differently than the other Imaging Types.

When the system is initialized, the statuses will be set up, **but not activated** , for each exported Imaging Type (excluding General Radiology which is activated). **Note: 6 statuses will exist in the file for each of the 9 Imaging Types (i.e., 54 total statuses, 6 per Imaging Type).** This makes it possible for the status parameter setup to be tailored differently for each Imaging Type.

The fields you edit in this option generally fall into three basic categories:

1. Fields that indicate what data is mandatory for an exam to progress to the given status.
2. Which prompts should be asked of the user when trying to move an exam into the given status (applies to the Status Tracking option only).
3. Fields that indicate to the various workload report routines whether an exam in a particular exam status should be used in the compilation of that report.

Except for the Imaging Type, Examination Status, User Key Needed, and Default Next Status fields, all responses are answered with a YES/NO or bypassed.

☞	This version of the software changes the appearance of a number of the prompts by using the Title for the prompt instead of the actual field Name.

**Note: Only the Status Tracking of Exams option will follow the status parameters for the "Ask" prompts. Case No. Exam Edit or Edit Exam by Patient will not do this. All three options will follow the "Require" parameters to progress to the next status.**

IMAGING TYPE - Statuses are defined for each Imaging Type. You begin in this option by telling the system which activated Imaging Type you want to edit. Remember, an Imaging Type is activated when one or more Imaging Locations and one or more procedures have been assigned to it.

EXAMINATION STATUS - This field is the current exam status being defined. When the software is installed, the required entries of the Examination Status file are created for each Imaging Type:

1. There is a status with an order of "1" (WAITING FOR EXAM)  for each Imaging Type. This is the status that the module will place an exam in upon registration regardless of which data has been entered. **The name and order of the status must not be changed.**

1. There is a status with an order of "9" (COMPLETE)  for each Imaging Type. When an exam reaches this status, then the module considers the exam complete and the exam can no longer be called up by case number. The case number can then be reused. **The name and order of the status must not be changed.**

1. There is a status with an order of "0" (CANCELLED)  for each Imaging Type. Cancelled case numbers are also reused. **The name and order of the status must not be changed.**

If you intend to assign statuses other than the above three, a numbering system of 2 through 8 is used to assign each status. The higher the number assigned to a status, the more complete the exam should be.

The statuses Called for Exam, Examined, and Transcribed are also installed with the software and appear as part of the selection list. No order numbers are installed for Called for Exam, Examined, or Transcribed. They are available for your use but are not required for status tracking to function. **If you apply an order number to any one of these three statuses, you will activate that status.** We suggest you use the worksheet provided at the back of this manual to plan your strategy when implementing new Imaging Types and/or statuses.

ORDER IN SEQUENCE OF STATUS PROGRESSION  - This field contains the logical order that this exam status falls into. The order of the progression is set up by your site and must be a number from 2 through 8. If this field is left blank, then the Exam Status Tracking function will not use the status you selected.

SHOULD THIS STATUS APPEAR IN STATUS TRACKING - **For any statuses that you activate, consider answering YES at this prompt.** The Appears on Status Tracking field, if set to YES, will cause exams of that status to come up for edit in the Status Tracking option. If left blank or NO, exams of that status will be bypassed. If, for example, you answer NO or bypass this field for every status, you would get nothing on Status Tracking.

Unless there is some site-specific reason to do otherwise, all sites should have Waiting for Exam appear on status tracking, because a newly registered exam is automatically set to it. Examined is a status that sites often want to appear in Status Tracking. The system does not allow Complete and Cancelled statuses to appear on status tracking.

An example of when this field would be set to NO is for a status called Transcribed. Many times after a report is transcribed it may not be verified for a day or two and the number of Transcribed exams may get very large. If Transcribed was displayed in the status tracking function, then the system performance would suffer because all these exams would have to be processed and displayed.

USER KEY NEEDED TO MOVE AN EXAM TO THIS STATUS - When extra protection is desired on an exam status, use this field to define the security key. If this field is set to a valid security key, then the user will need that key in order to move an exam into this status.

If a key is desired, IRM will have to create it and allocate it to the appropriate users. It is the coordinator's responsibility to enter this key into this field after IRM creates it. The key name must start with "RA".

DEFAULT NEXT STATUS FOR EXAM - This field contains the name of the next status that the current status can advance to, after the parameters of that next status are met. The next status must be active, i.e., it must have data for the parameter Order in Sequence of Status Progression. The Exam Status Tracking function uses this field in determining which prompts should be displayed for edit by the user. For example, if the "Default Next Status" is Examined for a case in the Waiting for Exam status, the Status Tracking option will prompt for all the "Ask…" fields you have set to YES for the Examined status.

**Note: If you do not enter a "Default next status for exam", the user will be asked to choose a next status during status tracking.** Most sites choose a default next status that requires the most possible data entry at one session. For example, the default next status for Waiting for Exam might be Examined, and the default next status for Examined might Complete.

The more default next statuses you use, the more times a user will have to use the status tracking option to force the exam to go to the next status. However, if you go to the other extreme and make Waiting for Exam's default next status Complete, you may not get a fine enough granularity of status differentiation for status tracking.

A simple, but still viable setup would be the following:

| Appear on Status Tracking:   | Default Next Status:   |
|------------------------------|------------------------|
| Waiting for Exam             | Examined               |
| Examined                     | Complete               |

CAN AN EXAM BE CANCELLED WHILE IN THIS STATUS - While an exam is in this status, should the user be allowed to cancel an exam? Answer with YES to allow canceling and NO to disallow canceling. If no entry is made in this field for the current status, then the user will **not** be allowed to cancel the exam.

GENERATE EXAM ALERT FOR REQUESTING PHYSICIAN - This field contains a YES if the exam status should generate an alert to the requesting physician that the patient has been examined.

☞	GENERATE EXAMINED HL7 MESSAGE - If an HL7 message should be generated when a patient is examined, enter a YES at this prompt. The usual purpose of this field is to identify the status where images have been collected. The HL7 message recipient is usually a vendor-supplied PACS or other system that needs this HL7 message to trigger some action. There are other events that automatically trigger different HL7 messages to be sent by Rad/Nuc Med. These are fully discussed in the technical manual.

Vist *A* RAD CATEGORY – This field will only appear if your site is running the Imaging package and is only needed by sites using VistaRad for soft-copy reading of images.

**Vistarad Category Values:** If this Examination Status is to be used for exams that will be read with VistaRad, then enter a value that corresponds to it from the following selections:

W	Waiting for Exam

E	Examined (assigned when the tech has completed image acquisition)

D	Dictated/Interpreted (assigned when the radiologist has completed the diagnostic reading)

T	Transcribed (assigned when the report has been transcribed)

**Note:** Not all status codes should be assigned a Vistarad Category value. Exam statuses other than the above selections should not be entered into this field.

**Vistarad Types of Lists:** The Vistarad software produces the following types of lists of Radiology exams. Each type includes exams based on the value of the Examination Status at the time the list is compiled according to the Vistarad Category that is assigned.

Vistarad Type of List	Rad/Nuc Med Exam Vistarad Category

Unread	Includes all exams with Category "E"

Recent	Includes Categories "D" and "T"

All Active	Includes Categories "D", "T", and "E"

Pending	Includes all exams with Category "W"

**Exam Locking:** When a radiologist reads exams from the Vistarad workstation, the software uses an exam "lock" to guarantee that the same exam is not read by two or more radiologists at the same time. In order for an exam to be locked, it must pass these tests:

1. It is not already locked by another radiologist, and
2. Its current Status must be "Examined"

The "Examined" Status is assigned at the time the technologist completes the image acquisition and performs the corresponding Case Edit operation in the Radiology package. The Vistarad Category field is used to let Vistarad know which Status values mean "Examined" and therefore which ones are eligible to be locked for reading.

**Status Change Requirements**

-----------------------------------------------

TECHNOLOGIST REQUIRED - This field may be set to YES to require that the name of the Technologist must be entered in order for an exam to be moved into the current status being defined.

RESIDENT OR STAFF REQUIRED **-** This field may be set to YES to require that an Interpreting Resident or Staff Physician be entered in order for an exam to be moved into the current status being defined.

DETAILED PROCEDURE REQUIRED - This field may be set to YES to require that a Detailed Procedure type be entered in order for an exam to be moved into the current status being defined. If the Division parameter requiring that a Detailed Procedure type be entered when ordering an exam is set to YES, then the Division requirement takes precedence over this requirement.

FILM ENTRY REQUIRED **-** This field may be set to YES to denote that Film Entry is required in order for an exam to be moved into the current status being defined.

DIAGNOSTIC CODE REQUIRED - This field may be set to YES to require that the Primary Diagnostic Code be entered in order for an exam to be moved into the current status being defined.

CAMERA/EQUIP/RM REQUIRED - This field may be set to YES to require that the Camera/Equip/Rm be entered in order for an exam to be moved into the current status being defined.

PROCEDURE MODIFIERS REQUIRED – This field should be set to YES if an exam requires at least 1 procedure modifier be entered in order for an exam to be moved into the current status being defined.

CPT MODIFIERS REQUIRED - This field should be set to YES if an exam requires at least 1 CPT modifier be entered in order for an exam to be moved into the current status being defined.

(Radiopharmaceuticals requirements)

**The following Radiopharmaceutical prompts only appear if you are editing the Imaging Types of Nuclear Medicine or Cardiology Studies.**

☞	RADIOPHARMS &amp; DOSAGES REQUIRED - This field may be set to YES to require that the Radiopharmaceuticals and Dosages be entered in order for an exam of this Imaging Type to be moved into the current status being defined.

To override the requirement for radiopharmaceutical on an individual procedure, set the "Suppress Radiopharm Prompt" field of the Rad/Nuc Med Procedure file to "1" for that procedure using Procedure Enter/Edit option.

☞	ACTIVITY DRAWN REQUIRED (RADIOPHARM) - This field may be set to YES to require that the Activity Drawn be required in order for an exam of this Imaging Type to be moved into the current status being defined.

☞	DRAWN DT/TIME AND PERSON REQUIRED (RADIOPHARM) -  This field may be set to YES to require that the Date/Time of the measure and the Person who measured the dose be entered in order for an exam of this Imaging Type to be moved into the current status being defined.

☞	ADMIN DT/TIME/PERSON REQUIRED (RADIOPHARM) - This field may be set to YES to require that the Date/Time of Dose Administration and the Person who administered the dose be entered in order for an exam to be moved into the current status being defined.

☞	ROUTE/SITE REQUIRED (RADIOPHARM ADMINISTERED) - This field may be set to YES to require that the Route of Administration and Site of Administration be entered in order for an exam of this Imaging Type to be moved into the current status being defined.

**Note: If a selected route has no associated site, this requirement is ignored.**

☞	LOT NO. REQUIRED (RADIOPHARM) - This field may be set to YES to require that the Lot No. be entered in order for an exam of this Imaging Type to be moved into the current status being defined.

☞	VOLUME/FORM REQUIRED (RADIOPHARM) - This field may be set to YES to require that the Volume and Form be entered in order for an exam of this Imaging Type to reach the current status being defined.

**WARNING: You must use the reporting feature of the system**

**as a prerequisite for the following requirements:**

REPORT ENTERED REQUIRED - This field may be set to YES to require that an exam have an entry in the Rad/Nuc Med Reports file #74. This does **not** mean that the report text field of the report record must be populated.

IMPRESSION REQUIRED - This field may be set to YES to require that a report Impression be entered in order for an exam to be moved into the current status being defined. **For each Imaging Type, the Impression should be required at some point (probably for the Transcribed or Complete status). Since the report text can be purged, it is strongly advised that an Impression be mandatory with each exam.**

VERIFIED REPORT REQUIRED - This field may be set to YES to require that the report be Verified in order for an exam to be moved into the current status being defined.

**Status Tracking Functions**

**-------------------------------------------**

Depending on how each site sets up the following fields, the user may or may not be prompted for the data while using the exam status tracking function.

ASK FOR TECHNOLOGIST - If this field is set to YES, then the user will be prompted for the Technologist in order to update an exam to this status.

ASK FOR INTERPRETING PHYSICIAN - If this field is set to YES, then the user will be prompted for both the Resident and Staff Interpreting Physicians in order to update an exam to this status.

ASK FOR PROCEDURE **-** If this field is set to YES, then the user will be prompted for the Procedure in order to update an exam to this status.

ASK FOR FILM DATA **-** If this field is set to YES, then the user will be prompted for the Film Data in order to update an exam to this status.

ASK FOR DIAGNOSTIC CODE **-** If this field is set to YES, then the user will be prompted for the Primary Diagnostic Code in order to update an exam to this status. If a Primary Diagnostic code is entered, another prompt will appear asking for a Secondary Diagnostic Code.

ASK FOR CAMERA/EQUIP/RM - If this field is set to YES, then the user will be prompted for the Camera/Equip/Rm in order to update an exam to this status.

ASK FOR PROCEDURE MODIFIERS - If this field is set to YES, then the user will be prompted for Procedure Modifiers in order to update an exam to this status.

ASK FOR CPT MODIFIERS - If this field is set to YES, then the user will be prompted for CPT Modifiers in order to update an exam to this status.

ASK FOR USER CODE - If this field is set to YES, then the user will be prompted for the User Code in order to update an exam to this status.

☞	ASK MEDICATIONS &amp; DOSAGES - This parameter works in conjunction with a parameter on the Rad/Nuc Med Procedure file #71. If this field is set to YES, **and** the "Prompt for Meds" field of the procedure (in the Rad/Nuc Med Procedure file #71) is set to YES, then the user will be prompted for the Medication and Dose in order to update an exam of this Imaging Type to this status.

☞	ASK MEDICATION ADMIN DT/TIME &amp; PERSON  If this field is set to YES, then the user will be prompted for the Date and Time the medication was administered and the Person who administered the dose in order to update an exam of this Imaging Type to this status. However, this will only happen if medications and dosages were entered.

(Radiopharmaceuticals functions)

**The following Radiopharmaceutical prompts only appear if you are editing the Imaging Types of Nuclear Medicine or Cardiology Studies.**

☞	ASK RADIOPHARMACEUTICALS AND DOSAGES - If this field is set to YES, then the user will be prompted for the Radiopharmaceutical and Dose in order to update an exam of this Imaging Type to this status.

**To override this parameter, and turn OFF the prompt for radiopharmaceuticals on an individual procedure, set the "Suppress Radiopharm Prompt" field of the Rad/Nuc Med Procedure file to "1" for that procedure using the Procedure Enter/Edit option.**

☞	ASK ACTIVITY DRAWN (RADIOPHARMACEUTICAL) - If this field is set to YES and a Radiopharmaceutical has been entered, then the user will be prompted for the Activity Drawn in order to update an exam of this Imaging Type to this status.

☞	ASK DRAWN DT/TIME &amp; PERSON (RADIOPHARMACEUTICAL) - If this field is set to YES and a Radiopharmaceutical has been entered, then the user will be prompted for the Date/Time of measure and Person who measured the dose when updating an exam of this Imaging Type to this status.

☞	ASK ADMIN DT/TIME &amp; PERSON (RADIOPHARMACEUTICAL) - If this field is set to YES and a Radiopharmaceutical has been entered, then the user will be prompted for the Date/Time of dose administration and the Person who administered the dose in order to update an exam of this Imaging Type to this status.

☞	ASK ROUTE/SITE OF ADMIN (RADIOPHARM) - If this field is set to YES and a Radiopharmaceutical has been entered, then the user will be prompted for the Route of administration and Site of administration in order to update an exam of this Imaging Type to this status.

☞	ASK LOT NO. (RADIOPHARM) - If this field is set to YES and a Radiopharmaceutical has been entered, then the user will be prompted for the Lot No. in order to update an exam of this Imaging Type to this status.

☞	ASK VOLUME/FORM (RADIOPHARM) - If this field is set to YES and a Radiopharmaceutical has been entered, then the user will be prompted for Volume and Form in order to update an exam of this Imaging Type to this status.

**Management Report Criteria**

**-----------------------------------------------**

When the workload report routine is processing an exam that is in the exam status currently being defined, it will check the following associated parameters to determine whether to include the exam in the report compilation.

Cancelled and/or Complete exams will be included on any report addressed in this option if the field for Cancelled and/or Complete contains a YES. The only exception to this is the Delinquent Status Report. Cancelled and Complete exams will not be included on the Delinquent Status Report even if you do enter YES in the "Delinquent Status Report?" field for the Cancelled and/or Complete statuses.

CLINIC REPORT SHOULD INCLUDE EXAMS OF THIS STATUS - Set this parameter to YES, to indicate that exams with the exam status currently being defined should be included in the Clinic Workload Report.

PTF BEDSECTION REPORT SHOULD INCLUDE EXAMS OF THIS STATUS - Set this parameter to YES, to indicate that exams with the exam status currently being defined should be included in the PTF Bedsection Workload Report.

SERVICE REPORT (WORKLOAD) SHOULD INCLUDE EXAMS OF THIS STATUS - Set this parameter to YES, to indicate that exams with the exam status currently being defined should be included in the Service Workload Report.

SHARING/CONTRACT REPORT (WORKLOAD) SHOULD INCLUDE EXAMS OF THIS STATUS - Set this parameter to YES, to indicate that exams with the exam status currently being defined should be included in the Sharing/Contract Workload Report.

WARD REPORT (WORKLOAD) SHOULD INCLUDE EXAMS OF THIS STATUS - Set this parameter to YES, to indicate that exams with the exam status currently being defined should be included in the Ward Workload Report.

FILM USAGE REPORT (WORKLOAD) SHOULD INCLUDE EXAMS OF THIS STATUS - Set this parameter to YES, to indicate that exams with the exam status currently being defined should be included in the Film Usage Workload Report.

TECHNOLOGIST REPORT (WORKLOAD) SHOULD INCLUDE EXAMS OF THIS STATUS - Set this parameter to YES to indicate that exams with the exam status currently being defined should be included in the Technologist Workload Report.

AMIS REPORT (WORKLOAD) SHOULD INCLUDE EXAMS OF THIS STATUS - Set this parameter to YES, to indicate that exams with the exam status currently being defined should be included in the AMIS Workload Report.

DETAILED PROCEDURE REPORT (WORKLOAD) SHOULD INCLUDE EXAMS OF THIS STATUS - Set this parameter to YES, to indicate that exams with the exam status currently being defined should be included in the Detailed Procedure Workload Report.

CAMERA/EQUIP/RM REPORT SHOULD INCLUDE EXAMS OF THIS STATUS - Set this parameter to YES, to indicate that exams with the exam status currently being defined should be included in the Camera/Equip/Rm Workload Report.

PHYSICIAN REPORT SHOULD INCLUDE EXAMS OF THIS STATUS - Set this parameter to YES, to indicate that exams with the exam status currently being defined should be included in the Physician Workload Report.

RESIDENT REPORT SHOULD INCLUDE EXAMS OF THIS STATUS - Set this parameter to YES, to indicate that exams with the exam status currently being defined should be included in the Resident Workload Report.

STAFF REPORT SHOULD INCLUDE EXAMS OF THIS STATUS - Set this parameter to YES, to indicate that exams with the exam status currently being defined should be included in the Staff Workload Report.

DELINQUENT STATUS REPORT SHOULD INCLUDE EXAMS OF THIS STATUS - Set this parameter to YES, to indicate that exams with the exam status currently being defined should be included in the Delinquent Status Report.

**Radiopharmaceutical Dosage Ticket Print Control**

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

**Note: The following radiopharmaceutical prompt only appears if you are editing the Imaging Type Nuclear Medicine or Cardiology Studies.**

☞	PRINT DOSAGE TICKET WHEN EXAM REACHES THIS STATUS - If an exam of this Imaging Type that uses radiopharmaceuticals reaches this status and this field is set to YES, a dosage ticket will be printed if the following are also true:

1. A valid print device has been assigned to the Imaging Location.
2. YES has been answered for the Radiopharms/Dosages Required field at this (or lower) status for this Imaging Type.

#### Exported Setup

The following setup is exported for all Imaging Types. Any setup already done by your site will be left untouched. Recommended answers are shown for all fields, but you will have to fill in the unanswered fields. The fields shaded, only apply to Imaging Type file entries whose "Radiopharmaceuticals Used?" field is set to YES (Nuclear Medicine and/or Cardiology Studies). This field is not editable.

Note: The Statuses are populated, but not activated.

If Imaging Types other than General Radiology are activated at your medical center, you will have to assign order numbers to any additional statuses you will be using, indicate whether the statuses should appear on Status Tracking, assign a default next status for each, and if you feel it is necessary, review all the other parameters associated with the statuses.

**Field:	Statuses:**

|                                                | Can-celled   | Waiting  for  Exam   | Called  for Exam   | Exam-ined   | Tran-scribed   | Com-plete   |
|------------------------------------------------|--------------|----------------------|--------------------|-------------|----------------|-------------|
| Order in sequence of status progression        | **0**        | **1**                |                    |             |                | **9**       |
| Should this Status appear in Status Tracking   |              | **Y**                |                    |             |                |             |
| User Key needed to move an exam to this status |              |                      |                    |             |                |             |
| Default next status for exam                   |              |                      |                    |             |                |             |
| Can an exam be cancelled while in this status  | **Y**        | **Y**                | **Y**              |             |                |             |
| Generate exam alert for requesting physician   |              |                      |                    |             |                |             |
| Generate Examined HL7 Message                  |              |                      |                    |             |                |             |
| VISTARAD Category                              |              |                      |                    |             |                |             |

|                                                | Can-celled   | Waiting  for  Exam   | Called  for Exam   | Exam-ined   | Tran-scribed   | Com-plete   |
|------------------------------------------------|--------------|----------------------|--------------------|-------------|----------------|-------------|
| **Data Requirements for this Status**          | **-----**    | **-----**            | **-----**          | **-----**   | **-----**      | **-----**   |
| Technologist Required                          |              |                      | **Y**              | **Y**       | **Y**          | **Y**       |
| Resident or Staff Required                     |              |                      |                    |             | **Y**          | **Y**       |
| Detailed Procedure Required                    |              |                      |                    | **Y**       | **Y**          | **Y**       |
| Film Entry Required                            |              |                      |                    | **Y**       | **Y**          | **Y**       |
| Diagnostic Code Required                       |              |                      |                    |             | **Y**          | **Y**       |
| Camera/Equip/RM Required                       |              |                      |                    |             | **Y**          | **Y**       |
| Radiopharms & Dosages required                 |              |                      |                    |             |                |             |
| Activity Drawn required (Radiopharm)           |              |                      |                    |             |                |             |
| Drawn Dt/Time and Person required (Radiopharm) |              |                      |                    |             |                |             |
| Admin Dt/Time/Person required (Radiopharm)     |              |                      |                    |             |                |             |
| Route/Site required (Radiopharm administered)  |              |                      |                    |             |                |             |
| Lot No. required (Radiopharm)                  |              |                      |                    |             |                |             |
| Volume/Form required (Radiopharm)              |              |                      |                    |             |                |             |
| Report Entered required                        |              |                      |                    |             | **Y**          | **Y**       |
| Impression required                            |              |                      |                    |             |                | **Y**       |
| Verified Report required                       |              |                      |                    |             |                | **Y**       |
| **To Move to this Status**                     | **-----**    | **-----**            | **-----**          | **-----**   | **-----**      | **-----**   |
| Ask for Technologist                           |              |                      | **Y**              | **Y**       |                |             |
| Ask for Interpreting Physician                 |              |                      |                    |             | **Y**          |             |
| Ask for Procedure                              |              |                      |                    | **Y**       |                |             |
| Ask for Film Data                              |              |                      |                    | **Y**       |                |             |
| Ask for Diagnostic Code                        |              |                      |                    |             | **Y**          |             |
| Ask for Camera/Equip/RM                        |              |                      |                    | **Y**       |                |             |
| Ask for User Code                              |              |                      |                    |             |                |             |
| Ask Medications & Dosages                      |              |                      |                    |             |                |             |
| Ask Medication Admin Dt/Time & Person          |              |                      |                    |             |                |             |
| Ask Radiopharmaceuticals and Dosages           |              |                      |                    | **Y**       |                |             |
| Ask Activity Drawn (Radiopharmaceutical)       |              |                      |                    |             |                |             |
| Ask Drawn Dt/Time & Person (Radiopharm)        |              |                      |                    |             |                |             |
| Ask Admin Dt/Time & Person (Radiopharm)        |              |                      |                    |             |                |             |
| Ask Route/Site of Admin (Radiopharm)           |              |                      |                    |             |                |             |
| Ask  No. (Radiopharm)                          |              |                      |                    |             |                |             |
| Ask Volume/Form (Radiopharm)                   |              |                      |                    |             |                |             |

|                                                         | Can-celled   | Waiting  for  Exam   | Called  for Exam   | Exam-ined   | Tran-scribed   | Com-plete   |
|---------------------------------------------------------|--------------|----------------------|--------------------|-------------|----------------|-------------|
| **Exams in this Status should appear on these Reports** | **-----**    | **-----**            | **-----**          | **-----**   | **-----**      | **-----**   |
| Clinic Report                                           |              | **Y**                | **Y**              | **Y**       | **Y**          | **Y**       |
| PTF Bedsection Report                                   |              | **Y**                | **Y**              | **Y**       | **Y**          | **Y**       |
| Service Report (Workload)                               |              | **Y**                | **Y**              | **Y**       | **Y**          | **Y**       |
| Sharing/Contract Report (Workload)                      |              | **Y**                | **Y**              | **Y**       | **Y**          | **Y**       |
| Ward Report (Workload)                                  |              | **Y**                | **Y**              | **Y**       | **Y**          | **Y**       |
| Film Usage Report (Workload)                            |              | **Y**                | **Y**              | **Y**       | **Y**          | **Y**       |
| Technologist Report (Workload)                          |              | **Y**                | **Y**              | **Y**       | **Y**          | **Y**       |
| AMIS Report (Workload)                                  |              | **Y**                | **Y**              | **Y**       | **Y**          | **Y**       |
| Detailed Procedure Report (Workload)                    |              | **Y**                | **Y**              | **Y**       | **Y**          | **Y**       |
| Camera/Equip/Rm Report                                  |              | **Y**                | **Y**              | **Y**       | **Y**          | **Y**       |
| Physician Report                                        |              | **Y**                | **Y**              | **Y**       | **Y**          | **Y**       |
| Resident Report                                         |              | **Y**                | **Y**              | **Y**       | **Y**          | **Y**       |
| Staff Report                                            |              | **Y**                | **Y**              | **Y**       | **Y**          | **Y**       |
| Delinquent Status Report                                |              | **Y**                | **Y**              | **Y**       | **Y**          |             |
| **Radiopharmaceutical Dosage Ticket Print Control**     | **-----**    | **-----**            | **-----**          | **-----**   | **-----**      | **-----**   |
| Print Dosage Ticket when exam reaches this status       |              |                      |                    |             |                |             |

The following example takes you through entries for Complete when setting up the Imaging Type, Nuclear Medicine. Remember, the prompts for radiopharmaceuticals will only appear when the Imaging Type is Nuclear Medicine or Cardiology Studies.

Examination Status Entry/Edit

Select an Imaging Type: **NUCLEAR MEDICINE**

Select an Examination Status: **COM** PLETE Imaging Type: NUCLEAR MEDICINE

Order: 9

...OK? Yes// **&lt;RET&gt;** (Yes)

Name of Current Exam Status: COMPLETE// **&lt;RET&gt;**

Order in sequence of status progression: 9// **&lt;RET&gt;**

Should this Status appear in Status Tracking ?: NO// **&lt;RET&gt;**

User Key needed to move an exam to this status: **&lt;RET&gt;**

Default next status for exam: **&lt;RET&gt;**

Can an exam be cancelled while in this status ?: NO// **&lt;RET&gt;**

Generate exam alert for requesting physician ?: NO// **&lt;RET&gt;**

Generate Examined HL7 Message:

Status Change Requirements

--------------------------

Please indicate which of the following is required

in order to place an exam into the 'COMPLETE' status:

Technologist Required ?: YES// **&lt;RET&gt;**

Resident Or Staff Required ?: YES// **&lt;RET&gt;**

Detailed Procedure required ?: YES// **&lt;RET&gt;**

Film Entry Required ?: NO// **&lt;RET&gt;**

Diagnostic Code Required ?: NO// **&lt;RET&gt;**

Camera/Equip/Rm Required ?: NO// **&lt;RET&gt;**

(Radiopharmaceutical requirements)

Radiopharms &amp; Dosages required ?: YES// **&lt;RET&gt;**

Activity Drawn required (Radiopharm) ?: YES// **&lt;RET&gt;**

Drawn Dt/Time and Person required (Radiopharm) ?: YES// **&lt;RET&gt;**

Admin Dt/Time/Person required (Radiopharm) ?: YES// **&lt;RET&gt;**

Route/Site required (Radiopharm administered) ?: YES// **&lt;RET&gt;**

Lot No. required (Radiopharm) ?: YES// **&lt;RET&gt;**

Volume/Form required (Radiopharm) ?: YES// **&lt;RET&gt;**

WARNING: You must use the reporting feature of the system as

a prerequisite for the following requirements:

Report Entered required ?: YES// **&lt;RET&gt;**

Impression required ?: YES// **&lt;RET&gt;**

Verified Report required ?: YES// **&lt;RET&gt;**

Status Tracking Functions

-------------------------

Please indicate which of the following should be asked when

changing an exam's status to 'COMPLETE' while using

the 'status tracking' feature:

Ask for Technologist ?: YES// **&lt;RET&gt;**

Ask For Interpreting Physician ?: YES// **&lt;RET&gt;**

Ask for Procedure ?: YES// **&lt;RET&gt;**

Ask For Film Data ?: NO// **&lt;RET&gt;**

Ask For Diagnostic Code ?: YES// **&lt;RET&gt;**

Ask For Camera/Equip/Rm ?: NO// **&lt;RET&gt;**

Ask for User Code ?: NO// **&lt;RET&gt;**

Ask Medications &amp; Dosages ?: YES// **&lt;RET&gt;**

Ask Medication Admin Dt/Time &amp; Person ?: YES// **&lt;RET&gt;**

(Radiopharmaceutical functions)

Ask Radiopharmaceuticals and Dosages ?: YES// **&lt;RET&gt;**

Ask Activity Drawn (Radiopharmaceutical) ?: YES// **&lt;RET&gt;**

Ask Drawn Dt/Time &amp; Person (Radiopharmaceutical) ?: YES// &lt;RET&gt;

Ask Admin Dt/Time &amp; Person (Radiopharmaceutical) ?: YES// **&lt;RET&gt;**

Ask Route/Site of Admin (Radiopharm) ?: YES// &lt;RET&gt;

Ask  No. (Radiopharm) ?: YES// &lt;RET&gt;

Ask Volume/Form (Radiopharm) ?: YES// **&lt;RET&gt;**

Management Report Criteria

--------------------------

Please indicate which of the following workload reports should

include exams with the 'COMPLETE' status:

Clinic Report should include exams of this status ?: YES// **&lt;RET&gt;**

PTF Bedsection Report should include exams of this status ?: YES// **&lt;RET&gt;**

Service Report (Workload) should include exams of this status ?: YES// **&lt;RET&gt;**

Sharing/Contract Report (Workload) should include exams of this status ?: YES// **&lt;RET&gt;**

Ward Report (Workload) should include exams of this status ?: YES// **&lt;RET&gt;**

Film Usage Report (Workload) should include exams of this status ?: YES// **&lt;RET&gt;**

Technologist Report (Workload) should include exams of this status ?: YES// **&lt;RET&gt;**

AMIS Report (Workload) should include exams of this status ?: YES// **&lt;RET&gt;**

Detailed Procedure Report (Workload) should include exams of this status ?: YES// **&lt;RET&gt;**

Camera/Equip/Rm Report should include exams of this status ?: YES// **&lt;RET&gt;**

Physician Report should include exams of this status ?: YES// **&lt;RET&gt;**

Resident Report should include exams of this status ?: YES// **&lt;RET&gt;**

Staff Report should include exams of this status ?: YES// **&lt;RET&gt;**

Delinquent Status Report should include exams of this status ?: YES// **&lt;RET&gt;**

Radiopharmaceutical Dosage Ticket Print Control

-----------------------------------------------

Print Dosage Ticket when exam reaches this status ?: NO// **&lt;RET&gt;**

Select an Examination Status: **&lt;RET&gt;**

Checking order numbers

\_\_\_\_\_\_\_\_\_ and Default Next Status used for status progression \_\_\_\_\_\_\_\_\_

within : NUCLEAR MEDICINE

Required order numbers are in place.

Data Inconsistency Report For Exam Statuses

DEVICE: HOME// **&lt;RET&gt;** (enter a printer or &lt;RET&gt; to display on screen)

Page: 1

Date:

Data Inconsistency Report For Exam Statuses

================================================================================

Checking order numbers

\_\_\_\_\_\_\_\_\_ and Default Next Status used for status progression \_\_\_\_\_\_\_\_\_

within : NUCLEAR MEDICINE

Required order numbers are in place.

Exam Status Data Inconsistencies Not Found.

The following example shows a setup with inconsistencies as demonstrated in the Data Inconsistency Report that follows the setup:

Select an Imaging Type: **NUCLEAR MEDICINE**

Select an Examination Status: **COMPLETE** Imaging Type: NUCLEAR MEDICINE

Order: 9

Name of Current Exam Status: COMPLETE// **&lt;RET&gt;**

Order in sequence of status progression: 9// **&lt;RET&gt;**

Should this Status appear in Status Tracking ?: NO// **&lt;RET&gt;**

User Key needed to move an exam to this status: **&lt;RET&gt;**

Default next status for exam: **&lt;RET&gt;**

Can an exam be cancelled while in this status ?: NO// **&lt;RET&gt;**

Generate exam alert for requesting physician ?: NO// **&lt;RET&gt;**

Generate Examined HL7 Message: **&lt;RET&gt;**

Status Change Requirements

--------------------------

Please indicate which of the following is required

in order to place an exam into the 'COMPLETE' status:

Technologist Required ?: YES// **&lt;RET&gt;**

Resident Or Staff Required ?: YES// **&lt;RET&gt;**

Detailed Procedure required ?: YES// **&lt;RET&gt;**

Film Entry Required ?: YES// **&lt;RET&gt;**

Diagnostic Code Required ?: YES// **&lt;RET&gt;**

Camera/Equip/Rm Required ?: YES// **&lt;RET&gt;**

(Radiopharmaceutical requirements)

Radiopharms &amp; Dosages required ?: NO// **&lt;RET&gt;**

Activity Drawn required (Radiopharm) ?: NO// **&lt;RET&gt;**

Drawn Dt/Time and Person required (Radiopharm) ?: NO// **&lt;RET&gt;**

Admin Dt/Time/Person required (Radiopharm) ?: NO// **&lt;RET&gt;**

Route/Site required (Radiopharm administered) ?: NO// **&lt;RET&gt;**

Lot No. required (Radiopharm) ?: NO// **&lt;RET&gt;**

Volume/Form required (Radiopharm) ?: NO// **&lt;RET&gt;**

WARNING: You must use the reporting feature of the system as

a prerequisite for the following requirements:

Report Entered required ?: YES// **&lt;RET&gt;**

Impression required ?: NO// **&lt;RET&gt;**

Verified Report required ?: YES// **&lt;RET&gt;**

Status Tracking Functions

-------------------------

Please indicate which of the following should be asked when

changing an exam's status to 'COMPLETE' while using

the 'status tracking' feature:

Ask for Technologist ?: YES// **&lt;RET&gt;**

Ask For Interpreting Physician ?: YES// **&lt;RET&gt;**

Ask for Procedure ?: NO// **&lt;RET&gt;**

Ask For Film Data ?: YES// **&lt;RET&gt;**

Ask For Diagnostic Code ?: YES// **&lt;RET&gt;**

Ask For Camera/Equip/Rm ?: NO// **&lt;RET&gt;**

Ask for User Code ?: NO// **&lt;RET&gt;**

Ask Medications &amp; Dosages ?: NO// **&lt;RET&gt;**

Ask Medication Admin Dt/Time &amp; Person ?: NO// **&lt;RET&gt;**

(Radiopharmaceutical functions)

Ask Radiopharmaceuticals and Dosages ?: NO// **&lt;RET&gt;**

Ask Activity Drawn (Radiopharmaceutical) ?: NO// **&lt;RET&gt;**

Ask Drawn Dt/Time &amp; Person (Radiopharmaceutical) ?: NO// **&lt;RET&gt;**

Ask Admin Dt/Time &amp; Person (Radiopharmaceutical) ?: NO// **&lt;RET&gt;**

Ask Route/Site of Admin (Radiopharm) ?: NO// **&lt;RET&gt;**

Ask  No. (Radiopharm) ?: NO// **&lt;RET&gt;**

Ask Volume/Form (Radiopharm) ?: NO// **&lt;RET&gt;**

Management Report Criteria

--------------------------

Please indicate which of the following workload reports should

include exams with the 'COMPLETE' status:

Clinic Report should include exams of this status ?: YES// **&lt;RET&gt;**

PTF Bedsection Report should include exams of this status ?: YES// **&lt;RET&gt;**

Service Report (Workload) should include exams of this status ?: YES// **&lt;RET&gt;**

Sharing/Contract Report (Workload) should include exams of this status ?: YES// **&lt;RET&gt;**

Ward Report (Workload) should include exams of this status ?: YES// **&lt;RET&gt;**

Film Usage Report (Workload) should include exams of this status ?: YES// **&lt;RET&gt;**

Technologist Report (Workload) should include exams of this status ?: YES// **&lt;RET&gt;**

AMIS Report (Workload) should include exams of this status ?: YES// **&lt;RET&gt;**

Detailed Procedure Report (Workload) should include exams of this status ?: YES// **&lt;RET&gt;**

Camera/Equip/Rm Report should include exams of this status ?: YES// **&lt;RET&gt;**

Physician Report should include exams of this status ?: YES// **&lt;RET&gt;**

Resident Report should include exams of this status ?: YES// **&lt;RET&gt;**

Staff Report should include exams of this status ?: YES// **&lt;RET&gt;**

Delinquent Status Report should include exams of this status ?: NO// **&lt;RET&gt;**

Radiopharmaceutical Dosage Ticket Print Control

-----------------------------------------------

Print Dosage Ticket when exam reaches this status ?: NO// **&lt;RET&gt;**

Select an Examination Status: **&lt;RET&gt;**

When exiting this option, you receive a report on the consistency of the data you entered. In the example shown here, several inconsistencies are noted and may or may not require correction for the status tracking function to work properly.

Checking order numbers

\_\_\_\_\_\_\_\_\_\_\_ and Default Next Status used for status progression \_\_\_\_\_\_\_\_\_

within : NUCLEAR MEDICINE

Required order numbers are in place.

DEVICE: HOME// (Enter a Device)

Page: 1

Date:

Data Inconsistency Report For Exam Statuses

================================================================================

\_\_\_\_\_\_\_\_\_ Warning on reaching Complete \_\_\_\_\_\_\_\_\_

within : NUCLEAR MEDICINE

The following are permissible, but could lead to failure to

complete cases when prompts are not answered in lower status(es).

STATUS  PROMPT      DATA

------  ------      ------

EXAMINED ASK FOR INTERPRETING PHYS?   Y

RESIDENT OR STAFF REQUIRED?   N

EXAMINED ASK FOR FILM DATA?    Y

FILM ENTRY REQUIRED?    N

EXAMINED ASK FOR DIAGNOSTIC CODE?    Y

DIAGNOSTIC CODE REQUIRED?    N

EXAMINED ASK FOR CAMERA/EQUIP/RM?    Y

CAMERA/EQUIP/RM REQUIRED?    N

TRANSCRIBED ASK FOR CAMERA/EQUIP/RM?    Y

CAMERA/EQUIP/RM REQUIRED?    N

COMPLETE ASK FOR CAMERA/EQUIP/RM?    N

CAMERA/EQUIP/RM REQUIRED?    Y

Checking order numbers

\_\_\_\_\_\_\_\_\_ and Default Next Status used for status progression \_\_\_\_\_\_\_\_\_

within : NUCLEAR MEDICINE

Required order numbers are in place.

Exam Status Data Inconsistencies Not Found.

In the above sample report, if status tracking were used to enter data, the parameters would potentially allow users to leave the Camera/Equip/Rm field blank in every Status Tracking edit session and never get a prompt at the final edit session. This would result in the exam staying in the Transcribed status. A better solution would be to change the "Ask For Camera/Equip/Rm" field to YES on the Complete status or change the "Camera/Equip/Rm Required" field on the Transcribed and Examined statuses to YES.

## Data Inconsistency Report For Exam Statuses

#### Example Status Tracking Sessions

The following sessions show how four statuses are affected by changes in data.

These are the assigned statuses for the examples:

Status			Order		Default Next Status

WAITING FOR EXAM	 	1		TRANSCRIBED

CALLED FOR EXAM	 	3		TRANSCRIBED

TRANSCRIBED		 	7		COMPLETE

COMPLETE		 	9

**Backing down to lower status** : Deleting data previously entered may cause an exam status to back down to a lower status.

Enter Case #, Status, (N)ext status, '^' to Stop: NEXT// **521**

Case # being tracked: 521

Name: TEST,FEMALE   Case # : 20

Division : HINES CIO FIELD OFFICE Location: ULTRASOUND A

Procedure: ECHOGRAM ABDOMEN COMPLETE (Detailed)

***** Old Status: CALLED FOR EXAM

***** New Status: TRANSCRIBED

Do you wish to continue? YES// &lt;ret&gt;

PRIMARY INTERPRETING RESIDENT: **&lt;ret&gt;**

PRIMARY INTERPRETING STAFF: **&lt;ret&gt;**

Select FILM SIZE: **&lt;ret&gt;**

PRIMARY DIAGNOSTIC CODE: **&lt;ret&gt;**

PRIMARY CAMERA/EQUIP/RM: **&lt;ret&gt;**

Select TECHNOLOGIST: PROVIDER,NINE// **@**

SURE YOU WANT TO DELETE? **Y** (Yes)

Select TECHNOLOGIST: **&lt;ret&gt;**

PREGNANT AT TIME OF ORDER ENTRY: NO

PREGNANCY SCREEN: u Patient is unable to answer or is unsure

PREGNANCY SCREEN COMMENT: Patient sent to lab for test

No 'technologist'  entered for this exam.

No 'film data'   entered for this exam.

No 'camera/equip/room'  entered for this exam.

No 'report'   entered for this exam.

...exam status backed down to 'WAITING FOR EXAM'

STATUS CHANGE DATE/TIME: JUN 10,1997@10:06// **&lt;ret&gt;**

...Status backed down for case #: 521

**Upgrading status but not to Default Next Status** : A case may be upgraded to a status that is not its DEFAULT NEXT STATUS, if that case’s data satisfy all required data for a status that’s higher than the old status, but lower than the default next status.

Case # being tracked: 521

Name:PATIENT,ONE   Case # : 521

Division : HINES CIO FIELD OFFICE Location: ULTRASOUND A

Procedure: ECHOGRAM ABDOMEN COMPLETE (Detailed)

<!-- image -->

Do you wish to continue? YES// **&lt;ret&gt;**

PRIMARY INTERPRETING RESIDENT: &lt;ret&gt;

PRIMARY INTERPRETING STAFF: **&lt;ret&gt;**

Select FILM SIZE: **&lt;ret&gt;**

PRIMARY DIAGNOSTIC CODE: **&lt;ret&gt;**

PRIMARY CAMERA/EQUIP/RM: **&lt;ret&gt;**

Select TECHNOLOGIST: PROVIDER,NINE

Select TECHNOLOGIST: **&lt;ret&gt;**

No 'film data'   entered for this exam.

No 'camera/equip/room'  entered for this exam.

No 'report'   entered for this exam.

No 'camera/equip/room'  entered for this exam.

No 'report'   entered for this exam.

...though upgraded, new status level (CALLED FOR EXAM)

is not as high as the desired level (TRANSCRIBED)

STATUS CHANGE DATE/TIME: JUN 10,1997@10:06// **&lt;ret&gt;**

...Status successfully changed for case #: 521

**Status unchanged** : A case’s status will remain the same, if no data had been added to, nor deleted from it.

Exam Status Tracking Module  Division: HINES CIO FIELD OFFICE

Date :  11:15 AM  Status : CALLED FOR EXAM

Locations: ULTRASOUND A

Case # Date Patient  Procedure  	 Equip/Rm

------ ---- -------  ---------  	 --------

521 9:55 AM PATIENT,ONE  ECHOGRAM ABDOMEN COMPLETE

Enter Case #, Status, (N)ext status, '^' to Stop: NEXT// **521**

Case # being tracked: 521

Name: PATIENT,ONE   Case # : 521

Division : HINES CIO FIELD OFFICE Location: ULTRASOUND A

Procedure: ECHOGRAM ABDOMEN COMPLETE (Detailed)

***** Old Status: CALLED FOR EXAM

***** New Status: TRANSCRIBED

Do you wish to continue? YES// **&lt;ret&gt;**

PRIMARY INTERPRETING RESIDENT: **&lt;ret&gt;**

PRIMARY INTERPRETING STAFF: PROVIDER,TEN// **&lt;ret&gt;**

Select SECONDARY INTERPRETING STAFF: &lt;ret&gt;

Select FILM SIZE: **&lt;ret&gt;**

PRIMARY DIAGNOSTIC CODE: NORMAL// **&lt;ret&gt;**

Select SECONDARY DIAGNOSTIC CODE: **&lt;ret&gt;**

PRIMARY CAMERA/EQUIP/RM: **&lt;ret&gt;**

Select TECHNOLOGIST: PROVIDER,NINE // **&lt;ret&gt;**

No 'film data'   entered for this exam.

No 'camera/equip/room'  entered for this exam.

...exam status not changed??

...Status unchanged for case #: 521

**Qualifies for higher status than Default Next Status** : A case may have enough data to qualify for a higher status than its DEFAULT NEXT STATUS, but Status Tracking will not allow the case to be upgraded to a status higher than the DEFAULT NEXT STATUS. If this should occur, a message will be displayed to remind the user to re-edit this case.

Exam Status Tracking Module  Division: HINES CIO FIELD OFFICE

Date :  11:16 AM  Status : CALLED FOR EXAM

Locations: ULTRASOUND A

Case # Date Patient  Procedure  	 Equip/Rm

------ ---- -------  ---------  	 --------

521 9:55 AM PATIENT,ONE  ECHOGRAM ABDOMEN COMPLETE

Enter Case #, Status, (N)ext status, '^' to Stop: NEXT// **521**

Case # being tracked: 521

Name: PATIENT,ONE   Case # : 521

Division : HINES CIO FIELD OFFICE Location: ULTRASOUND A

Procedure: ECHOGRAM ABDOMEN COMPLETE (Detailed)

***** Old Status: CALLED FOR EXAM

***** New Status: TRANSCRIBED

Do you wish to continue? YES// **&lt;ret&gt;**

PRIMARY INTERPRETING RESIDENT: **&lt;ret&gt;**

PRIMARY INTERPRETING STAFF: PROVIDER,TEN// **&lt;ret&gt;**

Select SECONDARY INTERPRETING STAFF: **&lt;ret&gt;**

Select FILM SIZE: **2**

1 2X12

2 2X4

3 2X6

CHOOSE 1-3: **1**

AMOUNT(#films or cine ft): **1**

Select FILM SIZE: &lt;ret&gt;

PRIMARY DIAGNOSTIC CODE: NORMAL// &lt;ret&gt;

Select SECONDARY DIAGNOSTIC CODE: **&lt;ret&gt;**

PRIMARY CAMERA/EQUIP/RM: **PORTABLE** PORTABLE

Select TECHNOLOGIST: PROVIDER,NINE // **&lt;ret&gt;**

This case also qualifies for higher status(es) :

COMPLETE

Since Status Tracking can only upgrade one status level at a time,

please edit this exam again.

STATUS CHANGE DATE/TIME: JUN 10,1997@11:18//

...Status successfully changed for case #: 521

Exam Status Tracking Module  Division: HINES CIO FIELD OFFICE

Date :  11:18 AM  Status : CALLED FOR EXAM

Locations: ULTRASOUND A

Case # Date Patient  Procedure  	 Equip/Rm

------ ---- -------  ---------  	 --------

Enter Case #, Status, (N)ext status, '^' to Stop: NEXT// **N**

Exam Status Tracking Module  Division: HINES CIO FIELD OFFICE

Date :  11:18 AM  Status : TRANSCRIBED

Locations: ULTRASOUND A

Case # Date Patient  Procedure  	 Equip/Rm

------ ---- -------  ---------  	 --------

20 06/20/94 PATIENT,THREE ZZLINE ULTRASOUND  PORTABLE

169 01/19/95 PATIENT,FOUR  ECHOGRAM ABDOMEN COMPLETE ROOM1

521 9:55 AM PATIENT,ONE  ECHOGRAM ABDOMEN COMPLETE PORTABLE

Enter Case #, Status, (N)ext status, '^' to Stop: NEXT// **521**

Case # being tracked: 521

Name: PATIENT,ONE   Case # : 521

Division : HINES CIO FIELD OFFICE Location: ULTRASOUND A

Procedure: ECHOGRAM ABDOMEN COMPLETE (Detailed)

***** Old Status: TRANSCRIBED

***** New Status: COMPLETE

Do you wish to continue? YES// **&lt;ret&gt;**

PRIMARY INTERPRETING RESIDENT: **&lt;ret&gt;**

PRIMARY INTERPRETING STAFF: PROVIDER,TEN // **&lt;ret&gt;**

Select SECONDARY INTERPRETING STAFF: **&lt;ret&gt;**

Select FILM SIZE: 2X12// **&lt;ret&gt;**

FILM SIZE: 2X12// &lt;ret&gt;

AMOUNT(#films or cine ft): 1// **&lt;ret&gt;**

Select FILM SIZE: **&lt;ret&gt;**

PRIMARY DIAGNOSTIC CODE: NORMAL// **&lt;ret&gt;**

Select SECONDARY DIAGNOSTIC CODE: **&lt;ret&gt;**

PRIMARY CAMERA/EQUIP/RM: PORTABLE// **&lt;ret&gt;**

Select TECHNOLOGIST: PROVIDER,NINE // **&lt;ret&gt;**

STATUS CHANGE DATE/TIME: JUN 10,1997@11:18// **&lt;ret&gt;**

...Status successfully changed for case #: 521

...will now designate request status as 'COMPLETE'...

Visit credited.

...request status successfully updated.

## ***** Old Status: WAITING FOR EXAM

### Film Type Entry/Edit

**[RA FILMEDIT]**

This function allows you to edit existing film types and enter new film types. These film types build the list of choices which the technologist can choose from when selecting a Film Size during the Status Tracking of Exams, Edit Exam by Patient, and Case No. Exam Edit options to indicate which films were used during a procedure.

An entry should be an identifying name or size. To speed up processing, assign each film type a name with unique characters at the beginning of the entry. If your medical center wants to get a report showing exams that did not use films, an entry of NO FILMS on this list is an appropriate choice. Once a film size has been entered through this option, it cannot be deleted; however, it can be inactivated. Also, enter a corresponding wasted film for each film size.

| Prompt/User Response                                                                                                                | Discussion                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Film Type Entry/Edit                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Select FILM SIZES:  **10X12**  Are you adding '10X12' as a new FILM SIZES (the 46TH)?  **Y**  (Yes)  FILM: 10X12//  **&lt;RET&gt;** | Enter ?? if you want a list of film sizes already entered at your site.  The entry should be 3-30 characters in length.                                                                                                                                                                                                                                                                                                                                                               |
| IS THIS A 'CINE' FILM SIZE?:  **NO**                                                                                                | If this field contains a YES, it indicates that this is cine film. Cine film is treated differently in compiling the AMIS reports and the Film Usage Report.                                                                                                                                                                                                                                                                                                                          |
| FLUORO ONLY?:  **&lt;RET&gt;**                                                                                                      | If this field contains a YES, it indicates that this film is used for fluoro. Exams where this film size is entered are assumed to be fluoro not requiring the use of films. Leaving this field blank is the same as answering No.                                                                                                                                                                                                                                                    |
| INACTIVATION DATE:  **&lt;RET&gt;**                                                                                                 | If this film size entry should no longer be needed, enter a date here to inactivate it. That will remove it from the user selections.  If the film type is active, there should be  **no entry**  in this field.                                                                                                                                                                                                                                                                      |
| WASTED FILM?:  **&lt;RET&gt;**                                                                                                      | Bypass this field, as shown here, if this film size is NOT a wasted type. If this field contains a YES, it indicates that the film will be considered a wasted film type and will be excluded from the "Film Usage Report". Instead, it will be included on the "Wasted Film Report".  If a film size is already associated with a wasted film size, the former cannot also be set to a wasted film size by answering "YES" at this prompt.  Let's enter a wasted film for the 10X12. |
| Select FILM SIZES:  **W-10X12**                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Are you adding 'W-10X12' as a new FILM SIZES (the 46TH)?  **Y**  (Yes)  FILM: W-10X12//  **&lt;RET&gt;**                            | We suggest you distinguish all wasted film in the same way, such as using "W-" before the name of its counterpart.                                                                                                                                                                                                                                                                                                                                                                    |
| IS THIS A 'CINE' FILM SIZE?:  **NO**  FLUORO ONLY?:  **&lt;RET&gt;**  INACTIVATION DATE:  **&lt;RET&gt;**                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| WASTED FILM?:  **Y**  YES  ANALOGOUS UNWASTED FILM SIZE:  **10X12**                                                                 | Entering "10X12" here means that when a technician enters "W-10X12" on a case, it is the "10X12" size that has been wasted.  Enter the corresponding film.                                                                                                                                                                                                                                                                                                                            |
| Select FILM SIZES:  **&lt;RET&gt;**                                                                                                 | When you exit this option, something similar to the following is displayed:                                                                                                                                                                                                                                                                                                                                                                                                           |

Relationship between 'Unwasted Film Size' and 'Corresponding Wasted FilmSize':

'Unwasted Film Size'  'Corresponding Wasted Film Size'

------------------------------------------------------------------------------

10X12    W-10X12

11X14    W-11X14

14X17    W-14X17

2X12    W-2X12

2X4    W-2X4

2X6    unassociated with a 'Wasted Film' type

....

Enter RETURN to continue or '^' to exit: **&lt;RET&gt;**

### Label/Header/Footer Formatter

**[RA FLASHFORM]**

The Label/Header/Footer Formatter option is used to enter and edit flash card, jacket and examination label formats, and headers and footers. A format specifies the data you want printed and how you want it printed on each type of card or label. Headers are the line or lines of information at the top of a result report, usually including the patient name, social security number and similar information. Footers are the information printed at the bottom of a report, for example, patient name, examination date, page number, etc.

The header, footer, and label format specifications that you enter by using the Label/Header/Footer Formatter option are stored in the Label Print Fields file #78.7. Various programs use these specifications when printing exam results reports and the labels that are printed at the time an exam is registered.

On the following page is a list of the choices you have for formatting flash cards, exam labels, jacket labels, headers and footers. When the data depends on the availability of a specific requirement, we've also included what that requirement is.

| **Label Print Fields:**          | **Requirement:**                                                                                                                                            |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Age of Patient                   | Date of Birth entered in MAS                                                                                                                                |
| Attending Physician at Order     | Must be entered in MAS                                                                                                                                      |
| Attending Physician Current      | Must be entered in MAS                                                                                                                                      |
| Case Number                      | Case must be registered                                                                                                                                     |
| Case Number Barcode              | Case must be registered, printer hardware must be capable of printing barcodes, printer device definition must be set up by IRM to support barcode printing |
| Current Date/Time                |                                                                                                                                                             |
| Current Patient Location         |                                                                                                                                                             |
| Date of Birth                    | Date of Birth entered in MAS                                                                                                                                |
| Date of Exam                     | Case must be registered                                                                                                                                     |
| Date Report Entered              | After report is entered                                                                                                                                     |
| Date Reported                    | After report is entered                                                                                                                                     |
| Diagnostic Code                  | After diagnostic codes are entered                                                                                                                          |
| Exam Modifiers                   | Modifiers must be entered                                                                                                                                   |
| Free Text                        |                                                                                                                                                             |
| Hospital Division (Institution)  |                                                                                                                                                             |
| Imaging Location                 | Exam must be registered                                                                                                                                     |
| Last Time this Exam Performed    |                                                                                                                                                             |
| Last Visit for any Exam          |                                                                                                                                                             |
| Long Case Number                 | Case must be registered                                                                                                                                     |
| Long Case Number Barcode         |                                                                                                                                                             |
| Name of Patient                  |                                                                                                                                                             |
| Page Number                      |                                                                                                                                                             |
| ☞Patient Address Line 1          | First line of street address must be entered in MAS                                                                                                         |
| ☞Patient Address Line 2          | Second and third lines of address must be entered in MAS                                                                                                    |
| ☞Patient Address Line 3          | City, State, and Zip must be entered in MAS                                                                                                                 |
| Primary Physician at Order       | Must be entered in MAS                                                                                                                                      |
| Primary Physician Current        | Must be entered in MAS                                                                                                                                      |
| Procedure                        |                                                                                                                                                             |
| Procedure Barcode, 30 chars      | Printer hardware must be capable of printing barcodes, printer device definition must be set up by IRM to support barcode printing                          |
| Procedure Barcode, 60 chars      | Printer hardware must be capable of printing barcodes, printer device definition must be set up by IRM to support barcode printing                          |
| Report Status                    | Report must be entered                                                                                                                                      |
| Request Entered Date/Time        |                                                                                                                                                             |
| Requesting Area                  |                                                                                                                                                             |
| Requesting Physician             |                                                                                                                                                             |
| Resident                         | Must be entered                                                                                                                                             |
| Resident Signature               | Report must be entered and verified by resident                                                                                                             |
| ☞Resident Signature Name         | Must be verified by resident, then looks for Signature Block Printed Name or defaults to name from the .01 field of File 200.                               |
| Service                          |                                                                                                                                                             |
| Sex of Patient                   | Must be entered in MAS                                                                                                                                      |
| SSN of Patient                   | Must be entered in MAS                                                                                                                                      |
| SSN of Patient Barcode           | Printer hardware must be capable of printing barcodes, printer device definition must be set up by IRM to support barcode printing                          |
| ☞ SSN of Patient Barcode-No Dash | Printer hardware must be capable of printing barcodes, printer device definition must be set up by IRM to support barcode printing                          |
| Staff Radiologist                | Primary Staff must be entered                                                                                                                               |
| Staff Signature                  | Report must be entered and verified by staff                                                                                                                |
| Staff Signature Name             | Must be verified by a staff member, then looks for Signature Block Printed Name or defaults to name from the .01 field of File 200.                         |
| Technologist                     | Must be entered in Exam Edit option                                                                                                                         |
| Usual Patient Category           | Must be entered via Update Patient Record                                                                                                                   |
| Verified Date                    | Report must be verified                                                                                                                                     |
| Verifying Electronic Signature   | Report must be verified                                                                                                                                     |
| Verifying Radiologist            | Report must be verified                                                                                                                                     |
| Verifying Signature              | Report must be verified                                                                                                                                     |
| Verifying Signature Block        | Report must be verified                                                                                                                                     |
| ☞Verifying Signature Name        | Must be verified, then uses Signature Block Name.                                                                                                           |
| ☞Verifying Signature Title       | Must be verified, then uses Signature Block Title from the New Person file #200.                                                                            |

When you specify formats you can also enter a "TITLE" to be printed for each field. When the field is printed, the title will precede the actual data. The positioning of each field on the page is site-specific. If no title is entered at this step, a default title is filled in by the system. If no title is desired, then the word "NONE" should be entered when you are prompted for "TITLE". This might be useful when printing the patient's address since the default would be PATIENT ADDRESS LINE 1, etc.

You will be prompted for row and column positions. These positions determine how your flash card or label is formatted. There can be a maximum of 66 rows from top to bottom of a page in a format but you must limit the number of rows used to fit on your labels and/or results report headers and footers. There can be a maximum of 80 columns across a page in a format, but labels usually allow less than 80 columns.

**After you have selected all of the fields you need, you will be asked the number of rows in the format. Be sure to answer with the highest row number you have assigned. This is necessary so that the print program will know how much space to allow on a page for headers and footers.**

After a format has been entered or edited, the system will display a test version of the format, so that you can see what it will actually look like and make any necessary changes.

When you enter Location Set-up Parameters, the Imaging Locations file #79.1 stores information telling which specifications in the Label Print Fields file #78.7 should be used to print the following:

1. Default Flash Card Format
2. Default Exam Label Format
3. Default Jacket Label Format
4. Default Report Header Format
5. Default Report Footer Format

These parameters are set using the Location Parameter Set-up option.

**Note: When designing a card or label for a specific purpose, keep in mind which data will be available at the time the card or label is printed. For instance, if the card is going to be printed at the time of registration, the system will not know the name of the technologist. Therefore, the technologist will not print out on the form even if you include the technologist field when defining the format. See the chart on the preceding page for data requirements for the fields .**

Fields that are to be printed twice in any one format should be enclosed in double quotes (e.g., a second Free Text field would be entered "FREE TEXT"). The Free Text field can be used to enter a statement which will serve as a heading or to indicate an area on the flash card where a comment or description is to be entered. When entered as free text, this statement will be interpreted by the system in its literal sense; i.e., exactly as you have entered it. You must then specify what will appear by entering the free text through the sub-field, "Literal Text". For example, if you make Free Text a part of the jacket label format and enter "***RETURN TO FILE ROOM***" at the "Literal Text:" prompt, then "***RETURN TO FILE ROOM***" will print on all jacket labels using the format.

Before starting, design your format on paper, adding spacing, counting characters for alignment, etc. Using graph paper makes it easier to count characters, lines, columns and spaces. You can use the &lt;Space&gt; key to adjust spacing. We'll show you how that works in our example.

Let's design the following flash card format. Note our plan to line up data by using spaces between the field and the colon.

NAME :	SSN :

EXAM DATE:   CASE:

PROCEDURE:

COMMENTS :

REQUESTING PHYS:

| Prompt/User Response                                                                                                                                                                                                                                                    | Discussion                                                                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Label/Header/Footer Formatter  &gt;&gt;&gt; Exam Label/Report Header/Report Footer/Flash Card Formatter &lt;&lt;&lt;  Note: re-compilation will remove all local modifications                                                                                          | **Note: The system refers to anything you design as a Flash Card Format even if it is a label or report header.**                                                                                    |
| Select FLASH CARD FORMATS FORMAT NAME:  **FLASH &amp; COMMENT**  Are you adding 'FLASH &amp; COMMENT' as a new FLASH CARD FORMATS (the 7TH)?  **Y**  (Yes)  FORMAT NAME: FLASH &amp; COMMENT//  **&lt;RET&gt;**                                                         | Enter "??" to obtain a list of formats already designed by your site. We'll call our format, FLASH &amp; COMMENT.  This is the 7th one we have on file. They can be selected and edited at any time. |
| Select FIELD:  FREE TEXT  Are you adding 'FREE TEXT' as a new PRINT FIELDS  (the 1ST for this FLASH CARD FORMATS)?  **Y**  (Yes)  ROW:  **5**                                                                                                                           |                                                                                                                                                                                                      |
| COLUMN:  **2**                                                                                                                                                                                                                                                          |                                                                                                                                                                                                      |
| Select FIELD:  **REQUESTING PH**  YSICIAN  Are you adding 'REQUESTING PHYSICIAN' as  a new PRINT FIELDS (the 2ND for this FLASH CARD  FORMATS)?  **Y**  (Yes)                                                                                                           | Requesting Physician will be another field.                                                                                                                                                          |
| ROW:  **10**  COLUMN:  **2**  TITLE (OPTIONAL):  **REQUESTING PHYS:&lt;sp&gt;**                                                                                                                                                                                         | It will print in row 10, column 2 as "REQUESTING PHYS: ". We added a space after the colon before hitting the <RET> key.                                                                             |
| Select FIELD:  **NAME OF PATIENT**  Are you adding 'NAME OF PATIENT' as a new PRINT  FIELDS (the 3RD for this FLASH CARD FORMATS)?  **Y**  (Yes)  ROW:  **1**  COLUMN:  **2**  TITLE (OPTIONAL):  **NAME&lt;sp&gt;&lt;sp&gt;&lt;sp&gt;&lt;sp&gt;&lt;sp&gt;:&lt;sp&gt;** | We are using five spaces between NAME and the colon and one space after the colon to line up colons and data.                                                                                        |
| Select FIELD:  SSN OF PATIENT  Are you adding 'SSN OF PATIENT' as a new PRINT  FIELDS (the 4TH for this FLASH CARD FORMATS)?  **Y**  (Yes)  ROW:  **1**  COLUMN:  **40**  TITLE (OPTIONAL):  **SSN&lt;sp&gt;:&lt;sp&gt;**                                               | There's one space between SSN and the colon and one after the colon.                                                                                                                                 |
| Select FIELD:  DATE OF EXAM  Are you adding 'DATE OF EXAM' as a new PRINT FIELDS  (the 5TH for this FLASH CARD FORMATS)?  **Y**  (Yes)  ROW:  **2**  COLUMN:  **2**  TITLE (OPTIONAL):  **EXAM DATE:&lt;sp&gt;**                                                        |                                                                                                                                                                                                      |
| Select FIELD:  PROCEDURE  Are you adding 'PROCEDURE' as a new PRINT FIELDS  (the 6TH for this FLASH CARD FORMATS)?  **Y**  (Yes)  ROW:  **3**  COLUMN:  **2**  TITLE (OPTIONAL):  **PROCEDURE:&lt;sp&gt;**                                                              |                                                                                                                                                                                                      |

| Prompt/User Response                                                                                                                                                                                                                            | Discussion                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Select FIELD:  **CASE**  NUMBER  Are you adding 'CASE NUMBER' as a new PRINT FIELDS  (the 7TH for this FLASH CARD FORMATS)?  **Y**  (Yes)  ROW:  **2**  COLUMN:  **40**  TITLE (OPTIONAL):  **CASE:&lt;sp&gt;**  Select FIELD:  **&lt;RET&gt;** | When we finish adding fields, we hit the &lt;RET&gt; key.                                                        |
| NUMBER OF ROWS IN FORMAT:  **10**                                                                                                                                                                                                               | Find the field with the highest row number and enter that number here. In this case it was Requesting Physician. |

Then the format of the flash card is displayed.

...format 'FLASH &amp; COMMENT' has been compiled.

&lt;&lt;&lt;&lt;&lt;&lt;----------------------------Column No.------------------------------&gt;&gt;&gt;&gt;&gt;&gt;

0--------1---------2---------3---------4---------5---------6---------7---------8

1 0  0  0  0  0  0  0  0

NAME : PATIENT,FIVE  SSN : 000-38-3342

EXAM DATE: DEC 13,1984 14:30  CASE: CASE,ONE

PROCEDURE: 1A - SKULL

COMMENTS :

REQUESTING PHYS: PROVIDERD,ONE

Comments:

The new patient address label print fields are useful for printing mailing labels for reminder postcards, mammography follow-up, etc.

The order of field entry does not matter. For example, the items on the 7 th row may be entered before rows 1-6 because the compiler reorders them per your numbering instructions.

### Major AMIS Code Entry/Edit

**[RA MAJORAMIS]**

This function allows you to add a new AMIS code or edit existing AMIS codes. AMIS (Automated Medical Information System) codes are used in the compilation of various workload reports, including the AMIS Report.

**When the system is first installed, all necessary entries and data associated with each entry will be part of the module.**

| Prompt/User Response                                                                                                                                                                                                                   | Discussion                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| Major AMIS Code Entry/Edit  Select MAJOR RAD/NUC MED AMIS CODES DESCRIPTION:  **GASTRO**  INTESTINAL  DESCRIPTION: GASTROINTESTINAL//  **&lt;RET&gt;**  WEIGHT: 6//  Select MAJOR RAD/NUC MED AMIS CODES DESCRIPTION:  **&lt;RET&gt;** | Enter the code you want to edit. |

Supervisor Menu ...

**Utility Files Maintenance Menu ...**

### ☞Nuclear Medicine Setup Menu

**(Radiopharmaceutical) Number Enter/Edit**

**Route of Administration Enter/Edit**

**Site of Administration Enter/Edit**

**Vendor/Source (Radiopharmaceutical) Enter/Edit**

Overview:

This menu contains the options to build and manage the Nuclear Medicine radiopharmaceutical lot numbers, routes and sites of administration, and vendor source.

A number of Routes of Administration and Sites of Administration were exported with the software. Print the contents of their respective files (Route of Administration #71.6 and Site of Administration #71.7) using the options Route of Administration List and Site of Administration List before you attempt to add data. You may edit the names of the routes and sites, but you may not delete them.

Add sites (Site of Administration Enter/Edit) before Routes of Administration since the sites must be in place so that you can select them during route edits and associate them with routes. Likewise, vendors/sources must be in place before editing lots.

#### ☞Lot (Radiopharmaceutical) Number Enter/Edit

**[RA NM EDIT ]**

This option allows you to enter lot numbers for the radiopharmaceuticals used at your facility. Before entering new lots, you may need to first use the Vendor/Source (Radiopharmaceutical) Enter/Edit option to enter sources for use with this option.

| Prompt/User Response                                                                                                                                                                                          | Discussion                                                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Lot (Radiopharmaceutical) Number Enter/Edit  Select RADIOPHARMACEUTICAL  NUMBER/ID:  **048**                                                                                                                  | You can enter a new  number or ID here.                                                                                |
| Are you adding '048' as a new RADIOPHARMACEUTICAL LOT (the 26TH)?  **y**  (Yes)  RADIOPHARMACEUTICAL  SOURCE:  UNIVERSITY LABS  NUMBER/ID: 048//  **&lt;RET&gt;**  SOURCE: UNIVERSITY LABS//  **&lt;RET&gt;** | Select a source from the list that you built using the option Vendor/Source (Radiopharmaceutical) Enter/Edit.          |
| EXPIRATION DATE:  KIT #:  **&lt;RET&gt;**                                                                                                                                                                     | When a lot is no longer being used, enter an expiration date.  Enter a kit number if it applies to this lot.           |
| RADIOPHARM:  **SULFUR COLLOID**  TC-99M  DX201  Select RADIOPHARMACEUTICAL  NUMBER/ID:                                                                                                                        | Entering one or two "?" here will give you a list of active radiopharmaceuticals that you can associate with this lot. |

#### ☞Route of Administration Enter/Edit

**[]**

Use this option to build and manage a list of routes of administration and their corresponding sites of administration. You may want to use the Site of Administration Enter/Edit option first to define sites that will be associated with the routes you enter here.

**Note** : If no sites are associated with a particular route and status tracking parameters require/ask a route/site, the status parameter is ignored.

Route of Administration Enter/Edit

Select ROUTE OF ADMINISTRATION NAME: **INTRAVENOUS**

Are you adding 'INTRAVENOUS' as a new ROUTE OF ADMINISTRATION (the 19TH)? **Y** (Yes)

NAME: INTRAVENOUS// **&lt;RET&gt;**

Select SYNONYMS: **&lt;RET&gt;**

Current parameters for entry of sites for this route :

PROMPT FOR FREE TEXT SITE? =

VALID SITES OF ADMINISTRATION =

-- NOTE --

If 'PROMPT FOR FREE TEXT SITE?' is 'Y',

then users will not be given a selection

of predefined 'VALID SITES'

Select one of the following:

P  PROMPT FOR FREE TEXT SITE?

V  VALID SITES OF ADMINISTRATION

Edit which field: **V** ALID SITES OF ADMINISTRATION

Select VALID SITES OF ADMINISTRATION: **??**

Valid sites of drug administration for this route of administration

should be entered here. During case edits, users will be restricted to

selecting only sites entered here when this route of administration is

used.

Choose from:

CERVICAL SUBARACHNOID SPACE

ENDOTRACHEAL TUBE

GALL BLADDER

LEFT ANTECUBITAL FOSSA

. . .

Select VALID SITES OF ADMINISTRATION: LEFT JUGULAR

Select VALID SITES OF ADMINISTRATION: RIGHT JUGULAR

Select VALID SITES OF ADMINISTRATION: (etc.) **&lt;RET&gt;**

#### ☞Site of Administration Enter/Edit

**[RA NM EDIT SITE]**

Use this option to build a list of sites for the administration of radiopharmaceuticals. You can also enter a synonym for the site, so users have a choice of terms for selection. This list is used by the option Route of Administration Enter/Edit in the Valid Sites of Administration field.

| Prompt/User Response                                                                                                                                                                                                                                                           | **Discussion**   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| Site of Administration Enter/Edit  Select SITE OF ADMINISTRATION NAME:  **LEFT JUGULAR**  Are you adding 'LEFT JUGULAR' as a new SITE OF ADMINISTRATION (the 36TH)?  **Y**  (Yes)  NAME: LEFT JUGULAR//  Select SYNONYM:  **&lt;RET&gt;**  Select SITE OF ADMINISTRATION NAME: |                  |

#### ☞Vendor/Source (Radiopharmaceutical) Enter/Edit

**[RA NM EDIT SOURCE]**

Use this option to build a list of vendors, pharmacies or other sources for the radiopharmaceuticals used in your facility. This list is used by the  (Radiopharmaceutical) Number Enter/Edit option in the Radiopharmaceutical Lot Source field.

| Prompt/User Response                                                                                                                                                                                                                                                                                                           | Discussion   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| Vendor/Source (Radiopharmaceutical) Enter/Edit  Select RADIOPHARMACEUTICAL SOURCE VENDOR/PHARMACY:  **CHEMICALS INC.**  Are you adding 'CHEMICALS INC.' as  a new RADIOPHARMACEUTICAL SOURCE (the 11TH)?  **Y**  (Yes)  VENDOR/PHARMACY: CHEMICALS INC.//  **&lt;RET&gt;**  Select RADIOPHARMACEUTICAL SOURCE VENDOR/PHARMACY: |              |

**Supervisor Menu ...**

**Utility Files Maintenance Menu ...**

### Order Entry Procedure Display Menu ...

**Common Procedure Enter/Edit**

**Create OE/RR Protocol from Common Procedure**

**Display Common Procedure List**

Overview:

This menu contains the options to manage the common procedure display used in either OE/RR or in the Request an Exam option.

#### Common Procedure Enter/Edit

**[RA COMMON PROCEDURE]**

The most frequently ordered procedures can be set up in a Common Procedure Display to make ordering a Rad/Nuc Med procedure easier for the ordering clinician. You may enter as many procedures into the Common Procedure file as you wish, however, you may only use sequence numbers from 1 to 40 per Imaging Type. Only procedures with sequence numbers are displayed, therefore the maximum number of common procedures that can be displayed is 40 per Imaging Type.

This menu option may be used to add and/or remove (inactivate) procedures from the display (Common Procedure List) users see when entering requests. Procedures should not be deleted from this file, just inactivated. Active common procedure entries require a sequence number to tell the system the order in which they should be displayed on the screen. When you enter "YES" to the Inactivate from List prompt field it will automatically remove the procedure's sequence number. The system will automatically resequence active common procedures upon exit from the option.

If you want to assign a new entry a particular sequence number on the Common Procedure List, you should reassign the sequence numbers of all procedures on the list that follow the insertion point and assign the selected sequence number to the new entry. For example, if you have 10 entries on your Common Procedure List and you wish to enter a procedure as sequence number 8, you could reassign sequence numbers 8, 9 and 10 to numbers 11, 12, and 13 and then assign the new entry to number 8. This manual realignment of sequence numbers should all be done before exiting the option, because this tells the system the order in which the procedures should be displayed.

The system will automatically resequence the numbers to remove gaps in numbering upon exit. For example, say you exit the option leaving 10 active common procedures for Vascular Lab Imaging Type and they happen to have sequence number 3, 5, 6, 7, 10, 20, 35, 37, 38, 40. The automatic re-sequencing will replace their order numbers with 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 respectively.

The Radiology/Nuclear Medicine Request an Exam option will display these procedures in the order in which you sequence them. Version 2.5 of OE/RR will also display an identically numbered common procedure list. Version 3.0 of OE/RR will display the same common procedures; however, they will always appear in alphabetical order. To accommodate this, you may wish to number the procedures so that their names are alphabetized if the same clinicians will be using both OE/RR version 3.0 and the Request and Exam option.

If you are running version 2.5 of OE/RR, you may also establish a procedure as an orderable item in the OE/RR package through this option. You will be prompted for the name the procedure can be ordered by through OE/RR, Imaging Location where the procedure will be performed, category of exam, requested date of exam, mode of transport of the patient, urgency of the exam, whether isolation procedures are required and any modifiers associated with the procedure. You **must** enter a Name and Imaging Location or the procedure will not be accepted as an orderable item. After establishing a procedure as an orderable item in OE/RR, you should utilize the Create OE/RR Protocol from Common Procedure option to actually set up the orderable item (protocol) in the OE/RR package. You may not edit a protocol once it has been created through the Create OE/RR Protocol from Common Procedure option. If you are running a version of OE/RR higher than 2.5, none of the above applies, and you will not see any prompts for creating protocols. Creating quick order protocols for OE/RR version 3.0 and beyond will be done through OE/RR and will no longer be possible through Radiology/Nuclear Medicine.

There is no limit to the number of entries that may be added to the Rad/Nuc Med Common Procedure file #71.3. Any procedure entered into this file (with or without a sequence number) can be converted into an OE/RR protocol, thus making the procedure an orderable item selectable by any user requesting an exam through OE/RR. When you establish an orderable item through this option and then create a protocol through the Create OE/RR Protocol from Common Procedure option, you are building a quick order. This means you may select the protocol through OE/RR and have certain information already associated with the procedure.

It is suggested that before you add a new entry to the Common Procedure List, you use the option Display Common Procedure List to obtain a list of procedures and their sequence numbers. That will help you determine where you want the new entry placed and what sequence numbers can be used.

| Prompt/User Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Discussion                                                                                                                                                                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Common Procedure Enter/Edit  ☞Select one of the following Imaging Types:  GENERAL RADIOLOGY  NUCLEAR MEDICINE  ULTRASOUND  CT SCAN  CARDIOLOGY STUDIES (NUC MED)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                           |
| Select IMAGING TYPE:  **NM**  NUCLEAR MEDICINE  Select RAD/NUC MED COMMON PROCEDURE:  **??**  PARATHYROID SCAN (3)  GASTROESOPHAGEAL REFLUX STUDY (2)  GI BLOOD LOSS-ACUTE GI BLEED (5)  WHOLE BLOOD VOLUME (4)  LYMPHATIC/LYMPH NODE IMAGING (no sequence number)  HEPATOBILIARY SCAN (HIDA SCAN) (6)  ESOPHAGEAL MOTILITY (7)  CARDIAC SHUNT DETECTION (8)  CEREBRAL BLOOD FLOW (1)  You may enter a new RAD/NUC MED COMMON PROCEDURE  if you wish. Enter a procedure name. Only  active procedures may be selected.  Answer with RAD/NUC MED PROCEDURES NAME  Do you want the entire RAD/NUC MED PROCEDURES  List?  **NO**  Select RAD/NUC MED COMMON PROCEDURE:  BONE SCAN  (NM Broad )  Are you adding 'BONE SCAN' as  a new RAD/NUC MED COMMON PROCEDURE (the 19TH)?  Y  (Yes)  PROCEDURE: BONE SCAN//  **&lt;RET&gt;** | Note that the procedures already entered as Common Procedures appear with their sequence number to the right. If there is no sequence number, that procedure has been "inactivated" from the common procedure list.       |
| INACTIVATE FROM LIST:  **&lt;RET&gt;**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | When adding a new procedure, simply bypass this prompt. To remove a procedure from the Common Procedure list, enter YES at this prompt.  To reactivate a procedure, enter an @ at this prompt to remove the YES response. |

| Prompt/User Response                                                                                                                                                                                                                                                                                                                                             | Discussion                                                                                                                                                                                                                                                                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SEQUENCE NUMBER: 12//  &lt;RET&gt;                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                 |
| Do you wish to establish this procedure as a quick order item in OE/RR? No//  **YES**                                                                                                                                                                                                                                                                            | Let's make this an orderable protocol in OE/RR. all prompts below this are for the purpose of defining enough data to establish a quick order protocol. If you answer NO to this prompt, none of the prompts below will appear. (This prompt and the ones below will not appear if your site has installed a version of OE/RR higher than 2.5.) |
| NAME OF ORDERABLE ITEM:  BONE SCAN                                                                                                                                                                                                                                                                                                                               | This is the text that will appear to the user ordering the exam.                                                                                                                                                                                                                                                                                |
| Select MODIFIERS:  **&lt;RET&gt;**  IMAGING LOCATION:  **?**  Enter the Imaging Location for this procedure.  The Imaging Type of the procedure and the Imaging Type of the location must be the same.  Answer with IMAGING LOCATIONS TYPE OF IMAGING  Choose from:  NUC MED LOC (NUCLEAR MEDICINE-449)  NUC  (NUCLEAR MEDICINE-639)  IMAGING LOCATION:  **NUC** | There are no specific modifiers that go with this exam so we can bypass this prompt.  The exam request will be printed at the location entered here.                                                                                                                                                                                            |
| CATEGORY OF EXAM:  **?**  If an entry is not made for this field, the  category of 'Inpatient' will  automatically be entered for each request  generated from the protocol that  is built for this procedure.  Choose from:  I INPATIENT  O OUTPATIENT  C CONTRACT  S SHARING  E EMPLOYEE  R RESEARCH  CATEGORY OF EXAM:  **&lt;RET&gt;**                       | In this example, the default of Inpatient is what we want, so we strike the <RET> key to bypass this prompt.                                                                                                                                                                                                                                    |
| REQUESTED DATE:  **?**  If an entry is not made in this field, the date  of today (TODAY) will automatically be  entered for each request generated from the  protocol that is built for this procedure.  Choose from:  TODAY TODAY  TODAY+1 TOMORROW  REQUESTED DATE:  **&lt;RET&gt;**                                                                          | The default of Today is fine so we strike the <RET> key to bypass this prompt.                                                                                                                                                                                                                                                                  |
| MODE OF TRANSPORT:  **?**  If an entry is not made in this field, the mode  of transport of 'ambulatory' will  automatically be entered for each request  generated from the protocol that  is built for this procedure.  Choose from:  a AMBULATORY  p PORTABLE  s STRETCHER  w WHEEL CHAIR  MODE OF TRANSPORT:  **&lt;RET&gt;**                                | Ambulatory is acceptable, so we can bypass this prompt.                                                                                                                                                                                                                                                                                         |
| ISOLATION PROCEDURES:  **?**  If an entry is not made in this field, a value  of 'NO' (isolation procedures not required)  will automatically be entered for each request  generated from the protocol that is built for  this procedure.  Choose from:  y YES  n NO  ISOLATION PROCEDURES:  **&lt;RET&gt;**                                                     | Isolation is not required.                                                                                                                                                                                                                                                                                                                      |
| REQUEST URGENCY:  **?**  If an entry is not made in this field, a request  urgency of 'ROUTINE' will automatically  be entered for each request generated from the  protocol that is built for this procedure.  Choose from:  1 STAT  2 URGENT  9 ROUTINE  REQUEST URGENCY:  **&lt;RET&gt;**                                                                     | Routine is acceptable.                                                                                                                                                                                                                                                                                                                          |
| Select RAD/NUC MED COMMON PROCEDURE:  **&lt;RET&gt;**                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                 |

Create OE/RR Protocol from Common Procedure

**[RA CREATE OE/RR PROTOCOL]**

**Note: This option is functional only if OE/RR Version 2.5 is installed. If a higher version of OE/RR is installed, this option is not needed and will display a message to that effect.**

This option is used to create orderable items (protocols) in the Order Entry/Results Reporting (OE/RR) package Version 2.5 based upon entries in the Rad/Nuc Med Common Procedures file. When you choose the option, the entire list of procedures in the Rad/Nuc Med Common Procedure file is presented for your selection as shown below. Press the &lt;RET&gt; key until your choice comes up. Then select the number of that choice. We added Bone Scan to the file in the previous chapter. Now a protocol will be created for it.

| Prompt/User Response                        | Discussion   |
|---------------------------------------------|--------------|
| Create OE/RR Protocol from Common Procedure |              |

Create an OE/RR Protocol from a Radiology/Nuclear Medicine

Common Procedure

1 ACUTE GI BLOOD LOSS IMAGING

2 ANGIO CAROTID CEREBRAL UNILAT S&amp;I

3 ANGIO CERVICOCEREBRAL CATH CP

4 ARTHROGRAM KNEE CP

5 BONE AGE

6 BRAIN IMAGING COMPLETE STUDY WITH VASCULAR FLOW, PLANAR

7 CHEST STEREO PA

8 ECHOCARDIOGRAM M-MODE COMPLETE

9 MAMMOGRAM BILAT

10 RADIONUCLIDE THERAPY, HYPERTHYROIDISM

11 ABDOMEN 1 VIEW

12 ARTHROGRAM ANKLE S&amp;I

13 ANGIO CORONARY BILAT INJ S&amp;I

14 ECHOGRAM ABDOMEN COMPLETE

15 RADIONUCLIDE THERAPY, THYROID SUPPRESSION

Type '^' to STOP, or

Choose from 1-15: **&lt;RET&gt;**

16 BRAIN IMAGING, PLANAR ONLY

17 BONE SCAN

18 ACROMIOCLAVICULAR J BILAT

Type '^' to STOP, or

Choose from 1-18: **17**

Processing the BONE SCAN procedure.

Located in the RA (RADIOLOGY/NUCLEAR MEDICINE) namespace.

RA584 BONE SCAN PROTOCOL Created

#### Display Common Procedure List

**[RA DISPLAY COMMON PROCEDURES]**

This option allows you to look at what the common procedure list will look like to the user, when using the request a procedure either through OE/RR version 2.5 or the Radiology/Nuclear Medicine option. OE/RR version 3.0 will also display the same procedures, but they will be in alphabetical order.

| Prompt/User Response                                      | Discussion   |
|-----------------------------------------------------------|--------------|
| Display Common Procedure List  **RAD**  GENERAL RADIOLOGY |              |

Select one of the following Imaging Types:

GENERAL RADIOLOGY

NUCLEAR MEDICINE

ULTRASOUND

CT SCAN

CARDIOLOGY STUDIES (NUC MED)

Select IMAGING TYPE: **GENERAL** RADIOLOGY

COMMON RADIOLOGY/NUCLEAR MEDICINE PROCEDURES (GENERAL RADIOLOGY)

----------------------------------------------------------------

1) ACUTE GI BLOOD LOSS IMAGING  7) ECHOGRAM ABDOMEN COMPLETE

2) ANGIO CAROTID CEREBRAL UNILAT S&amp; 8) RADIONUCLIDE THERAPY, THYROID SU

3) ANGIO CORONARY BILAT INJ S&amp;I  9) ABDOMEN 1 VIEW

4) ARTHROGRAM ANKLE S&amp;I   10) MAMMOGRAM BILAT

5) BRAIN IMAGING, PLANAR ONLY  11) BONE AGE

6) CHEST STEREO PA   12) BONE SCAN

Press RETURN to continue... **&lt;RET&gt;**

**Supervisor Menu ...**

**Utility Files Maintenance Menu ...**

### Procedure Edit Menu ...

**Activate/Inactivate Standard Procedures**

**Cost of Procedure Enter/Edit**

**Procedure Enter/Edit**

**Procedure Message Entry/Edit**

**Procedure Modifier Entry**

Overview:

This menu contains the options to define and manage data for procedures.


#### Activate/Inactivate Standard Procedures

[RA PROCEDURE ACTIVATE]

This option is used to batch activate or inactivate the new Oracle/Cerner standard procedures. The user can choose to activate/inactivate a set of individual procedures, procedures by modality, or ALL of the new standard procedures. The RAD/NUC MED PROCEDURE field STANDARD PROCEDURE? is used to identify these. Radiology patch RA*5.0*226 deployed the new procedures with an inactive date so the sites may control how they are activated.

| Prompt/User Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Discussion                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Activate/Inactivate Standard Procedures  Select one of the following:  1  Activate  2  Inactivate  Activate or Inactivate the new standard  procedures?:  **1**  Activate  Select one of the following:  1  Choose Individual Procedures  2  By Modality  3  All  How do you want to activate the new Oracle/Cerner standard procedures?:  **1**  Choose Individual Procedures  Select Procedures(s):  **NM LIVER***  **Output:**  NM LIVER IMAGING SPECT Activated!  NM LIVER IMAGING SPECT W/ VASCULAR FLOW Activated!  NM LIVER IMAGING STATIC Activated!  NM LIVER IMAGING W/ VASCULAR FLOW Activated! | In this example we will activate a selection of individual standard procedures.  Select a RAD/NUC MED PROCEDURES NAME from the displayed list.  To deselect a NAME type a minus sign (-) in front of it, e.g., -NAME.  Use an asterisk (*) to do a wildcard selection, e.g.,  enter NAME* to select all entries that begin with the text 'NAME'. Wildcard selection is case sensitive.  All procedures matching the user’s selection will be displayed as they are activated or inactivated |

**Cost of Procedure Enter/Edit**

**[RA PROCOSTEDIT]**

This function allows you to apply a cost to procedures. Unit cost and Total cost appear on the Procedure/CPT Statistics Report [RA CPTSTATS].

You are asked for an imaging type, the procedure you want to edit, and the cost. Only procedures matching the selected imaging type(s) can have their cost edited. Select procedures by entering either the CPT code for the procedure or the procedure name.

Cost of Procedure Enter/Edit

Select Imaging Type: All// **&lt;ret&gt;**

Another one (Select/De-Select): **&lt;ret&gt;**

Select RAD/NUC MED PROCEDURES NAME: **71020** CHEST X-RAY CHEST 2 VIEWS PA&amp;LAT (RAD Detailed) CPT:71020

COST OF PROCEDURE: **99.98**

#### Procedure Enter/Edit

**[RA PROCEDURE]**

This function allows you to enter new procedures into the system and to edit existing procedures. Entries in this file are used as the allowable selections for users at any Procedure prompt. This function must be used to associate the CPT (Current Procedural Terminology) codes for applicable descendent procedures with contrast media. This prompt appears as part of the Request an Exam, Register an Exam, Add Exam to Last Visit, Case No. Exam Edit, and the Exam Status Tracking options.

1. RAD/NUC MED PROCEDURES NAME - You can only edit the name of the procedure if the procedure was added by your site; if the procedure was distributed by the package, editing the name field is not allowed. Entries are related to Imaging Types. If the same procedure is done by two different locations of differing Imaging Types then you need to enter them with slightly different names but with the same CPT and AMIS codes:

US - Carotid Doppler

VAS - Carotid Doppler

**Note** : In order to comply with the CPRS procedure naming convention, the name must not contain a semicolon (;).

1. TYPE OF IMAGING - This field is used to associate a particular Imaging Type to a procedure. Each procedure can only be associated with one Imaging Type. You may enter a new procedure with a slightly different name to make it show up for a second Imaging Type.

Example: You want Carotid Doppler for Ultrasound and for Vascular Lab. One procedure can be called Carotid Doppler and assigned to the Ultrasound Imaging Type and the other VAS - Carotid Doppler with the Vascular Lab Imaging Type.

If you have activated a new Imaging Type and are changing the Imaging Type of procedures to match the new Imaging Type, you will also have to deactivate these procedures from the Common Procedure list (if they are common procedures). They can later be put on a separate new common procedure list under the new Imaging Type. Refer to Common Procedure Enter/Edit for more information.

1. TYPE OF PROCEDURE - There are four types of procedures:

**Detailed** - Procedure is associated with an AMIS code and must have a CPT code assigned to it.

**Series** - Procedure is associated with more than one AMIS code and must have a CPT code assigned to it. It is recommended that the Type of Procedure field be set to Series for all procedures with more than one AMIS code. In addition to being reported under each AMIS code, the procedures with multiple AMIS codes are also tallied in the "Series of AMIS Codes" line item of the AMIS Report. Setting these procedures as a Series type serves as a reminder to users. The AMIS Report counts each Series procedure the same as the Detailed procedure in the body of the report, but an additional line tallies the Series procedures by themselves. The Bilateral, Operating Room, and Portable modifiers are not allowed for Series procedures as that would cause the AMIS Report to be incorrect.

**Broad** - Procedure is mainly used by the receptionist, clerk, or ordering clinician when scheduling a patient for an exam. It is used when s/he is not exactly sure which Detailed or Series procedure will be performed. However, before the exam can be considered Complete, the procedure should be changed to a Detailed or Series in order to ensure adequate workload credit to your facility. Broad procedures are not associated with a CPT or AMIS codes. These prompts will not be seen if the user selects Broad as the procedure type. If no CPT code is entered for a Detailed or Series procedure, the procedure type is automatically changed to Broad.

If the Division parameter requiring a Detailed or Series procedure upon initial exam registration is set to YES, then the ordering party will not be able to select a Broad procedure.

**Parent** - Procedure is used for ordering purposes only. It must have descendants (other procedures of Detailed or Series type) that are actually registered. Parent procedures are used to simplify the ordering process when a group of related procedures must be done. (See Parent/Descendent Exam and Printsets) Similar to Broad procedures, they act as temporary placeholders. When a parent order is requested, the system automatically finds all the descendants and checks for the use of contrast media. The parent procedure is never actually registered. If one or more of the registered descendent procedures associated with the parent procedure uses contrast media, the parent procedure will be flagged as being associated with contrast media. When creating a Parent procedure, make the parent name slightly different than any of its descendants so the system will accept it as a new procedure. **Remember, when creating a Parent, no CPT code is entered therefore, it will not be registered** . All descendants must be either Detailed or Series Type with a CPT code.

Example:

Parent: 	Arthrogram of the Shoulder (or Arthrogram -

Shoulder)

Descendants:	73040

23350

1. ☞	MODALITY - This is a new field that only appears when you are defining either Detailed or Series type procedures. Each procedure can have more than one modality. The modality data is used by the Imaging package to produce a modality work list that will help to correctly identify a patient. If you are not running the Imaging package at your site, you may bypass this field.
2. ☞SINGLE REPORT - This is a new field that only appears when you define a procedure as a Parent procedure. If this field is left unanswered, then the reporting of the procedure's descendants will be put into separate reports, as in the previous version. If this field is answered YES, then the reporting of the procedure's descendants will be combined into one report, where the case records for these descendants will have the same data for report text, impression, pre-verifier, verifier, staff (primary and secondary), residents (primary and secondary), diagnoses, and all other report-related fields.
3. HEALTH SUMMARY WITH REQUEST **-** This field points to the Health Summary Type file. When a procedure is requested, this field is checked for an associated Health Summary Type and, if one exists, it is printed along with the request. You can select an appropriate Health Summary Type here. If necessary, you may need to check with your clinical coordinator for help in setting up useful health summary formats.
4. SYNONYM **-** One or more synonyms may be associated with a procedure. At any Procedure prompt, a synonym can be entered to select a procedure if you have predefined the synonym here.
5. ☞PROMPT FOR MEDS  - This is a new field. It only appears for procedures that are Detailed or Series. If this field is set to YES, case edits will prompt for medications administered for this procedure. To make Status Tracking prompt for medications administered, this field must be set to YES **and** the Examination Status parameter "Ask Medications &amp; Dosages" must be set to YES for one or more statuses of the procedure's Imaging Type.
6. ☞DEFAULT MEDICATION **-** This is a new field. It only appears for procedures that are Detailed or Series. Use this field to enter any medications when they are usually used for the procedure. Radiopharmaceuticals may not be entered in this field. Medications, if defined here, are entered automatically into the patient exam record by the system during registration.

☞	DEFAULT MED DOSE  will only appear if you enter a Default Medication. If a default dose is entered, it will be automatically entered on the patient's exam record at the time the procedure is registered. Acceptable format: 99999.999 unit\_of\_measure. Unit\_of\_measure may be between 1-30 characters in length. Example: 2.5 mg

1. ☞SUPPRESS RADIOPHARM PROMPT - This is a new prompt that only applies to Detailed or Series procedures with an Imaging Type that uses radiopharmaceuticals (i.e., nuclear medicine or cardiology studies). If the exam status setup for the affected Imaging Types specifies that radiopharmaceutical data should be asked and/or required to progress to various statuses, this field can be used to over-ride that requirement for a particular procedure.

Available categories are defined as follows:

0 or blank - 	Ask for Radiopharmaceutical if and when exam status parameters specify (this is the default).

- 	Suppress the Radiopharmaceutical prompt. Never ask or require Radiopharmaceutical even if exam status parameters specify that a Radiopharmaceutical should be entered. Even if default Radiopharmaceuticals are entered for the procedure they will not be automatically entered on the exam record by the system when the case is registered.

1. ☞PROMPT FOR RADIOPHARM RX - This is a new prompt that only applies to Detailed or Series procedures with an Imaging Type that uses radiopharmaceuticals (nuclear medicine or cardiology studies). It controls whether case edit and status tracking options prompt for prescribing physician, prescribed radiopharmaceutical dose, and witness to the dose administration. If you answer YES to this field, prescriber and witness prompts will appear for any radiopharmaceuticals entered for this procedure. (For example, a witness is necessary for a Total Body Iodine procedure so you would answer YES at this field for that procedure.) If this field is left blank, prescriber and witness prompts will not appear. If this field is set to YES, Status Tracking will prompt during each edit session until the data is entered; case edits will always prompt, even if the data has already been entered.
2. ☞DEFAULT RADIOPHARMACEUTICAL - This is a new prompt that only applies to Detailed or Series procedures with an Imaging Type that uses radiopharmaceuticals (nuclear medicine or cardiology studies). It will be automatically entered as a radiopharmaceutical on patients' nuclear medicine exam records during registration. This information can be changed, if necessary, during case edit. If nothing is entered in this field, no radiopharmaceuticals will be automatically entered during registration for this procedure.

**Note** : The radiopharmaceutical is the only data item that is actually automatically entered on the patient exam record during registration. No dosage amounts or routes of administration are entered automatically; however, they will appear as default responses.

☞	LOW ADULT DOSE (in mCi) - This is the lowest usual adult dosage commonly associated with this radiopharmaceutical when administered for this procedure. The system will display this value and the high adult dose when asking for the actual dosage during case editing. If the dosage entered for an exam falls outside of the usual high/low range, the person editing the case will see a warning message. If you do not want a warning to appear no matter how low the dosage entered, do not enter a low range dosage here.

☞	HIGH ADULT DOSE (in mCi) - This is the highest usual adult dosage commonly associated with this radiopharmaceutical when administered for this procedure. The system will display this value and the low adult dose when asking for the actual dosage during case editing. If the dosage entered for an exam falls outside of the usual high/low range, the person editing the case will see a warning message. **This is a mandatory data item.**

☞	USUAL DOSE (in mCi) - This is the usual dosage (in mCi) associated with this radiopharmaceutical. It will appear as an informational item on the screen just before the user is prompted for the actual Dose. If nothing is entered in this field, no usual dose information will be displayed. The usual dose you enter here must fall within the Low Adult Dose and High Adult Dose described above.

☞	DFLT ROUTE OF ADMINISTRATION - This is the route of administration commonly associated with this radiopharmaceutical for this procedure. It will appear as the default response when the route of administration is asked during case editing. If nothing is entered in this field, no default route of administration will be displayed.

☞	DEFAULT SITE OF ADMINISTRATION - This is the bodily site for administering the radiopharmaceutical for the procedure being defined. The system will use this for the default response during case editing. If nothing is entered here, there will be no default response to the Site of Administration question during case editing.

☞	DEFAULT FORM  This is the form of this Radiopharmaceutical when used in this procedure. If entered, it will be used as the default answer to the "Form" prompt during case edits.

1. AMIS CODE -This field contains the valid AMIS code(s) from the Major AMIS Codes file associated with this exam procedure. There may be more than one AMIS code associated with each procedure. If the procedure type is Detailed, there will be one AMIS code. If the procedure type is Series, there will be more than one AMIS code. Broad and Parent types of procedures have no AMIS code.

AMIS WEIGHT MULTIPLIER **-** You are not likely to change an AMIS Weight Multiplier unless VA HEADQUARTERS rules the change. However, if you add a new procedure, you must determine from VA HEADQUARTERS guidelines what should be entered at this prompt.

This field contains a number (0-99) to indicate to the various workload report routines how many times to multiply the weighted work units associated with the AMIS code. The weight for each AMIS code is stored in the Major Rad/Nuc Med AMIS Code file.

Most multipliers will be 1. However, there are some that are greater than 1. For example, the procedure called Upper GI + Small Bowel has the AMIS code 9-Gastrointestinal which has a weight of 6 work units. But, the AMIS multiplier is 2. Therefore on the workload reports, the site will get credit for 12 weighted work units each time it is performed.

Radiology Central Office has directed that the weighted work unit for Ultrasound procedures involving multiple organs in the same visit can be counted only once if the organs are located close to each other (i.e. Liver and Gallbladder).

BILATERAL - This field contains a YES to indicate that this is a bilateral procedure or a NO if it is not a bilateral procedure. If it contains a YES, then the system multiplies the AMIS weight by 2. No harm is done by indicating the Multiplier as 2 and Bilateral as YES. The system will only use 2 as the multiplier, not (2*2).

1. CPT CODE - Editing the CPT Code for existing procedures is no longer allowed because of possible contrast media associations. If the CPT Code of the procedure in the RAD/NUC MED PROCEDURE (#71) file must be changed, the procedure should be INACTIVATED and a new procedure, with the correct CPT Code, should be created.
2. DEFAULT CPT MODIFIERS(PROC) - Default CPT Modifier(s) entered for this procedure will be automatically entered into the exam record during exam registration.
3. STAFF REVIEW REQUIRED - If the procedure requires an interpreting staff physician's review of the resident's report, even though the division parameter is set to allow residents to verify reports, enter a YES at this prompt. (Refer to Personnel Classification and Division Parameter Set-up for other factors that control whether residents can verify reports.) This field does not appear with Broad or Parent procedures.
4. REQUIRED FLASH CARD PRINTER - This field contains the name (1-20 characters) of the location where the flash cards for this procedure are to be printed. Normally, the flash cards are printed at the reception desk, however, for particular procedures the flash cards may be printed at a different location such as where the exam is to be performed. This field does not appear with Parent procedures since Parent procedures are not registered.

**Note:** The exam labels will print out on the flash card printer associated with the imaging location parameter.

1. REQUIRED FLASH CARD FORMAT - If a flash card format has been defined, you can associate a specific format with this procedure. Otherwise the format defined for the location will be used. This field does not appear with Parent procedures, since flash cards are only printed during registration and parent procedures are never registered.
2. FILM TYPE  - This field contains a default value of the type of film from the Film Sizes file that is usually needed for this procedure. During the exam registration process, the system checks this field for a film type. If film type exists, then it is automatically entered into the Film Type field of the exam record. The entry in the exam record can be edited. Only procedures that are performed a relatively high number of times, such as Chest PA&amp;LAT, should have data entered for this field. This field does not appear with Parent procedures since parent procedures are never registered.
3. NORMAL AMOUNT NEEDED FOR EXAM - This field contains the default value (a number from 1 through 10) of the normal amount of film usually required for this procedure. During the exam registration process, the system checks this field for data. If data is present, then the information in this field is stuffed into the "Number Used" field of the exam record. The technologist is allowed to modify this data after performing the exam. Only procedures that are performed a relatively high number of times should have data entered for this field. The procedure CHEST PA&amp;LAT is a good example.
4. RAD/NM PHYS APPROVAL REQUIRED - If YES is entered at this prompt, when a request for this procedure is entered, the request will require the name of the approving physician. This name will print on the request form.
5. MESSAGE - You can select a message from the Rad/Nuc Med Procedure Message file for this procedure that will automatically appear at the time of the request and will be printed on the request form.
6. DESCENDENTS - This field only appears with Parent procedures. Enter any Detailed or Series procedures that make up the set. Remember that the Parent procedure is a placeholder for ordering and will not be registered, so all procedures to be registered must be entered as descendants.
7. **Note** : To add a second procedure that is the same as one already entered, enter either the CPT code or the procedure name in quotes as shown here:

Select DESCENDENTS: FOOT 2 VIEWS// ?

Answer with DESCENDENTS

Choose from:

ANKLE 2 VIEWS

FOOT 2 VIEWS

TOE(S) 2 OR MORE VIEWS

You may enter a new DESCENDENTS, if you wish

Enter a procedure name which is related to the parent procedure.

Select only active detailed or series procedures of the same

imaging type as the parent.

Answer with RAD/NUC MED PROCEDURES NAME, or CPT CODE, or SYNONYM

Do you want the entire RAD/NUC MED PROCEDURES List? n (No)

Select DESCENDENTS: FOOT 2 VIEWS// **"FOOT 2 VIEWS"**

1. ☞EDUCATIONAL DESCRIPTION - This is a new field used to describe the procedure and give information about its purpose in confirming or eliminating various diagnoses. It may be used for educational purposes by clinicians who are trying to familiarize themselves with imaging procedures that are available. If you enter an educational description, you are also asked if you want to "Display Educational Description When Ordered". Entering YES at that field displays the description along with any Procedure Message during the ordering process.

**Note** : If you are using the Screen Editor to add an Educational Description and you want a list of items, to keep the list from wrapping add a space (&lt;sp&gt;) before each item as shown in the following example:

When ordering this procedure, we recommend the following steps be taken:

&lt;sp&gt;1) Do this first.

&lt;sp&gt;2) Next do this.

&lt;sp&gt;3) Etc.

1. ☞DISPLAY EDUCATIONAL DESCRIPTION WHEN ORDERED - This field determines whether or not the Educational Description of a procedure should be displayed along with the procedure message (if any) at the time the procedure is ordered. Enter YES to display the description with the procedure message, NO to not display the description.
2. INACTIVATION DATE  - If the procedure has an inactivation date prior to the current date, then the procedure is not a valid choice and will not appear on the list of active procedures when displayed to the user. Entering an inactivation date makes the procedure invisible to users so it cannot be selected. This should only be done if the procedure becomes obsolete or should not be ordered or performed at your site. You can enter a future date. This is useful if for example a CPT becomes inactive on January 1 and you want to enter it earlier than that date. Inactivation takes effect at **midnight** of the date you enter.

Here is an example of a Nuclear Medicine, Detailed procedure. The prompts for radiopharmaceuticals only appear when the procedure has an Imaging Type of Nuclear Medicine or Cardiology Studies:

Prompt/ **User Response**

Select RAD/NUC MED PROCEDURES NAME: **ACUTE GI BLOOD LOSS IMAGING** ( *NM Detailed* ) CPT:78278

NAME: ACUTE GI BLOOD LOSS IMAGING Replace **&lt;RET&gt;**

TYPE OF IMAGING: NUCLEAR MEDICINE// **&lt;RET&gt;**

TYPE OF PROCEDURE: DETAILED// **&lt;RET&gt;**

Select MODALITY: **&lt;RET&gt;**

HEALTH SUMMARY WITH REQUEST: INPATIENT// **&lt;RET&gt;**

Select SYNONYM: INPT// **&lt;RET&gt;**

☞PROMPT FOR MEDS: YES// **&lt;RET&gt;**

☞Select DEFAULT MEDICATION: LIDOCAINE 0.5% W/EPI INJ MDV// **&lt;RET&gt;**

DEFAULT MEDICATION: LIDOCAINE 0.5% W/EPI INJ MDV// **&lt;RET&gt;**

☞DEFAULT MED DOSE: **&lt;RET&gt;**

Reminder --

Selection of 'Suppress' for 'SUPPRESS RADIOPHARM PROMPT' will result in

the deletion of all default radiopharmaceutical information for this

procedure.

☞SUPPRESS RADIOPHARM PROMPT: Always// **&lt;RET&gt;**

☞PROMPT FOR RADIOPHARM RX: YES// **&lt;RET&gt;**

☞Select DEFAULT RADIOPHARMACEUTICAL: SULFUR COLLOID TC-99M// PERCHLORACAP 250MG

CAPS  DX201

...OK? Yes// **&lt;RET&gt;** (Yes)

DEFAULT RADIOPHARMACEUTICAL: PERCHLORACAP 250MG CAPS

// **&lt;RET&gt;**

LOW ADULT DOSE (in mCi): 2// **&lt;RET&gt;**

HIGH ADULT DOSE (in mCi): 5// **&lt;RET&gt;**

Input a 'Usual Dose' value within the range of: 2-5

USUAL DOSE (in mCi): 3// **&lt;RET&gt;**

DFLT ROUTE OF ADMINISTRATION: ORAL// **&lt;RET&gt;**

DEFAULT SITE OF ADMINISTRATION: MOUTH// **&lt;RET&gt;**

DEFAULT FORM: Solid (Other)// **&lt;RET&gt;**

Select DEFAULT RADIOPHARMACEUTICAL: **&lt;RET&gt;**

Select AMIS CODE: NUCLEAR MEDICINE// **&lt;RET&gt;**

AMIS CODE: NUCLEAR MEDICINE// **&lt;RET&gt;**

AMIS WEIGHT MULTIPLIER: 1// **&lt;RET&gt;**

Select AMIS CODE: **&lt;RET&gt;**

CPT CODE: 78278// **(no editing) &lt;&lt;&lt;&lt;&lt; NO EDITING ALLOWED**

STAFF REVIEW REQUIRED: NO// **&lt;RET&gt;**

RAD/NM PHYS APPROVAL REQUIRED: NO// **&lt;RET&gt;**

REQUIRED FLASH CARD PRINTER: **&lt;RET&gt;**

REQUIRED FLASH CARD FORMAT: ER FORMAT// **&lt;RET&gt;**

Select FILM TYPE: 11X14// **&lt;RET&gt;**

FILM TYPE: 11X14// **&lt;RET&gt;**

NORMAL AMOUNT NEEDED FOR EXAM: 1// **&lt;RET&gt;**

Select FILM TYPE: **&lt;RET&gt;**

Select MESSAGE:  SMITH BEFORE ORDERING THIS PROCEDURE// **&lt;RET&gt;**

☞EDUCATIONAL DESCRIPTION:

This test is designed to LOCATE the site of KNOWN GI bleeding, NOT to

determine whether there IS GI bleeding.

Edit? NO// **&lt;RET&gt;**

☞DISPLAY EDUCATIONAL DESCRIPTION WHEN ORDERED: YES// **&lt;RET&gt;**

INACTIVATION DATE: **&lt;RET&gt;**

Here is an example of a Parent procedure entry:

Prompt/ **User Response**

Select RAD/NUC MED PROCEDURES NAME: **AORTAL FEMORAL RUNOFF**

Are you adding 'AORTAL FEMORAL RUNOFF' as

a new RAD/NUC MED PROCEDURES (the 737TH)? **Y** (Yes)

RAD/NUC MED PROCEDURES TYPE OF PROCEDURE: **P** PARENT

NAME: AORTAL FEMORAL RUNOFF Replace &lt;RET&gt;

TYPE OF IMAGING: **GEN** ERAL RADIOLOGY

TYPE OF PROCEDURE: PARENT// **&lt;RET&gt;**

☞SINGLE REPORT: **YES**

HEALTH SUMMARY WITH REQUEST: **&lt;RET&gt;**

Select SYNONYM: **&lt;RET&gt;**

RAD/NUC MED PHYS APPROVAL REQUIRED: NO// **&lt;RET&gt;**

Select MESSAGE: **&lt;RET&gt;**

Select DESCENDENTS: **75625** CONTRAST X-RAY EXAM OF AORTA AORTO ABD TRANS L W/SERIAL FILMS S&amp;I (Detailed) CPT:75625

Are you adding 'AORTO ABD TRANS L W/SERIAL FILMS S&amp;I' as

a new DESCENDENTS (the 1ST for this RAD/NUC MED PROCEDURES)? **Y** (Yes)

Select DESCENDENTS: **36200** PLACE CATHETER IN AORTA AORTA, CATHETER (FEMORAL OR AXILLARY APPROACH) (Detailed) CPT:36200

Are you adding 'AORTA, CATHETER (FEMORAL OR AXILLARY APPROACH)' as

a new DESCENDENTS (the 2ND for this RAD/NUC MED PROCEDURES)? **Y** (Yes)

Select DESCENDENTS: **75716** ARTERY X-RAYS, ARMS/LEGS ANGIO EXTREMITY BILAT S&amp;I (Detailed) CPT:75716

Are you adding 'ANGIO EXTREMITY BILAT S&amp;I' as

a new DESCENDENTS (the 3RD for this RAD/NUC MED PROCEDURES)? **Y** (Yes)

Select DESCENDENTS: **&lt;RET&gt;**

☞EDUCATIONAL DESCRIPTION:

No existing text

Edit? NO// **&lt;RET&gt;**

INACTIVATION DATE: **&lt;RET&gt;**

Here is an example of editing an existing CT SCAN, Detailed, procedure. In this edit session, we are adding contrast media to the procedure.

Select RAD/NUC MED PROCEDURES NAME: CT ABDOMEN W/CONT (CT Detailed) CPT:74160

TYPE OF IMAGING: CT SCAN// **&lt;RET&gt;**

TYPE OF PROCEDURE: DETAILED// **&lt;RET&gt;**

CONTRAST MEDIA USED: No// Yes

Select CONTRAST MEDIA: ?

You may enter a new CONTRAST MEDIA, if you wish

Enter the contrast agent(s) associated with this procedure.

Choose from:

I Ionic Iodinated

N Non-ionic Iodinated

L Gadolinium

C Cholecystographic

G Gastrografin

B Barium

M unspecified contrast media

Select CONTRAST MEDIA: N (N Non-ionic Iodinated)

Are you adding 'Non-ionic Iodinated' as

a new CONTRAST MEDIA (the 1ST for this RAD/NUC MED PROCEDURES)? No// Y

(Yes)

Select CONTRAST MEDIA: **&lt;RET&gt;**

Select MODALITY: CT// **&lt;RET&gt;**

HEALTH SUMMARY WITH REQUEST: **&lt;RET&gt;**

Select SYNONYM: **&lt;RET&gt;**

PROMPT FOR MEDS: **&lt;RET&gt;**

Select DEFAULT MEDICATION: **&lt;RET&gt;**

Select AMIS CODE: COMPUTED TOMOGRAPHY// **&lt;RET&gt;**

AMIS CODE: COMPUTED TOMOGRAPHY// **&lt;RET&gt;**

AMIS WEIGHT MULTIPLIER: 1// **&lt;RET&gt;**

BILATERAL?: **&lt;RET&gt;**

CT HEAD OR BODY?: BODY// **&lt;RET&gt;**

Select AMIS CODE: **&lt;RET&gt;**

CPT CODE// 74160 (no editing)    &lt;&lt;&lt;&lt;&lt; NO EDITING ALLOWED

Select DEFAULT CPT MODIFIERS(PROC): **&lt;RET&gt;**

STAFF REVIEW REQUIRED: NO// **&lt;RET&gt;**

RAD/NM PHYS APPROVAL REQUIRED: NO// **&lt;RET&gt;**

REQUIRED FLASH CARD PRINTER: **&lt;RET&gt;**

REQUIRED FLASH CARD FORMAT: **&lt;RET&gt;**

Select FILM TYPE: DRY LASER FILM// **&lt;RET&gt;**

FILM TYPE: DRY LASER FILM// **&lt;RET&gt;**

NORMAL AMOUNT NEEDED FOR EXAM: 1// **&lt;RET&gt;**

Select FILM TYPE: **&lt;RET&gt;**

Select MESSAGE:  SMITH BEFORE ORDERING THIS PROCEDURE

// **&lt;RET&gt;**

EDUCATIONAL DESCRIPTION: **&lt;RET&gt;**

No existing text

Edit? NO// **&lt;RET&gt;**

INACTIVATION DATE: **&lt;RET&gt;**

CT ABDOMEN W/CONT is a descendent procedure, updating parent(s)...

Updating parent: CT ABDOMEN

Updating parent: CT CHEST &amp; ABDOMEN &amp; PELVIS

Updating parent: CT ABDOMEN &amp; PELVIS

Updating parent: CT CHEST &amp; ABDOMEN

Select RAD/NUC MED PROCEDURES NAME:

#### Procedure Message Entry/Edit

**[RA PROCMSGEDIT]**

This option is used to enter, edit and delete messages related to procedures. These messages are used at the time of request to alert the requester of special requirements related to the procedure. The requirements may be other tests that need to be done before the procedure or special approval needed to request the procedure.

Messages entered through this option are associated with procedures in the Rad/Nuc Med Procedures file using the option Procedure Enter/Edit. Multiple messages can be associated with one procedure.

**Note: Procedure messages cannot be deleted from this file. Instead, use the Procedure Enter/Edit option to remove the message from the procedure.**

| Prompt/User Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Discussion                                                                                                                                                                                                                                                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Procedure Message Entry/Edit  Select RAD/NUC MED PROCEDURE MESSAGE TEXT:  **??**  Choose from:  Patient must be NPO after  before test  Patient must have RUQ pain, fever, elevated WBC  Patient must not have eaten within 3 hours  This test is not useful for assessing CHRONIC  cholecystitis!  This field contains messages concerning special  requirements when ordering a procedure.  One or more of these messages can be tied to a  procedure in the RAD/NUC MED PROCEDURES  file (#71).  Select RAD/NUC MED PROCEDURE MESSAGE TEXT:  **Make sure the patient has not eaten for 3 hours prior to the test to avoid a false positive result!**  Are you adding 'Make sure the patient has not eaten for 3 hours prior to the test to avoid a false positive result!' as a new RAD/NUC MED PROCEDURE MESSAGE (the 17TH)?  **Y**  (Yes)  TEXT: Make sure the patient has not eaten for 3 hours prior to the test to avoid a false positive result! Replace  **&lt;RET&gt;**  Select RAD/NUC MED PROCEDURE MESSAGE TEXT:  **&lt;RET&gt;** | In this example, we show you how to add a new message. It must be 3 to 240 characters in length.  **Do not begin the message with any special characters such as "*" or "#". Use letters or numbers only.**  **Note: It is strongly recommended that the 1st 30 characters of the message text be unique to facilitate selection of entries.** |

#### Procedure Modifier Entry

**[RA MODIFIER]**

This option allows the entry of new modifiers to the Procedure Modifier file (#71.2). Procedure modifiers are used to further describe the procedure. Frequently used modifiers include Right, Left, Bilateral, Portable, etc. This file provides the list of selections for the prompt "Select MODIFIERS" found in the exam edit options. An examination report will show any modifiers that have been entered for that examination.

You cannot delete a modifier. To make it inactive for an Imaging Type, type an at sign (@) at the prompt "Select TYPE OF IMAGING" for the Imaging Type you want.

**If all Imaging Types are deleted from the "TYPE OF IMAGING:" field for a modifier, users will not be able to select it for any exams.**

| Prompt/User Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Discussion                                                   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| Procedure Modifier Entry  Select Procedure Modifier:  **CORONAL**  Are you adding 'CORONAL' as a new PROCEDURE  MODIFIERS (the 11TH)?  **Y**  (Yes)                                                                                                                                                                                                                                                                                                                                                                         | Enter a modifier 2 - 30 characters in length.                |
| Select TYPE OF IMAGING:  **?**  Answer with TYPE OF IMAGING  You may enter a new TYPE OF IMAGING, if you wish  Enter the Imaging Type(s) for which this  modifier is valid.  Answer with IMAGING TYPE TYPE OF IMAGING, or ABBREVIATION  Choose from:  ANGIO/NEURO/INTERVENTIONAL  CARDIOLOGY STUDIES (NUC MED)  CT SCAN  GENERAL RADIOLOGY  MAGNETIC RESONANCE IMAGING  NUCLEAR MEDICINE  ULTRASOUND  VASCULAR LAB  MAMMOGRAPHY  Select TYPE OF IMAGING:  **GEN**  ERAL RADIOLOGY  Select TYPE OF IMAGING:  **&lt;RET&gt;** | Enter one or more Imaging Types that will use this modifier. |

| Prompt/User Response                                                                                                                                                                                                                                                        | Discussion                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AMIS CREDIT INDICATOR:  **?**  If this modifier receives extra AMIS credit,  enter the type of credit indicator it requires.  Choose from:  b BILATERAL  o OPERATING ROOM  p PORTABLE  AMIS CREDIT INDICATOR:  **&lt;RET&gt;**  Select Procedure Modifier:  **&lt;RET&gt;** | If this modifier would mean that the procedure is done bilaterally or in the operating room or with portable equipment, you should select the appropriate response here. For example, the modifier whose name is "Bilateral" should have "b" entered in this field. AMIS credit is doubled when a procedure or exam has a bilateral modifier. Operating room and portable exams are counted under both the exams AMIS category and the operating room or portable AMIS category. |


### Radiology Community Care Consult Entry/Edit

**[RA COMCARE]**

This menu is used to associate a Community Care Consult title with an Imaging Location. The consult title naming convention must match the standard depicted in patch RA*5.0*148:

COMMUNITY CARE-IMAGING &lt;TYPE OF IMAGING&gt;-AUTO

The Type of Imaging listed in the consult title must match the Type of Imaging for this Imaging Location it is being associated with.

The Community Care Consult title that is associated with this location will be used for imaging orders submitted to this location that are referred to community care via the option ‘Refer Selected Requests to COMMUNITY CARE Provider’ [RA ORDERREF].

| Prompt/User Response                                                                                                                                                                                                                   | Discussion                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| Radiology Community Care Consult Entry/Edit  Select IMAGING LOCATIONS:  **MRI (MAGNETIC RESONANCE IMAGING-500)**  Select COMMUNITY CARE REQUEST SERVICE:  **??**  Choose from:  COMMUNITY CARE-IMAGING MAGNETIC RESONANCE IMAGING-AUTO | Select Imaging Location to edit and then the Community Care Consult title to associate with it. |
| Select COMMUNITY CARE REQUEST SERVICE:  COMMUNITY CARE-IMAGING MAGNETIC RESONANCE IMAGING-AUTO                                                                                                                                         |                                                                                                 |

### Reports Distribution Edit

**[RA DISTEDIT]**

The distribution queue functionality of this package makes it possible to print results reports by ward, clinic, file room, etc. If a distribution queue is activated, at the time a report is verified, it will automatically be placed in the appropriate queue(s). This option allows you to edit specific report distribution queues. The types of distribution queues which can be edited are the following:

Clinic Reports

File Room

Medical Records

Other than Ward or Clinic

Requesting Physician

Ward Reports

Information which may be edited for the distribution queues include: a top of page message, the category of reports to be included in the queue, and the date after which the distribution queue should become inactivated.

| Prompt/User Response                                                                                                                                                                               | Discussion                         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| Reports Distribution Edit  Select REPORT DISTRIBUTION QUEUE NAME:  **??**  Choose from:  CLINIC REPORTS  FILE ROOM  MEDICAL RECORDS  OTHER THAN WARD OR CLINIC  REQUESTING PHYSICIAN  WARD REPORTS | Select the queue you want to edit. |
| Select REPORT DISTRIBUTION QUEUE NAME:  **FILE**  ROOM                                                                                                                                             |                                    |

TOP OF PAGE MESSAGE: ***** Radiology File Room Distribution *****

Replace **&lt;RET&gt;**

| Prompt/User Response                                                                                                                                                                                                                                                                                      | Discussion                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CATEGORY OF REPORTS: ALL REPORTS//  **??**  This field contains the categories available for  rad/nuc med reports.  Choices are : 'I' for inpatient, 'O' for  outpatient, 'N' for non ward or clinic, 'A'  for all reports.  Choose from:  I INPATIENT  O OUTPATIENT  N NON WARD OR CLINIC  A ALL REPORTS |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| CATEGORY OF REPORTS: ALL REPORTS//  **I**  INPATIENT                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| INACTIVATION DATE:  **T**  (AUG 29, 1994)  Select REPORT DISTRIBUTION QUEUE NAME:  **&lt;RET&gt;**                                                                                                                                                                                                        | As long as a queue is active, when results reports are verified, the Report Distribution file will be populated with the reports that belong in the active queues. For example, if the patient is an inpatient and his report is verified, it would be placed in the Ward Reports queue, the File Room queue, and the Medical Records queue if all three are active. As long as no inactivation date is entered here, the distribution queue is active.  **Note**  : If your facility is not using Distribution Queues, you should enter an Inactivation Date. This will avoid an accumulation of unwanted reports in the distribution queues. |

### Sharing Agreement/Contract Entry/Edit

**[RA SHARING]**

This function allows you to enter new sharing agreements/contracts into the system and edit existing ones.

A Sharing Agreement between two sites might be a situation where both facilities share the cost and maintenance of a particular piece of equipment. An example would be a mobile MRI which goes from site to site.

In Contract Agreement, one site is solely responsible for the equipment's cost and maintenance and is reimbursed for each examination performed on a patient from the other facility.

**Note: A patient whose category of exam is "Contract" or "Sharing", must have an entry from this file associated with the exam.**

When the category of an exam is "Contract" or "Sharing" agreement and an exam's Contract/Sharing Source field is entered, that exam will be included in the Sharing Agreement/Contract Report. Users must choose one of the agreements you enter here. To make the exam category "Contract" or "Sharing", the category of exam must be edited when the exam is ordered or during registration or case edit.

| Prompt/User Response                                                                                                                                                                                                                                                                                                                                                                                        | Discussion                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Sharing Agreement/Contract Entry/Edit  Select Agreement/Contract:  **??**  Choose from:  LFL CONTRACTORS  MEMORIAL  Select Agreement/Contract:  Are you adding '' as  a new CONTRACT/SHARING AGREEMENTS (the 3RD)?  **Y**  (Yes)  AGREEMENT NAME: //  **&lt;RET&gt;**  TYPE OF AGREEMENT:  **??**  Choose from:  S SHARING  C CONTRACT  TYPE OF AGREEMENT:  **S**  SHARING  INACTIVATION DATE:  &lt;RET&gt; | Check to make sure your entry is not already in the file by entering "??" at the first prompt. |

### Standard Reports Entry/Edit

**[RA STANDRPTS]**

This function allows you to enter new standard reports or to edit existing ones. These are generic reports (e.g., normal chest) that may be inserted into a procedure report. They are site specific, meaning the Imaging Services decide what reports are to be standard and what the text of the report should be. Any Division or Imaging Location may use any standard report. A standard report may be used as the entire report or may serve as a starting point for a report.

These standard reports are used by the transcriptionist in the Report Entry/Edit option of the Films Reporting Menu. If the transcriptionist selects a standard report for a specific exam, the report and impression fields will be filled in for that exam.

**The Transcriptionist will only be given the "Select 'Standard' Report to Copy" prompt during the Report Enter/Edit function, if the Division parameter Allow Standard Reports is set to "YES".**

Standard Report Strategies:

1. May be an **entire** report (e.g., "Normal Chest")
2. May include standard information which is in **every** report for a given procedure (e.g., how an UGI, B.E., or Nuc Med procedure was performed, what was injected, what images were obtained). Then specifics of the case will be added in the dictation. (If you are using this strategy, you do not necessarily have to put in a standard impression.)
3. Could have a standard report for each test for each attending, if you want, since each may have his/her own wording preference.

| Prompt/User Response                                                                                                                                | Discussion                                                                                                                                                                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Standard Reports Entry/Edit  Select STANDARD REPORTS:  **CHEST**  Are you adding 'NORMAL CHEST' as a new STANDARD  REPORTS (the 3RD)?  **Y**  (Yes) | Enter the name of a report 3 - 30 characters in length.                                                                                                                                    |
| STANDARD REPORTS REPORT NUMBER: 3//  **&lt;RET&gt;**  STANDARD REPORT:  CHEST//  **&lt;RET&gt;**                                                    | If you are using the VA FileMan screen editor, this is what will appear next. A line editor will be different. Please contact IRM if you have questions concerning screen or line editing. |

------------------------------------------------------------------------------

REPORT TEXT:

No existing text

Edit? NO// **Y** ES

==============================================================================[ WRAP ][ INSERT ]=&lt; REPORT TEXT &gt;[ &lt;PF1&gt;H=Help ]=======T=======T=======T=======T=======T=======T=======T=======T=======T====T **Chest exam is within normal limits.**

Saving text ...

------------------------------------------------------------------------------

IMPRESSION:

No existing text

Edit? NO// **Y** ES

==============================================================================[ WRAP ][ INSERT ]=&lt; IMPRESSION &gt;[ &lt;PF1&gt;H=Help ]=======T=======T=======T=======T=======T=======T=======T=======T=======T====T **Normal Chest X-Ray.**

Saving text ...

------------------------------------------------------------------------------

### Valid Imaging Stop Codes Edit

**[RA VALID STOP CODES]**

The Imaging Stop Codes file #71.5 must be updated every year around October 1 when VA Headquarters MAS issues revised stop codes (also known as DSS ID) and after your IRM installs the yearly MAS maintenance patch that updates the stop codes in the Clinic Stop file #40.7. You may add and delete entries from the Imaging Stop Codes file using this option.

Only stop codes entered here will be valid selections when editing the DSS ID field in the option Location Parameter Set-Up (Imaging Locations file).

| Prompt/User Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Discussion                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| Valid Imaging Stop Codes Edit  Select IMAGING STOP CODES VALID CODE:  **??**  Choose from:  NUCLEAR MEDICINE 109  PET 146  RADIONUCLIDE THERAPY 144  ULTRASOUND 115  VASCULAR LABORATORY 421  X-RAY 105  Only stop codes valid for imaging should be  entered in this file.  When a stop code becomes invalid, it should be  deleted from this file.  When a new stop code becomes valid for imaging  procedures, it should be added to this file.  Entries are used as a selection list when  editing procedure stop codes, and to screen the  principal clinic edit of Imaging Locations. |                                                                          |
| Choose from:  ADMITTING/SCREENING 102  ADULT DAY HEALTH CARE 190  ALCOHOL SCREENING 706  ALCOHOL TREATMENT-GROUP 556  ...  Select IMAGING STOP CODES VALID CODE:  **MAMMOGRAM**  703  Are you adding 'MAMMOGRAM' as a new IMAGING STOP CODES (the 5TH)?  **Y**  (Yes)  VALID CODE: MAMMOGRAM//  Select IMAGING STOP CODES VALID CODE:  **&lt;RET&gt;**                                                                                                                                                                                                                                      | Your list of choices contains the entries in the Clinic Stop file #40.7. |

VistaRad Category Entry/Edit

**[RA VISTARAD CATEGORY E]**

This option may be displayed under the 'Utility Files Maintenance Menu' ONLY IF the VistaRad component of the Imaging package is being used; otherwise, this option will not be displayed.

This option allows the user to update only the VISTARAD CATEGORY field that is in the EXAMINATION STATUS file (#72), without having to go through all the other fields that are seen in the 'Examination Status Entry/Edit' option.

In this option, you will be asked to select one Imaging type and an examination status, then you will be prompted to enter/edit the value of the VISTARAD CATEGORY. The option will continue to ask for another examination status, until you are done with that Imaging type.

Prompt/ **User Response**

VistaRad Category Entry/Edit

Select an Imaging Type: GENERAL RADIOLOGY

Select EXAMINATION STATUS: **EXAMINED** Imaging Type: GENERAL RADIOLOGY

Order: 3

...OK? Yes// **&lt;RET** &gt; (Yes)

VISTARAD CATEGORY: **?**

This field is only needed for sites that will be using VistaRad for soft-copy reading of images. This information is used by VistaRad software to prepare the various types of exam lists that are displayed on the VistaRad workstation, and to properly manage exam locking for the radiologists.

If this Examination Status is to be used for exams that will be read with VistaRad, then enter a value that corresponds to it from the following list. Note that not all status codes should be assigned a VistaRad Category value, but only those that apply.

All other Exam Status codes that may be defined in the Radiology Exam Status file should NOT be entered into this field.

Choose from:

W Waiting for Exam

## E Examined

D Dictated/Interpreted

T Transcribed

VISTARAD CATEGORY: **Exami** Examined

Select EXAMINATION STATUS: **^**

## 8 Maintenance Files Print Menu ...

Supervisor Menu ...

Maintenance Files Print Menu ...

**Complication Type List**

**Diagnostic Code List**

**Examination Status List**

**Film Sizes List**

**Label/Header/Footer Format List**

**Major AMIS Code List**

**Modifier List**

**Nuclear Medicine List Menu...**

**Procedure File Listings**

**Report Distribution Lists**

**Sharing Agreement/Contract List**

**Standard Reports Print**

**Rad/Nuc Med HL7 Voice Reporting Errors**

**Overview:**

This menu corresponds to the Utility Files Maintenance Menu. Each option allows you to print out a dated, hard copy of the data from the related file.

### Complication Type List

**[RA COMPRINT]**

This option provides a list of the complications from the Complication Types file #78.1 and whether or not each is considered a Contrast Medium Reaction.

For more information on complication types, refer to the Index and the chapter on Complication Type Entry/Edit.

| Prompt/User Response   | Discussion                                                                               |
|------------------------|------------------------------------------------------------------------------------------|
| Complication Type List |                                                                                          |
| DEVICE: (Printer Name) | Enter the name of a printer or press the <RET> key to display the output on your screen. |

Complication Types      PAGE 1

CONTRAST

MEDIUM

COMPLICATION   REACTION?

------------------------------------------------------------------------------

CONTRAST REACTION  YES

NAUSEA AND VOMITING  NO

NO COMPLICATION   NO

PREGNANCY   NO

SEVERE MORBIDITY  NO

### Diagnostic Code List

**[RA DIAGP]**

This option lists the contents of the Diagnostic Codes file #78.3.

For more information diagnostic codes, refer to the Index and the chapter on Diagnostic Code Enter/Edit.

| Prompt/User Response   | Discussion                                                                                                                           |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Diagnostic Code List   |                                                                                                                                      |
| DEVICE: (Printer Name) | Enter the name of a printer or press the <RET> key to display the output on your screen. See the next page for an example of a list. |

Diagnostic Codes      PAGE 1

PRINT

ON  GENERATE

ABNORMAL ABNORMAL

NUMBER DIAGNOSTIC CODE     REPORT ALERT?

------------------------------------------------------------------------------

1 NORMAL      NO

There were no problems for this exam!

------------------------------------------------------------------------------

2 MINOR ABNORMALITY    NO

There was a slight abnormality in this exam!

------------------------------------------------------------------------------

3 MAJOR ABNORMALITY, NO ATTN. NEEDED  NO

There was a major problem, but no attention was needed!

------------------------------------------------------------------------------

4 ABNORMALITY, ATTN. NEEDED   YES  YES

There was a major problem, and attention is necessary!

------------------------------------------------------------------------------

5 MAJOR ABNORMALITY, PHYSICIAN AWARE  NO

There is a major problem, and the doctor is aware of it!

------------------------------------------------------------------------------

6 UNDICTATED FILMS NOT RETURNED, 3 DAYS  NO

------------------------------------------------------------------------------

7 UNSATISFACTORY/INCOMPLETE EXAM   YES

This exam was either unsatisfactory or incomplete!

------------------------------------------------------------------------------

8 POSSIBLE MALIGNANCY, FOLLOW-UP NEEDED  YES

A possible malignancy was noted. Follow-up action should be taken.

------------------------------------------------------------------------------

9 POSSIBLE MALIGNANCY, FOLLOW-UP CRITICAL

Follow-up must be done, and documented

------------------------------------------------------------------------------

10 OVEREXPOSURE, MECH ERROR    YES  NO

OVEREXPOSURE DUE TO A MECHANICAL ERROR

------------------------------------------------------------------------------

**Note:** A blank in the "Print on Abnormal Report" column or the "Generate Abnormal Alert?" column is the same a "NO".

### Examination Status List

**[RA EXAMSTATUSP]**

This option lists the contents of the Examination Status file #72. It lists all contents of the Examination Status file whether or not the Imaging Types and statuses are activated. Our example shows only one of the Imaging Types that has been activated.

For more information on exam statuses, refer to the index and the chapter on Examination Status Entry/Edit.

| Prompt/User Response                                                                                                          | Discussion                                                                                                                                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Examination Status List                                                                                                       |                                                                                                                                                                                                                    |
| Select Imaging Type:  **NUC**  LEAR MEDICINE  Another one (Select/De-Select):  **&lt;RET&gt;**  Select Device: (Printer Name) | This report now allows printing by selected Imaging Types.  Enter the name of a printer or press the &lt;RET&gt; key to display the output on your screen.  See the next three pages for an example of the output. |

Examination Statuses   Page: 1

Run Date:

--------------------------------------------------------------------------------

Type Of Imaging: NUCLEAR MEDICINE

Status: ***CANCELLED***    Order: 0

Default Next Status:     User Key Needed:

Generate Examined HL7 Message:

Generate Exam Alert:     Allow Canceling?: YES

Appear On Status Tracking?: NO   Print Dosage Ticket: NO

ASK ON STATUS TRACKING:  REQUIRED FOR CHANGE TO THIS STATUS:

-----------------------  -----------------------------------

WORKLOAD REPORTS THAT USE THIS STATUS IN ITS COMPLETION:

--------------------------------------------------------

AMIS

Status: ***WAITING FOR EXAM***   Order: 1

Default Next Status: EXAMINED    User Key Needed:

Generate Examined HL7 Message:

Generate Exam Alert: NO    Allow Canceling?: YES

Appear On Status Tracking?: YES   Print Dosage Ticket: NO

ASK ON STATUS TRACKING:  REQUIRED FOR CHANGE TO THIS STATUS:

-----------------------  -----------------------------------

WORKLOAD REPORTS THAT USE THIS STATUS IN ITS COMPLETION:

--------------------------------------------------------

CLINIC

PTF BEDSECTION

SERVICE

SHARING/CONTRACT

WARD

FILM USAGE

TECHNOLOGIST

AMIS

DETAILED PROCEDURE

CAMERA/EQUIP/RM

PHYSICIAN

RESIDENT

STAFF

DELINQUENT STATUS

Examination Statuses   Page: 2

Run Date:

--------------------------------------------------------------------------------

Status: ***EXAMINED***    Order: 2

Default Next Status: TRANSCRIBED   User Key Needed:

Generate Examined HL7 Message: YES

Generate Exam Alert: NO    Allow Canceling?: NO

Appear On Status Tracking?: YES   Print Dosage Ticket: YES

ASK ON STATUS TRACKING:  REQUIRED FOR CHANGE TO THIS STATUS:

-----------------------  -----------------------------------

TECHNOLOGIST    TECHNOLOGIST

PROCEDURE    DETAILED PROCEDURE

FILM DATA    FILM ENTRY

CAMERA/EQUIP/RM    CAMERA/EQUIP/RM

MEDICATIONS &amp; DOSAGES   RADIOPHARMS/DOSAGES

MED ADM DT/TIME/PERSON

RADIOPHARMS AND DOSAGES

ADM DT/TIME/PERSON

LOT NO.

WORKLOAD REPORTS THAT USE THIS STATUS IN ITS COMPLETION:

--------------------------------------------------------

CLINIC

PTF BEDSECTION

SERVICE

SHARING/CONTRACT

WARD

FILM USAGE

TECHNOLOGIST

AMIS

DETAILED PROCEDURE

CAMERA/EQUIP/RM

PHYSICIAN

RESIDENT

STAFF

DELINQUENT STATUS

Status: ***TRANSCRIBED***    Order: 3

Default Next Status: COMPLETE    User Key Needed:

Generate Examined HL7 Message:

Generate Exam Alert: YES    Allow Canceling?: NO

Appear On Status Tracking?: NO   Print Dosage Ticket: NO

ASK ON STATUS TRACKING:  REQUIRED FOR CHANGE TO THIS STATUS:

-----------------------  -----------------------------------

TECHNOLOGIST    TECHNOLOGIST

INTERPRETING PHYS   REPORT ENTERED

PROCEDURE    IMPRESSION

FILM DATA    RESIDENT OR STAFF

DIAGNOSTIC CODE    DETAILED PROCEDURE

CAMERA/EQUIP/RM    FILM ENTRY

MEDICATIONS &amp; DOSAGES   CAMERA/EQUIP/RM

Examination Statuses   Page: 3

Run Date:

--------------------------------------------------------------------------------

MED ADM DT/TIME/PERSON   RADIOPHARMS/DOSAGES

RADIOPHARMS AND DOSAGES

ACTIVITY DRAWN

DRAWN DT/TIME/PERSON

ADM DT/TIME/PERSON

ROUTE/SITE OF ADM

LOT NO.

VOLUME/FORM

WORKLOAD REPORTS THAT USE THIS STATUS IN ITS COMPLETION:

--------------------------------------------------------

CLINIC

PTF BEDSECTION

SERVICE

SHARING/CONTRACT

WARD

FILM USAGE

TECHNOLOGIST

AMIS

DETAILED PROCEDURE

CAMERA/EQUIP/RM

PHYSICIAN

RESIDENT

STAFF

DELINQUENT STATUS

Status: ***COMPLETE***    Order: 9

Default Next Status:     User Key Needed:

Generate Examined HL7 Message:

Generate Exam Alert: NO    Allow Canceling?: NO

Appear On Status Tracking?: NO   Print Dosage Ticket: NO

ASK ON STATUS TRACKING:  REQUIRED FOR CHANGE TO THIS STATUS:

-----------------------  -----------------------------------

TECHNOLOGIST    TECHNOLOGIST

INTERPRETING PHYS   REPORT ENTERED

PROCEDURE    VERIFIED REPORT

FILM DATA    IMPRESSION

DIAGNOSTIC CODE    RESIDENT OR STAFF

CAMERA/EQUIP/RM    DETAILED PROCEDURE

MEDICATIONS &amp; DOSAGES   FILM ENTRY

MED ADM DT/TIME/PERSON   CAMERA/EQUIP/RM

RADIOPHARMS AND DOSAGES   RADIOPHARMS/DOSAGES

ACTIVITY DRAWN

DRAWN DT/TIME/PERSON

ADM DT/TIME/PERSON

ROUTE/SITE OF ADM

LOT NO.

VOLUME/FORM

Examination Statuses   Page: 4

Run Date:

--------------------------------------------------------------------------------

WORKLOAD REPORTS THAT USE THIS STATUS IN ITS COMPLETION:

--------------------------------------------------------

CLINIC

PTF BEDSECTION

SERVICE

SHARING/CONTRACT

WARD

FILM USAGE

TECHNOLOGIST

AMIS

DETAILED PROCEDURE

CAMERA/EQUIP/RM

PHYSICIAN

RESIDENT

STAFF

DELINQUENT STATUS

### Film Sizes List

**[RA FILMP]**

This option lists the contents of the Film Sizes file #78.4.

For more information on films, refer to the Index and the chapter on Film Type Entry/Edit.

| Prompt/User Response   | Discussion                                                                               |
|------------------------|------------------------------------------------------------------------------------------|
| Film Sizes List        |                                                                                          |
| DEVICE: (Printer Name) | Enter the name of a printer or press the <RET> key to display the output on your screen. |

Film Size Specifications     PAGE 1

F   W

l   a

C u   s

i o   t Analogous

n r   e Unwasted Film

Film  e o Inactivation Dt d Size

------------------------------------------------------------------------------

10X12  N

11X14  N

14X17  N

2X12  N

2X4  N JUL 5,1996

2X6  N

3X FILMS  N

CHROMATIC  N

CINE  Y

DENTAL  N

FLUORO ONLY N

NO FILMS  N

W-10X12  N   Y 10X12

W-11X14  N   Y 11X14

W-14X17  N   Y 14X17

W-2X12  N   Y 2X12

W-2X4  N JUL 5,1996 Y 2X4

W-2X6  N   Y 2X6

W-3X FILMS  N   Y 3X FILMS

W-CHROMATIC N   Y CHROMATIC

W-CINE  Y   Y CINE

W-DENTAL  N   Y DENTAL

W-FLUORO ONLY N   Y FLUORO ONLY

### Label/Header/Footer Format List

**[RA FLASHFORMP]**

This option prints the contents of the Lbl/Hdr/Ftr Formats file #78.2.

For more information on formats, refer to the Index and the chapter on Label/Header/Footer Formatter.

| Prompt/User Response            | Discussion                                                                               |
|---------------------------------|------------------------------------------------------------------------------------------|
| Label/Header/Footer Format List |                                                                                          |
| DEVICE: (Printer Name)          | Enter the name of a printer or press the <RET> key to display the output on your screen. |

Exam Label/Report Header/Report Footer/Flash Card Formats

PAGE 1

FIELD   ROW COL TITLE

TEXT

------------------------------------------------------------------------------

FORMAT NAME: ER FORMAT

NAME OF PATIENT  1 2 NAME :

SSN OF PATIENT   1 40 SSN :

DATE OF EXAM   2 1 EXAM DATE:

TECHNOLOGIST   2 40 TECH:

PROCEDURE   3 1 PROCEDURE:

FREE TEXT   5 2  COMMENTS :

VERIFYING RADIOLOGIST  10 2 INTERPRETER:

Exam Label/Report Header/Report Footer/Flash Card Formats

PAGE 2

FIELD   ROW COL TITLE

TEXT

------------------------------------------------------------------------------

FORMAT NAME: EXAM HEADER

FREE TEXT   1 1  EXAM REPORT

NAME OF PATIENT  1 15 PATIENT:

CURRENT DATE/TIME  1 50 DATE:

SSN OF PATIENT   2 1 SSN:

ATTENDING PHYSICIAN AT ORDER 2 40 Att at Order:

REQUESTING PHYSICIAN  3 1 REQ PHYS:

ATTENDING PHYSICIAN CURRENT 3 40 Att Current:

REQUEST ENTERED DATE/TIME 4 1

CURRENT PATIENT LOCATION 5 1

### Major AMIS Code List

**[RA MAJORAMISP]**

This option lists the contents of the Rad/Nuc Med AMIS Codes file #71.1.

For more information on AMIS codes, refer to the Index and the chapter on Major AMIS Code Entry/Edit.

| Prompt/User Response   | Discussion                                                                               |
|------------------------|------------------------------------------------------------------------------------------|
| Major AMIS Code List   |                                                                                          |
| DEVICE: (Printer Name) | Enter the name of a printer or press the <RET> key to display the output on your screen. |

Major AMIS Codes      PAGE 1

MAJOR

AMIS

CODE DESCRIPTION      WEIGHT

------------------------------------------------------------------------------

1 SKULL,INC.SINUS,MASTOID,JAW,ETC   3

2 CHEST-SINGLE VIEW     1

3 CHEST MULTIPLE VIEW     2

4 CARDIAC SERIES     3

5 ABDOMEN-KUB      2

6 OBSTRUCTIVE SERIES     3

7 SKELETAL-SPINE &amp; SACROILIAC    3

8 SKELETAL-BONE &amp; JOINTS    2

9 GASTROINTESTINAL     6

10 GENITOURINARY      6

11 CHOLECYSTOGRAM,ORAL     5

12 CHOLANGIOGRAM     10

13 LAMINOGRAM      5

14 BRONCHOGRAM      5

15 DIGITAL SUBTRACTION ANGIOGRAPHY   15

16 ANGIOGRAM,CATH- CEREBRAL    15

17 ANGIOGRAM,CATH- VISCERAL    20

18 ANGIOGRAM,CATH- PERIPHERAL    10

19 VENOGRAM      15

20 MYELOGRAM      10

21 COMPUTED TOMOGRAPHY     8

22 INTERVENTIONAL RADIOGRAPHY    20

23 ULTRASOUND,ECHOENCEPHALOGRAM    7

24 OTHER       5

25 EXAMS IN OPER.SUITE AT SURGERY   1

26 PORTABLE (BEDSIDE) EXAMINATIONS   1

27 NUCLEAR MEDICINE     1

### Modifier List

**[RA MODIFIERP]**

This option lists the contents of the Procedure Modifiers file #71.2.

For more information on modifiers, refer to the Index and the chapter on Procedure Modifier Entry.

| Prompt/User Response   | Discussion                                                                               |
|------------------------|------------------------------------------------------------------------------------------|
| Modifier List          |                                                                                          |
| DEVICE: (Printer Name) | Enter the name of a printer or press the <RET> key to display the output on your screen. |

Procedure Modifiers      PAGE 1

AMIS CREDIT

NAME    INDICATOR

-----------------------------------------------------------------------------

TYPE OF IMAGING: CARDIOLOGY STUDIES (NUC MED)

RIGHT

TYPE OF IMAGING: CT SCAN

RIGHT

TYPE OF IMAGING: GENERAL RADIOLOGY

BILATERAL EXAM   BILATERAL

PORTABLE EXAM   PORTABLE

OPERATING ROOM EXAM  OPERATING ROOM

LEFT

RIGHT

TEST    PORTABLE

TEST BILATERAL   BILATERAL

TEST OR    OPERATING ROOM

NEW ONE    OPERATING ROOM

OBLIQUE

**Supervisor Menu ...**

**Maintenance Files Print Menu ...**

### ☞Nuclear Medicine List Menu ...

**(Radiopharmaceutical) Number List**

**Route of Administration List**

**Site of Administration List**

**Vendor/Source (Radiopharmaceutical) List**

Use this menu in conjunction with the Nuclear Medicine Setup Menu.

#### ☞Lot (Radiopharmaceutical) Number List

**[RA NM PRINT ]**

This option prints a list of entries in the Radiopharmaceutical Lot file #71.9. The file is exported without data. It prints in 132 column format.

RADIOPHARMACEUTICAL LOT            PAGE 1

NUMBER/ID   RADIOPHARMACEUTICAL   KIT #  EXPIRATION DATE INACTIVE

---------------------------------------------------------------------------------------------------------------------------------

SOURCE: CHEMICALS INC.

5535         123598Y34512548

1234    TECHNETIUM Tc99m SESTAMIBI     JAN 20,1997

SOURCE: DUPONT

PER 1234   PERCHLORACAP 250MG CAPS   235

456    SULFUR COLLOID TC-99M   445  DEC 31,1997  YES

MAA 7136   TECHNETIUM Tc99m ALBUMIN AGGREGATED 1-5

7635    TECHNETIUM Tc99m MEDRONATE

MDP 6136P   TECHNETIUM Tc99m MEDRONATE  100     YES

MDP 6137P   TECHNETIUM Tc99m MEDRONATE  100

MDP 6137P   TECHNETIUM Tc99m MEDRONATE  101

DTPA 1234   TECHNETIUM Tc99m PENTETATE

SOURCE: SQUIBB

12345    TECHNETIUM Tc99m ALBUMIN AGGREGATED 333

MDP 6137P   TECHNETIUM Tc99m MEDRONATE  1

#### ☞Route of Administration List

**[]**

This option prints a list of entries in the Route of Administration file #71.6. A number of routes were exported with this version of the software.

ROUTE OF ADMINISTRATION     PAGE 1

NAME

SITES OF ADMIN     PROMPT

--------------------------------------------------------------------------------

CATHETER

URINARY BLADDER

G-TUBE    (synonym) GASTROSTOMY TUBE

(synonym) FEEDING TUBE

INHALATION   (synonym) VENTILATOR

MOUTH

TRACHEAL TUBE

NOSE

ENDOTRACHEAL TUBE

TRACHEOSTOMY

INTRA-ARTICULAR   (synonym) JOINT

(synonym) ARTICULAR

LEFT HIP

RIGHT HIP

LEFT KNEE

RIGHT KNEE

LEFT WRIST

RIGHT WRIST

LEFT SHOULDER

RIGHT SHOULDER     Yes

INTRADERMAL   (synonym) SKIN Yes

INTRALESIONAL     Yes

INTRAMUSCULAR   (synonym) IM

(synonym) I.M.

RIGHT FOREARM

LEFT FOREARM

LEFT SHOULDER

RIGHT SHOULDER

LEFT HIP

RIGHT HIP

INTRAOCULAR   (synonym) EYE

RIGHT EYE

LEFT EYE

INTRAPERITONEAL   (synonym) PERITONEAL

INTRAPLEURAL   (synonym) PLEURA

LEFT PLEURA

RIGHT PLEURA

INTRATHECAL   (synonym) SPINAL

LUMBAR SUBARACHNOID SPACE

CERVICAL SUBARACHNOID SPACE

#### ☞Site of Administration List

**[RA NM PRINT SITE]**

This option prints a list of entries in the Site of Administration file #71.7. A number of sites were exported with this version of the software.

SITE OF ADMINISTRATION      PAGE 1

NAME    (SYNONYM)

--------------------------------------------------------------------------------

CERVICAL SUBARACHNOID SPACE SUBARACHNOID SPACE

ENDOTRACHEAL TUBE  ETT

E.T.T.

GALLBLADDER   GB

G.B.

INTRAOCULAR   EYE

LEFT ANTECUBITAL FOSSA  L. ANTECUBITAL FOSSA

L ANTECUBITAL FOSSA

ANTECUBITAL FOSSA

LEFT ARM   L ARM

L. ARM

ARM

LEFT BUTTOCK   L BUTTOCK

L. BUTTOCK

BUTTOCK

LEFT DELTOID   L DELTOID

L. DELTOID

DELTOID

LEFT EYE   L. EYE

L EYE

EYE

LEFT FEMORAL   L. FEMORAL

L FEMORAL

FEMORAL

L. GROIN

L GROIN

GROIN

LEFT FOOT   L. FOOT

L FOOT

FOOT

LEFT FOREARM   L. FOREARM

L FOREARM

FOREARM

LEFT GLUTEUS   L GLUTEUS

L. GLUTEUS

GLUTEUS

LEFT HAND   L. HAND

L HAND

HAND

#### ☞Vendor/Source (Radiopharmaceutical) List

**[RA NM PRINT SOURCE]**

This option prints a list of entries in the Radiopharmaceutical Source file #71.8. The file is exported without data.

RADIOPHARMACEUTICAL SOURCE     PAGE 1

VENDOR/PHARMACY

----------------------------------------------------------------------------

CHEMICALS INC.

DUPONT

NATURAL CHEMICALS LABORATORY

PHARM-A-LOGIC (OFF SITE)

SQUIBB

UNIVERSITY LABS

UNIVERSITY NUCLEAR PHARMACY

**Supervisor Menu ...**

**Maintenance Files Print Menu ...**

### Procedure File Listings ...

☞ **HIST Display Rad/NM Procedure Contrast Media History**

**Active Procedure List (Long)**

**Active Procedure List (Short)**

**Alpha Listing of Active Procedures**

**Barcoded Procedure List**

**Display Rad/NM Procedure Contrast Media History**

**Inactive Procedure List (Long)**

**Invalid CPT/Stop Code List**

**List of Inactive Procedures (Short)**

☞ List of Procedures with Contrast

**Parent Procedure List**

**Procedure Message List**

**Series of Procedures List**

All of these reports access data in the Rad/Nuc Med Procedures file #71. Many of the following printouts are lengthy. "Q"ueuing these reports to be printed after hours should be considered.

#### ☞HIST Display Rad/NM Procedure Contrast Media History

**[RA CMAUDIT HISTORY]**

This option allows the user to look back at the prior contrast medium/media data associated with a Rad/Nuc Med Procedure.

1. From the Menu below, select the Supervisor Menu by typing ‘ **Supervisor Menu** ’ next to Select Rad/Nuc Med Total System Menu Option:

<!-- image -->

1. From the Supervisor Menu, select the Maintenance Files Print Menu by typing ‘ **Maintenance Files Print Menu** ’ next to Select Supervisor Menu Option:
<!-- image -->

1. From the Maintenance Files Print Menu, select Procedure File Listings by typing ‘ **Procedure File Listings** ’ next to Select Maintenance Files Print Menu Option:

<!-- image -->

1. From the Procedure file Listings Menu, select HIST Display Rad/NM Procedure Contrast Media History by typing ‘ **HIST Display Rad/NM Procedure Contrast Media History** ’ next to Select Procedure File Listings Option:

<!-- image -->

1. The Select Procedure Prompt displays. Enter a specific procedure, (for example, CT PELVIS W/CONT) or type ‘ALL’ to select all available procedures.

<!-- image -->

1. At the prompt: ‘ **Another one (Select/De-Select),** ’ enter another procedure or **&lt;RET&gt;** to continue.
2. At the appropriate prompt, enter the start and end dates for the search.
3. At the **DEVICE HOME//** prompt, enter the device on which to print the data or **&lt;RET&gt;** for the default (screen).

<!-- image -->

##### Sample Contrast Media Edit History by Procedure Report

Contrast Media Edit History By Procedure

Run Date: Dec 16, 2004 From: JAN 11,1919 To: NOV 3,2004  Page 1

Procedure    Date/Time Changed User

Contrast Media

--------------------------------------------------------------------------------

CT PELVIS W/CONT   Oct 27, 2004 1:28 pm VISTPATIENT,ONE

Gastrografin

CT PELVIS W/CONT   Oct 27, 2004 1:29 pm VISTPATIENT,TWO

**User deleted all contrast media data**

CT PELVIS W/CONT   Oct 27, 2004 2:39 pm VISTPATIENT,THREE

Gastrografin, Barium

CT PELVIS W/CONT   Oct 27, 2004 2:40 pm VISTPATIENT,FOUR

**User deleted all contrast media data**

CT PELVIS W/CONT   Oct 27, 2004 2:41 pm VISTPATIENT,FIVE

Gastrografin, Barium

CT PELVIS W/CONT   Oct 27, 2004 2:41 pm VISTPATIENT,SIX

Enter RETURN to continue or '^' to exit:

#### Active Procedure List (Long)

**[RA PROCLONG]**

This option prints a listing of all active procedures, their CPT and AMIS codes, AMIS weight multiplier, whether it is a bilateral procedure or a CT of the head or body, the type of procedure (broad, series, detailed or parent), flash card information, and whether review of the report and approval of the request is required. The report is sorted by AMIS category, then procedure name. It is a lengthy printout, so queuing the output should be considered.

If you assign one or more modalities to a procedure, the abbreviated and long name of each modality will print as the last item for the procedure.

**Note:** Contrast media associations will display, when appropriate.

| Prompt/User Response                                                                                                                                                                 | Discussion                                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| Active Procedure List (Long)  Select Imaging Type: All//  **NUC**  LEAR MEDICINE  Another one (Select/De-Select):  **&lt;RET&gt;**  This report requires a 132 column output device. | This report now allows printing by selected Imaging Types.                                              |
| DEVICE: (Printer Name or "Q")                                                                                                                                                        | If you enter "Q" instead of a printer name, you will also see prompts for a device and a time to print. |

Active Radiology/Nuclear Medicine Procedures (Long)     DEC 13,1996 08:43 PAGE 1

CPT             CT

CODE PROCEDURE / CPT MODIFIER   AMIS CODE  MULTIPLIER BILATERAL HEAD/BODY

-----------------------------------------------------------------------------------------------------------------------

78278 ACUTE GI BLOOD LOSS IMAGING 27 - NUCLEAR MEDICINE  1

Type of Procedure  : DETAILED

Required Flash Card Printer:

Required Flash Card Format : ER FORMAT

Cost of Procedure  :

Health Summary With Request: INPATIENT

Staff Review of Reports Req: NO

Rad Approval of Request Req: NO

Type of Imaging  : NUCLEAR MEDICINE

Suppress Radiopharm Prompt : Always

Prompt for Radiopharm RX : YES

Default Radiopharmaceutical: PERCHLORACAP 250MG CAPS

Usual Dose  : 3

Dflt Administration Route : ORAL

Dflt Administration Site : MOUTH

High Adult Dose  : 5

Low Adult Dose  : 2

Default Form  : Solid (Other)

Prompt for Medication? :

Descendents  :

Procedure Message  :

Educational Description : This test is designed to LOCATE the site of KNOWN GI

bleeding, NOT to determine whether there IS GI bleeding.

#### Active Procedure List (Short)

**[RA PROCSHORT]**

This is a list of active procedures, sorted by AMIS category and procedure name. Since the report can be lengthy, consider queuing the output. Only procedures with an AMIS code are included.

**Note:** Contrast media associations will display, when appropriate.

| Prompt/User Response                                                                                                                                                                   | Discussion                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Active Procedure List (Short)  Select Imaging Type: All//  **GEN**  ERAL RADIOLOGY  Another one (Select/De-Select):  **&lt;RET&gt;**  This report requires a 132 column output device. | This report now allows printing by selected Imaging Types.                                                                                                    |
| DEVICE: (Printer Name or "Q")                                                                                                                                                          | Enter the name of a printer that prints 132 columns.  If you enter "Q" instead of a printer name, you will also see prompts for a device and a time to print. |

Active Radiology/Nuclear Medicine Procedures (Short)  	  PAGE 1

CPT	BI-	IMG

CODE	PROCEDURE		AMIS CODE 	MULT 	LAT CT TYPE MODALITY

--------------------------------------------------------------------------------------

76062	BONE SURV COMP (INCL APPENDIC	1 -SKULL,INC.SINUS,MASTOID,JAW,ET	1 RAD

---------------------------------------------------------------------------------------------------------------

76061	BONE SURV LMTD (E.G. METASTATI	1 -SKULL,INC.SINUS,MASTOID,JAW,ET	1 RAD

--------------------------------------------------------------------------------------

#### Alpha Listing of Active Procedures

**[RA ALPHALIST]**

As you can see by the example below, this is a shorter, alphabetical listing of the active procedures. Since the report can be lengthy, consider queuing the output.

**Note:** Contrast media associations will display, when appropriate.

| Prompt/User Response                                                                                                                                                                        | Discussion                                                                                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Alpha Listing of Active Procedures  Select Imaging Type: All//  **GEN**  ERAL RADIOLOGY  Another one (Select/De-Select):  **&lt;RET&gt;**  This report requires a 132 column output device. | This report now allows printing by selected Imaging Types.                                                                                                    |
| DEVICE: (Printer Name or "Q")                                                                                                                                                               | Enter the name of a printer that prints 132 columns.  If you enter "Q" instead of a printer name, you will also see prompts for a device and a time to print. |

Alpha Listing of Active Procedures					  PAGE 1

CPT			BI- IMG

NAME	 TYPE MODALITY

--------------------------------------------------------------------------------------

ABDOMEN 1 VIEW	74000	5	ABDOMEN-KUB	1  RAD

--------------------------------------------------------------------------------------

ABDOMEN 2 VIEWS	74010	5	ABDOMEN-KUB	1  RAD

--------------------------------------------------------------------------------------

ABDOMEN FOR FETAL AGE 1 VIEW	74720	5	ABDOMEN-KUB	1  RAD

--------------------------------------------------------------------------------------

ABDOMEN FOR FETAL AGE MULT VIEWS	74725	5	ABDOMEN-KUB	1  RAD

--------------------------------------------------------------------------------------

ABDOMEN MIN 3 VIEWS+CHEST	74022	2	CHEST-SINGLE VIEW	1  RAD

6 	OBSTRUCTIVE SERIES	1

--------------------------------------------------------------------------------------

ACROMIOCLAVICULAR J BILAT	73050	8	SKELETAL-BONE &amp; JOINTS	1 YES RAD

#### ☞Barcoded Procedure List

**[RA BARPROCPRINT]**

If your site uses barcodes, use this option to print a list of barcoded CPTs and/or Procedures for a selected Imaging Type.

| Prompt/User Response    | Discussion                                                                                                       |
|-------------------------|------------------------------------------------------------------------------------------------------------------|
| Barcoded Procedure List | If you don't know the height of the barcode, you need to print a test version and count the lines as shown here: |

To print barcoded procedure list, you will need to know the height (in

vertical lines) of the barcode output on the printer to be used.

| Prompt/User Response                                                                                                                | Discussion                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Do you wish to print a sample barcode for the purpose of determining the height (in vertical lines) of the barcode? No//  **Y**  ES | If you don't know the height of the barcodes printed at your site, enter YES to obtain a sample barcode. You may need to contact IRM for the name of a printer for barcodes. |

Select a printer with barcode setup: (Enter the name of the device)

DO YOU WANT YOUR OUTPUT QUEUED? NO// **Y** (YES)

Requested Start Time: NOW// **&lt;RET&gt;** (DEC 11, 1996@12:46:25)

Request Queued, Task #: 35507

| Prompt/User Response                    | Discussion                                                                   |
|-----------------------------------------|------------------------------------------------------------------------------|
| Enter the height of the barcode:  **^** | Exit the option and get the printout of the test barcode. Here's an example: |

Barcode test print

Printed on: 	Page 1

----------------------------------------------------------------------------

LINE 1

LINE 2

LINE 3

LINE 4

LINE 5

LINE 6

LINE 7

LINE 8

LINE 9

LINE 10

TEST BARCODE PRINT BarcodeBarcodeBarcodeBarcodeBarcode

BarcodeBarcodeBarcodeBarcodeBarcode

BarcodeBarcodeBarcodeBarcodeBarcode

TEST BARCODE PRINT

LINE 1

LINE 2

LINE 3

LINE 4

LINE 5

LINE 6

LINE 7

LINE 8

LINE 9

LINE 10

Using the line counts printed above and below the example barcode to determine how many vertical lines the barcode occupies (include the procedure name line printed below the barcode), it appears to be 4 lines. Now you can print a list of barcodes used by your Imaging Type. Return to the option.

To print barcoded procedure list, you will need to know the height (in

vertical lines) of the barcode output on the printer to be used.

Do you wish to print a sample barcode for the purpose of determining the

height (in vertical lines) of the barcode? No// **&lt;RET&gt;**

Enter the height of the barcode: **4**

Select one of the following:

C  CPT barcode

P  Procedure barcode

B  Both barcodes

Which of the above would you like to print?: **B** oth

Select the data element you wish to sort by: **??**

Enter 'C' to sort by the CPT Code, or 'P' to sort by the

procedure.

Select one of the following:

C  CPT Code

P  Procedure

Select the data element you wish to sort by: **P** rocedure

Select Imaging Type: **GEN** ERAL RADIOLOGY

Another one (Select/De-Select): **&lt;RET&gt;**

Select Procedure: **ALL**

Another one (Select/De-Select): **&lt;RET&gt;**

Select a printer with barcode setup: (Enter the barcode printer name)

DO YOU WANT YOUR OUTPUT QUEUED? NO// **Y** (YES)

Requested Start Time: NOW// **&lt;RET&gt;** (DEC 11, 1996@12:47:58)

Request Queued, Task #: 35508

#### Inactive Procedure List (Long)

**[RA INACPRCLONG]**

This output is the same as that for Active Procedure List (Long) only these procedures have all been inactivated. Since the report can be lengthy, consider queuing the output.

If you assigned one or more modalities to a procedure, the abbreviated and long name of each modality will print as the last item for the procedure.

**Note:** Contrast media associations will display, when appropriate.

| Prompt/User Response                                                                                                                                                                    | Discussion                                                                                                                                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inactive Procedure List (long)  Select Imaging Type: All//  **GEN**  ERAL RADIOLOGY  Another one (Select/De-Select):  **&lt;RET&gt;**  This report requires a 132 column output device. | This report now allows printing by selected Imaging Types.                                                                                                    |
| DEVICE: (Printer Name or "Q")                                                                                                                                                           | Enter the name of a printer that prints 132 columns.  If you enter "Q" instead of a printer name, you will also see prompts for a device and a time to print. |

Inactive Radiology/Nuclear Medicine Procedures (Long)  	  PAGE 1

CODE	PROCEDURE / CPT MODIFIER	AMIS CODE 	MULTIPLIER	BILATERAL	HEAD/BODY

---------------------------------------------------------------------------------------------------------------

70350	CEPHALOGRAM ORTHODONTIC	1 -SKULL,INC.SINUS,MASTOID,JAW,ET	1

Type of Procedure  : DETAILED

Required Flash Card Printer:

Required Flash Card Format :

Cost of Procedure  :

Health Summary With Request:

Staff Review of Reports Req:

Rad Approval of Request Req:

Type of Imaging  : GENERAL RADIOLOGY

Prompt for Medications :

Descendents  :

Procedure Message  :

Educational Description :

--------------------------------------------------------------------------------------

#### Invalid CPT/Stop Code List

**[RA INVALID CPT/STOP]**

This option prints a list of Invalid CPT or Stop Codes. When generating the report, you can choose to include procedures that already have been marked Inactive (by entering an inactive date through the option Procedure Enter/Edit). It should be noted that the system sees procedure and CPTs as two separate entities. In other words, an active procedure can have a valid or invalid CPT associated with it. This report will print a warning if a Parent procedure has no Descendents, and if a detailed or series procedure has no AMIS code(s). It will also tell you if an Imaging Location setup doesn't meet criteria for workload crediting.

| Prompt/User Response       | Discussion   |
|----------------------------|--------------|
| Invalid CPT/Stop Code List |              |

This option prints a list of Radiology/Nuclear Medicine Procedures

with missing or invalid CPT's and DSS ID's, and Imaging Locations

pointing to Hospital Locations with inappropriate set-up parameters.

Broad, parent and inactive procedures are not required to have codes.

To be valid, DSS ID's must be in the Imaging Stop Codes file 71.5;

CPT's must be nationally active.

| Prompt/User Response                                                                                                                                      | Discussion                                                                                                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Include Inactive procedures? NO//  **&lt;RET&gt;**  Select Imaging Type: All//  **GEN**  ERAL RADIOLOGY  Another one (Select/De-Select):  **&lt;RET&gt;** | This report now allows printing by selected Imaging Types.                                                                                                                                           |
| DEVICE: (Printer Name or "Q")                                                                                                                             | Enter the name of a printer or press the &lt;RET&gt; key to bring the output to the screen.  If you enter "Q" instead of a printer name, you will also see prompts for a device and a time to print. |

RADIOLOGY/NUCLEAR MEDICINE INVALID CPT AND STOP CODES

Run Date: Sep 30, 1996@13:41:04     Page: 1

ABDOMEN FOR FETAL AGE 1 VIEW (Detailed, RAD)

Invalid CPT 74720

ABDOMEN FOR FETAL AGE MULT VIEWS (Detailed, RAD)

Invalid CPT 74725

ANGIO CERVICOCEREBRAL SELECT 1 VESSEL S&amp;I (Detailed, RAD)

No CPT entered.

No stop code(s) entered.

ANGIO CERVICOCEREBRAL SELECT 2 VESSEL S&amp;I (Type missing, Imaging Type missing)

Invalid CPT 75654

. . . Etc.

Imaging Type(s): GENERAL RADIOLOGY

TOTAL INVALID CPT CODES: 53

TOTAL MISSING CPT CODES: 1

TOTAL BROKEN POINTERS TO CPT CODES: 0

TOTAL PARENT PROCEDURES W/O DESCENDENTS: 0

TOTAL SERIES AND/OR DETAILED PROCEDURES W/O AMIS CODES: 3

**Note** : Remember to review the entries in the Imaging Stop Codes file #71.5

every year in October to make sure they agree with VA HQ rules. If the entries in file 71.5 are not accurate, this report will not be accurate.

Imaging Location: MAMMOGRAPHY

700-series noncredit Stop Code being used

#### List of Inactive Procedures (Short)

**[RA INACPRCSHORT]**

This output is the same as Inactive Procedure List (Long) excluding the Type of Procedure, Required Flash Card Printer, Required Flash Card Format, Staff Review of Reports Req, and Rad Approval of Request Req fields. Since the report can be lengthy, consider queuing the output.

**Note:** Contrast media associations will display, when appropriate.

| Prompt/User Response                                                                                                                                                                         | Discussion                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| List of Inactive Procedures (Short)  Select Imaging Type: All//  **GEN**  ERAL RADIOLOGY  Another one (Select/De-Select):  **&lt;RET&gt;**  This report requires a 132 column output device. | This report now allows printing by selected Imaging Types.                                                                                                    |
| DEVICE: (Printer Name or "Q")                                                                                                                                                                | Enter the name of a printer that prints 132 columns.  If you enter "Q" instead of a printer name, you will also see prompts for a device and a time to print. |

Inactive Radiology/Nuclear Medicine Procedures (Short)  	SEP 30,1996  PAGE 1

CPT						 BI- IMG

CODE	PROCEDURE		AMIS CODE 	MULT LAT CT TYPE MODALITY

--------------------------------------------------------------------------------------------------------------

70350	CEPHALOGRAM ORTHODONTIC	1 -SKULL,INC.SINUS,MASTOID,JAW,ET	1  RAD

--------------------------------------------------------------------------------------------------------------

70355	PANOREX	1 -SKULL,INC.SINUS,MASTOID,JAW,ET	1  RAD

#### ☞List of Procedures with Contrast

**[RA PROCMEDIA]**

This option allows the supervisor to generate a list of procedures that are associated with contrast media or medium. The option allows the user to select procedures by imaging type and whether the procedures are active or inactive.

The format of the report includes: Procedure Name, CPT Code, CPT Modifier(s), Procedure Type, Imaging Type, and Inactivation Date (if applicable).

1. From the Menu below, select the Supervisor Menu by typing ‘ **Supervisor Menu** ’ next to Select Rad/Nuc Med Total System Menu Option:

<!-- image -->

1. From the Supervisor Menu, select the Maintenance Files Print Menu by typing ‘Maintenance Files Print Menu’ next to Select Supervisor Menu Option:
<!-- image -->

1. From the Maintenance Files Print Menu, select Procedure File Listings by typing ‘Procedure File Listings’ next to Select Maintenance Files Print Menu Option:

<!-- image -->

1. From the Procedure file Listings Menu, select List of Procedures with Contrast by typing ‘List of Procedures with Contrast’ next to Select Procedure File Listings Option:

<!-- image -->

1. The Select Imaging Type Prompt displays. Enter a specific, Type of Imaging (see Imaging Types below) (for example, CT SCAN) or type ‘ALL’ to select all available imaging types.

**Imaging Types**

ANGIO/NEURO/INTERVENTIONAL

CARDIOLOGY STUDIES (NUC MED)

CT SCAN

GENERAL RADIOLOGY

MAGNETIC RESONANCE IMAGING

MAMMOGRAPHY

NUCLEAR MEDICINE

ULTRASOUND

VASCULAR LAB

<!-- image -->

1. At the prompt: ‘ **Another one (Select/De-Select),** ’ enter another procedure or **&lt;RET&gt;** to continue.
2. At the Select Procedure Status prompt, enter the desired status.
3. At the **DEVICE: HOME//** prompt, enter the device on which to print the data or **&lt;RET&gt;** for the default (screen).

Rad/Nuc Med Procedures with Contrast Media/Medium

Date: Dec 17, 2004       Page 1

CPT  Procedure

CPT Modifiers     Contrast Media

Procedure Type  Imaging Type  Inactivation Date

------------------------------------------------------------------------------------

74010  ABDOMEN 2 VIEWS

RESIDENT/TEACHING PHYS SERV   Barium

'OPT OUT' PHYS/PRACT EMERG OR URGENT SERVICE Cholecystographic

Ionic Iodinated

Non-ionic Iodinated

Gadolinium

Gastrografin

unspecified contrast media

DETAILED  GENERAL RADIOLOGY

Press RETURN to continue...

#### ☞Parent Procedure List

**[RA PARENT PROCEDURE LIST]**

The Parent Procedure List includes only parent type procedures and all fields applicable to parent procedures that are included on the Active Procedure long listing. It shows whether they are printsets (i.e., Single Report = Yes), whether a health summary is associated with it for printing with the request, whether Radiology/Nuclear Medicine approval is required to order it, its imaging type, all descendants and their CPT codes, whether the descendants use contrast media, and the educational description.

If you assigned one or more modalities to a procedure and the procedure is a descendant of the parent, then the abbreviated modality displays to the right of the descendant.

**Note:** Contrast media associations will display, when appropriate.

Parent Procedure List

Select Imaging Type: All// **&lt;RET&gt;**

Another one (Select/De-Select): **&lt;RET&gt;**

Select one of the following:

A  Active

I  Inactive

B  Both

Select Procedure Status: **A** Active

DEVICE: HOME// (Printer Name)

Active Parent Procedure List     PAGE 1

Parent Name

------------------------------------------------------------------------------

C&amp;P SPINAL SURVEY

Single Report : YES

Hlth Summary w Req. :

Rad Approval of Req.: NO

Type of Imaging : GENERAL RADIOLOGY

Descendants  : (72040) SPINE CERVICAL MIN 2 VIEWS

(72070) SPINE THORACIC 2 VIEWS

(72100) SPINE LUMBOSACRAL MIN 2 VIEWS

Procedure Message :

Educational Desc : THIS STUDY IS USED FOR C&amp;P WHEN A COMPLETE SPINE

IS NEEDED FOR RATINGS

------------------------------------------------------------------------------

BONE SCAN PARENT

Single Report : YES

Hlth Summary w Req. :

Rad Approval of Req.: NO

Type of Imaging : NUCLEAR MEDICINE

Descendants  : (78306) BONE IMAGING, WHOLE BODY

(78990) PROVISION OF DIAGNOSTIC RADIONUCLIDES

Procedure Message :

Educational Desc : Patient should drink 32 ounces of fluid after

Radionuclide injection and before imaging. Patient

is imaged 2 to 3 hours after the radionuclide

injection.

#### Procedure Message List

**[RA PROCMSGPRINT]**

This option prints the contents of the Rad/Nuc Med Procedure Message file #71.4. If there is a large number of entries in this file, consider queuing the output.

| Prompt/User Response          | Discussion                                                                                                                                                                                           |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Procedure Message List        |                                                                                                                                                                                                      |
| DEVICE: (Printer Name or "Q") | Enter the name of a printer or press the &lt;RET&gt; key to bring the output to the screen.  If you enter "Q" instead of a printer name, you will also see prompts for a device and a time to print. |

RAD/NUC MED PROCEDURE MESSAGE LIST    PAGE 1

TEXT

------------------------------------------------------------------------------

If the patient has not eaten for more than 36 hours or is on TPN, please inform Nuclear Medicine Service so CCK can be administered.

If the patient is on morphine, you cannot assess for CBD obstruction since it will cause spasm of the Sphincter of Oddi.

Make sure the patient has not eaten for 3 hours prior to the test, to avoid a false positive result!

Patient must be NPO after  the night before the test!

Patient must have RUQ pain, fever, elevated WBC

Patient must not have eaten within 3 hours of this test!

This test is useful in assessing for ACUTE cholecystitis only, not chronic cholecystitis! Try US for chronic cholecystitis.

#### Series of Procedures List

**[RA PROCSERIES]**

This list is the same as the Active Procedure List (Long) except it contains only Series procedures.

If you assigned one or more modalities to a procedure, then the abbreviated and long name of each modality will print as the last item for the procedure.

**Note:** Contrast media associations will display, when appropriate.

| Prompt/User Response                                                                                                                                                               | Discussion                                                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Series of Procedures List  Select Imaging Type: All//  **GEN**  ERAL RADIOLOGY  Another one (Select/De-Select):  **&lt;RET&gt;**  This report requires a 132 column output device. | This report now allows printing by selected Imaging Types.                                                                                                    |
| DEVICE: (Printer Name or "Q")                                                                                                                                                      | Enter the name of a printer that prints 132 columns.  If you enter "Q" instead of a printer name, you will also see prompts for a device and a time to print. |

Radiology/Nuclear Medicine Procedures (Series Only)  	  PAGE 1

CODE	PROCEDURE / CPT MODIFIERS		AMIS CODE 	MULTIPLIER	BILATERAL	HEAD/BODY

---------------------------------------------------------------------------------------------------------------

76062	BONE SURV COMP (INCL APPENDIC	1 -SKULL,INC.SINUS,MASTOID,JAW,ET	1

Type of Procedure  : SERIES

Required Flash Card Printer:

Required Flash Card Format :

Staff Review of Reports Req:

Rad Approval of Request Req:

Type of Imaging  : GENERAL RADIOLOGY

Descendents  :

Procedure Message  :

---------------------------------------------------------------------------------------------------------------76061	BONE SURV LMTD (E.G. METASTATI	1 -SKULL,INC.SINUS,MASTOID,JAW,ET	1

Type of Procedure  : SERIES

Required Flash Card Printer:

Required Flash Card Format :

Staff Review of Reports Req:

Rad Approval of Request Req:

Type of Imaging  : GENERAL RADIOLOGY

Descendents  :

Procedure Message  :

### Report Distribution Lists

**[RA DISTP]**

This option displays data in the Report Distribution Queue file #74.3.

For more information on report distribution, refer to the Index and the chapter on Reports Distribution Edit.

| Prompt/User Response      | Discussion                                                                                     |
|---------------------------|------------------------------------------------------------------------------------------------|
| Report Distribution Lists |                                                                                                |
| DEVICE: (Printer Name)    | Enter the name of a printer or press the &lt;RET&gt; key to display the output on your screen. |

Report Distribution Queue List     PAGE 1

CATEGORY OF  INACTIVATION

NAME    REPORTS  DATE

TOP OF PAGE MESSAGE

--------------------------------------------------------------------------------

CLINIC REPORTS   OUTPATIENT

***** Clinic Distribution *****

================================================================================

FILE ROOM   INPATIENT

***** Radiology File Room Distribution *****

================================================================================

MEDICAL RECORDS   ALL REPORTS

***** MAS Medical Records Room Distribution *****

================================================================================

OTHER THAN WARD OR CLINIC NON WARD OR CLINIC

***** Non Ward or Clinic Reports *****

================================================================================

REQUESTING PHYSICIAN  ALL REPORTS

================================================================================

WARD REPORTS   INPATIENT

***** Ward Distribution *****

================================================================================

### Sharing Agreement/Contract List

**[RA SHARINGP]**

This option prints data from the Contract/Sharing Agreement file #34.

For more information on sharing agreements and contracts, refer to the Index and the chapter on Sharing Agreement/Contract Entry/Edit.

| Prompt/User Response            | Discussion                                                                               |
|---------------------------------|------------------------------------------------------------------------------------------|
| Sharing Agreement/Contract List |                                                                                          |
| DEVICE: (Printer Name)          | Enter the name of a printer or press the <RET> key to display the output on your screen. |

Contract/Sharing Agreements   OCT 3,1996  PAGE 1

TYPE OF INACTIVATION

AGREEMENT NAME   AGREEMENT DATE

------------------------------------------------------------------------------

CONTRACTOR LFL   CONTRACT

MEMORIAL HOSPITAL  SHARING

HOSPITAL  SHARING

### Standard Reports Print

**[RA STANDPRINT]**

This option prints data from the Standard Reports file #74.1.

For more information on standard reports, refer to the Index and the chapter on Standard Reports Entry/Edit.

| Prompt/User Response   | Discussion                                                                                                                                      |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Standard Reports Print |                                                                                                                                                 |
| DEVICE: (Printer Name) | Enter the name of a printer or press the &lt;RET&gt; key to display the output on your screen.  Here is an example of what the report contains: |

Standard Reports List    OCT 3,1996  PAGE 1

REPORT

NUMBER STANDARD REPORT

------------------------------------------------------------------------------

1 NORMAL CHEST - PA/LAT

Report Text:

PA and Lateral views of the chest were obtained. The bones and soft tissues are unremarkable. The cardiac silhouette is normal in size. The lung fields are clear bilaterally.

Impression:

Normal Chest X-ray.

Standard Reports List    OCT 3,1996  PAGE 2

REPORT

NUMBER STANDARD REPORT

------------------------------------------------------------------------------

2 NORMAL LUMBAR SPINE

Report Text:

The disc spaces are normal. There is no spondylolysis or spondylolisthesis.

Impression:

Normal lumbar sacral spine.

### VistaRad Category Print

**[RA VISTARAD CATEGORY P]**

This option may be displayed under the 'Maintenance Files Print Menu' ONLY IF the VistaRad component of the Imaging package is being used; otherwise, this option will not be displayed.

This option allows the user to list only the VISTARAD CATEGORY field that is in the EXAMINATION STATUS file (#72), without having to list all the other fields that are seen in the 'Examination Status List' option.

In this option, you will be asked to select one or more Imaging types and then a device. The current VISTARAD CATEGORY value for all exam statuses of the selected Imaging types will be displayed/printed.

Prompt/ **User Response**

VistaRad Category Print

Select Imaging Type: **GENE** RAL RADIOLOGY

Another one (Select/De-Select): CT SCAN

Another one (Select/De-Select): **&lt;RET&gt;**

Select Device: HOME// **&lt;RET&gt;** TELNET Right Margin: 80// **&lt;RET&gt;**

VistaRad Categories   Page: 1

Run Date:

----------------------------------------------------------------------

Type Of Imaging: CT SCAN

Status   Order VistaRad Category

CANCELLED   0

WAITING FOR EXAM  1 Waiting for Exam

EXAMINED   2 Examined

TRANSCRIBED   3 Transcribed

COMPLETE   9

Type Of Imaging: GENERAL RADIOLOGY

Status   Order VistaRad Category

CANCELLED   0

WAITING FOR EXAM  1

## CALLED FOR EXAM  2

EXAMINED   3 Examined

TRANSCRIBED   4

Enter RETURN to continue or '^' to exit: **&lt;RET&gt;**

VistaRad Categories   Page: 2

Run Date:

----------------------------------------------------------------------

COMPLETE   9

Enter RETURN to continue or '^' to exit:


## 9 Radiology HL7 Menu

Supervisor Menu ...

**Radiology HL7 Menu ...**

### Send ADT HL7 message to PACS

[RA ADT]

This option forces an ADT-A08 patient demographic update message to be sent from VistA to PACS. If the patient selected had a patient identifier (SSN) update, an ADT-A47 message will also be sent. Note that this option requires patch MAG*3*183 be installed and configured. Please see the MAG*3*183 patch description for details on setting up ADT messages to PACS.

Select Patient(s): TEST,PATIENT TRES III  5-2-53 100001113 NO

NSC VETERAN

Another one (Select/De-Select):

Would you like to task this Job? Yes// n (No)

Demographic updates sent for 1 patients

| Prompt/User Response                          | Discussion                                                                       |
|-----------------------------------------------|----------------------------------------------------------------------------------|
| Select Patient(s):                            | Enter a patient or ‘ALL’ to send demographic updates for all radiology patients. |
| Another one (Select/De-Select):               | Enter additional patients                                                        |
| Would you like to task this Job? Yes// n (No) | Enter Yes or No                                                                  |

Select Patient(s): TEST,PATIENT TRES III  5-2-53 100001113 NO

NSC VETERAN

Another one (Select/De-Select):

Would you like to task this Job? Yes// (Yes)

Requested Start Time: NOW// (OCT 05, 2017@09:13:26)

Task# 148673

| Prompt/User Response                         | Discussion                                                      |
|----------------------------------------------|-----------------------------------------------------------------|
| Would you like to task this Job? Yes// (Yes) | Enter Yes or No                                                 |
| Requested Start Time: NOW//                  | If you choose to task it, you will be prompted for a start time |
| Task# 148673                                 | Confirmation TASK number displayed                              |

### Rad/Nuc Med HL7 Voice Reporting Errors

**[RA HL7 VOICE REPORTING ERRORS]**

This option displays HL7 messages received from Voice Recognition Reporting Tools (MedSpeak, PowerScribe, TalkStation, etc.) which have been rejected by Vist *A* Radiology. These messages are stored in the HL7 Message Exceptions file #79.3.

Further options are available to allow the list to be printed and individual messages can be resent and/or deleted.

| Prompt/User Response                                                                                                                                                     | Discussion                                                                                                     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Rad/Nuc Med HL7 Voice Reporting Exception List                                                                                                                           | This report allows printing by selected Voice Reporting Application, Date and Radiology User.                  |
| Select Voice Reporting Application: ALL//  **RA-C**  LIENT-TCP  Another one (Select/De-Select):  **RA-T**  ALKLINK-TCP  Another one (Select/De-Select):  **&lt;RET&gt;** | Enter the name of a Voice Reporting Application (File #771) or press the <RET> key to select all applications. |
| Exception starting date/time:  **JAN1**  ()                                                                                                                              | Enter a date to begin reporting from.                                                                          |
| Exception ending date/time: NOW//  **&lt;RET&gt;**  (JUN 11, 1999@12:18:26)                                                                                              | Enter the most recent date/time to report on or press the &lt;RET&gt; key to accept the default of now.        |

| Prompt/User Response                                                                                 | Discussion                                                                                                                                                                 |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select Radiology User: ALL//  **TAY**  LOR,CAMERON  Another one (Select/De-Select):  **&lt;RET&gt;** | Individual users can be selected for reporting. (Entries associated with unknown users will always be displayed). Alternatively, press the <RET> key to display all users. |

HL7 Voice Reporting Errors    	Page: 1 of 1

**Date Time Patient   Case# User**

HL7 Voice Reporting Application: MEDSPEAK

1. MAR 12,1999 11:17:20 NAMEB,PATIENT  1111 USER,ONE

Error: Event Protocol Pointer (field #773,8) missing

2.   Not known   ????? Not Known

Error: Missing Exam Date and/or Case Number

3.   NAMEA,PATIENT  1 Not Known

Error: Invalid Provider Name

HL7 Voice Reporting Application: TALKSTATION

4. MAR 16,1999 13:45:28 NAMEC,PATIENT  2022 USER,ONE

Error: Case Number Invalid

Enter ?? for more actions

PL Print Exceptions List FS First Screen  UP Prev HL7 Exception

RS Resend HL7 Message NS Next Screen  DN Next HL7 Exception

DE Delete HL7 Exception LS Last Screen  Q Quit

Select Action: Next Screen//

| Prompt/User Response                                                                                                                                                                                    | Discussion                                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select Action: Next Screen//  **&lt;RET&gt;**                                                                                                                                                           | List Manager will display the next page of HL7 Exceptions in the center screen.                                                                            |
| Select Action: Next Screen//  **LS**                                                                                                                                                                    | List Manager will jump to the last screen of entries in the file.                                                                                          |
| Select Action: Quit//  **FS**                                                                                                                                                                           | List Manager will re-display the first screen of entries shown above.                                                                                      |
| Select Action: Next Screen//  **&lt;&gt;**                                                                                                                                                              | Scroll down through each entry individually.                                                                                                               |
| Select Action: Next Screen//  **&lt;&gt;**                                                                                                                                                              | Scroll back up through each entry individually.                                                                                                            |
| Select Action: Next Screen//  **PL**  Select Device: (enter a printer)  Do you want your output QUEUED? NO//  **Y**  (YES)  Requested Start Time: NOW//  **&lt;RET&gt;**  Request Queued, Task #: 81303 | The entire list will be sent to a printer. (Each Sending Application will start on a separate page).  Print immediately or request the job to start later. |

================================================================================

HL7 Voice Reporting Errors      Page: 1

(MEDSPEAK - RADIOLOGY/NUCLEAR MEDICINE)  Printed:

==============================================================================

Exception Date: MAR 12,1999 at 11:17:20 User: USER,ONE

Patient Name: NAMEB,PATIENT   Case: 1111

Reason Rejected: Event Protocol Pointer (field #773,8) missing

Exception Date:  at  User: Not Known

Patient Name: Not known   Case: ?????

Reason Rejected: Missing Exam Date and/or Case Number

Exception Date:  at  User: Not Known

Patient Name: NAMEA,PATIENT   Case: 1

Reason Rejected: Invalid Provider Name

================================================================================

HL7 Voice Reporting Errors      Page: 2

(TALKSTATION - RADIOLOGY/NUCLEAR MEDICINE) Printed:

==============================================================================

Exception Date: MAR 16,1999 at 13:45:28 User: USER,ONE

Patient Name: NAME,PATIENT1   Case: 2022

Reason Rejected: Case Number Invalid

Exception Date: MAR 19,1999 at 15:12:25 User: USER,ONE

Patient Name: NAME,PATIENT2   Case: 2098

Reason Rejected: Missing Exam Date

Exception Date: MAR 23,1999 at 14:38:57 User: USER,ONE

Patient Name: NAME,PATIENT3   Case: 1111

Reason Rejected: Invalid Procedure

Exception Date: MAR 23,1999 at 15:07:53 User: USER,ONE

Patient Name: NAME,PATIENT4   Case: 22

Reason Rejected: Invalid Diagnostic Code

Exception Date: APR 5,1999 at 15:37:09 User: USER,ONE

Patient Name: NAME,PATIENT3   Case: 278

Reason Rejected: Report already on file

Exception Date: APR 6,1999 at 14:39:14 User: USER,ONE

Patient Name: NAME,PATIENT3   Case: 278

Reason Rejected: Report already on file

| Prompt/User Response                                                                                   | Discussion                                                                                                                                                                                                                                       |
|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select Action: Next Screen//  **RS**  Select HL7 Exception (1-34)  **:9**  Re-sending Message #3749... | To re-send a message from the list,  Select an entry from the list. Once re-sent it cannot be re-selected. A message similar to "Message Re-submitted on JUN 11, 1999@14:15:51" is displayed instead of the rejection reason.                    |
| Select Action: Next Screen//  DE  Select HL7 Exception (1-34) :  **10**  Deleting Exception...         | To permanently delete an exception report entry, select an entry from the list.  Once deleted it cannot be re-selected. A message similar to "Reported Exception Deleted on JUN 11, 1999@14:22:40" is displayed instead of the rejection reason. |

### Resend Radiology HL7 Message

[RA HL7 MESSAGE RESEND]

There are many reasons why an HL7 message may not reach its attempted destination. This option allows you to re-send HL7 messages for such cases. The option will prompt for a Radiology case and will then build a new HL7 message in the hope that it will reach the subscribing applications this time.

| Prompt/User Response               | Discussion                                                                                                                                                                                                          |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Enter Case Number:  **120400-111** | Enter an active case number, or a completed case as "MMDDYY-999", or a patient's name, or a patient's 9 digit SSN, or the first character of the patient's last name and the last four digits of the patient's SSN. |

Choice Case No. Procedure   Name   Pt ID

------ -------- ---------   ----------------- ------

1 120400-111 ABDOMEN FOR FETAL AGE 1 V PATIENT,TEST  9999

=====================================================================

Re-Broadcast the 'EXAM REGISTERED' HL7 message for this case??? YES// **y** YES

| Prompt/User Response   | Discussion                                                                                                                                                                                                       |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                        | A confirmation prompt is displayed. Enter "Y" to Continue or "N" to cancel. The prompt will either read:  EXAM REGISTERED,  EXAM CANCELLED, or  REPORT VERIFIED depending on the current exam and report status. |

### Resend Radiology HL7 Messages by Date Range

[RA HL7 MESSAGE RESEND BY DATE RANGE]

This option can be used to resend HL7 messages to selected subscribers by date range. This can be useful for sending historical data to a new radiology interface, such as PACS. However, it must be run with caution. It is not recommended to resend a date range over one month at a time and always queue it to run outside of normal business hours.

| Prompt/User Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Discussion                                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Beginning Date:  **FEB 13, 2021**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Enter the beginning date for the date range you plan to resend.                                                                                                                                                                                                                                                                                                                              |
| Ending Date: NOW//  **FEB 18, 2021**  *** Pick the application in which to send the radiology data ***  #1 RA-CLIENT-IMG  #2 RA-PSCRIBE-TCP  #3 RA-TALKLINK-TCP  #4 TIUHL7 EX RECEIVING APP  #5 MAG PRECACHE CLIENT  #6 RA-NTPV2-TCP  Enter a number (1-6):  **2**  The: RA-PSCRIBE-TCP will be the recipient  Reviewing exams for selected time period... (This may take a few minutes)..  **.**  During this period of time 3 Exams were performed and app Run time= 0 Hours.  Scheduled time to run:  **TODAY@23:59//&lt;enter&gt;**  Task #:  **4489963**  Has been Tasked | Enter the end date for the date range to resend.  Select the receiving application to resend messages to. Note this list will vary based on HL7 interfaced devices implemented at your site.  Accept the default or enter a new date/time to queue the task to run. Always queue it outside of normal business hours.  Make a note of the TASK number in case you need to go in and stop it. |

## 10 Radiology Study Tracker Menu

Supervisor Menu ...

**Radiology Study Tracker Menu ...**

### Check a Radiology or Consult Study for Images

[MAGD ACN CHECK]

This option will check individual radiology or clinical specialty studies are checked for the existence of images.

| Prompt/User Response                                                                                                                                                                                                                                                                                                                                                                                                                                  | Discussion                                                                                                                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Enter an Accession Number:  **660-011020-73**  No images were found for this accession number  Enter an Accession Number:  **660-072919-611**  Information on Study for Accession Number: 660-072919-611  ------------------------------------------------  Set #1: Legacy (Group: 31955)  PATIENT: PATIENT,SEVENTWONINE SSN: 000-00-0729  DOB: 1925  PROCEDURE: MRI KNEE WITHOUT CONTRAST  DICOM -- STUDIES: 1 SERIES: 6 IMAGES: 311  DCM FILES: 311 | This can be a legacy accession number, a site specific accession number or a consult number (e.g. 660-GMR-123, 111231-345, 660-111231-345)  Displayed if no images are found.  Details of images found displayed |

### Report Radiology Studies without Images

[MAGD RAD RANGE CHECK]

Users holding the MAGD QR REPORT security key can run this report to check a range of radiology studies for the existence of images.

| Prompt/User Response                                                                                                                                                                                                                                                                         | Discussion                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Search for Radiology Exams Lacking Images  ------------------------------------------  Enter the earliest date for the study.  Earliest Study Date: T-1000 (MAY 10, 2018)  Enter the latest date for the study.  Latest Study Date: T (FEB 03, 2021)  Recommend report output of 132 columns | Enter the beginning date and ending date to search for radiology studies without images. |

Radiology Exams without Images in VistA Imaging

From MAY 10,2018 to FEB 3,2021@23:59:59

Imaging Location: TD-MAINRAD

Accession  Patient Name   Last4 Exam Date Procedure

--------------------------------------------------------------------------------------

012617-408  PATIENT,ONETWOSIX  0126 JAN 26,2017 ABDOMEN 1 VIEW

Press RETURN to continue or '^' to exit:

Radiology Exams without Images in VistA Imaging

From MAY 10,2018 to FEB 3,2021@23:59:59

Imaging Location: TD-RAD

Accession  Patient Name   Last4 Exam Date Procedure

--------------------------------------------------------------------------------------

660-060718-443 PATIENT,SIXZEROSEVEN  0607 JUN 7,2018 ABDOMEN 1 VIEW

660-060718-444 PATIENT,SIXZEROSEVEN  0607 JUN 7,2018 CHEST 2 VIEWS PA&amp;LAT

660-081318-445 PATIENT,EIGHTONETHREE  0813 AUG 13,2018 CHEST 2 VIEWS PA&amp;LAT

660-040319-609 PATIENT,ONEZEROTWOTHREE  1023 APR 3,2019 ABDOMEN 1 VIEW

660-073019-612 PATIENT,SEVENTWONINE  0729 JUL 30,2019 MRI KNEE WITHOUT CONTRAST

660-011420-615 PATIENT,ONEONEFOUR  0114 JAN 14,2020 CHEST 2 VIEWS PA&amp;LAT

Press RETURN to continue or '^' to exit:

RUN COMPLETED at Feb 03, 2021@13:55:06

### DICOM Query Client

[MAGD QUERY]

The DICOM Query Client option is used to interrogate PACS for information about patients, studies, series, and images.

### DICOM Query/Retrieve Client

[MAGD QUERY/RETRIEVE]

Users holding the MAGD QR MANUAL RETRIEVE security key can use the DICOM Query/Retrieve client option to interrogate PACS for information about patients, studies, series, and images. It is also used for transferring DICOM objects from PACS to VistA or other destinations.

### Compare Radiology Image Count on PACS with VistA

[MAGD RAD COUNT COMPARE]

Users holding the MAGD QR REPORT security key can run this option to batch compare radiology image count on PACS with those on VistA. Comparison by patient, date range, or IEN range.

********************************************************************************

***          ***

*** DICOM Radiology Image Count Comparer    ***

*** ------------------------------------    ***

***          ***

*** This application passes the radiology files to find completed studies. ***

*** It compares the count of the study's images (if any) with those on PACS. ***

***          ***

*** No images are transferred from the PACS to VistA, however.  ***

***          ***

*** The DICOM Gateway issues the DICOM Query/Retrieve requests to send ***

*** the images from the PACS to VistA.     ***

********************************************************************************

| Prompt/User Response                                                                                                                                                                                                                                                                       | Discussion                                                                                                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Scan by Date, Report Number, Patient, or Accession (D, N, P, or A): DATE//  **P**  Please select the Radiology PACS Query/Retrieve Provider  DICOM Q/R Service Class Providers  ------------------------------------  1 -- LAUREL BRIDGE POWER TOOLS  2 -- LOCAL DVTK QUERY  3 -- PACS Q/R | Select your preference to scan by Date, Report Number, Patient, or Accession number. Enter to select the default of DATE.  This is the provider that has images stored. |
| Select the provider application (1-3):  **3**  Enter Patient:  **P0729**  -- 1 MATCH                                                                                                                                                                                                       | Prompt based on your ‘Scan by’ selection earlier                                                                                                                        |

Social Sec# Sex Patient’s Name  Birth Date

------------- --- ----------------  ------------

1) 000-00-0000 M PATIENT,SEVENTWONINE 1925

Patient has 2 imaging studies on file from Jul 19, 2017 to Jul 19, 2018

| Prompt/User Response                                                                                                                                         | Discussion                                        |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| Is this the correct patient? n//  **Y**  Enter the scanning order for studies: ASCENDING//  **ASCENDING**  Enter the earliest date for the study.            | Confirm patient  The order studies are scanned.   |
| Earliest Study Date: Jul 19, 2017//  **&lt;enter&gt;**  Enter the latest date for the study.  Latest Study Date: Jul 19, 2018@23:59:59 //  **&lt;enter&gt;** | Defaults pulled in from initial patient selection |

### Retrieve Missing Radiology Images from PACS

[MAGD RAD AUTO RETRIEVE]

Holders of the MAGD QR AUTO RETRIEVE security key can use this option to batch compare radiology image UIDs on PACS with those on VistA and retrieve the missing images from PACS.

### Display stats for automatic radiology Q/R runs

[MAGD Q/R RAD RUN STATISTICS]

This option will display the statistics for all the radiology Q/R image compare and retrieve runs. Data includes VistA/Legacy studies processed, VistA studies without images, series and image counts, and new SOP class and PACS counts.

Entry #1 Started: Feb 03, 2021@13:14:55 Ended: Feb 03, 2021@13:15:01

CONSULTS COMPARE IMAGE COUNTS by PATIENT Status: COMPLETED

PACS: PACS Q/R

DFN: 719 Beginning Date: Jul 19, 2017 Ending Date: Jul 19, 2018

Sort Order: ASCENDING   Hours: YYYYYYYYYYYYYYYYYYYYYYYY

Last Accession #: 660-GMR-272   M12345678901N12345678901

Last Study Date: Jul 19, 2018 Last DFN: 719 Last Report #: 272

Services: CARDIOLOGY, GASTROENTEROLOGY, HEMATOLOGY, OPHTHALMOLOGY, DENTAL-OPT,

DENTAL-INPT

VISTA STUDIES PROCESSED\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_2

VISTA STUDIES WITHOUT IMAGES\_\_\_\_\_\_\_\_\_\_\_\_1

LEGACY STUDIES PROCESSED\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_3

LEGACY SERIES COUNT\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_1

LEGACY IMAGE COUNT\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_15

NEW SOP CLASS STUDIES PROCESSED\_\_\_\_\_\_\_\_\_0

NEW SOP CLASS SERIES COUNT\_\_\_\_\_\_\_\_\_\_\_\_\_\_0

NEW SOP CLASS IMAGE COUNT\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_0

PACS STUDIES PROCESSED\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_1

PACS STUDIES WITHOUT IMAGES\_\_\_\_\_\_\_\_\_\_\_\_\_1

PACS SERIES COUNT\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_1

PACS IMAGE COUNT\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_4

PACS STUDY LEVEL RETRIEVES\_\_\_\_\_\_\_\_\_\_\_\_\_\_0

PACS SERIES LEVEL RETRIEVES\_\_\_\_\_\_\_\_\_\_\_\_\_0

PACS IMAGES RETRIEVED\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### Delete the stats for automatic radiology Q/R runs

[MAGD RAD STATISTICS DELETE]

Holders of the MAG SYSTEM security key can run this option to delete the stats for automatic radiology Q/R runs

| Prompt/User Response                                                                                                                                                                 | Discussion                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| There is one entry in the AUTOMATIC DICOM Q/R RUN STATS for CONSULTS.  Do you want to remove it? n//  **Y**  The AUTOMATIC DICOM Q/R RUN STATS file for CONSULTS has been truncated. | Indicated the number of records stored  Confirm removal of statistical data |

### Stop automatic Q/R processes

[MAGD STOP AUTOMATIC PROCESSES]

Holders of the MAGD QR REPORT security key can use this option to stop all automatic compare image count on PACS with VistA and retrieval of missing radiology study and CPRS consult/procedure images.

| Prompt/User Response                                                                                                                   | Discussion                                               |
|----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| RADIOLOGY COMPARE IMAGE COUNTS  Started: 2/3/21 2:19 pm  Stop this process? y//  **Y**  VistA Automatic Q/R Processing will stop soon. | Displays running process  Confirm termination of process |

In the Automatic Q/R Process, the following message will be reported:

User requested VistA Automatic Q/R Processing to stop at Feb 03, 2021@14:19:49

RUN Stopped by User at Feb 03, 2021@14:19:49

## 11 Worksheets

### Division Parameters

Division: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Parameter     	Parameter Set Equal to: 	YES  	NO

================================================================

**Division-wide Order Entry Parameters:**

ASK IMAGING LOCATION:	\_\_\_	\_\_\_

TRACK REQUEST STATUS CHANGES:	\_\_\_	\_\_\_

CLINICAL HISTORY MESSAGE: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Exam Entry/Edit Parameters:**

DETAILED PROCEDURE REQUIRED:	\_\_\_	\_\_\_

ASK 'CAMERA/EQUIP/RM':	\_\_\_	\_\_\_

AUTO USER CODE FILING:	\_\_\_	\_\_\_

TRACK EXAM STATUS CHANGES:	\_\_\_	\_\_\_

ASK EXAM STATUS TIME:	\_\_\_	\_\_\_

TIME LIMIT FOR FUTURE EXAMS:	\_\_\_	\_\_\_

**Films Reporting Parameters:**

ALLOW STANDARD REPORTS:	\_\_\_	\_\_\_

ALLOW BATCHING OF REPORTS:	\_\_\_	\_\_\_

ALLOW COPYING OF REPORTS:	\_\_\_	\_\_\_

IMPRESSION REQUIRED ON REPORTS:	\_\_\_	\_\_\_

ALLOW VERIFYING BY RESIDENTS:	\_\_\_	\_\_\_

**Division Parameters (continued)**

Division: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Parameter     	Parameter Set Equal to: 	YES  	NO

==============================================================

ALLOW RPTS ON CANCELLED CASES?:	\_\_\_	\_\_\_

WARNING ON RPTS NOT YET VERIF?: 	\_\_\_	\_\_\_

AUTO E-MAIL TO REQ. PHYS?: 	\_\_\_	\_\_\_

ALLOW  COTS HL7 RPTS	\_\_\_	\_\_\_

**Miscellaneous Division Parameters:**

PRINT FLASH CARD FOR EACH EXAM:	\_\_\_	\_\_\_

PRINT JACKET LBLS W/EACH VISIT:	\_\_\_	\_\_\_

CONTRAST REACTION MESSAGE: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

RPHARM DOSE WARNING MESSAGE: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Imaging Locations Associated with this Division:**

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### Camera/Equip/Room

NAME:		DESCRIPTION:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### Location Parameters

Imaging Location: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Imaging Type: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Principal Clinic: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Parameter        Parameter Set Equal to

==============================================================

**Flash Card Parameters**

HOW MANY FLASH CARDS PER VISIT: 0 1 2 3 4 5 6 7 8 9 10

DEFAULT FLASH CARD FORMAT: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Jacket Label Parameters**

HOW MANY JACKET LBLS PER VISIT: 0 1 2 3 4 5 6 7 8 9 10

DEFAULT JACKET LABEL FORMAT: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Exam Label Parameters**

HOW MANY EXAM LABELS PER VISIT: 0 1 2 3 4 5 6 7 8 9

DEFAULT EXAM LABEL FORMAT: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Report Parameters**

DEFAULT REPORT HEADER FORMAT: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

DEFAULT REPORT FOOTER FORMAT: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

REPORT LEFT MARGIN: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

REPORT RIGHT MARGIN: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

PRINT DX CODES IN REPORT?:			YES: \_\_\_\_	NO: \_\_\_\_

VOICE DICTATION AUTO-PRINT:		YES: \_\_\_\_	NO: \_\_\_\_

**Location Parameters (continued)**

Imaging Location: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Parameter        Parameter Set Equal to

==============================================================

**Cameras/ Equipment/Rooms Used by this Imaging Location:**

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Default CPT Modifiers used by this Location:**

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Recipients of the 'Stat' Alert for this Location**

STAT REQUEST ALERT RECIPIENTS:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Location Parameters (continued)**

Imaging Location: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Parameter        Parameter Set Equal to

==============================================================

URGENT REQUEST ALERTS?:			YES: \_\_\_\_	NO: \_\_\_\_

ALLOW 'RELEASED/NOT VERIFIED':		YES: \_\_\_\_	NO: \_\_\_\_

**Credit and DSS Parameters**

CREDIT METHOD: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

DSS ID: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### Classification

**CLASSIFICATION	LOCATION**

**NAME	(Resident/Staff/Clerk/Technologist)	ACCESS**

=========================================================

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### Blank Examination Status Worksheet

**Imaging Type:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Field:	Statuses:**

|                                                | Can-celled   | Waiting  for  Exam   | Called  for Exam   | Exam-ined   | Tran-scribed   | Com-plete   |
|------------------------------------------------|--------------|----------------------|--------------------|-------------|----------------|-------------|
| Order in sequence of status progression        |              |                      |                    |             |                |             |
| Should this Status appear in Status Tracking   |              |                      |                    |             |                |             |
| User Key needed to move an exam to this status |              |                      |                    |             |                |             |
| Default next status for exam                   |              |                      |                    |             |                |             |
| Can an exam be cancelled while in this status  |              |                      |                    |             |                |             |
| Generate exam alert for requesting physician   |              |                      |                    |             |                |             |
| Generate Examined HL7 Message                  |              |                      |                    |             |                |             |
| VISTARAD Category                              |              |                      |                    |             |                |             |
| **Data Requirements for this Status**          | **-----**    | **-----**            | **-----**          | **-----**   | **-----**      | **-----**   |
| Technologist Required                          |              |                      |                    |             |                |             |
| Resident Or Staff Required                     |              |                      |                    |             |                |             |
| Detailed Procedure Required                    |              |                      |                    |             |                |             |
| Film Entry Required                            |              |                      |                    |             |                |             |
| Diagnostic Code Required                       |              |                      |                    |             |                |             |
| Camera/Equip/RM Required                       |              |                      |                    |             |                |             |
| Procedure Modifiers Required                   |              |                      |                    |             |                |             |
| CPT Modifiers Required                         |              |                      |                    |             |                |             |
| Radiopharms & Dosages required                 |              |                      |                    |             |                |             |
| Activity Drawn required (Radiopharm)           |              |                      |                    |             |                |             |
| Drawn Dt/Time and Person required (Radiopharm) |              |                      |                    |             |                |             |
| Admin Dt/Time/Person required (Radiopharm)     |              |                      |                    |             |                |             |
| Route/Site required (Radiopharm Administered)  |              |                      |                    |             |                |             |
| Lot No. required (Radiopharm)                  |              |                      |                    |             |                |             |
| Volume/Form required (Radiopharm)              |              |                      |                    |             |                |             |
| Report Entered Required                        |              |                      |                    |             |                |             |
| Impression Required                            |              |                      |                    |             |                |             |
| Verified Report Required                       |              |                      |                    |             |                |             |

| **To Move to this Status**               | **-----**   | **-----**   | **-----**   | **-----**   | **-----**   | **-----**   |
|------------------------------------------|-------------|-------------|-------------|-------------|-------------|-------------|
| Ask for Technologist                     |             |             |             |             |             |             |
| Ask for Interpreting Physician           |             |             |             |             |             |             |
| Ask for Procedure                        |             |             |             |             |             |             |
| Ask for Film Data                        |             |             |             |             |             |             |
| Ask for Diagnostic Code                  |             |             |             |             |             |             |
| Ask for Camera/Equip/RM                  |             |             |             |             |             |             |
| Ask for Procedure Modifiers              |             |             |             |             |             |             |
| Ask for CPT Modifiers                    |             |             |             |             |             |             |
| Ask for User Code                        |             |             |             |             |             |             |
| Ask Medications & Dosages                |             |             |             |             |             |             |
| Ask Medication Admin Dt/Time & Person    |             |             |             |             |             |             |
| Ask Radiopharmaceuticals and Dosages     |             |             |             |             |             |             |
| Ask Activity Drawn (Radiopharmaceutical) |             |             |             |             |             |             |
| Ask Drawn Dt/Time & Person (Radiopharm)  |             |             |             |             |             |             |
| Ask Admin Dt/Time & Person (Radiopharm)  |             |             |             |             |             |             |
| Ask Route/Site of Admin (Radiopharm)     |             |             |             |             |             |             |
| Ask  No. (Radiopharm)                    |             |             |             |             |             |             |
| Ask Volume/Form (Radiopharm)             |             |             |             |             |             |             |

| **Exams in this Status should appear on these Reports**   | **-----**   | **-----**   | **-----**   | **-----**   | **-----**   | **-----**   |
|-----------------------------------------------------------|-------------|-------------|-------------|-------------|-------------|-------------|
| Clinic Report                                             |             |             |             |             |             |             |
| PTF Bedsection Report                                     |             |             |             |             |             |             |
| Service Report (Workload)                                 |             |             |             |             |             |             |
| Sharing/Contract Report (Workload)                        |             |             |             |             |             |             |
| Ward Report (Workload)                                    |             |             |             |             |             |             |
| Film Usage Report (Workload)                              |             |             |             |             |             |             |
| Technologist Report (Workload)                            |             |             |             |             |             |             |
| AMIS Report (Workload)                                    |             |             |             |             |             |             |
| Detailed Procedure Report (Workload)                      |             |             |             |             |             |             |
| Camera/Equip/RM Report                                    |             |             |             |             |             |             |
| Physician Report                                          |             |             |             |             |             |             |
| Resident Report                                           |             |             |             |             |             |             |
| Staff Report                                              |             |             |             |             |             |             |
| Delinquent Status Report                                  |             |             |             |             |             |             |
| **Radiopharmaceutical Dosage Ticket Print Control**       | **-----**   | **-----**   | **-----**   | **-----**   | **-----**   | **-----**   |
| Print Dosage Ticket when exam reaches this status         |             |             |             |             |             |             |

Examination Statuses

Below is the set of exam statuses as released for each Imaging Type. **Note: They are populated, but not activated.** To activate, assign an Order number, a Default Next Status, and indicate that it should Appear on Status Tracking.

**Field:	Statuses:**

|                                                | Can-celled   | Waiting  for  Exam   | Called  for Exam   | Exam-ined   | Tran-scribed   | Com-plete   |
|------------------------------------------------|--------------|----------------------|--------------------|-------------|----------------|-------------|
| Order in sequence of status progression        | **0**        | **1**                |                    |             |                | **9**       |
| Should this Status appear in Status Tracking   |              | **Y**                |                    |             |                |             |
| User Key needed to move an exam to this status |              |                      |                    |             |                |             |
| Default next status for exam                   |              |                      |                    |             |                |             |
| Can an exam be cancelled while in this status  | **Y**        | **Y**                | **Y**              |             |                |             |
| Generate exam alert for requesting physician   |              |                      |                    |             |                |             |
| Generate Examined HL7 Message                  |              |                      |                    |             |                |             |
| **Data Requirements for this Status**          | **-----**    | **-----**            | **-----**          | **-----**   | **-----**      | **-----**   |
| Technologist Required                          |              |                      | **Y**              | **Y**       | **Y**          | **Y**       |
| Resident Or Staff Required                     |              |                      |                    |             | **Y**          | **Y**       |
| Detailed Procedure Required                    |              |                      |                    | **Y**       | **Y**          | **Y**       |
| Film Entry Required                            |              |                      |                    | **Y**       | **Y**          | **Y**       |
| Diagnostic Code Required                       |              |                      |                    |             | **Y**          | **Y**       |
| Camera/Equip/RM Required                       |              |                      |                    |             | **Y**          | **Y**       |
| Radiopharms & Dosages required                 |              |                      |                    |             |                |             |
| Activity Drawn required (Radiopharm)           |              |                      |                    |             |                |             |
| Drawn Dt/Time and Person required (Radiopharm) |              |                      |                    |             |                |             |
| Admin Dt/Time/Person required (Radiopharm)     |              |                      |                    |             |                |             |
| Route/Site required (Radiopharm administered)  |              |                      |                    |             |                |             |
| Lot No. required (Radiopharm)                  |              |                      |                    |             |                |             |
| Volume/Form required (Radiopharm)              |              |                      |                    |             |                |             |
| Report Entered required                        |              |                      |                    |             | **Y**          | **Y**       |
| Impression required                            |              |                      |                    |             |                | **Y**       |
| Verified Report required                       |              |                      |                    |             |                | **Y**       |
| **To Move to this Status**                     | **-----**    | **-----**            | **-----**          | **-----**   | **-----**      | **-----**   |
| Ask for Technologist                           |              |                      | **Y**              | **Y**       |                |             |
| Ask for Interpreting Physician                 |              |                      |                    |             | **Y**          |             |
| Ask for Procedure                              |              |                      |                    | **Y**       |                |             |
| Ask for Film Data                              |              |                      |                    | **Y**       |                |             |
| Ask for Diagnostic Code                        |              |                      |                    |             | **Y**          |             |
| Ask for Camera/Equip/RM                        |              |                      |                    | **Y**       |                |             |
| Ask for User Code                              |              |                      |                    |             |                |             |
| Ask Medications & Dosages                      |              |                      |                    |             |                |             |
| Ask Medication Admin Dt/Time & Person          |              |                      |                    |             |                |             |

| Ask Radiopharmaceuticals and Dosages                    |           |           |           | **Y**     |           |           |
|---------------------------------------------------------|-----------|-----------|-----------|-----------|-----------|-----------|
| Ask Activity Drawn (Radiopharmaceutical)                |           |           |           |           |           |           |
| Ask Drawn Dt/Time & Person (Radiopharm)                 |           |           |           |           |           |           |
| Ask Admin Dt/Time & Person (Radiopharm)                 |           |           |           |           |           |           |
| Ask Route/Site of Admin (Radiopharm)                    |           |           |           |           |           |           |
| Ask  No. (Radiopharm)                                   |           |           |           |           |           |           |
| Ask Volume/Form (Radiopharm)                            |           |           |           |           |           |           |
| **Exams in this Status should appear on these Reports** | **-----** | **-----** | **-----** | **-----** | **-----** | **-----** |
| Clinic Report                                           |           | **Y**     | **Y**     | **Y**     | **Y**     | **Y**     |
| PTF Bedsection Report                                   |           | **Y**     | **Y**     | **Y**     | **Y**     | **Y**     |
| Service Report (Workload)                               |           | **Y**     | **Y**     | **Y**     | **Y**     | **Y**     |
| Sharing/Contract Report (Workload)                      |           | **Y**     | **Y**     | **Y**     | **Y**     | **Y**     |
| Ward Report (Workload)                                  |           | **Y**     | **Y**     | **Y**     | **Y**     | **Y**     |
| Film Usage Report (Workload)                            |           | **Y**     | **Y**     | **Y**     | **Y**     | **Y**     |
| Technologist Report (Workload)                          |           | **Y**     | **Y**     | **Y**     | **Y**     | **Y**     |
| AMIS Report (Workload)                                  |           | **Y**     | **Y**     | **Y**     | **Y**     | **Y**     |
| Detailed Procedure Report (Workload)                    |           | **Y**     | **Y**     | **Y**     | **Y**     | **Y**     |
| Camera/Equip/Rm Report                                  |           | **Y**     | **Y**     | **Y**     | **Y**     | **Y**     |
| Physician Report                                        |           | **Y**     | **Y**     | **Y**     | **Y**     | **Y**     |
| Resident Report                                         |           | **Y**     | **Y**     | **Y**     | **Y**     | **Y**     |
| Staff Report                                            |           | **Y**     | **Y**     | **Y**     | **Y**     | **Y**     |
| Delinquent Status Report                                |           | **Y**     | **Y**     | **Y**     | **Y**     |           |
| **Radiopharmaceutical Dosage Ticket Print Control**     | **-----** | **-----** | **-----** | **-----** | **-----** | **-----** |
| Print Dosage Ticket when exam reaches this status       |           |           |           |           |           |           |

### Procedure Setup

(This worksheet addresses **only the new fields** , except Single Report which is only seen when editing Parent Procedures. Remember, the radiopharmaceutical prompts are only used with Nuclear Medicine/Cardiology Studies Imaging Type procedures.)

**Procedure** : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

=========================================================

PROMPT FOR MEDS:	YES \_\_\_\_	NO \_\_\_\_

DEFAULT MEDICATION: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	DOSE: \_\_\_\_\_\_\_\_\_\_\_

SUPPRESS RADIOPHARM PROMPT:	ASK (O) \_\_\_\_	NEVER ASK (1) \_\_\_\_

PROMPT FOR RADIOPHARM RX: 	YES \_\_\_\_	NO \_\_\_\_

*DEFAULT RADIOPHARMACEUTICAL: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

LOW DOSE:	\_\_\_\_\_\_\_	HIGH DOSE:	\_\_\_\_\_\_	USUAL DOSE: \_\_\_\_\_\_

ROUTE:	\_\_\_\_\_\_\_	SITE:	\_\_\_\_\_\_	FORM: 	\_\_\_\_\_\_

EDUCATIONAL DESCRIPTION: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

DISPLAY EDUCATIONAL DESCRIPTION: 	YES \_\_\_\_	NO \_\_\_\_

*	Default Radiopharmaceutical is the only field automatically "stuffed" (added to the record) in the case data. Low, High, and Usual doses are displayed for information during exam edits, and route, site, and form will appear as defaults during exam edits.

### ☞Radiopharmaceuticals

Provide a list of radiopharmaceuticals and their synonyms to your Pharmacy ADPAC so that the pharmaceuticals can be added to the Drug file #50 along with their VA Classification of DX200, DX201, or DX202. See an example of Radiopharmaceutical entries with synonyms in the Drug file following this worksheet.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### Example Radiopharmaceutical Drug Classifications

The following is an example of the radiopharmaceutical entries in the Drug file from one of our test sites.

NUC MED RADIOPHARMS IN DRUG FILE

VA CLASS GENERIC NAME

---------------------------------------------

DX200 Tc99m SODIUM PERTECHNETATE

Synonym: SODIUM PERTECHNETATE

Synonym: TECHNETIUM

Synonym: TC99M

DX200 Tc99m MEDRONATE

Synonym: MDP

Synonym: TC99M

DX200 Tc99m PENTETATE (DTPA)

Synonym: DTPA

Synonym: TC99M

DX200 TL-201 THALLOUS CHLORIDE

Synonym: TL201

Synonym: THALLIUM

Synonym: Tl

DX200 Tc99m MEBROFENIN

Synonym: TC99M

Synonym: HIDA

Synonym: MEBROFENIN

DX200 Tc99m ALBUMIN COLLOID

Synonym: TC99M

Synonym: ALBUMIN COLLOID

Synonym: AC

DX200 Tc99m SULFUR COLLOID

Synonym: TC99M

DX200 Tc99m SESTAMIBI

Synonym: TC99M

Synonym: SESTAMIBI

DX200 Ga-67 GALLIUM CITRATE

Synonym: GA67

DX200 I-123 SODIUM IODIDE

Synonym: SODIUM IODIDE

Synonym: I123

DX200 I-131 SODIUM IODIDE

Synonym: SODIUM IODIDE

Synonym: I131

DX200 Xe-133 XENON GAS

Synonym: XE133

Synonym: XENON

DX200 In-111 PENTETATE (DTPA)

Synonym: IN111

Synonym: INDIUM

DX200 In-111 OXINE

Synonym: IN111

Synonym: INDIUM

DX200 Co-57 CYANCOBALAMIN

Synonym: CO57

Synonym: CO-57

Synonym: COBALT 57

Synonym: CYANCOBALAMIN

DX200 Tc99m LABELLED WBC's

Synonym: TC99M

Synonym: WBC

DX200 In-111 LABELLED WBC's

Synonym: WBC

Synonym: INDIUM

DX200 Tc99m ALBUMIN AGGREGATED

Synonym: TC99M

Synonym: MAA

DX200 Tc99m EXAMETAZIME (CERETEC)

Synonym: TC99M

Synonym: CERETEC

DX200 Tc99m BICISATE (NEUROLITE)

Synonym: TC99M

Synonym: NEUROLITE

DX200 Tc99m LABELLED RBC's

Synonym: TC99M

Synonym: RBC

Synonym: SODIUM PERTECHNETATE

DX200 Tc99m SODIUM PERTECHNETATE/Cold Pyrolite

Synonym: TC99M

Synonym: PYP

DX200 In-111 OctreoScan

Synonym: INDIUM

Synonym: OCTREOSCAN

### ☞Nuclear Medicine Setup

| **Sites of Administration**   | **Synonym(s)**   |
|-------------------------------|------------------|
|                               |                  |
|                               |                  |
|                               |                  |
|                               |                  |
|                               |                  |
|                               |                  |
|                               |                  |
|                               |                  |
|                               |                  |
|                               |                  |

**Vendor/Source**

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

**Nuclear Medicine Setup (continued)**

**Routes of Administration**

ROUTE: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	(P)rompt for Free Text or (V)alid Site: \_\_\_\_

Synonyms:	Valid Sites:

ROUTE: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	(P)rompt for Free Text or (V)alid Site: \_\_\_\_

Synonyms:	Valid Sites:

ROUTE: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	(P)rompt for Free Text or (V)alid Site: \_\_\_\_

Synonyms:	Valid Sites:

ROUTE: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	(P)rompt for Free Text or (V)alid Site: \_\_\_\_

Synonyms:	Valid Sites:

## 12 ☞Parent/Descendent Exam and Printsets

### Definition

An exam set or printset contains a Parent procedure and its Detailed or Series descendent procedures. Requesting a Parent will automatically cause each descendent to be presented for registration as separate cases under a single visit date and time. If the parent is defined to be a printset, the collection and printing of all common report related data between the descendants is seen as one entity.

### Common Data for Printsets

For a printset, a single report is entered regardless of how many descendent cases are registered. Common data for all cases in a printset includes all fields recorded in the Rad/Nuc Med Report file #74 and a few fields in the Rad/Nuc Med Patient file #70: report text, impression, diagnostic codes, primary and secondary residents and staff, verifier, pre-verifier, clinical history, verification and pre-verification date/time and physician, transcriptionist, no-purge indicator, reported date, report status, and exam date/time. For printsets, case-related fields that are common data (residents, staff, diagnostic codes, etc.) are now editable only through report editing functions, and are no longer editable via case editing options. This is necessary to ensure that there is no opportunity for users to enter different data in these fields for each case in a printset.

### Non-Common Data for Printsets

Non-common data still exists for each procedure in a printset. Non-common data includes modifiers, case number, exam status, complications, film, and most other fields that can be edited separately for each case.

### Single Report Setup for Printsets

When setting up Parent type procedures through the Procedure Enter/Edit option, you will see a new prompt, "SINGLE REPORT:", that should be set to YES to indicate that reporting for the registered descendants of the parent procedure will be combined into a single report, making it a printset. If the field is left blank, a separate report will be required for each registered descendent and the cases will NOT be treated as a printset. When descendants are registered in the

Rad/Nuc Med Patient file #70, the "MEMBER OF SET" field on the case record is set automatically by the system as follows:

1 	= descendent procedure, separate reports required

2 	= descendent procedure, single report for all cases under this exam date/time

blank 	= not a descendent, separate report required

Selection of any member of a printset in report related functions will bring up certain identifying information (case numbers, procedures) for all cases in the printset.

Report printouts and displays are modified for printsets to show all non-common data (such as procedure names and modifiers) on one report. The report print format for printsets has been changed to include each procedure and its modifiers. Residents, staff, and diagnoses are printed once for each printset because they are the same for cases in the printset. The same changes have been made to screen displays of reports, to email messages containing reports, and to the retained erroneous report that is stored on the report record before amending it.

If a report for a printset is deleted, each exam in the printset will show that its report was deleted.

If a user tries to create a report for a cancelled case, and the cancelled case belongs to a printset where the other cases of the printset already have a report, then the cancelled case will refer to the same report as the rest of the printset if:

the Division parameter allows reports on cancelled cases, or

the user owns the RA MGR security key.

If neither of these conditions is true, the cancelled case will NOT have a report associated with it. If a cancelled case is selected via a voice recognition system, and the case is part of a printset, the user will not be able to enter a report. Instead, an error message will be transmitted notifying him to use  for reporting on this case.

### Special Character Designation for Printsets

All options that do case lookups and displays will now show special characters to the left of the case number column for cases belonging to a printset **. Note: These will only appear on cases that are entered after the installation of V. 5.0.** This also includes the List Reports in a Batch option and the Distribution Queue Menu options: Clinic Distribution List, Ward Distribution List, and Unprinted Reports List. The Register an Exam and Display Patient Demographics options also display special characters for cases in a printset when the list of the last five procedures is displayed. Options such as Status Tracking do NOT display the special characters because cases of the same printset may be in different statuses and therefore would not appear on the same screen.

In the example below, "+" denotes the first case registered in a set of descendants, and "." appears to the left of the rest of the descendants in the set. Only printsets are displayed this way. So, if the parent procedure's "SINGLE REPORT" field is not set (i.e., if it is left blank), there will be no special characters to the left of the case number. The sequence of case numbers/procedures within a printset are shown in the same order as they were registered regardless of whether the lookup is from an exam edit or report edit/print options.

Sample look-up display:

Case No. Procedure   Exam Date

----------- ------------  -------------

1 122 HAND 3 OR MORE VIEWS

2 **+** 113 ANKLE 2 VIEWS

3 **.** 114 FOOT 2 VIEWS

4 **.** 115 TOE(S) 2 OR MORE VIEWS

5 81 NECK SOFT TISSUE

### HL7 Interface

The HL7 interface to the voice recognition systems is changed so that the voice recognition system screen showing active cases for a selected patient will display cases belonging to a printset. For more complete information on the interface, refer to the Rad/Nuc Med Technical Manual.

The PACS/Imaging interface is changed to include multiple OBR and OBX segments for each individual procedure when a single HL7 message broadcasting an imaging report must account for all the cases in a printset.

### Registration

During registration, a single Detailed, Series, or Broad procedure request can be replaced by a parent-printset from the same Imaging Type and the predefined descendant(s) can either be registered or discarded for other procedures by doing the following:

1. Enter "Pn" at the prompt, where "P" indicates that you want to trigger the parent-printset registration feature and "n" is the request number. The request must NOT be a parent. Only one "n" value is allowed. You will then see a prompt for a parent procedure.
1. Enter a parent procedure of the same imaging type as the requested procedure. The parent must be predefined as a printset.
2. Then proceed to register the predefined descendant(s) OR, discard (^) its descendant(s) and register any descendants you choose when it asks you for more procedures to add on.

The list of requests displayed will have a "+" in front of procedures that are printset parents. (A "+" will not display in front of non-printset parents.) After the replacement printset parent is registered, all outstanding orders that have matching procedures to any just registered will be displayed as a reminder that these may be duplicates and might have to be cancelled.

See the session capture that shows the use of Pn in the chapter Register Patient for Exams, Radiology/Nuclear Medicine User Manual.

### Editing Data

During exam edit, each individual case can be retrieved and edited separately. When editing a case or Diagnostic Code on a case that is a member of a printset, no entering or editing will be allowed on common data. Common data may only be entered and edited through Report Entry/Edit since it must be the same for all cases in the printset. The Report Entry/Edit option now displays all case numbers, exam statuses and procedures that belong to the same printset as the case selected.

When common data is entered through Report Entry/Edit all printset cases' statuses will be updated accordingly. A screen display will warn transcriptionists that all cases are being updated with the same common data. Case editing options only update the status of the individual case being edited; case editing no longer allows editing of report-related fields that are common to all cases in the printset, and, therefore, case editing cannot affect the status of other cases in the printset.

### Labels, Headers, Footers

Label Print field output on printed labels and report headers and footers is modified to print a "+" next to data that is non-common to indicate that the data is part of a related set. This was done because multiple values cannot be printed in the restricted space available in report headers and footers, or on labels. Label print fields affected (case number, procedure, last time this exam performed, long case number, technologist, resident, staff radiologist, and exam modifiers) will have a YES in the new "UNIQUE" field #6 on the Label Print Fields file #78.7. This un-

editable field is released with data and should NOT need further tailoring by the site.

### VA Fileman Prints/Inquiries

The same "+" is used for computed fields on the Rad/Nuc Med Report file #74 when output is generated using VA FileMan Inquire or Print options. An example of this would be using VA FileMan to print File #74's Primary Camera/Equip/Rm computed field. Since the data for this field could be different for each case in a printset, only the data from the first case registered is printed, and a "+" is printed next to it to indicate there could be different Primary Camera/Equip/Rms in other members of the printset.

Any case number in a printset can be used in VA FileMan lookups of the Rad/Nuc Med Report file #74 to retrieve a report for the printset. A new "OTHER CASE#" field #4.5 has been added to this file, and contains all case numbers for a printset report other than the case number already in the "DAY/CASE#" field #.01.

### Add Exams to Last visit

The Add Exams to Last Visit option now allows cases to be added to exam sets **as long as no report has been entered yet for any of the cases** . No new order will be created; the added case will point to the same order as the rest of the cases in the exam set. This is true for printsets, as well as exam sets that require separate reports for each case.

### CPRS Interface for Printsets

The Rad/Nuc Med OE/RR V. 3.0 (CPRS) interface includes functionality to make it plain to the user that a single report applies to multiple procedures.

### Imaging/Multi-Media Interface Effects on Printsets

If your facility is running the Imaging interface, a placeholder ("stub") report will be created to hold the image IDs as soon as the images are collected. From that point on, a lowercase "i" will appear next to the procedure on various lookup screens, but the stub report is otherwise transparent to the user. If you need to delete a printset exam member, you will not be allowed to since a stub report exists. However, you can cancel the case instead.


## 14 Case Edits and Status Tracking

### Overview

The case edit and status tracking options can vary considerably due to the way the system is set up at your site. By defining Division parameters using Division Parameter Set-up [RA SYSDIV], procedure parameters using the Procedure Enter/Edit [RA PROCEDURE] option, and status parameters using the Examination Status Entry/Edit [RA EXAMSTATUS] option you can control a great deal of what the user sees when doing case edits or updating the status of a record. The flow of prompts you see in the case edit and status tracking sections of the user manual may not reflect what your user sees. This chapter is dedicated to providing you some insight into the system response to variations in setup.

### Taking Control

The case edit options **always** follow the same logic; you have little control over what is asked and when it is asked. Case No. Exam Edit and Edit Exam by Patient will prompt for data items that are automatically entered by the system during registration (such as inpatient, ward, bed section, etc.) and data already entered previously. This gives the opportunity to change incorrect data. Complications can also be entered in the case edit options.

To gain control of what and when specific fields appear for editing, you should set up statuses via Examination Status Enter/Edit and use Status Tracking of Exams to enter case information. In other words, always use Status Tracking of Exams for entering case data if you want to control the data flow. Use Case Edit options when you want to edit complications and fields already populated. If your facility does not use Status Tracking, you must make sure Exam Status Parameters don't require any fields that are not asked in the Case Edit options or else you will have problems getting cases to Complete.

### Stuffing Data and Default Responses

Stuffed data is data that automatically becomes an entry in the record because certain conditions are met. Depending on the data that is stuffed, it may or may not be editable. For instance, the sign-on user name may be stuffed but not editable, whereas the requested detailed procedure may be stuffed but it is editable at registration. Default responses may be stuffed data, or they may be provided as

the most logical response to a prompt (e.g., Default Response//) and only become part of the record when you strike the &lt;RET&gt; key to accept it. Some data items such as Default Radiopharmaceutical, can be set up through Procedure Enter/Edit to be automatically entered (stuffed) on a patient exam record. Other data items, such as radiopharmaceutical dose, form etc., are not stuffed into the record, but will appear as default responses if defined for a procedure.

**Only detailed and series procedures** are capable of having stuffed and default responses. Therefore, a parent does not have default responses, but its descendants can have them. A broad procedure cannot have default responses. However, if the requested broad procedure is changed to a detailed procedure at registration, then the user can benefit from the detailed procedure's default answers. If the procedure is changed later on, during case edits or status tracking, the user will need to check the data in the default fields to verify accuracy.

☞The fields that can have responses stuffed when entering data are Film Size, Radiopharmaceuticals, and Med Administered. The default data for these fields are entered via the option Procedure Enter/Edit. If the procedure is not a Nuclear Medicine or Cardiology Studies procedure, then radiopharmaceuticals cannot be associated with it.

☞If a radiopharmaceutical and/or medication was stuffed during registration and then the procedure was later changed, the program will delete the stuffed data and display information messages on the screen.

### ☞Radiopharmaceutical Logic

The following radiopharmaceutical logic pertains only to those procedures that use radiopharmaceuticals. There are three parameters that work in conjunction to determine what prompts the user sees:

**Whether** the user is **asked** for radiopharmaceuticals,

**When** the user is **asked** for radiopharmaceuticals, and

**If** radiopharmaceuticals are **required** .

**Suppress Radiopharm Prompt** , edited via the option Procedure Enter Edit, determines **whether** or not the user is **asked** for a radiopharmaceutical. It can contain Always (0 or Null (no answer entered)) or Never (1) using the following definitions:

0 **Always** ( **same as Null** ) ask for Radiopharmaceutical if and when exam status parameters specify (this is the default).

1 **Never** ask (suppress the radiopharmaceutical prompts) or require Radiopharmaceutical even if exam status parameters specify that a Radiopharmaceutical should be entered. If default Radiopharmaceuticals are entered for the procedure they **will not** be automatically entered on the exam record by the system when the case is registered.

**Ask Radiopharms and Dosages?** (while in a specific status), edited via the option Examination Status Entry/Edit, can contain a YES ( **when** trying to progress to this status, **ask** it) or NULL (don't ask it).

**Radiopharms/Dosages Required?** , edited via the option Examination Status Entry/Edit, determines **if** entry of a radiopharmaceutical is **required** . It can contain either a YES (it is required) or NULL (it is not required). This determines whether it is required to progress to the status.

To suppress asking/requiring radiopharmaceuticals on an individual procedure, you must enter NEVER on the procedure field, Suppress Radiopharm Prompt. Status Tracking and Case Edit both skip radiopharmaceutical prompts if NEVER is entered. Status update logic will also skip over the radiopharmaceutical requirement if NEVER is in the field, even if the Exam Status, Radiopharms/Dosages Required?, parameters are set to YES. Also, Registration will **not** stuff default radiopharmaceuticals if NEVER is in that field, even if default radiopharmaceuticals have been entered on the procedure file. The Procedure Enter/Edit option will delete any default radiopharmaceuticals previously entered for this procedure if this field is NEVER.

### ☞Medication Logic

Medication logic pertains to all types of procedures. There are two parameters that work in conjunction to determine what prompts the user sees:

**Whether** the user is **asked** for medications, and

**When** the user is **asked** for medications.

**Prompt for Meds** (Rad/Nuc Med Procedure file #71, field #5), edited via the option Procedure Enter Edit, determines **whether** or not the user is **asked** for a medication.

**Ask Medications &amp; Dosages?** (Examination Status file #72, field #.27), edited via the option Examination Status Entry/Edit, can contain a YES ( **when** in this status, **ask** it) or NULL (don't ask it).

Medication prompts will only appear if both Ask Medications &amp; Dosages and Prompt for Meds are set to YES. Case Edits and Status Tracking both use Prompt for Meds, but Case Edits will always ask (and re-ask on additional edit sessions), whereas Status Tracking will only present the medication prompt for the appropriate status as set up in File #72. Medications do not affect status updates because they are **never** required.

### ☞Radiopharm Prescription &amp; Prescribing Physician/Dose Logic

This logic affects only those procedures that use radiopharmaceuticals. There is only one determining factor:

**Whether** the user is **asked** for the prescribing physician and prescribed dose.

Examination Status parameter fields concerning prescriptions for radiopharmaceuticals do not exist. A single field on the Rad/Nuc Med Procedure file #71, Prompt for Radiopharm RX, field #19, is used for determining prompting logic. During the Status Tracking session where the dose administered has been entered, Status Tracking will ask for prescription data only if Field #19 is set to YES. Once prescription data is entered, Status Tracking will no longer prompt for prescription data in subsequent edits; however, if only one prescription field (physician or dose) is entered, Status Tracking will continue to ask both fields at every subsequent edit session. Case edits will always ask for prescription data if Field #19 is set to YES. In both Case Edits and Status Tracking, a warning will continue to display if the dose administered is outside of the high/low range. Prescription data do not affect status updates because it cannot be required.

### Population of Imaging Exam Data

| **Patient Exam Data Field**                                                                                                                                | **Automatically**  **Entered**                                                                 | **Dx Code Edit**   | **Asked in Case Edits**                     | **Asked in Case Edits only if already populated**   | **Asked in Status Tracking if "Ask" param is set to YES**                 | **Cannot be**  **asked**  **in**  **Status Trking**   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|--------------------|---------------------------------------------|-----------------------------------------------------|---------------------------------------------------------------------------|-------------------------------------------------------|
| **Visit:**                                                                                                                                                 |                                                                                                |                    |                                             |                                                     |                                                                           |                                                       |
| Exam Date                                                                                                                                                  |                                                                                                |                    |                                             |                                                     |                                                                           | X                                                     |
| Type of Imaging                                                                                                                                            | When registered                                                                                |                    |                                             |                                                     |                                                                           | X                                                     |
| Hospital Division                                                                                                                                          | When registered                                                                                |                    |                                             |                                                     |                                                                           | X                                                     |
| Imaging Location                                                                                                                                           | When registered                                                                                |                    |                                             |                                                     |                                                                           | X                                                     |
| **Examinations:**                                                                                                                                          |                                                                                                |                    |                                             |                                                     |                                                                           |                                                       |
| Case Number                                                                                                                                                | When registered                                                                                |                    |                                             |                                                     |                                                                           | X                                                     |
| Procedure                                                                                                                                                  |                                                                                                |                    | X                                           |                                                     | X                                                                         |                                                       |
| Exam Status                                                                                                                                                | After each edit of case and report.                                                            |                    |                                             |                                                     |                                                                           | X                                                     |
| Category of Exam                                                                                                                                           | When registered                                                                                |                    | X                                           |                                                     |                                                                           | X                                                     |
|                                                                                                                                                            |                                                                                                |                    |                                             |                                                     |                                                                           |                                                       |
| Ward                                                                                                                                                       | When registered if inpatient                                                                   |                    |                                             | X                                                   |                                                                           | X                                                     |
| Service                                                                                                                                                    | When registered if inpatient                                                                   |                    |                                             | X                                                   |                                                                           | X                                                     |
| Bedsection                                                                                                                                                 | When registered if inpatient                                                                   |                    |                                             | X                                                   |                                                                           | X                                                     |
| Principal Clinic                                                                                                                                           | When registered if outpatient                                                                  |                    | If category = opt                           | X                                                   |                                                                           | X                                                     |
| Contract/Sharing Source                                                                                                                                    | When registered if entered on request                                                          |                    |                                             | Also asked if category = contract/sharing           |                                                                           | X                                                     |
| Research Source                                                                                                                                            | When registered if entered on request                                                          |                    |                                             | Also asked if category = research                   |                                                                           | X                                                     |
| Contrast Media Used                                                                                                                                        | When registered procedure is associated with contrast media, this field will default to “YES.” |                    | X                                           | Always Asked                                        | Always Asked                                                              |                                                       |
| Contrast Media                                                                                                                                             | When Contrast Media Used is YES, the user can edit the contrast media used for the exam.       |                    | Only Asked if ‘Contrast Media Used’ =”Yes”  | Only Asked if ‘Contrast Media Used’ =”Yes”          | Only Asked if ‘Contrast Media Used’ =”Yes”                                |                                                       |
| Imaging Order                                                                                                                                              | When registered                                                                                |                    |                                             |                                                     |                                                                           | X                                                     |
| Primary Interpreting Staff                                                                                                                                 |                                                                                                | If NOT a printset  |                                             |                                                     | If NOT a printset                                                         |                                                       |
| Secondary Interpreting Staff                                                                                                                               |                                                                                                | If NOT a printset  |                                             |                                                     | If NOT a printset                                                         |                                                       |
| Primary Interpreting Resident                                                                                                                              |                                                                                                | If NOT a printset  |                                             |                                                     | If NOT a printset                                                         |                                                       |
| Secondary Interpreting Residents                                                                                                                           |                                                                                                | If NOT a printset  |                                             |                                                     | If NOT a printset                                                         |                                                       |
| Primary Diagnostic Code                                                                                                                                    |                                                                                                | If NOT a printset  |                                             |                                                     | If NOT a printset                                                         |                                                       |
| Secondary Diagnostic Codes                                                                                                                                 |                                                                                                | If NOT a printset  |                                             |                                                     | If NOT a printset                                                         |                                                       |
| Requesting Physician                                                                                                                                       | When registered                                                                                |                    | X                                           |                                                     |                                                                           | X                                                     |
| Complication                                                                                                                                               |                                                                                                |                    | X                                           |                                                     |                                                                           | X                                                     |
| Complication Text                                                                                                                                          |                                                                                                |                    | When a complication is entered              |                                                     |                                                                           | X                                                     |
| Primary Camera/Equip/Rm                                                                                                                                    |                                                                                                |                    | If division param = YES                     |                                                     | X                                                                         |                                                       |
| Requested Date                                                                                                                                             | When registered                                                                                |                    |                                             |                                                     |                                                                           | X                                                     |
| Requesting Location                                                                                                                                        | When registered                                                                                |                    |                                             |                                                     |                                                                           | X                                                     |
| Visit                                                                                                                                                      | When complete                                                                                  |                    |                                             |                                                     |                                                                           | X                                                     |
| Dosage Ticket Printed?                                                                                                                                     | When printed                                                                                   |                    |                                             |                                                     |                                                                           | X                                                     |
| HL7 Examined Msg Sent?                                                                                                                                     | When sent                                                                                      |                    |                                             |                                                     |                                                                           | X                                                     |
| Film Size Data:                                                                                                                                            |                                                                                                |                    |                                             |                                                     |                                                                           |                                                       |
| Film Size                                                                                                                                                  | When registered if set up on procedure                                                         |                    | X                                           |                                                     | X                                                                         |                                                       |
| Amount (#films)                                                                                                                                            | When registered if set up on procedure                                                         |                    | X                                           |                                                     | X                                                                         |                                                       |
| Exam Status Times                                                                                                                                          |                                                                                                |                    |                                             |                                                     |                                                                           |                                                       |
| Status Change 	Date/Time                                                                                                                                                            | After each status change if division param = NO                                                |                    |                                             |                                                     | If division param = YES                                                   |                                                       |
| New Status                                                                                                                                                 | X                                                                                              |                    |                                             |                                                     |                                                                           | X                                                     |
| Computer User                                                                                                                                              | X                                                                                              |                    |                                             |                                                     |                                                                           | X                                                     |
| Activity Log                                                                                                                                               |                                                                                                |                    |                                             |                                                     |                                                                           |                                                       |
| Log Date                                                                                                                                                   | If division param = YES                                                                        |                    |                                             |                                                     |                                                                           | X                                                     |
| Type of Action                                                                                                                                             | X                                                                                              |                    |                                             |                                                     |                                                                           | X                                                     |
| Computer User                                                                                                                                              | X                                                                                              |                    |                                             |                                                     |                                                                           | X                                                     |
| Technologist  Comment                                                                                                                                      |                                                                                                |                    | X                                           |                                                     |                                                                           |                                                       |
| Modifiers                                                                                                                                                  | When registered, from request                                                                  |                    | X                                           |                                                     |                                                                           | X                                                     |
| Technologist                                                                                                                                               |                                                                                                | X                  | X                                           |                                                     | X                                                                         |                                                       |
| Medications                                                                                                                                                |                                                                                                |                    |                                             |                                                     |                                                                           |                                                       |
| Med Administered                                                                                                                                           | If procedure defaults set up                                                                   |                    | If procedure param for meds = YES           |                                                     | If procedure param for meds = YES                                         |                                                       |
| Med Dose                                                                                                                                                   |                                                                                                |                    | If procedure param for meds = YES           |                                                     | If procedure param for meds = YES                                         |                                                       |
| Date/Time Med 	Administered                                                                                                                                                            |                                                                                                |                    |                                             | X                                                   | If procedure param for meds = YES                                         |                                                       |
| Person Who 	Administered Med                                                                                                                                                            |                                                                                                |                    |                                             | X                                                   | If procedure param for meds = YES                                         |                                                       |
| Clinical History for Exam                                                                                                                                  | When registered, from request                                                                  |                    |                                             |                                                     |                                                                           |                                                       |
| Radiopharmaceuticals                                                                                                                                       |                                                                                                |                    |                                             |                                                     |                                                                           |                                                       |
| Radiopharms                                                                                                                                                | When registered, if procedure defaults set up                                                  |                    | If procedure param Suppress Radiopharm = NO |                                                     | If procedure param Suppress Radiopharm = NO                               |                                                       |
| Fields below are asked only if a radiopharm is entered. Radiopharms and related fields only apply to procedures of Nuclear Medicine or Cardiology Studies. |                                                                                                |                    |                                             |                                                     |                                                                           |                                                       |
| Prescribed Dose by 	MD Override                                                                                                                                                            |                                                                                                |                    | If procedure Rx param = YES                 |                                                     | If not already entered, and if procedure Rx param = YES                   |                                                       |
| Prescribing 	Physician                                                                                                                                                            |                                                                                                |                    | If procedure Rx param = YES                 |                                                     | If not already entered, and if procedure Rx param = YES                   |                                                       |
| Activity Drawn                                                                                                                                             |                                                                                                |                    |                                             | X                                                   | X                                                                         |                                                       |
| Date/Time Drawn                                                                                                                                            |                                                                                                |                    |                                             | X                                                   | X                                                                         |                                                       |
| Person Who 	Measured Dose                                                                                                                                                            |                                                                                                |                    |                                             | X                                                   | X                                                                         |                                                       |
| Dose Administered                                                                                                                                          |                                                                                                |                    | X                                           |                                                     | X                                                                         |                                                       |
| Date/Time Dose 	Administered                                                                                                                                                            |                                                                                                |                    | X                                           |                                                     | X                                                                         |                                                       |
| Person Who 	Administered Dose                                                                                                                                                            |                                                                                                |                    | X                                           |                                                     | X                                                                         |                                                       |
| Witness to Dose 	Administration                                                                                                                                                            |                                                                                                |                    | If procedure Rx param = YES                 |                                                     | If not already entered, and if procedure Rx param = YES                   |                                                       |
| Route of 	Administration                                                                                                                                                            |                                                                                                |                    |                                             | X                                                   | X                                                                         |                                                       |
| Site of 	Administration                                                                                                                                                            |                                                                                                |                    |                                             | X                                                   | X (unless no predefined sites for route, and Free Text site param is OFF) |                                                       |
| Site of Admin Text                                                                                                                                         |                                                                                                |                    |                                             | X                                                   | X                                                                         |                                                       |
| Lot No.                                                                                                                                                    |                                                                                                |                    |                                             | X                                                   | X                                                                         |                                                       |
| Volume                                                                                                                                                     |                                                                                                |                    |                                             | X                                                   | X                                                                         |                                                       |
| Form                                                                                                                                                       |                                                                                                |                    |                                             | X                                                   | X                                                                         |                                                       |


## 17 Outpatient Workload Crediting

### Imaging Stop Codes File 71.5

This file contains the stop codes that can be used by imaging services. They are determined by MAS, VA Headquarters. You can edit these stop codes via the option Valid Imaging Stop Codes Edit and delete any not used at your site. It provides the list of selections for stop codes assignment to Imaging Locations. Upkeep of this file is entirely up to you, the ADPAC. It is not a pointed-to file (meaning preservation of its data does not affect reports, etc.) therefore entries should be deleted if they don't need to be on the selection list.

### Invalid CPT/Stop Code List

The report option Invalid CPT/Stop Code List under the Procedure File Listings menu should be used as a tool to review the validity of procedure CPTs, Imaging Location setup, and several other "sanity checks". Warnings and errors on this report must be addressed in order to properly credit imaging workload at your facility.

This report shows any CPTs that are nationally inactive, missing, or have broken pointers. It prints warnings for Parent type procedures with no Descendents, and for detailed or series procedures with no AMIS code(s). The report will also tell you if there are any Imaging Locations with incorrect DSS IDs (i.e., Stop codes not in the Imaging Stop Codes file), and if an Imaging Location is not pointing to a Hospital Location file #44 entry marked as Occasion of Service.

### Valid Imaging Stop Codes Edit

All stop codes are determined by the Medical Administration Office in VA Headquarters which updates the contents of the Clinic Stop file #40.7 every October 1 via a software release. After IRM installs the software that updates that file, you can use the option Inquire to File Entries to get a listing of the entries in File #40.7 and check them against entries in your Imaging Stop Codes file #71.5. If there are any changes, you need to update File #71.5 by deleting the ones that have become obsolete and adding the codes that correspond to the imaging services done at your site via the option Valid Imaging Stop Codes Edit. **If you add new Stop Codes, it is your responsibility to first verify that the codes are recognized as valid for Imaging Services by MAS, VA Headquarters.**

### Location Parameter Edit

Whenever you use the Location Parameter Edit option to edit or set up an Imaging Location, the software automatically checks the "pointed to" entry in the Hospital Location file #44. You should see a short message such as "Location is OK" after editing. If the software detects a problem, it will attempt to correct the problem, possibly by creating a new File #44 entry for the Imaging Location to point to. This will happen if someone has erroneously entered appointment patterns for the File #44 location. If the Stop Codes don't agree, the Stop Code entry in File #44 will be overwritten to match the DSS ID entered by the Rad/Nuc Med ADPAC. If an error cannot be resolved by the software, you will see a message telling you to take some action. If the software can fix the problem, you will see a message telling you what was done.

### Options that can Potentially Trigger Crediting

Case No. Exam Edit

Edit Exam by Patient

Report Entry/Edit

On-line Verifying of Reports

Verify Report Only

Status Tracking of Exams

Update Exam Status

Diagnostic Code Entry by Case No.

Resident On-line Pre-Verification

Verify Batch

Report Entry through vendor supplied Voice Recognition Systems

### Crediting

1. Rad/Nuc Med sends data to the PCE (Patient Care Encounter) package whenever an exam's status progresses to Complete.

1. Using the option Mass Override Exam Status or Override a Single Exam Status to Complete does **not** result in any stop code or CPT crediting.

1. Crediting is only filed for outpatients.

1. The following data is mandatory for each case:

Detailed Procedure with a valid CPT code

Primary Interpreting Staff or Primary Interpreting Resident

Patient

Exam Date/Time

DSS ID

Requesting Location

1. The PCE package sends the Scheduling Package the crediting data that needs to be transmitted to .

1. If PCE accepts the Rad/Nuc Med crediting data, a value will be written to the Visit field #27 of the Rad/Nuc Med Patient file #70 on that case. If not, the failure bulletin is sent to recipients.

1. If descendent cases are registered for a given exam date/time, each case may be either Complete or Cancelled before data is sent to PCE.

### Errors

There is a bulletin (RAD/NUC MED CREDIT FAILURE) that can be used to notify a mail group of credit errors generated specifically through Radiology/Nuclear Medicine. Your IRM should set up a mail group that includes the ADPAC, or whoever will be responsible for researching and resolving crediting problems.

**Note:** For more information on outpatient crediting, please see the PCE and Scheduling documentation.

## 18 Troubleshooting

### On-line Verifying of Reports

The following is a chart using various parameter set-ups in the options Division Parameter Set-up and Classification Enter/Edit to show how On-line Verifying of Reports is affected. If selecting another physician's reports in on-line verifying is not working the way you feel it should, check this chart to see what you need to change.

| Division Parameter  Set-up  Allow Verifying by Residents   | Classifi-  cation Enter/Edit  Allow Verifying of Others   | Classification  Enter/Edit  Classification of User logged on   | Depending on parameters, the physician using on-line verification may or may not be allowed to select another physician's reports.  First prompts displayed when On-line Verifying of Reports is selected   |
|------------------------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Y                                                          | Y                                                         | Resident                                                       | Select Interpreting Physician*                                                                                                                                                                              |
| N                                                          | N                                                         | Resident                                                       | Interpreting Residents are not allowed to verify reports.                                                                                                                                                   |
| Y                                                          | N                                                         | Resident                                                       | Select one of the following:  1 Pre-verified...  2 Draft...  3 ...                                                                                                                                          |
| N                                                          | Y                                                         | Resident                                                       | Interpreting Residents are not allowed to verify reports.                                                                                                                                                   |
| Y                                                          | Y                                                         | Staff                                                          | Select Interpreting Physician                                                                                                                                                                               |
| N                                                          | N                                                         | Staff                                                          | Select one of the following:  1 Pre-verified...  2 Draft...  3 ...                                                                                                                                          |
| Y                                                          | N                                                         | Staff                                                          | Select one of the following:  1 Pre-verified...  2 Draft...  3 ...                                                                                                                                          |
| N                                                          | Y                                                         | Staff                                                          | Select Interpreting Physician                                                                                                                                                                               |

* The Select Interpreting Physician prompt allows the user to choose another physician and review that physician's reports. If this isn't the first prompt displayed, the user cannot edit another physician's reports.

**Physician Title on Reports** : The title that prints to the right of the physicians' names on the results report is taken from the New Person File #200 Signature Block Title field #20.3. So, if you find that incorrect titles are printing, have the user or IRM edit this field.

### Reports

Workload Reports: Please note that the separation of workload figures by imaging type supported in version 4.5 will take effect only on exams entered after the ADPAC activates the new imaging types. For example, if an exam was entered before the new imaging type was activated, the exam will be counted under its old imaging type. To include only exams entered after the new imaging types were activated, the beginning date entered at the date range prompts when generating the report must be after the date when the new imaging types were activated.

For most workload reports that are sortable/selectable by one-many-all, division and imaging type, the division totals page will only print if there is more than one imaging type in the division. If there is only one imaging type in the division, the imaging type total page is used for the division total.

The following reports calculate workload counts (i.e., exam counts, patient visit counts, and weighted work units) in a similar way:

Functional Area Workload Reports...

Clinic Report

PTF Bedsection Report

Service Report

Sharing Agreement/Contract Report

Ward Report

Special Reports...

Camera/Equip/Rm Report

Personnel Workload Reports...

Physician Report

Resident Report

Staff Report

Technologist Report

Transcription Report

Data must fall within the date range selected.

Exam Status file (#72) parameters are checked to see if the case's exam status is one that should cause the exam to appear on the report.

Exam status must have an Imaging Type the user has selected or defaulted to, and the exam's division must be one the user selected or defaulted to.

1. Checks the Category of Exam to identify the patient category (inpatient, outpatient, research, or other). The personnel reports identify the patient as an inpatient or outpatient. The functional reports identify the patient as an inpatient, outpatient, research, or other. The clinic report will ignore a case if the category is inpatient. The ward, bedsection, and service reports will ignore a case if the category is outpatient or other.

1. Ignores the case if the procedure does not exist in the Rad/Nuc Med Procedure file (#71). (This would mean there is a broken pointer type of data corruption problem in the record.) Theoretically, this shouldn't happen. If it does, it means that someone completely deleted a procedure.

1. Ignores the case if there are no AMIS codes associated with the procedure. (AMIS codes can be entered using the Procedure Enter/Edit option.)

1. Ignores the case on the Sharing Agreement/Contract report if the pointed to entry in the Contract/Sharing Agreements file (#34) does not exist. ("Does not exist" means there is a broken pointer type of data corruption, which happens when someone inadvertently deletes an entry from the Contract/Sharing Agreements file.) If no contract/sharing source was entered, the case is reported under other.

1. Calculates the weighted work units (WWUs). The AMIS Weight Multiplier field of the Rad/Nuc Med Procedures file contains a number (0-99) to indicate to the various workload report routines how many times to multiply the weighted work units associated with the AMIS code. The Weight for each AMIS code is stored in the Weight field of the Major Rad/Nuc Med AMIS Code file.

Most multipliers will be 1. However, there are some that are greater than 1. For example, a procedure called Upper GI and Small Bowel might have AMIS code 9-Gastrointestinal which has a Weight of 6 work units, and an AMIS Weight Multiplier of 2. Therefore, on the workload reports, the site will get credit for 12 weighted work units (WWUs) each time it is performed. If there are multiple AMIS codes for the procedure, each AMIS Weight Multiplier is multiplied by the AMIS weight, then the results are summed.

Below is a sample of the exam/procedure/AMIS data relationship. Using this sample, the WWUs for the exam would be 12, and the exam would count as 2 exams.

Rad/Nuc Med exam 		AMIS categories

data stored in	Procedures stored in	stored in

Rad/Nuc Med Patient	Rad/Nuc Med Procedures	Rad/Nuc Med Major

file #70:	file #71:	AMIS Codes file #71.1:

-----------------------------------	-----------------------------------------	 ---------------------------------

| Patient: Joe Veteran  Procedure: ----------------&gt;  Exam Modifiers: (none)   | Procedure:  **Upper GI**  AMIS codes data:  AMIS Code(s): -------------&gt;  AMIS Weight Multiplier:  **2**  Bilateral:  CT Head or Body:   | Desc: Gastrointestinal  Weight:  **6**   |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|

In the above example, this would be the calculation for Weighted Work Units: 6 X 2 = 12.

The modifiers (operating room, portable, and bilateral) have special meaning and cause increased counts. If the AMIS Weight Multiplier is less than 2, "bilateral" affects the WWUs by multiplying the AMIS Weight Multiplier by 2. The result is multiplied by the AMIS code's "Weight". In the sample above, if the procedure had been bilateral, WWUs would never have been affected. Here's step-by-step how it works:

It finds all the AMIS codes associated with each procedure. If no AMIS weight has been entered, the default is 1.

If bilateral (i.e., the procedure's "Bilateral" field is set to "YES" **or** a bilateral modifier was entered during exam ordering or case editing), the multiplier value (AMIS Weight Multiplier) is doubled.

For each AMIS code on the procedure, it multiplies the weight times the weight multiplier of each code, then sums the products (if more than one AMIS code on the procedure).

1. Increments the counts for division, Imaging Type report, procedure etc.

1. If more than one AMIS code exists for the procedure, the appropriate exam category count is incremented by one. If only one AMIS code for the procedure, increment the patient count by the weight multiplier.

1. Cases with more than one technologist, resident, and staff will be incremented accordingly with a message warning that the total number of exams and weighted work units will be higher in these personnel reports than the other workload reports.

1. WWUs are printed on all functional area reports, the Technologist Report, and the Camera/Equip/Rm Report. WWUs do not apply to the Physician, Resident, Staff and Transcription Reports.

Abnormal Exam Report: This report includes only those exams that have a Diagnostic Code whose "PRINT ON ABNORMAL REPORT" field in the Diagnostic Codes file #78.3 is set to "YES".

If several cases share one report (printset), then they will be printed together under the same patient and exam date/time.

Delinquent Status Report: There are times when an exam seems like it should be in the Complete status when it is actually in a Transcribed or lower status. The following steps describe how this might happen.

- A case is registered; the status is Waiting for Exam.
- The exam is completed quickly and images are sent to the radiologist or nuclear medicine physician before status tracking or case edit is used.
- The transcriptionist enters the report, but the status either cannot be upgraded because the case has not been edited by the technician or cannot be upgraded to the status immediately before Complete.
- The report is verified, but the technician still has not done case edit or status tracking, so the exam remains in some status lower than Complete.
- The technician now uses status tracking (not Case No. Edit or Edit Exam by Patient). Status tracking pushes the exam status to Examined (or whatever the next ordered status is) because it is designed to push the status to the next ordered status rather than the highest possible status.
- Status Tracking will display all higher status(es) for which this exam now qualifies. However, if the technician does not follow up with additional status tracking edits of the same case, the case stays in Examined or Transcribed (or whatever) and goes into the "black hole" until it shows up on the Delinquent Status report.

Another scenario circumstance that may cause the same finding:

If status tracking cannot account for incomplete cases, the other possibility is that an error occurred on a tasked job that was supposed to update the status. This is likely if there are very few occurrences. Since status update tasks call so many other programs, the error might not even show evidence to IRM that Radiology/Nuclear Medicine is responsible. This could be reconstructed based on log subfiles that are populated (if the logs are turned on) together with careful scrutiny of the error log that IRM can access.

Use the Delinquent Status report regularly to catch this infrequent happening.


## 20 Frequently Asked Questions

Many of the following questions were originally asked over E-Mail. Whenever you see quotes around a statement (some editing was necessary), it was lifted from actual questions and answers from the sites. We wanted to provide the user's viewpoint along with items of particular importance that we feel need to be discussed as often as possible. The following should be viewed as possible solutions to handle various conditions, but not necessarily the only way or the best solution at every site. When in doubt, consult with your hospital IRM Service.

### Imaging Types

**Question** : How do I deactivate an Imaging Type that we have been using?

**Answer** : Assigning an Imaging type not previously used to locations and procedures "activates" that Imaging Type. That causes workload reports for that Imaging Type to be separately reported. Imaging Types also affect the enter/edit options and screen displays. When a user signs on to the computer, s/he signs on under a specific location and Imaging Type which affects the data the user can see or edit.

Once an Imaging Type has been "activated" and used by registering cases to the associated location, it takes a great deal of effort and time to deactivate the Imaging Type.

If an Imaging Type is to be deactivated, these are the steps that must be taken. We'll use the example of wanting to deactivate Ultrasound (there may be one or more Ultrasound Imaging locations) and send everything to General Radiology.

1. First and foremost, **DO NOT DELETE THE IMAGING TYPE, LOCATION(S), OR ASSOCIATED PROCEDURES** . Whenever you have the urge to delete, remember that deletion causes loss of historical data and possible database corruption.
2. All procedures are associated with an Imaging Type. In our example scenario, any procedure with an Imaging Type of Ultrasound will need to be changed to an Imaging Type of General Radiology by using the option Procedure Enter/Edit. This must be done to prevent additional procedures from being registered in the Ultrasound location(s).
3. Sign on under each Ultrasound location (or use the Switch Locations option) and check for all pending cases for that location using the option Pending/Hold Rad/Nuc Med Request Log. Print a list of these for tracking purposes.
4. As patients arrive, sign on under the location(s) you want to send the pending cases to and register each of the cases at the selected location (in this case General Radiology locations). You can either use existing General Radiology locations or add a new one using the option Location Parameter Set-up. Over time, all the requests that were submitted to the Ultrasound location(s) should be registered in a General Radiology location.

1. You can use the Exam Status Display or Status Tracking of Exams options to find all cases in progress for the Ultrasound location(s). Close out, gradually, all the cases in the locations for the Imaging Type that will be deactivated.

### Procedures

1. **Question** : Can I edit the procedures?

**Answer** : Yes, you can edit the procedure. If the procedure has a CPT Code you cannot edit that procedure’s CPT Code, you can only edit the name field if the procedure was added by the site.

If no CPT Code is entered, the procedure type is automatically changed to "Broad". "Series" procedures may have multiple AMIS codes. A "Parent" procedure must have descendants.

If you want to use the same procedure in two different Imaging Locations with different Imaging Types, enter procedure names slightly differently but use the same CPT and AMIS codes.

1. **Question** : Explain the concept behind broad procedures.

"I know that they do not have associated CPT or AMIS codes. I gather that they are to be used PRELIMINARILY, and then changed to detailed procedures. Is this correct? This would seem to make sense only if a site is using remote on-line order requests (either OE/RR or from within the Radiology package)."

**Answer** : "...when ward/clinic clerks are transcribing written chart orders to V *IST* A, they are not always able to correlate the provider's written order to a Radiology Procedure found in the computer. Rather than halting the process and trying to find the provider for a further clarification, etc., a 'Broad' procedure may be ordered with an explanation in the Clinical History field."

1. **Question** : Is there any way to restrict users to only being able to request broad procedures?

"The main problem is that there are many similar procedures and requesting physicians usually will not know the difference between them. In fact, they CANNOT know what we will ultimately decide to do for the patient." "...I think the best option for Nuclear Medicine is to list only the broad procedures "bone scan", "renal scan", etc. Then WE will choose which detailed procedure to convert it to. This is one of the ways in which Nuclear Medicine needs differ from those of Radiology, since, as was mentioned, many of their procedures are straight forward enough so that the requester CAN be given a choice of the detailed procedure."

**Answer** : You can use the Rad/Nuc Med Common Procedure file to implement this. "Enter broad procedures as the only "active" ones in the Rad/Nuc Med Common Procedure file. That way, only the broad ones will be displayed when the ordering party sees the order screen."

"In addition, if your site is using OE/RR, then you should make sure the Quick Order protocols (if there are any set up) only use broad procedures. Although that wouldn't completely prohibit ordering of series and detailed procedures, people are much more likely to choose from what they can see on the screen."

1. **Question** : "When and how does the conversion from a request for a broad procedure to detailed or series take place?"

**Answer** : The conversion to a detailed or series procedure takes place at registration or during case editing and/or Status Tracking of Exams.

"When the patient is registered, (the Imaging Service) can clear up the murkiness by switching the order to Series or Detailed procedure."

"I would also assign a msg. (procedure message) to each of the Broad procedures that requests a Clinical History that spells out the exact exam they are looking for. This Clinical History could then be used, in conjunction with the expertise of the imaging department, to decide which Detailed procedures to switch to."

1. **Question** : When a physician orders a procedure, I want the physician to also see what the preps are for that procedure so the preps can be ordered at the same time. For instance, an angiogram should "show you how many IV units are needed for that test." How do I do that?

**Answer** : A message can be displayed with any radiology/nuclear medicine procedure. Build your message(s) using the option Procedure Message Entry/Edit. Then use the option Procedure Enter/Edit to assign the message(s) to the procedure. When ordering a procedure that has one or more messages, the message is displayed as soon as the procedure is selected.

### Case Numbers

1. **Question** : I have two active cases with the same case number. Will this be a problem?

**Answer** : A case number can be assigned to two different cases, although it normally should not happen. Case numbers for completed cases are reused so this is what has taken place:

- Case X is completed and its case number is reused by Case Y.
- Case Y is not completed yet when Case X is "Unverified", which reopens it with the same case number. Both cases are active and identified by the same case number.

This will not cause problems but may be confusing when attempting to pull up a record by its case number. In this situation, be sure to verify the name of the patient whose report you want to work with, to make sure you have the correct case.

1. **Question** : "Case numbers are reaching the ten thousands. Does this mean anything". In the past case numbers were usually two or three digits.

**Answer** : Case numbers for Completed cases are deleted each week and are then available for reuse. It appears that your cases are not reaching the status of Complete.

Using the option Examination Status Entry/Edit in the Utility Files Maintenance menu, check your exam statuses for Complete within each Imaging Type. Any item under Status Change Requirements that contains a YES is required data for a case to reach the status of Complete. Also check the Status Tracking Functions items; if data must be present for a case to reach Complete, then the user must be asked for that data. Here is an example of what you will find in that option. Note the data in **bold** print.

Examination Status Entry/Edit

Select an Imaging Type: nucLEAR MEDICINE

Select an Examination Status: COMPLETE Imaging Type: NUCLEAR MEDICINE

Order: 9

...OK? Yes// (Yes)

Name of Current Exam Status: COMPLETE//

Order in sequence of status progression: 9//

Should this Status appear in Status Tracking ?: NO

//

User Key needed to move an exam to this status:

Default next status for exam:

Can an exam be cancelled while in this status ?: NO

//

Generate exam alert for requesting physician ?: NO

//

Generate Examined HL7 Message:

**Status Change Requirements**

--------------------------

Please indicate which of the following is required

in order to place an exam into the 'COMPLETE' status:

**Technologist Required ?: YES//**

**Resident Or Staff Required ?: YES//**

**Detailed Procedure required ?: YES//**

**Film Entry Required ?: YES//**

**Diagnostic Code Required ?: NO//**

**Camera/Equip/Rm Required ?: YES//**

(Radiopharmaceutical requirements)

**Radiopharms &amp; Dosages required ?: YES//**

**Activity Drawn required (Radiopharm) ?: NO//**

**Drawn Dt/Time and Person required (Radiopharm) ?: NO//**

**Admin Dt/Time/Person required (Radiopharm) ?: NO//**

**Route/Site required (Radiopharm administered) ?: NO//**

**No. required (Radiopharm) ?: NO//**

**Volume/Form required (Radiopharm) ?: NO//**

WARNING: You must use the reporting feature of the system as

a prerequisite for the following requirements:

**Report Entered required ?: YES//**

**Impression required ?: YES//**

**Verified Report required ?: YES//**

**Status Tracking Functions**

-------------------------

Please indicate which of the following should be asked when

changing an exam's status to 'COMPLETE' while using

the 'status tracking' feature:

**Ask for Technologist ?: YES//**

**Ask For Interpreting Physician ?: YES//**

**Ask for Procedure ?: YES//**

**Ask For Film Data ?: YES//**

**Ask For Diagnostic Code ?: YES//**

**Ask For Camera/Equip/Rm ?: YES//**

**Ask for User Code ?: NO//**

**Ask Medications &amp; Dosages ?: YES//**

**Ask Medication Admin Dt/Time &amp; Person ?: YES//**

(Radiopharmaceutical functions)

**Ask Radiopharmaceuticals and Dosages ?: YES//**

**Ask Activity Drawn (Radiopharmaceutical) ?: YES//**

**Ask Drawn Dt/Time &amp; Person (Radiopharmaceutical) ?: YES//**

**Ask Admin Dt/Time &amp; Person (Radiopharmaceutical) ?: YES//**

**Ask Route/Site of Admin (Radiopharm) ?: YES//**

**Ask  No. (Radiopharm) ?: YES//**

**Ask Volume/Form (Radiopharm) ?: YES//**

Management Report Criteria

--------------------------

Please indicate which of the following workload reports should

include exams with the 'COMPLETE' status:

Clinic Report should include exams of this status ?: YES// ^

One site keeps on top of their Incomplete cases by running the Incomplete Exam Report within the Daily Management Reports menu several times a day. It helps them "to track down lost or misplaced films in order to get them read and also to see if a Technician accidentally forgot to case edit." They correct any errors daily.

### Requesting/Scheduling Requests

1. **Question** : Could someone provide a step-by-step procedure used for requesting/scheduling requests, complete with who does what?

**Answer** : The following is an example of the work flow at one VAMC:

1. Request comes to Radiology via .
2. Request goes into Waiting to be Scheduled bucket. (i.e., Request status = Pending)
3. Techs are responsible daily for scheduling their area (e.g. CT tech gets all CT requests, US gets  requests, etc.) All other requests go to the regular staff techs for scheduling.
4. Inpatients get called down the same day, unless they are for Fluoro or some other exam needing prep. Then they are given a date in the computer using the option Schedule a Request. **Note** : we do NOT give a time for inpatient appointments. They simply are ON CALL. As a rule, they are called first before our outpatients show up.
5. Outpatient requests are given a date and a time in the Schedule a Request option and also we go in to the Scheduling package under Make an Appointment and give it the same date and time. (Use of the Scheduling package is optional.)
6. All outpatients are printed appointment letters by the techs and our letters have the preps on them also. (Done through the Scheduling package)
7. If a patient calls and cannot come in, the tech puts the request on hold using the Hold a Request option and you can choose whatever reasons you want from your file. They also write on the request that the patient was unable to come. It then goes back to the Waiting to be scheduled bucket, and gets rescheduled as above with letters and all. If a patient fails to report, we do the same thing and give him another appointment.
8. If a patient fails to report two times, we use the option Cancel a Request and return the request to the attending physician.

"This makes it great because seldom are there any requests in a Pending status for very long, and you can easily see if you have missed someone. Also, once it is in a Scheduled status you can easily tell your workload for any given day, and also find out by date or by patient when a test is scheduled."

1. **Question** : How are routine requests handled for No Shows of patients that have called in for a re-appointment? Is there a way for the user to edit the desired/requested date of the request if the x-ray is desired on the day of the appointment?

**Answer** : "Under the Rad/Nuc Med Order/Entry menu you can schedule a request. It will list pending requests and you choose which ones you want to schedule, then it will prompt you for date and time desired. One thing, if these requests already have a schedule date, you must place them on hold first, then move to schedule."

1. **Question** : For those who are using the Schedule a Request option, do your "MAS people have it and are you keeping a suspense file for your hard copies of rescheduled requests?"

**Answer** : One site stated they use a suspense file: "The only reason we do is if the computer system should happen to go down, we can enter from the printed requests in our back-up system and continue business as usual without having to try to get patient charts for routine x-rays.

Another site had this to say: "We put the hard copies in an accordion type file for the day of the month it was scheduled. If a patient is a no show, we put the request on hold and reschedule it once if they fail to report a second time, we d/c the request with reason: Patient failed to report. "

1. **Question** : "Once the X-ray request has been scheduled, the scheduled date on the request cannot be changed. Correct?"

**Answer** : "Incorrect. You **can** change the scheduled date again, but it takes a few extra steps. If you have a request for which the scheduled date must be changed, use the Rad/Nuc Med Order/Entry menu and place the request on Hold (Hold a Request option). Then use the Schedule a Request option and enter the new date.

### Printing/Batching/Etc.

**Question** : "Is it possible to have Angiograms and Venograms queued to a printer in the Vascular Lab after the report has been transcribed?"

**Answer** : One view: "Are angios and venos done in a separate location? If so, they will print to the report printer assigned for that location. Or, you can Batch all the angios and venos in the same Batch, and then print this Angio/Veno Batch anytime to any printer.

Distribution Queues are for distribution of **verified reports** and are broken up by inpatient/outpatient/file room/etc. You wouldn't be able to get angios/venos broken out by using Distribution Queues."

Another view: "Your transcriptionists could use Batch names such as 'transcriptionist name/radiology section/date' or whatever scheme your folks feel comfortable with to distinguish the batches. Read up on Batches in the ADPAC manual, especially the management of same so you can set up a proper print/purge scenario at your VAMC that will get the job done but not allow the Report Batches file to grow too large."

**In addition to the above, we would like to stress the fact that verifying a report triggers its placement into the Distribution Queue. If a site leaves reports Released/Unverified, it will not be able to use the Distribution Queue.**

### Purging Records

1. **Question** : "Can anyone doing transcription within Radiology Service give me some input reference time frame for purging as follows:

Activity log cut off.

Report log cut off.

Clinical history cut off.

Tracking time cut off. (Exam status changes)

After the report goes the impression remains forever -- IRMS needs to get some purging done and I would sure like some input if possible from other stations."

**Answer** : There are many ways to handle purging. Here are a few of the examples from the sites:

1. We "have the report purge set to coincide with when we purge the film files. That is 5 years."
2. Activity log cut off	999 days

Report cut off	999 days

Clinical history	999 days

Tracking cut off	999 days

Order data cut off	 30 days

1. Activity log cut off	90days

Report cut-off	1825 days

Clinical History	90 days

Tracking time cut-off	90 days

Order data cut-off	30 days

1. "We started full purges of everything over a year old but have now moved to doing it every six months. Do be careful that you have ensured that impressions are supplied. We were getting a lot of 'Refer to report such-and-such' and, of course, it would have been purged too. You will only be able to purge those exams which are Complete, so there may be some clean up to do before you can proceed. If you're really timid, you could archive the global on tape, until you're confident of your procedure."

1. **Question** : What do you do with report text such as "See above" or "Refer to..." when purging?

**Answer** : One view: "A very important issue was raised. If you plan to purge report text after a period of time, leaving only the impression, make sure that the radiologists know this (and keep reminding them). I have seen many dictation where the impression read something like "As above", which obviously is not that helpful if "the above" has been deleted! In fact, you must specifically warn those who dictate not to do this."

Another view: "We use the Indicate No Purge option when the physician dictates the impression as "see above report". " **Note** : Transcriptionists need to be trained to do this.

### Verifying Reports

- **Question** : "I would like some input about who can Verify a report. Can it be only the radiologist who dictated and signed the report? Or can a radiologist sign other radiologists' reports?"

**Answer** : "Radiologists can verify their own reports and, if the site parameters are turned on, a radiologist may also be given the ability to verify other radiologists' reports."

1. **Question** : "How can I get the titles of contract radiologists to appear on the report without local modifications?"

**Answer** : "The Rad/Nuc Med software uses the Signature Block Title field in the New Person file #200 as the title printed to the right of each primary and secondary staff and resident's name. You can edit this field so that it shows that a person classified as Radiology/Nuclear Medicine resident or staff is a contract radiologist."

(See the Troubleshooting chapter for more detail)

### Hold/Cancelled/Pending/Scheduled

1. **Question** : Does anyone use the Pending/Hold Rad/Nuc Med Request Log (used to be Log of Pending Radiology Requests)?

**Answer** : "We use this list extensively. We also print it to each ward every evening at . The nurses love it . They can run down the list and make sure that patients that are to be NPO, are. We haven't had a miss in the last year. We also print to the lab a  each morning. They look for the CTs and Specials and draw these patients early. By the time the patient is ready to be done, the lab work is ready. It has really helped."

1. **Question** : "What do you do in the event the patient is Scheduled. These don't show up on a Pending report. We have so many patients scheduled and the floors "forget" to give the patients preps.

**Answer** : One site: "There is an option Log of Scheduled Requests by Procedure. We print one for us and each ward prints one daily (Ward/Clinic Scheduled Request Log) to prep the next day's patients. This will group GIs, CTs, BEs, Chests, etc. together and gives the patient name, SSN, procedure, patient location and time of appointment. For inpatients when we schedule a request we give date only with no time since they are On Call. We do give outpatients a time of course. Since we have instituted this, we have had little or no repeat preps, since all shifts have this option and it saved us work all around."

Another site: "We are on full ward and clinic order entry which includes scheduling. The wards just call for special things like BEs, IVPs, etc. and we give them a date, and they enter the request in the pending file for that date.

1. **Question** : "After you schedule a request, there should be a way of looking at it and seeing the time and date of the appointment. As it stands now, you can see that it is scheduled but unless you print out days forward, you cannot find the appointment."

**Answer** : "Go under Detailed Request Display either by patient or date. If you have ... given it a time and date, it will appear on the Detailed Request Display. Just select the # of the request (it will have an "s" in the column for status)". Enter Yes at the prompt "Do you wish to display request status tracking log?".

1. **Question** : How is workload credited for the Transcription Report?

**Answer** : The transcriptionist that initiates/creates the report is credited with the total number of lines regardless of how many transcriptionists may have contributed to the report. The length of each line is summed and divided by 75 to determine the total number of lines. The number of lines counted is always the current number of lines in the report. So, if lines have been added, changed, or deleted, only the final number of lines are counted at the time the Transcription Report is run.

### Doubling Workload Credit

**Question** : What is the effect of the modifier on special reports? When exactly is the workload credit doubled in the system?

**Answer** : The following reports do a calculation that will double workload counts if the Bilateral modifier is used and the AMIS weight multiplier associated with the procedure AMIS pair is 1 or "blank":

Physician Report [RA WKLPHY]

Resident Report [RA WKLRES]

Exam Room Report [RA WKLROOM]

Staff Report [RA WKLSTAFF]

Technologist Report [RA WKLTECH]

PTF Bedsection Report [RA LWKLBEDSEC]

Clinic Report [RA LWKLCLINIC]

Service Report [RA LWKLSERVICE]

Sharing Agreement/Contract Report [RA LWKLSHARING]

Ward Report [RA LWKLWARD]

Cost Distribution Report [RA CDR REPORT]

Film Usage Report [RA FILMUSE]

AMIS Code Dump by Patient [RA AMISDUMP]

AMIS Report [RA AMIS]

Detailed Procedure Report [RA WKLPROCEDURE]

### Effect of Portable and Operating Room Modifiers

**Question:** Which workload reports are affected and how?

**Answer:** The AMIS Report and the AMIS Code Dump by Patient are affected. In the AMIS Code Dump by Patient when an AMIS Code is selected all procedures not in that AMIS category are usually bypassed. However, if the user selects either AMIS category 25 (Operating Room) or 26 (Portable) then all exams that meet the other criteria, regardless of the AMIS code of the procedure performed, will be included if the exam contains an Operating Room or Portable type of modifier. Therefore, if an ankle x-ray (AMIS code 8) is done, and a modifier of the "Operating Room" type was entered for the exam, then that exam will show up under and AMIS Code Dump by Patient when AMIS code 25 is selected **and** when AMIS Code 8 is selected.

In the AMIS Report and Detailed Procedure Report (Detailed Procedure Workload Report) the same procedure described above would be counted under both AMIS code 8 and AMIS code 25.

### Complications

**Question** : "How would you delete a complication done months ago on an exam? This patient who has never had a reaction to contrast dye has a contrast reaction message come up when a CT is done."

**Answer** : Use the Update Patient Record option. Enter NO at the question Contrast Medium Allergy. The Adverse Reaction Tracking package will automatically create an 'Entered in Error record.

### Contracting Out

**Question** : "Is anyone contracting out mammograms and how are they handled through ?"

**Answer** :

One site: "Once the appointment is made, our scheduling clerk enters a request through  from the handwritten consult. When the results are mailed back, the study is registered in to get a case no. Under case edit, No Room used is entered along with No Films with a 0. After this is completed, the clerk then enters the report into the system from the copy stating at the beginning of the report that THIS STUDY WAS PERFORMED AT ... BY DRS., etc. The report is then verified. MRIs are handled the same way in order to make the reports for these exams readily available to the medical staff."

Another site: "We also indicate under category (IP, OP, etc.) that they are a contract source and the contractor's name. That way they are separated from the actual workload performed on site."

### Research

**Question** : "Is there any facility out there involved in X-raying body parts for research purposes?"

**Answer** : "We register any patient involved in research as a Research patient in the Exam Category field. We get credit for this in our CDR report."

### General Editing Helpful Hints

**Question** : "How can I keep text from wrapping when using the Screen Editor?"

**Answer** : On each new line, enter a space &lt;sp&gt; before entering the text as in the following example:

When ordering this procedure, we recommend the following steps be taken:

&lt;sp&gt;1) Do this first.

&lt;sp&gt;2) Next do this.

&lt;sp&gt;3) Etc.

**Question** : "How do I add a second identical entry in a field that accepts multiple entries?"

**Answer** : Enter the second, third, etc. entry in quotes as shown here:

Select DESCENDENTS: FOOT 2 VIEWS// ?

Answer with DESCENDENTS

Choose from:

ANKLE 2 VIEWS

FOOT 2 VIEWS

TOE(S) 2 OR MORE VIEWS

You may enter a new DESCENDENTS, if you wish

Enter a procedure name which is related to the parent procedure.

Select only active detailed or series procedures of the same

imaging type as the parent.

Answer with RAD/NUC MED PROCEDURES NAME, or CPT CODE, or SYNONYM

Do you want the entire RAD/NUC MED PROCEDURES List? n (No)

Select DESCENDENTS: FOOT 2 VIEWS// **"FOOT 2 VIEWS"**


## 22 ☞Stop Task (TaskMan)

One of the new features in this version is the ability of the user to stop tasks. All reports that can consume a significant amount of CPU/print time are now stoppable through the Stop Task action of the Taskman User [XUTM USER] option under the User's Toolbox [XUSERTOOLS] menu. The enhanced report logic checks for a stop flag during processing that is done before printing actually begins as well as during printing. You can get to this menu from any menu prompt in the Radiology/Nuclear Medicine software simply by typing TBOX. Here is an example of how it works. Note that TBOX is a Common Option under the menu.

Exam Entry/Edit Menu ...

Films Reporting Menu ...

Management Reports Menu ...

Outside Films Registry Menu ...

Patient Profile Menu ...

Radiology/Nuclear Med Order Entry Menu ...

Supervisor Menu ...

Switch Locations

Update Patient Record

User Utility Menu ...

Select Rad/Nuc Med Total System Menu Option: **??**

Exam Entry/Edit Menu ... [RA EXAMEDIT]

Films Reporting Menu ... [RA RPT]

Management Reports Menu ... [RA MGTRPTS]

Outside Films Registry Menu ... [RA OUTSIDE]

Patient Profile Menu ... [RA PROFILES]

Radiology/Nuclear Med Order Entry Menu ... [RA ORDER]

Supervisor Menu ... [RA SUPERVISOR]

Switch Locations [RA LOC SWITCH]

Update Patient Record [RA PTEDIT]

User Utility Menu ... [RA USERUTL]

You can also select a secondary option:

Rad/Nuc Med Total System Menu ... [RA OVERALL]

Radiology/Nuclear Med Order Entry Menu ... [RA ORDER]

Supervisor Menu ... [RA SUPERVISOR]

Utility Files Maintenance Menu ... [RA MAINTENANCE]

Or a Common Option:

TBOX User's Toolbox ... [XUSERTOOLS]

VA View Alerts [XQALERT]

Press 'RETURN' to continue, '^' to stop: **&lt;RET&gt;**

Continue [XUCONTINUE]

**&gt; Reverse lock ZZLUKE

Halt [XUHALT]

MailMan Menu ... [XMUSER]

Restart Session [XURELOG]

Time [XUTIME]

Where am I? [XUSERWHERE]

Select Rad/Nuc Med Total System Menu Option: **tbox** User's Toolbox

Display User Characteristics

Edit User Characteristics

Electronic Signature code Edit

Menu Templates ...

Spooler Menu ...

Switch UCI

TaskMan User

User Help

Select User's Toolbox Option: **task** Man User

Select TASK: **??**

Please wait while I find your tasks...searching...finished!

1: (Task #35437) DQ^RAFLH, DQ^RAFLH. Device LINE. POC,POC.

From  at , By you.

Waiting for device \_LTA1707:

-------------------------------------------------------------------------------

2: (Task #35591) ENTASK^RAMAINP, Rad/Nuc Med Active Procedures (Long).

Device LINE. POC,POC. From  at , By you. Unscheduled by you.

-------------------------------------------------------------------------------

3: (Task #35680) DQ^RAFLH, DQ^RAFLH. Device LINE. POC,POC.

From  at , By you. Unscheduled by you.

-------------------------------------------------------------------------------

4: (Task #35823) DQ^RAFLH, DQ^RAFLH. Device LINE. POC,POC.

From  at , By you. Unscheduled by you.

-------------------------------------------------------------------------------

5: (Task #35825) PRTORD^RAORDQ, PRTORD^RAORDQ. Device FIELD SUPPORT. POC,POC.

From  at , By you. Completed  at .

-------------------------------------------------------------------------------

6: (Task #35826) DQ^RAFLH, DQ^RAFLH. Device LINE. POC,POC.

From  at , By you. Unscheduled by you.

-------------------------------------------------------------------------------

Press RETURN to continue or '^' to exit: **^**

Select TASK: **1** DQ^RAFLH

Taskman User Option

Display status.

Stop task.

Edit task.

Print task.

List own tasks.

Select another task.

Select Action (Task # 35437): **stop** Stop task.

Task unscheduled and stopped.

Taskman User Option

Display status.

Stop task.

Edit task.

Print task.

List own tasks.

Select another task.

Select Action (Task # 35437): **&lt;RET&gt;**

Display User Characteristics

Edit User Characteristics

Electronic Signature code Edit

Menu Templates ...

Spooler Menu ...

Switch UCI

TaskMan User

User Help

Select User's Toolbox Option: **&lt;RET&gt;**

Exam Entry/Edit Menu ...

Films Reporting Menu ...

Management Reports Menu ...

Outside Films Registry Menu ...

Patient Profile Menu ...

Radiology/Nuclear Med Order Entry Menu ...

Supervisor Menu ...

Switch Locations

Update Patient Record

User Utility Menu ...

Select Rad/Nuc Med Total System Menu Option:

## 23 Glossary

| Active                                                                   | An order status that occurs when a request to perform a procedure on a patient has been registered as an exam, but before it has reached a status of Complete.                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Activity log                                                             | A log of dates and times data was entered and/or changed. The Radiology/Nuclear Medicine system is capable of maintaining activity logs for reports, exam status changes, imaging type parameter changes, purge dates, outside film registry activity, and order status changes.                                                                                                                                                                                                                                                                                                    |
| Alert                                                                    | Alerts consist of information displayed to specific users triggered by an event. For example, alerts pertaining to Rad/Nuc Med include the Stat Imaging Request alert, an Imaging Results Amended alert, and an Abnormal Imaging Results alert. The purpose of an alert is to make a user aware that something has happened that may need attention. Refer to Kernel and OE/RR documentation for more information about alerts.                                                                                                                                                     |
| AMIS code                                                                | For imaging, one of 27 codes used to categorize procedures, calculate workload crediting and weighted work units. AMIS codes are determined by VA Central Office and should not be changed at the medical centers.                                                                                                                                                                                                                                                                                                                                                                  |
| AMIS weight multiplier                                                   | A number associated with a procedure-AMIS code pair that is multiplied by the AMIS code weighted work units. If the multiplier is greater than 1, a single exam receives multiple exam credits.                                                                                                                                                                                                                                                                                                                                                                                     |
| Attending physician                                                      | The Radiology/Nuclear Medicine software obtains this data from the MAS package, which is responsible for its entry and validity. Refer to the Vist  *A*  MAS package documentation for more information and a description of the meaning of this term as it applies to V  *IST*  A.                                                                                                                                                                                                                                                                                                 |
| Batch                                                                    | In the Radiology/Nuclear Medicine system, a batch is a set of results reports. Transcriptionists may create batches to keep similar reports together and cause them to print together. One possible purpose might be to print all reports dictated by the same physician together.                                                                                                                                                                                                                                                                                                  |
| Bedsection                                                               | See PTF Bedsection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Bilateral                                                                | A special type of modifier that can be associated with an exam, a procedure, or an AMIS code. When an exam is bilateral due to one of the aforementioned associations, workload credit and exam counts are doubled for that exam on most workload and AMIS reports.                                                                                                                                                                                                                                                                                                                 |
| Broad procedure                                                          | A non-specific procedure that is useful for ordering when the ordering party is not familiar enough with imaging procedures to be able to specify the exact procedure that is to be performed. Before an exam status can progress to Complete, the imaging service must determine a more specific procedure and change the exam procedure to reflect the actual Detailed or Series procedure done. Depending on site parameters, broad procedures may or may not be used at a given facility. Also see Detailed and Series procedure.                                               |
| Bulletin                                                                 | A special type of mail message that is computer-generated and sent to a designated user or members of a mail group. Bulletins are usually created to inform someone of an event triggered by another user's data entry, or exam and request updates that require some action on the part of the bulletin recipient.                                                                                                                                                                                                                                                                 |
| CPT code                                                                 | See Current Procedural Terminology                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Camera/Equipment/Room                                                    | The specific room or piece of equipment used for a patient's imaging exam. Each is associated with one or more imaging locations. The Radiology/Nuclear Medicine system supports, but does not require users to record the camera/equipment/room used for each exam.                                                                                                                                                                                                                                                                                                                |
| Cancelled                                                                | A status that can be associated with an exam. Also see Discontinued.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Case number                                                              | A computer-generated number assigned to the record generated when one patient is registered for one procedure at a given date/time. Note that when multiple procedures are registered for a patient at the same date/time, each procedure will be given a different case number. Case numbers will be recycled and reused by a new patient/procedure/date instance when the exam attains a Complete status.                                                                                                                                                                         |
| Category of exam                                                         | For the purposes of this system, category of exam must be Outpatient, Inpatient, Contract, Sharing, Employee, or Research. Several workload and statistical reports print exam counts by category. Others use the category to determine whether exams should be included on the report.                                                                                                                                                                                                                                                                                             |
| Clinic                                                                   | Hospital locations where outpatients are cared for. In , clinics are represented by entries in the Hospital Location file (#44). Radiology/Nuclear Medicine Imaging Locations, represented by entries in the Imaging Location file (#79.1), are a subset of the Hospital Location file.                                                                                                                                                                                                                                                                                             |
| Clinical history                                                         | Data entered in the Radiology/Nuclear Medicine system during exam ordering and exam edit. Usually entered by the requesting party to inform the imaging service why the exam needs to be done and what they hope to find out by doing the exam.                                                                                                                                                                                                                                                                                                                                     |
| Clinical history message                                                 | Text that, if entered in system parameter setup, will always display when the user is prompted for clinical history. Generally used to instruct the user on what they should enter for clinical history.                                                                                                                                                                                                                                                                                                                                                                            |
| Common procedure                                                         | A frequently ordered procedure that will appear on the order screen. Up to 40 per imaging type are allowed by the system. Other active Rad/Nuc Med procedures are selectable for ordering, but only the ones designated as common procedures and given a display sequence number will be displayed prior to selection.                                                                                                                                                                                                                                                              |
| Complete                                                                 | A status that can be attained by an order or an exam.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Complication                                                             | A problem that occurs during or resulting from an exam, commonly a contrast medium reaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Contract                                                                 | A possible category of exam when imaging services are contracted out.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Contrast medium                                                          | A radio-opaque injectable or ingestible substance that appears on radiographic images and is helpful in image interpretation. It is used in many imaging procedures.                                                                                                                                                                                                                                                                                                                                                                                                                |
| Contrast reaction message                                                | A warning message that will display when a patient who has had a previous contrast medium reaction is registered for a procedure that uses contrast media. The message text is entered during Rad/Nuc Med division parameter setup.                                                                                                                                                                                                                                                                                                                                                 |
| Credit stop code                                                         | See Stop Code. Also see MAS package documentation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Current Procedural Terminology (CPT)                                     | A set of codes published annually by the American Medical Association which include Radiology/Nuclear Medicine procedures. Each active detailed or series procedure must be assigned a valid, active CPT code to facilitate proper workload crediting. In V  *IST*  A, CPT's are represented by entries in the CPT file #81.                                                                                                                                                                                                                                                        |
| Descendent                                                               | A type of Rad/Nuc Med procedure. One of several associated with a 'Parent' type of procedure. The descendent procedures are actually registered and performed. Also see Parent.                                                                                                                                                                                                                                                                                                                                                                                                     |
| Desired date (of an order)                                               | The date the ordering party would like for the exam to be performed. Not an appointment date. The imaging service is at liberty to change the date depending on their availability.                                                                                                                                                                                                                                                                                                                                                                                                 |
| Detailed procedure                                                       | A procedure that represents the exact exam performed, and is associated with a CPT code and an AMIS code.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Diagnostic code                                                          | Represented, for the purposes of this system, by entries in the Diagnostic Codes file (#78.3). Diagnostic codes describe the outcome of an exam, such as normal, abnormal. A case may be given one or more (or no) diagnostic code(s).                                                                                                                                                                                                                                                                                                                                              |
| Discontinued                                                             | An order status that occurs when a user cancels an order.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Distribution queue                                                       | A mechanism within the Radiology/Nuclear Medicine system that facilitates printing results reports at various hospital locations, such as the patient's current ward or clinic, the file room, and medical records.                                                                                                                                                                                                                                                                                                                                                                 |
| Division, Rad/Nuc Med                                                    | A subset of the Vist  *A*  Institution file (#4). Multi-divisional sites are usually sites responsible for imaging at more than one facility.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Draft                                                                    | A report status that is assigned to all Rad/Nuc Med results reports as soon as they are initially entered into the system, but before they are changed to a status of Verified or (if allowed) Released/Not Verified.                                                                                                                                                                                                                                                                                                                                                               |
| DSS ID                                                                   | Formerly Stop Code associated with each procedure, now DSS ID associated with each Imaging Location.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Electronic signature code                                                | A security code that the user must enter to identify him/herself to the system. This is required before the user is allowed to electronically verify Rad/Nuc Med reports. This is not the same as the Access/Verify codes.                                                                                                                                                                                                                                                                                                                                                          |
| Exam label                                                               | One of 3 types of labels that can be printed at the time exam registration is done for a patient. Also see jacket label, flash card.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Exam set                                                                 | An exam set contains a Parent procedure and its Detailed or Series descendent procedures. Requesting a Parent will automatically cause each descendent to be presented for registration as separate cases under a single visit date and time.                                                                                                                                                                                                                                                                                                                                       |
| Exam status                                                              | The state of an exam that describes its level of progress. Valid exam statuses are represented in this system by entries in the Examination Status file (#72). Examples are ordered, cancelled, complete, waiting for exam, called for exam, and transcribed. The valid set of exam statuses can, to a degree, be tailored by the site. There are many parameters controlling required data fields, status tracking and report contents that are determined when the parameters of this file are set up. There are separate and different set of statuses for requests and reports. |
| Exam status parameter setup                                              | See Exam status.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Exam status time                                                         | The date/time when an exam's status changes, triggered by exam data entry that can be done through over a dozen different options.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Film size                                                                | Represented by entries in the Film Sizes file (#78.4) in this system. Used to facilitate film use/waste tracking.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Flash card                                                               | One of 3 labels that can be generated at the time an exam is registered for a patient. The flash card was named because it can be photographed along with an x-ray, and its image will appear on the finished x-ray. Helpful in marking x-ray images with the patient's name, SSN, etc. to ensure that x-rays are not mixed up.                                                                                                                                                                                                                                                     |
| Footer                                                                   | The last lines of the results report, the format of which can be specified using the Lbl/Hdr/Ftr formatter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Format                                                                   | The specification for print locations of fields on a printed page. In this system, print formats can be specified using the Lbl/Hdr/Ftr formatter.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Header                                                                   | The top lines of the results report, the format of which can be specified using the Lbl/Hdr/Ftr formatter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Health Summary                                                           | Refers to a report or  software package that produces a report showing historical patient data. Can be configured to meet various requirements. Refer to the Health Summary documentation for more information.                                                                                                                                                                                                                                                                                                                                                                     |
| Hold                                                                     | An order status occurring when a user puts an order on hold, indicating that a study should not yet be done or scheduled, but that it will likely be needed in the future.                                                                                                                                                                                                                                                                                                                                                                                                          |
| Hospital location                                                        | Represented in  by entries in the Hospital Location file (#44). Rad/Nuc Med locations are a subset of the Hospital Location file.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Imaging location                                                         | One of a subset of Hospital Locations (See Hospital location) that is represented in the Imaging Location file #79.1, and is a location where imaging exams are performed.                                                                                                                                                                                                                                                                                                                                                                                                          |
| Imaging type                                                             | For the Rad/Nuc Med software, the set of valid imaging types is:  ANGIO/NEURO/INTERVENTIONAL  GENERAL RADIOLOGY  MAMMOGRAPHY  NUCLEAR MEDICINE  ULTRASOUND  VASCULAR LAB  CARDIOLOGY STUDIES (NUC MED)  CT SCAN  MAGNETIC RESONANCE IMAGING  These are the imaging types that are supported by this version of the software. Each imaging location and procedure may be associated with only one imaging type.                                                                                                                                                                      |
| Impression                                                               | A short description or summary of a patient's exam results report. Usually mandatory data to complete an exam. The impression is not purged from older reports even though the lengthier report text is.                                                                                                                                                                                                                                                                                                                                                                            |
| Inactivate                                                               | The process of making a record in a file inactive, usually by entering an inactive date on that record or deleting a field that is necessary to keep it active. When a record is inactive, it becomes essentially "invisible" to users. Procedures, common procedures, modifiers, and exam statuses can be inactivated.                                                                                                                                                                                                                                                             |
| Inactivation date                                                        | A date entered on a record to make it inactive. See Inactivate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Information Resources Management                                         | The service within VA hospitals that supports the installation, maintenance, troubleshooting, and sometimes local modification of Vist  *A*  software packages and the hardware that they run on.                                                                                                                                                                                                                                                                                                                                                                                   |
| Interpreting physician  (also Interpreting Resident, Interpreting Staff) | The resident or staff physician who interprets exam images.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| IRM                                                                      | See Information Resources Management.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Jacket label                                                             | One of the 3 types of labels that can be generated at the time an exam is registered for a patient. Usually affixed to the x-ray film jacket. (See also exam label, flash card.)                                                                                                                                                                                                                                                                                                                                                                                                    |
| Key                                                                      | See security key.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Label print fields                                                       | Fields that are selectable for printing on a label, report header, or report footer on formats that are designed using the Lbl/Hdr/Ftr formatter.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Lbl/Hdr/Ftr formatter                                                    | The name given to the option/mechanism that allows users to define formats for labels and for headers and footers on results reports. Users can specify which fields to print at various columns and lines on the label or report header/footer.                                                                                                                                                                                                                                                                                                                                    |
| Mode of transport                                                        | The patient's method of moving within the hospital, (ambulatory, wheelchair, portable, stretcher) designated at the an exam is ordered.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Modifier                                                                 | Additional information about the characteristics of an exam or procedure (such as bilateral, operating room, portable, left, right). Also see bilateral, operating room, portable.                                                                                                                                                                                                                                                                                                                                                                                                  |
| No purge indicator                                                       | A flag that can be set on the exam record to force the purge process to bypass the record. Guarantees that the record will not be purged when a historic data purge is scheduled by IRM. Also see Purge.                                                                                                                                                                                                                                                                                                                                                                            |
| Non-credit stop code                                                     | Certain stop codes, usually for health screening, that do not count toward workload credit. If a non-credit stop code is assigned to a procedure, another credit stop code must also be assigned. Also see Stop code.                                                                                                                                                                                                                                                                                                                                                               |
| OE/RR                                                                    | See Order Entry/Results Reporting.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| On-line verification                                                     | The option within the Radiology/Nuclear Medicine package that allows physicians to review, modify, and electronically sign patient result reports.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Operating room                                                           | A special type of procedure modifier, that, when assigned to an exam will cause the exam to be included in workload/AMIS reports under both the AMIS code of the procedure and under the AMIS code designated for Operating Room.                                                                                                                                                                                                                                                                                                                                                   |
| Order                                                                    | The paper or electronic request for an imaging exam to be performed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Order Entry                                                              | The process of requesting that one or more exams be performed for a patient. Order entry for Radiology/Nuclear Medicine procedures can be accomplished through a Rad/Nuc Med software option or through a separate Vist  *A*  package, Order Entry/Results Reporting (OE/RR).                                                                                                                                                                                                                                                                                                       |
| Order Entry/Results Reporting                                            | A Vist  *A*  package that performs that functions of ordering for many clinical packages, including Radiology/Nuclear Medicine.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Outside films registry                                                   | A mechanism in this system that allows users to track films done outside of the medical center. This can also be accomplished through the Vist  *A*  Records Tracking package. Refer to Records Tracking documentation for more information.                                                                                                                                                                                                                                                                                                                                        |
| Parent procedure                                                         | A type of Rad/Nuc Med procedure that is used for ordering purposes. It must be associated with Descendent procedures that are of procedure type Detailed and/or Series. At the time of registration the descendent procedures are actually registered. Setting up a parent procedure provides a convenient way to order multiple related procedures on one order. Parent/descendent procedure relationships must be set up ahead of time during system definition and file tailoring by the ADPAC.                                                                                  |
| Pending                                                                  | An order status that every Rad/Nuc Med order is placed in as soon as it is ordered through this system's ordering option. This system also receives orders from the Vist  *A*  OE/RR system and places them in a pending status.                                                                                                                                                                                                                                                                                                                                                    |
| Portable                                                                 | A special type of procedure modifier, that, when assigned to an exam will cause the exam to be included in workload/AMIS reports under both the AMIS code of the procedure and under the AMIS code designated for Portable.                                                                                                                                                                                                                                                                                                                                                         |
| Pre-verification                                                         | The process whereby a resident reviews a report and affixes his/her electronic signature to indicate that the report is ready for staff (attending) review, facilitated through an option in this system for Resident Pre-verification.                                                                                                                                                                                                                                                                                                                                             |
| Primary Interpreting Staff/ Resident                                     | The attending or resident primarily responsible for the interpretation of the case. (See also Secondary Interpreting Staff/Resident.)                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Primary physician                                                        | The Radiology/Nuclear Medicine software obtains this data from the MAS package, which is responsible for its entry and validity. Refer to the Vist  *A*  MAS package documentation for more information and a description of the meaning of this term as it applies to V  *IST*  A.                                                                                                                                                                                                                                                                                                 |
| Principal clinic                                                         | For the purposes of the Radiology/Nuclear Medicine system, this term is usually synonymous with 'referring clinic'. However, for the purposes of crediting, it is defined as the DSS (clinic/stop) code that is associated with the imaging location where the exam was performed                                                                                                                                                                                                                                                                                                   |
| Printset                                                                 | A printset contains a Parent procedure and its Detailed or Series descendent procedures. If the parent is defined to be a printset, the collection and printing of all common report related data between the descendants is seen as one entity.                                                                                                                                                                                                                                                                                                                                    |
| Problem draft                                                            | A report status that occurs when a physician identifies a results report as having unresolved problems, and designates the status to be Problem Draft. Depending on site parameters, a report may be designated as a Problem Draft due to lack of an impression. Also see Problem statement.                                                                                                                                                                                                                                                                                        |
| Problem statement                                                        | When a results report is in the Problem Draft status, the physician or transcriptionist is required to enter a brief statement of the problem. This problem statement appears on report displays and printouts.                                                                                                                                                                                                                                                                                                                                                                     |
| Procedure                                                                | For the purposes of this system, a medical procedure done with imaging technology for diagnostic purposes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Procedure message                                                        | Represented in this system by entries in the Rad/Nuc Med Procedure Message file (#71.4). If one or more procedure messages are associated with a procedure, the text of the messages will be displayed when the procedures is ordered, registered, and printed on the request form. Useful in alerting ordering clinicians and imaging personnel of special precautions, procedures, or requirements of a given procedure.                                                                                                                                                          |
| Procedure type                                                           | A characteristic of a Rad/Nuc Med procedure that affects exam processing and workload crediting. See Detailed, Series, Broad, and Parent.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| PTF Bedsection                                                           | See MAS documentation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Purge                                                                    | The process that is scheduled at some interval by IRM to purge historic computer data. In this system, purges are done on results report text, orders, activity logs, and clinical history.                                                                                                                                                                                                                                                                                                                                                                                         |
| Registration (of an exam)                                                | The process of creating a computer record for one or more patient/procedure/visit date-time instances. Usually done when the patient arrives at the imaging service for an exam.                                                                                                                                                                                                                                                                                                                                                                                                    |
| Released/not verified                                                    | A results report status that may or may not be implemented at a given medical center. Reports in this status may be viewed or printed by hospital staff outside of the imaging service.                                                                                                                                                                                                                                                                                                                                                                                             |
| Report batch                                                             | See Batch.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Report status                                                            | The state of a report that describes its progress level. Valid report statuses in this system are Draft, Problem draft, Released/not verified (if the site allows this status), and Verified. The status of a report may affect the status of an exam. Also see Exam status. Exams and requests each have a separate and different set of statuses.                                                                                                                                                                                                                                 |
| Request                                                                  | Synonymous with order. See Order.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Request status                                                           | The state of a request (order) that describes its progress level. Valid request statuses in this system are Unreleased(only if created through OE/RR), Pending, Hold, Scheduled, Active, Discontinued, and Complete. Reports and exams each have a separate and different set of statuses.                                                                                                                                                                                                                                                                                          |
| Request urgency                                                          | Data entered at the time an exam is ordered to describe the priority/criticality of completing the exam quickly (i.e. Stat, Urgent, Routine).                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Requesting location                                                      | Usually the location where the patient was last seen or treated (an inpatient's ward, or an outpatient's clinic). All requesting locations are represented by an entry in the Vist  *A*  Hospital Location file (#44). The requesting location may be, but is usually not an imaging location.                                                                                                                                                                                                                                                                                      |
| Requesting physician                                                     | The physician who requested the exam.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Research source                                                          | A research project or institution that refers a patient for a Radiology/Nuclear Medicine exam.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Scheduled                                                                | An order status that occurs when imaging personnel enter a date when the exam is expected to be performed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Secondary Interpreting Staff/Resident                                    | This generally refers to an attending/resident that assisted or sat in on review of the case, but is not primarily responsible for it. It may also be used to indicate a second reviewer of the case, for quality control or peer review purposes.                                                                                                                                                                                                                                                                                                                                  |
| Security key                                                             | Represented by an entry in the Vist  *A*  Security Key file. Radiology/Nuclear Medicine keys include RA MGR, RA ALLOC, and RA VERIFY. Various options and functionalities within options require that the user "own" a security key                                                                                                                                                                                                                                                                                                                                                 |
| Staff                                                                    | Imaging Attending.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Staff review (of reports)                                                | The requirement where an attending imaging physician is required to review the reports written by a resident imaging physician.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Standard report                                                          | Represented in this system by entries in the Standard Reports file (#74.1). Standard reports can be created by the ADPAC during system definition and set-up. If the division setup specifies that they are allowed, transcriptionists will be offered a selection of standard report text and impressions to minimize data entry effort.                                                                                                                                                                                                                                           |
| Status tracking                                                          | The mechanism within this system that facilitates exam tracking from initial states to the complete state. ADPACs must specify during exam status parameter setup which statuses will be used, which data fields will be required to progress to each status, which data fields will be prompted, and exams of which statuses will be included on various management reports.                                                                                                                                                                                                       |
| Stop code                                                                | Member of a coding system designed by VA Central Office to aid in determining workload and reimbursement of the medical centers. Stop codes are controlled by VA Central Office MAS. Imaging stop codes are represented by entries in the Valid Imaging Stop Code file #71.5. Imaging stop codes are a subset of the Vist  *A*  Clinic Stop file #40.7. See MAS documentation for more information.                                                                                                                                                                                 |
| Synonym                                                                  | In the Radiology/Nuclear Medicine package, synonyms are alternate terms that can be associated with procedures for the purposes of convenient look-up/retrieval. A given procedure may have more than one synonym, and a given synonym may be used for more than one procedure.                                                                                                                                                                                                                                                                                                     |
| Technologist                                                             | Radiology/Nuclear Medicine personnel who usually are responsible for performing imaging exams and entering exam data into the system.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Time-out                                                                 | The amount of time allowed before a user is automatically logged out of the system if no keystrokes are entered. This is a security feature, to help prevent unauthorized users from accessing your Vist  *A*  account in case you forget to log off the system or leave your terminal unattended.                                                                                                                                                                                                                                                                                  |
| Transcribed                                                              | An exam status that may occur when a results report is initially entered into the system for an exam. If this status is not activated at the site, it will not occur.                                                                                                                                                                                                                                                                                                                                                                                                               |
| Unreleased                                                               | An order status that occurs when an exam order is created, but no authorization to carry out the order has been given. This is possible only if the order is created through the OE/RR software.                                                                                                                                                                                                                                                                                                                                                                                    |
| Verification                                                             | For the purposes of this system, the process of causing a results report to progress to the status of Verified. This happens when a physician affixes his/her electronic signature to the report, or when a transcriptionist, with the proper authorization, enters the name of a physician who has reviewed and approved a report. This is analogous to a physician signing a paper report.                                                                                                                                                                                        |
| Verified                                                                 | A results report status that occurs at the time of verification. A report is verified when the interpreting physician electronically signs the report or gives his/her authorization that the report is complete and correct. Also see Verification.                                                                                                                                                                                                                                                                                                                                |
|                                                                          | Veterans Health Information Systems and Technology Architecture. Formerly known as DHCP.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Waiting for exam                                                         | An exam status that occurs as soon as the exam is first registered. The system automatically places all exams in this status upon registration.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Ward                                                                     | The hospital location where an inpatient resides. In V  *IST*  A, wards are a subset of the Hospital Location file (#44).                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Weighted work unit                                                       | The number that results from multiplying the weight of a procedure's AMIS code with the procedure's AMIS weight multiplier for that AMIS code. If a procedure has more than one AMIS code, the multiplication is done for each and the results are summed.                                                                                                                                                                                                                                                                                                                          |
| Workload credit                                                          | A general term that can refer to either the CPT type of workload credit that is used in the VA to calculate reimbursement to medical centers for work done, or the AMIS crediting used by the AMIS workload system.                                                                                                                                                                                                                                                                                                                                                                 |

## 24 Index

## A

Abnormal Alert	VII-6

Abnormal Exam Report	VII-6, XV-5

Abnormal Report	III-2, III-5

Access Erroneous Reports	III-3

Activation of exam status	VII-19

Active Procedure List (Long)	VIII-19, VIII-24

example	VIII-24

Active Procedure List (Short)	VIII-19, VIII-25

example	VIII-25

Activity Drawn

exam status	VII-16

Activity Drawn Required (Radiopharm)	II-6, VII-13

Add Exams to Last Visit	III-4, VII-60, XII-5

Add/Remove Report from Batch	III-4

Admin Dt/Time/Person Required (Radiopharm)	II-6, VII-13

Adverse reaction tracking	VII-2

Alert

exam status	VII-10

stat request	II-4

Allergy

contrast media	VII-2

Allow Batching of Reports	V-5

Allow Copying of Reports	V-5

Allow E-Sig on COTS HL7 Rpts	V-7

Allow Released/Not Verified	II-3, V-6, V-24

Allow Rpts on Cancelled Cases	V-6

Allow Standard Reports	VII-81

Allow Verifying by Residents	V-6, XV-1

Allow Verifying of Others	V-6, XV-1

Alpha Listing of Active Procedures	VIII-19, VIII-26

example	VIII-26

Alphabetical listing of active procedures	VIII-26

AMIS	VII-2

category	XVI-12

code(s)	XIV-1

contrast media use determined by	VII-2

credit indicator	VII-76

VACO	VII-42

weight	XV-3

weight	VII-42

weight multiplier	XV-3

workload report	XV-3

AMIS Code	VII-65, XVI-12

AMIS Code Dump by Patient	III-5, XVI-12

AMIS Report	III-5, VII-42, VII-61, XVI-12

AMIS reports	VII-31

AMIS Weight Multiplier	VII-65

AMIS Workload Report

exam status	VII-17

Appears on Status Tracking

field	VII-9

Ask Activity Drawn (Radiopharmaceutical)	II-6, VII-16

Ask Admin Dt/Time &amp; Person (Radiopharmaceutical)	II-6, VII-16

Ask 'Camera/Equip/Rm'	V-4

Ask Drawn Dt/Time &amp; Person (Radiopharmaceutical)	II-6, VII-16

Ask Exam Status Time	V-4

Ask for Camera/Equip/Rm	VII-15

Ask for Diagnostic Code	VII-15

Ask for Film Data	VII-15

Ask for Interpreting Physician	VII-14

Ask for Procedure	VII-14

Ask for Technologist	VII-14

Ask for User Code	VII-15

Ask Imaging Location	II-4

Ask Lot No. (Radiopharm)	II-6, VII-16

Ask Medication Admin Dt/Time &amp; Person	II-5, VII-15

Ask Medications &amp; Dosages	II-5, VII-15

case edits/status tracking	XIII-3

Ask Radiopharmaceutical

case edits/status tracking	XIII-2

field	VII-13, VII-16

Ask Radiopharmaceuticals and Dosages	II-5, II-6, VII-15

Ask Radiopharms and Dosages

case edits/status tracking	XIII-3

Ask Route/Site of Admin (Radiopharm)	II-6, VII-16

Ask Volume/Form (Radiopharm)	II-6, VII-16

Auto E-Mail to Req. Phys?	II-3, V-7

## B

Barcoded Procedure List	VIII-19, VIII-27

example	VIII-27

Batch names	XVI-8

Batching reports	V-5

Bilateral	VII-76

effect on workload reports	XV-3

Bilateral procedure	VII-66

Broad procedures	VII-61, XVI-2

suggested use of	XVI-3

Bulletin

crediting failure	XIV-3

Bulletins	II-11

## C

Called for Exam	VII-8

Camera/Equip/Rm	V-23

required	V-4

worksheet	XI-3

Camera/Equip/Rm Description	V-18

Camera/Equip/Rm Entry/Edit	V-1, V-18, V-23

example	V-18

Camera/Equip/Rm Required	VII-12

Camera/Equipment/Room	V-18, V-20

Cameras/equip/rooms used by this location	V-23

Can an Exam be Cancelled while in this Status	VII-10

Cancel a Request	III-3, XVI-7

Cancel an Exam	III-4

Cancelled	VII-8, XVI-10

Cancelled cases	V-6

Cancelled exams	VII-17

Case edit	XIII-1, XVI-3

Case Edits and Status Tracking	II-5

Case No. Exam Edit	III-4, VII-2, VII-7, VII-31, VII-60, XIV-2

Case number

exceptionally high	XVI-4

processing to completion	XVI-4

reuse/recycling of	XVI-4

same on two active cases	XVI-4

Category of exam

effect on workload reports	XV-3

CDR report	XVI-13

Check list	I-1, II-1, II-10

Cine film	VII-31

Classification

worksheet	XI-7

Classification Enter/Edit	II-11, III-1, VI-1, VI-2, XV-1

example	VI-2

Classification of user	XV-1

Clerical List	VI-1, VI-6

Clerk	VI-2

Clinic Report	XV-2, XVI-12

Clinic Stop file	XIV-1

Clinic Workload Report

exam status	VII-17

Clinical history	V-6

for broad procedure request	XVI-3

Clinical History Message	V-2, V-3

Common Data for Printsets	XII-1

Common procedure	XVI-3

imaging type, by	VII-50

Common Procedure Enter/Edit	VII-49, VII-50

example	VII-51

Common Procedure List	VII-50, VII-60

Complete exams	VII-17

Complete status	V-6, VII-8

Complication	XVI-13

Complication Report	III-2, III-5, VII-3

Complication Type Entry/Edit	VII-1, VII-2, VIII-2

example	VII-2

Complication Type List	VII-2, VIII-1, VIII-2

example	VIII-2

Contract radiologists	XVI-10

Contract/Sharing	VIII-44

Contract/Sharing Agreements file	XV-3

Contract/Sharing Source	VII-80

Contracting out	XVI-13

Contrast Medium Allergy	XVI-13

Contrast medium reaction	VII-2

Contrast Medium Reaction	VII-3

Contrast reaction	XVI-13

correction of erroneous	XVI-13

Contrast Reaction	VII-2

Cost Distribution Report	XVI-12

Cost of Procedure Enter/Edit	VII-57, VII-59

CPRS Interface for Printsets	XII-5

CPT

nationally active	VIII-31

CPT codes

invalid/missing	XIV-1

Create a Batch	III-3

Create OE/RR Protocol	VII-51

Create OE/RR Protocol from Common Procedure	VII-49, VII-51, VII-55

example	VII-55

Credit clinic stop codes	VIII-31

Credit failure	V-10

Credit Method	V-26

Interpretation Only	V-26

No Credit	V-26

Regular	V-26

Technical Component Only	V-26

Crediting	V-26

required data	XIV-2

workload	VII-42, VII-76, VII-83

workload	XIV-1

Crediting workload	VII-76

## D

Daily Log Report	III-5

Daily Management Reports	XVI-6

Daily Report	III-2

Data Inconsistency Report for Exam Statuses	VII-26

Date/Time of dose administration

exam status	VII-16

Date/Time of measure

exam status	VII-16

Default (Flash Card, Jacket Label, Exam Label) Format	V-22

Default Exam Label Format	VII-37

Default Flash Card Format	VII-37

Default Form	VII-65

Default Jacket Label Format	VII-37

Default Med Dose	VII-63

Default Medication	II-8, VII-63

associated with a procedure	VII-63

Default Next Status	VII-10

Default Next Status for Exam	VII-9

Default Radiopharmaceutical	II-8

associated with a procedure	VII-64

form	II-8

high dose	II-8

low dose	II-8

route	II-8

usual dose	II-8

Default Report Footer Format	V-22

Default Report Header Format	V-22, VII-37

Default Responses	XIII-1

Delete a Report	III-3

Delete Printed Batches	III-4

Delete Printed Batches by Date	III-3

Deletion of stuffed data	XIII-2

Delinquent Status Report	III-5, VII-17

exam status	VII-18

Descendent procedures	VII-67, XIV-1

Detailed	VII-60

Detailed procedure entry

example	VII-69

Detailed Procedure Report	XVI-12

Detailed Procedure Required	VII-12

Detailed Procedure Workload Report	XVI-12

exam status	VII-18

Detailed procedures	XVI-2

stuffed /default responses	XIII-2

Detailed Request Display	III-4, XVI-11

Device Specifications for Imaging Locations	V-23

Dflt Route of Administration	VII-65

Dflt Site of Administration	VII-65

Diagnostic Code and Interpreter Edit by Case No.	II-1

Diagnostic Code Enter/Edit	VII-1, VII-4, VIII-3

example	VII-5

inactive	II-5

Diagnostic Code Entry by Case No.	III-4, XIV-2

Diagnostic Code List	VIII-1, VIII-3

example	VIII-3

Diagnostic Code Required	VII-12

Diagnostic codes	VII-4, XVIII-4

abnormal results	VII-4

system, include in	VII-4

triggering alerts	VII-4

Diagnostic Codes file

Inactive field	VII-4

Display a Rad/Nuc Med Report	III-3

Display Common Procedure List	VII-49, VII-51, VII-56

example	VII-56

Display Educational Description	II-8

Display Educational Description When Ordered	VII-68

Display Patient Demographics	III-3

Display Rad/Nuc Med Procedure Information	III-3

Distribution queue	XVI-8

multiple active	VII-79

Reports Distribution Edit option	VII-77

Distribution Queue

Report Distribution Lists	VIII-43

report verification triggering entry into	XVI-8

Distribution Queue Menu	III-3

Division	I-1, III-1, V-2, V-21

Division Parameter Set-up	I-1, II-10, V-1, V-2, V-27, XV-1

affecting case edits/status tracking	XIII-1

Division parameters

changes to	V-10

changes, when they take effect	V-10

example	V-10

worksheet	XI-1

Dosage ticket	VII-18

exam status	VII-18

Doubling workload credit	XVI-11

Downtime	II-2

Draft Report	III-4

Drawn Dt/Time and Person Required (Radiopharm)	II-6, VII-13

DSS ID	V-26, XIV-1, XIV-2

workload crediting	VII-83

Duplicate Flash Card	III-4

DX200 Radiopharmaceuticals, Diagnostic	II-1, II-10

DX201 Imaging Agents (in vivo), Radiopharmaceuticals	II-1, II-10

DX202 Non-Imaging Agents Radiopharmaceuticals	II-1, II-10

## E

Edit Exam by Patient	III-4, VII-2, VII-7, XIV-2

Editing Data	XII-4

Educational Description	II-8, VII-68

Electronic signature	VI-2

Enter Last Past Visit Before Vist *A	III-3*

Exam Category	XVI-13

Exam Deletion	III-3

Exam labels	V-21, V-22

Exam Profile (selected sort)	III-3

Exam registration	V-24

Exam Room Report	XVI-12

Exam status

activation of	VII-8, VII-19

alert	VII-10

cancelled	VII-7, VII-8, VII-9

complete	VII-7, VII-8, VII-9

dosage ticket	VII-18

effect on workload reports	XV-3

exported setup	VII-18

HL7 message	VII-10

medications	VII-15

parameters	II-7

radiopharmaceutical functions	VII-15

Radiopharmaceuticals requirements	VII-12

waiting for exam	VII-7, VII-8, VII-9

Exam Status	V-4, V-6

Exam Status Display	III-4, XVI-2

Exam Status Display/Tracking options	III-2

Exam Status Tracking	VII-60

Examination Statistics	III-5

Examination status	V-4

parameters	V-4

worksheet	XI-9

Examination Status	VII-8

Examination Status Entry/Edit	II-5, II-6, II-10, V-4, VII-1, VII-7, VIII-5, XVI-4

affecting case edits/status tracking	XIII-1

suggested entries	VII-19

Examination Status file	V-4, VII-7

Examination Status List	VIII-1, VIII-5

example	VIII-5

Examination status parameters	V-4, V-6

Examined	VII-8

Examined status for Nuclear Medicine

example	VII-23

## F

Film Entry Required	VII-12

Film Sizes List	VIII-1, VIII-10

example	VIII-10

Film Type	VII-67

Film Type Entry/Edit	VII-1, VII-31, VIII-10

example	VII-31

Film Usage Report	VII-31, VII-32, XVI-12

Film Usage Workload Report

exam status	VII-17

Films Reporting Menu	VII-81

Flash card formatter

example of set-up	VII-39

Flash card, jacket labels, exam label parameters	V-21

Flash cards	I-1, V-7, V-10, V-21, V-22

Footers

results reports	VII-34

Frequently asked questions	XVI-1

Functional Area Workload Reports	III-5

Future Registration	V-5

## G

Generate Exam Alert for Requesting Physician	VII-10

Generate Examined HL7 Message	II-5, VII-10

## H

Header/Footer formatter

example of set-up	VII-39

Headers

results reports	VII-34

Health screening stop codes	XIV-1

Health Summary Type file	VII-62

Health Summary with Request	VII-62

High Adult Dose	VII-64

HIST Display Rad/NM Procedure Contrast Media History	VIII-20

HL7 Interface	XII-3

HL7 message	VII-10

Hold	XVI-10

Hold a Request	III-3, XVI-7, XVI-8

Hospital Location file	V-9, V-12, V-13, V-21, V-27, XVIII-3, XVIII-6, XVIII-12, XVIII-14

Occasion of Service entry	XIV-1

Pattern Date field	V-9

Type field	V-9, V-21

Hospital Location Type, prompt	V-21

How Many (Flash Cards, Jacket Labels, Exam Labels) per Visit	V-22

How Many Jacket Lbls Per Visit	V-10

## I

Imaging location	II-11, V-9, V-18, V-21

access	II-11

assignment to users	II-11

Imaging Location	I-1, VII-51

assignment to users	VI-2

Imaging location access

when changes take effect	VI-2

Imaging Location Access	VI-2

Imaging location, inactivation of	V-24

Imaging locations

data corruption due to deletion of	XVI-1

new	V-9

Imaging locations associated with division	V-9

Imaging Locations file	V-9, VII-37

Imaging stop codes	VIII-31, XIV-1

Imaging Stop Codes file	V-26

Imaging type	I-1, III-1, V-2, VII-8

activation of	XVI-1

associating a procedure with	VII-60

common procedure, by	VII-50

data corruption due to deletion of	XVI-1

deactivating of	XVI-1

exam status	VII-7

examination status	VII-7

modifier screening by	VII-75

Nuclear Medicine	II-6

procedures associated with	XVI-1

sign-on definition of	XVI-1

Imaging Type file	VII-19

Implementation check list	II-1

Impression	V-2, VII-14

common problem in data entry of	XVI-9

Impression Required	VII-14

Impression Required on Reports	V-6

Impressions	XVI-9

Inactivate	VII-50

Inactivation Date

associated with a procedure	VII-68

Inactivation of Imaging Location	V-24

Inactive

Diagnostic Code Enter/Edit	II-5

Inactive Procedure List (long)	VIII-30

example	VIII-30, VIII-41

Inactive Procedure List (Long)	VIII-19

Inactive procedures	VIII-31, VIII-33

Incomplete cases	XVI-6

Incomplete Exam Report	III-5, XVI-6

Indicate No Purge	XVI-10

Indicate No Purging of an Exam/Report	III-4

Inquire to File Entries	XIV-1

Inquire to File Options	III-3

Installation check	I-1, II-1, II-10

virgin install	I-1

virgin install	II-10

Institution file	V-2

Interpreting physician	XV-1

Interpreting Resident	VI-2

Interpreting Resident List	VI-1, VI-6

Interpreting residents	XV-1

Interpreting Staff	VI-2

Interpreting Staff List	VI-1, VI-6

Invalid CPT/Stop Code List	VIII-19, VIII-31, XIV-1

example	VIII-31

Invalid locations	V-9

## J

Jacket labels	I-1, V-10, V-21, V-22

Jacket Labels	III-3

## L

Lab work	XVI-10

Label formatter

example of set-up	VII-39

Label Print Fields file	VII-37

Label/Header/Footer Format List	VIII-11

example	VIII-11

Label/header/footer formats	I-1

Label/Header/Footer Formatter	II-7, V-22, V-28, V-29, VII-1, VII-34, VIII-11

example	VII-39

new fields	II-7

Label/Header/Footer List	VIII-1

Labels, Headers, Footers	XII-4

Lbl/Hdr/Ftr formats	XVIII-8

flash card	XVIII-6

footer	XVIII-6

format	XVIII-6

header	XVIII-6

List Exams with Inactive/Invalid Statuses	III-3

List of active procedures

short	VIII-25

List of Cameras/Equip/Rms	V-1, V-20

List of inactive procedures	VIII-30

List of Inactive Procedures (Short)	VIII-19, VIII-33

example	VIII-33

List of invalid CPT or stop codes	VIII-31

List of series of procedures	VIII-41

List Reports in a Batch	III-3

Listing of all active procedures	VIII-24

Location	I-1, III-1, V-2, V-21

Location Parameter List	V-1, V-33

example	V-33

Location Parameter Set-up	I-1, II-3, II-10, V-1, V-21, VII-38, XVI-2

camera/equip/rm, associated	V-18

example	V-27

Location Parameter Set-Up	V-10

Location parameters	V-10

when changes take effect	V-27

worksheet	XI-4

Location Set-up Parameters	VII-37

Log of Scheduled Requests by Procedure	III-4, XVI-11

Long Case Number Barcode	II-7

Lot (Radiopharmaceutical) Number Enter/Edit	VII-43, VII-44, VII-47

example	VII-44

Lot (Radiopharmaceutical) Number List	VIII-14, VIII-15

Lot No. Required (Radiopharm)	II-6, VII-13

Lot Number Enter/Edit	II-8

Low Adult Dose	VII-64

## M

Maintenance Files Print Menu	II-11, III-3, VII-1, VIII-18

Major AMIS Code Entry/Edit	VII-1, VII-42, VIII-12

example	VII-42

Major AMIS Code List	VIII-1, VIII-12

example	VIII-12

Major AMIS Codes file	VII-65

Major Rad/Nuc Med AMIS Code file	VII-65

Management report criteria

exam status	VII-16

status tracking	VII-16

Margin, left	V-23

Mass Override Exam Status	III-4

Medication Logic

case edits/status tracking	XIII-3

Medications

associated with a procedure	VII-62

exam status	VII-15

Message	VII-67

Missing or invalid CPTs	VIII-31

Modifier List	VIII-1, VIII-13

example	VIII-13

Modifiers	VII-51

effect on workload reports	XV-3

Multiple AMIS codes

effect on workload reports	XV-5

Multipliers

effect on workload reports	XV-3

## N

No Complication	VII-2

No shows	XVI-7

Non-Common Data for Printsets	XII-1

Non-count stop codes	XIV-1

NPO	XVI-10

Nuclear Medicine List Menu	VIII-1

Nuclear Medicine List Menu (all options)	III-3

Nuclear Medicine setup

worksheet	XI-18

Nuclear Medicine Setup Menu	I-4, II-8, III-3, VII-1, VIII-14

routes	II-8

sites	II-8

## O

OE/RR	VII-51, XVI-3

using common procedures to create protocols	VII-55

On-line Verifying of Reports	III-4, V-6, XIV-2, XV-1

Operating room	VII-76

effect on workload reports	XV-3

Order entry	XVI-11

Order Entry Parameters	V-2, V-22

Order Entry Procedure Display Menu	VII-1

Order Entry/Results Reporting	V-2

Order in Sequence of Status Progression	VII-8

Order number	VII-8

Order of the progression	VII-8

Ordering

broad procedures	XVI-3

common procedures	XVI-3

OE/RR	XVI-3

rescheduling	XVI-6

sample workflow	XVI-6

user problem in selecting procedures	XVI-3

Orders

accounting for all pending	XVI-2

Outside Films Profile	III-3

Outside Films Registry Menu	III-3

Override a Single Exam Status to 'complete'	III-4

## P

Parameters

changes, when they take effect	V-10

when changes take effect	V-27

Parent procedure	VII-61

separate reports	VII-62

single report	VII-62

Parent procedure entry	VII-70

Parent Procedure List	VIII-19, VIII-38

Parent procedures	XIV-1

single report all descendents	II-9

Parent/Descendent Exam and Printsets	I-4, XII-1

Patient Care Encounter	XIV-2

Patient charts	XVI-7

Pending	XVI-10

Pending orders

accounting for	XVI-2

Pending requests	XVI-7

Pending/Hold Rad/Nuc Med Request Log	III-3, XVI-2, XVI-10

Person who administered the dose

exam status	VII-16

Person who measured

exam status	VII-16

Personnel classification	IV-1

Personnel classification lists

example	VI-6

Personnel Workload Reports	III-5

Pharmacy Drug file

radiopharmaceuticals	II-1, II-10

VA Classifications	II-1

Physician Report	XV-2, XVI-12

Physician Title on Reports	XV-2

Physician Workload Report

exam status	VII-18

Population of Imaging Exam Data	XIII-5

Portable	VII-76, XVI-12

effect on workload reports	XV-3

Preps	XVI-10

Primary Camera/Equip/Rm prompt	V-4

Print a Batch of Reports	III-3

Print Division Parameter List	V-1, V-14

example	V-14

Print Dosage Ticket when Exam Reaches this Status	II-6

Print DX Codes in Report?	V-23

Print File Entries	III-3, V-9

option	II-9

Print Flash Card for Each Exam	V-10

prompt	V-21

Print Jacket Labels with Each Visit	V-8, V-10, V-21

Print Rad/Nuc Med Requests by Date	III-3

Print Selected Requests by Patient	III-3

Print Worksheets	III-3

Printer set-up	V-22, V-27, V-33

Printing/batching	XVI-8

Printsets

Add Exams to Last Visit	XII-5

cancelled cases	XII-2

common data	XII-1

CPRS interface	XII-5

editing data	XII-4

HL7 interface	XII-3

labels/headers/footers	XII-4

non-common data	XII-1

RA MGR key	XII-2

single report	XII-1

special character designation	XII-2

VA Fileman prints/inquiries	XII-5

Procedure	V-2

AMIS weight multiplier	XV-3

cost, entering of	VII-59

done by locations of different imaging types	VII-60

Procedure Enter/Edit	II-1, II-3, II-8, VII-1, VII-57, VII-60, VII-74, VIII-31, XVI-1, XVI-4

affecting case edits/status tracking	XIII-1

medication parameters	II-8

parent procedure entry example	VII-70

radiopharmaceutical parameters	II-8

Procedure File Listings	VIII-1, VIII-18, XIV-1

Procedure message

for broad type	XVI-3

Procedure Message Entry/Edit	VII-57, VII-74, XVI-4

example	VII-74

Procedure Message List	VIII-19, VIII-40

example	VIII-40

Procedure modifier

bilateral	VII-76

operating room	VII-76

portable	VII-76

screened by imaging type	VII-75

Procedure Modifier Entry	VII-57, VII-75, VIII-13

example	VII-75

Procedure modifiers	VII-75

Procedure setup

worksheet	XI-13

Procedures

broad	XVI-2

changing broad to detailed/series	XVI-3

changing imaging type of	XVI-1

CPT	XVI-2

data corruption due to deletion of	XVI-1

detailed	XVI-2

edit	XVI-2

imaging type of	XVI-1

message	XVI-3

name edit	XVI-2

originally distributed	XVI-2

Profile of Rad/Nuc Med Exams	III-3

Prompt for Meds	II-8, VII-62

case edits/status tracking	XIII-3

Prompt for Radiopharm Rx	II-8, VII-63

PTF Bedsection Report	XV-2, XVI-12

PTF Bedsection Workload Report

exam status	VII-17

Purging	V-11

Purging records	XVI-8

## Q

Quick order	VII-51

## R

RA ALLOC	II-10, II-11, III-1, III-5, IV-1, VI-6, XVIII-12

RA HL7 Voice Reporting Errors	IX-2

RA MGR	II-10, III-3, III-4, IV-1, V-6, V-11, XVIII-12

RA VERIFY	II-10, III-4, III-5, IV-1, XVIII-12

Rad/NM Phys Approval Required	VII-67

Rad/Nuc Med HL7 Voice Reporting Errors	VIII-1, IX-2

Rad/Nuc Med Location Access	VI-2

Rad/Nuc Med Personnel Menu	II-11, III-3, VI-1, VI-6

Rad/Nuc Med Procedures file	II-3, VII-15

Rad/Nuc Med Procedures Name	VII-60

Rad/Nuc Med Total System Menu	II-10

Radiopharm Prescription &amp; Prescribing Physician/Dose Logic	XIII-4

Radiopharmaceutical Dosage Ticket Print Control	VII-18

Radiopharmaceutical dose

High Adult Dose	II-3

Low Adult Dose	II-3

Radiopharmaceutical Drug Classifications

example	XI-16

Radiopharmaceutical functions

exam status	VII-15

Radiopharmaceutical Logic

in case edits/status tracking	XIII-2

Radiopharmaceutical Lot Source

field	VII-47

Radiopharmaceuticals	I-4

associated with a procedure	VII-63

requirements	VII-12

setup/definition of	II-1, II-10

suppress asking/requiring	XIII-3

VA Drug Classifications	II-1, II-10

worksheet	XI-14

Radiopharmaceuticals Used?

field	VII-19

Radiopharms &amp; Dosages Required	II-6, VII-13

Radiopharms/Dosages Required

field	II-6

Radiopharms/Dosages Required?

case edits/status tracking	XIII-3

Reason Edit	VII-1

Reason for hold/DC of order	XVI-7

Register an Exam	VII-60

Register Patient for Exams	III-4

Registration

changing a broad to detailed or series	XVI-3

future dates	V-5

use of Pn	XII-3

Released/not verified	V-24

Released/Unverified	XVI-8

Report	VII-17

Report Distribution Lists	VIII-1, VIII-43

example	VIII-43

Report Entered Required	VII-14

Report Entry/Edit	II-1, III-5, V-5, VII-81, XIV-2

Report footer	V-22

Report header	V-22

Report Left Margin	V-23

Report Parameters	V-22

Report purge	XVI-9

Report Right Margin	V-23

Report text	V-6

Reports Distribution Edit	VII-1, VII-77, VIII-43

example	VII-78

Request	XVI-6

Request an Exam	III-3, VII-60

Request Printer Name	V-22

Request status	V-3

Requesting physician	VII-6

Requests

Display of	XVI-10

lab work	XVI-10

NPO	XVI-10

preps	XVI-10

scheduled	XVI-10

status tracking log	XVI-10

tracking	XVI-10

Required Flash Card Format	VII-66

Required Flash Card Printer	VII-66

Rescheduling requests	XVI-7

Research	XVI-13

Research patient	XVI-13

Resend Radiology HL7 Message	IX-6, IX-7

Resident	XV-1

Resident On-line Pre-Verification	III-4, XIV-2

Resident or Staff Required	VII-12

Resident Report	XV-2, XVI-12

Resident Signature Name	II-7

Resident Workload Report

exam status	VII-18

Results reports

batch printing	XVI-8

distribution queues	XVI-8

headers/footers	VII-34

print location of	XVI-8

queuing to printers	XVI-8

title of physician	XV-2

Review Required	VII-66

Route of Administration Enter/Edit	VII-43, VII-45, VII-46

example	VII-45

Route of Administration file	VII-43

Route of Administration List	II-8, VII-43, VIII-14, VIII-16

Route/Site of administration

exam status	VII-16

Route/Site Required (Radiopharm Administered)	II-6, VII-13

Routes

radiopharmaceutical	II-8

Rpharm Dose Warning Message	II-3, V-8

## S

Sample Contrast Media Edit History by Procedure Report	VIII-23

Schedule a Request	III-3, XVI-6, XVI-7, XVI-8

Scheduled	XVI-10

Scheduling	XIV-2

Scheduling package	XVI-6

Scheduling requests

rescheduling	XVI-6

step-by-step example	XVI-6

Screening

Abnormal Report	III-5

Access Erroneous Reports	III-3

Add Exams to Last Visit	III-4

Add/Remove Report from Batch	III-4

AMIS Code Dump by Patient	III-5

AMIS Report	III-5

Cancel a Request	III-3

Cancel an Exam	III-4

Case No. Exam Edit	III-4

Complication Report	III-5

Create a Batch	III-3

Daily Log Report	III-5

Delete a Report	III-3

Delete Printed Batches	III-4

Delete Printed Batches by Date	III-3

Delinquent Status Report	III-5

Detailed Request Display	III-4

Diagnostic Code Entry by Case No.	III-4

Display a Rad/Nuc Med Report	III-3

Display Patient Demographics	III-3

Display Rad/Nuc Med Procedure Information	III-3

distribution queue	III-3

division	III-2

Draft Report	III-4

Duplicate Flash Card	III-4

Edit Exam by Patient	III-4

effects of RA ALLOC key	III-5

Enter Last Past Visit Before DHCP	III-3

Exam Deletion	III-3

Exam Profile (selected sort)	III-3

Exam Status Display	III-4

Examination Statistics	III-5

Functional Area Workload Reports	III-5

Hold a Request	III-3

imaging location	III-2

imaging type	III-2

Incomplete Exam Report	III-5

Indicate No Purging of an Exam/Report	III-4

Inquire to File Options	III-3

Jacket Labels	III-3

List Exams with Inactive/Invalid Statuses	III-3

List Reports in a Batch	III-3

Log of Scheduled Requests by Procedure	III-4

Maintenance Files Print Menu	III-3

Mass Override Exam Status	III-4

Nuclear Medicine List Menu (all options)	III-3

Nuclear Medicine Setup Menu (all options)	III-3

On-line Verifying of Reports	III-4

option allocation	III-3

Outside Films Profile	III-3

Outside Films Registry	III-3

Override a Single Exam Status to 'complete'	III-4

Pending/Hold Rad/Nuc Med Request Log	III-3

Personnel Workload Reports	III-5

Print a Batch of Reports	III-3

Print File Entries	III-3

Print Rad/Nuc Med Requests by Date	III-3

Print Selected Requests by Patient	III-3

Print Worksheets	III-3

Profile of Rad/Nuc Med Exams	III-3

Rad/Nuc Med Personnel Menu	III-3

Register Patient for Exams	III-4

Report Entry/Edit	III-5

report ownership	III-2

reports	III-2

Request an Exam	III-3

Resident On-line Pre-Verification	III-4

Schedule a Request	III-3

Search File Entries	III-3

security keys	III-5

security keys	III-3

Select Report to Print by Patient	III-3

selected imaging type	III-2

Special Reports	III-5

Status Tracking of Exams	III-4

Switch Locations	III-4

System Definition Menu	III-4

Test Label Printer	III-4

Transcription Report	III-4

Unverified Reports	III-5

Unverify a Report	III-4

Update Exam Status	III-4

Update Patient Record	III-4

Utility Files Maintenance Menu	III-4

Verify Batch	III-4

Verify Report Only	III-5

View Exam by Case No.	III-4

Ward/Clinic Scheduled Request Log	III-4

Screening stop codes	XIV-1

Search File Entries	III-3

Security key

status tracking	VII-9

Security keys	II-10, IV-1

RA ALLOC	II-10

RA MGR	II-10, V-6, V-11

RA VERIFY	II-10

used in options	III-5

Select Interpreting Physician	XV-1

Select Report to Print by Patient	III-3

Select sign-on location	IV-1

Series	VII-61

Series of Procedures List	VIII-19, VIII-41

Service Report	XV-2, XVI-12

Service Workload Report

exam status	VII-17

Seven Hundred series stop codes	XIV-1

Sharing Agreement/Contract	XV-3

Sharing Agreement/Contract Entry/Edit	VII-1, VII-80, VIII-44

example	VII-80

Sharing Agreement/Contract List	VIII-1, VIII-43

example	VIII-44

Sharing Agreement/Contract Report	VII-80, XV-2, XVI-12

Sharing/Contract Workload Report

exam status	VII-17

Should this Status Appear in Status Tracking	VII-9

Signature block title, use in results report	XV-2

Sign-on imaging type	III-2

Single Report	II-8, VII-62

parent procedure	VII-62

Single Report Setup for Printsets	XII-1

Site of Administration Enter/Edit	VII-43, VII-46

example	VII-46

Site of Administration file	VII-43

Site of Administration List	II-8, VII-43, VIII-14, VIII-17

Sites

radiopharmaceutical	II-8

Special Character Designation for Printsets	XII-2

Special Reports	III-5, XV-2

Staff	XV-1

Staff Report	XV-2, XVI-12

Staff Signature Name	II-7

Staff Workload Report

exam status	VII-18

Standard reports	XVIII-12

Standard Reports Entry/Edit	V-5, VII-1, VII-81, VIII-45

example	VII-82

Standard Reports Print	VIII-1, VIII-45

example	VIII-45

Stat Request Alert Recipients	II-4, V-24

Status

exam	VII-7

order	VII-7

report	VII-7

Status Change Requirements	XVI-4

Status parameter

route/site	VII-45

Status tracking	VII-8, XIII-1

Status Tracking	XVI-4

security key	VII-9

Status tracking functions	VII-14

Status Tracking of Exams	III-4, VII-7, VII-31, XIV-2, XVI-2

Stop code crediting

effect of division on	XIV-2

effect of exam status override	XIV-2

effect of outpatient status	XIV-2

error tracking/recovery using MAS mail group bulletins	XIV-3

options that trigger	XIV-2

Stop code crediting, error tracking/recovery using Rad/Nuc Med bulletin	XIV-3

Stop codes	XIV-1

background errors	XIV-3

crediting of	XIV-2

how they are passed to MAS	XIV-1

invalid/missing	XIV-1

VA Headquarters	VII-83

yearly update	VII-83

Stop Codes

assignment to procedures	XIV-1

Stopping tasked jobs	XVII-1

Stuffing Data	XIII-1

Submit Request To prompt	V-25

Supervisor Menu	VII-1, VIII-18

Suppress Radiopharm Prompt	II-8, VII-63

Switch Locations	III-4, V-10, V-27, XVI-2

Synonym

associated with a procedure	VII-62

System Definition Menu	II-11, III-4, V-1, VII-1

## T

Tasked jobs

stopping	XVII-1

Technologist	VI-2

Technologist List	VI-1, VI-6

Technologist Report	XV-2, XVI-12

Technologist Required	VII-12

Technologist Workload Report

exam status	VII-17

Test Label Printer	III-4

Time Limit for Future Exams	V-5

Title of interpreting physician on results reports	XVI-10

Title of physician on results reports	XV-2

Track Exam Status Changes	V-4

Tracking requests	XVI-10

Transcribed	VII-8

Transcription

standard reports	VIII-45

Transcription Report	III-4, XV-2

Transcriptionist	V-5, VII-81, XVI-8

Trouble shooting	XV-1

Type of Imaging	VII-60

Type of Procedure	VII-60

Type of Procedure field	VII-61

## U

Unverified Reports	II-3, III-5, V-6

Unverify a Report	III-4

Update Exam Status	III-4, XIV-2

Update Patient Record	III-4, XVI-13

Urgent Request Alerts	II-5

Urgent Request Alerts?	V-24

User Key Needed to Move an Exam to this Status	VII-9

Usual Dose	VII-64

Utility Files Maintenance	XVI-4

Utility Files Maintenance Menu	I-4, II-11, III-4, VII-1, VII-43, VII-49, VIII-1

## V

VA Fileman Prints/Inquiries	XII-5

VA Headquarters	XIV-1

Valid Imaging Stop Codes Edit	VII-1, VII-83, XIV-1

example	VII-83

Valid Sites of Administration

field	VII-46

Vendor/Source (Radiopharmaceutical) Enter/Edit	VII-43, VII-47

example	VII-47

Vendor/Source (Radiopharmaceutical) List	VIII-14, VIII-18

Verified Report Required	VII-14

Verified reports	XVI-8

Verify a report	XVI-10

Verify Batch	III-4, XIV-2

Verify Report Only	III-5, XIV-2

Verifying others' reports	XVI-10

Verifying reports	V-6, XVI-10

Verifying Signature Name	II-7

View Exam by Case No.	III-4

Voice Dictation Auto-Print	V-23

Voice Recognition Systems	XIV-2

Volume/Form Required (Radiopharm)	II-6, VII-14

## W

Waiting for exam	VII-8

Ward Report	XVI-12

Ward Workload Report

exam status	VII-17

Ward/Clinic Scheduled Request Log	III-4, XVI-11

Warning on Rpts Not Yet Verified	V-6

Wasted Film Report	VII-32

Wasted film sizes	VIII-10

Wasted Film, prompt	VII-32

Weight	VII-42, XV-3

Weighted work unit	VII-42, VII-65

Weighted work units	XV-3

Workload

multiple AMIS codes	XV-5

Workload credit	VII-61

Workload crediting	VII-42, VII-76, VII-83

doubling of	XVI-11

effect of modifiers	XVI-11

options that trigger	XIV-2

Workload report	XV-3

Workload reports	VII-42, XVI-1

effect of contract/sharing on	XV-3

effect of exam status on	XV-3

effect of multiple residents	XV-5

effect of multiple staff	XV-5

effect of multiple technologists	XV-5

effects of AMIS code on	XV-3

multipliers	XV-3

troubleshooting	XV-2

WWU	VII-65

WWUs	XV-3

## X

XUSESIG	VI-2

1. If the user selects an option that is screened by location, s/he will only be able to access exam data within X-RAY 1.