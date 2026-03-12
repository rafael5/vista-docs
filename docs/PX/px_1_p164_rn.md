---
app_name: Patient Care Encounter (PCE) (PX)
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
package_id: PX
patch: null
patch_gap: null
section: ''
source_file: px_1_p164_rn.docx
status: draft
title: PATIENT CARE ENCOUNTER
---

# PATIENT CARE ENCOUNTER
(PCE)

Release Notes
PX*1.0*164

February 2006


 Health System Design &amp; Development

Revision History

| **Date**   |   **Revision** | **Description**                                                                                                          | **Author**   |
|------------|----------------|--------------------------------------------------------------------------------------------------------------------------|--------------|
| 10/20/05   |            0.1 | Added two modifications patch includes, removed PXCEPRV routine, and updated checksum values to reflect correct numbers. | REDACTED     |
| 01/06/06   |            1   | Added new functionality, enhancements to the software                                                                    | REDACTED     |

**Table of Contents**

Introduction	1

Patient Financial Services System	1

Software Interfaces	1

Overview of New Functionality	1

Package Name Enhancements	2

Options and Actions	2

Reports and Profiles	2

Files and Fields	2

New Files	2

Changed Files	2

VISIT file (#9000010)	2

VCPT file (#9000010.18)	3

Other Functionality	3

Charge Message SC/EI Classifications	3

API Changes	3

1889 NAME: DBIA 1889-A (DATA2PCE)	3

ACCOUNT	3

PROCEDURE	3

1900 NAME: DBIA 1900-A	4

^VSIT	5


## Introduction

### Patient Financial Services System

The Patient Care Encounter (PCE) patch is part of the Patient Financial Services System (PFSS) project. PFSS patches are being released on various schedules. Some patch functionality will not be active until a new PFSS switch is activated during final implementation. PFSS will initially be implemented at select pilot sites ONLY.

The purpose of the PFSS project is to prepare the Veterans Health Information Systems and Technology Architecture () environment for the implementation of a commercial off-the-shelf (COTS) billing replacement system. The project consists of the implementation of the billing replacement system, business process improvements, and enhancements to  to support integration with the COTS billing replacement system. Significant changes to  legacy systems and ancillary packages are necessary.

These PFSS software components are not operational until the PFSS On/Off Switch, distributed with patch IB*2*260, is set to "ON". The ability for the local site to set the switch to "ON" will be provided at the appropriate time with the release of a subsequent Integrated Billing (IB) patch. For more information about the PFSS project, review the documentation accompanying this patch and refer to the following website: REDACTED/.

### Software Interfaces

PCE processing assumes the following  packages are installed and fully patched:

Kernel				V.8.0

VA FileMan			V.22.0

MailMan 				V.8.0

CPT/HCPCS Codes 		V.6.0

DSS 				V.3.0

PCE				V.1.0

ICD				V.18

LEX				V.2.0

IB				V.2.0

PX*1.0*164 requires the prior installation of the following patches:

IB*2*286

SD*5.3*430

### Overview of New Functionality

The PCE PFSS 1B project will add the following new functionality to the PCE Application:

- A new field, PFSS Account Reference, which is used by the external billing system to attach charges for 1 st and 3 rd party billing.
- PCE now determines if there is a PFSS Account Reference available either by being passed-in with a DATA2PCE API call, or by association with a scheduled appointment, or through association with an order.
- If no PFSS Account Reference is available, PCE will call the Integrated Billing subsystem (IBB) Get Account API to create a new PFSS Account Reference.
- A new field, Department Code, which defines the service area for a charge.
- A new field, PFSS Charge ID, which uniquely identifies each charge item in the external billing system.
- Changes to the DATA2PCE API and Visit Tracking to accommodate the new fields.
- A new filer routine used to file charges into the Integrated Billing subsystem (IBB) cache buffer *.*
- New dynamically created Charge Message SC/EI classifications for procedures that are auto-populated based on the procedure clinical indicators and are filed with the charge message into the IBB cache buffer.
- A new post-installation routine to activate the Order/Entry Result Reporting package in the Visit Tracking Parameters (#150.9) file.

## Package Name Enhancements

The new features, functions, and enhancements of the PCE package are grouped and discussed in detail in the following sections.

### Options and Actions

There are no new additions or changes to any of the menu options in the PCE package.

### Reports and Profiles

There are no new reports or changes to the reports in the PCE package.

### Files and Fields

This section contains new or changed files and fields in the PCE package.

#### New Files

There are no new files added to the PCE package.

#### Changed Files

##### VISIT file (#9000010)

Field Number		Field Name

.26			PFSS ACCOUNT REFERENCE

##### VCPT file (#9000010.18)

Field Number		Field Name

.19			DEPARTMENT CODE

.2			PFSS CHARGE ID

### Other Functionality

#### Charge Message SC/EI Classifications

Based on the associated clinical indicators, the Charge Message SC/EI classifications will be auto-populated according to the following rules:

If the SC/EI for at least one ICD-9 is "Yes", then the Charge Message SC/EI will automatically be set to "Yes".

If the SC/EI for all ICD-9's is "No", then the Charge Message SC/EI will automatically be set to "No".

If at least one ICD-9 is missing an SC/EI and none of the other ICD-9's SC/EI is "Yes", use the Encounter Level SC/EI.

#### API Changes

##### 1889	NAME: DBIA 1889-A (DATA2PCE)

###### ACCOUNT

Add a dotted variable to the calling parameters which represents the PFSS Account Reference.

$$DATA2PCE^PXAPI(INPUTROOT,PKG,SOURCE,.VISIT,USER,ERRDISP,.ERRARRAY,PPEDIT,.ERRPROB, .ACCOUNT)   This is a function which will  return a value identifying the status of the call. Data that is processed by PCE will be posted on the PXK VISIT DATA EVENT protocol.

Modified Parameter Description:

(Optional) A dotted variable name, where ACCOUNT is the PFSS Account Reference associated with the data being passed by the calling application. Each PFSS Account Reference represents an internal entry number in the PFSS ACCOUNT file (# 375).

###### PROCEDURE

Add a new DEPARTMENT subscript to the procedure level for the DATA2PCE API.

The "PROCEDURE" node may have multiple entries (i). Only active CPT/HCPCS codes will be accepted. The "PROCEDURE" node documents the procedure(s), the number of times the procedure was performed, the diagnosis the procedure is associated with and the narrative that describes the procedure. It also enables documentation of the provider who performed the procedure, the date/time the procedure was performed and any comments that are associated with the procedure. To delete the entire "PROCEDURE" entry, set the "DELETE" node to 1.

"PROCEDURE",i,"DEPARTMENT")	A 3-digit code that defines the service area. Missing Department Codes will be assigned a Department Code. The Department Code will be the Stop Code associated (in the HOSPITAL LOCATION file, #44) with the Hospital Location of the patient visit.

108::=Laboratory

160::=Pharmacy

419::=Anesthesiology

423::=Prosthetics

180::=Oral Surgery

401::=General Surgery

402::=Cardiac Surgery

401::=General Surgery

402::=Cardiac Surgery

403::=Otorhinolaryngology (ENT)

404::=Gynecology

406::=Neurosurgery

407::=Ophthalmology

409::=Orthopedics

410::=Plastic Surgery (inc. H&amp;N)

411::=Podiatry

412::=Proctology

413::=Thoracic Surgery

415::=Peripheral Vascular

457::=Transplantation

105::=General Radiology

109::=Nuclear Medicine

109::=Cardiology Studies (Nuclear Med)

115::=Ultrasound

703::=Mammography

150::=CT Scan

151::=Magnetic Resonance Imaging

152::=Angio-Neuro-Interventional

421::=Vascular Lab

##### 1900	NAME: DBIA 1900-A

Visit Tracking is a utility that can be used by a variety of  modules (usually via PCE), with potential benefits for clinical, administrative, and fiscal applications. Visit Tracking will allow  packages to link an event to a patient visit entry, thereby linking that event to any number of events occurring throughout the hospital during the patient's outpatient and/or inpatient episode.

###### ^VSIT

Field Number		Variable		Description

.26			VSIT("ACT")		PFSS ACCOUNT REFERENCE (pointer

PFSS ACCOUNT file #375)