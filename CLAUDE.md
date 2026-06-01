---
# Machine-readable project descriptor — schema v1 (2026-05-05).
name: vista-docs
kind: [pipeline, cli, data]
status: active
languages: [python]

runtime:
  needs:
    - python>=3.10
    - uv
    - "internet (only at crawl/fetch stages; downstream stages read disk)"
  optional:
    - "Docling (DOCX/PDF → markdown)"
  excludes: []

distribution:
  pypi: null
  github: rafael5/vista-docs

location: ~/projects/vista-docs
data_location: ~/data/vista-docs                # output never in this repo

exposes:
  cli:
    - "vista-docs (Click; subcommands per pipeline stage)"
  python_api: src/vista_docs/
  pipeline_stages:
    - "1. crawl — VDL HTML → catalog records"
    - "2. classify — filename/title → DocType"
    - "3. fetch — URL derivation + HTTP download"
    - "4. ingest — DOCX/PDF → markdown via Docling + post-processing"
    - "5. enrich — extract metadata from markdown, rewrite YAML frontmatter"
    - "6. audit — normalize frontmatter + audit DB"
    - "6.5 chunk — heading tree + FTS5 index"
    - "6.6 entities — routines/globals/options/rpcs/codes"
    - "6.7 quality — is_latest + quality_score + views"
  formats_produced:
    - "~/data/vista-docs/md-img/ (markdown + extracted images)"
    - "~/data/vista-docs/state/frontmatter.db (SQLite — consumed by vista-cli + vista-docs-api)"

consumes:
  formats: ["VDL HTML catalog", "DOCX", "PDF"]
  services: ["VA Document Library (vdl.va.gov)"]

companions:
  - project: vista-docs-api
    relation: "downstream — FastAPI server reads frontmatter.db (stage 7)"
  - project: vista-cli
    relation: "downstream — joins frontmatter.db with vista-meta TSVs into a queryable surface"
  - project: vista-meta
    relation: "complementary — vista-meta supplies code+data models from a live VistA; vista-docs supplies the documentation corpus"

incompatibilities:
  - "Output data lives in ~/data/vista-docs/, never in the repo. Don't commit pipeline output."
  - "Crawl/fetch stages need network; downstream stages must run offline (no live network calls past stage 3)."
  - "Skills under ~/claude/skills/ (vdl, vdl-pipeline, vista-system, vista-fileman, va-docx-structure) are required reading for changes to crawler / ingest / enrich stages."

docs:
  primary: README.md
  skills:
    - "~/claude/skills/vdl"
    - "~/claude/skills/vdl-pipeline"
    - "~/claude/skills/vista-system"
    - "~/claude/skills/vista-fileman"
    - "~/claude/skills/va-docx-structure"
---

# Claude Project Context — vista-docs

## What this project is

`vista-docs` is a TDD Python pipeline that crawls the VA VistA Document Library (VDL),
downloads DOCX/PDF manuals, converts them to structured markdown, and analyses the corpus.
Output data lives in `~/data/vista-docs/` — never in this repo.

## Skills
- `~/claude/skills/vdl/` — VDL catalog structure, URL patterns, crawling gotchas
- `~/claude/skills/vdl-pipeline/` — complete operating manual: CLI, stages, enrich fields, gotchas
- `~/claude/skills/vista-system/` — VistA package architecture, namespaces, relationships
- `~/claude/skills/vista-fileman/` — FileMan APIs, global conventions, data dictionary
- `~/claude/skills/va-docx-structure/` — DOCX structure survey, ingest post-processing, callout patterns
- `~/claude/skills/knowledge-capture/` — capture new findings back to skills after each session

## Project structure

