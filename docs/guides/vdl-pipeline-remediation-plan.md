# VDL Pipeline Remediation Plan

**Source assessment:** `guides/vdl-search-assessment.md`
**Scope:** Concrete pipeline changes in `vista-docs` (this repo) needed to fix the 11 issues catalogued in the assessment.
**Target artifacts produced/affected:**
- `~/data/vista-docs/inventory/vdl_inventory_enriched.csv` (public index, consumed by `vistadocs.github.io`)
- `~/data/vista-docs/md-img/**/*.md` (markdown corpus, mirrored to `vistadocs/vdl`)
- `~/data/vista-docs/state/frontmatter.db` (canonical post-ingest DB)

This plan is implementation-only. It does **not** repeat the rationale from the assessment; it lists what to change, where, in what order, and how to verify.

---

## 0. Map of where each issue gets fixed

| Assessment § | Issue | Pipeline stage | File(s) of record |
|---|---|---|---|
| 3.1 | UTF-8 mojibake | ingest (4) + enrich-inventory | `src/vista_docs/ingest/postprocess.py` (new pass) and `scripts/enrich_inventory.py` |
| 3.2 | Source-document typos | enrich-inventory | `scripts/enrich_inventory.py` + new `data/typo_corrections.yaml` |
| 3.3 | `app_name_full` inconsistency | enrich-inventory | `scripts/enrich_inventory.py` + new `data/package_master.yaml` |
| 3.4 | Multiple abbrevs / same package | enrich-inventory | `data/package_master.yaml` (alias rows) |
| 3.5 | `doc_code` → `doc_label` drift | enrich-inventory | `scripts/enrich_inventory.py` (canonical map already partial — finish it) |
| 3.6 | Sparse `pkg_ns` | enrich-inventory | `data/package_master.yaml` |
| 3.7 | Section name parenthetical | enrich-inventory | `scripts/enrich_inventory.py::SECTION_CODE` |
| 3.8 | Heading-level variance | ingest (4) | `src/vista_docs/ingest/postprocess.py` |
| 3.9 | Doc-level vs package-level status | enrich-inventory + post-ingest 6.7 | already partly addressed via `is_latest`; bridge to CSV |
| 3.10 | Markdown coverage | ingest (4) — incremental | tracked, not coded as one-shot |
| §4 | CSV → markdown linking (`github_md_url`) | post-ingest 6 → enrich-inventory | new `pipeline/build_md_url_map.py` + `scripts/enrich_inventory.py` |

The three high-priority root-cause fixes — 3.3, 3.4, 3.6 — collapse to **one artifact**: `data/package_master.yaml`. Build that first.

---

## 1. Phase ordering

Phases are ordered so each delivers a shippable CSV refresh and so later phases depend only on artifacts that earlier phases produced.

| Phase | Deliverable | Depends on |
|---|---|---|
| **P1** | `data/package_master.yaml` + enrich consumes it | — |
| **P2** | mojibake + typo cleanup at enrich | — (parallel to P1) |
| **P3** | canonical `doc_code` → `doc_label` finalized | P1 (so it can be applied in same pass) |
| **P4** | `github_md_url` column + mapping builder | post-ingest 6 already done |
| **P5** | heading-level normalization in ingest | — |
| **P6** | doc-level `is_latest` surfaced in CSV | post-ingest 6.7 (already done) |
| **P7** | section-name cleanup, schema metadata stamp | trivial; bundle with P1 |
| **P8** | markdown-coverage backlog reporter | P4 |

P1–P3 + P7 are achievable in one CSV refresh. P4 needs the mapping builder. P5–P6 are independent and can ship anytime.

---

## 2. P1 — Package-master table (fixes 3.3, 3.4, 3.6)

### 2.1 New file: `data/package_master.yaml`

Authoritative, hand-curated, keyed by `app_name_abbrev` (the VDL abbreviation as it appears in the inventory CSV today). One entry per VDL-known abbreviation.

Schema:

