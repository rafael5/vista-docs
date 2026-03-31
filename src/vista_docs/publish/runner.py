"""
I/O layer for building the human-browsable publish/ tree and pushing it to GitHub.

Reads consolidated/ and md-img/, computes PublishEntry objects via builder.py,
copies .md files and their sibling image directories to publish/ under
human-readable paths, and writes a top-level INDEX.md.

This module is intentionally thin; all path/naming logic lives in builder.py
(pure, unit-tested). Excluded from unit-test coverage.

-------------------------------------------------------------------------------
AXIOMS
-------------------------------------------------------------------------------

A.  IMAGE DIRECTORIES ARE COPIED WITH THEIR ORIGINAL NAMES.
    Markdown image refs use the source directory stem (e.g. "or-3-0-453.../001.png").
    Image dirs are copied as siblings of the dest .md under the same name, so
    all image refs resolve without any rewriting.

B.  COLLISION RESOLUTION.
    If two entries map to the same dest_path, the second is skipped with a warning.
    This should not happen in practice given builder.py's variant logic.

C.  INDEX.md.
    A top-level INDEX.md is written listing all output files grouped by section
    and package, with relative links. This serves as a human entry point.

D.  GIT STATE PRESERVATION.
    When force=True and publish/ already contains a .git/ repo, only the
    generated content is cleared (not .git/ or .gitignore). This lets
    run_publish --force + run_push work without re-initializing the repo.

E.  PUSH: MARKDOWN ONLY.
    run_push() commits and pushes only .md files. Images are excluded via
    .gitignore so the GitHub repo stays small (<200 MB vs 1.9 GB with images).
"""

from __future__ import annotations

import logging
import shutil
import subprocess
from datetime import date
from pathlib import Path

from vista_docs.publish.builder import PublishEntry, _compact, build_publish_entries, load_app_info

log = logging.getLogger(__name__)

# Written to publish/.gitignore on first push — excludes binary image files.
_GITIGNORE = """\
# Image directories — binary content excluded to keep the GitHub repo small.
# All markdown documents are tracked; images are available in the local
# ~/data/vista-docs/publish/ tree but not pushed to the remote.
*.png
*.jpg
*.jpeg
*.gif
*.tif
*.tiff
*.bmp
*.svg
*.webp
"""


def run_publish(
    consolidated_dir: Path,
    md_img_dir: Path,
    manifest_path: Path,
    inventory_csv: Path,
    out_dir: Path,
    packages: list[str] | None = None,
    force: bool = False,
) -> dict[str, int]:
    """
    Write the human-browsable publish/ tree.

    Returns:
        Dict with keys: packages, anchor_files, patch_files, image_dirs.
    """
    if out_dir.exists() and force:
        if (out_dir / ".git").exists():
            # Preserve git state: clear generated content but not .git/ or .gitignore
            for item in out_dir.iterdir():
                if item.name not in (".git", ".gitignore"):
                    shutil.rmtree(item) if item.is_dir() else item.unlink()
            log.debug("Cleared publish/ content (preserved .git/)")
        else:
            shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    app_info = load_app_info(inventory_csv)
    log.info("Loaded %d app entries from inventory", len(app_info))

    entries = build_publish_entries(
        consolidated_dir=consolidated_dir,
        md_img_dir=md_img_dir,
        manifest_path=manifest_path,
        app_info=app_info,
        packages=packages,
    )
    log.info("Computed %d publish entries", len(entries))

    dest_seen: set[Path] = set()
    anchor_count = 0
    patch_count = 0
    img_dir_count = 0
    pkg_seen: set[str] = set()
    final_entries: list[PublishEntry] = []  # entries with collision-resolved paths

    for entry in entries:
        dest_abs = out_dir / entry.dest_path
        if dest_abs in dest_seen:
            # Resolve collision by appending (compacted) source stem to filename
            stem = dest_abs.stem + "--" + _compact(entry.src_md.stem)
            dest_abs = dest_abs.parent / (stem + dest_abs.suffix)
            entry = PublishEntry(
                src_md=entry.src_md,
                dest_path=dest_abs.relative_to(out_dir),
                src_image_dirs=entry.src_image_dirs,
                doc_label=entry.doc_label,
                is_patch=entry.is_patch,
            )
            log.warning("Collision resolved → %s", entry.dest_path)
        dest_seen.add(dest_abs)
        final_entries.append(entry)

        dest_abs.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(entry.src_md, dest_abs)

        # Track package (second component of dest_path)
        parts = entry.dest_path.parts
        if len(parts) >= 2:
            pkg_seen.add(parts[1])

        # Copy sibling image directories alongside dest .md (Axiom A)
        for img_dir in entry.src_image_dirs:
            dest_img = dest_abs.parent / img_dir.name
            if dest_img.exists():
                shutil.rmtree(dest_img)
            shutil.copytree(img_dir, dest_img)
            img_dir_count += 1
            log.debug("  img_dir → %s", dest_img.relative_to(out_dir))

        if entry.is_patch:
            patch_count += 1
        else:
            anchor_count += 1

        log.info("%-60s → %s", str(entry.src_md)[-55:], entry.dest_path)

    _write_index(out_dir, final_entries)

    log.info(
        "publish/: %d packages, %d anchor docs, %d patch docs, %d image dirs",
        len(pkg_seen),
        anchor_count,
        patch_count,
        img_dir_count,
    )

    return {
        "packages": len(pkg_seen),
        "anchor_files": anchor_count,
        "patch_files": patch_count,
        "image_dirs": img_dir_count,
    }


