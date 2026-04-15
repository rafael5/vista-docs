#!/usr/bin/env python3
"""Audit & normalize md-img frontmatter; build canonical cross-reference SQLite.

Stage 6 of the vista-docs pipeline (after crawl/fetch/ingest/enrich/sync).
Runs idempotently and incrementally: on re-runs, only files whose mtime
changed since the last audit are reprocessed; the SQLite store is updated
in place.

Pipeline actions per file:
  1. Robust-parse frontmatter (fallback line-parser for YAML errors)
  2. Strip duplicate pandoc title block following the frontmatter
  3. Fix cp1252<->utf8 mojibake in all string values AND body
  4. Re-extract file_numbers, security_keys, menu_options from body
  5. Fill description/audience when empty or garbage
  6. Write normalized frontmatter back with canonical key order
  7. Stamp audit_applied: YYYY-MM-DD
  8. Upsert into ~/data/vista-docs/state/frontmatter.db

Run:
    python3 pipeline/audit_frontmatter.py                # incremental (default)
    python3 pipeline/audit_frontmatter.py --force        # reprocess every file
    python3 pipeline/audit_frontmatter.py --pkg XU       # one package dir only
    python3 pipeline/audit_frontmatter.py --limit 30     # smoke test
"""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

import yaml

MDI = Path("/home/rafael/data/vista-docs/md-img")
STATE = Path("/home/rafael/data/vista-docs/state")
SURVEY = Path("/home/rafael/data/vista-docs/survey")
DB_PATH = STATE / "frontmatter.db"
BACKUP_PATH = STATE / f"frontmatter_backup_{datetime.now():%Y-%m-%d}.jsonl"
REPORT_PATH = SURVEY / f"frontmatter_audit_{datetime.now():%Y-%m-%d}.md"

# ---------- Mojibake fixer (cp1252-as-utf8 double-decode artifacts) ----------
MOJIBAKE_MAP = {
    "â€™": "\u2019",  # right single quote
    "â€˜": "\u2018",  # left single quote
    "â€œ": "\u201c",  # left double quote
    "â€\x9d": "\u201d",  # right double quote (the â€<0x9d> case)
    "â€": "\u201d",  # right double quote (trailing bare)
    'â€"': "\u2014",  # em dash / en dash collapse (sometimes)
    "â€¦": "\u2026",  # ellipsis
    "â€¢": "\u2022",  # bullet
    "â€“": "\u2013",  # en dash
    "â€”": "\u2014",  # em dash
    "Ã©": "\u00e9",
    "Ã¨": "\u00e8",
    "Ãª": "\u00ea",
    "Ã«": "\u00eb",
    "Ã¡": "\u00e1",
    "Ã ": "\u00e0",
    "Ã¢": "\u00e2",
    "Ã¤": "\u00e4",
    "Ã­": "\u00ed",
    "Ã³": "\u00f3",
    "Ã¶": "\u00f6",
    "Ãº": "\u00fa",
    "Ã±": "\u00f1",
    "Ã§": "\u00e7",
    "Â\xa0": "\u00a0",
    "Â ": " ",
    "Ã\x9f": "\u00df",
}
_MOJI_RE = re.compile("|".join(re.escape(k) for k in sorted(MOJIBAKE_MAP, key=len, reverse=True)))


def fix_mojibake(s: str) -> tuple[str, int]:
    if not isinstance(s, str):
        return s, 0
    n = 0

    def _sub(m):
        nonlocal n
        n += 1
        return MOJIBAKE_MAP[m.group(0)]

    out = _MOJI_RE.sub(_sub, s)
    # Also try the generic round-trip: if string still contains â€ or Ã, attempt
    # reinterpreting as latin1 bytes decoded as utf-8
    if "â€" in out or "Ã" in out:
        try:
            rt = out.encode("latin1").decode("utf-8")
            if rt != out and all(ord(c) < 0xFFFD for c in rt):
                n += 1
                out = rt
        except (UnicodeEncodeError, UnicodeDecodeError):
            pass
    return out, n


# ---------- Frontmatter parse/unparse ----------
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
DUP_FM_RE = re.compile(r"\A\s*---\n(.*?)\n---\n", re.DOTALL)

