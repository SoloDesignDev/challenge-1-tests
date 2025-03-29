#!/bin/sh
set -e

echo "🚀 Starting test runner"
echo "📦 Cloning student repo..."
git clone "$REPO_URL" user
cd user
git checkout "$COMMIT_HASH"
cd ..

echo "📦 Installing test dependencies..."
pip install -r requirements.txt

echo "🧪 Running stage $STAGE_ID tests..."
pytest -q tests/stage-${STAGE_ID}.test.py --tb=short > result.log || true

cat result.log

if grep -q "failed=0" result.log; then
  echo "✅"
else
  echo "❌"
fi
