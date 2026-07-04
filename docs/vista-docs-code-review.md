# vista-docs — Comprehensive Code Review

**Date:** 2026-06-01
**Scope:** all active code under `src/vista_docs/`, `pipeline/`, `scripts/`, the CLI, the Makefile, and the supporting docs.
**Question asked:** Is the pipeline organized, modular, and self-documenting enough that (a) a third-party author could understand it and (b) it will be easy to change six months from now? Does each stage have a preflight check that the prior stage completed and a postflight validation? Verdict: *needs refactor* or not?

---

## 1. Headline verdict

**NEEDS REFACTOR — structural, not a rewrite.**

The *components* are good: the `normalize/` package has a textbook pure/IO split, test discipline is real (55 test files, 95% gate), and the prose documentation (`docs/vdl-arch-overview.md`, `src/vista_docs/README.md`) is unusually thorough. The pure ETL logic is sound.

The *system* has drifted. New phases (index 6–6.7, normalize, consolidate, manifest, publish, validate) were bolted on faster than the organization, orchestration, and gating could keep up. The result is a pipeline that is **hard to run end-to-end, hard to reason about as a whole, and carries dead weight and naming traps that will actively mislead a future reader.**

The single most important gap is exactly the one you asked about: **there is no real preflight/postflight contract between stages, and the one command that is supposed to chain them is a stub.** A new operator cannot, today, run the pipeline from a documented single entry point and have it fail loudly when a prerequisite is missing.

Severity legend: 🔴 blocker for "easy to maintain / understand" · 🟠 significant · 🟡 minor / polish.

---

## 2. Orchestration is fictional (🔴)

This is the headline finding.

- **`vista-docs pipeline` is a no-op stub.** `cli/main.py:749-755` loops over `["crawl","fetch","ingest","survey"]`, echoes each stage name, and prints `"(not yet implemented)"`. It runs nothing.
- **`make pipeline` calls that stub** (`Makefile:89-90`). The documented headline orchestration target does nothing.
- **Even the *intended* scope is incomplete.** The stub's stage list is `crawl → fetch → ingest → survey`. It omits `enrich`, `sync`, the 6–6.7 DB build, `consolidate`, `manifest`, `normalize`, `publish`, and `validate`. There is no single command — implemented or even *designed* — that builds the full corpus.
- **`normalize` has no Makefile target at all.** The `.PHONY` list (`Makefile:1-3`) and targets cover everything except `normalize`. Since `publish` silently falls back to `consolidated/` bodies when `normalized/` is absent (`cli/main.py:629-642`), a `make`-driven workflow will quietly publish un-normalized markdown and never tell you.
- **Three different execution models coexist** for what is conceptually one pipeline:
  1. CLI subcommands (`crawl`…`sync`, `consolidate`…`push`) — stages 1–5, 8–11.
  2. Loose standalone scripts (`python3 pipeline/audit_frontmatter.py` …) — stages 6–6.7.
  3. A 1448-line hand-run script (`scripts/enrich_inventory.py`) that is *secretly mandatory* (see §5).

A third-party author landing on this repo has no obvious "run the pipeline" button, and the button that looks like one lies to them.

**Impact on your two goals:** this alone fails both "easy for a third party to understand" and "easy to change in six months." The mental model of the pipeline lives only in docs and in the operator's head, not in runnable code.

---

## 3. No preflight/postflight contract between stages (🔴)

You specifically asked that each phase verify the prior stage completed before running, and validate its own output so the next stage knows it is safe to proceed. **Today this is inconsistent and mostly absent.**

### 3.1 Preflight (does this stage confirm its prerequisite ran?)

| Stage | Preflight today | Quality |
|---|---|---|
| crawl | none (first stage) | n/a |
| fetch | checks `vdl_inventory.csv` exists (`main.py:107`) | ✅ explicit |
| ingest | implicit — queries DB for `fetch_status==OK`; empty result just processes 0 | ⚠️ silent |
| enrich | implicit — queries `ingest_status==OK` | ⚠️ silent |
| sync | checks `vdl_inventory_enriched.csv` exists (`main.py:267`) | ✅ explicit |
| survey | implicit — `ingest_status==OK` query | ⚠️ silent |
| headings | none | ❌ |
| consolidate | none — reads `md-img/`, processes 0 if empty | ❌ |
| normalize | none explicit — reads `consolidated/`, processes 0 if empty | ❌ |
| manifest | none — builds from `md-img/` | ❌ |
| validate | checks target dir exists (`main.py:566`) | ✅ explicit |
| publish | checks `corpus-manifest.json` exists (`main.py:619`) | ✅ explicit |
| push | checks manifest (or `publish/` if `--no-publish`) | ✅ explicit |
| **6 audit** | `--pkg` dir existence only | ⚠️ shallow |
| **6.5 chunk** | `frontmatter.db` *file* exists | ⚠️ shallow |
| **6.6 entities** | `frontmatter.db` *file* exists | ⚠️ shallow |
| **6.7 quality** | `frontmatter.db` *file* exists | ⚠️ shallow |

The pattern is three different idioms (explicit file check / silent DB query / nothing) applied unevenly. The 6.x "preflight" is a **file-exists check, not a stage-completion check** — `frontmatter.db` exists the moment stage 6 runs once, so 6.5/6.6/6.7 happily run against a *stale or partial* DB and silently emit degraded output (zero sections, quality scores computed against missing components) with no error.

### 3.2 Postflight (does this stage bless its own output?)

Only **two** stages validate their output:
- `normalize` runs the §11 validation gate and refuses on hard issues (`main.py:452-458`).
- `publish`/`push` run `_run_validation_gate` (`main.py:499-544`) — the genuinely good, durable hard gate that makes it impossible to push a broken corpus.