CANONICAL_KEYS = [
    "title",
    "doc_type",
    "doc_label",
    "doc_layer",
    "doc_subject",
    "app_code",
    "app_name",
    "section",
    "app_status",
    "pkg_ns",
    "patch_ver",
    "patch_id",
    "group_key",
    "description",
    "audience",
    "keywords",
    "file_numbers",
    "security_keys",
    "menu_options",
    "page_count",
    "word_count",
    "section_count",
    "table_count",
    "figure_count",
    "appendix_count",
    "has_toc",
    "is_stub",
    "pub_date",
    "revision_count",
    "revision_newest",
    "revision_oldest",
    "docx_url",
    "pdf_url",
    "app_url",
    "audit_applied",
]


def parse_frontmatter(text: str) -> tuple[dict | None, str, str]:
    """Return (fm_dict|None, fm_raw, body). Uses YAML; falls back line-parse."""
    m = FM_RE.match(text)
    if not m:
        return None, "", text
    fm_raw = m.group(1)
    body = text[m.end() :]
    try:
        fm = yaml.safe_load(fm_raw)
        if isinstance(fm, dict):
            return fm, fm_raw, body
    except yaml.YAMLError:
        pass
    # Fallback: line-parse `key: value`
    fm = {}
    cur_key = None
    for line in fm_raw.splitlines():
        if not line.strip():
            continue
        if line.startswith("  - ") and cur_key:
            if not isinstance(fm.get(cur_key), list):
                fm[cur_key] = []
            fm[cur_key].append(line[4:].strip().strip("\"'"))
            continue
        mkv = re.match(r"^([a-zA-Z_][\w]*)\s*:\s*(.*)$", line)
        if mkv:
            k, v = mkv.group(1), mkv.group(2).strip()
            if v == "" or v == "[]":
                fm[k] = [] if v == "[]" else ""
            elif v == "True" or v == "true":
                fm[k] = True
            elif v == "False" or v == "false":
                fm[k] = False
            elif re.fullmatch(r"-?\d+", v):
                fm[k] = int(v)
            elif re.fullmatch(r"-?\d+\.\d+", v):
                try:
                    fm[k] = float(v)
                except ValueError:
                    fm[k] = v
            else:
                fm[k] = v.strip("\"'")
            cur_key = k
        # else: continuation lines folded into prior key as string
    return fm, fm_raw, body


def strip_duplicate_title_block(body: str) -> tuple[str, bool]:
    """Pandoc embeds a second --- title: --- block from docx meta; drop it."""
    m = DUP_FM_RE.match(body)
    if not m:
        return body, False
    inner = m.group(1)
    # only strip if it looks like a title block (contains title: or is short)
    if "title:" in inner.lower() or len(inner) < 400:
        return body[m.end() :].lstrip("\n"), True
    return body, False


def dump_frontmatter(fm: dict) -> str:
    """Emit YAML with canonical key order, stable, no mojibake-breeding keys."""
    ordered = {}
    for k in CANONICAL_KEYS:
        if k in fm:
            ordered[k] = fm[k]
    for k in fm:
        if k not in ordered:
            ordered[k] = fm[k]
    return yaml.safe_dump(
        ordered, allow_unicode=True, sort_keys=False, default_flow_style=False, width=1000
    )


# ---------- Extractors ----------
# FileMan file numbers: "FILE #N", "FILE (#N)", "File NNN", "#N.NN", "FILE NUMBER N"
FILE_NUM_RE = re.compile(
    r"\b(?:FILE|File|file)\s*(?:NUMBER|number|#)?\s*\(?\s*#?\s*(\d{1,6}(?:\.\d{1,4})?)\)?"
)
# also: "(#NNN)" inline after an entity name
FILE_PAREN_RE = re.compile(r"\(\s*#\s*(\d{1,6}(?:\.\d{1,4})?)\s*\)")

