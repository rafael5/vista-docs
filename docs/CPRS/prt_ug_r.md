---
app_name: Computerized Patient Record System (CPRS)
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
package_id: CPRS
patch: null
patch_gap: null
section: ''
source_file: prt_ug_r.docx
status: draft
title: CPRS Provider Role Tool (PRT)
---

# CPRS Provider Role Tool (PRT)

# User Guide: GUI Version

# V1.0

<!-- image -->

July 2021


Revision History

NOTE: The revision history cycle begins once changes or enhancements are requested after the document has been baselined.

| Date      |   Revision | Description                                                                                                                                       | Author                |
|-----------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| 7/28/2021 |       0.04 | OR*3.0*453: Redacted the manual for the VA Document Library (VDL).  Removed names in revision history, port numbers and links to software builds. | CPRS Development Team |
| 3/4/2021  |       0.03 | OR*3.0*453: updated the Preparing for a Provider Role Change, Move Patient Orders to a New Provider sections                                      | REDACTED              |
| 7/6/2020  |       0.02 | Patch OR*3.0*453: revisions                                                                                                                       | REDACTED              |
| May 2020  |       0.01 | Revising per dev review                                                                                                                           | REDACTED              |

**Artifact Rationale**

Per the Veteran-focused Integrated Process (VIP) Guide, the User’s Guide is required to be completed prior to Critical Decision Point #2 (CD2), with the expectation that it will be updated as needed. A User Guide is a technical communication document intended to give assistance to people using a particular system, such as VistA end users. It is usually written by a technical writer, although it can also be written by programmers, product or project managers, or other technical staff. Most user guides contain both a written guide and the associated images. In the case of computer applications, it is usual to include screenshots of the human-machine interfaces, and hardware manuals often include clear, simplified diagrams. The language used is matched to the intended audience, with jargon kept to a minimum or explained thoroughly. The User Guide is a mandatory, build-level document, and should be updated to reflect the contents of the most recently deployed build. The sections documented herein are required if applicable to your product.

**Table of Contents**

1.	Introduction	1

1.1.	Purpose	1

1.1.1.	Assumptions	1

1.1.2.	Coordination	2

1.1.3.	Disclaimers	2

1.1.3.1.	Software Disclaimer	2

1.1.3.2.	Documentation Disclaimer	2

1.1.4.	Documentation Conventions	2

1.1.5.	References and Resources	3

1.1.5.1.	VA Document Library	3

1.1.5.2.	Online Help	3

1.2.	National Service Desk and Organizational Contacts	3

2.	System Summary	4

2.1.	System Configuration	4

2.2.	Data Flows	5

2.3.	User Access Levels	5

2.4.	Continuity of Operation	5

3.	Getting Started	6

3.1.	Logging On	6

3.2.	System Menu	6

3.2.1.	Logging in to the Stand-alone PRT through Two-Factor Authentication	6

3.2.2.	Logging in to the Stand-Alone PRT without Two-Factor Authentication	8

3.2.3.	Logging into PRT through the CPRS GUI	8

3.3.	Changing User ID and Password	9

3.4.	Exit System	9

3.5.	Caveats and Exceptions	9

4.	Using the Software	9

4.1.	Preparing for a Provider Role Change	9

4.2.	Viewing the PRT Main Window	10

4.2.1.	Window Layout	10

4.2.2.	Buttons &amp; Menu Items	14

4.3.	How to Reassign Patient Orders	15

4.3.1.	Select a Current Provider and An Order Date Range	15

4.3.2.	Select a New Provider for Reassigned Orders	17

4.3.3.	Move Patient Orders to a New Provider	19

4.3.4.	Reassign Orders	20

4.4.	How to View a Patient’s Orders	23

4.5.	How to Create an Audit Report	24

5.	Troubleshooting	25

5.1.	Special Instructions for Error Correction	25

6.	Acronyms and Abbreviations	25

Table of Figures

Figure 1: Provider Role Tool server connection dialog	3

Figure 2: Data Flow between VistA and CPRS Workstation	5

Figure 3: Provider Role Tool Server Connection Dialog	6

Figure 4: Windows Security Dialog – VistA Logon Certificate Selection	7

Figure 5 – PIN dialog	7

Figure 7: VistA Sign-On dialog	8

Figure 8: Provider Role Tool Main Window	10

Figure 9: Left side of the Provider Role Tool Main Window	11

Figure 10: Right side of the Provider Role Tool Main Window	12

