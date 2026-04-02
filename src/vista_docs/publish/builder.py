"""
Pure logic for building the human-browsable publish/ tree.

Takes consolidated groups and single-version docs and maps each to a
human-readable destination path under:

    {section}/{APP — Full Application Name}/{Doc Label}.md
    {section}/{APP — Full Application Name}/{Doc Label} — {Variant}.md
    {section}/{APP — Full Application Name}/patches/{PATCH_ID} — {Doc Label}.md

-------------------------------------------------------------------------------
AXIOMS
-------------------------------------------------------------------------------

A.  CONSOLIDATED GROUPS TAKE PRECEDENCE.
    The consolidated/ directory provides the master file for any group of 2+
    documents. Single-version files (no consolidated group) are taken directly
    from md-img/.

B.  DEDUPLICATION.
    The same consolidated group sometimes appears under two doc_type directories
    (e.g. 'dibr' and 'installation-guide') due to inconsistent doc_type tagging
    in the source corpus. We keep the entry with the highest-priority doc_type
    code (more specific > more generic).

C.  IMAGE DIRECTORIES.
    Each .md file may have a sibling directory of images (same stem, no suffix).
    These are discovered at the source location and copied alongside the dest .md
    with their original names intact — markdown image refs already point to them
    by their source stem, so no rewriting is needed.

D.  PATCH-LAYER DOCS.
    Documents with doc_layer='patch' go in a patches/ subdirectory using the
    filename pattern '{PATCH_ID} — {Doc Label}.md'.  This keeps the top-level
    of each package folder focused on the anchor/system documents.

E.  VARIANT DISAMBIGUATION.
    When a package has two or more consolidated groups of the same doc_label
    (e.g. CPRS has two Technical Manuals), a variant suffix is extracted from
    the consolidated_title and appended: '{Doc Label} — {Variant}.md'.
"""

from __future__ import annotations

import csv
import re
from dataclasses import dataclass, field
from pathlib import Path

# ---------------------------------------------------------------------------
# Canonical doc_code → human label
# ---------------------------------------------------------------------------

DOC_LABELS: dict[str, str] = {
    # Inventory codes (uppercase)
    "AG": "Administrator's Guide",
    "API": "API Manual",
    "APX": "Appendix",
    "CFG": "Configuration Guide",
    "CRU": "Clinical Reminder Update",
    "CVG": "Conversion Guide",
    "DESC": "Description Document",
    "DG": "Developer Guide",
    "DIBR": "Deployment, Installation, Back-Out, and Rollback Guide",
    "FAQ": "Frequently Asked Questions",
    "FORM": "VBA Form",
    "IG": "Installation Guide",
    "IG-IMP": "Implementation Guide",
    "INT": "Interface Specification",
    "PDD": "Patch Description Document",
    "POM": "Production Operations Manual",
    "QRG": "Quick Reference Guide",
    "REF": "Reference Guide",
    "RN": "Release Notes",
    "RS": "Requirements Specification",
    "SG": "Security Guide",
    "SG-SET": "Setup Guide",
    "SM": "Site Manual",
    "SUP": "Supplement",
    "TG": "Technical Guide",
    "TM": "Technical Manual",
    "TRG": "Training Guide",
    "UG": "User Guide",
    "UM": "User Manual",
    "VDD": "Version Description Document",
    "WF": "Workflow Guide",
    # Normalized pipeline names (lowercase with hyphens)
    "installation-guide": "Installation Guide",
    "technical-manual": "Technical Manual",
    "user-manual": "User Manual",
    "release-note": "Release Notes",
    "quick-ref": "Quick Reference Guide",
    "supplement": "Supplement",
    "base-setup": "Setup Guide",
    "base-impl": "Implementation Guide",
    "base-dev": "Developer Guide",
    "base-hl7": "HL7 Interface Guide",
    "unknown": "Document",
}