```yaml
# data/package_master.yaml
# Authoritative VistA package master table.
# Source seed: distinct app_name_abbrev values from vdl_inventory_enriched.csv
# Curation: hand-edited; no per-document subjectivity allowed in canonical fields.

packages:
  PXRM:
    canonical_name: "Clinical Reminders"
    pkg_ns: "PXRM"            # M namespace (FileMan #9.4 NAMESPACE field)
    canonical_pkg: "PXRM"     # post-consolidation identity (= self for non-merged)
    aliases: []               # other abbrevs that should also resolve here
    notes: ""

  KMPR:
    canonical_name: "Resource Usage Monitor"
    pkg_ns: "KMPR"
    canonical_pkg: "KMPR"
    aliases: ["RUM"]          # legacy abbrev that pre-dates KMP* consolidation

  RUM:
    canonical_name: "Resource Usage Monitor"
    pkg_ns: "KMPR"
    canonical_pkg: "KMPR"     # legacy; CSV rows still appear under RUM
    aliases: []

  ANRV:
    canonical_name: "Visual Impairment Service Team (VIST)"
    pkg_ns: "ANRV"
    canonical_pkg: "ANRV"
    aliases: []
  # ... one entry per distinct abbrev
```

Rule for `canonical_name` selection when source CSV has multiple `app_name_full`:
- Prefer the value that matches the VistA `PACKAGE` file #9.4 NAME if available
- Else the value that does *not* contain a colon-prefixed subject (`X: Y`)
- Else the most frequent in the inventory

### 2.2 Seeding

Add a small seeding utility (do **not** check seeded YAML in until reviewed):

```
scripts/seed_package_master.py
  --inventory ~/data/vista-docs/inventory/vdl_inventory.csv
  --out data/package_master.seed.yaml
```

Output groups every distinct `app_name_abbrev` with the set of `app_name_full` values seen and their counts; a human edits this into `package_master.yaml`. The 14 inconsistent abbreviations from §3.3 + the 5 multi-abbrev cases from §3.4 are the curation targets.

### 2.3 Consumer changes — `scripts/enrich_inventory.py`

Add at module top:

```python
PACKAGE_MASTER = Path(__file__).parent.parent / "data" / "package_master.yaml"
```

Load once at startup; build two indexes:
- `by_abbrev: dict[str, dict]` — direct lookup
- `alias_to_canonical: dict[str, str]` — alias abbrev → canonical abbrev

Replace the per-row derivation of `app_name_full` and `pkg_ns` with table lookup:

```python
master = PACKAGE_MASTER_BY_ABBREV.get(row["app_name_abbrev"])
if master:
    row["app_name_full"]   = master["canonical_name"]
    row["pkg_ns"]          = row.get("pkg_ns") or master["pkg_ns"]
    row["canonical_pkg"]   = master["canonical_pkg"]
else:
    row["canonical_pkg"]   = row["app_name_abbrev"]   # passthrough
    # leave app_name_full and pkg_ns at their derived values; flag for curation
```

The previously-derived `app_name_full` (which often holds a per-document subject) moves into a new column `doc_subject_raw` for fidelity. The existing `doc_subject` (from `extract_subject`) is unchanged.

### 2.4 New CSV columns

| Column | Source | Notes |
|---|---|---|
| `canonical_pkg` | package master | always populated |
| `doc_subject_raw` | original `app_name` parens-stripped | fidelity copy of pre-canonicalization value |

`pkg_ns` keeps its name and column position; coverage rises to ~100% for any abbrev present in `package_master.yaml`. Rows whose abbrev is absent from the master are flagged in the data-quality report.

### 2.5 Verification

- `pkg_ns` non-blank rate: target ≥ 99% (from current 74%)
- `app_name_full` per `app_name_abbrev` distinct count: target = 1 for every abbrev in master
- Snapshot diff: spot-check `OR`, `XU`, `PXRM`, `LR`, `SD`, `MPIF`, `KMPR`/`RUM` in old vs new CSV
- Unit tests in `tests/unit/test_enrich_package_master.py` cover the loader + fallback when master is missing an abbrev

