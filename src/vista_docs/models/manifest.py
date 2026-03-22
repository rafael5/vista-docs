"""
Pure dataclasses and enums for pipeline state management.

ManifestEntry is the central record that tracks every document
through every pipeline stage. FetchStatus and DocType are enums
used throughout the pipeline.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class FetchStatus(str, Enum):
    PENDING = "pending"
    OK = "ok"
    ERROR = "error"
    SKIPPED = "skipped"


class DocType(str, Enum):
    TECHNICAL_MANUAL = "technical-manual"
    USER_MANUAL = "user-manual"
    INSTALLATION_GUIDE = "installation-guide"
    RELEASE_NOTE = "release-note"
    QUICK_REF = "quick-ref"
    CHANGE_PAGE = "change-page"
    SUPPLEMENT = "supplement"
    BASE_SETUP = "base-setup"
    BASE_SECURITY = "base-security"
    BASE_DEV = "base-dev"
    BASE_HL7 = "base-hl7"
    BASE_IMPL = "base-impl"
    BASE_OTHER = "base-other"
    UNKNOWN = "unknown"


@dataclass
class ManifestEntry:
    """Tracks a single document through the full pipeline."""

    # Identity
    package_id: str        # e.g. "OR*3.0"
    app_code: str          # namespace prefix, e.g. "OR"
    doc_title: str
    doc_type: DocType = DocType.UNKNOWN
    patch: str = ""        # e.g. "OR*3.0*350" (most recent patch)

    # Source URLs (either or both may be present)
    docx_url: str = ""
    pdf_url: str = ""

    # Output
    output_filename: str = ""   # canonical .md filename

    # Fetch stage
    fetch_status: FetchStatus = FetchStatus.PENDING
    local_path: str = ""
    fetched_ext: str = ""       # "docx" or "pdf"
    fetch_size: int = 0
    fetch_error: str = ""

    # Ingest stage
    ingest_status: FetchStatus = FetchStatus.PENDING
    markdown_path: str = ""
    ingest_error: str = ""

    # Row ID in pipeline.db (0 = not yet persisted)
    db_id: int = 0
