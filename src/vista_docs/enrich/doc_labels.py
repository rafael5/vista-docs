"""
Canonical doc_code → doc_label table loader and applier.

Two pure functions:

  parse_doc_labels(yaml_text) -> dict[str, str]
      Load the curated doc_labels table from data/doc_labels.yaml.

  apply_canonical_label(doc_code, current_label, table) -> (label, subtitle)
      If ``doc_code`` is in the canonical table, return the canonical label
      and any non-canonical original wording as a subtitle. Otherwise return
      ``(current_label, "")`` unchanged.

Drives remediation §4 (assessment issue 3.5).
"""

from __future__ import annotations

from pathlib import Path

import yaml


def parse_doc_labels(yaml_text: str) -> dict[str, str]:
    """Parse a doc-labels YAML document into a {code: canonical_label} dict."""
    raw = yaml.safe_load(yaml_text) or {}
    labels = raw.get("labels") or {}
    out: dict[str, str] = {}
    for code, label in labels.items():
        if not label:
            raise ValueError(f"doc_labels: '{code}' has empty canonical label")
        out[code] = label
    return out


def load_doc_labels(path: Path) -> dict[str, str]:
    """Read a doc-labels YAML file."""
    return parse_doc_labels(path.read_text(encoding="utf-8"))


def apply_canonical_label(
    doc_code: str,
    current_label: str,
    table: dict[str, str],
) -> tuple[str, str]:
    """Return ``(canonical_label, subtitle)`` for the given code.

    - If ``doc_code`` is unknown or empty, pass ``current_label`` through.
    - If the current label matches the canonical, subtitle is empty.
    - If the current label differs, subtitle preserves the original wording
      (which often carries useful per-document subtitle text like
      "Manager/ADPAC Guide") and the label is replaced with the canonical.
    """
    if not doc_code or doc_code not in table:
        return current_label, ""

    canonical = table[doc_code]
    if current_label and current_label != canonical:
        return canonical, current_label
    return canonical, ""