# VistA global names like ^DPT(, ^DD(, ^PS(50, — map where known
GLOBAL_TO_FILE = {
    "^DPT": "2",
    "^DIC": "1",
    "^DD": "0",
    "^DIA": "1.1",
    "^PS(50": "50",
    "^PSDRUG": "50",
    "^OR(100": "100",
    "^TIU(8925": "8925",
    "^VA(200": "200",
    "^VA(4": "4",
    "^XWB(8994": "8994",
    "^LAB(60": "60",
    "^AUPNPROB": "9000011",
    "^AUPNVSIT": "9000010",
    "^RAMIS(71": "71",
    "^PSRX": "52",
}
GLOBAL_RE = re.compile(r"\^[A-Z][A-Z0-9]{1,5}(?:\([0-9]{1,6})?")

# Security keys: known seed list from Kernel + FileMan + common packages
KNOWN_KEYS = {
    "XUAUDITING",
    "XUFILEGRAM",
    "XUMGR",
    "XUPROGMODE",
    "XUSCREENMAN",
    "XUSPF200",
    "XUSPY",
    "XUARCHIVE",
    "XUDEV",
    "XUAFFILIATE",
    "DDXP-DEFINE",
    "DIEXTRACT",
    "DIMANAGER",
    "DIUSER",
    "DG SECURITY OFFICER",
    "DGMTCOR",
    "DGMST",
    "DG ELIGIBILITY",
    "ORES",
    "ORELSE",
    "ORES,ORELSE",
    "OREMAS",
    "ORMGR",
    "LRLAB",
    "LRSUPER",
    "LRVERIFY",
    "LRPHSUPR",
    "LRPHSET",
    "PSJ RPHARM",
    "PSJ PHARM TECH",
    "PSJI MGR",
    "PSORPH",
    "PSOMGR",
    "PROVIDER",
    "CLINICIAN",
    "PSB MGR",
    "PSDMGR",
    "PSA ORDERS",
    "RAMGR",
    "SD SUPERVISOR",
    "TIUMGR",
    "USRWX",
    "PXRM MANAGER",
}
# fallback regex: all-caps VistA key pattern mentioned near "key"
KEY_CONTEXT_RE = re.compile(r"\b([A-Z][A-Z0-9 ]{2,25})\b\s*(?:security\s+)?key\b", re.IGNORECASE)
KEY_TOKEN_RE = re.compile(r"\b([A-Z]{2,6}[A-Z0-9]{0,2}(?:[- ][A-Z0-9]{1,10}){0,2})\b")

MENU_OPTION_RE = re.compile(r"\b(?:option|menu)\s+([A-Z][A-Z0-9 ]{2,30})\b")

STRIP_TAGS_RE = re.compile(r"<[^>]+>")
MULTI_WS_RE = re.compile(r"\s+")


def extract_file_numbers(body: str) -> list[str]:
    nums = set()
    for m in FILE_NUM_RE.finditer(body):
        n = m.group(1)
        if "." not in n and int(n) > 999999:
            continue
        nums.add(n)
    for m in FILE_PAREN_RE.finditer(body):
        nums.add(m.group(1))
    for m in GLOBAL_RE.finditer(body):
        g = m.group(0).rstrip("(")
        if g in GLOBAL_TO_FILE:
            nums.add(GLOBAL_TO_FILE[g])
    # sanity filter: drop numbers > 999999 unless sub-file notation
    out = sorted(
        (n for n in nums if (("." in n) or (n.isdigit() and int(n) <= 999999))),
        key=lambda x: (float(x), x),
    )
    return out


def extract_security_keys(body: str) -> list[str]:
    keys = set()
    for k in KNOWN_KEYS:
        if re.search(r"\b" + re.escape(k) + r"\b", body):
            keys.add(k)
    # context-based: "<TOKEN> security key" or "key <TOKEN>"
    for m in re.finditer(
        r"(?:security\s+key[s]?\s+(?:called|named|\:)?\s*)([A-Z][A-Z0-9\- ]{2,25})",
        body,
    ):
        tok = m.group(1).strip().rstrip(".,;:")
        if 2 < len(tok) < 30 and " " not in tok[:3]:
            keys.add(tok)
    for m in re.finditer(
        r"\b([A-Z][A-Z0-9]{1,6}(?:[- ][A-Z0-9]{1,10}){0,2})\s+(?:security\s+)?key\b",
        body,
    ):
        tok = m.group(1).strip()
        if tok.isupper() and len(tok) >= 3:
            keys.add(tok)
    return sorted(keys)


