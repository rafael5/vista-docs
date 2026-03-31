"""
I/O layer for building the human-browsable publish/ tree.

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
"""

from __future__ import annotations

import logging
import shutil
from pathlib import Path

from vista_docs.publish.builder import PublishEntry, build_publish_entries, load_app_info

log = logging.getLogger(__name__)


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
            # Resolve collision by appending source stem to filename
            stem = dest_abs.stem + "--" + entry.src_md.stem
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

            lines.append(f"### {pkg}")
            lines.append("")

            for entry in sorted(anchor_entries, key=lambda e: e.dest_path.name):
                rel = entry.dest_path
                name = rel.name.removesuffix(".md")
                lines.append(f"- [{name}]({rel})")

            if patch_entries:
                lines.append(f"- **patches/** ({len(patch_entries)} patch documents)")

            lines.append("")

    (out_dir / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")
    log.info("INDEX.md written (%d entries)", total)
