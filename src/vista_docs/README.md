# VistA Docs — Package Reference

This document describes every subpackage in `src/vista_docs/`, organized in the order the pipeline stages are intended to be run.  **Keep this file updated whenever a package's purpose, inputs, outputs, or prerequisites change.**

---

## Pipeline Stages

| # | Module | CLI Command | Purpose | Input | Output | Prerequisites |
|---|--------|-------------|---------|-------|--------|---------------|
| 1 | `crawl` | `vista-docs crawl` | Scrape the VA VDL website to discover all applications and documents | Live VDL website (`va.gov/vdl/`) | `inventory/vdl_inventory.csv`, `inventory/vdl_inventory.json`, optional timestamped snapshot | None |
| 2 | `fetch` | `vista-docs fetch` | Download DOCX/PDF files from VDL URLs to local storage | `inventory/vdl_inventory.csv`, VDL HTTP URLs | `raw/{app_code}/*.docx` (or `.pdf`), fetch status written to `state/pipeline.db` | `crawl` — inventory must exist |
| 3 | `ingest` | `vista-docs ingest` | Convert DOCX files to GitHub Flavored Markdown via Pandoc; extract images; scaffold YAML frontmatter | `raw/{app_code}/*.docx`; Pandoc 3.x (external) | `md-img/{app_code}/*.md` with frontmatter stub; `md-img/{app_code}/{stem}/` image dirs (001.png, …) | `fetch` — raw DOCX must exist; Pandoc installed |
| 4 | `enrich` | `vista-docs enrich` | Extract metadata from markdown content and populate YAML frontmatter (word count, revision history, stub flag, security keys, audience, TOC presence, etc.) | `md-img/{app_code}/*.md` (from ingest) | Same files updated in-place with fully populated frontmatter | `ingest` — markdown must exist |
| 5 | `enrich` (sync) | `vista-docs sync` | Sync inventory metadata (app name, section, doc type, pub date) into each document's frontmatter | `inventory/vdl_inventory_enriched.csv`, `md-img/**/*.md` | Same files updated in-place with inventory fields added | `enrich` — frontmatter must already exist |
| 6 | `survey` | `vista-docs survey` | Analyze the corpus and produce human-readable stats reports | `md-img/**/*.md` (enriched) | `survey/survey-enrichment.csv`, `survey/survey-summary.md` | `enrich` |
| 7 | `analyze` | `vista-docs headings` | Identify structural heading patterns by doc type and classify each heading (BOILERPLATE / COMMON / UNIQUE) | `md-img/**/*.md` | `survey/heading_analysis/{doc_type}.json`, `{doc_type}_lexicon.json`, `summary.md`, `lexicon_stats.md` | `ingest` |
| 8 | `analyze` | `vista-docs consolidate` | Group multi-version documents by (app, doc type, title) and consolidate into a master document with prior versions appended | `md-img/**/*.md`; groups by normalized title similarity | `consolidated/{app}/{doc_type}/{title}.md`; sibling image dirs copied alongside; `consolidated/consolidation_summary.md` | `enrich` |
| 9 | `analyze` | `vista-docs manifest` | Build the authoritative provenance index — maps every source document to its role (anchor, patch, plain) and its consolidated master if one exists | `md-img/**/*.md` | `migration/corpus-manifest.json` (package, doc_type, doc_layer, patch_id, consolidated_master, source path, SHA-256 for each doc) | `consolidate` — consolidated output must exist |
| 10 | `publish` | `vista-docs publish` | Write the human-browsable publish tree: anchor docs at `{section}/{pkg}/`, patch docs under `patches/`, image dirs copied alongside each `.md` | `consolidated/`, `md-img/`, `migration/corpus-manifest.json`, `inventory/vdl_inventory_enriched.csv` | `publish/{section}/{pkg--full-name}/{label[--variant]}.md`; `publish/{section}/{pkg}/patches/{patch-id}--{label}.md`; `publish/INDEX.md` | `consolidate` + `manifest` |
| 11 | `publish` | `vista-docs push` | Regenerate publish/ then commit and push markdown-only to GitHub (`publish/.gitignore` excludes images). Initialises the git repo on first run. | Same inputs as `publish`; remote defaults to `git@github.com:vistadocs/vdl.git` (override with `--remote`); `--no-publish` skips regeneration | New commit pushed to `origin/main`; `publish/.gitignore` written on first run | `consolidate` + `manifest`; SSH key authorised on vistadocs org |

---

## Support Modules

These modules are used by pipeline stages but are not pipeline stages themselves.

| Module | Purpose | Key Contents |
|--------|---------|--------------|
| `models` | Shared data classes used throughout the pipeline | `ManifestEntry`, `FetchStatus`, `IngestStatus` (manifest.py); `Section`, `Application`, `Document` (catalog.py) |
| `manifest` | SQLite manifest store and query operations | `store.py` — open/read/write `state/pipeline.db`; `builder.py` — inventory rows → ManifestEntry; `operations.py` — filter/query helpers |
| `classify` | Document type classifier (reserved — not yet active) | Placeholder for future ML/rule-based doc type classification |
| `migrate` | Retired site-builder I/O runners (kept for reference) | `changelog_builder.py`, `docs_builder.py`, `repo_builder.py`, `verify_builder.py` — logic modules still tested; `changelog_runner.py`, `docs_runner.py`, `repo_populator.py`, `verify_runner.py` retired, no CLI exposure |
| `config` | Centralized path and HTTP constants | `DATA_DIR`, `RAW_DIR`, `MD_IMG_DIR`, `SURVEY_DIR`, `DB_PATH`; HTTP constants (rate limit, user-agent, timeout); `VDL_BASE` URL |
| `cli` | Click-based entry point wiring all subcommands | `main.py` — `vista-docs` CLI group; subcommand registration; `--verbose` / `--pkg` global options |

---

## Data Flow Summary

```
va.gov/vdl/
    │
    ▼ crawl
inventory/vdl_inventory.csv
    │
    ▼ fetch
raw/{app}/*.docx
    │
    ▼ ingest  (Pandoc)
md-img/{app}/*.md  +  md-img/{app}/{stem}/  (images)
    │
    ▼ enrich  →  sync
md-img/{app}/*.md  (frontmatter fully populated)
    │
    ├─▶ survey        →  survey/survey-*.csv / .md
    ├─▶ headings      →  survey/heading_analysis/
    ├─▶ consolidate   →  consolidated/{app}/{doc_type}/*.md  +  images
    │       │
    │       ▼ manifest
    │   migration/corpus-manifest.json
    │       │
    │       ▼ publish
    │   publish/{section}/{pkg}/  (human-browsable tree)
    │   publish/INDEX.md
    │
    └─▶ (classify — future)
```

---

## Naming Conventions

| Layer | Format | Example |
|-------|--------|---------|
| `raw/` filenames | VA original filename | `PSO_7_0_PHARMACIST_UM.docx` |
| `md-img/` filenames | kebab-case from Pandoc | `pso-7-0-pharmacist-um.md` |
| `consolidated/` filenames | VA doc slug / safe title | `ecs_dibrg.md` |
| `publish/` dirs | `{abbrev}--{full-name}` kebab | `pso--pharmacy-outpatient-pharmacy/` |
| `publish/` filenames | `{label}[--{variant}].md` | `technical-manual--gui-v7.md` |
| `publish/patches/` filenames | `{patch-id}--{label}.md` | `pso-7-0-628--release-notes.md` |
