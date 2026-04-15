#!/usr/bin/env python3
"""Compute quality_score + is_latest on the documents table, expose as views.

Stage 6.7 of the vista-docs pipeline. Runs after entities (6.6). Pure SQL
on top of what the earlier stages already materialized; no new md-img work.

Adds / refreshes:
  documents.patch_num_int   INTEGER  — numeric suffix of patch_id
  documents.is_latest       INTEGER  — 1 for the newest doc in each group_key
  documents.quality_score   INTEGER  — 0..100, composite of existing signals
  v_doc_enriched            VIEW     — documents + per-doc ref counts
  v_group_latest            VIEW     — one row per group_key, latest doc
  v_app_latest              VIEW     — count of latest-version docs per app

Run:
    python3 apply_quality_views.py          # recompute all 3 columns + views
"""

from __future__ import annotations

import argparse
import re
import sqlite3
import sys
from datetime import datetime
from pathlib import Path

DB_PATH = Path("/home/rafael/data/vista-docs/state/frontmatter.db")
PATCH_TAIL_RE = re.compile(r"\*(\d+)\s*$")


def ensure_columns(con: sqlite3.Connection):
    cols = {row[1] for row in con.execute("PRAGMA table_info(documents)")}
    if "patch_num_int" not in cols:
        con.execute("ALTER TABLE documents ADD COLUMN patch_num_int INTEGER")
    if "is_latest" not in cols:
        con.execute("ALTER TABLE documents ADD COLUMN is_latest INTEGER DEFAULT 0")
    if "quality_score" not in cols:
        con.execute("ALTER TABLE documents ADD COLUMN quality_score INTEGER DEFAULT 0")
    con.commit()


def fill_patch_num_int(con: sqlite3.Connection):
    """Parse trailing integer from patch_id (NS*V*P form); NULL otherwise."""
    rows = con.execute(
        "SELECT doc_id, patch_id FROM documents WHERE patch_id IS NOT NULL AND patch_id!=''"
    ).fetchall()
    updates = []
    for doc_id, patch_id in rows:
        m = PATCH_TAIL_RE.search(patch_id or "")
        updates.append((int(m.group(1)) if m else None, doc_id))
    con.executemany("UPDATE documents SET patch_num_int=? WHERE doc_id=?", updates)
    con.commit()
    return len([u for u in updates if u[0] is not None])


def fill_is_latest(con: sqlite3.Connection):
    """Mark the newest doc per group_key as is_latest=1, others 0.

    Ordering within a group_key:
      1. patch_num_int DESC (highest patch wins)
      2. pub_date DESC      (fallback for anchor docs without patches)
      3. doc_id DESC        (final tie-break, stable)
    Docs with NULL/empty group_key are treated as their own singleton group.
    """
    con.execute("UPDATE documents SET is_latest=0")
    con.execute("""
      WITH ranked AS (
        SELECT doc_id,
          ROW_NUMBER() OVER (
            PARTITION BY COALESCE(NULLIF(group_key,''), 'doc-' || doc_id)
            ORDER BY COALESCE(patch_num_int, -1) DESC,
                     COALESCE(pub_date,'') DESC,
                     doc_id DESC
          ) AS rn
        FROM documents
      )
      UPDATE documents
         SET is_latest=1
       WHERE doc_id IN (SELECT doc_id FROM ranked WHERE rn=1)
    """)
    con.commit()
    return con.execute("SELECT COUNT(*) FROM documents WHERE is_latest=1").fetchone()[0]


