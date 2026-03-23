# Claude Project Context — vista-docs

## What this project is

`vista-docs` is a TDD Python pipeline that crawls the VA VistA Document Library (VDL),
downloads DOCX/PDF manuals, converts them to structured markdown, and analyses the corpus.
Output data lives in `~/data/vista-docs/` — never in this repo.

## Skills to load for this project

```
vdl              — VDL catalog structure, URL patterns, crawling gotchas
vdl-pipeline     — Complete operating manual: CLI, stages, enrich fields, gotchas
vista-system     — VistA package architecture, namespaces, relationships
vista-fileman    — FileMan APIs, global conventions, data dictionary
va-docx-structure — DOCX structure survey, ingest post-processing, callout patterns
knowledge-capture — Capture new findings back to skills after each session
```

## Project structure

```
src/vista_docs/
  models/        — pure dataclasses (no logic, no I/O)
  crawl/         — VDL HTML → catalog records
  classify/      — filename/title → DocType
  fetch/         — URL derivation + HTTP download
  ingest/        — DOCX/PDF → markdown via Docling + post-processing
  enrich/        — extract metadata from markdown, rewrite YAML frontmatter
  survey/        — corpus structure analysis (stats.py pure; analyzer.py I/O)
  manifest/      — SQLite pipeline state management
  cli/           — `vista-docs` Click command with subcommands

tests/
  unit/          — fast, no I/O, no network (run in CI)
  integration/   — SQLite, file I/O, optional network (@pytest.mark.network)
  fixtures/      — static HTML/DOCX/manifest test data (committed, small)
```

## Data directory (NOT in this repo)

```
~/data/vista-docs/
  inventory/     — VDL catalog CSV/JSON (from `vista-docs crawl`)
  state/         — pipeline.db SQLite (pipeline state)
  raw/           — downloaded DOCX/PDF by namespace
  markdown/      — converted docs by namespace
  survey/        — corpus analysis outputs
  guides/        — synthesised reference guides (hand-edited)
  skill-updates/ — staged TSV exports for ~/claude/skills updates
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

# Pipeline targets
make crawl      # vista-docs crawl  → ~/data/vista-docs/inventory/
make fetch      # vista-docs fetch  → ~/data/vista-docs/raw/
make ingest     # vista-docs ingest → ~/data/vista-docs/markdown/
make survey     # vista-docs survey → ~/data/vista-docs/survey/
make verify     # vista-docs verify → sanity-check artifacts
make pipeline   # crawl → fetch → ingest → survey in order
```

## CLI

```
vista-docs crawl   [--delay N] [--snapshot] [--max-apps N]
vista-docs fetch   [--pkg CPRS] [--dry-run] [--force] [--delay N]
vista-docs ingest  [--pkg CPRS] [--scaffold] [--force]
vista-docs enrich  [--pkg CPRS] [--force]
vista-docs survey  [--pkg CPRS] [--output PATH]     # stub
vista-docs verify  [--fix]                           # stub
vista-docs pipeline [--pkg CPRS] [--from crawl|fetch|ingest|survey]  # stub
```

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
- `--pkg` flag always takes VDL app_code (CPRS/ADT), never VistA namespace (OR/DG)
- Every new I/O layer goes into `[tool.coverage.run] omit` in pyproject.toml immediately
- New extractor TDD cycle: test → fail-confirm → implement → make check → enrich --force
