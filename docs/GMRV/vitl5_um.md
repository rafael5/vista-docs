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
is_change_pages: false
library_max_patch: null
package_id: GMRV
patch: null
patch_gap: null
section: ''
source_file: vitl5_um.docx
status: draft
title: Version 5.0
---

<!-- image -->

**Vitals / Measurements**

**User Manual**

# Version 5.0

# October 2002

Revised September 2009

GMRV*5.0*23


Office of Enterprise Development

###### Revision History

| Date           |   Revision | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Author   |
|----------------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| September 2009 |       5.23 | Sections updated for Patch 23 (GMRV*5.0*23):  - updated Title Page  - updated Revision History  - updated Table of Contents  - updated Introduction, page 1-2 and 1-4  - updated Using Vitals Manager, pages 2-2, 2-3, 2-4, 2-5, 2-7, 2-8, and 2-9  - updated Using Vitals, pages 3-3, and 3-4  - updated Entering Vitals Data, pages 4-3, 4-4, 4-6, 4-7, 4-10, 4-12, 4-14, 4-15, 4-16, and 4-21  - added “Enter Vitals Menu Bar” section, page 4-8.  - updated Reports, pages 5-2, 5-3, 5-4  - updated Appendix A – Access Key Listing, pages 6-2  - updated Appendix C – Using Vitals in CPRS, pages 8-5, 8-6, and 8-7                    | REDACTED |
| April 2006     |       5.3  | Sections updated for Patch 3 (GMRV*5.0*3):  - updated Title Page  - updated Revision History  - updated Table of Contents, all pages  - updated Introduction, page 1-1, 1-2  - removed Implementation and Maintenance chapter  - updated Using Vitals Manager, pages 2-2, 2-5, 2-6  - removed Package Operation chapter; replaced with new Using Vitals chapter, updated all pages  - updated Entering Vitals Data, all pages  - updated Reports, all pages  - updated Appendix A, all pages  - updated Appendix B, page 7-3, 7-4  - added Appendix C – Using Vitals in CPRS v26  - updated Glossary, all pages  - updated Index, all pages | REDACTED |
| October 2003   |       5.1  | Sections updated for Patch 1 (GMRV*5.0*1):  Revision History  Table of Contents  Site Files  Entering Vitals Data  Reports                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | REDACTED |
| January 2002   |       5    | Initial Publication                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | REDACTED |

This page intentionally left blank for double-side printing.

###### Table of Contents

1.	Introduction	1-1

Functionality	1-1

Information on GUI software	1-2

Adding Vitals to the Tools Menu in CPRS	1-5

2.	Using Vitals Manager	2-1

Getting Started with Vitals Manager	2-1

Managing Vitals Categories and Qualifiers	2-2

Printing a Qualifiers Table	2-3

Editing Abnormal Values	2-3

Editing System Parameters	2-4

Creating/Editing a Template	2-6

3.	Using Vitals	3-1

Getting Started with Vitals	3-1

Overview of the Vitals window	3-2

Editing User Options	3-3

About CCOW	3-4

Joining a Clinical Context	3-5

Breaking the Clinical Link	3-5

Showing status	3-5

4.	Entering Vitals Data	4-1

Selecting a Patient and a Template	4-1

Entering Data for a Single Patient	4-3

Enter Vitals Menu Bar	4-8

Entering Data for Multiple Patients	4-10

Creating a User Template	4-14

Viewing Allergies	4-19

Marking Vitals as Entered in Error	4-20

5.	Reports	5-1

Viewing a Graphic Report	5-1

Printing a Report	5-2

6.	Appendix A – Access Key Listing	6-1

7.	Appendix B – Customizing the Client Installation	7-1

8.	Appendix C – Using Vitals in CPRS	8-1

Overview of Vitals Lite	8-1

Opening the Vitals Lite window in CPRS	8-2

Viewing Data in Vitals Lite	8-3

Entering Vitals in Vitals Lite	8-5

Correcting Vitals in CPRS	8-6

9.	Glossary	9-1

10.	Index	10-5

## 1 Introduction

The Vitals/Measurements application is designed to store in the patient's electronic medical record all vital signs and various measurements associated with a patient's hospital stay or outpatient clinic visit. Data entered can be accessed by several VistA (Veterans Health Information Systems and Technology Architecture) applications (e.g., CPRS, Health Summary) that interface with the Vitals/Measurements application.

The Vitals application is composed of two modules: Vitals and Vitals Manager. Each module is accessed separately through GUI executable icons on the user’s desktop. The Vitals module is used to enter patient data, and is assigned to clinical staff. The Vitals Manager module is used to manage the Vitals templates and abnormal values ranges, and is assigned to the Clinical Application Coordinator, package coordinator, and Information Resource Management Service (IRMS) staff.

A Dynamic Link Library (DLL) file is also provided to allow other applications to use the Vitals/Measurements GUI. See Appendix C for more information on the DLL.

GMV MANAGER is the only security key in this application. This key controls access to the Vitals Manager module. This key also allows a user to view/create/edit all other user’s templates in the Vitals Manager module; without this key the user can only view, create, or edit their own user templates. This key should be assigned to the package coordinator.

### Functionality

•	Provides a GUI (Graphical User Interface) to make collecting and viewing of data easier. Additional information on GUI software is contained at the end of this chapter.

•	Supports documentation of a patient's vital signs (e.g., temperature, pulse, and respiration), and tracks a patient's height, weight, central venous pressure (CVP), circumference/girth and oxygen saturation via oximetry with supplemental oxygen information. Also supports documentation of detailed or positional blood pressures for a patient (for example, bilateral blood pressures taken in a sitting position).

•	Displays latest information on all of the patient's vitals/measurements in both metric equivalents and U.S. customary units (when appropriate) along with the date/time the information was obtained, and the name of the user who entered the information.

•	Allows facilities to establish hospital-wide high and low values for most vital signs and measurements. Identifies abnormal values, those values outside the high and low range, on vitals/measurements reports.

•	Allows users to record a reason for the omission of a patient's vitals/measurements (such as Patient on Pass).