Every other stage (crawl, fetch, ingest, enrich, sync, survey, headings, consolidate, manifest, 6–6.7) produces output with **no postflight check** that the next stage can rely on. The acquire DB (`pipeline.db`) tracks per-doc `fetch_status`/`ingest_status`, which is good bookkeeping, but nothing aggregates it into a "stage N is complete and clean → stage N+1 may run" signal.

### 3.3 What "good" looks like here

The `_run_validation_gate` pattern is exactly the right shape — it just needs to be generalized into a per-stage contract:

- **A uniform preflight helper**: each stage declares its required inputs (a file, a populated table, a prior-stage "done" marker) and raises a `ClickException` with a remediation hint (`Run: vista-docs <prev>`) when missing. Several stages already do this ad hoc; lift it into one helper so coverage is uniform and the *quality* of the check is "prior stage actually produced N expected outputs," not "a file exists."
- **A uniform postflight stamp**: each stage writes a small completion record (counts + status + timestamp + input fingerprint) — either rows in a `stage_runs` table or a `state/<stage>.done.json`. The next stage's preflight reads that record instead of guessing from file presence. This is the "next stage knows it's ok to run" signal you asked for, and it makes the whole pipeline introspectable.
- **A real `pipeline` orchestrator** that chains stages, runs each stage's preflight → work → postflight, and stops on the first hard failure.

This is the highest-value refactor in the whole review and directly answers your central requirement.

---

## 4. Dead and orphaned code (🟠)

Confirmed by import-graph analysis across `src/`, `pipeline/`, `scripts/`, `cli/`, and `tests/`.

### 4.1 `migrate/` — entire package is unreachable (~1,346 LOC + 4 test files)

The README already admits this is "retired," and the import graph confirms it is **completely disconnected from every runnable entry point**:

| Module | LOC | Status |
|---|---|---|
| `changelog_builder.py` | 175 | TEST-ONLY (only its own unit test imports it) |
| `docs_builder.py` | 155 | TEST-ONLY |
| `repo_builder.py` | 285 | TEST-ONLY |
| `verify_builder.py` | 86 | TEST-ONLY |
| `changelog_runner.py` | 110 | **DEAD** (no importer, no `__main__`) |
| `docs_runner.py` | 205 | **DEAD** |
| `repo_populator.py` | 241 | **DEAD** |
| `verify_runner.py` | 89 | **DEAD** |

The four runners (645 LOC) are reachable from *nothing*. The four builders (701 LOC) are green-but-orphaned — kept alive only by passing unit tests, with no production caller. The package's continued existence also **inflates the apparent importance of `analyze/corpus_manifest.py`**, since `migrate/` is its only external consumer of `ManifestRecord`.

**Recommendation:** delete `migrate/` and its four tests, or move it to `~/projects/archive/`. Deleting it breaks no live path. Keeping ~1,346 lines of untraceable code is the opposite of "easy for a third party to understand."

### 4.2 `normalize/page_bridge_pure.py` — F7, parked half-finished (🟠)

Fully implemented and tested, but **not wired into `normalize_body()`**. Its documented dependency (`pdf_reader.py`) does not exist, and the `*.toc.yaml` sidecars it references are never written. `ClassifyResult.page_bridge` is computed but never consumed. It currently reads as *accidentally omitted* rather than *deliberately deferred*. Either implement and wire F7, or move it behind an explicit "F7 — deferred, see spec §13 #2" marker with a one-line skip comment in `normalize_body` where F7 would sit (the F-sequence otherwise jumps F6 → F8 → F9 with no explanation).

### 4.3 Stale scripts pointing at non-existent paths (🟡)

`add_toc_image_md.py`, `test_ackq_images.py`, and `extract_monograph.py` read/write `markdown-image/` or `markdown/` — directory names that predate the canonical `md-img/` layout. They are stale leftovers. `test_ackq_images.py` is additionally a **misnamed stray**: it lives in `scripts/`, is `test_`-prefixed (so pytest will try to collect it), but contains no tests — just an imperative Docling spike with `print()`s. Rename (drop `test_` prefix) or delete.

### 4.4 Stale documentation claims (🟡)

- `src/vista_docs/README.md:34` calls `classify/` "reserved — not yet active." **It is live**: `classify/rules.py` is called by `manifest/builder.py:69` to set `doc_type`, which the CLI uses on every `fetch`. Fix the description; do not remove the package.
- `scripts/README.md` contradicts itself: its header says scripts here are "*not* part of the automated pipeline," yet lists `enrich_inventory.py` as "Active." Both cannot be true (see §5). It also omits `normalize_census.py` and `seed_package_master.py` entirely.

---

## 5. The hidden mandatory script (🔴)

**`scripts/enrich_inventory.py` (1448 lines) is a mandatory pipeline stage masquerading as an ad-hoc utility.**

- It is the *only* producer of `vdl_inventory_enriched.csv`.
- `vista-docs sync` **raises and aborts** if that CSV is missing (`main.py:266-267`).
- `vista-docs publish` loads it for app-name/section resolution (`main.py:625`, `publish/builder.py:215`), and `publish/runner.py` even emits a rel-path join key *specifically so this script can read it back* and add `github_md_url`.

So a fresh corpus build silently fails at `sync` unless the operator knows to hand-run a 1448-line script first — a script with **no CLI command, no Makefile target, no automated invocation, and no tests** (it lives outside `src/`, so it is exempt from the 95% gate). It also carries its *own third copy* of the mojibake fixer and doc-label tables.

