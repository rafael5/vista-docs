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
source_file: pxrm_2_2_um_appd.docx
status: draft
title: pxrm 2 2 um appd.docx
---

**Appendix D: VA GEC Reports**

In December 2003, a Healthcare Inspection by the Department of Veteran Affairs Office of Inspector General was conducted on the Homemaker/Home Health Aide Program to evaluate Department of Veteran Affairs (VA) Medical facilities compliance with the Veteran Health Administration (VHA) policy for providing services to patients that were clinically appropriate, cost effective, and met customer expectations. The outcome of that Inspection revealed a lack of supportable data for placement of patients.

As part of the Undersecretary for Health’s commitment to complying with VA policy, the need for accurately documenting and reporting patient placements is needed. VA Geriatric Extended Care (VA GEC) Reports will serve as an interim reporting method until the national rollup of VA GEC Referral data is provided through Computerized Patient Record System Reengineered (CPRS-R). VA GEC Reports will display the percent of patients referred to select GEC programs who meet the eligibility criteria as outlined in the Under Secretary for Health’s Information Letter IL 10-2003-005 and VHA Handbook 1140.2.

VA GEC Reports will provide quarterly statistical reports on the following VA funded programs.

- Homemaker/Home Health Aide, when Funding Source=VA
- Adult Day Health Care, when Funding Source=VA
- VA In-Home Respite, when Funding Source=VA
- Care Coordination, when Funding Source=VA

Select data from the VA Geriatric Extended Care Referral screening tool, released with Clinical Reminders 2.0, will be used in calculating the criteria totals for patients screened and referred for each of the four programs listed above.

### Data Elements for Reporting taken from the VA GEC Referral Screening of the following:

- Source
- Living Situation
- Instrumental Activities of Daily Living
- Basic Activities of Daily Living
- Patient Behaviors and Symptoms
- Cognitive Status
- Prognosis

### Data Elements for Reporting taken from Patient File and Scheduling File

Age of Patient is 75 years or greater

Patient Identified as a High Utilizer of Medical Services

### Implementation Requirements

The stakeholder will create an Excel spreadsheet for the purpose of importing the data received from the local sites, according to the specifications provided in the Algorithm that follows.

Local sites must task the job by setting the queue to automatically generate the quarterly reports.

The Office of Geriatric and Extended Care is responsible for importing data received, via electronic email, into a GEC created excel spreadsheet.

## Product Features

The main feature of this product is the creation of a report that will allow monitoring compliance of VA patients referred to specified VA funded Geriatric Extended Care programs.

- Create a tool that will extract the data on patients meeting the criteria from the VA funded GEC program.
- The extracted data will be emailed to appropriate compliance office.

### New Option

GEC Fiscal Quarterly Rollup [PXRM GEC2 QUARTERLY ROLLUP]

This is a queueable option that will gather and report to Washington DC the Fiscal Quarterly information. This option should never be placed on an individual’s menu. It should be scheduled for the 8th day of the first month of the next calendar quarter at any time of the facility’s choosing. The rescheduling frequency should be set to “3M” (every three months).

### New Mail Group

GEC2 NATIONAL ROLLUP

When this mail group is installed, it will contain the email address of the two individuals in Washington DC who will receive the quarterly data. These names should not be removed. Names of local individuals (for example, CACs) may be added, if they desire to receive these reports.

### Important NOTE:

We recommend thorough testing of GEC reminder dialogs by staff prior to implementation to avoid GEC report roll-up inaccuracies. Testing of GEC reminder dialogs and reports in a test account should mimic the actual processes and workload capture used in the site's production environment.

Informatics staff and GEC referral staff should work together to identify potential issues that arise during testing that may require modification of clinical processes and/or workload capture. Accurate capture and reporting of GEC referral health factors may require careful analysis of workload capture processes at sites that use Event Capture software. Inaccurate reporting may lead to questions from the Inspector General’s office concerning funding for the patients referred to the “Home Help” type of programs.

### Potential issues if you use Event Capture

(reported by a test site):

1. Event capture does not pass workload to PCE in real time. Data is not passed to PCE until after hours, so this needs to be taken into account when testing.
2. There are several steps where real front-line users could make minor mistakes that would result in data entry/workload not matching up with the Care coordination note.
    1. Event capture date/time must be an exact match to the date/time of PCE/TIU
    2. Clinic location must be the same.
    3. Data passes after hours from EC to PCE.
    4. There is no drop-down menu to select from. 1 and 2 above must be manually entered.
    5. Patient name must be re-selected (or use spacebar return).

## Algorithm For GEC (Next Generation) Software

