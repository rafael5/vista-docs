"""
Unit tests for classify/rules.py — pure filename + title → DocType classification.
"""

from vista_docs.classify.rules import classify
from vista_docs.models.manifest import DocType


class TestClassifyByFilename:
    def test_technical_manual_tm_suffix(self):
        assert classify("cprsguitm.docx", "") == DocType.TECHNICAL_MANUAL

    def test_technical_manual_explicit(self):
        assert classify("cprs_technical_manual.docx", "") == DocType.TECHNICAL_MANUAL

    def test_user_manual_um_suffix(self):
        assert classify("tiuum.docx", "") == DocType.USER_MANUAL

    def test_installation_guide_ig_suffix(self):
        assert classify("cprsig.docx", "") == DocType.INSTALLATION_GUIDE

    def test_installation_guide_install_keyword(self):
        assert classify("cprs_install.docx", "") == DocType.INSTALLATION_GUIDE

    def test_installation_guide_dibr_filename(self):
        assert classify("dg_5_3_1057_dibr.docx", "") == DocType.INSTALLATION_GUIDE

    def test_release_note_rn_suffix(self):
        assert classify("cprspatch_rn.docx", "") == DocType.RELEASE_NOTE

    def test_quick_ref_qr_suffix(self):
        assert classify("cprsqr.docx", "") == DocType.QUICK_REF

    def test_change_page_cp_suffix(self):
        assert classify("cprscp.docx", "") == DocType.CHANGE_PAGE

    def test_supplement_sp_suffix(self):
        assert classify("cprssp.docx", "") == DocType.SUPPLEMENT

    def test_case_insensitive(self):
        assert classify("CPRSGUITM.DOCX", "") == DocType.TECHNICAL_MANUAL


class TestClassifyByTitle:
    def test_title_technical_manual(self):
        assert classify("unknown.docx", "CPRS Technical Manual") == DocType.TECHNICAL_MANUAL

    def test_title_user_manual(self):
        assert classify("unknown.docx", "TIU User Manual") == DocType.USER_MANUAL

    def test_title_installation_guide(self):
        assert classify("unknown.docx", "CPRS Installation Guide") == DocType.INSTALLATION_GUIDE

    def test_title_release_notes(self):
        assert classify("unknown.docx", "Patch OR*3.0*350 Release Notes") == DocType.RELEASE_NOTE

    def test_title_quick_reference(self):
        assert classify("unknown.docx", "CPRS Quick Reference") == DocType.QUICK_REF

    def test_title_security_guide(self):
        assert classify("unknown.docx", "VistA Security Guide") == DocType.BASE_SECURITY

    def test_title_hl7_interface(self):
        assert classify("unknown.docx", "HL7 Interface Specification") == DocType.BASE_HL7


class TestClassifyFallback:
    def test_unknown_returns_unknown(self):
        assert classify("randomfile.docx", "Some Unknown Document") == DocType.UNKNOWN

    def test_filename_takes_priority_over_title(self):
        # filename says TM, title says UM — filename wins
        result = classify("cprsguitm.docx", "CPRS User Manual")
        assert result == DocType.TECHNICAL_MANUAL

    def test_empty_inputs_returns_unknown(self):
        assert classify("", "") == DocType.UNKNOWN


# ---------------------------------------------------------------------------
# Extended title rules — user-facing guide variants all map to USER_MANUAL
# ---------------------------------------------------------------------------


class TestUserFacingGuides:
    def test_user_guide(self):
        assert classify("bmsug.docx", "Bed Management Solution User Guide") == DocType.USER_MANUAL

    def test_users_guide(self):
        assert (
            classify("ifcap.docx", "IFCAP Control Point Clerk User's Guide") == DocType.USER_MANUAL
        )

    def test_adpac_guide(self):
        assert classify("qam.docx", "Clinical Monitoring System ADPAC Guide") == DocType.USER_MANUAL

    def test_managers_manual(self):
        assert classify("pxrm.docx", "Clinical Reminders Manager's Manual") == DocType.USER_MANUAL

    def test_administrators_guide(self):
        assert (
            classify("mag.docx", "VistA Imaging VIX Administrator's Guide") == DocType.USER_MANUAL
        )

    def test_admin_guide_short(self):
        assert classify("bms.docx", "Bed Management Solution Admin Guide") == DocType.USER_MANUAL

    def test_systems_management_guide(self):
        assert classify("xobv.docx", "VistALink Systems Management Guide") == DocType.USER_MANUAL

    def test_system_management_guide(self):
        assert classify("xm.docx", "MailMan System Management Guide") == DocType.USER_MANUAL


