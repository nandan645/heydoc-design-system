#!/usr/bin/env bash
# Rebuild the element board (and optionally the film) from source/gen into examples/.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT/source/gen"
python3 build.py >/dev/null            # note: also regenerates source/film.html (the board reuses film parts)
cp ../board.html "$ROOT/examples/element-board.html"
echo "✓ examples/element-board.html"
if [[ "${1:-}" == "--film" ]]; then
  cp ../film.html "$ROOT/examples/explainer-film.html"
  echo "✓ examples/explainer-film.html"
fi
python3 "$ROOT/scripts/check_tokens.py"
python3 "$ROOT/scripts/bundle.py"