def extract_menu_options(body: str) -> int:
    """Rough count of distinct menu option identifiers."""
    opts = set()
    for m in MENU_OPTION_RE.finditer(body):
        opts.add(m.group(1).strip())
    return len(opts)


def make_description(body: str, title: str) -> str:
    """First meaningful prose paragraph, stripped, ≤300 chars."""
    # Remove HTML tags, images, code blocks first
    b = re.sub(r"```.*?```", "", body, flags=re.DOTALL)
    b = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", b)
    b = STRIP_TAGS_RE.sub("", b)
    # Skip heading lines and short lines
    for para in re.split(r"\n\s*\n", b):
        para = MULTI_WS_RE.sub(" ", para).strip()
        if not para or para.startswith("#") or len(para) < 60:
            continue
        if re.match(r"^[|\-\*+=\s]+$", para):
            continue
        if para.lower().startswith(("table of contents", "contents", "revision history")):
            continue
        return para[:300].rsplit(" ", 1)[0] + ("..." if len(para) > 300 else "")
    return ""


AUDIENCE_BY_DOCTYPE = {
    "TM": "Technical staff, IRM, system administrators",
    "UM": "End users (clinical / administrative, per package)",
    "UG": "End users and package coordinators (ADPAC)",
    "IG": "System administrators performing installation",
    "DIBR": "System administrators, deployment engineers",
    "RN": "System administrators, end users reviewing changes",
    "SG": "ISSOs, security officers, system administrators",
    "API": "VistA / M developers integrating with the package",
    "POM": "Production operations, release engineers",
    "TG": "Technical implementers",
    "VDD": "Release managers, configuration management",
    "CFG": "System administrators performing configuration",
    "QRG": "End users (quick reference)",
    "TRG": "Trainers and end users during onboarding",
    "FORM": "N/A (VA form, not VistA documentation)",
}


