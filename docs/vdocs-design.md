# vdocs — Pipeline Design Document

**Status:** Founding design (greenfield rewrite). **Date:** 2026-06-01.
**Supersedes:** the v1 implementation in this repo (kept for *reference only* — see §16).
**Audience:** the implementer(s) of the new repo, and any third-party author who must
understand the whole system from cold.

**Naming convention:** the project, git repository, Python import package, and CLI are all
**`vdocs`** (repo `vdocs`, `import vdocs`, `vdocs <command>`). This is the v2 rewrite that
replaces the legacy **`vista-docs`** codebase; the short unified name keeps repo, package,
and command identical so there is nothing to drift. (The published *corpus* repo
[`vistadocs/vdl`] and the separate downstream API repo are unaffected by this rename.)

This document is the single source of architectural truth for the rewrite. It is written
to be read top-to-bottom by someone who has never seen the project. Every non-obvious
choice is an explicit decision with rationale (the ADR tables in §10). If the code and
this document disagree, the document is the bug report.

---

## 1. Purpose and scope

`vdocs` turns the **VA VistA Document Library (VDL)** — a sprawling website of
DOCX/PDF technical manuals — into two co-equal deliverables:

1. a **clean, human-browsable markdown corpus published on GitHub** (docs-as-code), and
2. a **maximally machine-discoverable knowledge base** exposed through an **MCP server**
   that provides **structured, computable, semantic search** across the entire corpus.

It is an **ETL/document-modernization pipeline**: acquire → conform → curate → **serve**.

There are exactly **two classes of consumer**, and the entire architecture is shaped by
serving both without compromising either:

1. **Humans** browsing GitHub — want *whole, readable markdown documents* with stable
   diffs and history.
2. **Machines / LLM agents** via the MCP endpoint — want *atomic, addressable, computable
   units* (sections, entities, codes, cross-references, version lineage) retrievable by
   **meaning (semantic), keyword (lexical), field (structured), and relationship (graph)** —
   combined.

The central architectural decision (§6) follows directly: **keep documents whole as the
source of truth; derive every machine view — index, embeddings, knowledge graph — from
them.** We never force one consumer's storage model onto the other, and every machine view
is always rebuildable from the source.

Machine-discoverability is a **primary goal**, not an afterthought: every retrievable unit
has a stable, durable identifier; every unit carries structured metadata for filtering; and
the corpus ships a machine-readable discovery descriptor (§14).

**Git-native version history is a primary goal.** VDL documents are dominated by *manual*
version control — revision-history tables, patch-history matrices, "change pages," per-section
"(Patch NN)" annotations — that clutter the prose and force a reader to mentally filter decades
of bookkeeping to reach the actual content. A truly **GitHub-native** migration moves that
burden where it belongs: out of the prose and into **structured lineage that git can carry
natively**. Every logical document collapses to **one anchor document** — a single living
markdown file at a version-free path — whose body is *current content only*; the manual revision
apparatus is stripped out and the full patch/version lineage is **captured in sidecar files that
travel with the anchor document** (`history.yaml` + the retained prior-version bodies, §6.4/§6.6).

We deliberately **do not** mechanically replay every patch as a git commit in this pass — that is
high-overhead bookkeeping for little immediate payoff. Instead the architecture **captures
everything needed to do it later**: a future, opt-in `push --replay-history` can reconstruct each
document's commit history (`git log`/`git blame`/`git diff`) entirely from the captured sidecars,
with no re-acquisition. This is what "rolling prior versions up under a consolidated document"
means here: the patch series collapses into one anchor document **plus a complete, machine-
structured lineage** — not N near-duplicate files each carrying its own embedded changelog.
Mechanism in §6.6; pipeline reflection in §8.

---

## 2. Design tenets

These are non-negotiable. Every later section is an application of one of these.

1. **One source of truth per fact.** A datum lives in exactly one place. Everything else
   is *derived* and rebuildable. No fact is copied into two stores "for convenience."
2. **Immutability of evidence.** Raw acquired documents and extracted binary assets are
   **write-once**. All cleaning is *derivation into a new artifact*, never edit-in-place.