---

## 3. P2 — Text cleanup (fixes 3.1, 3.2)

### 3.1 Mojibake correction

Add `ftfy>=6.2` to `pyproject.toml` (runtime dep, `[project.dependencies]`), `uv lock`, commit lock.

In `scripts/enrich_inventory.py`, before the main row loop:

```python
import ftfy

TEXT_FIELDS = ("doc_title", "doc_subject", "app_name_full", "app_name")

def fix_text(s: str) -> str:
    if not s:
        return s
    return ftfy.fix_text(s, normalization="NFC")
```

Apply to every row at read time. Same logic also runs once over `vdl_inventory.csv` source if mojibake originates upstream — but that file is the crawl output; applying at enrich is sufficient because enrich is the public-facing artifact.

For the markdown corpus (the `vistadocs/vdl` content tier), add a one-time backfill: `pipeline/fix_mojibake.py` walks `~/data/vista-docs/md-img/**/*.md`, runs `ftfy.fix_text` over body and frontmatter, writes back if changed. This is **idempotent and safe to re-run**.

### 3.2 Typo corrections

New file: `data/typo_corrections.yaml`

```yaml
# Hand-curated. Each entry replaces `source` with `corrected` in selected fields.
# Add new entries when a search-affecting typo is discovered.
corrections:
  - source: "Staph Aurerus"
    corrected: "Staph Aureus"
    fields: [doc_title, doc_subject, app_name_full]
  - source: "DIBORG"
    corrected: "DIBRG"
    fields: [doc_title, doc_subject]
  - source: "Health Data  Informatics"   # double-space
    corrected: "Health Data Informatics"
    fields: [app_name_full]
```

In enrich, after `fix_text`, apply corrections:

```python
def apply_typos(value: str, field: str) -> str:
    for c in TYPO_CORRECTIONS:
        if field in c["fields"] and c["source"] in value:
            value = value.replace(c["source"], c["corrected"])
    return value
```

### 3.3 Search-side fallback (cheap)

To preserve searchability on the original spelling without bloating the CSV: emit a sibling `doc_search_aliases` column listing original-spelling tokens that were corrected on this row. The web table can include this column in DataTables' search index but hide it from view.

```
doc_search_aliases: "Aurerus|DIBORG"
```

### 3.4 Verification

- `tests/unit/test_text_fixers.py`: 12+ table-driven cases for each mojibake pattern from §3.1 of the assessment, plus typo corrections
- Mojibake regex sweep on output CSV: 0 hits for `â€™`, `â€"`, `Â`, `Ã©`, `Ã¨`
- Typo regex sweep: 0 hits for entries in `typo_corrections.yaml` outside `doc_search_aliases`

---

## 4. P3 — Canonical `doc_code` → `doc_label` (fixes 3.5)

`scripts/enrich_inventory.py` already has `DOC_LABELS` infrastructure (line ~189, "Each entry: (regex pattern, doc_code, canonical doc_label)"). The drift comes from the suffix-fallback path picking up the document's own title text rather than a canonical label.

### 4.1 Make canonical labels authoritative

Add a top-level dict and apply it as the **last** step before write:

```python
CANONICAL_DOC_LABELS = {
    "RN":   "Release Notes",
    "DIBR": "Deployment, Installation, Back-Out, and Rollback Guide",
    "IG":   "Installation Guide",
    "TM":   "Technical Manual",
    "UG":   "User Guide",
    "UM":   "User Manual",
    "CFG":  "Configuration Guide",
    "INT":  "Interface Specification",
    "REF":  "Reference",
    "POM":  "Production Operations Manual",
    "SG":   "Security Guide",
    "VDD":  "VistA Database Design",
    # ... fill the full set from the existing DOC_LABELS regex table
}

# After all derivations:
if row["doc_code"] in CANONICAL_DOC_LABELS:
    if row["doc_label"] != CANONICAL_DOC_LABELS[row["doc_code"]]:
        row["doc_subtitle"] = row["doc_label"]   # preserve the per-doc wording
        row["doc_label"]    = CANONICAL_DOC_LABELS[row["doc_code"]]
```

