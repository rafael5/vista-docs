# vista-docs — Target Filesystem
**Date:** 2026-03-22
**Status:** Approved pre-build proposal — no code written

---

## What Is Consumed From the Current Filesystem

### From `~/vista-docs/scripts/` — reference implementations (master)

| Script | Lines | Becomes |
|---|---|---|
| `vdl_inventory.csv` | data | `~/data/vista-docs/inventory/vdl_inventory.csv` |
| `manifest.json` | data | `~/data/vista-docs/state/seed/manifest-legacy.json` |
| `guides-manifest.json` | data | `~/data/vista-docs/state/seed/guides-manifest-legacy.json` |
| `tier1_state.json` | data | `~/data/vista-docs/state/seed/tier1-state-legacy.json` |
| `tier1_fetch/*.docx` | raw docs | `~/data/vista-docs/raw/<NAMESPACE>/` |
| `survey-data*.json` + `survey-report*.txt` | reference output | `~/data/vista-docs/survey/legacy/` |
| `survey/` (subdirectory) | reference output | `~/data/vista-docs/survey/legacy/by-package/` |
| `doc_authority_updates.txt`, `*.tsv` | reference data | `~/data/vista-docs/skill-updates/legacy/` |
| `pilot_manifest.py` | logic reference | `src/vista_docs/classify/` + `src/vista_docs/manifest/` |
| `fetch.py` | logic reference | `src/vista_docs/fetch/` |
| `fetch_guides.py` | logic reference | `src/vista_docs/fetch/` |
| `fetch_tier1.py` | logic reference | `src/vista_docs/fetch/` |
| `ingest.py` | logic reference | `src/vista_docs/ingest/` |
| `corpus_survey.py` | logic reference | `src/vista_docs/survey/` |
| `verify_corpus.py` | logic reference | `src/vista_docs/verify/` |
| `apply_skill_updates.py` | logic reference | `src/vista_docs/skills/` |
| `add_gap_docs.py` | logic reference | `src/vista_docs/manifest/` |
| `add_manifest_packages.py` | logic reference | `src/vista_docs/manifest/` |
| `rebuild_gap_entries.py` | logic reference | `src/vista_docs/manifest/` |
| `bootstrap.sh` | retired | replaced by `make install` |

### From `~/projects/archive/vdl-crawl/vdl-crawl.py` — unique to archive

The only script not in `~/vista-docs/scripts/`. The standalone VDL catalog crawler.
Becomes `src/vista_docs/crawl/` (parser + session).

### From `~/vista-docs/guides/` — synthesized guide outputs

| From | To |
|---|---|
| `guides/v1/*.md`, `guides/v1/*.docx` | `~/data/vista-docs/guides/legacy/v1/` |
| `guides/v2/*.md`, `guides/v2/*.docx` | `~/data/vista-docs/guides/legacy/v2/` |
| `guides/v3/*.docx` | `~/data/vista-docs/guides/legacy/v3/` |
| `guides/vista_cprs_arch_guide.*` | `~/data/vista-docs/guides/legacy/` |

### From `~/claude/`

| What | Used for |
|---|---|
| `templates/python/` | Base project scaffold — copy + rename `myproject` → `vista_docs` |
| `skills/vdl/SKILL.md` | VDL catalog knowledge |
| `skills/vista-system/SKILL.md` | VistA architecture, packages, relationships |
| `skills/vista-fileman/SKILL.md` | FileMan APIs, globals, data dictionary |
| `skills/va-docx-structure/SKILL.md` | Corpus findings, ingest checklist, table types |
| `skills/vdl-pipeline/SKILL.md` | Legacy pipeline reference |
| `skills/knowledge-capture/SKILL.md` | End-of-session knowledge extraction |

---

## Script → Module Map

