"""
Unit tests for crawl/parser.py — pure HTML → catalog record parsing.

HTML fixtures mirror the real VDL structure (section.asp / application.asp links,
table-based document rows). No network, no filesystem.
"""

from vista_docs.crawl.parser import (
    _extract_app_code,
    _parse_app_name,
    parse_application_page,
    parse_index,
    parse_section_page,
)
from vista_docs.models.catalog import Application, Document, Section

# ---------------------------------------------------------------------------
# Fixtures (minimal but structurally correct)
# ---------------------------------------------------------------------------

INDEX_HTML = """
<html><body>
<a href="section.asp?secid=1">Clinical</a>
<a href="section.asp?secid=2">Infrastructure</a>
<a href="section.asp?secid=1">Clinical</a>
<a href="/other/page.html">Other link</a>
</body></html>
"""

SECTION_HTML = """
<html><body>
<a href="application.asp?appid=55">Admission Discharge Transfer (ADT)</a>
<a href="application.asp?appid=56">CPRS: Problem List (GMPL) - ARCHIVE</a>
<a href="application.asp?appid=57">Social Work (SOW) - DECOMMISSIONED JUL 2020</a>
<a href="application.asp?appid=55">Admission Discharge Transfer (ADT)</a>
<a href="/other/">Not an app</a>
</body></html>
"""

APP_HTML = """
<html><body>
<table>
  <tr>
    <td>DG*5.3*1057 DIBR Guide</td>
    <td><a href="/vdl/documents/Clinical/ADT/dg_5_3_1057_dibr.docx">DOCX</a></td>
    <td>03/15/2024</td>
  </tr>
  <tr>
    <td>DG*5.3*1057 DIBR Guide</td>
    <td><a href="/vdl/documents/Clinical/ADT/dg_5_3_1057_dibr.pdf">PDF</a></td>
    <td>03/15/2024</td>
  </tr>
  <tr>
    <td colspan="3">Header row with no file link</td>
  </tr>
</table>
</body></html>
"""

APP_HTML_NO_TABLE = """
<html><body>
<h1>App with no table</h1>
<a href="/vdl/documents/OR/cprsguitm.docx">CPRS Technical Manual</a>
<a href="/vdl/documents/OR/cprsguitm.pdf">CPRS Technical Manual PDF</a>
</body></html>
"""


# ---------------------------------------------------------------------------
# _parse_app_name (internal helper)
# ---------------------------------------------------------------------------


class TestParseAppName:
    def test_active_app(self):
        name, status, date = _parse_app_name("Nursing (NUR)")
        assert name == "Nursing (NUR)"
        assert status == "active"
        assert date == ""

    def test_archive_app(self):
        name, status, date = _parse_app_name("CPRS: Problem List (GMPL) - ARCHIVE")
        assert status == "archive"
        assert "ARCHIVE" not in name

    def test_decommissioned_with_date(self):
        name, status, date = _parse_app_name("Social Work (SOW) - DECOMMISSIONED JUL 2020")
        assert status == "decommissioned"
        assert date == "JUL 2020"
        assert "DECOMMISSIONED" not in name


class TestExtractAppCode:
    def test_simple_code(self):
        assert _extract_app_code("Nursing (NUR)") == "NUR"

    def test_complex_name(self):
        assert _extract_app_code("Admission Discharge Transfer (ADT)") == "ADT"

    def test_no_code(self):
        assert _extract_app_code("No parentheses here") == ""


# ---------------------------------------------------------------------------
# parse_index
# ---------------------------------------------------------------------------


