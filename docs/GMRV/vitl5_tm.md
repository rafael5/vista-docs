---
app_name: Vitals/Measurements (GMRV)
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: null
doc_type: technical-manual
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
source_file: vitl5_tm.docx
status: draft
title: vitl5 tm.docx
---

<!-- image -->

**VITALS / MEASUREMENTS**

**TECHNICAL MANUAL AND**

**PACKAGE SECURITY GUIDE**

**Version 5.0**

**October 2002**

Revised September 2009

for GMRV*5.0*23


Office of Enterprise Development

###### Revision History

| **Date**       | **Revision**   | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | **Author**   |
|----------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| September 2009 | 5.0*23         | Updated for Patch GMRV*5.0*23:  - Functionality list, p. 1-1  - Vitals web link, p. 1-2  - Screen captures, Figs. 1-2,  - Virgin installation steps, p. 2-1  - Implementation Considerations, p. 2-3  - Client Requirements, p. 2-4  - Routine list, Ch. 3  - Removed  version number, p. 5-1  - Remote Procedure Call Descriptions,   5  - Removed archive/purge instructions, Ch. 6  - External Relations removed and replaced with instructions for finding them on FORUM, Ch. 8  - Removed reference to timestamp, p. 9-1  - Added Appendix A: Parameter Settings | REDACTED     |
| September 2008 | 5.0*22         | Updated for Patch GMRV*5.0*22:  - Routine Descriptions, p. 5-9 through 5-34                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | REDACTED     |
| April 2006     | 5.0*3          | Updated for Patch GMRV*5.0*3:  - Cover Page  - Revision History  - Implementation and tenance, p. 2-4  - Routine Descriptions, p. 3-1 through 3-8  - Exported Options, p. 5-1 through 5-34  - External Relations, p. 8-47 through 8-96  - Internal Relations, p. 9-1  - Software Product Security, p. 12-1                                                                                                                                                                                                                                                            | REDACTED     |
| October 2002   | 5.0            | Initial Release                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | REDACTED     |

This page intentionally left blank for double-side printing.

###### Table of Contents

1.	Introduction	1-1

Functionality	1-1

Information on GUI software	1-2

2.	Implementation and Maintenance	2-1

Description	2-1

Virgin Installation of Software	2-1

Non-Virgin Installation of Software	2-3

Implementation Considerations	2-3

Resource Requirements	2-4

3.	Routine Descriptions	3-1

4.	File List and Related Information	4-1

File Descriptions	4-1

Package Default Definition	4-1

5.	Exported Options	5-1

Delphi Components	5-1

Remote Procedure Calls (RPC)	5-1

Menu Option by Name	5-35

6.	Archiving and Purging	6-1

7.	Callable Routines	7-1

8.	External Relations	8-1

9.	Internal Relations	9-1

10.	Package-wide Variables	10-3

11.	SAC Exemptions	11-1

12.	Software Product Security	12-1

Security Management	12-1

Security Features	12-1

13.	Glossary	13-1

14.	Appendix A – Parameter Settings	14-1

This page intentionally left blank for double-side printing.

## 1 Introduction

The Vitals/Measurements application is designed to store in the patient's electronic medical record all vital signs and various measurements associated with a patient's hospital stay or outpatient clinic visit.  Data can be accessed by several  (Veterans Health Information Systems and Technology Architecture) applications (e.g., CPRS, Health Summary) that interface with the Vitals/Measurements application.

### Functionality

•	Contains a GUI (Graphical User Interface) to make editing and viewing of data easier.  Additional information on GUI software is contained at the end of this chapter.

•	Supports documentation of a patient's vital signs (e.g., temperature, pulse, and respiration).

•	Tracks a patient's height, weight, central venous pressure (CVP), circumference/girth and oxygen saturation via oximetry with supplemental oxygen information.

•	Supports documentation of detailed or positional blood pressures for a patient (i.e., bilateral blood pressures taken in a sitting, standing and lying position).

