#!/usr/bin/env python3
"""
fetch.py — Download source documents for vista-docs pilot packages.

Each manifest entry represents ONE document (docx + pdf pair already collapsed).
Strategy:
  1. Try docx_url first
  2. On 404/403/error, fall back to pdf_url
  3. Save to raw/<pkg>/<filename>
  4. Update manifest fetch_status and local_path

Usage:
    python3 fetch.py --manifest scripts/manifest.json [--pkg cprs] [--dry-run]
"""

import json
import time
import argparse
import sys
from pathlib import Path

try:
    import requests
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
except ImportError:
    print("ERROR: requests not installed. Run: pip install requests")
    sys.exit(1)

BASE_RAW_DIR = Path("raw")

HEADERS = {
    "User-Agent": (
        "vista-docs-pilot/0.1 (open-source VDL modernization pilot; "
        "github.com/vista-docs) Mozilla/5.0"
    ),
    "Accept": "application/octet-stream,application/pdf,*/*",
}


def make_session() -> requests.Session:
    session = requests.Session()
    retry = Retry(total=3, backoff_factor=2, status_forcelist=[429, 500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    session.headers.update(HEADERS)
    return session


def fetch_document(doc: dict, pkg_key: str, session: requests.Session,
                   dry_run: bool, delay: float) -> dict:
    """
    Fetch one document. Try docx first, fall back to pdf.
    Returns updated doc dict.
    """
    out_dir = BASE_RAW_DIR / pkg_key
    out_dir.mkdir(parents=True, exist_ok=True)

    # Build attempt list: (format, url, save_filename)
    attempts = []
    if doc.get("docx_url") and doc.get("docx_filename"):
        attempts.append(("docx", doc["docx_url"], doc["docx_filename"]))
    if doc.get("pdf_url") and doc.get("pdf_filename"):
        attempts.append(("pdf",  doc["pdf_url"],  doc["pdf_filename"]))

    if not attempts:
        doc["fetch_status"] = "skipped"
        doc["fetch_error"]  = "no URLs in manifest"
        return doc

    if dry_run:
        fmt, url, fname = attempts[0]
        print(f"  [DRY-RUN] {fname} ({fmt}) ← {url}")
        doc["fetch_status"] = "dry-run"
        return doc

    for fmt, url, save_name in attempts:
        local_path = out_dir / save_name

        # Already cached?
        if local_path.exists() and local_path.stat().st_size > 1024:
            print(f"  [CACHED]  {save_name} ({local_path.stat().st_size // 1024} KB)")
            doc["fetch_status"] = f"ok-{fmt}"
            doc["local_path"]   = str(local_path)
            doc["fetch_format"] = fmt
            return doc

        try:
            print(f"  [FETCH]   {save_name} ← {url}")
            resp = session.get(url, timeout=30, stream=True)

            if resp.status_code == 200:
                ct = resp.headers.get("content-type", "")
                if "text/html" in ct and fmt == "docx":
                    print(f"            ↳ got HTML (not a .docx) — trying PDF")
                    continue

                with open(local_path, "wb") as f:
                    for chunk in resp.iter_content(chunk_size=65536):
                        f.write(chunk)

                size_kb = local_path.stat().st_size // 1024
                print(f"            ↳ saved {size_kb} KB [{fmt}]")
                doc["fetch_status"] = f"ok-{fmt}"
                doc["local_path"]   = str(local_path)
                doc["fetch_format"] = fmt
                time.sleep(delay)
                return doc

            elif resp.status_code in (403, 404):
                print(f"            ↳ HTTP {resp.status_code} — trying next format")
                time.sleep(0.3)
                continue

            else:
                print(f"            ↳ HTTP {resp.status_code} — unexpected")
                continue

        except requests.exceptions.RequestException as e:
            print(f"            ↳ network error: {e}")
            continue

    # All attempts failed
    tried = ", ".join(f[0] for f in attempts)
    doc["fetch_status"] = "error"
    doc["fetch_error"]  = f"all formats failed ({tried}): {doc.get('docx_filename','?')}"
    print(f"  [ERROR]   {doc.get('docx_filename', doc.get('pdf_filename', '?'))} — all attempts failed")
    return doc


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", default="scripts/manifest.json")
    parser.add_argument("--pkg",      default=None)
    parser.add_argument("--dry-run",  action="store_true")
    parser.add_argument("--delay",    type=float, default=1.5)
    args = parser.parse_args()

    with open(args.manifest, encoding="utf-8") as f:
        manifest = json.load(f)

    session = make_session()
    counts = {"ok": 0, "error": 0, "skip": 0}

    for pkg_key, pkg in manifest["packages"].items():
        if args.pkg and pkg_key != args.pkg:
            continue

        print(f"\n{'='*60}")
        print(f"  Package: {pkg_key} ({pkg['package_id']})")
        print(f"  Documents: {pkg['doc_counts']['total']}")
        print(f"{'='*60}")

        for i, doc in enumerate(pkg["documents"]):
            # Skip already-fetched
            if doc.get("fetch_status", "pending") in ("ok-docx", "ok-pdf"):
                print(f"  [DONE]    {doc.get('docx_filename') or doc.get('pdf_filename')} (cached)")
                counts["ok"] += 1
                continue

            updated = fetch_document(doc, pkg_key, session, args.dry_run, args.delay)
            pkg["documents"][i] = updated

            s = updated["fetch_status"]
            if s.startswith("ok"):
                counts["ok"] += 1
            elif s == "skipped":
                counts["skip"] += 1
            elif s not in ("dry-run",):
                counts["error"] += 1

    if not args.dry_run:
        with open(args.manifest, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2)
        print(f"\nManifest updated: {args.manifest}")

    print(f"\nFetch summary: {counts['ok']} ok | {counts['error']} errors | {counts['skip']} skipped")


if __name__ == "__main__":
    main()