# ---------- Main ----------
def process_file(path: Path, backup_fh) -> dict:
    """Process one md file. Returns audit record."""
    rec = {
        "rel_path": str(path.relative_to(MDI)),
        "path": str(path),
        "issues": [],
        "moji_fixes": 0,
        "dup_block_stripped": False,
        "fm_recovered": False,
        "changed": False,
    }
    try:
        raw = path.read_text(encoding="utf-8")
    except Exception as e:
        rec["issues"].append(f"read_error:{e}")
        return rec
    fm, fm_raw, body = parse_frontmatter(raw)
    if fm is None:
        rec["issues"].append("no_frontmatter")
        return rec
    had_fm_error = False
    try:
        yaml.safe_load(fm_raw)
    except yaml.YAMLError:
        had_fm_error = True
        rec["fm_recovered"] = True
        rec["issues"].append("yaml_recovered")

    # Backup original
    backup_fh.write(
        json.dumps(
            {
                "rel_path": rec["rel_path"],
                "original_fm": fm_raw,
                "had_yaml_error": had_fm_error,
            }
        )
        + "\n"
    )

    # Strip dup title block in body
    body_new, stripped = strip_duplicate_title_block(body)
    rec["dup_block_stripped"] = stripped

    # Fix mojibake in fm string values
    total_moji = 0
    for k, v in list(fm.items()):
        if isinstance(v, str):
            fixed, n = fix_mojibake(v)
            if n:
                fm[k] = fixed
                total_moji += n
        elif isinstance(v, list):
            new_list = []
            for item in v:
                if isinstance(item, str):
                    fx, n = fix_mojibake(item)
                    total_moji += n
                    new_list.append(fx)
                else:
                    new_list.append(item)
            fm[k] = new_list
    # Fix mojibake in body
    body_fixed, n = fix_mojibake(body_new)
    total_moji += n
    body_new = body_fixed
    rec["moji_fixes"] = total_moji

    # Re-extract structural fields
    file_nums = extract_file_numbers(body_new)
    sec_keys = extract_security_keys(body_new)
    menu_ct = extract_menu_options(body_new)
    if not fm.get("file_numbers"):
        fm["file_numbers"] = file_nums
    else:
        existing = {str(x) for x in fm["file_numbers"]}
        merged = sorted(
            existing | set(file_nums),
            key=lambda x: (float(x) if re.fullmatch(r"\d+(?:\.\d+)?", str(x)) else 9e9, str(x)),
        )
        fm["file_numbers"] = merged
    if not fm.get("security_keys"):
        fm["security_keys"] = sec_keys
    else:
        fm["security_keys"] = sorted(set(fm["security_keys"]) | set(sec_keys))
    if not fm.get("menu_options"):
        fm["menu_options"] = menu_ct

    # Fill description if empty or malformed (e.g. markdown list inlined)
    desc = fm.get("description")
    if (not desc) or (isinstance(desc, str) and desc.strip().startswith("- [")):
        fm["description"] = make_description(body_new, fm.get("title", ""))
    elif isinstance(desc, str):
        fx, n = fix_mojibake(desc)
        fm["description"] = fx

    # Fill audience if empty or garbage (html/markdown leaked from body)
    aud = fm.get("audience") or ""
    if (not aud) or any(tok in str(aud) for tok in ("<!--", "](#", "|--", "<span", "[↑")):
        dt = fm.get("doc_type", "")
        fm["audience"] = AUDIENCE_BY_DOCTYPE.get(dt, "")

    # Ensure lists are lists not None
    for list_key in ("file_numbers", "security_keys", "keywords"):
        if fm.get(list_key) is None:
            fm[list_key] = []

    # Stamp audit
    fm["audit_applied"] = datetime.now().strftime("%Y-%m-%d")

    rec["file_numbers"] = fm["file_numbers"]
    rec["security_keys"] = fm["security_keys"]
    rec["menu_options"] = fm["menu_options"]

    # Write back
    new_fm_yaml = dump_frontmatter(fm)
    new_text = "---\n" + new_fm_yaml + "---\n" + body_new
    if new_text != raw:
        path.write_text(new_text, encoding="utf-8")
        rec["changed"] = True

    # Flag for manual review
    if not fm.get("title"):
        rec["issues"].append("missing_title")
    if fm.get("is_stub"):
        rec["issues"].append("is_stub")
    if fm.get("word_count", 1) < 100:
        rec["issues"].append("very_short")
    if fm.get("patch_id") is None and fm.get("doc_layer") == "patch":
        rec["issues"].append("patch_without_id")
    if total_moji > 20:
        rec["issues"].append(f"heavy_mojibake:{total_moji}")

    rec["fm"] = {
        k: fm.get(k)
        for k in (
            "title",
            "doc_type",
            "app_code",
            "pkg_ns",
            "patch_id",
            "doc_layer",
            "section",
            "app_status",
            "word_count",
            "is_stub",
        )
    }
    return rec


