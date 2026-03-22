"""
Pure HTML → catalog record parsing for the VA VDL.

No I/O. Takes raw HTML strings, returns dataclasses.

VDL HTML is 3-level:
  1. Index page (va.gov/vdl/) — links with "section.asp" → Section names + URLs
  2. Section page            — links with "application.asp" → Application names + URLs
  3. Application page        — tables with file links → Document records

All functions are pure: string in, dataclass list out.
"""

from __future__ import annotations

import re
from urllib.parse import parse_qs, urljoin, urlparse

from bs4 import BeautifulSoup

from vista_docs.models.catalog import Application, Document, Section

_VDL_BASE = "https://www.va.gov/vdl/"

# ---------------------------------------------------------------------------
# Application status extraction
# ---------------------------------------------------------------------------

_ARCHIVE_RE = re.compile(r"\s*-\s*ARCHIVE\s*$", re.I)
_DECOMM_RE = re.compile(r"\s*-\s*DECOMMISSIONED\s*(.*?)\s*$", re.I)
_APP_CODE_RE = re.compile(r"\(([A-Z0-9+/ ]{1,20})\)\s*$")


def _parse_app_name(raw: str) -> tuple[str, str, str]:
    """
    Extract (clean_name, status, decommission_date) from a raw app name string.

    Examples:
      'CPRS: Problem List (GMPL) - ARCHIVE'      → ('CPRS...', 'archive', '')
      'Social Work (SOW) - DECOMMISSIONED JUL 2020' → ('Social Work (SOW)', 'decommissioned', 'JUL 2020')
      'Nursing (NUR)'                             → ('Nursing (NUR)', 'active', '')
    """
    m = _ARCHIVE_RE.search(raw)
    if m:
        return raw[: m.start()].strip(), "archive", ""
    m = _DECOMM_RE.search(raw)
    if m:
        return raw[: m.start()].strip(), "decommissioned", m.group(1).strip()
    return raw.strip(), "active", ""


def _extract_app_code(name: str) -> str:
    """Extract 'NUR' from 'Nursing (NUR)'."""
    m = _APP_CODE_RE.search(name)
    return m.group(1).strip() if m else ""


# ---------------------------------------------------------------------------
# Level 1: parse VDL index page → Section list
# ---------------------------------------------------------------------------


def parse_index(html: str, base_url: str = _VDL_BASE) -> list[Section]:
    """
    Parse the VDL home page and return a list of Sections.

    Sections are found as <a href="...section.asp?secid=N">Name</a> links.
    Applications list is not populated here — call parse_section_page() next.
    """
    soup = BeautifulSoup(html, "html.parser")
    seen: set[str] = set()
    sections: list[Section] = []

    for a in soup.find_all("a", href=True):
        href: str = str(a["href"])
        if "section.asp" not in href:
            continue
        full_url = urljoin(base_url, href)
        params = parse_qs(urlparse(full_url).query)
        sec_id = params.get("secid", [""])[0]
        if sec_id in seen:
            continue
        seen.add(sec_id)
        name = a.get_text(strip=True)
        if name:
            sections.append(Section(name=name, url=full_url))

    return sections


# ---------------------------------------------------------------------------
# Level 2: parse section page → Application list
# ---------------------------------------------------------------------------


def parse_section_page(
    html: str,
    section_id: str = "",
    section_name: str = "",
    base_url: str = _VDL_BASE,
) -> list[Application]:
    """
    Parse a VDL section page and return a list of Applications.

    Applications are found as <a href="...application.asp?appid=N">Name</a> links.
    App name is parsed for status suffix (ARCHIVE / DECOMMISSIONED).
    """
    soup = BeautifulSoup(html, "html.parser")
    seen: set[str] = set()
    apps: list[Application] = []

    for a in soup.find_all("a", href=True):
        href: str = str(a["href"])
        if "application.asp" not in href:
            continue
        full_url = urljoin(base_url, href)
        params = parse_qs(urlparse(full_url).query)
        app_id = params.get("appid", [""])[0]
        if app_id in seen:
            continue
        seen.add(app_id)

        raw_name = a.get_text(strip=True)
        clean_name, status, decomm_date = _parse_app_name(raw_name)
        app_code = _extract_app_code(clean_name)

        apps.append(
            Application(
                name=clean_name,
                package_id="",  # derived later during manifest build
                app_code=app_code,
                url=full_url,
                status=status,
                decommission_date=decomm_date,
                documents=[],
            )
        )

    return apps


# ---------------------------------------------------------------------------
# Level 3: parse application page → Document list
# ---------------------------------------------------------------------------

_FILE_EXTS = {".pdf", ".doc", ".docx", ".zip", ".txt"}
_DATE_RE = re.compile(
    r"(\d{1,2}/\d{1,2}/\d{4}|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*\s+\d{4})",
    re.I,
)


def parse_application_page(html: str, base_url: str = "https://www.va.gov/") -> list[Document]:
    """
    Parse a VDL application page and return a list of Documents.

    Documents are found in tables — each row may have a PDF/DOCX file link.
    Falls back to a broader link scan if no table-based docs are found.
    """
    soup = BeautifulSoup(html, "html.parser")
    docs: list[Document] = []

    # Primary: table-based scan
    for table in soup.find_all("table"):
        for row in table.find_all("tr"):
            cells = row.find_all(["td", "th"])
            if len(cells) < 2:
                continue
            cell_texts = [c.get_text(strip=True) for c in cells]

            file_links = [
                a
                for a in row.find_all("a", href=True)
                if any(str(a["href"]).lower().endswith(ext) for ext in _FILE_EXTS)
            ]

            for a in file_links:
                href: str = str(a["href"])
                full_url = urljoin(base_url, href)
                filename = urlparse(href).path.rsplit("/", 1)[-1]
                ext = "." + filename.rsplit(".", 1)[-1].lower() if "." in filename else ""

                link_text = a.get_text(strip=True)
                # Real VDL: link text is the format label ("DOCX"/"PDF"),
                # actual title is in the first non-link cell.
                # Fallback: if link text looks like a title, use it directly.
                if link_text.upper() in ("DOCX", "PDF", "DOC", "ZIP", "TXT", "WORD"):
                    doc_type = link_text.upper()
                    doc_title = next(
                        (
                            t
                            for t in cell_texts
                            if t and t.upper() not in ("DOCX", "PDF", "DOC", "ZIP", "TXT", "WORD")
                        ),
                        filename,
                    )
                else:
                    doc_title = link_text or (cell_texts[1] if len(cell_texts) > 1 else filename)
                    doc_type = cell_texts[0] if cell_texts else ""

                date_str = ""
                for ct in cell_texts:
                    m = _DATE_RE.search(ct)
                    if m:
                        date_str = m.group(1)
                        break

                docs.append(
                    Document(
                        title=doc_title,
                        url=full_url,
                        file_date=date_str,
                        filename=filename,
                        file_ext=ext,
                        doc_type_label=doc_type,
                    )
                )

    # Fallback: broad link scan if no table docs found
    if not docs:
        for a in soup.find_all("a", href=True):
            href = str(a["href"])
            if any(href.lower().endswith(ext) for ext in _FILE_EXTS):
                full_url = urljoin(base_url, href)
                filename = urlparse(href).path.rsplit("/", 1)[-1]
                ext = "." + filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
                docs.append(
                    Document(
                        title=a.get_text(strip=True),
                        url=full_url,
                        file_date="",
                        filename=filename,
                        file_ext=ext,
                        doc_type_label="",
                    )
                )

    return docs