**Recommendation:** promote it to a first-class stage — `vista-docs enrich-inventory` + `make enrich-inventory`, wired into the orchestrator *before* `sync`, with its pure transforms moved into `src/vista_docs/` under test. This is the clearest example of organizational drift creating a fragile, invisible dependency.

---

## 6. Naming collisions and inverted package grouping (🟠)

### 6.1 "manifest" means three unrelated things

1. **`src/vista_docs/manifest/`** — the SQLite **`pipeline.db` acquisition-state store** (`store.py`/`builder.py`/`operations.py`), with `ManifestEntry`. Pure bookkeeping.
2. **`analyze/corpus_manifest.py`** — builds **`corpus-manifest.json`**, a delivery-stage provenance index, with `ManifestRecord`. Nothing to do with SQLite.
3. **The `vista-docs manifest` CLI command** — invokes concept #2, *not* the package literally named `manifest/`.

A reader chasing the `manifest` command lands in `analyze/`, never in the `manifest/` package; and two near-homonym dataclasses (`ManifestEntry` vs `ManifestRecord`) are trivially conflated. **Recommendation:** rename the SQLite package `manifest/` → `state/` (it already owns `state/pipeline.db`), eliminating the collision; and rename one dataclass (e.g. `ManifestRecord` → `CorpusEntry`).

### 6.2 `analyze/` does two unrelated jobs, and `analyze/runner.py` is mis-named

`analyze/` mixes **read-only analysis** (`headings.py`, `lexicon.py`, `diff.py`) with **delivery transformation** (`consolidate.py`, `corpus_manifest.py` and their runners). These are different lifecycle phases. Meanwhile `survey/` — also pure analysis — is its own top-level package. So the layout is inverted: pure analysis is split across `survey/` *and* `analyze/`, while delivery logic is buried *inside* `analyze/`.

Also, `analyze/runner.py` is the *headings* runner, but its unqualified name implies it is the runner for the whole package (the siblings are correctly named `consolidation_runner.py`, `corpus_manifest_runner.py`).

**Recommendation:**
- Rename `analyze/runner.py` → `analyze/heading_runner.py` for symmetry.
- Split `analyze/`: keep analysis (`headings`/`lexicon`/`diff`/`heading_runner`) together (or fold into `survey/`); move delivery (`consolidate*`, `corpus_manifest*`) into a `consolidate/` package next to `normalize/`, `publish/`. This makes package layout match the documented stage order.

*(Note: `diff.py` and `lexicon.py` are NOT orphans — `diff` feeds `consolidate.py:405`, `lexicon` feeds the `headings` command. Both are live.)*

---

## 7. Duplication (🟠)

The "new stages bolted on" pattern produced repeated logic that will rot independently:

- **Three separate mojibake fixers / doc-label tables**: in `pipeline/audit_frontmatter.py`, `scripts/enrich_inventory.py`, and `src/vista_docs/enrich/`. A cp1252 fix applied in one will silently diverge from the others.
- **Three independent mtime-cache implementations**: the exact idiom `if rp in prior and abs(mtime - prior[rp]) < 1.0: skip` is copy-pasted across `audit_frontmatter.py:941`, `chunk_sections.py:211`, `extract_entities.py:377`, each with its own near-identical `*_mtimes` table and loader.
- **Copy-pasted DB-exists guard** (identical message) in `chunk_sections.py:189`, `extract_entities.py:357`, `apply_quality_views.py:172`.
- **`strip_frontmatter()` + `FM_RE`/`DUP_FM_RE`** reimplemented in chunk + entities; a richer parser again in audit.
- **Coverage-view SQL template** (`SELECT x, COUNT(DISTINCT doc_id) … JOIN documents USING(doc_id)`) repeated ~10× across the 6.x scripts.
- **Hardcoded absolute paths** (`/home/rafael/data/vista-docs/...`) duplicated across all four `pipeline/` scripts instead of importing `vista_docs.config` — these will break for any other user or path.

A shared `pipeline/_common.py` (config-derived paths, db helper, frontmatter split, incremental-walk helper, the missing-input guard) removes ~100–150 lines and the divergent hardcoded paths in one move.

---

## 8. `audit_frontmatter.py` is a 979-line god-script (🟠)

It bundles ≥7 independently-testable responsibilities: mojibake repair, frontmatter parse/unparse + key ordering, entity extraction (file numbers / security keys / menu options), description+audience synthesis, a 190-line per-file orchestrator, SQLite schema+upsert, and reporting. Several of these are *parallel reimplementations* of logic in `enrich/` and `enrich_inventory.py`. Because it lives outside `src/`, none of it is unit-tested. Decompose: move the pure pieces into tested `src/vista_docs/` modules, leave a thin I/O driver.

---

## 9. Stage numbering is incoherent (🟡)

The docs number stages `1, 2, 3, 4, 5, 5+ (survey), 5+ (headings), 6, 6.5, 6.6, 6.7, 8, 9, 9.5, 10, 10+, 11`. **There is no stage 7**, two stages share "5+", and there is a gap from 6.7 to 8. This is harmless to execution but is friction for a new reader trying to build a mental model, and it reflects the same bolt-on history. Renumber as a clean linear sequence (or drop numbers and rely on names + a DAG) once the packages are reorganized.

---

## 10. Smaller code-smell items (🟡)

- `__import__("pathlib").Path(output)` appears at `main.py:306` and `main.py:352` — an ugly inline import inconsistent with every other command, which does `import pathlib` normally.
- The CLI module docstring (`main.py:8-9`) says `survey`/`headings` write to `state.db`; they actually write files to `SURVEY_DIR`. The docstring also omits `sync` and `normalize` from its command list.
- `manifest` and `consolidate` commands don't preflight their inputs even though `publish`/`push` (their consumers) do — the check is in the wrong place; it should be at the producer.