# Higher priority = preferred when two entries share the same (app, title)
_DTYPE_PRIORITY: dict[str, int] = {
    # Inventory codes are more specific — prefer them
    "dibr": 20,
    "ig-imp": 18,
    "ig": 16,
    "ug": 15,
    "um": 15,
    "rn": 15,
    "tm": 15,
    "tg": 14,
    "ag": 14,
    "qrg": 14,
    "sg": 14,
    "sm": 13,
    "sg-set": 13,
    "sup": 12,
    "pom": 12,
    "pdd": 12,
    "vdd": 12,
    "cfg": 12,
    "cvg": 12,
    "dg": 12,
    "rs": 12,
    "trg": 12,
    "wf": 12,
    "api": 12,
    "faq": 12,
    "ref": 12,
    "int": 12,
    "cru": 12,
    # Normalized names are less specific
    "installation-guide": 5,
    "technical-manual": 5,
    "user-manual": 5,
    "release-note": 5,
    "quick-ref": 5,
    "supplement": 5,
    "base-setup": 5,
    "base-impl": 5,
    "base-dev": 5,
    "base-hl7": 5,
    "unknown": 1,
}


def _dtype_priority(dt: str) -> int:
    return _DTYPE_PRIORITY.get(dt.lower(), 10)


def get_doc_label(doc_type: str) -> str:
    """Return human-readable label for a doc_type code."""
    upper = doc_type.upper()
    if upper in DOC_LABELS:
        return DOC_LABELS[upper]
    lower = doc_type.lower()
    if lower in DOC_LABELS:
        return DOC_LABELS[lower]
    # Fallback: title-case the code
    return doc_type.replace("-", " ").replace("_", " ").title()


# ---------------------------------------------------------------------------
# App info
# ---------------------------------------------------------------------------


@dataclass
class AppInfo:
    abbrev: str
    full_name: str
    section: str


# ---------------------------------------------------------------------------
# Section name overrides — applied before to_kebab()
# ---------------------------------------------------------------------------
_SECTION_RENAMES: dict[str, str] = {
    # Drop the parenthetical: most packages here are not HealtheVet systems
    "VistA/GUI Hybrids (formerly HealtheVet)": "vista-gui-hybrids",
}


def to_kebab(s: str) -> str:
    """
    Convert any string to pure kebab-case: [a-z0-9-] only.

    This is the single canonical normalizer for ALL path components
    (sections, package dirs, document filenames, variant suffixes).
    It produces output that is bash-safe without quoting, URL-safe,
    Python Path-safe, and consistent with the existing md-img layer.

    Rules applied in order:
      1. Lowercase everything
      2. & → and
      3. Apostrophes / smart quotes → removed (e.g. "manager's" → "managers")
      4. Any run of non-[a-z0-9] characters → single hyphen
      5. Collapse multiple hyphens → single hyphen
      6. Strip leading/trailing hyphens
    """
    s = s.lower()
    s = s.replace("&", "and")
    s = re.sub(r"[''`\u2018\u2019]", "", s)  # apostrophes / smart quotes
    s = re.sub(r"[^a-z0-9]+", "-", s)  # everything else → hyphen
    s = re.sub(r"-+", "-", s)  # collapse consecutive hyphens
    return s.strip("-")


# Compiled once for performance
_VERSION_RE = re.compile(r"\bversion-(\d+(?:-\d+)*)")
_UPDATED_RE = re.compile(r"-updated-[a-z0-9]+(?:-[a-z0-9]+)*$")


def _compact(s: str) -> str:
    """
    Compact administrative noise from a kebab-case string.

    Applied to variant/title components in filenames (not to package dirs or
    doc labels themselves, where the full name adds browsability value).

    Rules:
      1. version-N[-M] → vN[-M]   (e.g. version-5-3 → v5-3, version-7 → v7)
      2. -updated-PATCHREF$ → remove   (e.g. -updated-pso-7-0-628 → "")
      3. Strip residual leading/trailing hyphens
    """
    s = _VERSION_RE.sub(r"v\1", s)
    s = _UPDATED_RE.sub("", s)
    return s.strip("-")


