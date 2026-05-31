"""
Unit tests for enrich/inventory_fields.py

build_inventory_index(rows) — dedup PDF/DOCX pairs, exclude noise rows
fields_for_doc(index, app_code, title) — return merged frontmatter fields
"""

from vista_docs.enrich.inventory_fields import build_inventory_index, fields_for_doc

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


def _row(**kwargs) -> dict:
    """Build a minimal enriched-inventory row, with sensible defaults."""
    defaults = {
        "app_name_abbrev": "PSO",
        "app_name_full": "Outpatient Pharmacy",
        "app_status": "active",
        "section_code": "CLI",
        "doc_title": "PSO User Manual",
        "doc_format": "docx",
        "doc_code": "UM",
        "doc_label": "User Manual",
        "doc_layer": "anchor",
        "doc_subject": "Nurse",
        "group_key": "PSO:PSO:7.0",
        "pkg_ns": "PSO",
        "patch_id": "PSO*7.0",
        "patch_ver": "7.0",
        "app_url": "https://www.va.gov/vdl/application.asp?appid=41",
        "doc_url": "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpt/pso_um.docx",
        "companion_url": "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpt/pso_um.pdf",
        "noise_type": "",
    }
    defaults.update(kwargs)
    return defaults


# ---------------------------------------------------------------------------
# build_inventory_index
# ---------------------------------------------------------------------------


def test_build_inventory_index_empty():
    assert build_inventory_index([]) == {}


def test_build_inventory_index_single_docx():
    rows = [_row()]
    idx = build_inventory_index(rows)
    assert ("PSO", "PSO User Manual") in idx


def test_build_inventory_index_excludes_noise():
    rows = [_row(noise_type="vba_form"), _row(noise_type="va_ref")]
    assert build_inventory_index(rows) == {}


def test_build_inventory_index_dedup_prefers_docx():
    """When both PDF and DOCX rows exist, the DOCX row should be kept."""
    docx_row = _row(doc_format="docx", doc_url="https://example.com/file.docx")
    pdf_row = _row(doc_format="pdf", doc_url="https://example.com/file.pdf")
    idx = build_inventory_index([pdf_row, docx_row])
    result = idx[("PSO", "PSO User Manual")]
    assert result["doc_url"].endswith(".docx")


def test_build_inventory_index_dedup_pdf_only():
    """When only a PDF row exists, it is still indexed."""
    pdf_row = _row(doc_format="pdf", doc_url="https://example.com/file.pdf")
    idx = build_inventory_index([pdf_row])
    result = idx[("PSO", "PSO User Manual")]
    assert result["doc_url"].endswith(".pdf")


def test_build_inventory_index_multiple_apps():
    rows = [
        _row(app_name_abbrev="PSO", doc_title="Doc A"),
        _row(app_name_abbrev="ADT", doc_title="Doc B"),
    ]
    idx = build_inventory_index(rows)
    assert ("PSO", "Doc A") in idx
    assert ("ADT", "Doc B") in idx


# ---------------------------------------------------------------------------
# fields_for_doc
# ---------------------------------------------------------------------------


def test_fields_for_doc_not_found():
    idx = build_inventory_index([_row()])
    assert fields_for_doc(idx, "PSO", "Nonexistent Title") is None


def test_fields_for_doc_wrong_app():
    idx = build_inventory_index([_row()])
    assert fields_for_doc(idx, "ADT", "PSO User Manual") is None


def test_fields_for_doc_returns_section():
    idx = build_inventory_index([_row(section_code="CLI")])
    result = fields_for_doc(idx, "PSO", "PSO User Manual")
    assert result is not None
    assert result["section"] == "CLI"


def test_fields_for_doc_returns_app_name():
    idx = build_inventory_index([_row()])
    result = fields_for_doc(idx, "PSO", "PSO User Manual")
    assert result["app_name"] == "Outpatient Pharmacy"


def test_fields_for_doc_returns_app_status():
    idx = build_inventory_index([_row(app_status="archive")])
    result = fields_for_doc(idx, "PSO", "PSO User Manual")
    assert result["app_status"] == "archive"


def test_fields_for_doc_includes_doc_type_when_doc_code_set():
    idx = build_inventory_index([_row(doc_code="UM")])
    result = fields_for_doc(idx, "PSO", "PSO User Manual")
    assert result["doc_type"] == "UM"


