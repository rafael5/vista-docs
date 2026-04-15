#!/usr/bin/env python3
"""Chunk md-img documents into sections and index them for search.

Stage 6.5 of the vista-docs pipeline (runs after the frontmatter audit).

For every file under ~/data/vista-docs/md-img/, parses the ATX heading
hierarchy (#, ##, ###, ...) into a parent-linked section tree and writes it
to ~/data/vista-docs/state/frontmatter.db:

    doc_sections         one row per heading, with body text
    doc_sections_fts     FTS5 virtual table over heading + body
    doc_section_mtimes   incremental cache

Hybrid search is then one query away:
    SELECT s.heading, snippet(doc_sections_fts,1,'<b>','</b>',' … ',15)
    FROM doc_sections_fts JOIN doc_sections s ON s.section_id=rowid
    WHERE doc_sections_fts MATCH 'audit AND XUPROGMODE'
    ORDER BY rank LIMIT 20;

Run:
    python3 pipeline/chunk_sections.py                 # incremental
    python3 pipeline/chunk_sections.py --force         # reindex every doc
    python3 pipeline/chunk_sections.py --pkg XU        # one package only
"""

from __future__ import annotations

import argparse
import re
import sqlite3
import sys
from datetime import datetime
from pathlib import Path

MDI = Path("/home/rafael/data/vista-docs/md-img")
DB_PATH = Path("/home/rafael/data/vista-docs/state/frontmatter.db")

FM_RE = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)
DUP_FM_RE = re.compile(r"\A\s*---\n.*?\n---\n", re.DOTALL)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$", re.MULTILINE)
CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
HTML_TAG_RE = re.compile(r"<[^>]+>")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)")
WS_RE = re.compile(r"\s+")

SLUG_STRIP = re.compile(r"[^a-z0-9\s-]")
SLUG_DASH = re.compile(r"\s+")


def slugify(heading: str) -> str:
    s = heading.lower()
    s = SLUG_STRIP.sub("", s)
    s = SLUG_DASH.sub("-", s).strip("-")
    return s[:100] or "section"


def strip_frontmatter(text: str) -> str:
    m = FM_RE.match(text)
    body = text[m.end() :] if m else text
    # strip duplicate pandoc title block
    m2 = DUP_FM_RE.match(body)
    if m2:
        body = body[m2.end() :]
    return body.lstrip("\n")


def clean_body_text(s: str) -> str:
    s = CODE_FENCE_RE.sub(" ", s)
    s = IMAGE_RE.sub(" ", s)
    s = HTML_TAG_RE.sub(" ", s)
    s = WS_RE.sub(" ", s).strip()
    return s


def parse_sections(text: str):
    """Yield (level, heading, char_start, char_end) with body boundaries."""
    body = strip_frontmatter(text)
    matches = list(HEADING_RE.finditer(body))
    if not matches:
        return [(1, "(document body)", 0, len(body), body)]
    out = []
    # Preamble (if any text before first heading)
    first = matches[0]
    if first.start() > 20:
        out.append((1, "(preamble)", 0, first.start(), body[: first.start()]))
    for i, m in enumerate(matches):
        level = len(m.group(1))
        # Strip leading '#' chars that pandoc sometimes emits inside the text
        heading = re.sub(r"^[#\s]+", "", m.group(2).strip()).strip()
        if not heading:
            heading = "(empty heading)"
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        sec_body = body[start:end]
        out.append((level, heading, m.start(), end, sec_body))
    return out


def ensure_schema(con: sqlite3.Connection):
    con.executescript("""
    CREATE TABLE IF NOT EXISTS doc_sections (
        section_id INTEGER PRIMARY KEY,
        doc_id INTEGER NOT NULL,
        parent_section_id INTEGER,
        level INTEGER NOT NULL,
        seq INTEGER NOT NULL,
        heading TEXT NOT NULL,
        anchor TEXT NOT NULL,
        char_start INTEGER,
        char_end INTEGER,
        word_count INTEGER,
        body TEXT,
        FOREIGN KEY(doc_id) REFERENCES documents(doc_id),
        FOREIGN KEY(parent_section_id) REFERENCES doc_sections(section_id)
    );
    CREATE INDEX IF NOT EXISTS idx_sec_doc ON doc_sections(doc_id);
    CREATE INDEX IF NOT EXISTS idx_sec_parent ON doc_sections(parent_section_id);
    CREATE INDEX IF NOT EXISTS idx_sec_level ON doc_sections(level);

    CREATE TABLE IF NOT EXISTS doc_section_mtimes (
        rel_path TEXT PRIMARY KEY,
        mtime REAL,
        indexed_at TEXT
    );
    """)
    # FTS5 external-content table
    has_fts = con.execute("SELECT 1 FROM sqlite_master WHERE name='doc_sections_fts'").fetchone()
    if not has_fts:
        con.executescript("""
        CREATE VIRTUAL TABLE doc_sections_fts USING fts5(
            heading, body,
            content='doc_sections',
            content_rowid='section_id',
            tokenize='porter unicode61'
        );
        CREATE TRIGGER doc_sections_ai AFTER INSERT ON doc_sections BEGIN
            INSERT INTO doc_sections_fts(rowid, heading, body)
            VALUES (new.section_id, new.heading, new.body);
        END;
        CREATE TRIGGER doc_sections_ad AFTER DELETE ON doc_sections BEGIN
            INSERT INTO doc_sections_fts(doc_sections_fts, rowid, heading, body)
            VALUES('delete', old.section_id, old.heading, old.body);
        END;
        """)


