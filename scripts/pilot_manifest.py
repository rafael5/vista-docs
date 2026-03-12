#!/usr/bin/env python3
"""
pilot_manifest.py — Build processing manifest for vista-docs pilot packages.

Reads vdl_inventory.csv, filters to the 4 pilot packages, collapses
.docx/.pdf row pairs into single manifest entries (both URLs preserved),
classifies each document, and writes manifest.json.

Usage:
    python3 pilot_manifest.py --inventory vdl_inventory.csv --out manifest.json
"""

import csv
import json
import re
from pathlib import Path
import argparse
from collections import defaultdict

# =============================================================================
# 1. PILOT PACKAGE DEFINITIONS
# =============================================================================

PILOT_PACKAGES = {
    "cprs": {
        "app_name":    "Computerized Patient Record System (CPRS)",
        "package_id":  "OR*3.0",
        "section":     "clinical",
        "doc_dir":     "docs/clinical/cprs",
        "archive_dir": "archive/clinical/cprs",
    },
    "tiu": {
        "app_name":    "CPRS: Text Integration Utility (TIU)",
        "package_id":  "TIU*1.0",
        "section":     "clinical",
        "doc_dir":     "docs/clinical/tiu",
        "archive_dir": "archive/clinical/tiu",
    },
    "hl7": {
        "app_name":    "HL7 (VistA Messaging)",
        "package_id":  "HL*1.6",
        "section":     "infrastructure",
        "doc_dir":     "docs/infrastructure/hl7",
        "archive_dir": "archive/infrastructure/hl7",
    },
    "adt": {
        "app_name":    "Admission Discharge Transfer (ADT)",
        "package_id":  "DG*5.3",
        "section":     "clinical",
        "doc_dir":     "docs/clinical/adt",
        "archive_dir": "archive/clinical/adt",
    },
}

# =============================================================================
# 2. CLASSIFICATION HELPERS
# =============================================================================

RN_RE          = re.compile(r'release.?note|_rn\.(?:pdf|docx)|_rn_|patch.?note', re.I)
INSTALL_RE     = re.compile(r'install|deploy|back.?out|rollback|dibr|dibrg|builds', re.I)
CHANGE_PAGE_RE = re.compile(r'change.?page|_cp\.(?:docx|pdf)', re.I)
SUPPLEMENT_RE  = re.compile(r'supplement|suppl|addend', re.I)
SETUP_RE       = re.compile(r'setup|config.*guide|configuration', re.I)
QUICK_REF_RE   = re.compile(r'quick.?ref|_qr\.(?:docx|pdf)|quick.?card', re.I)
PATCH_RE       = re.compile(r'[A-Z]+\*[\d.]+\*(\d+)', re.I)


def classify(doc_type: str, docx_filename: str, pdf_filename: str):
    """Return (doc_class, patch_num) for a collapsed document entry."""
    blob = f"{doc_type} {docx_filename} {pdf_filename}".lower()
    patches = [int(p) for p in PATCH_RE.findall(blob)]
    patch_num = max(patches) if patches else None

    if RN_RE.search(blob):          return "release-note",    patch_num
    if INSTALL_RE.search(blob):     return "install",          patch_num
    if QUICK_REF_RE.search(blob):   return "quick-ref",        patch_num
    if CHANGE_PAGE_RE.search(blob): return "change-page",      patch_num
    if SUPPLEMENT_RE.search(blob):  return "supplement",       patch_num
    if SETUP_RE.search(blob):       return "base-setup",       patch_num
    if "security" in blob:          return "base-security",    patch_num
    if "developer" in blob or "site manager" in blob:
                                    return "base-dev",         patch_num
    if "hl7" in blob and ("interface" in blob or "handbook" in blob):
                                    return "base-hl7",         patch_num
    if "implementation" in blob:    return "base-impl",        patch_num
    if "technical manual" in blob or re.search(r'_tm\.', blob):
                                    return "base-tm",          patch_num
    if ("user manual" in blob or "user guide" in blob
            or re.search(r'_um\.|_ug\.', blob)):
                                    return "base-um",          patch_num
    return "base-other", patch_num


def slug(text: str) -> str:
    s = re.sub(r'[^\w\s-]', '', text.lower())
    s = re.sub(r'[\s_]+', '-', s.strip())
    return re.sub(r'-+', '-', s)[:80]


# Stable base names — used when there is only ONE doc of this type per package
BASE_NAMES = {
    "base-tm":       "technical-manual",
    "base-um":       "user-manual",
    "base-dev":      "developer-manual",
    "base-hl7":      "hl7-interface",
    "base-security": "security-guide",
    "base-impl":     "implementation-guide",
    "base-setup":    "setup-guide",
}


