"""
Pure HTML → catalog record parsing.

No I/O. Takes raw HTML strings, returns dataclasses.
The real HTML structure is approximated here — tests use fixture files
in tests/fixtures/html/ that capture actual VDL pages.
"""
from __future__ import annotations

import re
from html.parser import HTMLParser

from vista_docs.models.catalog import Application, Document, Section


# ---------------------------------------------------------------------------
# Package ID extraction
# ---------------------------------------------------------------------------

_PKG_RE = re.compile(r"\(([A-Z]+\*[\d.]+)\)")
_CODE_RE = re.compile(r"^([A-Z]+)")


def _extract_package_id(text: str) -> str:
    """Extract package_id like 'OR*3.0' from 'CPRS (OR*3.0)'."""
    m = _PKG_RE.search(text)
    return m.group(1) if m else ""


def _extract_app_code(package_id: str) -> str:
    """Extract namespace prefix 'OR' from 'OR*3.0'."""
    m = _CODE_RE.match(package_id)
    return m.group(1) if m else ""


# ---------------------------------------------------------------------------
# Section listing parser
# ---------------------------------------------------------------------------

class _SectionParser(HTMLParser):
    """
    Parses the VDL index page that lists sections and their applications.

    Expected structure (simplified):
      <h2>Section Name</h2>
      <ul>
        <li><a href="/vdl/application.asp?appid=N">App Name (PKG*1.0)</a></li>
        ...
      </ul>
    """

    def __init__(self) -> None:
        super().__init__()
        self.sections: list[Section] = []
        self._current_section: Section | None = None
        self._in_h2 = False
        self._in_li_a = False
        self._current_link: str = ""
        self._current_text: str = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "h2":
            self._in_h2 = True
            self._current_text = ""
        elif tag == "a" and self._current_section is not None:
            href = dict(attrs).get("href", "") or ""
            if "application" in href or "appid" in href:
                self._in_li_a = True
                self._current_link = href
                self._current_text = ""

    def handle_endtag(self, tag: str) -> None:
        if tag == "h2":
            self._in_h2 = False
            name = self._current_text.strip()
            if name:
                section = Section(name=name, url="")
                self.sections.append(section)
                self._current_section = section

        elif tag == "a" and self._in_li_a:
            self._in_li_a = False
            text = self._current_text.strip()
            pkg_id = _extract_package_id(text)
            app = Application(
                name=text,
                package_id=pkg_id,
                app_code=_extract_app_code(pkg_id),
                url=self._current_link,
            )
            if self._current_section is not None:
                self._current_section.applications.append(app)

    def handle_data(self, data: str) -> None:
        if self._in_h2 or self._in_li_a:
            self._current_text += data


def parse_sections(html: str) -> list[Section]:
    """Parse VDL index HTML into a list of Sections with Applications."""
    parser = _SectionParser()
    parser.feed(html)
    return [s for s in parser.sections if s.applications]


# ---------------------------------------------------------------------------
# Application page parser
# ---------------------------------------------------------------------------

class _AppPageParser(HTMLParser):
    """
    Parses a VDL application page that lists documents in a table.

    Expected structure (simplified):
      <table class="vdl-table">
        <tr>
          <td><a href="/vdl/docs/file.docx">Document Title</a></td>
          <td>MM/YYYY</td>
        </tr>
        ...
      </table>
    """

    def __init__(self) -> None:
        super().__init__()
        self.documents: list[Document] = []
        self._in_vdl_table = False
        self._in_td = False
        self._td_index = 0          # 0-based column index within current <tr>
        self._current_url = ""
        self._current_title = ""
        self._current_date = ""
        self._in_doc_link = False
        self._current_text = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_dict = dict(attrs)
        if tag == "table":
            cls = attr_dict.get("class", "") or ""
            if "vdl-table" in cls:
                self._in_vdl_table = True
        elif tag == "tr" and self._in_vdl_table:
            self._td_index = 0
            self._current_url = ""
            self._current_title = ""
            self._current_date = ""
        elif tag == "td" and self._in_vdl_table:
            self._in_td = True
            self._current_text = ""
        elif tag == "a" and self._in_td and self._td_index == 0:
            href = attr_dict.get("href", "") or ""
            ext = href.rsplit(".", 1)[-1].lower() if "." in href else ""
            if ext in ("docx", "pdf", "doc"):
                self._in_doc_link = True
                self._current_url = href
                self._current_text = ""

    def handle_endtag(self, tag: str) -> None:
        if tag == "table":
            self._in_vdl_table = False
        elif tag == "a" and self._in_doc_link:
            self._in_doc_link = False
            self._current_title = self._current_text.strip()
        elif tag == "td" and self._in_vdl_table:
            if self._td_index == 1:
                self._current_date = self._current_text.strip()
            self._td_index += 1
            self._in_td = False
        elif tag == "tr" and self._in_vdl_table:
            if self._current_url and self._current_title:
                self.documents.append(
                    Document(
                        title=self._current_title,
                        url=self._current_url,
                        file_date=self._current_date,
                    )
                )

    def handle_data(self, data: str) -> None:
        if self._in_doc_link or (self._in_td and self._td_index == 1):
            self._current_text += data


def parse_application_page(html: str) -> list[Document]:
    """Parse a VDL application page into a list of Documents."""
    parser = _AppPageParser()
    parser.feed(html)
    return parser.documents
