"""
enrich_inventory.py

Produces vdl_inventory_enriched.csv from vdl_inventory.csv.

Fields added / derived:

Patch Identity:
  pkg_ns           — VistA package namespace (e.g. DG, IB, PSJ)
  patch_ver        — software version string (e.g. 5.3, 2.0)
  patch_ver_major  — major version as integer (e.g. 5)
  patch_ver_minor  — minor version as integer (e.g. 3); 0 if major-only
  patch_num        — patch number as integer (e.g. 1057)
  patch_id         — canonical VistA patch ID: NS*V*P (patch docs) or NS*V (anchor docs)
  patch_id_full    — full raw prefix for multi-namespace patches (e.g. DG*5.3*554/TIU*1*184)
  multi_ns         — 1 if title contains multiple NS*V*P segments (slash-separated)

Document Identity:
  doc_code         — normalized doc type abbreviation (e.g. RN, TM, DIBR)
  doc_label        — canonical doc type full label (e.g. Release Notes)
  doc_layer        — anchor | patch | plain (structural role in functional group)
  doc_subject      — qualifier/subject stripped from title (e.g. ADT, Agent Cashier)
  doc_format       — file format without dot: pdf | docx | doc  (replaces doc_file_ext)

App / Section:
  app_name_abbrev  — app identifier extracted from app_name parens; fallback map applied
  section_code     — short section code (CLI, FIN, GUI, INF, MON)
  group_key        — functional group identifier: app_name_abbrev:pkg_ns:patch_ver

Flags:
  noise_type       — '' = genuine VistA doc | 'vba_form' = VBA benefits form |
                     'va_ref' = non-VistA VA reference doc (e.g. strategic plan)

URLs:
  companion_url    — URL of the paired format (PDF↔DOCX); empty if no pair; listed after doc_url

Source field renames (in-place):
  filename   → doc_filename
  file_ext   → doc_file_ext
  app_name   → app_name_full  (abbrev stripped out)

Source fields dropped:
  doc_type, doc_date, app_code

Usage:
  python3 enrich_inventory.py
"""

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse

INPUT_CSV  = Path("/home/rafael/data/vista-docs/inventory/vdl_inventory.csv")
OUTPUT_CSV = Path("/home/rafael/data/vista-docs/inventory/vdl_inventory_enriched.csv")
SCHEMA_JSON = Path("/home/rafael/data/vista-docs/inventory/vdl_inventory_schema.json")

# ---------------------------------------------------------------------------
# Section code map
# ---------------------------------------------------------------------------
SECTION_CODE = {
    'Clinical':                                        'CLI',
    'Financial-Administrative':                        'FIN',
    'VistA/GUI Hybrids (formerly HealtheVet)':         'GUI',
    'Infrastructure':                                  'INF',
    'Monograph':                                       'MON',
}

