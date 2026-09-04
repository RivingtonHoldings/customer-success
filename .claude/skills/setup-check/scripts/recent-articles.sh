#!/usr/bin/env bash
# Lists the N most recently updated articles in the local help center mirror for one MLS.
# Usage: recent-articles.sh <baldwin|crmls> [N]
# Reads the YAML frontmatter that /sync-help-center writes (title, state, updated_at).
set -euo pipefail
mls="${1:-baldwin}"
n="${2:-5}"
dir="docs/help-center/${mls}"
if [ ! -d "$dir" ]; then
  echo "No mirror folder at ${dir}."
  exit 0
fi
state="${dir}/sync-state.json"
if [ -f "$state" ]; then
  last=$(python3 -c "import json,sys;print(json.load(open('$state')).get('last_run','unknown'))" 2>/dev/null || echo unknown)
  echo "Last sync: ${last}"
else
  echo "Last sync: never (no sync-state.json)"
fi
count=$(find "$dir" -maxdepth 1 -name '*.md' ! -name 'README.md' | wc -l | tr -d ' ')
if [ "$count" = "0" ]; then
  echo "No articles in ${dir}."
  exit 0
fi
echo "Articles in mirror: ${count}"
for f in "$dir"/*.md; do
  [ "$(basename "$f")" = "README.md" ] && continue
  updated=$(awk -F': ' '/^updated_at:/{print $2; exit}' "$f" | tr -d '"')
  title=$(awk -F': ' '/^title:/{sub(/^title: /,""); print; exit}' "$f" | sed 's/^"//; s/"$//')
  st=$(awk -F': ' '/^state:/{print $2; exit}' "$f" | tr -d '"')
  printf '%s\t%s\t%s\n' "${updated:-0000-00-00}" "${title:-$(basename "$f")}" "${st:-?}"
done | sort -r | head -n "$n" | awk -F'\t' '{printf "%s  %s  (%s)\n", substr($1,1,10), $2, $3}'
