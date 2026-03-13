#!/usr/bin/env python3
"""
ingest.py — Convert fetched VDL documents to markdown using Docling.

Usage (run from repo root):
    python3 scripts/ingest.py --manifest scripts/manifest.json [--pkg cprs] [--base-only] [--force]
"""

import json
import re
import argparse
import sys
from pathlib import Path
from datetime import datetime

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed. Run: pip install pyyaml")
    sys.exit(1)

try:
    from docling.document_converter import DocumentConverter
    DOCLING_AVAILABLE = True
except ImportError:
    DOCLING_AVAILABLE = False
    print("WARNING: docling not installed — run: pip install docling")
    print("         Continuing in scaffold-only mode.\n")

MAX_STUB_ENTRIES = 50  # cap patch history stubs for large gaps (e.g. ADT=258)

# =============================================================================
# 1. VA POST-PROCESSING TRANSFORMS
# =============================================================================

TITLE_PAGE_PATTERNS = [
    re.compile(r'^Department of Veterans Affairs\s*$', re.M | re.I),
    re.compile(r'^Office of Information[^\n]*\s*$', re.M | re.I),
    re.compile(r'^Veterans Health Administration\s*$', re.M | re.I),
    re.compile(r'^VistA\s+[-–]\s+\w.*\nVersion \d', re.M | re.I),
]

OUTLINE_NUM_RE  = re.compile(r'^(#{1,6})\s+(?:\d+\.)+\d*\s+', re.M)
EMPTY_HEAD_RE   = re.compile(r'^#{1,6}\s*$', re.M)
# Docling emits 7–10 hashes on some VA section headers — cap at H6
HEADING_OVERFLOW_RE = re.compile(r'^#{7,}(\s)', re.M)
# Orphaned bare-number headings left after outline-number stripping e.g. "### 1\n"
ORPHAN_NUM_HEAD_RE  = re.compile(r'^(#{1,6})\s+\d+\s*$', re.M)
VISTA_TERM_RE  = re.compile(
    r'((?:(?:^[ \t]*>.*$|^Select \w.*:.*$|^Enter .*:.*$)\n?){3,})', re.M)
RPC_TABLE_RE   = re.compile(r'(\|[^\n]*\bRPC\b[^\n]*\|)', re.I)
TOC_BLOCK_RE   = re.compile(r'(?:^[-*]\s+\[.*?\]\(#.*?\)\s*\n){4,}', re.M)

# Revision history table: header row contains "Patch" or "Version"
REVISION_RE    = re.compile(
    r'(\|[^\n]*(Patch|Version)[^\n]*\|\s*\n\|[-| :]+\|\s*\n(?:\|[^\n]+\|\s*\n)+)', re.I)

# Patch: require full namespace*version*patch pattern to avoid false positives
PATCH_FULL_RE  = re.compile(r'([A-Z]+\*[\d.]+)\*(\d{3,4})')

# Date: MM/DD/YYYY, MM/YYYY, YYYY-MM, Month YYYY
DATE_RE        = re.compile(
    r'(\d{1,2}/\d{1,2}/\d{4}|\d{1,2}/\d{4}|\d{4}-\d{2}|'
    r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*[\s,]+\d{4})', re.I)

MONTH_MAP = {
    'jan':'01','feb':'02','mar':'03','apr':'04','may':'05','jun':'06',
    'jul':'07','aug':'08','sep':'09','oct':'10','nov':'11','dec':'12'
}


def normalise_date(raw: str) -> str:
    """Normalise any date string to YYYY-MM."""
    raw = raw.strip()
    m = re.match(r'(\d{1,2})/\d{1,2}/(\d{4})', raw)   # MM/DD/YYYY
    if m: return f"{m.group(2)}-{int(m.group(1)):02d}"
    m = re.match(r'(\d{1,2})/(\d{4})', raw)            # MM/YYYY
    if m: return f"{m.group(2)}-{int(m.group(1)):02d}"
    if re.match(r'\d{4}-\d{2}', raw): return raw       # already YYYY-MM
    m = re.match(r'([A-Za-z]+)[\s,]+(\d{4})', raw)     # Month YYYY
    if m:
        mon = MONTH_MAP.get(m.group(1).lower()[:3], '01')
        return f"{m.group(2)}-{mon}"
    return raw