Figure 11: Center Portion of the Main Provider Role Tool Window	13

Figure 12: A typical Provider Role Tool session after the user has added a new provider	14

Figure 13: Choose Current Provider/Order Dates (highlighted in red for clarity)	16

Figure 14: Select Current Provider and Order Dates window (highlighted in yellow for clarity)	16

Figure 15: Add New Provider selected (highlighted in red for clarity)	17

Figure 16: Add New Provider (highlighted in yellow for clarity)	18

Figure 17: Reassign Signed Patient Orders window after a new provider has been added	18

Figure 18: Reassign Signed Patient Orders window after a patient and new provider have been selected	19

Figure 19: Reassign Signed Patient Orders window before “Apply Changes” has been clicked (highlighted in red for clarity)	20

Figure 20: Reassign Orders button, highlighted in red for clarity	21

Figure 21 – Transfer Completed window	21

Figure 22 – Copy Results to Clipboard	22

Figure 23: Notepad text report	23

Figure 24: Qualifying Orders for Patient(s)	24

Figure 25: Audit Report	25

## 1 Introduction

### Purpose

The purpose of this guide is to provide instructions on how to use the Provider Role Tool (PRT) application.

The Provider Role Tool enables authorized users to reassign future alerts for *qualifying patient orders* from a current provider to one or more new providers. It handles the cases where a provider changes roles while remaining at the same site (for example, a provider who moves from VA to DOD but does not relocate or a resident who rotates from one specialty service to another, i.e.: Oncology to Surgery). The goal is for the current provider to no longer receive notifications for orders written in the previous role, while being able to receive notifications for orders written in the new role. The purpose is to improve patient care by having alerts available to the provider now responsible for continuing that patient’s treatment or therapy.

One way to think of the Provider Role Tool is to consider it a more advanced version of the CPRS Surrogates feature. The Surrogates feature lets you redirect all notifications from one provider to another – useful when one provider is on vacation. Provider Role Tool redirects only selected notifications – those related to qualifying orders issued while the current provider was acting in a now-discontinued role or capacity at a given site.

The Provider Role Tool application swaps “qualifying” patient orders from an original provider to a substitute provider. The reassignment ensures that the original provider won’t receive any notifications associated with the orders in question, but that the substitute provider will receive them.  (A “qualifying” patient order is an open order issued by the original provider during a specified time period --by default, the last calendar year).

The Provider Role Tool implements VA New Service Request (NSR) 20130504. The program is independent from CPRS but works with CPRS GUI servers.

NSR 20130504 was written because of a provider who moved from VA to DOD while remaining at the same site. After the role change, the provider was no longer looking after VA patients, and was instead responsible for DOD patients. This role change put the facility into a difficult situation. If they assigned a surrogate for the original provider, that surrogate received order notifications for the original provider’s VA *and* DOD patients. If they did not assign a surrogate, the original provider continued to receive notifications for VA patients. They needed a solution that would let the original provider move on to new duties without receiving notifications for orders issued in the abandoned VA role.

#### Assumptions

**Users:** The Provider Role Tool will be used by personnel that sites designate to reassign responsibility from one provider to another. It is assumed that using Provider Role Tool will be an administrative function, perhaps performed by a Clinical Application Coordinator (CAC). The CAC can perform this function under the direction of clinical personnel who can speak to how qualifying orders will be reassigned to one or more different providers. However, it is up to sites to decide on the process to reassign orders.

**Accessibility:** The Provider Role Tool is fully compliant with Section 508 accessibility directives.

**Provider Role Tool GUI Interface:** The Provider Role Tool was built to run in the Microsoft Windows operating environment.

#### Coordination

To use the Provider Role Tool, sites will need to coordinate the installation and make sure the correct users are authorized to use the software.

For installation, sites need to coordinate their local resources with Information Technology Operations and Services (ITOPS) support. The site Computerized Patient Record System (CPRS) Coordinator may be involved in selecting which users will need to use Provider Role Tool. It is anticipated that CACs will use the Provider Role Tool to reassign orders to new providers.

#### Disclaimers

##### Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government during their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely if any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

##### Documentation Disclaimer

*The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.*

#### Documentation Conventions

This manual uses several methods to highlight different aspects of the material.

Descriptive text is presented in a proportional font (as represented by this font).

**Note:** Notes are used to call a user’s attention to an important matter or idea. It will be in bold.

**Warning:** This paragraph is a caution for users that if they do something, the result could be serious, including loss of data.

