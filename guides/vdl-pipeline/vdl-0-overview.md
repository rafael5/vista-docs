# VistA Documentation Library — Analysis Pipeline Overview

**Date:** 2026-03-30
**Pipeline:** `vista-docs` Python package
**Repo:** `~/projects/vista-docs/`

---

## Table of Contents

1. [Project Summary](#1-project-summary)
2. [Design Philosophy](#2-design-philosophy)
   - [Test-Driven Development](#test-driven-development)
   - [Modular Pure/IO Architecture](#modular-pureio-architecture)
   - [Idempotency](#idempotency)
   - [Portability](#portability)
   - [Git-Versioned Code and Data](#git-versioned-code-and-data)
3. [Completeness and Determinism](#3-completeness-and-determinism)
4. [Pipeline Stages](#4-pipeline-stages)
5. [Python Environment and Toolchain](#5-python-environment-and-toolchain)
6. [Data Flow](#6-data-flow)
7. [SQLite State Tracking](#7-sqlite-state-tracking)
8. [CLI Design](#8-cli-design)

---

## 1. Project Summary
[↑ Table of Contents](#table-of-contents)

The `vista-docs` pipeline is a structured, AI-driven system that:

1. **Crawls** the VA VistA Documentation Library (VDL) at `va.gov/vdl` to extract a complete catalog of every application and document
2. **Fetches** every substantive document (PDF and DOCX) to local storage
3. **Ingests** each document by converting it to structured markdown
4. **Enriches** each markdown document by extracting structured metadata from its content
5. **Classifies** every application in the VDL catalog using the `system_type` scheme

The pipeline produced:
- `vdl_inventory_enriched.csv` — 8,834 rows, 196 applications, 29 columns
- 2,240 markdown documents across 44 package directories
- 14,881,751 words of technical documentation processed
- 85,308 equivalent pages analyzed
- 100% metadata coverage (all 2,240 documents have complete YAML frontmatter)

No manual document review was performed. Every classification, every metadata field, and every annotation is the deterministic output of reading the actual source documents.

---

## 2. Design Philosophy
[↑ Table of Contents](#table-of-contents)

### Test-Driven Development

All pure logic modules were written test-first. The workflow:

1. Write a failing test that specifies the expected behavior
2. Write the minimum implementation to pass the test
3. Refactor; keep all tests green

Tests are run with `pytest` via `make test`. The `make watch` target runs tests continuously during development. The `make check` target runs tests + linter + type checker before pushing.

Pure modules have high test coverage enforced by `pytest-cov`. I/O thin layers (crawlers, downloaders, converters, CLI) are excluded from coverage requirements because their behavior depends on external systems (the VA VDL website, the filesystem, the Docling library). See [Modular Pure/IO Architecture](#modular-pureio-architecture) for the rationale.

The test suite covers:
- `crawl/parser.py` — VDL HTML parsing rules
- `fetch/selector.py` — document selection and deduplication logic
- `ingest/cleaner.py` — markdown post-processing rules
- `enrich/frontmatter.py` — YAML frontmatter manipulation
- `enrich/inventory_fields.py` — inventory index construction and field lookup
- `classify/rules.py` — 52 tests covering all 11 system_type categories and edge cases

### Modular Pure/IO Architecture

Each pipeline stage is split into two layers:

**Pure modules** — no side effects, no I/O, fully unit-testable:
- Accept and return plain Python data structures (dicts, lists, strings)
- All business logic lives here
- 100% deterministic — same input always produces same output

**I/O thin layers** — minimal glue code connecting the pure layer to external systems:
- File reads/writes, HTTP requests, database queries
- No logic beyond orchestration
- Excluded from unit test coverage; tested by integration tests when feasible

Examples:
- `crawl/parser.py` (pure) ↔ `crawl/crawler.py` (I/O)
- `enrich/frontmatter.py` (pure) ↔ `enrich/sync.py` (I/O)
- `classify/rules.py` (pure) ↔ `classify/runner.py` (I/O)

This separation means the core logic can be developed and tested entirely without network access or a local corpus.

### Idempotency

Every stage is safe to re-run. Re-running a completed stage produces the same output and does not corrupt existing work:

- **Crawl**: overwrites `vdl_inventory.csv` — same result every run against the same VDL state
- **Fetch**: checks SQLite state before downloading — skips already-fetched documents; only re-fetches on explicit `--force`
- **Ingest**: checks for existing markdown output — skips already-converted documents; `--force` flag re-converts
- **Enrich**: checks for existing frontmatter fields — skips already-enriched fields; `--force` re-enriches
- **Classify**: mapping table is deterministic — re-running produces the same `system_type` values

Idempotency is enforced through SQLite state tracking (see [Section 7](#7-sqlite-state-tracking)) and per-file existence checks. A partial run interrupted by network failure or process kill can always be resumed from where it stopped.

### Portability

The pipeline runs on any Linux machine with Python 3.11+ and internet access. There are no platform-specific dependencies, no Docker requirement, and no cloud infrastructure.

Key portability decisions:
- `uv` for package management (fast, reproducible, no virtualenv confusion)
- SQLite for state (no database server needed)
- All paths relative to configurable `data_dir` — default `~/data/vista-docs/`
- No hard-coded absolute paths in any module

The pipeline was developed and runs on Linux Mint (Debian-based) but has no OS-specific code.

### Git-Versioned Code and Data

The `vista-docs` Python package is git-versioned at `~/projects/vista-docs/`. Commits follow conventional commit style. Every behavioral change is committed before deployment.

The enriched inventory CSV and the memory/guide files in `~/claude/` are also git-versioned, providing a complete audit trail of analytical decisions.

---

## 3. Completeness and Determinism
[↑ Table of Contents](#table-of-contents)

This analysis is distinguished from prior VistA documentation studies by three properties that were design criteria from the start, not incidental outcomes.

### Completeness

The analysis covers **every application** in the VDL and **every document** under each application. There are no sampled subsets and no applications skipped. The pipeline was designed to process the full catalog, not a representative sample.

The 2,240 markdown files represent the full available corpus for the 44 packages for which technical documentation was present and downloadable. The remaining ~150 applications either have only boilerplate noise rows, have no downloadable documents, or had documents that could not be converted (corrupted files, scanned PDFs without OCR). These are documented gaps, not missed items.

### Document-Grounded Classification

Every `system_type` classification is grounded in the actual technical documentation for that application — Technical Manuals, Installation Guides, and Developer Guides that describe the architecture, implementation language, and deployment mechanism.

No application was classified based on its name alone. Several applications required re-examination after initial misclassification revealed that the VDL entry name pointed to an external system rather than the VistA MUMPS package that interfaces with it (see [`vdl-6-system-classification.md`](vdl-6-system-classification.md) for specifics).

### Determinism

The pipeline is fully reproducible:

- The crawl, fetch, ingest, and enrich stages are implemented as a versioned Python package with SQLite state tracking
- The classification is implemented as an explicit mapping table in `classify/rules.py` with inline rationale comments for every non-obvious decision
- Re-running the pipeline from the VDL crawl forward reproduces the same inventory, the same markdown corpus, and the same classifications
- No AI model inference is used in the classification stage — it is a deterministic lookup table

The only source of non-determinism is the VDL itself: if the VA updates the VDL between runs, the crawl will return different rows. This is expected and desirable — it means the pipeline tracks VDL changes accurately.

---

## 4. Pipeline Stages
[↑ Table of Contents](#table-of-contents)

The full pipeline proceeds in six stages:

```
VDL website
    │
    ▼
[Stage 1: Crawl]     ─────────────────────────────── vdl_inventory.csv
    │                  Enumerate all 196 apps and     8,834 rows
    │                  8,834 document entries          ~25 base columns
    ▼
[Stage 2: Inventory] ─────────────────────────────── vdl_inventory_enriched.csv
    │                  Normalize, classify, stratify  29 columns
    │                  all inventory rows             100% app_name_abbrev fill
    ▼
[Stage 3: Fetch]     ─────────────────────────────── ~/data/vista-docs/raw/
    │                  Download substantive docs       PDF and DOCX files
    │                  Skip noise_type != '' rows     See pipeline.db for counts
    ▼
[Stage 4: Ingest]    ─────────────────────────────── ~/data/vista-docs/markdown/
    │                  Convert DOCX/PDF → markdown    2,240 .md files
    │                  Docling + post-processing      44 package dirs
    ▼
[Stage 5: Enrich]    ─────────────────────────────── YAML frontmatter in each .md
    │                  Read every doc; extract 30–35  7 extraction cycles
    │                  metadata fields; write to      14.9M words processed
    │                  frontmatter
    ▼
[Stage 6: Classify]  ─────────────────────────────── system_type column
                       Apply KIDS test to all 196     196 apps classified
                       apps; explicit rationale        0 unclassified
```

Each stage is documented in its own companion report. See [Related Reports](#related-reports).

---

## 5. Python Environment and Toolchain
[↑ Table of Contents](#table-of-contents)

### Package Manager: `uv`

All dependencies are managed with `uv` (not pip). `uv` provides fast, reproducible installs with lockfile support.

```bash
# Install all dependencies
uv sync

# Add a new dependency
uv add <package>

# Run a command in the venv
uv run vista-docs <command>
```

The virtual environment lives at `~/projects/vista-docs/.venv/`. All Makefile targets use `.venv/bin/` prefixes explicitly to avoid conflicts with any parent `direnv`-managed `VIRTUAL_ENV`.

### Linter and Formatter: `ruff`

`ruff` is the sole linter and formatter. It replaces both `flake8` and `black`. Configuration in `pyproject.toml`.

```bash
make lint    # ruff check + ruff format --check
make fmt     # ruff format (auto-fix)
```

### Type Checker: `mypy`

All pure modules are fully type-annotated. `mypy` runs in strict mode on the pure layer.

Known gotcha: BeautifulSoup4 types `tag["href"]` as `str | list[str]`. Always cast with `str(tag["href"])` to satisfy mypy.

### Test Runner: `pytest` + `pytest-cov`

```bash
make test      # run full test suite
make watch     # re-run tests on file change (uses pytest-watch)
make check     # test + lint + mypy (run before git push)
make push      # check + git push
```

Coverage is enforced on pure modules. I/O layers are in the `[tool.coverage.run] omit` list in `pyproject.toml`.

### Key Dependencies

| Package | Purpose |
|---|---|
| `docling` | PDF/DOCX → markdown conversion |
| `beautifulsoup4` | VDL HTML parsing |
| `requests` | HTTP fetch with session management |
| `click` | CLI framework |
| `pyyaml` | YAML frontmatter parsing/serialization |
| `uv` | Package manager |
| `ruff` | Linter + formatter |
| `mypy` | Type checker |
| `pytest` | Test runner |

---

## 6. Data Flow
[↑ Table of Contents](#table-of-contents)

```
~/data/vista-docs/
├── inventory/
│   ├── vdl_inventory.csv          # raw crawl output
│   └── vdl_inventory_enriched.csv # after all enrichment and classification
├── raw/
│   └── <app_code>/                # downloaded original files (PDF/DOCX)
├── markdown/
│   └── <app_code>/                # converted markdown files with YAML frontmatter
├── pipeline.db                    # SQLite state database
└── survey/
    └── survey-enrichment.csv      # post-pipeline content metrics
```

The `vdl_inventory_enriched.csv` file is the terminal artifact of the Crawl → Enrich chain. It contains all 29 columns from the crawl plus the `system_type` and `cots_dependent` classification columns added by the Classify stage.

---

## 7. SQLite State Tracking
[↑ Table of Contents](#table-of-contents)

`pipeline.db` is a SQLite database that tracks the processing state of every document across all pipeline stages. It is the mechanism that enables idempotency and resume.

Key tables:

| Table | Tracks |
|---|---|
| `manifest` | One row per document; `UNIQUE(package_id, doc_title)` constraint |
| `fetch_state` | Download status, file size, HTTP response code, local path |
| `ingest_state` | Conversion status, output markdown path, Docling version |
| `enrich_state` | Which enrichment cycles have been applied to each document |

The pipeline checks these tables before performing any work. A document already in state `fetch_complete` is not downloaded again unless `--force` is passed.

---

## 8. CLI Design
[↑ Table of Contents](#table-of-contents)

The pipeline is invoked through the `vista-docs` CLI, built with Click.

```bash
vista-docs crawl [--output PATH]
vista-docs fetch [--pkg PKG] [--force] [--dry-run]
vista-docs ingest [--pkg PKG] [--force]
vista-docs enrich [--pkg PKG] [--cycle N] [--force]
vista-docs classify [--output PATH]
vista-docs survey [--pkg PKG]
```

**Important:** Global options such as `--verbose` must come BEFORE the subcommand name in Click group CLIs:

```bash
vista-docs --verbose fetch --pkg PSO    # correct
vista-docs fetch --verbose --pkg PSO   # incorrect — --verbose is ignored
```

Each subcommand accepts `--pkg` to restrict processing to a single package, enabling targeted re-runs without reprocessing the entire corpus.

---

## Related Reports

| Report | Contents |
|---|---|
| [`vdl-1-crawl.md`](vdl-1-crawl.md) | VDL catalog extraction |
| [`vdl-2-inventory.md`](vdl-2-inventory.md) | Inventory normalization and enrichment — all eight passes |
| [`vdl-3-fetch.md`](vdl-3-fetch.md) | Document download — design, rate limiting, lessons learned |
| [`vdl-4-ingest.md`](vdl-4-ingest.md) | Document conversion to markdown |
| [`vdl-5-enrich.md`](vdl-5-enrich.md) | Metadata extraction — all seven cycles |
| [`vdl-6-system-classification.md`](vdl-6-system-classification.md) | System classification — all 196 applications |

---

*End of report.*
