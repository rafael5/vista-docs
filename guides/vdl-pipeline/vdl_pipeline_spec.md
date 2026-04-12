# VistA VDL Comprehensive Analysis Pipeline — Complete Specification
**Version:** 2.0 | **Date:** 2026-03-20 | **Status:** Authoritative

---

## Table of Contents

1. [Assumptions](#1-assumptions)
2. [Environment Variables](#2-environment-variables)
3. [OS & Runtime Component Versions](#3-os--runtime-component-versions)
4. [Python Virtual Environment (uv)](#4-python-virtual-environment-uv)
5. [Directory Layout](#5-directory-layout)
6. [Pipeline Stage Table](#6-pipeline-stage-table)
7. [Quality / Validation / Verification Checks Per Stage](#7-quality--validation--verification-checks-per-stage)
8. [Gate Checks Summary](#8-gate-checks-summary)
9. [Self-Improvement Loop](#9-self-improvement-loop)
10. [Key Design Decisions](#10-key-design-decisions)

---

## 1. Assumptions

| ID | Assumption |
|---|---|
| A1 | VDL source URL: `https://www.va.gov/vdl/` — public, no authentication required |
| A2 | **Scope: active documents only.** Archived and decommissioned documents are filtered out at crawl time (Stage 1) and never inserted into `corpus.db`. The VDL site's own status taxonomy is the authority — no inference. |
| A3 | This is a **cold start** — no prior inventory, index, or downloaded files exist at pipeline initiation |
| A4 | The pipeline is **self-improving**: Stage 7 (Gap Analysis) produces a gap register that feeds back into Stage 3 (Fetch) as new fetch targets on each remediation loop iteration |
| A5 | The project root is a single directory defined by `VDLP_ROOT`; all subdirectories are defined by this spec and created by Stage 0 |
| A6 | LLM-assisted stages (S6, S8) call `api.anthropic.com` using the Anthropic Python SDK inside the venv |
| A7 | The pipeline is **human-supervised at gate checks** — no stage auto-promotes without a passing validation report written to `reports/gates/` |
| A8 | Politeness: 1 request/second with ±0.25s jitter; `robots.txt` is parsed and respected; `User-Agent` is set to `VDLP_USER_AGENT` |
| A9 | **OS: Linux Mint 22.x (Ubuntu 24.04 LTS base)** |
| A10 | **All Python runs inside a single project venv managed by `uv`.** The OS Python (`/usr/bin/python3`) is never touched. No `sudo pip`. No `--break-system-packages`. |
| A11 | **All Python packages are installed and managed exclusively with `uv`.** `pip` is never called directly by any pipeline script. |
| A12 | `SQLite corpus.db` is the **single source of truth** for all pipeline state. No JSON, CSV, or other file carries pipeline state. Markdown and TSV files in `reports/` are human-readable exports only — they are never read back as state. |
| A13 | Every stage script is **idempotent**: re-running with the same inputs produces identical outputs and skips already-completed work by querying `corpus.db` status fields before acting |
| A14 | Every stage script is **deterministic**: given the same `corpus.db` state and input files, it produces the same outputs. LLM calls use `temperature=0` and a fixed `seed` parameter where supported. |
| A15 | **Only scripts update `corpus.db` and files under `raw/`, `text/`, `state/`.** No human edits these directly. GUI tools (`sqlitebrowser`, `dbeaver`) are read-only inspection tools — humans open snapshot copies, not the live DB. |
| A16 | Snapshot copies of `corpus.db` are taken before and after every stage script run. Snapshots are retained for the 3 most recent runs per stage (pruned by `lib/snapshot_prune.sh`). |
| A17 | Self-improvement loop terminates when: the gap register is stable (zero new `fetch_new_doc` entries after a full S3→S9 pass), OR `VDLP_MAX_LOOP_ITERATIONS` is reached (default: 3) |
| A18 | Synthesis skeleton (`schema/synthesis_skeleton.md`) and eval questions (`schema/evals.json`) are **written once by a human before S8 runs** and are version-controlled. They define scope — the corpus fills the skeleton, it does not expand it. |
| A19 | Document conversion uses **Docling** as the primary converter for `.docx` and structured `.pdf`. `pdfplumber` is the fallback for PDFs that Docling fails on. LibreOffice is used only for format-conversion pre-processing (`.doc` → `.docx`), never for text extraction. |
| A20 | `ANTHROPIC_API_KEY` is stored only in `$VDLP_ROOT/.env` and is never committed to version control. `.env` is listed in `.gitignore`. |

---

## 2. Environment Variables

All variables are stored in `$VDLP_ROOT/.env`. Every script sources `scripts/lib/env.sh` which loads `.env` and validates required variables are set before proceeding.

### 2.1 Path Variables

| Variable | Value / Purpose |
|---|---|
| `VDLP_ROOT` | Absolute path to project root, e.g. `/home/user/vdlp` — set by user, never has a trailing slash |
| `VDLP_DB` | `${VDLP_ROOT}/state/corpus.db` |
| `VDLP_SCHEMA_DIR` | `${VDLP_ROOT}/schema` |
| `VDLP_SCHEMA_FILE` | `${VDLP_ROOT}/schema/document_schema.json` |
| `VDLP_SCRIPTS_DIR` | `${VDLP_ROOT}/scripts` |
| `VDLP_RAW_DIR` | `${VDLP_ROOT}/raw` |
| `VDLP_TEXT_DIR` | `${VDLP_ROOT}/text` |
| `VDLP_STATE_DIR` | `${VDLP_ROOT}/state` |
| `VDLP_SNAPSHOT_DIR` | `${VDLP_ROOT}/state/snapshots` |
| `VDLP_EXTRACTS_DIR` | `${VDLP_ROOT}/state/extracts` |
| `VDLP_REPORTS_DIR` | `${VDLP_ROOT}/reports` |
| `VDLP_LOG_DIR` | `${VDLP_ROOT}/logs` |
| `VDLP_VENV_DIR` | `${VDLP_ROOT}/.venv` |
| `VDLP_PYTHON` | `${VDLP_ROOT}/.venv/bin/python` — always the venv interpreter, never system Python |

### 2.2 Crawl & Fetch Variables

| Variable | Default | Purpose |
|---|---|---|
| `VDLP_VDL_BASE_URL` | `https://www.va.gov/vdl/` | VDL root URL |
| `VDLP_CRAWL_DELAY_SEC` | `1` | Base politeness delay between requests (seconds) |
| `VDLP_CRAWL_JITTER_SEC` | `0.25` | Random jitter added to delay (±) |
| `VDLP_CRAWL_MAX_DOCS` | `0` | 0 = unlimited; set to e.g. `20` for test/dev runs |
| `VDLP_FETCH_TIMEOUT_SEC` | `30` | HTTP request timeout |
| `VDLP_FETCH_MAX_RETRIES` | `2` | Max retry attempts before marking `permanent_error` |
| `VDLP_URL_PROBE_SAMPLE_N` | `50` | Number of URLs to HEAD-probe in S2 |
| `VDLP_URL_PROBE_PASS_PCT` | `0.95` | Minimum pass rate required to clear S2 gate |
| `VDLP_USER_AGENT` | `VistA-VDL-Research-Pipeline/2.0` | HTTP User-Agent header |

### 2.3 LLM Variables

| Variable | Default | Purpose |
|---|---|---|
| `ANTHROPIC_API_KEY` | *(set by user)* | Anthropic API key — never hardcoded |
| `VDLP_LLM_MODEL` | `claude-sonnet-4-20250514` | Model for S6 extraction and S8 synthesis |
| `VDLP_LLM_MAX_TOKENS` | `4096` | Max tokens per LLM call |
| `VDLP_LLM_TEMPERATURE` | `0` | Temperature for all LLM calls — determinism |

### 2.4 Pipeline Control Variables

| Variable | Default | Purpose |
|---|---|---|
| `VDLP_MAX_LOOP_ITERATIONS` | `3` | Self-improvement loop hard termination limit |
| `VDLP_SNAPSHOT_KEEP_N` | `3` | Snapshots retained per stage/phase |
| `VDLP_MIN_CONVERTED_WORD_PCT` | `0.20` | Min ratio of converted:estimated source words (S4 validation) |
| `VDLP_MIN_EVAL_PASS_RATE` | `0.80` | Min eval pass rate to clear S9 gate |
| `VDLP_MIN_EXTRACT_PASS_RATE` | `0.95` | Min extraction success rate to clear S6 validation |

### 2.5 Version Pin Variables (enforced by S0)

| Variable | Required Value |
|---|---|
| `VDLP_REQUIRE_BASH_VERSION` | `5.2` |
| `VDLP_REQUIRE_PYTHON_VERSION` | `3.12` |
| `VDLP_REQUIRE_SQLITE_VERSION` | `3.45` |
| `VDLP_REQUIRE_UV_VERSION` | `0.4` |

---

## 3. OS & Runtime Component Versions

### 3.1 System Components (Linux Mint 22.x / Ubuntu 24.04 LTS)

| Component | Shipped Version | Minimum Required | Check Command |
|---|---|---|---|
| Bash | 5.2.21 | 5.2 | `bash --version` |
| SQLite CLI | 3.45.1 | 3.45 | `sqlite3 --version` |
| curl | 8.5.0 | 8.0 | `curl --version` |
| git | 2.43.0 | 2.40 | `git --version` |
| LibreOffice | 24.2.x | 24.0 | `libreoffice --version` |
| uv | 0.4.x | 0.4 | `uv --version` |
| System Python | 3.12.x | *(not used by pipeline)* | `python3 --version` |

**System Python is never called by any pipeline script.** It is listed here only for reference. All pipeline execution uses `$VDLP_PYTHON` = `${VDLP_ROOT}/.venv/bin/python`.

`uv` is installed system-wide (not in venv) via: `curl -LsSf https://astral.sh/uv/install.sh | sh`

### 3.2 Python Runtime (inside venv)

| Component | Version | Purpose |
|---|---|---|
| Python | 3.12.x | Runtime — provisioned by `uv` from `pyproject.toml` |
| anthropic | 0.34.x | Anthropic SDK for S6, S8 LLM calls |
| docling | 2.x | Primary .docx and structured PDF converter (S4) |
| pdfplumber | 0.11.x | Fallback PDF text extractor (S4) |
| requests | 2.32.x | HTTP crawl, probe, fetch (S1, S2, S3) |
| beautifulsoup4 | 4.12.x | HTML parsing for crawl (S1) |
| lxml | 5.2.x | XML/HTML parser backend for bs4 (S1) |
| jsonschema | 4.22.x | Schema validation for document records and extracts |
| python-dotenv | 1.0.x | `.env` file loading in Python scripts |
| rich | 13.x | Structured console output and progress bars |
| tenacity | 8.x | Retry logic for HTTP and LLM calls |

All versions are pinned in `pyproject.toml` with lower-bound constraints. `uv lock` produces a `uv.lock` file that pins exact transitive versions for full reproducibility.

---

## 4. Python Virtual Environment (uv)

### 4.1 Setup (one-time, run by S0)

```
# S0 runs these — never run manually
uv venv ${VDLP_ROOT}/.venv --python 3.12
uv pip install --project ${VDLP_ROOT} -r pyproject.toml
```

`pyproject.toml` lives at `${VDLP_ROOT}/pyproject.toml`. `uv.lock` lives alongside it. Both are version-controlled.

### 4.2 Activation

Pipeline scripts **do not activate the venv**. They call the interpreter directly:

```bash
${VDLP_PYTHON} scripts/s1_crawl.py
# expands to: /home/user/vdlp/.venv/bin/python scripts/s1_crawl.py
```

This is explicit, unambiguous, and immune to shell activation state. No `source .venv/bin/activate` anywhere in pipeline scripts.

### 4.3 Package Updates

```bash
# To add a package:
uv add <package>          # updates pyproject.toml and uv.lock
# To sync all packages to lock file:
uv sync
# Never use:
pip install ...           # FORBIDDEN in this project
```

---

## 5. Directory Layout

```
$VDLP_ROOT/
│
├── .env                              # All environment variables (not version-controlled)
├── .gitignore                        # Excludes: .env, .venv/, raw/, state/snapshots/, logs/
├── pyproject.toml                    # Python dependencies (uv-managed)
├── uv.lock                           # Exact pinned dependency tree
│
├── schema/                           # Static definition artifacts — version-controlled
│   ├── document_schema.json          # Canonical DB record schema (S0 creates, all stages validate against)
│   ├── extract_schema.json           # Schema for per-document LLM extraction JSON (S6)
│   ├── synthesis_skeleton.md         # Guide structure skeleton — written by human before S8
│   └── evals.json                    # Eval questions — written by human before S9
│
├── scripts/
│   ├── lib/                          # Shared utilities — sourced/imported, not run directly
│   │   ├── env.sh                    # Bash env loader + version checks
│   │   ├── env.py                    # Python env loader (loads .env, exports to os.environ)
│   │   ├── db.py                     # Python DAO layer — all DB reads/writes go through here
│   │   ├── snapshot.sh               # db_snapshot_before / db_snapshot_after functions
│   │   ├── snapshot_prune.sh         # Prune old snapshots to VDLP_SNAPSHOT_KEEP_N
│   │   ├── db_report.py              # Generate one-page Markdown DB summary
│   │   └── db_diff_report.sh         # Pre/post diff wrapper — calls db_report.py on both snapshots
│   │
│   ├── run_s0_bootstrap.sh           # Stage runner: snapshots + calls s0_bootstrap.py + diff report
│   ├── run_s1_crawl.sh               # Stage runner
│   ├── run_s2_url_probe.sh           # Stage runner
│   ├── run_s3_fetch.sh               # Stage runner
│   ├── run_s4_convert.sh             # Stage runner
│   ├── run_s5_classify.sh            # Stage runner
│   ├── run_s6_extract.sh             # Stage runner
│   ├── run_s7_gap_analysis.sh        # Stage runner
│   ├── run_s8_synthesize.sh          # Stage runner
│   ├── run_s9_eval.sh                # Stage runner
│   ├── run_s10_remediate.sh          # Stage runner
│   │
│   ├── s0_bootstrap.py               # Create dirs, DB schema, validate environment
│   ├── s1_crawl.py                   # Crawl VDL, build inventory (active docs only)
│   ├── s1_validate.py                # S1 post-run validation
│   ├── s2_url_probe.py               # HEAD-probe all source_urls, write url_probe_status
│   ├── s3_fetch.py                   # Download raw files to raw/
│   ├── s3_validate.py                # S3 post-run validation
│   ├── s4_convert.py                 # Convert raw files to Markdown in text/
│   ├── s4_validate.py                # S4 post-run validation
│   ├── s5_classify.py                # Classify doc_type, package_code, content_tags per doc
│   ├── s5_validate.py                # S5 post-run validation
│   ├── s6_extract.py                 # LLM-assisted structured extraction per doc
│   ├── s6_validate.py                # S6 post-run validation
│   ├── s7_gap_analysis.py            # Build gap register from corpus + extracts
│   ├── s7_validate.py                # S7 post-run validation
│   ├── s8_synthesize.py              # LLM-assisted guide synthesis
│   ├── s8_validate.py                # S8 post-run validation
│   ├── s9_eval.py                    # Run eval questions against architecture guide
│   └── s10_gap_remediate.py          # Gap remediation + self-improvement loop control
│
├── raw/                              # Downloaded binary files — never edited by humans
│   └── {doc_id}/
│       └── {filename}.{ext}          # Original file as downloaded
│
├── text/                             # Converted Markdown files — never edited by humans
│   └── {doc_id}/
│       └── {filename}.md             # Docling/pdfplumber output
│
├── state/
│   ├── corpus.db                     # SINGLE SOURCE OF TRUTH — never edited by humans or GUI tools
│   ├── extracts/                     # Per-document LLM extraction JSON (S6 output)
│   │   └── {doc_id}_extract.json
│   ├── snapshots/                    # DB snapshots — openable in sqlitebrowser/dbeaver
│   │   ├── s1_crawl_before_20260320T120000Z.db
│   │   ├── s1_crawl_after_20260320T120500Z.db
│   │   ├── .last_before_s1_crawl     # Pointer file (plain text, one path)
│   │   ├── .last_after_s1_crawl
│   │   └── ...
│   └── loop_state.json               # Self-improvement loop iteration counter + termination record
│
├── reports/
│   ├── gates/                        # Gate pass/fail reports — written by validation scripts
│   │   ├── s2_gate_PASS_20260320T121000Z.md
│   │   ├── s9_gate_FAIL_20260320T150000Z.md
│   │   └── ...
│   ├── diffs/                        # Pre/post DB diff reports per stage run
│   │   ├── db_diff_s1_crawl_20260320T120500Z.md
│   │   └── ...
│   ├── gap_register.md               # Living gap register (human-readable export from DB)
│   ├── coverage_map.tsv              # Topic → document coverage matrix
│   ├── architecture_guide.md         # PRIMARY SYNTHESIS OUTPUT
│   ├── provenance.json               # Claim → source sidecar for architecture_guide.md
│   └── eval_results.json             # Eval run results per version
│
└── logs/                             # Per-stage timestamped run logs
    ├── s1_crawl_20260320T120000Z.log
    └── ...
```

---

## 6. Pipeline Stage Table

| Stage | Name | Runner Script | Core Script(s) | Inputs | Outputs |
|---|---|---|---|---|---|
| **S0** | Bootstrap & Environment | `run_s0_bootstrap.sh` | `s0_bootstrap.py` | `.env`, `pyproject.toml` | Full directory tree; `corpus.db` with empty schema; `document_schema.json`; `extract_schema.json` |
| **S1** | Crawl & Inventory | `run_s1_crawl.sh` | `s1_crawl.py`, `s1_validate.py` | `VDLP_VDL_BASE_URL`; empty `corpus.db` | `corpus.db` populated with one row per **active** document (`fetch_status=pending`); crawl log |
| **S2** | URL Probe | `run_s2_url_probe.sh` | `s2_url_probe.py` | `corpus.db` (all `source_url` values) | `corpus.db` `url_probe_status` field updated per row; `reports/gates/s2_gate_*.md` |
| **S3** | Fetch (Download) | `run_s3_fetch.sh` | `s3_fetch.py`, `s3_validate.py` | `corpus.db` (`url_probe_status=200\|301`); `VDLP_RAW_DIR` | Binary files in `raw/{doc_id}/`; `corpus.db` `fetch_status` updated |
| **S4** | Convert to Text | `run_s4_convert.sh` | `s4_convert.py`, `s4_validate.py` | Binary files in `raw/`; `corpus.db` | Markdown files in `text/{doc_id}/`; `corpus.db` `convert_status` updated |
| **S5** | Classify & Survey | `run_s5_classify.sh` | `s5_classify.py`, `s5_validate.py` | Markdown files in `text/`; `corpus.db` | `corpus.db` `doc_type`, `package_code`, `content_tags` populated; `reports/coverage_map.tsv` |
| **S6** | Structured Extraction | `run_s6_extract.sh` | `s6_extract.py`, `s6_validate.py` | Markdown files in `text/`; `corpus.db`; LLM API | `state/extracts/{doc_id}_extract.json` per doc; `corpus.db` `extract_status` updated |
| **S7** | Gap Analysis | `run_s7_gap_analysis.sh` | `s7_gap_analysis.py`, `s7_validate.py` | `corpus.db`; `state/extracts/`; `reports/coverage_map.tsv` | `corpus.db` `gap_register` table populated; `reports/gap_register.md` |
| **S8** | Synthesis | `run_s8_synthesize.sh` | `s8_synthesize.py`, `s8_validate.py` | `state/extracts/`; `coverage_map.tsv`; `gap_register.md`; `schema/synthesis_skeleton.md`; LLM API | `reports/architecture_guide.md`; `reports/provenance.json` |
| **S9** | Eval & Quality Gate | `run_s9_eval.sh` | `s9_eval.py` | `reports/architecture_guide.md`; `schema/evals.json` | `reports/eval_results.json`; `reports/gates/s9_gate_*.md` |
| **S10** | Gap Remediation | `run_s10_remediate.sh` | `s10_gap_remediate.py` | `corpus.db` `gap_register` table; `reports/eval_results.json`; `state/loop_state.json` | New `fetch_status=pending` rows in `corpus.db` for remediable gaps; updated `reports/gap_register.md`; updated `state/loop_state.json`; triggers S3→S9 re-run for new targets only |

### Stage Runner Script Pattern (all runners identical in structure)

Every `run_sN_*.sh` follows this exact pattern — no exceptions:

```bash
#!/usr/bin/env bash
set -euo pipefail
source "${VDLP_ROOT}/scripts/lib/env.sh"       # loads .env, checks versions
source "${VDLP_ROOT}/scripts/lib/snapshot.sh"  # provides db_snapshot_before/after

STAGE="s1_crawl"                               # unique per runner

db_snapshot_before "${STAGE}"
"${VDLP_PYTHON}" "${VDLP_SCRIPTS_DIR}/s1_crawl.py"     2>&1 | tee "${VDLP_LOG_DIR}/${STAGE}_$(date -u +%Y%m%dT%H%M%SZ).log"
db_snapshot_after  "${STAGE}"
bash "${VDLP_SCRIPTS_DIR}/lib/db_diff_report.sh" "${STAGE}"
```

---

## 7. Quality / Validation / Verification Checks Per Stage

### Stage 0 — Bootstrap

| Check Type | Check | Failure Action |
|---|---|---|
| **Pre-run** | Bash version ≥ 5.2 (`bash --version`) | Abort with version mismatch message |
| **Pre-run** | Python 3.12 available at `$VDLP_PYTHON` path | Abort |
| **Pre-run** | SQLite ≥ 3.45 (`sqlite3 --version`) | Abort |
| **Pre-run** | `uv` ≥ 0.4 installed system-wide | Abort |
| **Pre-run** | `ANTHROPIC_API_KEY` is set (non-empty) | Abort |
| **Pre-run** | `VDLP_ROOT` directory is writable | Abort |
| **Pre-run** | Disk space ≥ 20GB free at `VDLP_ROOT` | Abort |
| **Post-run** | All 12 subdirectories created and writable | Assert |
| **Post-run** | `corpus.db` opens, returns schema tables | Assert |
| **Post-run** | `document_schema.json` is valid JSON Schema (self-validates) | Assert |
| **Post-run** | `extract_schema.json` is valid JSON Schema | Assert |
| **Post-run** | venv Python responds at `${VDLP_PYTHON} --version` | Assert |
| **Post-run** | All required Python packages importable from venv | Assert |

### Stage 1 — Crawl & Inventory

| Check Type | Check | Failure Action |
|---|---|---|
| **Pre-run** | S0 gate recorded as PASS in `corpus.db` `pipeline_gates` table | Abort |
| **Pre-run** | `corpus.db` `documents` table has zero rows (cold-start guard) | Abort if rows > 0 and `VDLP_CRAWL_MAX_DOCS=0` (prevents accidental re-crawl) |
| **Pre-run** | Network reachable: HEAD `VDLP_VDL_BASE_URL` returns 200 | Abort |
| **Pre-run** | `robots.txt` fetched and parsed; crawl path not disallowed | Abort if disallowed |
| **Post-run** | Row count > 500 (VDL has thousands of active docs) | WARN + write to gate report |
| **Post-run** | Zero NULL values in `doc_id`, `source_url`, `filename`, `filetype` | Assert |
| **Post-run** | Zero duplicate `doc_id` values | Assert |
| **Post-run** | `status` field = `active` for 100% of rows (scope enforcement) | Assert |
| **Post-run** | `url_probe_status` = `pending` for 100% of rows (not yet probed) | Assert |
| **Post-run** | `last_updated` populated for all rows | Assert |
| **Post-run** | File extension distribution: ≥ 70% `.docx` or `.pdf` | WARN if not met |
| **Post-run** | Every `source_url` starts with `https://www.va.gov/vdl/` | Assert |

### Stage 2 — URL Probe

| Check Type | Check | Failure Action |
|---|---|---|
| **Pre-run** | S1 post-validation PASS recorded in `pipeline_gates` | Abort |
| **Pre-run** | All `corpus.db` rows have `url_probe_status=pending` | Abort if any already probed (idempotency: skip already-probed, warn if all complete) |
| **Post-run** | Zero rows with NULL `url_probe_status` | Assert |
| **post-run** | Probe summary written to `logs/s2_probe_summary.json` | Assert |
| **GATE** | ≥ 95% of probed URLs return 200 or 301 | **HARD HALT** — write `reports/gates/s2_gate_FAIL_*.md` with URL pattern diagnostics; pipeline does not proceed to S3 until human reviews and re-runs S2 |
| **Post-GATE** | Gate result written to `corpus.db` `pipeline_gates` table | Assert |

### Stage 3 — Fetch

| Check Type | Check | Failure Action |
|---|---|---|
| **Pre-run** | S2 gate PASS in `pipeline_gates` | Abort |
| **Pre-run** | `VDLP_RAW_DIR` writable | Abort |
| **Pre-run** | Disk space ≥ 10GB free | Abort |
| **During** | `fetch_status` written back immediately after each document (not batched) | Enforced in DAO layer |
| **During** | No row left in `fetch_status=fetching` at script exit | Enforced by cleanup handler |
| **Post-run** | Count of `fetch_status=ok` rows equals count of files in `raw/` | Assert |
| **Post-run** | Zero files in `raw/` with size < 1KB | Assert |
| **Post-run** | `fetch_status` for every row is in `{ok, 404, permanent_error, error}` — no nulls, no `fetching` | Assert |
| **Post-run** | `fetch_status=ok` rate ≥ 85% of `url_probe_status=200` rows | WARN if below; write to gate report |
| **Post-run** | All `permanent_error` rows have non-null `fetch_error` message | Assert |

### Stage 4 — Convert

| Check Type | Check | Failure Action |
|---|---|---|
| **Pre-run** | S3 post-validation PASS in `pipeline_gates` | Abort |
| **Pre-run** | Docling importable from venv | Abort |
| **Pre-run** | `VDLP_TEXT_DIR` writable | Abort |
| **During** | `convert_status` written back immediately per document | Enforced in DAO |
| **During** | No row in `convert_status=converting` at script exit | Enforced by cleanup handler |
| **Post-run** | Count of `convert_status=ok` equals count of `.md` files in `text/` | Assert |
| **Post-run** | Zero `.md` files with size < 100 bytes | Assert |
| **Post-run** | Each `.md` file contains ≥ 1 line starting with `#` (heading present) | Assert |
| **Post-run** | Sampled word count: converted ≥ `VDLP_MIN_CONVERTED_WORD_PCT` × estimated source words | WARN per failing doc; log for manual review |
| **Post-run** | `convert_status=ok` rate ≥ 90% of `fetch_status=ok` rows | WARN if below |
| **Post-run** | All `converted_error` rows have non-null `ingest_error` message | Assert |

### Stage 5 — Classify & Survey

| Check Type | Check | Failure Action |
|---|---|---|
| **Pre-run** | S4 post-validation PASS in `pipeline_gates` | Abort |
| **Pre-run** | All `convert_status=ok` rows have a corresponding `.md` file in `text/` | Assert |
| **Post-run** | Zero rows with `convert_status=ok` and NULL `doc_type` | Assert |
| **Post-run** | `package_code` populated for ≥ 90% of `convert_status=ok` rows | Assert |
| **Post-run** | `coverage_map.tsv` written and non-empty | Assert |
| **Post-run** | Coverage map contains ≥ 1 row for each of the 29 known VistA packages | WARN for any missing package |
| **Post-run** | All `content_tags` values are from the controlled vocabulary defined in `schema/content_tag_vocab.json` | Assert |

### Stage 6 — Structured Extraction (LLM)

| Check Type | Check | Failure Action |
|---|---|---|
| **Pre-run** | S5 post-validation PASS in `pipeline_gates` | Abort |
| **Pre-run** | `ANTHROPIC_API_KEY` valid: test call returns 200 | Abort |
| **Pre-run** | `state/extracts/` writable | Abort |
| **During** | Each extract JSON validated against `schema/extract_schema.json` before writing | Re-queue on validation failure; mark `extract_status=schema_error` after `VDLP_FETCH_MAX_RETRIES` |
| **During** | `extract_status` written back immediately per document | Enforced in DAO |
| **Post-run** | `extract_status=ok` rate ≥ `VDLP_MIN_EXTRACT_PASS_RATE` (default 95%) of `convert_status=ok` rows | Assert |
| **Post-run** | Aggregate across all extracts: ≥ 100 unique RPC names extracted | Assert |
| **Post-run** | Aggregate: ≥ 50 unique FileMan file numbers extracted | Assert |
| **Post-run** | Aggregate: ≥ 20 unique VistA package codes extracted | Assert |
| **Post-run** | Zero extract JSON files that fail `extract_schema.json` validation | Assert |

### Stage 7 — Gap Analysis

| Check Type | Check | Failure Action |
|---|---|---|
| **Pre-run** | S6 post-validation PASS in `pipeline_gates` | Abort |
| **Pre-run** | Count of `extract_status=ok` extracts matches count of files in `state/extracts/` | Assert |
| **Post-run** | `gap_register` table created in `corpus.db` with ≥ 1 row | Assert |
| **Post-run** | Every gap row has non-null: `package_code`, `gap_type`, `severity` | Assert |
| **Post-run** | `severity` values restricted to `{critical, major, minor}` | Assert |
| **Post-run** | `gap_register.md` written to `reports/` and is non-empty | Assert |
| **Post-run** | Gap register in DB and MD file have identical row counts | Assert (export fidelity check) |

### Stage 8 — Synthesis (LLM)

| Check Type | Check | Failure Action |
|---|---|---|
| **Pre-run** | S7 post-validation PASS in `pipeline_gates` | Abort |
| **Pre-run** | `schema/synthesis_skeleton.md` exists and is non-empty | Abort |
| **Pre-run** | `schema/evals.json` exists with ≥ 8 questions (evals written before synthesis) | Abort |
| **Pre-run** | `ANTHROPIC_API_KEY` valid | Abort |
| **Post-run** | `architecture_guide.md` word count > 5,000 | Assert |
| **Post-run** | `provenance.json` has ≥ 1 entry per major guide section (sections defined in skeleton) | Assert |
| **Post-run** | Zero guide sections contain only the literal placeholder text `TBD` | Assert |
| **Post-run** | Guide contains a `## Coverage Status` section with a gap table | Assert |
| **Post-run** | All VistA identifiers in guide (file numbers, RPC names) are traceable to a provenance entry | Assert |

### Stage 9 — Eval & Quality Gate

| Check Type | Check | Failure Action |
|---|---|---|
| **Pre-run** | S8 post-validation PASS in `pipeline_gates` | Abort |
| **Pre-run** | `schema/evals.json` has ≥ 8 questions | Abort |
| **Pre-run** | `reports/architecture_guide.md` exists | Abort |
| **Post-run** | `eval_results.json` written and valid JSON | Assert |
| **Post-run** | Every eval question has a recorded `pass` or `fail` result | Assert |
| **GATE** | Pass rate ≥ `VDLP_MIN_EVAL_PASS_RATE` (default 80%) | **HARD HALT** if below — write `reports/gates/s9_gate_FAIL_*.md` with per-question failures; pipeline does not proceed to S10 |
| **Post-GATE** | Gate result written to `corpus.db` `pipeline_gates` table | Assert |

### Stage 10 — Gap Remediation

| Check Type | Check | Failure Action |
|---|---|---|
| **Pre-run** | S9 gate PASS in `pipeline_gates` | Abort |
| **Pre-run** | `state/loop_state.json` exists; current iteration < `VDLP_MAX_LOOP_ITERATIONS` | Abort if max iterations reached — write termination record |
| **Post-run** | Every gap entry has `remediation_action` in `{fetch_new_doc, out_of_scope, accepted_gap}` | Assert |
| **Post-run** | All new `fetch_new_doc` rows have valid `source_url` (not null, starts with `https://`) | Assert |
| **Post-run** | Zero duplicate `doc_id` values introduced | Assert |
| **Post-run** | `loop_state.json` updated with: iteration number, gap counts before/after, termination reason if final | Assert |
| **Post-run** | If zero new `fetch_new_doc` entries: loop termination recorded as `stable_gap_register` | Assert |

---

## 8. Gate Checks Summary

Two stages produce **hard pipeline halts**. All other validation failures produce warnings logged to `reports/gates/` and `corpus.db` `pipeline_gates` table but do not halt.

| Gate | Stage | Condition | Halt Behavior |
|---|---|---|---|
| **URL Probe Gate** | End of S2 | < 95% of probed URLs return 200 or 301 | Write `reports/gates/s2_gate_FAIL_<ts>.md` with URL pattern diagnostics and distribution of status codes; write FAIL to `pipeline_gates`; S3 refuses to start until S2 gate = PASS |
| **Eval Quality Gate** | End of S9 | Pass rate < 80% across eval questions | Write `reports/gates/s9_gate_FAIL_<ts>.md` with per-question pass/fail, guide section gaps, and recommended corpus expansions; write FAIL to `pipeline_gates`; S10 refuses to start until S9 gate = PASS |

### Gate Enforcement Mechanism

Gates are not enforced by file presence — they are enforced by the `pipeline_gates` table in `corpus.db`. Every stage's pre-run check queries:

```sql
SELECT result FROM pipeline_gates
WHERE stage = 's2_url_probe'
ORDER BY recorded_at DESC
LIMIT 1;
```

If the result is not `PASS`, the stage aborts. This means a gate cannot be bypassed by deleting a file or touching a timestamp — the DB must record a PASS.

---

## 9. Self-Improvement Loop

```
S7 Gap Analysis → classifies each gap:
    ├── fetch_new_doc   → URL identified in VDL not yet in corpus
    ├── out_of_scope    → gap acknowledged, explicitly excluded from guide
    └── accepted_gap    → gap documented in guide Coverage Status table

S10 Remediation → for fetch_new_doc gaps:
    └── inserts new rows into corpus.db as fetch_status=pending
        └── triggers partial re-run: S3 → S4 → S5 → S6 → S7 → S8 → S9
            (only new documents processed in S3–S6; S7–S9 re-run on full corpus)

Loop terminates when EITHER:
    (a) gap_register is stable: zero new fetch_new_doc entries after full pass, OR
    (b) loop iteration count reaches VDLP_MAX_LOOP_ITERATIONS (default: 3)

Termination is deterministic:
    - VDL is a finite library
    - doc_id uniqueness enforced — no document fetched twice
    - max iterations is a hard environment variable
```

`state/loop_state.json` records: current iteration, entry gap count, exit gap count, termination reason. This file is the only JSON file that carries state — it is written only by S10 and read only by S10's pre-run check.

---

## 10. Key Design Decisions

| Decision | Rationale |
|---|---|
| **uv for all Python package management** | Order-of-magnitude faster than pip for installs and syncs; `uv.lock` provides exact reproducibility across machines; `uv venv` provisions the correct Python version without touching OS Python |
| **Venv interpreter called directly (`${VDLP_PYTHON}`), never via `source activate`** | Shell activation state is fragile and invisible in logs. Direct path is explicit, auditable, and immune to `PATH` manipulation |
| **OS Python never touched** | Linux Mint 22 / Ubuntu 24.04 ships Python 3.12 as a system component used by OS tools. Altering it breaks package managers. The venv is completely isolated. |
| **SQLite is the only state store** | JSON manifests edited by multiple scripts drift into silent inconsistency. One DB, one DAO layer (`lib/db.py`), one writer per field. Every script imports `db.py` — no script writes SQL directly. |
| **`pipeline_gates` table in DB, not gate files** | Gate state cannot be bypassed by file deletion or timestamp manipulation. The DB record is authoritative. Every stage's pre-run check queries the table. |
| **URL Probe is a dedicated stage (S2), not part of S1 crawl** | The previous run's URL pattern bug (`/documents/` vs `/vdl/documents/`) caused 6,935 failed fetch attempts before detection. Probing is cheap (HEAD requests, no body); fetching is expensive (full download). Separating them makes the bug surface before any bytes are downloaded. |
| **Snapshot copies are openable in GUI tools; live DB is never opened in GUI tools** | `sqlitebrowser` and DBeaver are read-only inspection tools for this project. They must never open `corpus.db` directly — file locking during a pipeline run would corrupt state. Snapshots are independent `.db` copies — safe to open at any time. |
| **LLM extraction (S6) is separate from synthesis (S8)** | Extraction is mechanical and verifiable: pull FileMan file numbers, RPC names, globals, HL7 types. Each result validates against `extract_schema.json`. Synthesis is generative. Mixing them makes extraction outputs unverifiable and synthesis ungovernable. |
| **Synthesis skeleton and evals written before S8 runs** | Skeleton defines scope — the corpus fills it, it does not expand it. Evals define quality — they are written before content so quality is measurable, not just legible. Both are version-controlled artifacts. |
| **`temperature=0` for all LLM calls** | Pipeline is deterministic. Identical inputs must produce identical outputs on re-runs. Temperature 0 is the primary mechanism. |
| **Gap register stored in DB, not only in Markdown** | `gap_register.md` is a human-readable export. S10 reads gap remediation actions from `corpus.db` `gap_register` table programmatically. Markdown files are never read back as input to any script. |
| **Active-only scope enforced at crawl time (S1), not post-filter** | Archived and decommissioned documents are never inserted into `corpus.db`. They do not consume disk space in `raw/` or `text/`. The `status=active` filter is applied during HTML parsing in S1 against the VDL's own taxonomy — never inferred. |
| **`VDLP_CRAWL_MAX_DOCS` test limiter** | Every developer working on this pipeline can run `VDLP_CRAWL_MAX_DOCS=20` to validate output shape on a small sample before committing to a full crawl. This variable is checked at the start of S1 and documented in `.env`. |
| **One runner script per stage, one core script per stage** | Runner scripts handle cross-cutting concerns (snapshots, logging, diff reports). Core scripts do exactly one thing. Separation means core scripts are independently testable with `VDLP_CRAWL_MAX_DOCS=5`. |
