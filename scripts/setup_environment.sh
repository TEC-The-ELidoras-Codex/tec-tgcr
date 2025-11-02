#!/bin/bash
# setup_environment.sh
# One-time setup script to install all dependencies for TEC workspace scripts
# Run this ONCE: bash scripts/setup_environment.sh

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*"
}

# Color codes
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

log "=========================================="
log "TEC Workspace Environment Setup"
log "=========================================="

# 1. Python packages
log "Installing Python packages..."
python3 -m pip install --upgrade pip setuptools wheel > /dev/null 2>&1 || true

PYTHON_DEPS=(
    "PyJWT"          # GitHub App tokens
    "requests"       # GitHub API
    "cryptography"   # GitHub App JWT signing
    "cairosvg"       # SVG to PNG conversion
)

for pkg in "${PYTHON_DEPS[@]}"; do
    log "  Installing $pkg..."
    python3 -m pip install "$pkg" > /dev/null 2>&1 || {
        log "  WARNING: Failed to install $pkg (may already be installed)"
    }
done

log "${GREEN}✓ Python packages installed${NC}"

# 2. System packages (macOS)
if [[ "$OSTYPE" == "darwin"* ]]; then
    log "Detected macOS. Checking Homebrew..."
    if ! command -v brew &> /dev/null; then
        log "Installing Homebrew..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi

    BREW_DEPS=("rclone" "git")
    for pkg in "${BREW_DEPS[@]}"; do
        if ! command -v "$pkg" &> /dev/null; then
            log "  Installing $pkg via Homebrew..."
            brew install "$pkg" || log "  WARNING: Failed to install $pkg"
        else
            log "  $pkg already installed"
        fi
    done
    log "${GREEN}✓ macOS packages checked${NC}"
fi

# 3. System packages (Linux)
if [[ "$OSTYPE" == "linux"* ]]; then
    log "Detected Linux. Checking apt packages..."
    
    LINUX_DEPS=("git" "build-essential" "python3-dev")
    
    # Check if we can use apt
    if command -v apt-get &> /dev/null; then
        # Try to install rclone
        if ! command -v rclone &> /dev/null; then
            log "  Installing rclone..."
            curl https://rclone.org/install.sh | sudo bash > /dev/null 2>&1 || \
                log "  WARNING: rclone install failed. Install manually: https://rclone.org/install/"
        else
            log "  rclone already installed"
        fi
        
        for pkg in "${LINUX_DEPS[@]}"; do
            if ! dpkg -l | grep -q "^ii  $pkg"; then
                log "  Installing $pkg via apt..."
                sudo apt-get install -y "$pkg" > /dev/null 2>&1 || \
                    log "  WARNING: Failed to install $pkg"
            else
                log "  $pkg already installed"
            fi
        done
    fi
    log "${GREEN}✓ Linux packages checked${NC}"
fi

# 4. Bitwarden CLI (optional but recommended)
log "Checking Bitwarden tools..."
if command -v bw &> /dev/null; then
    log "  ✓ Bitwarden CLI (bw) installed"
else
    log "  Bitwarden CLI not found. Install from: https://bitwarden.com/download/"
fi

if command -v bws &> /dev/null; then
    log "  ✓ Bitwarden Secrets Manager (bws) installed"
else
    log "  Bitwarden Secrets Manager not found. Install from: https://bitwarden.com/download/"
fi

# 5. Git hooks (optional)
log "Setting up Git hooks..."
if [[ ! -d "$REPO_ROOT/.git/hooks" ]]; then
    mkdir -p "$REPO_ROOT/.git/hooks"
fi

# Create a simple pre-commit hook if it doesn't exist
HOOK_FILE="$REPO_ROOT/.git/hooks/pre-commit"
if [[ ! -f "$HOOK_FILE" ]]; then
    cat > "$HOOK_FILE" << 'HOOK'
#!/bin/bash
# Pre-commit hook: warn if .env.local would be committed
if git diff --cached --name-only | grep -q ".env.local"; then
    echo "WARNING: .env.local is staged for commit. This file should be gitignored!"
    echo "Run: git reset HEAD .env.local"
    exit 1
fi
exit 0
HOOK
    chmod +x "$HOOK_FILE"
    log "  ✓ Pre-commit hook installed"
fi

# 6. Create .env.local from template if needed
log "Checking .env.local..."
if [[ ! -f "$REPO_ROOT/.env.local" ]]; then
    log "  No .env.local found. Creating from template..."
    cat > "$REPO_ROOT/.env.local" << 'ENV'
# Local environment variables (NEVER COMMIT THIS FILE)
# Use Bitwarden Secrets Manager to populate these:
#   bash scripts/secrets/generate_env_from_bws.sh

# GitHub
GITHUB_TOKEN=your_token_here

# Optional: Bitwarden
BWS_ACCESS_TOKEN=your_token_here

# Optional: Azure/OneDrive
AZURE_STORAGE_ACCOUNT=
AZURE_STORAGE_KEY=
ENV
    log "  ✓ .env.local created (EDIT THIS WITH YOUR TOKENS)"
    log "  ${YELLOW}→ Add your tokens to .env.local${NC}"
else
    log "  ✓ .env.local already exists"
fi

# 7. Summary
log ""
log "=========================================="
log "${GREEN}Setup Complete!${NC}"
log "=========================================="
log ""
log "Next steps:"
log "  1) Edit .env.local with your tokens"
log "  2) Configure OneDrive (if using):"
log "     rclone config create onedrive microsoft account type=onedrive"
log "  3) Test a script:"
log "     python3 scripts/archive_workspace.py --dry-run"
log ""
log "Scripts are ready to use:"
log "  • scripts/archive_workspace.py"
log "  • scripts/push_to_onedrive.sh"
log "  • scripts/export_brand_assets.py"
log "  • scripts/export_canon_bundle.py"
log "  • scripts/extract_embedded_png.py"
log "  • scripts/generate_run_manifest.py"
log ""