### 4.2 New CSV column

| Column | Source | Notes |
|---|---|---|
| `doc_subtitle` | original non-canonical label (e.g. "Manager/ADPAC Guide") | empty when label is already canonical |

### 4.3 Verification

- Group-by `doc_code` over output CSV, count distinct `doc_label`: every code → 1 label
- Spot-check the 5 codes from §3.5 (`CFG`, `INT`, `REF`, `UG`, `UM`)
- DataTables Doc Type dropdown collapses cleanly

---

## 5. P4 — `github_md_url` column (fixes §4 / 3.10 surface)

**Revised after pre-P4 audit (see §14 follow-ups).** The original plan called for a new post-ingest stage 6.4 reading from `frontmatter.db`. Investigation showed `~/data/vista-docs/publish/` is the canonical mirror of `github.com/vistadocs/vdl` and already encodes the full anchor/patch/plain layout, with the join keys we need sitting in each .md file's own frontmatter. Building the URL map directly from `publish/` is simpler, has one less moving part, and aligns with the consolidation strategy decision (anchor-first, per the discussion that preceded this revision).

### 5.1 New module: `src/vista_docs/publish/url_map.py`

Pure-ish builder. Walks `~/data/vista-docs/publish/` and emits a `patch_id → publish-relative-path` map. Each .md file in publish/ has one of three frontmatter shapes:

| File source | Detected by | Join keys it contributes |
|---|---|---|
| Anchor (consolidated multi-version) | `master_source:` + `prior_versions:` keys | First whitespace-token of `master_source` and each `prior_versions` entry — e.g. `"DG*5.3*952 DIBRG"` → `"DG*5.3*952"`. ~9 keys typical, all map to the same anchor URL. |
| Plain singleton (mirrored from `md-img/`) | `patch_id:` set, no `master_source` | The `patch_id` value (often anchor-style like `"ADT*5.3"`). |
| Patch under `patches/` subdir | `patch_id:` set, no `master_source` | The `patch_id` value (always `"NS*V*P"`). |

`INDEX.md` and `README.md` are skipped.

Pure functions:

```python
def parse_patch_id(source_token: str) -> str:
    """Extract patch_id from a master_source / prior_versions entry.
    'DG*5.3*952 DIBRG' -> 'DG*5.3*952'
    """

def keys_from_frontmatter(fm: dict) -> list[str]:
    """Return all patch_id keys this entry contributes."""
```

I/O thin layer:

```python
def walk_publish_tree(publish_root: Path) -> dict[str, str]:
    """Walk publish/, return {patch_id: rel_path_to_md}."""

def write_url_map_json(publish_root: Path) -> dict:
    """Walk + write publish/url_map.json with full URLs."""
```

`url_map.json` schema:

```json
{
  "generated_at": "2026-05-04T...",
  "github_owner": "vistadocs",
  "github_repo": "vdl",
  "branch": "main",
  "entries": {
    "DG*5.3*952": "clinical/adt--admission-discharge-transfer/deployment-installation-back-out-and-rollback-guide--dibrg.md",
    "DG*5.3*916": "clinical/adt--admission-discharge-transfer/deployment-installation-back-out-and-rollback-guide--dibrg.md",
    "DG*5.3*864": "clinical/adt--admission-discharge-transfer/patches/dg-5-3-864--installation-guide.md"
  }
}
```

### 5.2 Optional integration with publish runner

Phase A (immediate): standalone — `python -c "from vista_docs.publish.url_map import write_url_map_json; write_url_map_json(...)"`. Run after `vista-docs publish`. No mandatory wiring.

Phase B (follow-up): call `write_url_map_json` from `publish/runner.py::run_publish` so it's always fresh after a publish. One-line addition.

### 5.3 Consumer change in `scripts/enrich_inventory.py`

After all other derivations:

