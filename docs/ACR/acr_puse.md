---
app_name: Ambulatory Care Reporting (ACR)
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: 2018-10
doc_type: user-manual
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-11'
is_base: false
is_change_pages: false
library_max_patch: null
package_id: ACR
patch: 640
patch_gap: null
section: ''
source_file: acr_puse.docx
status: draft
title: acr puse.docx
---

**PIMS V. 5.3 Scheduling Module User Manual**

**Ambulatory Care Reporting Menu**

ACRP Reports Menu

ACRP Ad Hoc Report Menu

ACRP Ad Hoc Report

Delete an Ad Hoc Report Template

Display Ad Hoc Report Template Parameters

Print from Ad Hoc Template

Clinic Appointment Availability Report

Clinic Group Maintenance for Reports

Clinic Utilization Statistical Summary

Data Validation Menu

Enc. by IP DSS ID/DSS ID by Freq. (IP0, IP1, IP2)

Means Test IP Visits &amp; Uniques (IP3, IP4, IP5)

Most Frequent 50 IP CPT Codes (IP6)

Most Frequent 50 IP ICD Diagnosis Codes (IP7)

Most Frequent 20 IP Practitioner Types (IP8)

Visits and Unique IP SSNs by County (IP9)

Enc. by DSS ID/DSS ID by Freq. (OP0, OP1, OP2)

Means Test Visits &amp; Uniques (OP3, OP4, OP5)

Most Frequent 50 CPT Codes (OP6)

Most Frequent 50 ICD Diagnosis Codes (OP7)

Most Frequent 20 Practitioner Types (OP8)

Visits and Unique SSNs by County (OP9)

Encounter Activity Report

Encounter ‘Action Required’ Report

Means Test/Eligibility/Enrollment Report

Outpatient Diagnosis/Procedure Frequency Report

Outpatient Diagnosis/Procedure Code Search

Outpatient Encounter Workload Statistics

Patient Activity by Appointment Frequency

Patient Appointment Statistics

Patient Encounter List

Performance Monitor Menu

Performance Monitor Summary Report

Performance Monitor Detailed Report

Performance Monitor Retransmit Report (AAC)

Review of Scheduling/PCE/Problem List Data

Retroactive Visits List

SC Veterans Awaiting Appointments

Trend of Facility Uniques by 12

Veterans Without Activity Since a Specified Date

Error Listing

Transmission Reports

Transmission History Report - Full

Transmission History for Patient

Supervisor Ambulatory Care Menu

Edit Appointment Type for Add/Edit Encounters

Check Transmitted Outpatient Encounter Files

Purge Ambulatory Care Reporting files

Scheduling/PCE Bad Pointer Count

Edit Outpatient Encounter

Purge rejections that are past database close-out

Data Transmission Report

Incomplete Encounter Management

Incomplete Encounter Reports

Alpha List of Incomplete Encounters

Encounters Transmitted with MT Status of U

Incomplete Encounter Error Report

Incomplete Encounters by Error Code

Summary Report - IEMM

Correct Incomplete Encounters

Retransmit Ambulatory Care Data by

Retransmit Selected Error Code

Selective Retransmission of NPCDB Rejections

Revision History

Initiated on 1/12/07

