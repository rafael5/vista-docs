# vista-docs

Pilot modernization of the VA VistA Documentation Library (VDL) into a
version-controlled, markdown-based document corpus.

## Pilot Packages

| Package | ID | Gap |
|---|---|---|
| CPRS | OR*3.0 | 0 |
| TIU | TIU*1.0 | 2 |
| HL7 | HL*1.6 | 0 |
| ADT | DG*5.3 | 258 |

## Pipeline

```
VDL PDFs/DOCX → fetch.py → raw/
raw/ → ingest.py (Docling) → docs/<package>/document.md
docs/ → Zensical → static site
```

## Setup

```bash
./bootstrap.sh --github-user YOUR_USERNAME
python3 scripts/pilot_manifest.py --inventory scripts/vdl_inventory.csv
python3 scripts/fetch.py --manifest scripts/manifest.json
python3 scripts/ingest.py --manifest scripts/manifest.json --base-only
```

## Document Format

Each base document (`technical-manual.md`, `user-manual.md`, etc.) follows
the canonical format:

1. **YAML frontmatter** — package metadata, patch levels, currency status
2. **Base document body** — converted from VDL source, stable canonical reference
3. **Patch History section** — append-only changelog; `[VDL]` | `[FORUM]` | `[UNDOCUMENTED]`

The git commit history mirrors the Patch History section — one commit per patch.