# ---------------------------------------------------------------------------
# app_name_abbrev fallback — for VDL apps that never had a parenthetical code.
# These are derived (not VDL-assigned); keyed on app_name_full after parens stripped.
# ---------------------------------------------------------------------------
APP_ABBREV_FALLBACK = {
    'CPRS: Clinical Reminder Updates':                                          'PXRM',
    'KAAJEE':                                                                   'KAAJEE',
    'KAAJEE (XU and XWB)':                                                      'KAAJEE',
    'HL7 (VistA Messaging)':                                                    'HL7',
    'Laboratory: Universal Interface':                                          'LA',
    'Laboratory (LA and LR)':                                                   'LR',
    'Laboratory: Anatomic Pathology':                                           'LR',
    'Laboratory: Blood Bank':                                                   'LR',
    'Laboratory: Blood Bank Workarounds':                                       'LR',
    'Laboratory: Howdy Computerized Phlebotomy Login Process':                  'LR',
    'Laboratory: National Laboratory Tests (NLT) Documents and LOINC Request Form': 'LR',
    'Patient Record Flags':                                                     'PRF',
    'Home Telehealth':                                                          'DHT',
    'HDR - Historical (HDR-Hx)':                                                'HDR',
    'Release of Information (ROI) Manager':                                     'ROI',
    'Registries':                                                               'ONCO',
    'Intake and Output':                                                        'GMR',
    'Duplicate Record Merge: Patient Merge':                                    'MPIF',
    'Diagnostic Related Group (DRG) Grouper':                                   'DRG',
    'Person Services':                                                          'MPI',
    'Health Management Platform':                                               'HMP',
    'Quality Management Integration Module':                                    'QMIM',
    'Decision Support System (DSS) Extracts':                                   'ECX',
    'Group Notes':                                                              'OR',
    'SlotMaster (Kernel ZSLOT)':                                                'ZSLOT',
    'VHA Point of Service (Kiosks)':                                            'VPS',
    'Pharmacy: API':                                                            'PSA',
    'RAI/MDS':                                                                  'RMDS',
    'Veterans Health Information Exchange (VHIE) Portal':                       'VHIE',
    'CPRS: Bulk Parameter Editor for Notifications':                            'OR',
    'Name Standardization':                                                     'XOB',
    'Health Data Informatics':                                                  'HDI',
    'Health Data  Informatics':                                                 'HDI',
    'Standard Files and Tables':                                                'HL',
    'List Manager':                                                             'VALM',
    'M-to-M Broker':                                                            'XWB',
    'XML Parser (VistA)':                                                       'MXML',
    'ICD-9-CM':                                                                 'ICD',
    'WebHR':                                                                    'WEBHR',
    'Electronic Wait List':                                                     'SD',
    'Single Signon/User Context (SSO/UC) (XU and XWB)':                        'SSO',
    'Remote Procedure Call (RPC) Broker':                                       'XWB',
    'Monograph':                                                                'MON',
}

# ---------------------------------------------------------------------------
# decommission_date normalization — "MMM YYYY" → "YYYY-MM"
# ---------------------------------------------------------------------------
MONTH_MAP = {
    'JAN': '01', 'FEB': '02', 'MAR': '03', 'APR': '04',
    'MAY': '05', 'JUN': '06', 'JUL': '07', 'AUG': '08',
    'SEP': '09', 'OCT': '10', 'NOV': '11', 'DEC': '12',
}
DATE_RE = re.compile(r'^([A-Za-z]{3})\s+(\d{4})$')


def normalize_date(raw):
    """'DEC 2019' → '2019-12'; returns raw unchanged if unrecognised."""
    if not raw:
        return ''
    m = DATE_RE.match(raw.strip())
    if m:
        mon = MONTH_MAP.get(m.group(1).upper())
        if mon:
            return f"{m.group(2)}-{mon}"
    return raw


# ---------------------------------------------------------------------------
# patch_ver split
# ---------------------------------------------------------------------------

def split_patch_ver(ver_str):
    """Return (major_int, minor_int) from version string like '5.3', '3', '1.10'."""
    if not ver_str:
        return '', ''
    parts = ver_str.split('.')
    try:
        major = int(parts[0])
        minor = int(parts[1]) if len(parts) > 1 else 0
        return str(major), str(minor)
    except ValueError:
        return '', ''


# ---------------------------------------------------------------------------
# noise_type classification
# ---------------------------------------------------------------------------

def classify_noise(url):
    """Return noise_type for a shared (repeated) URL."""
    p = urlparse(url)
    netloc = p.netloc.lower()
    if netloc in ('www.vba.va.gov', 'vba.va.gov',
                  'www.benefits.va.gov', 'benefits.va.gov'):
        return 'vba_form'
    if '/vdl/' not in p.path:
        return 'va_ref'
    return ''  # within VDL but somehow shared — treat as genuine


