#!/usr/bin/env python3
"""
Extract structured application profiles from the VistA Monograph markdown.

Reads:  ~/data/vista-docs/markdown/MON/vista-monograph-july-2023.md
Writes: ~/data/vista-docs/survey/monograph_apps.csv
        ~/data/vista-docs/survey/monograph_apps.json

Each of the ~187 application entries under "### The VistA Modules" is parsed
into 14 fields using a line-by-line state machine keyed on bold field labels.
"""

from __future__ import annotations

import csv
import html
import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

MARKDOWN = Path.home() / "data/vista-docs/markdown/MON/vista-monograph-july-2023.md"
OUTPUT_DIR = Path.home() / "data/vista-docs/survey"

# ---------------------------------------------------------------------------
# Field definitions  (output key → regex that matches the bold label line)
# ---------------------------------------------------------------------------

_FIELDS: list[tuple[str, re.Pattern]] = [
    ("vista_package_name", re.compile(r"^\*\*VistA Package Name:\*\*\s*(.*)")),
    ("vasi_name", re.compile(r"^\*\*VASI Name:\*\*\s*(.*)")),
    ("vasi_id", re.compile(r"^\*\*VASI ID:\*\*\s*(.*)")),
    ("vasi_status", re.compile(r"^\*\*VASI System Status:\*\*\s*(.*)")),
    ("version", re.compile(r"^\*\*Version:\*\*\s*(.*)")),
    ("namespace", re.compile(r"^\*\*Namespace:\*\*\s*(.*)")),
    ("spm_product_line", re.compile(r"^\*\*SPM Product Line:\*\*\s*(.*)")),
    ("brief_description", re.compile(r"^\*\*Brief Description:\*\*\s*(.*)")),
    ("vasi_link", re.compile(r"^\*\*VASI ID link:\*\*\s*(.*)")),
    ("vdl_link", re.compile(r"^\*\*VDL link:\*\*\s*(.*)")),
    (
        "business_functions",
        re.compile(
            r"^\*\*VHA Business Function Framework Line\(s\) of Business and Function\(s\):\*\*\s*(.*)"
        ),
    ),
    ("business_owner", re.compile(r"^\*\*VHA Business Owner:\*\*\s*(.*)")),
    ("full_description", re.compile(r"^\*\*Full Description and Features:\*\*\s*(.*)")),
]

_FIELD_KEYS = [k for k, _ in _FIELDS]
_LABEL_RE = re.compile(r"^\*\*[A-Z]")  # quick pre-filter: starts with **[A-Z]
_MD_LINK_RE = re.compile(r"\[.*?\]\((https?://[^)]+)\)")  # extract URL from [text](url)
_BOLD_WRAP_RE = re.compile(r"^\*\*(.*?)\*\*$")  # **value** → value
_UNICODE_ZERO_WIDTH = re.compile(r"[\u200b\u200c\u200d\ufeff\u00a0]")


# ---------------------------------------------------------------------------
# Cleaning helpers
# ---------------------------------------------------------------------------


def _clean(text: str) -> str:
    """Decode HTML entities, strip zero-width chars, collapse whitespace."""
    text = html.unescape(text)
    text = _UNICODE_ZERO_WIDTH.sub("", text)
    return text.strip()


def _clean_field(key: str, raw: str) -> str:
    """Field-specific post-processing."""
    raw = _clean(raw)

    if key == "vdl_link":
        m = _MD_LINK_RE.search(raw)
        return m.group(1) if m else ""

    if key == "vasi_link":
        # REDACTED or Not Applicable → empty
        if raw.upper() in ("REDACTED", "NOT APPLICABLE", "NA", "N/A"):
            return ""
        m = _MD_LINK_RE.search(raw)
        return m.group(1) if m else raw

    # Strip **value** wrapper (business_owner sometimes has this)
    m = _BOLD_WRAP_RE.match(raw)
    if m:
        raw = m.group(1)

    return raw


# ---------------------------------------------------------------------------
# Section extraction
# ---------------------------------------------------------------------------


