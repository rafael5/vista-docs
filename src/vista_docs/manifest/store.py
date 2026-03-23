"""I/O thin layer: SQLite pipeline state management."""

from __future__ import annotations

import logging
import sqlite3
from pathlib import Path

from vista_docs.models.manifest import DocType, FetchStatus, ManifestEntry

logger = logging.getLogger(__name__)

_CREATE_SQL = """
CREATE TABLE IF NOT EXISTS manifest (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    package_id      TEXT NOT NULL,
    app_code        TEXT NOT NULL,
    doc_title       TEXT NOT NULL,
    doc_type        TEXT NOT NULL DEFAULT 'unknown',
    patch           TEXT NOT NULL DEFAULT '',
    docx_url        TEXT NOT NULL DEFAULT '',
    pdf_url         TEXT NOT NULL DEFAULT '',
    output_filename TEXT NOT NULL DEFAULT '',
    fetch_status    TEXT NOT NULL DEFAULT 'pending',
    local_path      TEXT NOT NULL DEFAULT '',
    fetched_ext     TEXT NOT NULL DEFAULT '',
    fetch_size      INTEGER NOT NULL DEFAULT 0,
    fetch_error     TEXT NOT NULL DEFAULT '',
    ingest_status   TEXT NOT NULL DEFAULT 'pending',
    markdown_path   TEXT NOT NULL DEFAULT '',
    ingest_error    TEXT NOT NULL DEFAULT '',
    UNIQUE(package_id, doc_title)
)
"""


def open_db(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute(_CREATE_SQL)
    conn.commit()
    return conn


def _row_to_entry(row: sqlite3.Row) -> ManifestEntry:
    return ManifestEntry(
        db_id=row["id"],
        package_id=row["package_id"],
        app_code=row["app_code"],
        doc_title=row["doc_title"],
        doc_type=DocType(row["doc_type"]),
        patch=row["patch"],
        docx_url=row["docx_url"],
        pdf_url=row["pdf_url"],
        output_filename=row["output_filename"],
        fetch_status=FetchStatus(row["fetch_status"]),
        local_path=row["local_path"],
        fetched_ext=row["fetched_ext"],
        fetch_size=row["fetch_size"],
        fetch_error=row["fetch_error"],
        ingest_status=FetchStatus(row["ingest_status"]),
        markdown_path=row["markdown_path"],
        ingest_error=row["ingest_error"],
    )


def load_all(conn: sqlite3.Connection) -> list[ManifestEntry]:
    rows = conn.execute("SELECT * FROM manifest ORDER BY id").fetchall()
    return [_row_to_entry(r) for r in rows]


def upsert(conn: sqlite3.Connection, entry: ManifestEntry) -> ManifestEntry:
    """Insert or update a manifest entry. Returns entry with db_id set."""
    conn.execute(
        """
        INSERT INTO manifest (
            package_id, app_code, doc_title, doc_type, patch,
            docx_url, pdf_url, output_filename,
            fetch_status, local_path, fetched_ext, fetch_size, fetch_error,
            ingest_status, markdown_path, ingest_error
        ) VALUES (
            :package_id, :app_code, :doc_title, :doc_type, :patch,
            :docx_url, :pdf_url, :output_filename,
            :fetch_status, :local_path, :fetched_ext, :fetch_size, :fetch_error,
            :ingest_status, :markdown_path, :ingest_error
        )
        ON CONFLICT(package_id, doc_title) DO UPDATE SET
            doc_type        = excluded.doc_type,
            patch           = excluded.patch,
            docx_url        = excluded.docx_url,
            pdf_url         = excluded.pdf_url,
            output_filename = excluded.output_filename,
            fetch_status    = excluded.fetch_status,
            local_path      = excluded.local_path,
            fetched_ext     = excluded.fetched_ext,
            fetch_size      = excluded.fetch_size,
            fetch_error     = excluded.fetch_error,
            ingest_status   = excluded.ingest_status,
            markdown_path   = excluded.markdown_path,
            ingest_error    = excluded.ingest_error
        """,
        {
            "package_id": entry.package_id,
            "app_code": entry.app_code,
            "doc_title": entry.doc_title,
            "doc_type": entry.doc_type.value,
            "patch": entry.patch,
            "docx_url": entry.docx_url,
            "pdf_url": entry.pdf_url,
            "output_filename": entry.output_filename,
            "fetch_status": entry.fetch_status.value,
            "local_path": entry.local_path,
            "fetched_ext": entry.fetched_ext,
            "fetch_size": entry.fetch_size,
            "fetch_error": entry.fetch_error,
            "ingest_status": entry.ingest_status.value,
            "markdown_path": entry.markdown_path,
            "ingest_error": entry.ingest_error,
        },
    )
    conn.commit()
    row = conn.execute(
        "SELECT id FROM manifest WHERE package_id=? AND doc_title=?",
        (entry.package_id, entry.doc_title),
    ).fetchone()
    from dataclasses import replace

    return replace(entry, db_id=row["id"])
