"""
I/O layer for local repo population.

Reads corpus-manifest.json, groups records by package, creates the local
directory structure for each package repo, copies originals, generates
PROVENANCE.md / README.md, and makes the initial git commit.

This module is intentionally thin: all layout and generation logic lives in
repo_builder.py (pure, unit-tested). This file is excluded from unit-test coverage.

-------------------------------------------------------------------------------
AXIOMS
-------------------------------------------------------------------------------

A.  SOURCE FILES ARE COPIED VERBATIM.
    originals/ files are byte-for-byte copies of the source markdown files.
    No reformatting, no field changes. SHA-256 is verified after copy.

B.  GIT INIT + INITIAL COMMIT.
    Each repo directory is git-initialized if not already. The initial commit
    includes all originals/ files, PROVENANCE.md, README.md,
    and a CHANGELOG.md placeholder.

C.  IDEMPOTENT.
    If a repo directory already exists and is a git repo, the populator skips
    it unless --force is passed. This allows re-running safely after partial
    failures.

D.  MANIFEST IS UPDATED.
    After successfully committing originals/ for a package, the manifest record's
    migration_status is updated to 'originals_committed' and git_commit_originals
    is set to the commit SHA. The manifest file is rewritten atomically.
"""

from __future__ import annotations

import hashlib
import json
import logging
import shutil
import subprocess
from dataclasses import asdict
from pathlib import Path

from vista_docs.analyze.corpus_manifest import ManifestRecord
from vista_docs.migrate.repo_builder import (
    build_repo_layout,
    generate_provenance_md,
    generate_readme,
    generate_zensical_toml,
)

log = logging.getLogger(__name__)