# ---------------------------------------------------------------------------
# Doc type vocabulary — ordered most-specific first.
# Each entry: (regex pattern, doc_code, canonical doc_label)
# Matched against the portion of the title after the patch/version prefix.
# ---------------------------------------------------------------------------
DOC_TYPE_PATTERNS = [
    # DIBR variants — must come before generic "Installation Guide"
    (r'Deployment[,\s]+Installation[,\s]+Back.?Out[,\s]+and[,\s]+Rollback', 'DIBR',
     'Deployment, Installation, Back-Out, and Rollback Guide'),
    (r'Deploy.*Install.*(?:Rollback|Back.?Out)',                             'DIBR',
     'Deployment, Installation, Back-Out, and Rollback Guide'),
    (r'\bDIBRG?\b|\bDIRB\b',                                                 'DIBR',
     'Deployment, Installation, Back-Out, and Rollback Guide'),

    # Setup / Configuration — before generic "Guide"
    (r'Set\s*[Uu]p\s+and\s+Config(?:uration)?\s+Guide', 'CFG', 'Setup and Configuration Guide'),
    (r'Config(?:uration)?\s+Guide',                      'CFG', 'Configuration Guide'),

    # Quick Reference — before generic "Guide"
    (r'Quick\s+Reference\s+(?:Guide|Card)', 'QRG', 'Quick Reference Guide'),

    # IG variants
    (r'Implementation\s+Guide',              'IG-IMP', 'Implementation Guide'),
    (r'Install(?:ation)?\s+(?:and\s+)?(?:Configuration\s+)?Guide', 'IG', 'Installation Guide'),
    (r'Install(?:ation)?\s+Manual',          'IG',     'Installation Guide'),
    (r'Install\s+Deploy\s+Guide',            'IG',     'Installation Guide'),

    # User docs
    (r'User\s+Manual',                       'UM',  'User Manual'),
    (r'User\s+Guide',                        'UG',  'User Guide'),
    (r'(?:Manager|Supervisor|ADPAC)\s+(?:Manual|Guide)', 'UG', 'Manager/ADPAC Guide'),
    (r'Clinical\s+Coordinator\s+Manual',     'UM',  'Clinical Coordinator Manual'),

    # Technical docs
    (r'Technical\s+Manual',                  'TM',  'Technical Manual'),
    (r'Technical\s+Guide',                   'TG',  'Technical Guide'),
    (r'API\s+Manual',                        'API', 'API Manual'),

    # Interface / integration specs
    (r'(?:HL7\s+)?Interface\s+(?:Document|Specification|Spec)', 'INT', 'Interface Specification'),
    (r'Interface\s+Toolkit',                 'REF', 'Interface Toolkit'),
    (r'Feed\s+Guide',                        'INT', 'Interface Feed Guide'),

    # Security / ops
    (r'Security\s+Guide',                    'SG',  'Security Guide'),
    (r'Security\s+Manual',                   'SG',  'Security Guide'),
    (r'Production\s+Operations\s+Manual',    'POM', 'Production Operations Manual'),
    (r'Setup\s+Guide',                       'SG-SET', 'Setup Guide'),

    # Release / version docs
    (r'Release\s+Notes',                     'RN',  'Release Notes'),
    (r'Patch\s+Description',                 'PDD', 'Patch Description Document'),
    (r'Version\s+Description\s+Document',    'VDD', 'Version Description Document'),
    (r'Description\s+Document',              'DESC', 'Description Document'),

    # Clinical Reminder Updates
    (r'Clinical\s+Reminder\s+Update',        'CRU', 'Clinical Reminder Update'),

    # Conversion / migration
    (r'Conversion\s+Guide',                  'CVG', 'Conversion Guide'),

    # Reference
    (r'Frequently\s+Asked\s+Questions',      'FAQ', 'Frequently Asked Questions'),
    (r'\bAppendix\b',                        'APX', 'Appendix'),
    (r'Training\s+Guide',                    'TRG', 'Training Guide'),
    (r'Training\s+Manual',                   'TRG', 'Training Manual'),
    (r'(?:Quick\s+)?Reference\s+(?:Card|Guide|Manual)', 'REF', 'Reference'),
    (r'(?:Information\s+)?Flowchart',        'REF', 'Reference'),

    # VA forms
    (r'^\d{2}[–\-]\d+',                     'FORM', 'VBA Form'),
    (r'^(?:VA|VBA|SF)\d',                    'FORM', 'VBA Form'),
    (r'(?:Application|Form)\s+\d{2}-\d+',   'FORM', 'VBA Form'),
]

