"""I/O helpers for the normalize stage (coverage-omitted, integration-tested).

Sidecar read/write, source hashing, and raw-source location. Pure transform
logic lives in the ``*_pure.py`` modules; this is the thin filesystem layer.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

import yaml

from vista_docs.normalize.revision_pure import RevisionRecord


def source_sha256(path: Path) -> str:
    """Streaming SHA-256 of a raw source file (docx/pdf)."""
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def history_sidecar_name(doc_path: Path) -> str:
    """``foo.md`` -> ``foo.history.yaml`` (shares the document basename)."""
    return doc_path.with_suffix("").name + ".history.yaml"


def write_history_sidecar(
    doc_path: Path,
    document_name: str,
    source_docx: str,
    records: list[RevisionRecord],
) -> Path:
    """Write the ``*.history.yaml`` revision sidecar next to ``doc_path``."""
    data = {
        "document": document_name,
        "source_docx": source_docx,
        "revisions": [
            {
                "date": r.date,
                "version": r.version,
                "pages": r.pages,
                "change": r.change,
                "refs": r.refs,
            }
            for r in records
        ],
    }
    side = doc_path.parent / history_sidecar_name(doc_path)
    side.write_text(
        yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=1000),
        encoding="utf-8",
    )
    return side


def find_raw_source(raw_dir: Path, url: str) -> Path | None:
    """Best-effort locate the raw docx/pdf for a frontmatter ``*_url`` value."""
    if not url:
        return None
    name = url.rsplit("/", 1)[-1]
    if not name:
        return None
    matches = list(raw_dir.rglob(name))
    return matches[0] if matches else None