# Explicit filename overrides for titles where slug generation produces noise.
# Key: exact doc_type_raw string. Value: desired output stem (no .md).
FILENAME_OVERRIDES = {
    "CPRS Setup Guide":                              "setup-guide-canonical",
    "HL7 HL*1.6 HLO System Manager Manual":          "hlo-system-manager-manual",
    "HL7 HL*1.6 HLO VMS Developer Manual":           "hlo-vms-developer-manual",
    "HL7 V. 1.6 Technical Manual":                   "technical-manual-legacy",
    "HL7 V. 1.6*161 Site Manager Developer Manual":  "developer-manual-p161",
    "HL7 V. 1.6*56 Site Manager Developer Manual":   "developer-manual-p56",
}


def output_filename(doc_class: str, title: str, patch_num, siblings: int) -> str:
    """
    Return output markdown filename.

    If siblings > 1 (multiple docs of this class in the package), always
    disambiguate:
      - by patch number if available:  setup-guide-p569.md
      - by title slug if no patch:     user-manual-bed-control.md

    If siblings == 1 use the stable canonical name: setup-guide.md
    """
    # Check explicit override first
    if title in FILENAME_OVERRIDES:
        return f"{FILENAME_OVERRIDES[title]}.md"

    base_name = BASE_NAMES.get(doc_class, slug(title))

    if siblings == 1:
        return f"{base_name}.md"

    if patch_num is not None:
        return f"{base_name}-p{patch_num}.md"

    # No patch number — extract a short disambiguator from the title.
    # Strategy: strip leading boilerplate (package names, version strings,
    # doc type words that duplicate base_name) and keep the meaningful tail.
    BOILERPLATE = re.compile(
        r"^(?:hl7|vista|pims|cprs|tiu|adt|or|dg|tiu)"
        r"(?:\s*[-*v]?\s*[\d.*]+)?"   # version/patch
        r"(?:\s+(?:version|v)\s*[\d.]+)?"
        r"\s*[-–]?\s*",
        re.I
    )
    TYPE_WORDS = re.compile(
        r"^(?:technical|user|developer|site\s+manager|security|implementation"
        r"|setup|configuration|quick\s+ref(?:erence)?)\s*(?:manual|guide|card)?\s*[-–]?\s*",
        re.I
    )
    stripped = BOILERPLATE.sub("", title)
    stripped = TYPE_WORDS.sub("", stripped).strip(" -–")
    disambig = slug(stripped) if stripped else slug(title)

    # Truncate to keep filenames sane
    disambig = disambig[:50].rstrip("-")
    return f"{base_name}-{disambig}.md" if disambig else f"{base_name}-{slug(title)[:40]}.md"


def out_subdir(doc_class: str, archive_dir: str, doc_dir: str) -> str:
    if doc_class.startswith("base-"):
        return doc_dir
    subdirs = {
        "change-page":  f"{archive_dir}/change-pages",
        "release-note": f"{archive_dir}/release-notes",
        "install":      f"{archive_dir}/install",
        "supplement":   f"{archive_dir}/supplements",
        "quick-ref":    f"{archive_dir}/quick-ref",
    }
    return subdirs.get(doc_class, f"{archive_dir}/other")


# =============================================================================
# 3. PAIR COLLAPSING
# =============================================================================

def collapse_pairs(rows: list[dict]) -> list[dict]:
    """
    Every document in the VDL appears as exactly two rows (docx + pdf).
    Group by (app_name, doc_type) and collapse each pair into one entry
    with both docx_url and pdf_url present.
    """
    groups: dict[tuple, list] = defaultdict(list)
    for r in rows:
        key = (r['app_name'].strip(), r['doc_type'].strip())
        groups[key].append(r)

    collapsed = []
    for (app_name, doc_type), grp in groups.items():
        docx_row = next((r for r in grp if r['file_ext'] == '.docx'), None)
        pdf_row  = next((r for r in grp if r['file_ext'] == '.pdf'),  None)
        base_row = docx_row or pdf_row  # use docx as primary if available

        collapsed.append({
            "app_name":    app_name,
            "doc_type_raw": doc_type,
            "title":       doc_type,   # doc_title col contains "DOCX"/"PDF" — doc_type has the real title
            "docx_url":    docx_row['doc_url'] if docx_row else None,
            "pdf_url":     pdf_row['doc_url']  if pdf_row  else None,
            "docx_filename": docx_row['filename'] if docx_row else None,
            "pdf_filename":  pdf_row['filename']  if pdf_row  else None,
        })

    return collapsed


# =============================================================================
# 4. MANIFEST BUILDER
# =============================================================================