---

## 11. What is genuinely good (keep it)

So the refactor doesn't throw out the strengths:

- **`normalize/` is exemplary**: a clean orchestrator (`normalize_body`) sequencing 12 side-effect-free `*_pure` modules, all I/O confined to `io.py`/`runner.py`, every stage with inline `# F4 …` comments that explain *why ordering matters*. A third party can follow it. Use this as the template for the rest of the codebase.
- **The publish/push validation gate** (`_run_validation_gate`) is the right durable-safety pattern — generalize it, don't replace it.
- **Test discipline** is real: pure logic has unit tests, I/O is integration-tested and coverage-omitted deliberately.
- **The prose docs** (`vdl-arch-overview.md` with Mermaid + stage table, `src/vista_docs/README.md`) are better than most projects ever get. The problem is drift between docs and code, not absence of docs.
- **Good reuse where it counts**: `corpus_manifest_runner` reuses `consolidate.py`'s grouping rather than reimplementing it.

---

## 12. Recommended refactor plan (priority order)

**Phase A — make it runnable and honest (addresses your core ask):**
1. Implement the `pipeline` orchestrator for real, covering *all* stages (including 6–6.7, normalize, and enrich-inventory). Have it run each stage's preflight → work → postflight and stop on first hard failure. 🔴
2. Add a uniform **preflight** helper (required-input check with a `Run: vista-docs <prev>` hint) and a uniform **postflight** completion stamp (`stage_runs` table or `state/<stage>.done.json`) consumed by the next stage's preflight. 🔴
3. Promote `enrich_inventory.py` to `vista-docs enrich-inventory` + Makefile target, wired before `sync`. 🔴
4. Add the missing `normalize` Makefile target; make `publish` *warn loudly* (not silently fall back) when `normalized/` is absent. 🔴

**Phase B — remove dead weight:**
5. Delete or archive `migrate/` (+ its 4 tests). 🟠
6. Resolve F7/`page_bridge`: wire it or explicitly mark deferred. 🟠
7. Delete/rename stale scripts (`add_toc_image_md`, `test_ackq_images`, `extract_monograph`) and the misnamed test. 🟡

**Phase C — fix the naming/structure traps:**
8. Rename `manifest/` package → `state/`; rename `ManifestRecord` → `CorpusEntry`. 🟠
9. Rename `analyze/runner.py` → `analyze/heading_runner.py`; split `analyze/` into analysis vs delivery (`consolidate/`). 🟠
10. Fold the 6–6.7 scripts into the CLR/CLI as subcommands (or one `build-db`), using `vista_docs.config` paths, with pure logic moved into tested `src/` modules. 🟠

**Phase D — de-duplicate and polish:**
11. Extract `pipeline/_common.py`; unify the three mojibake fixers and three mtime caches. 🟠
12. Decompose `audit_frontmatter.py`. 🟠
13. Fix stale docstrings/READMEs, the `__import__("pathlib")` smell, the `classify` "not active" claim, and renumber stages. 🟡

---

## 13. Answering your exact questions

- **Orphan/redundant/confusing code?** Yes on all three: `migrate/` (orphan, ~1.3k LOC), three duplicated mojibake/mtime implementations (redundant), and the triple "manifest" naming + a stub `pipeline` command + a hidden-mandatory 1448-line script (confusing).
- **Logically coherent / modular / separation of concerns now that new phases exist?** Partially. Module-level separation is excellent in `normalize/` and decent elsewhere, but the *package grouping* is inverted (`analyze/` mixes analysis and delivery; `survey/` is a stray peer) and the *execution model* is fragmented across CLI / loose scripts / hand-run script.
- **Does each phase preflight the prior stage and postflight its own output?** **No.** Preflight is inconsistent (explicit / silent / none) and shallow where present (file-exists, not stage-complete); postflight exists only for normalize and publish/push. This is the top thing to fix.
- **Self-documenting?** The code reads well at the function level and the prose docs are strong, but the system is *not* self-documenting end-to-end: the entry point lies, a mandatory stage is undocumented-as-mandatory, and docs have drifted from code.
- **Needs refactor?** **Yes — a targeted structural refactor, not a rewrite.** The logic is worth keeping; the orchestration, gating, packaging, and dead-code cleanup are not yet at the "easy to maintain in six months / easy for a stranger to understand" bar. Phases A–B above get you most of the way; C–D get you all the way.

---

# Appendix A — The Stage Contract (design specification)

This appendix specifies the concrete stage abstraction that Phase A (§12) is built on:
every pipeline stage becomes **idempotent, self-contained, and bounded by a declared
contract with a preflight and a postflight**. It is written to be implementable as-is.

The code shapes below are *specification*, not an implementation — they define the
interface and the on-disk schema, not the pipeline logic itself.

## A.0 Decision record — why this shape (the four governing principles)

These four points were agreed before the spec was written and are recorded here so the
reasoning behind every design choice below is traceable.

1. **The contract is a *declared object*, not two functions bolted onto each stage.**
   The leverage is not "every stage has a preflight" — it is *one* `Stage` abstraction
   that every stage conforms to, so the orchestrator is generic and the dependency graph
   is explicit and inspectable. The current divergence (three preflight idioms: explicit
   file-check / silent DB query / nothing) exists precisely *because* each stage
   hand-rolls its own checks. A shared contract type makes uniform gating a property the
   architecture enforces, not a convention we hope holds. The existing
   `_run_validation_gate` is the postflight prototype — we generalize it, not reinvent it
   per stage.

