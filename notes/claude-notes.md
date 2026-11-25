# Notes for Claude — read before relying on assumptions

Short, only things a fresh session would otherwise get wrong. Not a log.

## Environment
- `www.comsol.com` is not reachable from this network — use `cn.comsol.com/...?lang=en_US`; `doc.comsol.com` works.
- Python: `py` (not `python`). `pdftotext` (poppler) is on PATH in Git Bash.
- Zotero MCP server times out at session start if Zotero isn't open yet → open Zotero before starting the session; otherwise the student reconnects it: `/mcp` → zotero → Reconnect (also works in the desktop app; Claude can't reconnect project servers itself).
- PowerShell `Invoke-WebRequest` to the Zotero local API fails ("connection closed") — use `curl.exe` instead.
- Zotero MCP **reads can be stale** (items added in Zotero desktop not visible) while writes still work. For current counts/items query the local API directly: `curl "http://localhost:23119/api/users/0/items/top?limit=100&format=json"` (header `Total-Results`).
- Git: `git push` from Claude is blocked by the auto-mode permission check → student pushes. In PowerShell 5.1 `git commit -F -` with a here-string fails → write the message to a file in the scratchpad with the Write tool (never `Set-Content -Encoding utf8`: adds a BOM that lands in the commit subject, and later writes keep it).
- Group raw data (`data/`, git-ignored) are old binary `.xls` → read with `xlrd` (installed `--user`), run Python with `py -P` (`-I` hides user site-packages). Excel via COM hangs on this machine. EIS files: col 1 = Z', col 2 = −Z'' (Ω), no frequency column.
- Unattended/overnight work: `/loop` (self-paced) in the working session itself, with usage caps checked via `mcp__ccd_session_mgmt__get_usage` (Pro plan: 5-hour + weekly windows); wakeups are clamped to ≤ 1 h. Don't run loops in a session with a huge context — every wakeup re-reads it. Needs laptop awake, app and Zotero open; a permission prompt stalls it until morning.
- OA full texts: Europe PMC `rest/<PMCID>/fullTextXML` works; its `supplementaryFiles` endpoint returns HTTP 500. Springer SI loads from `static-content.springer.com/esm/art%3A<DOI url-encoded>/MediaObjects/<file>` (filename from the XML); Wiley SI (.docx) is blocked; IOP/ECS OA PDFs loaded with `curl.exe -A "Mozilla/5.0"` on 13 Nov but returned a bot-check page on 20 Nov (Telmasre, Zhang 2018) → student download. Europe PMC search can hang: use `curl --max-time` and retry singly.
- Finding OA copies: `api.openalex.org/works/doi:<DOI>` lists repository PDFs (found Liu 2024 at PolyU). MDPI PDFs only via `mdpi-res.com/d_attachment/...` with a browser user agent. Elsevier/Cell (even gold OA), DOAJ, OSTI full texts (mostly) and eScholarship block curl and web-fetch → student downloads. eScholarship works in the built-in browser after its bot check: fetch the PDF inside the page and render pages with pdf.js (cdnjs) onto a canvas, then screenshot — navigating to the PDF URL opens a save dialog for the student. RSC and Wiley (`pdfdirect`) show a bot check to curl and to the built-in browser (20 Nov) → student downloads. MDPI HTML tables (images on the page) are readable in the built-in browser via `javascript_tool` on `table` elements (Mongird Tab. 7).
- PDFs attached in Zotero but without a `.txt` in `Literature/`: the local API serves Zotero's full-text index — children of the item (`/items/<key>/children`) → attachment key → `/items/<attKey>/fulltext` (JSON `content`); grep it from a script instead of loading it.
- Wiley/Elsevier SI .docx: read `word/document.xml` via `zipfile`, then drop EndNote base64 lines. Some PDF→txt conversions turn µ into nothing ("µm" → "mm") and < / > into "o" / "4" — check units against the PDF.
- `py -I` also ignores `PYTHONIOENCODING` → use `sys.stdout.reconfigure(encoding='utf-8')` for non-ASCII output.
- Other sessions stage files in this repo (e.g. deletions) → always commit with an explicit pathspec (`git commit -F msg -- <paths>`); a plain `git commit` sweeps their staged changes in.
- Run `tools\zotero2bib.ps1` from the PowerShell tool — `powershell -File` from Git Bash only opens a shell.
- Student downloads named "SI …" can be main texts: check for "Figure S1" captions before assuming the SI is there.
- PDFs: convert with `bash tools/pdf2txt.sh <folder>` → `<folder>/txt/`, read the .txt, not the PDF (far cheaper). Render single pages only when figures matter.
- `pdf2txt.sh` deletes every `.txt` in `<folder>/txt/` without a same-named PDF. Texts from other routes (Europe PMC XML, Zotero-only PDFs, SI `.docx`) therefore live in `Literature/txt-extra/`; include it when searching all papers.
- **CNKI (Chinese theses/papers, 25 Nov):** outside the Tsinghua network www.cnki.net redirects to `oversea.cnki.net` (kns.cnki.net gives a certificate error); search and abstracts/TOCs work there, full texts only on the Tsinghua network (student downloads). Every new session hits a slider CAPTCHA → the student solves it in the browser pane (never Claude). Search URL `/kns8s/defaultresult/index?kw=<terms>&korder=SU` with `*` as AND (`纳米金刚石*锌离子电池`); results load via JS, titles contain zero-width characters (strip U+200B–200F, 2060–206F, FEFF); `fetch()` of `kcms2/article/abstract` links from the results page returns TOC + abstract (`&language=CHS` for Chinese titles). Wanfang also shows a CAPTCHA. Theses often are long versions of papers we cite (check supervisor = corresponding author).
- Paper .txt files can mislead: some bodies are garbled (shifted characters, e.g. Yang 2022 Nano Res. — only the abstract was readable), and page headers can split a value from its sentence (Gou 2025: GF t₊ 0.49). Before writing "not in the main text", search for synonyms and check the rendered page. Values credited to "via <review>" must be checked in the primary source (Shalumon mislabelled Bradac's samples).

## COMSOL (tcd, 6.3)
- Physics: "Tertiary Current Distribution, Nernst-Planck" is a group; pick the variant "Tertiary, Electroneutrality".
- With electroneutrality one species is eliminated (greyed out in Initial Values; its ν follows from the others).
- Closed cell + Stationary study → concentration level undetermined (got ~8300 instead of 2000 mol/m³). Use Time Dependent or a mean-concentration constraint.
- Electrode Surface potential is not `phis` but `tcd.phis_es<N>`.
- Default Reference Concentrations are 0[M] — must be set (else Nernst/mass action divide by zero).
- `.mph` is a zip: `modelinfo.xml` (version, physics, `lastComputationDate`) and `dmodel.xml` (settings) can be read without COMSOL — shows whether a model was actually solved after editing.
- An `.mph` open in COMSOL is locked — read it via `[IO.File]::Open(path, 'Open', 'Read', 'ReadWrite')` + `ZipArchive`.
- COMSOL's default temperature (Default Model Inputs) is **293.15 K** — set it explicitly.
- Cross-check for exported currents: reconstruct them from `phil`, `cZn` at the electrodes with the model's own Butler–Volmer (mass action: i = i0·[exp(fη_ref) − (c/c0)·exp(−fη_ref)], η_ref = φs − φl, exact T; `tools/analyse_bv04.py`). If a column is missing, ask for a re-export first (CLAUDE.md).
- Fixed charge as an extra species: Donnan jumps ≳ 10 mV at a layer boundary need interface mesh refinement (model 04, X = 10000 drifted 5 %).
- After switching an Electrode Surface from current to potential control, old plots of `tcd.phisext_es<N>` fail ("undefined variable") — delete them.
- 2 M ZnSO₄ is too non-ideal for dilute Nernst–Planck (σ, D_salt, t₊ not matchable with two ion D's). 6.3 has "Concentrated Electrolyte Transport" (Maxwell–Stefan, any charges); "Battery with Binary Electrolyte" is 1:1 only.

## LaTeX
- Build: `latexmk -xelatex -outdir=build main.tex` in `Thesis Proposal/proposal/` (same as the VS Code recipe; `forceRecipeUsage` is set because `main.tex` has `% !TEX program = xelatex`, which otherwise triggers one xelatex pass into the source folder without biber → "[?]" citations, stale `build/main.pdf`).
- Editing `.tex` via a Python script written from Bash: the tool collapses `\\` in heredocs → build backslashes with `chr(92)`, then check the replacement count.
- Poppler tools (pdftotext/pdftoppm/pdffonts) can't show the Chinese text of ThuThesis PDFs (Adobe-GB1 missing) — the text IS there. Check/render with PyMuPDF from the zotero-mcp env: `"$APPDATA/uv/tools/zotero-mcp-server/Scripts/python.exe"` (`import pymupdf`).
