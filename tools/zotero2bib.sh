#!/usr/bin/env bash
# Export all Zotero items (local API, Zotero must be running) to the proposal's refs.bib.
# Usage: bash tools/zotero2bib.sh
set -euo pipefail
cd "$(dirname "$0")/.."   # run from anywhere
out="Thesis Proposal/proposal/ref/refs.bib"
tmp="$(mktemp)"
start=0
while :; do
  chunk="$(curl -sf "http://localhost:23119/api/users/0/items/top?format=bibtex&limit=100&start=$start")" || { echo "Zotero not reachable"; exit 1; }
  [ -z "$chunk" ] && break
  printf '%s\n\n' "$chunk" >> "$tmp"
  start=$((start+100))
done
# drop url/urldate: otherwise GB/T 7714 prints every article as [J/OL] with access date (DOI is kept)
grep -vE '^\s*(url|urldate)\s*=' "$tmp" > "$out"; rm -f "$tmp"
echo "$(grep -c '^@' "$out") entries -> $out"