class TestParseIndex:
    def test_returns_sections(self):
        sections = parse_index(INDEX_HTML)
        assert isinstance(sections, list)
        assert all(isinstance(s, Section) for s in sections)

    def test_deduplicates_by_secid(self):
        sections = parse_index(INDEX_HTML)
        assert len(sections) == 2  # "Clinical" appears twice in fixture

    def test_section_names(self):
        sections = parse_index(INDEX_HTML)
        names = {s.name for s in sections}
        assert "Clinical" in names
        assert "Infrastructure" in names

    def test_section_url_contains_secid(self):
        sections = parse_index(INDEX_HTML)
        clinical = next(s for s in sections if s.name == "Clinical")
        assert "secid=1" in clinical.url

    def test_ignores_non_section_links(self):
        sections = parse_index(INDEX_HTML)
        urls = [s.url for s in sections]
        assert not any("/other/" in u for u in urls)

    def test_empty_html_returns_empty(self):
        assert parse_index("<html><body></body></html>") == []


# ---------------------------------------------------------------------------
# parse_section_page
# ---------------------------------------------------------------------------


class TestParseSectionPage:
    def test_returns_applications(self):
        apps = parse_section_page(SECTION_HTML)
        assert isinstance(apps, list)
        assert all(isinstance(a, Application) for a in apps)

    def test_deduplicates_by_appid(self):
        apps = parse_section_page(SECTION_HTML)
        assert len(apps) == 3  # ADT appears twice; deduplicated

    def test_app_name_cleaned(self):
        apps = parse_section_page(SECTION_HTML)
        adt = next(a for a in apps if "ADT" in a.app_code)
        assert adt.name == "Admission Discharge Transfer (ADT)"

    def test_app_code_extracted(self):
        apps = parse_section_page(SECTION_HTML)
        adt = next(a for a in apps if "Admission" in a.name)
        assert adt.app_code == "ADT"

    def test_archive_status(self):
        apps = parse_section_page(SECTION_HTML)
        gmpl = next(a for a in apps if "GMPL" in a.name)
        assert gmpl.status == "archive"

    def test_decommissioned_status_and_date(self):
        apps = parse_section_page(SECTION_HTML)
        sow = next(a for a in apps if "SOW" in a.name)
        assert sow.status == "decommissioned"
        assert sow.decommission_date == "JUL 2020"

    def test_app_url_contains_appid(self):
        apps = parse_section_page(SECTION_HTML)
        adt = next(a for a in apps if "ADT" in a.app_code)
        assert "appid=55" in adt.url

    def test_ignores_non_app_links(self):
        apps = parse_section_page(SECTION_HTML)
        assert all("application.asp" in a.url for a in apps)

    def test_empty_html_returns_empty(self):
        assert parse_section_page("<html><body></body></html>") == []


# ---------------------------------------------------------------------------
# parse_application_page
# ---------------------------------------------------------------------------


class TestParseApplicationPage:
    def test_returns_documents(self):
        docs = parse_application_page(APP_HTML)
        assert isinstance(docs, list)
        assert all(isinstance(d, Document) for d in docs)

    def test_finds_docx_and_pdf(self):
        docs = parse_application_page(APP_HTML)
        exts = {d.file_ext for d in docs}
        assert ".docx" in exts
        assert ".pdf" in exts

    def test_document_title(self):
        docs = parse_application_page(APP_HTML)
        titles = {d.title for d in docs}
        assert "DG*5.3*1057 DIBR Guide" in titles

    def test_document_filename(self):
        docs = parse_application_page(APP_HTML)
        filenames = {d.filename for d in docs}
        assert "dg_5_3_1057_dibr.docx" in filenames

    def test_document_date_extracted(self):
        docs = parse_application_page(APP_HTML)
        docx_doc = next(d for d in docs if d.file_ext == ".docx")
        assert "2024" in docx_doc.file_date

    def test_doc_type_label(self):
        docs = parse_application_page(APP_HTML)
        docx_doc = next(d for d in docs if d.file_ext == ".docx")
        assert docx_doc.doc_type_label == "DOCX"

    def test_no_table_fallback_to_link_scan(self):
        docs = parse_application_page(APP_HTML_NO_TABLE)
        assert len(docs) == 2
        filenames = {d.filename for d in docs}
        assert "cprsguitm.docx" in filenames

    def test_empty_html_returns_empty(self):
        assert parse_application_page("<html><body></body></html>") == []