2. **Postflight emits the exact signal preflight consumes — one notion of "done".**
   If stage *N*'s postflight and stage *N+1*'s preflight independently define
   "complete," they drift. Instead, postflight writes a **completion record** (status +
   counts + timestamps + input/output fingerprints), and the next stage's preflight reads
   *that record* plus a cheap re-validation. This directly fixes the observed bug where
   6.5/6.6/6.7 preflight on *"does `frontmatter.db` exist"* — true the instant stage 6
   runs once — and therefore silently run against a **stale or partial** DB. A
   fingerprint in the completion record makes "my input changed since upstream blessed
   it" detectable, which is also exactly what skip-if-unchanged idempotency needs.

3. **"Idempotent" is the weak word — the strong form is *immutable input tree →
   owned output tree, atomically committed*.** Idempotency is hard to guarantee for
   stages that mutate files **in place** (`enrich`, `sync`, `audit_frontmatter` all
   rewrite `md-img/`): it then depends on every transform being a true fixed point (the
   mojibake fixers and YAML re-serialization are *not* obviously fixed points), there is
   no rollback or change-diff, and a crashed run leaves a half-mutated tree that
   preflight cannot distinguish from a complete one. `normalize/` already shows the right
   pattern (`consolidated/` → `normalized/`, never mutating its input). A stage should be
   a transform from a read-only input artifact to its own output artifact, re-runnable to
   byte-identical output, committed atomically (write to temp, swap on success). The
   in-place mutators (`enrich`, `sync`, `audit`) are the thing to remove — and the
   measured storage math (§A.5) shows this is not only correct but *cheap*: the corpus is
   90%+ binary assets, so versioning the text at every stage costs ≈1 G total, while
   de-duplicating the assets the pipeline currently triplicates *saves* ≈4 G. Immutable
   per-stage text trees are therefore the model **from the start**, not a deferred
   "hardening" — see §A.5 for the two-storage-class design.

4. **"Self-contained" means self-contained at the *boundary*, not the
   *implementation*.** A stage declares its inputs/outputs and reaches into nothing
   else's internals — but it must **not** own a private copy of shared logic. That is how
   the codebase grew three mojibake fixers and three mtime-cache implementations.
   Self-contained *interface*, shared *libraries*. This principle is a guardrail against
   the contract refactor accidentally sanctifying the existing duplication.

**Scope caveat (also on the record):** this contract solves *orchestration and gating*.
It is orthogonal to the *organization* problems (the triple "manifest" naming, dead
`migrate/`, inverted `analyze/` grouping, hidden-mandatory `enrich_inventory.py`). Both
must be done; neither subsumes the other. And on **grain**: define stages at the level of
an artifact a human would name and reason about — do not split one-per-function. 6/6.5/
6.6/6.7 are the right grain; resist finer.

## A.1 The two core types

### `ArtifactContract` — one declared input or output

```
ArtifactContract:
    key:         str          # stable id, e.g. "md-img", "frontmatter.db:documents"
    kind:        Kind         # FILE | TREE | SQLITE_TABLE | SQLITE_VIEW | GIT_REMOTE
    locator():   -> Resolved  # resolves path/(db,table) FROM vista_docs.config — never hardcoded
    produced_by: str | None   # the Stage.name that emits this, or None if external (VDL/raw)
    min_count:   int          # smallest cardinality that counts as "non-empty" (default 1)

    validate()    -> CheckResult       # (ok: bool, count: int, problems: list[str])
    fingerprint() -> str               # cheap content signature (see A.4)
```

`validate()` answers *"does this artifact exist and is it structurally usable?"* —
existence **plus** minimal structural validity **plus** the `min_count` floor. It is
deliberately shallow (it is a gate, not a linter); deep validation is a stage's own
postflight gate (e.g. the frontmatter schema check), not the artifact contract.

### `Stage` — the unit of work

```
Stage:
    name:          str         # slug; identical in CLI subcommand, Makefile target, completion record
    description:   str         # one line
    requires:      list[ArtifactContract]   # inputs that must exist & be valid & up-to-date
    produces:      list[ArtifactContract]   # outputs guaranteed on success
    idempotency:   SKIP_IF_UNCHANGED | ALWAYS_RERUN | FORCE_ONLY
    contract_ver:  int         # bump when produces[] shape changes (invalidates downstream)

    preflight(ctx, force) -> PreflightResult   # PROCEED | SKIP | FAIL(reason, remediation)
    run(ctx, force)       -> RunResult         # the work; atomic commit; returns counts
    postflight(ctx, run)  -> PostflightResult  # validate produces[]; on success write completion record
```

A stage exposes exactly this. The CLI subcommand and the orchestrator both drive stages
through the same `preflight → run → postflight` sequence; there is no second code path.

## A.2 The completion record — the "done" signal (principle #2)

Postflight writes one row per (stage, pkg-scope). Lives in `state/pipeline.db` (the
existing acquire/state DB — recommended over a third store; see §6.1 rename). This table
*is* the inter-stage contract surface.

```sql
CREATE TABLE IF NOT EXISTS stage_runs (
    stage            TEXT NOT NULL,          -- Stage.name
    pkg              TEXT NOT NULL DEFAULT '',-- '' = whole corpus, else app_code scope
    status           TEXT NOT NULL,          -- 'ok' | 'failed' | 'partial'
    started_at       TEXT NOT NULL,          -- ISO-8601
    finished_at      TEXT NOT NULL,          -- ISO-8601
    inputs_fp        TEXT NOT NULL,          -- JSON {artifact_key: fingerprint} actually consumed
    outputs_fp       TEXT NOT NULL,          -- JSON {artifact_key: fingerprint} produced
    counts           TEXT NOT NULL,          -- JSON {processed, skipped, errors, ...}
    contract_ver     INTEGER NOT NULL,       -- Stage.contract_ver at run time
    tool_ver         TEXT NOT NULL,          -- vista_docs.__version__ (+ normalize_version etc.)
    PRIMARY KEY (stage, pkg)
);
```

