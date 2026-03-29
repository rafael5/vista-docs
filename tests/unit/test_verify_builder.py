"""
Unit tests for migrate/verify_builder.py — SHA-256 result classification and summary.

All tests use in-memory data; no filesystem I/O.
"""

from vista_docs.migrate.verify_builder import VerifyResult, classify_result, summarize_results

_SHA = "a" * 64
_SHA2 = "b" * 64


# ---------------------------------------------------------------------------
# TestClassifyResult
# ---------------------------------------------------------------------------


class TestClassifyResult:
    def test_matching_hashes_ok(self):
        assert classify_result(_SHA, _SHA) == "ok"

    def test_mismatched_hashes(self):
        assert classify_result(_SHA, _SHA2) == "mismatch"

    def test_missing_file(self):
        assert classify_result(_SHA, None) == "missing"

    def test_empty_expected_matching(self):
        assert classify_result("", "") == "ok"

    def test_empty_expected_mismatch(self):
        assert classify_result("", _SHA) == "mismatch"


# ---------------------------------------------------------------------------
# TestSummarizeResults
# ---------------------------------------------------------------------------


def _result(status: str, app_code: str = "PSO") -> VerifyResult:
    return VerifyResult(
        app_code=app_code,
        original_path=f"originals/technical-manual/{app_code}_TM.md",
        expected_sha256=_SHA,
        actual_sha256=_SHA if status == "ok" else (_SHA2 if status == "mismatch" else ""),
        status=status,
    )


class TestSummarizeResults:
    def test_empty_results(self):
        s = summarize_results([])
        assert s["total"] == 0
        assert s["ok"] == 0
        assert s["mismatch"] == 0
        assert s["missing"] == 0

    def test_all_ok(self):
        results = [_result("ok"), _result("ok")]
        s = summarize_results(results)
        assert s["total"] == 2
        assert s["ok"] == 2
        assert s["mismatch"] == 0
        assert s["missing"] == 0

    def test_mixed_statuses(self):
        results = [_result("ok"), _result("mismatch"), _result("missing")]
        s = summarize_results(results)
        assert s["total"] == 3
        assert s["ok"] == 1
        assert s["mismatch"] == 1
        assert s["missing"] == 1

    def test_packages_with_issues_listed(self):
        results = [
            _result("ok", "PSO"),
            _result("mismatch", "PSB"),
            _result("missing", "PSJ"),
        ]
        s = summarize_results(results)
        assert "PSB" in s["packages_with_issues"]
        assert "PSJ" in s["packages_with_issues"]
        assert "PSO" not in s["packages_with_issues"]

    def test_no_issues_empty_packages_list(self):
        results = [_result("ok"), _result("ok")]
        s = summarize_results(results)
        assert s["packages_with_issues"] == []

    def test_packages_with_issues_deduplicated(self):
        results = [_result("mismatch", "PSO"), _result("missing", "PSO")]
        s = summarize_results(results)
        assert s["packages_with_issues"].count("PSO") == 1

    def test_summary_has_pass_flag_when_all_ok(self):
        results = [_result("ok")]
        s = summarize_results(results)
        assert s["passed"] is True

    def test_summary_fails_on_mismatch(self):
        results = [_result("mismatch")]
        s = summarize_results(results)
        assert s["passed"] is False

    def test_summary_fails_on_missing(self):
        results = [_result("missing")]
        s = summarize_results(results)
        assert s["passed"] is False

    def test_summary_fails_on_empty(self):
        s = summarize_results([])
        assert s["passed"] is False
