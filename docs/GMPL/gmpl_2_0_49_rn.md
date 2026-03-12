---
app_name: 'CPRS: Problem List (GMPL)'
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
package_id: GMPL
patch: null
patch_gap: null
section: ''
source_file: gmpl_2_0_49_rn.docx
status: draft
title: gmpl 2 0 49 rn.docx
---

**Problem Selection List Enhancements (Patches GMPL*2.0*49 and OR*3.0*429)**

**Release Notes**

<!-- image -->

**December 2017**


Enterprise Program Management Office (EPMO)

Table of Contents

Table of Contents	2

Installation Requirements	3

Required Patches	3

Release Method	3

Known Issue	3

New Features	3

New Parameters	4

Installation Requirements

Required Patches

Below is a list of patches that you must verify are properly installed on your system before OR*3.0*434 can be installed:

GMPL*2.0*40

GMPL*2.0*45

OR*3.0*385

Please see the *Problem Selection List Enhancements (Patches OR*3.0*429 and GMPL*2.0*49) Deployment, Installation, Back-Out, and Rollback Guide* for further instructions.

Release Method

The Problem Selection List Enhancements will be released as part of a combined multi-package build under PROBLEM SELECTION LIST BUILD 1.0. This combined build consists of the GMPL*2.0*49 and OR*3.0*429 patches. The patches are expected to be installed on existing VistA platforms.

Known Issue

There are no known issues with Problem Selection List Enhancements.

New Features

Problem Selection List Enhancements include new features and changes include

Problem Selectin List file structure

A new parameter ORQQPL SELECTION LIST

The migration of existing lists if they are actively assigned

The installation of a new VA National Problem Selection List

<!-- image -->

A CAC, or appropriate person, can assign a Problem Selection List that will display on the left of the Problems tab. If a list is assigned, there will be a listing of categories and when the category is selected, the pane below displays the problems it contains.  This screen capture shows the VA-National Problem Selection List Content.

A new key GMPL IMPRT UTIL that will enable the users to import problem selection lists

updates to the Problem Selection List menu items

additions and updates to menu actions that assist in the creation and maintenance of selection lists

For users that only use CPRS, the only change they may see would be in the problem selection list they are assigned.

Users who work on problem list creation and assignments will see new menu options, including the ability to import problem selection lists for those who have been assigned the GMPL IMPRT UTIL key.

New Parameter

ORQQPL SELECTION LIST is a new parameter that will contain the problem selection list assignments. During the installation process, any existing problem selection lists that are actively assigned will be moved from where they are now stored to this new parameter.

When the patches are installed, the VA National Problem Selection List will be assigned at the Package level. Unless some other active assignment exists, all users and clinics will use the national list. If sites choose, they may make other assignments.

Assignments can be made at the following levels starting at the most general and going to the most specific: Package, System, Division, Location, and User. Package is only set by a nationally released patch. As with all parameters, the more specific level always takes priority over the more general assignment. So, if no other problem selection lists are assigned, all levels will inherit the Package level national list. However any assignment to a more specific level overrides the more general. So an assignment at Division or User overrides the Package level.