# Prompt — Regenerate the VistA docs pipeline and harden it against all data-quality errors

> Paste everything below the line into a fresh session started in `~/projects/vista-docs`.
> It is self-contained; it assumes no prior conversation.

---

You are working in the **`vista-docs`** Python pipeline project. Your job is to
**completely regenerate the published VistA Documentation Library corpus from
source, fix every data-quality defect at the generator level (not by loosening
consumers), and add comprehensive, permanent guardrails** so a broken corpus can
never be published again.

## Orientation — read these first

- **Pipeline code:** `~/projects/vista-docs/` — Python; TDD; toolchain `uv` /
  `ruff` / `mypy` / `pytest`; use `.venv/bin/`-prefixed tools; run the project's
  `make check` (vet/lint/type/test) before any commit.
- **Published output:** `~/data/vista-docs/publish/` — one markdown file per
  document with YAML frontmatter, laid out `publish/<section>/<app>/<doc>.md`.
  It is its own git repo, remote `git@github.com:vistadocs/vdl.git`.
- **Intermediate stages:** under `~/data/vista-docs/` (`raw`, `docx-to-md`,
  `md-img`, `consolidated`, `inventory`, `survey`, `state`).
- **Skills:** read `~/claude/skills/vdl-pipeline/SKILL.md` (stage list, CLI
  commands, `pipeline/audit_frontmatter.py`, incremental mtime caches) and
  `~/claude/skills/vdl/SKILL.md` (the VDL section taxonomy: `CLI`/`FIN`/`GUI`/
  `INF`/`MON`).
- **TDD is a hard rule:** write a failing test first for every fix and every new
  validator, confirm it fails, then implement, then confirm green.

## Known defects to fix — VERIFY each against the live code before changing (treat file/line refs as leads, not gospel)

1. **~22% of published docs (≈317 / 1420) have invalid-YAML frontmatter.** The
   `description` and `audience` fields carry raw HTML table markup and
   backslash/quote/control-char garbage that the serializer emits as YAML that
   won't re-parse — e.g. `description: "<table> <col style=\\"width: 4%\\" />…"`
   and `(ACKQ\3.0\3)` ("unknown escape character"). Inspect
   `pipeline/audit_frontmatter.py` → `dump_frontmatter()` (the `yaml.safe_dump`
   call) and the audience extractor in `src/vista_docs/enrich/extractors.py`.
   - **Fix at the content level, not just escaping:** these fields are dumped
     HTML blobs that are useless as frontmatter. Strip HTML/markdown to plain
     text — or drop `description` entirely if no consumer uses it (decide from
     evidence). Then guarantee safe serialization.
   - **Then guarantee correctness:** after serializing a doc's frontmatter,
     round-trip it through a strict `yaml.safe_load` and **raise** if it does not
     parse. No document may ever be written with unparseable frontmatter.

2. **Two frontmatter schemas are mixed; ≈191 consolidated docs lack
   `section` / `app_name` / `title`.** The consolidation stage
   (`src/vista_docs/analyze/consolidation_runner.py`) writes a hardcoded legacy
   schema (`consolidated_title`, `master_source`, `prior_versions`, …) and never
   merges the rich inventory fields. **Unify it:** consolidated docs must carry
   the same required keys as single-version docs (`section`, `app_code`,
   `app_name`, `pkg_ns`, `doc_type`, `doc_label`, `title`, …), derived from the
   inventory / package master, while preserving the consolidation extras
   (`master_source`, `prior_versions`) as additional keys.

3. **Encoding mojibake** (e.g. `Developerâ€™s` → `Developer's`). `fix_mojibake()`
   exists in `audit_frontmatter.py`, but consolidated docs never pass through
   audit. Ensure every emitted doc — single-version AND consolidated — is
   mojibake-fixed and UTF-8 clean.

4. **Stale output:** `publish/` is weeks behind `md-img/`. The regen resolves
   this; confirm the final corpus reflects current upstream.

## Guardrails to add — the durable win: make broken data impossible to publish

Add **all** of the following:

