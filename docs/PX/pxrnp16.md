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
source_file: pxrnp16.docx
status: draft
title: pxrnp16.docx
---

**Patient Care Encounter (PCE)**

**Clinical Reminders**

Patch PX*1.0*16

**Release Notes**

July 1997


Technical Services

Computerized Patient Record System Product Line

**PCE Clinical Reminders Patch 16, PX*1.0*16**

**Release Notes**

Patch 16 enhances the Clinical Reminders component of Patient Care Encounter (PCE) by adding new functionality, bug fixes, and new reminder definitions.

This document lists:

**1.** E3Rs this patch resolves

**2.** NOISes this patch resolves

**3.** Patches on which this patch is dependent

**4.** Impact on Health Summary

**5.** Option changes

**6.** Data dictionary changes

**7.** Distributed file data changes

**8.** Distributed reminders changes

**9.** New reminders distributed

**10.** Distributed taxonomies changes

**11.** Documentation changes

**1. E3Rs this patch resolves**

9083	CPT Credit for Health Factor Screen

Resolution:	Answer “YES” in the new “USE IN DATE DUE CALC” field for health factors,

taxonomies, and/or computed findings to use the finding to satisfy the reminder.

**2. NOISes this patch resolves**

BOS-1296-11365	Wrong date used for Education reminders.

STX-1296-70857

Resolution:	Now using the most recent education date.

STL-0497-40086	The final frequency was not getting set properly when there was a frequency

in a taxonomy, health factor, or computed finding.

Resolution:	Establishing the final frequency and age range now works correctly.

SLC-0397-52391	Getting undefined error when trying to delete site defined reminder.

Resolution:	When reminders were created from scratch, they were not properly put into

the site’s number space. This caused several problems including the

undefined error. Site-defined reminders are now put into the site’s number

space when they are copied or created from scratch.

WNY-0397-0166	The site-defined disclaimer did not display on the Health Summary.

Resolution:	Site defined disclaimer now displays properly.

ERI-0197-21920	When editing a taxonomy only the CPT file was available as a source file.

Resolution:	The installation of the new ICD files deleted the PXRS application group.

This patch restores the application group making the ICD files again

available as source files.

**NOISes this patch partially resolves**

STC-1196-41784	Lab extracts (outside of “CH” node) cannot be found based on the laboratory

FAR-0996-42264	test or related CPT code. Pap Smears from Lab package cannot be found.

Resolution:	Use taxonomy definitions to track CPT codes entered through Lab and

extracted by PCE.

**3. Patches on which this patch is dependent**

PX*1.0*2	PX*1.0*16 will not install unless this previous reminder patch has been

installed on your system.

HS*2.7*10	Health Summary patch

PX*1*13	PCE patch to be installed after HS*2.7*10.

DI*21*33, DI*21*36	FileMan patch 33 caused a problem with word processing output in the

reminder display, and 36 fixed it.

**4. Health Summary Impact**

a. The following Health Summary components are temporarily disabled during the install, which takes less than 10 minutes.

PCE CLINICAL MAINTENANCE

PCE CLINICAL REMINDER

PCE EDUCATION

PCE EDUCATION LATEST

b. Sites can suppress “N/A” (not applicable) from displaying for wrong patient sex and outside age range findings by entering an “S” and/or an “A” in the IGNORE ON N/A field in a reminder’s definition in the REMINDER/ MAINTENANCE File.

When a reminder is N/A due to age range, a message is displayed in the Clinical Maintenance component.

Example:

Patient’s age (72) is greater than reminder maximum age of 65.

Enter “A” in the IGNORE ON N/A field if you don’t want these messages displayed.

c. The last line displayed for each of the reminder items in the Clinical Maintenance component gives the final frequency and age range used for the reminder. The final frequency is based on the baseline age range and frequency, which may be modified by Frequency and/or Rank Frequency definitions associated with taxonomy, health factor, and computed findings. The reminder frequency text appears similar to the following: “Final Frequency and Age Range Used: 1 year for ages 50 and older.”

