#!/usr/bin/env python3
"""
rebuild_gap_entries.py — Upsert gap-package entries into guides-manifest.json
from the authoritative vdl_inventory.csv.

Usage:
    python scripts/rebuild_gap_entries.py [--dry-run]

What it does:
    1. Reads vdl_inventory.csv (must be in scripts/)
    2. Filters to active, .docx, no-Archive-in-URL rows for the gap packages
    3. For each target filename:
       - If already in guides-manifest.json with fetch_status=ok → skip (preserve)
       - If present with error/pending → replace with fresh entry from inventory
       - If absent → insert
    4. Updates meta.packages and meta.total_documents
    5. Writes guides-manifest.json in place

Gap packages and target filenames (derived from inventory, active only):
    PSB  — PSB_3_0_P131_tm.docx        (Technical Manual, PSB*3*131)
    MAG  — IMGTECHMAN_F.docx            (Technical Manual)
           MAG_Display_User_Manual.docx (Clinical Display UM)
    YS   — YS_MHA_UM.docx              (Phase 3 User Manual)
           ys_mha_tm.docx              (Phase 3 Technical Manual)
           mha_web_um.docx             (Web UM, YS*5.01*265)
    PCMM — pcmmug.docx                 (PCMM User Manual)
           pcmmmhtcug.docx             (MHTC User Manual)
    WEBP — pcmm_web_ug.docx            (PCMM Web User Guide)
           sd_53_603_tm.docx           (PCMM Web Technical Manual)
"""

import argparse
import csv
import json
import sys
from pathlib import Path

SCRIPT_DIR    = Path(__file__).parent
INVENTORY_CSV = SCRIPT_DIR / "vdl_inventory.csv"
MANIFEST_JSON = SCRIPT_DIR / "guides-manifest.json"

# ---------------------------------------------------------------------------
# Target filenames per gap package — derived from vdl_inventory active rows.
# Extend this dict when adding future gap packages.
# ---------------------------------------------------------------------------
GAP_TARGETS: dict[str, list[str]] = {
    "PSB":  ["PSB_3_0_P131_tm.docx"],
    "MAG":  ["IMGTECHMAN_F.docx", "MAG_Display_User_Manual.docx"],
    "YS":   ["YS_MHA_UM.docx", "ys_mha_tm.docx", "mha_web_um.docx"],
    "PCMM": ["pcmmug.docx", "pcmmmhtcug.docx"],
    "WEBP": ["pcmm_web_ug.docx", "sd_53_603_tm.docx"],
}

# Map inventory doc_type keywords → manifest category
def infer_category(doc_type: str) -> str:
    dt = doc_type.lower()
    if any(x in dt for x in ["technical manual", "security guide", "security manual"]):
        return "technical-manual"
    if any(x in dt for x in ["release note", "release notes"]):
        return "release-notes"
    if any(x in dt for x in ["installation", "install guide", "deployment", "dibrg"]):
        return "setup-config"
    return "user-manual"


def load_inventory(path: Path) -> dict[str, dict]:
    """Return {filename: row} for all active .docx rows, no Archive in URL."""
    index: dict[str, dict] = {}
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            if (
                row["app_status"].lower() == "active"
                and row["file_ext"].lower() == ".docx"
                and "Archive" not in row.get("doc_url", "")
            ):
                index[row["filename"]] = row
    return index


def build_entry(inv_row: dict) -> dict:
    return {
        "filename":     inv_row["filename"],
        "app_code":     inv_row["app_code"],
        "app_name":     inv_row["app_name"],
        "doc_type":     inv_row["doc_title"],
        "doc_url":      inv_row["doc_url"],
        "category":     infer_category(inv_row["doc_title"]),
        "fetch_status": "pending",
        "ingest_status":"pending",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true",
                        help="Print plan without modifying files")
    args = parser.parse_args()

    if not INVENTORY_CSV.exists():
        sys.exit(f"ERROR: inventory not found at {INVENTORY_CSV}")
    if not MANIFEST_JSON.exists():
        sys.exit(f"ERROR: manifest not found at {MANIFEST_JSON}")

    inventory = load_inventory(INVENTORY_CSV)
    print(f"Inventory loaded: {len(inventory)} active .docx rows")

    with open(MANIFEST_JSON) as f:
        manifest = json.load(f)

    docs = manifest["documents"]

    # Index existing manifest entries by filename (last wins on dupe)
    existing: dict[str, int] = {d["filename"]: i for i, d in enumerate(docs)}

    inserted = []
    replaced = []
    skipped  = []
    missing  = []   # in target list but not in inventory

    for app_code, filenames in GAP_TARGETS.items():
        for fn in filenames:
            inv_row = inventory.get(fn)
            if inv_row is None:
                missing.append((app_code, fn))
                continue

            new_entry = build_entry(inv_row)

            if fn in existing:
                idx = existing[fn]
                current = docs[idx]
                if current.get("fetch_status") == "ok":
                    skipped.append(fn)
                    continue
                # Replace error/pending with fresh entry; preserve any ok fields
                docs[idx] = new_entry
                replaced.append(fn)
            else:
                docs.append(new_entry)
                existing[fn] = len(docs) - 1
                inserted.append(fn)

    # Update meta
    all_packages = list(dict.fromkeys(
        manifest["meta"].get("packages", []) +
        [c for c in GAP_TARGETS if c not in manifest["meta"].get("packages", [])]
    ))
    manifest["meta"]["packages"] = all_packages
    manifest["meta"]["total_documents"] = len(docs)

    # Report
    print(f"\nGap entry reconciliation:")
    print(f"  Inserted : {len(inserted)}")
    for fn in inserted:
        print(f"    + {fn}")
    print(f"  Replaced : {len(replaced)}")
    for fn in replaced:
        print(f"    ~ {fn}")
    print(f"  Skipped  : {len(skipped)}  (already fetch_status=ok)")
    for fn in skipped:
        print(f"    = {fn}")
    if missing:
        print(f"  NOT IN INVENTORY ({len(missing)}) — cannot add:")
        for app, fn in missing:
            print(f"    ! [{app}] {fn}")

    print(f"\nManifest total_documents: {manifest['meta']['total_documents']}")

    if args.dry_run:
        print("\n[dry-run] No files written.")
        return

    with open(MANIFEST_JSON, "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"\nWrote {MANIFEST_JSON}")


if __name__ == "__main__":
    main()
