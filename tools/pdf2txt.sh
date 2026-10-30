#!/usr/bin/env bash
# Convert PDFs to plain text so Claude can read them cheaply.
# Usage: bash tools/pdf2txt.sh "Literature/Potential"
# Output: <folder>/txt/<name>.txt — existing files are skipped (incremental).
# PDFs are copied to a temp file first, because pdftotext on Windows fails on non-ASCII file names.
set -euo pipefail
src="${1:?folder with PDFs}"
out="$src/txt"
mkdir -p "$out"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
n=0
for f in "$src"/*.pdf; do
  [ -e "$f" ] || continue
  t="$out/$(basename "${f%.pdf}").txt"
  [ -s "$t" ] && continue
  cp "$f" "$tmp/in.pdf"
  pdftotext -enc UTF-8 "$tmp/in.pdf" "$tmp/out.txt" && cp "$tmp/out.txt" "$t" && n=$((n+1))
done
# drop .txt files whose PDF was deleted
for t in "$out"/*.txt; do
  [ -e "$t" ] || continue
  [ -e "$src/$(basename "${t%.txt}").pdf" ] || { rm -f "$t"; echo "removed orphan: $(basename "$t")"; }
done
echo "converted $n new file(s) -> $out"