3. **Every stage is a pure transform from declared inputs to declared outputs**, bounded
   by a **contract** (preflight + postflight), **idempotent**, and **self-contained at its
   boundary** (it declares what it touches and reaches into nothing else's internals).
4. **Self-contained ≠ self-implemented.** Shared logic lives in *one* shared library, not
   copied per stage. (This is the explicit antidote to v1's three mojibake fixers.)
5. **Split storage along axes of independent change, ownership, and consumption** — not
   "atomicity for its own sake" (§6).
6. **Derive structure, don't shred the source.** Whole files on disk; atomic units in the
   derived DB.
7. **Fail loud, never silently degrade.** A missing prerequisite or a broken output stops
   the pipeline with a remediation message — it never produces a quietly-degraded artifact.
8. **The pipeline is a declared graph, not a script.** The DAG is data; the orchestrator is
   generic; there is no hand-maintained stage list to drift.
9. **Self-documenting by construction.** Names say what things are; the package layout
   mirrors the pipeline; the contract table *is* the architecture diagram.
10. **Lineage is mandatory.** Every derived artifact records the source(s) and tool
    version it was produced from. You can always answer "where did this byte come from?"
11. **Machine-discoverability is a first-class output.** Every retrievable unit (document,
    section, entity) has a **stable, durable, re-run-invariant ID**; carries structured
    metadata for filtering; is reachable by hybrid search (semantic + lexical + structured +
    graph); and is exposed through a standard protocol (MCP). The corpus is *computable*,
    not merely published.
12. **Version history is captured lineage, not prose — and git-replayable later.** A document's
    patch/version lineage is stripped from the body and captured in sidecars that travel with the
    anchor document (`history.yaml` + the retained prior bodies) — never left as revision tables,
    change pages, or "(Patch NN)" annotations in the prose. The manual version-control apparatus
    is *evidence*, not content. Mechanical replay into git commit history is a deferred capability
    the capture *preserves*, not work this pass performs. (Mechanism: §6.6.)

### Non-goals

- Not a general document-management system or CCMS. Not DITA/S1000D authoring (§5.4).
- Not multi-tenant; single-node, single-maintainer scale (≈3–4 GB raw, ≈3k documents).
- Not a real-time service. It is a batch pipeline; the *API* (separate repo) is the service.
- No web authoring UI. Source edits, if any, are git PRs against the gold corpus.

---

## 3. What we are deliberately not repeating from v1

Recorded so the rewrite doesn't drift back. (Full analysis: `vista-docs-code-review.md`.)

- **No fictional orchestration.** v1's `pipeline` command was a `print()` stub; there was
  no single command that built the corpus. v2's orchestrator is the spine (§7–8).
- **No in-place mutation.** v1 rewrote `md-img/` in three stages, making idempotency
  un-provable and rollback impossible. v2 versions text per stage (§5).
- **No hidden mandatory scripts.** v1's 1448-line `enrich_inventory.py` was an undocumented
  hard dependency of `sync`/`publish`. v2 makes catalog enrichment a first-class stage (§8).
- **No god-scripts.** v1's 979-line `audit_frontmatter.py` did seven jobs. v2 decomposes
  into pure libraries + thin stage drivers.
- **No naming collisions.** v1 had three different "manifest" concepts. v2 names them
  `state.db`, `index.db`, and `corpus-manifest.json` (§5.5).
- **No duplicated logic.** v1 had three mojibake fixers, three mtime caches, three
  frontmatter parsers. v2 has a single shared kernel (§9.2).
- **No dead packages.** v1 carried ~1,350 LOC of unreachable `migrate/` code. v2 ships
  only what the DAG reaches; everything in the repo is live or a test.
- **No computed metadata baked into bodies.** This was the root cause of the in-place churn
  (§6.3).

---

## 4. Architecture at a glance — the medallion model

v2 is organized as a **medallion data lake** (bronze → silver → gold), the data-engineering
industry's standard frame for exactly this raw→curated progression. Each layer is a set of
**declared artifacts**; each arrow is a **stage** with a contract.

```
                          ┌──────────────── BRONZE (immutable evidence) ─────────────────┐
  VDL website ──crawl──►  catalog.raw ──catalog──►  catalog.enriched ──fetch──►  raw/ (docx·pdf, write-once)
                          └───────────────────────────────────────────────────────────────┘
                                                                                  │
                          ┌──────────── SILVER (conformed, per-doc, versioned text) ─────┐
                          │  convert ──►  text@converted  + assets/ (CAS images, write-once)
                          │  enrich  ──►  text@enriched    (identity frontmatter baked)
                          │  normalize ─►  text@normalized  + bundle sidecars (history, tables…)
                          └───────────────────────────────────────────────────────────────┘
                                                                                  │
                          ┌──────────── GOLD (curated, derived, computable) ─────────────┐
                          │  consolidate ─► consolidated/ (version groups)
                          │  index       ─► index.db (documents, sections+FTS5, entities, quality; stable IDs) ← derived shred
                          │  relate      ─► index.db:relations (doc↔entity, doc↔doc xref — knowledge graph)
                          │  embed       ─► vectors.db (per-chunk embeddings — semantic index)
                          │  manifest    ─► corpus-manifest.json + discovery.json (lineage + machine catalog)
                          │  publish     ─► publish/ (human tree, markdown-only)
                          │  validate    ─► HARD GATE (schema + lineage + anchors)
                          └───────────────────────────────────────────────────────────────┘
                                       │                                          │
            ┌──────── SERVE (read-only over gold) ─────────┐                      │
            │  push ─► github.com/vistadocs/vdl  (humans)  │◄─────────────────────┘
            │  mcp  ─► MCP endpoint (agents):              │
            │          hybrid search · fetch · entities ·  │◄── index.db + vectors.db + corpus bundles
            │          xref · lineage                      │
            └──────────────────────────────────────────────┘

  Orchestration state + lineage  ──►  state.db  (stage_runs, fingerprints)   [cross-cutting]
```

**Layer invariants:**

- **Bronze is immutable.** Once written, never modified. It is the audit trail and the
  re-derivation root. Content-addressed where it's binary.
- **Silver is per-document and versioned.** Each conforming stage writes a *new* immutable
  text tree; the previous one is retained. `diff text@enriched text@normalized` shows
  exactly what `normalize` did.
- **Gold is curated and consumer-shaped.** The DB is a *derived* projection (rebuildable
  from silver). The publish tree is the human deliverable. Nothing in gold is a source of
  truth that isn't reproducible from silver + bronze.

---

## 5. Storage model

### 5.1 Two storage classes (the foundational split)

Grounded in v1's measured corpus: it is **>90% binary assets**. Images were copied ~3×
(≈6.8 GB of duplicates) while the text that actually changes was overwritten in place. v2
inverts this:

| Class | What | Policy | Why |
|---|---|---|---|
| **Asset store** (write-once) | raw docx/pdf; extracted images | content-addressed (`<sha256>.<ext>`), never mutated or copied | dominates size; never changes; referenced by hash from text |
| **Versioned text** | markdown + frontmatter + structured sidecars | a new immutable tree per conforming stage; kept | tiny (≈1 GB for the *entire* history); diffable; rollback = tree swap |

Result: **full per-stage text history *and* a net storage reduction** (≈4 GB saved by
de-duplicating assets; ≈1 GB spent versioning all text).

### 5.2 The content bundle (per-document unit)

Each document is a **directory of typed parts** (the Hugo "page-bundle" / Jekyll-collection
pattern), not a mega-file and not scattered fragments. This keeps *related* things together
while separating *by lifecycle/type*:

```
<doc-slug>/
  body.md            # prose + small inline tables + figure refs; IDENTITY frontmatter baked in
  history.yaml       # version-lineage sidecar: ordered patch history + refs to retained prior bodies (machine-owned)
  tables/            # large data tables extracted to data sidecars
    field-listing.csv
    file-attributes.csv
  refs.yaml          # anchor/alias map + outbound link map (machine-owned)
  # images referenced by sha256 into the shared asset store — NOT copied here
  # computed metadata (word_count, quality_score, entities…) lives in index.db — NOT here
```

A bundle is the unit of versioning in silver. The `text@*` trees are trees *of bundles*.

### 5.3 Layer → directory map

```
$LAKE/                                   # DATA_DIR, default ~/data/vdocs, env-overridable
  bronze/
    catalog/raw.{csv,json}               # crawl
    catalog/enriched.{csv,json}          # catalog
    raw/<sha256>.<docx|pdf>              # fetch (content-addressed)
    raw/index.json                       # sha256 → (app_code, title, source_url) map
  assets/<sha256>.<ext>                  # convert (content-addressed image store)
  silver/
    text/01-converted/<app>/<slug>/...   # convert  (bundles)
    text/02-enriched/<app>/<slug>/...    # enrich
    text/03-normalized/<app>/<slug>/...  # normalize  (gold-quality bodies live here)
  gold/
    consolidated/<app>/<type>/...        # consolidate
    corpus-manifest.json                 # manifest (lineage)
    discovery.json                       # manifest (machine discovery descriptor — §14)
    glossary.md                          # normalize (single-sourced corpus glossary)
    publish/<section>/<pkg>/...          # publish (human tree; markdown-only, images materialized+gitignored)
  state.db                               # orchestration: stage_runs, fingerprints, lineage
  index.db                               # derived corpus index + knowledge graph (rebuildable)
  vectors.db                             # semantic index: per-chunk embeddings (rebuildable)
  reports/                               # analyze: survey, headings, lexicon (diagnostic, off critical path)
```

Numbered text trees (`01-`, `02-`, `03-`) make the silver progression self-evident on `ls`.

### 5.4 Why not shred the source into component files (DITA/S1000D)?

The domain (software technical manuals) is exactly where DITA/DocBook/**S1000D** and CCMS
systems live. We deliberately **reject source-shredding** because:

- **Reassembly tax + single point of failure.** A shredded corpus needs a build to produce
  anything readable; the assembly engine becomes the most fragile, least-contributable part.
- **Git works at document grain.** `diff`/`blame`/PR and "one file, one history" are *the*
  properties that make docs-as-code maintainable. Shredding destroys them.
- **One-way door.** Whole files → components is always derivable later; components →
  re-humanized prose is not. Keep the reversible option.
- **Both consumers are already served** by "whole bundle + derived DB." Shredding the
  *files* buys the API nothing the DB doesn't already give it.
- **Cost/benefit is wrong at our scale.** DITA/S1000D pay off with teams, conditional
  assembly, and CCMS tooling. A single maintainer would drown in the tooling.

The *good* form of shredding — semantic chunking for retrieval — is real and we do it, but
as a **derived artifact** (`index.db` §6.4), never as the storage format.

### 5.5 The derived stores (no naming collisions)

| Store | Role | Owner | Rebuildable? | Key contents |
|---|---|---|---|---|
| `state.db` | Orchestration + lineage | the orchestrator | no (it *is* the history) | `stage_runs`, artifact fingerprints, run lineage |
| `index.db` | Derived corpus index + knowledge graph | `index` + `relate` | **yes** (from silver) | `documents`, `doc_sections`+FTS5, entity tables, `relations` (graph edges), quality/is_latest, views; **stable IDs** on every unit |
| `vectors.db` | Semantic index | `embed` | **yes** (from `index.db` chunks) | per-chunk embeddings + ANN index (sqlite-vec), keyed by section stable ID; records embedding-model id+version |

The provenance JSON produced by `manifest` is `corpus-manifest.json` (plus the machine
**discovery descriptor** `discovery.json`, §14). Distinct things, distinct unambiguous names
— there is no type or package called "manifest." All derived stores are opened **read-only**
by the MCP server (§14).

**Stable identifiers (the machine-discoverability prerequisite).** Every document, section,
and entity has a deterministic ID that is invariant across re-runs — a document ID from its
identity (`app_code` + doc slug + version), a section ID from `doc_id` + heading-path slug,
an entity ID from `(type, canonical-name)`. IDs are **never** SQLite rowids. This single
contract is what lets the published markdown anchors, the vector index keys, the graph nodes,
and the MCP resource URIs all reference the *same* unit unambiguously — and lets a re-embed
or re-index reuse prior work instead of rebuilding from scratch.

---

## 6. Content model and document decomposition

### 6.1 The governing rule

Split two things into separate storage **iff** they differ on *change rate*, *ownership*,
or *consumer*. Otherwise keep them together (every seam is a reassembly cost and a sync
hazard).

### 6.2 Whole file as source; every machine view derived from it

The body bundle (`body.md`) is the durable, human-readable source of truth. **Every machine
view is derived from it and fully rebuildable:** the atomic/queryable index (sections,
entities, codes, version lineage, full-text → `index.db`); the **knowledge graph** (relations
between docs and entities → `index.db:relations`); and the **semantic index** (per-chunk
embeddings → `vectors.db`). We never fragment `body.md` — the *retrieval chunk* is the
derived section, not a file on disk. This is "derive, don't shred" (§5.4) applied to search:
shredding for retrieval happens only in the derived stores, never to the source.

### 6.3 Frontmatter is split by lifecycle (not "sidecar vs baked-in")

v1's mistake was treating all metadata uniformly, which forced constant body rewrites. v2
classifies every metadata field by lifecycle and routes it accordingly:

| Class | Examples | Storage | Rationale |
|---|---|---|---|
| **Identity / human-curated** | title, doc_type, app_code, section, pkg_ns, version, source provenance (the required keys) | **Baked into `body.md` frontmatter** | defines the document; stable; docs-as-code norm; atomic with the prose |
| **Computed / derived** | word_count, page_count, quality_score, is_latest, keywords, extracted entities, stub flag | **`index.db` only — never in the body** | mechanically regenerated; baking it churns the body hash and guarantees staleness |
| **Heavy structured / machine-owned** | revision history, anchor/alias + link maps, large data tables | **Bundle sidecars** (`history.yaml`, `refs.yaml`, `tables/*.csv`) | would pollute prose; consumed structurally |

Consequence: once computed fields leave the body, `enrich`/`normalize` stop rewriting
bodies for metadata-only reasons, so the silver tree fingerprints (§7) mean what we want —
a body diff is a *real content* diff.

### 6.4 The decomposition decisions (the candidate table — all adopted)

Beyond images and revision history (already split in v1), v2 adopts these splits:

| Component | Decision | Where it goes |
|---|---|---|
| **Images** | split — write-once, huge, render-consumer | content-addressed `assets/`, referenced by sha256 |
| **Revision history** | split — machine-structured, query-consumer, prose-polluting | `history.yaml` sidecar (ordered lineage + refs to retained prior bodies); `revision_sidecar` pointer in body FM; **captured for later, opt-in git commit-replay** (§6.6) |
| **Large data tables** (data-dictionary / file-field listings) | **split** — structured data masquerading as prose; wreck diffs; API wants them as data | `tables/*.csv` sidecars; a reference/embed stub left in body. Small inline tables stay. |
| **Corpus-wide boilerplate** (legal notices, "how to use this manual", standard headers/footers) | **single-source** — duplicated across hundreds of docs | one shared boilerplate artifact; bodies reference it |
| **Glossary / acronym lists** | **promote to one shared corpus-level glossary** | `gold/glossary.md` (+ index.db terms); de-duplicate per-doc copies |
| **TOC, anchor/alias map, link maps** | derived — never store in body | regenerated TOC; `refs.yaml` sidecar / index.db |
| **Code / routine listings, MUMPS snippets** | keep in body for reading; **derive** to entity tables for query | `body.md` + `index.db` entities |
| **Prose, figures+captions, small tables** | keep in body — the irreducible human document | `body.md` |

The split detectors already exist in v1 (`boilerplate_pure`, `tables_pure`, `lexicon`) and
are the strongest reuse candidates (§16).

### 6.5 The "don't over-decompose" guardrail

Test for any proposed seam: *can a contributor still open one thing, read it, change it, and
see a sensible diff?* If a change requires editing five fragments, the decomposition has
gone too far. We cut exactly the seams in §6.4 and stop.

### 6.6 Version lineage: one anchor document, patch history captured for later git replay

The VDL ships each manual as a *series of versioned artifacts* (initial release + dozens of
patches), and every artifact re-embeds its own ever-growing revision apparatus. v2 collapses that
series into **one anchor document** and **captures the lineage as structured sidecars** — the
decluttering win *now*, with git-native version history available as a *deferred* capability
(tenet #12, goal §1). We split the two deliberately: stripping the clutter pays off immediately;
spending a commit-per-patch is mechanical overhead we don't take on until it's wanted.

**Grouping.** `catalog` assigns every fetched artifact a **version-group key** = document identity
(`app_code` + doc-identity slug) *with the version/patch component removed*, plus an ordering key
(patch number, then official revision date). `consolidate` gathers all members of a group and
orders them **oldest → newest**; `index` records the lineage and flags the newest member
`is_latest`.

**The anchor document.** Each version group collapses to one **anchor document**: a single living
markdown file at a stable, version-free path, whose body is the *latest* normalized version. Prior
versions are **not** separate published files. A reader opens the anchor and sees only current
content.

**Capture, don't replay (yet).** Rather than spend a commit per patch now, `consolidate`
**captures the full lineage into sidecars that travel with the anchor document**, so the bundle is
self-describing and a later replay needs nothing else:

- `history.yaml` — the ordered patch lineage: for each version, its patch id, official date,
  revision note, `source_sha256`, document stable ID, and a content-addressed reference to that
  version's **retained normalized body**.
- the prior-version normalized bodies themselves are **retained** (content-addressed; never
  re-acquired) and referenced by hash from `history.yaml` — so the ordered chain of *what each
  patch actually said*, not merely a changelog *about* it, travels with the anchor.

This is the "appropriate sidecar files that travel with the anchor document": everything required
to reconstruct history is captured next to the living doc, at document grain. Capture is
**append-only** — a later run in which a new VDL patch becomes the latest body appends one entry to
`history.yaml` and retains the previous body; nothing already captured is rewritten.

**Deferred git replay (designed-for, not run now).** Because the lineage and every prior body are
captured, a later, opt-in **`push --replay-history`** (§13) can reconstruct each group's history as
a sequence of commits against its one file — oldest body first, then each patch as a commit whose
diff *is* that patch's change, commit metadata drawn from `history.yaml`. After that one-time
replay, on GitHub:

- `git log <doc>.md` **is** the revision-history table (no inline table needed),
- `git blame <doc>.md` attributes every surviving line to the patch that introduced it,
- `git diff <patchA>..<patchB> -- <doc>.md` shows exactly what a patch changed.

Until that pass is run, the anchor file's git history is ordinary corpus history and the full
lineage lives in the sidecars — losing nothing, deferring only the mechanical replay.

**Declutter (now, independent of replay).** `normalize` strips the manual version-control
apparatus from the body — revision / patch-history tables, change-page markers, inline "(Patch
NN)" provenance annotations — routing the structured facts to `history.yaml` (§6.4). What remains
in `body.md` is the document, not its changelog. This immediate payoff does **not** wait on git
replay.

**Acquisition is per-version-group.** `crawl`/`fetch`/`convert`/`normalize` process *every* version
of a document, not only the latest — the historical bodies are exactly what capture (and any future
replay) preserve. Latest-only acquisition would discard the lineage this goal exists to keep.

**Prerequisite.** Stable IDs (§5.5): the document ID is keyed on identity + version, but the anchor
*file path* is keyed on the version-group key — so the living file's identity is invariant across
patches while its captured lineage grows.

---

## 7. The stage contract (orchestration core)

The pipeline is a **directed acyclic graph of stages over declared artifacts**. This is the
"software-defined asset" model (Dagster's mental model) implemented as a small in-house
runner (ADR-002).

### 7.1 The two core types

```python
class ArtifactContract:
    key: str                 # stable id, e.g. "silver/text@normalized", "index.db:documents"
    kind: Kind               # FILE | TREE_TEXT | TREE_ASSET_CAS | SQLITE_TABLE | SQLITE_VIEW | GIT_REMOTE
    storage_class: Class     # ASSET_WRITE_ONCE | TEXT_VERSIONED | STATE | EXTERNAL
    produced_by: str | None  # the Stage.name that emits it (None = external, e.g. VDL site)
    optional: bool = False   # soft dependency (missing → loud WARN, not FAIL)
    def locate(cfg) -> Resolved: ...           # resolve path/(db,table) FROM typed config — never hardcoded
    def validate(cfg) -> CheckResult: ...       # exists + structurally usable + min cardinality
    def fingerprint(cfg) -> str: ...            # cheap content signature (cheap by default, strong on --verify)

class Stage:
    name: str                # slug — identical in CLI subcommand, DAG node, completion record
    description: str         # one line
    requires: list[ArtifactContract]
    produces: list[ArtifactContract]
    idempotency: SKIP_IF_UNCHANGED | ALWAYS_RERUN | FORCE_ONLY
    contract_ver: int        # bump when produces[] shape changes → invalidates downstream
    def preflight(ctx, force) -> PROCEED | SKIP | FAIL(reason, remediation): ...
    def run(ctx, force) -> RunResult: ...        # the work; writes to a temp location, atomic-swaps on success
    def postflight(ctx, run) -> OK | FAIL: ...   # validate produces[]; on success write the completion record
```

A stage exposes exactly this. The CLI subcommand and the orchestrator drive every stage
through the identical `preflight → run → postflight` sequence. There is no second code path.

### 7.2 The completion record (the "done" signal)

`postflight` writes one row per `(stage, scope)` to `state.db`. This table *is* the
inter-stage contract surface; `status='ok'` is reachable **only** by passing postflight.

```sql
CREATE TABLE stage_runs (
    stage         TEXT NOT NULL,
    scope         TEXT NOT NULL DEFAULT '',   -- '' = whole corpus, else app_code
    status        TEXT NOT NULL,              -- 'ok' | 'failed'
    started_at    TEXT NOT NULL,
    finished_at   TEXT NOT NULL,
    inputs_fp     TEXT NOT NULL,              -- JSON {artifact_key: fingerprint} consumed
    outputs_fp    TEXT NOT NULL,              -- JSON {artifact_key: fingerprint} produced
    counts        TEXT NOT NULL,              -- JSON {processed, skipped, errors, ...}
    contract_ver  INTEGER NOT NULL,
    tool_ver      TEXT NOT NULL,
    PRIMARY KEY (stage, scope)
);
```

### 7.3 Preflight / postflight algorithms

**Preflight(S, force):**
1. For each `C in S.requires`: `C.validate()` must pass, else `FAIL(remediation="Run: vdocs " + C.produced_by)`. (If `C.optional` and absent → loud WARN, proceed.)
2. For each internal upstream `U=C.produced_by`: require `stage_runs[U].status=='ok'`, compatible `contract_ver`, and `C.fingerprint() == stage_runs[U].outputs_fp[C.key]`. Mismatch → `FAIL("{C.key} changed since {U} produced it; re-run {U}")`. *(This is what makes "the next stage knows it's ok to run" real, and fixes v1's stale-DB class of bug.)*
3. Skip decision: if `not force` and `idempotency==SKIP_IF_UNCHANGED` and `stage_runs[S].inputs_fp == current input fps` and `produces[].validate()` all pass → `SKIP`.
4. else `PROCEED`.

**Postflight(S):**
1. `produces[].validate()` all must pass; run any stage-specific deep gate (e.g. the
   frontmatter schema gate for `validate`).
2. On any failure: write `stage_runs[S]=failed` (do **not** bless) and raise. Downstream
   preflight will refuse.
3. On success: write `stage_runs[S]=ok` with input/output fingerprints, counts, versions.

**Producer vs consumer split:** *output validity* is asserted by the producer's postflight
(it knows what good looks like); *input presence/currency* by the consumer's preflight. The
consumer never re-deep-validates upstream output — it trusts `ok` + cheap `validate()` +
fingerprint match. No duplicated gates.

### 7.4 Atomicity and idempotency

- Every stage writes to `OUT.tmp/` and atomic-renames to `OUT/` on success, so a crash
  never leaves a half-written artifact that preflight mistakes for complete.
- `SKIP_IF_UNCHANGED` makes re-runs cheap; `--verify` upgrades fingerprints to full content
  hashes for paranoid/CI runs. Because silver stages read immutable inputs and write owned
  outputs, idempotency is *provable*: re-run and diff for byte-identity.

### 7.5 The orchestrator

A generic runner: topologically sort the `produces/requires` graph (§8 table *is* the
graph), then for each stage run `preflight → run → postflight`, stopping on the first hard
failure. `vdocs run [--from STAGE] [--to STAGE] [--only STAGE] [--force] [--verify]`.
There is no hand-maintained ordered stage list anywhere.

---

## 8. The pipeline — stages and contracts

The DAG, by medallion layer. This table is authoritative; the orchestrator derives order
from it.

| Layer | Stage | requires | produces | idempotency |
|---|---|---|---|---|
| 🥉 | **crawl** | `vdl` (external) | `catalog.raw` | FORCE_ONLY (network) |
| 🥉 | **catalog** | `catalog.raw` | `catalog.enriched` (patch identity, doc labels, app/section, search aliases) | SKIP_IF_UNCHANGED |
| 🥉 | **fetch** | `catalog.enriched` | `raw` (CAS docx/pdf), `raw/index.json` | SKIP_IF_UNCHANGED |
| 🥈 | **convert** | `raw`, `raw/index.json` | `text@converted`, `assets` (CAS) | SKIP_IF_UNCHANGED |
| 🥈 | **enrich** | `text@converted`, `catalog.enriched` | `text@enriched` (identity FM baked), `index.db:doc_meta_staged` | SKIP_IF_UNCHANGED |
| 🥈 | **normalize** | `text@enriched`, `raw` (for source_sha256) | `text@normalized` (+ `history.yaml`, `tables/*.csv`, `refs.yaml` sidecars; boilerplate/glossary refs) | SKIP_IF_UNCHANGED |
| 🥇 | **consolidate** | `text@normalized`, `assets` | `consolidated` (version groups — one anchor document per group; ordered `history.yaml` lineage + retained prior bodies captured as travel-with sidecars; `is_latest` flagged — the captured replay source, §6.6) | SKIP_IF_UNCHANGED |
| 🥇 | **index** | `text@normalized`, `consolidated` (grouping) | `index.db` (documents, doc_sections+FTS5, entities, quality, is_latest, views; **stable IDs**) | SKIP_IF_UNCHANGED |
| 🥇 | **relate** | `index.db` (documents, entities, sections) | `index.db:relations` (doc↔entity, doc↔doc xref, entity↔entity — the knowledge graph) | SKIP_IF_UNCHANGED |
| 🥇 | **embed** | `index.db:doc_sections` | `vectors.db` (per-chunk embeddings + ANN index) | SKIP_IF_UNCHANGED |
| 🥇 | **manifest** | `consolidated`, `index.db`, `vectors.db`, `state.db` (lineage) | `corpus-manifest.json` + `discovery.json` | SKIP_IF_UNCHANGED |
| 🥇 | **publish** | `corpus-manifest.json`, `text@normalized`, `consolidated`, `assets`, `catalog.enriched`, `glossary` | `publish` (markdown-only human tree + INDEX) | SKIP_IF_UNCHANGED |
| 🥇 | **validate** | `publish`, `text@normalized`, `index.db`, `vectors.db` | (HARD GATE — schema + lineage + dead-anchor + ID/vector integrity; sets its own `ok`) | ALWAYS_RERUN |
| 🚀 | **push** | `publish` (+ validate `ok`) | `git:vistadocs/vdl` (one anchor file per version group + travel-with lineage sidecars; **commit-replay deferred behind opt-in `--replay-history`**, §6.6) | FORCE_ONLY |
| ⬩ | **analyze** (off critical path) | `text@normalized` | `reports/` (survey, headings, lexicon) | SKIP_IF_UNCHANGED |

Notes:
- **`catalog`** is the promoted, first-class home of v1's hidden `enrich_inventory.py`
  logic. It is a normal stage with a contract — never a hand-run script.
- **`normalize` runs per-document before `consolidate`** (cleaner: normalization is a
  per-doc transform; consolidation is grouping). v1 had this backwards. `normalize` also
  **strips the manual version-control apparatus** (revision tables, change pages, "(Patch NN)"
  annotations) from bodies — git carries that lineage instead (§6.6).
- **Acquisition is per-version-group, not per-latest-doc.** `crawl`/`fetch`/`convert`/
  `normalize` process *every* version of a document (initial release + all patches), because
  the historical bodies are what `push` replays into commit history. Latest-only acquisition
  would discard the very history this goal exists to preserve.
- **`consolidate` captures the version rollup; `push` defers the git replay** (§1, §6.6).
  `consolidate` collapses each group to one anchor document and captures the ordered lineage +
  retained prior bodies into travel-with sidecars (`history.yaml`). `push` commits the anchor
  files and their sidecars; it does **not** replay a commit-per-patch by default. That mechanical
  history build is opt-in (`push --replay-history`) and can run any time later *from the captured
  sidecars alone* — no re-acquisition, nothing rewritten.
- **`index` / `relate` / `embed` are the derived machine views** (atomic index, knowledge
  graph, semantic index). They are rebuildable and *not* on the human-publish critical path,
  so re-deriving them never blocks a docs push.
- **`embed` is idempotent on the embedding-model id+version** (carried in `contract_ver`): a
  model change invalidates `vectors.db` and forces a re-embed; unchanged model + unchanged
  chunks → skip. The model id+version is recorded in lineage.
- **`relate`** materializes the knowledge graph from already-extracted entities and
  cross-references — it adds no new extraction, only edges, so it is cheap and re-runnable.
- **`analyze`** is diagnostic and parallel; nothing depends on it.
- **Serving is not a batch stage.** `push` (humans) and the **MCP server** (machines, §14)
  are read-only consumers of gold; the MCP server is a long-running service (`vdocs
  serve-mcp`), not a DAG node.
- The frontmatter **schema gate** lives in `validate` and is **non-optional before
  `push`** — it is impossible to push a corpus with broken frontmatter.

---

## 9. Cross-cutting concerns

### 9.1 Typed configuration

One `Settings` object (Pydantic Settings, ADR-005): all paths derived from `LAKE` (env
`DATA_DIR`), all HTTP/limits/remotes typed and validated at startup. No module-level path
constants scattered across files; no hardcoded absolute paths anywhere (a v1 sin in the 6.x
scripts). Stages receive resolved paths via `ctx`, never compute them ad hoc.

### 9.2 The shared kernel (anti-duplication — tenet #4)

Exactly **one** implementation of each cross-cutting primitive, in a `kernel/` package, used
by every stage:

- `kernel/text/` — mojibake/cp1252 repair, control-char scrub, HTML strip. (v1 had **three**
  copies; v2 has one, property-tested.)
- `kernel/frontmatter/` — the *only* YAML frontmatter codec (parse, canonical-order emit,
  round-trip-safe). Identity-only on write (§6.3).
- `kernel/fingerprint/` — tree/file/sqlite fingerprints + the single incremental-walk +
  mtime-cache helper. (v1 had **three** mtime caches.)
- `kernel/cas/` — content-addressed store: `put(bytes) -> sha256`, `get(sha256)`, `link`.
- `kernel/lineage/` — provenance stamping (`source_sha256`, `converter`, `tool_ver`, `at`).
- `kernel/db/` — SQLite open/migrate/upsert helpers; one place that knows pragmas.

**Rule:** if a second stage needs a primitive, it imports it from `kernel/` or the primitive
is promoted *into* `kernel/`. Copy-paste across stages is a build-breaking review failure.

### 9.3 Validation and schema gates

- Frontmatter is validated against a **draft 2020-12 JSON Schema** (`additionalProperties:
  false`) *and* a Pydantic model — at write time (schema-on-write) in the codec, and again
  as the hard gate in `validate`. Hard violations block publish/push; soft (type drift,
  unknown keys) are advisory.
- Pure transforms (normalize filters, parsers) get **property-based tests** (Hypothesis,
  ADR-008) in addition to example tests — idempotency and round-trip are properties.

### 9.4 Lineage and provenance

Every gold and silver artifact carries, in its frontmatter or sidecar, the `source_sha256`
of the bronze document it derives from, the `converter`/`tool_ver`, and timestamps. The
`manifest` stage rolls these into `corpus-manifest.json`. `state.db` records stage-level
lineage (which input fingerprints produced which output fingerprints). You can answer "where
did this byte come from, and with what tool version?" for anything.

### 9.5 Observability and failure

- Structured logging (structlog, ADR-007): JSON in CI, pretty in TTY. Every stage logs
  counts and the completion record.
- **Fail loud (tenet #7):** preflight failures carry a remediation (`Run: vdocs X`);
  postflight never blesses a degraded output; soft-optional inputs (e.g. a missing
  `normalized` tree) produce a *prominent* WARN, never a silent fallback (a specific v1 bug).
- No `print()` in library code; the CLI layer is the only thing that writes to stdout for
  humans.

---

## 10. Tooling decisions (ADRs)

Decided up front. Each: choice, why, and the credible alternative we rejected.

| # | Decision | Choice | Rationale | Rejected alternative |
|---|---|---|---|---|
| 001 | Language / runtime | **Python 3.12**, `uv` for deps/lock | mature docx/pandoc/docling ecosystem; team standard; v1 reuse | — |
| 002 | Orchestration | **In-house DAG runner** on the Stage/Artifact abstraction | single-node, no scheduler/UI needs; full control; self-documenting; zero heavy runtime dep; abstraction is deliberately Dagster-shaped for cheap future lift | **Dagster** (best conceptual fit via software-defined assets; adopt if multi-tenant/scheduling/observability needs arise) · Airflow (ops-heavy, overkill) · Snakemake/Make (file-dep only, no contracts) |
| 003 | Large-asset versioning | **Custom content-addressed store** in the lake (`<sha256>.<ext>`); git holds markdown only | simplest thing that dedups; no LFS quota/server | **DVC** (credible: git-native data versioning + pipeline DAG + CAS — adopt if you want git-tracked data lineage) · **Git LFS** (only if images must render on GitHub) |
| 004 | State / index store | **SQLite** ×3 (`state.db`, `index.db`, `vectors.db`); FTS5 for lexical search | zero-ops, single-file, embedded; FTS5 is excellent; consumers (MCP server) read them directly | Postgres (ops overhead, unneeded at scale) |
| 005 | Config | **Pydantic Settings** | typed, validated-at-startup, env-overridable; kills scattered path constants | module-level constants (v1; untyped, drift-prone) |
| 006 | Data models / contracts | **Pydantic v2** for boundary types (frontmatter, manifest, config, artifacts); dataclasses for pure-internal | validation + serialization for free; powers the schema gate | raw dataclasses everywhere (v1; manual validation) |
| 007 | Logging | **structlog** | structured, context-rich, CI/TTY aware | stdlib logging only |
| 008 | Testing | **pytest + Hypothesis**, TDD | property tests fit pure transforms; team TDD rule | example-only tests |
| 009 | CLI | **Typer** | type-hint-driven, modern DX, auto-help; one command per stage + `run` | Click (v1; fine, but Typer is the greenfield upgrade) |
| 010 | DOCX/PDF → markdown | **Pandoc default + Docling for an evidence-based allowlist** | v1's hardest-won lesson: Docling avoids the cross-ref bare-marker explosion for specific docs; keep it per-doc and evidence-driven | Docling-for-all (slower, heavier) · Pandoc-for-all (breaks on the allowlisted docs) |
| 011 | Markdown flavor / publish | **GFM**, docs-as-code, markdown-only in git, images materialized+gitignored | standard, GitHub-native, diff-friendly | committing images to git (bloat) |
| 012 | Vector store | **sqlite-vec** (`vectors.db`) | keeps the zero-ops single-file ethos; embeds ANN in SQLite at our scale (~tens of thousands of chunks); same backup/versioning story as `index.db` | dedicated vector DB (Qdrant/LanceDB — ops overhead, unneeded) · pgvector (needs Postgres) |
| 013 | Embedding model | **Pluggable provider, default a high-quality local model**; model id+version recorded in lineage and gates `vectors.db` | reproducible, offline, free; lineage makes re-embeds tracked; pluggable allows upgrades | hardcoded API embeddings (cost, network, non-reproducible) — kept as an opt-in provider |
| 014 | Machine protocol | **MCP via the official MCP Python SDK** | the standard for agent ↔ data; native Resources/Tools/Prompts map onto the corpus; host-agnostic | bespoke REST only (a thin REST facade may still wrap the same engine, but MCP is the headline interface) |
| 015 | Hybrid ranking | **Reciprocal Rank Fusion (RRF)** over semantic + lexical, with a structured pre-filter | parameter-light, robust, no score normalization; each mode independently callable | learned re-rankers (overkill now; revisit if quality demands) · single-mode retrieval (misses recall) |
| 016 | Document version control | **Collapse each patch series to one anchor file and *capture* the full lineage (ordered `history.yaml` + retained prior bodies) in travel-with sidecars; defer mechanical git commit-replay to an opt-in later pass** (§6.6) | declutters bodies to current content *now* at low cost; preserves a *complete, self-contained* lineage so the truly GitHub-native `git log`/`blame`/`diff` history can be built later with zero re-acquisition; avoids spending a commit-per-patch of mechanical churn up front | replaying every patch *in this pass* (high overhead, little immediate payoff) · keeping per-version files (N near-duplicates, lost diffs) · leaving revision tables inline (VDL/v1 status quo — clutter, not computable) · discarding prior bodies (would make later replay impossible) |

---

## 11. Repository and package layout

The package tree mirrors the pipeline (tenet #9). Every top-level package under `src/` is
either a stage, the kernel, the orchestrator, or shared models — and **every one is reached
by the DAG or is a test fixture.** No dead packages.

```
src/vdocs/
  kernel/          # the single shared kernel (§9.2) — text, frontmatter, fingerprint, cas, lineage, db
  models/          # Pydantic boundary types: Catalog, Document, Frontmatter, ArtifactContract, ...
  contracts/       # ArtifactContract definitions + the artifact registry (one place)
  orchestrator/    # generic DAG runner, stage_runs I/O, preflight/postflight engine
  stages/
    crawl/         # each stage: pure logic (*_pure.py) + thin driver (stage.py) implementing Stage
    catalog/
    fetch/
    convert/
    enrich/
    normalize/     # F1–F10 filters as pure modules, sequenced by one orchestrator function
    consolidate/
    index/
    relate/        # knowledge-graph edge materialization → index.db:relations
    embed/         # chunk → embedding → vectors.db (pluggable provider)
    manifest/
    publish/
    validate/
    push/
    analyze/
  server/          # MCP server (read-only over gold) + hybrid-search engine — §14
    mcp.py         #   MCP Resources / Tools / Prompts
    search.py      #   hybrid retrieval (semantic + lexical + structured + graph) + RRF fusion
    ids.py         #   stable-ID scheme + URI resolution (shared with stages)
  cli/             # Typer app: one subcommand per stage + `run` (orchestrator) + `serve-mcp`
  config.py        # Pydantic Settings
tests/
  unit/            # pure logic, no I/O (mirrors src 1:1)
  property/        # Hypothesis tests for transforms
  integration/     # SQLite/file I/O, fixtures, @network-marked live tests
  fixtures/
docs/
  vdocs-design.md            # this document
  adr/                       # one file per ADR as they evolve
  stages/                    # per-stage reference (generated from contracts where possible)
```

**Hard rules** (CI-enforced): no top-level `.py` modules; every stage implements the `Stage`
protocol; pure logic has no I/O; I/O layers are coverage-omitted and integration-tested; a
primitive used by ≥2 stages must live in `kernel/`.

---

## 12. Testing strategy

- **TDD throughout** (write the failing test first), per the team rule.
- **Unit (pure):** every pure function; no filesystem/network/SQLite. Mirrors `src/` 1:1.
- **Property (Hypothesis):** idempotency (`normalize(normalize(x)) == normalize(x)`),
  round-trips (frontmatter encode/decode), and invariants (no anchor points nowhere) for the
  transform-heavy stages.
- **Integration:** stage drivers against SQLite + local fixtures; the `validate` gate against
  known-bad corpora; the orchestrator against a tiny synthetic DAG.
- **Contract tests:** every `ArtifactContract.validate()`/`fingerprint()` against real and
  corrupt fixtures.
- Coverage gate ≥95% on `src/` excluding the explicitly-omitted I/O layers.

---

## 13. Delivery — docs-as-code to GitHub

- The **gold publish tree is markdown-only**; images are materialized from the asset store
  for browsability and **gitignored** (they live in the lake / optionally an LFS or release
  asset, ADR-003).
- The published repo is the human deliverable: stable file paths, one-file-one-history,
  PR-reviewable. Identity frontmatter travels with each file; computed metadata does not
  (it's in `index.db`, which the API serves).
- **Version history is captured now, git-replayable later (§6.6).** Each logical document is one
  **anchor file** at a stable, version-free path; the manual revision apparatus is stripped from
  the body (→ `history.yaml` + retained prior bodies that travel with the anchor). `push` commits
  the anchor files and their lineage sidecars; it does **not** replay a commit-per-patch by
  default. An opt-in `push --replay-history` can later rebuild each file's full commit history
  (`git log`/`blame`/`diff`) *entirely from the captured sidecars* — no re-acquisition — making
  the corpus truly GitHub-native whenever that payoff is wanted. Either way the prose is
  decluttered to current content today: prior versions roll up under the anchor document and the
  version-control clutter is gone.
- `push` is gated: it regenerates publish, runs the hard `validate` gate, and only then
  commits. A broken corpus cannot reach GitHub.

---

## 14. Delivery — the machine interface (MCP & semantic search)

This is the headline machine output: an **MCP server** that exposes the corpus to LLM agents
for **structured, computable, semantic search**. It is a thin, read-only serving layer over
the gold derived stores (`index.db`, `vectors.db`) and the corpus bundles — it performs no
transformation and owns no source of truth.

### 14.1 What "structured, computable, semantic" means here

The server answers queries across four retrieval modes and **fuses** them, rather than
offering only one:

- **Semantic** — meaning-based nearest-neighbour over per-chunk embeddings (`vectors.db`).
- **Lexical** — exact / keyword / phrase over FTS5 (`index.db:doc_sections_fts`).
- **Structured** — typed filters over fields (`app_code`, `doc_type`, `section`, `is_latest`,
  FileMan file number, has-entity, date) — deterministic, composable.
- **Graph** — traversal over `relations` (which routine is defined where; which docs
  reference this RPC; the version lineage of a document).

"Computable" means results are **data, not prose**: every hit carries a stable ID, a typed
score, structured metadata, and a resolvable URI — so an agent can chain calls
(search → fetch → traverse) deterministically.

### 14.2 Hybrid ranking

Default `mode=hybrid` runs semantic + lexical and fuses with **Reciprocal Rank Fusion**
(RRF, ADR-015) — robust, parameter-light, no score-normalization headaches. The structured
filter is applied **before** ranking (a WHERE clause), so semantic recall is never spent on
out-of-scope chunks. Each mode is also independently callable for agents that want control.

### 14.3 MCP surface

Modeled on the three MCP primitives — **Resources** (addressable data), **Tools** (callable
functions), **Prompts** (templated workflows):

**Resources** (stable URIs, so a host can load them as context):
- `vdocs://doc/{doc_id}` — a whole document bundle (markdown + identity frontmatter).
- `vdocs://section/{section_id}` — a single section (the retrieval chunk).
- `vdocs://entity/{type}/{name}` — an entity dossier (definition + every reference).
- Resource templates enumerate apps, doc-types, and packages for browsing.

**Tools** (typed in/out, JSON-schema'd):
- `search(query, mode=hybrid, filters={app,doc_type,section,is_latest,has_entity,…}, k)` →
  ranked `[{section_id, doc_id, title, snippet, score, uri, metadata}]`.
- `get_document(doc_id)` / `get_section(section_id)` → full content + metadata + neighbours.
- `find_entity(name, type?)` → where defined + every reference (graph).
- `cross_references(id, direction=out|in)` → graph neighbours of a doc/entity.
- `list_versions(group_key)` → version lineage with `is_latest`.
- `get_lineage(id)` → provenance back to the bronze source + tool versions.

**Prompts**: pre-baked retrieval workflows (e.g. "answer-with-citations over vdocs", "trace a
routine across the corpus") that wire the tools together with citation discipline.

### 14.4 Discovery descriptor (maximal discoverability)

`manifest` emits a machine-readable **discovery descriptor** (`gold/discovery.json`): the
corpus schema (entity types, fields, enums), counts, the stable-ID scheme, the embedding
model id+version, and the MCP capabilities. This is the "front door" that lets an agent (or
another tool) understand the corpus *without* crawling it — JSON Schema for the data, plus the
MCP capability manifest the server advertises on connect.

### 14.5 Boundaries

- **Read-only, derived-only.** The server opens `index.db` / `vectors.db` read-only and serves
  the corpus bundles. A corpus rebuild produces new derived stores; the server reopens them.
  It never writes back, never transforms.
- **Stable IDs are the contract** (§5.5). Anchors in the published markdown, vector keys, graph
  nodes, and MCP resource URIs all reference the *same* IDs — so a citation an agent returns is
  resolvable in the human GitHub corpus too.
- **Not a stage.** It is a long-running service (`vdocs serve-mcp`), versioned with the
  derived-store `contract_ver` it expects; it refuses to start against an incompatible store.

---

## 15. The downstream API (separate repo, for context)

`index.db` is the contract with the existing API repo (`vista-docs-api`, out of scope for
this rewrite). It is a **derived, rebuildable** artifact: the API treats it read-only and
never writes back. The pipeline owns its schema (`index` stage + `contract_ver`). This keeps
the API decoupled — a corpus rebuild produces a new `index.db`; the API just reopens it. The
new MCP server (§14) is the headline machine interface; this REST API continues to work
unchanged off the same `index.db`.

---

## 16. Reuse from the v1 repo (reference-only)

v1 is **reference, not foundation.** Port *pure logic with tests*, discard *structure,
orchestration, scripts, and in-place I/O*. High-value reuse candidates (all are pure or
nearly so, and already tested):

| v1 source | Reuse as | Notes |
|---|---|---|
| `normalize/*_pure.py` (F1–F10 filters) | `stages/normalize/` pure modules | the genuinely good part of v1; clean pure/IO split already |
| `survey/stats.py`, `analyze/headings.py`, `analyze/lexicon.py`, `analyze/diff.py` | `stages/analyze/` | pure analysis; boilerplate/glossary detection feeds §6.4 splits |
| `classify/rules.py` | `stages/catalog/` or `convert/` | doc-type classification (was wrongly marked "inactive" in v1) |
| `validate/frontmatter.py` + JSON schema | `stages/validate/` + `kernel/frontmatter/` | the hard gate; the best safety pattern in v1 |
| `crawl/parser.py`, `fetch/strategy.py` | `stages/crawl,fetch/` pure parts | VDL HTML parsing + URL derivation logic |
| `ingest/converter.py` backend-selection + `DOCLING_DOCS` allowlist | `stages/convert/` | the evidence-based Pandoc/Docling decision (ADR-010) |
| `enrich/extractors.py`, `enrich_inventory.py` transforms | `stages/enrich/`, `stages/catalog/` (decomposed) | extract the *pure* transforms; **discard** the 1448-line script shell and the in-place I/O |

**Discard wholesale:** `migrate/` (dead), the `pipeline/` standalone-script execution model,
the in-place-mutation runners, the three duplicated mojibake/mtime/frontmatter
implementations (replace with one `kernel/` each), and all hardcoded paths.

---

## 17. Phased build plan

Each phase ends with a runnable, tested increment. Build the spine before the stages.

1. **Kernel + config + models + contracts + orchestrator.** The Stage/Artifact
   abstraction, `state.db`, the generic DAG runner, the shared kernel (one mojibake/
   frontmatter/fingerprint/CAS each), Pydantic config. A no-op two-stage DAG proves
   preflight→run→postflight + completion records + skip/force end-to-end.
2. **Bronze:** crawl → catalog → fetch, with the CAS raw store and lineage.
3. **Silver:** convert (Pandoc+Docling) → enrich (identity FM + staged meta) → normalize
   (F1–F10 + bundle sidecars: history, tables, refs; boilerplate/glossary single-sourcing).
4. **Gold derive:** consolidate → index (sections+FTS5+entities+quality, **stable IDs**) →
   **relate** (knowledge graph) → manifest (+ `discovery.json`).
5. **Gold deliver (humans):** publish (markdown-only + materialized assets) → validate (hard
   gate) → push (anchor files + captured lineage sidecars; **commit-replay deferred**, §6.6).
   Plus analyze (off critical path).
6. **Machine interface (§14):** **embed** (chunk → `vectors.db`) → the **MCP server**
   (`serve-mcp`) with hybrid search (semantic + lexical + structured + graph, RRF). This is
   the headline machine output.
7. **Harden:** property tests for transforms, `--verify` full-hash mode, `gc` for old silver
   trees, the per-stage `docs/stages/` reference generated from contracts, and the opt-in
   `push --replay-history` that builds git commit history from the captured `history.yaml`
   sidecars + retained prior bodies (§6.6) — the deferred git-native version-control payoff.

Steps 1–2 already deliver the thing v1 never had: a real orchestrated pipeline with
contracts. Everything after is filling in stages against a spine that already enforces
idempotency, gating, and lineage.

---

## 18. Glossary

- **Artifact** — a declared, contract-bound input/output of a stage (a file, tree, DB table,
  or remote). Identified by a stable `key`.
- **Asset store (CAS)** — content-addressed, write-once store for binaries (`<sha256>.<ext>`).
- **Bronze / Silver / Gold** — medallion layers: immutable evidence / conformed versioned
  text / curated deliverable.
- **Bundle** — a per-document directory of typed parts (`body.md` + sidecars).
- **Completion record** — the `stage_runs` row a stage writes on success; the "done" signal
  the next stage's preflight reads.
- **Contract** — a stage's declared `requires`/`produces` plus its preflight/postflight.
- **Derived artifact** — anything rebuildable from bronze+silver (e.g. `index.db`,
  `publish/`). Never a source of truth.
- **Identity frontmatter** — the small, stable, human-curated metadata baked into `body.md`.
- **Lineage** — the recorded chain from a derived byte back to its bronze source + tool
  version.
- **Shred** — decompose a document into atomic units. We shred only into the *derived DB*,
  never the source files.
- **Stage** — one node of the pipeline DAG; a pure transform from `requires` to `produces`.
- **Version group** — the set of all VDL artifacts (initial release + every patch) that are the
  same logical document; keyed by document identity with the version/patch component removed.
  Collapses to one anchor document in publish (§6.6).
- **Anchor document** (a.k.a. living / consolidated document) — the single, version-free markdown
  file that represents a version group at its latest content; prior versions are not published as
  separate files but **captured in travel-with lineage sidecars** (`history.yaml` + retained prior
  bodies, §6.6).
- **Commit replay** — the *deferred, opt-in* reconstruction of a version group's patch lineage as
  an ordered sequence of git commits against its anchor file, built **from the captured
  `history.yaml` + retained prior bodies** (§6.6). Not run in the default pipeline; `push
  --replay-history` performs it.
- **Stable ID** — deterministic, re-run-invariant identifier for a document/section/entity;
  the cross-reference contract shared by markdown anchors, the vector index, the graph, and
  MCP resource URIs.
- **Chunk** — the retrieval unit for search; a derived `doc_section`, never a file on disk.
- **Embedding / vector index** — per-chunk vectors in `vectors.db` enabling semantic
  (meaning-based) retrieval.
- **Knowledge graph** — `index.db:relations`; edges between documents and entities
  (defines / references / versions) enabling computable traversal.
- **Hybrid search** — fusion of semantic + lexical + structured + graph retrieval (default
  via RRF).
- **RRF (Reciprocal Rank Fusion)** — rank-based score fusion across retrieval modes;
  parameter-light and normalization-free.
- **MCP (Model Context Protocol)** — the open protocol by which the corpus is exposed to LLM
  agents as Resources, Tools, and Prompts.
- **Discovery descriptor** — `gold/discovery.json`; the machine-readable "front door"
  describing the corpus schema, ID scheme, embedding model, and MCP capabilities.
```
