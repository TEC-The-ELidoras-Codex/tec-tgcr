#!/usr/bin/env bash
# tec_bundle_cli.sh - skeleton CLI for Resonance Bundle creation
# Usage: bash scripts/tec_bundle_cli.sh create --source <folder> --output <file> [--validate]

set -euo pipefail

CMD="$1" || true
shift || true

usage(){
  cat <<EOF
Usage: $0 create --source <folder> --output <file> [--validate]
       $0 help
EOF
}

create_bundle(){
  local SOURCE=""
  local OUTPUT=""
  local VALIDATE=false
  while [[ $# -gt 0 ]]; do
    case "$1" in
      --source) SOURCE="$2"; shift 2;;
      --output) OUTPUT="$2"; shift 2;;
      --validate) VALIDATE=true; shift 1;;
      *) echo "Unknown arg $1"; usage; exit 2;;
    esac
  done

  if [[ -z "$SOURCE" || -z "$OUTPUT" ]]; then
    echo "--source and --output are required"; usage; exit 2
  fi

  echo "[tec_bundle_cli] Creating bundle from $SOURCE -> $OUTPUT"

  # 1) Validate meta.yaml if requested
  if [[ "$VALIDATE" == "true" ]]; then
    echo "  - Validating meta.yaml against schema..."
    # placeholder: user can integrate jsonschema or other validators
  fi

  # 2) Build ZIP
  tmpdir=$(mktemp -d)
  cp -r "$SOURCE"/* "$tmpdir/"
  pushd "$tmpdir" > /dev/null
  zip -r "$OUTPUT" . > /dev/null
  popd > /dev/null
  rm -rf "$tmpdir"

  # 3) Compute evidence hash
  if command -v sha256sum > /dev/null; then
    echo "  - Computing evidence hash..."
    hash=$(sha256sum "$OUTPUT" | awk '{print $1}')
    echo "evidence_hash: $hash"
  fi

  echo "Bundle created: $OUTPUT"
}

case "$CMD" in
  create)
    create_bundle "$@" ;;
  help|--help|-h)
    usage ;;
  *)
    usage; exit 2 ;;
esac