# Pre-compile
DOC_TYPE_COMPILED = [
    (re.compile(pat, re.IGNORECASE), code, label)
    for pat, code, label in DOC_TYPE_PATTERNS
]

# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

# Pattern A: DG*5.3*1057 Deployment...
PATCH_A = re.compile(
    r'^(?:[A-Za-z ]+\s)?'           # optional prefix text (e.g. "CPRS ")
    r'([A-Z][A-Z0-9]+)'             # namespace
    r'\*([\d]+(?:\.[\d]+)?)'        # version (major or major.minor)
    r'\*(\d+)'                      # patch number (first one if multi-patch)
    r'(?:/\d+)*'                    # optional additional patches /NNN
    r'\s*(.*)',                      # remainder = doc type + subject
    re.DOTALL
)

# Full multi-namespace prefix capture: NS*V*P/NS*V*P/...
PATCH_FULL = re.compile(
    r'^(?:[A-Za-z ]+\s)?'
    r'([A-Z][A-Z0-9]+\*[\d.]+\*\d+'
    r'(?:/[A-Z][A-Z0-9]+\*[\d.]+\*\d+)*)',
    re.DOTALL
)

# Multi-namespace detector: slash between two NS*V*P segments
MULTI_NS_RE = re.compile(
    r'[A-Z][A-Z0-9]+\*[\d.]+\*\d+/[A-Z][A-Z0-9]+\*'
)

# Pattern B: PIMS Version 5.3 ADT Technical Manual
PATCH_B = re.compile(r'[Vv]ersion\s+([\d]+\.[\d]+)\b')

# Version-only in doc_filename: appcode_major_minor_...
FNAME_VER = re.compile(r'^[a-z0-9]+_(\d+)_(\d+)', re.IGNORECASE)

# p-prefixed patch in doc_filename: ..._p1064_... or ..._1064_...
FNAME_PATCH = re.compile(r'_p?(\d{3,5})_', re.IGNORECASE)


def classify_doc_type(text):
    """Return (doc_code, doc_label) for the best match in text, or ('', '') if none."""
    for pattern, code, label in DOC_TYPE_COMPILED:
        if pattern.search(text):
            return code, label
    return '', ''


def extract_subject(title, patch_prefix, doc_label):
    """
    Strip patch_prefix and doc_label from title; what remains is the subject.
    """
    remainder = title
    if patch_prefix:
        remainder = remainder[len(patch_prefix):].strip()
    if doc_label:
        remainder = re.sub(re.escape(doc_label), '', remainder, flags=re.IGNORECASE).strip()
    remainder = re.sub(
        r'Deployment[,\s]+Installation[,\s]+Back.?Out[,\s]+and[,\s]+Rollback\s*Guide?',
        '', remainder, flags=re.IGNORECASE).strip()
    remainder = re.sub(r'^[\s\-–—:,]+|[\s\-–—:,]+$', '', remainder)
    return remainder


# ---------------------------------------------------------------------------
# doc_subject cleaning — strip artifact values, keep genuine qualifiers
# ---------------------------------------------------------------------------

_BARE_YEAR_RE      = re.compile(r'^\d{4}$')
_BARE_VERSION_RE   = re.compile(r'^[\d.]+$')
_BARE_PUNCT_RE     = re.compile(r'^[*\s,\-]+$')
_PATCH_ARTIFACT_RE = re.compile(r'^\*\d+')
_PATCH_ID_RE       = re.compile(r'^[A-Z][A-Z0-9]+\*[\d.]+\*\d+(?:/[A-Z][A-Z0-9]+\*[\d.]+\*\d+)*$')


