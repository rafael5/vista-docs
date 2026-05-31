"""I/O layer for corpus-wide frontmatter validation.

Walks a markdown tree, validates every document with the pure rules in
``validate.frontmatter``, writes a human-readable summary + a flags CSV, and
reports whether any *hard* failure was found. The publish/push gate and the
``validate`` CLI stage both call ``validate_tree``.

Intentionally thin: all rules live in ``validate/frontmatter.py`` (pure,
unit-tested). Excluded from the unit-test coverage gate.
"""

from __future__ import annotations

import csv
import logging
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

from vista_docs.validate.frontmatter import Violation, validate_doc_bytes

log = logging.getLogger(__name__)

# Generated index pages carry no frontmatter and are not corpus documents.
_SKIP_NAMES = frozenset({"INDEX.md", "README.md", "consolidation_summary.md"})


@dataclass
class ValidateReport:
    """Outcome of validating a whole tree."""

    root: Path
    total: int = 0
    clean: int = 0
    flagged: list[tuple[str, list[Violation]]] = field(default_factory=list)
    by_code: Counter = field(default_factory=Counter)

    @property
    def hard_failures(self) -> int:
        """Number of documents with at least one hard violation."""
        return sum(1 for _, vs in self.flagged if any(v.severity == "hard" for v in vs))

    @property
    def ok(self) -> bool:
        return self.hard_failures == 0


def validate_tree(root: Path, skip_names: frozenset[str] = _SKIP_NAMES) -> ValidateReport:
    """Validate every ``*.md`` under ``root`` (recursively)."""
    report = ValidateReport(root=root)
    for path in sorted(root.rglob("*.md")):
        if path.name in skip_names:
            continue
        report.total += 1
        try:
            raw = path.read_bytes()
        except OSError as e:
            vs = [Violation("read_error", "hard", str(e)[:120])]
        else:
            vs = validate_doc_bytes(raw)
        if vs:
            rel = str(path.relative_to(root))
            report.flagged.append((rel, vs))
            for v in vs:
                report.by_code[v.code.split(":")[0]] += 1
        else:
            report.clean += 1
    return report


def format_summary(report: ValidateReport) -> str:
    """Return a multi-line human-readable summary."""
    lines = [
        f"Validated {report.total} documents under {report.root}",
        f"  clean:         {report.clean}",
        f"  flagged:       {len(report.flagged)}",
        f"  hard failures: {report.hard_failures}",
    ]
    if report.by_code:
        lines.append("  violation breakdown:")
        for code, n in report.by_code.most_common():
            lines.append(f"    {code:<22} {n}")
    return "\n".join(lines)


def write_flags_csv(report: ValidateReport, csv_path: Path) -> None:
    """Write one row per (document, violation) to ``csv_path``."""
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["rel_path", "code", "severity", "detail"])
        for rel, vs in report.flagged:
            for v in vs:
                w.writerow([rel, v.code, v.severity, v.detail])
    log.info("Wrote validation flags → %s", csv_path)
