# Current State — 30 Oct 2026 (last work on the project: 21 Oct)

## Supervisor
- **Decided (14 Oct):** COMSOL only, no DFT. Start by getting familiar with COMSOL.
- **18 Oct:** proposal must be in Tsinghua format (ThuThesis 选题报告); cover: Department of Mechanical Engineering, Mechanical Engineering, Master of Science.
- **Message sent 18 Oct** asking for: (1) approximate ND amount per separator (mg), (2) raw data of SI Fig. S5 and S6, (3) spacer/spring of the CR2032 cells (→ compressed separator thickness), (4) the paper's `.mph` file. **Answer (18 Oct):** talk to Dr. Yanmei Zhang first (first author, equal contribution, of the group's ND synthesis paper, ACS Nano 20 (2026) 20231; Tsinghua ME). She forwarded the questions to the former postdoc. **Answers 19 Oct** (→ `parameters.md`): ND 0.1–0.4 mg/separator, Φ10 mm, layer 30–50 µm on the fibres, zeta ND@GF −38.8 mV, stack Zn/sep/Zn, CP 50 µm. Raw S5/S6 + `.mph` in a few days → group `.mph` files in `COMSOL/Old models/` (20 Oct); raw data of SI Fig. S6 (Bruce–Vincent) in `data/figure S6/` (30 Oct, evaluated, see COMSOL models). S5 raw data: unknown. **Key estimate:** this loading gives fixed charge ≤ ~100 mol/m³, but ~3100 needed for t₊ = 0.69 → Donnan exclusion alone likely can't explain the measured t₊ (to test with model 03).
- Proposal deadline: **mid-December** (student, 30 Oct). Paper still under review (30 Oct).
- **Nobody who worked on the paper is left in the group** (student, 30 Oct): the former postdoc can provide data, but not how the experiments were done → don't plan on protocol questions.
- Still to ask later (supervisor): proposal length; her view on dendrite growth; manufacturing-chapter idea; the approach below.

