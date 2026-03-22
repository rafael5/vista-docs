"""
Unit tests for manifest/builder.py — pure inventory CSV rows → ManifestEntry list.

Key behaviour: DOCX+PDF row-pairs for the same document are collapsed into
a single ManifestEntry with both docx_url and pdf_url populated.
"""

from vista_docs.manifest.builder import build_entries_from_rows
from vista_docs.models.manifest import DocType, FetchStatus, ManifestEntry

# ---------------------------------------------------------------------------
# Minimal row fixtures (match real CSV column names)
# ---------------------------------------------------------------------------

DOCX_ROW = {
    "section_name": "Clinical",
    "app_name": "Admission Discharge Transfer (ADT)",
    "app_code": "ADT",
    "app_status": "active",
    "decommission_date": "",
    "doc_title": "DG*5.3*1057 DIBR Guide",
    "doc_type": "DOCX",
    "filename": "dg_5_3_1057_dibr.docx",
    "file_ext": ".docx",
    "doc_date": "",
    "doc_url": "https://va.gov/documents/Clinical/ADT/dg_5_3_1057_dibr.docx",
    "app_url": "https://va.gov/vdl/application.asp?appid=55",
}

PDF_ROW = {
    **DOCX_ROW,
    "doc_type": "PDF",
    "filename": "dg_5_3_1057_dibr.pdf",
    "file_ext": ".pdf",
    "doc_url": "https://va.gov/documents/Clinical/ADT/dg_5_3_1057_dibr.pdf",
}

DOCX_ROW_2 = {
    **DOCX_ROW,
    "doc_title": "DG*5.3*1064 Release Notes",
    "filename": "dg_5_3_p1064_rn.docx",
    "doc_url": "https://va.gov/documents/Clinical/ADT/dg_5_3_p1064_rn.docx",
}

PDF_ROW_2 = {
    **DOCX_ROW_2,
    "doc_type": "PDF",
    "filename": "dg_5_3_p1064_rn.pdf",
    "file_ext": ".pdf",
    "doc_url": "https://va.gov/documents/Clinical/ADT/dg_5_3_p1064_rn.pdf",
}

DOCX_ONLY_ROW = {
    **DOCX_ROW,
    "doc_title": "DOCX Only Document",
    "filename": "docx_only.docx",
    "doc_url": "https://va.gov/documents/Clinical/ADT/docx_only.docx",
}

TIU_DOCX_ROW = {
    "section_name": "Clinical",
    "app_name": "Text Integration Utilities (TIU)",
    "app_code": "TIU",
    "app_status": "active",
    "decommission_date": "",
    "doc_title": "TIU Technical Manual",
    "doc_type": "DOCX",
    "filename": "tiutm.docx",
    "file_ext": ".docx",
    "doc_date": "",
    "doc_url": "https://va.gov/documents/Clinical/TIU/tiutm.docx",
    "app_url": "https://va.gov/vdl/application.asp?appid=62",
}


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


class TestBuildEntriesFromRows:
    def test_returns_list_of_manifest_entries(self):
        entries = build_entries_from_rows([DOCX_ROW])
        assert isinstance(entries, list)
        assert all(isinstance(e, ManifestEntry) for e in entries)

    def test_collapses_docx_pdf_pair_into_one_entry(self):
        entries = build_entries_from_rows([DOCX_ROW, PDF_ROW])
        assert len(entries) == 1

    def test_collapsed_entry_has_both_urls(self):
        entries = build_entries_from_rows([DOCX_ROW, PDF_ROW])
        e = entries[0]
        assert e.docx_url.endswith(".docx")
        assert e.pdf_url.endswith(".pdf")

    def test_two_pairs_produce_two_entries(self):
        entries = build_entries_from_rows([DOCX_ROW, PDF_ROW, DOCX_ROW_2, PDF_ROW_2])
        assert len(entries) == 2

    def test_docx_only_has_empty_pdf_url(self):
        entries = build_entries_from_rows([DOCX_ONLY_ROW])
        assert entries[0].docx_url != ""
        assert entries[0].pdf_url == ""

    def test_app_code_set(self):
        entries = build_entries_from_rows([DOCX_ROW])
        assert entries[0].app_code == "ADT"

    def test_doc_title_set(self):
        entries = build_entries_from_rows([DOCX_ROW])
        assert entries[0].doc_title == "DG*5.3*1057 DIBR Guide"

    def test_fetch_status_starts_pending(self):
        entries = build_entries_from_rows([DOCX_ROW])
        assert entries[0].fetch_status == FetchStatus.PENDING

    def test_doc_type_classified(self):
        entries = build_entries_from_rows([DOCX_ROW])
        assert entries[0].doc_type != DocType.UNKNOWN

    def test_output_filename_generated(self):
        entries = build_entries_from_rows([DOCX_ROW])
        assert entries[0].output_filename.endswith(".md")
        assert entries[0].output_filename != ""

    def test_different_packages_separate_entries(self):
        entries = build_entries_from_rows([DOCX_ROW, TIU_DOCX_ROW])
        assert len(entries) == 2
        codes = {e.app_code for e in entries}
        assert "ADT" in codes
        assert "TIU" in codes

    def test_empty_rows_returns_empty(self):
        assert build_entries_from_rows([]) == []

    def test_pdf_row_before_docx_still_collapses(self):
        entries = build_entries_from_rows([PDF_ROW, DOCX_ROW])
        assert len(entries) == 1
        assert entries[0].docx_url.endswith(".docx")
        assert entries[0].pdf_url.endswith(".pdf")

    def test_skips_decommissioned_apps(self):
        decomm_row = {**DOCX_ROW, "app_status": "decommissioned"}
        entries = build_entries_from_rows([decomm_row])
        assert len(entries) == 0

    def test_includes_archive_apps(self):
        archive_row = {**DOCX_ROW, "app_status": "archive"}
        entries = build_entries_from_rows([archive_row])
        assert len(entries) == 1
