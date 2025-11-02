#!/bin/bash
# Push artifacts to OneDrive using rclone
# Requires: rclone configured with 'onedrive' remote
# Usage: ./scripts/push_to_onedrive.sh [--dry-run] [--source SOURCE] [--dest DEST]

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE="${1:-artifacts}"
DEST_REMOTE="${2:-onedrive:/Apps/TEC/artifacts}"
DRY_RUN=false

# Parse flags
while [[ $# -gt 0 ]]; do
    case $1 in
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --source)
            SOURCE="$2"
            shift 2
            ;;
        --dest)
            DEST_REMOTE="$2"
            shift 2
            ;;
        *)
            shift
            ;;
    esac
done

# Logging
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*"
}

# Check rclone installed
if ! command -v rclone &> /dev/null; then
    log "ERROR: rclone not found. Install via: https://rclone.org/install/"
    exit 1
fi

# Check onedrive remote configured
if ! rclone listremotes | grep -q "^onedrive:$"; then
    log "ERROR: 'onedrive' remote not configured."
    log "Run: rclone config create onedrive microsoft account type=onedrive"
    exit 1
fi

# Resolve source path
SOURCE_PATH="${REPO_ROOT}/${SOURCE}"
if [[ ! -d "$SOURCE_PATH" ]]; then
    log "WARNING: Source directory not found: $SOURCE_PATH"
    log "Creating $SOURCE_PATH..."
    mkdir -p "$SOURCE_PATH"
fi

# Sync
log "Syncing from $SOURCE_PATH to $DEST_REMOTE..."

RCLONE_OPTS=(
    --progress
    --stats=30s
    --exclude=".git/**"
    --exclude=".gitignore"
)

if [[ "$DRY_RUN" == "true" ]]; then
    log "[DRY RUN] Command:"
    log "rclone sync '${SOURCE_PATH}' '${DEST_REMOTE}' --dry-run ${RCLONE_OPTS[*]}"
    rclone sync "${SOURCE_PATH}" "${DEST_REMOTE}" --dry-run "${RCLONE_OPTS[@]}"
else
    log "Starting sync..."
    rclone sync "${SOURCE_PATH}" "${DEST_REMOTE}" "${RCLONE_OPTS[@]}"
    log "Sync complete."
fi

log "Done."
