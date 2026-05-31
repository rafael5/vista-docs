# Docs-as-Code: GitHub-Based Web Publishing Pipelines
## Best Practices from Major Software Companies — and Application to the VDL

*Written March 2026. Audience: Rafael — VistA Docs Library transformation, 2,888 documents, 139 packages.*

---

## 1. What Docs-as-Code Is

Docs-as-code applies software engineering discipline to documentation:

| Software development | Docs-as-code equivalent |
|---|---|
| Source code in git | Markdown files in git |
| Code review via pull request | Doc changes via pull request |
| CI/CD builds and tests | Build pipeline lints, links, publishes |
| Versioned releases | Versioned doc sets per product release |
| Issue tracker for bugs | Issue tracker for doc bugs |
| Package registry | Documentation portal / search index |

The canonical pipeline is:

```
Author → PR → Review → Merge → CI Build → Static Site → CDN/Hosting
```

Every stage is automated and auditable. No CMS, no manual FTP, no Word attachments emailed to a webmaster.

---

## 2. Why Large Companies Converge on This Model

At scale (hundreds of packages, thousands of pages), the alternatives fail:

- **Wikis** (Confluence, SharePoint) — no versioning, no review gates, no build pipeline, URL rot
- **DITA/XML CMS** (Arbortext, oXygen) — high tooling cost, writer bottleneck, poor Git integration
- **Custom CMS** — expensive to maintain, hard to onboard engineers who can write
- **Shared Word/PDF repo** — no web delivery, no search, no links between docs

Docs-as-code solves all of these. The tradeoff is upfront pipeline investment and writer training.

---

## 3. The Six Major Models

---

### 3.1 Microsoft — learn.microsoft.com (OPS / DocFX)

**Scale:** ~30,000 articles per major product (Azure alone), hundreds of product families, thousands of contributors.