The **only** way a row reaches `status='ok'` is by passing postflight. That is the
mechanism by which "the next stage knows it is ok to run": the next preflight refuses
unless its upstreams have `status='ok'` with a compatible `contract_ver` and matching
fingerprints.

## A.3 Preflight and postflight algorithms (precise)

### `preflight(S, force)`

```
1. For each input contract C in S.requires:
   a. r = C.validate()
      if not r.ok:  FAIL(reason=r.problems,
                         remediation = "Run: vista-docs " + (C.produced_by or "<external>"))
   b. If C.produced_by is an internal stage U:
        rec = stage_runs[U, pkg]
        if rec is None or rec.status != 'ok':   FAIL("upstream {U} not complete", "Run: vista-docs "+U)
        if rec.contract_ver incompatible with S's expectation: FAIL("contract drift; rebuild "+U)
        if C.fingerprint() != rec.outputs_fp[C.key]:
            FAIL("{C.key} changed since {U} produced it (hand-edit or partial write); re-run "+U)
            # may be downgraded to WARN behind --allow-stale

2. Decide skip (idempotency):
   if not force and S.idempotency == SKIP_IF_UNCHANGED:
       mine = stage_runs[S, pkg]
       if mine and mine.status=='ok'
          and mine.inputs_fp == {C.key: C.fingerprint() for C in S.requires}
          and all(C.validate().ok for C in S.produces):
              return SKIP   # nothing upstream changed and my outputs still valid

3. return PROCEED
```

Step 1b is the fix for the stale/partial-DB class of bug: presence is necessary but the
fingerprint match against the upstream's *recorded* output is what proves currency.

### `postflight(S, run_result)`

```
1. problems = []
   for each output contract C in S.produces:
       r = C.validate();  if not r.ok: problems += r.problems
2. Run stage-specific deep gate if any (e.g. validate's FM schema gate, normalize §11).
3. if problems or gate failed:
       write stage_runs[S] = status='failed', counts, timestamps   # do NOT bless
       RAISE   # next stage's preflight will refuse on status != 'ok'
   else:
       write stage_runs[S] = status='ok',
             inputs_fp  = {C.key: C.fingerprint() for C in S.requires},
             outputs_fp = {C.key: C.fingerprint() for C in S.produces},
             counts, started/finished, contract_ver, tool_ver
```

### Where each check lives (producer vs consumer)

- **Output validity** is asserted by the **producer's postflight** (it knows what
  "good" means for its outputs). The consumer does **not** re-deep-validate upstream
  output — it trusts `status='ok'` + cheap `validate()` + fingerprint match.
- **Input presence/compatibility/currency** is asserted by the **consumer's preflight**.

This split is deliberate: it removes the temptation to duplicate the frontmatter/normalize
gates in every downstream stage.

## A.4 Fingerprints (principle #2/#3 — cheap by default, strong on demand)

