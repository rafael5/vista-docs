"""
I/O layer for corpus manifest generation.

Reads the markdown corpus, runs consolidation to determine each document's
transformation role, builds a CorpusManifest, and writes corpus-manifest.json.

This module is intentionally thin: all logic lives in corpus_manifest.py and
consolidate.py (pure, unit-tested). This file is excluded from unit-test coverage.

-------------------------------------------------------------------------------
AXIOMS
-------------------------------------------------------------------------------

A.  ONLY DOCUMENTS WITH REQUIRED FRONTMATTER ARE INCLUDED.
    A document must have doc_type, app_code, and title in frontmatter to be
    included. Documents missing any of these three fields are logged and skipped.
    They do NOT appear in the manifest.

B.  CONSOLIDATION IS RUN INLINE.
    The runner calls run_consolidation logic (group_documents + consolidate_group)
    internally to determine each document's transformation role. The consolidation
    results are NOT written to disk by this runner — use `vista-docs consolidate`
    for that. The purpose here is role classification only.

C.  STUB DETECTION FROM FRONTMATTER.
    A document is treated as a stub if its frontmatter contains is_stub: true.

D.  OUTPUT: corpus-manifest.json in out_dir.
    The JSON is serialized with indent=2, sorted_keys=False, and utf-8 encoding.
    A summary line is logged: total docs, packages, transformation breakdown.
"""

from __future__ import annotations

import dataclasses
import json
import logging
import re
from pathlib import Path

from vista_docs.analyze.consolidate import (
    ConsolidationResult,
    DocumentRecord,
    consolidate_group,
    group_documents,
)
from vista_docs.analyze.corpus_manifest import CorpusManifest, build_manifest

log = logging.getLogger(__name__)

# Legacy doc_type codes → normalized values (mirrors DB normalization applied 2026-03-27)
_DOC_TYPE_NORMALIZE: dict[str, str] = {
    "RN": "release-note",
    "DIBR": "installation-guide",
    "UM": "user-manual",
    "UG": "user-manual",
    "TG": "user-manual",
    "REF": "user-manual",
    "IG": "installation-guide",
    "IG-IMP": "base-impl",
    "TM": "technical-manual",
    "VDD": "technical-manual",
    "DESC": "technical-manual",
    "POM": "supplement",
    "TRG": "supplement",
    "APX": "supplement",
    "PDD": "supplement",
    "SG": "base-setup",
    "SG-SET": "base-setup",
    "CFG": "base-setup",
    "INT": "base-hl7",
    "API": "base-dev",
    "QRG": "quick-ref",
}

# Frontmatter field extractors
_FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
# Note: use [ \t]* (not \s*) between colon and value to avoid consuming newlines
# when a preceding field has an empty value (e.g. "doc_subject: \napp_code: ADT").
_FIELD_RE = re.compile(r"^(\w+):[ \t]*(.+?)[ \t]*$", re.MULTILINE)


def _fm_field(text: str, field: str) -> str:
    m = _FM_RE.match(text)
    if not m:
        return ""
    for fm in _FIELD_RE.finditer(m.group(1)):
        if fm.group(1) == field:
            return fm.group(2).strip().strip('"').strip("'")
    return ""


def _fm_int(text: str, field: str) -> int:
    val = _fm_field(text, field)
    try:
        return int(val)
    except (ValueError, TypeError):
        return 0


def _fm_bool(text: str, field: str) -> bool:
    return _fm_field(text, field).lower() in ("true", "yes", "1")


def _build_transformation_map(
    results: dict[str, ConsolidationResult],
) -> dict[str, tuple[str, str, str]]:
    """
    Build {source_path: (transformation, consolidated_master_path, role)}
    from consolidation results.

    Master documents → "consolidated-master".
    Non-master members → "consolidated-addendum".
    """
    tmap: dict[str, tuple[str, str, str]] = {}
    for result in results.values():
        master_docs_path = f"docs/{result.group.doc_type}/{result.group.group_title}.md"
        # Master
        tmap[result.master.path] = ("consolidated-master", master_docs_path, "master")
        # Non-masters
        for doc in result.group.members:
            if doc is not result.master and doc.path not in tmap:
                tmap[doc.path] = ("consolidated-addendum", master_docs_path, "addendum")
    return tmap


