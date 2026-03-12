---
app_name: Vitals/Measurements (GMRV)
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
package_id: GMRV
patch: null
patch_gap: null
section: ''
source_file: vitl5_p23_rn.docx
status: draft
title: GMRV*5.0*23
---

<!-- image -->

**VITALS / MEASUREMENTS**

**RELEASE NOTES**

# GMRV*5.0*23


# September 2009


Office of Enterprise Development

## Vitals/Measurements Release Notes

**************************************************************************

This software release is Section 508 compliant.

**************************************************************************

1) This patch modifies the existing Vitals package routines so they use the "PXRMINDX(120.5" index to find patient vital sign records. Before this patch, these routines used the AA cross-reference in the GMRV VITAL MEASUREMENT file (#120.5). This new approach is being used because a new software package called Clinical Observations will also collect patient vitals data, but will store data in a different file. The Clinical Observations (CliO) package will update the "PXRMINDX(120.5" index just as the Vitals package currently does. The "PXRMINDX(120.5" index belongs to the Clinical Reminders package and is used to resolve reminders related to patient vital signs. These routine changes will allow the Vitals package to retrieve patient vital signs data from both the GMRV VITAL MEASUREMENT (#120.5) and the Clinical Observations package. The programming calls will continue to function as before with the same input parameters and output with two exceptions. The GMV LATEST VM and GMV V/M ALLDATA Remote Procedure Calls (RPCs) will return an extra piece of data that identifies the package where the record is stored (e.g., Vitals or CliO). These RPCs are used by the Vitals Graphical User Interface (GUI).

applications and locally developed routines that use these existing Application Program Interfaces (APIs) should not see any change with invoking the APIs or the format of the results.

VistA applications that use the AA cross-reference or get data directly from the Vitals package globals will modify their existing code to use the "PXRMINDX(120.5" index and the APIs provided in this patch.

Facilities that do local development with direct global reads of the AA cross-reference are encouraged to change their code to use the "PXRMINDX(120.5" index and one of the existing APIs (e.g., GMRVUTL or GMVPXRM) to get the record data.

Several new APIs are added to the GMVUTL routine to retrieve patient records.

Three new routines (GMVGETVT, GMVGETQL and GMVGETC) are added to retrieve information about vital types (GMRV VITAL TYPE file #120.51), qualifiers (GMRV VITAL QUALIFIER file #120.52) and categories (GMRV VITAL CATEGORY file #120.53).

The Remote Procedure Calls—and corresponding Integration Control Registrations (ICR) #, if any—use the modified routines:

GMV CUMULATIVE REPORT

GMV PT GRAPH

GMV LATEST VM (4358)

GMV V/M ALLDATA (4654)

GMV EXTRACT REC (4416)

GMV LATEST VITALS FOR PATIENT

GMV LATEST VITALS BY LOCATION

GMV ENTERED IN ERROR-PATIENT

Application Programming Interfaces (and corresponding ICR #, if any) use the modified routines:

EN^GMVPXRM (3647)

VITALS^GMVPXRM (3647)

EN6^GMRVUTL (1120)

EN1^GMRVUT0 (1446)

EN1^GMVHS (4791)

EN3^GMRVSC0 (1444)

EN1^GMVDCEXT (4251)

EN1^GMVDCSAV (3996)

CALBMI^GMRVBMI

CALBMI^GMVBMI

GMVUTL (5046) new

GMVGETVT (5047) new

GMVGETQL (5048) new

GMVGETC (5050) new

The GMRVUT0 and GMVHS Application Programming Interfaces (APIs) each return an array. Before this patch the right most subscript in each array was the internal entry number of the record in GMRV VITAL MEASUREMENT file (#120.5). Once a facility starts to use the Clinical Observations package, a record in the array may come from the new OBS file (#704.117) instead of the GMRV VITAL MEASUREMENT file (#120.5). If the record comes from the OBS file (# 704.117) this subscript will be a phony number. It will not be the internal entry number of the record because the OBS file (#704.117) uses a Global Unique ID (GUID) which is a string of unique characters to identify its records instead of a purely canonic number. Assigning a phony canonic number to the subscript allows the existing applications that call these APIs to continue to $ORDER through the array. The existing applications that have permission to use these APIs do not use this subscript to actually look up the record in the GMRV VITAL MEASUREMENT file (#120.5) so the change should not cause a problem.

2) The following five options under the Reports menu of the Vitals User interface will no longer be available:

Vital Signs Record

B/P Plotting Chart

Weight Chart

POx/Respiration Chart

Pain Chart

Similar graphic reports can be printed by right-clicking in the data grid display and selecting the Print Graph option or using the Print Graph option under the File menu.

3) This patch fixes some existing problems:

a) Remedy ticket 116911

Under certain conditions the GMRVUT0 API (ICR #1446) returned an abnormal flag for a Pain score. The software does not currently recognize a normal range for Pain scores, so there never should be an abnormal flag for any patient pain score.

b) Remedy ticket 174395

The GMRVUT0 API (ICR #1446) did not return Blood Pressure and Pulse readings when the value was not numeric (e.g., Refused). This API now returns records where the reading is non-numeric.

c) Remedy ticket 277170

Prior to GMRV*5*22 the Vitals.exe and GMV\_VitalsViewEnter.dll had a bug

that used the date/time from the workstation clock as the default for when

the observation was made. The default date/time should be taken from the

server clock. The GMRV*5*22 patch fixed the problem in the Vitals.exe

only. This patch will fix the problem in the GMV\_VitalsViewEnter.dll file.

d) Remedy ticket 277330

