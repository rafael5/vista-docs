# VistA Monograph — Provenance, Quality, and Data Validity

**Document analysed:** *VistA Monograph July 2023*
**VA VDL URL:** `https://www.va.gov/vdl/application.asp?appid=239`
**DOCX source:** `https://www.va.gov/vdl/documents/Monograph/Monograph/vista_monograph_0723_r.docx`
**Local markdown:** `~/data/vista-docs/markdown/MON/vista-monograph-july-2023.md`
**Structured extract:** `~/data/vista-docs/survey/monograph_apps.{csv,json}`
**Cross-reference:** `~/data/vista-docs/survey/crossref_monograph.{txt,json}`

---

## 1. What the Monograph Is

The VistA Monograph is a VA-published document that catalogs the ~187 VistA software
packages that make up the VistA electronic health record system. For each package it
provides a structured profile: names, identifiers, namespace, version, status, business
ownership, and descriptions.

It is **not** a technical manual, patch note, or user guide. It functions as a
**registry snapshot** — a point-in-time catalog of what packages exist and who owns them.

---

## 2. Provenance — Almost Certainly a VASI Database Export

Despite being published as a DOCX narrative document, the Monograph's content almost
certainly originates as an automated export from **VASI (VA System Inventory)**, the VA's
internal IT system registry, rather than as a human-authored text.

### Evidence

| Signal | Observation |
|--------|-------------|
| **Structural regularity** | All 187 entries use identical field labels in identical order, without a single deviation. Human authorship of 187+ entries at that consistency level is implausible without a template/generator. |
| **Controlled vocabulary** | `vasi_status` values are always one of `Active`, `Inactive`, `Not A System` — classic database dropdown values. |
| **Uniform VASI link redaction** | Every `**VASI ID link:**` field is `REDACTED`. This is a batch substitution of internal `vaww.` intranet URLs before publication — not 187 individual editorial decisions. |
| **Formulaic descriptions** | `brief_description` and `full_description` text reads like database-entry prose: terse, occasionally incomplete, sometimes mid-sentence truncated. |
| **Machine-parseable** | The document parses cleanly with a simple line-by-line state machine keyed on `**Bold Label:**` patterns — exactly what you'd expect from a templated export. |

### Implication

The Monograph's content quality is bounded by **VASI's data quality at export time
(July 2023)**. Every gap, stale status, or thin description reflects what was in VASI
at that moment, not an editorial oversight.

---

## 3. VASI — The Underlying Registry

VASI is a **manually maintained** human-curated database. There is no API or automated
feed that keeps it current. Each application entry must be created and updated by hand,
typically triggered by formal events: new system registration, IT governance audits,
or budget cycles.

### Failure modes from manual curation

- **Staleness by neglect** — no trigger, no update. A package reactivated after a
  funding gap may remain "Inactive" in VASI indefinitely.
- **Subsystem ambiguity** — whether a package gets its own VASI record vs. being
  subsumed under a parent is a human data entry decision, not a technical fact.
- **Definitional drift** — "Inactive" in VASI means formally deregistered at the
  enterprise level, which may not match operational reality at individual VAMCs.

### Reliability hierarchy (most → least current)

```
1. Patch recency (patch_num in VDL inventory)  — objective, automated
2. VDL page status (active/archive)             — semi-automated, crawled
3. VASI status in Monograph                     — manual snapshot, July 2023
```

---

## 4. Coverage

### What the Monograph covers
- ~187 application entries under `### The VistA Modules`
- Primarily legacy/established packages that were registered in VASI by July 2023
- Packages in active development at VA sites with stable VASI entries

### What it misses
- **47 active VDL inventory apps are absent** — these are newer packages added to VDL
  after the Monograph's VASI snapshot (e.g., Community Care, various registries,
  EHM Platform, Lighthouse, VIA)
- **5 appids exist in the Monograph but not in VDL inventory** — likely decommissioned
  apps whose VDL pages were removed (appids 3, 132, 152, 177, 192)
- **9 Monograph entries link to decommissioned VDL apps** — the VDL page still existed
  at snapshot time but was subsequently archived

---

## 5. Field-by-Field Quality Assessment