def extract_revision_info(md: str, pkg_id: str = "") -> dict:
    """
    Extract the MOST RECENT patch number and date from the revision history table.

    VA documents may reference cross-package patches (e.g. XU*8.0*679 in a CPRS
    doc). We identify the primary namespace by frequency and prefer patches within
    it. Falls back to overall max if no primary namespace patches found.
    """
    from collections import Counter

    m = REVISION_RE.search(md)
    if not m:
        return {}

    table = m.group(0)

    # Collect (namespace, patch_num, date_str) per row
    rows_data = []
    for row in table.split("\n"):
        if not row.startswith("|") or "---" in row:
            continue
        ns_patches = PATCH_FULL_RE.findall(row)
        dates      = DATE_RE.findall(row)
        if ns_patches:
            date_str = normalise_date(dates[0]) if dates else None
            for ns, p in ns_patches:
                rows_data.append((ns, int(p), date_str))

    if not rows_data:
        return {}

    # Determine primary namespace: use pkg_id prefix if supplied, else most frequent
    ns_counts  = Counter(ns for ns, _, _ in rows_data)
    if pkg_id:
        # e.g. pkg_id = "OR*3.0" — match namespace exactly
        primary_ns = pkg_id if pkg_id in ns_counts else ns_counts.most_common(1)[0][0]
    else:
        primary_ns = ns_counts.most_common(1)[0][0]

    primary = [(ns, p, d) for ns, p, d in rows_data if ns == primary_ns]
    pool    = primary if primary else rows_data

    # Best = highest patch in primary namespace
    best = max(pool, key=lambda x: x[1])
    result = {"patch": best[1]}
    if best[2]:
        result["date_raw"] = best[2]
    return result


def extract_title_from_body(md: str) -> str | None:
    """
    Extract the document title from the first H1 heading in the body.
    Returns None if no H1 found (fallback to filename-derived title).
    """
    m = re.search(r'^#\s+(.+)$', md, re.M)
    return m.group(1).strip() if m else None


def is_change_pages_doc(md: str) -> bool:
    """
    Detect VA change-pages documents — diff artifacts that list page replacements.
    Signature: 'Replace Pages:' table near the top of the document.
    """
    # Check only the first 3000 chars to avoid false positives deep in a doc
    head = md[:3000]
    return bool(re.search(r'Replace Pages?\s*:', head, re.I))


def apply_transforms(md: str, pkg_id: str = "") -> tuple[str, dict]:
    rev_info = extract_revision_info(md, pkg_id=pkg_id)

    # Extract title before boilerplate stripping removes H1 candidates
    extracted_title = extract_title_from_body(md)
    if extracted_title:
        rev_info["extracted_title"] = extracted_title

    # Flag change-pages docs before any transforms alter the content
    rev_info["is_change_pages"] = is_change_pages_doc(md)

    # Strip title page boilerplate
    for pat in TITLE_PAGE_PATTERNS:
        md = pat.sub('', md)

    # Strip empty headings left by title page removal
    md = EMPTY_HEAD_RE.sub('', md)

    # Cap heading depth — Docling emits 7-10 hashes on some VA headers
    md = HEADING_OVERFLOW_RE.sub(r'######\1', md)

    md = TOC_BLOCK_RE.sub('', md)
    md = OUTLINE_NUM_RE.sub(r'\1 ', md)

    # Remove orphaned bare-number headings left after outline stripping e.g. "### 1"
    md = ORPHAN_NUM_HEAD_RE.sub('', md)

    # Fence VistA terminal blocks
    md = VISTA_TERM_RE.sub(
        lambda m: f"\n```vista\n{m.group(1).rstrip()}\n```\n", md)

    # Mark RPC tables for downstream tooling
    md = RPC_TABLE_RE.sub(r'<!-- rpc-table -->\n\1', md)

    # Normalise image paths to assets/
    md = re.sub(
        r'!\[(.*?)\]\((?!assets/)([^)]+)\)',
        lambda m: f"![{m.group(1)}](assets/{Path(m.group(2)).name})", md)

    # Clean up blank lines left by removals
    md = re.sub(r'\n{4,}', '\n\n\n', md)
    return md.strip(), rev_info


