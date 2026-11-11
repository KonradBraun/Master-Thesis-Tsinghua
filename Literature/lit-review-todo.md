# Literature review — to-do (proposal §1–§2)

Living list, carried over from the night loop of 10 Nov 2026. Results go into `review-matrix.md` (conventions in its header); Zotero tags and notes as described there. Strike or reorder freely.

## For the student — next steps (11 Nov)
1. **Optional SI downloads** (only if B1 needs more detail): Su 2022 AFM https://doi.org/10.1002/adfm.202204306 (Wiley → "Supporting Information" at the end) · Gou 2025 https://doi.org/10.1016/j.jechem.2024.09.047 (Elsevier → "Appendix A. Supplementary data").
2. **Ask the group (WeChat, low priority):** sp²/sp³/C–O/C=O fractions from the XPS fit behind Zhang 2026 ACS Nano Fig. 2D — only needed if ND surface chemistry becomes a model parameter.

Done 11 Nov: Zotero cleanup (62 misplaced PDF copies on Shao DML59VLW → Trash; all had their own items with PDFs; Shao's own PDF attached); filtering scheme decided (`use-*` tags, criteria in `review-matrix.md` header).

Claude's side next: D3 outline with `use-*` tags, then writing §4 and §2; B1/C1 only as polish.

## Open tasks (priority first)
- [ ] **PDF processing (ongoing).** New files in `Literature/manual download/` → `bash tools/pdf2txt.sh "Literature/manual download"`; check for "Figure S1" captions before assuming an SI is included. Per paper: matrix row, §2.2 comparison-table fields (GF grade, Zn thickness → DOD, σ/t₊ with method and ΔV, Zn//Zn life at j/Q with GF control, CE, simulation setup), needs-access list, Zotero tag + note. Processed: everything in the folder as of 11 Nov (31 PDFs incl. 2 duplicate SI files, 2 Wiley .docx SI — read via `zipfile`, no conversion needed).
- [ ] **B1 — finish:** find papers that critique FEM field maps in Zn papers; then final synthesis bullet in §2.4 "COMSOL inside Zn separator/coating papers" (10 papers + Telmasre 2025 counter-example done).
- [ ] **B2 — test-condition practice for Zn anodes** (5–8 papers): DOD/Zn utilisation, N/P, E/C ratio, cumulative capacity, CE protocols, symmetric-cell pitfalls, reporting standards. Still to read: 10.1016/j.joule.2022.06.002 (Li 2022, needs access), 10.1016/j.joule.2023.05.004 (Yu 2023, abstract only). Done: Li 2022 soft shorts, Wu 2024 capacity inflection. → rows in §2.1, sharper "test conditions" bullet.
- [ ] **B3 — alternatives to GF (context, 5–8 papers):** cellulose, polymer membranes, ultrathin separators vs a GF control. Unverified leads: 10.1016/j.ensm.2021.10.002, 10.1002/adma.202304667, 10.1002/adfm.202316619, 10.1002/aenm.202101299, 10.1063/5.0214281. → short subsection in §2.2.
- [ ] **C1 — OA full texts of abstract-only items:** 10.1039/d5nh00172b · 10.1039/d5eb00142k · 10.3390/batteries9070387 · 10.3390/en13133307 (cost/cycle-life for §1) · 10.1016/j.enrev.2024.100117 · 10.1038/s41467-017-00519-2 · 10.1038/srep07056 · 10.1126/sciadv.1600320 · 10.3389/fchem.2022.899810 · 10.1002/aenm.202401479 (repository copy).
- [ ] **C2 — verify every † number** in the matrix against abstract or full text.
- [ ] **C3 — resolve `origin-unknown` items** (10 left) → CN/INT; recount the table.
- [ ] **D1 — LaTeX draft of the §2.2 comparison table** (`Thesis Proposal/drafts/tab-separators.tex`, full-text rows, keys from `refs.bib`).
- [ ] **D2 — gaps from `triage.md`:** activity/thermodynamic-factor data for ZnSO₄ (Pitzer & Mayorga 1974 and newer); modelling of HER, corrosion, ZHS precipitation (2–4 papers).
- [ ] **D3 — paragraph outline §2.1–§2.5** (claim · evidence with numbers · citation keys; ends with the gap statement).
- [ ] **D4 — consistency audit:** matrix vs `notes/parameters.md` and `paper-summary.md`.
- [ ] **D5 — σ–t₊ figure** (GF → modified, full-text rows), optional.

## Access notes
Europe PMC `fullTextXML` for OA papers; Springer SI via `static-content.springer.com`; Wiley SI blocked; IOP/ECS OA PDFs via curl — details in `../notes/claude-notes.md`.