| Script(s) | Pure module | I/O module |
|---|---|---|
| `vdl-crawl.py` (archive) | `crawl/parser.py` | `crawl/session.py` |
| `pilot_manifest.py` (classify section) | `classify/rules.py` | — |
| `pilot_manifest.py`, `add_gap_docs.py`, `add_manifest_packages.py`, `rebuild_gap_entries.py` | `manifest/operations.py` | `manifest/store.py` |
| `fetch.py`, `fetch_guides.py`, `fetch_tier1.py` | `fetch/strategy.py` | `fetch/downloader.py` |
| `ingest.py` (post-processing section) | `ingest/postprocess.py` | `ingest/converter.py` |
| `corpus_survey.py` (detector functions) | `survey/detectors.py` | `survey/analyzer.py` |
| `verify_corpus.py` | `verify/checks.py` | `verify/runner.py` |
| `apply_skill_updates.py` | `skills/operations.py` | `skills/exporter.py` |

---

## Target: Project Repo `~/projects/vista-docs/`

Code only. Git-controlled. No data files, no generated outputs, no binaries.

```
~/projects/vista-docs/
│
├── src/
│   └── vista_docs/
│       ├── __init__.py
│       ├── config.py                        # all data paths, rate limits, constants
│       │
│       ├── models/                          # dataclasses — zero logic, zero I/O
│       │   ├── __init__.py
│       │   ├── catalog.py                   # Section, Application, Document
│       │   └── manifest.py                  # ManifestEntry, FetchStatus, DocType (enums)
│       │
│       ├── crawl/                           # VDL catalog → inventory
│       │   ├── __init__.py
│       │   ├── parser.py                    # HTML → catalog records          [PURE]
│       │   └── session.py                   # requests.Session + rate limit   [I/O]
│       │
│       ├── classify/                        # Document type classification
│       │   ├── __init__.py
│       │   └── rules.py                     # filename + title → DocType      [PURE]
│       │
│       ├── fetch/                           # Document downloading
│       │   ├── __init__.py
│       │   ├── strategy.py                  # URL derivation, fallback order   [PURE]
│       │   └── downloader.py                # HTTP download, retry, write      [I/O]
│       │
│       ├── ingest/                          # DOCX/PDF → Markdown
│       │   ├── __init__.py
│       │   ├── postprocess.py               # all VA markdown transforms        [PURE]
│       │   └── converter.py                 # Docling wrapper                  [I/O]
│       │
│       ├── survey/                          # Corpus structure analysis
│       │   ├── __init__.py
│       │   ├── detectors.py                 # table/style/callout detection    [PURE]
│       │   └── analyzer.py                  # walk corpus, call detectors      [I/O]
│       │
│       ├── manifest/                        # Pipeline state management
│       │   ├── __init__.py
│       │   ├── operations.py                # filter, merge, upsert, dedup     [PURE]
│       │   └── store.py                     # SQLite read/write                [I/O]
│       │
│       ├── verify/                          # Pipeline sanity checks
│       │   ├── __init__.py
│       │   ├── checks.py                    # validation rules                 [PURE]
│       │   └── runner.py                    # apply checks, report results     [I/O]
│       │
│       ├── skills/                          # Skill TSV export
│       │   ├── __init__.py
│       │   ├── operations.py                # TSV merge, dedup, diff           [PURE]
│       │   └── exporter.py                  # read/write TSV files             [I/O]
│       │
│       └── cli/                             # Single `vista-docs` entry point
│           ├── __init__.py
│           └── main.py                      # subcommands: crawl|manifest|fetch|
│                                            #   ingest|survey|verify|skills|pipeline
│
├── tests/
│   ├── conftest.py                          # fixtures, paths, pytest marks (network, slow)
│   │
│   ├── fixtures/                            # static test data — small, committed
│   │   ├── html/
│   │   │   ├── vdl_home.html               # VDL main landing page (sanitised)
│   │   │   ├── section_listing.html         # section page with app links
│   │   │   ├── app_page_active.html         # app page: active docs only
│   │   │   └── app_page_mixed.html          # app page: active + archive + decommissioned
│   │   ├── docx/
│   │   │   ├── minimal.docx                 # heading + body paragraph only
│   │   │   ├── with_revision_table.docx     # contains a patch revision table
│   │   │   ├── with_callouts.docx           # contains NOTE/WARNING/CAUTION blocks
│   │   │   ├── with_toc.docx                # contains TOC field to be stripped
│   │   │   ├── with_screen_capture.docx     # contains Screen Capture style paragraphs
│   │   │   └── with_outline_headings.docx   # contains "1.2.3 Heading" numbered headings
│   │   ├── csv/
│   │   │   └── sample_inventory.csv         # 20-row extract from vdl_inventory.csv
│   │   └── manifests/
│   │       ├── all_pending.json             # manifest: no documents fetched yet
│   │       ├── mixed_status.json            # manifest: ok/error/pending mix
│   │       └── fully_fetched.json           # manifest: all ok-docx or ok-pdf
│   │
│   ├── unit/                                # fast, no I/O, no network — always run in CI
│   │   ├── test_models.py                   # Section/Application/Document/ManifestEntry
│   │   ├── test_parser.py                   # HTML → catalog records
│   │   ├── test_rules.py                    # filename + title → DocType
│   │   ├── test_strategy.py                 # URL derivation, DOCX↔PDF fallback
│   │   ├── test_postprocess.py              # all markdown transforms
│   │   ├── test_detectors.py                # table-type, style, callout detection
│   │   ├── test_operations.py               # manifest filter/merge/upsert/dedup
│   │   ├── test_checks.py                   # verification rules
│   │   └── test_skill_operations.py         # TSV merge and dedup logic
│   │
│   └── integration/                         # real I/O — run manually or with -m integration
│       ├── test_store.py                    # SQLite round-trip (create/read/update/query)
│       ├── test_converter.py                # Docling on fixture DOCX files
│       ├── test_analyzer.py                 # survey over fixture DOCX directory
│       ├── test_crawler.py                  # @pytest.mark.network — live VDL crawl
│       └── test_downloader.py               # @pytest.mark.network — live document download
│
├── CLAUDE.md                                # project context (see below)
├── pyproject.toml                           # from template + vista-docs deps + CLI entry point
├── uv.lock                                  # committed lockfile
├── Makefile                                 # template targets + pipeline targets
├── .python-version                          # 3.12
├── .envrc                                   # direnv: activate .venv
├── .gitignore                               # template standard + Docling cache
├── .env.example                             # DATA_DIR override, LOG_LEVEL, VA_CONTACT_EMAIL
├── .pre-commit-config.yaml                  # ruff lint+format, yaml/toml, debug-statements
└── .github/
    ├── dependabot.yml
    └── workflows/
        └── ci.yml                           # unit tests only; integration + network skipped
```

