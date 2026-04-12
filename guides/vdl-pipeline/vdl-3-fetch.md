# VDL Pipeline — Stage 3: Fetch

**Date:** 2026-03-30
**Module:** `vista_docs/fetch/`
**Output:** `~/data/vista-docs/raw/<app_code>/`

---

## Table of Contents

1. [Overview](#1-overview)
2. [Design](#2-design)
3. [Document Selection](#3-document-selection)
4. [Download Mechanics](#4-download-mechanics)
5. [State Tracking](#5-state-tracking)
6. [Problems Encountered and Fixes](#6-problems-encountered-and-fixes)
7. [Lessons Learned](#7-lessons-learned)
8. [Results](#8-results)
9. [Fetch Snapshot as of 2026-03-30](#9-fetch-snapshot-as-of-2026-03-30)

---

## 1. Overview
[↑ Table of Contents](#table-of-contents)

The fetch stage downloads every substantive document in the VDL inventory to local storage. Noise rows (`noise_type != ''`) are skipped. The output is a directory tree of raw PDF and DOCX files, organized by application code, that serves as the input to the ingest stage.

**Input:** `~/data/vista-docs/inventory/vdl_inventory_enriched.csv`
**Output:** `~/data/vista-docs/raw/<app_code>/<filename>` (PDF and DOCX files)

---

## 2. Design
[↑ Table of Contents](#table-of-contents)

The fetch stage is split into:
- **`fetch/selector.py`** — pure; selects which documents to download; resolves DOCX vs PDF preference
- **`fetch/downloader.py`** — I/O; executes HTTP downloads; writes files; updates state

### DOCX Preference

When both a DOCX and a PDF exist for the same document, DOCX is always preferred for download and ingest. DOCX files produce higher-quality markdown because:
- They contain structured XML that Docling can parse with full fidelity
- Tables, headers, and lists are explicitly tagged in the XML
- No OCR is required
- Font and layout artifacts do not interfere with text extraction

The `companion_url` field in `vdl_inventory_enriched.csv` already identifies the paired format for each document. The selector reads this field directly — it does not re-discover pairs by scanning the inventory. The URL of the format not downloaded is recorded in `pipeline.db` as `companion_url` for reference.

### Directory Structure

```
~/data/vista-docs/raw/
├── PSO/
│   ├── pso_7_tm.docx
│   ├── pso_7_407_dibr.docx
│   └── ...
├── ADT/
│   └── ...
└── ...
```

Each directory corresponds to one `app_name_abbrev`. Directory names are lowercase.

---

## 3. Document Selection
[↑ Table of Contents](#table-of-contents)

The fetch stage reads `vdl_inventory_enriched.csv` directly. The enriched inventory already carries `noise_type`, `doc_format`, `companion_url`, and `doc_slug` — fields the fetch stage depends on but does not compute. This means document selection is a pure read-and-filter operation with no classification logic of its own.

`fetch/selector.py` applies the following selection logic:

1. **Skip noise rows** — rows where `noise_type != ''` are excluded (VBA forms and VA reference docs)
2. **Resolve format preference** — the enriched inventory's `companion_url` field identifies DOCX/PDF pairs; DOCX is always preferred
3. **Skip already-fetched** — check `fetch_state` table in `pipeline.db`
4. **Apply `--pkg` filter** — if specified, restrict to one `app_name_abbrev`

The `build_entries_from_rows` function constructs a `ManifestEntry` per document (collapsing DOCX+PDF pairs using `doc_slug` as the deduplication key) before the selector runs. The `doc_slug` field from the enriched inventory is used directly as the stable document identifier in `pipeline.db` — it is not recomputed during fetch.

---

## 4. Download Mechanics
[↑ Table of Contents](#table-of-contents)

### HTTP Session

Downloads use a persistent `requests.Session` configured with:
- Connection pooling (reuses TCP connections for the same host)
- Browser-like `User-Agent` header (some VA servers return 403 to default requests agents)
- `stream=True` for large file downloads (avoids loading entire file into memory)

### Rate Limiting

The VA VDL is a public government website, but bulk downloading without rate limiting risks triggering server-side blocks or degrading service for other users. The downloader inserts a configurable delay between requests. Default: 0.5 seconds between downloads.

### Retry Logic

Transient failures are retried with exponential backoff:
- Maximum 3 retry attempts
- Initial backoff: 2 seconds
- Backoff multiplier: 2× (2s → 4s → 8s)
- Retried on: connection timeout, HTTP 429, HTTP 503, HTTP 502

Persistent failures (HTTP 404, HTTP 403, empty response) are recorded in `pipeline.db` with status `fetch_failed` and not retried automatically.

### File Validation

After each download:
1. File size is checked against `Content-Length` header if provided
2. Zero-byte files are rejected and recorded as `fetch_failed`
3. DOCX files are validated by checking for the PK ZIP magic bytes (`50 4B 03 04`)
4. PDF files are validated by checking for the PDF magic bytes (`25 50 44 46`)

---

## 5. State Tracking
[↑ Table of Contents](#table-of-contents)

Download state is persisted in `pipeline.db` (`fetch_state` table):

| Column | Description |
|---|---|
| `doc_id` | Document identifier (from manifest) |
| `status` | `pending`, `fetch_complete`, `fetch_failed`, `fetch_skipped` |
| `local_path` | Absolute path to downloaded file |
| `file_size` | File size in bytes |
| `http_status` | HTTP response code |
| `fetched_at` | Timestamp |
| `error` | Error message if `fetch_failed` |

The fetch stage checks this table before any download. A document with `status = 'fetch_complete'` is not re-downloaded unless `--force` is passed. This makes the fetch stage fully resumable — a run interrupted at any point can be restarted and will continue from where it stopped.

---

## 6. Problems Encountered and Fixes
[↑ Table of Contents](#table-of-contents)

### Problem 1: HTTP 403 Forbidden on VA Servers

**Symptom:** Many document URLs returned HTTP 403 with the default `requests` user agent (`python-requests/2.x`).

**Root cause:** VA web infrastructure blocks requests with non-browser user agents.

**Fix:** Set a realistic browser `User-Agent` header on all requests:
```python
session.headers.update({
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
})
```

### Problem 2: SSL Certificate Verification Failures

**Symptom:** Some VA document URLs returned SSL errors (`SSLCertVerificationError`).

**Root cause:** Some VA servers use intermediate certificates not included in the default Python CA bundle. The VA PKI chain is occasionally out of date or uses non-standard root CAs.

**Fix:** The VA's certificate chain issues are not the pipeline's problem to solve. Downloads to affected URLs are recorded as `fetch_failed` with the SSL error and skipped. Investigators can manually download these files if needed. No SSL verification bypass (`verify=False`) was implemented — disabling SSL verification is a security risk and was rejected as a fix.

### Problem 3: Content-Type Mismatch

**Symptom:** Some URLs returning `Content-Type: text/html` instead of `application/pdf` or the OOXML MIME type, containing an HTML error page rather than the document.

**Root cause:** Broken or redirected URLs on the VA server side. Some older document links in the VDL point to pages that redirect to a "document not found" HTML page with HTTP 200.

**Fix:** After download, validate file magic bytes. If a file downloaded as DOCX contains HTML (`<html>` tag at start), record as `fetch_failed`. This catches silent 200-OK HTML error pages.

### Problem 4: Redirect Loops and Infinite Redirects

**Symptom:** A small number of document URLs caused `requests` to enter redirect loops.

**Root cause:** VA server misconfiguration on some legacy document URLs.

**Fix:** Set `requests` `max_redirects=5`. Requests exceeding the redirect limit are recorded as `fetch_failed`.

### Problem 5: Large Files Causing Memory Pressure

**Symptom:** Some DOCX files (e.g., CPRS User Manual: 19MB) caused excessive memory usage when loaded entirely into memory.

**Root cause:** `requests.get()` without `stream=True` loads the entire response body into memory before writing.

**Fix:** Use `stream=True` and write in chunks:
```python
response = session.get(url, stream=True)
with open(local_path, "wb") as f:
    for chunk in response.iter_content(chunk_size=65536):
        f.write(chunk)
```

### Problem 6: Duplicate Filenames Across Applications

**Symptom:** Multiple applications have documents with identical filenames (e.g., `technical_manual.docx`). Without namespacing, files overwrite each other.

**Fix:** Store files in per-application subdirectories (`raw/<app_code>/`). Within each directory, filenames are unique (enforced by the VDL).

### Problem 7: `AR/WS` App Code Slash in File Paths

**Symptom:** `app_name_abbrev = "AR/WS"` creates an invalid file path: `raw/AR/WS/` is interpreted as a nested directory `WS/` inside `AR/`.

**Fix:** Sanitize slashes in app codes when constructing directory names: `AR/WS` → `ar_ws`. Applied in `fetch/selector.py` before path construction.

### Problem 8: Rate Limiting Causing HTTP 429

**Symptom:** After downloading several hundred files in rapid succession, the VA server began returning HTTP 429 (Too Many Requests).

**Root cause:** Insufficient delay between requests.

**Fix:** Increased default delay to 0.5 seconds and implemented exponential backoff on 429 responses (2s → 4s → 8s before retry).

---

## 7. Lessons Learned
[↑ Table of Contents](#table-of-contents)

**Always validate file content, not just HTTP status.** HTTP 200 does not mean a document was successfully delivered. VA servers sometimes return HTML error pages with a 200 status. Magic byte validation after download catches these silent failures.

**Never disable SSL verification.** The proper response to SSL errors is to record the failure and move on. Disabling verification introduces a security vulnerability and should never be done in a pipeline that processes government documents.

**Use `stream=True` for all file downloads.** Memory overhead from non-streaming downloads is unpredictable. Large files (10MB+) exist in the VDL corpus. Always stream.

**Rate limiting is not optional.** The VA VDL is a public service. Bulk downloads without rate limiting risk service degradation for other users and server-side IP blocking. 0.5 seconds per request is a reasonable minimum for a corpus of ~7,500 documents.

**File path sanitization must happen before any I/O.** The `AR/WS` slash problem appeared only during a full-corpus run. Any non-alphanumeric character in an application code should be sanitized to `_` before constructing filesystem paths.

**Idempotent state tracking is essential.** Downloads that fail due to transient errors must be retryable without re-downloading everything. The SQLite state table makes it possible to resume a large download that was interrupted partway through without re-downloading files that already completed.

---

## 8. Results

[↑ Table of Contents](#table-of-contents)

Fetch results are authoritative only as read from `pipeline.db`. The counts below reflect the state recorded in the `fetch_state` table after the fetch run completes — they are not declared upfront.

To query current fetch state:

```sql
SELECT status, COUNT(*) AS n
FROM fetch_state
GROUP BY status
ORDER BY n DESC;
```

```sql
-- Format breakdown for successfully fetched documents
SELECT f.doc_format, COUNT(*) AS n
FROM fetch_state fs
JOIN manifest m ON fs.doc_id = m.doc_id
GROUP BY m.doc_format
ORDER BY n DESC;
```

Results for the initial full-corpus fetch are recorded in `pipeline.db` under the `manifest` table. Consult the database directly for current counts — the numbers change as documents are re-fetched, new inventory rows are added, or failures are resolved.

---

## 9. Fetch Snapshot as of 2026-03-30
[↑ Table of Contents](#table-of-contents)

**This is a point-in-time snapshot only.** These numbers reflect the state recorded in `pipeline.db` on 2026-03-30. They are not projections or targets — they are what the database shows. Run the queries in §8 to get current counts.

### Fetch summary

| Metric | Value |
|---|---|
| Total manifest rows | 2,956 |
| Fetch successful (`fetch_status = ok`) | 2,909 |
| Fetch failed (`fetch_status = error`) | 47 |
| Success rate | 98.4% |

### Format breakdown (successfully fetched)

| Format | Count | % of fetched |
|---|---|---|
| DOCX | 2,865 | 98.5% |
| PDF | 44 | 1.5% |

DOCX dominates because the selector always prefers DOCX when a pair exists. The 44 PDF-only downloads are documents for which no DOCX counterpart was available on the VDL.

### Storage

| Metric | Value |
|---|---|
| Total disk usage | 3,153.8 MB |
| Average file size | 1,110 KB |
| Largest single file | 27.5 MB |

### Package coverage

| Metric | Value |
|---|---|
| Packages with at least one fetched document | 138 |

**Top 10 packages by document count:**

| Package | Documents fetched |
|---|---|
| SD | 345 |
| IB | 153 |
| PSO | 147 |
| ADT | 137 |
| PRCA | 106 |
| PSJ | 96 |
| VES | 95 |
| CPRS | 92 |
| PSS | 79 |
| YS | 78 |

### Fetch failures by package

All 47 fetch failures are "all URLs failed" errors — both the DOCX and PDF variants returned non-recoverable HTTP errors (404 or server-side 403). They are not transient network failures.

| Package | Failed docs |
|---|---|
| VHIC | 20 |
| NUMI | 6 |
| DGBT | 5 |
| TMP | 3 |
| PSS | 2 |
| PREM | 2 |
| PECS | 2 |
| VES | 1 |
| SD | 1 |
| ROEG | 1 |

The VHIC cluster (20 failures) is the largest single source of fetch errors. These documents exist in the VDL inventory but the linked files return 404 — the VA server has removed them or the URLs have changed since the inventory was crawled.

---

*End of report.*