## Approach — agreed with the student 30 Oct, not yet discussed with the supervisor
**Goal:** find out in simulation why ND@GF cells perform so much better (Zn//Zn 47 h → 3738 h at 2 mA/cm²) — rank candidate mechanisms by how much of the improvement each can explain, not predict cycle life.
1. **Done:** 1D baseline GF (models 01–02), ND layer with fixed charge (03) → fixed-charge/Donnan effect negligible at realistic loading.
2. **Model 04 (short):** virtual Bruce–Vincent → upper bound of the layer effect on the *measured* t₊ + limits of the method in Zn cells. t₊ = 0.69 is cited, not used as calibration target; t₊ only as scenario parameter; fixed charge X estimated physically (loading, surface groups, zeta).
3. **Main work: recreate the processes in the cell (2D)** — pore structure / current distribution (GF pores up to 14 µm vs NDs filling the voids; metric: uniformity of current density at the anode) · interface (nucleation, kinetics, passivation; parametric) · corrosion/HER (option; Tafel I_corr halves, Fig. 2f; COMSOL "Water-Based with Electroneutrality" + HER). Mechanics (puncture +18 %) only discussed. Optional: dendrite onset via Sand's time or phase field.
4. **If time is left:** full cells (open) · design study (ND loading/distribution) / manufacturing tolerances (RWTH link, below) · DFT only with the supervisor's OK (excluded 14 Oct).

**Framing of critique (student, 30 Oct):** the group's t₊ = 0.69 is questioned only through our own simulation results (model 04) — never as "miscalculated". The S6 raw-data check (below) is background, not a thesis statement.
Later, for the thesis: switch electrolyte to COMSOL 6.3 "Concentrated Electrolyte Transport" (2 M ZnSO₄ is too non-ideal for dilute Nernst–Planck) and compare both.

**Comparison with the paper's model (later):** same geometry with bumps on the anode; A = as in paper (0.5 V, NDs as holes) · B = same but constant current 2 mA/cm² · C = + concentration gradients and real parameters · D = + NDs as charged layer. Metric: current density along the anode (max/mean). Shows which part of the paper's effect survives.

**Proposed (17 Oct), not yet discussed with supervisor — RWTH link:** one thesis chapter on manufacturing tolerances / process window for the ND coating (UQ Module); automation only as method.

**Metrics instead of colour plots:** std. dev. of current density along the anode · max/mean Zn²⁺ flux · depletion depth. Claims: trends and mechanisms, not absolute accuracy.

**Improvements over the paper's model (SI §1.7):** NDs with physical properties · tertiary instead of secondary · realistic operating point (constant 2 mA/cm²) instead of 0.5 V · current density as result, not only field plots · quantitative metrics, mesh convergence · time-dependent · validated against measurements.

## COMSOL models (in `COMSOL/`)
- `Simulation_01_ZnZn_1D_test.mph` — free electrolyte, placeholders. Checked: profile 1987–2013 mol/m³, 73 mV — matches hand estimate. Lessons → `notes/claude-notes.md`.
- `02_ZnZn_1D_separator.mph` — **done (19 Oct), matches hand estimate:** t_plus 0.51 → cZn 1895–2105 mol/m³, 75.6 mV; t_plus 0.69 → ~1934–2066, 74.6 mV (kinetics dominate at i0 = 5 A/m²). Setup: L = 675 µm; D_Zn = D_salt/(2(1−t_plus)), D_SO4 = D_salt/(2·t_plus) → 3.34e-10 / 3.21e-10 m²/s at t_plus = 0.51 (fitted to D_salt = 3.27e-10; model σ ~3.5× too high, accepted: ohmic drop only a few mV); Separator node ε = 0.92, Tortuosity τ = 1.84 (from 2.83/5.67); parametric sweep over t_plus.
- `03_ZnZn_1D_ND_layer.mph` — **first results (19 Oct):** ND layer 40 µm (domain 1, at anode), fixed charge as immobile species cX (z = −1), Donnan initial values. 2 mA/cm², 1800 s: **GF profile identical for all X** (1905→2105; steady state has zero SO₄ flux). Only cZn inside the layer rises: at anode 1895 / 1905 / 1920 / 2165 / 2815 mol/m³ for X = 0 / 50 / 100 / 1000 / 3100. Realistic X ≤ ~100 → ~1 % effect. Voltage 75.63 / 75.56 / 75.48 / 74.12 / 71.23 mV (realistic X: −0.15 mV; group's nucleation overpotential differs by ~10 mV GF vs ND@GF — different quantity). **i_app sweep 2–35 mA/cm²** (cZn at anode, X = 0 / 100): 1895/1920 · 1473/1499 · 946/974 · 419/454 · 156/202 → realistic charge adds only 25–46 mol/m³ (cZn ≥ X/2 "buffer"); limiting current (~38 mA/cm², uncompressed GF) unchanged since GF profile unchanged; below i_lim no Sand's time in 1D. **Conclusion: fixed-charge mechanism negligible in 1D** (ideal solution, homogenised charge). Next: virtual Bruce–Vincent, then 2D.
- `04_ZnZn_1D_BruceVincent.mph` — **set up, not solved** (21 Oct): Save As of 03, only parameter `dV = 10[mV]` added. Still to do (guide: `comsol-guide-04.md`, 30 Oct): Electrode Surface 2 → potential `dV`, log output times incl. 600 s, tolerance 1e-6, sweep `X_ND` × `i0` (5 / 2000 A/m²), export point evaluations to `COMSOL/results/`. Own estimate to test: a 40 µm layer can raise the measured t₊ to at most ~0.53, even if perfectly selective; with i₀ = 5 A/m² the Bruce–Vincent formula is ill-conditioned (ΔV − η₀ ≈ 0.13 mV).
  Sweep now `i0` = 0.5 / 5 / 2000 A/m² (0.5 ≈ measured R₀ of the GF cell). Settings of 03/04 confirmed by screenshots (30 Oct): ES1 = Electric potential 0 V; Nernst E_eq + Butler–Volmer with mass action law → η is pure activation overpotential.

**S6 raw data evaluated (30 Oct, `data/figure S6/`, own evaluation with `tools/analyse_s6.py`: HF intercept = R_bulk, LF end of arc = R_total):** chronoamperometry 0.1–600 s (0.1 s steps) + EIS before/after (Z', −Z'' only, no frequency column).

| | GF | ND@GF |
|---|---|---|
| I(0.1 s) → I(600 s) | 68.3 → 39.8 µA (−42 %; still −4 %/100 s at 600 s; exp. fit τ ≈ 210 s) | 40.1 → 34.7 µA (−13 %, mostly in the first 10 s; ~steady at 600 s) |
| R_bulk before / after | 7.3 / 6.0 Ω | 1.85 / 1.92 Ω |
| R_total before / after | ~680–690 / ~1255–1280 Ω | ~376–388 / ~404–429 Ω |
| I·R_total before / after | 47 / 51 mV | 16 / 14 mV |
| t₊ recalculated (group formula, ΔV = 10 mV) | 0.52–0.53 (reported 0.51) | 0.99–1.15 depending on R read-off (reported 0.69) |

Findings: (1) Ohm's law needs ~47–51 / ~14–16 mV, not 10 mV → F13 confirmed. (2) ND@GF t₊ is ill-conditioned and not reproducible → 0.69 unusable as calibration target. (3) Transport alone (measured R_bulk, t₊ 0.2–0.5) gives only 0.5–4 % decay → measured decay is interfacial (GF R_total +85 %, ND@GF +6 %). (4) ND@GF R_bulk 1.85 Ω with σ = 2.94 S/m, A = 0.785 cm² → L ≤ ~430 µm, consistent with the compressed-thickness estimate; the GF cell's 7.3 Ω implies extra series resistance (cell-to-cell scatter, F15). Single cells, no repeats.
→ Consequences: see Approach (agreed 30 Oct). Why Bruce–Vincent fails here (own): R_interface is 50–200× R_bulk, so the transport signal is only ~1–4 % of the current and is buried by interface changes.
- Group's models `Old models/GF(1).mph`, `ND@GF(1).mph` (COMSOL 6.3, Apr 2025) — first look from the file contents, without opening in COMSOL: **only Electric Currents (AC/DC), one stationary study**, 2D (no axisymmetry found), terminals 0.5 V / 0 V, conductivities 3.5 and 2.15 S/m; ND@GF window title "diamond part removed" (NDs as holes). → no Secondary Current Distribution / diluted species as stated in SI §1.7, i.e. pure ohmic conduction. Verify in COMSOL.
- Office PC has COMSOL 5.6: model 01 rebuilt there (results after geometry fix not yet checked); 6.3 files can't be opened there.
- i₀ = 5 A/m² still a start value → calibrate on Fig. 3c/3d.

## Next steps
0. Add the group's files to the project · 1. COMSOL model 04: finish and solve virtual Bruce–Vincent (guide: `notes/comsol-guide-04.md`), then i₀ calibration · 2. start writing Ch. 3.4 (ion transport, t₊, Sand's time) · 3. motivation literature for Ch. 1 (student searches; put PDFs in `Literature/Potential`).

## Proposal timeline — agreed 30 Oct; deadline mid-December (assumed Mon 14 Dec)
As of 30 Oct: no chapter text yet (only headings in `data/chap0*.tex`).
- **30 Oct – 8 Nov:** add the group's files · solve + document model 04 · verify group model in COMSOL · write Ch. 3.4
- **9 – 15 Nov:** i₀ calibration (Fig. 3c/3d) · rest of Ch. 3 + Ch. 4 · supervisor meeting: research question + length
- **16 – 22 Nov:** first 2D step (group geometry, comparison models A/B) — start of the main simulation work · Ch. 2 + 5
- **23 – 29 Nov:** Ch. 6, 7 (preliminary results), 8, 1 → full draft to supervisor ~27 Nov
- **30 Nov – 14 Dec:** feedback, revision, ~1 week buffer, submission

## Data
Parameters with sources and status: `notes/parameters.md`. Requested from the group: see Supervisor. **Wishlist for the former postdoc (data only, proposal 30 Oct):** original SEM images of GF and ND@GF (S3 — pore structure for the 2D model) · raw voltage data Fig. 3c/3d (i₀ calibration) · raw Tafel data Fig. 2f (corrosion) · S5 raw data (conductivity). Note: SI §1.6 uses the **separator** area A in σ = L/(R·A) (size not stated) → raw S5 data give the area-specific resistance directly, independent of their L and A.
**No own lab measurements planned** (student, 30 Oct): data come from the group (former postdoc) or are estimates. Compressed GF thickness: ~430 µm estimate (Hess 2018; consistent with the ND@GF R_bulk in S6), 675 µm as the other sensitivity case.
Not requested (nice to have): zeta potential of the NDs, ND distribution through the GF thickness, which side faces the anode, repeat measurements.

## Tools and setup
- **COMSOL 6.3:** laptop, full licence (incl. Electrodeposition, Battery Design, Optimization, Uncertainty Quantification).
- **LaTeX:** proposal in `Thesis Proposal/proposal/` — ThuThesis v7.7.1 (original in `tools/thuthesis/`), proposal mode, English, `fontset=fandol` (→ `windows` for the final version after installing the Windows Chinese supplemental fonts), XeLaTeX (`.latexmkrc` + recipe in `.vscode/settings.json`), biblatex `thuthesis-numeric` + biber. In text: `\cite{}` = superscript (default), `\parencite{}` = inline [1] when the number is part of the sentence. Open on the cover: student ID, Chinese title, working title. Refresh references: `powershell -ExecutionPolicy Bypass -File tools\zotero2bib.ps1` (strips url/urldate).
- **Zotero 10 + MCP server** (v0.14.1, local writes): 105 top-level items (local API, 30 Oct) sorted into chapter collections + "Parameter sources (ZnSO4, GF)" + "Manufacturing (option)"; DFT papers in "4 Continuum Modelling / DFT (likely not needed)". MCP reads can be stale → query local API (see claude-notes). Small open items: Ma PhD thesis → item type Dissertation; Hess 2018 without PDF (arXiv version available); Cytiva catalog → type Report, number CY53855.
- PDFs: `bash tools/pdf2txt.sh "Literature/Potential"` (Git Bash) → `txt/`.
- Python via `py`; Remote Control on; sleep on mains power disabled.
- **Git repository:** private, `github.com/KonradBraun/Master-Thesis-Tsinghua`, branch `main` (set up 30 Oct). Tracks all notes and the LaTeX sources (`.tex` = latest text incl. formatting; PDF is rebuilt, not tracked). `.gitignore` excludes `.mph`/`.exe`, `Literature/Potential/`, the group's confidential files (`Literature/*.pdf|docx|png`, `data/` — the group's raw data go there) and LaTeX build output → **back up `.mph` and group files separately.** Push: done by the student (Claude's push is blocked by the permission check).

## To pass on to the group
Reference errors in the manuscript: [4] = [16] · [2] broken DOI (correct: 10.1002/aenm.202102707) · SI [1] incomplete · SI [3] mixes two Kresse & Furthmüller 1996 papers. Possible mismatch in Fig. 5c (check original). Further inconsistencies: paper-summary F13–F21.
