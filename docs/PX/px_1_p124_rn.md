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
source_file: px_1_p124_rn.docx
status: draft
title: PATIENT CARE ENCOUNTER
---

# PATIENT CARE ENCOUNTER

# (PCE)
 

RELEASE NOTES

**PX*1.0*124
August 2005**


 Health System Design &amp; Development

*(This page intentionally left blank for two-sided copying.)*

**Table of Contents**

Introduction	1

Dependencies	1

NEW Report	1

New Fields	3

Diagnosis Classifications	3

Encounter Classification	4

Diagnoses Association	4

API Changes	5

*(This page intentionally left blank for two-sided copying.)*

## Introduction

The PCE application has been enhanced to collect and store additional medical data including clinical indicator and enrollment identifiers.  Successful completion of the project results in greater accuracy and more useful clinical data for medical decision making.  Clinical Ancillary packages will pass required clinical data to PCE to be extracted by Integrated Billing (IB) to create third-party insurance claims.

PCE is being enhanced to include PCE Missing Data report in order to identify those encounters that do not have required fields for billing.  The required elements for the encounter include attached procedure codes (CPT and/or HCPCS), diagnosis codes (ICD-9), and related Service-Connected/Environmental Indicators (SC/EI).  The Missing Data report is a useful tool for HIMS staff to identify those PCE Encounters with clinical data deficiencies.

### Dependencies

PCE is dependent upon the following  packages:

**Package	Minimum Version**

Kernel                                                                                                                  8.0

VA FileMan                                                                                                       22.0

Patient Information Management System (PIMS)                                              5.3

Order Entry/Results Reporting (OE/RR)                                                            3.0

Automated Information Collection System (AICS)                                           3.0

PCE Patient/IHS Subset (PXPT)                                                                        1.0

### NEW Report

The Missing Data Report (MDR) identifies CIDC data elements missing from PCE.  It provides staff the ability to sort encounters with CIDC defects using a number of specific data items.  It also allows the printing of statistics versus detail in order to perform trending for possible follow-up through education/training.

Options exported with this patch will attach the MDR to the PCE Coordinator menu.

The HIMS (Health Information Management Systems) staff can use this report to complete PCE encounters.  It can also be used as a clinical staff training tool.

**Note** :  The MDR must be printed to a 132 column device in order to view the entire data set.

**Sample MDR Report**

By Clinic, Provider, and Date

through

Page 1

Patient                   	SSN          	Date/Time           	Enc. ID         Created by User    	Defect

===================================================================================================================================

OUTPATIENT DIAG (BAY PINES)

Unknown

SORT VALUE:  DATA SOURCE= RAD/NUC MED

:

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

PCEpatient, One	000-00-0001  NOV 03, 2004@14:18  HMX8P-BAY       PCEprovider, One             Procedure: 73110 missing assoc. DXs

Diagnosis: 171.6 missing

Diagnosis: 171.2 missing SC/EI

TOTAL DEFECTS FOR HMX8P-BAY:  1

TOTAL DEFECTS FOR :  1

TOTAL ENCOUNTERS FOR :  1

TOTAL DEFECTS FOR SORT VALUE - RAD/NUC MED: 3

TOTAL ENCOUNTERS FOR SORT VALUE - RAD/NUC MED: 1

TOTAL DEFECTS FOR Unknown: 3

TOTAL ENCOUNTERS FOR Unknown: 1

TOTAL DEFECTS FOR OUTPATIENT DIAG (BAY PINES):  3

TOTAL ENCOUNTERS FOR OUTPATIENT DIAG (BAY PINES): 1

### New Fields

The new CIDC fields in the PCE application consist of the Service Connection (SC) and/or Environmental Indicator (EI) status (including Combat Veteran status), and the CPT associated diagnoses.

PCE Diagnoses are optionally identified as Ordering (O), Resulting (R) Or Both Ordering and Resulting.

ICD9 Code or Diagnosis:  000.07// 000.07    RETICULOSARCOMA SPLEEN

COMPLICATION/COMORBIDITY

...OK? Yes//   (Yes)

Provider Narrative:  RETICULOSARCOMA INVOLVING SPLEEN