def load_app_info(csv_path: Path) -> dict[str, AppInfo]:
    """Load {abbrev.upper(): AppInfo} from vdl_inventory_enriched.csv."""
    apps: dict[str, AppInfo] = {}
    with csv_path.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            abbrev = row["app_name_abbrev"].strip()
            full = row["app_name_full"].strip()
            raw_section = row["section_name"].strip()
            if abbrev and full and abbrev not in apps:
                section = _SECTION_RENAMES.get(raw_section, to_kebab(raw_section))
                apps[abbrev.upper()] = AppInfo(
                    abbrev=to_kebab(abbrev),
                    full_name=to_kebab(full),
                    section=section,
                )
    return apps


# ---------------------------------------------------------------------------
# Publish entry
# ---------------------------------------------------------------------------


@dataclass
class PublishEntry:
    src_md: Path
    dest_path: Path  # relative path within publish/ root
    src_image_dirs: list[Path] = field(default_factory=list)
    doc_label: str = ""
    is_patch: bool = False


# ---------------------------------------------------------------------------
# Filename helpers
# ---------------------------------------------------------------------------


def _extract_variant(consolidated_title: str, app_abbrev: str, label: str) -> str:
    """
    Extract the distinctive portion of a consolidated_title, stripping the
    app abbreviation and doc label (from either end).  Returns a raw string
    (not yet kebab-encoded) for the caller to pass through to_kebab().

    Examples:
        ("cprs technical manual: gui version", "CPRS", "Technical Manual") → "gui version"
        ("outpatient pharmacy version 7 release notes", "PSO", "Release Notes")
            → "outpatient pharmacy version 7"
        ("pharmacy operational updates deployment...", "PSO", "Deployment...")
            → "pharmacy operational updates"
    """
    t = consolidated_title.lower().strip("\"'")

    # Strip app_abbrev prefix (e.g. "cprs ")
    prefix = app_abbrev.lower()
    if t.startswith(prefix):
        t = t[len(prefix) :].lstrip(" _-:")

    dl = label.lower()

    # Try stripping doc_label from the start
    if t.startswith(dl):
        t = t[len(dl) :].lstrip(" _-:,")
    # Try stripping doc_label from the end
    elif t.endswith(dl):
        t = t[: -len(dl)].rstrip(" _-:,")
    # Try stripping doc_label from anywhere (last resort — avoids redundant variant)
    elif dl in t:
        t = t.replace(dl, " ").strip(" _-:,")

    return t.strip(" _-:,")


# ---------------------------------------------------------------------------
# Frontmatter reader
# ---------------------------------------------------------------------------

_FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
_FIELD_RE = re.compile(r"^(\w[\w-]*):\s*(.+?)\s*$", re.MULTILINE)


def _read_frontmatter(path: Path) -> dict[str, str]:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return {}
    m = _FM_RE.match(text)
    if not m:
        return {}
    return {
        f.group(1): f.group(2).strip().strip('"').strip("'") for f in _FIELD_RE.finditer(m.group(1))
    }


# ---------------------------------------------------------------------------
# Image discovery
# ---------------------------------------------------------------------------


def _find_image_dirs(md_path: Path) -> list[Path]:
    """Return sibling directories whose names are referenced by image links in the .md."""
    try:
        text = md_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []
    # Collect referenced image dir names (first path component of image src).
    # [^\n)] prevents matching across lines (avoids frontmatter false positives).
    referenced: set[str] = set()
    for m in re.finditer(r'!\[[^\n\]]*\]\(([^\n)]+)\)|<img[^>\n]+src=["\']([^"\'\n]+)["\']', text):
        src = (m.group(1) or m.group(2) or "").strip()
        if src:
            parts = src.replace("\\", "/").split("/")
            if len(parts) > 1:
                referenced.add(parts[0])
    dirs = []
    for name in referenced:
        candidate = md_path.parent / name
        try:
            if candidate.is_dir():
                dirs.append(candidate)
        except OSError:
            pass
    return dirs