d. The most recent health factor finding within each health factor category is displayed in the Clinical Maintenance component and used by the reminder for processing. When multiple health factors are included in a reminder definition, and there are multiple health factor results, the historical perspective of the health factors within their health factor category is available via the Health Factor components.

e. The most recent taxonomy finding within each taxonomy in a reminder definition is displayed in the Clinical Maintenance component and used by the reminder for processing.

**5. Options Changed**

a. The *Reminder Edit* option has been changed to include prompts for the new fields distributed in the PCE REMINDER/ MAINTENANCE ITEM file with this patch. The sequence of prompts and the sequence of fields on the worksheet in Appendix A-3 (Clinical Reminders Definition) are now the same.

b. The Inquire and List Reminder Item options include display of:

- New fields distributed in the PCE REMINDER/MAINTENANCE ITEM file.

- Taxonomies and health factors with the APPLY LOGIC notation. For example:

VA-MAMMOGRAM/SCREEN (TF(16)) - which indicates that this taxonomy is entry 16 in the PCE TAXONOMY file.

INACTIVATE BREAST CANCER SCREEN (HF(42)) - which indicates that this health factor is entry 42 in the HEALTH FACTORS file.

- The APPLY LOGIC default or user modified value, not previously displayed for the user, but found to be very useful for the clinical coordinators defining reminders.

- The Expanded APPLY LOGIC for the user to review.

c. The HEALTH FACTOR EDIT option on the TABLE MAINTENANCE menu option now accepts Health Factor names up to 40 characters long.

**6. File Data Dictionary Changes**

a. Changes to Files ICD DIAGNOSIS (#80), ICD OPERATION PROCEDURE  (#80.1), and CPT (#81):  Added “PXRS” to the APPLICATION GROUP field for these three files.

*Problem Resolved:* When the new versions of files 80, 80.1, and 81 were released, the APPLICATION GROUP was overwritten. This Application Group is used to include only these files as appropriate source files when building taxonomies using the Taxonomy edit option. Future releases of files 80, 80.1, and 81 will contain the “PXRS” Application Group.

b. Changes to HEALTH FACTORS file (#9999999.64):  The (.01) FACTOR field was changed from 3-30 characters to 3-40 characters. The “B” cross-reference was redefined to use the full 40 characters to create the “B” cross-reference.

c. Changes to PCE REMINDER/MAINTENANCE ITEM file (#811.9):  Modified the file description field to incorporate the new fields distributed with this patch.

- Added new field IGNORE ON N/A (#1.8). This field allows a reminder to be defined so that nothing will be displayed on the Clinical Maintenance Health Summary Component if the reminder is N/A for specific reasons. As of this patch, the allowable reasons are wrong sex and wrong age.

- Changed the name of the AGE FINDING multiple to BASELINE AGE FINDING.

- The following multiple fields in the PCE REMINDER MAINTENANCE ITEM file definition have new fields added to them:  Taxonomy Findings, Health Factor Findings, and Computed Findings.  Each of these multiples has three new fields which may be used to control how the reminder works.

1) USE IN DATE DUE CALC (Optional):  This allows the reminder to use a match on a Taxonomy Finding, Health Factor Finding, or Computed Finding as a result which is included in the determination of when the reminder is due. A blank in this field indicates the date of the match findings data will not be used to determine the next date the reminder will be due.

2) RANK FREQUENCY (Optional):  This field is used to rank the frequency and age ranges that are associated with Health Factor Findings, Taxonomy Findings, and Computed Findings. It is used for the situations 1) where more than one match is found among Taxonomy Findings, and/or Health Factor Findings and/or Computed Findings, and 2) where more than one of the Findings definitions has its own age range and frequency. The rank is used to establish a priority or ranking that tells the reminder logic which age range and frequency should take precedence. The value that can be entered in the Rank field is a number from 1 to 999, or blank. The highest ranking (priority) is number 1. When there are multiple Findings found, the Finding with the highest rank will be used to set the final frequency and age range. When the Rank fields are blank (null) in the Findings multiples, and there are multiple Findings found, the reminder logic will use the frequency that will make the reminder be given most often. For example, a Health Factor Finding has age range 25-50 with a frequency of 6 months, and a Taxonomy Finding has age range 25-70 and a frequency of 1 year. The Health Factor age and frequency would be used for the reminder, since a 6 month interval is more frequent than 1 year interval.

