# Literature review — to-do (proposal §1–§2)

Living list, carried over from the night loop of 10 Nov 2026. Results go into `review-matrix.md` (conventions in its header); Zotero tags and notes as described there. Strike or reorder freely.

## For the student — next steps (11 Nov)
1. **Optional SI downloads** (only if B1 needs more detail): Su 2022 AFM https://doi.org/10.1002/adfm.202204306 (Wiley → "Supporting Information" at the end) · Gou 2025 https://doi.org/10.1016/j.jechem.2024.09.047 (Elsevier → "Appendix A. Supplementary data").
2. **Download (T2, 13 Nov) into `manual download/`:** Rana 2025 Joule https://doi.org/10.1016/j.joule.2025.102167 (main text + SI: interfacial pH model, HER parameters) · optional Rana 2026 AEM https://doi.org/10.1002/aenm.202503630 (HER kinetic values on Zn).
3. **Download for §1 (T5, 13 Nov)** — gold/bronze OA but publishers block Claude: Wang 2025 https://doi.org/10.1016/j.enrev.2024.100117 (BESS accident counts, vent gas, suppression) · Olivetti 2017 https://doi.org/10.1016/j.joule.2017.08.019 (Li/Co supply numbers) · Feng 2018 https://doi.org/10.1016/j.ensm.2017.05.013 (paywalled; thermal-runaway temperatures, only if §1 needs them).
4. **Ask the group (WeChat, low priority):** sp²/sp³/C–O/C=O fractions from the XPS fit behind Zhang 2026 ACS Nano Fig. 2D — only needed if ND surface chemistry becomes a model parameter.

