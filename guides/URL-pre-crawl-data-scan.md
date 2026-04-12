# URL Pre-Crawl Data Scan — Guide

A pre-crawl interrogation tool walks a website's link graph without downloading data artifacts. Its purpose is to give you a complete picture of scope, depth, link topology, and data yield *before* committing to a full crawl — so you can tune parameters, avoid traps, and not waste hours on a site that has nothing useful.

---

## What the Script Does

### Core behavior
- Accepts a single seed URL as the entry point
- Derives the **base domain** from that URL and stays strictly within it
- Follows HTML anchor links (`<a href>`) only — does not download referenced files
- Tracks every URL it has seen to avoid revisiting (deduplication)
- Stops at a configurable depth limit

### What it does NOT do
- Download PDFs, DOCX, XLSX, or any binary artifact
- Follow links to external domains
- Submit forms, execute JavaScript, or interact with dynamic content (unless a headless browser mode is enabled — see Pitfalls)
- Store page content — it records metadata only

---

## Script Architecture

### Input options

| Flag | Description | Default |
|---|---|---|
| `--url URL` | Seed URL to start from | required |
| `--depth N` | Maximum link depth to traverse | 3 |
| `--delay N` | Seconds between requests (politeness) | 1.0 |
| `--timeout N` | Per-request timeout in seconds | 10 |
| `--user-agent STR` | Custom User-Agent string | descriptive bot string |
| `--respect-robots` | Honor robots.txt rules | true |
| `--output FILE` | Write JSON/CSV report to file | stdout |

### Processing pipeline

**Phase 1 — Seed and robots check**
- Fetch and parse `robots.txt` at the base domain
- Record which paths are disallowed, crawl-delay directives, and sitemap references
- If a sitemap (`sitemap.xml` or `sitemap_index.xml`) exists, parse it immediately — this is the single highest-yield action in pre-crawl (see Best Practices)

**Phase 2 — BFS link traversal**
- Maintain a queue of (URL, depth) pairs seeded with the entry URL
- For each URL in the queue:
  1. Check: already visited? Skip.
  2. Check: exceeds depth limit? Record but do not enqueue children.
  3. Check: robots.txt disallowed? Record as blocked, skip.
  4. Fetch the page with a HEAD request first (checks status code and Content-Type without downloading body)
  5. If Content-Type is `text/html`: fetch the body and extract all `<a href>` links
  6. If Content-Type is a data artifact type (PDF, DOCX, etc.): record it as a found artifact, do not download
  7. Classify each extracted link as on-domain or off-domain
  8. Enqueue on-domain HTML links not yet visited, if within depth limit

**Phase 3 — Report generation**
- Aggregate all collected metadata into structured report sections (see Report section below)

### Data structures

The script maintains these in memory during traversal:

- `visited: set[str]` — all URLs fetched or attempted
- `queue: deque[(url, depth)]` — BFS frontier
- `pages: list[PageRecord]` — one record per HTML page visited
- `artifacts: list[ArtifactRecord]` — one record per data file found
- `off_domain_links: Counter[str]` — external domains and their link counts
- `errors: list[ErrorRecord]` — 4xx, 5xx, timeouts, redirects

### PageRecord fields
- URL, depth, HTTP status, Content-Type, response time (ms)
- Number of on-domain links found
- Number of off-domain links found
- Number of artifact links found on this page
- Page title (from `<title>` tag)
- Redirect chain (if any)

### ArtifactRecord fields
- URL, depth at which it was found, parent page URL
- File type (inferred from URL extension and Content-Type header)
- File size (from `Content-Length` header if present — not always reliable)
- HTTP status of HEAD request

---

## Report Output

### Summary block

```
Seed URL:          https://example.gov/documents/
Base domain:       example.gov
Depth limit:       4
Pages visited:     312
Pages blocked:     18  (robots.txt)
Pages errored:     7   (4xx/5xx)
Redirects:         23
Total links found: 1,847
  On-domain:       1,204  (65%)
  Off-domain:      643    (35%)
Crawl time:        4m 12s
Avg response:      340ms
```

### Artifact inventory

```
Data artifacts found (on-domain only):
  PDF:   148  (~2.1 GB estimated, 67 with unknown size)
  DOCX:    34  (~180 MB estimated)
  XLSX:    12  (~45 MB estimated)
  CSV:      8  (~12 MB estimated)
  PPTX:     3  (~90 MB estimated)
  JSON:    22  (likely API responses or data exports)
  Total:  227 artifacts across 89 pages
```

