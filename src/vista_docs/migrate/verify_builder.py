"""
Verify-originals result classifier: compare expected vs actual SHA-256 hashes.

classify_result(expected, actual) → "ok" | "mismatch" | "missing"
summarize_results(results)        → dict

-------------------------------------------------------------------------------
AXIOMS
-------------------------------------------------------------------------------

A.  STATUS VALUES:
    - "ok":       actual SHA-256 matches expected (file is intact)
    - "mismatch": file exists but hash differs (file was modified or corrupted)
    - "missing":  file not found on disk (original_path absent in repo)

B.  SUMMARY FIELDS:
    - total, ok, mismatch, missing counts
    - packages_with_issues: sorted, deduplicated list of app_codes with any
      non-ok result
    - passed: True only when total > 0 and mismatch == 0 and missing == 0
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class VerifyResult:
    """Verification outcome for one original document."""

    app_code: str
    original_path: str
    expected_sha256: str
    actual_sha256: str
    status: str
    """'ok' | 'mismatch' | 'missing'"""


def classify_result(expected: str, actual: str | None) -> str:
    """
    Classify one hash comparison.

    Args:
        expected: SHA-256 from corpus-manifest.json.
        actual:   SHA-256 computed from file on disk, or None if file missing.

    Returns:
        'ok' | 'mismatch' | 'missing'
    """
    if actual is None:
        return "missing"
    return "ok" if expected == actual else "mismatch"


def summarize_results(results: list[VerifyResult]) -> dict:
    """
    Aggregate verification results into a summary dict.

    Returns:
        {
            total: int,
            ok: int,
            mismatch: int,
            missing: int,
            packages_with_issues: list[str],  # sorted, deduplicated
            passed: bool,
        }
    """
    total = len(results)
    ok = sum(1 for r in results if r.status == "ok")
    mismatch = sum(1 for r in results if r.status == "mismatch")
    missing = sum(1 for r in results if r.status == "missing")

    packages_with_issues = sorted({r.app_code for r in results if r.status != "ok"})

    passed = total > 0 and mismatch == 0 and missing == 0

    return {
        "total": total,
        "ok": ok,
        "mismatch": mismatch,
        "missing": missing,
        "packages_with_issues": packages_with_issues,
        "passed": passed,
    }