---

## Target: Data Directory `~/data/vista-docs/`

Not a git repo. Never committed. Backed up with rsync separately from code.
All paths are defined in `src/vista_docs/config.py` and overridable via `DATA_DIR` env var.

```
~/data/vista-docs/
│
├── inventory/                               # VDL catalog — written by `vista-docs crawl`
│   ├── vdl_inventory.csv                    # current working inventory (full VDL, 167+ packages)
│   ├── vdl_inventory.json                   # same data, hierarchical (sections → apps → docs)
│   └── snapshots/                           # dated snapshots for tracking VDL changes
│       └── 2026-03-22_vdl_inventory.csv     # (seeded from ~/vista-docs/scripts/vdl_inventory.csv)
│
├── state/                                   # pipeline state
│   ├── pipeline.db                          # SQLite: all documents × all stages × full history
│   └── seed/                                # legacy manifests — read-only reference
│       ├── manifest-legacy.json             # from ~/vista-docs/scripts/manifest.json
│       ├── guides-manifest-legacy.json      # from ~/vista-docs/scripts/guides-manifest.json
│       └── tier1-state-legacy.json          # from ~/vista-docs/scripts/tier1_state.json
│
├── raw/                                     # downloaded source files — written by `vista-docs fetch`
│   ├── OR/                                  # CPRS
│   ├── TIU/                                 # Text Integration Utilities
│   ├── HL/                                  # HL7
│   ├── DG/                                  # ADT (+ adtbe_um.docx, adt_pims_tm.docx from tier1)
│   ├── ASU/                                 # Authorization/Subscription (asutm.docx from tier1)
│   ├── KRN/                                 # Kernel (krn_8_0_tm.docx from tier1)
│   ├── LA/                                  # Laboratory (lab_ledi_*.docx from tier1)
│   ├── MD/                                  # Medicine/Clinical Procedures (from tier1)
│   ├── NUR/                                 # Nursing (nurs4_*.docx from tier1)
│   ├── PSN/                                 # (psn_4_*.docx from tier1)
│   ├── PSS/                                 # Pharmacy Data Management (PSS_1_*.docx from tier1)
│   ├── XWB/                                 # RPC Broker (xwb_1_1_*.docx from tier1)
│   ├── DI/                                  # VA FileMan
│   ├── IB/                                  # Integrated Billing
│   ├── PRCA/                                # Accounts Receivable
│   ├── ECME/                                # Electronic Claims
│   ├── VPR/                                 # Virtual Patient Record
│   └── <NAMESPACE>/                         # one dir per package namespace, added as crawled
│
├── markdown/                                # converted markdown — written by `vista-docs ingest`
│   ├── OR/
│   │   ├── cprs-technical-manual.md         # canonical filename from manifest
│   │   ├── cprs-user-manual.md
│   │   └── ...
│   ├── TIU/
│   ├── HL/
│   ├── DG/
│   └── <NAMESPACE>/
│
├── survey/                                  # corpus analysis — written by `vista-docs survey`
│   ├── corpus-survey.json                   # full machine-readable (all packages)
│   ├── corpus-survey.txt                    # human-readable report
│   ├── by-package/                          # per-package breakdowns
│   │   ├── OR-survey.json
│   │   ├── TIU-survey.json
│   │   ├── HL-survey.json
│   │   ├── DG-survey.json
│   │   └── <NAMESPACE>-survey.json
│   └── legacy/                              # reference outputs from old pipeline (read-only)
│       ├── survey-data.json
│       ├── survey-report.txt
│       ├── survey-report-v2.txt
│       └── by-package/
│           ├── survey-data-cprs.json
│           ├── survey-data-tiu.json
│           ├── survey-data-hl7.json
│           └── survey-data-adt.json
│
├── guides/                                  # synthesized reference guides
│   ├── clinical/
│   │   ├── cprs/                            # new guides go here as they are produced
│   │   ├── tiu/
│   │   └── adt/
│   ├── infrastructure/
│   │   └── hl7/
│   └── legacy/                              # from ~/vista-docs/guides/ — read-only reference
│       ├── v1/
│       │   ├── cprs_pce_guide.md
│       │   ├── cprs_pce_guide.docx
│       │   ├── cprs_reports_guide.md
│       │   └── cprs_reports_guide.docx
│       ├── v2/
│       │   ├── cprs_pce_guide_v2.md
│       │   ├── cprs_pce_guide_v2.docx
│       │   ├── cprs_reports_guide_v2.md
│       │   └── cprs_reports_guide_v2.docx
│       ├── v3/
│       │   ├── cprs_pce_guide_v3.docx       # no .md yet — in-progress
│       │   └── cprs_reports_guide_v3.docx
│       └── vista_cprs_arch_guide.md
│
└── skill-updates/                           # staged exports for ~/claude/skills
    ├── packages.tsv                         # new/updated package rows
    ├── file-index.tsv                       # new file→package mappings
    ├── relationships.tsv                    # new inter-package relationships
    └── legacy/                              # from ~/vista-docs/scripts/ — read-only reference
        ├── doc_authority_updates.txt
        ├── file_index_additions.tsv
        ├── packages_additions.tsv
        └── relationships_additions.tsv
```