# =============================================================================
# 2. FRONTMATTER
# =============================================================================

def build_frontmatter(doc: dict, pkg: dict, rev_info: dict) -> dict:
    patch_num = rev_info.get("patch") or doc.get("patch_num")
    base_max  = pkg.get("base_max_patch")
    lib_max   = pkg.get("library_max_patch")

    if base_max and lib_max:
        gap = lib_max - base_max
        currency = (
            "current"        if gap == 0  else
            "minor-lag"      if gap <= 10 else
            "stale"          if gap <= 50 else
            "severely-stale"
        )
    else:
        currency = "unverifiable"

    # Prefer title extracted from H1 body over filename-derived title
    title = (
        rev_info.get("extracted_title")
        or doc.get("title", "")
    )

    return {
        "title":               title,
        "doc_type":            doc.get("doc_class", "unknown"),
        "app_name":            pkg.get("app_name", ""),
        "package_id":          pkg.get("package_id", ""),
        "section":             pkg.get("section", ""),
        "patch":               patch_num,
        "base_max_patch":      base_max,
        "library_max_patch":   lib_max,
        "patch_gap":           (lib_max - base_max) if (base_max and lib_max) else None,
        "currency_status":     currency,
        "doc_date":            rev_info.get("date_raw"),
        "source_file":         doc.get("docx_filename") or doc.get("pdf_filename", ""),
        "fetch_format":        doc.get("fetch_format", ""),
        "is_base":             doc.get("is_base", False),
        "is_change_pages":     rev_info.get("is_change_pages", False),
        "change_pages_merged": False,
        "forum_patch_stub":    False,
        "ingest_date":         datetime.now().strftime("%Y-%m-%d"),
        "status":              "draft",
    }


def frontmatter_str(fm: dict) -> str:
    return "---\n" + yaml.dump(fm, default_flow_style=False, allow_unicode=True) + "---\n\n"


# =============================================================================
# 3. PATCH HISTORY SKELETON
# =============================================================================