“Snapshots” of computer online displays (for example, character-based screen captures/dialogs) and computer source code are shown in a non-proportional font and enclosed within a box.

Select OPTION NAME: XPAR EDIT PARAMETER       Edit Parameter Values

Edit Parameter Values

Also included are Graphical User Interface (GUI) Microsoft Windows images (for example, dialogs or forms).

<!-- image -->

Figure 1: Provider Role Tool server connection dialog

#### References and Resources

##### VA Document Library

Provider Role Tool documentation is available on the VA Document Library (VDL): [http://www.va.gov/vdl](http://www.va.gov/vdl)

##### Online Help

Instructions, procedures, and other information are available from the Provider Role Tool online help file. You may access the help file by clicking **Help | Contents** from the menu bar or by pressing the F1 key while any Provider Role Tool dialog is open. Much of the information in this User Manual is also in the Provider Role Tool online help.

### National Service Desk and Organizational Contacts

| Name                                      | Role                       | Org   | Contact Info                                                                   |
|-------------------------------------------|----------------------------|-------|--------------------------------------------------------------------------------|
| CPRS Clinical Application Coordinator     | Tier 0 Support             | VHA   | Local Clinical App Coordinator information should be available from your site. |
| OI&T National Service Desk                | Tier 1 Support             | OI&T  | REDACTED                                                                       |
| Health Product Support                    | Tier 2 Support             | VHA   | REDACTED                                                                       |
| OI&T System Admin/Field Operation Support | Tier 2 & 3 support         | OI&T  | REDACTED                                                                       |
| VistA Patch Maintenance                   | Tier 3 Application Support | OI&T  | REDACTED                                                                       |

**Table 1: Tier Support Contact Information**

## 2 System Summary

The Provider Role Tool is a client-server GUI application that enables users to reassign existing orders to another provider.  This reassignment often happens because a provider is changing roles but is remaining at the same location.  For example, a reassignment would happen if a provider was working for the VA but took a position with a Department of Defense co-located site.  The provider would still be at a VA site but would no longer be responsible for VA patients.

The Provider Role Tool GUI is a front-end application that interacts with the VistA database using CPRS communication protocols.  It affects which users receive notifications.

To launch the Provider Role Tool, users will either select an item from the CPRS Tools menu or activate it from an icon.

Once logged in, the user can select the provider whose orders need to be changed and the date range for those orders. After selecting the provider, patients with orders from the selected provider display on the left side of the main PRT window.

### System Configuration

The Provider Role Tool runs on workstations that have CPRS installed on them. It communicates with servers that interact with the VistA database, as shown below.

<!-- image -->

Figure 2: Data Flow between VistA and CPRS Workstation

### Data Flows

See Figure 2 above.

### User Access Levels

Only users who have been assigned the OR PRT ACCESS key may use the Provider Role Tool application.

### Continuity of Operation

If the VistA database is functioning and can be accessed, Provider Role Tool should be available. The protection of data and other items are related to the VistA database, not PRT.

## 3 Getting Started

### Logging On

Users can launch Provider Role Tool directly from an icon or from the CPRS Tools menu. If the site chooses to use Provider Role Tool from the Tools menu, CACs or other support personnel will need to add the menu item to CPRS.

### System Menu

This section will give instructions on the ways that a user can access the Provider Role Tool.

#### Logging in to the Stand-alone PRT through Two-Factor Authentication

You can use your Personal Identification Verification (PIV) card and Personal Identification Number (PIN) to access PRT.

To login to the Provider Role Tool with your PIV card:

<!-- image -->

1. Double-click the PRT icon on your desktop. You will immediately see the Provider Role Tool Server Connection Dialog.

Figure 3: Provider Role Tool Server Connection Dialog

1. In the Windows Security dialog, select the certificate associated with your PIV card and click “OK”.
<!-- image -->

Figure 4: Windows Security Dialog – VistA Logon Certificate Selection

<!-- image -->

1. Enter your PIN and click “OK”.

Figure 5 – PIN dialog

1. On the System Use Notification window, click “OK”. **Note:** After you click “OK”, you will see the PRT main window and will not need to enter your Access and Verify Codes.

#### Logging in to the Stand-Alone PRT without Two-Factor Authentication

If you don’t have a PIV card, do the following:

1. Double-click the PRT icon on your desktop.
2. On the VistA Sign-On dialog, input your Access Code and your Verify Code and click “OK”.
<!-- image -->

Figure 6: VistA Sign-On dialog

#### Logging into PRT through the CPRS GUI

1. On the CPRS main menu, click “Tools”.
2. Click “Provider Role Tool”.

### Changing User ID and Password

Users will use the same credentials that they use to access VistA or CPRS. Whenever those credentials need to be renewed, the same credentials will be used for Provider Role Tool.

### Exit System

To exit the system, the user either selects the X in the upper right corner of the dialog or selects **File | Exit** on the menu bar.

### Caveats and Exceptions

N/A

## 4 Using the Software

### Preparing for a Provider Role Change

It’s important to properly research and prepare before attempting a provider role change. Remember that the Provider Role Tool, though it displays patient names, is reassigning *orders* , not patients. The purpose of the application is to ensure that new notifications for recently issued orders go to a newly designated provider(s).

To successfully implement a provider role change using the Provider Role Tool, you should answer these questions before attempting a transfer:

1. **Who is changing roles?** The management team identifies the provider changing roles.
2. **What patients have qualifying orders?** The management team identifies patients who will be affected by the role change. Provider Role Tool defines these patients as those who have qualifying orders issued by the provider changing roles during a specified time period.
3. **Who will receive order notifications for these qualifying orders?** The management team identifies the new provider(s) who will now manage the patients and orders formerly assigned to the departing provider.
4. **How far back are we going?** The management team also determines a time period covered by the transfer, such as “all orders from one year ago until today at midnight”.
5. **How will we allocate transfers between multiple new providers?** The management team specifies how patients/orders will be allocated between new providers. This could be simple, as in “evenly divide patients between these three new providers”. Or it could be complex, as in “find all the cardiac patients and assign them to provider X and find all the orthopedic patients and assign them to provider Y”.
6. **Are the designated new providers aware of this pending transfer?** It’s incumbent on the management team to get “buy-in” from the new providers that will suddenly be receiving order notifications for patients formerly managed by the previous provider.
7. **Are the designated new providers able to receive the appropriate order notifications?** You can’t transfer orders to a new provider who isn’t able to receive order notifications.
8. **Are you sure simple surrogacy is not sufficient?** Provider Role Tool is designed to serve the business case where a provider is changing roles *at the same site* . If the provider is retiring or leaving the site, other business processes are probably more appropriate.

The Provider Role Tool can optionally assist in discovering patients and orders for a departing provider. For example, a user can enter a departing provider and a date range, and “assign” them to a new provider. In the Qualifying Orders window, Provider Role Tool will present a detailed listing of qualified orders for each patient. The management team can use this listing when designating which patients/orders go to each newly designated provider.

### Viewing the PRT Main Window

#### Window Layout

After logging in, the user will see the Reassign Patient Orders window, which is the main window for the Provider Role Tool.

<!-- image -->

Figure 7: Provider Role Tool Main Window

The main Provider Role Tool window has three sections:

<!-- image -->

- **Left side** : Selects and displays a current provider and associated patients/orders associated with that provider and the chosen date range

**Figure 8: Left side of the Provider Role Tool Main Window**

- **Right side** : Selects and displays new providers and the patients/orders assigned to each.
<!-- image -->

Figure 9: Right side of the Provider Role Tool Main Window

<!-- image -->

- **Center** : Buttons to move patients between old and new providers:

Figure 10: Center Portion of the Main Provider Role Tool Window

The screen capture below shows a typical Provider Role Tool session in mid-progress. The user has already selected a current provider, added two new providers, and has transferred patients from the current provider to the new provider.  However, the changes have not been applied yet.

<!-- image -->

Figure 11: A typical Provider Role Tool session after the user has added a new provider

Additional features in the Provider Role Tool GUI:

- Most tables and lists have popup or context menus with additional actions. When in doubt, right click to see if a menu pops up.
- The main screen supports drag and drop. You can drag patients from left to right or between providers in the right panel.
- Some tables support double click. You can double click a patient to see associated orders.
- Most tables and lists support multiple selections using standard Windows techniques.

#### Buttons &amp; Menu Items

All buttons on the main window have corresponding menu commands in the “Edit” main menu. All buttons and menu items have shortcuts (command keys) that are displayed when the “ALT” key is pressed.

- **Choose Current Provider and Order Dates** : Displays a popup dialog (see additional help) in which the user can select the current provider from a list. The user can also modify the default selection period, which defaults to the past calendar year. Upon selection, the patients list at left screen will be populated with patients. The order count for each patient displays to the right of their names.
- **Add Selected** : Moves the *selected* current provider’s patients (at left screen) to the selected new provider (at right screen).
- **Add All** : Moves all current provider’s patients (at left screen) to the selected new provider (at right screen).
- **Undo Selected** : Removes all *selected* patients at right screen (new provider) and restores them at left screen (current provider). It also removes all selected new providers.
- **Undo All** : Removes all patients at right screen (new provider) and restores them at left screen (current provider). It also removes all new providers.

### How to Reassign Patient Orders

There are four phases in moving patient orders from a current provider to one or more new providers:

1. Select a Current Provider and an Order Date Range.
2. Select a New Provider for reassigned orders.
3. Move Patient Orders to the New Provider.
4. Reassign Orders.

#### Select a Current Provider and An Order Date Range

The first phase of reassigning patient orders is to select a current provider and an order date range:

1. On the **View** menu, select one of the following:
    1. All orders by patient.
    2. All orders by patient and transfer type.
    3. Individual orders by patient and transfer type.
2. Click the “Choose Current Provider/Order Dates” button on the main window or select **Edit | Choose Current Provider/Order Dates** on the menu.
<!-- image -->

**Figure 12: Choose Current Provider/Order Dates (highlighted in red for clarity)**

In the Select Current Provider and Order Dates dialog box, perform the following:

1. Select an “Orders Start Date” and an “Orders Stop Date”.  To set a new date, select the “Orders Start Date” or “Orders Stop Date” calendar and type a date.
2. Type the last name (or part of the last name) of a provider or click on a name in the drop-down.
3. If desired, check the “Include terminated providers that hold the PROVIDER key” checkbox.
4. Click “OK”.
<!-- image -->

**Figure 13: Select Current Provider and Order Dates window (highlighted in yellow for clarity)**

**Notes:** The default “Orders Start Date” is one year ago from today and the default “Orders Stop Date” is the current date.  
The “Orders Start Date” can be any date in the past, but the “Orders Stop Date” cannot be a future date.
The dialog box does a search by last name, not by first or middle name. You can only type the name of one provider.

**Warning:** Selecting a new provider and date range will erase any unapplied assignments you have made in the Provider Role Tool: Reassign Signed Patient Orders window.

#### Select a New Provider for Reassigned Orders

The second phase of reassigning patient orders is to select a new provider.

1. Click “Add New Provider” on the main window or select **Edit | Add New Provider** on the menu.
<!-- image -->

Figure 14: Add New Provider selected (highlighted in red for clarity)

In the Add New Provider dialog box, perform the following:

1. Type the last name (or part of the last name) of a provider or click on a name in the drop-down. You can select only one new provider at a time.
2. Click “OK”.
<!-- image -->

Figure 15: Add New Provider (highlighted in yellow for clarity)

1. To add multiple new providers, repeat the steps above as often as needed.
<!-- image -->

Note: After a new provider is added, the Reassign Signed Patient Orders window will look like this:

Figure 16: Reassign Signed Patient Orders window after a new provider has been added

#### Move Patient Orders to a New Provider

The third phase of reassigning patient orders is to move the patient orders to new providers and apply the changes.

1. In the Provider Role Tool: Reassign Signed Patient Orders window, do the following:
    1. Click on a new provider.
    2. Click on a patient name.
    <!-- image -->

**Figure 17: Reassign Signed Patient Orders window after a patient and new provider have been selected**

1. Click the “Add Selected” button on the main window or select **Edit | Add Selected** on the menu. **Note:** You can assign all patients to a new provider by clicking on the “Add All” button or selecting **Edit | Add All** .
2. Click the “Apply Changes” button on the main window or select **Edit | Apply Changes** on the menu.

<!-- image -->

Figure 18: Reassign Signed Patient Orders window before “Apply Changes” has been clicked (highlighted in red for clarity)

#### Reassign Orders

The fourth phase of reassigning patient orders is to complete the Reassign Orders dialog, which makes the changes permanent.

After the user has clicked the “Apply Changes” button, the Review Orders (Review and Execute) window will display.   Because this is an irreversible change, Provider Role Tool requires this deliberate review step. The Review and Execute window displays the orders that need to be reassigned, and the user must click the Reassign Orders button to complete the reassignment process.

**To complete the order reassignment:**

1. Accept the default “Effective Date” of today or change to a future date.  The “Effective Date” cannot be a past date.
<!-- image -->

Figure 19: Reassign Orders button, highlighted in red for clarity

1. Review the list of reassigned orders.

## Note: 	The review screen will likely have hundreds or possibly thousands of individual orders. The tool presents the list and requires another button click mainly as a “stop and pause” feature.

1. Click the “Reassign Orders” button to complete reassignment.
<!-- image -->
2. When the Transfer Completed window appears, click “OK”.

Figure 20 – Transfer Completed window

1. Review the results to see if any reassignments failed.
2. Optionally copy the reassignment results to the Windows clipboard by right-clicking on the Reassign Orders (Review and Execute) screen and clicking “Copy Results to Clipboard”.
<!-- image -->

Figure 21 – Copy Results to Clipboard

1. Return to the main window by clicking the “X” in the top right corner.

Below is a screen capture showing the text report pasted into Notepad.

<!-- image -->

Figure 22: Notepad text report

### How to View a Patient’s Orders

Once patients are listed in either pane of the main window, the user can bring up the Qualifying Orders for Patient(s) window and view the details about the orders.

A qualifying order has the following characteristics:

- It was issued by the selected provider.
- It was issued during the selected date range.
- It is a signed order.
- It is in a state identified as potentially generating a future notification.

The Qualifying Orders for Patient(s) window has three sections:

- Qualifying orders for the selected patient are listed on the left side of the window. Some orders may be in an expired or discontinued state, but these orders are still considered qualifying orders.
- The details about an order are shown on the right side of the window.
- The order transfer history is listed on the bottom right side of the window.

**To view a patient’s orders:**

1. Select a current or new provider on the Provider Role Tool: Reassign Signed Patient Orders window (the main window).

In the Qualifying Orders for Patient(s) window, perform one of the following tasks:

1. Double-click on a patient on either the left or right pane.
2. Right-click on a patient on either the left or right pane and then, click on “Show Orders for selected patient(s)”.

To view the details and transfer history of a patient’s order, left-click, right-click or press the shift key on a patient’s name.

Click the “Close” button to go back to the main window.

<!-- image -->

Figure 23: Qualifying Orders for Patient(s)

### How to Create an Audit Report

The audit report displays **all** order reassignments that occurred within a specific time period at the VistA site that you are affiliated with.

You will see order reassignments in **all** statuses for **all** patients transferred from and to **all** providers at your VistA site within a specified time period.

The audit report default Stop Date is the current date and the default Start Date is one year behind today’s date.

**To create an audit report:**

1. On the PRT Menu, select **View | Audit Report** .
2. On the Audit Report window, do the following:
    1. Select an “Audit Start Date” and an “Audit Stop Date”.  To set a new date, select the “Audit Start Date” or “Audit Stop Date” calendar and type a date.
    2. Click the “Build Report” button.
    3. To view details about an order, click on an order and then, click the “Show Orders” button.  You will then
    4. To view details about an order, click on the order and then, click the “Show Orders” button.  You will be taken to the Qualifying Orders for Patient(s) window.
    5. To go back to the main window, click the “Close” button.
    <!-- image -->

Figure 24: Audit Report

## 5 Troubleshooting

If the user receives an error stating they are not authorized to use Provider Role Tool, verify the user is assigned the OR PRT ACCESS key.

### Special Instructions for Error Correction

N/A

## 6 Acronyms and Abbreviations

| 2FA   | Two-Factor Authentication                                                                                 |
|-------|-----------------------------------------------------------------------------------------------------------|
| CAC   | Clinical Application Coordinator                                                                          |
| CD2   | Critical Decision Point #2                                                                                |
| CPRS  | Computerized Patient Record System.                                                                       |
| DOD   | Department of Defense                                                                                     |
| GUI   | Graphical User Interface                                                                                  |
| ITOPS | Information Technology Operations and Services (formerly known as Service Delivery and Engineering [SDE]) |
| MVI   | Master Veteran Index                                                                                      |
| NSR   | New Service Request                                                                                       |
| PIN   | Personal Identification Number                                                                            |
| PIV   | Personal Identification Verification                                                                      |
| PRT   | Provider Role Tool                                                                                        |
| SDE   | Service Delivery and Engineering                                                                          |
| VA    | Veterans Affairs                                                                                          |
| VDL   | VA Document Library                                                                                       |
| VIP   | Veteran-focused Integration Process                                                                       |
| VistA | Veterans Health Information Systems and Technology Architecture                                           |