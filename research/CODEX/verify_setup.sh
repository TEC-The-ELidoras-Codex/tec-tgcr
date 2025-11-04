#!/usr/bin/env bash

# CODEX Quick Start Checklist
# Run this to verify your CODEX is set up correctly

echo "=== CODEX v1.0 Setup Verification ==="
echo ""

# Check directory structure
echo "Checking directory structure..."
for dir in core_theory nodes clusters _templates _refinements; do
  if [ -d "$dir" ]; then
    echo "✓ $dir/ exists"
  else
    echo "✗ $dir/ missing"
  fi
done
echo ""

# Check core files
echo "Checking core files..."
for file in README.md CODEX_INDEX.md GPT_IMPORT_GUIDE.md _templates/CODEX_CARD_TEMPLATE.md; do
  if [ -f "$file" ]; then
    echo "✓ $file exists"
  else
    echo "✗ $file missing"
  fi
done
echo ""

# Check card files
echo "Checking CODEX cards..."
cards=(
  "core_theory/CODEX_CHRONOSPHERE.md"
  "core_theory/CODEX_PAC_MAN_UNIVERSE.md"
  "nodes/CODEX_SYNTHETIC_INTROSPECTION.md"
  "nodes/CODEX_GUT_BRAIN_PHI_T.md"
  "clusters/CODEX_SLEEP_TOKEN_RAIN.md"
  "clusters/CODEX_TDWP.md"
)

for card in "${cards[@]}"; do
  if [ -f "$card" ]; then
    echo "✓ $(basename $card)"
  else
    echo "✗ $(basename $card) missing"
  fi
done
echo ""

echo "=== CODEX Setup Complete ==="
echo ""
echo "Next steps:"
echo "1. Read README.md (this directory)"
echo "2. Review CODEX_INDEX.md for navigation"
echo "3. Pick a reading path based on your interest"
echo "4. Use GPT_IMPORT_GUIDE.md to integrate with AI"
echo ""
echo "Questions? See README.md or CODEX_INDEX.md"
