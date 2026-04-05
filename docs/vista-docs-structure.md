# vista-docs v2 — Proposed Project Structure

**Status:** Proposal — no code written
**Date:** 2026-03-22
**Skills used:** vista-system, vista-fileman, va-docx-structure, vdl-pipeline,
                 vdl, knowledge-capture, bash-quality-checker

---

## Guiding Principles

The existing archive (`~/projects/archive/vdl-crawl`, `~/projects/archive/vdl-transform`,
`~/vista-docs`) has ~3,900 lines across 10 monolithic scripts with no tests, no package
structure, and logic tangled with I/O throughout. The redesign applies three rules:

1. **Separation of concerns** — pure logic lives in testable modules; I/O lives in thin wrappers
2. **Data outside the repo** — all downloaded files, survey outputs, manifests, and databases
   live in `~/data/vista-docs/`, never committed to git
3. **TDD from the first line** — every pure function has a test written before the implementation

---

## Locations

| What | Where |
|---|---|
| Code (git repo) | `~/projects/vista-docs/` |
| All data and state | `~/data/vista-docs/` |
| Skills | `~/claude/skills/` |
| Template origin | `~/claude/templates/python/` |

---

## Project Repo: `~/projects/vista-docs/`

```
~/projects/vista-docs/
│
├── src/
│   └── vista_docs/
│       ├── __init__.py
│       ├── config.py                   # data paths, rate limits, constants, user-agent
│       │
│       ├── models/                     # pure dataclasses — no logic, no I/O
│       │   ├── __init__.py
│       │   ├── catalog.py              # Section, Application, Document
│       │   └── manifest.py             # ManifestEntry, FetchStatus, DocType (enums)
│       │
│       ├── crawl/                      # VDL catalog → inventory
│       │   ├── __init__.py
│       │   ├── parser.py               # HTML → catalog records  [PURE — primary test target]
│       │   └── session.py              # requests.Session wrapper [I/O thin layer]
│       │
│       ├── classify/                   # Document type classification
│       │   ├── __init__.py
│       │   └── rules.py                # filename + title → DocType  [PURE — primary test target]
│       │
│       ├── fetch/                      # Document downloading
│       │   ├── __init__.py
│       │   ├── strategy.py             # URL derivation, DOCX/PDF fallback logic  [PURE]
│       │   └── downloader.py           # HTTP download, retry, rate limit  [I/O thin layer]
│       │
│       ├── ingest/                     # DOCX/PDF → Markdown
│       │   ├── __init__.py
│       │   ├── postprocess.py          # all VA-specific markdown transforms  [PURE — primary test target]
│       │   └── converter.py            # Docling wrapper  [I/O thin layer]
│       │
│       ├── survey/                     # Corpus structure analysis
│       │   ├── __init__.py
│       │   ├── detectors.py            # table-type, style, callout detection  [PURE — primary test target]
│       │   └── analyzer.py             # orchestration over corpus files  [I/O thin layer]
│       │
│       ├── manifest/                   # Pipeline state management
│       │   ├── __init__.py
│       │   ├── operations.py           # filter, merge, update, deduplicate  [PURE — primary test target]
│       │   └── store.py                # SQLite read/write  [I/O thin layer]
│       │
│       └── cli/                        # Single `vista-docs` command, subcommands
│           ├── __init__.py
│           └── main.py                 # crawl | fetch | ingest | survey | verify | pipeline
│
├── tests/
│   ├── conftest.py                     # shared fixtures, data path helpers, pytest marks
│   │
│   ├── fixtures/                       # static test data — committed to repo, small
│   │   ├── html/
│   │   │   ├── section_listing.html    # captured VDL section-list page (sanitised)
│   │   │   ├── app_page_active.html    # app page with active documents
│   │   │   └── app_page_archive.html   # app page with archived/decommissioned entries
│   │   ├── docx/
│   │   │   ├── minimal.docx            # bare DOCX: heading + body + table
│   │   │   ├── with_revision.docx      # DOCX with revision history table
│   │   │   ├── with_callouts.docx      # DOCX with NOTE/WARNING/CAUTION blocks
│   │   │   └── with_toc.docx           # DOCX with TOC field to be stripped
│   │   └── manifests/
│   │       ├── all_pending.json        # manifest with no fetched docs
│   │       ├── mixed_status.json       # manifest with ok/error/pending mix
│   │       └── fully_fetched.json      # manifest with all docs ok
│   │
│   ├── unit/                           # fast, no I/O, no network — run in CI
│   │   ├── test_catalog_models.py      # Section/Application/Document dataclass behaviour
│   │   ├── test_manifest_models.py     # ManifestEntry, FetchStatus, DocType
│   │   ├── test_parser.py              # HTML → catalog records (section, app, doc extraction)
│   │   ├── test_rules.py               # filename + title → DocType classification
│   │   ├── test_strategy.py            # URL derivation, DOCX↔PDF fallback, paired URL logic
│   │   ├── test_postprocess.py         # all markdown transforms (callouts, headings, TOC strip,
│   │   │                               #   revision extraction, screen-style normalise, boilerplate)
│   │   ├── test_detectors.py           # table-type detection, style classification, callout patterns
│   │   └── test_operations.py          # manifest filter, merge, status update, deduplication
│   │
│   └── integration/                    # slower — real SQLite, real files, optional network
│       ├── test_store.py               # SQLite manifest round-trip (create/read/update/query)
│       ├── test_converter.py           # Docling DOCX→markdown on fixture files (skip if no docling)
│       ├── test_crawler.py             # live VDL crawl — @pytest.mark.network (skipped in CI)
│       └── test_downloader.py          # live document download — @pytest.mark.network (skipped in CI)
│
├── CLAUDE.md                           # project context for Claude sessions
├── pyproject.toml                      # build, deps, pytest config, ruff, mypy, coverage
├── uv.lock                             # locked dependency tree (committed)
├── Makefile                            # standard + pipeline targets
├── .python-version                     # 3.12
├── .envrc                              # direnv: activate .venv
├── .gitignore                          # standard + data/ paths, Docling cache
├── .env.example                        # DATA_DIR, LOG_LEVEL, VA_USER_AGENT
├── .pre-commit-config.yaml             # ruff lint+format, yaml/toml check
└── .github/
    └── workflows/
        └── ci.yml                      # unit tests only (no network); integration skipped
```