def clean_doc_subject(subject, app_abbrev, doc_title, doc_label):
    """
    Remove artifact values from doc_subject; return cleaned string (may be '').

    Rules applied in order (first match clears the value):
    1. Equals app_name_abbrev (case-insensitive)  — redundant app echo
    2. Equals doc_title (full title echo)
    3. Equals doc_label exactly                   — redundant type echo
    4. Starts with '/'                            — multi-NS title continuation fragment
    5. Bare 4-digit year
    6. Bare digits/dots only                      — version fragment (.01, 2.0)
    7. Pure punctuation / whitespace
    8. Starts with *digits                        — patch artifact
    9. Entirely a NS*V*P (or NS*V*P/NS*V*P) pattern — patch ID residue
    10. Length <= 2 AND no alphabetic characters  — clears '.1' but keeps 'AP', 'IO'
    """
    if not subject:
        return ''
    s = subject.strip()
    if not s:
        return ''
    if app_abbrev and s.upper() == app_abbrev.upper():
        return ''
    if s == doc_title:
        return ''
    if doc_label and s == doc_label:
        return ''
    if s.startswith('/'):
        return ''
    if _BARE_YEAR_RE.match(s):
        return ''
    if _BARE_VERSION_RE.match(s):
        return ''
    if _BARE_PUNCT_RE.match(s):
        return ''
    if _PATCH_ARTIFACT_RE.match(s):
        return ''
    if _PATCH_ID_RE.match(s):
        return ''
    if len(s) <= 2 and not any(c.isalpha() for c in s):
        return ''
    return s


# ---------------------------------------------------------------------------
# doc_slug — stable URL-safe document identifier
# ---------------------------------------------------------------------------

_SLUG_NON_ALNUM = re.compile(r'[^a-z0-9]+')


def make_doc_slug(doc_filename):
    """Return URL-safe slug: Path(doc_filename).stem lowercased, non-alnum → '_'."""
    stem = Path(doc_filename).stem
    return _SLUG_NON_ALNUM.sub('_', stem.lower()).strip('_')


# ---------------------------------------------------------------------------

ABBR_RE = re.compile(r'\s*\(([A-Z0-9/+\-]{1,10})\)\s*$')


