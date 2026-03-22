"""
Pure function: inventory CSV rows → list[ManifestEntry].

Collapses DOCX+PDF row-pairs (same app_code + doc_title) into a single
ManifestEntry with both docx_url and pdf_url populated.

Skips decommissioned apps. Classifies doc type. Generates output filenames.
"""

from __future__ import annotations

import re

from vista_docs.classify.rules import classify
from vista_docs.models.manifest import FetchStatus, ManifestEntry

_UNSAFE_RE = re.compile(r"[^a-z0-9]+")
_PATCH_RE = re.compile(r"([A-Z]+\*[\d.]+\*[\d]+)", re.I)


def _slugify(text: str) -> str:
    """Convert a document title to a safe filename stem."""
    slug = _UNSAFE_RE.sub("-", text.lower()).strip("-")
    return slug[:80]  # cap length


def _extract_patch(title: str) -> str:
    """Extract a patch identifier like 'OR*3.0*350' from a doc title."""
    m = _PATCH_RE.search(title)
    return m.group(1).upper() if m else ""


def build_entries_from_rows(rows: list[dict]) -> list[ManifestEntry]:
    """
    Convert flat inventory CSV rows into collapsed ManifestEntry records.

    Rules:
    - Group by (app_code, doc_title).
    - DOCX and PDF rows for the same document are merged into one entry.
    - Decommissioned apps are skipped; archive apps are included.
    - doc_type is classified from filename + title.
    - output_filename is derived from the doc title slug.
    """
    # Bucket rows by (app_code, doc_title)
    buckets: dict[tuple[str, str], list[dict]] = {}
    for row in rows:
        if row.get("app_status", "active") == "decommissioned":
            continue
        key = (row["app_code"], row["doc_title"])
        buckets.setdefault(key, []).append(row)

    entries: list[ManifestEntry] = []
    for (app_code, doc_title), bucket_rows in buckets.items():
        docx_url = ""
        pdf_url = ""
        filename = ""

        for row in bucket_rows:
            ext = row.get("file_ext", "").lower()
            url = row.get("doc_url", "")
            if ext == ".docx":
                docx_url = url
                filename = row.get("filename", "")
            elif ext == ".pdf":
                pdf_url = url
                if not filename:
                    filename = row.get("filename", "")

        doc_type = classify(filename, doc_title)
        output_filename = _slugify(doc_title) + ".md"

        entries.append(
            ManifestEntry(
                package_id="",  # not in inventory; filled later if needed
                app_code=app_code,
                doc_title=doc_title,
                doc_type=doc_type,
                patch=_extract_patch(doc_title),
                docx_url=docx_url,
                pdf_url=pdf_url,
                output_filename=output_filename,
                fetch_status=FetchStatus.PENDING,
            )
        )

    return entries