def _modules_lines(text: str) -> list[str]:
    """Return only the lines in the '### The VistA Modules' section."""
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.strip() == "### The VistA Modules":
            start = i + 1
            break
    if start is None:
        raise ValueError("Could not find '### The VistA Modules' heading")
    return lines[start:]


# ---------------------------------------------------------------------------
# Block splitting
# ---------------------------------------------------------------------------


def _split_blocks(lines: list[str]) -> list[tuple[str, list[str]]]:
    """
    Split module lines into per-application blocks.

    Returns list of (app_name, block_lines) where block_lines is everything
    after the #### heading up to (but not including) the next #### heading.
    """
    blocks: list[tuple[str, list[str]]] = []
    current_name: str | None = None
    current_lines: list[str] = []

    for line in lines:
        if line.startswith("#### "):
            if current_name is not None:
                blocks.append((current_name, current_lines))
            current_name = _clean(line[5:])
            current_lines = []
        elif current_name is not None:
            current_lines.append(line)

    if current_name is not None:
        blocks.append((current_name, current_lines))

    return blocks


# ---------------------------------------------------------------------------
# Per-block field extraction
# ---------------------------------------------------------------------------


def _parse_block(app_name: str, lines: list[str]) -> dict:
    """Extract all fields from a single application block."""
    record: dict[str, list[str]] = {k: [] for k in _FIELD_KEYS}
    current_key: str | None = None

    for line in lines:
        # Quick pre-filter before running all regexes
        if _LABEL_RE.match(line):
            matched = False
            for key, pattern in _FIELDS:
                m = pattern.match(line)
                if m:
                    current_key = key
                    first_value = m.group(1).strip()
                    if first_value:
                        record[current_key].append(first_value)
                    matched = True
                    break
            if matched:
                continue

        if current_key is not None:
            record[current_key].append(line)

    # Assemble each field: join accumulated lines, clean
    result: dict[str, str] = {"app_name": app_name}
    for key in _FIELD_KEYS:
        raw_lines = record[key]
        # Strip trailing blank lines
        while raw_lines and not raw_lines[-1].strip():
            raw_lines.pop()
        raw = "\n".join(raw_lines).strip()
        result[key] = _clean_field(key, raw)

    return result


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

COLUMNS = ["app_name"] + _FIELD_KEYS


def extract(markdown_path: Path) -> list[dict]:
    text = markdown_path.read_text(encoding="utf-8")
    module_lines = _modules_lines(text)
    blocks = _split_blocks(module_lines)
    return [_parse_block(name, lines) for name, lines in blocks]


def write_csv(records: list[dict], path: Path) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(records)


def write_json(records: list[dict], path: Path) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)


def report(records: list[dict]) -> None:
    print(f"Extracted {len(records)} application profiles\n")

    # Fields with no data at all (likely parsing miss)
    for key in _FIELD_KEYS:
        empty = sum(1 for r in records if not r[key])
        if empty:
            pct = empty / len(records) * 100
            print(f"  {key:30s}  {empty:3d} empty ({pct:.0f}%)")

    # Spot-check namespace fill
    with_ns = sum(1 for r in records if r["namespace"] not in ("", "Not Applicable", "NA"))
    print(f"\n  Namespace filled: {with_ns}/{len(records)}")

    vdl_filled = sum(1 for r in records if r["vdl_link"])
    print(f"  VDL link filled:  {vdl_filled}/{len(records)}")


if __name__ == "__main__":
    if not MARKDOWN.exists():
        print(f"ERROR: markdown file not found: {MARKDOWN}", file=sys.stderr)
        sys.exit(1)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    records = extract(MARKDOWN)
    report(records)

    csv_path = OUTPUT_DIR / "monograph_apps.csv"
    json_path = OUTPUT_DIR / "monograph_apps.json"

    write_csv(records, csv_path)
    write_json(records, json_path)

    print(f"\nWrote {csv_path}")
    print(f"Wrote {json_path}")