```python
url_map_path = Path("/home/rafael/data/vista-docs/publish/url_map.json")
if url_map_path.exists():
    data = json.loads(url_map_path.read_text())
    entries = data["entries"]
    base = f"https://github.com/{data['github_owner']}/{data['github_repo']}/blob/{data['branch']}"
    raw  = f"https://raw.githubusercontent.com/{data['github_owner']}/{data['github_repo']}/{data['branch']}"
else:
    entries, base, raw = {}, "", ""

# In the per-row loop:
rel = entries.get(row["patch_id"], "")
row["github_md_url"]     = f"{base}/{rel}"     if rel else ""
row["github_md_raw_url"] = f"{raw}/{rel}"      if rel else ""
```

The CSV's `patch_id` is the universal join key:
- Anchor docs: `patch_id == "NS*V"` (e.g. `"ADT*5.3"`) — matches plain-singleton publish entries.
- Patch docs: `patch_id == "NS*V*P"` (e.g. `"DG*5.3*864"`) — matches either an anchor (consolidated case, many-to-one) or a `patches/{patch_id}--{label}.md` file (singleton patch case).
- Plain docs (no patch_ver, no patch_num): `patch_id == ""` — no match, empty URL. Correct: these are usually noise (VBA forms, va_ref).
- 20 versionless patches: `patch_id == ""` (because patch_ver is missing). No match. Documented gap (§14).

### 5.4 New CSV columns

| Column | Notes |
|---|---|
| `github_md_url` | empty if no markdown counterpart |
| `github_md_raw_url` | empty if no markdown counterpart |

### 5.5 Web UI follow-up (out of repo scope)

Documented for the `vistadocs.github.io` maintainer:
- Add column entry in `COLS` for `github_md_url`
- Render as `<a href="...">MD</a>` orthogonal column (similar to existing PDF/DOCX render)
- Add help-text note about anchor consolidation per assessment §4.5

### 5.6 Verification

- `tests/unit/test_url_map.py`: pure-function coverage of `parse_patch_id` and `keys_from_frontmatter`
- After running `write_url_map_json` against real `publish/`: assert all 9 patches in the ADT DIBR group resolve to the same anchor URL
- After `enrich_inventory`: assert row count where `github_md_url != ""` matches the count of CSV `patch_id` values that have a corresponding entry in `url_map.json`
- Spot-check that 2 CSV rows (PDF + DOCX) for the same logical doc resolve to the same URL
- HEAD probe a sample of 50 URLs after the next `vista-docs push` to verify no 404s

---

## 6. P5 — Heading-level normalization (fixes 3.8)

Add to `src/vista_docs/ingest/postprocess.py` (the existing post-Docling pass). New function:

```python
def normalize_top_heading_level(md: str) -> str:
    """If the topmost heading is not H1, promote all heading levels uniformly
    so that the topmost becomes H1. Idempotent."""
    headings = [m for m in HEADING_RE.finditer(md)]
    if not headings:
        return md
    min_level = min(len(m.group(1)) for m in headings)
    if min_level == 1:
        return md
    delta = min_level - 1
    return HEADING_RE.sub(
        lambda m: "#" * (len(m.group(1)) - delta) + m.group(2),
        md,
    )
```

Where `HEADING_RE = re.compile(r"^(#{1,6})(\s.*)$", re.MULTILINE)`.

Wire into the post-ingest sequence. Add unit test with the GMRC-style H2-top fixture (3 known cases per assessment §3.8).

One-time backfill: `pipeline/normalize_headings.py` walks `~/data/vista-docs/md-img/**/*.md`, applies the same function, writes back if changed. Safe to re-run.

### Verification

- After backfill: scan all 1,418 markdown files; topmost heading level is `#` for ≥99% (allow exception list for edge cases)
- Subsequent `make ingest` runs do not regress — confirmed by the post-ingest unit test

---

## 7. P6 — Surface doc-level `is_latest` in CSV (fixes 3.9 partially)

