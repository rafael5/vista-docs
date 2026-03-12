---
app_name: 'Registry: Airborne Hazard Open Burn Pit (AHOBPR) (PXRM)'
base_max_patch: null
change_pages_merged: false
currency_status: unverifiable
doc_date: null
doc_type: setup-config
fetch_format: ''
forum_patch_stub: false
ingest_date: '2026-03-11'
is_base: false
is_change_pages: false
library_max_patch: null
package_id: PXRM
patch: 176
patch_gap: null
section: ''
source_file: pxrm_2_19_ig.docx
status: draft
title: pxrm 2 19 ig.docx
---

<!-- image -->

**Home Telehealth (HT)**

**PXRM*2*19 TIU*1*258 GMTS*2.7*98**

**INSTALLATION and SETUP GUIDE**

**July 2017**

**Department of Veterans Affairs Office of Information &amp; Technology (OI&amp;T)**

**Enterprise Program Management Office (EPMO)**

Contents

INTRODUCTION	1

Web Sites	11

Getting Help	11

PRE-INSTALLATION	12

Required Software for PXRM*2*19	12

Estimated Installation Time: approximately 20 minutes	12

NOTE: We recommend that a Clinical Reminders Manager or CAC be present during the install, so that if questions occur during the install of Reminder Exchange entries, a knowledgeable person can respond to them.	12

INSTALLATION	14

1. Retrieve host file containing the multi-package build and zip file containing new TXML templates.14 2. Install the build first in a training or test account	14

1. Load the distribution.	14
    1. Backup a Transport Global	14
    2. Compare Transport Global to Current System	15
    3. Verify Checksums in Transport Global	15
    4. Print Transport Global (optional)	15
2. Install the build.	15
3. Install File Print	15
4. Build File Print	16
5. Post-Install Routines	16
6. Deletion of init routines	17

SET-UP	18

Setup Instructions – Summary Steps	21

Setup Instructions – Detailed Steps	26

1. Create a new user class in for your HT clinicians	26
2. Edit your “CCHT TEMPLATES” folder in SHARED TEMPLATES to be HT TEMPLATES	26
3. Expand the HT\_TXML\_TEMPLATES.ZIP file to a known location.	26
4. Create GUI dialogs for the HT reminder dialogs	26
5. Verify that the four new HT clinical reminders launch (reminder dialogs linked) from the Reminders drawer	29
6. Create/edit the consult quick order to HOME TELEHEALTH ENROLLMENT OUTPT	31
7. Configure two new Health Summary types for the CPRS GUI Reports tab.	33
8. Assign the TIU HT MENU and (optional) PXRM HT DEFINITION EDIT to CAC(s)	33
9. Link the HT templates to NOTE TITLES	33
10. (Optional for all sites) If you need to change the FREQUENCY of the HT PERIODIC EVALUATION.	35
11. Build the 5 reminder report templates and do sample runs of each, with a short date range.	36

APPENDIX A: FILE ENTRY DELETE AND POINTER UPDATE	51

APPENDIX B: CROSSWALK FROM CCHT PILOT TO NATIONAL RELEASE	57

APPENDIX C: HT QUEUED MAILMAN REPORT	69

APPENDIX D: CONTENTS OF THE PACKED REMINDER EXPORT HT TEMPLATES/REMINDERS SET	86

APPENDIX E: CLINIC CROSSWALK	96

APPENDIX F: INSTALLATION EXAMPLE	99

APPENDIX G: FILEMAN SEARCHES FOR HT PILOT SITES	105

APPENDIX H: HEALTH FACTORS	119

7/12/2017	Home Telehealth Templates Installation Guide	iii

APPENDIX I: HEALTH FACTORS (ALPHA SORT W/ CATEGORY)	123

APPENDIX J: EDUCATION TOPICS	126

APPENDIX K: ACRONYMS AND GLOSSARY	127

ACRONYMS	128

Glossary	129

##### Introduction

The purpose of this project is to release new national reminders and reminder dialogs that will be used by Care Coordinators (Nurses, Social Workers, Rehab Specialists, Dietitians, Pharmacists and Psychologists) managing patients enrolled in HT programs.

The National Office of Connected Care (10P8) wishes to have a comprehensive, integrated template set in use at all VA facilities caring for Home Telehealth patients.

###### NOTE: These national patches and subsequent template set originated as the Care Coordination Home Telehealth (CCHT) Phase III Pilot program executed over several years at a small number of VA Medical Centers. As such, there are some steps in this document that should only apply to former pilot sites and some steps that apply only to non-pilot sites. These steps are marked accordingly.

This document is an Installation and Setup guide. The intended audience is both IT patch installers and facility CACs. IT installers should ensure that CAC partners receive a copy of this guide and work closely with CACs before, during, and after the installation.

The HT project is being distributed as a bundled build containing the following patches:

**PXRM*2*19** installs the new national reminders and dialogs, queues a report to run and sends MailMan output to the Clinical Reminders mail group.

The pre-install will disable PXRM options and protocols; run two routines that will rename any program-specific HEALTH FACTORS or EDUCATION TOPICS found at CCHT Pilot sites where those entries are installed at National IENs; and remove any previous version of the Reminder Exchange file used by the patch install.

The post-install will re-enable the options and protocols; invoke the Reminder Exchange utility to install the Clinical Reminders content; prompt for recipients and then queue the MailMan report; attempt to set the ORWPCE EXCLUDE HEALTH FACTORS and TIU TEMPLATE REMINDER DIALOGS parameters for the relevant entries; and send an install message to the local Clinical Reminders mail group.

**PXRM Inventory**

Reminder Definitions

VA-HT CAREGIVER RISK ASSESSMENT

VA-HT CONTINUUM OF CARE (FOLLOW-UP) VA-HT CONTINUUM OF CARE (INITIAL)

VA-HT OBJ BARRIERS TO LEARNING

VA-HT OBJ CAREGIVER NAME/RELATIONSHIP VA-HT OBJ CATEGORY OF CARE LAST

VA-HT OBJ CCM RATING LAST

VA-HT OBJ CONTINUUM OF CARE LAST DONE VA-HT OBJ EDUCATION TOPICS ALL

VA-HT OBJ EMERGENCY PRIORITY RATING LAST VA-HT OBJ MEDICATION RECONCILIATION

VA-HT OBJ NIC/CCM RATING LAST VA-HT PERIODIC EVALUATION

Reminder Dialogs

VA-HT ASSESSMENT TREATMENT PLAN TEMPLATE VA-HT CAREGIVER ASSESSMENT TEMPLATE

VA-HT CAREGIVER RISK ASSESSMENT VA-HT CAREGIVER/VETERAN REFERRAL VA-HT CONTINUUM OF CARE TEMPLATE

VA-HT CONTINUUM OF CARE (FOLLOW-UP) VA-HT CONTINUUM OF CARE (INITIAL)

VA-HT DISCHARGE TEMPLATE VA-HT INTERVENTION TEMPLATE VA-HT PERIODIC EVALUATION

VA-HT SCREENING CONSULT TEMPLATE

VA-HT TECH EDUCATION &amp; INSTALLATION TEMPLATE VA-HT TEMPLATE FOR PREVIOUSLY ENROLLED PATIENTS VA-HT VIDEO VISIT TEMPLATE

Reminder Terms

| VA-HT BL GEC BASIC ADLS                       |
|-----------------------------------------------|
| VA-HT BL GEC IADLS                            |
| VA-HT BL HT BASIC ADLS                        |
| VA-HT BL HT IADLS                             |
| VA-HT BL NIC/CCM CRITERIA                     |
| VA-HT CAREGIVER RELATIONSHIP                  |
| VA-HT CAREGIVER RISK ASSESSMENT DONE          |
| VA-HT CATEGORY OF CARE                        |
| VA-HT CCF DOES NOT MEET CCM CRITERIA          |
| VA-HT CCF DOES NOT MEET NIC CRITERIA          |
| VA-HT CCF FOLLOW-UP ASSESSMENT COMPLETED      |
| VA-HT CCF INITIAL ASSESSMENT COMPLETED        |
| VA-HT CCF MEETS CHRONIC CARE MGMT CRITERIA    |
| VA-HT CCF MEETS NIC CRITERIA                  |
| VA-HT CCF UNPAID CAREGIVER-YES                |
| VA-HT CCM (CHRONIC CARE MGMT) CRITERIA        |
| VA-HT DISCHARGE REASONS                       |
| VA-HT EMERGENCY PRIORITY RATINGS              |
| VA-HT ENROLLMENT-START DATE                   |
| VA-HT ENROLLMENT-START DATE (PREV ENROLL)     |
| VA-HT MEDICATIONS VIA NON-PROVIDER            |
| VA-HT PERIODIC EVALUATION COMPLETED           |
| VA-HT PT/CAREGIVER LIST OF ACTIVE MEDICATIONS |
| VA-HT PT/CAREGIVER QUESTIONS ON MEDICATIONS   |

| VA-HT SUPPRESS FOR AGE <75       |
|----------------------------------|
| VA-HT UNABLE TO SCREEN CAREGIVER |

Reminder Taxonomies

VA-HT ENCOUNTER PHONE 21 VA-HT ENCOUNTER PHONE 11 VA-HT ENCOUNTER PHONE 5

New Health Factors

| HT (HOME TELEHEALTH)                     |
|------------------------------------------|
| HT ASSESSMENT/TREATMENT PLAN             |
| HT BARRIERS TO LEARNING                  |
| HT BATHING HELP/SUPRVISION LAST 7D-NO    |
| HT BATHING HELP/SUPRVISION LAST 7D-YES   |
| HT BED MOBIL HELP/SUPERV LAST 7D-NO      |
| HT BED MOBIL HELP/SUPERV LAST 7D-YES     |
| HT CAREGIVER ASSESSMENT SCREEN COMPLETED |
| HT CAREGIVER REFERRAL BEREAVE SUPPORT    |
| HT CAREGIVER REFERRAL C/G SUPPORT GRP    |
| HT CAREGIVER REFERRAL EDUC/TRAINING      |
| HT CAREGIVER REFERRAL FAMILY COUNSEL     |
| HT CAREGIVER REFERRAL INDIVID COUNSEL    |
| HT CAREGIVER REFERRAL MEDICAL EVAL,F/U   |
| HT CAREGIVER REFERRAL OTHER SERVICE      |
| HT CAREGIVER REFERRAL SOCIAL WORK        |
| HT CAREGIVER REFERRAL SVCS IN PLACE      |
| HT CAREGIVER REFERRAL(S) NON VA SYSTEM   |
| HT CAREGIVER REFERRAL(S) VA SYSTEM       |
| HT CAREGIVER REVIEW OF WRITTEN MATERIALS |
| HT CAREGIVER RISK ASSESSMENT SCREEN      |
| HT CAREGIVER STATES ESSENTIAL CONCEPTS   |
| HT CATEGORY OF CARE-ACUTE CARE           |
| HT CATEGORY OF CARE-CHRONIC CARE MGMT    |
| HT CATEGORY OF CARE-HEALTH PROMOTION     |
| HT CATEGORY OF CARE-NON INSTITUTIONAL    |
| HT CATEGORY OF CARE-OTHER                |
| HT CCF 1 OR MORE BEHAV/COGN PROBLEMS     |
| HT CCF 12 OR MORE CLINIC STOPS PAST YR   |
| HT CCF 2 OR MORE ADL DEFICITS            |
| HT CCF AGE 75 OR GREATER                 |
| HT CCF AGITATED/DISORIENTED-NO           |
| HT CCF AGITATED/DISORIENTED-YES          |
| HT CCF CAREGIVER ACCESSIBLE              |
| HT CCF CAREGIVER CAN INCREASE HELP       |
| HT CCF CAREGIVER CAN'T INCREASE HELP     |

| HT CCF CAREGIVER LIVES WITH PT-NO      |
|----------------------------------------|
| HT CCF CAREGIVER LIVES WITH PT-YES     |
| HT CCF CAREGIVER NOT ACCESSIBLE        |
| HT CCF CAREGIVER-ADL HELP              |
| HT CCF CAREGIVER-CHILD                 |
| HT CCF CAREGIVER-EMOTIONAL SUPPORT     |
| HT CCF CAREGIVER-FRIEND/NEIGHBOR       |
| HT CCF CAREGIVER-IADL HELP             |
| HT CCF CAREGIVER-OTHER                 |
| HT CCF CAREGIVER'S CITY                |
| HT CCF CAREGIVER'S NAME                |
| HT CCF CAREGIVER'S PHONE               |
| HT CCF CAREGIVER'S STATE               |
| HT CCF CAREGIVER'S STREET ADDRESS      |
| HT CCF CAREGIVER'S ZIP CODE            |
| HT CCF CAREGIVER-SPOUSE                |
| HT CCF COMPLEXITY TOO GREAT-NO         |
| HT CCF COMPLEXITY TOO GREAT-YES        |
| HT CCF DELUSIONS-NO                    |
| HT CCF DELUSIONS-YES                   |
| HT CCF DIFFIC MAKE SELF UNDERSTOOD-NO  |
| HT CCF DIFFIC MAKE SELF UNDERSTOOD-YES |
| HT CCF DIFFIC REASONABLE DECISIONS-NO  |
| HT CCF DIFFIC REASONABLE DECISIONS-YES |
| HT CCF DOES NOT MEET CCM CRITERIA      |
| HT CCF DOES NOT MEET NIC CRITERIA      |
| HT CCF FLARE UP CHRONIC CONDITION-NO   |
| HT CCF FLARE UP CHRONIC CONDITION-YES  |
| HT CCF FOLLOW-UP ASSESSMENT COMPLETED  |
| HT CCF GROUP SETTING NON RELATIVES     |
| HT CCF HALLUCINATIONS-AUDITORY         |
| HT CCF HALLUCINATIONS-NONE             |
| HT CCF HALLUCINATIONS-OLFACTORY        |
| HT CCF HALLUCINATIONS-SENSORY          |
| HT CCF HALLUCINATIONS-TACTILE          |
| HT CCF HALLUCINATIONS-VISUAL           |
| HT CCF INITIAL ASSESSMENT COMPLETED    |
| HT CCF LIFE EXPECTANCY < 6 MO          |
| HT CCF LIVES ALONE                     |
| HT CCF LIVES ALONE IN COMMUNITY        |
| HT CCF LIVES AT OTHER                  |
| HT CCF LIVES BOARD AND CARE            |
| HT CCF LIVES DOMICILIARY               |
| HT CCF LIVES HOMELESS                  |

| HT CCF LIVES HOMELESS SHELTER           |
|-----------------------------------------|
| HT CCF LIVES NURSING HOME               |
| HT CCF LIVES PRIVATE HOME               |
| HT CCF LIVES WITH ADULT CHILD           |
| HT CCF LIVES WITH CHILD                 |
| HT CCF LIVES WITH OTHER                 |
| HT CCF LIVES WITH SPOUSE & OTHERS       |
| HT CCF LIVES WITH SPOUSE ONLY           |
| HT CCF MEETS CHRONIC CARE MGMT CRITERIA |
| HT CCF MEETS NIC CATEGORY A CRITERIA    |
| HT CCF MEETS NIC CATEGORY B CRITERIA    |
| HT CCF MEETS NIC CRITERIA               |
| HT CCF MOOD DISORDER DEPRESSION-NO      |
| HT CCF MOOD DISORDER DEPRESSION-YES     |
| HT CCF MOOD DISORDER MANIC-NO           |
| HT CCF MOOD DISORDER MANIC-YES          |
| HT CCF NIC CRITERIA NO-ACUTE CARE MGMT  |
| HT CCF NIC CRITERIA NO-HLTH PROMOTION   |
| HT CCF PHYSICALLY ABUSIVE BEHAVIOR-NO   |
| HT CCF PHYSICALLY ABUSIVE BEHAVIOR-YES  |
| HT CCF POTENTIAL FOR INCR INDEP-NO      |
| HT CCF POTENTIAL FOR INCR INDEP-YES     |
| HT CCF PROBLEMS WITH 3 OR MORE ADLS     |
| HT CCF PROBLEMS WITH 3 OR MORE IADL     |
| HT CCF PTSD/OTHER ANXIETY-NO            |
| HT CCF PTSD/OTHER ANXIETY-YES           |
| HT CCF RECOMMEND REFERRAL-NO            |
| HT CCF RECOMMEND REFERRAL-YES           |
| HT CCF RESISTING CARE-NO                |
| HT CCF RESISTING CARE-YES               |
| HT CCF SERVICES IN PLACE-NO             |
| HT CCF SERVICES IN PLACE-YES            |
| HT CCF SUBST ABUSE/DEPENDENCE-NO        |
| HT CCF SUBST ABUSE/DEPENDENCE-YES       |
| HT CCF UNPAID CAREGIVER-NO              |
| HT CCF UNPAID CAREGIVER-YES             |
| HT CCF VERBALLY ABUSIVE BEHAVIOR-NO     |
| HT CCF VERBALLY ABUSIVE BEHAVIOR-YES    |
| HT CCF WANDERING-NO                     |
| HT CCF WANDERING-YES                    |
| HT CG/VETERAN REFERRAL COMPLETED        |
| HT CG/VETERAN REFERRAL(S) NOT UTILIZED  |
| HT CLINICAL REASON FOR ENROLLMENT       |
| HT CONSULTS/REFERRALS RECOMMENDED       |

| HT CONTINUUM OF CARE (CCF)              |
|-----------------------------------------|
| HT DIFFICULT MANAGING MEDS/LAST 7D-NO   |
| HT DIFFICULT MANAGING MEDS/LAST 7D-YES  |
| HT DIFFICULT MNG FINANCES/LAST 7D-NO    |
| HT DIFFICULT MNG FINANCES/LAST 7D-YES   |
| HT DIFFICULT PREPARE MEALS/LAST 7D-NO   |
| HT DIFFICULT PREPARE MEALS/LAST 7D-YES  |
| HT DIFFICULT TRANSPORTATION/LAST 7D-NO  |
| HT DIFFICULT TRANSPORTATION/LAST 7D-YES |
| HT DIFFICULT USING PHONE LAST 7D-NO     |
| HT DIFFICULT USING PHONE LAST 7D-YES    |
| HT DIFFICULT W/ HOUSEWORK/LAST 7D-NO    |
| HT DIFFICULT W/ HOUSEWORK/LAST 7D-YES   |
| HT DIFFICULT WITH SHOPPING/LAST 7D-NO   |
| HT DIFFICULT WITH SHOPPING/LAST 7D-YES  |
| HT DISCHARGE                            |
| HT DISCHARGE-ADMITTED TO NURSING HOME   |
| HT DISCHARGE-ALL ISSUES ADDRESSED(NO)   |
| HT DISCHARGE-ALL ISSUES ADDRESSED(YES)  |
| HT DISCHARGE-HAS MET GOALS              |
| HT DISCHARGE-NO RESPONSE TO PROGRAM     |
| HT DISCHARGE-NO VA PRIMARY CARE SVCS    |
| HT DISCHARGE-OTHER FOLLOW-UP            |
| HT DISCHARGE-PATIENT IS DECEASED        |
| HT DISCHARGE-PHONE,ELECT SVCS UNAVAIL   |
| HT DISCHARGE-PROLONGED HOSPITALIZATION  |
| HT DISCHARGE-PROVIDER REQUESTS DC       |
| HT DISCHARGE-PT/CG REQUEST DC SERVICES  |
| HT DISCHARGE-REFERRED TO HOSPICE        |
| HT DISCHARGE-REFERRED TO MENTAL HEALTH  |
| HT DISCHARGE-REFERRED TO NEW LOCATION   |
| HT DISCHARGE-REFERRED TO PRIMARY CARE   |
| HT DISCHARGE-REFERRED TO SOCIAL WORK    |
| HT DISCHARGE-RELOCATED OUT OF SVC AREA  |
| HT DISCHARGE-UNABLE TO OPERATE DEVICES  |
| HT DISEASE INDICATIONS-COPD             |
| HT DISEASE INDICATIONS-DEPRESSION       |
| HT DISEASE INDICATIONS-DIABETES         |
| HT DISEASE INDICATIONS-HEART FAILURE    |
| HT DISEASE INDICATIONS-HYPERTENSION     |
| HT DISEASE INDICATIONS-OBESITY          |
| HT DISEASE INDICATIONS-OTHER            |
| HT DISEASE INDICATIONS-PTSD             |
| HT DISEASE INDICATIONS-SUBSTANCE ABUSE  |

6	Home Telehealth Templates Install and Setup Guide	7/12/2017

| HT DISINTERESTED/LACKS MOTIVATION        |
|------------------------------------------|
| HT DRESSING HELP/SUPERV LAST 7D-NO       |
| HT DRESSING HELP/SUPERV LAST 7D-YES      |
| HT EATING HELP/SUPERVISION LAST 7D-NO    |
| HT EATING HELP/SUPERVISION LAST 7D-YES   |
| HT EMERG PRIORITY HIGH-IMMEDIATE EVAL    |
| HT EMERG PRIORITY LOW-HAS RESOURCES      |
| HT EMERG PRIORITY MOD-SVCS AFTER 3-7D    |
| HT ENROLLMENT-ENDING DATE                |
| HT ENROLLMENT-START DATE                 |
| HT ENROLLMENT-START DATE (PREV ENROLL)   |
| HT EQUIP INSTALLED BY OTHER              |
| HT EQUIP INSTALLED BY SUPPORT STAFF      |
| HT EQUIP INSTALLED BY VETERAN/CAREGIVER  |
| HT GETS MEDS VIA NON-VA PROVIDER-NO      |
| HT GETS MEDS VIA NON-VA PROVIDER-YES     |
| HT HEALTH EDUCATION PLAN                 |
| HT HEALTH EDUCATION RESPONSE             |
| HT INDICATIONS-# OUTPT VISITS PAST YR    |
| HT INDICATIONS-DISTANCE (HOURS)          |
| HT INDICATIONS-DISTANCE (MILES)          |
| HT INDICATIONS-HX HIGH COST/HIGH USE     |
| HT INDICATIONS-HX HOSPITALIZATONS        |
| HT LEARNING BARRIER-ANGRY                |
| HT LEARNING BARRIER-ANXIETY              |
| HT LEARNING BARRIER-APHASIA              |
| HT LEARNING BARRIER-COGNITIVE IMPAIRMENT |
| HT LEARNING BARRIER-CULTURAL             |
| HT LEARNING BARRIER-HEARING IMPAIRED     |
| HT LEARNING BARRIER-HOMELESS             |
| HT LEARNING BARRIER-IMPAIRED MEMORY      |
| HT LEARNING BARRIER-NONE IDENTIFIED      |
| HT LEARNING BARRIER-NOT MOTIVATED        |
| HT LEARNING BARRIER-OVERWHELMED          |
| HT LEARNING BARRIER-PAIN                 |
| HT LEARNING BARRIER-PHYSICAL LIMITATIONS |
| HT LEARNING BARRIER-POOR CONCENTRATION   |
| HT LEARNING BARRIER-UNABLE TO READ       |
| HT LEARNING BARRIER-UNABLE TO WRITE      |
| HT LEARNING BARRIER-VISUALLY IMPAIRED    |
| HT MEALS PREPARED BY OTHER/LAST 7D-NO    |
| HT MEALS PREPARED BY OTHER/LAST 7D-YES   |
| HT MEETS TELEHEALTH CRITERIA(NO)         |
| HT MEETS TELEHEALTH CRITERIA(YES)        |

| HT MOVE INDOOR HELP/SUPERV LAST 7D-NO    |
|------------------------------------------|
| HT MOVE INDOOR HELP/SUPERV LAST 7D-YES   |
| HT NEEDS REINFORCEMENT/REVIEW/FOLLOW-UP  |
| HT NO EVIDENCE OF LEARNING               |
| HT NO FOLLOW-UP NEEDED/INDICATED         |
| HT PERIODIC EVALUATION COMPLETED         |
| HT PLAN-MED DISCREP SENT TO PROVIDER     |
| HT PLAN-REVIEWED LIST OF CURRENT MEDS    |
| HT PT/CG HAS LIST OF ACTIVE MEDS-NO      |
| HT PT/CG HAS LIST OF ACTIVE MEDS-YES     |
| HT PT/CG HAS QUESTIONS ON MEDS-NO        |
| HT PT/CG HAS QUESTIONS ON MEDS-YES       |
| HT REASON FOR NON-ENROLLMENT             |
| HT RECENT CHANGE IN FUNCTION-NO          |
| HT RECENT CHANGE IN FUNCTION-YES         |
| HT REFERRAL-CONSULT COMPLETION           |
| HT REFERRALS FOR VETERAN/CAREGIVER       |
| HT REFERRALS-CAREGIVER NOT SATISFIED     |
| HT REFERRALS-CAREGIVER SATISFIED         |
| HT REPEAT DEMONSTRATION NEXT VISIT       |
| HT TEACH CAREGIVER/FAMILY/SIGNIF OTHER   |
| HT TELEHEALTH DELIVERY/INSTALL MODE      |
| HT TELEHEALTH DEMOGRAPHICS               |
| HT TOILET HELP/SUPERVISION LAST 7D-NO    |
| HT TOILET HELP/SUPERVISION LAST 7D-YES   |
| HT TRANSFERS HELP/SUPERV LAST 7D-NO      |
| HT TRANSFERS HELP/SUPERV LAST 7D-YES     |
| HT UNABLE TO SCREEN CAREGIVER            |
| HT VET NOT INTERESTED TELEHEALTH PROGRAM |
| HT VET/CAREGIVER VIEW VIDEOS/HEALTH TV   |
| HT VETERAN REFERRAL EDUC/TRAINING        |
| HT VETERAN REFERRAL OTHER SERVICE        |
| HT VETERAN REFERRAL SVCS IN PLACE        |
| HT VETERAN REFERRAL(S) NON VA SYSTEM     |
| HT VETERAN REFERRAL(S) VA SYSTEM         |
| HT VETERAN REVIEW OF WRITTEN MATERIALS   |
| HT VETERAN STATES ESSENTIAL CONCEPTS     |
| HT VETERAN'S GOAL FOR ENROLLMENT         |
| HT W/C MOBIL HELP/SUPERV LAST 7D-NO      |
| HT W/C MOBIL HELP/SUPERV LAST 7D-YES     |

New Education Topics

| VA-HOME TELEHEALTH-CAREGIVER EDUCATION/SUPPORT    |
|---------------------------------------------------|
| VA-HOME TELEHEALTH-DISEASE MGMT/PATIENT SELF-MGMT |

| VA-HOME TELEHEALTH-IN HOME MONITORING    |
|------------------------------------------|
| VA-HOME TELEHEALTH-MEDICATION MANAGEMENT |

TIU Template Fields

| BLANK SPACE1               |
|----------------------------|
| OPTIONAL TEXT              |
| OTHER(REQ-DISP ONLY)       |
| TEXT (1-60 CHARACTERS) REQ |
| VA-HT EDIT50               |
| VA-HT OTHER                |
| VA-HT SPECIFY              |
| VA-HT VITAL SIGNS MODE     |
| VA-HT W-P2LINES(R)         |
| VA-HT W-P4LINES(R)         |
| VA-HT W-P6LINES            |
| VA-HT W-P6LINES(R)         |

**TIU*1.0*258** deploys the twelve official titles for the Home Telehealth (HT) program, and will ensure compliance with the HT program’s TIU Document Definitions Hierarchy. The end result from the TIU installation should be a document class named HOME TELEHEALTH NOTES installed under the PROGRESS NOTES document class. Contained in HOME TELEHEALTH NOTES will be the titles for HT. They are:

HT ASSESSMENT TREATMENT PLAN NOTE HT CAREGIVER ASSESSMENT NOTE

HT CONTINUUM OF CARE NOTE HT DISCHARGE NOTE

HT INTERVENTION NOTE HT NOTE

HT PERIODIC EVALUATION NOTE

HT SCREENING CONSULT (will be installed under CONSULTS document class) HT SUMMARY OF EPISODE NOTE

HT TECH EDUCATION NOT

HT TELEPHONE CASE MANAGEMENT NOTE HT VIDEO VISIT NOTE

The patch has an environment check routine, TIUP258E, which searches for several items and scenarios:

- CLINICAL COORDINATOR user class
- Document Classes:
    - CARE COORDINATION HOME TELEHEALTH NOTES
    - HOME TELEHEALTH NOTES
    - CONSULTS
- Pre-existing “CCHT” or “HT” named local titles (e.g. “CCHT NOTE” or “HT NOTE”)

If CLINICAL COORDINATOR or CONSULTS are missing, the installation will abort and cannot continue until the issue is corrected.

For any pre-existing “CCHT” or “HT” local titles, the environment check is only concerned with titles that have a name match to an incoming national title and are not part of CONSULTS, CARE COORDINATION HOME TELEHEALTH NOTES, or HOME TELEHEALTH NOTES.

If any local titles meet these criteria, a list of each title along with the IEN from TIU DOCUMENT DEFINITION (#9825.1) will be displayed on the screen and the installation will abort.

For example, if a site already has a title named HT NOTES but that title is *not* sitting under a document class of CARE COORDINATION HOME TELEHEALTH NOTES, or HOME

TELEHEALTH NOTES, then this title will be displayed on the installer’s screen and the install will abort. Alternatively, if a title named HT PERIODIC EVALUATION is found under HOME TELEHEALTH NOTES, this will not trigger an abort condition for the installation.

Verifying installation environment...

Checking for existing document classes... Document class found: HOME TELEHEALTH NOTES

Document class check complete.

Now checking for any local titles that may conflict with new national titles.

***INSTALL ABORTING***

The following title NAMES (.01) have been found in TIU DOCUMENT DEFINITION. These titles are NOT part of the HOME TELEHEALTH NOTES document class or the CARE COORDINATION HOME TELEHEALTH NOTES document class.

These NAMES will clash with new National titles in patch TIU*1*258.

To correct this issue, please work with site staff to rename these titles. HT NOTE(#50)

**INSTALL WILL NOW ABORT. TRANSPORT GLOBAL(S) WILL BE UNLOADED**

Please re-install HT TEMPLATES PROJECT 1.0 when corrections are complete.

Example display from a test installation

The TIU pre-install routine will prepare the TIU environment to receive the new HT titles. For CCHT pilot sites, this means inactivating the CARE COORDINATION HOME TELEHEALTH NOTES document class and renaming it to HOME TELEHEALTH NOTES. After that, the relevant “CCHT” note titles will be renamed to “HT” equivalents provided the titles are a member of the HOME TELEHEALTH NOTES document class (or CONSULTS document class in the case of CCHT SCREENING CONSULT). For a given title, if a name match is found, but that title is found in a different document class than expected, a new HT title will be created (during post-install) in lieu of renaming the CCHT title.

For sites that did not participate in the CCHT pilot program, the pre-install routine will inactivate and rename the CARE COORDINATION HOME TELEHEALTH NOTES document class. Any pre-existing local title(s) with will be renamed (“CCHT” to “HT”) but only if the title(s) are found in the expected document class.

The post-install routine will complete the document definition installations; map the newly introduced HT titles to the HT Enterprise Standard Titles; and if possible, activate the new titles. If the mapping or activation fails for a given title, those tasks can be accomplished locally via TIU package options.

**GMTS*2.7*98** adds two new Health Summary reports for display on the CPRS Reports tab. These reports will display both local and remote data.

This patch contains an environment check routine, GMTSPI98, that will run when the KIDS build is first loaded. This routine checks for the presence of any file entries at IEN 5000018 and 5000019 in the ^GMT(142 global. These IENs should be undefined/empty as the 5000000+ IEN range is reserved for new National remote health summary types. If an entry is found at either location, the install will abort. If this occurs, the site should contact the National Help Desk for assistance with the Health Summary package and moving the existing entry(ies) to a different IEN in the ^GMT(142 global. Once this has been corrected, the site may then re-load and re- install the bundle.

The pre-install will remove any previous version of the Reminder Exchange file used to create the two new remote Health Summary Types. The post-install will create a stub entry in HEALTH SUMMARY TYPE (#142) for each of the two remote Health Summary Types and then call the Reminder Exchange utility to populate the stub entries with the content for each Health Summary Type. All other Health Summary items are installed via Reminder Exchange by the PXRM*2.0*19 patch.

###### Web Sites

| **Site**                              | **URL**                                                  | **Description**                                                                             |
|---------------------------------------|----------------------------------------------------------|---------------------------------------------------------------------------------------------|
| National Clinical Reminders site      | http://vista.med.va.gov/reminders                        | Contains manuals, PowerPoint  presentations, and other information about Clinical Reminders |
| National Clinical Reminders Committee | http://vaww.portal.va.gov/sites/ncrc public/default.aspx | This committee directs the development of new and revised  national reminders               |
| VA Software  Document Library         | http://www.va.gov/vdl/                                   | Contains manuals for Clinical  Reminders and related applications.                          |

###### Getting Help

If you require further technical assistance, please notify your local IT support to log a national CA Service Desk Manager (SDM) ticket (previously a Remedy™ ticket) or contact the VA Service Desk at 1-888-596-4357 and have them submit a national CA ticket to the Incident Area: NTL.APP.VISTA.CLINICAL REMINDERS 2\_0 and we will contact you.

##### Pre-Installation

This manual describes how to install the bundled patches, PXRM*2*19, GMTS*2.7*98, and TIU*1*258.

###### Required Software for PXRM*2*19

| **Package/Patch**                     | **Namespace**   |   **Version** | **Comments**   |
|---------------------------------------|-----------------|---------------|----------------|
| Clinical Reminders                    | PXRM            |           2   | Fully patched  |
| GEN. MED. REC. – VITALS  GMRV*5*25    | GMRV            |           5   |                |
| Health Summary                        | GMTS            |           2.7 | Fully patched  |
| HL7                                   | HL              |           1.6 | Fully patched  |
| Kernel                                | XU              |           8   | Fully patched  |
| MailMan                               | XM              |           7.1 | Fully patched  |
| NATIONAL DRUG FILE  PSN*4.0*176       | PSN             |           4   |                |
| Pharmacy Data Management  PSS*1.0*133 | PSS             |           1   |                |
| Outpatient Pharmacy  PSO*7.0*299      | PSO             |           7   |                |
| RADIOLOGY/NUCLEAR MEDICINE  RA*5*56   | RA              |           5   |                |
| TOOLKIT  XT*7.3*111                   | XT              |           7.3 |                |
| VA FileMan                            | DI              |          22.2 | Fully patched  |

###### Estimated Installation Time: approximately 20 minutes

###### NOTE: We recommend that a Clinical Reminders Manager or CAC be present during the install, so that if questions occur during the install of Reminder Exchange entries, a knowledgeable person can respond to them.

**Pre-Installation Instructions**

1. Please review the setup steps beginning on page 18 before starting the installation. The installation will do the following:
    - Disable PXRM menu options and protocols.
    - Delete any previous version of the associated Reminder Exchange entry.
    - At pilot program sites, converts a subset of the pre-existing local HT components to National components.

1. ***Pilot sites.*** Inspect and remove any pre-existing “CCHT” or “HT” entries at the SYSTEM level for the following parameters: ORWPCE EXCLUDE HEALTH FACTORS. Use the General Parameter Tools menu [XPAR MENU TOOLS] to clean up these parameter entries.

Select OPTION NAME: XPAR MENU TOOLS	General Parameter Tools	menu

LV	List Values for a Selected Parameter LE	List Values for a Selected Entity

LP	List Values for a Selected Package LT	List Values for a Selected Template EP	Edit Parameter Values

ET	Edit Parameter Values with Template EK	Edit Parameter Definition Keyword

Select General Parameter Tools &lt;TEST ACCOUNT&gt; Option: EP	Edit Parameter Values

--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: ORWPCE EXCLUDE HEALTH FACTORS Excluded Health

Factors

ORWPCE EXCLUDE HEALTH FACTORS may be set for the following:

|   1 | User     | USR   | [choose                         | from                            | NEW PERSON]                     |
|-----|----------|-------|---------------------------------|---------------------------------|---------------------------------|
|   2 | Location | LOC   | [choose                         | from                            | HOSPITAL LOCATION]              |
|   3 | Service  | SRV   | [choose                         | from                            | SERVICE/SECTION]                |
|   4 | Division | DIV   | [choose                         | from                            | INSTITUTION]                    |
|   5 | System   | SYS   | [DVF.FO-SLC.MED.VA.GOV]         | [DVF.FO-SLC.MED.VA.GOV]         | [DVF.FO-SLC.MED.VA.GOV]         |
|   6 | Package  | PKG   | [ORDER ENTRY/RESULTS REPORTING] | [ORDER ENTRY/RESULTS REPORTING] | [ORDER ENTRY/RESULTS REPORTING] |

Enter selection: 5	System	DVF.FO-SLC.MED.VA.GOV

-- Setting ORWPCE EXCLUDE HEALTH FACTORS	for System: DVF.FO-SLC.MED.VA.GOV --

Select Sequence: ?

Sequence	Value

1. CCHT ASSESSMENT/TREATMENT PLAN
2. CCHT CAREGIVER RISK ASSESSMENT SCREEN
3. CCHT CONTINUUM OF CARE
4. CCHT DISCHARGE
5. CCHT REFERRALS FOR VETERAN/CAREGIVER
6. CCHT TELEHEALTH DELIVERY/INSTALL MODE
7. CCHT TELEHEALTH DEMOGRAPHICS

Select Sequence: 2

Sequence: 2//	2

Health Factor: CCHT ASSESSMENT/TREATMENT PLAN// HT ASSESSMENT/TREATMENT PLAN

1. Before beginning the installation, the IT person who will install the patch bundle should determine the individuals and/or mail group(s) at the local facility that should receive the queued MailMan report generated by the post-install. This report should be shared with local Clinical Reminders support/configuration staff and/or any other local staff as deemed appropriate by each facility.
2. Facility CACs: Review local TIU titles for any titles that may present conflicts as explained in the TIU*1.0*258 section of the Introduction. Doing this task before IT

attempts the installation will avoid delay if conflicts are found and the patch install is aborted.

## Installation

This build can be installed with users on the system, but it should be done during non-peak hours.

***The installation needs to be done by a person with DUZ(0) set to "@."***

1. **Retrieve host file containing the multi-package build and zip file containing new TXML templates.**

REDACTED REDACTED - REDACTED

Albany Hines

Salt Lake City

Use sftp to access the build from one of the following locations:

The name of the host file is HT\_TEMPLATES\_1\_0.KID

The name of the zip file is HT\_TXML\_TEMPLATES.ZIP – send this file to the Clinical Reminders CAC at the site for which you are installing.

1. **Install the build first in a training or test account.**

Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

###### 1 Load the distribution.

In programmer mode, type, D ^XUP, select the Kernel Installation &amp; Distribution System menu (XPD MAIN), then the Installation option, and then the option LOAD a Distribution. Enter your directory name and HT\_TEMPLATES\_1.0.KID at the Host File prompt.

###### Example

From the Installation menu, you may elect to use the following options:

###### 2 Backup a Transport Global

This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.

###### 3 Compare Transport Global to Current System

This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

###### 4 Verify Checksums in Transport Global

This option will allow you to ensure the integrity of the routines that are in the transport global. If there are any discrepancies, do not run the Install Package(s) option. Instead, run the Unload a Distribution option to remove the Transport Global from your system.

Retrieve the file again from the anonymous directory (in case there was corruption in transferring) and Load the Distribution again. If the problem still exists, log a Remedy ticket and/or call the national Help Desk (1-888-596-HELP) to report the problem.

###### 5 Print Transport Global (optional)

This option will allow you to view the components of the KIDS build.

###### 6 Install the build.

From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s).  Select the build xxx  and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

Select Installation &amp; Distribution System Option: **Installation**

Select Installation Option: **INSTALL PACKAGE(S)**

Select INSTALL NAME: **HT TEMPLATES PROJECT 1.0**

Answer "NO" to the following prompts:

Want KIDS to INHIBIT LOGONs during install? NO// **NO**

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// **NO**

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// **NO**

**NOTE: DO NOT QUEUE THE INSTALLATION** , because this installation may ask questions requiring responses and queuing will stop the installation. The most common are replacements for finding items or quick orders during the installation of Reminder Exchange file entries.

###### Installation Example

See Appendix G .

###### 7 Install File Print

Use the KIDS Install File Print option to print out the results of the installation process. You can select the multi-package build or any of the individual builds included in the multi- package build.

Select Utilities Option: **Install** File Print Select INSTALL NAME: HT TEMPLATES PROJECT 1.0

###### 8 Build File Print

Use the KIDS Build File Print option to print out the build components.

Select Utilities Option:	Build File Print Select BUILD NAME: **HT TEMPLATES PROJECT 1.0** DEVICE: HOME//

###### 9 Post-Install Routines

Following successful installation of the KIDS build, the post-install routine invokes the Reminders Exchange Utility's silent installer to correctly install the HT Document Definition hierarchy, maps the newly introduced HT titles to the HT Enterprise Standard Titles, and if possible, activates the new titles.

- The installation will place the following major file entries in the Reminder Exchange file #811.8 (full contents of the Reminder Exchange file are in Appendix D ):

REMINDER DIALOG

VA-HT ASSESSMENT TREATMENT PLAN TEMPLATE VA-HT CAREGIVER ASSESSMENT TEMPLATE

VA-HT CAREGIVER RISK ASSESSMENT VA-HT CAREGIVER/VETERAN REFERRAL VA-HT CONTINUUM OF CARE TEMPLATE

VA-HT CONTINUUM OF CARE (FOLLOW-UP) VA-HT CONTINUUM OF CARE (INITIAL)

VA-HT DISCHARGE TEMPLATE VA-HT INTERVENTION TEMPLATE VA-HT PERIODIC EVALUATION

VA-HT SCREENING CONSULT TEMPLATE

VA-HT TECH EDUCATION &amp; INSTALLATION TEMPLATE VA-HT TEMPLATE FOR PREVIOUSLY ENROLLED PATIENTS VA-HT VIDEO VISIT TEMPLATE

REMINDER DEFINITION

VA-HT CAREGIVER RISK ASSESSMENT

VA-HT CONTINUUM OF CARE (FOLLOW-UP) VA-HT CONTINUUM OF CARE (INITIAL)

VA-HT OBJ BARRIERS TO LEARNING

VA-HT OBJ CAREGIVER NAME/RELATIONSHIP VA-HT OBJ CATEGORY OF CARE LAST

VA-HT OBJ CCM RATING LAST

VA-HT OBJ CONTINUUM OF CARE LAST DONE VA-HT OBJ EDUCATION TOPICS ALL

VA-HT OBJ EMERGENCY PRIORITY RATING LAST VA-HT OBJ MEDICATION RECONCILIATION

VA-HT OBJ NIC/CCM RATING LAST VA-HT PERIODIC EVALUATION

- **If you need to change the frequency of the HT PERIODIC EVALUATION reminder to a value other than the exported 180 days, use the PXRM HT DEFINITION EDIT option. This option has been created expressly to allow sites to edit the frequency for the HT PERIODIC EVALUATION reminder.** The option should be assigned as a secondary menu item to the user(s) responsible for maintaining the Home Telehealth reminder definitions.

- The post-init of this GMTS patch will install the new entries in the HEALTH SUMMARY TYPE file (#142). They are:

REMOTE HT CLINICAL REMINDERS REMOTE HT TRACKING

The stub entries in the ^GMT(142 global during pre-install are then populated by the Reminder Exchange file GMTS HS TYPE FOR VA-HT which is silently installed via the Reminder Exchange utility.

###### 10 Deletion of init routines

PXRMP19B, PXRMP19I, TIUP258, and GMTSPI98 can safely be deleted from the system once installation is successful and all HT reminders, reminder dialogs, and associated templates have been verified to be complete and working as expected. Local IT staff should consider keeping a copy of these routines as they may prove useful in the event of any unexpected issues with this patch. PXRMP19A should remain on the system until such time as Clinical Reminder CACs and or Home Telehealth staff determine that the MailMan report described in Appendix C is no longer necessary. At that time, PXRMP19A, may also be deleted from the system.

###### 11 Assign TIU HT MENU

The TIU HT MENU includes options to facilitate implementation of the TIU support for Home Telehealth. It should be assigned to individuals tasked with such activities.

## Set-up

###### Overview

Installation of the multi-package build does the following:

- Enables PXRM options and protocols,
- Installs the associated Reminder Exchange entries.
- Queues a single report to run and sends output via MailMan message to recipients selected during installation.

The TIU patch exports a new menu with two options: TIU HT MENU

This menu includes options to facilitate implementation of the TIU support for Home Telehealth.

TIU HT TITLE MAPPINGS

This option prints a list of all HT Titles, with their Status and VHA Enterprise Standard Titles. This will allow you to verify that the appropriate titles were installed, renamed, and mapped by patch TIU*1*258.

TIU HT VERIFY TITLES

This option prints a list of all HT Titles, with their Status and Print Names. This will allow you to verify that the appropriate titles were installed, renamed, or inactivated by patch TIU*1*258.

###### Background – Design Logic

**For the reminders module imports:**

There are three variations of the HT CONTINUUM OF CARE reminder dialog/template:

- Two are linked to reminder definitions
    - VA-HT CONTINUUM OF CARE (INITIAL) *(has a non-interactive HF for initial assessment)*
    - VA-HT CONTINUUM OF CARE (FOLLOW-UP) *(has a non-interactive HF for f/u assessment)*
- One template, the HT CONTINUUM OF CARE template, has an interactive required item for initial/follow-up at the top of the template. This template is attached to a note title of same name and is also stand-alone in Shared Templates.

These reminder dialogs will be linked to note titles of the same name: HT ASSESSMENT TREATMENT PLAN NOTE

HT CAREGIVER ASSESSMENT NOTE HT CONTINUUM OF CARE NOTE

HT DISCHARGE NOTE

HT INTERVENTION NOTE HT NOTE

HT PERIODIC EVALUATION NOTE HT TECH EDUCATION

HT TELEPHONE CASE MANAGEMENT NOTE HT VIDEO VISIT NOTE

Of the 13 reminder definitions:

- Four of the packed reminder exports are true “clinical reminders” in the Reminders drawer: *(Displayed here in order of how they will fire during a Veteran’s course of HT care):*
    - VA-HT CONTINUUM OF CARE (INITIAL)
    - VA-HT CAREGIVER RISK ASSESSEMENT
    - VA-HT PERIODIC EVALUATION
    - VA-HT CONTINUUM OF CARE (FOLLOW-UP)

- Nine reminder definitions are used to evaluate data objects:
    - VA-HT OBJ BARRIERS TO LEARNING
    - VA-HT OBJ CAREGIVER NAME/RELATIONSHIP
    - VA-HT OBJ CATEGORY OF CARE LAST
    - VA-HT OBJ CCM RATING LAST
    - VA-HT OBJ CONTINUUM OF CARE LAST DONE
    - VA-HT OBJ EDUCATION TOPICS ALL
    - VA-HT OBJ EMERGENCY PRIORITY RATING LAST
    - VA-HT OBJ MEDICATION RECONCILIATION
    - VA-HT OBJ NIC/CCM RATING LAST

Three of the reminder dialogs will be “stand-alone” in the SHARED TEMPLATES HT folder:

- VA-HT CONTINUUM OF CARE TEMPLATE
- VA-HT CAREGIVER ASSESSMENT TEMPLATE
- VA-HT TECH EDUCATION &amp; INSTALLATION TEMPLATE

###### For the two GUI dialog templates (.txml files):

- **VA-HOME TELEHEALTH SCREENING** is linked to the CONSULT SERVICE (file #123.5) HOME TELEHEALTH ENROLLMENT OUTPT in the CPRS GUI Template Editor. It will be used in a consult QUICK ORDER to order the consult. (NOTE: It should be named HOME TELEHEALTH ENROLLMENT OUTPT in your file. This new naming does not affect the template in any way nor VistA Integration).

###### 12 VA-HT MONTHLY MONITOR:

There are full HT templates embedded within other templates:

The HT ASSESSMENT TREATMENT PLAN template has three collapsed (optional) templates embedded:

VA-HT CONTINUUM OF CARE TEMPLATE VA-HT CAREGIVER RISK ASSESSMENT VA-HT CAREGIVER/VETERAN REFERRAL

The HT CAREGIVER ASSESSMENT template contains two collapsed (optional) templates:

VA-HT CAREGIVER RISK ASSESSMENT VA-HT CAREGIVER/VETERAN REFERRAL

The HT PERIODIC EVALUATION template contains two collapsed (optional) templates:

VA-HT CAREGIVER RISK ASSESSMENT VA-HT CAREGIVER/VETERAN REFERRAL

VA-HT TEMPLATE FOR PREVIOUSLY ENROLLED PATIENTS

This template is intended for use by non-pilot sites to sweep up HT currently enrolled patients for the 4 new national HT clinical reminders where note documentation had been done without the standardized national HT reminder dialogs with health factors to trigger the new HT reminders when they should be due. It is for ONE-TIME use on current HT patients. This template should be used on each patient in order to set the health factors associated with the date of enrollment, date of last periodic evaluation, and the non-institutional care status. Once the health factors are set, the HT clinical reminders will now be applicable to each of these patients.

The template should be added to the HT Templates folder within the Shared Templates folder of the CPRS GUI editor. Your site will create a GUI template dialog linked to the VA-HT TEMPLATE FOR PREVIOUSLY ENROLLED PATIENTS. You will then link this template to the generic HT NOTE title.

This template should be used soon after installation of the HT Templates bundle. The CAC should notify the HT Lead that the template is available for use. Once Care Coordinators have used the template on all HT currently enrolled patients, the HT Lead should notify the CAC that the GUI dialog template can be removed from service.

***In summary*** , this is a rather complex configuration, done for the convenience of HT clinicians at various sites who have different preferences.

Since all of the four clinical reminders exist as templates on note titles and some are additionally stand-alone in CPRS’ Shared Templates, it’s possible that many HT clinicians may not go to the actual clinical reminders (Reminders drawer) to resolve their clinical reminders

If HT clinicians are timely with their documentation, these four HT clinical reminders (which are basically 'documentation benchmarks') are most beneficial for HT site leads who would be running reminder report templates as they deem desirable, in order to check HT clinical reminder status across the enrolled patients at any point in time, for oversight and monitoring of timely documentation:

- A summary report of all four (4) HT clinical reminders (no individual patient data) with raw numbers and percentages of HT reminders due versus resolved
- Four (4) reminder report templates for EACH of the four (4) HT clinical reminders, for the user running the report to easily determine and communicate to other HT staff which individual patients have reminders past due with date.

Four (4) reminder report templates for EACH of the (4) HT clinical reminders, for the user running the report to easily determine and communicate to other HT staff which individual patients have reminders past due with date.

HT staff will now have an easy method of checking HT reminder status on individual patients, through the new Health Summary on the CPRS GUI Reports tab, as well as new data objects in templates that display reminder status.

**Setup Instructions – Summary Steps**

The following is a summary of the setup steps, with hyperlinks to detailed instructions and examples that follow.

1. Map any local findings to the appropriate reminder terms

1. VA-HT ENROLLMENT-START DATE

This term is released the health factor HT ENROLLMENT DATE.

Map any local finding(s) representing the home telehealth enrollment date for the patient.

1. VA-HT CCF INITIAL ASSESSMENT COMPLETED

This term is released the health factor HT CCF INITIAL ASSESSMENT COMPLETED. Map any local finding(s) representing completion of the initial home telehealth continuum of care assessment.

1. VA-HT CCF MEETS NIC CRITERIA

This term is released the health factor HT CCF MEETS NIC CRITERIA.

Map any local finding(s) representing the Non-Institutional Care criteria is met by the patient.

1. VA-HT CCF DOES NOT MEET NIC CRITERIA

This term is released the health factor HT CCF DOES NOT MEET NIC CRITERIA. Map any local finding(s) representing the Non-Institutional Care criteria is not met by the patient.

1. VA-HT DISCHARGE REASONS

This term is released with several health factors representing a patient’s discharge from home telehealth along with the specific reason.

Map any local finding(s) representing the intent of this term.

1. VA-HT ENROLLMENT-START DATE (PREV ENROLL)

This term is released with the health factor HT ENROLLMENT-START DATE (PREV ENROLL).

Map any local finding(s) representing documentation of an historical start date for home telehealth.

1. VA-HT CCF FOLLOW-UP ASSESSMENT COMPLETED

This term is released with the health factor HT CCF FOLLOW-UP ASSESSMENT COMPLETED.

Map any local finding(s) representing completion of a follow-up home telehealth continuum of care assessment.

1. VA-HT CCF MEETS CHRONIC CARE MGMT CRITERIA

This term is released with the health factor HT CCF MEETS CHRONIC CARE MGMT CRITERIA.

Map any local finding(s) representing the Chronic Care Management criteria is met by the patient.

1. VA-HT CCF DOES NOT MEET CCM CRITERIA

This term is released with the health factor HT CCF DOES NOT MEET CCM CRITERIA. Map any local finding(s) representing the Chronic Care Management criteria is not met by the patient.

1. VA-HT PERIODIC EVALUATION COMPLETED

This term is released with the health factor HT PERIODIC EVALUATION COMPLETED. Map any local finding(s) representing the completion of the home telehealth periodic evaluation.

1. VA-HT CCF UNPAID CAREGIVER-YES

This term is released with the health factor HT CCF UNPAID CAREGIVER-YES. Map any local finding(s) representing the Veteran has an unpaid caregiver on file for the current HT enrollment.

1. VA-HT UNABLE TO SCREEN CAREGIVER

This term is released with the health factor HT UNABLE TO SCREEN CAREGIVER. Map any local finding(s) representing the inability to complete the Zarit caregiver risk Assessment.

1. VA-HT CAREGIVER RISK ASSESSMENT DONE

This term is released with the MH finding for the Zarit Caregiver Risk Assessment . Map any local finding(s) representing then completion of the Zarit caregiver risk Assessment.

1. Optional: Create a user class if your site wishes to restrict certain aspects TIU usage and/or implement business rules .

1. Create or edit folder in Shared Templates to house the HT Templates

PILOT SITES: Edit the name of your “CCHT TEMPLATES” folder in SHARED TEMPLATES to be "HT TEMPLATES".

NON-PILOT SITE:

1. Create a folder named “HT TEMPLATES” in the SHARED TEMPLATES section of the CPRS GUI Template Editor.

1. Create a GUI dialog in the HT TEMPLATES folder for the VA-HT TEMPLATE FOR PREVIOUSLY ENROLLED PATIENTS. This template will be linked to the HT NOTE title. This template is used to set historical data for HT patients so that the HT clinical reminders will be triggered appropriately.

1. When notified by the HT Lead, the CAC should remove the associated GUI template from service.

1. Extract the contents of the “HT\_TXML\_TEMPLATES.ZIP” file to a location of your choosing. From that location, import the two txml files (shown below) into the CPRS GUI Template Editor, into your PERSONAL templates.

1. HT MONTHLY MONITOR.TXML
2. HT PROVIDER CONSULT.TXML

1. Create GUI dialogs for the HT reminder dialogs in the DOCUMENT TITLES drawer and link these items to the associated note.
    1. HT ASSESSMENT TREATMENT PLAN TEMPLATE
    2. HT CAREGIVER ASSESSMENT TEMPLATE
    3. HT CONTINUUM OF CARE TEMPLATE
    4. HT DISCHARGE TEMPLATE
    5. HT INTERVENTION TEMPLATE
    6. HT PERIODIC EVALUATION TEMPLATE
    7. HT SCREENING CONSULT TEMPLATE
    8. HT TECH EDUCATION &amp; INSTALLATION TEMPLATE
    9. HT VIDEO VISIT TEMPLATE

1. Set the four new HT clinical reminders at the user level (yourself first) and verify that they launch (reminder dialogs linked) in the Reminders drawer. (They will be in the “All Evaluated” folder, no matter what the status is of each reminder for a patient.)

1. Create/edit the consult quick order to HOME TELEHEALTH ENROLLMENT OUTPT

1. Configure the two new Health Summary types for the CPRS GUI Reports tab.
2. Assign the new TIU and PXRM menu options to CAC(s) responsible for managing HT Clinical Reminders.

1. After testing all templates (the nine reminder dialogs [step #3] and the two TXML templates [step #2]), link them to note titles .

1. (optional) Change the frequency of the HT PERIODIC EVALUATION reminder if you wish to have a value other than the exported 180 days,
2. Build the five reminder report templates and do a sample run of each with a short date range.

###### After completing the above steps, we recommend the following:

- Preview the HOME TELEHEALTH SCREENING dialog to ensure that the two data objects are working without any errors.

- Review what your site does for the consult order to HT/Home Telehealth.

- PILOT SITES ONLY – Re-pointing of HEALTH FACTORS and/or EDUCATION TOPICS: All pilot sites will need to check to see if they need to go through a process with FileMan to replace the “CCHT” health factor and/or education topics entries in the associated files with the corresponding “HT” entries. See Appendix A “File Entry Delete and Pointer Update” for detailed explanation and steps. This same process/issue is applicable for the five new EDUCATION TOPICS included in the bundle. The post-install will handle any HT renaming as

long as the topics are installed at a low Internal Entry Number (IEN). If the IEN is high, the same manual re-pointing will need to occur.

“Low” and “high” refer to the number range associated with a given health factor. Each health factor in the file has an associated IEN. If the IEN is less than 100,000 this is considered “low” and is reserved for nationally released health factors. IENs greater than 100,000 are considered “high” and are health factors that have been created locally by the facility.

**Setup Instructions – Detailed Steps**

###### 13 Create a new user class in for your HT clinicians.

- will be linked to a note title of the same name (this is a text paragraph only and is non-interactive)

If your site wishes to restrict certain aspects of TIU usage or implement specific business rules pertaining to HT, then a new user class may be created for this purpose.

NOTE: your site may already have a user class called “HT NURSE” (for Home Telehealth Nurse), or HT NURSE, or HT CLINICIAN, or HT STAFF, because of an earlier Home Telehealth project called VistA Integration for Home Telehealth..

<!-- image -->

The documentation for that project (Home Telehealth Technical Installation Guide) is on the VDL (VistA Documentation Library) at [http://www4.va.gov/vdl/application.asp?appid=154](http://www4.va.gov/vdl/application.asp?appid=154) and the specific page that refers to user class is section #12 on page 14 of the Home Telehealth Technical Install Guide.

###### 14 Edit your “CCHT TEMPLATES” folder in SHARED TEMPLATES to be HT TEMPLATES.

Use your site’s naming conventions, and locate this folder according to your site’s conventions and where your HT clinicians will find it.

<!-- image -->

1. **Expand the HT\_TXML\_TEMPLATES.ZIP file to a known location. From that location, import the two .txml files into** the CPRS GUI Template Editor, into your PERSONAL templates **.**

1. HT MONTHLY MONITOR.TXML
2. HT PROVIDER CONSULT.TXML

###### 15 Create GUI dialogs for the HT reminder dialogs in the DOCUMENT TITLES drawer and follow the instructions for linking the dialogs to the correct note titles

- First, ensure that the TIU TEMPLATE REMINDER DIALOG parameter is set at the SYSTEM level for the HT reminder dialogs template. PXRM*2.0*19 tries to do this automatically during installation, but sometimes manual intervention is necessary.
    - Reminder Managers Menu [PXRM MANAGER]
        - CPRS Reminder Configuration
            - TIU Template Reminder Dialog Parameter

- Choose System and enter a ? at the Select Display Sequence prompt. This will show a list of all reminder dialogs that can be used as templates in CPRS GUI.

Reminder Dialogs allowed as Templates may be set for the following:

- Ensure all HT reminder dialogs are in this list. If not, add them.

| 1                                                                                                                                                                                                  | User         | User         | User         | USR                                       | [choose                                   | from                                      | NEW PERSON]                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|--------------|--------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|
| 2                                                                                                                                                                                                  | Team (OE/RR) | Team (OE/RR) | Team (OE/RR) | OTL                                       | [choose                                   | from                                      | OE/RR LIST]                               |
| 3                                                                                                                                                                                                  | Service      | Service      | Service      | SRV                                       | [choose                                   | from                                      | SERVICE/SECTION]                          |
| 4                                                                                                                                                                                                  | Division     | Division     | Division     | DIV                                       | [choose                                   | from                                      | INSTITUTION]                              |
| 5	System		SYS		[DVF.FO-SLC.MED.VA.GOV] Enter selection: 5	System	DVF.FO-SLC.MED.VA.GOV  Setting Reminder Dialogs allowed as Templates for System: ABC.SYSTEM.MED.VA.GOV Select Display Sequence: ? |              |              |              |                                           |                                           |                                           |                                           |
| Display Sequence                                                                                                                                                                                   |              |              | Value        |                                           |                                           |                                           |                                           |
| 51                                                                                                                                                                                                 | 51           |              | VA-HT        | ASSESSMENT TREATMENT PLAN TEMPLATE        | ASSESSMENT TREATMENT PLAN TEMPLATE        | ASSESSMENT TREATMENT PLAN TEMPLATE        | ASSESSMENT TREATMENT PLAN TEMPLATE        |
| 52                                                                                                                                                                                                 | 52           |              | VA-HT        | CAREGIVER ASSESSMENT TEMPLATE             | CAREGIVER ASSESSMENT TEMPLATE             | CAREGIVER ASSESSMENT TEMPLATE             | CAREGIVER ASSESSMENT TEMPLATE             |
| 53                                                                                                                                                                                                 | 53           |              | VA-HT        | CONTINUUM OF CARE TEMPLATE                | CONTINUUM OF CARE TEMPLATE                | CONTINUUM OF CARE TEMPLATE                | CONTINUUM OF CARE TEMPLATE                |
| 54                                                                                                                                                                                                 | 54           |              | VA-HT        | DISCHARGE TEMPLATE                        | DISCHARGE TEMPLATE                        | DISCHARGE TEMPLATE                        | DISCHARGE TEMPLATE                        |
| 55                                                                                                                                                                                                 | 55           |              | VA-HT        | INTERVENTION TEMPLATE                     | INTERVENTION TEMPLATE                     | INTERVENTION TEMPLATE                     | INTERVENTION TEMPLATE                     |
| 56                                                                                                                                                                                                 | 56           |              | VA-HT        | PERIODIC EVALUATION                       | PERIODIC EVALUATION                       | PERIODIC EVALUATION                       | PERIODIC EVALUATION                       |
| 57                                                                                                                                                                                                 | 57           |              | VA-HT        | SCREENING CONSULT TEMPLATE                | SCREENING CONSULT TEMPLATE                | SCREENING CONSULT TEMPLATE                | SCREENING CONSULT TEMPLATE                |
| 58                                                                                                                                                                                                 | 58           |              | VA-HT        | TECH EDUCATION & INSTALLATION TEMPLATE    | TECH EDUCATION & INSTALLATION TEMPLATE    | TECH EDUCATION & INSTALLATION TEMPLATE    | TECH EDUCATION & INSTALLATION TEMPLATE    |
| 59                                                                                                                                                                                                 | 59           |              | VA-HT        | TEMPLATE FOR PREVIOUSLY ENROLLED PATIENTS | TEMPLATE FOR PREVIOUSLY ENROLLED PATIENTS | TEMPLATE FOR PREVIOUSLY ENROLLED PATIENTS | TEMPLATE FOR PREVIOUSLY ENROLLED PATIENTS |
| 60                                                                                                                                                                                                 | 60           |              | VA-HT        | VIDEO VISIT TEMPLATE                      | VIDEO VISIT TEMPLATE                      | VIDEO VISIT TEMPLATE                      | VIDEO VISIT TEMPLATE                      |

- Next, go to DOCUMENT TITLES in the CPRS GUI Template Editor.
- Create a new HT TITLES folder in the DOCUMENT TITLES drawer.
- One at a time, create a NEW TEMPLATE for each of these templates in the HT TITLES folder:

HT ASSESSMENT TREATMENT PLAN template HT CAREGIVER ASSESSMENT template

HT CONTINUUM OF CARE template HT DISCHARGE template

HT INTERVENTION template

HT PERIODIC EVALUATION template

HT SCREENING CONSULT template HT TECH EDUCATION template

HT VIDEO VISIT template

- To link a reminder template to a note title, select the template from the ‘reminder dialog’ picklist, and then select the note title in the ‘associated title’ field. This example is shown using the HT Caregiver Assessment.

<!-- image -->

- When you click the APPLY button, the template name will change to upper-case and take on the name of the note title:
<!-- image -->

The HT templates all have the same name as the note title. The CPRS GUI template link uses the

.01-NAME field in the ‘associated title’ field

When done, your list of linked templates to note titles should look like this (9 reminder dialog templates and 1 text template):

<!-- image -->

| **TITLE (.01 NAME)**              | **HAS TEMPLATE**   |
|-----------------------------------|--------------------|
| HT ASSESSMENT TREATMENT PLAN NOTE | YES (RD)           |
| HT CAREGIVER ASSESSMENT NOTE      | YES (RD)           |
| HT CONTINUUM OF CARE NOTE         | YES (RD)           |
| HT DISCHARGE NOTE                 | YES (RD)           |
| HT INTERVENTION NOTE              | YES (RD)           |
| HT NOTE                           | NO                 |
| HT PERIODIC EVALUATION NOTE       | YES (RD)           |
| HT SCREENING CONSULT              | YES (RD)           |
| HT SUMMARY OF EPISODE NOTE        | YES (TXML)         |
| HT TECH EDUCATION NOTE            | YES (RD)           |
| HT TELEPHONE CASE MANAGEMENT NOTE | NO                 |
| HT VIDEO VISIT NOTE               | YES (RD)           |

RD = Reminder Dialog

1. **Verify that the four new HT clinical reminders launch (reminder dialogs linked) from the Reminders drawer.** (They will be in the “All Evaluated” folder, no matter what the status is of each reminder for a patient.) You may choose to either add the four reminders for yourself at the User level or, you could add yourself to the user class referenced in step #1 and then turn on the reminders for the member of that user class.

Do not add the VA-HT CONTINUUM OF CARE (INITIAL) to any level for now. Additional logic will be added to this reminder and sent in an PXRM update later.

###### Turning on the four new HT Clinical Reminders for users:

Click the alarm clock or "?" in the CPRS GUI header, then click on ACTION, then “EDIT COVER SHEET REMINDER LIST”:

When the next window appears, select level = USER CLASS and HT STAFF for the user class, Use the  to move the HT reminders from the LOWER LEFT window (active reminders) to the LOWER RIGHT window so that they are configured for the USER CLASS. Then set the padlock on each one to lock this reminder configuration.

Do not add the VA-HT CONTINUUM OF CARE (INITIAL) to

any level for now. Additional logic will be added to this reminder and sent in an PXRM update later.

The four new HT clinical reminders can be found in the “ALL EVALUATED” folder for any patient. Preview each one of them to ensure the reminder dialog loads.

###### 16 Create/edit the consult quick order to HOME TELEHEALTH ENROLLMENT OUTPT:

Use your site’s naming convention and following VHA Consult Business Rules. OCC recommends creating a HOME TELEHEALTH ENROLLMENT OUTPT sub-service under CARE COORDINATION HOME TELEHEALTH SCREENING*. If you already have a

quick order to CARE COORDINATION HOME TELEHEALTH SCREENING, you can review your configuration (others may have to create a new quick order). **Reminder: The consult service CARE COORDINATION HOME TELEHEALTH SCREENING**

###### cannot be renamed as other VistA software depends on the presence of that exact name.

QO	Enter/edit quick orders

Select QUICK ORDER NAME: **GMRCT HOME TELEHEALTH ENROLLMENT**

Are you adding 'GMRCT HOME TELEHEALTH ENROLLMENT' as a new ORDER DIALOG? No// Y (Yes)

TYPE OF QUICK ORDER: **CONSULTS**

NAME: GMRCT HOME TELEHEALTH ENROLLMENT Replace

DISPLAY TEXT: **Home Telehealth Enrollment Consult**

VERIFY ORDER: **y** YES DESCRIPTION:

No existing text Edit? NO// **&lt;ENTER&gt;**

Consult to Service/Specialty: **HOME TELEHEALTH ENROLLMENT OUTPT**

Consult Type:

Reason for Request:

Initial Screening for Home Telehealth services. Edit? No// y	(Yes)

==[ WRAP ]==[ INSERT ]=========&lt; Reason for Request &gt;========[ &lt;PF1&gt;H=Help ]==

&lt;=======T=======T=======T=======T=======T=======T=======T=======T=======T&gt;====

Category:

Urgency: ROUTINE//

Place of Consultation: CONSULTANT'S CHOICE Attention:

Provisional Diagnosis:

Consult to Service/Specialty: HOME TELEHEALTH ENROLLMENT OUTPT

Urgency: ROUTINE

Place of Consultation: Consultant's Choice

(P)lace, (E)dit, or (C)ancel this quick order? PLACE// Auto-accept this order? NO//

***** Set CARE COORDINATION HOME TELEHEALTH SCREENING service’s Service

Usage to Grouper Only and then create the HOME TELEHEALTH ENROLLMENT OUTPT service as a sub-service of CARE COORDINATION HOME TELEHEALTH SCREENING. Reference the Consult/Request Tracking User Manual if you need explicit instructions for editing/creating consult services. [(http://www.va](http://www.va.gov/vdl)) . [gov/vdl)](http://www.va.gov/vdl))

###### Linking the consult request template to the HOME TELEHEALTH ENROLLMENT OUTPT consult service

- Go into the GUI Template Editor to EDIT Shared Templates, and select the CONSULTS drawer:

- Copy the HT PROVIDER CONSULT GUI dialog template imported in Step #3 into the CONSULT REASONS FOR REQUEST folder. LINK the HT consult service to the template in the 'associated consult service' field. Click APPLY and note that the GUI dialog template name will change to match that of the associated consult service.

<!-- image -->

<!-- image -->

- Make sure that this consult quick order is on an order menu for your ordering providers when you are ready to begin the pilot. Launch this quick order from a menu as a verification step, so that you are assured that the template loads and the order is working.

###### 17 Configure two new Health Summary types for the CPRS GUI Reports tab.

- Follow your facility’s rules and conventions for configuring these health summary types.
- Sequencing new Health Summary types is done in the GUI Parameters option.

|   2 | User   | USR   | [choose from NEW PERSON]   |
|-----|--------|-------|----------------------------|
|   4 | System | SYS   | [PUGET-SOUND.MED.VA.GOV]   |

Select CPRS Manager Menu Option: **PE** CPRS Configuration (Clin Coord) Select CPRS Configuration (Clin Coord) Option: **GP** GUI Parameters Select GUI Parameters Option: **HS** GUI Health Summary Types

Allowable Health Summary Types may be set for the following:

Enter selection: **4** System	xxx.MED.VA.GOV

- Setting Allowable Health Summary Types for System: PUGET-SOUND.MED.VA.GOV - Sequence: 20//

Health Summary: REMOTE **HT TRACKING**

Sequence: 21//

*(your sequence numbers will be different)*

Health Summary: REMOTE **HT CLINICAL REMINDERS**

###### 18 Assign the TIU HT MENU and (optional) PXRM HT DEFINITION EDIT to CAC(s).

- Use Menu Management options to assign TIU HT MENU to the CAC(s) responsible for managing Home Telehealth Documents and/or Clinical Reminders. Depending on your facility’s IT support structure, this may be handled at a facility level or by Regional IT support.

###### 19 Link the HT templates to NOTE TITLES (after making sure that the nine reminder dialogs and two TXML templates are tested and ready to go).

- Go to DOCUMENT TITLES in the CPRS GUI Template Editor.
- Create a new HT TITLES folder in the DOCUMENT TITLES drawer.
- One at a time, create a NEW TEMPLATE for each of these templates in the HT TITLES folder:

HT ASSESSMENT TREATMENT PLAN template HT CAREGIVER ASSESSMENT template

HT CONTINUUM OF CARE template HT DISCHARGE template

HT INTERVENTION template

HT PERIODIC EVALUATION template

HT SCREENING CONSULT template

HT TECH EDUCATION template HT VIDEO VISIT template

- To link a reminder template to a note title, select the template from the ‘reminder dialog’ picklist, and then select the note title in the ‘associated title’ field. This example is shown using the HT Caregiver Assessment.
<!-- image -->
- When you click the APPLY button, the template name will change to upper-case and take on the name of the note title:
<!-- image -->

The HT templates all have the same name as the note title. The CPRS GUI template link uses the

.01-NAME field in the ‘associated title’ field

When done, your list of linked templates to note titles should look like this (9 reminder dialog templates and 1 text template):

<!-- image -->

| **TITLE (.01 NAME)**              | **HAS TEMPLATE**   |
|-----------------------------------|--------------------|
| HT ASSESSMENT TREATMENT PLAN NOTE | YES (RD)           |
| HT CAREGIVER ASSESSMENT NOTE      | YES (RD)           |
| HT CONTINUUM OF CARE NOTE         | YES (RD)           |
| HT DISCHARGE NOTE                 | YES (RD)           |
| HT INTERVENTION NOTE              | YES (RD)           |
| HT NOTE                           | NO                 |
| HT PERIODIC EVALUATION NOTE       | YES (RD)           |
| HT SCREENING CONSULT              | YES (RD)           |
| HT SUMMARY OF EPISODE NOTE        | YES (TXML)         |
| HT TECH EDUCATION NOTE            | YES (RD)           |
| HT TELEPHONE CASE MANAGEMENT NOTE | NO                 |
| HT VIDEO VISIT NOTE               | YES (RD)           |

RD = Reminder Dialog

1. **(Optional for all sites) If you need to change the FREQUENCY of the HT PERIODIC EVALUATION.** (This example uses 180 days – set the frequency to whatever time period is needed at your site.)

List Reminder Definitions

Inquire about Reminder Definition Add/Edit Reminder Definition

Copy Reminder Definition Activate/Inactivate Reminders

Edit HT PERIODIC Reminder Definition Frequency Reminder Edit History

Integrity Check Selected Integrity Check All

RL RI RE RC RA HT RH ICS ICA

Select Reminder Definition Management &lt;TEST ACCOUNT&gt; Option: HT	Edit HT PERIODIC Reminder Definition Frequency

The current frequency for this reminder definition is: 180D Enter a new REMINDER FREQUENCY: 180D// **???**

Choose one of the following frequencies for this reminder definition: 90D (or 3M), 120D (or 4M), 180D (or 6M)

The current frequency for this reminder definition is: 180D Enter a new REMINDER FREQUENCY: 180D// **90D**

Done

###### 20 Build the 5 reminder report templates and do sample runs of each, with a short date range.

HT CCF INITIAL

HT CCF FOLLOW-UP HT C/G ASSESSMENT

HT PERIODIC EVALUATION

CREATING THE NEW HT CATEGORY (this should be done first, before starting to build the 5 report templates) (used in the (5) REMINDERS SUMMARY’)

HT (4) REMINDERS SUMMARY

###### 11a. Example: CREATING THE HT CCF INITIAL reminder report template

Combined report for all Facilities : N// YES

347

ID

Select another FACILITY: BOISE-RO Select another FACILITY:

531

Select FACILITY: Boise, ID

Select Reminder Managers Menu Option: RP	Reminder Reports Select Reminder Reports Option: d	Reminders Due Report Select an existing REPORT TEMPLATE or return to continue:

Select one of the following:

I	Individual Patient

R	Reminder Patient List

L	Location

1. OE/RR Team
2. PCMM Provider

T	PCMM Team

PATIENT SAMPLE: L// l	Location

Select one of the following:

HA	All Outpatient Locations

HAI	All Inpatient Locations

HS	Selected Hospital Locations

CA	All Clinic Stops(with encounters) CS	Selected Clinic Stops

GS	Selected Clinic Groups

Determine encounter counts for: HS// CS	Selected Clinic Stops

Select CLINIC STOP: 179	HOME TELEVIDEO CARE

Select another CLINIC STOP: 371	HT SCREENING

Select another CLINIC STOP: 683	HT NON-VIDEO MONITORING Select another CLINIC STOP: 684	HT NON-VIDEO INTRVNTION Select another CLINIC STOP: 685	CARE OF HT PROGRAM PATIENTS Select another CLINIC STOP: 686	PHONE CONTACT BY CC STAFF

Select another CLINIC STOP:

Select one of the following:

P	Previous Encounters

F	Future Appointments

PREVIOUS ENCOUNTERS OR FUTURE APPOINTMENTS: P// Previous Encounters

Enter ENCOUNTER BEGINNING DATE:		T-30	(MAY 31, 2009) Enter ENCOUNTER ENDING DATE: T	(JUN 30, 2009)

Enter EFFECTIVE DUE DATE: Jun 30, 2009//	(JUN 30, 2009)

Select SERVICE CATEGORIES: A,I// ?

The possible service categories for the report are: A	AMBULATORY

1. HOSPITALIZATION
2. IN HOSPITAL

C	CHART REVIEW

T	TELECOMMUNICATIONS

N	NOT FOUND

S	DAY SURGERY

O	OBSERVATION

E	EVENT (HISTORICAL)

R	NURSING HOME

D	DAILY HOSPITALIZATION DATA

X	ANCILLARY PACKAGE DAILY DATA

Select SERVICE CATEGORIES: A,I// **A,H,I,T,E,R**

Select one of the following:

D	Detailed

S	Summary

TYPE OF REPORT: S// Detailed

Combined report for all Clinic Stops : N// YES

Display All Future Appointments: N// O

Sort by Next Appointment date: N// O

Print full SSN: N// O

Building Hospital Locations List Done

Elapsed time for building hospital locations: 0 secs Building patient listDone

Elapsed time for building patient list: 0 secs

Calling the scheduling package to gather appointment data | Elapsed time for call to the Scheduling Package: 0 secs

Sorting SDAMA301 Output Done

Elapsed time for sorting SDAMA301 output: 0 secs

Elapsed time for removing invalid encounter(s): 0 secDone

Elapsed time for reminder evaluation: 0 secs done

Create a new report template: N// YES

STORE REPORT LOGIC IN TEMPLATE NAME: HT CCF INITIAL

Are you adding 'HT CCF INITIAL' as

a new REMINDER REPORT TEMPLATE (the 200TH)? No// Y	(Yes) REMINDER REPORT TEMPLATE REPORT TITLE: HT CCF Initial

**Changes to template 'HT CCF INITIAL' have been saved**

*&lt;&lt;&lt; this part is just the running of the report with the new template &gt;&gt;*

Print delimited output only: N// O

Include deceased patients on the list? N// O Include test patients on the list? N// O Save due patients to a patient list: N// O

DEVICE: HOME// ;80;9999	HOME	(CRT)

VISN

Print locations with no patients? YES// NO

Select individual REMINDER: HT CONTINUUM OF CARE (INITIAL)

###### 11b. Example: CREATING THE HT CCF FOLLOW-UP reminder report template

Select Reminder Reports Option:	Reminders Due Report Select an existing REPORT TEMPLATE or return to continue:

Select one of the following:

I	Individual Patient

R	Reminder Patient List

L	Location

1. OE/RR Team
2. PCMM Provider

T	PCMM Team

PATIENT SAMPLE: L// l	Location Select FACILITY: Boise, ID	531

Select another FACILITY: BOISE-RO	ID	347

Select another FACILITY:

Combined report for all Facilities : N// YES Select one of the following:

HA	All Outpatient Locations

HAI	All Inpatient Locations

HS	Selected Hospital Locations

CA	All Clinic Stops(with encounters) CS	Selected Clinic Stops

GS	Selected Clinic Groups

Determine encounter counts for: HS// CS	Selected Clinic Stops

Select CLINIC STOP: 179	HOME TELEVIDEO CARE

Select another CLINIC STOP: 371	HT SCREENING

Select another CLINIC STOP: 683	HT NON-VIDEO MONITORING Select another CLINIC STOP: 684	HT NON-VIDEO INTRVNTION Select another CLINIC STOP: 685	CARE OF HT PROGRAM PATIENTS Select another CLINIC STOP: 686	PHONE CONTACT BY CC STAFF

Select another CLINIC STOP:

Select one of the following:

P	Previous Encounters

F	Future Appointments

PREVIOUS ENCOUNTERS OR FUTURE APPOINTMENTS: P// Previous Encounters

Enter ENCOUNTER BEGINNING DATE:		T-30	(MAY 31, 2009) Enter ENCOUNTER ENDING DATE: T	(JUN 30, 2009)

Enter EFFECTIVE DUE DATE: Jun 30, 2009//	(JUN 30, 2009)

Select SERVICE CATEGORIES: A,I// A,H,I,T,E,R

Select one of the following: D	Detailed

S	Summary

TYPE OF REPORT: S// Detailed

Combined report for all Clinic Stops : N// YES Display All Future Appointments: N// O

Sort by Next Appointment date: N// O Print full SSN: N// O

Print locations with no patients? YES// NO

Select individual REMINDER: HT CONTINUUM OF CARE (FOLLOW-UP)	VISN

Create a new report template: N// YES

###### 11c. Example: CREATING THE HT CAREGIVER ASSESSMENT reminder report template

Select Reminder Reports Option:	Reminders Due Report

Select an existing REPORT TEMPLATE or return to continue: Select one of the following:

I	Individual Patient

R	Reminder Patient List

L	Location

1. OE/RR Team
2. PCMM Provider

T	PCMM Team

PATIENT SAMPLE: L// l	Location

Select FACILITY: Boise, ID

531

Select another FACILITY: BOISE-RO Select another FACILITY:

ID

347

TYPE OF REPORT: S// Detailed

Combined report for all Clinic Stops : N// YES Display All Future Appointments: N// O

Sort by Next Appointment date: N// O Print full SSN: N// O

Print locations with no patients? YES// NO

Select individual REMINDER: HT CAREGIVER ASSESSMENT	VISN

Create a new report template: N// YES

STORE REPORT LOGIC IN TEMPLATE NAME: HT CAREGIVER ASSESSMENT

Are you adding 'HT CAREGIVER ASSESSMENT' as

a new REMINDER REPORT TEMPLATE (the 202ND)? No// Y	(Yes)

REMINDER REPORT TEMPLATE REPORT TITLE: HT Caregiver Assessment Changes to template 'HT CAREGIVER ASSESSMENT' have been saved

Print delimited output only: N// O

Include deceased patients on the list? N// O Include test patients on the list? N// O Save due patients to a patient list: N// O DEVICE: HOME// ;80;9999	HOME	(CRT)

Building Hospital Locations List Done

Elapsed time for building hospital locations: 0 secs Building patient listDone

Elapsed time for building patient list: 0 secs

Calling the scheduling package to gather appointment data | Elapsed time for call to the Scheduling Package: 0 secs Sorting SDAMA301 Output Done

Elapsed time for sorting SDAMA301 output: 0 secs

Elapsed time for removing invalid encounter(s): 0 secDone Elapsed time for reminder evaluation: 0 secs	done

No patient visits found

Report timing data:

Elapsed time for building hospital locations: 0 secs Elapsed time for building patient list: 0 secs Elapsed time for reminder evaluation: 0 secs

Elapsed time for removing invalid encounter(s): 0 secs Elapsed time for sorting SDAMA301 output: 0 secs Elapsed time for call to the Scheduling Package: 0 secs

End of the report. Press ENTER/RETURN to continue...

###### 11d. Example: CREATING THE HT PERIODIC EVALUATION reminder report template

Combined report for all Facilities : N// YES Select one of the following:

HA	All Outpatient Locations

HAI	All Inpatient Locations

HS	Selected Hospital Locations

CA	All Clinic Stops(with encounters) CS	Selected Clinic Stops

GS	Selected Clinic Groups

Determine encounter counts for: HS// CS	Selected Clinic Stops Select CLINIC STOP: 179	HOME TELEVIDEO CARE

Select another CLINIC STOP: 371	HT SCREENING

Select another CLINIC STOP: 683	HT NON-VIDEO MONITORING Select another CLINIC STOP: 684	HT NON-VIDEO INTRVNTION Select another CLINIC STOP: 685	CARE OF HT PROGRAM PATIENTS Select another CLINIC STOP: 686	PHONE CONTACT BY CC STAFF

Select another CLINIC STOP:

Select one of the following:

P	Previous Encounters

F	Future Appointments

PREVIOUS ENCOUNTERS OR FUTURE APPOINTMENTS: P// Previous Encounters Enter ENCOUNTER BEGINNING DATE:	T-30	(MAY 31, 2009)

Enter ENCOUNTER ENDING DATE: T	(JUN 30, 2009)

Enter EFFECTIVE DUE DATE: Jun 30, 2009//	(JUN 30, 2009)

347

ID

Select another FACILITY: BOISE-RO Select another FACILITY:

531

Select FACILITY: Boise, ID

Select Reminder Reports Option:	Reminders Due Report

Select an existing REPORT TEMPLATE or return to continue: Select one of the following:

I	Individual Patient

R	Reminder Patient List

L	Location

1. OE/RR Team
2. PCMM Provider

T	PCMM Team

PATIENT SAMPLE: L// l	Location

Select SERVICE CATEGORIES: A,I// A,H,I,T,E,R

Select one of the following: D	Detailed

S	Summary

TYPE OF REPORT: S// Detailed

Combined report for all Clinic Stops : N// YES Display All Future Appointments: N// O

Sort by Next Appointment date: N// O Print full SSN: N// O

Print locations with no patients? YES// NO

Select individual REMINDER: HT PERIODIC EVALUATION	VISN Create a new report template: N// YES

STORE REPORT LOGIC IN TEMPLATE NAME: HT PERIODIC EVALUATION

Are you adding 'HT PERIODIC EVALUATION' as

a new REMINDER REPORT TEMPLATE (the 204TH)? No// Y	(Yes) REMINDER REPORT TEMPLATE REPORT TITLE: HT Periodic Evaluation

Changes to template 'HT PERIODIC EVALUATION' have been saved

Print delimited output only: N// O

Include deceased patients on the list? N// O Include test patients on the list? N// O Save due patients to a patient list: N// O DEVICE: HOME// ;80;9999	HOME	(CRT)

Building Hospital Locations List Done

Elapsed time for building hospital locations: 0 secs Building patient listDone

Elapsed time for building patient list: 0 secs

Calling the scheduling package to gather appointment data | Elapsed time for call to the Scheduling Package: 0 secs Sorting SDAMA301 Output Done

Elapsed time for sorting SDAMA301 output: 0 secs

Elapsed time for removing invalid encounter(s): 0 secDone Elapsed time for reminder evaluation: 0 secs	done

Jun 30, 2009 6:23:48 pm	Page 1

Clinical Reminders Due Report - Detailed Report Report Title: HT Periodic Evaluation

Patient Sample: Location

Location:	Selected Clinic Stops (Prior Encounters) HOME TELEVIDEO CARE 179

HT NON-VIDEO MONITORING 683 HT NON-VIDEO INTRVNTION 684 HT SCREENING 371

CARE OF HT PROGRAM PATIENTS 685 PHONE CONTACT BY CC STAFF 686

Reminder:	HT PERIODIC EVALUATION

Appointments:	Next Appointment only

Date Range:	5/31/2009 to 6/30/2009 Effective Due Date:	6/30/2009

Date run:	6/30/2009 6:22:43 pm Template Name:	HT PERIODIC EVALUATION

Combined report: Combined Facility and Combined Locations Service categories: A,H,I,T,E,R

A - AMBULATORY

H - HOSPITALIZATION I - IN HOSPITAL

T - TELECOMMUNICATIONS E - EVENT (HISTORICAL)

R - NURSING HOME

No patient visits found Report timing data:

Elapsed time for building hospital locations: 0 secs Elapsed time for building patient list: 0 secs Elapsed time for reminder evaluation: 0 secs

Elapsed time for removing invalid encounter(s): 0 secs Elapsed time for sorting SDAMA301 output: 0 secs Elapsed time for call to the Scheduling Package: 0 secs

End of the report. Press ENTER/RETURN to continue...

###### 11e. Example CREATING THE NEW HT CATEGORY - 4 HT CLINICAL REMINDERS

Select Reminder Managers Menu Option: cp	CPRS Reminder Configuration Select CPRS Reminder Configuration Option: ?

CA	Add/Edit Reminder Categories CL	CPRS Lookup Categories

CS	CPRS Cover Sheet Reminder List MH	Mental Health Dialogs Active PN	Progress Note Headers

RA	Reminder GUI Resolution Active

TIU	TIU Template Reminder Dialog Parameter DL	Default Outside Location

PT	Position Reminder Text at Cursor NP	New Reminder Parameters

GEC	GEC Status Check Active WH	WH Print Now Active

Select CPRS Reminder Configuration Option: **CA Add/Edit Reminder Categories**

Selection List	Jun 30, 2009@19:02:05	Page:	1 of	1

Reminder Categories Item Reminder Category

1. CHRONIC DISEASE
2. DEPRESSION

11	VISN PC MEASURES FY09

+ Next Screen	- Prev Screen	?? More Actions	&gt;&gt;&gt;                   AD	Add	PT	List/Print All	QU	Quit

Select Item: Quit// **AD** Add

Select new REMINDER CATEGORY name: HT

Are you adding 'HT2' as a new REMINDER CATEGORY (the 12TH)? No// y	(Yes)

NAME: HT// DESCRIPTION:

No existing text Edit? NO// y	YES

==[ WRAP ]==[ INSERT ]=============&lt; DESCRIPTION &gt;===========[ &lt;PF1&gt;H=Help ]====

4 HT (Home Telehealth) reminders

&lt;=======T=======T=======T=======T=======T=======T=======T=======T=======T&gt;======

Select INDIVIDUAL REMINDERS: HT CONTINUUM OF CARE (INITIAL)	VISN

Are you adding 'HT CONTINUUM OF CARE (INITIAL)' as

a new INDIVIDUAL REMINDERS (the 1ST for this REMINDER CATEGORY)? No// Y	(Yes) DISPLAY ORDER: 1

Select INDIVIDUAL REMINDERS: HT CONTINUUM OF CARE (FOLLOW-UP)	VISN Are you adding 'HT CONTINUUM OF CARE (FOLLOW-UP)' as

a new INDIVIDUAL REMINDERS (the 2ND for this REMINDER CATEGORY)? No// Y	(Yes) DISPLAY ORDER: 2

Select INDIVIDUAL REMINDERS: HT CAREGIVER ASSESSMENT	VISN

Are you adding 'HT CAREGIVER ASSESSMENT' as

a new INDIVIDUAL REMINDERS (the 3RD for this REMINDER CATEGORY)? No// Y	(Yes) DISPLAY ORDER: 3

Select INDIVIDUAL REMINDERS: HT CAREGIVER/VETERAN REFERRAL	VISN Select INDIVIDUAL REMINDERS: HT PERIODIC EVALUATION	VISN

###### 11f: Example: CREATING THE REMINDER REPORT TEMPLATE THAT IS A

**SUMMARY REPORT OF THE (4) HT REMINDERS** (Here’s where you use the HT ‘category’)

Select

Reminder Reports	&lt;PUG TST&gt; Option: d	Reminders Due Report

Select an existing REPORT TEMPLATE or return to continue: Select one of the following:

I	Individual Patient

R	Reminder Patient List

L	Location

1. OE/RR Team
2. PCMM Provider

T	PCMM Team

PATIENT SAMPLE: L// l	Location

Select FACILITY: PUGET SOUND HCS/

Select another FACILITY:

Select one of the following:

HA	All Outpatient Locations

HAI	All Inpatient Locations

HS	Selected Hospital Locations

CA	All Clinic Stops(with encounters) CS	Selected Clinic Stops

GS	Selected Clinic Groups

Determine encounter counts for: HS// &lt;ENT&gt; LOCATION: HT NON VIDEO INTERVENTION

Select another LOCATION: &lt;Enter all your HT clinic locations until done&gt;&gt;

Select one of the following:

P	Previous Encounters

F	Future Appointments

PREVIOUS ENCOUNTERS OR FUTURE APPOINTMENTS: P// revious Encounters

Enter ENCOUNTER BEGINNING DATE:	3/1/10	(MAR 01, 2010) Enter ENCOUNTER ENDING DATE: 3/5/10	(MAR 05, 2010)

Enter EFFECTIVE DUE DATE: May 24, 2010//	(MAY 24, 2010)

Select SERVICE CATEGORIES: A,I//

Select one of the following: D	Detailed

S	Summary

TYPE OF REPORT: S// ummary

Print locations with no patients? YES// n	NO

Print percentages with the report output? NO// y	YES Select a REMINDER CATEGORY: HT

...OK? Yes//	(Yes)

Select another REMINDER CATEGORY: &lt;ENT&gt; Select individual REMINDER: &lt;ENT&gt;

Create a new report template: N// y	YES

STORE REPORT LOGIC IN TEMPLATE NAME: HT (4) REMINDERS,SUMMARY

Are you adding 'HT (4) REMINDERS,SUMMARY' as

a new REMINDER REPORT TEMPLATE (the 235TH)? No// Y	(Yes)

REMINDER REPORT TEMPLATE REPORT TITLE: HT 4 reminders summary

**Changes to template 'HT (4) REMINDERS,SUMMARY' have been saved**

Print delimited output only: N// O

Include deceased patients on the list? N// O Include test patients on the list? N// O Save due patients to a patient list: N// O

DEVICE: HOME// ;80;9999	HOME	(CRT)

Building hospital locations list |

Elapsed time for building hospital locations list: 0 secs

Building patient list |

Elapsed time for building patient list: 0 secs  Elapsed time for removing invalid encounter(s): 0 secs Elapsed time for reminder evaluation: 0 secs

May 24, 2010 11:49:19 am	Page 1

Clinical Reminders Due Report - Summary Report Report Title:	HT 5 reminders summary

Patient Sample:	Location

Location:	Selected Hospital Locations (Prior Encounters)

HT/HBPC TELEPHONE

Reminder Category:	HBPC

Date Range:	3/1/2010 to 3/5/2010 Effective Due Date:	5/24/2010

Date run:	5/24/2010 11:46:29 am Template Name:	HT (4) REMINDERS,SUMMARY

Summary report:	Individual Locations only Service categories:	A,I

A - AMBULATORY I - IN HOSPITAL

###### 11g. Example: GRANT ACCESS TO THE REMINDER REPORT TEMPLATES TO YOURSELF AND YOUR HT SITE LEAD

**11h. Example: RUNNING THE REMINDER REPORT TEMPLATES**

Select Reminder Reports Option: DRU	Reminders Due Report (User)

Select REPORT TEMPLATE:HT

1. HT (5) REMINDERS SUMMARY	HT (5) Reminders - Summary
2. HT C/G RISK ASSESSMENT	HT Caregiver Risk Assessment
3. HT CONT OF CARE (F/U)	HT Continuum of Care (F/U)
4. HT CONT OF CARE (INITIAL)	HT Continuum of Care (Initial) Press &lt;RETURN&gt; to see more, '^' to exit this list, OR

CHOOSE 1-5: 5	HT CONT OF CARE (INITIAL)	HT Continuum of Care (Initial)

**Appendix A: File Entry Delete and Pointer Update**

**OVERVIEW**

**This procedure is only** ***potentially*** **necessary at sites that participated in the CCHT pilot program.**

The following is an example of how to delete a HEALTH FACTORS file entry and then update any pointers to a new entry. This same procedure can be used to delete and update any local EDUCATION TOPICS file entries.

If you are a CCHT pilot site, you can determine the need to follow this procedure by examining the entries in the HEALTH FACTORS and EDUCATION TOPICS files. PXRM*2.0*19 exports entries to both of those files. Internal Entry Numbers (IENs) less than 100,000 in these files are intended for National entries. During installation, if the “CCHT” health factors and “HOME TELEHEALTH” education topics are found at IENs &lt; 100,000, the patch will rename these entries to “HT…” for health factors and “VA-HOME TELEHEALTH…” for education topics. If these entries are found to be at IENs &gt; 100,000 (i.e. Local), PXRM*2.0*19 will install new National entries at low IENs and your site will need to perform the delete/pointer update process below.

###### WARNING! A LOCAL “CCHT” HEALTH FACTOR OR EDUCATION TOPIC SHOULD ONLY BE DELETED AND HAVE POINTERS UPDATED AFTER CONFIRMING THAT THE LOCAL “CCHT” HEALTH FACTOR HAS BEEN SUPERSEDED BY A NATIONAL “HT” HEALTH FACTOR.

The process described below involves using FileMan to delete entries in a given file, and subsequently updating any other files that pointed to the deleted entry to now point to a new entry. This is a manual process and is not technically possible to be automatically performed as part of a post-install routine.

**EDUCATION TOPICS**

Check to see if the education topics exported in the reminder exchange file have been installed at national IENs and if any local education topics need to be replaced.

Perform a FileMan search of the EDUCATION TOPICS file. Look for topics that have “HOME TELEHEALTH” in the NAME. Output the NAME and NUMBER. If an education topic has a “VA-“ entry at an IEN of less than 100,000 AND a non “VA-“ entry then that non “VA-“ entry is a candidate for the delete and re-point process.

Enter or Edit File Entries Print File Entries

Search File Entries Modify File Attributes Inquire to File Entries Utility Functions ...

Data Dictionary Utilities ... Transfer Entries

Other Options ...

Select VA FileMan &lt;TEST ACCOUNT&gt; Option: **search File Entries**

OUTPUT FROM WHAT FILE: **EDUCATION TOPICS//**

-A- SEARCH FOR EDUCATION TOPICS FIELD: **NAME**

-A- CONDITION: **CONTAINS**

-A- CONTAINS: **HOME TELEHEALTH**

-B- SEARCH FOR EDUCATION TOPICS FIELD:

IF: **A//** NAME CONTAINS (case-insensitive) "HOME TELEHEALTH" STORE RESULTS OF SEARCH IN TEMPLATE:

SORT BY: **NAME//**

START WITH NAME: **FIRST//** FIRST PRINT FIELD: **NAME** THEN PRINT FIELD: **NUMBER** THEN PRINT FIELD:

Heading (S/C): EDUCATION TOPICS SEARCH	Replace DEVICE: ;;9999	HOME

EDUCATION TOPICS SEARCH	MAR 20,2013	07:51	PAGE 1 NAME

NUMBER

VA-HOME TELEHEALTH (HT) 37

VA-HOME TELEHEALTH-CAREGIVER EDUCATION/SUPPORT 19

VA-HOME TELEHEALTH-DISEASE MGMT/PATIENT SELF-MGMT 21

VA-HOME TELEHEALTH-IN HOME MONITORING 18

VA-HOME TELEHEALTH-MEDICATION MANAGEMENT 20

In this sample search, only the VA-HOME TELEHEALTH education topics are present. If a search result returned a local entry of HOME TELEHEALTH IN HOME MONITORING at IEN 660124, that entry would be a candidate for being deleted from EDUCATION TOPICS and any pointers should be updated to point to the national entry, VA-HOME TELEHEALTH IN HOME MONITORING. Refer to the document “File Entry Delete and Pointer Update” for details of this process.

**HEALTH FACTORS**

Check to see if the health factors exported in the reminder exchange file have been installed at national IENs and if any local health factors need to be replaced.

Perform a FileMan search of the HEALTH FACTORS file. Look for health factors that have “HT ” in the FACTOR field. Output the FACTOR and NUMBER. If a health factor has an “HT “ entry at an IEN of less than 100,000 AND a “CCHT “ entry, then that “CCHT ” entry is a candidate for the delete and re-point process.

Select VA FileMan &lt;TEST ACCOUNT&gt; Option: **Search File Entries**

OUTPUT FROM WHAT FILE: EDUCATION TOPICS// **HEALTH FACTORS**

(3440 entries)

-A- SEARCH FOR HEALTH FACTORS FIELD: **FACTOR**

-A- CONDITION: **CONTAINS**

-A- CONTAINS: **HT NOTE: type a space after the T**

-B- SEARCH FOR HEALTH FACTORS FIELD:

IF: **A** FACTOR CONTAINS (case-insensitive) "HT " STORE RESULTS OF SEARCH IN TEMPLATE:

SORT BY: **FACTOR//**

START WITH FACTOR: **FIRST//** FIRST PRINT FIELD: **FACTOR** THEN PRINT FIELD: **NUMBER** THEN PRINT FIELD:

Heading (S/C): HEALTH FACTORS SEARCH	Replace

DEVICE: ;;9999	HOME  **SUGGEST QUEUEING OUTPUT TO MAILMAN AS SEARCH WILL TAKE A LONG TIME TO COMPLETE**

HEALTH FACTORS SEARCH		MAR 20,2013	07:58	PAGE 1 FACTOR	NUMBER

| CCHT TEST ONE                      |   660012 |
|------------------------------------|----------|
| CCHT VETERAN REFERRAL SOCIAL WORK  |   660014 |
| HT VETERAN REFERRAL SOCIAL WORK    |      820 |
| HT VETERAN REFERRAL SVCS IN PLACE  |      822 |
| HT VETERAN REFERRAL TRANSPORTATION |      831 |

In this sample search, the VETERAN REFERRAL SOCIAL WORK factor has a “CCHT “ entry and an “HT “ entry at IEN less than 100,000. Note that the names are an exact match (excluding “CC”). The “CCHT “ entry would be a candidate for the delete and re-point process with any associated pointers being updated to reference the HT VETERAN REFERRAL SOCIAL WORK entry.

**DELETE AND REPOINT EXAMPLE**

The following is an example of deleting a HEALTH FACTOR file entry and updating the pointers associated with that entry to reference a new HEALTH FACTOR file entry. When a delete/repoint is made, the output will contain a list of files that point to the HEALTH FACTORS (or EDUCATION TOPICS) file. For each file there with either be a listing of the entries that were updated or a “NO RECORDS TO PRINT” message indicating no pointers needed updating.

VA FileMan Version 22.0

Enter or Edit File Entries Print File Entries

Search File Entries Modify File Attributes Inquire to File Entries Utility Functions ...

Data Dictionary Utilities ... Transfer Entries

Other Options ...

Select VA FileMan &lt;TEST ACCOUNT&gt; Option: **Enter or Edit File Entries**

INPUT TO WHAT FILE: **HEALTH FACTORS//**

EDIT WHICH FIELD: **ALL//**

Select HEALTH FACTORS: **CCHT VETERAN REFERRAL SOCIAL WORK**

FACTOR: CCHT TEST ENTRY// **@**

SURE YOU WANT TO DELETE THE ENTIRE 'CCHT TEST ENTRY' HEALTH FACTORS? **YES**

(Yes)

SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO' BY ENTRIES IN THE 'HEALTH SUMMARY TYPE' FILE, ETC.,

DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? No// **Y**

(Yes)

WHICH DO YOU WANT TO DO? --

1. DELETE ALL SUCH POINTERS
2. **CHANGE ALL SUCH POINTERS TO POINT TO A DIFFERENT 'HEALTH FACTORS' ENTRY**

CHOOSE 1) OR 2): **2**

THEN PLEASE INDICATE WHICH ENTRY SHOULD BE POINTED TO Select HEALTH FACTORS: **HT VETERAN REFERRAL SOCIAL WORK**

NOTE: This is where you would choose the appropriate HT version of the health factor (or education topic) being replaced. In this case, HT VETERAN REFERRAL SOCIAL WORK.

(RE-POINTING WILL OCCUR WHEN YOU LEAVE 'ENTER/EDIT' OPTION)

Select HEALTH FACTORS:

...EXCUSE ME, JUST A MOMENT PLEASE... DEVICE: HOME// ;;9999	HOME

HEALTH SUMMARY TYPE entries whose 'SELECTION ITEM' pointers have been changed

MAR 19,2013	10:04	PAGE 1

*** NO RECORDS TO PRINT ***

REMINDER DIALOG entries whose 'FINDING ITEM' pointers have been changed

MAR 19,2013	10:04	PAGE 1

*** NO RECORDS TO PRINT ***

REMINDER DIALOG entries whose 'ADDITIONAL FINDINGS' pointers have been changed

MAR 19,2013	10:04	PAGE 1

*** NO RECORDS TO PRINT ***

REMINDER FINDING ITEM PARAMETER entries whose 'FINDING ITEM' pointers have been changed

MAR 19,2013	10:04	PAGE 1

*** NO RECORDS TO PRINT ***

HEALTH FACTOR RESOLUTION entries whose 'NAME' pointers have been changed

MAR 19,2013	10:04	PAGE 1

*** NO RECORDS TO PRINT ***

REMINDER EXTRACT SUMMARY entries whose 'FINDING ITEM' pointers have been changed

MAR 19,2013	10:04	PAGE 1

*** NO RECORDS TO PRINT ***

REMINDER EXTRACT SUMMARY entries whose 'FINDING ITEM' pointers have been changed

MAR 19,2013	10:04	PAGE 1

*** NO RECORDS TO PRINT ***

REMINDER TERM entries whose 'FINDING ITEM' pointers have been changed

MAR 19,2013	10:04	PAGE 1

*** NO RECORDS TO PRINT ***

REMINDER DEFINITION entries whose 'FINDING ITEM' pointers have been changed

MAR 19,2013	10:04	PAGE 1

*** NO RECORDS TO PRINT ***

NUPA PCE INFO entries whose 'HAD HEALTH FACTOR' pointers have been changed

MAR 19,2013	10:04	PAGE 1

*** NO RECORDS TO PRINT ***

NUPA PCE INFO entries whose 'RECEIVED PREV HEALTH FACTOR' pointers have been cha nged

MAR 19,2013	10:04	PAGE 1

*** NO RECORDS TO PRINT ***

NUPA PCE INFO entries whose 'DECLINED HEALTH FACTOR' pointers have been changed

MAR 19,2013	10:04	PAGE 1

*** NO RECORDS TO PRINT ***

NUPA PCE INFO entries whose 'N/A HEALTH FACTOR' pointers have been changed

MAR 19,2013	10:04	PAGE 1

*** NO RECORDS TO PRINT ***

V HEALTH FACTORS entries whose 'HEALTH FACTOR' pointers have been changed

MAR 19,2013	10:04	PAGE 1

**660204	CRPATIENT,TWO	NOV 8,2011@08:00**

HEALTH FACTORS entries whose 'CATEGORY' pointers have been changed

MAR 19,2013	10:04	PAGE 1

*** NO RECORDS TO PRINT ***

HEALTH FACTORS entries whose 'NOT USED WITH' pointers have been changed

MAR 19,2013	10:04	PAGE 1

*** NO RECORDS TO PRINT ***

Enter or Edit File Entries Print File Entries

Search File Entries Modify File Attributes Inquire to File Entries Utility Functions ...

Data Dictionary Utilities ... Transfer Entries

Other Options ...

**Appendix B: Crosswalk from CCHT Pilot to National** **Release**

This is a table is intended to help sites know what data is being installed into their systems and also assist with any local decisions to inactivate unused/unwanted health factors. The table shows a comparison between the health factors distributed in the VA-HT PROJECT reminder exchange file (installed by PXRM*2.0*19) to corresponding entries from the CCHT Phase 3 Pilot Program.

The HT TEMPLATES 1.0 column is the authoritative list of health factors being used by the Home Telehealth clinical reminders content. Health factor category names appear in **bold** text. If the only difference between two health factor names is “HT” vs. “CCHT”, those items will appear on the same row. Such as:

| **HT TEMPLATES 1.0**                  | **PILOT PHASE 3**                       |
|---------------------------------------|-----------------------------------------|
| HT CAREGIVER REFERRAL BEREAVE SUPPORT | CCHT CAREGIVER REFERRAL BEREAVE SUPPORT |

New health factors will not have an equivalent Pilot entry.

| **HT TEMPLATES 1.0**           | **PILOT PHASE 3**   |
|--------------------------------|---------------------|
| HT CATEGORY OF CARE-ACUTE CARE |                     |

Pilot health factors no longer used in the HT Templates will not have an equivalent HT entry.

| **HT TEMPLATES 1.0**   | **PILOT PHASE 3**                      |
|------------------------|----------------------------------------|
|                        | CCHT CAREGIVER RISK ASSESSMENT SCORE 0 |

There are 271 new HT-specific health factors included in the VA-HT PROJECT reminder exchange file. The “GEC” health factors being exported are VA national, already exist at VA sites, and are not included in this table.

| **HT TEMPLATES 1.0**                     | **PILOT PHASE 3**                            |
|------------------------------------------|----------------------------------------------|
|                                          | **CCHT (CARE COORDINATION HOME TELEHEALTH)** |
| **HT (HOME TELEHEALTH)**                 |                                              |
|                                          | CCHT APPROX DELIVERY DATE FOR EQUIPMENT      |
|                                          | CCHT ASSESSMENT TX PLAN TEMPLATE USED        |
| **HT ASSESSMENT/TREATMENT PLAN**         | **CCHT ASSESSMENT/TREATMENT PLAN**           |
| HT BARRIERS TO LEARNING                  |                                              |
| HT BATHING HELP/SUPRVISION LAST 7D-NO    | CCHT BATHING HELP/SUPRVISION LAST 7D-NO      |
| HT BATHING HELP/SUPRVISION LAST 7D-YES   | CCHT BATHING HELP/SUPRVISION LAST 7D-YES     |
| HT BED MOBIL HELP/SUPERV LAST 7D-NO      | CCHT BED MOBIL HELP/SUPERV LAST 7D-NO        |
| HT BED MOBIL HELP/SUPERV LAST 7D-YES     | CCHT BED MOBIL HELP/SUPERV LAST 7D-YES       |
|                                          | CCHT C/G RISK ASSESSMENT DIALOG USED         |
|                                          | CCHT C/G RISK SCREEN TEMPLATE USED           |
|                                          | CCHT CAREGIVER ASSESSMENT SCREEN DONE        |
|                                          | CCHT CAREGIVER ASSESSMENT TEMPLATE USED      |
| HT CAREGIVER ASSESSMENT SCREEN COMPLETED | HT CAREGIVER ASSESSMENT SCREEN COMPLETED     |
| HT CAREGIVER REFERRAL BEREAVE SUPPORT    | CCHT CAREGIVER REFERRAL BEREAVE SUPPORT      |
| HT CAREGIVER REFERRAL C/G SUPPORT GRP    | CCHT CAREGIVER REFERRAL C/G SUPPORT GRP      |
| HT CAREGIVER REFERRAL EDUC/TRAINING      | CCHT CAREGIVER REFERRAL EDUC/TRAINING        |
| HT CAREGIVER REFERRAL FAMILY COUNSEL     | CCHT CAREGIVER REFERRAL FAMILY COUNSEL       |
| HT CAREGIVER REFERRAL INDIVID COUNSEL    | CCHT CAREGIVER REFERRAL INDIVID COUNSEL      |
| HT CAREGIVER REFERRAL MEDICAL EVAL,F/U   | CCHT CAREGIVER REFERRAL MEDICAL EVAL,F/U     |
| HT CAREGIVER REFERRAL OTHER SERVICE      | CCHT CAREGIVER REFERRAL OTHER SERVICE        |
| HT CAREGIVER REFERRAL SVCS IN PLACE      | CCHT CAREGIVER REFERRAL SVCS IN PLACE        |
| HT CAREGIVER REFERRAL(S) NON VA SYSTEM   | CCHT CAREGIVER REFERRAL(S) NON VA SYSTEM     |
| HT CAREGIVER REFERRAL(S) VA SYSTEM       | CCHT CAREGIVER REFERRAL(S) VA SYSTEM         |
|                                          | CCHT CAREGIVER RISK ASSESSMENT SCORE 0       |
|                                          | CCHT CAREGIVER RISK ASSESSMENT SCORE 1       |
|                                          | CCHT CAREGIVER RISK ASSESSMENT SCORE 10      |
|                                          | CCHT CAREGIVER RISK ASSESSMENT SCORE 11      |
|                                          | CCHT CAREGIVER RISK ASSESSMENT SCORE 12      |
|                                          | CCHT CAREGIVER RISK ASSESSMENT SCORE 13      |
|                                          | CCHT CAREGIVER RISK ASSESSMENT SCORE 14      |
|                                          | CCHT CAREGIVER RISK ASSESSMENT SCORE 15      |
|                                          | CCHT CAREGIVER RISK ASSESSMENT SCORE 16      |
|                                          | CCHT CAREGIVER RISK ASSESSMENT SCORE 2       |
|                                          | CCHT CAREGIVER RISK ASSESSMENT SCORE 3       |

|                                          | CCHT CAREGIVER RISK ASSESSMENT SCORE 4    |
|------------------------------------------|-------------------------------------------|
|                                          | CCHT CAREGIVER RISK ASSESSMENT SCORE 5    |
|                                          | CCHT CAREGIVER RISK ASSESSMENT SCORE 6    |
|                                          | CCHT CAREGIVER RISK ASSESSMENT SCORE 7    |
|                                          | CCHT CAREGIVER RISK ASSESSMENT SCORE 8    |
|                                          | CCHT CAREGIVER RISK ASSESSMENT SCORE 9    |
| HT CAREGIVER REVIEW OF WRITTEN MATERIALS | HT CAREGIVER REVIEW OF WRITTEN MATERIALS  |
| **HT CAREGIVER RISK ASSESSMENT SCREEN**  | **CCHT CAREGIVER RISK ASSESSMENT SCREEN** |
| HT CAREGIVER STATES ESSENTIAL CONCEPTS   |                                           |
|                                          | CCHT CATEGORY-ACUTE CARE                  |
|                                          | CCHT CATEGORY-CHRONIC CARE                |
|                                          | CCHT CATEGORY-HEALTH PROMOTION            |
|                                          | CCHT CATEGORY-NON INSTITUTIONAL CARE      |
| HT CATEGORY OF CARE-ACUTE CARE           |                                           |
| HT CATEGORY OF CARE-CHRONIC CARE MGMT    | HT CATEGORY OF CARE-CHRONIC CARE MGMT     |
| HT CATEGORY OF CARE-HEALTH PROMOTION     |                                           |
| HT CATEGORY OF CARE-NON INSTITUTIONAL    |                                           |
| HT CATEGORY OF CARE-OTHER                |                                           |
|                                          | CCHT CATEGORY-TELEPHONE CASE MANAGEMENT   |
| HT CCF 1 OR MORE BEHAV/COGN PROBLEMS     | CCHT CCF 1 OR MORE BEHAV/COGN PROBLEMS    |
| HT CCF 12 OR MORE CLINIC STOPS PAST YR   | CCHT CCF 12 OR MORE CLINIC STOPS          |
| HT CCF 2 OR MORE ADL DEFICITS            | CCHT CCF 2 OR MORE ADL DEFICITS           |
| HT CCF AGE 75 OR GREATER                 | CCHT CCF AGE 75 OR GREATER                |
| HT CCF AGITATED/DISORIENTED-NO           | CCHT CCF AGITATED/DISORIENTED-NO          |
| HT CCF AGITATED/DISORIENTED-YES          | CCHT CCF AGITATED/DISORIENTED-YES         |
| HT CCF CAREGIVER ACCESSIBLE              | CCHT CCF CAREGIVER ACCESSIBLE             |
| HT CCF CAREGIVER CAN INCREASE HELP       | CCHT CCF CAREGIVER CAN INCREASE HELP      |
| HT CCF CAREGIVER CAN'T INCREASE HELP     | CCHT CCF CAREGIVER CAN'T INCREASE HELP    |
| HT CCF CAREGIVER LIVES WITH PT-NO        | CCHT CCF CAREGIVER LIVES WITH PT-NO       |
| HT CCF CAREGIVER LIVES WITH PT-YES       | CCHT CCF CAREGIVER LIVES WITH PT-YES      |
| HT CCF CAREGIVER NOT ACCESSIBLE          | CCHT CCF CAREGIVER NOT ACCESSIBLE         |
|                                          | CCHT CCF CAREGIVER SAME NAME AS PT        |
| HT CCF CAREGIVER-ADL HELP                | CCHT CCF CAREGIVER-ADL HELP               |
| HT CCF CAREGIVER-CHILD                   | CCHT CCF CAREGIVER-CHILD                  |
| HT CCF CAREGIVER-EMOTIONAL SUPPORT       | CCHT CCF CAREGIVER-EMOTIONAL SUPPORT      |
| HT CCF CAREGIVER-FRIEND/NEIGHBOR         | CCHT CCF CAREGIVER-FRIEND/NEIGHBOR        |
| HT CCF CAREGIVER-IADL HELP               | CCHT CCF CAREGIVER-IADL HELP              |
| HT CCF CAREGIVER-OTHER                   | CCHT CCF CAREGIVER-OTHER                  |
| HT CCF CAREGIVER'S CITY                  | CCHT CCF CAREGIVER'S CITY                 |
| HT CCF CAREGIVER'S NAME                  | CCHT CCF CAREGIVER'S NAME                 |
| HT CCF CAREGIVER'S PHONE                 | CCHT CCF CAREGIVER'S PHONE                |

| HT CCF CAREGIVER'S STATE               | CCHT CCF CAREGIVER'S STATE               |
|----------------------------------------|------------------------------------------|
| HT CCF CAREGIVER'S STREET ADDRESS      | CCHT CCF CAREGIVER'S STREET ADDRESS      |
| HT CCF CAREGIVER'S ZIP CODE            | CCHT CCF CAREGIVER'S ZIP CODE            |
| HT CCF CAREGIVER-SPOUSE                | CCHT CCF CAREGIVER-SPOUSE                |
| HT CCF COMPLEXITY TOO GREAT-NO         | CCHT CCF COMPLEXITY TOO GREAT-NO         |
| HT CCF COMPLEXITY TOO GREAT-YES        | CCHT CCF COMPLEXITY TOO GREAT-YES        |
| HT CCF DELUSIONS-NO                    | CCHT CCF DELUSIONS-NO                    |
| HT CCF DELUSIONS-YES                   | CCHT CCF DELUSIONS-YES                   |
| HT CCF DIFFIC MAKE SELF UNDERSTOOD-NO  | CCHT CCF DIFFIC MAKE SELF UNDERSTOOD-NO  |
| HT CCF DIFFIC MAKE SELF UNDERSTOOD-YES | CCHT CCF DIFFIC MAKE SELF UNDERSTOOD-YES |
| HT CCF DIFFIC REASONABLE DECISIONS-NO  | CCHT CCF DIFFIC REASONABLE DECISIONS-NO  |
| HT CCF DIFFIC REASONABLE DECISIONS-YES | CCHT CCF DIFFIC REASONABLE DECISIONS-YES |
| HT CCF DOES NOT MEET CCM CRITERIA      | CCHT CCF DOES NOT MEET CCM CRITERIA      |
| HT CCF DOES NOT MEET NIC CRITERIA      | CCHT CCF DOES NOT MEET NIC CRITERIA      |
| HT CCF FLARE UP CHRONIC CONDITION-NO   | CCHT CCF FLARE UP CHRONIC CONDITION-NO   |
| HT CCF FLARE UP CHRONIC CONDITION-YES  | CCHT CCF FLARE UP CHRONIC CONDITION-YES  |
| HT CCF FOLLOW-UP ASSESSMENT COMPLETED  | CCHT CCF FOLLOW-UP ASSESSMENT DONE       |
| HT CCF GROUP SETTING NON RELATIVES     | CCHT CCF GROUP SETTING NON RELATIVES     |
| HT CCF HALLUCINATIONS-AUDITORY         | CCHT CCF HALLUCINATIONS-AUDITORY         |
| HT CCF HALLUCINATIONS-NONE             | CCHT CCF HALLUCINATIONS-NONE             |
| HT CCF HALLUCINATIONS-OLFACTORY        | CCHT CCF HALLUCINATIONS-OLFACTORY        |
| HT CCF HALLUCINATIONS-SENSORY          | CCHT CCF HALLUCINATIONS-SENSORY          |
| HT CCF HALLUCINATIONS-TACTILE          | CCHT CCF HALLUCINATIONS-TACTILE          |
| HT CCF HALLUCINATIONS-VISUAL           | CCHT CCF HALLUCINATIONS-VISUAL           |
| HT CCF INITIAL ASSESSMENT COMPLETED    |                                          |
|                                        | CCHT CCF INITIAL ASSESSMENT DONE         |
| HT CCF LIFE EXPECTANCY < 6 MO          | CCHT CCF LIFE EXPECTANCY < 6 MO          |
| HT CCF LIVES ALONE                     | CCHT CCF LIVES ALONE                     |
| HT CCF LIVES ALONE IN COMMUNITY        | CCHT CCF LIVES ALONE IN COMMUNITY        |
| HT CCF LIVES AT OTHER                  | CCHT CCF LIVES AT OTHER                  |
| HT CCF LIVES BOARD AND CARE            | CCHT CCF LIVES BOARD AND CARE            |
| HT CCF LIVES DOMICILIARY               | CCHT CCF LIVES DOMICILIARY               |
| HT CCF LIVES HOMELESS                  | CCHT CCF LIVES HOMELESS                  |
| HT CCF LIVES HOMELESS SHELTER          | CCHT CCF LIVES HOMELESS SHELTER          |
| HT CCF LIVES NURSING HOME              | CCHT CCF LIVES NURSING HOME              |
| HT CCF LIVES PRIVATE HOME              | CCHT CCF LIVES PRIVATE HOME              |
| HT CCF LIVES WITH ADULT CHILD          | CCHT CCF LIVES WITH ADULT CHILD          |
| HT CCF LIVES WITH CHILD                | CCHT CCF LIVES WITH CHILD                |
| HT CCF LIVES WITH OTHER                | CCHT CCF LIVES WITH OTHER                |
| HT CCF LIVES WITH SPOUSE & OTHERS      | CCHT CCF LIVES WITH SPOUSE & OTHERS      |
| HT CCF LIVES WITH SPOUSE ONLY          | CCHT CCF LIVES WITH SPOUSE ONLY          |

| HT CCF MEETS CHRONIC CARE MGMT CRITERIA   | CCHT CCF MEETS CCM CRITERIA              |
|-------------------------------------------|------------------------------------------|
| HT CCF MEETS NIC CATEGORY A CRITERIA      | CCHT CCF MEETS NIC CATEGORY A CRITERIA   |
| HT CCF MEETS NIC CATEGORY B CRITERIA      | CCHT CCF MEETS NIC CATEGORY B CRITERIA   |
| HT CCF MEETS NIC CRITERIA                 | CCHT CCF MEETS NIC CRITERIA              |
| HT CCF MOOD DISORDER DEPRESSION-NO        | CCHT CCF MOOD DISORDER DEPRESSION-NO     |
| HT CCF MOOD DISORDER DEPRESSION-YES       | CCHT CCF MOOD DISORDER DEPRESSION-YES    |
| HT CCF MOOD DISORDER MANIC-NO             | CCHT CCF MOOD DISORDER MANIC-NO          |
| HT CCF MOOD DISORDER MANIC-YES            | CCHT CCF MOOD DISORDER MANIC-YES         |
| HT CCF NIC CRITERIA NO-ACUTE CARE MGMT    | CCHT CCF NIC CRITERIA NO-ACUTE CARE MGMT |
| HT CCF NIC CRITERIA NO-HLTH PROMOTION     | CCHT CCF NIC CRITERIA NO-HLTH PROMOTION  |
| HT CCF PHYSICALLY ABUSIVE BEHAVIOR-NO     | CCHT CCF PHYSICALLY ABUSIVE BEHAVIOR-NO  |
| HT CCF PHYSICALLY ABUSIVE BEHAVIOR-YES    | CCHT CCF PHYSICALLY ABUSIVE BEHAVIOR-YES |
| HT CCF POTENTIAL FOR INCR INDEP-NO        | CCHT CCF POTENTIAL FOR INCR INDEP-NO     |
| HT CCF POTENTIAL FOR INCR INDEP-YES       | CCHT CCF POTENTIAL FOR INCR INDEP-YES    |
| HT CCF PROBLEMS WITH 3 OR MORE ADLS       | CCHT CCF PROBLEMS IN 3 OR MORE ADLS      |
| HT CCF PROBLEMS WITH 3 OR MORE IADL       | CCHT CCF PROBLEMS WITH 3 OR MORE IADL    |
| HT CCF PTSD/OTHER ANXIETY-NO              | CCHT CCF PTSD/OTHER ANXIETY-NO           |
| HT CCF PTSD/OTHER ANXIETY-YES             | CCHT CCF PTSD/OTHER ANXIETY-YES          |
| HT CCF RECOMMEND REFERRAL-NO              | CCHT CCF RECOMMEND REFERRAL              |
| HT CCF RECOMMEND REFERRAL-YES             | CCHT CCF RECOMMEND REFERRAL-NO           |
| HT CCF RESISTING CARE-NO                  | CCHT CCF RESISTING CARE-NO               |
| HT CCF RESISTING CARE-YES                 | CCHT CCF RESISTING CARE-YES              |
| HT CCF SERVICES IN PLACE-NO               | CCHT CCF SERVICES IN PLACE-NO            |
| HT CCF SERVICES IN PLACE-YES              | CCHT CCF SERVICES IN PLACE-YES           |
| HT CCF SUBST ABUSE/DEPENDENCE-NO          | CCHT CCF SUBST ABUSE/DEPENDENCE-NO       |
| HT CCF SUBST ABUSE/DEPENDENCE-YES         | CCHT CCF SUBST ABUSE/DEPENDENCE-YES      |
| HT CCF UNPAID CAREGIVER-NO                | CCHT CCF UNPAID CAREGIVER-NO             |
| HT CCF UNPAID CAREGIVER-YES               | CCHT CCF UNPAID CAREGIVER-YES            |
| HT CCF VERBALLY ABUSIVE BEHAVIOR-NO       | CCHT CCF VERBALLY ABUSIVE BEHAVIOR-NO    |
| HT CCF VERBALLY ABUSIVE BEHAVIOR-YES      | CCHT CCF VERBALLY ABUSIVE BEHAVIOR-YES   |
| HT CCF WANDERING-NO                       | CCHT CCF WANDERING-NO                    |
| HT CCF WANDERING-YES                      | CCHT CCF WANDERING-YES                   |
| HT CG/VETERAN REFERRAL COMPLETED          |                                          |
|                                           | CCHT CG/VET REFER DIALOG/TEMPLATE USED   |
|                                           | CCHT CG/VETERAN REFERRAL TEMPLATE DONE   |
|                                           | CCHT CG/VETERAN REFERRAL TEMPLATE USED   |
| HT CG/VETERAN REFERRAL(S) NOT UTILIZED    | CCHT CG/VETERAN REFERRAL(S) NOT UTILIZED |
| HT CLINICAL REASON FOR ENROLLMENT         | CCHT CLINICAL REASON FOR ENROLLMENT      |
| HT CONSULTS/REFERRALS RECOMMENDED         |                                          |
|                                           | CCHT CONT OF CARE TITLE/TEMPLATE USED    |
|                                           | CCHT CONT OF CARE(EMBEDDED)TEMPLATE USED |

|                                         | CCHT CONTACT MADE FOR EQUIP RETURN       |
|-----------------------------------------|------------------------------------------|
|                                         | **CCHT CONTINUUM OF CARE**               |
| **HT CONTINUUM OF CARE (CCF)**          |                                          |
| HT DIFFICULT MANAGING MEDS/LAST 7D-NO   | CCHT DIFFICULT MANAGING MEDS/LAST 7D-NO  |
| HT DIFFICULT MANAGING MEDS/LAST 7D-YES  | CCHT DIFFICULT MANAGING MEDS/LAST 7D-YES |
| HT DIFFICULT MNG FINANCES/LAST 7D-NO    | CCHT DIFFICULT MNG FINANCES/LAST 7D-NO   |
| HT DIFFICULT MNG FINANCES/LAST 7D-YES   | CCHT DIFFICULT MNG FINANCES/LAST 7D-YES  |
| HT DIFFICULT PREPARE MEALS/LAST 7D-NO   | CCHT DIFFICULT PREPARE MEALS/LAST 7D-YES |
| HT DIFFICULT PREPARE MEALS/LAST 7D-YES  |                                          |
| HT DIFFICULT TRANSPORTATION/LAST 7D-NO  |                                          |
| HT DIFFICULT TRANSPORTATION/LAST 7D-YES |                                          |
|                                         | CCHT DIFFICULT TRANSPRTATION/LAST 7D-NO  |
|                                         | CCHT DIFFICULT TRANSPRTATION/LAST 7D-YES |
| HT DIFFICULT USING PHONE LAST 7D-NO     | CCHT DIFFICULT USING PHONE LAST 7D-NO    |
| HT DIFFICULT USING PHONE LAST 7D-YES    | CCHT DIFFICULT USING PHONE LAST 7D-YES   |
| HT DIFFICULT W/ HOUSEWORK/LAST 7D-NO    | CCHT DIFFICULT W/ HOUSEWORK/LAST 7D-NO   |
| HT DIFFICULT W/ HOUSEWORK/LAST 7D-YES   | CCHT DIFFICULT W/ HOUSEWORK/LAST 7D-YES  |
| HT DIFFICULT WITH SHOPPING/LAST 7D-NO   | CCHT DIFFICULT WITH SHOPPING/LAST 7D-NO  |
| HT DIFFICULT WITH SHOPPING/LAST 7D-YES  | CCHT DIFFICULT WITH SHOPPING/LAST 7D-YES |
|                                         | CCHT DIGITAL CAMERA SERIAL #             |
| **HT DISCHARGE**                        | **CCHT DISCHARGE**                       |
|                                         | CCHT DISCHARGE TEMPLATE USED             |
| HT DISCHARGE-ADMITTED TO NURSING HOME   | CCHT DISCHARGE-ADMITTED TO NURSING HOME  |
|                                         | CCHT DISCHARGE-ALL EQUIP RETURNED (NO)   |
|                                         | CCHT DISCHARGE-ALL EQUIP RETURNED (YES)  |
| HT DISCHARGE-ALL ISSUES ADDRESSED(NO)   | CCHT DISCHARGE-ALL ISSUES ADDRESSED(NO)  |
| HT DISCHARGE-ALL ISSUES ADDRESSED(YES)  | CCHT DISCHARGE-ALL ISSUES ADDRESSED(YES) |
|                                         | CCHT DISCHARGE-EQUIP RETURN (OTHER)      |
| HT DISCHARGE-HAS MET GOALS              | CCHT DISCHARGE-HAS MET GOALS             |
| HT DISCHARGE-NO RESPONSE TO PROGRAM     | CCHT DISCHARGE-NO RESPONSE TO PROGRAM    |
| HT DISCHARGE-NO VA PRIMARY CARE SVCS    | CCHT DISCHARGE-NO VA PRIMARY CARE SVCS   |
| HT DISCHARGE-OTHER FOLLOW-UP            | CCHT DISCHARGE-OTHER FOLLOW-UP           |
| HT DISCHARGE-PATIENT IS DECEASED        | CCHT DISCHARGE-PATIENT IS DECEASED       |
| HT DISCHARGE-PHONE,ELECT SVCS UNAVAIL   | CCHT DISCHARGE-PHONE,ELECT SVCS UNAVAIL  |
| HT DISCHARGE-PROLONGED HOSPITALIZATION  | CCHT DISCHARGE-PROLONGED HOSPITALIZATION |
| HT DISCHARGE-PROVIDER REQUESTS DC       | CCHT DISCHARGE-PROVIDER REQUESTS DC      |
| HT DISCHARGE-PT/CG REQUEST DC SERVICES  | CCHT DISCHARGE-PT/CG REQUEST DC SERVICES |
| HT DISCHARGE-REFERRED TO HOSPICE        | CCHT DISCHARGE-REFERRED TO HOSPICE       |
| HT DISCHARGE-REFERRED TO MENTAL HEALTH  | CCHT DISCHARGE-REFERRED TO MENTAL HEALTH |
| HT DISCHARGE-REFERRED TO NEW LOCATION   | CCHT DISCHARGE-REFERRED TO NEW LOCATION  |
| HT DISCHARGE-REFERRED TO PRIMARY CARE   | CCHT DISCHARGE-REFERRED TO PRIMARY CARE  |

| HT DISCHARGE-REFERRED TO SOCIAL WORK    | CCHT DISCHARGE-REFERRED TO SOCIAL WORK   |
|-----------------------------------------|------------------------------------------|
| HT DISCHARGE-RELOCATED OUT OF SVC AREA  | CCHT DISCHARGE-RELOCATED OUT OF SVC AREA |
| HT DISCHARGE-UNABLE TO OPERATE DEVICES  | CCHT DISCHARGE-UNABLE TO OPERATE DEVICES |
|                                         | CCHT DISEASE INDICATIONS-CHF             |
| HT DISEASE INDICATIONS-COPD             | CCHT DISEASE INDICATIONS-COPD            |
| HT DISEASE INDICATIONS-DEPRESSION       | CCHT DISEASE INDICATIONS-DEPRESSION      |
| HT DISEASE INDICATIONS-DIABETES         | CCHT DISEASE INDICATIONS-DIABETES        |
| HT DISEASE INDICATIONS-HEART FAILURE    |                                          |
| HT DISEASE INDICATIONS-HYPERTENSION     | CCHT DISEASE INDICATIONS-HYPERTENSION    |
| HT DISEASE INDICATIONS-OBESITY          |                                          |
| HT DISEASE INDICATIONS-OTHER            | CCHT DISEASE INDICATIONS-OTHER           |
| HT DISEASE INDICATIONS-PTSD             | CCHT DISEASE INDICATIONS-PTSD            |
| HT DISEASE INDICATIONS-SUBSTANCE ABUSE  |                                          |
|                                         | CCHT DISEASE INDICATIONS-SUBST ABUSE     |
| HT DISINTERESTED/LACKS MOTIVATION       |                                          |
| HT DRESSING HELP/SUPERV LAST 7D-NO      | CCHT DRESSING HELP/SUPERV LAST 7D-NO     |
| HT DRESSING HELP/SUPERV LAST 7D-YES     | CCHT DRESSING HELP/SUPERV LAST 7D-YES    |
| HT EATING HELP/SUPERVISION LAST 7D-NO   | CCHT EATING HELP/SUPERVISION LAST 7D-NO  |
| HT EATING HELP/SUPERVISION LAST 7D-YES  | CCHT EATING HELP/SUPERVISION LAST 7D-YES |
|                                         | CCHT EDUC ON EQUIP-CARE COORDINATOR      |
|                                         | CCHT EDUC ON EQUIP-CONTRACT VENDOR       |
|                                         | CCHT EDUC ON EQUIP-SUPPORT STAFF         |
| HT EMERG PRIORITY HIGH-IMMEDIATE EVAL   | CCHT EMERG PRIORITY HIGH-IMMEDIATE EVAL  |
| HT EMERG PRIORITY LOW-HAS RESOURCES     | CCHT EMERG PRIORITY LOW-HAS RESOURCES    |
| HT EMERG PRIORITY MOD-SVCS AFTER 3-7D   | CCHT EMERG PRIORITY MOD-SVCS AFTER 3-7D  |
| HT ENROLLMENT-ENDING DATE               | CCHT ENROLLMENT-ENDING DATE              |
| HT ENROLLMENT-START DATE                | CCHT ENROLLMENT-START DATE               |
| HT ENROLLMENT-START DATE (PREV ENROLL)  | CCHT ENROLLMENT-START DATE (PREV ENROLL) |
| HT EQUIP INSTALLATION MODE-OTHER        | CCHT EQUIP INSTALLATION MODE-OTHER       |
|                                         | CCHT EQUIP INSTALLED BY CARE COORDINATOR |
|                                         | CCHT EQUIP INSTALLED BY CONTRACT VENDOR  |
|                                         |                                          |
| HT EQUIP INSTALLED BY SUPPORT STAFF     | CCHT EQUIP INSTALLED BY SUPPORT STAFF    |
| HT EQUIP INSTALLED BY VETERAN/CAREGIVER |                                          |
|                                         | CCHT EQUIP INSTALLED BY VETERAN/CAREGVR  |
|                                         | CCHT EQUIP MAILED,INSTALL BY VET/CAREGVR |
|                                         | CCHT EQUIP TAKEN HOME,INSTALL BY VET/CG  |
| HT GETS MEDS VIA NON-VA PROVIDER-NO     | CCHT GETS MEDS VIA NON-VA PROVIDER-NO    |
| HT GETS MEDS VIA NON-VA PROVIDER-YES    | CCHT GETS MEDS VIA NON-VA PROVIDER-YES   |
| HT HEALTH EDUCATION PLAN                |                                          |
| HT HEALTH EDUCATION RESPONSE            |                                          |

| HT INDICATIONS-# OUTPT VISITS PAST YR    | CCHT INDICATIONS-# OUTPT VISITS PAST YR   |
|------------------------------------------|-------------------------------------------|
| HT INDICATIONS-DISTANCE (HOURS)          | CCHT INDICATIONS-DISTANCE (HOURS)         |
| HT INDICATIONS-DISTANCE (MILES)          | CCHT INDICATIONS-DISTANCE (MILES)         |
| HT INDICATIONS-HX HIGH COST/HIGH USE     | CCHT INDICATIONS-HX HIGH COST/HIGH USE    |
| HT INDICATIONS-HX HOSPITALIZATONS        | CCHT INDICATIONS-HX HOSPITALIZATONS       |
|                                          | CCHT INTERVENTION TEMPLATE USED           |
| HT LEARNING BARRIER-ANGRY                |                                           |
| HT LEARNING BARRIER-ANXIETY              |                                           |
| HT LEARNING BARRIER-APHASIA              |                                           |
| HT LEARNING BARRIER-COGNITIVE IMPAIRMENT | HT LEARNING BARRIER-COGNITIVE IMPAIRMENT  |
| HT LEARNING BARRIER-CULTURAL             |                                           |
| HT LEARNING BARRIER-HEARING IMPAIRED     |                                           |
| HT LEARNING BARRIER-HOMELESS             |                                           |
| HT LEARNING BARRIER-IMPAIRED MEMORY      |                                           |
| HT LEARNING BARRIER-LANGUAGE             | CCHT LEARNING BARRIER-LANGUAGE            |
| HT LEARNING BARRIER-NONE IDENTIFIED      | CCHT LEARNING BARRIER-NONE IDENTIFIED     |
| HT LEARNING BARRIER-NOT MOTIVATED        |                                           |
| HT LEARNING BARRIER-OVERWHELMED          |                                           |
| HT LEARNING BARRIER-PAIN                 |                                           |
| HT LEARNING BARRIER-PHYSICAL LIMITATIONS |                                           |
| HT LEARNING BARRIER-POOR CONCENTRATION   | HT LEARNING BARRIER-POOR CONCENTRATION    |
| HT LEARNING BARRIER-UNABLE TO READ       | CCHT LEARNING BARRIER-UNABLE TO READ      |
| HT LEARNING BARRIER-UNABLE TO WRITE      |                                           |
| HT LEARNING BARRIER-VISUALLY IMPAIRED    | CCHT LEARNING BARRIER-VISUALLY IMPAIRED   |
|                                          | CCHT MAKE TIME FOR SELF=FREQUENTLY        |
|                                          | CCHT MAKE TIME FOR SELF=NEARLY ALWAYS     |
|                                          | CCHT MAKE TIME FOR SELF=NEVER             |
|                                          | CCHT MAKE TIME FOR SELF=RARELY            |
|                                          | CCHT MAKE TIME FOR SELF=SOMETIMES         |
| HT MEALS PREPARED BY OTHER/LAST 7D-NO    | CCHT MEALS PREPARED BY OTHER/LAST 7D-NO   |
| HT MEALS PREPARED BY OTHER/LAST 7D-YES   | CCHT MEALS PREPARED BY OTHER/LAST 7D-YES  |
|                                          | CCHT MEASURING DEVICE-OTHER               |
|                                          | CCHT MEDS ADAPTATIONS-NONE NEEDED         |
|                                          | CCHT MEDS ADAPTATIONS-OTHER               |
|                                          | CCHT MEDS ADAPT-FOR VISUAL IMPAIRMENT     |
|                                          | CCHT MEDS ADAPT-MEDS ARE COLOR CODED      |
|                                          | CCHT MEDS ADAPT-USES PILLBOX              |
|                                          | CCHT MEDS ADAPT-VA PREPARES/POURS MEDS    |
|                                          | CCHT MEDS SPECIAL ADAPTATIONS             |
| HT MEETS TELEHEALTH CRITERIA(NO)         | CCHT MEETS TELEHEALTH CRITERIA(NO)        |
| HT MEETS TELEHEALTH CRITERIA(YES)        | CCHT MEETS TELEHEALTH CRITERIA(YES)       |

|                                         | CCHT MESSAGING DEVICE TYPE/SERIAL #      |
|-----------------------------------------|------------------------------------------|
|                                         | CCHT MESSAGING DEVICE-BLOOD GLUCOSE      |
|                                         | CCHT MESSAGING DEVICE-BLOOD PRESSURE     |
|                                         | CCHT MESSAGING DEVICE-PULSE              |
|                                         | CCHT MESSAGING DEVICE-PULSE OXIMETRY     |
|                                         | CCHT MESSAGING DEVICE-WEIGHT             |
|                                         | CCHT MESSAGING/MONITORING TYPE/SERIAL #  |
|                                         | CCHT MESSAGING/MONITORING-BLOOD GLUCOSE  |
|                                         | CCHT MESSAGING/MONITORING-BLOOD PRESSURE |
|                                         | CCHT MESSAGING/MONITORING-OTHER          |
|                                         | CCHT MESSAGING/MONITORING-PULSE          |
|                                         | CCHT MESSAGING/MONITORING-PULSE OXIMETRY |
|                                         | CCHT MESSAGING/MONITORING-SPIROMETRY     |
|                                         | CCHT MESSAGING/MONITORING-WEIGHT         |
| HT MOVE INDOOR HELP/SUPERV LAST 7D-NO   | CCHT MOVE INDOOR HELP/SUPERV LAST 7D-NO  |
| HT MOVE INDOOR HELP/SUPERV LAST 7D-YES  | CCHT MOVE INDOOR HELP/SUPERV LAST 7D-YES |
| HT NEEDS REINFORCEMENT/REVIEW/FOLLOW-UP | HT NEEDS REINFORCEMENT/REVIEW/FOLLOW-UP  |
| HT NO EVIDENCE OF LEARNING              |                                          |
| HT NO FOLLOW-UP NEEDED/INDICATED        |                                          |
| HT PERIODIC EVALUATION COMPLETED        |                                          |
|                                         | CCHT PERIODIC EVAL DIALOG/TEMPLATE USED  |
|                                         | CCHT PERIODIC EVALUATION DONE            |
|                                         | CCHT PERIPHERALS-BP CUFF (SERIAL #)      |
|                                         | CCHT PERIPHERALS-GLUCOSE CABLES          |
|                                         | CCHT PERIPHERALS-NONE NEEDED             |
|                                         | CCHT PERIPHERALS-OTHER                   |
|                                         | CCHT PERIPHERALS-PULSE OX (SERIAL #)     |
|                                         | CCHT PERIPHERALS-SPIROMETRY (SERIAL #)   |
|                                         | CCHT PERIPHERALS-STETHOSCOPE             |
|                                         | CCHT PERIPHERALS-WEIGHT SCALE (SERIAL #) |
|                                         | CCHT PHONE-DSL LINE                      |
|                                         | CCHT PHONE-MODEM                         |
|                                         | CCHT PHONE-NO FEATURES                   |
| HT PLAN-MED DISCREP SENT TO PROVIDER    | CCHT PLAN-MED DISCREP SENT TO PROVIDER   |
| HT PLAN-REVIEWED LIST OF CURRENT MEDS   | CCHT PLAN-REVIEWED LIST CURRENT MEDS     |
|                                         | CCHT PREVIOUSLY ENROLLED TEMPLATE USED   |
| HT PT/CG HAS LIST OF ACTIVE MEDS-NO     | CCHT PT/CG HAS LIST OF ACTIVE MEDS-NO    |
| HT PT/CG HAS LIST OF ACTIVE MEDS-YES    | CCHT PT/CG HAS LIST OF ACTIVE MEDS-YES   |
| HT PT/CG HAS QUESTIONS ON MEDS-NO       | CCHT PT/CG HAS QUESTIONS ON MEDS-NO      |
| HT PT/CG HAS QUESTIONS ON MEDS-YES      | CCHT PT/CG HAS QUESTIONS ON MEDS-YES     |
|                                         | CCHT PT/CG KNOWS MED INDICATIONS-NO      |

|                                         | CCHT PT/CG KNOWS MED INDICATIONS-YES      |
|-----------------------------------------|-------------------------------------------|
|                                         | CCHT PT/CG KNOWS MED SIDE EFFECTS-YES     |
|                                         | CCHT PT/CG KNOWS MED SIDE EFF-NO          |
|                                         | CCHT PT/CG KNOWS REFILL PROCESS-NO        |
|                                         | CCHT PT/CG KNOWS REFILL PROCESS-YES       |
|                                         | CCHT PT/CG TAKES MEDS AS PRESCRIBED-NO    |
|                                         | CCHT PT/CG TAKES MEDS AS PRESCRIBED-YES   |
| HT REASON FOR NON-ENROLLMENT            | CCHT REASON FOR NON-ENROLLMENT            |
| HT RECENT CHANGE IN FUNCTION-NO         | CCHT RECENT CHANGE IN FUNCTION-NO         |
| HT RECENT CHANGE IN FUNCTION-YES        | CCHT RECENT CHANGE IN FUNCTION-YES        |
| HT REFERRAL-CONSULT COMPLETION          | CCHT REFERRAL-CONSULT COMPLETION          |
|                                         | CCHT REFERRALS CAREGIVER NOT SATISFIED    |
|                                         | CCHT REFERRALS CAREGIVER SATISFIED        |
| **HT REFERRALS FOR VETERAN/CAREGIVER**  | **CCHT REFERRALS FOR VETERAN/CAREGIVER**  |
| HT REFERRALS-CAREGIVER NOT SATISFIED    |                                           |
| HT REFERRALS-CAREGIVER SATISFIED        |                                           |
| HT REPEAT DEMONSTRATION NEXT VISIT      |                                           |
|                                         | CCHT SCREENING CONSULT TEMPLATE USED      |
|                                         | CCHT STRAINED WITH RELATIVES=FREQUENTLY   |
|                                         | CCHT STRAINED WITH RELATIVES=NEVER        |
|                                         | CCHT STRAINED WITH RELATIVES=NRLY ALWAYS  |
|                                         | CCHT STRAINED WITH RELATIVES=RARELY       |
|                                         | CCHT STRAINED WITH RELATIVES=SOMETIMES    |
|                                         | CCHT STRESSED WORK/FAMILY=FREQUENTLY      |
|                                         | CCHT STRESSED WORK/FAMILY=NEARLY ALWAYS   |
|                                         | CCHT STRESSED WORK/FAMILY=NEVER           |
|                                         | CCHT STRESSED WORK/FAMILY=RARELY          |
|                                         | CCHT STRESSED WORK/FAMILY=SOMETIMES       |
| HT TEACH CAREGIVER/FAMILY/SIGNIF OTHER  |                                           |
|                                         | CCHT TECH EDUCATION TEMPLATE USED         |
| HT TECH EDUC DEVICE ASSIGNED            |                                           |
|                                         | CCHT TELEHEALTH COORDINATOR (NAME)        |
| **HT TELEHEALTH DELIVERY/INSTALL MODE** | **CCHT TELEHEALTH DELIVERY/INSTALL MODE** |
| **HT TELEHEALTH DEMOGRAPHICS**          | **CCHT TELEHEALTH DEMOGRAPHICS**          |
|                                         | **CCHT TELEHEALTH DEVICE(S)**             |
|                                         | CCHT TEMPLATE USE (PHASE 3)               |
| HT TOILET HELP/SUPERVISION LAST 7D-NO   | CCHT TOILET HELP/SUPERVISION LAST 7D-NO   |
| HT TOILET HELP/SUPERVISION LAST 7D-YES  | CCHT TOILET HELP/SUPERVISION LAST 7D-YES  |
| HT TRANSFERS HELP/SUPERV LAST 7D-NO     | CCHT TRANSFERS HELP/SUPERV LAST 7D-NO     |
| HT TRANSFERS HELP/SUPERV LAST 7D-YES    | CCHT TRANSFERS HELP/SUPERV LAST 7D-YES    |
| HT UNABLE TO SCREEN CAREGIVER           |                                           |

| HT VET NOT INTERESTED TELEHEALTH PROGRAM   | HT VET NOT INTERESTED TELEHEALTH PROGRAM   |
|--------------------------------------------|--------------------------------------------|
| HT VET/CAREGIVER VIEW VIDEOS/HEALTH TV     |                                            |
|                                            | CCHT UNCERTAIN WHAT TO DO=FREQUENTLY       |
|                                            | CCHT UNCERTAIN WHAT TO DO=NEARLY ALWAYS    |
|                                            | CCHT UNCERTAIN WHAT TO DO=NEVER            |
|                                            | CCHT UNCERTAIN WHAT TO DO=RARELY           |
|                                            | CCHT UNCERTAIN WHAT TO DO=SOMETIMES        |
|                                            | CCHT VETERAN REFERRAL ADULT DAY CARE       |
| HT VETERAN REFERRAL EDUC/TRAINING          | CCHT VETERAN REFERRAL EDUC/TRAINING        |
|                                            | CCHT VETERAN REFERRAL EMPLOYMENT ASSIST    |
|                                            | CCHT VETERAN REFERRAL FAMILY COUNSEL       |
|                                            | CCHT VETERAN REFERRAL FINANCIAL ASSIST     |
|                                            | CCHT VETERAN REFERRAL HOME HEALTH SVC      |
|                                            | CCHT VETERAN REFERRAL HOMEMKR/CHORE ASST   |
|                                            | CCHT VETERAN REFERRAL HOSPICE              |
|                                            | CCHT VETERAN REFERRAL HOUSING              |
|                                            | CCHT VETERAN REFERRAL INDIVIDUAL COUNSEL   |
|                                            | CCHT VETERAN REFERRAL LEGAL ASSIST         |
|                                            | CCHT VETERAN REFERRAL MEDICAL EVAL, F/U    |
|                                            | CCHT VETERAN REFERRAL NURS HOME PLACEMNT   |
| HT VETERAN REFERRAL OTHER SERVICE          | CCHT VETERAN REFERRAL OTHER SERVICE        |
|                                            | CCHT VETERAN REFERRAL RESPITE              |
|                                            | CCHT VETERAN REFERRAL SOCIAL WORK          |
| HT VETERAN REFERRAL SVCS IN PLACE          | CCHT VETERAN REFERRAL SVCS IN PLACE        |
|                                            | CCHT VETERAN REFERRAL TRANSPORTATION       |
| HT VETERAN REFERRAL(S) NON VA SYSTEM       | CCHT VETERAN REFERRAL(S) NON VA SYSTEM     |
| HT VETERAN REFERRAL(S) VA SYSTEM           | CCHT VETERAN REFERRAL(S) VA SYSTEM         |
| HT VETERAN REVIEW OF WRITTEN MATERIALS     |                                            |
| HT VETERAN STATES ESSENTIAL CONCEPTS       |                                            |
| HT VETERAN'S GOAL FOR ENROLLMENT           | CCHT VETERAN'S GOAL FOR ENROLLMENT         |
|                                            | CCHT VIDEO VISIT TEMPLATE USED             |
|                                            | CCHT VIDEO VISIT-AUDIO/VIDEO CONNECTION    |
|                                            | CCHT VIDEOPHONE SERIAL #                   |
| HT W/C MOBIL HELP/SUPERV LAST 7D-NO        | CCHT W/C MOBIL HELP/SUPERV LAST 7D-NO      |
| HT W/C MOBIL HELP/SUPERV LAST 7D-YES       | CCHT W/C MOBIL HELP/SUPERV LAST 7D-YES     |
| **PREFERRED HEALTHCARE LANGUAGE**          |                                            |
| PREFERRED HEALTHCARE LANGUAGE-ASL          |                                            |
| PREFERRED HEALTHCARE LANGUAGE-BRAILLE      |                                            |
| PREFERRED HEALTHCARE LANGUAGE-CHINESE      | PREFERRED HEALTHCARE LANGUAGE-CHINESE      |
| PREFERRED HEALTHCARE LANGUAGE-ENGLISH      | PREFERRED HEALTHCARE LANGUAGE-ENGLISH      |
| PREFERRED HEALTHCARE LANGUAGE-FRENCH       | PREFERRED HEALTHCARE LANGUAGE-FRENCH       |

| PREFERRED HEALTHCARE LANGUAGE-GERMAN       | PREFERRED HEALTHCARE LANGUAGE-GERMAN     |
|--------------------------------------------|------------------------------------------|
| PREFERRED HEALTHCARE LANGUAGE-ITALIAN      |                                          |
| PREFERRED HEALTHCARE LANGUAGE-KOREAN       | PREFERRED HEALTHCARE LANGUAGE-KOREAN     |
| PREFERRED HEALTHCARE LANGUAGE-OTHER        |                                          |
| PREFERRED HEALTHCARE LANGUAGE-PORTUGUESE   | PREFERRED HEALTHCARE LANGUAGE-PORTUGUESE |
| PREFERRED HEALTHCARE LANGUAGE-RUSSIAN      | PREFERRED HEALTHCARE LANGUAGE-RUSSIAN    |
| PREFERRED HEALTHCARE LANGUAGE-SPANISH      | PREFERRED HEALTHCARE LANGUAGE-SPANISH    |
| PREFERRED HEALTHCARE LANGUAGE-TAGALOG      | PREFERRED HEALTHCARE LANGUAGE-TAGALOG    |
| PREFERRED HEALTHCARE LANGUAGE-  VIETNAMESE |                                          |

#### Appendix C: HT Queued MailMan Report

When the HT TEMPLATES build is installed, a single MailMan message will be sent. Message subjects will be:

- LOCAL CCHT HFs NOT USED IN NAT’L HT REMINDER DIALOG CONTENT This report will build a list of all health factors on the system where:
    - Considered “local” (file IEN 100,000 or greater), **and**
        - Factor contains “CCHT” or “CARE COORDINATION HOME TELEHEALTH”, **or**
        - Category contains “CCHT” or “CARE COORDINATION HOME TELEHEALTH”
    - **And** the health factor is not used by any of the new HT clinical reminder content

This report is automatically run as part of the post-installation process for patch PXRM*2.0*19. The MailMan message generated by this report is sent to the recipients chosen by the person installing the patch bundle. This first run of this report is intended as a baseline in order to assist sites with configuration and/or any necessary cleanup related to Home Telehealth health factors. NOTE: A health factor appearing in this report should only be interpreted to mean that the health factor is not part of the HT Templates build. These health factors could actually be in use **outside** of the National HT dialogs. Any given health factor should **not** be deleted/deprecated/inactivated based solely on this report. Any such decisions should be made in concert with the local facility personnel who can best determine how/where a given health factor is or is not being used.

After any cleanup/configuration issues are resolved, the report may be run again, as needed, to verify no outstanding issues are remaining. To run the report again, you will need a programmer’s assistance. That individual will need to execute the following program:

DEV&gt;D MAIN^PXRMP19A

The program will, again, generate the MailMan message with one slight difference in delivery. When not run as part of the post-installation, the report will be sent directly to the programmer executing the code (DUZ). That person should forward the message to the appropriate points-of- contact. No new menu options were created for this report due to its temporary nature and the fact that a subsequent national patch would have been necessary to remove it from the OPTION file.

###### LOCAL CCHT HFs NOT USED IN NAT’L HT REMINDER DIALOGS CONTENT

Purpose: Provides information to sites on status of Health Factors on system vs. National dialogs. This report attempts to find all local Health Factors that are NOT used in the National dialogs for HT. This is done via building a list of local Health Factors whose name contains “CCHT” or “HOME TELEHEALTH” and then comparing that list to the Health Factors used in the National dialogs.

Subj: LOCAL CCHT HFs NOT USED IN NAT'L HT REMINDER DIALOG CONTENT	[#65148]

02/22/11@12:27	60 lines

From: Clinical Reminders Support	In 'IN' basket.	Page 1	*New*

HEALTH FACTOR

CATEGORY

INACTIVE?

CCHT APPROX DELIVERY DATE FOR EQUIPMENT  CCHT TELEHEALTH DELIVERY/INSTALL MODE

NO

CCHT BATHING HELP/SUPRVISION LAST 7D-NO CCHT CONTINUUM OF CARE

CCHT BATHING HELP/SUPRVISION LAST 7D-YES CCHT CONTINUUM OF CARE

CCHT BED MOBIL HELP/SUPERV LAST 7D-NO CCHT CONTINUUM OF CARE

CCHT BED MOBIL HELP/SUPERV LAST 7D-YES CCHT CONTINUUM OF CARE

CCHT CAREGIVER ASSESSMENT SCREEN DONE

CCHT CAREGIVER RISK ASSESSMENT SCREEN

CCHT CAREGIVER ASSESSMENT TEMPLATE USED CCHT TEMPLATE USE (PHASE 3)

CCHT CAREGIVER RISK ASSESSMENT SCORE 0

CCHT CAREGIVER RISK ASSESSMENT SCORE 1

CCHT CAREGIVER RISK ASSESSMENT SCORE 10  CCHT CAREGIVER RISK ASSESSMENT SCREEN

CCHT CAREGIVER RISK ASSESSMENT SCORE 11  CCHT CAREGIVER RISK ASSESSMENT SCREEN

CCHT CAREGIVER RISK ASSESSMENT SCORE 12  CCHT CAREGIVER RISK ASSESSMENT SCREEN

CCHT CAREGIVER RISK ASSESSMENT SCORE 13  CCHT CAREGIVER RISK ASSESSMENT SCREEN

CCHT CAREGIVER RISK ASSESSMENT SCORE 14

CCHT CAREGIVER RISK ASSESSMENT SCORE 15  CCHT CAREGIVER RISK ASSESSMENT SCREEN

CCHT CAREGIVER RISK ASSESSMENT SCORE 16

###### SAMPLE

|      | CCHT CAREGIVER RISK ASSESSMENT SCREEN                                    | NO   |
|------|--------------------------------------------------------------------------|------|
| CCHT | CAREGIVER RISK ASSESSMENT SCORE 2  CCHT CAREGIVER RISK ASSESSMENT SCREEN | NO   |
| CCHT | CAREGIVER RISK ASSESSMENT SCORE 3  CCHT CAREGIVER RISK ASSESSMENT SCREEN | NO   |
| CCHT | CAREGIVER RISK ASSESSMENT SCORE 4  CCHT CAREGIVER RISK ASSESSMENT SCREEN | NO   |
| CCHT | CAREGIVER RISK ASSESSMENT SCORE 5  CCHT CAREGIVER RISK ASSESSMENT SCREEN | NO   |
| CCHT | CAREGIVER RISK ASSESSMENT SCORE 6  CCHT CAREGIVER RISK ASSESSMENT SCREEN | NO   |
| CCHT | CAREGIVER RISK ASSESSMENT SCORE 7  CCHT CAREGIVER RISK ASSESSMENT SCREEN | NO   |
| CCHT | CAREGIVER RISK ASSESSMENT SCORE 8  CCHT CAREGIVER RISK ASSESSMENT SCREEN | NO   |
| CCHT | CAREGIVER RISK ASSESSMENT SCORE 9  CCHT CAREGIVER RISK ASSESSMENT SCREEN | NO   |
| CCHT | CATEGORY-ACUTE CARE  CCHT ASSESSMENT/TREATMENT PLAN                      | NO   |
| CCHT | CATEGORY-CHRONIC CARE  CCHT ASSESSMENT/TREATMENT PLAN                    | NO   |
| CCHT | CATEGORY-HEALTH PROMOTION  CCHT ASSESSMENT/TREATMENT PLAN                | NO   |
| CCHT | CATEGORY-NON INSTITUTIONAL CARE CCHT ASSESSMENT/TREATMENT PLAN           | NO   |
| CCHT | CATEGORY-TELEPHONE CASE MANAGEMENT CCHT ASSESSMENT/TREATMENT PLAN        | NO   |
| CCHT | CCF 1 OR MORE BEHAV/COGN PROBLEMS CCHT CONTINUUM OF CARE                 | NO   |
| CCHT | CCF 12 OR MORE CLINIC STOPS CCHT CONTINUUM OF CARE                       | NO   |
| CCHT | CCF 2 OR MORE ADL DEFICITS CCHT CONTINUUM OF CARE                        | NO   |
| CCHT | CCF AGE 75 OR GREATER CCHT CONTINUUM OF CARE                             | NO   |
| CCHT | CCF AGITATED/DISORIENTED-NO CCHT CONTINUUM OF CARE                       | NO   |
| CCHT | CCF AGITATED/DISORIENTED-YES CCHT CONTINUUM OF CARE                      | NO   |
| CCHT | CCF CAREGIVER ACCESSIBLE CCHT CONTINUUM OF CARE                          | NO   |
| CCHT | CCF CAREGIVER CAN INCREASE HELP                                          |      |

| CCHT CONTINUUM OF CARE	NO  CCHT CCF CAREGIVER CAN'T INCREASE HELP  CCHT CONTINUUM OF CARE	NO  CCHT CCF CAREGIVER LIVES WITH PT-NO  CCHT CONTINUUM OF CARE	NO  CCHT CCF CAREGIVER LIVES WITH PT-YES  CCHT CONTINUUM OF CARE	NO  CCHT CCF CAREGIVER NOT ACCESSIBLE  CCHT CONTINUUM OF CARE	NO  CCHT CCF CAREGIVER SAME NAME AS PT  CCHT CONTINUUM OF CARE	NO   |                                                        |    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|----|
| CCHT                                                                                                                                                                                                                                                                                                                                                         | CCF CAREGIVER'S CITY CCHT CONTINUUM OF CARE            | NO |
| CCHT                                                                                                                                                                                                                                                                                                                                                         | CCF CAREGIVER'S NAME CCHT CONTINUUM OF CARE            | NO |
| CCHT                                                                                                                                                                                                                                                                                                                                                         | CCF CAREGIVER'S PHONE CCHT CONTINUUM OF CARE           | NO |
| CCHT                                                                                                                                                                                                                                                                                                                                                         | CCF CAREGIVER'S STATE CCHT CONTINUUM OF CARE           | NO |
| CCHT                                                                                                                                                                                                                                                                                                                                                         | CCF CAREGIVER'S STREET ADDRESS CCHT CONTINUUM OF CARE  | NO |
| CCHT                                                                                                                                                                                                                                                                                                                                                         | CCF CAREGIVER'S ZIP CODE CCHT CONTINUUM OF CARE        | NO |
| CCHT                                                                                                                                                                                                                                                                                                                                                         | CCF CAREGIVER-ADL HELP CCHT CONTINUUM OF CARE          | NO |
| CCHT                                                                                                                                                                                                                                                                                                                                                         | CCF  CAREGIVER-CHILD CCHT CONTINUUM OF CARE            | NO |
| CCHT                                                                                                                                                                                                                                                                                                                                                         | CCF CAREGIVER-EMOTIONAL SUPPORT CCHT CONTINUUM OF CARE | NO |
| CCHT                                                                                                                                                                                                                                                                                                                                                         | CCF CAREGIVER-FRIEND/NEIGHBOR CCHT CONTINUUM OF CARE   | NO |
| CCHT                                                                                                                                                                                                                                                                                                                                                         | CCF CAREGIVER-IADL HELP CCHT CONTINUUM OF CARE         | NO |
| CCHT                                                                                                                                                                                                                                                                                                                                                         | CCF  CAREGIVER-OTHER CCHT CONTINUUM OF CARE            | NO |
| CCHT                                                                                                                                                                                                                                                                                                                                                         | CCF CAREGIVER-SPOUSE CCHT CONTINUUM OF CARE            | NO |
| CCHT                                                                                                                                                                                                                                                                                                                                                         | CCF COMPLEXITY TOO GREAT-NO CCHT CONTINUUM OF CARE     | NO |
| CCHT                                                                                                                                                                                                                                                                                                                                                         | CCF COMPLEXITY TOO GREAT-YES CCHT CONTINUUM OF CARE    | NO |
| CCHT                                                                                                                                                                                                                                                                                                                                                         | CCF DELUSIONS-NO                                       |    |

|      | CCHT CONTINUUM OF CARE                                     | NO   |
|------|------------------------------------------------------------|------|
| CCHT | CCF DELUSIONS-YES  CCHT CONTINUUM OF CARE                  | NO   |
| CCHT | CCF DIFFIC MAKE SELF UNDERSTOOD-NO CCHT CONTINUUM OF CARE  | NO   |
| CCHT | CCF DIFFIC MAKE SELF UNDERSTOOD-YES CCHT CONTINUUM OF CARE | NO   |
| CCHT | CCF DIFFIC REASONABLE DECISIONS-NO CCHT CONTINUUM OF CARE  | NO   |
| CCHT | CCF DIFFIC REASONABLE DECISIONS-YES CCHT CONTINUUM OF CARE | NO   |
| CCHT | CCF DOES NOT MEET NIC CRITERIA CCHT CONTINUUM OF CARE      | NO   |
| CCHT | CCF FLARE UP CHRONIC CONDITION-NO CCHT CONTINUUM OF CARE   | NO   |
| CCHT | CCF FLARE UP CHRONIC CONDITION-YES CCHT CONTINUUM OF CARE  | NO   |
| CCHT | CCF FOLLOW-UP ASSESSMENT DONE CCHT CONTINUUM OF CARE       | NO   |
| CCHT | CCF GROUP SETTING NON RELATIVES CCHT CONTINUUM OF CARE     | NO   |
| CCHT | CCF HALLUCINATIONS-AUDITORY CCHT CONTINUUM OF CARE         | NO   |
| CCHT | CCF HALLUCINATIONS-NONE CCHT CONTINUUM OF CARE             | NO   |
| CCHT | CCF HALLUCINATIONS-OLFACTORY CCHT CONTINUUM OF CARE        | NO   |
| CCHT | CCF HALLUCINATIONS-SENSORY CCHT CONTINUUM OF CARE          | NO   |
| CCHT | CCF HALLUCINATIONS-TACTILE CCHT CONTINUUM OF CARE          | NO   |
| CCHT | CCF HALLUCINATIONS-VISUAL CCHT CONTINUUM OF CARE           | NO   |
| CCHT | CCF INITIAL ASSESSMENT DONE CCHT CONTINUUM OF CARE         | NO   |
| CCHT | CCF LIFE EXPECTANCY < 6 MO CCHT CONTINUUM OF CARE          | NO   |
| CCHT | CCF LIVES ALONE  CCHT CONTINUUM OF CARE                    | NO   |
| CCHT | CCF LIVES ALONE IN COMMUNITY CCHT CONTINUUM OF CARE        | NO   |
| CCHT | CCF LIVES AT OTHER                                         |      |

|      | CCHT CONTINUUM OF CARE                                     | NO   |
|------|------------------------------------------------------------|------|
| CCHT | CCF LIVES BOARD AND CARE CCHT CONTINUUM OF CARE            | NO   |
| CCHT | CCF LIVES DOMICILIARY CCHT CONTINUUM OF CARE               | NO   |
| CCHT | CCF LIVES HOMELESS  CCHT CONTINUUM OF CARE                 | NO   |
| CCHT | CCF LIVES HOMELESS SHELTER CCHT CONTINUUM OF CARE          | NO   |
| CCHT | CCF LIVES NURSING HOME CCHT CONTINUUM OF CARE              | NO   |
| CCHT | CCF LIVES PRIVATE HOME CCHT CONTINUUM OF CARE              | NO   |
| CCHT | CCF LIVES WITH ADULT CHILD CCHT CONTINUUM OF CARE          | NO   |
| CCHT | CCF LIVES WITH CHILD CCHT CONTINUUM OF CARE                | NO   |
| CCHT | CCF LIVES WITH OTHER CCHT CONTINUUM OF CARE                | NO   |
| CCHT | CCF LIVES WITH SPOUSE & OTHERS CCHT CONTINUUM OF CARE      | NO   |
| CCHT | CCF LIVES WITH SPOUSE ONLY CCHT CONTINUUM OF CARE          | NO   |
| CCHT | CCF MEETS NIC CATEGORY A CRITERIA CCHT CONTINUUM OF CARE   | NO   |
| CCHT | CCF MEETS NIC CATEGORY B CRITERIA CCHT CONTINUUM OF CARE   | NO   |
| CCHT | CCF MEETS NIC CRITERIA CCHT CONTINUUM OF CARE              | NO   |
| CCHT | CCF MOOD DISORDER DEPRESSION-NO CCHT CONTINUUM OF CARE     | NO   |
| CCHT | CCF MOOD DISORDER DEPRESSION-YES CCHT CONTINUUM OF CARE    | NO   |
| CCHT | CCF MOOD DISORDER MANIC-NO CCHT CONTINUUM OF CARE          | NO   |
| CCHT | CCF MOOD DISORDER MANIC-YES CCHT CONTINUUM OF CARE         | NO   |
| CCHT | CCF NIC CRITERIA NO-ACUTE CARE MGMT CCHT CONTINUUM OF CARE | NO   |
| CCHT | CCF NIC CRITERIA NO-HLTH PROMOTION CCHT CONTINUUM OF CARE  | NO   |
| CCHT | CCF PHYSICALLY ABUSIVE BEHAVIOR-NO                         |      |

|      | CCHT CONTINUUM OF CARE                                     | NO   |
|------|------------------------------------------------------------|------|
| CCHT | CCF PHYSICALLY ABUSIVE BEHAVIOR-YES CCHT CONTINUUM OF CARE | NO   |
| CCHT | CCF POTENTIAL FOR INCR INDEP-NO CCHT CONTINUUM OF CARE     | NO   |
| CCHT | CCF POTENTIAL FOR INCR INDEP-YES CCHT CONTINUUM OF CARE    | NO   |
| CCHT | CCF PROBLEMS IN 3 OR MORE ADLS CCHT CONTINUUM OF CARE      | NO   |
| CCHT | CCF PROBLEMS WITH 3 OR MORE IADL CCHT CONTINUUM OF CARE    | NO   |
| CCHT | CCF PTSD/OTHER ANXIETY-NO CCHT CONTINUUM OF CARE           | NO   |
| CCHT | CCF PTSD/OTHER ANXIETY-YES CCHT CONTINUUM OF CARE          | NO   |
| CCHT | CCF RECOMMEND REFERRAL CCHT CONTINUUM OF CARE              | NO   |
| CCHT | CCF RECOMMEND REFERRAL-NO CCHT CONTINUUM OF CARE           | NO   |
| CCHT | CCF RESISTING CARE-NO CCHT CONTINUUM OF CARE               | NO   |
| CCHT | CCF RESISTING CARE-YES CCHT CONTINUUM OF CARE              | NO   |
| CCHT | CCF SERVICES IN PLACE-NO CCHT CONTINUUM OF CARE            | NO   |
| CCHT | CCF SERVICES IN PLACE-YES CCHT CONTINUUM OF CARE           | NO   |
| CCHT | CCF SUBST ABUSE/DEPENDENCE-NO CCHT CONTINUUM OF CARE       | NO   |
| CCHT | CCF SUBST ABUSE/DEPENDENCE-YES CCHT CONTINUUM OF CARE      | NO   |
| CCHT | CCF UNPAID CAREGIVER-NO CCHT CONTINUUM OF CARE             | NO   |
| CCHT | CCF UNPAID CAREGIVER-YES CCHT CONTINUUM OF CARE            | NO   |
| CCHT | CCF VERBALLY ABUSIVE BEHAVIOR-NO CCHT CONTINUUM OF CARE    | NO   |
| CCHT | CCF VERBALLY ABUSIVE BEHAVIOR-YES CCHT CONTINUUM OF CARE   | NO   |
| CCHT | CCF WANDERING-NO  CCHT CONTINUUM OF CARE                   | NO   |
| CCHT | CCF WANDERING-YES                                          |      |

|      | CCHT CONTINUUM OF CARE                                                   | NO   |
|------|--------------------------------------------------------------------------|------|
| CCHT | CG/VETERAN REFERRAL TEMPLATE  DONE CCHT REFERRALS FOR VETERAN/CAREGIVER  | NO   |
| CCHT | CG/VETERAN REFERRAL(S) NOT UTILIZED CCHT REFERRALS FOR VETERAN/CAREGIVER | NO   |
| CCHT | CLINICAL REASON FOR ENROLLMENT CCHT (HOME TELEHEALTH)                    | NO   |
| CCHT | CONTACT MADE FOR EQUIP RETURN CCHT DISCHARGE                             | NO   |
| CCHT | CONTINUUM OF CARE TEMPLATE USED CCHT TEMPLATE USE (PHASE 3)              | NO   |
| CCHT | DIFFICULT MANAGING MEDS/LAST 7D-NO CCHT CONTINUUM OF CARE                | NO   |
| CCHT | DIFFICULT MANAGING MEDS/LAST 7D-YES CCHT CONTINUUM OF CARE               | NO   |
| CCHT | DIFFICULT MNG FINANCES/LAST 7D-NO CCHT CONTINUUM OF CARE                 | NO   |
| CCHT | DIFFICULT MNG FINANCES/LAST 7D-YES CCHT CONTINUUM OF CARE                | NO   |
| CCHT | DIFFICULT PREPARE MEALS/LAST 7D-YES CCHT CONTINUUM OF CARE               | NO   |
| CCHT | DIFFICULT TRANSPRTATION/LAST 7D-NO CCHT CONTINUUM OF CARE                | NO   |
| CCHT | DIFFICULT TRANSPRTATION/LAST 7D-YES CCHT CONTINUUM OF CARE               | NO   |
| CCHT | DIFFICULT USING PHONE LAST 7D-NO CCHT CONTINUUM OF CARE                  | NO   |
| CCHT | DIFFICULT USING PHONE LAST 7D-YES CCHT CONTINUUM OF CARE                 | NO   |
| CCHT | DIFFICULT W/ HOUSEWORK/LAST 7D-NO CCHT CONTINUUM OF CARE                 | NO   |
| CCHT | DIFFICULT W/ HOUSEWORK/LAST 7D-YES CCHT CONTINUUM OF CARE                | NO   |
| CCHT | DIFFICULT WITH SHOPPING/LAST 7D-NO CCHT CONTINUUM OF CARE                | NO   |
| CCHT | DIFFICULT WITH SHOPPING/LAST 7D-YES CCHT CONTINUUM OF CARE               | NO   |
| CCHT | DIGITAL CAMERA SERIAL # CCHT TELEHEALTH DEVICE(S)                        | NO   |
| CCHT | DISCHARGE-ADMITTED TO NURSING HOME CCHT DISCHARGE                        | NO   |
| CCHT | DISCHARGE-ALL EQUIP RETURNED (NO)                                        |      |

|      | CCHT DISCHARGE                                     | NO   |
|------|----------------------------------------------------|------|
| CCHT | DISCHARGE-ALL EQUIP RETURNED (YES) CCHT DISCHARGE  | NO   |
| CCHT | DISCHARGE-ALL ISSUES ADDRESSED(NO) CCHT DISCHARGE  | NO   |
| CCHT | DISCHARGE-ALL ISSUES ADDRESSED(YES) CCHT DISCHARGE | NO   |
| CCHT | DISCHARGE-EQUIP RETURN (OTHER) CCHT DISCHARGE      | NO   |
| CCHT | DISCHARGE-HAS MET GOALS CCHT DISCHARGE             | NO   |
| CCHT | DISCHARGE-NO RESPONSE TO PROGRAM CCHT DISCHARGE    | NO   |
| CCHT | DISCHARGE-NO VA PRIMARY CARE SVCS CCHT DISCHARGE   | NO   |
| CCHT | DISCHARGE-OTHER FOLLOW-UP CCHT DISCHARGE           | NO   |
| CCHT | DISCHARGE-PATIENT IS DECEASED CCHT DISCHARGE       | NO   |
| CCHT | DISCHARGE-PHONE,ELECT SVCS UNAVAIL CCHT DISCHARGE  | NO   |
| CCHT | DISCHARGE-PROLONGED HOSPITALIZATION CCHT DISCHARGE | NO   |
| CCHT | DISCHARGE-PROVIDER REQUESTS DC CCHT DISCHARGE      | NO   |
| CCHT | DISCHARGE-PT/CG REQUEST DC SERVICES CCHT DISCHARGE | NO   |
| CCHT | DISCHARGE-REFERRED TO HOSPICE CCHT DISCHARGE       | NO   |
| CCHT | DISCHARGE-REFERRED TO MENTAL HEALTH CCHT DISCHARGE | NO   |
| CCHT | DISCHARGE-REFERRED TO NEW LOCATION CCHT DISCHARGE  | NO   |
| CCHT | DISCHARGE-REFERRED TO PRIMARY CARE CCHT DISCHARGE  | NO   |
| CCHT | DISCHARGE-REFERRED TO SOCIAL WORK CCHT DISCHARGE   | NO   |
| CCHT | DISCHARGE-RELOCATED OUT OF SVC AREA CCHT DISCHARGE | NO   |
| CCHT | DISCHARGE-UNABLE TO OPERATE DEVICES CCHT DISCHARGE | NO   |
| CCHT | DISEASE INDICATIONS-CHF                            |      |

| CCHT TELEHEALTH DEMOGRAPHICS	NO   | CCHT TELEHEALTH DEMOGRAPHICS	NO                                   | CCHT TELEHEALTH DEMOGRAPHICS	NO   | CCHT TELEHEALTH DEMOGRAPHICS	NO   |
|-----------------------------------|-------------------------------------------------------------------|-----------------------------------|-----------------------------------|
| CCHT                              | DISEASE INDICATIONS-COPD  CCHT TELEHEALTH DEMOGRAPHICS            |                                   | NO                                |
| CCHT                              | DISEASE INDICATIONS-DEPRESSION CCHT TELEHEALTH DEMOGRAPHICS       |                                   | NO                                |
| CCHT                              | DISEASE INDICATIONS-DIABETES CCHT TELEHEALTH DEMOGRAPHICS         |                                   | NO                                |
| CCHT                              | DISEASE INDICATIONS-HYPERTENSION CCHT TELEHEALTH DEMOGRAPHICS     |                                   | NO                                |
| CCHT                              | DISEASE  INDICATIONS-OTHER CCHT TELEHEALTH DEMOGRAPHICS           |                                   | NO                                |
| CCHT                              | DISEASE INDICATIONS-PTSD  CCHT TELEHEALTH DEMOGRAPHICS            |                                   | NO                                |
| CCHT                              | DISEASE INDICATIONS-SUBST ABUSE CCHT TELEHEALTH DEMOGRAPHICS      |                                   | NO                                |
| CCHT                              | DRESSING HELP/SUPERV LAST 7D-NO CCHT CONTINUUM OF CARE            |                                   | NO                                |
| CCHT                              | DRESSING HELP/SUPERV LAST 7D-YES CCHT CONTINUUM OF CARE           |                                   | NO                                |
| CCHT                              | EATING HELP/SUPERVISION LAST 7D-NO CCHT CONTINUUM OF CARE         |                                   | NO                                |
| CCHT                              | EATING HELP/SUPERVISION LAST 7D-YES CCHT CONTINUUM OF CARE        |                                   | NO                                |
| CCHT                              | EDUC ON EQUIP-CARE COORDINATOR CCHT TELEHEALTH DEMOGRAPHICS       |                                   | NO                                |
| CCHT                              | EDUC ON EQUIP-CONTRACT VENDOR CCHT TELEHEALTH DEMOGRAPHICS        |                                   | NO                                |
| CCHT                              | EDUC ON EQUIP-SUPPORT STAFF CCHT TELEHEALTH DEMOGRAPHICS          |                                   | NO                                |
| CCHT                              | EMERG PRIORITY HIGH-IMMEDIATE EVAL CCHT ASSESSMENT/TREATMENT PLAN |                                   | NO                                |
| CCHT                              | EMERG PRIORITY LOW-HAS RESOURCES CCHT ASSESSMENT/TREATMENT PLAN   |                                   | NO                                |
| CCHT                              | EMERG PRIORITY MOD-SVCS AFTER 3-7D CCHT ASSESSMENT/TREATMENT PLAN |                                   | NO                                |
| CCHT                              | ENROLLMENT-ENDING DATE CCHT (HOME TELEHEALTH)                     |                                   | NO                                |
| CCHT                              | ENROLLMENT-START DATE CCHT (HOME TELEHEALTH)                      |                                   | NO                                |
| CCHT                              | EQUIP INSTALLATION  MODE-OTHER CCHT TELEHEALTH DELIVERY/INSTALL   | MODE                              | NO                                |
| CCHT                              | EQUIP INSTALLED BY CARE COORDINATOR                               |                                   |                                   |

|      | CCHT TELEHEALTH DELIVERY/INSTALL MODE                                     | NO   |
|------|---------------------------------------------------------------------------|------|
| CCHT | EQUIP INSTALLED BY CONTRACT VENDOR  CCHT TELEHEALTH DELIVERY/INSTALL MODE | NO   |
| CCHT | EQUIP INSTALLED BY SUPPORT STAFF  CCHT TELEHEALTH DELIVERY/INSTALL MODE   | NO   |
| CCHT | EQUIP INSTALLED BY  VETERAN/CAREGVR CCHT TELEHEALTH DELIVERY/INSTALL MODE | NO   |
| CCHT | EQUIP MAILED,INSTALL BY VET/CAREGVR CCHT TELEHEALTH DELIVERY/INSTALL MODE | NO   |
| CCHT | EQUIP TAKEN HOME,INSTALL BY VET/CG  CCHT TELEHEALTH DELIVERY/INSTALL MODE | NO   |
| CCHT | INDICATIONS-# OUTPT VISITS PAST YR CCHT TELEHEALTH DEMOGRAPHICS           | NO   |
| CCHT | INDICATIONS-DISTANCE (HOURS) CCHT TELEHEALTH DEMOGRAPHICS                 | NO   |
| CCHT | INDICATIONS-DISTANCE (MILES) CCHT TELEHEALTH DEMOGRAPHICS                 | NO   |
| CCHT | INDICATIONS-HX HIGH COST/HIGH USE CCHT TELEHEALTH DEMOGRAPHICS            | NO   |
| CCHT | INDICATIONS-HX HOSPITALIZATONS CCHT TELEHEALTH DEMOGRAPHICS               | NO   |
| CCHT | LEARNING BARRIER-LANGUAGE  CCHT ASSESSMENT/TREATMENT PLAN                 | NO   |
| CCHT | LEARNING BARRIER-NONE IDENTIFIED CCHT ASSESSMENT/TREATMENT PLAN           | NO   |
| CCHT | LEARNING BARRIER-UNABLE TO READ CCHT ASSESSMENT/TREATMENT PLAN            | NO   |
| CCHT | LEARNING BARRIER-VISUALLY IMPAIRED CCHT ASSESSMENT/TREATMENT PLAN         | NO   |
| CCHT | MAKE TIME FOR SELF=FREQUENTLY  CCHT CAREGIVER RISK ASSESSMENT SCREEN      | NO   |
| CCHT | MAKE TIME FOR SELF=NEARLY ALWAYS  CCHT CAREGIVER RISK ASSESSMENT SCREEN   | NO   |
| CCHT | MAKE TIME FOR SELF=NEVER  CCHT CAREGIVER RISK ASSESSMENT SCREEN           | NO   |
| CCHT | MAKE TIME FOR SELF=RARELY  CCHT CAREGIVER RISK ASSESSMENT SCREEN          | NO   |
| CCHT | MAKE TIME FOR SELF=SOMETIMES  CCHT CAREGIVER RISK ASSESSMENT SCREEN       | NO   |
| CCHT | MEALS PREPARED BY OTHER/LAST 7D-NO CCHT CONTINUUM OF CARE                 | NO   |
| CCHT | MEALS PREPARED BY OTHER/LAST 7D-YES                                       |      |

CCHT CONTINUUM OF CARE	NO

CCHT MEASURING DEVICE-OTHER

CCHT TELEHEALTH DEVICE(S)	NO

CCHT MEDS ADAPT-FOR VISUAL IMPAIRMENT

CCHT ASSESSMENT/TREATMENT PLAN	NO

CCHT MEDS ADAPT-MEDS ARE COLOR CODED

CCHT ASSESSMENT/TREATMENT PLAN	NO

CCHT MEDS ADAPT-USES PILLBOX

CCHT ASSESSMENT/TREATMENT PLAN	NO

CCHT MEDS ADAPT-VA PREPARES/POURS MEDS

CCHT ASSESSMENT/TREATMENT PLAN	NO

CCHT MEDS ADAPTATIONS-NONE NEEDED

CCHT ASSESSMENT/TREATMENT PLAN	NO

CCHT MEDS ADAPTATIONS-OTHER

CCHT ASSESSMENT/TREATMENT PLAN	NO

CCHT MEDS SPECIAL ADAPTATIONS

CCHT ASSESSMENT/TREATMENT PLAN	NO

CCHT MEETS TELEHEALTH CRITERIA(NO)

CCHT TELEHEALTH DEMOGRAPHICS	NO

CCHT MEETS TELEHEALTH CRITERIA(YES)

CCHT TELEHEALTH DEMOGRAPHICS	NO

CCHT MESSAGING DEVICE TYPE/SERIAL #

CCHT TELEHEALTH DEVICE(S)	NO

CCHT MESSAGING DEVICE-BLOOD GLUCOSE

CCHT TELEHEALTH DEVICE(S)	NO

CCHT MESSAGING DEVICE-BLOOD PRESSURE

CCHT TELEHEALTH DEVICE(S)	NO

CCHT MESSAGING DEVICE-PULSE

CCHT TELEHEALTH DEVICE(S)	NO

CCHT MESSAGING DEVICE-PULSE OXIMETRY

CCHT TELEHEALTH DEVICE(S)	NO

CCHT MESSAGING DEVICE-WEIGHT

CCHT TELEHEALTH DEVICE(S)	NO

CCHT MESSAGING/MONITORING TYPE/SERIAL #

CCHT TELEHEALTH DEVICE(S)	NO

CCHT MESSAGING/MONITORING-BLOOD GLUCOSE

CCHT TELEHEALTH DEVICE(S)	NO

CCHT MESSAGING/MONITORING-BLOOD PRESSURE

CCHT TELEHEALTH DEVICE(S)	NO

CCHT MESSAGING/MONITORING-OTHER

CCHT TELEHEALTH DEVICE(S)	NO

CCHT MESSAGING/MONITORING-PULSE

|      | CCHT TELEHEALTH DEVICE(S)                                        | NO   |
|------|------------------------------------------------------------------|------|
| CCHT | MESSAGING/MONITORING-PULSE OXIMETRY CCHT TELEHEALTH DEVICE(S)    | NO   |
| CCHT | MESSAGING/MONITORING-SPIROMETRY CCHT TELEHEALTH DEVICE(S)        | NO   |
| CCHT | MESSAGING/MONITORING-WEIGHT CCHT TELEHEALTH DEVICE(S)            | NO   |
| CCHT | MOVE INDOOR HELP/SUPERV LAST 7D-NO CCHT CONTINUUM OF CARE        | NO   |
| CCHT | MOVE INDOOR HELP/SUPERV LAST 7D-YES CCHT CONTINUUM OF CARE       | NO   |
| CCHT | PERIODIC EVALUATION DONE  CCHT ASSESSMENT/TREATMENT PLAN         | NO   |
| CCHT | PERIPHERALS-BP CUFF (SERIAL #) CCHT TELEHEALTH DEVICE(S)         | NO   |
| CCHT | PERIPHERALS-GLUCOSE CABLES CCHT TELEHEALTH DEVICE(S)             | NO   |
| CCHT | PERIPHERALS-NONE NEEDED CCHT TELEHEALTH DEVICE(S)                | NO   |
| CCHT | PERIPHERALS-OTHER  CCHT TELEHEALTH DEVICE(S)                     | NO   |
| CCHT | PERIPHERALS-PULSE OX (SERIAL #) CCHT TELEHEALTH DEVICE(S)        | NO   |
| CCHT | PERIPHERALS-SPIROMETRY (SERIAL #) CCHT TELEHEALTH DEVICE(S)      | NO   |
| CCHT | PERIPHERALS-STETHOSCOPE CCHT TELEHEALTH DEVICE(S)                | NO   |
| CCHT | PERIPHERALS-WEIGHT SCALE (SERIAL #) CCHT TELEHEALTH DEVICE(S)    | NO   |
| CCHT | PHONE-DSL LINE  CCHT TELEHEALTH DEMOGRAPHICS                     | NO   |
| CCHT | PHONE-MODEM  CCHT TELEHEALTH DEMOGRAPHICS                        | NO   |
| CCHT | PHONE-NO FEATURES  CCHT TELEHEALTH DEMOGRAPHICS                  | NO   |
| CCHT | PLAN-MED DISCREP SENT TO PROVIDER CCHT ASSESSMENT/TREATMENT PLAN | NO   |
| CCHT | PLAN-REVIEWED LIST CURRENT MEDS CCHT ASSESSMENT/TREATMENT PLAN   | NO   |
| CCHT | REASON FOR  NON-ENROLLMENT CCHT TELEHEALTH DEMOGRAPHICS          | NO   |
| CCHT | RECENT CHANGE IN FUNCTION-NO                                     |      |

| CCHT CONTINUUM OF CARE	NO  CCHT RECENT CHANGE IN FUNCTION-YES  CCHT CONTINUUM OF CARE	NO  CCHT REFERRAL-CONSULT COMPLETION   |                                                                           |    |
|------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|----|
|                                                                                                                              | CCHT (HOME TELEHEALTH)                                                    | NO |
| CCHT                                                                                                                         | REFERRALS-CAREGIVER NOT  SATISFIED CCHT REFERRALS FOR VETERAN/CAREGIVER   | NO |
| CCHT                                                                                                                         | REFERRALS-CAREGIVER SATISFIED  CCHT REFERRALS FOR VETERAN/CAREGIVER       | NO |
| CCHT                                                                                                                         | STRAINED WITH  RELATIVES=FREQUENTLY CCHT CAREGIVER RISK ASSESSMENT SCREEN | NO |
| CCHT                                                                                                                         | STRAINED WITH RELATIVES=NEVER  CCHT CAREGIVER RISK ASSESSMENT SCREEN      | NO |
| CCHT                                                                                                                         | STRAINED WITH RELATIVES=NRLY ALWAYS CCHT CAREGIVER RISK ASSESSMENT SCREEN | NO |
| CCHT                                                                                                                         | STRAINED WITH RELATIVES=RARELY  CCHT CAREGIVER RISK ASSESSMENT SCREEN     | NO |
| CCHT                                                                                                                         | STRAINED WITH RELATIVES=SOMETIMES  CCHT CAREGIVER RISK ASSESSMENT SCREEN  | NO |
| CCHT                                                                                                                         | STRESSED WORK/FAMILY=FREQUENTLY  CCHT CAREGIVER RISK ASSESSMENT SCREEN    | NO |
| CCHT                                                                                                                         | STRESSED WORK/FAMILY=NEARLY  ALWAYS CCHT CAREGIVER RISK ASSESSMENT SCREEN | NO |
| CCHT                                                                                                                         | STRESSED WORK/FAMILY=NEVER  CCHT CAREGIVER RISK ASSESSMENT SCREEN         | NO |
| CCHT                                                                                                                         | STRESSED WORK/FAMILY=RARELY  CCHT CAREGIVER RISK ASSESSMENT SCREEN        | NO |
| CCHT                                                                                                                         | STRESSED WORK/FAMILY=SOMETIMES  CCHT CAREGIVER RISK ASSESSMENT SCREEN     | NO |
| CCHT                                                                                                                         | TOILET HELP/SUPERVISION LAST 7D-NO CCHT CONTINUUM OF CARE                 | NO |
| CCHT                                                                                                                         | TOILET HELP/SUPERVISION LAST 7D-YES CCHT CONTINUUM OF CARE                | NO |
| CCHT                                                                                                                         | TRANSFERS HELP/SUPERV LAST 7D-NO CCHT CONTINUUM OF CARE                   | NO |
| CCHT                                                                                                                         | TRANSFERS HELP/SUPERV LAST 7D-YES CCHT CONTINUUM OF CARE                  | NO |
| CCHT                                                                                                                         | UNCERTAIN WHAT TO DO=FREQUENTLY  CCHT CAREGIVER RISK ASSESSMENT SCREEN    | NO |
| CCHT                                                                                                                         | UNCERTAIN WHAT TO DO=NEARLY ALWAYS  CCHT CAREGIVER RISK ASSESSMENT SCREEN | NO |
| CCHT                                                                                                                         | UNCERTAIN WHAT TO DO=NEVER                                                |    |

CCHT CAREGIVER RISK ASSESSMENT SCREEN	NO

CCHT UNCERTAIN WHAT TO DO=RARELY

CCHT CAREGIVER RISK ASSESSMENT SCREEN	NO

CCHT UNCERTAIN WHAT TO DO=SOMETIMES

CCHT CAREGIVER RISK ASSESSMENT SCREEN	NO

CCHT VETERAN'S GOAL FOR ENROLLMENT

CCHT (HOME TELEHEALTH)	NO

CCHT VIDEO VISIT-AUDIO/VIDEO CONNECTION

CCHT TELEHEALTH DEVICE(S)	NO

CCHT VIDEOPHONE SERIAL #

CCHT TELEHEALTH DEVICE(S)	NO

CCHT W/C MOBIL HELP/SUPERV LAST 7D-NO

CCHT CONTINUUM OF CARE	NO

CCHT W/C MOBIL HELP/SUPERV LAST 7D-YES

CCHT CONTINUUM OF CARE	NO

CCHT-CAREGIVER REFERRAL BEREAVE SUPPORT

CCHT REFERRALS FOR VETERAN/CAREGIVER	NO

CCHT-CAREGIVER REFERRAL C/G SUPPORT GRP

CCHT REFERRALS FOR VETERAN/CAREGIVER	NO

CCHT-CAREGIVER REFERRAL EDUC/TRAINING

CCHT REFERRALS FOR VETERAN/CAREGIVER	NO

CCHT-CAREGIVER REFERRAL FAMILY COUNSEL

CCHT REFERRALS FOR VETERAN/CAREGIVER	NO

CCHT-CAREGIVER REFERRAL INDIVID COUNSEL

CCHT REFERRALS FOR VETERAN/CAREGIVER	NO

CCHT-CAREGIVER REFERRAL MEDICAL EVAL,F/U

CCHT REFERRALS FOR VETERAN/CAREGIVER	NO

CCHT-CAREGIVER REFERRAL OTHER SERVICE

CCHT REFERRALS FOR VETERAN/CAREGIVER	NO

CCHT-CAREGIVER REFERRAL SVCS IN PLACE

CCHT REFERRALS FOR VETERAN/CAREGIVER	NO

CCHT-CAREGIVER REFERRAL(S) NON VA SYSTEM

CCHT REFERRALS FOR VETERAN/CAREGIVER	NO

CCHT-CAREGIVER REFERRAL(S) VA SYSTEM

CCHT REFERRALS FOR VETERAN/CAREGIVER	NO

CCHT-GETS MEDS VIA NON-VA PROVIDER-NO

CCHT ASSESSMENT/TREATMENT PLAN	NO

CCHT-GETS MEDS VIA NON-VA PROVIDER-YES

CCHT ASSESSMENT/TREATMENT PLAN	NO

CCHT-PT/CG HAS LIST OF ACTIVE MEDS-NO

CCHT ASSESSMENT/TREATMENT PLAN	NO

CCHT-PT/CG HAS LIST OF ACTIVE MEDS-YES

CCHT ASSESSMENT/TREATMENT PLAN	NO

CCHT-PT/CG HAS QUESTIONS ON MEDS-NO

CCHT ASSESSMENT/TREATMENT PLAN	NO

CCHT-PT/CG HAS QUESTIONS ON MEDS-YES

CCHT ASSESSMENT/TREATMENT PLAN	NO

CCHT-PT/CG KNOWS MED INDICATIONS-NO

CCHT ASSESSMENT/TREATMENT PLAN	NO

CCHT-PT/CG KNOWS MED INDICATIONS-YES

CCHT ASSESSMENT/TREATMENT PLAN	NO

CCHT-PT/CG KNOWS MED SIDE EFF-NO

CCHT ASSESSMENT/TREATMENT PLAN	NO

CCHT-PT/CG KNOWS MED SIDE EFFECTS-YES

CCHT ASSESSMENT/TREATMENT PLAN	NO

CCHT-PT/CG KNOWS REFILL PROCESS-NO

CCHT ASSESSMENT/TREATMENT PLAN	NO

CCHT-PT/CG KNOWS REFILL PROCESS-YES

CCHT ASSESSMENT/TREATMENT PLAN	NO

CCHT-PT/CG TAKES MEDS AS PRESCRIBED-NO

CCHT ASSESSMENT/TREATMENT PLAN	NO

CCHT-PT/CG TAKES MEDS AS PRESCRIBED-YES

CCHT ASSESSMENT/TREATMENT PLAN	NO

CCHT-VETERAN REFERRAL ADULT DAY CARE

CCHT REFERRALS FOR VETERAN/CAREGIVER	NO

CCHT-VETERAN REFERRAL EDUC/TRAINING

CCHT REFERRALS FOR VETERAN/CAREGIVER	NO

CCHT-VETERAN REFERRAL EMPLOYMENT ASSIST

CCHT REFERRALS FOR VETERAN/CAREGIVER	NO

CCHT-VETERAN REFERRAL FAMILY COUNSEL

CCHT REFERRALS FOR VETERAN/CAREGIVER	NO

CCHT-VETERAN REFERRAL FINANCIAL ASSIST

CCHT REFERRALS FOR VETERAN/CAREGIVER	NO

CCHT-VETERAN REFERRAL HOME HEALTH SVC

CCHT REFERRALS FOR VETERAN/CAREGIVER	NO

CCHT-VETERAN REFERRAL HOMEMKR/CHORE ASST

CCHT REFERRALS FOR VETERAN/CAREGIVER	NO

CCHT-VETERAN REFERRAL HOSPICE

CCHT REFERRALS FOR VETERAN/CAREGIVER	NO

CCHT-VETERAN REFERRAL HOUSING

CCHT REFERRALS FOR VETERAN/CAREGIVER	NO

CCHT-VETERAN REFERRAL INDIVIDUAL COUNSEL

CCHT REFERRALS FOR VETERAN/CAREGIVER	NO

CCHT-VETERAN REFERRAL LEGAL ASSIST

NO

CCHT-VETERAN REFERRAL(S) VA SYSTEM

CCHT REFERRALS FOR VETERAN/CAREGIVER

CCHT-VETERAN REFERRAL(S) NON VA SYSTEM  CCHT REFERRALS FOR VETERAN/CAREGIVER

CCHT-VETERAN REFERRAL TRANSPORTATION

CCHT-VETERAN REFERRAL SVCS IN PLACE

CCHT-VETERAN REFERRAL SOCIAL WORK

CCHT-VETERAN REFERRAL RESPITE

CCHT-VETERAN REFERRAL OTHER SERVICE

CCHT-VETERAN REFERRAL NURS HOME PLACEMNT CCHT REFERRALS FOR VETERAN/CAREGIVER

CCHT-VETERAN REFERRAL MEDICAL EVAL, F/U CCHT REFERRALS FOR VETERAN/CAREGIVER

CCHT REFERRALS FOR VETERAN/CAREGIVER

#### Appendix D: Contents of the Packed Reminder Export HT Templates/Reminders Set

Exchange File Components	Mar 02, 2017@10:10:04	Page:	1 of	1

Component	Category	Exists- Source:	DOE,JOHN at SALT LAKE CITY

Date Packed: 03/02/2017@10:10:04 Package Version: 2.0P62

Description:

This pack is to support installation of PXRM*2.0*19.	It contains the standardized reminder dialogs and definitions as requested by the

VHA Office of Connected Care(10P8).

The following Clinical Reminder items were selected for packing: REMINDER DIALOG

VA-HT DISCHARGE TEMPLATE VA-HT VIDEO VISIT TEMPLATE

VA-HT TECH EDUCATION &amp; INSTALLATION TEMPLATE VA-HT CONTINUUM OF CARE TEMPLATE

VA-HT SCREENING CONSULT TEMPLATE

VA-HT ASSESSMENT TREATMENT PLAN TEMPLATE VA-HT CAREGIVER ASSESSMENT TEMPLATE

VA-HT INTERVENTION TEMPLATE

VA-HT CAREGIVER/VETERAN REFERRAL VA-HT CAREGIVER RISK ASSESSMENT VA-HT CONTINUUM OF CARE (INITIAL) VA-HT PERIODIC EVALUATION

VA-HT CONTINUUM OF CARE (FOLLOW-UP)

VA-HT TEMPLATE FOR PREVIOUSLY ENROLLED PATIENTS

REMINDER DEFINITION

VA-HT PERIODIC EVALUATION

VA-HT CAREGIVER RISK ASSESSMENT VA-HT CONTINUUM OF CARE (INITIAL)

VA-HT OBJ EMERGENCY PRIORITY RATING LAST VA-HT OBJ EDUCATION TOPICS ALL

VA-HT OBJ CATEGORY OF CARE LAST VA-HT OBJ NIC/CCM RATING LAST

VA-HT OBJ MEDICATION RECONCILIATION VA-HT CONTINUUM OF CARE (FOLLOW-UP) VA-HT OBJ BARRIERS TO LEARNING

VA-HT OBJ CCM RATING LAST

VA-HT OBJ CONTINUUM OF CARE LAST DONE

Non-exchangeable order dialog(s):

Name: PSH OERR

Type: Dialog

Display Text: Non VA Medications

Non-exchangeable TIU object(s):

TIU Object: PATIENT AGE

Object Method: S X=$$AGE^TIULO(DFN)

TIU Object: PATIENT DATE OF DEATH

Object Method: S X=$$DOD^TIULO(DFN)

TIU Object: PAIN

Object Method: S X=$$PAIN^TIULO(+$G(DFN))

TIU Object: PATIENT HEIGHT

Object Method: S X=$$HEIGHT^TIULO(+$G(DFN))

TIU Object: PATIENT WEIGHT

Object Method: S X=$$WEIGHT^TIULO(+$G(DFN))

TIU Object: TEMPERATURE

Object Method: S X=$$TEMP^TIULO(+$G(DFN))

TIU Object: PULSE

Object Method: S X=$$PULSE^TIULO(+$G(DFN))

TIU Object: RESPIRATION

Object Method: S X=$$RESP^TIULO(+$G(DFN))

TIU Object: BLOOD PRESSURE

Object Method: S X=$$BP^TIULO(+$G(DFN))

TIU Object: ACTIVE MEDICATIONS

Object Method: S X=$$LIST^TIULMED(DFN,"^TMP(""TIUMED"",$J)",1)

Keywords:

HOME TELEHEALTH, PXRM*2.0*19,  HT,

VA-HT PROJECT,

Components:

ROUTINE

ORDER

GMRV VITAL TYPE

PAIN	X

MH TESTS AND SURVEYS

ZBI SCREEN	X

TIU TEMPLATE FIELD

1. VA-HT SPECIFY	X
2. VA-HT W-P4LINES(R)	X
3. VA-HT W-P2LINES(R)	X
4. BLANK SPACE1	X
5. OPTIONAL TEXT	X
6. VA-HT EDIT50	X
7. OTHER(REQ-DISP ONLY)	X
8. VA-HT OTHER	X
9. TEXT (1-60 CHARACTERS) REQ	X
10. VA-HT W-P6LINES(R)	X
11. VA-HT W-P6LINES	X
12. VA-HT VITAL SIGNS MODE	X

EDUCATION TOPICS

1. VA-HOME TELEHEALTH-CAREGIVER EDUCATION/SUPPORT	X
2. VA-ALCOHOL ABUSE FOLLOW-UP	X
3. VA-ALCOHOL ABUSE MEDICATIONS	X
4. VA-ALCOHOL ABUSE EXERCISE	X
5. VA-ALCOHOL ABUSE DIET	X
6. VA-ALCOHOL ABUSE LIFESTYLE ADAPTATIONS	X
7. VA-ALCOHOL ABUSE COMPLICATIONS	X
8. VA-ALCOHOL ABUSE DISEASE PROCESS	X
9. VA-SMOKING CESSATION	X
10. VA-IMMUNIZATIONS	X
11. VA-EXERCISE	X
12. VA-NUTRITION/OBESITY	X
13. VA-HTN NUTRITION EDUCATION	X
14. VA-HTN MEDICATION ADHERENCE	X
15. VA-HTN EXERCISE	X
16. VA-DIABETES FOLLOW-UP	X
17. VA-DIABETES MEDICATIONS	X
18. VA-DIABETES FOOT CARE	X
19. VA-DIABETES EXERCISE	X
20. VA-DIABETES DIET	X
21. VA-DIABETES LIFESTYLE ADAPTATIONS	X
22. VA-DIABETES COMPLICATIONS	X
23. VA-DIABETES DISEASE PROCESS	X
24. VA-SAFETY/HOME/FALLS	X
25. VA-ADVANCE DIRECTIVES SCREENING	X
26. VA-ADVANCE DIRECTIVES	X
27. VA-HOME TELEHEALTH-MEDICATION MANAGEMENT	X
28. VA-HOME TELEHEALTH-IN HOME MONITORING	X
29. VA-HOME TELEHEALTH-DISEASE MGMT/PATIENT SELF-MGMT	X HEALTH FACTORS

| 74                                         | HT                                         | CCF                                        | PTSD/OTHER ANXIETY-YES                     | X   | X   |
|--------------------------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|-----|-----|
| 75                                         | HT                                         | CCF                                        | SUBST ABUSE/DEPENDENCE-NO                  | X   | X   |
| 76                                         | HT                                         | CCF                                        | SUBST ABUSE/DEPENDENCE-YES                 | X   | X   |
| 77                                         | HT                                         | CCF                                        | MOOD DISORDER MANIC-NO                     | X   | X   |
| 78                                         | HT                                         | CCF                                        | MOOD DISORDER MANIC-YES                    | X   | X   |
| 79                                         | HT                                         | CCF                                        | MOOD DISORDER DEPRESSION-NO                | X   | X   |
| 80                                         | HT                                         | CCF                                        | MOOD DISORDER DEPRESSION-YES               | X   | X   |
| 81                                         | HT                                         | CCF                                        | DELUSIONS-NO                               | X   | X   |
| 82                                         | HT                                         | CCF                                        | DELUSIONS-YES                              | X   | X   |
| 83                                         | HT                                         | CCF                                        | HALLUCINATIONS-TACTILE                     | X   | X   |
| 84                                         | HT                                         | CCF                                        | HALLUCINATIONS-OLFACTORY                   | X   | X   |
| 85                                         | HT                                         | CCF                                        | HALLUCINATIONS-VISUAL                      | X   | X   |
| 86                                         | HT                                         | CCF                                        | HALLUCINATIONS-AUDITORY                    | X   | X   |
| 87                                         | HT                                         | CCF                                        | HALLUCINATIONS-SENSORY                     | X   | X   |
| 88                                         | HT                                         | CCF                                        | HALLUCINATIONS-NONE                        | X   | X   |
| 89                                         | HT                                         | CCF                                        | POTENTIAL FOR INCR INDEP-NO                | X   | X   |
| 90                                         | HT                                         | CCF                                        | POTENTIAL FOR INCR INDEP-YES               | X   | X   |
| 91                                         | HT                                         | CCF                                        | FLARE UP CHRONIC CONDITION-NO              | X   | X   |
| 92                                         | HT                                         | CCF                                        | FLARE UP CHRONIC CONDITION-YES             | X   | X   |
| 93	HT RECENT CHANGE IN FUNCTION-NO         | 93	HT RECENT CHANGE IN FUNCTION-NO         | 93	HT RECENT CHANGE IN FUNCTION-NO         | 93	HT RECENT CHANGE IN FUNCTION-NO         |     | X   |
| 94	HT RECENT CHANGE IN FUNCTION-YES        | 94	HT RECENT CHANGE IN FUNCTION-YES        | 94	HT RECENT CHANGE IN FUNCTION-YES        | 94	HT RECENT CHANGE IN FUNCTION-YES        |     | X   |
| 95	HT CCF AGITATED/DISORIENTED-NO          | 95	HT CCF AGITATED/DISORIENTED-NO          | 95	HT CCF AGITATED/DISORIENTED-NO          | 95	HT CCF AGITATED/DISORIENTED-NO          |     | X   |
| 96	HT CCF AGITATED/DISORIENTED-YES         | 96	HT CCF AGITATED/DISORIENTED-YES         | 96	HT CCF AGITATED/DISORIENTED-YES         | 96	HT CCF AGITATED/DISORIENTED-YES         |     | X   |
| 97	HT CCF DIFFIC MAKE SELF UNDERSTOOD-NO   | 97	HT CCF DIFFIC MAKE SELF UNDERSTOOD-NO   | 97	HT CCF DIFFIC MAKE SELF UNDERSTOOD-NO   | 97	HT CCF DIFFIC MAKE SELF UNDERSTOOD-NO   |     | X   |
| 98	HT CCF DIFFIC MAKE SELF UNDERSTOOD-YES  | 98	HT CCF DIFFIC MAKE SELF UNDERSTOOD-YES  | 98	HT CCF DIFFIC MAKE SELF UNDERSTOOD-YES  | 98	HT CCF DIFFIC MAKE SELF UNDERSTOOD-YES  |     | X   |
| 99	HT CCF DIFFIC REASONABLE DECISIONS-NO   | 99	HT CCF DIFFIC REASONABLE DECISIONS-NO   | 99	HT CCF DIFFIC REASONABLE DECISIONS-NO   | 99	HT CCF DIFFIC REASONABLE DECISIONS-NO   |     | X   |
| 100	HT CCF DIFFIC REASONABLE DECISIONS-YES | 100	HT CCF DIFFIC REASONABLE DECISIONS-YES | 100	HT CCF DIFFIC REASONABLE DECISIONS-YES | 100	HT CCF DIFFIC REASONABLE DECISIONS-YES |     | X   |
| 101	HT CCF UNPAID CAREGIVER-NO             | 101	HT CCF UNPAID CAREGIVER-NO             | 101	HT CCF UNPAID CAREGIVER-NO             | 101	HT CCF UNPAID CAREGIVER-NO             |     | X   |
| 102	HT CCF CAREGIVER CAN'T INCREASE HELP   | 102	HT CCF CAREGIVER CAN'T INCREASE HELP   | 102	HT CCF CAREGIVER CAN'T INCREASE HELP   | 102	HT CCF CAREGIVER CAN'T INCREASE HELP   |     | X   |
| 103	HT CCF CAREGIVER CAN INCREASE HELP     | 103	HT CCF CAREGIVER CAN INCREASE HELP     | 103	HT CCF CAREGIVER CAN INCREASE HELP     | 103	HT CCF CAREGIVER CAN INCREASE HELP     |     | X   |
| 104	HT CCF CAREGIVER NOT ACCESSIBLE        | 104	HT CCF CAREGIVER NOT ACCESSIBLE        | 104	HT CCF CAREGIVER NOT ACCESSIBLE        | 104	HT CCF CAREGIVER NOT ACCESSIBLE        |     | X   |
| 105	HT CCF CAREGIVER ACCESSIBLE            | 105	HT CCF CAREGIVER ACCESSIBLE            | 105	HT CCF CAREGIVER ACCESSIBLE            | 105	HT CCF CAREGIVER ACCESSIBLE            |     | X   |
| 106	HT CCF CAREGIVER-IADL HELP             | 106	HT CCF CAREGIVER-IADL HELP             | 106	HT CCF CAREGIVER-IADL HELP             | 106	HT CCF CAREGIVER-IADL HELP             |     | X   |
| 107	HT CCF CAREGIVER-ADL HELP              | 107	HT CCF CAREGIVER-ADL HELP              | 107	HT CCF CAREGIVER-ADL HELP              | 107	HT CCF CAREGIVER-ADL HELP              |     | X   |
| 108	HT CCF CAREGIVER-EMOTIONAL SUPPORT     | 108	HT CCF CAREGIVER-EMOTIONAL SUPPORT     | 108	HT CCF CAREGIVER-EMOTIONAL SUPPORT     | 108	HT CCF CAREGIVER-EMOTIONAL SUPPORT     |     | X   |
| 109	HT CCF CAREGIVER-OTHER                 | 109	HT CCF CAREGIVER-OTHER                 | 109	HT CCF CAREGIVER-OTHER                 | 109	HT CCF CAREGIVER-OTHER                 |     | X   |
| 110	HT CCF CAREGIVER-FRIEND/NEIGHBOR       | 110	HT CCF CAREGIVER-FRIEND/NEIGHBOR       | 110	HT CCF CAREGIVER-FRIEND/NEIGHBOR       | 110	HT CCF CAREGIVER-FRIEND/NEIGHBOR       |     | X   |
| 111	HT CCF CAREGIVER-CHILD                 | 111	HT CCF CAREGIVER-CHILD                 | 111	HT CCF CAREGIVER-CHILD                 | 111	HT CCF CAREGIVER-CHILD                 |     | X   |
| 112	HT CCF CAREGIVER-SPOUSE                | 112	HT CCF CAREGIVER-SPOUSE                | 112	HT CCF CAREGIVER-SPOUSE                | 112	HT CCF CAREGIVER-SPOUSE                |     | X   |
| 113	HT CCF CAREGIVER'S PHONE               | 113	HT CCF CAREGIVER'S PHONE               | 113	HT CCF CAREGIVER'S PHONE               | 113	HT CCF CAREGIVER'S PHONE               |     | X   |
| 114	HT CCF CAREGIVER'S ZIP CODE            | 114	HT CCF CAREGIVER'S ZIP CODE            | 114	HT CCF CAREGIVER'S ZIP CODE            | 114	HT CCF CAREGIVER'S ZIP CODE            |     | X   |
| 115	HT CCF CAREGIVER'S STATE               | 115	HT CCF CAREGIVER'S STATE               | 115	HT CCF CAREGIVER'S STATE               | 115	HT CCF CAREGIVER'S STATE               |     | X   |
| 116	HT CCF CAREGIVER'S CITY                | 116	HT CCF CAREGIVER'S CITY                | 116	HT CCF CAREGIVER'S CITY                | 116	HT CCF CAREGIVER'S CITY                |     | X   |
| 117	HT CCF CAREGIVER'S STREET ADDRESS      | 117	HT CCF CAREGIVER'S STREET ADDRESS      | 117	HT CCF CAREGIVER'S STREET ADDRESS      | 117	HT CCF CAREGIVER'S STREET ADDRESS      |     | X   |
| 118	HT CCF CAREGIVER'S NAME                | 118	HT CCF CAREGIVER'S NAME                | 118	HT CCF CAREGIVER'S NAME                | 118	HT CCF CAREGIVER'S NAME                |     | X   |
| 119	HT CCF CAREGIVER LIVES WITH PT-NO      | 119	HT CCF CAREGIVER LIVES WITH PT-NO      | 119	HT CCF CAREGIVER LIVES WITH PT-NO      | 119	HT CCF CAREGIVER LIVES WITH PT-NO      |     | X   |
| 120	HT CCF CAREGIVER LIVES WITH PT-YES     | 120	HT CCF CAREGIVER LIVES WITH PT-YES     | 120	HT CCF CAREGIVER LIVES WITH PT-YES     | 120	HT CCF CAREGIVER LIVES WITH PT-YES     |     | X   |
| 121	HT CCF UNPAID CAREGIVER-YES            | 121	HT CCF UNPAID CAREGIVER-YES            | 121	HT CCF UNPAID CAREGIVER-YES            | 121	HT CCF UNPAID CAREGIVER-YES            |     | X   |
| 122	HT CCF LIVES HOMELESS SHELTER          | 122	HT CCF LIVES HOMELESS SHELTER          | 122	HT CCF LIVES HOMELESS SHELTER          | 122	HT CCF LIVES HOMELESS SHELTER          |     | X   |
| 123	HT CCF LIVES HOMELESS                  | 123	HT CCF LIVES HOMELESS                  | 123	HT CCF LIVES HOMELESS                  | 123	HT CCF LIVES HOMELESS                  |     | X   |
| 124	HT CCF LIVES AT OTHER                  | 124	HT CCF LIVES AT OTHER                  | 124	HT CCF LIVES AT OTHER                  | 124	HT CCF LIVES AT OTHER                  |     | X   |
| 125	HT CCF LIVES DOMICILIARY               | 125	HT CCF LIVES DOMICILIARY               | 125	HT CCF LIVES DOMICILIARY               | 125	HT CCF LIVES DOMICILIARY               |     | X   |
| 126	HT CCF LIVES NURSING HOME              | 126	HT CCF LIVES NURSING HOME              | 126	HT CCF LIVES NURSING HOME              | 126	HT CCF LIVES NURSING HOME              |     | X   |
| 127	HT CCF LIVES BOARD AND CARE            | 127	HT CCF LIVES BOARD AND CARE            | 127	HT CCF LIVES BOARD AND CARE            | 127	HT CCF LIVES BOARD AND CARE            |     | X   |
| 128	HT CCF LIVES PRIVATE HOME              | 128	HT CCF LIVES PRIVATE HOME              | 128	HT CCF LIVES PRIVATE HOME              | 128	HT CCF LIVES PRIVATE HOME              |     | X   |
| 129	HT CCF LIVES WITH OTHER                | 129	HT CCF LIVES WITH OTHER                | 129	HT CCF LIVES WITH OTHER                | 129	HT CCF LIVES WITH OTHER                |     | X   |
| 130	HT CCF GROUP SETTING NON RELATIVES     | 130	HT CCF GROUP SETTING NON RELATIVES     | 130	HT CCF GROUP SETTING NON RELATIVES     | 130	HT CCF GROUP SETTING NON RELATIVES     |     | X   |
| 131	HT CCF LIVES WITH ADULT CHILD          | 131	HT CCF LIVES WITH ADULT CHILD          | 131	HT CCF LIVES WITH ADULT CHILD          | 131	HT CCF LIVES WITH ADULT CHILD          |     | X   |
| 132	HT CCF LIVES WITH CHILD                | 132	HT CCF LIVES WITH CHILD                | 132	HT CCF LIVES WITH CHILD                | 132	HT CCF LIVES WITH CHILD                |     | X   |
| 133	HT CCF LIVES WITH SPOUSE & OTHERS      | 133	HT CCF LIVES WITH SPOUSE & OTHERS      | 133	HT CCF LIVES WITH SPOUSE & OTHERS      | 133	HT CCF LIVES WITH SPOUSE & OTHERS      |     | X   |
| 134	HT CCF LIVES WITH SPOUSE ONLY          | 134	HT CCF LIVES WITH SPOUSE ONLY          | 134	HT CCF LIVES WITH SPOUSE ONLY          | 134	HT CCF LIVES WITH SPOUSE ONLY          |     | X   |
| 135	HT CCF LIVES ALONE                     | 135	HT CCF LIVES ALONE                     | 135	HT CCF LIVES ALONE                     | 135	HT CCF LIVES ALONE                     |     | X   |
| 136	GEC REFERRAL IADL                      | 136	GEC REFERRAL IADL                      | 136	GEC REFERRAL IADL                      | 136	GEC REFERRAL IADL                      | X   | X   |

|   137 | GEC   | RECENT CHANGE IN IADL FX-YES         |    | X   |
|-------|-------|--------------------------------------|----|-----|
|   138 | GEC   | RECENT CHANGE IN IADL FX-NO          |    | X   |
|   139 | GEC   | MEALS PREPARED BY OTHERS/LAST 7D-YES |    | X   |
|   140 | GEC   | MEALS PREPARED BY OTHERS/LAST 7D-NO  |    | X   |
|   141 | GEC   | DIFFICULTY WITH SHOPPING/LAST 7D-YES |    | X   |
|   142 | GEC   | DIFFICULTY WITH SHOPPING/LAST 7D-NO  |    | X   |
|   143 | GEC   | DIFFICULTY W/ HOUSEWORK/LAST 7D-YES  |    | X   |
|   144 | GEC   | DIFFICULTY W/ HOUSEWORK/LAST 7D-NO   |    | X   |
|   145 | GEC   | DIFFICULTY USING PHONE/LAST 7D-YES   |    | X   |
|   146 | GEC   | DIFFICULTY USING PHONE/LAST 7D-NO    |    | X   |
|   147 | GEC   | DIFFICULTY PREPARE MEALS/LAST 7D-YES |    | X   |
|   148 | GEC   | DIFFICULTY PREPARE MEALS/LAST 7D-NO  |    | X   |
|   149 | GEC   | DIFFICULTY MNG FINANCES/LAST 7D-YES  |    | X   |
|   150 | GEC   | DIFFICULTY MNG FINANCES/LAST 7D-NO   |    | X   |
|   151 | GEC   | DIFFICULTY MANAGING MEDS/LAST 7D-YES |    | X   |
|   152 | GEC   | DIFFICULTY MANAGING MEDS/LAST 7D-NO  |    | X   |
|   153 | GEC   | DIFFICULT TRANSPORTATION/LAST 7D-YES |    | X   |
|   154 | GEC   | DIFFICULT TRANSPORTATION/LAST 7D-NO  |    | X   |
|   155 | HT    | DIFFICULT PREPARE MEALS/LAST 7D-NO   |    | X   |
|   156 | HT    | DIFFICULT PREPARE MEALS/LAST 7D-YES  |    | X   |
|   157 | HT    | MEALS PREPARED BY OTHER/LAST 7D-YES  |    | X   |
|   158 | HT    | MEALS PREPARED BY OTHER/LAST 7D-NO   |    | X   |
|   159 | HT    | DIFFICULT W/ HOUSEWORK/LAST 7D-YES   |    | X   |
|   160 | HT    | DIFFICULT W/ HOUSEWORK/LAST 7D-NO    |    | X   |
|   161 | HT    | DIFFICULT WITH SHOPPING/LAST 7D-YES  |    | X   |
|   162 | HT    | DIFFICULT WITH SHOPPING/LAST 7D-NO   |    | X   |
|   163 | HT    | DIFFICULT TRANSPORTATION/LAST 7D-YES |    | X   |
|   164 | HT    | DIFFICULT TRANSPORTATION/LAST 7D-NO  |    | X   |
|   165 | HT    | DIFFICULT USING PHONE LAST 7D-YES    |    | X   |
|   166 | HT    | DIFFICULT USING PHONE LAST 7D-NO     |    | X   |
|   167 | HT    | DIFFICULT MANAGING MEDS/LAST 7D-YES  |    | X   |
|   168 | HT    | DIFFICULT MANAGING MEDS/LAST 7D-NO   |    | X   |
|   169 | HT    | DIFFICULT MNG FINANCES/LAST 7D-YES   |    | X   |
|   170 | HT    | DIFFICULT MNG FINANCES/LAST 7D-NO    |    | X   |
|   171 | GEC   | REFERRAL BASIC ADL                   | X  | X   |
|   172 | GEC   | TRANSFERS HELP/SPRVISION LAST 7D-YES |    | X   |
|   173 | GEC   | TRANSFERS HELP/SPRVISION LAST 7D-NO  |    | X   |
|   174 | GEC   | TOILET HELP/SUPERVISION LAST 7D-YES  |    | X   |
|   175 | GEC   | TOILET HELP/SUPERVISION LAST 7D-NO   |    | X   |
|   176 | GEC   | BATHING HELP/SUPERVISION LAST 7D-NO  |    | X   |
|   177 | GEC   | RECENT CHANGE IN ADL FX-YES          |    | X   |
|   178 | GEC   | RECENT CHANGE IN ADL FX-NO           |    | X   |
|   179 | GEC   | MOVING AROUND INDOORS LAST 7D-YES    |    | X   |
|   180 | GEC   | MOVING AROUND INDOORS LAST 7D-NO     |    | X   |
|   181 | GEC   | INDEPENDENT IN WC LAST 7D-YES        |    | X   |
|   182 | GEC   | INDEPENDENT IN WC LAST 7D-NO         |    | X   |
|   183 | GEC   | EATING HELP/SUPERVISION LAST 7D-YES  |    | X   |
|   184 | GEC   | EATING HELP/SUPERVISION LAST 7D-NO   |    | X   |
|   185 | GEC   | DRESS HELP/SUPERVISION LAST 7D-YES   |    | X   |
|   186 | GEC   | DRESS HELP/SUPERVISION LAST 7D-NO    |    | X   |
|   187 | GEC   | BED POSITIONING HELP LAST 7D-YES     |    | X   |
|   188 | GEC   | BED POSITIONING HELP LAST 7D-NO      |    | X   |
|   189 | GEC   | BATHING PHYS ASST NEEDED LAST 7D-YES |    | X   |
|   190 | GEC   | BATHING PHYS ASST NEEDED LAST 7D-NO  |    | X   |
|   191 | GEC   | BATHING HELP/SUPERVISION LAST 7D-YES |    | X   |
|   192 | HT    | EATING HELP/SUPERVISION LAST 7D-YES  |    | X   |
|   193 | HT    | EATING HELP/SUPERVISION LAST 7D-NO   |    | X   |
|   194 | HT    | TOILET HELP/SUPERVISION LAST 7D-YES  |    | X   |
|   195 | HT    | TOILET HELP/SUPERVISION LAST 7D-NO   |    | X   |
|   196 | HT    | BED MOBIL HELP/SUPERV LAST 7D-YES    |    | X   |
|   197 | HT    | BED MOBIL HELP/SUPERV LAST 7D-NO     |    | X   |
|   198 | HT    | TRANSFERS HELP/SUPERV LAST 7D-YES    |    | X   |
|   199 | HT    | TRANSFERS HELP/SUPERV LAST 7D-NO     |    | X   |

|   200 | HT   | MOVE INDOOR HELP/SUPERV LAST 7D-YES   |    | X   |
|-------|------|---------------------------------------|----|-----|
|   201 | HT   | MOVE INDOOR HELP/SUPERV LAST 7D-NO    |    | X   |
|   202 | HT   | BATHING HELP/SUPRVISION LAST 7D-YES   |    | X   |
|   203 | HT   | BATHING HELP/SUPRVISION LAST 7D-NO    |    | X   |
|   204 | HT   | DRESSING HELP/SUPERV LAST 7D-YES      |    | X   |
|   205 | HT   | DRESSING HELP/SUPERV LAST 7D-NO       |    | X   |
|   206 | HT   | W/C MOBIL HELP/SUPERV LAST 7D-YES     |    | X   |
|   207 | HT   | W/C MOBIL HELP/SUPERV LAST 7D-NO      |    | X   |
|   208 | HT   | CCF FOLLOW-UP ASSESSMENT COMPLETED    |    | X   |
|   209 | HT   | REFERRALS FOR VETERAN/CAREGIVER       | X  | X   |
|   210 | HT   | VETERAN REFERRAL SVCS IN PLACE        |    | X   |
|   211 | HT   | VETERAN REFERRAL(S) NON VA SYSTEM     |    | X   |
|   212 | HT   | VETERAN REFERRAL(S) VA SYSTEM         |    | X   |
|   213 | HT   | VETERAN REFERRAL OTHER SERVICE        |    | X   |
|   214 | HT   | VETERAN REFERRAL EDUC/TRAINING        |    | X   |
|   215 | HT   | CAREGIVER REFERRAL SOCIAL WORK        |    | X   |
|   216 | HT   | CAREGIVER REFERRAL SVCS IN PLACE      |    | X   |
|   217 | HT   | CAREGIVER REFERRAL(S) NON VA SYSTEM   |    | X   |
|   218 | HT   | CAREGIVER REFERRAL(S) VA SYSTEM       |    | X   |
|   219 | HT   | CAREGIVER REFERRAL BEREAVE SUPPORT    |    | X   |
|   220 | HT   | CAREGIVER REFERRAL OTHER SERVICE      |    | X   |
|   221 | HT   | CAREGIVER REFERRAL MEDICAL EVAL,F/U   |    | X   |
|   222 | HT   | CAREGIVER REFERRAL EDUC/TRAINING      |    | X   |
|   223 | HT   | CAREGIVER REFERRAL C/G SUPPORT GRP    |    | X   |
|   224 | HT   | CAREGIVER REFERRAL FAMILY COUNSEL     |    | X   |
|   225 | HT   | CAREGIVER REFERRAL INDIVID COUNSEL    |    | X   |
|   226 | HT   | CG/VETERAN REFERRAL COMPLETED         |    | X   |
|   227 | HT   | CAREGIVER RISK ASSESSMENT SCREEN      | X  | X   |
|   228 | HT   | UNABLE TO SCREEN CAREGIVER            |    | X   |
|   229 | HT   | CAREGIVER ASSESSMENT SCREEN COMPLETED |    | X   |
|   230 | HT   | CG/VETERAN REFERRAL(S) NOT UTILIZED   |    | X   |
|   231 | HT   | REFERRALS-CAREGIVER NOT SATISFIED     |    | X   |
|   232 | HT   | REFERRALS-CAREGIVER SATISFIED         |    | X   |
|   233 | HT   | ASSESSMENT/TREATMENT PLAN             | X  | X   |
|   234 | HT   | CATEGORY OF CARE-OTHER                |    | X   |
|   235 | HT   | CATEGORY OF CARE-HEALTH PROMOTION     |    | X   |
|   236 | HT   | CATEGORY OF CARE-CHRONIC CARE MGMT    |    | X   |
|   237 | HT   | CATEGORY OF CARE-ACUTE CARE           |    | X   |
|   238 | HT   | CATEGORY OF CARE-NON INSTITUTIONAL    |    | X   |
|   239 | HT   | HEALTH EDUCATION PLAN                 | X  | X   |
|   240 | HT   | CONSULTS/REFERRALS RECOMMENDED        |    | X   |
|   241 | HT   | TEACH CAREGIVER/FAMILY/SIGNIF OTHER   |    | X   |
|   242 | HT   | VET/CAREGIVER VIEW VIDEOS/HEALTH TV   |    | X   |
|   243 | HT   | CAREGIVER REVIEW OF WRITTEN MATERIALS |    | X   |
|   244 | HT   | VETERAN REVIEW OF WRITTEN MATERIALS   |    | X   |
|   245 | HT   | REPEAT DEMONSTRATION NEXT VISIT       |    | X   |
|   246 | HT   | NO FOLLOW-UP NEEDED/INDICATED         |    | X   |
|   247 | HT   | HEALTH EDUCATION RESPONSE             | X  | X   |
|   248 | HT   | NO EVIDENCE OF LEARNING               |    | X   |
|   249 | HT   | NEEDS REINFORCEMENT/REVIEW/FOLLOW-UP  |    | X   |
|   250 | HT   | DISINTERESTED/LACKS MOTIVATION        |    | X   |
|   251 | HT   | CAREGIVER STATES ESSENTIAL CONCEPTS   |    | X   |
|   252 | HT   | VETERAN STATES ESSENTIAL CONCEPTS     |    | X   |
|   253 | HT   | EMERG PRIORITY HIGH-IMMEDIATE EVAL    |    | X   |
|   254 | HT   | EMERG PRIORITY MOD-SVCS AFTER 3-7D    |    | X   |
|   255 | HT   | EMERG PRIORITY LOW-HAS RESOURCES      |    | X   |
|   256 | HT   | PLAN-MED DISCREP SENT TO PROVIDER     |    | X   |
|   257 | HT   | PLAN-REVIEWED LIST OF CURRENT MEDS    |    | X   |
|   258 | HT   | PT/CG HAS QUESTIONS ON MEDS-YES       |    | X   |
|   259 | HT   | PT/CG HAS QUESTIONS ON MEDS-NO        |    | X   |
|   260 | HT   | PT/CG HAS LIST OF ACTIVE MEDS-YES     |    | X   |
|   261 | HT   | PT/CG HAS LIST OF ACTIVE MEDS-NO      |    | X   |
|   262 | HT   | GETS MEDS VIA NON-VA PROVIDER-YES     |    | X   |

| 263	HT GETS MEDS VIA NON-VA PROVIDER-NO      |    | X   |
|----------------------------------------------|----|-----|
| 264	HT DISCHARGE                             | X  | X   |
| 265	HT DISCHARGE-HAS MET GOALS               |    | X   |
| 266	HT DISCHARGE-PT/CG REQUEST DC SERVICES   |    | X   |
| 267	HT DISCHARGE-UNABLE TO OPERATE DEVICES   |    | X   |
| 268	HT DISCHARGE-RELOCATED OUT OF SVC AREA   |    | X   |
| 269	HT DISCHARGE-ADMITTED TO NURSING HOME    |    | X   |
| 270	HT DISCHARGE-NO VA PRIMARY CARE SVCS     |    | X   |
| 271	HT DISCHARGE-PHONE,ELECT SVCS UNAVAIL    |    | X   |
| 272	HT DISCHARGE-REFERRED TO HOSPICE         |    | X   |
| 273	HT DISCHARGE-PATIENT IS DECEASED         |    | X   |
| 274	HT DISCHARGE-PROLONGED HOSPITALIZATION   |    | X   |
| 275	HT DISCHARGE-PROVIDER REQUESTS DC        |    | X   |
| 276	HT DISCHARGE-NO RESPONSE TO PROGRAM      |    | X   |
| 277	HT CCF INITIAL ASSESSMENT COMPLETED      |    | X   |
| 278	HT (HOME TELEHEALTH)                     | X  | X   |
| 279	HT ENROLLMENT-START DATE                 |    | X   |
| 280	HT PERIODIC EVALUATION COMPLETED         |    | X   |
| 281	HT ENROLLMENT-START DATE (PREV ENROLL)   |    | X   |
| 282	PREFERRED HEALTHCARE LANGUAGE            | X  | X   |
| 283	PREFERRED HEALTHCARE LANGUAGE-ENGLISH    |    | X   |
| 284	PREFERRED HEALTHCARE LANGUAGE-OTHER      |    | X   |
| 285	PREFERRED HEALTHCARE LANGUAGE-ASL        |    | X   |
| 286	PREFERRED HEALTHCARE LANGUAGE-BRAILLE    |    | X   |
| 287	PREFERRED HEALTHCARE LANGUAGE-PORTUGUESE |    | X   |
| 288	PREFERRED HEALTHCARE LANGUAGE-ITALIAN    |    | X   |
| 289	PREFERRED HEALTHCARE LANGUAGE-RUSSIAN    |    | X   |
| 290	PREFERRED HEALTHCARE LANGUAGE-KOREAN     |    | X   |
| 291	PREFERRED HEALTHCARE LANGUAGE-GERMAN     |    | X   |
| 292	PREFERRED HEALTHCARE LANGUAGE-VIETNAMESE |    | X   |
| 293	PREFERRED HEALTHCARE LANGUAGE-TAGALOG    |    | X   |
| 294	PREFERRED HEALTHCARE LANGUAGE-FRENCH     |    | X   |
| 295	PREFERRED HEALTHCARE LANGUAGE-CHINESE    |    | X   |
| 296	PREFERRED HEALTHCARE LANGUAGE-SPANISH    |    | X   |
| 297	HT BARRIERS TO LEARNING                  | X  | X   |
| 298	HT LEARNING BARRIER-VISUALLY IMPAIRED    |    | X   |
| 299	HT LEARNING BARRIER-UNABLE TO WRITE      |    | X   |
| 300	HT LEARNING BARRIER-UNABLE TO READ       |    | X   |
| 301	HT LEARNING BARRIER-PHYSICAL LIMITATIONS |    | X   |
| 302	HT LEARNING BARRIER-PAIN                 |    | X   |
| 303	HT LEARNING BARRIER-OVERWHELMED          |    | X   |
| 304	HT LEARNING BARRIER-NOT MOTIVATED        |    | X   |
| 305	HT LEARNING BARRIER-HOMELESS             |    | X   |
| 306	HT LEARNING BARRIER-HEARING IMPAIRED     |    | X   |
| 307	HT LEARNING BARRIER-CULTURAL             |    | X   |
| 308	HT LEARNING BARRIER-POOR CONCENTRATION   |    | X   |
| 309	HT LEARNING BARRIER-IMPAIRED MEMORY      |    | X   |
| 310	HT LEARNING BARRIER-APHASIA              |    | X   |
| 311	HT LEARNING BARRIER-COGNITIVE IMPAIRMENT |    | X   |
| 312	HT LEARNING BARRIER-ANXIETY              |    | X   |
| 313	HT LEARNING BARRIER-ANGRY                |    | X   |
| 314	HT LEARNING BARRIER-NONE IDENTIFIED      |    | X   |
| 315	HT VETERAN'S GOAL FOR ENROLLMENT         |    | X   |
| 316	HT CLINICAL REASON FOR ENROLLMENT        |    | X   |
| 317	HT TELEHEALTH DEMOGRAPHICS               | X  | X   |
| 318	HT MEETS TELEHEALTH CRITERIA(YES)        |    | X   |
| 319	HT REASON FOR NON-ENROLLMENT             |    | X   |
| 320	HT MEETS TELEHEALTH CRITERIA(NO)         |    | X   |
| 321	HT INDICATIONS-HX HOSPITALIZATONS        |    | X   |
| 322	HT INDICATIONS-DISTANCE (HOURS)          |    | X   |
| 323	HT INDICATIONS-DISTANCE (MILES)          |    | X   |
| 324	HT INDICATIONS-# OUTPT VISITS PAST YR    |    | X   |
| 325	HT INDICATIONS-HX HIGH COST/HIGH USE     |    | X   |

|   326 | HT   | DISEASE                              | INDICATIONS-OTHER                    | X   | X   |
|-------|------|--------------------------------------|--------------------------------------|-----|-----|
|   327 | HT   | DISEASE                              | INDICATIONS-SUBSTANCE ABUSE          | X   | X   |
|   328 | HT   | DISEASE                              | INDICATIONS-PTSD                     | X   | X   |
|   329 | HT   | DISEASE                              | INDICATIONS-DEPRESSION               | X   | X   |
|   330 | HT   | DISEASE                              | INDICATIONS-OBESITY                  | X   | X   |
|   331 | HT   | DISEASE                              | INDICATIONS-DIABETES                 | X   | X   |
|   332 | HT   | DISEASE                              | INDICATIONS-HYPERTENSION             | X   | X   |
|   333 | HT   | DISEASE                              | INDICATIONS-COPD                     | X   | X   |
|   334 | HT   | DISEASE                              | INDICATIONS-HEART FAILURE            | X   | X   |
|   335 | HT   | VET NOT                              | INTERESTED TELEHEALTH PROGRAM        | X   | X   |
|   336 | HT   | REFERRAL-CONSULT COMPLETION          | REFERRAL-CONSULT COMPLETION          |     | X   |
|   337 | HT   | TELEHEALTH DELIVERY/INSTALL MODE     | TELEHEALTH DELIVERY/INSTALL MODE     | X   | X   |
|   338 | HT   | EQUIP INSTALLED BY OTHER             | EQUIP INSTALLED BY OTHER             |     | X   |
|   339 | HT   | EQUIP INSTALLED BY VETERAN/CAREGIVER | EQUIP INSTALLED BY VETERAN/CAREGIVER |     | X   |
|   340 | HT   | EQUIP INSTALLED BY SUPPORT STAFF     | EQUIP INSTALLED BY SUPPORT STAFF     |     | X   |
|   341 | HT   | DISCHARGE-OTHER FOLLOW-UP            | DISCHARGE-OTHER FOLLOW-UP            |     | X   |
|   342 | HT   | DISCHARGE-REFERRED TO MENTAL HEALTH  | DISCHARGE-REFERRED TO MENTAL HEALTH  |     | X   |
|   343 | HT   | DISCHARGE-REFERRED TO SOCIAL WORK    | DISCHARGE-REFERRED TO SOCIAL WORK    |     | X   |
|   344 | HT   | DISCHARGE-REFERRED TO NEW LOCATION   | DISCHARGE-REFERRED TO NEW LOCATION   |     | X   |
|   345 | HT   | DISCHARGE-REFERRED TO PRIMARY CARE   | DISCHARGE-REFERRED TO PRIMARY CARE   |     | X   |
|   346 | HT   | DISCHARGE-ALL ISSUES ADDRESSED(NO)   | DISCHARGE-ALL ISSUES ADDRESSED(NO)   |     | X   |
|   347 | HT   | DISCHARGE-ALL ISSUES ADDRESSED(YES)  | DISCHARGE-ALL ISSUES ADDRESSED(YES)  |     | X   |
|   348 | HT   | ENROLLMENT-ENDING DATE               | ENROLLMENT-ENDING DATE               |     | X   |
|   349 | HT   | LEARNING BARRIER-LANGUAGE            | LEARNING BARRIER-LANGUAGE            |     | X   |

REMINDER SPONSOR

1. VHA Office of Connected Care (10P8)	X

REMINDER COMPUTED FINDINGS

VA-AGE	X

VA-FILEMAN DATE	X

REMINDER TAXONOMY

1. VA-HT ENCOUNTER PHONE 21	X
2. VA-HT ENCOUNTER PHONE 11	X
3. VA-HT ENCOUNTER PHONE 5	X

REMINDER TERM

|   354 | VA-HT   | BL NIC/CCM CRITERIA                     | X   |
|-------|---------|-----------------------------------------|-----|
|   355 | VA-HT   | CCM (CHRONIC CARE MGMT) CRITERIA        | X   |
|   356 | VA-HT   | SUPPRESS FOR AGE <75                    | X   |
|   357 | VA-HT   | BL GEC IADLS                            | X   |
|   358 | VA-HT   | BL HT IADLS                             | X   |
|   359 | VA-HT   | BL GEC BASIC ADLS                       | X   |
|   360 | VA-HT   | BL HT BASIC ADLS                        | X   |
|   361 | VA-HT   | CATEGORY OF CARE                        | X   |
|   362 | VA-HT   | EMERGENCY PRIORITY RATINGS              | X   |
|   363 | VA-HT   | PT/CAREGIVER QUESTIONS ON MEDICATIONS   | X   |
|   364 | VA-HT   | PT/CAREGIVER LIST OF ACTIVE MEDICATIONS | X   |
|   365 | VA-HT   | MEDICATIONS VIA NON-PROVIDER            | X   |
|   366 | VA-HT   | DISCHARGE REASONS                       | X   |
|   367 | VA-HT   | CCF FOLLOW-UP ASSESSMENT COMPLETED      | X   |
|   368 | VA-HT   | CCF INITIAL ASSESSMENT COMPLETED        | X   |
|   369 | VA-HT   | CCF DOES NOT MEET CCM CRITERIA          | X   |
|   370 | VA-HT   | CCF MEETS CHRONIC CARE MGMT CRITERIA    | X   |
|   371 | VA-HT   | CCF DOES NOT MEET NIC CRITERIA          | X   |
|   372 | VA-HT   | CCF MEETS NIC CRITERIA                  | X   |
|   373 | VA-HT   | ENROLLMENT-START DATE                   | X   |
|   374 | VA-HT   | PERIODIC EVALUATION COMPLETED           | X   |
|   375 | VA-HT   | CAREGIVER RISK ASSESSMENT DONE          | X   |
|   376 | VA-HT   | UNABLE TO SCREEN CAREGIVER              | X   |
|   377 | VA-HT   | CCF UNPAID CAREGIVER-YES                | X   |
|   378 | VA-HT   | ENROLLMENT-START DATE (PREV ENROLL)     | X   |

1. VA-HT CAREGIVER RELATIONSHIP	X
2. VA-HT CONTINUUM OF CARE LAST	X

REMINDER DEFINITION

1. VA-HT OBJ NIC/CCM RATING LAST	X
2. VA-HT OBJ CATEGORY OF CARE LAST	X
3. VA-HT OBJ EMERGENCY PRIORITY RATING LAST	X
4. VA-HT OBJ MEDICATION RECONCILIATION	X
5. VA-HT CONTINUUM OF CARE (FOLLOW-UP)	X
6. VA-HT PERIODIC EVALUATION	X
7. VA-HT CAREGIVER RISK ASSESSMENT	X
8. VA-HT CONTINUUM OF CARE (INITIAL)	X
9. VA-HT OBJ CAREGIVER NAME/RELATIONSHIP	X
10. VA-HT OBJ CONTINUUM OF CARE LAST DONE	X
11. VA-HT OBJ CCM RATING LAST	X
12. VA-HT OBJ BARRIERS TO LEARNING	X
13. VA-HT OBJ EDUCATION TOPICS ALL	X

REMINDER DIALOG

1. VA-HT CONTINUUM OF CARE (FOLLOW-UP)	X
2. VA-HT PERIODIC EVALUATION	X
3. VA-HT CONTINUUM OF CARE (INITIAL)	X
4. VA-HT CAREGIVER RISK ASSESSMENT	X
5. VA-HT CAREGIVER/VETERAN REFERRAL	X
6. VA-HT INTERVENTION TEMPLATE	X
7. VA-HT TEMPLATE FOR PREVIOUSLY ENROLLED PATIENTS	X
8. VA-HT CAREGIVER ASSESSMENT TEMPLATE	X
9. VA-HT ASSESSMENT TREATMENT PLAN TEMPLATE	X
10. VA-HT SCREENING CONSULT TEMPLATE	X
11. VA-HT CONTINUUM OF CARE TEMPLATE	X
12. VA-HT TECH EDUCATION &amp; INSTALLATION TEMPLATE	X
13. VA-HT VIDEO VISIT TEMPLATE	X
14. VA-HT DISCHARGE TEMPLATE	X

HEALTH SUMMARY COMPONENT

CLINICAL REMINDERS FINDINGS	X

PCE HEALTH FACTORS SELECTED	X

CLINICAL REMINDERS DUE	X

NEXT OF KIN	X

MAS ADMISSIONS/DISCHARGES	X

MAS CLINIC VISITS PAST	X

HEALTH SUMMARY TYPE

1. VA-HT NIC/CCM RATING LAST	X
2. VA-GEC IADLS	X
3. VA-HT IADLS	X
4. VA-GEC BASIC ADLS	X
5. VA-HT BASIC ADLS	X
6. VA-HT CATEGORY OF CARE LAST	X
7. VA-HT EMERGENCY LEVEL LAST	X
8. VA-HT MED RECON	X
9. VA-HT REMINDERS DUE	X
10. VA-HT ENROLLMENT START	X
11. VA-HT CAREGIVER	X
12. VA-NEXT OF KIN	X
13. VA-ADMISSIONS PAST YR	X
14. VA-OUTPT APPTS PAST YR	X

HEALTH SUMMARY OBJECTS

1. VA-HT NIC/CCM RATING LAST(TIU)	X
2. VA-GEC IADLS(TIU)	X
3. VA-HT IADLS(TIU)	X
4. VA-GEC BASIC ADLS(TIU)	X

1. VA-HT BASIC ADLS(TIU)	X
2. VA-HT CATEGORY OF CARE(TIU)	X
3. VA-HT EMERGENCY LEVELS(TIU)	X
4. VA-HT MED RECON(TIU)	X
5. VA-HT REMINDERS DUE(TIU)	X
6. VA-HT ENROLLMENT START DATE(TIU)	X
7. VA-HT CAREGIVER(TIU)	X
8. VA-NEXT OF KIN(TIU)	X
9. VA-ADMISSIONS PAST YR(TIU)	X
10. VA-OUTPT APPTS PAST YR(TIU)	X

TIU DOCUMENT DEFINITION

| 436	HT NIC/CCM RATING LAST       | 436	HT NIC/CCM RATING LAST                   | X   |
|----------------------------------|----------------------------------------------|-----|
| PATIENT AGE                      | PATIENT AGE                                  | X   |
| 437	GEC IADLS (LAST)             | 437	GEC IADLS (LAST)                         | X   |
| 438	HT IADLS LAST                | 438	HT IADLS LAST                            | X   |
| 439	GEC BASIC ADLS (LAST)        | 439	GEC BASIC ADLS (LAST)                    | X   |
| 440	HT BASIC ADLS LAST           | 440	HT BASIC ADLS LAST                       | X   |
| 441	HT CATEGORY OF CARE          | 441	HT CATEGORY OF CARE                      | X   |
| 442	HT EMERGENCY PRIORITY RATING | 442	HT EMERGENCY PRIORITY RATING             | X   |
| 443	HT MED RECON                 | 443	HT MED RECON                             | X   |
| ACTIVE MEDICATIONS               | ACTIVE MEDICATIONS                           | X   |
| 444	HT REMINDERS DUE             | 444	HT REMINDERS DUE                         | X   |
| 445	HT ENROLLMENT START DATE     | 445	HT ENROLLMENT START DATE                 | X   |
| 446	HT CAREGIVER                 | 446	HT CAREGIVER                             | X   |
| 447	NEXT OF KIN                  | 447	NEXT OF KIN                              | X   |
| BLOOD PRESSURE                   | BLOOD PRESSURE                               | X   |
| PAIN                             | PAIN                                         | X   |
| PATIENT WEIGHT                   | PATIENT WEIGHT                               | X   |
| PATIENT HEIGHT                   | PATIENT HEIGHT                               | X   |
| RESPIRATION                      | RESPIRATION                                  | X   |
| PULSE                            | PULSE                                        | X   |
| TEMPERATURE                      | TEMPERATURE                                  | X   |
| 448	ADMISSIONS PAST YR           | 448	ADMISSIONS PAST YR                       | X   |
| 449                              | OUTPT APPTS PAST YR	X  PATIENT DATE OF DEATH |     |

**Appendix E: Clinic Crosswalk**

| **Current Clinic Location**                                                      | **Prim. Stop Code**   |   **Sec. Stop Code** | **Note Titles**               | **Templates**                  | **Definition**                                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------|-----------------------|----------------------|-------------------------------|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **HT SCREENING OFC**                                                             | Prog. Dep Clinic Code |                  371 | HT  Screening Consult         | HT  Screening Consult Template | This consult document is used to document initial evaluation for enrollment WHETHER OR NOT the patient is actually enrolled.  **NOTE:**  Use to close consult                                                                                                                                                                                                       |
| **HT SCREENING TC**  **or**  **HT SCREENING PHONE**  **or**  **HT SCREENING PH** | Prog. Dep Phone Code  |                      |                               |                                |                                                                                                                                                                                                                                                                                                                                                                     |
| **HT TECH EDUCATION**                                                            | 674                   |                  685 | HT Tech Education Note        | HT Tech Education Template     | This document contains patient education, skill validation and installation for technology on all HT patients.  NOTE: ALWAYS attached to the coding pair 674/685 (Non- Count)  Use as often as needed when re-educating the patient on technology, changing or troubleshooting technology or adding new peripheral devices. Training/Education on  technology only. |
| **HT INTERVENTION**                                                              | Prog. Dep Phone Code  |                  684 | **HT**  **Intervention Note** | HT  Intervention Template      | This progress note contains information about all interventions generated from symptoms, behavior and knowledge data gathered from daily monitoring by a non-video messaging device.  **NOTE:**  Use  **ONLY**  to document patient encounters in response to alerts from vendor data- not  to be used as generic note, and not to be used with VIDEO visit.        |

| **HT MONTHLY MONITOR**                                                                          | 683                   |   Prog. Dep.  **Blank for HBPC** | **HT Monthly Monitor Note**                                                                                                                                                        | HT Monthly Monitor Template            | This progress note contains information about the monthly monitoring of patients assigned non-video messaging devices.  **NOTE:**  Document using this note title once each calendar month on  EVERY  messaging patient regardless of other patient interactions during the month. Not to be used for patients on video technology  that does not have messaging functionality.   |
|-------------------------------------------------------------------------------------------------|-----------------------|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **HT VIDEO VISIT**                                                                              | Prog Dep              |                              179 | HT Video Visit Note                                                                                                                                                                | HT Video Visit Template                | This document contains information about any visit over a video device (tele-Monitor/ Videophone) that meets required criteria for secondary Stop Code xxx179  **NOTE:**  Must meet certain documentation requirements of  replicating a face-to-face visit or it can’t be coded as 179                                                                                           |
| **HT ASSESS TX**  **PLAN HM**                                                                   | Prog and Location Dep |                              685 | HT  Assessment Treatment Plan                                                                                                                                                      | HT  Assessment Treatment Plan Template | This document contains information about the visit with the patient/caregiver which includes the clinical assessment and the HT Plan of Care. Additional signature is requested by the Primary Care Provider (and others, including program staff, as appropriate).Additional time needs to be allocated in DSS upon setup for this Clinic Location                               |
| **HT ASSESS TX PLAN TC**  **or**  **HT ASSESS TX PLAN PHONE**  **or**  **HT ASSESS TX PLAN PH** |                       |                                  |                                                                                                                                                                                    |                                        |                                                                                                                                                                                                                                                                                                                                                                                   |
| **HT ASSESS TX PLAN OF**  **or**  **HT ASSESS TX PLAN OFC**                                     |                       |                                  |                                                                                                                                                                                    |                                        |                                                                                                                                                                                                                                                                                                                                                                                   |
| **HT VISIT TC**  **or**  **HT VISIT PHONE**  **or**  **HT VISIT PH**                            | Prog. Dep Phone Code  |                              685 | **FIRST, select the HT Clinic Location (left) where the visit is taking place:**  1. **By telephone (TC, Phone, PH)** 2. **In the office (OFC)** 3. **At the patient's home (HM)** |                                        |                                                                                                                                                                                                                                                                                                                                                                                   |
| **HT VISIT OFC**                                                                                | Prog. Dep Clinic Code |                              685 |                                                                                                                                                                                    |                                        |                                                                                                                                                                                                                                                                                                                                                                                   |
| **HT VISIT HM**                                                                                 | 118 or HBPC  code     |                              685 |                                                                                                                                                                                    |                                        |                                                                                                                                                                                                                                                                                                                                                                                   |

| **SECOND**  **, select a Note Title/Template (right) to pair with the clinic location (above)**   | HT  Discharge Note          | HT  Discharge Template            | This Document contains closure of the patients’ case and discharge from the HT program. Basically, this note is a discharge summary.  NOTE: Designed to facilitate closing the case of a HT patient. May have an encounter attached to it if the discharge is done by telephone or office visit. Will not have an encounter if patient is not  present.   |
|---------------------------------------------------------------------------------------------------|-----------------------------|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                   | HT Note                     | N/A                               | Generic Note title to encompass all other HT activities. Select documentation templates from  the template drawer.                                                                                                                                                                                                                                        |
|                                                                                                   | HT Periodic Evaluation Note | HT Periodic Evaluation Template   | Periodic review and upgrade of the plan of care  NOTE: Summarization of care for a period of time. Interval dependent on VISN/Program.                                                                                                                                                                                                                    |
|                                                                                                   | HT  Continuum of Care Note  | HT  Continuum of Care Template    | Note title to be used with the Continuum of Care clinical reminder dialog  NOTE: Initial CCF will be included in the Assessment  Treatment Plan template. This note title to be used thereafter.                                                                                                                                                          |
|                                                                                                   | HT  Caregiver Assessment    | HT  Caregiver Assessment Template | NOTE: Will combine both the High-risk Screen &amp; referral for assistance in one note title and  template.                                                                                                                                                                                                                                               |

#### Appendix F: Installation Example

###### Re-Install

Select Installation &lt;TEST ACCOUNT&gt; Option: 2	Verify Checksums in Transport Global

Select INSTALL NAME: HT TEMPLATES PROJECT 1.0	3/6/17@10:42:25

=&gt; HT TEMPLATES 1.0	;Created on Mar 06, 2017@08:31:06

This Distribution was loaded on Mar 06, 2017@10:42:25 with header of HT TEMPLATES 1.0	;Created on Mar 06, 2017@08:31:06

It consisted of the following Install(s):

HT TEMPLATES PROJECT 1.0	TIU*1.0*258	PXRM*2.0*19	GMTS*2.7*98

Want each Routine Listed with Checksums: Yes//	YES DEVICE: HOME//	HOME

PACKAGE: HT TEMPLATES PROJECT 1.0	Mar 06, 2017 10:42 am	PAGE 1

0 Routine checked, 0 failed.

PACKAGE: TIU*1.0*258	Mar 06, 2017 10:42 am	PAGE 1

TIUP258	Calculated	103966494

TIUP258E	Calculated	39956358

2 Routines checked, 0 failed.

PACKAGE: PXRM*2.0*19	Mar 06, 2017 10:42 am	PAGE 1

| PXRMCCHT   | Calculated   |   24334245 |
|------------|--------------|------------|
| PXRMHTED   | Calculated   |    4905599 |
| PXRMP19A   | Calculated   |   50240117 |
| PXRMP19B   | Calculated   |  106974297 |
| PXRMP19E   | Calculated   |    1345736 |
| PXRMP19I   | Calculated   |   48601801 |

6 Routines checked, 0 failed.

PACKAGE: GMTS*2.7*98	Mar 06, 2017 10:42 am	PAGE 1

GMTSP98E	Calculated	5307666

GMTSPI98	Calculated	14297806

2 Routines checked, 0 failed.

1. Load a Distribution
2. Verify Checksums in Transport Global
3. Print Transport Global
4. Compare Transport Global to Current System
5. Backup a Transport Global
6. Install Package(s)

Restart Install of Package(s) Unload a Distribution

Select Installation &lt;TEST ACCOUNT&gt; Option: 6	Install Package(s) Select INSTALL NAME: HT TEMPLATES PROJECT 1.0		3/6/17@10:42:25

=&gt; HT TEMPLATES 1.0	;Created on Mar 06, 2017@08:31:06

This Distribution was loaded on Mar 06, 2017@10:42:25 with header of HT TEMPLATES 1.0	;Created on Mar 06, 2017@08:31:06

It consisted of the following Install(s):

HT TEMPLATES PROJECT 1.0	TIU*1.0*258	PXRM*2.0*19	GMTS*2.7*98

Checking Install for Package HT TEMPLATES PROJECT 1.0 Install Questions for HT TEMPLATES PROJECT 1.0

Checking Install for Package TIU*1.0*258

Will first run the Environment Check Routine, TIUP258E Verifying installation environment...

Checking for existing document classes...

Document class found: CARE COORDINATION HOME TELEHEALTH NOTES Document class check complete.

Now checking for any local titles that may conflict with new national titles. Local title check complete. No conflicts found.

Environment check complete. Install will proceed.

Install Questions for TIU*1.0*258

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// Checking Install for Package PXRM*2.0*19

Install Questions for PXRM*2.0*19 Incoming Files:

811.8	REMINDER EXCHANGE	(including data) Note:	You already have the 'REMINDER EXCHANGE' File. I will OVERWRITE your data with mine.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// Checking Install for Package GMTS*2.7*98

Will first run the Environment Check Routine, GMTSP98E Verifying installation environment...

Verification complete; environment check passed Install Questions for GMTS*2.7*98

Incoming Files:

811.8	REMINDER EXCHANGE	(including data) Note:	You already have the 'REMINDER EXCHANGE' File. I will OVERWRITE your data with mine.

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

DEVICE: HOME// ;;999	HOME

Install Started for HT TEMPLATES PROJECT 1.0 :

Mar 06, 2017@10:44:28

Build Distribution Date: Mar 06, 2017 Installing Routines:

Mar 06, 2017@10:44:28

Install Started for TIU*1.0*258 :

Mar 06, 2017@10:44:28

Build Distribution Date: Mar 06, 2017 Installing Routines:

Mar 06, 2017@10:44:28

Running Pre-Install Routine:  PRE^TIUP258 Preparing HT Document Class &amp; Titles for Update...

Inactivating CARE COORDINATION HOME TELEHEALTH NOTES.

Renaming document class CARE COORDINATION HOME TELEHEALTH NOTES as HOME TELEHEALTH NOTES.

Inactivating HT SCREENING CONSULT. Inactivating HT INTERVENTION NOTE. Inactivating HT SUMMARY OF EPISODE NOTE. Inactivating HT DISCHARGE NOTE. Inactivating HT VIDEO VISIT NOTE.

Inactivating HT ASSESSMENT TREATMENT PLAN NOTE. Inactivating HT CAREGIVER ASSESSMENT NOTE.

Inactivating HT CONTINUUM OF CARE NOTE. Inactivating CCHT NOTE.

Inactivating HT PERIODIC EVALUATION NOTE.

Inactivating HT TECH EDUCATION NOTE. Inactivating HT TELEPHONE CASE MANAGEMENT NOTE.

Renaming CCHT NOTE as HT NOTE.

Installing PACKAGE COMPONENTS:

Installing PRINT TEMPLATE Installing SORT TEMPLATE Installing OPTION

Mar 06, 2017@10:44:29

Running Post-Install Routine: POST^TIUP258 HT SCREENING CONSULT successfully installed HT INTERVENTION NOTE successfully installed

HT SUMMARY OF EPISODE NOTE successfully installed HT DISCHARGE NOTE successfully installed

HT VIDEO VISIT NOTE successfully installed

HT ASSESSMENT TREATMENT PLAN NOTE successfully installed HT CAREGIVER ASSESSMENT NOTE successfully installed

HT CONTINUUM OF CARE NOTE successfully installed HT NOTE successfully installed

HT PERIODIC EVALUATION NOTE successfully installed HT TECH EDUCATION NOTE successfully installed

HT TELEPHONE CASE MANAGEMENT NOTE successfully installed Attempting to map HT titles to VHA Enterprise Standard Titles...

Reindexing TIU Titles......

Updating Routine file...

The following Routines were created during this install: TIUCTP

TIUCTM

Updating KIDS files...

TIU*1.0*258 Installed.

Mar 06, 2017@10:44:30

Not a production  UCI NO Install Message sent

Install Started for PXRM*2.0*19 :

Mar 06, 2017@10:44:30

Build Distribution Date: Mar 06, 2017 Installing Routines:

Mar 06, 2017@10:44:30

Running Pre-Install Routine: PRE^PXRMP19I DISABLE options.

DISABLE protocols.

Attempting to rename CCHT Health Factors... Installing Data Dictionaries:

Mar 06, 2017@10:44:32

Installing Data:

Mar 06, 2017@10:44:33

Installing PACKAGE COMPONENTS:

Installing OPTION

Mar 06, 2017@10:44:33

Running Post-Install Routine: POST^PXRMP19I ENABLE options.

ENABLE protocols.

Preparing to install Reminder Exchange entry VA-HT PROJECT. This is a very large entry that installs numerous components. Installation of this entry will take 10-15 minutes.

There are 3 Reminder Exchange entries to be installed.

1. Installing Reminder Exchange entry TIU TEMPLATE URL FIX
2. Installing Reminder Exchange entry VA-HT EDUCATION TOPICS
3. Installing Reminder Exchange entry VA-HT PROJECT

The post-install will generate a single MailMan message: LOCAL CCHT HFs NOT USED IN NAT'L HT CLIN REMINDER CONTENT

The installer is strongly encouraged to include the site's local Clinical Reminders support/configuration personnel/mail group as recipients.

Send mail to: THOMPSON,WILLIAM//	THOMPSON,WILLIAM

Select basket to send to: IN// And Send to:

Queueing post-install message... DONE - Task #1781082

Checking ORWPCE EXCLUDE HEALTH FACTORS at the SYSTEM level for each HT Health Factor Category

Parameter set for HT (HOME TELEHEALTH) Parameter set for HT CONTINUUM OF CARE (CCF)

Checking TIU TEMPLATE REMINDER DIALOGS at the SYSTEM level

Setting Data Fields for TIU-HS Objects Setting Data Fields Complete

Updating Routine file... Updating KIDS files...

PXRM*2.0*19 Installed.

Mar 06, 2017@10:55:50

Not a production  UCI NO Install Message sent

Install Started for GMTS*2.7*98 :

Mar 06, 2017@10:55:50

Build Distribution Date: Mar 06, 2017 Installing Routines:

Mar 06, 2017@10:55:50

Running Pre-Install Routine: PRE^GMTSPI98 Installing Data Dictionaries:

Mar 06, 2017@10:55:50

Installing Data:

Mar 06, 2017@10:55:50

Running Post-Install Routine: POST^GMTSPI98

1. Installing Reminder Exchange entry VA-HT REMOTE HEALTH SUMMARY TYPES Updating Routine file...

Updating KIDS files...

GMTS*2.7*98 Installed.

Mar 06, 2017@10:55:51

Not a production  UCI NO Install Message sent

Updating Routine file... Updating KIDS files...

HT TEMPLATES PROJECT 1.0 Installed.

Mar 06, 2017@10:55:51

No link to PACKAGE file

GMTS*2.7*98

Install Completed

#### Appendix G: FileMan Searches for HT Pilot Sites

**OVERVIEW**

This information is for reference/use by Clinical Application Coordinator(s) (CACs) at sites that participated in the CCHT Templates Project pilot program. The nationally released version of these templates (HT Templates Project 1.0: TIU*1*258, PXRM*2.0*19, GMTS*2.7*98) will install a complete template set. Some files will have entries left over from the pilot program that should be manually cleaned up and/or inactivated. How to handle this cleanup is a local decision.

The following FileMan search examples can be used at such facilities to identify unused items from the pilot program. Oftentimes, CACs either no longer have FileMan access or do not have access to all the files listed below. In these scenarios, CACs should work with either local or Region-based IT staff to assist with running these searches.

***************************************************************************** Do not use FileMan to perform edits/renaming of the following file entries. Edits should be done via the proper package options and in the case of GUI templates and/or GUI template fields, the CPRS GUI Template Editor.

*****************************************************************************

**REMINDER TERM**

Search for terms that have “CCHT” or “CARE COORD” in the name. Terms with a CLASS of national cannot be locally edited but any term with a CLASS of VISN or LOCAL can be edited by the site. This search will likely find terms that should not be modified. Use caution when making decisions about which terms to edit.

Select VA FileMan &lt;TEST ACCOUNT&gt; Option: Search File Entries OUTPUT FROM WHAT FILE: BUILD// REMINDER TERM	(1009 entries)

-A- SEARCH FOR REMINDER TERM FIELD: ?

Answer with FIELD NUMBER, or LABEL

|   Choose | from:   |                               |
|----------|---------|-------------------------------|
|     0.01 |         | NAME                          |
|     0.04 |         | DATE CREATED                  |
|     1    |         | DESCRIPTION	(word-processing) |
|    20    |         | FINDINGS	(multiple)           |
|   100    |         | CLASS                         |
|   101    |         | SPONSOR                       |
|   102    |         | REVIEW DATE                   |
|   110    |         | EDIT HISTORY	(multiple)       |

-A- SEARCH FOR REMINDER TERM FIELD: .01	NAME

-A- CONDITION: CONTAINS

-A- CONTAINS: CCHT

-B- SEARCH FOR REMINDER TERM FIELD: NAME

-B- CONDITION: CONTAINS

-B- CONTAINS: CARE COORD

A	NAME CONTAINS (case-insensitive) "CCHT"

B

Or

NAME

CONTAINS

(case-insensitive)

"CARE

COORD"

-C- SEARCH FOR REMINDER TERM FIELD: IF:

OR:

| OR:                                                                                                                                                                                                |     |        |       |          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|--------|-------|----------|
| STORE RESULTS OF SEARCH IN TEMPLATE:                                                                                                                                                               |     |        |       |          |
| SORT BY: NAME//  START WITH NAME: FIRST// FIRST PRINT FIELD: NAME THEN PRINT FIELD: CLASS THEN PRINT FIELD:  Heading (S/C): REMINDER TERM SEARCH	Replace DEVICE: ;;9999	HOME  REMINDER TERM SEARCH | MAY | 9,2013 | 07:48 | PAGE 1   |
| NAME                                                                                                                                                                                               |     |        |       | CLASS    |
| VA-GEC CARE COORDINATION COMMENTS                                                                                                                                                                  |     |        |       | NATIONAL |
| CCHT DISCHARGE REASONS                                                                                                                                                                             |     |        |       | VISN     |
| CCHT SUPPRESS FOR AGE <75                                                                                                                                                                          |     |        |       | VISN     |
| 3 MATCHES FOUND.                                                                                                                                                                                   |     |        |       |          |

**REMINDER DEFINITION**

Search for definitions that have “CCHT” or “CARE COORD” in the name. Definitions with a CLASS of national cannot be locally edited but any definition with a CLASS of VISN or LOCAL can be edited by the site. This search will likely find definitions that should not be modified. Use caution when making decisions about which definitions to edit.

Select Fileman (VA) &lt;TEST ACCOUNT&gt; Option:	Search File Entries OUTPUT FROM WHAT FILE: REMINDER DEFINITION//

-A- SEARCH FOR REMINDER DEFINITION FIELD: NAME

-A- CONDITION: CONTAINS

-A- CONTAINS: CARE COOR

-B- SEARCH FOR REMINDER DEFINITION FIELD: NAME

-B- CONDITION: CONTAINS

-B- CONTAINS: CCHT

-C- SEARCH FOR REMINDER DEFINITION FIELD:

IF: A	NAME CONTAINS (case-insensitive) "CARE COOR" OR: B		Or NAME CONTAINS (case-insensitive) "CCHT" OR:

STORE RESULTS OF SEARCH IN TEMPLATE:

SORT BY: NAME//

START WITH NAME: FIRST// FIRST PRINT FIELD: NAME THEN PRINT FIELD: CLASS THEN PRINT FIELD:

Heading (S/C): REMINDER DEFINITION SEARCH	Replace DEVICE:	HOME

REMINDER DEFINITION SEARCH	MAY	9,2013	08:12		PAGE 1 NAME				CLASS

VA-GEC REFERRAL CARE COORDINATION	NATIONAL

CCHT NIC CONTINUUM OF CARE	LOCAL

CCHT PERIODIC EVALUATION	VISN

CCHT PERIODIC EVALUATION (VER2)	VISN

4 MATCHES FOUND.

**REMINDER DIALOG**

Due to the numerous dialog components, site may find it more convenient to use the Reminder Dialog Management menu to locate any LOCAL or VISN reminder dialogs and associated components. This can be done using the Search List feature of dialog management.

Select Reminder Dialog Management &lt;TEST ACCOUNT&gt; Option: **DI	Reminder Dialogs**

**Dialog List** May 09, 2013@10:17:12	Page:	1 of	51 REMINDER VIEW (ALL REMINDERS BY NAME)

Item Reminder Name	Linked Dialog Name &amp; Dialog Status

1. AL LUNG LESION	AL LUNG LESION DIALOG
2. AL RPT HEMOGLOBIN A1C &gt;9 OR MISSIN
3. ALBANY DB PT W/LDL &gt; 99
4. AVJ DDK HOME OX BAKUP	HOME OXYGEN RENEWAL
5. AVJ HOME OXYGEN RENEWAL	HOME OXYGEN RENEWAL
6. Alcohol Screen(PRL)	V2 ALCOHOL SCREEN NEW
7. BASELINE MEDICAL EVALUATION/V23
8. BATH ACOVE FALL HISTORY	BATH ACOVE FALL HISTORY DIA
9. BATH ACOVE FUNCTIONAL STATUS REMIN BATH ACOVE KATZ DIALOG
10. BATH ACOVE POSITIVE FALL REMINDER	BATH ACOVE POSITIVE FALL HI
11. BATH ACOVE POSITIVE URINARY INCONT BATH ACOVE POSITIVE URINARY
12. BATH ACOVE URINARY INCONTINENCE	BATH ACOVE URINARY INCONTIN
13. BATH ALLERGY REMINDER	BATH ALLERGY REVIEW DIALOG
14. BATH BRADEN SCALE FOLLOWUP	VA-VANOD SKIN REASSESSMENT
15. BATH BRADEN SCALE INITIAL	VA-VANOD SKIN INITIAL ASSES
16. BATH BRADEN SCALE INITIAL SCREEN

+	Enter ?? for more actions	&gt;&gt;&gt;

AR	All reminders	LR	Linked Reminders	QU	Quit CV	Change View	RN	Name/Print Name

Select Item: Next Screen// **CV	Change View**

Select one of the following:

1. Reminder Dialogs
2. Dialog Elements
3. Forced Values
4. Dialog Groups

P	Additional Prompts

R	Reminders

RG	Result Group (Mental Health)

RE	Result Element (Mental Health) TYPE OF VIEW: R// **D		Reminder Dialogs**

Select Item: Next Screen// SL	SL Search for: CCHT // CCHT

**Dialog List** May 09, 2013@10:19:58	Page:	4 of	26 DIALOG VIEW (REMINDER DIALOGS - SOURCE REMINDER NAME)

+Item Reminder Dialog Name	Source Reminder	Status

1. **CCHT (3 DATA OBJECTS ONLY)	*NONE***
2. CCHT CONTINUUM OF CARE	CCHT NIC CONTINUUM OF CAR Linked

1. CHF DIALOG	ZZV2 CHF MANAGEMENT	Linked
2. CHF EJECTION FRACTION PROVIDER DIALOG	V2 EJECTION FRACTION MISS Linked
3. CHF MEDICAL MANAGEMENT	V2 CHF MEDICAL MANAGEMENT Linked
4. CHF NOT ON ACEI NOR BETA BLOCKER	ZZTEST CHF NOT ON ACEI NO Linked
5. CHF ON ACEI AND BETA BLOCKER	ZZTEST CHF ON ACEI AND BE Linked
6. CHF ON ACEI AND NOT BETA BLOCKER	ZZTEST CHF ON ACEI BUT NO Linked
7. CHF ON BETA BLOCKER NOT ON ACEI	ZZTEST CHF NOT ON ACEI ON Linked
8. CHF WEIGHT EDUCATION DIALOG	V2 CHF WEIGHT EDUCATION
9. CHF WEIGHT EDUCATION DIALOG 2-27-06	V2 CHF WEIGHT EDUCATION	Linked
10. CMS SUICIDE ASSESSMENT MH TOOL	COL-MH SUICIDE RISK ASSES
11. CN HOME O2 CERTIFICATION DIALOG	*NONE*
12. CN PAIN PLAN DIALOG	CN PAIN PLAN REMINDER	Linked
13. CN PAIN SCREEN DIALOG	*NONE*
14. COLON CA SCREEN DIALOG (2)	V2 COLON CANCER SCREEN	Linked

+	+ Next Screen	- Prev Screen	?? More Actions	&gt;&gt;&gt;

...searching for 'CCHT' Find Next 'CCHT'? Yes//

As unused reminder dialogs are found, these entries can be edited. Entries could have the DISABLED field set, or names could be changed to begin with “ZZ”, which is often used to indicate an unused file entry. How a given site chooses to handle the items that are no longer used (disable, ZZ, etc.) is a local decision.

Following the example searches above for Reminder Terms and Reminder Definitions, these files can also be searched for CCHT items. Each FileMan file name is listed with the FileMan file number in parentheses. Under each file is the FileMan Field Name(s) with the corresponding FileMan Field Number(s).

**HEALTH SUMMARY TYPE (#142)**

FileMan search of Health Summary Type, looking for:

NAMEs (.01) that contain “CCHT”, or “CARE COORD” Or, TITLEs (.02) that contain “CCHT”, or “CARE COORD”

**HEALTH SUMMARY OBJECT (#142.5)**

FileMan search of Health Summary Object, looking for:

NAMEs (.01) that contain “CCHT”, “CARE COORD”

**TIU DOCUMENT DEFINITIO** N **(#8925.1)**

FileMan search of TIU Document Definition, looking for:

NAMEs (.01) that contain “CCHT” or “CARE COORD”

Or, ABBREVIATIONs (.02) that contain “CCHT” or “CARE COORD”

Or PRINT NAMEs (.03) that contain “CCHT” or “CARE COORD”

**TIU TEMPLATE (#8927)**

FileMan search of TIU Template, looking for NAMEs (.01) that contain “CCHT”, “CARE COORD” , or use the CPRS GUI Template Editor to find relevant template fields. Any edits must be done via the GUI Template Editor.

**TIU TEMPLATE FIELD (#8927.1)**

FileMan search of TIU Template Field, looking for NAMEs (.01) that contain “CCHT”, “CARE COORD”, or use the CPRS GUI Template Editor to find relevant template fields. Any edits must be done via the GUI Template Editor.

**Pilot Program Reminder Exchange Reference**

Below is the listing of the reminder exchange file used as part of Phase 3 of the CCHT Pilot Program. This information can be used as a guide to help identify items that may no longer be needed after installation of the HT Templates bundle. For example, this listing could be compared with the reminder exchange files distributed with the HT Templates 1.0 software bundle in order to help determine the file entries that may no longer be necessary/in use. The reminder exchange files in HT Templates 1.0 are:

VA-HT EDUCATION TOPICS VA-HT PROJECT

VA-HT REMOTE HEALTH SUMMARY TYPES

Exchange File Components	May 23, 2010@11:34

Component	Category	Exists- Source:

Date Packed: 05/23/2010@11:30:47 Package Version: 2.0P12 Description:

*************	BEFORE STARTING THIS INSTALL:	******************

- Read the CCHT Templates Pilot CAC Installation Guide
- Build the (3) health summary types - configuration below

********************************************************************

The following Clinical Reminder items were selected for packing:

REMINDER DIALOG

CCHT DISCHARGE TEMPLATE CCHT VIDEO VISIT TEMPLATE

CCHT TECH EDUCATION TEMPLATE CCHT CONTINUUM OF CARE TEMPLATE CCHT SCREENING CONSULT TEMPLATE

CCHT PERIODIC EVALUATION TEMPLATE

CCHT ASSESSMENT TREATMENT PLAN TEMPLATE CCHT CAREGIVER ASSESSMENT TEMPLATE

CCHT TEMPLATE FOR PREVIOUSLY ENROLLED PATIENTS CCHT INTERVENTION TEMPLATE

CCHT (3 DATA OBJECTS ONLY)

REMINDER DEFINITION

CCHT BL SCREENING CONSULT CCHT BL TECH EDUCATION CCHT PERIODIC EVALUATION

CCHT CONTINUUM OF CARE (FOLLOW-UP) CCHT CONTINUUM OF CARE (INITIAL) CCHT CAREGIVER/VETERAN REFERRAL CCHT CAREGIVER RISK ASSESSMENT

********************************************************************

**DEPRESSION REMINDER STATUS Health Summary type:**

**For the HEALTH SUMMARY TYPE "DEPR REMINDER STATUS", you will need to ADD your site's SELECTION ITEM for your DEPRESSION SCREEN clinical reminder. Use this for the configuration:**

Create/Modify Health Summary Type

Select Health Summary Type: DEPR REMINDER STATUS (OBJ) TITLE: Depression reminder status

SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes// SUPPRESS SENSITIVE PRINT DATA: NO SSN//

LOCK:

Select component: REMINDERS DUE

SUMMARY ORDER: 5// 5

HEADER NAME: Reminders Due//

Select SELECTION ITEM: VI-20 DEPR

Searching for a CLINICAL REMINDER/MAINTENANCE VI-20 DEPRESSION SCREENING (v09.1.1)	VISN

...OK? Yes// (Yes) Select SELECTION ITEM: &lt;ENT&gt; Select COMPONENT: &lt;ENT&gt;

**HEMOGLOBIN A1C LAST	Health Summary type:**

**Use your site's in-house lab test(s) for the selection item for the LAB TEST SELECTED health summary component. If your site uses Health Factors to document OUTSIDE A1c values, add those into the configuration:**

NAME: A1C LAST (OBJ)	OWNER: MINER,MAURI N SUPPRESS COMP WITHOUT DATA: yes

SUMMARY ORDER: 5	COMPONENT NAME: LAB TESTS SELECTED

OCCURRENCE LIMIT: 1	HEADER NAME: Lab Tests Selected SELECTION ITEM: HEMOGLOBIN A1c

SUMMARY ORDER: 10	COMPONENT NAME: SELECTED HEALTH FACTORS

OCCURRENCE LIMIT: 1

SELECTION ITEM: OUTSIDE A1C LESS THAN 7.0 SELECTION ITEM: OUTSIDE A1C BETWEEN 7.0-9.0 SELECTION ITEM: OUTSIDE A1C BETWEEN 9.1-11.0 SELECTION ITEM: OUTSIDE A1C GREATER THAN 11.0

SUPPRESS SENSITIVE PRINT DATA: NO SSN

TITLE: Hemoglobin A1c last

**PULSE OXIMETRY OUTPT LAST Health Summary type:**

NAME: PULSE OX OUTPT LAST(OBJ)	OWNER: MINER,MAURI N SUPPRESS COMP WITHOUT DATA: yes

SUMMARY ORDER: 5

COMPONENT NAME: VITAL SIGNS SELECTED OUTPAT.

OCCURRENCE LIMIT: 1	HEADER NAME: Vital Select Outpat.

SELECTION ITEM: PULSE  OXIMETRY SUPPRESS SENSITIVE PRINT DATA: NO SSN

TITLE: Pulse Oximetry Outpt-last

******************************************************************** Non-exchangeable order dialog(s):

Name: PSH OERR

Type: Dialog

Display Text: Non VA Medications

Name: GMRCT SOCIAL WORK (SEA)

Type: Quick  Order Display Text: Social Work consult

Display Group: CONSULTS

Package: CONSULT/REQUEST TRACKING

Consult to Service/Specialty: SOC WRK-MEDICINE OUTPT (PCCS)

Reason for Request: CCHT patient referred for Social Work co ...

Category: OUTPATIENT Urgency: ROUTINE

Place of Consultation: Consultant's Choice

Non-exchangeable TIU object(s):

TIU Object: PATIENT AGE

Object Method: S X=$$AGE^TIULO(DFN)

TIU Object: PATIENT DATE OF DEATH

Object Method: S X=$$DOD^TIULO(DFN)

TIU Object: ALLERGIES/ADR

Object Method: S X=$$MAIN^ARJADR(DFN,0,"^TMP(""TIULADR"",$J)",0)

TIU Object: PATIENT HEIGHT

Object Method: S X=$$HEIGHT^TIULO(+$G(DFN))

TIU Object: PATIENT WEIGHT

Object Method: S X=$$WEIGHT^TIULO(+$G(DFN))

TIU Object: TEMPERATURE

Object Method: S X=$$TEMP^TIULO(+$G(DFN))

TIU Object: PULSE

Object Method: S X=$$PULSE^TIULO(+$G(DFN))

TIU Object: RESPIRATION

Object Method: S X=$$RESP^TIULO(+$G(DFN))

TIU Object: BLOOD PRESSURE

Object Method: S X=$$BP^TIULO(+$G(DFN))

TIU Object: ACTIVE MEDICATIONS

Object Method: S X=$$LIST^TIULMED(DFN,"^TMP(""TIUMED"",$J)",1)

TIU Object: PAIN

Object Method: S X=$$PAIN^TIULO(+$G(DFN))

Keywords:

Components:

ROUTINE

1 PXRMPDEM	X

LABORATORY TEST

HEMOGLOBIN A1c	X

ORDER DIALOG

GMRCT SOCIAL WORK (SEA)	X

PSH OERR	X

GMRV VITAL TYPE

PULSE OXIMETRY	X

PAIN	X

| MH   | TESTS AND SURVEYS  PHQ9   |                                         | X   |
|------|---------------------------|-----------------------------------------|-----|
|      | PHQ-2                     | PHQ-2                                   | X   |
| TIU  |                           | TEMPLATE FIELD                          |     |
| 2    | 2                         | CCHT W-P4LINES(R)                       | X   |
| 3    | 3                         | CCHT W-P2LINES(R)                       | X   |
| 4    | 4                         | CCHT CHANGE TO PROVIDER-CG/VET          | X   |
| 5    | 5                         | CCHT EDIT50                             | X   |
| 6    | 6                         | CCHT CHANGE TO PROVIDER-CG/VET EMBEDDED | X   |
| 7    | 7                         | CCHT SPECIFY                            | X   |
| 8    | 8                         | CCHT OTHER                              | X   |
| 9    | 9                         | CCHT NEW/USED                           | X   |
| 10   | 10                        | CCHT BL PRESSURE CUFF SIZE              | X   |
| 11   | 11                        | CCHT W-P6LINES(R)                       | X   |
| 12   | 12                        | CCHT W-P6LINES                          | X   |
| 13   | 13                        | CCHT VITAL SIGNS MODE                   | X   |

EDUCATION TOPICS

1. HOME TELEHEALTH-CAREGIVER EDUCATION/SUPPORT	X
2. HOME TELEHEALTH-MEDICATION MANAGEMENT	X
3. HOME TELEHEALTH-DISEASE MGMT/PATIENT SELF-MGMT	X
4. HOME TELEHEALTH-IN HOME MONITORING	X

HEALTH FACTORS

|   18 | CCHT   | TEMPLATE USE (PHASE 3)              | TEMPLATE USE (PHASE 3)              | TEMPLATE USE (PHASE 3)              | TEMPLATE USE (PHASE 3)              | TEMPLATE USE (PHASE 3)              | X   | X   |
|------|--------|-------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|-----|-----|
|   19 | CCHT   | INTERVENTION TEMPLATE USED          | INTERVENTION TEMPLATE USED          | INTERVENTION TEMPLATE USED          | INTERVENTION TEMPLATE USED          | INTERVENTION TEMPLATE USED          |     | X   |
|   20 | CCHT   | CONTINUUM OF CARE                   | CONTINUUM OF CARE                   | CONTINUUM OF CARE                   | CONTINUUM OF CARE                   | CONTINUUM OF CARE                   | X   | X   |
|   21 | CCHT   | CCF MEETS CCM CRITERIA              | CCF MEETS CCM CRITERIA              | CCF MEETS CCM CRITERIA              | CCF MEETS CCM CRITERIA              | CCF MEETS CCM CRITERIA              |     | X   |
|   22 | CCHT   | CCF FOLLOW-UP ASSESSMENT DONE       | CCF FOLLOW-UP ASSESSMENT DONE       | CCF FOLLOW-UP ASSESSMENT DONE       | CCF FOLLOW-UP ASSESSMENT DONE       | CCF FOLLOW-UP ASSESSMENT DONE       |     | X   |
|   23 | CCHT   | CCF MEETS NIC CRITERIA              | CCF MEETS NIC CRITERIA              | CCF MEETS NIC CRITERIA              | CCF MEETS NIC CRITERIA              | CCF MEETS NIC CRITERIA              |     | X   |
|   24 | CCHT   | ASSESSMENT/TREATMENT PLAN           | ASSESSMENT/TREATMENT PLAN           | ASSESSMENT/TREATMENT PLAN           | ASSESSMENT/TREATMENT PLAN           | ASSESSMENT/TREATMENT PLAN           | X   | X   |
|   25 | CCHT   | PERIODIC EVALUATION DONE            | PERIODIC EVALUATION DONE            | PERIODIC EVALUATION DONE            | PERIODIC EVALUATION DONE            | PERIODIC EVALUATION DONE            |     | X   |
|   26 | CCHT   | (CARE COORDINATION HOME TELEHEALTH) | (CARE COORDINATION HOME TELEHEALTH) | (CARE COORDINATION HOME TELEHEALTH) | (CARE COORDINATION HOME TELEHEALTH) | (CARE COORDINATION HOME TELEHEALTH) | X   | X   |
|   27 | CCHT   | ENROLLMENT-START DATE (PREV ENROLL) | ENROLLMENT-START DATE (PREV ENROLL) | ENROLLMENT-START DATE (PREV ENROLL) | ENROLLMENT-START DATE (PREV ENROLL) | ENROLLMENT-START DATE (PREV ENROLL) |     | X   |
|   28 | CCHT   | ENROLLMENT-START DATE               | ENROLLMENT-START DATE               | ENROLLMENT-START DATE               | ENROLLMENT-START DATE               | ENROLLMENT-START DATE               |     | X   |
|   29 | CCHT   | PREVIOUSLY ENROLLED TEMPLATE USED   | PREVIOUSLY ENROLLED TEMPLATE USED   | PREVIOUSLY ENROLLED TEMPLATE USED   | PREVIOUSLY ENROLLED TEMPLATE USED   | PREVIOUSLY ENROLLED TEMPLATE USED   |     | X   |
|   30 | CCHT   | CCF CAREGIVER-OTHER                 | CCF CAREGIVER-OTHER                 | CCF CAREGIVER-OTHER                 | CCF CAREGIVER-OTHER                 | CCF CAREGIVER-OTHER                 |     | X   |
|   31 | CCHT   | CCF CAREGIVER-FRIEND/NEIGHBOR       | CCF CAREGIVER-FRIEND/NEIGHBOR       | CCF CAREGIVER-FRIEND/NEIGHBOR       | CCF CAREGIVER-FRIEND/NEIGHBOR       | CCF CAREGIVER-FRIEND/NEIGHBOR       |     | X   |
|   32 | CCHT   | CCF CAREGIVER-CHILD                 | CCF CAREGIVER-CHILD                 | CCF CAREGIVER-CHILD                 | CCF CAREGIVER-CHILD                 | CCF CAREGIVER-CHILD                 |     | X   |
|   33 | CCHT   | CCF CAREGIVER-SPOUSE                | CCF CAREGIVER-SPOUSE                | CCF CAREGIVER-SPOUSE                | CCF CAREGIVER-SPOUSE                | CCF CAREGIVER-SPOUSE                |     | X   |
|   34 | CCHT   | CCF CAREGIVER'S NAME                | CCF CAREGIVER'S NAME                | CCF CAREGIVER'S NAME                | CCF CAREGIVER'S NAME                | CCF CAREGIVER'S NAME                |     | X   |
|   35 | CCHT   | CAREGIVER                           | RISK                                | ASSESSMENT                          | SCREEN                              |                                     | X   | X   |
|   36 | CCHT   | CAREGIVER                           | RISK                                | ASSESSMENT                          | SCORE                               | 16                                  |     | X   |
|   37 | CCHT   | CAREGIVER                           | RISK                                | ASSESSMENT                          | SCORE                               | 15                                  |     | X   |
|   38 | CCHT   | CAREGIVER                           | RISK                                | ASSESSMENT                          | SCORE                               | 14                                  |     | X   |
|   39 | CCHT   | CAREGIVER                           | RISK                                | ASSESSMENT                          | SCORE                               | 13                                  |     | X   |
|   40 | CCHT   | CAREGIVER                           | RISK                                | ASSESSMENT                          | SCORE                               | 12                                  |     | X   |
|   41 | CCHT   | CAREGIVER                           | RISK                                | ASSESSMENT                          | SCORE                               | 11                                  |     | X   |
|   42 | CCHT   | CAREGIVER                           | RISK                                | ASSESSMENT                          | SCORE                               | 10                                  |     | X   |
|   43 | CCHT   | CAREGIVER                           | RISK                                | ASSESSMENT                          | SCORE                               | 9                                   |     | X   |
|   44 | CCHT   | CAREGIVER                           | RISK                                | ASSESSMENT                          | SCORE                               | 8                                   |     | X   |
|   45 | CCHT   | CAREGIVER                           | RISK                                | ASSESSMENT                          | SCORE                               | 7                                   |     | X   |
|   46 | CCHT   | CAREGIVER                           | RISK                                | ASSESSMENT                          | SCORE                               | 6                                   |     | X   |
|   47 | CCHT   | CAREGIVER                           | RISK                                | ASSESSMENT                          | SCORE                               | 5                                   |     | X   |
|   48 | CCHT   | CAREGIVER                           | RISK                                | ASSESSMENT                          | SCORE                               | 4                                   |     | X   |
|   49 | CCHT   | CAREGIVER                           | RISK                                | ASSESSMENT                          | SCORE                               | 3                                   |     | X   |
|   50 | CCHT   | CAREGIVER                           | RISK                                | ASSESSMENT                          | SCORE                               | 2                                   |     | X   |
|   51 | CCHT   | CAREGIVER                           | RISK                                | ASSESSMENT                          | SCORE                               | 1                                   |     | X   |
|   52 | CCHT   | CAREGIVER                           | RISK                                | ASSESSMENT                          | SCORE                               | 0                                   |     | X   |
|   53 | CCHT   | CAREGIVER                           | ASSESSMENT SCREEN DONE              | ASSESSMENT SCREEN DONE              | ASSESSMENT SCREEN DONE              | ASSESSMENT SCREEN DONE              | X   | X   |
|   54 | CCHT   | UNCERTAIN                           | WHAT TO DO=NEARLY ALWAYS            | WHAT TO DO=NEARLY ALWAYS            | WHAT TO DO=NEARLY ALWAYS            | WHAT TO DO=NEARLY ALWAYS            | X   | X   |
|   55 | CCHT   | UNCERTAIN                           | WHAT TO DO=FREQUENTLY               | WHAT TO DO=FREQUENTLY               | WHAT TO DO=FREQUENTLY               | WHAT TO DO=FREQUENTLY               | X   | X   |
|   56 | CCHT   | UNCERTAIN                           | WHAT TO DO=SOMETIMES                | WHAT TO DO=SOMETIMES                | WHAT TO DO=SOMETIMES                | WHAT TO DO=SOMETIMES                | X   | X   |
|   57 | CCHT   | UNCERTAIN                           | WHAT TO DO=RARELY                   | WHAT TO DO=RARELY                   | WHAT TO DO=RARELY                   | WHAT TO DO=RARELY                   | X   | X   |
|   58 | CCHT   | UNCERTAIN                           | WHAT TO DO=NEVER                    | WHAT TO DO=NEVER                    | WHAT TO DO=NEVER                    | WHAT TO DO=NEVER                    | X   | X   |
|   59 | CCHT   | STRAINED                            | WITH RELATIVES=NRLY ALWAYS          | WITH RELATIVES=NRLY ALWAYS          | WITH RELATIVES=NRLY ALWAYS          | WITH RELATIVES=NRLY ALWAYS          | X   | X   |
|   60 | CCHT   | STRAINED                            | WITH RELATIVES=FREQUENTLY           | WITH RELATIVES=FREQUENTLY           | WITH RELATIVES=FREQUENTLY           | WITH RELATIVES=FREQUENTLY           | X   | X   |
|   61 | CCHT   | STRAINED                            | WITH RELATIVES=SOMETIMES            | WITH RELATIVES=SOMETIMES            | WITH RELATIVES=SOMETIMES            | WITH RELATIVES=SOMETIMES            | X   | X   |
|   62 | CCHT   | STRAINED                            | WITH RELATIVES=RARELY               | WITH RELATIVES=RARELY               | WITH RELATIVES=RARELY               | WITH RELATIVES=RARELY               | X   | X   |
|   63 | CCHT   | STRAINED                            | WITH RELATIVES=NEVER                | WITH RELATIVES=NEVER                | WITH RELATIVES=NEVER                | WITH RELATIVES=NEVER                | X   | X   |
|   64 | CCHT   | STRESSED                            | WORK/FAMILY=NEARLY ALWAYS           | WORK/FAMILY=NEARLY ALWAYS           | WORK/FAMILY=NEARLY ALWAYS           | WORK/FAMILY=NEARLY ALWAYS           | X   | X   |
|   65 | CCHT   | STRESSED                            | WORK/FAMILY=FREQUENTLY              | WORK/FAMILY=FREQUENTLY              | WORK/FAMILY=FREQUENTLY              | WORK/FAMILY=FREQUENTLY              | X   | X   |
|   66 | CCHT   | STRESSED                            | WORK/FAMILY=SOMETIMES               | WORK/FAMILY=SOMETIMES               | WORK/FAMILY=SOMETIMES               | WORK/FAMILY=SOMETIMES               | X   | X   |
|   67 | CCHT   | STRESSED                            | WORK/FAMILY=RARELY                  | WORK/FAMILY=RARELY                  | WORK/FAMILY=RARELY                  | WORK/FAMILY=RARELY                  | X   | X   |
|   68 | CCHT   | STRESSED                            | WORK/FAMILY=NEVER                   | WORK/FAMILY=NEVER                   | WORK/FAMILY=NEVER                   | WORK/FAMILY=NEVER                   | X   | X   |
|   69 | CCHT   | MAKE TIME FOR SELF=NEARLY ALWAYS    | MAKE TIME FOR SELF=NEARLY ALWAYS    | MAKE TIME FOR SELF=NEARLY ALWAYS    | MAKE TIME FOR SELF=NEARLY ALWAYS    | MAKE TIME FOR SELF=NEARLY ALWAYS    |     | X   |
|   70 | CCHT   | MAKE TIME FOR SELF=FREQUENTLY       | MAKE TIME FOR SELF=FREQUENTLY       | MAKE TIME FOR SELF=FREQUENTLY       | MAKE TIME FOR SELF=FREQUENTLY       | MAKE TIME FOR SELF=FREQUENTLY       |     | X   |
|   71 | CCHT   | MAKE TIME FOR SELF=SOMETIMES        | MAKE TIME FOR SELF=SOMETIMES        | MAKE TIME FOR SELF=SOMETIMES        | MAKE TIME FOR SELF=SOMETIMES        | MAKE TIME FOR SELF=SOMETIMES        |     | X   |
|   72 | CCHT   | MAKE TIME FOR SELF=RARELY           | MAKE TIME FOR SELF=RARELY           | MAKE TIME FOR SELF=RARELY           | MAKE TIME FOR SELF=RARELY           | MAKE TIME FOR SELF=RARELY           |     | X   |
|   73 | CCHT   | MAKE TIME FOR SELF=NEVER            | MAKE TIME FOR SELF=NEVER            | MAKE TIME FOR SELF=NEVER            | MAKE TIME FOR SELF=NEVER            | MAKE TIME FOR SELF=NEVER            |     | X   |
|   74 | CCHT   | C/G RISK SCREEN TEMPLATE USED       | C/G RISK SCREEN TEMPLATE USED       | C/G RISK SCREEN TEMPLATE USED       | C/G RISK SCREEN TEMPLATE USED       | C/G RISK SCREEN TEMPLATE USED       |     | X   |
|   75 | CCHT   | REFERRALS FOR VETERAN/CAREGIVER     | REFERRALS FOR VETERAN/CAREGIVER     | REFERRALS FOR VETERAN/CAREGIVER     | REFERRALS FOR VETERAN/CAREGIVER     | REFERRALS FOR VETERAN/CAREGIVER     | X   | X   |
|   76 | CCHT   | VETERAN REFERRAL SOCIAL WORK        | VETERAN REFERRAL SOCIAL WORK        | VETERAN REFERRAL SOCIAL WORK        | VETERAN REFERRAL SOCIAL WORK        | VETERAN REFERRAL SOCIAL WORK        |     | X   |
|   77 | CCHT   | VETERAN REFERRAL HOSPICE            | VETERAN REFERRAL HOSPICE            | VETERAN REFERRAL HOSPICE            | VETERAN REFERRAL HOSPICE            | VETERAN REFERRAL HOSPICE            |     | X   |
|   78 | CCHT   | VETERAN REFERRAL SVCS IN PLACE      | VETERAN REFERRAL SVCS IN PLACE      | VETERAN REFERRAL SVCS IN PLACE      | VETERAN REFERRAL SVCS IN PLACE      | VETERAN REFERRAL SVCS IN PLACE      |     | X   |
|   79 | CCHT   | VETERAN REFERRAL(S) NON VA SYSTEM   | VETERAN REFERRAL(S) NON VA SYSTEM   | VETERAN REFERRAL(S) NON VA SYSTEM   | VETERAN REFERRAL(S) NON VA SYSTEM   | VETERAN REFERRAL(S) NON VA SYSTEM   |     | X   |
|   80 | CCHT   | VETERAN REFERRAL(S) VA SYSTEM       | VETERAN REFERRAL(S) VA SYSTEM       | VETERAN REFERRAL(S) VA SYSTEM       | VETERAN REFERRAL(S) VA SYSTEM       | VETERAN REFERRAL(S) VA SYSTEM       |     | X   |
|   81 | CCHT   | VETERAN REFERRAL NURS HOME PLACEMNT | VETERAN REFERRAL NURS HOME PLACEMNT | VETERAN REFERRAL NURS HOME PLACEMNT | VETERAN REFERRAL NURS HOME PLACEMNT | VETERAN REFERRAL NURS HOME PLACEMNT |     | X   |
|   82 | CCHT   | VETERAN REFERRAL HOUSING            | VETERAN REFERRAL HOUSING            | VETERAN REFERRAL HOUSING            | VETERAN REFERRAL HOUSING            | VETERAN REFERRAL HOUSING            |     | X   |
|   83 | CCHT   | VETERAN REFERRAL ADULT DAY CARE     | VETERAN REFERRAL ADULT DAY CARE     | VETERAN REFERRAL ADULT DAY CARE     | VETERAN REFERRAL ADULT DAY CARE     | VETERAN REFERRAL ADULT DAY CARE     |     | X   |
|   84 | CCHT   | VETERAN REFERRAL RESPITE            | VETERAN REFERRAL RESPITE            | VETERAN REFERRAL RESPITE            | VETERAN REFERRAL RESPITE            | VETERAN REFERRAL RESPITE            |     | X   |
|   85 | CCHT   | VETERAN REFERRAL HOMEMKR/CHORE ASST | VETERAN REFERRAL HOMEMKR/CHORE ASST | VETERAN REFERRAL HOMEMKR/CHORE ASST | VETERAN REFERRAL HOMEMKR/CHORE ASST | VETERAN REFERRAL HOMEMKR/CHORE ASST |     | X   |
|   86 | CCHT   | VETERAN REFERRAL HOME HEALTH SVC    | VETERAN REFERRAL HOME HEALTH SVC    | VETERAN REFERRAL HOME HEALTH SVC    | VETERAN REFERRAL HOME HEALTH SVC    | VETERAN REFERRAL HOME HEALTH SVC    |     | X   |
|   87 | CCHT   | VETERAN REFERRAL TRANSPORTATION     | VETERAN REFERRAL TRANSPORTATION     | VETERAN REFERRAL TRANSPORTATION     | VETERAN REFERRAL TRANSPORTATION     | VETERAN REFERRAL TRANSPORTATION     |     | X   |

|   88 | CCHT   | VETERAN REFERRAL EMPLOYMENT ASSIST   |    | X   |
|------|--------|--------------------------------------|----|-----|
|   89 | CCHT   | VETERAN REFERRAL FINANCIAL ASSIST    |    | X   |
|   90 | CCHT   | VETERAN REFERRAL LEGAL ASSIST        |    | X   |
|   91 | CCHT   | VETERAN REFERRAL MEDICAL EVAL, F/U   |    | X   |
|   92 | CCHT   | VETERAN REFERRAL FAMILY COUNSEL      |    | X   |
|   93 | CCHT   | VETERAN REFERRAL INDIVIDUAL COUNSEL  |    | X   |
|   94 | CCHT   | VETERAN REFERRAL OTHER SERVICE       |    | X   |
|   95 | CCHT   | VETERAN REFERRAL EDUC/TRAINING       |    | X   |
|   96 | CCHT   | CAREGIVER REFERRAL SVCS IN PLACE     |    | X   |
|   97 | CCHT   | CAREGIVER REFERRAL(S) NON VA SYSTEM  |    | X   |
|   98 | CCHT   | CAREGIVER REFERRAL(S) VA SYSTEM      |    | X   |
|   99 | CCHT   | CAREGIVER REFERRAL BEREAVE SUPPORT   |    | X   |
|  100 | CCHT   | CAREGIVER REFERRAL OTHER SERVICE     |    | X   |
|  101 | CCHT   | CAREGIVER REFERRAL MEDICAL EVAL,F/U  |    | X   |
|  102 | CCHT   | CAREGIVER REFERRAL EDUC/TRAINING     |    | X   |
|  103 | CCHT   | CAREGIVER REFERRAL C/G SUPPORT GRP   |    | X   |
|  104 | CCHT   | CAREGIVER REFERRAL FAMILY COUNSEL    |    | X   |
|  105 | CCHT   | CAREGIVER REFERRAL INDIVID COUNSEL   |    | X   |
|  106 | CCHT   | CG/VETERAN REFERRAL TEMPLATE DONE    |    | X   |
|  107 | CCHT   | CG/VETERAN REFERRAL TEMPLATE USED    |    | X   |
|  108 | CCHT   | DISCHARGE                            | X  | X   |
|  109 | CCHT   | DISCHARGE-PT/CG REQUEST DC SERVICES  |    | X   |
|  110 | CCHT   | DISCHARGE-REFERRED TO NEW LOCATION   |    | X   |
|  111 | CCHT   | DISCHARGE-REFERRED TO MENTAL HEALTH  |    | X   |
|  112 | CCHT   | DISCHARGE-REFERRED TO SOCIAL WORK    |    | X   |
|  113 | CCHT   | DISCHARGE-REFERRED TO PRIMARY CARE   |    | X   |
|  114 | CCHT   | DISCHARGE-REFERRED TO HOSPICE        |    | X   |
|  115 | CCHT   | DISCHARGE-PATIENT IS DECEASED        |    | X   |
|  116 | CCHT   | DISCHARGE-PHONE,ELECT SVCS UNAVAIL   |    | X   |
|  117 | CCHT   | DISCHARGE-NO VA PRIMARY CARE SVCS    |    | X   |
|  118 | CCHT   | DISCHARGE-ADMITTED TO NURSING HOME   |    | X   |
|  119 | CCHT   | DISCHARGE-RELOCATED OUT OF SVC AREA  |    | X   |
|  120 | CCHT   | DISCHARGE-UNABLE TO OPERATE DEVICES  |    | X   |
|  121 | CCHT   | DISCHARGE-HAS MET GOALS              |    | X   |
|  122 | CCHT   | ENROLLMENT-ENDING DATE               |    | X   |
|  123 | CCHT   | CCF UNPAID CAREGIVER-YES             |    | X   |
|  124 | CCHT   | CCF DOES NOT MEET CCM CRITERIA       |    | X   |
|  125 | CCHT   | CCF INITIAL ASSESSMENT DONE          |    | X   |
|  126 | CCHT   | CCF DOES NOT MEET NIC CRITERIA       |    | X   |
|  127 | CCHT   | CAREGIVER ASSESSMENT TEMPLATE USED   |    | X   |
|  128 | CCHT   | PLAN-MED DISCREP SENT TO PROVIDER    |    | X   |
|  129 | CCHT   | PLAN-REVIEWED LIST CURRENT MEDS      |    | X   |
|  130 | CCHT   | PT/CG HAS QUESTIONS ON MEDS-NO       |    | X   |
|  131 | CCHT   | PT/CG HAS QUESTIONS ON MEDS-YES      |    | X   |
|  132 | CCHT   | PT/CG HAS LIST OF ACTIVE MEDS-NO     |    | X   |
|  133 | CCHT   | PT/CG HAS LIST OF ACTIVE MEDS-YES    |    | X   |
|  134 | CCHT   | GETS MEDS VIA NON-VA PROVIDER-NO     |    | X   |
|  135 | CCHT   | GETS MEDS VIA NON-VA PROVIDER-YES    |    | X   |
|  136 | CCHT   | MEDS ADAPTATIONS-NONE NEEDED         |    | X   |
|  137 | CCHT   | MEDS ADAPTATIONS-OTHER               |    | X   |
|  138 | CCHT   | MEDS ADAPT-FOR VISUAL IMPAIRMENT     |    | X   |
|  139 | CCHT   | MEDS ADAPT-VA PREPARES/POURS MEDS    |    | X   |
|  140 | CCHT   | MEDS ADAPT-MEDS ARE COLOR CODED      |    | X   |
|  141 | CCHT   | MEDS ADAPT-USES PILLBOX              |    | X   |
|  142 | CCHT   | MEDS SPECIAL ADAPTATIONS             |    | X   |
|  143 | CCHT   | PT/CG TAKES MEDS AS PRESCRIBED-NO    |    | X   |
|  144 | CCHT   | PT/CG TAKES MEDS AS PRESCRIBED-YES   |    | X   |
|  145 | CCHT   | PT/CG KNOWS REFILL PROCESS-NO        |    | X   |
|  146 | CCHT   | PT/CG KNOWS REFILL PROCESS-YES       |    | X   |
|  147 | CCHT   | PT/CG KNOWS MED SIDE EFF-NO          |    | X   |
|  148 | CCHT   | PT/CG KNOWS MED SIDE EFFECTS-YES     |    | X   |
|  149 | CCHT   | PT/CG KNOWS MED INDICATIONS-NO       |    | X   |
|  150 | CCHT   | PT/CG KNOWS MED INDICATIONS-YES      |    | X   |
|  151 | CCHT   | LEARNING BARRIER-VISUALLY IMPAIRED   |    | X   |
|  152 | CCHT   | LEARNING BARRIER-LANGUAGE            |    | X   |
|  153 | CCHT   | LEARNING BARRIER-UNABLE TO READ      |    | X   |
|  154 | CCHT   | LEARNING BARRIER-NONE IDENTIFIED     |    | X   |
|  155 | CCHT   | CLINICAL REASON FOR ENROLLMENT       |    | X   |
|  156 | CCHT   | TELEHEALTH DEMOGRAPHICS              | X  | X   |
|  157 | CCHT   | DISEASE INDICATIONS-OTHER            |    | X   |
|  158 | CCHT   | DISEASE INDICATIONS-SUBST ABUSE      |    | X   |

|   159 | CCHT   | DISEASE INDICATIONS-HYPERTENSION     |    | X   |
|-------|--------|--------------------------------------|----|-----|
|   160 | CCHT   | DISEASE INDICATIONS-PTSD             |    | X   |
|   161 | CCHT   | DISEASE INDICATIONS-DEPRESSION       |    | X   |
|   162 | CCHT   | DISEASE INDICATIONS-DIABETES         |    | X   |
|   163 | CCHT   | DISEASE INDICATIONS-COPD             |    | X   |
|   164 | CCHT   | DISEASE INDICATIONS-CHF              |    | X   |
|   165 | CCHT   | CCF 12 OR MORE CLINIC STOPS          |    | X   |
|   166 | CCHT   | CCF LIVES ALONE IN COMMUNITY         |    | X   |
|   167 | CCHT   | CCF AGE 75 OR GREATER                |    | X   |
|   168 | CCHT   | CCF PROBLEMS WITH 3 OR MORE IADL     |    | X   |
|   169 | CCHT   | CCF 2 OR MORE ADL DEFICITS           |    | X   |
|   170 | CCHT   | CCF MEETS NIC CATEGORY B CRITERIA    |    | X   |
|   171 | CCHT   | CCF LIFE EXPECTANCY < 6 MO           |    | X   |
|   172 | CCHT   | CCF 1 OR MORE BEHAV/COGN PROBLEMS    |    | X   |
|   173 | CCHT   | CCF PROBLEMS IN 3 OR MORE ADLS       |    | X   |
|   174 | CCHT   | CCF MEETS NIC CATEGORY A CRITERIA    |    | X   |
|   175 | CCHT   | CCF NIC CRITERIA NO-HLTH PROMOTION   |    | X   |
|   176 | CCHT   | CCF NIC CRITERIA NO-ACUTE CARE MGMT  |    | X   |
|   177 | CCHT   | CCF COMPLEXITY TOO GREAT-NO          |    | X   |
|   178 | CCHT   | CCF SERVICES IN PLACE-NO             |    | X   |
|   179 | CCHT   | CCF SERVICES IN PLACE-YES            |    | X   |
|   180 | CCHT   | CCF RECOMMEND REFERRAL-NO            |    | X   |
|   181 | CCHT   | CCF RECOMMEND REFERRAL               |    | X   |
|   182 | CCHT   | CCF COMPLEXITY TOO GREAT-YES         |    | X   |
|   183 | CCHT   | CCF POTENTIAL FOR INCR INDEP-NO      |    | X   |
|   184 | CCHT   | CCF POTENTIAL FOR INCR INDEP-YES     |    | X   |
|   185 | CCHT   | CCF FLARE UP CHRONIC CONDITION-NO    |    | X   |
|   186 | CCHT   | CCF FLARE UP CHRONIC CONDITION-YES   |    | X   |
|   187 | CCHT   | RECENT CHANGE IN FUNCTION-NO         |    | X   |
|   188 | CCHT   | RECENT CHANGE IN FUNCTION-YES        |    | X   |
|   189 | CCHT   | CCF AGITATED/DISORIENTED-NO          |    | X   |
|   190 | CCHT   | CCF AGITATED/DISORIENTED-YES         |    | X   |
|   191 | CCHT   | CCF DIFFIC MAKE SELF UNDERSTOOD-NO   |    | X   |
|   192 | CCHT   | CCF DIFFIC MAKE SELF UNDERSTOOD-YES  |    | X   |
|   193 | CCHT   | CCF DIFFIC REASONABLE DECISIONS-NO   |    | X   |
|   194 | CCHT   | CCF DIFFIC REASONABLE DECISIONS-YES  |    | X   |
|   195 | CCHT   | CCF RESISTING CARE-NO                |    | X   |
|   196 | CCHT   | CCF RESISTING CARE-YES               |    | X   |
|   197 | CCHT   | CCF PHYSICALLY ABUSIVE BEHAVIOR-NO   |    | X   |
|   198 | CCHT   | CCF PHYSICALLY ABUSIVE BEHAVIOR-YES  |    | X   |
|   199 | CCHT   | CCF VERBALLY ABUSIVE BEHAVIOR-NO     |    | X   |
|   200 | CCHT   | CCF VERBALLY ABUSIVE BEHAVIOR-YES    |    | X   |
|   201 | CCHT   | CCF WANDERING-NO                     |    | X   |
|   202 | CCHT   | CCF WANDERING-YES                    |    | X   |
|   203 | CCHT   | CCF PTSD/OTHER ANXIETY-NO            |    | X   |
|   204 | CCHT   | CCF PTSD/OTHER ANXIETY-YES           |    | X   |
|   205 | CCHT   | CCF SUBST ABUSE/DEPENDENCE-NO        |    | X   |
|   206 | CCHT   | CCF SUBST ABUSE/DEPENDENCE-YES       |    | X   |
|   207 | CCHT   | CCF MOOD DISORDER MANIC-NO           |    | X   |
|   208 | CCHT   | CCF MOOD DISORDER MANIC-YES          |    | X   |
|   209 | CCHT   | CCF MOOD DISORDER DEPRESSION-NO      |    | X   |
|   210 | CCHT   | CCF MOOD DISORDER DEPRESSION-YES     |    | X   |
|   211 | CCHT   | CCF DELUSIONS-NO                     |    | X   |
|   212 | CCHT   | CCF DELUSIONS-YES                    |    | X   |
|   213 | CCHT   | CCF HALLUCINATIONS-TACTILE           |    | X   |
|   214 | CCHT   | CCF HALLUCINATIONS-OLFACTORY         |    | X   |
|   215 | CCHT   | CCF HALLUCINATIONS-VISUAL            |    | X   |
|   216 | CCHT   | CCF HALLUCINATIONS-AUDITORY          |    | X   |
|   217 | CCHT   | CCF HALLUCINATIONS-SENSORY           |    | X   |
|   218 | CCHT   | CCF HALLUCINATIONS-NONE              |    | X   |
|   219 | GEC    | REFERRAL IADL                        | X  | X   |
|   220 | GEC    | RECENT CHANGE IN IADL FX-NO          |    | X   |
|   221 | GEC    | RECENT CHANGE IN IADL FX-YES         |    | X   |
|   222 | GEC    | DIFFICULTY MNG FINANCES/LAST 7D-NO   |    | X   |
|   223 | GEC    | DIFFICULTY MNG FINANCES/LAST 7D-YES  |    | X   |
|   224 | GEC    | DIFFICULTY MANAGING MEDS/LAST 7D-NO  |    | X   |
|   225 | GEC    | DIFFICULTY MANAGING MEDS/LAST 7D-YES |    | X   |
|   226 | GEC    | DIFFICULTY USING PHONE/LAST 7D-NO    |    | X   |
|   227 | GEC    | DIFFICULTY USING PHONE/LAST 7D-YES   |    | X   |
|   228 | GEC    | DIFFICULT TRANSPORTATION/LAST 7D-NO  |    | X   |
|   229 | GEC    | DIFFICULT TRANSPORTATION/LAST 7D-YES |    | X   |

|   230 | GEC   | DIFFICULTY WITH SHOPPING/LAST 7D-NO   |    | X   |
|-------|-------|---------------------------------------|----|-----|
|   231 | GEC   | DIFFICULTY WITH SHOPPING/LAST 7D-YES  |    | X   |
|   232 | GEC   | DIFFICULTY W/ HOUSEWORK/LAST 7D-NO    |    | X   |
|   233 | GEC   | DIFFICULTY W/ HOUSEWORK/LAST 7D-YES   |    | X   |
|   234 | GEC   | MEALS PREPARED BY OTHERS/LAST 7D-NO   |    | X   |
|   235 | GEC   | MEALS PREPARED BY OTHERS/LAST 7D-YES  |    | X   |
|   236 | GEC   | DIFFICULTY PREPARE MEALS/LAST 7D-NO   |    | X   |
|   237 | GEC   | DIFFICULTY PREPARE MEALS/LAST 7D-YES  |    | X   |
|   238 | CCHT  | DIFFICULT MNG FINANCES/LAST 7D-NO     |    | X   |
|   239 | CCHT  | DIFFICULT MNG FINANCES/LAST 7D-YES    |    | X   |
|   240 | CCHT  | DIFFICULT MANAGING MEDS/LAST 7D-NO    |    | X   |
|   241 | CCHT  | DIFFICULT MANAGING MEDS/LAST 7D-YES   |    | X   |
|   242 | CCHT  | DIFFICULT USING PHONE LAST 7D-NO      |    | X   |
|   243 | CCHT  | DIFFICULT USING PHONE LAST 7D-YES     |    | X   |
|   244 | CCHT  | DIFFICULT TRANSPRTATION/LAST 7D-NO    |    | X   |
|   245 | CCHT  | DIFFICULT TRANSPRTATION/LAST 7D-YES   |    | X   |
|   246 | CCHT  | DIFFICULT WITH SHOPPING/LAST 7D-NO    |    | X   |
|   247 | CCHT  | DIFFICULT WITH SHOPPING/LAST 7D-YES   |    | X   |
|   248 | CCHT  | DIFFICULT W/ HOUSEWORK/LAST 7D-NO     |    | X   |
|   249 | CCHT  | DIFFICULT W/ HOUSEWORK/LAST 7D-YES    |    | X   |
|   250 | CCHT  | MEALS PREPARED BY OTHER/LAST 7D-NO    |    | X   |
|   251 | CCHT  | MEALS PREPARED BY OTHER/LAST 7D-YES   |    | X   |
|   252 | CCHT  | DIFFICULT PREPARE MEALS/LAST 7D-YES   |    | X   |
|   253 | GEC   | REFERRAL BASIC ADL                    | X  | X   |
|   254 | GEC   | RECENT CHANGE IN ADL FX-NO            |    | X   |
|   255 | GEC   | RECENT CHANGE IN ADL FX-YES           |    | X   |
|   256 | GEC   | INDEPENDENT IN WC LAST 7D-NO          |    | X   |
|   257 | GEC   | INDEPENDENT IN WC LAST 7D-YES         |    | X   |
|   258 | GEC   | MOVING AROUND INDOORS LAST 7D-NO      |    | X   |
|   259 | GEC   | MOVING AROUND INDOORS LAST 7D-YES     |    | X   |
|   260 | GEC   | TRANSFERS HELP/SPRVISION LAST 7D-NO   |    | X   |
|   261 | GEC   | TRANSFERS HELP/SPRVISION LAST 7D-YES  |    | X   |
|   262 | GEC   | BED POSITIONING HELP LAST 7D-NO       |    | X   |
|   263 | GEC   | BED POSITIONING HELP LAST 7D-YES      |    | X   |
|   264 | GEC   | TOILET HELP/SUPERVISION LAST 7D-NO    |    | X   |
|   265 | GEC   | TOILET HELP/SUPERVISION LAST 7D-YES   |    | X   |
|   266 | GEC   | EATING HELP/SUPERVISION LAST 7D-NO    |    | X   |
|   267 | GEC   | EATING HELP/SUPERVISION LAST 7D-YES   |    | X   |
|   268 | GEC   | DRESS HELP/SUPERVISION LAST 7D-NO     |    | X   |
|   269 | GEC   | DRESS HELP/SUPERVISION LAST 7D-YES    |    | X   |
|   270 | GEC   | BATHING PHYS ASST NEEDED LAST 7D-NO   |    | X   |
|   271 | GEC   | BATHING PHYS ASST NEEDED LAST 7D-YES  |    | X   |
|   272 | GEC   | BATHING HELP/SUPERVISION LAST 7D-NO   |    | X   |
|   273 | GEC   | BATHING HELP/SUPERVISION LAST 7D-YES  |    | X   |
|   274 | CCHT  | W/C MOBIL HELP/SUPERV LAST 7D-NO      |    | X   |
|   275 | CCHT  | W/C MOBIL HELP/SUPERV LAST 7D-YES     |    | X   |
|   276 | CCHT  | DRESSING HELP/SUPERV LAST 7D-NO       |    | X   |
|   277 | CCHT  | DRESSING HELP/SUPERV LAST 7D-YES      |    | X   |
|   278 | CCHT  | BATHING HELP/SUPRVISION LAST 7D-NO    |    | X   |
|   279 | CCHT  | BATHING HELP/SUPRVISION LAST 7D-YES   |    | X   |
|   280 | CCHT  | MOVE INDOOR HELP/SUPERV LAST 7D-NO    |    | X   |
|   281 | CCHT  | MOVE INDOOR HELP/SUPERV LAST 7D-YES   |    | X   |
|   282 | CCHT  | TRANSFERS HELP/SUPERV LAST 7D-NO      |    | X   |
|   283 | CCHT  | TRANSFERS HELP/SUPERV LAST 7D-YES     |    | X   |
|   284 | CCHT  | BED MOBIL HELP/SUPERV LAST 7D-NO      |    | X   |
|   285 | CCHT  | BED MOBIL HELP/SUPERV LAST 7D-YES     |    | X   |
|   286 | CCHT  | TOILET HELP/SUPERVISION LAST 7D-NO    |    | X   |
|   287 | CCHT  | TOILET HELP/SUPERVISION LAST 7D-YES   |    | X   |
|   288 | CCHT  | EATING HELP/SUPERVISION LAST 7D-NO    |    | X   |
|   289 | CCHT  | EATING HELP/SUPERVISION LAST 7D-YES   |    | X   |
|   290 | CCHT  | CCF UNPAID CAREGIVER-NO               |    | X   |
|   291 | CCHT  | CCF CAREGIVER CAN'T INCREASE HELP     |    | X   |
|   292 | CCHT  | CCF CAREGIVER CAN INCREASE HELP       |    | X   |
|   293 | CCHT  | CCF CAREGIVER NOT ACCESSIBLE          |    | X   |
|   294 | CCHT  | CCF CAREGIVER ACCESSIBLE              |    | X   |
|   295 | CCHT  | CCF CAREGIVER-IADL HELP               |    | X   |
|   296 | CCHT  | CCF CAREGIVER-ADL HELP                |    | X   |
|   297 | CCHT  | CCF CAREGIVER-EMOTIONAL SUPPORT       |    | X   |
|   298 | CCHT  | CCF CAREGIVER'S PHONE                 |    | X   |
|   299 | CCHT  | CCF CAREGIVER'S ZIP CODE              |    | X   |
|   300 | CCHT  | CCF CAREGIVER'S STATE                 |    | X   |

|   301 | CCHT   | CCF                                 | CAREGIVER'S CITY                    | X   | X   |
|-------|--------|-------------------------------------|-------------------------------------|-----|-----|
|   302 | CCHT   | CCF                                 | CAREGIVER'S STREET ADDRESS          | X   | X   |
|   303 | CCHT   | CCF                                 | CAREGIVER LIVES WITH PT-NO          | X   | X   |
|   304 | CCHT   | CCF                                 | CAREGIVER SAME NAME AS PT           | X   | X   |
|   305 | CCHT   | CCF                                 | CAREGIVER LIVES WITH PT-YES         | X   | X   |
|   306 | CCHT   | CCF                                 | LIVES HOMELESS SHELTER              | X   | X   |
|   307 | CCHT   | CCF                                 | LIVES HOMELESS                      | X   | X   |
|   308 | CCHT   | CCF                                 | LIVES AT OTHER                      | X   | X   |
|   309 | CCHT   | CCF                                 | LIVES DOMICILIARY                   | X   | X   |
|   310 | CCHT   | CCF                                 | LIVES NURSING HOME                  | X   | X   |
|   311 | CCHT   | CCF                                 | LIVES BOARD AND CARE                | X   | X   |
|   312 | CCHT   | CCF                                 | LIVES PRIVATE HOME                  | X   | X   |
|   313 | CCHT   | CCF                                 | LIVES WITH OTHER                    | X   | X   |
|   314 | CCHT   | CCF                                 | GROUP SETTING NON RELATIVES         | X   | X   |
|   315 | CCHT   | CCF                                 | LIVES WITH ADULT CHILD              | X   | X   |
|   316 | CCHT   | CCF                                 | LIVES WITH CHILD                    | X   | X   |
|   317 | CCHT   | CCF                                 | LIVES WITH SPOUSE & OTHERS          | X   | X   |
|   318 | CCHT   | CCF                                 | LIVES WITH SPOUSE ONLY              | X   | X   |
|   319 | CCHT   | CCF                                 | LIVES ALONE                         | X   | X   |
|   320 | CCHT   | CONT OF CARE(EMBEDDED)TEMPLATE USED | CONT OF CARE(EMBEDDED)TEMPLATE USED |     | X   |
|   321 | CCHT   | EMERG PRIORITY LOW-HAS RESOURCES    | EMERG PRIORITY LOW-HAS RESOURCES    |     | X   |
|   322 | CCHT   | EMERG PRIORITY MOD-SVCS AFTER 3-7D  | EMERG PRIORITY MOD-SVCS AFTER 3-7D  |     | X   |
|   323 | CCHT   | EMERG PRIORITY HIGH-IMMEDIATE EVAL  | EMERG PRIORITY HIGH-IMMEDIATE EVAL  |     | X   |
|   324 | CCHT   | ASSESSMENT TX PLAN TEMPLATE USED    | ASSESSMENT TX PLAN TEMPLATE USED    |     | X   |
|   325 | CCHT   | CG/VETERAN REFERRAL(S) NOT UTILIZED | CG/VETERAN REFERRAL(S) NOT UTILIZED |     | X   |
|   326 | CCHT   | REFERRALS CAREGIVER NOT SATISFIED   | REFERRALS CAREGIVER NOT SATISFIED   |     | X   |
|   327 | CCHT   | REFERRALS CAREGIVER SATISFIED       | REFERRALS CAREGIVER SATISFIED       |     | X   |
|   328 | CCHT   | CATEGORY-TELEPHONE CASE MANAGEMENT  | CATEGORY-TELEPHONE CASE MANAGEMENT  |     | X   |
|   329 | CCHT   | CATEGORY-HEALTH PROMOTION           | CATEGORY-HEALTH PROMOTION           |     | X   |
|   330 | CCHT   | CATEGORY-CHRONIC CARE               | CATEGORY-CHRONIC CARE               |     | X   |
|   331 | CCHT   | CATEGORY-ACUTE CARE                 | CATEGORY-ACUTE CARE                 |     | X   |
|   332 | CCHT   | CATEGORY-NON INSTITUTIONAL CARE     | CATEGORY-NON INSTITUTIONAL CARE     |     | X   |
|   333 | CCHT   | VETERAN'S GOAL FOR ENROLLMENT       | VETERAN'S GOAL FOR ENROLLMENT       |     | X   |
|   334 | CCHT   | PERIODIC EVAL DIALOG/TEMPLATE USED  | PERIODIC EVAL DIALOG/TEMPLATE USED  |     | X   |
|   335 | CCHT   | TELEHEALTH DEVICE(S)                | TELEHEALTH DEVICE(S)                | X   | X   |
|   336 | CCHT   | MESSAGING/MONITORING TYPE/SERIAL #  | MESSAGING/MONITORING TYPE/SERIAL #  |     | X   |
|   337 | CCHT   | VIDEOPHONE SERIAL #                 | VIDEOPHONE SERIAL #                 |     | X   |
|   338 | CCHT   | MESSAGING DEVICE TYPE/SERIAL #      | MESSAGING DEVICE TYPE/SERIAL #      |     | X   |
|   339 | CCHT   | DIGITAL CAMERA SERIAL #             | DIGITAL CAMERA SERIAL #             |     | X   |
|   340 | CCHT   | TELEHEALTH DELIVERY/INSTALL MODE    | TELEHEALTH DELIVERY/INSTALL MODE    | X   | X   |
|   341 | CCHT   | APPROX DELIVERY DATE FOR EQUIPMENT  | APPROX DELIVERY DATE FOR EQUIPMENT  |     | X   |
|   342 | CCHT   | EQUIP MAILED,INSTALL BY VET/CAREGVR | EQUIP MAILED,INSTALL BY VET/CAREGVR |     | X   |
|   343 | CCHT   | EQUIP TAKEN HOME,INSTALL BY VET/CG  | EQUIP TAKEN HOME,INSTALL BY VET/CG  |     | X   |
|   344 | CCHT   | EQUIP INSTALLATION MODE-OTHER       | EQUIP INSTALLATION MODE-OTHER       |     | X   |
|   345 | CCHT   | EQUIP INSTALLED BY CONTRACT VENDOR  | EQUIP INSTALLED BY CONTRACT VENDOR  |     | X   |
|   346 | CCHT   | EQUIP INSTALLED BY CARE COORDINATOR | EQUIP INSTALLED BY CARE COORDINATOR |     | X   |
|   347 | CCHT   | MESSAGING/MONITORING-OTHER          | MESSAGING/MONITORING-OTHER          |     | X   |
|   348 | CCHT   | MESSAGING/MONITORING-SPIROMETRY     | MESSAGING/MONITORING-SPIROMETRY     |     | X   |
|   349 | CCHT   | MESSAGING/MONITORING-WEIGHT         | MESSAGING/MONITORING-WEIGHT         |     | X   |
|   350 | CCHT   | MESSAGING/MONITORING-PULSE OXIMETRY | MESSAGING/MONITORING-PULSE OXIMETRY |     | X   |
|   351 | CCHT   | MESSAGING/MONITORING-PULSE          | MESSAGING/MONITORING-PULSE          |     | X   |
|   352 | CCHT   | MESSAGING/MONITORING-BLOOD GLUCOSE  | MESSAGING/MONITORING-BLOOD GLUCOSE  |     | X   |
|   353 | CCHT   | MESSAGING/MONITORING-BLOOD PRESSURE | MESSAGING/MONITORING-BLOOD PRESSURE |     | X   |
|   354 | CCHT   | PERIPHERALS-OTHER                   | PERIPHERALS-OTHER                   |     | X   |
|   355 | CCHT   | PERIPHERALS-GLUCOSE CABLES          | PERIPHERALS-GLUCOSE CABLES          |     | X   |
|   356 | CCHT   | PERIPHERALS-SPIROMETRY (SERIAL #)   | PERIPHERALS-SPIROMETRY (SERIAL #)   |     | X   |
|   357 | CCHT   | PERIPHERALS-STETHOSCOPE             | PERIPHERALS-STETHOSCOPE             |     | X   |
|   358 | CCHT   | PERIPHERALS-BP CUFF (SERIAL #)      | PERIPHERALS-BP CUFF (SERIAL #)      |     | X   |
|   359 | CCHT   | PERIPHERALS-PULSE OX (SERIAL #)     | PERIPHERALS-PULSE OX (SERIAL #)     |     | X   |
|   360 | CCHT   | PERIPHERALS-WEIGHT SCALE (SERIAL #) | PERIPHERALS-WEIGHT SCALE (SERIAL #) |     | X   |
|   361 | CCHT   | PERIPHERALS-NONE NEEDED             | PERIPHERALS-NONE NEEDED             |     | X   |
|   362 | CCHT   | MESSAGING DEVICE-PULSE              | MESSAGING DEVICE-PULSE              |     | X   |
|   363 | CCHT   | MEASURING DEVICE-OTHER              | MEASURING DEVICE-OTHER              |     | X   |
|   364 | CCHT   | MESSAGING DEVICE-WEIGHT             | MESSAGING DEVICE-WEIGHT             |     | X   |
|   365 | CCHT   | MESSAGING DEVICE-PULSE OXIMETRY     | MESSAGING DEVICE-PULSE OXIMETRY     |     | X   |
|   366 | CCHT   | MESSAGING DEVICE-BLOOD GLUCOSE      | MESSAGING DEVICE-BLOOD GLUCOSE      |     | X   |
|   367 | CCHT   | MESSAGING DEVICE-BLOOD PRESSURE     | MESSAGING DEVICE-BLOOD PRESSURE     |     | X   |
|   368 | CCHT   | MEETS TELEHEALTH CRITERIA(YES)      | MEETS TELEHEALTH CRITERIA(YES)      |     | X   |
|   369 | CCHT   | REASON FOR NON-ENROLLMENT           | REASON FOR NON-ENROLLMENT           |     | X   |
|   370 | CCHT   | MEETS TELEHEALTH CRITERIA(NO)       | MEETS TELEHEALTH CRITERIA(NO)       |     | X   |
|   371 | CCHT   | PHONE-NO FEATURES                   | PHONE-NO FEATURES                   |     | X   |

|   372 | CCHT   | PHONE-DSL LINE                      | X   |
|-------|--------|-------------------------------------|-----|
|   373 | CCHT   | PHONE-MODEM                         | X   |
|   374 | CCHT   | INDICATIONS-HX HOSPITALIZATONS      | X   |
|   375 | CCHT   | INDICATIONS-DISTANCE (HOURS)        | X   |
|   376 | CCHT   | INDICATIONS-DISTANCE (MILES)        | X   |
|   377 | CCHT   | INDICATIONS-# OUTPT VISITS PAST YR  | X   |
|   378 | CCHT   | INDICATIONS-HX HIGH COST/HIGH USE   | X   |
|   379 | CCHT   | TELEHEALTH COORDINATOR (NAME)       | X   |
|   380 | CCHT   | SCREENING CONSULT TEMPLATE USED     | X   |
|   381 | CCHT   | REFERRAL-CONSULT COMPLETION         | X   |
|   382 | CCHT   | CONT OF CARE TITLE/TEMPLATE USED    | X   |
|   383 | CCHT   | EQUIP INSTALLED BY VETERAN/CAREGVR  | X   |
|   384 | CCHT   | EQUIP INSTALLED BY SUPPORT STAFF    | X   |
|   385 | CCHT   | EDUC ON EQUIP-CARE COORDINATOR      | X   |
|   386 | CCHT   | EDUC ON EQUIP-SUPPORT STAFF         | X   |
|   387 | CCHT   | EDUC ON EQUIP-CONTRACT VENDOR       | X   |
|   388 | CCHT   | TECH EDUCATION TEMPLATE USED        | X   |
|   389 | CCHT   | VIDEO VISIT-AUDIO/VIDEO CONNECTION  | X   |
|   390 | CCHT   | VIDEO VISIT TEMPLATE USED           | X   |
|   391 | CCHT   | DISCHARGE-OTHER FOLLOW-UP           | X   |
|   392 | CCHT   | DISCHARGE-EQUIP RETURN (OTHER)      | X   |
|   393 | CCHT   | CONTACT MADE FOR EQUIP RETURN       | X   |
|   394 | CCHT   | DISCHARGE-ALL EQUIP RETURNED (NO)   | X   |
|   395 | CCHT   | DISCHARGE-ALL EQUIP RETURNED (YES)  | X   |
|   396 | CCHT   | DISCHARGE-ALL ISSUES ADDRESSED(NO)  | X   |
|   397 | CCHT   | DISCHARGE-ALL ISSUES ADDRESSED(YES) | X   |
|   398 | CCHT   | DISCHARGE-NO RESPONSE TO PROGRAM    | X   |
|   399 | CCHT   | DISCHARGE-PROVIDER REQUESTS DC      | X   |
|   400 | CCHT   | DISCHARGE-PROLONGED HOSPITALIZATION | X   |
|   401 | CCHT   | DISCHARGE TEMPLATE USED             | X   |
|   402 | CCHT   | CG/VET REFER DIALOG/TEMPLATE USED   | X   |
|   403 | CCHT   | C/G RISK ASSESSMENT DIALOG USED     | X   |

REMINDER SPONSOR

1. CARE COORDINATION HOME TELEHEALTH	X
2. Mental Health and Behavioral Science Strategic	X Group

REMINDER COMPUTED FINDINGS

1. VA-AGE	X
2. VA-DATE OF DEATH	X

REMINDER TERM

1. CCHT DISCHARGE REASONS	X
2. CCHT CAREGIVER ASSESSMENT SCORE 0-7	X
3. CCHT CAREGIVER ASSESSMENT SCORE 8 AND HIGHER	X
4. CCHT SUPPRESS FOR AGE &lt;75	X
5. CCHT DEVICE TYPE ASSIGNED	X

REMINDER DEFINITION

1. CCHT PERIODIC EVALUATION	X
2. CCHT CAREGIVER/VETERAN REFERRAL	X
3. CCHT CAREGIVER RISK ASSESSMENT	X
4. CCHT CONTINUUM OF CARE (FOLLOW-UP)	X
5. CCHT CONTINUUM OF CARE (INITIAL)	X
6. CCHT BL SCREENING CONSULT	X
7. CCHT BL TECH EDUCATION	X

REMINDER DIALOG

|   420 | CCHT   | (3 DATA OBJECTS ONLY)                     | X   |
|-------|--------|-------------------------------------------|-----|
|   421 | CCHT   | INTERVENTION TEMPLATE                     | X   |
|   422 | CCHT   | TEMPLATE FOR PREVIOUSLY ENROLLED PATIENTS | X   |
|   423 | CCHT   | CAREGIVER ASSESSMENT TEMPLATE             | X   |
|   424 | CCHT   | ASSESSMENT TREATMENT PLAN TEMPLATE        | X   |
|   425 | CCHT   | PERIODIC EVALUATION TEMPLATE              | X   |
|   426 | CCHT   | SCREENING CONSULT TEMPLATE                | X   |
|   427 | CCHT   | CONTINUUM OF CARE TEMPLATE                | X   |
|   428 | CCHT   | TECH EDUCATION TEMPLATE                   | X   |
|   429 | CCHT   | VIDEO VISIT TEMPLATE                      | X   |
|   430 | CCHT   | DISCHARGE TEMPLATE                        | X   |
|   431 | CCHT   | CAREGIVER/VETERAN REFERRAL                | X   |

1. CCHT CAREGIVER RISK ASSESSMENT	X
2. CCHT CONTINUUM OF CARE (FOLLOW-UP)	X
3. CCHT CONTINUUM OF CARE (INITIAL)	X

HEALTH SUMMARY COMPONENT

CLINICAL REMINDERS DUE	X

VITAL SIGNS SELECTED OUTPAT.	X

LAB TESTS SELECTED	X

PCE HEALTH FACTORS SELECTED	X

NEXT OF KIN	X

CONSULTS BRIEF	X

MAS ADMISSIONS/DISCHARGES	X

MAS CLINIC VISITS PAST	X

HEALTH SUMMARY TYPE

1. DEPR REMINDER STATUS (OBJ)	X
2. PULSE OX OUTPT LAST(OBJ)	X
3. A1C LAST (OBJ)	X
4. CCHT CAREGIVER(OBJ)	X
5. NEXT OF KIN(OBJ)	X
6. CCHT REMINDERS DUE(OBJ)	X
7. CCHT CCF NIC RATING(OBJ)	X
8. GEC IADLS (OBJ)	X
9. GEC BASIC ADLS(OBJ)	X
10. CCHT EMERGENCY LEVELS(OBJ)	X
11. CCHT CATEGORY OF CARE(OBJ)	X
12. CCHT MED RECON (OBJ)	X
13. CCHT VETERAN'S GOAL(OBJ)	X
14. CONSULTS PAST(OBJ)	X
15. CCHT ENROLLMENT START(OBJ)	X
16. ADMISSIONS PAST YR(OBJ)	X
17. OUTPT VISITS PAST YR(OBJ)	X

HEALTH SUMMARY OBJECTS

1. DEPRESSION REMINDER STATUS	X
2. PULSE OXIMETRY OUTPT LAST	X
3. A1C LAST	X
4. CCHT CAREGIVER	X
5. NEXT OF KIN	X
6. CCHT REMINDERS DUE	X
7. CCHT CCF NIC RATING LAST	X
8. GEC IADLS FOR CCHT	X
9. GEC BASIC ADLS	X
10. CCHT EMERG LEVELS	X
11. CCHT CATEGORY OF CARE	X
12. CCHT MED RECON	X
13. CCHT VETERAN'S GOAL	X
14. CONSULTS PAST	X
15. CCHT ENROLLMENT START DATE	X
16. ADMISSIONS PAST YR	X
17. OUTPT VISITS PAST YR	X

TIU DOCUMENT DEFINITION

1. DEPRESSION REMINDER STATUS	X
2. PULSE OXIMETRY OUTPT (LAST)	X
3. HEMOGLOBIN A1C (LAST)	X
4. CCHT CAREGIVER	X
5. NEXT OF KIN	X
6. CCHT REMINDERS DUE	X

ALLERGIES/ADR	X

PAIN	X

PATIENT WEIGHT	X

PATIENT HEIGHT	X

BLOOD PRESSURE	X

RESPIRATION	X

PULSE	X

TEMPERATURE	X

ACTIVE MEDICATIONS	X

1. CCHT CCF NIC RATING LAST	X

PATIENT AGE	X

1. GEC IADLS (LAST)	X

1. GEC BASIC ADLS (LAST)	X
2. CCHT EMERGENCY PRIORITY RATING	X
3. CCHT CATEGORY OF CARE	X
4. CCHT MED RECON	X
5. CCHT VETERAN'S GOAL	X
6. CONSULTS PAST	X
7. CCHT ENROLLMENT START DATE	X
8. ADMISSIONS PAST YR	X
9. OUTPT VISITS PAST YR	X

PATIENT DATE OF DEATH	X

#### Appendix H: Health Factors

| GEC BATHING HELP/SUPERVISION LAST 7D-NO   | GEC TOILET HELP/SUPERVISION LAST 7D-YES   |
|-------------------------------------------|-------------------------------------------|
| GEC BATHING HELP/SUPERVISION LAST 7D-YES  | GEC TRANSFERS HELP/SPRVISION LAST 7D-NO   |
| GEC BATHING PHYS ASST NEEDED LAST 7D-NO   | GEC TRANSFERS HELP/SPRVISION LAST 7D-YES  |
| GEC BATHING PHYS ASST NEEDED LAST 7D-YES  | HT (HOME TELEHEALTH)                      |
| GEC BED POSITIONING HELP LAST 7D-NO       | HT ASSESSMENT/TREATMENT PLAN              |
| GEC BED POSITIONING HELP LAST 7D-YES      | HT BARRIERS TO LEARNING                   |
| GEC DIFFICULT TRANSPORTATION/LAST 7D-NO   | HT BATHING HELP/SUPRVISION LAST 7D-NO     |
| GEC DIFFICULT TRANSPORTATION/LAST 7D-YES  | HT BATHING HELP/SUPRVISION LAST 7D-YES    |
| GEC DIFFICULTY MANAGING MEDS/LAST 7D-NO   | HT BED MOBIL HELP/SUPERV LAST 7D-NO       |
| GEC DIFFICULTY MANAGING MEDS/LAST 7D-YES  | HT BED MOBIL HELP/SUPERV LAST 7D-YES      |
| GEC DIFFICULTY MNG FINANCES/LAST 7D-NO    | HT CAREGIVER ASSESSMENT SCREEN COMPLETED  |
| GEC DIFFICULTY MNG FINANCES/LAST 7D-YES   | HT CAREGIVER REFERRAL BEREAVE SUPPORT     |
| GEC DIFFICULTY PREPARE MEALS/LAST 7D-NO   | HT CAREGIVER REFERRAL C/G SUPPORT GRP     |
| GEC DIFFICULTY PREPARE MEALS/LAST 7D-YES  | HT CAREGIVER REFERRAL EDUC/TRAINING       |
| GEC DIFFICULTY USING PHONE/LAST 7D-NO     | HT CAREGIVER REFERRAL FAMILY COUNSEL      |
| GEC DIFFICULTY USING PHONE/LAST 7D-YES    | HT CAREGIVER REFERRAL INDIVID COUNSEL     |
| GEC DIFFICULTY W/ HOUSEWORK/LAST 7D-NO    | HT CAREGIVER REFERRAL MEDICAL EVAL,F/U    |
| GEC DIFFICULTY W/ HOUSEWORK/LAST 7D-YES   | HT CAREGIVER REFERRAL OTHER SERVICE       |
| GEC DIFFICULTY WITH SHOPPING/LAST 7D-NO   | HT CAREGIVER REFERRAL SOCIAL WORK         |
| GEC DIFFICULTY WITH SHOPPING/LAST 7D-YES  | HT CAREGIVER REFERRAL SVCS IN PLACE       |
| GEC DRESS HELP/SUPERVISION LAST 7D-NO     | HT CAREGIVER REFERRAL(S) NON VA SYSTEM    |
| GEC DRESS HELP/SUPERVISION LAST 7D-YES    | HT CAREGIVER REFERRAL(S) VA SYSTEM        |
| GEC EATING HELP/SUPERVISION LAST 7D-NO    | HT CAREGIVER REVIEW OF WRITTEN MATERIALS  |
| GEC EATING HELP/SUPERVISION LAST 7D-YES   | HT CAREGIVER RISK ASSESSMENT SCREEN       |
| GEC INDEPENDENT IN WC LAST 7D-NO          | HT CAREGIVER STATES ESSENTIAL CONCEPTS    |
| GEC INDEPENDENT IN WC LAST 7D-YES         | HT CATEGORY OF CARE-ACUTE CARE            |
| GEC MEALS PREPARED BY OTHERS/LAST 7D-NO   | HT CATEGORY OF CARE-CHRONIC CARE MGMT     |
| GEC MEALS PREPARED BY OTHERS/LAST 7D-YES  | HT CATEGORY OF CARE-HEALTH PROMOTION      |
| GEC MOVING AROUND INDOORS LAST 7D-NO      | HT CATEGORY OF CARE-NON INSTITUTIONAL     |
| GEC MOVING AROUND INDOORS LAST 7D-YES     | HT CATEGORY OF CARE-OTHER                 |
| GEC RECENT CHANGE IN ADL FX-NO            | HT CCF 1 OR MORE BEHAV/COGN PROBLEMS      |
| GEC RECENT CHANGE IN ADL FX-YES           | HT CCF 12 OR MORE CLINIC STOPS PAST YR    |
| GEC RECENT CHANGE IN IADL FX-NO           | HT CCF 2 OR MORE ADL DEFICITS             |

| GEC RECENT CHANGE IN IADL FX-YES       | HT CCF AGE 75 OR GREATER                |
|----------------------------------------|-----------------------------------------|
| GEC REFERRAL BASIC ADL                 | HT CCF AGITATED/DISORIENTED-NO          |
| GEC REFERRAL IADL                      | HT CCF AGITATED/DISORIENTED-YES         |
| GEC TOILET HELP/SUPERVISION LAST 7D-NO | HT CCF CAREGIVER ACCESSIBLE             |
| HT CCF CAREGIVER CAN'T INCREASE HELP   | HT CCF CAREGIVER CAN INCREASE HELP      |
| HT CCF CAREGIVER LIVES WITH PT-NO      | HT CCF LIVES NURSING HOME               |
| HT CCF CAREGIVER LIVES WITH PT-YES     | HT CCF LIVES PRIVATE HOME               |
| HT CCF CAREGIVER NOT ACCESSIBLE        | HT CCF LIVES WITH ADULT CHILD           |
| HT CCF CAREGIVER-ADL HELP              | HT CCF LIVES WITH CHILD                 |
| HT CCF CAREGIVER-CHILD                 | HT CCF LIVES WITH OTHER                 |
| HT CCF CAREGIVER-EMOTIONAL SUPPORT     | HT CCF LIVES WITH SPOUSE & OTHERS       |
| HT CCF CAREGIVER-FRIEND/NEIGHBOR       | HT CCF LIVES WITH SPOUSE ONLY           |
| HT CCF CAREGIVER-IADL HELP             | HT CCF MEETS CHRONIC CARE MGMT CRITERIA |
| HT CCF CAREGIVER-OTHER                 | HT CCF MEETS NIC CATEGORY A CRITERIA    |
| HT CCF CAREGIVER'S CITY                | HT CCF MEETS NIC CATEGORY B CRITERIA    |
| HT CCF CAREGIVER'S NAME                | HT CCF MEETS NIC CRITERIA               |
| HT CCF CAREGIVER'S PHONE               | HT CCF MOOD DISORDER DEPRESSION-NO      |
| HT CCF CAREGIVER'S STATE               | HT CCF MOOD DISORDER DEPRESSION-YES     |
| HT CCF CAREGIVER'S STREET ADDRESS      | HT CCF MOOD DISORDER MANIC-NO           |
| HT CCF CAREGIVER'S ZIP CODE            | HT CCF MOOD DISORDER MANIC-YES          |
| HT CCF CAREGIVER-SPOUSE                | HT CCF NIC CRITERIA NO-ACUTE CARE MGMT  |
| HT CCF COMPLEXITY TOO GREAT-NO         | HT CCF NIC CRITERIA NO-HLTH PROMOTION   |
| HT CCF COMPLEXITY TOO GREAT-YES        | HT CCF PHYSICALLY ABUSIVE BEHAVIOR-NO   |
| HT CCF DELUSIONS-NO                    | HT CCF PHYSICALLY ABUSIVE BEHAVIOR-YES  |
| HT CCF DELUSIONS-YES                   | HT CCF POTENTIAL FOR INCR INDEP-NO      |
| HT CCF DIFFIC MAKE SELF UNDERSTOOD-NO  | HT CCF POTENTIAL FOR INCR INDEP-YES     |
| HT CCF DIFFIC MAKE SELF UNDERSTOOD-YES | HT CCF PROBLEMS WITH 3 OR MORE ADLS     |
| HT CCF DIFFIC REASONABLE DECISIONS-NO  | HT CCF PROBLEMS WITH 3 OR MORE IADL     |
| HT CCF DIFFIC REASONABLE DECISIONS-YES | HT CCF PTSD/OTHER ANXIETY-NO            |
| HT CCF DOES NOT MEET CCM CRITERIA      | HT CCF PTSD/OTHER ANXIETY-YES           |
| HT CCF DOES NOT MEET NIC CRITERIA      | HT CCF RECOMMEND REFERRAL-NO            |
| HT CCF FLARE UP CHRONIC CONDITION-NO   | HT CCF RECOMMEND REFERRAL-YES           |
| HT CCF FLARE UP CHRONIC CONDITION-YES  | HT CCF RESISTING CARE-NO                |
| HT CCF FOLLOW-UP ASSESSMENT COMPLETED  | HT CCF RESISTING CARE-YES               |
| HT CCF GROUP SETTING NON RELATIVES     | HT CCF SERVICES IN PLACE-NO             |
| HT CCF HALLUCINATIONS-AUDITORY         | HT CCF SERVICES IN PLACE-YES            |
| HT CCF HALLUCINATIONS-NONE             | HT CCF SUBST ABUSE/DEPENDENCE-NO        |
| HT CCF HALLUCINATIONS-OLFACTORY        | HT CCF SUBST ABUSE/DEPENDENCE-YES       |
| HT CCF HALLUCINATIONS-SENSORY          | HT CCF UNPAID CAREGIVER-NO              |
| HT CCF HALLUCINATIONS-TACTILE          | HT CCF UNPAID CAREGIVER-YES             |
| HT CCF HALLUCINATIONS-VISUAL           | HT CCF VERBALLY ABUSIVE BEHAVIOR-NO     |
| HT CCF INITIAL ASSESSMENT COMPLETED    | HT CCF VERBALLY ABUSIVE BEHAVIOR-YES    |
| HT CCF LIFE EXPECTANCY < 6 MO          | HT CCF WANDERING-NO                     |
| HT CCF LIVES ALONE                     | HT CCF WANDERING-YES                    |
| HT CCF LIVES ALONE IN COMMUNITY        | HT CG/VETERAN REFERRAL COMPLETED        |
| HT CCF LIVES AT OTHER                  | HT CG/VETERAN REFERRAL(S) NOT UTILIZED  |

| HT CCF LIVES BOARD AND CARE             | HT CLINICAL REASON FOR ENROLLMENT        |
|-----------------------------------------|------------------------------------------|
| HT CCF LIVES DOMICILIARY                | HT CONSULTS/REFERRALS RECOMMENDED        |
| HT CCF LIVES HOMELESS                   | HT CONTINUUM OF CARE (CCF)               |
| HT CCF LIVES HOMELESS SHELTER           | HT DIFFICULT MANAGING MEDS/LAST 7D-NO    |
| HT DIFFICULT MNG FINANCES/LAST 7D-NO    | HT DIFFICULT MANAGING MEDS/LAST 7D-YES   |
| HT DIFFICULT MNG FINANCES/LAST 7D-YES   | HT EMERG PRIORITY HIGH-IMMEDIATE EVAL    |
| HT DIFFICULT PREPARE MEALS/LAST 7D-NO   | HT EMERG PRIORITY LOW-HAS RESOURCES      |
| HT DIFFICULT PREPARE MEALS/LAST 7D-YES  | HT EMERG PRIORITY MOD-SVCS AFTER 3-7D    |
| HT DIFFICULT TRANSPORTATION/LAST 7D-NO  | HT ENROLLMENT-ENDING DATE                |
| HT DIFFICULT TRANSPORTATION/LAST 7D-YES | HT ENROLLMENT-START DATE                 |
| HT DIFFICULT USING PHONE LAST 7D-NO     | HT ENROLLMENT-START DATE (PREV ENROLL)   |
| HT DIFFICULT USING PHONE LAST 7D-YES    | HT EQUIP INSTALLATION MODE-OTHER         |
| HT DIFFICULT W/ HOUSEWORK/LAST 7D-NO    | HT EQUIP INSTALLED BY CONTRACT VENDOR    |
| HT DIFFICULT W/ HOUSEWORK/LAST 7D-YES   | HT EQUIP INSTALLED BY HOME TELEHEALTH    |
| HT DIFFICULT WITH SHOPPING/LAST 7D-NO   | HT EQUIP INSTALLED BY SUPPORT STAFF      |
| HT DIFFICULT WITH SHOPPING/LAST 7D-YES  | HT EQUIP INSTALLED BY VETERAN/CAREGIVER  |
| HT DISCHARGE                            | HT GETS MEDS VIA NON-VA PROVIDER-NO      |
| HT DISCHARGE-ADMITTED TO NURSING HOME   | HT GETS MEDS VIA NON-VA PROVIDER-YES     |
| HT DISCHARGE-ALL ISSUES ADDRESSED(NO)   | HT HEALTH EDUCATION PLAN                 |
| HT DISCHARGE-ALL ISSUES ADDRESSED(YES)  | HT HEALTH EDUCATION RESPONSE             |
| HT DISCHARGE-HAS MET GOALS              | HT INDICATIONS-# OUTPT VISITS PAST YR    |
| HT DISCHARGE-NO RESPONSE TO PROGRAM     | HT INDICATIONS-DISTANCE (HOURS)          |
| HT DISCHARGE-NO VA PRIMARY CARE SVCS    | HT INDICATIONS-DISTANCE (MILES)          |
| HT DISCHARGE-OTHER FOLLOW-UP            | HT INDICATIONS-HX HIGH COST/HIGH USE     |
| HT DISCHARGE-PATIENT IS DECEASED        | HT INDICATIONS-HX HOSPITALIZATONS        |
| HT DISCHARGE-PHONE,ELECT SVCS UNAVAIL   | HT LEARNING BARRIER-ANGRY                |
| HT DISCHARGE-PROLONGED HOSPITALIZATION  | HT LEARNING BARRIER-ANXIETY              |
| HT DISCHARGE-PROVIDER REQUESTS DC       | HT LEARNING BARRIER-APHASIA              |
| HT DISCHARGE-PT/CG REQUEST DC SERVICES  | HT LEARNING BARRIER-COGNITIVE IMPAIRMENT |
| HT DISCHARGE-REFERRED TO HOSPICE        | HT LEARNING BARRIER-CULTURAL             |
| HT DISCHARGE-REFERRED TO MENTAL HEALTH  | HT LEARNING BARRIER-HEARING IMPAIRED     |
| HT DISCHARGE-REFERRED TO NEW LOCATION   | HT LEARNING BARRIER-HOMELESS             |
| HT DISCHARGE-REFERRED TO PRIMARY CARE   | HT LEARNING BARRIER-IMPAIRED MEMORY      |
| HT DISCHARGE-REFERRED TO SOCIAL WORK    | HT LEARNING BARRIER-LANGUAGE             |
| HT DISCHARGE-RELOCATED OUT OF SVC AREA  | HT LEARNING BARRIER-NONE IDENTIFIED      |
| HT DISCHARGE-UNABLE TO OPERATE DEVICES  | HT LEARNING BARRIER-NOT MOTIVATED        |
| HT DISEASE INDICATIONS-COPD             | HT LEARNING BARRIER-OVERWHELMED          |
| HT DISEASE INDICATIONS-DEPRESSION       | HT LEARNING BARRIER-PAIN                 |
| HT DISEASE INDICATIONS-DIABETES         | HT LEARNING BARRIER-PHYSICAL LIMITATIONS |
| HT DISEASE INDICATIONS-HEART FAILURE    | HT LEARNING BARRIER-POOR CONCENTRATION   |
| HT DISEASE INDICATIONS-HYPERTENSION     | HT LEARNING BARRIER-UNABLE TO READ       |
| HT DISEASE INDICATIONS-OBESITY          | HT LEARNING BARRIER-UNABLE TO WRITE      |
| HT DISEASE INDICATIONS-OTHER            | HT LEARNING BARRIER-VISUALLY IMPAIRED    |
| HT DISEASE INDICATIONS-PTSD             | HT MEALS PREPARED BY OTHER/LAST 7D-NO    |
| HT DISEASE INDICATIONS-SUBSTANCE ABUSE  | HT MEALS PREPARED BY OTHER/LAST 7D-YES   |
| HT DISINTERESTED/LACKS MOTIVATION       | HT MEETS TELEHEALTH CRITERIA(NO)         |

| HT DRESSING HELP/SUPERV LAST 7D-NO         | HT MEETS TELEHEALTH CRITERIA(YES)       |
|--------------------------------------------|-----------------------------------------|
| HT DRESSING HELP/SUPERV LAST 7D-YES        | HT MOVE INDOOR HELP/SUPERV LAST 7D-NO   |
| HT EATING HELP/SUPERVISION LAST 7D-NO      | HT MOVE INDOOR HELP/SUPERV LAST 7D-YES  |
| HT EATING HELP/SUPERVISION LAST 7D-YES     | HT NEEDS REINFORCEMENT/REVIEW/FOLLOW-UP |
| HT NO FOLLOW-UP NEEDED/INDICATED           |                                         |
| HT PERIODIC EVALUATION COMPLETED           |                                         |
| HT PLAN-MED DISCREP SENT TO PROVIDER       |                                         |
| HT PLAN-REVIEWED LIST OF CURRENT MEDS      |                                         |
| HT PT/CG HAS LIST OF ACTIVE MEDS-NO        |                                         |
| HT PT/CG HAS LIST OF ACTIVE MEDS-YES       |                                         |
| HT PT/CG HAS QUESTIONS ON MEDS-NO          |                                         |
| HT PT/CG HAS QUESTIONS ON MEDS-YES         |                                         |
| HT REASON FOR NON-ENROLLMENT               |                                         |
| HT RECENT CHANGE IN FUNCTION-NO            |                                         |
| HT RECENT CHANGE IN FUNCTION-YES           |                                         |
| HT REFERRAL-CONSULT COMPLETION             |                                         |
| HT REFERRALS FOR VETERAN/CAREGIVER         |                                         |
| HT REFERRALS-CAREGIVER NOT SATISFIED       |                                         |
| HT REFERRALS-CAREGIVER SATISFIED           |                                         |
| HT REPEAT DEMONSTRATION NEXT VISIT         |                                         |
| HT TEACH CAREGIVER/FAMILY/SIGNIF OTHER     |                                         |
| HT TECH EDUC DEVICE ASSIGNED               |                                         |
| HT TELEHEALTH DELIVERY/INSTALL MODE        |                                         |
| HT TELEHEALTH DEMOGRAPHICS                 |                                         |
| HT TOILET HELP/SUPERVISION LAST 7D-NO      |                                         |
| HT TOILET HELP/SUPERVISION LAST 7D-YES     |                                         |
| HT TRANSFERS HELP/SUPERV LAST 7D-NO        |                                         |
| HT TRANSFERS HELP/SUPERV LAST 7D-YES       |                                         |
| HT UNABLE TO SCREEN CAREGIVER              |                                         |
| HT VET NOT INTERESTED TELEHEALTH PROGRAM   |                                         |
| HT VETERAN REFERRAL EDUC/TRAINING          |                                         |
| HT VETERAN REFERRAL SVCS IN PLACE          |                                         |
| HT VETERAN REFERRAL(S) NON VA SYSTEM       |                                         |
| HT VETERAN STATES ESSENTIAL CONCEPTS       |                                         |
| PREFERRED HEALTHCARE LANGUAGE              |                                         |
| PREFERRED HEALTHCARE LANGUAGE-ASL          |                                         |
| PREFERRED HEALTHCARE LANGUAGE-BRAILLE      |                                         |
| PREFERRED HEALTHCARE LANGUAGE-CHINESE      |                                         |
| PREFERRED HEALTHCARE LANGUAGE-ENGLISH      |                                         |
| PREFERRED HEALTHCARE LANGUAGE-FRENCH       |                                         |
| PREFERRED HEALTHCARE LANGUAGE-GERMAN       |                                         |
| PREFERRED HEALTHCARE LANGUAGE-ITALIAN      |                                         |
| PREFERRED HEALTHCARE LANGUAGE-KOREAN       |                                         |
| PREFERRED HEALTHCARE LANGUAGE-OTHER        |                                         |
| PREFERRED HEALTHCARE LANGUAGE-  PORTUGUESE |                                         |

| PREFERRED HEALTHCARE LANGUAGE-RUSSIAN    |    |
|------------------------------------------|----|
| PREFERRED HEALTHCARE LANGUAGE-SPANISH    |    |
| PREFERRED HEALTHCARE LANGUAGE-TAGALOG    |    |
| PREFERRED HEALTHCARE LANGUAGE-VIETNAMESE |    |

**Appendix I: Health Factors (Alpha Sort w/ Category)**

**GEC REFERRAL BASIC ADL**

| GEC BATHING HELP/SUPERVISION LAST 7D-NO   | GEC INDEPENDENT IN WC LAST 7D-NO         |
|-------------------------------------------|------------------------------------------|
| GEC BATHING HELP/SUPERVISION LAST 7D-YES  | GEC INDEPENDENT IN WC LAST 7D-YES        |
| GEC BATHING PHYS ASST NEEDED LAST 7D-NO   | GEC MOVING AROUND INDOORS LAST 7D-NO     |
| GEC BATHING PHYS ASST NEEDED LAST 7D-YES  | GEC MOVING AROUND INDOORS LAST 7D-YES    |
| GEC BED POSITIONING HELP LAST 7D-NO       | GEC RECENT CHANGE IN ADL FX-NO           |
| GEC BED POSITIONING HELP LAST 7D-YES      | GEC RECENT CHANGE IN ADL FX-YES          |
| GEC DRESS HELP/SUPERVISION LAST 7D-NO     | GEC TOILET HELP/SUPERVISION LAST 7D-NO   |
| GEC DRESS HELP/SUPERVISION LAST 7D-YES    | GEC TOILET HELP/SUPERVISION LAST 7D-YES  |
| GEC EATING HELP/SUPERVISION LAST 7D-NO    | GEC TRANSFERS HELP/SPRVISION LAST 7D-NO  |
| GEC EATING HELP/SUPERVISION LAST 7D-YES   | GEC TRANSFERS HELP/SPRVISION LAST 7D-YES |

**GEC REFERRAL IADL**

| GEC DIFFICULT TRANSPORTATION/LAST 7D-NO   | GEC DIFFICULTY USING PHONE/LAST 7D-YES   |
|-------------------------------------------|------------------------------------------|
| GEC DIFFICULT TRANSPORTATION/LAST 7D-YES  | GEC DIFFICULTY W/ HOUSEWORK/LAST 7D-NO   |
| GEC DIFFICULTY MANAGING MEDS/LAST 7D-NO   | GEC DIFFICULTY W/ HOUSEWORK/LAST 7D-YES  |
| GEC DIFFICULTY MANAGING MEDS/LAST 7D-YES  | GEC DIFFICULTY WITH SHOPPING/LAST 7D-NO  |
| GEC DIFFICULTY MNG FINANCES/LAST 7D-NO    | GEC DIFFICULTY WITH SHOPPING/LAST 7D-YES |
| GEC DIFFICULTY MNG FINANCES/LAST 7D-YES   | GEC MEALS PREPARED BY OTHERS/LAST 7D-NO  |
| GEC DIFFICULTY PREPARE MEALS/LAST 7D-NO   | GEC MEALS PREPARED BY OTHERS/LAST 7D-YES |
| GEC DIFFICULTY PREPARE MEALS/LAST 7D-YES  | GEC RECENT CHANGE IN IADL FX-NO          |
| GEC DIFFICULTY USING PHONE/LAST 7D-NO     | GEC RECENT CHANGE IN IADL FX-YES         |

**HT (HOME TELEHEALTH)**

| HT CLINICAL REASON FOR ENROLLMENT   | HT ENROLLMENT-START DATE (PREV ENROLL)   |
|-------------------------------------|------------------------------------------|
| HT ENROLLMENT-ENDING DATE           | HT REFERRAL-CONSULT COMPLETION           |
| HT ENROLLMENT-START DATE            | HT VETERAN'S GOAL FOR ENROLLMENT         |

**HT ASSESSMENT/TREATMENT PLAN**

| HT CATEGORY OF CARE-ACUTE CARE        | HT GETS MEDS VIA NON-VA PROVIDER-YES   |
|---------------------------------------|----------------------------------------|
| HT CATEGORY OF CARE-CHRONIC CARE MGMT | HT PERIODIC EVALUATION COMPLETED       |
| HT CATEGORY OF CARE-HEALTH PROMOTION  | HT PLAN-MED DISCREP SENT TO PROVIDER   |
| HT CATEGORY OF CARE-NON INSTITUTIONAL | HT PLAN-REVIEWED LIST OF CURRENT MEDS  |
| HT CATEGORY OF CARE-OTHER             | HT PT/CG HAS LIST OF ACTIVE MEDS-NO    |
| HT EMERG PRIORITY HIGH-IMMEDIATE EVAL | HT PT/CG HAS LIST OF ACTIVE MEDS-YES   |
| HT EMERG PRIORITY LOW-HAS RESOURCES   | HT PT/CG HAS QUESTIONS ON MEDS-NO      |
| HT EMERG PRIORITY MOD-SVCS AFTER 3-7D | HT PT/CG HAS QUESTIONS ON MEDS-YES     |
| HT GETS MEDS VIA NON-VA PROVIDER-NO   |                                        |

HT CAREGIVER ASSESSMENT SCREEN COMPLETED

HT BATHING HELP/SUPRVISION LAST 7D-NO

HT CCF LIVES WITH SPOUSE &amp; OTHERS

HT BATHING HELP/SUPRVISION LAST 7D-YES

HT CCF LIVES WITH SPOUSE ONLY

HT BED MOBIL HELP/SUPERV LAST 7D-NO

HT CCF MEETS CHRONIC CARE MGMT CRITERIA

HT BED MOBIL HELP/SUPERV LAST 7D-YES

HT CCF MEETS NIC CATEGORY A CRITERIA

HT CCF 1 OR MORE BEHAV/COGN PROBLEMS

HT CCF MEETS NIC CATEGORY B CRITERIA

HT CCF 12 OR MORE CLINIC STOPS PAST YR

HT CCF MEETS NIC CRITERIA

HT CCF 2 OR MORE ADL DEFICITS

HT CCF MOOD DISORDER DEPRESSION-NO

HT CCF AGE 75 OR GREATER

HT CCF MOOD DISORDER DEPRESSION-YES

HT CCF AGITATED/DISORIENTED-NO

HT CCF MOOD DISORDER MANIC-NO

HT CCF AGITATED/DISORIENTED-YES

HT CCF MOOD DISORDER MANIC-YES

HT CCF CAREGIVER ACCESSIBLE

HT CCF NIC CRITERIA NO-ACUTE CARE MGMT

HT CCF CAREGIVER CAN INCREASE HELP

HT CCF NIC CRITERIA NO-HLTH PROMOTION

HT CCF CAREGIVER CAN'T INCREASE HELP

HT CCF PHYSICALLY ABUSIVE BEHAVIOR-NO

HT CCF CAREGIVER LIVES WITH PT-NO

HT CCF PHYSICALLY ABUSIVE BEHAVIOR-YES

HT CCF CAREGIVER LIVES WITH PT-YES

HT CCF POTENTIAL FOR INCR INDEP-NO

HT CCF CAREGIVER NOT ACCESSIBLE

HT CCF POTENTIAL FOR INCR INDEP-YES

HT CCF CAREGIVER SAME NAME AS PT

HT CCF PROBLEMS WITH 3 OR MORE ADLS

HT CCF CAREGIVER-ADL HELP

HT CCF PROBLEMS WITH 3 OR MORE IADL

HT CCF CAREGIVER-CHILD

HT CCF PTSD/OTHER ANXIETY-NO

HT CCF CAREGIVER-EMOTIONAL SUPPORT

HT CCF PTSD/OTHER ANXIETY-YES

HT CCF CAREGIVER-FRIEND/NEIGHBOR

HT CCF RECOMMEND REFERRAL-NO

HT CCF CAREGIVER-IADL HELP

HT CCF RECOMMEND REFERRAL-YES

HT CCF CAREGIVER-OTHER

HT CCF RESISTING CARE-NO

HT CCF CAREGIVER'S CITY

HT CCF RESISTING CARE-YES

HT CCF CAREGIVER'S NAME

HT CCF SERVICES IN PLACE-NO

HT CCF CAREGIVER'S PHONE

HT CCF SERVICES IN PLACE-YES

HT CCF CAREGIVER'S STATE

HT CCF SUBST ABUSE/DEPENDENCE-NO

HT CCF CAREGIVER'S STREET ADDRESS

HT CCF SUBST ABUSE/DEPENDENCE-YES

HT CCF CAREGIVER'S ZIP CODE

HT CCF UNPAID CAREGIVER-NO

HT CCF CAREGIVER-SPOUSE

HT CCF UNPAID CAREGIVER-YES

HT CCF COMPLEXITY TOO GREAT-NO

HT CCF VERBALLY ABUSIVE BEHAVIOR-NO

HT CCF COMPLEXITY TOO GREAT-YES

HT CCF VERBALLY ABUSIVE BEHAVIOR-YES

HT CCF DELUSIONS-NO

HT CCF WANDERING-NO

HT CCF DELUSIONS-YES

HT CCF WANDERING-YES

HT CCF DIFFIC MAKE SELF UNDERSTOOD-NO

HT DIFFICULT MANAGING MEDS/LAST 7D-NO

HT CCF DIFFIC MAKE SELF UNDERSTOOD-YES

HT DIFFICULT MANAGING MEDS/LAST 7D-YES

HT CCF DIFFIC REASONABLE DECISIONS-NO

HT DIFFICULT MNG FINANCES/LAST 7D-NO

HT CCF DIFFIC REASONABLE DECISIONS-YES

HT DIFFICULT MNG FINANCES/LAST 7D-YES

HT CCF DOES NOT MEET CCM CRITERIA

HT DIFFICULT PREPARE MEALS/LAST 7D-NO

HT CCF DOES NOT MEET NIC CRITERIA

HT DIFFICULT PREPARE MEALS/LAST 7D-YES

HT CCF FLARE UP CHRONIC CONDITION-NO

HT DIFFICULT TRANSPORTATION/LAST 7D-NO

HT CCF FLARE UP CHRONIC CONDITION-YES

HT DIFFICULT TRANSPORTATION/LAST 7D-YES

**HT CAREGIVER RISK ASSESSMENT SCREEN HT CONTINUUM OF CARE (CCF)**

| HT CCF FOLLOW-UP ASSESSMENT COMPLETED   | HT DIFFICULT USING PHONE LAST 7D-NO    |
|-----------------------------------------|----------------------------------------|
| HT CCF GROUP SETTING NON RELATIVES      | HT DIFFICULT USING PHONE LAST 7D-YES   |
| HT CCF HALLUCINATIONS-AUDITORY          | HT DIFFICULT W/ HOUSEWORK/LAST 7D-NO   |
| HT CCF HALLUCINATIONS-NONE              | HT DIFFICULT W/ HOUSEWORK/LAST 7D-YES  |
| HT CCF HALLUCINATIONS-OLFACTORY         | HT DIFFICULT WITH SHOPPING/LAST 7D-NO  |
| HT CCF HALLUCINATIONS-SENSORY           | HT DIFFICULT WITH SHOPPING/LAST 7D-YES |
| HT CCF HALLUCINATIONS-TACTILE           | HT DRESSING HELP/SUPERV LAST 7D-NO     |
| HT CCF HALLUCINATIONS-VISUAL            | HT DRESSING HELP/SUPERV LAST 7D-YES    |
| HT CCF INITIAL ASSESSMENT COMPLETED     | HT EATING HELP/SUPERVISION LAST 7D-NO  |
| HT CCF LIFE EXPECTANCY < 6 MO           | HT EATING HELP/SUPERVISION LAST 7D-YES |
| HT CCF LIVES ALONE                      | HT MEALS PREPARED BY OTHER/LAST 7D-NO  |
| HT CCF LIVES ALONE IN COMMUNITY         | HT MEALS PREPARED BY OTHER/LAST 7D-YES |
| HT CCF LIVES AT OTHER                   | HT MOVE INDOOR HELP/SUPERV LAST 7D-NO  |
| HT CCF LIVES BOARD AND CARE             | HT MOVE INDOOR HELP/SUPERV LAST 7D-YES |
| HT CCF LIVES DOMICILIARY                | HT RECENT CHANGE IN FUNCTION-NO        |
| HT CCF LIVES HOMELESS                   | HT RECENT CHANGE IN FUNCTION-YES       |
| HT CCF LIVES HOMELESS SHELTER           | HT TOILET HELP/SUPERVISION LAST 7D-NO  |
| HT CCF LIVES NURSING HOME               | HT TOILET HELP/SUPERVISION LAST 7D-YES |
| HT CCF LIVES PRIVATE HOME               | HT TRANSFERS HELP/SUPERV LAST 7D-NO    |
| HT CCF LIVES WITH ADULT CHILD           | HT TRANSFERS HELP/SUPERV LAST 7D-YES   |
| HT CCF LIVES WITH CHILD                 | HT W/C MOBIL HELP/SUPERV LAST 7D-NO    |
| HT CCF LIVES WITH OTHER                 | HT W/C MOBIL HELP/SUPERV LAST 7D-YES   |

**HT DISCHARGE**

| HT DISCHARGE-ADMITTED TO NURSING HOME   | HT DISCHARGE-PROVIDER REQUESTS DC      |
|-----------------------------------------|----------------------------------------|
| HT DISCHARGE-ALL ISSUES ADDRESSED(NO)   | HT DISCHARGE-PT/CG REQUEST DC SERVICES |
| HT DISCHARGE-ALL ISSUES ADDRESSED(YES)  | HT DISCHARGE-REFERRED TO HOSPICE       |
| HT DISCHARGE-HAS MET GOALS              | HT DISCHARGE-REFERRED TO MENTAL HEALTH |
| HT DISCHARGE-NO RESPONSE TO PROGRAM     | HT DISCHARGE-REFERRED TO NEW LOCATION  |
| HT DISCHARGE-NO VA PRIMARY CARE SVCS    | HT DISCHARGE-REFERRED TO PRIMARY CARE  |
| HT DISCHARGE-OTHER FOLLOW-UP            | HT DISCHARGE-REFERRED TO SOCIAL WORK   |
| HT DISCHARGE-PATIENT IS DECEASED        | HT DISCHARGE-RELOCATED OUT OF SVC AREA |
| HT DISCHARGE-PHONE,ELECT SVCS UNAVAIL   | HT DISCHARGE-UNABLE TO OPERATE DEVICES |
| HT DISCHARGE-PROLONGED HOSPITALIZATION  |                                        |

**HT REFERRALS FOR VETERAN/CAREGIVER**

| HT CAREGIVER REFERRAL BEREAVE SUPPORT   | HT VETERAN REFERRAL FAMILY COUNSEL     |
|-----------------------------------------|----------------------------------------|
| HT CAREGIVER REFERRAL C/G SUPPORT GRP   | HT VETERAN REFERRAL FINANCIAL ASSIST   |
| HT CAREGIVER REFERRAL EDUC/TRAINING     | HT VETERAN REFERRAL HOME HEALTH SVC    |
| HT CAREGIVER REFERRAL FAMILY COUNSEL    | HT VETERAN REFERRAL HOMEMKR/CHORE ASST |
| HT CAREGIVER REFERRAL INDIVID COUNSEL   | HT VETERAN REFERRAL HOSPICE            |
| HT CAREGIVER REFERRAL MEDICAL EVAL,F/U  | HT VETERAN REFERRAL HOUSING            |
| HT CAREGIVER REFERRAL OTHER SERVICE     | HT VETERAN REFERRAL INDIVIDUAL COUNSEL |
| HT CAREGIVER REFERRAL SOCIAL WORK       | HT VETERAN REFERRAL LEGAL ASSISTANCE   |
| HT CAREGIVER REFERRAL SVCS IN PLACE     | HT VETERAN REFERRAL MEDICAL EVAL, F/U  |
| HT CAREGIVER REFERRAL(S) NON VA SYSTEM  | HT VETERAN REFERRAL NURS HOME PLACEMNT |

| HT CAREGIVER REFERRAL(S) VA SYSTEM     | HT VETERAN REFERRAL OTHER SERVICE    |
|----------------------------------------|--------------------------------------|
| HT CG/VETERAN REFERRAL COMPLETED       | HT VETERAN REFERRAL RESPITE          |
| HT CG/VETERAN REFERRAL(S) NOT UTILIZED | HT VETERAN REFERRAL SOCIAL WORK      |
| HT REFERRALS-CAREGIVER NOT SATISFIED   | HT VETERAN REFERRAL SVCS IN PLACE    |
| HT REFERRALS-CAREGIVER SATISFIED       | HT VETERAN REFERRAL TRANSPORTATION   |
| HT VETERAN REFERRAL ADULT DAY CARE     | HT VETERAN REFERRAL(S) NON VA SYSTEM |
| HT VETERAN REFERRAL EDUC/TRAINING      | HT VETERAN REFERRAL(S) VA SYSTEM     |
| HT VETERAN REFERRAL EMPLOYMENT ASSIST  |                                      |

**HT TELEHEALTH DELIVERY/INSTALL MODE**

| HT EQUIP INSTALLATION MODE-OTHER         | HT EQUIP TAKEN HOME,INSTALLED BY VET/CG   |
|------------------------------------------|-------------------------------------------|
| HT EQUIP INSTALLED BY SUPPORT STAFF      |                                           |
| HT EQUIP INSTALLED BY VETERAN/CAREGIVER  |                                           |
| HT EQUIP MAILED,INSTALL BY VET/CAREGIVER |                                           |

**HT TELEHEALTH DEMOGRAPHICS**

| HT DISEASE INDICATIONS-COPD            | HT INDICATIONS-# OUTPT VISITS PAST YR    |
|----------------------------------------|------------------------------------------|
| HT DISEASE INDICATIONS-DEPRESSION      | HT INDICATIONS-DISTANCE (HOURS)          |
| HT DISEASE INDICATIONS-DIABETES        | HT INDICATIONS-DISTANCE (MILES)          |
| HT DISEASE INDICATIONS-HEART FAILURE   | HT INDICATIONS-HX HIGH COST/HIGH USE     |
| HT DISEASE INDICATIONS-HYPERTENSION    | HT INDICATIONS-HX HOSPITALIZATONS        |
| HT DISEASE INDICATIONS-OBESITY         | HT MEETS TELEHEALTH CRITERIA(NO)         |
| HT DISEASE INDICATIONS-OTHER           | HT MEETS TELEHEALTH CRITERIA(YES)        |
| HT DISEASE INDICATIONS-PTSD            | HT REASON FOR NON-ENROLLMENT             |
| HT DISEASE INDICATIONS-SUBSTANCE ABUSE | HT VET NOT INTERESTED TELEHEALTH PROGRAM |

**PREFERRED HEALTHCARE LANGUAGE**

| PREFERRED HEALTHCARE LANGUAGE-ENGLISH      | PREFERRED HEALTHCARE LANGUAGE-KOREAN     |
|--------------------------------------------|------------------------------------------|
| PREFERRED HEALTHCARE LANGUAGE-OTHER        | PREFERRED HEALTHCARE LANGUAGE-GERMAN     |
| PREFERRED HEALTHCARE LANGUAGE-ASL          | PREFERRED HEALTHCARE LANGUAGE-VIETNAMESE |
| PREFERRED HEALTHCARE LANGUAGE-BRAILLE      | PREFERRED HEALTHCARE LANGUAGE-TAGALOG    |
| PREFERRED HEALTHCARE LANGUAGE-  PORTUGUESE | PREFERRED HEALTHCARE LANGUAGE-FRENCH     |
| PREFERRED HEALTHCARE LANGUAGE-ITALIAN      | PREFERRED HEALTHCARE LANGUAGE-CHINESE    |
| PREFERRED HEALTHCARE LANGUAGE-RUSSIAN      | PREFERRED HEALTHCARE LANGUAGE-SPANISH    |

#### Appendix J: Education Topics

**VA-HOME TELEHEALTH (HT)**

| VA-HOME TELEHEALTH-CAREGIVER  EDUCATION/SUPPORT    | VA-HOME TELEHEALTH-CAREGIVER  EDUCATION/SUPPORT    |
|----------------------------------------------------|----------------------------------------------------|
| VA-HOME TELEHEALTH-DISEASE  MGMT/PATIENT SELF-MGMT | VA-HOME TELEHEALTH-DISEASE  MGMT/PATIENT SELF-MGMT |

**VA-HOME TELEHEALTH-CAREGIVER EDUCATION/SUPPORT**

The Non-Paid Caregiver will receive both the education (via the in home messaging device, telemonitor, videophone or telephone) as well as the support necessary to enhance the care provided to the Veteran.

1. The Care Coordinator will assign the appropriate DMP to help educate the caregiver on the disease process of the Veteran.
2. The Care Coordinator will help coordinate the appropriate resources to support the caregiver.

**VA-HOME TELEHEALTH-DISEASE MGMT/PATIENT SELF-MGMT**

The Veteran, upon enrollment, will be assigned the appropriate Disease Management Protocol (DMP) that will enhance the Veteran's ability to self-manage his/her chronic disease process.

1. The Care Coordinator will assign a Disease Management Protocol (DMP) appropriate for the veteran upon enrollment.
2. The Care Coordinator will monitor the Veteran's responses to the DMP questions to provide interventions when necessary.
3. Interventions are designed to enhance the Veteran's ability to self-manage his/her disease process.

**VA-HOME TELEHEALTH-IN HOME MONITORING**

Veteran receives care coordination and daily monitoring via an in-home messaging/monitoring device of his/her chronic disease(s) by a Care Coordinator.

1. The Care Coordinator monitors measurements and/or individual responses to questions directly related to the Veteran's chronic disease(s).
2. The Care Coordinator responds/intervenes timely to alerts indicating need.
3. The Care Coordinator updates the Veteran's provider routinely and as needed.
4. Veteran and/or caregiver understand proper setup and procedure for in-home monitoring.
5. Veteran and/or caregiver understand the confidentiality of health information.
6. Veteran and/or caregiver understand that he/she must follow his/her normal emergency plan for any emergency.
7. Veteran and/or caregiver understand that his/her in home messaging/monitoring device is not a 911 or emergency device.
8. Veteran and/or caregiver understand how to contact Home Telehealth staff for any questions, problems with equipment, or concerns.

**VA-HOME TELEHEALTH-MEDICATION MANAGEMENT**

Veteran has provided the VA with a complete list of Non VA medications and OTC drugs &amp; supplements.

The Veteran understands his/her VA prescribed medications and takes his/her medications as prescribed.

1. The Care Coordinator reviews all medications upon enrollment into the HT program and at regular intervals throughout the Veteran's active enrollment.
2. The Care Coordinator reports any discrepancies to the Veteran's provider for reconciliation.
3. The Care Coordinator routinely educates Veteran on his/her medications and responds timely to any question the Veteran may have about his/her medication.

### Appendix K: Acronyms and Glossary

###### National Acronym Directory:

[http://vaww1.va.gov/Acronyms/](http://vaww1.va.gov/Acronyms/)

**Acronyms**

| **Term**   | **Definition**                                                 |
|------------|----------------------------------------------------------------|
| ASU        | Authorization/Subscription Utility                             |
| CCHT       | Care Coordination Home Telehealth (former name; now called HT) |
| CDCO       | Corporate Data Center Operations (includes AITC)               |
| HT         | Home Telehealth                                                |
| CPRS       | Computerized Patient Record System                             |
| DD         | Data Dictionary                                                |
| EPMO       | Enterprise Program Management Office                           |
| ESM        | Enterprise Systems Management (ESM)                            |
| FIM        | Functional Independence Measure                                |
| SFTP       | Secure File Transfer Protocol                                  |
| GMTS       | VistA namespace for Health Summary package                     |
| GUI        | Graphic User Interface                                         |
| IAB        | Initial Assessment & Briefing                                  |
| MED REC    | Medication Reconciliation                                      |
| OCC        | Office of Connected Care                                       |
| OI         | Office of Information                                          |
| OIF/OEF    | Operation Iraqi Freedom/Operation Enduring Freedom             |
| PCS        | Patient Care Services                                          |
| PXRM       | Clinical Reminder Package namespace                            |
| RSD        | Requirements Specification Document                            |
| TIU        | Text Integration Utilities                                     |
| TIU/HS     | TIU-Health Summary data objects                                |
| TXML       | Template format for CPRS GUI dialog templates                  |
| VA         | Department of Veteran Affairs                                  |
| USR        | VistA namespace for ASU package                                |
| VistA      | Veterans Health Information System and Technology Architecture |
| VLER       | Virtual Lifetime Electronic Record                             |

**Glossary**

Master OIT Glossary: [http://vaww.oed.wss.va.gov/process/Lists/glossary/default.aspx](http://vaww.oed.wss.va.gov/process/Lists/glossary/default.aspx)

| Term                                         | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Austin Information Technology Center  (AITC) | Austin Information Technology Center (AITC) is part of the corporate data center Operations (CDCO). The central repository for National  Patient Care Database is maintained at the AITC.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Care Coordinators                            | Care Coordinators are licensed health care professionals who help veteran patients self-manage their condition. Care Coordinators guide and support veteran patients to ensure they receive the right care, in the  right place, at the right time, from the right person.                                                                                                                                                                                                                                                                                                                                                     |
| Corporate Data Center Operations  (CDCO)     | VA's integration of five national data centers, which incorporates the AITC.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Clinical Data  Services (CDS)                | Clinical Data Service (CDS) is the access service to patient-centric, clinical data persisted in HDR (Health Data Repository) data stores.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Clinical Context Object Workgroup  (CCOW)    | Clinical Context Object Workgroup (CCOW) is used to share patient and user context between applications                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Clinical Reminders                           | A clinical reminder is a software decision support tool that defines evaluation and resolution logic for a given clinical activity. The evaluation logic defines conditions in the database, including the presence or absence of specified criteria such as diagnoses, procedures, health factors, medications, or demographic variables (e.g., age, gender). A reminder may or may not require provider resolution, depending on its purpose and design, through a user interface, also  known as a reminder dialog.                                                                                                         |
| Consult                                      | Referral of a patient by a healthcare provider to another hospital service/specialty, to obtain a medical opinion based on patient evaluation and completion of any procedures, modalities, or treatments  the consulting specialist deems necessary to render a medical opinion.                                                                                                                                                                                                                                                                                                                                              |
| Computerized Patient Records System (CPRS)   | Computerized Patient Records System (CPRS) provides an integrated patient record system for clinicians, managers, quality assurance staff, and researchers. The primary goal of CPRS is to create a fast and easy- to-use product that gives physicians enough information through clinical reminders, results reporting, and expert system feedback to make better decisions regarding orders and treatment. VistA software integrated with CPRS includes Pharmacy, Lab, Radiology, Allergy Tracking, Consults, Dietetics, Progress Notes, Problem List, Patient  Administration, Vitals, PCE, TIU, ASU and Clinical Lexicon. |
| Data File Number  (DFN)                      | Patient’s Internal Entry Number (IEN)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Health Data                                  | A data repository of clinical information that resides on one or more                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

| Term                                          | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Repository (HDR)                              | independent platforms and is used by clinicians and other personnel to  facilitate longitudinal patient-centric care.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Health Level 7 (HL7)                          | HL7 is an ANSI standard for electronic data exchange in healthcare environments. It is an interface specification designed to standardize the transfer of health care information between systems. HL7 is an application layer protocol for electronic data exchange in health care environments. The HL7 protocol is a collection of standard formats for health care data. This communication protocol allows healthcare institutions to exchange key sets of data between different application systems. The protocol accommodates the flexibility necessary to allow  compatibility for specialized data sets that have facility-specific needs. |
| ID                                            | Coded Value data type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Interface Engine (IE)                         | A device or software application that connects disparate system, transforms data, converts data, routes data, ensures the delivery of data and is rules based. The IE provides a consistent HL7 compliant communication environment. That is separate from the specific and individual application needs. In this environment, messages can be routed, transformed, converted and delivery guaranteed as required by  the application.                                                                                                                                                                                                               |
| Integration Control Number (ICN)              | The Integration Control Number (ICN) is a unique identifier assigned to patients when they are added to the Master Patient Index (MPI). ICNs fall under two categories: national and local. The ICN follows the ASTM E1714-95 standard for a universal health identifier. ICNs link patients to their records across VA systems.  The ICN is stored in a message using the HL7 CX format. The ID subfield is the ICN.  The type subfield is USVHA.                                                                                                                                                                                                   |
| Master Patient Index (MPI)                    | The objectives of the Master Patient Index (MPI) are to create an index that uniquely identifies each active patient treated by the VA and to identify the sites where a patient is receiving care. This is crucial to the sharing of patient information across sites.  MPI manages the synchronization of patient file information between the Master Patient Index and the patient's treatment facilities to ensure that data being shared is stored in the correct patient's record.                                                                                                                                                             |
| Patient Information  Management System (PIMS) | This umbrella application contains the Scheduling, Registration, PCE, and Enrollment applications that relate to patient information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Protocol                                      | A set of procedures for establishing and controlling data transmission                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Remote Data View  (RDV)                       | A CPRS application that allows a caregiver to view patient data that is  stored in another VistA facility.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Telehealth                                    | Telehealth is the use of electronic communications and information technology to provide and support health care when distance separates  the participants. It covers health care practitioners interacting with patients and patients interacting with other patients.                                                                                                                                                                                                                                                                                                                                                                              |
| Telemedicine                                  | Telemedicine is the provision of care by a licensed independent health                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

| Term                          | Definition                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                               | care provider that directs, diagnoses, or otherwise provides clinical treatment delivered using electronic communications and information  technology when distance separates the provider and the patient. .                                                                                                                                                                                               |
| TCP/IP                        | Transaction Control Protocol/Internet Protocol (TCP/IP) is a set of protocols for Layers 3 (Network) and 4 (Transport) of the OSI network model. TCP/IP has been developed over a period of 30 years under the auspices of the Department of Defense. It is a de facto standard, particularly as higher-level layers over Ethernet. TCP/IP predates the  OSI model; therefore, TCP/IP is not OSI-compliant. |
| VistA                         | Veterans Health Information Systems and Technology Architecture (VistA), formerly known as Decentralized Hospital Computer Program (DHCP), encompasses the complete information environment at VA medical facilities. It consists of hardware, software packages, and comprehensive support for system-wide and station specific, clinical,  and administrative automation needs.                           |
| VistA Interface  Engine (VIE) | Vitria BusinessWare software that has been configured specifically for  the VHA VistA environment                                                                                                                                                                                                                                                                                                           |
| VistAWeb                      | A web-based application to view patient data from various VA facilities.                                                                                                                                                                                                                                                                                                                                    |
| VLER                          | Virtual Lifetime Electronic Record, a program to integrate VA, DoD,  and private patient records.                                                                                                                                                                                                                                                                                                           |