•	Associates qualifiers (alpha characters appended to the measurement's numeric value) to provide a more detailed description of the patient's vitals/measurements.

•	Contains detailed help windows to assist users in associating appropriate qualifiers with the patient vitals/measurements.

•	Prints temperature, height, and weight in both metric equivalents and  customary units.

•	Prints patient's cumulative measurements on the Vitals Signs Record and the Cumulative Vitals Report.

•	Displays latest information on all of the patient's vitals/measurements in both metric equivalents and  customary units (when appropriate) along with the date/time the information was obtained.

•	The displays include the patient's intake and output when present in the patient's database (refer to the Intake and Output application).

•	Allows facilities to establish hospital-wide high and low values for each vital sign or measurement.

•	Identifies abnormal patient values on vitals/measurements reports (those values outside the high and low range).

•	Displays graphic reports on workstation monitors.

•	Provides APIs so other  applications can send or receive patient data.

•	Records a reason for the omission of a patient's vitals/measurements.

•	Supports an interface to vital signs monitor connected to the workstation.

### Information on GUI software

Internet WWW Documentation

Documentation for this product (including user manual, technical manual and package security guide, release notes, and installation guide) is available on the Internet (World Wide Web) from the [VHA Software Document Library (VDL)](http://www.va.gov/vdl/) &lt;http://www.va.gov/vdl/&gt;:

REDACTED

**GUI and Windows**

GUI stands for Graphical User Interface, most frequently seen as the Windows screen.  If you have already used programs with these screens, then the Vitals GUI screen will seem familiar to you.  The Vitals GUI is only implemented on the Microsoft Windows platform at this time.

If you have little or no familiarity with Windows, you can browse through the Windows help file for information about the basics of using Windows.  Also, see the next few paragraphs for brief descriptions of some GUI features.

To access the Windows Help File, click the Start button in the taskbar and click Help.  Use this help file as a reference whenever you have general questions about Windows.

The following is an example of what a GUI screen looks like (Fig. 1-1):

Fig. 1-1

**Windows**

An “application window” is the area on your computer screen used by a program.  If you have more than one program running at the same time, you can go from one program to another by clicking in each application window.  The currently active window contains a colored bar (usually blue) at the top of the window.  An inactive window contains a gray bar at the top of the window.  You can also move, close, or minimize the application window to make room for another window.  (See Help in Windows for further instructions on these functions.)

<!-- image -->

<!-- image -->

<!-- image -->

Fig. 1-2

**Pop-up Windows**

These are “mini” windows that pop up within a window to provide or request information.  Usually they require some action before they will go away.  Clicking on buttons with the words &lt;Cancel&gt;, &lt;Exit&gt;, or something similar closes these windows.

**Menus**

Menus are shown in the gray bar near the top of the window.  Some examples of menus are: File, Edit, Reports, and Help — typical menus for most Windows applications.  When you click on one of these, a list of options is displayed.

**Help**

Online help and documentation are available in several formats: hints, context-sensitive help, menu help, and Internet Web documentation.

**Hints**

Place the cursor over a specific button, and a pop-up box will appear containing a short description of that button.

**Context-Sensitive Help**

Use the “F1” key at any time to obtain help on the current screen.

**Menu Help**

Select the Help Menu at the top of the screen.  A Table of Contents opens.  Choose one of the contents, or type in a topic you want help on.  A screen appears containing help about that subject.

**Access Keys**

Use access keys to quickly get to an option through the pull-down menus by holding down the Alt key and pressing the underlined letter of the desired pull-down menu, then (still holding down the Alt key) press the underlined letter of the desired option.

This page intentionally left blank for double-side printing.

## 2 Implementation and Maintenance

### Description

This chapter provides guidelines for implementing the Vitals/Measurements application.  It is important to complete all of the steps contained in this chapter before assigning menu options to clinical staff.

### Virgin Installation of Software

The following steps should be followed when the Vitals/Measurements software is installed in an environment where no previous installation of the Vitals/Measurements application has taken place.

1.  Setting up the software environment.

Information Resource Management Services (IRMS) staff should install the software using the Installation Guide in a test environment prior to installing the software in the production () account.  The following  packages should reside in the environment where the Vitals/Measurements application is to be installed:

a.	VA FileMan V. 22 or greater,

b.	Kernel V. 8.0 or greater,

c.	Kernel Toolkit V. 7.3 or greater,

d.	Kernel RPC Broker V. 1.1 or greater,

e.	PIMS V. 5.3 or greater,

f.	Intake and Output V. 4.0,

g	Health Summary V. 2.7 or greater,

h.	Nursing V. 4.0 or greater.

Data entered into the test environment CANNOT be transferred into the production environment.  It is recommended that a limited amount of data be entered into the test directory in order for the user to become familiar with the application and to establish an acceptable training database.

2.  Name spacing and file listing.

Vitals/Measurements is found in the GMV namespace.  All routines, templates and options begin with GMV.  File numbers are in the range of 120.5 to 120.57 and are stored in the ^GMR and ^GMRD globals.

3.  Editing site configurable files.

Site configurable files can be edited through the Vitals Manager module.

4.  Queuing TaskMan jobs.

No queued TaskMan jobs are associated with this application.

5.  Accessing modules.

The Vitals application, i.e., the Vitals and Vitals Manager modules are accessed separately through the GUI executable icons on the user’s desktop.  The Vitals module is assigned to the clinical staff so they can use the Vitals application, and the Vitals Manager module is assigned to the Clinical Application Coordinator, package coordinator, and Information Resource Management Service (IRMS) staff so they can use the Vitals Manager application to manage the Vitals templates and abnormal values.

6.  Assigning modules.

The Vitals Manager module should be assigned to Clinical Application Coordinator, package coordinator, and Information Resource Management Service (IRMS) staff.

The Vitals module should be assigned to clinical staff.

7.  Security keys.

There is one security key in this application, it is GMV MANAGER.  This new key allows a user to view/create/edit all other user’s templates in the Vitals Manager module, without this key the user can only view/create/edit his/her own user templates.  This key also allows a user to use (run) other user’s templates in the Vitals application.  This key should be assigned to the package coordinator.

8.  Printer issues.

Users may print some reports on Client (Windows) printers and other reports on  (device file) printers.

9.  On-line Help.

Throughout the application, on-line help is available when questions arise.  The user can click on the Help button or menu at the top of the screen to see a table of contents and index containing help on how to enter data, print reports, etc..

### Non-Virgin Installation of Software

Follow steps 1 through 9 above when installing the software in an environment where a previous version of the application has been installed.

### Implementation Considerations

Some sites prefer to delay implementation of the software until they have a point of care data entry system, but this software can be implemented without a point of care system.  Vital sign entry can be accomplished by ancillary service personnel, (e.g., PIMS, Dietetics, Pharmacy).  Interested users of this software are encouraged to form a committee to work cooperatively on the implementation and training of the package.  Setting up test wards is a good way to begin a cooperative implementation effort.  The Vitals/Measurements module is appropriate for all personnel who obtain and record patient vitals/measurements.  Conceivably this module could be used by nursing, dietetics, medicine, and other disciplines as appropriate.

### Resource Requirements

The minimal hardware requirements for the software are two data input devices (usually PC workstations running Windows 9x or NT (Ver. 4 or later)) and one printer per location.  12 megabytes of available memory is needed to run the program.  The following statistics regarding the disk storage requirements of the software were compiled by an average test site.

#### Server Requirements

Globals	Type of Data	Size

DDs	Data Dictionaries	40 k

GMR	Patient data for the	25-75 k/

Text Generator,	patient

Vitals/Measurements,

Intake and Output, Adverse

Reaction Tracking and Consult/

Request Tracking Modules

GMRD	Static data for the	10 k depending

Text Generator,	on the global

Vitals/Measurements	efficiency

and Intake and Output

Modules

#### Client Requirements

The client (disk) storage requirements are approximately:

**Type of Data		Size**

Vitals.exe		1900 k

VitalsManager.exe		1200 k

GMV\_VitalsViewEnter.dll	1500 k

VITALS.HLP		41 k

VITALSMANAGER.HLP	22 k

GMV\_VitalsViewEnter.hlp	23 k

## 3 Routine Descriptions

GMVBMI    ;HIOFO/YH,FT-EXTRACT HEIGHT TO CALCULATE BMI FOR WEIGHT;

;;5.0;GEN. MED. REC. - VITALS;**3,23**;Oct 31, 2002

GMVBP0    ;HIOFO/YH,FT-KYOCERA B/P GRAPH - STORE DATA IN ^TMP($J) ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVBP1    ;HIOFO/YH,FT-CALCULATE KYOCERA B/P GRAPH DATA ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVBP2    ;HIOFO/YH,FT-DEFINE KYOCERA BP GRAPH MACRO ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVBP3    ;HIOFO/YH,FT-DEFINE KYOCERA B/P GRAPH MACRO (CONT.) ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVBP4    ;HIOFO/YH,FT-CALL KYOCERA B/P GRAPH MACRO ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVBP5    ;HIOFO/YH,FT-CALCULATE KYOCERA B/P GRAPH DATA (CONT.) ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVCAQU   ;HOIFO/YH,FT-DISPLAY CATEGORY/QUALIFIER/SYNONYM TABLE FOR VITAL TYPE  ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVCHAR   ;HIOFO/YH,FT-EXTRACT CHARACTERISTIC DATA ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVCLIN   ;HOIFO/YH,FT-RETURNS A LIST OF PATIENTS WITH CLINIC APPOINTMENTS WITHIN A GIVEN PERIOD ;

;;5.0;GEN. MED. REC. - VITALS;**1**;Oct 31, 2002

GMVDCCHK  ;HOIFO/DAD,FT-VITALS COMPONENT: CHECK DATA VALUE ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVDCCNV  ;HOIFO/DAD,FT-VITALS COMPONENT: CONVERT UNITS ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVDCEXT  ;HOIFO/DAD,FT-VITALS COMPONENT: EXTRACT PATIENT DATA ;

;;5.0;GEN. MED. REC. - VITALS;**23**;Oct 31, 2002

GMVDCHLP  ;HOIFO/DAD,FT-VITALS COMPONENT: HELP TEXT ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVDCRPC  ;HOIFO/DAD-VITALS COMPONENT: RPCs ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVDCSAV  ;HOIFO/DAD,FT-VITALS COMPONENT: SAVE DATA ;

;;5.0;GEN. MED. REC. - VITALS;**9,3,23**;Oct 31, 2002

GMVDCUTL  ;HOIFO/DAD,FT-VITALS COMPONENT: UTILITIES ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVDCVAL  ;HOIFO/DAD,FT-VITALS COMPONENT: VALIDATE DATA ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVDCVAM  ;HOIFO/DAD,FT-VITALS COMPONENT: VALIDATE DATA (CONT.) ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVDS0    ;HIOFO/YH,FT-DISPLAY LATEST VITALS/MEASUREMENTS ;

;;5.0;GEN. MED. REC. - VITALS;**23**;Oct 31, 2002

GMVDS1    ;HOIFO/YH,FT-CURRENT VITALS BY PATIENT OR LOCATION ;

;;5.0;GEN. MED. REC. - VITALS;**23**;Oct 31, 2002

GMVDS2    ;HOIFO/RM,YH,FT-VITAL SIGNS DISPLAY ;

;;5.0;GEN. MED. REC. - VITALS;**23**;Oct 31, 2002

GMVER0    ;HOIFO/FT-VITALS ENTERED IN ERROR FOR A PATIENT ;

;;5.0;GEN. MED. REC. - VITALS;**23**;Oct 31, 2002

GMVER1    ;HOIFO/RM,YH,FT-ENTERED IN ERROR FOR A  ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVFSYN   ;HOIFO/RM,YH,FT-X REFERENCE FOR VITAL TYPE, CATEGORY AND SYNONYM ;

;;5.0;GEN. MED. REC. - VITALS;**8**;Oct 31, 2002

GMVFUT0   ;HOIFO/RM,FT-FILE UTILITIES FOR 120.5 FILE ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVFUT2   ;HOIFO/RM,FT-FILE UTILITIES FOR 120.52 FILE ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVFUT3   ;HOIFO/RM,FT-FILE UTILITIES FOR 120.53 FILE ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVGETC   ;HOIFO/FT-GET CATEGORY INFORMATION ;

;;5.0;GEN. MED. REC. - VITALS;**23**;Oct 31, 2002

GMVGETD   ;HOIFO/YH,FT-EXTRACTS WARD/ROOM-BED/PT AND PT VITALS ;

;;5.0;GEN. MED. REC. - VITALS;**3,22,23**;Oct 31, 2002

GMVGETD1  ;HOIFO/YH-EXTRACT VITALS/MEASUREMENT RECORDS FOR A GIVEN DATE ;

;;5.0;GEN. MED. REC. - VITALS;**23**;Oct 31, 2002

GMVGETD2  ;HOIFO/YH-EXTRACT VITALS/MEASUREMENT RECORDS FOR A GIVEN DATE (CONT.) ;

;;5.0;GEN. MED. REC. - VITALS;**1,23**;Oct 31, 2002

GMVGETQ   ;HOIFO/YH,FT-UTILITIES TO OBTAIN DATE/TIME, HOSPITAL, DUZ, VITAL CATEGORY AND EDIT V/M ;

;;5.0;GEN. MED. REC. - VITALS;**3**;Oct 31, 2002

GMVGETQL  ;HOIFO/FT-GET QUALIFIER INFORMATION ;

;;5.0;GEN. MED. REC. - VITALS;**23**;Oct 31, 2002

GMVGETVT  ;HOIFO/FT-GET VITAL TYPE INFORMATION ;

;;5.0;GEN. MED. REC. - VITALS;**23**;Oct 31, 2002

GMVGGR1   ;HOIFO/YH,FT-VITAL SIGNS RECORD SF 511 ;

;;5.0;GEN. MED. REC. - VITALS;**3,23**;Oct 31, 2002

GMVGGR2   ;HOIFO/YH,FT-SET ^TMP($J) GLOBAL ;

;;5.0;GEN. MED. REC. - VITALS;**3,23**;Oct 31, 2002

GMVGR0    ;HIOFO/MH,YH,FT-VITALS GRAPH (PART 1) ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVGR1    ;HIOFO/YH,FT-SET ^TMP($J) GLOBAL ;

;;5.0;GEN. MED. REC. - VITALS;**1**;Oct 31, 2002

GMVGR2    ;HIOFO/YH,FT-VITALS GRAPH KYOCERA DEFINE MACRO (PART 1) ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVGR3    ;HIOFO/YH,FT-VITALS GRAPH KYOCERA DEFINE MACRO (PART 2) ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVGR4    ;HIOFO/YH,FT-VITALS GRAPH KYOCERA PRINT COMMANDS (PART 1) ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVGR5    ;HIOFO/RM,YH,FT-TMP TO EXTRACT DATA FROM IO PACKAGE ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVGR6    ;HIOFO/YH,FT-VITALS GRAPH KYOCERA PRINT COMMANDS (PART 2) ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVGR7    ;HIOFO/YH,FT-VITALS GRAPH KYOCERA DEFINE MACRO FOR PULSE OX./CG/CVP ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVHB0    ;HIOFO/YH,FT-HP LASER B/P GRAPH - DATA ARRAY ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVHB1    ;HIOFO/YH,FT-HP LASER B/P GRAPH - FORM ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVHB2    ;HIOFO/YH,FT-HP LASER B/P GRAPH - BOX DATA ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVHB3    ;HIOFO/YH,FT-HP LASER B/P GRAPH - ID ;

;;5.0;GEN. MED. REC. - VITALS;**1**;Oct 31, 2002

GMVHB4    ;HIOFO/YH,FT-HP LASER B/P GRAPH - ^TMP DATA ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVHDR    ;HIOFO/FT-HEALTH DATA REPOSITORY API ;

;;5.0;GEN. MED. REC. - VITALS;**2,17**;Oct 31, 2002

GMVHG0    ;HIOFO/YH,FT-HP LASER SF 511 GRAPH - DATA ARRAY ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVHG1    ;HIOFO/YH,FT-HP LASER SF511 GRAPH - FORM ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVHG2    ;HIOFO/YH,FT-HP LASER SF 511 GRAPH - BOX DATA ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVHG3    ;HIOFO/YH,FT-HP LASER SF 511 GRAPH - ID ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVHG4    ;HIOFO/YH,FT-HP LASER SF 511 GRAPH - ^TMP DATA ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVHPN0   ;HIOFO/YH,FT-HP LASER PAIN CHART - DATA ARRAY ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVHPN1   ;HIOFO/YH,FT-HP LASER PAIN CHART - FORM ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVHPN2   ;HIOFO/YH,FT-HP LASER PAIN CHART - ^TMP DATA ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVHPO0   ;HIOFO/YH,FT-HP LASER PULSE OXIMETRY/RESP. GRAPH - DATA ARRAY ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVHPO1   ;HIOFO/YH,FT-HP LASER PULSE OXIMETRY/RESP. GRAPH - FORM ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVHPO2   ;HIOFO/YH,FT-HP LASER PULSE OXIMETRY/RESP. GRAPH - BOX DATA ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVHPO3   ;HIOFO/YH,FT-HP LASER PULSE OXIMETRY/RESP. GRAPH - ^TMP DATA ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVHS     ;HIOFO/FT-RETURN PATIENT DATA UTILITY ;

;;5.0;GEN. MED. REC. - VITALS;**3,23**;Oct 31, 2002

GMVHS1    ;HIOFO/FT-RETURN PATIENT DATA UTILITY (cont.) ;

;;5.0;GEN. MED. REC. - VITALS;**3,23**;Oct 31, 2002

GMVHW0    ;HIOFO/YH,FT-HP LASER WEIGHT CHART - DATA ARRAY ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVHW1    ;HIOFO/YH,FT-HP LASER WEIGHT CHART - FORM AND GRAPH ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVHW2    ;HIOFO/YH,FT-HP LASER WEIGHT CHART - BOX DATA ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVKPN0   ;HCIOFO/YH,FT-KYOCERA PAIN CHART - DATA ARRAY ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVKPN1   ;HCIOFO/YH,FT-KYOCERA PAIN CHART MACRO-1 ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVKPN2   ;HCIOFO/YH,FT-KYOCERA KYOCERA PAIN CHART PRINT COMMANDS (PART 1) ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVKPO0   ;HIOFO/YH,FT-KYOCERA PULSE OXIMETRY/RESP. GRAPH - DATA ARRAY ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVKPO1   ;HIOFO/YH,FT-KYOCERA PULSE OXIMETRY/RESP. GRAPH - GRAPH DATA ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVKPO2   ;HIOFO/YH,FT-KYOCERA PULSE OXIMETRY/RESP. MACRO-1 ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVKPO3   ;HIOFO/YH,FT-KYOCERA PULSE OXIMETRY/RESP. GRAPH - MACRO 2 ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVKPO4   ;HIOFO/YH,FT-GRAPH KYOCERA PRINT COMMANDS (PART 1) ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVLAT0   ;HOIFO/YH,FT-DISPLAY LATEST VITALS/MEASUREMENTS FOR A PATIENT ;

;;5.0;GEN. MED. REC. - VITALS;**1,3,23**;Oct 31, 2002

GMVLATS   ;HOIFO/YH,FT-QUEUES LATEST VITALS/MEASUREMENTS ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVLBP0   ;HIOFO/YH,FT-PATIENT BLOOD PRESSURE LINE PRINTER GRAPH - 1 ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVLBP1   ;HIOFO/YH,FT-SYSTOLIC/DIASTOLIC GRAPH ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVLBP2   ;HIOFO/YH,FT-SET GRAPH LOWER BOX DATA ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVLGQU   ;HIOFO/YH,FT-UTILITY FOR LEGEND, PO2 AND QUALIFIER ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVLPO0   ;HIOFO/YH,FT-DOT MATRIX OXIMETRY/RESP. GRAPH - DATA ARRAY ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVLPO1   ;HIOFO/YH,FT-DOT MATRIX PULSE OXIMETRY AND RESPIRATION GRAPH ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVLPO2   ;HIOFO/YH,FT-DOT MATRIX HIOFO/YH-PULSE OX. AND RESPIRATION DATA ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVLWT0   ;HIOFO/YH,FT-DOT MATRIX WEIGHT GRAPH - DATA ARRAY ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVLWT1   ;HIOFO/YH,FT-DOT MATRIX PATIENT WEIGHT GRAPH - 2 ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVLWT2   ;HIOFO/YH,FT-DOT MATRIX WEIGHT GRAPH - 3 ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVLWT3   ;HIOFO/YH,FT-DOT MATRIX PATIENT WEIGHT GRAPH - 4 ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVPAR    ; HOIFO/DP - XPARameter RPC ;

;;5.0;GEN. MED. REC. - VITALS;**3**;Oct 31, 2002

GMVPCE3   ;HIOFO/RM,FT-V/M Data Validation for AICS ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVPXRM   ;HIOFO/FT-API to return FILE 120.5 data ;

;;5.0;GEN. MED. REC. - VITALS;**6,23**;Oct 31, 2002

GMVQUAL   ;HOIFO/YH,FT-VITAL QUALIFIERS ;

;;5.0;GEN. MED. REC. - VITALS;**8**;Oct 31, 2002

GMVRPCHL  ;HIOFO/FT-RPC FOR HOSPITAL LOCATION SELECTION ;

;;5.0;GEN. MED. REC. - VITALS;**3,22**;Oct 31, 2002

GMVRPCM   ; HOIFO/DP - RPC for Vitals Manager ;

;;5.0;GEN. MED. REC. - VITALS;**1,8,13,3**;Oct 31, 2002

GMVRPCP   ;HOIFO/DP-RPC for GMV\_PtSelect.pas ;

;;5.0;GEN. MED. REC. - VITALS;**1,3,22**;Oct 31, 2002

GMVRPCU   ; HOIFO/DP - RPC for Vitals User ;

;;5.0;GEN. MED. REC. - VITALS;**3**;Oct 31, 2002

GMVSAS0   ;HIOFO/RM,YH,FT-CALCULATE ABNORMAL V/S ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVSC0    ;HOIFO/MD,YH,FT-CUMULATIVE VITALS/MEASUREMENTS FOR PATIENT OVER GIVEN  ;

;;5.0;GEN. MED. REC. - VITALS;**23**;Oct 31, 2002

GMVSC1    ;HOIFO/YH,FT-CUMULATIVE V/M - CONTINUED ;

;;5.0;GEN. MED. REC. - VITALS;**23**;Oct 31, 2002

GMVSC2    ;HIRMFO/YH,FT-CUMULATIVE V/M - CONTINUED ;

;;5.0;GEN. MED. REC. - VITALS;**23**;Oct 31, 2002

GMVSR0    ;HOIFO/RM,YH,FT-VITAL SIGNS RECORD SF 511 ;

;;5.0;GEN. MED. REC. - VITALS;**23**;Oct 31, 2002

GMVSR1    ;HIOFO/RM,YH-PATIENT VITAL SIGNS-I/O SF 511 GRAPH - 1 ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVSR2    ;HIOFO/YH,FT-PATIENT VITAL SIGNS-I/O SF 511 GRAPH - 2 ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVUID    ;HIOFO/FT-VUID-RELATED UTILITIES ;

;;5.0;GEN. MED. REC. - VITALS;**8**;Oct 31, 2002

GMVUT0    ;HIOFO/RM,YH,FT-INPUT TRANSFORMS FOR VITAL TYPES ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVUT2    ;HOIFO/YH,RM,FT-ENTRY TO GATHER PATIENT VITAL/MEASURMENT DATA ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVUT3    ;HIOFO/YH,FT-VITAL MEASUREMENT SITE/QUALIFIER SELECTION ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVUTL    ;HOIFO/RM,MD,FT-CALLABLE ENTRY POINTS FOR PROGRAMMER UTILITIES ;

;;5.0;GEN. MED. REC. - VITALS;**23**;Oct 31, 2002

GMVUTL1   ;HOIFO/YH,FT-EXTRACT CLINIC LIST AND MARK VITALS ENTERED IN ERROR ;

;;5.0;GEN. MED. REC. - VITALS;**1,3**;Oct 31, 2002

GMVUTL2   ;HOIFO/YH,FT-BP HIGH/LOW LIMITS AND DEFAULT QUALIFIER;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVUTL3   ;HOIFO/YH,FT-RPCBROKER UTILITY ROUTINE TO EXTRACT NURSING UNIT/ROOM-BED - 3 ;

;;5.0;GEN. MED. REC. - VITALS;**3**;Oct 31, 2002

GMVUTL7   ;HIOFO/DS,FT-RPC API TO RETURN ALL VITALS/CATEGORIES/QUALIFIERS ;

;;5.0;GEN. MED. REC. - VITALS;**3**;Oct 31, 2002

GMVUTL8   ;HIOFO/DS,FT-RPC API TO RETURN ALL VITALS/CATEGORIES/QUALIFIERS ;

;;5.0;GEN. MED. REC. - VITALS;**1,3**;Oct 31, 2002

GMVVDEF1  ;BPOIFO/JG,HIOFO/FT - BUILD HL7 ORU^R01 MESSAGE FOR VITALS ;

;;5.0;GEN. MED. REC. - VITALS;**5,8,12,17,11**;Oct 31, 2002

GMVVDEFK  ;BPOIFO/JG,HIOFO/FT - KIDS POST INSTALL FOR VDEF PATCH ;

;;5.0;GEN. MED. REC. - VITALS;**5**;Oct 31, 2002

GMVVS1    ;HIOFO/YH,FT-PATIENT VITAL SIGNS-I/O SF 511 GRAPH - 1 ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVVS2    ;HIOFO/YH,FT-PATIENT VITAL SIGNS-I/O SF 511 GRAPH - 2 ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVVS3    ;HIOFO/YH,FT-PATIENT VITAL SIGNS-I/O SF 511 GRAPH - 3 ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVVS4    ;HIOFO/YH,FT-PATIENT VITAL SIGNS-GRAPH ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVWT0    ;HIOFO/YH,FT-KYOCERA WEIGHT GRAPH - DATA ARRAY ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVWT1    ;HIOFO/YH,FT-KYOCERA WEIGHT GRAPH - GRAPH DATA ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVWT2    ;HIOFO/YH,FT-KYOCERA WEIGHT GRAPH - MACRO ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVWT3    ;HIOFO/YH,FT-KYOCERA WEIGHT GRAPH - MACRO (CONT.) ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

GMVWT4    ;HIOFO/YH,FT-KYOCERA WEIGHT GRAPH - MACRO CALL ;

;;5.0;GEN. MED. REC. - VITALS;;Oct 31, 2002

## 4 File List and Related Information

### File Descriptions

GMRV VITAL MEASUREMENT     120.5

This file contains vital sign information and other measurement data for a patient.

GMRV VITAL TYPE     120.51

This file contains a list of vital sign types, and various parameters which mold the data entry.

GMRV VITAL QUALIFIER     120.52

This file contains a list of qualifiers for vitals/measurements.

GMRV VITAL CATEGORY     120.53

This file contains a list of qualities or characteristics that can be affixed to a vital measurement.

GMRV VITALS PARAMETERS     120.57

This file contains the various site configurable parameters for the Vitals/Measurements application.

### Package Default Definition

UP    SEND  DATA                USER

DATE  SEC.  COMES  SITE   RSLV  OVER

FILE #      NAME                         DD    CODE  W/FILE DATA   PTS   RIDE

-------------------------------------------------------------------------------

120.5       GMRV VITAL MEASUREMENT       YES   YES   NO

120.51      GMRV VITAL TYPE              YES   YES   YES    ADD    NO    NO

120.52      GMRV VITAL QUALIFIER         YES   YES   YES    ADD    NO    YES

120.53      GMRV VITAL CATEGORY          YES   YES   YES    ADD    NO    NO

120.57      GMRV VITALS PARAMETERS       YES   YES   YES    ADD    NO    YES

This page intentionally left blank for double-side printing.

## 5 Exported Options

### Components

Vitals/Measurements uses RPC Broker and VA FileMan Delphi Components in the display and navigation of screens.  Vitals utilizes only the standard components as supplied with .

Below is a list of the  components this application currently uses along with a short description.

TeeChart	Displays charts and graphs.  It is used in Vitals/Measurements to graphically plot various measurements versus time.

ResizerPanel	Resizes its client components when the form is resized or the screen resolution is changed.  This takes care of proper size and position of components with regard to the font size used in Windows.  It is there so users can resize the application Windows to meet their needs.

VersionInfoResource	Retrieves VERSIONINFO data from the executable.  It is used in the about boxes in Vitals/Measurements to display version information.

RPCBroker	Used for all non-FTP communication with the server.

FMDC	Used for saving, deleting, validating, and retrieving data in FileMan data dictionaries.

DateTime	Allows the user to visually select a date and time.  It is provided as an option on all date/time fields.

PatientSelectionFrame	Allows user to select a patient, by unit, team, ward, clinic or name. The frame is on a resize panel.

ReportFrame	Allows users to view patients vitals data and create a configurable graph of data.

### Remote Procedure Calls (RPC)

NAME: **GMV ADD VM** TAG: EN1

ROUTINE: GMVDCSAV                     RETURN VALUE TYPE: SINGLE VALUE

AVAILABILITY: SUBSCRIPTION            INACTIVE: ACTIVE

WORD WRAP ON: TRUE

DESCRIPTION:

This remote procedure call is used to enter a new Vital/Measurement record

in the GMRV Vital Measurement file (#120.5).

This remote procedure call is documented in Integration Agreement 3996.

INPUT PARAMETER: GMRVDATA               PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 255              REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

This variable contains the data needed to create a Vital/Measurement

record in the GMRV Vital Measurement (#120.5) file. The values are parsed

out of the GMRVDATA variable and filed.

GMRVDATA has the following data:

piece1^piece2^piece3^piece4^piece5

where:

piece1 = date/time in FileMan internal format

piece2 = patient number from FILE 2 (i.e., DFN)

piece3 = vital type, a semi-colon, the reading, a semi-colon, and

oxygen flow rate and percentage values [optional] (e.g.,

21;99;1 l/min 90%)

piece4 = hospital location (FILE 44) pointer value

piece5 = user number from FILE 200 (i.e., DUZ), an asterisk, and the

qualifier (File 120.52) internal entry numbers separated by

colons (e.g., 547*50:65)

RETURN PARAMETER DESCRIPTION:

RESULT does not return a value.

The data is filed in the GMRV VITAL MEASUREMENT (#120.5) file.

Example:

&gt; S GMRVDATA="3051011.1635^134^1;120/80;^67^87*2:38:50:75"

&gt; D EN1^GMVDCSAV(.RESULT,GMRVDATA)

NAME: **GMV ALLERGY** TAG: ALLERGY

ROUTINE: GMVUTL3                      RETURN VALUE TYPE: ARRAY

AVAILABILITY: SUBSCRIPTION            INACTIVE: ACTIVE

WORD WRAP ON: TRUE

DESCRIPTION:

This remote procedure call retrieves the patient's allergy information.

This remote procedure call is documented in Integration Agreement 4350.

INPUT PARAMETER: DFN                    PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 30               REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

DFN is a pointer to the PATIENT file (#2).

RETURN PARAMETER DESCRIPTION:

Returns the patient allergy information in the array specified.

The result array returns:

RESULT(n)=This patient has the following allergy(ies):

(n+1)=piece1

where piece1 = the allergy name

n = sequential number starting at 1.

If there is no data, then the following is returned:

RESULT(1)=No Allergy Assessment

Example:

&gt; S DFN=134

&gt; D ALLERGY^GMVUTL3(.RESULT,DFN) ZW RESULT

&gt; RESULT(1)="This patient has the following allergy(ies): "

&gt; RESULT(2)="PENICILLIN"

NAME: **GMV CHECK DEVICE** TAG: CHKDEV

ROUTINE: GMVUTL2                      RETURN VALUE TYPE: ARRAY

AVAILABILITY: RESTRICTED              INACTIVE: ACTIVE

WORD WRAP ON: TRUE

DESCRIPTION:

This RPC calls a KERNEL utility to return a list of printers the user may

select to print output. Returns a maximum of twenty entries.

INPUT PARAMETER: GMVIEN                 PARAMETER TYPE: LITERAL

REQUIRED: YES                         SEQUENCE NUMBER: 1

DESCRIPTION:

The value to begin the search in the Device file (#3.5). Can be null.

INPUT PARAMETER: GMVDIR                 PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 1                REQUIRED: YES

SEQUENCE NUMBER: 2

DESCRIPTION:

Direction of the search (1 = forward, -1 = backwards).

If DIR is null, then set to 1.

INPUT PARAMETER: GMVRMAR                PARAMETER TYPE: LITERAL

REQUIRED: YES                         SEQUENCE NUMBER: 3

DESCRIPTION:

Right margin as a single number or range (e.g, 80, 132 or "80-132").

RETURN PARAMETER DESCRIPTION:

RESULT(n)=P1^P2^P3^P4^P5^P6

where n = a sequential number starting with 1

P1 = File 3.5  IEN

P2 = File 3.5 name (.01 value)

P3 = File 3.5 name (.01 value) or flag to indicate last entry in

the array

P4 = location of terminal

P5 = right margin

P6 = page length

NAME: **GMV CLINIC PT** TAG: CLINPTS

ROUTINE: GMVCLIN                      RETURN VALUE TYPE: ARRAY

AVAILABILITY: RESTRICTED              INACTIVE: ACTIVE

WORD WRAP ON: TRUE

DESCRIPTION:

This procedure lists patients who have an appointment for a selected

clinic and a given period of time.

INPUT PARAMETER: CLIN                   PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 30               REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

CLIN contains the name of the selected clinic from the Hospital Location

file (#44).

INPUT PARAMETER: BDATE                  PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 30               REQUIRED: YES

SEQUENCE NUMBER: 2

DESCRIPTION:

BDATE contains TODAY, TOMORROW, YESTERDAY, PAST WEEK or PAST MONTH.

RETURN PARAMETER DESCRIPTION:

Returns a list of patient names and DFNs for the selected clinic and the

given date span in the array specified.

NAME: **GMV CLOSEST READING** TAG: CLOSEST

ROUTINE: GMVGETD                      RETURN VALUE TYPE: SINGLE VALUE

AVAILABILITY: RESTRICTED              INACTIVE: ACTIVE

DESCRIPTION:

This remote procedure call returns the observation date/time and reading

of the record closest to the date/time specified for the patient and vital

type.

INPUT PARAMETER: GMVDFN                 PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 12               REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

A pointer to the Patient (#2) file (i.e., DFN).

INPUT PARAMETER: GMVDT                  PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 14               REQUIRED: NO

SEQUENCE NUMBER: 2

DESCRIPTION:

The date/time to search from. The default is NOW.

INPUT PARAMETER: GMVT                   PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 5                REQUIRED: YES

SEQUENCE NUMBER: 3

DESCRIPTION:

The vital type abbreviation as it appears in FILE 120.51, Field 1 (e.g.,

WT).

INPUT PARAMETER: GMVFLAG                PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 1                REQUIRED: NO

SEQUENCE NUMBER: 4

DESCRIPTION:

A flag to indicate if the search should look before or after the date/time

specified in the GMVDT value where 1 indicates before, 2 indicates after

and 0 indicates either direction.

RETURN PARAMETER DESCRIPTION:

Returns a string composed of two pieces. The first piece contains the

observation date/time (FILE 120.5, Field .01) of the record that was

found. The second piece contains the rate (FILE 120.5, Field 1.2) of the

record. If there is an error, the first piece will be -1 and the second

piece will be the error text.

Example:

&gt; S GMVDFN=134,GMVDT=3090225.08,GMVT="WT",GMVFLAG=0

&gt; D CLOSEST(.TEST,GMVDFN,GMVDT,GMVT,GMVFLAG) ZW TEST

&gt; TEST="3081106.142926^135"

NAME: **GMV CONVERT DATE** TAG: GETDT

ROUTINE: GMVGETQ                      RETURN VALUE TYPE: SINGLE VALUE

AVAILABILITY: SUBSCRIPTION            INACTIVE: ACTIVE

WORD WRAP ON: TRUE

DESCRIPTION:

This remote procedure call converts a user-supplied date/time into VA

FileMan's internal and external date format.

This remote procedure call is documented in Integration Agreement 4353.

INPUT PARAMETER: GMRDATE                PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 30               REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

GMRDATE is the user-supplied date/time text.

RETURN PARAMETER DESCRIPTION:

RESULT=Date in internal FileMan format^Date in external FileMan format

Example:

&gt; S GMRDATE="10/11/2005@10:30AM"

&gt; D GETDT^GMVGETQ(.RESULT,GMRDATE) ZW RESULT

&gt; RESULT="3051011.103^OCT 11, 2005@10:30:00"

NAME: **GMV CUMULATIVE REPORT** TAG: EN1

ROUTINE: GMVSC0                       RETURN VALUE TYPE: SINGLE VALUE

AVAILABILITY: RESTRICTED              INACTIVE: ACTIVE

DESCRIPTION:

Prints the Cumulative Vitals Report.

INPUT PARAMETER: GMVDATA                PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 150              REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

A multi-piece variable that identifies the values needed to run the

report.

Piece  1: DFN

2: Start date/time of the report range (FileMan format)

3: End date/time of the report range (FileMan format)

4: n/a

5: Device name (File 3.5, Field .01)

6: Device internal entry number

7: date/time to print the report (FileMan format)

8: ward internal entry number (File 42)

9: hospital location internal entry number (File 44)

10: list of rooms separated by a comma (e.g., 200,210,220)

RETURN PARAMETER DESCRIPTION:

Returns a message stating the outcome of the request to queue the report.

If the report was successfully queued, RESULT will be "Report sent to

device. Task #: " ZTSK" where ZTSK is the task number of the job. If the

report could not be queued, RESULT will be "Unable to task the report."

NAME: **GMV DLL VERSION** TAG: DLL

ROUTINE: GMVUTL8                      RETURN VALUE TYPE: SINGLE VALUE

AVAILABILITY: SUBSCRIPTION            INACTIVE: ACTIVE

DESCRIPTION:

Returns a YES or NO response to indicate if the Dynamic Link Library (DLL)

file should be used.

This remote procedure call is documented in Integration Agreement 4420.

INPUT PARAMETER: GMVX                   PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 50               REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

This value is the name of the file and the date/time associated with it

(e.g., GMV\_VITALSVIEWENTER.DLL:v. 07/21/05 10:34).

RETURN PARAMETER DESCRIPTION:

Returns YES if the file can be used. Returns NO, if the file cannot be

used. Returns null if the file was not found.

Example:

&gt; S GMVX="GMV\_VITALSVIEWENTER.DLL:v. 07/21/05 10:34"

&gt; D DLL^GMVUTL8(.RESULT,GMVX) ZW RESULT

&gt; RESULT="NO"

NAME: **GMV ENTERED IN ERROR-PATIENT** TAG: EN1

ROUTINE: GMVER0                       RETURN VALUE TYPE: SINGLE VALUE

AVAILABILITY: RESTRICTED              INACTIVE: ACTIVE

DESCRIPTION:

Prints a report of all vitals/measurements entered in error for the

selected patient for a given date/time range.

INPUT PARAMETER: GMVDATA                PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 150              REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

A multi-piece variable that identifies the values needed to run the

report.

Piece  1: DFN

2: Start date/time of the report range (FileMan format)

3: End date/time of the report range (FileMan format)

4: n/a

5: Device name (File 3.5, Field .01)

6: Device internal entry number

7: date/time to print the report (FileMan format)

8: n/a

9: n/a

10: n/a

RETURN PARAMETER DESCRIPTION:

Returns a message stating the outcome of the request to queue the report.

If the report was successfully queued, RESULT will be "Report sent to

device. Task #: " ZTSK" where ZTSK is the task number of the job. If the

report could not be queued, RESULT will be "Unable to task the report."

NAME: **GMV EXTRACT REC** TAG: GETVM

ROUTINE: GMVGETD                      RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: SUBSCRIPTION            INACTIVE: ACTIVE

WORD WRAP ON: TRUE

DESCRIPTION:

This remote procedure call retrieves vital records from the GMRV Vital

Measurement (#120.5) file for a selected patient within a given date span.

This remote procedure call is documented in Integration Agreement 4416.

INPUT PARAMETER: GMRVDATA               PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 30               REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

GMRVDATA consists of 4 pieces of information:

piece1^piece2^piece3^piece4

where piece1 = Patient (#2) file pointer (i.e., DFN)

piece2 = End date of search (FileMan internal format)

piece3 = single vital type abbreviation (File 120.51, Field 1)

[optional] If not defined, the default is

"T;P;R;BP;HT;WT;PN;PO2;CG;CVP"

piece4 = Start date of search (FileMan internal format)

RETURN PARAMETER DESCRIPTION:

Returns the name of the global array (i.e., ^TMP($J,"GRPC")) containing a

list of vital records for the selected patient within the defined date

range.

The TMP global contains:

^TMP($J,"GRPC",n)=piece1^piece2

where piece1 = File 120.5 IEN

piece2 = a string of text in the following format:

Date/time taken (external)   Vital Type Abbreviation:

Rate  units (Metric value) (Qualifiers)

n = sequential number starting at 1.

Example:

&gt; S GMRVDATA="134^3051028^BP^3051001"

&gt; D GETVM^GMVGETD(.RESULT,GMRVDATA) ZW RESULT

&gt; RESULT="^TMP(538999278,"GRPC")"

&gt; D ^%G

&gt; Global ^TMP($J,"GRPC"

&gt; ^TMP(538999278,"GRPC",1)=8858^10/11/05@16:35   B/P:   120/80*  (L ARM,

SITTING, CAROTID, CALF) \_VITPROVIDER,ONE

&gt;                       2)=8961^10/20/05@14:47   B/P:   128/81*  (L ARM,

SITTING, PALPATED) \_VITPROVIDER,TWO

If there is no data, then the following is returned:

^TMP($J,"GRPC",1)=0^NO VITALS/MEASUREMENTS ENTERED WITHIN THIS PERIOD

NAME: **GMV GET CATEGORY IEN** TAG: CATEGORY

ROUTINE: GMVUTL8                      RETURN VALUE TYPE: SINGLE VALUE

AVAILABILITY: SUBSCRIPTION            INACTIVE: ACTIVE

DESCRIPTION:

Returns the IEN if the value is found in the GMRV VITAL CATEGORY (#120.53)

file.

This remote procedure call is documented in Integration Agreement 4354.

INPUT PARAMETER: GMVCAT                 PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 45               REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

GMVCAT = Name of Category (from FILE 120.53) (e.g., METHOD)

RETURN PARAMETER DESCRIPTION:

Returns the IEN if GMVCAT exists in FILE 120.53

Example:

&gt; S GMVCAT="METHOD"

&gt; D CATEGORY^GMVUTL8(.RESULT,GMVCAT) ZW RESULT

&gt; RESULT=2

NAME: **GMV GET CURRENT TIME** TAG: TIME

ROUTINE: GMVUTL7                      RETURN VALUE TYPE: SINGLE VALUE

AVAILABILITY: SUBSCRIPTION            INACTIVE: ACTIVE

WORD WRAP ON: FALSE

DESCRIPTION:

Gets the current date and time from the server.

This remote procedure call is documented in Integration Agreement 4355.

RETURN PARAMETER DESCRIPTION:

Returns current date and time in FileMan internal and external format.

Example:

&gt; D TIME^GMVUTL7(.RESULT) ZW RESULT

&gt; RESULT=3051011.143332

Note: There is an input parameter, P2, listed in the TIME line tag of the

GMVUTL7 routine. However, it is not used. It can be set to any value or

omitted. It remains for backwards compatibility.

NAME: **GMV GET VITAL TYPE IEN** TAG: TYPE

ROUTINE: GMVUTL8                      RETURN VALUE TYPE: SINGLE VALUE

AVAILABILITY: SUBSCRIPTION            INACTIVE: ACTIVE

DESCRIPTION:

Returns the IEN if the value is found in the GMRV VITAL TYPE (#120.51)

file.

This remote procedure call is documented in Integration Agreement 4357.

INPUT PARAMETER: GMVTYPE                PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 55               REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

GMVTYPE = Name of Vital Type (from FILE 120.51) (e.g., WEIGHT)

RETURN PARAMETER DESCRIPTION:

Returns the IEN if GMVTYPE exists in FILE 120.51.

Example:

&gt; S GMVTYPE="WEIGHT"

&gt; D TYPE^GMVUTL8(.RESULT,GMVTYPE) ZW RESULT

&gt; RESULT=9

NAME: **GMV LATEST VITALS BY LOCATION** TAG: EN1

ROUTINE: GMVDS1                       RETURN VALUE TYPE: SINGLE VALUE

AVAILABILITY: RESTRICTED              INACTIVE: ACTIVE

DESCRIPTION:

Prints the latest vitals/measurements for all patients on a given ward

location.

INPUT PARAMETER: GMVDATA                PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 150              REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

A multi-piece variable that identifies the values needed to run the

report.

Piece  1: n/a

2: n/a

3: n/a

4: n/a

5: Device name (File 3.5, Field .01)

6: Device internal entry number

7: date/time to print the report (FileMan format)

8: ward internal entry number (File 42)

9: hospital location internal entry number (File 44)

10: n/a

RETURN PARAMETER DESCRIPTION:

Returns a message stating the outcome of the request to queue the report.

If the report was successfully queued, RESULT will be "Report sent to

device. Task #: " ZTSK" where ZTSK is the task number of the job. If the

report could not be queued, RESULT will be "Unable to task the report."

NAME: **GMV LATEST VITALS FOR PATIENT** TAG: EN1

ROUTINE: GMVDS1                       RETURN VALUE TYPE: SINGLE VALUE

AVAILABILITY: RESTRICTED              INACTIVE: ACTIVE

DESCRIPTION:

Prints the latest vitals/measurements for the selected patient.

INPUT PARAMETER: GMVDATA                PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 150              REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

A multi-piece variable that identifies the values needed to run the

report.

Piece  1: DFN

2: n/a

3: n/a

4: n/a

5: Device name (File 3.5, Field .01)

6: Device internal entry number

7: date/time to print the report (FileMan format)

8: n/a

9: n/a

10: n/a

RETURN PARAMETER DESCRIPTION:

Returns a message stating the outcome of the request to queue the report.

If the report was successfully queued, RESULT will be "Report sent to

device. Task #: " ZTSK" where ZTSK is the task number of the job. If the

report could not be queued, RESULT will be "Unable to task the report."

NAME: **GMV LATEST VM** TAG: GETLAT

ROUTINE: GMVGETD                      RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: SUBSCRIPTION            INACTIVE: ACTIVE

WORD WRAP ON: TRUE

DESCRIPTION:

This remote procedure call retrieves the latest vital records for a given

patient.

This remote procedure call is documented in Integration Agreement 4358.

INPUT PARAMETER: GMRDFN                 PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 10               REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

GMRDFN variable is a pointer to the Patient (#2) file (i.e., DFN).

RETURN PARAMETER DESCRIPTION:

Returns the name of the global array (i.e., ^TMP($J,"GRPC")) containing

the latest vitals for the selected patient.

The TMP global contains:

^TMP($J,"GRPC",n)=piece1

where piece1 = is a formatted line of text.

n = sequential number starting at 1.

The formatted line of text includes the vital type, value and unit

(), value and unit (metric), qualifiers, supplemental oxygen, body

mass index value, person who entered the record and the database where

the record is stored.

If there is no data for the patient, the following is returned:

^TMP($J,"GRPC",1)=There are no results to report

Example:

&gt; S GMRDFN=134

&gt; D GETLAT^GMVGETD(.RESULT,GMRDFN) ZW RESULT

&gt; RESULT="^TMP(539349605,"GRPC")"

&gt; D ^%G

&gt; Global ^TMP($J,"GRPC"

&gt; ^TMP(539349605,"GRPC",1)=Temp.: (08/09/05@08:00)  102 F  (38.9 C)*

(ORAL) \_VITPROVIDER,ONE\_Vitals

&gt;                       2)=Pulse:       (07/14/05@16:33)  55

(LEFT,CAROTID,PALPATED,LYING)  \_VITPROVIDER,ONE\_Vitals

Enter RETURN to continue or '^' to exit:

&gt;                       3)=Resp.:       (07/14/05@16:33)  31

(SPONTANEOUS,SITTING) \_VITPROVIDER,ONE\_Vitals

&gt;                       4)=Pulse Ox:    (08/22/05@13:48)  99% with

supplemental O2 1 L/min 90% NASAL CANNULA  \_VITPROVIDER,ONE\_Vitals

&gt;                       5)=B/P:         (09/26/05@11:30)  120/80* (L

ARM,SITTING,CAROTID,CALF)  \_VITPROVIDER,TWO\_Vitals

&gt;                       6)=Ht.: (09/14/05@17:18)  5 ft 6 in (167.64

cm) (ACTUAL)  \_VITPROVIDER,ONE\_Vitals

&gt;                       7)=Wt.: (09/14/05@17:18)  135 lb  (61.36 kg)

(ACTUAL,STANDING)  \_VITPROVIDER,ONE\_Vitals

&gt;                       8)=Body Mass Index:             22

9)=CVP:         (08/22/05@17:09)  15 cmH2O (11.0

mmHg)  \_VITPROVIDER,ONE\_Vitals

10)=Circ/Girth:  (07/22/05@10:22)  1 in (2.54 cm)

(DRY,ABDO MINAL)  \_VITPROVIDER,TWO\_Vitals

11)=Pain: (09/15/05@16:43)  5

\_VITPROVIDER,ONE\_Vitals

NAME: **GMV LOCATION SELECT** TAG: RPC

ROUTINE: GMVRPCHL                     RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: SUBSCRIPTION            INACTIVE: ACTIVE

WORD WRAP ON: TRUE

DESCRIPTION:

Select a hospital location by name, from a patient appointment or from a

patient admission. Can also generate a list of active clinics.

This remote procedure is documented in Integration Agreement 4461.

INPUT PARAMETER: OPTION                 PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 10               REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

Routine tag line in GMVRPCHL to call.

INPUT PARAMETER: DATA                   PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 100              REQUIRED: YES

SEQUENCE NUMBER: 2

DESCRIPTION:

Other data as required for the call.

RETURN PARAMETER DESCRIPTION:

This remote procedure call allows the user to select a hospital location.

The entry point is RPC^GMVRPCHL. It has input parameters of RESULTS,

OPTION and DATA (ex. RPC^GMVRPCHL(.RESULTS,OPTION,DATA).

The RESULTS variable will contain the ^TMP("GMVHLOC",$J) global array

reference. The ^TMP("GMVHLOC",$J) global array contains the results.

The OPTION variable identifies a line label in the GMVRPCHL routine that

will be invoked to process the call.

The DATA variable contains any additional values needed by the OPTION

variable to process the call.

1) When the OPTION value is NAME, this RPC will do a file lookup.

The DATA value is a three part value separated by carets(^). The first

part is a file number. The second part is a value to look up. The third

part is the field or fields to do the look up on. If the third piece is

not defined, the lookup is done on the .01 field of the file.

The TMP global contains:

^TMP("GMVHLOC",$J,0)=piece1

^TMP("GMVHLOC",$J,n)=piece2^piece3

where piece1 = number of entries found

piece2 = file number, a semi-colon and record IEN

piece3 = field value

Example:

&gt;S OPTION="NAME",DATA="44^OUTPATIENT^.01"

&gt;D RPC^GMVRPCHL(.RESULT,OPTION,DATA) ZW RESULT

&gt;RESULT="^TMP("GMVHLOC",539052767)"

&gt;D ^%G

&gt;Global ^TMP("GMVHLOC",$J

&gt;^TMP("GMVHLOC",539052767,0)=3

1)=44;75^OUTPATIENT NUC MED

2)=44;74^OUTPATIENT RADIOLOGY

3)=44;80^OUTPATIENT ULTRASOUND

2) When the OPTION value is APPT, this RPC will return a list of clinic

appointments for the patient.

The DATA value is a four part value separated by carets(^). The first

piece is DFN. The second piece is the start date of the search. If

not defined, this value defaults to 365 days prior to today. The third

piece is the end date of the search. If not defined, the value defaults

to today. Both dates are in FileMan internal format. The fourth piece is

a string of numbers to indicate what types of appointments to return. If

not defined, the value defaults to "123456789" (i.e., all appointment

types) where:

1 - Active/Kept

2 - Inpatient appts. only

3 - No-shows

4 - No-shows, auto-rebook

5 - Cancelled by clinic

6 - Cancelled by clinic, auto rebook

7 - Cancelled by patient

8 - Cancelled by patient, auto rebook

9 - No action taken

The TMP global contains:

^TMP("GMVHLOC",$J,0)=piece1

^TMP("GMVHLOC",$J,n)=piece2^piece3^piece4^piece5^piece6^piece7

^piece8^piece9^

where piece1 = number of entries found

piece2 = date/time of appt (FM internal)

piece3 = date/time of appt (external)

piece4 = hospital location IEN (FILE 44)

piece5 = hospital location name (FILE 44, Field .01)

piece6 = appt status (internal)

piece7 = appt status (external)

piece8 = appt type (internal)

piece9 = appt type (external)

Example:

&gt; S OPTION="APPT",DATA="78^3051201^3051206^"

&gt; D RPC^GMVRPCHL(.RESULT,OPTION,DATA) ZW RESULT

&gt; RESULT="^TMP("GMVHLOC",539052767)"

&gt; D ^%G

&gt; Global ^TMP("GMVHLOC",$J

&gt; ^TMP("GMVHLOC",539052767,0)=1

1)=3051206.1^DEC 6,2005@10:00^88^WEIGHT

CLINIC^^^9^REGULAR

3) When the OPTION value is ADMIT, this RPC will return a list of

hospital admissions for the patient specified.

The DATA value is the patient's DFN.

The TMP global contains:

^TMP("GMVHLOC",$J,0)=piece1

^TMP("GMVHLOC",$J,n)=piece2^piece3^piece4^piece5^piece6

where piece1 = number of entries found

piece2 = date/time of admission (external)

piece3 = hospital location IEN (FILE 44)

piece4 = hospital location name (FILE 44, Field .01)

piece5 = type of movement (FILE 405.1, Field .01)

piece6 = movement IEN (FILE 405)

Example:

&gt; S OPTION="ADMIT",DATA=134

&gt; D RPC^GMVRPCHL(.RESULT,OPTION,DATA) ZW RESULT

&gt; RESULT="^TMP("GMVHLOC",539052767)"

&gt; D ^%G

&gt; Global ^TMP("GMVHLOC",$J

&gt; ^TMP("GMVHLOC",539052767,0)=1

1)=Apr 09, 2001 1:48:43 pm^67^

2-ASM^DIRECT^1712

4) When the OPTION value is CLINIC, this RPC will return a list of

