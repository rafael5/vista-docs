# VDL Pipeline — Stage 2a: Inventory Web Publication

**Date:** 2026-03-30
**Repository:** `~/git/vistadocs/vistadocs.github.io/`
**Live URL:** `https://vistadocs.github.io`

---

## Table of Contents

1. [Overview](#1-overview)
2. [Hosting: GitHub Pages](#2-hosting-github-pages)
3. [Technology Stack](#3-technology-stack)
4. [Architecture](#4-architecture)
5. [Column Design](#5-column-design)
6. [Filtering Design](#6-filtering-design)
7. [Data Pipeline to Web](#7-data-pipeline-to-web)
8. [Deployment Workflow](#8-deployment-workflow)
9. [Lessons Learned](#9-lessons-learned)

---

## 1. Overview
[↑ Table of Contents](#table-of-contents)

After the inventory enrichment stage produces `vdl_inventory_enriched.csv`, that file is published as an interactive web table so that the complete VDL catalog can be browsed, filtered, and searched without downloading anything.

**Input:** `~/data/vista-docs/inventory/vdl_inventory_enriched.csv` (8,834 rows, 30 columns, 4.1 MB)
**Output:** Interactive table at `https://vistadocs.github.io`

The web table is the public face of the inventory. It allows any user to filter by system type, section, package, document type, status, format, or layer, and to search document titles — without writing SQL or loading a spreadsheet.

---

## 2. Hosting: GitHub Pages
[↑ Table of Contents](#table-of-contents)

### Why GitHub Pages

The site is hosted on GitHub Pages. The decision was straightforward:

- **Free and permanent.** No server to provision, no hosting bill, no expiration.
- **Zero infrastructure.** No web server, no database, no build pipeline, no deployment keys, no containers.
- **Static is sufficient.** The inventory is a read-only dataset. There is no user authentication, no writes, and no server-side logic. A static file host is architecturally correct — not a compromise.
- **Version-controlled by default.** The CSV and HTML live in a git repository. Every change to the data or the UI is a commit. History is built in.
- **Instant deployment.** `git push` to `main` is the entire deployment pipeline. GitHub Pages serves the updated site within seconds.

### What GitHub Pages serves

GitHub Pages serves whatever files are in the repository root. No configuration file is needed for a single-page site. The repository contains:

```
vistadocs.github.io/
├── index.html                    # The entire web application
└── vdl_inventory_enriched.csv    # The data
```

That is the complete site. The browser loads `index.html`, which fetches `vdl_inventory_enriched.csv` from the same origin and renders the table client-side.

### Alternatives considered

| Option | Why rejected |
|---|---|
| Self-hosted web server | Requires infrastructure, maintenance, and uptime management — unnecessary for a static read-only dataset |
| Netlify / Vercel | Free tier available but adds a third-party dependency with account management overhead |
| GitHub Gist + bl.ocks.org | Limited to single-file content; no custom domain |
| Converting CSV to JSON and embedding | Doubles the data maintenance burden; CSV is the authoritative artifact |

---

## 3. Technology Stack
[↑ Table of Contents](#table-of-contents)

The entire application is a single HTML file with no build step, no npm, no bundler, and no local toolchain. All libraries are loaded from public CDNs.

### Libraries

| Library | Version | CDN | Purpose |
|---|---|---|---|
| PapaParse | 5.4.1 | jsdelivr | CSV parsing — converts the raw CSV string to a JavaScript array of row objects |
| jQuery | 3.7.1 | code.jquery.com | Required by DataTables; DOM manipulation |
| DataTables | 2.0.8 | cdn.datatables.net | Sortable, filterable, paginated table with server-less operation |
| DataTables Buttons | 3.0.2 | cdn.datatables.net | Column visibility toggle ("Show/hide columns" button) |
| DataTables ColVis | 3.0.2 | cdn.datatables.net | Column visibility extension used by the Buttons plugin |

### Rationale for each

**PapaParse** is the standard for client-side CSV parsing in JavaScript. It handles quoted fields, embedded commas, and newlines within values correctly. The alternative — fetching the CSV and parsing it manually — is fragile and error-prone. PapaParse is 50 KB and has no dependencies.

**DataTables** is the most widely used, documented, and maintained JavaScript table library. It was chosen over alternatives for three reasons:
1. Per-column filtering is a first-class feature (not a plugin afterthought)
2. The orthogonal data API separates display rendering from filter/sort values — critical for this use case where columns render HTML badges and links
3. The existing documentation for exactly this pattern (dropdown filters in a second header row) is thorough and well-tested

**jQuery** is a DataTables dependency, not an independent choice. DataTables 2.x still requires jQuery. This is a known limitation of the DataTables ecosystem.

**DataTables Buttons + ColVis** adds a "Show/hide columns" button that lets users declutter the table by hiding columns they do not need. The inventory has 8 visible columns — some users want to focus on document type and title only.

### Why no framework (React, Vue, etc.)

A JavaScript framework would add a build step, a `node_modules` directory, a bundler, and a deployment pipeline. For a single-page read-only table, all of that is unnecessary complexity. The entire application is 265 lines of HTML + CSS + JavaScript. There is no state management beyond what DataTables handles internally.

### Why CDN rather than local copies

CDN delivery means:
- No binary assets committed to the repository (keeps the repo small)
- Browsers may already have the libraries cached from other sites
- No local toolchain required to update the site

The tradeoff is a dependency on CDN availability. For a reference tool — not a production application with uptime SLAs — this is acceptable.

---

## 4. Architecture
[↑ Table of Contents](#table-of-contents)

The application is entirely client-side. There is no server-side code.

```
Browser
  │
  ├── GET index.html          (served by GitHub Pages)
  │
  ├── GET vdl_inventory_enriched.csv   (same origin, via PapaParse)
  │     └── PapaParse parses CSV → array of row objects
  │
  └── DataTables initializes
        ├── Builds column definitions with orthogonal render functions
        ├── Populates dropdown filters from unique values
        └── Renders table with pagination, sorting, filtering
```

### Orthogonal rendering

The central architectural decision is the use of DataTables' orthogonal data pattern. Each column's `render` function returns different content depending on the requested `type`:

```javascript
render: function(row, type) {
  var raw = row[col.field] || '';

  // For sort and filter: return plain text
  if (type !== 'display') return raw;

  // For display: return HTML
  if (col.field === 'app_status') {
    var cls = { active: 'badge-active', archive: 'badge-archive',
                decommissioned: 'badge-decommissioned' }[raw] || '';
    return '<span class="badge ' + cls + '">' + esc(raw) + '</span>';
  }
  if (col.field === 'doc_title') {
    return row.doc_url
      ? '<a href="' + esc(row.doc_url) + '" target="_blank">' + esc(raw) + '</a>'
      : esc(raw);
  }
  return esc(raw);
}
```

When DataTables filters or sorts a column, it requests `type = 'filter'` or `type = 'sort'` and receives plain text. When it renders to the DOM, it requests `type = 'display'` and receives HTML. Without this separation, the Status dropdown filter would try to match against `<span class="badge badge-active">active</span>` and find nothing.

### XSS prevention

All values written into HTML are passed through `esc()`:

```javascript
function esc(s) {
  return String(s || '')
    .replace(/&/g, '&amp;').replace(/</g, '&lt;')
    .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}
```

Document titles, package names, and URLs from the CSV are untrusted input. `esc()` is applied to all of them before insertion into the DOM. URLs are used only in `href` attributes on anchor tags — never injected as raw HTML.

---

## 5. Column Design
[↑ Table of Contents](#table-of-contents)

Eight columns are displayed, in this order:

| # | Column header | CSV field | Render |
|---|---|---|---|
| 1 | System Type | `system_type` | Plain text |
| 2 | Section | `section_name` | Plain text |
| 3 | Package | `app_name_abbrev` | Bold |
| 4 | Doc Type | `doc_label` (fallback: `doc_code`) | Plain text |
| 5 | Status | `app_status` | Colored badge |
| 6 | Format | `doc_format` | Plain text |
| 7 | Layer | `doc_layer` | Plain text |
| 8 | Document Title | `doc_title` | Hyperlink (via `doc_url`) |

The remaining 22 inventory columns are not displayed. The table is a navigation and discovery interface, not a data dump. Users who need the full schema should download the CSV.

### Column ordering rationale

The order moves from broadest to narrowest classification:

- **System Type** first — the most analytically significant grouping; distinguishes VistA packages from non-VistA systems
- **Section** second — the VDL's own organizational grouping (Clinical, Financial-Administrative, etc.)
- **Package** third — the specific application
- **Doc Type, Status, Format, Layer** — document-level attributes that narrow within a package
- **Document Title** last and widest — the specific document, with a direct link

This ordering means a user reading left to right moves from context to content.

### Doc Type fallback

The `doc_label` field is used for the Doc Type column, with `doc_code` as a fallback for the 8.4% of rows where `doc_label` is empty:

```javascript
var raw = col.field === 'doc_label'
  ? (row.doc_label || row.doc_code || '')
  : (row[col.field] || '');
```

This ensures the Doc Type dropdown is populated and filterable even for unlabelled rows that have a `doc_code` but no `doc_label`.

### Default sort

The table initializes sorted by System Type (column 0) ascending, then Package (column 2) ascending. This groups all VistA packages together and sorts alphabetically within each system type.

---

## 6. Filtering Design
[↑ Table of Contents](#table-of-contents)

Filtering uses a second header row (`<tr class="filter-row">`) rendered directly beneath the main column headers. Each cell in the filter row contains either a dropdown (`<select>`) or a text input, depending on the column type.

### Dropdown filters (columns 1–7)

Columns with a bounded vocabulary use exact-match dropdown filters. Unique values are pre-computed from the full dataset before DataTables initializes:

```javascript
var seen = {};
rows.forEach(function(r) {
  var v = (col.field === 'doc_label' ? (r.doc_label || r.doc_code) : r[col.field]) || '';
  if (v) seen[v] = true;
});
uniqueVals[col.field] = Object.keys(seen).sort();
```

Each dropdown includes an "All" option as the first entry. Selecting a value triggers an anchored regex search so that partial matches do not fire:

```javascript
api.column(i).search(
  val ? '^' + $.fn.dataTable.util.escapeRegex(val) + '$' : '',
  true,   // regex
  false   // smart search off
).draw();
```

The anchoring (`^...$`) is essential. Without it, selecting "patch" would also match "dispatch".

### Text search (Document Title)

The Document Title column uses a free-text input with substring matching. This is appropriate because document titles are long and varied — exact matching would require typing a full title.

### Filter row visibility sync

When a user hides a column using the "Show/hide columns" button, the corresponding filter cell must also be hidden. This is handled by listening to the `column-visibility.dt` event:

```javascript
function syncFilterRow() {
  api.columns().every(function(i) {
    var th = $($('#vdl thead tr.filter-row th').get(i));
    this.visible() ? th.show() : th.hide();
  });
}
syncFilterRow();
api.on('column-visibility.dt', syncFilterRow);
```

Without this, hidden columns leave orphaned visible filter cells that shift the remaining filters out of alignment with their columns.

---

## 7. Data Pipeline to Web
[↑ Table of Contents](#table-of-contents)

The CSV file in the GitHub Pages repository is a copy of the enriched inventory. It is not generated from the repository — it is copied from the pipeline output.

### Copy step

```bash
cp ~/data/vista-docs/inventory/vdl_inventory_enriched.csv \
   ~/git/vistadocs/vistadocs.github.io/vdl_inventory_enriched.csv
```

This is a manual step, run whenever the inventory is re-enriched or re-classified. It is not automated — the pipeline and the web repository are intentionally decoupled. The pipeline can be re-run as many times as needed without affecting the live site until the operator explicitly copies and pushes the updated CSV.

### When to update

The CSV in the web repository should be updated when:
- The enrichment pipeline adds new columns (e.g., `system_type` was added in March 2026)
- A new crawl captures new VDL documents
- Classification or labelling corrections are applied

### File size

The CSV is 4.1 MB. This is comfortably within GitHub Pages' file size limits and is small enough for typical broadband connections to load in under a second. The browser parses 8,834 rows with PapaParse in approximately 100–200ms on a modern machine — imperceptible to the user.

---

## 8. Deployment Workflow
[↑ Table of Contents](#table-of-contents)

```bash
# 1. Copy updated CSV from pipeline output
cp ~/data/vista-docs/inventory/vdl_inventory_enriched.csv \
   ~/git/vistadocs/vistadocs.github.io/

# 2. Stage and commit
cd ~/git/vistadocs/vistadocs.github.io
git add index.html vdl_inventory_enriched.csv
git commit -m "Update inventory and/or UI changes"

# 3. Push — this is the entire deployment
git push
```

GitHub Pages picks up the push and serves the updated site within seconds. There is no build step, no CI pipeline, no manual trigger.

### Authentication

GitHub removed HTTPS password authentication in August 2021. Pushes must use SSH. The remote is configured as:

```
git remote set-url origin git@github.com:vistadocs/vistadocs.github.io.git
```

SSH key authentication must be set up on the local machine before the first push. Once configured, `git push` is unattended.

---

## 9. Lessons Learned
[↑ Table of Contents](#table-of-contents)

### Orthogonal rendering is not optional for HTML columns

The first implementation populated dropdowns by calling `col.data()` inside `initComplete`. This returns rendered HTML — badge markup, anchor tags — not plain text. Every dropdown appeared empty because `<span class="badge badge-active">active</span>` never matched the regex `^active$`.

The correct approach is to pre-compute unique values from the raw data array before DataTables initializes, and to use a `render` function that returns plain text for all non-display types. DataTables' orthogonal data model exists precisely for this separation. Understanding it upfront would have avoided this iteration entirely.

### Develop and test directly on GitHub Pages

An attempt was made to develop and test using a local Python HTTP server (`python3 -m http.server`). This introduced a second environment to manage, an address-in-use error when the server was already running, and a subtle discrepancy: the local CSV was a stale copy that did not include `system_type`, so the System Type dropdown appeared empty locally but was expected to work on the live site.

The correct workflow is simpler: make the change, commit, push, and test on the live GitHub Pages URL. GitHub Pages deploys within seconds. The "local web server" layer added friction without benefit for a single static file with no build step.

### Never serve the CSV from a separate working directory

Initially the CSV was copied to `~/data/vista-docs/www/` as the "web root." This introduced a third copy of the file (pipeline output → www/ → git repo) and caused repeated silent failures where the wrong copy was being served. The correct design is one copy: the file lives in the git repository and is served from there.

### The filter row must be kept in sync with column visibility

When the DataTables column visibility toggle hides a column, the corresponding `<th>` in the filter row is not automatically hidden. The filter cells shift left while the data columns shift, misaligning every filter after the hidden column.

The fix — listening to `column-visibility.dt` and explicitly hiding/showing filter cells — is straightforward once the problem is understood. The symptom (dropdowns under the wrong columns) is confusing until the root cause is recognized.

### Exact-match regex anchoring prevents false positives

Without anchoring the dropdown regex with `^...$`, selecting a value like "patch" from the Layer dropdown also matches rows where `doc_layer = 'dispatch'` or any other value containing the substring. The `$.fn.dataTable.util.escapeRegex()` utility handles special characters in values; the `^...$` anchors enforce exact matching. Both are required.

### GitHub HTTPS authentication was removed in 2021

Attempting `git push` over HTTPS prompts for a password that GitHub no longer accepts. The error message (`remote: Support for password authentication was removed`) is clear, but the fix — switching the remote URL to SSH — needs to be done once and requires an SSH key already configured for the GitHub account. Confirm SSH is working before the first push attempt.

### Column order shapes how users read the table

The initial column order placed Document Title first, which made the table feel like a raw document list. Reordering to System Type → Section → Package → Doc Type → Status → Format → Layer → Document Title transformed the table into a classification browser: users naturally read left to right, narrowing from broad context to specific document. Column order is a UX decision, not a cosmetic one.

---

*End of report.*
