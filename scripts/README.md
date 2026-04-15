# Ad-hoc / one-off scripts

Utilities that are **not** part of the automated pipeline. They document
the history of the corpus and are kept so past operations are reproducible,
but they should not be invoked as part of a regular run.

| Script | Purpose | Status |
|---|---|---|
| `enrich_inventory.py`     | Builds `vdl_inventory_enriched.csv` from `vdl_inventory.csv` (parses titles, classifies doc types, pairs PDF↔DOCX, extracts patch identities). Called from the project README. | **Active** — rerun whenever the raw inventory is re-crawled. |
| `classify_vista_type.py`  | One-off: adds `system_type` + `cots_dependent` columns to the enriched inventory (11-value classification scheme). | Historical |
| `extract_monograph.py`    | One-off: extracts structured app profiles from the VistA Monograph DOCX. | Historical |
| `ingest_monograph.py`     | One-off: fetch/ingest/enrich the Monograph (bypasses pipeline because `app_code` is blank in source CSV). | Historical |
| `ingest_blank_appcode.py` | One-off: handle packages with blank `app_code` by assigning synthetic codes. | Historical |
| `crossref_monograph.py`   | One-off: cross-references enriched VDL inventory against Monograph data. | Historical |
| `add_toc_image_md.py`     | One-off: injected a Table of Contents + back-to-TOC links into ACKQ markdown. | Historical |
| `test_ackq_images.py`     | Exploration script for Docling image extraction on ACKQ DOCX. Not a pytest test (despite the name). | Historical |

Anything here worth graduating into the automated pipeline belongs under
`pipeline/` or inside `src/vista_docs/`.
