#!/usr/bin/env python3
"""
Cross-reference: VDL enriched inventory vs VistA Monograph.

Checks:
  1. VDL link validity (monograph links → inventory app_url)
  2. App name consistency (monograph app_name vs inventory app_name_full)
  3. Namespace consistency (monograph namespace vs inventory pkg_ns)
  4. Coverage gaps (inventory apps not in monograph, monograph apps not in inventory)
  5. VASI status vs inventory status

Writes: ~/data/vista-docs/survey/crossref_monograph.json
        ~/data/vista-docs/survey/crossref_monograph_report.txt
"""

from __future__ import annotations

import csv
import json
import textwrap
from collections import Counter, defaultdict
from pathlib import Path

INVENTORY_CSV = Path.home() / "data/vista-docs/inventory/vdl_inventory_enriched.csv"
MONOGRAPH_JSON = Path.home() / "data/vista-docs/survey/monograph_apps.json"
OUTPUT_DIR = Path.home() / "data/vista-docs/survey"

# ---------------------------------------------------------------------------
# Load
# ---------------------------------------------------------------------------


def load_inventory() -> tuple[list[dict], dict, dict, dict]:
    """Return (all_rows, active_by_url, all_by_url, name_by_url)."""
    with open(INVENTORY_CSV, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    active_docx = [
        r
        for r in rows
        if r["noise_type"] == "" and r["app_status"] == "active" and r["doc_format"] == "docx"
    ]

    active_by_url: dict[str, dict] = {}
    for r in active_docx:
        url = r["app_url"].rstrip("/")
        if url not in active_by_url:
            active_by_url[url] = r

    all_by_url: dict[str, dict] = {}
    for r in rows:
        if r["noise_type"] != "":
            continue
        url = r["app_url"].rstrip("/")
        # Prefer active row if available
        if url not in all_by_url or r["app_status"] == "active":
            all_by_url[url] = r

    return rows, active_by_url, all_by_url


def load_monograph() -> list[dict]:
    return json.loads(MONOGRAPH_JSON.read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------


def check_vdl_links(mono: list[dict], active_by_url: dict, all_by_url: dict) -> dict:
    matched, decommissioned, not_in_inv, no_link = [], [], [], []

    for r in mono:
        url = r["vdl_link"].rstrip("/")
        if not url:
            no_link.append(
                {
                    "mono_name": r["app_name"],
                    "namespace": r["namespace"],
                    "vasi_status": r["vasi_status"],
                }
            )
            continue
        if url in active_by_url:
            matched.append(r["app_name"])
        elif url in all_by_url:
            inv_row = all_by_url[url]
            decommissioned.append(
                {
                    "mono_name": r["app_name"],
                    "inv_name": inv_row["app_name_full"],
                    "inv_status": inv_row["app_status"],
                    "vdl_url": url,
                }
            )
        else:
            not_in_inv.append(
                {
                    "mono_name": r["app_name"],
                    "vdl_url": url,
                    "appid": url.split("appid=")[-1],
                }
            )

    return {
        "matched_count": len(matched),
        "decommissioned": decommissioned,
        "not_in_inventory": not_in_inv,
        "no_link": no_link,
    }


def check_names(mono: list[dict], active_by_url: dict) -> list[dict]:
    mismatches = []
    for r in mono:
        url = r["vdl_link"].rstrip("/")
        if not url or url not in active_by_url:
            continue
        inv_name = active_by_url[url]["app_name_full"]
        mono_name = r["app_name"]
        if inv_name.lower().strip() != mono_name.lower().strip():
            mismatches.append(
                {
                    "mono_name": mono_name,
                    "inv_name": inv_name,
                    "vdl_url": url,
                    "appid": url.split("appid=")[-1],
                }
            )
    return mismatches


def check_namespaces(mono: list[dict], active_by_url: dict) -> dict:
    matches, mismatches, one_missing = 0, [], 0
    inv_ns_by_url = {url: r["pkg_ns"] for url, r in active_by_url.items() if r["pkg_ns"]}
    for r in mono:
        url = r["vdl_link"].rstrip("/")
        mono_ns = r["namespace"].strip()
        skip_values = {"", "not applicable", "na", "n/a", "multiple namespace"}
        if not url or mono_ns.lower() in skip_values:
            one_missing += 1
            continue
        inv_ns = inv_ns_by_url.get(url, "")
        if not inv_ns:
            one_missing += 1
            continue
        if mono_ns == inv_ns:
            matches += 1
        else:
            mismatches.append(
                {
                    "mono_name": r["app_name"],
                    "mono_ns": mono_ns,
                    "inv_ns": inv_ns,
                    "vdl_url": url,
                    "note": _ns_note(mono_ns, inv_ns),
                }
            )
    return {"matches": matches, "mismatches": mismatches, "one_side_missing": one_missing}


def _ns_note(mono_ns: str, inv_ns: str) -> str:
    """Classify the type of namespace discrepancy."""
    # If monograph has multiple namespaces listed
    if "," in mono_ns or " or " in mono_ns.lower() or " and " in mono_ns.lower():
        return "multi-ns in monograph"
    return "single discrepancy"


def check_coverage(mono: list[dict], active_by_url: dict) -> dict:
    mono_urls = {r["vdl_link"].rstrip("/") for r in mono if r["vdl_link"]}
    inv_active_urls = set(active_by_url.keys())
    # Remove the monograph app itself from the gap (appid=239)
    monograph_self = "https://www.va.gov/vdl/application.asp?appid=239"
    inv_gap = inv_active_urls - mono_urls - {monograph_self}

    return {
        "in_inv_not_mono_count": len(inv_gap),
        "in_inv_not_mono": sorted(
            [
                {
                    "name": active_by_url[u]["app_name_full"],
                    "section": active_by_url[u]["section_code"],
                    "appid": u.split("appid=")[-1],
                    "url": u,
                }
                for u in inv_gap
            ],
            key=lambda x: x["name"],
        ),
    }


def check_vasi_status(mono: list[dict], active_by_url: dict) -> dict:
    """Monograph VASI status vs inventory active status."""
    issues = []
    for r in mono:
        url = r["vdl_link"].rstrip("/")
        if not url or url not in active_by_url:
            continue
        vasi = r["vasi_status"].strip()
        if vasi.lower() in ("inactive", "not a system"):
            issues.append(
                {
                    "mono_name": r["app_name"],
                    "vasi_status": vasi,
                    "inv_status": "active",
                    "namespace": r["namespace"],
                    "vdl_url": url,
                }
            )
    vasi_dist = dict(Counter(r["vasi_status"] for r in mono).most_common())
    return {"distribution": vasi_dist, "active_in_inv_but_inactive_in_mono": issues}


# ---------------------------------------------------------------------------
# Report formatting
# ---------------------------------------------------------------------------


def _wrap(text: str, indent: int = 4) -> str:
    prefix = " " * indent
    return textwrap.fill(text, width=100, initial_indent=prefix, subsequent_indent=prefix)


def build_report(results: dict) -> str:
    lines = []
    w = lines.append

    w("=" * 100)
    w("VDL ENRICHED INVENTORY  vs  VISTA MONOGRAPH — CROSS-REFERENCE REPORT")
    w("=" * 100)
    w("")

    # --- VDL Links ---
    vdl = results["vdl_links"]
    w(f"1. VDL LINK VALIDITY  ({vdl['matched_count']} matched of 187 monograph entries)")
    w("-" * 60)
    w(f"   Matched active inventory URL : {vdl['matched_count']}")
    w(f"   Link resolves to decommissioned app : {len(vdl['decommissioned'])}")
    w(f"   Link not found in inventory at all : {len(vdl['not_in_inventory'])}")
    w(f"   No VDL link (Not Applicable)       : {len(vdl['no_link'])}")
    w("")

    if vdl["decommissioned"]:
        w("   Monograph lists active apps whose VDL page is decommissioned in inventory:")
        for x in vdl["decommissioned"]:
            w(f"     • {x['mono_name'][:55]:<55}  → inv: {x['inv_name'][:40]} [{x['inv_status']}]")
    w("")

    if vdl["not_in_inventory"]:
        w("   VDL links in monograph not found anywhere in inventory:")
        for x in vdl["not_in_inventory"]:
            w(f"     • {x['mono_name'][:55]:<55}  appid={x['appid']}")
    w("")

    # --- Names ---
    names = results["name_mismatches"]
    w(f"2. APP NAME CONSISTENCY  ({len(names)} mismatches out of 142 matched entries)")
    w("-" * 60)
    w("   Note: Most are minor formatting differences (punctuation, 'Pharmacy:' prefix,")
    w("   acronym expansion).  Substantive ones flagged below.")
    w("")
    for x in names:
        mono_n = x["mono_name"][:48]
        inv_n = x["inv_name"][:48]
        if mono_n.lower().replace(" ", "") != inv_n.lower().replace(" ", ""):
            w(f"     MONO: {mono_n}")
            w(f"     INV:  {inv_n}")
            w("")

    # --- Namespaces ---
    ns = results["namespaces"]
    w(f"3. NAMESPACE CONSISTENCY  ({ns['matches']} match, {len(ns['mismatches'])} mismatch)")
    w("-" * 60)
    for x in ns["mismatches"]:
        w(f"     {x['mono_name'][:48]:<48}  MONO={x['mono_ns']:<20}  INV={x['inv_ns']}")
    w("")

    # --- Coverage ---
    cov = results["coverage"]
    w(f"4. COVERAGE GAPS  ({cov['in_inv_not_mono_count']} active inventory apps not in monograph)")
    w("-" * 60)
    by_section: dict = defaultdict(list)
    for x in cov["in_inv_not_mono"]:
        by_section[x["section"]].append(x["name"])
    for section in ("CLI", "FIN", "GUI", "INF"):
        apps = by_section.get(section, [])
        if apps:
            w(f"   [{section}]  {len(apps)} apps:")
            for name in apps:
                w(f"          {name}")
    w("")

    # --- VASI status ---
    vs = results["vasi_status"]
    w("5. VASI STATUS DISTRIBUTION")
    w("-" * 60)
    for status, n in vs["distribution"].items():
        w(f"   {n:4d}  {status}")
    w("")
    issues = vs["active_in_inv_but_inactive_in_mono"]
    if issues:
        w(f"   Apps active in VDL inventory but Inactive/Not-A-System in monograph: {len(issues)}")
        for x in issues:
            w(f"     • {x['mono_name'][:55]:<55}  VASI={x['vasi_status']}")
    w("")

    w("=" * 100)
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    _, active_by_url, all_by_url = load_inventory()
    mono = load_monograph()

    results = {
        "vdl_links": check_vdl_links(mono, active_by_url, all_by_url),
        "name_mismatches": check_names(mono, active_by_url),
        "namespaces": check_namespaces(mono, active_by_url),
        "coverage": check_coverage(mono, active_by_url),
        "vasi_status": check_vasi_status(mono, active_by_url),
    }

    report = build_report(results)
    print(report)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "crossref_monograph_report.txt").write_text(report, encoding="utf-8")
    (OUTPUT_DIR / "crossref_monograph.json").write_text(
        json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"\nWrote {OUTPUT_DIR}/crossref_monograph_report.txt")
    print(f"Wrote {OUTPUT_DIR}/crossref_monograph.json")