def build_patch_history(doc: dict, pkg: dict) -> str:
    base_max = pkg.get("base_max_patch")
    lib_max  = pkg.get("library_max_patch")

    if not (base_max and lib_max and lib_max > base_max):
        return ""

    gap = lib_max - base_max
    vdl_patches = {
        d["patch_num"]: d["title"]
        for d in pkg.get("documents", [])
        if not d.get("is_base") and d.get("patch_num") and d["patch_num"] > base_max
    }

    pkg_id    = pkg.get("package_id", "PKG")
    truncated = gap > MAX_STUB_ENTRIES

    lines = [
        "\n\n---\n\n",
        "## Patch History\n\n",
        f"Base document covers through `{pkg_id}*{base_max}`. "
        f"VDL library max: `{pkg_id}*{lib_max}` (gap: {gap}).\n",
        "FORUM is authoritative — true gap may be larger.\n\n",
        "| Tag | Meaning |\n|---|---|\n",
        "| `[VDL]` | Content from VDL change-pages document |\n",
        "| `[FORUM]` | FORUM patch description (LLM-drafted, human-reviewed) |\n",
        "| `[UNDOCUMENTED]` | No source available yet |\n\n---\n\n",
    ]

    if truncated:
        lines.append(
            f"> **Note:** Gap is {gap} patches. Showing first {MAX_STUB_ENTRIES}. "
            f"Expand after FORUM integration.\n\n---\n\n"
        )

    shown = 0
    for p in range(base_max + 1, lib_max + 1):
        if truncated and shown >= MAX_STUB_ENTRIES:
            remaining = lib_max - (base_max + shown)
            lines.append(
                f"<!-- {remaining} patches ({pkg_id}*{base_max + shown + 1}"
                f"–*{lib_max}) omitted — expand after FORUM integration -->\n"
            )
            break

        if p in vdl_patches:
            lines += [
                f"### `{pkg_id}*{p}` — [VDL]\n\n",
                f"- **Source:** _{vdl_patches[p]}_\n",
                f"- **Released:** <!-- date from VDL document -->\n",
                f"- **Changes:** <!-- merge_change_pages.py will populate -->\n\n---\n\n",
            ]
        else:
            lines += [
                f"### `{pkg_id}*{p}` — [UNDOCUMENTED]\n\n",
                f"- **Source:** No VDL or FORUM data yet\n",
                f"- **Released:** <!-- date from FORUM -->\n",
                f"- **Changes:** <!-- LLM-draft from FORUM patch description -->\n\n---\n\n",
            ]
        shown += 1

    return "".join(lines)


# =============================================================================
# 4. CONVERSION
# =============================================================================

def convert_document(doc: dict, pkg: dict, force: bool, repo_root: Path) -> dict:
    local_path_str = doc.get("local_path")
    if not local_path_str:
        doc["convert_status"] = "skipped-no-file"
        return doc

    local_path = (repo_root / local_path_str).resolve()
    if not local_path.exists():
        print(f"  [MISSING] {local_path_str}")
        doc["convert_status"] = "skipped-no-file"
        doc["convert_error"]  = f"not found: {local_path}"
        return doc

    out_path = (repo_root / doc["out_path"]).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if out_path.exists() and not force:
        print(f"  [CACHED]  {doc['out_path']}")
        doc["convert_status"] = "done"
        return doc

    print(f"  [CONVERT] {local_path_str}")

    if not DOCLING_AVAILABLE:
        fm  = build_frontmatter(doc, pkg, {})
        out = (
            frontmatter_str(fm)
            + f"# {doc.get('title', 'Document')}\n\n"
            + f"> ⚠️ Scaffold placeholder — Docling conversion required.\n"
            + f"> Source: `{local_path_str}`\n"
        )
        if doc.get("is_base"):
            out += build_patch_history(doc, pkg)
        out_path.write_text(out, encoding="utf-8")
        print(f"            ↳ scaffold → {doc['out_path']}")
        doc["convert_status"] = "scaffold"
        return doc

    try:
        converter   = DocumentConverter()
        result      = converter.convert(str(local_path))
        docling_doc = result.document

        # Archive lossless DoclingDocument JSON
        archive_json = out_path.parent / "archive" / (out_path.stem + ".json")
        archive_json.parent.mkdir(parents=True, exist_ok=True)
        archive_json.write_text(docling_doc.model_dump_json(indent=2), encoding="utf-8")

        raw_md       = docling_doc.export_to_markdown()
        md, rev_info = apply_transforms(raw_md, pkg_id=pkg.get("package_id", ""))
        fm           = build_frontmatter(doc, pkg, rev_info)
        full         = frontmatter_str(fm) + md

        if doc.get("is_base"):
            full += build_patch_history(doc, pkg)

        out_path.write_text(full, encoding="utf-8")
        print(f"            ↳ done → {doc['out_path']}")
        doc["convert_status"] = "done"
        doc["archive_json"]   = str(archive_json.relative_to(repo_root))

    except Exception as e:
        print(f"            ↳ ERROR: {e}")
        doc["convert_status"] = "error"
        doc["convert_error"]  = str(e)

    return doc