```
src/vista_docs/         ← canonical ETL pipeline (stages 1-5)
  models/               — pure dataclasses (no logic, no I/O)
  crawl/                — VDL HTML → catalog records
  classify/             — filename/title → DocType
  fetch/                — URL derivation + HTTP download
  ingest/               — DOCX/PDF → markdown via Docling + post-processing
  enrich/               — extract metadata from markdown, rewrite YAML frontmatter
  survey/               — corpus structure analysis (stats.py pure; analyzer.py I/O)
  manifest/             — SQLite pipeline state management
  cli/                  — `vista-docs` Click command with subcommands

pipeline/               ← post-ingest stages 6-6.7 (operate on md-img + frontmatter.db)
  audit_frontmatter.py    — stage 6    normalize frontmatter + audit DB
  chunk_sections.py       — stage 6.5  heading tree + FTS5 index
  extract_entities.py     — stage 6.6  routines/globals/options/rpcs/codes
  apply_quality_views.py  — stage 6.7  is_latest + quality_score + views
  README.md               — stage reference

scripts/                ← ad-hoc / one-off tools (NOT part of automated pipeline)
  enrich_inventory.py     — produces vdl_inventory_enriched.csv (active, run on demand)
  README.md               — historical inventory

tests/
  unit/                 — fast, no I/O, no network (run in CI)
  integration/          — SQLite, file I/O, optional network (@pytest.mark.network)
  fixtures/             — static HTML/DOCX/manifest test data (committed, small)

guides/                 ← synthesised reference docs (hand-edited)
```

**Rule:** all active library code lives under `src/vista_docs/`. Top-level
`.py` files are not permitted — put stable stages in `pipeline/`, one-off
scripts in `scripts/`, or promote into `src/vista_docs/` with tests.

## Data directory (NOT in this repo)

```
~/data/vista-docs/
  inventory/     — VDL catalog CSV/JSON (from `vista-docs crawl`)
  state/         — pipeline.db + frontmatter.db SQLite (pipeline state)
  raw/           — downloaded DOCX/PDF by namespace (from `vista-docs fetch`)
  md-img/        — converted markdown + extracted images (from `vista-docs ingest`)
  survey/        — corpus analysis outputs (from `vista-docs survey` / `headings`)
  consolidated/  — master + addenda consolidation (from `vista-docs consolidate`)
  normalized/    — normalized markdown bodies (from `vista-docs normalize`)
  migration/     — corpus-manifest.json (from `vista-docs manifest`)
  publish/       — human-browsable GitHub tree (from `vista-docs publish`)
```

## Dev workflow

```bash
make install    # create .venv, install deps, install pre-commit hooks
make test       # run unit tests only (fast)
make test-lf    # rerun only last-failed
make watch      # TDD mode: auto-rerun on file save
make cov        # pytest + coverage report (95% min)
make check      # lint + mypy + cov (full gate = CI)
make format     # auto-format with ruff
make push       # check + git push
make pull       # git pull origin main

# Pipeline targets (each wraps the matching vista-docs subcommand)
make crawl        # → ~/data/vista-docs/inventory/
make fetch        # → ~/data/vista-docs/raw/
make ingest       # → ~/data/vista-docs/md-img/
make enrich       # populate frontmatter in-place
make sync         # join inventory_enriched.csv fields into frontmatter
make survey       # → ~/data/vista-docs/survey/
make headings     # → ~/data/vista-docs/survey/heading_analysis/
make consolidate  # → ~/data/vista-docs/consolidated/
make manifest     # → ~/data/vista-docs/migration/corpus-manifest.json
make publish      # → ~/data/vista-docs/publish/
make validate     # frontmatter hard gate
make publish-push # regenerate publish/ then git push corpus (NOT `make push`)
make pipeline     # crawl → fetch → ingest → survey in order
```

**Note:** `make push` runs `check` + `git push` for *this repo*. The corpus
push to the docs GitHub is `make publish-push` (`vista-docs push`).

## CLI

