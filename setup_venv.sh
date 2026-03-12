#!/usr/bin/env bash
# =============================================================================
#  setup_venv.sh — vista-docs analysis environment
#  Creates a Python 3.12 venv with uv for the full VDL pipeline:
#    - fetch / ingest (Docling, python-docx, requests, PyYAML)
#    - corpus survey / manifest / analysis scripts (standard lib + extras)
#  Usage: bash setup_venv.sh [TARGET_DIR]
#         TARGET_DIR defaults to ./vista-docs-env
# =============================================================================
set -uo pipefail

# =============================================================================
#  CONSTANTS
# =============================================================================
PYTHON_VERSION="3.12"
DEFAULT_ENV_DIR="${HOME}/vista-docs/.venv"
ENV_DIR="${1:-$DEFAULT_ENV_DIR}"

# =============================================================================
#  HELPERS
# =============================================================================
has_cmd() { command -v "$1" >/dev/null 2>&1; }

info()  { printf '\033[1;34m[INFO]\033[0m  %s\n' "$*"; }
ok()    { printf '\033[1;32m[ OK ]\033[0m  %s\n' "$*"; }
warn()  { printf '\033[1;33m[WARN]\033[0m  %s\n' "$*"; }
die()   { printf '\033[1;31m[FAIL]\033[0m  %s\n' "$*" >&2; exit 1; }

# =============================================================================
#  PREFLIGHT — uv must be installed
# =============================================================================
if ! has_cmd uv; then
  die "uv not found. Install it first:  curl -LsSf https://astral.sh/uv/install.sh | sh"
fi

UV_VERSION_RAW=$(uv --version 2>/dev/null || true)
UV_VERSION=$(printf '%s' "$UV_VERSION_RAW" | head -1 | tr -d '[:space:]')
info "uv version: ${UV_VERSION:-unknown}"

# =============================================================================
#  CREATE VENV
# =============================================================================
info "Creating Python ${PYTHON_VERSION} venv at: ${ENV_DIR}"

if [[ -d "$ENV_DIR" ]]; then
  warn "Directory '${ENV_DIR}' already exists — skipping venv creation."
  warn "To recreate: rm -rf '${ENV_DIR}' && bash setup_venv.sh"
else
  uv venv "$ENV_DIR" --python "$PYTHON_VERSION" \
    || die "Failed to create venv. Is Python ${PYTHON_VERSION} available to uv?"
  ok "Venv created: ${ENV_DIR}"
fi

# Derive activate path (works for bash/zsh on macOS and Linux)
ACTIVATE="${ENV_DIR}/bin/activate"
[[ -f "$ACTIVATE" ]] || die "Activate script not found at: ${ACTIVATE}"

# =============================================================================
#  INSTALL PACKAGES
# =============================================================================
info "Installing packages into venv..."

# uv pip install targets the venv when VIRTUAL_ENV is set or --python is given.
# Using --python points directly at the venv interpreter — no activation needed.
PY_BIN="${ENV_DIR}/bin/python"

uv pip install \
  --python "$PY_BIN" \
  \
  `# ── Document conversion (ingest.py / Docling) ───────────────────────` \
  "docling>=2.0,<3" \
  \
  `# ── Document read/write (corpus_survey, toc_reconstruct) ────────────` \
  "python-docx>=1.1" \
  "python-frontmatter>=1.1" \
  "PyYAML>=6.0" \
  \
  `# ── HTTP fetch (fetch.py, fetch_guides.py) ───────────────────────────` \
  "requests>=2.32" \
  \
  `# ── Markdown processing ──────────────────────────────────────────────` \
  "mistune>=3.0" \
  \
  `# ── Data analysis / reporting ────────────────────────────────────────` \
  "tabulate>=0.9" \
  \
  `# ── Jupyter (optional but useful for ad-hoc corpus inspection) ───────` \
  "ipykernel>=6.0" \
  \
  || die "Package installation failed."

ok "All packages installed."

# =============================================================================
#  VERIFY KEY IMPORTS
# =============================================================================
info "Verifying key imports..."

VERIFY_SCRIPT="
import sys
failures = []
checks = [
    ('docling',           'docling'),
    ('python-docx',       'docx'),
    ('python-frontmatter','frontmatter'),
    ('PyYAML',            'yaml'),
    ('requests',          'requests'),
    ('mistune',           'mistune'),
    ('tabulate',          'tabulate'),
]
for pkg_name, module in checks:
    try:
        __import__(module)
        print(f'  OK  {pkg_name}')
    except ImportError as e:
        print(f'  FAIL {pkg_name}: {e}')
        failures.append(pkg_name)
sys.exit(1 if failures else 0)
"

VERIFY_RAW=$("$PY_BIN" -c "$VERIFY_SCRIPT" 2>&1 || true)
printf '%s\n' "$VERIFY_RAW"

# Check if any FAIL lines appeared
FAIL_COUNT_RAW=$(printf '%s' "$VERIFY_RAW" | grep -c '  FAIL' || true)
FAIL_COUNT=$(printf '%s' "$FAIL_COUNT_RAW" | tr -d '[:space:]')
FAIL_COUNT="${FAIL_COUNT:-0}"

if [[ "$FAIL_COUNT" -gt 0 ]]; then
  die "${FAIL_COUNT} import(s) failed — see above."
fi

ok "All imports verified."

# =============================================================================
#  FREEZE LOCKFILE
# =============================================================================
LOCKFILE="${ENV_DIR}/requirements.lock"
info "Writing lockfile: ${LOCKFILE}"
FREEZE_RAW=$(uv pip freeze --python "$PY_BIN" 2>/dev/null || true)
printf '%s\n' "$FREEZE_RAW" > "$LOCKFILE"
LOCK_LINES_RAW=$(wc -l < "$LOCKFILE" || echo 0)
LOCK_LINES=$(printf '%s' "$LOCK_LINES_RAW" | tr -d '[:space:]')
ok "Lockfile written (${LOCK_LINES} packages)."

# =============================================================================
#  DONE
# =============================================================================
printf '\n'
ok "Environment ready."
printf '\n'
printf '  Activate:   source %s\n' "$ACTIVATE"
printf '  Deactivate: deactivate\n'
printf '  Lockfile:   %s\n' "$LOCKFILE"
printf '\n'
printf '  To restore from lockfile later:\n'
printf '    uv venv %s --python %s\n' "$ENV_DIR" "$PYTHON_VERSION"
printf '    uv pip install --python %s/bin/python -r %s\n' "$ENV_DIR" "$LOCKFILE"
printf '\n'