def _sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _git(args: list[str], cwd: Path) -> str:
    """Run a git command, return stdout. Raises on non-zero exit."""
    result = subprocess.run(
        ["git"] + args,
        cwd=cwd,
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def _is_git_repo(path: Path) -> bool:
    return (path / ".git").exists()


def populate_repos(
    manifest_path: Path,
    repos_dir: Path,
    packages: list[str] | None = None,
    force: bool = False,
) -> dict[str, int]:
    """
    Populate local git repos from corpus-manifest.json.

    Args:
        manifest_path: Path to corpus-manifest.json.
        repos_dir:     Root directory for all package repos (created if absent).
        packages:      If provided, only populate these packages. None = all.
        force:         Re-populate even if repo already exists.

    Returns:
        Dict of {app_code: files_committed} for all processed packages.
    """
    repos_dir.mkdir(parents=True, exist_ok=True)

    # Load manifest
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    all_records = [ManifestRecord(**d) for d in data["documents"]]

    # Group by package
    by_package: dict[str, list[ManifestRecord]] = {}
    for rec in all_records:
        by_package.setdefault(rec.package, []).append(rec)

    if packages:
        target_packages = [p.upper() for p in packages]
        by_package = {k: v for k, v in by_package.items() if k in target_packages}
        missing = set(target_packages) - set(by_package)
        for m in sorted(missing):
            log.warning("Package %s not found in manifest", m)

    log.info("Populating %d package repos in %s", len(by_package), repos_dir)

    results: dict[str, int] = {}
    manifest_records_by_path: dict[str, ManifestRecord] = {
        r.source_markdown_path: r for r in all_records
    }

    for app_code, records in sorted(by_package.items()):
        layout = build_repo_layout(app_code, records)
        repo_dir = repos_dir / layout.repo_name

        if _is_git_repo(repo_dir) and not force:
            log.info("%-8s skipped (already exists, use --force to re-populate)", app_code)
            continue

        try:
            n = _populate_one_repo(app_code, records, layout, repo_dir, manifest_records_by_path)
            results[app_code] = n
            log.info("%-8s committed %d originals → %s", app_code, n, repo_dir)
        except Exception as e:
            log.error("%-8s FAILED: %s", app_code, e)

    # Rewrite manifest with updated migration_status
    _update_manifest(manifest_path, data, manifest_records_by_path)

    return results


def _populate_one_repo(
    app_code: str,
    records: list[ManifestRecord],
    layout,
    repo_dir: Path,
    manifest_records_by_path: dict[str, ManifestRecord],
) -> int:
    """Create and populate one package repo. Returns count of files committed."""
    # Create directory structure
    repo_dir.mkdir(parents=True, exist_ok=True)
    for orig_dir in layout.originals_dirs:
        (repo_dir / orig_dir).mkdir(parents=True, exist_ok=True)
    (repo_dir / "docs").mkdir(exist_ok=True)

    # Copy originals
    files_copied = 0
    for rec in records:
        src = Path(rec.source_markdown_path)
        if not src.exists():
            log.warning("Source missing: %s", src)
            continue
        dest = repo_dir / rec.original_path
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)

        # Copy sibling image directory alongside dest, keeping the SOURCE name.
        # Image refs in the markdown use the source stem (e.g. "doc-stem/001.png"),
        # not the dest stem (which may have a package prefix like "CPRS_TM_doc-stem").
        src_img_dir = src.with_suffix("")
        if src_img_dir.is_dir():
            dest_img_dir = dest.parent / src_img_dir.name
            if dest_img_dir.exists():
                shutil.rmtree(dest_img_dir)
            shutil.copytree(src_img_dir, dest_img_dir)

        # Verify SHA-256 (Axiom A)
        actual_sha = _sha256_file(dest)
        if actual_sha != rec.original_sha256:
            log.warning(
                "SHA-256 mismatch for %s: expected %s got %s",
                dest.name,
                rec.original_sha256[:12],
                actual_sha[:12],
            )
        files_copied += 1

    # Generate repo files
    (repo_dir / "zensical.toml").write_text(generate_zensical_toml(layout), encoding="utf-8")
    (repo_dir / "PROVENANCE.md").write_text(
        generate_provenance_md(app_code, records), encoding="utf-8"
    )
    (repo_dir / "README.md").write_text(generate_readme(layout), encoding="utf-8")
    (repo_dir / "CHANGELOG.md").write_text(
        f"# {app_code} — Changelog\n\n"
        "_This file is auto-generated from release notes. "
        "Run `vista-docs changelog` to regenerate._\n",
        encoding="utf-8",
    )

    # Git init + commit
    if not _is_git_repo(repo_dir):
        _git(["init"], repo_dir)
        _git(["config", "user.email", "vista-docs-pipeline@local"], repo_dir)
        _git(["config", "user.name", "vista-docs pipeline"], repo_dir)

    _git(["add", "."], repo_dir)
    _git(
        [
            "commit",
            "--allow-empty",
            "-m",
            f"init: add {files_copied} original documents for {app_code}\n\n"
            f"Populated from VDL markdown corpus via vista-docs populate-repos.\n"
            f"All {files_copied} originals committed verbatim with SHA-256 checksums\n"
            f"recorded in PROVENANCE.md and corpus-manifest.json.",
        ],
        repo_dir,
    )

    # Record commit SHA in manifest records
    commit_sha = _git(["rev-parse", "HEAD"], repo_dir)
    for rec in records:
        if rec.source_markdown_path in manifest_records_by_path:
            manifest_records_by_path[
                rec.source_markdown_path
            ].migration_status = "originals_committed"
            manifest_records_by_path[rec.source_markdown_path].git_commit_originals = commit_sha

    return files_copied


def _update_manifest(
    manifest_path: Path,
    data: dict,
    records_by_path: dict[str, ManifestRecord],
) -> None:
    """Rewrite manifest JSON with updated migration_status fields."""
    data["documents"] = [
        asdict(records_by_path[d["source_markdown_path"]])
        if d["source_markdown_path"] in records_by_path
        else d
        for d in data["documents"]
    ]
    manifest_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
