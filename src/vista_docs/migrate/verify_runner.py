"""
I/O layer for verifying committed originals against corpus-manifest.json SHA-256 hashes.

Reads corpus-manifest.json, walks each repo's originals/, computes SHA-256 of each
file, and compares against the manifest's original_sha256.

Excluded from unit-test coverage (I/O layer).
"""

from __future__ import annotations

import hashlib
import json
import logging
from pathlib import Path

from vista_docs.analyze.corpus_manifest import ManifestRecord
from vista_docs.migrate.verify_builder import VerifyResult, classify_result, summarize_results

log = logging.getLogger(__name__)


def _sha256_file(path: Path) -> str | None:
    """Return hex SHA-256 of file contents, or None if file is missing/unreadable."""
    try:
        data = path.read_bytes()
    except OSError:
        return None
    return hashlib.sha256(data).hexdigest()


def run_verify(
    manifest_path: Path,
    repos_dir: Path,
    packages: list[str] | None = None,
) -> list[VerifyResult]:
    """
    Verify all committed originals against corpus-manifest.json.

    Args:
        manifest_path: Path to corpus-manifest.json.
        repos_dir:     Root of local repos (vista-{pkg}/ dirs).
        packages:      If provided, only check these packages. None = all.

    Returns:
        List of VerifyResult for every checked record.
    """
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    all_records = [ManifestRecord(**d) for d in data["documents"]]

    if packages:
        target = {p.upper() for p in packages}
        all_records = [r for r in all_records if r.package in target]

    results: list[VerifyResult] = []

    for rec in all_records:
        repo_dir = repos_dir / f"vista-{rec.package.lower()}"
        if not repo_dir.exists():
            log.warning("Repo not found: %s", repo_dir)
            continue

        file_path = repo_dir / rec.original_path
        actual = _sha256_file(file_path)
        status = classify_result(rec.original_sha256, actual)

        results.append(
            VerifyResult(
                app_code=rec.package,
                original_path=rec.original_path,
                expected_sha256=rec.original_sha256,
                actual_sha256=actual or "",
                status=status,
            )
        )

        if status != "ok":
            log.warning("%-8s %-8s %s", rec.package, status.upper(), rec.original_path)

    summary = summarize_results(results)
    log.info(
        "Verify complete: %d total, %d ok, %d mismatch, %d missing",
        summary["total"],
        summary["ok"],
        summary["mismatch"],
        summary["missing"],
    )

    return results