def fill_quality_score(con: sqlite3.Connection):
    """Composite 0-100. Signals come from existing tables only (no md re-parse).

    Components (all capped):
      + content_depth     : 0-40  (word_count/100)
      + structure_depth   : 0-15  (section count / 2)
      + fileman_coverage  : 0-15  (#file_refs × 3)
      + security_coverage : 0-10  (#security_keys × 3)
      + operational_depth : 0-10  (menu_options)
      + has_metadata      : 0-10  (page_count > 0)
    Penalties:
      if is_stub=1  → score = 0
      if word_count < 100 → cap at 15
    """
    con.execute("""
      WITH refs AS (
        SELECT d.doc_id,
               COALESCE((SELECT COUNT(*) FROM doc_file_refs f
                          WHERE f.doc_id=d.doc_id),0) AS n_files,
               COALESCE((SELECT COUNT(*) FROM doc_security_keys k
                          WHERE k.doc_id=d.doc_id),0) AS n_keys,
               COALESCE((SELECT COUNT(*) FROM doc_sections s
                          WHERE s.doc_id=d.doc_id),0) AS n_sections
          FROM documents d
      )
      UPDATE documents
         SET quality_score = (
           SELECT CASE
             WHEN documents.is_stub=1 THEN 0
             WHEN COALESCE(documents.word_count,0) < 100 THEN
               MIN(15,
                 MIN(10, refs.n_files * 3)
                 + MIN(5, refs.n_keys * 3))
             ELSE MIN(100,
                 MIN(40, COALESCE(documents.word_count,0)/100)
               + MIN(15, refs.n_sections/2)
               + MIN(15, refs.n_files * 3)
               + MIN(10, refs.n_keys * 3)
               + MIN(10, COALESCE(documents.menu_options,0))
               + (CASE WHEN COALESCE(documents.page_count,0)>0 THEN 10 ELSE 0 END)
             )
           END
           FROM refs WHERE refs.doc_id = documents.doc_id
         )
    """)
    con.commit()


VIEWS_SQL = """
DROP VIEW IF EXISTS v_doc_enriched;
CREATE VIEW v_doc_enriched AS
SELECT d.*,
       (SELECT COUNT(*) FROM doc_file_refs      f WHERE f.doc_id=d.doc_id) AS n_files,
       (SELECT COUNT(*) FROM doc_security_keys  k WHERE k.doc_id=d.doc_id) AS n_keys,
       (SELECT COUNT(*) FROM doc_routines       r WHERE r.doc_id=d.doc_id) AS n_routines,
       (SELECT COUNT(*) FROM doc_globals        g WHERE g.doc_id=d.doc_id) AS n_globals,
       (SELECT COUNT(*) FROM doc_options        o WHERE o.doc_id=d.doc_id) AS n_options,
       (SELECT COUNT(*) FROM doc_rpcs           p WHERE p.doc_id=d.doc_id) AS n_rpcs,
       (SELECT COUNT(*) FROM doc_codes          c WHERE c.doc_id=d.doc_id) AS n_codes,
       (SELECT COUNT(*) FROM doc_sections       s WHERE s.doc_id=d.doc_id) AS n_sections
  FROM documents d;

DROP VIEW IF EXISTS v_group_latest;
CREATE VIEW v_group_latest AS
SELECT * FROM v_doc_enriched WHERE is_latest=1;

DROP VIEW IF EXISTS v_app_latest;
CREATE VIEW v_app_latest AS
SELECT app_code,
       app_name,
       section,
       COUNT(*)        AS n_latest_docs,
       SUM(word_count) AS total_words,
       AVG(quality_score) AS avg_quality
  FROM v_group_latest
 GROUP BY app_code, app_name, section
 ORDER BY n_latest_docs DESC;
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--verbose", action="store_true")
    ap.parse_args()

    if not DB_PATH.exists():
        print(f"[!] {DB_PATH} missing — run audit_frontmatter.py first", file=sys.stderr)
        sys.exit(2)

    con = sqlite3.connect(DB_PATH)
    t0 = datetime.now()
    ensure_columns(con)
    n_patch = fill_patch_num_int(con)
    n_latest = fill_is_latest(con)
    fill_quality_score(con)
    con.executescript(VIEWS_SQL)
    con.commit()
    elapsed = (datetime.now() - t0).total_seconds()

    # Summary
    n_docs = con.execute("SELECT COUNT(*) FROM documents").fetchone()[0]
    q_rows = con.execute(
        """SELECT
             AVG(quality_score) AS avg_q,
             MIN(quality_score) AS min_q,
             MAX(quality_score) AS max_q,
             SUM(CASE WHEN quality_score>=70 THEN 1 ELSE 0 END) AS high_q,
             SUM(CASE WHEN quality_score<20  THEN 1 ELSE 0 END) AS low_q
           FROM documents"""
    ).fetchone()
    con.close()

    print(f"[+] Updated {n_docs} documents in {elapsed:.1f}s")
    print(f"    patch_num_int filled : {n_patch}")
    print(f"    is_latest=1          : {n_latest}  (one per group)")
    print(
        f"    quality avg={q_rows[0]:.1f}  min={q_rows[1]}  max={q_rows[2]}"
        f"  high(>=70)={q_rows[3]}  low(<20)={q_rows[4]}"
    )


if __name__ == "__main__":
    main()