- **Frontmatter schema + validator module** (`src/vista_docs/validate/…`, with
  tests). For every doc it must verify:
  - frontmatter re-parses with a **strict** YAML loader;
  - all required keys present and non-empty (`section`, `app_code`, `app_name`,
    `pkg_ns`, `doc_type`, `doc_label`, `title`);
  - `section` ∈ {CLI, FIN, GUI, INF, MON};
  - no raw HTML tags / markdown control sequences in scalar fields
    (`description`, `audience`, `title`, `doc_subject`);
  - no residual mojibake patterns and no C0 control characters;
  - the file is valid UTF-8;
  - schema uniformity — no doc using the legacy-only key set.
- **A `validate` CLI / pipeline stage** that runs the validator across the whole
  `publish/` tree (and ideally `md-img/`), prints a summary + a flags CSV, and
  **exits non-zero on any hard failure**.
- **A publish/push hard gate:** `publish` (and `push`) must refuse to run if
  `validate` reports any hard failure — you cannot ship a broken corpus.
- **Serializer-level invariant:** `dump_frontmatter()` self-validates every write
  (round-trip parse) and raises on failure, so defects never reach disk.
- **Golden/snapshot unit tests for the serializer** using the exact known-nasty
  inputs (HTML-table `description`, `(ACKQ\3.0\3)`, mojibake strings, embedded
  quotes/colons), asserting the output re-parses and round-trips.
- **GitHub Actions CI** on the `vistadocs/vdl` repo (or the pipeline repo) that
  runs the validator on the corpus on every push/PR and fails on any violation.
- **A git pre-push (or pre-commit) hook** in `publish/` that runs the validator
  locally before anything leaves the machine.
- **Extend `audit_frontmatter.py` flags** with `invalid_yaml_after_dump` and
  `legacy_schema` so the audit report surfaces these going forward.

## Execution sequence

0. **Baseline.** Run the current audit and record exact counts (total docs,
   invalid-YAML, missing-`section`, mojibake) so you can prove improvement.
1. TDD + implement defect fixes #1–#3.
2. TDD + implement the validator, the `validate` stage, the publish/push gate,
   the serializer invariant, and the golden tests.
3. **Full regen** from current source, reusing caches where safe:
   `enrich --force` → `sync --force` → `audit --force` → `consolidate --force` →
   `manifest` → `publish --force`. Run `crawl`/`fetch`/`ingest` too only if the
   upstream DOCX have changed. (`sync` skips docs that already have `section`
   unless `--force`, so always pass `--force` here.)
4. Run `validate` over the regenerated `publish/`. It must report **zero** hard
   failures.
5. **External acceptance check** with the docs browser: point `vdocs`
   (`~/projects/vista-docs-tui`) at the new corpus and confirm it loads every doc
   with a **strict** YAML parser — its tolerant fallback existed only as a
   workaround for exactly these bugs. Add a one-off strict-parse test over the
   whole corpus and confirm every doc parses cleanly with **zero fallbacks** and
   **zero `Uncategorized`/blank-app** docs.
6. Add the CI workflow + the pre-push hook.
7. Review the diff and a written before/after summary, then — **only after the
   user confirms** — `push` the corpus to `vistadocs/vdl` and commit the pipeline
   changes.

## Constraints

- **TDD always** — failing test first, then code. The validator and serializer
  especially need thorough tests.
- **Fix at the source (generator), never by loosening consumers.** Do not weaken
  `vdocs`'s parser; keep it strict-capable for the acceptance check.
- **Deterministic / idempotent:** a second full regen must produce byte-identical
  output.
- **No scope creep** beyond data-quality / regen / guardrails. Do not redesign
  the pipeline architecture.
- **Do NOT push to GitHub or any remote without explicit confirmation.** Stop
  after step 6 and show the validation summary, before/after counts, and the
  diff; wait for approval before any push.

## Definition of done

- 0 invalid-YAML docs · 0 docs missing required keys · 0 legacy-schema docs ·
  0 mojibake/control-char/HTML-in-scalar violations.
- `validate` is a hard gate before publish/push; the serializer self-validates;
  CI + pre-push hook are in place.
- `vdocs` loads the full corpus with a strict parser — zero fallbacks, zero
  `Uncategorized`.
- Before/after counts documented; the full regen is deterministic on rerun.
- Everything committed (pipeline repo + corpus repo); the push to `vistadocs/vdl`
  is pending only the user's approval.
