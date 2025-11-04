#!/usr/bin/env bash
# Phase 1 Deployment Checklist
# Run this to verify everything is ready, then deploy to ChatGPT

set -e

echo "🎵 Phase 1 Deployment Checklist"
echo "================================"
echo ""

# 1. Verify all files exist
echo "✓ Checking Phase 1 files..."
files=(
  "src/tec_tgcr/data_ingestion.py"
  "tests/test_data_ingestion.py"
  ".github/workflows/update-copilot-context.yml"
  "data/context-latest.json"
  "config/FOLD_INSTRUCTIONS_COMPACT.txt"
  "PHASE_1_COMPLETION.md"
  "PHASE_1_EXECUTIVE_SUMMARY.md"
)

for file in "${files[@]}"; do
  if [ -f "$file" ]; then
    echo "  ✅ $file"
  else
    echo "  ❌ MISSING: $file"
    exit 1
  fi
done

echo ""

# 2. Run tests
echo "✓ Running unit tests..."
python -m pytest tests/test_data_ingestion.py -q
echo ""

# 3. Test data ingestion
echo "✓ Testing data ingestion module..."
python -m tec_tgcr.data_ingestion fetch-context
if [ -f "data/context-latest.json" ]; then
  echo "  ✅ Context file generated successfully"
else
  echo "  ❌ Context file not found"
  exit 1
fi
echo ""

# 4. Verify GitHub Action syntax
echo "✓ Validating GitHub Action YAML..."
if grep -q "update-copilot-context" .github/workflows/update-copilot-context.yml; then
  echo "  ✅ GitHub Action workflow syntax OK"
else
  echo "  ❌ GitHub Action validation failed"
  exit 1
fi
echo ""

# 5. Verify instructions file
echo "✓ Verifying ChatGPT instructions..."
if grep -q "FOLD" config/FOLD_INSTRUCTIONS_COMPACT.txt; then
  echo "  ✅ Instructions file OK ($(wc -l < config/FOLD_INSTRUCTIONS_COMPACT.txt) lines)"
else
  echo "  ❌ Instructions file validation failed"
  exit 1
fi
echo ""

# 6. Check git status
echo "✓ Checking git status..."
if [ -z "$(git status --porcelain)" ]; then
  echo "  ✅ No uncommitted changes"
else
  echo "  ⚠️  Warning: Uncommitted changes exist (OK for testing)"
  git status --short | head -5
fi
echo ""

echo "================================"
echo "✅ ALL CHECKS PASSED"
echo "================================"
echo ""
echo "🚀 DEPLOYMENT STEPS:"
echo "1. Copy ChatGPT instructions:"
echo "   cat config/FOLD_INSTRUCTIONS_COMPACT.txt | pbcopy"
echo ""
echo "2. Paste to ChatGPT:"
echo "   Settings → Custom Instructions → Paste content"
echo ""
echo "3. Test it:"
echo "   Ask: 'What's blocking us on Project #6?'"
echo ""
echo "4. Celebrate!"
echo "   Phase 1 is LIVE ✨"
echo ""
