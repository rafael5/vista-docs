#!/usr/bin/env python3
"""
verify_corpus.py — Sanity-check core vista-docs pipeline files.

Checks:
  1. vdl_inventory.csv   — URL format, required columns, row counts
  2. manifest.json       — pilot manifest structure, URL format, fetch status
  3. guides-manifest.json — guides manifest structure, URL format, fetch status
  4. fetch.py            — presence and basic syntax
  5. fetch_guides.py     — presence and basic syntax
  6. pilot_manifest.py   — presence, no legacy fix_url(), correct inventory ref

Usage:
    python3 verify_corpus.py                  # checks all files relative to script dir
    python3 verify_corpus.py --scripts /path/to/scripts
    python3 verify_corpus.py --only inventory manifest
    python3 verify_corpus.py --fix-manifest   # patch /vdl/ into manifests in-place

Exit codes:
    0 — all checks passed
    1 — one or more failures
    2 — one or more warnings (no failures)
"""

import argparse
import ast
import csv
import io
import json
import re
import subprocess
import sys
from pathlib import Path

# =============================================================================
# 1. OUTPUT HELPERS
# =============================================================================

RESET  = "\033[0m"
BOLD   = "\033[1m"
RED    = "\033[31m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
CYAN   = "\033[36m"
GREY   = "\033[90m"

def _c(colour, text): return f"{colour}{text}{RESET}"

def header(title):
    print(f"\n{BOLD}{CYAN}{'='*60}{RESET}")
    print(f"{BOLD}{CYAN}  {title}{RESET}")
    print(f"{BOLD}{CYAN}{'='*60}{RESET}")

def ok(msg):    print(f"  {_c(GREEN,  '✓')} {msg}")
def warn(msg):  print(f"  {_c(YELLOW, '⚠')} {msg}")
def fail(msg):  print(f"  {_c(RED,    '✗')} {msg}")
def info(msg):  print(f"  {_c(GREY,   '·')} {msg}")

# =============================================================================
# 2. SHARED CHECKS
# =============================================================================

BAD_URL_PAT  = re.compile(r'https://www\.va\.gov/documents/')   # missing /vdl/
GOOD_URL_PAT = re.compile(r'https://www\.va\.gov/vdl/documents/')

def check_url(url: str) -> bool:
    """Return True if URL is correctly formed (has /vdl/)."""
    return bool(GOOD_URL_PAT.match(url))

def sample_bad_urls(urls: list[str], n: int = 3) -> list[str]:
    bad = [u for u in urls if not check_url(u)]
    return bad[:n]

# =============================================================================
# 3. INVENTORY CHECK
# =============================================================================

REQUIRED_INVENTORY_COLS = {
    'app_code', 'app_name', 'app_status', 'doc_type',
    'filename', 'file_ext', 'doc_url',
}