# =============================================================================
# 5. MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest",  default="scripts/manifest.json")
    parser.add_argument("--pkg",       default=None,
                        help="Comma-separated package keys to process (case-insensitive), e.g. PSB,MAG,YS")
    parser.add_argument("--base-only", action="store_true")
    parser.add_argument("--force",     action="store_true")
    args = parser.parse_args()

    manifest_path = Path(args.manifest).resolve()
    repo_root     = manifest_path.parent.parent

    with open(manifest_path, encoding="utf-8") as f:
        manifest = json.load(f)

    # Normalise guides-manifest (flat documents list) to pilot packages shape.
    # Guides docs use: app_code, filename, local_path, category, fetch_status.
    # We synthesise a minimal pkg dict per app_code so convert_document() works
    # unchanged. Fields not present in guides manifest are set to safe defaults.
    if "documents" in manifest and "packages" not in manifest:
        pkgs: dict = {}
        for doc in manifest["documents"]:
            key = doc.get("app_code", "UNKNOWN").lower()
            if key not in pkgs:
                pkgs[key] = {
                    "package_id":       doc.get("app_code", "UNKNOWN"),
                    "app_name":         doc.get("app_name", doc.get("app_code", "")),
                    "section":          doc.get("section", ""),
                    "base_max_patch":   None,
                    "library_max_patch": None,
                    "documents":        [],
                }
            # Map guides fields → ingest fields
            d = dict(doc)
            d.setdefault("docx_filename", doc.get("filename", ""))
            d.setdefault("title",         doc.get("filename", "").replace("_", " "))
            d.setdefault("doc_class",     doc.get("category", "unknown"))
            d.setdefault("is_base",       False)
            # out_path: docs/<PKG>/<stem>.md  (mirrors fetch output layout)
            fname  = doc.get("filename", "unknown.docx")
            stem   = Path(fname).stem
            app    = doc.get("app_code", "UNKNOWN")
            d.setdefault("out_path", f"docs/{app}/{stem}.md")
            # Reconstruct local_path from known fetch layout if absent
            if not d.get("local_path") and d.get("fetch_status","").startswith("ok"):
                d["local_path"] = f"docs/{app}/{fname}"
            pkgs[key]["documents"].append(d)
        manifest = {"packages": pkgs}

    counts = {"done": 0, "scaffold": 0, "skip": 0, "error": 0}
    pkg_filter = {p.strip().lower() for p in args.pkg.split(",")} if args.pkg else None

    for pkg_key, pkg in manifest["packages"].items():
        if pkg_filter and pkg_key.lower() not in pkg_filter:
            continue

        print(f"\n{'='*60}")
        print(f"  Package: {pkg_key} ({pkg['package_id']})")
        print(f"{'='*60}")

        for i, doc in enumerate(pkg["documents"]):
            if args.base_only and not doc.get("is_base"):
                continue
            if doc.get("fetch_status") not in ("ok-docx", "ok-pdf", "ok"):
                if args.base_only:
                    print(f"  [NO-FETCH] {doc.get('title','?')[:55]}")
                continue

            updated = convert_document(doc, pkg, args.force, repo_root)
            pkg["documents"][i] = updated
            s = updated.get("convert_status", "skip")
            counts[s if s in counts else "skip"] += 1

    print(f"\nConversion: {counts['done']} done | {counts.get('scaffold',0)} scaffold "
          f"| {counts['skip']} skipped | {counts['error']} errors")

    # Only write back pilot manifests (packages format).
    # guides-manifest.json is owned by fetch_guides.py; we normalised it
    # in-memory only, so re-opening the original to check is safe.
    with open(manifest_path, encoding="utf-8") as f:
        original = json.load(f)
    if "packages" in original:
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2)
        print(f"Manifest updated: {manifest_path}")


if __name__ == "__main__":
    main()