Stage 6.7 (`pipeline/apply_quality_views.py`) already populates `documents.is_latest` per anchor/patch group. Bridge into the public CSV.

### 7.1 New CSV column

| Column | Source | Notes |
|---|---|---|
| `doc_is_latest` | `documents.is_latest` joined by `patch_id_full` | `1` for the most-current document in its functional group, `0` otherwise; empty for rows without a markdown counterpart |

Implementation: the same `doc_url_map` join opened in P4 already gives access to the DB; add `is_latest` to the SELECT. No new infrastructure.

### 7.2 Verification

- For each `(canonical_pkg, doc_code, doc_layer)` group, exactly one `doc_is_latest == 1` row exists when at least one such row has a markdown counterpart
- Count of `doc_is_latest == 1 AND app_status == 'archive'` is small but nonzero (confirms the metric is genuinely doc-level, not package-level)

---

## 8. P7 — Trivial schema cleanup (fixes 3.7) and metadata stamp (open question §6.2)

### 8.1 Section-name cleanup

In `scripts/enrich_inventory.py::SECTION_CODE`, split the historical note off:

```python
SECTION_NAME_REWRITES = {
    "VistA/GUI Hybrids (formerly HealtheVet)": ("VistA/GUI Hybrids", "formerly HealtheVet"),
}

# In the row loop:
clean, note = SECTION_NAME_REWRITES.get(row["section_name"], (row["section_name"], ""))
row["section_name"]  = clean
row["section_notes"] = note   # new column
```

### 8.2 CSV metadata stamp

Add a sibling JSON file alongside the CSV at write time:

```
~/data/vista-docs/inventory/vdl_inventory_enriched.meta.json
{
  "generated_at": "2026-05-04T12:34:56Z",
  "row_count": 8834,
  "schema_version": "2026-05",
  "package_master_sha": "<git sha of data/package_master.yaml>",
  "frontmatter_db_mtime": "2026-05-03T22:10:00Z"
}
```

This addresses open question §6.2 of the assessment without bloating every row.

---

## 9. P8 — Markdown coverage backlog (operationalizes 3.10)

Add `pipeline/coverage_report.py`:

Reads the enriched CSV after a refresh and emits `~/data/vista-docs/inventory/coverage_backlog.csv` with columns:

```
canonical_pkg, app_status, doc_code, doc_layer, patch_id_full,
doc_url, has_markdown
```

filtered to rows where `github_md_url == "" AND app_status == 'active' AND doc_code IN ('DIBR','IG','TM','RN','UG','UM')`. Sort by package activity then doc_code.

This operationalizes the §3.10 prioritization without committing to a specific conversion target — it's a backlog the maintainer pulls from.

---

## 10. Data-quality report (catch regressions)

After every enrich-inventory run, write `~/data/vista-docs/inventory/data_quality_report.md` containing:

| Check | Current | Target | Status |
|---|---|---|---|
| `pkg_ns` populated | 99.4% | ≥99% | ✅ |
| `app_name_full` distinct per abbrev (max) | 1 | 1 | ✅ |
| `doc_label` distinct per code (max) | 1 | 1 | ✅ |
| Mojibake patterns in any text col | 0 | 0 | ✅ |
| Known typos (uncorrected) | 0 | 0 | ✅ |
| `github_md_url` coverage | 39% | rises with §3.10 | — |
| Rows with empty `canonical_pkg` | 0 | 0 | ✅ |

Each check maps 1:1 to assessment §7. Implement each as a function in a new module `src/vista_docs/enrich/quality.py` so they're independently unit-testable; the runner just dispatches and tabulates.

CI gate: `make check` runs the quality checks against the latest enriched CSV (when present) and fails the build on regression of any line marked ≥M priority.

---

## 11. File-by-file change summary