### Depth distribution

```
Depth  Pages  Artifacts  Avg Links/Page
  1      4        2         18.2
  2     38       12         11.4
  3    142       89          6.8
  4    128      124          3.1
```

A rising artifact count at deeper levels is a strong signal to increase depth in a real crawl.

### Top artifact-bearing pages

Lists the 10 pages with the most artifact links — useful for targeting a selective crawl.

### Off-domain link summary

Top external domains by link count — helps identify CDNs, partner sites, or mirrors that may hold additional relevant data.

### Error log

Every failed URL with its status code, parent page, and depth.

### Robots.txt summary

Which paths are disallowed, crawl-delay value, and sitemap URLs found.

---

## Best Practices for Pre-Crawl Interrogation

### 1. Always check robots.txt and sitemap first

`robots.txt` tells you what is explicitly off-limits and often contains a `Sitemap:` directive. A sitemap can enumerate thousands of URLs in seconds without touching a single HTML page. Parse the sitemap before doing any BFS — it may give you 80% of your target URLs immediately and reveal the true scope of the site.

### 2. Use HEAD requests before GET

A HEAD request fetches only headers, not the body. Use it to check:
- HTTP status (avoid fetching 404 pages)
- Content-Type (skip binary files you cannot parse)
- Content-Length (estimate download size before committing)

Only follow with a full GET if the HEAD confirms the page is HTML and reachable.

### 3. Set a conservative depth first, then expand

Start with depth 2 or 3. Review the depth distribution in the report: if artifact counts are still rising at the deepest level, increase depth. A flat or declining artifact count at depth N means going deeper yields diminishing returns.

### 4. Check response times early

If the first 10 pages average over 2 seconds per response, adjust your delay and timeout settings accordingly. Sites with slow responses will cause a deep crawl to run for hours. The pre-crawl assessment gives you realistic timing data before you commit.

### 5. Look for pagination patterns

Many document libraries paginate: `/documents?page=1`, `/documents?page=2`, etc. If you see query parameters with `page=`, `offset=`, or `start=` in links, your crawler needs to follow them. A pre-crawl that doesn't find many artifacts at shallow depth but shows heavy pagination links is a signal the real content is behind pagination, not nested links.

### 6. Identify JavaScript-rendered content early

If pages return minimal HTML with few links but the site visually shows rich content, it is likely JavaScript-rendered. A standard HTML parser will miss most links. You will need a headless browser (Playwright, Selenium) for the real crawl. The pre-crawl can detect this heuristically: if a page has fewer than 3 `<a href>` tags and a large inline `<script>` block, flag it as likely dynamic.

### 7. Respect crawl-delay — it protects your access

If `robots.txt` specifies a `Crawl-delay`, honor it. Many government and institutional sites rate-limit aggressively. Ignoring the delay will get your IP blocked, ruining not just this crawl but any future access.

### 8. Normalize URLs before deduplication

`/docs/file.pdf`, `/docs/file.pdf?lang=en`, and `/docs/file.pdf#section1` are the same file. Normalize URLs by stripping fragments (`#...`) and sorting/filtering query parameters before adding to the visited set, or you will fetch the same resource dozens of times.

### 9. Track redirects explicitly

A URL that redirects to another domain is not on-domain anymore. Follow redirect chains and re-evaluate domain membership at the final destination, not the initial URL.

### 10. Estimate total download size before committing