def _write_index(out_dir: Path, entries: list[PublishEntry]) -> None:
    """Write top-level INDEX.md with links to all published documents."""
    from collections import defaultdict

    # Group by section → pkg_folder → entries
    tree: dict[str, dict[str, list[PublishEntry]]] = defaultdict(lambda: defaultdict(list))
    for entry in entries:
        parts = entry.dest_path.parts
        if len(parts) >= 3:
            section = parts[0]
            pkg = parts[1]
        elif len(parts) == 2:
            section = "_Other"
            pkg = parts[0]
        else:
            continue
        tree[section][pkg].append(entry)

    lines: list[str] = [
        "# VistA Documentation Library — Published Corpus",
        "",
        "_Human-browsable consolidated markdown. "
        "Anchor documents represent master + all prior versions as appendices. "
        "Patch documents are individual patch-level releases._",
        "",
        "---",
        "",
    ]

    total = sum(len(v) for pkg_map in tree.values() for v in pkg_map.values())
    lines.append(f"**{total} documents** across **{sum(len(v) for v in tree.values())} packages**")
    lines.append("")

    for section in sorted(tree):
        lines.append(f"## {section}")
        lines.append("")
        for pkg in sorted(tree[section]):
            pkg_entries = tree[section][pkg]
            anchor_entries = [e for e in pkg_entries if not e.is_patch]
            patch_entries = [e for e in pkg_entries if e.is_patch]

            doc_count = len(anchor_entries) + (1 if patch_entries else 0)
            lines.append("<details>")
            lines.append(f"<summary><strong>{pkg}</strong> ({doc_count} docs)</summary>")
            lines.append("")

            for entry in sorted(anchor_entries, key=lambda e: e.dest_path.name):
                rel = entry.dest_path
                name = rel.name.removesuffix(".md")
                lines.append(f"- [{name}]({rel})")

            if patch_entries:
                lines.append(f"- **patches/** ({len(patch_entries)} patch documents)")

            lines.append("")
            lines.append("</details>")
            lines.append("")

    content = "\n".join(lines)
    (out_dir / "INDEX.md").write_text(content, encoding="utf-8")
    (out_dir / "README.md").write_text(content, encoding="utf-8")
    log.info("INDEX.md / README.md written (%d entries)", total)


# ---------------------------------------------------------------------------
# GitHub push (Axiom E)
# ---------------------------------------------------------------------------