| **Date**   | **Description (Patch # if applic.)**                                                                                                                                                                                                                  | **Project Manager**   | **Technical Writer**   |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|------------------------|
| Oct 2018   | Updated to reflect changes from patch SD*5.3*640, ACRP and APM HL7 Shutdown. This includes adding notations regarding the ACRP and APM transmissions and related menu options that are being disabled. See pages 4, 5, 9, 13, 36, 50, 64, 74, 75, 76. | redacted              | redacted               |
| June 2014  | SD*5.3*593 – Updated title to MOST FREQUENT 50 IP ICD DIAGNOSIS CODES (IP) every occurrence  Updated title to MOST FREQUENT 50 IP ICD DIAGNOSIS CODES (OP7) every occurrence  Updated ICD-9-DM CODES to the generic “ICD”                             | redacted              | redacted               |
| 11/28/11   | SD*5.3*560 – Updated option:  Edit Outpatient Encounter                                                                                                                                                                                               | redacted              | redacted               |
| 1/29/09    | Name change update - Austin Automation Center (AAC) to Austin Information Technology Center (AITC)                                                                                                                                                    | redacted              | redacted               |
| 8/14/08    | Minor formatting changes                                                                                                                                                                                                                              | redacted              | redacted               |
| 2/22/07    | SD*5.3*466 - Ambulatory Care, Phase II enhancements                                                                                                                                                                                                   | redacted              | redacted               |
| 1/12/07    | SD*5.3*358 – Updated options:  Veterans Without Activity Since a Specified Date  SC Veterans Awaiting Appointments                                                                                                                                    | redacted              | redacted               |

**Overview**

The Ambulatory Care Reporting Project (ACRP) enhances the process of collecting and storing encounter-based clinical, diagnostic, and administrative outpatient and inpatient data for daily transmission to the Austin Information Technology Center (AITC), (formerly the Austin Automation Center (AAC)).

The Ambulatory Care project will be working in concert with the National Patient Care Database project (NPCDB).  The two projects have common objectives.

1. Capture and record selected demographic data about the patient
2. Identify the date and time services were provided
3. Identify what was done, why it was done, and who provided the services
4. Move the information from  to the NPCDB via an Event Driven Reporting mechanism for the purpose of workload credit

**NOTE:** Starting October 1, 2018, the Ambulatory Care nightly job and Performance Monitor data extract daily transmissions, and monthly APM Performance Monitor Task generated from each VistA site are no longer needed to be sent to the AITC; the NPCDB is being shut down in Austin and the Corporate Data Warehouse (CDW) is replacing the database as the authoritative source. The VistA extracts done to populate the CDW will replace the need for the HL7 transmission.

This transmission has been stopped with Scheduling patch SD*5.3*640. This patch release includes:

- Disable AMB-CARE and SDPM logical links in the HL LOGICAL LINK file (#870).
- Unschedule the following three tasks:
    - Ambulatory Care Nightly Transmission to NPCDB [SCDX AMBCAR NIGHTLY XMIT]
    - Nightly job for PM data extract [SDOQM PM NIGHTLY JOB]
    - Schedule APM Performance Monitor Task [SCRPW APM TASK JOB].
- Place the following options ‘out of order’:
    - Ambulatory Care Nightly Transmission to NPCDB [SCDX AMBCAR NIGHTLY XMIT]
    - Retransmit Ambulatory Care Data by Date Range [SCDX AMBCAR RETRANS BY DATE]
    - Retransmit Selected Error Code [SCDX AMBCAR RETRANS ERROR]
    - Selective Retransmission of NPCDB Rejections [SCDX AMBCAR RETRANS SEL REJ]
    - Schedule APM Performance Monitor Task [SCRPW APM TASK JOB]
    - Performance Monitor Retransmit Report (AAC) [SCRPW PM RETRANSMIT REPORT]
    - Nightly job for PM data extract [SDOQM PM NIGHTLY JOB]
Collecting more specific and encounter-based clinical, diagnostic, and administrative data will enable more detailed analysis of VHA’s outpatient and inpatient healthcare activity.  Tracking the amount of care provided across the types of healthcare services offered will be key in the calculation of corporate costs.  The information will also be a valuable database for resource utilization studies, forecasting, and healthcare planning for the future.
All options in the ACRP Reports menu have been modified to return multiple reports when multiple divisions are selected.  For example, if you select division A and division B, the output will contain a report for division A, a report for division B, and a report that reflects the combination of divisions A and B.
**Overview**
The following is a brief description of the options contained in the Ambulatory Care Reporting Menu.
ACRP REPORTS MENU
ACRP AD HOC REPORT MENU
ACRP AD HOC REPORT
This option allows creation of workload reports in many variations according to specified parameters.
DELETE AN AD HOC REPORT TEMPLATE
This option is used to delete report templates that are no longer used.
DISPLAY AD HOC REPORT TEMPLATE PARAMETERS
This option displays report parameters that are stored as a template.
PRINT FROM AD HOC TEMPLATE
This option allows the printing of workload reports from pre-defined templates.
CLINIC APPOINTMENT AVAILABILITY REPORT
The Clinic Appointment Availability Report provides clinic availability and utilization statistics for a selected data range.  It can be used to validate data transmitted to  via the Clinic Waiting Time extracts.
CLINIC GROUP MAINTENANCE FOR REPORTS
This option allows for entering, editing, and printing clinic groups and clinic
group assignments which are used for reports.
CLINIC UTILIZATION STATISTICAL SUMMARY
This option is used to print clinic utilization statistics for a specified date range.
DATA VALIDATION MENU
ENC. BY IP DSS ID/DSS ID BY FREQ. (IP0, IP1, IP2)
This option produces a report that returns inpatient statistics by DSS Identifier in a format that matches the Austin IP0, IP1, and IP2 reports.
MEANS TEST IP VISITS &amp; UNIQUES (IP3, IP4, IP5)
This option produces a summary of inpatient Means Test visits and uniques in a format that matches the Austin IP3, IP4, and IP5 reports.
**Overview**
MOST FREQUENT 50 IP CPT CODES (IP6)
This option produces a listing of the 50 most frequent inpatient ambulatory procedure codes with associated provider type frequency in a format that matches the Austin IP6 report.
MOST FREQUENT 50 IP ICD DIAGNOSIS CODES (IP7)
This option produces a listing of the 50 most frequent inpatient diagnoses with associated provider type frequency in a format that matches the Austin IP7 report.
MOST FREQUENT 20 IP PRACTITIONER TYPES (IP8)
This option produces inpatient practitioner type frequency statistics in a format that matches the Austin IP8 report.
VISITS AND UNIQUE IP SSNs BY COUNTY (IP9)
This option provides counts of inpatient encounters, visits, and uniques by state and county in a format that matches the Austin IP9 report.
ENC. BY DSS ID/DSS ID BY FREQ. (OP0, OP1, OP2)
This option produces a report that returns outpatient statistics by DSS Identifier in a format that matches the Austin OP0, OP1, and OP2 reports.
MEANS TEST VISITS &amp; UNIQUES (OP3, OP4, OP5)
This option produces a summary of outpatient Means Test visits and uniques in a format that matches the Austin OP3, OP4, and OP5 reports.
MOST FREQUENT 50 CPT CODES (OP6)
This option produces a listing of the 50 most frequent outpatient ambulatory procedure codes with associated provider type frequency in a format that matches the Austin OP6 report.
MOST FREQUENT 50 ICD DIAGNOSIS CODES (OP7)
This option produces a listing of the 50 most frequent outpatient diagnoses with
associated provider type frequency in a format that matches the Austin OP7
report.
MOST FREQUENT 20 PRACTITIONER TYPES (OP8)
This option produces outpatient practitioner type frequency statistics in a format that matches the Austin OP8 report.
**Overview**
VISITS AND UNIQUE SSNs BY COUNTY (OP9)
This option provides counts of outpatient encounters, visits, and uniques by state and county in a format that matches the Austin OP9 report.
ENCOUNTER ACTIVITY REPORT
This option produces a report of encounter, visit, and unique patient
statistics by selected clinic, provider, or stop code.
ENCOUNTER ‘ACTION REQUIRED’ REPORT
This option is used to print a report of “action required” encounters in detailed
or statistics format for a specified date range.
MEANS TEST /ELIGIBILITY/ENROLLMENT REPORT
This option is used to produce statistics of encounters, visits, and uniques by encounter Means Test indicator, encounter eligibility, and current enrollment priority.
OUTPATIENT DIAGNOSIS/PROCEDURE FREQUENCY REPORT
This option produces a report which returns ranked lists of diagnoses and procedures by frequency.
OUTPATIENT DIAGNOSIS/PROCEDURE CODE SEARCH
This option produces a report which returns lists of patients that have had outpatient procedures or diagnoses within groups, ranges, or selections specified by the user.
OUTPATIENT ENCOUNTER WORKLOAD STATISTICS
This option prints outpatient encounter workload statistics based on “parent”
encounters in the OUTPATIENT ENCOUTNER file.
PATIENT ACTIVITY BY APPOINTMENT FREQUENCY
This option is used for printing patient appointment activity for a selected date
range by selected stop codes, a range of stop codes, or by clinic group.
PATIENT APPOINTMENT STATISTICS
This option prints workload statistics and patient lists related to clinic appointments.
PATIENT ENCOUNTER LIST
This option is used to print a listing of patient encounters in reverse
chronological order for a specified patient.
**Overview**
Performance Monitor Menu
Performance Monitor Summary Report
This option is used to generate a report monitoring outpatient encounters, their associated progress notes, and the number of days it took providers to sign the notes.
Performance Monitor Detailed Report
This option is used to generate a detailed report on information pertaining to outpatient encounters and the progress notes associated with them.
Performance Monitor Retransmit Report (AAC)*
This option is used to retransmit reports in the event problems are encountered with the transmission of the report generated by the background option “Schedule APM Performance Monitor Task” or to retroactively transmit previous month’s data.**Note** : Both “PERFORMANCE MONITOR RETRANSMIT REPORT (AAC)” and “Schedule APM Performance Monitor Task” options have been placed out of order with patch SD*5.3*640; the background option “Schedule APM Performance Monitor Task” has also been unscheduled since APM transmission has been discontinued.
REVIEW OF SCHEDULING/PCE/PROBLEM LIST DATA
This option is used to print a report of Scheduling, Patient Care Encounter, Visit
Tracking, and Problem List data for a selected patient and encounter date.
RETROACTIVE VISITS LIST
This option is used to print a list of appointments and/or add/edits that have been entered after workload data has been transmitted to the Austin Information Technology Center (AITC), (formerly the Austin Automation Center (AAC)).
SC VETERANS AWAITING APPOINTMENTS
This option produces a report in either one of two formats regarding service-connected (sc) veterans awaiting appointments - one lists sc veterans entered into VistA in the past year that have not been given an appointment - the other lists sc veterans with appointments where the scheduled appointment date is more than 30 days beyond the desired date defined for that appointment.
TREND OF FACILITY UNIQUES BY 12
This option is used for trending facility outpatient uniques by overlapping 12
month date ranges for the past 5 years.
*AAC stands for Austin Automation Center.  The name of that facility has been changed to Austin Information Technology Center (AITC).
**Overview**
VETERANS WITHOUT ACTIVITY SINCE A SPECIFIED DATE
This option produces a report which extracts a listing of veterans not defined as deceased that have not had medical center activity since a specified date range.
ERROR LISTING
This option is used to generate the Transmitted Outpatient Encounter Error List which contains a listing of the errors reported by the NPCDB in  for a user-specified date range.
TRANSMISSION REPORTS
TRANSMISSION HISTORY REPORT - FULL
This option provides a complete transmission history of all encounters for a
selected date range for selected divisions, clinics, and patients.
TRANSMISSION HISTORY FOR PATIENT
This option provides the ACRP transmission history of all encounters for a selected patient in a selected time frame.
SUPERVISOR AMBULATORY CARE MENU
You must hold the SD SUPERVISOR security key to access these options except for the Edit Outpatient Encounter option which requires the SCENI ENCOUNTER EDIT key.
EDIT APPOINTMENT TYPE FOR ADD/EDIT ENCOUNTERS
This option is used to edit the appointment type for add/edit encounters.
CHECK TRANSMITTED OUTPATIENT ENCOUNTER FILES
This option searches the OUTPATIENT ENCOUNTER file (#409.68) for encounters that are “checked out” but have no entry in the TRANSMITTED OUTPATIENT ENCOUNTER file (#409.73).
PURGE AMBULATORY CARE REPORTING FILES
This option purges the TRANSMITTED OUTPATIENT ENCOUNTER file (#409.73) of all encounters that occurred during a user-specified date range.
SCHEDULING/PCE BAD POINTER COUNT
This option reports the numbers of patient appointments and dispositions with
missing or incorrect outpatient encounter pointers.
**Overview**
EDIT OUTPATIENT ENCOUNTER
This option allows you to edit four fields from the OUTPATIENT ENCOUNTER file (#409.68).
PURGE REJECTIONS THAT ARE PAST DATABASE CLOSE-OUT
This option purges the TRANSMITTED OUTPATIENT ENCOUNTER ERROR file (#409.75) of encounter rejections that cannot be transmitted due to the NPCD database close-out.
DATA TRANSMISSION REPORT
This option is used to generate the NPCDB Data Transmission Report which displays a log of transmissions to the NPCDB for a user-specified date range.
INCOMPLETE ENCOUNTER MANAGEMENT
Incomplete Encounter Reports
ALPHA LIST OF INCOMPLETE ENCOUNTERS
The Alpha List of Incomplete Encounters option prints a list of all errors found in the TRANSMITTED OUTPATIENT ENCOUNTER ERROR file (#409.75) at the time the report is generated.
eNCOUNTERS TRANSMITTED WITH MT STATUS OF U
This option prints a list of patients who have encounters that will transmit with a Means Test indicator of U.
Incomplete Encounter Error Report
The Incomplete Encounter Error Report is used to print all inconsistencies and missing data for a selected date range for encounter records which 1) have not been transmitted or 2) have been rejected by the Austin NPCD.
Incomplete Encounters by error code
The Incomplete Encounters by Error Code option is used to print the errors in the TRANSMITTED OUTPATIENT ENCOUNTER ERROR CODE file (#409.76).
summary Report - iemm
This report prints a summary showing total encounters for a date range and the number and percentage of incomplete encounters.
CORRECT INCOMPLETE ENCOUNTERS
This option is used to view and correct incomplete encounters.
**Overview**
RETRANSMIT AMBULATORY CARE DATA BY DATE RANGE
This option is used to mark outpatient encounters within a user-specified date range for retransmission to the NPCDB in .**Note:** This option has been placed out of order with patch SD*5.3*640 since ACRP transmission has been discontinued.
RETRANSMIT SELECTED ERROR CODE
This option allows users to re-flag encounter activity with a specified error code for transmission to NPCDB.**Note:** This option has been placed out of order with patch SD*5.3*640 since ACRP transmission has been discontinued.
SELECTIVE RETRANSMISSION OF NPCDB REJECTIONS
This option provides a list of patients who currently have rejections from NPCDB and the ability to selectively choose which encounters should be marked for retransmission.**Note:** This option has been placed out of order with patch SD*5.3*640 since ACRP transmission has been discontinued.
**ACRP Reports Menu**
**ACRP Ad Hoc Report Menu**
**ACRP Ad Hoc Report**
This option allows creation of workload reports from the ACRP databases, in a variety of different ways, according to specified parameters.  It is based on encounter activity found in the OUTPATIENT ENCOUNTER file.
***Parameter Selection***
Parameter selection for this report is presented in a series of screens that group each type of parameter.  The actual set of parameter prompts will vary depending on the type of report being selected.
On the first screen, general introductory information is displayed.  If Ad Hoc report templates have been previously defined, the user is provided the opportunity to select an existing template.  Parameters restored from existing templates can be reviewed and edited prior to queueing to a device.  If an existing template is not selected, the next screen presented begins selection of a fresh set of report parameters.
After all the parameters have been selected, you will be given the opportunity to edit the parameters before the report is printed.  Holders of the SC AD HOC TEMPLATE security key may create a report parameter template that can be reused.
**Report Format**
Format determines the appearance of the report.  If summary format is selected, the user may specify the inclusion of a comparison of data from the selected date range to the same date range in the previous year.  In detailed format, lists of patients or ranked lists of diagnoses and procedures (or both) may be selected.
Output can be produced as formatted text or in delimited format for ease of transfer into spreadsheet software for further formatting or manipulation.
**Report Perspective**
The data type selected at this point determines what data element will be used to organize and accrue workload subtotals for output.  In instances where a given data element returns a null value (no data) for a patient or encounter, this will be represented on the output by the text value ~~~NONE~~~.  If detailed format has been selected, the user will be required to select actual data element values for which they wish to produce detail lists.
**ACRP Reports Menu**
**ACRP Ad Hoc Report Menu**
**ACRP Ad Hoc Report**
**Report Limitations**
Parameters selected at this point determine the scope of the data that will be returned.  At a minimum, a date range must be selected.Multiple data elements may be selected as additional limitations.  For each additional limitation, the user must choose a list or range of data values for that element and specify if encounters where this particular data element is found should be included or excluded from the report. **All** of the “include” factors must be true for an encounter to be included; however, an encounter will be excluded if **any** of the “exclude” factors are true.
**Report Print Order**
The next screen allows the user to define output order as alphabetical (by the data value of the selected perspective data type) or by the data element subtotal of encounters, visits, or uniques.  A descriptive title may also be specified which will be included in the header of the report.
If detailed format that includes patient lists has been selected, another screen will be displayed that allows the selection of additional print fields to include in the patient list portion of the report.  Data elements may also be selected.  However, if detail by patient or visit has been specified, only “patient-related” data elements may be selected.  If detail by encounter is specified, any of the data elements may be selected.
***Interpreting Delimited Output***
Although it is a single output, the delimited format of this report contains multiple tables that represent the sections of the formatted-text style of the report.  Each table is separated with a dashed line header.  The first row of each table represents the column headers for that table.
*Notice to IRM staff and ACRP Ad Hoc Report Users*
The ACRP Ad Hoc Report is designed to be a powerful and flexible tool for extracting workload data and statistics from the Ambulatory Care Reporting Project database.  However, like using VA FileMan to produce output for complex search criteria, this report has the potential to have a noticeable impact on computer response time when system use is heavy.
**ACRP Reports Menu**
**ACRP Ad Hoc Report Menu**
**ACRP Ad Hoc Report**
Due to the multiplicity inherent in the data that constitutes ambulatory care reporting, sizeable temporary globals for the purpose of tracking unique patient, visit, and encounter statistics may be created during the processing of large reports.
It is recommended that users begin with conservative date ranges and report specifications until they are familiar with report format and corresponding system impact.  It may be indicated that extensive reports should be queued to process during other than normal working hours.
**ACRP Reports Menu**
**ACRP Ad Hoc Report Menu**
**Delete an Ad Hoc Report Template**
Holders of the SC AD HOC TEMPLATE security key may create report parameter templates through the ACRP Ad Hoc Report option that can be reused and shared with others.  This option is used to delete those report templates that are no longer needed.
Only holders of the SC AD HOC TEMPLATE security key may access this option.
**ACRP Reports Menu**
**ACRP Ad Hoc Report Menu**
**Display Ad Hoc Report Template Parameters**
Holders of the SC AD HOC TEMPLATE security key may create report parameter templates through the ACRP Ad Hoc Report option that can be reused and shared with others. This option provides a method to display to the screen or print to a print device the report parameters that are stored as the selected template.  No editing is allowed through this option.
Information displayed may include report format, report perspective, report limitations, report print order, and template information such as date created, created by, and date last edited.
The only prompts are for template name and device.
**ACRP Reports Menu**
**ACRP Ad Hoc Report Menu**
**Print from Ad Hoc Template**
Holders of the SC AD HOC TEMPLATE security key may create report parameter templates through the ACRP Ad Hoc Report option that can be reused and shared with others.  This option allows users to print reports using those templates. Parameters contained in the selected template cannot be edited through this option.
While the ACRP Ad Hoc Report requires a certain amount of orientation to use, this option is intended to provide a method by which users without such orientation may select existing report parameters and produce reports accordingly.  It allows users of the ACRP Ad Hoc Report to define “canned” reports that can easily be shared with others.  Sites may wish to assign this option separately to users as indicated.
The output includes a cover page showing the report parameters selected.  Report output is the same as would be produced using the ACRP Ad Hoc Report.
**ACRP Reports Menu**
**Clinic Appointment Availability Report**
The Clinic Appointment Availability Report provides clinic availability and utilization statistics for a selected data range.  It can be used to validate data transmitted to  via the Clinic Waiting Time extracts.
Two extracts will be performed on a recurring basis.  One will look prospectively at appointment slot availability and report open slots and clinic capacity for each day of a specified number of days into the future (initially, 180 days).  Data will be reported individually for each division/credit pair/clinic combination found.  The other extract will look at availability retrospectively and report the number of open slots, clinic capacity, and patient encounters for each of a specified number of days in the past (initially, the prior month).  This data will be reported in the same way as the first extract.
A report will be sent to the members of the SC CLINIC WAIT TIME mail group at the end of each extract run.  This report will provide a summary of the data contained in the transmitted extract.  Data contained in this report will reflect availability as of the report run date/time.  Due to facility data entry and appointment scheduling since the run time of a specific extract, this report may not exactly match extracted data but should accurately reflect clinic availability at the time of the report.
The Clinic Appointment Availability report may be run for one/many/all divisions.  You may choose to print the report in summary or detail format.  In the detail format, clinic availability may be limited by clinic name or DSS credit pair.
If you select to print the report in summary format you may limit clinics by selecting only desired DSS credit pairs.  Additionally, you may print "Listing of appointments for selected patients" by selecting the report in detail format.  Unlimited number of patients may be entered for receiving their appointment history in all or selected clinics.
This report sorts by date range of the "date scheduled", prints selected patients alphabetically, and includes appointment status, completion date for canceled/no-show/check-out appointments, and scheduling/canceling person's name.  To follow up the continuity of related appointments the rebook date is available, if applicable.
**ACRP Reports Menu**
**Clinic Group Maintenance for Reports**
This option allows for entering, editing, deleting, and printing clinic groups and clinic group assignments which are used by various reports in the ACRP Reports Menu.
Clinic group functionality provides a more facility-flexible manner of grouping clinics than the traditional division, service, name, and clinic stop code categories.  Assigning clinics to clinic groups allows users to organize data by group or limit output to a specific group.
Clinic groups for reports can be thought of as somewhat synonymous with primary care teams but are broader in function.  They can be used to group clinics by service provided, physical location, etc.  An example of this would be the definition of a “MHC” clinic group that would allow the  staff to obtain a report of ‘action required’ encounters for Mental Health Clinics only.
The following actions are available.
Edit Clinic Groups	Allows deletion of unused clinic group.  Cannot
delete clinic group that has clinics assigned to
it.
Print Clinic Groups	Provides a list of clinic groups, in alphabetical
order, at date/time printed.
Delete Clinic Groups	Allows editing of existing clinic group or
addition of new clinic group.
Edit Clinic Group Assignments	Allows editing of clinic group assignments
either for a selected clinic or a range of clinics.
Print Clinic Group Assignments	Provides a list of clinic group assignments
either alphabetically by clinic name or by clinic
group.  Those clinics not assigned to a clinic
group are also included.
This option is locked with the SD SUPERVISOR security key.
**ACRP Reports Menu**
**Clinic Utilization Statistical Summary**
This option is used to print clinic utilization statistics for a specified date range for one/many/all divisions.  Statistics may be printed for all clinics, selected clinics, a range of clinics, a range of stop codes, or by a single clinic group.
It is intended to provide an indication of utilization by considering a clinic’s unused (or perhaps, overused) scheduling capacity.  It includes a percentage of scheduling utilization (scheduled slots vs. total slots), and a percentage of actual utilization (scheduled slots less no-shows vs. total slots).
The accuracy of utilization as reflected by this report is dependent on the accuracy of the clinic profiles for the clinics being examined.  That is, if a clinic profile has many more slots defined than the provider could possibly see, it will appear as though the clinic has poor utilization even though the provider may be very busy.
Data elements produced on the report will include the number of scheduled appointments, additional variable appointment slots, no shows, additional variable no-show slots, overbooks, open slots, adjusted availability, clinic capacity, scheduling utilization percentage, and actual utilization percentage for each selected clinic/stop code/clinic group.  A note is provided at the bottom of each page explaining how some of the data elements on the report are derived.
When any of the clinic selection criteria is used, the output may be divided into two sections, the Clinic Summary and the Provider Summary.  The Provider Summary is based on the default providers defined for those clinics which appear in the Clinic Summary.  This may not necessarily be the provider that actually provided treatment to the patient.
A provider may have several clinics which appear in the Clinic Summary.  In the Provider Summary, the statistics from a provider’s multiple clinics are combined into a single line item.  Clinics that do not have a default provider defined are not reflected in the Provider Summary.
**ACRP Reports Menu**
**Data Validation Menu**
**Enc. by IP DSS ID/DSS ID by Freq. (IP0, IP1, IP2)**
This option produces a report which displays inpatient encounter statistics by DSS Identifier in a format that matches the Austin IP0, IP1, and IP2 reports.  This report uses the same logic as the VistA OP0, OP1, and OP2 reports that are used for outpatient encounters.
The first portion of the output (IP0, IP1) lists the inpatient encounters by DSS Identifier.  There is a column for each month of the fiscal year selected; however, data will only be provided through the selected date.
The second portion of the output (IP2) displays the inpatient encounters by DSS ID by frequency.  Information provided includes frequency as primary, frequency as credit, # of male/female encounters, # of male/female uniques, total encounters, and total uniques.
If more than one division is selected, a report will print for each division as well as a summary page for all divisions.
**ACRP Reports Menu**
**Data Validation Menu**
**Means Test IP Visits &amp; Uniques (IP3, IP4, IP5)**
This option produces a summary of inpatient Means Test visits and uniques in a format that matches the Austin IP3, IP4, and IP5 reports.  This report uses the same logic as the VistA OP3, OP4, and OP5 reports that are used for outpatient encounters.
If more than one division is selected, a report will print for each division as well as a summary page for all divisions.
The three portions of the report are as follows.
*Means Test Visit Summary*
Current month Means Test visits and year-to date Means Test visits by category.
*Means Test Visit Summary (Unique SSNs Based on Latest Visit)*
Current month Means Test uniques and year-to-date Means Test uniques by category.
*Means Test Uniques by Gender, POW Status and Age*
Current month Means Test by category broken down by uniques such as gender, POW status, and age groups.
**ACRP Reports Menu**
**Data Validation Menu**
**Most Frequent 50 IP CPT Codes (IP6)**
This option produces a listing of the 50 most frequent inpatient ambulatory procedure codes with associated provider type frequency in a format that matches the Austin IP6 report. This report uses the same logic as the VistA OP6 report that is used for outpatient encounters.
Information provided includes rank, CPT code (number and name), CPT code frequency, provider type, and provider type frequency.
If more than one division is selected, a report will print for each division as well as a summary page for all divisions.
**ACRP Reports Menu**
**Data Validation Menu**
**Most Frequent 50 IP ICD Diagnosis Codes (IP7)**
This option produces a listing of the 50 most frequent inpatient diagnoses with associated provider type frequency in a format that matches the Austin IP7 report.  This report uses the same logic as the VistA OP7 report that is used for outpatient encounters.
Information provided includes rank, ICD diagnosis code number and name, provider type, number of primary diagnosis uniques, total uniques, primary diagnosis encounters, and total encounters.
If more than one division is selected, a report will print for each division as well as a summary page for all divisions.
**ACRP Reports Menu**
**Data Validation Menu**
**Most Frequent 20 IP Practitioner Types (IP8)**
This option produces inpatient practitioner type frequency statistics in a format that matches the Austin IP8 report.  This report uses the same logic as the VistA OP8 report that is used for outpatient encounters.
Information provided includes rank, VA Code #, specialty, subspecialty, and frequency.
If more than one division is selected, a report will print for each division as well as a summary page for all divisions.
**ACRP Reports Menu**
**Data Validation Menu**
**Visits and Unique IP SSNs by County (IP9)**
This option produces counts of inpatient encounters, visits, and uniques by state and county in a format that matches the Austin IP9 report.  This report uses the same logic as the VistA OP9 report that is used for outpatient encounters.
Information provided includes county; state; number of visits, encounters, and uniques.
If more than one division is selected, a report will print for each division as well as a summary page for all divisions.
**ACRP Reports Menu**
**Data Validation Menu**
**Enc. by DSS ID/DSS ID by Freq. (OP0, OP1, OP2)**
This option produces a report which returns statistics by DSS Identifier in a format that matches the Austin OP0, OP1, and OP2 reports.
The first portion of the output (OP0, OP1) lists the encounters by DSS Identifier.  There will be a column for each month of the fiscal year selected; however, data will only be provided through the selected date.
The second portion of the output (OP2) shows DSS ID by frequency.  Information provided includes frequency as primary, frequency as credit, # of male/female encounters, # of male/female uniques, total encounters, and total uniques.
If more than one division is selected, a report will print for each division as well as a summary page for all divisions.
**ACRP Reports Menu**
**Data Validation Menu**
**Means Test Visits &amp; Uniques (OP3, OP4, OP5)**
This option produces a summary of Means Test visits and uniques in a format that matches the Austin OP3, OP4, and OP5 reports.  If more than one division is selected, a report will print for each division as well as a summary page for all divisions.
The three portions of the report are as follows.
*Means Test Visit Summary*
Current month Means Test visits and year-to date Means Test visits by category.
*Means Test Visit Summary (Unique SSNs Based on Latest Visit)*
Current month Means Test uniques and year-to-date Means Test uniques by category.
*Means Test Uniques by Gender, POW Status and Age*
Current month Means Test by category broken down by uniques such as gender, POW status, and age groups.
**ACRP Reports Menu**
**Data Validation Menu**
**Most Frequent 50 CPT Codes (OP6)**
This option produces a listing of the 50 most frequent ambulatory procedure codes with associated provider type frequency in a format that matches the Austin OP6 report.
Information provided includes rank, CPT code (number and name), CPT code frequency, provider type, and provider type frequency.
If more than one division is selected, a report will print for each division as well as a summary page for all divisions.
**ACRP Reports Menu**
**Data Validation Menu**
**Most Frequent 50 ICD Diagnosis Codes (OP7)**
This option produces a listing of the 50 most frequent diagnoses with associated provider type frequency in a format that matches the Austin OP7 report.
Information provided includes rank, ICD diagnosis code number and name, provider type, number of primary diagnosis uniques, total uniques, primary diagnosis encounters, and total encounters.
If more than one division is selected, a report will print for each division as well as a summary page for all divisions.
**ACRP Reports Menu**
**Data Validation Menu**
**Most Frequent 20 Practitioner Types (OP8)**
This option produces practitioner type frequency statistics in a format that matches the Austin OP8 report.
Information provided includes rank, VA Code #, specialty, subspecialty, and frequency.
If more than one division is selected, a report will print for each division as well as a summary page for all divisions.
**ACRP Reports Menu**
**Data Validation Menu**
**Visits and Unique SSNs by County (OP9)**
This option produces counts of encounters, visits, and uniques by state and county in a format that matches the Austin OP9 report.
Information provided includes county; state; number of visits, encounters, and uniques.
If more than one division is selected, a report will print for each division as well as a summary page for all divisions.
**ACRP Reports Menu**
**Encounter Activity Report**
This option provides a report of encounter, visit, and unique patient statistics within a specified date range by one of three selected perspectives:  clinic, provider, or stop code.  It can be produced in summary or detailed format.
In the summary format, counts of encounters, visits, and uniques are displayed for each of the items in the selected perspective, as well as a report total for the three workload elements.   The output can be produced alphabetically or by frequency of encounters, visits, or uniques.
Detail format allows selection of specific clinics, providers, or stop codes.  For each of the items selected, it will produce frequency ranked lists of diagnoses and procedures recorded (including the procedure modifiers), in addition to counts of encounters, visits, and uniques.
**ACRP Reports Menu**
**Encounter ‘Action Required’ Report**
This option is used to print a report of ‘action required’ encounters in detailed or statistics only format for a specified date range.
You may print the data for all clinics, selected clinics, a range of clinics, all clinic groups, or an individual clinic group.  The report requires 132 column output.
The detailed format allows the following print order selection within clinics:  alphabetic, date/time, or terminal digit.  The user can select continuous output (without pagination by clinic) or output that produces a separate page for every clinic.  This format includes both detailed lists and a statistical summary.
The detailed lists are organized by clinic and include patient name, SSN, date/time of encounter and type (scheduled appointment, add/edit, disposition, etc.).  It also reflects the check-in and check-out user (if defined) and attempts to list all of the data elements that are required for transmission to the National Patient Care Database (NPCDB).**Note:** The transmission to NPCDB has been shut down with patch SD*5.3*640.
The statistics only format (and the statistics portion of the detailed format) provides counts of deficiencies by reason and by clinic location.  Counts by deficiency reason are likely to be greater than counts by location since a single encounter may have more than one deficiency reason.  These statistics will be organized and subtotaled by clinic group if output by clinic group is selected.
**ACRP Reports Menu**
**Means Test/Eligibility/Enrollment Report**
This option is used to produce statistics of encounters, visits, and uniques for a selected date range by the following categories:  encounter Means Test indicator, encounter eligibility, and current enrollment priority.
The detailed format of this report will produce lists of patients sorted by one of the three above-mentioned categories.  You may then specify sub-sorts.  These optional sort selections include the following.  Additional sorts are available under these choices.
Diagnosis
Patient Demographics
Patient Eligibility
Primary Care
Enrollment (current)
In instances where a given data element returns a null value (no data) for a patient or encounter, this will be represented by the text value ~~~NONE~~~.
The output includes a cover page showing the report parameters selected.
If more than one division is selected, a report will print for each division as well as a summary page for all divisions.
**ACRP Reports Menu**
**Outpatient Diagnosis/Procedure Frequency Report**
This option produces a report which returns ranked lists by diagnosis frequency, procedure frequency, or both diagnosis and procedure frequency for a selected date range.
Information provided may include code number, procedure, diagnosis, number of times primary diagnosis, number of times secondary diagnosis, and total frequency.  In addition, the associated procedure modifier(s) will be displayed.
If more than one division is selected, a report will print for each division as well as a summary page for all divisions.
**ACRP Reports Menu**
**Outpatient Diagnosis/Procedure Code Search**
This option produces a report which returns lists of patients that have had
outpatient procedures or diagnoses within groups, ranges, or selections specified
by the user.
As criteria for the search, the user is required to define search elements that consist of diagnosis or procedure lists or ranges.  Up to 26 search elements can be specified.  As each element is defined, it is assigned an alphabetic character (“A”, “B”, “C”, etc.) which is used to refer to the search element when specifying the combine logic that will be used to produce the report.
When all desired search elements have been selected, the user is prompted to enter combine logic.  Similar to VA FileMan search functionality, combine logic determines how the selected elements will be applied in the search.  As with FileMan, the apostrophe ( ’ ) can be used to negate an individual element.
For example, if you wish to produce a list of patients with a diagnosis of COPD and who had undergone a bronchoscopy, you could define element “A” as a diagnosis range that encompasses the appropriate ICD codes and element “B” as a procedure list that contains the CPT codes representing bronchoscopy procedures.  By specifying the combine logic “AB”, you can produce a listing where both elements were recorded within the date range specified.
If you want to produce a list of patients with diagnoses in the range 250.0 to 250.9 excluding diagnoses 250.4 to 250.6, you can define element “A” as a diagnosis range 250.0 to 250.9 and element “B” as a diagnosis range 250.4 to 250.6.  Then by specifying a combine logic of “A’B” you could produce a listing of diagnoses in the larger first range, but not in the second range.
Multiple combine logic statements may be entered.  The report will return instances where any of these rules are found to be true.  A single combine logic statement applies “AND” logic—the statement “ABC” means “A&amp;B&amp;C”.  “OR” logic may be created by entering more than one combine statement.  If the first statement is “A” and the second is “B”, the resulting logic will be “A or B”.
The next prompt allows the user to specify if the report should produce a detail list by patient unique, visit, or encounter.  Additional print fields may also be selected.  Only “patient related” data elements may be selected as additional print fields if the detail is by patient or visit.  Detail by encounter allows the selection of “encounter related” data elements as well.
**ACRP Reports Menu**
**Outpatient Diagnosis/Procedure Code Search**
Selected report parameters are displayed prior to queueing.  The user may print or redisplay the parameters or may quit without queueing the report.
If more than one division is selected, a report will print for each division as well as a summary page for all divisions.  The output also includes a cover page showing the report parameters selected.
**ACRP Reports Menu**
**Outpatient Encounter Workload Statistics**
This option provides a comprehensive accounting of encounter workload broken out by type and status for a specified date range.  It provides statistics of encounters, visits, and uniques for a facility and by division (if multidivisional).  Users may optionally obtain a breakout of statistics by clinic group; detailed lists of encounters, visits, or uniques for a division; or a list of ‘action required’/not accepted unique patients.
This report is based on counts of “parent" encounters in the OUTPATIENT ENCOUNTER file.  The entry of encounter data normally results in the creation of multiple records in the OUTPATIENT ENCOUNTER file, representing the primary stop code, the credit stop code (if any), and the addition of procedure codes.  A checked-out encounter will normally consist of 2-3 records in the OUTPATIENT ENCOUNTER file.
A patient encounter will consist of a single “parent” encounter (the primary stop code record).  As such, a count of “parent” encounters is an accurate reflection of patient encounter workload.  Conceptually, an “encounter” consists of all of the related data stored in the OUTPATIENT ENCOUNTER, VISIT and PCE “V” files.
In the FileMan sense, the term "parent" used here refers to records where the PARENT ENCOUNTER field is null.  "Child" encounters are outpatient encounter records that contain a pointer in this field to another outpatient encounter record.Facility workload, via transmission to the National Patient Care Database (NPCDB), is derived from "parent" encounters that have a status of *checked out* and have been referred to the transmission process.  Information contained in "child" encounters is not referred directly to the transmission process, but rather, gathered with the "parent" encounter when the "parent" encounter is transmitted.The **Outpatient Encounter Workload Section** of the report is a count of "parent" outpatient encounters by status values that are considered to be "for credit".  These statuses include *checked in* , *checked out* , *no action taken* , *inpatient appointment* , *future* , and *action required* .  Only statuses found in the database for the date range are reflected on the report.
**ACRP Reports Menu**
**Outpatient Encounter Workload Statistics**Within the *checked out* category of the Outpatient Encounter Workload section, encounters are further subcategorized by transmission status.  Only subcategories that are found will appear on the report.  These subcategories include the following.**No transmission record** - “Parent" encounters that are checked out but have not been referred to the transmission process (which should have happened when the record was checked out).**Rejected for transmission** - Encounters which have failed to pass the checks for data elements required for transmission of workload to .**Not required, not transmitted** - Encounters that have been referred to the transmission process (they have a record in the TRANSMITTED OUTPATIENT ENCOUNTER file) but are not flagged to be transmitted, nor have they been transmitted.**Awaiting transmission** - Records that have been referred to the transmission process since the last nightly transmission.  They will be sent in the next nightly transmission if they pass the pre-transmission screening requirements.**Transmitted, no acknowledgement** - Encounters that have been referred to HL7 for transmission to .  If there were no problems with HL7, they have been sent to .  The number in this category should roughly match the average number of encounters produced by a facility on any given work day.  If these numbers are substantially greater than the facility's average daily workload, it may indicate a problem with HL7 has caused a failure to transmit data to ; or it may indicate a problem with the incoming filer that processes the acknowledgment messages returning from .**Transmitted, rejected** - Encounters that have been sent to  but have failed the requirements for filing into NPCDB.**Transmitted, error** - One of the possible  acknowledgement statuses (not currently in use).**Transmitted, accepted** - Encounters that have been sent to , processed, and an acknowledgment message indicating acceptance has been returned to the facility.  This indicates the encounter has been recorded in NPCDB for national facility workload credit.
**ACRP Reports Menu**
**Outpatient Encounter Workload Statistics**
Only encounters in the Outpatient Encounter Workload section (encounters with "for credit" statuses) are used to calculate visits and uniques as reflected in the Facility Outpatient Visits and Facility Outpatient Uniques sections of this report.The **Non-Workload Section** of the report is a count of "parent" encounters by statuses that are not given outpatient workload credit (nationally).  These include *deleted* , *non-count* , *no-show* , and *cancelled* statuses.  Only statuses that are found will appear on the report.The **Facility Outpatient Visits Section** of the report is a count of one per patient per day (regardless of the number of encounters a patient may have had on a given day).  For multi-divisional sites, the station totals are not the sum of all divisions.  If a patient was seen at more than one division on a single day, they reflect as a visit to each division; however, they are still just a single visit for the facility on that date (as calculated by this report).
A patient visit will accrue to only one of the subcategories in this section.  If a patient had multiple encounters on a single day and as few as one of those encounters has a "transmitted, accepted" status, the patient's visit will accrue in the 'Transmitted, accepted visits” subcategory.  If none of the patient's encounters on that date have a "transmitted, accepted" status, the visit will accrue to the “Act. Req./not accepted” subcategory.The **Facility Outpatient Uniques Section** of the report is a count of one per patient for the entire date range (regardless of the number of visits a patient had).  For multi-divisional sites, the station totals are not a sum of all of the divisions.  If a patient was seen at more than one division during the date range, they reflect as a unique patient for each division; however, they are still counted as a single unique for the facility (as calculated by this report).
The unique patient will accrue to only one of the subcategories in this section.  If the patient had multiple visits during the date range and as few as one of those visits had an encounter with a "transmitted, accepted" status, the unique will accrue to the 'Transmitted, accepted unique pts.” subcategory.  If none of the patient's visits had any encounters with a "transmitted, accepted" status, the unique will accrue to the “Act. Req./not accepted unique pts.” subcategory.
**ACRP Reports Menu**
**Patient Activity by Appointment Frequency**
This option is used for printing patient appointment activity for a selected date range for one/many/all divisions.  You may choose to print by selected stop codes, a range of stop codes, or by clinic group.  You may then specify the output order as alphabetic or by visit frequency.
Output from this report will include counts by clinic and stop code for each appointment that is within the parameters specified by the user.  A list of future appointments is also provided for each patient identified.
This report can be used by clinical staff to identify patients that are using an excessive amount of resources and assist them in consolidating and managing future care in a more cost effective manner.
**ACRP Reports Menu**
**Patient Appointment Statistics**
The Patient Appointment Statistics option is used for printing workload statistics and patient lists related to clinic appointments for a selected date range.  The report reflects uncancelled appointment workload including walk-in (unscheduled) appointments.   It does not represent all outpatient activity.
You may choose the report format from the following criteria.
    - All clinics, selected clinics, or a range of clinics
    - Selected stop codes or a range of stop codes
    - Clinic group
You may then choose to list patient names on the report and, if so, choose how the names will appear within each clinic - alphabetically, by appointment date/time, or by terminal digit.
**ACRP Reports Menu**
**Patient Encounter List**
This option is used to print a listing of patient encounters in reverse chronological order for a specified patient and date range.  Data items include date/time of encounter, encounter location, encounter number, encounter type, and transmission status.
It is formatted for printer output or convenient CRT display and provides a quick way to review all encounters entered for a patient during the date range specified.  This can be useful for performing data validation and verifying the current completion or transmission status of an individual encounter.
**ACRP Reports Menu**
**Performance Monitor Menu**
**Performance Monitor Summary Report**
The Performance Monitor Summary Report option generates a report of outpatient encounters within a user-selected time frame using nationally defined screening criteria to identify encounters requiring progress notes.  The report reflects encounter counts for the entire facility and also breaks down the counts for each division.
Information provided includes the following.
    - Total number of encounters
    - Average time span, in days, that it takes the provider to sign a progress note
    - Percentages by elapsed time and frequency for an acceptable signature
    - Total number of notes needing acceptable signatures
    - Total number of encounters having only a scanned note (Imaging)
The only prompts are for a date range and device.  The report can be queued to run at any time; however, the end date must precede the report run date by at least 14 days.
**ACRP Reports Menu**
**Performance Monitor Menu**
**Performance Monitor Detailed Report**
The Performance Monitor Detailed Report option generates a detailed report on information pertaining to outpatient encounters and progress notes associated with them.  It identifies the encounter, the provider, whether a note was done on an encounter, and whether the note was signed within a given time frame.  It allows reporting to a specific time period, DSS identifier, or provider to determine facility performance and compliance with the performance indicator for progress note entry.
The following defines terms as used for this report.
Progress Note	any Text Integrated Utility (TIU) document
DSS Identifier	3 character number that represents the clinic in which the care
was provided
Numerator	a checked-out patient encounter in Ambulatory Care with a
completed or amended progress note signed by the primary
provider for that encounter
Denominator	a checked-out patient encounter in Ambulatory Care in clinics
where a progress note shall be expectedEncounters that are to be excluded from both the numerator and denominator are as follows.
    - Encounters that occurred in a non-count clinic
    - Encounters that occurred under certain DSS Identifiers
    - Checked-out encounters that have only TIU scanned imagesEncounters that are to be included in the denominator but excluded from the numerator are as follows.
    - Progress notes with a status of unsigned, unco-signed, undictated, untranscribed, unverified, unreleased, purged, deleted, or retracted
    - Progress notes signed by other than an acceptable provider even if the note status is completed or amended.
**ACRP Reports Menu**
**Performance Monitor Menu**
**Performance Monitor Detailed Report**
The user can define the screening criteria for the report with the following fields.
*Number of days for elapsed time*
This is the number of acceptable days elapsed before signing the note; used for flagging note as compliant/non-compliant.  The time span from end to time the report is run has to be at least two days.
*Start and end date of report*
The time span from start date to end date must be at least as great as the time limit entered for acceptable signatures.
*Division and Provider*
Choose one/many/all.
*Stop codes by range*
Provides the ability to select the stop codes individually, by range, or combination (e.g., 100,302  or 200-450,800).  If the default value of NO is entered here, you will proceed to the “Select Stop Code” prompt.
*Stop code (DSS ID)*
Choose one/many/all.  If ALL is selected you will be asked if you want all stop codes and credit pairs in the Performance Monitor national cohort or not.
*Count scanned notes*
Should encounters with scanned (Imaging) notes be counted on the report - Yes/No.
The user can define the primary and secondary sort criteria for the report by choosing from the following list:  division, clinic, provider, stop code, date, and patient.
**ACRP Reports Menu**
**Performance Monitor Menu**
**Performance Monitor Retransmit Report (AAC)***
The Performance Monitor Retransmit Report (AAC) option is used to transmit Performance Monitor (TIU) data to the Austin Information Technology Center (AITC), (formerly the Austin Automation Center (AAC)), in the event problems were encountered with the data transmission generated by the background option “Schedule APM Performance Monitor Task”.**Note:** This option has been placed out of order with patch SD*5.3*640 since ACRP and APM transmissions have been discontinued.The “Schedule APM Performance Monitor Task” option is scheduled to run on the 15 th of each month as a background job.  A local mail group, SD PM NOTIFICATION TIU will receive notification when the process completes.  This mail group will also receive reject messages from the server in the event that a problem is encountered with the transmission.**Note:** This option has been unscheduled and placed out of order with patch SD*5.3*640 since the APM transmission has been discontinued.
The Performance Monitor Retransmit Report (AAC) option can also be used to retroactively transmit previous month’s extracts.
The only prompts are for the month/year of the TIU’s National Rollup to transmit and a start time.  You may enter a date/time or time only.  If only the time is entered, the current date is assumed.  Time is required as part of the response.
*AAC stands for Austin Automation Center.  The name of that facility has been changed to Austin Information Technology Center (AITC).
**ACRP Reports Menu**
**Review of Scheduling/PCE/Problem List Data**
This option is used to print information obtained from the Scheduling, Outpatient Encounter, Visit Tracking, and Patient Problem List databases.  It provides a method of reviewing all data elements filed in conjunction with encounter data entry.
The report is run for a selected patient and encounter date.  Two different report formats are available - short or long.  The short format of the report does not include the Visit Tracking and Patient Problem List portions of the output.
This output is intended to provide comprehensive output of all encounter data filed for a patient activity date.  Due to the nature of the databases involved, the data returned is lengthy and in some respects redundant.  It is not designed for routine use but is a valuable tool for performing critical single-patient encounter data entry validation, and for examining database relationships when examples of problem encounters that cannot be processed normally are identified.
**ACRP Reports Menu**
**Retroactive Visits List**
The Retroactive Visits List option is used to print a list of encounters and/or add/edits that have been entered after workload data has been transmitted to the Austin Information Technology Center (AITC), (formerly the Austin Automation Center (AAC)).  The report may be used as a tool to help control late check ins.  It should be noted that non-count clinics are excluded.
The option provides for two different types of close-out check; database update only (to make sure the database is correct) or workload credit (for reimbursement).  You will then be prompted for a date range (of visit dates), and for one/many/all divisions (at multidivisional facilities).  You may choose to find the data by stop code (one/many/all) or clinic (one/many/all).  If stop code is selected, the system will look at all clinics in the specified division(s) that match the stop code(s), then look at the add/edits for the specified stop code(s).  If clinic is selected, the system will look at the clinic(s) specified, then look at the add/edits for any associated clinic(s) that match the specified clinic(s).
The output will list the encounter date/time, date entered, date transmitted, patient name, patient ID, type (standalone or add/edit), user who entered, and clinic (clinic will only appear for add/edits when an associated clinic has been specified.)  The total number of encounters will also be provided.
**ACRP Reports Menu**
**SC Veterans Awaiting Appointments**
This option produces a report in two different formats regarding service-connected veterans awaiting appointments.  One format lists service-connected veterans entered into  in the past year that have not yet been given an appointment.  The other format lists service-connected veterans with appointments in the future where the scheduled appointment date is more than 30 days beyond the 'desired date' defined for that appointment.
Data items include patient name and social security number, primary eligibility, date entered, address, and phone number.  You may choose to run the report for all service-connected veterans, those 50 to 100% service connected, or those 0-50% service connected.  For patients that are 0-50% service connected, a list of rated service-connected disabilities is included.  In the format related to future appointments, those appointments that are greater than 30 days beyond the 'desired date' are displayed.
You may choose to print a detailed report or statistics only.  The detailed format will include the statistical report page.
The detailed report may also be printed in delimited format as shown below.
NAME^SSN^PRIM. ELIG.^DATE ENTERED INTO FILE^STREET ADDRESS^CITY^STATE^ZIP^PHONE NUMBER
FRED,LUMPY^444-44-4443^SC &lt; 50%^^^^^^**NOTE:** Once the Scheduling Replacement application has been implemented at your site, this report will no longer be accurate.
**ACRP Reports Menu**
**Trend of Facility Uniques by 12**
This option is used for trending facility inpatient and outpatient uniques by overlapping 12 month date ranges for the past 5 years.  You may run the report for one/many/all divisions.  Output includes a count of uniques for each 12 month date range and displays a histogram that represents the volume of these uniques.
You may run the report for checked out outpatients, checked out inpatients, or both.  At multiple division facilities, the report may be run for one/many/all divisions.
The output includes a count of uniques for each 12 month date range and displays a histogram that represents the volume of these uniques.
**ACRP Reports Menu**
**Veterans Without Activity Since a Specified Date**
This option produces a report which extracts a listing of veterans, not defined as deceased, that have not had medical center activity since a specified date range.  Activity is determined by an examination of fee basis authorizations, inpatient and outpatient care (including future appointments).
You may specify sub-sorts of the detail lists.  These optional sort selections include the following.  Additional sorts are available under these choices.
Diagnosis
Patient Demographics
Patient Eligibility
Primary Care
Enrollment (current)
In instances where a given data element returns a null value (no data) for a patient or encounter, this will be represented by the text value ~~~NONE~~~.
Information provided on the report includes patient name, social security number, date of last activity, location of last activity, Means Test, and primary eligibility.**NOTE:** Once the Scheduling Replacement application has been implemented at your site, this report will no longer be accurate.
**Error Listing**
This option generates the Transmitted Outpatient Encounter Error List which contains a listing of the errors reported by the National Patient Care Database (NPCDB) for a user-specified date range.  The error code description describes why the encounter data could not be filed in the NPCDB.
If you select the default of first at the “Start with date…” prompt, the report will automatically print to the last date.
Information provided may include patient name, encounter date, hospital location, error code, error code description, and date/time of transmission to NPCDB.
**Transmission Reports**
**Transmission History Report - Full**
The Transmission History Report - Full option provides a complete transmission history of all encounters for a selected date range for selected divisions, clinics, and patients.  The date range is applied to the transmission date and not the encounter date.
Information provided on the report includes patient name followed by brief ID (last four of SSN), encounter date, encounter unique visit ID, date transmitted, acknowledgment code, and whether or not transmission of the encounter occurred before workload close-out (yes or no).
The report is printed alphabetically by division name and within that by clinic name.  The division name, division number, and clinic name are provided in the footer on each page of the report.
**Transmission Reports**
**Transmission History for Patient**The Transmission History for Patient option provides a history of all encounters for a selected patient during a selected time frame.  All transmissions of the encounter are included on the report, even if the transmission occurred after the date range selected (as the date range signifies encounter date not transmission date).
The report is sorted by encounter date and includes subtotals for the total number of times each encounter was transmitted and acknowledged.  Information provided on the report includes encounter date, encounter unique visit ID, hospital location, date transmitted, acknowledgment code, and whether or not transmission of the encounter occurred before workload close-out (yes or no).
**Supervisor Ambulatory Care Menu**
**Edit Appointment Type for Add/Edit Encounters**
This option provides the ability to redesignate appointment types for computer-generated encounters that inappropriately received a “regular” appointment type in the SCHEDULING VISITS file (#409.5).
You may run this option for patients who have appointment type error codes of 405, 406, 4050, or 4060.  Select the appropriate appointment.  The appointment date, location, and type will be displayed.  You are then prompted for the correct appointment type -  which will usually be “computer generated”.
Once the appointment type for these add/edit encounters has been changed to computer generated, you may use the Computer Generated Menu [SDACS CGMENU] to process the correct appointment type for these encounters.
**Supervisor Ambulatory Care Menu**
**Check Transmitted Outpatient Encounter Files**
This option searches the OUTPATIENT ENCOUNTER file (#409.68) for encounters that are “checked out” but have no entry in the TRANSMITTED OUTPATIENT ENCOUNTER file (#409.73).  If these encounters are for non-count clinics, the status of the encounter is changed to “non-count”.  If the encounter is for a count clinic and no transmission record exists, a transmission record is created in File #409.73.
**Supervisor Ambulatory Care Menu**
**Purge Ambulatory Care Reporting files**
This option will purge the TRANSMITTED OUTPATIENT ENCOUNTER file (#409.73) of all encounters that occurred during a user-specified date range.  This will result in the deletion of corresponding entries in the DELETED OUTPATIENT ENCOUNTER file (#409.74), the TRANSMITTED OUTPATIENT ENCOUNTER ERROR file (#409.75), and the ACRP TRANSMISSION HISTORY file (#409.77).
The beginning date of the date range cannot be prior to .  The ending date of the date range cannot be later than the last day of the month prior to the last National Patient Care Database close-out date.  For example, if the last National Patient Care Database close-out occurred on , then the allowable date range for purging would be  through .
A sample of the mail message sent by the ACRP purger is provided.
Subj: Purging of ACRP files from  to  [#63541]
4 Lines
From: ACRP PURGER in ‘IN’ basket.  Page 1  **NEW**
-----------------------------------------------------------------------------
10000 entries were purged from the Transmitted Outpatient Encounter file (#409.73).  9900 of them pointed to entries in the Outpatient Encounter file (#409.68) and 100 of them pointed to entries in the Deleted Outpatient Encounter file (#409.74).
**Supervisor Ambulatory Care Menu**
**Scheduling/PCE Bad Pointer Count**
Discrepancies have been noted between the PATIENT file (#2) APPOINTMENT and DISPOSITION LOG-IN DATE/TIME multiples and the entries they point to in the OUTPATIENT ENCOUNTER file (#409.68).  In some cases the encounter pointed to does not exist, and in other cases, it contains inconsistent data.  In a different problem, there may be more than one encounter entry for the same appointment or disposition, while the PATIENT file entry points to only one of these duplicates.
This option will report such discrepancies.  That information will then be used to determine the magnitude of the existing data problems.
It is suggested when running this option the date range be  to the current date.  It is also suggested this task be queued to run during off-hours.  When the task completes, a MailMan message will be sent to the user showing the numbers of patient appointments and dispositions with missing or incorrect outpatient encounter pointers.  When initially run, the same message will be sent to the ACRP team at the Albany CIO Field Office.
**Supervisor Ambulatory Care Menu**
**Edit Outpatient Encounter**
The Edit Outpatient Encounter option allows you to change four fields from the OUTPATIENT ENCOUNTER file (#409.68).  These fields are set by the software and are not editable through VA FileMan.  They may be changed only through this option or through the Encounter Information action found on the error display screen of the Correct Incomplete Encounters option.
Upon selecting an encounter, the system will echo back and display the current primary STOP CODE as a default.  At this point, the user will be permitted to edit the STOP CODE.  However, validations are made to insure only a valid STOP CODE can be selected.  For example, if the selected STOP CODE was Inactive at the time of the encounter, the user will not be permitted to select that STOP CODE and the following warning message will be displayed and the user will be returned to the STOP CODE prompt.
“Sorry, that Stop Code was INACTIVE at the time of the selected encounter.”
Also, if the Restriction Type for the selected STOP CODE  is not ‘P’ (primary only) or ‘E’ (either) and the Restriction Date is prior to the encounter date, the user will not be allowed to select this STOP CODE and the following warning message will be displayed and the user returned to the STOP CODE prompt:
“Sorry, the Restriction Type for that Stop Code is ‘S’ (secondary only).
You cannot select this stop code.”Accepting the default values at the prompts APPOINTMENT TYPE and ENTER THE ELIGIBILITY FOR THIS APPOINTMENT will change the current values displayed to those default values. For example, accepting the default of *regular* at the APPOINTMENT TYPE prompt will change the “Current Appointment Type for Encounter” from *employee* to *regular* . If *employee* is the correct value, you would need to type in *employee* at the APPOINTMENT TYPE prompt. The same logic applies to the ENTER THE ELIGIBILITY FOR THIS APPOINTMENT prompt
However, validations are made to insure only a valid APPOINTMENT TYPE can be selected.  For example, if the Service Connection Indicator in the Visit associated with the selected encounter equals YES, the user will not be allowed to change either the APPOINTMENT TYPE or the ELIGIBILITY. The following warning message will be displayed:
“The Visit associated with the selected encounter is SERVICE CONNECTED.
You cannot edit the Appointment Type or Eligibility for this encounter.”
If the Service Connection Indicator equals NO, the user will not be allowed to change the APPOINTMENT TYPE to Service Connected. The following warning message will be displayed:
“The Visit entry associated with the selected encounter is NOT SERVICE CONNECTED.  You cannot change the Appointment Type to SERVICE CONNECTED.”
If the current APPOINTMENT TYPE is Computer Generated, the same validation check will apply. When applicable, in addition to one of the above warning messages displaying, it will also display what the new Appointment Type is.  For example:
“The Visit entry associated with the selected encounter is SERVICE CONNECTED.  You cannot change the Appointment Type to non-SERVICE CONNECTED.
Appointment Type has been updated to Service Connected.”
-OR-
“The Visit entry associated with the selected encounter is NOT SERVICE CONNECTED.  You cannot change the Appointment Type to SERVICE
CONNECTED.
The Appointment Type has been updated to Regular.”
If there is only one eligibility for the patient (the primary), you will be asked if you wish to use that as the new eligibility for the encounter being edited. No additional eligibilities can be selected.
After all valid edits have been made, the system will update all applicable records with the changes, including the Outpatient Encounter file (#409.68), the Visit file (#9000010) and when applicable, the Transmit Required flag will be switched to YES in the Transmitted Outpatient Encounter file (#409.73) to insure the edited encounter is Retransmitted to Austin.**Note:** The retransmission function has been disabled with patch SD*5.3*640 since the transmission has been discontinued.
This option is only available to holders of the SCENI ENCOUNTER EDIT security key.
**Supervisor Ambulatory Care Menu**
**Purge rejections that are past database close-out**
This option will queue a task to search through the TRANSMITTED OUTPATIENT ENCOUNTER ERROR file (#409.75) for encounters that were rejected by the National Patient Care Database (NPCDB) and will not be transmitted due to closing of the NPCDB for database credit.  All entries that are found will be removed from the file and, consequently, will no longer be found on the NPCDB Data Error Report.
This option only needs to be run after the NPCDB has been closed for database credit, although running it multiple times will have no detrimental effect.  It is recommended you wait 7 days after database close-out before utilizing the option to allow return of any potential rejections from the NPCDB.
**Data Transmission Report**
This option generates a report which displays the transmission status of events within a user specified date range.  Transmission is to the National Patient Care Database.
If you select the default of first at the “Start with date…” prompt, the report will automatically print to the last date.
Information provided may include date/time of event, whether or not transmitted, type of event, date/time of transmission to NPCDB, acknowledgment status from NPCDB, patient name, and encounter date.
**Incomplete Encounter Management**
**Incomplete Encounter Reports**
**Alpha List of Incomplete Encounters**
The Alpha List of Incomplete Encounters option prints a list of all errors found in the TRANSMITTED OUTPATIENT ENCOUNTER ERROR file (#409.75) at the time the report is generated.  The report is sorted by division and, within each division, alphabetically by patient name.  Information provided includes patient name, SSN, error code, error source, encounter date, and clinic.  It is recommended the report be queued to a printer.
**Incomplete Encounter Management**
**Incomplete Encounter Reports**
**Encounters Transmitted with MT Status of U**
This report prints a list of patients who have encounters that will transmit with a Means Test indicator of 'U'.  The patient will be included on the report only if ALL the patient's encounters within the date range selected will transmit with a MTI of 'U'.  This will focus the list on patients who do not have a valid MT status in the National Patient Care Database (NPCD) for the date range chosen.
You may print for previous fiscal year, current fiscal year, or a selected date range.  The current fiscal year is the suggested date range for this report.  Please note that if you select your own date range you may not generate an accurate picture of the AMB CARE closeouts where the Means Test indicator equals 'U'.
Information provided on the report may include patient name, last four of the SSN, outpatient encounter date, Means Test indicator, medical center division, and the clinic the encounter occurred in.  The encounter will be marked with an asterisk (*) if the encounter record has been transmitted.  The report is sorted alphabetically by patient name.
Running this report will generate a MailMan message to the user initiating the report providing such information as start and end times for the report run, total time it took the report to process, how many records were scanned, how many were included in the report, and a patient count.Formatted for a 132 col. output, this report will not format correctly to an 80 column device.  The report should be scheduled to run during non-peak hours. **Incomplete Encounter Management**
**Incomplete Encounter Reports**
**Incomplete Encounter Error Report**
The Incomplete Encounter Error Report is used to print all inconsistencies and missing data for a selected date range for encounter records which 1) have not been transmitted or 2) have been rejected by the Austin National Patient Care Database (NPCD).  This provides an all-inclusive error report which may be used during the correction process.The *sort* criteria will always be by division, clinic, patient, encounter date. *Selection* criteria includes any two of the following fields:  clinic, patient, error code, or clinic stop code.
It is recommended the report be queued as it may be quite lengthy.  When printed, each clinic will print on a separate page.
**Incomplete Encounter Management**
**Incomplete Encounter Reports**
**Incomplete Encounters by Error Code**
The Incomplete Encounters by Error Code option provides a list of the errors which are in the TRANSMITTED OUTPATIENT ENCOUNTER ERROR CODE file (#409.76).  You may sort the report by one or all divisions and one or all error codes.  Errors are sorted by patient name within each error code.
Information provided on the report includes error code and description, patient name, last four of SSN, date and time of the encounter, and clinic.
**Incomplete Encounter Management**
**Incomplete Encounter Reports**
**Summary Report - IEMM**
This report prints a summary showing total encounters for a date range and the number and percentage of incomplete encounters.  The report may be printed as summary only or summary with detail.
The summary only report lists encounters for all clinics and divisions.  For each clinic, the number of encounters, the number of incomplete encounters, and the percentage rate will be provided.
The summary report with detail lists the errors for the selected divisions/clinics in descending order of occurrence.  Shown for each error is the number of occurrences and its percentage of the total number of occurrences.
In addition to the printed version of both types of report, the summary only section is available as a bulletin that can be queued to run as a nightly background job or at user-specified times.  This bulletin will be sent to the user-specified mail group.
**Incomplete Encounter Management**
**Correct Incomplete Encounters**
The Correct Incomplete Encounters option is used to view and correct incomplete encounters.  Anyone may view the View Expanded action of this option.  The Encounter Information action is locked with the SCENI ENCOUNTER EDIT security key while the other actions are locked with the SCENI IEMM EDIT security key.
Initial selection criteria for the incomplete encounters is patient name, clinic, or error code.  Selection by clinic or error code will prompt for a date range.  The date range default is the same value as used in the Appointment Management option; that is, the number of days in the past the software should initially search for appointments.  You may modify your selection criteria via the following “change” actions:  patient, clinic, date range, and error code.  Other actions available from the initial display include Display Errors and Expand Encounter.  The Expand Encounter action may display appointment demographics, appointment event log, patient information, and check out information.  This action will only display for encounters that are appointments.  If the encounter is a standalone add/edit, you will receive a warning that the encounter cannot be expanded.
Following is a brief description of the actions available from the error display screen.**View Expanded** Redisplays each error code with its corrective action**Check Out** Goes through the check out process**Correct Errors** Calls the appropriate option to correct the selected error **or** if 	corrective action is reflagged, will automatically reflag the selected 	error for transmission**Patient Demographics** Prompts through patient demographic information**Load/Edit Patient Data** Calls the Load/Edit Patient Data option functionality**Encounter Information** Allows editing of select fields that are set by the software.
Fields which may be edited through Encounter Information
are appointment type, eligibility of encounter, medical center
division, and clinic stop code.**Retransmit Error** Flags the selected error for retransmission
**Incomplete Encounter Management**
**Correct Incomplete Encounters**
The validator (edit checker mechanism) reviews the encounter immediately after you have completed entries/edits and before exit from the record edit process.  If the data passes validation, the encounter record is flagged for retransmission.If multiple inconsistent encounters exist for a patient which contain the same *demographic* error, that error will be corrected for all the encounters when it is corrected for a single encounter.
**Retransmit Ambulatory Care Data by****Note:** This option has been placed out of order with patch SD*5.3*640 since ACRP transmission has been discontinued.
This option is used to mark outpatient encounters, within a user-specified date range, for retransmission to the National Patient Center Database in Austin.
Since data collection by the NPCDB began , it is best to use this option after that date.
**Retransmit Selected Error Code****Note:** This option has been placed out of order with patch SD*5.3*640 since ACRP transmission has been discontinued.
This option allows re-flagging of encounter activity with a specified error code for transmission to the National Patient Care Database.
To avoid overload, no more than 5000 encounters will be flagged at a time for transmission.  A report is produced which reflects statistics regarding the activity identified/flagged for transmission.  If more than 5000 encounters are identified, text will be included in the report advising to re-run the utility on a subsequent date to flag encounters not included in the initial run.  The printed report is also sent in the form of a mail message to the individual that ran the report.
If there are no encounters found, the following message will appear on the report.
*No errors on file since the most recent database closeout date.*
**Selective Retransmission of NPCDB Rejections****Note:** This option has been placed out of order with patch SD*5.3*640 since ACRP transmission has been discontinued.
This option displays a list of those patients who currently have rejections from the National Patient Care Database on file and are not marked for retransmission.  The list only includes demographic and other non-encounter related errors.
You can then selectively choose which patient encounters should be marked for retransmission.  Entries which are selected will be marked by an asterisk (*) and will be flagged for retransmission when you exit the option.
You may choose to select all patients from the list or individual patients (by patient name or encounter number).  A deselect function is also provided.  You must make a selection before you can utilize the deselect function.  Again, you may deselect individual patients or decide to deselect your entire selection.