active clinics.

The DATA value is FROM^MAXIMUM^DIRECTION.

Where:

FROM = Value to begin the search (optional). Default is

null (i.e., start with the first entry in the B x-ref).

MAXIMUM = Maximum number of entries to return. (optional)

Default is 100.

DIRECTION = Direction of search (optional). 1 means forward and -1

means backwards. Default is 1.

The TMP global contains:

^TMP("GMVHLOC",$J,0)=piece1

^TMP("GMVHLOC",$J,n)=piece2^piece3

where piece1 = number of entries found

piece2 = 44;ien (44, a semi-colon and the entry number)

piece3 = location name (FILE 44, Field .01)

n is a sequential number starting with zero

Example:

&gt; S OPTION="CLINIC",DATA="A^5^1"

&gt; K RESULTS D RPC^GMVRPCHL(.RESULTS,OPTION,DATA) ZW RESULTS

&gt; RESULTS="^TMP("GMVHLOC",540221719)"

&gt; D ^%G

&gt; Global ^TMP("GMVHLOC",$J

&gt; ^TMP("GMVHLOC",540221719,0)=5

1)=44;140^ANDY'S AUDIO NON-COUNT CLINIC

2)=44;139^ANDY'S AUDIOLOGY COUNT CLINIC

3)=44;76^AUDIOLOGY AND SPEECH PATHOLOGY

