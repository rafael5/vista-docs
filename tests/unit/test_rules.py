"""
Unit tests for classify/rules.py — pure filename + title → DocType classification.
"""
import pytest

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