Done 11 Nov: Zotero cleanup (62 misplaced PDF copies on Shao DML59VLW → Trash; all had their own items with PDFs; Shao's own PDF attached); filtering scheme decided (`use-*` tags, criteria in `review-matrix.md` header).

Claude's side next: §2 prose section by section (§2.1 written 13 Nov); remaining searches only as targeted gaps right before the section that needs them (B1/D2 → §2.3, C1 → §1/§2.4).

## Targeted search round (from 13 Nov) — brief for the separate `/loop` session
The broad search is done; this round closes specific gaps, in the order the proposal needs them (§2.3 writing 18–24 Nov, §1 25–29 Nov).

**Each iteration**
1. Call `mcp__ccd_session_mgmt__get_usage`. 5-hour window ≥ 60 % → schedule a wakeup and wait for the reset (no work). Weekly "all models" ≥ 60 % → write a status line below and stop the loop (the proposal-writing session needs the rest).
2. Take the first open task T1–T9 below; do one task (or one batch of ≤ 4 papers) per iteration; tick it here with a one-line result.
3. Commit the touched files locally (no push).

**Rules** (CLAUDE.md applies in full)
- Bibliographic data from Zotero only, never from memory; add missing items by DOI first. Tags as in the `review-matrix.md` header: `lr-<matrix section>`, status, `CN`/`INT`, `rel-*`. **No `use-*` tags** — write proposals as "Proposed `use-*`" lines under the matrix section; the student decides in the writing session.
- Every number with its location (`Fig.`, `Tab.`, `p.`); `~` = read off a figure; `(calc)` = own calculation.
- Full texts: OA routes in `../notes/claude-notes.md` (Europe PMC, Springer SI, IOP/ECS via curl). Paywalled → add to "For the student" above (DOI + what is needed); the student downloads into `manual download/`, then `bash tools/pdf2txt.sh "Literature/manual download"`. Read the `.txt`, grep for the needed passages before reading whole papers.
- Matrix section numbers are the old topic labels: matrix §2.3 = NDs (proposal §2.4), matrix §2.4 = simulation (proposal §2.3).
- Write only to `Literature/` (matrix, this file, `triage.md`), `notes/parameters.md` (T6 only), Zotero and `refs.bib` (`tools\zotero2bib.ps1` from the PowerShell tool after each task that adds items). **Do not touch `Thesis Proposal/`** — another session writes there.

**Tasks**
- [x] **T1 (§2.3, = B1):** done 13 Nov — Mistry 2021 (reporting checklist), Shah 2020 (grid convergence at singularities), Cornish 2022 (validation survey), Jang 2021 (tip effect weak in 3D); no Zn-specific critique found; B1 synthesis + proposed `use-*` in matrix §2.4.
- [x] **T2 (§2.3, = D2 part 2):** done 13 Nov — Herrmann 2023 (ZHS/pH speciation, cathode), Zhang 2018 (HER as BV side reaction, COMSOL, acid), Rana 2025 Joule + Rana 2026 AEM (paywalled → student list); no coupled HER–pH–ZHS anode model in ZnSO₄ found; table + synthesis in matrix §2.4.
- [x] **T3 (§2.3, part of C1):** done 13 Nov (Europe PMC) — Han: 10 mM CuSO₄, 300–400 nm pores, effect only above limiting current, none at 1 M; Tikekar: needs fixed-anion fraction ~0.1 of salt, Li solid electrolyte theory; rows + §2.4 synthesis upgraded.
- [x] **T4 (§2.4, part of C1):** done 13 Nov (PolyU repository, published version) — layer 5.8 µm (1.6/14 µm worse); ζ not reported; 10¹² cm⁻² sites asserted without derivation in the main text; SI not read.
- [x] **T5 (§1, part of C1):** done 13 Nov — Mongird Tab. 7 read (Li-ion 271 $/kWh, 3500 cyc; Zn hybrid 265 $/kWh, RTE 0.72, TRL 5); Wang 2025, Olivetti, Feng blocked → student list; §1 synthesis updated.
- [ ] **T6 (§4/§5, = D2 part 1):** ZnSO₄ activity / osmotic coefficients up to ~2–3 mol kg⁻¹ (Pitzer & Mayorga 1974 and newer) → thermodynamic factor at 2 M; new row in `notes/parameters.md` with source and status.
- [ ] **T7 (= C2):** verify every † number, but only for items tagged `use-core` or `use-context`.
- [ ] **T8 (= C3):** resolve `origin-unknown` for `use-core`/`use-context` items; recount the CN/INT table for those items only.
- [ ] **T9 (optional):** 1–2 clearly relevant papers from Chinese-language journals (Zn separators, ND, or Zn deposition modelling), tagged `CN` — only if they add content.

When all tasks are ticked: one summary line here ("Targeted round finished <date>: …") and stop the loop.

## Open tasks (priority first)
B1 done (T1, 13 Nov); C1–C3 and D2 are scheduled in the targeted round above (T1–T8).
- [ ] **PDF processing (ongoing).** New files in `Literature/manual download/` → `bash tools/pdf2txt.sh "Literature/manual download"`; check for "Figure S1" captions before assuming an SI is included. Per paper: matrix row, §2.2 comparison-table fields (GF grade, Zn thickness → DOD, σ/t₊ with method and ΔV, Zn//Zn life at j/Q with GF control, CE, simulation setup), needs-access list, Zotero tag + note. Processed: everything in the folder as of 11 Nov (31 PDFs incl. 2 duplicate SI files, 2 Wiley .docx SI — read via `zipfile`, no conversion needed).
- [x] **B2 — test-condition practice for Zn anodes:** Li 2022 Joule, Yu 2023 (full text 11 Nov), Li 2022 soft shorts, Wu 2024, Dong 2022, Guo 2025 → covered in §2.1 ¶4 and §2.2 ¶6.
- [ ] **B3 — alternatives to GF (context, 5–8 papers):** cellulose, polymer membranes, ultrathin separators vs a GF control. Unverified leads: 10.1016/j.ensm.2021.10.002, 10.1002/adma.202304667, 10.1002/adfm.202316619, 10.1002/aenm.202101299, 10.1063/5.0214281. → short subsection in §2.2.
- [ ] **C1 — OA full texts of abstract-only items:** 10.1039/d5nh00172b · 10.1039/d5eb00142k · 10.3390/batteries9070387 · 10.1038/s41467-017-00519-2 · 10.3389/fchem.2022.899810.
- [ ] **C2 — verify every † number** in the matrix against abstract or full text.
- [ ] **C3 — resolve `origin-unknown` items** (10 left) → CN/INT; recount the table.
- [ ] **D1 — LaTeX draft of the §2.2 comparison table** (`Thesis Proposal/drafts/tab-separators.tex`, full-text rows, keys from `refs.bib`).
- [ ] **D2 — gaps from `triage.md`:** activity/thermodynamic-factor data for ZnSO₄ (Pitzer & Mayorga 1974 and newer) → T6; HER/ZHS modelling done (T2).
- [ ] **D3 — paragraph outline §2.1–§2.6** (claim · evidence with numbers · citation keys; ends with the gap statement; §2 order changed 12 Nov, mapping in the matrix header). In `../Thesis Proposal/drafts/outline-sec2.md`, one section at a time with student review: §2.1 (12 Nov) and §2.2 (13 Nov) reviewed and tagged; §2.3–§2.6 only as one-line paragraph plans, then prose.
- [ ] **D4 — consistency audit:** matrix vs `notes/parameters.md` and `paper-summary.md`.
- [ ] **D5 — σ–t₊ figure** (GF → modified, full-text rows), optional.

## Access notes
Europe PMC `fullTextXML` for OA papers; Springer SI via `static-content.springer.com`; Wiley SI blocked; IOP/ECS OA PDFs via curl — details in `../notes/claude-notes.md`. MDPI PDFs: `mdpi-res.com/d_attachment/...` with a browser user agent (mdpi.com/.../pdf is blocked). OA status and repository copies: OpenAlex `api.openalex.org/works/doi:<DOI>` (found Liu 2024 at PolyU). Elsevier/Cell (even gold/bronze OA) and DOAJ are blocked for curl and web-fetch → student list (13 Nov).