**New files**
- `data/package_master.yaml` (curated)
- `data/typo_corrections.yaml` (curated)
- `pipeline/build_md_url_map.py` (stage 6.4)
- `pipeline/fix_mojibake.py` (one-time + safe re-run)
- `pipeline/normalize_headings.py` (one-time + safe re-run)
- `pipeline/coverage_report.py`
- `scripts/seed_package_master.py` (developer tool, not a stage)
- `src/vista_docs/enrich/quality.py`
- `tests/unit/test_enrich_package_master.py`
- `tests/unit/test_text_fixers.py`
- `tests/unit/test_heading_normalize.py`
- `tests/unit/test_doc_url_map.py`

**Modified files**
- `scripts/enrich_inventory.py` — load master + typo + canonical labels + URL map; emit new columns
- `src/vista_docs/ingest/postprocess.py` — add `normalize_top_heading_level`
- `pipeline/README.md` — insert stage 6.4
- `pyproject.toml` — add `ftfy`; add `pyyaml` if not already present
- `Makefile` — add `make enrich-inventory`, `make coverage-report`, `make data-quality`

**No-change files**
- `src/vista_docs/crawl/*` — input CSV is unchanged
- `src/vista_docs/manifest/*` — pipeline.db unchanged
- `pipeline/apply_quality_views.py` — already produces `is_latest`; no edits

---

## 12. CSV schema delta (one-glance reference)

| Column | Add / Modify | Source |
|---|---|---|
| `canonical_pkg` | **add** | `data/package_master.yaml` |
| `pkg_ns` | modify (coverage) | `data/package_master.yaml` |
| `app_name_full` | modify (canonical) | `data/package_master.yaml` |
| `doc_subject_raw` | **add** | original `app_name` parens-stripped |
| `doc_label` | modify (canonical) | `CANONICAL_DOC_LABELS` |
| `doc_subtitle` | **add** | pre-canonical label string |
| `doc_search_aliases` | **add** | original-spelling tokens for typo'd rows |
| `section_name` | modify (cleaned) | `SECTION_NAME_REWRITES` |
| `section_notes` | **add** | parenthetical historical note |
| `github_md_url` | **add** | `doc_url_map` |
| `github_md_raw_url` | **add** | `doc_url_map` |
| `doc_is_latest` | **add** | `documents.is_latest` |

All other columns unchanged. Column order: keep existing positions for current columns; append new ones at the right of their conceptual group (identity → URLs → quality).

---

## 13. Acceptance criteria

The remediation is complete when, on a fresh `make pipeline && make enrich-inventory` run:

1. `data_quality_report.md` shows green for every M+ check (§10)
2. `git diff` of `vdl_inventory_enriched.csv` shows non-empty `github_md_url` for every row whose `patch_id_full` corresponds to an existing markdown file
3. The web table at `vistadocs.github.io` (after the parallel UI PR) shows a "MD" link in the right column on those rows
4. No mojibake regex match anywhere in the CSV
5. `pkg_ns` populated rate ≥ 99%
6. Every `app_name_abbrev` resolves to a single `app_name_full`
7. Every `doc_code` resolves to a single `doc_label`
8. CI quality gate is wired into `make check`

Open questions §6 of the assessment are deferred — they are policy decisions, not pipeline blockers.

---

## 14. Out-of-phase follow-ups

Items uncovered during P1–P8 implementation that don't fit any current phase. Captured here so they aren't lost; promote into a phase only if they become load-bearing.