4)=44;87^BARB'S CLINIC

5)=44;217^ OUTPATIENT

If an error is encountered for NAME, ADMIT, APPT or CLINIC, a "-1"

followed by a caret and the error message text (i.e., -1^error message) is

returned in RESULT(0).

NAME: **GMV MANAGER** TAG: RPC

ROUTINE: GMVRPCM                      RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: SUBSCRIPTION            INACTIVE: ACTIVE

WORD WRAP ON: TRUE

DESCRIPTION:

Performs many functions for the Manager module.

This remote procedure call is documented in Integration Agreement 4360.

INPUT PARAMETER: OPTION                 PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 10               REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

Routine tag line in GMVRPCM to call.

INPUT PARAMETER: DATA                   PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 100              REQUIRED: YES

SEQUENCE NUMBER: 2

DESCRIPTION:

Other data as required for the call.

RETURN PARAMETER DESCRIPTION:

This remote procedure call performs various actions such as building

selection lists and modifying package parameters. The entry point is

RPC^GMVRPCM. It has input parameters of RESULTS, OPTION and DATA (ex:

RPC^GMVRPCM(.RESULTS,OPTION,DATA).

The RESULTS variable will contain the ^TMP("GMVMGR",$J) global array

reference. The ^TMP("GMVMGR",$J) global array contains the results.

The OPTION variable identifies a line label in the GMVRPCM routine

that will be invoked to process the call.

The DATA variable contains any additional values needed by the OPTION

variable to process the call.

1) When the OPTION value is ADDQUAL, this RPC will link a GMRV VITAL

QUALIFIER (#120.52) file entry to a GMRV VITAL TYPE (#120.51) file entry.

The DATA value is a three part value separated by semi-colons(;). The

first value is the FILE 120.51 internal entry number (IEN). The second

value is the GMRV VITAL CATEGORY (#120.53) IEN. The third value is the

GMRV VITAL QUALIFIER (#120.52).

Example:

&gt; S DATA="1;1;1"

&gt; S OPTION="ADDQUAL"

&gt; D RPC^GMVRPCM(.RESULT,OPTION,DATA) ZW RESULT

&gt; RESULT="^TMP("GMVMGR",539356158)"

&gt; D ^%G

&gt; Global ^TMP("GMVMGR",$J

&gt; ^TMP("GMVMGR",539356158,0)=1^Qualifier Assigned

If an error is encountered, a "-1" followed by a caret and the error

message text (i.e., -1^error message) is returned.

2) When the OPTION value is DELQUAL, this RPC will unlink a qualifier to

a GMRV VITAL TYPE (#120.51) file entry.

The DATA value is a three part value separated by semi-colons. The first

value is the FILE 120.51 internal entry number (IEN). The second value is

the GMRV VITAL CATEGORY (#120.53) IEN. The third value is the GMRV VITAL

QUALIFIER (#120.52) IEN.

Example:

&gt; S DATA="1;1;1"

&gt; S OPTION="DELQUAL"

&gt; D RPC^GMVRPCM(.RESULT,OPTION,DATA) ZW RESULT

&gt; RESULT="^TMP("GMVMGR",539356158)"

&gt; D ^%G

&gt; Global ^TMP("GMVMGR",$J

&gt; ^TMP("GMVMGR",539356158,0)=1^Qualifier removed.

If an error is encountered, a "-1" followed by a caret and the error

message text (i.e., -1^error message) is returned.

3) When the OPTION value is DELTEMP, this RPC will delete a data input

template definition.

The DATA value is a two part value separated by a caret (^). The first

value is the ENTITY value. See IA #2263 for a list of entity values.

The second value is the name of the data input template.

Example:

&gt; S DATA="USR^PAIN ONLY"

&gt; S OPTION="DELTEMP"

&gt; D RPC^GMVRPCM(.RESULT,OPTION,DATA) ZW RESULT

&gt; RESULT="^TMP("GMVMGR",539356158)"

&gt; D ^%G

&gt; Global ^TMP("GMVMGR",$J

&gt; ^TMP("GMVMGR",539356158,0)=1^Template Removed.

If an error is encountered, a "-1" followed by a caret and the error

message text (i.e., -1^error message) is returned.

4) When the OPTION value is GETCATS, this RPC will return a list of

qualifiers (FILE 120.52) associated with a vital type (FILE 120.51).

The DATA value is a one part value. It is a pointer value to FILE 120.51

The TMP global contains:

^TMP("GMVMGR",$J,0)=piece1^piece2

^TMP("GMVMGR",$J,n)=piece3^piece4^piece5

where piece1 = number of categories (FILE 120.53) associated with this

vital type

piece2 = vital type name

piece3 = category IEN (FILE 120.53)

piece4 = category name (FILE 120.53, Field .01)

piece5 = qualifier names (FILE 120.52, Field .01) separated by a

comma and space

n = sequential number starting with 1

Example:

&gt; S DATA="21"

&gt; S OPTION="GETCATS"

&gt; D RPC^GMVRPCM(.RESULT,OPTION,DATA) ZW RESULT

&gt; RESULT="^TMP("GMVMGR",539356158)"

&gt; D ^%G

&gt; Global ^TMP("GMVMGR",$J

&gt; ^TMP("GMVMGR",539356158,0)=1^PULSE OXIMETRY

1)=2^METHOD^AEROSOL/HUMIDIFIED MASK, CPAP, FACE

TENT, L ARM, MASK, NASAL CANNULA, NON RE-BREATHER, PARTIAL RE-BREATHER,

ROOM AIR, T-PIECE, TRACHEOSTOMY COLLAR, VENTILATOR, VENTURI MASK

If an error is encountered, a "-1" followed by a caret and the error

message text (i.e., -1^error message) is returned.

5) When the OPTION value is GETDATA, this RPC will return the value of

the entry you specify.

The DATA value is a three part value. The first part is the file number.

The second part is the IEN number of the entry. The third part is the

field number.

The TMP global contains:

^TMP("GMVMGR",$J,0)=external value of the field

Example:

&gt; S DATA="120.51^1^1"

&gt; D RPC(.RESULT,"GETDATA",DATA) ZW RESULT

&gt; RESULT="^TMP("GMVMGR",539339804)"

&gt; D ^%G

&gt; Global ^TMP("GMVMGR",$J

&gt; ^TMP("GMVMGR",539339804,0)=BP

If a value cannot be found, then a null value is returned.

6) When the OPTION value is GETDEF, this RPC will return default template

names.

The DATA value is a one part value. If it is null, then all default

templates for that user will be returned.

The TMP global contains:

^TMP("GMVMGR",$J,0)=piece1

^TMP("GMVMGR",$J,n)=piece2^piece3

where piece1 = number of templates found

piece2 = an IEN value, a semi-colon, and a global reference

piece3 = template name

n = sequential number starting with 1

Example A:

&gt; S DATA=""

&gt; S OPTION="GETDEF"

&gt; D RPC^GMVRPCM(.RESULT,OPTION,DATA) ZW RESULT

&gt; RESULT="^TMP("GMVMGR",539356158)"

&gt; D ^%G

&gt; Global ^TMP("GMVMGR",$J

&gt; ^TMP("GMVMGR",539356158,0)=4

1)=125;SC(^WARD 10A

2)=334;DIC(4.2,^TEST

3)=4601;VA(200,^Height ONLY

4)=547;VA(200,^All Vital Signs

If the DATA value is an entity value (see IA 2263 for a list of entity

values), then the default template name for that entity will be returned.

The TMP global contains:

^TMP("GMVMGR",$J,0)=template name

Example B:

&gt; S DATA="USR"

&gt; S OPTION="GETDEF"

&gt; D RPC^GMVRPCM(.RESULT,OPTION,DATA) ZW RESULT

&gt; RESULT="^TMP("GMVMGR",539356158)"

&gt; D ^%G

&gt; Global ^TMP("GMVMGR",$J

&gt; ^TMP("GMVMGR",539356158,0)=MY DEFAULT

If an error is encountered, a "-1" followed by a caret and the error

message text (i.e., -1^error message) is returned.

7) When the OPTION value is GETHILO, this RPC will return the abnormal

high or low value for a vital type.

The DATA value is a one part value which identifies a field number in

the GMRV VITALS PARAMETERS (#120.57) field.

The TMP global contains:

^TMP("GMVMGR",$J,0)=field value

Example:

&gt; S DATA=5.2

&gt; S OPTION="GETHILO"

&gt; D RPC^GMVRPCM(.RESULT,OPTION,DATA) ZW RESULT

&gt; RESULT="^TMP("GMVMGR",539356158)"

&gt; D ^%G

&gt; Global ^TMP("GMVMGR",$J

&gt; ^TMP("GMVMGR",539356158,0)=94

A zero is returned if there is no value in the field.

8) When the OPTION value is GETLIST, this RPC returns a list of entries

for the file number specified.

The DATA value is a one part value. It is a file number.

The TMP global contains:

^TMP("GMVMGR",$J,0)=piece1^piece2

^TMP("GMVMGR",$J,n)=piece3^piece4

where piece1 = number of entries returned

piece2 = file name [not returned in all cases]

piece3 = file number, a semi-colon and record IEN

piece4 = the .01 value of the record

n = sequential number starting with 1

Examples:

Retrieve a list of wards.

&gt; S DATA=42

&gt; S OPTION="GETLIST"

&gt; D RPC^GMVRPCM(.RESULT,OPTION,DATA) ZW RESULT

&gt; RESULT="^TMP("GMVMGR",539363784)"

&gt; D ^%G

&gt; Global ^TMP("GMVMGR",$J

&gt; ^TMP("GMVMGR",539363784,0)=26^WARD LOCATION

1)=42;14^10A

n)=42;15^10B

26)=42;39^10Z

Retrieve a list of clinics.

&gt; S DATA=44

&gt; S OPTION="GETLIST"

&gt; D RPC^GMVRPCM(.RESULT,OPTION,DATA) ZW RESULT

&gt; RESULT="^TMP("GMVMGR",539363784)"

&gt; D ^%G

&gt; Global ^TMP("GMVMGR",$J

&gt; ^TMP("GMVMGR",539363784,0)=61

1)=44;6^HOUSE/A

n)=44;8^HOUSE/C

61)=44;39^HOUSE/ZZ

Retrieve a list vital types.

&gt; S DATA=120.51

&gt; S OPTION="GETLIST"

&gt; D RPC^GMVRPCM(.RESULT,OPTION,DATA) ZW RESULT

&gt; RESULT="^TMP("GMVMGR",539363784)"

&gt; D ^%G

&gt; Global ^TMP("GMVMGR",$J

&gt; ^TMP("GMVMGR",539363784,0)=10^GMRV VITAL TYPE

1)=120.51;1^BLOOD PRESSURE

N)=120.51;19^CENTRAL VENOUS PRESSURE

10)=120.51;9^WEIGHT

Retrieve a list of qualifiers.

&gt; S DATA=120.52

&gt; S OPTION="GETLIST"

&gt; D RPC^GMVRPCM(.RESULT,OPTION,DATA) ZW RESULT

&gt; RESULT="^TMP("GMVMGR",539363784)"

&gt; D ^%G

&gt; Global ^TMP("GMVMGR",$J

&gt; ^TMP("GMVMGR",539363784,0)=80^GMRV VITAL QUALIFIER

1)=120.52;74^ABDOMINAL

n)=120.52;42^ACTUAL

