---
app_name: Vitals/Measurements (GMRV)
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: null
doc_type: user-manual
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-11'
is_base: false
is_change_pages: true
library_max_patch: null
package_id: GMRV
patch: null
patch_gap: null
section: ''
source_file: vitl_5_p22_um.docx
status: draft
title: vitl 5 p22 um.docx
---

#### June 2008

This distribution contains change pages for Patch GMRV*5.0*22 of the Vitals / Measurements User Manual.

These change pages for Vitals / Measurements Patch 22 should be inserted into the latest version of the Vitals / Measurements User Manual (revised April 2006 for Patch GMRV*5.0*3).

Patch GMRV*5.0*22 pages:

Replace Pages:	With Pages:

Title Page	Title Page

Revision History	Revision History

2-1 to 2-6	2-1 to 2-6

<!-- image -->

**VITALS / MEASUREMENTS USER MANUAL**

**Version 5.0**

**October 2002**

Revised April 2006 for Patch GMRV*5.0*3

Department of Veterans Affairs Health Systems Design &amp; Development

Provider Systems

*This page intentionally left blank for double-side printing.*

## Revision History

| **Date**     |   **Revision** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | **Author**   |
|--------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| January 2002 |            5   | Initial Publication                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | REDACTED     |
| October 2003 |            5.1 | Sections updated for Patch 1 (GMRV*5.0*1): Revision History  Table of Contents Site Files  Entering Vitals Data  Reports                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | REDACTED     |
| April 2006   |            5.3 | Sections updated for Patch 3 (GMRV*5.0*3):  - updated Title Page - updated Revision History - updated Table of Contents, all pages - updated Introduction, page 1-1, 1-2 - removed Implementation and Maintenance chapter - updated Using Vitals Manager, pages 2-2, 2-2, 2-5, 2-6 - removed Package Operation chapter; replaced with new Using Vitals chapter, updated all pages - updated Entering Vitals Data, all pages - updated Reports, all pages - updated Appendix A, all pages - updated Appendix B, page 7-3, 7-4 - added Appendix C – Using Vitals in CPRS v26 - updated Glossary, all pages - updated Index, all pages | REDACTED     |

October 2002	Vitals/Measurements 5.0	i

*Rev. April 2006* User Manual

*This page intentionally left blank for double-side printing.*

ii	Vitals/Measurements 5.0		October 2002 User Manual *Rev. April 2006*

## 1Using Vitals Manager

Vitals Manager allows a site’s administrator (CAC, IRMS) to define the way that vitals appear in the Vitals/Measurements application. This includes activities such as creating and editing templates, associating qualifiers with different vital types, setting normal/abnormal value ranges for each vital type, and printing a list of qualifiers and their associated categories and vital types.

The Vitals Manager module is used to maintain the site files and settings necessary for a site to operate the software, and the Vitals (user) module is used to collect, store and display patient data. **All the options discussed in this chapter are contained in the Vitals Manager module.**

#### This chapter shows you how to:

1. Start the Vitals Manager module
2. Manage Vitals Categories and Qualifiers
3. Print a qualifiers table
4. Edit abnormal values
5. Create/edit a template

**Getting Started with Vitals Manager**

When you double click on the Vitals Manager icon, enter your access and verify codes at the VistA sign-on window, and click on the OK button, the main window will open (Figure 2-1):

<!-- image -->

**Figure 2-1**

<!-- image -->

1 Patch GMRV*5.0*3 April 2006 Removed the original Chapter 2 “Installation and Implementation.” Changed this chapter title from “Site Parameters” to more accurately reflect chapter content.

Using Vitals Manager

### 1Managing Vitals Categories and Qualifiers

Qualifiers describe how patient vital signs and measurements were taken. These qualifiers are categorized by location (e.g., right arm, left leg), position (e.g., lying, sitting, standing), method (e.g., cuff, Doppler, assisted ventilator, etc.), site (e.g., right, left), quality (e.g., actual, estimated), and cuff size (e.g., adult, small adult, pediatric). Synonyms are used as qualifier abbreviations and are appended to the measurement's numeric values on graphic reports.