---

## Data Directory: `~/data/vista-docs/`

Not a git repo. Backed up separately. All paths configured in `config.py`.

```
~/data/vista-docs/
│
├── inventory/                          # VDL catalog — written by `vista-docs crawl`
│   ├── vdl_inventory.csv               # current working inventory (full VDL catalog)
│   ├── vdl_inventory.json              # same data, hierarchical (sections → apps → docs)
│   └── snapshots/                      # dated snapshots for tracking VDL changes over time
│       └── 2026-03-22_vdl_inventory.csv
│
├── state/                              # pipeline state tracking
│   └── pipeline.db                     # SQLite: every document, every stage, full status history
│                                       # replaces manifest.json and guides-manifest.json
│
├── raw/                                # downloaded source files — written by `vista-docs fetch`
│   ├── OR/                             # by package namespace code
│   │   ├── cprsguitm.docx
│   │   └── ...
│   ├── TIU/
│   ├── HL/
│   ├── DG/
│   └── <NAMESPACE>/                    # one dir per package namespace
│
├── markdown/                           # converted documents — written by `vista-docs ingest`
│   ├── OR/
│   │   ├── cprs-technical-manual.md    # canonical filename from manifest
│   │   └── ...
│   ├── TIU/
│   ├── HL/
│   └── <NAMESPACE>/
│
├── survey/                             # corpus analysis — written by `vista-docs survey`
│   ├── corpus-survey.json              # full machine-readable survey (all packages)
│   ├── corpus-survey.txt               # human-readable report
│   └── by-package/                     # per-package breakdowns
│       ├── OR-survey.json
│       ├── TIU-survey.json
│       └── ...
│
├── guides/                             # synthesised reference guides (hand-edited outputs)
│   ├── clinical/
│   │   ├── cprs/
│   │   │   ├── cprs-pce-guide.md
│   │   │   ├── cprs-reports-guide.md
│   │   │   └── vista-cprs-arch-guide.md
│   │   ├── tiu/
│   │   └── adt/
│   └── infrastructure/
│       └── hl7/
│
└── skill-updates/                      # staged TSV exports for ~/claude/skills updates
    ├── packages.tsv                    # new package rows staged for apply_skill_updates
    ├── file-index.tsv                  # new file→package mappings
    └── relationships.tsv              # new inter-package relationships
```

---

## Module Responsibilities

### Pure modules — the primary TDD targets

These contain zero I/O. Every function takes plain Python values and returns plain Python values.
Write the test first; implement second.

| Module | Input | Output | What it does |
|---|---|---|---|
| `crawl/parser.py` | raw HTML string | `list[Section \| Application \| Document]` | Parses VDL catalog pages |
| `classify/rules.py` | filename, title | `DocType` | Classifies document type from filename/title patterns |
| `fetch/strategy.py` | doc_url, ext | `list[str]` (ordered URLs to try) | Derives DOCX/PDF fallback order, paired URL swap |
| `ingest/postprocess.py` | raw markdown str | clean markdown str | All VA-specific transforms (strip TOC, callouts, headings, boilerplate, etc.) |
| `survey/detectors.py` | paragraph/table object | `StyleClass \| TableType \| CalloutType` | Classifies corpus elements |
| `manifest/operations.py` | `list[ManifestEntry]`, filters | filtered/updated `list[ManifestEntry]` | Filter, merge, dedup, status update |

### I/O thin layers — tested in integration only

| Module | External dependency | What it wraps |
|---|---|---|
| `crawl/session.py` | `requests` | HTTP session with rate limiting and retry |
| `fetch/downloader.py` | `requests`, filesystem | Download file, write to raw/, update state |
| `ingest/converter.py` | `docling` | DOCX/PDF → raw markdown string |
| `survey/analyzer.py` | `python-docx`, filesystem | Walk corpus files, call detectors |
| `manifest/store.py` | `sqlite3` | Read/write pipeline.db |

