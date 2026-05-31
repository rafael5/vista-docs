"""Integration: consolidated docs carry the unified schema and are clean.

Fixes #2 (unified schema) and #3 (mojibake-fixed) verified end-to-end.
"""

from __future__ import annotations

import yaml

from vista_docs.analyze.consolidation_runner import run_consolidation
from vista_docs.validate.frontmatter import REQUIRED_KEYS, validate_doc_bytes

_FM = """\
---
title: {title}
doc_type: TM
doc_label: Technical Manual
doc_layer: {layer}
doc_subject: Audiometric Module
app_code: ACKQ
app_name: Quality Audiology and Speech Analysis and Reporting (QUASAR)
section: CLI
app_status: active
pkg_ns: ACKQ
patch_ver: '3'
group_key: 'ACKQ:ACKQ:3'
word_count: {wc}
pub_date: {date}
---

# {title}

## Introduction

This is the {title} body content describing the audiometric module in detail.

## Unique-{tag}

A section unique to {title} that should be preserved as an addendum.
"""


def _write(path, title, layer, wc, date, tag):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        _FM.format(title=title, layer=layer, wc=wc, date=date, tag=tag),
        encoding="utf-8",
    )


def test_consolidated_output_is_unified_and_clean(tmp_path):
    md_img = tmp_path / "md-img" / "ACKQ"
    _write(md_img / "v3.md", "QUASAR Version 3 Technical Manual", "anchor", 500, "June 2025", "a")
    _write(md_img / "v2.md", "QUASAR Version 2 Technical Manual", "anchor", 300, "Jan 2020", "b")

    out_dir = tmp_path / "consolidated"
    results = run_consolidation(tmp_path / "md-img", out_dir, min_versions=2)
    assert results, "expected at least one consolidated group"

    consolidated = [p for p in out_dir.rglob("*.md") if p.name != "consolidation_summary.md"]
    assert consolidated, "expected consolidated output files"

    for path in consolidated:
        raw = path.read_bytes()
        # Hard guardrail: zero violations (valid YAML, required keys, section, …).
        assert validate_doc_bytes(raw) == [], f"{path} failed validation"

        fm = yaml.safe_load(raw.decode("utf-8").split("---\n")[1])
        # Inherited canonical keys present and non-empty:
        for k in REQUIRED_KEYS:
            assert fm.get(k), f"{path} missing required key {k}"
        # Consolidation provenance extras carried as additional keys:
        assert fm["master_source"]
        assert fm["consolidated_from"].endswith("versions")
        assert isinstance(fm["prior_versions"], list) and fm["prior_versions"]
        assert fm["section"] == "CLI"