Categories and qualifiers are nationally defined and cannot be changed locally. Each vital type is linked to one or more categories (with the exception of  Pain and Central Venous Pressure, which are not associated with any qualifier) and each category may be linked to one or more qualifiers. The linkages between categories and vital types are also nationally defined and cannot be changed locally, but the qualifiers within those categories can be changed. (See the National Term Rapid Turnaround web site at [REDACTED](http://vista.med.va.gov/ntrt/) to request a new qualifier.)

To view the categories and qualifiers that are associated with a particular vital type, double-click the Vitals folder to display the full list of vital types, then click on a vital type to view. A list of categories and qualifiers displays on the right side of the Vitals Manager window (Figure 2-2):

<!-- image -->

**Figure 2-2**

To associate a vitals qualifier with a category, select the desired category, then select the appropriate qualifiers for that category. Checkmarks will appear next to the selected qualifiers.

<!-- image -->

1 Patch GMRV*5.0*3 April 2006 Combined “Adding Vitals Qualifiers” and “Associating Vitals Qualifiers with a Category” sections into new “Managing Vitals Categories and Qualifiers” section to reflect new functionality.

Using Vitals Manager

**Category changes are automatically saved.** The qualifiers selected here for a category and vital type will be the only qualifiers available to the user when entering patient data.

### Printing a Qualifiers Table

The Qualifiers Table is a list of all qualifiers for each vital type and its categories, including each qualifier’s synonym. The Package Coordinator may use this list to determine the accuracy and completeness of the qualifier selection. Qualifiers that are not associated with a category and vital type do not appear in this list.

To print the Qualifiers Table go through the main menu bar and select File, Print Qualifiers Table. The following screen appears:

<!-- image -->

**Figure 2-3**

Select an appropriate device in the Device field. Select a date/time to queue this report in the Queue To Run at field. The default date/time is the current server date/time. This report can’t be queued to run for a past date/time. Click the OK button to print the report.

### Editing Abnormal Values

An abnormal value is defined as a value outside the normal range for a vital type. You can define what these high/low values should be so that when a user enters a vital/measurement outside the normal range of values for a vital type, the value will show on the data table as an abnormal value. It will be bold, or a different color dependent upon how it is defined in the User Options option in the Vitals module. User Options is used to define what the text should look like in the data table (bold, different color, etc.) for both normal and abnormal values. Refer to the section on Editing User Options in the Entering Vitals Data chapter in this manual.

To edit abnormally high and low vital type values double click on the Abnormal Values folder to open it, then click on the vital type you wish to edit high/low values for. The following window appears (Figure 2-4):

Using Vitals Manager

<!-- image -->

**Figure 2-4**

You can either move the bar up or down to change the abnormal value or type in the abnormal value. If you type in a value, the meter will not reflect the value until you click in an area outside the box where you entered the value. **Click the Save Abnormal Values button next to the Abnormal Values heading at the top of the window to save the values** .

### Editing System Parameters

There are 3 system parameters in the Vitals Manager module. They are:

#### Allow User Templates Help Menu Web Address Version Compatibility

To edit system parameters double click on the System Parameters folder to open it (Figure 2-5). Below are instructions for editing each of the system parameters.

**Allow User Templates** allows a CAC or package coordinator to decide whether a clinician should be able to create/edit user templates in the Vitals Manager and Vitals modules. When the checkbox is checked, a clinician is able to create/edit user templates in the Vitals Manager and Vitals modules.

**Help Menu Web Address** contains the address for the Vitals Home Page and directs the user’s default browser to this page when accessed.

**Version Compatibility** is used to check if a client version is compatible or not with the current version of Vitals running on the VistA M server. All previously installed versions of

Using Vitals Manager

Vitals/Measurements are listed in this parameter. Only the version(s) that are compatible with the current server version are checked. These versions are identified by their executable name and the Windows file version. Because backward compatibility is required, more than one version of the software may be flagged as compatible.

<!-- image -->

**1** **Figure 2-5**

#### Click the Save System Parameters button next to the System Parameters heading at the top of the window to save the values.

**Special Note** : The VistA server install (KIDS Build) will automatically set the Help Menu Web Address and Version Compatibility parameters for the client/server versions being installed.

After an installation this parameter should be carefully reviewed. Modification of this parameter should not be needed unless the site is testing a patch or performing local modifications to the client software.

<!-- image -->

1 Patch GMRV*5.0*3 April 2006 Updated screen capture.

Using Vitals Manager

### Creating/Editing a Template

Templates are a set of vitals/measurements grouped together to make data entry simpler and easier. Using the Vitals Manager module, templates can be created for the following categories 1 :

**System** – Templates are available to all system users

**Division** – Templates are available to all users within a division (for multi-divisional sites) **Location** – Templates are available to all users within a particular ward , team, or clinic **User** – Templates are available only to the individual user who created the template

#### Note: The Allow User Templates system parameter must be checked and system parameters must be saved in order to see User templates.

All templates are created the same way. The following instructions show how to create/edit a template for a Location.

To create a new template, go through the main menu bar and select Templates, New Template. You can also click on the Create a New Vitals Input Template button on the toolbar to create a new template. The following window appears (Figure 2-6).

<!-- image -->

**Figure 2-6**

In the Type section of the window, select the type of template you want to add by clicking the appropriate radio button. In this case the type selected is Location.

<!-- image -->

**Figure 2-7**

<!-- image -->

1 Patch GMRV*5.0*3 April 2006 Updated the template category descriptions for clarity.