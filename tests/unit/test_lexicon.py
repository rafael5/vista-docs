"""
Unit tests for analyze/lexicon.py — heading lexicon and frequency statistics.

All tests use synthetic DocTypeProfile objects; no filesystem I/O.
"""

import pytest

from vista_docs.analyze.headings import (
    BOILERPLATE,
    BOILERPLATE_THRESHOLD,
    COMMON,
    UNIQUE,
    UNIQUE_THRESHOLD,
    DocTypeProfile,
    HeadingRecord,
)
from vista_docs.analyze.lexicon import (
    FrequencyBin,
    LexiconEntry,
    LexiconStats,
    build_lexicon,
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _record(
    normalized: str,
    doc_count: int,
    doc_frequency: float,
    category: str,
    raw_variants: list[str] | None = None,
    level_counts: dict[int, int] | None = None,
) -> HeadingRecord:
    return HeadingRecord(
        normalized=normalized,
        raw_variants=raw_variants or [normalized.title()],
        level_counts=level_counts or {2: doc_count},
        doc_count=doc_count,
        doc_frequency=doc_frequency,
        category=category,
    )


def _profile(
    doc_type: str,
    doc_count: int,
    headings: list[HeadingRecord],
) -> DocTypeProfile:
    return DocTypeProfile(
        doc_type=doc_type,
        doc_count=doc_count,
        total_heading_occurrences=sum(r.doc_count for r in headings),
        unique_normalized_count=len(headings),
        boilerplate_threshold=BOILERPLATE_THRESHOLD,
        unique_threshold=UNIQUE_THRESHOLD,
        headings=headings,
    )


# ---------------------------------------------------------------------------
# Minimal profile fixtures
# ---------------------------------------------------------------------------

# 10 docs: 1 boilerplate (100%), 2 common (40%, 30%), 7 unique (10% each)
_HEADINGS_10 = [
    _record("introduction", 10, 1.00, BOILERPLATE),
    _record("background", 4, 0.40, COMMON),
    _record("configuration", 3, 0.30, COMMON),
    _record("alpha", 1, 0.10, UNIQUE),
    _record("beta", 1, 0.10, UNIQUE),
    _record("gamma", 1, 0.10, UNIQUE),
    _record("delta", 1, 0.10, UNIQUE),
    _record("epsilon", 1, 0.10, UNIQUE),
    _record("zeta", 1, 0.10, UNIQUE),
    _record("eta", 1, 0.10, UNIQUE),
]
PROFILE_10 = _profile("release-note", 10, _HEADINGS_10)

# Single-document profile
_HEADINGS_1 = [
    _record("overview", 1, 1.00, BOILERPLATE),
    _record("details", 1, 1.00, BOILERPLATE),
]
PROFILE_1 = _profile("release-note", 1, _HEADINGS_1)

# Empty profile (no headings)
PROFILE_EMPTY = _profile("empty", 0, [])


# ---------------------------------------------------------------------------
# TestLexiconEntries
# ---------------------------------------------------------------------------


class TestLexiconEntries:
    def test_returns_lexicon_stats(self):
        result = build_lexicon(PROFILE_10)
        assert isinstance(result, LexiconStats)

    def test_lexicon_size_matches_unique_normalized_count(self):
        result = build_lexicon(PROFILE_10)
        assert result.lexicon_size == len(_HEADINGS_10)

    def test_entries_sorted_alphabetically(self):
        result = build_lexicon(PROFILE_10)
        names = [e.normalized for e in result.entries]
        assert names == sorted(names)

    def test_every_heading_appears_as_entry(self):
        result = build_lexicon(PROFILE_10)
        norms = {e.normalized for e in result.entries}
        assert norms == {r.normalized for r in _HEADINGS_10}

    def test_entry_fields_preserved(self):
        result = build_lexicon(PROFILE_10)
        intro = next(e for e in result.entries if e.normalized == "introduction")
        assert intro.doc_count == 10
        assert intro.doc_frequency == 1.0
        assert intro.category == BOILERPLATE
        assert len(intro.raw_variants) >= 1

    def test_empty_profile_returns_empty_entries(self):
        result = build_lexicon(PROFILE_EMPTY)
        assert result.entries == []
        assert result.lexicon_size == 0


# ---------------------------------------------------------------------------
# TestCategoryCounts
# ---------------------------------------------------------------------------


class TestCategoryCounts:
    def test_boilerplate_count(self):
        result = build_lexicon(PROFILE_10)
        assert result.category_counts[BOILERPLATE] == 1

    def test_common_count(self):
        result = build_lexicon(PROFILE_10)
        assert result.category_counts[COMMON] == 2

    def test_unique_count(self):
        result = build_lexicon(PROFILE_10)
        assert result.category_counts[UNIQUE] == 7

    def test_category_pcts_sum_to_100(self):
        result = build_lexicon(PROFILE_10)
        total = sum(result.category_pcts.values())
        assert abs(total - 100.0) < 0.01

    def test_boilerplate_pct_correct(self):
        result = build_lexicon(PROFILE_10)
        # 1 of 10 headings = 10%
        assert abs(result.category_pcts[BOILERPLATE] - 10.0) < 0.01

    def test_empty_profile_zero_counts(self):
        result = build_lexicon(PROFILE_EMPTY)
        assert result.category_counts[BOILERPLATE] == 0
        assert result.category_counts[COMMON] == 0
        assert result.category_counts[UNIQUE] == 0

    def test_empty_profile_zero_pcts(self):
        result = build_lexicon(PROFILE_EMPTY)
        assert result.category_pcts[BOILERPLATE] == 0.0


# ---------------------------------------------------------------------------
# TestFrequencyStats
# ---------------------------------------------------------------------------


class TestFrequencyStats:
    def test_min_frequency(self):
        result = build_lexicon(PROFILE_10)
        assert result.min_freq == pytest.approx(0.10, abs=1e-4)

    def test_max_frequency(self):
        result = build_lexicon(PROFILE_10)
        assert result.max_freq == pytest.approx(1.00, abs=1e-4)

    def test_mean_frequency_correct(self):
        # (1.0 + 0.4 + 0.3 + 7×0.1) / 10 = (1.0+0.4+0.3+0.7)/10 = 2.4/10 = 0.24
        result = build_lexicon(PROFILE_10)
        assert result.mean_freq == pytest.approx(0.24, abs=1e-4)

    def test_median_frequency_correct(self):
        # sorted freqs: 0.1×7, 0.3, 0.4, 1.0 → median of 10 values = avg of 5th+6th
        # sorted: [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.3,0.4,1.0]
        # 5th (idx4)=0.1, 6th (idx5)=0.1 → median=0.1
        result = build_lexicon(PROFILE_10)
        assert result.median_freq == pytest.approx(0.10, abs=1e-4)

    def test_std_dev_positive(self):
        result = build_lexicon(PROFILE_10)
        assert result.std_dev > 0.0

    def test_p25_le_median_le_p75(self):
        result = build_lexicon(PROFILE_10)
        assert result.p25 <= result.median_freq <= result.p75

    def test_p90_ge_p75(self):
        result = build_lexicon(PROFILE_10)
        assert result.p90 >= result.p75

    def test_single_doc_all_1_0(self):
        result = build_lexicon(PROFILE_1)
        assert result.min_freq == pytest.approx(1.0)
        assert result.max_freq == pytest.approx(1.0)
        assert result.mean_freq == pytest.approx(1.0)
        assert result.std_dev == pytest.approx(0.0)

    def test_empty_profile_stats_are_zero(self):
        result = build_lexicon(PROFILE_EMPTY)
        assert result.mean_freq == 0.0
        assert result.std_dev == 0.0
        assert result.min_freq == 0.0
        assert result.max_freq == 0.0


# ---------------------------------------------------------------------------
# TestFrequencyHistogram
# ---------------------------------------------------------------------------


class TestFrequencyHistogram:
    def test_histogram_has_ten_bins(self):
        result = build_lexicon(PROFILE_10)
        assert len(result.histogram) == 10

    def test_histogram_bins_cover_0_to_100_pct(self):
        result = build_lexicon(PROFILE_10)
        labels = [b.label for b in result.histogram]
        assert labels[0] == "0–10%"
        assert labels[-1] == "90–100%"

    def test_histogram_counts_sum_to_lexicon_size(self):
        result = build_lexicon(PROFILE_10)
        total = sum(b.count for b in result.histogram)
        assert total == result.lexicon_size

    def test_histogram_bin_0_10_correct(self):
        # Frequencies: 7×0.1 → these are exactly 10% (≤0.10 boundary)
        # 0–10% bin should capture the 7 unique headings at 10%
        result = build_lexicon(PROFILE_10)
        bin_0_10 = next(b for b in result.histogram if b.label == "0–10%")
        assert bin_0_10.count == 7

    def test_histogram_bin_90_100_correct(self):
        # 1 heading at 100% → in the 90–100% bin
        result = build_lexicon(PROFILE_10)
        bin_top = next(b for b in result.histogram if b.label == "90–100%")
        assert bin_top.count == 1

    def test_empty_profile_all_bins_zero(self):
        result = build_lexicon(PROFILE_EMPTY)
        assert all(b.count == 0 for b in result.histogram)


# ---------------------------------------------------------------------------
# TestLexiconEntryDataclass
# ---------------------------------------------------------------------------


class TestLexiconEntryDataclass:
    def test_entry_is_dataclass(self):
        result = build_lexicon(PROFILE_10)
        entry = result.entries[0]
        assert isinstance(entry, LexiconEntry)

    def test_frequency_bin_is_dataclass(self):
        result = build_lexicon(PROFILE_10)
        assert isinstance(result.histogram[0], FrequencyBin)