•	Associates qualifiers (alpha characters appended to the measurement's numeric value) to provide a more detailed description of the patient's vitals/measurements.

•	Contains online help windows to assist users. Online help is accessed through the Help menu at the top of the screen, or by pressing the F1 key on the keyboard.

•	Displays graphic reports on workstation monitors, and provides a variety of printable reports. Reports can be printed for an individual patient or for multiple patients.

•	Provides APIs that pass patient vitals/measurements information within a specific date range to the other VistA applications.

•	Provides compliance with the Clinical Context Object Workgroup (CCOW) standard. The CCOW standard provides a way for applications to know which other applications are currently running, and which patients are selected in those applications.

•	Supports an interface to vital signs monitor connected to the workstation.

### Information on GUI software


**Accessibility Features in Vitals 5.0**

Keyboard shortcuts and navigation options have been added to make the GUI accessible to a wider range of users, including those who have limited dexterity, low vision, or other disabilities. See Appendix A for a complete listing of access keys and shortcuts.

Intranet WWW Documentation

Documentation for this product (including user manual, technical manual and package security guide, release notes, and installation guide) is available on the VA intranet at the following address: REDACTED

**GUI and Windows**

GUI stands for Graphical User Interface, most frequently seen as the Windows screen. If you have already used programs with these screens, then the Vitals GUI screen will seem familiar to you. The Vitals GUI is only implemented on the Windows platform at this time.

If you have little or no familiarity with Windows, you can browse through the Windows help file for information about the basics of using Windows. Also, see the next few paragraphs for brief descriptions of some GUI features.

To access the Windows Help File, click the Start button in the taskbar and click Help. Use this help file as a reference whenever you have general questions about Windows.

The following is an example of the control elements found in a GUI screen:

Figure -

**Windows**

An “application window” is the area on your computer screen used by a program. If you have more than one program running at the same time, you can go from one program to another by clicking in each application window. The currently active window contains a colored bar (usually blue) at the top of the window. An inactive window contains a gray bar at the top of the window. You can also move, close, or minimize the application window to make room for another window. (See Help in Windows for further instructions on these functions.)

<!-- image -->

<!-- image -->

<!-- image -->

Figure -

**Pop-up Windows**

These are “mini” windows that pop up within a window to provide or request information. Usually they require some action before they will go away. Clicking on buttons with the words Cancel, Exit, or something similar closes these windows.

**Menus**

Menus are shown in the gray bar near the top of the window. Some examples of menus are: File, Edit, Reports, and Help — typical menus for most Windows applications. When you click on one of these, a list of options is displayed.

**Help**

Online help and documentation are available in several formats: hints, context-sensitive help, menu help, and Internet Web documentation.

**Hints**

Place the cursor over a specific button and a pop-up box will appear containing a short description of that button.

**Context-Sensitive Help**

Use the “F1” key at any time to obtain help on the current screen.

**Menu Help**

Select the Help Menu at the top of the screen. A Table of Contents opens. Choose one of the contents, or type in a topic you want help on. A screen appears containing help about that subject.

**Access Keys**

Use access keys to quickly get to an option through the pull-down menus by holding down the Alt key and pressing the underlined letter of the desired pull-down menu, then (still holding down the Alt key) press the underlined letter of the desired option. Some other screen components (e.g., buttons such as OK) can also be reached by holding down the Alt key and pressing the underlined letter for that screen component. Some buttons and icons can be invoked by holding down the Ctrl key and pressing a letter key. A few can be invoked by pressing a function key (e.g., F5). See Appendix A for a full list of access keys.

**Tool Bars**

Tool bars are shown in the gray bar below the Menu bar. The tool bar contains icons (with or without text) that invoke functionality when clicked on using the mouse. For example, the printer icon opens a dialog box allowing the user to select a printer.

**Trees**

Trees are lists that the user can expand or collapse in order to navigate to needed information. The plus sign (+) to the left of a tree item indicates that tree item contains additional entries. Clicking on the plus sign will expand the tree list to display those additional entries. A minus sign (-) will appear to the left of the tree list instead of a plus sign after that item is clicked. Clicking on the minus sign will collapse the list to hide the items again.

### Adding Vitals to the Tools Menu in CPRS

A site may use the Tools menu to give users access to other client software from within CPRS. The parameter, ORWT TOOLS MENU, is used to set up the list of software that appears on the menu. This parameter may be set up for the site, then overridden as appropriate at the division, service, and user levels.

Each item entered on the menu should have the form, NAME=COMMAND. NAME is the name you want the user to see on the menu. An ampersand may be used in front of a letter to allow keyboard access to the menu item. The COMMAND may be a line that can be executed by Windows. It may also be any file for which Windows has a file association.

Example:  Create a User tools menu that contains Vitals and Vitals Manager.

Select General Parameter Tools Option:  ep  Edit Parameter Values

--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: orwt TOOLS MENU     CPRS GUI Tools MenuORWT TOOLS MENU may be set for the following:

1   User          USR    [choose from NEW PERSON]

2   Location      LOC    [choose from HOSPITAL LOCATION]

2.5 Service       SRV    [choose from SERVICE/SECTION]

3   Division      DIV    [REGION 5]

4   System        SYS    [OEC.ISC-SLC.VA.GOV]

Enter selection: **1  User   NEW PERSON**

Select NEW PERSON NAME: **VITUSER, THREE          CT**

-------------- Setting ORWT TOOLS MENU  for User: VITUSER, THREE --------------

Select Sequence: **1**

Are you adding 1 as a new Sequence? Yes// **YES**

Sequence: 1// **1**

Name=Command: **Vitals=&lt;directory\_name&gt;”\Vitals.exe” /p=%PORT /s=%SRV /cprs /dfn=%DFN**

Select Sequence: **2**

Are you adding 2 as a new Sequence? Yes// **YES**

Sequence: 2// **2**

Name=Command: **Vitals Manager=&lt;directory\_name&gt;”\VitalsManager.exe” /p=%PORT /s=%SRV /cprs /dfn=%DFN**

Select Sequence:

Note the quotation marks in the Vitals and Vitals Manager examples. A path that contains space characters (like C:\Program Files\...) must be surrounded by quotation marks. Entries on the command line may also contain parameters.

It is possible to pass context-sensitive parameters. These are parameters that are entered as placeholders, and then converted to the appropriate values at runtime. These placeholder parameters are:

%SRV	= Server name for the current broker connection.

%PORT	= Port number for the current broker connection.

%MREF	= M code giving the global reference where the patient DFN is stored.

%DFN	= The actual DFN of the currently selected patient.

%DUZ	= Internal entry number of the current user.

So, if you have another application that needs to know, for example, the identity of the current user and currently selected patient, you could list %DUZ and %DFN as parameters in the command that executes that program.

When the user clicks “Vitals” from the Tools menu, Vitals will be called and the actual server, port, and global reference will be substituted as command line parameters.

## 2 Using Vitals Manager

Vitals Manager allows a site’s administrator (CAC, IRMS) to define the way that vitals appear in the Vitals/Measurements application. This includes activities such as creating and editing templates, associating qualifiers with different vital types, setting normal/abnormal value ranges for each vital type, and printing a list of qualifiers and their associated categories and vital types.

The Vitals Manager module is used to maintain the site files and settings necessary for a site to operate the software, and the Vitals (user) module is used to collect, store and display patient data. **All the options discussed in this chapter are contained in the Vitals Manager module.**

**This chapter shows you how to:**

1.	Start the Vitals Manager module

2. 	Manage Vitals Categories and Qualifiers

3.	Print a qualifiers table

4. 	Edit abnormal values

5. 	Create/edit a template

### Getting Started with Vitals Manager

When you double click on the Vitals Manager icon, enter your access and verify codes at the VistA sign-on window, and click on the OK button, the main window will open (Figure 2-1):

<!-- image -->

Figure -

### Managing Vitals Categories and Qualifiers

Qualifiers describe how patient vital signs and measurements were taken. These qualifiers are categorized by location (e.g., right arm, left leg), position (e.g., lying, sitting, standing), method (e.g., cuff, Doppler, assisted ventilator, etc.), site (e.g., right, left), quality (e.g., actual, estimated), and cuff size (e.g., adult, small adult, pediatric). Synonyms are used as qualifier abbreviations and are appended to the measurement's numeric values on some displays.

Vital types, categories, and qualifiers are nationally defined and cannot be changed locally. Each vital type may be linked to one or more categories, and each category may be linked to one or more qualifiers. The linkages between qualifiers, categories, and vital types are also nationally defined and cannot be changed locally. (See the National Term Rapid Turnaround web site at REDACTED to request a qualifier change.)

To view the categories and qualifiers that are associated with a particular vital type, double-click the Vitals folder to display the full list of vital types, then click on a vital type to view. A list of categories and qualifiers displays on the right side of the Vitals Manager window (Figure 2-2):

<!-- image -->

Figure -

### Printing a Qualifiers Table

The Qualifiers Table is a list of all qualifiers for each vital type and its categories, including each qualifier’s synonym. The Package Coordinator may use this list to determine the accuracy and completeness of the qualifier selection. Qualifiers that are not associated with a category and vital type do not appear in this list.

To print the Qualifiers Table go through the main menu bar and select File, Print Qualifiers Table. The following screen appears:

<!-- image -->

Figure -

Select an appropriate device in the Device field. Select a date/time to queue this report in the Queue To Run at field. The default date/time is the current server date/time. This report can’t be queued to run for a past date/time. Click the OK button to print the report.

### Editing Abnormal Values

An abnormal value is defined as a value outside the normal range for a vital type. You can define what these high/low values should be so that when a user enters a vital/measurement outside the normal range of values for a vital type, the value will show on the data table as an abnormal value. It will be bold, or a different color dependent upon how it is defined in the User Options option in the Vitals module. User Options is used to define what the text should look like in the data table (bold, different color, etc.) for both normal and abnormal values. Refer to the section on Editing User Options in the Entering Vitals Data chapter in this manual.

To edit abnormally high and low vital type values double click on the Abnormal Values folder to open it, then click on the vital type you wish to edit high/low values for. The following window appears (Figure 2-4):

<!-- image -->

Figure -

You can either move the bar up or down to change the abnormal value or type in the abnormal value. If you type in a value, the meter will not reflect the value until you click in an area outside the box where you entered the value. **Click the Save Abnormal Values button next to the Abnormal Values heading at the top of the window to save the values** .

### Editing System Parameters

There are 3 system parameters in the Vitals Manager module. They are:

**Allow User Templates**

**Help Menu Web Address**

**Version Compatibility**

To edit system parameters double click on the System Parameters folder to open it (Figure 2-5). Below are instructions for editing each of the system parameters.

**Allow User Templates** allows a CAC or package coordinator to decide whether a clinician should be able to create/edit user templates in the Vitals Manager and Vitals modules. When the checkbox is checked, a clinician is able to create/edit user templates in the Vitals Manager and Vitals modules.

**Help Menu Web Address** contains the address for the Vitals Home Page and directs the user’s default browser to this page when accessed.

**Version Compatibility** is used to check if a client version is compatible or not with the current version of Vitals running on the VistA M server. All previously installed versions of Vitals/Measurements are listed in this parameter. Only the version(s) that are compatible with the current server version are checked. These versions are identified by their executable name and the Windows file version. Because backward compatibility is required, more than one version of the software may be flagged as compatible.

<!-- image -->

Figure -

**Click the Save System Parameters button next to the System Parameters heading at the top of the window to save the values.**

**Special Note** : The VistA server install (KIDS Build) will automatically set the Help Menu Web Address and Version Compatibility parameters for the client/server versions being installed. After an installation this parameter should be carefully reviewed. Modification of this parameter should not be needed unless the site is testing a patch or performing local modifications to the client software.

### Creating/Editing a Template

Templates are a set of vitals/measurements grouped together to make data entry simpler and easier. Using the Vitals Manager module, templates can be created for the following categories:

**System** – Templates are available to all system users

**Division** – Templates are available to all users within a division (for multi-divisional sites)

**Location** – Templates are available to all users within a particular ward , team, or clinic

**User** – Templates are available only to the individual user who created the template

**Note:  The Allow User Templates system parameter must be checked and system parameters must be saved in order to see User templates.**

All templates are created the same way. The following instructions show how to create/edit a template for a Location.

To create a new template, go through the main menu bar and select Templates, New Template. You can also click on the Create a New Vitals Input Template button on the toolbar to create a new template. The following window appears (Figure 2-6).

<!-- image -->

Figure -

In the Type section of the window, select the type of template you want to add by clicking the appropriate radio button. In this case the type selected is Location.

<!-- image -->

Figure -

Enter the name of the (division, location, user) this template is to be associated with in the Division/Location/User Name field (Figure 2-7). In this case the field says Location Name. For Location, only entries in the Hospital Location (#44) file may be selected. For Division, only entries in the Institution (#4) file may be selected. For User, only entries in the New Person (#200) file may be selected. For System, only entries in the Kernel System Parameters (#8989.3) file may be selected.

Enter the name of the template you want to add in the Template Name field (maximum length is 30 characters).

Enter a short description of the template in the Template Description field (maximum length is 50 characters). This field is optional. Click the OK button to create the blank template.

<!-- image -->

Figure -

Your new blank template appears on the screen (Figure 2-8). Now you can edit your template to add vital types and qualifiers to it. Click the Add button on the right side of the screen display to add vital types to the template and the following window appears.

<!-- image -->

Figure -

Click on each of the vital types you want to add to your template (Figure 2-9). You may select multiple vital types by holding down the Ctrl key and selecting multiple vital types, or hold down the Shift key to select a range of vital types. Click the OK button when finished.

<!-- image -->

Figure -

Your template now has vital types, but no default qualifiers (Figure 2-10). To assign default qualifiers you must select each vital type to edit it. Select a vital type by clicking on it, and the qualifiers for that vital type appear in a drop-down list on the bottom portion of the screen.

<!-- image -->

Figure - – The Template Editor screen

Select the qualifiers desired by clicking on the desired entry in the list. Only one qualifier can be selected from each category (Figure 2-11). You can select US or Metric scale for each appropriate vital type from the Measurement box. US is the default. **Qualifiers are automatically saved.**

Now your template is complete.

Make a template a default by going through the main menu bar and selecting Templates, Set Default Template, or click the Set Template as Default button on the toolbar. The default templates show up with a yellow icon on the list on the left side of the screen.

Each Division, Location, and User (e.g., 3AS) can have only one template at a time designated as the default. Designating a template as a default is merely a way to indicate a preference for that template. You do not have to indicate a template as a default. However, it is recommended that you designate one System level template as a default. When first time users enter patient data, the default System template will be displayed until the user selects another template instead.

Select a vital type and click the Delete button on the right side of the Template Editor screen to remove a vital type from the template.

Use the up/down arrow buttons to move vital types around in the list.

Go through the main menu bar and select Templates, Save Template, or click on the Save Template button to save the template settings.

To delete a template, highlight the template name, then from the main menu bar select Templates, Delete Template, or click on the Delete Template button.

## 3 Using Vitals

This chapter contains an overview of the features and options available in the Vitals module.

Online help is available throughout the Vitals application. Click the Help menu at the top of the screen to see a table of contents and index containing help on how to enter data, print reports, etc. There is help available on every screen by pressing the F1 key.

This chapter contains the following topics and sections:

1.	Start the Vitals module

2.	Get an Overview of the Vitals window

3. 	Customize the GUI by editing User Options

4.	Learn about CCOW and Clinical Context management

### Getting Started with Vitals

To open the Vitals application, double-click the Vitals icon on your desktop, or select Vitals from your CPRS Tools menu. Enter your access and verify codes at the VistA sign-on window, and then click the OK button. The main Vitals window opens:

<!-- image -->

Figure -

### Overview of the Vitals window

The Vitals window is divided into two main sections: the Patient Selector panel on the left, and the Vitals Data area on the right. In the example above (Figure 3-1), the Vitals Data area is empty because a patient has not yet been selected.

The screen layout is saved between sessions, so the last lookup that was used appears when opening the Vitals module. For example,  if “Ward” was the last selection made in the Patient Group List, then it will be the default selection when the current session is opened. The software will display previous values as defaults whenever possible. See the Selecting a Patient and a Template section (page 4-1) for more information about the Patient Selector panel.

The Vitals application contains a navigation bar across the top of the main window:

<!-- image -->

The Patient Name-SSN-DOB box at left is a button. Clicking this button opens a Patient Inquiry screen containing general information such as address, status, and appointments for this patient. This report can be printed. See Figure 4-4.

The Hospital Location-Date box is an informational area that displays the patient’s current hospital location, if one has been assigned, and the currently selected date range.

The Pt S elect button opens and closes the Patient Selector panel. See Figure 4-3.

The E nter Vitals button opens the Vitals Input screen when a single patient is selected so users can select templates and enter vitals data. See Figure 4-6.

If multiple patients are selected, the E nter Vitals button will be unavailable; instead, a button labeled Input Vitals for the Selected Patients will become available. This button is located at the bottom of the Patient Selector pane. See Figure 4-8.

The Alle r gies button opens a list of any allergies the patient may have.

A similar navigation bar is available at the top of the Enter Vitals window:

<!-- image -->

The Patient Name-SSN-DOB box at left is a button. Clicking this button opens a Patient Inquiry screen containing general information such as address, status, and appointments for this patient. This report can be printed. See Figure 4-4.

The Hospital Location-Date box is an informational area that displays the patient’s current hospital location, if one has been assigned, and the currently selected date range.

Read Monitor retrieves data from a vital sign monitor connected to the workstation.

The D ate/Time button opens a date/time selection window. See  Figure 4-7

The H ospital button opens a hospital location selection window. See Figure 4-5.

The Exp. Vie w button opens and closes the template selection panel at the left side of the Enter Vitals window. See Figure 4-6.

The Latest V . button opens and closes the latest vitals display panel at the bottom of the Enter Vitals window. See Figure 4-6.

### Editing User Options

You can customize the Vitals windows by choosing how to display the text on the data table and the latest vitals area. You can change the color of the text, the background color, bold the text, and show qualifier abbreviations. To edit these preferences, go through the main menu bar and select File, User Options. The following window appears (Figure 3-2).

<!-- image -->

Figure -

Preferences can be set for both normal and abnormal values. Click the Text button to select a text color for the table and latest vitals display. Click the Background button to select a background color for the table and latest vitals display. Check the Bold checkbox to make the text bold. Check the Show Qualifiers checkbox to show qualifier abbreviations with each value.

Click the Defaults button to restore default settings. Default settings for normal values are:

Text is black, Background is white, Bold is not checked, and Show Qualifiers is checked.

Default settings for abnormal values are:

Text is red, Background is white, Bold is not checked, and Show Qualifiers is checked.

The Search Delay setting allows the user to define a time lag to use between entering characters and beginning the patient lookup. If the time lag passes before the next character is typed, the patient lookup component will use the characters already entered to create a selection list.

<!-- image -->

Figure -

Select the appropriate search delay in seconds from the dropdown list (Figure 3-3).

Click the Apply button to save the settings. Click the OK button when finished.

### About CCOW

Clinical Context Management (also called “CCOW”) is a way for VistA applications to synchronize their clinical context based on the Clinical Context Object Workgroup standard. In simple terms, this means that if CCOW-compliant applications are sharing context and one of the applications changes to a different patient, the other applications will change to that patient as well. By default, the CCOW link is automatically active. (See Appendix C for information on using /noccow or /ccow=patientonly switches to disable CCOW or limit its functionality.)

Vitals has been made CCOW-compliant and can now synchronize with other CCOW-compliant VistA applications. For example, if you are logged in on CPRS (which is also CCOW-compliant) and clicked the Vitals link, the Vitals GUI will be launched and will open the same patient that is active in CPRS. You can also open two different Vitals sessions and not synchronize them, allowing you to view two patients’ charts at the same time.

For more information about the CCOW standards for VistA applications, see the Workgroup web site at: REDACTED .

The CCOW icon shows whether Vitals is linked with other CCOW compliant applications on the desktop. One of these three icons will display:

<!-- image -->

Active – A single figure with a chain link indicates that CCOW link is active.

<!-- image -->

Broken – Multiple figures with a broken chain link indicates that the CCOW link has been broken and that the applications are no longer synchronized.

<!-- image -->

Unavailable – A red circle with a diagonal line through it indicates that the Contextor software has not been installed and CCOW is not available.

#### Joining a Clinical Context

The CCOW clinical link is automatically active, and will remain active unless you break the clinical link. To manually join the clinical context, go through the File menu and select Rejoin Clinical Link. If you want the other open applications to synchronize with the current patient in the active application, select Use this Application’s Data. If you want the current application to synchronize with the patient that is open in another application, select Use Global Data.

The CCOW icon changes to Active and all open VistA applications are synchronized.

#### Breaking the Clinical Link

To break the CCOW Clinical Context link, go through the File menu and select Break the Clinical Link.

The CCOW icon changes to Broken and the VistA applications are un-synchronized, allowing you to work on two different patients when multiple CCOW-compliant applications are open..

#### Showing status

To see information about CCOW, go through the File menu and select Show Status. An information window opens, stating whether or not the Contextor software has been installed, and whether the application is participating in a clinical context.

This page intentionally left blank for double-side printing.

## 4 Entering Vitals Data

The Vitals module is used to enter vitals data, create user templates, view allergies, and mark incorrect vitals as entered in error. These topics are discussed in this chapter. The Vitals module also lets the user print several different Vitals reports; this is discussed in the Reports chapter in this manual.

**This chapter shows you how to:**

Select a patient for vitals entry

Enter vitals data

Create a user template

View allergies

Mark vitals as entered in error

Edit user options

### Selecting a Patient and a Template

To enter vitals data, you will use a template. Templates are a set of vitals/measurements grouped together to make data entry simpler and easier. Templates for system, divisions, locations, and users can be created in the Vitals Manager module. Refer to the section on Creating/Editing a Template in the Using Vitals Manager chapter of this manual for more information on creating/editing templates for system, divisions, locations, and users. If allowed, templates can be created for yourself as a user in the Vitals module. These templates are called user templates. For information on creating a user template refer to the section on Creating a User Template later in this chapter.

The Patient Selector must be open in order to select a patient. To open the Patient Selector, go through the main menu bar and select File, Pt Select, or click the Pt Select button on the top right side of the screen. The last lookup that was used appears when opening the Patient Selector.

Patients can be selected by Unit, Ward, Team, Clinic, or All. “Unit” allows the user to select from a list of Nursing units. “Ward” allows the user to select from a list of MAS Wards. “Team” allows the user select from a list of teams defined in the OE/RR List file (#100.21). “Clinic” allows the user select from a list of clinics for a predetermined period of time (e.g., Today, Yesterday, Past week). “All” allows the user to select a single patient by name or SSN.

To begin selecting patient names, click the desired tab under Patient Groups List (in this example “All” is selected), then enter the first few letters of the patient’s name, or the last four digits of the patient’s Social Security Number. A list of patients matching those criteria are listed on the bottom left portion of the screen (Figure 4-1).

Figure -

At this point you can either select a single patient name or multiple patient names.

### Entering Data for a Single Patient

Select a patient name by double clicking it. A confirmation screen appears (Figure 4-2).

Figure -

This screen shows you additional information on the selected patient. If the patient selected is a sensitive patient, a sensitive patient screen will appear telling you that this patient’s information is available on a need-to-know basis only. Click the OK button to confirm your patient selection.

The patient information opens in the Vitals window (Figure 4-3), showing existing data on a graph and in a spreadsheet-like data grid. You can access a text-only version of the data grid by going through the File menu and selecting Data Grid Report.

<!-- image -->

Figure -

The time scale runs from left to right, displaying the most recent values on the far right side of the graph and grid. You can move left and right across the graph by moving the slider bar between the graph and the grid. To expand the graph and grid displays for the selected patient, click the Pt Select button to close the Patient Selector pane.

You can view patient data within a selected date range: “Six Months” is selected in the example above (Figure 4-3). Select a predetermined time frame by clicking one of the values on the left of the graph: “Today” displays today’s data only, “T-1” displays data for today plus one previous day, “T-7” displays data for today plus seven previous days, and so on. “All Results” displays all available vitals data for the selected patient. If you would rather define your own dates, click the Date Range button, then set "Start with" and "Go to" dates.

You can view 15 different types of graphs for the selected date range. Select a graph type from the Graph drop-down list, or click a vital type row heading in the grid to graph that vital type. The TPR graph is selected in the example above, showing Temp, Pulse, and Respiration values.

Four Graph Options checkboxes are available on the left side of the graph. If the check boxes are not visible, right-click the screen (but not on the graph itself) and select Graph Options. This menu option may also be selected from the File menu.

Click the Values checkbox to display a numeric label for each point on the graph.

Click the Time Scale checkbox to view the graph in actual time instead of evenly distributed intervals. You can also click on a data point in the graph to see additional information about the vitals that were entered on that day.

Click the 3D checkbox to create a 3D effect on the graph. This option is only available when the Time Scale checkbox has been checked.

Click the Allow Zoom checkbox to zoom the graph view in or out. You can zoom in by clicking inside the graph and dragging a selection box around one or more data values to view in detail, or by clicking the Zoom Graph In button (the magnifying glass icon with the plus sign in the center). You can zoom out by clicking the Zoom Graph Out button (the magnifying glass icon with the minus sign in the center.) Enter a new value in the Zoom Percent text box to change the zoom percentage (default is 10). Click the Reset Zoom button to reset the Zoom Percent box to its original value.

Two additional graph options can be accessed from this window. Right-click the screen (but not on the graph itself) to display these menu options, or select them from the File menu:

Select Graph Color allows you to set the background color of the graph.

Print Graph allows you to send the graph display to a printer. The graph will be printed as it appears on the screen at the time of printing.

The remaining right-click menu options (Entered in Error, Enter Vitals, and Allergies) are described later in this chapter.

You can view a report containing general patient information by clicking the patient name button at the top left corner of the screen, by selecting Patient Inquiry from the File menu, or by selecting Pt Info from the View menu (Figure 4-4) .

<!-- image -->

Figure -

Click the Print button to print this report. Click the Close button to close this screen.

Click the Enter Vitals button to go to the Enter Vitals screen. The Hospital Location Selector window opens first (Figure 4-5). If a location has been assigned to the patient already, the Hospital Location window will not open.

<!-- image -->

Figure -

To select a location, click one of the three tabs in the Hospital Location Selector:

The Appointments tab lists all appointments for this patient for the last year. Click an appointment to select that clinic location.

The Admissions tab lists all existing admissions for this patient. Click an admission to select that hospital location.

The Name tab allows you to search for all available hospital locations. Enter the first few letters of the location name to open a list of matching locations, then click one to select it.

Click the Select button to complete the Hospital Location selection, or click the Cancel button to cancel the selection.

The Enter Vitals window opens, showing the selected patient’s name, Social Security number, and date of birth in the upper left corner of the window. The selected Hospital Location and current Date/Time are also shown at the top of the window.

<!-- image -->

Figure -

Click the Read Monitor button (Figure 4-6) to retrieve vital sign readings from a vital sign monitor (VSM) connected to the workstation. The vital sign readings that appear on the VSM screen will be sent to the "Enter Vitals" screen and pasted into the input template.

Click on the Date/Time button to select a different date or time (Figure 4-7). The default date/time is the current server date/time.

<!-- image -->

Figure -

Select a date from the calendar by clicking on it, or click Today to select the current date. Select a time either by entering in the time in the Time field, or by selecting the time using the hour and minute lists under the Time field, or click Now to select the current time. Click the Midnight button to select 12:00 midnight. Click the OK button to complete the selection, or click the Cancel button to cancel the selection. You cannot select a date/time in the future.

Select a template from the Templates list on the left side of the screen (Figure 4-6). Templates are categorized by System, Division, Location, and User. Templates for system, division, and location are available to everybody. You can select anybody’s user template as long as you have the GMV MANAGER key. If you do not have the GMV MANAGER key, only your own user templates will be available in the User category. Contact your IRMS support person if you think you should have the GMV MANAGER key.

Enter values for the vital types by typing them in the appropriate box. The default qualifiers for each vital type appear to the right of the down arrow button for each vital type. Click the down-arrow button next to each vital type to select a different qualifier, if necessary.

**Note:** BMI is calculated from Height and Weight values and cannot be entered here.

To enter a non-numeric value for a particular vital sign or measurement, use one of these options:

Click Patient on Pass to mark all vitals as "Pass" for this date/time.

Click the U… checkbox next to any vital sign to indicate that information is unavailable.

Click the R… checkbox next to any vital sign to indicate that the patient refused that measurement.

The last two options are available only if the Enable U. and/or Enable R. boxes at the top of the Enter Vitals window are checked.

Click the Save button to save the data for these vital types. Click the Save And Exit button to save the data for these vital types and close the Enter Vitals window. Click the Exit button to close the Enter Vitals window without saving any data.

The look of the Units column can be changed by checking the Units as Drop Down List box. When the Units column is set to a metric setting, the data entry for that vital type is expected to be a metric reading. If the user wants to enter the reading in US Standard format, select the US Standard format from the Units column. To make US Standard the default for a vital type, the template definition must be edited. Refer to the Creating a User Template section for more information on creating/editing templates.

Click the Exp. View button to view/hide the Template fields on the left side of the screen. Click the LatestV button to view/hide the latest vitals display on the bottom of the screen. The latest vitals display shows the most recent reading for each vital type on record for the patient. If there is no reading for a vital type (e.g., CVP), then that vital type is not listed.

#### Enter Vitals Menu Bar

You may also access the functions described above using the menu bar on the Enter Vitals screen, which allows access using only the keyboard. (See Appendix A for a complete list of access keys.)

The menu bar lies below the title bar. The Enter Vitals menu bar contains two options: **File** and **View** . Click an option on the menu bar to list all the operations you can perform from within that menu. Click the desired option to execute a specific function.

Each menu option and its corresponding suboptions display as follows:

##### File

The following options are available from the File menu:

- Patient Inquiry
- Latest Vitals Report
- Read Monitor:
- Date/Time	(Ctrl + D)
- Hospital	(Ctrl + H)
- Save
- Exit

##### View

The following options are available from the View menu:

- Expanded View
- Latest Vitals
- Enable U
- Enable R
- Unit as Drop Down List

### Entering Data for Multiple Patients

If you have taken vitals for a group of patients in one ward or unit, these instructions will help you enter the vitals for all the patients in one session. The Location and Date/Time settings remain the same throughout the session, so you can quickly enter the same vitals information for each patient in the list.

Select multiple patients by holding down the Ctrl key and clicking on specific patients, or hold down the Shift key to select a range of patients. To select an entire ward you must first select all the names in the ward.

Once you have selected the patients (Figure 4-8), click the Input Vitals for the Selected Patients button at the bottom left corner of the screen.

<!-- image -->

Figure -

No confirmation screen will appear when multiple patients are selected, but if any sensitive patients are selected, a confirmation screen will appear for each sensitive patient. You must respond to these screens before the Enter Vitals window will open.

You may receive the following warning: “You must leave the CCOW patient context to work with multiple patients.” Go to the File menu and select Break the Clinical Link to turn off the CCOW functionality.

The Hospital Location Selector window opens first (Figure 4-9). If a location has been assigned to the first patient already, the Hospital Location window will not open.

<!-- image -->

Figure -

To select a location, click one of the three tabs on the Hospital Location Selector:

The Appointments tab lists all appointments for this patient for the last year. Click an appointment to select that clinic location.

The Admissions tab lists all existing admissions for this patient. Click an admission to select that hospital location.

The Name tab allows you to search for all available hospital locations. Enter the first few letters of the location name to open a list of matching locations, then click one to select it.

Click the Select button to complete the Hospital Location selection, or click the Cancel button to cancel the selection.

The Enter Vitals window opens (Figure 4-10). The Patient List on the top left portion of the screen contains the list of patients that were previously selected. The arrow indicates which patient you are entering data for – in this example, VITPATIENT,FOUR.

<!-- image -->

Figure -

Click the Read Monitor button (Figure 4-10) to retrieve vital sign readings from a vital sign monitor (VSM) connected to the workstation. The vital sign readings that appear on the VSM screen will be sent to the "Enter Vitals" screen and pasted into the input template.

Click on the Date/Time button and select a date/time (refer to Figure 4-7). The default date/time is the current server date/time. The selected date/time appears in the top Navigation Bar.

Select a template from the Templates list on the left side of the screen (Figure 4-10). Templates are categorized by System, Division, Location, and User. Templates for system, division, and location are available to everybody. You can select anybody’s user template as long as you have the GMV MANAGER key. If you do not have the GMV MANAGER key, only your own user templates will be available in the User category. Contact your IRMS support person if you think you should have the GMV MANAGER key.

Enter values for the vital types by typing them in the appropriate box. The default qualifiers for each vital type appear to the right of the down arrow button for each vital type. Click the down arrow button next to each vital type to select a different qualifier, if necessary.

**Note:** BMI is calculated from Height and Weight values and cannot be entered here.

To enter a non-numeric value for a particular vital sign or measurement, use one of these options:

Click Patient on Pass to mark all vitals as "Pass" for this date/time.

Click the U… checkbox next to any vital sign to indicate that information is unavailable.

Click the R… checkbox next to any vital sign to indicate that the patient refused that measurement.

The last two options are available only if the Enable U. and/or Enable R. boxes at the top of the Enter Vitals window are checked.

Click the Save button to save the data for these vital types and move on to the next patient. Click the Exit button to exit the template without saving any data.

If you select another patient name without clicking the Save button, this message appears:

<!-- image -->

Figure -

Click Yes to save the original patient’s data and switch to the new patient. Click No to switch to the new patient without saving the original patient’s data.

The look of the Units column can be changed by checking the Units as Drop Down List box. When the Units column is set to a metric setting that means the data entry for that vital type is expected to be a metric reading. If the user wants to enter the reading in US Standard format then select the US Standard format from the Units column. To make US Standard the default for a vital type, the template definition must be edited. Refer to the section on Creating a User Template for more information on creating/editing templates.

Click the Exp View button to view/hide the Template fields on the left side of the screen. Click the LatestV button to view/hide the latest vitals display on the bottom of the screen. The latest vitals display shows the most recent reading for each vital type on record for the patient. If there is no reading for a vital type (e.g., CVP), then that vital type is not listed.

### Creating a User Template

Templates are a set of vitals/measurements grouped together to make data entry simpler and easier. If the system parameter Allow User Templates in the Vitals Manager module is checked, you may create/edit your own templates in this screen. If Allow User Templates is not checked, then the creation of user templates is not allowed. Refer to the section called Editing System Parameters in the Using Vitals Manager chapter for more information.

To create/edit a template for a system, division, or location refer to the section called Creating/Editing a Template in the Using Vitals Manager chapter of this manual.

To create or edit a user template, go through the main menu bar and select File, Edit User Templates. The following window appears (Figure 4-12).

<!-- image -->

Figure -

You can only see templates that you created in this window: if you have not created any templates, all fields in this window will be empty. Click the New Template button at the bottom of the window to create a new template for yourself as a user.

<!-- image -->

Figure -

Enter a name for the template in the Template Name field (maximum length is 30 characters) (Figure 4-13). The name should help the user distinguish what the template does. Click the OK button to continue.

<!-- image -->

Figure -

Your new blank template appears in the list on the left side of the screen (Figure 4-14). Click on the name of your new template to select it. Enter a short description of the template in the Description field (maximum length is 50 characters). This field is optional.

Now you can edit your template to add vital types and qualifiers to it. Click the Add button on the right side of the screen (Figure 4-14) to add vital types to the template. The following window appears.

<!-- image -->

Figure -

Click on each of the vital types you want to add to your template (Figure 4-15). You may select multiple vital types by holding down the Ctrl key and selecting multiple vital types, or hold down the Shift key to select a range of vital types.

<!-- image -->

Figure -

Your template now has vital types, but no default qualifiers (Figure 4-16). To assign default qualifiers you must select each vital type to edit it. Select a vital type by clicking on it, and the qualifiers for that vital type appear in a dropdown list on the bottom portion of the screen.

<!-- image -->

Figure -

Select the qualifiers desired by selecting from the dropdown list. Only one qualifier can be selected from each category (Figure 4-17). You can select US or Metric scale from the Measurement box for each vital type where appropriate. US Standard is the default.

<!-- image -->

Figure -

Now your template is complete (Figure 4-18). Click Save to save this new template and add it to the User Templates list. The template is ready to use.

If you would like to edit an existing User Template, click the template name in the User Templates list to select it. Any of the following items may be updated:

Change the Template Name (up to 30 characters)

Change the Template Description (up to 50 characters)

To add a new vitals type, click the plus sign button and select one or more vitals types

To delete an existing vital type, select the vital type and then click the minus sign button

To add or modify qualifiers for a vital type, select the vital type and then check or clear the checkboxes in  the Qualifiers list. If no qualifiers are available for the selected vital type, the Qualifiers list will be empty.

When you are finished making changes to the template, click the Save button at the bottom of the window. The template is ready to use.

If you would like to delete an existing User Template, click the template name in the User Templates list to select it, then click the Delete button at the bottom of the window.

Click the Close button at the bottom of the window to return to the main Vitals window.

### Viewing Allergies

To view any allergies this patient may have, click on the Allergies button at the top of the main Vitals window. The Allergy Display screen opens (Figure 4-19).

<!-- image -->

Figure -

Click the Close button to close this window.

### Marking Vitals as Entered in Error

Vitals data values cannot be deleted once they have been saved – if incorrect vitals data have been saved, they must be marked "Entered in Error" and replaced with corrected data. Any data values that have been marked "in error" will continue to be stored in the Vitals database, but will not be displayed in the patient’s data grid and graph.

Users can mark any vitals that were incorrectly entered as “entered in error” by using this option. Users will still need to go back and enter a new entry to correct the entry that will be marked as entered in error. Refer to Entering Vitals Data for more information.

To mark vitals data as entered in error, a patient must be selected in the main Vitals window.

Locate the incorrect vitals data, then click its column heading in the graph (Figure 4-20). The Entered In Error window opens, listing all the vitals entries for the selected date.

<!-- image -->

Figure -

Alternately, you can right-click on the graph and select Entered In Error from the pop-up menu or from the File menu. Select a date by clicking the down-arrow button to display a calendar. The default date is today. September 15, 2005 is selected in this example.

Select the incorrect entry by clicking on the entry – Blood Pressure is selected in this example (Figure 4-20). You can select multiple entries by holding down the Shift key or the Control key and clicking the entries to select them.

Select the reason the entry or entries are incorrect by clicking the appropriate radio button in the Reason section. Click the Mark as Entered in Error button to mark the vitals as entered in error.

**Note:** Records entered through the Clinical Observations (CliO) package cannot be changed to Entered in Error here. They must be addressed in the CliO package.

<!-- image -->

Figure -

A confirmation screen appears (Figure 4-21). Click the Yes button to confirm the entry is correct. Click the No button to select a different entry.

You may now enter new vitals data to replace the incorrect entries, if necessary.

To print a list of all Entered In Error vitals for this patient, see the Printing a Report section.

*This page intentionally left blank for double-side printing.*

## 5 Reports

The Vitals module is used to print several different Vitals reports. The viewing and printing of these reports is discussed in this chapter. The Vitals module also lets the user enter vitals data, create user templates, view allergies, mark incorrect vitals as entered in error, and edit user preferences for data display on the vitals data table, these topics are discussed in the Entering Vitals Data chapter in this manual.

**This chapter shows you how to:**

1.	View a graphic report

2.	Print a report

### Viewing a Graphic Report

When a patient is selected in the main Vitals window, existing vitals data values are displayed on the right side of the window in a graph (top) and a grid (bottom). The time scale runs from left to right, displaying the most recent values on the far right. You can select a date range and a type of graph to narrow down the amount of data to be displayed.

To view a graphic report for a particular patient, use one of the following methods to select a date range from the box on the top left side of the reports screen:

Click a predetermined time frame from the box on the left of the graph. TODAY displays today’s data only, T-1 displays data for today plus one previous day, T-7 displays data for today plus seven previous days, and so on up to Two Years worth of past data. All Results displays all available vitals data for the selected patient.

Click Date Range to select a customized date range, then set "Start with" and "Go to" dates.

All data within the selected date range is displayed in the graph and grid. This example shows the graph portion only (Figure 5-1):

<!-- image -->

Figure -

You can view 15 different types of graphs for the selected date range for this patient. Select a graph type from the Graph drop-down list next to the slider bar, or click a vital type row heading in the grid to graph that particular vital type. The “TPR” graph is selected in this example (Figure 5-1), showing Temp, Pulse, and Respiration values.

Note: Intake and Output values are obtained from the I&amp;O application and displayed in the bottom rows of the data grid. These rows show the total amount of liquid for the day, in milliliters, and do not include solids. Because these rows display total values, the Entered By and Location values are not tracked for Intake and Output.

Four Graph Options checkboxes are available on the left side of the graph. If the check boxes are not visible, right-click the screen (but not on the graph itself) and select Graph Options. This menu option may also be selected from the File menu.

Click the Values checkbox to display a numeric label for each point on the graph.

Click the Time Scale checkbox to view the graph in actual time instead of evenly distributed intervals. You can click on a data point in the graph to see additional information about the vitals that were entered that day.

Click the 3D checkbox to create a 3D effect on the graph. This option is only available if the Time Scale checkbox has been checked.

Click the Allow Zoom checkbox to zoom the graph view in or out. You can zoom in by clicking inside the graph and dragging a selection box around one or more data values to view them in detail, or by clicking the Zoom Graph In icon (the magnifying glass icon with the plus sign in the center). You can zoom out by clicking the Zoom Graph Out button (the magnifying glass icon with the minus sign in the center.) Enter a new value in the Zoom Percent text box to change the zoom percentage (default is 10). Click the Reset Zoom button to reset the Zoom Percent box to its original value.

Two additional graph options can be accessed from this window. Right-click the screen (but not on the graph itself) to display these menu options, or select them from the File menu:

Select Graph Color allows you to set the background color of the graph.

Print Graph allows you to send the graph display to a printer. The graph will be printed as it appears on the screen at the time of printing, for the selected patient only.

### Printing a Report

Four standard reports are available in the Vitals application:

Cumulative Vitals Report	Available for single patient, entire ward, or selected rooms on a ward

Latest Vitals by Location	Available for an entire ward

Latest Vitals Display for a Patient	Available for single patient only

Vitals Entered in Error for a Patient	Available for single patient only

These reports cannot be viewed on-screen; they must be sent to a printer. These reports require a printer that can handle 80 or more columns:

To print a report, go through the main menu bar and select Reports, then select the report you want to queue. The following window appears (Figure 5-2).

<!-- image -->

Figure -

The selected report appears in the Select Report field. You may select a different report from the drop-down list in this field, if necessary.

In the Include Patients section, you may select a specific patient, an entire ward, or specific rooms/beds on a ward. The default patient is the currently selected patient. Ward and Room/Beds do not apply when a specific patient is selected.

Enter a Start Date and an End Date for the selected report, if appropriate. The default date for Start Date and End Date is today. Start/End dates do not apply when printing the Latest Vitals by Location report, or the Latest Vitals Display for a Patient report.

Select a device from the Select Device field by typing in a partial name and selecting the appropriate device from the list.

You can also select a date/time to print this report (default is today). Reports cannot be queued to print for a past date/time.

Click the Print button to print the report. A dialog box appears indicating the success or failure of the queuing of the report.

**Note:** As of Patch GMRV*5.0*23, three reports were moved from the File menu to the Reports menu:

- Patient Inquiry
- Allergies
- Data Grid Report

In addition, a new report, Graph Report, was added to the Reports menu. The Graph Report option was added to convey trending information to users using screen readers.

## 6 Appendix A – Access Key Listing

The following is a listing of access keys for the Vitals and Vitals Manager applications.

| **Screen**                  | **Option / Button Text**                  | **Access Key**   | **Shortcut  Key #1**   | **Shortcut  Key #2**   |
|-----------------------------|-------------------------------------------|------------------|------------------------|------------------------|
| Main User                   | **File**  Menu                            | Alt + F          |                        |                        |
|                             | Enter Vitals                              | E                | Ctrl + E               |                        |
|                             | Printer Setup                             | P                | Ctrl + P               |                        |
|                             | Entered in Error                          | N                | Ctrl + R               |                        |
|                             | Edit User templates                       | U                | Ctrl + U               |                        |
|                             | User Options                              | S                | Ctrl + S               |                        |
|                             | Rejoin Clinical Link                      | R                |                        |                        |
|                             | Use this Application’s Data               |                  | Ctrl + A               |                        |
|                             | Use Global Data                           |                  | Ctrl + G               |                        |
|                             | Break the Clinical Link                   | B                | Ctrl + B               |                        |
|                             | Show Status                               | H                | Ctrl + O               |                        |
|                             | Select Graph Color                        | C                | Ctrl + Alt + C         |                        |
|                             | Print Graph                               | I                | F9                     |                        |
|                             | Exit                                      | X                | Ctrl + Alt + X         |                        |
|                             |                                           |                  |                        |                        |
|                             | **Reports**  Menu                         | Alt + P          |                        |                        |
|                             | Patient Inquiry                           | P                | Ctrl + Alt + Q         |                        |
|                             | Allergies                                 | R                | Ctrl + L               |                        |
|                             | Data Grid Report                          | D                | Ctrl + Alt + G         |                        |
|                             | Graph Report                              | G                | Ctrl + Alt + R         |                        |
|                             | Cumulative Vitals Report                  | C                | Ctrl + F1              |                        |
|                             | Latest Vitals by Location                 | L                | Ctrl + F2              |                        |
|                             | Latest Vitals Display for a Patient       | A                | Ctrl + F3              |                        |
|                             | Print Vitals Entered in Error for Patient | I                | Ctrl + F4              |                        |
|                             |                                           |                  |                        |                        |
|                             | **View**  Menu                            | Alt + V          |                        |                        |
|                             | Graph Options                             | G                | Ctrl + Alt + O         |                        |
|                             | Pt Select                                 | S                | Ctrl + Alt + S         |                        |
|                             |                                           |                  |                        |                        |
|                             | **Help**  Menu                            | Alt + H          |                        |                        |
|                             | Index                                     | I                | Ctrl + X               |                        |
|                             | Vitals Web Site                           | W                | Ctrl + W               |                        |
|                             | About                                     | A                | Ctrl + T               |                        |
|                             |                                           |                  |                        |                        |
|                             | Unit button                               |                  | Alt + U                |                        |
|                             | Ward button                               |                  | Alt + W                |                        |
|                             | Team button                               |                  | Alt + T                |                        |
| Main User  (cont)           | Clinic button                             |                  | Alt + C                |                        |
|                             | All button                                |                  | Alt + A                |                        |
|                             | Patient List                              |                  | Alt + I                |                        |
|                             | Date                                      |                  | Alt + D                |                        |
|                             | Graph                                     |                  | Alt + G                |                        |
|                             | Values checkbox                           |                  | Alt + L                |                        |
|                             | Time Scale checkbox                       |                  | Alt + M                |                        |
|                             | 3D checkbox                               |                  | Alt + 3                |                        |
|                             | Allow Zoom checkbox                       |                  | Alt + Z                |                        |
|                             | Enter Vitals button                       |                  | Alt + E                |                        |
|                             | Patient Inquiry button                    |                  | Ctrl + I               |                        |
|                             | Print                                     |                  | Ctrl + P               | F9                     |
|                             | Allergies button                          |                  | Alt + R                | Ctrl + L               |
|                             | Pt Select button                          |                  | Alt + S                | Ctrl+Alt+S             |
| Enter Vitals                |                                           |                  |                        |                        |
|                             | Templates                                 |                  | Alt + T                |                        |
|                             | Date/Time button                          |                  | Alt + D                | Ctrl + D               |
|                             | Hospital button                           |                  | Alt + H                | Ctrl + H               |
|                             | Exp View button                           |                  | Alt + W                |                        |
|                             | Latest V button                           |                  | Alt + V                |                        |
|                             | Enable U.                                 |                  | Alt + U                |                        |
|                             | Enable R                                  |                  | Alt + R                |                        |
|                             | Patient on Pass                           |                  | Alt + P                |                        |
|                             | Units as Drop Down List                   |                  | Alt + N                |                        |
|                             | Save And Exit button                      |                  | Alt + A                |                        |
|                             | Save button                               |                  | Alt + S                |                        |
|                             | Exit button                               |                  | Alt + X                |                        |
|                             | Read Monitor                              |                  | Alt + M                |                        |
| Hospital Location  Selector | Appointments tab                          |                  | Alt + P                |                        |
|                             | Admissions tab                            |                  | Alt + M                |                        |
|                             | Name tab                                  |                  | Alt + N                |                        |
|                             | Select button                             |                  | Alt + S                |                        |
|                             | Cancel button                             |                  | Alt + C                |                        |
| Select Date/Time            |                                           |                  |                        |                        |
|                             | OK button                                 |                  | Alt + O                |                        |
|                             | Cancel button                             |                  | Alt + C                |                        |
|                             | Today button                              |                  | Alt + T                |                        |
|                             | <<< button                                |                  | Alt + <                |                        |
|                             | >>> button                                |                  | Alt + >                |                        |
|                             | Now button                                |                  | Alt + N                |                        |
|                             | Midnight button                           |                  | Alt + M                |                        |
|                             | Time                                      |                  | Alt + I                |                        |
| Printer Setup               |                                           |                  |                        |                        |
|                             | Name                                      |                  | Alt + N                |                        |
|                             | Properties                                |                  | Alt + P                |                        |
|                             | Size                                      |                  | Alt + Z                |                        |
|                             | Source                                    |                  | Alt + S                |                        |
|                             | Portrait                                  |                  | Alt + O                |                        |
|                             | Landscape                                 |                  | Alt + A                |                        |
|                             | Network                                   |                  | Alt + W                |                        |
| Entered In Error            |                                           |                  |                        |                        |
|                             | Select Date                               |                  | Alt + D                |                        |
|                             | Incorrect Date/Time                       |                  | Alt + T                |                        |
|                             | Incorrect Reading                         |                  | Alt + R                |                        |
|                             | Incorrect Patient                         |                  | Alt + P                |                        |
|                             | Invalid Record                            |                  | Alt + E                |                        |
|                             | Mark as Entered in Error                  |                  | Alt + M                |                        |
|                             | Cancel                                    |                  | Alt + C                |                        |
|                             |                                           |                  |                        |                        |
| Create/Edit user templates  | Create/Edit user templates                |                  |                        |                        |
|                             | **File**  Menu                            | Alt + F          |                        |                        |
|                             | New Template                              | W                |                        |                        |
|                             | Delete                                    | D                |                        |                        |
|                             | Save                                      | S                |                        |                        |
|                             | Exit                                      | X                |                        |                        |
|                             |                                           |                  |                        |                        |
|                             | **Vitals**  Menu                          |                  |                        |                        |
|                             | Add                                       | A                |                        |                        |
|                             | Delete                                    | D                |                        |                        |
|                             | Down                                      | W                |                        |                        |
|                             | Up                                        | U                |                        |                        |
|                             |                                           |                  |                        |                        |
|                             | User Templates                            |                  | Alt + U                |                        |
|                             | Template Name                             |                  | Alt + N                |                        |
|                             | Description                               |                  | Alt + E                |                        |
|                             | Template Vitals                           |                  | Alt + V                |                        |
|                             | Metric                                    |                  | Alt + M                |                        |
|                             | Up arrow icon                             |                  | Ctrl + U               |                        |
|                             | Down arrow icon                           |                  | Ctrl + W               |                        |
|                             | Plus sign icon                            |                  | Ctrl + A               |                        |
|                             | Minus sign icon                           |                  | Ctrl + D               |                        |
|                             | Delete                                    |                  | Alt + D                |                        |
|                             | Save                                      |                  | Alt + S                |                        |
|                             | New Template                              |                  | Alt + W                |                        |
|                             | Close                                     |                  | Alt + C                |                        |
|                             |                                           |                  |                        |                        |
| Templates                   | Templates                                 |                  |                        |                        |
|                             | Name                                      | Alt + N          |                        |                        |
|                             | Description                               | Alt + E          |                        |                        |
|                             | Up                                        | Ctrl +U          |                        |                        |
|                             | Down                                      | Ctrl + W         |                        |                        |
|                             | Add                                       | Ctrl + A         |                        |                        |
|                             | Delete                                    | Alt + D          |                        |                        |
|                             | Metric                                    | Alt + M          |                        |                        |
|                             | Default                                   | Alt + L          |                        |                        |
|                             |                                           |                  |                        |                        |
| User Preferences            | User Preferences                          |                  |                        |                        |
|                             | Defaults                                  |                  | Alt + D                |                        |
|                             | Apply                                     |                  | Alt + A                |                        |
|                             | OK                                        |                  | Alt + O                |                        |
|                             | Cancel                                    |                  | Alt + C                |                        |
|                             | Text (Normal Values)                      |                  | Alt + T                |                        |
|                             | Background (Normal Values)                |                  | Alt + B                |                        |
|                             | Text (Abnormal Values)                    |                  | Alt + X                |                        |
|                             | Background (Abnormal)                     |                  | Alt + G                |                        |
|                             | Search Delay                              |                  | Alt + S                |                        |
|                             |                                           |                  |                        |                        |
| Report Options              | Report Options                            |                  |                        |                        |
|                             | Select Report                             |                  | Alt + R                |                        |
|                             | Patient                                   |                  | Alt + T                |                        |
|                             | Patients Located at                       |                  | Alt + L                |                        |
|                             | Start Date                                |                  | Alt + S                |                        |
|                             | End Date                                  |                  | Alt + E                |                        |
|                             | Device                                    |                  | Alt + D                |                        |
|                             | Queue To Run At                           |                  | Alt + Q                |                        |
|                             | Print                                     |                  | Alt + P                |                        |
|                             | Cancel                                    |                  | Alt +C                 |                        |
|                             |                                           |                  |                        |                        |
| Vitals Manager              | Vitals Manager                            |                  |                        |                        |
|                             | **File**  Menu                            | Alt + F          |                        |                        |
|                             | Print Qualifiers Table                    | P                |                        |                        |
|                             | Exit                                      | X                |                        |                        |
|                             | **System Parameters**  Menu               | Alt + S          |                        |                        |
|                             | Save Systems Parameters                   | S                |                        |                        |
|                             | **Abnormal Values**  Menu                 | Alt + B          |                        |                        |
|                             | Save Abnormal Values                      | A                |                        |                        |
|                             | **Templates**  Menu                       | Alt + T          |                        |                        |
|                             | New Template …                            | N                |                        |                        |
|                             | Save Template                             | S                |                        |                        |
|                             | Delete Template …                         | D                |                        |                        |
|                             | Set Default Template                      | E                |                        |                        |
| Qualifiers                  |                                           | Alt + Q          |                        |                        |
|                             | **Help**  Menu                            | Alt + H          |                        |                        |
|                             | Index                                     | I                |                        |                        |
|                             | Contents                                  | C                |                        |                        |
|                             | Vitals Website                            | W                |                        |                        |
|                             | About                                     | A                |                        |                        |
|                             |                                           |                  |                        |                        |
| System Parameters           | System Parameters                         |                  |                        |                        |
|                             | Allow User Templates                      | Alt + U          |                        |                        |
|                             | Help Menu Web Address                     | Alt + W          |                        |                        |
|                             | Version Compatibility                     | Alt + V          |                        |                        |
|                             |                                           |                  |                        |                        |

This page intentionally left blank for double-side printing.

## 7 Appendix B – Customizing the Client Installation

The client installation by default installs and builds the icons and program folder items without any command line switches. Vitals/Measurements utilizes the ServerList utility of the RPC Broker for selecting a server to connect to if it is configured on the client workstation. Instructions for configuration and utilization of the ServerList utility can be found in the RPC Broker documentation located on the VDL. If the ServerList utility has not been configured on the client, the applications by default will attempt to connect to the server identified in the users HOSTS file as BROKERSERVER on Listener Port 9200. Adding command line parameters to the shortcuts as shown below by right clicking the appropriate Vitals/Measurements application icon and selecting the Properties menu item can easily override these parameters.

<!-- image -->

Figure -

The above (Figure 7-1) is a standard properties view of the Vitals icon as displayed when right clicking the icon. Select the Shortcut tab to proceed with customization.

<!-- image -->

Figure -

This example (Figure 7-2) will attempt to connect the application to the server identified in your HOSTS file as *yourserver* and will use listener port 9200.

Vitals/Measurements V. 5.0 command line parameters available from the command prompt or within Windows shortcut definitions are:

Vitals.exe	 [ **/server** = *servername* ] [ **/port** = *listenerport* ] 
 [ **/tempdir** = *temporarydirectory* ] [ **/helpdir** = *helpdirectory* ] [ **/debug** ={on|off}] [/ **noccow** ] [/ **ccow** =patientonly]

VitalsManager.exe	 [ **/server** = *servername* ] [ **/port** = *listenerport* ] [ **/helpdir** = *helpdirectory* ]
 [ **/debug** ={on|off}]

| **Switches**   |          | **Description**                                                                                                                                                                                                                                | **Example**       |
|----------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| /server        | /server  | Specifies an alternate server to connect to. The server must be defined in the clients hosts. file.  Default Hosts. file locations:  NT 4.0/W2K = c:\winnt\system32\drivers\etc\hosts.  Windows 9x = c:\windows\hosts.  Default = BROKERSERVER | /server=vista     |
| /port          | /port    | Specifies an alternate listener port on the selected server. This is the TCP/IP port that the broker is running on VistA server.  Default = 9200                                                                                               | /port=9200        |
| /tempdir       | /tempdir | Location accessible to the client workstation and current user for storage of temporary scratch files.  Default =  *application\_directory*  \temp                                                                                             | /tempdir=C:\temp  |
| /helpdir       | /helpdir | Location of the Vitals/Measurements windows help files.  Default =  *application\_directory*  \help                                                                                                                                            | /helpdir=C: \help |
<!-- rpc-table -->
| /debug         | /debug   | Set the debug mode for both the RPC Broker and the Vitals/Measurements application.  Default = Off.                                                                                                                                            |                   |
|                |          |                                                                                                                                                                                                                                                |                   |
|                |          |                                                                                                                                                                                                                                                |                   |

This page intentionally left blank for double-side printing.

## 8 Appendix C – Using Vitals in CPRS

Patch GMRV*5.0*3 provides a Dynamic Link Library (DLL) file that allows other applications to use a limited set of Vitals/Measurements features within their own applications. This DLL is currently used by CPRS v26 or later, and the features appear on screen as part of the Vitals Lite window.

The DLL name is **GMV\_VitalsViewEnter.dll** and it is automatically installed as part of the patch. This DLL is not called by the Vitals.exe or VitalsManager.exe files that make up the Vitals Graphical User Interface (GUI), and it does not need to be registered in the Windows registry.

### Overview of Vitals Lite

When the user clicks on the Vitals section of the CPRS Cover Sheet, the DLL is invoked and the Vitals Lite window opens. From this window, the user can:

View patient vitals data in a graph and grid format.

Select date ranges for retrieving data

Select vital types, intake and output values (liquid values only) to plot on the graph

Use zoom features to view the graph data

Display numerical values for each point on the graph

Display the graph in 3-D format

Print a graph to a Windows-type printer

View the qualifier abbreviations along with the numerical values in the grid

View the name of the person who entered the data and the hospital location associated with the record in the grid (except for I&amp;O values)

Change the background color of the graph

Enter vitals data using existing input templates

Mark existing records as entered in error

Display patient allergy data.

The following sections describe the Vitals Lite functionality in CPRS. See the CPRS User Guide in the VistA Documentation Library for more detailed information about CPRS.

### Opening the Vitals Lite window in CPRS

In CPRS, select a patient and open the Cover Sheet. Click anywhere inside the Vitals section to open the Vitals Lite window:

<!-- image -->

The Vitals Lite window displays the selected patient’s vitals and measurements in a graph and a spreadsheet-like grid. The next three sections describe how to view existing vitals, enter vitals, and correct vitals for this patient.

### Viewing Data in Vitals Lite

<!-- image -->

The time scale runs from left to right, displaying the most recent values on the far right side of the graph and grid. You can move left and right across the graph by moving the slider bar between the graph and the grid.

You can view patient data within a selected date range: “Six Months” is selected in the example above. Select a predetermined time frame by clicking one of the values on the left of the graph: “Today” displays today’s data only, “T-1” displays data for today plus one previous day, “T-7” displays data for today plus seven previous days, and so on. “All Results” displays all available vitals data for the selected patient. If you would rather define your own dates, click the Date Range button, then set "Start with" and "Go to" dates.

The patient data on the grid can also be viewed as a text report, by selecting Data Grid Report from the File menu.

You can view 15 different types of graphs for the selected date range. Select a graph type from the Graph drop-down list, or click a vital type row heading in the grid to graph that vital type. The TPR graph is selected in the example above, showing Temp, Pulse, and Respiration values.

Four Graph Options checkboxes are available on the left side of the graph. If the check boxes are not visible, right-click the screen (but not on the graph itself) and select Graph Options. This menu option may also be selected from the File menu.

Click the Values checkbox to display a numeric label for each point on the graph.

Click the Time Scale checkbox to view the graph in actual time instead of evenly distributed intervals. You can also click on a data point in the graph to see additional information about the vitals that were entered on that day.

Click the 3D checkbox to create a 3D effect on the graph. This option is only available if the Time Scale checkbox is checked.

Click the Allow Zoom checkbox to zoom the graph view in or out. You can zoom in by clicking inside the graph and dragging a selection box around one or more data values to view in detail, or by clicking the Zoom Graph In button (the magnifying glass icon with the plus sign in the center). You can zoom out by clicking the Zoom Graph Out button (the magnifying glass icon with the minus sign in the center.) Enter a new value in the Zoom Percent text box to change the zoom percentage (default is 10). Click the Reset Zoom button to reset the Zoom Percent box to its original value.

Two additional graph options can be accessed from this window. Right-click the screen (but not on the graph itself) to display these menu options, or select them from the File menu:

Select Graph Color allows you to set the background color of the graph.

Print Graph allows you to send the graph display to a printer. The graph will be printed as it appears on the screen at the time of printing.

The remaining right-click menu options (Entered in Error, Enter Vitals, and Allergies) are described later in this chapter.

You can view a report containing general patient information by clicking on the patient name button at the top left corner of the screen, or by selecting Patient Inquiry from the File menu.

### Entering Vitals in Vitals Lite

Click the Enter Vitals button at the top of the Vitals Lite window. The Enter Vitals window for the selected patient opens:

<!-- image -->

**NOTE:** If you have access to the Encounter button, the Enter Vitals window can also be opened from the CPRS Notes tab:

In the Notes window, click the Encounter button and select an existing appointment or admission, or create a new one.

In the Encounter window, click the Vitals tab, then click the Enter Vitals button to invoke the DLL and open the Enter Vitals window. The user will be able to enter vitals data using existing input templates.

The Enter Vitals window opens, showing the selected patient’s name, Social Security number, and date of birth in the upper left corner of the window. The selected Hospital Location and current Date/Time are also shown at the top of the window.

Click the Read Monitor button to retrieve vital sign readings from a vital sign monitor (VSM) connected to the workstation.

Click the Date/Time button to select a different date or time.

Click the Hospital button to select a different hospital location.

The list of available vital types is determined by the template that is selected. Select a template from the Templates list on the left side of the window. See page 2-6 for information about using the Vitals Manager module to create and update templates.

Enter values for the vital types by typing them in the appropriate box. The default qualifiers for each vital type appear to the right of the down arrow button for each vital type. To select a different qualifier, click the down-arrow button next to each vital type.

**NOTE:** To enter a non-numeric value for a particular vital sign or measurement, use one of these options:

Click Patient on Pass to mark all vital signs as "Pass" for this date/time.

Click the U… checkbox next to any vital to indicate that information is unavailable.

Click the R… checkbox next to any vital to indicate that the patient refused that measurement.

The last two options are available only if the Enable U. and/or Enable R. boxes at the top of the Enter Vitals window are checked.

Click the Save button to save the data for these vital types. Click the Save And Exit button to save the data for these vital types and close the Enter Vitals window. Click the Exit button to close the window without saving any data.

### Correcting Vitals in CPRS

Vitals data values cannot be deleted once they have been saved – if incorrect vitals data have been saved, they must be marked "Entered in Error" and replaced with corrected data. Any data values that have been marked "in error" will continue to be stored in the Vitals database, but will not be displayed in the patient’s data grid and graph.

Users can mark any vitals that were incorrectly entered as “entered in error” by using this procedure. Users will still need to go back and add a new entry to correct the entry that will be marked as entered in error.

Click the Entered in Error button at the top of the Vitals Lite window, or right-click on the grid and select Entered In Error from the pop-up window, or from the File menu. The Entered in Error window for the selected patient opens:

<!-- image -->

**Note:** Records entered through the Clinical Observations (CliO) package cannot be changed to Entered in Error here. They must be addressed in the CliO package.

Select a date by clicking the down-arrow button to display a calendar. The default date is today. October 9, 2005 is selected in the example above.

Select the incorrect vitals entry by clicking it – Pain is selected in the example above. You can select multiple entries by holding down the Ctrl key and clicking the entries to select them.

Select the reason the entry or entries are incorrect by clicking the appropriate radio button in the Reason section. Click the Mark as Entered in Error button to mark the vitals as entered in error.

You may now enter new vitals data to replace the incorrect entries, if necessary

## 9 Glossary

Access Code   A unique sequence of characters known by and assigned only to the user, the system manager and/or designated alternate(s). The access code (in conjunction with the verify code) is used by the computer to identify authorized users.

ADP Coordinator / ADPAC / Application Coordinator    Automated Data Processing Application Coordinator. The person responsible for implementing an application developed to support a specific functional area such as Nursing, PIMS, etc.

Application   A system of computer programs and files that have been specifically developed to meet the requirements of a user or group of users. Examples of VistA applications are the PIMS and Vitals/Measurements application.

Application Data   From a CCOW perspective, this is the patient record that is open in the active application. When joining a clinical context, select Use Application Data to force all open CCOW-compliant applications to switch to the patient that is open in the active application.

Archive   The process of moving data to some other storage medium, usually a magnetic disk, and deleting the information from active storage in order to free-up disk space on the system.

Backup Procedures   The provisions made for the recovery of data files and program libraries and for restart or replacement of ADP equipment after the occurrence of a system failure.

BMI   A patient's body mass index, which is calculated by dividing the person's weight in kilograms by the square of his height in meters.

Bulletin   A canned message that is automatically sent by MailMan to a user when something happens to the database.

CCOW   Clinical Context Object Workgroup standard. CCOW provides a way for applications to know which other applications are running and which patients are selected in those applications. This standard allows for synchronization of patient data across all open applications.

Data Dictionary   A description of file structure and data elements within a file.

DLL   Dynamic Link Library

Device   A hardware input/output component of a computer system (e.g., CRT, printer).

Edit   Used to change/modify data typically stored in a file.

Field   A data element in a file.

File   The M construct in which data is stored for retrieval at a later time. A group of related records.

File Manager or FileMan    Within this manual, FileManager or FileMan is a reference to VA FileMan. FileMan is a set of M routines used to enter, edit, print, and sort/ search related data in a file; a data base.

Global   An M term used when referring to a file stored on a storage medium, usually a magnetic disk. In the Vitals software, for example, vitals data is stored in one global, and patient data is stored in another global.

Global Data    From a CCOW perspective, this is the patient record that all CCOW-compliant applications are focused on. When joining a clinical context, select Use Global Data to synchronize the active application with the patient that is open in the other applications.

GMRV   This signifies the General Medical Record namespace assigned to the Vitals/Measurements application.

GMRY   This signifies the General Medical Record namespace assigned to the Intake and Output application.

GMV   Vitals/Measurements namespace, parent package to GMRV.

GUI   Graphical User Interface – a Windows-like screen that uses pull-down menus, icons, pointer devices, and other metaphor-type elements that can make a computer program more understandable, easier to use, allow multi-processing (more than one window or process available at once), and so on.

I&amp;O   The Intake and Output application.

IRMS   Information Resource Management Service.

Kernel   A set of software utilities. These utilities provide data processing support for the application packages developed within the VA. They are also tools used in configuring the local computer site to meet the particular needs of the hospital. The components of this operating system include: MenuMan, TaskMan, Device Handler, Log-on/Security, and other specialized routines.

M   Formerly known as MUMPS or the Massachusetts (General Hospital) Utility Multi-Programming System. This is the programming language used for all VistA applications.

MailMan   An electronic mail, teleconferencing, and networking system.

Menu   A set of options or functions available to users for editing, formatting, generating reports, etc.

Module   A component of the Vitals software application that covers a single topic or a small section of a broad topic.

Namespace   A naming convention followed in the VA to identify various applications and to avoid collision between applications. It is used as a prefix for all routines and globals used by the application. The Vitals package uses GMV as its namespace.

OIFO   Office of Information Field Office, formerly known as Information Resource Management Field Office, and Information Systems Center.

Option   A functionality that is invoked by the user. The information defined in the option is used to drive the menu system. Options are created, associated with others on menus, or given entry/exit actions. For example, the GMV V/M GUI is the main menu for the Vitals/Measurements application.

Package   Otherwise known as an application. A set of M routines, files, documentation and installation procedures that support a specific function within VistA (e.g., the ADT and Vitals/Measurements applications).

Password   A protected word or string of characters that identifies or authenticates a user, a specific resource, or an access type (synonymous with Verify Code).

Patient Context     From a CCOW perspective, a patient context session is created for a single client device with at least one CCOW participant "joined" to the context session. If a user is running Vitals and CPRS from a single workstation, each application is a participant in the patient context session, and when a patient record is open in one application, the same patient record is automatically opened in all other participating applications.

PIMS   Patient Information Management System previously known as the MAS Package.

Pointer   A special data type of VA FileMan that takes its value from another file. This is a method of joining files together and avoiding duplication of information.

Program   A set of M commands and arguments, created, stored, and retrieved as a single unit in M.

Protocol   A single entry point referencing multiple routine entry points to execute several inter related, required processes which perform specific functions. When multiple protocols are associated with a single procedure (i.e., intravenous lines or IV lines), they are found grouped under a single option.

Qualifier   A word that gives a more detailed description of an item.

Queuing   The scheduling of a process/task to occur at a later time. Queuing is normally done if a task uses up a lot of computer resources.

Routine   A set of M commands and arguments, created, stored, and retrieved as a single unit in M.

Security Key   A function which unlocks specific options and makes them accessible to an authorized user.

Sensitive Information   Any information which requires a degree of protection and which should be made available only to authorized users.

Site Configurable   A term used to refer to features in the system that can be modified to meet the needs of each site.

Software   A generic term referring to a related set of computer programs.

Synonym   A qualifier abbreviation appended to vitals/measurements numeric values on graphic reports.

Task Manager or TaskMan   A part of Kernel which allows programs or functions to begin at specified times or when devices become available. See Queuing.

User   A person who enters and/or retrieves data in a system, usually utilizing a CRT.

User Context     CCOW allows users to authenticate and sign-on to multiple applications that are CCOW-enabled and User Context-aware using a single set of credentials. This reduces the need for multiple ID's and passwords in the VistA clinician desktop environment. If a user is running Vitals on a workstation and the CCOW user context is enabled, additional CCOW applications can be opened automatically without requiring the user to sign in again.

Utility   An M program that assists in the development and/or maintenance of a computer system.

Verify Code   A unique security code which serves as a second level of security access. Use of this code is site specific; sometimes used interchangeably with a password.

VistA   Veterans Health Information Systems and Technology Architecture.

Vital Type   A category of vital sign or measurement (e.g., pulse, respiration, blood pressure, temperature).

Workstation   A personal computer running the Windows 9x or NT operating system.


## 11 Index

## A

Abnormal Values

appearance in Vitals, 3-4

set ranges for Vitals, 2-3

Access Keys, i, 6-1

Accessibility, 1-2

Add

a Vitals link to the CPRS Tools menu, 1-5

Qualifiers to Vitals types, 2-2

Templates, 2-6

Vitals for multiple patients, 4-10

Vitals for one patient, 4-3

Allergies

button, 3-2

view, 4-19

## B

Break the Clinical Link, 3-5

Buttons, in Vitals windows, 3-2

## C

Categories, 2-2

CCOW

break the clinical link, 3-5

overview, 3-4

rejoin the clinical context, 3-5

show status, 3-5

Context management, 3-4

Correct inaccurate Vitals Data, 4-20

CPRS, 1-6, *See* Vitals Lite

CPRS Tools Menu

add a link to Vitals, 1-5

Create a User Template, 4-14

Customize the Client Installation, 7-1

## D

Data Grid Report, 4-3

Date/Time Selector button, 3-3

Delete Vitals. *See* Entered in Error

Division Template. *See* Vitals Manager

DLL, 8-1

Documentation, 1-2

## E

Edit

Abnormal Values settings, 2-3

Qualifiers, 2-2

System Parameters, 2-4

User Options settings, 3-3

Vitals data, 4-20

Enter Vitals

for multiple patients, 4-10

for one patient, 4-3

Enter Vitals button, 3-2

Entered in Error, 4-20

Entering Vitals Data, 4-1

Expand View button, 3-3

## G

Glossary, 9-1

Graph Options

setting, 4-4

Graphic Reports, 5-1

## H

Hospital Selector button, 3-3

## I

Installation

options to customize the client, 7-1

Intake / Output, 5-2

## J

Join a clinical context, 3-5

## L

Latest Vitals button, 3-3

Location Template. *See* Vitals Manager

## M

Managing Site Files

Abnormal Values ranges, 2-3

Categories and Qualifiers, 2-2

Overview of Vitals Manager, 2-1

System Parameters, 2-4

Templates, 2-6

## N

Navigation Bars, 3-2

## O

Open

Vitals, 3-1

Vitals Manager, 2-1

Options

edit User Preferences, 3-3

Overview of GUI software, 1-2

## P

Package Operation. *See* Using Vitals

Patient Selector button, 3-2

Preferences. *See* User Options for Vitals

Print

general patient information, 4-5

Qualifiers Table report, 2-3

Vitals reports, 5-2

## Q

Qualifiers, 2-2

## R

Rejoin Clinical Context, 3-5

Reports

overview of, 5-2

printing, 5-3

viewing data in a graph, 5-1

## S

Security keys, 1-1

Shortcut Keys, i, 6-1

Show CCOW Status, 3-5

Site Files. *See* Vitals Manager

System Overview, 1-1

System Parameters, 2-4

System Template. *See* Vitals Manager

## T

Templates

creating and editing, 2-6

selecting, 4-1

types of, 2-6

User, 4-14

## U

User Options for Vitals, 3-3

User Template

create a, 4-14

delete a, 4-18

edit a, 4-18

## V

Version Compatibility. *See* System Parameters

View

Allergies, 4-19

CCOW status, 3-5

general patient information, 4-5

Intake/Output values in a report, 5-2

Vitals data in a graph, 5-1

Vitals

application features, 1-1

enter data for multiple patients, 4-10

enter data for one patient, 4-3

link to the CPRS Tools Menu, 1-5

make corrections, 4-20

Overview, 3-1

overview of main window, 3-2

selecting a template and patient, 4-1

Vitals Lite, 8-1

Vitals Manager

create or edit a Template, 2-6

edit Abnormal Values, 2-3

edit System Parameters, 2-4

Overview, 2-1

print a Qualifiers Table report, 2-3

work with Categories and Qualifiers, 2-2