The package does not export any archive/purge functionality. However, Section 6 of the Technical Manual provides instructions for using FileMan functionality to do so. Archiving/purging vitals records is discouraged. Therefore, these instructions will be removed from the Technical Manual.

4) E3R 19259 - CASMED Interface Changes

A "Read Monitor" button is added to the "Enter Vitals" screen. When this

button is invoked, the software will attempt to retrieve vital sign

readings from a vital sign monitor (VSM) connected to the workstation.

The vital sign readings that appear on the VSM screen will be sent to the

"Enter Vitals" screen and pasted into the input template. This saves the

user from having to type in the values.

There are two types of interfaces between the "Read Monitor" button and

the vital signs monitor: 1) direct link to a CASMED VSM and 2) a Dynamic

Link Library (DLL) link to all other VSMs.

When the Vitals software starts up, the VSM connected to the workstation

should be turned on. The Vitals software checks all of the DLLs in the

"Program Files\VistA\Vitals\Plugins" directory to determine if any of the

DLLs respond to the VSM. The first DLL that confirms it can "talk" to the

VSM is recognized. If none of the DLLs respond, the VSM is considered to

be a CASMED VSM and that interface is used.

Vendor supplied DLLs should be placed in the "Program

Files\VistA\Vitals\Plugins" directory of the workstation where the VSM

will be connected. If this directory does not exist, it should be created.

Other files supplied by a VSM vendor should be placed in the "Program

Files\vendor name\" directory (e.g., "Program Files\ACME Medical Co\".

5) 508 COMPLIANCE

Section 508 testing was conducted on the software by two test engineers from the VA Section 508 Program Office.  The software was modified to meet their recommendations and re-tested. The software is now 508 compliant.  Many of the changes are not noticeable since they involve use of screen reading software.  One new report, Graph Report, was added.  It summarizes in text format the values on the graph display.

6) Patient Safety Issue (PSPO 1258)

Remedy ticket 301139 was entered and elevated to a Patient Safety Issue (PSPO 1258).  The wrong weight was entered for a patient, but was later changed to “Entered in Error.”  In the meantime, a medication was given to the patient based on the wrong weight.  No harm came to the patient, but there was a period of seven days before it was discovered that the dosage was incorrect.  To prevent similar occurrences, the software will do an additional check on any new weight and height values entered. If the new weight value differs by 20% or more from previous values, a warning message displays. If the new height value differs by 10% or more from previous values, a warning message displays.