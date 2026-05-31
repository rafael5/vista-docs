"""
Unit tests for enrich/text_fixers.py

Three pure functions:
  - fix_mojibake(text)            — repair Latin-1/UTF-8 misencoding via ftfy
  - parse_typo_corrections(yaml)  — load curated correction table
  - apply_typo_corrections(text, field, corrections) -> (corrected, aliases)

Drives remediation §3 (assessment issues 3.1, 3.2).
"""

from __future__ import annotations

import textwrap

import pytest

from vista_docs.enrich.text_fixers import (
    TypoCorrection,
    apply_typo_corrections,
    fix_mojibake,
    parse_typo_corrections,
)

# ---------------------------------------------------------------------------
# fix_mojibake — patterns from assessment §3.1 + real inventory samples
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "broken,expected",
    [
        # Right single quote: ftfy's default uncurls to ASCII apostrophe
        # (a deliberate normalization that improves searchability).
        ("Developerâ€™s Guide", "Developer's Guide"),
        # En dash / em dash mojibake decodes to the proper Unicode dashes
        # (preserved, not flattened — ftfy only uncurls quotes by default).
        ("Clinical Pathways â€“ Lung", "Clinical Pathways – Lung"),
        ("Clinical Pathways â€” Lung", "Clinical Pathways — Lung"),
        # Non-breaking space stays as NBSP (preserves layout intent).
        ("HelloÂ World", "Hello\xa0World"),
        # Already-clean text passes through unchanged
        ("Plain ASCII text", "Plain ASCII text"),
        # Empty string
        ("", ""),
        # Real inventory sample (multi-pattern in one string)
        (
            "Kernel 8.0 Developerâ€™s Guide: Address Hygiene UG",
            "Kernel 8.0 Developer's Guide: Address Hygiene UG",
        ),
    ],
)
def test_fix_mojibake_repairs_known_patterns(broken: str, expected: str) -> None:
    assert fix_mojibake(broken) == expected


def test_fix_mojibake_idempotent() -> None:
    """Running twice must produce the same result as running once."""
    once = fix_mojibake("Developerâ€™s Guide")
    twice = fix_mojibake(once)
    assert once == twice


def test_fix_mojibake_handles_none_safely() -> None:
    """Defensive: empty / falsy input returns empty string, not None."""
    assert fix_mojibake("") == ""


# ---------------------------------------------------------------------------
# parse_typo_corrections
# ---------------------------------------------------------------------------


SIMPLE_YAML = textwrap.dedent(
    """\
    corrections:
      - source: "Staph Aurerus"
        corrected: "Staph Aureus"
        fields: [doc_title, doc_subject, app_name_full]
      - source: "DIBORG"
        corrected: "DIBRG"
        fields: [doc_title, doc_subject]
      - source: "Health Data  Informatics"
        corrected: "Health Data Informatics"
        fields: [app_name_full]
    """
)


def test_parse_typo_corrections_returns_list_of_corrections() -> None:
    out = parse_typo_corrections(SIMPLE_YAML)
    assert len(out) == 3
    assert all(isinstance(c, TypoCorrection) for c in out)


def test_parse_typo_corrections_populates_fields() -> None:
    out = parse_typo_corrections(SIMPLE_YAML)
    assert out[0] == TypoCorrection(
        source="Staph Aurerus",
        corrected="Staph Aureus",
        fields=("doc_title", "doc_subject", "app_name_full"),
    )


def test_parse_typo_corrections_empty_yaml_returns_empty() -> None:
    assert parse_typo_corrections("corrections: []\n") == []


def test_parse_typo_corrections_missing_source_raises() -> None:
    bad = textwrap.dedent(
        """\
        corrections:
          - corrected: "X"
            fields: [doc_title]
        """
    )
    with pytest.raises(ValueError, match="source"):
        parse_typo_corrections(bad)


def test_parse_typo_corrections_missing_corrected_raises() -> None:
    bad = textwrap.dedent(
        """\
        corrections:
          - source: "X"
            fields: [doc_title]
        """
    )
    with pytest.raises(ValueError, match="corrected"):
        parse_typo_corrections(bad)


# ---------------------------------------------------------------------------
# apply_typo_corrections
# ---------------------------------------------------------------------------


@pytest.fixture
def corrections() -> list[TypoCorrection]:
    return parse_typo_corrections(SIMPLE_YAML)


def test_apply_returns_corrected_text_for_matching_field(
    corrections: list[TypoCorrection],
) -> None:
    text, aliases = apply_typo_corrections(
        "Methicillin Resistant Staph Aurerus", "doc_title", corrections
    )
    assert text == "Methicillin Resistant Staph Aureus"
    assert aliases == ["Staph Aurerus"]


def test_apply_does_not_correct_when_field_not_in_scope(
    corrections: list[TypoCorrection],
) -> None:
    """Health Data  Informatics correction is scoped to app_name_full only."""
    text, aliases = apply_typo_corrections("Health Data  Informatics", "doc_title", corrections)
    assert text == "Health Data  Informatics"
    assert aliases == []


def test_apply_returns_no_aliases_for_clean_text(
    corrections: list[TypoCorrection],
) -> None:
    text, aliases = apply_typo_corrections("ordinary clean title", "doc_title", corrections)
    assert text == "ordinary clean title"
    assert aliases == []


def test_apply_collects_multiple_aliases_when_multiple_corrections_match(
    corrections: list[TypoCorrection],
) -> None:
    text, aliases = apply_typo_corrections("Staph Aurerus DIBORG combo", "doc_title", corrections)
    assert text == "Staph Aureus DIBRG combo"
    assert set(aliases) == {"Staph Aurerus", "DIBORG"}


def test_apply_handles_empty_text(corrections: list[TypoCorrection]) -> None:
    text, aliases = apply_typo_corrections("", "doc_title", corrections)
    assert text == ""
    assert aliases == []


def test_apply_real_inventory_dibrg_sample(corrections: list[TypoCorrection]) -> None:
    """Real row from the inventory CSV (line 3516)."""
    title = "Home Telehealth Reporting Enhancements (HTRE)  Phase 3 Build 1 DIBORG"
    text, aliases = apply_typo_corrections(title, "doc_title", corrections)
    assert text.endswith("Phase 3 Build 1 DIBRG")
    assert aliases == ["DIBORG"]
