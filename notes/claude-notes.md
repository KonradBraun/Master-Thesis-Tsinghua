# Notes for Claude — read before relying on assumptions

Short, only things a fresh session would otherwise get wrong. Not a log.

## Environment
- `www.comsol.com` is not reachable from this network — use `cn.comsol.com/...?lang=en_US`; `doc.comsol.com` works.
- Python: `py` (not `python`). `pdftotext` (poppler) is on PATH in Git Bash.
- Zotero MCP server times out at session start if Zotero isn't open yet → open Zotero before starting the session; otherwise the student reconnects it: `/mcp` → zotero → Reconnect (also works in the desktop app; Claude can't reconnect project servers itself).
- PowerShell `Invoke-WebRequest` to the Zotero local API fails ("connection closed") — use `curl.exe` instead.
- Zotero MCP **reads can be stale** (items added in Zotero desktop not visible) while writes still work. For current counts/items query the local API directly: `curl "http://localhost:23119/api/users/0/items/top?limit=100&format=json"` (header `Total-Results`).
- PDFs: convert with `bash tools/pdf2txt.sh <folder>` → `<folder>/txt/`, read the .txt, not the PDF (far cheaper). Render single pages only when figures matter.

## COMSOL (tcd, 6.3)
- Physics: "Tertiary Current Distribution, Nernst-Planck" is a group; pick the variant "Tertiary, Electroneutrality".
- With electroneutrality one species is eliminated (greyed out in Initial Values; its ν follows from the others).
- Closed cell + Stationary study → concentration level undetermined (got ~8300 instead of 2000 mol/m³). Use Time Dependent or a mean-concentration constraint.
- Electrode Surface potential is not `phis` but `tcd.phis_es<N>`.
- Default Reference Concentrations are 0[M] — must be set (else Nernst/mass action divide by zero).
- `.mph` is a zip: `modelinfo.xml` (version, physics, `lastComputationDate`) and `dmodel.xml` (settings) can be read without COMSOL — shows whether a model was actually solved after editing.
- 2 M ZnSO₄ is too non-ideal for dilute Nernst–Planck (σ, D_salt, t₊ not matchable with two ion D's). 6.3 has "Concentrated Electrolyte Transport" (Maxwell–Stefan, any charges); "Battery with Binary Electrolyte" is 1:1 only.

## LaTeX
- Poppler tools (pdftotext/pdftoppm/pdffonts) can't show the Chinese text of ThuThesis PDFs (Adobe-GB1 missing) — the text IS there. Check/render with PyMuPDF from the zotero-mcp env: `"$APPDATA/uv/tools/zotero-mcp-server/Scripts/python.exe"` (`import pymupdf`).