80)=120.52;99^WRIST

Retrieve a list of CPRS teams.

&gt; S DATA=100.21

&gt; S OPTION="GETLIST"

&gt; D RPC^GMVRPCM(.RESULT,OPTION,DATA) ZW RESULT

&gt; RESULT="^TMP("GMVMGR",539363784)"

&gt; D ^%G

&gt; Global ^TMP("GMVMGR",$J

&gt; ^TMP("GMVMGR",539363784,0)=103

1)=100.21;28^1AS

n)=100.21;60^1ASO

103)=100.21;96^consult team

Retrieve a list of nursing units.

&gt; S DATA=211.4

&gt; S OPTION="GETLIST"

&gt; D RPC^GMVRPCM(.RESULT,OPTION,DATA) ZW RESULT

&gt; RESULT="^TMP("GMVMGR",539363784)"

&gt; D ^%G

&gt; Global ^TMP("GMVMGR",$J

&gt; ^TMP("GMVMGR",539363784,0)=21

1)=211.4;7^10E

n)=211.4;17^10W

21)=211.4;9^SICU

If an error is encountered, a "-1" followed by a caret and the error

message text (i.e., -1^error message) is returned.

9) When the OPTION value is GETQUAL, this RPC returns a list of

qualifiers associated with this vital type.

The DATA value is a two part value separated by a semi-colon. The first

part is vital type (FILE 120.51) IEN. The second part is a category (FILE

120.53) IEN.

The TMP global contains:

^TMP("GMVMGR",$J,0)=piece1^piece2

^TMP("GMVMGR",$J,n)=piece3^piece4

where piece1 = number of entries found

piece2 = category name (FILE 120.53, Field .01)

piece3 = qualifier IEN

piece4 = qualifier name (FILE 120.52, Field .01)

n = sequential number starting with 1

Example:

&gt; S DATA="1;1",OPTION="GETQUAL"

&gt; D RPC^GMVRPCM(.RESULT,OPTION,DATA) ZW RESULT

&gt; RESULT="^TMP("GMVMGR",539356158)"

&gt; D ^%G

&gt; Global ^TMP("GMVMGR",$J

&gt; ^TMP("GMVMGR",539356158,0)=6^LOCATION

1)=139^Test Qualifier

2)=53^FEMORAL

3)=2^L ARM

4)=4^L LEG

5)=24^PERIPHERAL

6)=1^R ARM

If an error is encountered, a "-1" followed by a caret and the error

message text (i.e., -1^error message) is returned.

10) When the OPTION value is GETTEMP, this RPC will return a list data

input templates defintions.

The DATA value is a two part value separated by a caret. The first part

is an entity value. See IA 2263 for a list of entities. The second part is

a data input template name.

When DATA is null, all data input template definitions are returned.

The TMP global contains:

^TMP("GMVMGR",$J,0)=piece1

^TMP("GMVMGR",$J,n)=piece2^piece3^piece4^piece5^piece6

where piece1 = number of entries returned

piece2 = 1, 2, 3, or 4. (1 = Domain, 2 = Institution, 3 = Hospital

location and 4 = New Person)

piece3 = file IEN, a semi-colon and global reference

piece4 = Field .01 value of the file specified in piece3

piece5 = template name

piece6 = template description text, a bar, vital type IEN (FILE

120.51), a colon, a metric flag (0= and 1=metric), category IEN

(FILE 120.53), a coma, and a qualifier IEN (FILE 120.52), a tilde

indicates additional category and qualifier combinations for the vital

type. A semi-colon indicates the start of the next vital type.

n = sequential number starting with 1

Example:

&gt; S DATA="USR",OPTION="GETTEMP"

&gt; D RPC^GMVRPCM(.RESULT,OPTION,DATA) ZW RESULT

&gt; RESULT="^TMP("GMVMGR",539356158)"

&gt; D ^%G

&gt; Global ^TMP("GMVMGR",$J

&gt; ^TMP("GMVMGR",539356158,0)=1

1)=4^547;VA(200,^VITUSER,ONE^MY DEFAULT^ALL

VITALS|1:0:1,2~2,59~3,50;20:1|

If an error is encountered, a "-1" followed by a caret and the error

message text (i.e., -1^error message) is returned.

11) When the OPTION value is LOOKUP, this RPC will do a file lookup

The DATA value is a three part value separated by a caret. The first part

is a file number. The second part is a value to look up. The third part is

the field or fields to do the look up on. If the third piece is not

defined, the lookup is done on the .01 field of the file.

The TMP global contains:

^TMP("GMVMGR",$J,0)=piece1

^TMP("GMVMGR",$J,n)=piece2^piece3

where piece1 = number of entries found

piece2 = file number, a semi-colon and record IEN

piece3 = field value

Example:

&gt; S DATA="44^OUTPAT^.01",OPTION="LOOKUP"

&gt; D RPC^GMVRPCM(.RESULT,OPTION,DATA) ZW RESULT

&gt; RESULT="^TMP("GMVMGR",539359648)"

&gt; D ^%G

&gt; Global ^TMP("GMVMGR",$J

&gt; ^TMP("GMVMGR",539359648,0)=3

1)=44;75^OUTPATIENT NUC MED

2)=44;74^OUTPATIENT RADIOLOGY

3)=44;80^OUTPATIENT ULTRASOUND

If an error is encountered, a "-1" followed by a caret and the error

message text (i.e., -1^error message) is returned.

12) When the OPTION value is NEWQUAL, this RPC will always return an

error message instructing the user to use the New Term Rapid Turnaround

process.

The DATA value is always null.

Example:

&gt; S DATA=""

&gt; S OPTION="NEWQUAL"

&gt; D RPC^GMVRPCM(.RESULT,OPTION,DATA) ZW RESULT

&gt; RESULT="^TMP("GMVMGR",539356158)"

&gt; D ^%G

&gt; Global ^TMP("GMVMGR",$J

&gt; ^TMP("GMVMGR",539356158,0)=-1^Use the New Term Rapid Turnaround (NTRT)

process to add qualifiers

13) When the OPTION value is NEWTEMP, this RPC will file a new data

input template.

The DATA value is a three part value separated by a caret. The first part

is an entity. See IA 2263 for a list of entities. The second part is

the name of the data input template. The third part is the description

text. If the third part is null, the template description will default to

"No Description".

The TMP global contains:

^TMP("GMVMGR",$J,0)=piece1^piece2^piece3^piece4

