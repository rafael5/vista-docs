"""
Heading lexicon and frequency statistics for a DocTypeProfile.

build_lexicon(profile) → LexiconStats

-------------------------------------------------------------------------------
AXIOMS
-------------------------------------------------------------------------------

A.  LEXICON = FULL VOCABULARY, NOT JUST "UNIQUE" CATEGORY.
    The lexicon for a doc type is the complete set of distinct normalized
    heading strings found across all documents of that type — BOILERPLATE,
    COMMON, and UNIQUE headings alike. The UNIQUE classification from
    headings.py describes frequency bands; the lexicon is the vocabulary.
    Callers who want only the high-information headings should filter by
    `entry.category == UNIQUE`.

B.  ALPHABETICAL ORDER.
    Lexicon entries are sorted by their normalized form. This produces a
    stable, scannable vocabulary list. Frequency sorting is available via
    the parent DocTypeProfile.headings (sorted by doc_frequency desc).

C.  STATISTICS ARE COMPUTED OVER ALL HEADINGS IN THE PROFILE.
    Mean, median, std_dev, and percentiles are computed from the
    doc_frequency values of all distinct normalized headings — not weighted
    by occurrence count, not filtered by category. Each heading contributes
    one data point regardless of how many times it appears in documents.
    Rationale: the lexicon is a vocabulary, not a corpus; each word is
    counted once.

D.  HISTOGRAM USES 10 EQUAL-WIDTH BINS OVER [0%, 100%].
    Bin boundaries: 0–10%, 10–20%, ..., 90–100%.
    A heading at exactly a bin boundary (e.g. 10%) falls in the lower bin
    (0–10%), except the 100% boundary which falls in the 90–100% bin.
    Formally: bin i covers (i*10%, (i+1)*10%], with bin 0 covering [0%, 10%].
    This gives a quick visual of how top-heavy (many boilerplate, few unique)
    or bottom-heavy (many unique, few boilerplate) the heading distribution is.

E.  EMPTY PROFILES.
    A profile with no headings (doc_count = 0 or no non-stub documents)
    produces a LexiconStats with zero counts, zero frequencies, and empty
    histogram bins. No division-by-zero or NaN values are produced.

F.  PERCENTILES USE LINEAR INTERPOLATION (same as NumPy default).
    P25, P50 (median), P75, P90 are computed without requiring NumPy:
    we sort the frequency list and use the standard interpolation formula
    `L + (R - L) * f` where L and R are adjacent sorted values and f is
    the fractional index position. This matches numpy.percentile behavior.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field

from vista_docs.analyze.headings import BOILERPLATE, COMMON, UNIQUE, DocTypeProfile

# ---------------------------------------------------------------------------
# Output data structures
# ---------------------------------------------------------------------------


@dataclass
class LexiconEntry:
    """One entry in the heading lexicon for a doc type."""

    normalized: str
    """Normalized heading text (the lexicon key)."""

    raw_variants: list[str]
    """Up to MAX_VARIANTS raw forms that mapped to this normalized string."""

    level_counts: dict[int, int]
    """Occurrence counts by heading level, e.g. {2: 12, 3: 2}."""

    doc_count: int
    """Number of documents containing this heading."""

    doc_frequency: float
    """doc_count / total docs in the doc type. Range [0.0, 1.0]."""

    category: str
    """BOILERPLATE | COMMON | UNIQUE (from headings.py thresholds)."""


@dataclass
class FrequencyBin:
    """One histogram bucket for the heading frequency distribution."""

    label: str
    """Human-readable label, e.g. '0–10%'."""

    low: float
    """Lower boundary (inclusive for bin 0, exclusive for others)."""

    high: float
    """Upper boundary (inclusive)."""

    count: int
    """Number of headings whose doc_frequency falls in this bin."""


@dataclass
class LexiconStats:
    """Heading lexicon and frequency statistics for one doc type."""

    doc_type: str
    doc_count: int
    lexicon_size: int
    """Total number of distinct normalized headings (= len(entries))."""

    # Category breakdown
    category_counts: dict[str, int]
    """Count of headings in each category: {BOILERPLATE: N, COMMON: N, UNIQUE: N}."""

    category_pcts: dict[str, float]
    """Percentage of headings in each category (0–100). Sums to 100."""

    # Frequency distribution
    mean_freq: float
    median_freq: float
    std_dev: float
    min_freq: float
    max_freq: float
    p25: float
    p75: float
    p90: float

    # Histogram
    histogram: list[FrequencyBin]
    """10 equal-width frequency bins (Axiom D)."""

    # Alphabetical lexicon
    entries: list[LexiconEntry] = field(default_factory=list)
    """All headings sorted alphabetically by normalized form (Axiom B)."""


# ---------------------------------------------------------------------------
# Builder (pure — no I/O)
# ---------------------------------------------------------------------------


def build_lexicon(profile: DocTypeProfile) -> LexiconStats:
    """
    Build a LexiconStats from a DocTypeProfile.

    Computes the alphabetical heading vocabulary and frequency distribution
    statistics. See module axioms for computation details.

    Args:
        profile: A DocTypeProfile produced by headings.build_profile().

    Returns:
        LexiconStats with entries, category counts/pcts, and all stats.
    """
    headings = profile.headings  # sorted by doc_frequency desc from build_profile

    # Alphabetical lexicon entries (Axiom B)
    entries = sorted(
        [
            LexiconEntry(
                normalized=r.normalized,
                raw_variants=r.raw_variants,
                level_counts=r.level_counts,
                doc_count=r.doc_count,
                doc_frequency=r.doc_frequency,
                category=r.category,
            )
            for r in headings
        ],
        key=lambda e: e.normalized,
    )

    n = len(entries)

    # Category counts and percentages
    cat_counts = {BOILERPLATE: 0, COMMON: 0, UNIQUE: 0}
    for r in headings:
        cat_counts[r.category] = cat_counts.get(r.category, 0) + 1

    if n > 0:
        cat_pcts = {k: round(v / n * 100, 2) for k, v in cat_counts.items()}
        # Correct rounding drift on the largest category so sum = exactly 100
        largest = max(cat_counts, key=lambda k: cat_counts[k])
        cat_pcts[largest] = round(100.0 - sum(v for k, v in cat_pcts.items() if k != largest), 2)
    else:
        cat_pcts = {BOILERPLATE: 0.0, COMMON: 0.0, UNIQUE: 0.0}

    # Frequency statistics (Axiom C, E, F)
    freqs = sorted(e.doc_frequency for e in entries)
    if freqs:
        mean_f = sum(freqs) / n
        var = sum((f - mean_f) ** 2 for f in freqs) / n
        std = math.sqrt(var)
        min_f = freqs[0]
        max_f = freqs[-1]
        median_f = _percentile(freqs, 50)
        p25 = _percentile(freqs, 25)
        p75 = _percentile(freqs, 75)
        p90 = _percentile(freqs, 90)
    else:
        mean_f = median_f = std = min_f = max_f = p25 = p75 = p90 = 0.0

    # Histogram (Axiom D)
    histogram = _build_histogram(entries)

    return LexiconStats(
        doc_type=profile.doc_type,
        doc_count=profile.doc_count,
        lexicon_size=n,
        category_counts=cat_counts,
        category_pcts=cat_pcts,
        mean_freq=round(mean_f, 6),
        median_freq=round(median_f, 6),
        std_dev=round(std, 6),
        min_freq=round(min_f, 6),
        max_freq=round(max_f, 6),
        p25=round(p25, 6),
        p75=round(p75, 6),
        p90=round(p90, 6),
        histogram=histogram,
        entries=entries,
    )


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _percentile(sorted_vals: list[float], pct: float) -> float:
    """
    Compute a percentile using linear interpolation (Axiom F).

    Args:
        sorted_vals: Ascending-sorted list of floats. Must be non-empty.
        pct:         Percentile in [0, 100].

    Returns:
        Interpolated percentile value.
    """
    n = len(sorted_vals)
    if n == 1:
        return sorted_vals[0]
    idx = (pct / 100) * (n - 1)
    lo = int(idx)
    hi = min(lo + 1, n - 1)
    frac = idx - lo
    return sorted_vals[lo] + (sorted_vals[hi] - sorted_vals[lo]) * frac


def _build_histogram(entries: list[LexiconEntry]) -> list[FrequencyBin]:
    """
    Build 10 equal-width frequency bins over [0%, 100%] (Axiom D).

    Bin assignment: bin i covers (i*0.1, (i+1)*0.1] for i > 0;
    bin 0 covers [0.0, 0.1].
    """
    bins = []
    for i in range(10):
        low = i / 10
        high = (i + 1) / 10
        label = f"{i * 10}–{(i + 1) * 10}%"
        count = 0
        for e in entries:
            f = e.doc_frequency
            if i == 0:
                if low <= f <= high:
                    count += 1
            else:
                if low < f <= high:
                    count += 1
        bins.append(FrequencyBin(label=label, low=low, high=high, count=count))
    return bins