---

## Makefile Targets

```
Standard (from template):
  make install      install deps + pre-commit hooks
  make test         unit tests only (fast)
  make test-lf      rerun last-failed
  make watch        TDD mode: rerun on save
  make cov          test + coverage report (80% min)
  make check        lint + mypy + cov
  make push         check + git push
  make pull         git pull

Pipeline (new):
  make crawl        vista-docs crawl  → ~/data/vista-docs/inventory/
  make fetch        vista-docs fetch  → ~/data/vista-docs/raw/
  make ingest       vista-docs ingest → ~/data/vista-docs/markdown/
  make survey       vista-docs survey → ~/data/vista-docs/survey/
  make verify       vista-docs verify → sanity-check all artifacts
  make pipeline     run crawl → fetch → ingest → survey in order
```

---

## Key Dependencies (pyproject.toml)

```
Runtime:
  requests          HTTP crawl and fetch
  python-docx       DOCX corpus survey (detectors.py)
  pyyaml            YAML frontmatter in synthesised guides
  docling           DOCX/PDF → markdown (optional; ingest scaffolds without it)
  click             CLI subcommands (vista-docs crawl|fetch|ingest|survey|...)

Dev (existing template set):
  pytest, pytest-cov, pytest-watch, pytest-randomly
  ruff, mypy, pre-commit
```

---

## CLI Entry Point

Single command with subcommands (defined as `vista-docs` in `[project.scripts]`):

```
vista-docs crawl   [--delay N] [--snapshot]
vista-docs fetch   [--pkg OR] [--dry-run] [--force]
vista-docs ingest  [--pkg OR] [--scaffold] [--force]
vista-docs survey  [--pkg OR] [--output ~/data/vista-docs/survey/]
vista-docs verify  [--fix]
vista-docs pipeline [--pkg OR] [--from crawl|fetch|ingest|survey]
```

---

## CLAUDE.md (project-level)

The project CLAUDE.md will direct Claude to load these skills at session start:

```
Skills to load for this project:
  vdl                — VDL catalog structure, URL patterns, crawling gotchas
  vista-system       — VistA package architecture, namespaces, relationships
  vista-fileman      — FileMan APIs, global conventions, data dictionary
  va-docx-structure  — Corpus survey findings, ingest checklist, frontmatter schema
  vdl-pipeline       — Pipeline script reference (archive — for comparison only)
  knowledge-capture  — Capture new findings back to skills after each session
```

---

## Test Strategy

### Unit tests (always run — fast — CI-safe)

All tests in `tests/unit/` use only fixtures and plain Python objects. No filesystem,
no network, no database, no Docling.

Example flow for `test_parser.py`:
```
1. Load tests/fixtures/html/section_listing.html
2. Call parse_sections(html_string)
3. Assert: returns list of Section dataclasses with correct fields
```

Example flow for `test_postprocess.py`:
```
1. Input: raw markdown string with NOTE: callout
2. Call format_callouts(markdown)
3. Assert: output contains "> **NOTE:**" blockquote
```

### Integration tests (slower — run manually or with `pytest -m integration`)

Tests in `tests/integration/` may touch SQLite, local fixture DOCX files, or
(when explicitly enabled) live VA servers.

Mark network tests so they are skipped in CI:
```python
@pytest.mark.network      # skipped unless --run-network passed
@pytest.mark.slow         # skipped unless -m slow passed
```

### Coverage

80% minimum enforced by `make cov` and CI. Pure modules should be 95%+.
I/O thin layers are exempt from the minimum — they are tested in integration only.

---

## Migration from Archive

The archive (`~/projects/archive/vdl-transform/`, `~/vista-docs/scripts/`) is
reference only. The new project will not copy code from it — it will:

1. Use the archive survey data in `~/vista-docs/scripts/survey/` as expected
   output fixtures to validate the new survey implementation
2. Use the archive `vdl_inventory.csv` as the starting inventory input
3. Use the archive `manifest.json` structure as a schema reference only
4. Migrate the guides from `~/vista-docs/guides/` into `~/data/vista-docs/guides/`

---

## What Is NOT in the Repo

| Item | Why | Where instead |
|---|---|---|
| `vdl_inventory.csv` | Generated output, large, frequently refreshed | `~/data/vista-docs/inventory/` |
| `manifest.json` / `pipeline.db` | Runtime state, not code | `~/data/vista-docs/state/` |
| `raw/*.docx` / `raw/*.pdf` | Large binary files | `~/data/vista-docs/raw/` |
| `markdown/*.md` (converted) | Generated output | `~/data/vista-docs/markdown/` |
| `survey-report.txt` | Generated output | `~/data/vista-docs/survey/` |
| Synthesised guides | Hand-edited outputs, not source | `~/data/vista-docs/guides/` |
| `.venv/` | Machine-local environment | `~/projects/vista-docs/.venv/` (gitignored) |
| Docling model cache | Large binary | `~/.cache/docling/` (gitignored) |