where piece1 = 1, 2, 3, or 4 (1 = DOMAIN (#4.2), 2 = INSTITUTION (#4),

3 = HOSPITAL LOCATION, and 4 = NEW PERSON)

piece2 = IEN, a semi-colon, and global reference (e.g., 3;DIC(4.2)

piece3 = the .01 field value for the record in piece2

piece4 = data input name

Example:

&gt; S DATA="USR^1 EAST^All Vital Types"

&gt; S OPTION="NEWTEMP"

&gt; D RPC^GMVRPCM(.RESULT,OPTION,DATA) ZW RESULT

&gt; RESULT="^TMP("GMVMGR",539343036)"

&gt; D ^%G

&gt; Global ^TMP("GMVMGR",$J

&gt; ^TMP("GMVMGR",539343036,0)=4^547;VA(200,^VITUSER,ONE^1 EAST

If an error is encountered, a "-1" followed by a caret and the error

message text (i.e., -1^error message) is returned.

14) When the OPTION value is RENTEMP, this RPC will rename a data input

template.

The DATA value is a three part value separated by a caret. The first part

is an entity. See IA 2263 for a list of entities. The second part is the

current template name. The third part is the new name of the template.

The TMP global contains:

^TMP("GMVMGR",$J,0)=1^Renamed

Example:

&gt; S DATA="USR^FRANK'S DEFAULT^MY DEFAULT"

&gt; S OPTION="RENTEMP"

&gt; D RPC^GMVRPCM(.RESULT,OPTION,DATA) ZW RESULT

&gt; RESULT="^TMP("GMVMGR",539356158)"

&gt; D ^%G

&gt; Global ^TMP("GMVMGR",$J

&gt; ^TMP("GMVMGR",539356158,0)=1^Renamed

If an error is encountered, a "-1" followed by a caret and the error

message text (i.e., -1^error message) is returned.

15) When the OPTION value is SETDATA, this RPC always returns an error

message that instructs the user to use the New Term Rapid Turnaround

process.

The DATA value is null.

Example:

&gt; S DATA=""

&gt; S OPTION="SETDATA"

&gt; D RPC^GMVRPCM(.RESULT,OPTION,DATA) ZW RESULT

&gt; RESULT="^TMP("GMVMGR",539356158)"

&gt; D ^%G

&gt; Global ^TMP("GMVMGR",$J

&gt; ^TMP("GMVMGR",539356158,0)=-1^Use the New Term Rapid Turnaround (NTRT)

process to add qualifiers

16) When the OPTION value is SETDEF, this RPC will set that data input

template as a default.

The DATA value is a two part value separated by a caret. The first part is

an entity. See IA 2263 for a list of entities. The second part is the

name of the template that will become the default template.

The TMP global contains:

^TMP("GMVMGR",$J,0)=1^Set As Default

Example:

&gt; S DATA="USR^FRANK'S LIST"

&gt; S OPTION="SETDEF"

&gt; D RPC^GMVRPCM(.RESULT,OPTION,DATA) ZW RESULT

&gt; RESULT="^TMP("GMVMGR",539356158)"

&gt; D ^%G

&gt; Global ^TMP("GMVMGR",$J

&gt; ^TMP("GMVMGR",539356158,0)=1^Set As Default.

If an error is encountered, a "-1" followed by a caret and the error

message text (i.e., -1^error message) is returned.

17) When the OPTION value is SETHILO, this RPC will set the high and low

abnormal values for a vital type.

The DATA value is a two part value separated by a caret. The first part

is a field number in the GMRV VITALS PARAMETERS (#120.57) file. The

second part is the value that field should be set to.

The TMP global contains:

^TMP("GMVMGR",$J,0)=1^Update Complete.

Example:

&gt; S DATA="5.1^102",OPTION="SETHILO"

&gt; D RPC^GMVRPCM(.RESULT,OPTION,DATA) ZW RESULT

&gt; RESULT="^TMP("GMVMGR",539356158)"

&gt; D ^%G

&gt; Global ^TMP("GMVMGR",$J

&gt; ^TMP("GMVMGR",539356158,0)=1^Update Complete.

If an error is encountered, a "-1" followed by a caret and the error

message text (i.e., -1^error message) is returned.

18) When the OPTION value is SETTEMP, this RPC will save the input

template definition.

DATA is a three part value separated by a caret. The first part is

an entity. See IA 2263 for a list of entities. The second part is the

template name. The third part is the template definition.

The TMP global contains:

^TMP("GMVMGR",$J,0)=1^Template Saved.

Example:

&gt; S DATA="USR^ONE VITAL TYPE ONLY^CONTAINS ONLY ONE VITAL TYPE|2:0:1,102"|

&gt; S OPTION="SETTEMP"

&gt; D RPC^GMVRPCM(.RESULT,OPTION,DATA) ZW RESULT

&gt; RESULT="^TMP("GMVMGR",539356158)"

&gt; D ^%G

&gt; Global ^TMP("GMVMGR",$J

&gt; ^TMP("GMVMGR",539356158,0)=1^Template Saved.

If an error is encountered, a "-1" followed by a caret and the error

message text (i.e., -1^error message) is returned.

19) When the OPTION value is VALID, this RPC will validate data.

DATA is a four part value separated by a caret. The first part is the

a file number. The second part is a record number. The third part is a

field number. The fourth part is the value to validate.

The TMP global contains:

^TMP("GMVMGR",$J,0)=1^Valid Data

Example:

&gt; S DATA="120.5^8864^.01^3051012.1034",OPTION="VALID"

&gt; D RPC^GMVRPCM(.RESULT,OPTION,DATA) ZW RESULT

&gt; RESULT="^TMP("GMVMGR",539343036)"

&gt; D ^%G

&gt; Global ^TMP("GMVMGR",$J

&gt; ^TMP("GMVMGR",539343036,0)=1^Valid Data

If an error is encountered, a "-1" followed by a caret and the error

message text (i.e., -1^error message) is returned.

NAME: **GMV MARK ERROR** TAG: ERROR

ROUTINE: GMVUTL1                      RETURN VALUE TYPE: SINGLE VALUE

AVAILABILITY: SUBSCRIPTION            INACTIVE: ACTIVE

DESCRIPTION:

This remote procedure call marks a selected vitals record in the GMRV

Vital Measurement (#120.5) file as entered-in-error.

This remote procedure call is documented in Integration Agreement 4414.

INPUT PARAMETER: GMVDATA                PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 60               REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

GMVDATA contains the following information:

piece1^piece2^piece3

where piece1 = FILE 120.5 IEN

piece2 = FILE 200 IEN (i.e., DUZ)

piece3 = A single value to indicate the reason for the error.

1 = INCORRECT DATE/TIME, 2 = INCORRECT , 3 =

INCORRECT PATIENT and 4 = INVALID RECORD

RETURN PARAMETER DESCRIPTION:

If the record is marked as entered in error, RESULT is set to "OK".

Otherwise, RESULT is set to "Record Not Found"

Example:

&gt; S GMVDATA="1560^547^1"

&gt; D ERROR^GMVUTL1(.RESULT,GMVDATA) ZW RESULT

&gt; RESULT="OK"

NAME: **GMV NUR UNIT PT** TAG: APTLIST

ROUTINE: GMVUTL8                      RETURN VALUE TYPE: ARRAY

AVAILABILITY: RESTRICTED              INACTIVE: ACTIVE

DESCRIPTION:

Returns a list of active patients for a nursing location.

INPUT PARAMETER: LOC                    PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 60               REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

NURS LOCATION file (#211.4) ien.

RETURN PARAMETER DESCRIPTION:

ARRAY - Subscripted by sequential number with DFN in first piece and

patient name in second piece.

example: ARRAY(#)=DFN^patient name^SSN^DOB^SEX AND AGE^ATTENDING^VETERAN

^INTERNAL DATE/TIME DECEASED^EXTERNAL DATE/TIME DECEASED

NAME: **GMV PARAMETER** TAG: RPC

ROUTINE: GMVPAR                       RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: SUBSCRIPTION            INACTIVE: ACTIVE

WORD WRAP ON: TRUE

DESCRIPTION:

Sets and retrieves parameter values used by the graphical user interface.

This remote procedure call is documented in Integration Agreement 4367.

INPUT PARAMETER: OPTION                 PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 10               REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

Routine tag line to call.

INPUT PARAMETER: ENT                    PARAMETER TYPE: LITERAL

SEQUENCE NUMBER: 2

DESCRIPTION:

The entity value to use. See Integration Agreement 2263 and FILE 8989.518

for a list of entity values.

INPUT PARAMETER: PAR                    PARAMETER TYPE: LITERAL

SEQUENCE NUMBER: 3

DESCRIPTION:

The parameter value to use. See FILE 8989.51 for a list of parameter

values. This value must start with the letters "GMV" (no quotes).

INPUT PARAMETER: INST                   PARAMETER TYPE: LITERAL

SEQUENCE NUMBER: 4

DESCRIPTION:

The instance to use.

INPUT PARAMETER: VAL                    PARAMETER TYPE: LITERAL

SEQUENCE NUMBER: 6

DESCRIPTION:

The value assigned to a parameter. Values are stored in FILE 8989.5.

RETURN PARAMETER DESCRIPTION:

This remote procedure call sets and retrieves parameter settings that

are used in the graphical user interface.

The entry point is RPC^GMVPAR.. It has input parameters of RESULTS,

OPTION, ENT, PAR, INST and VAL (ex:

RPC^GMVPAR(RESULTS,OPTION,ENT,PAR,INST,VAL).

The RESULTS variable contains the results of the call or the location

where the results can be found.

The OPTION variable identifies the entry point in the GMVPAR routine

that will be invoked to process the call.

If an error occurrs, the ^TMP global contains:

^TMP($J,0)=-1^error message text

1) When the OPTION value is DELPAR, this RPC deletes the value for the

instance, parameter and entity specified.

The TMP global contains:

^TMP($J,0)=1^Instance deleted

Example:

&gt; S OPTION="DELPAR",ENT="SYS",PAR="GMV DLL VERSION"

&gt; S INST="GMV\_VITALSVIEWENTER.DLL:v. 07/21/05 10:34"

&gt; D RPC^GMVPAR(.RESULT,OPTION,ENT,PAR,INST) ZW RESULT

&gt; RESULT="^TMP(538999278)"

&gt; D ^%G

&gt; Global ^TMP($J

&gt; ^TMP(538999278,0)=1^Instance deleted

2) When the OPTION value is ENTVAL, this RPC returns the external value

of the entity specified.

The TMP global contains:

TMP($J,0)=external value

Example:

&gt; S OPTION="ENTVAL",ENT="USR"

&gt; D RPC(.RESULT,OPTION,ENT) ZW RESULT

&gt; RESULT="^TMP(538993252)"

&gt; D ^%G

&gt; Global ^TMP($J

&gt; ^TMP(538993252,0)=TRAXLER,FRANK

3) When the OPTION value is GETLST, this RPC returns a list of instances

and their values for the parameter and entity specified.

The TMP global contains:

^TMP($J,0)=piece1

^TMP($J,n)=piece2^piece3

where piece1 = number of entries returned

piece2 = instance name

piece3 = instance value

n = sequential number starting with 1

Example:

&gt; S OPTION="GETLST",ENT="USR",PAR="GMV USER DEFAULTS"

&gt; D RPC(.RESULT,OPTION,ENT,PAR) ZW RESULT

&gt; RESULT="^TMP(538993252)"

&gt; D ^%G

&gt; Global ^TMP($J

&gt; ^TMP(538993252,0)=44

1)=DefaultTemplate^547;VA(200,|MY DEFAULT|

n)=UNIT\_INDEX^0

44)=WARD\_INDEX^-1

4) When the OPTION value is GETPAR, this RPC will get the value for the

instance, parameter and entity specified.

The TMP global contains:

^TMP($J,0)=piece1

where piece1 = value

Example:

&gt; S ENT="USR",PAR="GMV USER DEFAULTS",INST="DefaultTemplate"

&gt; S OPTION="GETPAR"

&gt; D RPC(.RESULT,OPTION,ENT,PAR,INST) ZW RESULT

&gt; RESULT="^TMP(538993252)"

&gt; D ^%G

&gt; Global ^TMP($J

&gt; ^TMP(538993252,0)=547;VA(200,|MY DEFAULT|

5) When the OPTION value is SETPAR, this RPC set the value of an instance

for the instance, parameter and entity specified.

The TMP global contains:

^TMP($J,0)=1^Parameter updated

Example:

&gt; S OPTION="SETPAR",ENT="USR",PAR="GMV USER DEFAULTS",INST="SearchDelay"

&gt; S VAL=1.5

&gt; D RPC^GMVPAR(.RESULT,OPTION,ENT,PAR,INST,VAL) ZW RESULT

&gt; RESULT="^TMP(538999278)"

&gt; D ^%G

&gt; Global ^TMP($J

&gt; ^TMP(538999278,0)=1^Parameter updated

NAME: **GMV PT GRAPH** TAG: EN1

ROUTINE: GMVSR0                       RETURN VALUE TYPE: SINGLE VALUE

AVAILABILITY: RESTRICTED              INACTIVE: ACTIVE

DESCRIPTION:

Prints Vitals/Measurements Graphic Reports.

INPUT PARAMETER: GMVDATA                PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 150              REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

A multi-piece variable that identifies the values needed to run the

report.

Piece  1: DFN

2: Start date/time of the report range (FileMan format)

3: End date/time of the report range (FileMan format)

4: Number indicating graph type *

5: Device name (File 3.5, Field .01)

6: Device internal entry number

7: date/time to print the report (FileMan format)

8: ward internal entry number (File 42)

9: hospital location internal entry number (File 44)

10: list of rooms separated by a comma (e.g., 200,210,220)

* Graph = 1 prints Vital Signs Record

= 2 prints B/P Plotting Chart

= 3 prints Weight Chart

= 4 prints Pulse Oximetry/Respiratory Graph

= 5 prints Pain Chart

RETURN PARAMETER DESCRIPTION:

Returns a message stating the outcome of the request to queue the report.

If the report was successfully queued, RESULT will be "Report sent to

device. Task #: " ZTSK" where ZTSK is the task number of the job. If the

report could not be queued, RESULT will be "Unable to task the report."

NAME: **GMV PTSELECT** TAG: RPC

ROUTINE: GMVRPCP                      RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED              INACTIVE: ACTIVE

WORD WRAP ON: TRUE

DESCRIPTION:

Used as a method of processing a patient DFN and returning all warnings

and notices (i.e. sensitivity or same last 4 of SSN) to the client

application for processing.  Also includes a call to log access of

sensitive patients to the DG SECURITY LOG file.

INPUT PARAMETER: RESULT                 PARAMETER TYPE: REFERENCE

MAXIMUM DATA LENGTH: 30               REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

This is the RPC return array variable.

INPUT PARAMETER: OPTION                 PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 30               REQUIRED: YES

SEQUENCE NUMBER: 2

DESCRIPTION:

Contains the appropriate method to perform within this RPC call.

Options are:

SELECT: Performs a select of the supplied DFN (param 3) and returns the

notices and warnings for the DFN

LOGSEC: Logs a security entry in the DG SECURITY LOG file.

INPUT PARAMETER: DFN                    PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 12               REQUIRED: YES

SEQUENCE NUMBER: 3

DESCRIPTION:

Contains the DFN of the patient to process in the SELECT or LOGSEC method

of param 2.

INPUT PARAMETER: DATA                   PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 80               REQUIRED: NO

SEQUENCE NUMBER: 4

DESCRIPTION:

Used to pass in the option name to DGSEC when logging against the DG

SECURITY LOG file.

RETURN PARAMETER DESCRIPTION:

RESULTS(0)   =Success or failure flag (-1 or 1) from both SELECT &amp; LOGSEC

methods

RESULTS(1..n)=Messages to process by the client from the SELECT method.

NAME: **GMV QUALIFIER TABLE** TAG: EN1

ROUTINE: GMVCAQU                      RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED              INACTIVE: ACTIVE

WORD WRAP ON: TRUE

DESCRIPTION:

Prints a list of categories and qualifiers associated with individual

vital types (e.g., blood pressure). Data comes from the GMRV Vital

Qualifier (#120.52) file and the GMRV Vital Category (#120.53) file.

INPUT PARAMETER: GMVDATA                PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 150              REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

A multi-piece variable that identifies the values needed to run the

report.

Piece  1: n/a

2: n/a

3: n/a

4: n/a

5: Device name (File 3.5, Field .01)

6: Device internal entry number

7: date/time to print the report (FileMan format)

8: n/a

9: n/a

10: n/a

RETURN PARAMETER DESCRIPTION:

Returns a message stating the outcome of the request to queue the report.

If the report was successfully queued, RESULT will be "Report sent to

device. Task #: " ZTSK" where ZTSK is the task number of the job. If the

report could not be queued, RESULT will be "Unable to task the report."

NAME: **GMV ROOM/BED** TAG: ROOMBED

ROUTINE: GMVGETD                      RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED              INACTIVE: ACTIVE

WORD WRAP ON: TRUE

DESCRIPTION:

This procedure extracts room/bed information from Room-Bed file (#405.4)

for a given MAS ward.

INPUT PARAMETER: GMRWARD                PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 30               REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

GMRWARD is a MAS ward name from the Ward Location file (#42).

RETURN PARAMETER DESCRIPTION:

Returns the global array name (i.e., ^TMP($J,"GROOM")) containing a list

of rooms/beds for the given MAS ward.

^TMP($J,"GROOM",n)=Roombed

n is a sequential number starting at 1.

If there is no data, then the global array is undefined.

NAME: **GMV TEAM PATIENTS** TAG: TEAMPT

ROUTINE: GMVUTL3                      RETURN VALUE TYPE: ARRAY

AVAILABILITY: RESTRICTED              INACTIVE: ACTIVE

WORD WRAP ON: TRUE

DESCRIPTION:

This procedure retrieves patients assigned to a given team.

INPUT PARAMETER: GMVTEAM                PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 30               REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

GMVTEAM is the internal entry number of the selected team (File 100.21).

RETURN PARAMETER DESCRIPTION:

Returns a list of patients in the array specified.

RESULT(n)=Patient name^DFN^SSN (w/hyphens)^DOB (external)^SEX and AGE^

Attending^Veteran^Date of Death (external)^Date of Death

(internal)^Ward name^Roombed

n is a sequential number starting at 1.

NAME: **GMV USER** TAG: RPC

ROUTINE: GMVRPCU                      RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: SUBSCRIPTION            INACTIVE: ACTIVE

WORD WRAP ON: TRUE

DESCRIPTION:

Retrieves data about the user (e.g., parameter settings).

This remote procedure call is documented in Integration Agreement 4366.

INPUT PARAMETER: OPTION                 PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 10               REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

Routine tag line to call in GMVRPCU.

INPUT PARAMETER: DATA                   PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 100              REQUIRED: YES

SEQUENCE NUMBER: 2

DESCRIPTION:

Other data as required for the call.

RETURN PARAMETER DESCRIPTION:

This Remote Procedure Call (RPC) performs various actions focusing on the

user. The entry point is RPC^GMVRPCU. It has input parameters of RESULTS,

OPTION and DATA (e.g., RPC^GMVRPCU(RESULTS,OPTION,DATA)).

The RESULTS variable contains the results of the call or the location

where the results can be found.

The OPTION variable identifies another entry point in the GMVRPCU routine

that is invoked to process the call.

The DATA variable contains any values needed by the OPTION variable to

process the call.

1) When the OPTION value is SETPAR, this RPC will set and/or delete the

value of a GMV USER DEFAULTS setting (e.g., the user's default template).

The DATA value is a two part value separated by a caret. The first part

is name of a setting. The second part is the value of the setting. If the

second part is null, the existing value of the setting is deleted.

The TMP global contains:

^TMP("GMVUSER",$J,0)=1^Parameter set.

or

^TMP("GMVUSER",$J,0)=1^Parameter cleared

Example:

&gt; S DATA="DefaultTemplate^547;VA(200,|MY DEFAULT",OPTION="SETPAR"|

&gt; D RPC^GMVRPCU(.RESULT,OPTION,DATA) ZW RESULT

&gt; RESULT="^TMP("GMVUSER",539374023)"

&gt; D ^%G

&gt; Global ^TMP("GMVUSER",$J

&gt; ^TMP("GMVUSER",539374023,0)=1^Parameter set.

If an error is encountered, a "-1" followed by a caret and the error

message text (i.e., -1^error message) is returned.

2) When the OPTION value is GETPAR, this RPC will return the value of the

GMV USER DEFAULTS setting specified in the DATA value.

The DATA value is a one part value. It is the name of a setting (e.g.,

the user's default template).

The TMP global contains:

^TMP("GMVUSER",$J,0)=value of setting or null

Example:

&gt; S DATA="DefaultTemplate",OPTION="GETPAR"

&gt; D RPC^GMVRPCU(.RESULT,OPTION,DATA) ZW RESULT

&gt; RESULT="^TMP("GMVUSER",539374023)"

&gt; D ^%G

&gt; Global ^TMP("GMVUSER",$J

&gt; ^TMP("GMVUSER",539374023,0)=547;VA(200,|ONE VITAL TYPE ONLY|

3) When the OPTION value is SIGNON, this RPC will return information about

the user who is currently signed onto the system.

The DATA value is not used. The user's IEN (i.e., DUZ) to the NEW PERSON

(#200) file value must be defined when this call is made.

The RESULT variable will return the following array:

RESULT(0)=NEW PERSON (#200) file internal entry number (DUZ)

RESULT(1)=User's name (FILE 200, Field .01)

RESULT(2)=Domain (FILE 4.2) internal entry number

RESULT(3)=Domain name (FILE 4.2, Field .01)

RESULT(4)=Institution (FILE 4) internal entry number the user is signed

into (i.e., DUZ(2))

RESULT(5)=Institution name (FILE 4, Field .01)

RESULT(6)="0" or "1". "1" indicates the user has the GMV MANAGER or

programmer key. "0" indicates the user has neither key.

RESULT(7)=The user's title (FILE 200, Field 8)

RESULT(8)=This value is always null.

RESULT(9)=Number of seconds the system will wait for a response from

the user (i.e., DTIME). The default time is 300 seconds.

RESULT(10)=INSTITUTION (#4) file IEN^FILE 4 external value^station

number (e.g., 499^SUPPORT ISC^499).

Example:

&gt; S OPTION="SIGNON"

&gt; D RPC(.RESULT,OPTION) ZW RESULT

&gt; RESULT="^TMP("GMVUSER",539375907)"

&gt; D ^%G

&gt; Global ^TMP("GMVUSER",$J

&gt; ^TMP("GMVUSER",539375907,0)=547

1)=VITUSER,ONE

2)=334

3)=DEV.DEV.FO-HINES.MED.VA.GOV

4)=499

5)=SUPPORT ISC

6)=1

7)=PROGRAMMER

8)=

9)=9999

10)=499^SUPPORT ISC^499

NAME: **GMV V/M ALLDATA** TAG: VMDATA

ROUTINE: GMVGGR1                      RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: SUBSCRIPTION            INACTIVE: ACTIVE

WORD WRAP ON: TRUE

DESCRIPTION:

This remote procedure call lists all vitals/measurements data for a given

date/time span.

This remote procedure call is documented in Integration Agreement 4654.

INPUT PARAMETER: GMVDATA                PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 60               REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

GMVDATA consists of 4 pieces of data:

piece1^piece2^piece3^piece4

where piece1 = File 2 IEN (i.e., DFN)

piece2 = Start date/time for search (FileMan internal format)

piece3 = End date/time for search (FileMan internal format)

piece4 = 0 (zero)

RETURN PARAMETER DESCRIPTION:

RESULT array returns the data or a "NO DATA" message.

Case A: The NO DATA message is returned.

The TMP global returns:

^TMP($J,1)=lastname,first  social security number  date of birth  age

"(Yrs)" gender

^TMP($J,2)="Unit:" unit  "Room:" room

^TMP($J,3)="Division:" division

^TMP($J,4)= search date range

^TMP($J,5)="NO DATA"

Example:

&gt; S GMVDATA="90^3051012^3051012^0"

&gt; D VMDATA^GMVGGR1(.RESULT,GMVDATA) ZW RESULT

&gt; RESULT="^TMP(539349605)"

&gt; D ^%G

&gt; Global ^TMP($J

&gt; ^TMP(539349605,1)=VITPATIENT,ONE 000-11-1234  JAN 2,1934  71 (Yrs)

MALE

2)=Unit:    Room:

3)=Division:

4)=OCT 11,2005 - OCT 11,2005

5)=NO DATA

Case B: Fourth piece of GMVDATA (Flag) is 0

The TMP global returns:

^TMP($J,1)=lastname,first social security number  date of birth  age

"(Yrs)" sex

^TMP($J,2)="Unit:" unit  "Room:" room

^TMP($J,3)="Division:" division

^TMP($J,4)= search date range

^TMP($J,n)=piece1 through piece23

where piece1 = date of reading in mm-dd-yy format

piece2 = time of reading in hh:mm:ss format

piece3 = Temperature value and qualifier abbreviations

piece4 = Pulse value and qualifier abbreviations

piece5 = Respiration and qualifier abbreviations

piece6 = Pulse Oximetry value, qualifier abbreviations, flow rate

and percentage value

piece7 = Blood Pressure value and qualifier abbreviations

piece8 = Weight value (pounds) and qualifier abbreviations

piece9 = Weight value (kilos)

piece10 = Body Mass Index calculation

piece11 = Height value (inches) and qualifier abbreviations

piece12 = Height value (centimeters)

piece13 = Circumference Girth value (inches) and qualifier

abbreviations

piece14 = Circumference Girth value (centimeters)

piece15 = Central Venous Pressure value (cmH2O)

piece16 = Central Venous Pressure value (mmHg)

piece17 = Input value (from Intake &amp; Output package)

piece18 = Output value (from Intake &amp; Output package)

piece19 = Pain value

piece20 = always null

piece21 = always null

piece22 = hospital location (FILE 44, Field .01)

piece23 = name of person who entered the data (FILE 200, Field .01)

piece24 = database where the record is stored

Example:

&gt; S GMVDATA="134^3050901^3050930^0"

&gt; D VMDATA^GMVGGR1(.RESULT,GMVDATA) ZW RESULT

&gt; RESULT="^TMP(539349605)"

&gt; D ^%G

&gt; Global ^TMP($J

&gt; ^TMP(539349605,1)=VITPATIENT,TWO 000-11-1234  JUN 1,1957  48 (Yrs)

FEMALE

2)=Unit: 2-ASM   Room:

3)=Division: TEST HINES

4)=SEP 1,2005 - SEP 30,2005

5)=09-14-05^17:18:00^^^^^^^61.36^22^66-

A^167.64^^^^^^^^ ^^2-ASM^VITPROVIDER,ONE^Vitals

6)=09-26-05^11:30:57^^^^^120/80*- La Si Car