---

## Makefile Targets

```
── Standard (from template) ────────────────────────────────────────────────
make install      uv sync --extra dev + pre-commit hooks
make test         pytest unit/ only (fast, always clean)
make test-lf      rerun last-failed tests
make watch        ptw TDD mode
make cov          pytest --cov, 80% threshold
make check        lint + mypy + cov (CI gate)
make push         check + git push
make pull         git pull

── Pipeline ─────────────────────────────────────────────────────────────────
make crawl        vista-docs crawl   → ~/data/vista-docs/inventory/
make manifest     vista-docs manifest → ~/data/vista-docs/state/pipeline.db
make fetch        vista-docs fetch   → ~/data/vista-docs/raw/
make ingest       vista-docs ingest  → ~/data/vista-docs/markdown/
make survey       vista-docs survey  → ~/data/vista-docs/survey/
make verify       vista-docs verify  → stdout (exit 0/1/2)
make skills       vista-docs skills  → ~/data/vista-docs/skill-updates/
make pipeline     crawl→manifest→fetch→ingest→survey→verify in order
```

---

## CLI Design

Single entry point `vista-docs` with subcommands:

```
vista-docs crawl      [--delay N] [--snapshot] [--limit N]
vista-docs manifest   [--pkg OR] [--gap] [--rebuild] [--dry-run]
vista-docs fetch      [--pkg OR] [--tier tier1|guides|all] [--dry-run] [--force]
vista-docs ingest     [--pkg OR] [--scaffold] [--force]
vista-docs survey     [--pkg OR]
vista-docs verify     [--fix] [--only inventory|manifest|raw|markdown]
vista-docs skills     [--dry-run]
vista-docs pipeline   [--pkg OR] [--from crawl|manifest|fetch|ingest|survey]
```