# ---------------------------------------------------------------------------
# Extended title rules — reference / quick-access docs map to QUICK_REF
# ---------------------------------------------------------------------------


class TestQuickRefVariants:
    def test_getting_started_guide(self):
        assert classify("xm.docx", "MailMan Getting Started Guide") == DocType.QUICK_REF

    def test_tutorial(self):
        assert classify("di.docx", "VA FileMan DDE Utility Tutorial") == DocType.QUICK_REF

    def test_quick_start_guide(self):
        assert classify("mag.docx", "VistARad Quick Start Guide") == DocType.QUICK_REF

    def test_shortcut_list(self):
        assert classify("mag.docx", "VistARad Shortcut List") == DocType.QUICK_REF

    def test_faq(self):
        assert classify("prea.docx", "AMPL Frequently Asked Questions Guide") == DocType.QUICK_REF

    def test_brochure(self):
        assert classify("pxrm.docx", "IHD Reminders Clinician Brochure") == DocType.QUICK_REF


# ---------------------------------------------------------------------------
# Extended title rules — supporting/reference material maps to SUPPLEMENT
# ---------------------------------------------------------------------------


class TestSupplementVariants:
    def test_glossary(self):
        assert (
            classify("edis.docx", "Emergency Dept Integration Software Glossary")
            == DocType.SUPPLEMENT
        )

    def test_troubleshooting_guide(self):
        assert classify("pecs.docx", "PECS Troubleshooting Guide") == DocType.SUPPLEMENT

    def test_trouble_shooting_guide_spaced(self):
        assert classify("pecs.docx", "PREC*6*516 TROUBLE SHOOTING GUIDE") == DocType.SUPPLEMENT

    def test_training_guide(self):
        assert classify("hinq.docx", "DVB*4*49 Training Guide") == DocType.SUPPLEMENT

    def test_workflow_doc(self):
        assert classify("capri.docx", "DVBA*2.7*150 Workflow - Audio") == DocType.SUPPLEMENT

    def test_production_operations_manual(self):
        assert classify("ciss.docx", "CISS Production Operations Manual") == DocType.SUPPLEMENT

    def test_prod_ops_manual_abbrev(self):
        assert (
            classify("prea.docx", "AMPL Production Operations Manual (POM)") == DocType.SUPPLEMENT
        )

    def test_checklist(self):
        assert (
            classify("pxrm.docx", "Airborne Hazard/Open Burn Pit CAC Checklist")
            == DocType.SUPPLEMENT
        )

    def test_flowchart(self):
        assert classify("pait.docx", "PAIT Version 1 Information Flowchart") == DocType.SUPPLEMENT


# ---------------------------------------------------------------------------
# Extended title rules — install/deploy variants map to INSTALLATION_GUIDE
# ---------------------------------------------------------------------------


class TestInstallGuideVariants:
    def test_deployment_guide(self):
        assert (
            classify("kaajee.docx", "KAAJEE 1.1.0 Deployment Guide") == DocType.INSTALLATION_GUIDE
        )

    def test_rollback_instructions(self):
        assert classify("kaajee.docx", "KAAJEE Rollback Instructions") == DocType.INSTALLATION_GUIDE

    def test_readme_file(self):
        assert classify("kaajee.docx", "KAAJEE 1.0.0 ReadMe File") == DocType.RELEASE_NOTE

    def test_readme_lowercase(self):
        assert classify("xwb.docx", "XWB*1.1*73 Readme File") == DocType.RELEASE_NOTE

    def test_installation_manual(self):
        assert (
            classify("mmrs.docx", "MRSA Program Tools Version 1 Installation Manual")
            == DocType.INSTALLATION_GUIDE
        )

    def test_conversion_guide(self):
        assert classify("md.docx", "MD*1*5 Conversion Guide") == DocType.INSTALLATION_GUIDE


# ---------------------------------------------------------------------------
# Extended title rules — developer/technical docs map to BASE_DEV
# ---------------------------------------------------------------------------


class TestDevDocVariants:
    def test_programmer_manual(self):
        assert classify("mpif.docx", "MPI/PD Version 1 VISTA Programmer Manual") == DocType.BASE_DEV

    def test_api_manual(self):
        assert classify("pso.docx", "API Manual - Pharmacy Reengineering") == DocType.BASE_DEV
