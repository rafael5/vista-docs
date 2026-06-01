"""
Unit tests for enrich/doc_labels.py

Two pure functions:
  - parse_doc_labels(yaml_text) -> dict[str, str]
  - apply_canonical_label(doc_code, current_label, table) -> (label, subtitle)

Drives remediation §4 (assessment issue 3.5).
"""

from __future__ import annotations

import textwrap

import pytest

from vista_docs.enrich.doc_labels import (
    apply_canonical_label,
    parse_doc_labels,
)

SIMPLE_YAML = textwrap.dedent(
    """\
    labels:
      RN:   "Release Notes"
      DIBR: "Deployment, Installation, Back-Out, and Rollback Guide"
      UG:   "User Guide"
      UM:   "User Manual"
      CFG:  "Configuration Guide"
      INT:  "Interface Specification"
      REF:  "Reference"
    """
)


# ---------------------------------------------------------------------------
# parse_doc_labels
# ---------------------------------------------------------------------------


def test_parse_doc_labels_returns_dict() -> None:
    table = parse_doc_labels(SIMPLE_YAML)
    assert isinstance(table, dict)
    assert table["UG"] == "User Guide"
    assert table["DIBR"] == "Deployment, Installation, Back-Out, and Rollback Guide"


def test_parse_doc_labels_empty_returns_empty_dict() -> None:
    assert parse_doc_labels("labels: {}\n") == {}


def test_parse_doc_labels_rejects_empty_label() -> None:
    bad = textwrap.dedent(
        """\
        labels:
          UG: ""
        """
    )
    with pytest.raises(ValueError, match="UG"):
        parse_doc_labels(bad)


# ---------------------------------------------------------------------------
# apply_canonical_label
# ---------------------------------------------------------------------------


@pytest.fixture
def table() -> dict[str, str]:
    return parse_doc_labels(SIMPLE_YAML)


def test_apply_replaces_drift_label_and_emits_subtitle(table: dict[str, str]) -> None:
    """The classic §3.5 case: UG with 'Manager/ADPAC Guide' label."""
    label, subtitle = apply_canonical_label("UG", "Manager/ADPAC Guide", table)
    assert label == "User Guide"
    assert subtitle == "Manager/ADPAC Guide"


def test_apply_leaves_canonical_label_unchanged_no_subtitle(
    table: dict[str, str],
) -> None:
    label, subtitle = apply_canonical_label("UG", "User Guide", table)
    assert label == "User Guide"
    assert subtitle == ""


def test_apply_unknown_code_passes_through(table: dict[str, str]) -> None:
    """Code not in the canonical table preserves whatever label it had."""
    label, subtitle = apply_canonical_label("XYZ", "Some Label", table)
    assert label == "Some Label"
    assert subtitle == ""


def test_apply_empty_code_passes_through(table: dict[str, str]) -> None:
    label, subtitle = apply_canonical_label("", "Some Label", table)
    assert label == "Some Label"
    assert subtitle == ""


def test_apply_known_code_with_empty_label_fills_canonical(
    table: dict[str, str],
) -> None:
    """Edge case: row has doc_code but no doc_label — fill canonical, no subtitle."""
    label, subtitle = apply_canonical_label("UG", "", table)
    assert label == "User Guide"
    assert subtitle == ""


@pytest.mark.parametrize(
    "code,drift_label,expected_canonical",
    [
        ("CFG", "Setup and Configuration Guide", "Configuration Guide"),
        ("INT", "Interface Feed Guide", "Interface Specification"),
        ("REF", "Interface Toolkit", "Reference"),
        ("UG", "Manager/ADPAC Guide", "User Guide"),
        ("UM", "Clinical Coordinator Manual", "User Manual"),
    ],
)
def test_apply_handles_every_assessment_drift_case(
    table: dict[str, str],
    code: str,
    drift_label: str,
    expected_canonical: str,
) -> None:
    """Every drift case from assessment §3.5 must collapse to the canonical."""
    label, subtitle = apply_canonical_label(code, drift_label, table)
    assert label == expected_canonical
    assert subtitle == drift_label