def run_manifest(
    markdown_dir: Path,
    out_dir: Path,
    doc_types: list[str] | None = None,
) -> CorpusManifest:
    """
    Build the corpus manifest and write corpus-manifest.json to out_dir.

    Args:
        markdown_dir: Root of the markdown corpus (*.md walked recursively).
        out_dir:      Directory to write corpus-manifest.json (created if absent).
        doc_types:    If provided, only include these doc types. None = all.

    Returns:
        CorpusManifest for the processed corpus.
    """
    from datetime import datetime, timezone

    out_dir.mkdir(parents=True, exist_ok=True)

    # Load all documents
    records: list[DocumentRecord] = []
    stub_paths: set[str] = set()
    total_files = 0

    for md_path in sorted(markdown_dir.rglob("*.md")):
        total_files += 1
        try:
            text = md_path.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            log.warning("Could not read %s: %s", md_path, e)
            continue

        doc_type = _fm_field(text, "doc_type")
        app_code = _fm_field(text, "app_code")
        title = _fm_field(text, "title")

        if not doc_type or not app_code or not title:
            continue
        # Normalize legacy doc_type codes
        doc_type = _DOC_TYPE_NORMALIZE.get(doc_type, doc_type)
        if doc_types and doc_type not in doc_types:
            continue

        is_stub = _fm_bool(text, "is_stub")
        path_str = str(md_path)
        if is_stub:
            stub_paths.add(path_str)

        records.append(
            DocumentRecord(
                path=path_str,
                title=title,
                doc_type=doc_type,
                app_code=app_code,
                word_count=_fm_int(text, "word_count"),
                pub_date=_fm_field(text, "pub_date"),
                doc_layer=_fm_field(text, "doc_layer"),
                patch_id=_fm_field(text, "patch_id"),
                is_stub=is_stub,
                text=text,
            )
        )

    log.info("Loaded %d documents from %d files", len(records), total_files)

    # Run consolidation to determine transformation roles
    groups = group_documents(records)
    multi = [g for g in groups if len(g.members) >= 2]
    results: dict[str, ConsolidationResult] = {}
    for group in multi:
        group_key = f"{group.app_code}:{group.doc_type}:{group.group_title}"
        try:
            result = consolidate_group(group)
            results[group_key] = result
        except Exception as e:
            log.error("Consolidation failed for %s: %s", group_key, e)

    log.info(
        "Consolidation: %d groups, %d multi-version",
        len(groups),
        len(multi),
    )

    transformation_map = _build_transformation_map(results)
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    manifest = build_manifest(records, transformation_map, stub_paths, generated_at)

    # Write JSON
    out_path = out_dir / "corpus-manifest.json"
    _write_manifest_json(out_path, manifest)
    log.info("Manifest written: %s (%d documents)", out_path, manifest.total_documents)

    # Log transformation breakdown
    by_trans: dict[str, int] = {}
    for rec in manifest.documents:
        by_trans[rec.transformation] = by_trans.get(rec.transformation, 0) + 1
    for trans, count in sorted(by_trans.items(), key=lambda x: -x[1]):
        log.info("  %-26s %4d", trans, count)

    return manifest


def _write_manifest_json(path: Path, manifest: CorpusManifest) -> None:
    """Serialize CorpusManifest to JSON at path."""
    data = {
        "generated": manifest.generated,
        "total_documents": manifest.total_documents,
        "total_packages": manifest.total_packages,
        "documents": [dataclasses.asdict(doc) for doc in manifest.documents],
    }
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
