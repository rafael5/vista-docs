"""
Pure dataclasses representing the VDL catalog hierarchy.

Section → Application → Document

No logic, no I/O. These are the output types of crawl/parser.py.
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Document:
    """A single document entry on a VDL application page."""

    title: str
    url: str              # canonical URL on va.gov/vdl
    file_date: str        # display date string from VDL (e.g. "03/2024")


@dataclass
class Application:
    """A VistA application (package) listed under a VDL section."""

    name: str
    package_id: str       # e.g. "OR*3.0", "TIU*1.0"
    app_code: str         # namespace prefix, e.g. "OR", "TIU"
    url: str              # VDL application page URL
    documents: list[Document] = field(default_factory=list)


@dataclass
class Section:
    """A top-level VDL section (e.g. 'Clinical', 'Infrastructure')."""

    name: str
    url: str
    applications: list[Application] = field(default_factory=list)
