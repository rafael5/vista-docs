#!/usr/bin/env bash
# =============================================================================
#  bootstrap.sh — Set up vista-docs pilot repo on a local machine
#
#  Creates the full directory structure, installs Python dependencies,
#  initializes git, and configures the GitHub remote.
#
#  Requirements:
#    - Python 3.10+ (Docling requires >=3.10)
#    - git
#    - pip
#    - GitHub account with 'vista-docs' repo created (public, empty)
#
#  Usage:
#    chmod +x bootstrap.sh
#    ./bootstrap.sh [--github-user YOUR_USERNAME] [--skip-docling]
#
#  After running:
#    1. Copy vdl_inventory.csv into scripts/
#    2. Run: python3 scripts/pilot_manifest.py --inventory scripts/vdl_inventory.csv
#    3. Run: python3 scripts/fetch.py --manifest scripts/manifest.json
#    4. Run: python3 scripts/ingest.py --manifest scripts/manifest.json --base-only
# =============================================================================

set -uo pipefail

# =============================================================================
# 1. DEFAULTS & ARGS
# =============================================================================

GITHUB_USER=""
SKIP_DOCLING=false
REPO_NAME="vista-docs"
REPO_DIR="$(pwd)/${REPO_NAME}"

for arg in "$@"; do
  case "$arg" in
    --github-user=*) GITHUB_USER="${arg#*=}" ;;
    --skip-docling)  SKIP_DOCLING=true ;;
    --help)
      echo "Usage: ./bootstrap.sh [--github-user=USERNAME] [--skip-docling]"
      exit 0
      ;;
  esac
done

# =============================================================================
# 2. HELPERS
# =============================================================================

info()  { echo -e "\033[0;34m[INFO]\033[0m  $*"; }
ok()    { echo -e "\033[0;32m[OK]\033[0m    $*"; }
warn()  { echo -e "\033[0;33m[WARN]\033[0m  $*"; }
fail()  { echo -e "\033[0;31m[FAIL]\033[0m  $*"; exit 1; }

has_cmd() { command -v "$1" >/dev/null 2>&1; }

require_cmd() {
  local cmd="$1"
  local hint="${2:-}"
  has_cmd "$cmd" || fail "'$cmd' not found. ${hint}"
}

# =============================================================================
# 3. PREREQUISITE CHECKS
# =============================================================================

info "Checking prerequisites..."

require_cmd git  "Install git: https://git-scm.com"
require_cmd python3 "Install Python 3.10+: https://python.org"
require_cmd pip3 "Install pip: python3 -m ensurepip"

PY_VERSION_RAW=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')" 2>/dev/null || echo "0.0")
# Version check using sort -V (correct; avoids string comparison bug)
version_gte() { printf '%s\n%s' "$2" "$1" | sort -V -C; }
if ! version_gte "$PY_VERSION_RAW" "3.10"; then
  fail "Python 3.10+ required (found $PY_VERSION_RAW). — Install from https://python.org"
fi
ok "Python $PY_VERSION_RAW"

# =============================================================================
# 4. DIRECTORY STRUCTURE
# =============================================================================

info "Creating repository structure..."

mkdir -p "${REPO_DIR}"/{scripts,raw} \
         "${REPO_DIR}"/docs/clinical/{cprs,tiu,adt} \
         "${REPO_DIR}"/docs/infrastructure/hl7 \
         "${REPO_DIR}"/archive/clinical/{cprs/{change-pages,release-notes,install,supplements,quick-ref},tiu/{change-pages,release-notes,install,supplements},adt/{change-pages,release-notes,install,supplements}} \
         "${REPO_DIR}"/archive/infrastructure/hl7/{change-pages,release-notes,supplements}

ok "Directory structure created at ${REPO_DIR}"

# =============================================================================
# 5. COPY SCRIPTS
# =============================================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

for script in pilot_manifest.py fetch.py ingest.py; do
  if [[ -f "${SCRIPT_DIR}/${script}" ]]; then
    cp "${SCRIPT_DIR}/${script}" "${REPO_DIR}/scripts/${script}"
    ok "Copied ${script}"
  else
    warn "${script} not found in ${SCRIPT_DIR} — copy manually"
  fi
done

# =============================================================================
# 6. PYTHON DEPENDENCIES
# =============================================================================

info "Installing Python dependencies..."

VENV_DIR="${REPO_DIR}/.venv"
python3 -m venv "$VENV_DIR"
# shellcheck source=/dev/null
source "${VENV_DIR}/bin/activate"

pip install --quiet --upgrade pip

# Core always-required deps
pip install --quiet requests pyyaml
ok "requests, pyyaml installed"

# Docling: large install (~1-2 GB with models), optional for scaffold mode
if [[ "$SKIP_DOCLING" == "false" ]]; then
  info "Installing Docling (this may take several minutes and ~1-2 GB)..."
  pip install --quiet docling
  ok "Docling installed"
else
  warn "Skipping Docling install (--skip-docling). Run in scaffold mode only."
  warn "Install later: pip install docling"
fi

# Freeze requirements
pip freeze > "${REPO_DIR}/requirements.txt"
ok "requirements.txt written"

# =============================================================================
# 7. GIT INIT
# =============================================================================

cd "${REPO_DIR}"

git init --quiet
ok "Git initialized"

# .gitignore
cat > .gitignore <<'GITIGNORE'
.venv/
__pycache__/
*.pyc
raw/
*.docx
*.pdf
.DS_Store
*.egg-info/
dist/
build/
GITIGNORE

# README
cat > README.md <<'README'
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
README

git add .
git commit --quiet -m "chore: initial vista-docs pilot scaffold"
ok "Initial commit created"

# =============================================================================
# 8. GITHUB REMOTE
# =============================================================================

if [[ -n "$GITHUB_USER" ]]; then
  REMOTE_URL="git@github.com:${GITHUB_USER}/${REPO_NAME}.git"
  git remote add origin "$REMOTE_URL"
  ok "Remote added: ${REMOTE_URL}"
  info "To push: git push -u origin main"
  info "Make sure the repo exists at: https://github.com/${GITHUB_USER}/${REPO_NAME}"
else
  warn "No --github-user provided. Add remote manually:"
  warn "  git remote add origin git@github.com:YOUR_USER/${REPO_NAME}.git"
fi

# =============================================================================
# 9. NEXT STEPS
# =============================================================================

echo ""
echo "================================================================"
echo "  vista-docs pilot ready at: ${REPO_DIR}"
echo "================================================================"
echo ""
echo "  Next steps:"
echo ""
echo "  1. Copy your inventory file:"
echo "     cp vdl_inventory.csv ${REPO_DIR}/scripts/"
echo ""
echo "  2. Build the manifest:"
echo "     cd ${REPO_DIR}"
echo "     source .venv/bin/activate"
echo "     python3 scripts/pilot_manifest.py \\"
echo "         --inventory scripts/vdl_inventory.csv \\"
echo "         --out scripts/manifest.json"
echo ""
echo "  3. Fetch documents (polite 1.5s delay between requests):"
echo "     python3 scripts/fetch.py --manifest scripts/manifest.json"
echo ""
echo "  4. Convert base documents first:"
echo "     python3 scripts/ingest.py \\"
echo "         --manifest scripts/manifest.json \\"
echo "         --base-only"
echo ""
echo "  5. Review output in docs/ — check frontmatter and patch history"
echo ""
echo "  6. Push to GitHub:"
echo "     git push -u origin main"
echo ""