Clf^^^^^^^^^^^^^^^2-A SM^VITPROVIDER,TWO^Vitals.

NAME: **GMV VITALS/CAT/QUAL** TAG: GETVITAL

ROUTINE: GMVUTL7                      RETURN VALUE TYPE: ARRAY

AVAILABILITY: SUBSCRIPTION            INACTIVE: ACTIVE

WORD WRAP ON: TRUE

DESCRIPTION:

Returns all qualifier information for the vital types selected.

This remote procedure call is documented in Integration Agreement 4359.

INPUT PARAMETER: GMVLIST                PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 60               REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

A list of vital type abbreviations (FILE 120.51, Field 1) separated by

up-arrows (e.g., "HT^WT" for height and weight). When the value is null,

all qualifier information will be returned for all vital types.

RETURN PARAMETER DESCRIPTION:

Returns the qualifier information for the selected vital types in the

array specified. Includes the abnormal high and low values for the vital

type, if any.

The result array contains:

RESULT(n)=piece1^piece2^piece3^piece4^piece5^piece6^piece7^piece8^piece9

RESULT(n.nnn)=pieceA^pieceB^pieceC^pieceD

where n is a sequential number starting with 1

piece1 = V for vital type

piece2 = FILE 120.51 IEN for this vital type

piece3 = vital type name (FILE 120.51, Field .01)

piece4 = Abbreviation (FILE 120.51, Field 1)

piece5 = PCE Abbreviation (FILE 120.51, Field 7)

piece6 = If vital type is Blood Pressure this is the

abnormal systolic high value (File 120.57, Field 5.7).

If vital type is Temperature, this is the abnormal high

value (File 120.57, Field 5.1)

If vital type is Respiration, this is the abnormal high

value (File 120.57, Field 5.5)

If vital type is Pulse, this is the abnormal high value

(File 120.57, Field 5.3)

If vital type is Central Venous Pressure, this is the

abnormal high value (File 120.57, Field 6.1)

piece7 = If vital type is Blood Pressure this is the

abnormal diastolic high value (File 120.57, Field 5.71).

If vital type is Temperature, this is the abnormal low

value (File 120.57, Field 5.2)

If vital type is Respiration, this is the abnormal low

value (File 120.57, Field 5.6)

If vital type is Pulse, this is the abnormal low value

(File 120.57, Field 5.4)

If vital type is Central Venous Pressure, this is the

abnormal low value (File 120.57, Field 6.2)

piece8 = If vital type is Blood Pressure this is the

abnormal systolic low value (File 120.57, Field 5.8).

If vital type is Central Pressure, this is the abnormal

O2 saturation (File 120.57, Field 6.3)

piece9 = If vital type is Blood Pressure this is the

abnormal diastolic low value (File 120.57, Field 5.81).

RESULT(n.nnn)=pieceA^pieceB^pieceC^pieceD

where pieceA = C for CATEGORY or Q for QUALIFIER

if pieceA is C, then

pieceB = FILE 120.53 IEN for this category

pieceC = category name (FILE 120.53, Field .01)

pieceD = null

if pieceB is Q, then

pieceB = FILE 120.52 IEN for this qualifier

pieceC = qualifier name (FILE 120.52, Field .01)

pieceD = synonym (FILE 120.52, Field .02)

Example:

&gt; S GMVLIST="HT^WT"

&gt; D GETVITAL^GMVUTL7(.RESULT,GMVLIST) ZW RESULT

&gt; RESULT(1)="V^8^HEIGHT^HT^HT^"

&gt; RESULT(1.001)="C^4^QUALITY"

&gt; RESULT(1.002)="Q^42^ACTUAL^A"

&gt; RESULT(1.003)="Q^43^ESTIMATED^E"

&gt; RESULT(1.004)="Q^107^Stated^St"

&gt; RESULT(2)="V^9^WEIGHT^WT^WT^"

&gt; RESULT(2.001)="C^2^METHOD"

&gt; RESULT(2.002)="Q^39^OTHER^Oth"

&gt; RESULT(2.003)="Q^50^SITTING^Si"

&gt; RESULT(2.004)="Q^51^STANDING^St"

&gt; RESULT(2.005)="C^4^QUALITY"

&gt; RESULT(2.006)="Q^42^ACTUAL^A"

NAME: **GMV WARD LOCATION** TAG: WARDLOC

ROUTINE: GMVGETD                      RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED              INACTIVE: ACTIVE

WORD WRAP ON: TRUE

DESCRIPTION:

This procedure extracts MAS ward locations from the Ward Location file

(#42).

INPUT PARAMETER: DUMMY                  PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 1                REQUIRED: NO

SEQUENCE NUMBER: 1

DESCRIPTION:

When this input parameter is set to the letter "P", only wards that have

patients will be returned. Otherwise, all active wards will be returned.

RETURN PARAMETER DESCRIPTION:

Returns the global array name containing a list of MAS wards (i.e.,

^TMP($J,"GWARD")).

^TMP($J,"GWARD",n)=piece1^piece2^piece3

where:

piece1 = ward IEN (FILE 42)

piece2 = ward name (FILE 42, Field .01)

piece3 = hospital location IEN (FILE 44)

n is a sequential number starting at 1.

Example:

&gt; S DUMMY="P"

&gt; D WARDLOC^GMVGETD(.RESULT,DUMMY) ZW RESULT

&gt; RESULT="^TMP(540221719,"GWARD")"

&gt; D ^%G

&gt; Global ^TMP($J,"GWARD"

&gt; ^TMP(540221719,"GWARD",1)=2^1AS^2

2)=1^2-AS^1

3)=13^2-ASM^67

4)=25^214-2 DOM^149

5)=3^3AS^128

6)=4^4AS-1^4

7)=22^4B^153

8)=23^4C^155

9)=24^4D^154

10)=12^5NM^63

11)=6^6AS^10

12)=7^7AS^11

13)=8^DOM^23

14)=10^MICU^36

15)=5^NHCU^5

NAME: **GMV WARD PT** TAG: WARDPT

ROUTINE: GMVGETD                      RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: RESTRICTED              INACTIVE: ACTIVE

WORD WRAP ON: TRUE

DESCRIPTION:

This procedure lists patients registered on a particular MAS ward.

INPUT PARAMETER: GMRWARD                PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 30               REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