def check_inventory(path: Path) -> tuple[int, int]:
    """Returns (failures, warnings)."""
    failures = warnings = 0
    header(f"vdl_inventory.csv  [{path}]")

    if not path.exists():
        fail(f"File not found: {path}")
        return 1, 0

    with open(path, newline='', encoding='utf-8') as f:
        content = f.read()

    reader = csv.DictReader(io.StringIO(content))
    cols   = set(reader.fieldnames or [])
    rows   = list(reader)

    # Column check
    missing = REQUIRED_INVENTORY_COLS - cols
    if missing:
        fail(f"Missing columns: {', '.join(sorted(missing))}")
        failures += 1
    else:
        ok(f"All required columns present ({len(cols)} total)")

    # Row count
    total   = len(rows)
    active  = [r for r in rows if r.get('app_status') == 'active']
    docx    = [r for r in active if r.get('file_ext') == '.docx']
    info(f"Rows: {total} total  |  {len(active)} active  |  {len(docx)} active .docx")

    if total < 5000:
        warn(f"Row count ({total}) is lower than expected (~6900). File may be truncated.")
        warnings += 1
    else:
        ok(f"Row count plausible ({total})")

    # URL format
    all_urls  = [r.get('doc_url', '') for r in rows if r.get('doc_url')]
    bad_count = sum(1 for u in all_urls if BAD_URL_PAT.search(u))
    bad_good  = sum(1 for u in all_urls if GOOD_URL_PAT.match(u))
    bad_other = len(all_urls) - bad_count - bad_good

    if bad_count > 0:
        fail(f"{bad_count} URLs missing /vdl/ — run: sed -i '' "
             f"'s|va.gov/documents/|va.gov/vdl/documents/|g' {path.name}")
        for u in sample_bad_urls(all_urls):
            info(f"  e.g. {u}")
        failures += 1
    else:
        ok(f"All {bad_good} URLs have correct /vdl/ prefix")

    # Duplicate filenames within active .docx
    seen: dict[str, int] = {}
    for r in docx:
        fn = r.get('filename', '')
        seen[fn] = seen.get(fn, 0) + 1
    dups = {k: v for k, v in seen.items() if v > 1}
    if dups:
        warn(f"{len(dups)} duplicate .docx filenames across active rows")
        for fn, count in list(dups.items())[:3]:
            info(f"  {fn} ({count}x)")
        warnings += 1
    else:
        ok(f"No duplicate active .docx filenames")

    return failures, warnings

# =============================================================================
# 4. MANIFEST CHECK (shared logic for pilot + guides manifests)
# =============================================================================

def check_manifest_file(path: Path, manifest_type: str) -> tuple[int, int]:
    """Generic manifest checker. manifest_type: 'pilot' or 'guides'."""
    failures = warnings = 0
    header(f"{path.name}  [{path}]")

    if not path.exists():
        fail(f"File not found: {path}")
        return 1, 0

    try:
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        fail(f"Invalid JSON: {e}")
        return 1, 0

    ok("Valid JSON")

    # Extract documents list depending on manifest shape
    if manifest_type == 'guides':
        docs = data.get('documents', [])
        meta = data.get('meta', {})
        if not meta:
            warn("No 'meta' block found")
            warnings += 1
        else:
            ok(f"meta.total_documents = {meta.get('total_documents', '?')}")
    else:
        # Pilot manifest: nested under packages → pkg → documents
        docs = []
        packages = data.get('packages', {})
        if not packages:
            fail("No 'packages' key found in manifest")
            return 1, 0
        for pkg_key, pkg in packages.items():
            pkg_docs = pkg.get('documents', [])
            docs.extend(pkg_docs)
        ok(f"Packages: {list(packages.keys())}")

    info(f"Total document entries: {len(docs)}")

    if len(docs) == 0:
        fail("No documents found in manifest")
        return 1, 0

    # URL checks
    if manifest_type == 'guides':
        urls = [d.get('doc_url', '') for d in docs if d.get('doc_url')]
    else:
        # Pilot manifest uses docx_url / pdf_url
        urls = []
        for d in docs:
            for key in ('docx_url', 'pdf_url'):
                u = d.get(key)
                if u:
                    urls.append(u)

    bad_count = sum(1 for u in urls if BAD_URL_PAT.search(u))
    good_count = sum(1 for u in urls if GOOD_URL_PAT.match(u))

    if bad_count > 0:
        fail(f"{bad_count}/{len(urls)} URLs missing /vdl/ — use --fix-manifest to patch")
        for u in sample_bad_urls(urls):
            info(f"  e.g. {u}")
        failures += 1
    else:
        ok(f"All {good_count} URLs have correct /vdl/ prefix")

    # Fetch status summary
    statuses: dict[str, int] = {}
    for d in docs:
        s = d.get('fetch_status', 'unknown')
        statuses[s] = statuses.get(s, 0) + 1

    status_parts = '  |  '.join(f"{k}: {v}" for k, v in sorted(statuses.items()))
    info(f"fetch_status — {status_parts}")

    errors = [d.get('filename', d.get('docx_filename', '?'))
              for d in docs if d.get('fetch_status') == 'error']
    if errors:
        warn(f"{len(errors)} documents in error state")
        for fn in errors[:5]:
            info(f"  {fn}")
        if len(errors) > 5:
            info(f"  ... and {len(errors)-5} more")
        warnings += 1

    # Required fields per entry
    if manifest_type == 'guides':
        required_fields = {'filename', 'app_code', 'doc_url', 'category', 'fetch_status'}
    else:
        required_fields = {'docx_url', 'doc_class', 'fetch_status', 'out_path'}

    missing_fields: list[str] = []
    for d in docs:
        missing = required_fields - set(d.keys())
        if missing:
            name = d.get('filename') or d.get('docx_filename', '?')
            missing_fields.append(f"{name}: missing {', '.join(sorted(missing))}")

    if missing_fields:
        warn(f"{len(missing_fields)} entries missing required fields")
        for m in missing_fields[:3]:
            info(f"  {m}")
        warnings += 1
    else:
        ok(f"All entries have required fields")

    return failures, warnings

