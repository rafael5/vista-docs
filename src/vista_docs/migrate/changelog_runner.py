"""
I/O layer for CHANGELOG generation.

Reads corpus-manifest.json, groups release-note records by package, reads
each RN file from the local repo's originals/, builds CHANGELOG.md, and
writes it to the repo root with a git commit.

This module is intentionally thin; all logic lives in changelog_builder.py.
Excluded from unit-test coverage.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path

from vista_docs.analyze.corpus_manifest import ManifestRecord
from vista_docs.migrate.changelog_builder import build_changelog

log = logging.getLogger(__name__)


def run_changelog(
    manifest_path: Path,
    repos_dir: Path,
    packages: list[str] | None = None,
) -> dict[str, int]:
    """
    Generate CHANGELOG.md for each package repo.

    Args:
        manifest_path: Path to corpus-manifest.json.
        repos_dir:     Root of the local repos (contains vista-{pkg}/ dirs).
        packages:      If provided, only process these packages. None = all.

    Returns:
        Dict of {app_code: rn_count} for all processed packages.
    """
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    all_records = [ManifestRecord(**d) for d in data["documents"]]

    # Group release-note records by package
    rn_by_package: dict[str, list[ManifestRecord]] = {}
    for rec in all_records:
        if rec.doc_type == "release-note":
            rn_by_package.setdefault(rec.package, []).append(rec)

    # All packages that have repos (even those with 0 release notes get a CHANGELOG)
    all_packages: set[str] = {rec.package for rec in all_records}
    if packages:
        target = {p.upper() for p in packages}
        all_packages = all_packages & target

    results: dict[str, int] = {}

    for app_code in sorted(all_packages):
        repo_name = f"vista-{app_code.lower()}"
        repo_dir = repos_dir / repo_name

        if not repo_dir.exists():
            log.warning("Repo not found: %s (run populate-repos first)", repo_dir)
            continue

        rn_records = rn_by_package.get(app_code, [])

        # Build content map from originals/ in the repo
        content_map: dict[str, str] = {}
        for rec in rn_records:
            orig_file = repo_dir / rec.original_path
            if orig_file.exists():
                try:
                    content_map[rec.original_path] = orig_file.read_text(
                        encoding="utf-8", errors="replace"
                    )
                except OSError as e:
                    log.warning("Could not read %s: %s", orig_file, e)

        changelog_text = build_changelog(app_code, rn_records, content_map)
        changelog_path = repo_dir / "CHANGELOG.md"
        changelog_path.write_text(changelog_text, encoding="utf-8")

        # Git commit
        try:
            import subprocess

            subprocess.run(
                ["git", "add", "CHANGELOG.md"],
                cwd=repo_dir,
                check=True,
                capture_output=True,
            )
            subprocess.run(
                [
                    "git",
                    "commit",
                    "-m",
                    f"changelog: generate from {len(rn_records)} release notes",
                ],
                cwd=repo_dir,
                check=True,
                capture_output=True,
            )
        except Exception as e:
            log.warning("Git commit failed for %s: %s", app_code, e)

        results[app_code] = len(rn_records)
        log.info("%-8s %3d release notes → CHANGELOG.md", app_code, len(rn_records))

    return results