GMRWARD contains the name of ward from Ward Location file (#42).

RETURN PARAMETER DESCRIPTION:

Returns the name of the global array containing the list of patients on

the selected ward (i.e., ^TMP($J,"GMRPT")).

^TMP($J,"GMRPT",n)=DFN^Name^SSN (w/hyphens)^DOB^Sex and Age^Attending^

Veteran^Date of Death (internal)^Date of Death

(external)^Ward name^Roombed

n is a sequential number starting at 1.

If there are no patients on the ward, then the global array is undefined.

NAME: **GMV WARD/ROOM PATIENTS** TAG: ROOMPT

ROUTINE: GMVUTL7                      RETURN VALUE TYPE: ARRAY

AVAILABILITY: RESTRICTED              INACTIVE: ACTIVE

DESCRIPTION:

Returns a list of patients in the ward and rooms specified.

INPUT PARAMETER: GMVWRD                 PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 60               REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

Name of the ward (e.g., 2EAST).

INPUT PARAMETER: GMVRLST                PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 150              REQUIRED: YES

SEQUENCE NUMBER: 2

DESCRIPTION:

The room numbers of the ward separated by comma (e.g., 200,210,220).

RETURN PARAMETER DESCRIPTION:

RESULT(n)=patient name^DFN^DOB (external)^SSN (no hyphens)

where n is a sequential number beginning with 0 (zero)

### Menu Option by Name

NAME: GMV V/M GUI

MENU TEXT: Vitals/Measurements GUI Application

TYPE: Broker (Client/Server)

PACKAGE: GEN. MED. REC. - VITALS

DESCRIPTION:   This option controls access to the GUI Vitals/Measurements

application.

RPC: GMV MANAGER

RPC: GMV ADD VM

RPC: GMV ALLERGY

RPC: GMV CLINIC PT

RPC: GMV CONVERT DATE

RPC: GMV CUMULATIVE REPORT

RPC: GMV ENTERED IN ERROR-PATIENT

RPC: GMV EXTRACT REC

RPC: GMV GET CURRENT TIME

RPC: GMV LATEST VITALS BY LOCATION

RPC: GMV LATEST VITALS FOR PATIENT

RPC: GMV LATEST VM

RPC: GMV MARK ERROR

RPC: GMV PT GRAPH

RPC: GMV PTSELECT

RPC: GMV QUALIFIER TABLE

RPC: GMV ROOM/BED

RPC: GMV TEAM PATIENTS

RPC: GMV V/M ALLDATA

RPC: GMV VITALS/CAT/QUAL

RPC: GMV WARD LOCATION

RPC: GMV WARD PT

RPC: GMV WARD/ROOM PATIENTS

RPC: GMV USER

RPC: GMV NUR UNIT PT

RPC: GMV CHECK DEVICE

RPC: GMV PARAMETER

RPC: ORWPT PTINQ

RPC: GMV GET CATEGORY IEN

RPC: GMV GET VITAL TYPE IEN

RPC: VAFCTFU CONVERT DFN TO ICN

RPC: VAFCTFU CONVERT ICN TO DFN

RPC: GMV DLL VERSION

RPC: GMV LOCATION SELECT

RPC: GMV CLOSEST

UPPERCASE MENU TEXT: VITALS/MEASUREMENTS GUI APPLIC

## 6 Archiving and Purging

No provisions for archiving or purging have been made for this release and none are planned for

the future.

This page intentionally left blank for double-side printing.

## 7 Callable Routines

There are no callable routines.

This page intentionally left blank for double-side printing.

## 8 External Relations

1.	The following  applications must reside in the system before Vitals/Measurements, Version 5.0 can be installed:

a.	VA FileMan V. 22 or greater,

b.	Kernel V. 8.0 or greater,

c.	Kernel Toolkit V. 7.3 or greater,

d.	Kernel RPC Broker V. 1.1 or greater,

e.	PIMS V. 5.3 or greater,

f.	Intake and Output V. 4.0,

g	Health Summary V. 2.7 or greater,

h.	Nursing V. 4.0 or greater.

2.	Interface Control Registrations (formerly known as Integration Agreements) between the Vitals/Measurements software and other  applications exist.  Database Interface Control Registrations (DICR) are available on the DBA menu on Forum.  For complete information regarding the DICRs for Vitals V. 5.0, please refer to the *Integration Control Registrations (Agreements) Menu* [DBA IA ISC] option under the *DBA* [DBA] option on FORUM.

The following screen capture shows one way to access the DBA option in FORUM:

Select Software Services Primary Menu Option:  DBA MENU

NAME   NAMESPACE AND FILESPACE REGISTRATIONS ...

IAs    INTEGRATION CONTROL REGISTRATIONS ...

PKG    PACKAGE FILE INFORMATION ...

STN    INSTITUTION FILE INFORMATION ...

STND   STANDARDS ...

Select DBA MENU Option: IAS  INTEGRATION CONTROL REGISTRATIONS

HELP   Instructions for Entering ICRs

GET#   GET NEW Integration Control Registration #(s)

ADD    ADD/EDIT Pending Integration Control Registration

ROLL   Roll up ICR into Mail Message

FILE   File-type Integration Control Registrations Menu ...

ROU    Routine-type ICRs Menu ...

RPC    Remote Procedure Call-type ICRs Menu ...

OTH    Print 'Other'-type ICRs

SUPP   Supported References Menu ...

CONT   Controlled Subscription ICRs Menu ...

PRIV   Private ICRs Menu ...

CUST   Custodial Package Menu ...

INQ    Inquire to an Integration Control Registration

SUBS   Subscriber Package Menu ...

APIS   Supported API Report

VBLE   Lookup ICRs by Variable

PEND   Print ICRs in Pending Status

ACTV   Print Active ICRs

ALL    Print ALL ICRs

Select INTEGRATION CONTROL REGISTRATIONS Option: CUST  Custodial Package Menu

1      ACTIVE ICRs by Custodial Package

2      Print ALL ICRs by Custodial Package

3      Supported References Print All

Select Custodial Package Menu Option: 1  ACTIVE ICRs by Custodial Package

Select PACKAGE NAME: GMRV  GEN. MED. REC. - VITALS     GMRV     National

DEVICE: HOME//

## 9 Internal Relations

The namespace used for version 5 is GMV.

NAME: GMV V/M GUI

MENU TEXT: Vitals/Measurements GUI Application

TYPE: Broker (Client/Server)

PACKAGE: GEN. MED. REC. - VITALS

DESCRIPTION:   This option controls access to the GUI Vitals/Measurements

application.

RPC: GMV MANAGER

RPC: GMV ADD VM

RPC: GMV ALLERGY

RPC: GMV CLINIC PT

RPC: GMV CONVERT DATE

RPC: GMV CUMULATIVE REPORT

RPC: GMV ENTERED IN ERROR-PATIENT

RPC: GMV EXTRACT REC

RPC: GMV GET CURRENT TIME

RPC: GMV LATEST VITALS BY LOCATION

RPC: GMV LATEST VITALS FOR PATIENT

RPC: GMV LATEST VM

RPC: GMV MARK ERROR

RPC: GMV PT GRAPH

RPC: GMV PTSELECT

RPC: GMV QUALIFIER TABLE

RPC: GMV ROOM/BED

RPC: GMV TEAM PATIENTS

RPC: GMV V/M ALLDATA

RPC: GMV VITALS/CAT/QUAL

RPC: GMV WARD LOCATION

RPC: GMV WARD PT

RPC: GMV WARD/ROOM PATIENTS

RPC: GMV USER

RPC: GMV NUR UNIT PT

RPC: GMV CHECK DEVICE

RPC: GMV PARAMETER

RPC: ORWPT PTINQ

RPC: GMV GET CATEGORY IEN

RPC: GMV GET VITAL TYPE IEN

RPC: VAFCTFU CONVERT DFN TO ICN

RPC: VAFCTFU CONVERT ICN TO DFN

RPC: GMV DLL VERSION

RPC: GMV LOCATION SELECT

RPC: GMV CLOSEST

UPPERCASE MENU TEXT: VITALS/MEASUREMENTS GUI APPLIC

This page intentionally left blank for double-side printing.

## 10 Package-wide Variables

No package-wide variables are used in this application.

This page intentionally left blank for double-side printing.

## 11 SAC Exemptions

There is one SAC Exemption associated with this package.

VITALS/MEASUREMENTS

1	STANDARD SECTION:     1		ANSI

DATE GRANTED:     JAN 25, 1996

Vitals/Measurements has been granted a SAC exemption to use the 1995 VA SAC #4.4.2.1 to use $TEXT on a line that doesn’t contain ;; to check for the existence of a routine.

This page intentionally left blank for double-side printing.

## 12 Software Product Security

### Security Management

No additional security measures are to be applied.  Vitals/Measurements uses the standard RPC broker log-in procedure to validate the user and allow access to the system.

No additional licenses are necessary to run the software.

Confidentiality of staff and patient data and the monitoring of this confidentiality is no different than with any other paper reference.

### Security Features

a.	Mail groups and alerts.

There are no mail groups or alerts associated with this software.

b.	Remote systems.

Application data is transmitted to the Health Data Repository (HDR).

c.	Archiving/Purging.

Refer to the chapter on Archiving and Purging, in this manual.

d.	Contingency Planning.

It is the responsibility of the using service to develop a local contingency plan to be used in the event of application problems.

e.	Interfacing.

No specialized (non VA) interfaces are used or required by the application.

f.	Electronic signatures.

Electronic signatures are not used by the application.

g.	Menus.

There are no options of special note for the Information Security Officers (ISO's) to view.

h.	Security Keys.

There is one security key in this application, it is GMV MANAGER.  This new key allows a user to view/create/edit all other user’s templates in the Vitals module, without this key the user can only view/create/edit his/her own user templates.  This key also allows a user to use (run) other user’s templates in the Vitals application.  This key is required to access the Vitals Manager module.  This key should be assigned to the package coordinator.

i.	File Security.

WR     LAY  AUD

NUMBER  NAME                     GLOBAL NAME     ACC  ACC  ACC  ACC  ACC  ACC

------------------------------------------------------------------------------

120.5   GMRV VITAL MEASUREMENT   ^GMR(120.5,     @         @    @    @

120.51  GMRV VITAL TYPE          ^GMRD(120.51,   @         @    @    @    @

120.52  GMRV VITAL QUALIFIER     ^GMRD(120.52,   @         @    @    @    @

120.53  GMRV VITAL CATEGORY      ^GMRD(120.53,   @         @    @    @    @

120.57  GMRV VITALS PARAMETERS   ^GMRD(120.57,   @         @    @    @

j.	References.

There are no special reference materials for this package.

k.	Official Policies.

There are no special official policies for this package.

## 13 Glossary

Access Code   A unique sequence of characters known by and assigned only to the user, the system manager and/or designated alternate(s).  The access code (in conjunction with the verify code) is used by the computer to identify authorized users.

ADP Coordinator/ADPAC/Application Coordinator   Automated Data Processing Application Coordinator.  The person responsible for implementing a set of computer programs (application package) developed to support a specific functional area such as Nursing, PIMS, etc.

Application   A system of computer programs and files that have been specifically developed to meet the requirements of a user or group of users.  Examples of  applications are the PIMS and Vitals/Measurements application.

Archive   The process of moving data to some other storage medium, usually a magnetic disk, and deleting the information from active storage in order to free-up disk space on the system.

Backup Procedures   The provisions made for the recovery of data files and program libraries and for restart or replacement of ADP equipment after the occurrence of a system failure.

BMI   This is the patient's body mass index, which is calculated by dividing the person's weight in kilograms by the square of his height in meters.

Bulletin   A canned message that is automatically sent by MailMan to a user when something happens to the database.

Contingency Plan   A plan which assigns responsibility and defines procedures for use of the backup/restart/recovery and emergency preparedness procedures selected for the computer system based on risk analysis for that system.

Data Dictionary   A description of file structure and data elements within a file.

Device   A hardware input/output component of a computer system (e.g., CRT, printer).

Edit   Used to change/modify data typically stored in a file.

Field   A data element in a file.

File   The M construct in which data is stored for retrieval at a later time.  A group of related records.

File Manager or FileMan   Within this manual, FileManager or FileMan is a reference to VA FileMan.  FileMan is a set of M routines used to enter, edit, print, and sort/ search related data in a file; a data base.

Global   An M term used when referring to a file stored on a storage medium, usually a magnetic disk.  In the Vitals software, for example, vitals data is stored in one global, and patient data is stored in another global.

GMRV   This signifies the General Medical Record namespace assigned to the Vitals/Measurements application.

GMRY   This signifies the General Medical Record namespace assigned to the Intake and Output application.

GMV   Vitals/Measurements namespace, parent package to GMRV.

GUI   Graphical User Interface - a Windows-like screen that uses pull-down menus, icons, pointer devices, and other metaphor-type elements that can make a computer program more understandable, easier to use, allow multi-processing (more than one window or process available at once), etc.

I&amp;O   The Intake and Output application.

IRMS   Information Resource Management Service.

Kernel   A set of software utilities.  These utilities provide data processing support for the application packages developed within the VA.  They are also tools used in configuring the local computer site to meet the particular needs of the hospital.  The components of this operating system include: MenuMan, TaskMan, Device Handler, Log-on/Security, and other specialized routines.

LAYGO   An acronym for Learn As You Go.  A technique used by VA FileMan to acquire new information as it goes about its normal procedure.  It permits a user to add new data to a file.

M   Formerly known as MUMPS or the  () Utility Multi-Programming System.  This is the programming language used to write all  applications.

MailMan   An electronic mail, teleconferencing, and networking system.

Menu   A set of options or functions available to users for editing, formatting, generating reports, etc.

Module   A component of the Vitals software application that covers a single topic or a small section of a broad topic.

Namespace   A naming convention followed in the VA to identify various applications and to avoid collision between applications.  It is used as a prefix for all routines and globals used by the application.  The Vitals package uses GMV as its namespace.

OIFO   Office of Information Field Office, formerly known as Information Resource Management Field Office, and .

Option   A functionality that is invoked by the user.  The information defined in the option is used to drive the menu system.  Options are created, associated with others on menus, or given entry/exit actions.  For example, the GMV V/M GUI is the main menu for the Vitals/Measurements application.

Package   Otherwise known as an application.  A set of M routines, files, documentation and installation procedures that support a specific function within  (e.g., the ADT and Vitals/Measurements applications).

Password   A protected word or string of characters that identifies or authenticates a user, a specific resource, or an access type (synonymous with Verify Code).

PIMS   Patient Information Management System previously known as the MAS Package.

Pointer   A special data type of VA FileMan that takes its value from another file.  This is a method of joining files together and avoiding duplication of information.

Program   A set of M commands and arguments, created, stored, and retrieved as a single unit in M.

Protocol   A single entry point referencing multiple routine entry points to execute several inter related, required processes which perform specific functions.  When multiple protocols are associated with a single procedure (i.e., intravenous lines or IV lines), they are found grouped under a single option.

Qualifier   A word that gives a more detailed description of an item.

Queuing   The scheduling of a process/task to occur at a later time.  Queuing is normally done if a task uses up a lot of computer resources.

&lt;RET&gt;   Carriage return.

Routine   A set of M commands and arguments, created, stored, and retrieved as a single unit in M.

Security Key   A function which unlocks specific options and makes them accessible to an authorized user.

Sensitive Information   Any information which requires a degree of protection and which should be made available only to authorized users.

Site Configurable   A term used to refer to features in the system that can be modified to meet the needs of each site.

Software   A generic term referring to a related set of computer programs.

Synonym   A qualifier abbreviation appended to vitals/measurements numeric values on graphic reports.

Task Manager or TaskMan   A part of Kernel which allows programs or functions to begin at specified times or when devices become available.  See Queuing.

User   A person who enters and/or retrieves data in a system, usually utilizing a CRT.

Utility   An M program that assists in the development and/or maintenance of a computer system.

Verify Code   A unique security code which serves as a second level of security access.  Use of this code is site specific; sometimes used interchangeably with a password.

Veterans Health Information Systems and Technology Architecture.

Vital Type   A category of vital sign or measurement (e.g., pulse, respiration, blood pressure, temperature).

Workstation   A personal computer running the Windows 9x or NT operating system.

## 14 Appendix A – Parameter Settings

This table contains a list of parameter settings used by the Vitals/Measurement Standalone and Vitals Lite Graphical User Interfaces (GUIs).

**Note:** The GUIs use these parameter settings to start the software. When a GUI is open and the user changes the settings (e.g., checks a checkbox) that change works immediately in the GUI, but the parameter setting is not saved to the server until the user exits the GUI. If you are trying to debug a problem and have a GUI and a Mumps session open with the parameter settings showing at the same time, you will not see the parameter settings change until you close the GUI.

**How can you see these parameter settings on the server?**

Example:

&gt; **D ^XPAREDIT**

--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: **GMV&lt;return&gt;**

1   GMV ALLOW USER TEMPLATES     Allow individual user templates

2   GMV DEFAULT VALUES     ENTER GMV DEFAULTS

3   GMV DLL VERSION     Vitals DLL version check

4   GMV GUI VERSION     Active Vitals Measurements executables

5   GMV TEMPLATE     Templates for vitals V5

Press &lt;RETURN&gt; to see more, '^' to exit this list, OR

CHOOSE 1-5: **&lt;return&gt;**

6   GMV TEMPLATE DEFAULT     Default Templates for vitals V5

7   GMV USER DEFAULTS     GMV User Defaults

8   GMV WEBLINK     Vitals Measurments Home Page

CHOOSE 1-8: 7

Select NEW PERSON NAME: **LASTNAME,FIRST &lt;return&gt;**

------------- Setting GMV USER DEFAULTS  for User: LASTNAME,FIRST -------------

Select Parameter setting **: ?&lt;return&gt;**

Parameter setting                     Value

-----------------                     -----

ABNORMALBGCOLOR                       15

ABNORMALBOLD                          OFF

ABNORMALQUALIFIERS                    ON

ABNORMALTEXTCOLOR                     9

CLINIC\_INDEX                          9

CPRSMetricStyle                       CPRSMetricStyle

CanvasAbnormal                        15;9;0;1;15

CanvasNormal                          15;0;0;1;15;15388544;15388544;ORWPT PTINQ

CloseInputWindowAfterSave             DoNotCloseInputWindow

ConversionWarningStatus               OFF

DefaultTemplate                       547;VA(200,|full list

GRAPH OPTIONS VISIBLE                 0

GRAPHCOLOR                            16777215

GRAPHOPTIONS                          OFF

GRAPHOPTIONS-1                        OFF

GRAPHOPTIONS-2                        OFF

GRAPHOPTIONS-3                        OFF

GRAPHOPTIONS-4                        ON

GRAPH\_INDEX                           3

Enter RETURN to continue or '^' to exit:

| **Parameter Name**    | **Example**                               | **Explanation**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------------|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ABNORMALBGCOLOR       | 15                                        | A number that represents the data grid background color for abnormal values. There are 16 colors to choose from.  0 - Black  1 - Maroon  2 - Green  3 - Olive  4 - Navy  5 - Purple  6 - Teal  7 - Gray  8 - Silver  9 - Red  10 - Lime  11 - Yellow  12 - Blue  13 - Fuchsia  14 - Aqua  15 – White                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ABNORMALBOLD          | ON or OFF                                 | ON means the abnormal values appear in bold font. OFF means the abnormal values appear in regular font.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ABNORMALQUALIFIERS    | ON or OFF                                 | ON means the qualifiers are shown on the data grid for abnormal values. OFF means they are not shown for abnormal values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ABNORMALTEXTCOLOR     | 0 through 15                              | The number that represents the text color for abnormal values shown in the data grid. (See the list above.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
<!-- rpc-table -->
| CLINIC_INDEX          | 1                                         | An RPC returns an array with the list of clinics to select from. This number indicates the array node of the clinic selected. It is “-1” if no clinic was ever selected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| CPRSMetricStyle       | CPRSMetricStyle or VitalsMetricStyle      | When the “Units as Drop Down List” checkbox in the “Enter Vitals” window is checked this value is “CPRSMetricStyle”. If it is not checked the value is “VitalsMetricStyle”.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| CanvasAbnormal        | 15;9;0;1;15                               | User preferences for abnormal values. Set from File &#124; User Options &#124; Values Display tab.  1  st  value (e.g., 15) - Color of the background. Same as ABNORMALBGCOLOR.  2  nd  value (e.g., 9) - Color of the text. Same as ABNORMALTEXTCOLOR.  3  rd  value (e.g., 0) - Show text in bold font. Same as ABNORMALBOLD.  4  th  value (e.g., 1) - Show qualifiers. Same as ABNORMAL QUALIFIERS.  5  th  value (e.g. 15) - Background color for today’s values. Not currently used. User cannot set this value.                                                                                                                                                                                                                                                                            |
<!-- rpc-table -->
| CanvasNormal          | 15;0;0;1;15;15388544;15388544;ORWPT PTINQ | User preferences for normal values. Set from File &#124; User Options &#124; Values Display tab.  1  st  value (e.g., 15) - Color of the background. Same as NORMALBGCOLOR.  2  nd  value (e.g., 0) - Color of the text. Same as NORMALTEXTCOLOR.  3  rd  value (e.g., 0) - Show text in bold font. Same as NORMALBOLD.  4  th  value (e.g., 1) - Show qualifiers. Same as NORMALQUALIFIERS.  5  th  value (e.g., 15) - Background color for today’s values. Not currently used. User cannot set this value.  The following values are set by the software. The user cannot change them. These values control the File &#124; Patient Inquiry display.  6  th  value (e.g., 15388544) – Background color  7  th  value (e.g., 15388544) – Text color  8  th  value (e.g., ORWPT PTINQ) – RPC Name |
| DefaultTemplate       | 547;VA(200,&#124;full list                | The input template selected by the user. In this example, the template belongs to user 547 in the NEW PERSON file (#200). The template name is “full list”.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| GRAPH OPTIONS VISIBLE | 0 or 1                                    | 1 means the “Values”, “Time Scale”, “3D” and “Allow Zoom” checkboxes are visible. 0 means they are hidden. This parameter is set from the Vitals Lite GUI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| GRAPHCOLOR            | 16777215                                  | The code for the background color for the data graph. There are too many colors to list.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| GRAPHOPTIONS          | ON or OFF                                 | The “Show/Hide Graph Option” controls a panel that contains the “Values”, “3D”, “Allow Zoom” and “Time Scale” checkboxes. ON means the panel will be displayed to the user. OFF means it will be hidden from view.  Same as  the GRAPH OPTIONS VISIBLE parameter but is set from the Vitals Standalone GUI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| GRAPHOPTIONS-1        | ON or OFF                                 | ON means the “Values” checkbox has a checkmark. OFF means it is blank.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| GRAPHOPTIONS-2        | ON or OFF                                 | ON means the “3D” checkbox has a checkmark. OFF means it is blank.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| GRAPHOPTIONS-3        | ON or OFF                                 | ON means the “Allow Zoom” checkbox has a checkmark. OFF means it is blank.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| GRAPHOPTIONS-4        | ON or OFF                                 | ON means the “Time Scale” checkbox has a checkmark. OFF means it is blank.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| GRAPH_INDEX           | 0                                         | A number to indicate the vital type(s) that appear on the data graph.  0 – Temperature  1 – Pulse  2 – Respiration  3 – B/P  4 – Pulse Ox  5 – Height  6 – Weight  7 – BMI  8 - Pain  9 – Height/Weight  10 - TPR  11 – B/P - Weight  12 – C/G  13 – CVP  14 – Intake  15 – Output                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| GRIDSIZE              | 212                                       | Width in pixels of the data grid.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| GridDateRange         | 12                                        | selection. Default value is 12 (Two Years).  0 – Today  1 – T-1  2 – T-2  3 – T-3  4 – T-4  5 – T-5  6 – T-6  7 – T-7  8 – T-8  9 – T-9  10 – Six Months  11 – One Year  12 – Two Years  13 – All Results  14 –                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| LastVitalsListHeight  | 130                                       | Height in pixels of the “Latest vitals on file for this patient” portion of the “Enter Vitals’ window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| NORMALBGCOLOR         | 0 through 15                              | The background color for the normal values in the data grid. (See the list above.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| NORMALBOLD            | ON or OFF                                 | ON means the normal values appear in the bold font. OFF means the normal values appear in regular font.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| NORMALQUALIFIERS      | ON or OFF                                 | ON means the qualifiers are shown on the data grid for normal values. OFF means they are not shown for normal values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| NORMALTEXTCOLOR       | 0 through 15                              | The number that represents the text color for normal values shown in the data grid. (See the list above.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| OneUnavailalbeBox     |                                           | Not currently used. May be used in the future.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ParamTreeWidth        | 211                                       | Width in pixels of the “Templates” portion of the “Enter Vitals” window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| RefuseStatus          | ON or OFF                                 | ON means the “Enable R” checkbox in “Enter Vitals” window is checked. OFF means it is not checked.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| SELECTOR_TAB          | 4                                         | A number that indicates which patient selector tab is selected.  0 – Unit  1 – Ward  2 – Team  3 – Clinic  4 – All                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| SearchDelay           | 1.0                                       | Indicates the number of seconds the software will wait before trying to automatically look up a patient name using the characters entered by the user. Set by the user in:  File &#124; User Options &#124; Search Delay tab.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ShowLastVitals        | ShowLastVitals or NoLatest Vitals         | Show or hide the values for the “Latest vitals on file for this patient” portion of the “Enter Vitals” window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ShowTemplates         | ShowTemplates or NoTemplates              | “ShowTemplates” means that the “Template” list in the “Enter Vitals” window is shown. “NoTemplates” means it is hidden.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
<!-- rpc-table -->
| TEAM_INDEX            | -1                                        | An RPC returns an array with the list of teams to select from. This number indicates the array node of the team selected. It is “-1” if no team was ever selected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| TfrmGMV_InputLite     | 800;600;-4;-4;808;574;0                   | Parameters of the Vitals Standalone (EXE) window.  1  st  value (e.g., 800)  – User’s Windows  screen resolution (width)  2  nd  value (e.g., 600) – User’s Windows screen resolution (height)  3  rd  value (e.g., -4) – Position of the left side of the window  4  th  value (e.g., -4) – Position of the top side of the window  5  th  value (e.g., 808) – Width in pixels of the window  6  th  value (e.g., 574) – Height in pixels of the window  7  th  value (e.g., 0) – Not currently used. Cannot be set by the user.                                                                                                                                                                                                                                                                 |
<!-- rpc-table -->
| UNIT_INDEX            | 7                                         | An RPC returns an array with the list of (nursing) units to select from. This number indicates the array node of the unit selected. It is “-1” if no unit was ever selected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| UnavailableStatus     | ON or OFF                                 | ON means the “Enable U” checkbox in “Enter Vitals” window is checked. OFF means it is not checked.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| VIEW-HEIGHT           | 566                                       | The height in pixels for the Vitals Lite (DLL) View window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| VIEW-LEFT             | 59                                        | The pixel location for the left side of the Vitals Lite (DLL).View window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| VIEW-TOP              | 0                                         | The pixel location for the top of the Vitals Lite (DLL) View window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| VIEW-WIDTH            | 741                                       | The width in pixels for the Viitals Lite (DLL) View window.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| VitalsLite            | 800;600;0;0;800;566;0                     | Parameters of the Vitals Lite (DLL) window.  1  st  value (e.g., 800)  – User’s Windows  screen resolution (width)  2  nd  value (e.g., 600) – User’s Windows screen resolution (height)  3  rd  value (e.g., 0) – Position of the left side of the window  4  th  value (e.g., 0) – Position of the top side of the window  5  th  value (e.g., 800) – Width in pixels of the window  6  th  value (e.g., 566) – Height in pixels of the window  7  th  value (e.g., 0) – Not currently used. Cannot be set by the user.                                                                                                                                                                                                                                                                         |
<!-- rpc-table -->
| WARD_INDEX            | 6                                         | An RPC returns an array with the list of wards to select from. This number indicates the array node of the ward selected. It is “-1” if no ward was ever selected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |