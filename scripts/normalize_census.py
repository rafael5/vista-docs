#!/usr/bin/env python3
"""P0.2 — normalize-stage corpus census (Class A/B/C/D).

Walks ``consolidated/``, runs the pure normalize orchestrator on each document,
and tags it with the §8 class plus the signals that drive F3/F7 effort sizing
(native vs inferred headings, Word anchors, pagination, PDF availability, dead
nav-link wrapping, revision tables). Writes ``survey/normalize_census.csv`` and
prints a summary.

Run:  .venv/bin/python scripts/normalize_census.py
Not part of the automated pipeline (ad-hoc discovery tool; see scripts/README.md).
"""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

import yaml

from vista_docs.config import DATA_DIR
from vista_docs.normalize.anchors_pure import extract_headings
from vista_docs.normalize.lint_pure import dead_anchors
from vista_docs.normalize.normalize_pure import normalize_body
from vista_docs.validate.frontmatter import split_frontmatter

FIELDS = [
    "rel_path",
    "app_code",
    "doc_class",
    "final_headings",
    "word_anchors",
    "headings_promoted",
    "is_paginated",
    "has_pdf",
    "nav_links_unwrapped",
    "dead_links_swept",
    "dead_anchors_remaining",
    "revision_count",
]


def census_row(path: Path, root: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    fm_raw, body = split_frontmatter(text)
    fm = (yaml.safe_load(fm_raw) if fm_raw else {}) or {}
    has_pdf = bool(fm.get("pdf_url"))
    r = normalize_body(body, description=fm.get("description"), has_pdf=has_pdf)
    rel = path.relative_to(root)
    return {
        "rel_path": str(rel),
        "app_code": rel.parts[0] if rel.parts else "",
        "doc_class": r.stats["doc_class"],
        "final_headings": len(extract_headings(r.body)),
        "word_anchors": len(r.aliases),
        "headings_promoted": r.stats["headings_promoted"],
        "is_paginated": int(r.stats["boilerplate_removed"] > 0),
        "has_pdf": int(has_pdf),
        "nav_links_unwrapped": r.stats["nav_links_unwrapped"],
        "dead_links_swept": r.stats["dead_links_swept"],
        "dead_anchors_remaining": len(dead_anchors(r.body)),
        "revision_count": r.frontmatter.get("revision_count", 0),
    }


def main() -> None:
    root = DATA_DIR / "consolidated"
    out = DATA_DIR / "survey" / "normalize_census.csv"
    rows = [census_row(p, root) for p in sorted(root.rglob("*.md"))]

    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)

    n = len(rows)
    by_class = Counter(r["doc_class"] for r in rows)
    nav = sum(1 for r in rows if r["nav_links_unwrapped"])
    pseudo_b = sum(1 for r in rows if r["doc_class"] == "B" and r["final_headings"] <= 2)
    c_with_pdf = sum(1 for r in rows if r["doc_class"] == "C" and r["has_pdf"])
    with_rev = sum(1 for r in rows if r["revision_count"])
    clean = sum(1 for r in rows if r["dead_anchors_remaining"] == 0)

    print(f"normalize census — {n} consolidated docs → {out}")
    for cls in ("A", "B", "C", "D"):
        print(f"  Class {cls}: {by_class.get(cls, 0):4d}")
    print(f"  docs with dead nav-link wrapping : {nav}")
    print(f"  'pseudo-B' (B but <=2 headings)  : {pseudo_b}")
    print(f"  Class-C docs WITH pdf (F7-ready) : {c_with_pdf}")
    print(f"  docs with a revision table       : {with_rev}")
    print(f"  docs with 0 dead anchors after   : {clean}/{n}")


if __name__ == "__main__":
    main()