| Field | Quality | Notes |
|-------|---------|-------|
| `app_name` (#### heading) | High | Consistent with VDL inventory names (minor formatting differences) |
| `vista_package_name` | High | Generally matches `app_name`; occasional abbreviation differences |
| `vasi_name` | Medium | VASI's own name for the system; may differ from VDL name |
| `vasi_id` | High | Numeric ID; reliable where present |
| `vasi_status` | **Low for currency** | Manual entry, July 2023 snapshot; stale for many active packages |
| `version` | Medium | Reflects version at export time; may not match latest patch |
| `namespace` | Medium | 16 discrepancies vs VDL inventory; some multi-namespace entries |
| `spm_product_line` | Medium | Useful for organizational grouping |
| `brief_description` | Medium | Database text, formulaic but generally accurate |
| `full_description` | Low–Medium | Highly variable length and quality; some very thin |
| `vasi_link` | **Unusable** | 100% REDACTED — internal intranet URLs stripped at publication |
| `vdl_link` | High | 142/187 resolve to active VDL pages; best join key to inventory |
| `business_functions` | Low | Formulaic VHA framework text; low signal for technical analysis |
| `business_owner` | Medium | VHA office attribution; useful for organizational mapping |

---

## 6. VASI Status Conflict Analysis

29 entries are listed as `Inactive` or `Not A System` in the Monograph but appear as
`active` in the VDL inventory. These split cleanly into two categories:

### "Not A System" — subsystems/modules (trust VASI)

VASI made a data entry decision not to register these as independent systems. The parent
package is active and heavily patched. Examples:

- LR sub-modules: Anatomic Pathology, EPI, Electronic Data Interchange, Point of Care
  (all part of `LR*5.2*500` — a very active package)
- Group Notes (`OR*3.0*629`) — a feature of CPRS/OR, not standalone
- VistALink (`XOBV`), XML Parser (`MXML`), Electronic Signature (`XOBE`) — infrastructure
  components deliberately not registered as independent systems

### "Inactive" — VASI is stale (trust VDL + patch count)

These packages have substantial patch histories, indicating continued active deployment
despite VASI showing them as inactive:

| App | Namespace | Max Patch | Assessment |
|-----|-----------|-----------|------------|
| Primary Care Management Module | SD | 620 | Definitely active — VASI very stale |
| Mental Health | YS | 255 | Definitely active |
| PAID | PRS | 133 | Active |
| Kernel Toolkit | XT | 98 | Active infrastructure |
| HINQ | DVB | 49 | Active |
| CCR / HepC | ROR | 42 | Active |

Packages with max_patch = 0 and no recent VDL documents are more credibly inactive
(SlotMaster, Survey Generator, PATS, FFP, IRT, IdM, etc.).

---

## 7. Namespace Discrepancies

16 namespace mismatches were found between the Monograph and VDL enriched inventory.
Notable cases:

| App | Monograph NS | Inventory NS | Explanation |
|-----|-------------|--------------|-------------|
| EDIS | EDP | EDIS | Monograph uses legacy namespace |
| XML Parser | MXML | XT | Kernel subsystem; namespace ambiguity |
| VistALink | XOBV | XOB | Version namespace difference |

Some Monograph entries list multiple namespaces (`A or B`) or use informal descriptions
instead of the actual M namespace prefix.

---

## 8. Name Consistency

86 of 142 matched entries have name differences between the Monograph and VDL inventory.
The majority are minor formatting differences:

- Punctuation: `Pharmacy: Bar Code Medication Administration` vs `Pharmacy - Bar Code...`
- Prefix conventions: `VistA - Laboratory: Anatomic Pathology` vs `Anatomic Pathology`
- Acronym expansion: `CPRS` vs `Computerized Patient Record System`

These are cosmetic and do not indicate data quality problems.

---

## 9. Using the Monograph in Analysis

### Good uses
- **Package enumeration** — the most complete single-source list of established VistA
  packages, with VASI IDs and business ownership
- **Organizational mapping** — SPM product lines and VHA business owners
- **Namespace lookup** — first-pass namespace identification (verify against inventory)
- **Historical baseline** — what the VA formally recognized as VistA as of July 2023

### Poor uses
- **Operational status** — use VDL inventory + patch recency instead
- **Current version** — use latest patch_id from VDL inventory instead
- **Complete coverage** — 47 active packages are absent; supplement with VDL inventory
- **VASI links** — all redacted; useless

### Join key to VDL inventory
```python
# Monograph → Inventory match
monograph["vdl_link"].rstrip("/") == inventory["app_url"].rstrip("/")

# 142/187 entries match this way (76%)
# Remaining 45 = no VDL link (22) + decommissioned (9) + not in inventory (5) + no link (9)
```

---

## 10. Pipeline Notes

- The Monograph has `app_code=""` in the VDL source CSV — it cannot be processed via
  `vista-docs --pkg MON`. Use `ingest_monograph.py` (project root) which calls the
  pipeline functions directly with `app_code="MON"`.
- Structured extraction: `extract_monograph.py` (project root) produces
  `monograph_apps.{csv,json}` with 14 fields per entry.
- Cross-reference analysis: `crossref_monograph.py` (project root) runs 5 validation
  checks against `vdl_inventory_enriched.csv`.
