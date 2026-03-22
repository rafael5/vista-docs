"""
Unit tests for crawl/parser.py — pure HTML → catalog record parsing.

All tests use static fixture HTML; no network, no filesystem I/O.
"""
import pytest

from vista_docs.crawl.parser import parse_sections, parse_application_page


# ---------------------------------------------------------------------------
# Minimal HTML fixtures (inline — full fixtures live in tests/fixtures/html/)
# ---------------------------------------------------------------------------

SECTION_LISTING_HTML = """
<html><body>
<div class="vdl-content">
  <h2>Clinical</h2>
  <ul>
    <li><a href="/vdl/application.asp?appid=100">CPRS (OR*3.0)</a></li>
    <li><a href="/vdl/application.asp?appid=101">TIU (TIU*1.0)</a></li>
  </ul>
  <h2>Infrastructure</h2>
  <ul>
    <li><a href="/vdl/application.asp?appid=200">HL7 (HL*1.6)</a></li>
  </ul>
</div>
</body></html>
"""

APP_PAGE_HTML = """
<html><body>
<h1>CPRS (OR*3.0)</h1>
<table class="vdl-table">
  <tr>
    <td><a href="/vdl/docs/cprsguitm.docx">CPRS Technical Manual</a></td>
    <td>03/2024</td>
  </tr>
  <tr>
    <td><a href="/vdl/docs/cprsinstall.docx">CPRS Installation Guide</a></td>
    <td>01/2023</td>
  </tr>
</table>
</body></html>
"""


# ---------------------------------------------------------------------------
# parse_sections
# ---------------------------------------------------------------------------

class TestParseSections:
    def test_returns_list(self):
        sections = parse_sections(SECTION_LISTING_HTML)
        assert isinstance(sections, list)

    def test_section_count(self):
        sections = parse_sections(SECTION_LISTING_HTML)
        assert len(sections) == 2

    def test_section_names(self):
        sections = parse_sections(SECTION_LISTING_HTML)
        names = [s.name for s in sections]
        assert "Clinical" in names
        assert "Infrastructure" in names

    def test_applications_under_section(self):
        sections = parse_sections(SECTION_LISTING_HTML)
        clinical = next(s for s in sections if s.name == "Clinical")
        assert len(clinical.applications) == 2

    def test_application_name(self):
        sections = parse_sections(SECTION_LISTING_HTML)
        clinical = next(s for s in sections if s.name == "Clinical")
        cprs = next(a for a in clinical.applications if "CPRS" in a.name)
        assert cprs.name == "CPRS (OR*3.0)"

    def test_application_url(self):
        sections = parse_sections(SECTION_LISTING_HTML)
        clinical = next(s for s in sections if s.name == "Clinical")
        cprs = next(a for a in clinical.applications if "CPRS" in a.name)
        assert "appid=100" in cprs.url

    def test_application_package_id_extracted(self):
        sections = parse_sections(SECTION_LISTING_HTML)
        clinical = next(s for s in sections if s.name == "Clinical")
        cprs = next(a for a in clinical.applications if "CPRS" in a.name)
        assert cprs.package_id == "OR*3.0"

    def test_application_app_code_extracted(self):
        sections = parse_sections(SECTION_LISTING_HTML)
        clinical = next(s for s in sections if s.name == "Clinical")
        cprs = next(a for a in clinical.applications if "CPRS" in a.name)
        assert cprs.app_code == "OR"

    def test_empty_html_returns_empty_list(self):
        assert parse_sections("<html><body></body></html>") == []

    def test_infrastructure_section_one_app(self):
        sections = parse_sections(SECTION_LISTING_HTML)
        infra = next(s for s in sections if s.name == "Infrastructure")
        assert len(infra.applications) == 1


# ---------------------------------------------------------------------------
# parse_application_page
# ---------------------------------------------------------------------------

class TestParseApplicationPage:
    def test_returns_list(self):
        docs = parse_application_page(APP_PAGE_HTML)
        assert isinstance(docs, list)

    def test_document_count(self):
        docs = parse_application_page(APP_PAGE_HTML)
        assert len(docs) == 2

    def test_document_title(self):
        docs = parse_application_page(APP_PAGE_HTML)
        titles = [d.title for d in docs]
        assert "CPRS Technical Manual" in titles

    def test_document_url(self):
        docs = parse_application_page(APP_PAGE_HTML)
        tm = next(d for d in docs if "Technical" in d.title)
        assert "cprsguitm.docx" in tm.url

    def test_document_date(self):
        docs = parse_application_page(APP_PAGE_HTML)
        tm = next(d for d in docs if "Technical" in d.title)
        assert tm.file_date == "03/2024"

    def test_empty_table_returns_empty_list(self):
        html = "<html><body><h1>App</h1><table class='vdl-table'></table></body></html>"
        assert parse_application_page(html) == []