---

## CLAUDE.md — Data Paths Section (project-level)

```markdown
## Data paths
- Inventory:    ~/data/vista-docs/inventory/vdl_inventory.csv
- Pipeline DB:  ~/data/vista-docs/state/pipeline.db
- Raw docs:     ~/data/vista-docs/raw/<NAMESPACE>/
- Markdown:     ~/data/vista-docs/markdown/<NAMESPACE>/
- Survey:       ~/data/vista-docs/survey/
- Guides:       ~/data/vista-docs/guides/
- Skill TSVs:   ~/data/vista-docs/skill-updates/
- Legacy seed:  ~/data/vista-docs/state/seed/  (read-only reference)

## Skills to load for this project
- vdl               VDL catalog structure, URL patterns, crawling conventions
- vista-system      VistA packages, namespaces, relationships, known gaps
- vista-fileman     FileMan APIs, globals, data dictionary
- va-docx-structure Corpus findings, ingest checklist, table type detection
- vdl-pipeline      Legacy pipeline reference (~/vista-docs/scripts/ — do not modify)
- knowledge-capture Run at end of session to update ~/claude/skills/

## Reference code (read-only — do not modify)
- ~/vista-docs/scripts/    master legacy scripts
- ~/projects/archive/      earlier iterations
```

---

## Key Architectural Decisions

| Decision | Rationale |
|---|---|
| SQLite replaces JSON manifests | Queryable, atomic writes, schema-enforced, no corruption on partial write |
| `~/data/` separate from `~/projects/` | Follows FILESYSTEM.md convention; data never committed to git |
| Single `vista-docs` CLI, not per-script entry points | One command to learn; subcommands map 1:1 to pipeline stages |
| `fetch_tier1.py` + `fetch_guides.py` + `fetch.py` → one `fetch/downloader.py` | All three did the same HTTP work with minor variations; unified with `--tier` flag |
| Legacy outputs in `legacy/` subdirs (not deleted) | Survey data from 142-doc run is the validation baseline for the new survey implementation |
| `bootstrap.sh` retired | `make install` replaces it; the project template handles all setup |