Sum `Content-Length` values from artifact HEAD requests. Even partial data (some files don't report size) gives a floor estimate. If you find 500 PDFs averaging 5MB each, that is 2.5GB — know this before starting the real crawl.

---

## Common Crawling Mistakes — Problems and Remedies

| # | Mistake | Consequence | Remedy |
|---|---|---|---|
| 1 | **Ignoring robots.txt** | IP ban, legal exposure, blocked access for the whole institution | Always fetch and parse robots.txt first; never request disallowed paths |
| 2 | **No crawl delay / too aggressive** | Rate limiting, 429 errors, IP block, service disruption to the target | Respect `Crawl-delay` in robots.txt; default to ≥1s between requests; back off on 429 |
| 3 | **Not normalizing URLs** | Infinite loops, fetching the same file hundreds of times with trivial query variations | Strip fragments, canonicalize query params, use a visited set on the normalized URL |
| 4 | **Following off-domain links** | Crawl expands to the entire internet; wastes time and resources | Derive base domain from seed URL and enforce it strictly on every enqueued link |
| 5 | **Assuming all content is in HTML** | Misses JavaScript-rendered pages entirely — finds 0 links on pages full of content | Detect JS-heavy pages by low link count + heavy script tags; use headless browser when needed |
| 6 | **No depth limit** | Crawl enters infinite pagination, sitemaps-of-sitemaps, or calendar archives | Always set a depth limit; inspect depth distribution before increasing it |
| 7 | **Not following redirects properly** | Misclassifies off-domain redirects as on-domain; double-fetches canonical URLs | Follow all redirects, re-check domain at final URL, deduplicate on final URL |
| 8 | **Using GET for every request** | Downloads megabytes of HTML you throw away just to check Content-Type | Use HEAD first; only GET confirmed HTML pages |
| 9 | **Skipping sitemap.xml** | Spends hours doing BFS when the site already published a complete URL list | Check `robots.txt` for `Sitemap:` directive; parse all sitemap/sitemap-index files before BFS |
| 10 | **Treating URL extension as ground truth for file type** | `.php` files that serve PDFs get skipped; `.pdf` URLs that 404 get queued | Use `Content-Type` from HEAD response as the authoritative file type, not the URL extension |
| 11 | **No timeout per request** | A single hung connection stalls the entire crawl indefinitely | Set per-request timeouts (10–30s); retry once with exponential backoff then skip |
| 12 | **Storing everything in memory** | Crawl crashes after thousands of pages due to OOM | Write visited set and queue to SQLite or disk; allow resume after interruption |
| 13 | **No User-Agent string** | Request looks like a vulnerability scanner; triggers WAFs and immediate blocking | Set a descriptive, honest User-Agent that identifies your script and contact info |
| 14 | **Ignoring session/auth requirements** | Crawl hits login redirects; every page resolves to the login page | Pre-check: does the seed URL redirect to `/login`? Establish session/cookies before crawling |
| 15 | **Not handling pagination** | Finds only first page of document listings; misses 90% of artifacts | Detect `?page=`, `?offset=`, `?start=` patterns in links; explicitly follow all pagination chains |
| 16 | **Treating all PDFs as equally valuable** | Downloads thousands of tiny boilerplate PDFs (agendas, notices) while missing large data-rich reports | Use `Content-Length` from HEAD to prioritize large files; inspect naming patterns before full fetch |
| 17 | **Not logging errors** | A 403 on a key directory silently kills 30% of expected yield; you never know | Log every non-200 response with its URL, status, and parent page; review before starting the real crawl |
| 18 | **Crawling from the wrong seed URL** | Starts from a landing page instead of the document index; BFS never reaches the real data | Explore the site manually first; identify the deepest practical seed URL closest to the actual data |
| 19 | **Absolute vs relative URL resolution** | Relative links like `../docs/file.pdf` are joined against the wrong base; links break | Always resolve links against the actual response URL (`resp.url`), not a static base string — especially after redirects |
| 20 | **No resume capability** | A crash at hour 3 of a 4-hour crawl means starting over | Persist state (visited set, queue, artifact list) to SQLite after every page; support `--resume` flag |

---

## Pre-Crawl Checklist

Before running a full crawl, the pre-crawl scan should answer all of these:

- [ ] Is robots.txt accessible? What is disallowed? What is the crawl delay?
- [ ] Is there a sitemap? How many URLs does it enumerate?
- [ ] Does the seed URL redirect? To where? Is the final destination on-domain?
- [ ] Are pages HTML or JavaScript-rendered? (Check link counts on first 5 pages)
- [ ] Does the site require authentication? (Check for login redirects)
- [ ] How many artifacts are found at each depth level? Is yield still rising at max depth?
- [ ] What is the estimated total artifact size?
- [ ] What is the average response time? Is rate limiting occurring?
- [ ] Are there pagination patterns that require explicit handling?
- [ ] What is the on-domain vs off-domain link ratio? (High off-domain = many dead ends)
- [ ] How many errors (4xx/5xx) are occurring? Which paths are failing?
- [ ] Which pages contain the highest concentration of artifacts? (Target these first)