3) USE IN APPLY LOGIC (Optional):  This field allows the user to indicate that a Taxonomy Finding, Health Factor Finding or Computed Finding should be included as part of the “Apply Logic.” The Apply Logic is used to determine whether or not a reminder should be applied (given) to a patient. This is very useful for those situations where a reminder should only be given to, or NOT given to patients with a particular Taxonomy, Health Factor, or Computed Finding on file. The USE IN APPLY LOGIC field can be defined with one of the following sets of codes:

EQUATES TO BOOLEAN

CODE	VALUE	OPERATOR/LOGIC

----	----------	---------------------------

“”	blank (null)	not included in Apply Logic

&amp;	“AND”	&amp;(Finding)

!	“OR”	!(Finding)

&amp;’	“AND NOT”	&amp;‘(Finding)

!’	“OR NOT	!‘(Finding)

The value in this definition is used to create a Boolean “APPLY LOGIC” string. The Apply Logic string always includes (SEX)&amp;(AGE), but will add &amp;(Finding), !(Finding), &amp;‘(Finding), or !‘(Finding) to the string, depending on the value in the USE IN APPLY LOGIC field. If a more detailed definition of the APPLY LOGIC string is required, then the APPLY LOGIC string can be created via FileMan. When the APPLY LOGIC string is defined via FileMan, the “USE IN APPLY LOGIC” field is ignored.