def test_fields_for_doc_omits_doc_type_when_doc_code_empty():
    """Don't overwrite existing classify-derived doc_type with empty string."""
    idx = build_inventory_index([_row(doc_code="")])
    result = fields_for_doc(idx, "PSO", "PSO User Manual")
    assert "doc_type" not in result


def test_fields_for_doc_returns_doc_label():
    idx = build_inventory_index([_row(doc_label="User Manual")])
    result = fields_for_doc(idx, "PSO", "PSO User Manual")
    assert result["doc_label"] == "User Manual"


def test_fields_for_doc_returns_doc_layer():
    idx = build_inventory_index([_row(doc_layer="patch")])
    result = fields_for_doc(idx, "PSO", "PSO User Manual")
    assert result["doc_layer"] == "patch"


def test_fields_for_doc_returns_group_key():
    idx = build_inventory_index([_row(group_key="PSO:PSO:7.0")])
    result = fields_for_doc(idx, "PSO", "PSO User Manual")
    assert result["group_key"] == "PSO:PSO:7.0"


def test_fields_for_doc_returns_pkg_ns_and_patch_fields():
    idx = build_inventory_index([_row(pkg_ns="PSO", patch_id="PSO*7.0*599", patch_ver="7.0")])
    result = fields_for_doc(idx, "PSO", "PSO User Manual")
    assert result["pkg_ns"] == "PSO"
    assert result["patch_id"] == "PSO*7.0*599"
    assert result["patch_ver"] == "7.0"


def test_fields_for_doc_returns_doc_subject():
    idx = build_inventory_index([_row(doc_subject="Nurse")])
    result = fields_for_doc(idx, "PSO", "PSO User Manual")
    assert result["doc_subject"] == "Nurse"


def test_fields_for_doc_returns_app_url():
    idx = build_inventory_index([_row(app_url="https://www.va.gov/vdl/application.asp?appid=41")])
    result = fields_for_doc(idx, "PSO", "PSO User Manual")
    assert result["app_url"] == "https://www.va.gov/vdl/application.asp?appid=41"


def test_fields_for_doc_empty_optional_fields_are_empty_string():
    """Empty optional fields (pkg_ns, patch_id, etc.) stay as empty strings."""
    idx = build_inventory_index(
        [_row(pkg_ns="", patch_id="", patch_ver="", doc_subject="", group_key="")]
    )
    result = fields_for_doc(idx, "PSO", "PSO User Manual")
    assert result["pkg_ns"] == ""
    assert result["patch_id"] == ""
    assert result["patch_ver"] == ""
    assert result["doc_subject"] == ""
    assert result["group_key"] == ""


# ---------------------------------------------------------------------------
# app_fields_for_code — app-level backfill for docs with no title match
# ---------------------------------------------------------------------------


class TestAppFieldsForCode:
    def test_returns_app_level_fields_for_known_code(self):
        from vista_docs.enrich.inventory_fields import app_fields_for_code

        index = build_inventory_index(
            [
                _row(
                    app_name_abbrev="PRCA",
                    app_name_full="Accounts Receivable (AR)",
                    section_code="FIN",
                    app_status="active",
                    doc_title="PRCA TM",
                    pkg_ns="PRCA",
                    app_url="https://va.gov/vdl/application.asp?appid=9",
                ),
            ]
        )
        fields = app_fields_for_code(index, "PRCA")
        assert fields is not None
        assert fields["section"] == "FIN"
        assert fields["app_name"] == "Accounts Receivable (AR)"
        assert fields["app_status"] == "active"
        assert fields["pkg_ns"] == "PRCA"
        assert fields["app_url"].endswith("appid=9")

    def test_returns_none_for_unknown_code(self):
        from vista_docs.enrich.inventory_fields import app_fields_for_code

        index = build_inventory_index([_row(app_name_abbrev="PSO")])
        assert app_fields_for_code(index, "NOPE") is None

    def test_does_not_include_doc_level_fields(self):
        from vista_docs.enrich.inventory_fields import app_fields_for_code

        index = build_inventory_index([_row(app_name_abbrev="PSO")])
        fields = app_fields_for_code(index, "PSO")
        # App-level only — never guesses a doc_label/patch_id from an unrelated row.
        assert "doc_label" not in fields
        assert "patch_id" not in fields