def index_file(con: sqlite3.Connection, rel_path: str, doc_id: int, text: str):
    c = con.cursor()
    c.execute("DELETE FROM doc_sections WHERE doc_id=?", (doc_id,))
    sections = parse_sections(text)
    # Build parent chain via a level stack
    stack = []  # [(level, section_id), ...]
    for seq, (level, heading, cstart, cend, sec_body) in enumerate(sections):
        while stack and stack[-1][0] >= level:
            stack.pop()
        parent = stack[-1][1] if stack else None
        cleaned = clean_body_text(sec_body)
        wc = len(cleaned.split())
        c.execute(
            """INSERT INTO doc_sections(doc_id, parent_section_id, level, seq,
                heading, anchor, char_start, char_end, word_count, body)
               VALUES(?,?,?,?,?,?,?,?,?,?)""",
            (
                doc_id,
                parent,
                level,
                seq,
                heading[:200],
                slugify(heading),
                cstart,
                cend,
                wc,
                cleaned[:20000],
            ),
        )
        sid = c.lastrowid
        stack.append((level, sid))
    return len(sections)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--pkg", default=None)
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    if not DB_PATH.exists():
        print(f"[!] {DB_PATH} missing — run audit_frontmatter.py first", file=sys.stderr)
        sys.exit(2)

    con = sqlite3.connect(DB_PATH)
    ensure_schema(con)

    # doc map from documents table
    rows = con.execute("SELECT doc_id, rel_path FROM documents").fetchall()
    doc_map = {rp: did for did, rp in rows}

    if args.pkg:
        root = MDI / args.pkg
        files = sorted(root.rglob("*.md")) if root.is_dir() else []
    else:
        files = sorted(MDI.rglob("*.md"))

    # incremental filter
    mt_rows = con.execute("SELECT rel_path, mtime FROM doc_section_mtimes").fetchall()
    prior = {} if args.force else {r[0]: r[1] for r in mt_rows}
    kept, skipped = [], 0
    for p in files:
        rp = str(p.relative_to(MDI))
        if rp in prior and abs(p.stat().st_mtime - prior[rp]) < 1.0:
            skipped += 1
            continue
        kept.append(p)
    files = kept[: args.limit] if args.limit else kept

    print(f"[+] Indexing {len(files)} files (skipped {skipped} unchanged)...")
    t0 = datetime.now()
    total_sections = 0
    missing_doc = 0
    for i, p in enumerate(files, 1):
        if i % 250 == 0:
            print(f"    {i}/{len(files)}")
        rp = str(p.relative_to(MDI))
        doc_id = doc_map.get(rp)
        if doc_id is None:
            missing_doc += 1
            continue
        try:
            txt = p.read_text(encoding="utf-8")
        except Exception:
            continue
        try:
            n = index_file(con, rp, doc_id, txt)
            total_sections += n
            con.execute(
                "INSERT OR REPLACE INTO doc_section_mtimes VALUES(?,?,?)",
                (rp, p.stat().st_mtime, datetime.now().isoformat(timespec="seconds")),
            )
        except Exception as e:
            print(f"    ! {rp}: {type(e).__name__}: {e}", file=sys.stderr)
    con.commit()
    # Rebuild FTS index (external-content tables need manual rebuild after bulk changes)
    con.execute("INSERT INTO doc_sections_fts(doc_sections_fts) VALUES('rebuild')")
    con.commit()
    con.close()
    elapsed = (datetime.now() - t0).total_seconds()
    print(
        f"[+] {total_sections} sections indexed in {elapsed:.1f}s "
        f"({missing_doc} files had no frontmatter.db document row)"
    )
    print("[+] Done.")


if __name__ == "__main__":
    main()
