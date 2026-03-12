---
app_name: Laboratory (LA and LR)
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: null
doc_type: technical-manual
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-12'
is_base: false
is_change_pages: false
library_max_patch: null
package_id: LR
patch: null
patch_gap: null
section: ''
source_file: lab5_2sg.docx
status: draft
title: lab5 2sg.docx
---

Decentralized Hospital Computer Program

**LABORATORY**

**PACKAGE SECURITY GUIDE**

Version 5.2

October 1994

SENSITIVE INFORMATION

Information Systems Center

Dallas, Texas

Table Of Contents

Package Security	1

Laboratory Security Keys	2

Laboratory File Security	4

Accession/Load/Worklist Security	6

Individual Module Requirements/Concerns	7

Blood Bank	7

Anatomic Pathology	7

Microbiology	8

Chemistry/Immunology	8

Phlebotomy	8

## Package Security

The Laboratory System has interaction with almost all other Decentralized Hospital Computer Program (DHCP) packages. Because of this interaction, as well as the patient data maintained in the Laboratory files, security is a real and necessary concern.

Laboratory System security is maintained by use of Laboratory security keys, Laboratory file security, and proper menu assignments. This guide will discuss each element of security management and give guidelines for the assignment of access to the Laboratory System.

## Laboratory Security Keys

Each user of the Lab system must have the appropriate “keys” assigned to him before he can access the system. File #19.1 (SECURITY KEY) contains the key names, a short description, and a list of the holders. You will need to enter the users’ names under each of the appropriate key names. Following is a list of the Lab keys:

**NOTE:** It should be noted that these keys are used as locks for particular options, and are also checked elsewhere. Some routines check for user security keys.

**Key	Users**

LRANAT	Anatomic Pathology users*

LRAPSUPER	Anyone allowed to use the Anatomic Pathology Supervisor Menu and edit SNOMED codes

LRAU	Autopsy Module users*

LRBLOODBANK	Blood Bank users

LRBLSUPER	For Blood Bank supervisory level decisions

LRCY	Cytology Module users*

LREM	Electron Microscopy Module users*

LRLAB	Laboratory Personnel only

LRLIASON	Laboratory Application Coordinator

LRMICRO	Microbiology users

LRMIVERIFY	Microbiology personnel*

**Key	Users**

LRSP	Surgical Pathology Module users*

LRSUPER	Laboratory Supervisors

LRVERIFY	Anyone who is authorized to verify lab results

LRPHMAN	Phlebotomists*

LRPHSUPER	Supervisor of the phlebotomy collection team

Any combination of the security levels may be used, as deemed appropriate by the Laboratory.

* This key may be used to lock menu options, as the site deems appropriate.


## Laboratory File Security

**DD	READ	WRITE
FILE	ACCESS	ACCESS	ACCESS	DELETE	LAYGO**

60	@		l	@	l
61	@		l	@	l
61.1	@		l	@	l
61.2	@		l	@	l
61.3	@		l	@	l
61.4	@		l	@	l
61.5	@		l	@	l
61.6	@		l	@	l
62	@		l	@	l
62.05	@		l	l	l
62.06	@		l	l	l
62.07	@		@	@	@
62.1	@		l	@	l
62.2	@		l	l	l
62.3	@		l	l	l
62.4	@		l	l	l
62.5	@		l	l	l
62.55	@		l	l	l
62.6	@		l	l	l
63	@	l	l	l	l
63.9999	@	l	l	l	l
64	@		l	l	l
64.5	@		l	l	l
64.6	@	l	l	l	l
64.7	@	@	@	@	@

**DD	READ	WRITE
FILE	ACCESS	ACCESS	ACCESS	DELETE	LAYGO**

65	@		l	L	
65.4	@			L	L
65.5	@			l	
66	@			@	l
67	@			@	
67.1	@		l	@

67.2	@		l	@	
67.3	@		l	@	
67.9	@		l	l	l
68	@		l	l	l
68.2	@		l	l	l
68.4	@		l	l	l
69	@		@	@	
69.1	@		@	@	@
69.2	@		l	l	l
69.9	@		l	@	@
69.91	@	l	l	l	l


## Accession/Load/Worklist Security

Two additional fields have been added to the software package to allow other ancillary laboratories (not within Laboratory Service) to use this module for accessioning, verification, and reporting of their data:

1.	File #68 (Accession Area), field: User Access Authorization
This field points to File #19.1, Security Keys. If there is an entry in this field, only users having the security key for this accession area will be able to use the verification options for data entry or modification of data. This will not affect users’ ability to accession tests for the Accession Area.

**NOTE** :	You will need to contact your site manager if new keys need to be established. The key must exist before it can be assigned. If users NOT having the Access Authorization selects the locked Accession Area, the system echoes “??” and allows them to select again.

2.	File #68.2 (Load/Worklist), field: User Access Authorization
A site may also select to prevent the building and unloading of load/work lists from users outside of the Accession Area. An entry in this field will give this additional security.  This field also points to the File #19.1.

If these fields have null entries, any user may access the Accession Area and the Load/Worklists.


## Individual Module Requirements/Concerns


### Blood Bank

In addition to the LRLAB and LRVERIFY security keys, the Blood Bank Module requires only the LRBLOODBANK key to access the majority of the options. The LRBLSUPER key is, however, necessary to access all of the options in the Supervisor’s Menu, as well as to release incompatible blood using the Disposition-Relocation [LRBLIDR] option in the Inventory Menu.

Since the various options, excluding those in the Supervisor’s menu, do not require specific security keys, regulating access to the options must be accomplished via strict menu management. Menus must be constructed at each site, tailored to the actual needs of the individuals using the module.

### Anatomic Pathology

In addition to the LRLAB and LRVERIFY security keys, the Anatomic Pathology Module requires several specific keys to access the appropriate Accession Area

LRANAT	Anatomic Pathology users

LRAU	Autopsy Module users

LRCY	Cytology Module users

LREM	Electron Microscopy Module users

LRSP	Surgical Pathology Module users

and the options that should be limited to Supervisory grade or higher level personnel.

LRAPSUPER	Anyone allowed to use the Anatomic Pathology Supervisor Menu and edit SNOMED codes

LRSUPER	Laboratory Supervisors

Since the various options, excluding those in the Supervisor’s menu, do not require specific security keys once you have the appropriate Accession Area keys, regulating access to the options must be accomplished via strict menu management.

### Microbiology

In addition to the LRLAB and LRVERIFY security keys, the Microbiology Module requires only the LRMICRO key to access the majority of the options and the LRMIVERIFY key to release results. The LRSUPER key is necessary to access the options in the Microbiology Supervisor’s Menu.

### Chemistry/Immunology

The Chemistry subscript Module requires the LRLAB and LRVERIFY security keys to access the majority of the options. The LRSUPER key is necessary to access the options in the Supervisor’s Menu.

### Phlebotomy

The phlebotomy section requires  the LRLAB and LRPHMAN keys to access the necessary options. The LRPHSUPER key is, however, necessary to access the options needed by the Phlebotomy supervisor.