The information for the “criteria” is taken from the letter # IL 10-2004-005 entitled UNDER SECRETARY FOR HEALTH’S INFORMATION LETTER dated May 3 2004. pages B-2 and B-3

The following is the Algorithm or thought process that will be used in the software to determine if a patient meets the criteria necessary to be placed in one of the monitored programs. HEALTH FACTORS that are part of the patient record for an evaluation, are designated with capital letters (below).

7D = 7 days

YES or NO = Yes or No response from the Dialog Additional explanations found to the right of health factor

**Initial Requirement is to be referred to one of the following VA funded programs** . ( Requires **1** or **6,** plus one of the other Health Factors)

1. GEC ADULT DAY HEALTH CARE (REFERRED TO)
2. GEC HOMECARE FUNDING-VA
3. GEC HOMEMAKER/HOME HEALTH AIDE
4. GEC VA IN-HOME RESPITE
5. GEC HOME TELEHEALTH (REFERRED TO)
6. GEC TELEHEALTH FUNDING-VA

### Criteria #1 : “Three or more Activities of Daily Living (ADL) dependencies.”

(Any 3 of the ADL’s below)

- GEC BATHING HELP/SUPERVISION LAST 7D-YES
- GEC BED POSITIONING HELP LAST 7D-YES
- GEC DRESS HELP/SUPERVISION LAST 7D-YES
- GEC EATING HELP/SUPERVISION LAST 7D-YES
- GEC INDEPENDENT IN WC LAST 7D-YES
- GEC MOVING AROUND INDOORS LAST 7D-YES
- GEC TOILET HELP/SUPERVISION LAST 7D-YES
- GEC TRANSFERS HELP/SPRVISION LAST 7D-YES

### OR

**Criteria #2 : “Significant cognitive impairment** ” (Any 1 of those indicated below)

- GEC CAN BE UNDERSTOOD LAST 7D-NO
- GEC ENDANGERED SAFETY LAST 90D-YES
- GEC MADE REASONABLE DECISIONS LAST 7D-NO
- GEC HALLUCINATIONS/DELUSIONS LAST 7D-YES
- GEC PHYSICALLY ABUSIVE LAST 7D-YES
- GEC RESISTS CARE LAST 7D-YES
- GEC VERBALLY ABUSIVE LAST 7D-YES
- GEC WANDERING LAST 7D-YES

### OR

**Criteria #3 “ Prognosis of Life Expectancy of less than 6 months”**

(Any 1 of these health factors )

- GEC LIFE EXPECTANCY &lt; 6MO-YES

### OR

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

### AND

“(a) Dependency in three or more Instrumental ADL (IADL)” (Any 3 of the IADL)

- GEC DIFFICULT TRANSPORTATION/LAST 7D-YES
- GEC DIFFICULTY MANAGING MEDS/LAST 7D-YES
- GEC DIFFICULTY MNG FINANCES/LAST 7D-YES
- GEC DIFFICULTY PREPARE MEALS/LAST 7D-YES
- GEC DIFFICULTY USING PHONE/LAST 7D-YES
- GEC DIFFICULTY W/ HOUSEWORK/LAST 7D-YES
- GEC DIFFICULTY WITH SHOPPING/LAST 7D-YES

### OR

“(b) Recent discharge from a nursing home, or upcoming nursing home discharge plan contingent

on receipt of home and community – based care services.”

- GEC COMMUNITY NRSNG HOME (REFERRED FROM)
- GEC VA DOMICILIARY (REFERRED FROM)
- GEC VA NURSING HOME

### OR

“(c) Seventy Five Years old , or older.”

(Obtained from the Patient’s Records using an API call)

### OR

“(d) High use of medical services defined as **three** or more hospitalizations in the past year and/or utilization of outpatient and/or emergency evaluation units **twelve** or more times in the past year.

( The API ….GETAPPT^SDAMA201(…) to retrieve appointments etc.)

### OR

“(f) Living alone in the Community”

- GEC ALONE

## Example: Home Health Eligibility Report (All patients)

Use the GEC Referral Report on the Reminder Managers Menu to produce reports.

CF	Reminder Computed Finding Management ... RM	Reminder Definition Management ...

SM	Reminder Sponsor Management ... TXM	Reminder Taxonomy Management ... TRM	Reminder Term Management ...

LM	Reminder Location List Management ... RX	Reminder Exchange

RT	Reminder Test

OS	Other Supporting Menus ...

INFO	Reminder Information Only Menu ... DM	Reminder Dialog Management ...

CP	CPRS Reminder Configuration ... RP	Reminder Reports ...

MST	Reminders MST Synchronization Management ... PL	Reminder Patient List Menu ...

PAR	Reminder Parameters ... XM	Reminder Extract Menu ... GEC	GEC Referral Report