def parse_row(row):
    """Return dict of enrichment fields for a single CSV row."""
    title        = row['doc_title'].strip()
    doc_filename = row['doc_filename'].strip()
    app_code     = row.get('app_name_abbrev', '').strip() or (
        m.group(1) if (m := ABBR_RE.search(row.get('app_name_full', ''))) else ''
    )

    vista_pkg_ns  = ''
    patch_ver     = ''
    patch_num     = ''
    doc_code      = ''
    doc_label     = ''
    doc_subj      = ''
    patch_prefix  = ''
    patch_id_full = ''
    multi_ns      = '0'

    # --- Multi-namespace detection ---
    if MULTI_NS_RE.search(title):
        multi_ns = '1'
        mf = PATCH_FULL.match(title)
        if mf:
            patch_id_full = mf.group(1)

    # --- Patch Identity ---
    m = PATCH_A.match(title)
    if m:
        vista_pkg_ns = m.group(1)
        patch_ver    = m.group(2)
        patch_num    = str(int(m.group(3)))
        remainder    = m.group(4).strip()
        patch_prefix = f"{vista_pkg_ns}*{patch_ver}*{m.group(3)}"
        doc_code, doc_label = classify_doc_type(remainder)
        doc_subj = extract_subject(remainder, '', doc_label)

    else:
        m_ver = PATCH_B.search(title)
        if m_ver:
            patch_ver    = m_ver.group(1)
            vista_pkg_ns = app_code
            version_end  = m_ver.end()
            remainder_b  = title[version_end:].strip()
        else:
            remainder_b = title
            m_fn = FNAME_VER.match(doc_filename.lower())
            if m_fn:
                patch_ver    = f"{m_fn.group(1)}.{m_fn.group(2)}"
                vista_pkg_ns = app_code

        if not patch_num:
            m_fp = FNAME_PATCH.search(doc_filename)
            if m_fp:
                patch_num = str(int(m_fp.group(1)))

        doc_code, doc_label = classify_doc_type(title)
        doc_subj = extract_subject(remainder_b, '', doc_label)

    # --- VBA Form override ---
    if re.match(r'^\d{2}[–\-]\d+', title) or re.match(r'^(?:VBA|SF)\d', doc_filename, re.IGNORECASE):
        doc_code     = 'FORM'
        doc_label    = 'VBA Form'
        doc_subj     = re.sub(r'^[\d–\-]+\s*[–\-—]\s*', '', title).strip()
        vista_pkg_ns = patch_ver = patch_num = ''

    return {
        'vista_pkg_ns':  vista_pkg_ns,
        'patch_ver':     patch_ver,
        'patch_num':     patch_num,
        'doc_code':      doc_code,
        'doc_label':     doc_label,
        'doc_subject':   doc_subj,
        'patch_id_full': patch_id_full,
        'multi_ns':      multi_ns,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    with open(INPUT_CSV, newline='', encoding='utf-8') as f_in:
        reader = csv.DictReader(f_in)
        rows = list(reader)

    # --- Pass 1: per-row rename, extract, parse ---
    enriched = []
    for row in rows:
        if 'filename' in row:
            row['doc_filename'] = row.pop('filename')
        if 'file_ext' in row:
            row['doc_file_ext'] = row.pop('file_ext')

        m = ABBR_RE.search(row['app_name'])
        row['app_name_abbrev'] = m.group(1) if m else ''
        if m:
            row['app_name'] = ABBR_RE.sub('', row['app_name']).strip()
        row['app_name_full'] = row.pop('app_name')

        parsed = parse_row(row)
        parsed['pkg_ns'] = parsed.pop('vista_pkg_ns')
        enriched.append({**row, **parsed})

    # --- Pass 2: global enrichment ---

    # Shared URLs → noise_type
    url_counts = Counter(r['doc_url'] for r in enriched)
    shared_urls = {u for u, c in url_counts.items() if c > 1}

    # Companion URLs: group by base URL (without extension)
    base_to_urls = defaultdict(dict)  # base → {ext: full_url}
    for r in enriched:
        url = r['doc_url']
        if '.' in url.split('/')[-1]:
            base = url.rsplit('.', 1)[0]
            ext  = '.' + url.rsplit('.', 1)[1].lower()
        else:
            base = url
            ext  = ''
        base_to_urls[base][ext] = url

    for row in enriched:
        # app_name_abbrev fallback
        if not row['app_name_abbrev']:
            row['app_name_abbrev'] = (
                APP_ABBREV_FALLBACK.get(row['app_name_full'], '')
                or row['pkg_ns']
            )

        # doc_subject — strip artifact values (must run after app_name_abbrev is final)
        row['doc_subject'] = clean_doc_subject(
            row.get('doc_subject', ''),
            row['app_name_abbrev'],
            row['doc_title'],
            row.get('doc_label', ''),
        )

        # section_code
        row['section_code'] = SECTION_CODE.get(row['section_name'], '')

        # decommission_date → YYYY-MM
        row['decommission_date'] = normalize_date(row['decommission_date'])

        # patch_ver_major / patch_ver_minor
        row['patch_ver_major'], row['patch_ver_minor'] = split_patch_ver(row['patch_ver'])

        # doc_layer
        has_ver = bool(row['patch_ver'])
        has_num = bool(row['patch_num'])
        if has_ver and not has_num:
            row['doc_layer'] = 'anchor'
        elif has_num:
            row['doc_layer'] = 'patch'
        else:
            row['doc_layer'] = 'plain'

        # patch_id — canonical NS*V*P or NS*V
        ns, ver, num = row['pkg_ns'], row['patch_ver'], row['patch_num']
        if ns and ver and num:
            row['patch_id'] = f"{ns}*{ver}*{num}"
        elif ns and ver:
            row['patch_id'] = f"{ns}*{ver}"
        else:
            row['patch_id'] = ''

        # doc_format — extension without dot
        ext = row['doc_file_ext']
        row['doc_format'] = ext.lstrip('.') if ext else ''

        # group_key — functional group identifier (only when version is known)
        if row['patch_ver']:
            row['group_key'] = f"{row['app_name_abbrev']}:{row['pkg_ns']}:{row['patch_ver']}"
        else:
            row['group_key'] = ''

        # noise_type
        if row['doc_url'] in shared_urls:
            row['noise_type'] = classify_noise(row['doc_url'])
        else:
            row['noise_type'] = ''

        # companion_url — paired format URL
        url = row['doc_url']
        if '.' in url.split('/')[-1]:
            base = url.rsplit('.', 1)[0]
            ext  = '.' + url.rsplit('.', 1)[1].lower()
        else:
            base, ext = url, ''

        pairs = base_to_urls.get(base, {})
        companion = ''
        for other_ext, other_url in pairs.items():
            if other_ext != ext:
                companion = other_url
                break
        row['companion_url'] = companion

        # doc_slug — stable URL-safe document identifier (PDF/DOCX pairs share slug)
        row['doc_slug'] = make_doc_slug(row['doc_filename'])

    # --- Output column order (27 columns) ---
    out_fields = [
        'section_name', 'section_code',
        'app_name_full', 'app_name_abbrev', 'app_status', 'decommission_date',
        'pkg_ns', 'patch_ver', 'patch_ver_major', 'patch_ver_minor', 'patch_num',
        'patch_id', 'patch_id_full', 'multi_ns',
        'group_key',
        'doc_code', 'doc_label', 'doc_layer',
        'doc_title', 'doc_filename', 'doc_slug', 'doc_format', 'doc_subject',
        'noise_type',
        'app_url', 'doc_url', 'companion_url',
    ]

    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f_out:
        writer = csv.DictWriter(f_out, fieldnames=out_fields, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(enriched)

    # --- Schema JSON ---
    schema = {
        "description": "Field type manifest for vdl_inventory_enriched.csv",
        "generated": "2026-03-23",
        "row_count": len(enriched),
        "fields": {
            "section_name":      {"type": "string",   "category": "section",  "nullable": False},
            "section_code":      {"type": "string",   "category": "section",  "nullable": False,
                                  "values": ["CLI", "FIN", "GUI", "INF", "MON"]},
            "app_name_full":     {"type": "string",   "category": "app",      "nullable": False},
            "app_name_abbrev":   {"type": "string",   "category": "app",      "nullable": False},
            "app_status":        {"type": "string",   "category": "app",      "nullable": False,
                                  "values": ["active", "archive", "decommissioned"]},
            "decommission_date": {"type": "string",   "category": "app",      "nullable": True,
                                  "format": "YYYY-MM"},
            "pkg_ns":            {"type": "string",   "category": "patch",    "nullable": True},
            "patch_ver":         {"type": "string",   "category": "patch",    "nullable": True,
                                  "note": "Do not sort as string — use patch_ver_major/minor"},
            "patch_ver_major":   {"type": "integer",  "category": "patch",    "nullable": True},
            "patch_ver_minor":   {"type": "integer",  "category": "patch",    "nullable": True},
            "patch_num":         {"type": "integer",  "category": "patch",    "nullable": True},
            "patch_id":          {"type": "string",   "category": "patch",    "nullable": True,
                                  "format": "NS*V*P (patch) or NS*V (anchor)"},
            "patch_id_full":     {"type": "string",   "category": "patch",    "nullable": True,
                                  "note": "Full multi-NS prefix e.g. DG*5.3*554/TIU*1*184; set only when multi_ns=1"},
            "multi_ns":          {"type": "boolean",  "category": "patch",    "nullable": False,
                                  "storage": "0/1 string in CSV"},
            "group_key":         {"type": "string",   "category": "patch",    "nullable": True,
                                  "format": "app_name_abbrev:pkg_ns:patch_ver"},
            "doc_code":          {"type": "string",   "category": "document", "nullable": True},
            "doc_label":         {"type": "string",   "category": "document", "nullable": True},
            "doc_layer":         {"type": "string",   "category": "document", "nullable": False,
                                  "values": ["anchor", "patch", "plain"]},
            "doc_title":         {"type": "string",   "category": "document", "nullable": False},
            "doc_filename":      {"type": "string",   "category": "document", "nullable": False,
                                  "note": "Web document filename — not a VistA FileMan file"},
            "doc_slug":          {"type": "string",   "category": "document", "nullable": False,
                                  "note": "URL-safe stable identifier from filename stem (lowercase, non-alnum→'_'); PDF/DOCX pairs share slug"},
            "doc_format":        {"type": "string",   "category": "document", "nullable": False,
                                  "values": ["pdf", "docx", "doc"],
                                  "note": "file format without dot — replaces doc_file_ext; use for YAML frontmatter"},
            "doc_subject":       {"type": "string",   "category": "document", "nullable": True,
                                  "note": "Derived from doc_title; best-effort only"},
            "noise_type":        {"type": "string",   "category": "flag",     "nullable": False,
                                  "values": ["", "vba_form", "va_ref"],
                                  "note": "Exclude non-empty values from VistA documentation analysis"},
            "companion_url":     {"type": "string",   "category": "url",      "nullable": True,
                                  "note": "URL of paired format (PDF↔DOCX); empty if no pair exists"},
            "app_url":           {"type": "string",   "category": "url",      "nullable": False},
            "doc_url":           {"type": "string",   "category": "url",      "nullable": False},
        }
    }

    with open(SCHEMA_JSON, 'w', encoding='utf-8') as f:
        json.dump(schema, f, indent=2)

    # --- Summary report ---
    total  = len(enriched)
    active = [r for r in enriched if r['app_status'] == 'active' and not r['noise_type']]

    def pct(n, d=total):
        return f"{n}  ({100*n/d:.1f}%)"

    print(f"Total rows          : {total}")
    print(f"  active + clean    : {len(active)}")
    print()
    print(f"pkg_ns filled       : {pct(sum(1 for r in enriched if r['pkg_ns']))}")
    print(f"patch_ver filled    : {pct(sum(1 for r in enriched if r['patch_ver']))}")
    print(f"patch_num filled    : {pct(sum(1 for r in enriched if r['patch_num']))}")
    print(f"patch_id filled     : {pct(sum(1 for r in enriched if r['patch_id']))}")
    print(f"doc_code filled     : {pct(sum(1 for r in enriched if r['doc_code']))}")
    print(f"doc_subject filled  : {pct(sum(1 for r in enriched if r['doc_subject']))}")
    print(f"doc_slug filled     : {pct(sum(1 for r in enriched if r['doc_slug']))}")
    print(f"app_abbrev filled   : {pct(sum(1 for r in enriched if r['app_name_abbrev']))}")
    print(f"companion_url filled: {pct(sum(1 for r in enriched if r['companion_url']))}")
    print(f"group_key filled    : {pct(sum(1 for r in enriched if r['group_key']))}")
    print()

    layer_counts = Counter(r['doc_layer'] for r in enriched)
    noise_counts = Counter(r['noise_type'] for r in enriched)
    multi_ns_count = sum(1 for r in enriched if r['multi_ns'] == '1')
    print(f"doc_layer    : anchor={layer_counts['anchor']}  patch={layer_counts['patch']}  plain={layer_counts['plain']}")
    print(f"noise_type   : vba_form={noise_counts['vba_form']}  va_ref={noise_counts['va_ref']}  clean={noise_counts['']}")
    print(f"multi_ns=1   : {multi_ns_count}")

    no_doc_code = [r['doc_title'] for r in enriched if not r['doc_code'] and not r['noise_type']]
    print(f"\nClean rows with no doc_code: {len(no_doc_code)}")
    print("Sample unresolved titles:")
    seen = set()
    for t in no_doc_code:
        if t not in seen:
            seen.add(t)
            print(f"  {t}")
        if len(seen) >= 15:
            break

    print(f"\nOutput CSV   : {OUTPUT_CSV}  ({len(out_fields)} columns)")
    print(f"Schema JSON  : {SCHEMA_JSON}")


if __name__ == '__main__':
    main()