| Discovered in | Item | Why it's not in a phase |
|---|---|---|
| P2 | `package_master.py` could apply `fix_mojibake` to `canonical_name` at load time, defending against future bootstraps that re-introduce mojibake from raw inventory. | Cost of one stale entry was 30 seconds to fix by hand (MMRS / "Aurerus"). Worth doing only if mojibake reappears in the master more than once. |
| P1 | 35 abbrevs in `data/package_master.yaml` still have empty `pkg_ns` — mostly web apps and external-facing services where the M namespace is genuinely unclear (KAAJEE, HL7, DHT, MJCF, HDR, …). | Pure curation work, no code change. Each entry needs a person who knows the package's M-side identity. Closing this gap takes `pkg_ns` coverage from 93.7% → ≥99%. |
| P1 | The bootstrap step that produced `data/package_master.yaml` was a one-off `/tmp` script. If the source inventory adds new abbrevs, re-bootstrapping requires recreating that logic. | The `scripts/seed_package_master.py` tool already handles re-seeding; the curation overrides are codified in the YAML itself. Only worth promoting if abbrev churn becomes frequent. |
| P3-audit | `src/vista_docs/migrate/repo_builder.py::_DOC_TYPE_LABEL` is a separate label table for the retired migrate/ subsystem (no CLI exposure per `src/vista_docs/README.md`). It uses lowercase normalized keys (`installation-guide`, `release-note`, …), not the inventory codes (RN, IG). | Different vocabulary, retired subsystem. Don't fold into `data/doc_labels.yaml`. If migrate/ is ever revived, design a separate `data/normalized_doc_labels.yaml`. |
| P3-audit | `src/vista_docs/publish/builder.py::_SECTION_RENAMES` has its own kebab-case rule for `"VistA/GUI Hybrids (formerly HealtheVet)" → "vista-gui-hybrids"`. Will overlap with assessment §3.7 (`section_notes` column). | Will be unified in P7 when section-name cleanup runs at enrich time. The kebab transform is local to publish-tree filename generation; both can survive in parallel for now. |
| Audit | `vdl_inventory_enriched.csv` has 20 patch-layer rows where `patch_ver=""` but `patch_num` is set, so `patch_id=""` and `group_key=""`. They cannot be matched to an anchor by `patch_id_full`. | Upstream extraction gap in `parse_row`. They will appear in P4 with empty `github_md_url` and should be flagged in the data-quality report (§10) as a known gap. |
| Pre-P4 audit | Local `~/data/vista-docs/publish/` tree carries 34,382 PNG files (~1.9 GB). Sampling shows ~80% are decorative chrome — VA seal cover images (one hash appears in 20% of `001.png` files), VistA logos, cursor icons, page-divider widgets — and ~20% are genuine UI screenshots / diagrams. **These images are already excluded from the github.com/vistadocs/vdl repo via `publish/.gitignore` (`*.png`, `*.jpg`, … per `publish/runner.py::_GITIGNORE`)**, so they cost zero upload bandwidth and have zero impact on search/query infrastructure (CSV index, web table, frontmatter.db FTS, github mirror). Pure local disk hygiene. | Three options if hygiene matters later: (a) hardlink-dedupe identical boilerplate (~30% disk recovery, zero risk); (b) drop all PNGs from `publish/` (regeneratable from `md-img/` via `vista-docs publish`); (c) prune only `< 50 KB` images (`find publish -name '*.png' -size -50k -delete`) to keep real screenshots and drop chrome. Not blocking anything — defer until disk pressure is real. |

**Bugs fixed mid-flight (not deferred):**

| When | Bug | Resolution |
|---|---|---|
| P2 | `data/package_master.yaml::MMRS::canonical_name` was bootstrapped from the typo'd inventory ("Staph Aurerus"). | Fixed in master; defensive sweep of all curated YAMLs added (`tests/unit/test_text_fixers.py` and `data/typo_corrections.yaml`). |
| Pre-P4 | `src/vista_docs/publish/builder.py::DOC_LABELS` had its own upper-case label table that drifted from `data/doc_labels.yaml` (REF, SM differed). Would have produced broken `github_md_url` values in P4. | Replaced inline upper-case codes with a `load_doc_labels(CURATED_DATA_DIR / "doc_labels.yaml")` import. Lower-case normalized keys (a different vocabulary) remain inline. New regression test `test_uppercase_codes_match_canonical_yaml` locks them in lock-step. |
| Pre-P4 | Stale 60 KB `data/package_master.seed.yaml` left over from the P1 bootstrap; not loaded by anything. | Identified for deletion (rm denied — left for user to remove). |

When picking up an item from this list, either fold it into an existing phase (if scope-aligned) or create a new phase Pn+ with its own acceptance criteria — don't just inline-fix without recording the decision.