def build_manifest(inventory_path: str) -> dict:
    manifest = {"generated_from": inventory_path, "packages": {}}

    raw_by_pkg: dict[str, list] = {k: [] for k in PILOT_PACKAGES}

    with open(inventory_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("app_status") != "active":
                continue
            for pkg_key, pkg_meta in PILOT_PACKAGES.items():
                if row["app_name"] == pkg_meta["app_name"]:
                    raw_by_pkg[pkg_key].append(row)
                    break

    for pkg_key, raw_rows in raw_by_pkg.items():
        meta = PILOT_PACKAGES[pkg_key]
        collapsed = collapse_pairs(raw_rows)
        docs = []

        # First pass: classify all docs
        classified = []
        for entry in collapsed:
            doc_class, patch_num = classify(
                entry["doc_type_raw"],
                entry["docx_filename"] or "",
                entry["pdf_filename"] or "",
            )
            classified.append((entry, doc_class, patch_num))

        # Count siblings per doc_class to detect collisions
        from collections import Counter as _Counter
        class_counts = _Counter(dc for _, dc, _ in classified if dc.startswith("base-"))

        for entry, doc_class, patch_num in classified:
            is_base   = doc_class.startswith("base-")
            siblings  = class_counts.get(doc_class, 1) if is_base else 1
            out_dir   = out_subdir(doc_class, meta["archive_dir"], meta["doc_dir"])
            out_md    = output_filename(doc_class, entry["title"], patch_num, siblings)
            out_path  = f"{out_dir}/{out_md}"

            docs.append({
                "title":         entry["title"],
                "doc_type_raw":  entry["doc_type_raw"],
                "docx_url":      entry["docx_url"],
                "pdf_url":       entry["pdf_url"],
                "docx_filename": entry["docx_filename"],
                "pdf_filename":  entry["pdf_filename"],
                "doc_class":     doc_class,
                "patch_num":     patch_num,
                "is_base":       is_base,
                "out_dir":       out_dir,
                "out_md":        out_md,
                "out_path":      out_path,
                "fetch_status":  "pending",
                "fetch_format":  None,
                "local_path":    None,
                "convert_status": None,
            })

        docs.sort(key=lambda d: (0 if d["is_base"] else 1, d["patch_num"] or 0))

        base_patches = [d["patch_num"] for d in docs if d["is_base"] and d["patch_num"]]
        all_patches  = [d["patch_num"] for d in docs if d["patch_num"]]

        manifest["packages"][pkg_key] = {
            "app_name":          meta["app_name"],
            "package_id":        meta["package_id"],
            "section":           meta["section"],
            "doc_dir":           meta["doc_dir"],
            "archive_dir":       meta["archive_dir"],
            "base_max_patch":    max(base_patches)  if base_patches else None,
            "library_max_patch": max(all_patches)   if all_patches  else None,
            "patch_gap":         (max(all_patches) - max(base_patches))
                                 if (base_patches and all_patches) else None,
            "doc_counts": {
                "total":         len(docs),
                "base":          sum(1 for d in docs if d["is_base"]),
                "change_pages":  sum(1 for d in docs if d["doc_class"] == "change-page"),
                "release_notes": sum(1 for d in docs if d["doc_class"] == "release-note"),
                "install":       sum(1 for d in docs if d["doc_class"] == "install"),
                "supplement":    sum(1 for d in docs if d["doc_class"] == "supplement"),
                "quick_ref":     sum(1 for d in docs if d["doc_class"] == "quick-ref"),
            },
            "documents": docs,
        }

    return manifest


# =============================================================================
# 5. ENTRY POINT
# =============================================================================

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inventory", required=True)
    parser.add_argument("--out", default="manifest.json")
    parser.add_argument(
        "--preserve-fetch-status",
        action="store_true",
        help="Merge fetch_status, local_path, fetch_format from an existing manifest "
             "so re-running after URL/naming fixes does not require re-fetching.",
    )
    args = parser.parse_args()

    manifest = build_manifest(args.inventory)

    if args.preserve_fetch_status and Path(args.out).exists():
        # Load prior manifest and re-apply fetch state by matching on docx_filename
        with open(args.out, encoding="utf-8") as f:
            prior = json.load(f)

        # Build lookup: docx_filename → fetch fields
        prior_fetch: dict[str, dict] = {}
        for pkg in prior.get("packages", {}).values():
            for doc in pkg.get("documents", []):
                key = doc.get("docx_filename") or doc.get("pdf_filename")
                if key and doc.get("fetch_status", "pending") != "pending":
                    prior_fetch[key] = {
                        "fetch_status": doc.get("fetch_status"),
                        "fetch_format": doc.get("fetch_format"),
                        "local_path":   doc.get("local_path"),
                        "fetch_error":  doc.get("fetch_error"),
                    }

        # Apply to new manifest
        merged = restored = 0
        for pkg in manifest["packages"].values():
            for doc in pkg["documents"]:
                key = doc.get("docx_filename") or doc.get("pdf_filename")
                if key and key in prior_fetch:
                    doc.update(prior_fetch[key])
                    restored += 1
                merged += 1

        print(f"Preserved fetch status: {restored}/{merged} documents restored.")

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    print(f"\nvista-docs pilot manifest → {args.out}\n")
    print(f"{'Package':<10} {'Docs':>6} {'Base':>6} {'CP':>6} {'RN':>6} {'Gap':>6}")
    print("-" * 44)
    for pkg_key, pkg in manifest["packages"].items():
        c   = pkg["doc_counts"]
        gap = pkg["patch_gap"] if pkg["patch_gap"] is not None else "?"
        print(f"{pkg_key:<10} {c['total']:>6} {c['base']:>6} "
              f"{c['change_pages']:>6} {c['release_notes']:>6} {gap:>6}")
    print()


if __name__ == "__main__":
    main()