**Architecture:**
- All content lives in public GitHub repos under the [MicrosoftDocs](https://github.com/MicrosoftDocs) org — one repo per product family (e.g., `azure-docs`, `windows-uwp`, `sql-docs`)
- Source format: Markdown with YAML frontmatter + a Microsoft-flavored extension dialect (DocFX Flavored Markdown — DFM) supporting note/warning callouts, tabbed content, include files
- Build system: **Open Publishing System (OPS)** — Microsoft's internal CI platform that triggers on every PR and merge
- Static site generator: **DocFX** (open source, written in .NET) → generates HTML + JSON search index
- Hosting: Azure CDN, 100% on Azure infrastructure
- Every article has an "Edit this page" link → GitHub PR workflow
- Community PRs are triaged by a bot (Openpublishing-build) that runs builds and flags broken links

**Versioning model:** Multiple `main-` branches per major product version, with a `toc.yml` file that defines navigation trees. Versions are surfaced as a dropdown on the page.

**Key pattern — centralized portal, federated repos:**
The portal (learn.microsoft.com) is one unified surface, but the content is distributed across hundreds of repos. Each repo is owned by a product team. The platform team owns the build system and theme. Product teams own their Markdown.

**Pros:**
- Massive scale proven — tens of thousands of articles, global CDN
- Community contribution model works — external PRs flow naturally
- DocFX handles API reference generation from code (XML doc comments → Markdown)
- Versioning is explicit and auditable in git
- Search is first-class (Azure Cognitive Search behind the portal)

**Cons:**
- OPS is proprietary — you cannot run the exact Microsoft build locally
- DFM extensions (`::: zone`, `> [!NOTE]`) are non-standard and create lock-in
- The `toc.yml` navigation files are complex to maintain at scale
- DocFX is .NET-based — heavier toolchain than Python/Node alternatives
- Repo-per-product creates cross-linking friction (relative links across repos break easily)

**What Microsoft got right:**
- One unified URL namespace (`learn.microsoft.com/en-us/<product>/`) even though content is in 200+ repos
- Content reuse via `!INCLUDE` directives across repos
- "Freshness" metadata in frontmatter — articles have `ms.date` and stale ones get flagged
- Localization pipeline built into OPS — same Markdown, translated builds run in parallel

---

### 3.2 Google — developers.google.com / cloud.google.com

**Scale:** Thousands of guides, references, tutorials across hundreds of Google products.

**Architecture:**
- **Hugo** (Go-based static site generator) with custom themes — very fast builds
- Source in internal Piper repos (Google's internal monorepo) mirrored to GitHub for community products
- Public-facing products (Cloud, Android, Firebase) use a hybrid: internal authoring → GitHub export → Hugo build → Google CDN
- Devsite (Google's internal build toolchain) renders final HTML; externally visible as the site
- Markdown + some YAML frontmatter; heavy use of reStructuredText for Python API docs

**Key pattern — Hugo + Docsy for open source, internal Devsite for proprietary:**
For open-source products (Kubernetes, gRPC, TensorFlow), Google uses the **Docsy** Hugo theme (open source, community-maintained). For internal products, a proprietary pipeline.

**Pros:**
- Hugo is the fastest static site generator available — sub-second incremental builds even at large scale
- Docsy is excellent for multi-product portals — left nav, versioned docs, API reference integration
- Strong tooling for code samples — samples are pulled from tested code repositories, not copy-pasted into Markdown
- Search via Google Search (naturally)

**Cons:**
- Devsite toolchain is not publicly available
- Hugo's template language (Go templates) has a steep learning curve
- The split between internal/external pipelines creates sync friction
- Code sample freshness is hard to guarantee across hundreds of products

**What Google got right:**
- Code samples in docs are pulled from real, tested code via include directives — samples are always runnable
- `codelab` format (step-by-step tutorials) is a first-class content type with its own build toolchain (Claat)
- Contributor guides are detailed and enforced via CI — new content must pass style linting before merge

---

### 3.3 Meta — Docusaurus

**Scale:** Facebook/Meta open-sourced Docusaurus, which is now used by thousands of projects including Jest, React, Babel, PyTorch, Supabase, and dozens of others.

**Architecture:**
- **Docusaurus** (React-based, Node.js) — open source, Apache 2.0
- Markdown (MDX — Markdown + JSX) source files
- One `docusaurus.config.js` per site — configures nav, sidebar, plugins, search
- Versioning via `docs/` directory structure + `versions.json`
- Algolia DocSearch for search (free for open source docs)
- Typically hosted on GitHub Pages, Netlify, or Vercel
- GitHub Actions for CI/CD — on every push to main, rebuild and deploy

**Key pattern — per-repo sites with a shared theme:**
Each product owns its own Docusaurus instance. There is no "platform team" mediating builds. The repo IS the site.

**Pros:**
- Zero infrastructure cost — GitHub Pages + GitHub Actions is fully free
- MDX enables interactive components inside documentation (live code editors, charts)
- Versioning is trivially simple — copy the `docs/` folder to `versioned_docs/version-X.Y/`
- Algolia DocSearch is excellent and free for open source
- Huge community — best-maintained of all open-source doc generators in 2026
- Sidebar auto-generation from directory structure

**Cons:**
- Node.js build — slower than Hugo for very large sites (1,000+ pages starts to feel it)
- MDX (React in Markdown) creates a high barrier for non-technical writers
- No built-in multi-repo portal — linking 139 Docusaurus sites into one search requires Algolia federation
- JavaScript bundle can be heavy for documentation sites
- React dependency means security patches can cascade across all sites simultaneously

**What Meta got right:**
- First-class versioning that maps directly to software release cycles
- Plugin architecture — search, analytics, blog, API reference all pluggable
- "Classic" theme is polished enough to use out of the box with no design work

---

### 3.4 HashiCorp — developer.hashicorp.com

**Scale:** ~10 major products (Terraform, Vault, Consul, Nomad, etc.), each with extensive docs, versioned per release.

**Architecture:**
- **Next.js** (React SSR/SSG) for the portal — custom-built
- MDX source content in individual product repos (e.g., `hashicorp/terraform`, `hashicorp/vault`)
- A separate `hashicorp/web-platform` controls the shared theme and portal
- Content is pulled from product repos at build time — the portal aggregates content from ~10 repos
- GitHub Actions CI for validation; Vercel for hosting
- Algolia search across all products unified

**Key pattern — federated content, centralized portal:**
Product teams write Markdown in their own repos. The portal is a separate Next.js app that imports content from all product repos at build time via the GitHub API. This is architecturally the same as Microsoft's OPS model but built in Node.js.

**Pros:**
- Unified search and navigation across all products
- Each product repo can be developed and tested independently
- Version selector works across all products consistently
- High visual polish — HashiCorp docs are widely cited as among the best in the industry
- The content aggregation model scales well — adding a new product = adding one repo import

**Cons:**
- Very high engineering investment to build the portal — not replicable without a dedicated team
- Next.js SSR adds hosting complexity vs. static-only options
- Product teams can't preview exactly how their content will look in the portal without running the whole platform
- Build times for the full portal can be long when aggregating 10+ repos

**What HashiCorp got right:**
- Navigation is generated from frontmatter (`nav_title`, `page_title`) — no separate TOC file to maintain
- "Beta" and "deprecated" badges on individual pages
- Try-it-live embedded terminals for CLI products (Katacoda-style)
- Changelog and upgrade guides are first-class navigation items, not afterthoughts

---

### 3.5 Kubernetes / CNCF — kubernetes.io

**Scale:** Community-maintained, 20+ languages (localization), hundreds of contributors, releases every 4 months.

**Architecture:**
- **Hugo** + **Docsy** theme
- Single GitHub repo (`kubernetes/website`) — all content, all languages, all versions
- Multiple branches: `main` (in-development) + `release-X.Y` branches (one per Kubernetes release)
- Branch-based versioning — the website build reads the current branch and sets the version header
- GitHub Actions CI: Netlify preview builds for every PR, promotion to production on merge
- Hosted on Netlify (community tier, free for OSS)

**Key pattern — community ownership, branch-per-release:**
There is no product team owning docs. SIG Docs (a Kubernetes Special Interest Group) governs the repo. Every contributor is a community member. Release cycles are tightly coordinated — docs PRs for a new release are opened against the release branch, not main.

**Pros:**
- Fully open, entirely community-maintained — no cost
- Hugo + Docsy is the most proven stack for large multi-language technical docs
- Branch-per-release versioning is robust and maps 1:1 to software releases
- Netlify previews for every PR make review fast and visual
- Localization is first-class — all translations are in the same repo, same pipeline

**Cons:**
- Single repo for all content becomes large and slow to clone over time
- Hugo + Docsy requires Go template expertise to customize
- Branch-per-release requires careful cherry-pick discipline for bug fixes and backports
- Community governance is slow — major structural changes require SIG Docs consensus
- Localization lags main by weeks to months

**What Kubernetes got right:**
- Shortcodes for reusable content patterns (feature-state banners, tabs, code blocks with copy button)
- Strict content type taxonomy: Concept / Task / Tutorial / Reference — every page is one of these
- Contributor guide is extremely detailed and enforced via CI (Netlify CMS spell check, link checker, Hugo build)

---

### 3.6 Stripe — stripe.com/docs

**Scale:** Hundreds of API reference pages + conceptual guides, widely cited as the best API documentation in the industry.

**Architecture:** Proprietary. Not open source. What is known:
- MDX-based source content
- Custom React components for interactive examples (live API request/response, language switcher)
- Deployed on Stripe's own infrastructure
- API reference is generated from an internal OpenAPI/JSON Schema source of truth
- Search is custom-built (not Algolia)

**Key pattern — docs as product:**
Stripe treats documentation as a product feature with the same engineering investment as the product itself. Writers and engineers collaborate in the same PR workflow. Every code sample is tested in CI.

**Pros:**
- Highest quality bar in the industry — interactive, consistent, always up-to-date
- Language switcher on every code sample (curl, Python, Ruby, Node, PHP, Java, Go, .NET)
- API reference and conceptual docs are unified — you never have to leave the docs to find a reference
- Code samples in docs are tested in CI — they cannot go stale

**Cons:**
- Entirely proprietary — cannot be used or replicated
- Requires significant engineering investment (dedicated docs engineering team)
- The interactive components require React expertise to author
- Not applicable to legacy document libraries without full rewrite

**What Stripe got right:**
- "Ruthless consistency" — every page follows the same pattern
- Contextual API reference embedded in conceptual guides
- Request/response samples for every endpoint, in every language

---

## 4. Comparison Table

| Model | Generator | Source Format | Versioning | Hosting | Search | Multi-repo Portal | Engineering Cost |
|---|---|---|---|---|---|---|---|
| **Microsoft** | DocFX | Markdown + DFM | Branches | Azure CDN | Azure Search | OPS (proprietary) | Very High |
| **Google** | Hugo / Devsite | Markdown / RST | Branches | Google CDN | Google Search | Devsite (proprietary) | Very High |
| **Meta/Docusaurus** | Docusaurus (React) | MDX | Directory copy | GitHub Pages / Netlify | Algolia | Manual federation | Low |
| **HashiCorp** | Next.js (custom) | MDX | Branches | Vercel | Algolia | Content aggregation | High |
| **Kubernetes** | Hugo + Docsy | Markdown | Branches | Netlify | Algolia | Single repo | Medium |
| **Stripe** | Custom React | MDX | Unknown | Own infra | Custom | N/A | Very High |

---

## 5. Cross-Cutting Patterns (What All Models Share)

Regardless of toolchain, every scaled docs-as-code pipeline shares these characteristics:

### 5.1 Frontmatter as the Data Layer
Every Markdown file carries YAML frontmatter with structured metadata:
- `title`, `description` — for SEO and navigation
- `ms.date` / `last_reviewed` — freshness tracking
- `doc_type` / `content_type` — for filtering and taxonomy
- `version` — for branch-aware rendering

This frontmatter IS the content management database. There is no separate CMS.

### 5.2 Static Site Generators, Not Dynamic Servers
All of these sites are pre-built HTML + CSS + JS deployed to a CDN. There is no server rendering documentation on request. This means:
- Near-zero hosting cost per page view
- No CMS security vulnerabilities
- Build-time link validation
- Trivially scalable under any traffic

### 5.3 CI/CD as the Quality Gate
Every pipeline runs automated checks on PR:
- Link checker (no dead links)
- Spell checker
- Frontmatter validator (required fields present)
- Build validator (site must build successfully)
- Style linter (sentence case titles, no passive voice, etc.)

Nothing ships without passing CI.

### 5.4 Content Types as a First-Class Taxonomy
Every large doc set defines explicit content types. Kubernetes: Concept / Task / Tutorial / Reference. Microsoft: Overview / How-to / Tutorial / Concept / Reference / Quickstart. HashiCorp: Introduction / Overview / Tutorial / Reference / Internals.

Content types matter because they define the reader's expectation and the author's template. A reference page and a tutorial have completely different structures.

### 5.5 Navigation Generated from Metadata, Not Hand-Maintained
At scale, you cannot maintain a hand-edited nav tree. All of the above models auto-generate navigation from either:
- `toc.yml` files that reference pages (Microsoft)
- `_category_.json` files in directories (Docusaurus)
- Frontmatter `nav_title` / `sidebar_position` (HashiCorp, Docusaurus)
- `weight` frontmatter + directory structure (Hugo/Docsy)

The key principle: nav structure is declared in the content repository, not in a separate CMS.

### 5.6 Monorepo vs. Federated Repos
The fundamental architectural choice:

| | Monorepo | Federated |
|---|---|---|
| Example | Kubernetes, ReadTheDocs | Microsoft, HashiCorp |
| Portal | Single build | Aggregation layer required |
| Cross-linking | Trivial (relative paths) | Complex (absolute URLs) |
| Team autonomy | Low (shared PRs) | High (own repo) |
| Search | Trivial | Requires unified index |
| Scale limit | Repo size / build time | Aggregation complexity |

For 139 packages, federated (one repo per package) is almost always the right choice. The cost is building the portal aggregation layer.

---

## 6. VA Doc-Code Reference

This section is the authoritative reference for the VA VistA Documentation Library (VDL) document type system — both the official VA taxonomy and the `DocType` classifier buckets used in the pipeline.

### 6.1 Official VA Doc Codes

The VA VDL assigns each document a short code that identifies its type. These codes appear in filenames (`cprsguitm.docx` = TM), in VDL page tables, and in the inventory CSV. This table covers every official code, what it means, what the document contains, and implementation notes for the pipeline.

| VA Code | Full Name | Definition | Typical content | Era / status | Audience | `DocType` bucket | Notes |
|---|---|---|---|---|---|---|---|
| **RN** | Release Notes | Patch-level change log distributed with every KIDS patch build. Mandatory for all patches. | What changed, why it changed, known issues, affected routines, backout procedure summary. Always includes patch number, date, and patch sequence dependencies. | Current — every patch has one | Developers, IRM, site managers | `release-note` | Most common doc type in corpus (735 docs). One RN per KIDS patch. Title is always the patch number (e.g. "PSJ*5*381"). Filename suffix `rn.` or patch-name pattern `or_3_0_350_rn`. |
| **DIBR** | Deploy / Install / Back-out / Rollback | Combined installation document introduced post-2015. Supersedes standalone IG for new patches. | Four mandatory sections: (1) Deployment prerequisites and sequence, (2) step-by-step installation procedure, (3) back-out plan if install fails, (4) rollback/uninstall procedure. | Current — standard for patches after ~2015 | IRM, system administrators | `installation-guide` | Replaced IG as the VA standard for patch install docs. Title format is standardized: "PackageName Patch XX*X*NNN Deploy, Install, Back-Out, Rollback Guide". Filename contains `dibr`. |
| **IG** | Installation Guide | Standalone installation and setup document. Predates DIBR; still in use for package-level (non-patch) installs. | Prerequisites, install sequence, verification steps, post-install tasks. May cover initial site setup as well as patch install. | Legacy for patches; current for package installs | IRM, system administrators | `installation-guide` | Many older packages still use IG format rather than DIBR. Both map to `installation-guide`. Filename suffix `ig.` or contains `install`. |
| **UM** | User Manual | Comprehensive end-user operational reference. The primary document for clinical and administrative users of a package. | All menus, options, and workflows a user needs to operate the package. Organized by functional area. Includes field-by-field descriptions of data entry screens. | Current | End users (clinicians, clerks, coordinators) | `user-manual` | Highest-value doc type for web publishing — most frequently consulted. Often very long (100–500 pages). Filename suffix `um.`. |
| **UG** | User Guide | Functionally identical to UM; a title variant used by some packages. | Same content scope as UM — full operational reference for end users. | Current | End users | `user-manual` | No filename suffix distinction from UM; classified by title only. Some packages used UG instead of UM for stylistic reasons — no semantic difference. |
| **TM** | Technical Manual | Internal design and architecture reference for developers and support staff. | FileMan data dictionaries (all files and fields), routine descriptions, globals layout, callable entry points (APIs), integration agreements (ICRs), external interface specifications. | Current | Developers, integration engineers | `technical-manual` | Second-highest technical value for web publishing — contains the data dictionary and integration specs that developers reference constantly. Often very long. Filename suffix `tm.`. Both signal paths (filename + title) covered in classifier. |
| **VDD** | Version Description Document | High-level overview of a named package version — what the version is, not how to install or use it. | Package capabilities, component list, dependency versions, system requirements, version history summary. Describes the version scope; does not contain step-by-step procedures. | Legacy — predates DIBR/RN era; rarely produced post-2010 | Project managers, site managers | *(gap — propose `release-note`)* | **Classifier gap: no rule exists.** Currently falls to `UNKNOWN`. No filename suffix convention (`vdd.`) is covered in `_FILENAME_RULES`, and no title rule for "version description" exists. Best available bucket is `release-note` (version-scoped summary). Action: add `vdd\.` filename rule and `version\s+description` title rule. |
| **POM** | Production Operations Manual | Runbook for the IRM/operations team managing the production VistA environment. | Startup/shutdown procedures, background job management, backup and recovery, monitoring, performance tuning, escalation paths. Not for end users. | Current for complex packages; rare overall | IRM, system administrators | `supplement` | Audience is operations staff, not users. Classified as `supplement` because it is adjunct to the package — not a standalone end-user or developer reference. Title pattern `productions? operations manual` or bare `pom`. |
| **TRG** | Training Guide | Structured curriculum for instructor-led or self-paced training on the package. | Learning objectives, conceptual background, exercises with step-by-step scenarios, knowledge checks, assessment materials. Written for a training context, not daily reference. | Current but uncommon | Trainers, students | `supplement` | **Partial classifier gap:** Title rule `training\s+guide` covers most cases. However, no filename rule for `tg.` or `trg.` suffix exists — files with those suffixes and generic titles fall to `UNKNOWN`. Action: add `(tg\.|trg\.)` to `_FILENAME_RULES`. Classified as `supplement` because it is curriculum material, not an operational reference. |
| **SMG** | Systems Management Guide | Reference for Application Coordinators (ADPACs) and site managers who administer the package at the site level. | Parameter file setup, menu configuration, user access assignment, security key management, site-specific option management, coordinator workflows. Bridges UM (end user) and TM (developer). | Current | ADPACs, site managers, coordinators | `user-manual` | The ADPAC is the site-level administrator of a VistA package — not a developer, not a typical end user. SMG covers admin tasks that UM doesn't. Classified as `user-manual` because it is a user-facing operational reference; audience is just narrower than UM. Title pattern `systems? management`. |
| **QRG** | Quick Reference Guide | Condensed one-page or short reference card for experienced users. | Key commands, menu paths, workflow shortcuts, field codes. Designed to fit on one printed page or a small card; not a comprehensive reference. | Current but uncommon | Experienced end users | `quick-ref` | Typically very short (1–4 pages). Filename suffix `qr.` or `qrg.`; title `quick ref` or `quick reference`. |
| **SUP** | Supplement | Adjunct material that extends a primary document. | Glossaries, appendices, errata lists, ancillary reference tables, additional scenarios. Too short or specialized to stand alone as a primary doc. | Current | Varies | `supplement` | Catch-all for material that belongs alongside a primary document. Filename suffix `sp.`; title `supplement`. |
| **CP** | Change Page | Replacement page(s) for a printed binder manual. Distributed when a correction is too small to warrant a full document reissue. | The corrected text only — one or more pages that the reader physically removes from a binder and replaces. No context; reader must know which manual it belongs to. | Legacy — obsolete for web delivery | Document custodians | `change-page` | A relic of the pre-web printed binder era. Rarely produced after 2010 but still present in the corpus (163 docs). Has no meaning outside a printed binder; in a web pipeline, the change should be applied as an edit to the parent document. The CP diff applier (planned pipeline stage) handles this. |

---

### 6.2 Title-Classified Variants

Documents without an official VA code but classified by title pattern. These exist because different packages coined their own type names for documents that map to an existing `DocType` bucket.

| Title pattern | Full Name | Definition | Typical content | `DocType` bucket | Notes |
|---|---|---|---|---|---|
| ADPAC Guide | Application Coordinator Guide | Operational reference for the package's Application Coordinator (ADPAC) — the site-level administrator. Narrower scope than SMG; covers a single coordinator role rather than all admin functions. | Package-specific coordinator workflows, option assignment, user setup tasks specific to the coordinator's responsibilities. | `user-manual` | ADPAC = Application Package Coordinator. A VA-specific role that exists at every VistA site. Title pattern `adpac.?guide`. |
| Manager's Manual | Manager's Manual | Role-specific manual for clinical or administrative managers. Covers supervisory functions and management-level menu options not present in the standard UM. | Reports, management queries, approval workflows, supervisory access options. | `user-manual` | Title pattern `manager.?s?\s+manual`. |
| Administrator's Guide | Administrator's Guide | Setup and configuration reference for system or application administrators. Covers parameter files, security keys, and option assignments at an administrative level. | Parameter file setup, security key list, option assignments, access control configuration. | `user-manual` | Title pattern `administrator.?s?\s+guide` or `admin\s+guide`. |
| Vendor Guide | Vendor Guide | Integration reference for third-party vendors connecting external systems to VistA. | Interface specifications, data formats, connection requirements, HL7 segment mapping, VistA API call sequences. | `user-manual` | Title pattern `vendor\s+guide`. Often covers the same ground as a BASE_HL7 doc; classified as `user-manual` because it is a how-to operational reference for a specific audience. |
| Readme / Patch Readme | Readme File | Short patch-specific note distributed informally with early KIDS builds. Predates the formal RN format. | Install sequence, dependencies, any pre/post-install instructions. Typically 1–3 pages. | `release-note` | Title pattern `read.?me`. Same intent as RN; classified identically. |
| Security Guide | Security Guide | Security configuration and compliance reference for the package. | Access controls, audit logging, security key assignments, VA security policy implementation, sensitive data handling. | `base-security` | Title pattern `security`. Infrastructure-category doc because it addresses site-wide security configuration rather than package operation. |
| HL7 / Interface Spec | HL7 Interface Specification | Specification for HL7 message interfaces implemented by the package. | HL7 message types, trigger events, Z-segment definitions, field mappings to FileMan, acknowledgment rules. | `base-hl7` | Title pattern `hl7` or `interface.?spec`. Infrastructure-category because HL7 interfaces span multiple packages and sites. |
| Setup / Configuration Guide | Setup or Configuration Guide | Installation-adjacent document covering parameter file configuration and initial site customization after install. | Parameter file values, site-specific option settings, initial configuration checklist. Narrower than IG; assumes install is done. | `base-setup` | Title pattern `set.?up` or `configuration`. |
| Developer Guide / Programmer Manual / API Manual | Developer / Programmer / API Reference | Internal developer reference for building against or extending the package. | Callable routines, integration agreements (ICRs), APIs, extension points, coding conventions for the package. | `base-dev` | Title pattern `developer`, `programming`, `programmer`, or `api\s+manual`. |
| Implementation Guide | Implementation Guide | System integration and deployment planning document. Broader scope than IG — covers workflow design decisions and integration with other VistA packages. | Site readiness criteria, workflow mapping, package interdependencies, implementation sequence for a multi-package rollout. | `base-impl` | Title pattern `implementation`. |
| Glossary / Dictionary | Glossary or Data Dictionary | Standalone terminology reference or data-element reference not embedded in a TM. | Term definitions, abbreviation expansions, data element names and descriptions. | `supplement` | Title pattern `\bglossary\b` or `\bdictionary\b`. |
| Troubleshooting Guide | Troubleshooting Guide | Diagnostic reference for resolving known errors and system alerts. Adjunct to the UM or TM. | Error message list, common failure modes with causes and resolutions, diagnostic procedures. | `supplement` | Title pattern `troubl.{0,3}shoot`. Note: "TROUBLE SHOOTING" (two words) appears in some titles — the regex handles this. |
| Flowchart / Checklist | Flowchart or Checklist | Process diagram or task verification list distributed as a standalone document. | Process flow diagrams, step-by-step verification checklists for install or configuration tasks. | `supplement` | Title patterns `\bflowchart\b` and `\bchecklist\b`. |
| Getting Started | Getting Started Guide | Introductory condensed reference for new users. Covers the most common tasks needed to get productive quickly. | First-day tasks, navigation orientation, most-used options, where to find more help. | `quick-ref` | Title pattern `getting\s+started`. |
| Tutorial | Tutorial | Hands-on exercise document with step-by-step scenarios. Not a comprehensive reference — used alongside a UM or TRG. | Scenario walkthroughs, practice exercises, annotated screenshots of key workflows. | `quick-ref` | Title pattern `\btutorial\b`. |
| FAQ | Frequently Asked Questions | Question-and-answer format reference for common issues, clarifications, and edge cases. | Questions grouped by topic with concise answers; pointers to the UM or TM for full detail. | `quick-ref` | Title pattern `frequently\s+asked` or `faq\b`. |
| *(unmatched)* | Unknown | No filename or title rule matched. | Ambiguous titles: menus, demos, presentations, patch follow-ups, meeting notes. | `UNKNOWN` | 25 unknowns in the current corpus — genuinely ambiguous; requires manual review and re-classification. |

---

### 6.3 DocType Buckets in the Published Site

How each `DocType` value surfaces to readers in the portal navigation:

| `DocType` value | Reader-facing label | Nav section | Typical count in corpus |
|---|---|---|---|
| `user-manual` | User Manual / User Guide | Primary reference | 563 |
| `technical-manual` | Technical Manual | Technical reference | 318 |
| `installation-guide` | Installation & Deployment | Getting started | 857 |
| `release-note` | Release Notes | Changelog | 735 |
| `quick-ref` | Quick Reference | Quick start | 19 |
| `change-page` | Change Pages | Corrections | 163 |
| `supplement` | Supplementary Docs | Appendices | 68 |
| `base-security` | Security | Infrastructure | 26 |
| `base-hl7` | HL7 Interface | Infrastructure | 24 |
| `base-setup` | Setup & Configuration | Infrastructure | 22 |
| `base-dev` | Developer / API | Developer reference | 46 |
| `base-impl` | Implementation | Infrastructure | 22 |
| `base-other` | Other Base Docs | Infrastructure | — |
| `unknown` | Uncategorized | Review queue | 25 |

---

### 6.4 Classifier Audit — TM, TRG, VDD

Three codes warrant attention before the next classifier pass:

| VA Code | Full name | Classifier result | Verdict | Action |
|---|---|---|---|---|
| **TM** | Technical Manual | `TECHNICAL_MANUAL` via filename `tm\.` + title `technical.?manual` | **Correct.** Both signal paths covered. | None. |
| **TRG** | Training Guide | `SUPPLEMENT` via title `training\s+guide` — but **no filename rule for `tg.` or `trg.`** | **Partial gap.** Title-named files classify correctly. Files whose filename contains `tg.` or `trg.` and whose title is generic (e.g. `pso_trg.docx` with title "Pharmacy") fall to `UNKNOWN`. | Add `(tg\.\|trg\.)` to `_FILENAME_RULES` → `DocType.SUPPLEMENT`. Add test in `test_classify.py`. |
| **VDD** | Version Description Document | `UNKNOWN` — **no filename rule and no title rule** | **Gap.** No path to classification. All VDDs hit `UNKNOWN`. | Decide bucket (recommend `release-note`). Add `vdd\.` filename rule and `version\s+description` title rule. Add tests. |

---

## 7. Application to the VistA Docs Library (VDL)

The VDL pipeline already mirrors the best industry practices in its data layer. Here is how the remaining pipeline maps to the models above.

### Current State (as of March 2026)
- **2,888 documents** fully enriched with 34-field YAML frontmatter
- **139 packages** → 139 local git repos populated
- **1,393 Markdown files** in `docs/` directories
- **CHANGELOG.md** per repo from 711 release notes
- **Zensical** static site generator building per-package sites
- **136/139 sites** building successfully (2 toml bugs + 1 AR/WS path bug pending fix)

### How the VDL Maps to the Industry Models

| VDL component | Industry equivalent | Closest model |
|---|---|---|
| 139 `vista-<pkg>/` repos | Product repos with `docs/` | HashiCorp / Microsoft federated |
| Zensical `zensical.toml` | `docusaurus.config.js` / `config.yaml` | Docusaurus / Hugo |
| YAML frontmatter (34 fields) | `toc.yml` + frontmatter metadata | Microsoft OPS |
| CHANGELOG.md from release notes | Changelog as first-class nav item | HashiCorp |
| `originals/` git history | Version branches / source of truth | Microsoft / Kubernetes |
| Portal site generator (planned) | learn.microsoft.com / developer.hashicorp.com | Microsoft / HashiCorp portal |

### Architectural Decisions for the Remaining Pipeline

#### A. Portal Aggregation Layer
The planned "Portal site generator" is the most important remaining item. Industry models:

- **Microsoft approach:** A `toc.yml` master file references all packages; OPS aggregates at build time
- **HashiCorp approach:** A Next.js app imports MDX content from all product repos at build time
- **Docusaurus approach:** A monorepo with all sites as plugins (works but scales poorly past ~50 sites)
- **Hugo approach:** A central Hugo site with `content/` as a symlink farm pointing to all repos

**Recommendation for VDL:** The Hugo monolithic portal approach is the best fit because:
1. Zensical is already generating per-package sites; a Hugo portal aggregates metadata and index pages
2. Hugo can read frontmatter from all 2,888 Markdown files and generate a package index, search index, and cross-package navigation without importing the full site content
3. Static, no Node.js server, trivially hostable on GitHub Pages

#### B. Versioning Strategy
The VDL has a different versioning challenge than typical software docs: VistA packages have patch histories (sequential patch numbers like `PSJ*5*381`), not semantic versions.

Industry mapping:
- **Kubernetes branch-per-release** — most analogous: one branch per KIDS patch, cherry-picks for corrections
- **Microsoft `ms.date` freshness** — the `pub_date` frontmatter field already serves this purpose

**Recommendation:** The git history importer (planned) should create commits in `pub_date` order per package, giving each repo a meaningful git history. This enables `git log` as a changelog and `git diff` between patches.

#### C. Search
At 2,888 documents across 139 packages, search is critical.

| Option | Cost | Quality | Effort |
|---|---|---|---|
| Algolia DocSearch | Free for open source | Excellent | Low — add script tag |
| Pagefind (static, Rust-based) | Free, self-hosted | Good for single sites | Medium — embed in Zensical |
| Lunr.js (client-side) | Free | Acceptable for small sites | Low |
| Meilisearch (self-hosted) | Server cost | Excellent | High |

**Recommendation:** Pagefind per-package sites. Algolia for the portal if open-source; Meilisearch self-hosted if VA-internal.

#### D. GitHub Actions CI Pipeline
Every merged PR should run:

```yaml
# Canonical VDL CI pipeline
jobs:
  build:
    - Validate YAML frontmatter (required fields: title, doc_type, package, pub_date)
    - Build Zensical site (fail on any error)
    - Run link checker (no dead internal links)

  publish:
    - Push built site to GitHub Pages (gh-pages branch)
    - Update portal search index
```

This mirrors Microsoft's OPS build validation and Kubernetes' Netlify preview model.

### Recommended VDL Pipeline End State

```
[GitHub Repos — 139 packages]
    ↓ (Zensical build per repo)
[Per-package static sites]
    ↓ (GitHub Actions on push to main)
[GitHub Pages — vista-<pkg>.github.io or custom domain]
    ↓ (Portal aggregator reads all repos' frontmatter)
[Portal — unified search + package index + cross-package nav]
    ↓ (Algolia or Pagefind search index)
[User-facing: browse by package, doc_type, patch, date]
```

This maps directly to the **HashiCorp model** (federated repos + centralized portal).

---

## 8. Key Risks and Mitigations

| Risk | Industry lesson | VDL mitigation |
|---|---|---|
| Dead links between packages | Microsoft uses absolute URLs within OPS | Use package-relative paths; link checker in CI |
| Stale docs after patches | Microsoft `ms.date` staleness alerts | `pub_date` frontmatter + CI freshness report |
| Navigation rot | All models auto-generate nav from frontmatter | Never hand-edit nav — generate from frontmatter always |
| Build time explosion | Google/Hugo: incremental builds | Zensical per-package builds in parallel; portal rebuilds only changed packages |
| Frontmatter drift | Microsoft enforces canonical frontmatter schema via OPS | Validate against `CANONICAL_FIELD_ORDER` in CI |
| Original document accessibility | All models keep source alongside built site | `originals/` directory in repo — Zensical links to them |
| Classifier gaps (VDD, TRG filename) | N/A | Fix rules in `classify/rules.py` before next pipeline run (see §6.4) |

---

## 9. Summary: What to Steal from Each Model

| Model | The one thing worth copying |
|---|---|
| **Microsoft** | Centralized portal + federated content repos + `ms.date` freshness tracking |
| **Google** | Code samples pulled from tested source, not hand-typed — apply to all MUMPS/M examples |
| **Meta/Docusaurus** | Versioning via directory copy; zero-cost GitHub Pages deployment |
| **HashiCorp** | Frontmatter-driven navigation; changelog as a first-class nav item |
| **Kubernetes** | Strict content type taxonomy enforced by CI; community PR preview builds |
| **Stripe** | Every page has one job; ruthless structural consistency |

---

*Sources:*
- [Microsoft Docs on GitHub (MicrosoftDocs org)](https://github.com/MicrosoftDocs)
- [Docs-as-Code — Write the Docs](https://www.writethedocs.org/guide/docs-as-code/)
- [What is Docs as Code? — Kong Inc.](https://konghq.com/blog/learning-center/what-is-docs-as-code)
- [AI is Transforming Documentation into a True Product](https://compositecode.blog/2025/12/04/ai-is-forcing-docs-to-grow-up/)