def _ensure_schema(con: sqlite3.Connection):
    con.executescript("""
    CREATE TABLE IF NOT EXISTS documents (
        doc_id INTEGER PRIMARY KEY,
        rel_path TEXT UNIQUE NOT NULL,
        title TEXT, doc_type TEXT, doc_label TEXT, doc_layer TEXT,
        app_code TEXT, app_name TEXT, section TEXT, app_status TEXT,
        pkg_ns TEXT, patch_ver TEXT, patch_id TEXT, group_key TEXT,
        word_count INTEGER, page_count INTEGER, is_stub INTEGER,
        pub_date TEXT, docx_url TEXT, pdf_url TEXT,
        menu_options INTEGER, audit_applied TEXT,
        description TEXT, audience TEXT
    );
    CREATE INDEX IF NOT EXISTS idx_doc_app ON documents(app_code);
    CREATE INDEX IF NOT EXISTS idx_doc_pkg ON documents(pkg_ns);
    CREATE INDEX IF NOT EXISTS idx_doc_section ON documents(section);
    CREATE INDEX IF NOT EXISTS idx_doc_type ON documents(doc_type);

    CREATE TABLE IF NOT EXISTS doc_file_refs (
        doc_id INTEGER NOT NULL, file_number TEXT NOT NULL,
        PRIMARY KEY(doc_id, file_number),
        FOREIGN KEY(doc_id) REFERENCES documents(doc_id)
    );
    CREATE INDEX IF NOT EXISTS idx_file_num ON doc_file_refs(file_number);

    CREATE TABLE IF NOT EXISTS doc_security_keys (
        doc_id INTEGER NOT NULL, security_key TEXT NOT NULL,
        PRIMARY KEY(doc_id, security_key),
        FOREIGN KEY(doc_id) REFERENCES documents(doc_id)
    );
    CREATE INDEX IF NOT EXISTS idx_key ON doc_security_keys(security_key);

    CREATE TABLE IF NOT EXISTS doc_keywords (
        doc_id INTEGER NOT NULL, keyword TEXT NOT NULL,
        PRIMARY KEY(doc_id, keyword)
    );
    CREATE INDEX IF NOT EXISTS idx_kw ON doc_keywords(keyword);

    CREATE TABLE IF NOT EXISTS audit_issues (
        doc_id INTEGER NOT NULL, issue TEXT NOT NULL,
        PRIMARY KEY(doc_id, issue)
    );

    -- Convenience views
    CREATE VIEW IF NOT EXISTS v_file_coverage AS
      SELECT file_number, COUNT(DISTINCT doc_id) AS doc_count,
             GROUP_CONCAT(DISTINCT d.app_code) AS apps
      FROM doc_file_refs f JOIN documents d USING(doc_id)
      GROUP BY file_number ORDER BY doc_count DESC;

    CREATE VIEW IF NOT EXISTS v_key_coverage AS
      SELECT security_key, COUNT(DISTINCT doc_id) AS doc_count,
             GROUP_CONCAT(DISTINCT d.app_code) AS apps
      FROM doc_security_keys k JOIN documents d USING(doc_id)
      GROUP BY security_key ORDER BY doc_count DESC;
    """)


