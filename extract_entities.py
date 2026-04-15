#!/usr/bin/env python3
"""Extract VistA entities (RPCs, routines, menu options, terminology codes)
from md-img bodies into cross-reference tables.

Stage 6.6 of the vista-docs pipeline. Runs after chunk (6.5). Populates new
tables in frontmatter.db:

    doc_rpcs           (doc_id, rpc_name)
    doc_routines       (doc_id, routine, tag, full_ref)   -- TAG^ROUTINE or ^ROUTINE
    doc_options        (doc_id, option_name)
    doc_globals        (doc_id, global_name)
    doc_codes          (doc_id, system, code)             -- LOINC / ICD-10 / …

Conservative extraction: only patterns with strong local context (e.g.
"RPC: <NAME>", `\\[OPTION NAME\\]`, `^GLOBAL(`) are accepted. False-positive
avoidance beats recall here — the cross-ref store is a normalization
substrate, not a first-draft search index.

Run:
    python3 extract_entities.py           # incremental (default)
    python3 extract_entities.py --force   # re-extract every doc
    python3 extract_entities.py --pkg XU  # one package only
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
CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)

# ---------- Routines: ^ROUTINE, TAG^ROUTINE, $$TAG^ROUTINE ----------
# VistA M routines: uppercase, 2-8 chars, may start with % (system routines)
# Tag may include digits + letters.
ROUTINE_RE = re.compile(r"(?:\$\$)?([A-Z][A-Z0-9]{0,7})\^(%?[A-Z][A-Z0-9]{1,7})\b")
GLOBAL_RE = re.compile(r"\^(%?[A-Z][A-Z0-9]{1,7})(?=\(|\b)")

# ---------- Menu options: bracketed uppercase identifier ----------
# Matches `[XU MAINT]` / `\[XU MAINT\]` / `[XUMAINT]` — pandoc escapes brackets
OPTION_RE = re.compile(r"\\?\[([A-Z][A-Z0-9][A-Z0-9 \-_/]{1,38}[A-Z0-9\]])\\?\]")

# ---------- RPC names: strict context ----------
# Accept only very-tight patterns:
#   "RPC: NAME"             — colon-introduced
#   "RPC `NAME`"            — backticked
#   "RPC **NAME**"          — bolded
#   "RPC named NAME"        — "named" introducer
#   "remote procedure call <NAME>" (same shapes)
# NAME: VistA RPCs are all-caps identifiers with spaces, 2-4 tokens, each
# token 2-15 chars of [A-Z0-9].
_RPC_NAME = r"([A-Z][A-Z0-9]{1,14}(?:\s+[A-Z0-9][A-Z0-9]{1,14}){1,4})"
RPC_CTX_RE = re.compile(
    r"(?:\bRPC\b|\bRemote\s+Procedure\s+Call\b)"
    r"(?:s|\(s\))?"
    r"[\s:,]{1,3}"
    r"(?:named\s+|called\s+|`|\*\*|\[)?" + _RPC_NAME + r"(?:`|\*\*|\])?"
)

# ---------- Terminology codes ----------
# LOINC: 4-5 digits, hyphen, check digit. Usually preceded by LOINC or unambiguous.
LOINC_RE = re.compile(r"\b(\d{4,5}-\d)\b")
# ICD-10-CM: letter + 2 digits, optional decimal + up to 4 chars
ICD10_RE = re.compile(r"\b([A-TV-Z]\d{2}(?:\.\d{1,4})?)\b")
# RxNorm RXCUI: numeric, needs context
RXCUI_RE = re.compile(r"\bRXCUI[:\s]+(\d{3,8})\b", re.IGNORECASE)
# SNOMED CT: needs context
SNOMED_RE = re.compile(r"\bSNOMED(?:\s*CT)?[:\s]+(\d{6,18})\b", re.IGNORECASE)
# CPT: 5-digit, needs context
CPT_RE = re.compile(r"\bCPT[:\s]+(\d{5})\b")


# Context window around ambiguous code matches
def _has_nearby(body: str, match_start: int, *needles: str, window: int = 120) -> bool:
    left = max(0, match_start - window)
    snippet = body[left : match_start + window].lower()
    return any(n.lower() in snippet for n in needles)


# ---------- Common false-positive filters ----------
ROUTINE_BLACKLIST = {
    # pandoc anchor / markdown link fragments that superficially look like
    # TAG^ROUTINE or ^ROUTINE but aren't VistA code
    "TOC",
    "NBSP",
    "SEC",
}
OPTION_BLACKLIST = {
    # markdown link text that is NOT a VistA option
    "TABLE OF CONTENTS",
    "SEE APPENDIX",
    "NOTE",
    "EXAMPLE",
    "IMPORTANT",
    "WARNING",
    "CAUTION",
    "TIP",
    "BACK TO TOC",
    "TOP",
    "REFERENCES",
    "INDEX",
    "GLOSSARY",
    "INTRODUCTION",
    "OVERVIEW",
    "SUMMARY",
    "APPENDIX A",
    "APPENDIX B",
    "APPENDIX C",
    "FIGURE",
    "CHAPTER",
}


def strip_frontmatter(text: str) -> str:
    m = FM_RE.match(text)
    body = text[m.end() :] if m else text
    m2 = DUP_FM_RE.match(body)
    if m2:
        body = body[m2.end() :]
    return body


# ---------- Extractors ----------
def extract_routines(body: str) -> set[tuple[str, str, str]]:
    """Return {(routine, tag, full_ref)}. Bare ^ROUTINE gets tag=''."""
    out = set()
    for m in ROUTINE_RE.finditer(body):
        tag, rtn = m.group(1), m.group(2)
        if rtn in ROUTINE_BLACKLIST:
            continue
        # exclude obvious prose words that happen to match (e.g. AS^IF, OK^NO)
        if tag in {"AS", "OR", "IF", "IS", "ON", "TO", "OF", "BY", "NO", "AM", "PM"}:
            continue
        out.add((rtn, tag, f"{tag}^{rtn}"))
    # Bare ^ROUTINE (no tag)
    for m in GLOBAL_RE.finditer(body):
        g = m.group(1)
        # only accept as "routine" if NOT followed by ( — that would be a global
        if body[m.end() : m.end() + 1] != "(" and len(g) >= 3 and g not in ROUTINE_BLACKLIST:
            out.add((g, "", f"^{g}"))
    return out


def extract_globals(body: str) -> set[str]:
    """^GLOBAL( form."""
    out = set()
    for m in GLOBAL_RE.finditer(body):
        if body[m.end() : m.end() + 1] == "(":
            g = m.group(1)
            if len(g) >= 2:
                out.add(g)
    return out


def extract_options(body: str, has_option_context: bool) -> set[str]:
    """Bracketed uppercase identifiers that look like VistA option names.
    Only extracted if the file mentions 'option' or 'menu' within the body."""
    if not has_option_context:
        return set()
    out = set()
    for m in OPTION_RE.finditer(body):
        name = m.group(1).strip().rstrip("]").strip()
        # Must contain a space OR be 6+ chars (options like XUMAINT)
        if len(name) < 4 or name in OPTION_BLACKLIST:
            continue
        # Exclude markdown anchor refs (no-space-all-caps followed by digits only is OK)
        if not re.match(r"^[A-Z][A-Z0-9 \-_/]{2,}$", name):
            continue
        # Quick sanity: don't take very long with only spaces
        if name.count(" ") > 6:
            continue
        out.add(name)
    return out


_RPC_FALSE_POSITIVES = {
    "REMOTE PROCEDURE CALL",
    "RPC BROKER",
    "BROKER",
    "SERVER",
    "VISTA LINK",
    "HEALTHE VET",
    "NEW PERSON",
    "REMOTE PROCEDURE",
}


def extract_rpcs(body: str, has_rpc_context: bool) -> set[str]:
    if not has_rpc_context:
        return set()
    out = set()
    for m in RPC_CTX_RE.finditer(body):
        name = m.group(1).strip()
        # Must have at least one space (multi-token) AND be 6-60 chars
        if " " not in name or not (6 <= len(name) <= 60):
            continue
        if name in _RPC_FALSE_POSITIVES:
            continue
        out.add(name)
    return out


def extract_codes(body: str) -> set[tuple[str, str]]:
    """Return {(system, code)}."""
    out = set()
    # LOINC — require context
    for m in LOINC_RE.finditer(body):
        code = m.group(1)
        if _has_nearby(body, m.start(), "loinc"):
            out.add(("LOINC", code))
    # ICD-10 — require context
    for m in ICD10_RE.finditer(body):
        code = m.group(1)
        if _has_nearby(body, m.start(), "icd-10", "icd10", "icd "):
            out.add(("ICD10", code))
    for m in RXCUI_RE.finditer(body):
        out.add(("RXNORM", m.group(1)))
    for m in SNOMED_RE.finditer(body):
        out.add(("SNOMED", m.group(1)))
    for m in CPT_RE.finditer(body):
        out.add(("CPT", m.group(1)))
    return out


# ---------- DB schema ----------
SCHEMA = """
CREATE TABLE IF NOT EXISTS doc_rpcs (
    doc_id INTEGER NOT NULL, rpc_name TEXT NOT NULL,
    PRIMARY KEY(doc_id, rpc_name)
);
CREATE INDEX IF NOT EXISTS idx_rpc_name ON doc_rpcs(rpc_name);

CREATE TABLE IF NOT EXISTS doc_routines (
    doc_id INTEGER NOT NULL, routine TEXT NOT NULL,
    tag TEXT NOT NULL DEFAULT '', full_ref TEXT NOT NULL,
    PRIMARY KEY(doc_id, full_ref)
);
CREATE INDEX IF NOT EXISTS idx_routine_name ON doc_routines(routine);
CREATE INDEX IF NOT EXISTS idx_routine_full ON doc_routines(full_ref);

CREATE TABLE IF NOT EXISTS doc_options (
    doc_id INTEGER NOT NULL, option_name TEXT NOT NULL,
    PRIMARY KEY(doc_id, option_name)
);
CREATE INDEX IF NOT EXISTS idx_option_name ON doc_options(option_name);

CREATE TABLE IF NOT EXISTS doc_globals (
    doc_id INTEGER NOT NULL, global_name TEXT NOT NULL,
    PRIMARY KEY(doc_id, global_name)
);
CREATE INDEX IF NOT EXISTS idx_global_name ON doc_globals(global_name);

CREATE TABLE IF NOT EXISTS doc_codes (
    doc_id INTEGER NOT NULL, system TEXT NOT NULL, code TEXT NOT NULL,
    PRIMARY KEY(doc_id, system, code)
);
CREATE INDEX IF NOT EXISTS idx_code_system ON doc_codes(system);
CREATE INDEX IF NOT EXISTS idx_code_code ON doc_codes(code);

CREATE TABLE IF NOT EXISTS doc_entity_mtimes (
    rel_path TEXT PRIMARY KEY, mtime REAL, extracted_at TEXT
);
"""

VIEWS = """
DROP VIEW IF EXISTS v_rpc_coverage;
CREATE VIEW v_rpc_coverage AS
  SELECT rpc_name, COUNT(DISTINCT doc_id) AS doc_count,
         GROUP_CONCAT(DISTINCT d.app_code) AS apps
  FROM doc_rpcs JOIN documents d USING(doc_id)
  GROUP BY rpc_name ORDER BY doc_count DESC;

DROP VIEW IF EXISTS v_routine_coverage;
CREATE VIEW v_routine_coverage AS
  SELECT routine, COUNT(DISTINCT doc_id) AS doc_count,
         GROUP_CONCAT(DISTINCT d.app_code) AS apps
  FROM doc_routines JOIN documents d USING(doc_id)
  GROUP BY routine ORDER BY doc_count DESC;

DROP VIEW IF EXISTS v_option_coverage;
CREATE VIEW v_option_coverage AS
  SELECT option_name, COUNT(DISTINCT doc_id) AS doc_count,
         GROUP_CONCAT(DISTINCT d.app_code) AS apps
  FROM doc_options JOIN documents d USING(doc_id)
  GROUP BY option_name ORDER BY doc_count DESC;

DROP VIEW IF EXISTS v_global_coverage;
CREATE VIEW v_global_coverage AS
  SELECT global_name, COUNT(DISTINCT doc_id) AS doc_count,
         GROUP_CONCAT(DISTINCT d.app_code) AS apps
  FROM doc_globals JOIN documents d USING(doc_id)
  GROUP BY global_name ORDER BY doc_count DESC;

DROP VIEW IF EXISTS v_code_coverage;
CREATE VIEW v_code_coverage AS
  SELECT system, code, COUNT(DISTINCT doc_id) AS doc_count,
         GROUP_CONCAT(DISTINCT d.app_code) AS apps
  FROM doc_codes JOIN documents d USING(doc_id)
  GROUP BY system, code ORDER BY doc_count DESC;
"""


def process_file(con: sqlite3.Connection, rel_path: str, doc_id: int, text: str) -> dict:
    body_full = strip_frontmatter(text)
    body = CODE_FENCE_RE.sub(" ", body_full)  # avoid code-block false positives

    body_lower = body.lower()
    has_opt_ctx = ("option" in body_lower) or ("menu" in body_lower)
    has_rpc_ctx = ("rpc" in body_lower) or ("remote procedure" in body_lower)

    routines = extract_routines(body)
    globals_ = extract_globals(body)
    options = extract_options(body, has_opt_ctx)
    rpcs = extract_rpcs(body, has_rpc_ctx)
    codes = extract_codes(body)

    c = con.cursor()
    for tbl in ("doc_rpcs", "doc_routines", "doc_options", "doc_globals", "doc_codes"):
        c.execute(f"DELETE FROM {tbl} WHERE doc_id=?", (doc_id,))
    for rpc in rpcs:
        c.execute("INSERT OR IGNORE INTO doc_rpcs VALUES(?,?)", (doc_id, rpc))
    for routine, tag, full_ref in routines:
        c.execute(
            "INSERT OR IGNORE INTO doc_routines VALUES(?,?,?,?)", (doc_id, routine, tag, full_ref)
        )
    for opt in options:
        c.execute("INSERT OR IGNORE INTO doc_options VALUES(?,?)", (doc_id, opt))
    for g in globals_:
        c.execute("INSERT OR IGNORE INTO doc_globals VALUES(?,?)", (doc_id, g))
    for system, code in codes:
        c.execute("INSERT OR IGNORE INTO doc_codes VALUES(?,?,?)", (doc_id, system, code))
    return {
        "rpcs": len(rpcs),
        "routines": len(routines),
        "options": len(options),
        "globals": len(globals_),
        "codes": len(codes),
    }


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
    con.executescript(SCHEMA)

    rows = con.execute("SELECT doc_id, rel_path FROM documents").fetchall()
    doc_map = {rp: did for did, rp in rows}

    if args.pkg:
        root = MDI / args.pkg
        files = sorted(root.rglob("*.md")) if root.is_dir() else []
    else:
        files = sorted(MDI.rglob("*.md"))

    mt_rows = con.execute("SELECT rel_path, mtime FROM doc_entity_mtimes").fetchall()
    prior = {} if args.force else {r[0]: r[1] for r in mt_rows}
    kept, skipped = [], 0
    for p in files:
        rp = str(p.relative_to(MDI))
        if rp in prior and abs(p.stat().st_mtime - prior[rp]) < 1.0:
            skipped += 1
            continue
        kept.append(p)
    files = kept[: args.limit] if args.limit else kept

    print(f"[+] Extracting from {len(files)} files (skipped {skipped} unchanged)...")
    t0 = datetime.now()
    totals = dict(rpcs=0, routines=0, options=0, globals=0, codes=0)
    missing = 0
    for i, p in enumerate(files, 1):
        if i % 250 == 0:
            print(f"    {i}/{len(files)}")
        rp = str(p.relative_to(MDI))
        doc_id = doc_map.get(rp)
        if doc_id is None:
            missing += 1
            continue
        try:
            txt = p.read_text(encoding="utf-8")
            counts = process_file(con, rp, doc_id, txt)
            for k, v in counts.items():
                totals[k] += v
            con.execute(
                "INSERT OR REPLACE INTO doc_entity_mtimes VALUES(?,?,?)",
                (rp, p.stat().st_mtime, datetime.now().isoformat(timespec="seconds")),
            )
        except Exception as e:
            print(f"    ! {rp}: {type(e).__name__}: {e}", file=sys.stderr)

    # (Re)build views so they reflect current data
    con.executescript(VIEWS)
    con.commit()
    con.close()
    elapsed = (datetime.now() - t0).total_seconds()
    print(f"[+] Done in {elapsed:.1f}s. Extracted:")
    for k, v in totals.items():
        print(f"    {k}: {v}")
    if missing:
        print(f"    (skipped {missing} files with no documents.doc_id row)")


if __name__ == "__main__":
    main()