def run_push(
    out_dir: Path,
    remote_url: str,
    commit_message: str | None = None,
) -> bool:
    """
    Commit and push the publish/ tree (markdown only) to a remote git repo.

    Initialises the repo if needed, writes .gitignore to exclude images,
    stages all tracked files, commits, and pushes to origin/main.

    Args:
        out_dir:        Path to publish/ directory (must already exist).
        remote_url:     SSH or HTTPS URL of the remote, e.g.
                        "git@github.com:vistadocs/vdl.git".
        commit_message: Override the auto-generated commit message.

    Returns:
        True if a new commit was pushed; False if nothing changed.

    Raises:
        RuntimeError: if any git command fails.
    """

    # GitHub's recommended per-file size limit (hard limit is 100 MB)
    _GITHUB_SIZE_LIMIT = 50 * 1024 * 1024  # 50 MB

    def _git(*args: str, check: bool = False) -> subprocess.CompletedProcess[str]:
        result = subprocess.run(
            ["git", *args],
            cwd=out_dir,
            capture_output=True,
            text=True,
        )
        if check and result.returncode != 0:
            raise RuntimeError(
                f"git {' '.join(args)} failed (exit {result.returncode}):\n{result.stderr.strip()}"
            )
        return result

    # Write .gitignore if missing
    gitignore = out_dir / ".gitignore"
    if not gitignore.exists():
        gitignore.write_text(_GITIGNORE, encoding="utf-8")
        log.info(".gitignore written (images excluded)")

    # Scan for oversize markdown files and append them to .gitignore
    oversize: list[str] = sorted(
        str(md.relative_to(out_dir))
        for md in out_dir.rglob("*.md")
        if md.stat().st_size > _GITHUB_SIZE_LIMIT
    )
    if oversize:
        existing_gi = gitignore.read_text(encoding="utf-8")
        new_entries = [p for p in oversize if p not in existing_gi]
        if new_entries:
            with gitignore.open("a", encoding="utf-8") as f:
                f.write("\n# Markdown files exceeding GitHub's 50 MB limit\n")
                for path in new_entries:
                    f.write(f"{path}\n")
        for path in oversize:
            size_mb = (out_dir / path).stat().st_size / 1_048_576
            log.warning("Excluding oversized file (%.0f MB): %s", size_mb, path)
        log.warning("%d oversized file(s) excluded from push", len(oversize))

    # Initialise repo if needed
    if not (out_dir / ".git").exists():
        _git("init", "-b", "main", check=True)
        log.info("Initialised git repo in %s", out_dir)

    # Set remote
    existing = _git("remote", "get-url", "origin")
    if existing.returncode != 0:
        _git("remote", "add", "origin", remote_url, check=True)
        log.info("Remote added: %s", remote_url)
    elif existing.stdout.strip() != remote_url:
        _git("remote", "set-url", "origin", remote_url, check=True)
        log.info("Remote updated → %s", remote_url)

    # Stage everything (.gitignore keeps images and oversize files out)
    _git("add", "-A", check=True)

    # Commit if there are staged changes
    if _git("diff", "--cached", "--quiet").returncode != 0:
        msg = commit_message or f"Publish VDL corpus ({date.today()})"
        _git("commit", "-m", msg, check=True)
        log.info("Committed: %s", msg)

    # Push if there are any local commits not yet on the remote.
    # (Covers both a fresh commit above and a commit that failed to push last run.)
    unpushed = _git("log", "origin/main..HEAD", "--oneline")
    has_unpushed = unpushed.returncode == 0 and unpushed.stdout.strip()
    # Also covers brand-new repos where origin/main doesn't exist yet
    no_remote_ref = unpushed.returncode != 0

    if not has_unpushed and not no_remote_ref:
        log.info("Nothing to push — remote is already up to date")
        return False

    # Force is safe: publish/ is always regenerated from canonical sources.
    _git("push", "-u", "origin", "main", "--force", check=True)
    log.info("Pushed to %s", remote_url)
    return True