```
# Acquire (stages 1-3) — writes pipeline.db
vista-docs crawl    [--delay N] [--snapshot] [--max-apps N]
vista-docs fetch    [--pkg CPRS] [--dry-run] [--force] [--delay N]
vista-docs ingest   [--pkg CPRS] [--scaffold] [--force]

# Enrich corpus (stages 4-5) — populate frontmatter in md-img/ in-place
vista-docs enrich   [--pkg CPRS] [--force]
vista-docs sync     [--pkg CPRS] [--force]            # join inventory_enriched.csv fields into FM

# Analysis (read-only over the enriched corpus)
vista-docs survey   [--pkg CPRS] [--output PATH]
vista-docs headings [--output PATH] [--min-docs N] [--boilerplate-threshold F] [--unique-threshold F]

# Delivery (markdown corpus → GitHub)
vista-docs consolidate [--output PATH] [--min-versions N] [--doc-type TYPE ...]
vista-docs manifest    [--output PATH] [--doc-type TYPE ...]
vista-docs publish     [--output PATH] [--pkg PKG ...] [--force] [--no-validate]
vista-docs validate    [--target PATH] [--md-img]     # hard gate before publish/push
vista-docs push        [--remote URL] [--message STR] [--no-publish]

# Orchestration
vista-docs pipeline [--pkg CPRS] [--from crawl|fetch|ingest|survey]   # crawl → fetch → ingest → survey

# Post-ingest DB build (stages 6-6.7) — run as scripts, write frontmatter.db
python3 pipeline/audit_frontmatter.py   [--force] [--pkg CODE] [--limit N]
python3 pipeline/chunk_sections.py      [--force] [--pkg CODE]
python3 pipeline/extract_entities.py    [--force] [--pkg CODE]
python3 pipeline/apply_quality_views.py                          # pure SQL; always re-runs
```

Full end-to-end architecture (ASCII + Mermaid + per-stage table): see
[`docs/vdl-arch-overview.md`](docs/vdl-arch-overview.md).

**Note:** `--pkg` takes the VDL `app_code` (CPRS, ADT, PSO), NOT the VistA M
namespace (OR, DG, PSO). These are not the same.

## Architecture rules

- **Pure functions in src/vista_docs/*/\*_pure_module\*.py**: zero I/O, zero side effects
- **I/O in thin layer modules**: wrap external dependencies, tested in integration only
- **Write test first**: every pure function has a unit test before implementation
- **TDD order**: models → crawl/parser → classify/rules → manifest/operations → fetch/strategy → ingest/postprocess → survey/detectors → cli

## Testing conventions

- `tests/unit/` — no filesystem, no network, no SQLite, no Docling
- `tests/integration/` — may use SQLite, local fixtures, optionally live VA
- Mark network tests: `@pytest.mark.network` (skipped unless `--run-network`)
- One test file per source module: `src/foo/bar.py` → `tests/unit/test_bar.py`
- Coverage minimum: 95% overall (enforced by pre-push hook)

## Environment

- Python 3.12, managed via `uv`
- Virtual env: `.venv/` (auto-activated via direnv + `.envrc`)
- Runtime deps: requests, python-docx, pyyaml, click
- Optional heavy dep: docling (DOCX/PDF → markdown) — install separately
- Lockfile: `uv.lock` — always commit after changing dependencies

## Adding a dependency

```bash
# 1. Add to pyproject.toml
# 2. Re-lock and sync:
uv lock && uv sync --extra dev
# 3. Commit both pyproject.toml and uv.lock
```

## Code style

- Formatter + linter: `ruff` only (no black)
- Line length: 100
- Rules: E, F, I (errors, pyflakes, isort)
- Pre-commit hooks enforce style on every commit

## Claude guidelines

- Prefer editing existing files over creating new ones
- Keep functions small and independently testable
- Pure functions take plain Python values, return plain Python values — no side effects
- Use `logging` not `print()` in library code
- No mocks unless unavoidable — prefer real objects and fakes
- After any session with new findings, update vdl-pipeline/SKILL.md and memory files
- Update `src/vista_docs/README.md` in the same commit whenever any package's inputs, outputs, CLI, or prerequisites change
- `--pkg` flag always takes VDL app_code (CPRS/ADT), never VistA namespace (OR/DG)
- Every new I/O layer goes into `[tool.coverage.run] omit` in pyproject.toml immediately
- New extractor TDD cycle: test → fail-confirm → implement → make check → enrich --force
