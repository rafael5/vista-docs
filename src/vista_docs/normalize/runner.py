"""Normalize stage runner (I/O layer; coverage-omitted, integration-tested).

Reads the **lossless** ``consolidated/`` tree and writes cleaned gold markdown to
a separate ``normalized/`` tree, so ``consolidated/`` is never mutated and
normalize is always re-runnable from it (spec §3, §10). For each document it
applies the pure :func:`normalize_body` orchestrator, routes the merged
frontmatter through the guarded audit serializer (``safe_dump_frontmatter`` — the
single owner of canonical keys), stamps provenance (``normalized_at`` /
``converter`` / ``source_sha256`` / ``normalize_version``), and writes a
``*.history.yaml`` sidecar for any document with a revision table.

Deterministic: a same-day re-run with ``--force`` regenerates byte-identical
output.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import yaml

from vista_docs.config import RAW_DIR
from vista_docs.normalize import NORMALIZE_VERSION
from vista_docs.normalize.io import find_raw_source, source_sha256, write_history_sidecar
from vista_docs.normalize.normalize_pure import normalize_body
from vista_docs.validate.frontmatter import safe_dump_frontmatter, split_frontmatter

log = logging.getLogger(__name__)

# The ingest converter (DOCX -> GFM). Set from the real pandoc version when known.
CONVERTER = "pandoc"


@dataclass
class NormalizeStats:
    processed: int = 0
    skipped: int = 0
    revisions_extracted: int = 0
    sidecars_written: int = 0


def normalize_file(in_path: Path, out_path: Path, *, raw_dir: Path, today: str) -> int:
    """Normalize ``in_path`` -> ``out_path``; return the revision count written."""
    text = in_path.read_text(encoding="utf-8")
    fm_raw, body = split_frontmatter(text)
    if fm_raw is None:
        log.warning("no frontmatter: %s", in_path)
        return 0
    fm = yaml.safe_load(fm_raw) or {}

    result = normalize_body(
        body,
        description=fm.get("description"),
        has_pdf=bool(fm.get("pdf_url")),
    )
    fm.update(result.frontmatter)
    fm["normalized_at"] = today
    fm["normalize_version"] = NORMALIZE_VERSION
    fm["converter"] = CONVERTER

    raw = find_raw_source(raw_dir, fm.get("docx_url") or fm.get("pdf_url") or "")
    if raw is not None:
        fm["source_sha256"] = source_sha256(raw)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    if result.revisions:
        side = write_history_sidecar(
            out_path, out_path.name, fm.get("docx_url", ""), result.revisions
        )
        fm["revision_sidecar"] = side.name

    new_text = "---\n" + safe_dump_frontmatter(fm) + "---\n" + result.body
    out_path.write_text(new_text, encoding="utf-8")
    return len(result.revisions)


def run_normalize(
    input_dir: Path,
    output_dir: Path,
    *,
    pkg: str | None = None,
    force: bool = False,
    raw_dir: Path = RAW_DIR,
    today: str | None = None,
) -> NormalizeStats:
    """Normalize every ``*.md`` under ``input_dir`` into ``output_dir`` (mirror tree)."""
    stats = NormalizeStats()
    stamp = today or datetime.now().strftime("%Y-%m-%d")
    for path in sorted(input_dir.rglob("*.md")):
        rel = path.relative_to(input_dir)
        if pkg and rel.parts and rel.parts[0].lower() != pkg.lower():
            continue
        out_path = output_dir / rel
        if out_path.exists() and not force:
            stats.skipped += 1
            continue
        n_rev = normalize_file(path, out_path, raw_dir=raw_dir, today=stamp)
        stats.processed += 1
        if n_rev:
            stats.revisions_extracted += n_rev
            stats.sidecars_written += 1
    return stats
