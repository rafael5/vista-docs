"""
Text-cleanup primitives for the enrich-inventory stage.

Three pure functions:

  fix_mojibake(text)
      Repair UTF-8/Latin-1 misencoding artifacts (â€™, â€", Â, …) using ftfy.

  parse_typo_corrections(yaml_text)
      Load the curated typo-correction table from data/typo_corrections.yaml.

  apply_typo_corrections(text, field, corrections) -> (corrected, aliases)
      Apply field-scoped corrections; return both the corrected string and a
      list of original-spelling tokens that were replaced (for emitting
      doc_search_aliases).

Drives remediation §3 (assessment issues 3.1, 3.2).
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import ftfy
import yaml


@dataclass(frozen=True)
class TypoCorrection:
    source: str
    corrected: str
    fields: tuple[str, ...]


def fix_mojibake(text: str) -> str:
    """Repair encoding artifacts in ``text``. Idempotent and Unicode-safe."""
    if not text:
        return ""
    return ftfy.fix_text(text, normalization="NFC")


def parse_typo_corrections(yaml_text: str) -> list[TypoCorrection]:
    """Parse a typo-corrections YAML document into a list of TypoCorrection."""
    raw = yaml.safe_load(yaml_text) or {}
    items = raw.get("corrections") or []

    out: list[TypoCorrection] = []
    for i, item in enumerate(items):
        if "source" not in item:
            raise ValueError(f"typo_corrections[{i}]: missing required field 'source'")
        if "corrected" not in item:
            raise ValueError(f"typo_corrections[{i}]: missing required field 'corrected'")
        out.append(
            TypoCorrection(
                source=item["source"],
                corrected=item["corrected"],
                fields=tuple(item.get("fields") or ()),
            )
        )
    return out


def load_typo_corrections(path: Path) -> list[TypoCorrection]:
    """Read a typo-corrections YAML file."""
    return parse_typo_corrections(path.read_text(encoding="utf-8"))


def apply_typo_corrections(
    text: str,
    field: str,
    corrections: list[TypoCorrection],
) -> tuple[str, list[str]]:
    """Apply every correction whose ``fields`` include ``field`` to ``text``.

    Returns ``(corrected_text, aliases)`` where ``aliases`` is the list of
    ``source`` strings that were actually substituted in this call. Callers
    accumulate aliases across fields to emit ``doc_search_aliases`` so search
    UIs can still match the original spelling.
    """
    if not text:
        return "", []

    aliases: list[str] = []
    out = text
    for c in corrections:
        if field in c.fields and c.source in out:
            out = out.replace(c.source, c.corrected)
            aliases.append(c.source)
    return out, aliases