Replace

RETICULOSARCOMA INVOLVING SPLEEN

Is this Diagnosis Ordering, Resulting, or Both:

Modifier:

Encounter Provider:  PCEprovider,one//        GTS

Provider Narrative Category:

Comments:

#### Diagnosis Classifications

A DIAGNOSIS CLASSIFICATIONS prompt has been added for Service Connection (SC) and/or Environmental Indicator (EI) status (including Combat Veteran status) for an individual ICD-9 code.  If a patient is SC as indicated in eligibility, the PCE Application provides the SC Connection % and Rated Disabilities breakdown.  Diagnosis Classifications display in the following order:

SERVICE CONNECTED
Was treatment for SC Condition?

COMBAT VETERAN
Was treatment related to Combat?

AGENT ORANGE
Was treatment related to Agent Orange Exposure?

IONIZING RADIATION
Was treatment related to Ionizing Radiation Exposure?

ENVIRONMENTAL CONTAMINANTS
Was treatment related to Environmental Contaminant Exposure?

MILITARY SEXUAL TRAUMA
Was treatment related to Military Sexual Trauma?

HEAD AND/OR NECK CANCER
Was treatment related to Head and/or Neck Cancer?

**Example screen of ICD codes:**

ICD9 Code or Diagnosis:  2]000.07// 000.07    RETICULOSARCOMA SPLEEN

COMPLICATION/COMORBIDITY

...OK? Yes//   (Yes)

Provider Narrative:  RETICULOSARCOMA INVOLVING SPLEEN

Replace

RETICULOSARCOMA INVOLVING SPLEEN

Is this Diagnosis Ordering, Resulting, or Both:

Modifier:

Encounter Provider:  PCEprovider,one//        GTS

Provider Narrative Category:

Comments:

--- Classification --- [Required]

Was treatment for SC Condition? YES//

Was treatment related to Ionizing Radiation Exposure? NO//

Was treatment related to Environmental Contaminant Exposure? NO//

#### Encounter Classification

THE ENCOUNTER CLASSIFICATION will be auto populated according to the following rules:

- If the SC/EI for at least one ICD-9 is "Yes" the Encounter Level SC/EI will automatically be set to "Yes".
- If the SC/EI for all ICD-9s are "No" the Encounter Level SC/EI will automatically be set to "No".
- If at least one ICD-9 is missing an SC/EI determination and the other ICD-9s SC/EI determinations are either “No” or missing data, there will be no association with SC/EI.  No change will be made at the Encounter Level at this point.

#### Diagnoses Association

One Primary diagnosis, and up to seven Secondary diagnoses may be associated with a procedure as clinical indicators.

CPT Code: 99201//        OFFICE/OUTPATIENT VISIT, NEW

Select CPT MODIFIER:

Provider Narrative:  OFFICE/OUTPATIENT VISIT, NEW  Replace

OFFICE/OUTPATIENT VISIT, NEW

Quantity:  1// 1

Principal Procedure:  YES// YES

Ordering Provider:

Encounter Provider:  PCEprovider,one//        GTS

Provider Narrative Category:

Comments:

Primary Diagnosis:  000.01// 000.01  000.01    RETICULOSARCOMA HEAD     COMPLIC

ATION/COMORBIDITY

...OK? Yes//   (Yes)

1st Secondary Diagnosis:  000.02// 000.02  000.02     RETICULOSARCOMA THORAX

COMPLICATION/COMORBIDITY

...OK? Yes//   (Yes)

2nd Secondary Diagnosis:  000.03// 000.03  000.03     RETICULOSARCOMA ABDOM

COMPLICATION/COMORBIDITY

...OK? Yes//   (Yes)

3rd Secondary Diagnosis:  000.04//

The example above shows prompts for three secondary diagnoses.  The application can accommodate seven secondary diagnoses prompts.

#### API Changes

The DATA2PCE and PXCA Application Program Interface (API) Files, which are used by other packages to exchange data with the PCE files, were updated to include the CPT associated diagnoses and the diagnosis classifications of  SC, CV, AO, IR, EC, MST, and HNC.