- APPLY LOGIC:  The Field name previously called “LOGIC” (field #9) has had its field name changed to “APPLY LOGIC.” This field is used by the reminder logic to determine if a reminder should be applied to a patient. Prior to this patch, the user was not able to see the contents of this field. This field will be blank, unless users decide to define their own APPLY LOGIC. When the reminder is run and the APPLY LOGIC field is blank, “Default APPLY LOGIC” is created based on the reminder definition. The Default APPLY LOGIC string always includes (SEX)&amp;(AGE), but will add &amp;(Finding), !(Finding), &amp;‘(Finding), or !‘(Finding) to the string, depending on the value in the USE IN APPLY LOGIC fields. If a more complex definition of the APPLY LOGIC string is required, then the APPLY LOGIC string can be created via FileMan. When the APPLY LOGIC string is defined via FileMan, this “User Modified APPLY LOGIC” overrides the Default Apply Logic. The Default APPLY LOGIC is ignored.

- The Default or User Modified APPLY LOGIC is now viewable by the users in the *Inquiry* and *List Reminder* options.

- **Hin** t: If you want to get rid of the “User Modified APPLY LOGIC” and go back to the “Default APPLY LOGIC,” you must delete the user-defined APPLY LOGIC by entering @ for the APPLY LOGIC field with FileMan. (The @ is the delete symbol for FileMan).

d. Changes to V PATIENT ED file (#900010.16) to make the “AA” cross-reference, consistent with the other V-files distributed with PCE.

**7. Changes And Additions to Data Distributed In Files**

The reminder definition changes include:

a.	Modifications related to taxonomies:

- Some taxonomy definitions now include ICD diagnosis V-codes. These can be used when a patient is only being treated for the preventive maintenance item at the visit. The taxonomies with V-codes are used by the reminder as results which are included into the due date calculation.

- Some taxonomy definitions were changed to incorporate CPT codes. The taxonomies with these CPT codes are used by the reminder as results which are included in the date due calculation.

Please keep in mind that some taxonomies include historical coded values, which are no longer active. The historical coded values will be useful when historical data becomes available from the Scheduling package.

b.	Modifications related to health factors:

Clinicians need a way to turn off a reminder for a particular patient for a number of reasons, including co-morbidity and patient refusal. A standard coded terminology has not been defined that can adequately deal with all of the reasons for a reminder to be turned off. Until standard terminology can be developed, a generic solution is needed. This patch is distributing new health factors which provide a generic solution. These new health factor names are prefixed with “INACTIVATE” and  “ACTIVATE” followed by text representing a reminder (e.g., INACTIVATE SIGMOIDOSCOPY). An “INACTIVATE” and “ACTIVATE” health factor combination is distributed for each NCHP reminder (prefixed with VA-*).

All of the INACTIVATE and ACTIVATE health factors are defined as part of the “REMINDER FACTORS” health factor category. The reminder logic treats all of the health factors defined within a single health factor category as toggles. The most recent health factor defined in the reminder that is part of a particular health factor category will be the health factor finding used by the reminder logic.

The distributed “VA-*” prefixed reminders each have the INACTIVATE and ACTIVATE health factors added to their reminder definitions. The Health Factor Findings portion of these reminders is defined with these new health factors, illustrating how a health factor can be defined to prevent application of a reminder to a patient, or to activate a previously inactivated reminder for a patient.

When a clinician uses the INACTIVATE and ACTIVATE health factors, a reason for the inactivation of the reminder for the patient should be recorded in the COMMENT field of the V Health Factor File. The comment is displayed in the health summary clinical maintenance component for the most recent health factor within the health factor category. By selecting an “INACTIVATE” health factor for a patient, the patient will be considered “not eligible” or “not appropriate” to receive the reminder.

To reactivate any of the VA-* reminders for a patient, a clinician must document the ACTIVATE health factor related to the reminder. Since the ACTIVATE and INACTIVATE health factors are in the same category, “REMINDER FACTORS,” and are both defined in the reminder definition, the two health factors act as a toggle for each other. If a previously marked “INACTIVATE” health factor exists for a patient, but subsequently an “ACTIVATE” health factor is entered for the patient, and both of these health factors are defined in a reminder’s definition, then the most recent health factor entered, “ACTIVATE” health factor, will be used to satisfy the reminder. Clinicians may choose to create more specific health factors for each reminder to indicate the reason for inactivation or activation. The health factor names don’t have to be prefixed with “INACTIVATE” or “ACTIVATE.” Reminder definitions must have these health factors defined in them with the appropriate “USE IN APPLY LOGIC” in order for the reminders to function appropriately.

c.	Technical descriptions for each of the reminders have been changed to reflect the new reminder

definitions.

**8. Changes to “VA-*” prefixed Reminders**

VA-*BREAST CANCER SCREEN

Modified existing Taxonomy:

VA-MAMMOGRAM/SCREEN

with “match found” fields as follows:

USE IN DATE DUE CALC = YES

VA-MAMMOGRAM/SCREEN taxonomy content added to CPT codes 76090-76092:

ICD Diagnosis:

V76.1 Breast;Special screening for malignant neoplasms

Added Health Factor:

INACTIVATE BREAST CANCER SCREEN

with “match found” fields as follows:

REMINDER FREQUENCY = 0Y

USE IN APPLY LOGIC= &amp;’

ACTIVATE BREAST CANCER SCREEN

with blank “match found” fields, if this is the most current health factor, of the two listed, then the logic will continue based on the other age, sex, and frequency definitions.

VA-*CERVICAL CANCER SCREEN

Modified Reminder Type:

PROCEDURE (was Laboratory Test)

*Removed Target Result Findings File and Items (pre-init).

Added new Taxonomy:

VA-CERVICAL CANCER SCREEN

with “match found” fields as follows:

USE IN DATE DUE CALC = YES

VA-CERVICAL CANCER SCREEN Taxonomy content:

CPT Code:

Q0091 Obtaining screen pap smear

88150 Cytophathology, Pap smear

Q0060-Q0061 (inactive-for historical)

P3000-P3001 (inactive-for historical)

ICD Diagnosis Code:

V76.2 Cervix;Special screening for malignant neoplasms

Added new Health Factors:

INACTIVATE CERVIX CANCER SCREEN

with “match found” fields as follows:

FREQUENCY = 0Y

USE IN APPLY LOGIC = &amp;’

ACTIVATE CERVIX CANCER SCREEN

with blank “match found” fields to continue processing.

VA-*CHOLESTEROL SCREEN (F) - Some sites may be using V82.9 for the cholesterol screen, but due to its general OTHER connotation - we are not distributing the V82.9 code in a taxonomy, since we aren’t certain how sites may be using this code. Local sites may add it to a local taxonomy and use as a result if desired.

Modified existing Taxonomy:

VA-CHOLESTEROL SCREEN

with “match found” fields as follows:

USE IN DATE DUE CALC = YES

VA-CHOLESTEROL SCREEN Taxonomy content added:

CPT Code (added to existing 83718-83721, and G0054):

80061 Lipid Panel (includes 82465)

82465 Cholesterol, serum, total

thru 82470 Assay Serum Cholesterol

83700 Assay Blood Lipids

thru 83705 Assay Blood Lipid Groups

Added Health Factor:

INACTIVATE CHOLESTEROL SCREEN

with “match found” fields as follows:

FREQUENCY = 0Y

USE IN APPLY LOGIC = &amp;’

ACTIVATE CHOLESTEROL SCREEN

with blank “match found” fields to continue processing.

VA-*CHOLESTEROL SCREEN (M)

Same changes as VA-*CHOLESTEROL SCREEN (F)

VA-*COLORECTAL CANCER SCREEN (FOBT) - Since the preventive maintenance reminders require either an FOBT “or” a SIG, this reminder provides a good example of how the reminders can be built based on other reminder results too.

**Significant number of changes**

Modified Reminder Type:

EXAM (was Laboratory Test)

Added Target Result Findings File:

EXAM with the following item:

FOBT(CLINIC)

Added existing Taxonomy to reminder:

VA-FOBT (CPT codes 82270-82273)with “match found”

fields as follows:

USE IN DATE DUE CALC = YES

Added new Taxonomy VA-COLORECTAL CANCER SCREEN to reminder:

VA-COLORECTAL CANCER SCREEN Taxonomy content:

ICD Diagnosis Code:

V76.41 Rectum; Special screening for malignant neoplasms

Note: This taxonomy could be modified in a local reminder to “Use in Date Due Calc” = YES if the site knows that a FOBT or SIG is done at an encounter with this ICD Diagnosis. It is distributed so a match will display in the reminder findings, but the finding is not used to determine when the reminder is due. This is because we are not sure how sites use this code. Does it designate whether a FOBT or SIG was done? This taxonomy is information on both the FOBT and SIG reminders.

Added new Health Factors:

INACTIVATE FOBT CANCER SCREEN

with “match found” fields as follows:

FREQUENCY = 0Y

USE IN APPLY LOGIC = &amp;’

ACTIVATE FOBT CANCER SCREEN

with blank “match found” fields to continue processing.

VA-*COLORECTAL CANCER SCREEN (SIG.)

Changed to work with FOBT results also.

****Many changes using new functionality - review entire definition****

VA-*FITNESS AND EXERCISE SCREEN

Added new Taxonomy VA-EXERCISE COUNSELING to reminder:

VA-EXERCISE COUNSELING Taxonomy content:

ICD Diagnosis Code:

V65.41 Exercise Counseling; Other counseling not otherwise specified

Not sure how to use the V69.0 Lack of physical exercise; Problems related to Lifestyle

Added new Health Factors:

INACTIVATE EXERCISE SCREEN

with “match found” fields as follows:

FREQUENCY = 0Y

USE IN APPLY LOGIC = &amp;’

ACTIVATE EXERCISE SCREEN

with blank “match found” fields to continue processing.

VA-*HYPERTENSION SCREEN

Modified existing Taxonomy:

VA-HYPERTENSION SCREEN

with “match found” fields as follows:

USE IN DATE DUE CALC = YES

VA-HYPERTENSION SCREEN Taxonomy Content =

CPT Code (added):

80060 Hypertension Panel

93770 Measurement Venous Pressure

ICD Diagnosis Code (existed):

V81.1 Hypertension; Special screening for cardiovascular, respiratory, or genitourinary diseases.

VA-*INFLUENZA IMMUNIZATION

Added new Taxonomy VA-INFLUENZA IMMUNIZATION to reminder:

VA-INFLUENZA IMMUNIZATION Taxonomy content:

ICD Diagnosis Code:

V04.8 Influenza; Need for prophylactic vaccination and inoculation against certain viral diseases

with “match found” fields as follows:

USE IN DATE DUE CALC = YES

Added new Health Factors:

INACTIVATE INFLUENZA IMMUNIZATION

with “match found” fields as follows:

FREQUENCY = 0Y

USE IN APPLY LOGIC = &amp;’

ACTIVATE INFLUENZA IMMUNIZATION

with blank “match found” fields to continue processing.

VA-*PNEUMOCOCCAL VACCINE

Modified existing Taxonomy VA-PNEUMOCOCCAL VACCINE:

VA-PNEUMOCOCCAL VACCINE Taxonomy content:

ICD Diagnosis Code (added):

V06.6 Streptococcus pneumoniae (pneumococcus) and influenza;Need for prophylactic vaccination and inoculation against certain viral diseases.

CPT Code (added):

G0009

90732

with “match found” fields as follows:

USE IN DATE DUE CALC = YES

Added new Health Factors:

INACTIVATE PNEUMOCOCCAL VACCINE

with “match found” fields as follows:

FREQUENCY = 0Y

USE IN APPLY LOGIC = &amp;’

ACTIVATE PNEUMOCOCCAL VACCINE

with blank “match found” fields to continue processing.

VA-*PROBLEM DRINKING SCREEN

Added new Taxonomy VA-ALCOHOLISM SCREENING to reminder:

VA-ALCOHOLISM SCREENING Taxonomy content:

ICD Diagnosis Code:

V79.1 Alcoholism; Special screening for mental disorders and developmental handicaps

with “match found” fields as follows:

USE IN DATE DUE CALC = YES

Added new Health Factors:

INACTIVATE PROBLEM DRINKING SCREEN

with “match found” fields as follows:

FREQUENCY = 0Y

USE IN APPLY LOGIC = &amp;’

ACTIVATE PROBLEM DRINKING SCREEN

with blank “match found” fields to continue processing.

VA-*SEATBELT AND ACCIDENT SCREEN

-----------------------------------

Reminder Type:	EDUCATION

Print Name:	Seatbelt and Accident Screen

Related VA-* Reminder:	VA-*SEATBELT AND ACCIDENT SCREEN

Reminder Description:

Seatbelt and accident education given yearly to all patients.

This "VA-*SEATBELT AND ACCIDENT SCREEN" reminder is based on the "Seatbelt Use and Accident Avoidance Counseling" guideline specified in the VHA HANDBOOK 1101.8, APPENDIX A.

Target Condition: Motor vehicle associated injuries.

Target Group: General Outpatient population.

Recommendation: All patients should be urged to use seatbelts in automobiles, wear helmets when riding bicycles or motorcycles, and to refrain from driving after drinking.

Goal for FY 2000: 85% of Veterans report regular use of seatbelts in automobiles. 80% of motorcyclists and 50% of bicyclists report use of helmets. 50% of primary care providers routinely provide age-appropriate counseling on safety precautions to prevent unintentional injury.

Technical Description:

If this reminder is not going to be used at your facility, the INACTIVE FLAG should be set to inactive.

This reminder represents the minimum criteria for checking if the patient has had seatbelt and accident screening. The "VA-SEAT BELT USE SCREENING" education topic is the result finding that will satisfy this reminder.

The Ambulatory Care EP recommends a variation on this reminder, represented in the "VA-SEATBELT EDUCATION" reminder. This reminder includes a check for seatbelt use education given to the patient, in addition to the screening.

Please review both of these reminder definitions, choose one of them to use. If local modifications need to be made, copy the preferred reminder to a new reminder and make your reminder modifications.

Target Groups - Baseline:

Do In Advance Time Frame:	Do if DUE within 1 month

Sex Specific:

Ignore on N/A:

Frequency for Age Range:	1 year for all ages

Match Text:	Seatbelt education due yearly for all patients.

No Match Text:

Targeted Result Findings for EDUCATION reminder type:

EDUCATION TOPICS

VA-SEAT BELT USE SCREENING

Target Result Match Text:

No Match Text

Target Conditions:

1 Diagnosis/Procedure Taxonomy Findings:

Taxonomy:	VA-SAFETY COUNSELING (TF(35))

Match freq/age:

Rank Frequency:

Use in Date Due Calc:	YES

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

2 Health Factor Findings:

Health Factor:	INACTIVATE SEATBELT SCREEN (HF(61))

Match Freq/Age:	0Y - Not Indicated for all ages

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:	AND NOT

Match Text:

No Match Text:

Health Factor:	ACTIVATE SEATBELT SCREEN (HF(62))

Match Freq/Age:

Rank Frequency:

Use in Date Due Calc:

Use in Apply Logic:

Match Text:

No Match Text:

General Match Text:

General No Match Text:

3 Computed Findings:

Default APPLY LOGIC to see if the Reminder should apply to a patient:

(SEX)&amp;(AGE)&amp;'(HF(61))

Expanded Apply Logic:

(SEX)&amp;(AGE)&amp;'(HF(INACTIVATE SEATBELT SCREEN))

VA-*TETANUS DIPHTHERIA IMMUNIZATION

Added new Taxonomy VA-TETANUS DIPHTHERIA to reminder:

VA-TETANUS DIPHTHERIA Taxonomy content:

ICD Diagnosis Code (V-codes added):

V03.5 Diphtheria alone

V03.7 Tetanus toxoid alone

V06.1 Diphtheria-tetanus-pertussis, combined (DTP)

V06.3 Diphtheria-tetanus-pertussis with poliomyelitis (DTP + polio)

V06.5 Tetanus-diphtheria (Td),;Need for prophylactic vaccination and

inoculation against combinations of diseases

with “match found” fields as follows:

Use in Date Due Calc = Yes

Added new Health Factors:

INACTIVATE TD IMMUNIZATION

with “match found” fields as follows:

Frequency = 0Y

Use in Apply Logic = &amp;’

ACTIVATE TD IMMUNIZATION

with blank “match found” fields to continue processing.

VA-*TOBACCO USE SCREEN

Some sites may be using V69.8 for the tobacco screen, but due to its general OTHER Problems related to lifestyle” connotation - we are not distributing the V69.8 code in a taxonomy. If you know your site is only using this code for tobacco screening, then it is acceptable to build a local taxonomy with this V-code defined for your sites tracking purposes.

Added new Health Factors:

INACTIVATE TOBACCO USE SCREEN

with “match found” fields as follows:

Frequency = 0Y

Use in Apply Logic = &amp;’

ACTIVATE TOBACCO USE SCREEN

with blank “match found” fields to continue processing.

VA-*WEIGHT AND NUTRITION SCREEN

Added new Taxonomy VA-WEIGHT AND NUTRITION SCREEN to reminder:

VA-WEIGHT AND NUTRITION SCREEN Taxonomy content:

ICD Diagnosis Code:

V65.3 Dietary surveillance and counseling; Other persons seeking consultation without complaint or sickness

V77.8 Obesity;Special screening for endocrine, nutritional,metabolic, and immunity disorders

with “match found” fields as follows:

Use in Date Due Calc = Yes

Added new Health Factors:

INACTIVATE WEIGHT/NUTRITION SCREEN

with “match found” fields as follows:

Frequency = 0Y

Use in Apply Logic = &amp;’

ACTIVATE WEIGHT/NUTRITION SCREEN

with blank “match found” fields to continue processing.

**9. New Reminder Definitions Distributed**

a. **New Definitions**

VA-DIABETIC FOOT EXAM

VA-DIABETIC EYE EXAM

VA-DIABETIC FOOT CARE ED.

b. **Changed Ambulatory Care EP Definitions (VA- Prefix):**

#### Changes made were similar to the VA-* prefixed equivalent

VA-ALCOHOL ABUSE EDUCATION

VA-BLOOD PRESSURE CHECK

VA-EXERCISE EDUCATION

VA-FECAL OCCULT BLOOD TEST

VA-FLEXISIGMOIDOSCOPY

VA-INFLUENZA VACCINE

VA-MAMMOGRAM

VA-NUTRITION/OBESITY EDUCATION

VA-PAP SMEAR

VA-PPD

VA-PNEUMOVAX

VA-SEAT BELT EDUCATION

VA-TOBACCO EDUCATION

**10. PCE TAXONOMY (File 811.2) Content Changes**

a.	Changed the name of entry 17 from ALCOHOL ABUSE to VA-ALCOHOL ABUSE. (Released 	without the VA- prefix)

b.	New Taxonomy entries distributed:

VA-ALCOHOLISM SCREENING	34

VA-CERVICAL CANCER SCREEN	30

VA-COLORECTAL CANCER SCREEN	31

VA-DIABETES	28

VA-EXERCISE COUNSELING	32

VA-FOBT	27

VA-INFLUENZA IMMUNIZATION	33

VA-SAFETY COUNSELING	35

VA-TETANUS DIPHTHERIA	29

VA-WEIGHT AND NUTRITION SCREEN	36

c.	Changed these existing taxonomy entries previously distributed:

VA-CHOLESTEROL	24

VA-HYPERTENSION SCREEN	23

VA-MAMMOGRAM/SCREEN	16

VA-PNEUMOCOCCAL VACCINE	25

d.	Standardized short description text for the taxonomies.

EXAM (File 9999999.15) new entries distributed:

-------------------------------------------------------

FOBT(CLINIC)

HEALTH FACTOR (File 9999999.64) new entries distributed:

-------------------------------------------------------

REMINDER CATEGORY

ACTIVATE BREAST CANCER SCREEN

ACTIVATE CERVIX CANCER SCREEN

ACTIVATE CHOLESTEROL SCREEN

ACTIVATE EXERCISE SCREENING

ACTIVATE FOBT CANCER SCREEN

ACTIVATE INFLUENZA IMMUNIZATION

ACTIVATE PNEUMOCOCCAL VACCINE

ACTIVATE PROBLEM DRINKING SCREEN

ACTIVATE SEAT BELT SCREEN

ACTIVATE SIGMOIDOSCOPY

ACTIVATE TD IMMUNIZATION

ACTIVATE TOBACCO USE SCREEN

ACTIVATE WEIGHT/NUTRITION SCREEN

INACTIVATE BREAST CANCER SCREEN

INACTIVATE CERVIX CANCER SCREEN

INACTIVATE CHOLESTEROL SCREEN

INACTIVATE EXERCISE SCREENING

INACTIVATE FOBT CANCER SCREEN

INACTIVATE INFLUENZA IMMUNIZATATION

INACTIVATE PNEUMOCOCCAL VACCINE

INACTIVATE PROBLEM DRINKING SCREEN

INACTIVATE SEAT BELT SCREEN

INACTIVATE SIGMOIDOSCOPY

INACTIVATE TD IMMUNIZATION

INACTIVATE TOBACCO USE SCREEN

INACTIVATE WEIGHT/NUTRITION SCREEN

**11. Documentation Changes**

Clinical Reminders Patch manuals:

Release Notes	PXRNP16.PDF

User Manual	PXUMP16.PDF

This documentation, which describes the new functionality introduced by patch 16, is available on the Software Services Web page ((152.127.1.95) and the following FTP servers:

IRM FIELD OFFICE	FTP ADDRESS	DIRECTORY

================	=============	===================

REDACTED

The documentation files are in the form of Adobe Acrobat files.

PXUMP16.PDF replaces Chapter 10 and Appendix A in the PCE User Manual, as well as Appendix C in the PCE Technical Manual. Rather than update both of these appendices, we combined the two for this patch. These pages haven’t been incorporated into the existing PCE documentation (PXUM.PDF and PXTM.PDF) because of the extent of the changes.