def build_db(records: list[dict], full_rebuild: bool = False):
    """Upsert records into frontmatter.db. If full_rebuild, wipe+repopulate all tables."""
    con = sqlite3.connect(DB_PATH)
    _ensure_schema(con)
    c = con.cursor()
    if full_rebuild:
        for tbl in (
            "audit_issues",
            "doc_keywords",
            "doc_security_keys",
            "doc_file_refs",
            "documents",
        ):
            c.execute(f"DELETE FROM {tbl}")
    for rec in records:
        if "fm" not in rec or not rec.get("fm"):
            continue
        try:
            raw = Path(rec["path"]).read_text(encoding="utf-8")
            fm, _, _ = parse_frontmatter(raw)
            if not fm:
                continue
        except Exception:
            continue
        # Delete old rows for this doc first (upsert semantics)
        row = c.execute(
            "SELECT doc_id FROM documents WHERE rel_path=?", (rec["rel_path"],)
        ).fetchone()
        if row:
            old_id = row[0]
            for tbl in ("audit_issues", "doc_keywords", "doc_security_keys", "doc_file_refs"):
                c.execute(f"DELETE FROM {tbl} WHERE doc_id=?", (old_id,))
            c.execute("DELETE FROM documents WHERE doc_id=?", (old_id,))
        c.execute(
            """INSERT INTO documents(rel_path, title, doc_type, doc_label,
            doc_layer, app_code, app_name, section, app_status, pkg_ns,
            patch_ver, patch_id, group_key, word_count, page_count, is_stub,
            pub_date, docx_url, pdf_url, menu_options, audit_applied,
            description, audience)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (
                rec["rel_path"],
                fm.get("title"),
                fm.get("doc_type"),
                fm.get("doc_label"),
                fm.get("doc_layer"),
                fm.get("app_code"),
                fm.get("app_name"),
                fm.get("section"),
                fm.get("app_status"),
                fm.get("pkg_ns"),
                str(fm.get("patch_ver") or ""),
                fm.get("patch_id"),
                fm.get("group_key"),
                fm.get("word_count") or 0,
                fm.get("page_count") or 0,
                1 if fm.get("is_stub") else 0,
                str(fm.get("pub_date") or ""),
                fm.get("docx_url"),
                fm.get("pdf_url"),
                fm.get("menu_options") or 0,
                fm.get("audit_applied"),
                (fm.get("description") or "")[:500],
                (fm.get("audience") or "")[:200],
            ),
        )
        doc_id = c.lastrowid
        for fn in fm.get("file_numbers") or []:
            try:
                c.execute("INSERT OR IGNORE INTO doc_file_refs VALUES(?,?)", (doc_id, str(fn)))
            except Exception:
                pass
        for k in fm.get("security_keys") or []:
            try:
                c.execute("INSERT OR IGNORE INTO doc_security_keys VALUES(?,?)", (doc_id, str(k)))
            except Exception:
                pass
        for kw in (fm.get("keywords") or [])[:25]:
            try:
                c.execute(
                    "INSERT OR IGNORE INTO doc_keywords VALUES(?,?)", (doc_id, str(kw).lower())
                )
            except Exception:
                pass
        for issue in rec.get("issues", []):
            c.execute("INSERT OR IGNORE INTO audit_issues VALUES(?,?)", (doc_id, issue))
    con.commit()
    con.close()


def write_report(records: list[dict], elapsed: float):
    total = len(records)
    changed = sum(1 for r in records if r.get("changed"))
    moji_fixed = sum(r.get("moji_fixes", 0) for r in records)
    dup_stripped = sum(1 for r in records if r.get("dup_block_stripped"))
    fm_recovered = sum(1 for r in records if r.get("fm_recovered"))
    flagged = [r for r in records if r.get("issues")]
    issue_ct = Counter()
    for r in records:
        for i in r.get("issues", []):
            issue_ct[i.split(":")[0]] += 1
    files_extracted = sum(1 for r in records if r.get("file_numbers"))
    keys_extracted = sum(1 for r in records if r.get("security_keys"))
    all_files = Counter()
    all_keys = Counter()
    for r in records:
        for fn in r.get("file_numbers", []) or []:
            all_files[str(fn)] += 1
        for k in r.get("security_keys", []) or []:
            all_keys[str(k)] += 1
    lines = [
        f"# Frontmatter Audit Report — {datetime.now():%Y-%m-%d}",
        "",
        f"- Total md-img files: **{total}**",
        f"- Files modified: **{changed}**",
        f"- YAML errors recovered: **{fm_recovered}**",
        f"- Duplicate title blocks stripped: **{dup_stripped}**",
        f"- Mojibake substitutions: **{moji_fixed}**",
        f"- Docs with file_numbers extracted: **{files_extracted}**",
        f"- Docs with security_keys extracted: **{keys_extracted}**",
        f"- Elapsed: {elapsed:.1f}s",
        "",
        "## Issue breakdown",
        "| Issue | Count |",
        "|---|---:|",
    ]
    for k, v in issue_ct.most_common():
        lines.append(f"| {k} | {v} |")
    lines += [
        "",
        f"## Manual review queue ({len(flagged)} docs)",
        "Full list in `frontmatter_audit_flags.csv`.",
        "",
        "## Top 25 FileMan files referenced",
        "| File # | Docs |",
        "|---|---:|",
    ]
    for fn, c in all_files.most_common(25):
        lines.append(f"| {fn} | {c} |")
    lines += ["", "## Top 25 Security keys referenced", "| Key | Docs |", "|---|---:|"]
    for k, c in all_keys.most_common(25):
        lines.append(f"| `{k}` | {c} |")
    lines += [
        "",
        "## Canonical store",
        f"- SQLite: `{DB_PATH}`",
        "  - tables: documents, doc_file_refs, doc_security_keys, doc_keywords, audit_issues",
        "  - views: v_file_coverage, v_key_coverage",
        f"- Backup (original frontmatter): `{BACKUP_PATH}`",
        "",
        "## Query examples",
        "```sql",
        "-- Find every doc that references FileMan file #200 (NEW PERSON)",
        "SELECT rel_path, title FROM documents d JOIN doc_file_refs f USING(doc_id)",
        "WHERE f.file_number='200';",
        "",
        "-- All docs documenting the XUPROGMODE security key",
        "SELECT rel_path, title FROM documents d JOIN doc_security_keys k USING(doc_id)",
        "WHERE k.security_key='XUPROGMODE';",
        "",
        "-- Cross-package reference map for a file",
        "SELECT * FROM v_file_coverage WHERE file_number IN ('2','200','50','60','8925');",
        "```",
    ]
    REPORT_PATH.write_text("\n".join(lines))
    # Flag CSV
    import csv

    flag_csv = SURVEY / "frontmatter_audit_flags.csv"
    with flag_csv.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["rel_path", "issues", "app_code", "doc_type", "word_count", "title"])
        for r in flagged:
            fm = r.get("fm", {})
            w.writerow(
                [
                    r["rel_path"],
                    ";".join(r["issues"]),
                    fm.get("app_code", ""),
                    fm.get("doc_type", ""),
                    fm.get("word_count", ""),
                    fm.get("title", ""),
                ]
            )


def load_existing_mtimes() -> dict:
    """Return {rel_path: mtime_str} from prior audit, for incremental skip."""
    if not DB_PATH.exists():
        return {}
    try:
        con = sqlite3.connect(DB_PATH)
        # mtime stored as ISO string in documents.audit_applied is day-granular;
        # for file-level incremental we use a sidecar table.
        con.execute("""CREATE TABLE IF NOT EXISTS audit_mtimes(
            rel_path TEXT PRIMARY KEY, mtime REAL, audited_at TEXT)""")
        rows = con.execute("SELECT rel_path, mtime FROM audit_mtimes").fetchall()
        con.close()
        return {r[0]: r[1] for r in rows}
    except sqlite3.Error:
        return {}


def save_mtimes(records: list[dict]):
    con = sqlite3.connect(DB_PATH)
    con.execute("""CREATE TABLE IF NOT EXISTS audit_mtimes(
        rel_path TEXT PRIMARY KEY, mtime REAL, audited_at TEXT)""")
    now = datetime.now().isoformat(timespec="seconds")
    for r in records:
        try:
            mt = Path(r["path"]).stat().st_mtime
            con.execute(
                "INSERT OR REPLACE INTO audit_mtimes VALUES(?,?,?)", (r["rel_path"], mt, now)
            )
        except Exception:
            pass
    con.commit()
    con.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument(
        "--force", action="store_true", help="Re-process every file, ignore incremental mtime cache"
    )
    ap.add_argument("--pkg", default=None, help="Process only one app_code directory (e.g. XU)")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    STATE.mkdir(parents=True, exist_ok=True)
    SURVEY.mkdir(parents=True, exist_ok=True)

    if args.pkg:
        root = MDI / args.pkg
        if not root.is_dir():
            print(f"[!] package dir not found: {root}", file=sys.stderr)
            sys.exit(2)
        files = sorted(root.rglob("*.md"))
    else:
        files = sorted(MDI.rglob("*.md"))

    # Incremental skip: compare mtime to cache
    prior = {} if args.force else load_existing_mtimes()
    skipped = 0
    if prior:
        kept = []
        for p in files:
            rp = str(p.relative_to(MDI))
            if rp in prior and abs(p.stat().st_mtime - prior[rp]) < 1.0:
                skipped += 1
                continue
            kept.append(p)
        files = kept

    if args.limit:
        files = files[: args.limit]
    print(f"[+] Processing {len(files)} md files (skipped {skipped} unchanged since last audit)...")
    t0 = datetime.now()
    records = []
    with BACKUP_PATH.open("w") as bfh:
        for i, p in enumerate(files, 1):
            if i % 250 == 0:
                print(f"    {i}/{len(files)}")
            try:
                rec = process_file(p, bfh)
            except Exception as e:
                rec = {
                    "rel_path": str(p.relative_to(MDI)),
                    "path": str(p),
                    "issues": [f"process_error:{type(e).__name__}:{str(e)[:80]}"],
                }
            records.append(rec)
    elapsed = (datetime.now() - t0).total_seconds()
    print(f"[+] Normalized {sum(1 for r in records if r.get('changed'))} files in {elapsed:.1f}s")
    if records:
        print("[+] Upserting SQLite cross-reference DB...")
        build_db(records, full_rebuild=args.force and not args.pkg)
        save_mtimes(records)
        print(f"[+] Writing report to {REPORT_PATH}")
        write_report(records, elapsed)
    else:
        print("[+] Nothing to process (all files up to date).")
    print("[+] Done.")


if __name__ == "__main__":
    main()
