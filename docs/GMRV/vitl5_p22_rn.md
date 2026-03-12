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
source_file: vitl5_p22_rn.docx
status: draft
title: Patch GMRV*5.0*22
---

<!-- image -->

**VITALS / MEASUREMENTS**

**RELEASE NOTES**

# Patch GMRV*5.0*22


# September 2008


Health Systems Design &amp; Development

Provider Systems

## Vitals/Measurements Release Notes

**************************************************************************

This release has been checked for 508 compliance as a component of CPRS. The entire application is scheduled for a compliance review in the future.  Any compliance issues found during the review will be corrected by a patch after the review.

**************************************************************************

This patch fixes some existing problems:

1. Before this patch, if a facility created an input template containing a vital type of Pulse Oximetry with a default qualifier, that Qualifier will not show up on the template. This problem happened in Vitals User and Vitals Lite. After this patch, the default qualifier will appear on the template when accessed by the end users.

1. Before this patch, in Vitals User, if a user selected a patient from the "Ward" list and entered data for that patient, the wrong hospital location was stored in the database. After this patch, the correct hospital location will be stored.

Routines: GMVRPCP

1. Before this patch, when a user entered the patient's height and the unit of measurement was inches, the user had to convert the value from feet and inches into inches. This was the case with Vitals User and Vitals Lite. However, previous versions of CPRS (v25 and earlier) allowed the user to enter the patient's height in feet and inches (e.g., 5'9) and the software calculated the number of inches. After this patch, when entering a patient's height and the unit of measurement is inches, the user will be able to enter inches (e.g., 69) or feet and inches (e.g., 5'9 or 5'9").

1. Before this patch, when creating an input template, you could not select the default unit of measurement for Central Venous Pressure (CVP). After this patch, users will be able to select the unit of measurement. However, both units are metric so the Metric radio button will designate “mmHg” and the  radio button will designate “cmH2O”.

1. Before this patch, if the user clicked the Date/Time button in Vitals Lite or Vitals User and then clicked the "NOW" button, the current date and time were retrieved from the clock on the workstation. If the workstation's clock was incorrect, a wrong date/time was displayed. After this patch, "NOW" will be calculated from the database's clock.

1. Before this patch, if the user did not have the "Show Qualifiers" boxes checked under the "User Options" option of Vitals User, the values in the "L/Min/%" line of the data grid of  Vitals Lite did not appear correctly if you entered Pulse Oximetry with a method qualified by a percentage. It just shows ‘/’.  After this patch, the values in the data grid of Vitals Lite will appear correctly regardless if the "Show Qualifiers" boxes are checked.

1. Several sites have reported that Vitals User and Vitals Lite take too long to start.  When the software starts, it builds lists of choices for the user to select from.  Building the list of all clinics can take thirty or more seconds when the site has thousands of active clinics.  This patch speeds up the building of the clinics list by making a change to the Remote Procedure Call (RPC) - GMV LOCATION SELECT.

After this patch the CLINIC list will be initially populated with the first 500 active clinics. As the user scrolls down the list or types in a clinic name the software will get the next 500 active clinics. This change will also affect the way the scroll bar works when scrolling through the clinic list.  Since the scroll bar uses this RPC to retrieve the clinic records, users will be able to scroll through 500 records at a time.

Routines: GMVRPCHL, GMVGETD

1. In the data grid display of Vitals User and Vitals Lite, there is space to display data from the Intake and Output package. The Application Programming Interface (API) that returns the data provides the total liquid amount of a patient's intake and output for a 24 hour period.  The API returns the date but not the times the values were recorded.  Before this patch, the data grid displayed a time of "00:00:00" as the time. After this patch, the data grid will display a time of "23:59:59.”

1. The "Help" menu for Vitals Lite, Vitals User and Vitals Manager have an option that opens up a web page meant to help the user find out more information about the Vitals/Measurements software. The web address for this page was set to REDACTED when version 5 was released.

Sites also have the ability to change the address used in the HELP menu by updating it in the Vitals Manager GUI. However, when sites did choose to change the default web address, it was ignored and the standard default address was used.

This patch will change the default address to REDACTED and if sites choose to change the HELP web address to something other than the default, it will be recognized.

Routines: GMV22PST

1. Before this patch, the "Print Qualifiers Table" report in Vitals Manager GUI errors out if the user selects a printer that does not allow queuing. The option should not allow the user to select printers that do not allow queuing of the output. After this patch, Vitals Manager will present only printers that allow queuing.

1. Before this patch, "Standing" can be selected as a qualifier when entering a weight value for a patient. "Standing" should not be a qualifier choice when entering a weight value. After this patch, "STANDING" will not be a choice when entering a patient's weight. This patch checks all input templates, too. If "STANDING" is defined as a default qualifier in an input template, it is removed.

Routines: GMV22PST

1. Before this patch, when editing qualifiers in the "Edit User Templates" option of Vitals User, an access violation and list out of bounds error can occur. To create the problem, select a vital type that has qualifiers, make some changes, save the changes, change the qualifiers without re-selecting the vital type and save the change. This generates an access violation and/or list out of bounds error. After this patch, the error will not occur.

1. Before this patch, when there are too many qualifiers in a data grid cell, you cannot always see the rightmost text in the cell and the cell cannot be expanded. After this patch, when the mouse pointer hovers over the cell, the full value of the cell will appear in the lower left hand side of the status bar. When the user clicks the cell, the full value of the cell will appear in a hover hint for several seconds.

1. Before this patch, when a user selected a "SENSITIVE" patient in Vitals User, the software did not correctly call the Registration package utility to notify it that a sensitive patient record was being accessed.  After this patch, Vitals User will correctly notify the Registration package.

Routines: GMVRPCP

1. Before this patch, when a user entered a blood pressure value that contained spaces, Vitals User and Vitals Lite saved the value with the spaces. After this patch, the spaces will not be saved.

1. Before this patch, when a method for Pulse Ox was selected and no value was entered for either O2 Concentration % or Flow Rate, the method/qualifier was not displayed.  Now if any method/qualifier is selected, it is displayed regardless of the values entered in O2 Concentration and Flow Rate.

1. If a sensitive record is selected in Vitals User, the user must acknowledge the sensitive data window before the record will open and SSN, etc., become available.  However, if multiple patients are selected for data input in Vitals and the first is a sensitive record, it opens in the background and SSN, DOB, etc., can be seen while the sensitive data window is being reviewed.  This could be considered a privacy violation and has caused concern among nursing staff. After this patch, the sensitive data will not display until the user confirms the patient selection.