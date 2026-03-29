"""
I/O layer for populating docs/ in each package repo.

Reads corpus-manifest.json, builds DocsEntry classifications per package,
finds source files (consolidated output or originals/), copies to docs/,
and commits with git.

This module is intentionally thin; all classification logic lives in
docs_builder.py (pure, unit-tested). Excluded from unit-test coverage.

-------------------------------------------------------------------------------
AXIOMS
-------------------------------------------------------------------------------

A.  CONSOLIDATED FILE LOOKUP.
    The consolidated output directory uses raw doc_type codes as subdirectory
    names (e.g. 'ig/', 'tm/') while the manifest uses normalized names
    ('installation-guide', 'technical-manual'). The runner builds a lookup
    index by scanning ALL files in the consolidated dir, reading their
    `consolidated_title` and `app_code` frontmatter fields, and keying on
    (app_code.upper(), consolidated_title). This key matches the group_title
    extracted from the manifest's `consolidated_master` field.

B.  ORIGINALS SOURCE.
    For source='original' entries, the file is already committed in the repo at
    originals/{doc_type}/{filename}. It is copied to docs/{doc_type}/{filename}.

C.  GIT COMMIT.
    A single commit is made per package after all docs/ files are written.
    Message: "docs: populate docs/ from consolidated masters and originals"
"""

from __future__ import annotations

import json
import logging
import re
import shutil
import subprocess
from pathlib import Path

from vista_docs.analyze.corpus_manifest import ManifestRecord
from vista_docs.migrate.docs_builder import build_docs_entries

log = logging.getLogger(__name__)

_FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
_FIELD_RE = re.compile(r"^(\w+):[ \t]*(.+?)[ \t]*$", re.MULTILINE)


def _fm_field(text: str, field: str) -> str:
    m = _FM_RE.match(text)
    if not m:
        return ""
    for fm in _FIELD_RE.finditer(m.group(1)):
        if fm.group(1) == field:
            return fm.group(2).strip().strip('"').strip("'")
    return ""


def _build_consolidated_index(consolidated_dir: Path) -> dict[tuple[str, str], Path]:
    """
    Scan consolidated_dir and build {(app_code, consolidated_title): file_path}.

    Reads every .md file's frontmatter for app_code and consolidated_title.
    This bridges the raw-doc_type directory names to normalized manifest keys.
    """
    index: dict[tuple[str, str], Path] = {}
    for md_path in consolidated_dir.rglob("*.md"):
        if md_path.name == "consolidation_summary.md":
            continue
        try:
            text = md_path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        app_code = _fm_field(text, "app_code").upper()
        title = _fm_field(text, "consolidated_title").strip('"').strip("'")
        if app_code and title:
            index[(app_code, title)] = md_path
    log.info("Consolidated index: %d entries from %s", len(index), consolidated_dir)
    return index


def _git(args: list[str], cwd: Path) -> str:
    result = subprocess.run(["git"] + args, cwd=cwd, capture_output=True, text=True, check=True)
    return result.stdout.strip()


def run_docs(
    manifest_path: Path,
    repos_dir: Path,
    consolidated_dir: Path,
    packages: list[str] | None = None,
) -> dict[str, int]:
    """
    Populate docs/ in each package repo.

    Args:
        manifest_path:    Path to corpus-manifest.json.
        repos_dir:        Root of local repos (vista-{pkg}/ dirs).
        consolidated_dir: Root of consolidated output (from vista-docs consolidate).
        packages:         If provided, only process these packages. None = all.

    Returns:
        Dict of {app_code: files_written} for all processed packages.
    """
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    all_records = [ManifestRecord(**d) for d in data["documents"]]

    # Build consolidated file index once (Axiom A)
    consolidated_index = _build_consolidated_index(consolidated_dir)

    # Group records by package
    by_package: dict[str, list[ManifestRecord]] = {}
    for rec in all_records:
        by_package.setdefault(rec.package, []).append(rec)

    if packages:
        target = {p.upper() for p in packages}
        by_package = {k: v for k, v in by_package.items() if k in target}

    results: dict[str, int] = {}

    for app_code, records in sorted(by_package.items()):
        repo_dir = repos_dir / f"vista-{app_code.lower()}"
        if not repo_dir.exists():
            log.warning("Repo not found: %s", repo_dir)
            continue

        entries = build_docs_entries(records)
        if not entries:
            continue

        files_written = 0
        for entry in entries:
            dest = repo_dir / entry.docs_path
            dest.parent.mkdir(parents=True, exist_ok=True)

            if entry.source == "consolidated":
                key = (app_code.upper(), entry.consolidated_title)
                src = consolidated_index.get(key)
                if src is None:
                    log.warning(
                        "%-8s consolidated file not found: (%s, %s)",
                        app_code,
                        app_code,
                        entry.consolidated_title,
                    )
                    continue
                shutil.copy2(src, dest)
            else:
                # source == "original"
                src = repo_dir / entry.original_path
                if not src.exists():
                    log.warning("%-8s original missing: %s", app_code, src)
                    continue
                shutil.copy2(src, dest)

            files_written += 1

        if files_written == 0:
            continue

        # Git commit (Axiom C)
        try:
            _git(["add", "docs/"], repo_dir)
            _git(
                [
                    "commit",
                    "-m",
                    f"docs: populate {files_written} files from consolidated masters and originals",
                ],
                repo_dir,
            )
        except subprocess.CalledProcessError as e:
            log.warning("Git commit failed for %s: %s", app_code, e.stderr.strip())

        results[app_code] = files_written
        log.info("%-8s %3d files → docs/", app_code, files_written)

    return results