# ---------------------------------------------------------------------------
# Main builder
# ---------------------------------------------------------------------------


def build_publish_entries(
    consolidated_dir: Path,
    md_img_dir: Path,
    manifest_path: Path,
    app_info: dict[str, AppInfo],
    packages: list[str] | None = None,
) -> list[PublishEntry]:
    """
    Compute all PublishEntry objects for the publish/ tree.

    Args:
        consolidated_dir:  Root of consolidation output.
        md_img_dir:        Root of md-img/ (Pandoc-converted source docs).
        manifest_path:     Path to corpus-manifest.json.
        app_info:          {abbrev.upper(): AppInfo} from load_app_info().
        packages:          If provided, only include these package codes.

    Returns:
        List of PublishEntry, one per output .md file.
    """
    import json

    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    pkg_filter = {p.upper() for p in packages} if packages else None

    # -----------------------------------------------------------------------
    # Step 1: Collect consolidated groups, deduplicating by (app, title).
    # -----------------------------------------------------------------------
    # key = (app_code_upper, consolidated_title_lower)
    # value = (md_path, doc_type)
    consolidated_best: dict[tuple[str, str], tuple[Path, str]] = {}

    for md in consolidated_dir.rglob("*.md"):
        if md.name == "consolidation_summary.md":
            continue
        fm = _read_frontmatter(md)
        app = fm.get("app_code", "").upper().strip()
        title = fm.get("consolidated_title", "").lower().strip().strip("\"'")
        dt = fm.get("doc_type", "").strip()
        if not app or not title:
            continue
        if pkg_filter and app not in pkg_filter:
            continue
        key = (app, title)
        existing = consolidated_best.get(key)
        if existing is None or _dtype_priority(dt) > _dtype_priority(existing[1]):
            consolidated_best[key] = (md, dt)

    # -----------------------------------------------------------------------
    # Step 2: For each consolidated group compute the dest path.
    # Group by (app, doc_label) to detect variants needing disambiguation.
    # -----------------------------------------------------------------------
    from collections import defaultdict

    # {(app, doc_label): [(title, md, dt), ...]}
    by_app_label: dict[tuple[str, str], list[tuple[str, Path, str]]] = defaultdict(list)
    for (app, title), (md, dt) in consolidated_best.items():
        label = get_doc_label(dt)
        by_app_label[(app, label)].append((title, md, dt))

    entries: list[PublishEntry] = []

    for (app, label), group in by_app_label.items():
        info = app_info.get(app)
        section = info.section if info else "other"
        pkg_folder = f"{info.abbrev}--{info.full_name}" if info else to_kebab(app)

        needs_variant = len(group) > 1
        label_k = to_kebab(label)

        for title, md, dt in sorted(group, key=lambda x: x[0]):
            if needs_variant:
                variant = _extract_variant(title, app, label)
                variant_k = _compact(to_kebab(variant)) if variant else ""
                # Skip variant if it duplicates the label (e.g. release-notes--release-notes)
                if variant_k and variant_k != label_k:
                    filename = f"{label_k}--{variant_k}.md"
                else:
                    title_k = _compact(to_kebab(title))
                    filename = f"{label_k}--{title_k}.md"
            else:
                filename = f"{label_k}.md"

            dest = Path(section) / pkg_folder / filename
            img_dirs = _find_image_dirs(md)

            entries.append(
                PublishEntry(
                    src_md=md,
                    dest_path=dest,
                    src_image_dirs=img_dirs,
                    doc_label=label,
                    is_patch=False,
                )
            )

    # -----------------------------------------------------------------------
    # Step 3: Single-version docs — take directly from md-img/.
    # -----------------------------------------------------------------------
    # Build set of source paths that are already represented by a consolidated group.
    consolidated_sources: set[str] = set()
    for d in data["documents"]:
        if d.get("consolidated_master"):
            consolidated_sources.add(d["source_markdown_path"])

    # Index manifest records by source path
    manifest_by_path: dict[str, dict] = {d["source_markdown_path"]: d for d in data["documents"]}

    # Collect single-version docs grouped by (app, doc_label) for anchor/plain layer
    # to detect variant conflicts.
    # key = (app, doc_label) → [(rec, src_path), ...]
    single_anchor: dict[tuple[str, str], list[tuple[dict, Path]]] = defaultdict(list)
    single_patch: list[tuple[dict, Path]] = []

    for src_path_str, rec in manifest_by_path.items():
        if src_path_str in consolidated_sources:
            continue  # already covered by consolidated group
        app = rec.get("package", "").upper()
        if pkg_filter and app not in pkg_filter:
            continue

        src = Path(src_path_str)
        if not src.exists():
            continue

        dt = rec.get("doc_type", "unknown")
        layer = rec.get("doc_layer", "")
        patch_id = (rec.get("patch_id") or "").strip()

        label = get_doc_label(dt)

        if layer == "patch" and patch_id:
            single_patch.append((rec, src))
        else:
            single_anchor[(app, label)].append((rec, src))

    # Anchor/plain single-version docs
    for (app, label), anchor_group in single_anchor.items():
        info = app_info.get(app)
        section = info.section if info else "other"
        pkg_folder = f"{info.abbrev}--{info.full_name}" if info else to_kebab(app)

        needs_variant = len(anchor_group) > 1
        label_k = to_kebab(label)

        for rec, src in sorted(anchor_group, key=lambda x: x[1].stem):
            if needs_variant:
                fm = _read_frontmatter(src)
                title_raw = fm.get("title", src.stem)
                variant = _extract_variant(title_raw, app, label)
                variant_k = _compact(to_kebab(variant)) if variant else ""
                # Skip variant if it duplicates the label
                if variant_k and variant_k != label_k:
                    filename = f"{label_k}--{variant_k}.md"
                else:
                    filename = f"{label_k}--{_compact(src.stem)}.md"
            else:
                filename = f"{label_k}.md"

            dest = Path(section) / pkg_folder / filename
            img_dirs = _find_image_dirs(src)

            entries.append(
                PublishEntry(
                    src_md=src,
                    dest_path=dest,
                    src_image_dirs=img_dirs,
                    doc_label=label,
                    is_patch=False,
                )
            )

    # Patch-layer single-version docs
    # Group by (app, doc_label) to detect duplicates (same patch, same type)
    patch_dest_seen: set[Path] = set()
    for rec, src in sorted(single_patch, key=lambda x: (x[0]["package"], x[0].get("patch_id", ""))):
        app = rec.get("package", "").upper()
        info = app_info.get(app)
        section = info.section if info else "other"
        pkg_folder = f"{info.abbrev}--{info.full_name}" if info else to_kebab(app)

        dt = rec.get("doc_type", "unknown")
        patch_id = (rec.get("patch_id") or "").strip()
        label = get_doc_label(dt)
        label_k = to_kebab(label)
        patch_k = _compact(to_kebab(patch_id))
        filename = f"{patch_k}--{label_k}.md"
        dest = Path(section) / pkg_folder / "patches" / filename

        # Resolve collisions by appending source stem
        if dest in patch_dest_seen:
            filename = f"{patch_k}--{label_k}--{_compact(src.stem)}.md"
            dest = Path(section) / pkg_folder / "patches" / filename
        patch_dest_seen.add(dest)

        img_dirs = _find_image_dirs(src)

        entries.append(
            PublishEntry(
                src_md=src,
                dest_path=dest,
                src_image_dirs=img_dirs,
                doc_label=label,
                is_patch=True,
            )
        )

    return entries
