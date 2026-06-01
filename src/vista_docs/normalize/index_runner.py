"""Anchor-index emit + normalized-tree validation (I/O; coverage-omitted).

Walks ``normalized/`` to (a) emit the corpus anchor index to ``survey/`` (spec
§11.5) and (b) run the §11 checks — noise linter, dead-anchor sweep, sidecar
integrity — aggregating a flags report. The pure rules live in ``index_pure.py``
and ``lint_pure.py``; this is the thin filesystem layer.
"""

from __future__ import annotations

import csv
import json
import logging
from dataclasses import dataclass, field
from pathlib import Path

import yaml

from vista_docs.normalize.index_pure import anchor_index_entry, build_anchor_index
from vista_docs.normalize.lint_pure import dead_anchors, noise_violations, sidecar_violations
from vista_docs.validate.frontmatter import split_frontmatter
from vista_docs.validate.schema import validate_against_schema

log = logging.getLogger(__name__)


def _read(path: Path) -> tuple[dict, str]:
    fm_raw, body = split_frontmatter(path.read_text(encoding="utf-8"))
    fm = (yaml.safe_load(fm_raw) if fm_raw else {}) or {}
    return fm, body


def emit_anchor_index(normalized_dir: Path, out_path: Path) -> int:
    """Write ``{doc: {headings, slugs, aliases}}`` JSON; return the doc count."""
    entries = []
    for p in sorted(normalized_dir.rglob("*.md")):
        fm, body = _read(p)
        rel = str(p.relative_to(normalized_dir))
        entries.append(anchor_index_entry(rel, body, fm.get("anchor_aliases") or {}))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(build_anchor_index(entries), indent=2, sort_keys=True, ensure_ascii=False),
        encoding="utf-8",
    )
    return len(entries)


@dataclass
class NormalizedValidation:
    docs: int = 0
    noise: int = 0
    dead: int = 0
    sidecar: int = 0
    schema_hard: int = 0
    schema_soft: int = 0
    flags: list[tuple[str, str, str]] = field(default_factory=list)

    @property
    def total(self) -> int:
        return self.noise + self.dead + self.sidecar + self.schema_hard + self.schema_soft

    @property
    def hard(self) -> int:
        """Gate-blocking issues (spec §11): noise, dangling anchors, broken
        sidecars, and hard schema violations — but not advisory schema flags."""
        return self.noise + self.dead + self.sidecar + self.schema_hard

    def hard_flags(self) -> list[tuple[str, str, str]]:
        return [f for f in self.flags if f[1] != "schema:soft"]


def validate_normalized(
    normalized_dir: Path, flags_csv: Path | None = None
) -> NormalizedValidation:
    """Run §11 noise/dead-anchor/sidecar checks over ``normalized/``."""
    rep = NormalizedValidation()
    sidecars = {p.name for p in normalized_dir.rglob("*.history.yaml")}
    for p in sorted(normalized_dir.rglob("*.md")):
        rep.docs += 1
        fm, body = _read(p)
        rel = str(p.relative_to(normalized_dir))
        for code in noise_violations(body):
            rep.noise += 1
            rep.flags.append((rel, f"noise:{code}", ""))
        for tgt in dead_anchors(body):
            rep.dead += 1
            rep.flags.append((rel, "dead_anchor", tgt))
        for viol in validate_against_schema(fm):
            if viol.severity == "hard":
                rep.schema_hard += 1
            else:
                rep.schema_soft += 1
            rep.flags.append((rel, f"schema:{viol.severity}", viol.code))
        side = fm.get("revision_sidecar")
        backref = None
        side_path = p.parent / side if side else None
        if side_path is not None and side_path.exists():
            try:
                sd = yaml.safe_load(side_path.read_text(encoding="utf-8")) or {}
                backref = sd.get("document")
            except (yaml.YAMLError, OSError):
                backref = None
        for code in sidecar_violations(p.name, side, sidecars, backref):
            rep.sidecar += 1
            rep.flags.append((rel, "sidecar", code))
    if flags_csv is not None:
        flags_csv.parent.mkdir(parents=True, exist_ok=True)
        with flags_csv.open("w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["rel_path", "code", "detail"])
            w.writerows(rep.flags)
    return rep
