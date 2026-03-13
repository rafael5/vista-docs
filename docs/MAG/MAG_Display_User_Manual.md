---
app_name: VistA Imaging System (MAG)
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: null
doc_type: user-manual
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-12'
is_base: false
is_change_pages: false
library_max_patch: null
package_id: MAG
patch: null
patch_gap: null
section: ''
source_file: MAG_Display_User_Manual.docx
status: draft
title: VistA Imaging
---

<!-- image -->

# VistA Imaging

**Clinical Display User Manual**

**July 2024 – Revision 15**

Department of Veterans Affairs Office of Enterprise Development Health Provider Systems

**Clinical Display Workstation User Manual July 2024**

Property of the US Government

This is a controlled document. No changes to this document may be made without the express written consent of the VistA Imaging development office.

While every effort has been made to assure the accuracy of the information provided, this document may include technical inaccuracies and/or typographical errors. Changes are periodically made to the information herein and incorporated into new editions of this document.

Product names mentioned in this document may be trademarks or registered trademarks of their respective companies, and are hereby acknowledged.

VistA Imaging Office of Enterprise Development Department of Veterans Affairs

Internet: [REDACTED](https://vaww.edis2.med.va.gov/main)

SharePoint: [REDACTED](https://vaww.edis2.med.va.gov/main)

### Revision History

| **Date**   |   **Rev** | **Notes**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| July 2024  |        15 | Made following edits to support MAG*3.0*334.  1. Changed Options and System Manager menus with newly added screenshots. The diagram is on Figure 1: Menu Bar in the VistA Imaging Display Main Window. 2. Changed Table 1 on the VistA Imaging main menu, added new Item: Set Workstation’s Alternate Video Viewer. 3. Deleted Set Station Alternate Video Viewer from Appendix E: For System Managers. 4. Deleted Set Station Alternate Video Viewer from Table 2 in the Appendix E for System Managers. 5. Changed Table 2 to add a statement for default timeout value of ‘6’(six) minutes. |
| Sept 2018  |        14 | Changes for MAG*3.0*216 to remove help menu items that do not work under Windows 10. REDACTED                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| April 2018 |        13 | Changes in support of MAG*3.0*188. REDACTED                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Nov2017    |        12 | Changes in support of MAG*3.0*188 and MAG*3.0*191 to the MUSE EKG Viewer section and the Processing ROI Requests section. REDACTED , REDACTED ,  REDACTED                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| June 2017  |        11 | Added instructions for 2FA PIV/PIN that replace the previous access/verify login process. (Signing in to Clinical Display) REDACTED , REDACTED                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Jan2017    |        10 | Added the Copy Image (before Delete) for ReIndex in Clinical Capture menu option and description in the Image Delete Window section in Appendix C. REDACTED , REDACTED                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Aug 2016   |         9 | Changes were made to the MUSE EKG section and a new section, Annotating Images Captured with Clinical Capture Client, was added. The Main  Window Help Menu Graphic was changed, due to the new link to display the user guide and in Appendix E, the menu for system managers has changed. The option to Open Image by Image ID is new.  REDACTED , REDACTED                                                                                                                                                                                                                                  |
| Mar 2015   |         8 | Made edits to pages 18, 25, 55, 65, 145 and 146 due to a menu wording change for Patch 149. Also, fixed two typos found on pages 37, 57 and in the Index.  Several pictures needed to be replaced (as they were absent) and their alt-text was added. Table of contents was reformatted. REDACTED , REDACTED                                                                                                                                                                                                                                                                                   |
| Aug2013    |         7 | Implemented comments from REDACTED . REDACTED                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Aug 2013   |         6 | Updated for Patch 131 New sections: Scout Menu, Using Scout Lines and XML Documents  REDACTED , REDACTED .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Mar 2013   |         5 | Updated for Patch 130. Multiple minor edits for consistency and to enhance usability. Screenshots updated throughout the document to include the new Color Channel and MUSE EKG buttons. Updated content of all relevant sections: VistA Imaging Display Main Window, Toolbars in the Full Resolution Viewer,  New sections: Viewing the Different Color Channels of an Image and Processing ROI Requests.  REDACTED  REDACTED .                                                                                                                                                               |
| Dec 2012   |         4 | Updated for Patch 122,  *Annotations*  . See the change pages for details about the changes, which are too numerous to list. REDACTED  REDACTED , REDACTED .                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Jan 2012   |         3 | Updated for Patch 121: Added section  *Watermarked Images for Rescinded Advance Directives*  . REDACTED  H. Suri. REDACTED .                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| July 2011  |         2 | Revision for Patch 117. REDACTED                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Aug 2010   |         1 | Initial draft. Eddie Null. REDACTED                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

**Contents**

**Introduction	1**

Terms of Use	1

Conventions	2

Acronyms	2

Related Information	3

Getting Help	3

**Getting Started	5**

Using Clinical Display	5

Signing in to Clinical Display	5

VistA Imaging Display Main Window	8

Menu Bar in the VistA Imaging Display Main Window	9

**File Menu	9**

**Context Menu	9**

**Options Menu	10**

**View Menu	11**

**Utilities Menu	11**

**Reports Menu	12**

**System Manager Menu	12**

**Help Menu	12**

Toolbar in the VistA Imaging Display Main Window	12

Fields	13

Show Message History Window Button	13

Selecting a Patient	13

Using the Patient Lookup Box	14

Using the Menu Bar or Toolbar	15

Using the Image List Toolbar	16

**Working with the Image List Window	17**

Image List Window	17

Menu Bar in the Image List	18

**File Menu	18**

**Context Menu	18**

**Options Menu	18**

**View Menu	19**

**Reports Menu	20**

**Filters Menu	20**

**Layouts Menu	21**

**Utilities Menu	24**

**Manager Menu	25**

**Help Menu	25**

Toolbar in the Image List Window	27

Filter Buttons	28

Icons in the Item Column	28

Display of the Column Listings	29

Popup Menu in the Image List Window	30

Image Information Window	31

Working with Filters in the Image List Window	31

Applying the Filters in the Image List	31

Image Filters Add/Edit Window	32

**File Menu	32**

**Edit Menu	32**

**Options Menu	32**

**Help Menu	33**

Creating Private Filters	33

Editing or Deleting a Private Filter or Filter Details	37

Viewing Deleted Image Placeholders	38

Viewing Patient Clinical Records in VistA	38

Viewing Radiology Exams	39

Viewing Progress Notes, Clinical Procedures and Consults	40

Viewing Controlled Images in the Image List Window	41

**Working with Abstracts	43**

Abstracts Window	43

Image Group Abstracts Window	43

Image Information Window	44

Toolbar in the Abstracts Window	45

Popup Menu in the Abstracts Window	46

Viewing Abstracts	47

Viewing Image Information	48

Synchronizing Image Data in Related Windows	48

Viewable and Non-Viewable Images	49

Images That Are Not Viewable Due to an Error	49

Blocked Images in the Abstracts Window	49

Controlled Images in the Abstracts Window	51

File Types Viewable in Clinical Display	51

File Types Viewable Using an Alternate Viewer	52

Watermarked Images for Rescinded Advance Directives	53

Description of the Viewers	54

Full Resolution Viewer	54

**File Menu	55**

**Image Menu	56**

**View Menu	57**

**Layout Menu	58**

**Page Menu	58**

**Help Menu	58**

Radiology Viewer	63

**File Menu	65**

**Image Menu	65**

**View Menu	67**

**Rotate Menu	67**

**CT Presets Menu	68**

**View Info Menu	68**

**FullRes Menu	68**

**View Settings Menu	69**

**Options Menu	69**

**Tools Menu	70**

**Scout Menu	71**

**Help Menu	71**

Video Player	76

**File Menu	77**

**Options Menu	77**

**View Menu	77**

**Actions Menu	77**

**Help Menu	78**

MUSE EKG	79

**File Menu	81**

**MUSE Test Type and Format ID Mapping	83**

Format Table Defaults	84

Override a Default Format ID	86

Verify the new Format ID.	87

Add a New Test Type	88

MUSE Debug	88

**Image Menu	89**

**XML Documents	94**

**Using Scout Lines	95**

Overview of Scout Images and Scout Lines	95

Displaying Scout Images and Scout Lines	96

Menu Bar in the Scout Window	97

**File Menu	97**

**Image Menu	97**

**View Menu	98**

**Rotate Menu	99**

**CT Presets Menu	99**

**ViewInfo Menu	99**

**Options Menu	100**

**Scout Menu	100**

Working With Scout Images	100

Specifying the Color of the Scout Line	103

Hiding Scout Lines and Turning off Automatic Detection of Scout Images	104

**Viewing the Different Color Channels of an Image	105**

The Color Channel Button	105

The Color Channel Option on the Image Menu	106

Using the Color Channel Separator to Compare Images in Dual Stack View	107

**Working With Annotations	108**

Overview	108

Annotation Permissions	114

Annotating Images at Remote Sites	114

Activating the Annotation Mode	114

Annotation Tool Buttons	115

Creating Annotations	117

Drawing Lines	117

Drawing Freehand Drawings	118

Drawing Rectangles	118

Adding Text to Images	118

Drawing Ellipses	119

Drawing Arrows	119

Highlighting Areas	120

Using the Ruler	120

Measuring Angles in Images	121

Modifying Annotations	122

Selecting Annotations	122

Moving Annotations	123

Resizing Annotations	123

Deleting Annotations	123

Changing Selected Annotation Attributes	124

Setting Color Properties	124

Setting Line/Arrow Properties	125

Setting Freehand Properties	126

Setting Rectangle/Highlighter Properties	127

Setting Text Properties	128

Setting Ellipse Properties	129

Setting Ruler Properties	130

Setting Protractor Properties	132

Setting Global Annotation Attributes	134

Setting Global Annotation Font Attributes	134

Setting Global Annotation Line Width Attributes	135

Setting Global Annotation Color Attributes	136

Setting Global Annotation Opacity Attributes	136

Setting Global Annotation Arrow Attributes	137

Hiding and Showing Annotations	137

Hiding Annotations	138

Showing Annotations	140

Viewing Audit History	143

Viewing Annotation Information	145

Annotating images captured with Clinical Capture Client.	145

Annotating RAD Package Images and DoD Radiology Images	149

Exiting Annotation Mode and Saving Annotations	149

Guidelines	150

Printing a Single Image	151

Image Print Options Window	152

Release of Information handle Release requests	153

How Clinical Display handles Release of Information requests	153

Printing Multiple Images	156

Printing All Images of a Patient	159

Processing ROI Requests	160

Monitoring the Status of Release of Information Jobs	164

Printing Images with Annotations	165

Printing Images with Annotations Using the Release of Information Feature	166

Copying an Image	166

**Configuring User Preferences for the Image List and Abstracts	167**

Configuring the Display of Windows for Patient Selection	167

Configuring the Abstract and Image Viewers	168

Configuring Remote Image Views	169

Configuring Alternate Viewer Options	170

Configuring the Layout Style of the Image List	171

Configuring User Preferences for Annotation Options	172

**Viewing Patient Images at Remote Sites	174**

Using Remote Image Views (RIVs)	174

Partial Results	175

Configuring User Preferences for RIVs	176

Configuring Your Connection to Remote Sites	177

**Editing the Image Index Entries	179**

Image Index Edit Window	179

Menu Bar in the Image Index Edit Window	179

**File Menu	179**

**Options Menu	180**

**Help Menu	180**

Editing Index Fields	180

**Checking Quality Assurance on Images	183**

QA Review Window	183

Menu Bar in the QA Review Window	184

**File Menu	184**

Applying Advanced Filters to the QA Review	187

Selecting an Existing Filter for the QA Review Queries	189

Specifying the QA Review Parameters	189

Performing the QA Review	192

Performing QA Review on a Single Image within a Group	193

Images with Incorrect Index Values	193

Running the QA Review Report	194

**File Menu	197**

**Options Menu	197**

**Help Menu	197**

**Displaying Reports	198**

Report Window	198

Menu Bar in the Report Window	198

**File Menu	198**

**Help Menu	199**

Image Report	199

Patient Profile	200

Health Summary	200

Discharge Summary	201

**Appendix A: Shortcut Key Legend	203**

Full Resolution Viewer and Radiology Viewer	203

Image Viewer	203

Image List Window	203

Radiology Viewer	204

Cine Viewer	204

Abstract Windows	204

Page Functions	204

Activate Windows	205

Focus in Any Window	205

Help Topics	205

Menu Option Access	205

Closing Dialog Boxes	205

Popup Menu Shortcuts	205

**Appendix B: Clinical Display Security Keys	206**

**Appendix C: Deleting Images	209**

When an Image Is Deleted	209

Image Delete Window	210

Menu Bar in the Image Delete Window	210

**File Menu	210**

**Options Menu	210**

**Help Menu	211**

Toolbar in the Image Delete Window	211

Deleting Single Images	212

Deleting Image Groups	212

Deleting Images with Questionable Integrity (QI Issues)	213

Deleting Images With Annotations	214

Deleting A Single Image With Annotations	214

Deleting an Image Group With Annotations	215

**Appendix D: Clinical Context Object Workgroup	217**

CCOW Overview	217

Patient Context in Clinical Display	217

**Appendix E: For System Managers	219**

System Manager Menu Options	219

Message History Window	220

Viewing Messages	220

Image Information Advanced	221

Image Information/Properties Window	221

Toolbar in the Image Information/Properties Window	222

**Index	223**

## Introduction

<!-- image -->

This manual explains how to use the Clinical Display software. Clinical Display is a part of the Veterans Health Information System and Technology Architecture (VistA) Imaging System.

Clinical and administrative staff responsible for providing patient care and maintaining patient’s

electronic medical records should use this manual.

This manual introduces you to the Clinical Display application and explains how to navigate and complete the following tasks:

- Signing in to Clinical Display
- Selecting a Patient
- *Working with the Image List*
- *Working with Abstracts*
- *Viewing Patient Images at Remote Sites*
- *Printing Images,*
- *Configuring User Preferences for the Image List and Abstracts*
- *Displaying Reports*
- *Working With Annotations*
- *Using Scout Lines*

Supporting information is provided in the following appendixes:

- *Appendix A: Shortcut Key Legend* to navigate in the interface
- *Appendix B: Clinical Display Security Keys* list for restricted tasks
- *Appendix C: Deleting Images* to delete single images and group images
- *Appendix D: Clinical Context Object Workgroup* on CCOW compliance
- *Appendix E: For System Managers* for access to all functionality in Clinical Display

### Terms of Use

In compliance with Food and Drug Administration (FDA) and VA policies, authorization to use this software is contingent on the execution of a Site Agreement between the VistA Imaging Product Development group and the site where this software is installed.

In addition to any restrictions noted in the Site Agreement, the following restrictions apply.

| <!-- image -->   | Caution: Federal law restricts this device to use by or on the order of either a licensed practitioner or persons lawfully engaged in the manufacture or distribution of the product.                                                                                                           |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <!-- image -->   | The FDA classifies VistA Imaging as a medical device. Unauthorized Modifications to VistA Imaging, including the Clinical Display software, will adulterate the medical device. The use of an adulterated medical device violates US federal law (21CFR820).                                    |
| <!-- image -->   | Clinical Display is not intended for the primary interpretation of radiology exams or EKG waveforms. When Clinical Display is installed on approved and properly maintained hardware, primary interpretation of other image types is permissible by licensed practitioners at their discretion. |

### Conventions

This manual uses the following conventions:

- Controls, options, and button names are shown in **Bold** .
- A vertical bar is used to separate menu choices. For example: “ **Select File | Open** ” means: “Click the **File** menu, and then select the **Open** option.”
- Keyboard key names are shown in bold and in brackets.
- When this document is used online, hyperlinks are indicated by blue text.
- Useful or supplementary information is shown in a Tip.
- Important or required information is shown in a Note.
<!-- image -->
- Critical information is indicated by:

### Acronyms

| **Acronym**   | **Definition**                                                             |
|---------------|----------------------------------------------------------------------------|
| **CCOW**      | Clinical Context Object Workgroup                                          |
| **CPRS**      | Computerized Patient Record System                                         |
| **DICOM**     | Digital Imaging and Communications in Medicine                             |
| **DoD**       | Department of Defense (DoD)                                                |
| **EKG**       | Electrocardiogram                                                          |
| **FAQ**       | Frequently Asked Questions                                                 |
| **FDA**       | Food and Drug Administration                                               |
| **HIMS ROI**  | Health Information Management Services Release of Information (department) |
| **HRN**       | Health Record Number                                                       |

| **Acronym**   | **Definition**                                                 |
|---------------|----------------------------------------------------------------|
| **IHS**       | Indian Health Service                                          |
| **ID**        | Identifier or Identification                                   |
| **IRM**       | Information Resources Management                               |
| **OED**       | Office of Enterprise Development                               |
| **QA**        | Quality Assurance                                              |
| **QI**        | Questionable Integrity                                         |
| **RIV**       | Remote Image Views                                             |
| **ROI**       | Release of Information                                         |
| **SSN**       | Social Security Number                                         |
| **TGA**       | Targa Image                                                    |
| **TIU**       | Text Integration Utility                                       |
| **US**        | United States                                                  |
| **VA**        | Veteran Affairs                                                |
| **VHA**       | Veteran Health Administration                                  |
| **VistA**     | Veterans Health Information System and Technology Architecture |

**Related Information**

For additional information about VistA Imaging Clinical Display, see the following documents:

- [Imaging System User Manual](https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/mag_display_user_manual.pdf)
- [Imaging System Technical Manual](https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/IMGtechman_f.pdf)
- [Imaging System Installation Guide](https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/IMGinstallgd_f.pdf)
- [HIM FAQ Page](https://vaww.vha.vaco.portal.va.gov/sites/HDI/HIM/vaco_HIM/SitePages/Home.aspx)

### Getting Help

REDACTED

## Getting Started

<!-- image -->

This chapter provides how-to instructions for the following operations:

- *Using Clinical Display*
- *Signing in to Clinical Display*
- Navigating the *VistA Imaging Display Main Window*
- *Selecting a Patient*

### Using Clinical Display

At most sites, Clinical Display is started from the CPRS tools menu. Clinical Display behaves the same way regardless of whether the application is started from CPRS or from the desktop.

### Signing in to Clinical Display

When you start the application from CPRS, you are automatically signed in. The patient that is selected in CPRS is the same as the patient selected in Clinical Display when the application is opened. This method of matching the same patient between two applications is performed by Clinical Context Object Workgroup (CCOW), a standard for synchronizing common data. See *Appendix D: Clinical Context Object Workgroup* for information on CCOW and patient context in Clinical Display.

For more information on using Clinical Display in the context of CPRS, see the *CPRS User Guide* at [http://www.va.gov/vdl/documents/Clinical/Comp\_Patient\_Recrd\_Sys\_(CPRS)/cprsguium.pdf](http://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/cprsguium.pdf)

1. Double-click the Display Shortcut on the Windows desktop, or click **Start | All Programs** | **VistA Imaging Programs | VistA Imaging Clinical Display 32-bit.**
<!-- image -->
2. Make sure you have a valid PIV card attached to the computer. You will be prompted to select a certificate: Then click on the OK button.

<!-- image -->

1. Next, you will be prompted to enter your PIN. Enter your PIN and click on the OK button.
<!-- image -->

Upon successful authentication and login, the user will be allowed to continue to the application. When an attempt to log in with PIV/PIN fails to authenticate 2FA, the application will revert the user to the Access/Verify screen. If the VistA Sign-on box displays, type your access and verify codes in the **Access Code** and **Verify Code** boxes, then click **OK** .

<!-- image -->

1. If the Select Division dialog box is displayed, select your division and click **OK** .
<!-- image -->

The VistA Imaging Display main window opens. Continue to the next section.

<!-- image -->

### VistA Imaging Display Main Window

You can perform the following tasks from the VistA Imaging Display main window:

- Select a patient
- Set user preferences
- Show or suspend patient context
- Create and use image filters
- Configure remote image view configuration (if available)
- View reports
- Use additional features if you have the appropriate security keys

**Note** : The Utilities and System Manager menus on the menu bar may not be available to you if your site coordinator has not assigned you access to these tools.

Figure 1: Menu Bar in the VistA Imaging Display Main Window

<!-- image -->

**Note** : The Clinical Display software is user configurable. Its appearance may not match the examples shown in this manual. Details on how to configure your system by setting user preferences are explained later in this manual.

**Menu Bar in the VistA Imaging Display Main Window**

File Menu

| **Menu Option**   | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select Patient    | Opens the Patient Lookup window.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Login             | When selecting Login you will be prompted for your PIV PIN code. Follow the Signing into Clinical Display procedures in this manual.  If you are already logged into VistA you will receive a Confirm message for logging out. See Logout below.                                                                                                                                                                                                                                            |
| Logout            | Confirms your logout from the VistA database.  <!-- image -->  **Note**  : If you are not logged in, the following message confirms this.  <!-- image -->                                                                                                                                                                                                                                                                                                                                   |
| Remote Login      | If you are not already logged into VistA the Connect To dialog box is displayed. Follow the Signing into Clinical Display procedures in this manual starting at Step 3.  If you are already logged into VistA you will receive a Confirm message for logging out. See Logout above.  <!-- image -->  After confirming that you want to log out the dialog box closes and the Connect To box opens. Continue the Signing into Clinical Display procedures in this manual starting at Step 3. |
| Exit              | Ends your session in Clinical Display.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

Context Menu

| **Menu Option**   | **Description**   |
|-------------------|-------------------|
| Show Context      |                   |

| **Menu Option**    | **Description**                                                                                   |
|--------------------|---------------------------------------------------------------------------------------------------|
| Suspend Context    | See Appendix D: Clinical Context Object Workgroup for the details of CCOW and these menu options. |
| Resume Get Context | See Appendix D: Clinical Context Object Workgroup for the details of CCOW and these menu options. |
| Resume Set Context | See Appendix D: Clinical Context Object Workgroup for the details of CCOW and these menu options. |

Options Menu

Table 1:Options Menu

| **Menu Option**                          | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Image List Filters                       | Displays the Image Filter Add/Edit window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| User Preferences                         | Displays the User Preferences window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Set Workstation’s Alternate Video Viewer | Opens the Windows Open File dialog box to select a video file viewer to use for all video files. VistA Imaging displays video files in the VistA Imaging Video Display window by default.  For an alternate video viewer to be used for video files, the 'Use Alternate Video Player' radio button must be selected in the Video File Options window.  If ‘Use Alternate Video Player' is selected, all video files will be opened in the video file viewer that is associated with files defined through the operation system. |
| Remote Image Views Configuration         | Opens the Remote Image Views Configuration window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Refresh Patient Images                   | Refreshes the Image List and all Abstracts windows that are open when the refresh was initiated.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Pre Fetch Patient Images                 | All images for the patient are queued to be copied from the Jukebox to the Magnetic Image server for faster loading of images. User must have a MAG PREFETCH Security Key.                                                                                                                                                                                                                                                                                                                                                      |
| Save Settings Now                        | Equivalent to the Windows Save button to explicitly save settings as you go along.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Save Settings On Exit                    | On or off option:  - When selected the settings are saved on exiting Clinical Display. - When not selected, all changes to settings are lost on exiting if you do not manually save the changes.                                                                                                                                                                                                                                                                                                                                |
| Show Hints                               | Show Hints has the following options:  - Main Imaging Display Window - When selected a check mark appears and hints are displayed. - Turn Hints OFF for all windows - When selected a check mark appears and hints are not shown. - Turn Hints ON for all windows - When selected a check mark appears and hints are displayed.                                                                                                                                                                                                 |
| CPRS Link Options                        | Allows user to break the Link to CPRS. It is only enabled if VistA Imaging was started from the CPRS Tools menu.                                                                                                                                                                                                                                                                                                                                                                                                                |
| ShortCut Key Legend                      | Opens the Short Cut Key Legend which is shown in the System References section of this manual.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Message Log                              | Opens the Imaging Session Message History window. (available as a button on the Toolbar)                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Disable Automatic Color Channel          | By disabling the automatic separation, color images will load and display faster. When disabled, the user can choose to show color channels on an image by image basis.                                                                                                                                                                                                                                                                                                                                                         |

View Menu

| **Menu Option**     | **Description**                                                                          |
|---------------------|------------------------------------------------------------------------------------------|
| Image List          | Opens the Image List window.                                                             |
| Abstracts           | Opens the Abstracts window. (available as a button on the Toolbar)                       |
| MUSE EKG Window     | Opens the MUSE EKG viewer.                                                               |
| Group Window        | Enabled if a Group Abstracts window is open. It is used to bring the window into focus.  |
| Radiology Exams     | Opens the Radiology Exam listing window.                                                 |
| Progress Notes      | Opens the Progress Notes window.                                                         |
| Clinical Procedures | Opens the Clinical Procedures window.                                                    |
| Consults            | Opens the Consults window. The link to Consults is not available.                        |
| Toolbar -Main       | Toggles between displaying the Main Toolbar or not.                                      |
| Active Windows      | <!-- image -->  Selecting an entry in the list enables transfer of focus to that window. |

Utilities Menu

(The menu options are displayed only if you have certain security keys. See *Appendix B: Clinical Display Security Keys* .)

| **Menu Option**   | **Description**                                                           |
|-------------------|---------------------------------------------------------------------------|
| QA Review         | Opens the QA Review utility. See  *Checking Quality Assurance on Images.* |
| QA Review Report  | Opens the QA Review Report utility. See  *Running the QA Review Report.*  |

Reports Menu

| **Menu Option**   | **Description**                                                                                 |
|-------------------|-------------------------------------------------------------------------------------------------|
| Patient Profile   | Displays the Patient Profile report window.                                                     |
| Health Summary    | Displays the Health Summary Reports window.                                                     |
| Discharge Summary | Displays the Discharge Summary List window. When you select a summary, the report is displayed. |

System Manager Menu

**Note** : This menu is enabled only if you hold the MAG SYSTEM security key. See *Appendix E:* For System Managers for the menu options.

Help Menu

| **Menu Option**                  | **Description**                                                                                                                                                                                                                                                                |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VistA Imaging Display User Guide | This is a link to the current Display User Guide on the VistA Imaging SharePoint site. When selected, the User Guide will be opened in your browser.  For I.H.S. sites, the link can be changed in the IMAGING SITE PARAMETERS File (#2006.1), in the DISPLAY HELP URL  field. |
| Contents                         | Displays a welcome to the VA VistA Imaging Help System.                                                                                                                                                                                                                        |
| Imaging Display Window           | Displays windows in the application beginning with the main window and describes the use.                                                                                                                                                                                      |
| Error Code Lookup                | Displays the Error Lookup window so you can find out the meaning by entering the error code in the error message.                                                                                                                                                              |
| Legal Notices                    | Lists the medical and vendor regulations pertaining to this software.                                                                                                                                                                                                          |
| Use Internet Explorer for help.  | Sets the default browser to Internet Explorer. This is selected by default and it is not configurable.                                                                                                                                                                         |
| About                            | Displays the About window, which specifies the software name, current Patch number, current version and build, past versions installed, and so on.                                                                                                                             |

**Toolbar in the VistA Imaging Display Main Window**

| **Button**                                 | **Description**              |
|--------------------------------------------|------------------------------|
| <!-- image -->  Open the Image List window | Opens the Image List Window. |

| **Button**                                       | **Description**                                                                                                                                                                                                                                 |
|--------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <!-- image -->  Select/Create an Image Filter    | Opens the Image Filter List Add/Edit window.                                                                                                                                                                                                    |
| <!-- image -->  Open the Abstracts window        | Opens the Abstracts Window.                                                                                                                                                                                                                     |
| Open the VistA Health Summary Reports window     | Opens the Health Summary Report window. When the window opens, there may be many Health Summary Reports for the selected patient. You select the Health Summary Report from the list of reports that are available and the report is displayed. |
| <!-- image -->  Open the MUSE EKG viewing window | Opens the MUSE EKG viewer.                                                                                                                                                                                                                      |
| <!-- image -->  Open the User Preferences window | Opens the User Preferences window.                                                                                                                                                                                                              |
| <!-- image -->  Select a Patient                 | Opens the Patient Lookup window.                                                                                                                                                                                                                |
| Remote Image Views Configuration                 | Opens the Remote Image View Configuration window.                                                                                                                                                                                               |

<!-- image -->

<!-- image -->

**Fields**

| **Field**              | **Description**                                                                                                   |
|------------------------|-------------------------------------------------------------------------------------------------------------------|
| Patient                | Displays the patient name and identifier if a patient is selected. If no patient is selected, the field is blank. |
| Institution Identifier | Institution identifier that the client is currently logged in to. For example, SLC = Salt Lake City.              |

**Show Message History Window Button**

| **Button**                               | **Description**                                                                                                                                |
|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| <!-- image -->  Show/Hide Message window | Displayed in the lower left corner of the VistA Imaging main window, this button opens the Message History Window where you can view messages. |

### Selecting a Patient

Clinical Display provides three ways to select patients:

- Patient lookup box

- Menu bar or toolbar
- Image List toolbar

**Using the Patient Lookup Box**

The Patient lookup box enables you to quickly perform a patient lookup by not having to navigate a system menu or another popup window. Typing one of the following patient identifiers in the Patient lookup box displays one patient or a list of patients with similar names or other similar identifiers:

- Patient Name (or partial name)
- Full SSN
- Last four digits of the SSN
- Health Record Number (HRN) [for Indian Health Services (IHS) sites only].

**Notes** : (1) If you are at an IHS site, you can search for a patient by HRN. By default, the agency is initially set to the VA. If you are at an IHS site, screens and printed reports will use the HRN as the patient ID. (2) If you hold the MAG PAT PHOTO ONLY security key, you are only able to look up patients to verify their identities through a photo ID. You cannot view their medical records. Refer to *Appendix B: Clinical Display Security Keys* .

1. Type the patient identifier in the Patient lookup box.
<!-- image -->
    - If an exact match is found, then the patient is selected in the VistA Imaging Display main window. User Preferences can be set to open the Image List and or the Abstracts window when a patient is selected. Continue to the next section Working with the Image List.
    - If multiple patients match the patient identifier you entered, then the Patient Lookup window displays the matching patients and their demographics, as shown.
    <!-- image -->

1. Choose the patient by selecting the appropriate row and then click **OK** (or **Cancel** if the patient you are searching for is not listed).

If no match is found, the status message displays “NO MATCH for lookup on” (the patient identifier provided), as shown.

<!-- image -->

1. Enter a new patient name in the Patient lookup box.

**Note** : To work with the patient data, see the next chapter *Working with the Image List* .

**Using the Menu Bar or Toolbar**

1. In the VistA Imaging Display main window, perform either step:
    - Choose **File | Select Patient** from the menu bar.
    <!-- image -->
    <!-- image -->
    - Click the **Select a Patient** button   on the toolbar.

If an exact match is found, the Patient Lookup window opens displaying the patient's data and the silhouette is replaced with the patient's photo.

<!-- image -->

If multiple patients match the patient identifier you entered, then the Patient Lookup window displays the matching patients and their demographics, as shown.

<!-- image -->

1. Choose the patient by selecting the appropriate row and then clicking **OK** (or **Cancel** if the patient you are searching for is not listed).

If no match is found, the status message displays “NO MATCH for lookup on” (the patient identifier provided), as shown. The Patient list and patient photo are blank.

<!-- image -->

1. Click **Cancel** or enter a new patient name or HRN to search.

**Note** : To work with the patient data, see the next chapter *Working with the Image List.*

**Using the Image List Toolbar**

The Image List window is explained in detail in the next chapter.

<!-- image -->

1. Click the **Open the Image List window** button   on the toolbar.
<!-- image -->
2. In the Image List window, click the **Select a Patient** button  on the toolbar.

**Note** : To work with the patient data, see the next chapter *Working with the Image List* window.

## Working with the Image List Window

<!-- image -->

The Image List Window  is used to perform the following tasks:

- Enables you to select an image or image group and opens the selection in the appropriate viewer or the Group Abstracts window (for image groups).
- Enables you to filter the patient’s images.
- Shows the remote sites that are connected or disconnected where the patient has images (if the ability to view remote images is enabled).
- Enables you to navigate to other windows and tools within the application through the button toolbar and file menu options.
- Indicates which images have existing annotations.

### Image List Window

<!-- image -->

<!-- image -->

<!-- image -->

In the Clinical Display Image List window, single images that have annotations have the Annotations  icon. An image group that contains one or more annotated images has the  Annotations icon.

### Menu Bar in the Image List

File Menu

| **Menu Option**                                          | **Description**                                                                                                                                             |
|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select Patient                                           | Opens the Patient Lookup window.                                                                                                                            |
| Open Image                                               | Opens the image.                                                                                                                                            |
| Open Image in 2nd Radiology Window                       | Enables the user to view two DICOM images side by side                                                                                                      |
| Image Copy                                               | See Printing and Copying Images                                                                                                                             |
| Image Print                                              | See Printing and Copying Images                                                                                                                             |
| Image Print Options                                      | Opens the Image Print Options window.                                                                                                                       |
| Image Report                                             | Opens the Image Report for the selected image.                                                                                                              |
| Image Delete (shown if a single image is selected)       | Opens the Image Delete window.                                                                                                                              |
| Image Group Delete (shown if an image group is selected) | Opens the Image Delete window.                                                                                                                              |
| Image Index Edit                                         | Opens the Image Index Edit window for the selected image.                                                                                                   |
| Image Information                                        | Opens the Image Information window.                                                                                                                         |
| Image Information Advanced                               | Opens the Image Information/properties window.                                                                                                              |
| Cache images                                             | Caches the currently selected image in the background to the workstation, enabling you to continue working while the images are brought to the workstation. |
| Close                                                    | Closes the Image List window                                                                                                                                |
| Exit                                                     | Closes the imaging session                                                                                                                                  |

Context Menu

| **Menu Option**                                                                 | **Description**                                                                 |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| Pertains to CCOW compliance. See Appendix D: Clinical Context Object Workgroup. | Pertains to CCOW compliance. See Appendix D: Clinical Context Object Workgroup. |

Options Menu

| **Menu Option**        | **Description**                                |
|------------------------|------------------------------------------------|
| Refresh Patient Images | Refreshes the list of images and image status. |

| **Menu Option**                  | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Prefetch Patient Images          | All images for the patient are queued to be copied from the Jukebox to the Magnetic Image server for faster loading of images. User must have a MAG PREFETCH Security Key.                                                                                                                                                                                                                                                     |
| User Preferences                 | User Preferences has the following options:  - Configure User Preferences - Displays the User Preferences window. - Save Settings Now - Equivalent to the Windows Save button to explicitly save settings as you go along. - Save Settings on Exit - When selected the settings are saved on exiting Clinical Display. When not selected, all changes to settings are lost on exiting if you do not manually save the changes. |
| Remote Image Views Configuration | Configures remote image views (RIVs).                                                                                                                                                                                                                                                                                                                                                                                          |
| Shows Hints                      | Shows Hints has the following options:  - Show Hints on This Window - When selected a check mark appears. - Hints OFF for all windows - When selected a check mark appears and hints are not shown. - Hints ON for all windows - When selected a check mark appears and hints are displayed.                                                                                                                                   |
| Browse Image List                | Normally focus will shift to the image when an image is opened. To enable browsing a patient’s images with the arrow keys, the user would select ‘Browse Image List’.                                                                                                                                                                                                                                                          |
| CPRS Sync Options                | Allows user to break the link to CPRS. Enabled only if VistA Imaging was started from the CPRS Tool menu.                                                                                                                                                                                                                                                                                                                      |
| Shortcut Key legend              | Opens the Short Cut Key Legend which is shown in the System References section of this manual.                                                                                                                                                                                                                                                                                                                                 |
| Message Log                      | Opens Message History Window.                                                                                                                                                                                                                                                                                                                                                                                                  |
| Disable Automatic Color Channel  | By disabling the automatic separation, color images will load and display faster. When disabled, the user can choose to show color channels on an image by image basis.                                                                                                                                                                                                                                                        |

View Menu

| **Menu Option**   | **Description**                                                   |
|-------------------|-------------------------------------------------------------------|
| MUSE EKG Window   | Opens the MUSE EKG window.                                        |
| Group Window      | Brings the Group Abstracts window to the forefront if it is open. |
| Radiology Exams   | Opens the Radiology Exams window.                                 |
| Progress Notes    | Opens the Progress Notes window.                                  |

| **Menu Option**   | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Toolbars          | Toolbars has the following options:  - Main Toolbar - The top toolbar of the window. - Main Toolbar in tree - If the Tree View is visible the user can insert the Main Toolbar at the top of the Tree View. This option gives the maximum area to the Image Panel when viewing images in the Image List window. - Image Toolbar - Is the toolbar for the Image Viewer. - Tree Sort Buttons - This will show/hide the Tree Sort button toolbar. - Filter Buttons - This will show/hide the Filter Button bar. - Remote Connections - This will show/hide the remote image connection toolbar at the bottom of the Image List window. |
| Active windows    | Displays the active windows                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Go to Main Window | Sets focus on the Main Window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

Reports Menu

| **Menu Option**   | **Description**                                                         |
|-------------------|-------------------------------------------------------------------------|
| Patient Profile   | Displays the Patient Profile report for a selected patient.             |
| Health Summary    | Displays the VistA Health Summary report window for a selected patient. |
| Discharge Summary | Displays the Discharge Summaries window for a selected patient.         |

Filters Menu

| **Menu Option**                    | **Description**                                               |
|------------------------------------|---------------------------------------------------------------|
| Image List Filters                 | Opens the Image Filter Add/Edit window.                       |
| Filter Details                     | Displays the filter Information window for the active filter. |
| Refresh Filter list                | Refreshes the filter list.                                    |
| Filters as Buttons                 | Turns on or off filters as buttons.                           |
| Multi-Line Tabs                    | Turns on or off multi-line tabs.                              |
| Include Deleted Image Placeholders | Displays or hides deleted image placeholders.                 |

Layouts Menu

| **Menu Option**   | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Abstracts         | Abstracts has the following options:  - Show Abstracts – This item works when abstracts are shown in the Image List window or the Abstracts window itself. Selecting or clearing this item will show or hide the Abstracts Component on the Image List window or the Abstracts window if “Abstracts Viewer in Separate Window’ is selected. - Abstracts Bottom – Position the Abstracts at the bottom of the window. - Abstracts Left – Positions the Abstracts to the left side of the window. - Abstracts Bottom Tree – Positions the Abstracts to the bottom of the Tree View. The Tree View will become visible when this option is selected. - Abstract Viewer in Separate Window –  View the abstracts in a separate window.  - Refresh – Reloads all abstract images. |

| **Menu Option**                                                                                                                                                                                                                                                                  | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tree view  For details, see  *Using the Tree View*  Window  <!-- image -->  In the tree view, single images that have annotations have the Annotations indicator. A group of images that has annotations has the Annotations icon..  <!-- image -->  Configure Tree View Window. | Tree view has the following options:  - Show Tree View – Show or Hide the Tree View. - Sort Buttons – Show or Hide the Tree Sort buttons. - Auto Expand/Collapse – If selected then the Tree Level will collapse when an item from a different branch is selected. - ‘Specialty – Event’ – Configure Tree View with Specialty Index value as the first branch and Event as the second. - ‘Type – Specialty’ – Configure the Tree View with the Type Index value as the first branch and the Specialty as the second. - ‘Package – Type’ – Configure the Tree View with Package Index value as the first branch and Type as the second. - Custom – Opens the Configure Tree View window - Expand All – All levels of the tree are expanded. - Expand 1 level – All Tree nodes are expanded so that the first level is visible. This is useful when multiple tree levels are used. - Collapse All – All levels are collapsed so that only the first level of the image properties is visible. - Refresh – Refreshes the Tree View listing. <!-- image --> |

| **Menu Option**                      | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| List view                            | List view has the following options:  - Show Image List – Show or Hide the List View. - Select Columns – Opens the Column Selector window - Fit to Text – Select to resize the columns so that they will display the longest entry. - Fit to Window – Adjusts the columns to fit in the Image List window - Show Grid – Display or hide the grid. The grid provides an easy way to measure and compare portions of the study. Studies can be displayed both with the grid on and off. To toggle the grid, select the Display/Hide Study. - Preview Abstract – Previews the abstract of the selected image - Preview Report – Previews the report of the selected image - Refresh – Refreshes the list of images for the selected patient.  **Note**  : If both the Tree View and List View (and optionally the Abstracts) are visible, all data is updated when the patient images are refreshed. |
| Explorer Style                       | Tree View to the left and the image on the right                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Explorer with List                   | Same as the Explorer style plus the list view on top of the image                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Explorer with Abstracts              | Same as the Explorer style plus the abstracts displayed at the bottom of the Tree View                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Abstract strip                       | Abstracts at the bottom of the window and the Full Resolution image displayed at the top.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Abstract strip left                  | Abstracts to the left of the window and the Full Resolution image displayed on the right.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Abstract strip with List             | Same as Abstracts strip left plus the list view to the top of the Full Resolution image.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| List with Previews                   | List view is on the top with Abstracts, Image Information and Image Report panes visible as preview panes. The panes are updated when a new entry is selected in the list.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Document Viewer in a separate window | If selected this will display the Full Resolution Image in the Full Resolution window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

| **Menu Option**    | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Set Active Control | The menu item makes navigation easier for the Image List. An indicator can be used to visually determine the active control and Short Cut keys are available to navigate to the main controls on the Image List window.  Set Active Control has the following options:  - Abstract – This will set the Abstract Viewer as the active control. If the Abstract window is where the abstracts are being shown then this function will Open the abstract window and set focus to it. - Tree View – Tree View control in the Image List window will be made the active control. It will be made visible. - List View – The List View control in the Image List window will be made the active control. It will be made visible. - Full Resolution Viewer – This will set the Full Resolution Viewer as the active control. If the Full Resolution window is where Images are being shown then this function will Open the Full Resolution window and set focus to it. - Active Control Indicator – If selected a yellow bar will be displayed to the left of the control that currently has focus. |

Utilities Menu

| **Menu Option**   | **Description**                                                                                                                                                                                                                                                                                         |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| QA Review         | QA Review – Opens the QA Review Window.                                                                                                                                                                                                                                                                 |
| QA Review Report  | Opens the Select a Date Range window with the QA Review / Image Status Report window in the background.  **Note**  : The QA Review / Image Status Report window is a blank report template. When you specify the date range and click OK, the results are displayed in the QA Statistics Report window. |
| Edit Index fields | Opens the Image Index Edit window.                                                                                                                                                                                                                                                                      |

| **Menu Option**         | **Description**                                                                                                                                                                                                                                              |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ROI Processing Options1 | ROI Print Options menu has the following submenus:  - Print all listed images…– Opens the ROI Processing window. - Choose Images to Process – Opens a dialog box in which you can select the images you want Clinical Display to process for ROI disclosure. |
| ROI Processing Status1  | Displays the ROI status screen.                                                                                                                                                                                                                              |
| Image Status            | Displays the current image status and allows the user to change the image status from the current status to: Viewable, QA Reviewed, or Needs Review (block from view).                                                                                       |
| Controlled Status       | Changes the “Controlled” status of an image (controlled image on the Utilities menu) to “Controlled” or “Not Controlled.” When you select Refresh, the image entry is marked as controlled in the Image List, tree view, and Abstract viewers.               |

Manager Menu

| **Menu Option**                                                                                                 | **Description**                                                                                                 |
|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| The menu option requires the MAG SYSTEM security key. See Appendix E: For System Managers for the menu options. | The menu option requires the MAG SYSTEM security key. See Appendix E: For System Managers for the menu options. |

Help Menu

| **Menu Option**      | **Description**                                         |
|----------------------|---------------------------------------------------------|
| Image Listing window | Displays the online help file for the Image List window |
| About                | Opens the About window.                                 |

***Using the Tree View Window***

<!-- image -->

<!-- image -->

In the tree view, single images that have annotations have the	Annotations indicator. A group of images that has annotations has the Annotations icon. **.**

<!-- image -->

1 Requires the MAG ROI key.

<!-- image -->

***Configure Tree View Window***

The Configure Tree View window is opened from the **Layouts | Tree view** menu by selecting the **Custom** menu option.

<!-- image -->

Select an item in the **Property Title** list and it will be added as the next tree level. To remove a Level, drag it away with the mouse and drop it (anywhere).

Click the **OK** button and the tree view will be reconfigured with the selected image properties as the new levels. Clicking **Cancel** will close the window without applying the changes.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

**Note** : In the graphic, the user selects Captured By ‘Cap By’ and then the Short Description ‘Short Desc’.

<!-- image -->

**Toolbar in the Image List Window**

**Note** : When no patient is selected, a silhouette is displayed in place of the patient's photo.

| **Button**                             | **Description**                                                                                                                                                                                               |
|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select a Patient                       | Opens the Patient Lookup window.                                                                                                                                                                              |
| Refresh Patient Images                 | Refreshes the list of images for the selected patient  **Note**  : If both the Tree View and List View (and optionally the Abstracts) are visible, all data is updated when the patient images are refreshed. |
| Select/Create an Image Filter          | Opens the Image Filter Add/Edit window.                                                                                                                                                                       |
| Configure User Preferences             | Opens the User Preferences window.                                                                                                                                                                            |
| Show/Hide Abstracts                    | Displays or hides image abstracts in the Image List window.                                                                                                                                                   |
| Open the Image                         | Opens the selected image.                                                                                                                                                                                     |
| Open the Report                        | Opens the report associated with the selected image.                                                                                                                                                          |
| Preview Abstract of selected list item | Previews the abstract of the selected image.                                                                                                                                                                  |
| Preview Report of selected list item   | Previews the report of the selected image.                                                                                                                                                                    |
| Fit Columns to  Text                   | Select to resize the columns so that they will display the longest entry.                                                                                                                                     |
| Fit Columns in Window                  | Adjusts the columns to fit in the Image List window.                                                                                                                                                          |

| **Button**                               | **Description**                            |
|------------------------------------------|--------------------------------------------|
| Select Columns                           | Selects a column in the Image List window. |
| <!-- image -->  Open the MUSE EKG window | Opens the MUSE EKG viewing window.         |

<!-- image -->

**Filter Buttons**

The Filters menu enables you to set user preferences to add, remove, and display filters as buttons. Buttons on the Filters menu provide quick access to filters. The following buttons are displayed above the list pane to sort the images.

<!-- image -->

| **Button**      | **Description**                                                 |
|-----------------|-----------------------------------------------------------------|
| #Adv Directives | Filter to show all of the images that are Advanced Directives   |
| #Clin 2Yr       | Filter to show all Clinical images acquired in the last 2 years |
| #Clin All       | Filter to show all of the clinical images                       |
| #Rad All        | Filter to show all radiology images                             |

<!-- image -->

In the Item column,, the following icons indicate in the Image List and Tree View:

| **Icon**       | **Description**                                                                                                 |
|----------------|-----------------------------------------------------------------------------------------------------------------|
| <!-- image --> | Indicates the image has associated annotations.                                                                 |
| <!-- image --> | Indicates the image group has one or more images with associated annotations.                                   |
| <!-- image --> | Indicates a single image.  Single images are not part of an image group.                                        |
| <!-- image --> | Indicates an image group  An image group is a collection of related single images of the same or mixed formats. |
| <!-- image --> | Indicates an image that has been cached.                                                                        |
|                | Indicates a "Needs Review" status                                                                               |
|                | Indicates a "TIU Authorization Failed" status.                                                                  |
| <!-- image --> | Indicates that the image has been updated in the database and needs to be refreshed in the Image List.          |

<!-- image -->

<!-- image -->

| **Icon**       | **Description**                                                                                                                                                                                                |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <!-- image --> | Indicates the image has associated annotations.                                                                                                                                                                |
| <!-- image --> | Indicates the image group has one or more images with associated annotations.                                                                                                                                  |
| <!-- image --> | Indicates that the image is a Controlled Image.                                                                                                                                                                |
| <!-- image --> | Deleted Image. Deleted image placeholders are displayed when the user selects Filters &#124; Include Deleted Image Placeholders option from the Image list window. This setting is saved as a user preference. |
|                | Deleted Image group. Indicates that the group of images has been deleted. This icon is displayed when Include Deleted Image Placeholders is selected.                                                          |

<!-- image -->

**Display of the Column Listings**

You can vary the display of the data in the following ways:

- Sort the order of images by selecting a column heading.
- Change the column width by selecting the column dividers and dragging them to the left or right.
- Display a popup menu of options by right-clicking in the Image List.
<!-- image -->
- Display or hide columns by right-clicking in the Image List and clicking the **Select Columns** option to open the Column Selector window shown. You can select each column name or click **All** to select all column names to display. When you are finished, you can click **OK** to save and close, or **Apply** and **Close** .

<!-- image -->

<!-- image -->

**Popup Menu in the Image List Window**

| **Menu Option**            | **Description**                                                                                                          |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------|
| Open Image                 | Opens the selected image in the appropriate viewer, Full Resolution, Radiology, or Group Abstracts.                      |
| Image Report               | Opens the Image Report for the selected image.                                                                           |
| Image Delete               | [security key required] See Appendix C: Deleting Images.                                                                 |
| Image Index Edit           | [security key required] See  *Appendix B: Clinical Display Security Keys.*                                               |
| Image Information          | Displays the image information for the image.                                                                            |
| Image Information Advanced | [security key required] Displays more detailed image information exclusively for system managers. See Image Information. |
| Cache Images               | <!-- image -->  Caches images and marks the row in the image list with a  .                                              |
| Select Columns             | Displays the Column Selector window.                                                                                     |
| Fit Columns to Text        | Resize the column so that all text is visible.                                                                           |
| Fit Columns to Window      | Resizes the columns so that they fit to the window size.                                                                 |

**Image Information Window**

**Note** : See *Image Information Window* and *Viewing Image Information* in the chapter *Working with Abstracts* .

### Working with Filters in the Image List Window

The Image List and Abstract windows are populated based on the filters that are set. Only the images that fit the criteria of the selected filter are displayed. You can use filters to limit the number of images displayed such as Clinical Type, Specialty or Sub Specialty, or Procedure and Event.

Filters are used in two modes in the interface:

- Normal, used in the Image List window
- Advanced, used in the QA Review utility

**Note** : Security keys are required. See *Applying Advanced Filters to the QA Review* .

The two types of filters used in the Image List are:

- Public = filters available to all users indicated by pound (#) sign before the name. An example of a public filter is ‘#Clin All’ images.

**Note** : Only users holding the MAG SYSTEM security key can create public filters.

- Private = user-specified and available only for users who create them

**Applying the Filters in the Image List**

Available filters are usually shown as buttons at the top of the Image List. To filter information in the lists, click a filter button for that filter.

If the filter buttons are not visible, they can be displayed as follows:

1. To display all the filters as buttons above the list pane in the Image List window, select
##### Filters | Filters as Buttons.
    1. To display the filters in stackable rows of buttons, choose **Filters | Multiline Tabs** .
**Image Filters Add/Edit Window**
<!-- image -->
File Menu
| **Menu Option**   | **Description**                                                       |
|-------------------|-----------------------------------------------------------------------|
| New               | Allows you to create a new filter.                                    |
| Save              | Saves changes to the selected filter.                                 |
| Save As           | Saves the filter with a new name.                                     |
| Save as Public    | Saves the filter as a public filter. For MAG SYSTEM key holders only. |
Edit Menu
| **Menu Option**   | **Description**              |
|-------------------|------------------------------|
| Delete Filter     | Deletes the selected filter. |
Options Menu
| **Menu Option**         | **Description**                               |
|-------------------------|-----------------------------------------------|
| Clear All               | Clears all filter selections.                 |
| Refresh Drop Down Lists | Refreshes all drop down lists for the filter. |
| **Menu Option**      | **Description**             |
|----------------------|-----------------------------|
| Refresh Filter lists | Refreshes the filter lists. |
| Refresh Details      | Refreshed the filter.       |
Help Menu
| **Menu Option**   | **Description**                       |
|-------------------|---------------------------------------|
| Image Filter      | Displays the Image Filters help file. |
**Creating Private Filters**
    1. To create a private filter, perform one of the following steps:
    <!-- image -->
        - In the VistA Imaging Display main window, either click the **Select/Create an Image**
##### Filter button
menu bar.on the toolbar or choose **Options | Image List Filters** from the
<!-- image -->
    - In the Image List window, either click the **Select/Create an Image Filter** on the toolbar or choose **Filters | Image List Filters** from the menu bar.
    <!-- image -->
The Image Filters Add/Edit window opens.
    1. Choose **File | New** from the menu bar.
        - The filter information in the Filter Details pane is cleared so that you can specify a new filter.
        - The title bar changes from the current filter to "Image Filter Add/Edit: Custom" to indicate that you are working in custom mode when you create a filter. Once the filter is saved and you select it in the Private or Public pane, the filter name is displayed in the title bar in place of "Custom".
    1. Select the General Properties tab in the lower pane.
    2. At the Class of Images field, select a class:
        - Clinical for diagrams and images
        - Administrative for Means Test, Forms, Advanced Directives**Note** : For some users, only the **Clinical** setting is available, as shown. Filters can be either Clinical or Administrative. System Administrators assign users access to Clinical , Administrative or both types of filters.
    1. Select the data range from the drop-down list.
    2. At the Origin of the Image field, click the **Select** button, specify the origins for the filter in the Origin Selection window, and click **OK** .
    3. Select the Clinical Properties tab and on the Packages window displayed, select the VistA packages that you want.
    <!-- image -->
    4. For the Clinical Types,, Specialty/SubSpec, and Procedure/Event windows, select the filter criteria that you want.**Note** : If you do not make a selection, the system includes all of the entries in the list. All three windows work the same way.
<!-- image -->
    1. To save your new private filters, click the **Save** button at the bottom of the Image Filter Add/Edit window.
    2. In the Save As Private Filter window displayed, enter the name of the new filter in the Private Filter Name field**Note** : The filter name must be at least three characters in length with no special characters (like punctuation marks or slashes). The name can be all numeric, all alphas, or mixed.
    1. Click **Save** and then **OK** or **Close** .**Note** : The **Save As** button operates the same way. The **OK** button does not save the filter information but simply closes the window like the **Close** button.**Important** : If you have the MAG SYSTEM security key, you can choose the **File| Save as Public** option to save the filter as a public filter.
The filters are listed at the bottom of the Filters menu. The first group is private filters, shown as numbers 1 – 6 in the example. The second group is public filters, shown as numbers 1-9 in the example.
<!-- image -->
When you select a patient, the total image count for the patient will be displayed with the number of images that match the filter in use. In the following example, there are 13 images for this patient and all 13 match the Clinical All filter.
<!-- image -->
**Editing or Deleting a Private Filter or Filter Details****Note** : You can edit a Private Filter by selecting the filter name from the Private tab. You can create a new filter by the same name as an old filter and then save and overwrite the old filter.
    1. Open the Image Filter Add/Edit window.
Your newly created filters are listed in the Private filters pane, as shown in the example.
<!-- image -->
    1. To clear the fields but keep the filter, select the filter in the Private pane and choose**Options | Clear All** from the menu bar.
    1. Re-enter the filter values and save.
    2. To delete a filter, right-click it in the Private filters pane and click **Delete,** or select the filter and choose **Edit | Delete Filter** .
    <!-- image -->
    3. Click **OK** in the delete confirmation message.
    4. To refresh your filters, choose any of the following options from the menu bar:
##### 1 Options | Refresh Drop Down Lists
##### 2 Options | Refresh Details
    1. After you are finished, choose **Filters |Filter Details** to view your filters in detail, as shown in this example.
    <!-- image -->
**Viewing Deleted Image Placeholders**To show or hide deleted image placeholders, select **Filters | Include Deleted Image Placeholder.** Selecting this option enables the display of deleted image placeholders for a deleted image in the Image List window and the Abstracts window. This option is saved as a user preference.
<!-- image -->

<!-- image -->
The following icons are used for deleted image placeholders:

### Viewing Patient Clinical Records in VistA

Patient clinical records consist of:

- Radiology Exams
- Progress Notes
- Clinical Procedures
- Consults

You can view them using the View menu in the Main Display window. You can choose to display the radiology exams and progress notes when you select a patient by setting user preferences on the Image List window or the main Clinical Display window. See *Configuring the Display of Windows for Patient Selection.*

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

**Viewing Radiology Exams**

The Radiology Exam Listing window displays the radiology studies for the selected patient. You can view images associated with the exam report or view the exam report itself.

1. From the VistA Imaging Display main window or the Image List window, choose **View | Radiology Exams** from the menu bar.
<!-- image -->
2. Select a study and click on any of the following buttons to view the results or change the layout of the window.

| **Button**                         | **Description**                                                                                                             |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| View Image                         | View the images of a selected study in the Group Abstracts window.  **Note**  : Double-clicking the row works the same way. |
| View Report                        | View the report for the selected study.                                                                                     |
| <!-- image -->  Reset Column Width | Reset the column width on the exam listing window.                                                                          |
| Stretch Height to Maximum          | Set the exam window to the maximum height.                                                                                  |
| Reset to Starting Height           | Set the exam window to the starting height.                                                                                 |
| Help                               | Display user help for the exam window.                                                                                      |

**Viewing Progress Notes, Clinical Procedures and Consults**

1. To view the information from the main display window, choose **View | Progress Notes** , **Clinical Procedures** , or **Consults** .
2. To sort the list in a column, select the column header, and to reverse the order re-select the column header.
3. Double-click any Progress Note title to open the TIU Document Images window and the abstracts behave in the same way as they do in the Abstracts window and Group Abstracts window.

An example of a Progress Notes list is shown below. The Clinical Procedures and Consults lists are built and shown in the same window style.

<!-- image -->

<!-- image -->

1. To view the associated image, click the **View Image** button .
<!-- image -->
2. To view the associated report, click the **View Report** button .

**Note** : For details on displaying reports, see *Displaying Reports.*

<!-- image -->

1. To change the column width, drag the left or right border and to return to the original width, click the **Reset Column Width** button .

### Viewing Controlled Images in the Image List Window

<!-- image -->

To protect the privacy of the patient, images of a sensitive nature can be marked as controlled. You can mark an individual image or an image in a group as a controlled image. The Controlled Image icon   is displayed for an item in the tree view and Image List if the controlled image is a:

- Standalone (single) image
- Image Group
- Image Group where the first image in the group is controlled

**Note** : For a description of the types of controlled images, see *Controlled Images in the Abstracts Window.*

**Important** : To mark an image as a controlled image in the Image List, you must have a patient selected and the Image List open.

<!-- image -->

1. Select an entry in the Image List that does not have the Controlled Image   icon.
2. From the menu bar, choose **Utilities| Controlled Image** , and change the value for a controlled image to **True** .

**Note** : The Utilities Menu option is available only to holders of the MAG EDIT or MAG SYSTEM security keys.

<!-- image -->

<!-- image -->

1. Click the Refresh **Patient Images button** .

The image entry is now marked as controlled	in the Image List and tree view.

## Working with Abstracts

<!-- image -->

In Clinical Display, all images are displayed as abstracts in the Abstracts window. An *abstract* is a reduced quality representation (or thumbnail) of the actual image.

### Abstracts Window

The title bar of the Abstracts window displays the patient name. If multiple images fill the window, a scroll bar is automatically displayed to move through the images.

<!-- image -->

<!-- image -->

In the abstracts window, the	Annotations indicator in the upper left corner of the thumbnail for a single image indicates that annotations exist for the image. When the abstract is for an image group, the	Annotations indicator indicates that annotations exist for one or more images.

<!-- image -->

**Note** : Only abstracts that match the selected filter are displayed in the Abstracts window.

**Image Group Abstracts Window**

Selecting an image group abstract opens the Group Abstracts window and an abstract of each image of the group is displayed. Selecting any image in this group displays it in the appropriate viewer. The Group Abstracts window has the same properties as the Abstracts window.

**Note** : An Image Group is represented by showing the first image abstract in the group as the preview and text above the preview stating the number of images in the group.

<!-- image -->

In the Group Abstracts window, the	Annotations indicator indicates which images in the group have annotations.

<!-- image -->

**Image Information Window**

<!-- image -->

Image Information is displayed in the Image Information window when you right-click an abstract and select Image Information from the popup menu in the Abstracts window (or right- click a row in the Image List window). In the Image Information window, the	Annotations indicator in the upper left corner of the thumbnail indicates that annotations exist for the image.

<!-- image -->

This window provides the following information for verification purposes:

- Details about the image and the associated procedure
- Image ID and, if applicable, the image group
- Patient name
- Description of the image followed by the procedure and date
- Image indexes
- Capture date (date the image was added to the patient record) and user who captured the image
- Status and reason for the status
- Indication that the image has associated annotations

**Toolbar in the Abstracts Window**

| **Button**                             | **Description**                                    |
|----------------------------------------|----------------------------------------------------|
| <!-- image -->  Next Page              | Displays the next page of images.                  |
| <!-- image -->  Previous Page          | Displays the previous page of images.              |
| <!-- image -->  Decrease Abstract Size | Decreases the size of all the displayed abstracts. |
| <!-- image -->  Increase Abstract Size | Increases the size of all the displayed abstracts. |

| **Button**              | **Description**                 |
|-------------------------|---------------------------------|
| <!-- image -->  Refresh | Refreshes the Abstracts window. |

**Popup Menu in the Abstracts Window**

By right clicking on any image abstract you will open a popup menu. This popup menu gives you shortcuts to options and actions you may perform. Certain options are unavailable depending on the security keys that you hold.

<!-- image -->

| **Menu Option**            | **Description**                                                                                                                                                                                                                             |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Open Image                 | Opens the selected image in the appropriate viewer such as Full Resolution, Radiology, or Group Abstracts.                                                                                                                                  |
| Image Report               | Opens the Image Report for the selected image.                                                                                                                                                                                              |
| Image Delete               | Deletes an image only if you hold the proper security keys. See Appendix C: Deleting Images.                                                                                                                                                |
| Image Information          | Opens the Image Information Window.                                                                                                                                                                                                         |
| Image Information Advanced | Opens the Image Information/Properties Window.                                                                                                                                                                                              |
| Cache Images               | Cache all the images in the selected group in the background                                                                                                                                                                                |
| Image List Filters         | Opens the Image Filters Add/Edit Window.                                                                                                                                                                                                    |
| Refresh                    | Refreshes the Abstracts window.                                                                                                                                                                                                             |
| Resize the Abstracts       | When selected, an abstract displays a green border that you can drag to the size that you want. When you select  **Finish**  in the Resize Abstracts window, all the abstracts are resized to the same dimensions as the selected abstract. |

| **Menu Option**   | **Description**                                                                                                                                                                        |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Options           | Displays the following options, which are the same as the buttons on the toolbar:  <!-- image -->  **Note**  : The Previous Abstract and Next Abstract buttons are not on the toolbar. |
| Font Size         | Selectable font sizes from 6pt to 12pt.                                                                                                                                                |
| Toolbar           | Displays or hides the toolbar in the Abstracts window.                                                                                                                                 |
| Show Hints        | Activates or deactivates the Hints.                                                                                                                                                    |
| Go to Main Window | Displays the VistA Imaging Display Main Window.                                                                                                                                        |
| Active Windows    | Displays a list of active windows. Select one of the windows from the list to bring the window to the front.                                                                           |
| Help              | Displays online help.                                                                                                                                                                  |

### Viewing Abstracts

1. From the VistA Imaging Display main window, select a patient.
<!-- image -->
2. Click the **Open the Abstracts Window** button  tool on the toolbar. The Abstracts window opens with the abstracts displayed.
3. Click on a single abstract to open the image in full view.

The appropriate viewer is selected. For details on the various viewers, see *Description of the Viewers.*

1. To view an image group, select the image group that you want to view. The group opens in the Group Abstracts window.
2. Click an image.

The image is displayed in full view in the appropriate viewer.

**Note:** If the Deleted Image placeholder is checked, the abstracts window will display the deleted image placeholder icon.

### Viewing Image Information

1. To view the image information either:
    - In the Image List window, right-clicking a row and select **Image Information.**
    - In the Abstracts window, right-click an abstract and select **Image Information.**
2. View the information as shown in this example and then click **Close** .

### Synchronizing Image Data in Related Windows

Clinical Display synchronizes the selected images in the related windows for a selected patient. For example, if you select an image in the Image List window the abstract of that image will be selected in the Abstracts window, it will be displayed in the appropriate viewer, as shown in the example below.

If the Image List window is configured to show the image lists, tree view, abstracts, and report previews the same image will be selected in each of the panes of that window.

<!-- image -->

**Note** : Even if you do not have the Abstracts and Image List displayed in the same window, they will be synchronized, along with all of the other windows such as the Preview Report and Information panes.

### Viewable and Non-Viewable Images

The following sections explain which images are viewable and non-viewable for various reasons.

**Images That Are Not Viewable Due to an Error**

If any of the following bitmaps are displayed in the Abstracts window instead of the actual image, the following table explains how to resolve this problem.

| **Bitmap**     | **Reason and Solution for Inability to View an Abstract**                                                                                                                                                                                                                                                   |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <!-- image --> | If one of the abstracts is located on the Juke Box, 'Display Juke Box Images' must be selected in the View Preferences window to have the abstract displayed. Otherwise, this generic bitmap is displayed. Clicking this button causes the full resolution image to be displayed in the appropriate window. |
| <!-- image --> | If the VistA Imaging application cannot connect to the VistA Imaging Network server to retrieve images, this Error bitmap is displayed. Call the IRM Service to report this problem.                                                                                                                        |
| <!-- image --> | If an image from a PACS device has not been copied to the VistA Imaging server, this PACS bitmap is displayed. REDACTED                                                                                                                                                                                     |
| <!-- image --> | If an image group from a PACS device has not been copied to the VistA Imaging server, this PACS Group bitmap is displayed. REDACTED                                                                                                                                                                         |
| <!-- image --> | If an Error occurs in displaying an abstract, this Error opening abstract bitmap is displayed. Call the IRM Service to report this problem.                                                                                                                                                                 |
| <!-- image --> | If the Abstract file is corrupt or cannot be opened by VistA Imaging, this Format Error bitmap is displayed. Call the IRM Service to report this problem.                                                                                                                                                   |
| <!-- image --> | If the Image file is a motion video file, this Motion Video bitmap is displayed. Selecting this graphic causes the motion video to be displayed in the Video window.                                                                                                                                        |
| <!-- image --> | If the abstract does not exist on the Image Server, this Abstract Not Found bitmap is displayed. Selecting the graphic may display the full-resolution image in the appropriate window.                                                                                                                     |
| <!-- image --> | If there is a possible database integrity problem with the Image File entry, this ID mismatch bitmap is displayed. This image may require corrections.  Contact the site’s Imaging ADPAC and/or Coordinator.                                                                                                |

**Blocked Images in the Abstracts Window**

Some images are blocked from view for some users. Such images are labeled as blocked and the abstract is displayed as the bitmap shown:

<!-- image -->

Users who do not hold the **MAG EDIT** or **MAG SYSTEM** security keys are blocked from viewing images marked as Needs Review. The three types of blocked images are:

- TIU business rules (set in VistA and enforced in Clinical Display). If you select an image that is blocked due to a TIU Authorization failure, the system displays the following message.
<!-- image -->

**Exception** : If you hold the **MAG DELETE** security key, you can view the Image from the Image Delete window to make an informed decision before deleting it.

- Questionable Integrity: When an image entry is accessed for viewing the Questionable Integrity (QI) check is run before the image data is returned to the Client. If the image data does not pass the QI check then the image is marked as QI.
- Images That Need Review

If you select an image with a status of “Needs Review” and are assigned the MAG EDIT or MAG SYSTEM security key, the system displays a warning message explaining that the image is a blocked non-viewable image with a status of “Needs Review”. Clicking **OK** closes the message but clicking **Ignore** enables you to view the image.

<!-- image -->

If you select an image with a status of “Needs Review” and are not assigned the MAG EDIT or MAG SYSTEM security key, the system displays a warning message that the image is not viewable with the status of "Needs Review". Clicking **OK** closes the message.

<!-- image -->

**Controlled Images in the Abstracts Window**

To protect the privacy of the patient, images of a sensitive nature can be marked as controlled. The abstracts of controlled images are not displayed.

You can mark an image "controlled" through the Index Edit Utility if you are assigned the **MAG EDIT or MAG SYSTEM** security key. The default bitmap of a window shade with the text Controlled Image is shown in place of the abstract.

<!-- image -->

A controlled image can be opened by clicking the   default bitmap.

**File Types Viewable in Clinical Display**

The following file types when selected in the Abstracts window are automatically displayed in full view in the following viewers in Clinical Display.

| **File Extension**   | **Image Type**            | **Viewer Used**        |
|----------------------|---------------------------|------------------------|
| 756                  | Historical 756            | Radiology Viewer       |
| ASC                  | Text file Image extension | Full Resolution Viewer |
| AVI                  | Motion Video              | Video Player           |
| BIG                  | X-ray big file 2000K      | Radiology Viewer       |
| BMP                  | Bitmap file               | Full Resolution Viewer |
| BW                   | Black and White           | Full Resolution Viewer |
| DCM                  | DICOM file                | Radiology Viewer       |
| HTM                  | Web Document              | Full Resolution Viewer |
| HTML                 | Web Document              | Full Resolution Viewer |
| JPG                  | Full Color                | Full Resolution Viewer |
| MHT                  | MIME HTML Document        | Full Resolution Viewer |
| MHTML                | MIME HTML Document        | Radiology Viewer       |
| PAC                  | X-ray image               | Radiology Viewer       |
| PDF                  | Adobe Acrobat             | Full Resolution Viewer |
| TGA                  | Targa Image               | Radiology Viewer       |
| TIF                  | Scanned Document          | Full Resolution Viewer |
| TXT                  | Text file import          | Full Resolution Viewer |

**File Types Viewable Using an Alternate Viewer**

When you select any of the following file types in the Abstracts window, you can choose to display the full view in Clinical Display or in an alternate viewer (outside Clinical Display) such as the Windows Media Player.

| **File Extension**   | **Image Type**                  |
|----------------------|---------------------------------|
| DOC/ DOCX            | Word Document                   |
| MP3                  | Motion Video MPEG-3             |
| MP4                  | Motion Video 4                  |
| MPEG                 | Motion Video                    |
| MPG                  | Motion Video                    |
| RTF                  | Rich Text Format                |
| WAV                  | Audio file                      |
| XML                  | Extensible Markup Language file |

**Watermarked Images for Rescinded Advance Directives**

When an Advance Directive Note is rescinded through the TIU menu option, the images that are attached to that note are watermarked with the text “Rescinded”. You can view the watermarked images when you select them. The following figure shows a watermarked image.

<!-- image -->

### Description of the Viewers

**Note** : The Clinical Display application automatically selects the appropriate viewer any time an image is opened from an abstract, the Image List, Tree View, menu options, etc.

You can view the image in full view in various ways:

- When you double-click an entry in the image list the image or image group is opened in the Full Resolution Viewer, Radiology Viewer, or for image groups, the Group Abstracts window is opened with the selected images.
- A user preference can be set to automatically select the row by just placing the mouse over the row.

Double-clicking a row opens the viewer for a single image, or the Group Abstracts window for image groups. A user preference can be set to automatically open the image in the appropriate viewer by just placing the mouse over the row.

**Full Resolution Viewer**

Clicking a single image abstract opens the image in the appropriate viewers. Non-DICOM images are automatically opened in the Full Resolution Viewer, as shown in this example.

<!-- image -->

The viewer provides tools to assist you while working with images. The configurable toolbar menus are explained in detail in this section. You can select one or more Non-DICOM images from the Abstracts window to load in to the viewer.

<!-- image -->

When you click on a single non-DICOM image that is not part of an Image Group from the Abstracts Window or the Image List, the image opens in the Full Resolution Viewer. The image is selected in the Abstracts window and the row is selected on the Image List.

If there are multiple images open in the Full Resolution Viewer you can bring an image to its full size in the viewer by moving the mouse over the image and double-clicking.

***Menu Bar in the Full Resolution Viewer***

File Menu

| **Menu Option**          | **Description**                                                                                                                        |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Duplicate Selected Image | Creates a copy of the selected image inside the Full Resolution Viewer. The duplicate image is treated as a unique and separate image. |
| Copy Image to Clipboard  | Copies the selected image to the Clipboard. See Printing and Copying Images for details.                                               |
| Print Image              | Prints the selected image. See Printing and Copying Images for details.                                                                |
| Print Options            | Opens the Image Print Options window.                                                                                                  |
| Image Report             | Opens the Image Report for the selected image.                                                                                         |
| Image Delete             | Delete the selected image. See Appendix C for deleting images.                                                                         |
| Close Selected Image     | Closes the selected image. If a duplicate was made of the image the duplicate will remain open.                                        |
| Close All Images         | Closes all of the images in the Full Resolution Viewer.                                                                                |
| Image Information        | If an image is selected the option opens the Image Information window.                                                                 |

| **Menu Option**            | **Description**                                                                 |
|----------------------------|---------------------------------------------------------------------------------|
| Image Information Advanced | If an image is selected the option opens the Image Information Advanced window. |
| Exit                       | Exits the Full Resolution Viewer.                                               |

Image Menu

| **Menu Option**     | **Description**                                                                                                                                                                                                                                                                                                                                                                             |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Apply to All        | When selected, all of the images opened in the Full Resolution Viewer will have all actions applied to them from the Image Menu options.                                                                                                                                                                                                                                                    |
| Zoom                | Zoom has the following options:  - Zooms In - to zoom in to an image - Zoom Out - to zoom out of an image - Fit to Width - to fit the image to the window width (horizontal) - Fit to Height - to fit the image to the height of the window (vertical) - Fit to Window - to fit the image to the entire window (vertical and horizontal) - Actual Size - to show image in its original size |
| Mouse               | Mouse has the following options:  - Pan - to pan image by dragging mouse - Magnify - to magnify an image where the mouse is clicked - Zoom - to zoom into an area of the image selected with the mouse - Pointer - to go back to mouse pointer                                                                                                                                              |
| Rotate              | Rotate has the following options:  - Right - Rotates the image 90 degrees clockwise - Left - Rotates the image 90 degrees counterclockwise - 180 - Rotates the image 180 degrees - Flip Horizontal - Flips the image horizontally - Flip Vertical - Flips the image vertically                                                                                                              |
| Contrast/Brightness | Contrast/Brightness has the following options:  - ‘Contrast +’ - Increases the contrast of an image - ‘Contrast –‘ - Decreases the contrast of an image - ‘Brightness +’ - Increases the brightness of an image - ‘Brightness –‘ - Decreases the brightness of an image                                                                                                                     |
| Invert              | Reverses the colors of the image.                                                                                                                                                                                                                                                                                                                                                           |

| **Menu Option**   | **Description**                                                                                                                                                                                                                                                                                                                                                                    |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Color Channel     | Enables users to select the color channel of a 24-bit image displayed in the viewer by selecting one of the following sub- menu options:  Full Color (RGB) – Displays all channels. Red Channel – Displays the red channel. Blue Channel – Displays the blue channel.  Green Channel – Displays the green channel.                                                                 |
| Reset             | Resets the currently selected image to its original display settings including zoom, contrast, window brightness, and orientation                                                                                                                                                                                                                                                  |
| Scroll            | Scroll has the following options:  - Top Left - scroll to the top left corner of the image - Top Right - scroll to the top right corner of the image - Bottom Left - scroll to the bottom left corner of the image - Bottom Right - scroll to the bottom right corner of the image - Left - scroll to the left - Right - scroll to the right - Up - scroll up - Down - scroll down |
| Maximize Image    | Enable image to fill the entire window.                                                                                                                                                                                                                                                                                                                                            |
| Previous Image    | Displays the previous image.                                                                                                                                                                                                                                                                                                                                                       |
| Next Image        | Displays the next image.                                                                                                                                                                                                                                                                                                                                                           |

View Menu

| **Menu Option**   | **Description**                                                                                                                  |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Viewer Settings   | Enables you to set default values for the number of rows and columns, and the maximum number of images to display in the viewer. |
| Refresh           | Refreshed the current view in the Full Resolution Viewer.                                                                        |
| Realign Images    | Realigns the images that are in the Full Resolution Viewer.                                                                      |
| Lock Image Size   | Locks the image size while it is being viewed.                                                                                   |
| Toolbar           | Displays the toolbar.                                                                                                            |
| Show Hints        | Displays Hints when the cursor is over a control in VistA Imaging.                                                               |
| Pan Window        | Opens a Pan Window.                                                                                                              |
| GoTo Main Menu    | Displays the VistA Imaging Display main window.                                                                                  |
| Active windows    | Displays the active windows currently open in VistA Imaging Display.                                                             |

Layout Menu

| **Menu Option**   | **Description**                                                                                                      |
|-------------------|----------------------------------------------------------------------------------------------------------------------|
| Tile All          | Images are resized and are positioned in the viewer as tiles.                                                        |
| Default Layout    | Restores the default layout.                                                                                         |
| Next Viewer Page  | Displays the next page of images. (This menu option is enabled only when there is more than one page of images.)     |
| Prev Viewer Page  | Displays the previous page of images. (This menu option is enabled only when there is more than one page of images.) |
| <!-- image -->    | Enable the user to customize the number and position of images in the window.                                        |

Page Menu

This Page Menu is only enabled when a multiple page image is selected.

| **Menu Option**   | **Description**                       |
|-------------------|---------------------------------------|
| First             | Go to the first page of the image.    |
| Previous          | Go to the previous page of the image. |
| Next              | Go to the next page of the image.     |
| Last              | Go to the last page of the image.     |

Help Menu

| **Menu Option**        | **Description**       |
|------------------------|-----------------------|
| Full Resolution Viewer | Displays online help. |

***Toolbars in the Full Resolution Viewer***

The Full Resolution Viewer has three toolbars, shown in the following example. The toolbars can be dragged and dropped in the viewer to place them side-by-side, two across and one down,

or stacked three high. Using the buttons on the three toolbars, you can manipulate the image and navigate around the Full Resolution Viewer.

<!-- image -->

Each toolbar is shown below with a description of each button in the toolbar.

| <!-- image -->                              |                                                                                                            |
|---------------------------------------------|------------------------------------------------------------------------------------------------------------|
| <!-- image -->  Apply Actions to all Images | Applies the actions to all images.                                                                         |
| <!-- image -->  Fit Image in Window         | Resizes the image to fit in the viewing window.                                                            |
| <!-- image -->  Fit to Width                | Fits the image to the width of the viewing window.                                                         |
| <!-- image -->  Zoom In                     | When selected, the image will magnify each time the button is clicked.                                     |
| <!-- image -->  Zoom Out                    | When selected, the image magnification will reduce each time the button is selected.                       |
| <!-- image -->  Mouse Magnifier             | When button is clicked, you use your mouse and scroll on the image and the area on the image is magnified. |

| <!-- image -->  Zoom in on Selected Area                | You select this option and set a point on the image. The image point selected zooms in or out with the movement of the mouse.   |
|---------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| <!-- image -->  Pan Image with Mouse                    | With the mouse a user clicks on the image and the image scrolls with the mouse movement.                                        |
| <!-- image -->  Mouse Pointer                           | Changes the mouse back to a pointing device.                                                                                    |
| <!-- image -->  Maximize Image                          | Button enables you to specify the image size and layout. A drop down list appears when selected with options for you to select. |
| <!-- image -->  Tile all Images                         | Images are resized and are positioned in the viewer as tiles.                                                                   |
| <!-- image -->  Rotate Counter Clockwise 90             | Rotates the Image 90 degrees counterclockwise each time the button is clicked.                                                  |
| <!-- image -->  Rotate Clockwise 90                     | Rotates the Image 90 degrees clockwise each time the button is clicked.                                                         |
| <!-- image -->                                          |                                                                                                                                 |
| <!-- image -->  Refresh Images                          | Refreshes the images.                                                                                                           |
| <!-- image -->  Remove Selected Image(s)(Not a Delete)) | Removes only the selected images from the Full Resolution Viewer pane.                                                          |
| <!-- image -->  Remove All Images (Not a Delete))       | Removes all of the images from Full Resolution Viewer pane.                                                                     |
| <!-- image -->  Image Report + Print Copy Menu          | In the drop down menu there are three options to: Copy Image, Print Image, and Image Report.                                    |
| <!-- image -->  Goto First Page                         | Go to the first page of a multi-page image.                                                                                     |
| <!-- image -->  Goto Previous Page                      | Go to the previous page of a multi-page image.                                                                                  |
| <!-- image -->  Goto Next Page                          | Go to the next page of a multi-page image.                                                                                      |
| <!-- image -->  GoTo Last Page                          | Go to the last page of a multi-page image.                                                                                      |
| <!-- image -->  Flip Vertical                           | Flips the image vertically.                                                                                                     |

| <!-- image -->  Flip Horizontal   | Flips the image horizontally.                                                                                                                                                                                                                                                                                                                                                                                                   | Flips the image horizontally.                                                                                                      |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| <!-- image -->  Invert Image      | Reverses the colors of the image.                                                                                                                                                                                                                                                                                                                                                                                               | Reverses the colors of the image.                                                                                                  |
| Color Channel                     | Cycles through the color channels of a 24-bit image. The view of the button changes depending on the channel that is displayed.  <!-- image -->  – View of the Color Channel button showing all channels  <!-- image -->  – View of the Color Channel button showing the red channel  <!-- image -->  – View of the Color Channel button showing the green channel  – View of the Color Channel button showing the blue channel |                                                                                                                                    |
| <!-- image -->  Reset Image       | Resets the currently selected image to its original display settings including zoom, contrast, window brightness, and orientation.                                                                                                                                                                                                                                                                                              | Resets the currently selected image to its original display settings including zoom, contrast, window brightness, and orientation. |
| <!-- image -->  Annotations       | Opens the Annotation toolbar and places the selected image in Annotation Mode.                                                                                                                                                                                                                                                                                                                                                  | Opens the Annotation toolbar and places the selected image in Annotation Mode.                                                     |
| <!-- image -->                    |                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                    |
| <!-- image -->                    |                                                                                                                                                                                                                                                                                                                                                                                                                                 | Magnification: Use the scroll bar to increase or decrease magnification.                                                           |
| <!-- image -->                    |                                                                                                                                                                                                                                                                                                                                                                                                                                 | Brightness: Use the scroll bar to increase or decrease brightness.                                                                 |
| <!-- image -->                    |                                                                                                                                                                                                                                                                                                                                                                                                                                 | Contrast: Use the scroll bar to increase or decrease contrast.                                                                     |

<!-- image -->

<!-- image -->

***Popup Menu in the Full Resolution Viewer***

Right-click an image in the Full Resolution Viewer displays the following popup menu.

**Note** : The commands in first group of the menu are a subset of the tools in the toolbar.

<!-- image -->

| **Menu Option**            | **Description**                                                                             |
|----------------------------|---------------------------------------------------------------------------------------------|
| Image Report               | Opens the Image Report for the selected image.                                              |
| Image Delete               | Deletes an image only if you hold the proper security keys. See Appendix C: Deleting Images |
| Image Information          | Opens the Image Information Window                                                          |
| Image Information Advanced | Opens the Image Information/Properties Window                                               |
| Font Size                  | Selectable font sizes from 6pt to 12pt.                                                     |
| Toolbar                    | Displays or hides the toolbar in the Abstracts window.                                      |
| Show Hints                 | Activates or deactivates the Hints.                                                         |
| Go to Main Window          | Displays the VistA Imaging Display Main Window.                                             |
| Help                       | Displays online help.                                                                       |

**Radiology Viewer**

Clicking a DICOM or TGA image from the Abstracts window, Image List window, or the Group Abstracts window, opens the image in the Radiology Viewer. The Radiology Viewer opens the images in a single view or group view.

***Single View***

If you select a single radiology image the viewer will open the image as a single view.

<!-- image -->

***Group View***

Selecting a group of DICOM images from the Group Abstracts window or from the Image List window opens the DICOM images in the Radiology Viewer but only one image at a time is displayed. Using the tools on the viewer the user is able to scroll through the images of the study.

<!-- image -->

You can view radiology studies using several views. One view is the Layout View which you can specify a 1x1, 2x1 or a 3x2, or a 4x3 view. Using the scroll wheel of your mouse you can move quickly between images in the stack or layout views.

If you double click an image in the layout view the image will appear in the stack view at full size. Additionally, if you double click the stack view will switch the study back to the layout view.

<!-- image -->

Clicking the Annotations  button opens the Annotation toolbar. You can annotate all images that open in the Radiology Viewer, such as dermatology and ophthalmology images. However, you cannot annotate RAD package images or DoD radiology images in the Radiology Viewer. For RAD package images and DoD radiology images, you can only create temporary measurements using the ruler and protractor tools on the Annotation toolbar.

***Menu Bar in Radiology Viewer***

File Menu

| **Menu Option**   | **Description**                                                                                                     |
|-------------------|---------------------------------------------------------------------------------------------------------------------|
| Copy              | Copies the image to the Clipboard. You must provide your electronic signature and the reason for copying the image. |
| Print             | Prints the image. You must provide your electronic signature and the reason for printing the image.                 |
| Print Options     | Opens the image Print Options window.                                                                               |
| Report            | Displays the report associated with the image.                                                                      |
| Exit              | Closes the Radiology Viewer.                                                                                        |

Image Menu

| **Menu Option**   | **Description**                                                                                                                                                                                                                                                                                                                                                                                              |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Apply to All      | Applies actions to all images.                                                                                                                                                                                                                                                                                                                                                                               |
| Zoom              | Zoom has the following options:  - Zooms In – to zoom in to an image - Zoom Out – to zoom out of an image - Fit to Width –to fit the image to the window width (horizontal) - Fit to Height - to fit the image to the height of the window (vertical) - Fit to Window –to fit the image to the entire window (vertical and horizontal) - Actual Size –to show image in its original size                     |
| Mouse             | Mouse has the following options:  - Pan - to pan image by dragging mouse - Magnify - to magnify an image where the mouse is clicked - Zoom - to zoom into an area of the image selected with the mouse - Annotations – to open the Annotations toolbar - Ruler – Ruler Measurement - Angle Tool – Angle measurement tool - Ruler/Angle Pointer – Measurement pointer - Auto Window/Level – Window/Level tool |
| Window/Level      | Window/Level has the following options:  - ‘Window +’ - Increases the contrast of an image                                                                                                                                                                                                                                                                                                                   |

| **Menu Option**   | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                   | - ‘Window –‘ - Decreases the contrast of an image - ‘Level +’ - Increases the brightness of an image - ‘Level –‘ - Decreases the brightness of an image                                                                                                                                                                                                                                                                                                                                                   |
| Invert (Reverse)  | Inverts the colors of the image                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Color Channel     | Enables users to select the color channel of a 24-bit image displayed in the viewer by selecting one of the following sub- menu options:  Full Color (RGB) – Displays all channels. Red Channel – Displays the red channel. Blue Channel – Displays the blue channel.  Green Channel – Displays the green channel.                                                                                                                                                                                        |
| Reset Image       | Resets the currently selected image to its original display settings including zoom, window/level, and orientation.                                                                                                                                                                                                                                                                                                                                                                                       |
| Reset All         | Resets all of the images to their original display settings including zoom, window/level and orientation.                                                                                                                                                                                                                                                                                                                                                                                                 |
| Scroll            | Scroll has the following options:  - Top Left - scroll to the top left corner of the image - Top Right - scroll to the top right corner of the image - Bottom Left - scroll to the bottom left corner of the image - Bottom Right - scroll to the bottom right corner of the image - Left - scroll to the left - Right - scroll to the right - Up - scroll up - Down - scroll down                                                                                                                        |
| Maximize Image    | Maximizes the current image (or if the current view is stack view, this changes the view to layout view). This option is not available if the current image is in the second stack.                                                                                                                                                                                                                                                                                                                       |
| Stack Cine        | Contains options for using the stack cine. This option is available only if the current view is a stack view.  Stack Cine has the following options:  - Start - Start the stack cine loop. - Stop - Stop the stack cine loop. - Speed Up - Speed up the stack cine loop. - Slow Down - Slow down the stack cine loop - Range Start - Set the start position for the stack cine loop. - Range End - Set the end position for the stack cine loop. - Range Clear - Clear the image for the stack cine loop. |
| First Image       | Moves to the first image in the study.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

| **Menu Option**      | **Description**                                                                                                                                             |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Previous Image       | Moves to the first image in the study.                                                                                                                      |
| Next Image           | Moves to the next image in the study.                                                                                                                       |
| Last Image           | Moves to the last image in the study.                                                                                                                       |
| Cache Selected Study | Caches the currently selected study in the background to the workstation, enabling you to continue working while the images are brought to the workstation. |

View Menu

| **Menu Option**   | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Pan Window        | A pane will open in the upper left corner of the display. This is the Pan Window box and it displays a full sized version of the image with the zoomed portion highlighted.  The scroll bar at the bottom of the box can be used to adjust the amount of magnification.  Move the scroll bar:  - to the right will increase magnification. - to the left will decrease magnification.  The mouse can be dragged around the image to move the highlighted area. |
| Go To Main Window | Changes the focus to the VistA Imaging Display main window.                                                                                                                                                                                                                                                                                                                                                                                                    |
| Active windows    | Displays the active windows currently open in VistA Imaging Display.                                                                                                                                                                                                                                                                                                                                                                                           |

Rotate Menu

| **Menu Option**     | **Description**                                                                                                                           |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Rotate Clockwise 90 | Rotates the currently selected image clockwise (to the right) 90  degrees. If “Apply-All” is selected, then all images will rotate.       |
| Rotate Minus 90     | Rotates the currently selected image counter clockwise (to the left) 90 degrees. If “Apply-All” is selected, then all images will rotate. |
| Rotate 180          | Rotates the currently selected image 180 degrees. If “Apply-All”  is selected, then all images will rotate.                               |
| Flip Horizontal     | Flips the currently selected image horizontally. If “Apply-All” is  selected, then all images will flip horizontally.                     |
| Flip Vertical       | Flips the currently selected image vertically. If “Apply-All” is  selected, then all images will flip vertically.                         |

CT Presets Menu

| **Menu Option**   | **Description**                                                                                                                                                                  |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Abdomen           | Sets the currently selected window/level values such that they can view the abdomen. If “Apply-All” is selected, then all images will change to the same window/level value.     |
| Bone              | Sets the currently selected window/level values such that they can view bone. If “Apply-All” is selected, then all images will change to the same window/level value.            |
| Disk              | Sets the currently selected window/level values such that they can view disk. If “Apply-All” is selected, then all images will change to the same window/level value.            |
| Head              | Sets the currently selected window/level values such that they can view the head. If “Apply-All” is selected, then all images will change to the same window/level value.        |
| Lung              | Sets the currently selected window/level values such that they can view the lungs. If “Apply-All” is selected, then all images will change to the same window/level value.       |
| Mediastinum       | Sets the currently selected window/level values such that they can view the mediastinum. If “Apply-All” is selected, then all images will change to the same window/level value. |

View Info Menu

| **Menu Option**            | **Description**                                                                                                                                                  |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Image Info                 | Displays information about the image, including the patient name, ID, number of pages in the image, the page dimensions, bit depth, and file format information. |
| DICOM Header               | Displays the DICOM Header associated with the image (if it is available).                                                                                        |
| Radiology Image Info       | Displays information from the header of the image including the modality, series and image numbers.                                                              |
| Image Information Advanced | Displays the Image Information/properties window.                                                                                                                |

FullRes Menu

| **Menu Option**   | **Description**                                                                                                                                                                                                                                                                  |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| View              | If the original full quality image is available for the down- sampled image being displayed the FullRes menu option is available.  When you click  **View**  from the menu option the original image in full quality is requested, cached on the workstation and then displayed. |

Note:

VistA Imaging stores images from the DICOM Gateway. In many cases a down-sampled version of the image is stored to make it load faster and the original image is saved in full quality. This down-sampled image is lower in quality than the original and is used by Clinical Display (not VistARad).

Most radiology images have a down-sampled image. CT, MR, RF, US images usually do NOT have a down-sampled and the full quality image is stored. The decision to create a down-sampled image is configurable on the DICOM Gateway and is based on the modality.

When the Radiology Viewer loads an image, it determines if it has loaded the full quality image or a down-sampled/compressed image. If the image is down-sampled/compressed, a message below the image and in the title bar indicates the image is not full quality and the menu option is available. If the image displayed is full quality, the warnings are hidden and the menu option is disabled. When a user selects to view the full resolution image, the client requests the image. This might take a few minutes (depending on where it is coming from). Once the image is retrieved, it is displayed in the viewer (and cached on the workstation). If there is an error retrieving the image, the error is displayed.

View Settings Menu

| **Menu Option**   | **Description**                                                                                                          |
|-------------------|--------------------------------------------------------------------------------------------------------------------------|
| 1x1 Stack         | Puts the viewer into a single image stack mode.                                                                          |
| 2x1 Stack         | Puts the viewer into a dual stack mode where two images from different (or the same) studies can be viewed and compared. |
| 3x2 Layout        | Puts the viewer into a layout mode where 6 images are displayed at once.                                                 |
| 4x3 Layout        | Puts the viewer into a layout mode where 12 images are displayed at once.                                                |

Options Menu

| **Menu Option**   | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Stack View        | Stack View has the following options:  - Page Together - When selected, two stack views will page together. This does not guarantee they will always be on the same image number, but as one stack changes images, the other stack will follow. - Page With Different Settings - When selected, each stack will page with the settings held from the previous image in that stack. - Page With Same Settings - When selected, each stack will page with the settings from the stack that changed images.  If the left stack changes images, both stacks will change |

| **Menu Option**     | **Description**                                                                                                                                                                                                                                                                                                                                                     |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                     | images and then set their view settings (window/level, zoom, etc.) to the same as the left stack.  - Page With Image Settings - When selected, each image will automatically set itself based on the contents of the image. It does not matter what the previous image had set.                                                                                     |
| Layout View         | Layout View has the following options:  - Use Selected Window Settings - When selected and the user changes images; the next image loaded will use the same settings as the previous image. - Use Individual Settings – When selected, each image will automatically set itself based on the contents of the image. It does not matter what the previous image had. |
| Image Settings      | Image Settings has the following options:  - Use Device Window Level if Available - When selected, the image will be automatically window leveled using values specified in the DICOM header (if available). - Use Histogram for Window Level - When selected the image will be window leveled using the contents of the image.                                     |
| Mouse Magnify Shape | You have the option to use a Magnifying glass, which will magnify the selected portion directly on the image where the cursor is placed, as in the picture below.  Mouse Magnify Shape has the following options:  - Circle - Rectangle                                                                                                                             |
| Labels On           | If selected, then the orientation labels are displayed on the image (always on the middle left side of the image).                                                                                                                                                                                                                                                  |

Tools Menu

| **Menu Option**   | **Description**                                                                                                                                                                                         |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cine Tool         | Displays the cine tool dialog to allow moving between frames in a single image.                                                                                                                         |
| Cine Tool Focus   | Sets the focus to the cine tool dialog.                                                                                                                                                                 |
| Pixel Values      | When selected, if you select on an image, the hint will change to the value of the pixel at the location clicked. If not selected, then the hint will contain series and study description information. |

Scout Menu

| **Menu Option**           | **Description**                                                                                                                                                                                                                                                                                                                                 |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Display Scout Lines       | When the option is selected, information for scout lines is automatically loaded and scout lines are displayed.  Turning the Display Scout Lines option off enables you to conserve resources if loading all the images in the series is slow and if you do need Clinical Display to open scout images in the Scout window automatically.       |
| Auto Detect Scout Images  | When the option is selected, if a CT study is selected the Radiology Viewer will automatically detect Scout images and open them in the Scout window.  When the  **Auto Detect Scout Images**  option is turned off, you can put a scout image in the Scout window by selecting the image and then the option  **Add Image to Scout Window**  . |
| Scout Line Color          | This option lets you define the color of the scout line in the Scout window by choosing one of the available colors:  **Red**  ,  **Blue**  ,  **Green**  , or  **Yellow**  .                                                                                                                                                                   |
| Show Scout Window         | Opens the Scout window when the window is not displayed.                                                                                                                                                                                                                                                                                        |
| Add Image to Scout Window | Puts the selected image in the Scout window.                                                                                                                                                                                                                                                                                                    |

Help Menu

| **Menu Option**   | **Description**                                                            |
|-------------------|----------------------------------------------------------------------------|
| Radiology Viewer  | Displays help contents for the Radiology Viewer.                           |
| ImageGear Version | Version of the ImageGear software included in the Clinical Display client. |

***Popup Menu in the Group Abstracts Window***

You can right click a DICOM image and open it in a second Radiology window to compare it with a study image that is already open.

| Open Image in 2nd Radiology Window   | <!-- image -->  The image is opened in a side-by-side view next to the first DICOM image.   |
|--------------------------------------|---------------------------------------------------------------------------------------------|

***Toolbar in the Stack View Slide***

The Stack View Slide toolbar is enabled when a study of more than one image is selected and shown in the stack view. This tool enables you to scroll through the stack and adjust the playing speed.

| <!-- image -->   | To the left of the study are buttons that allow navigating through the images in the study.  <!-- image -->  Click the  **First Image in Study button**  button to go to the first image in the study.  <!-- image -->  Click the  **List Images In**  button   button to go to the last image in the study.  <!-- image -->  Click  **Previous Study button**  the    button to go to the previous image in the study.  <!-- image -->  Click the  **Next Study Image**  button    button to go to the next image in the study.  Below the buttons is a study slider that shows the position of the image in the current study. The user can move the slider in order to view another image  The button below the slider allows the user to play the images in the study (in a loop).When the user clicks the play button it will change to a stop button to allow the user to stop the scrolling of images.  Below the button is another slider that controls the speed of the loop.   |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| <!-- image -->   | If you right mouse select the study slider a menu opens which allows you to adjust the range parameters.  Range Start: Set the range of the loop to start at the currently selected image.  Range End: Set the range of the loop to end at the currently selected image.  Range Clear: Clear the range of images to scroll.  Start: Start the looping (same as clicking the play button). Stop: Stop the looping (same as clicking the stop button).   |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <!-- image -->   | This label shows:  the current image in the study (on the left),  the description of the image and bit depth, width and height of the image                                                                                                                                                                                                                                                                                                            |

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

***Toolbar in the Radiology Viewer***

<!-- image -->

The Radiology Viewer has two toolbars used to manipulate the images to study them.

| <!-- image -->                   |                                                                                                                     |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Apply Actions to All Images      | Applies selected actions to all visible images.                                                                     |
| Reset Image to original setting. | Resets the currently selected image to its original display settings including zoom, window/level, and orientation. |
| Fit Image in Window              | Resizes image to fit to the window size.                                                                            |
| Fit the Image Height             | Resizes image to fit to the height of the window size.                                                              |
| Fit the Image Width.             | Resizes image to fit to the width of the window size.                                                               |
| Actual Size                      | Resets the image to the actual size.                                                                                |
| Flip Vertical                    | Flips the image vertically.                                                                                         |

| Flip Horizontal                   | Flips the image horizontally.                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rotate Left (counter  -clockwise) | Rotates the image counter clockwise.                                                                                                                                                                                                                                                                                                                                                                                                |
| Rotate right (clockwise)          | Rotates the image clockwise.                                                                                                                                                                                                                                                                                                                                                                                                        |
| <!-- image -->  Invert Image      | Inverts the image.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Color Channel (all channels)      | Cycles through the color channels of a 24-bit image.  The view of the button changes depending on the channel displayed.  <!-- image -->  – View of the Color Channel button showing all channels  <!-- image -->  – View of the Color Channel button showing the red channel  <!-- image -->  – View of the Color Channel button showing the green channel  – View of the Color Channel button showing the blue channel            |
| Pan Image with mouse              | Positions the cursor in the middle of this window.  Select and hold down the left mouse button. The cursor will appear as a  “hand”.  When the cursor (“hand”) is moved up and down the middle of the window, the document will move upwards and downwards. Using this technique, you will be able to view all portions of the document image.  Close the Document Image Window by selecting the “X” in the top right  hand corner. |
| Mouse Magnifier                   | Mouse pointer magnifier.                                                                                                                                                                                                                                                                                                                                                                                                            |
| Zoom in on Selected Area          | Zoom button.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Auto Window/Level                 | Auto Window Level control.                                                                                                                                                                                                                                                                                                                                                                                                          |
| Open a Pan Window                 | Opens a Pan Window.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <!-- image -->                    |                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Copy to clipboard                 | Copies the image to a clipboard.                                                                                                                                                                                                                                                                                                                                                                                                    |

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

| Print Image              | Prints the image.                                        |
|--------------------------|----------------------------------------------------------|
| Image Report             | Opens the Image Report for the selected image.           |
|                          |                                                          |
| Win -Change Window Value | Adjusts the brightness and contrast at the window level. |
| Lev- Change Level Value  | Adjusts the brightness and contrast at the image level.  |
| Zoom                     | Increases or decreases the zoom.                         |

<!-- image -->

<!-- image -->

<!-- image -->

***DICOM Multi-frame Cine Viewer***

The DICOM Multi-frame Cine Viewer is a type of Radiology Viewer and is used to display multi-frame images that are DICOM and TGA images only. When they are selected in the Radiology Viewer, the DICOM Multi-frame Cine View window automatically opens.

**Note** : You can also open this dialog box by choosing Tools | Cine Tool from the Radiology Viewer menu.

<!-- image -->

| **Field or Button**   | **Description**                                                                       |
|-----------------------|---------------------------------------------------------------------------------------|
| Cine                  | Plays the study from the current page and speed setting.                              |
| Stop                  | Stops the playing of the study.                                                       |
| Reset                 | Returns the study to the first page.                                                  |
| Play Mode (Play once) | Plays the study once.                                                                 |
| Play Mode (Repeat)    | Repeats the playing of the study as if in a play loop.                                |
| Page slider           | Moving the slider left to right and back will move through the pages of the study.    |
| Cine Speed slider     | Controls the playing speed, the slider is moved to left to right to adjust the speed. |
| Previous Page         | Selecting this button moved the slider and displays the previous page of the study.   |
| Next Page             | Selecting this button moved the slider and displays the next page of the study.       |

**Video Player**

Motion video files can be saved as part of the patient record using VistA Imaging. When a selected patient image is a motion video clip, the Video Player window is opened. User preferences can also be set to view video using an alternate viewer.

<!-- image -->

- Use the toolbar buttons to play, pause, stop and rewind.
- Use the slider bar to browse the video clip, frame by frame.
- "Start" and "end" points can be set.
- Select "video loop" mode to continuously play all or part of the file.

The Video Play can be displayed in two ways depending on the user preferences that you have selected:

- Without the progress bar and sliders, as shown:
<!-- image -->
- With the progress bar and sliders, as shown:
<!-- image -->

***Menu Bar in the Video Player***

##### File Menu

| **Menu Option**   | **Description**                                |
|-------------------|------------------------------------------------|
| Image Report      | Opens the Image Report for the selected image. |
| Exit              | Will close the Video Player window.            |

**Options Menu**

| **Menu Option**      | **Description**                                                             |
|----------------------|-----------------------------------------------------------------------------|
| Show Progress bar    | Show or hide the progress bar.                                              |
| Increment in Seconds | Changes the progress bar to increment by seconds.                           |
| Increment in Frames  | Changes the progress bar to increment by frames.                            |
| Video Loop           | Replays the video in a continuous loop.                                     |
| Stay on Top          | Keeps the Video Player open on top of the active windows.                   |
| Speed                | Option is enabled if the progress bar is shown.  - Slow - Medium and - Fast |

##### View Menu

| **Menu Option**   | **Description**                                                                                                                                                                                     |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Zoom Out          | Decreases the size of the window.                                                                                                                                                                   |
| Zoom In           | Increases the size of the window.                                                                                                                                                                   |
| Default           | Resets the size of the display to the default (original).  **Note**  : the default size is the best size for picture quality.                                                                       |
| Start Set Point   | Sets the Start Point at different places in the video will select a region of the video clip. When a region is selected, only that part of the video clip will be shown, when you 'play' the video. |
| Set End Point     | Sets the End Point at different places in the video will select a region of the video clip. When a region is selected, only that part of the video clip will be shown, when you 'play' the video.   |
| Clear Start/End   | Clears the selected region is played.                                                                                                                                                               |

**Actions Menu**

| Menu Option   | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| Play          | Will start the video in motion from the current position of the slider bar. |
| Stop          | Will stop the video.                                                        |
| Rewind        | Rewind the video clip to the beginning.                                     |

##### Help Menu

| Menu Option         | Description                            |
|---------------------|----------------------------------------|
| Video Player window | Displays the online Video Player help. |

<!-- image -->

***Toolbar in the Video Player***

| <!-- image -->                     |                                                                                                                                                                                                                                                                                                                      |
|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Play                               | Starts the video in motion from the current position of the slider bar.                                                                                                                                                                                                                                              |
| <!-- image -->  Pause              | Pauses the video.                                                                                                                                                                                                                                                                                                    |
| <!-- image -->  Stop               | **S**  tops the video.                                                                                                                                                                                                                                                                                               |
| <!-- image -->  Rewind             | **R**  ewinds the video clip to the beginning.                                                                                                                                                                                                                                                                       |
| <!-- image -->  Progress Bar       | Shows the video length and current position.  When the Progress Bar is active, the video might seem a little "choppy" or "hesitant"; this is because extra processing is needed to synchronize the control with the current frame of the video clip.  Use the Progress Bar to browse the video clip, frame by frame. |
| Fast Forward                       | Move forward in the video. This is only available if the progress bars and sliders are not selected.                                                                                                                                                                                                                 |
| One Frame Forward                  | Move one frame forward. This is only available if the progress bars and sliders are not selected.                                                                                                                                                                                                                    |
| <!-- image -->  One Frame Backward | Move one frame back. This is only available if the progress bars and sliders are not selected.                                                                                                                                                                                                                       |

<!-- image -->

**Note** : The user preference for showing the progress bar is selected and shown in this view of the toolbar.

***Popup Menu in the Video Player***

Right-clicking in the Video Player opens a popup menu providing shortcuts to options and actions you can perform.

<!-- image -->

| **Menu Option**   | **Description**                                                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Image Report      | Opens the Image Report for the selected image.                                                                                                        |
| Set Start Point   | Sets the start point at a location to begin the video clip. When you set the start point, the video begins at that point when you click Play.         |
| Set End Point     | Sets the end point at a location to stop the video clip. When you set the end point, the video runs and then stops at that point when you click Play. |
| Clear Start/End   | Clears the selected region.                                                                                                                           |
| Video Loop        | Sets the continuous play of the whole video clip, or the selected portion.                                                                            |
| Goto Main Menu    | Changes the application focus to the Main Imaging Display window.                                                                                     |

**MUSE EKG**

The VistA Imaging System can interface with the GE/Marquette MUSE EKG Management system. When an Imaging/MUSE interface is active, EKGs are viewable from any VistA Imaging workstation using the EKG Display window. The VistA Imaging Display application can also be configured to show the EKGs for a patient automatically whenever a patient is selected. This is done through the Options | User Preferences menu.

<!-- image -->

On the Clinical Display main window or in the Image List window, click the Open the MUSE EKG viewing window button  to open the MUSE EKG window.

Starting with Clinical Display Patch 167, the Display Client interfaces with the GE MUSE Systems using the GE MUSE API 3. This version of the MUSE Patient Study Viewer will connect to MUSE Systems that are running MUSE v8 SP2 and later. The electrocardiograms (EKGs) and other data types displayed in this viewer are MUSE generated Portable Document Format (PDF) images of the patient tests.

The new window is a copy of the Full resolution window modified to work with images that are not referenced in the IMAGE File (#2005). The functionality of the toolbar buttons and the image viewer is the same as in the Full Resolution Viewer. The images displayed in this viewer are MUSE generated PDF images of the patient tests.

***MUSE EKG Viewer***

1. If you are connecting to multiple MUSE Systems, the number of studies from each MUSE system is displayed in this panel. Clicking on the panel will display connection information about each system.
2. Click “Size” to increase/decrease the height of the list. Click “List” to show/hide the list of

studies.

1. The MUSE study data is displayed on the header panel of each image. The overlay function is no longer available.
2. If the study is not confirmed, then “UNCONFIRMED” is displayed in a second header panel. The overlay of “UNCONFIRMED” is no longer available.

***EKG List***

<!-- image -->

<!-- image -->

| Columns   | Columns                                                                                                                                                                                                         |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| #         | Incremental number of each study loaded.                                                                                                                                                                        |
| Test Type | ECG, Stress, Holter, etc.                                                                                                                                                                                       |
| Date/Time | The date /time the test was administered.                                                                                                                                                                       |
| Site      | Each MUSE Site is defined in the NETWORK LOCATIONS File (#2005.2). In that File, a field named 'Site' is a free text field. A descriptive text can be entered to tell the users which site the EKG Study is on. |
| Conf      | Confirmed or UnConfirmed.                                                                                                                                                                                       |

**Note:** Studies may be sorted by selecting the head of the column in the study dropdown. Selecting the column again will resort that column in reverse order. The study list also contains a column indicating whether an EKG has been confirmed or not. In addition, EKGs that have been automatically interpreted by the MUSE server, but have not been confirmed by a cardiologist, have an UNCONFIRMED header at the top of the EKG report.

***Menu Bar in the MUSE EKG Viewer***

File Menu

| **Menu Option**          | **Description**                                                                                                                                                                                                                                                                                                                                                              |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Copy Image to Clipboard  | Copies the selected image to the Clipboard. See Printing and Copying Images for details.                                                                                                                                                                                                                                                                                     |
| Print Selected Image     | Prints the selected image. See Printing and Copying Images for details.                                                                                                                                                                                                                                                                                                      |
| Print Options            | Opens the Image Print Options window. Users can select more than one EKG study and print them all at one time. The Popup Menu has a Print Selected Images… option which will open the Printer Dialog window. The user can select a printer and click “OK.” Selecting the File &#124; Print Selected Images… option will also print the images selected in the EKG Test List. |
| Close Selected Image     | Closes the selected image. If a duplicate was made of the image the duplicate will remain open.                                                                                                                                                                                                                                                                              |
| Close All Images         | Closes all of the images in the MUSE EKG Display Viewer                                                                                                                                                                                                                                                                                                                      |
| Open In Alternate Viewer | Opens the selected EKG Study in the PDF Alternate Viewer.                                                                                                                                                                                                                                                                                                                    |
| Exit                     | Exit the MUSE EKG Display                                                                                                                                                                                                                                                                                                                                                    |

##### Options Menu

| **Menu Option**   | **Description**                                                                                                                                             |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Show Messages     | Open a message list area at the bottom of the window. The list of messages is a list of all HTTP messages sent, and the Status and Status message received. |
| Show List         | Show or Hide the list of Patient Studies.                                                                                                                   |

| **Menu Option**                                                                                                                                                                                     | **Description**                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Change List Size                                                                                                                                                                                    | The size of the List of Patient Studies will cycle through the small, medium and large sizes.                                                 |
| Show Format Table                                                                                                                                                                                   | The list of MUSE FORMAT TABLE entries will be displayed. The list will include the default Format IDs and any entries made at the VistA Site. |
| Grid On                                                                                                                                                                                             | Allows user to turn the grid on or off.                                                                                                       |
| If the user has the MAG System Security Key and has set MUSE DEBUG=TRUE in the MAG.INI file, then the 'Debug' menu item will be visible, and the following:  Debug Sub-Menu items will be available |                                                                                                                                               |
| Close all Connection(s)                                                                                                                                                                             | Connections to all MUSE Server will be closed.                                                                                                |
| Open all Connection(s)                                                                                                                                                                              | Connections to all MUSE Servers will be attempted.                                                                                            |
| Get Patient Tests                                                                                                                                                                                   | Retrieve a listing of all Patient Studies from all Connected MUSE Systems.                                                                    |
| Show Debug Window                                                                                                                                                                                   | See MUSE Debug window section.                                                                                                                |

<!-- image -->

A new menu option, Grid On, has been added to the Options menu of the MUSE EKG Clinical Display window. The menu option will default to being checked when the window is opened.

When the Grid On option is checked (image above) the test generated, by the MUSE system, will include a grid. When Grid On is unchecked, the test generated by the MUSE system will not include a grid.

## MUSE Test Type and Format ID Mapping

<!-- image -->

To display the MUSE Format Table, open the MUSE EKG Display viewer and Select the menu: Options | Show Format Table. The MUSE Format Table window will be displayed and the default mappings will be listed.

<!-- image -->

##### Default mapping:

**MUSE Format Table Columns:**

Site:

- The MUSE System entry in the NETWORK LOCATION File.
- “All Sites” means the default mapping for all MUSE Systems.
- “All Sites” is not an entry in the NETWORK LOCATION File. (Internal Entry Number) IEN:
- The Internal Entry Number is for the NETWORK LOCATION entry.
- '0' means the default mapping is for all MUSE Systems. Test Type:
- This field can be modified by the user. Grid:
- Enter 'Yes' if a Grid is displayed, 'No' if a Grid is not displayed. Format ID:
- Enter the new Format ID Number for the Test Type.

**Format Table Defaults**

<!-- image -->

This table is a representation of the data in the MUSE FORMAT TABLE File #2006.172. It is a mapping of MUSE Test Types to the MUSE Format ID number for a specified MUSE System. The default Format IDs listed below are used by the MUSE System to compile the MUSE Test data, for the specified Test Type, into a PDF File for viewing. The default Format IDs cannot be modified. Sites can add entries to this file to override any of the default mappings if needed. If the MUSE Format IDs are not correct for a certain MUSE System, a site specific Format IDs can be entered into the MUSE FORMAT TABLE, those Format IDs will override the defaults. Open the MUSE EKG Display window, and select the menu: Options | Show Format Table to see the MUSE Format Table. Below is an example of the MUSE Format Table with only the default mappings:

The default mappings listed above may not be correct for all MUSE Systems. If this is the case the user will need to override the default mapping for that MUSE System.

Example: Table MUSE A below is a screen shot of a MUSE System that has the default mappings.

<!-- image -->

(Table MUSE A)

Example: Table MUSE B below is a screen shot of a MUSE System that has different Format ID's than the defaults. Notice in MUSE B below, the Format ID's for VistA ECG, VistA HiRes, VistA Stress and VistA Holter are different than the defaults in MUSE A.

<!-- image -->

(Table MUSE B)

The site will have to override the Default Format IDs, and map the four 'VistA…' entries to the

Format IDs that are on their system

### Override a Default Format ID

To override a default Format ID, the user will need to make an entry into the MUSE FORMAT TABLE #2006.172 File.

Use FileMan Enter/Edit option to add a new entry to the file.

The highlight content below is the information the user will been to update: Example:

SLC&gt;D P^DI

VA FileMan 22.2

Select Option: ENTER OR EDIT FILE ENTRIES

Input to what File: MUSE FORMAT TABLE// (0 entries) EDIT WHICH FIELD: ALL//

Select MUSE FORMAT TABLE DESCRIPTION: ZZZ MUSE VistA ECG

Are you adding 'ZZZ MUSE VistA ECG' as

a new MUSE FORMAT TABLE (the 1ST)? No// y (Yes) NETWORK LOCATION: ZZZ MUSE SYS

TEST TYPE: RestingECG GRID: N NO

FORMAT ID NUMBER: 11

Select MUSE FORMAT TABLE DESCRIPTION:

<!-- image -->

After all four overrides have been entered; Open the MUSE Format Table to verify the change

In the table above, the entry for the following has a Format ID of 11. Site : ZZZ MUSE SYS

Test Type: RestingECG Grid: NO

This Format ID of 11 for ‘RestingECG’.

### Verify the new Format ID.

To determine what Format ID was used to generate the MUSE Test Image, click on a Test in the list. After the Test is displayed, check the menu: Options | Show Messages.

A message area will display at the bottom of the window.

Scroll to the bottom of the messages, then scroll up until you see 'Format ID = nn' That will be the Format ID that used to generate the Test.

<!-- image -->

Example of the message panel in the VistA Imaging MUSE EKG Viewer

### Add a New Test Type

If a new Test Type is added to the MUSE System, the VistA Imaging MUSE EKG Viewer will use the Format ID =1 to display Tests of that Type. Format ID 1, is a general format that is used when the Test Type is unknown to the VistA Imaging EKG Viewer.

To specify a specific Format ID for the new Test Type, Use FileMan to:

1. Enter the Test Type into the MUSE TEST TYPES File #2006.171
2. Enter a mapping of Test Type and Format ID into the MUSE FORMAT TABLE File #2006.172

### MUSE Debug

If a site is reporting issues with the MUSE EKG Display window, support personnel and the Imaging Site manager can use the Debug window to display the full HTTP Request and Response for the last five items.

Repeating the steps to reproduce the issue with the Debug window open will help support personnel to find the issue.

The top two panels are the request and response in Extensible Markup Language (XML) format. The bottom two panels are the request and response, in a Tree view format.

<!-- image -->

Image Menu

| **Menu Option**   | **Description**                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Apply to All      | When selected, all of the images opened in the MUSE EKG Display Viewer will have all actions applied to them from the Image Menu options.                                                                                                                                                                                                                                                   |
| Zoom              | Zoom has the following options:  - Zooms In - to zoom in to an image - Zoom Out - to zoom out of an image - Fit to Width - to fit the image to the window width (horizontal) - Fit to Height - to fit the image to the height of the window (vertical) - Fit to Window - to fit the image to the entire window (vertical and horizontal) - Actual Size - to show image in its original size |
| Mouse             | Mouse has the following options:  - Pan - to pan image by dragging mouse - Magnify - to magnify an image where the mouse is clicked - Zoom - to zoom into an area of the image selected with the mouse - Pointer - to go back to mouse pointer                                                                                                                                              |
| Rotate            | Rotate has the following options:  - Right - Rotates the image 90 degrees clockwise - Left - Rotates the image 90 degrees counterclockwise - 180 - Rotates the image 180 degrees - Flip Horizontal - Flips the image horizontally - Flip Vertical - Flips the image vertically                                                                                                              |
| Reset             | Resets the currently selected image to its original display settings including zoom, contrast, window brightness, and orientation.                                                                                                                                                                                                                                                          |

| **Menu Option**   | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Scroll            | Scroll has the following options:  - Top Left - scroll to the top left corner of the image - Top Right - scroll to the top right corner of the image - Bottom Left - scroll to the bottom left corner of the image - Bottom Right - scroll to the bottom right corner of the image - Left - scroll to the left - Right - scroll to the right - Up - scroll up - Down - scroll down ##### View Menu Menu Option Description Viewer Settings Enables you to set default values for the number of rows and columns, and the maximum number of images to display in the viewer. Refresh Refreshed the current view in the MUSE EKG Display Viewer. Realign Images Realigns the images that are in the MUSE EKG Display Viewer. Lock Image Size Locks the image size while it is being viewed. Toolbar Displays the toolbar. Show Hints Displays Hints when the cursor is over a control in VistA Imaging. GoTo Main Menu Displays the VistA Imaging Display main window. Active windows Displays the active windows currently open in VistA Imaging Display. **Layout Menu** Menu Option Description Tile All Images are resized and are positioned in the viewer as tiles. Default Layout Restores the default layout. Next Viewer Page Displays the next page of images. (This menu option is enabled only when there is more than one page of images.) Prev Viewer Page Displays the previous page of images. (This menu option is enabled only when there is more than one page of images.) Menu Option Description   Enable the user to customize the number and position of images in the window. ##### Page Menu This Page Menu is only enabled when a multiple page image is selected. Menu Option Description First Go to the first page of the image. Previous Go to the previous page of the image. Next Go to the Next page of the image. Last Go to the last page of the image. ##### Help Menu Menu Option Description MUSE ECG Display Displays information about the current MUSE EKG Display window. ***Toolbar in the MUSE EKG Viewer*** The Toolbars in the MUSE EKG Viewer are the same as the Full Resolution Viewer. There are three toolbars. The toolbars can be dragged and dropped in the viewer to place them side-by- side, two across and one down, or stacked three high. Using the buttons on the three toolbars, you can manipulate the image and navigate around the MUSE EKG Viewer. The MUSE EKG Viewer only lists the MUSE generated PDF images from the patient tests. Some of the tool buttons will not be enabled or will not function on PDF images. Each toolbar is shown below with a description of each button in the toolbar.     Apply Actions to all Images Applies the actions to all images. Fit Image in Window Resizes the image to fit in the viewing window. Fit to Width Fits the image to the width of the viewing window. Zoom In When selected, the image will magnify each time the button is clicked. Zoom Out When selected, the image magnification will reduce each time the button is selected. Mouse Magnifier When button is clicked, you use your mouse and scroll on the image and the area on the image is magnified. Zoom in on Selected Area You select this option and set a point on the image. The image point selected zooms in or out with the movement of the mouse. Pan Image with Mouse With the mouse a user clicks on the image and the image scrolls with the mouse movement. Mouse Pointer Changes the mouse back to a pointing device. Maximize Image Button enables you to specify the image size and layout. A drop down list appears when selected with options for you to select. Tile all Images Images are resized and are positioned in the viewer as tiles. Rotate Counter Clockwise 90 Rotates the Image 90 degrees counterclockwise each time the button is clicked. Rotate Clockwise 90 Rotates the Image 90 degrees clockwise each time the button is clicked.     Refresh Images Refreshes the images. Remove Selected Image(s)(Not a Delete)) Removes only the selected images from the MUSE EKG Display Viewer pane. Remove All Images (Not a Delete)) Removes all of the images from MUSE EKG Display Viewer pane. Image Report + Print Copy Menu In the drop down menu there are three options to: Copy Image, Print Image, and Image Report. Goto First Page Go to the first page of a multi-page image. Goto Previous Page Go to the previous page of a multi-page image. Goto Next Page Go to the next page of a multi-page image. GoTo Last Page Go to the last page of a multi-page image. Reset Image Resets the currently selected image to its original display settings including zoom, contrast, window brightness, and orientation. Resets the currently selected image to its original display settings including zoom, contrast, window brightness, and orientation.           Magnification: Use the scroll bar to increase or decrease magnification. |
| Maximize Image    | Enable image to fill the entire window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Previous Image    | Displays the previous image.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Next Image        | Displays the next image.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## XML Documents

<!-- image -->

The VistA Imaging System lets you store and display XML documents that contain Clinical Document Architecture (CDA) information. The CDA information in the XML document is displayed with a style sheet that is distributed with the patch and installed on the workstation. When you select the XML document, it opens in an Internet Explorer browser window using the style sheet.

**Note** : As of Aug. 2013, this functionality is used primarily in Indian Health Service (IHS) sites.

<!-- image -->

## Using Scout Lines

<!-- image -->

You can view scout lines for localizer images and navigate through a stack of cross-sectional CT or MR images in the Radiology viewer of Clinical Display and the Scout window, associated with this viewer. Clinical Display generates the scout lines dynamically on the scout image enabling clinicians to display specific cross-sectional images in the Radiology viewer by clicking the appropriate scout line in the localizer image.

The ability to view scout lines and scout images in Clinical Display enables clinicians to view scout images and scout lines in Clinical Display without having to use a dedicated radiology application such as VistARad.

### Overview of Scout Images and Scout Lines

A *scout line* is a perpendicular line that can be displayed on a sagittal image wherever there is also a corresponding axial image of the same part of the body.

*Localizer images* , also called *scout images* , are used in MR and CT studies to identify the relative anatomical position of a collection of cross-sectional images. A localizer can be acquired as a separate image, as is often done for CTs, or it can be dynamically generated, as is done for MRs. In a scout image, scout or reference lines indicate the position of each cross-sectional image.

Using scout lines enables clinicians to display the sagittal and axial images simultaneously from the same study; one containing a scout line perpendicular to the area being studied, and the other image displaying a cross-sectional view of the same area. The scout line lets clinicians determine the specific area they are viewing in the axial image. This is needed because, for example, it is nearly impossible to distinguish between the axial views of any of the lumbar vertebrae without using a scout line. The ability to use scout lines in Clinical Display helps clinicians to make more accurate diagnoses.

### Displaying Scout Images and Scout Lines

You can view scout lines for localizer images and navigate through a stack of cross-sectional CT or MR images in Clinical Display and the Scout window.

When you click a scout image in the Abstracts window, if the image is CT image and if the option to display scout lines is selected, the image opens in the Scout window and the corresponding cross-sectional image from the series opens in the Radiology viewer.

<!-- image -->

If the image is an MR image, it opens in the Radiology viewer. If it is a scout image, the Scout menu is available and you can place the image in the Scout window by choosing **Scout | Add Image to Scout Window** .

<!-- image -->

When you navigate through the stack of images in the series using the arrow buttons in the Radiology viewer, the scout line on the localizer image in the Scout window shifts to show the position of the cross-section.

When you click in the Scout window, the scout line shifts and the image in the Radiology viewer changes to show the relevant cross-section.

**Menu Bar in the Scout Window**

File Menu

| **Menu Option**   | **Description**                                |
|-------------------|------------------------------------------------|
| Report            | Displays the report associated with the image. |
| Close             | Closes the Radiology Viewer.                   |

Image Menu

| **Menu Option**   | **Description**                                                                                                                                                           |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Zoom              | Adjusts the magnification of the image in the window according to the selected option:  - Zoom In - Zoom Out - Fit to Width - Fit to Height - Fit to Window - Actual Size |

| **Menu Option**   | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Mouse             | Performs one of the following tasks by selecting one of the available mouse options:  - Pan – Selecting this option displays a Pan tool that enables you to pan to different areas of the image. - Magnify – Selecting this option displays a Magnifier tool that enables you to magnify areas of the image - Zoom – Selecting this option displays a Zoom tool that enables you to draw an area on the image and zoom into it. - Annotations – Selecting this option displays the Annotation Toolbar - Auto Window/Level – Selecting this option displays a tool that allows you to adjust the levels of the image. |
| Window/Level      | Adjusts the contrast and brightness of the image in the window by selecting one of the following options:  - Window + – Increases the contrast of the image. - Window – –Decreases the contrast of the image. - Level + – Increases the brightness of the image. - Level – –Decreases the brightness of the image.                                                                                                                                                                                                                                                                                                   |
| Invert (Reverse)  | Inverts the colors of the image in the window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Reset Image       | Resets the currently selected image to its original display settings including zoom, window/level, and orientation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Scroll            | Scroll has the following options:  - Top Left – Scroll to the top left corner of the image. - Top Right – Scroll to the top right corner of the image. - Bottom Left – Scroll to the bottom left corner of the image. - Bottom Right – Scroll to the bottom right corner of the image. - Left – Scroll to the left. - Right – Scroll to the right. - Up – Scroll up. - Down – Scroll down.                                                                                                                                                                                                                           |
| First Image       | Moves to the first image in the study.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Previous Image    | Moves to the first image in the study.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Next Image        | Moves to the next image in the study.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Last Image        | Moves to the last image in the study.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

View Menu

| **Menu Option**   | **Description**                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Pan               | Display the Pan window that shows the area of the image displayed in the Scout window. |

| **Menu Option**   | **Description**                                                 |
|-------------------|-----------------------------------------------------------------|
| Go To Main Window | Changes the focus to the Clinical Display main window.          |
| Active windows    | Displays the active windows currently open in Clinical Display. |

Rotate Menu

| **Menu Option**     | **Description**                                                                  |
|---------------------|----------------------------------------------------------------------------------|
| Rotate Clockwise 90 | Rotates the currently selected image clockwise (to the right) 90 degrees.        |
| Rotate Minus 90     | Rotates the currently selected image counter clockwise (to the left) 90 degrees. |
| Rotate 180          | Rotates the currently selected image 180 degrees.                                |
| Flip Horizontal     | Flips the currently selected image horizontally.                                 |
| Flip Vertical       | Flips the currently selected image vertically.                                   |

CT Presets Menu

| **Menu Option**   | **Description**                                                                          |
|-------------------|------------------------------------------------------------------------------------------|
| Abdomen           | Sets the currently selected window/level values such that they can view the abdomen.     |
| Bone              | Sets the currently selected window/level values such that they can view bone.            |
| Disk              | Sets the currently selected window/level values such that they can view disk.            |
| Head              | Sets the currently selected window/level values such that they can view the head.        |
| Lung              | Sets the currently selected window/level values such that they can view the lungs.       |
| Mediastinum       | Sets the currently selected window/level values such that they can view the mediastinum. |

ViewInfo Menu

| **Menu Option**   | **Description**                                                                                                                                                                      |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Image Info        | Displays information about the image in the Scout window, including the patient name, ID, number of pages in the image, the page dimensions, bit depth, and file format information. |
| DICOM Header      | Displays the DICOM Header associated with the image in the Scout window (if the DICOM Header is available).                                                                          |

| **Menu Option**            | **Description**                                                                                                                                                                       |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Radiology Image Info       | Displays information from the header of the image including the modality, series and image numbers.                                                                                   |
| Image Information Advanced | Displays the Image Information/properties window with detailed information about the image displayed in the Scout window, including information about the series to which it belongs. |

Options Menu

| **Menu Option**     | **Description**                                                                                                                                                                                         |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Mouse Magnify Shape | Selects the shape of the mouse tool used to select the area of the image that is magnified when you choose  **Image &#124; Mouse &#124; Magnify**  . The options are  **Circle**  and  **Rectangle**  . |

Scout Menu

| **Menu Option**                | **Description**                                                                                                                                            |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Remove Image from Scout Window | Removes the image from the Scout window. This option is useful when you want to remove the image from the Scout window because the wrong one is displayed. |
| Scout Line Color               | Sets the color of the scout line. The options are  **Red, Blue, Green,**  and  **Yellow**  .                                                               |

**Working With Scout Images**

Scout images display in the Scout window, which is part of the Radiology viewer. The scout line on the image in the Scout window shows the relationship of the image in the Scout window and the image in the Radiology viewer (if there is such a relationship).

##### To open a Scout image in the Scout window:

1. Start Clinical Display and select a patient.
2. In the Image List window, double-click a study with either CT or MR images.

<!-- image -->

1. In the Group Abstracts window that displays, click an image from the series.
<!-- image -->

The Radiology viewer loads all the information from the text file in addition to the DICOM header to determine scout information and displays a message informing you about that.

<!-- image -->

1. If the image is a scout image, it displays in the Scout window.

**Note** : The **Scout | Auto Detect** menu option in the Radiology viewer must be selected for the Scout window to display. If the **Auto Detect** option is not selected, select it from the Scout menu and try again.

<!-- image -->

1. If the image is an MR image or if the image is not a scout image, choose **Scout | Add Image to Scout Window** to place the image in the Scout window.

When the image is selected in the Scout window, the Radiology viewer determines if any other displayed image is associated and displays a scout line in the correct location on the image in the Scout window.

1. Use the navigation controls of the viewer window (the arrows left of the image area or the Image menu options) to page through the in the Radiology viewer.

The position of the scout line on the image in the Scout window changes to show the slice that the image displayed in the Radiology viewer represents. This is illustrated in the following screenshot.

<!-- image -->

1. Click on the image in the Scout window.

The scout line shifts and the image in the Radiology viewer changes to show selected or nearest slice image.

**Specifying the Color of the Scout Line**

You can change the color of the Scout line to be one of the supported colors: red, blue, green or yellow. This color selection is stored in VistA as a user preference.

##### To change the color of the scout line:

1. In the Scout window, choose **Scout | Scout Line Color | &lt;** ***ColorOption*** **&gt;** where

**&lt;** ***ColorOption*** **&gt;** is one of the available menu options: **Red** , **Blue** , **Green** and **Yellow** .

If the Scout window is displayed, you will see the change in the color of the scout line. If the Scout window is not displayed, you will see the change when the Scout window opens.

<!-- image -->

**Hiding Scout Lines and Turning off Automatic Detection of Scout Images**

Loading all the header information for the images in a study is necessary to display scout lines. If you are not using scout lines or if you want to speed up the loading of the images in a series, you can turn the options to automatically detect scout lines and to display scout lines off.

##### To turn off automatic detection and the display of scout lines:

1. In the Radiology viewer, from the **Scout** menu deselect **Auto Detect Scout Images** and

##### Display Scout Lines.

The change is effective immediately. It is saved in your user preferences in VistA. The next time the Radiology viewer loads a series, it will not load the header information.

If you want to display scout lines, you must turn the options to automatically detect scout lines on.

##### To turn automatic detection and the display of scout lines back on:

1. In the Radiology viewer, from the **Scout** menu select **Auto Detect Scout Images** and

##### Display Scout Lines.

The change is effective immediately. It is saved in your user preferences in VistA. The next time the Radiology viewer loads a series, it will not load the header information and display scout lines.

## Viewing the Different Color Channels of an Image

<!-- image -->

You can separate and display individual red, green, and blue color channels of 24-bit color images.

Separating the color channels and displaying them is useful because a full color 24-bit image can reveal different diagnostic information when cycling between the individual color channels.

Separating the color channels also lets you compare the views of individual channels side by side or the view of a single channel and the view of the full color image.

<!-- image -->

You can cycle through the channels of a 24-bit image displayed in both the Full Resolution viewer and the Radiology viewer by clicking the  Color Channel button on the toolbar or by using the **Color Channel** option of the the **Image** menu.

**The Color Channel Button**

<!-- image -->

The  Color Channel button on the toolbar is enabled when you open a 24-bit image. The following image shows the color separation button enabled in the Radiology Viewer.

<!-- image -->

The following image shows the Color Channel button in the Full Resolution Viewer.

<!-- image -->

The view of the button changes depending on the channel displayed.

<!-- image -->

– View of the Color Channel button showing all channels.

<!-- image -->

– View of the Color Channel button showing the red channel.

<!-- image -->

<!-- image -->

– View of the Color Channel button showing the green channel.

– View of the Color Channel button showing the blue channel.

**The Color Channel Option on the Image Menu**

The **Color Channel** option on the **Image** menu of both the Full Resolution and the Radiology viewers is enabled when a 24-bit image is displayed. It has four sub-menus:

**Full Color (RGB)** – Displays all channels. **Red Channel** – Displays the red channel. **Blue Channel** – Displays the blue channel. **Green Channel** – Displays the green channel.

The following image shows the **Color Channel** option in the Radiology Viewer.

<!-- image -->

**Using the Color Channel Separator to Compare Images in Dual Stack View**

In the Radiology viewer you can set up a dual stack view where, for example, the left stack shows the full-color view and the right stack shows one of the color channels from the same image. The following image shows an example of a dual stack comparison.

<!-- image -->

The information bar (the yellow bar at the bottom of the radiology image) indicates the color channel that is displayed. The color channel display can be inverted by clicking on the Invert Image toolbar button when a color channel is selected.

## Working With Annotations

<!-- image -->

You can annotate images in the Full Resolution Viewer and in the Radiology Viewer.

### Overview

You can use annotations to make notes, comments, and callouts to transcribe inscriptions, add symbols, and highlight areas of interest. Annotations overlay an image (or document scanned as an image) without altering the image. Although annotations become part of the patient’s medical record, they are saved separately from the image in the VistA database.

For example, you can draw an arrow or an ellipse over an area of interest, or you can supply measurements of length or angle using the ruler tool or the protractor tool. You can annotate images or documents scanned as images that are of the following type: .bmp, .dcm, .jpg, .pdf (single page and multi-page), .tga, and .tif (single page and multi-page).

You cannot add permanent annotations to remote radiology images from the Department of Defense (DoD).

You cannot view annotations on DoD images that were created by a DoD application. Clinical Display does not provide any indication that an image has such annotations. However, you can create *temporary* measurements using the ruler and protractor tools on the Annotation toolbar in the Radiology viewer. In the Full Resolution Viewer, DoD images cannot be annotated or measured.

You can add annotations before and after the Text Integration Utility (TIU) note is signed or consult resulted, if allowed by TIU business rules. Clinical Display makes it easy for you to distinguish which annotations were made before and after the TIU note is signed or consult resulted by automatically changing their appearance. See *Creating Annotations* for more information.

In Clinical Display, you can selectively view and hide annotations that are part of images displayed in the Full Resolution Viewer and in the Radiology Viewer.

In the Radiology Viewer, you can make annotations to images in a single or dual stack mode but not in the layout view.

You can annotate all images that open in the Radiology Viewer, such as dermatology and ophthalmology images, except RAD package images and DoD radiology images. For RAD package images and DoD radiology images, you can only create *temporary* measurements using the ruler and protractor tools on the Annotation toolbar. For more information on creating temporary annotations to Radiology Package images, see *Annotating images captured with Clinical Capture Client.*

*Starting with MAG*3.0*167 Clinical Display and MAG*3.0*151 Clinical Capture, Clinical* Capture will communicate with Clinical Display for the annotation of patient images. In Clinical Capture, the annotation functionality was removed. Users of Clinical Capture now have the option to open newly captured images, or existing patient images, in Clinical Display. Images are

opened in a separate window specifically for annotation. Opening in a separate window will not disrupt any image that is currently opened for display purposes.

The following table lists the menu items and windows that are used to annotate images from actions in the Clinical Capture application.

| <!-- image -->                                                                                                                                                                                       | If the menu option File &#124; Open Image for Annotation after Image OK is checked, then any image captured will automatically open for annotation in the Display Image by ID # window of Clinical Display. (see graphic below)                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <!-- image -->                                                                                                                                                                                       | If the user is viewing an Image in the Patient's latest Images window, the user can select the menu option: Options &#124; Open Image in Clinical Display. This action will open the image for annotation in the Display Image by ID # window of Clinical Display. (see graphic below) |
| If Clinical Display is not open, performing the actions above will automatically open Clinical Display.  The user can also open or synchronize with Clinical Display by using the menu option below. |                                                                                                                                                                                                                                                                                        |
| <!-- image -->                                                                                                                                                                                       | Select the menu option: Tools &#124; Open/Sync with Clinical Display.  One of two dialog boxes below will be displayed.                                                                                                                                                                |

| <!-- image -->   | If Clinical Display is running, you will see this Confirmation Dialog box. Click “OK” to synchronize Clinical Capture and Clinical Display.  When Synchronized, a message is displayed to notify Clinical Display that Capture has requested an Image to be opened for annotation.  That image will be opened in the Display Image by ID # window of Clinical Display. (see graphic below)                        |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <!-- image -->   | If Clinical Display is not running, you will see this Confirmation Dialog box. Click “OK” to open Clinical Display and synchronize with Clinical Capture.  When synchronized, a message is displayed to notify Clinical Display that Clinical Capture has requested an image to be opened for annotation.  That image will be opened in the Display Image by ID # window of Clinical Display. (see graphic below) |

<!-- image -->

<!-- image -->

Display Image from ID # Window

This window is used to open an image for annotation when requested by Clinical Capture.

The window is similar to the Full Resolution window, and has the same menu options and toolbars. Annotating an image is performed the same as the Full Resolution window.

An additional panel at the top of the window displays Patient Name and Image ID of the opened image.

Also displayed are the CCOW icon

and text

These are visual reminders that CCOW Patient Context is not maintained in this window.

With Patient Context off, the user can annotate an image for a different patient than is currently begin viewed.

<!-- image -->

|                |                                                                                                                                                                                                                                                                                                                    |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <!-- image --> |                                                                                                                                                                                                                                                                                                                    |
| <!-- image --> | In Clinical Display, the menu option System Manager &#124; Open Image by ID for annotation can be selected as an alternate way to open an image for annotation.  This allows the user to open an Image for annotation while viewing other images.  This menu option is also on the Image List window Manager menu. |

Annotating RAD Package Images and DoD Radiology Images

.

Clinical Display pops up a notification that an image or image group has been annotated in VistARad when hovering over an abstract, tree item, or list view item. The icons appear in the Abstracts window, in the tree view, and in list view.

The following image shows the hover-over notification in the Abstracts window.

<!-- image -->

The following image shows the hover-over notification in tree view.

<!-- image -->

The following image shows the hover-over notification in list view.

<!-- image -->

The following table summarizes the annotation functionality for the different image types and viewers.

| **Image Type**                              | **Annotations Supported?**   | **Notes**                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **BMP**                                     | yes                          | All users can view images with their annotations, print images with their annotations, and view the annotation history of an image.  Users with annotation permission can create annotations on images.  Users holding the MAG ANNOTATE MGR security key can edit and delete previously saved annotations on an image. |
| **DCM (single image and multi-frame cine)** | yes                          |                                                                                                                                                                                                                                                                                                                        |
| **JPG**                                     | yes                          |                                                                                                                                                                                                                                                                                                                        |
| **PDF (single page and multi-page)**        | yes                          |                                                                                                                                                                                                                                                                                                                        |
| **TGA**                                     | yes                          |                                                                                                                                                                                                                                                                                                                        |

| **Image Type**                               | **Annotations Supported?**   | **Notes**                                                                                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------------|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **TIFF (single page and multi-page)**        | yes                          |                                                                                                                                                                                                                                                                                                                                                                                                                |
| **RAD package images annotated in VistARad** | no                           | Users cannot view or print the annotations that were created in VistARad.  Clinical Display provides notification that an image or image group was annotated in VistARad.  All users can create  *temporary*  measurements using the ruler and protractor tools on the Annotation toolbar.  All users can print the temporary annotations, but cannot save them when they close the annotation session.        |
| **DoD radiology images**                     | no                           | Users cannot view or print DoD annotations on radiology images. Clinical Display does not provide a notification as it does with VistARad annotated images.  All users can create  *temporary*  measurements using the ruler and protractor tools on the Annotation toolbar in the Radiology viewer. Users can print these temporary annotations, but cannot save them when they close the annotation session. |
| **DoD non-radiology images**                 | no                           | These images are read-only. All users cannot create  *temporary*  measurements using the ruler and protractor tools on the Annotation toolbar.                                                                                                                                                                                                                                                                 |
| **Waveform displays in the MUSE EKG viewer** | no                           |                                                                                                                                                                                                                                                                                                                                                                                                                |

### Annotation Permissions

Site administrators can use a set of parameter definitions to set annotation permissions. These parameters provide the flexibility to grant and deny annotation permissions to individual users at the site, to all users of a particular service at that site, to an entire division associated with that site, or for all users at the site.

The MAG ANNOTATE MGR key provides users with the ability to edit and delete saved annotations. It also lets the user create annotations regardless of their annotation parameter definition settings. Typically the MAG ANNOTATE MGR key is reserved for privileged users who must change annotations as, for example, in a quality control role. To ensure that annotations created by other users are modified in a controlled manner, this key is not intended for wide distribution.

### Annotating Images at Remote Sites

Annotation permissions for remote users are defined using the same parameter definitions and key as local users, as described in the previous section.

### Activating the Annotation Mode

Image annotation is now an integrated feature of the Full Resolution Viewer and the Radiology Viewer. Opening the Annotation toolbar places the image in Annotation Mode, allowing authorized users to add annotations to it. Annotation Mode is active until the Annotation toolbar is closed. In the Radiology Viewer, users can annotate selected images in single or dual stack mode. You can also annotate DICOM multi-frame cine loops, one frame at a time.

##### To open the Annotation toolbar and place the image in the Annotation Mode, do one of the following to a selected image:

<!-- image -->

<!-- image -->

<!-- image -->

- From the Full Resolution Viewer toolbar, click the Annotations  button located next to the Refresh  button.
<!-- image -->
- From the image in the Full Resolution Viewer toolbar, click the **Annotations** button located next to the **Close** button on the title bar.

<!-- image -->

<!-- image -->

<!-- image -->

- From the Radiology Viewer, click the Annotations  button to open the Annotation toolbar.

By default, when you first open an image that has annotations, the most recently saved annotation layer becomes the current view. If you have annotation permission, you can further annotate the image. When you save your changes, they are saved as a new layer. The layers become the image’s history of annotation sessions (“history layers”). For more information about history layers, see *Viewing Audit History* .

Annotations you make to an image associated with a Text Integration Utility (TIU) note before the note is signed or consult resulted are visually different from annotations made after the note is signed or consult resulted. Annotations you make before the note is signed or consult resulted have solid lines and normal text (as demonstrated in the left image). Annotations you make after the note is signed or consult resulted have dashed lines and underlined text (as demonstrated in the image on the right).

<!-- image -->

<!-- image -->

**Annotation Tool Buttons**

The Annotation toolbar is a floating tool panel. When the Annotation toolbar is open, you can drag the Annotation toolbar to any location on the screen. Click and hold down the left mouse button over the Annotation toolbar’s title bar and drag it to the desired spot on the screen.

If you have more than one image displayed in a viewer, annotation mode, and hence the actions of the Annotation toolbar are applied to the image that has focus.

The Annotation toolbar has three sections:

- The upper part of the toolbar displays the annotation tools.
- Just below the Annotation tools section is information about user permissions and annotation counts.
<!-- image -->
- The Status bar displays either session information or annotator information, depending on whether you have an annotation(s) currently selected in the image. When the toolbar first opens, the Status bar displays the following text: **Current Annotation Session** .

The following table describes the buttons available in the Annotation toolbar.

| <!-- image -->   | **Edit Annotations**  button           |
|------------------|----------------------------------------|
| <!-- image -->   | **View Annotations**  button           |
| <!-- image -->   | **Select Annotation**  button          |
| <!-- image -->   | **Line**  button                       |
| <!-- image -->   | **Freehand**  button                   |
| <!-- image -->   | **Rectangle**  button                  |
| <!-- image -->   | **Text**  button                       |
| <!-- image -->   | **Ellipse**  button                    |
| <!-- image -->   | **Arrow**  button                      |
| <!-- image -->   | **Highlighter**  button                |
| <!-- image -->   | **Ruler**  button                      |
| <!-- image -->   | **Protractor**  button                 |
| <!-- image -->   | **Annotation Property Editor**  button |
| <!-- image -->   | Global Annotation Attributes button    |
| <!-- image -->   | **Audit History**  button              |
| <!-- image -->   | **Annotation Information**  button     |

The User permissions line provides the following information:

1. The user permission setting:
    1. Read Only
    2. Read/Write Permission
    3. Master Key Permission
    4. RAD Package
    5. DOD
2. The count of annotations on the page and the count of hidden annotations on the page. If the image is multi-paged, both counts span all of the pages.
<!-- image -->

When the image cannot be annotated or if you select and try to modify a pre-existing saved annotation, the line will display the read-only indicator . The indicator also appears when viewing RAD package images, DoD radiology images, or when the user does not have annotation permission.

The following image shows the read only indicator when a RAD package image is open in the Radiology viewer.

<!-- image -->

<!-- image -->

The Status bar displays the session state except when an annotation in the image is selected. A selected annotation will display the annotator’s name, annotator’s service, and date/time when the annotation was last saved. If the information is longer than the status bar, hover over the status bar to see the full listing. If the hover over information needs to be displayed longer, you can click the Annotation Information  button (be sure to select one or more annotations before clicking the button).

### Creating Annotations

**Drawing Lines**

<!-- image -->

You can use the Line  button to draw lines on an image. To draw a line:

<!-- image -->

1. Click the Line  button.
2. Click and drag the mouse to draw the line on the image.
3. Release the mouse button.
<!-- image -->

The Select Annotation	tool becomes active again.

<!-- image -->

**Drawing Freehand Drawings**

<!-- image -->

You can use the Freehand  button to hand draw annotations, such as curved lines, or shapes not possible with the rectangle or ellipse. Using the Freehand Properties dialog box, you can allow the annotation tool to draw a line from the beginning to the end of the freehand drawing to produce a closed path (see *Setting Freehand Shape Properties* ).

To make a freehand drawing:

<!-- image -->

1. Click the Freehand  button.
2. Click and drag the mouse to make the drawing.
3. Release the mouse button.
<!-- image -->

The Select Annotation	tool becomes active again.

<!-- image -->

**Drawing Rectangles**

<!-- image -->

Use the Rectangle	button to draw an unfilled rectangle on the image (as opposed to the Highlighter tool that draws a filled rectangle on the image).

To draw a rectangle:

<!-- image -->

1. Click the Rectangle	button.
2. Click and drag the rectangle on the image to the desired height and width.
3. Release the mouse button.
<!-- image -->

<!-- image -->

The Select Annotation	button becomes active again.

**Adding Text to Images**

<!-- image -->

You can use the Text button to add text on the image. After you have entered the text, you can change the size or color of the font (see *Setting Text Properties* ). If you need to edit the text after you have left the text box, use the **Text** tab of the Text Properties dialog box (see *Editing Text* .)

If the text appears too small or too large, you can set the text size of the annotation (see *Setting Text Properties* ) or you can set all future text annotations with the global text properties. If you have a low resolution image, you would use a small font size and for high resolution images you will use a larger font size. For more information on setting your global font annotations properties, see *Setting Global Annotation Attributes.*

To enter text:

<!-- image -->

1. Click the Text	button.
2. Click and drag the text pad on the image to the desired height and width. If you do not drag the text box, you cannot see the text until you finish typing and click outside of the text box.
3. Release the mouse button.

<!-- image -->

The Select Annotation	button becomes active again, but the cursor is blinking in the text box waiting for you to enter text.

<!-- image -->

1. If you click outside of the text box without entering text, Clinical Display automatically inserts the following text in the text box: **Enter Text Here** (see *Editing Text* for more information).
<!-- image -->
2. To enter text in the text box, start typing text in the text box. If you enter any illegal characters, you will be asked to delete them.
<!-- image -->

**Note:** The following characters are illegal and are not allowed: &amp; &lt; &gt;To edit the text after you have left the text box, see *Editing Text* .

1. When you are finished typing text, click anywhere outside of the text box to close the text box.

**Drawing Ellipses**

<!-- image -->

Use the Ellipse	button to draw an ellipse on the image. To draw an ellipse:

<!-- image -->

1. Click the Ellipse	button.
2. Click and drag the ellipse on the image to the desired height and width.
3. Release the mouse button.
<!-- image -->

<!-- image -->

The Select Annotation	button becomes active again.

**Drawing Arrows**

<!-- image -->

You can use the Arrow  button to draw an arrow on the image. To draw an arrow:

<!-- image -->

1. Click the Arrow  button.
2. Click and drag the mouse to draw the line in the direction of the arrow.
3. Release the mouse button.
<!-- image -->

After you drag and release the mouse, Clinical Display automatically inserts the arrow head where you release the mouse. The Select Annotation	tool becomes active again.

<!-- image -->

**Highlighting Areas**

<!-- image -->

Use the Highlighter  button to highlight an area on an image. To draw a highlight:

<!-- image -->

1. Click the Highlighter  button.
2. Click and drag the mouse to make the highlight fit the area to be highlighted.
3. Release the mouse button.
<!-- image -->

The Select Annotation	button becomes active again.

<!-- image -->

**Using the Ruler**

<!-- image -->

Use the Ruler  button to place a ruler over the image. You can use rulers to measure absolute and relative distances on an image.

To draw a ruler:

<!-- image -->

<!-- image -->

1. Click the Ruler  button. The **Ruler** menu opens.
<!-- image -->
2. In the Ruler menu, click the Ruler  button.
3. Click the image and hold the left mouse button down to start measuring.
4. Drag the tool to define the end measuring point.
5. Release the mouse button.
<!-- image -->

If the image has no pre-existing calibration information (for example, not a DICOM image that has pixel spacing information in the DICOM header), the Calibrate Ruler dialog box opens.

***Calibrating Rulers***

If the image is not a pre-calibrated DICOM image, the Calibrate Ruler dialog box opens the first time you create a ruler on the image. You can calibrate rulers to have absolute or relative

measurements. For an absolute measurement, draw the start and end points of the ruler between two known reference points located in the image and then choose the appropriate measurement units. Additional rulers drawn on the image will have the same calibration setting. To measure relative distances, calculate ratios of one ruler measurement to another ruler’s measurements that are placed over areas of the image.

If the image has pre-calibrated DICOM information, the ruler will automatically provide measurement information as the ruler is drawn. You cannot override the DICOM calibration information in the Calibrate Ruler dialog box.

To calibrate the ruler, do the following from the Calibrate Ruler dialog box::

1. Select the unit of measurement from the **What is the measurement unit?** drop-down list. Selections are: Centimeter (cm), Millimeter (mm), Inches (in), and Relative (unit).
<!-- image -->

<!-- image -->
2. Enter the numeric measurement in the **What is the measurement?** text boxes.
3. Do one of the following:
    - To set the calibration, click **Set** .
    - To cancel the calibration modification, click **Cancel** .

**Measuring Angles in Images**

<!-- image -->

Use the Protractor  button to measure angles in the image. You can change the protractor’s

attributes, such as color of the line, opacity, and font size (see *Setting Protractor Properties* ). To add a protractor::

<!-- image -->

1. Click the	Protractor button.
2. Click the image to begin the first line segment.
3. Move the mouse to the area to where the first line segment is to end.
4. Click to set the vertex.
<!-- image -->
5. Move to the area to where the second line segment is to end.
6. Click to end the second line segment.
<!-- image -->

<!-- image -->

The Select Annotation	tool becomes active again.

The value of the angle is displayed in degrees near the vertex.

### Modifying Annotations

**Selecting Annotations**

<!-- image -->

Use the Select Annotation	button to select annotations. When you select annotations, image handles or selection borders display on the annotations to indicate that the annotations are selected. Image handles are the tiny, square blocks on lines, freehand drawings, and arrows.

Image selection borders are the checkered borders around rectangles, ellipses, text, and highlights.

<!-- image -->

To select one annotation with the Select Annotation	button::

<!-- image -->

1. Click the Select Annotation	button.
<!-- image -->
2. Click on the annotation.

To select one or more annotations with the Select Annotation	button:

<!-- image -->

<!-- image -->

1. Click the Select Annotation	button.
2. Drag the mouse over the area to be selected.
<!-- image -->

A marquee (selection box) appears around the entire area selected.

<!-- image -->

To select all annotations on an image with the Select All option from the Edit Annotations  button:

<!-- image -->

<!-- image -->

1. Click the Edit Annotations  button.
2. Click Select All.

All annotations on the current page are selected.

**Moving Annotations**

<!-- image -->

Use the Select Annotation	button to move annotations you have made but have not yet saved. Only users with the MAG ANNOTATE MGR key can move annotations after they have been saved. Clinical Display only allows you to move one annotation at a time.

To move a selected annotation:

1. Select an annotation.
2. Drag the annotation to the new location.
3. Release the mouse button.

**Resizing Annotations**

<!-- image -->

Use the Select Annotation	button to resize annotations you have made but have not yet saved. Only users with the MAG ANNOTATE MGR key can resize annotations after they have been saved.

To resize a selected annotation:

1. Depending on the type of annotation, either click the selection border (for rectangle or ellipse type of annotations) or click an image selection handle (for line-based annotations).
2. Drag the annotation to the new size.
3. Release the mouse.

**Deleting Annotations**

<!-- image -->

You can only delete annotations you have not yet saved. Only users with the MAG ANNOTATE MGR key can delete saved annotations. To delete annotations, you can either select annotations with the Select Annotation	button or the **Select All** menu option. Another option is to use **Delete All Annotations** to delete all of the annotations on the page. When you delete an annotation, your deletion is recorded in audit history and can be viewed by you or other users.

You cannot delete annotations in a history layer.

##### To delete selected annotations:

<!-- image -->

1. Use the Select Annotation	button to select one, some, or more annotations to delete.
<!-- image -->

<!-- image -->
2. Click the Edit Annotations  button. The **Edit Annotations** menu opens.
3. To delete selected annotations, click **Delete Selected Annotations** .
4. Do one of the following:
    - Click **Yes** to delete the selected annotations and close the Confirm delete dialog box.
    - Click **No** to cancel the deletion and return to the Annotation Mode..

<!-- image -->

To delete all annotations on the current page using the Edit Annotations  button:

<!-- image -->

1. Click the Edit Annotations  button.
2. The Edit Annotations menu opens.
<!-- image -->
3. To delete all annotations, select **Delete All Annotations** .
4. Do one of the following:
    - Click **Yes** to delete the all annotations and close the Confirm delete dialog box.
    - Click **No** to cancel the deletion.

**Changing Selected Annotation Attributes**

<!-- image -->

<!-- image -->

You can use the **Annotation Property Editor** button to modify the properties of a selected annotation before you save your annotations. To edit saved annotations you must have the MAG ANNOTATE MGR key. The **Annotation Property Editor** button is available when you have only one unsaved annotation selected. When you change properties using the Annotation Property Editor, the changes do not get applied to other annotations. For example, if you want to change the line color of the selected annotation to blue, use the Annotation Property Editor. If you want to change the line color of all future annotations, use the Global Annotation Attributes. For more information, see *Setting Global Annotation Attributes.*

1. Select the annotation to be edited.

Image Handles or selection borders appear on the annotation.

<!-- image -->

1. Click the Annotation Property Editor  button.

The Annotation Property Editor dialog box applicable to the selected annotation opens.

1. The Annotation Property Editor dialog box provides different tabs and settings, depending on the type of annotation being edited.

**Setting Color Properties**

Use the Annotation Property Editor **Color** tab to change the color, opacity, and fill of the selected annotation.

1. Select the annotation to change its color properties.
<!-- image -->
2. Click the **Annotation Property Editor** button..
3. Click the **Color** tab of the dialog box that opens. The title bar and view may vary depending on the type of shape selected. When the shape is a rectangle or an ellipse, you can select a checkbox for the fill of the shape.

<!-- image -->

1. To select a color for the annotation, click a color on the **Annotation Color** pallet. The color selected is displayed in the **Color selected** field.
2. To adjust the opacity, move the indicator between **Min** and **Max** .
<!-- image -->
    - Moving the indicator toward **Min** makes the annotation more transparent.

<!-- image -->

- Moving the indicator toward **Max** makes the annotation more opaque.
1. To fill in a shape, clear the **No Fill** check box.
2. To clear the fill in a shape, click the **No Fill** check box.
3. Click **OK** to close the Annotation Property Editor dialog box.

**Setting Line/Arrow Properties**

Use the Line/Arrow Property Editor dialog box to change attributes related to lines and arrows. The Line/Arrow Property Editor dialog box has two tabs: **Shape** and **Color** .

***Setting Line/Arrow Shape Properties***

Use the Line/Arrow Property editor **Shape** tab to modify line width, arrow head type, length of arrow head, and angle of the arrow head of the selected line or arrow.

To set the line or arrow properties for a selected line or arrow:

<!-- image -->

1. Click the Annotation Property Editor  button. The Line/Arrow Property Editor dialog box opens.

<!-- image -->

1. Use the decrease and increase arrows beside the **Width** text box to modify the width of the line for the selected line or arrow annotation. For a thicker line, use a higher number in the **Width** box.

**Note:** If you have a line annotation selected, the **Arrow Head** drop-down box is automatically set to **None** and the **Length** and **Angle** text boxes are disabled.

1. To add or modify an arrow head, click the **Arrow Head** drop-down menu to select the arrow head type.
<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->
    - For no arrow head, select **None** in the drop-down box.
    - For a Pointer, select **Pointer** in the drop-down box.
    - For a solid arrow, select **Solid** in the drop-down box.
    - For an open arrow, select **Open** in the drop-down box.
    - For a solid pointer, select **Solid** pointer in the drop-down box.
2. To modify the arrow head length and angle, use the **Length** and **Angle** text boxes.
3. To make the arrow head longer or shorter, use the decrease and increase arrows beside the **Length** text box. The higher the range number, the longer the arrow head.
4. To make the angle of the arrow head lesser or greater, use the decrease and increase arrows beside the **Angle** text box. The higher the range number, greater the angle.
5. Click **OK** to close the Line/Arrow Property editor dialog box.

**Setting Freehand Properties**

Use the Freehand Property Editor dialog box to adjust the width, color, and opacity of the freehand annotation. You can also allow the annotation tool to draw a line from the beginning to the end of the freehand drawing to produce a closed path.

***Setting Freehand Shape Properties***

Use the Freehand Property Editor **Shape** tab to adjust the width of the line for the freehand annotation. This tab is also used to produce a closed path.

To set the line properties for a selected freehand drawing:

<!-- image -->

1. Click the **Annotation Property Editor** button. The Freehand Property Editor dialog box opens.

<!-- image -->

<!-- image -->

1. Use the decrease and increase arrows beside the **Width** text box to modify the width of the line for the selected freehand drawing. For a thicker line, use a higher number in the **Width** box.
2. To produce a closed path for a freehand annotation, click the **Closed** check box.
<!-- image -->
3. To close the Freehand Property Editor dialog box,, click **OK.**

**Setting Rectangle/Highlighter Properties**

Use the Rectangle/Highlighter Property editor to modify the width, color and opacity of the selected rectangle or highlight. Rectangles and highlights can both be modified by this editor. A rectangle is not usually filled, but you can change the fill property. A highlight is usually filled and it usually has a low opacity setting to allow you to see through the annotation to the image beneath the highlighted area.

***Setting Rectangle/Highlighter Shape Properties***

Use the Rectangle/Highlighter Property Editor Shape tab to modify the width of the line used to outline the rectangle or highlight.

To set the line width for a rectangle or highlight:

1. Click the Rectangle or Highlight to select it.
<!-- image -->
2. Click the Annotation Property Editor  button.

The Rectangle/Highlighter Property Editor dialog box opens.

<!-- image -->

1. Use the decrease and increase arrows beside the **Width** text box to modify the width of the line for the selected rectangle or highlight. For a thicker line, use a higher number in the **Width** box.
2. To close the Rectangle/Highlighter Property Editor dialog box, click **OK** .

**Setting Text Properties**

Use the Text Property Editor dialog box to modify font style and size, text, and color of the selected text.

***Setting Text Font Styles and Sizes***

Use the Text Property Editor **Font** tab to adjust font style and size. Only one font is allowed to keep the style of text annotations consistent across the VistA database.

1. Click the text to select it.
<!-- image -->
2. Click the Annotation Property Editor  button. The Text Property Editor dialog box opens.
<!-- image -->
3. To select a style, click a style type from the **Style** list. Choices are: **Regular** , **Bold** , **Italic** , and **Bold Italic** .
4. To select a font size, click a font size from the **Size** list. Choices are: **8** , **9** , **10** , **11** , **12** , **14** , **16** , **18** , **20** , **22** , **24** , **26** , **28** , **36** , **48** , and **72** .

1. To close the Text Property Editor dialog box,, click **OK** .

***Editing Text***

Use the Text Property Editor **Text** tab to add or edit text after you have left the text box. To add or modify text:

1. Click the **Text** tab from the Text Property Editor dialog box.
<!-- image -->

The Text Property Editor **Text** tab opens. The **Alignment** list allows you to position the text in the text box on the image. The **Word Wrap** check box only affects the text in the **Text** tab. It does not affect the text on the image.

1. To edit the text, click in the text annotation area and begin typing. If you type any illegal characters, you will not be able to leave the text annotation area until you delete them.

**NOTE** : The following characters are illegal and not allowed: &amp; &lt; &gt;

1. To change the alignment of the text in the text annotation area, click the **Alignment** drop- down menu.
2. To close the Text Property Editor dialog box, click **OK** .

**Setting Ellipse Properties**

Use the Ellipse Property editor to modify the width, color and opacity of the selected ellipse.

***Setting Ellipse Shape Properties***

Use the Ellipse Property Editor Shape tab to specify the width of the line for the Ellipse. To set the shape properties of an ellipse:

1. Click the Ellipse to select it.
<!-- image -->
2. Click the Annotation Property Editor  button. The Ellipse Property Editor dialog box opens.

<!-- image -->

1. Use the decrease and increase arrows beside the **Width** text box to modify the line width. The higher number, the greater the width.
2. To close the Ellipse Property Editor dialog box, click **OK** .

**Setting Ruler Properties**

You can select the color and width properties for rulers using the Ruler Properties dialog box.

***Setting Ruler Font Styles and Sizes***

Use the Ruler Property Editor **Font** tab to adjust font settings for the text associated with the ruler. Font settings include style and size.

To set the font style and size of the text for a ruler:

1. Click the ruler to select it.
<!-- image -->
2. Click the Annotation Property Editor  button. The Ruler Property Editor dialog box opens.
<!-- image -->
3. To select a style, click a style type from the **Style** list. Choices are: **Regular** , **Bold** , **Italic** , and **Bold Italic** .
4. To select a size, click a font size from the **Size** list. Choices are: **8** , **9** , **10** , **11** , **12** , **14** , **16** , **18** , **20** , **22** , **24** , **26** , **28** , **36** , **48** , and **72** .
5. To close the Ruler Property Editor dialog box, click **OK** .

***Setting Ruler Shape Properties***

Use the Ruler Editor Shape tab to specify the width of the line for the ruler.

1. Click the **Shape** tab from the Ruler Property Editor dialog box. The Ruler Property Editor Shape tab opens.
<!-- image -->
2. Use the decrease and increase arrows beside the **Width** text box to modify the line width. The higher number, the greater the width.
3. To close the Ruler Property Editor dialog box, click **OK** .

***Modifying Start Line Length and End Line Length***

You can modify the length of the start and end line for the ruler. To modify the length of the start and end line of the selected ruler:

1. Click the **Measure** tab from the Ruler Property Editor dialog box. The Ruler Property Editor dialog box opens.
<!-- image -->
2. Use the decrease and increase arrows beside the **Start Line Length** text box to modify the start line length. The greater the number, the longer the line starting the ruler. As shown below, the start line length is shorter than the end line length.

<!-- image -->

<!-- image -->

1. Use the decrease and increase arrows beside the **End Line Length** text box to modify the end line length. The greater the number, the longer the line ending the ruler.
2. To close the Ruler Property Editor dialog box, click **OK** .

**Setting Protractor Properties**

Use the Protractor Property Editor tool to modify font, line width, and color of the selected protractor annotation.

***Setting Protractor Font Styles and Sizes***

Use the Protractor Property Editor Font tab to adjust font settings for the text associated with the protractor tool. Font settings include style and size. Only one font is allowed to keep the style of text annotations consistent across the VistA database.

To set the font style and size for a protractor:

1. Click the Protractor to select it.
<!-- image -->
2. Click the Annotation Property Editor  button. The Protractor Property Editor dialog box opens.
<!-- image -->
3. To select a style, click a style type from the **Style** list. Choices are: **Regular** , **Bold** , **Italic** , and **Bold Italic** .
4. To select a size, click a font size from the **Size** list. Choices are: **8** , **9** , **10** , **11** , **12** , **14** , **16** , **18** , **20** , **22** , **24** , **26** , **28** , **36** , **48** , and **72** .

***Setting the Protractor Shape Properties***

Use the Protractor Editor **Shape** tab to specify the width of the line for the protractor. To set the line property of a protractor:

1. Click the **Shape** tab from the Protractor Property Editor dialog box. The Protractor Property Editor **Shape** tab opens.

<!-- image -->

1. Use the decrease and increase arrows beside the **Line Size** text box to modify the line width. The higher number, the greater the width.
2. To close the Protractor Property Editor dialog box click **OK** .

### Setting Global Annotation Attributes

<!-- image -->

You can use the Global Annotation Attributes  button or the **Annotation** tab from the User Preference dialog box to change annotation attribute settings for future annotations. These changes do not affect any pre-existing annotations.

Because the global annotation attribute user preferences are stored in your user settings, you can control annotation settings differently in Clinical Capture than in Clinical Display. For example, you may decide to set the color of arrow annotations drawn in Clinical Capture to blue and in Clinical Display to red. Thus, you can distinguish your annotations made during the capture process from your annotations made during display. Additionally, if other users choose different colors, then you will be able to visually distinguish different user’s annotations.

**Note** : You must save the changes you make to the global annotation attributes to have them applied in future sessions. To save the changes, use one of the Clinical Display User Preferences save options: **Save Settings Now** or **Save Settings on Exit** .

Default Values for Annotations

The following table displays default values for annotations. If you change these values in the Global Annotation Attributes dialog boxes, these values will no longer be the default.

| Attributes              | Default Value   |
|-------------------------|-----------------|
| Annotation Font Name    | Arial           |
| Annotation Font Style   | Regular         |
| Annotation Font Size    | 36              |
| Annotation Line Width   | 5               |
| Annotation Color        | Green           |
| Annotation Opacity      | 159             |
| Annotation Arrow Style  | Pointer         |
| Annotation Arrow Length | 35              |
| Annotation Arrow Angle  | 35              |

**Setting Global Annotation Font Attributes**

The Global Annotation Attributes **Font** tab is used to adjust font settings, such as style and size. For example, you can choose to make all fonts bold and sized to 14 points. Only one font is available in order to keep the style of text annotations consistent across the VistA database. The default font is Arial. The default style is regular, and the default font size is 36 points.

To set global annotation font attributes:

<!-- image -->

1. Click the Global Annotation Attributes  button or the **Annotation** tab from the User Preference dialog box..
<!-- image -->

The Global Annotation Attributes dialog box opens.

1. To select a font style, click a style type from the **Style** list. Choices are: **Regular** , **Bold** , **Italic** , and **Bold Italic** .
2. To select a font size, click a font size in the **Size** list. Choices are: **8** , **9** , **10** , **11** , **12** , **14** , **16** , **18** , **20** , **22** , **24** , **26** , **28** , **36** , **48** , and **72** .
3. To close the Global Annotation Attributes dialog box click the **OK** button.

**Setting Global Annotation Line Width Attributes**

Use the Global Annotation Attributes **Line Width** tab to modify the width of annotations. The default line width is **5** .

To set global annotation line width attributes, do the following:

1. Click the **Line Width** tab in the Global Annotation Attributes dialog box. The Global Annotation Attributes **Line Width** tab opens.
<!-- image -->
2. Use the decrease and increase arrows beside the **Line Size** text box to modify the line width. The higher number, the greater the width.
3. To close the Global Annotation Attributes dialog box click the **OK** button.

**Setting Global Annotation Color Attributes**

Use the Global Annotation Attributes **Color** tab to modify the default color of all annotations.

1. Click the **Color** tab from the Global Annotation Attributes dialog box. The **Color** tab opens.
<!-- image -->
2. To select a color for your annotations, click a color on the **Primary Colors** pallet. The color selected is displayed in the **Color selected** field.
3. To close the Global Annotation Attributes dialog box click **OK** .

**Setting Global Annotation Opacity Attributes**

Use the Global Annotation Attributes **Opacity** tab to modify the opacity of the color of annotations. The higher the opacity level, the more opaque the color is for the annotation. The default setting for opacity is: **159** .

1. Click the **Opacity** tab in the Global Annotation Attributes dialog box. The Global Annotation Attributes **Opacity** tab opens.
<!-- image -->

The opacity of annotations can be modified by either using the increase and decrease arrows beside the **Opacity** field or by dragging the indicator between **Min** and **Max** .

1. To use the arrows beside the **Opacity** field, click the increase or decrease arrows. The higher number, the more opaque the color of the annotation.

1. To use the indicator to adjust the opacity, move the indicator between **Min** and **Max** .
    - Moving the indicator toward **Min** makes the annotation more transparent.
    <!-- image -->
    - Moving the indicator toward **Max** makes the annotation more opaque.
    <!-- image -->
2. To close the Global Annotation Attributes dialog box, click **OK** .

**Setting Global Annotation Arrow Attributes**

Use the Global Annotation Attributes **Arrow** tab to modify arrow annotations. You can modify the pointer style, length, and angle. The default arrow attributes are **Pointer** for Pointer Style, **35** for Pointer Length, and **35** for Pointer Angle.

1. Click the Arrow tab in the Global Annotation Attributes dialog box. The Global Annotation Attributes **Arrow** tab opens.
<!-- image -->
2. Click the **Pointer Style** drop-down arrow to modify the arrow head type.
<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->
    - For no arrow head, select **None** in the drop-down box.
    - For a Pointer, select **Pointer** in the drop-down box.
    - For a solid arrow, select **Solid** in the drop-down box.
    - For an open arrow, select **Open** in the drop-down box.
    - For a solid pointer, select **Solid** pointer in the drop-down box.
3. To make the arrow head longer or shorter, use the decrease and increase arrows beside the **Pointer Length** text box. The higher the number, the longer the arrow head.
4. To make the angle of the arrow head lesser or greater, use the decrease and increase arrows beside the **Pointer Angle** text box. The higher the number, greater the angle.
5. To close the Global Annotation Attributes dialog box, click **OK** .

### Hiding and Showing Annotations

You can hide and show annotations that belong to you or to other users. For example, you can choose to hide all annotations for printing or to view the image without the clutter of other users’

annotations. Hiding an annotation is not treated as a change unless you add another annotation. If you save your annotations with one or more of the annotations hidden, you create a history layer along with a sub-layer named **As Last Viewed** .

**Hiding Annotations**

You can hide all annotations, selected annotations, annotations by user, annotations by service, or annotations by date.

To hide all annotations:

<!-- image -->

1. Click the View Annotations  button. The **Hide/Show** menu opens.
<!-- image -->
2. From the **Hide** menu, Click All to hide all annotations. To hide a selection of annotations:
    1. Select the annotations you want to hide.
    <!-- image -->
    2. Click the View Annotations  button. The **Hide/Show** menu opens.
    <!-- image -->
    3. Click **Selected** from the **Hide** menu. The selected annotations are hidden.
##### To hide annotations by user:
<!-- image -->
    1. Click the View Annotations  button. The **Hide/Show** menu opens.
<!-- image -->
    1. Click **By User** from the **Hide** menu.
    <!-- image -->
The Choices Available dialog box opens.
    1. Select the user ID of the user’s annotations you are hiding.
    2. To hide the user’s annotations, click **OK** .
The Choices Available dialog box closes and the image is displayed with the user’s annotations
hidden.
##### To hide annotations by service:
<!-- image -->
    1. Click the View Annotations  button. The **Hide/Show** menu opens.
    <!-- image -->
    2. Click **By Service** from the **Hide** menu. The Choices Available dialog box opens.
<!-- image -->
    1. Select the service annotation type you are hiding.
    2. To hide the service annotation, click **OK** .
The Choices Available dialog box closes and the image is displayed with the annotations for the service type hidden.
##### To hide annotations by date:
<!-- image -->
    1. Click the View Annotation  button. The **Hide/Show** menu opens.
    <!-- image -->
    2. Click **By Date** from the **Hide** menu.
    <!-- image -->
The Choices Available dialog box opens.
    1. Select the date of annotations to be hidden.
    2. To hide the annotations, click **OK** .
The Choices Available dialog box closes and the image is displayed with the annotations for that date hidden.
**Showing Annotations**
You can show all annotations, annotations by user, annotations by service, or annotations by date.
##### To show all hidden annotations:
<!-- image -->

<!-- image -->
    1. Click the View Annotations  button. The **Hide/Show** menu opens.
    2. Select **All** from the **Show** menu.
All annotations are shown, including annotations on other pages of a multi-page image.
##### To show hidden annotations by user:
<!-- image -->

<!-- image -->
    1. Click the View Annotations  button. The **Hide/Show** menu opens.
    2. Select **By User** from the **Show** menu.
    <!-- image -->
The Choices Available dialog box opens with the user name(s) of any user with hidden annotations.
    1. Select the user name.
    2. To show the annotations of the selected user, click **OK** . The annotations of the selected user are shown.
##### To show annotations by service:
<!-- image -->
    1. Click the View Annotations  button. The **Hide/Show** menu opens.
<!-- image -->
    1. Select **By Service** from the **Show** menu.
    <!-- image -->
The Choices Available dialog box opens with the service associated with hidden annotations.
    1. Click the service associated with the hidden annotations to be shown.
    2. To show the annotations, click **OK** .
The Choices Available dialog box closes with the hidden annotations for the service shown.
##### To show annotations by date:
<!-- image -->

<!-- image -->
    1. Click the View Annotations  button. The **Hide/Show** menu opens.
    2. Select **By Date** from the **Show** menu.
The Choices Available dialog box opens with the dates associated with the hidden annotations.
<!-- image -->
    1. Select the date associated with the hidden annotations.
    2. To show the annotations, click **OK** .

### Viewing Audit History

When you save annotations to an image, your annotations are permanently associated with the image. Each time you save your session, your annotations are saved as a new layer (also referred to as a “history layer”). Each layer can be viewed separately when you want to see how annotations were created and arranged on the image at a given point in time. When you are in a history layer, you cannot make any changes to the annotations that have already been made.

<!-- image -->

The Audit History  button expands the Annotation toolbar to show the annotation history for the image. You can expand the annotation tree to show layer history associated with the image. Layers are “roll ups” which means that newer layers will show that layer’s annotations along with the layers saved from earlier times. The top layer is marked as **Current Annotation Session** in the annotation history tree. You can only make changes to the current annotation layer.

<!-- image -->

When you select a layer saved with hidden annotations, you see a plus sign next to the layer. When you expand the plus sign, you see the option **As Last Viewed** below the layer. When you select a layer, all annotations are displayed, including the ones that are hidden. When you select the option **As Last Viewed** below the layer, the hidden annotations are not displayed. The reason for the **As Last Viewed** layer is that the annotator may have wanted the view to show a mixture of saved and unsaved annotations. By clicking on As Last Viewed you will see what the information was intended to convey. For patient safety however, when an image initially opens for display, all annotations in the last saved layer will show.

<!-- image -->

##### To open the audit history window::

1. Open an image and display the Annotation toolbar.
<!-- image -->
2. Click the Audit History  button.
<!-- image -->

The Annotation toolbar expands to display a tree view of annotation layers.

1. Click the Expand	icon next to the **Current Annotation Session** heading.
<!-- image -->

<!-- image -->

<!-- image -->

The **Current Annotation Session** heading expands to display the audit history of annotations related to the selected image.

1. Select a layer to view.

As you click through the layers, the annotations on the image in the Full Resolution Viewer or the Radiology Viewer change to reflect how the annotations appeared when they were saved.

1. Do one of the following:
    - To get a full listing of a user name displayed, hover over a history list item to display a tooltip with the user and annotation information.
    <!-- image -->
    - To close the audit history window, click the Audit History  button.

### Viewing Annotation Information

<!-- image -->

Use the Annotation Information  tool to view user name, image, and annotation information for one or more annotations. The Information dialog box provides the following information: your user name, the number of pages included in the image, the total count of annotations, number of annotations on the current page, total number of hidden annotations, and the count of hidden annotations on the page. The Information dialog box provides additional information depending on the circumstances: the number of annotations selected and whether the image is a single- or multi-page image.

<!-- image -->

1. To open the annotation information tool, click the Annotation Information  button. The Information dialog box opens.

The following Information dialog box is what you will see when you select all annotations on an image.

<!-- image -->

1. Click the **OK** button to close the Information dialog box..

**Note** : If you are viewing an image that was annotated in VistARad or is a DoD radiology image, the content of the Information dialog box will be different.

### Annotating images captured with Clinical Capture Client.

Starting with MAG*3.0*167 Clinical Display and MAG*3.0*151 Clinical Capture, Clinical Capture will communicate with Clinical Display for the annotation of patient images. In Clinical Capture, the annotation functionality was removed. Users of Clinical Capture now have the option to open newly captured images, or existing patient images, in Clinical Display. Images are opened in a separate window specifically for annotation. Opening in a separate window will not disrupt any image that is currently opened for display purposes.

The following table lists the menu items and windows that are used to annotate images from actions in the Clinical Capture application.

| <!-- image -->   | If the menu option File &#124; Open Image for Annotation after Image OK is checked, then any image captured will automatically open for annotation in the Display Image by ID # window of Clinical Display. (see graphic below)                                                        |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <!-- image -->   | If the user is viewing an Image in the Patient's latest Images window, the user can select the menu option: Options &#124; Open Image in Clinical Display. This action will open the image for annotation in the Display Image by ID # window of Clinical Display. (see graphic below) |

If Clinical Display is not open, performing the actions above will automatically open Clinical Display.

The user can also open or synchronize with Clinical Display by using the menu option below.

| <!-- image -->   | Select the menu option: Tools &#124; Open/Sync with Clinical Display.  One of two dialog boxes below will be displayed.   |
|------------------|---------------------------------------------------------------------------------------------------------------------------|

| <!-- image -->   | If Clinical Display is running, you will see this Confirmation Dialog box. Click “OK” to synchronize Clinical Capture and Clinical Display.  When Synchronized, a message is displayed to notify Clinical Display that Capture has requested an Image to be opened for annotation.  That image will be opened in the Display Image by ID # window of Clinical Display. (see graphic below)                        |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <!-- image -->   | If Clinical Display is not running, you will see this Confirmation Dialog box. Click “OK” to open Clinical Display and synchronize with Clinical Capture.  When synchronized, a message is displayed to notify Clinical Display that Clinical Capture has requested an image to be opened for annotation.  That image will be opened in the Display Image by ID # window of Clinical Display. (see graphic below) |

<!-- image -->

<!-- image -->

Display Image from ID # Window

This window is used to open an image for annotation when requested by Clinical Capture.

The window is similar to the Full Resolution window, and has the same menu options and toolbars. Annotating an image is performed the same as the Full Resolution window.

An additional panel at the top of the window displays Patient Name and Image ID of the opened image.

Also displayed are the CCOW icon

and text

These are visual reminders that CCOW Patient Context is not maintained in this window.

With Patient Context off, the user can annotate an image for a different patient than is currently begin viewed.

<!-- image -->

| <!-- image -->   |                                                                                                                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <!-- image -->   | In Clinical Display, the menu option System Manager &#124; Open Image by ID for annotation can be selected as an alternate way to open an image for annotation.  This allows the user to open an Image for annotation while viewing other images.  This menu option is also on the Image List window Manager menu. |

### Annotating RAD Package Images and DoD Radiology Images

You can only create temporary measurement annotations onto RAD Package and DoD radiology images. You can draw rulers and protractors on the image in the Radiology Viewer. The temporary annotations are discarded when you close the image.

If the image has measurement information in the image header, it automatically calibrates the rulers and displays DCM in parentheses next to the measurement. If the image does not have measurement information, you are prompted to calibrate the ruler.

##### To make temporary measurements on Radiology Package images:

1. Open a Radiology Package or DoD radiology image. The Radiology Viewer displays the image.

<!-- image -->

1. Click the Annotation	button to activate the Annotation Mode.
<!-- image -->

The Annotation toolbar opens with many of the buttons disabled (grayed out). VistARad and DoD radiology always show the read-only indicator as indicated by the Read-Only  icon, and will either show **RAD Package** or **DOD** .

<!-- image -->

<!-- image -->

1. You can draw a ruler . See *Using the Ruler* for more information about drawing a ruler.
<!-- image -->

<!-- image -->

1. You can draw a Protractor . See *Measuring Angles in Images* for more information about using the protractor.

### Exiting Annotation Mode and Saving Annotations

Close the Annotation toolbar, the image, or the viewer to save your annotation changes. When you save annotation changes, you create a new annotation history layer. Once annotations are saved, they are can be viewed on the image but are in read-only mode. Review your annotations when exiting Annotation Mode because your annotation layer will become a permanent part of the patient record unless you choose to discard the items you added. See *Viewing Audit History* for more information.

To the exit Annotation Mode:

1. Click the **Close** button on the Annotation toolbar, the annotated image, or the image viewer.
2. In the confirmation dialog box that displays do one of the following:
    - To save your annotations and exit Annotation Mode, click **Yes** . Your annotations are saved and the image exits Annotation Mode.
    - To exit Annotation Mode without saving your annotation changes, click **No** . Your annotation changes are discarded.
    - To resume working with annotations, click **Cancel** . Your annotation changes are not saved, but the image remains in Annotation Mode.
    - Printing Images, Processing ROI Requests and Copying Images This chapter provides information about these topics:
        - Printing images (single, multiple, and with annotations)
        - Processing ROI requests
        - Copying images
    Users who view patient images can also print and copy the images.
    Users need the MAG ROI or the MAG SYSTEM key to process ROI requests.**Note** : If you are at an IHS site, you can use the patient’s HRN to find the patient.

### Guidelines

- The print and copy functions can be accessed from the Image List window or from any of the viewers in the application.

**Note** : The MUSE EKG viewer does not have image copy functionality.

- Usually, a Reason code and an electronic signature are needed to print or copy an image. Users who have been assigned the MAG ROI key will need to enter a Reason code, but do not need to enter an electronic signature.
- An electronic signature is required only once for each imaging session. An imaging session starts at sign in and ends when you sign off, including when the application shuts down.
- Accepting the Physician Agreement for downloading images is required only once for each imaging session.
- Annotations can be printed with images either using the **Print Image** option from the

**File** menu, or from the Release of Information (ROI) feature.

- Annotations of RAD package images that were made in VistARad are not displayed in Clinical Display and are not printed when printing the image. When printing the image, Clinical Display adds the following text above the printed image: **This image was annotated in VistARad. To view annotation(s) open in VistARad.**

### Printing a Single Image

1. Select a patient’s image.

The appropriate viewer may open depending on User Preference setting.

1. If the viewer that opens is the:
<!-- image -->

<!-- image -->
    - Full Resolution Viewer, click the **Image Report + Print Copy Menu** button  and **Print Image** from the drop down menu or select **Print Image** from the File menu. Radiology Viewer, click the **Print Image** button	from the toolbar or select

**Print** from the File menu.

<!-- image -->

- MUSE EKG viewer, click the **Print** button	.
- Image viewer in the Image List window, select **File | Image Print** from the menu bar.
1. If this is the first time printing an image in this session and if you do not hold the MAG ROI key, you are prompted for an Electronic Signature. Enter your code and click **OK** .

**Note** : If you hold the MAG ROI security key, you are not prompted for an electronic signature for printing or copying. The MAG ROI key is assigned to HIMS ROI Officers.

<!-- image -->

1. In the Accept the Physician Agreement for Downloaded Images dialog box that displays, accept the agreement by clicking **OK** .
<!-- image -->

1. Select a purpose for printing the image from the list provided.
<!-- image -->
2. Click **OK** .
3. Verify the printer selection and click **OK** .
<!-- image -->

### Image Print Options Window

When the “Image Print Options…” menu option is selected, the Image Print Options window will open. In the Image Print Options window, the Image will be previewed (displayed) before being printed. The user can select to view the image in Normal mode or convert to Bitmap (rasterized) mode. After viewing the image as it will be printed, the user can then select the Print button to print the image.

<!-- image -->

When “convert to Bitmap Image” is selected, a bitmap representation (rasterized version) of the

image will be displayed.

<!-- image -->

### Release of Information handle Release requests

**How Clinical Display handles Release of Information requests**

Requests for patient VistA Imaging records are submitted as background processing jobs, handled by the local VIX server. In addition, Release of Information (ROI) clerks can send radiology studies to a designated DICOM CD-writer queue. They can queue multiple ROI requests for processing, monitor their status, and retrieve finished work. Once a request has been completed it is kept on the server for a period of time. Clinical Display downloads finished jobs to the ROI clerk’s local PC when the clerk requests the job from the server. The ROI office can then decide how to furnish the disclosure information to the requestor, for example, by copying

the finished job to a CD disc or by printing the contents to paper. A completed disclosure job consists of the items requested along with a manifest summarizing the work performed.

Clinical Display produces a disclosure product for each submitted ROI job. The disclosure product can include any of the following, depending on content of the request.

- DICOM Studies: If the request contains DICOM images, they are automatically routed to CD-writer queue to produce DICOM media.
- Non-DICOM Artifacts: All other VistA Imaging artifacts are packaged into a zipped file called the Disclosure File.

The Disclosure File contains a manifest identifying the disclosed artifacts along with how the Disclosure File was assembled. The Disclosure File also contains a Disclosure PDF file. The Disclosure PDF file organizes all of the artifacts along with navigation bookmarks. The Disclosure PDF can be opened by a standard PDF viewer. Depending on the request, there may be some files that cannot be added into the Disclosure PDF file because of PDF incompatibility. In those instances, files are copied into to the Disclosure File, alongside the Disclosure PDF. If artifacts contain annotations, the server will burn the annotations into a copy of the artifact and place it into the Disclosure PDF. Annotations on DICOM images are not burned into DICOM images.

**Note** : The DICOM Gateway is used to route radiology studies to a named DICOM CD writer. The CD writers should be named and configured correctly in order for the ROI clerk to see them in the **DICOM CD Writer Queue** list.

The following figure shows the overall processing flow and result of the ROI request.

The Disclosure File (this file is in ZIP format)

The Disclosure PDF File (this is a structured file with bookmark navigation)

The Manifest File

Other files that cannot be added to the

DOistchloesr ufirlesPtDhaFt Fcialennot be

(e.g., WAadVd, eAdVtIo, ethtce.)

DOistchleorsfuilresPthDaFt cFailnenot be (e.g., WaAdVd,eAdVtIo, ethtce.)

Disclosure PDF File

(e.g., WAV, AVI, etc.)

Submit the ROI Job

Produces

Server

The Disclosure Request Job

This job could contain a mixture of VistA Imaging items

that could include

JPG, TIF, BMP, TGA, AVI, DICOM,

PDF, and other types contained in the VistA Imaging

database for the identified patient

DICOM CD-writer Queue

DICOM content is queued to have a DICOM-CD produced

<!-- image -->

The following table shows the file types in VistA Imaging that can be added to the disclosure product.

**Table 1 – VistA Imaging File Types that Clinical Display Handles for ROI Processing**

| **Image File Type**   | **Image Content**         | **Default Object Type**   | **Convertible to PDF format**   | **Routed to**  **DICOM**  **Gateway**   | **Notes**                                                    |
|-----------------------|---------------------------|---------------------------|---------------------------------|-----------------------------------------|--------------------------------------------------------------|
| 756                   | Historical                | XRAY                      | N                               | Y                                       | 756  converted to  .TGA                                      |
| ABS                   | Abstract file             | Still Image               | Y                               |                                         | This file type cannot be disclosed. It is a derivative file. |
| ASC                   | Text file Image extension | Text                      | Y                               |                                         |                                                              |
| AVI                   | Motion Video              | Motion Video              | N                               |                                         |                                                              |
| BIG                   | Xray big file 2000k       | XRAY                      | Y                               | Y                                       |                                                              |
| BMP                   | Bit map file              | Still Image               | Y                               |                                         |                                                              |
| BW                    | Black and White           | BWMED                     | Y                               | Y                                       |                                                              |
| DCM                   | DICOM                     | DICOM  Image              | N                               | Y                                       |                                                              |
| DOC                   | Word Document             | MS Word                   | N                               |                                         |                                                              |
| HTM                   | Web HTML  Document        | HTML                      | N                               |                                         |                                                              |
| JPG                   | Full Color JPEG           | Still Image               | Y                               |                                         |                                                              |
| MPG                   | Motion Video MPEG         | Motion Video              | N                               |                                         |                                                              |
| PAC                   | XRAY  image from PACS     | XRAY                      | Y                               | Y                                       |                                                              |
| PDF                   | Adobe PDF                 | Adobe Document            | Y                               |                                         |                                                              |
| RTF                   | Rich Text Document        | Rich Text                 | N                               |                                         |                                                              |

| **Image File Type**     | **Image Content**                    | **Default Object Type**   | **Convertible to PDF format**   | **Routed to**  **DICOM**  **Gateway**   | **Notes**                                                                                                                                 |
|-------------------------|--------------------------------------|---------------------------|---------------------------------|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| TGA                     | Targa Image Format                   | Still Image               | Y                               | Y                                       |                                                                                                                                           |
| TIF                     | Scanned TIFF  Format                 | Document                  | Y                               |                                         |                                                                                                                                           |
| WAV                     | Audio WAV file                       | Audio                     | N                               |                                         |                                                                                                                                           |
| Patch 34 DICOM  Objects | DICOM SOP  classes from some source. | n/a                       | N                               |                                         | Currently the SOP classes are not supported in a viewer so these objects cannot be displayed.  These will not be disclosed in MAG*3.0*130 |

Users who have MAG ROI or the MAG SYSTEM key can process ROI requests. They can print multiple images, all images for a patient, save the ROI job to a file and send it to a CD burner.

**Printing Multiple Images**

##### To print multiple images:

1. Select a patient.

##### 3 Click Utilities| ROI Print Options | Choose Images to Process.

<!-- image -->

- If you only intend to print a few images, click **None** in the **ROI Multi Image Processing** area in the Image List window, then select the images you wish to print.
<!-- image -->
1. Once you have selected the images you wish to print, click **Continue** . A window will open titled “Process Images for”: &lt;Patient Name&gt;.
2. Select or clear the **Suppress printing of Print Summary** box as desired. The print summary page contains a summary of the print job. If you do not want to print the summary page, check the checkbox **Suppress printing of Print Summary** in the Process Images for: window.
3. Verify that the number of images selected matches the number selected to print as displayed in the Print Images for: window.
4. Click the **Print** button.
5. In the Print dialog box that displays, select the printer and then click **OK** .
<!-- image -->
6. Enter electronic signature, if prompted and click **OK** .

1. If the Accept the Physician Agreement for Downloaded Images window displays, click

**OK** to accept the agreement.

<!-- image -->

1. In the Physician Agreement for Downloaded Images window that displays, select the reason to print the images. Then, click **OK** .
<!-- image -->

The **Image Processing Summary** at the bottom of the Process images for: window shows the status of the processed images.

<!-- image -->

**Printing All Images of a Patient**

##### To print all images of a patient:

1. Select **Utilities | ROI Processing Options| Print all listed images…** Process Images

for:… window opens.

1. A print summary page is printed by default when multiple images are printed. If you do not want to print the summary page, select the checkbox **Suppress printing of Print Summary** in the Process Images for: window. The print summary page contains a summary of the print job.
2. Verify that the image count matches the number of selected images and click **Print** .
3. In the Print dialog box, choose the printer you want to use and click **OK** .
4. Enter electronic signature, if prompted and click **OK** .
5. If the Accept the Physician Agreement for Downloaded Images window displays, click

**OK** to accept the agreement.

1. Select the purpose for which the images are being printed. Then, click **OK** .

The **Image Processing Summary** at the bottom of the Process images for: window shows the status of the processed images.

**Processing ROI Requests**

##### To process an ROI request:

1. Select a patient.

##### 4 Click Utilities| ROI Print Options | Choose Images to Process.

<!-- image -->

<!-- image -->

The Process Images for: window opens.

<!-- image -->

1. Select the **Print the Disclosure** or **To File and CD** tab depending on your needs.
    - Select the **Print the Disclosure** tab to sends the ROI job to the printer.
    - Select the **To File and CD** to save the file to the disk or to send it to a CD writer that is configured and connected to the computer from which you are processing the ROI request. Then go to step 10.
2. In the **Print the Disclosure** tab, select or clear the **Suppress printing of Print Summary** box as desired. The print summary page contains a summary of the print job. If you do not want to print the summary page, check the checkbox **Suppress printing of Print Summary** in the Process Images for: window.
3. Verify that the number of images selected matches the number selected to print as displayed in the Print Images for: window.
4. Click the **Print** button.

1. In the Print dialog box that displays, select the printer and then click **OK** . Then go to step 12.
<!-- image -->
2. In the **To File and CD** tab, choose the CD writer queue from the **DICOM CD Writer Queue list** . The list contains all configured CD writers that are connected to the workstation from which the ROI request is processed.
<!-- image -->
3. Click the **Process ROI Request** button.
<!-- image -->
4. Enter electronic signature, if prompted and click **OK** .

1. If the Accept the Physician Agreement for Downloaded Images window displays, click

**OK** to accept the agreement.

<!-- image -->

1. In the Physician Agreement for Downloaded Images window that displays, select the reason for the disclosure. Then, click **OK** .
<!-- image -->

The **Image Processing Summary** at the bottom of the Process images for: window shows the status of the processed images.

**Note:** If the user changes patients before the previously selected print job is completed, Clinical Display will respond that it cannot change patients at the time. A message will be displayed warning the user that the ROI Report may be incomplete if the patient is changed.

<!-- image -->

This warning is displayed in the message dialog and the user is asked if they want to continue with the Patient Change. The three user choices are: OK, Cancel, or Break Link. **Cancel is the default choice and is the suggested option for the end user.**

**Monitoring the Status of Release of Information Jobs**

ROI clerks can monitor the status of the ROI requests that they have submitted. They can see the status of all ROI jobs they have submitted in the Release of Information Status window.

- To display the Release of Information Status window, in the Image List window, select

##### Utilities | ROI Processing Status.

<!-- image -->

You can sort the jobs in the Release of Information Status window by clicking on a column header. You can sort each column sorts in ascending and descending order.

- If the status of a job is **ROI\_COMPLETE** or **EXPORT\_QUEUE** , this means that the job has been completed on the server.
- **ROI\_COMPLETE** status indicates that job contains non-DICOM artifacts for download and that there may be a DICOM CD ready for pickup if the **DICOM Routing** column displays a location where to pick up the DICOM CD.
- **EXPORT\_QUEUE** status indicates that the job has been completed on the server and that the job only contains DICOM studies.
- The **DICOM Routing column** indicates where to pick up the DICOM CD.

### Printing Images with Annotations

You can print an image with all, some, or none of its annotations. Visible annotations are printed with the image. You can customize the view by hiding or showing annotations. You can also print Annotation history layers. The procedures for printing images with annotations are the same as the ones for printing image with no annotations.

If the image has annotations, the printout has a second line with details about the annotations on the specific page.

<!-- image -->

### Printing Images with Annotations Using the Release of Information Feature

If your user account has the MAG ROI key you, you can print images through the Release of Information (ROI) feature of Clinical Display. In ROI, images you select for printing will print with all annotations that are in the latest history layer.

**Note** : Radiology package images do not print with annotations when creating pages through the ROI feature of Clinical Display.

### Copying an Image

1. Select a patient’s image. The image opens in the appropriate viewer.
2. If the viewer that opens is the:
<!-- image -->
    - Full Resolution Viewer, click the **Image Report + Print Copy Menu** button  and **Copy Image** from the drop down menu or select **Copy Image to Clipboard** from the File menu.
    <!-- image -->
    - Radiology Viewer, click the **Copy to Clipboard** button  from the toolbar or select **Copy** from the File menu
3. If the user preference is set to view image in Image List Window, you can select **Image Copy** from the **File** menu. If this is the first time copying an image in this session you will be prompted for an electronic signature. Enter your code and click **OK** .

**Note** : If you hold the MAG ROI security key, you are not prompted for an electronic signature for printing or copying. The MAG ROI key is assigned to HIMS ROI Officers. You can continue to step 4.

<!-- image -->

1. Accept the Physician Agreement for Downloading Images by clicking **OK** .
2. In the window that displays, select a purpose for copying the image from the list. Then, click **OK** .
3. Click **OK** and then paste the image into your document or graphics editor.

**Note** : The Clipboard is not a part of Clinical Display.

<!-- image -->

The Clinical Display interface can be configured to match the ways you prefer to work. You can:

- Display certain windows when you select a patient
- Display certain viewers when you work with an abstract or document image
- Choose remote image views and connections to remote sites
- Choose viewers for video files and PDFs
- Choose options for displaying the Image List, tree view layout, pointer movement, and mouse selects to open an item
- Choose to always view annotations
- Choose global annotation attributes

### Configuring the Display of Windows for Patient Selection

<!-- image -->

1. From the VistA Imaging Display main window, choose **Options | User Preferences** , or click the **Configure User Preferences** button   on the toolbar in the Image List window.

The Patient Selected tab of the User Preferences dialog box is displayed.

<!-- image -->

1. Select the check box for each window that you want displayed when you select a patient:
    - Abstract window
    - Image List window
    - Radiology Exams window
    - MUSE EKG's viewer window
    - Progress Notes window

**Note** : Click the Save button only when you are finished with all the tabs.

1. Keep the dialog box open and continue.

### Configuring the Abstract and Image Viewers

Shown below is an example of the image abstracts and the non-Radiology Document/Image viewer in the same window as the image list. The Image List can be displayed in the same window as the Abstracts viewer, tree view, list view, Image Reports, and full resolution images inside the Image List window.

If you want this display, you can set it on the Abstract &amp; Image Viewers tab.

<!-- image -->

1. In the User Preferences dialog box, select the Abstract &amp; Image Viewers tab.
<!-- image -->

1. If you select the check box to display abstracts in the Abstract Viewer, then select to display the abstract in the Image List or a separate window.
2. Select to display a non-radiology document or image in the Image List or a separate window.

**Note** : Click the Save button only when you are finished with all the tabs.

1. Keep the dialog box open and continue.

### Configuring Remote Image Views

For information about these options, see *Configuring User Preferences for RIVs* .

### Configuring Alternate Viewer Options

1. In the User Preferences dialog box, select the Alternate Viewer Options tab.
<!-- image -->

1. To play video files, leave the default setting to use the Imaging video player or select an alternate video player.
2. If you chose to use the default video player, select the check box if you want to explicitly select to play the video.
3. For Adobe PDF files, leave the default setting to use the Imaging Viewer or select an Alternate PDF viewer. The Imaging Viewer will not display bookmarks for PDF files. To use bookmark functionality in PDF files you will need to use an Alternate PDF Viewer.

**Note** : Click the Save button only when you are finished with all the tabs.

1. Keep the dialog box open and continue.

### Configuring the Layout Style of the Image List

1. In the User Preferences dialog box, select the Layout Style tab.
<!-- image -->

1. Leave the default setting to show the Image List and select to show the tree view, or clear the **Show Image List** check box and select only **Show Tree View** . The Image List and Tree View can be shown together in the Image List window. If you choose to not show the Image List or the Tree View in the Image List window then clear both check boxes. If the Image List and Tree View are not selected the Image List window will be displayed showing the menu bar, toolbar, and can be configured through the preferences to be display the panes and information that are configurable through the preferences.
2. If you chose to show the Image List, then select if you also want to show a preview of the abstracts and reports.
3. Select an item to change the pointer speed to slow, medium or fast.
4. Click the **Save** button to save all the settings and close the dialog box.

**Important** : Clicking Close cancels all settings you may have added and closes the dialog box.

### Configuring User Preferences for Annotation Options

You can set Global Annotation Attributes from the User Preferences dialog box.

By default, when you display an image, all annotations in the latest history layer are shown. However, you can clear the **Show Annotations With Image When Displayed** check box in the User Preference dialog box to prevent annotations from automatically showing. When you turn off the automatic display of annotations, you can manually show annotations on the currently displayed image by going into annotation mode and using the **Hide/Show** options. For information about viewing annotations, see *Hiding and Showing Annotations* .

To configure user preferences for annotations:

1. From the main Clinical Display menu, select **Options | User Preferences** .
<!-- image -->
2. In the User Preferences dialog box, click the **Annotation** tab.
<!-- image -->
3. Click the **Global Attributes** button on the **Annotation** tab to open the Global Annotation Attributes dialog box.

The Global Annotation Attributes Editor dialog box opens.

<!-- image -->

1. Change the settings as desired. For information about the global annotation attributes, see

*Setting Global Annotation Attributes* .

1. Click **OK** to close the Global Annotation Attributes dialog box and return to the User Preferences dialog box.
2. To save your changes and close the User Preferences dialog box, click **Save** .

## Viewing Patient Images at Remote Sites

<!-- image -->

A patient can have images at a local VA site, remote VA sites, and the DoD Images from remote sites are not stored locally but are retrieved on demand and cached temporarily. You can access a patient's images stored at any remote sites only if the patient has been seen at the local site.

Depending on your configuration settings, your workstation may automatically show images from remote sites, or you may need to connect to a remote site manually before remote images are displayed. The next section explains how to connect manually. The *Configuring User Preferences for RIVs* section explains the configuration options related to remote image views.

### Using Remote Image Views (RIVs)

1. To view an image at a remote site, select a patient.

If Remote Image Views are configured, the Image List displays all the remote sites that the patient visited at the bottom of the window, as shown in the example.

- The sites in **green** are the active (connected) sites for the selected patient and include the number of studies or image groups (displayed in parentheses) that the patient has at that site.

**Note** : Only the sites that have implemented a VIX will be able to click the DoD tab to connect to the DoD.

- Any site in **red** with a line through it is not connected.
<!-- image -->

To connect to the site (in red), click the site name. Once connected, the site name will be shown in green.

The Image List window and the Abstracts window (shown below) display the studies from the remote site. The studies are integrated with the local studies and sorted by procedure date so that the most recent studies (regardless of the location) are displayed at the top.

<!-- image -->

### Partial Results

When retrieving information for a patient who has been seen at a DoD medical facility, Clinical Display presents information from multiple DoD sources. In some situations, Clinical Display will display a message indicating that the results are partial (shown below). This behavior only applies to DoD data.

<!-- image -->

Partial results can be returned due to many possible reasons. For example:

- If one DoD source responds within 30 seconds but another does not, Clinical Display returns the available data with the Partial results indicator.
- If a specific DoD source has so much data it will take a long time to send all of it, Clinical Display may return available information as a Partial result rather than make the user wait for all the information to become available: for example if a patient has multiple radiology images available.
<!-- image -->

If “Partial” appears in the DoD remote site button, you can refresh the patient by clicking the **Refresh Patient Images** button  on the toolbar to retry requesting data from the DoD which might return a full result.

### Configuring User Preferences for RIVs

You can set user preferences for RIVs that determine the behavior of remote image viewing.

1. To access the remote image views user preferences, choose **Options | User Preferences** from the menu bar in the VistA Imaging Display main window, and select the Remote Image View tab shown.
<!-- image -->

1. Select or clear any of the following options:

| **Option**                                              | **Description**                                                                                                                                                                                                               |
|---------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Remote Image Views Auto-Connect Enabled                 | If this option is selected, Clinical Display automatically connects to all remote sites where the patient has been seen.  **Note**  : This option might slow down viewing patient data.                                       |
| Only Auto-Connect to Sites in Local VISN                | When selected, the auto connect option applies only to sites in your local VISN.                                                                                                                                              |
| Auto-Connect to the DoD                                 | When selected, Clinical Display automatically connects to the DoD when a patient who has been seen at the DoD is selected.  **Note**  : This option might slow down viewing patient data.                                     |
| Hide ‘Patient Active’ Sites with 0 Images on Toolbar    | When selected, the Remote Image Views toolbar in the Image List window will not show sites that the patient visited if the patient has 0 studies at that site. This could be useful if a patient has been seen at many sites. |
| Hide Disconnected Sites For Selected Patient on Toolbar | When selected, the Remote Image Views toolbar displays only connected sites for the selected patient. Disconnected sites are not displayed on the toolbar.                                                                    |

| **Option**               | **Description**                                                                                                                                       |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Display Remote Abstracts | When selected, the Clinical Display client displays abstract images from remote sites.  **Note**  : This option might slow down viewing patient data. |

1. Click **Save** and **Close** .

### Configuring Your Connection to Remote Sites

If you want to disconnect from one or more of the remote sites, follow these steps:

<!-- image -->

1. Choose **Options | Remote Image Views Configuration** from the menu bar, in the VistA Imaging Display main window or in the Image List window or click the **Remote Image Views Configuration** button  on the toolbar.

The Remote Image Views Configuration window opens.

<!-- image -->

| **Column Name**   | **Description**                                                                                                                                                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Site Name         | Location of the VA site or DoD site                                                                                                                                                                                                                       |
| Site Code         | Code representing the site                                                                                                                                                                                                                                |
| Status            | Status can be one of the following:  Patient Active - Site is connected and the patient has images at the site.  Inactive - Site is disconnected and the patient does not have images at the site.  Disconnected - Connection not established to the site |
| Image Count       | Total number of image and image groups at the site for the patient                                                                                                                                                                                        |

1. Select one or more sites and choose one of the following options:
    - Click **Disconnect** to disconnect from the selected site(s).
    - Click **Disconnect All** to disconnect from all connected sites.

1. Click **Close** when you are finished.

## Editing the Image Index Entries

<!-- image -->

**Note** : You can access this utility only if you hold the **MAG EDIT** or **MAG SYSTEM** security key.

When images are captured, they are indexed, as shown in the example. If they are indexed incorrectly (for example, a Teledermatology image is indexed as a cardiology image), you can use the Image Index Edit Utility to edit or add values to correctly index the image. The Index Edit Utility edits the index fields of an image group or single image.

The Image Index Edit utility can be used from the Image List window or the QA Review window.

### Image Index Edit Window

<!-- image -->

**Menu Bar in the Image Index Edit Window**

File Menu

| **Menu Option**   | **Description**                                    |
|-------------------|----------------------------------------------------|
| Save              | Save is the same as the  **OK**  button.           |
| Exit              | Exit will close the window without saving changes. |

Options Menu

| **Menu Option**    | **Description**                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Initial Values     | Initial Values: will populate all enabled fields with the initial value of the field. |
| Clear Fields       | Will clear all enabled fields.                                                        |
| Include All Fields | Include All Fields: Will enabled all fields.                                          |
| Exclude All Fields | Exclude All Fields: will disable all fields and discard any changes.                  |

Help Menu

| **Menu Option**   | **Description**                                                        |
|-------------------|------------------------------------------------------------------------|
| Index Edit Help   | Index Edit Help: will bring up the On-Line help topic for this window. |

### Editing Index Fields

**Note** : When you edit an index on a group of images, the images within the edited group are not automatically updated or changed. You will have to edit each image if changes need to be made in the way that the images were indexed.

1. To use the Image Edit Index Utility from the QA Review Utility, select **File | Image Index Edit** .

The utility is also available from the *Image List Window* .

<!-- image -->

The Image Edit Index window opens.

<!-- image -->

1. Select the check box next to the Index field that you need to change. The drop-down list for the selected Index term is activated.
2. To select all the indexes, select **Options | Include All Fields** or exclude all indexes, select **Exclude All Fields** .
3. Select the drop down list for the index term and click the correct term from the list. You can update as many Indexes as you need to.
4. Click **OK** or select **File | Save** to update the Image Index.

The Image Index Edit window closes and a Confirm window is displayed, as shown in this example confirming that the Origin is changed to "VA".

<!-- image -->

1. Click **OK** to make the changes or **Cancel** .

Clicking OK makes the selected changes to the image index. If you click Cancel, the Confirm window closes and no changes are made to the image index.

<!-- image -->

<!-- image -->

**Note** : If you change and accept the change for any of the index fields, a Refresh icon  is displayed in the Image List window. You will need to refresh the images by clicking the **Refresh Patient Images** button  on the toolbar.

## Checking Quality Assurance on Images

<!-- image -->

**Note** : You must hold the **MAG EDIT, MAG QA REVIEW,** or **MAG SYSTEM** security keys.

The Quality Assurance (QA)) Utility enables authorized users to review a sampling of images acquired into VistA Imaging through the Capture Client or the Import API, or both. This utility verifies that:

- Images captured in VistA Imaging are assigned to the correct patient
- Indexes of the images were set correctly when the images were captured
- Images meet locally or nationally defined quality standards

During the review process, you can change image index values using the Index Edit Utility (see chapter *Editing the Image Index Entries* ) for image groups and single images captured by the Capture Workstation and Import API. As previously mentioned, an *image group* is a collection of related single images of the same or mixed formats. Saved *Single images* are not part of an image group.

**Note** : Images captured by the DICOM Gateway and images within a group are not listed for QA Review.

### QA Review Window

The QA Review window can be accessed through: **Utilities| QA Review** .

<!-- image -->

**Menu Bar in the QA Review Window**

File Menu

| **Menu Option**            | **Description**                                                                                                                                                |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Image Delete               | Users with the correct security Keys can delete an image.                                                                                                      |
| Image Index Edit           | The Image Index Edit window opens. The Image Index values can be edited there. If edits are made, the status Button will change to show an edit has been made. |
| Image Information Advanced | Users with the correct security key have access to this menu option.                                                                                           |
| Exit                       | Close the QA Review utility window.                                                                                                                            |

Options Menu

| **Menu Option**     | **Description**                                                                                                       |
|---------------------|-----------------------------------------------------------------------------------------------------------------------|
| Refresh List        | Refreshes the filtered image list.                                                                                    |
| Clear all           | Clears the form.                                                                                                      |
| Select Columns      | Opens the columns select form. User can select which columns to view.                                                 |
| Fit to Text         | Fit the width of the columns to the longest text in each.                                                             |
| Fit to Window       | Space the columns so that all are visible in the image list.                                                          |
| Preview Report      | If selected, the report pane will be visible and will display the associated report of the image if one exists.       |
| Preview Image Info  | If selected, the information pane will be visible and information on the selected image will be displayed.            |
| QA Review Report    | Opens the QA report utility window. (see QA Report section)                                                           |
| Shortcut Key legend | Opens the Shortcut Key Legend window, which describes all shortcut keys that are in effect for VistA Imaging Display. |
| Message Window      | Opens the Imaging Session Message History window.                                                                     |

Filter Menu

| **Menu Option**    | **Description**                                                                                                                               |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Image List Filters | Opens the Image Filter Add/Edit window. User can Create, Edit or Select an image filter. If a filter is selected, its name will be displayed. |

| **Menu Option**                             | **Description**                                                                                                                                      |
|---------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Filter Details                              | Opens an Information window that shows details of the current filter.                                                                                |
| Quick Search Panel                          | Opens the quick search pane. The Quick search pane has the new search properties that will be available to verifying personnel.                      |
| Search Images captured by VI Capture Client | When selected the quick search will include all of the images for the date range selected that were captured using the VistA Imaging Capture client. |
| Search Images captured by VI Import API     | When selected the quick search will include all of the images for the date range selected that came in via the VistA Imaging Import API.             |

Image Menu

| **Menu Option**   | **Description**                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Zoom              | Zoom has the following options:  - Zooms In - to zoom in to an image - Zoom Out - to zoom out of an image - Fit to Width - to fit the image to the window width (horizontal) - Fit to Height - to fit the image to the height of the window (vertical) - Fit to Window - to fit the image to the entire window (vertical and horizontal) - Actual Size - to show image in its original size |
| Mouse             | Mouse has the following options:  - Pan - to pan image by dragging mouse - Magnify - to magnify an image where the mouse is clicked - Zoom - to zoom into an area of the image selected with the mouse - Pointer - to go back to mouse pointer                                                                                                                                              |
| Rotate            | Rotate has the following options:  - Right - Rotates the image 90 degrees clockwise - Left - Rotates the image 90 degrees counterclockwise - 180 - Rotates the image 180 degrees - Flip Horizontal - Flips the image horizontally - Flip Vertical - Flips the image vertically                                                                                                              |

| **Menu Option**     | **Description**                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Contrast/Brightness | Contrast/Brightness has the following options:  - ‘Contrast +’ - Increases the contrast of an image - ‘Contrast –‘ - Decreases the contrast of an image - ‘Brightness +’ - Increases the brightness of an image - ‘Brightness –‘ - Decreases the brightness of an image                                                                                                            |
| Invert              | Reverses the colors of the image.                                                                                                                                                                                                                                                                                                                                                  |
| Reset               | Resets the currently selected image to its original display settings including zoom, contrast, window brightness, and orientation.                                                                                                                                                                                                                                                 |
| Scroll              | Scroll has the following options:  - Top Left - scroll to the top left corner of the image - Top Right - scroll to the top right corner of the image - Bottom Left - scroll to the bottom left corner of the image - Bottom Right - scroll to the bottom right corner of the image - Left - scroll to the left - Right - scroll to the right - Up - scroll up - Down - scroll down |
| Maximize Image      | Resize image to fill the entire window.                                                                                                                                                                                                                                                                                                                                            |
| Next Image          | Displays the next image.                                                                                                                                                                                                                                                                                                                                                           |
| Previous Image      | Displays the previous image.                                                                                                                                                                                                                                                                                                                                                       |

Action Menu

| **Menu Option**           | **Description**                                                                                                                                                                                                   |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Image Status QA Reviewed  | Changes the status of the image to QA Reviewed. When the status of an image is changed the list button will change to a 'Refresh needed' button. This indicates that a change has been made to the listed image.  |
| Image Status Needs Review | Changes the status of the image to Needs Review. When the status of an image is changed the list button will change to a 'Refresh needed' button. This indicates that a change has been made to the listed image. |
| Next                      | Selects the Next image in the list. When 'Next' is selected the status of the current image is not changed. The next image in the list will be displayed in the Image Viewer.                                     |
| Previous                  | Selects the Previous image in the list. When ‘Previous’ is selected the status of the current image is not changed. The previous image in the list will be displayed in the Image Viewer.                         |

Help Menu

| QA Review Help   | Opens the What’s New in Patch 93 document.   |
|------------------|----------------------------------------------|

### Applying Advanced Filters to the QA Review

**Note** : You must hold the **MAG EDIT** or **MAG SYSTEM** security key.

1. In the QA Review window choose **Filter | Image List Filters** and after the Image Filter Add/Edit window opens select a filter from the list.

The Image Filter Add/Edit window opens.

<!-- image -->

1. Select the General properties tab in the lower part of the window.
<!-- image -->

1. Click the **Clinical** button for the class of image and specify the date range and origin of the image.

**Note** : Specifying the Clinical class adds the Clinical properties tab to the lower part of the window.

1. Select the Clinical Properties tab and configure the properties that will be included in the filter.
<!-- image -->
2. Select the Advanced properties tab.
<!-- image -->
3. Set any of the following options:
    - Use Capture Date for Date Range: If the ‘Use Capture Date for Data Range’ check box is selected then the filter will search the Date Range (selected on the ‘General Properties’ tab) by using the Date/Time the Image was saved to the database. If cleared the date used for the date range is the Procedure/Exam Date /Time. (The procedure/exam data time is the default date used).
    - Description contains: If the ‘Description Contains’ field has any text in it, then only

images that have that text (anywhere in the short description) will be returned.

- Image Status: The Image Status Field in the Image File has the following values

‘Viewable’, ‘Verified’, ‘In Progress’ and ‘Needs Review’.

- Image Saved by: You can select the person who captured the images, and only images captured by that person (and satisfying all other properties) will be returned.

<!-- image -->

<!-- image -->

1. Click the **Save** button		at the bottom of the window to save the filter, or click the **Save As** button	to save the filter to another name.

### Selecting an Existing Filter for the QA Review Queries

When you select a filter a list of all images and image groups that match the filter are displayed in the QA Review window. The list of images returned when a filter is used will be limited by the dates specified in the filter parameters. If no dates are specified then the filter will return all of the images for the QA Review that match the filter.

**Note** : The Quick search button will be enabled only after all values are selected.

1. From the QA Review window, choose **Filter| Image List Filters** from the menu bar.

1. Select a Private or Public filter from the list of filters and click **OK** .
<!-- image -->
2. Continue to the procedure *Performing the QA Review* .

### Specifying the QA Review Parameters

1. From the VistA Imaging Display main window or the Image List window, choose

**Utilities | QA Review** from the menu bar to open the QA Review window.

<!-- image -->

1. Select the date range by clicking the drop down list.

If you select **&lt;select date range&gt;** , select a From and To date from the date window displayed. Select the desired date range.

<!-- image -->

<!-- image -->

1. Click the **Captured by** button to refresh the drop down list to display the users who captured images within the specified date range, and then select a user from the list.

<!-- image -->

<!-- image -->

1. Click the **Status(s)** button  to further limit images that are returned.

1. Select the status(s) that you want returned by moving the statuses to the Selected Values list in the Status Selection window displayed. Click **OK** to continue or **Cancel** to close the Status Selection window.
<!-- image -->
2. For the specified date range and user selected, select either:
    - The percentage to return by selecting a number from the drop down list, or by typing a numerical value in the field, or
    - The maximum number of images to return by selecting a number from the drop down list or by typing a numerical value in the field.
    <!-- image -->

<!-- image -->

1. Click the **Quick Search** button  to begin the search.

The search results are displayed in the QA Review window, as shown.

<!-- image -->

### Performing the QA Review

Within your search results, review the data based on the following QA requirements:

- Images captured in VistA Imaging are assigned to the correct patient
- Indexes of the images were set correctly when the images were captured
- Images meet locally or nationally defined quality standards
    1. Select an image from the list shown in the example.
    <!-- image -->
    1. Examine the image in the right pane using the buttons in the toolbar above the image to manipulate the image if necessary.
    2. Review the Image Information and Image Report in the panes on the left.
    <!-- image -->
    3. If the image meets the QA review requirements, click the QA Reviewed button  .
    4. In the same manner, review each item in the list.
<!-- image -->

<!-- image -->
    1. Click the **Next** button     or the **Previous** button  to move forward or backward in the list.**Note** : If an image does not meet the QA review requirements, then the image must be marked as Needs Review.
    1. To mark an image with a status of **Needs Review** , follow steps 1 through 3 above and then either.
        - Select **Action** from the menu bar and select **Image Status =&gt; Needs Review**
        - Use the shortcut by pressing CRTL+ALT+R.
    2. Select the **Reason for Status Change.**
    <!-- image -->

<!-- image -->
The Image List is updated with the    icons. When a refresh of the Image List occurs, the image will have the	icon next to it.
**Performing QA Review on a Single Image within a Group**
When a group of images is selected in the QA Review window:
    - The number of images in that group are indicated by the number in the # Img column, and
    - All the images in that group are shown in the bottom right portion of the window.
    <!-- image -->
To change the status of an image within the group:
    1. Select an image by clicking the abstract at the bottom right in the QA Review window
    2. Click **QA Reviewed** on the left, or in the main menu
    3. Select Image Status| QA Reviewed
    4. To mark an image as “Needs Review” select **Image Status| Needs Review** from the main menu
**Images with Incorrect Index Values**If an image does not meet the QA Review requirements due to incorrect index values, you can edit the image index values using the Image Index Edit utility explained in the chapter *Editing the Image Index Entries.* After correcting the index values for the image so that it meets the QA review requirements, you can mark the image as **QA Reviewed** .
**Running the QA Review Report****Note:** you must have MAG SYSTEM, MAG EDIT or MAG QA REVIEW security keys to run the QA Review Report.
The QA Review Report returns reports based on the search criteria entered in the QA Statistics Report window and contains the following information:
    - Image counts by users and image status. It also returns the QA Review Status of images and QA Review percentages for the selected date range.
    - Images captured by each user in the selected date range.
    - Number of image entries per each image status.
    - Number of multi-page images (in the pages column).
    - Percentage of captured images that have been marked as QA Reviewed for the selected date range.
To run the QA Review Report:
    1. Do either of the following:
        - In the VistA Imaging Display main window, click **Utilities| QA Review Report**
        <!-- image -->
        - In the Image list window, click **Utilities| QA Review Report**
    2. In the QA Statistics Report window, select the items you want included in the report. You can choose:
        - Date range
        - Deleted images
        - Existing images
        - Run reports by status
    - Run reports by users and status
    <!-- image -->
    <!-- image -->
    1. Click Run Report. The new reports will be listed in the QA Statistics Report window.
QA Statistics Reports Options Menu
The Menu Bar Options are displayed below: File:
<!-- image -->
Action:
<!-- image -->
<!-- image -->
Options:
Help:
<!-- image -->
    1. To open the desired report:
        - Double-click the report column, or
        <!-- image -->
        - Select the report and click the **View Report** button under the list of reports.
***Menu Bar in the QA Review/Image Status Report***
File Menu
| **Menu Option**     | **Description**                                           |
|---------------------|-----------------------------------------------------------|
| Save As             | Saves the report data as a Comma Separated Value file.    |
| Open in Spreadsheet | Saves the file in a CSV Format and also open in MS Excel. |
| Exit                | Closes the window.                                        |
Options Menu
| **Menu Option**   | **Description**                                                                                                                   |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Active Forms      | Opens a window that lists all the active forms in the application. You can easily switch to a form by selecting if from the list. |
| Stay on Top       | Keeps the QA Review report open on top of the active windows.                                                                     |
Help Menu
| **Menu Option**   | **Description**                        |
|-------------------|----------------------------------------|
| Image Reports     | Opens the help topic on Image reports. |

## Displaying Reports

<!-- image -->

You can display reports in two ways:

- By using the Reports menu on the menu bar in the Image List window. The reports that are available are the:
- Health Summary (select one from the Health Summary window)
- Discharge Summary (select one from the Discharge Summaries window)

### Report Window

The report window dynamically displays all image reports and patient reports.

<!-- image -->

**Menu Bar in the Report Window**

File Menu

| **Menu Option**   | **Description**                                                                                                                                      |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| New Report Window | Open a new report window to view multiple reports at the same time. Reports will overwrite each other if more than one is opened in the same window. |
| Font              | Opens the Font window. Enables you to strikeout or underline text and change the font, font style, size, script, and color.                          |
| Print             | Opens the Print window.                                                                                                                              |
| Print Setup       | Opens the Print Setup window.                                                                                                                        |

| **Menu Option**   | **Description**           |
|-------------------|---------------------------|
| Exit              | Closes the report window. |

Help Menu

| **Menu Option**   | **Description**                                                |
|-------------------|----------------------------------------------------------------|
| Image Reports     | Displays the online help for viewing associated image reports. |

### Image Report

1. From the Image List, Tree View or Abstracts window, right-click an image row or abstract to display the popup menu.
2. Select the Image Report from the menu.

The Image report contains the long description for the image followed by the clinical report. If a report is not available a No Report Available dialog is shown.

<!-- image -->

1. On the File menu, select any option to change the font, set printer options, and to print.

### Patient Profile

1. From the VistA Imaging Display main window or the Image List window, choose

**Reports | Patient Profile** from the menu bar to display the report.

<!-- image -->

1. On the File menu, select any option to change the font, set printer options, and print.

### Health Summary

1. From the VistA Imaging Display main window or the Image List window, choose

**Reports | Health Summary** from the menu bar.

<!-- image -->

1. Select a **Health Summary report** from the list and click the **Open** button. The report is displayed.
<!-- image -->
2. On the File menu, select any option to change the font, set printer options, and print.

### Discharge Summary

1. From the VistA Imaging Display main window or the Image List window, choose

**Reports | Discharge Summary** from the menu bar. The Discharge Summary report is displayed.

<!-- image -->

<!-- image -->

1. Click the **Reset Column Width** button  to reset the column widths.

<!-- image -->

1. Select the Health Summary report from the available list and click the **View Report** button . The report is displayed. If images accompany the report, you can view them by clicking the camera button in the Discharge Summaries window.
<!-- image -->
2. On the File menu, select any option to change the font, set printer options, and print.

## Appendix A: Shortcut Key Legend

<!-- image -->

### Full Resolution Viewer and Radiology Viewer

| Shift+Ctrl+S           | Reset Image to initial setting   |
|------------------------|----------------------------------|
| Shift+Ctrl+I           | Zoom In                          |
| Shift+Ctrl+O           | Zoom Out                         |
| Shift+Ctrl+W           | Fit Image to Width               |
| Shift+Ctrl+A           | Zoom Image to Actual Size        |
| Shift+Ctrl+Left arrow  | Scroll Left                      |
| Shift+Ctrl+Right arrow | Scroll Right                     |
| Shift+Ctrl+Up arrow    | Scroll Up                        |
| Shift+Ctrl+Down arrow  | Scroll Down                      |
| Shift+Ctrl+HOME        | Scroll to Top Left               |
| Shift+Ctrl+PgUp        | Scroll to Top Right              |
| Shift+Ctrl+PgDown      | Scroll to Bottom Right           |
| Shift+Ctrl+End         | Scroll Bottom Left               |
| Shift+Ctrl+J           | More Contrast                    |
| Shift+Ctrl+K           | Less Contrast                    |
| Shift+Ctrl+N           | More Brightness                  |
| Shift+Ctrl+M           | Less Brightness                  |
| Shift+Ctrl+R           | Rotate Right 90 degrees          |

**Image Viewer**

| Ctrl+Alt+P   | Previous Page Images   |
|--------------|------------------------|
| Ctrl+Alt+N   | Next Page Images       |
| Ctrl+P       | Previous Image         |
| Ctrl+N       | Next Image             |

### Image List Window

| Ctrl+F5   | Active Control: Abstracts   |
|-----------|-----------------------------|
| Ctrl+F6   | Active Control: Tree View   |

| Ctrl+F7   | Active Control: List View       |
|-----------|---------------------------------|
| Ctrl+F8   | Active Control: Full Resolution |

**Radiology Viewer**

| Ctrl+P      | Previous Image       |
|-------------|----------------------|
| Ctrl+N      | Next Image           |
| Ctrl+F      | First Image          |
| Ctrl+L      | Last Image           |
| Ctrl+C      | Cine Tool Focus      |
| Shft+Ctrl+D | More Window Value    |
| Shft+Ctrl+F | Less Window Value    |
| Shft+Ctrl+C | More Level Value     |
| Shft+Ctrl+V | Less Level Value     |
| Shft+Ctrl+Y | Start Stack Cine     |
| Shft+Ctrl+T | Stop Stack Cine      |
| Shft+Ctrl+G | Slow Down Stack Cine |
| Shft+Ctrl+H | Speed Up Stack Cine  |

### Cine Viewer

| Ctrl+C   | Switch to Radiology Viewer   |
|----------|------------------------------|

**Abstract Windows**

| Ctrl+O     | Smaller Abstracts       |
|------------|-------------------------|
| Ctrl+I     | Larger Abstracts        |
| Ctrl+Alt+P | Previous Page Abstracts |
| Ctrl+Alt+N | Next Page Abstracts     |
| Ctrl+P     | Previous Abstract       |
| Ctrl+N     | Next Abstract           |

### Page Functions

| Ctrl+Alt+Left Arrow   | Go to First Page    |
|-----------------------|---------------------|
| Ctrl+Alt+Down Arrow   | Go to Previous Page |

| Ctrl+Alt+Up Arrow    | Go to Next Page   |
|----------------------|-------------------|
| Ctrl+Alt+Right Arrow | Go To Last Page   |

**Activate Windows**

| Ctrl+L   | Image List Filters                      |
|----------|-----------------------------------------|
| Ctrl+M   | Go to VistA Imaging Display main window |
| Ctrl+W   | Switch to an active window              |
| Alt+F6   | Switch to the last active window        |

### Focus in Any Window

| Ctrl+T     | Hide/Show Toolbar        |
|------------|--------------------------|
| Ctrl+R     | Refresh Abstracts/Images |
| Ctrl+Alt+M | Open Popup Menu          |

**Help Topics**

| F1   | Open Help for the current control   |
|------|-------------------------------------|

### Menu Option Access

| Alt+SPACE   | System menu for the window   |
|-------------|------------------------------|

**Closing Dialog Boxes**

| Alt+F4   | Close the Active Window   |
|----------|---------------------------|

**Popup Menu Shortcuts**

| Mouse +Right-Click   | Abstracts Window                                                                                          |
|----------------------|-----------------------------------------------------------------------------------------------------------|
| Ctrl+Shift+M         | Group Abstract Window Full Resolution Window Image List Window Radiology List Window  Image Filter Window |

## Appendix B: Clinical Display Security Keys

<!-- image -->

**Note** : Functionality is restricted to protect VistA from unauthorized access and to comply with HIPAA Regulations.

All users of Clinical Display hold one or more security keys that correspond to their access level and the work they will perform. Each security key unlocks application functionality.

| **Security Key**   | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MAG ANNOTATE MGR   | Enables the holder to modify and delete annotations to images. Only users with this key can make changes to saved annotations.                                                                                                                                                                                                                                                                                                                                  |
| MAG DELETE         | Enables the holder to delete images from the IMAGE file (#2005). Pointers in parent packages such as Medicine, Surgery, Lab, Radiology, and TIU are also deleted.  **Note**  : See also  *Appendix C: Deleting Images.*                                                                                                                                                                                                                                         |
| MAG EDIT           | Enables the holder to edit an image. Used to correct an image field when an index field is selected that is incorrect or incomplete (such as correcting a wrong specialty).  Enables the holder to access the QA Review Utility when performing quality assurance reviews of the captured images.  **Note**  : Only the Chief of HIMS, or authorized designated personnel (i.e., VistA Imaging Coordinator or Scanning Supervisor) should be assigned this key. |
| MAG PAT PHOTO ONLY | Enables a user to view the patient photo only and gives the user no other functionality.  <!-- image -->  For details on how to perform a patient lookup, see  *Selecting a Patient.*                                                                                                                                                                                                                                                                           |
| MAG PREFETCH       | Enables the holder to "prefetch" or queue all images for a patient. This means that all images for a patient that are on the jukebox will be copied from the jukebox to the magnetic server cache.                                                                                                                                                                                                                                                              |
| MAG QA REVIEW      | User can access QA Review and QA Review Report from Clinical Display Utilities Menu.                                                                                                                                                                                                                                                                                                                                                                            |
| MAG RAD SETTINGS   | Enables the holder to edit the CT Presets in the Clinical Imaging Display Radiology Viewer window.                                                                                                                                                                                                                                                                                                                                                              |

| **Security Key**   | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MAG ROI            | Enables users to submit ROI requests, print (single or multiple) images or to copy images without having to enter an electronic signature. This key should only be assigned to the HIMS Release of Information Officer.  Users of this key can also get statistics about the current ROI requests and view their processing status by accessing the ROI Statistics page.                                                                                                  |
| MAG SYSTEM         | Enables the holder to modify site parameters using the Background Processor or to modify workstation parameters using the MAGSYS application. Also enables the display of DICOM header data for radiology images on Clinical Display workstations.  **Note**  : This is for personnel managing VistA Imaging Systems.  Enables users to submit ROI requests and to monitor the status of ROI requests and to modify the configuration of the VIX related to ROI requests. |
| MAGDISP ADMIN      | Enables the holder to display administrative images/documents.                                                                                                                                                                                                                                                                                                                                                                                                            |
| MAGDISP CLIN       | Enables the holder to display clinical images/documents.                                                                                                                                                                                                                                                                                                                                                                                                                  |

## Appendix C: Deleting Images

<!-- image -->

**Note** : You must hold the MAG DELETE security key.. If you do not hold the security key and you attempt to select the Image Delete menu option, the following message will be displayed instead of the Image Delete window.

<!-- image -->

**Note:** Image deletion can occur on a single image or a group of images.

### When an Image Is Deleted

The system performs the following tasks when you delete an image:

- The name of the user, reason for deletion and the date/time are saved to the IMAGE file (#2005).
- The entry in the IMAGE file (#2005) is copied to IMAGE AUDIT file (#2005.1) The entry in IMAGE file (#2005) is then deleted.
- If the image was associated with a clinical report, i.e. Lab or Radiology, then the Image Pointer is deleted from the associated file.
<!-- image -->

<!-- image -->

<!-- image -->
- When an image is deleted the Image List is updated with the   icon in the item column. Refreshing the Image List removes the deleted images from the list.

| Deletion of the image from the Image Share is performed by the Background Processor, not by each individual workstation, so that the actual deletion of the image from the Image Share might be delayed.   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Deleting an annotated image permanently disassociates all its annotations and the annotation history from the image.                                                                                       |

### Image Delete Window

<!-- image -->

**Menu Bar in the Image Delete Window**

File Menu

| **Menu Option**   | **Description**                                                                                                                                                                              |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Delete            | Deletes the image if a Reason for Deletion has been entered. If no Reason for Deletion has been entered a Confirm panel is displayed stating that a reason is needed for deleting the image. |
| Exit              | Cancels and closes the Image Delete window and displays a Cancellation confirmation.                                                                                                         |

Options Menu

| **Menu Option**   | **Description**                                                             |
|-------------------|-----------------------------------------------------------------------------|
| Image Report      | Displays the Image Report in the text area of the Image Delete window.      |
| Image Text File   | Displays the Image Text File in the text area of the Image Delete window.   |
| Image Information | Displays the Image Information in the text area of the Image Delete window. |
| Clear             | Clears the text area in the text area of the Image Delete window.           |

| **Menu Option**                                                    | **Description**                                                                                               |
|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Copy Image (before Delete) for Re- Association in Clinical Capture | Copy the Image to a local user directory so the image can be re- imported to correct patient or index values. |

Copy Image (before Delete) for Re-Association in Clinical Capture

This option is intended to alleviate the cumbersome process that was previously needed when an image was attached to the incorrect patient, or incorrect TIU note. Sites will no longer have to print the image, take it to the scanning clerks, have the image scanned and attached to the correct patient and/or correct TIU Note. This menu option will copy an image to a local user directory before the image is deleted. HIMs personnel can then use Clinical Capture to import the image from the local user directory to a new patient, or to the same patient and different index values.

Note: Image Groups and DICOM Study Groups cannot be copied as a Group. For Image Groups (Non-DICOM), select each image for deletion from the Group Abstract window, then copy each image before deletion.

DICOM Study Groups need to be re-associated through the DICOM Gateway. Help Menu

| **Menu Option**                  | **Description**                                                                                                                                                                                                                                                |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VistA Imaging Display User Guide | This is a link to the Display User Guide on the VistA Imaging SharePoint site. When selected, the User Guide will open in the browser.  For I.H.S sites, the link can be changed in the IMAGING SITE PARAMETERS File (#2006.1), in the DISPLAY HELP URL field. |

**Toolbar in the Image Delete Window**

| **Button**                                                                      | **Description**                                                           |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| <!-- image -->  Display the Report associated with the image in the text area . | Displays the Image Report in the text area of the Image Delete window.    |
| <!-- image -->  Display the Image. Text file in the text area  .                | Displays the Image Text File in the text area of the Image Delete window. |

| **Button**                                                        | **Description**                                                             |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <!-- image -->  Display the Image Information in the text area  . | Displays the Image Information in the text area of the Image Delete window. |

### Deleting Single Images

The image abstract is displayed in the upper left corner when a single image is selected. Image information is displayed in the text pane positioned in the upper right corner. The associated report can be displayed in the text pane.

This section describes the steps to delete an image that does not have annotations. To delete images with annotations, see the section *Deleting A Single Image With Annotations* .

##### To delete a single image:

1. Right-click the image in the Abstracts window or the Image List window from the Image List or Tree View.
2. Select **Image Delete** from the popup menu.

The Image Delete window opens. You can look at the image report, .TXT information, or image Information.

<!-- image -->

1. To view the Image Report in the text pane, choose **Options | Image Report** or click the **Display the Report associated with the image in the text area** button .
<!-- image -->
2. To view the associated Image Text File in the text pane, choose **Options | Image Text File** or click the **Display the Image Text file in the text area** button.
<!-- image -->
3. To view information about the image in the text pane, choose **Options | Image Information** or click the **Display the Image Information in the text area** button .
4. To view the group abstracts for the image, click the **Open the Abstracts window**
<!-- image -->

button .

1. To remove all information from the text pane, choose **Options | Clear** .
1. In the Image Delete window, select a **Reason for Deletion** from the drop-down list and click OK.

The image is deleted and you get an information dialog box informing you that the image was deleted.

### Deleting Image Groups

The abstracts for the images in the group are displayed under the group abstract to the left of the window. The number of images contained in the group is displayed in the delete prompt.

This section describes the steps to delete an image group that does not have annotations. To delete an image group with annotations, see the section *Deleting an Image Group With Annotations* .

##### To delete an image group:

1. Right click the image group in the Abstracts window or the from the Image List window.
2. Select **Image Group Delete** from the popup menu. The Image Delete window opens.
<!-- image -->
3. In the Image Delete window, select a **Reason for Deletion** from the drop down list and click **OK** to delete the image group.

If the image group is deleted is and an information dialog box displays informing you that the image group was deleted.

### Deleting Images with Questionable Integrity (QI Issues)

Abstracts of images with QI issues are not displayed. An "ID mismatch" icon is displayed instead, as shown in the example. When you select this icon, the image and associated report are not displayed. Instead, an error message describing the QI issue is shown.

<!-- image -->

An Error message describing the QI issue is displayed instead.

<!-- image -->

In the Image Delete window the QI image abstract and the associated report are displayed. The description of the issue is displayed in the delete prompt and you can view the image abstract, image information, and image report before deleting the image.

<!-- image -->

### Deleting Images With Annotations

Deleting an annotated image must be done with care. Deleted images can be restored if deleted in error. Deleting an annotated image permanently disassociates all its annotations and the annotation history. Even if the deleted image is restored, restoring the link to its annotations along with the annotation history is not possible.

That is why when you attempt to delete an annotated image, Clinical Display lets you put it in a Needs Review state, which sends the image to QA Review instead of deleting it. When an annotated image is in Needs Review state it is only available for QA Review. It is not available to other users.

**Deleting A Single Image With Annotations**

To delete a single image with annotations:

1. Right-click the image in the Abstracts window or the Image List window from the Image List or Tree View.
2. Select Image Delete from the popup menu.
<!-- image -->

A dialog box displays informing you that deleting the image will delete the annotations and the annotation history.

1. To delete the image:
    1. Click **Delete** in the Confirm dialog box.
    2. In the Image Delete window, select a **Reason for Deletion** from the drop down list and click **OK** .

This deletes the image, the annotations and the annotation history. An information dialog box displays informing you that the image was deleted.

1. To send the image for QA review:
    1. Click **Needs Review** in the Confirm dialog box.
    <!-- image -->
    2. In the Reason for Status Change dialog box that displays, select the reason the image needs to be reviewed. Then, click **OK** .

An information dialog box displays informing you that the status of the image changed to Needs QA Review.

1. To close the Confirm dialog box without making any changes, click **Cancel** .

**Deleting an Image Group With Annotations**

To delete an image group with annotations:

1. Right-click the image group in the Abstracts window or the Image List window from the Image List or Tree View.
2. Select **Image Group Delete** from the popup menu.
<!-- image -->

A dialog box displays informing you that deleting the image group will delete the annotations and the annotation history.

1. To delete the image group:

1. Click **Delete** in the Confirm dialog box.
2. In the Image Delete window, select a **Reason for Deletion** from the drop down list and click **OK** .

This deletes the image group, the annotations and the annotation history. An information dialog box displays informing you that the image group was deleted.

1. To send the image group for QA review:
    1. Click **Needs Review** in the Confirm dialog box.
    2. In the Reason for Status Change dialog box that displays, select the reason the image group needs to be reviewed. Then, click **OK** .

An information dialog box displays informing you that the status of the image group changed to Needs QA Review.

1. To close the Confirm dialog box without making any changes, click **Cancel** .

## Appendix D: Clinical Context Object Workgroup

<!-- image -->

### CCOW Overview

Clinical Context Object Workgroup (CCOW) is an HL7 standard for clinical context management which synchronizes applications so that they are mutually aware of common elements. Clinical Display workstation is CCOW compliant and uses this standard to interface with CPRS, VistA Imaging TeleReader and other CCOW compliant applications.

When a clinician uses a CCOW compliant application (such as CPRS) and starts another CCOW compliant application (such as Clinical Display) the second application will automatically sign on with the same user credentials. When the clinician selects a patient in CPRS, it is also selected in Clinical Display.

When the QA Review window is open in Clinical Display, patient context is suspended. Patient context can also be suspended manually in both the Clinical Display and CPRS applications.

### Patient Context in Clinical Display

Clinical Display enables you to show context, suspend context, resume context, or resume setting the context for the patient. If patient context is suspended, it must be resumed before changing patients if you want to synchronize patients. In the Image List | Context menu, you can select:

| **Menu Option**    | **Description**                                                                                                                                                                                                                |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Show Context       | Shows the Context.                                                                                                                                                                                                             |
| Suspend Context    | Breaks the CCOW connection with CPRS which you can do manually through the menu option, or is done by the application while using certain utilities which displays images for multiple patients such as the QA Review Utility. |
| Resume Get Context | Gets the current Context.                                                                                                                                                                                                      |
| Resume Set Context | Resumes setting the Context.                                                                                                                                                                                                   |

Clinical Display uses the following icons throughout the application.

|    | Application is in Context     |
|----|-------------------------------|
|    | Application is not in Context |
|    | Context is changing           |

<!-- image -->

<!-- image -->

<!-- image -->

## Appendix E: For System Managers

<!-- image -->

**Note** : System Managers in Clinical Display must hold the **MAG SYSTEM** security key and have access to all of the Clinical Display functionality in addition to system manager functions.

### System Manager Menu Options

In the VistA Imaging Display main window and the Image List window, the System Manager menu on the menu bar is enabled if you hold the MAG SYSTEM security key.

<!-- image -->

Table 2

| **Menu Option**                             | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|---------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Workstation Configuration Window            | Enables the system manager to set the workstation configuration in the MAG.INI file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Clear Current Patient                       | If a patient is selected, this option clears the patient’s data from  display and readies the application for a new patient.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Image File Net Security ON                  | Turns ON/OFF Imaging Network security:  When Imaging Network security is ON, the Imaging system makes a connection to the Imaging Network Server as a user who is defined in the Imaging Site Parameters file and breaks the connection when the Image is opened or fails to open.  When Imaging Network Security is off, Imaging makes no attempt to connect to a network directory. The workstation must have a drive mapped to the Network directory to be able to capture images or the user who is logged in to the workstation must have access to the Imaging Network server. (intended for debugging purposes) |
| Show Messages from last OpenSecureFile Call | Each time an Image is opened, Imaging Network Security is used to connect and disconnect from the Image Network Server.  If you select this option, all messages generated from the last call to open image(s) are added to the Imaging Session Message History window. See  *Message History Window*  below.                                                                                                                                                                                                                                                                                                          |

| **Menu Option**                 | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Change Timeout Value            | Each workstation times out after a specific time of inaction. The timeout value is set in the IMAGE SITE PARAMETERS File. This setting can be changed for individual workstations to override the IMAGE SITE PARAMETERS value. The changed setting will remain in effect until it is changed again. If the setting is changed to '0' (zero) then the entry from the IMAGE SITE PARAMETERS file will be used as the timeout.  VistA Routine MAGGTU6 was modified, if the value in the TIMEOUT WINDOWS DISPLAY field (#121) of the IMAGING SITE PARAMETERS File #2006.1 is blank and the WorkStation TimeOut minutes in MAG.ini value is also blank, it will return the default timeout value of 6 minutes. |
| Patient Lookup/Login Enabled    | When VistA Imaging is opened from the CPRS 'Tools' menu, the Patient Lookup and Login functions are disabled in the VistA Imaging application. This option enables you to enable/disable the functions. (Intended for debugging purposes)                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Open Image by ID for annotation | User will be prompted for an Image ID. That image will then be opened in the 'Display Image by ID # ' window for annotation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

**Message History Window**

The Message History window is used to view system messages for debugging purposes.

<!-- image -->

**Viewing Messages**

1. Open the Message History window by performing any of the following steps:
    - In the VistA Imaging Display main window or Image List window, choose **System Manager | Show Messages from last Open Secure File Call** from the menu bar.

<!-- image -->

- In the VistA Imaging Display main window, click the **message window button**

in the lower left corner of the window.

- In the Image List window, choose **Options | Message Log** from the menu bar.
1. To display user messages in the Message History window, choose **Options** | **System Messages** from the menu.

If **System Messages** is not selected, user messages are displayed in the window.

1. To display system messages, select **System Messages** again to select it.
2. To refresh the information layout, choose **Refresh | Refresh Display** .
3. To automatically update the message in real time, choose **Refresh | AutoUpdate** . Reselecting Auto Update clears the option and stops the automatic update.
4. To format the display of the messages, choose **Options** and **Word Wrap** , **Font** , **Background Color.**
5. To keep the window open on top of all open Clinical Display windows, select **Stay on Top** .
6. To find text, choose **Options | Find Text** , enter the words in the Find window, and select the **Find Text** button.
7. To remove all entries in the Message History log, choose **Options | Clear history** .
8. To close the window, choose **File | Exit** .

### Image Information Advanced

Image Information Advanced displays more detail than standard information displayed in the

*Image Information Window* , which is available to all users.

### Image Information/Properties Window

In the sample window, the Image Information/properties window shows detailed data about an image or image groups.

<!-- image -->

**Toolbar in the Image Information/Properties Window**

| <!-- image -->   | Shows the internal information stored in the IMAGE file (#2005) for the Internal Entry Number (IEN) displayed in the edit box. When the window is opened, the selected Image's IEN is displayed. The IEN can be changed which gives you the option of viewing information for any Image. If the edit box is empty, then clicking the ^MAG(2005 button will display the information for the last Image entry in the IMAGE file (#2005).   |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <!-- image -->   | The IEN of the currently selected image.                                                                                                                                                                                                                                                                                                                                                                                                 |
| <!-- image -->   | Next: Loads the Next Image IEN in to the edit field and displays its Global List.                                                                                                                                                                                                                                                                                                                                                        |
| <!-- image -->   | Previous: Loads the previous IEN values                                                                                                                                                                                                                                                                                                                                                                                                  |
| <!-- image -->   | Loads the Group IEN for the current IEN being displayed.                                                                                                                                                                                                                                                                                                                                                                                 |
| <!-- image -->   | Displays internal information used by the application.                                                                                                                                                                                                                                                                                                                                                                                   |
| <!-- image -->   | Displays the associated TXT file in the memo area                                                                                                                                                                                                                                                                                                                                                                                        |
| <!-- image -->   | Displays the Image Information in the memo area                                                                                                                                                                                                                                                                                                                                                                                          |
| <!-- image -->   | Displays all of the fields for the IEN.                                                                                                                                                                                                                                                                                                                                                                                                  |
| <!-- image -->   | Displays any flags that have been set for the IEN.                                                                                                                                                                                                                                                                                                                                                                                       |

## Index

<!-- image -->

<!-- image -->

#### A

Abstracts · 12

button · 15

corrupt · 53 not found · 53 viewing · 51

window · 47 working with · 47

Actual Size button · 80 Alternate viewers · 57

annotating DoD Radiology Images · 159 annotating images at remote sites · 122 annotating RAD package images · 120, 159 annotation

global attributes · 143 annotation arrow properties · 146 annotation color · 145

annotation font · 143 annotation history layer · 160 annotation history layers · 152 annotation information · 154

Annotation Information tool · 154 Annotation Information button · 125 annotation line width · 144

Annotation Mode · 67, 122, 132, 159, 160 annotation opacity · 146

annotation permissions · 122, 123 Annotation Property Editor · 133

Annotation Property Editor button · 124, 132, 133, 135

Annotation toolbar · 123, 124

*annotations* · 1, 116, 120, 123 audit history · 152

color properties · 133

creating · 126 default settings · 143 deleting · 132 drawing arrows · 128

drawing ellipses · 127

drawing freehand drawings · 126 drawing lines · 126

drawing rectangles · 126 editing text · 137

ellipse properties · 138 filtering · 147

*freehand shape properties* · 126, 135

hiding · 147, 148, 149 hiding and showing · 147

highlighting areas of an image · 128 line/arrow properties · 134 modifying · 130, 132

moving · 131 protractor font · 141 protractor line · 141

protractor properties · 141 Rectangle/Highlighter properties · 136 resizing · 131

ruler length · 140 ruler properties · 139

ruler width and length · 140 saving · 160

selecting · 131

showing · 150, 151, 152

text · 127

text properties · 137 using the ruler · 128

viewing information about · 154 Annotations button · 67

Apply Actions to all Images button · 64, 98 Apply Actions to All Images button · 79 Arrow button · 124

**As Last Viewed annotation layer** · 147, 153 ASC file type · 55

Audit History button · 153 Audit History button · 125

audit history of annotations · 152, 154

**audit history window** · 153 Auto Window/Level button · 81 AVI file type · 55

<!-- image -->

BIG file type · 55

Bitmaps, non-viewable images · 53 Blocked images · 54

BMP file type · 56 BW file type · 56

<!-- image -->

Cache images · 50

Calibrate Ruler dialog box · 129 calibrating rulers · 129

CCOW · 5, 10, 229

Cine, Radiology · 81

Clinical Context Object Workgroup · 5, 229 Clinical Procedures · 12, 44

Clinical Types · 38

Color Channel button · 67, 80, 113 Column listings, displaying · 33 Column Selector window · 33 Configure Tree View window · 29

Configure User Preferences button · 30 Consults · 12, 42, 44

Controlled images description · 55

icon · 45

on the Utilities menu · 28 viewing · 45

Copy to clipboard button · 81 Copying an Image · 176

CPRS

link options · 11 patient selection · 5

creating annotations · 126

<!-- image -->

#### D

DCM file type · 56

**deleting**

image with annotations · 226 images with annotations · 226, 227

Deleting

images with questionable integrity · 225 single images · 224

deleting a group of annotated images · 227 deleting a single annotated image · 226 deleting annotated images · 226

deleting annotations · 132 deleting images · 221 DICOM Gateway · 75 DICOM images · 68, 69

DICOM Multi-frame Cine Viewer · 81 Discharge Summary report · 14, 213 Down-sampled image · 75

drawing freehand drawings · 126 drawing lines · 126

drawing rectangles · 126

<!-- image -->

#### E

Edit Annotations button · 124 editing text annotations · 137 EKG Display window · 86 Ellipse button · 124

Ellipse Property editor · 138

exiting Annotation mode · 160

<!-- image -->

File types

756 · 55

ASC · 55

AVI · 55

BIG · 55

BMP · 56

BW · 56

DCM · 56

HTM · 56

HTML · 56

JPG · 56

MHT · 56

MHTML · 56

PAC · 56

PDF · 56

TGA · 56

TIF · 57

TXT · 57

viewable in an alternate viewer · 57 viewable in Clinical Display · 55

Filters

as buttons in the Image List Window · 31, 35 Clinical Properties · 38

creating · 37

deleting · 41

General Properties · 38 Multi-line tabs · 35

on the Filters menu · 40 private · 35, 37

public · 35 working with · 34

Fit Columns in Window button · 31 Fit Columns to Text button · 31

Fit Image in Window button · 64, 79, 98

Fit the Image Height button · 79

Fit the Image Width button · 79 Fit to Width button · 64, 98

Flip Horizontal button · 66, 80

Flip Vertical button · 66, 80 Freehand button · 124

Freehand Properties dialog box · 126 Freehand Property Editor dialog box · 135, 136

<!-- image -->

#### G

GE/Marquette · *See* MUSE EKG global annotation attributes · 143

arrow · 146

color · 145

font · 143

line width · 144 opacity · 146

Global Annotation Attributes button · 143 Global Annotation Attributes button · 125

Global Annotation Attributes dialog box · 125, 133, 143,

144, 145, 146, 147, 183, 184

Goto First Page button · 66, 100 GoTo Last Page button · 66, 100 Goto Next Page button · 66, 100 Goto Previous Page button · 66, 100 Group Abstracts window · 47

Group Window · 12

<!-- image -->

#### H

Health Summary report · 14, 213, 214 Health Summary Report button · 15 hiding

annotations · 147

hiding annotations · 147, 148, 149 Highlighter button · 124

HTM file type · 56 HTML file type · 56

<!-- image -->

#### I	L

Icons in the item column · 32 ID mismatch · 53

Image Delete window · 222 Image Filter List button · 15

Image Filters Add/Edit window · 36 Image group · 47, 194

Image Index Edit Utility editing index fields · 191 purpose · 190

Image information advanced · 233

viewing · 52

window · 48

Image Information/Properties window · 233 Image List · 20

button · 15

filters menu option · 10 menu option · 12 window · 20

Image report · 211

Image Report + Print Copy Menu button · 66, 100 Image Report button · 81

**i** mage **w** ith **a** nnotations deleting · 226

images

deleting · 221

**i** mages **w** ith **a** nnotations deleting · 226, 227

Information dialog box · 154, 155

Invert Image button · 66, 80

<!-- image -->

JPG file type · 56 Juke Box · 53

Line button · 124

Line/Arrow Property Editor dialog box · 134 Login · 9

Logout · 10

<!-- image -->

#### M

MAG ANNOTATE MGR key · 132

MAG DELETE security key · 54, 218, 221

MAG EDIT security key · 54, 55, 190, 194, 218 MAG PAT PHOTO ONLY security key · 17, 218 MAG PREFETCH security key · 218

MAG RAD SETTINGS security key · 219 MAG ROI security key · 161, 176, 219

MAG SYSTEM security key · 14, 39, 54, 190, 219, 231

MAGDISP ADMIN security key · 219 MAGDISP CLIN security key · 219 Maximize Image button · 65, 99 measuring angles in images · 130 Menu bar

Full Resolution Viewer · 60

Image Index Edit window · 190, 191 QA Review window · 195

Radiology Viewer · 71 Video Player · 83

VistA Imaging Display main window · 9, 208, 209, 211,

222

Message History message Log · 11 viewing · 232

MHT file type · 56 MHTML file type · 56

modifying annotations · 130, 132 Motion video

bitmap · 53

clip · 82

Mouse Magnifier button · 65, 80, 99

Mouse Pointer button · 65, 99 moving annotations · 131 MP3 file type · 57

MP4 file type · 57 MPEG file type · 57 MPG file type · 57 Multi-line tabs · 35 MUSE EGK button · 15 MUSE EKG viewer · 86

<!-- image -->

Needs Review · 54 NO MATCH · 17, 19

<!-- image -->

Open a Pan Window button · 81 Open the Image button · 30

Open the MUSE EKG window button · 31 Open the Report button · 30

<!-- image -->

PAC file type · 56 PACS device · 53

Pan Image with mouse button · 80 Pan Image with Mouse button · 65, 99 Patient

lookup box · 16 Lookup button · 16

profile on the Reports menu · 14 selecting · 16

PDF file type · 56 Popup menu

Abstracts window · 50

Full Resolution Viewer · 68 Group Abstracts window · 78 Image List window · 34

Video Player · 86

Pre Fetch Patient Images · 11 Preview Abstract button · 31 Preview Report button · 31 Printing an Image · 161 Procedure/Event · 38

Progress Notes · 12, 42, 44

Protractor button · 124, 130 protractor font · 141 protractor line · 141 protractor properties · 141

Protractor Property Editor · 141, 142

protractors · 130

<!-- image -->

#### Q

QA · *See* Quality Assurance QA Review · 12

performing · 204

report · 12

QA Review Report · *See* Status / Verification Report QA Review Window · 194

Quality Assurance · 194 Questionable Integrity · 54

<!-- image -->

#### R

Radiology

Exam Listing window · 43 exams menu option · 12 exams, viewing · 43 studies · 70

viewer · 68

read only indicator · 125 read-only indicator · 125 Rectangle button · 124

Rectangle/Highlighter Property editor · 136 Refresh Images button · 65, 99

Refresh Patient Images · 11 Refresh Patient Images button · 30

Remote image view configuration button · 16

configuration menu option · 11 Configuration window · 188

viewing patient data at remote sites · 185 Remote image views

using · 185 Remote Login · 10

Remove All Images (Not a Delete) button · 66, 100 Remove Selected Image(s)(Not a Delete) button · 65, 100 Reports

Discharge Summary · 14, 214

Health Summary · 14, 213 Image report · 211 Patient Profile · 14

QA Review report · 12 Request of Information · *See* ROI Reset Image button · 67, 100

Reset Image to original setting button · 79 resizing annotations · 131

RIVs · 187

ROI · 161, 176, 219

Rotate Clockwise 90 button · 65, 99

Rotate Counter Clockwise 90 button · 65, 99 Rotate Left button · 80

Rotate right button · 80 RTF file type · 57

Ruler button · 124

Ruler menu · 128

Ruler Property Editor · 139, 140, 141

<!-- image -->

#### S

Save Settings now · 11 on Exit · 11

saving annotations · 160 Security keys

for deleting images · 221

MAG DELETE · 54, 218, 221

MAG EDIT · 54, 55, 190, 194, 218 MAG PAT PHOTO ONLY · 218 MAG PREFETCH · 218

MAG RAD SETTINGS · 219 MAG ROI · 161, 176, 219

MAG SYSTEM · 39, 54, 190, 219 MAGDISP ADMIN · 219 MAGDISP CLIN · 219

PAT PHOTO ONLY · 17

select all annotations option · 131 Select Annotation button · 124, 130 Select Columns button · 31

Select Patient button · 30 Select/Create Image Filter button · 30 selecting annotations · 130

Sensitive images · 55

setting color properties for annotations · 133 setting ellipse properties for annotations · 138

*setting freehand shape properties for annotations* · 126, 135

setting line/arrow properties for annotations · 134 setting Rectangle/Highlighter properties for annotations ·

136

setting ruler length · 140 setting ruler properties · 139

setting ruler width and length · 140

setting text properties for annotations · 137 Shortcut Keys · 11, 215

Show Hints · 11, 51

Show or Hide Abstracts button · 30 Show/Hide Message Window button · 16 showing

annotations · 147

showing annotations · 150, 151, 152 Signing in · 5

Single image · 194 Site Code · 189

Site Name · 188

Specialty/SubSpec · 38 Stack View Slide · 78

Status/Verification Report window · 205 System Manager menu · 8

<!-- image -->

temporary annotations · 159

temporary measurement annotations · 159 text annotations · 127

Text button · 124

Text Integration Utility · 123 Text Properties dialog box · 127

Text Property Editor dialog box · 137, 138 TGA file type · 56

TGA image · 68 TIF file type · 57

Tile all Images button · 65, 99 TIU business rules · 54

TIU Note Consults · 42 Tool bar

Abstracts window · 49

Full Resolution Viewer · 63

Image Information/Properties window · 234 Image List window · 30

Radiology Viewer · 79 Stack View Slide · 78 Video Player · 85

VistA Imaging Display main window · 15 TXT file type · 57

<!-- image -->

User Preference dialog box · 143, 144, 183 User Preferences

button · 15 menu option · 11

User Preferences, configuring alternate viewer options · 181

dialog box · 178

image abstracts with image list · 179 layout style of the image list · 182 patient selection window · 178

Utilities menu · 8

<!-- image -->

#### V

View Annotations button · 124 Viewers

description of · 59

DICOM Multi-frame Cine · 81 MUSE EKG · 86

Radiology · 68 Video Player · 82

VistA Imaging Display main window · 8

<!-- image -->

#### W

WAV file type · 57 Windows

Abstracts · 47 Column Selector · 33

Configure Tree View · 29

DICOM Multiframe Cine View · 81 EKG Display · 86

Group Abstracts · 47 Image Filters Add/Edit · 36 Image Information · 48

Image Information/Properties · 233 Image List · 20

Progress Notes · 44 QA Review · 194

Radiology Exam Listing · 43 Radiology Viewer · 68 Status/Verification Report · 205 Video Player · 82

VistA Imaging Display main · 8

<!-- image -->

Zoom In button · 64, 99

Zoom in on Selected Area button · 65, 81, 99 Zoon Out button · 65, 99

- If you intend to print most of the images on the list, unselect the images that you wish to exclude from the print queue by clicking each image in the Image List window.

- If you intend to process most of the images on the list, unselect the images that you wish to exclude from the processing job by clicking each image in the image list.

- Patient Profile