# =============================================================================
# 5. PYTHON SCRIPT CHECKS
# =============================================================================

def check_python_script(path: Path, checks: list[tuple]) -> tuple[int, int]:
    """
    checks: list of (description, pattern, expect_absent, fix_hint)
      expect_absent=True  → FAIL if pattern found
      expect_absent=False → FAIL if pattern not found
    """
    failures = warnings = 0
    header(f"{path.name}  [{path}]")

    if not path.exists():
        fail(f"File not found: {path}")
        return 1, 0

    source = path.read_text(encoding='utf-8')

    # Syntax check via ast
    try:
        ast.parse(source)
        ok("Python syntax valid")
    except SyntaxError as e:
        fail(f"Syntax error: {e}")
        failures += 1
        return failures, warnings

    # Subprocess syntax double-check
    result = subprocess.run(
        [sys.executable, '-m', 'py_compile', str(path)],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        fail(f"py_compile failed: {result.stderr.strip()}")
        failures += 1

    # Pattern checks
    for description, pattern, expect_absent, fix_hint in checks:
        found = bool(re.search(pattern, source))
        if expect_absent and found:
            fail(f"{description}")
            if fix_hint:
                info(f"  Fix: {fix_hint}")
            failures += 1
        elif not expect_absent and not found:
            fail(f"{description}")
            if fix_hint:
                info(f"  Fix: {fix_hint}")
            failures += 1
        else:
            ok(description)

    return failures, warnings

# =============================================================================
# 6. IN-PLACE URL FIX
# =============================================================================

def fix_manifest_urls(path: Path) -> int:
    """Patch /vdl/ into all doc_url fields in a JSON manifest. Returns count fixed."""
    if not path.exists():
        return 0
    content = path.read_text(encoding='utf-8')
    fixed   = content.replace(
        'https://www.va.gov/documents/',
        'https://www.va.gov/vdl/documents/',
    )
    count = content.count('https://www.va.gov/documents/')
    if count:
        path.write_text(fixed, encoding='utf-8')
    return count

# =============================================================================
# 7. MAIN
# =============================================================================

ALL_CHECKS = ['inventory', 'manifest', 'guides-manifest', 'fetch', 'fetch-guides', 'pilot-manifest']

def main():
    parser = argparse.ArgumentParser(
        description="Verify core vista-docs pipeline files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        '--scripts', type=Path,
        help="Path to vista-docs/scripts/ directory (default: directory of this script)",
    )
    parser.add_argument(
        '--only', nargs='+', choices=ALL_CHECKS, metavar='CHECK',
        help=f"Run only these checks: {', '.join(ALL_CHECKS)}",
    )
    parser.add_argument(
        '--fix-manifest', action='store_true',
        help="Patch missing /vdl/ in manifest.json and guides-manifest.json in-place",
    )
    args = parser.parse_args()

    scripts_dir  = args.scripts or Path(__file__).parent
    run_checks   = set(args.only) if args.only else set(ALL_CHECKS)

    total_failures = 0
    total_warnings = 0

    # ── Optional in-place fix ────────────────────────────────────────────────
    if args.fix_manifest:
        for mf in ['manifest.json', 'guides-manifest.json']:
            p = scripts_dir / mf
            n = fix_manifest_urls(p)
            if n:
                print(f"{_c(GREEN, '✓')} Patched {n} URLs in {mf}")
            else:
                print(f"{_c(GREY, '·')} No bad URLs found in {mf} (already correct)")

    # ── Inventory ────────────────────────────────────────────────────────────
    if 'inventory' in run_checks:
        f, w = check_inventory(scripts_dir / 'vdl_inventory.csv')
        total_failures += f; total_warnings += w

    # ── Pilot manifest ───────────────────────────────────────────────────────
    if 'manifest' in run_checks:
        f, w = check_manifest_file(scripts_dir / 'manifest.json', 'pilot')
        total_failures += f; total_warnings += w

    # ── Guides manifest ──────────────────────────────────────────────────────
    if 'guides-manifest' in run_checks:
        f, w = check_manifest_file(scripts_dir / 'guides-manifest.json', 'guides')
        total_failures += f; total_warnings += w

    # ── fetch.py ─────────────────────────────────────────────────────────────
    if 'fetch' in run_checks:
        f, w = check_python_script(scripts_dir / 'fetch.py', [
            ("No legacy /vdl/ fix workaround needed (URLs correct in manifest)",
             r'va\.gov/documents/', True,
             "Remove hardcoded URL substitution — inventory and manifests are now correct at source"),
            ("References manifest.json",
             r'manifest\.json', False, None),
            ("Has request delay / rate limiting",
             r'sleep|DELAY|time\.sleep', False,
             "Add a delay between requests to avoid hammering VA servers"),
        ])
        total_failures += f; total_warnings += w

    # ── fetch_guides.py ──────────────────────────────────────────────────────
    if 'fetch-guides' in run_checks:
        f, w = check_python_script(scripts_dir / 'fetch_guides.py', [
            ("No legacy /vdl/ fix workaround needed (URLs correct in manifest)",
             r'va\.gov/documents/', True,
             "Remove hardcoded URL substitution — guides-manifest.json is now correct at source"),
            ("References guides-manifest.json",
             r'guides-manifest\.json', False, None),
            ("Has request delay / rate limiting",
             r'sleep|DELAY|time\.sleep', False,
             "Add a delay between requests to avoid hammering VA servers"),
            ("Saves manifest after each fetch (resumable)",
             r'save_manifest', False,
             "Add save_manifest() call after each document fetch"),
        ])
        total_failures += f; total_warnings += w

    # ── pilot_manifest.py ────────────────────────────────────────────────────
    if 'pilot-manifest' in run_checks:
        f, w = check_python_script(scripts_dir / 'pilot_manifest.py', [
            ("No fix_url() workaround (removed — inventory URLs are correct)",
             r'def fix_url', True,
             "Remove fix_url() function — inventory is now correct at source"),
            ("No fix_url() call sites remaining",
             r'fix_url\(', True,
             "Remove all fix_url() calls — use doc_url directly"),
            ("References vdl_inventory.csv",
             r'vdl_inventory\.csv', False, None),
            ("Has --preserve-fetch-status flag",
             r'preserve.fetch.status', False,
             "Add --preserve-fetch-status argument to allow manifest rebuild without re-fetching"),
        ])
        total_failures += f; total_warnings += w

    # ── Summary ──────────────────────────────────────────────────────────────
    print(f"\n{'='*60}")
    if total_failures == 0 and total_warnings == 0:
        print(f"{_c(GREEN, BOLD + 'ALL CHECKS PASSED' + RESET)}")
        sys.exit(0)
    elif total_failures == 0:
        print(f"{_c(YELLOW, BOLD + f'PASSED WITH {total_warnings} WARNING(S)' + RESET)}")
        sys.exit(2)
    else:
        print(f"{_c(RED, BOLD + f'{total_failures} FAILURE(S)  {total_warnings} WARNING(S)' + RESET)}")
        sys.exit(1)


if __name__ == '__main__':
    main()
