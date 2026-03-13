#!/usr/bin/env python3
"""
fetch_guides.py — Download docs listed in guides-manifest.json.

The VDL inventory lists .docx URLs, but many files are only available as .pdf
at the same path. This script tries the .docx URL first; on 404 it retries
with the extension changed to .pdf and saves under the .pdf filename.

Usage:
    python fetch_guides.py                        # fetch all pending
    python fetch_guides.py --pkg PXRM             # one package only
    python fetch_guides.py --cat release-notes    # one category only
    python fetch_guides.py --dry-run              # print plan, no downloads
    python fetch_guides.py --force                # re-fetch already-fetched docs

Output layout:
    docs/
      CPRS/   OR_3_0_377_RN.docx  (or .pdf when only PDF resolved)
      GMTS/   hsum_2_7_um.pdf
      PXRM/   pxrm_2_4_um.docx
      ...

Manifest fields updated per document:
    fetch_status:  "ok" | "error" | "skipped"
    fetched_ext:   "docx" | "pdf"    (actual file type saved; only on "ok")
    fetched_url:   URL that succeeded (only on "ok")
    fetch_error:   error message     (only on "error")
    fetch_size:    bytes written      (only on "ok")
    fetch_time:    ISO timestamp      (only on "ok")

Rate:  1.5 s between requests (same as fetch.py)
"""

import argparse
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

try:
    import requests
    from requests.exceptions import HTTPError
except ImportError:
    sys.exit("requests not installed — run: pip install requests")

SCRIPT_DIR = Path(__file__).parent
MANIFEST   = SCRIPT_DIR / "guides-manifest.json"
DOCS_DIR   = SCRIPT_DIR.parent / "docs"
DELAY      = 1.5
HEADERS    = {"User-Agent": "vdl-fetch/1.0"}


def load_manifest():
    with open(MANIFEST) as f:
        return json.load(f)


def save_manifest(data):
    with open(MANIFEST, "w") as f:
        json.dump(data, f, indent=2)


def try_get(url):
    resp = requests.get(url, timeout=60, headers=HEADERS)
    resp.raise_for_status()
    return resp


def pdf_url(docx_url):
    if docx_url.lower().endswith(".docx"):
        return docx_url[:-5] + ".pdf"
    return None


def fetch_doc(entry, docs_dir, force=False, dry_run=False):
    pkg      = entry["app_code"]
    filename = entry["filename"]
    url_docx = entry.get("doc_url") or entry.get("url", "")
    dest_dir = docs_dir / pkg

    prior_ext  = entry.get("fetched_ext", "docx")
    saved_name = Path(filename).stem + "." + prior_ext
    dest       = dest_dir / saved_name

    if entry.get("fetch_status") == "ok" and dest.exists() and not force:
        return "skipped"

    if dry_run:
        url_pdf = pdf_url(url_docx)
        print(f"    will try: {url_docx}")
        if url_pdf:
            print(f"    fallback: {url_pdf}")
        return "dry-run"

    dest_dir.mkdir(parents=True, exist_ok=True)

    resp         = None
    resolved_url = url_docx
    resolved_ext = "docx"

    try:
        resp = try_get(url_docx)
    except HTTPError as e:
        if e.response is not None and e.response.status_code == 404:
            url_fallback = pdf_url(url_docx)
            if url_fallback:
                try:
                    resp         = try_get(url_fallback)
                    resolved_url = url_fallback
                    resolved_ext = "pdf"
                except Exception as e2:
                    entry["fetch_status"] = "error"
                    entry["fetch_error"]  = f"docx 404; pdf also failed: {e2}"
                    return "error"
            else:
                entry["fetch_status"] = "error"
                entry["fetch_error"]  = str(e)
                return "error"
        else:
            entry["fetch_status"] = "error"
            entry["fetch_error"]  = str(e)
            return "error"
    except Exception as e:
        entry["fetch_status"] = "error"
        entry["fetch_error"]  = str(e)
        return "error"

    save_path = dest_dir / (Path(filename).stem + "." + resolved_ext)
    save_path.write_bytes(resp.content)

    entry["fetch_status"] = "ok"
    entry["fetched_ext"]  = resolved_ext
    entry["fetched_url"]  = resolved_url
    entry["fetch_size"]   = len(resp.content)
    entry["fetch_time"]   = datetime.now(timezone.utc).isoformat()
    entry.pop("fetch_error", None)
    return "ok"


def main():
    parser = argparse.ArgumentParser(
        description="Fetch VDL docs listed in guides-manifest.json"
    )
    parser.add_argument("--pkg",     help="Filter by app_code (e.g. PXRM)")
    parser.add_argument("--cat",     help="Filter by category (e.g. release-notes)")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force",   action="store_true")
    args = parser.parse_args()

    data = load_manifest()
    docs = data["documents"]

    if args.pkg:
        docs = [d for d in docs if d["app_code"] == args.pkg]
    if args.cat:
        docs = [d for d in docs if d["category"] == args.cat]

    pending = docs if args.force else [
        d for d in docs if d.get("fetch_status") != "ok"
    ]

    total    = len(pending)
    est_mins = (total * DELAY) / 60

    print("guides-manifest.json — fetch plan")
    print(f"  Documents to fetch : {total}")
    print(f"  Estimated time     : {est_mins:.1f} min @ {DELAY}s delay")
    print(f"  Output directory   : {DOCS_DIR}")
    print(f"  .docx->pdf fallback: enabled")
    if args.dry_run:
        print(f"  Mode               : DRY RUN\n")
    print()

    if total == 0:
        print("Nothing to fetch.")
        return

    counts = {"ok": 0, "error": 0, "skipped": 0, "dry-run": 0}

    for i, entry in enumerate(pending, 1):
        pkg    = entry["app_code"]
        fname  = entry["filename"]
        cat = entry.get("category", "user-manual")
        prefix = f"[{i:>3}/{total}] [{pkg:<6}] [{cat:<14}]"

        result = fetch_doc(entry, DOCS_DIR, force=args.force, dry_run=args.dry_run)
        counts[result] = counts.get(result, 0) + 1

        if result == "ok":
            ext     = entry.get("fetched_ext", "docx")
            size_kb = entry.get("fetch_size", 0) // 1024
            saved   = Path(fname).stem + "." + ext
            flag    = " [PDF]" if ext == "pdf" else ""
            print(f"{prefix} ok{flag:<6} {saved}  ({size_kb} KB)")
        elif result == "error":
            print(f"{prefix} ERROR    {fname}  — {entry.get('fetch_error', '')}")
        elif result == "skipped":
            print(f"{prefix} skipped  {fname}")
        else:
            print(f"{prefix} {result:<8} {fname}")

        if not args.dry_run:
            save_manifest(data)

        if result not in ("skipped", "dry-run") and i < total:
            time.sleep(DELAY)

    pdf_count  = sum(1 for d in data["documents"]
                     if d.get("fetch_status") == "ok" and d.get("fetched_ext") == "pdf")
    docx_count = sum(1 for d in data["documents"]
                     if d.get("fetch_status") == "ok" and d.get("fetched_ext") == "docx")

    print(f"\nDone.  ok={counts['ok']}  error={counts['error']}  skipped={counts['skipped']}")
    print(f"       saved as docx={docx_count}  pdf={pdf_count}")

    if counts["error"]:
        print("\nFailed documents:")
        for d in data["documents"]:
            if d.get("fetch_status") == "error":
                print(f"  {d['filename']}  — {d.get('fetch_error', '')}")


if __name__ == "__main__":
    main()