| Kind | Cheap fingerprint (default) | Strong fingerprint (`--verify`) |
|---|---|---|
| `TREE` text (ingested…audited, consolidated, normalized, publish) | sha256 of sorted `(relpath, size, mtime_ns)` lines | sha256 of sorted `(relpath, sha256(bytes))` |
| `TREE` asset store (`assets`, `raw`) — write-once | `(file_count, manifest_hash)`; sealed once written, never re-hashed | sha256 over sorted content hashes |
| `FILE` (inventory csv/json, corpus-manifest.json, survey/*) | `(size, mtime_ns)` digest | sha256 of contents |
| `SQLITE_TABLE` | `(row_count, max(rowid), schema_sql_hash)` | sha256 over ordered row digest |
| `SQLITE_VIEW` | `(row_count, definition_hash)` | sha256 over ordered row digest |
| `GIT_REMOTE` | last-pushed commit sha | — |

The cheap form is what makes `SKIP_IF_UNCHANGED` fast; the strong form is for a paranoid
`--verify` run or CI. Per-file mtime caches inside stages (the three current
implementations) become an *internal* optimization behind the stage's `run()` — the
**stage-grain** fingerprint in `stage_runs` is the contract-level signal, and the
per-file caches should be unified into one shared helper (principle #4).

## A.5 Storage model: two classes, and the artifact registry

**Decision (grounded in measured storage, 2026-06-01).** The corpus is dominated by
binary assets, not text. Versioning the text per stage is therefore essentially free, and
the current pipeline already pays a *larger* cost duplicating the assets it should be
sharing:

| layer | total | markdown text | images |
|---|---|---|---|
| `raw/` | 3.6 G | — | 3.6 G (docx/pdf) |
| `md-img/` | 3.0 G | **239 M** | 2.8 G |
| `consolidated/` | 1.8 G | **45 M** | ~1.75 G |
| `publish/` | 2.3 G | (subset) | ~2.25 G |
| `normalized/` | 46 M | **44 M** | ~0 |

Images are copied ~3× today (`md-img` → `consolidated` → `publish` ≈ **~6.8 G** of largely
duplicate bytes), while the text — the only thing the mutating stages change — is
destructively overwritten in place. The storage strategy is inverted. The fix splits
every artifact into one of two classes:

1. **Write-once asset store** — `raw/` (docx/pdf) and a **content-addressed image store**
   (`assets/<sha256>.<ext>`). Written once at fetch/ingest, never mutated or copied again;
   markdown references assets by hash. De-duplicating the image triplication cuts the image
   footprint from ~6.8 G to ~2.8 G (**~4 G saved**).
2. **Versioned text artifacts** — markdown + frontmatter + `*.history.yaml` sidecars. Each
   mutating stage writes a **new immutable tree** instead of overwriting its input. The
   whole text history (ingested → enriched → synced → audited → consolidated → normalized)
   is ≈ **1 G total** — kept forever, cheaply.

Net: full per-stage text history *and* a net storage reduction. This makes principle #3
structural (idempotency is provable by diffing trees; rollback is a tree swap) and it
**eliminates the `@version` hack** — each stage now owns a genuinely distinct artifact at a
distinct path, not the same `MD_IMG_DIR` distinguished only by fingerprint. Two new config
constants back the text/asset split: `TEXT_DIR` (versioned text trees) and `ASSETS_DIR`
(content-addressed store).

Every artifact in the pipeline, with its kind, storage class, where it resolves (always via
`vista_docs.config`), and which stage owns it:

| key | kind | class | locator (from config) | produced_by |
|---|---|---|---|---|
| `vdl` (website) | external | — | `VDL_BASE` | — |
| `inventory.csv` | FILE | text | `INVENTORY_DIR/vdl_inventory.csv` | crawl |
| `inventory.json` | FILE | text | `INVENTORY_DIR/vdl_inventory.json` | crawl |
| `inventory.enriched.csv` | FILE | text | `INVENTORY_DIR/vdl_inventory_enriched.csv` | **enrich-inventory** (§5) |
| `raw` | TREE | **asset (write-once)** | `RAW_DIR/{app}/*.docx·pdf` | fetch |
| `pipeline.db:manifest@fetch` | SQLITE_TABLE | state | `(DB_PATH,"manifest" where fetch_status='ok')` | fetch |
| `assets` | TREE (CAS) | **asset (write-once)** | `ASSETS_DIR/<sha256>.<ext>` | ingest |
| `pipeline.db:manifest@ingest` | SQLITE_TABLE | state | `(DB_PATH,"manifest" where ingest_status='ok')` | ingest |
| `text/ingested` | TREE | **text (versioned)** | `TEXT_DIR/01-ingested/{app}/*.md` | ingest |
| `text/enriched` | TREE | **text (versioned)** | `TEXT_DIR/02-enriched/` | enrich |
| `text/synced` | TREE | **text (versioned)** | `TEXT_DIR/03-synced/` | sync |
| `text/audited` | TREE | **text (versioned)** | `TEXT_DIR/04-audited/` | audit (6) |
| `frontmatter.db:documents` | SQLITE_TABLE | state | `(FM_DB,"documents")` | audit (6) |
| `frontmatter.db:doc_sections` | SQLITE_TABLE | state | `(FM_DB,"doc_sections")` | chunk (6.5) |
| `frontmatter.db:doc_routines…codes` | SQLITE_TABLE | state | `(FM_DB, entity tables)` | entities (6.6) |
| `frontmatter.db:v_doc_enriched` | SQLITE_VIEW | state | `(FM_DB,"v_doc_enriched")` | quality (6.7) |
| `survey` | TREE/FILE | text | `SURVEY_DIR/survey-*.csv·json` | survey |
| `survey/heading_analysis` | TREE | text | `SURVEY_DIR/heading_analysis/` | headings |
| `consolidated` | TREE | **text (versioned)** | `DATA_DIR/consolidated/{app}/{type}/*.md` (images by `assets` ref) | consolidate |
| `corpus-manifest.json` | FILE | text | `DATA_DIR/migration/corpus-manifest.json` | manifest |
| `normalized` | TREE | **text (versioned)** | `DATA_DIR/normalized/{app}/{type}/*.md` (+`*.history.yaml`) | normalize |
| `publish` | TREE | text + materialized assets | `DATA_DIR/publish/{section}/{pkg}/*.md` (+INDEX.md; images materialized from `assets`, gitignored) | publish |
| `git:vistadocs/vdl` | GIT_REMOTE | — | `VDL_REMOTE` | push |

**Notes.**
- The text trees (`01-ingested` … `04-audited`) replace the three in-place mutations of
  `MD_IMG_DIR`. Each is a complete, immutable markdown tree; downstream stages read the
  latest one named in their contract. `diff 02-enriched 03-synced` shows exactly what `sync`
  did — the central debugging win, impossible under in-place mutation.
- Images are written **once** to the content-addressed `assets` store at ingest.
  `consolidated` and `normalized` carry only markdown and reference assets by hash; `publish`
  is the *only* place images are materialized into a browsable layout, and those copies are
  gitignored and regenerable — a publish-local convenience, not pipeline duplication.
- Retention: keep all text versions (≈1 G); never auto-prune (that defeats rollback). Offer
  an explicit `gc` to drop intermediate text trees older than N runs if ever desired.
- Implementation choice for the text layer: **plain materialized trees** (recommended —
  simplest, zero new deps) or a **git-backed text layer** (free dedup/diff/history; aligns
  with the existing `publish/.gitignore` that already keeps images out of git). Start with
  plain trees; adopt git only if you want the history UX.

## A.6 Per-stage contract table (requires → produces)

| Stage | requires | produces | idempotency |
|---|---|---|---|
| crawl | `vdl` (external) | `inventory.csv`, `inventory.json` | FORCE_ONLY (network) |
| enrich-inventory | `inventory.csv` | `inventory.enriched.csv` | SKIP_IF_UNCHANGED |
| fetch | `inventory.csv` | `raw`, `pipeline.db:manifest@fetch` | SKIP_IF_UNCHANGED |
| ingest | `raw`, `pipeline.db:manifest@fetch` | `text/ingested`, `assets`, `pipeline.db:manifest@ingest` | SKIP_IF_UNCHANGED |
| enrich | `text/ingested` | `text/enriched` | SKIP_IF_UNCHANGED |
| sync | `text/enriched`, `inventory.enriched.csv` | `text/synced` | SKIP_IF_UNCHANGED |
| audit (6) | `text/synced` | `text/audited`, `frontmatter.db:documents` | SKIP_IF_UNCHANGED |
| chunk (6.5) | `text/audited`, `frontmatter.db:documents` | `frontmatter.db:doc_sections` | SKIP_IF_UNCHANGED |
| entities (6.6) | `text/audited`, `frontmatter.db:documents` | `frontmatter.db:doc_routines…codes` | SKIP_IF_UNCHANGED |
| quality (6.7) | `frontmatter.db:doc_sections`, `frontmatter.db:documents` | `frontmatter.db:v_doc_enriched` (+is_latest, quality_score) | ALWAYS_RERUN (pure SQL) |
| survey | `text/audited` | `survey` | SKIP_IF_UNCHANGED |
| headings | `text/audited` | `survey/heading_analysis` | SKIP_IF_UNCHANGED |
| consolidate | `text/audited`, `assets` | `consolidated` | SKIP_IF_UNCHANGED |
| manifest | `consolidated`, `text/audited` | `corpus-manifest.json` | SKIP_IF_UNCHANGED |
| normalize | `consolidated`, `raw` | `normalized` | SKIP_IF_UNCHANGED |
| publish | `corpus-manifest.json`, `normalized`*, `consolidated`, `assets`, `inventory.enriched.csv` | `publish` | SKIP_IF_UNCHANGED |
| validate | `publish`, `normalized` | (gate only — no artifact; sets its own `ok`) | ALWAYS_RERUN |
| push | `publish` (+ validate `ok`) | `git:vistadocs/vdl` | FORCE_ONLY |

\* `normalized` is a *soft* require for publish: absent → publish proceeds on
`consolidated` but **must warn loudly** (today it falls back silently — §2). Encode this
as `requires` with an `optional=True` flag that downgrades a missing-input FAIL to a
prominent WARN, so the contract records which body source was used.

This table **is** the pipeline DAG. The orchestrator topologically sorts it; there is no
separate hand-maintained stage list to drift (the current stub's `["crawl","fetch",
"ingest","survey"]` is exactly such a drifted list).

## A.7 Two worked examples

**chunk (6.5) — fixes the stale-DB bug.** `requires = [frontmatter.db:documents,
text/audited]`. Preflight: `documents.validate()` requires the table exists *and*
`row_count ≥ 1`; then it reads `stage_runs['audit']`, requires `status='ok'`, and checks
`fingerprint(documents) == stage_runs['audit'].outputs_fp['frontmatter.db:documents']`.
If audit was re-run on a larger corpus but 6.5 was not, the fingerprints differ →
preflight FAILs with *"documents changed since audit produced it; re-run chunk"* instead
of today's silent partial index. Postflight: `doc_sections.validate()` requires
`row_count ≥ 1`; on success records `outputs_fp['frontmatter.db:doc_sections']`.

**normalize — already 90% conformant.** `requires=[consolidated, raw]`,
`produces=[normalized]`. Its existing §11 validation is lifted verbatim into postflight
(principle #1: generalize, don't reinvent). It already reads an immutable input and writes
a distinct output tree (principle #3) — the only addition is writing the `stage_runs`
completion record so `publish`'s preflight can confirm currency rather than just checking
`normalized/` exists.

## A.8 Adoption path (low-risk, incremental)

1. **Land the plumbing first, behavior-neutral:** add the `stage_runs` table, the
   `ArtifactContract`/`Stage` types, and a shared fingerprint/validate helper library
   (this is also where the unified mojibake fixer and mtime-cache live — principle #4).
2. **Wrap, don't rewrite:** each existing runner becomes a `Stage.run()`; populate
   `requires`/`produces` from §A.6. Existing logic is untouched. Preflight/postflight
   start in **warn-only** mode (log mismatches, don't fail) so you can observe the
   fingerprint signals against the real corpus before enforcing.
3. **Flip to enforcing** stage by stage once warn-mode is quiet.
4. **Build the real orchestrator** on the §A.6 DAG; delete the `pipeline` stub and the
   hand-maintained stage list. Replace `make pipeline` to call it; add the missing
   `normalize` and 6.x targets.
5. **Adopt the two-storage-class model early (§A.5) — alongside step 2, not last.** The
   storage math makes it cheap (~1 G to version all text; ~4 G *saved* by de-duplicating
   images) and it *simplifies* the contract by removing the `@version` hack. Concretely:
   stand up the content-addressed `assets` store at ingest, and give enrich/sync/audit
   their own `text/NN-*` output trees instead of mutating `MD_IMG_DIR`. Each stage then
   commits atomically (write tree to temp, swap on success) and idempotency becomes
   verifiable by diffing consecutive trees.

Steps 1–4 deliver the idempotent, contract-bounded, preflight/postflight pipeline you
asked for without a rewrite. Step 5 is **not** deferred hardening: because the corpus is
90%+ binary assets, removing the three in-place mutators is cheap and *nets a storage
reduction*, so fold it in alongside the wrap step (2) rather than treating it as a later
phase. Together they make idempotency and rollback structural rather than best-effort.
