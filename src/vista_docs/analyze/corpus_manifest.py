"""
Corpus manifest builder: enumerate all documents with provenance and transformation metadata.

build_manifest(records, transformation_map, stub_paths, generated_at) → CorpusManifest
original_filename(doc) → str

-------------------------------------------------------------------------------
AXIOMS
-------------------------------------------------------------------------------

A.  ONE RECORD PER DOCUMENT.
    Every DocumentRecord in the input produces exactly one ManifestRecord.
    No records are skipped, merged, or de-duplicated. The manifest is a
    complete enumeration of the corpus.

B.  FILENAME CONVENTION FOR ORIGINALS:
      {app_code}_{safe_patch_id}_{doc_type_abbrev}_{title_slug}.md
    - safe_patch_id: patch_id with non-alphanumeric characters replaced by '_',
      leading/trailing '_' stripped. Omitted (along with its separator) if empty.
    - doc_type_abbrev: fixed abbreviation per doc_type (Axiom C).
    - title_slug: lowercase, non-alphanumeric replaced by '_', stripped,
      truncated to 40 characters.
    The resulting filename contains only [a-zA-Z0-9_-] plus the '.md' suffix.
    No double underscores.

C.  DOC TYPE ABBREVIATIONS:
      installation-guide → IG,  release-note → RN,  user-manual → UM,
      technical-manual → TM,    change-page → CP,   supplement → SUPP,
      base-dev → DEV,           base-hl7 → HL7,     base-security → SEC,
      base-setup → SETUP,       base-impl → IMPL,   quick-ref → QR,
      unknown → UNK.

D.  TRANSFORMATION CLASSIFICATION (in priority order):
      1. is_stub == True OR path in stub_paths → "stub"
      2. path in transformation_map            → use map value
      3. doc_type == "release-note"            → "release-note"
      4. doc_type == "change-page"             → "change-page"
      5. otherwise                             → "standalone"
    The transformation_map is built by the runner after running consolidation.

E.  SHA-256 IS COMPUTED FROM TEXT BYTES (utf-8).
    If DocumentRecord.text is empty, sha256 is the hash of the empty string —
    a deterministic sentinel value, not an error.

F.  MIGRATION STATUS STARTS AS "pending".
    git_commit_originals and git_commit_docs start as None.
    These fields are populated by the commit phase of the migration runner.

G.  REPO NAME: "vista-{app_code.lower()}"
    The target repository slug for a document in package PSO is "vista-pso".
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field

from vista_docs.analyze.consolidate import DocumentRecord

# ---------------------------------------------------------------------------
# Doc type abbreviations (Axiom C)
# ---------------------------------------------------------------------------

_DOC_TYPE_ABBREV: dict[str, str] = {
    "installation-guide": "IG",
    "release-note": "RN",
    "user-manual": "UM",
    "technical-manual": "TM",
    "change-page": "CP",
    "supplement": "SUPP",
    "base-dev": "DEV",
    "base-hl7": "HL7",
    "base-security": "SEC",
    "base-setup": "SETUP",
    "base-impl": "IMPL",
    "quick-ref": "QR",
    "unknown": "UNK",
}

_TITLE_SLUG_MAX = 40

# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class ManifestRecord:
    """One row in the corpus manifest — describes one document's provenance."""

    package: str
    """Package namespace (app_code), e.g. 'PSO'."""

    repo: str
    """Target repository slug, e.g. 'vista-pso' (Axiom G)."""

    original_path: str
    """Path within the target repo: 'originals/{doc_type}/{filename}'."""

    original_sha256: str
    """SHA-256 hex digest of the document text (utf-8 encoded, Axiom E)."""

    source_markdown_path: str
    """Filesystem path of the source markdown file."""

    doc_type: str
    doc_layer: str
    pub_date: str
    patch_id: str
    word_count: int

    transformation: str
    """
    How this document is handled in the migration (Axiom D):
    'consolidated-master' | 'consolidated-addendum' | 'standalone' |
    'release-note' | 'change-page' | 'stub'
    """

    consolidated_master: str
    """
    Path in docs/ of the consolidated master file this document feeds into.
    Non-empty only when transformation == 'consolidated-addendum'.
    """

    consolidated_role: str
    """'master' | 'addendum' | '' — role within the consolidation group."""

    git_commit_originals: str | None = None
    """Git SHA after the document is committed to originals/. None until committed."""

    git_commit_docs: str | None = None
    """Git SHA after the document's canonical form is committed to docs/. None until committed."""

    migration_status: str = "pending"
    """'pending' | 'originals_committed' | 'docs_committed' | 'verified'"""


@dataclass
class CorpusManifest:
    """The complete org-level traceability index for the VistA corpus migration."""

    generated: str
    """ISO 8601 timestamp string."""

    total_documents: int
    total_packages: int

    documents: list[ManifestRecord] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Filename helpers (Axiom B)
