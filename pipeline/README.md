# Post-ingest pipeline stages (6–6.7)

These scripts extend the main ETL pipeline (`src/vista_docs/`, stages 1–5:
crawl → fetch → ingest → enrich → sync). They run **after** the markdown
corpus exists under `~/data/vista-docs/md-img/` and all write into a single
canonical SQLite at `~/data/vista-docs/state/frontmatter.db`.

Each stage is idempotent, incremental (mtime cache), and supports `--pkg
CODE` to scope work to one app and `--force` to rebuild.

Run order on a fresh corpus:

```bash
python3 pipeline/audit_frontmatter.py      # 6.   normalize frontmatter + audit DB
python3 pipeline/chunk_sections.py         # 6.5  heading tree + FTS5 index
python3 pipeline/extract_entities.py       # 6.6  routines/globals/options/rpcs/codes
python3 pipeline/apply_quality_views.py    # 6.7  is_latest + quality_score + views
```

On subsequent runs the first three stages skip unchanged docs (via
`audit_mtimes` / `doc_section_mtimes` / `doc_entity_mtimes` tables) and
finish in seconds. Stage 6.7 is pure SQL and always re-runs the three
updates + view rebuilds.

| # | Script | Adds / updates |
|---|---|---|
| 6   | `audit_frontmatter.py`   | `documents`, `doc_file_refs`, `doc_security_keys`, `doc_keywords`, `audit_issues`, `audit_mtimes`; normalizes every md-img frontmatter in place |
| 6.5 | `chunk_sections.py`      | `doc_sections` (parent-linked tree), `doc_sections_fts` (FTS5), `doc_section_mtimes` |
| 6.6 | `extract_entities.py`    | `doc_routines`, `doc_globals`, `doc_options`, `doc_rpcs`, `doc_codes`; `v_{routine,global,option,rpc,code}_coverage` views; `doc_entity_mtimes` |
| 6.7 | `apply_quality_views.py` | `documents.patch_num_int`, `documents.is_latest`, `documents.quality_score`; `v_doc_enriched`, `v_group_latest`, `v_app_latest` views |

Full reference: `~/claude/skills/vdl-pipeline/SKILL.md` (sections Audit
Stage 6, Chunk Stage 6.5, Entity Stage 6.6, Quality Stage 6.7).

Downstream consumer: `~/projects/vista-docs-api/` (stage 7, FastAPI server
that serves this DB as JSON).