Select Reminder Managers Menu Option: **GEC** GEC Referral Report All Reports will print on 80 Columns

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

Select Option or ^ to Exit: 8// **9** 'Home Help' Eligibility

Select a year for the report (i.e.2005) YEAR or ^ to exit:	(2004-2030): **2005**

Select a Fiscal QUARTER in the year 2005 (i.e.2) Fiscal Years start in October.

Fiscal Quarter 1 same as Calendar Quarter 4 Fiscal Quarter 2 same as Calendar Quarter 1 Fiscal Quarter 3 same as Calendar Quarter 2 Fiscal Quarter 4 same as Calendar Quarter 3

Fiscal Quarter or ^ to exit: (1-4): **2**

Select one of the following:

A M

All Patients Multiple Patients

Select Patients or ^ to exit: A// **&lt;Enter&gt;** ll Patients

Select one of the following:

Y	YES

N	NO

Select Show Test Patients in this Report? Y or N or ^ to exit: **YES**

DEVICE: HOME// **;;999** ANYWHERE	Right Margin: 80//

Please wait ...

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

## Example 2: Home Health Eligibility Report (Multiple patients)

This report lets you select individual patient names.

Select Reminder Managers Menu Option: **GEC** GEC Referral Report

All Reports will print on 80 Columns

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

Select Option or ^ to Exit: 9// **9** 'Home Help' Eligibility

Select a year for the report (i.e.2005) YEAR or ^ to exit:	(2004-2030): **2005**

Select a Fiscal QUARTER in the year 2005 (i.e.2) Fiscal Years start in October.

Fiscal Quarter 1 same as Calendar Quarter 4 Fiscal Quarter 2 same as Calendar Quarter 1 Fiscal Quarter 3 same as Calendar Quarter 2 Fiscal Quarter 4 same as Calendar Quarter 3

Fiscal Quarter or ^ to exit: (1-4): **2**

Select one of the following:

A M

All Patients Multiple Patients

Select Patients or ^ to exit: A// **M** ultiple Patients

DEVICE: HOME//	ANYWHERE	Right Margin: 80// Please wait ...

=============================================================================

Referred to Homemaker/Home Health Aide(HHHA) or Adult Day Health Care(ADHC) or VA In-Home Respite(VAIHR) or Care Coordination programs(CC)

From: 01/01/2005 To: 03/31/2005

Fiscal Quarter: 2 (Calendar Quarter 1)

Criteria

Name	SSN	Prog.	0	#1 #2 #3 #4 Date	Not Eligible

=============================================================================

## Example: National Data Report

673,7,ADHC,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

673,8,ADHC,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

673,9,ADHC,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

673,7,CC,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

673,8,CC,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

673,9,CC,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

673,7,HHHA,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

673,8,HHHA,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

673,9,HHHA,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

673,7,VAIHR,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

673,8,VAIHR,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

673,9,VAIHR,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

The above information is Geriatric Extended Care "Home" Referral data from TAMPA VAMC #673 for Fiscal Quarter # 4 of 2008. (Calendar Quarter 3)

Each section of data is separated by a comma. The table below defines the sections. Numbers represent Patients. Patient only counted once.

1. Number for the site.
2. Number that stands for the Month (1=January)...
3. Acronym for the Program (ADHC,HHHA,VAIHR,CC)
4. Total number of patients referred to the program that month
5. Number that DID NOT MEET ANY of the criteria
6. Number that only met criteria 1
7. Number that only met criteria 2
8. Number that only met criteria 3
9. Number that only met criteria 4
10. Number that only met both criteria's 1 and 2
11. Number that only met both criteria's 1 and 3
12. Number that only met both criteria's 1 and 4
13. Number that only met both criteria's 2 and 3
14. Number that only met both criteria's 2 and 4
15. Number that only met both criteria's 3 and 4
16. Number that only met the criteria's 1 and 2 and 3
17. Number that only met the criteria's 1 and 2 and 4
18. Number that only met the criteria's 1 and 3 and 4
19. Number that only met the criteria's 2 and 3 and 4
20. Number that met all criteria's, 1 and 2 and 3 and 4

The Basic Criteria for Eligibility is shown below.

1: Problems with 3 or more ADL's.

2: 1 or more patient behavior or cognitive problem. 3: Expected life limit of less than 6 months.

4: Combination of the following:

2 or more ADL dependencies.

&lt;AND&gt; 2 or more of the following: problems with 3 or more IADL's.

&lt;OR&gt; age of patients is 75 or more.

&lt;OR&gt; living alone in the community.

&lt;OR&gt; utilizes the clinics 12 or more times in the preceding 12 months.