# ---------------------------------------------------------------------------


def _safe_patch_id(patch_id: str) -> str:
    """
    Convert a VistA patch ID to a filesystem-safe string.

    'PSO*7.0*507' → 'PSO_7_0_507'
    ''             → ''
    """
    if not patch_id:
        return ""
    return re.sub(r"[^a-zA-Z0-9]+", "_", patch_id).strip("_")


def _title_slug(title: str) -> str:
    """
    Convert a document title to a lowercase filesystem-safe slug (max 40 chars).

    'PSO Technical Manual' → 'pso_technical_manual'
    'Kernel 8.0: Systems Management (Binder)' → 'kernel_8_0_systems_management_bi'
    """
    s = title.lower()
    s = re.sub(r"[^a-z0-9]+", "_", s).strip("_")
    return s[:_TITLE_SLUG_MAX]


def original_filename(doc: DocumentRecord) -> str:
    """
    Generate the originals/ filename for a document (Axiom B).

    Format: {app_code}_{safe_patch_id}_{doc_type_abbrev}_{title_slug}.md
    The patch_id segment is omitted if doc.patch_id is empty.

    Args:
        doc: DocumentRecord with app_code, patch_id, doc_type, and title populated.

    Returns:
        Filesystem-safe filename string ending in '.md'.
    """
    parts = [doc.app_code]
    pid = _safe_patch_id(doc.patch_id)
    if pid:
        parts.append(pid)
    abbrev = _DOC_TYPE_ABBREV.get(doc.doc_type, "UNK")
    parts.append(abbrev)
    slug = _title_slug(doc.title)
    if slug:
        parts.append(slug)
    return "_".join(parts) + ".md"


# ---------------------------------------------------------------------------
# SHA-256 (Axiom E)
# ---------------------------------------------------------------------------


def _sha256(text: str) -> str:
    """Compute the SHA-256 hex digest of a UTF-8 encoded string."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Transformation classification (Axiom D)
# ---------------------------------------------------------------------------


def _determine_transformation(
    doc: DocumentRecord,
    transformation_map: dict[str, tuple[str, str, str]],
    stub_paths: set[str],
) -> tuple[str, str, str]:
    """
    Classify a document's migration transformation.

    Returns:
        (transformation, consolidated_master, consolidated_role)
    """
    # Stub check first (Axiom D priority 1)
    if doc.is_stub or doc.path in stub_paths:
        return ("stub", "", "")

    # Explicit map entry (priority 2)
    if doc.path in transformation_map:
        return transformation_map[doc.path]

    # Release notes and change pages always have fixed transformations (priority 3/4)
    if doc.doc_type == "release-note":
        return ("release-note", "", "")
    if doc.doc_type == "change-page":
        return ("change-page", "", "")

    return ("standalone", "", "")


# ---------------------------------------------------------------------------
# Manifest builder (Axiom A)
# ---------------------------------------------------------------------------


def build_manifest(
    records: list[DocumentRecord],
    transformation_map: dict[str, tuple[str, str, str]],
    stub_paths: set[str],
    generated_at: str,
) -> CorpusManifest:
    """
    Build the corpus manifest from document records.

    Args:
        records:            All DocumentRecord objects (text populated for SHA-256).
        transformation_map: {source_path: (transformation, consolidated_master, role)}
                            Built by the runner after running consolidation.
        stub_paths:         Set of source paths that are stubs (in addition to
                            records where is_stub=True).
        generated_at:       ISO 8601 timestamp string for the manifest header.

    Returns:
        CorpusManifest with one ManifestRecord per input document.
    """
    packages: set[str] = set()
    documents: list[ManifestRecord] = []

    for doc in records:
        transformation, cons_master, cons_role = _determine_transformation(
            doc, transformation_map, stub_paths
        )
        filename = original_filename(doc)
        original_path = f"originals/{doc.doc_type}/{filename}"
        sha = _sha256(doc.text)
        repo = f"vista-{doc.app_code.lower()}"
        packages.add(doc.app_code)

        documents.append(
            ManifestRecord(
                package=doc.app_code,
                repo=repo,
                original_path=original_path,
                original_sha256=sha,
                source_markdown_path=doc.path,
                doc_type=doc.doc_type,
                doc_layer=doc.doc_layer,
                pub_date=doc.pub_date,
                patch_id=doc.patch_id,
                word_count=doc.word_count,
                transformation=transformation,
                consolidated_master=cons_master,
                consolidated_role=cons_role,
            )
        )

    return CorpusManifest(
        generated=generated_at,
        total_documents=len(documents),
        total_packages=len(packages),
        documents=documents,
    )
